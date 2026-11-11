# WFP4-PRODUCTS: short product twiddles and banded phase evaluation

For every N>=2 and secret s modulo N, n=ceil(log2N), ONE uniform physical
algorithm recovers the ENTIRE s with unconditional probability STRICTLY>2/3
under the exact fixed-original-joint error model below. Jointly on EVERY
branch, including failed/discarded work and aborts, it has

 T=O(2^(n/2) n (log2n)^(11/8)), SC=O(n^2), ENTIRE SQ=O(n),
 Q=3*2^40(n+32) EXACTLY, epsilon(n)=1/3.                   (0.1)

The exact indices are1,0,0,0. The finite n=1 branch has bounded absolute cost.
The exponent n/2 is linear, not sqrt(n). No clean-only success or expected
resource bound is substituted. All inactive/padded/helper/source fields count.

## 0. Complete immediate source and actual new words

The immediate material source is WFP3, a435f409-97a2-42a6-906b-cb1921384153,
immutable commit bfefa5e56527f9da7de99faed170193419b1f7f6. Its COMPLETE main
is graded-source.md, SHA-256
808dd4fb1609c859a15fa079f9f495d8d10b9118c4fcce96571d1bb604c3b8b1.
All FIVE complete mathematical helpers are unchanged: profile-source.md,
joint-source.md, spts-source.md, sources/RQ-SPLIT-proof.md and
pc-controlled-source.md, hashes respectively
bf2c3430cb60d48220f2d165eca9dafd01b16ea742afb12d87e888b00019acea,
f912b269b63e66803912eed6d517ca795731d5439a6616553493d7eba98e8d7f,
373939d8a0439acd480aad17f85ab9067d474f995a4c720f43af6a2f42bf409e,
2952a6f52b94dfa9d0e03471b9e7611f185db198dbc9274639dbc03ce7d1ca80,
bd862728628c582bf5d4f2c6592e2e5a8a59397da63dbfc0a89097e47d99a2f6.
Every active algorithmic/statistical helper is included; historical paths
inside old Section0 comments refer to their own archives, not missing lemmas.
The source carries weighted-pivot, SPTS-JM, PCT, peer SPTS1/RQ/FNS credits;
these and the actual extraction/interpolation/arithmetic methods are retained.
No separately imported ancestor feature is used outside this complete source.

THREE coordinated changes define this algorithm: short-product recursive
Fourier twiddles, banded short-product phase evaluation in EVERY coarse
predicate role, and m=2^100 ceil(L^(3/4)) with all dependent fields/caps
recomputed. This changes actual circuits and subsampling, not just a displayed
envelope. Improving the Fourier circuit alone would leave the old per-record
predicate and sparse lookup costs dominant. We bound all three together.
No equality to the predecessor's actual capped output law is claimed. Its
flat-entry and score-margin proofs are re-established for the new words.

## 1. Exact input context and unchanged statistical reference

Use EXACTLY this fifth-object context:

"Among the Q acquired copies, an adversary fixes a set B of at most floor(epsilon(n) Q) malformed positions, possibly depending on N and s. The joint state is arbitrary subject to its reduced state on all other positions being exactly rho_s^{tensor (Q-|B|)}. Malformed systems may be correlated or entangled with each other and with other systems subject to that marginal promise. No source control, purification access, or preparation inverse is supplied."

Set epsilon(n)=1/3. The bank is fixed before passive release; no replacement
or active source reaction is allowed. Conditional unread-state changes are
permitted, and arbitrary inaccessible references/fixed-B mixtures are covered.

Acquire EXACT original k=3*2^22(n+32), Q=2^18 k registers before any new abort.
Run the complete collective EXTRACT, position release, row X, all source caps
and late private split of graded-source.md1: J_e=n+4,
h=ceil(log2(2^64 Q(n+5))), F=2^21h. A uniform k-subset of all positions is
measured in fresh private X/Y axes, retaining W,beta,Z. The other m_R=Q-k
rows stay untouched by EVERY coarse operation here. R_ret=m_R/3+ceil(sqrt(16k))
and all original endpoint capacities are unchanged. Each original acquisition
pays n+1 plus real extraction/measurement/reset work.

