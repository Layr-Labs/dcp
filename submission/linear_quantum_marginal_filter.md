# Complete deterministic phase-filter proof for LQ-MARGINAL

This is required evidence with [the main proof](linear_quantum_marginal.md)
and [the complete controller](linear_quantum_marginal_controller.md),
and [the joint-input proof](linear_quantum_marginal_model.md).
All five claims cite all four current proof files. Sections 2--10 give
the complete selected parameter, full-input module and inverse,
deterministic probability bound, fixed recursion, retained-leakage
verification, known-undo interface and charged resource proof. Main
Sections 1--5, 7--8 and model Sections 1--8 contain the complete selected
source/model/score/precision, gradient and endpoint proofs. Main Section 10
gives exact source credits, including material E joint-model use.
No prior verdict or omitted external theorem is a mathematical premise.

## 1. Exact direct and inherited sources

The direct semantic source is public submission
6e8dae83-9556-4fa1-9e3e-0237b7083742, commit
2f4f96f7fe3fe58cbf815ea0e2158ab562f2f777. Its full needed mathematical
content is included in the current main proof. The complete literal
controller method is the public E controller credited in main Section 10.
E's dyadic selector argument was read after the symmetric proposal;
its exact public member, commit, hash and read passage are recorded there.
The dyadic identity is not claimed as new. The semantic source's inherited
ROB-G2/R24/EP-A and Ambainis--Kokainis--Vihrovs credits are retained there,
without claiming direct consultation of those original sources. No general
variable-time-search theorem is used. The full proof follows.

## 2. One complete parameter and register rule

Let n=ceil(log2 N), K=2^n, and M=2K. As in the source, C=N for odd N and
C=N/2 for even N. The classes are singletons for odd N and
{v,v+N/2}, 0<=v<C, for even N. Retain every source parameter outside the
replaced selector and verifier, including Q, all label/score precisions,
the 80 gradient-preparation cap, and the final trit threshold Q/3.

Use the square-root scale

    a_n=ceil(sqrt(n+1)), A_scale=2^64*a_n,
    L=max{j>=0:9^j<=K},
    B_j=least power of two >=A_scale*3^j,
    b_j=log2 B_j, j=0,...,L,
    R_v=4n+128, D_attempts=1024.                     (D2)

Here L is recursive depth; ell=log2(n+2) is the logarithmic cost variable.
No selector seeds or random Grover times are drawn or used. This does not
remove the source's axis randomness, acquisition measurements, or gradient
preparation. No delivery is repeated or added.

Each retained attempt has candidate v on n qubits, opponent w on n+1
qubits, one stopping word z, ONE logical probe b_probe, and its fresh
verification-output bit. All start at zero before that attempt's forward
preparation. The shared verifier has its own opponent, stopping word and
ONE logical probe. These logical probes are included in allocated work,
retained after actual leakage, and acted on by the complete literal words.
They are not Boolean scratch that is assumed zero on arbitrary logical
input. Clean arithmetic/Boolean helpers are separate.

For N=2 the selector and these selector probes are omitted, as in the
source. The source's Q rule, gradient and final endpoint remain in force.

## 3. The literal Grover sign and the symmetric probe

For a fixed candidate v and fixed computational row-record string, let
D_v(w) mean v<C, w<C, w!=v, and w beats v in the source's class tournament.
The predicate uses at most four source pair signs, has reusable linear
quantum scratch, and is exact for every record string. Let d be its marked
count. For valid v, 0<=d<C<=K, so a=d/M<1/2.

For d>0, let u_0 and u_1 be the normalized uniform unmarked and marked
vectors. Write sin^2(theta)=a, with 0<theta<pi/4, and use basis (u_0,u_1).
Let R_D=diag(1,-1), R_u=2|uniform><uniform|-I and G_v=R_u R_D.
The exact source sign gives

    G_v=[cos(2theta),-sin(2theta)]
        [sin(2theta), cos(2theta)]
       =cos(2theta) I+sin(2theta) J,
    J=[0,-1;1,0], J u_0=u_1.                       (D3)

