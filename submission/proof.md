# WFP3: graded-confidence weighted Fourier pivots

For every N>=2, s in Z/NZ and n=ceil(log2N), ONE uniform physical algorithm
recovers the ENTIRE s with unconditional success strictly greater than2/3.
Jointly on EVERY branch, including all failed and discarded work,

 T=O(2^((1/2)n)n(log2n)^(3/2)), SC=O(n^2), SQ=O(n),
 Q=3*2^40(n+32) EXACTLY, epsilon(n)=1/3.                    (0.1)

The four exact growth indices are1,0,0,0. The logarithmic representative is
for n>=2; the same finite n=1 program has bounded absolute costs. The factor
1/2 multiplies n. This is not an expected-resource claim. It uses the inherited biased starting unitary and WEIGHTED hitting analysis.
The present changes are stated in Section0; the old
uniform-pivot proof is still not applied to biased amplitudes.

## 0. Immediate source, current program and evidence scope

The immediate material source is WFP2, submission
8921a73c-be6c-44ed-8be2-96379b30127f, commit
74e6ba0ae971d02202b28e9dd7a02ef3fd0c707c. Its COMPLETE current main is
profile-source.md, SHA-256
bf2c3430cb60d48220f2d165eca9dafd01b16ea742afb12d87e888b00019acea.
Its four complete algorithmic helpers are copied unchanged as joint-source.md,
spts-source.md, sources/RQ-SPLIT-proof.md and pc-controlled-source.md. Their
hashes are respectively
f912b269b63e66803912eed6d517ca795731d5439a6616553493d7eba98e8d7f,
373939d8a0439acd480aad17f85ab9067d474f995a4c720f43af6a2f42bf409e,
2952a6f52b94dfa9d0e03471b9e7611f185db198dbc9274639dbc03ce7d1ca80,
bd862728628c582bf5d4f2c6592e2e5a8a59397da63dbfc0a89097e47d99a2f6.
The older weighted-source.md mentioned in the source's historical Section0
belongs to THAT source archive, not this one. It is a redundant prior-profile
main; no lemma below requires it. The complete selected current proof and
all its algorithmic helpers are present here. Historical source comments
about its own archive do not specify this archive's contents or parameters.

The current WFP3 program changes THREE linked choices: graded confidence
ell_i for accepted constraint i, block implementation of the truncated QFT,
and m=2^100 L with ALL dependent integer caps and layouts recomputed. The
whole changed program and joint proof are below. Graded confidence improves
the weighted recursive COST sum, while still summing all survival tails.
It does not replace a worst-case cutoff by an expectation. The block QFT
implements precisely the source kernel on its exact-catalyst event, using
ordinary register adders rather than an arbitrary phase primitive.

The source carries WFP, SPTS-JM, PCT, peer0xplemonade SPTS1, RQ/FNS and earlier
credits; those remain in the copied members. No separately imported ancestor
feature or independent authorship of inherited mechanisms is claimed. Old
adaptive ModelM passages remain historical: joint-source.md supplies the
fixed-original-joint input statistics used here. Earlier acceptance, replay
scripts and numerical checks are not mathematical premises.

## 1. Fixed input, unchanged acquisition and original reference endpoint

The fifth structured object uses EXACTLY the context

"Among the Q acquired copies, an adversary fixes a set B of at most floor(epsilon(n) Q) malformed positions, possibly depending on N and s. The joint state is arbitrary subject to its reduced state on all other positions being exactly rho_s^{tensor (Q-|B|)}. Malformed systems may be correlated or entangled with each other and with other systems subject to that marginal promise. No source control, purification access, or preparation inverse is supplied."

The whole original bank is fixed before passive release in fixed order.
It cannot be replaced or acted on in response to an outcome. Conditional
unread-state changes after earlier measurements are allowed. Unread passive
source-held state is excluded from accessible allocation by the challenge
rule. Arbitrary inaccessible reference and convex mixtures of fixed-B
components are included. No conditionally fresh-good or independent-bad
premise, purification access or source control/inverse is assumed.

Run EXACTLY the source acquisition/compression and late private split:

 k=3*2^22(n+32), Q=2^18 k,
 m_R=Q-k, r_R=m_R/3, Delta=ceil(sqrt(16k)),
 R_ret=r_R+Delta, g_ret=m_R-R_ret.                          (1.1)

Each of the Q raw registers runs the same collective EXTRACT with J_e=n+4,
h=ceil(log2(2^64 Q(n+5))) and F=2^21 h. Apply the same row X, discard/reset
position and probes and retain reported W in[0,N). After ALL deliveries,
the same bounded Fisher-Yates subset sampler selects k rows; only these are
measured in fresh private X/Y axes. Retain every label, sign Z and basis beta.
The m_R other rows remain untouched by ALL coarse operations below.
All original source counts, shuffle caps and malformed numerical branches
are unchanged. Every branch acquires exactly Q, even a subsequent abort.

We recall the full-reference consequences PROVED in joint-source.md Sections2-6.
Discarding position makes the complete extraction channel diagonal in hidden
Fourier labels, including the scalar padded block. There is an unconditional
comparison process changing only good reports to their hidden labels, with
probability/trace-distance loss <=2^-62. In that process all good hidden labels
are independent uniform in[0,N); conditional on those labels the good rows
are pure products and factor from the arbitrary remaining extension. Bad
records/states may depend arbitrarily on the good labels. They need not be
independent. In particular conditioning on bad reports is NOT used to claim
uniform good labels. All later algorithms are channels, so the single
unconditional comparison loss covers the present algorithm too.

