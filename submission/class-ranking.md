# R4: complete dyadic phase-class instrument

## 1. Interface, provenance and finite circuits

Input: n>=256, 1<=b<=ceil(n/3), a known p, k independent phase
qubits with known signed labels a_j divisible by 2^p. Let
c_j=(a_j/2^p) mod2^b. The input pure phase-index state is

 2^(-k/2) sum_y exp(i theta sum_j a_j y_j)|y>,

where theta is the common phase frequency. All operations below depend
only on n,b,c and measured index functions, never on theta or unused
high label blocks. A successful output has exact label
sum_j (y1_j-y0_j)a_j for two DISTINCT bit strings with equal low sums
mod2^b. The relative phase is consequently correct and the label is
divisible by 2^(p+b). Every returned pair is correct for EVERY input
label tuple; only the success lower bound uses fresh independent uniform
c_j in [0,2^b). This distinction matters.

Let ell=ceil(log2(n+2)), C=4096. For b<12ell+96 use LOW with k=b+6.
Otherwise use HIGH with k=ceil(4(b+ell)/3)+128. Put m=ceil(k/4),
L=2^m, r=m+64, sigma=2^r. All are explicitly computed integers.
For n>=256 all index, sum, address, offset and count words below have
O(n) bits; k<=20(n+1) is a generous uniform bound. Functions on invalid
encodings use zero defaults and valid flags, with division denominator
replaced by 1 unless positive. Loop bounds depend on n,b,k, not success.

Conceptual four-block modular filtering and canonical dictionaries are
credited to Chukhin/Kulikov/Levitskii/Mihajlin, arXiv:2608.07309v1,
Sections 3.1-3.3, https://arxiv.org/html/2608.07309v1 . We supply a
complete different phase-class instrument, not that paper's QRAQM
algorithm or runtime theorem. R3 supplies the surrounding schedule
and CQ storage method, as precisely credited in proof.md Section 1.
No prime sampling, Grover search, random subset, quantum walk, QRAM,
claw-finding oracle or source-state preparation inverse is used here.

## 2. LOW: deterministic streamed fiber enumeration

Compute f(y)=sum c_j y_j mod2^b reversibly, measure e=f(y), and
uncompute its register using y. The original index is a flat phase
superposition on the fiber F_e. Enumerate all k-bit strings in lexicographic
order with an explicit k-bit counter, computing f each time with O(n)-bit
integer arithmetic. Retain the first C distinct solutions; stop as soon
as C are retained or the finite 2^k counter ends. The retained list is
ordinary classical memory of C*k=O(n) bits. This is deterministic and
bounded even for pathological labels. No discovery oracle is invoked.

Reversibly compute the index of y in this at-most-C list, with an extra
NOTFOUND flag. Measure that flag; on NOTFOUND discard the whole input.
On FOUND, compute the listed string from the index and XOR it into y,
uncomputing temporary comparisons. Measure floor(index/2). Discard an
unpaired last index. Otherwise the low index bit is the exact output
phase, and its two listed strings give its full signed difference label.
All comparisons, list scans and inverse functions are finite Boolean
circuits with defaults off the prepared support. They are unitary XOR
computations on the full space, not a promised partial permutation.

## 3. LOW: success and work

Before each fresh attempt c is independent uniform and y is uniform
because the phase amplitudes are flat. For any z!=y the incidence z-y
has a coefficient +/-1, so Pr[f(z)=f(y)]=2^-b. Consequently

 E |F_f(y)|=1+(2^k-1)2^-b<65.

Markov gives Pr[|F_f(y)|>C]<65/C. On all fibers of size <=C the
streamed list is complete. Dropping at most one unpaired string per
fiber loses mass <=2^b/2^k=1/64, unconditionally for each fixed c.
Thus LOW success >=1-65/4096-1/64=3967/4096>20/21. Larger fibers
may give additional success; no completeness claim for them is needed.
The source-family verified-pair proof applies exactly.

A candidate sum, all associated comparisons and bookkeeping cost at
most O((n+1)^8) charged bit/gate operations, including O(n)-bit address
and generated-circuit fees. No large array is needed. Since
b<12ell+96, 2^(b+6)<=2^102*2^(12ell)<=C0(n+2)^12, with an absolute
C0. LOW work is O((n+2)^20), including initialization and cleanup;
its workspace is polynomial (O(n^2) ordinary bits and O(n^2) qubits
are sufficient). The large outside constant is fixed, not advice.

## 4. HIGH: canonical projection and actual measured classes

