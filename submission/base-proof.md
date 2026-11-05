This is the clean per-invocation lemma A for COLR2. All counters,
precision parameters and caps below are per invocation; its canonical zero
count law describes A alone, not the wrapper in proof.md.

# COL3: bounded depth-first collimation with literal-frequency output

## Theorem, exact configuration and provenance

For every N>=2 and s in Z/NZ let n=ceil(log2 N). COL3 recovers the entire
secret with unconditional probability>2/3 from independent ideal source copies.
The SAME program has these bounds on EVERY branch:

 T=O(n^(33/2) 2^((538/63)sqrt n)), S_C=O(n^2 2^(8sqrt n)),
 S_Q=O(n) qubits, Q=O(n^3 2^((34/63)sqrt n)).

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

Set u=ceil(sqrt n), R=4u, L=2^R, b0=R-4, D=ceil((n-1)/b0), q=R*2^D.
Define A0=32/15, m_est=2^24(n+20+ceil(log2(n+5))),
C=2(n+5)m_est+n,
Qstar=C*8R(q+1) A0^D, Qcap=ceil(1024Qstar),
p=n+ceil(log2(Qcap+2))+40.
Finally define G=2^100 n^10 L^2,
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
https://arxiv.org/pdf/1112.3333 . COL3 reproduces the needed argument and adds
literal-frequency selection and source-only all-moduli recovery below.
COL3 materially builds on COL2 submission d543ab39-1eb4-4a37-b599-93be16274b9b,
which in turn changes COL1 b01d40e7-f315-422f-a2eb-9b87148fe864 from R=8u
to R=4u. COL3 keeps R=4u but replaces stored incidence vectors with aggregate
metadata, replaces quadratic-pass sorting with explicit bottom-up merges,
and reduces the literal work cutoff using the bit-loop count below. Source
caps and all-moduli recovery remain specified, with a tighter source envelope.
No prior verdict is a correctness premise; all arguments are reproduced.
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

To collimate two same-level length-L vectors, enumerate all L^2 pairs (i,j).
For prescribed b<=b0, the bucket is (b_i+c_j) mod2^b. Order each bucket by
ORIGINAL local indices (i,j) only, not by full label values. Divide it into
blocks of L and at most one short block. All table sorting uses the following
ordinary classical bottom-up merge algorithm. Start sorted runs of length1;
merge adjacent runs into a second array by comparing the stated lexicographic
key and taking the smaller original-index tie first. Double run length each
pass until it covers the array. Each pass copies/compares O(M) records for
an array of M<=L^2 entries; at most2R+1 passes suffice. End-of-run tests
handle partial last runs. Store two O(M) arrays, swap their roles each pass,
and release the obsolete one. Comparisons, record copies, counters, keys,
wire/address generation and every bit read/write are charged. There is no
unit-cost word operation. Bucket sorting never inspects high label bits.

Compute the injection (i,j)->(blockID,rank) reversibly by a literal sequential
equality/XOR lookup through all L^2 rows, with a clean output of2R+1 bits.
A second lookup of the inverse, default zero outside its image, XORs the
old2R-bit input to zero. Both are reversible compute-XOR circuits even on
uninitialized inputs. There are fewer than2L blocks: number<=L+2^b<2L.
BlockID therefore takes R+1 bits, rank R bits. For each row compare an
O(R)-bit quantum index with its classical constant, compute an equality
prefix with O(R) scratch, XOR output bits and reverse the prefix. Each
lookup has O(L^2 poly(R)) gates and O(R) quantum scratch. The controller
streams all gates and table bits, paying addresses; no QRAM is supplied.

Measure blockID. A full block leaves a length-L uniform phase vector; a
short block is discarded and BOTH children are generated afresh. Total
short-block mass is at most2^b(L-1)/L^2<=1/16 for ANY input tables in the
ideal phase-vector computation, without random-table-entry assumptions.
For the measured bucket remainder y set

 F_new=F*2^b, b_new=(b_i+c_j-y)/2^b,
 ellSum_new=ellSum_left_i+ellSum_right_j, h_new=h_left_i+h_right_j.

The removed phase exp(2pi i F*y*theta) is common. The aggregate identities
follow by adding the children's identities; c_new=c_left+c_right+F*y.
No conceptual incidence string or original-label list is needed to compute
these updates. Child source coordinates are disjoint, so their conceptual
incidences concatenate and remain distinct. Old tables/registers are released
when no longer needed. Measurement selects the appropriate L aggregate rows
classically; it does not measure the quantum rank. Only these rows are used
by later literal lookups.

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

The following explicit BASIC-step bound covers all nonrecursive work:
G=2^100 n^10 L^2 per internal attempt/final processing, per expected leaf,
and for the one-time bounded gradient preparation.

Each full phase label or low-part sum is a sum of at most q original n-bit
labels, so has at most n+ceil(log2(q+1))+1<=3n bits. Hamming weights have
O(log q)<=O(n) bits. A record stores a constant number of these integers
and O(R)-bit indexes/block/rank fields, hence at most2^10 n bits. It stores
NO q-bit incidence string, original-label array or recursive pointer graph.
All aggregates update by additions of O(n)-bit integers. Leaf tables use
only R<=n original labels while being formed. Root keys use stored aggregate
integers, not a fresh scan of the conceptual q original coordinates.

