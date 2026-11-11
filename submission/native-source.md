## 0. CURRENT bindings and exact arithmetic selection

Below3-5 are exact source Gamma/quantum/phase proofs, without obsolete C2.
Old0-2 are replaced by CURRENT1-2/full logical1/5/6/8 and joint/graded helpers.
Historical old3.4/B4 cost binds to currentlogical6-8, not a missing formula.

## 1. Exact input and finite reference

N>=2,n=ceil log2N,s moduloN; rho_s=N^-1 sum_x|psi_xs><psi_xs|,
psi_xs=(|0,x>+|1,x+s modN>)/sqrt2. EXACT model/context in manifest and FULL
joint-source1-2: fixed B before passive releases, joint good marginal
rho_s tensor(Q-|B|), arbitrary allowed bad-good/reference correlations,
no source control/purification/inverse. At n<2^4096 reference S executes
COMPLETE same-noise joint-source/SPTS-JM including finite cases, allQ,
success>11/16; full joint,spts,RQ proofs supplied.

## 2. Actual parameters and complete outer bindings

Use current logical1/8's ACTUAL m, q=n+32,M=2^q,
L=ceil log2n,ell=ceil log2(L+2),v=1+ceil log2(ell+2).
A=2^20,C=2^24,bF=60+ceil log2q,g=128+2ceil log2q,
D=ceil(2^80M/m),root=ceil sqrtD,Budget=2^28root.
K=max{j>=0:(64q3^j)^2<=D},Hmax=128K,A_j=3^j,
a_i=32+2ceil log2(i+1),ell_i=2^17a_i,
r_idx=ceil log2(2^24Hmax ell_Hmax),Bcap_j leastpower2 with
Bcap_j A_j>=16root. Recompute EVERY dependent width/list/clock/precision/
verification/abort cap at ACTUAL m. Integer powering/search/ceilings are
real finite bit work. Full source/EXTRACT/private split in graded1,
ALL Fisher-Yates/anchor/filter/guard/coefficient/weighted sixteen-attempt
clock/pre-attempt debit/class expansion/champion/untouched endpoint and
all refusal/abort/cleanup rules are COMPLETE graded2-10/joint1-6,
with currentlogical1-8's explicit word/statistical/kernel replacements.
No oldm complete output law or absent source is used.

## 3. Exact modular products and complete short instruction streams

Use the parent's EXPLICIT logarithmic Gamma arithmetic below UNCHANGED.
Its full exact ring/recurrence proof is reproduced; no external circuit-size
or fast-multiplication existence theorem is invoked. The actual changes are
WHOLE-entry compilation, local staging and the balanced sampler, not H(T).

Define Gamma_T(a,c)=(a*c) mod(2^T+1), in canonical residues0..2^T represented
on T+1 bits. Its public domain is ADMISSIBLE T: with x=floor(log2T), ell_x=ceil(log2(x+1)),
H(T)=2^max(2,floor(x/2)-ell_x), H(T) divides T. Full unsigned t-bit multiplication
M_t uses schoolbook for t<=128; otherwise choose T the LEAST power of two
with T>=2t, zero-pad both inputs to T+1 bits, and compute Gamma_T. Such T
is admissible and T<4t. Since x*y<2^(2t)<=2^T, Gamma_T is the EXACT full
integer product, with every bit above2t zero. Use its low2t bits, retaining
all high padding and garbage until the whole product reverse.

Gamma_T base T<=256 computes an actual (T+1)-bit schoolbook product, then
reduces by a real fold modulo2^T+1. For T>256, set

 x=floor(log2T), ell_x=ceil(log2(x+1)),
 H=2^max(2,floor(x/2)-ell_x), h=T/H,
 b=H*ceil((2h+log2H+2)/H), Q_local=2^b+1.                 (3.0)

Here H>=4, H^2<=max(16,T/(x+1)^2)<=T/9, h>=9H, and h is EXACTLY
integer. b is a MULTIPLE of H, need NOT be a power of two. The ACTUAL
pointwise recursion is Gamma_b, not a full unsigned b+1-bit product.
Descendant admissibility follows from monotonicity: for x>=8, floor(x/2)
never decreases. The ceiling ell_x increases only at x=2^k, where floor(x/2)
also increases by one; their difference therefore never decreases. Clamping
at2 preserves monotonicity. Since b<T, H(b)<=H(T), both powers of two;
H(b) divides H(T), which divides b. Strict shrink follows below.