The full-reference diagonal extraction proof in joint-source.md2-6 gives a
SINGLE unconditional comparison loss<=2^-62 replacing good reports by latent
labels. In that comparison good hidden labels are iid uniform in[0,N), and
conditional on them the good rows are pure products, factoring from arbitrary
remaining extensions. Bad reports can depend on good labels. We never infer
conditional fresh-good behavior from a bad report or cap surviving.

The original private-split count event fails<=1/64; on it shadow bad fraction
is<=1/3+1/1024 and retained bad count<=R_ret. The full original integer score
event E_int has additional failure<=2^-80 and supplies margin1/64 in both
fresh/exact roles against all necessary false integer classes. Its proof is
fixed-record and covers adaptively selected candidate lists. With the true
integer class supplied, the unchanged endpoint has UNCONDITIONAL reference
success>=91/128 before its listed losses; even-modulus parity is not conditioned
on coarse success. We keep that input bank unchanged and subtract exceptions.

For n<2^4096 execute COMPLETE SPTS-JM of joint-source.md, including its own
noisy-input finite cases and all Q originals, with success>11/16. This fixed
finite range changes only outside constants in (0.1).

## 2. New exact public parameters and complete outer algorithm

For n>=2^4096 let L=ceil(log2n), q=n+32, M=2^q. Let u be the LEAST positive
integer with u^4>=L^3, computed by integer comparison/binary search. Set

 m=2^100 u, A=2^20, C=2^24,
 b_F=60+ceil(log2q), g=128+2ceil(log2q), G=2^g,
 D=ceil(2^80 M/m), root=ceil(sqrt D).

Thus m=Theta(L^(3/4)), 2^100<=m<=2^100 L=old_m. Retain ALL original formulas
from graded-source.md2, using this actual new m and D: K is largest j>=0
with (64q3^j)^2<=D, Hmax=128K, A_j=3^j,
a_i=32+2ceil(log2(i+1)), ell_i=2^17a_i,
r_idx=ceil(log2(2^24 Hmax ell_Hmax)), Budget=2^28 root.
Bcap_j is the least power of two with Bcap_j A_j>=16root.
Recompute every dependent width, padding, angle/constraint table and sampler
cap. Public integer powers, fourth roots, square roots, ceilings and scans
use counted finite bit arithmetic, not real primitives or instance advice.

Perform the SAME complete outer program: uniform m-subset of shadow records
with capped partial Fisher-Yates; independent uniform integer anchor v with
its n+256 cap; label-only H(W) collision filter; constant-term guard; flagged
sparse cubic-score start; weighted recursive dyadic antipodal-class pivots
and exact fixed 16-attempt doubling-clock sampler; hard pre-attempt debit
B A_j against Budget; classical expansion of EVERY visited dyadic class to
both rounded original integer classes plus offsets[-A-2,A+2]; original
full-k integer champion; original untouched-bank endpoint. The empty-list
and every refusal/abort output and cleanup remain the specified source rules.
Only the actual inner words/phase precision in Sections3-5 replace their
source counterparts. Every recursive inverse is the actual new reverse word.

Old parameter inequalities remain: m<=k, D<=2^(2n), n/9<=K<=n,
Hmax=O(n), ell_max=O(L), g,b_F=O(L). The lower K bound only used
m*4096q^2<=2^(n/2+112), which is easier when m decreases. Also
m n+m^2+m g=O(n^2). In particular g>=2b_F+8 EXACTLY. All finite guards
bound work on wrong-label, wrong-gradient and arbitrary malformed paths too.

## 3. Exact short multiplication, clean use and uniform generation

Here is the concrete arithmetic used below, derived in the Boolean bit model.
For t a power of two, multiply unsigned t-bit x,y. At t=1 use one AND into
a fresh zero target. Otherwise write x=x0+2^h x1, y=y0+2^h y1, h=t/2. Compute

 z0=x0 y0, z2=x1 y1,
 d=|x1-x0| |y0-y1|, sign=[x1<x0] XOR [y0<y1],
 c=z0+z2+(-1)^sign d=x1 y0+x0 y1,
 xy=z0+2^h c+2^(2h)z2.                                  (3.1)

