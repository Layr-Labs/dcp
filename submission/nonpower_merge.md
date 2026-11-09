# Non-power intermediate vectors and the merge retention proof

This file specifies part of the SAME NONPOWER-QUARTER algorithm as proof.md,
not an oracle. All arithmetic, lookups, gates and source copies are charged
in the model of proof2. Source promise is independent ideal coset copies.
The final root length is still a power of two, so qudit_decoder.md applies.

## A. Exact dimensions and uniform vector representation

On the main range let m be the stated exact integer fourth root and
 base=ceil(n/(m+1)-m/2)+2, dl=base, H=base+m-1.
For 0<=i<m define
 lambda_i=base+i, delta_i=2^(i-m-2),
 M_i=2^lambda_i-2^(lambda_i+i-m-2)=(1-delta_i)2^lambda_i.
Proof8 establishes base>=16m+64u, u=ceil(log2n), hence these are EXACT
positive integers and 7/8<=M_i/2^lambda_i<1. There is no floor error.
The index uses lambda_i qubits with zero ideal amplitude outside [0,M_i).
The final root length is M_m=2^d on d qubits, d=1 for coarse or r for data.
No fictitious non-power Hilbert-space dimension is used.

A length-M vector is M^(-1/2)sum_(a<M)exp(2pi i lab[a] theta)|a>,
up to global phase. For precision p store common c=lab[0] mod2^p and
ABSOLUTE high parts hi[a]=(lab[a]-c)/2^p, so lab[a]=c+2^p hi[a].
Do NOT subtract hi[0] at intermediate levels. The logical labels are sums
of distinct canonical source coordinates with coefficients0/1. Distinct
indices have distinct incidence vectors; disjoint children use disjoint
fresh source coordinates. Root relative W is formed only after completion.

LEAF acquires dl phase qubits and their known labels as proof9. Their
tensor index is uniform on2^dl. Compute the predicate index<M_0 using
reversible comparison, measure it, uncompute the comparison scratch.
If false reset/release all work and retry a fresh leaf, subject to the
root selected-source cap. If true its state is the uniform phase vector
on [0,M_0), with the original distinct binary subset incidences. The
success probability is 1-delta_0, independent of all label values/phases.
Classical generation may enumerate the full2^dl tensor labels then keep
M_0; this is a factor<16/15 overhead, counted in work/storage. This is
real postselection with failed source copies and work charged, not a
free uniform-nonpower-state preparation.

## B. Explicit finite merge instrument for arbitrary integer lengths

Inputs have lengths A,B with index widths lambda, common precision p,
common prefixes cA,cB, and absolute high tables hA,hB. Choose a window b
and output integer L, with output width ell=ceil(log2 L). Put q=2^b,
c=(cA+cB) mod2^p, car=floor((cA+cB)/2^p), car in{0,1}.
Compute s=(hA[a]+hB[z]+car) modq reversibly by XOR lookups and fixed
bit arithmetic, measure its b computational-basis bits as s, and uncompute
the quantum scratch using the still-retained input indices. The classical
s is recorded. For b=0 there is one residue and no residue measurement.
The selected pair set is
 P_s={(a,z):a<A,z<B,(hA[a]+hB[z]+car) modq=s}.
All its pairs have equal magnitude; write v_s=|P_s|. If v_s=0 FAIL.
Only this selected residue's pairs are processed; no q-sized bucket table
or A*B list is constructed.

Here are the complete classical order and quantum rank maps. Stable-sort
(aA[a],a), aA=hA modq, and (aB[z],z), aB=hB modq. Use digit width lambda
and 2^lambda counters. Each valid input length is >=7/8*2^lambda, so this
counter array is a constant-factor input array. At most two digit passes
suffice because b<=2lambda. A pass zeroes counters, scans/increments them,
prefix-sums bucket starts, stable-copies every key/index bit to the next
bucket position, and increments that position. Keys, counters, pointers
and record bits have their exact finite widths. This gives stable order
by (residue,original index), including ties, with O(n(A+B)) core bit work
and O(H(A+B)) residue/rank bits. For b=0 use the identity order.

For each nonempty A residue class t, merge-join the B class s-car-t modq.
Order the resulting groups by increasing t. A group is the rectangle
A_t x B_(s-car-t), with indices in their stable order, and size a_t b_t.
Compute its prefix offset o_t among these rectangle sizes. Store input
positions, class starts/sizes and offsets in explicit per-input tables.
For a valid pair the injective rank is
 R=o_t+(posA(a)-startA_t)*b_t+(posB(z)-startB_t), 0<=R<v_s.
Load these known values by the explicit XOR lookup below; compute R
reversibly. Check validity (both padded input indices in range and their
class relation correct); an invalid address returns FAIL with reset.

