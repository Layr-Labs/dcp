# PS7: same-bucket sum pooling with smaller joint exponential envelopes

PS7 directly reuses SG6 submissiondc8d6d56-9618-46bc-97a3-e9b18ec65099's
triangular sum-rescue channel and PG5's adaptive exact source framework.
Instead of fixed four-input groups, it pools ALL first-pass SUM states within
each bucket and pairs them by original positions. pooled-sieve.md proves the
full conditional law, new three-event shortage bound and exact parameters.
All four resource envelopes improve jointly to coefficient1180959/500000;
success and clean-input tolerance are unchanged. No prior verdict is a premise.

The inherited VFD3-M4 foundation is submission
6f4423a3-e180-476f-987a-b1c4cdaa898e, candidate
c3719a087388963198f068135526bd69fe3ab877. Its spectral ensemble,
exact arithmetic, outer decoder and primary flat-difference channel
are reproduced below; PS7 replaces the quota/instrument proof explicitly. Earlier VFD3/FD2 ancestry remains acknowledged in
Section 13. No prior mathematical verdict is a premise.

## 1. The theorem and the exact algorithm configuration

For every integer N >= 2 and fixed s in Z/NZ, let n=ceil(log2 N). PS7
receives only fresh independent copies of the mixed state in rules.md. It
outputs the entire s with unconditional probability at least 1019/1024.
The same execution has, on every branch, including every abort,

    T(N,s)   = O(n^3 (log2 n) 2^((1180959/500000) sqrt(n)+21 sqrt(log2 n))),
    S_C(N,s) = O(n (log2 n) 2^((1180959/500000) sqrt(n))),
    S_Q(N,s) = O((log2 n) 2^((1180959/500000) sqrt(n))).

These asymptotic envelopes apply for n>=2. The n=1 cases are explicitly
handled below and have absolute finite costs. Each envelope has growth
index exactly 1/2. Constants are absolute, independent of N, s, outcomes
and memory contents. They include source calls, classical bit work,
addressing, generated gates, measurements, initialization and all failures.
The structured objects declare these exact envelopes. Both time exponent
coefficients 1180959/500000 and 21 are explicitly proved; no unspecified
inside big-O coefficient is replaced by a number.

For n<=16, PS7 exhaustively tests t=0,...,N-1 by Section 10 with k=n+10
fresh tests per candidate. It returns the first candidate passing all tests,
or zero if none passes. This is a fixed finite prefix of the single algorithm.
It does not run the sieve or generate the phase table.

For n>=17 put h=n+1, m=floor(log2 N), q=55/8, r=25/9.
`clog(x)` is the bit length of x-1. Define the exact integers

    ell=min{v>=1 : v+sum_(j=0)^(v-1)floor(r*j)>=m-1},
    J=m-1-ell, lambda=clog(1024*h),
    M=8192*lambda, F=2^36*lambda,
    L_i=ceil(F*q^(ell-i)), i=0,...,ell,
    R=4*(J+1)*L_0, global_coin_trial_limit=4R,
    a_phase=clog(2^20*R), t_phase=n+a_phase+4, k=n+10.

Compute ell by binary search on[1,m-1] and the displayed finite sum; its
upper endpoint is feasible. All rational powers/ceilings are exact integer
operations, L_i=ceil(F*55^t/8^t). For i=0,...,ell-1 greedily allocate
b_i up to floor(r*(ell-i-1)) until their sum is exactly J. Capacity guarantees
this. For each target j=0,...,J allocate a_i greedily from b_i until sum a_i=j,
and let c_i=b_i-a_i. These widths are deterministic, independent of outcomes.
The exact bounds 2^r<q<2^(1391/500),
ell<=(849/1000)sqrt(n)+2 and ell=Theta(sqrt n) are proved from small rational
inequalities in pooled-sieve.md Section3. They imply
L_0=O(log2(n)*2^((1180959/500000)sqrt(n))). No guessed exponent constant is used.

Every abort outputs the n-bit encoding of zero and releases its workspace.
All loops, allocations and return values are defined on every measurement
string. No unbounded repetition, favorable-outcome conditioning, oracle,
instance-dependent advice or uncharged preparation is part of PS7.

The source, arithmetic and outer decoder foundations are reproduced below.
The original flat-difference foundation derives from FD2 submission
286f74f7-dd46-4db7-9fe2-031755c76a04, candidate
773a35a977a66bbe10fa6f8f6ea50c2021f0fba0 (outside this challenge scope),
through the explicitly named VFD3/MDC1/PG sources. The new pooled-sum
instrument, distribution proof and quotas are in pooled-sieve.md; no
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
not the PS7 schedule. A Boolean MUX(control,x,y) is

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
of N and s. PS7 generates it once by the finite rational schedule in
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

