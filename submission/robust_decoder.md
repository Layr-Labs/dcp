# Resetting prefix verification and bounded backtracking

This file defines the main decoder of QUDIT-L32-LARGE jointly with
proof.md Sections2..10 and15. It is part of the proof, not an oracle.
The finite algorithm remains proof13/18. All logarithms are base2.
Let l=log2n,u=ceil(l),b0=floor(H/2)-1024u,Lblk=ceil(n/b0),noise=ceil(log2(n^5)),
Cc=64dl2^m,Cf=16dl2^m,Y=ceil(log2Cc),E=8u,
w=64u,htop=Y+E+12,P=htop+Y+8,
Kc=65536u,I=16Lblk+128(w+u),Hchain=8w+64u.
Each actual data block b uses r=b+noise; no global fixed r is used.
There are at most two controllers,one for each component of the secret.
Every root is measured and ALL quantum work reset before the next root.
The prefix,block stack,counters and candidate records persist classically.

## A. A low-label-only X-verification instrument

For B>=1,h>=1,B+h<=n, the supplier has a physical integer label k
uniform on[0,2^(B+h)) and its phase qubit (|0>+e^(2pi i k theta)|1>)/sqrt2.
Retain only L=k mod2^B in the classical table. LE may compute full k in
its reusable source register, but its upper h bits are not retained as
leaf or intermediate table entries. They are not needed by this kernel.
Run exactly the binary MERGE instrument of proof6/9 with final d=1,
precision B, and the same tapered lengths. In its classical maps use L
and sums of L as logical labels. Analytically distinguish the physical
label K,initially k,from the stored low-label sum L,initially k mod2^B.

Induction on each instrument: before a merge amplitudes have equal
magnitudes and phases proportional to the sum of physical labels K.
The residue measurement,sorting,pair rank and reindexing depend only on
stored L; K-L is divisible by2^B at leaves and sums preserve that relation.
Therefore every residue below B of K equals that of L. The recorded
common prefix c of L is also the common physical residue modulo2^p.
The same injective pair permutation and measured residue of proof6
select an equal-magnitude phase vector with physical sum labels,while
stored L follows exact integer addition. FAIL depends only on residue
bucket counts. Nothing in that instrument needs the unknown high part
of K when the final operation is X measurement rather than computing W.
The root,up to a global phase,is (|0>+e^(2pi i2^B W theta)|1>)/sqrt2
with analytic W=(K_1-K_0)/2^B. The algorithm never computes W here.
Measure X,record plus/minus,reset all work. Missing root records PLUS.
No unknown rotation or unknown-label gate has been introduced.

Let G contain all stored low labels,merge residues,rank selections,
retry/cap and source assignments,but no unused high source labels or
root measurement. Conditional on G and completion,the high labels
k=L+2^B tau have independent uniform tau modulo2^h. Distinct final
indices have distinct 0/1 incidence vectors on disjoint canonical source
coordinates,as proof10 shows. Their difference has a coefficient +/-1.
Consequently W modulo2^h is uniform conditional G. The possibly large
carry from sums of L is G-measurable and only translates that uniform
law. This remains valid when h is large; no full high-label table exists.
The completion probability is at least5/8 under cap Cf,by proof9's
expected selected cost<=6dl2^m and Markov. Root |W|<=2^h Cf follows
from the physical source footprint even though W is not stored.

Memory lemma. At level i stored sums of L are below2^(B+i+gw),where
gw=ceil(log2dl). Store high parts in w_i=B+i+gw-tp_i=R_i+i+gw bits
and one common prefix. The next sum fits in w_i+1 bits. All instrument
maps,lookups and inverses use these exact widths; all arithmetic carries
are retained. With k=m-1-i,R_i<=(k+2)H and i+gw<=H,we get
w_i<=(k+3)H. The geometric tapered row bound proof14 therefore gives
O(H2^H) bits INCLUDING all retained siblings,scratch and prefix storage.
There is no extra h2^H term,even when h is of order n. Source arithmetic
still costs its full O(n) width per row. Physical high labels are an
analysis device,not accessible storage. Even on wrong LE outcomes,the
retained L is in[0,2^B),so these dimensions and all guards remain valid.