The controlled implementation preserves this sign. In particular a
controlled diffusion made from H, a zero phase, H has its additional
controlled minus corrected by Z on the unchanged active flag, as in the
source/controller proof. A replacement by -G_v is not permitted. Every
G_v^(-1) below is the actual inverse word R_D R_u, with the same exact
controls and full address costs. No phase approximation is used.

For any positive integer t, start a probe in 0 and apply chronologically

    H_probe, controlled-on-probe G_v^(2t), H_probe, G_v^(-t).

Before the last word, probe outcomes 0 and 1 have operators
(I+G_v^(2t))/2 and (I-G_v^(2t))/2. Since the powers commute, after it the
operators are exactly

    K_0=(G_v^(-t)+G_v^t)/2=cos(2t theta) I,
    K_1=(G_v^(-t)-G_v^t)/2=-sin(2t theta) J.         (D4)

Thus from u_0 the two components are

    probe 0:  cos(2t theta) u_0,
    probe 1: -sin(2t theta) u_1.                   (D5)

The signs are retained scalar amplitudes. Failure restores exactly the
same unmarked direction, and success lies exactly in the marked subspace.
When d=0, the uniform opponent is fixed by G_v. The two H gates cancel on
that state, no success occurs, and the opponent remains uniform. This
empty case is also why the literal controlled sign in D3 is required.

## 4. A total module on every logical input, and its actual inverse

Assign a distinct nonzero code c to this probe. At module entry compute
the Boolean helper

    alpha=[z=0 OR z=c].

The following is the complete chronological module. All G_v iterations
are emitted even on stopped quantum branches.

1. Apply an unconditional H to b_probe. Compute f=alpha AND b_probe in
   a clean helper. Apply G_v exactly 2t times controlled on f. Uncompute
   f from the unchanged alpha and b_probe BEFORE the next H.
2. Apply the second unconditional H to b_probe. Apply the literal inverse
   G_v exactly t times, each controlled on alpha.
3. Compute f=alpha AND b_probe. For each 1 bit of the classical constant
   c, apply CNOT from f to that bit of z. This exchanges 0 and c when
   alpha=b_probe=1, fixes the other code words, and preserves alpha.
   Uncompute f BEFORE changing b_probe.
4. Compute D_v(w) in clean predicate work, XOR alpha AND D_v(w) into
   b_probe, and reverse the predicate computation. It does not change
   v,w,z or the read-only records.
5. Recompute the same membership predicate from the new z to clear
   alpha. Clear every comparison and Boolean helper by its literal
   reverse word.

The saved alpha is valid after Step 3 because z in {0,c} is invariant
under the guarded exchange. Step 4 leaves z unchanged. The conjunction
helpers are erased before either of their defining bits changes. D_v is
independent of b_probe, so its helper can be cleared after the probe XOR.
These facts hold for every logical word, including arbitrary probe values
and superpositions. Every clean Boolean helper returns to zero.

If alpha=0, all controlled words and permutations are inactive. The two
unconditional H gates cancel exactly, even for an arbitrary input probe.
Thus all earlier stopped codes outside {0,c} are fixed. If alpha=1 and
the reachable input is z=0, b_probe=0, opponent u_0, D5 followed by Steps
3--4 gives

    cos(2t theta)|z=0,b_probe=0>u_0
      -sin(2t theta)|z=c,b_probe=0>u_1.             (D6)

The same probe is therefore zero at every completed reachable module.
No intermediate measurement, fresh probe, per-probe history, reset or
irreversible assignment occurs. This conclusion is not asserted for an
arbitrary logical input; such an input is still acted on by the total
unitary just specified.

