# Saved-copy shift search with streamed exact arithmetic

## Result and provenance

For every integer N >= 2 and s in Z/NZ, let n = ceil(log2 N), L = 2^n,
and k = n+24. The single algorithm below has unconditional full-secret
success probability greater than 2/3. On every branch it satisfies

    T = O(2^(n/2) n^2 log2 n),   S_C = O(n),
    S_Q = O(n^2),               Q = n+24 = O(n).

The displayed time envelope is for n >= 2. A bound valid also at n=1 is
C 2^(n/2) n^2 max{1,log2 n} for one absolute constant C; n=1 uses the explicit
constant-size procedure below. All asymptotic constants are independent of
N, s, source outcomes, and measurement outcomes. The four exact growth
indices are [1,0,0,0]. The fractional error guarantee is epsilon = 1 - 1/x^4,
x = 10^64 - 3, under the heralded malformed-copy model of Section 8;
in the clean problem (no herald) the algorithm and all bounds are unchanged.

Snapshot provenance: this snapshot reproduces public submission
b45accfa-78b4-45f0-a9aa-b8e82ed22fd4 unchanged except Section 1's acquisition step, Section 5.3's
sample count, Section 6's error-model paragraph and the new Section 8 (heralded
filter and tolerance). No earlier verdict is a premise.

The base snapshot is a tighter implementation and resource analysis of GordoAR's saved-copy
search, submission 613ca17b-835c-4180-98af-b08f0c06c5bc, source commit
`dad28090a6fe6b51e884ce80633e0221a259105d`, `submission/proof.md` and
`submission/submission.json`. Its search, k, integer round rule, projector
construction, and hybrid argument are materially reused here. The one-copy
test and reversible Boolean evaluation also occur in the challenge baseline
at `cdb1ebff130d861e2c61e9cf517ab66c0a56ca7a`, `submission/proof.md`.
We reproduce the needed proofs rather than assume the earlier acceptance.
The improvement over that submission's stated envelopes is from
O(2^(n/2) n^5) to O(2^(n/2) n^2 log2 n) total work, and from O(n^2) to O(n)
classical bits. Quantum storage, sample count, and error model are unchanged.
This is not a new search principle, a lower bound, a global priority claim,
or a subexponential DCP algorithm. In particular it does not reach
2^{O(n^{1/3})}. The implementation detail responsible for the improvement
is proved in Sections 4 and 5.

## 1. The algorithm

Acquire exactly k well-formed source states through FILTER (Section 8) and retain
all of them. In the clean problem FILTER is the identity, so exactly k independent
ideal source states rho_s are acquired.
Sample j consists of a qubit b_j and an n-qubit residue y_j. The source costs
k(n+1) work units. No purification, offset x, inverse preparation circuit,
or coherent source access is supplied or used.

For n=1, N=2. Apply H to each b_j and measure it in the computational basis.
Output 0 if all k measured bits are 0; output 1 otherwise. Measure all k bits,
even after a nonzero bit is seen. No extra copies are requested.

For n>=2, prepare an n-qubit candidate register as

    |u> = (1/sqrt(L)) sum_{t=0}^{L-1} |t>.

Define the integer r exactly by

    r = isqrt(9L) // 4 = floor(3 sqrt(L)/4).

Here isqrt is the floor of the nonnegative square root, and // is integer
division. The identity follows because floor(floor(x)/4)=floor(x/4).
Perform exactly r iterations of R followed by D, as defined below.
Measure the candidate register. Output t if t<N, and output 0 otherwise.
There are no restarts, verification samples, postselection, or adaptive loops.
The quantum computation uses only exact Clifford+T gates and final
computational-basis measurements. Ancillas start in |0> and are cleaned.

## 2. The implemented projector reflection

For t<N define a permutation of all n-bit y, including invalid encodings, by

    f_t^-(y) = (y-t) mod N  if y<N, and y otherwise.

Its inverse f_t^+ adds t modulo N on y<N and is the identity on y>=N.
Let C_t apply f_t^- conditioned on the first sample qubit b being 1.
Set V_t=(H tensor I) C_t and

    A_t = V_t^dagger (|0><0| tensor I) V_t,
    P_t = A_t^{tensor k}.

