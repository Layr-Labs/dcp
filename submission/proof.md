# MSRL4: sharper literal-root stream envelopes

## Joint theorem, exact parameters and provenance

For every N>=2 and fixed s modulo N, n=ceil(log2 N), the SAME program
recovers the entire secret with unconditional probability>2/3 and has
these bounds on EVERY branch:

 T=O(n^(37/4)(log2 n)2^((89/64)sqrt(n)*sqrt(log2 n))),
 S_C=O(n^(7/4)2^(n^(1/4))) bits, S_Q=O(n) qubits,
 Q=O(n^(5/2)(log2 n)2^((49/128)sqrt(n)*sqrt(log2 n))).

Resource representatives apply for n>=2, with n=1 fixed absolute
cost, storage and count. Outside constants are absolute. Growth indices are1/2,1/4,0,1/2.
The fifth law is0 under the canonical independent ideal-copy model.
No positive-corruption guarantee or maximum-tolerance impossibility is claimed.

This is a time/source/classical-memory tradeoff. Compared with polynomial-space
recomputation it uses larger classical tables to improve time/source envelopes.
Compared with the sqrt(n)-exponent table construction it has smaller classical
growth index but slower sqrt(n log n) time/source growth. No tight-cost,
practical, optimality, fastest-known or cube-root claim is made.

For n<1048576 use the exact exhaustive baseline: n+2 fresh controlled-
subtraction/X tests per candidate t<N, returning the first all-plus candidate
or zero. True t passes certainly; each false candidate passes with probability
2^(-(n+2)), so success>3/4 by a union bound. Q<=N(n+2), T=O(2^n n^4),
and spaces O(n^2). The fixed finite prefix fits the displayed envelopes
with absolute constants, including n^2<=1048576n for quantum space.
A source/time outside constant as large as2^1048580 is allowed, explicitly
not a practical performance assertion. Remaining descriptions use n>=1048576.

Set ell=ceil(log2 n), R=isqrt(isqrt(n-1))+1, L=2^R,
T0=isqrt(n*ell-1)+1, m=ceil(T0/R), t=mR,
v=ell+4, b0=t-R-v, D=ceil((n-1)/b0),
r=R+2ceil(log2(R+2))+8, q=r*m^(D+1), Sroot=isqrt(q-1)+1.
All roots and ceilings are INTEGER algorithms with counted schoolbook work.
R is exactly ceil(n^(1/4)); no real advice or irrational parameter is used.
Set f0=16n/(16n-1), A0=m*f0,
m_est=2^24(20+ceil(log2(n+7))), C=2(n+5)m_est+n,
Qstar=C*32r*m*Sroot*A0^D, Qcap=ceil(1024Qstar),
p=n+ceil(log2(Qcap+2))+40.
Set G=2^100 n^5*2^t, E0=G, E_i=f0(mE_(i-1)+G),
Wstar=G+C*8Sroot*(mE_D+G), B=ceil(1024Wstar).
Compute these rationals/integers EXACTLY before source acquisition.
Abort and output zero before a source acquisition would exceed Qcap
or a core bit/gate step would exceed B. Monitoring and cleanup are charged.

The collimation/reindexing context is Kuperberg arXiv:1112.3333v1 Sections4.2,
4.3 and4.6. Regev quant-ph/0406151v1 Section3 supplies polynomial-space
multi-input subset-merging context. Their results/verdicts are not premises:
MSRL4 supplies its complete rank instrument, probabilities and counted circuits.
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

This candidate materially carries the locally archived MSR1 (no ID
while uploads are paused). Its source configuration, circuit semantics and
storage are unchanged; controller-tools.md supplies the tighter per-mask
bit implementation and fully charged monitor. G decreases from n^8 to n^5
with the same absolute coefficient. The source cap/precision remain fixed;
only the literal work cap decreases. No old verdict is a proof premise.

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

## An extra product root and an exact literal frequency

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

