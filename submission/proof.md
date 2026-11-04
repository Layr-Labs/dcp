# RGRST1: coherent retained-block search with linear source count

## Scope and attribution

For every integer N>=2 and s in Z/NZ let n=ceil(log2 N), D=2^n,
and k=1024(n+20), r=floor(5k/16). The algorithm below uses exactly k source copies and recovers
the entire secret with unconditional probability greater than 2/3.
All four declared worst-case bounds hold jointly on every execution branch:

 T=O(2^(n/2) n^2 (log2 n)^2), S_C=O(n), S_Q=O(n^2), Q=1024(n+20)=O(n),

where the logarithmic time envelope applies for n>=2; n=1 has absolute cost.
The sole numerical time-growth index remains 1: replacing 2^n by 2^(n/2)
is a full-envelope improvement, not an index change or subexponential time.
The unscored tolerance law is floor(5Q/16) under the explicit fixed-position
corruption model below; clean independent ideal copies are included.

RGRST1 directly reuses GRST1 submission
7068970f-faaa-4e47-99c0-7dad0b3284db for the coherent retained-block
query, Grover schedule, original-state hybrid and streamed arithmetic.
It replaces the all-zero acceptance predicate with a Hamming-weight threshold
and increases the fixed linear sample count. The explicit corruption-model
text is reused from RLQGR1 submission
641e8707-91e2-4257-a82d-d1f7bde2349e; its classical-score analysis is not used here.
Earlier retained-block RST1 is 6487a417-1e14-4295-bf4f-c8219ade0f2e.
The baseline source, standard Grover and sequential-test provenance are
retained in those sources; the needed arguments are reproduced in full here.
Standard search context: Grover, A fast quantum mechanical algorithm for
database search, quant-ph/9605043v3, algorithm and amplitude analysis.
No external theorem, accepted verdict or numerical test is a premise.
This is a resource/robustness result for the challenge, not a new fastest-known
DCP algorithm, a subexponential time result or the cube-root research goal.

## Fixed-position malformed-copy model

For Q=k acquired source copies, before the algorithm's private randomness
an adversary may choose at most tau(n,Q)=floor(5Q/16) acquisition positions
and an arbitrary joint density operator on the corresponding declared n+1
qubit source registers. It may know N,s and the algorithm. All other copies
are independent ideal rho_s for that fixed s, and their product state is
tensor-independent of the malformed subsystem. Malformed copies may be
mutually entangled or classically correlated. The adversary cannot alter
registers or the controller after delivery, or choose positions based on
private measurement outcomes. The algorithm does not know those positions.
This is exactly the corruption context stated in the structured fifth claim,
with a stronger count law than the preceding classical-record guarantee.
Clean independent ideal input is the case of an empty malformed set.
The count is based on actual acquired Q=k, not its O(n) upper envelope.

## Exact single-copy and block projectors

For candidate t<N define U_t on a source copy to subtract t modulo N from
the n-bit data register when its control is 1, acting identically for invalid
strings y>=N. This is a permutation on the complete encoded domain.
Let A_t=U_t^dagger (|+><+| tensor I) U_t.
For source rho_s, A_s rho_s=rho_s and tr(A_t rho_s)=1/2 for t!=s.
Indeed a source component becomes
(|0,x>+|1,(x+s-t) mod N>)/sqrt(2); at t=s the control is |+>,
and at t!=s its two data labels are distinct, so the control is I/2.
Averaging over x gives the mixed-state assertion.
Acquire exactly k copies once, with the allowed joint density sigma.
Let V_t apply U_t and then H to each source control. Let W be the sum of the
k transformed control bits in the computational basis. Define P_t as the
orthogonal projector V_t^dagger [W<=r] V_t on the entire encoded block.
For invalid t>=N define P_t=0. These are exact projectors, not noisy POVMs.
Let q<=r be the actual malformed count and h=k-q the honest count.
At t=s every honest transformed control is exactly |0>. At most q controls
can then be 1 on any basis component, even with entangled malformed registers.
Thus P_s sigma=sigma, with NO probabilistic exception.

At false t<N, tracing out each honest data register gives a transformed
control I/2. The honest controls are independent uniform bits, independent
of all malformed registers, because of the product promise. Measuring all
controls analytically, acceptance of W<=r implies that the honest count
Y is <=r, regardless of malformed outcomes. Hence

 tr(P_t sigma)<=Pr(Bin(h,1/2)<=r).

