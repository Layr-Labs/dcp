# RS7: exact Hadamard source labels and a smaller fifteen-event sieve

RS7 extends the elementary-source RS6S, submission
967b0ccc-a313-4030-bd7b-32597ad8f838, adding a global rescue of SUMs from
the first-R rejected-difference rescue. Their exact S*S distribution,
14641-term correlation evaluator, positive degree-fifteen certificate,
finite small-H branches and success1/5 are proved in recycle-sieve.md
Section12. The actual smaller ratio q=5847/1000 and fifteen-event schedule
establish the new complete joint bounds. The elementary repeated-Hadamard
extractor and schoolbook implementation remain unchanged in form, with
all parameters recomputed. No predecessor verdict validates this candidate.

The direct published foundation is RR8,4e2ca900-70e1-4923-a469-ea5a1bc0e25b,
at ae634c28a7e4a2683087607a83a432adb370b5d7. The exact elementary source
extractor, modular arithmetic and rational decoder are directly reused from
VFD3-M4,6f4423a3-e180-476f-987a-b1c4cdaa898e, at
c3719a087388963198f068135526bd69fe3ab877. MDC1's minimum-feasible-capacity
construction,7c30b190-e90b-492c-b52c-29cf1a9da1a7, remains a material source.
RS4/RS4V/RS5/RS6 supply the fully reproduced later recycling developments;
all provenance is retained, but no predecessor verdict is a proof premise.

## 1. The theorem and the exact algorithm configuration

For every integer N >= 2 and fixed s in Z/NZ, let n=ceil(log2 N). RS7
receives only fresh independent copies of the mixed state in rules.md. It
outputs the entire s with unconditional probability at least 1019/1024.
The same execution has, on every branch, including every abort,

    T(N,s)   = O(n^(9/2) (log2 n) 2^((564341027/250000000) sqrt(n))),
    S_C(N,s) = O(n (log2 n) 2^((564341027/250000000) sqrt(n))),
    S_Q(N,s) = O((log2 n) 2^((564341027/250000000) sqrt(n))).

These asymptotic envelopes apply for n>=2. The n=1 cases are explicitly
handled below and have absolute finite costs. Each envelope has growth
index exactly 1/2. Constants are absolute, independent of N, s, outcomes
and memory contents. They include source calls, classical bit work,
addressing, generated gates, measurements, initialization and all failures.
The structured objects declare these exact envelopes. The exponential coefficient 564341027/250000000 is explicitly proved;
no unspecified inside big-O coefficient is replaced by a number.

For n<=16, RS7 exhaustively tests t=0,...,N-1 by Section 10 with k=n+10
fresh tests per candidate. It returns the first candidate passing all tests,
or zero if none passes. This is a fixed finite prefix of the single algorithm.
It does not run the sieve or generate the phase table.

For n>=17 put h=n+1, m=floor(log2 N), q=5847/1000, r=6369/2500.
`clog(x)` is the bit length of x-1. Define the exact integers

    ell=min{v>=1 : v+sum_(j=0)^(v-1)floor(r*j)>=m-1},
    J=m-1-ell, lambda=clog(1024*h),
    M=8192*lambda, F=2^62*lambda,
    L_i=ceil(F*q^(ell-i)), i=0,...,ell,
    R=4*(J+1)*L_0, global_coin_trial_limit=4R,
    M_src=8192*clog(1024*R*(n+3)), k=n+10.

Compute ell by binary search on[1,m-1] and the displayed finite sum; its
upper endpoint is feasible. All rational powers/ceilings are exact integer
operations, L_i=ceil(F*5847^t/1000^t). For i=0,...,ell-1 greedily allocate
b_i up to floor(r*(ell-i-1)) until their sum is exactly J. Capacity guarantees
this. For each target j=0,...,J allocate a_i greedily from b_i until sum a_i=j,
and let c_i=b_i-a_i. These widths are deterministic, independent of outcomes.
The exact bounds 2^r<q<2^(25477/10000),
ell<=(22151/25000)sqrt(n)+2 and ell=Theta(sqrt n) are proved from small rational
inequalities in recycle-sieve.md Section6. They imply
L_0=O(log2(n)*2^((564341027/250000000)sqrt(n))). No guessed exponent constant is used.