Differences have magnitude<2^h, so EXACTLY three h-bit recursive products
suffice. Comparisons/subtractions/absolute values, sign selection, padded
2h+2-bit cross term and 2t-bit recombination are ripple Boolean circuits of
O(t) size. One explicit full-adder computes v=a XOR b, sum=v XOR carry,
nextcarry=(a AND b) XOR (v AND carry); the two AND terms cannot both be1.
Subtraction uses complement plus carry1. For a-b mod2^h, sign is NOT final
carry; conditional complement and add sign gives its absolute value.
The signed d is represented in width2h+2 by conditional complement/add sign;
the true nonnegative c fits that width. No large arithmetic primitive is used.

Keep EVERY intermediate Boolean wire until the entire product has been used.
Each Boolean gate has a fresh zero target: AND is Toffoli, XOR two CNOTs,
NOT a CNOT and X. Thus the actual forward gate count and allocated scratch
obey 3T(t/2)+O(t), hence O(t^log2(3)) and also O(t^(8/5)), since3^5<2^8.
Arbitrary widths are padded to a next power of two. Copy the product to an
external target by XOR, ADD it to an accumulator, or use it to shift a
catalyst, then reverse the ENTIRE Boolean DAG ONCE. There is no recursive
recomputation/uncomputation doubling the three subcalls. All intermediate
scratch returns to zero. The product inputs never change. By linearity this
is valid on coherent, entangled inputs; the complete Clifford+T words and
actual inverse exist on all states, without measurements or postselection.

We give the full uniform generation account, since an irregular preloaded
circuit would not be free. The recursive layout reserves the three child
DAG areas followed by O(t) local ripple areas; their sizes satisfy the same
recurrence and are computed from t alone. Store gate type and three LOCAL
offsets per primitive, with O(log(t+2)) bits per offset. Fixed recursive
loops and ripple loops generate these tables in polynomial(t) bit work;
there are only O(log L) needed widths, all at most O(L), and this one-time
polynomial(L) preprocessing is counted. No table depends on a secret, source
label or coherent query. Actual field visits, offset calculations, stack
and table-index updates per emitted primitive cost at most
C(1+log2(t+2))^4 bit/instruction actions, a conservative schoolbook bound.
Descriptors are fetched as real short bit fields, not unit-cost words.

Place the multiplier, short input staging, accumulators and catalyst in one
power-of-two aligned poly(L)-size local quantum window. Its fixed base prefix
is retained in the paid native wire-role generator; primitive indices change
only O(log L) low address bits. All descriptor/control/offset bit actions,
reads/writes AND actual gates pay the FULL O(L) combined-memory address fee.
No full L-bit descriptor is copied or rebuilt for each primitive. This is
the same persistent native-role emission convention as the complete source:
full indexed-gate addressing is paid, with additional generation work counted.
The direct known prefix is not an instruction oracle or quantum lookup.
Consequently a complete short product/use/reverse costs

 C L t^(8/5)(1+log2(t+2))^4                               (3.2)

plus O(L) per externally copied bit. This includes both actual reverses.

To use a query substring, CNOT-copy its contiguous t bits into the short
local window, reversing order if required. This is coherent basis copying,
not cloning or measuring an arbitrary state. After product/use/reverse,
reverse those CNOTs too. A known classical coefficient substring is read
sequentially into a local basis word and cleared at exit. Global source and
query pointers follow regular forward/reverse contiguous blocks. Their
binary carry flips amortize over the walk; fixed power-of-two block strides
change the block index with the same bound. Thus a block costs O(t) extra
core actions, not O(L^2) descriptor initialization per block. Long bases and
word lengths are formed ONCE per record or Fourier call, with polynomial(L)
work, not once per bit. Arbitrary correlations with other quantum work move
through these exact CNOT/word operations. No coherent bit selects a bank or
classical memory address.