On the source component with offset x, C_t produces

    (|0,x> + |1,(x+s-t) mod N>)/sqrt(2).

For t=s the first qubit is |+>, so the test after H passes with certainty.
For t!=s the two residue strings are distinct for every x, so tracing out
the residue gives I/2, and the probability of a zero after H is exactly 1/2.
This proves the same facts for the mixed input. Independence at acquisition
therefore implies, for sigma_s=rho_s^{tensor k},

    Tr(P_s sigma_s)=1,
    Tr(P_t sigma_s)=2^(-k)   for every t<N, t!=s.                 (1)

The circuit implements the following exact unitary, without assuming it as
an oracle:

    R = sum_{t<N} |t><t| tensor (I-2P_t)
        + sum_{N<=t<L} |t><t| tensor I.                         (2)

First compute v=[t<N] into a clean flag. On each sample apply the controlled
permutation from Section 4, enabled by v and b_j, then H on b_j. Do this for
all k samples, reusing the arithmetic workspace. Compute the AND of v and
all conditions [b_j=0] into clean ancillas, apply Z to its result, and reverse
the AND computation. Undo all H gates and permutations in reverse order,
and uncompute v. Thus on t<N this is conjugation of the all-pass phase flip
by V_t^{tensor k}. On t>=N the phase flip is disabled and the entire
compute/uncompute sequence is the identity. In particular invalid candidates
are never marked. Arithmetic and conjunction work qubits return to zero
exactly, including when the saved samples are entangled with the candidate.
The saved samples themselves need not return to their original state.

Diffusion is D=2|u><u|-I. Hadamards before and after a sign flip of the
all-zero candidate implement -D. Supply the global factor -1, if needed
for the equalities below, with XZXZ on a spare clean qubit. This is -I on
that qubit and leaves it clean. This constant overhead implements D exactly.
A conjunction chain implements the all-zero phase flip in O(n) gates and
O(n) ancillas. All negated controls use X before and after the chain.

## 3. Success with the same mixed batch throughout

Use a purification only in the mathematical analysis:

    |Phi_s> = tensor_{j=1}^k
              (1/sqrt(N)) sum_{x=0}^{N-1} |x>_{E_j}|psi_{x,s}>.

Every physical operation is extended by the identity on E. Equation (1)
and the fact that the P_t are orthogonal projectors imply

    P_s|Phi_s>=|Phi_s>,
    ||P_t|Phi_s>||=2^(-k/2)   for valid t!=s.                   (3)

Define the ideal comparison reflection

    R_*=(I-2|s><s|) tensor I.

It is not available to the algorithm. For every normalized candidate vector
|a>=sum_t a_t|t>, orthogonal candidate labels give the exact identity

    ||(R-R_*)(|a>|Phi_s>)||^2
      = 4 sum_{t<N,t!=s} |a_t|^2 2^(-k) <= 4*2^(-k).          (4)

There is no factor N in this bound. The correct-label summand vanishes by
(3), and the invalid-label summands vanish by (2). Put W=DR and W_*=DR_*.
The algebraic telescoping identity is

    W^r-W_*^r = sum_{j=0}^{r-1} W^{r-1-j}(W-W_*)W_*^j.

In each summand W_*^j|u>|Phi_s> is a candidate state tensored with the
unchanged |Phi_s>. Apply (4) there. The actual-circuit prefix W^{r-1-j} is
unitary and cannot amplify the vector norm. The triangle inequality yields

    delta := ||W^r|u>|Phi_s>-W_*^r|u>|Phi_s>||
          <= 2r*2^(-k/2)
          <= (3/2)*2^(n/2)*2^(-(n+24)/2) = 3/8192.             (5)

This is a state-specific hybrid bound on ideal intermediate states, not an
operator-norm bound on all data states. It remains valid over exponentially
many iterations with the same real batch, even if that batch is disturbed
and correlated after the first iteration. Independence is invoked only for
the initial product state in (1). No refreshed samples are hidden in (5).

For completeness the ideal search probability is derived here. Let
sin(theta)=1/sqrt(L) and |b> be the uniform vector of labels other than s.
In the basis (|s>,|b>), |u>=(sin(theta),cos(theta)) and

    D R_* = [[cos(2theta), sin(2theta)],
             [-sin(2theta), cos(2theta)]].