Every abort outputs the n-bit encoding of zero and releases its workspace.
All loops, allocations and return values are defined on every measurement
string. No unbounded repetition, favorable-outcome conditioning, oracle,
instance-dependent advice or uncharged preparation is part of RS7.

The source, arithmetic and outer decoder foundations are reproduced below.
The original flat-difference foundation derives from FD2 submission
286f74f7-dd46-4db7-9fe2-031755c76a04, candidate
773a35a977a66bbe10fa6f8f6ea50c2021f0fba0 (outside this challenge scope),
through the explicitly named VFD3/MDC1/PG sources. The new pooled-sum
instrument, distribution proof and quotas are in recycle-sieve.md; no
historical acceptance is a proof premise or a cube-root complexity claim.

## 2. Exact reversible operations on the entire encoded domain

Use temporary arithmetic width w=n+2. A Boolean ripple adder with initial carry
c_0 in {0,1} is the following fixed loop for i=0,...,w-1:

    p_i = a_i XOR b_i
    z_i = p_i XOR c_i
    g_i = a_i AND b_i
    h_i = p_i AND c_i
    c_(i+1) = g_i XOR h_i.

Here g_i and h_i are mutually exclusive. Truth tables prove the sum and carry
identities, and induction proves the w-bit sum and final carry. Retain all
intermediate Boolean wires until reversal. SUB(X,C) means this same ADD loop on
X and the bitwise complement of the w-bit C, WITH INITIAL CARRY ONE. It returns
(X-C) modulo 2^w and final carry [X>=C]. This also holds at C=0: the complemented
zero plus carry-in represents 2^w. Replacing it with the wrapped constant
(-C mod 2^w) and carry-in zero would give the wrong comparison when C=0 and is
not the RS7 schedule. A Boolean MUX(control,x,y) is

    y XOR (control AND (x XOR y)).

To add a known c in [0,N) conditionally modulo N, let X be the n-bit input,
zero padded to width w, and let B be the quantum control bit. Compute

    (_, geN) = SUB(X,N)
    active = B AND NOT(geN)
    (S,_) = ADD(X,c,0)
    (D,ge) = SUB(S,N)
    V = MUX(ge,D,S)
    out = low_n_bits(MUX(active,V,X)).

On X<N and B=1 this is X+c mod N. On B=0 or X>=N it fixes X. The inverse uses

    (_,geN) = SUB(Y,N)
    active = B AND NOT(geN)
    (D,gec) = SUB(Y,c)
    (P,_) = ADD(Y,N-c,0)
    V = MUX(gec,D,P)
    out = low_n_bits(MUX(active,V,Y)).

For Y<N this selects Y-c or Y+N-c and is the inverse; on invalid encodings it
is identity. The formulas include c=0 and N=2^n. All sums used in comparisons
are below 2^w. Wrapped subtraction outputs are used only under the appropriate
comparison/MUX. Thus the maps are mutually inverse permutations on ALL n-bit
encodings, not just on the valid residues.

Each ADD/SUB has five Boolean gates per bit before constant simplification;
three arithmetic loops and the MUXes use fewer than 100w Boolean gates per map.
Compute each Boolean output into a fresh clean wire, XOR the final n output bits
into a target, and reverse the Boolean schedule. This implements an XOR oracle
with clean scratch. To implement the in-place permutation f, XOR-compute f(X)
into clean Y, swap X,Y, and XOR-compute f^-1(X) into Y. The latter clears old X.
This proves scratch cleanup on every basis state; linearity proves the unitary
on superpositions. The control B is preserved.