For any classical table with E rows of w bits and index width ell, XOR
lookup iterates every row x0, computes [index=x0] with an AND/Toffoli
chain, CNOT-XORs its1 entry bits, then uncomputes the chain. Out-of-range
indices give0. It is a unitary, self-inverse circuit on the WHOLE padded
space, costing O(E(ell+w)) gates and O(ell+w) qubits. Every table bit read,
gate generation, gate execution and later reset is charged. No QRAM.

From R compute Q=floor(R/L) and J=R modL by reversible restoring long
division. An explicit implementation keeps R, an O(n)-bit quotient and
remainder and O(n) carry/borrow scratch: scan input bits most significant
first, shift the remainder, compare/subtract the known L, and record the
quotient bit. Each of O(n) rounds uses O(n) controlled bit operations.
Schoolbook reversible multiplication in the rank formula similarly uses
shifted controlled ripple additions, O(n^2) gates and O(n) scratch.
Inverse these computations after copying J into a separate output index.
Measure Q in the computational basis. If Q>=floor(v_s/L), FAIL/reset.
Otherwise retain that classical Q, copy J, and uncompute all quantum
rank/division/lookup scratch using the retained input pair. The measured
Q wire can be uncomputed because R determines it on this outcome branch.
No quantum measurement outcome or postselection is free.

Construct the selected inverse list J->(a,z), J=0..L-1, as the pairs of
contiguous ranks [QL,(Q+1)L). Find its first rectangle by scanning group
headers, divide the first local rank by its known b_t ONCE to obtain the
starting pair, then enumerate pairs with increment/wrap of the B position
and A position. All later rectangles start at their first pair; the last
partial rectangle simply stops. There is no per-row or per-group long
division. XOR this inverse list into the original input registers using
output J as index; this clears both input indices on the selected image.
The inverse lookup is0 off the valid image, hence is a finite full-space
unitary also on bad states. Reset all cleared scratch before returning.
The successful output has EXACTLY L entries and equal magnitudes, with
new common prefix c'=c+2^p s and high labels
 (hA[a]+hB[z]+car-s)/2^b.
These are exact nonnegative integers; high-field widths include the carry.
Thus the output is a phase vector collimated to p+b. There is no unknown
phase correction; the common prefix contributes only a global phase.

For fixed input tables, residue s occurs with probability v_s/(AB).
Each complete block Q then contains exactly L equal-magnitude pairs.
Consequently the exact FAIL probability of this instrument is
 sum_s (v_s modL)/(AB).                         (B.1)
This holds for arbitrary phases. Every accepted output index still has
a distinct0/1 canonical incidence vector, by injective pair reindexing.

## C. Deterministic work and storage of the maps

All fields used for residues, positions, class sizes, pair counts, ranks
and group offsets are O(H) bits; output high labels use proof9's actual
w_i widths. No array with AB rows or q rows is allocated. Radix counters
have2^lambda rows, at most8/7 times the valid input length. Stable sorting,
merge-joining, prefix additions, table initialization and all lookup gate
scans cost O(n(A+B+L)) core work and the corresponding actual-width
storage, with addressing paid separately by proof14.

Classical rectangle-size products do not cost O(n^2) for each input row.
Use schoolbook multiplication at the ACTUAL bit lengths of the known
counts a_t,b_t. For positive integers a,b,
 log2(a+1)log2(b+1)<=C(a+b)
for an absolute C, since xy<=(x^2+y^2)/2 and log2(z+1)^2<=C'z.
The classes are disjoint, so the sum of these product costs is O(A+B).
Finding bit lengths, zero-padding their products and adding O(H)-bit
prefix offsets costs O(n) per group, hence O(n(A+B)). The inverse selected
interval walk costs O(nL) plus its ONE O(n^2) starting division.
Quantum multiplication/division also costs O(n^2) ONCE per merge on the
superposed index, not per row. On this main range every input has at
least2^(base-1)>=n^2 rows, so these additive O(n^2) costs fit O(n(A+B)).
All loops and maps are finite on padded/invalid addresses. Source/root
caps apply during every retry; no probabilistic running-time cutoff is
silently removed from the every-branch resource ledger.

## D. Conditional pairwise-uniform bucket moments

At a window beginning at precision p, condition on ALL source LOW bits
mod2^p and all previous structural choices, residues, retries and index
assignments, excluding unused higher source bits and the current root
measurement. Call this G. Every stored absolute high label is
 constant(entry)+sum_v incidence(entry,v)*tau_v modq,