Work in R=Z/Q_local with canonical b+1-bit residues. Put
eta=2^(b/H), omega=eta^2=2^(2b/H), so eta^H=-1 and omega^(H/2)=-1.
Use the H-point transform A_j=sum_i a_i omega^(ij) modQ_local.
Its COMPLETE radix-two word bit-reverses PUBLIC index order then visits
length2,4,...,H and every consecutive block: for i<length/2 compute
u+2^((2b/length)i)v and u-2^((2b/length)i)v moduloQ_local into fresh words.
All old fields remain. Inverse uses negative exponents and multiplication
by2^(-log2H). Root powers and every actual offset/loop are computed by finite
bit arithmetic. Public wire-list reindexing is compiled into actual local
offsets, not free motion or copying of unknown quantum data.

This inverse is exact even if Q_local is COMPOSITE. For a nonzero k moduloH,
write k=2^v k_odd and pair the character terms by shift H/2^(v+1). Their
ratio omega^(k H/2^(v+1))=2^(b k_odd)=-1, so the sum is0. For k=0 the sum
isH. Since Q_local is odd, H is invertible by the given power of2. Expanding
inverse*forward proves identity. The even/odd split of the defining sum
proves the specified radix-two word. No primality, prime search, field
oracle or approximate Fourier arithmetic is needed.

Encode each parent input a, whose low T bits have h-bit chunks a_i and
whose top bit is A, by the polynomial with first coefficient a_0-A and
remaining coefficients a_i. This represents a modulo2^T+1, since2^T=-1.
The first coefficient may be -1; all coefficient absolute values are<2^h.
Map them into the child ring by actual modular subtraction of the top bit.
TWIST coefficient i by eta^i, compute its H-point forward transform for
both inputs, then perform EXACTLY H pointwise recursive Gamma_b products.
Apply the inverse transform and UNTWIST coefficient i by eta^(-i).

Twisting proves the result is the NEGACYCLIC coefficient vector of the
product modulo z^H+1: for exponent i+j>=H the factor eta^(i+j-H) differs
from eta^(i+j) by -1, exactly the wrap sign. Each true signed coefficient
d_i has |d_i|<H2^(2h)<=2^(b-2). Hence the canonical child-ring residue
lifts UNIQUELY to that integer: compare with2^(b-1) and subtract Q_local
if greater/equal. Positive coefficients are below2^(b-2); negative ones
have residues above3*2^(b-2), so no boundary ambiguity arises. This is
exact signed lifting, not numerical rounding. Because z=2^h satisfies
z^H=2^T=-1 modulo the parent modulus, sum_i d_i 2^(hi) is a*c modulo2^T+1.
This proves the recursive arithmetic identity on every canonical input.

Actual finite ring words use fresh-target XOR/AND/NOT nodes, with CNOTs,
Toffoli and a fixed exact Clifford+T lift, plus X/copy. A fulladder uses
<=10nodes/bit. Complement-plus-carry subtraction, real sign/compare and
bitwise mux implement modular corrections. All canonical add/sub intermediates
fit b+4 bits. For a+b in[0,2Q_local-2] subtract Q_local once if needed;
for signed a-c add it if negative. A reusable signed reduction adds the
modulus if sign1, then compares/subtracts it if still >=modulus. All carry/
compare/select/sign bits remain GENUINE controls, never measured indices.

For a known power2^r reduce the public exponent modulo2b. If r>=b save
minus and replace r by r-b. Actual shifting/staging of the b+1-bit canonical
word and splitting at bit b gives z_low-z_high, in[-2^b,2^b]; correct once
and apply the known minus by canonical modular negation. Inverse exponents
use the SAME actual word. For base Gamma product z of2T+2 bits, write
z=z0+2^T z1+2^(2T)z2 and fold z0-z1+z2; this lies in
[-(2^T-1),2^T+2] and the same finite correction is exact. No whole integer
shift/product/division is a unit-cost operation. The word is defined on
all scratch bit states; functional/cleanup assertions use initialized helpers.

