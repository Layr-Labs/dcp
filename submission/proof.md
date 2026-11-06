# CST-128-S: capped shift testing with a sequential bit controller

## Theorem and source use

For every integer N>=2 and fixed s in Z/NZ, put n=ceil(log2 N), k=n+4,
and B=128N. The single algorithm CST-128-S below outputs the entire s with
unconditional probability greater than 29/32. On every execution branch,

    T = O(N n log2(n+2)),    S_C = O(n),    S_Q = O(n),
    Q <= min{128N, N(n+4)} <= 128*2^n.

The time bound includes classical bit operations, source cost, exact
Clifford+T gates, their generation and addressing, initialization, measurements,
reset, failed tests and output. Uniform envelopes for n>=2 are
2^n n log2 n, n, n, and 2^n, with exact growth indices [1,0,0,1].
For all n>=1 replace log2 n by max{1,log2 n}. Constants are absolute and
independent of N, s and outcomes. The fifth guarantee is epsilon(n)=0
with the exact clean-input error model in Section 6.

The stopping rule and cutoff proof materially reuse kaankolcu's CST-128,
submission f95bb4e2-3d08-4ca0-a34f-99841dca855a, evaluated commit
`6b7500d549149709fb089338c116904f210b23d1` in Layr-Labs/dcp.
Its `submission/proof.md` has SHA-256
`49e8e8d26cdedb4af196e3497ad1f9b41f9152f418734d89ae6100644e4cb73f`.
That proof declares O(N n^2) but already establishes O(N n log2(n+2)^2)
internally. The improvement here is to that stronger internal bound as well:
Section 4 gives a particular bit controller with only O(log(n+2)) work per
gate descriptor, not O(log(n+2)^2). No new probability or search principle
is claimed. The algorithm's quantum test and stopping rule are unchanged;
its counted controller is specified more tightly.

The explicit carry/borrow evaluators, exact Toffoli decomposition, streamed
address grammar and diagnostic arithmetic are adapted from our earlier
saved-copy candidate b45accfa-78b4-45f0-a9aa-b8e82ed22fd4, archived proof SHA-256
`9e7d2340eb23884cae46ed01eee00dfee4524f0df4aaa8710eba3c9e4d19e8e9`.
Its hosted validation/publication is separate from this proof and is not a
premise. Its saved-copy Grover algorithm, all-pass reflection, hybrid bound,
and O(n^2)-qubit batch are not part of CST-128-S. The earlier candidate's
source GordoAR 613ca17b-835c-4180-98af-b08f0c06c5bc supplied that search design;
no separate feature is imported directly from that source for this candidate.
The exact single-copy shift test and generic compute/swap/inverse construction
also occur in the prepared baseline at
`cdb1ebff130d861e2c61e9cf517ab66c0a56ca7a`, `submission/proof.md`.
All required arguments are reproduced below.

## 1. Complete program

Input is N in binary and access only to fresh independent copies

    rho_s = (1/N) sum_{x=0}^{N-1} |psi_{x,s}><psi_{x,s}|,
    |psi_{x,s}> = (|0,x> + |1,(x+s) mod N>)/sqrt(2).

The offset x, purification, inverse preparation and coherent source control
are unavailable and unused. Compute n, k=n+4 and B=128N. Store a global
acquisition count q=0. Enumerate classical candidates t=0,...,N-1.
For each candidate set j=0 and repeat:

1. If q=B, output 0 and halt, without requesting another copy.
2. Acquire one fresh copy (b,Y), increment q, and run the test below.
3. Measure/reset or discard all of this test's quantum registers. Retain its
   one-bit result. If it is minus, advance to the next candidate immediately.
4. Otherwise increment j. If j=k, output t and halt. Otherwise repeat.

If all candidates have been rejected, output 0 and halt. This last case has
zero probability on ideal inputs but makes the control flow total. The budget
is checked immediately before acquisition, not before reporting an acceptance.
An acceptance on copy B therefore succeeds without another budget check.
There are no restarts, retained copies, postselection or unbounded loops.
A test is always completed after acquiring its copy, even if q has just
become B. Its finite work is included in the resource count.

The test acts on the entire n-bit Y register by the exact permutation

    (b,y) -> (b, f_t(y)) if b=1, and (b,y) otherwise,
    f_t(y) = (y-t) mod N for y<N, and y for y>=N.

It applies H to b and measures b in the computational basis. Outcome 0 means
plus and outcome 1 means minus. Section 3 implements the permutation without
assuming an arithmetic oracle. Only one acquired copy is accessible at a time.