The inverse is the exact reverse sequence of ALL elementary gates. In
particular it first computes the final membership flag, reverses the
controlled D XOR, reverses the code exchange, applies controlled G_v^t,
H, controlled G_v^(-2t), H, and clears the initial membership flag, with
the corresponding conjunction and predicate words in reverse order.
There is no inverse of a measured check and no assumption that the input
probe is zero. Module inversion retains the same code-invariance argument
and returns all clean helpers to zero on every logical word.

## 5. Finite codes, blocks and complete prepared states

A dyadic block at scale B_j=2^b_j consists of the b_j modules

    h=0,...,b_j-1, t=2^h.

E_j contains TWO such blocks, each with its own distinct codes. Set
S_j=sum_(i<j)b_i. One explicit coarse-code rule is

    c(j,r,h)=3+2S_j+r*b_j+h,
    r in {0,1}, h in {0,...,b_j-1}.                 (D7)

Code 1 still records invalid v and code 2 still records an initially
marked opponent. Those two initial checks are the source's reversible
predicate-controlled exchanges of 0 with the indicated code. They do
not use or change b_probe. A coarse stopping register of width

    ceil(log2(3+2*sum_(j=0)^L b_j))

contains every selected code. Since L=O(n), b_j=O(n), there are O(n^2)
codes and this width is O(ell). No current code is reused by a later
coarse module. No code has to store an entire opponent or probe history.

Define F_j as follows: start the whole logical attempt at zero, prepare
uniform v over K and uniform w over M by H gates, make the invalid and
initial marked checks, then execute E_0,...,E_j. Let q_j and q_j^false
be its live and false-valid live probabilities, with live meaning z=0.
On an initially valid false candidate, failure of the initial marked
check leaves u_0. D6 then applies successively. Every earlier nonzero
code differs from the current module's code, so that branch is fixed.
The completed F_j state has b_probe=0 on every branch. This includes
invalid candidates and initially marked opponents. At a source vertex
d=0, all checks and modules leave the uniform opponent and code zero;
its contribution to q_j is exactly 1/K.

Every integer in D7 is public. S_j can be generated once along with the
public bounds; schoolbook code computation takes O(ell^2) raw work per
module. Its buffer is retained while its bits are used, and reused later.
No expanded module or gate program is stored.

## 6. Deterministic failure and the tournament sum

For B=2^b, the product identity obtained by b uses of
sin(2x)=2sin(x)cos(x) is

    product_(h=0)^(b-1) cos(2^(h+1)theta)
      =sin(2B theta)/(B sin(2theta)).               (D8)

On the all-failure branch each completed module restores u_0. Hence the
one-block failure probability, conditional on that direction, is

    product_(h=0)^(b-1) cos^2(2^(h+1)theta)
      <=min(1,1/(B^2 sin^2(2theta)))
      <=min(1,K/(B^2 d)).                          (D9)

The last inequality uses sin^2(2theta)=4a(1-a)>=2a=d/K. The two blocks
at a scale leave probability at most min(1,(K/(B^2d))^2). No statistical
independence is used: the two scalar failure factors multiply on exactly
the same restored direction. Previous-scale factors and failure of the
initial marked check are at most 1.

Fix any good record string with the source vertex. The source's tournament
count says that fewer than 2x false vertices have indegree d<x for every
real x>0. For completeness, a set of h vertices all with indegree <x has
h(h-1)/2 internal incoming edges and total indegree <hx, so h<2x+1.
The source is one such vertex for every x>0; removing it gives the stated
strict false-vertex count. All false vertices have d>=1.

Put t=K/B^2. Vertices with d<t contribute less than 2t to the sum of
their two-block survival upper bounds. In each bin

    2^r t<=d<2^(r+1)t, r=0,1,...,

there are fewer than 2^(r+2)t vertices and each contributes at most
2^(-2r). The bin contribution is therefore at most 4t*2^-r. Summing
the geometric series, including the low-degree set, gives

    sum_false min(1,(t/d)^2)<=2t+8t=10t,
    q_j^false<=10/B_j^2.                           (D10)

