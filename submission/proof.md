# QSR16: binary exact stream with a square-root time exponent

## Joint theorem, exact parameters and provenance

For every N>=2 and fixed s modulo N, n=ceil(log2 N), the SAME program
recovers the entire secret with unconditional probability>2/3 and has
these bounds on EVERY branch:

 T=O(n^(9983/1058)*2^((1041/368)sqrt(n))),
 S_C=O(n^(3/2)*2^((23/32)sqrt(n))) bits, S_Q=O(n) qubits,
 Q=O(n^(2082/529)*2^((32/23)sqrt(n))).

Resource representatives apply for n>=2, with n=1 fixed absolute
cost, storage and count. Outside constants are absolute. Growth indices are1/2,1/2,0,1/2.
The fifth law is0 under the canonical independent ideal-copy model.
No positive-corruption guarantee or maximum-tolerance impossibility is claimed.

This is a different Pareto configuration from the n^(1/4)-width stream
family: its time/source envelopes are faster asymptotically, while its
classical storage has square-root exponential growth. Quantum storage
stays linear. No joint dominance, practical crossover, tight cost,
optimality, fastest-known or cube-root claim is made.

For n<16777216 use the exact exhaustive baseline: n+2 fresh controlled-
subtraction/X tests per candidate t<N, returning the first all-plus candidate
or zero. True t passes certainly; each false candidate passes with probability
2^(-(n+2)), so success>3/4 by a union bound. Q<=N(n+2), T=O(2^n n^4),
and spaces O(n^2). The fixed finite prefix fits the displayed envelopes
with absolute constants, including n^2<=16777216n for quantum space.
A source/time outside constant as large as2^16777220 is allowed, explicitly
not a practical performance assertion. Remaining descriptions use n>=16777216.