The private split/count event fails with probability <=1/64. On it the shadow
bad fraction is <=1/3+1/1024 and retained bad count <=R_ret. The original
integer full-shadow score event E_int fails, in addition, with probability
<=2^-80. On E_int the original true INTEGER class wins every needed full
comparison, in both source fresh/exact roles, with margin1/64. This event
is about the measured records and covers adaptive lists of later candidates.

With the true original integer class supplied, the original endpoint has
unconditional reference success >=91/128 before the source's listed losses.
For even N it uses the unconditional good-label parity binomial extension,
not a law conditioned on a correct coarse answer; for odd N the class is
already the whole secret. We will preserve its input retained bank and
subtract coarse exceptional-event probabilities, as the source proves.
The exact endpoint uses its original ordinary gradient and corrections.

## 2. Uniform finite branch and exact public parameters

If n<2^4096, execute the COMPLETE SPTS-JM algorithm of joint-source.md and
return its result, with all Q sources and its noisy-input success guarantee.
This includes its own bounded n<64 branch, not a clean-only replacement.
The ratio between its old n(log n)^3 and the claimed n(log n)^(3/2) is bounded
on this fixed finite range, so it changes only an absolute outside constant.
No state-dependent advice or unreviewed finite solver is used.

For n>=2^4096 put

 L=ceil(log2 n), q=n+32, M=2^q,
 m=2^100 L, A=2^20, C=2^24,
 b_F=60+ceil(log2 q), g=128+2ceil(log2 q), G=2^g,
 D=ceil(2^80 M/m).                                        (2.1)

Here m is a NEW shadow-subsample size, not the retained-bank m_R. All roots,
ceilings and powers use integer arithmetic. Choose K as the largest j>=0
with (64q3^j)^2<=D; let A_j=3^j, Hmax=128K and root=ceil(sqrt(D)). Set

 a_i=32+2ceil(log2(i+1)), ell_i=2^17 a_i, 1<=i<=Hmax,
 ell_max=ell_Hmax,
 r_idx=ceil(log2(2^24 Hmax ell_max)), Budget=2^28 root.      (2.2)

Constraint i uses EXACTLY ell_i entries and its own fresh threshold. The
index rejection cap is the common r_idx. No allocation or rejected-index
loop grows beyond the public Hmax ell_max envelope. Accumulator widths and
threshold products use that constraint's actual ell_i, padded to a common
public maximal width if convenient. The threshold grid itself is unchanged.

For each stage j let Bcap_j be the least power of two with Bcap_j A_j>=16root.
These are public fixed caps, independent of source state, records and outcomes.
Use the source's exact 16-attempt doubling-clock/direct-or-Grover sampler,
with these values. Its current root stage is j=floor(r/128) at accepted count r.
Its pre-attempt debit is B A_j, checked BEFORE preparing query work. A refusal
ends coarse sampling; original success is not assumed after that refusal.

Some elementary bounds will be useful for ALL n in this branch. With
L>=4096 and n>=2^(L-1), log2 m=100+log2 L. Hence m<=k, D<=2^(2n),
and m*4096q^2<=2^(n/2+112). The latter and 3^(floor(n/8))<=2^(n/4) imply
K>=floor(n/8)>=n/9, while D<=2^(2n) implies K<=n. These inequalities follow
at L=4096 with enormous slack and persist when L increments: the exponential
2^(L-1) dominates 2L+log2L+O(1), whose consecutive increment is <5.
In particular Hmax=O(n), ell_max=O(L), m=Theta(L), g,b_F=O(L), and
m n+m^2+m g=O(n^2). Also g>=b_F+1. The bounds reserve fixed capacities for
all padded arrays, compiler fields and bad-input branches, not observed use.

Choose a uniform m-subset T of the k shadow positions with an additional
partial Fisher-Yates sampler. Cap each rejection at ceil(log2 k)+256 trials.
Because m<=k its total failure is <=2^-256 by the same rejection calculation.
In the uncapped comparison T is a uniform m-subset of ALL Q positions, since
the original k-subset is uniform; we use that law without conditioning on
sampler survival and subtract both cap discrepancies. Pick an independent
uniform anchor v in[0,N), with n+256 rejection trials, cap failure <=2^-256.
If any such preparation cap/explicit abort below fires, clear all work and
output0. The Q acquisitions have already occurred.

The new coarse universe is dyadic ANTIPODAL CLASSES

       a in[0,M/2), members a/M and (a+M/2)/M.             (2.3)

It is used even when N is odd. The Fourier query has q frequency bits x;
class a is its low q-1 bits, and its high bit is an unused member label.
The predicate is identical on both high-bit values. Additional preparation
flag/index junk is always invalid. No coherent computation of round(Nx/M)
or multiplication of two n-bit query words is performed.

## 3. Filtered labels and a true-oriented subsample score

For a reported label W let H(W)={W,-W,2W,-2W} modulo N. From T delete every
record with 0 in H(W) or |H(W)|<4, and every record whose H(W) intersects
another record's H. This depends ONLY on labels, not axes, signs or v.
Compare every pair if needed, using bounded ordinary bit arithmetic; retain
only the m original records, masks and current pair fields, not a large
unbounded graph. Let r_f be the remaining record count. If it is zero abort.
Remaining H supports are disjoint. Since M>=8N, the actual integer frequencies
+W,-W,+2W,-2W modulo M are also nonzero, distinct within a remaining record
and disjoint across records. All labels are in[0,N) by the total decoder.

