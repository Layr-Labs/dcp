# Private counting and a complete classical bucket dictionary

All quantum search/counting here acts on KNOWN newly reset private registers.
It never controls, prepares, purifies or inverts a DCP source. The only later
source-index operations are exact finite Boolean dictionary lookups.
Set U=2^t, L=2^R, lambda=2^30 n L and K=2^40 n L. The main proof gives
n>=2^32, t>=512R, t-2R>=80log2n and log2B<n/8. Every circuit/loop below
is expanded and charged, including private failures, measurements and reset.

## Literal private Grover and ordinary phase estimation

For a classically specified low-key/hash predicate P(z), compute it with
literal child-table equality/XOR scans, ripple sums/comparisons and the binary
hash matrix, phase its flag by Z, and reverse the scratch. Its base cost is
at most2^1000 n^2 L core steps, including generated gates/operand addresses.
There is no QRAM. The private t-bit register starts in H^t|0>.
Diffusion is EXACTLY D=2|unif><unif|-I=-H^t Z0_neg H^t. A computed zero flag
implements Z0_neg. To control D, control its zero reflection and add Z on the
control to implement the leading minus. Controlled marking is compute P,
controlled Z on its flag, uncompute. We control these known logical circuits,
not a free controlled version of an unknown subroutine. Toffoli/CNOT/NOT
have exact fixed Clifford+T decompositions.

In the uniform marked/unmarked basis the product of marking and D has
eigenvalues exp(+/-2i theta), sin^2(theta)=M/U, where M is the marked count.
The starting uniform state lies in that two-dimensional span. For M=0
its phase is0; for M=U its phase is1/2. This follows directly by multiplying
the reflection matrices and includes the controlled diffusion sign above.

Let J=ceil(sqrt(U)) in factor mode, or J=ceil(sqrt(UK)) in exact-count mode.
Compute it by integer square comparison. Let T be the least power of two
at least2^22 J and tau=log2T. Prepare the phase register by H^tau, apply
controlled Grover powers2^j by exactly2^j repetitions of the controlled
circuit, then inverse QFT and measure its integer y. Total Grover queries
are T-1, not a unit-cost power operation. Each dyadic Fourier rotation is a
controlled translation into the same p=128n gradient: compute its controls'
AND, add/subtract the known power of two, erase the AND. Its ripple gates,
scratch, generation and inverses count. The exact-count width obeys tau<=(t+R)/2+(log2n)/2+45<=2t,
using t-2R>=80log2n; factor width is smaller. Thus tau<p, so all those
dyadics are exact on the ideal-gradient reference. The imperfect physical
gradient is replaced ONCE by its main-proof initial trace bound.
There is no prepared sine window or coherent array of repeated estimates.

For eigenphase phi, the probability amplitude at y is
 (1/T) sum_(j=0)^(T-1) exp(2pi i j(phi-y/T)).
Writing d for circular distance, its magnitude is at most1/(2Td), since
|sin(pi d)|>=2d for0<=d<=1/2. Summing both tails of1/(4|Tphi-y|^2) by
the integral bound sum_(k>=a)1/k^2<=1/(a-1) proves
 Pr(d(phi,y/T)>eps)<=2/(T eps-4)<1/16,
for eps=1/(1024J), as T eps>=4096. Folding gamma=min(y/T,1-y/T)
is1-Lipschitz on the phase circle and maps both eigenphases to theta/pi.
The same good folded estimate bound therefore holds for their mixture.

## Counted classical output and median confidence

Generate beta with |beta-pi^2|<=2^(-P), P=ceil(log2(K+1))+32.
Use P+16 alternating rational terms for each arctangent in
pi=16atan(1/5)-4atan(1/239), square the interval and round to denominator2^P.
The alternating remainders give the stated accuracy; the identity follows
from tangent addition and the angles in(0,pi/2). No real coefficient is advice.
All coefficient work is classical, polynomial in n, with O((log n)^3) bits.

After measuring y, compute v=round(U beta gamma^2) CLASSICALLY by exact
integer products/division, nearest-integer ties downward. In exact-count
mode clamp to[0,K+1]. For0<=M<=K, theta<=2sqrt(M/U), so
0<=U theta^2-M<=16K^2/(3U). In this configuration
 K^2/U=2^(80+2log2n+2R-t)<=2^(80-78log2n)<2^(-180).
The eps-good phase changes U*pi^2*gamma^2 by less than
64sqrt(UK)*eps+16U eps^2<1/8; the beta error is less than2^(-28).
Thus the rounded/clamped output is EXACTLY M on every good estimate.
At M=0 the zero phase yields zero. Bad estimates still give bounded words.