Since r<=5k/16 and h>=11k/16, h/2-r>=k/32. The following elementary
concentration bound applies: if independent X_i in[0,1] have centered log
MGF f_i, then f_i'' is a variance under a tilt and is <=1/4. This follows
from E[(X_i-1/2)^2]<=1/4, so variance<=1/4 under every tilted law.
Integrating f_i(0)=f_i'(0)=0 yields E exp(lambda sum(X_i-E X_i))
<=exp(h lambda^2/8). Chernoff optimization gives lower-tail probability
at displacement d at most exp(-2d^2/h). Consequently

 tr(P_t sigma)<=exp(-k/512)=exp(-2(n+20))<=2^(-(n+20))=:eta.

The last inequality uses e^2>2. The estimate is uniform over all allowed
malformed joint states, every secret and every false candidate. No assumption
about the distribution or independence of malformed outcomes is made.

Let C be a new n-qubit candidate register. The physical reflection query is

 B=sum_(t=0)^(D-1) |t><t| tensor (I-2P_t).

It is an exact unitary, not a source oracle. It is built from counted gates
as described below. A mathematical purification v of sigma is used only in
the proof; B acts trivially on the inaccessible purifying environment.
The ideal comparison query is

 B_*= (I-2|s><s|) tensor I.

B_* is not implemented or assumed available. It is an analysis reference.
For any unit vector a in C, orthogonality of the candidate basis gives

 ||(B-B_*)(a tensor v)||^2
   =4 sum_(t<N,t!=s) |a_t|^2 ||P_t v||^2 <=4*eta.

The t=s term vanishes because P_s v=v; invalid t terms also vanish.
This bound needs only the ORIGINAL state v. It makes no assertion that
the physical retained block remains undisturbed at intermediate times.

## Algorithm including exact iteration count

Prepare C in |u>=H tensor-power n |0^n>, a uniform state on D labels.
The accessible block is the k acquired mixed copies, without purification access.
For n>=2 compute j=floor(3 sqrt(D)/4) by exact integer arithmetic:
j=isqrt(9D) div 4, where isqrt returns the integer floor square root.
Repeat j times the query B followed by diffusion
F=2|u><u|-I on C alone. Measure C in the computational basis.
If its value is <N output it, otherwise output zero. There is no verification
postselection or additional acquisition. All outcomes are included in the
success guarantee. Uncompute/dispose allocated scratch as necessary.

For n=1 (necessarily N=2), use the SAME k=1024(n+20) acquired copies and perform
sequential binary tests P_0 and then P_1, returning the first acceptance,
with zero fallback. The binary test coherently computes the aggregate
Hamming-weight-at-most-r predicate after U_t and H on every control, measures ONLY its flag,
uncomputes the predicate and reverses H and U_t. The Kraus operators on the
block are exactly P_t and I-P_t; individual controls are not measured.
This fixed finite branch is analyzed separately below. Every branch acquires
exactly k=1024(n+20) copies and has a predetermined finite iteration ceiling.

## Ideal rotation without approximate gates or real-number computation

Let theta=arcsin(1/sqrt(D)), only an analytic parameter. Define
|b>=(sum_(t!=s)|t>)/sqrt(D-1). Then
|u>=sin(theta)|s>+cos(theta)|b>.
In this ordered two-dimensional basis B_* is diag(-1,1), while
F=2|u><u|-I. Multiplying these 2-by-2 matrices shows that after j iterations
of FB_* the marked probability is sin^2((2j+1)theta).
No circuit computes theta, pi, a trigonometric function or an approximate rotation.

For D>=4, x=1/sqrt(D)<=1/2. The elementary facts theta>=x and
arcsin(x)/x<=arcsin(1/2)/(1/2)=pi/3 give

 (2j+1)theta >= (3sqrt(D)/2-1)/sqrt(D) >=1,
 (2j+1)theta <= (3sqrt(D)/2+1)*(pi/3)/sqrt(D) <=2pi/3.

For completeness, arcsin(x)/x is the average of the increasing function
1/sqrt(1-y^2) on [0,x], hence is increasing. All angle inequalities hold
for the floor choice because 3sqrt(D)/4-1<=j<=3sqrt(D)/4.
On the interval [1,2pi/3] the minimum of sin^2 is at an endpoint.
At the right endpoint it is 3/4; at the left, the alternating sine series
gives sin(1)>=1-1/6=5/6, hence sin^2(1)>=25/36.
(The standard inequalities 3<pi<4 suffice to place these endpoints.)
Thus ideal success is at least 25/36 for every n>=2.

## Hybrid bound for the reused unknown block

Let W=FB and W_*=FB_* with F extended by identity on the block/environment.
Telescoping j products gives

 W^j-W_*^j=sum_(r=0)^(j-1) W^(j-1-r)(W-W_*)W_*^r.