## 4. A new flat Fourier word from product twiddles

Start with the source q-bit positive QFT order: r=q-1 down to0, H_r and
controlled phases of angle2pi/2^(r-k+1) to k<r, then final wire reversal.
Partition the physical query indices into contiguous blocks of width b_F,
starting at the high end; a last low block may be shorter. Apply the EXACT
QFT within the highest block, then ALL cross phases to the immediately next
lower block, then its exact QFT, then its cross phases to the next, etc.
Omit ALL interactions between nonadjacent blocks. This is a NEW gate word.
An internal block QFT here means its H/phase CORE WITHOUT a local wire
reversal. Only the ONE final global reversal is applied. Recursive half
blocks use this same unreversed convention; (4.1) uses their physical bits.

For a high a-bit block with bits A_i (i=0 at its low physical end) and the
adjacent lower b-bit block B_j, the entire cross diagonal is

 exp(2pi i X Y/2^(a+b)),
 X=sum_i A_i 2^(a-1-i), Y=sum_j B_j 2^j.                 (4.1)

Indeed each product term has coefficient2^(j-i-b-1), exactly the original
angle. The high block has already received its Hadamards, the low one has
not. Cross diagonals commute with all remaining high-block gates on other
targets, so they can be moved to this boundary. This proves the usual
recursive decomposition directly from the specified gate word, without
assuming a Fourier primitive. Recurse within a block by splitting it in
half and applying (4.1) between its halves, down to one Hadamard per bit.

Implement each twiddle by the short multiplier of Section3, then SUBTRACT
its low a+b product bits modulo2^(a+b) from the TOP a+b bits of the ordinary
g-qubit positive gradient. The source gradient factors by bits; those top
bits are exactly gamma_(2^(a+b)). Subtraction kicks back the required
positive phase and returns that factor unchanged. Finally reverse product
and input staging. The source exact ripple adder and fixed Clifford+T
controls implement this with counted O(a+b) gates plus generation. Since
a+b<=2b_F<g, the factor always exists. On arbitrary non-gradient work this
is still an actual finite unitary with the stated scratch cleanup and its
actual reverse. On the independent exact-gradient event it implements (4.1)
exactly for ALL query/reference states, returning the catalyst uncorrelated.
There is no per-call rotation approximation or original-source inverse.

A t-bit internal QFT costs at most two half-size QFTs plus the short product
bound. Thus its core count is O(t^(8/5)(1+log(t+2))^4). There are O(q/b_F)
full/adjacent blocks; the full paid word and adjoint cost

 O(n L^(8/5)(1+log(L+2))^4)=O(nL^(7/4)).                 (4.2)

Here (log L)^4=O(L^(3/20)); this follows for example by maximizing
(log x)^4/x^(3/20) on x>=1. Constants are absolute, including the finite
initial range. No growing factor is absorbed into a fixed finite branch.

Every old retained pair r-k+1<=b_F lies within one block or adjacent blocks,
so is retained. Any newly omitted pair has r-k+1>b_F. Each input/output
pair has exactly one Hadamard path, giving a FLAT matrix entry of magnitude
M^-1/2 with phase equal to the sum of its retained binary pair terms. The
omitted positive phase sum is at most q2^-b_F, as in the source geometric
sum. Hence the NEW exact-gradient kernel U satisfies for EVERY x,f

 |U_(x,f)-M^-1/2 exp(2pi i f x/M)|
                         <=2pi q2^-b_F/sqrt(M).          (4.3)

This is a pointwise entry bound, not a constant operator-norm error applied
to an exponentially small peak. It is all the source base-column lower-bound
argument needs. The new word need not equal the old one on good or bad
catalysts; its own flat entries and (4.3) establish the necessary claim.

## 5. Banded short products for EVERY fresh coarse phase role

The coarse predicate needs W a/M mod1 for measured W and coherent q-bit a,
plus the source's fixed linear combinations with known pivots. The source
used q controlled p-bit additions, p=30+ceil(log2q). Replace ALL these fresh
coarse phase evaluations by the following actual finite word. Set

 P=p+8, t=largest power of two<=P/4, H=P+2t+2.