Empty bins, including all bins below the minimum integer degree, cause
no exception. If t<1 the low set is empty. This argument is deterministic
for EACH fixed good record string. False-edge transitivity is not needed.

Retain the source's exact index range

    Z=sum_(j=0)^(L-1)9^j*q_j^false,

with empty sum zero when L=0. Since B_j>=A_scale*3^j, L<=n and
a_n^2>=n+1, D10 gives

    Z<=10L/A_scale^2
      <=(10/2^128)*n/(n+1)<1/64.                   (D11)

This is a deterministic inequality, with no seed event or Markov bound.

## 7. The fixed recursive amplification and reachability

Use the source's literal words

    Trip(V)=V R_zero V^dagger O_live V,
    V_0=F_0, V_j=E_j Trip(V_(j-1)), j=1,...,L,
    O_live=I-2P_[z=0].                             (D12)

Products compose right to left. R_zero=2|0><0|-I acts on the current
candidate, opponent, code AND its logical probe. It excludes the read-only
records, gradient, other attempts, verification-output bit and clean
Boolean helpers. Including the probe is necessary: it is part of the
unitary logical workspace. The exact zero test and corrected global sign
use O(n) gates, as in the controller proof. There is no extra quantum
recursion stack or live-time estimate.

For psi=V|0> and p=||P_live psi||^2,

    V R_zero V^dagger=2|psi><psi|-I,
    <psi|O_live|psi>=1-2p,
    P_live Trip(V)|0>=(3-4p)P_live psi.             (D13)

Moreover Trip(V)|0>=2(1-2p)psi-O_live psi. Thus it creates no code or
probe support absent from psi. This proves reachability inductively:
before E_j its state is a linear combination of the preceding prepared
state and its live sign flip, all previous stopped codes are old codes,
and b_probe=0 on every term. Every code used in E_j is new. E_j therefore
fixes all previously stopped terms and only filters the preceding live
component. Its own success components have distinct nonzero codes.

If p_j is V_j's prepared live probability, induction gives the exact
direction identity

    P_live V_j|0>
      =[product_(h<j)(3-4p_h)]P_live F_j|0>.        (D14)

Signed cosines and the success signs in D6 do not invalidate this vector
identity. E_j is the same linear word in both sides, stopped-code
subspaces are orthogonal, and the scalar factors in D13 are literal.
There is no assumption that a failed amplitude is positive.

Since |3-4p_h|<=3, p_j<=9^j q_j. On a fixed good record, q_j=1/K+q_j^false
and D11 implies

    sum_(h<L)p_h<1/8+1/64=9/64.

Each x_h=(4/3)p_h lies in [0,1). The elementary induction
product(1-x_h)>=1-sum x_h therefore gives

    product_(h<L)(3-4p_h)>=(13/16)*3^L.

The source component in F_L remains exactly uniform/live. Thus a fresh
V_L returns that source with probability at least

    (169/256)*9^L/K>169/2304>1/16.                 (D15)

The strict lower bound follows from K<9^(L+1). For L=0 all products and
the Z sum are empty; the same inequality holds. It is valid without any
selector seed and for every fixed good record string.

The chronological forward call for j>0 is

    V_(j-1), O_live, V_(j-1)^dagger, R_zero,
    V_(j-1), E_j.

Its literal inverse is

    E_j^dagger, V_(j-1)^dagger, R_zero^dagger,
    V_(j-1), O_live^dagger, V_(j-1)^dagger.

All modules, checks and local arithmetic are reversed as defined above.
Reachability is used only for the success proof. The full inverse words
remain defined on every logical input, including nonzero probes.

## 8. Deterministic shared verification and 1024 retained attempts

For read-only v let W_v use its separate shared logical opponent/code/probe
workspace. Starting that workspace at zero, it prepares uniform w, makes
the invalid and initial marked checks, then performs R_v SINGLE dyadic
blocks at scale B_L. Give each (repeat,h) module a new code, for example

    c_v(r,h)=3+r*b_L+h,
    0<=r<R_v, 0<=h<b_L.

