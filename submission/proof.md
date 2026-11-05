# COL1: bounded depth-first collimation with literal-frequency output

## Theorem, exact configuration and provenance

For every N>=2 and s in Z/NZ let n=ceil(log2 N). COL1 recovers the entire
secret with unconditional probability>2/3 from independent ideal source copies.
The SAME program has these bounds on EVERY branch:

 T=O(n^8 2^(161sqrt n)), S_C=O(n^2 2^((33/2)sqrt n)),
 S_Q=O(n) qubits, Q=O(n^3 2^(sqrt n)).

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

Set u=ceil(sqrt n), R=8u, L=2^R, b0=R-4, D=ceil((n-1)/b0), q=R*2^D.
Define A0=32/15, m_est=2^24(n+20+ceil(log2(n+5))),
C=2(n+5)m_est+n,
Qstar=C*8R(q+1) A0^D, Qcap=ceil(1024Qstar),
p=n+ceil(log2(Qcap+2))+40.
Finally define G=2^100(n+q+L^2)^10,
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
https://arxiv.org/pdf/1112.3333 . COL1 reproduces the needed argument and adds
literal-frequency selection and source-only all-moduli recovery below.
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

## Uniform phase vectors and literal table access

A phase vector of length L is
L^(-1/2)sum_(j=0)^(L-1) exp(2pi i F b_j theta)|j>,
with known integer table b and an irrelevant common global phase. Its index
requires R qubits, NOT L qubits. We also store classical binary incidence
vectors describing which original leaf control bits contribute to each entry.
No amplitudes are stored. Initially a leaf tensors R fresh phase qubits with
known independent labels a_i uniform in[0,2^w), w<=n. Its index is the R-bit
source-control string, b_x=sum_i a_i x_i, F=1, and incidence is x itself.
The two physical ways to supply these qubits for general N appear below.
Every rejected source copy in those suppliers is charged.

To collimate two same-level vectors, form their product with L^2 index pairs.
For a prescribed b<=b0, partition pairs by (b_i+c_j) mod2^b, and within each
bucket use ORIGINAL lexicographic (i,j) order only. Divide each bucket into
blocks of L plus one possible short block. Enumerate the whole table
classically. Compute the injection (i,j)->(blockID,rank) reversibly by literal
sequential equality/XOR lookup over all L^2 entries, with a clean output of
2R+1 bits. Use a second lookup of the inverse (default zero outside the
image) to XOR the old 2R-bit input to zero. Both are full reversible compute-
XOR circuits, even outside their initialized image. There are fewer than2L
blocks, so R+1 block bits suffice; rank uses R bits. No QRAM is supplied.
Each lookup compares an O(R)-bit quantum index with a classical constant,
computes an equality prefix with O(R) scratch, XORs output bits and reverses
that prefix. It has O(L^2 poly(R)) gates and O(R) quantum scratch. All table
reads, gate generation, indices and addresses are charged below.

Measure blockID. A full block leaves a length-L uniform phase vector;
a short block is discarded and BOTH children are generated afresh.
Total short-block mass is at most2^b(L-1)/L^2<=1/16, for ANY input tables.
This deterministic counting argument assumes no random or independent table
entries. Every attempt/measurement/discard is counted. On full block with
bucket remainder y, put F_new=F*2^b and b_new=(b_i+c_j-y)/2^b.
The removed exp(2pi i F*y*theta) is common to the whole selected state.
Old tables/registers can be discarded after the exact reindexing; no relative
phase is lost. Classical incidences concatenate, with the left/right source
coordinates kept distinct. The global-offset identity
sum(original a_i*x_i)=F*b_x+c_global
is maintained exactly. Store original leaf labels for the final grouping.

For a target width w use D_w=ceil((w-1)/b0) levels, each cancelling b0 low
bits except the last remainder, so total cancellation is w-1. If w=1 there
are no collimation levels. Every surviving tree has EXACTLY R*2^D_w original
phase qubits, at most q. A depth-first traversal stores one R-qubit sibling
per level. On every failure release old tables and quantum work before retry.

