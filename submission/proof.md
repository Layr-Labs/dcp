# CADGR2: compressed adaptive robust threshold-block search

## Joint theorem, configuration and attribution

For every integer N>=2 and s in Z/NZ, let n=ceil(log2 N), D=2^n,
m=262144(n+20), r=floor(85m/256), A=n+20 and p=n+ceil(log2 m)+40.
The following algorithm acquires exactly Q=m source copies on every branch,
recovers the entire secret with unconditional probability>2/3, and jointly has

 T=O(2^(n/2+64sqrt(log2 n)) n^2(log2 n)^2),
 S_C=O(n^2) bits, S_Q=O(n) qubits, Q=m=O(n), tau(n,Q)=floor(85Q/256).

Time is declared for n>=2, with the finite n=1 branch specified below.
The indices are1,0,0,0. This is not subexponential time or the cube-root goal.
Direct predecessor: CADGR1 b2732ecd-4d8b-4873-9f0f-0c2f0a2bedd8, whose compressed algorithm and complete proof are reproduced and adjusted here.
Direct sources: RGRST1 5ca6075a-9dc9-42e2-9658-244ffae218a9
(threshold/tail/hybrid), RLQGR3 57a662bc-c2a5-421a-8400-cc39fb3d2998
(adaptive exact arithmetic and accounting), RLQGR2
8657ff0f-f4d3-4605-a583-a6d57d3205f4 (the directly carried label helper), and PG4
e40f2d5a-68c9-418b-b4e8-64a80305968e (reusable-gradient kickback and
one-initial-trace-error design, crediting Nam/Su/Maslov1803.04933v2 SectionII).
The compressed-control algorithm and mixed-eigenlabel gradient preparation
were developed in our CGRST1 bc7954eb-c7bb-47c0-abcd-6a95a0257673, whose
hosted review failed without a verdict/publication. Its proof is reproduced,
not assumed accepted. Earlier RLQGR2/GRST1/RST1 ancestry and Gidney arithmetic
attribution are retained. Standard context: Kitaev quant-ph/9511026v1 and
Grover quant-ph/9605043v3. Every needed argument is reproduced; no earlier
verdict, Fourier oracle or purification is a premise.

## Explicit fixed-position corruption model

Before private randomness, an adversary chooses at most floor(85Q/256)
acquisition positions and an arbitrary joint state on their declared n+1
qubit source registers. The remaining copies form an independent ideal
rho_s product for the same s, independent of the malformed subsystem.
Malformed copies may be mutually entangled. The adversary may know N,s and
the algorithm but cannot modify registers/controller after delivery or choose
positions adaptively from private outcomes. The algorithm is not told them.
This is exactly the error_model used by RGRST1/RLQGR2, with the stated
stronger count than RLQGR2. Clean input is included; no corruption probability
or impossibility of larger tolerance is claimed. Counts refer to actual Q.

## Compressing the source block without a free Fourier transform

Set chi_a=N^(-1/2)sum_y exp(2pi i a y/N)|y> and
phi_(a,s)=(|0>+exp(-2pi i as/N)|1>)/sqrt2. Expanding rho_s and summing its
uniform x cancels unequal Fourier labels, yielding exactly
rho_s=(1/N)sum_a |phi_(a,s)><phi_(a,s)| tensor |chi_a><chi_a|.
The Fourier vectors are analysis notation, not a physical transform.

Process every source copy sequentially with label-tools.md using K=N,d=n,
planned count C=m. Keep its SOURCE control qubit unmeasured and store the
extracted n-bit label classically; discard/reset its data and extraction
scratch before acquiring another. For an honest copy the latent a is uniform,
its control remains phi_(a,s) conditional on a, and extraction returns a except
with the stated small probability. Malformed input undergoes the same bounded
protocol; it leaves one arbitrary control qubit and a label in[0,N), possibly
correlated with other malformed qubits/labels. There are still at most r such
positions. Honest copies remain independent of that subsystem.

