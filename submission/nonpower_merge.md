# SEGMENT-VECTOR-LOGCAP: actual interval merges, real support resets and batch tails

This file is part of the SAME algorithm of proof.md, not a source oracle
or a predecessor certificate. EVERY binary merge uses B below, including
merges with a full-power output. No full-power INPUT assumption is made
at reset merges. Probabilities use the ideal-label reference of proof5;
actual branches retain the same finite caps and work allocations.

## A. Exact public cycles and actual projections

Use proof8's public cycles (a,v,sigma), padded widths lambda_i and reset
heights. In EACH cycle separately set h0=a,W=lambda_a,
 delta_j=(j+1)2^(j-v-sigma),M_j=(1-delta_j)2^lambda_(a+j),0<=j<v.
The symbols h0,v,sigma,W in E mean these LOCAL cycle values; W is an
index width and is distinct from the root frequency in proof9. Each
cycle has v>=128 and W>=2v+2sigma+64u. Thus all supports are EXACT
positive integers between7/8 and1 times their padded lengths. Widths
are nondecreasing with increments0/1; no false W+j identity is needed.

At height0 build a fresh full dl-qubit tensor leaf. Actually compute
and measure index<M_0 and clear comparator scratch. On false reset the
WHOLE leaf and rebuild fresh; on true retain the equal-magnitude vector
on its firstM_0 indices, with its ABSOLUTE high table and common prefix.
Within a cycle, local binary steps j=1..v-1 use B to output M_j.
At the nonfinal cycle's endpoint i=a+v, B instead outputs the FULL power
2^lambda_i with a4-bit window margin, using the actual nonpower children.
On failure reset both children and repeat fresh. On success perform the
next cycle's real range measurement index<M_next,0 at the SAME heighti;
on rejection rebuild the WHOLE reset subtree fresh, not merely its
last measurement. The next output has exactly M_next,0 entries.
At the final heightm use B with full output2^d and a2-bit margin,
d1 forcoarse,d=rout forfine. Internalresetoutputsremainunchanged.
Every predicate, comparator, table and retry is charged and capped.

Each successful entry retains a distinct binary0/1 incidence vector over
fresh canonical source coordinates. The logical storage is one prefix
c=lab[0]mod2^p and ABSOLUTE hi=floor(lab/2^p). A projection is index-only
and label/phase independent with retention exactly1-delta_0. It does not
supply a free state or erase previously acquired samples from counters.

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

At the FINAL merge of the last cycle both input lengths are
 M_(v-1)=(1-v2^(-sigma-1))2^H>=(7/8)2^H.
With FULL output2^d and b<=2H-d-2, B.1 gives, even on FULL
inputtables, q(2^d-1)/(Mprev²)<=16/49 sinceMprev>=7/8*2^H,
 Pr(FAIL_final)<=16/49.                         (E.3)
Each cycle transition's separate exact range-failure probability is
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


At every nonfinal cycle RESET binary merge, both input lengths are
at least(7/8)2^lambda_prev, outputL=2^lambda_next, and
b<=2lambda_prev-lambda_next-4. The EXACT B.1 remainder formula gives
 Pr(FAIL_reset |FULL input tables)<=2^b L/M_prev²<=4/49. (E.5)
The output is a genuine full-power phase vector because B chooses an
injective complete interval of preciselyL pairs, not an arbitrary
renormalization of a smaller state. The following range predicate is a
separate real measurement, with a separate fresh-subtree retry on false.
All projections and resets read no bits beyond their assigned precision.

## G. LOW coupling with actual cycle resets and projections

At a nonreset/nonfinal binary level in a cycle the conditional failure
probability q(G)<=e_j by E.1/E.2. At a reset level it is<=4/49 by E.5,
even conditional on full inputs; final q<=16/49 by E.3. Each cycle-start
range projection has q=delta_0<=1/16, independent of labels and phase.
All these bounds also hold conditional on F's LOW field, including the
just-built child costs and their upper ghost costs.

Given that LOW field, draw a fresh uniform U independent of it and all
future fresh constructions. First set failure iff U<=q(G), then sample
the current finite window/instrument outcomes from their correct
conditional law given G and this event; null branches are arbitrary.
This reproduces EXACTLY the actual joint law and does not assert U is
independent of the full saved high-label table. Current outcomes read
only their assigned low window. Higher accepted blocks remain uniform
and independent and can be deferred in the analysis. Source waiting
histories do not reveal them, as F proves. Every discarded construction
uses coordinates never reused by retained vectors.

Use deterministic upper threshold p_i=e_j at internal cycle levels,
4/49 at resets,16/49 at the final root, and delta_0 at projections.
Whenever actual success occurs but U<=p_i, append fresh ghost trials in
the upper process only. Its trial count is the first U>p_i, hence an
independent geometric variable with law(1-p_i)p_i^(g-1). Child upper
costs are LOW-measurable, so these parent coins are independent of them;
future upper copies are fresh. This preserves the joint independent
unread-window/upper-cost invariant for the next level. Ghost coordinates
added after actual success are separate and reveal no higher block of
its retained actual output. This is an analytical coupling, not a gate,
source purification, new sample, hidden oracle or physical coin.