Its r-th power gives ideal marked probability sin^2((2r+1)theta).
For a=1/sqrt(L)<=1/2, the derivative and convexity of arcsin give

    a <= arcsin(a) <= (pi/3)*a.

The upper bound is the chord from (0,0) to (1/2,pi/6). Since
3/(4a)-1 < r <= 3/(4a),

    1 <= 3/2-a <= (2r+1)theta <= (pi/3)(3/2+a) <= 2pi/3.

On [1,2pi/3] the minimum of sin^2 is at an endpoint.
Also sin(1)>=1-1/6=5/6, obtained by integrating
cos(z)>=1-z^2/2 on [0,1]. The latter follows from
1-cos(z)=2sin^2(z/2)<=z^2/2. Hence ideal success is at least
min(25/36,3/4)=25/36 for every n>=2.

For any normalized |p>,|q> and event projector E, expansion of the
difference and Cauchy-Schwarz give

    |<p|E|p>-<q|E|q>| <= 2||p-q||.

Use E for the event that the measured candidate equals s, including the
purifying registers. Equation (5) proves actual success at least

    25/36 - 3/4096 = 25573/36864 > 2/3.                       (6)

The map of invalid outputs to 0 can only add success when s=0. Tracing out
E gives exactly the mixed-input measurement probabilities.

When n=1 and N=2, the t=0 test always passes for s=0. For s=1 its k outcomes
are independent fair bits. The only failure is the all-zero string, with
probability 2^(-25). Thus every N, including the small case, is covered.

## 4. Linear-size exact arithmetic, including inverses

This section establishes O(n) elementary gates and O(n) reusable quantum
scratch per controlled permutation, rather than relaxing them to O(n^2).
The candidate bits are quantum inputs. There is no table indexed by t and
no enumeration of possible candidate values during circuit generation.
N is a classical constant using at most n+1 bits, including when N=2^n.

### 4.1 Fixed-width Boolean scans

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

### 4.2 Total permutations on all computational basis inputs

Let v=[t<N], already computed once for a query. For one copy set
h=v AND b AND [y<N]. A Boolean evaluator F^- produces an n-bit result:

    d = y-t mod 2^w,       beta = [y<t],
    z = d + beta*N mod 2^w,
    F^-(t,b,v,y) = low_n(z) if h=1, and y otherwise.             (7)

The mask beta*N is formed bitwise from the stored bits of N. If h=1 then
0<=y,t<N, so -N<y-t<N and z is precisely (y-t) mod N, lying below N.
The leading bit of z is then zero. If h=0, the arithmetic values, even on
invalid inputs, are ignored by the final selection. All scratch values
are nevertheless computed and uncomputed without measurement.

The inverse evaluator F^+ uses

    e = y+t in w bits,      gamma = [e>=N],
    z = e-gamma*N mod 2^w,
    F^+(t,b,v,y) = low_n(z) if h=1, and y otherwise.             (8)

For h=1, e<=2N-2<2^w, so the sum does not overflow and one subtraction
suffices. Both maps preserve the valid and invalid y ranges. For v=[t<N]
and either value of b, F^+ and F^- are mutual inverse permutations of all
n-bit y. To make their definitions inverse also for arbitrary flag inputs,
one may include [t<N] again in h. This adds one linear scan and is the
choice used here. The computed v is always correct in the search anyway.
There are a fixed number of width-w scans in (7) and (8), irrespective of
n, with no multiplication of quantum words. The only products by N here
are Boolean masks. Thus both evaluators have O(n) Boolean gates and wires.

### 4.3 Clean reversible evaluation and in-place permutation

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
workspace is reused between these evaluations and between saved copies.
This construction has O(n) gates, including copying, swap and uncomputation;
it is not merely a gate bound for a nonreversible forward calculation.

### 4.4 Exact phases and conjunctions

A conjunction of m literals is computed by a chain of at most m-1 Toffolis
into at most m-1 clean bits, followed by Z on the last bit and reversal.
The m=1 case is just Z; a zero literal is converted by X gates before and
after the construction. For R, m=k+1 includes v; for diffusion, m=n.
This is an exact projector phase flip, with O(k+n) work qubits and gates,
and no synthesis whose precision depends on the number of iterations.

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

