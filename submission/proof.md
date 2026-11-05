# COL5: bounded depth-first collimation with literal-frequency output

## Theorem, exact configuration and provenance

For every N>=2 and s in Z/NZ let n=ceil(log2 N). COL5 recovers the entire
secret with unconditional probability>2/3 from independent ideal source copies.
The SAME program has these bounds on EVERY branch:

 T=O(n^(33/2) 2^((96/31)sqrt n)), S_C=O(n^2 2^(2sqrt n)),
 S_Q=O(n) qubits, Q=O(n^3 2^((34/31)sqrt n)).

All outside constants are absolute. Indices are1/2,1/2,0,1/2. T is total charged
sequential work, not quantum depth. Q includes every filter/restart/discard.
The fifth law is0 under the canonical independent ideal-copy model, making
no impossibility claim about positive tolerance.

For n<4096 use the repository exhaustive baseline: for each t<N take n+2
fresh controlled-subtraction/X tests, reject on minus, return the first all-plus
candidate or zero fallback. The true shift passes certainly and any false
one passes with probability2^(-(n+2)); union gives success>3/4. Controlled
modular arithmetic has polynomial work/space by the clean construction below.
Q<=N(n+2), T=O(2^n n^4), S_C,S_Q=O(n^2) there. This FIXED finite prefix
fits the theorem after an absolute outside constant; for quantum space use
n^2<=4096n. The sample outside constant may be as large as2^4100, not a
practical claim. The rest describes n>=4096.

Set u=ceil(sqrt n), R=2u, L=2^R, b0=R-4, D=ceil((n-1)/b0), q=R*2^D.
Define A0=32/15, m_est=2^24(n+20+ceil(log2(n+5))),
C=2(n+5)m_est+n,
Qstar=C*8R(q+1) A0^D, Qcap=ceil(1024Qstar),
p=n+ceil(log2(Qcap+2))+40.
Finally define G=2^100 n^10 L,
E0=G, E_i=(16/15)(2E_(i-1)+G),
Wstar=G+C*4(q+1)(E_D+G), B=ceil(1024Wstar).
All rational powers here are integer powers and are computed EXACTLY.
There is no real arithmetic in parameters. Stop and output zero before a
source acquisition would exceed Qcap, or before core basic steps would exceed B.
The precise core-step convention and charged clock overhead appear below.
Parameters/constant tables are generated before starting that clock, with
all their deterministic work/space charged. No advice is supplied.

The collimation/trim method materially uses Kuperberg, Another subexponential-
time quantum algorithm for the dihedral hidden subgroup problem,
arXiv:1112.3333v1 Sections4.2,4.3,4.6, Algorithm4.1 and Proposition4.5.
https://arxiv.org/pdf/1112.3333 . COL5 reproduces the needed argument and adds
literal-frequency selection and source-only all-moduli recovery below.
COL5 materially builds on COL4 candidate a0d59808-df61-4241-88c2-19430194b090 for the
measured-bucket prefix map and the reproduced COL3 aggregate/recovery/cap
framework. It changes the actual R from4u to2u, rederiving depth, source,
precision, root support and work bounds below. It improves time and classical
space at higher source complexity; no simultaneous source improvement is
claimed. Published COL3 is20dcb56f-cf80-4e95-8784-b2c66b9f6577. Earlier
COL2/COL1 and mixed-gradient provenance are retained. No prior verdict is
a premise, and standard prefix sums or collimation are not claimed as inventions.
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

## Elementary source and permutation tools

Let chi_k=N^(-1/2)sum_x exp(2pi i kx/N)|x> and
phi_(k,s)=(|0>+exp(-2pi i ks/N)|1>)/sqrt2. Expansion of the specified rho_s
and summation over its uniform x gives exactly
rho_s=(1/N)sum_k |phi_(k,s)><phi_(k,s)| tensor |chi_k><chi_k|.
These are ensemble identities, not a Fourier circuit assumption.
label-tools.md implements counted controlled-translation/X/Y eigenlabel
extraction. Use original modulus N, d=n and planned total C=Qcap there.
It returns every true label before the cap except with probability<1/2048.
Conditional on a latent label, the source control is unchanged. Apply X to
that control to obtain, up to a global scalar, the POSITIVE phase qubit
q_k(theta)=(|0>+exp(2pi i k theta)|1>)/sqrt2 for theta=s/N.
Discard/reset data before acquiring another copy. Label replacement is an
UNCONDITIONAL ensemble coupling, not conditioning on no label errors.

