# HYBRID-TAPER late instrument, deferred-label coupling and batch tail

This file is part of the SAME algorithm of proof.md, not an oracle or
prior accepted theorem. EARLY levels run its full-power MERGE6.2.
The final root is always full2. All following probabilities concern the
ideal-label reference of proof5; actual labels are coupled until first
error, and deterministic caps apply on every actual branch.

## A. Exact transition and late dimensions

Use h0,v,sigma,lambda_i from proof8. Within this helper ONLY, W is
the switch INDEX width, distinct from the final frequency W in proof9.
Let W=lambda_h0 and
 delta_j=(j+1)2^(j-v-sigma),M_j=(1-delta_j)2^lambda_(h0+j),0<=j<v.
Proof8.6 gives W>=2v+2sigma+64u and v>=128. Hence all M_j are EXACT
integers, between7/8 and1 times their padded dimension. The late widths
are nondecreasing with increments0/1; they need not equalW+j.
START builds EARLY(h0), then actually computes/measures index<M0.
False resets the entire early tree and retries under the same counters;
true keeps preciselyM0 equal-magnitude entries. Labels are sums of
distinct canonical accepted coordinates with binary0/1 incidences.
The original storage is c=lab[0]mod2^p,ABSOLUTEhi=floor(lab/2^p),
so no hi[0] gauge is subtracted until the final root Wfrequency.
Projection is index-only and phase independent. All its cost is charged.
At late local levelj1..v-1, run the following complete MERGE with output
M_j; the final merge uses output2, with the2-bit window margin.

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
superposed index, not per row. Every LATE input has at least
(7/8)2^W>=n^2 rows by proof8.6, so these additive O(n^2) costs fit O(n(A+B)).
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

## E. Late loss bounds at nondecreasing widths

At late local level1<=j<v put delta=delta_(j-1),
zeta=delta_j-2delta=2^(j-v-sigma)>0,E=2^lambda_(h0+j).
The actual window b obeys b<=2lambda_prev-lambda_next. Put
k=2lambda_prev-lambda_next-b,J=2^k,L=M_j. Then
 V/q=mu=J(1-delta)^2E, L=(1-2delta-zeta)E,
 g=mu-JL=J(zeta+delta²)E.
For any integerx>=0, xmodL<=(x-JL)_++L*1_(x<JL).
D.1 gives E[(x-JL)_+|G]<=g+sqrt(mu)+1 and
Pr(x<JL|G)<=mu/(g-1)^2. Substituting in the EXACT B.1 formula,
 Pr(FAIL_j|G)<=g/mu+1/sqrt(mu)+1/mu+L/(g-1)^2
 <=2zeta+2delta²+2/sqrt(E)+2/E+4/(zeta²E)=e_j.   (E.1)
Here delta<=1/16,(1-delta)^2>=1/2,L<=E and
g>=zetaE>=2^(W+j-v-sigma)>=2 by8.6. This bound conditions on
LOW G, including built child costs, not full high-label tables.

Since v/2^sigma<=1/4, delta<=2^(j-v-3), so
 sum_j2delta²<=1/96, sum_j2zeta<1/(2v)<=1/256.
Unlike the old linear-width formula, late widths may have zero increments.
Use E>=2^W, not a false E=2^(base+j) identity. Geometric summation gives
 sum_j 2/sqrt(E)<=2v*2^(-W/2),
 sum_j 2/E<=2v*2^(-W),
 sum_j 4/(zeta²E)<=2^(2v+2sigma+2-W)/3.
The last uses sum_(j>=1)2^(-2j)=1/3. Under W>=2v+2sigma+64u,
these residuals total at most
 2v2^(-v-sigma-32u)+2v2^(-2v-2sigma-64u)+2^(2-64u)/3
 <1/768 for v>=128,u>=1. For example v<=2^v andsigma>=9 bound
these by2^(1-sigma-32u),2^(1-v-2sigma-64u),2^(2-64u)/3;
their endpoint sum is already<1/768 and decreases. Hence
 sum_(j=1)^(v-1)e_j<=1/96+1/256+1/768=1/64.      (E.2)
No pointwise3delta² bound is asserted for this schedule.

At the FINAL merge both input lengths are
 M_(v-1)=(1-v2^(-sigma-1))2^H>=(7/8)2^H.