## B. Physical verification of the odd prefix

Run the ONE coarse batch F. If M=1 or its SMALL branch returns s1,
skip this odd controller. Otherwise F returns chat and known rational
R0=M2^(-Y-E-8)+1/2. On its good event the true signed t0 congruent
s1-chat moduloM has |t0|<=R0,R0>=1,R0/M<=2^(-Y-E-7).
Define the integer
 Jtarget=min{J>=0:2^J>=4R0}.

Only integer comparisons against the rational 4R0 are needed. Then
4R0<=2^Jtarget<8R0. Split Jtarget into consecutive blocks of b0 bits,
last shortened. A prefix of j bits always has representative 0<=v<2^j.
For EVERY possible prefix,j<=Jtarget gives |t0-v|<9R0. The large-M
branch also gives Jtarget<log2M-Y-E-4; hence B=dn-j>=a2+1 for j>0.
These inequalities are independent of correctness of the proposed prefix.

To verify v at j>0 use kernel A with B=dn-j,h=j and cap Cf. Put
 gamma=2^(B-a2) modM, K0=(-2^j)^(-1) modM,
 J=(2^j K0+1)/M.
Compute the CRT unit alpha=1 mod2^a2,gamma*alpha=K0 modM.
For every fresh selected source copy apply Shift_(chat+v modM),then
Mult_alpha,LE,accept iff k<2^dn,then X on its control,as proof3.
Store only k mod2^B for A. The exact root relative phase is

 2pi*K0 W(t0-v)/M
   =2pi*J W(t0-v)/2^j - 2pi*W(t0-v)/(2^j M).

The first equality is modulo2pi using the CRT relation. The integer J
is odd. The second term has magnitude at most
 2pi*Cf*9R0/M <=18pi*2^(-E-7)<2^-E.
This bound holds for ANY prefix,not just correct past. On correct prefix
modulo2^j the first phase is integral2pi,so completed Xplus probability
>=1-eta²/4>=1-1/4096,where eta<=2^-E<=1/32. On wrong prefix,
uniform W modulo2^j implies ideal mean X=0,even if t0-v is even but
not divisible by2^j. Perturbation changes plus probability by at most
eta/2. Missing=>PLUS and missing probability<=3/8 give

 correct-prefix unconditional plus >=1-1/4096,
 wrong-prefix unconditional plus <=11/16+5eta/16 <7/10.       (B.1)

At j=0 verification returns PLUS without a query. Data proposals at
nonleaves use the ordinary known-label r-qubit fine root,cap Cf,of
proof11 and qudit_decoder.md with current prefix and next block length.
There is ONE attempt,not retry-until-completion. Its physical supplier
is the unchanged proof11.2 including the factor2^(-j) in alpha,unlike
verification above. On correct past the residual quotient is bounded
by R0 and perturbation<=2pi*Cf*R0/M<2^-E<1/(16n^4).
Thus completion>=5/8 and probability(completed AND decoded wrong)<=
rho=2/n^4. On wrong past it may return any block; it cannot repair an
earlier wrong bit. Table ranges and cost remain valid on those branches.
After the controller accepts a full Jtarget-bit prefix,choose its unique
signed representative in[-R0,R0] if one exists; else output0. Uniqueness
holds since2^Jtarget>=4R0. Return s1=(chat+t0) modM.

## C. Physical verification and data for the two-adic prefix

