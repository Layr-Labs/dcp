# GRST1: coherent retained-block search with linear source count

## Scope and attribution

For every integer N>=2 and s in Z/NZ let n=ceil(log2 N), D=2^n,
and k=n+20. The algorithm below uses exactly k source copies and recovers
the entire secret with unconditional probability greater than 2/3.
All four declared worst-case bounds hold jointly on every execution branch:

 T=O(2^(n/2) n^2 (log2 n)^2), S_C=O(n), S_Q=O(n^2), Q=n+20=O(n),

where the logarithmic time envelope applies for n>=2; n=1 has absolute cost.
The sole numerical time-growth index remains 1: replacing 2^n by 2^(n/2)
is a full-envelope improvement, not an index change or subexponential time.
The unscored tolerance law remains 0 under independent ideal source copies.

GRST1 materially builds on our RST1 submission
6487a417-1e14-4295-bf4f-c8219ade0f2e: its retained block, exact shift
projectors, source overlap and reversible arithmetic are reused below.
The sequential test loop is replaced by coherent reflection queries and
Grover diffusion; the previous proof's sequential bound is used only at n=1.
The controller now generates regular arithmetic circuits directly rather than
storing a local circuit description, giving linear classical storage.
RST1's source is the repository baseline at ccca08c, and its established
sequential-projection context is Ettinger, Hoyer and Knill,
Hidden Subgroup States are Almost Orthogonal, quant-ph/9901034v1,
Theorem 1, Section 2 and Lemmas 2-4. Grover search is standard: Grover,
A fast quantum mechanical algorithm for database search,
quant-ph/9605043v3, algorithm and amplitude analysis. The complete two-dimensional
rotation, error accumulation and charged implementation arguments are supplied
here; no external theorem, accepted verdict or diagnostic is a proof premise.
No new fastest-known DCP algorithm or novelty over the literature is asserted.

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
Acquire exactly k independent copies once, sigma=rho_s tensor-power k,
and put P_t=A_t tensor-power k. Then P_s sigma=sigma and
tr(P_t sigma)=2^(-k) for t<N,t!=s.
For invalid candidate t>=N define P_t=0; such candidates are unmarked.

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
   =4 sum_(t<N,t!=s) |a_t|^2 ||P_t v||^2 <=4*2^(-k).

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

For n=1 (necessarily N=2), use the SAME k=n+20 acquired copies and perform
sequential binary tests P_0 and then P_1, returning the first acceptance,
with zero fallback. The binary test coherently computes the aggregate
all-zero predicate after U_t and H on every control, measures ONLY its flag,
uncomputes the predicate and reverses H and U_t. The Kraus operators on the
block are exactly P_t and I-P_t; individual controls are not measured.
This fixed finite branch is analyzed separately below. Every branch acquires
exactly n+20 copies and has a predetermined finite iteration ceiling.

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

 ||W^j(|u>v)-W_*^j(|u>v)|| <=2j*2^(-k/2)
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
weight is a=2^(-k). Write w=(I-P_0)v. Then
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

Apply those U_t circuits and H to all k source controls. Compute a predicate
bit for [t<N] AND [all k transformed controls equal zero], apply Z to that
predicate bit, and uncompute it. Finally reverse H and U_t on the block.
This is exactly B with all scratch cleared. A reversible linear prefix-AND
chain costs O(k+n) gates and scratch, reusing its work between queries.
The [t<N] bit may be computed once per query, reused and uncomputed.
Every oracle invocation therefore has O(kn+k+n)=O(n^2) logical gates,
with O(n) arithmetic/predicate scratch beyond the retained O(n^2) block.

Diffusion on C is H^n (2|0^n><0^n|-I) H^n.
A multi-controlled phase flip implements I-2|0^n><0^n| with O(n)
Toffoli/Clifford gates and O(n) clean scratch. Its negative differs by a
GLOBAL phase only, so it is also a valid implementation of F for the
measured probabilities and hybrid argument. Equivalently choose the same
global sign for physical and ideal diffusion throughout. Diffusion has
no source access and has O(n) logical work.

## Uniform streaming controller and charged addressing

There is no stored arithmetic-circuit list. Each comparison, carry/borrow
scan, selection, history-XOR operation and prefix-AND chain above consists
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
allocation estimates. Every branch acquires exactly k=n+20 source copies,
including copies whose information is ultimately unused or discarded.

## Joint indices, error model and scientific comparison

For B_T=2^(n/2)n^2(log2 n)^2, log2 B_T=n/2+O(log n), giving exact index 1.
B_C=n, B_Qspace=n^2 and B_samples=n all have exact index 0. These are the
four supported structured envelopes for the same algorithm and k=n+20.
The n=1 exception for the logarithmic expression is explicitly bounded.
The fifth law is tau(n,Q)=0 with actual Q=n+20; every copy is independent
and ideal. No malformed-copy behavior is promised and no impossibility of
positive tolerance is asserted. This is the same canonical model as RST1.

Relative to RST1's declared work 2^n n^2(log2 n)^2, this work envelope is
smaller by factor 2^(-n/2); classical space improves from n log2 n to n,
while quantum space and sample envelopes remain n^2 and n. These compare
proved upper guarantees at the challenge's common success threshold,
not lower bounds or practical runtime measurements. They do not imply a
square-root n exponent, a better numerical index, dominance over
subexponential sieve time, or the goal 2^{O(n^(1/3))}. The useful alternative
is an explicit quadratic exponential-time speedup while retaining polynomial
space and linear source complexity in the stipulated source-only model.