For analysis define ideal compression by giving each honest copy its true
latent label instead, while leaving the malformed instrument unchanged.
The joint classical-label/quantum-control state sigma of this reference has
independent honest pairs(a,phi_(a,s)), with a uniform, and the arbitrary
malformed subsystem independent of them. Couple it to the actual extraction
using the exact source ensemble. On every correct honest extraction the
outputs and controls agree, so trace-distance error is at most the probability
of any honest label error, <1/2048<1/1024. This is a replacement comparison
with the UNCONDITIONAL ideal state, not conditioning on correct labels;
conditioning would incorrectly bias the uniform labels. All m copies are
acquired before the following gradient preparation, so even an eventual abort
has exactly Q=m rather than a random source count.

## Counted preparation of an approximate reusable gradient

Let G=2^p and gamma=G^(-1/2)sum_z exp(-2pi i z/G)|z>.
This ideal vector is a reference, not a free ancilla. Prepare an actual
mixed state close to it with the following exact Clifford+T protocol.
For at most A attempts, prepare a p-qubit maximally mixed register by H on
zero qubits followed by computational measurements whose outcomes are erased
and never used. It is I/G, equivalently a uniform mixture of Fourier vectors
chi_b of translations modulo G. All randomness, erasure and resets are charged.
Apply label-tools.md with K=G,d=p,planned count C=A. If the observed label b
is even, reset/release that register and try again. If it is odd, compute
a=-b mod G and its inverse by counted classical extended Euclid. Apply the
in-place permutation y->a*y mod G and retain the resulting register.
If no observed odd label occurs in A attempts, abort and output zero.

Multiplication by odd a is an exact permutation on all p-bit strings. Compute
its product low p bits into zero, swap, and XOR its inverse product to clear
the old input. fast-arithmetic.md supplies the counted clean integer products;
no phase gate synthesis is needed. On a correctly learned odd latent b,
this permutation maps chi_b to chi_(b*a^(-1))=chi_(-1)=gamma.
A fresh I/G each attempt has uniform independent latent b. The probability
of all A true labels being even is2^(-A). The label lemma bounds any mistaken
gradient label by<1/2048, and2^(-A)<1/2048 at n>=2. Thus abort or a wrong
retained gradient has combined weight<1/1024 in this ensemble analysis.

The physical gradient is generally MIXED, not a heralded exactly pure
non-Clifford Fourier state. In its analysis ensemble good weight is exactly
gamma; arbitrary bad weight plus aborts is<1/1024. Replacing the output by
an always-supplied gamma therefore costs at most1/1024 in trace distance,
charged ONCE for all future reuse by contraction. Metadata is unused afterward.
Fresh gradient registers and fixed preparation parameters are independent of
the source block; no extra DCP copy is acquired. Attempts, resets and aborts
are counted; no unobserved favorable event is postselected by the algorithm.

## Exact gradient use and bounded phase quantization

For stored label a and candidate t compute z=a*t mod N and
q=floor(G*z/N) in a clean p-bit quantum register. Add q modulo G into the
gradient, conditioned on the corresponding retained source-control being1,
then uncompute q and z. Translation by q has eigenvalue exp(+2pi i q/G)
on gamma, so gamma is unchanged and the source control gets that relative
phase. This works also for superposed t or entangled source controls. The
ideal-gamma subspace remains invariant after every such addition.

The reference phase correction is R_(a,t)=diag(1,exp(+2pi i at/N)). Since
q/G approximates z/N within1/G, each implemented rounded correction differs
in operator norm by<2pi/G<8/G. No physical arbitrary rotation is assumed.
Compute q EXACTLY: for u=G*z<2^(p+n), precompute C0=floor(2^(p+n+1)/N),
then q0=floor(u*C0/2^(p+n+1)) is floor(u/N) or one less. Calculate its
remainder and use one correction. All operands have O(n) bits; the complete
compute-XOR and inverse work is the same reciprocal construction as the
addendum. Power-of-two quotients are wire copies, not long divisions.

Use V_t applying these corrections then H to the m retained controls.
Count their computational ones coherently and reflect on [t<N AND weight<=r],
then undo V_t. A logarithmic-width weight register increments once per
control; clean controlled ripple increments and reverse cost O(m log m)
gates and O(log m) scratch. This implements a unitary reflection exactly,
including on arbitrary malformed data. Its ideal reference uses the exact
R_(a,t) above; invalid candidates have projector0 and are unmarked.
The V error is<=8m/G. Pulling back a projector costs at most twice that,
and reflecting costs another factor2, so rounded-query operator error is
<=32m/G on the invariant ideal-gamma subspace, uniformly over all label records.
Across j<=3*2^(n/2)/4 Grover queries the vector error is at most
24m*2^(n/2-p)<=24*2^(-n/2-40). A measurement-event probability changes by
at most twice vector distance, hence this error contributes<1/1024.

