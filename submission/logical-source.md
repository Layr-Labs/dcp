# Complete balanced-sample logic

## 0. Source and bindings

Source 393ac17a-06b9-4c90-8348-be3eae837118 supplies fullroot/native0-5/ALL5helpers.
S1-7 EXACT;8 defines P_bal ACTUALicbrt(L²)/16 sample/ALLcaps/statistics/work.
S:RhoDen=10^256-2. CURRENT RH=10^256-3,rhoB=((2RH+1)/3)/RH.
LogicalSCn²/SQn; physicalSCnL^(2/3)/SQn². OldC2/3.4 binds S6-7/8/
FULLgraded-joint; LOCALD!=SEARCHD. All inheritedcreditsremain;
no absentlemma/oldcompleteoutputlaw/previousverdict premise.

## 1. Actual parameters and unchanged outer program

For n<2^4096 run the COMPLETE same-noise finite algorithm of native-source1,
including its original acquisitions, success>11/16 and every cleanup. For
n>=2^4096 use native-source0-2 CURRENT input/error/parameter bindings, n=ceil log2N,
L=ceil log2n,q=n+32,M=2^q,ell=ceil log2(L+2),v=1+ceil log2(ell+2).
The ACTUAL changes are B=(ell+1)^2v, u=min(u6,B), m=2^100u, u6leastu^6>=L;
recompute D=ceil(2^80M/m),root=ceil sqrtD,K,Hmax,all widths/precision/tables/
lists/Bcaps/abort/guard formulas of native-source2 with this m. Keep A=2^20,
C=2^24,bF=60+ceil log2q,g=128+2ceil log2q and Budget=2^28root. No old sample
or cap is used. The actual subset/filter/cubic coefficients/anchor/constant
guard/gradient preparation/graded constraints/stopped sixteen-attempt
sampler/champion/untouched endpoint/source schedule and abort outputs are
EXACTLY native-source2,5 and graded-source7-10, except the new base word and guards below.
ALL five helpers and COMPLETE selected current native proofs are supplied. No old
whole-program output law, clean-helper embedding or verdict is substituted.

## 2. Exact short decoder and its rounded finite word

Retain the source HIGH-end contiguous bF blocks and partial LOW last block,
ALL adjacent product diagonals, both-block staging, and ONE final GLOBAL
reversal. Replace a standard b-bit exact core by the inverse decoder below;
stage back its REVERSED output ports to obtain the source UNREVERSED core.
Source staging zeros its input window even if output entangles with aux.
All products, diagonal phases and reverses use the COMPLETE explicit Gamma arithmetic quantum words of native-source3, with NEW7 native format/controller, full padding/code/helpers.
No faster external multiplier or arbitrary rotation primitive is used.

Let d=2^b, |F_x>=d^-1/2 sum_y exp(2pi ixy/d)|y>. Form A_b by the OLD source
block-QFT word at width k=min(b,ceil log2(2^10(b+1))), starting at the HIGH
end with partial LOW block, keeping exactly same/adjacent-block pairs.
Each omitted CP term has absolute angle whose total is<=2pi b2^-k<1/2;
if k=b none are omitted. Telescoping gives ||A_b-F_b||<1/2. Set V=A_b^dag,
c_(y,x)=<y|V|F_x>, p=d^-1 sum_x|c_(x,x)|²>=3/4: Re c_(x,x)>=7/8 by
unit-vector distance, hence its squared modulus>=49/64. Choose ideal
theta=asin(1/(2sqrtp)), then compute a public rounded theta_t=2pi r/2^g
as in3. H below means bitwise Hadamard, not a Fourier primitive.

Registers I,O,S,E,R have widths b,b,b,1,b and start O,S,E,R=0. The literal
chronological U word is H_O;SUB(O from I);H_S;phase(-OS/d);V_O;
ADD(S to O);B(theta_t)_E. ADD/SUB use actual reversible ripple words;
phase products use explicit Gamma compute/gradient subtraction/reverse.
B(theta)=[[cos,-sin],[sin,cos]]. D is phase(-IO/d);H_I;
sign(I=0 AND E=1);H_I;phase(+IO/d). Let Rz=2|0_OSE><0_OSE|-I,
T=U;D;U^dag;Rz;U. Decoder=T;XOR O into R;T^dag;phase(-IR/d);H_I;SWAP I,R.
Every inverse reverses the LITERAL new finite gate word on all states.