For any known unit alpha mod N, first applying y->alpha*y mod N to source
data produces rho_(alpha*s): x is still uniform by bijectivity. Extend by
identity on invalid y>=N. Implement constant modular products with n
controlled modular additions of alpha*2^j mod N into a clean accumulator,
copy the result and reverse. Each addition has O(n) Boolean gates/wires
by ripple comparisons/carries/selectors and clean compute-swap-inverse.
To apply the unit permutation in place, compute its value, swap registers
and XOR its inverse value using alpha^(-1). This costs O(n^2) gates and
O(n) scratch, including invalid-domain handling. Constants/inverses are
computed classically by counted schoolbook arithmetic/Euclid. NOT/CNOT/
Toffoli have exact constant-size Clifford+T decompositions. There is no
unit-cost word multiplication or source inverse. The same construction
works for odd constant permutations modulo2^p in gradient-tools.md.

The reference model below uses perfect labels, an ideal gradient and exact
known phase corrections. Actual labels, gradient and rounded corrections
are compared additively at the end. Every REAL circuit is specified with
counted gates, finite attempts and the two caps.

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
q-bit conceptual strings or a tree of original labels. Initially tensor R
fresh phase qubits with independent uniform w-bit labels a_i. For each R-bit
index x compute b_x=sum_i a_i*x_i, ellSum_x=sum_i(a_i mod Ftarget)*x_i,
h_x=popcount(x) by counted classical loops. Here F=1,c_global=0. The R
original labels are released after forming this table; only its three
aggregates persist. The physical source suppliers are specified below and
every rejected source copy in them is charged.

To collimate two same-level vectors, form their product index (i,j), each
component R bits. This represents L^2 amplitudes but DOES NOT enumerate an
L^2 classical table. Let A_i and B_j denote their full phase labels and let
b<=b0 be the prescribed cancellable width; Mres=2^b<=L/16.

First compute y=(A_i+B_j) mod Mres into a b-bit zero register, using two
L-row literal equality/XOR lookups of the child low labels and a clean ripple
sum. Measure y, then uncompute the child-label lookup scratch from unchanged
i,j and reset the measured y register using its known classical outcome.
This projects onto a bucket; its ideal conditional amplitudes have equal
magnitudes. No index is measured. All gates and measurements are counted.

Construct a CLASSICAL descriptor of the right child, sorted by
(B_j mod Mres, original j) with the bottom-up merge algorithm below. For each
residue r store count[r] and start[r], its number and first position in this
sorted descriptor. These arrays have Mres<=L entries. Let sortedB[m] give
its original j and let within[j] be j's zero-based rank in its residue group.
Thus sortedB[start[r]+within[j]]=j when B_j mod Mres=r. This descriptor is
classical; the physical j register has NOT been sorted or measured.

After the measured y is known, for i=0,...,L-1 compute the CLASSICAL arrays

 c_i=count[(y-A_i) mod Mres],
 P_0=0, P_(i+1)=P_i+c_i, S_i=start[(y-A_i) mod Mres].

There are L+1 prefix entries and L counts/starts. Put M=P_L<=L^2. Prefix
endpoints and counts use2R+1 bits when needed, since M can equal L^2.
The outcome M=0 has zero probability on this bucket; define abort there to
make the classical program complete. NO array indexed by both quantum i and
unmeasured y is supplied: y has already been measured. This order is essential.

On the measured-bucket subspace compute the rank
z=P_i+within[j], with0<=z<M, in a fresh2R-bit register. This needs an L-row
lookup of P_i, an L-row lookup of within[j], ripple arithmetic, copy to z and
full reversal of the lookup/arithmetic scratch. Define the forward function
on other (i,j) by this sum modulo L^2, so its compute-XOR circuit is globally
unitary. Bucket membership implies B_j mod Mres=(y-A_i) mod Mres, so within[j]
is in[0,c_i). Thus z orders bucket pairs in ORIGINAL lexicographic (i,j) order.