Use P-bit phase words and recompute interpolation/known-role constants at
this precision. Let W and a have binary bits w_k,a_j in[0,q). Pad their
high ends with zeros to whole t-bit blocks. If block bases are it,jt, retain
the pair precisely when

 (i+j)t<q and (i+j)t+2t-2>=q-P.                          (5.1)

For each retained pair compute its t-bit quantum-block times t-bit known
classical-block product by Section3. Put h=q-(i+j)t; then0<h<=P+2t<=H.
ADD that product times2^(H-h) modulo2^H into ONE reused H-bit accumulator,
using the exact register ripple adder, then reverse the short product and
staging. Higher integer bits are correctly ignored modulo1. All additions
and shifts are finite bit words with paid actual inverses. The final top P
accumulator bits are the actual phase word used by the interpolator. Keep
its remaining bits until their actual reverse cleanup; do not discard them
as if they were a reversible rounding primitive.

For each quantum block only a fixed number of coefficient blocks satisfy
(5.1), because t=Theta(P). Therefore there are O(q/t) short products, not
q^2/t^2. Their coefficient index has form floor(q/t)-i-d, with d in a fixed
bounded set. Visit query blocks consecutively and these coefficient blocks
by regular backward walks, using the persistent aligned pointers of Section3.
No arbitrary table of per-query addresses is loaded or copied. Per-product
external copies/additions use O(t+H)=O(L) core actions, dominated by (3.2).
Thus a full phase evaluation and its actual inverse cost

 O(n L^(8/5)(1+log(L+2))^4)=O(nL^(7/4)).                 (5.2)

Why it is accurate for EVERY basis a,W: a bit product contributes
w_k a_j2^(j+k-q) to the phase. Terms with j+k>=q are integers. Every term
with q-P<=j+k<q is retained by (5.1). Additional smaller terms may be
retained, which only reduces the omitted positive sum. For each fixed j,
the omitted geometric tail is <2^-P; summing q possibilities gives <q2^-P.
Truncating the final accumulator to its top P bits adds <2^-P. Circular
phase error is therefore at most(q+1)2^-P<q2^-p. This is a deterministic
pointwise bound including all padding boundaries, not a distributional or
average-case multiplication assumption.

Use the SAME finite trigonometric interpolator/rounding recipe as the source,
now at P bits; its fresh/exact role approximation allowance<=1/1024 still
holds, since the new phase error is smaller than the old admitted bound.
Known pivot words are computed by the same finite classical prescription
at P bits. Fixed linear phases 2a-u and2u-a use the original constant-size
signed phase-word arithmetic. The cubic score, common denominator, bounded
signed sums, threshold comparison and uncompute keep their source formulas
with these current phase words. In particular the canonical two-member
max/min comparison and bounded-score norm argument are unchanged as algebra,
while their deterministic numerical discrepancy is bounded afresh by the
same allowance. No equality to the old rounded predicate is asserted.

A complete constraint first computes these real phase words, interpolates
and accumulates its ell_i sampled records, applies its exact finite threshold
predicate, then reverses ALL actual arithmetic and phase words. It is a
unitary on arbitrary query states with zero helper restoration. The inverse
is the actual reversed circuit, not an inverse of any original source.
All labels/record indices are classical measured records; coherent a bits
remain controls in short arithmetic and never choose a classical address.

## 6. New base mass and the unchanged stopped weighted mechanism

We re-establish all numerical premises for the modified m and words.
Use the source label-only filter H(W)={W,-W,2W,-2W} modN, deleting low-order
or intersecting supports. Its good-generic event fails<=256m^2/N, including
composite/odd moduli; the proof assigns each deleted good to a DIFFERENT
deleted bad, so g_drop<=b_drop. A uniform m-subset has
Pr[b>m/3+m/1024]<=2^18/m. Good-label and fresh-axis score tails cost at most
exp(-m/2^21) and exp(-m/2^23). Their proofs expose good records first and
then arbitrary bad extensions; they do not condition on bad reports to
claim independent good labels. Since m>=2^100 these count/tail allowances
remain valid; since m<=old_m the generic collision allowance only improves.
The surviving true-oriented score is still>m/64 and r_f>=m/4.