## 2. Exact test law, cutoff coupling, and success

For each source component the controlled permutation produces

    (|0,x> + |1,(x+s-t) mod N>)/sqrt(2).

If t=s the residue strings coincide and b is |+>, so plus is certain.
If t!=s the strings are distinct, the reduced state of b is I/2, and plus
has probability exactly 1/2. This holds for each x and therefore for rho_s.
Every acquisition is independent of previous samples, records and workspace.
Thus the same test law holds conditionally on every history that reaches
that acquisition. In particular consecutive tests of a wrong candidate have
independent fair outcomes. No measured copy is reused.

For analysis only, remove the budget check and let X be the resulting total
acquisitions. This finite auxiliary program stops no later than candidate s.
On reaching a wrong candidate, the number of tests is a geometric waiting
time truncated at k, with conditional mean

    sum_{j=0}^{k-1} 2^(-j) = 2(1-2^(-k)) < 2.

The correct candidate requires k tests if reached. By linearity of expectation
and by bounding each reach probability by 1,

    E[X] <= 2(N-1)(1-2^(-k)) + k < 2(N-1)+k
          = 2N+n+2 <= 4N.                                   (1)

For the last step, n<=N and 2<=N for every N>=2. For example 2^(N-1)>=N
by induction implies n<=N-1, which is stronger than needed.
Conditioned on reaching any wrong t, acceptance has probability 2^(-k).
A union bound over at most N-1 such candidates gives

    Pr[uncapped wrong output] <= (N-1)2^(-k) < 1/16,           (2)

since N<=2^n and k=n+4. Correct acceptance is certain if s is reached.

One can couple the programs by presampling a finite array of independent
test results for each candidate and test number: all plus at t=s, independent
fair bits at other t. By the conditional test law this reproduces both
programs' output and acquisition distributions. The actual algorithms do
not generate or store this array. They follow the same path until a budget
halt. If X<=B, the capped program finishes the same tests and has the same
answer; in particular equality is allowed by the order in Section 1.

For a nonnegative random variable, E[X]>=B Pr[X>B], since X>=B on that event.
Thus (1) implies Pr[X>B]<=E[X]/B<=1/32. Combining this with (2),

    Pr[CST-128-S outputs s]
      >= 1 - (N-1)2^(-k) - [2(N-1)(1-2^(-k))+k]/(128N)
      > 29/32 > 2/3.                                        (3)

There is no assumption of independence between the two bad events. Output
0 at the budget halt can only help when s=0. This is unconditional success
for every fixed N,s, including N=2, not an average or postselected statement.

## 3. Linear exact arithmetic and clean workspace

The test uses a quantum n-bit copy T of the classical candidate t and a flag
v set to 1. Load them by indexed X gates into fresh zero qubits. The
permutation never changes T or v; clear them with the same X gates after
use. This is O(n) gates and O(n) additional qubits, fully counted. Keeping
the constants in these basis registers lets the same finite evaluator
grammar work for all candidates without an instance-dependent gate list.
N uses at most n+1 classical bits, also when N=2^n. Work at width w=n+1.

### 3.1 Fixed-width Boolean scans

Work at width w=n+1 with leading-zero extension of y and t. An addition scan
on inputs a_i,b_i uses c_0=0 and, for i=0,...,w-1,

    u_i = a_i XOR b_i,
    z_i = u_i XOR c_i,
    c_{i+1} = (a_i AND b_i) XOR (u_i AND c_i).

The terms in the last XOR cannot both be 1. A subtraction scan uses d_0=0
and

    u_i = a_i XOR b_i,
    z_i = u_i XOR d_i,
    d_{i+1} = ((NOT a_i) AND b_i)
               XOR ((NOT u_i) AND d_i).

The two borrow terms are also disjoint. These recurrences prove the sum
or difference modulo 2^w and the final carry or borrow by induction on i.
In particular final subtraction borrow is [a<b] for unsigned w-bit inputs.
Comparison, addition, subtraction, bitwise masking and bitwise selection
therefore each use O(w) Boolean gates and wires. Selection between a and b
under flag e is a_i XOR (e AND (a_i XOR b_i)). Each bit has a constant-size
NOT/XOR/AND block; its size does not depend on N or n.

### 3.2 Total permutations on all computational basis inputs