For B0~Bin(d,1/2), Markov on its squared centered deviation gives at least
3/4 mass in the strict central window of radius sqrt d. At most3sqrt d
integers are in that window. The central binomial mode is largest by the
adjacent coefficient ratio, hence has probability at least1/(4sqrt d).
The adjacent-mode ratio d/(d+2)>=1/2 implies that its two neighbors together
have at least that probability. Thus Pr(W=+1 or-1)>=1/(4sqrt q).

ONLY AFTER measuring the pair identifier inspect the full known labels and
compute W. Keep when W=+1, apply X when W=-1, otherwise discard the entire
root and regenerate all children. Root acceptance is at least
3/(16sqrt q)>=1/(8Sroot). Every accepted history gives precisely
q_1(Ftarget*theta), up to a common scalar, for arbitrary real theta.
Forgetting classical metadata therefore introduces no dephasing. Odd W
is not treated as literal one for odd-modulus phase recovery.

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
The generator(w=d) gives q_F(alpha_j*s/N), whose phase is
2pi*2^j*(f*(s mod M)/M) modulo2pi. No unavailable source power is used:
alpha_j is a counted ordinary data permutation on each newly acquired copy.

For every j collect m_est such generated qubits measured immediately in
EACH X and Y basis, accumulating classical means and discarding each qubit
before the next. Apply the label-tools64-direction decoder and its identical
half-angle unwrapping with J=n+4 to estimate
vartheta=f*(s mod M)/M modulo1. For this ONE unknown phase the tail bound is uniform in its value.
Union is only over2(n+5) empirical means, giving failure at most
4(n+5)exp(-8(20+ceil(log2(n+7))))<1/1024. No union over N possible secrets
is needed. The direction decoder and unwrapping are unchanged. Error after unwrapping
<2^(-n-8)<1/(2M), so round M times the rational to recover f*(s mod M)
mod M, then invert f classically to obtain r=s mod M. At M=1 set r=0 and
skip this entire odd-part step.