On the ideal initial state |u> tensor v, every W_*^r leaves v unchanged.
Unitarity and the original-state query bound therefore imply

 ||W^j(|u>v)-W_*^j(|u>v)|| <=2j*sqrt(eta)
 <=(3/2)*sqrt(D)*2^(-(n+20)/2)=3/2048.

This controls the ENTIRE physical computation, including all entanglement
and disturbance of the same source copies. It does not assume independent
queries, a refreshed block or that B equals B_* in operator norm.
For any effect E with 0<=E<=I, probabilities of two unit vectors at distance
epsilon differ by at most 2epsilon: expand
<z,Ez>-<w,Ew>=<z-w,Ez>+<w,E(z-w)> and use Cauchy-Schwarz.
Apply this to the event C=s, with environment and block ignored. Actual
success is at least

 25/36 - 3/1024 > 2/3,

because 25/36-2/3=1/36>3/1024. This is unconditional for every N,s.
Invalid-candidate fallback cannot reduce the probability of the C=s event.
The purification is merely a proof device, never an implemented resource.

At n=1, s=0 passes with certainty. For s=1 the original false-projector
weight is a=tr(P_0 sigma)<=eta<=2^(-21). Write w=(I-P_0)v. Then
|<v,v-w>|=||P_0v||^2=a, and P_1 v=v gives
||P_1 w||>=|<v,P_1 w>|=1-a. Thus success is at least
(1-2^(-21))^2>2/3. This also proves the claimed common success threshold
on the finite branch without importing any theorem.

## Building B from exact Clifford+T gates

No test is a black-box query. Keep t as quantum data in C throughout.
A reversible ripple circuit computes the valid-candidate bit [t<N].
For t<N implement controlled subtraction U_t on each source register,
using t as an unchanged input rather than a classical constant. For invalid
t use identity. On a source data input y compute [y<N] and [y<t], and
select y-t when y<N,y>=t, y+N-t when y<N,y<t, and y otherwise.
For inverse addition, select y+t if that sum<N, subtract N otherwise on
valid y, and preserve invalid y. O(n)-bit ripple carry/borrow recurrences,
comparisons and multiplexing use O(n) fixed-arity Boolean gates and wires.
They retain the inputs N (a classical constant) and t (a quantum register).
The extension remains a permutation for every candidate label.

Retain intermediate Boolean values, XOR the output into a target and reverse
the evaluation; this is a clean compute-XOR circuit with linear gate and
scratch counts. Compute f_t into zero, swap, and XOR the inverse g_t of the
new input into the old input to clear it. Conditional selection for the source
control and invalid t is included in the same constant-size Boolean pattern.
This implements U_t, including in superposition over t, in O(n) gates and
ancillas. Reverse the gates for U_t^dagger. Fixed-arity Boolean operations
use NOT/CNOT/Toffoli and exact constant-size Clifford+T decompositions.
No arbitrary-angle synthesis, precision parameter or unit-cost integer
arithmetic is used. All work ancillas are zero after each U_t.

Apply those U_t circuits and H to all k source controls. Into a clean
ceil(log2(k+1))-bit quantum weight register add each transformed source
control bit. A controlled increment is an in-place permutation implemented
by the same clean Boolean compute-swap-inverse construction on O(log(k+2))
bits, with O(log(k+2)) gates/scratch. Reverse these increments later to clear
the weight. Compare weight<=r and t<N into a clean predicate bit, apply Z,
reverse the comparisons, clear the weight and reverse all H and U_t.
This is exactly B with zero scratch, including on arbitrary malformed input.
The [t<N] bit may be computed once per query, reused and uncomputed.
Predicate work is O(k log(k+2)+n)=O(n^2); total query work is
O(kn+k log(k+2)+n)=O(n^2) logical gates. Arithmetic scratch is O(n),
and weight/predicate scratch O(log(n+2)), beyond the retained O(n^2) block.
For the finite measured binary test use the same predicate circuit, measure
ONLY its flag, then uncompute it and reverse H and U_t; the exact Kraus
operators on the retained block are P_t and I-P_t.

Diffusion on C is H^n (2|0^n><0^n|-I) H^n.
A multi-controlled phase flip implements I-2|0^n><0^n| with O(n)
Toffoli/Clifford gates and O(n) clean scratch. Its negative differs by a
GLOBAL phase only, so it is also a valid implementation of F for the
measured probabilities and hybrid argument. Equivalently choose the same
global sign for physical and ideal diffusion throughout. Diffusion has
no source access and has O(n) logical work.