Here is the needed adversarial filtering argument. Define the GOOD generic
label event: no good label in T has additive order at most4, and no two good
labels U,V obey aU=bV modulo N for a,b in{-4,-2,-1,1,2,4}. Its failure is
<=256m^2/N: each equation for two independent uniform labels has probability
<=4/N, and at most6 residues have order<=4. This includes order THREE; merely
checking 4U!=0 would not suffice. On this event good-good support intersections
are absent. One bad support cannot intersect two good supports, because
alpha U=beta W and gamma V=delta W with coefficients in{+-1,+-2} imply
(alpha delta)U=(gamma beta)V, a forbidden good-good relation. This proof uses
multiplication only, so is valid with zero divisors and nonprime N.
Thus EVERY deleted good record can be assigned to a DIFFERENT deleted bad
record: good records are not low-order, and each must neighbor a bad record
which itself is deleted. Consequently g_drop<=b_drop. Remaining r_f>=m/4
whenever the original subsample bad count is <=m/3+m/1024.

For phases t,u in R/Z define R_t(W)=cos(2pi Wt)X+sin(2pi Wt)Y and

 M_tu=[11(R_t-R_u)+R_(2t-u)-R_(2u-t)]/20.

As proved algebraically in the source, M_tu=(7B-2B^3)/5 for B=(R_t-R_u)/2,
so ||M_tu||<=1 for EVERY W, every t,u and arbitrary row. For a measured record

 G_j(t,u)=Z/10 [11(cs_beta(Wt)-cs_beta(Wu))
                       +cs_beta(W(2t-u))-cs_beta(W(2u-t))]. (3.1)

Here cs_X=cos(2pi*), cs_Y=sin(2pi*). Private fresh axes/signs give conditional
mean Tr(row M_tu) in[-1,1]; each realized G has magnitude<=2. For a good row
and t=s/N, uniform hidden W gives mean11/20 for an anchor v/N outside the
true original antipodal class, by exact character orthogonality as in RQ5.

The m-subset bad count b satisfies P[b>m/3+m/1024]<=2^18/m by the finite
population variance bound Var<=m/4. For fixed T,B and false anchor, let f_j
be the good row's axis-averaged score BEFORE filtering, as a function of its
hidden W. Those independent [-1,1] variables have mean11/20. Their sum is
at least(11/20)(m-b)-m/1024 except with exp(-m/2^21) probability. No bad
report is conditioned on to assert this independence. After exposing labels,
bad labels may depend on them, but removing a good record reduces this
conditional mean by at most1. Every remaining bad row has conditional mean
at least-1, and g_drop<=b_drop. The remaining total conditional mean is at
least the unfiltered good sum minus b: the removed bad positions compensate
for the possible removed good means.

Now expose fresh axes/outcomes after that label-only mask, and fix v. This
is the same joint law as sampling T and v after those axes, because their
private coins are independent. Conditional on good labels the good rows are
pure products and factor from the other systems, including bad reports.
Expose good outcomes first, then the arbitrary entangled bad rows. Bounded
conditional log-mgf estimates, with range width at most4, show that the
remaining actual sum is no less than that conditional mean minus m/1024
except with exp(-m/2^23). This is an unconditional bound averaged over the
labels; it does NOT claim that post-filtered good labels are uniform.
On the count/generic/tail events the filtered true-oriented sum is therefore

 (11/20)(m-b)-b-2m/1024
 >=[1/30-31/(20*1024)-2/1024]m >m/64.                    (3.2)

An anchor in the true original class has probability<=2/N and can be charged
as failure. Both exponential tails above are <2^-80 for m>=2^100.
All these estimates permit bad-good entanglement and adversarial dependence
of bad labels on good hidden labels; they use fresh private axes after labels.

## 4. Sparse cubic Fourier coefficients and the constant term

For a surviving record set d_beta=1 for X and -i for Y, alpha=2pi Wv/N.
Its score G_j(t,v/N) as a function of t has coefficients

 c_(+W)= Z[11d_beta-conj(d_beta)exp(-2i alpha)]/20,
 c_(-W)=conj(c_(+W)),
 c_(+2W)=Z d_beta exp(-i alpha)/20,
 c_(-2W)=conj(c_(+2W)),
 c_0=-11Z Re(d_beta exp(i alpha))/10.                     (4.1)

Summing these times exp(2pi i f t) equals (3.1) exactly. Nonconstant
coefficients have magnitude<=3/5 or1/20, and their per-record L1 sum is<=13/10.
They are disjoint across records by Section3. The total constant c0 is retained:
dropping it would invalidate the one-third mean bound.

The anchor was independently uniform in Z_N. Conditional on ANY filtered
labels, axes and signs, those labels have distinct nonzero character pairs
{W,-W}; hence exact finite character orthogonality gives

       E_v |c0(v)|^2=(121/200)r_f <=(121/200)m.            (4.2)

This holds for arbitrary actual records, not only good ones. The filter did
not use v. Let J be the next power of two >=4r_f. Compute c0 and the other
coefficients by the source Machin/Taylor rational recipe at precision ensuring
|c0hat-c0|<=2m/G and individual nonconstant error<=1/G. The arithmetic is
ordinary finite bit arithmetic. Abort if 4c0hat^2>C^2 J, an EXACT rational
comparison. On the count/generic event J>=m. If this guard fails, then
|c0|>(C/4)sqrt(J), since C>=4 and 2m/G is negligible by (2.1).
Equation(4.2) and Markov bound its probability by <16/C^2. No conditioning on
a favourable anchor or guard acceptance is used elsewhere; we subtract this
exception. Always J<=8m.

Thus outside the listed bad events the coefficients are sparse, their
constant term is controlled, and their true sum exceeds m/64. Concentration
and the anchor bound are different events and need no mutual independence.

## 5. An ordinary exact gradient catalyst and finite coefficient gates

