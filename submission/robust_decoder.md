# Resetting prefix verification and bounded backtracking

This file defines the main decoder of QUDIT-L16-CHAIN jointly with
proof.md Sections2..10 and15. It is part of the proof, not an oracle.
The finite algorithm remains proof13/18. All logarithms are base2.
Let l=log2n,u=ceil(l),b0=floor(l),Lblk=ceil(n/b0),r=ceil(log2(n^5)),
Cc=176dl2^m,Cf=16dl2^m,Y=ceil(log2Cc),E=8u,
w=floor(n/u²),Kc=134217728(m+10u+100)+352w,
I=16Lblk+128(w+u),Hchain=8w+64u.
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

First run exactly the coarse stages of proof11 with the larger Kc,Cc,E
above. Missing scores remain zero and roots are immediately reset.
If J0=Jfull the rounded coarse result is s1 and no odd controller runs.
Otherwise the same coarse calculation produces chat and the known
rational R0=M2^(-Y-E-8)+1/2. On correct coarse stages the true signed
t0 congruent s1-chat modulo M satisfies |t0|<=R0,with R0>=1 and
R0/M<=2^(-Y-E-7). Define the integer

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
copies and polynomial( n ) tables are needed,r<=Cf. This case uses no
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
 Qcap=Cc*Kc*(Y+E+6)+Cf*10I,Qbank=1024Qcap.         (D.1)
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

## F. Coarse correctness

Coarse virtual stages have iid fixed-parameter clean records by E.
The proof10/11 trig discrimination gap is >379/10000 before cap/table/
mesh/concentration losses. Cap loss contributes3/176 to the pair gap;
table/mesh losses remain2/625+2/4096. If C<=w,score-pair edits change
averages by at most6C/Kc<=3/176. Exact rational arithmetic gives
 379/10000 > 2/4096+2/625+3/176+3/176.
The proof11 Hoeffding threshold is now1/4096,with per-record
range[-1,1] giving2exp(-Kc/33554432). Kc>=2^27(m+10u+100)
preserves the original mesh/stage union exponent,so total coarse
failure remains<=2^-20. Both the deviation and Kc are changed together.
These are unconditional conditional-on-stage-start tails followed by
deterministic edits. A first-incorrect-stage union uses physical phase
identities only at correctpast; corruption may have occurred previously.

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
If no acceptance has occurred by I,on C<=w and correct coarse stages,
 Phi_I>I/4-2w=4Lblk+30w+32u > Lpart+8w+64u,
a contradiction. The last inequality uses Lblk>=32u,proved at the main
cutoff and increasing thereafter. Thus total probability of no acceptance
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

## I. Explicit counts,full resource envelopes and all-N guarantee

Let l=log2n>=128,u=ceil(l),w=floor(n/u²). Then
 n/(2u²)<=w<=n/l², w>=n/(4l²).
For the lower bound n/u²>=2 and floor(x)>=x/2; also u²<=2l².
We have w>=2^22(m+10u+100),w>=1024u,Lblk>=128u on this range.
These follow from n>=2^l,u<=l+1,m<=17l,by checking l128 with
integer/rational comparisons; each exponential-to-polynomial ratio
increases since ln2 dominates the sum of at most three reciprocal l
terms for l>=128. No validity threshold is left implicit.
Thus Kc<=384w: the baseline2^27(m+10u+100)<=32w. Since128w<=Lblk and128u<=Lblk,
 I=16Lblk+128(w+u)<=18Lblk.
Use proof8's Cc<=22n^17/l,Cf<=2n^17/l,Lblk<=(65/64)n/l,
Y+E+6<=27l. Therefore
 fine selected cap<=180CfLblk<512n^18/l²,
 coarse selected cap<=22n^17/l *384w*27l
                     <=228096n^17w<=228096n^18/l²,
 Qcap<=(228096+512)n^18/l²<2^18n^18/l².                              (I.1)

Choose epsilon=1/(33554432 n^17)=1/(2^25n^17) for EVERY n>=1.
There is NO epsilon(1)=0 exception. By E.1,
 E C<=n/(128l²)<=w/32, P(C>w)<=1/32.
Coarse edits satisfy6C/Kc<=3/176; F's exact gap still holds.
Combine this Markov bound,clean extraction2^-10,coarse2^-20,progress
2^-20 and wrongaccept2^-20. Their sum is below1/3. The odd controller
uses the signed reconstruction B only on its correct accepted path;
for the twoadic analysis condition only on its ACTUAL correct odd past
and apply the same uniform estimates,then union the first error. No
future corruption-count event is used to condition a virtual law.

All four envelopes remain unchanged. Coarse root count O(w*l)=O(n/l),
ordinary/chain roots at most10I=O(n/l),selected budget shape
O((n²/l²)2^m). All known-label root widths obey proof14,and all
verification widths obey A's low-only memory lemma independently of j.
Hence T_tree=O((n³/l)2^(m+dl)),S_C=O(H2^H),S_Q=O(n).
Coarse score enumeration is streamed and costs a FIXED polynomial in n
times2^m despite Kc=Theta(w); it is absorbed byexp(dl). Stored coarse
records O(w*n),integer w/parameter/circuit generation,prefix stack,
all source/extraction steps,known-gate synthesis,PGM bin/rank tables,
full address charges,sorting/lookups,resets and all unused/padding copies
are fully charged. B=0 product vectors have at most2n^5 entries and
O(logn) quantum wires. No high physical-label table or quantum oracle
is hidden. Substitution of proof15's unchanged64-term ceiling ledger
proves exactly the four declared full structured resource envelopes.

Nonvacuity: proof8 gives dl>=n/(32l),2^m>=n^16/2,Cf>=n^17/(4l).
Qcap>=160LblkCf>=40n^18/l²,so
 epsilonQbank >=(5/4096)n/l²,
which grows without bound. This is an auxiliary allowed raw count,not
a fractional score substitution. Finite all-N correctness is separately
proved in proof18,including the positive epsilon at n=1.