The test loads t into a computational-basis register and sets v=1. For the
total extension on arbitrary flag inputs, set h=v AND b AND [t<N] AND [y<N].
A Boolean evaluator F^- produces an n-bit result:

    d = y-t mod 2^w,       beta = [y<t],
    z = d + beta*N mod 2^w,
    F^-(t,b,v,y) = low_n(z) if h=1, and y otherwise.             (A)

The mask beta*N is formed bitwise from the stored bits of N. If h=1 then
0<=y,t<N, so -N<y-t<N and z is precisely (y-t) mod N, lying below N.
The leading bit of z is then zero. If h=0, the arithmetic values, even on
invalid inputs, are ignored by the final selection. All scratch values
are nevertheless computed and uncomputed without measurement.

The inverse evaluator F^+ uses

    e = y+t in w bits,      gamma = [e>=N],
    z = e-gamma*N mod 2^w,
    F^+(t,b,v,y) = low_n(z) if h=1, and y otherwise.             (B)

For h=1, e<=2N-2<2^w, so the sum does not overflow and one subtraction
suffices. Both maps preserve the valid and invalid y ranges. For v=[t<N]
and either value of b, F^+ and F^- are mutual inverse permutations of all
n-bit y. The [t<N] term in h makes their definitions inverse also for arbitrary
flag inputs, at the cost of one linear scan. Since the classical candidate
always satisfies t<N, v=1 is correct on every test performed by this algorithm.
There are a fixed number of width-w scans in (A) and (B), irrespective of
n, with no multiplication of quantum words. The only products by N here
are Boolean masks. Thus both evaluators have O(n) Boolean gates and wires.

### 3.3 Clean reversible evaluation and in-place permutation

Implement every Boolean gate into a fresh zero wire while retaining its
inputs. AND uses Toffoli, XOR uses at most two CNOTs, and NOT uses X and
CNOT. If both AND inputs name the same wire, copy it with CNOT instead;
there is no Toffoli with coincident controls. Constants use zero wires or X.
After computing a result, XOR its bits
into a target z and reverse the whole computation. This implements

    E_F: |t,b,v,y,z,0> -> |t,b,v,y,z XOR F(t,b,v,y),0>

with O(n) gates and O(n) scratch qubits, on arbitrary quantum states by
linearity. The intermediate values are quantum wires, not a classical
list of their values. This also works for arbitrary initial target z.

To apply F^- in place to y, take a clean n-bit target z, apply E_{F^-},
swap y and z using 3n CNOTs, and apply E_{F^+} with the new y as input and
the old y as target. The old y clears because F^+(F^-(y))=y. The result is
exactly the controlled permutation C_t, including identity outside valid
ranges. Interchanging plus and minus gives its inverse. The same O(n)
workspace is reused between these evaluations and between acquired copies.
This construction has O(n) gates, including copying, swap and uncomputation;
it is not merely a gate bound for a nonreversible forward calculation.

### 3.4 Exact Clifford+T and resetting

For a self-contained exact Toffoli decomposition, for bits a,b,c the integer
identity

    4abc = a+b+c -(a XOR b)-(a XOR c)-(b XOR c)
                   +(a XOR b XOR c)

holds in all eight cases. Compute its four parity expressions into four
clean bits with CNOTs. Apply T to a,b,c and the triple parity, and T^dagger
to the three pair parities. Reverse the parity computation. The phase is
exp(i*pi*abc), which is CCZ. Conjugating the target by H gives Toffoli.
Use T^dagger=T^7 if only forward T is primitive. This is a fixed-size exact
Clifford+T circuit with four reusable ancillary qubits. SWAP, X, Z and H
also have fixed exact implementations in the allowed gate set.
No approximate rotations, QRAM, or random source oracle are used.

The arithmetic finishes with all target and work qubits clean. After H and
the outcome measurement, measure every remaining source qubit and use an X
conditioned on its measurement to reset it to zero. A single classical
outcome bit suffices while scanning the register. Initialization, these
measurements, outcome storage, conditional resets, and releasing/reusing the
allocation each cost at most O(n log(n+2)) work. The basis candidate T and
v are also cleared as described above. No purification is stored or reset.

## 4. A concrete sequential bit controller

This section specifies the implementation change responsible for the time
improvement. It does not give O(1) cost to an n-bit word, a native register,
or random-access instruction. Its classical controller is a fixed finite
multitape bit machine with local read/write/move operations, plus the
explicitly charged interface to indexed classical data and quantum wires.
All stored tape cells count towards S_C. A local scan has one unit of
fixed-size logic per step; an indexed access still pays its full address
length. This uses the distinction in the rules between fixed-size logic
and an indexed memory access.