## 5. Streamed uniform generation and charged resources

### 5.1 Why a gate can be emitted in O(log(n+2)) charged work

The Boolean circuits above consist of a fixed number of sweeps. A sweep
has a fixed number of temporary wires and gates per bit. Allocate a block
of that fixed size for each position i. Its addresses are of the form
base + c*i + d, where c and d are fixed integers. Only adjacent carries
or borrows from position i-1 are referenced. Selection sweeps read the
corresponding indexed bits of earlier fixed blocks. Supply leading zeros
and boundary carries at the ends with fixed boundary cases.

A generator needs the sweep number, bit position, gate-within-block number,
direction, and a fixed number of block base addresses. To reverse a sweep,
visit its blocks and within-block gates in reverse order. To reverse a
whole evaluator, visit its fixed number of sweeps in reverse order. Wire
allocation and addresses are determined by n and these counters, so neither
a gate list nor a pointer table is needed to uncompute. Retaining values
in quantum wires does not require storing their addresses individually.
Nested calls have constant depth and finite templates.

Each gate descriptor has constant arity and O(log(n+2)) bits. Operations
on wire indices are additions, comparisons, increments, and multiplication
by a fixed constant. Binary scans perform these in O(log(n+2)) bit steps.
Between copies, update the sample-register base by adding n+1, rather than
multiplying two variable indices for every gate. The initial bases of the
fixed number of blocks may use a one-time multiplication of O(log(n+2))-bit
words. N is stored as its O(n)-bit input; read its i-th bit when a constant
mask or comparison requires it. Quantum candidate bits are named wires,
not classically read or quantum-addressed memory. The outer search counter
is addressed separately below.

To account for classical addressing without silently charging a second
log factor, place these fixed-many short index words, the gate descriptor,
and their ripple-control bits in named controller fields. Operate on their
bits by fixed sequential scans. The scan performs O(log(n+2)) fixed-size
bit operations; it does not perform a new arbitrary indexed memory lookup
for each bit of its own index. Reading a bit of N or emitting an indexed
quantum gate pays O(log(M+2)) for that indexed access. A gate template
uses only a constant number of such accesses. This is an ordinary uniform
bit controller using fixed control and sequential word scans, not a unit-cost
word RAM. One can realize its scans by moving over a word on a classical
work tape, with unit-cost adjacent moves and local logic; an arbitrary
indexed access still incurs the required address charge. All stored tape
bits are counted in S_C. Thus both generation and execution of one
constant-size quantum gate cost O(log(n+2)), including addressing.

For clarity, the addressing convention in the rules charges a *classical
indexed access* by its address length. Fixed-size logic and a sequential
scan of an explicitly stored word do not become nested indexed accesses.
If an implementation instead uses indexed arrays to simulate every local
bit operation of that controller, it adds unnecessary overhead. That
simulation is not the algorithm specified here. No stored instruction
sequence grows with r or with the number of gates in a round.

### 5.2 Work per iteration and preprocessing

Each reflection computes v in O(n) gates, performs k forward and k inverse
permutations in O(kn) gates, uses 2k Hadamards and an O(k)-gate conjunction,
and uncomputes v. Diffusion costs O(n) further gates. Since k=n+24<=25n
for n>=1, one round has O(n^2) elementary gates. Section 5.1 charges
O(n^2 log(n+2)) work for these gates, generation, and indexed accesses.
Initializing and clearing O(n) reusable scratch, if charged each round,
also fits this bound. The proof already cleans scratch unitarily.

An iteration counter and the precomputed limit r have O(n) bits. Updating
and comparing them by scans costs O(n) bit operations per round, or even
O(n log(n+2)) if every counter bit read is charged as an indexed access.
Both fit O(n^2 log(n+2)). Do not recompute r or multiply n-bit integers
inside the quantum gate loop.

Compute r once by binary search for isqrt(9*2^n), using O(n) steps on O(n)-bit
integers. Each square can be obtained by schoolbook shift-and-add into an
O(n)-bit accumulator, with O(n^2) bit operations and O(n) storage, reusing
one shifted copy and the accumulator. Counting every indexed bit access
adds at most a log(n+2) factor. The total preprocessing work is therefore
O(n^3 log(n+2)) and its classical space is O(n). The binary search maintains
a constant number of O(n)-bit words; it does not store all trials or
partial products. Computing n, k, the few memory-block bases, and the
integer division by 4 is covered by this bound.

