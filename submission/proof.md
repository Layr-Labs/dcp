# QSR4: polynomial classical storage with window-counted ranks

## Joint theorem, exact parameters and provenance

For every N>=2 and fixed s modulo N, n=ceil(log2 N), the SAME program
recovers the entire secret with unconditional probability>2/3 and has
these bounds on EVERY branch:

 T=O(n^(63/2)*(log2 n)^(-1/2)*2^(sqrt(n)*sqrt(log2 n)-2sqrt(n)*(log2 n)^(-1/2))),
 S_C=O(n^3*(log2 n)^(-1)) bits, S_Q=O(n) qubits,
 Q=O(n^(3/2)*sqrt(log2 n)*2^((1/2)sqrt(n)*sqrt(log2 n)-2sqrt(n)*(log2 n)^(-1/2))).

Resource representatives apply for n>=2, with n=1 fixed absolute
cost, storage and count. Outside constants are absolute. Growth indices are1/2,0,0,1/2.
The fifth law is0 under the canonical independent ideal-copy model.
No positive-corruption guarantee or maximum-tolerance impossibility is claimed.

This is a time/source/classical-memory tradeoff. It uses polynomial classical tables to remove the positive lower-order
exponent from the declared time and source envelopes. This costs more
classical memory than the quadratic and near-quadratic constructions. No tight-cost,
practical, optimality, fastest-known or cube-root claim is made.

For n<16777216 use the exact exhaustive baseline: n+2 fresh controlled-
subtraction/X tests per candidate t<N, returning the first all-plus candidate
or zero. True t passes certainly; each false candidate passes with probability
2^(-(n+2)), so success>3/4 by a union bound. Q<=N(n+2), T=O(2^n n^4),
and spaces O(n^2). The fixed finite prefix fits the displayed envelopes
with absolute constants, including n^2<=16777216n for quantum space.
A source/time outside constant as large as2^16777220 is allowed, explicitly
not a practical performance assertion. Remaining descriptions use n>=16777216.

Set ell=ceil(log2 n). Before any source/quantum work run
certified-log-tools.md with K=ell+16 to obtain exact rational xplus>=log2n
with error<=n^(-2). Set T0=ceil(sqrt(n*xplus)), R=ell,
m=ceil(T0/R), L=2^R, t=mR, using the helper's exact rational integer-root
and division algorithms. Set
v=ell+4, b0=t-R-v, D=ceil((n-1)/b0),
r=R+2ceil(log2(R+2))+8, q=r*m^(D+1).
All roots and ceilings are INTEGER algorithms with counted schoolbook work.
The polynomial-space schedule uses R=ell FIRST,
then m=ceil(T0/R); no irrational parameter is runtime advice.
No real advice or irrational parameter is used.
Set f0=8n/(8n-1), A0=m*f0,
Mgrid=2^20(q+1), hstat=ceil(log2(Mgrid+1))+ceil(log2(n+7))+20,
Kstat=2^32hstat, C=(n+5)Kstat+n,
Qstar=C*32r*m*A0^D, Qcap=ceil(1024Qstar),
p=128n.
Set G=2^10000 n^26*2^(ceil((t+5R)/2)), E0=G, E_i=f0(mE_(i-1)+G),
Wstar=G+C*32*(mE_D+G), B=ceil(1024Wstar).
The certified-log routine has separately charged worst-case O(n^16) work
and O(n^2) classical bits; it releases all large rational buffers before
the body. Other parameters below have O(n)-bit operands. Their deterministic exact
generation, including both caps, is also charged inside the O(n^16)
preprocessing allowance; the working clock then begins with quantum
preparation. No source copy is acquired during parameter generation.
Abort and output zero before a source acquisition would exceed Qcap
or a working core bit/gate step would exceed B. A separate terminal
cleanup allowance G is charged, so total core work is at most B+G<=2B;
cleanup acquires no source copies. Reserve a full gcount block
before each quantum count/factor call, aborting if it does not fit; completed
blocks are padded and charged. Monitoring and cleanup are charged.