NOT, CNOT and Toffoli implement the Boolean computations exactly. Toffoli has an
exact constant-size Clifford+T realization: for bits a,b,c,

    4abc = a+b+c -(a XOR b)-(a XOR c)-(b XOR c)+(a XOR b XOR c).

Applying T or T-dagger to these seven parities, computed/uncomputed by CNOT,
implements CCZ exactly. Conjugating its target by H implements Toffoli. Eight
bit assignments prove the identity exhaustively; there is no residual relative
or global phase. One reused parity ancilla suffices. Generous bounds of 100000w
elementary gates and 1000w scratch qubits cover a controlled permutation.

The controller streams this finite pattern using bit position, Boolean-operation
index and a constant number of block bases. It stores no circuit list. Classically
known wire addresses are computed by ordinary binary arithmetic. Section 11
charges their full bit cost. In particular, this construction supplies controlled
cyclic shifts U^c on valid data, U|x>=|x+1 mod N>, and controlled subtraction for
Section 10. It assumes no unit-cost quantum lookup or arithmetic oracle.

## 3. A finite rational phase decoder

Let dist be circular distance on R/Z. The fixed table `evidence/phase_grid.json`
contains rational coordinates for the 64 points exp(2*pi*i*r/64), with denominator
2^16. Each coordinate has absolute error <2^-16. The table is fixed independently
of N and s. RS7 generates it once by the finite rational schedule in
`evidence/rational_grid_certificate.py`, charging its entire finite generation
work and allocated memory. The included JSON is reproducibility evidence, not
an uncharged preloaded input. Here is a
self-contained error justification for its specified generator.

For q=5 and 239, sum the first 20 alternating terms of atan(1/q), obtaining a
lower bound; adding the next term gives an upper bound. Machin's identity
pi=16 atan(1/5)-4 atan(1/239) gives rational bounds p_lo,p_hi with width <2^-90
and 3<p_lo<p_hi<22/7. To prove the identity, tan(2 atan(1/5))=5/12 and
 tan(4 atan(1/5))=120/119. Subtracting atan(1/239) gives tangent one, and the
angle lies in (0,pi/2), hence is pi/4. At each argument 2r(p_lo+p_hi)/(2*64),
sum 60 sine or cosine Taylor terms. Its magnitude is below seven; remainder
bounds are respectively 7^121/121! and 7^120/120!, both <2^-200. Replacing pi by
the interval midpoint contributes <2*(p_hi-p_lo) per coordinate. Rounding to
16 fractional bits contributes <=2^-17. Their sum is <2^-16. The certificate
checks these strict inequalities using rational integers and fractions only.

Given empirical means x,y in [-1,1], select the smallest grid index r minimizing
squared Euclidean distance to the rational table point; return alpha=r/64. All
comparisons are exact rational comparisons. If x,y approximate cos(2*pi*theta),
sin(2*pi*theta) within 1/32 each, empirical-vector error is <=sqrt(2)/32. A true
grid point is within chordal distance pi/64 of the true point. Triangle
inequalities for nearest approximate-grid selection give chordal error at most

    p_hi/64 + 3/32 + 3/65536 < 1/4,

using sqrt(2)<3/2. A chord at circular distance d is 2 sin(pi*d)>=4d for
0<=d<=1/2, so dist(alpha,theta)<1/16. This decoder has no real-arithmetic,
angle-estimation, or synthesis oracle.

The following exact rational unwrapping routine is used twice. Given
alpha_0,...,alpha_H estimating 2^h theta modulo one, set z_H=alpha_H. For
h=H-1,...,0 choose, modulo one, from

    z_(h+1)/2, (z_(h+1)+1)/2

the candidate circularly closer to alpha_h, taking the smaller rational on a tie.
If every dist(alpha_h,2^h theta)<=eta=1/16, induction proves

    dist(z_h,2^h theta) <= eta*2^(-(H-h)).

The true nearby preimage has distance <=3eta/2 from alpha_h; the other has distance
>=1/2-3eta/2. These are strictly separated. The nearby preimage halves the prior
fine-scale error. This argument uses circular distance, so it includes wraparound
at zero. All numerators and denominators have O(H+1) bits.