With full output2 and b<=2H-3, B.1 gives, even on FULL input tables,
 Pr(FAIL_final)<=16/49.                         (E.3)
The transition's separate exact range-failure probability is
 delta_0=2^(-v-sigma)<=1/16.                     (E.4)
Every successful index still has a distinct binary incidence vector.

## F. Deferred accepted bits and the cost-measurable low field

This section justifies the particular conditioning used in E and G;
it does not assume that failure and actual cost are independent.
For each accepted ideal supplier value, one may draw its binary blocks
in order as needed for STRUCTURAL choices. This is an analytical
factorization of the iid uniform accepted values, not a different source
or an operation available to the algorithm. Full high tables may physically
be stored; probabilities below do not condition on that full record.
For a power-of-two accepted interval, the accepted uniform value is
independent of the number and values of preceding rejected acquisitions:
for any fixed rejected sequence each possible accepted value contributes
the same terminal factor. Direct modular suppliers are already uniform.
LE internal outcomes can be omitted from this coarse field because in
the ideal-label reference they feed no selection decision and each LE
uses a fixed gate count. Rejected/waiting histories do not expose the
unread bits of accepted coordinates used by surviving vectors.

At a node with current precision p, let G include all accepted source
bits below p used in the actual two child constructions, their structural
choices, source waiting counts, delivered costs and assignments, and
auxiliary LOW ghost variables of G below. The children use disjoint
fresh accepted coordinates. Child computational residue/rank choices
read only bits strictly below their ending precision p; transition range
predicates read only indices. Their probabilities depend on equal
magnitudes and these low bits, never on phase values. Consequently the
current window bits of surviving accepted coordinates remain mutually
independent uniform conditional G. Carries from adding lower bits and
incidence assignments are G-measurable. This is precisely D.1, now
with the costs and the LOW auxiliary variables explicitly included.
Bits beyond the current ending precision remain unread for future
structural laws as well. Known physical high fields do not invalidate
this coarser probability statement.

More formally, inductively extend the analytical field after each step
by that step's read low bits, index outcomes and fresh auxiliary coins.
Allocate each fresh accepted coordinate with independent unused blocks.
A discarded construction can have all its blocks revealed: its coordinates
are never reused. A retained construction reveals only blocks up to its
ending precision in this field. Projection success is index-only.
Thus induction preserves the independent unused blocks of retained
coordinates, even after repeated failures and random source stopping.
All cost counters and future-independent ghost costs in G are functions
of those already revealed variables. This proves the required joint
cost/unused-bit assertion, not merely a marginal uniform-frequency law.

## G. Analytical upper process with LOW parent coins

At an early merge the conditional failure probability is at most
p=2^-kappa even given FULL input tables by proof6.1, and its actual
failure law depends only on its current read low window. At a late
merge the failure probability conditional on F's G is q(G)<=e_j by E.1.
The final root has q<=16/49 even on full tables. A transition range
projection has q=delta_0 pointwise, independent of child labels/phases.

The following coupling works for the weaker LOW late bound. Given G,
sample U uniform[0,1] independently of G and of all future fresh child
constructions. First set failure iff U<=q(G); then sample the current
finite label-window/instrument-outcome variables from their correct
conditional distribution given G and that failure/success event. Null
conditional branches of probability0 can be assigned arbitrarily.
This reconstructs EXACTLY their original joint law. It never claims
U is independent of the full current high table. All blocks above the
ending precision can still be sampled independently later: the current
event depends only on the window and its computational index outcomes.
No phase operation, physical source purification, extra sample, oracle
or actual coin has been added; this is a classical probability coupling
of the latent-label/quantum-outcome law proved in3 and B/D.

For the upper process use the deterministic threshold p_i, namely p
at early levels, e_j at late nonfinal levels and16/49 at the final root.
The event U<=p_i dominates failure. Whenever actual success occurs
while U<=p_i, add ghost trials with fresh independent child copies in
the UPPER process only. Its trial count is the first U>p_i and is thus
an independent geometric G_i with
 Pr(G_i=g)=(1-p_i)p_i^(g-1),g>=1.
The just-built upper child costs are G-measurable, so U is independent
of them. Future upper child copies are fresh and independent of U.
Early auxiliary coins and late coins can be chosen as above using only
the current window and fresh randomness. Hence all ghost costs remain
measurable in the enlarged LOW field for the next level; they cannot
expose its higher window bits. When ghosts continue after real success,
they use new independent coordinates and do not alter the retained
actual output or reveal its unused blocks. This closes the joint induction
required by F, including random assignments and earlier failed trials.