The collimation/reindexing context is Kuperberg arXiv:1112.3333v1 Sections4.2,
4.3 and4.6. Regev quant-ph/0406151v1 Section3 supplies polynomial-space
multi-input subset-merging context. Their results/verdicts are not premises:
QSR4 supplies its complete rank instrument, probabilities and counted circuits.
It materially combines the locally archived COL13 constant-weight leaves
and PSR1 all-solutions stream enumeration (neither has a published
endpoint; all needed material is reproduced here). No novelty is asserted for these standard tradeoffs or ranking.

Published COL3,20dcb56f-cf80-4e95-8784-b2c66b9f6577, supplies carried aggregate,
unused-top-bit, all-moduli and cutoff arguments, reproduced here. Published
RLQGR2,8657ff0f-f4d3-4605-a583-a6d57d3205f4, supplies mixed-source eigenlabels;
published PG4,e40f2d5a-68c9-418b-b4e8-64a80305968e, supplied consulted gradient
kickback and one-initial-trace-error reuse. Their necessary helper arguments
and earlier Kitaev / Nam-Su-Maslov1803.04933v2 SectionII context are retained.
The ordinary mixed-eigenlabel gradient preparation differs from PG4's Fourier
circuit. No predecessor fast-arithmetic, robust-score or search circuit
is used. No source inverse, purification, hiding oracle or free QRAM is supplied.

This candidate carries published MSR3,5aafeb93-37d7-4b4c-bf75-44a2c84db4a8,
with its constant-weight tree and bit-serial accounting context. The local
MSR4/MSR5 known-frequency estimator is reproduced. This candidate replaces
stream enumeration by its new paid quantum-counting/hash rank instrument.
These changes require this candidate's own joint review. Other unpublished
parents are acknowledged without assuming their verdicts or inventing endpoints.

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
These inequalities hold for every R>=1, including this smaller-width regime. A rare individual h
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


## Multiway product ranking using counted quantum search

Take m same-level length-L vectors with common F and child records B_i[j],
U_i[j], h_i. Their product has t=mR index qubits and2^t equal-magnitude
amplitudes. Compute sum_i B_i[x_i] mod2^b, b<=b0, using m literal L-row
lookup/add networks from the preceding section, and measure the low key y.
Reset its register using the observed bits. This gives a uniform-magnitude
superposition on the set S of product indices with that key.

Apply hash-rank-tools.md IN FULL: privately factor-estimate its size, choose
a random binary index hash, measure that hash on the source phase index,
privately check its bucket size, and reject a large estimate. On an accepted
bucket run the explicit quantum-count-tools.md counter to compute rank(x),
then the binary-search inverse g(rank) to erase the old product index.
Only then measure the high rank bits and retain a full L chunk. If partial,
discard all m children and regenerate them. No exponential enumeration or
classical list of S is allocated. The phase-window counter uses O(n) qubits including private preparation
and unranking history, as proved in window-tools.md.

The helpers prove uniform regular-attempt failure<=1/(8n). This includes
original partial chunks, hash concentration failure and the bucket rejection
in the exact reference. Approximate count/factor errors are compared once
for the whole capped computation, not conditioned away from probabilities.
Every oracle call is its literal mL-row circuit with arithmetic/hash/compare
and reversed scratch. Private counting uses known H^t preparation and its
inverse; it never uses a DCP source preparation or inverse.

For the selected chunk generate ALL L metadata records by separately running
g on each known rank. This extra L factor is included in G. Measuring the
private deterministic reference result reveals no retained source phase.
Classically read the indicated child rows and write
 B_new=(sum_i B_i[z_i]-y)/2^b,
 U_new=sum_i U_i[z_i], h_new=sum_i h_i, F_new=F*2^b.