## 4. Source-only phase labels through binary phase estimation

For analysis define omega=exp(2*pi*i/N),

    chi_y = (1/sqrt(N)) sum_x omega^(-yx)|x>,
    q_y = (|0>+omega^(sy)|1>)/sqrt(2), Q_y=|q_y><q_y|.

Direct expansion of matrix entries gives

    rho_s = (1/N) sum_(y=0)^(N-1) Q_y tensor |chi_y><chi_y|.

Indeed the cross entry indexed by x,z sums omega^(y(z-x-s)), which vanishes
unless z=x+s mod N, and the diagonal blocks agree as well. Also U chi_y=omega^y
chi_y. This is an ensemble identity for the given mixed state; it supplies no
accessible hidden register or additional source operation to the algorithm.

The actual PS7 extractor is specified in phase-labels.md and fast-labels.md.
Its phase and shared gradient registers both have t_phase=n+clog(2^20 R)+4
bits. A counted reciprocal is generated once, then exact coherent modular
translation implements all powers together. The binary inverse Fourier
transform is exact in the ideal-gradient analysis, using recursive product
phases implemented with clean reversible adaptive multiplication and
additions into the appropriate top bits of the shared gradient. No Fourier
phase is truncated. Measured-residue rounding uses the same explicit fast
integer product. All data permutations extend to invalid encodings, and no
source inverse, QRAM or arithmetic/Fourier oracle is assumed.

Exact ideal QPE has label-error probability less than 1/(2^23 R) per source.
Its union across R acquisitions is less than 2^-23. Actual bounded gradient
preparation contributes input trace distance less than 2^-36 and abort less
than 2^-122. The global channel comparison costs less than 1/1024 in total.
Only the ideal gradient is assumed unchanged; actual errors are not refreshed
or declared independent. The first source phase qubit is retained. Every required circuit identity and charged bit algorithm is in
phase-labels.md, fast-labels.md and adaptive-arithmetic.md.

## 5. Exact primary categories and whole-bucket sum rescue

At a stage, labelsu are independent uniform in[0,B) with qubitsq_(A*u).
Decomposeu=r0+2^a(v+M0*h0), bucket by(r0,h0), and pair consecutive original
positions within each bucket. Middle valuesv remain iid uniform in[0,M0),
M0 an even power of two>=4; at most one input per bucket is unmatched.
Primary CNOT/target measurement yields a difference or SUM. Difference
flattening gives a kept uniform labeld in[0,M0/2) with probability1/4;
SUM has probability1/2 and a triangular middle-sum label in[0,2M0-2].
Rejected differences form the remaining category of probability1/4.

Hold every SUM state. Within its same bucket, pair SUM states in ORIGINAL
PAIR order, never by sum value. Their frequencies share offset2f0, so a
second difference cancels it, leavingq_(A*2^a*d), d=|sum1-sum2|. The exact
C_d flattening in pooled-sieve.md makes each rescue output uniform in[0,M0/2),
with conditional successp_M=1/6+1/(12M0^2). Discard the second-pass SUM
outcomes and at most one unpaired primary SUM per bucket; PS7 has only two
passes. No new source copies or quantum copying are used.

pooled-sieve.md Sections1-2 prove the complete primary category instrument,
conditional triangular SUM laws, rescue count/density identities and product
law. Given all primary categories and rescue keep flags, every primary/rescued
output is independent uniform with its correct phase qubit. Primary and SUM
values belong to disjoint input pairs. Pair assignment uses only categories,
bucket and original positions. Availability and fixed-prefix retention
therefore preserve the next-stage product law, without assuming independence
of the marginal primary-kept and SUM COUNTS or conditioning on middle values.

## 6. Exact coins with one global finite trial cap

For primaryd in(0,M0/2), use numeratorM0, denominator2(M0-d). For rescue,
C0=M0(2M0^2+1)/3, C_d=C0-M0*d^2+(d^3-d)/2; use numeratorC0,
denominator2C_d. Keep zero and rejectd>=M0/2. Every numerator is <=its
positive O(n)-bit denominator by the exact count proof. Drawclog(D) fair bitsV,
retry whenV>=D and otherwise accept whenV<numerator. Cubic counts use
charged adaptive multiplication. All fair bits, resets and rejected draws
are counted.

