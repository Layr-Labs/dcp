# PSR4: quantum-counted pairs with polynomial classical storage

## Joint theorem, exact configuration and material provenance

For every N>=2 and fixed s modulo N, n=ceil(log2 N), the SAME uniform exact
Clifford+T / classical-bit program recovers the entire secret with
unconditional success>2/3 and these bounds on EVERY execution branch:

 T=O(n^128*2^((33/32)sqrt(n)*sqrt(log2 n))),
 S_C=O(n^2) bits, S_Q=O(n) qubits,
 Q=O(n^4*2^((33/64)sqrt(n)*sqrt(log2 n))).

Resource representatives apply for n>=2, with n=1 fixed absolute cost,
storage and count. Outside constants are absolute. Growth indices are1/2,0,0,1/2.
The count law is0 under the canonical independent ideal-copy context; no
positive malformed-copy tolerance or maximum-tolerance impossibility is claimed.
Compared with the exponential-table construction, this trades slower time
and more source copies for polynomial classical storage. It does not claim
a cube-root algorithm, a new fastest-known algorithm, practical runtimes,
optimality or novelty for polynomial-space DCP merging.

For n<1048576 use the exact exhaustive baseline: for each t<N use n+2 fresh
controlled-subtraction/X tests and return the first all-plus candidate or zero.
The true t passes certainly and each false t passes with probability2^(-(n+2));
a union bound gives success>3/4. Q<=N(n+2), T=O(2^n n^4), and both spaces
are O(n^2) there. This fixed finite prefix fits the displayed envelopes with
absolute constants (for quantum space n^2<=1048576n). A source outside constant
as large as2^1048580 is allowed; this is explicitly not a practical assertion.
All remaining descriptions are for n>=1048576.

Set ell=ceil(log2 n), m=isqrt(n*ell-1)+1, t=m, R=1, L=2,
v=ceil(log2(m+1))+ell+5, b0=m-v, D=ceil((n-1)/b0), q=m^(D+1).
Positivity, width and pairing inequalities are proved below.
Set f0=8n/(8n-1), A0=m*f0,
Mgrid=2^20(q+1), hstat=n+ceil(log2(Mgrid+1))+ceil(log2(n+7))+20,
Kstat=2^32hstat, C=(n+5)Kstat+n,
Qstar=C*32m*A0^D, Qcap=ceil(1024Qstar),
p=128n.
Set G=2^10000 n^100*2^(ceil(m/2)+3), E0=G, E_i=f0(mE_(i-1)+G),
Wstar=G+C*32*(mE_D+G), B=ceil(1024Wstar).
All these integers/rationals are computed EXACTLY with counted integer
arithmetic before source acquisition. isqrt is integer binary search with
schoolbook comparisons/products, not a real oracle. The program aborts and
returns zero BEFORE another source acquisition would exceed Qcap or a core
bit/gate step would exceed B. Reserve gcount before every count/factor
block; abort before a block if it does not fit, and pad completed blocks to
their paid cost. All setup, monitoring, padding and cleanup are charged.