For completeness, the concentration estimate used below is elementary. If
X in {-1,1}, the second derivative of log E exp(t(X-E X)) is a tilted variance,
which is <=1. Its value and first derivative vanish at zero, giving an upper
bound t^2/2. Independence and Markov, optimized over t, then give

    Pr(|sample_mean-E X|>epsilon) <= 2 exp(-M epsilon^2/2).

At epsilon=1/32 the bound is 2 exp(-M/2048).

## 4. Source-only phase labels without an arbitrary-modulus QFT

For analysis define omega=exp(2*pi*i/N),

    chi_y = (1/sqrt(N)) sum_x omega^(-yx)|x>,
    q_y = (|0>+omega^(sy)|1>)/sqrt(2), Q_y=|q_y><q_y|.

Direct expansion of matrix entries gives

    rho_s = (1/N) sum_(y=0)^(N-1) Q_y tensor |chi_y><chi_y|.

Indeed the cross entry indexed by x,z sums omega^(y(z-x-s)), which vanishes
unless z=x+s mod N, and the diagonal blocks agree as well. Also U chi_y=omega^y
chi_y. This is an ensemble identity for the given mixed state; it supplies no
accessible hidden register or additional source operation to the algorithm.

For each h=0,...,n+2, do M_src Hadamard tests of controlled U^(2^h) on the source
DATA register in X, and M_src such tests in Y. Use a fresh/reset ancilla in |+>
for every test. Conditional on latent y in the exact ensemble, the means are
cos(2*pi*2^h*y/N), sin(2*pi*2^h*y/N). The data register remains chi_y; the first
source qubit is untouched. Hence these test outcomes are independent conditional
on y. U^(2^h) is the exact controlled addition by 2^h mod N of Section 2.
Measuring Y means S-dagger then H then a computational-basis measurement;
measuring X means H then that measurement. No approximate rotation is invoked.

Decode the two empirical means at each h by Section 3, then unwrap with H=n+2.
If all means are accurate, the estimate of y/N has circular error
<=1/(16*2^(n+2))<1/(2N). Round N times the estimate to the nearest integer modulo
N (smaller integer on a tie). Report that integer as y_hat and retain the first
source qubit. Dispose/reset the data and ancillas.

For every latent y, the probability that y_hat differs from y is at most

    delta_src = 4(n+3) exp(-M_src/2048) < 1/(1024R).

For the last inequality, let A=1024R(n+3), use M_src>=8192 log2 A and ln(2)<1:
exp(-M_src/2048)<=A^-4. The stated inequality follows immediately for R>=1.
The retained qubit, conditional on the latent y, is exactly q_y, even if the
reported label is wrong. We make no perfect-label assertion for this physical
extractor.

An ideal analysis may instead report the latent y. Couple it to the actual
extractor using the exact ensemble and the same test outcomes. Until a wrong
label occurs, their retained classical/quantum states coincide after local test
records are discarded. There are at most R label extractions; a conditional
union bound gives total divergence probability <1/1024. This is a proof coupling,
not coherent source access or conditioning the algorithm on an unobservable
correctness event. All later ideal-label arguments are transferred with this
additive error bound.

## 5. Exact four-pass and global recycling instruments

recycle-sieve.md Sections 1-6 and 10-12 specify the entire stage: primary flat
differences, second/third/fourth same-bucket SUM rescues, globally pooled PRIMARY rejected differences and rescues of their SUMs and FIRST-pass rejected differences, and SUMs from that rejected rescue. Same-bucket SUMs are paired by original position within their bucket,
never by label. The global V-SUM population is paired across the stage
by original generation position only after all bucket offsets have cancelled. The fourth SUM input has offset 8f0, which cancels
on difference. Its exact kernel, valid rational coins, independent uniform
conditional output states, and fixed output ordering are proved there.
The retained ensemble is uniform on [0,M0/2) with frequency A*2^a*d.
No second/third/fourth rejected difference is recycled. Fourth-pass SUMs
are discarded. Every middle width is at least two bits.