Its code width ceil(log2(3+R_v*b_L)) is O(ell). The complete W_v is the
literal full-input unitary of Section 4 composed with the exact initial
preparation/checks. The output predicate is [z=0 AND v<C]. It is exactly
1 for the source and exactly 0 for invalid v on the prepared inner-zero
subspace. No preparation is treated as a reset on arbitrary inner inputs.

For a valid false vertex d>=1, maximality of L gives 3^L>sqrt(K)/3.
Consequently

    K/B_L^2<9/A_scale^2<1/4.

Each failed block restores u_0; D9 therefore bounds every false vertex's
acceptance probability by

    (K/B_L^2)^R_v<(1/4)^(4n+128)
      =delta_det=2^(-8n-256).                      (D16)

There is no seed or union-bound exceptional event. The statement is
simultaneous for all false candidates on every fixed good record string.

Execute W_v, XOR its predicate into the fresh verification-output bit,
and execute the actual W_v^dagger. If P is its conjugated predicate
projector on the inner work, the resulting comparison with the correct
Win(v) XOR and unchanged inner zero has squared vector error exactly
2 times the wrong-predicate probability. For example when Win(v)=0,
the two nonzero error terms are -P|0> on output 0 and P|0> on output 1,
which are orthogonal. The Win(v)=1 case uses I-P. Thus D16 gives

    vector error<=sqrt(2 delta_det)<2^(-4n-127).    (D17)

The estimate uses the fresh verification-output bit in 0. The physical
controlled XOR remains a full unitary on arbitrary output-bit inputs;
that larger subspace does not need the D17 error bound. For superposed v
the stated estimate holds blockwise in v, and hence in norm, including
entanglement with the retained attempt or an inaccessible environment.
The stated bound is on the initial-inner-zero subspace. On an arbitrary
inner state, including actual leaked probe/code/opponent work, the exact
W, controlled XOR and W^dagger are used and remain unitary.

Make exactly 1024 fresh logical attempts. Run V_L and then this verifier
with a fresh output bit for each, sharing the same verifier workspace.
Retain every attempt register, probe and output bit. Compute the first
valid verified candidate into the answer, or 0 if none, with the source's
total reversible first-verified logic. No measurement, abort or retry is
conditioned on verification success.

For the comparison circuit replace each verification by the exact Win(v)
XOR and identity on its inner work. At fixed good records the fresh V_L
calls act on separate zero registers, so D15 gives total miss probability

    <(15/16)^1024<2^-64.

Every preceding IDEAL verification leaves its shared work zero. A
telescoping hybrid therefore uses D17 only on that initial-zero subspace
and gives total vector error

    <1024*2^(-4n-127)=2^(-4n-117)<=2^-121

for n>=1. Later actual gates preserve vector norms. Actual leakage is
retained and counted; it need not be zero before a later actual call.
For normalized states, any outcome probability differs by at most twice
their vector distance. The verification probability loss is <2^-120.

Every selector operation preserves the computational row-record values.
For each retained acquisition transcript ell its selector word is
sum_x |x><x| tensor S_(ell,x). Taking the answer trace sets x=x', even
when records are entangled with an inaccessible reference. Thus the
physical answer law is the average of these fixed-block laws under the
good-first measured-record law of main Section 5 and model Sections 4--6.
The actual unconditional coarse error is

    e<2^-80+2^-64+2^-120<2^-60.                    (D18)

The fixed B is used only in the proof. Good and bad systems need not
factor. No success is conditioned on all labels or on accurate decoding.
Model Section 6 supplies the full coherent-block operator calculation.

## 9. Complete known undo, source calls and the endpoint interface