### 4.1 Wire layout and instruction grammar

The evaluators consist of a fixed number of ripple and bitwise sweeps.
Reserve a fixed number of wire blocks, each of size c(n+1) for a fixed
integer c. Within each block, the wires for bit i have addresses

    base + c*i + d,

where d ranges over a fixed finite set. Gates read the current bit's
inputs and at most the preceding carry or borrow. Selection reads the
matching positions of earlier blocks. Boundary carries and leading zeros
have named wires. This describes addition, subtraction, masking, comparison
and selection by a constant-size list of templates with O(n) repetitions.
The single-copy clean evaluator's reverse is obtained by reversing sweep
order, bit order, and the constant-sized template order. The target-copy
and swap sweeps are equally explicit. Reversing the NOT/XOR/AND gates is
exact. Every fixed Toffoli expansion has a fixed inverse ordering when
needed. No addresses of intermediate values are kept in a table.

Each loop maintains a sweep identifier, a direction, a position i, a
constant-size within-template state and a constant number of current
wire-address words. A successor bit block changes these addresses by
fixed constants. Starting the reverse pass uses base+c*(w-1)+d, obtained
by a fixed number of shifts and additions of O(log(n+2))-bit integers.
Circuit calls have constant nesting depth and finitely many block bases.

### 4.2 Cost of one descriptor without a nested address charge

Choose an index-word width ell=ceil(log2(C_0(n+2))) for a fixed C_0 large
enough for every wire and block address. Bounds on circuit size and memory
below permit this absolute choice. Use a fixed number of separate classical
tape tracks for these ell-bit words, with boundary markers and heads
returned to a designated boundary after each arithmetic operation.
An increment, decrement, addition, subtraction, comparison, or copy of
such a word is a ripple scan with a one-bit carry/borrow or equality state.
A bounded number of heads move one cell per step. It costs O(ell) local
bit operations including return to the boundary, and O(ell) stored bits.
Multiplication by a fixed c is a fixed number of shifts/additions, also
O(ell). The finite template state is part of the machine's finite control.
An index-word bit is read at its current tape head, not through an array
lookup using a newly computed binary address for that bit.

To emit a constant-arity gate, copy its current address words and opcode
into a descriptor by these scans. Send this descriptor to the gate interface
and pay ceil(log2(M+2)) per wire address as stipulated. An indexed read of
a bit of the stored input N also costs this amount. A template uses only
a fixed number of such external accesses; the constant gate decomposition
multiplies this number by a constant. All interface and descriptor work is
O(ell+log(M+2))=O(log(n+2)) per gate. We charge each gate even when its
value is identity on some computational-basis branches.

There is no circular free lookup: the O(ell) local steps implement index
arithmetic explicitly. Simulating every local tape step with a random-access
array instruction would introduce another logarithm. That different
simulation is exactly the overhead avoided here. Nor is an O(n)-bit
counter processed inside every gate's descriptor loop. The controller has
separate finite loops for the long counters below.

### 4.3 Long counters, input bits, and total classical work

N, t, B and q occupy O(n) bits each. Allocate n+1 bits for classical t so
the terminal value N is representable even when N=2^n; only valid candidates
are loaded into the n-qubit register T. B is computed by a seven-bit left
shift, so q and B have at most n+8 bits. Each budget comparison and increment of q
is a bit scan costing O(n), or O(n log(n+2)) even if every bit access to these
long words is charged as indexed. There is one of each per test, plus at
most one terminal comparison. Incrementing t and comparing it with N costs
O(n log(n+2)) per candidate, with at most N candidates. The j and k counters
have O(log(n+2)) bits, and even fully indexed scans for them cost
O(log(n+2)^2)=O(n log(n+2)) per test. Load and clear T by scanning the n bits
of classical t, with one addressed X per set bit. Read bits of N in the
fixed arithmetic templates with charged indexed accesses. These operations
are O(n log(n+2)) per test, not per elementary quantum gate.

Compute n by scanning the binary input, detecting powers of two to obtain
ceil(log2 N), then compute k, B, ell and the fixed block bases. Elementary
bit scans and the short-word arithmetic just specified give
O(n log(n+2)) initialization work and O(n) storage. Integer precision is
exact; there are no transcendental functions, synthesis tolerances, or
long products. Writing the output t or 0 takes O(n log(n+2)) at most.

## 5. Joint all-branch resources