## 6. Exact rational coins and one global trial cap

Each channel uses the explicit rational coins in recycle-sieve.md; all
zero-label cases are specified there. Evaluate numerators/denominators by
counted integer arithmetic; draw clog(denominator) fair bits, retry out-of-
range draws, and compare an in-range draw with the numerator. One counter
permits at most 4R trials across all stages and batches. Abort if another
trial would exceed that cap. Section 8 of recycle-sieve.md proves fewer
than R coin calls on every branch and cap-abort probability <1/1024 by
coupling to independent fair Bernoulli completions. No conditioning on cap
survival is used to infer an ideal state law. All failed draws count.

## 7. Complete batches and all outcomes

Generate the fixed rational decoder by Section3, charging its finite
integer computation. Generate controlled-translation constants by repeated
modular doubling, and initialize the single global sampler-trial counter.
For each target j=0,...,J, sequentially acquire exactly
4L_0 source copies, retain the first L_0 labels below 2^m, and abort on
shortage. Initialize A=1,B=2^m. At each stage run the full stage (including Sections 10-12) of
recycle-sieve.md, retain its first L_(i+1) outputs in the prescribed order,
release extras/old buffers, and abort on shortage. Update A*=2^a_i,
B/=2^(b_i+1). At the final A=2^j,B=2,L_ell=F, retain the first 2M label-one
states, abort on shortage, measure M in X and M in Y, decode alpha_j and
release the batch. Save only alpha_j. Reconstruct and verify by Sections9-10.

The width identity w_i-b_i=1+(ell-i)+sum_(t>i)b_t>=2 proves all channels
have M0>=4. Final width is one. A*B starts <=N and decreases. Every
frequency identity uses the actual modulus N, including wrapped sums.
There are K_i=2^b_i<=q^(ell-i-1) buckets. All record widths, array ranges,
source limits and trial caps hold on erroneous-label/measurement branches.

## 8. Fifteen conditional concentration events

recycle-sieve.md Section 7 gives the complete fifteen-event conditional
Chernoff proof, including all rounding, unmatched entries and finite bounds.
It shows stage shortage <=15 exp(-16lambda) with F=2^62lambda and quota
ratio q=5847/1000. The six later events cover ZV,D5,RV,D6,ZR,D7, including success1/5
for the new R-SUM channel, with all correlations accounted conditionally. Initial and final shortages are smaller; the total shortage
budget is <1/1024. Conditional product state laws justify induction after
availability and fixed-prefix retention, without independence of population
counts. Outer-phase, source-label, global-coin-cap and fresh verification
budgets are each <=1/1024. The same program succeeds with probability at
least 1019/1024, with fixed bounds on every branch.

## 9. Coarse phase reconstruction and a short exact candidate interval

Apply Section 3's unwrapping routine to alpha_0,...,alpha_J with theta=s/N.
When the outer estimates are good,

    dist(z,s/N) <= 2^(-J)/16.

Generate exactly the integers

    C = { t in [0,N): dist(t/N,z) <= 2^(-J)/8 }.

Use exact rational endpoints and ceil/floor, splitting a circle interval crossing
zero into two ordinary intervals and excluding N. Enumerate only integers in
these intervals, in increasing order. Never loop through all N integers. For
any z, including erroneous estimates, its cardinality is at most

    N/(4*2^J)+2 < 2^ell+2.

This uses N<2^(m+1) and J=m-1-ell. The weak bound <=2^ell+2 is used for resources.
The true s belongs to C on the good event. The all-outcome candidate bound is
important: an erroneous phase estimate cannot produce an unbounded search.

## 10. Full-secret verification and unconditional success

For each candidate t in C, test at most n+10 independent fresh source copies.
On one copy conditionally subtract t on its data register when the FIRST source
qubit is one, using Section 2, then measure that qubit in X. Reject the candidate
at its first minus; output the first candidate passing all n+10 tests. If none
passes, output zero.