The inverse rank function is computed with only L-row scans:
- Scan all L disjoint intervals[P_i,P_(i+1)). Compare their2R+1-bit constant
  endpoints with zero-extended z using reused ripple scratch. If the interval
  contains z, XOR constant i into a clean R-bit index. Empty intervals match
  nothing. For z<M there is exactly one match. Outside that range use the
  all-zero default; the same circuit still computes a total Boolean function.
- Given this computed i, use an L-row lookup of P_i,S_i and form
  m=S_i+(z-P_i). On valid z, m is in[0,L) and sortedB[m] is the original j.
  An L-row lookup returns that j. For invalid arguments use modular arithmetic
  on2R+1 bits and default-zero lookup outside[0,L), defining a total function.
- Compute these inverse i,j values in CLEAN scratch, XOR them into the OLD
  input i,j registers, and reverse all inverse-function scratch. This is not
  an assumption that old target registers were zero. On the bucket subspace
  inverse(forward(i,j))=(i,j), so the old inputs become zero and can be released.

Every lookup scans its complete classical row list with equality-prefix,
controlled XOR and inverse-prefix gates. The interval inverse scans L rows,
not a quantum-addressed binary search. It uses O(R) scratch, reused per row;
no per-row flag or Boolean history accumulates. Forward and inverse circuits
are unitary on their complete encoded domains and work for superposed indexes
and entangled outside systems. Their gate/controller count is O(L poly(n));
there is no QRAM, inverse source or free coherent memory access.

Now measure the high R bits of z (the chunk number), keeping its low R bits
as the new index. A chunk with L entries is retained. The final short chunk,
if any, is discarded and BOTH child vectors are regenerated from fresh source
copies. The JOINT (bucket,chunk) instrument is exactly the partition into
consecutive length-L blocks in each lexicographic bucket. In the ideal
uniform product, bucket y has probability M_y/L^2 and its short weight is
(M_y mod L)/M_y. Therefore total partial probability BEFORE conditioning on y is

 sum_y (M_y mod L)/L^2 <=Mres*(L-1)/L^2<=1/16.

This bound holds for EVERY pair of child tables. It is NOT a 1/16 bound
conditional on y: a small bucket can consist entirely of a short chunk.
The expected-attempt analysis below conditions before this measurement.

For a full measured chunk, enumerate its L consecutive ranks CLASSICALLY.
For each z, binary search the nondecreasing P array for the last prefix<=z;
zero-length intervals are skipped, since P_L=M>z. This yields its unique i,
then j=sortedB[S_i+z-P_i]. These are ordinary classical addressed reads with
all bit/index costs charged, not quantum-addressed searches. At most O(R)
steps per rank suffice. Form the L output aggregate rows by

 F_new=F*2^b, b_new=(A_i+B_j-y)/2^b,
 ellSum_new=ellSum_left_i+ellSum_right_j, h_new=h_left_i+h_right_j.

Only O(L) rows are generated. The removed exp(2pi i F*y*theta) is common;
c_new=c_left+c_right+F*y proves the aggregate identities. The kept low rank
bits are not measured. Distinct conceptual incidences concatenate on disjoint
source coordinates. No original-label or incidence list is needed.

All classical sorting uses explicit bottom-up merges: start runs of length1,
merge adjacent runs into a second array by the stated lexicographic key,
take original-index ties first, and double the run length each pass. End/run
tests handle incomplete final runs. For Mrows<=L+1 there are O(R) passes,
O(Mrows) comparisons/copies per pass and two O(Mrows) buffers. Root sorting
uses its low-sum/weight key and original root index. No high phase-label bits
select or order buckets. Every comparison, copy, table read, address and gate
emission is charged. Old child tables, descriptors and scratch are released
when no longer needed; partial failures release both child states before retry.

For target width w use D_w=ceil((w-1)/b0) levels, cancelling b0 bits each
except the final remainder. Total cancellation is w-1. If w=1 there are no
levels. Every surviving tree contains EXACTLY q_w=R*2^D_w original phase
controls, at most q; this is a PROOF count, not an allocated incidence register.
Depth-first traversal stores one R-qubit sibling per level. Release failed
states/tables before retrying; all failed acquisitions and attempts are counted.

Decisions, bucket ordering and trimming use only INITIAL label bits below
w-1. Although the full b values are stored, they never select or order pairs
except through the prescribed cancellable low residues. Each total cancelled
prefix is at most w-1, so unused top bits cannot enter those residues after
normalization. ellSum and h use only low parts and original index bits.