For ideal theta, the first copy word maps |F_x,0> to |F_x,F_x>, a linear
copy of an orthonormal basis, not arbitrary-state cloning. After U the OSE
state is d^-1/2 sum_(z,y)c_(y,x-z)|y+z,z> tensor
(cos theta|0>+sin theta|1>). Marked O=x,E=1 mass is p sin²theta=1/4.
For fixed O=y, D tests overlap <0|H|F_(x-y)>=delta_xy, so preserves I's
Fourier label and flips precisely that marked part. U also preserves it.
U Rz U^dag is reflection about the actual U column. One reflection after D
multiplies good amplitude by3-4*(1/4)=2 and bad by1-4*(1/4)=0, with no
label-dependent phase. Thus T yields |F_x>|x>_O|chi_x>_SE. Copy x into R,
apply T^dag, then final phase/H/SWAP: result |x> with ALL auxiliaries0.
Linearity proves decoder F_b^dag including arbitrary reference coherence;
its inverse gives positive F_b. The full word has six B/B^dag occurrences.
Since ||B(theta_t)-B(theta)||<=|theta_t-theta|, telescoping bounds FULL
word norm error by6|theta_t-theta|<32*2^-g. Its adjoint has the same bound.
Only the O(b) logical copy/shift/flag/readback registers can retain rounding
junk. All arithmetic/carry/product/OR/private native scratch cleans for
arbitrary data/gradient states by exact compute/use/reverse, not merely on
ideal gamma. Rounding junk is handled coherently in4, never discarded.

## 3. Uniform public angle and elementary controls