Retain ALL cubic-score coefficients, including the constant, exactly as
in graded-source.md4. Nonconstant per-record L1 norm<=13/10, constant
second moment E_v|c0(v)|^2=(121/200)r_f, and J=next power of two>=4r_f
obeys J<=8m and, on the events above, J>=m. Compute their finite rational
approximations/angle words by the COMPLETE original streamed Machin/Taylor
and grid enumeration. Guard 4c0hat^2<=C^2J as an actual rational comparison.
Failure outside other events costs<16/C^2. No favorable anchor/guard
conditioning is used; every exceptional event is subtracted.

Prepare the SAME ordinary g-bit gradient by the source initialized mixed-work
translation test: all-even failure<=2^-80, label discrepancy<2^-115. This
is independent of originals, and on the complementary latent event the
catalyst is EXACT gamma. Charge this event ONCE for the whole computation.
Actual known coefficient gates retain their exact controlled-Ry scalar
correction, controlled-H construction, branch/index/flag layout and inverse
frequency lookup. No source-controlled preparation or arbitrary phase
primitive appears. Only the final Fourier word is replaced by Section4.

Coefficient error still gives ||htilde-h||_1<=2^40m/G<=2^-88m and
||htilde||_1<=2m, using the same g and smaller m. The true nearest dyadic
point x_s to M s/N differs in score by<5*2^-32m. The true-oriented m/64
score, this rounding, the NEW pointwise flat bound(4.3) and the unchanged
finite coefficient error show the actual flag0/zero-index numerator at
x_s has magnitude>=m/256, exactly the source triangle-inequality argument.
Therefore for a_s=x_s mod(M/2), actual base class weight is

 w_(a_s)>=m^2/(2^16*2J C^2 M)
          >=m/(2^68 M)>=1/D.                            (6.1)

This is the actual new base column on the exact-gradient event, not an
ideal uniform pivot or a small operator-norm hybrid.

The source Dirichlet full-secret-near versus FAR-class calculation uses
only the same coefficients, dyadic phases, cubic norm and deterministic
interpolator error allowance. Section5 preserves that allowance. Its exact
lower margin remains336899/12582912>1/64. The full original shadow bank
therefore satisfies E_far with additional failure<=2^-80 on the SAME count
event. For constraint i sampled AFTER its pivot, survival loss of a_s is
at most4*2^-a_i; sum_i4*2^-a_i<2^-30<2^-22. Graded lists ell_i and fresh
thresholds, index rejection caps and retained-endpoint independence remain
literal. Only fixed record/base strings and their real predicate words are
used in the following source weighted analysis.

For completeness, its mechanism uses actual starting weights w_a, chooses
three-call V_j=Vprev R0 Vprev^dag O_(P_j) Vprev, and bounds total surviving
FAR mass by the fresh random-threshold contraction rho. Before a NEAR visit,
a_s survives except for the just-counted fresh sketch error. With w_a_s>=1/D,
the normalized marked mass has the source lower threshold, and the
16-attempt doubling-clock/direct-or-Grover sampler succeeds in its stated
conditional range without knowing that mass. The mass-band sum bounds
expected debit until the FIRST PAST discrepancy by<2^16 sqrt(D). Markov
and the ACTUAL pre-attempt Budget=2^28 root give debit failure<=2^-12,
including the analytically first refused debit. D rho^Hmax<2^-64 follows
from n/9<=K<=n as before. Thus the full stopped coarse failure remains

 2^-22+2^-18+2^-24+2^-64+2^-12<2^-11.                    (6.2)

The complete derivation is graded-source.md8, reproduced in this archive;
its proof only needs (6.1), the fixed-predicate contraction/survival bounds
and the recomputed D,K/caps, all established here. No future cap survival,
correct answer or favorable base is conditioned on to invent a fresh law.
Every visited dyadic class is expanded, so a NEAR visit includes the actual
integer secret in the original champion list. That champion then supplies
the true class to the untouched original endpoint on E_int.