Before the new coarse search prepare an ordinary g-qubit positive-exponent
Fourier work state gamma=G^-1/2 sum_y exp(2pi i y/G)|y>. Use EXACTLY the
source RQ8.1 procedure for known modulus G: in at most80 attempts produce
I/G using fair measured Hadamard bits and forget that seed, run the fixed
translation label instrument with h_aux=ceil(log2(2^124(g+5))), reject even
estimates, and for an odd estimate u apply the exact permutation y->u*y modG
using known controlled additions and its inverse cleanup. No original DCP
source is called. The nondemolition eigenlabel proof gives all-even failure
<=2^-80 and total estimation discrepancy<2^-115. On the complementary
latent event the accepted work state is EXACTLY gamma, independent of the
original input. This event is used ONCE for the entire coarse computation,
not charged per repeated query. The original input law is unchanged upon
this independent work-state comparison.

On exact gamma, ADD a on its known register multiplies its state by
exp(-2pi i a/G). Thus a positive phase exp(2pi i k/G) conditional on some
query bits is implemented by ADD(-k) conditional on their computed AND.
An O(g)-gate controlled ripple word and clean AND scratch implement this
exactly, returning gamma uncorrelated for ALL control superpositions. Its
actual adjoint is the inverse word. The catalyst is excluded from the
all-zero query reflection and is reused unchanged in EVERY coarse call.
It is released before using the ORIGINAL endpoint gradient; that separate
original endpoint work/failure remains accounted by its source proof.

For a desired complex flag amplitude a in the unit disk, prepare its real
magnitude by Ry(theta), theta=2arccos|a|, then apply arg(a) phase to flag0.
All angles are rounded to multiples4pi/G for theta,2pi/G for phases. The
half-angle scalar below is then also an integer G-phase. The actual controlled
word is explicit, with no free rotation primitive: chronological S^dag,H,
P_theta conditional on the specified index, H,S, followed by the scalar
exp(-i theta/2) conditional on that index. Off that index the word is identity;
on it, S H P_theta H S^dag exp(-i theta/2)=Ry(theta).
The scalar correction is essential. All phases use exact gradient additions;
pattern ANDs and their scratch are uncomputed. Additional phase on flag0
gives the chosen complex coefficient. Controls may include branch/index
bits; none are classical measurements of the query.

The required finite angle selection is uniform and counted: enumerate the
G-spaced angle pairs with g-bit counters, evaluate the rational Taylor
cos/sin bounds, and retain the pair minimizing distance to the desired
coefficient to the fixed precision. Stream this enumeration with O(g^2)
scratch and keep only the chosen O(g)-bit pair per coefficient, never a G^2
array. The polar grid covers the unit disk to O(1/G); this also covers zero
magnitudes and endpoints, for which theta=0 or pi can be used EXACTLY.
Its O(G^2 poly(g)) setup per coefficient is polynomial in n, since G=O(q^2)
up to fixed constants. Desired constant amplitude uses c0hat/(C sqrt(J));
its magnitude is at most1/2 by the guard. All square roots/divisions can be
interval-computed or included in the same finite grid-distance comparison.
Individual coefficient-amplitude error is conservatively <=16/G.

A small controlled-H, needed for a conditional uniform index, is exact:
with V=S H T H S^dag one has V Z V^dag=H. The word V^dag,CZ,V on the target
therefore implements CH and is identity off its control; actual global phases
cancel. This is the selected PCT actual-word construction. No arbitrary
controlled preparation oracle or undocumented rotation library is assumed.

## 6. The flagged sparse starting UNITARY and flat truncated Fourier transform

Let f_j list the 4r_f distinct nonzero frequencies (4.1) modulo M, j<4r_f,
with chosen coefficients c_j. Allocate a branch bit b, log2 J index bits,
a good/failure flag z, q frequency bits and reused AND scratch, all zero.
Apply H to b and H to each index bit controlled on b=1. Thus b=0 has index0,
and b=1 is uniform on[0,J). With the coefficient gates of Section5 make
flag0 amplitude c_j/C on b=1,j<4r_f, exactly0 on b=1,j>=4r_f, and c0hat/(C
sqrt(J)) on b=0,index0. Invalid-index flag0 is suppressed EXACTLY by Ry(pi),
not by an approximate gate. Define arbitrary unitary blocks on unreachable
b=0,index!=0 states as needed; they do not affect this starting column.

Compute frequency f into its zero register by known pattern lookup from
(b,j): zero for b=0, f_j for valid b=1, and zero for invalid j. This is XOR
into f, an exact permutation on all inputs. Conditional on flag0, XOR the
inverse lookup of f into (b,j): f=0 has code(0,0), f=f_j has code(1,j).
The valid frequencies are unique, so on flag0 all branch/index bits become
zero. On failure the index may remain junk; it will NEVER be marked.
These XOR permutations are unitary on arbitrary inputs and their reverse
words exist. No postselection, successful-flag measurement or reset occurs
inside the preparation. Pattern tests use O(q) or O(log J) clean scratch,
reused rather than a coherent addressed table.

Now apply the source's truncated positive QFT kernel, with a NEW block
implementation. Its reference gate word is: r=q-1 down to0, H_r then phases
between r and k<r of angle2pi/2^(r-k+1), retaining r-k+1<=b_F, and finally
wire reversal. Define w=min(b_F,r+1). After H_r, let the UNCHANGED lower
query wires form the quantum integer

 y=sum_(d=1,...,w-1) f_(r-d) 2^(w-d-1), 0<=y<2^(w-1).

The absent top addend bit is a clean zero; for w=1 skip the block. Conditional
on query wire r=1, SUBTRACT y modulo2^w from the TOP w bits of gamma_(2^g).
The exact ordinary gradient factors by bits; its top w bits are precisely

 2^(-w/2) sum_z exp(2pi i z/2^w)|z>.