## A final pair with difference exactly plus or minus 2^(w-1)

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
(floor(ellSum/F),h), using the same explicit merge algorithm with original
root index as the last tie key. There are at most(q+1)^2 keys: ellSum<qF
and h in[0,q]. Pair consecutive original indices in each key, discarding
singletons by the same reversible reindex/measurement construction with
block size2. All these decisions still omit top bits. Paired probability
is at least1-(q+1)^2/L>=3/4 by the inequalities below.

For a selected pair x,y, equal key and common remainder imply equal EXACT
low sums, and equal h implies equal Hamming weight. Their conceptual Hamming
distance T is even and at least2; y-x has T/2 plus and T/2 minus coefficients.
Consequently the ORIGINAL full-label difference divided by F is
W=sum_i t_i(y_i-x_i), distributed as Bin(T,1/2)-T/2. Hence

 Pr(W=+1 or-1)=2*binom(T,T/2+1)/2^T>=1/(T+1)>=1/(q+1).

The central binomial coefficient is the maximum of T+1 terms summing2^T,
and the neighboring ratio T/(T+2)>=1/2 proves this bound. The controller
need not compute x,y or T. By the root invariant it computes W EXACTLY as
b_y-b_x from the two stored O(n)-bit phase labels, ONLY AFTER selecting and
measuring that pair. If W=+/-1 keep its qubit, applying X for the negative
sign; otherwise discard the whole root and regenerate. Root success is at
least1/[4(q+1)] conservatively. Every accepted history leaves precisely
q_F(theta)=(|0>+exp(2pi i F theta)|1>)/sqrt2 up to a global scalar, so
forgetting metadata does not dephase it. This literal frequency works for
arbitrary real theta, rather than only an odd multiple for power-of-two parity.

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
vartheta=f*(s mod M)/M modulo1. The same bounded-variable proof gives total
mean/decoder failure<1/1024 for the stated m_est. Error after unwrapping
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
In particular the final accept test depends on uniform classical target labels,
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

Let EQ_0=2R; a leaf needs R accepted labels, each taking at most2 acquisitions
in expectation. For collimation levels, every attempt succeeds with probability
at least15/16 conditional on any tables/history. Fresh children and discarded
copies are charged. Thus EQ_i<=A0*EQ_(i-1), A0=32/15. Root attempts have
success at least1/[4(q+1)] including the final-pair selection, so expected
source acquisitions over all calls are at most
Qstar=C*4(q+1)*EQ_D=C*8R(q+1)A0^D.
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

The explicit nonrecursive BASIC-step allowance is G=2^100 n^10 L per
internal attempt/final processing, per expected leaf, and for the one-time
bounded gradient preparation. Full phase labels/low sums have at most
n+ceil(log2(q+1))+1<=3n bits; weights, all aggregate and descriptor fields,
and2R+1-bit interval endpoints have O(n) bits. Each record fits2^10 n bits.
No L^2 pair table, q-bit incidence list or original-label graph is allocated.

Pair processing scans the two L-row child tables, sorts at most L right
records, initializes at most L residue counters, builds L+1 prefix endpoints,
and emits a constant number of L-row quantum lookup/interval networks.
Enumerating the L accepted output ranks takes O(R) CLASSICAL prefix-search
steps each. Root keys/sorting/pair lookups also have only L rows; leaf subset
tables have L rows. Each merge needs O(R) passes of O(L) record operations.
Releasing the entire depth-first path touches at most O(n L) rows. The total
number of these record operations is less than2^10 n^2 L.

Each record operation costs at most2^20 n^4 core steps, including bitwise
controllers. Ripple arithmetic/comparison/copy uses fewer than2^10 gates per
processed bit. Index/stride/address operands have O(n) bits, with at most
quadratic schoolbook bit cost; this includes a classical binary-search step.
Each quantum interval or lookup row emits O(n) gates with generated addresses,
constant-size controls, scratch clearing and full inverse work. No quantum
binary search or free array access is hidden. Consequently all table, prefix,
merge, lookup and frame work fits2^30 n^6 L basic steps.

