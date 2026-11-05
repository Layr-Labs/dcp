# COL16: known-frequency grid decoding without literal-root retries

## Theorem, exact configuration and provenance

For every N>=2 and s in Z/NZ let n=ceil(log2 N). COL16 recovers the entire
secret with unconditional probability>2/3 from independent ideal source copies.
The SAME program has these bounds on EVERY branch:

 T=O(n^9 2^(2sqrt n)), S_C=O(n^(5/2) 2^(sqrt n)),
 S_Q=O(n) qubits, Q=O(n^2 2^(sqrt n)).

The displayed time/sample envelopes apply for n>=2; n=1 has fixed absolute
cost and count. All outside constants are absolute. Indices are1/2,1/2,0,1/2. T is total charged
sequential work, not quantum depth. Q includes every filter/restart/discard.
The fifth law is0 under the canonical independent ideal-copy model, making
no impossibility claim about positive tolerance.

For n<262144 use the repository exhaustive baseline: for each t<N take n+2
fresh controlled-subtraction/X tests, reject on minus, return the first all-plus
candidate or zero fallback. The true shift passes certainly and any false
one passes with probability2^(-(n+2)); union gives success>3/4. Controlled
modular arithmetic has polynomial work/space by the clean construction below.
Q<=N(n+2), T=O(2^n n^4), S_C,S_Q=O(n^2) there. This FIXED finite prefix
fits the theorem after an absolute outside constant; for quantum space use
n^2<=262144n. The sample outside constant may be as large as2^262148, not a
practical claim. The rest describes n>=262144.

Set u=ceil(sqrt n), ell=ceil(log2 n), R=u+ell+16, L=2^R,
v=ell+4, b0=R-v=u+12,
D=ceil((n-1)/b0).
Set r=R+2ceil(log2(R+2))+8, q=r*2^D.
Define f0=16n/(16n-1), A0=2f0=32n/(16n-1),
Mgrid=2^20(q+1), hstat=ceil(log2(Mgrid+1))+ceil(log2(n+7))+20,
Kstat=2^32hstat, C=(n+5)Kstat+n,
Qstar=C*32r*A0^D, Qcap=ceil(1024Qstar),
p=n+ceil(log2(Qcap+2))+40.
Finally define G=2^100 n^5 L,
E0=G, E_i=f0(2E_(i-1)+G),
Wstar=G+C*16*(E_D+G), B=ceil(1024Wstar).
All rational powers here are integer powers and are computed EXACTLY.
There is no real arithmetic in parameters. Stop and output zero before a
source acquisition would exceed Qcap, or before core basic steps would exceed B.
The precise core-step convention and charged clock overhead appear below.
Parameters and fixed direction tables are generated before starting that clock, with
all their deterministic work/space charged. No advice is supplied.

The collimation/trim method materially uses Kuperberg, Another subexponential-
time quantum algorithm for the dihedral hidden subgroup problem,
arXiv:1112.3333v1 Sections4.2,4.3,4.6, Algorithm4.1 and Proposition4.5.
https://arxiv.org/pdf/1112.3333 . COL16 reproduces the needed argument and adds
the explicit root instrument and source-only all-moduli recovery below.
COL16 carries the complete locally archived COL13 constant-weight leaves,
prefix maps, depth-first storage, raw aggregates, source interface and charged
bit-serial controller (not yet published). It changes the final root output
and odd-part estimator: every selected pair supplies its KNOWN frequency,
and frequency-tools.md estimates each phase by explicit classical grid scoring.
It does not assert that an arbitrary odd frequency gives the desired odd-modulus
phase. The two-adic branch uses odd frequency only for parity, where it is exact.
The fixed G and the explicit absorption inequality cover all estimator and control work. All material from
unpublished local candidates is reproduced; no old verdict is a premise.
COL5 is276b1e08-9cd2-445e-b5ca-20e6eda6e4c6, COL4 is
a0d59808-df61-4241-88c2-19430194b090 and published COL3 is
20dcb56f-cf80-4e95-8784-b2c66b9f6577. All needed arguments are reproduced.
Label extraction and measured-eigenstate gradient preparation are from our
CGRST1 bc7954eb-c7bb-47c0-abcd-6a95a0257673 (its hosted review failed without
verdict/publication). Their arguments are reproduced, not assumed accepted.
Published RLQGR2 8657ff0f-f4d3-4605-a583-a6d57d3205f4 supplies the label
technique. PG4 e40f2d5a-68c9-418b-b4e8-64a80305968e supplied the consulted
reusable-gradient/kickback and one-initial-trace-error design; its own
Nam/Su/Maslov arXiv:1803.04933v2 SectionII attribution is retained. Our mixed
register preparation differs from PG4's preparation. No external theorem,
old verdict, heuristic table distribution, free QRAM or subset-sum oracle
is a premise. This is not a new fastest-known DCP algorithm or cube-root goal.

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
The first inequality is adequate here since R>=628. A rare individual h
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