Consequently subtraction returns this factor unchanged and kicks back
exp(+2pi i y/2^w). This is exactly the product of all retained controlled
phases after H_r. It holds by linearity for arbitrary entangled query input;
there is no measurement or assumption that the lower wires are known bits.
They are unchanged addend wires and exclude target r. Since g>=b_F+1, this
factor always exists. All other gradient bits remain untouched.

Use the complete source's linear reversible REGISTER ripple adder (RQ6.1),
with its actual inverse for subtraction, controlled on r by controlling every
primitive. Extra controls on NOT/CNOT/Toffoli use fixed exact Clifford+T AND/
Toffoli words and clean helpers, so O(w) gates and O(w) reusable scratch still
suffice. The clean top addend bit is an explicit allocated wire. Full carries
and scratch are reversed, even on arbitrary non-gradient work inputs. The
ADJOINT reverses these new complete words. This is not inversion of a source.

On the independent exact-gradient event the new word is EXACTLY the reference
QFT on the query and returns gamma uncorrelated. On other gradient components
the new word need not equal the reference word: their single preparation
failure bound is charged once in Section10. All words/allocations/cutoffs are
still bounded there. No per-query error hybrid or unpromised catalyst event
is used. Its ideal-event matrix entries are therefore unchanged:

 U_(x,f)=M^-1/2 exp(2pi i sum_(j+k<q, q-j-k<=b_F)
                                      f_j x_k 2^(-(q-j-k))). (6.1)

There is one Hadamard path per input/output pair, so EVERY entry has modulus
M^-1/2. The omitted part of the full binary product phase has magnitude
<=q 2^-b_F; hence

 |U_(x,f)-M^-1/2 exp(2pi i f x/M)| <=2pi q2^-b_F/sqrt(M).  (6.2)

This is a POINTWISE flat-entry bound, not a constant operator-norm error
asserted to preserve exponentially small peaks. It follows directly by
summing each omitted bit-pair term and |exp(iu)-exp(iv)|<=|u-v|. The retained
word is unitary by its gate construction, including the bit reversal.

Call this full known preparation V0. Its actual reverse word is V0^dagger.
The success-flag/zero-index sector has amplitudes

 a_x = (sum_f htilde_f U_(x,f))/(C sqrt(2J)),               (6.3)

where htilde denotes the ACTUAL chosen coefficient amplitudes, with constant
coefficient scaled by sqrt(J). Uniform polar errors and Taylor errors give
||htilde-h||_1 <=2^40 m/G <=2^-88 m. The constant guard and m>=2^100 imply
||htilde||_1<=2m. Neither this calculation nor the circuit normalizes h or
assumes a favourable flag outcome.

Let x_s be a nearest integer to M s/N, modulo M, and a_s=x_s mod(M/2).
For each record the derivative of (3.1) in its first phase argument has
magnitude <9N. Thus its sum at x_s/M differs from that at s/N by at most
(9N/(2M))m<5*2^-32m. Equations(3.2),(6.2) and the coefficient error above
show that the actual successful-sector numerator after removing M^-1/2 at x_s has magnitude
at least m/256. Therefore its individual basis probability, and hence
aggregate class weight w_(a_s), obeys

 w_(a_s)>=m^2/[2^16 *2J C^2 M]
          >=m/(2^20 C^2 M)=m/(2^68 M)>=1/D.              (6.4)

This lower bound is on the actual starting unitary on the independent
correct-gradient event. It introduces no per-query approximation loss.

## 7. True dyadic class versus FAR classes, then exact integer expansion

A dyadic class is NEAR if one of its two member phases has circular distance
<=A/N from s/N. Otherwise it is FAR. The fixed a_s above is NEAR. We prove
its actual-secret-near member beats BOTH members of every FAR class in the
full shadow bank with the required score margin.

For delta in R/Z let D_N(delta)=N^-1 sum_(W<N) exp(2pi i W delta).
The geometric sum gives |D_N(delta)|<=1/[N|sin(pi delta)|]<=1/[2N||delta||].
For true phase t=x_s/M, eta=t-s/N has |eta|<=1/(2M). The good-label expected
score against u is exactly

 [11(Re D_N(eta)-Re D_N(u-s/N))
   +Re D_N(2t-u-s/N)-Re D_N(2u-t-s/N)]/20.               (7.1)

For a FAR member u both its distance from s/N and from s/N+1/2 are >=A/N.
Thus the three cross terms are bounded by 1/(2A),
1/[2(A-2^-32)] and1/[2(2A-2^-33)], respectively. Also
Re D_N(eta)>=1-pi2^-32 by the elementary cosine Lipschitz bound.
Substitution with pi<22/7 and A=2^20 proves (7.1)>=11/20-1/4096.
These inequalities include wraparound and arbitrary odd/composite N.

Use the same good-first arbitrary-reference moment bound as joint-source.md:
good rows have that mean and product good output marginal; bad conditional
means are >=-1 and realized scores are bounded. On the SAME original shadow
count event, a tail k/256 costs at most exp(-k/(18*2^16)). Union over all
M=2^(n+32) member phases is still <2^-80, since k/(18*2^16)>10(n+32).
No conditional-good freshness after bad reports is used. The pointwise
interpolator/window error is the source's <=1/1024 in all fresh/exact roles.
The exact resulting lower margin is

 (11/20-1/4096)*(2/3-1/1024)
       -(1/3+1/1024)-1/256-1/1024
       =336899/12582912 >1/64.                            (7.2)

Call this record-measurable property E_far. The original integer score event
E_int is also kept. The original count failure is charged ONCE, not once
per score event. A true member row suffices in the coupled max/min comparison
in either canonical orientation, exactly as the source proves.