Let U_ell be the complete known physical coarse unitary at the classical
acquisition transcript ell: create the source's coherent axes/row records,
run the 1024 preparations and verifications above, and compute the answer.
It uses no fresh DCP source, including inside any G_v, W_v or inverse.
U_ell preserves the records used in its tests, is finite, and has an
actual gatewise inverse on all logical input states. For a purification
psi of the compressed bank, ideal gradient and zero work, write
Pi_z=U_ell^dagger P_z U_ell. Copy only the answer and apply U_ell^dagger.
The exact output is

    sum_z |z>Pi_z|psi>.

Its squared vector distance from |z_*>|psi> is 2(1-p), where z_* is the
correct class and p=<psi|Pi_(z_*)|psi>. The same calculation applies to
the direct-sum purification over retained acquisition transcripts and the
inaccessible reference. D18 is unconditional, so this distance is <2^-29 after
conversion to trace distance. No inverse acquisition, unknown-state
preparation inverse, or assumption about actual zero work is used.

Retain/count residual old logical work, including both sorts of probes,
and use fresh final helpers. At odd N return the class singleton. At even
N the same phase-corrected trit instrument uses the same compressed bank,
Q/3 threshold, decoded-label rules and gradient. Model Sections 3 and 7
prove its exact hidden-label comparison and the independent good parity
law from the original product good marginal. Bad trits can be arbitrarily
correlated with good trits; their false count is at most r in the reference.
The ideal endpoint success is at least 23/32. Model Sections 6--8 bound
the total undo, good-label, rounding and gradient losses by <1/256.
Thus full success is >183/256>11/16>2/3 without a conditional clean-input
or conditional-binomial assumption.

The exact source count is Q=3*2^16*(n+32), acquired once before the
selector and before any gradient-failure return. The selected fraction
is exactly 1/3 under the fixed joint clean-marginal specification in
main Section 0 and model Section 1. The source is passive and unread
registers stay outside algorithm storage as specified in model Section 2.
All actual local compression and filter words are unchanged. No source
control, purification access, preparation inverse, success postselection
or extra delivery is introduced. Every branch remains counted.

## 10. Literal generation, controls, memory and charged work

### 10.1. Fixed layout and the inherited complete edge stream

Use the complete actual controller proved in the current controller appendix,
Section 3. It is a finite-program bit controller with a fixed number of
local tapes/heads, marked bounded strips and ready operand-address words.
Pad public fields and rows to power-of-two slots. Include all padding,
inputs, initialization, tape heads, strips and buffers in allocation.
Every actual read/write, head move, endpoint test, fixed-size logic step,
address change/copy and gate dispatch counts as a raw action. Apply a
conservative full a_addr=ceil(log2(M_alloc+2)) debit to EVERY raw action,
even when a local tape action would require less under the rules. Thus
every classical indexed access and fixed-arity indexed quantum gate has
its full required address charge. There is no free instruction, word
copy, random tape access or quantum-addressed memory operation.

A ready address field is used directly by the classically addressed gate;
the rule does not require an extra fresh instruction copy per gate. Any
address read, construction or copy the controller actually performs is
counted. Consecutive arithmetic gadgets move the ready addresses by their
fixed strides. A carry walk reads/flips all visited bits and moves back
to its marked low end; no separate binary cursor is cleared per gate.
Across m consecutive increments or decrements of a w-bit address the
total is O(m+w) raw actions. Marked strip endpoints and rewinds cost
O(m+1). Hence a fixed number of complete w-bit ripple/copy/Boolean passes
cost O(w+a_addr), including initial address setup, inverse and head returns.

In particular, an edge predicate has the proved full raw cost

    E_raw=O(Q*[n*(p_phase+a_addr)+s+a_addr]+n+a_addr)
         =O(n^2*ell),                               (D19)

