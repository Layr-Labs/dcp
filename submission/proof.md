# PSR3: polynomial-space recomputation of all subset ranks

## Joint theorem, exact configuration and material provenance

For every N>=2 and fixed s modulo N, n=ceil(log2 N), the SAME uniform exact
Clifford+T / classical-bit program recovers the entire secret with
unconditional success>2/3 and these bounds on EVERY execution branch:

 T=O(n^11*2^((23/16)sqrt(n)*sqrt(log2 n))),
 S_C=O(n^2) bits, S_Q=O(n) qubits,
 Q=O(n^4*2^((11/16)sqrt(n)*sqrt(log2 n))).

Time/sample representatives apply for n>=2, with n=1 fixed absolute cost
and count. Outside constants are absolute. Growth indices are1/2,0,0,1/2.
The count law is0 under the canonical independent ideal-copy context; no
positive malformed-copy tolerance or maximum-tolerance impossibility is claimed.
Compared with the exponential-table construction, this trades slower time
and more source copies for polynomial classical storage. It does not claim
a cube-root algorithm, a new fastest-known algorithm, practical runtimes,
optimality or novelty for polynomial-space DCP merging.

For n<16777216 use the exact exhaustive baseline: for each t<N use n+2 fresh
controlled-subtraction/X tests and return the first all-plus candidate or zero.
The true t passes certainly and each false t passes with probability2^(-(n+2));
a union bound gives success>3/4. Q<=N(n+2), T=O(2^n n^4), and both spaces
are O(n^2) there. This fixed finite prefix fits the displayed envelopes with
absolute constants (for quantum space n^2<=16777216n). A source outside constant
as large as2^16777220 is allowed; this is explicitly not a practical assertion.
All remaining descriptions are for n>=16777216.

Set ell=ceil(log2 n), ellExt=ell+8ceil(log2(ell+1))+64,
T0=isqrt(n*ellExt-1)+1, m=ceil(3T0/4),
v=ceil(log2(m+1))+ell+5, b0=m-v, D=ceil((n-1)/b0), q=m^(D+1).
Positivity, width and pairing inequalities are proved below.
Set f0=32n/(32n-1), A0=m*f0,
Mgrid=2^20(q+1), hstat=n+ceil(log2(Mgrid+1))+ceil(log2(n+7))+20,
Kstat=2^32hstat, C=(n+5)Kstat+n,
Qstar=C*32m*A0^D, Qcap=ceil(1024Qstar),
p=n+ceil(log2(Qcap+2))+40.
Set G=2^100 n^5*2^m, E0=G, E_i=f0(mE_(i-1)+G),
Wstar=G+C*16*(mE_D+G), B=ceil(1024Wstar).
All these integers/rationals are computed EXACTLY with counted integer
arithmetic before source acquisition. isqrt is integer binary search with
schoolbook comparisons/products, not a real oracle. The program aborts and
returns zero BEFORE another source acquisition would exceed Qcap or a core
bit/gate step would exceed B. All setup, monitoring and cleanup are charged.