Coarse sampling uses the source's canonical coupled comparison on the TWO
members of (2.3). Fresh candidate phase words use W a/M with precision
p=30+ceil(log2 q); packed source word is simply W*2^p in q+p bits. Known
pivot exact words are computed classically. Antipodal member adds the same
parity bit, and the fixed interpolator, common denominator, signed sum width
and role discrepancy proofs apply literally to these phases. The original
N-prefix words are ALSO retained for the final integer tournament.

We analyze coarse sampling only until its FIRST visit to ANY NEAR class.
Before that visit every stored pivot is FAR, so (7.2) preserves the fixed
a_s except for a fresh-sketch survival error. For constraint i, the same source Hoeffding margin
3/256 bounds each required member failure by
exp(-ell_i/131072)<=2^(-a_i). Its list is sampled AFTER its pivot, so this
is a sequential conditional bound for every past before the first NEAR visit.
At most four orientations are charged. Since 2^(-a_i)<=2^-32/(i+1)^2,

 Pr[some such survival error] <=4 sum_(i=1,...,Hmax)2^(-a_i)
                 <4*2^-32 sum_(i=1,...,infty)(i+1)^-2
                 <2^-30 <2^-22.                          (7.3)

The last series is <1 by 1/(i+1)^2<=1/[i(i+1)] and telescoping, strictly.
No union over all possible pivot VALUES is taken, and no future event is
conditioned on. The stronger new bound fits the old conservative allowance.
This does not assert that a_s wins against another NEAR class; encountering
one is already the desired stopping event.

After sampling, do NOT elect a dyadic champion. For EACH accepted dyadic
class a (including the last saved pivot if its list is incomplete), compute
CLASSICALLY the two centres floor(Na/M) and floor(N(a+M/2)/M). Add all integer
residues within offsets[-A-2,A+2] of either centre, modulo N. There are only
O(A) per visited pivot, a fixed constant. If a was NEAR, one of these integers
is exactly s: circular distance<=A/N means the floor differs by <=A+1 modulo N.
Run the ORIGINAL full-k-record integer-class champion on this expanded list,
with its original N-prefix/known exact roles. If empty use class0. On E_int,
if any NEAR class was visited, the true original integer class is present
and wins the tournament. Finish with the UNCHANGED original endpoint on the
untouched rows. No coherent N times query multiplication is hidden in a leaf.

## 8. Weighted contraction, recursive preparations and stopped hitting cost

Fix the full actual records, filtered data/anchor, all finite coefficient
words and an exact catalyst. The preparation V0 is now a fixed unitary.
For each dyadic class c let w_c be its TOTAL base squared amplitude on the
markable flag0/zero-index sector, summed over its two member bits. All junk
is invalid. Weights can be zero or arbitrarily small; only w_(a_s)>=1/D is
needed on the good base event. Their total is at most1.

Use the source's exact nested contender sets S_r: classes different from
accepted pivots that win every stored fresh-list comparison. The fresh list
is iid uniform shadow indices, sampled AFTER its pivot, with at most r_idx
rejections per index. It and the uniform 16-bit threshold
-1/256+J_tau/2^23 use the source laws with CURRENT size ell_i at accepted count i. The total
index abort is <=Hmax ell_max 2^(-r_idx)<=2^-24.
The saved pivot is retained for final expansion even when its list is incomplete.
Let W(S)=sum_(c in S)w_c and P_j=S_(128j). Invertible gate generation always
uses the immutable prefix P_j, not a later history.

The source role discrepancy is uniform for EVERY record and pair:
epsilon_role=51*2^-26. Coupling the two hypothetical fresh pivot roles with
one common list/threshold of size ell_i, at fixed past/accepted count i,
gives Q(u,v)+Q(v,u)<=1+nu,
nu=128epsilon_role+2^-16=59/2^19<1/1024. This fact is distribution-free;
it does not rely on a uniformly selected pivot. The size ell_i depends ONLY
on i, not which hypothetical pivot is selected; coupled role distributions
therefore remain identical. The per-record discrepancy bound passes to an
average of ANY positive number ell_i of records with multiplicity. Neither
threshold-grid counting nor weighted contraction needs a common size across
different accepted counts. If a pivot p has law
w_p/W(S), weighted pair counting and removal of p give

 E[W(S_after)|S,past] <=(1+nu)W(S)/2 <=rho W(S), rho=3/4.  (8.1)

Indeed the numerator is sum_(u!=v)w_u w_v Q(u,v); pair the unordered terms.
Define the zero-mass chain as absorbing. Zero-weight false classes can remain
as logical elements; nothing assumes a positive minimum false-class weight.
Until a_s is removed/visited, important histories have mass at least1/D.

On the ENTIRE query/work pool except the catalyst, let R0=2|0><0|-I and

 V_j=V_(j-1) R0 V_(j-1)^dagger O_(P_j) V_(j-1).           (8.2)

For any marked query basis state x in P_j its amplitude is a_x F_j, where
F_0=1 and F_j=F_(j-1)[3-4W(P_j)F_(j-1)^2]. This follows by the two-reflection
identity; all complex base phases are retained. It is not a claim of equal
amplitudes. Common-factor proportionality holds on any nested history.

Put e_j=1/(4096j^2). A bad-size event is
W(P_j)>e_j/A_(j-1)^2, without the old cardinality +1 term. Equation(8.1) and
Markov bound its probability by4096 j^2 9^(j-1)rho^(128j). Summing as in the
source, with9rho^128<2^-28, gives total<2^-18. On all preceding good sizes,
0<F_j<=A_j and

 F_j>=A_j product_(l<=j)(1-4e_l/3)
     >=(1-1/1536)A_j >(1023/1024)A_j.                    (8.3)