Before the FIRST original acquisition, compile every public width's angle.
Represent V F_b by the directly specified naive H/CP/SWAP words of2:
EXACTLY2b Hadamards, other gates diagonal or permutations. A path starting
x chooses2b binary Hadamard outputs; its amplitude is2^-b omega^e,
including Hadamard signs as omega^(d/2), omega=exp(2pi i/d). Stream x and
ordered pairs of paths,2^(5b) pairs; retain only pairs both ending at x.
Then p=2^-3b sum cos(2pi(e-e')/d). No 2^b state array or nonuniform advice.

At P=g+2b+40 bits, compute rigorous cos intervals and round OUTWARD to
integer grid2^-P; accumulate their integer endpoints. Probability width
<=4*2^(-g-40), accumulator O(P+5b) bits. Machin pi=16atan(1/5)-4atan(1/239)
uses alternating sums with next-term bracket<=2^(-P-32). Use their midpoint
for x=2pi turns in[0,7]; Taylor cos through m=max128,P+16 terms has remainder
<=7^(2m)/(2m)!<=2^(-P-12). Add pi-width*turns by the Lipschitz bound, then
outward grid-round. Keep exact rational arithmetic; its bit work is counted.
Stream roots for b>4, cache at most16 for b<=4; pi cache constant-size.

For alpha=theta/(2pi) solve f(alpha)=2p(1-cos4pi alpha)=1 on[1/16,1/8].
Its derivative8pi p sin4pi alpha>1 there. Use p/cos intervals at g+40 bits.
At mostg+8 bisections suffice for interval width2^(-g-4): if a midpoint
comparison straddles1, derivative>=1 puts the root within the computed
max endpoint discrepancy of that midpoint; intersect with that interval.
Otherwise keep the indicated half. Round the RATIONAL midpoint to nearest
g-bit dyadic, ties decidable. Then |theta_t-theta|<4*2^-g; no exact real
rounding-tie oracle or unbounded search is needed.

P<=5L,b<=L+61,g<=2L+132 at L>=4096. Atan has<=P+40 iterations, rational
bitlength O(P²) even with product denominators; the cos loop has<=6L terms.
Even multiplying all term denominators gives intermediate size below
2^20(L+2)^4 bits. Schoolbook integer/rational arithmetic (allow cubic
Euclid cost) bounds each root by2^100(L+2)^16 bit work. Streaming compiler
space<=2^100(L+2)^20, time<=2^500 n^5(L+2)^100 since2^(5b)<=2^310n^5.
Bisection/word generation/clear fit these bounds. At L>=4096 space<n,
log2(time)<n/4; hence setup is polynomial-TOTAL, below2^(n/4), paid once
and cleared before original-bank coexistence. Public lengths/loops only;
no original datum or quantum control enters this compiler.

To implement phase P(2pi a/2^g) on flag, CNOT flag into the 1-bits of a
zero g-bit addend, SUBTRACT addend from the ordinary positive g-gradient
by the full MAJ/UMA inverse, then undo those CNOTs. This cleans addend/carry
for every gradient state, and kicks the stated phase on exact gamma.
B(theta)=exp(-i theta) S H P(2theta) H S^dag. Prepare a literal ONE, implement
P(-theta) on it by the same word and clear it. Thus global scalar is included;
the actual Clifford+T word is<=72g+8 gates, no arbitrary rotation primitive.

One extra active control costs at most31 gates per source elementary gate:
controlled-X=CNOT, controlled-CNOT=the exact supplied fifteen-gate CCX;
controlled-T/T^dag=compute flag AND target in a zero helper by CCX, apply
T/T^dag there, reverse CCX. Controlled-H follows R Z R^dag=H with
R=S H T H S^dag=e^(i pi/8)Ry(pi/4): apply R^dag, H-CNOT-H, R, seventeen
gates. R's scalar cancels exactly. All helpers clean including reference
entanglement. Source S gates expand as T²; all elementary operands remain
distinct and actual indexed-address/code generation is charged as in6.

## 4. Coherent first-failure wrapper and pointwise kernel

Use ONE shared O(polyL) short arena, O(b) logical core aux, failure index
ceil log2(numberBlocks+1) bits and active bit, all ACTUAL base work. Core j
computes active=[index=0] once, controls every elementary gate by it, then
conditionally on logical aux nonzero transposes index0 with index(j+1).
Earlier failures freeze future cores. Clear active using Eq0 XOR Eq(j+1).
On the base column active is again0. Elsewhere this is still a full finite
unitary; its ACTUAL inverse is used, with no off-column cleanup assumption.
Keep predicate-specific scratch disjoint from all base work.

The transposition is O(L) gates: pick a set bit p of the public j+1, CNOT
index_p into its other set bits to map j+1 to e_p, flip index_p controlled
on all other index bits0 AND auxNonzero, undo CNOTs. Zero-controls/AND-chain
use actual clean helpers. OR(aux), Eq0/Eqj cost O(b+L); undo OR after index
change since aux is untouched. Whole controller/address/gate costs count.
On base-column tag0 every earlier core's aux was0 and remains0. Thus its
scalar good block K_j=(I tensor<0|)W_j(I tensor|0>) is a contraction and
||K_j-F_b||<=32*2^-g. The final tag0 kernel FACTORIZES over the sequential
cores and unchanged adjacent diagonals; disjoint blocks and diagonals have
one intermediate label per fixed input/output, not a garbage sum. Its
relative entry error versus the old FLAT block word is
 eta<=product_j(1+32*2^-g*2^(b_j/2))-1<=2^(-L/2-80):
numberBlocks<=2^(L+1), b_j<=L+61,g>=2L+128 give sum factors<=2^(-L/2-91),
and exp(t)-1<=2t for t<=1/2. Therefore actual tag0 kernel entries differ
from full F_q by at most[2pi q2^-bF+eta]/sqrtM. Bad tags are NOT projected,
measured, reset, or ignored by the actual word; they are rejected by5.

## 5. Actual base weights, guarded search and unconditional success

Every fresh/exact graded predicate and final acceptance additionally requires
index=0. Both reject nonzero tags, hence discrepancy there is EXACTLY zero.
R0 tests the ENTIRE actual query/baseAux/index/active pool, catalyst excluded.
Let psi=U0|0> be this actual new base column, psi_a its projection to candidate
a with source successful flag/index and new failureIndex0, w_a=||psi_a||².
These orthogonal vectors retain arbitrary phases. On their support logical
core aux/active are0. Base U0 is identity on separate predicate scratch.
Each predicate sign and actual reflection2|psi><psi|-I preserve the span
of psi_a and remaining unmarked vector. The two-reflection identity gives
on nested P_j the marked vector F_j sum_(a in P_j)psi_a,
F_0=1,F_j=F_(j-1)[3-4W(P_j)F_(j-1)^2]. Thus source graded-source8 applies
with ACTUAL weights: accepted law w_a/W(P), contractionrho3/4, size-loss
sum<2^-18, stopped mass-band expecteddebit<2^16sqrtD, hard Budget failure
<2^-12. No uniform amplitudes or exponentially-many-call norm hybrid.

All count/filter/score/anchor/gradient exceptional events of graded-source3-7,10
remain, since2^100<=m<=2^100u6 and original record laws unchanged. Coefficients
obey ||htilde||1<=2m, coefficient loss<=2^-88m, true score>m/64 and nearest
point loss<5*2^-32m. The new kernel numerator loss is at most
2m(2pi q2^-bF+eta)<2^-55m+2eta m. Subtracting leaves>m/128, hence>=m/256.
The SAME true class weight>=m/(2^68M)>=1/D follows. No bad-tag probability
is compared with this exponentially small weight. The source near/far
margin336899/12582912>1/64 and fresh sketch survival sum<2^-22 use ONLY
unchanged coarse per-record phase/interpolator/threshold words, not base
flatness; their bounds remain and apply to EVERY proposed pivot. Full base
weights sum<=1. All other uses of biased base in graded-source6,8 require
only this pointwise lower bound and weighted identity, both proved here;
older uniform-pivot helpers apply only to the unchanged finite branch.

Thus stopped coarse failure remains<2^-11. The same full-original champion
and untouched endpoint are analyzed UNCONDITIONALLY with the literal fixed
joint-good marginal, not conditioning parity on base/search success. Sum
ALL losses of graded-source10, including one global exact-gradient latent
event, unchanged tails/labels/rejections and coarse budget, remains<3/128+
1/1024. Endpoint>=91/128 gives>703/1024>2/3. No per-call catalyst exception:
on exact gamma every new dyadic word preserves it, on its complement full
branchwise bounds still hold and the preparation exception is charged ONCE.

## 6. Complete runtime, space and exact declarations

All EXPLICIT Gamma/source3 arithmetic is retained. NEW controller7 replaces source3 C2 snapshot bridge, old d-bit code format and its cost. Full L fees, Pad2^120(L+2)^4, every actual compiler/arena address and cleanup count. Whole new core includes a CONSTANT number of products, ADDs,
V=A_b^dag calls, source primitive controls, Euler words, guard and reverses.
Its raw gate bound is O(b logb loglogb+g): old A_b costs
O(b(1+logk)^2(1+loglogk)), which is O(b logb loglogb); for logb>=12 this
follows (1+log(logb+12))²<=C logb with a fixed C, smaller values absorbed.
The explicit Gamma refined constants stay as source3; no external fast-size
premise. Partial low block's O(g) cost is separately included. New constant
control lifts/code words retain actual NEW full native O(D) decoding of7, not free
fields. There is NO remaining recursive Fourier-depth factor at width b.
O(n/L) full b=Theta(L) blocks therefore cost O(nL(ell+1)^2v), including
adjacent diagonals, both-block SWAP staging, one global reversal and all
O(L) guard gates/native field setup per core. Guards cost at most
O(nLell), within this ledger. Whole-entry NEW controller prefix init/clearO(L²)
per block and code/header selection are paid, not attached per inner gate.

Actual U*=nL(u+B). Source coefficient/frequency preparation and every
constraint/failed clock/generator/reflection/champion action retain
graded-source9 charged constructions with this ACTUAL U* and current2-7 complete word bounds. Hard pre-attempt token guards
bound EVERY branch by C nL(u+B)ceil sqrtD plus polynomial-TOTAL setup.
Balance u=min(u6,B) gives derived sqrtN nL(ell+1)sqrtv. For ell>=2^866,
(ell+1)sqrtv <=C L^(1/RhoDen): (log2L)/RhoDen eventually dominates the
log factors (at ell=2^866 its exponent budget>2^15 exceeds all fixed
source arithmetic constants, and the ratio subsequently increases).
Below that fixed ell threshold the actual bounded factor is an outside
constant. This proves EXACT declared T=O(2^(n/2)n(log2n)^(rho)),
not equality or optimality. Setup polynomialn is absorbed as proved3.

Repeated short code uses a constant number of source streams, public j and
g-bit angle fields, explicit controls and short guard words; its complete
allocation has bound2^280(Wpub+2)^12<Rshort=2^420(L+2)^16. All unused code
padding counts. Whole field/gradient/addend/product/compiler arenas and new
aux/index/active are O(polyL), with workspace reuse after cleared compiler.
Input/source/coefficient/record storage and source generator stack remain
SC=O(n²); ENTIRE genuine qubits including every unused/reserved cell remain
SQ=O(n). R0's extra polyL tests cost O(nL), catalyst excluded. No sparse
maximum-index interpretation is used. Code and pure classical compiler
workspace are real allocated bits and cleared. All branches including
wrong gradient, failure-tag, malformed report, abort and output-first
cleanup have these allocations and FULL word costs.

Acquire EXACTLY3*2^40(n+32) originals on EVERY branch, including unused ones
before abort; compiler precedes them and cannot fail or inspect them. No
work qubit is counted as a source; no source purification/preparationinverse
is available. The exact structured fraction1/3, four resource envelopes and
indices1,0,0,0 hold jointly for this ONE program and EVERY N/secret.

## 7. NEW complete specialized fixed-role native controller

## Real format, layout and fixed roles

Let d=ceil log2(4Rshort+2) be the needed offset width, D the least power of
two>=d, so d<=D<2d. Recompile immediate records as FOUR opcode bits then
three D-bit offsets, padded to power-of-two record strideSrec. Decode ALL
D bits, including leading zeros. Headers/PC/count/shift/base/argument fields
use D-bit words. This changes actual records, directory offsets, private
field layout and code-base headers; no old admission or output byte claim.
Genuine elementary gate words/order/roles remain identical after decoding.
Both program directions visit records in their correct order with actual
inverse opcode and forward payload-bit read, as in the current decoder.

Reserve constant many REAL aligned controller field slots, each D bits,
including every unused bit, plus D CLASSICAL marker bits first1/rest0.
Inside the Pad prefix keep separate actual READ/WRITE/marker descriptors
for each fixed role, carry/held bits, first/last fields and return control.
Actual full L-bit high-prefix descriptor fields are initialized ONCE per
whole entry, and counted. Each ready full address is its aligned fixed
role base plus low r=log2D position bits. This uses neither an arbitrary
indexed field base/index addition per access nor a free register reference.
All memory addresses are classical. Original source/gradient/query data
only controls emitted genuine gates, never controller addresses.

A constant number of once-per-record full D sweeps forms codeCursor by
actual PC shift/copy/add of codeBase, loads opcode/argument destinations,
updates PC/remaining and tests end. Source6's COMPLETE regular fixed-native
COPY/ripple/reverse engine already handles these sweeps in O(D+D) actions,
including prefixes/argument/branch/loop/index/return/instruction work and
true reverse. No arbitrary flat-record decoder is called to emit this
fixed controller. Fixed shifts/roles/boundary cases are finite microsteps.

## Payload and actual adaptive counter words

For each of four fields initialize its actual destination cursor and
left=width-1 by D real writes (four fields, constant O(D)). Repeat:
READ_C at ready codeCursor; WRITE_C at ready destination; increment both;
decrement left and stop on its actual underflow. Field widths are4 orD.
As before, left underflows precisely after width transfers; no per-bit
full-field left==0 scan. Actual arguments are filled bit by bit and serve
as existing address fields for the eventual gate emission. No word copy
or generic instruction fetch is silently charged as one bit operation.

An increment/decrement of a fixed role's D-bit cursor/sentinel word uses
its persistent READ/WRITE bit-role descriptors initially at position0.
Read old bit, write its complement, set carry=old (increment) or1-old
(decrement). If carry clears stop. Otherwise advance all ready bit-role
and marker descriptors by one low-r unit update; if that update wraps,
all D bits have been visited and return actual carry/underflow1. Continue
otherwise. On early stop at k>0, move all descriptors BACK by actual unit
decrements, reading the ready marker bit after each move; stop exactly
when it reads1 at0. Before return at k=0, a single marker read detects
that no move is needed. If the full walk wrapped it also already reads1.
Thus all role descriptors return to their actual initialized positions,
without copying a D-bit descriptor, rebuilding its high prefix, scanning
all r position bits each step, or decrementing a full sentinel at zero.
The marker strip/pointers/init/clear/read/write/branch instructions count.

The native engine is the COMPLETE supplied pc-controlled-source6, with
constant fixed microstep roles, existing real full-address fields and
signed unit strides. Here its loop skeleton has the additional ACTUAL
carry branch and marker-return branch just specified. Each selected logical
field bit needs constant native READ/WRITE/Boolean/branch/gate-generation
steps; positions are the represented native role descriptors, not general
logical-field indexed accesses. Descriptor updates are source6's actual
native carry walks. The refined count below applies to those real walks,
including their emitted bit addresses/indices/loop/argument/return actions.
It does not replace a full scan with a presumed O(1) integer operation.

## Deterministic count, including descriptor excursions

For an aligned descriptor that starts at zero low offset, 0->k uses
sum_(t<k)(1+trailingones(t))<2k visited bits; reversing k->0 changes the
same bits, so <4k. Constant-many READ/WRITE/marker roles retain O(k).
No carry reaches a high prefix. A full D-position walk wraps at D with
<2D visits; it already returns0. All loop/branch/marker actions are O(k+1)
per excursion. These are counts of ALL visited bits, not just data flips,
and they cover each adaptive stop separately without an extra +D or+r
initialization per excursion. The native engine's descriptor first/last/
prefix/return fields exist before the entry and are not copied again.
This bound uses the actual fixed-native instantiation above, not the diagnostic host realization of a ready operand.

For m consecutive D-bit cursor increments/decrements, logical bit i is
visited at most m/2^i+1, so all logical visits<2m+D, with any initial phase
and the final underflow/wrap. Descriptor excursion length is at most the
logical visits of that update; summing gives O(m+D) COMPLETE native actions.
For payload field widthw, two cursor increments and one left decrement
therefore cost O(w+D). Four fields total p=4+3D gives O(p+D)=O(D).
The constant complete per-record sweeps and actual gate emission add O(D).
Thus the COMPLETE new record word has O(D)=O(1+logL) native actions, all with FULL
L combined-memory fee. It never invokes the general fourteen-d bridge per
field bit. This is a real specialization to finite regular roles, not a
generic claim for arbitrary native field addressing or an instruction oracle.

## Whole entry, words and allocation

The COMPLETE new controller is the finite-state STEP/MOVE/BACK/RETURN word
above, with a fixed finite choice of cursor/destination/left roles and four
payload-field roles. Every old generic field-bit access in the decoder is
replaced by these actual ready-role operations. The only full-width actions
are the constant-many complete record-base/header/copy/add/PC/count/end
sweeps, O(D), already instantiated with the supplied native engine. There
is no remaining recursive call to an arbitrary short-record decoder, no
per-access full index snapshot/add/reverse, and no hidden direct memory
selection by a quantum value. The native source6 unit updates and FULL
microstep argument are used on their actual fields, with high prefixes
initialized once. The zero-start refinement above counts all their carry
visits and actual return/marker work rather than reinitializing the engine
per logical counter update. This is specialization to finite regular roles,
not a faster generic indexed-field primitive.

D-bit records, directory, stride/alignment, marker/controller fields, every
prefix and their generation/loading/clearing are paid. D<2d changes source
crude code counts by a constant factor. There are at most five public
width/role/shift parameters <=Wpub, a constant number of fixed templates
and <=2^160(Wpub+2)^4 elementary records per entry, including controlled
lifts/guard/constant words. Full record/header/directory/private alignment
and compiler storage are below2^280(Wpub+2)^12<Rshort2^420(L+2)^16. This
uses the EXPLICIT polynomial crude word bounds, not refined2^12500 as an
allocation. Genuine quantum offsets/catalyst/phase roles retain their old
layout; the opcode and full D-bit immediate offset produce the identical
intended elementary gate. Leading zeros and all reserved unused bits count.

The source Pad=2^120(L+2)^4 prefix contains the aligned fixed controller
fields/marker/descriptor pools and every unused cell; regenerate actual
code-base headers for the new format. Additional constant finite-state code
and fields have size<=2^100(L+2)^4. Full-prefix initialization/clearing costs
O(L²) per whole entry even if reusable, and O(n/L) entries pay O(nL).
Every emitted native bit/generation/branch/instruction/gate pays FULL L.
Private classical counter/carry/marker copies really clear at entry exit;
there is no retained transcript. All genuine quantum operations and TRUE
reverse order are unchanged, so source/query/gradient/reference channels
are identical to the current core/phase roles on ALL inputs. The complete
emitter bound is O(D)=O(1+logL) native actions per record, with arbitrary
starting cursor values, wrap/underflow and both program directions covered.


## 8. NEW sequential-program sparse preparation and actual integer-root sample

This section defines the CURRENT program P_bal; S denotes the complete reference
specialized-sweep program in1-7. For public L<2^156 execute S EXACTLY. For
L>=2^156, choose ACTUAL m=floor(icbrt(L²)/16), retain q=n+32,g,bF,C,A and the full
coarse/endpoint procedure, and recompute D=ceil(2^80M/m),K,Hmax,root,Budget,
every clock/width/precision/row/list/verification/abort cap from this m. No
source u6/min formula determines this main-branch sample. Use the NEW
frequency XOR/inverse below and U'=nL B, B=(ell+1)^2v, as the leaf ledger.
The actual native arithmetic/phase/controller S7 and exactifier S2-4 remain.

### 8.1 Explicit classical sequential controller and charged operations

Use a uniform fixed finite-state classical controller with a two-way
sequential PROGRAM TAPE for the immutable frequency-mask stream. Its local
transition reads/writes the one current bit, changes finite state, and moves
the head by at most one cell. These are fixed-size bit/head operations, NOT
a binary-indexed lookup at an arbitrary classical address. This is an
explicit choice of classical controller allowed by the uniform-controller/
bit-operation model: it is a finite machine, not a word-RAM, table oracle or
instance-dependent program. All other indexed classical operations continue
to pay FULL ceil log2(Memory+2); every quantum gate/measurement ALWAYS pays
that FULL address fee even when its operands were streamed. All tape bits,
read/head moves, output port bits, finite state, O(logMemory) head positions,
rewind and real initialization/clear are counted. No bit has zero read cost.

A tape transition accesses its head's current local bit and no indexed
memory address; it is not implemented by silently declaring a RAM read
at a stored index unit-cost. The machine/controller really has a sequential
head, with adjacent moves counted one by one. Its entire tape is physical
counted CLASSICAL storage. The rules' surcharge for an indexed access does
not add a binary address to this local finite-state transition. Counting
every head read as an indexed RAM operation instead would describe a
DIFFERENT, slower controller and would not prove the present bound. Thus
this explicit classical-machine construction, not just a Boolean circuit
size, is essential to P_bal. No quantum addressed memory is assumed.

The fixed transition table is independent of n, s, masks and outcomes.
Before repeated search, generate the actual mask tape by ordinary charged
bit arithmetic/transpose from measured filtered labels; its size is qJ.
Generation/testing/setup may use the original indexed controller and its
FULL L fees: their entire work is polynomial-TOTAL. A fixed loop reads J
mask bits sequentially into the actual control-address bit PORT, pads the
known high prefix, and writes the target-address PORT from a real regular
counter. Emitting both full O(L)-bit operands costs O(L) bit writes/head
moves, not a free word copy. Apply the addressed CNOT and pay FULL L.
Advance to the next actual tape row. After q rows rewind qJ cells, explicitly
paid. Reverse direction reads the same rows backward and emits the TRUE
inverse. Initial/final port clear is paid. No pointer jump skips tape bits.
All actual quantum address values are classical data and never selected
by a quantum register. The interface is exactly the permitted classically
addressed Clifford+T gate with supplied emitted bit-string indices.

The classical indexed engine used elsewhere and this local tape engine
are both finite parts of the uniform controller; switching is finite-state
control, with actual copied entry fields/prefixes counted. Local sequential
storage is not a new data source or advice. The proof uses the literal
fixed-size-logic and INDEXED-access distinction; it does not shorten the
fee on any existing indexed operation, including the source S7 engine.

### 8.2 Exact all-parity frequency XOR and full inverse

Let f_j,j<4r_f be the EXACT distinct nonzero frequencies of the filtered
records, J nextpower2>=4r_f, J<=8m<=L^(2/3)/2<=L/2. The branch/index/flag preparation
is exactly S's cubic-coefficient circuit. Into J zero one-hot wires compute
z_j=[branch=1 AND index=j AND j<4r_f], using explicit AND/CNOT words,
O(JlogJ) gates. On arbitrary branch/index input these are actual Boolean
functions, not known quantum data. Allocate separate zero parity wires
p_mask for ALL mask in[0,2^J), including p0=0. For each mask>0 let i be its
least set bit and parent=mask-2^i; apply CX(p_parent,p_mask),CX(z_i,p_mask).
Now p_mask=XOR_(j in mask)z_j. Actual parents/indices are generated by paid
finite tape bit scans, never a quantum-addressed table or generic polynomial-n interpreter per gate.

For frequency bit h=0..q-1, the immutable tape row is
 mask(h)=sum_(j<4r_f) f_j[h]2^j.
The sequential controller emits CX(p_mask(h),frequency_h). Reverse ALL
parity gates and one-hot gates. This XORs EXACTLY the original frequency
lookup on every branch/index/query vector: valid branch1 gets f_j, branch0
and invalid indices get0. All helpers0 again, including arbitrary reference
entanglement and failure flag. Since all operations are CNOT/Toffoli
permutations with true inverse, no phase or postselection is hidden. The
parity/output/reverse portion has EXACT4(2^J-1)+q CNOTs. All operands are
distinct; p0 is a separate constant-zero wire, not an invalid self-gate.

Mask tape has qJ<=q L^(2/3)/2 bits. Each output row costs O(J+L)=O(L) actual local
bit/head/generation work plus FULL L for its quantum gate. Total output
work/rewind is O(nL), not zero and not n gates with free addresses. The
parity-generation metadata uses explicit fixed-tape bit scans/counters and
O(polyL) work per mask, plus FULL L for each quantum gate: since 2^J<=2^(L/2)<=sqrt(2n), its whole work is
O(sqrt(n)polyL)=O(nL) eventually. Its bounded finite complement is an
outside constant. No classical operation is parallelized away.

Fix a separate dense parity capacity <=2^(floor(L/2))=O(sqrt n), one-hot
O(L), query q=O(n), source/catalyst and short arenas O(n). Count ENTIRE
physical prefixes/unused slots. Shift fixed quantum arena bases to disjoint
public aligned regions; compile real high prefixes once per entry. Short
code retains S7's small low-offset fields; long parity/output gates are
emitted by the explicit controller above with actual O(L)-bit addresses.
All move/init/clear/source work and every register are counted, SQ=O(n).

### 8.3 Exact index clearing by a bounded random injective hash

Include0 and all actual nonzero f_j in a label list of size<=J+1. Choose
khash=2ceil log2(J+1)+4 independent uniform binary q-bit rows. Pairwise
collision probability is2^-khash; union bound over label pairs is<1/16 for
ANY distinct list, including malicious classical labels. Test every actual
label; repeat at most256 independently, with actual abort on failure.
Failure<=16^-256 WITHOUT conditioning on good labels or search success.
Matrix generation/testing/table compilation are charged polynomial-TOTAL,
using at most O(nlogJ)+polyL classical bits. The fixed acquisition schedule
has already acquired ALL originals before any abort.

Apply the accepted linear hash to frequency by khash whole q-bit regular
CNOT sweeps, with real source6/S7 descriptors and FULL L fees. Into clean
scratch compute the inverse table on the khash-bit code by J equality/
controlled-XOR words; f=0 has code(branch0,index0), f_j code(1,j). Conditional
on the ORIGINAL coefficientflag0, XOR this code into branch/index. Reverse
table and hash. This is a unitary XOR permutation on EVERY frequency/code,
with TRUE inverse. On the base flag0 sector the frequency is supported on
the distinct actual label set, so the branch/index clears EXACTLY as S.
On coefficient failure it is not modified. Thus the ENTIRE base column
before the Fourier word is identical to S at the ACTUAL new m, not just a
postselected law. Different arbitrary-input extensions do not change the
reflection U0 R0 U0dag about that actual column. No source inverse appears.

Hash work is O(nLlogJ)+polyL, below nL B, since logJ=O(ell), B=(ell+1)^2v.
All arithmetic/table/AND helpers clean; only S's actual rounded-core logical
aux/index/active may be dirty, with exactly S's coherent guard and actual R0.
There is no data-dependent measurement inside the known base unitary.
R0 additionally tests the new actual parity/one-hot/hash work. Those helpers
are zero at base/predicate boundaries; its extra O(n) gates/FULL L fees fit
nL B. Rounded logical core aux/index/active remain actual retained base work,
never projected away or falsely asserted zero on all arbitrary inputs.

### 8.4 All numerical statistical premises at the new m

For L>=2^156 put r=icbrt(L²); r>=2^104, L^(2/3)/32<=m<=L^(2/3)/16,
2^100<=m<=L<=2^100L=the old proof's maximal m. Integer cube root uses counted public binary search/cubing,
r³<=L²<(r+1)³; no real primitive. All caps are recomputed, not old P's output law. Source k is
3*2^22(n+32), so m<=k. The proof of K>=n/9 used only
m*4096q²<=2^(n/2+112), valid here; D<=2^(2n),K<=n,Hmax=O(n),ell_max=O(L).
Full classical m*n,m²,m*g fit n². Actual L1 coefficient error bound
2^40m/G and ||htilde||1<=2m remain; the pointwise kernel margin therefore
still gives numerator>=m/256 and w_true>=m/(2^68M)>=1/D.

Private subset count/tails, label-only collision deletion, anchor/constant
guard and good-first cubic score proofs need m>=2^100 and the displayed
small collision256m²/N, NOT m<=u6. Their full supplied proofs apply and
the numerical losses remain bounded by S's stated allowances. Coarse
record sampling is IID from the FULL shadow bank, not the m subset; no
ell_max<=m assumption. All fresh/exact predicates, list laws/thresholds and
original full-secret champion remain. New base column equality and actual
rank-one reflection give the same guarded weighted pivots, contraction,
stopped band expectation and hard pre-attempt cutoff with the NEW D/caps.
Unconditional endpoint law is unchanged; hash failure adds at most16^-256.
Subtract it along with the existing S losses: main success>702/1024>2/3.
Smaller-L fallback S has its already supplied all-input same-noise proof.

### 8.5 Full new worst-branch ledger and exact objects

Coefficient preparation O(Jg+JlogJ) raw work with complete S7 costs polyL,
absorbed in nL B; new lookup/hash cost<=C nL B. Whole Fourier, every phase
role/constraint/generator/reflection, coins/clocks/debits/verification/reset
and failed attempts retain S's bounds with U'=nL B (NOT nL(m+B)). This
replacement is justified by the new actual forward/inverse words above,
not pretending the old m*n pattern loop is smaller. The graded recurrence
sum(t+t²)/3^t and actual hard token guard yield EVERY-branch
 T<=C U' Budget+polynomialTOTAL
   <=C sqrtN nL B/sqrtm+polynomialTOTAL
   =O(sqrtN nL^(2/3)(ell+1)^2v).
The new local tape/circuit controller costs are included in U'. All legacy
indexed work STILL FULL L. Hash compile and before-original theta compile,
mask transpose/tape generation/allocation/clear are polynomial-TOTAL; their
finite loops use actual bit work/space, bounded by a fixed polynomialn.
The parity workspace/address metadata term sqrt(n)polyL is separately
absorbed in nL B, not classified as a free or one-time exponential phase.

Let RH=10^256-3 and rhoB=((2RH+1)/3)/RH=2/3+1/(3RH). This exact fraction has
256-digit numerator/denominator and is the submitted logarithmic power.
For ell>=2^868, (ell+1)^2v<=C L^(1/(3RH)); the exponential-in-ell budget
exceeds2^15 already there, dominates the explicit fixed Gamma constants and
all logarithmic factors, and grows faster thereafter. Bounded complementary
ell and smaller-L fallback multiply an absolute outside constant. Thus
T=O(2^(n/2)n(log2n)^rhoB), index1, with SC=O(n²), ENTIRE SQ=O(n), index0.
Store all program/tape bits and head positions, hash/frequencies/source
records and every temporary, including old unused arena padding. No input/
program data sits in an uncounted external medium. Quantum gates are only
finite Clifford+T plus allowed measurement/source, with full address fees.
EXACT3*2^40(n+32) originals occur EVERY branch, including hash abort and
finite fallback; Q=O(n),index0. Exact fraction1/3/error-model text unchanged.
No matching lower bound, exact rate, infimum/O(nL^(2/3)) or optimality claim.