Signed recombination is O(T), not H full-length sign extensions/additions.
Since b+3<=3h, take each lifted d_i's actual sign and absolute b+3-bit
word. Mask its absolute bits into FOUR positive or FOUR negative tracks,
indexed by i mod4 at offset ih. Windows within any track are disjoint.
Reserve each track W=T+3h+10<2T bits. Sum the four positive tracks and the
four negative tracks separately with actual W-bit ripple. Each coefficient ends below T+2h, and summing four tracks needs at most
T+2h+2 bits, fitting W. Since H>=4 and h>=36, W<2T. Every nonnegative
subtotal fits W. For EACH subtotal Z, split at bitT and fold Z_low-Z_high;
W<2T makes this signed range(-2^T,2^T), corrected once into the parent
ring. Finally perform canonical modular subtraction of negative from positive.
This is Gamma_T's T+1-bit output. Every sign, comparison, track, upper bit,
transform, pointwise child and carry remains allocated until the WHOLE
product use/reverse. No child-local uncompute or recomputation is used.

The uniform widths are explicit. Put s=log2T and x=floor(s).
The clamped schedule satisfies H>=4 and
H^2<=max(16,T/(x+1)^2)<=T/9 for T>256. Thus h>=9H and

 b<2T/H+H+log2H+2 <=2T/H+2H,
 b<=3T/4, Hb<(9/4)T, b+3<=3h.                       (3.1)

For shrink use2/H<=1/2 and2H<=T/4 from h>=9H. For mass use
Hb<2T+2H^2<=20T/9<9T/4. For b+3, H+log2H+5<=3H<=h.
For s>=4096 the clamp is inactive. Since x>s-1 and
2^ell_x<2(x+1)<=2(s+1), floor(x/2)>x/2-1 gives
H^2>T/(32(s+1)^2)>T/(64(s+1)^2). Consequently

 b<32(s+1)sqrtT, log2b<=s/2+log2(s+1)+5,
 Hb/T<2+2/(x+1)^2<=2+2/s^2.                         (3.2)

These inequalities establish actual recursive termination and all widths.
The clamped small widths use their literal same Gamma words; no new fallback.

Each explicit modular add/subtract/root/fold/sign/mux word uses <=2^16b
nodes/retained slots by substitution of the real ripple bounds. There are
THREE H-point transforms, two twists and one untwist, H modular child
outputs, signed lifts, O(Hb)=O(T) copies and eight-track O(T) recombination.
A generous uniform LOCAL forward-node AND retained-slot count is
2^40 T(1+log2T), including all padding, literals, copies and fixed gate lifts.
Root/loop/table initialization and actual code generation are charged below.

Let F_G(T) count forward Boolean gates and A_G(T) ALL simultaneous retained
slots of Gamma_T. BOTH obey the same upper-bound recurrence

 F_G(T),A_G(T)<=H F_G(b)+2^40 T(1+log2T),
                       base<=2^10 T^2.                  (3.2)

Base includes the actual T+1-bit product and modular fold. The whole root
M_t is computed, used coherently, reversed in its ENTIRE DAG ONCE, then
literal1 fields X-cleared. Reverse topological order clears every fresh
target while preserving inputs and arbitrary references. There are H
FORWARD Gamma children, not2H clean child calls. All modular/transform/
track/child garbage is retained; the complete use/reverse costs O(F_G+T).

A crude bound F_G,A_G<=2^48T^4 follows inductively:
H b^4<=(9/4)T(3T/4)^3=(243/256)T^4. Local<=2^41T^2 fits the
13/256 slack, and base<=2^10T^2 fits too. This bound also supplies all
ACTUAL compiler/window allocation limits; no large refined analysis
constant below is used as an uncharged or excessively enlarged program.

For the refined recurrence define
 g(s)=s-2log2(s+1)-18, phi(T)=max(1024,g(log2T)).
For s>=4096, g(s)>=s/2, as holds at4096 with increasing slack.
Write psi=g(s)>2048. By(3.2), s'=log2b<=f(s)=s/2+log2(s+1)+5.
The function g is increasing for s>=2. Also b>=2T/H>=2sqrtT,
so s'>s/2>=2048. Since f(s)+1>=(s+1)/2,
 g(f(s))<=s/2-log2(s+1)-11=psi/2-2.
The clamp1024 is also <=psi/2-2. Therefore

 phi(b)<=psi/2-2.