Use sum1/l^2<=2; there is no omitted uniform-state amplitude assumption.
For current S_r inside P_j the marked probability is p=F_j^2 W(S_r).
The usual Grover two-dimensional calculation multiplies ALL marked amplitudes
by one scalar. Conditional on success, the accepted CLASS has distribution
w_c/W(S_r), for each clock and the direct branch, including conditioning on
all previous failed clocks. This is the weighted pivot law needed in (8.1).

For p>=1/2 the direct half succeeds with probability>=1/4. For p<=1/2,
averaging t uniformly on[0,B) gives mixed success>=1/8 once B>=4/sqrt(p),
by the finite sine-squared sum used in the complete source. While a_s is
present before a NEAR visit, W>=1/D, and (8.3) ensures the defined Bcap_j
reaches that scale. Sixteen qualifying attempts fail with probability
eta=(7/8)^16<1/4. Doubling-scale sums, with a geometric plateau at the cap,
bound the expected sum of B before acceptance by512/sqrt(p). Multiplication
by A_j and (8.3) bound expected TOKEN cost by1024/sqrt(W). No claim is made
for a false-only set of arbitrarily tiny weight after the stopping event.

For the ideal weighted chain, divide masses >=1/D into dyadic bands
[2^a/D,2^(a+1)/D). After four steps contraction implies probability of still
being in that band <=2rho^4=81/128<3/4; mass never increases. Thus expected
number of visits per band is at most16. Stopping at first NEAR visit, bad
sketch, size failure or accepted cap only reduces this band occupancy. Sum
1024*16 sum_(a>=0)2^(-a/2)*sqrt(D)<2^16 sqrt(D).
This analysis stops at a PAST discrepancy, not conditioned on future survival.
The actual capped sampler agrees with it until the same stopping time.
Markov with Budget=2^28 root gives debit-exhaustion failure before that stop
<=2^-12, including the analytical complete debit first refused by the guard.

Finally, if Hmax pivots were accepted with no NEAR visit or prior survival
error, a_s remains and mass>=1/D. Contraction gives probability<=D rho^Hmax.
Since D<=2^(2n), K>=n/9 and rho^4<1/2, this is <2^-64 on our branch.
Combining survival, size, index cap, pivot cap and token cutoff gives

 delta_coarse<=2^-22+2^-18+2^-24+2^-64+2^-12 <2^-11.        (8.4)

This holds for EVERY fixed record/base string satisfying E_far and (6.4),
regardless of its correlations with retained rows. It replaces the uniform
source proof; no cardinality oracle or preparation inverse of an unknown
source has been introduced.

## 9. Full work, compiler, simultaneous storage and literal samples

All arrays/loops have the fixed caps of Sections1-2. Put U*=nL^2. For
constraint i, each of its ell_i records uses q controlled p-bit additions,
p=30+ceil(log2q). The complete selected persistent generator RQ6.1/SPTS8
emits forward/reverse ripple words in O(p+L) actual core actions per adder,
including constant reads, descriptor initialization/carry walks and sentinel
termination. Each bit read/write, gate and generated instruction pays the
full O(L) address fee. Regular bases are formed once per record/adder. Fresh
index/cache access and finite trigonometric interpolation, O(log ell_max)-bit
signed accumulation, comparisons, flag/AND and all uncompute fit this bound.
Thus, for an absolute C independent of i,n and records,

 cost(constraint i)<=C ell_i nL^2
                   <=C'(1+log2(i+1))U*.                  (9.1)

Padding accumulator widths to ell_max costs O(log ell_max)=O(log L), which
fits the per-record nL^2 allowance. It does NOT pad the number of sampled
records or run ell_max additions at an early constraint. Actual ell_i and
threshold products are public known integers with fixed finite-width loops.

One V0 or actual inverse costs O(JnL) for forward pattern mapping AND inverse
index clearing, O(J(g+log J)L) for coefficient/scalar/AND words and at worst
O(JL^3) metadata initialization. Since J<=8m=O(L), these terms are O(nL^2):
L^4<=nL^2 on the main branch. The NEW block QFT has q blocks. Each uses
O(w+L)=O(L) actual ripple-generation core actions with persistent regular
wire-role pointers; descriptors are initialized once per block, not copied
per elementary gate. The source/addend window, gradient top segment, target
control, carry and clean padding wires have fixed offsets/strides. Pointer
increments/decrements amortize their bit changes; reverse blocks reverse
these walks. EACH bit action, instruction and actual gate pays its full
O(L) address fee. Therefore the whole QFT is O(nL^2), including controls,
wire reversal, initialization and actual adjoint. No free address-word or
phase synthesis primitive is assumed. One complete base costs C U*.

At root stage j=floor(r/128), at most128(j+1) current constraints occur in a
predicate. Summing (9.1) gives O((j+1)(1+log2(j+2))U*) work for its complete
forward/reverse oracle, with the same reused helper pool. The recursive
word is STILL V_j=Vprev R0 Vprev^dag O_(P_j) Vprev, P_j=S_(128j).
Let c_j bound BOTH complete preparations in units U*. Then

 c_0<=C, c_j<=3c_(j-1)+Cj(1+log2(j+1)).                (9.2)

Thus c_j/3^j<=C+C sum_(t=1,...,j)t(1+log2(t+1))/3^t.
This sum is bounded by sum t(1+t)/3^t<3, since log2(t+1)<=t and geometric
series give sum t/3^t=3/4 and sum t^2/3^t=3/2 (their sum9/4<3).
So BOTH actual words cost O(3^j U*) uniformly in j. A current root predicate
costs O((j+1)(1+log2(j+2))U*)<=C3^j U* as well. This accounts for late expensive
constraints without inserting their ell_max into every early recursive leaf.
The global statistical analysis, not the cost analysis, sums ALL constraints.