The Boolean formulas have O(n) gates and O(n) intermediate quantum bits.
Reversible evaluation, the swap, inverse evaluation and exact decomposition
preserve these linear bounds. Add the n+1 source qubits, T, v and constant
scratch. The peak is S_Q=O(n); the same allocation is reused for every test.
There are no growing quantum histories or batches. Classical storage is
N,t,q,B,j,k, a constant number of ell-bit fields and descriptors, measurement
bits and output. Thus S_C=O(n), with no stored circuit listing or transcript.
These allocation bounds hold independently of the outcomes, so M=O(n).
They justify the address length used in Section 4 without assuming a time
bound or successful execution.

Each completed test costs O(n log(n+2)) total charged work. This includes
its n+1 acquisition charge, gate emission/execution, counter scans and reset.
There are at most B=128N tests, at most Nk tests by the candidate loops,
at most N candidate transitions, and at most one terminal budget check.
Even a history of adversarial outcomes cannot exceed these bounds. Hence

    Q <= min{128N,N(n+4)},
    T = O((Q+N+1)n log(n+2)) = O(N n log(n+2)).                (4)

In particular (4) is a worst-case bound, not an expected bound inferred from
(1). The expectation appears only in the probability proof for the explicit
cap. Source, reset, failed acquisitions/tests and the capped failure branch
are all included. N<=2^n yields O(2^n n log2 n) for n>=2; n=1 has constant
work. One absolute outer constant gives C*2^n*n*max{1,log2 n} for all n>=1.
No finite-size leading gate or runtime constant is asserted.

## 6. Indices and the error model

For B_T(n)=2^n n log2 n and B_samples(n)=2^n on n>=2,

    log2 B_T = n + log2 n + log2 log2 n = n+O(log n),
    log2 B_samples = n.

Their outer logarithms are log2 n+O(1), so both exact growth indices are 1.
For B_C(n)=B_Q(n)=n the double logarithm is O(log log n), so both indices
are 0. The max{4,B} in the rules, constant factors and finitely many small
n do not change these limits. The structured time exponent coefficient is
1, its outer n power is 1, and its outer logarithm power is 1. The sample
exponent coefficient is 1 with no outer factors. The two space bounds have
empty exponents and n power 1. These are representative upper envelopes,
not lower bounds on actual costs. The sole numeric score, if accepted, is [1].

The fifth claim uses exactly CST-128's error-model text:

> Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

Specifically, for every fixed N,s, each newly delivered sample is rho_s,
in tensor product with all prior deliveries and the current workspace;
the source has no subsequent access to delivered registers. Acquisition
may stop adaptively, but every requested next sample satisfies this promise
conditional on the entire earlier history. With epsilon(n)=0 and actual
acquisition count Q, floor(epsilon(n)Q)=0 samples may be malformed. No
success guarantee for positive corruption is asserted, nor is positive
tolerance claimed impossible. Algorithm-created correlations are allowed.
Under this single model, (3), (4), and both memory bounds hold jointly.

## 7. Scope of improvement and diagnostics

Against CST-128's internal time O(N n log2(n+2)^2), the new time envelope
has ratio 1/log2(n+2) tending to zero. Against its declared O(2^n n^2), the
uniform time ratio is log2(n)/n tending to zero. The memory envelopes,
128N acquisition cap, k=n+4, success >29/32 and exact zero-tolerance model
are preserved. This is a strict improvement of proved upper guarantees
from a particular controller construction. It is not a lower-bound
separation for the inherited quantum test, or a new DCP time exponent.

The saved-copy candidate has fewer acquisitions and faster work but O(n^2)
qubits. Its guarantees and these are incomparable. Faster sieve rows can
also have larger classical storage. We claim neither a literature-wide
optimum nor progress to 2^{O(n^{1/3})} time. The new bound is within a
logarithmic factor of the O(Nn) source charge associated with the cap,
not a proved lower bound on every branch or on DCP.

`diagnostic.py` checks exact carry/borrow logic, all-basis reversible arithmetic
for small registers, the exact Clifford+T phase identity, and rational
one-copy probabilities. It also compares the bounded-record streamed descriptor
generator with the all-basis-tested reference gate list. Its search checks implement the capped sequential
program and compare finite exact output distributions with the uncapped
coupling. It tests the last allowed acquisition, acceptance at the cap,
and a succinct exponentially long cutoff-reaching trace at n>=125. These
are relevant cutoff checks; there is no Grover-round diagnostic. Finite
circuit listings, Python integers and distribution tables belong only to
the diagnostic. They are not the resource-bounded implementation in Sections
3 and 4 and do not establish asymptotic complexity or hosted acceptance.