IMPORTANT: decisions, bucket order and trimming never use high/middle label
values. Computing full values for storage is harmless; they do not select
pairs or order indices. At any stage the low bits being measured correspond
only to INITIAL bits below w-1. This rule is essential for the next proof.

## A final pair with difference exactly plus or minus 2^(w-1)

Set F=2^(w-1). Write original accepted labels a_i=ell_i+F*t_i, ell_i<F,
where t_i are independent fair bits. Every earlier choice uses only ell_i
and computational indices, so the current tree's unused t_i remain independent
fair bits when conditioning on those choices, NOT on the full known label
transcript. Computational partition probabilities are subset sizes and are
independent of all phases/top bits. Earlier failed root attempts use fresh
source labels and do not change this fact for the current attempt.

Root incidences x are distinct binary strings on q_w=R*2^D_w<=q coordinates.
All initial sums have a common residue modulo F; their low-part sums
sum ell_i*x_i consequently have the same residue too. Group root entries by
(floor(sum ell_i*x_i/F), Hammingweight(x)). There are at most(q+1)^2 keys.
Pair consecutive ORIGINAL indices within each key; a singleton is discarded
by the same reversible reindex/partial-measurement construction (now block
size2). All these choices still omit top bits. Paired probability is at least
1-(q+1)^2/L>=3/4, by the parameter inequalities below.

For a selected pair x,y, equal key gives equal low sums and equal Hamming
weights. Let T be their Hamming distance. They are distinct, so T>=2 is even,
and the numbers of +1 and-1 in y-x are each T/2. The ORIGINAL label difference
is F*W, where W=sum_i t_i(y_i-x_i) has the law Bin(T,1/2)-T/2. Hence

 Pr(W=+1 or-1)=2*binom(T,T/2+1)/2^T>=1/(T+1)>=1/(q+1).

The central binomial coefficient is the maximum of T+1 terms summing2^T,
and the neighboring ratio is T/(T+2)>=1/2, proving the inequality.
Only AFTER selecting/measuring this pair inspect FULL labels to determine W.
If W=+/-1 retain its one-qubit phase state, apply X for the negative sign,
and return q_F(theta). Otherwise discard the whole root and try again.
Root success per attempt is at least1/[4(q+1)] conservatively. Every accepted
history leaves EXACTLY the same q_F density; all history-dependent scalars
are global. Thus deleting the old labels/history adds no dephasing.
This produces a LITERAL frequency F for arbitrary real theta, not merely
an odd multiple suitable only for a power-of-two parity problem.

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

The following deliberately loose BASIC-step bound covers nonrecursive work:
G=2^100(n+q+L^2)^10 per internal attempt/final processing, per expected leaf,
and for the one-time bounded gradient preparation. Literal implementations:
- Enumerate all L^2 pairs, copy n-bit labels and q-bit incidence strings, sum
  by ripple bits, and bubble-sort by bucket then original indices. At most
  (L^2)^2 comparisons/swaps, with polynomial bit work on those record sizes.
- Compile both equality/XOR lookup networks by looping through their L^2
  classical entries; each has O(R)-bit equality, O(R) outputs and O(R) scratch.
  Generate every wire address by ordinary binary arithmetic; stream gates.
- Leaf subset tables enumerate L R-bit strings and use schoolbook bit sums.
  Final low-sum/Hamming keys scan q stored labels per entry; sorting/pairing
  and both inverse lookups have the same polynomial bounds.
- Every source extraction has at most2(n+5)*2^24 H tests with H<=2n below.
  Ripple translation and a straightforward bitwise controller cost at most
  2^20 n^4 basic steps per test; all means/decoding are smaller. Constant
  source permutations and inverses are also polynomial. Expected leaf cost
  is therefore at most2^80 n^8 plus the table loops. Gradient preparation
  with p<=2n, at most2n attempts and the same elementary routines also fits
  2^80 n^8. Fixed direction constants are generated before starting this clock.