After s1 has been recovered,let s=s1+M*s2 moduloN. For candidate v
of j bits of s2 apply Shift_(s1+M*v) then LE. Its label k is uniform
moduloN. Put kk=k mod2^a2,which is exactly uniform since2^a2 dividesN.
Its control phase is exp(2pi i kk(s2-v)/2^a2) after the same X
convention as proof12. For 0<j<a2 run A with B=a2-j,h=j,physical
label kk,retaining only kk mod2^B. Relative phase is exactly
2pi W(s2-v)/2^j. Correct prefix gives PLUS surely; wrong gives fair
X conditional completion. Missing=>PLUS obeys the looser B.1 bounds.
At j=a2 use ONE direct source qubit,X-measured,with full physical
label kk,without a collimation tree. The same true/fair law holds.
At j=0 verification is the trivial PLUS. If a2=0 skip this controller.

For a data proposal at j<a2 put wd=a2-j,b=min(b0,wd),kk=k mod2^wd,
B=wd-b. If B>=1 use the ordinary r-qubit fine root with these known
labels,cap Cf,exactly proof12. On correct prefix its phase is
2pi W*(remaining secret)/2^b and the decoder error<=rho.
If B=0,acquire r independent direct source phase qubits. Their product
is a 2^r-dimensional equal-amplitude vector with known labels equal to
the subset sums of their uniform kk modulo2^b. Distinct subsets differ
on at least one coordinate with coefficient +/-1,so every pair label
difference is uniform modulo2^b. Use exactly qudit_decoder.md with J=1.
It completes surely and has error<=rho on correct prefix. Only r selected
copies are needed,r<=Cf. Its explicit decoder cost is bounded by
O(2^(2b)n^128), with O(b+r) quantum wires, as qudit_decoder.md5 proves. This case uses no
invalid B=0 collimation tree. On wrong prefix,the physical source/qubits
and table ranges are still defined; no correctness is asserted for its
data proposal. Earlier wrong bits cannot be changed by appending a block.
All r qubits,PGM work and source work are reset after each proposal.

## D. Actual guarded controller with verification chains

For each component divide its target into fixed consecutive b0-bit blocks,
last shortened. Let Lpart<=Lblk be their number. A node consists of its
classical data-prefix stack and,only when that stack is full,a chain
height c in[0,Hchain]. Start empty. At most I logical iterations per
component are allowed. Before exceeding that count ABORT0.

At a nonfull data stack: hold all current-node parameters fixed. Run ALL
FOUR fresh verification records B/C and ALWAYS ONE fresh data proposal
for the SAME prefix,even if any check was minus. Only after all five
records and quantum resets,if any check was minus drop one last data
block (empty remains empty) and discard data; if all checks wereplus
but data missing,hold; else append its block. A newly full stack has
chain height0. There is one proposal attempt,no retry-until-completion.

At a full data stack with c<Hchain: hold its full-prefix parameters
fixed,run ALL FOUR fresh verification records and reset each root.
If every record isplus,increase c by1; if this reaches Hchain,ACCEPT
this component immediately. If any wasminus,decrease c by1 when c>0;
when c=0 instead drop the last data block and return to data mode.
There is no data root in chain mode. There is no strong K-record test,
no full-test counter and no unbounded repetition. Exhaustion without
acceptance ABORTs0. No truth or corruption flag is used by the algorithm.
Run odd first,then twoadic using accepted s1,and return the combined
secret. Empty components are skipped. The Hchain repetitions are real
physical prefix checks,not a conditional certificate available for free.

Set before source access
 Qcap=Cc*Kc+Cf*10I,Qbank=1024Qcap.         (D.1)
Two components times at most I iterations times at most five Cf-capped
records fits10I slots. Trivial/direct kernels and direct r-qubit B=0
data cost<=Cf. Coarse roots use Cc and include all rejects/failed attempts.
All guard/abort/accept paths reset work and pad exact MICROTAKE banks.
Every raw,discarded and padding copy counts in fixedQbank.

## E. Adaptive virtual classical records,including earlier bad roots