Partition the k bit positions by position modulo 4 into blocks A1,...,A4.
Let Sigma_i(alpha) be the exact nonnegative sum of c_j on the selected
positions of block i, and tuple(alpha) its full k-bit incidence mask.
Every block has at most m positions and at most L assignments.
Enumerate ALL block-2 and block-4 assignments, including zero. Sort by
(Sigma_i mod sigma, Sigma_i, tuple). For each residue retain the first
entry, giving a canonical table R_i(v)=(sum,tuple,VALID). A missing
residue is INVALID, not the zero tuple. Tables have at most L rows;
all raw tables and padding are counted physical basis qubits.

For ORIGINAL y coherently compute each Sigma_2(y), Sigma_4(y) modulo
sigma. Retrieve its canonical entry by a complete LINEAR scan over the
corresponding table: for each classically known key compare to the
quantum residue, controlled-XOR the known sum/tuple into the answer,
and uncompute the comparison. At most one row matches. Compare the
answer's tuple with y restricted to that block (not the whole y), and
require VALID. Compute the conjunction pass, measure it, and on failure
discard all k phase inputs. On pass uncompute the predicate and all
lookup/sum scratch using y and the recorded outcome. This is the exact
projector onto canonical membership. No classical data measurement here
measures a coherent answer register.

On pass compute and measure the FULL integer

 T=Sigma_1(y)+Sigma_2(y)+Sigma_3(y)+Sigma_4(y),
 q=(Sigma_1(y)+Sigma_2(y)-T) mod sigma.

Uncompute the function registers against the original y after recording
these classical outcomes. This leaves a flat phase superposition over
exactly the canonical strings with this T,q. Full T is a function of
LOW c only: it does not reveal high parts of the signed a_j. Measuring
its low residue first would yield the same joint classes; we do not
need to do so. All measurement probabilities and selections are phase
independent. The original y is retained until rank computation below.

## 5. HIGH: complete Cartesian metadata without enumerating pairs

After T,q are classical, construct one F row for EVERY block-1 assignment
alpha, if the following table lookup is VALID:

 (s2,t2)=R2((q-(Sigma_1(alpha)-T)) mod sigma),
 F=(Sigma_1(alpha)-T+s2, tuple(alpha)|t2, tuple(alpha)).

Similarly for every block-3 assignment gamma construct a valid G row

 (s4,t4)=R4((-q-Sigma_3(gamma)) mod sigma),
 G=(-Sigma_3(gamma)-s4, tuple(gamma)|t4, tuple(gamma)).