Allocate the saved copies, candidate and scratch explicitly. Source work
is exactly k(n+1)=O(n^2); addressing and initialization add at most
O(n^2 log(n+2)). The Hadamards for |u>, the n final measurements, comparison
with N, and writing the full n-bit output fit this bound as well.
There is no hidden preprocessing table or failed state-preparation attempt.

Thus total work on every branch is

    O((r+1)n^2 log(n+2) + n^3 log(n+2))
       = O(2^(n/2) n^2 log(n+2)).                             (9)

For the equality, r<=3*2^(n/2)/4 and n=O(2^(n/2)) for all n>=1.
For n>=2, log(n+2)=O(log2 n), giving the claimed structured envelope.
The n=1 procedure costs a fixed constant and satisfies the stated
max{1,log2 n} version. All outcomes, successful or otherwise, have the
same fixed schedule in the search branch.

### 5.3 Peak storage and samples

The saved batch uses k(n+1) qubits. Candidate, arithmetic workspace,
permutation target, flags, conjunction chains and constant gate-decomposition
scratch use O(n+k) further qubits. Hence S_Q=O(n^2), including all data
and ancillas. Arithmetic scratch is reused; it is not allocated for all
copies at once.

Classical storage consists of N, the O(n)-bit search limit and counter,
a constant number of O(n)-bit preprocessing words, O(log(n+2))-bit index
fields and one gate descriptor, and the n-bit measured output. Even if
these coexist, S_C=O(n). The list of past gates, all source labels x, and
the vector of test outcomes are never stored classically. In the n=1 branch
an accumulated AND and the current outcome suffice. Thus the total allocated
bits and qubits M=O(n^2), justifying the address length O(log(n+2)) used above.

In the clean problem exactly k=n+24 source copies are acquired once on every
branch and no others (under the heralded model see Section 8: at most D k raw).
This count includes the n=1 branch, unsuccessful search measurements, and
all final discards. Reusing the quantum registers does not mean reacquiring
a source state. Consequently Q=n+24=O(n), independently of peak storage.

## 6. Growth indices, error model, and scope of the improvement

For B_T(n)=2^(n/2)n^2 log2 n on n>=2,

    log2 B_T = n/2 + 2log2 n + log2 log2 n = n/2 + O(log n).

Its outer logarithm is log2 n + O(1), so the limsup index in rules.md is
exactly 1. A constant multiplier in the big-O bound does not change this.
For the envelopes n, n^2, n of classical storage, quantum storage, and
samples, respectively, the double logarithm is O(log log n), so their
indices are exactly 0. No matching lower bounds on actual usage are claimed.
The coefficient 1/2 inside the time exponent is preserved in the structured
bound; the outer polynomial and logarithm powers are 2 and 1. The other
three structured exponents are empty, with powers 1, 2, 1. Only the time
index is a numeric objective, so the score vector, if accepted, remains [1].

The fifth structured claim is the heralded tolerance of Section 8. In the
clean problem (every copy an independent ideal coset state, no herald), the
joint state of the acquired samples is rho_s^{tensor k}, FILTER is the identity,
and Equations (1)--(9) prove correctness and the four resource bounds jointly.

Relative to the full envelopes of submission 613ca17b, the time ratio is
(log2 n)/n^3 -> 0, and the classical-space ratio is 1/n -> 0. Quantum and
sample envelopes agree; the exact Q=n+24 and epsilon=0 error model agree.
This establishes a strict improvement in two declared upper bounds, not a
separation between the optimum costs of the underlying algorithms. In fact
the search algorithm is inherited; its unnecessary conservative resource
allowances are removed by the explicit construction above.

## 7. Diagnostic evidence and its limits