Each source extraction has at most2(n+5)*2^24 H tests, H<=2n. Translation
and its controller cost at most2^20 n^4 core steps per test. Expected leaf
filtering/acquisition and bounded gradient preparation with p<=2n and at most
2n attempts each fit2^80 n^8 steps. Fixed rational direction tables are
separately generated before the clock and charged. Their sum with the table
estimate is below G=2^100 n^10 L. Only the ideal rejection loops are counted
in expectation here; the actual two counters stop every execution branch.
The full global address/clock overhead is applied below after these core bit
steps, including generation and inverse work, have been counted.

Consequently E_0=G, E_i=(16/15)(2E_(i-1)+G) bound expected core steps of
one vector, and Wstar=G+C*4(q+1)*(E_D+G) bounds the entire uncapped reference.
All costs are uniform over phase values: computational partitions see only
uniform magnitudes, even if a preceding phase estimate was wrong.
B=ceil1024Wstar gives clock-abort probability<=1/1024 by Markov. No per-node
polynomial retry cap is multiplied through the tree. Both caps are computable
rational formulas, not unproved expected-only resource claims.

## Uniform charged resources and exact growth indices

For u>=64, b0=2u-4>=(31/16)u, so D<=16u/31+1. Thus
q<=4u*2^(16u/31), 4^D<=4*2^(32u/31).
A0=32/15<2^(9/8), checked by raising to the eighth power, gives
A0^D<=4*2^(18u/31). Also q+1<=8u*2^(16u/31), hence
4(q+1)^2<=256u^2*2^(32u/31)<=L=2^(2u).
For the last inequality, log2 u<=u/8 for u>=64: on[2^k,2^(k+1)) with k>=6,
log2 u<k+1<=2^(k-3)<=u/8, and the middle inequality follows by induction.
Then8+2log2 u<=8+u/4<=30u/31 for u>=64, which proves the claim.
Thus root paired mass is at least3/4 on every large input, not inferred from
finite parameter tests. In particular log2(q+1)<=u, so every stored word
length used above remains O(n).
m_est<=2^25 n and C<=2^28 n^2. With u^2<=2n the source formula implies
Qcap<=2^52 n^3*2^((34/31)u). This gives
H<=n+76+4log2 n+2u<=2n and p<=n+94+3log2 n+2u<=2n.
Both inequalities hold for n>=4096 by u<=sqrt n+1 and increasing linear
margin over the logarithmic/square-root terms.
G=2^100 n^10*2^(2u). The exact affine E recurrence has closed form
E_D=G*(33 A0^D-16)/17<=2G A0^D, by direct substitution including D=0.
Since q+1=O(u 2^(16u/31)), C=O(n^2), and u=O(sqrt n),
B=O(n^(25/2) 2^((96/31)u)), with96/31=2+34/31.
All these inner exponent coefficients are explicit; no O() inside an exponent
is replaced by1 or guessed from an index.

Classical memory contains active descriptor/sort/lookup tables of at most O(L)
records each with O(n) bits, a constant number of merge buffers, and at most
D sibling tables/frames. Even bounding every path frame by O(L) rows gives
O(n^2 L) bits including all copies, metadata, counters and scratch.
No original q-label list, q-bit incidence array or failed history accumulates.
The largest address length is O(u+log n), and source/work counters have that
same order of bits. After this allocation is established, each core step
including monitor updates, source charge n+1, all indexed access and generated
gate/wire addressing is conservatively charged at most O(n^4) work. A clock
update uses O(log B) bit steps with their full addresses and is included.
Thus every branch, including abort cleanup and all setup, has
T=O(n^(33/2) 2^((96/31)u)). Cleanup scans at most the smaller classical-memory
envelope; deterministic parameter setup is polynomial plus fixed constants.
Ceil u differs from sqrt n by<1, affecting only absolute outside factors.

Quantum space is one R-bit sibling per recursion level, old pair indexes, a2R-bit rank register and
O(R) inverse/equality/lookup scratch, leaf controls, one n-bit data/extraction system,
and the p-bit gradient with O(n) arithmetic scratch. R(D+1)=O(n), p<=2n;
stages reuse work. Conceptual incidences are NOT physical quantum or classical
registers. Thus S_Q=O(n). Classical space is O(n^2 2^(2sqrt n)); Qcap fits
O(n^3 2^((34/31)sqrt n)). The fixed finite branch was covered above.
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