Missing entries produce INVALID rows that never match. These table
lookups are CLASSICAL: use binary search in the sorted residue table,
with known addresses after each comparison is measured/read. No quantum
coherent-address facility is needed. F and G each have <=L rows; sort
valid rows by (exact signed first value, outer tuple). Merge the lists.
For each common exact value z keep its contiguous left and right row
ranges, lengths a_z,b_z>0 and offset

 o_z=sum_(z'<z) a_z' b_z'.

Store these fields in each row's metadata, together with its within-group
position. Also retain the group's interval endpoints. Let
K=sum_z a_z*b_z. Counts/products have O(k) bits since K<=L^2<=2^k.
A fat duplicate bucket uses row metadata, not enumeration of its pairs.
All arrays and group metadata occupy O(Ln) bits. Pad with explicit
INVALID records, never arithmetic-zero matches.

There is an EXACT bijection between the selected class of Section 4 and
all Cartesian pairs of rows of equal value in these arrays. A selected
y has unique outer assignments alpha=y|A1, gamma=y|A3. Canonicality
and q force its block-2 and block-4 tuples to be the retrieved values
above; full T forces F=G. Conversely F=G enforces exact total T, and
the lookup keys enforce q and the two canonical conditions. Disjoint
block positions give a unique full y. Neither direction assumes that
sums or residue buckets are unique. Thus this class has exactly K states.
K=0 cannot occur after the physical projection/measurement; if a malformed
classical control ever presents it, define an immediate bounded FAIL.

## 6. HIGH: reversible rank, inverse and output phase

For selected y retrieve its F row by the outer tuple y|A1 and G row by
y|A3, using explicit LINEAR known-row coherent scans. Retrieve their
group IDs, positions i,j, offset o and right count b_z. They belong to
the same group. Define

 rank(y)=o+i*b_z+j, 0<=rank<K.

Outside this condition use valid flag false and rank=0. Implement this
as an ordinary total Boolean function in a reversible XOR circuit,
uncomputing all local scratch after writing a k-bit rank register.
To invert rank v, scan all group intervals for the unique
 o<=v<o+a_z*b_z, compute (i,j)=divmod(v-o,b_z), then linearly retrieve
the corresponding left/right rows by group/position. The OR of their
full disjoint partial tuples is inverse(v). For invalid v use zero and
a false flag; safe division uses denominator 1. Uncompute all scratch.
These are O(L poly(n)) circuits, with O(n^2) reusable scratch.

Starting with original y and zero rank, compute rank(y), uncompute its
local scratch, and XOR inverse(rank) into original y. Uncompute inverse
scratch. ON THE PREPARED SUPPORT inverse(rank(y))=y, so original y is
now zero, unentangled, and may be released. Both XOR circuits are
unitary on their entire domains; no globally invertible rank promise
or free erasure has been assumed. The k-bit rank register carries the
original amplitudes in the bijective order 0,...,K-1.

Measure floor(rank/2). If the resulting pair index j has 2j+1>=K,
discard. Otherwise compute the two classical inverses y0=inverse(2j),
y1=inverse(2j+1) using the same metadata (ordinary known-address reads
are allowed for these CLASSICAL arguments). The low rank bit is

 (|0>+exp(i theta sum_l (y1_l-y0_l)a_l)|1>)/sqrt(2)

up to a global phase. Equal T implies sum_l (y1_l-y0_l)c_l=0 exactly,
so the full label is divisible by 2^(p+b). The strings differ; their
incidence has a unit coefficient +/-1. Discarding/resetting the now
classical tables cannot disturb this phase: conditional on the recorded
transcript they are known basis records. Nothing filters by a high label.

## 7. HIGH: fresh-law success, including all collisions and odd leftovers

This is an averaged fresh-attempt result, not pointwise success for fixed
adversarial c. Before fresh children are measured, their independent LOW
quotients c_j are uniform modulo 2^b, and original y is uniform.
Fix a block assignment y_i and another z_i. A differing bit supplies a
coefficient +/-1 in Sigma_i(z_i)-Sigma_i(y_i). Conditional on all other
weights, the probability this difference is 0 modulo 2^r is at most
2^-min(b,r): it is uniform modulo 2^r if r<=b, and at most one of the
2^b values can solve it if r>b. No independence between different
collisions is needed. A union bound for both full tables shows that the
probability original y is not canonical is <=2L*2^-min(b,r).

If r<=b this is exactly 2^-63. If r>b, use
m<=(b+ell)/3+33 and b>=12ell+96 to get

 1+m-b <=-2b/3+ell/3+34 <=-23ell/3-30 <=-30.

Thus canonical rejection has unconditional mass <=2^-30. This bound
also pays exact duplicates; no randomness heuristic for subset sums
or prime distribution is present. The coefficients are low parts of
fresh input labels, not fresh randomness requested from a source oracle.

For each fixed c, total T has at most (k+1)2^b possible integer values,
and q has at most 2^r values. Pairing a class discards at most ONE
original basis state per measured class, hence unconditional odd-last
mass (before canonical projection) is at most

 (k+1)2^(b+r-k).

This does not assume a typical class is large. Since
r<=k/4+65 and k>=4(b+ell)/3+128,
 k-b-r>=ell+31.
With k<=20(n+1) and 2^ell>=n+2 this mass is less than
20(n+1)/(n+2)*2^-31 <2^-26.
Therefore HIGH success >=1-2^-30-2^-26>20/21. Both success losses
are charged against original normalized mass; they are not conditional
probabilities incorrectly multiplied after postselection.

All successful paths give an exact pair phase even on labels for which
canonical projection is unlikely. Every test uses only c and index
functions. Conditional on its successful LOW transcript the incidence
on distinct child labels is nonzero with a unit coefficient; recursively
it has a unit coefficient on distinct original source leaves. Untouched
high blocks are independent uniform and cannot have influenced the
selection. The source's unused-block characteristic-function law follows
without conditioning on high-valued metadata. Retry transcripts also
use only low parts; no output is rejected for a zero high label.

## 8. Counted CQ memory, address semantics and exact reversible circuits

The large raw/canonical tables, F/G rows, sorting data and group metadata
are CLASSICAL data conditional on the controller transcript. Store them
in physical qubits in computational basis, with invariant

 sum_x p_x |x><x|_bank tensor rho_x^(active).

Correlations with active phase data are allowed. Measuring a known bank
cell returns its basis bit, and leaves the matching active rho_x. WRITE
resets that known cell to the requested bit after READ. Thus classical
processing of these records exactly simulates its ordinary bit algorithm,
without silently declaring basis storage free. The bank's full physical
width, initialization/reset, read/write gates, classical decisions,
address words and gate generation all count.

A row index and bit offset in these operations are CLASSICALLY KNOWN.
Generate that cell's numeric wire address directly using O(n)-bit
arithmetic; gate/address access charges O(n). Binary search and sorting
may choose their next address after a classical comparison/read, but
there is no coherent access in superposition. A word READ stages only
O(n) bits and a fixed number of such words is enough for an iterative
bitonic sorting schedule, scans, multiplication and group counts. Swap
records with known-address staged READ/WRITE. Because records are
classical conditional on the transcript, comparison flags may be
measured and forgotten immediately. No large reversible sorting history
is required for the BASIS tables. No ordinary classical copy of a whole
table or map exists. LOW retained C strings are an explicit fixed-size
ordinary exception within O(n^2).

In contrast the ORIGINAL index and its sum/lookup answers, rank, inverse
and predicate scratch may be coherent. Their reads are explicit LINEAR
scans of the classical bank: READ a row into a fixed classical staging
word, compute the equality against the quantum key, XOR known row
contents under its flag, uncompute the flag, proceed to the next known
row. Nothing measures the coherent key or answer except the specified
pass,T,q or pair-index measurements. Every scan visits <=O(L) rows and
pays each access. The same rows may be read again during uncomputation.
An exponentially large lookup is never charged as one operation.

Addition, signed comparison, multiplication, division with safe nonzero
conditional denominator, equality and XOR of O(n)-bit words have uniform
polynomial reversible Boolean implementations. For explicit conservative
bounds take O(n^2) scratch and O((n+1)^6) work INCLUDING address/gate
fees: schoolbook bounded loops plus compute/copy/uncompute satisfy this.
Exact Toffoli has a fixed Clifford+T decomposition. H, computational
measurement and reset are allowed primitives. There are no approximate
rotations. Circuit generation streams loop counters and gates, storing
no exponential instruction list. Required full signed labels and c
coefficients remain ordinary O(n^2) classical bits.

Reserve SIXTEEN full dense regions, each of capacity

 W=2^128*(L*Aword+Aword^2) qubits, Aword=1024(n+1).

Each table row and all fields fit a fixed number of Aword-bit records;
there are <=L rows in each raw, canonical, F, G and group array, plus
O(n^2) local coherent scratch. The generous constants accommodate
simultaneously the two raw tables, two canonical tables, F/G, group
metadata and staging; no object of size L^2 is stored. ALL unused cells,
validity flags, padding, headers, field boundaries and local scratch are
included. HIGH implies m>=4ell+64 and L>n+1, so sixteen W=O(Ln).
Allocate lazily for this one helper and release it in full before its
parent starts. All cells are initialized and reset with counted operations.
No all-seen-history is retained across attempts. Global allocation and
address size are O(n) bits even for the largest possible helper.

## 9. Deterministic work bounds on EVERY branch

Full raw generation enumerates <=L assignments/block, each subset sum
using <=k additions; with O(n)-bit words, fees and streamed control this
costs O(L(n+1)^7). Canonical and F/G sorting can use fixed iterative
bitonic networks padded to a power-of-two length <=2L. The O(L log^2 L)
comparators have O(n)-bit classical staged records; charging (n+1)^6
per comparator gives O(L(n+1)^8). Binary searches for <=2L F/G
lookups cost O(L(n+1)^7). Merging and metadata generation take at most
O(L(n+1)^6) with streamed counts and known-address writes. Each coherent
linear scan is O(L(n+1)^6), and there are a fixed number, including all
uncomputation scans. Finite arithmetic scratch can be reused and costs
O((n+1)^6) per invocation. Final classical inverses and labels cost
O(L(n+1)^6). Full initialization and cleanup cost O(W(n+1)^4),
which is O(L(n+1)^5) in HIGH. All ordinary controller work, gate output,
address computation and source staging is included in these overestimates.

A common safe upper bound for a HIGH helper is therefore
 C1*L(n+1)^12 work, C2*L(n+1) qubits, C3*(n+1)^2 ordinary bits,
for absolute constants. Failure returns and malformed control defaults
obey the same literal bounds. LOW's bound is Section 3. The helper
never acquires a DCP source copy; all such inputs were counted by the
surrounding generator. These facts, not an expected-time quantum search,
are what proof.md uses for the full branchwise theorem.