## 7. Full deterministic work, physical space and original samples

Put U*=n L^(7/4). Each ell_i-record constraint uses Section5 on every fresh
phase role, followed by the complete original finite interpolator, constant
number of role combinations, signed accumulations, comparisons, flags and
uncompute. Those additional per-record short-word/table actions are
polynomial(L) plus O(nL) label access, absorbed in U*. Index/cache fetch
and one-time long base formation per record are polynomial(L), not repeated
per primitive. Consequently

 cost(constraint i)<=C ell_i U*
                    <=C'(1+log2(i+1))U*.                 (7.1)

Lists have their ACTUAL ell_i, not ell_max at every early constraint; padding
the short accumulator width to the public maximum only costs O(log L).
All fresh and known candidate numerical roles have the deterministic
allowance proved in Section5. The actual record addresses are classical.

The base sparse forward-frequency mapping AND inverse index clearing cost
O(JnL), with all pattern/AND work. Since J<=8m=O(L^(3/4)), this is O(U*).
Coefficient/scalar/controlled-H words cost O(J(g+log J)L), metadata at most
O(JL^3); both are polynomial(L) and absorbed by U*. The new entire Fourier
word is O(U*) by (4.2), including final reversal. Reflection about the zero
query, excluding the catalyst as specified, has O(nL) cost. Thus BOTH the
complete new base and actual adjoint cost C U* on arbitrary inputs, including
wrong catalysts and failed flag sectors. No source preparation is inverted.

At root stage j there are at most128(j+1) current constraints. Summing (7.1)
gives complete predicate forward/reverse cost O(j(1+log2(j+1))U*). The
unchanged three-call generator therefore has

 c0<=C, c_j<=3c_(j-1)+Cj(1+log2(j+1)),
 c_j/3^j<=C+C sum_(t>=1)t(1+log2(t+1))/3^t<C'.           (7.2)

The series is bounded by sum(t+t^2)/3^t=9/4, since log2(t+1)<=t. The full
source finite(level,direction,position) recursive generator uses immutable
constraint prefixes and actual reverse words; it does not copy descriptions
per elementary gate. Its O(n log n) classical stack fits SCn^2. A short
arithmetic subroutine enters the local descriptor generator of Section3;
outer level/base work is paid per call, not attached afresh to each local
primitive. Full counter, sampler coin, measurement/reset, same-predicate
classical verification and reflected zero-word work fit C B A_j U* for an
attempt. Precompute stage integers3^j and shift by the power-of-two B for
actual debit B A_j; comparison/subtraction/copy uses O(nL) paid work. No
n-bit general product is needed inside an attempt. All larger public tables
are paid polynomial setup, not secretly omitted repeated arithmetic.

The PRE-ATTEMPT guard therefore bounds EVERY real branch by

 T_attempts<=C U* sum_admitted B A_j
            <=C U* Budget
            =O(2^(n/2) n L^(11/8)),                      (7.3)

because root=O(sqrt(M/m))=O(2^(n/2)L^(-3/8)). This is deterministic token
accounting, not an expected-time assertion. Equation(6.2) alone uses the
stopped expectation to prove that the actual cutoff rarely obstructs success.

All remaining work is polynomial in n: original acquisition/extraction and
shuffle, m-subset/filter, bounded streamed coefficient/angle enumeration,
precomputed local descriptor tables, accepted pivot/list caches, integer
class expansion/full-shadow tournament, original endpoint, initialization
and output-first cleanup. Angle search is streamed O(G^2 poly(g)) per
coefficient, G=O(q^2), with no G^2 allocation. All indices and arithmetic
loops have the original finite caps or smaller m-dependent caps. These
polynomial costs are uniformly absorbed by (7.3), including finitely many
initial exceptions via an absolute outside constant. All discarded and
failed work is counted.