For two same-level child tables A_i,B_j and prescribed b<=b0, compute
y=(A_i+B_j) mod2^b on their product R-bit indexes with two L-row XOR lookups
and ripple arithmetic. Measure y, uncompute label scratch from unchanged i,j,
and reset the measured bucket register using its classical value. Indexes
remain unmeasured. This represents L^2 basis amplitudes, not an L^2 table.

A CLASSICAL right descriptor sorted by(B_j mod2^b,original j) supplies
count[r],start[r],sortedB[m] and within[j]. Residue arrays have2^b<=L/(16n)
entries; within[j] is zero-based rank in j's residue, so
sortedB[start[r]+within[j]]=j for r=B_j mod2^b. After measuring y construct
c_i=count[(y-A_i) mod2^b], S_i=start[(y-A_i) mod2^b],
P_0=0, P_(i+1)=P_i+c_i for i=0,...,L-1. There are O(L) rows.
M=P_L<=L^2 is the bucket size; endpoints/counts use2R+1 bits to include
M=L^2. Define abort for M=0, a zero-probability bucket on any input support.

On this bucket f(i,j)=P_i+within[j] is an injective rank in[0,M), in original
lexicographic(i,j) order. Compute it into a clean2R-bit z with L-row lookups
and ripple sum/copy/inverse. Extend f outside this bucket by addition modL^2.
The inverse g(z) is explicit: scan L disjoint intervals[P_i,P_(i+1)), compare
constant endpoints to zero-extended z, and XOR the unique matching i into
clean scratch. Empty intervals do not match; outside[0,M) use zero default.
Load P_i,S_i by L-row lookup, compute m=S_i+z-P_i and j=sortedB[m] by another
L-row lookup. On valid ranks0<=m<L. Modular2R+1-bit arithmetic and default
zero outside[0,L) define g everywhere else. Compute g in CLEAN scratch,
XOR both values into OLD i,j, then reverse all g scratch. Since g(f(i,j))
=(i,j) on the measured bucket, old indexes become zero and can be released.
This composition of complete compute-XOR circuits is unitary globally; it
does not assume the old target registers were zero. It acts by linearity
also with arbitrary entangled outside systems.

Every quantum table use is a sequential scan: compare its O(n)-bit key with
each constant row, XOR the value controlled on equality, then uncompute
comparison scratch. The inverse scans intervals, NOT quantum-addressed binary
search. A constant number of L-row scans, O(n)-bit arithmetic and reused
O(n) scratch suffice. Classical constants, bit reads, gate generation and
addresses are fully charged. No QRAM or per-row quantum flags are supplied.

Measure the high R bits of z (chunk), retaining low R as index. Discard a
short last chunk and regenerate BOTH children. The joint(bucket,chunk)
instrument is exactly consecutive length-L lexicographic blocks per bucket.
For ideal uniform magnitudes, bucket mass is M_y/L^2 and conditional short
mass is(M_y modL)/M_y. Consequently total short probability is
sum_y(M_y modL)/L^2<=2^b(L-1)/L^2<=2^(-v)<=1/(16n)
for EVERY pair of tables. This is
BEFORE conditioning on y; individual small buckets can be entirely short.