Material context is Oded Regev, A Subexponential Time Algorithm for the
Dihedral Hidden Subgroup Problem with Polynomial Space, quant-ph/0406151v1,
Section3 (https://arxiv.org/pdf/quant-ph/0406151v1). Its multi-input subset
merging motivates this regime. PSR4 ranks all members of an accepted measured hash bucket and bounds
all sparsification, rejection and singleton losses uniformly for every list;
it proves a bounded accepted hash bucket and uses no fresh-uniform
higher-label assumption.
Kuperberg arXiv:1112.3333v1 Sections4.2-4.3 supply collimation/reindexing context.
No external algorithmic theorem or earlier verdict is a correctness premise.

PSR4 materially uses the source-only label/gradient/all-moduli/root-frequency
arguments reproduced through locally archived COL6-COL13 (no published endpoints; all needed material is reproduced). Published COL3 is20dcb56f-cf80-4e95-8784-b2c66b9f6577;
its carried raw-aggregate, unused-top-bit, recovery and cutoff arguments are
reproduced. Published RLQGR2,8657ff0f-f4d3-4605-a583-a6d57d3205f4, supplies the
consulted mixed-source eigenlabel argument. Published PG4,
e40f2d5a-68c9-418b-b4e8-64a80305968e, supplies consulted reusable-gradient
kickback and charging one initial trace error across adaptive reuse. The
ordinary mixed-eigenlabel preparation here differs from PG4's Fourier circuit;
its Nam/Su/Maslov1803.04933v2 SectionII attribution is retained. Helpers are
fully reproduced. No predecessor search or fast-arithmetic circuit, Fourier-source oracle,
purification access or free QRAM is used. The new private Grover counting
circuit is supplied explicitly, with no inverse source preparation.

This candidate carries the local PSR1/2/3 signed-object framework and
known-frequency decoder. The local MSR6/7 work supplies quantum-counted
hash/rank and the counted private phase window, reproduced in the helpers.
The new polynomial-space arity, caps and envelopes need their own review.
No previous verdict is a premise or rebound to these claims.

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

Use the complete hash-rank-tools.md instrument on this measured S. Its
predicate includes BOTH residue and weight keys. Private factor counting
selects a random binary hash width, the hash alone is measured on the source
index, and a second private factor estimate rejects large hash buckets.
Accepted exact-reference buckets have fewer than Kcap=2^40n^2L elements.
All approximate-count and factor/preparation errors are transferred by one
unconditional whole-computation hybrid, not excluded by conditioning.

The literal predicate computes sum_i a_i*z_i mod2^b and sum_i weight_i*z_i,
with known signed constants and reversible ripple arithmetic. It is also
expressible as m literal two-row queries with entries0 and a_i (and their
raw/weight entries). These rows need no exponential table; their entire
uniform generation is charged. Hash/parity and numerical comparisons are
explicit gates. quantum-count-tools.md and window-tools.md give every
private Grover reflection, known-index preparation, dyadic Fourier rotation,
integer count and bounded private-window preparation. No free oracle, source
inverse or QRAM is assumed.

Compute rank(x) by a bounded prefix count, then XOR its t-step binary-search
inverse g(rank) into the old x to erase that old product index. These are
complete XOR functions on all encodings; only their action on S is used for
erasure. Measure high rank bits and retain one low bit. Discard and regenerate
all m children if this is a final singleton. For a full pair, generate the
two selected original masks x,y by private inverse searches on their two
known ranks. Retain only those two m-bit masks. All these searches and their
reversals count, and no2^m classical candidate list or gate stream is stored.

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

Before hash sparsification, global singleton probability is at most
(m+1)2^b/2^m <=(m+1)2^(-v)<=1/(32n), uniformly for EVERY label list.
The hash helper adds less than1/(16n), so we use the weaker total failure
bound1/(8n). This is before conditioning on key/hash outcomes. A particular
rare class can be entirely singleton; no per-class success assumption is made.
The reference always preserves balanced amplitudes and signed aggregates.
Its cost/success bounds remain uniform after earlier secret-estimation errors.

For target w cancel exactly w-1 bits in D_w=ceil((w-1)/b0) levels, with a
possibly shorter final block. When w=1 there are no regular levels. Depth-first
recursion generates each group of m children, retaining at most m-1 sibling
phase qubits per level. A failed merge releases all children before retrying.
At most m^D_w accepted base controls occur in one surviving object. Every
failed generation, source filter, private count and measurement is charged.

## Known-frequency root without a uniform-label assumption

Generate an EXTRA m objects after the above complete w-1 cancellation.
Now F=Ftarget, and every rawLow_i is divisible by Ftarget: its difference
from F*a_i is an integer combination of original top bits times Ftarget.
Tensor the m qubits and measure the EXACT integer key

 (sum_i(rawLow_i/Ftarget)*x_i, sum_i weight_i*x_i).

Use precisely the hash/count/rank/unrank/pair instrument just proved,
with this exact key in place of the residue key. When D_w>=1 all child
weights are zero, and the first coordinate is an integer between-q and q.
There are at most2q+1 classes. When D_w=0, w=1, rawLow_i=0 and weights1;
there are only m+1<=2q+1 classes. Before hashing, paired mass is at least1-(2q+1)/2^m>=3/4.
The hash helper adds less than1/12 loss, so a pair succeeds with probability
at least2/3. All counts, hash failures and rejected buckets are charged.
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
The root retries only an unpaired outcome, with probability of a pair>=2/3.
frequency-tools.md estimates the phase using this joint W/qubit law.
For two-adic parity only, repeat until W is odd, which has conditional
probability1/2 for every T>=2. That branch succeeds per trial with probability
at least1/3. Arbitrary odd W is never substituted for literal one in odd moduli.

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

Prepare the single gradient described below before ANY counting or odd-part
work, including when a=0, then prepare the bounded-attempt global private
window. Its ideal gradient makes every dyadic counting rotation exact. Now write s=r+M*t, t in Z/2^a. At bit level ell=0,...,a-1 suppose t_low
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
before all counting may abort, but all acquired source copies still
count toward Q. Its ordinary preparation register is not part of source Q.

Actual source-label extraction uses planned count Qcap in label-tools.md.
Its whole-computation error<1/2048<1/1024 compares to true labels on the
UNCONDITIONAL exact ensemble. It remains uniform over adaptive CRT choices
and known estimates because every new source copy is independent and its
transformed Fourier label is uniform. Do not condition on correct labels
or absence of caps to claim uniform phases. Work/source caps enforce all
actual branch bounds even when labels/gradient/estimates are wrong.


## Counted reference expectations, literal guards and work

A CORE operation is a fixed-arity gate, measurement/reset, source acquisition,
classical Boolean bit operation or bit of circuit/address generation. Only
external monitor work is excluded from the core, and it is fully charged
below. No word, query, private preparation, sample or circuit controller is free.
The predicate has m known two-row contributions and signed sums, the measured
key, hash matrix and optional interval comparison. The deliberately loose
2^200n^12L core allowance expands every bit, gate, inverse and address.

The helpers supply actual physical count/factor circuits in
 gcount=2^1000n^30 2^(ceil(m/2)+2).
The bounded phase-window preparations and their discarded attempts are
included. A constant number of rank/inverse and pair-metadata operations
uses O(mL+1) blocks, L=2. Ordinary arithmetic, source-label helpers with
H<=2n, gradient128n, integer coefficient generation, resets and initial
window preparation fit
 G=2^10000n^100 2^(ceil(m/2)+3).
No2^m enumeration is executed. All Grover calls act on privately known
uniform index registers and expanded predicates, never a supplied source
inverse. Every failed tree or private attempt is counted.

A base object needs at most2 source acquisitions in expectation, including
the odd-part filter. With f0=8n/(8n-1), A0=mf0, regular-attempt success
is at least1-1/(8n) for every child list. Thus EQ_i<=A0 EQ_(i-1).
The extra root pair succeeds with probability at least2/3; parity succeeds
with probability at least1/3. Over at most C completed root calls,
 EQ<=Qstar=C32m A0^D.
Uniform core means are bounded by E0=G, E_i=f0(mE_(i-1)+G), hence
 E_D=G*((8nm+1)A0^D-8n)/(8n(m-1)+1)<=2G A0^D.
All known-frequency classical grid work is at most(n+5)2^150n^12q<=E_D,
since E_D>=Gm^D and q=m^(D+1). Include the initial gradient/window and
root retries in Wstar=G+C32(mE_D+G). These bounds use uniform conditional
means before attempts, not success-conditioned cost or independent tables.

The exact physical program aborts before acquiring more than Qcap=ceil1024Qstar
or executing more than B=ceil1024Wstar core steps. Each count/factor reserves
its full gcount cost BEFORE starting; completed blocks are padded to that
amount. Guards never interrupt a unitary. A failed reservation implies the
uncapped reference would exceed B. Markov gives each source/core cutoff loss
at most1/1024. Fixed word widths, clamped bad outputs and finite loop bounds
enforce every actual branch even when approximate estimates are incorrect.

Naive bit-serial binary counters and schoolbook guard/addition arithmetic use
O(n)-bit words. Every primitive classical/quantum access pays its full allocated-
memory address length, including the monitor's own index generation/access.
O(n^2) raw bit operations per guard/update, O(n) charged address and O(n)
generation slack give a loose O(n^4) FULLY CHARGED overhead per core step.
Block reservation may debit once and skip interior clock writes; all interior
gates/padding still pay their address costs. Direct source cost n+1 fits.
No gate stream or whole recursive computation history is stored. Initialization,
reset/deallocation and aborted-frame cleanup cost polynomial times peak storage
and are absorbed in the same caps/overhead.

## Uniform integer inequalities and precision

Let x=log2 n, Hscale=sqrt(nx) for analysis only, n>=2^20. Dyadic induction
gives ell<=n^(1/3)/2: for ell=j>=21, j<=2^((j-1)/3)/2 holds at21 and
persists, since(j+1)/j<2^(1/3); ell=20 is direct. Consequently
 m=ceil(sqrt(n ell))<=n^(2/3), log2m<=2x/3.
The dyadic bound n>=400log2n gives20x<=Hscale<=n/20. Also
ell<=21x/20 and sqrt(21/20)<=21/20 imply m<=9Hscale/8.
Since v=ceil(log2(m+1))+ell+5<=5ell/3+7<=2ell for ell>=21,
with ell=20 endpoint checked directly, v<=2(x+1)<=m/8. Therefore
 b0>=7m/8, D<=8n/(7m)+1<=n, mD<=8n/7+m<=2n.
Since m>=Hscale,
 log2q=(D+1)log2m<=(16/21)Hscale+(4/3)x.
Using Hscale>=20x and x>=20, this is at most m-4. Hence
 2^m>=16q>=4(2q+1),
which proves the old root pair bound without any internal-label distribution
assumption. Also log2q<=n, so all signed metadata fit O(n) bits.

Bernoulli with D<=n gives A0^D<=2m^D. The q bound makes log2(q+1)<n/4,
so hstat<=2n, C<=2^35n^2, Qstar<=64Cq. In particular
 Qcap<=2^80n^4 2^((16/21)Hscale).
The label precision H=ceil(log2(Qcap(n+5)+2))+20<=2n and
8Qcap2^(-128n)<1/1024 follow. With Kcap=2^41n^2, qpeBits<=2m<p=128n:
its upper bound m/2+2log2n+60 is below2m since m>=20x and x>=20.
Counting's small-angle cap bound follows from m>=Hscale and R=1<=Hscale/16,
exactly as proved in the helper. Its private rotations are exact on ideal Gamma.

The recurrence gives mE_D<=4Gq, Wstar<=1000CGq. Hence
 log2B<=10100+105x+m/2+(16/21)Hscale
 <=10100+105x+(3/2)Hscale<n/8.
Here10100+105x<=n/64 holds at2^20 and persists by dyadic induction, while
Hscale<=n/20. Thus the window's delta=2^(-100n), global preparation abort,
private factors and reused coherent count errors have total transfer<1/1024,
as proved in window-tools.md. All literal counter widths are O(n).

## Polynomial storage and unconditional full-secret success

Signed a/rawLow are bounded by q*2^n and weight by q, giving O(n)-bit
records. At most O(m(D+1))=O(n) objects/records are live, so the complete
classical frame stack uses O(n^2) bits. Even D hash matrices use at most
Dm^2<=2nm<=2n^2 bits. Private integer arithmetic, exact phase constants,
direction tables, CRT/Euclid, estimator records and streamed grid maxima
fit O(n^2). No source coefficient tree, q-record list,2^m solution table or
full emitted circuit accumulates. Thus S_C=O(n^2) jointly with the other bounds.

Sibling controls use O(m(D+1))=O(n) qubits. Private window, Grover-index,
phase arithmetic, source data and gradient128n each use O(n) qubits, with a
constant number live. Unranking history uses O(m(log n+1))=O(n): m<=9Hscale/8
and n^(-1/2)(log n)^(3/2) is bounded by elementary dyadic induction. Scratch
is reused across nested routines. No coherent median array, one-flag-per-row
array or window-test history lives in quantum storage. Therefore S_Q=O(n).
Every initialization, inverse and failed bounded attempt is charged.

Source-label replacement, initial gradient preparation/abort, known-phase
rounding, odd-part empirical estimation, source cutoff and core cutoff each
cost at most1/1024. The full window/factor/coherent-count hybrid adds at
most1/1024. These are unconditional channel/vector comparisons, with no IID
assertion conditioned on successful labels, caps or estimates. The reference
has exact two-adic outputs given correct earlier estimates. Hence the large
branch recovers the whole secret with probability>=1-7/1024>2/3. The fixed
exhaustive prefix succeeds>3/4. The clean law0 applies to this same program.

## Sharper asymptotic envelopes of this finite program

Use the ANALYTIC threshold n1=2^(2^20), never a runtime branch or advice.
For x>=2^20 the dyadic inequality log2x<=x/8192 implies
log2(4ell)<=3+log2x<=x/256, so ell<=n^(1/256)/4.
Then m<=2sqrt(n ell) gives log2m<=x/2+x/512<=129x/256.
Also m<=Hscale*(1+1/(2x))+1<=1025Hscale/1024.
For this range ell<=n^(1/8) by dyadic induction and m>=sqrt(n), so
v<=2ell<=m/256, giving b0>=255m/256, D<=256n/(255m)+1. Therefore
 log2q<=(129/255)Hscale+(129/128)x
 <=(129/255)Hscale+2x.
Since129/255<33/64, Qcap=O(n^4 2^((33/64)Hscale)).
Combining Wstar<=1000CGq and G's exact exponent yields
 B=O(n^104 2^((1025/2048+129/255)Hscale)).
The coefficient175189/174080 is strictly below33/32. With the fully charged
n^4 monitor/generation overhead, T=O(n^128 2^((33/32)Hscale)).
The finite range n<n1 is absorbed by an explicit additional outside factor
2^(100000n1) times the implementation constant. This huge absolute constant
is not a practical claim or an unknown coefficient hidden in the exponent.
Exact indices are1/2,0,0,1/2; all four envelopes and tolerance0 belong to the
SAME finite program. No positive-tolerance or maximum-impossibility claim follows.

## Material contribution route

The local PSR1/2/3 signed-object/pair framework and known-frequency decoder
are reproduced. Local MSR6/7 supplies the new hash/count/rank circuits and
linear-space private phase window, likewise reproduced, without a previous
verdict premise. Published COL3 supplies raw-aggregate/unused-top-bit/all-moduli
and cap accounting context, adapted here to signed disjoint coefficients.
RLQGR2 supplies mixed-source eigenlabels, PG4 supplies consulted reusable-
gradient kickback and one-initial-trace replacement, and CADGR1 supplied the
consulted ideal-prefix whole-computation vector hybrid for reused private
scratch. No CADGR1 threshold, robustness law or search schedule is used.
Standard quantum counting/window context is acknowledged in the helpers.
No supplied source inverse, purification, free QRAM, free classical search
or practical/optimal/cube-root result is asserted.