Set ell=ceil(log2 n), R=isqrt((529*n-1)//1024)+1, L=2^R,
m=2, t=2R, v=ell+4, b0=R-v, D=ceil((n-1)/b0),
r=R+2ceil(log2(R+2))+8, q=r*2^(D+1).
The integer expression makes R exactly ceil((23/32)sqrt(n)); no real
runtime advice or irrational parameter is used. Roots and ceilings are
counted integer algorithms. Remaining descriptions use n>=2^24.
Set f0=16n/(16n-1), A0=m*f0,
Mgrid=2^20(q+1), hstat=ceil(log2(Mgrid+1))+ceil(log2(n+7))+20,
Kstat=2^32hstat, C=(n+5)Kstat+n,
Qstar=C*32r*m*A0^D, Qcap=ceil(1024Qstar),
p=n+ceil(log2(Qcap+2))+40.
Set G=2^100 n^4*2^t, E0=G, E_i=f0(mE_(i-1)+G),
Wstar=G+C*32*(mE_D+G), B=ceil(1024Wstar).
Compute these rationals/integers EXACTLY before source acquisition.
Abort and output zero before a source acquisition would exceed Qcap
or a core bit/gate step would exceed B. After abort or completion, a
separate terminal G-core-step allowance clears/releases live tables and
qubits without acquiring sources; its own clock is charged in the same
way. Total core work is at most B+G<=2B. Initialization and cleanup count.

The collimation/reindexing context is Kuperberg arXiv:1112.3333v1 Sections4.2,
4.3 and4.6. Regev quant-ph/0406151v1 Section3 supplies polynomial-space
multi-input subset-merging context. Their results/verdicts are not premises:
QSR16 supplies its complete rank instrument, probabilities and counted circuits.
It materially combines the locally archived COL13 constant-weight leaves
and PSR1 all-solutions stream enumeration (neither has a published endpoint; needed material is reproduced). No novelty is asserted for these standard tradeoffs or ranking.

Published COL3,20dcb56f-cf80-4e95-8784-b2c66b9f6577, supplies carried aggregate,
unused-top-bit, all-moduli and cutoff arguments, reproduced here. Published
RLQGR2,8657ff0f-f4d3-4605-a583-a6d57d3205f4, supplies mixed-source eigenlabels;
published PG4,e40f2d5a-68c9-418b-b4e8-64a80305968e, supplied consulted gradient
kickback and one-initial-trace-error reuse. Their necessary helper arguments
and earlier Kitaev / Nam-Su-Maslov1803.04933v2 SectionII context are retained.
The ordinary mixed-eigenlabel gradient preparation differs from PG4's Fourier
circuit. No predecessor fast multiplication, robust score or Grover search
is used. No source inverse, purification, hiding oracle or free QRAM is supplied.

This directly carries the published MSRL5 finite stream/tree/control program,
submission8fca011e-b320-4999-b898-be09e4130cf3 at candidate
db205d41db86bf1604f853ab8c08ee273978f237, whose source is reproduced.
Its mathematical ancestor MSR3 is5aafeb93-37d7-4b4c-bf75-44a2c84db4a8.
The root now keeps every known W for odd-part estimation and only waits for
odd W in two-adic parity. frequency-tools.md reproduces the local MSR4/MSR5
known-frequency estimator, without any predecessor verdict as a premise.
The source/work caps and precision are recomputed for this new instrument.
No private quantum counting, hashing, window, bucket dictionary or
approximately clean counter is used. Stream rank/unrank remains EXACT.

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



## Uniform phase vectors, aggregate metadata and literal table access

For a fixed target width w<=n put Ftarget=2^(w-1). A phase vector of length L is
L^(-1/2)sum_(j=0)^(L-1) exp(2pi i F b_j theta)|j>,
with a known integer table b and irrelevant common global phase. It occupies
R index qubits, NOT L qubits. Per entry store only THREE integer aggregates:
its phase label b_j, its raw low-part sum ellSum_j, and its Hamming weight h_j.
Each has O(n) bits, as bounded below. Incidence vectors are NOT stored.

In the proof only, each entry corresponds to a distinct binary string x of
choices among the original leaf controls a_i. Its invariants are

 sum_i a_i*x_i = F*b_j+c_global,
 ellSum_j=sum_i (a_i mod Ftarget)*x_i, h_j=sum_i x_i.

The common integer c_global is independent of the index j. These identities
explain the aggregates; the controller does not enumerate or retain those
q-bit conceptual strings or a tree of original labels. Only the local r-bit
leaf strings used in the next construction are temporarily enumerated.

### Counted constant-weight leaves

Acquire r independent uniform w-bit labels a_i and tensor their phase controls.
Compute popcount into ceil(log2(r+1)) clean bits, measure its value h and
uncompute/reset that register. The remaining controls are a uniform-amplitude
phase state over the binom(r,h) bitstrings of weight h. Its phases are still
exp(2pi i theta sum_i a_i x_i); measurement never inspects any label bit.

Within each leaf attempt generate a classical binomial table C(t,k), 0<=t,k<=r, by Pascal addition,
with zero for k<0 or k>t. Entries have at most r+1 bits. To rank a weight-h
string in lexicographic order (zero before one), initialize z=0, rem=h.
For i=0,...,r-1, if x_i=1 add C(r-i-1,rem) to z and decrement rem.
To unrank z<binom(r,h), initialize rem=h; at position i set x_i=1 iff
z>=C(r-i-1,rem), and then subtract that coefficient and decrement rem.
The lexicographic partition into zero-prefix strings followed by one-prefix
strings proves by induction that these functions are inverses on this domain.

These are counted circuits, not oracles. A rem-dependent coefficient is
computed into r+1 scratch bits by scanning all r+1 possibilities for rem,
using equality controls and known constant XORs, then uncomputed. All adds,
comparisons and rem updates are exact ripple circuits. Ranking preserves x,
uses a rank accumulator and rem, copies its result, then reverses all r steps.
Unranking retains its comparison decisions as the r output bits; after
copying them, reverse each controlled subtraction/decrement and then erase
its decision by recomputing the comparison. Scratch is O(r) bits, independent
of the gate count. The coefficient table is CLASSICAL O(r^3) bits; quantum
lookups are literal scans. All loops, constants, wire addresses and gates
are counted. Each function has polynomial-in-r gates and bit generation.

Extend rank to zero on weight!=h and unrank to zero on z>=binom(r,h).
Validity flags are computed and erased; guarded arithmetic gives complete
Boolean functions, hence their clean XOR evaluations are unitaries on ALL
encodings. Compute rank into an r-bit register (binom(r,h)<=2^r), erase
the old x by XORing unrank(rank(x)), and reverse its temporary calculation.
Old x is zero on this measured subspace. The surviving rank state is uniform
on [0,binom(r,h)), with its original phases and no forgotten x information.

Measure the high r-R rank bits and keep only a full L-element chunk. A partial
chunk discards the entire leaf and reacquires r new labels. Globally BEFORE
conditioning on h the partial mass is
 sum_h (binom(r,h) mod L)/2^r <=(r+1)(L-1)/2^r<=1/16.
Indeed k=ceil(log2(R+2)), r=R+2k+8; k<=R+1 implies
r+1<=3R+11<=16(R+2)^2<=2^(2k+4), so16(r+1)<=2^(r-R).
The first inequality is adequate here since R>=32. A rare individual h
may be entirely partial; no conditional-per-h retention bound is asserted.

For each retained z in its known full chunk, unrank it CLASSICALLY and compute
b_z=sum_i a_i*x_i, ellSum_z=sum_i(a_i mod Ftarget)*x_i, h_z=h.
Only L rows are enumerated, with one reusable r-bit local string. Set F=1,
c_global=0 and release the r labels and binomial work when no longer needed.
All entries of this leaf have the SAME weight h. Combining two child tables
adds their weights, so all entries in each surviving tree have one common
weight, even though independently regenerated trees may have different ones.
The r source controls, rank, and arithmetic use O(r) quantum scratch; since
r=O(sqrt n), this fits the O(n) allocation with the rest of the recursion.


## Multiway product ranking and a single-pass output table

Take m same-level vectors of length L with common F. Write their label tables
as B_i[j], raw-low tables as U_i[j], and common weights as h_i. Their product
has t=mR quantum index bits and2^t equal-magnitude amplitudes. Coherently
compute sum_i B_i[x_i] mod2^b, b<=b0, with m literal L-row XOR lookup
networks and ripple additions. Each query compares its R-bit index with
each classical row, XORs the known value under equality, then erases the
equality scratch. Add to the residue and reverse the query before proceeding.
O(n) scratch is reused, not one quantum flag per row. All rows/gates/addresses
are generated and charged; this is NOT quantum-addressed RAM.

Measure the low-sum value y and reset its register using the known bits.
On the measured set S of product indices x, all magnitudes remain uniform.
Enumerate every CLASSICAL z in[0,2^t) using a t-bit counter, split it into
its m known R-bit components, read the child tables classically and compute
its residue. Count M=|S| in t+1 bits (M can equal2^t). Store no list of S.

The complete rank(x) is the number of valid z<x if x belongs to S, and zero
otherwise. Coherently compute validity with the same m lookup networks,
erase their data scratch, and retain one validity bit. Enumerate all z:
when its known residue is y, compare z to quantum x and conditionally
increment a t-bit rank accumulator. Copy under validity, reverse the entire
enumeration, and erase validity. The accumulator is at most2^t-1, since
at most that many strings are strictly below any x. Ripple increments and
comparisons have O(n) reusable quantum scratch. Reverse enumeration regenerates
classical decisions; no exponential history or gate stream is stored.

The complete inverse XOR function g(rank) enumerates valid classical z with
a t+1-bit classical count c; under equality of zero-extended quantum rank
with c, XOR that known product mask z into its target and erase equality
scratch. There is at most one match. Rank>=M has no match and returns zero.
Each function is a complete Boolean XOR unitary on ALL encodings. On the
measured S they are inverse because both enumerate the same numerical order.
Compute rank into a fresh t-bit register and XOR g(rank) into old x, erasing
old x on this measured support. No which-index information is discarded.

Measure the high t-R rank bits and retain low R. A partial last L-chunk
discards ALL m children and regenerates them. Globally BEFORE conditioning
on y the partial probability is
 sum_y(M_y modL)/2^t <=2^b(L-1)/2^t <=2^(-v)<=1/(16n).
This is uniform for every input table list; small individual buckets may
be entirely partial. No independent/uniform-current-label assumption is used.

For an accepted chunk, build its L output records by ONE MORE enumeration
of all valid classical product masks z, keeping their running rank c. When
c lies in the selected interval[chunk*L,(chunk+1)*L), compute and write row
c-chunk*L. The new record is
 B_new=(sum_i B_i[z_i]-y)/2^b,
 U_new=sum_i U_i[z_i], h_new=sum_i h_i.
Set F_new=F*2^b. Every quotient is exact. The invariant common offset becomes
c_global_new=sum_i c_global_i+F*y, independent of the retained rank. The
conceptual original incidence is the concatenation of child incidences,
still binary and distinct for every output row. All weights are common
throughout this vector. The per-row raw-low sum is computed only from lower
labels. Old tables/scratch are reset/released with counted work.

Crucially this is one2^t pass with L writes, NOT L separate inverse searches.
The coherent rank, inverse erasure, M counting and output construction use
a fixed number of2^t enumerations plus m literal L-row queries, each with
polynomial per-mask/row work. Only the child/output tables are exponential
in R; no2^t classical table is allocated.

For target w<=n apply D_w=ceil((w-1)/b0) regular levels, cancelling exactly
w-1 bits with a possibly shorter final remainder. When w=1 there are none.
Depth-first traversal retains at most m-1 R-qubit siblings per level.
A surviving vector uses exactly r*m^D_w original accepted base controls,
not counting discarded source copies. These original labels/incidences are
analysis objects, not an allocated global array. All failures regenerate
the whole affected group and are charged.

## An extra product root and a known random frequency

After the above full w-1 cancellation, generate an EXTRA m vectors with
F=Ftarget. Use their t-bit product index. A single vector's L entries may
be too few for final matching; the extra product is essential.

For each child, U_i[j] has a common residue modulo Ftarget: the incidence
invariant gives U_i[j]=Ftarget*b_j+c_global_i-Ftarget*(top-bit sum).
Thus the root key
 K(x)=sum_i floor(U_i[x_i]/Ftarget)
has equal value for two products exactly when their total raw-low sums
are equal. The omitted child residues are fixed across all its entries.
The key is nonnegative and at most q, so has at most q+1 values.
All product incidences also have common weight sum_i h_i.

Compute and measure K with the same literal L-row lookup/add networks;
reset its known bits. Apply the complete stream rank/unrank construction
on[0,2^t), now retaining full PAIRS (one low rank bit) rather than L-chunks.
A root singleton is discarded with all m children. The global paired mass
is at least1-(q+1)/2^t>=3/4 by the parameter proof below. Find the two
chosen product tuples by one classical enumeration, retaining only their
two t-bit masks. No global incidence vector is needed.

In the analysis write each original accepted w-bit label as
a_j=ell_j+Ftarget*T_j with ell_j<Ftarget and independent fair bits T_j.
Leaf Hamming weights/ranks and all regular/root decisions use only these
original lower labels and computational indices. At cumulative F, a top-bit
contribution is a multiple of Ftarget/F, so it cannot affect any prescribed
residue before total cancellation reaches w-1. Root raw-low keys also omit
the top bits. All computational partition probabilities depend only on set
sizes, since magnitudes are uniform. Therefore unused T_j are still
independent fair bits conditional on those LOWER choices, not on the full
stored high-label transcript. A missed root starts over with fresh sources.

Distinct selected product tuples have distinct original binary incidences
x,y. Their difference c=y-x is nonzero with entries{-1,0,1}, has raw-low
sum0 and total weight0. If d is its number of nonzeros, d is even,2<=d<=q,
with d/2 of each sign. Their full frequency difference divided by Ftarget is
 W=sum_j T_j*c_j ~ Bin(d,1/2)-d/2.
This also equals sum_i(B_i[y_i]-B_i[x_i]), because child common offsets cancel.

The characteristic function is E exp(2pi i W delta)=cos(pi delta)^d.
ONLY AFTER measuring the pair identifier inspect the full known labels and
compute W. In odd-part mode keep EVERY W, including zero and nonunits,
returning its exact qubit q_1(W*Ftarget*theta) with known W. Conditional on W,
forgetting other metadata causes no dephasing: every such qubit has this
same relative phase. Root pair acceptance is at least3/4, with retries
only for unpaired outcomes. frequency-tools.md uses these known frequencies,
not a substitution of arbitrary W for literal frequency one.

In two-adic parity mode only, discard even W and retry the whole root.
For each nonzero even support d, W is odd with probability1/2. Total
acceptance is at least3/8, hence at least1/3. Do not apply the old sign flip:
any odd W, including negative W, gives the same phase(-1)^bit for parity.
No literal-W=+/-1 rejection remains in this program.

## All-moduli source supply and full-secret recovery

Compute N=2^a M with M odd by trailing zeros; do not factor M.
If M>1, put d=floor(log2N), F=2^(d-1), f=F/2^a, a unit modulo M.
For j=0,...,n+4 choose a CRT unit alpha_j congruent to2^j mod M and1
mod2^a (use2^j mod N if a=0). This is counted Euclid/CRT arithmetic.
Transform each NEW source's data by alpha_j, extract its uniform N-label k,
and retain only k<2^d. Success is at least1/2 and retained labels are IID
uniform d-bit integers. Charge every rejected source. After X its control
is q_k(alpha_j*s/N). Run the root in odd-part mode with w=d.
Its result is q_1(W*2^j*vartheta), with W known and
vartheta=f*(s mod M)/M modulo1.

For each j collect Kstat such root outputs, choose a fresh fair X/Y basis
for each measurement, record (W,basis,outcome) classically and release the
qubit. frequency-tools.md proves a uniform population gap on the finite
Mgrid grid, Hoeffding concentration with this ACTUAL hstat, rational
half-angle unwrapping and final rounding. With failure<1/1024 simultaneously
over all n+5 stages it recovers f*(s mod M), then its inverse yields
r_secret=s mod M. All trigonometry is counted finite classical rational
work. At M=1 set r_secret=0 and skip this odd-part procedure.

If a>0 prepare the one counted gradient below before the two-adic loop;
otherwise it is omitted. Write s=r_secret+M*t_secret, t_secret modulo2^a.
At level ell=0,...,a-1, given its correct previous low bits t_low, put
s0=r_secret+M*t_low. A new untransformed source has phase q_k(s/N).
The gradient subtracts the known k*s0/N phase. The ideal phase is
q_(k mod2^w)(t'/2^w), w=a-ell, t'=(t_secret-t_low)/2^ell.
The reduced labels are independent uniform w-bit integers because2^w
divides N. Run the root in parity mode. Its phase is(-1)^(W*t');
odd W makes the X outcome the next bit EXACTLY in the ideal reference.
Repeat and output r_secret+M*t_secret, the entire secret.

At most C=(n+5)Kstat+n completed generator calls occur. Correct odd-part
estimation and earlier parity bits imply correctness by induction.
If earlier estimates are wrong the qubits are still balanced and source
labels uniform, so all cost/retry bounds remain valid. Correctness is not
a premise in the source/work cutoff expectations.

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



## Counted work, reference expectations and literal hard cutoffs

A leaf requires at most4r source acquisitions in expectation, including all
filters and partial weight-chunk retries. For regular levels, every group
of m fresh children succeeds with probability at least1-1/(16n) for every
input table list. Hence EQ_0<=4r and EQ_i<=A0*EQ_(i-1), A0=m*f0.
The extra product root costs m such children per trial and accepts with
probability at least1/3. Over at most C calls its expected source
count is at most Qstar=C*32r*m*A0^D. Markov gives source-cap abort
probability<=1/1024 in the uncapped exact reference. The actual guard stops
BEFORE exceeding Qcap, on every branch.

A CORE step is a fixed-size classical Boolean bit read/write/operation,
head move, circuit gate, measurement/reset, source acquisition or bit of
circuit/address generation, excluding only the monitor's own work.
No word, table query, whole enumeration pass or controller is free.
Use fixed bit-serial control with explicit loop masks and sequential pointers.
Signed/integer words have O(n) bits. A per-product-mask allowance2^40n^4
core operations covers m ordinary child-table reads, subset sums, rank
comparison/increment generation and output record computation, including
schoolbook address work. A fixed number of2^t enumerations covers M,
rank and reverse, g inverse, and output-table construction.

Coherent validity needs m literal L-row queries, not2^t queries per mask:
compute it once, retain one validity bit and erase data scratch; after rank
copy/reverse, compute it again to erase that bit. Their complete bit/gate
generation costs mL*poly(n)<=2^t*poly(n). Equality flags, ripple carries
and coefficient values are reset after use; no per-row quantum flag or
generated gate history accumulates. Full L output metadata are written
in a single enumeration, with no additional L factor in time.

Leaf Pascal/rank work is polynomial, its L output enumeration has polynomial
per row, and L<=2^t. Source eigenlabel/correction helpers, ordinary gradient
preparation with at most n+20 attempts, Euclid, basic direction decoding and all inverse
work and all leaf/table initialization/clearing fit2^80n^8L since
p,Hlabel<=2n and R>=96log2n as proved below. Leaf source/weight retries
leave an absolute geometric factor; G=2^100n^4*2^t covers leaf expected
work, bounded initial gradient and every internal/root nonrecursive step.
All initialization, table clearing, failed attempts and source controls
are included. Exact fixed Boolean gates have constant-size Clifford+T
decompositions; there are no arbitrary real rotations or uncharged oracles.

Uniform conditional expectations justify E0=G, E_i=f0(mE_(i-1)+G).
The exact recurrence is
 E_D=G*((16nm+1)A0^D-16n)/(16n(m-1)+1)<=2G A0^D.
The whole classical grid/unwrapping work is at most E_D, as shown below.
Including initial gradient and all root trials is safely bounded by
Wstar=G+C32(mE_D+G).
The B-step clock then has abort probability<=1/1024 by Markov in the
uncapped reference. Fresh trial costs may correlate with success; the
bound needs only uniform conditional mean and success bounds before each
new trial, not independent full tables or a favorable success-conditioned cost.

Costs remain uniform after earlier estimation errors. All supplied qubits
are balanced in magnitude, and leaf/chunk/rank operations select and permute
computational amplitudes without phase-dependent interference. Even if
assigned labels no longer match the intended phase semantics, every vector
still has uniform magnitudes; initial target labels remain uniform and the
metadata W test has the same unused-top-bit law. Thus correctness of earlier
estimates is not a condition in the cutoff expectations. Wrong labels and
the actual approximate gradient are handled by unconditional finite-channel
comparison, while the syntactic caps bound every actual branch.

controller-tools.md details the per-mask n^4 bound, helper absorption
using2^t/L>=n^96, and full O(n^2) monitor/address/source cost. No
private counter/dictionary or source-control approximation is introduced.

## Uniform binary parameters and full square-root envelopes

Write x=log2n, z=sqrt(n), c=23/32 for ANALYSIS only, x>=24.
Then cz<=R<=cz+1, v<=x+5, r<=3R<4z, r>=cz.
The ratios z/x and z/(x+5) increase for x>=24. Their endpoint values
give v/R<=1/64, R>=96x, 2r<=n and 2R<=n/2.
Thus b0>=63R/64>0, D<=n, and
 tD<=2R*(n/(R-v)+1)<=128n/63+2R<=3n.
The depth-first quantum index stack therefore remains O(n), including
its changed constant; no earlier tD<=2n bound is used.

All ceilings in q are bounded as follows. Put alpha=2577/1058.
 log2q=log2r+D+1<=log2r+n/(R-v)+2.
Using n/R^2<=1024/529 and v/R<=1/64,
 n*v/(R*(R-v))<2v, since65536/(529*63)<2.
With log2r<=x/2+2 and n/R<=(32/23)z this first gives the convenient
coarse bound log2q<=(32/23)z+(5/2)x+14 for support/width checks.
For the FINAL envelope retain the second-order denominator identity
 n/(R-v)=n/R+n*v/R^2+n*v^2/(R^2*(R-v)).
Its last term is at most(1024/529)*(64/63)*(32/23)*(x+5)^2/z<1:
(x+5)^2/2^(x/2) decreases after24, and at24 the upper bound is
430592/766521<1. Also r<=cz+x+13<=z, since(1-c)z>=x+13 already
at24 and z/x increases; hence log2r<=x/2. Therefore
 log2q<=(32/23)z+(1024/529+1/2)x+5120/529+3
       <=(32/23)z+alpha*x+13,
 q<=2^13*n^alpha*2^((32/23)z).
Every ceiling, including r and the final tree depth, is included. The
coarse bound above remains useful and valid for the following checks.
The product-root support is adequate despite this large tree:
 t-log2q>=(17/368)z-(5/2)x-14>=4.
The last inequality follows at x=24 and persists because z/x increases;
using z/x>=4096/24 gives an explicit linear lower bound in x.
Consequently2^t>=4(q+1), and all earlier root pairing/odd-W bounds apply.
This support check is essential; choosing a width below z/sqrt2 would
not support that argument. Every inequality holds for ALL integer n>=2^24.

The same bounds imply log2q<=2z<n-1, so every raw/weight/frequency record
has O(n) bits. Also hstat<=log2q+x+50<=2z: the excess over(32/23)z
is at most(7/2)x+64, which is smaller than(14/23)z already at24 and
remains so as z/x grows. Thus C<=2^36n*z. Since D<=n,
f0^D<2, A0^D<=2m^D and Qcap<=2^17Cq. In particular
 log2Qcap<=(32/23)z+4x+67<n-42,
and p=n+ceil(log2(Qcap+2))+40<=2n. The last strict inequality follows
at24 and persists as n dominates z and x; for example the stronger
2z+5x+120<=n follows there and is increasing in slack.
Source-label precision Hlabel and controller fields are O(n) bits,
while log2B and log2Qcap are O(z), with log2B>=t>=2cz.
These are syntactic width bounds independent of successful outcomes.

## Whole classical-estimator cost and simultaneous resources

The finite-grid helper bounds all n+5 stages by
(n+5)2^150n^12q core steps. Since E_D>=Gm^D and q=r*m^(D+1),
their ratio to E_D is at most2^154n^13*r*m/G.
Here r*m=2r<=n and G=2^100n^4*2^t, so this is at most
2^54n^10*2^(-t)<1, using t=2R>=192x. Thus the FULL grid evaluation,
record work, exact trigonometry and unwrapping fit E_D, not a free step.
All node, gradient, estimator and root work is included in Wstar.

The expectation recurrence and A0^D<=2m^D give Wstar<=1000CGq/r.
Since C=O(n^(3/2)), G=2^100n^4*2^(2R), r>=cz and
q<=2^13n^alpha*2^((32/23)z), the complete work guard has
 B=O(n^(7867/1058)*2^((1041/368)z)),
 Q=O(n^(2082/529)*2^((32/23)z)).
Here alpha+5=7867/1058, alpha+3/2=2082/529 and
alpha+7=9983/1058. Also2R<=(23/16)z+2, and23/16+32/23=1041/368 EXACTLY.
No coefficient is hidden inside an exponential O. The fully addressed
monitor/source cost per raw core event is O(n^2), as constructed in
controller-tools.md. This proves the stated time n^(9983/1058) envelope,
including separate terminal G cleanup and all initialized bit/qubit access.
The public O(n^16) exact parameter computation fits the same envelope,
since2^t>=n^192; polynomial-times-L clearing fits G as proved there.

The depth-first stack holds O(m(D+1))=O(n/R)=O(sqrt(n)) tables with
L O(n)-bit records, so S_C=O(n^(3/2)*2^((23/32)z)). The R ceiling
contributes only an outside factor2. Statistical records use O(n*z)
bits and ordinary arithmetic/control buffers O(n^2); both fit this SAME
classical envelope, since L>=sqrt(n). The grid is streamed, with no
q-sized score array. Quantum sibling indices use O(tD+t)=O(n), now with
tD<=3n, plus O(n) rank/sum/source/gradient scratch and a constant number
live. No incidence tree, emitted history, QRAM, private count/window,
coherent median or exponential quantum table is allocated.

The four source-label/gradient/phase-rounding/statistical allowances and
two Markov cutoffs total at most6/1024. Every comparison is unconditional
and all reference costs include retries; no source IID is conditioned on
correct labels, estimates or surviving caps. Correct parity follows after
correct odd-part recovery. Thus full-secret success>=1-6/1024>2/3, jointly
with all four every-branch resource bounds. Syntactic caps bound erroneous
actual outcomes too. The n<2^24 finite baseline has success>3/4 and its
explicit outside constants, with n=1 fixed separately.

## Exact scope and provenance of this Pareto point

The logical exact stream/tree/known-frequency construction is carried
from local QSR12/13/14 and the authenticated published MSRL5 stream source.
The new FIXED m=2, R=ceil((23/32)sqrt(n)) schedule, n<2^24 exhaustive
prefix, recomputed actual source/work guards and all simultaneous bounds
are proved here independently. The slower broad n^4 bit-serial generator
is used, not QSR15's newer streaming compiler. Published QSR11 supplies
only the reproduced known-frequency estimator helper in this configuration;
its private counting/dictionary and shifted-width schedule are absent.

Relative to the quarter-width known-frequency stream family, both time
and source ratios diverge in favor of this program, since their positive
sqrt(n log n) exponent dominates every fixed multiple of sqrt(n).
Its classical peak is larger, with growth index1/2 instead of1/4, and its
quantum space is still O(n). This is a Pareto tradeoff, not joint dominance.
All four indices are derived from these exact supported envelopes:
1/2,1/2,0,1/2 respectively. The clean law and canonical model agree.
No prior verdict, remote analytic-only threshold, practical crossover,
fastest-known, optimality or cube-root claim is made. The explicit finite
prefix and its potentially2^16777220 outside constant are fully disclosed.