Start Z_0=dl delivered qubits for the full-power leaf. At each binary
merge of height i the actual delivered cost is dominated by
 Z_i=sum_(a=1)^G_i (Z_(i-1,a,1)+Z_(i-1,a,2)),
with independent child copies and G_i independent of them. At h0,
after its early merge, insert an EXTRA geometric projection repetition
 P_h0=sum_(a=1)^G_proj Z_(h0,a),
with parameterdelta_0 and fresh early subtrees; this does NOT change
the canonical height or multiply the normalization by2. Use P_h0
as the child distribution for later heights. Positive retentions and
finite geometric variables establish almost-sure uncapped completion.
The actual capped execution agrees until a guard fires. Actual costs
and success can be correlated within a trial throughout this argument.

## H. Uniform exponential moment for normalized delivered cost

For a binary height i put F_i(z)=Eexp(zZ_i/(dl2^i)). The independent
upper recursion of G gives, with V=F_(i-1)(z/2)^2,
 F_i(z)=(1-p_i)V/(1-p_i V).
For the transition projection at the SAME height, use V=F_before(z)
instead, with p_i=delta_0. At the leaf logF_0(z)=z.
Let f_p(a)=a+log(1-p)-log(1-p exp(a)). On0<=a<=1/4,
exp(a)<2, so for p<1/2,
 f'_p(a)=1/(1-p exp(a))<=1/(1-2p), f_p(0)=0.
All denominators are positive there. If logF_before(z)<=Kz for
0<=z<=1/64 and K<=16, the next binary a=2logF_before(z/2)
(or projection a=logF_before(z)) is <=Kz<=1/4. Thus
 logF_after(z)<=Kz/(1-2p).

The cumulative multiplier is bounded by
 (1-2p)^(-h0) * (1-2delta_0)^(-1)
 *prod_j(1-2e_j)^(-1)*(1-32/49)^(-1)
 <=4*(8/7)*(32/31)*(49/17)<16.
Here (1-1/m)^(-m)<=4 for m>=2 bounds all early factors, E.2 and
prod(1-a_j)>=1-sum a_j give the late32/31, and E.3/E.4 give the
other factors. In particular every individual p_i<1/2, and every partial
product<=16. Induction therefore proves existence and the bound for
all moments used, including the SAME-height projection step. At root,
 Eexp(D_root/(64dl2^m))<=exp(1/4).                (H.1)
This holds uniformly conditional on any prior root/batch history;
fresh coordinate blocks and the same fixed public parameters suffice.
No claim of independence between actual root costs is needed.

## I. Batch tail, selected acquisitions and actual guards

For R sequential roots, the tower property applied to H.1 gives
 Eexp(D_inf/(64dl2^m))<=exp(R/4),
where D_inf is total delivered demand of the uncapped reference.
For ACTUAL D_R=1024dl2^m(R+u+16), Markov implies
 Pr(D_inf>D_R)
 <=exp((16R-1024(R+u+16))/64)<2^(-u-20)<=2^-20/n.  (I.1)
For example its exponent is <=-16u-256, and exp(-x)<=2^-x forx>=0.
This proves the delivered-guard bound; replacing it by a mean/Markov
constant would not have sufficed over the O(n) batches.

Each selected acquisition in the ideal supplier yields an accepted
qubit with conditional probability>=1/2. Extend potential indicators
past stopping solely for analysis. If A is their sum over C_R=4D_R
acquisitions, iterated conditional expectation yields
 E[3^-A]<=(2/3)^C_R.
A source-cap abort before demand abort/completion entailsA<=D_R. Hence
 Pr(source-cap abort before demand abort)
 <=3^D_R(2/3)^(4D_R)=(16/27)^D_R
 <=2^(-D_R/2)<=2^(-u-20)<=2^-20/n,              (I.2)
since (16/27)^2<1/2 and D_R>=2(u+20). Thus total batch abort<2^-19/n.
All rejected copies and failed/projection trials are included in these
actual counters. Wrong-label branches still execute finite guards and
the same public memory/work loops; probability analysis is transferred
by the first-error comparison in proof5.1, not by conditioning a whole
run on correct extraction. No earlier accepted artifact supplies a
missing probability argument here.