## Threshold guarantee under arbitrary malformed joint states

For exact phase corrections and ideal honest labels, t=s makes every honest
control zero after H. At most r malformed controls can be one in any basis
component, even if entangled. Thus the true projector P_s fixes sigma.
For false t<N, an honest control-one probability conditional on a is
sin^2(pi a(s-t)/N). Averaging its uniform a gives1/2 by the geometric-series
identity. The labels and phase qubits are independent across honest copies,
so their analytic measured ones have Bin(h,1/2) distribution, h>=171m/256.
Malformed contributions cannot reduce honest ones; hence acceptance implies
Y<=r. Since h/2-r>=m/512, bounded-variable concentration gives

 tr(P_t sigma)<=exp(-2(m/512)^2/h)<=exp(-m/131072)
               =exp(-2(n+20))<=2^(-(n+20))=:eta.

For that concentration inequality, centered log MGF second derivative is a
tilted variance<=1/4 for variables in[0,1]. Integrate twice and optimize
Markov to obtain exp(-2d^2/h). The bound is uniform in every false t and
allowed malformed state; malformed outcomes need no independence or bias.

This probability averages the joint classical-label/qubit state; fair
controls are NOT asserted conditional on a fixed label record. A direct sum
over records of sqrt(p_record)*purifications, with their separately compiled
unitaries, gives a vector fixed by P_s and the displayed false-projector norms.
It is only analysis: physical branches read labels sequentially with uniformly
bounded cost, requiring no QRAM or physical coherent label/purification access.

## Search, whole-computation hybrid and success

For n>=2 prepare n Hadamards and use exactly j=isqrt(9D) div4 query/diffusion
iterations, measuring the candidate and returning it if<N, otherwise zero.
The gradient abort already specified returns zero. No other restart,
postselection, verification copies or source operation is used.
Compare the exact reference block query B with B_* marking only s and doing
nothing to the block. For any candidate amplitudes tensor the original
purified direct-sum block, squared query error is
4sum_(t!=s)|a_t|^2||P_t v||^2<=4eta.
Telescoping the j iterations, every ideal prefix leaves the original block
unchanged and every physical suffix is unitary. Final vector error<=2j sqrt eta
<=3/2048, changing marked probability by<=3/1024. This accounts for all
reuse disturbance without claiming fresh or independent actual queries.

Ideal Grover success is at least25/36: with theta=arcsin(1/sqrt D), the usual
2-by-2 query/diffusion multiplication gives sin^2((2j+1)theta). Since D>=4,
theta>=1/sqrt D and arcsin(x)/x<=pi/3 for x<=1/2, the angle lies in[1,2pi/3].
The minimum of sine squared is at an endpoint; sin1>=5/6 and the other value
is3/4. There is no trigonometric computation in the circuit. Summing the
honest-label replacement, gradient preparation, rounding and block-hybrid
allowances gives unconditional success at least25/36-6/1024>2/3.

At n=1, N=2, instead acquire all m full source copies and perform binary
threshold projectors t=0 then1 on the original data using controlled modular
subtraction,H and the same weight<=r test. Measure ONLY the aggregate flag,
uncompute and retain the rejected block; zero fallback. The true projector
fixes the allowed input and each false projector weight<=eta as above.
s=0 succeeds certainly; for s=1, w=(I-P_0)v gives
||P_1 w||>=|<v,P_1 w>|=1-tr(P_0 sigma)>=1-eta, so success>2/3.
This is fixed finite work/space and does not run gradient preparation.
Its finite O(m(n+1)) qubits are absorbed in the uniform O(n) bound at n=1.
Every branch, including gradient aborts for n>=2, has exactly Q=m.

## Fully charged uniform resources