with independent uniform tau_v in Z/q and distinct0/1 incidence vectors.
Leaf range selection depends only on the index; all earlier merge choices
inspect only already-exposed LOW bits. Their computational residue/rank
measurements depend only on those bits and equal magnitudes. Induction
therefore preserves independence of the unused higher labels conditional G.
The physical full-label tables may be known to the computer; G is a
coarser analytical sigma-field, not the full computer record.

For two disjoint children, all pair incidences are distinct binary vectors,
with at most one zero vector. Any two DISTINCT NONZERO binary vectors
have a2x2 minor of determinant+1 or-1: use an exclusive coordinate from
each when neither contains the other; use one common and one extra
coordinate for proper containment; for disjoint supports use one each.
The two affine forms over Z/2^b are therefore jointly uniform, regardless
of their G-measurable additive constants. For q=1 this is the trivial
deterministic case with variance0. It follows, for V=AB and mu=V/q,
 |E(v_s|G)-mu|<=1, Var(v_s|G)<=mu.             (D.1)
Indeed all but possibly one bucket indicators are pairwise-independent
Bernoulli1/q, and the remaining zero-incidence indicator is deterministic.
No joint independence of the entire label or frequency table is asserted.

## E. Nonroot failure margins without kappa loss

For nonroot level1<=i<m let delta=delta_(i-1)<=1/16, E=2^lambda_i,
choose b<=2lambda_(i-1)-lambda_i, and put
 k=2lambda_(i-1)-lambda_i-b, J=2^k,
 L=M_i=(1-2delta)E,
 mu=J(1-delta)^2E, g=mu-JL=J delta^2 E.
For any integer v>=0,
 v modL <= (v-JL)_+ + L*1_(v<JL).
From D.1, E[(v_s-JL)_+|G]<=g+sqrt(mu)+1 and, since g>1,
 P(v_s<JL|G)<=mu/(g-1)^2 by Chebyshev. Substituting into B.1 gives
 E(FAIL|G)<=g/mu+1/sqrt(mu)+1/mu+L/(g-1)^2
   <=2delta^2+2/sqrt(E)+2/E+4/(delta^4 E)
   <=3delta^2.                                (E.1)
The middle bound uses (1-delta)^2>=1/2 and g>=delta^2 E>=2.
For the last, delta>=2^(-m-2), lambda_i>=base+1 and
base>=16m+64u. Dividing the three residual terms by delta^2 gives
at most2^(5-6m-32u),2^(4-14m-64u),2^(13-10m-64u), whose sum
is<1 for m>=2,u>=1. Thus the displayed bound holds throughout the
main range, not only eventually. Summing the geometric delta squares,
 sum_(i=1)^(m-1)3delta_(i-1)^2<=1/64.          (E.2)
This expectation is over fresh unused window labels AND the actual
residue/block measurement. It is not claimed conditional on full high
input tables, and no such stronger assertion is needed below.

The FINAL root has FULL power length L=2^d, inputs M_(m-1)=(7/8)2^H,
and b<=2H-d-2. The distribution-free bound B.1 gives, even conditional
on both COMPLETE input tables,
 P(FAIL)<=qL/V<=16/49, P(success)>=33/49.       (E.3)
Only this one final level incurs a constant loss. Its output length is
exactly2^d, including coarse d=1 and data d=r.

## F. Renewal source bound, including within-trial correlations

In the uncapped reference VEC_i, after FAIL reset both children and repeat
FRESH child constructions with the same parameters. Future trials use
fresh source systems and measurement coins. A trial's source cost may
correlate with its success; renewal still gives
 E C_i=E C_trial+P(FAIL) E C_i,
because only the FUTURE trial sequence must be fresh. Thus each nonroot
contributes factor at most(1-3delta^2)^(-1) to2E C_(i-1). At the leaf,
E C_0=dl/(1-delta_0) delivered qubits. By E.2, the product of nonroot
retentions is >=1-1/64=63/64; leaf retention is>=15/16, and final
root retention>=33/49. Consequently
 E delivered <=dl2^m*(16/15)*(64/63)*(49/33)<3dl2^m.
Supplier rejection has mean overhead<=2, independent of its accepted
uniform value; summing nonnegative waiting costs gives
 E selected source calls <6dl2^m.              (F.1)
This renewal argument does not assume cost and success independent
within a trial. Positive retentions and induction give almost-sure finite
uncapped completion. Capped actual roots are coupled to this reference
until their selected-call cutoff; Markov gives missing<=3/32 for cap
Cc=64dl2^m and<=3/8 for Cf=16dl2^m. Each root is completely reset.
The estimates are uniform for any fixed clean ideal preceding history;
phase values do not affect the computational bucket/rank probabilities.
Label errors are charged separately by proof13's first-error coupling,
not by conditioning this law on an extraction-success future event.