Material context is Oded Regev, A Subexponential Time Algorithm for the
Dihedral Hidden Subgroup Problem with Polynomial Space, quant-ph/0406151v1,
Section3 (https://arxiv.org/pdf/quant-ph/0406151v1). Its multi-input subset
merging motivates this regime. PSR3 instead ranks ALL solutions and discards
only a final singleton, proving a uniform bound for every current label list;
it does not assume a bounded bucket size or fresh uniform higher label bits.
Kuperberg arXiv:1112.3333v1 Sections4.2-4.3 supply collimation/reindexing context.
No external algorithmic theorem or earlier verdict is a correctness premise.

PSR3 materially uses the source-only label/gradient/all-moduli/root-frequency
arguments reproduced through locally archived COL6-COL13 (no submission IDs
while uploads are paused). Published COL3 is20dcb56f-cf80-4e95-8784-b2c66b9f6577;
its carried raw-aggregate, unused-top-bit, recovery and cutoff arguments are
reproduced. Published RLQGR2,8657ff0f-f4d3-4605-a583-a6d57d3205f4, supplies the
consulted mixed-source eigenlabel argument. Published PG4,
e40f2d5a-68c9-418b-b4e8-64a80305968e, supplies consulted reusable-gradient
kickback and charging one initial trace error across adaptive reuse. The
ordinary mixed-eigenlabel preparation here differs from PG4's Fourier circuit;
its Nam/Su/Maslov1803.04933v2 SectionII attribution is retained. Helpers are
fully reproduced. No predecessor Grover search, robust score, Fourier-source
oracle, purification access, free QRAM or fast-multiplication result is used.

This candidate carries the complete local PSR1/2 stream-rank circuit and
bit-serial controller, and the local COL14 known-frequency decoder. Its new
arity schedule, root output, odd-part estimator and literal caps are proved
here. No previous verdict is a premise or rebound to these claims.

## Counted source and constant permutations

Put chi_k=N^(-1/2)sum_x exp(2pi i kx/N)|x> and
phi_(k,s)=(|0>+exp(-2pi i ks/N)|1>)/sqrt2. Expanding the source and summing
its uniform x cancels unequal Fourier labels, giving exactly
rho_s=(1/N)sum_k |phi_(k,s)><phi_(k,s)| tensor |chi_k><chi_k|.
label-tools.md gives counted nondemolition eigenlabel extraction with K=N,
d=n, planned count Qcap, H=ceil(log2(Qcap(n+5)+2))+20, and
whole-computation error<1/2048. Given k, source
control is unchanged. Apply X to obtain the positive phase qubit
q_k(s/N)=(|0>+exp(2pi i ks/N)|1>)/sqrt2 up to a global scalar. Reset/discard
data before the next acquisition. The ideal-label comparison is unconditional,
not conditioning an IID assertion on correct extraction.

A known unit alpha mod N applied as y->alpha*y mod N on source data gives
rho_(alpha*s), since x->alpha*x is a bijection. Extend by identity for y>=N.
Clean evaluation uses n controlled modular additions of alpha*2^i into a
zero accumulator, copies the product, and reverses; apply the permutation
in place by compute-swap-inverse using alpha^(-1). Each complete-domain
ripple comparison/add/select has O(n) gates and reused O(n) scratch, so this
costs O(n^2) gates and O(n) qubits, including invalid-domain guarding. Euclid,
constants and controller work are charged. The same construction at width p
implements odd constant permutations modulo2^p. Fixed Boolean gates have
exact constant-size Clifford+T decompositions. No source inverse is used.
The reference below uses true labels, ideal gradient and exact known phases;
the actual finite circuits are compared additively with both caps enforced.


## One-qubit objects, signed aggregates and the regular instrument

For target width w<=n put Ftarget=2^(w-1). An object consists of a single
physical qubit q_a(F theta)=(|0>+exp(2pi i F a theta)|1>)/sqrt2, up to a
common scalar phase, and known classical integers a, rawLow and weight.
A base object has one fresh uniform w-bit label a, F=1,
rawLow=a mod Ftarget and weight=1. Its source supplier is specified below.

In the ANALYSIS ONLY, associate each object with a nonzero coefficient
vector c on its own original base controls. Its coefficients are in{-1,0,1},
its support is disjoint from any sibling's original controls, and

 F*a=sum_j original_a_j*c_j,
 rawLow=sum_j (original_a_j mod Ftarget)*c_j,
 weight=sum_j c_j.

The vector and original label tree are NOT stored. Three signed aggregate
integers per qubit suffice. Their bit lengths are bounded below. An original
label's unused top bit is never part of a pairing/ordering key.

A regular merge takes m same-level objects with common F. On their m index
qubits compute and MEASURE the key

 ((sum_i a_i*x_i) mod2^b, sum_i weight_i*x_i), b<=b0.

Known signed a_i are reduced modulo2^b classically. Controlled ripple adds
compute the first key. The second is Hamming weight at the first level
(all child weights1), and is identically zero at subsequent levels (weights0).
Thus it has at most m+1 values. Both key registers are reset using their
known measured classical bits; every reset/control bit is charged. The
remaining state is supported on the set S of m-bit strings with that key,
with its original phases and equal magnitudes. No phase value is measured.

Let M=|S|. The following explicit rank circuit implements consecutive pairs
in S without storing S or allocating an exponential classical array.
All strings are in ordinary binary numerical order. Enumerate every
classical z=0,...,2^m-1 using an m-bit counter, recompute key(z) by ordinary
counted integer operations, and accumulate M in m+1 bits (M can equal2^m).
Only the current mask, sums and count are retained.

For a quantum input x, define rank(x) as the number of valid z<x when x is
valid, and zero otherwise. Compute validity by the same coherent key circuit
and comparison with the measured key. To compute rank, enumerate all z;
when key(z) is valid, compare the known z with x and conditionally increment
an m-bit accumulator. Copy it to an output under validity, then reverse all
enumeration/increment steps and erase validity. This is a clean XOR evaluator
of a COMPLETE Boolean function. The accumulator never exceeds2^m-1, since
at most that many strings are strictly below any x. Quantum ripple arithmetic
and comparisons need O(n+m) scratch; no gate values from the entire loop
are retained. Reverse enumeration regenerates every classical decision.

The complete inverse function g(r) is the r-th valid string for r<M, and
zero for r>=M. Its XOR evaluator enumerates valid classical z while keeping
an m+1-bit classical count c; under equality of zero-extended quantum r with
c, XOR that known z into the target. Uncompute equality scratch each time,
then increment c. There is at most one match. An out-of-range r has no match
and returns zero. Thus this is a complete unitary XOR-function circuit,
including all invalid encodings, not a partial permutation prescription.
Its work is ONE enumeration, not a stored list and not a nested2^(2m) search.

Compute rank(x) into a fresh m-bit index r, then XOR g(r) into old x,
erasing old x on this measured subspace. All inverse scratch is cleaned.
Both steps are complete XOR-function unitaries on the entire Hilbert space;
rank and g are inverses on S because both enumerate S in the same order.
The resulting rank state is uniform in magnitude on[0,M). Measure its high
m-1 bits, retaining the LOW one-bit index. If the chosen last pair is a
singleton (M odd), discard ALL m child objects and regenerate them. Otherwise
exactly two strings x,y survive. Find those two classical masks by another
single enumeration using their known ranks. Store only the two m-bit masks.

The output label and aggregates are

 F_new=F*2^b,
 a_new=sum_i a_i*(y_i-x_i)/2^b,
 rawLow_new=sum_i rawLow_i*(y_i-x_i),
 weight_new=sum_i weight_i*(y_i-x_i)=0.

The first quotient is exact by the measured residue. The two amplitudes'
ratio is exp(2pi i F_new*a_new*theta), so this is a single qubit of the stated
kind, including negative a_new and arbitrary real theta. The conceptual
coefficient vector is the concatenation of(y_i-x_i)c_i. Disjoint child
supports make every coefficient still{-1,0,1}; x!=y and nonzero child
vectors ensure it is nonzero. The two weighted keys are equal, proving
weight_new=0. No conceptual vector is needed to compute any output.

Uniform conditional amplitudes imply that the GLOBAL singleton probability
is the number of odd classes divided by2^m. There are at most(m+1)2^b
classes, hence loss<= (m+1)2^b/2^m <=(m+1)2^(-v)<=1/(32n).
This is before conditioning on the measured key. An individual rare class
can be entirely singleton; no conditional-per-class bound is asserted.
The bound holds for EVERY classical label list, not merely an assumed
uniform list. Successful outputs always have balanced amplitudes, so the
same argument applies at every level and every phase value.

For target w cancel exactly w-1 bits in D_w=ceil((w-1)/b0) levels, with a
possibly shorter final block. When w=1 there are no regular levels. Depth-first
recursion generates each group of m children, retaining at most m-1 sibling
phase qubits per level. A failed merge releases all children before retrying.
At most m^D_w accepted base controls occur in one surviving object. Every
failed generation, source filter, measurement and enumeration is charged.

## Known-frequency root without a uniform-label assumption

Generate an EXTRA m objects after the above complete w-1 cancellation.
Now F=Ftarget, and every rawLow_i is divisible by Ftarget: its difference
from F*a_i is an integer combination of original top bits times Ftarget.
Tensor the m qubits and measure the EXACT integer key

 (sum_i(rawLow_i/Ftarget)*x_i, sum_i weight_i*x_i).

Use precisely the enumeration/rank/unrank/pair instrument just proved,
with this exact key in place of the residue key. When D_w>=1 all child
weights are zero, and the first coordinate is an integer between-q and q.
There are at most2q+1 classes. When D_w=0, w=1, rawLow_i=0 and weights1;
there are only m+1<=2q+1 classes. Thus root paired mass is at least
1-(2q+1)/2^m>=3/4, by the global parameter inequalities below.
The total accepted original-control count is m^(D_w+1)<=q.

Write each original uniform w-bit label as ell_j+Ftarget*t_j, ell_j<Ftarget.
Every earlier decision inspected only original lower labels and index/weight
information. Indeed at cumulative cancellation F, unused top contributions
are multiples of Ftarget/F; every regular residue cancels at most the remaining
w-1 bits. Root rawLow keys also omit the top bits. Therefore surviving unused
t_j remain independent fair bits conditional on those LOWER-bit choices,
NOT conditional on the full stored high-label transcript. All computational
partition probabilities depend on set sizes, not phases or top bits. A failed
unpaired root starts over with entirely fresh objects/copies.

For a selected root pair x,y, its signed conceptual coefficient vector has
rawLow sum0 and signed weight0, and is nonzero with entries{-1,0,1}.
If T is the number of its nonzeros, then T is even,2<=T<=q, with T/2 of
each sign. Consequently its full frequency difference divided by Ftarget is

 W=sum_j t_j*c_j ~ Bin(T,1/2)-T/2.

The characteristic function is E exp(2pi i W delta)=cos(pi delta)^T.
After measuring the pair identifier ONLY THEN inspect full stored phase
labels and compute W=sum_i a_i*(y_i-x_i). Keep every known W and its qubit
q_1(W*Ftarget*theta) for the odd-part estimator, including zero/nonunits.
Conditional on W, other forgotten history introduces no dephasing.
The root retries only an unpaired outcome, with probability of a pair>=3/4.
frequency-tools.md estimates the phase using this joint W/qubit law.
For two-adic parity only, repeat until W is odd, which has conditional
probability1/2 for every T>=2. That branch succeeds per trial with probability
at least3/8. Arbitrary odd W is never substituted for literal one in odd moduli.

## All-moduli source supply and full-secret recovery

Compute N=2^a M by trailing zeros, with M odd; this is not general factoring.
If M>1, put d=floor(log2 N), F=2^(d-1), f=F/2^a. Here d>=a+1, f is an
integer power of two and a unit modulo M. For each j=0,...,n+4 choose a CRT
unit alpha_j congruent to2^j mod M and1 mod2^a (at a=0 use2^j mod N).
Euclid/CRT computes it with counted polynomial bit work; gcd(alpha_j,N)=1.
Transform fresh source data by alpha_j, extract its uniform N-label k,
and keep only labels k<2^d. Success is2^d/N>=1/2, and retained labels are
independent uniform d-bit integers. Discard rejected copies, charging each.
After X the retained source controls are q_k(alpha_j*s/N).
The root(w=d) gives a known W and q_(WF)(alpha_j*s/N), whose phase is
2pi*W*2^j*(f*(s mod M)/M) modulo2pi. No unavailable source power is used:
alpha_j is a counted ordinary data permutation on each newly acquired copy.

For every j collect Kstat fresh known-frequency root outputs with phase
2pi W*2^j*vartheta, vartheta=f*(s mod M)/M. Measure in independent private
uniform X/Y bases and record(W,basis,outcome). frequency-tools.md proves
that finite empirical scoring on Mgrid rational phase candidates gives
circular error<1/32 simultaneously at all stages with failure<1/1024.
Its rational half-angle unwrapping and rounding recover the odd numerator
and the inverse of known f gives r=s mod M. At M=1 set r=0 and skip this.
Each qubit is measured/released before the next; only O(n^2) ordinary record
bits and a running grid maximum are retained. There is no grid-sized array,
FFT, physical arbitrary phase gate or phase-estimation oracle.

If a>0 prepare the single gradient described below before the two-adic
loop; if a=0 omit that preparation. Now write s=r+M*t, t in Z/2^a. At bit level ell=0,...,a-1 suppose t_low
contains its known ell low bits and set s0=r+M*t_low. A fresh untransformed
source, after label extraction and X, has phase q_k(s/N). Use the counted
gradient correction of gradient-tools.md to subtract known phase k*s0/N.
The reference phase is q_(k mod2^w)(t'/2^w), w=a-ell, t'=(t-t_low)/2^ell.
The reduced labels are independent uniform w-bit integers because2^w divides N.
No label filter is needed here. Repeat the root until W is odd, giving
relative phase(-1)^(W*t')=(-1)^t'. An X measurement gives the next bit EXACTLY in
the reference computation. Repeat and output r+M*t, the full representative s.
At most C=(n+5)Kstat+n completed root calls occur, counting every internal
pairing/parity retry in the budgets. On good odd-part estimation,
this is correct; even if a previous estimate were wrong, all qubits remain
balanced phases and the cost/partition bounds below still hold uniformly.
Correctness of earlier estimates is not a premise of these cost bounds.

## Counted approximate gradient and error transfer

gradient-tools.md supplies one actual approximate gamma_p from ordinary fresh
zero qubits, controlled modular translations, measurements and at most n+20
attempts. It acquires no DCP copies. Its trace-distance/abort allowance is
<1/1024, charged ONCE to all subsequent uses, not independently per reuse.
Ideal gamma is unchanged under translation, including on superpositions.
The source label k and known s0 are CLASSICAL, so compute
z=k*s0 mod N and c=floor(2^p*z/N) entirely classically by counted schoolbook
arithmetic. Controlled SUBTRACTION of c from gamma implements
exp(-2pi i c/2^p) on the source control. The exact reference correction is
exp(-2pi i k*s0/N); per use norm error<8/2^p. There are at most Qcap uses,
so telescoping quantum channels gives total error<=8Qcap*2^(-p)<1/1024.
All computations, constant loads, additions, inverse work and precision are
counted; no arbitrary rotations or phase oracle is free. Preparing gamma
before two-adic recovery may abort, but all acquired source copies still
count toward Q. Its ordinary preparation register is not part of source Q.

Actual source-label extraction uses planned count Qcap in label-tools.md.
Its whole-computation error<1/2048<1/1024 compares to true labels on the
UNCONDITIONAL exact ensemble. It remains uniform over adaptive CRT choices
and known estimates because every new source copy is independent and its
transformed Fourier label is uniform. Do not condition on correct labels
or absence of caps to claim uniform phases. Work/source caps enforce all
actual branch bounds even when labels/gradient/estimates are wrong.


## Reference expectations, hard cutoffs and complete counted implementation

A base object needs at most2 source acquisitions in expectation, including
its filter. For a regular level, fresh groups of m children are discarded
on failure and the success probability is at least1-1/(32n) for every label
list. Uniform conditional expectation and the geometric tail therefore give
EQ_0<=2 and EQ_i<=A0*EQ_(i-1), A0=m*f0. No independence of current labels
or their higher bits is required for the internal bound. At the root a fresh
trial has m children and acceptance at least3/4 for the estimator or3/8
for parity. Future trials use
fresh sources even when a trial's cost is correlated with its outcome. Thus
at most C calls have expected total acquisitions at most
C*(8/3)*m*2A0^D<=Qstar=C*32m*A0^D. Markov gives source-cutoff failure<=1/1024 in the
uncapped exact reference. The finite program aborts BEFORE exceeding Qcap.

A CORE step is one fixed-size Boolean bit operation/read/write, circuit gate,
measurement/reset, head move, source acquisition or bit of circuit generation,
excluding only the clock monitor's own work. Words, enumeration steps,
classical sums and whole gates' address descriptions are not free primitives.
Use a bit-serial finite-control generator with explicit work registers and
counted loop masks/pointers. Every m-bit enumeration value is generated,
every subset key recomputed, and every emitted gate/wire address constructed.

All arithmetic words below have at most3n bits, and m<=n. For each of2^m
masks, recomputing its key needs at most m signed additions/comparisons of
O(n) bits. Even using schoolbook bit arithmetic and O(n^2) control/address
generation per processed position, this is less than2^40 n^4 core work per
mask. A rank circuit adds an O(m)-bit comparison/increment, and its reverse;
unrank adds equality-controlled known-bit XORs and erases their scratch.
These have polynomially fewer positions than that allowance. A fixed number
of enumerations covers M counting, forward rank, inverse erasure, measured
pair recovery, metadata, initialization, resets and complete inverse work.
Hence2^50 n^6*2^m is a conservative per-merge/root allowance, without any
stored solution table or exponential gate stream. All loops are explicit
on the same counted controller. Clifford+T implements fixed Boolean gates
by exact constant-size NOT/CNOT/Toffoli decompositions. Signed arithmetic
and out-of-domain guards are finite complete Boolean functions.

Source extraction has2(n+5)*2^24 H tests with H<=2n. Each controlled ripple
translation, measurement, reset and generated address takes at most2^20n^4
core work. The label/phase decoder, Euclid, ordinary gradient preparation
with at most n+20 attempts, known corrections and all inverse work fit
2^80 n^8. Direction constants are generated before the clock by the counted
finite rational instructions in the helper. Thus G=2^100 n^5*2^m safely
covers a base object's expected work, the bounded initial gradient routine,
and each merge/root's nonrecursive work, with ample constant slack.

For internal retries E0=G and E_i=f0(mE_(i-1)+G) bound expected core work.
The exact finite recurrence evaluates to
 E_D=G*((32n*m+1)A0^D-32n)/(32n*(m-1)+1)<=2G A0^D,
because f0/(mf0-1)<=1. Including the initial gradient and all root trials,
frequency-tools.md bounds all grid postprocessing by(n+5)2^150n^12q<=E_D.
Thus Wstar=G+C*16*(mE_D+G) bounds all root trials, grid work and setup. B=ceil(1024Wstar) gives a core-clock abort
probability<=1/1024 by Markov in the uncapped reference. Counters check before
excess, not after. Every failed merge/root/filter is in these expectations.

The cost bounds remain uniform if an earlier phase estimate was wrong.
Fresh source controls after any known correction still have balanced
magnitudes and the declared initial target labels are uniform. The actual
phases then need not match their intended common theta, but all subsequent
computational subset partitions and selected pairs still leave balanced
one-qubit states. Their cardinality probabilities and metadata tests do not
inspect the phases. The root W test uses only the same uniform original
labels, so its expected-cost bound persists. Correct label-to-phase semantics
are used for correctness when previous estimates are right, never as a
hidden condition in the cutoff expectations. Actual wrong labels or an
imperfect gradient are handled by the unconditional finite-channel comparison;
syntactic caps bound their resources on every branch.

controller-tools.md details the per-mask n^4 bound and helper absorption:
2^s>=n^16, so the unchanged2^80n^8 helpers and a fixed number of
2^s*n^4 mask operations fit G=2^100n^5*2^s with leaf retry slack.
The full monitor/addressing overhead is n^2, proved with each monitor
bit access charged. These are implementation bounds, not free word costs.

## Global analytic bounds and simultaneous branch resources

Put Hscale=sqrt(n)*sqrt(log2 n) for ANALYSIS only. All runtime parameters
are the stated integers/rationals, with no real advice. The following safety
bounds hold for every n>=16777216, not merely finite diagnostics.

First ellExt<=n^(1/3). At n=2^24 this is128<=256. For ell=j>=25 use
n>2^(j-1) and j+8ceil(log2(j+1))+64<=2^((j-1)/3): at j=25 the left
side is129<=256, and each increment is at most9 while the left side is
at least128. Since(137/128)^3<2, induction preserves the inequality.
Thus m<=3sqrt(n*ellExt)/4+2<=3n^(2/3)/4+2<=n^(2/3).
Therefore v<=5ell/3+7<=2ell. The dyadic inequality n>=65536log2 n
holds at n=2^24 and throughout larger dyadic blocks by induction.
Since ell<=2log2 n and m>=3Hscale/4, we have m>=96ell>=16v.
Consequently b0>=15m/16>=1, D<=16n/(15m)+1<=n and m>=1024.
Also ellExt<=16ell, since ceil(log2(ell+1))<=ell/2 for ell>=24.
Thus log2 m<=(ell+log2 ell)/2+3<=ellExt/2.
Using m^2>=9n*ellExt/16 and mb0>=135n*ellExt/256 gives
 (n/b0)log2 m<=128m/135.
For m>=1024, 2log2 m+3<=m/32 by dyadic induction (2j+5<=2^j/32,j>=10).
It follows that
 log2 q<=(n/b0+2)log2 m<=128m/135+2log2 m<=m-4.
Hence2^m>=16q>=4(2q+1), proving root paired mass>=3/4 uniformly.
This uses no higher-label distribution assumption at an internal merge.

For conservative all-size estimates, m>=3Hscale/4, b0>=15m/16 and
log2 m<=2log2 n/3 give
 log2 q<=(128/135)Hscale+(4/3)log2 n.
Also m<=4Hscale from ellExt<=16ell, ell<=25log2 n/24 and the ceilings.
The dyadic bound n>=65536log2 n gives Hscale<=n/256 and
Hscale>=256log2 n. Thus log2(q+1)<n/4 and hstat<=2n,
Kstat<=2^33n and C<=2^35n^2. Bernoulli and D<=n yield A0^D<=2m^D.
The literal budgets satisfy Qstar<=64Cq and Wstar<=100GCq, so
 Qcap<=2^80n^4*2^Hscale, B<=2^220n^9*2^(5Hscale).
These imply source-label repetition H<=128+6log2 n+2Hscale<=2n,
p<=n+128+5log2 n+2Hscale<=2n; gradient repetition is O(log n).
All helper widths and finite capped costs are therefore justified.
The clock width is Theta(Hscale), using G>=2^m and these upper bounds.

## Sharper asymptotic coefficients with exposed outside constants

Set the ANALYTIC threshold n0=2^(2^20), never a runtime branch or advice.
For n>=n0 put x=log2 n>=2^20. Dyadic induction gives log2 x<=x/8192;
with81<=x/1024, the parameter satisfies
 ellExt<=x+8log2 x+81<=(1+1/512)x.
Therefore m<=3Hscale(1+1/1024)/4+7/4<=769Hscale/1024.
Also ellExt<=2x<=n^(1/64)/4: take logarithms and use3+log2 x<=x/64.
It follows that m<=n^(65/128). For the cancellation margin, ell<=n^(1/8)
for n>=2^64 by dyadic induction; hence v<=2ell<=m/256 at n>=n0,
using m>=3sqrt(n)/4 and n^(3/8)>=2048/3. Thus b0>=255m/256.
Together with m>=3Hscale/4 these give
 log2 q<=(n/b0+2)log2 m<=(104/153)Hscale+(65/64)log2 n.
Here(256/255)(4/3)(65/128)=104/153 exactly. Consequently
 Qcap<=2^80n^4*2^((11/16)Hscale),
 B<=2^220n^9*2^((23/16)Hscale),
since104/153<11/16 and769/1024+104/153=224153/156672<23/16.
The finite interval n<n0 has bounded ratios to the new positive envelopes;
the all-size cap estimates above and finite exhaustive prefix are safely
absorbed by an additional outside factor2^(4n0) times the old implementation
constant. Such enormous constants are explicit asymptotic accounting, not a
practical runtime claim or an unknown coefficient hidden inside an exponent.

Signed metadata are bounded by q*2^n in magnitude, so have at most3n bits;
log2 q<=n by the same inequalities. A complete recursion frame keeps at
most m such records and m-1 sibling one-qubit states. Since
m(D+1)<=16n/15+2m<=2n. Thus the ENTIRE classical frame allocation is
O(n^2) bits. Enumeration stores only current masks/counts/sums, at most two
selected masks and scalar parameters, never an array of size2^m or q.
The Kstat estimator records and streamed grid maximum also fit O(n^2).
Known CRT constants, rational parameter numerators/denominators, schoolbook
workspace and the finite direction table fit O(n^2) as well. Parameter power
numerators have O(D log n)=O(n) bits here; their generation is counted.
No previous failed history or complete generated gate program accumulates.

Quantum space is at most(m-1)(D+1) live sibling qubits, O(m) old/rank/compare
scratch in the active merge, O(n) coherent key/ripple arithmetic, one n-bit
source data system and the p-bit gradient. Stages reuse scratch, so it is
O(n) jointly with the above classical bound. No coefficient vectors, original
label trees, exponentially many equality flags or QRAM live in quantum space.
All reserved registers and work tables are initialized/reset with charged work.

controller-tools.md proves the complete bit-serial implementation and
O(n^2) fully charged work per core step, including its own monitor accesses,
wire/gate addressing and direct source charge n+1. Its address length is
O(log n), clock width O(sqrt(n log n)); no counter update or word is free.
Thus every branch has T=O(n^11*2^((23/16)Hscale)).
Abort cleanup resets the O(n) quantum systems and scans O(n^2) classical
bits with full addressing/control. Deterministic parameter/table generation,
allocation/initialization and final classical output are polynomial plus fixed
constants, absorbed by the same envelope. All four bounds hold together
on every branch, including wrong estimates and source/core aborts.

Source-label replacement, gradient preparation/abort, finite phase rounding,
odd-part empirical estimation, source cutoff and core cutoff each cost at
most1/1024 in the unconditional comparison with the uncapped exact reference.
That reference's final two-adic outputs are exact on correct earlier estimates,
and every phase generator terminates almost surely with finite expected cost.
Union bounds and trace contraction, not conditioning on a favorable event,
give success>=1-6/1024>2/3 for large n. The fixed prefix succeeds>3/4.

The logarithms of T,Q are explicit positive constants times
sqrt(n)*sqrt(log2 n)+O(log n), giving exact growth index1/2. Classical
polynomial storage and linear quantum space have index0. The canonical
malformed-copy count is0 under the independent ideal-copy model. No positive
corruption guarantee or impossibility for a larger count is inferred.