This is an iterated classical coupling,not conditioning on a clean run.
Let C count selected malformed copies over the active banks. The bank
selection coins are independent fair bits drawn AFTER its1024 deliveries.
Even after earlier corruptions,conditional on the preselection hidden
flags there are b bad bank slots and P(selected bad)=b/1024. Therefore
 E C <= E(sum b)/1024 <= epsilon*Qcap.             (E.1)
No clean-product assertion about the previous quantum workspace is needed
for this expectation. Root boundaries DO reset that entire workspace.
Let Lbad denote any clean LE error. The uniform per-label extraction
bound in proof5,with confidence sized by Qcap,gives P(Lbad)<=2^-10,
including clean requests after earlier malformed copies.

Fix arbitrary full actual classical history h before a root,including
analytical flags/labels; the root workspace is zero in product with an
arbitrary conditional private adversary state. Let mu_h be its fresh
ideal-label clean CLASSICAL record law at these same fixed parameters,
including missing and final measurement. Define
 nu_h(A)=P(actual record in A,no selectedbad and no clean LE error
           in this root | h).
Then 0<=nu_h<=mu_h as positive measures. To prove it,use a first-flag
unnormalised instrument induction: until the first flag every returned
copy is a fresh ideal product and correct label. Unchosen malformed bank
slots and their reset outcomes act only on the auxiliary environment.
Carry those records/private instruments in a hybrid that always supplies
a fresh ideal root copy and its latent correct label. Its core marginal
is mu_h; it never uses wrapper/LE-test outcomes for root decisions. The
no-first-flag branches coincide as unnormalised positive instruments.
Their output trace is nu_h; remaining hybrid branches give mu_h-nu_h.
This proof permits entangled malformed states and arbitrary private
instruments,by purification,linearity and tracing their environment.
It does not identify a conditional noflag law with the clean law.

Write p=1-nu_h(all). Couple virtual Y to actual X by Y=X on noflag,
and on flag sample Y from (mu_h-nu_h)/p using analytical classical coins
independent of the post-root private state conditional full actual
post-root history. If p=0 use Y=X. Thus Y has exactly law mu_h conditional
h. Earlier virtual records reveal no additional private quantum state
given full actual history: on noflag Y is determined by X,on flag the
new draw is independent of that state. Induct at every new reset root,
including those after earlier bad roots. For a fixed-parameter batch
its virtual records are iid clean records conditional batch-start
actual parameters and all previous virtual past. This includes four-plus-
data batches and four-record chain batches; no data root is adaptively omitted.

Define a root as TAINTED if it has either a selected malformed copy OR
any clean LE error,the same flag used in nu. Let T_t indicate at least
one tainted root in logical iteration t,and C_t=sum_(v<=t)T_v. These
variables are defined on EVERY path. Actual/virtual records agree on
all untainted roots,even when an earlier root was tainted. Unconditionally
C_t may count LE errors as well as bad-copy roots. On the event NO Lbad,
C_t<=C (the total selected malformed count),because each tainted iteration
then contains a distinct selected malformed acquisition. All conditional
expectations and stopped-potential estimates below use the UNCONDITIONAL
all-flag C_t. Only the FINAL deterministic edit implications restrict to
no Lbad and C<=w; no virtual law or expectation is conditioned on them.

## F. One wide-top coarse batch

This section REPLACES the staged coarse bootstrap. Compute from N before
source access htop=Y+E+12,P=htop+Y+8 and
 Kc=65536u.
These definitions are also used when the odd component is skipped,so the
raw source cap is fixed and padded. If M=1 put s1=0 without coarse roots.
Otherwise M>=3. Set h=min(htop,floor(log2M)),B=dn-h. In this main range
1<=h<=htop<=43u and B>=1. Since dn=a2+floor(log2M),B>=a2.
Compute gamma=2^(B-a2) modM and the CRT unit alpha with
 alpha=1 mod2^a2, gamma*alpha=1 modM.