The quotient is exact. Its common offset is sum_i c_global_i+F*y. The
conceptual original incidence is the concatenation of child incidences,
binary and distinct for every output row. Hashing/ranking only select and
permute original indices. All raw/phase/common-weight invariants persist.
Release child tables and scratch with counted reset/deallocation work.

For target w<=n use D_w=ceil((w-1)/b0) regular levels, with a possibly shorter
last remainder. When w=1 there are none. A surviving vector uses exactly
r*m^D_w accepted base controls; discarded controls count separately. The
depth-first stack retains m-1 sibling indices/tables at each level. No
original-incidence or q-label array is physically stored.

## An extra product root with a known random frequency

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
reset its known bits. Apply the same hash sparsification and quantum-counted
rank/unrank instrument, retaining full PAIRS (one low rank bit) instead of
L-chunks. A singleton discards all children. The old unpaired mass is at most
(q+1)/2^t<=1/4; the helper adds less than1/12, so pairing succeeds with
probability at least2/3. Generate the two selected product tuples by the
counted inverse g, retaining only their two t-bit masks. No global incidence
vector is needed.

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
compute W. For the odd-part estimator keep EVERY W and the exact qubit
q_1(W*Ftarget*theta), including W=0. Conditional on W, forgetting other
metadata introduces no dephasing. Root success is at least2/3, with retries
only for unpaired outcomes. frequency-tools.md gives a counted classical
estimator using the known W, not a literal-frequency substitution.
For two-adic parity only, repeat until W is odd. Its conditional probability
is1/2 for every d>=2, so total acceptance per trial is at least1/3.
Arbitrary odd W is never treated as literal one for odd-modulus recovery.

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

For every j collect Kstat fresh known-frequency root qubits, with phase
2pi W*2^j*vartheta, vartheta=f*(s mod M)/M. Measure each in a fresh private
uniform X or Y basis and record(W,basis,outcome). frequency-tools.md proves
that empirical scoring on the exact Mgrid grid estimates each2^j*vartheta
to circular error<1/32 with simultaneous failure probability<1/1024.
It counts finite rational trigonometry and all grid loops, using only O(n^2)
classical records and a streamed maximum. No quantum root is retained after
its measurement. Its rational half-angle unwrapping and rounding recover
f*(s mod M), then invert f classically. Call the resulting odd-part answer r_secret. At M=1 set r_secret=0.
In the following two-adic paragraph write r=r_secret, distinct from the leaf-size parameter r.