For t=s every source component becomes |+> tensor |x>, so the true candidate
always passes. For t!=s, its two data basis states are distinct for every x;
the first qubit is I/2 and passes with probability 1/2. Fresh source copies
make the all-pass probability 2^(-(n+10)), conditional on any past transcript
that reaches that wrong candidate. Union over at most N candidates bounds any
false early acceptance by N*2^(-(n+10))<=1/1024. This verifies the entire secret,
not only parity, and counts failed attempts as well.

In the ideal latent-label, uncapped-coin sieve, shortages, outer-phase
error and false verification each have probability<=1/1024. Outside those
three events the true candidate is generated and returned. Transfer to the
hard global coin cap loses at most1/1024 by its additive coupling. Couple the exact latent-label analysis to the actual Section4 extractor;
the first-wrong-label union bound loses at most1/1024. Therefore

    Pr(output=s)>=1-5/1024=1019/1024>2/3.

This is an additive probability comparison, not conditioning the source
law on an observable good-label flag or on successful postselection. All stage, trial and
source caps are fixed beforehand; no average-secret guarantee is substituted.

For the n<=16 exhaustive branch the true candidate is in the enumerated
set and the only possible failure is an earlier false acceptance. Its
probability is <=1/1024 by the same argument. It therefore satisfies the
stated uniform 1019/1024 guarantee as well.

## 11. Elementary joint worst-case work, memories and source charge

Let L=L_0. The exact schedule gives L=O((log2 n)2^(c sqrt n)),
c=564341027/250000000, ell=Theta(sqrt n), log L=O(sqrt n), R=O(nL)
and sum_(i<ell)L_i<2L. These are every-branch bounds for this one program.

Actual classical arithmetic. For v-bit nonnegative inputs, schoolbook
multiplication scans each of the v multiplier bits, adding the appropriately
shifted multiplicand into a 2v-bit accumulator when that bit is one.
Each addition/comparison has O(v) bounded-fan-in bit operations, so the
product has O(v^2) logical bit work and O(v) scratch. Signs use a separate
bit and magnitude arithmetic. Restoring binary division scans v dividend
bits, shifts a remainder, compares/subtracts the positive divisor and emits
a quotient bit; each step takes O(v), giving O(v^2) logical work and O(v)
scratch. All loops are bounded by declared widths; leading zeroes do not
change the upper bounds. No large-integer instruction or uncharged product
primitive is used. The kernel binomials are their fixed consecutive-factor
products divided by the fixed factorials. All intermediate widths are O(n):
H<=2^n, each kernel has a fixed number of constant-degree terms, and all
numeric coefficients are fixed integers/rationals. Exact divisions by the
fixed denominators can use the same restoring routine. Every signed value,
carry, controller step and failed sampler draw is counted.

Peak memory and its addresses. Keep a label and classical physical-wire
index for each live phase qubit in a fixed number of old/new/population
buffers. There are O(L) records, O(L) bucket counters and O(L) phase wires.
Labels use O(n) bits and pointers O(log L+log n). Stream fixed source
arithmetic gates rather than retaining the whole computation. A single
source register and O(n) ripple/copy/uncompute scratch are live at a time.
Classical decoder, parameter, coin and ordinary arithmetic storage is
polynomial in n. Since L grows exponentially in sqrt n, all fixed polynomial
scratch fits O(nL) classical bits and O(L) qubits after enlarging absolute
constants over a finite prefix. Thus

 SC=O(nL), SQ=O(L), A_addr=ceil(log2(M_alloc+2))=O(sqrt n).