These literal loops have degree at most ten in n+q+L^2 and coefficients below
2^100: ordinary NOT/CNOT/Toffoli ripple/equality templates may each use fewer
than2^10 fixed gates per bit, and their bitwise generation/index arithmetic
is included in the n^4 allowance. No large-word, QRAM, parallel or advice
operation is hidden in G. It is intentionally a much larger bound than the
actual linear lookup cost. A leaf's unbounded rejection loop is charged in
EXPECTATION here (<=2R acquisitions); actual loops are stopped by both caps.

Consequently E_0=G, E_i=(16/15)(2E_(i-1)+G) bound expected core steps of
one vector, and Wstar=G+C*4(q+1)*(E_D+G) bounds the entire uncapped reference.
All costs are uniform over phase values: computational partitions see only
uniform magnitudes, even if a preceding phase estimate was wrong.
B=ceil1024Wstar gives clock-abort probability<=1/1024 by Markov. No per-node
polynomial retry cap is multiplied through the tree. Both caps are computable
rational formulas, not unproved expected-only resource claims.

## Uniform charged resources and exact growth indices

For u>=64, b0>=7u, so D<=u/7+1 and
q=8u*2^D<=16u*2^(u/7)<=2^(u/2).
The last inequality follows from4+log2 u<=5u/14 at64 and its increasing margin.
Also4(q+1)^2<=L=2^(8u), proving final paired mass>=3/4. These inequalities
hold for all n>=4096, not just empirical lengths. In particular4^D<=2^(u/2).
m_est<=2^25 n and C<=2^28 n^2. Hence
Qcap<=2^46 n^3*2^u. This gives H<=n+70+4log2 n+u<=2n and
p<=n+88+3log2 n+u<=2n, as used in the basic-step estimates.
Since n,q<=L^2, G<=2^116*2^(160u). Summing the E recurrence yields
E_D<=(D+1)4^D G. Thus B=O(n^4 2^(161u)).
All these inner exponent coefficients are explicit; no O() inside an exponent
is replaced by1 or guessed from an index.

Classical memory contains tables of at most L^2 records of O(n+q+R) bits,
a constant number of sorting/lookup copies, depth-first sibling tables,
original source labels for the surviving tree, all counters and scratch.
There are O(n^2 L^2(q+n)) stored bits including all copies/path tables.
Since q+n<=2^(u/2+1), this gives O(n^2 2^((33/2)u)) including every
initialization and temporary array.
No failed table or discarded leaf history is accumulated. The largest
address length is O(u+log n); clock/source counters also have O(u+log n) bits.
Each core step, including monitor updates, source charge n+1, generation,
all indexed accesses and gate-address bits, is conservatively charged at
most O(n^4) work. A basic clock update costs O(log B) Boolean steps, each
with its full address charge, and is explicitly in this allowance.
Thus all branches, including abort cleanup, have
T=O(n^8 2^(161u))+deterministic polynomial setup and fixed constants.
Cleanup can scan classical memory if required; its (33/2)u envelope is smaller.
This proves the stated supported O(n^8 2^(161sqrt n)) bound. Ceil u differs
from sqrt n by<1, affecting only absolute outside factors.

Quantum space is one R-bit sibling per recursion level, two active index
registers and O(R) lookup/equality scratch, leaf source controls and one
n-bit data/extraction system, and one p-bit gradient with O(n) arithmetic
scratch. R(D+1)=O(n), p<=2n; stages reuse work. Incidence strings and lookup
tables are CLASSICAL, not quantum. Hence S_Q=O(n), including all input and
ancillas. Classical memory fits the supported n^2 2^((33/2)sqrt n), and the
literal Qcap bound fits n^3 2^(sqrt n). The finite branch was covered above. The coefficient in each exponential
is explicit; replacing ceil(sqrt n) by sqrt n changes only an outside constant.
All four envelopes are simultaneous worst-case branch guarantees.

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