Prepare the single gradient described below ONCE before any counting or
odd-part computation, including when a=0; its ideal state implements every
counting Fourier rotation exactly. Prepare the one bounded-attempt private
global window from window-tools.md before counting as well. Now write s=r+M*t, t in Z/2^a. At bit level ell=0,...,a-1 suppose t_low
contains its known ell low bits and set s0=r+M*t_low. A fresh untransformed
source, after label extraction and X, has phase q_k(s/N). Use the counted
gradient correction of gradient-tools.md to subtract known phase k*s0/N.
The reference phase is q_(k mod2^w)(t'/2^w), w=a-ell, t'=(t-t_low)/2^ell.
The reduced labels are independent uniform w-bit integers because2^w divides N.
No label filter is needed here. Repeat the root until its known W is odd,
giving relative phase(-1)^(W*t')=(-1)^t'. An X measurement gives the next bit EXACTLY in
the reference computation. Repeat and output r+M*t, the full representative s.
At most C=(n+5)Kstat+n completed root calls occur, with all internal
pairing/parity retries counted. On good odd-part estimation,
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



## Counted work, reference expectations and literal hard cutoffs

A CORE step is a fixed-size classical bit operation, gate, reset, private
random bit, source acquisition or bit of circuit/address generation, excluding
only the external monitor's own work. All ordinary arithmetic is bit serial.
No word, lookup, preparation, measurement, oracle, private helper or output
record is free. Exact Toffoli circuits have fixed Clifford+T decompositions.

hash-rank-tools.md expands one predicate into at most2^200 n^12 L core
steps, including its explicit row gates, arithmetic/hash and generation.
quantum-count-tools.md proves a count/factor block fits
 gcount=2^1000 n^25 2^(ceil((t+3R)/2)).
O(tL+1) blocks cover all rank/inverse, private factor estimates, exact bucket
readout and ALL L output records of one attempt. Other operations take
polynomial times L work, including generating random hash matrices, resetting
private registers, clearing tables, integer roots, Pascal leaf ranks and
coefficient generation. They fit the intentionally larger literal
 G=2^10000 n^26 2^(ceil((t+5R)/2)).
The source-label and gradient helpers fit2^200 n^8 as p=128n and H<=2n.
Leaf retries have an absolute geometric mean; expected leaf core cost<=G.
The one bounded gradient preparation and its failures also fit G. Its exact
ideal reference allows all dyadic counting rotations with p>=qpeBits.
window-tools.md gives the private global window, counted inside G.

In the exact reference a leaf needs<=4r source copies in expectation and
each regular group succeeds with probability>=1-1/(8n), uniformly for every
child table list and arbitrary phases. Write f0=8n/(8n-1), A0=mf0.
Then EQ_i<=A0 EQ_(i-1), EQ_0<=4r. Root parity acceptance>=1/3 and
pair acceptance>=2/3. Thus over at most C completed root calls,
 EQ<=Qstar=C32rm A0^D.
Uniform expected work is bounded by E0=G, E_i=f0(mE_(i-1)+G), with
 E_D=G*((8nm+1)A0^D-8n)/(8n(m-1)+1)<=2G A0^D.
All classical known-frequency grid work is at most(n+5)2^150n^12q<=E_D:
E_D>=G m^D, q=r m^(D+1), and G dominates2^151n^13rm.
Consequently EW<=Wstar=G+C32(mE_D+G). These estimates require only uniform
conditional success and mean bounds before fresh attempts, not independence
of complete tables or success-conditioned cost. Balanced magnitudes and low-
only selections make them uniform even after earlier secret-estimation errors.

Compute Qcap=ceil1024Qstar and B=ceil1024Wstar exactly. The physical program
checks source acquisitions, primitive core steps and count blocks BEFORE
they would exceed the corresponding caps. Before each whole gcount block,
reserve that entire paid amount and pad its execution to the fixed amount.
Thus no guard interrupts a unitary promised to be approximately clean.
An unsuccessful reservation means the corresponding uncapped reference has
cost>B, even though some budget remains. Both cap-abort probabilities are
at most1/1024 by Markov on the uncapped reference. All actual branches have
syntactic caps, including malformed internal approximate outcomes. Fixed
loop bounds and clamps make those outcomes legal finite encodings.

Use fixed bit-serial control and the COMPLETE monitor/address argument in
monitor-tools.md. For this polynomial allocation address length is
O(log n), while clock length is O(sqrt(n log n)). Its deliberately loose
per-core cost O(b*a^4+n), including every own-index/address operation,
is O(n). All core generation and ordinary arithmetic remain bit serial;
no word, query, source, controller or monitor is free. Terminal cleanup
uses its separate paid G, no sources, so body core<=B+G<=2B.

## Total metadata arithmetic on erroneous internal outcomes

Use signed8n-bit metadata fields and16n-bit classical/quantum scratch for
their sums; phase/gradient, count and search registers retain their specified
fixed widths. Before storing
a classical output record, verify its returned product mask has the measured
key and hash, check the normalized quotient remainder is zero, and check
field range. Check a read-out bucket count is in[1,Kcap], and check a returned
root frequency lies in[-q,q]. On a failed check or classical overflow return
zero globally. These checks cost polynomial per output row, fit the ordinary
2^800n^25L node ledger, and acquire no sources. Coherent predicate sums of
m8n-bit constants fit16n bits for every encoded input, since m<=n<2^n;
all reversible operations are complete fixed-width Boolean circuits.

In the exact reference every check passes: output masks belong to the measured
set, quotients are exact and metadata magnitudes are below q*2^n<2^(2n+1).
Thus these totality checks do not change reference retries, unused-top-bit
selection or expected-cost bounds. Their physical abort outputs are included
by unconditional channel contraction in the same global approximation hybrid;
they are not excluded by postselection or a new correctness assumption. All
actual branches remain fully defined even after arbitrarily bad approximate
count, factor or previous-secret outputs.

## Uniform polynomial-space parameters and precision

Write x=log2n,H=sqrt(nx), V=sqrt(n/x), n>=2^24, for ANALYSIS only. The runtime uses
ell=ceil(log2n),R=ell,L=2^ell and the short certified-log routine
K=ell+16. It proves0<=xplus-x<=n^(-2) and H<=T0<=H+2. Consequently
 x<=R<=x+1, L<=2n, H<=t<T0+R<=H+x+3,
 m>=H/(x+1)>=512, m<=n, r<=3R+8<=4R<=n.
Here H>=128x,H<=n/20,x^3<=n on this whole domain, by elementary monotonic
bounds checked at24. The leaf chunk inequality holds directly for every
R>=1 as already proved; it does not require independent phase-vector rows.

Since R+v<=2x+6, e=(R+v)/t<=1/64: (2x+6)/sqrt(2^x*x) decreases for
x>=24 and is less than1/64 at24. Thus b0>=63t/64,D<=64n/(63t)+1<=n,
tD<=2n and t-2R>=255H/256>=80x. This proves the private count bias cap
Kcap^2/2^t<=2^(80-76x)<2^(-1440). Its Fourier width is at most2t<p=128n.
No free dyadic gate or source-preparation inverse appears.

## Exact half-H source envelope with polynomial prefactor

The ceiling in m gives m<=(H+R+2)/R. Because R>=x,
 log2m<=x/2-(1/2)log2x+2(R+2)/H.
This uses log2(1+u)<=2u and involves only analysis constants, not a runtime
real logarithm. The full logarithm is positive, so n/t<=n/H yields
 (n/t)log2m<=H/2-(1/2)sqrt(n/x)log2x+2(R+2)/x<=H/2+3.
Retain the negative term in the sharper calculation below. Signed lower-order
coefficients ARE supported by the rational structured-bound contract.

Also2log2m<=x: the correction4(R+2)/H<=4(x+3)/(128x)<1 is smaller than
log2x. Thus1/(1-e)<=1+2e bounds the cancellation-denominator correction
2n(R+v)log2m/t^2 by R+v<=2x+6. Finally
2log2m+log2r<=x-log2x+4(R+2)/H+log2(4R)<=x+4,
since R<=2x and the positive fractional term is less than1. Hence
 log2q<=log2r+(n/b0+2)log2m<=H/2+3x+13<=H/2+3x+16,
 q<=2^16 n^3*2^(H/2).
This coarse bound is retained for the precision checks, but is not the final
resource claim. Retaining the negative term actually gives
 log2q<=H/2-(1/2)V*log2x+3x+13.
For x>=24, log2x>=9/2, since24^2>2^9. Also3x+13<=V/4:
at24, sqrt(24)<5 gives V/4>4096/20>85; the ratio
V/(3x+13)=2^(x/2)/(sqrt(x)(3x+13)) increases thereafter because its
logarithmic derivative is ln2/2-1/(2x)-3/(3x+13)>
1/3-1/48-1/24>0. Hence
 log2q<=H/2-(9/4)V+V/4=H/2-2V,
 q<=2^(H/2-2V).
These are uniform inequalities for every integer n>=2^24, not just powers
of two. Both final exponent terms have supported rational powers and exact
coefficients. Their sum remains positive in this domain.
In particular log2q+4<t,2^t>=4(q+1), and log2(q+1)<n/4.
All reference signed8n metadata fields fit, and Bernoulli gives A0^D<=2m^D.

## One confidence choice and complete guarded work

The same actual n-less confidence parameter has
hstat<=log2q+x+50<=H/2+4x+66<=H. Its grid/stage union proof is reproduced
in frequency-tools.md. Consequently Kstat<=2^32H,C<=2^35nH. The exact
source guard Qcap derived from Qstar<=64Cq proves
 Q=O(n^(3/2)*sqrt(x)*2^(H/2-2V)).
The loose Qcap<=2^100 n^5*2^(H/2) proves Hlabel<=2n and
8Qcap2^(-128n)<1/1024. All failed filters, root calls and retries count.

The actual block and node caps stay
 gcount=2^1000n^25*2^(ceil((t+3R)/2)),
 G=2^10000n^26*2^(ceil((t+5R)/2)).
Since t<H+R+2 and R<=x+1, ceil((t+5R)/2)<=H/2+3x+5.
Therefore G=O(n^29*2^(H/2)). The exact recurrence still proves
Wstar<=1000CGq/r. As r>=R>=x,
 B=O(n^(61/2)*x^(-1/2)*2^(H-2V)).
monitor-tools.md proves FULLY CHARGED O(n) per core event, including every
own-index/address generation and source cost n+1. The separately paid
terminal cleanup G and deterministic O(n^16) preprocessing are included.
Thus T=O(n^(63/2)*x^(-1/2)*2^(H-2V)).
The negative lower-order coefficient is explicit in both representatives;
no unspecified exponential O constant is hidden. The full clocks satisfy
log2B<=10300+110x+2H<n/8 throughout n>=2^24, using H<=n/20 and the
monotonic fixed/log terms. Thus all window/factor/count replacements total
less than1/1024 under the same fully counted cap.

## Joint polynomial storage and unconditional success

There are O(m(D+1))=O(n/R) resident tables, each L rows of O(n) bits.
Since R>=x and L<=2n, these use O(n^3/x) CLASSICAL bits. All other
classical body allocations use O(n^2): Dt^2<=2nt<=2n^2 hash matrices,
Kstat records of O(n) bits, streamed caps and powers, CRT/Euclid arithmetic
and phase estimates. The shortened exact logarithm uses O(x^3)<=O(n)
bits and the remaining pre-clock parameter generation O(n^2). Since x<=n,
all fit the SAME n^3/x peak bound. Every full allocation/address cost counts.

Product/sibling indices use O(tD+t)=O(n) qubits; private count/windows,
source data, fixed gradient128n and arithmetic scratch each use O(n) qubits,
with only a constant number live. Search history has O(t(R+x))=O(Hx)=O(n)
qubits, since x^(3/2)/sqrt(n) is bounded. No coherent median table, source
purification, q-label list,2^t solution list or free QRAM is allocated.

The six ordinary label/gradient/rounding/estimation/source-cap/work-cap
allowances total6/1024; the whole private-window/factor/count hybrid adds
at most1/1024. Totality checks pass on the exact reference and are
contractive abort channels on the actual computation. These are
unconditional comparisons, without conditioning IID on successful labels
or caps. Hence whole-secret success>=1-7/1024>2/3 in the large branch;
the finite exhaustive prefix succeeds>3/4. Actual erroneous internal
outcomes obey both guards, fixed widths and separate paid cleanup.

The fixed n<2^24 prefix is absorbed into absolute outside constants.
Time and source indices are exactly1/2; both polynomial space indices0.
The clean malformed-count law is0 without any maximum-tolerance claim.
This point spends more classical space than QSR1 or QSR2 to improve the full time and source envelopes with explicit negative
lower-order terms, and makes no joint-domination claim.
