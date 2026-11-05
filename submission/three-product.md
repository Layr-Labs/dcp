# RS14: explicit three-product arithmetic and coherent modular translation

This file specifies the ACTUAL new arithmetic and source implementation.
It replaces the quadratic ordinary multiplication in all sieve count/coin
kernels and source rounding, and replaces the individual controlled source
powers by one coherent modular-translation circuit. It also groups the
retained commuting Fourier phases into one quantum-word gradient addition
per output bit. All source errors, conditional ensembles, sieve/quota and
physical budgets retain their proofs after these exact circuit identities.
No faster-arithmetic, reciprocal or Fourier oracle is assumed.

## 1. Uniform bit algorithm for unsigned multiplication

For nonnegativev-bit inputs, pad both to dyadic widthw=2^ceil(log2 v).
The following fixed recursion computes the exact2w-bit product. Width1
is one AND. At widthw=2m splitx=x0+2^m x1,y=y0+2^m y1. Compute

 z0=x0*y0, z2=x1*y1,
 zd=(x1-x0)*(y0-y1),
 xy=z0+2^m(z0+z2+zd)+2^(2m)z2.                       (1.1)

Each of the THREE recursive magnitude products has widthm: both absolute
differences are<2^m. Compute their signs by ripple comparisons and Boolean
MUX/subtraction, multiply their unsigned magnitudes recursively, and restore
the sign ofzd. The identity follows becausez0+z2+zd=x0y1+x1y0.
A signed temporary of at most2w+3 bits suffices; final nonnegative output
has2w bits. Each split, signed addition, comparison, MUX and combination
usesO(w) bounded-fan-in Boolean operations and wires by the ripple identities
in proof.md Section2. Branchless Boolean selects handle signs on quantum
inputs; recursion depth and allocation depend ONLY on declared widths.
There are no data-dependent quantum branches or secret classical controls.

For dyadicw the recurrence isC(w)<=3C(w/2)+c0w. Its level sum gives
C(w)=O(3^log2 w). Sincew<2v, this isO(v^log2 3). The exact integer
inequality3^5<2^8 proveslog2 3<8/5, henceC(w)=O(v^(8/5)) uniformly.
This rational upper polynomial is explicitly conservative; the sharper
three-product recurrence is retained, and no fitted complexity is asserted.
Signed general inputs add one sign bit, magnitude conversion andO(v) work.
All fixed-degree kernel words areO(n) bits, so this bound applies with
absolute constants to all actual products.

Implement each bounded-fan-in Boolean gate by writing its result to a new
clean wire using NOT,CNOT,Toffoli; input wires remain intact. Store all gate
results and use the fixed circuit in reverse after copying its final output
to clean output wires. This is exact compute/copy/uncompute, withO(C(w))
Clifford+T gates andO(C(w)) temporary qubits. It does NOT claim linear
scratch for the recursive circuit. Constants, input copies, intermediate
products, every clean/dirty history wire, reversal, output copy and reset
are included. A regular depth-first generator emits this finite recursion
with a counted classical stack and fixed wire offsets. It never accesses
quantum-addressed memory; all gate locations are generated classically with
the full address costs below. The three recursive magnitude computations retain their gate histories
and are NOT cleaned locally inside the multiplication recursion. There is
one global reversal after copying the final product. Thus cleanup doubles
the three-product gate count; it does not change the recurrence into six
recursive calls per level. The complete gate list need not be retained.

## 2. Every remaining division and coin operation

The actual sieve/count formulas divide by FIXED factorials or fixed rational
coefficient denominators, with degrees at most63. Their bit lengths are
absolute constants independent ofN. Implement division by fixed positived
by scanning the dividend bits, updating a remainder<d, comparing/subtracting
d, and emitting one quotient bit per step. Each remainder operation has
constant width, soO(v) logical bit operations suffice for av-bit dividend.
Exact claimed quotients are justified by the count identities; the routine
also returns a remainder and behaves on every encoded input. A power-of-two
division is a shift/truncation with the correct rounding bit comparisons.
All actual kernel products use Section1, fixed-term additions use ripple
addition, and all intermediate signs/widths are bounded explicitly by their
constant degrees. There is no division of two arbitrary unknownv-bit words
inside any per-pair kernel.

Physical rational coins generate a declared number of fair bits, reject
out-of-range draws and compare to an integer numerator. They require only
linear-width comparisons and fixed-cap counters, not general division.
The existing literal4R physical-trial cap and coupling proof remain valid.
The final source round computesNZ by Section1 and divides by2^t by binary
shift/nearest-integer comparison. Outer rational-grid decoding uses fixed
constants and binary denominators; parameter computations with arbitrary
rational powers and integer division are ONCE-only polynomial work, fully
charged and absorbed by the stated exponential allocation. The new reciprocal
constant in Section3 is also generated once by the explicit ordinary
restoring bit division, rather than supplied as advice.

## 3. Exact modular reduction by generated integer products

Let source phase widtht be the fixed value in source-labels.md, letv=t+1,
W=v+n+2 and generate

 mu=floor(2^W/N)                                      (3.1)

ONCE by restoring binary division: scan theW+1 bits of2^W, at each step
shift the remainder, compare/subtractN and emit a quotient bit. This takes
O(nW)=O(n^2) logical bit operations andO(n) scratch, with full addressed
costO(n^3), before source calls. Its output hasO(n) bits. No uncounted
precision, advice or arithmetic primitive enters this generation.

For any0<=u<2^v compute

 q=floor(u*mu/2^W), r=u-qN,
 red_N(u)=r ifr<N, otherwise r-N.                      (3.2)