In factor mode clamp instead to[0,8U]. For every M>=1, theta>=sqrt(M/U).
The good estimate satisfies |pi gamma-theta|<=4/(1024sqrt(U)), at most
theta/(256sqrt(M)). Also M<=U theta^2<=(pi^2/4)M. The beta accuracy
therefore puts the unrounded v between0.99M and3M. If M>=2, rounding
keeps it in[M/2,8M]; for M=1 the lower bound0.99 rounds to at least1
and the upper bound rounds to at most3. Thus factor output lies in[M/2,8M].
No small-angle exact-count formula is asserted for large M.

Repeat the chosen private procedure b=2048n+1 times, resetting its index,
phase and scratch each time. Keep the integer results CLASSICALLY, sort,
and return their median. Conditional on any earlier classical history, each
new ideal-gradient private trial has bad probability<1/16. If the median
is bad, at least b/2 trials are bad. A union over their subsets gives
 probability<=2^b(1/16)^(b/2)<=2^(-b)<delta=2^(-200n).
This works for the exact integer or factor interval. No noise-independence
of the imperfect physical gradient is assumed: its one initial replacement
is applied before this analysis. At most O(n) quantum registers are live;
the b results and all sorting buffers use O(n^2) CLASSICAL bits.

## Born-weighted sparsification with a smaller cap

After measuring a low key, the source product index has uniform magnitudes
on a nonempty set S, size M, with arbitrary phases. Obtain a private factor
estimate Mtilde. Set h=0 if Mtilde<lambda; otherwise take the integer
floor-log2(Mtilde/lambda), clipped to[0,t], by shifts/comparisons.
Choose a uniform h-by-t binary matrix H, compute Hx by CNOTs and measure
only that hash, adding its observed value to the predicate. Do not measure x.

The Born law is: pick uniform z0 in S independently of H and retain its
hash bucket. Over F2, the bucket count is
 M'=1+sum_(z!=z0) 1[H(z XOR z0)=0].