Use the same source finite(level,direction,position) recursive generator with
immutable prefixes and actual reverse words. Its O(n log n) classical stack
fits SCn^2. There is ONE shared quantum query/helper pool. Per-attempt clock,
measurement/reset, classical verification of the SAME current predicate,
Budget arithmetic and B A_j debit cost at most C B A_j U*: stage tables and
operands have O(n) bits, and their bounded carry/shift work fits nL^2.
Consequently, on ALL inputs and histories including wrong gradients/base
failures, the PRE-ATTEMPT guard proves

 T_attempts<=C U* sum_(admitted attempts)B A_j
            <=C U* Budget=O(2^(n/2)n L^(3/2)).           (9.3)

Here root=ceil sqrt(ceil(2^80 M/m))=O(2^(n/2)L^(-1/2)). The inverse square-root
log comes from the recomputed m=2^100 L. We reduced BOTH the full base and
the weighted recursive preparation charge before using that gain. This is
a worst-case token-bound statement, not an expected-time claim. The stopped
hitting argument in Section8 establishes sufficient success under that cap.

Polynomial extraction, subset/filter work, streamed angle search,
precomputed constants/caches, at-most-Hmax accepted pivots, classical integer
expansion/full-record tournament, endpoint, initialization and complete
cleanup are separately paid and absorbed by (9.3). Even the finite G^2
angle enumeration is polynomial and is streamed without a G^2 table.
All capped failures and discarded samples/work are covered.

Original classical records/prefixes/labels and pivot caches occupy O(n^2)
bits. Additional m labels and 4m frequencies occupy O(mn); finite angle words
O(mg); masks, current arithmetic and streamed trigonometry O(n^2) or less.
Both original N-prefix and new dyadic M-prefix banks together remain O(n^2).
All profiles, source/ordinary-gradient counters, known word descriptors,
allocation padding, cap tables and every inactive field count in SCn^2.
No exponentially indexed classical lookup is supplied for free.

ENTIRE quantum allocation is the Q=O(n) retained rows plus one reused original
extraction/data workspace, q frequency wires, O(n) equality/adder/diffusion/
flag/constraint helpers, O(log J) branch/index fields and g=O(L) catalyst.
All source temporary registers, padding and unused helper fields count. The
endpoint reuses those pools after the coarse catalyst/query pool is released.
Thus SQ=O(n), jointly with SCn^2 for this same implementation. No extra copy
of a recursive candidate or retained state is allocated.

Exactly the original Q calls occur before any new abort. Ordinary initialized
ancillas, the gradient, phase constants and any failed query are NOT original
samples. Therefore Q=3*2^40(n+32) EXACTLY on every branch. All primitive gates,
measurements/reset, source fees, classical bit actions, arithmetic, actual
compiler output and full combined-memory operand addresses have their stated
charges. There is no QRAM, free word-RAM, source inverse/control, supplied
purification or arbitrary phase primitive.

## 10. Unconditional all-N success and exact declared objects

Work in the unconditional label comparison of Section1 and finally subtract
its <=2^-62 distance ONCE. The original k-count event, original integer score
event and reference endpoint comparison are unchanged. The new dyadic score
event costs one additional <=2^-80 tail, with the same count event charged
once. The new m-count/generic/two-score-tail/false-anchor/constant-guard events
have total failure bounded by

 2^18/m+256m^2/N+exp(-m/2^21)+exp(-m/2^23)+2/N+16/C^2.

For (2.1) and n>=2^4096 this is <1/4096. For example m>=2^100 controls the
first/tail terms, 16/C^2=2^-44, and n>=2^(L-1) makes the two N denominators
smaller than2^-100. The inequalities persist for L>=4096 by the same dyadic
exponential domination as Section2. Extra subset/anchor caps add <2^-254;
the independent coarse gradient adds <=2^-80+2^-115. All new losses together,
including the dyadic score tail, are <1/1024. The coefficient/pointwise Fourier
errors are deterministic bounds already in (6.4), not further stochastic
success assumptions or per-query hybrid errors.

On these events every fixed record/base string satisfies the stopped weighted
coarse bound (8.4). A NEAR visit places the ACTUAL integer secret in the
expanded final list, so E_int yields the true original class. The coarse
helper work acts only on measured records and ordinary independent work,
never on a retained row. One may therefore bound conditional coarse failure
for fixed records and then subtract its unconditional probability from a
reference endpoint supplied the true class. One does NOT condition the
unconditional retained parity law on base quality, count survival, Fourier
preparation, a correct coarse answer or successful labels.

The source's endpoint baseline91/128 minus its original combined losses
<3/128 (with (8.4) replacing the old coarse term), minus the NEW <1/1024 loss,
is >2/3. All original and new sampler failures, malformed rows, wrong labels,
work preparation errors, budgets and final output/cleanup are included.
Linearity extends this uniform guarantee to allowed fixed-B mixtures. For
n<2^4096 the COMPLETE selected old joint algorithm already succeeds >11/16.
Thus ALL N>=2 and s, including the clean case, have the strict >2/3 guarantee.

Finally the joint EVERY-BRANCH representatives are exactly (0.1). Their
logarithms give time index1 and three polynomial indices0. The supported
fraction is EXACTLY1/3 under the literal fixed joint-marginal context, not a
per-copy probability, flag assumption or assertion of maximal tolerance.
Neither source acceptance, numerical diagnostic nor earlier scored point
is used to establish any of these five statements.