One counter covers all sieve coin trials, with hard limit4R. Abort to zero
if another trial is required after that cap. WithP primary pairs andZ SUM
states, primary coin calls are <=P-Z and rescue calls<=floor(Z/2), so total
<=P<=L_i/2 on EVERY branch. Since sum_(i<ell)L_i<2L_0, all batches need
fewer than(J+1)L_0<R coins. The ideal-coin coupling and adaptive Bernoulli
bound in fast-labels.md give cap-abort probability<=exp(-R/4)<1/1024.
Never condition on no cap and assert an exact physical law; transfer it
additively. All branches obey the literal4R trial work bound.

## 7. The complete variable-width batches

Generate the fixed rational outer table and one bounded approximate t_phase-bit
gradient with all capped attempts counted; abort before source acquisition
if preparation fails. Generate the reciprocal and all adaptive constants with
full bit costs. Initialize the global coin counter. Forj=0,...,J in sequence:

1. Acquire exactly4L_0 source copies and extract reported labels with the
   exact source circuit. Keep the firstL_0 labels<2^m, discard extras,
   abort on shortage. SetA=1,B=2^m.
2. Fori=0,...,ell-1, bucket currentL_i records witha_i,c_i. Make primary
   pairs and process all of them in bucket/original order, collecting kept
   differences and separate same-bucket SUM buffers. Pair and process those
   SUM buffers by original-pair order; discard second-pass SUM outcomes.
   Output all primary successes first, then all rescue successes in fixed
   bucket/pair order. Use the shared trial cap throughout. Keep the first
   L_(i+1) outputs, discard extras and abort on shortage. SetA<-A2^a_i,
   B<-B/2^(b_i+1), resetting/reusing old records and temporary SUM buffers.
3. AtA=2^j,B=2,L_ell=F, retain the first2M label-one qubits or abort.
   MeasureM inX andM inY and obtainalpha_j by Section3. Release this batch
   and retain onlyalpha_j.
4. Reconstruct and verify by Sections9-10.

Forw_i=m-i-sum_(t<i)b_t, w_i-b_i=1+(ell-i)+sum_(t>i)b_t>=2, soM0>=4;
the final width is1. OrdinaryA*B starts<=N and decreases, including odd and
compositeN without a modulus substitution. Bucket countK_i=2^b_i<=q^(ell-i-1)
by2^(25/9)<q. Every record range and array cap remains defined on erroneous
labels and arbitrary measurement strings, not merely on successful branches.

## 8. Three-event shortages and the joint probability accounting

The elementary Chernoff bound for independent Bernoulli variables is
Pr(X<=(1-delta)mu)<=exp(-mu*delta^2/2). Its exponential-moment proof uses
Eexp(-uX)<=exp(mu(exp(-u)-1)), u=-ln(1-delta), Markov and
(1-delta)ln(1-delta)+delta>=delta^2/2, verified by differentiation.

Fix a stage bucket vector. WithI=L_i,K=2^b_i, primary-pair countP>=(I-K)/2,
primary-keptD~Bin(P,1/4), SUMcountZ~Bin(P,1/2), and pooled pair count
U>=(Z-K)/2. D andZ are NOT asserted independent. Conditional on all primary
categories, rescue countW~Bin(U,p_M>=1/6). Chooseepsilon=1/4096. The three
events D>=(1-epsilon)P/4, Z>=(1-epsilon)P/2 and W>=(1-epsilon)U/6 imply
Y=D+W>=(7/48-epsilon/6)I-11K/48, above the exact next quota. The surplus
q*(7/48-epsilon/6)-1=457/196608>1/512 handles ceilings with the statedF.
On the Z event, P>=Fq^(ell-i-1) and U>=Fq^(ell-i-1)/16. Separate primary
Chernoff bounds and a rescue bound CONDITIONAL on each good category vector
give shortage<=3exp(-16lambda), as fully proved in pooled-sieve.md Section4.
No false independence between D,Z,U is used.

Initial qualification shortage<=exp(-L_0/4), final label-one shortage
<=exp(-F/16), andF/M=2^23>=8. At mosth(h+2) checks have total failure
<=3h(h+2)exp(-16lambda)<1/1024. The exact conditional output-product law
preserves induction after availability and prefix retention. Outer phase
errors on available batches remain<=4h exp(-M/2048)<1/1024. Source/gradient
comparison and the global coin cutoff each cost<1/1024 additively; fresh
verification has its own1/1024 budget. No estimate is asserted on an aborted
branch. All caps and resources are fixed before the good-event analysis.

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
hard global coin cap loses at most1/1024 by its additive coupling. Transfer
exact source/gradient extraction to the actual prepared resource loses at
most1/1024 by the whole-computation comparison. Therefore

    Pr(output=s)>=1-5/1024=1019/1024>2/3.