Starting from Z_0=dl delivered coordinates for an UNPROJECTED full
leaf, every binary step is dominated by
 Z_i=sum_(t=1)^G_i (Z_(i-1,t,1)+Z_(i-1,t,2)),
with independent child copies and G_i independent of them. At EACH
cycle start, including height0, append a SAME-height projection process
 P_i=sum_(t=1)^G_proj Z_(i,t).
For a noninitial cycle this follows its full-power reset merge. A failed
projection rebuilds the full subtree, so this sum models the correct
actual retry, not only the last operation. It does not introduce an
extra factor2 into the height normalization. There are at most128
cycles and at most127 resets. Positive retentions imply almost-sure
uncapped completion; actual capped execution agrees until a guard.
Actual costs and actual success can remain correlated within each trial.

## H. Uniform exponential moment with a constant number of cycles

For a binary heighti let F_i(z)=Eexp(zZ_i/(dl2^i)). With
V=F_before(z/2)^2, the upper geometric law gives
 F_after(z)=(1-p)V/(1-pV).
For a SAME-height projection use V=F_before(z). Initially logF_0(z)=z
before projection. Define f_p(a)=a+log(1-p)-log(1-p exp(a)).
All p<=1/3 by E.2..E.5. For0<=a<=1/2,exp(a)<5/3 and
 f'_p(a)=1/(1-p exp(a))<=1/(1-5p/3)<=1+5p,
since p<=1/3<2/5. Denominators are positive and f_p(0)=0.
Thus each binary/projection step multiplies an upper linear slope K
by at most1+5p, as long as its argument is at most1/2.

For each cycle, prod_internal(1+5e_j)<=exp(5sum e_j)
<=exp(5/64)<9/8. Each projection factor<=21/16<4/3;
each reset factor<=69/49<3/2; the final factor<=129/49<3.
There are at most128 cycles by proof8, so ALL partial slope products obey
 K<=3*(9/8)^128*(4/3)^128*(3/2)^128
   =3*(9/4)^128<2^154.                          (H.1)
For0<=z<=2^-156, Kz<=1/4. At a binary step the argument
2logF_before(z/2)<=Kz; at projection it islogF_before(z)<=Kz.
Induction therefore validates every derivative bound and existence of
every moment used, including all same-height projection repetitions.
For the actualfull2^d final root, uniformly given any prior history,
 Eexp(D_root/(2^156 dl2^m))<=exp(1/4).           (H.2)
This is a proved fixed constant, not an asymptotic oracle or free retry.
Its very large size is retained in the ACTUAL finite guards below.

## I. Actual batch guards and acquisition tail

For R roots, tower conditional expectation gives
 Eexp(D_inf/(2^156 dl2^m))<=exp(R/4),
without assuming independence of actual root costs. The actual cap is
 D_R=2^156 dl2^m(R+u+16), C_R=4D_R.
Markov on this exponential moment yields
 Pr(D_inf>D_R)<=exp(-3R/4-u-16)<=2^-16/n.        (I.1)
Every supplier acquisition independently yields an accepted phase qubit
with conditional probability>=1/2. Extend its potential indicators past
stopping only for analysis. For the accepted countA inC_R acquisitions,
 E[3^-A]<=(2/3)^C_R.
A source-guard abort before demand abort/completion impliesA<=D_R, hence
 Pr(source abort before demand abort)
 <=3^D_R(2/3)^(4D_R)=(16/27)^D_R
 <=2^(-D_R/2)<=2^-12/n.                        (I.2)
The last uses(16/27)^2<1/2 andD_R>=2(u+12).
All actual delivered, rejected, failed and projection/reset demands are
counted. Wrong-label branches obey the same public finite loops/guards;
probabilities transfer by proof5's first-label-error coupling, never by
conditioning on all future labels being correct. At most3n batches
therefore have the same global abort budget used by proof13.

## J. Fine fixed raw cap after the actual full-vector generalization

The final fixed-table16/49 bound E.3 isuniforminlegald,soALL H slopes
andthe exponentialmoment remainvalid afterproof8's actualcapacity/field
checks. JensenH.2 yieldsEdelivered<=2^154dl2^m. Supplierwaitinghasmean
<=2andisindependentoftheaccepteduniformvaluebyF; sumpositivecosts
usingtruncation/monotoneconvergence toobtainEraw<=2^155dl2^m.
TheactualfineguardCf=2^161dl2^mthereforehasmissingprobability<=1/64,
uniformlygivenpriorhistoryanditsfixedB,h,d. Allrequests/retriesand
partialconstructionscount. Completion/guardreadsonlyLOWandcounters,
soallunusedtoplabelsandconditionalpairwiseuniformlawsremainvalid.
ThecoarseR-rootbatchesstillusetheactualIguardsunchanged. Allfine
work/copycapsareworst-case; meanisusedonlytoprovesuccessundercaps.