Here M_alloc includes ALL allocated bits/qubits, spare buffers, pointers,
inputs, outputs and current controller records. This is an actual space
count, not an assumption of free addresses. Addresses are known classical
base-plus-index values. Generate an A_addr-bit address by binary additions,
using O(A_addr) elementary bit accesses, EACH paying its full O(A_addr)
address charge. Emitting/copying it and selecting the classically addressed
gate fit O(A_addr^2) charged work per logical bit/gate instruction. A
constant number of such addresses and running cursors suffices. This is
the conservative O(n) allowance per logical instruction; no amortized
constant-time or quantum-addressed access is presumed. Classical arithmetic
has O(n)-bit scratch, and the quantum permutation's regular pattern is
regenerated backward when needed for cleanup. There is no retained
exponential circuit history, interpolation matrix or shared phase resource.

Source labels. Each controlled modular shift of Section2 has O(n) exact
Clifford+T gates and O(n) reused scratch. Generation and full addressing
therefore cost O(n A_addr^2)=O(n^2) per Hadamard test. Section4 uses
2(n+3)M_src tests per acquired copy, with M_src=O(sqrt n), giving
O(n^(7/2)) charged work per extracted label. Source acquisition costs n+1,
and all ancilla initialization, measurement, disposal and counter updates
fit this bound. The n+3 translation constants are generated by modular
doubling: each doubling, comparison and optional subtraction uses O(n)
logical bits, hence O(n^2) logical work over all constants and O(n^3)
charged work, whether precomputed once or conservatively regenerated per
copy. No iteration of U exponentially many times is performed.

For classical phase decoding, sample counts have O(log n) bits. The fixed
64 rational grid comparisons per level need O(log^2 n) schoolbook work.
Unwrapping uses binary rational denominators: halving, scaling a fixed
64-point alpha by a power of two, subtraction and circular comparisons
are O(n) logical operations per level, not a generic n-bit multiplication
at every step. Across n+3 levels this is O(n^2) logical work. The final
rounding of N times the rational estimate uses one O(n^2) schoolbook
product plus shifts/comparisons. With the full address-generation allowance,
all this classical decoding is O(n^3) charged work, below the per-copy
O(n^(7/2)) bound. The fixed rational decoder's finite generation is an
absolute counted cost, not a preloaded instance table.

There are at most R=O(nL) source LABEL extractions. They cost
O(n^(9/2)L) altogether, including every rejected/discarded acquisition.
Fresh final-verification samples are separately counted below; they are
not subjected to a label extraction and require only a controlled shift.

Sieve and exact coins. Stable counting sort and per-record differences
have O(n) logical bit work per record, including pointer/counter updates,
hence O(n^2 L_i) charged work per stage. All constant-degree correlation
kernels use O(n^2) schoolbook logical work per pair, including 625-term and
121-term evaluators and the finite small-H branch. Full addressing gives
O(n^3 L_i) charged work. Across at most n targets and sum_i L_i<2L this
is O(n^4 L), below source extraction. The proved fifteen-event stage
coin-call bound is7L_i/8. The literal global4R sampler-trial counter bounds
every failed fair draw, comparison, reset and zero-label coin. Each trial
uses O(n) logical operations, thus O(n^2) charged work; all physical trials
cost O(n^3 L). No expected-only runtime is substituted for these caps.

Final reconstruction and verification. The all-outcome candidate interval
contains at most2^ell+2 residues. Its exact rational endpoints and output
enumeration need polynomial work; each of at most(n+10)(2^ell+2) fresh
verification copies uses one O(n^2)-charged controlled shift. The bound
O(n^3(2^ell+2)) fits O(n^3 L), since q>2 and L>=F q^ell. All phase
estimates, counters, abort outputs, initialization and buffer release are
included. Exact parameter computations use polynomial bit work; L dominates
every fixed polynomial, so these also fit the displayed bound. The finite
n<=16 exhaustive branch is explicitly bounded; absolute outer constants
cover it and n=1 without altering an inside exponent coefficient.

Consequently the SAME program has on every branch

 T=O(n^(9/2)L), SC=O(nL), SQ=O(L),
 Q<=4(J+1)L+(n+10)(2^ell+2)=O(nL) for n>=17.

Substituting the proved L bound gives exactly the four declared envelopes.
All memories, sample counts and success bounds refer to this single
configuration and the same independent ideal-source promise.