## Uniform streaming controller and charged addressing

There is no stored arithmetic-circuit list. Each comparison, carry/borrow
scan, selection, history-XOR operation and weight-counter circuit above consists
of a fixed finite sequence of bit scans. Its gate type is chosen from a
constant-size template using the stage number and bit index. Allocate
linear-length history bands; wire addresses are base+index or base+index+1,
and fixed finite combinations thereof. Reversing a computation reverses
that finite stage order and scans the bit indices downward. Compute-swap-
inverse has constant nesting depth. The copies are a further single loop,
with the copy base advanced by n using binary addition at each copy.
When traversing backward, decrement that base by n. No local index
multiplication is performed in the streamed quantum circuit generator.
No recursion stack of length n or stored gate description is required.
Classical N bits select constant gates by reading the specified bit as
needed. The superposed t bits are circuit controls, never controller advice.

Classical allocation comprises N, n, D's compact power-of-two description,
j and the j-iteration counter, fixed-many copy/bit/stage indices and bases.
The long integers have O(n) bits, and local indices O(log(n+2)) bits.
A read-only schedule is a constant-size program, not instance advice.
Thus peak S_C=O(n). Input handling and j computation cost polynomial work:
integer square root of 9D can be computed by binary search on an O(n)-bit
interval with O(n) iterations of schoolbook O(n^2) arithmetic; full addressed
work is O(n^4), classical scratch O(n). Store a constant number of trial
endpoints and products and reuse them. Its polynomial preprocessing is
counted and is absorbed by the final exponential-time envelope.

Total allocated classical bits plus qubits M=O(n^2), established BEFORE
charging addresses. The model's address charge is consequently O(log(n+2)).
Charge O(log^2(n+2)) bit operations per logical gate for local address
calculation, streamed template generation, counters, indexed accesses to
those counters and the separate gate/address charge. Each fixed finite combination of O(log(n+2))-bit index additions
uses O(log(n+2)) Boolean steps, each charged its full O(log(n+2))
address overhead, and therefore fits this allowance. No per-gate
index multiplication is needed.
The j-counter may have O(n) bits, but ordinary binary increment uses O(1)
amortized changed bits across the fixed loop; it is accessed with
O(log(n+2))-bit addresses. Even conservatively charging O(n log(n+2))
per query to update/compare that counter is dominated by the query budget.
N is accessed by bit index, and no iteration performs a unit-cost read of
an n-bit constant. Initialization, acquisition, measurement, resetting,
all inverse computations and final disposal are included.

There are j<=3*2^(n/2)/4 iterations, so complete charged work is
O(2^(n/2) n^2 log^2(n+2)+n^4). The polynomial term is absorbed uniformly:
n^4/(2^(n/2)n^2(log2 n)^2) is bounded for n>=2, and tends to zero.
Since log(n+2)=Theta(log n) there, the declared envelope follows.
All constants are absolute; the finite branch n=1 has absolute resources.
There are no retries, expected-time limits, postselection or success-only
allocation estimates. Every branch acquires exactly k=1024(n+20) source copies,
including copies whose information is ultimately unused or discarded.

## Joint indices, error model and scientific comparison

For B_T=2^(n/2)n^2(log2 n)^2, log2 B_T=n/2+O(log n), giving exact index 1.
B_C=n, B_Qspace=n^2 and B_samples=n all have exact index 0. These are the
four supported structured envelopes for the same algorithm and k=1024(n+20).
The n=1 exception for the logarithmic expression is explicitly bounded.
The fifth law is tau(n,Q)=floor(5Q/16) with actual Q=k=1024(n+20).
The model is the fixed-position product-independent-ideal corruption promise
specified above. Under every allowed malformed joint state, the same
unconditional success and all four branchwise bounds hold jointly.
This includes clean input, and does not claim that larger tolerance is
impossible or translate a probability of corruption into a count.

Relative to clean-only GRST1, all four asymptotic resource envelopes are
unchanged while the new theorem tolerates floor(5Q/16) malformed copies
under its explicit additional model. The error-model text differs from
GRST1's canonical clean-only text, so the structured comparator does not
infer an order across those contexts. Relative to RLQGR1 under IDENTICAL
error-model text, RGRST1 has stronger tolerance and smaller time/classical
space guarantees, but uses n^2 rather than n qubits. These remain incomparable
resource tradeoffs because of quantum space. Both use O(n) acquired copies,
with different exact coefficients. No comparison of upper envelopes implies
lower bounds, a new time-growth index, a physical runtime measurement,
a new fastest-known DCP algorithm or the cube-root research goal.