The trace-distance transfer is a probability comparison, not an observable
good-gradient flag or conditioning/postselection. All stage, trial and
source caps are fixed beforehand; no average-secret guarantee is substituted.

For the n<=16 exhaustive branch the true candidate is in the enumerated
set and the only possible failure is an earlier false acceptance. Its
probability is <=1/1024 by the same argument. It therefore satisfies the
stated uniform 1019/1024 guarantee as well.

## 11. Joint worst-case resources in the charged model

All estimates in this section apply to the concrete execution just specified,
not merely to an average-success branch. Bit accesses as well as quantum gates
pay their full address charge. Work is sequential; no concurrency is credited.
Let L=L_0=ceil(F*q^ell), q=55/8,F=2^36lambda.
pooled-sieve.md proves ell<=(849/1000)sqrt n+2, log2q<1391/500,
ell=Theta(sqrt n), and

    L=O(log2(n)*2^((1180959/500000)sqrt(n))), sum_(i<ell)L_i<2L.

Consequently logL,logR=O(sqrt n), t_phase=O(n), M=O(log n), and R=O(nL).
Every fixed/generated constant, current local program and input register is
counted. The adaptive local descriptions have log sizeO(logn+sqrt(logn)),
which is o(sqrt n), so their extra allocation fits the following bounds.

Space and addressing. Store a label and classical wire index for each live
qubit, in old/new arrays, together with bucket counts and stable prefix pointers.
There are O(L) records and O(L) buckets. A label uses O(n) bits and each pointer
uses O(log L)=O(sqrt(n)) bits. The quotas, schedule, phase estimates, controller,
classical arithmetic and fixed rational table use O(n^2)+O(1) further bits.
The quantum arrays hold at most a constant multiple of L single phase qubits.
Only one source sample and O(n*2^(21sqrt(log2 n))) arithmetic/QPE scratch
qubits are live at a time. Classical pointer/local-program records use
O(n*2^(21sqrt(log2 n))*A_addr) further bits. Both fit the stated envelopes,
as proved in adaptive-arithmetic.md; they are not assumed free.
Batches are sequential. Classical scratch and quantum scratch are reused.
Thus

    S_C = O(nL),     S_Q=O(L),

including the subpolynomial-times-linear local scratch and pointer records.

This includes allocated spare output arrays, input/output buffers, counters,
all table data and the generator's storage. Freed/reset registers are reused;
only current local arithmetic/Fourier descriptions and Boolean-value
history are retained, fully counted, then released/reused. No instruction
log of the exponentially many whole-sieve operations is kept. The total allocated bit-plus-qubit
count is O(nL); its address length is therefore

    A_addr = ceil(log2(allocated bits and qubits + 2))=O(sqrt(n)).

Address-generation work is charged explicitly, including the indexed bit
accesses used while constructing an address. A constant number of address
buffers, loop counters and block bases suffice. For each logical instruction,
ordinary binary addition/subtraction/multiplication by a fixed small stride
constructs its O(A_addr)-bit wire addresses using O(A_addr) elementary bit
accesses. Charge O(A_addr) for each such access as well as the gate's own
addressing cost. Copying or emitting a complete address buffer also costs
O(A_addr^2) by this accounting. We use this straightforward worst-case
O(A_addr^2) cost per instruction, not an unproved amortized O(A_addr) generator.
The fixed modular Boolean template can be streamed. For the adaptive
arithmetic, padded pointer records and current local gate lists, with all
O(A_addr)-bit instruction copies charged, give the same O(A_addr^2) allowance.
Their explicit layout, sizing and memory proof is in adaptive-arithmetic.md;
no multiplication of two variable wire indices is assumed free.

Thus an O(n)-gate modular permutation from Section 2 is generated and applied
in O(n*A_addr^2)=O(n^2) charged work. The actual source extractor fuses controlled powers by the explicit counted
reciprocal circuit in fast-labels.md; no exponentially repeated translation,
arithmetic oracle or uncharged diagnostic builder is part of the program.

Source labels. The exact reciprocal/Fourier framework in fast-labels.md uses
adaptive-arithmetic.md's fully counted integer product. Including all generated
matrices and uniform local circuit/pointer records, per-source logical work is
O(n*2^(21sqrt(log2 n))). Every instruction pays the full O(A_addr^2)=O(n)
bit/address-generation allowance, giving charged work
O(n^2*2^(21sqrt(log2 n))) per source and
O(n^3*L*2^(21sqrt(log2 n))) across R=O(nL) acquisitions. Exact rounding,
preprocessing, source charge, resets, scratch and failures are included.
All extra local records have log size O(log n+sqrt(log n))=o(sqrt n), so
fit O(nL) classical/O(L) quantum before the address bound is used.