If a>0 prepare the single gradient described below before the two-adic
loop; if a=0 omit that preparation. Now write s=r+M*t, t in Z/2^a. At bit level ell=0,...,a-1 suppose t_low
contains its known ell low bits and set s0=r+M*t_low. A fresh untransformed
source, after label extraction and X, has phase q_k(s/N). Use the counted
gradient correction of gradient-tools.md to subtract known phase k*s0/N.
The reference phase is q_(k mod2^w)(t'/2^w), w=a-ell, t'=(t-t_low)/2^ell.
The reduced labels are independent uniform w-bit integers because2^w divides N.
No label filter is needed here. The generator(w) returns q_(2^(w-1)), now
with relative phase(-1)^t'. An X measurement gives the next bit EXACTLY in
the reference computation. Repeat and output r+M*t, the full representative s.
At most C=2(n+5)m_est+n generator calls occur. On good odd-part estimation,
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



## Counted work, reference expectations and literal hard cutoffs

A leaf requires at most4r source acquisitions in expectation, including all
filters and partial weight-chunk retries. For regular levels, every group
of m fresh children succeeds with probability at least1-1/(16n) for every
input table list. Hence EQ_0<=4r and EQ_i<=A0*EQ_(i-1), A0=m*f0.
The extra product root costs m such children per trial and accepts with
probability at least1/(8Sroot). Over at most C calls its expected source
count is at most Qstar=C*32r*m*Sroot*A0^D. Markov gives source-cap abort
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
preparation with at most n+20 attempts, Euclid, decoder means and all inverse
work fit2^80n^8 since p,H<=2n as proved below. Leaf source/weight retries
leave an absolute geometric factor; G=2^100n^5*2^t covers leaf expected
work, bounded initial gradient and every internal/root nonrecursive step.
All initialization, table clearing, failed attempts and source controls
are included. Exact fixed Boolean gates have constant-size Clifford+T
decompositions; there are no arbitrary real rotations or uncharged oracles.

Uniform conditional expectations justify E0=G, E_i=f0(mE_(i-1)+G).
The exact recurrence is
 E_D=G*((16nm+1)A0^D-16n)/(16n(m-1)+1)<=2G A0^D.
Including initial gradient and all root trials gives Wstar=G+C8Sroot(mE_D+G).
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

controller-tools.md details the per-mask n^4 bound and helper absorption:
2^s>=n^16, so the unchanged2^80n^8 helpers and a fixed number of
2^s*n^4 mask operations fit G=2^100n^5*2^s with leaf retry slack.
The full monitor/addressing overhead is n^2, proved with each monitor
bit access charged. These are implementation bounds, not free word costs.

## Explicit parameter inequalities and simultaneous resources

Write Hscale=sqrt(n)*sqrt(log2 n) for ANALYSIS only. Runtime parameters are
the stated integers/rationals. All following inequalities hold for every
n>=1048576, not only the finite diagnostic inputs.

First ell<=(3/4)n^(1/4). For ell=j>=21, (4j/3)^4<=2^(j-1) holds at
j=21 and is preserved by induction, since((j+1)/j)^4<2; n>=2^(j-1).
The only remaining ell=20 case in this domain is n=1048576 and is direct.
Hence m<=sqrt(n*ell)/R+2<=sqrt(3/4)n^(3/8)+2
<=7n^(3/8)/8+2<=n^(3/8).
For R>=32, ceil(log2(R+2))<=R/2 by the elementary dyadic bound
j+2<=2^(j-1) when2^j<=R<2^(j+1), j>=5. Thus r<=3R<=6n^(1/4).

For n in this domain n>=400log2 n, by checking n=1048576 and then
2^(j-1)>=400j for j>=21 with induction. Therefore
20log2 n<=Hscale<=n/20. Also R<=2n^(1/4)<=Hscale/16, since
32<=n^(1/4)sqrt(log2 n). And v<=log2 n+5<=5log2 n/4<=Hscale/16.
Consequently R+v<=t/8, b0>=7t/8>=1, D<=8n/(7t)+1 and D<=n.

We have t<T0+R<=sqrt(n*ell)+1+R<=9Hscale/8:
ell<=21log2 n/20, sqrt(21/20)<=21/20, R<=Hscale/16 and1<=Hscale/80.
Thus tD<=8n/7+t<=2n. Since log2 m<=3log2 n/8,
 q=r*m^(D+1)<=6n*2^((3/7)Hscale).
Indeed the m term contributes(3/7)Hscale+(3/4)log2 n and r contributes
at most(1/4)log2 n+log2 6. This proves2^t>=4(q+1), since t>=Hscale
and Hscale>=20log2 n. Hence the root paired mass is uniformly at least3/4.
These also imply log2 q<=n, so all label/raw/common-offset metadata fit O(n) bits.

Bernoulli and D<=n give(1-1/(16n))^D>=15/16, hence A0^D<=2m^D.
The unchanged pointwise mean plan has C<=2^33n log2 n. The exact source/work
formulas and Sroot<=2sqrt q now give
 Qcap<=2^72 n^(5/2)(log2 n)*2^((9/14)Hscale),
 B<=2^220 n^(29/4)(log2 n)*2^((99/56)Hscale).
One may use Qstar<=128Cq^(3/2), Wstar<=100GCq^(3/2)/r;
q^(3/2)<=6^(3/2)n^(3/2)2^((9/14)Hscale), and99/56=9/8+9/14.
For the work bound, mE_D<=4Gq/r and q/r>=1 give
Wstar<=100GCq^(3/2)/r; r>=R>=n^(1/4) supplies the extra outside
factor n^(-1/4). The displayed fixed coefficients cover constants and ceilings.
It follows that H<=128+6log2 n+2Hscale<=2n for source label repetitions,
and p<=n+128+5log2 n+2Hscale<=2n; gradient repetition is O(log n).
No unknown constant hidden in an exponential is replaced by1.

Each live vector has O(L) entries of O(n) bits, including all buffers and
metadata copies. At most O(m(D+1)) vectors/tables are active; tD<=2n
gives m(D+1)<=3n/R. Thus their classical space is O(n^2 L/R),
which is O(n^(7/4)L) since R>=n^(1/4). Scalar arithmetic, fixed generated
directions, local leaf labels/Pascal work and control scratch fit O(n^2),
absorbed since L=2^R>=R>=n^(1/4). No original q-label list, global incidence
vector,2^t table or gate history is allocated. Finally L<=2*2^(n^(1/4)),
giving the stated S_C envelope with explicit inner coefficient1.

Quantum storage is O(mR(D+1))=O(n) sibling/index qubits, O(n) active rank,
equality/lookup/ripple scratch, the n-bit source data and p-bit gradient.
No table entries or one-flag-per-row arrays live in quantum space. Stages
reuse/reset work. All initialization and deallocation are charged.

controller-tools.md proves the complete bit-serial implementation and
O(n^2) fully charged work per core step, including the monitor's own
accesses, gate/wire addresses and direct source cost n+1. Here allocated
address length is O(n^(1/4)+log n), and clock width O(sqrt(n log n));
neither counter updates nor word operations are free. Every branch has
T=O(n^(37/4)(log2 n)2^((99/56)Hscale)).
Setup is polynomial plus fixed constants; table initialization and
abort cleanup have polynomial times S_C cost, absorbed by the strict growth
gap n^(1/4)<<sqrt(n log2 n). There is no free allocation or favorable cap branch.

Source-label replacement, gradient preparation/abort, finite phase rounding,
odd-part empirical estimation, source cutoff and core cutoff each cost at
most1/1024 under unconditional union/trace contraction with the exact
uncapped reference. Its two-adic outputs are exact on correct earlier
estimates and every root eventually terminates with finite expected cost.
Success>=1-6/1024>2/3 follows in the large branch; the fixed prefix succeeds>3/4.


## Sharper envelope with the identical finite program

The preceding inequalities are retained as all-size safety/probability
bounds, not claimed tight. The following analysis sharpens the declared
asymptotic time and sample coefficients without changing a single runtime
parameter, cap or instrument. Set the ANALYTIC threshold n0=2^256.
This threshold is never used by the program; all smaller n still follow
the already specified branches. It affects only an absolute outside constant.
Write x=log2 n and Hscale=sqrt(n*x). For n>=n0, ell<=x+1.
The elementary dyadic inequality ell<=n^(1/16)/4 follows by taking
j=floor(x)>=256: j+2<=2^(j/16)/4 at j=256 and induction, since
(j+3)/(j+2)<=259/258<2^(1/16). The last strict comparison follows by
raising to the sixteenth power. This proves the bound also between powers of2.
Thus
 m<=n^(1/4)*sqrt(ell)+2<=n^(9/32)/2+2<=n^(9/32),
so log2 m<=9x/32. The old r<=6n^(1/4) is unchanged.
Also R+v<=2n^(1/4)+ell+4<=4n^(1/4)<=Hscale/64;
the middle bound uses ell+4<=2n^(1/4), immediate from the dyadic bound.
Since t>=Hscale, b0=t-R-v>=63t/64 and D<=64n/(63t)+1.
It follows that
 log2 q<=log2 r+(D+1)log2 m
 <=(2/7)Hscale+(13/16)x+log2 6
 <=(2/7)Hscale+x+log2 6.
Consequently q<=6n*2^((2/7)Hscale).

For the enumeration width, T0<=sqrt(n*ell)+1 and t<T0+R, whence
 t<=Hscale*(1+1/(2x))+1+R<=257Hscale/256.
Here sqrt(1+1/x)<=1+1/(2x), x>=256, and
(1+R)/Hscale<=3n^(-1/4)<=1/512 suffice; all are explicit at n0
and persist as n increases. No approximation is used in program parameters.
The already established cap recurrences, mean plan, Sroot<=2sqrt q and
r>=n^(1/4) now give, for n>=n0,
 Qcap<=2^72 n^(5/2)(log2 n)*2^((3/7)Hscale),
 B<=2^220 n^(29/4)(log2 n)*2^((23/16)Hscale).
Indeed (3/2)(2/7)=3/7 and 257/256+3/7=2567/1792<23/16.
The same fully charged n^2 monitor/compiler overhead proves
 T=O(n^(37/4)(log2 n)*2^((23/16)Hscale)).
Storage and clean-input guarantees are identical to those already proved.

The finite range n<n0 has uniformly bounded ratios to the new positive
representatives: the old displayed cap bounds give explicit finite constants,
and the very small baseline prefix is already bounded. For example an
additional outside factor2^(4n0), times the old absolute implementation
constant, safely absorbs these finite ratios. Such a finite constant is
not a practical claim and is not a hidden coefficient inside the asymptotic
exponent. The exact growth indices remain1/2,1/4,0,1/2.
This candidate carries unsubmitted MSR2's bit-serial implementation and the
corrected MSR1 derivation, all reproduced. Its additional contribution is
this sharper analysis of the same runtime program. No old review certifies
these new claims, and no previous numerical result is a proof premise.

The time/sample logarithms are explicit positive constants times
sqrt(n)*sqrt(log2 n)+O(log n), giving exact index1/2. Classical logarithm
is n^(1/4)+O(log n), index1/4; linear quantum space has index0. All four
bounds and zero malformed-count guarantee refer to this SAME configuration.
No positive tolerance or impossibility for a larger count is inferred.


## Further single-term refinement of the published literal-root program

This candidate directly carries published MSR3,
5aafeb93-37d7-4b4c-bf75-44a2c84db4a8, including EVERY literal runtime
parameter, source/work cap, preparation, stream-rank circuit, literal-W root
rejection, decoder and controller from that archive. No known-frequency grid,
private quantum-counting/hash/window instrument or new oracle is used.
The preceding one-term envelopes remain valid weaker safety bounds. This
section proves the stronger declared coefficients for the SAME finite program;
the previous acceptance is not a premise for these new mathematical claims.

Set the ANALYTIC threshold n1=2^(2^20), never a program branch. Write
x=log2n>=2^20 and Hscale=sqrt(nx). Dyadic induction gives log2x<=x/8192,
so log2(4ell)<=3+log2x<=x/256 and ell<=n^(1/256)/4. Hence
 m<=n^(1/4)sqrt(ell)+2<=n^(129/512).
The old r<=6n^(1/4) is unchanged. Also ell<=n^(1/8) for n>=2^64,
so R+v<=4n^(1/4)<=t/512. Thus b0>=511t/512 and
 D<=512n/(511t)+1.
Integer rounding t<T0+R<=Hscale*(1+1/(2x))+1+R gives
 t<=1025Hscale/1024,
since1/(2x)<=1/2048 and(1+R)/Hscale<=3n^(-1/4)<=1/2048 in this range.
Every inequality is uniform for all n>=n1, not just powers of two.

It follows that
 log2q<=log2r+(D+1)log2m
 <=(129/511)Hscale+(193/256)x+log2 6,
so q<=6n2^((129/511)Hscale). The unchanged literal-root cap formulas,
Sroot<=2sqrt(q), A0^D<=2m^D and C=O(n log2n) give
 Qcap<=constant*C*q^(3/2)
 =O(n^(5/2)(log2n)*2^((387/1022)Hscale)).
For work the already proved Wstar<=100GCq^(3/2)/r, r>=n^(1/4) and
G=2^100n^5*2^t give
 B=O(n^(29/4)(log2n)*2^((1025/1024+387/1022)Hscale)).
The fixed rational comparisons are
 387/1022 <49/128,
 1025/1024+387/1022=721919/523264 <89/64.
The SAME fully charged n^2 controller/monitor allowance therefore proves
 T=O(n^(37/4)(log2n)*2^((89/64)Hscale)),
 Q=O(n^(5/2)(log2n)*2^((49/128)Hscale)).
No outside power, storage allocation, precision, success distribution or
clean-copy law changes. Both new coefficients are strictly below the
published time23/16 and source3/7, while both memory envelopes are identical.

The all-size cap inequalities already proved absorb the fixed interval
n<n1 with an additional absolute factor2^(4n1) times the implementation
constant, plus the stated exhaustive prefix. This enormous disclosed factor
is not a practical runtime claim or a hidden coefficient inside an exponent.
The numeric indices remain1/2,1/4,0,1/2. The whole-secret success and
malformed-count law0 are exactly those of the reproduced SAME finite program.
No old review is rebound to the new statements, structured objects or hashes.