Both exist by ordinary extended Euclid/CRT. Supply a qubit by applying
Mult_alpha,LE,accepting iff k<2^dn,and X on its control. Acceptance>1/2
and the accepted k is uniform on[0,2^dn)=[0,2^(B+h)). The ordinary
KNOWN-label one-qubit root of proof9,with cap Cc=64dl2^m,then has phase
 2pi*2^B W*alpha*s/N =2pi W*s1/M (mod2pi).
Here W is computed from its ordinary full high-part table. This is not
the low-only verification kernel A; h is only O(logn) here,as cost lemma I
proves. Every selected supplier rejection and failed merge counts in Cc.

Run exactly Kc such capped roots at these FIXED parameters. On completion
measure a fresh fair X/Y basis,record(W,beta,Z) with Z=+1 or-1; missing
roots give scorezero. Reset ALL quantum work between roots. The expected
selected cost of an uncapped ideal root is<=6dl2^m,so missing probability
is<=3/32. The ordinary unused-top-label law proof10 still holds for this
larger h; its completed structural transcript G excludes the unused tau.

Dirichlet lemma. Conditional G and completion,write
 W=cst+sum_(v inSp)tau_v-sum_(v inSm)tau_v,
with independent uniform tau_v in{0,...,2^h-1},nonempty union,and all
coefficients +/-1. This is exactly the incidence-vector proof10,which
does not require h<=b0. For circular delta not an integer,put Lh=2^h.
The characteristic magnitude of one uniform tau is
 |sin(pi Lh delta)/(Lh sin(pi delta))|.
All other independent factors have magnitude<=1 and the cst contributes
only a phase. Therefore
 |E exp(2pi i delta W)|
  <=min(1,1/(Lh |sin(pi delta)|))
  <=min(1,1/(2Lh dist(delta,Z))).                 (F.1)
At integer delta use value1. These are finite geometric sums,not a
continuous-frequency oracle. Caps/completion inspect only low structural
bits and retain the top-label law. The supplier rejects only outside its
whole dyadic accepted interval,so accepted high labels remain uniform.