Distinct nonzero differences are linearly independent in pairs. The
indicators have mean2^(-h), pairwise independence, and hence
 mu=1+(M-1)2^(-h), Var(M')<=mu.
For an accurate factor and h>=1, M2^(-h) is in[lambda/8,4lambda], so
mu is in[lambda/8,4lambda+1]. Chebyshev bounds the probability of
M' outside[lambda/16,16lambda] by5/mu<=40/lambda.
For h=0 an accurate estimate gives M<=4lambda. This is a statement about
the random matrix and Born-selected bucket, not every individual bucket.

Privately factor-estimate M' and reject the group if that estimate exceeds
256lambda. Every accepted exact-reference bucket has
M'<=512lambda<K. Every bucket in the concentration interval passes, since
its estimate is at most128lambda; every accurate unhashed bucket also passes.
The physical rare factor errors are included in the conditional error bound.

For an unhashed regular bucket the total partial-L-chunk mass over all
original low keys is at most2^b0(L-1)/2^t<=1/(16n).
For good hashed buckets it is at most16L/lambda, and the exceptional hash
probability is at most40/lambda. The extra mass is bounded by
 (40+16L)/lambda<=56/(2^30 n)<1/(16n).
Thus regular success remains at least1-1/(8n), justifying the SAME
f0=8n/(8n-1) and source recurrence as before. At the root the original
unpaired mass is at most1/4 and the extra hash mass is less than1/12,
so pair success remains at least2/3. Every selection uses low predicates
and original numerical indices, preserving unused top-label bits.

## Complete dictionary, exact quantum reindexing, and metadata

On an accepted bucket use the private exact-count median above to obtain M'.
Reject if its output is not in[1,K]. Enumerate exactly that many DISTINCT
verified masks. At row i, the remaining count k=M'-i is known. Mark z iff
it satisfies the low-key/hash predicate and differs from every found mask.
A literal list scan computes each equality into one flag, adds it into a
small match counter, and erases the flag; reverse all scratch after marking.
The full predicate and diffusion fit2^1500 n^2 L core steps, as proved by the streaming gate/compiler ledger in circuit-tools.md,
including all K=2^40 n L masks and their generated indices. No coherent list or QRAM is used.

Set S_k=ceil(sqrt(U/k)) by integer comparison and J_k the least power of two
at least8S_k. Choose uniform classical j<J_k, prepare H^t|0>, perform j
Grover iterations, measure and verify the ENTIRE predicate classically.
Cap trials per row at1024n; exhaustion aborts globally. The two-reflection
matrix gives success sin^2((2j+1)theta), sin^2(theta)=k/U. Since k<=K<<U,
sin(2theta)>=sqrt(k/U), and the finite geometric sum gives
 mean success=1/2-sin(4J_k theta)/(4J_k sin(2theta))>1/4.
No theta is used at runtime. J_k<16S_k<=32sqrt(U/k). The probability any
row exhausts is at most K(3/4)^(1024n)<=2^n*2^(-256n)<delta,
where K<=2^n and (4/3)^4>2. Every accepted mask is exactly verified and
distinct even on erroneous-count branches. The count is clamped, so all
loops and allocated lists remain syntactically bounded on those branches.

Numerically sort the COMPLETE mask list z_0<...<z_(M'-1). This uses O(M't)
classical bits and counted compare/swaps; it need not store all original
incidences or phase labels. Implement the EXACT total Boolean functions
 rank(x)=i if x=z_i, otherwise0; g(i)=z_i for i<M', otherwise0
by literal equality/XOR scans of this known list. Reuse one equality flag
and O(n) scratch, uncomputing after each row. Compute rank into zero,
XOR g(rank) into the old index and discard its now-zero reference register.
On the supported source indices this is the required phase-preserving
reindexing. No private count has a quantum source-index control.

Measure high rank bits, retain a full L chunk (two entries at the root),
and test its endpoint against the known M'. Copy its dictionary slice to
generate ALL metadata rows by the ordinary child raw/phase/weight formulas.
Its numerical order is EXACTLY the original rank order. Private counting
and enumeration never touch the retained source phase register.
The common-offset/raw/common-weight and unused-top-bit invariants therefore
hold without change. Failed quotient/field/mask checks abort as specified.
Even after erroneous counts every lookup is a total fixed-width unitary;
reset of remaining garbage is a defined channel, not an inverse promise.

## Complete cost, space and unconditional error accounting

Let E=ceil((t+3R)/2). An exact-count trial uses T<2^24sqrt(UK);
b<=4096n repetitions and original predicate cost give at most
2^2000 n^(7/2) 2^E core work. Factor mode is no larger.
For enumeration, sum_(k=1)^(M')J_k<=64sqrt(UM'). With1024n trials per row,
total iterations<=2^36 n^(3/2) 2^(ceil((t+R)/2)).
Multiplying the expanded exclusion predicate costs at most
2^2500 n^(7/2) 2^E, including initializations/verification at each trial.
Sorting, exact integer roots, rank/g lookups, all output arithmetic,
coefficient preparation and generated indices have loose bound
2^900 n^25 L^2. As (t-R)/2>=63log2n, L^2<=2^E/n^63.
Thus that polynomial work is also below2^900 n^4 2^E.
Their sum is less than the ACTUAL whole-node allowance
 G=2^10000 n^4 2^E.
Reserve G BEFORE the regular/root post-child instrument and pad accept/discard branches
to it; abort if it does not fit. No subroutine or source state is given free.
The previous expected leaf bound2^800n^25L and bounded gradient work also
fit G, using the same exponential margin. Global core/source guards and
terminal cleanup remain active. No emitted gate history is retained.

Only one full dictionary is live: release it before a vector returns to
its parent, which allocates its dictionary after all children are ready.
The whole dictionary uses M't<=2^40 n L t classical bits. Since t=O(H),
this is O(n^(3/2)sqrt(log2n)L), contained in the SAME table-stack envelope
O(n^2 L/sqrt(log2n)): log2n<=sqrt(n). Other private/classical buffers are
O(n^2). The private phase register/index, gradient and Boolean scratch use
O(n) qubits, a constant number live; all median/list data are classical.

Analyze an ideal-gradient exact-label reference. At each node replace
incorrect private factors/counts and rare enumeration aborts by their
correct outputs, paying the SAME fixed G. Conditional on every prior
correct private output, the two factor medians, exact-count median and
enumeration fail with probability at most4delta. Thus the probability
of any first private error in the entire capped computation is at most
4Bdelta<1/1024, because log2B<n/8. The algorithms agree until that first
error; arbitrary later channels/guards do not require any correctness
assumption. This conditional first-error union replaces the old approximate
coherent-counter workspace hybrid. In particular there is no reused
approximately clean count state, sine window or source-index count oracle.
Source-label coupling and the single gradient trace replacement are charged
separately; no IID assertion is conditioned on no earlier errors or caps.
All actual branches obey fixed list bounds, whole-node reservations and
paid cleanup even after arbitrary internal wrong outputs.

Randomized search and elementary phase estimation are standard (Boyer,
Brassard, Hoyer and Tapp, quant-ph/9605034v1, Sections4-5); all formulas and
costs needed here are proved above. No novelty or unit-cost oracle theorem
is a premise.

The sharper base/exclusion query bounds and their raw controller generation are proved in circuit-tools.md. Source calls are priced separately from nonsource bit/gate events by monitor-tools.md; every address remains fully charged.