For a full chunk enumerate its L ranks CLASSICALLY. Binary search P for the
last prefix<=z (P_L=M>z) finds i even with repeated empty prefixes; read
j=sortedB[S_i+z-P_i]. These are ordinary addressed classical operations,
not quantum search. Generate only L output rows:
F_new=F*2^b, b_new=(A_i+B_j-y)/2^b,
ellSum_new=ellSum_left_i+ellSum_right_j, h_new=h_left_i+h_right_j.
The removed phase exp(2pi i F*y*theta) is common; c_new=c_left+c_right+F*y
establishes the aggregate invariants. Distinct conceptual incidences concatenate
on disjoint child coordinates. Old tables/registers are released after use.

All classical sorting is explicit bottom-up merging: sorted runs of length1,
merge adjacent runs into the second buffer by the stated lexicographic key,
choose original-index ties first, double run length, handle end/run tests.
For O(L) rows this needs O(R) passes of O(L) comparisons/copies and two
O(L) buffers. Root sorting uses low-sum quotient and original root index.
Only cancellable low residues order buckets; high phase labels do not.

For target width w use D_w=ceil((w-1)/b0) levels, cancelling b0 bits each
except the final remainder. Total cancellation is w-1. If w=1 there are no
levels. Every surviving tree contains EXACTLY q_w=r*2^D_w original phase
controls, at most q; this is a PROOF count, not an allocated incidence register.
Depth-first traversal stores one R-qubit sibling per level. Release failed
states/tables before retrying; all failed acquisitions and attempts are counted.

Decisions, bucket ordering and trimming use only INITIAL label bits below
w-1. Although the full b values are stored, they never select or order pairs
except through the prescribed cancellable low residues. Each total cancelled
prefix is at most w-1, so unused top bits cannot enter those residues after
normalization. ellSum and h use only low parts and original index bits.

## A final pair with a known centered-binomial frequency

At the root F=Ftarget=2^(w-1). In the ANALYSIS write each original accepted
label a_i=ell_i+F*t_i with ell_i<F and independent fair top bit t_i. All
earlier choices use only ell_i and computational indices. Thus the current
tree's unused t_i stay independent fair bits conditional on those choices,
NOT conditional on the full stored high-label transcript. Computational
partition probabilities are subset sizes independent of phases/top bits;
failed earlier root attempts use fresh source copies.

Root entries have distinct conceptual binary incidences x on q_w<=q controls.
Their initial full sums share a residue modulo F by the invariant. Their
ellSum values therefore share that same residue. Group entries by
floor(ellSum/F), using the same explicit merge algorithm with original
root index as the last tie key. There are at most q+1 keys since ellSum<qF; weight is already
constant throughout this tree. Pair consecutive original indices in each key, discarding
singletons by the same reversible reindex/measurement construction with
block size2. All these decisions still omit top bits. Paired probability
is at least1-(q+1)/L>=3/4 by the inequalities below.

For a selected pair x,y, equal key and common remainder imply equal EXACT
low sums. The propagated common weight gives equal Hamming weight. Their conceptual Hamming
distance T is even and at least2; y-x has T/2 plus and T/2 minus coefficients.
Consequently the ORIGINAL full-label difference divided by F is
W=sum_i t_i(y_i-x_i), distributed as Bin(T,1/2)-T/2. Hence

 E exp(2pi i W delta)=cos(pi delta)^T, |W|<=q.

The controller need not compute x,y or T. By the root invariant it computes
W EXACTLY as b_y-b_x from the two stored O(n)-bit phase labels, ONLY AFTER
selecting and measuring that pair. Return this W together with the retained
qubit q_(WF)(theta). DO NOT reject W=0, nonunits, even or large frequencies
in the odd-part estimator. Conditional on W, the phase state is exact up to
a global scalar, so forgetting other metadata does not dephase it.
The root repeats only when no pair was selected. Its success probability
is at least3/4, independent of phase values. Every retry uses fresh copies.
The low-sum/common-weight decisions omit the top bits, so the displayed
centered-binomial law holds before full-label conditioning, including the
random selected pair. frequency-tools.md uses precisely this joint law.
For two-adic parity only, repeat until W is odd. Given any T>=2,
Pr(W odd)=1/2 by the binomial generating function at-1. Together with
pairing, this branch succeeds with probability at least3/8 per attempt.

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