Original classical labels/records and both N/M-prefix banks occupy O(n^2).
The new m labels/frequencies cost O(mn), angle words O(mg), and extra short
multiplier descriptions/work counters O(L^(8/5)polylog L), all within O(n^2).
The outer stack O(n log n), lists/pivots, caches, integer/trigonometric
scratch and every inactive reservation also fit the original O(n^2) pool.
The known classical coefficient blocks are read into short local basis
registers; there is no coherent-addressed classical memory primitive.

ENTIRE SQ is O(n): Q=O(n) accessible retained rows plus shared extraction/
position/source pool, q frequency/query bits, original O(n) predicate/
reflection/flag helpers and g catalyst; local staged inputs, arithmetic DAG,
accumulator and their clean padding occupy O(L^(8/5)polylog L)=O(n). The
last inequality holds uniformly on n>=2^4096 by elementary exponential
versus power comparison, with absolute constants. Reserve the whole local
window, including all unused cells, not just nonzero or coherent scratch.
Every product frees its scratch by the actual reverse; recursion never
allocates multiple query or endpoint banks. Original raw source wires and
all fixed padding are included. Endpoint pools are reused after coarse
work is released. Thus the SAME configuration has SCn^2 and SQn jointly.
This is the ordinary classical implementation, not a basis-bank space
relabeling.

Exactly Q=3*2^40(n+32) original calls occur before any new abort, on EVERY
branch. Known ancillas, ordinary gradient initialization, finite arithmetic,
classical records, catalyst shifts and actual reverse words are not original
samples. All source/instruction/address/gate/measurement/init costs have
been counted. No QRAM, source inverse/control, extra purification, free
integer operation, uncharged circuit list or arbitrary phase is supplied.

## 8. Unconditional success and the five exact declarations

Combine the SINGLE unconditional good-label comparison<=2^-62 with the
original count and integer-score events. The NEW m/count/generic/two-tail/
anchor/constant-guard exceptional total remains

 2^18/m+256m^2/N+exp(-m/2^21)+exp(-m/2^23)+2/N+16/C^2
                                                       <1/4096.

Indeed m>=2^100 controls the reciprocal/tails, m<=old_m controls collisions,
16/C^2=2^-44, and N>2^(n-1) with n>=2^4096 controls denominators. Capped
subset/anchor samplers add<2^-254, new dyadic score event<=2^-80, independent
coarse catalyst<=2^-80+2^-115. All new exceptions total<1/1024, exactly the
source allowance. Fourier/coefficient and phase-interpolation errors are
deterministic pointwise bounds already used for base mass and score margins;
they are not extra stochastic events or per-query trace-distance hybrids.

For each fixed record/base string satisfying these properties, the actual
new words satisfy stopped coarse bound(6.2). A NEAR visit expands to the
actual secret's original integer class and E_int elects it. Coarse work
uses only measured records and independent ordinary work, never a retained
row. Subtract its unconditional failure from the original reference endpoint
supplied the true class. Never condition that endpoint's parity law on
coarse correctness, good labels, count survival, Fourier preparation or any
future cutoff. The reference endpoint baseline91/128 minus original combined
losses<3/128 (with (6.2) replacing the old coarse term), minus the new<1/1024,
is STRICTLY>2/3. The original source proof includes malformed rows, wrong
labels, all sampler/work errors, exact output and release. Linearity covers
fixed-B mixtures and arbitrary allowed references. The complete finite
SPTS-JM branch has success>11/16, so all N>=2 qualify with the SAME promise.

Equations(7.1)-(7.3), simultaneous physical allocation and exact original
sample count establish all four original structured objects jointly on
EVERY branch for this modified physical algorithm. For n>=2, log2T has
representative n/2+log2n+(11/8)log2log2n; thus its exact growth index is1.
Polynomial classical/quantum/sample representatives have index0. The
fractional expression is EXACTLY1/3 under the literal context of Section1,
not an iid per-copy error rate or a maximal-tolerance assertion. The change
from L^(3/2) to L^(11/8) is an unbounded factor L^(1/8), with new circuits
and a new literal subsample configuration proved together. Earlier source
acceptance, simulations and numerical checks are not mathematical premises.