For a candidate theta' the ideal exact-trig score is Z*cs_beta(Wtheta')
on completion and0 on missing. Fresh fair beta averaging gives its mean
(1/2)E[1_complete cos(2pi W(theta-theta'))],where theta=s1/M.
The ACTUAL score uses proof4's rational tab_beta with error<1/625.
Concretely,LARGE candidate c contributes
 Z*tab_beta(((W*c) mod2^P)/2^P),
and SMALL candidate a contributesZ*tab_beta(((W*a) modM)/M).
Modulo is the least nonnegative residue,also for negative W; missing
records contribute0. Both are finite rational arguments in[0,1).
All candidates are streamed classically; frequencies and denominators
are known integers,so no unknown rotation or quantum memory lookup occurs.

LARGE odd component: floor(log2M)>=htop. Then h=htop. Enumerate ALL
candidates theta'=c/2^P,0<=c<2^P,scoring each by the Kc records. Choose
the smallest maximum and call its point z. There is a closest gridpoint
with distance<=2^(-P-1). Since |W|<=2^h Cc<=2^(h+Y),its phase error
is<=2pi/512<pi/128; its exact score mean is at least
 (1-3/32)*(1/2)cos(pi/128) >=28971/64000,
using cos(pi/128)>=999/1000 (the elementary bound with pi<22/7 suffices).
Any candidate at circular distance>=4/2^h has by F.1 characteristic
magnitude<=1/8,thus score mean<=1/16,which is certainly<=71/200.
This bound holds conditional on every G before averaging. If the good
score event below holds,the maximizing z satisfies
 dist(z,theta)<4/2^h=2^(-Y-E-10).
Set chat=floor(Mz+1/2) modM and the known rational
 R0=M2^(-Y-E-8)+1/2.
Then the true signed lift t0 congruent s1-chat modM satisfies |t0|<=R0.
Because M>=2^htop=2^(Y+E+12),R0>=1 andR0/M<=2^(-Y-E-7)<1/2.
This is precisely the invariant needed by B; its small phase bound and
signed target length remain unchanged. Proceed to the odd controller.

SMALL odd component: floor(log2M)<htop. Then h=floor(log2M)>=1,
Lh=2^h<=M<2Lh. Enumerate the EXACT candidates theta'=a/M,
0<=a<M,score each,choose the smallest maximizing a and return it as s1.
No odd controller is run. True mean is at least(1-3/32)/2=29/64.
For a false candidate,circular delta>=1/M>1/(2Lh). By the geometric-sum
formula and monotonic sine on[0,pi/2],
 |E exp(2pi i delta W)|<=1/[Lh sin(pi/(2Lh))]<=1/sqrt2<71/100.
Indeed Lh>=2,and sin(x)/x>=2sqrt2/pi on0<x<=pi/4,so the middle
reciprocal is<=1/sqrt2. The last strict rational bound follows from
10000<2*71². The false score mean is thus<=71/200. This treats all odd
M>=3,including M=3,h=1; B>=1 still follows from the MAIN input range.
The exact candidate grid has M<2^htop<=2^P points and is a finite loop.

Robust score event. Use E's virtual CLASSICAL record construction for
this fixed-parameter Kc batch,including after earlier bad roots. These
reference records are iid conditional its start. Each exact-trig score
lies in[-1,1]. Hoeffding deviation1/24 has probability<=2exp(-Kc/1152)
per candidate. Since there are at most2^P candidates and
 Kc/1152=(512/9)u>56u, P<=77u,
a union bounds all deviations by2 exp((77 ln2-56)u)<2^-20.
Here ln2<7/10 and u>=128 give an upper bound2exp(-2u).
No whole-run noflag event is used to condition this concentration.
For both grids the true/nearest-versus-far mean gap is at least
 28971/64000-71/200=6251/64000.
On no clean LE error and selectedBad C<=w,at most C root records differ
from their virtual records. Any replacement changes a candidate score by
less than3,so changes a score pair by less than6. Table approximation
costs2/625 in normalized pairs. The exact strict inequality
 6251/64000 > 2/24+2/625+3/512,
with6C/Kc<=6w/Kc=3/512,leaves a positive gap. Thus no false/far candidate
can maximize actual scores on the concentration event. In SMALL this
returns exact s1; in LARGE it gives the stated z invariant. All root
records exist before candidates are scored,and no later copy is acquired
based on a candidate score. The full adaptive error probability for
coarse recovery is bounded by its2^-20 tail plus the separately charged
C/no-LE events,not by assuming actual clean records after earlier flags.

## G. Progress on the data tree and its verification chains

Define a conceptual rooted tree whose nodes are all data-block prefixes,
with a chain of Hchain links attached to each complete data candidate.
Only ONE such chain is attached to the actual true data candidate; its
nodes extend the true path. The controller does not know that path.
For its actual node let ell be data depth plus chain height,q its longest
common initial path length with the true path,and Phi=2q-ell. If the
data prefix is wrong,q is its data LCP and remains fixed while moving
on its wrong chain. If it is correct,q=ell including true chain links.
Every transient Phi<=Lpart+Hchain; acceptance is at a chain endpoint.

For each ordinary iteration use its FIVE virtual records from E to
define virtual increment g: correct append+1,wrong append or backtrack
-1,missing0 at correct data nodes. At empty node a rejected check actually
holds; assign g=-1 for a weaker lower bound. Four checkfalse-minus
probabilities sum<=1/1024,completed data>=5/8,and wrong-complete<=rho.
Batch independence therefore gives
 E(g|past)>=(1-1/1024)(5/8-2rho)-1/1024>1/2.
At wrong data nodes,allfour virtual checks pass with probability at most
(7/10)^4<1/4. Backtrack raises Phi,append lowers it,missing holds;
thus the corresponding virtual g has conditional mean>=1/2.

In chain mode define g=+1 for allplus and-1 for anyminus on the correct
chain,and opposite signs on a wrong chain. On the correct chain,anyminus
probability<=1/1024,so Eg>=1-2/1024>1/2. At height0 anyminus drops a
correct data block,which still has Phi increment-1. On a wrong chain,
allplus probability<1/4,so Eg>=1/2; height0 backtrack remains a step
towards the true path. All g lie in[-1,1]. Stop analysis at first ACCEPT
(correct or wrong) or guard,then extend g=1 as analytical variables.
There are no additional physical copies in this analytical extension.

E's coupling supplies these conditional statements given the complete
actual/virtual past,including earlier bad roots. On no clean LE error,
if iteration t is untainted its actual increment agrees with the virtual
one,or is larger at the empty-node clamp. If tainted,the two increments
are in[-1,1],so deltaPhi>=g-2T_t. SumT_t<=C. Conditional Hoeffding gives
 P(sum_(t=1)^I g_t <=I/4)<=exp(-I/32).
If no acceptance has occurred by I,on C<=w and correct coarse batch,
 Phi_I>I/4-2w=4Lblk+30w+32u > Lpart+8w+64u,
a contradiction: w=64u gives4Lblk+1952u>Lpart+576u
using only Lpart<=Lblk. Thus total probability of no acceptance
across both controllers is less than2^-20,apart from already charged
coarse/extraction/corruption events. Wrong acceptance is bounded next;
no correctness condition is inserted into the actual runtime rules.

## H. A stopped potential for wrong acceptance

Put D=ell-q>=0,off-true-path distance,and let C_t be the number of
tainted iterations so far. Define Z_t=3^(D-2C_t),initial1. At any wrong
node,ordinary OR chain,virtual append/up has probability p_up<=1/4,
virtual backtrack has p_down>=3/4,and other outcomes hold. Therefore
 E3^(virtual deltaD)=1+2p_up-(2/3)p_down<=1.
At a correct DATA node only a virtual wrong data append creates D=1,
with probability<=rho=2/n^4,so the conditional factor is at most1+2rho.
At a correct CHAIN node D remains0 on either up or backtrack,including
height0 back to correct data. Its factor is1. No ghost unknown physical
measurement or oracle is used to establish these bounds.

The actual deltaD is at most virtualdeltaD+2T_t. This pointwise bound
allows subtraction of2T_t even when taint is correlated with Y; hence
conditional expected factors for Z are still<=1+2rho. Stop Z at the
first actual acceptance or fixed guard and hold it thereafter. This is
a bounded stopping time. Iterate expectations to get
 E Z_stop<=(1+2rho)^I<=2.
If acceptance is WRONG then its data LCP<=Lpart-1 and its chain height
is Hchain,so D>=Hchain+1. On no Lbad and C<=w,
 Z_stop>=3^(Hchain+1-2w)>=3^(6w+64u).
Markov bounds wrong acceptance by2*3^(-6w-64u) per component; both
together contribute less than2^-20. This is an unconditional expectation
bound followed by an edit implication,not conditioning virtual laws on
future C or lack of flags. The actual controller never computes D,q,C
or Z. The physical verifier's false-prefix bound B.1 holds for EVERY
prefix,which is essential at wrong chain nodes after earlier errors.

## I. Large-block geometry and exact joint cap for depth32

Let l=log2n>=128,u=ceil(l),w=64u. Proof8 gives
Cc=64dl2^m<=4n^33/l, Cf=16dl2^m<=n^33/l,
Cc>=n^33/(2l), Cf>=n^33/(8l), m<=33l.
Thus Y<=m+u+6,htop=Y+8u+12<=42u+18<=43u,
P=htop+Y+8<=76u+32<=77u. Base>=n/(64l)>=256u:
check2^l>=16384l(l+1) at128, with increasing exponential ratio.
Consequently gw<=base/4 and m+gw+htop<=H.

For b0=floor(H/2)-1024u, H>=n/(32l+2)>n/(33l) gives
 b0>=n/(66u)-1024u-1>=n/(67u)>0,
using n>=67*66*u*(1024u+1), valid at128 and increasingly thereafter.
Hence Lblk<=67u+1<=68u. Each actual block b uses r=b+noise,
noise=ceil(log2(n^5))<=5u, r<=H, m+gw+b<=H and
2b<=H-2048u. Proof8's cancellation against B<=n-b proves root
capacity; nonroot dimensions and failures are unchanged. Actual odd
blocks obey b<=Jtarget<floor(log2M), so B>=a2+1. Twoadic B=0
uses its explicit direct vector. Verification uses A's low-only fields.
The same tapered sum19H2^H holds for ordinary full-label fields.
The explicit decoder costs O(2^(2b)n^128) work/bits, hence over O(u)
calls O(2^H/n^1900), and O(b+r) wires fit O(n), including all synthesis.

Use Kc=65536u,I=16Lblk+128(w+u)<=9408u,Hchain=576u.
The coarse cap CcKc<=264192n^33 and fine cap10CfI<=94815n^33
use u/l<=129/128. Thus
 Qcap=CcKc+10CfI<=359007n^33<2^19n^33.            (I.1)
The count includes every failed/capped/rejected source and tree, both
components' ordinary/chain records and exact padding. Reserve coarse
slots also when M=1 or SMALL skips odd decoding. Qbank=1024Qcap
on every branch; microbanks are1024 delivered copies followed by10 coins.

Set epsilon=l/(262144n^33)=l/(2^18n^33), natural0 atn1.
E's adaptive expectation gives EC<=2l<=2u=w/32, so P(C>w)<=1/32.
For F's concentration Kc/1152=(512/9)u>56u,P<=77u and
ln2<7/10 give union bound2exp((77ln2-56)u)<2^-20.
The exact score/edit margin is
 6251/64000>2/24+2/625+3/512,
with6w/Kc=3/512. Missing reference coarse probability remains<=3/32.
No actual-record law is conditioned on a future count or clean event.
G's progress contradiction uses
 I/4-2w=4Lblk+1952u>Lpart+576u=Lpart+Hchain.
H's stopped wrong-chain potential and E's all-flag taint expectation
remain valid before restricting deterministic edit implications to no
clean LE error and C<=w. Including extraction, total main failure is
<=1/32+2^-10+3*2^-20<1/3. Finite inputs use proof18's separate
bank-first argument: epsilon*kblock<=6/(2^18n^31)<2^-45 atn>=2;
atn1 the fraction0. The finite total failure remains<1/100.

All selected demand is O(n2^m)=O(n^33) over O(u) calls. Actual-width
tree accounting gives O(n²*l2^(m+dl)) charged work, O(H2^H) bits,
and O(n) qubits. Frame initialization O(u H²2^H) includes addresses
once and fits the tree bound. All source, extraction, CRT, guard, lookup,
compile/circuit, reset and padding costs are counted. The coarse grid
has <=2^77n^77 candidates and O(u) records of O(u) bits, hence fixed
polynomial addressed work; F64>=n/(64l) absorbs it. No quantum list,
QRAM, free rotation or subset-sum oracle is supplied. Exact proof15
substitution m+dl<=F64+16l+log2l+O(1) gives the full joint envelopes
 T=O(n^18*l²2^F64), SC=O((n^17/l)2^F64), SQ=O(n), Q=O(n^33).
All64 coefficients are retained. These are not only index comparisons.

On the MAIN range ONLY, CcKc>=32768n^33, so
 epsilon Qbank>=128log2n,
and the integer allowance>=floor(128log2n), unbounded. This auxiliary
count is not the fractional score and is not asserted in the finite range.