Both products are the Section1 circuit and the division by2^W is a shift.
Since0<=1/N-mu/2^W<2^-W, the estimateu*mu/2^W is at mostu/N and
less than1 below it. Thereforeq is eitherfloor(u/N) or one less;
r is in[0,2N), and one comparison/subtraction gives exactlyu moduloN.
Every intermediate hasO(n) bits: v,W,t andbit_length(mu) areO(n), and
all products have widths at most a fixed multiple ofn. Thus the whole
Boolean function usesO(n^(8/5)) gates/operations, with the history allocation
and clean reversal of Section1, not an arbitrary-modulus arithmetic oracle.

For source phase integerk in[0,2^t), define the permutation on all encoded
n-bit DATA inputs

 F_k(x)=(x+k) modN ifx<N, otherwise x.                  (3.3)

Whenx<N useu=x+k<2^(t+1) in(3.2); choose between its result andx with
a BooleanMUX controlled by[x<N]. Its explicit inverse, onvalidy<N, first
computeskappa=red_N(k), then emitsy-kappa ify>=kappa, otherwise y+N-kappa.
Forinvalidy>=N it returns y. These circuits have the sameO(n^(8/5)) logical
cost, including all comparisons and every gate-history cleanup.

To realize a clean permutation|k>|x> ->|k>|F_k(x)>, compute/copy/uncompute
F_k into an empty secondn-bit register, swap the two data registers, then
XOR the computed inverseF_k^-1(newx) into the oldx register and uncompute
that inverse computation. The old register becomeszero for every basis
input, valid or invalid. The phasek register is unchanged. Both computations
use fixed Boolean circuits and their clean reverses, so the proof holds by
linearity on every superposition and entangled input. No measurement or
postselection is used. All scratch histories are physically counted. This
is one coherent translationU^k of the source data, not2^t source calls or
repeated shifts. Onchi_y it multiplies the phase register byexp(2pi i ky/N)
exactly, preservingchi_y andq_y. Consequently the exact pre-transform QPE
state and every source tail/error comparison in source-labels.md apply.

## 4. Grouped retained phases, with one ripple addition per output

Use the same truncated ordinary Fourier network as source-labels.md.
For a forward output bitj, just after itsH all retained diagonal phases
with lower input bitsk andr=j-k+1<=B commute. Their product is

 exp(2pi i x_j d/2^B),
 d=sum_(k=max(0,j-B+1))^(j-1) x_k 2^(B-j+k-1).           (4.1)

This is a contiguous lower-bit quantum word with fixed shifts and zeros,
not a table lookup. Compute each bit's AND with controlx_j into a clean
B-bit addend usingO(B) Toffolis, perform oneB-bit ripple addition into the
shared gradient, and uncompute the AND word. The lower bits and control
are unchanged in the computational basis; the construction is exact on
superpositions by linearity. The two-quantum-addend ripple sum is computed
into a clean register, swapped and cleaned by inverse subtraction exactly
as in proof.md Section2 and the reproduced gradient addition identity.
It usesO(B) gates and scratch, rather thanB separateB-bit additions.
Subtract instead of add in the inverse network, reversing the order of
all grouped instructions andHadamards/swaps. Formula(4.1) proves the grouped
network is EXACTLY the same truncated unitary, including on entangled
inputs. All gradient-preparation and truncation errors therefore remain
unchanged, with no additional approximation or independent-noise assumption.
There aret grouped additions, givingO(tB)=O(n^(3/2)) logical gates.

## 5. Full charged resources, including quantum history

The exact source translation and measured-residue product costO(n^(8/5))
logical work; the grouped transformO(n^(3/2)) is smaller. Bounded gradient
preparation,mu and parameter generation are counted separately as fixed
polynomial work. Full gate/instruction addresses haveA_addr=O(sqrt n),
including all polynomial-size arithmetic histories, controller stacks,
regular wire offsets, current pointers, old/new record buffers and labels.
Their fullO(A_addr^2)=O(n) generation/access charge givesO(n^(13/5))
work per source label. There are at mostR=O(nL) such extractions, including
failed/discarded acquisitions and erroneous-label transcripts. Source work
isO(n^(18/5)L). The preparation-abort branch acquires no source copies and
still fits the counted polynomial initialization bound.

All kernel products areO(n^(8/5)) logical work, fixed divisions/comparisons
linear, and term counts/degrees fixed. AcrossO(n) targets andsumLi<2L,
full addresses giveO(n^(18/5)L) sieve work as well. Physical coin trials
and record sorting still fitO(n^3L), which is smaller; their fixed caps
are unchanged. Final verification, phase reconstruction and exact parameters
cost polynomial work orO(n^3L), also smaller. Every failure branch and
cleanup is included. The SAME execution therefore has

 T=O(n^(18/5)L), SC=O(nL+n^(8/5)), SQ=O(L+n^(8/5)), Q=O(nL).

BecauseL grows exponentially insqrt n, each fixed polynomial isO(L).
ThusSC=O(nL),SQ=O(L) with absolute constants absorbing the finite prefix,
without hiding any history wire or charging its space as time. The declared
exact acquisition inequalities remain unchanged. With the fullallocation
L=O(sqrt n2^(c sqrt n)), the final time envelope is

 T=O(n^(41/10)2^(c sqrt n)), c=112887342087/50000000000.

RS13's same actual arithmetic has the same polynomial factors; the new
sixth pass only changes the proved exponential coefficient through its
critical yield/quota schedule. All four full representatives strictly improve,
as quantified in proof.md Section12. The exact growth index remains1/2.
No lower bound on old work, practical finite-size speedup, fastest-known,
optimality or cube-root claim is asserted.