Sieve work. Stable bucket grouping and ordinary label updates use O(n)
logical work per record. Rescue C_d and coin parameters require exact
degree-three products, cost O(n*2^(20sqrt(log2 n))) logical work per group.
The full O(A_addr^2)=O(n) charge, sumL_i<2L and O(n) batches give
O(n^3 L*2^(20sqrt(log2 n))) work. Each O(n)-bit sampler trial costs O(n^2)
charged work; at most4R trials globally cost O(n^3 L). All rejected draws,
measurements, resets and counters are included. Both fit the source21 term.

Final reconstruction and verification. The candidate interval always has at
most 2^ell+2 integers. Its endpoints require O(n)-bit rational arithmetic;
with the same conservative charging, O(n^3) work suffices. Each of at most
(n+10)(2^ell+2) verification copies uses one O(n)-gate permutation, costing
O(n^2) including generation, addressing and its n+1 source charge. Therefore
O(n^3*(2^ell+2)) bounds final verification. Since L>=F*q^ell and q>2, this is
O(n^3 L), also within source work. Saving phase estimates, generating the
integer parameter schedule, initializing arrays and writing the final output
fit O(n^3*L*2^(21sqrt(log2 n))). The rational table is a fixed finite computation with an
absolute time/space constant charged to these bounds.

Consequently the one program, before assuming successful measurements, obeys

    T=O(n^3*L*2^(21sqrt(log2 n))),       S_C=O(nL),       S_Q=O(L).             (11.2)

Substitution of the L bound above gives the envelopes in Section 1. The finitely many
n<=16 cases have bounded input sets and at most 2^16*26 tests. Enlarging
absolute outer constants covers those instances as well, including n=1.

## 12. Exact indices and joint comparison

Putc=1180959/500000. The logarithm of every envelope isc sqrt n+O(log n),
including the time21sqrt(log2 n), polynomial powers and explicit log2n.
Its iterated logarithm is(1/2)log2n+log2c+o(1); all four exact indices are1/2.
The n=1 finite prefix and outer constants do not alter these limits.
Relative to SG6 every resource ratio is2^(-(481/200-1180959/500000)sqrt n),
tending to zero with the same error context. This is a strict full-guarantee
improvement, not a smaller time index, practical timing claim, optimality,
fastest-known DCP result or cube-root theorem. The larger finiteF is explicit.

## 13. Provenance and finite evidence

Direct sources include SG6 dc8d6d56-9618-46bc-97a3-e9b18ec65099 and PG5 7e1c8dba-adc8-46db-bf59-1f31688d41c2 and PG4 e40f2d5a-68c9-418b-b4e8-64a80305968e and PG3 5a99915d-bf94-4f6a-8969-5cc6e601a1a9,
PG2 873cba1f-780f-4fad-bd5b-9cf12b8de874 (unpublished after failed review),
MDC1 7c30b190-e90b-492c-b52c-29cf1a9da1a7 and the directly consulted
VFD3-M4 6f4423a3-e180-476f-987a-b1c4cdaa898e. Their retained material and
changes are identified at the beginning and in fast-labels.md. Earlier
VFD3 c2e60e34-e31d-4a65-8f18-a420030cf3e4 and VFD3-M
42e58ec0-80c2-4963-9539-c4fdb27e3ea5 remain acknowledged; the inherited
FD2 source is 286f74f7-dd46-4db7-9fe2-031755c76a04, candidate
773a35a977a66bbe10fa6f8f6ea50c2021f0fba0, outside this challenge scope.

Known square-root-growth context includes Kuperberg,
arXiv:quant-ph/0302112v2 Theorem I.1/Sections III,V and
arXiv:1112.3333v1 Sections 4.3,4.6. Its Section 4.5 heuristic constant
is not used. Nam/Su/Maslov arXiv:1803.04933v2 Section II motivates the
reusable gradient idea; all actual needed circuit proofs are reproduced.
No external retrieval or accepted verdict is a proof premise.

The current archived diagnostic checks exact pooled-category/output laws,
triangular counts and all new quota margins, with the fixed outer-decoder
constant generator/certificate also retained. Superseded arithmetic, QFT and
preparation diagnostic programs were run from frozen predecessor trees and
are historical checks; they were removed here to reduce duplicate input.
Their complete analytic arguments remain in proof.md, phase-labels.md,
fast-labels.md and adaptive-arithmetic.md. Every required proof premise is
in this snapshot, not a claim that a past test or verdict establishes PS7.
No hosted experiments are declared.