The increasing function z log2z on z>=1024 and the mass bound(3.2) give
 H b phi(b)log2phi(b)/T
 <=(2+2/s^2)(psi/2-2)log2(psi/2-2)
 <=[psi-4+(psi-4)/s^2]*(log2psi-1)
 <=(psi-3)*(log2psi-1)
 <=psi log2psi-psi.
Here psi<=s implies (psi-4)/s^2<=1, and log2psi>=1 proves the last step.
Thus the target C T phi(T)log2phi(T) has slack C T psi, sufficient for
local2^40T(1+s) whenever C>=2^42, since psi>=s/2.
The ACTUAL finite family T<=2^4096 costs at most2^12336T from the crude
bound. Contracting that family is ANALYSIS ONLY, with no algorithm change,
external table or advice. With absolute OUTSIDE constant C=2^12500,

 F_G(T),A_G(T)<=2^12500 T phi(T)log2phi(T),
 M_t forward/retained/use/reverse=
 O(t(1+log2(t+2))(1+log2(1+log2(t+2)))).              (3.3)

The full root T<4t, zero staging/high bits and t<=128 schoolbook all count.
The huge factor2^12500 is solely an OUTSIDE analysis constant. Actual
compiler/window allocation uses crude2^48T^4 and actual code lengths,
not that refined constant as a real allocation or exponent coefficient.
Every modulus/transform/arity/sign/carry/track/child cost is included.
Standard Fermat/negacyclic FFT principles remain derived and credited.
The arithmetic schedule and its loglog factor are retained here. Only its
actual fixed Boolean words are inlined by the complete-entry compiler below.

Generate COMPLETE short core/twiddle/phase-entry words ONCE BEFORE first
source acquisition, including all
nested Gamma/M/root/track operations, true gradient/accumulator adders,
constant preparation/clearing and WHOLE product reversals. Every Boolean
XOR/AND/NOT fresh target has its fixed CNOT/Toffoli/X Clifford+T lift;
all macros are inlined down to actual elementary gates. Equal AND controls
are normalized to one CNOT to the fresh target BEFORE lifting; fresh targets
never alias inputs. Every emitted gate has legal distinct operand wires. One exact CCX(a,b,c)
lift, in chronological order, is Hc,CXbc,Tdag_c,CXac,Tc,CXbc,Tdag_c,
CXac,Tb,Tc,Hc,CXab,Ta,Tdag_b,CXab; its eight basis columns verify directly. Recurse on a short
core as high-child, product twiddle, low-child to single H, WITHOUT internal
wire reversals. This is code generation, not runtime recursion or an oracle.

Set W_pub=8(L+128)<=9L. Even compiling all tuples of at most FIVE public
width/role/shift fields<=W_pub suffices for every actual entry. Each has at
most2^100(W_pub+2)^4 elementary gates from crude(3.1)-(3.3) and
2F(t/2)+Ct^4. All immediate code/headers/compiler workspace fit
2^201(W_pub+2)^12, within R_short=2^420(L+2)^16. This bound comes from the
EXPLICIT crude recurrence, never2^12500 refined constant as allocation.
Generation, loading, every actual descriptor bit and final clearing are
paid polynomial-TOTAL work. No truth-table search or preloaded advice.

Reserve/count separate actual classical code/compiler and genuine short
arenas of R_short bits/qubits, including alignment and UNUSED padding.
Put the short arenas first in their typed memories (aligned base0); count
the complete allocated prefixes and every unused cell. Place all short query-input slots, the ordinary g-bit catalyst, distinct
phase accumulators and product/carry pools at fixed disjoint local offsets.
Compile each width's local-to-arena renaming INTO its immediate fields;
only the actual query block width is staged. Never overlap the live catalyst
with a phase accumulator. All actual fields and output slots are distinct.
For L>=4096,420+16ceil(log2(L+2))+3<L-1, so these pools are O(n).
Let d=ceil(log2(4R_short+2))=O(1+log(L+2)); full physical addresses still
have O(L) bits. Fixed aligned arena prefixes are actual counted fields,
formed ONCE, with real low offsets; no sparse uncounted address range.

## 4. A new flat Fourier word from product twiddles