For every j collect Kstat fresh known-frequency root qubits. A returned
pair has state q_(WF)(alpha_j*s/N), or relative phase2pi W*2^j*vartheta,
where vartheta=f*(s mod M)/M. Measure each in a fresh private uniformly
chosen X or Y basis and store only(W,basis,outcome). frequency-tools.md
proves that streaming over the Mgrid rational phase candidates and maximizing
its bounded empirical score estimates2^j*vartheta to circular error<1/32.
Its simultaneous failure probability over all grid points and stages is
<1/1024, with all finite trig approximations included. This uses no quantum
rotation, free phase estimation, FFT or original-source purification.
Apply that helper's rational half-angle unwrapping and round M times the
result to recover f*(s mod M) modulo M, then invert the known unit f.
At M=1 set r=0 and skip this odd-part step. At most(n+5)Kstat root outputs
are requested, all measured/released immediately, with only O(n^2) ordinary
record bits at one stage and a streamed running grid maximum.

If a>0 prepare the single gradient described below before the two-adic
loop; if a=0 omit that preparation. Now write s=r+M*t, t in Z/2^a. At bit level ell=0,...,a-1 suppose t_low
contains its known ell low bits and set s0=r+M*t_low. A fresh untransformed
source, after label extraction and X, has phase q_k(s/N). Use the counted
gradient correction of gradient-tools.md to subtract known phase k*s0/N.
The reference phase is q_(k mod2^w)(t'/2^w), w=a-ell, t'=(t-t_low)/2^ell.
The reduced labels are independent uniform w-bit integers because2^w divides N.
No label filter is needed here. The root(w) is repeated until its known W is odd, giving
relative phase(-1)^(W*t')=(-1)^t'. An X measurement gives the next bit EXACTLY in
the reference computation. Repeat and output r+M*t, the full representative s.
At most C=(n+5)Kstat+n completed root calls occur (with the counted
internal pairing/odd-frequency retries). On good odd-part estimation,
this is correct; even if a previous estimate were wrong, all qubits remain
balanced phases and the cost/partition bounds below still hold uniformly.
In particular the pairing and parity decisions depend on uniform classical target labels,
not on whether their assigned phase function was correct.

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

## Expected reference costs and explicit hard cutoffs

Let EQ_0=4r. Each leaf attempt needs r accepted labels, with at most2r
source acquisitions in expectation. Retention is at least15/16 globally
and uniformly in the labels, so its mean is at most32r/15<=4r. Every
partial weight-chunk attempt and rejected source acquisition is included. For collimation levels, every attempt succeeds with probability
at least1-1/(16n) conditional on any tables/history. Fresh children and discarded
copies are charged. Thus EQ_i<=A0*EQ_(i-1), A0=32n/(16n-1). Root attempts have
success at least3/4 for known-frequency output and3/8 for two-adic odd
output. Expected source acquisitions over all calls are at most
C*(8/3)*EQ_D<=C*(32/3)r*A0^D<Qstar=C*32r*A0^D.
Uniform conditional bounds justify these geometric sums without asserting
independence of entire random tables. Qcap=ceil1024Qstar then gives source
cap abort probability<=1/1024 by Markov in the uncapped reference computation.
The actual source counter aborts BEFORE exceeding Qcap. All attempts, filters
and failed trees are included. Qcap is computed FIRST, before defining the
planned label-extraction precision; there is no circular parameter definition.

Here a CORE BASIC STEP is a fixed-size classical Boolean operation/bit read/
write, circuit gate, measurement, reset or source acquisition in the literal
uniform algorithm, including bit-level circuit generation but excluding the
main clock monitor's own updates. Arbitrary words are never basic steps.
The fully charged overhead, including that monitor and addresses, is bounded
separately. After deterministic parameter/fixed-table generation, run the core
under a B-step clock. If another step would exceed B, abort and output zero.
Abort cleanup is counted below; no favorable branch is postselected.

Use the explicit nonrecursive allowance G=2^100 n^5 L per internal
attempt/final processing, expected leaf, and bounded gradient preparation.
Phase labels/low sums have at most n+ceil(log2(q+1))+1<=3n bits; aggregate,
descriptor and interval fields are O(n) bits. Each record fits2^10 n bits.
There is no L^2 table or allocated conceptual-incidence graph.

Descriptors/counters/prefixes scan O(L) rows. Merge sorts and classical output
searches take O(R) passes/steps per row. Each quantum lookup/interval network
scans L rows. Root pairing and leaf subset tables have L rows. Leaf unranking has r
iterations with at most r coefficient scans each, r-bit ripple operations,
and O(n)-bit metadata additions. These fit the stated record-operation
allowance. Classical Pascal setup and the single quantum rank/unrank circuit
have polynomial work smaller than the G slack. Full path
cleanup touches O(n L) rows. Fewer than2^10 n^2 L record operations cover all.
Here is a concrete conservative BIT controller bound for each record.
The independent allocation below has at most2^(2^10 u) addressed bits and
wires for u>=512, even including all temporary scalar parameter generation.
Indeed tables have O(n^2 L) bits, scalar arithmetic uses polynomial space,
R<=2u, log2 n<=u/16, and the fixed rational-direction tables are finite
generated constants. Source/work counter lengths are also at most2^10 u:
from the exact new cap formulas alone and hstat<=2n, the allowance
G=2^100n^5L gives B<=2^300 n^(15/2)*2^(2u).
Its bit length is at most301+(15/2)log2 n+2u<=2^10u for u>=512.
This algebraic bound does not assume that the present core
cost bound is correct. Use A=ceil(2^10 u) address bits, padding short
controller words if convenient; they fit within the same allocation.

Implement the controller as a fixed finite-control bit-serial machine with
explicit work-tape heads. Head moves, bit reads/writes and Boolean transitions
are core operations; all tape accesses still receive the full allocation
address charge below. Gate descriptions and their wire addresses are built
on these tapes and streamed. There is no free indexed instruction lookup.
Implement iteration by Boolean ripple counters and sequential bit pointers.
Compute a record base from its row index and fixed stride ONCE using counted
schoolbook multiplication/addition. Within that record, increment/decrement
a bit pointer, instead of multiplying row/stride again for each bit. Each
complete pointer update, loop test, bit-index update, fixed-gate emission
and O(A)-bit control arithmetic takes at most a fixed constant times A^2
CORE bit operations. This includes the emitter's own bit-loop counters and
address calculations: a ripple loop has at most A positions, and even
allowing A bit operations to locate/update its current position gives A^2.
Every bit read/write/gate is still separately charged later by the full
allocation's addressing cost. No O(A)-bit word instruction is a basic step.

Copy/add/compare of an O(n)-bit record and emission of its ripple/lookup row
have O(n) elementary bit/gate positions. Prefix output search has O(R)
iterations with O(R)-bit counters/intervals, hence O(R^2) such positions.
Classical leaf unranking has r iterations with O(r)-bit comparison/subtraction
and coefficient addressing, hence O(r^2) positions and at most r base
computations. Constructing its subset metadata has at most r passes over
O(n) bits. All have at most2^12(nr+r^2+n) positions plus2^12 r base
computations. Since r<=3u, u^2<=2n and A^2<=2^21 n, their bit-pointer and
base work fits2^40 n^3 core operations, with ample fixed Boolean-gate slack.
Sorting treats record comparison/copy as one such operation; its O(R)
passes were already counted among the2^10 n^2 L record operations.

Quantum leaf ranking/unranking uses O(r^3) constant-bit/equality gate
positions (r steps, at most r coefficient rows, O(r) bits per row), and
O(r) scratch. Its complete emitted controller work is polynomial and
below the helper2^82 n^8 allowance below; it is once per leaf attempt,
not once per table row. Pascal generation has O(r^3) bit positions and
its own charged pointers. Thus tables, sorting, lookup/frame generation
and all record control cost at most2^50 n^5 L core operations. The stated
loop strategy also covers resets, copies and inverse circuits; no gate
stream or failed history accumulates. It is an explicit loose upper bound,
not a machine-word RAM accounting or an optimal controller claim.

A source extraction has2(n+5)*2^24 H tests, H<=2n, each within2^20 n^4
core steps including translation/controller. Expected leaf acquisitions are
at most4r; gradient preparation has p<=2n and at most2n attempts with the
same elementary routines. Each helper fits2^80 n^8, including means, decoding,
Euclid, known corrections, resets and inverse work. Direction constants are
separately generated before the clock and charged. For u>=512, n<=u^2 and
log2 u<=u/32 (proved below), so3log2 n<=6log2 u<=3u/16<R and n^3<=L.
Hence2^82 n^8+2^51 n^5 L<G/2. This also covers each leaf
attempt, including both ranking circuits and its table enumeration; multiplying
by16/15 for leaf retries leaves expected leaf core cost below G. Ideal rejection loops are charged in expectation;
actual counters stop every branch. Global address/monitor charges follow below.

frequency-tools.md bounds total classical grid postprocessing by
(n+5)2^150n^12q<=E_D. At most O(n^2) extra record bits and O(n)-bit
scalar scratch are needed. Its trig computation, signed reductions, score
sums, grid loop and their own bit control are primitive core steps; all
receive the same addressing and monitor charge below. A geometric root
retry contributes at most(8/3)(E_D+G) per requested root; C completed root
calls plus all grid processing and gradient setup are bounded by
G+C*16*(E_D+G). The explicit inequality in frequency-tools.md absorbs grid work into E_D.
The core implementation retains its proved nonrecursive slack.

Consequently E_0=G, E_i=f0(2E_(i-1)+G) bound expected core steps of
one vector, and Wstar=G+C*16*(E_D+G) bounds the entire uncapped reference.
All costs are uniform over phase values: computational partitions see only
uniform magnitudes, even if a preceding phase estimate was wrong.
B=ceil1024Wstar gives clock-abort probability<=1/1024 by Markov. No per-node
polynomial retry cap is multiplied through the tree. Both caps are computable
rational formulas, not unproved expected-only resource claims.

## Uniform charged resources and exact growth indices

For u>=512, log2 u<=u/32: on[2^k,2^(k+1)) with k>=9,
log2 u<k+1<=2^(k-5)<=u/32, with induction for the middle inequality.
Since ell<=2log2 u+1, R<=u+2log2 u+17<=2u.
Also ceil(log2(R+2))<=log2 u+3, so r<=R+2log2 u+14<=3u.
The last inequalities follow from log2 u<=u/32 and u>=512.
Now b0=u+12>=u, and n<=u^2 implies D=ceil((n-1)/(u+12))<=u.
Bernoulli gives f0^D<=16/15<2, since D<=n. Consequently
 2^D<=2^u, A0^D<=2^(u+1), q=r2^D<=3u2^u.
Meanwhile L=2^(u+ell+16)>=2^16 n2^u>=4(q+1).
For the last bound, n>(u-1)^2 and u>=512 give2^16n>=12u+4.
Thus every root has paired mass at least3/4. No second-order asymptotic
identity or ignored log factor is needed for these exact integer parameters.

The same q bound gives log2(q+1)<=u+log2 u+3. Hence
hstat<=u+3log2 u+47<=2u for u>=512, and Kstat<=2^33u.
C<=(n+5)2^33u+n<=2^35nu<=2^36 n^(3/2).
Together with r<=3u, A0^D<=2^(u+1), the literal source formula gives
 Qcap<=2^80 n^2*2^u.
Source extraction precision obeys H<=128+6log2 n+2u<=2n and
p<=n+128+5log2 n+2u<=2n. All operand and preparation bounds stay valid.
The gradient repetitions are O(log n). No source count is inferred from a
favorable branch or guessed exponential coefficient.

We have L<=2^17n2^u, since ell<log2 n+1 (with equality harmlessly
weakened when n is a power of2). Thus G=2^100n^5L<=2^117n^6 2^u.
The exact recurrence gives G A0^D<=E_D<=2G A0^D. Applying C's bound to
Wstar=G+C16(E_D+G) yields
 B<=2^300 n^(15/2)*2^(2u).
All fixed factors and ceilings fit the stated constant. The address/counter
bound used above remains independent and valid: this cap has bit length
at most301+(15/2)log2 n+2u<=2^10u. Parameter generation is counted.

Classical memory contains active descriptor/sort/lookup tables of at most O(L)
records each with O(n) bits, a constant number of merge buffers, and at most
D sibling tables/frames. Even bounding every path frame by O(L) rows gives
O(n*(D+1)*L+n^2) bits including all copies, metadata, counters,
estimator records and scratch. Since D<=u and L>=sqrt n, this is
O(n^(3/2)L), hence O(n^(5/2)2^(sqrt n)).
No original q-label list, q-bit incidence array or failed history accumulates.
The largest address length is O(u+log n), and source/work counters have that
same order of bits. Use the bit-serial controller described above and the independent
A=ceil(2^10 u) bound. An ordinary core bit access or a bounded-arity
gate has at most a fixed number of addressed operands; their full
log(total allocated bits+qubits) charge is at most O(A). Its address
generation and circuit emission were already counted among core bit steps.
A source acquisition additionally costs n+1, hence O(n), exactly as required.
There is no free source or initialization operation.

Implement the B-step monitor with an at-most-A-bit counter and the stored
at-most-A-bit constant B. Before a core step compare the counter to B,
abort if equal, otherwise increment. Bit-serial ripple comparison/increment,
head return, loop indexes and pointer generation use O(A^2) primitive bit
operations under the explicit word-loop bound already proved above. EVERY
one of these monitor operations also pays its O(A) allocated-memory
access charge; the monitor is not itself recursively monitored. Its work
is thus O(A^3), including its own control and addressed reads/writes.
The core clock measures only core work by definition, but the entire
monitor work is added here deterministically, not hidden in that definition.
Since u<=2sqrt n, A=O(sqrt n), so O(A^3+n)<=O(n^(3/2)) is a conservative
fully charged allowance per core step. This also covers quantum wire
addresses, bounded-arity Clifford+T execution and direct source cost.
Thus every branch, including abort cleanup and all setup, has
T=O(n^9 2^(2u)). Cleanup scans at most the smaller classical-memory
envelope; each cleanup bit access pays the same full address charge and
bit-serial control. Its polynomial times n^2 L cost is absorbed by the
strict exponential-coefficient gap1<2. Deterministic
parameter setup is polynomial plus fixed generated constants. If all
stack/table storage is reserved initially, explicitly writing every bit
with these same address/control charges has polynomial times n^2 L cost
and is absorbed by that strict coefficient gap; allocation is not free.
Ceil u differs from sqrt n by<1, affecting only absolute outside factors.

Quantum space is one R-bit sibling per recursion level, old pair indexes, a2R-bit rank register and
O(R) inverse/equality/lookup scratch, leaf controls, one n-bit data/extraction system,
and the p-bit gradient with O(n) arithmetic scratch. R(D+1)=O(n), p<=2n;
stages reuse work. Conceptual incidences are NOT physical quantum or classical
registers. Thus S_Q=O(n). Classical space is O(n^(5/2) 2^(sqrt n)); Qcap fits
O(n^2 2^(sqrt n)). The fixed finite branch was covered above.
All inner coefficients are explicit; no O() in an exponent is replaced by1.
These are simultaneous worst-case branch guarantees for this same program.

Source-label replacement, gradient preparation/abort, phase rounding,
odd-phase estimation, source cutoff and time cutoff each cost at most1/1024
in the comparison with the uncapped exact reference. Its final two-adic
measurements are exact and all phase generators eventually succeed with
finite expected cost. Union/trace contraction yields success>=1-6/1024>2/3
for large n; the finite branch succeeds>3/4. No conditional independence is
asserted after selecting a favorable cap/label event.

The logarithm of each exponential envelope is its explicit positive constant
times sqrt n plus O(log n), giving exact index1/2. The quantum polynomial
index is0. Canonical error tolerance is0: every acquired copy is ideal and
independent; no malformed-copy guarantee or maximum-tolerance impossibility
is inferred. The theorem is an explicit all-moduli collimation tradeoff with
linear quantum space and charged table access. It is not a novel fastest-known
DCP regime, an optimality claim, a practical runtime measurement or the stated
2^{O(n^(1/3))} research goal.

This candidate carries the complete local COL15 known-frequency decoder,
prefix mapping and controller. Its new integer R=u+ell+16 gives the exact
2sqrt(n) time coefficient, sqrt(n) sample coefficient and sqrt(n) classical
coefficient with fully exposed polynomial factors. It trades a larger sample
coefficient than COL15 for smaller time/classical coefficients. This is not a
claim to dominate COL15 jointly. No earlier verdict is rebound.