## 12. Exact indices and a strict full-envelope improvement

Put c=564341027/250000000. The log2 of each resource envelope is
c sqrt n+O(log n), so its iterated logarithm is(1/2)log2 n+log2 c+o(1).
All four exact indices are1/2. A finite prefix and absolute outside constants
do not change these limits. These are upper-envelope indices, not matching
lower bounds on the algorithm or on the DCP.

RS6S used the same time polynomial n^(9/2)(log n), with
c_old=282336983/125000000. Here c=564341027/250000000<c_old,
with exact difference332939/250000000. Every corresponding full-envelope
ratio is2^(-(332939/250000000)sqrt n), tending to zero. This compares
proved upper guarantees, not lower bounds on the predecessor's actual
consumption or a generally optimal DCP algorithm. The new actual channel
and quota schedule are not an equivalent rewrite or loosened old claim.
No practical finite-size, fastest-known, new-index or cube-root claim is made.
All polynomial/log factors and the large fixed F reserve are preserved.

## 13. Provenance and finite evidence

Direct published sources are RR8,4e2ca900-70e1-4923-a469-ea5a1bc0e25b,
for the primary/secondary/tertiary and primary-V instruments, global coin
cap and finite diagnostics; VFD3-M4,6f4423a3-e180-476f-987a-b1c4cdaa898e,
for directly reused exact modular arithmetic, repeated-Hadamard source
extraction, rational phase decoder and fresh verification; and MDC1,
7c30b190-e90b-492c-b52c-29cf1a9da1a7, for directly consulted minimum-
feasible-capacity design. The exact source byte hashes were checked against
published evidence. Their relevant graph declarations/history were read;
provisional graph proposals are not mathematical premises or verified ancestry.

RS4,b16fcbf5-7e11-4148-80f1-cee7ae2df6b5, RS4V,
d034cb7a-4593-4053-a03d-387e4514da0e, RS5,
16b2bedd-417e-4fae-b787-a2490a825af2, and RS6,
c1dab991-5431-485a-bf2c-caa96a195ca6 supply the fully reproduced later
recycling developments. Their publication is checked before graph links;
no prior verdict validates the present algorithm. Through RR8 the stage
inherits SG6,dc8d6d56-9618-46bc-97a3-e9b18ec65099, PS7,
cda83fcf-1faa-41d5-b858-d5ec44122fe6, and the PG4 global-sampler foundation,
e40f2d5a-68c9-418b-b4e8-64a80305968e. The earlier PG2/PG3/PG5 gradient,
Fourier and adaptive-product development is historical context, with no
active subroutine or theorem from those implementations in RS7.

Earlier VFD3,c2e60e34-e31d-4a65-8f18-a420030cf3e4, VFD3-M,
42e58ec0-80c2-4963-9539-c4fdb27e3ea5, and the inherited FD2,
286f74f7-dd46-4db7-9fe2-031755c76a04 at
773a35a977a66bbe10fa6f8f6ea50c2021f0fba0 (outside this graph scope),
remain acknowledged through the exact VFD3 foundations reproduced here.
Standard CNOT combination, distribution flattening, phase estimation and
schoolbook arithmetic are not claimed as discoveries. Kuperberg's
arXiv:quant-ph/0302112v2 and arXiv:1112.3333v1 provide square-root-growth
context; no heuristic leading coefficient or black-box algorithm is used.
Every needed mathematical premise is present in this snapshot.

The archived diagnostic checks exact correlation/count/coin laws, positive
rational certificate identities, all-outcome call/output caps and actual
fifteen-event quotas. The fixed rational decoder generator/certificate is
retained. Finite checks assist debugging; they are not a replacement for
the universal proof, physical quantum execution or acceptance. The manifest
declares no hosted experiments. The obsolete gradient/Fourier/interpolation
helper files are removed because the actual program no longer uses them;
their predecessor snapshots remain preserved outside this candidate.