Enumerating/initializing the pair tables uses O(L^2) whole-record operations.
Each merge pass uses O(L^2) record comparisons/copies, and there are O(R)
passes. Assigning buckets/blocks and emitting both inverse lookup networks
scan all L^2 rows. Final-key construction, sorting and pairing have only L
rows. A release of the full depth-first path touches at most O(n L^2) rows.
There are fewer than2^10 n^2 L^2 whole-record operations in total, including
end/run tests, metadata and cleanup, with plenty of slack for all loops.

Each such operation takes at most2^20 n^4 core steps, including ordinary
bitwise controllers. O(n)-bit addition/comparison/copy uses fewer than2^10
fixed gates per processed bit. Classical index/stride/wire-address operands
have O(n) bits; even schoolbook index products cost only quadratic bit work.
Lookup-row compilation emits O(R) elementary gates with fully generated wire
addresses and equality scratch/inverses; this too fits the same allowance.
The fourth power covers these controller steps and their own core bit reads.
Thus table, sort, lookup and frame work is at most2^30 n^6 L^2 basic steps.
This counts generation and sequential access, not merely quantum depth.

Every source extraction has at most2(n+5)*2^24 H tests with H<=2n. Ripple
translation and a straightforward bitwise controller cost at most2^20 n^4
core steps per test; means/decoding are smaller. A leaf needs at most2R
acquisitions in expectation including filtering. Expected leaf extraction
and bounded gradient preparation (p<=2n, at most2n attempts) each fit
2^80 n^8 basic steps using these same elementary routines. Fixed rational
direction tables are generated before the clock and separately charged.
The sum of these helper and table estimates is below G=2^100 n^10 L^2.
A leaf's unbounded rejection loop is charged in EXPECTATION here; both
actual counters stop every run. No large-word, QRAM, parallel, advice or
inverse-source operation is hidden in G. The fully charged address and
clock-monitor overhead is applied below after these core steps are counted.

Consequently E_0=G, E_i=(16/15)(2E_(i-1)+G) bound expected core steps of
one vector, and Wstar=G+C*4(q+1)*(E_D+G) bounds the entire uncapped reference.
All costs are uniform over phase values: computational partitions see only
uniform magnitudes, even if a preceding phase estimate was wrong.
B=ceil1024Wstar gives clock-abort probability<=1/1024 by Markov. No per-node
polynomial retry cap is multiplied through the tree. Both caps are computable
rational formulas, not unproved expected-only resource claims.

## Uniform charged resources and exact growth indices

For u>=64, b0=4u-4>=(63/16)u, so D<=16u/63+1. Thus
q<=8u*2^(16u/63), 4^D<=4*2^(32u/63).
A0=32/15<2^(9/8), checked by raising to the eighth power, gives
A0^D<=4*2^(18u/63). For the final paired-mass estimate we can also use the
looser b0>=3u, D<=u/3+1, q<=8u*2^(u/3)<=2^(u/2).
The last inequality follows from3+log2 u<=u/6 at64 and its increasing margin.
Consequently4(q+1)^2<=L=2^(4u), proving paired mass>=3/4 for all n>=4096.
m_est<=2^25 n and C<=2^28 n^2. Using u^2<=2n, the sharper bounds imply
Qcap<=2^52 n^3*2^((34/63)u). This gives
H<=n+76+4log2 n+u<=2n and p<=n+94+3log2 n+u<=2n.
G=2^100 n^10*2^(8u). The exact affine E recurrence has the closed form
E_D=G*(33 A0^D-16)/17<=2G A0^D. Substitution is also a direct induction,
including D=0. Since q+1=O(u 2^(16u/63)), C=O(n^2), and u=O(sqrt n),
the explicit B formula satisfies
B=O(n^(25/2) 2^((538/63)u)), with538/63=8+34/63.
All these inner exponent coefficients are explicit; no O() inside an exponent
is replaced by1 or guessed from an index.

Classical memory contains active pair/sort/lookup tables of at most L^2
records each with O(n) bits, a constant number of merge buffers, and at most
D sibling tables/frames. Even bounding every path frame by L^2 rows gives
O(n^2 L^2) bits including all copies, metadata, counters and scratch.
No original q-label list, q-bit incidence array or failed history accumulates.
The largest address length is O(u+log n), and source/work counters have that
same order of bits. After this allocation is established, each core step
including monitor updates, source charge n+1, all indexed access and generated
gate/wire addressing is conservatively charged at most O(n^4) work. A clock
update uses O(log B) bit steps with their full addresses and is included.
Thus every branch, including abort cleanup and all setup, has
T=O(n^(33/2) 2^((538/63)u)). Cleanup scans at most the smaller classical-memory
envelope; deterministic parameter setup is polynomial plus fixed constants.
Ceil u differs from sqrt n by<1, affecting only absolute outside factors.

Quantum space is one R-bit sibling per recursion level, two active indexes,
O(R) equality/lookup scratch, leaf controls, one n-bit data/extraction system,
and the p-bit gradient with O(n) arithmetic scratch. R(D+1)=O(n), p<=2n;
stages reuse work. Conceptual incidences are NOT physical quantum or classical
registers. Thus S_Q=O(n). Classical space is O(n^2 2^(8sqrt n)); Qcap fits
O(n^3 2^((34/63)sqrt n)). The fixed finite branch was covered above.
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