where p_phase=Theta(ell), s=bitlength(Q)+32=Theta(ell). This includes
all actual known-prefix reads: for every row and operand bit, set its
slice address in O(a_addr), scan its p_phase bits, prepare a reusable
known addend, controlled-add, reverse the preparation, and restore the
heads. It does not read a complete prefix for each overlapping slice or
store all Q*n slice constants. It also includes the fixed q=14 cosine
table scans with O(a_addr) setup charged for every constant-width gate,
the signed accumulations and reverse scans, the copied sign, all fixed
member-pair orientations, validity, equality and cleanup. No unchanged
source-array access is dropped in the new bound.

The exact controlled G_v and G_v^(-1) use this edge word and an O(n)
diffusion with the literal sign in D3. Their raw gate/controller cost is
O(E_raw+n). Their arithmetic helpers clear for every logical input and
every active flag. A quantum control bit is used as data, never as a
memory index. One additional conjunction helper in Section 4 gives the
required alpha AND probe control without changing any gate-arity bound.

### 10.2. Each new loop and every inverse

Each module computes alpha by two O(ell)-bit comparisons, performs its
two H gates and controlled powers, generates/uses its known code, makes
the guarded code XOR, evaluates/reverses D_v to clear the logical probe,
and clears all flags. Retain alpha across both controlled powers. Retain
alpha AND probe only during the first controlled power, then erase it
before the next H; recompute it only for the code exchange. Controls
remain unchanged while their constituent Grover words execute.

Keep one reusable O(n)-bit classical iteration counter and one bound
buffer. For each Grover iteration, compare/increment the counter by full
O(n)-bit scans, counting all reads, writes, carries, endpoint tests and
returns. Construct t=2^h and 2t by zeroing/copying the finite O(n)-bit
buffer and setting the designated bit, also with counted address setup.
One module costs

    O((3t+1)*(E_raw+n)) raw actions.               (D20)

This charges the short t=1 modules, every exact predicate check and even
full O(n)-bit counter work for them. A block has sum_(h<b)t=B-1 and
b<=B for B>=2. Including all module ends, h counters, code generation,
power-buffer setup and block endpoints, it costs O(B*(E_raw+n)). There
is no unproved constant-delay increment and no B-cell classical strip.
The exponential loop uses the finite binary counter, not stored history.

All new public integers have bounded sizes: b_j=O(n), code values O(n^2),
their binary widths O(ell), and loop-counter/bound buffers O(n). Public
code schoolbook arithmetic O(ell^2) is O(n) and is performed once per
module, with a fixed-size slot retained during the comparisons/XORs.
Use an O(n)-cell marked strip, or counted full-width binary tests, for
the h, block and R_v loops. Initial marking, end tests and rewinds cost
O(n) per block/module if needed and are already covered by D20. A new
endpoint is not created by an uncharged search through an exponential
word. Inverse loops descend through the same finite public indices,
load the same codes and bounds, reverse every local word, and have the
same charges. Actual nonzero probes or stopping words do not alter the
classical stream or any loop count.

Recursion frames contain a level, direction and one of a fixed number
of program positions, each O(ell) bits. A stack head enters, reads and
leaves O(ell) cells per frame occurrence. The schedules in Section 7
give the exact forward and inverse emitter, with depth at most L+1.
Only a leaf block uses the large iteration/bound buffers, so these are
reused between calls. No child recursion occurs inside a module. There
is no stored expanded circuit, quadratic quantum history, or quantum
recursion frame. Reflection/address setup and frame dispatch cost fit
the same recurrence below. The first-verified logic, complete U and
U^dagger use the same counted Boolean/reverse templates.

### 10.3. Complete selected recurrence

Since a_n<sqrt(n+1)+1<=2sqrt(n+1),

    B_j<2 A_scale*3^j=O(sqrt(n)*3^j).

Two blocks and the initial preparations/checks therefore have raw work
O(B_j*(E_raw+n)). Let t_j be the full raw work of V_j, including the
classical emitter. The selected literal recursion satisfies

    t_0=O(sqrt(n)*(E_raw+n)),
    t_j<=3t_(j-1)+O(sqrt(n)*3^j*(E_raw+n)).