Start with the source q-bit positive QFT order: r=q-1 down to0, H_r and
controlled phases of angle2pi/2^(r-k+1) to k<r, then final wire reversal.
Partition the physical query indices into contiguous blocks of width b_F,
starting at the high end; a last low block may be shorter. Apply the EXACT
QFT within the highest block, then ALL cross phases to the immediately next
lower block, then its exact QFT, then its cross phases to the next, etc.
Omit ALL interactions between nonadjacent blocks. This is a NEW gate word.
An internal core is UNREVERSED, including every recursive child; keep
exactly ONE final GLOBAL wire reversal. For EACH whole block, SWAP it into
zero fixed short-arena input slots by three CNOTs per bit, execute the
COMPLETE compiled core there, then SWAP back. Do NOT CNOT-clone before H.
For each adjacent diagonal, SWAP both blocks into separate local slots,
execute its full compiled product/gradient word, then SWAP both back.
The ordinary g-bit catalyst is allocated at its fixed arena location from
initialization and never measured/moved/reset at a call boundary. Separate
accumulator/product slots are counted, disjoint from this live catalyst.

For every query/catalyst/reference vector, SWAP-(U on the staged wires)-SWAP
acts exactly as the reference U on the original wires and restores the
added zero window. This follows by wire permutation and linearity, not an
ideal-gradient assumption. Product scratch also cleans for every such input
by exact compute/use/reverse. Thus every CURRENT role's full instrument is
preserved, even on bad gradient components. The actual sampler/caps below
change, so the OLD complete output law at its old sample is not substituted.
Every aligned boundary has new helpers0; extending R0's zero test to these
helpers therefore gives the same reflection on the zero embedding. It still
excludes the live catalyst. Its extra O(polyL) gates fit O(nL) charged work.

Whole-entry code/header selection is paid polynomial(logL) per block, never
per inner gate. NEW bridge fullprefix startup/clear additionally costs
O(L²) per whole entry, O(nL) total as3 charges, not an inner-gate cost.
Persistent global query/coefficient pointers use fixed
strides and real carry/underflow walks. In m updates of a w-bit pointer,
bitj is visited O(m/2^j+1) times, total O(m+w); the full supplied native
sweep construction includes descriptor setup and reverse passes. Long
prefixes are initialized once per whole scan; short arena pointers reset
with their real d-bit work. Every stage bit, gate and pointer action pays
FULL L. Hence all whole-block/adjacent staging is O(nL) plus paid entry
headers, within the ledger below. No per-gate L-bit address is rebuilt.

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

For the COMPILED t-bit internal core, count concatenated subwords by
two half-size cores plus(3.4), with NO runtime calls. This is a word-length
and charge recurrence. At each depth widths sum to at most t, and all roots have
width<=t. Monotonicity and O(1+log(t+2)) levels give
 C L Z'_L t(1+log2(t+2))^2(1+log2(1+log2(t+2))),
including ALL tiny-call selection/argument setup. Adjacent-block twiddles
have no larger bound. There are O(q/b_F) blocks, b_F=Theta(L). Put

                         B(ell)=(1+ell)^4 v, v=1+ceil(log2(ell+2)).

The COMPLETE paid word and actual adjoint, including final reversal, cost

                         O(n L B(ell)).                   (4.2)

The FOUR powers count ONE from the explicit unchanged logarithmic Gamma
arithmetic, TWO from the complete regular-native bridge controller and ONE from
the COMPLETE Fourier depth sum; v bounds the arithmetic loglog factor.
The new whole-entry word has no extra runtime nested dispatch/remapping
factor. Every real bit/descriptor/generation/instruction/gate/address fee
is retained. Fixed padding changes only outside constants; no depth is lost.

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
external copies/additions use O(t+H)=O(L) core actions, included in the raw bound (3.4).
Thus a full phase evaluation and its ACTUAL reverse cost

                         O(n L B(ell)),                   (5.2)

using(3.4), O(n/L) COMPLETE inlined product/shift/accumulator/reverse
entries and paid external staging. All source scalar/interpolator/threshold
words keep their full native costs, absorbed by nL; no slow generic
interpreter is invoked per repeated query. Code is independent of coefficient
values, which enter genuine local basis slots at classical record indices.
Only whole-entry headers/roles are selected. Persistent opposite block walks
and all global addressing/setup retain their source paid bounds.

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