At n>=2 keep m single source controls and mn classical label bits. Extraction
adds only one n-bit source data register and O(n) scratch; release it before
the next copy. Gradient preparation adds O(p) registers/scratch, p=O(n).
Queries use the same O(n) product workspace, p-bit gradient, n-bit candidate,
O(log m) weight and O(n) quotient buffers. Stages reuse work. Thus ALL quantum
registers have peak O(n); no m data registers persist. At n=1 the finite
full-block allocation fits an absolute outside constant. Classical labels,
N, reciprocals, counters, gradient metadata/inverse, generated arithmetic
bands/stack and all input/output/intermediates fit O(n^2) bits.

Establish this allocation before charging its O(log(n+2)) address width.
Ordinary bit-scan templates, index additions and their own accesses, gate
emission and classical record reads cost O(log^2(n+2)) per logical gate;
no word operation or table access is free. fast-arithmetic.md reproduces
RLQGR3's exact adaptive composite-ring interpolation, clean normalization
and reciprocal reduction. A clean product at width v costs
O(v 2^(64sqrt(log2 v))(log2 v)^2) fully CHARGED work and O(v) quantum scratch.
This includes logical gates, generated coefficients, classical intermediate
arithmetic, inverse work and whole-memory addressing. Its fixed finite-size
branch and uniform controller proof are part of that same theorem.
Use common width v=64(p+n+20): ceil(log2 m)<=n+23 gives p<=2n+63 and
v<=8192n for n>=2. Every operand, product, source correction, quotient
and gradient permutation fits this width. Multiplying width by a fixed
constant changes sqrt(log2 v)-sqrt(log2 n) by at most sqrt(log2 8192),
so its extra factor is an absolute outside constant, not a new unknown
inside-exponent coefficient. Thus each required product costs
O(n 2^(64sqrt(log2 n))(log2 n)^2). The exact reciprocal phase quotient
above uses a constant number of such products, shifts and single corrections
with O(n)-bit operands; it does not perform p stages of long division.
Controlled gradient addition, complete cleanup and constant ordinary scans
are smaller. Across m=O(n) controls the query work is
O(n^2 2^(64sqrt(log2 n))(log2 n)^2). Weight, diffusion and the O(n)-bit
iteration counter are smaller. With j<=3*2^(n/2)/4, this proves the stated
time envelope on every branch, including arbitrary malformed inputs.

Source and gradient label extraction have O(n^3) Hadamard tests, each O(n)
translation gates, plus polynomial empirical means, rational decoding/rounding
and inverse/parameter generation. ALL A attempts, discarded registers,
measurements, erasures and resets are included. A conservative O(n^8) charged
preprocessing bound is absorbed by the exponential envelope. Source acquisition
cost is exactly m(n+1)=O(n^2). Fixed table generation and the finite n=1 branch
are also counted. Every loop/allocation has an explicit cap on arbitrary
malformed inputs; there is no expected-only cost, free postselection, uncharged
parallel work or omitted precision/preparation term.

The structured envelopes are2^(n/2+64sqrt(log2 n))n^2(log2 n)^2,n^2,n,n,
with exact indices1,0,0,0. The count law floor(85Q/256) uses actual Q=m under
the same error-model text as RLQGR3. Relative to the earlier compressed
CGRST1 construction, time improves by the ratio
n^(-3/5)2^(64sqrt(log2 n))->0 while space/sample/tolerance envelopes persist.
Relative to RLQGR3's measured-record search, all four resource envelopes
match and the guaranteed malformed count increases from floor(Q/10) to
floor(85Q/256). The algorithms differ: CADGR2 retains source phase controls,
uses coherent threshold reflections and a whole-computation block hybrid.
These compare supported upper guarantees, not tight costs or practical
crossovers. RGRST1 retains a smaller time/classical-space guarantee with
more qubits and remains a tradeoff. This is not a new growth index,
fastest-known DCP result or cube-root goal. Gradient preparation is
explicitly approximate; reference states/purifications remain analytic.

## Explicit improvement over the published compressed predecessor

CADGR1 used m=1024(n+20) and fraction5/16. This construction uses m=262144(n+20) and fraction85/256, an increase of5/256. Its honest-minus-false threshold margin is smaller, m/512 instead of m/32. The source-count coefficient increases by256 so the concentration exponent and all subsequent probability budgets remain unchanged. All four asymptotic resource envelopes match CADGR1; their absolute outside constants increase. This is a supported-fraction improvement, not a new growth index, an assertion of tight complexity, or an impossibility result at fraction1/3.