Induction, L+1=O(n) and 3^L<=sqrt(K) give

    t_L=O((L+1)*3^L*sqrt(n)*(E_raw+n))
       =O(sqrt(K)*n^(7/2)*ell).                    (D21)

The shared verifier and its inverse have raw cost

    O(R_v*B_L*(E_raw+n))
      =O(sqrt(K)*n^(7/2)*ell),                     (D22)

because R_v=O(n). Its verification code/repeat loops and copied predicate
are included by Section 10.2. All 1024 calls, all retained attempts,
answer copying and the literal inverse of U add a constant factor or
polynomial overhead. No branch-dependent early stopping is used to
obtain D21 or D22.

Generate ceil(sqrt(n+1)) by exact integer binary search and schoolbook
squares. Generate all 3^j, B_j, b_j and S_j uniformly by integer
arithmetic, with at most O(n^3) raw work and O(n^2) stored bits. The
source/controller's acquisition cost is O(n^3*ell) raw, including
translations, all R_F=O(ell) tests per level/offset, exact reconstruction,
prefix division, measurements, resets and source charges Q(n+1).
Gradient initialization and all 80 attempts, the fixed table's counted
rational construction, final classical products/divisions, endpoint
translations, trit counts, fresh coin and invalid-answer handling have
their unchanged polynomial caps. These fit D21: any fixed polynomial
is absorbed by 2^(n/2)*n^(7/2)*ell with an absolute outer constant, and
the bounded finite n prefix can enlarge that same constant. No validity
threshold, finite-input advice, or change to the source algorithm is
introduced by that asymptotic comparison.

### 10.4. Simultaneous allocated space and the full address charge

Classical labels, flags and prefixes use Q*(2n+p_phase+1)=O(n^2) bits.
All public powers/bounds use O(n^2); S_j and current code data fit within
that budget. The recursion uses O(n*ell) bits. A fixed number of O(n)
counter/bound buffers and local strips, ready addresses/head locations,
arithmetic scratch, acquisition counts and gradient constants fit O(n^2).
There is no seed bank and no stored O(n^2)-gate or exponential program.
Every initialized/padded cell and the fixed table is included. Thus
S_C=O(n^2) without transferring any stored-program space assumption.

Unread raw registers are passive inaccessible-source state, excluded
under the rules. All acquired rows and current input work are counted.
Quantum storage is the Q rows and Q axes, each linear in n, with
the reusable acquisition/edge arithmetic of O(n) qubits. Every retained
attempt has O(n) candidate/opponent work, O(ell) code and just one added
logical probe; 1024 is an absolute constant. The one shared verifier
has O(n) logical work, including its code/probe and any actual leakage.
The O(n) zero-test helpers now include the attempt probe in the test.
The gradient uses O(ell), and the answer-copy/residual old work and fresh
endpoint helpers add O(n). All these banks can coexist with the classical
allocation, so the simultaneous peak remains S_Q=O(n), S_C=O(n^2).

An explicit allocation by a fixed number of padded banks is at most
C(n+2)^2 classical bits plus C(n+2) qubits for an absolute C, including
the fixed-size table and head records. Choose the corresponding padded
address width before initializing the layout; there is no circular
definition based on the eventual circuit length. Then a_addr=O(ell).
Multiplying the entire raw count D21--D22 by that full factor pays all
indexed gates/accesses and all local operations conservatively. This
proves the time bound in main Section 0. It does not use a constant-delay gate generator or a free
address copy.

All limits depend only on N and the public parameter rule. Malformed
records, missing sources on bad record blocks, actual verification
leakage, incorrect answers and gradient-preparation failures cannot
enlarge a counter, code, loop, recursion depth or allocated bank. All
specified modules and gates are executed on stopped quantum branches.
No measured intermediate success affects the filter stream. Thus the
resource and source-count bounds hold on every execution branch for
every N>=2, jointly with the exact clean-joint-marginal specification of main Section 0.