`diagnostic.py` is a standalone standard-library Python diagnostic. It checks
the carry and borrow recurrences; lifted reversible permutation circuits on
small complete computational-basis domains, including invalid t and y and
clean scratch; the phase-polynomial identity and conjunction phase; the
one-copy projector probabilities with exact rational arithmetic; and the
integer Grover rule and rational success margins for finite n.
Its output is a reproducible finite sanity check, not a proof of asymptotics,
a simulation of the full k=n+24 algorithm, a provider review, or benchmark
acceptance. The executable may keep circuit descriptions and use Python
integers for testing. Those are diagnostic implementation choices, not the
streaming controller specified and costed in Section 5. The complete
mathematical proof and cost derivation above establish the claims without
extrapolating finite tests.

## 8. Heralded filter and tolerance

Error model (exact text of the fifth structured claim):

Heralded malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires on an execution branch, and epsilon(n) the tolerated malformed fraction. Each acquired copy consists of an (n+1)-qubit register of the ideal copy's shape together with one classical herald bit f delivered with it. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed. A well-formed copy has f = 0 and its register is a fresh copy of rho_s, in tensor product with every other system (earlier copies, the adversary's system and the algorithm's registers). A malformed copy has f = 1 and its register is in an arbitrary state chosen by the adversary, possibly entangled with the adversary's private system and with other malformed copies. On every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. The herald is always correct, so malformation is detectable (an erasure-type error); its timing, its number within the promise and the malformed register contents are adversarial. In the clean problem no herald is supplied and every copy is well-formed. No source control, purification access or preparation inverse is supplied.

Let x = 10^64 - 3 = 9999999999999999999999999999999999999999999999999999999999999997, D = x^4 and epsilon = 1 - 1/D. FILTER: acquire one raw
copy; if its herald bit is f = 1, reset its n+1 qubits to |0> without any other
operation and acquire again; otherwise retain it as the next of the k saved
copies. A raw counter enforces the literal cutoff D k: if the next raw
acquisition would exceed D k, stop and output 0. All k copies are obtained
before any other operation; the herald reads are the only intermediate data.

Lemma 8.1. Under the promise, the cutoff D k is never reached before k
well-formed copies are retained. Proof. Otherwise Q = D k raw copies were
acquired with R <= k-1 well-formed, so B >= D k - k + 1 malformed, while the
promise gives B <= floor((1 - 1/D) D k) = D k - k. QED.

Lemma 8.2. Under the model, the retained k registers are in the state
rho_s^{tensor k} and in tensor product with the adversary and all discarded
registers, exactly as in the clean problem. Proof. Each well-formed copy is, at
delivery, a fresh rho_s in tensor product with every other system; malformed
registers are reset without interacting with retained ones, so adversarial
timing and entanglement act only on systems disjoint from the retained batch.
QED. Hence Sections 1--5 apply verbatim and success is at least 25573/36864.

Resources under the model. Raw acquisitions Q <= D k = O(n), since D is a fixed
absolute integer. Each raw copy costs n+1 source work, one herald read and at
most an O(n) reset, each step paying the O(log(n+2)) address factor: O(D k n log n)
= O(n^2 log n) extra work, below the time bound. The raw counter needs
O(log2(D k)) = O(log n) + 851 bits, so S_C = O(n). A malformed register reuses
one extra (n+1)-qubit slot released before the next acquisition, so S_Q = O(n^2).
All four bounds of Sections 5--6 therefore hold on every branch under the model.

Tolerance integers. The displayed integers t_i satisfy t_1 * ... * t_3 = x^2 + 1
exactly (direct integer multiplication; they need not be prime):

    t_1 = 5909009547859618446014307935656485996455360061473289284034355157
    t_2 = 8461654968574415353741992088106541809421651544931744139485636465
    t_3 = 2

Each of x-1, x, x+1 and every t_i has at most 64 decimal digits. The supported
expression

    9999999999999999999999999999999999999999999999999999999999999996*9999999999999999999999999999999999999999999999999999999999999998*5909009547859618446014307935656485996455360061473289284034355157*8461654968574415353741992088106541809421651544931744139485636465*2/9999999999999999999999999999999999999999999999999999999999999997^4

equals (x-1)(x+1)(x^2+1)/x^4 = (x^4-1)/x^4 = 1 - 1/x^4 = epsilon, a constant in
(0,1), with normalized numerator and denominator of 256 digits. This guarantee
covers detectable (heralded) malformed copies only; no tolerance of undetectable
corruption is claimed.
