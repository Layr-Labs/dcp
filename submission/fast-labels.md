# RS4: exact fast Fourier circuits, reciprocal reduction and a global coin budget

This file specifies the inherited exact source framework used by RS4. The spectral ensemble, exact
modular-add permutation, bounded gradient preparation, minimum-depth schedule,
quotas, outer phase decoder and final verification remain as reproduced in
proof.md and phase-labels.md. The constructions below are uniform algorithms,
not additional integer-arithmetic or quantum Fourier oracles.

## 1. The actual adaptive integer product

The exact adaptive product, all growing interpolation coefficients, fixed-loop
child widths, bit-operation recurrence, reversible evaluation and uniform
address/pointer representation are completely specified and proved in
adaptive-arithmetic.md Sections 1-3. For v-bit operands its logical cost is
M(v)=O(v*2^(20sqrt(log2 v))), with that explicit known coefficient.
All matrices are generated with counted arithmetic; there is no multiplication
oracle or preloaded instance advice. The base v<=65536 uses schoolbook loops.

## 2. Exact overlap-aware rectangular multiplication

For long v-bit A and short w-bit B, split A into h=ceil(v/w) base-2^w digits.
Compute each balanced product P_i=A_i B by the adaptive routine and write
P_i=u_i+2^w v_i. Emit u_0, then for i=1,...,h-1 add u_i+v_(i-1)+carry,
emit its low w bits and pass its single carry. Finish with v_(h-1)+carry,
allowing its final bit. This is exact column addition with only two terms
and one carry per column, so the overlap pass costs O(hw), not h full-v-bit
additions. The total is O(h*M(w)+v), and for v=O(n),w=O(sqrt n) this is
O(n*2^(20sqrt(log2 n))). Boolean evaluation/reversal gives the same bound
for gates and scratch. All coefficient generation and signed/carry logic
are included by the adaptive product proof.

## 3. Exact coherent translation from a counted precomputed reciprocal

For the sieve's fixed R put a=clog(2^20 R), t=n+a+4, H=2^t and
m=floor(log2 N). Compute C=floor(H/N) CLASSICALLY once before source acquisition.
To generate it explicitly, setW=H,C=0 and for j=t-m,...,0 compareW with
N*2^j. WhenW>=N*2^j subtract that threshold and set quotient bitj inC.
The invariantW<2N*2^j before each comparison, andW<N*2^j after it, proves
one subtraction suffices and the final remainder is<N. All integers have
O(t) bits, includingH's extra leading bit. The t-m+1=O(sqrt(n)) stages cost
O(n^(3/2)) logical bit work. Full addresses and storedC are charged once and
fit the overall sieve work and memory envelopes. It is not instance-dependent advice.

For a quantum t-bit phase integer k, reversibly compute

    q0=floor(k*C/H), r0=k-q0*N.

The reciprocal approximation satisfies 0<=1/N-C/H<1/H. Since k<H,
0<=k/N-k*C/H<1. Thus q0 is either floor(k/N) or one less, and 0<=r0<2N.
Compare r0 to N and subtract once if needed to obtain r=k mod N. All formulas
are total and exact on every t-bit k. The quotient q0 and constant C have at
most w=t-m+1=O(sqrt(n)) bits. Both products are long-by-short: k*C and q0*N.
Section 2 computes them with O(n*2^(20sqrt(log2 n))) logical gates, including overlap
carries; extracting the power-of-two quotient is a bit selection. Subtraction,
comparison and the optional correction use O(n) gates. No uncharged division
or multiplication remains in this coherent circuit.

Keep k unchanged. Evaluate the remainder circuit reversibly, use r as a quantum
addend in the exact modular permutation on source data x, and then reverse the
remainder computation. On x<N the permutation is x -> x+r mod N; on invalid
encodings x>=N it is identity, by the explicit arithmetic/MUX construction in
proof.md Section 2. With r fixed, its subtraction circuit is the inverse, so
compute/swap/inverse clears the old x register exactly. All carry/history
ancillas are uncomputed. The total map is |k>|x> -> |k>|x+k mod N> on valid
x, extended by identity outside the valid range. This is the exact product of
the original phase-estimation controlled powers. For source eigenstate chi_y,
its eigenphase is exp(2pi i*k*y/N); the first source qubit is untouched.
All operations are uniform counted Clifford+T gates. Their logical count and scratch fit O(n*2^(20sqrt(log2 n))).

## 4. Exact binary Fourier transform with recursive product phases

No Fourier truncation is used in RS4. Prepare a single actual t-bit gradient
by phase-labels.md's bounded preparation. First analyze an ideal gradient G_t.
For a local Fourier circuit of v<=t bits, let k=floor(v/2), l=v-k. Write its
input integer as x=A+2^k B, with A k bits and B l bits. The exact recursive
Fourier circuit is:

1. Apply F_l to the B block, with output integer C.
2. Apply the phase exp(2pi i*A*C/2^v).
3. Apply F_k to the A block, with output integer D.
4. Rotate the two contiguous blocks so that the output integer is C+2^l D.

F_0 is identity and F_1 is H. To prove the circuit, substitute
x=A+2^k B and z=C+2^l D into the Fourier kernel:

    x*z/2^v = B*C/2^l + A*C/2^v + A*D/2^k + B*D.

The last term is an integer and has trivial phase. The three other terms are
exactly the two recursive Fourier phases and the middle product phase, with
normalization 2^(-v/2). This proves the entire Fourier matrix on basis inputs;
linearity proves the unitary identity. Block rotation is a fixed permutation,
implemented with three reversals and O(v) SWAPs. Keeping actual child blocks
contiguous avoids any uncharged arbitrary permutation or address map.

To implement the middle phase, reversibly compute A*C by Section 1 into a
v-bit product register, retaining its Boolean history. Add that product modulo
2^v to the TOP v bits of G_t, then reverse the product computation. The ideal
gradient's eigenphase is exactly exp(2pi i*A*C/2^v) and G_t is returned unchanged.
Only its top v bits are addressed by the adder: adding a multiple of 2^(t-v)
to the whole integer leaves all lower bits untouched. Therefore this addition
costs O(v), not O(t) at every recursive node. The product circuit costs O(M(v)), including cleanup, and needs at most
that many temporary wires, with all classical generated records counted.

The Fourier recurrence has two half-size children and O(M(v)) local
product/adder/permutation work. Summing levels gives
Q(v)=O(v log(v)*2^(20sqrt(log2 v)))=O(v*2^(21sqrt(log2 v))).
adaptive-arithmetic.md Section 4 proves the exact coefficient21 and its
absorption of the logarithmic level count. Each local adder touches only
the TOP v bits, avoiding a full-t cost at every recursive node. Generated
local gate lists, their O(A_addr)-bit records, classical constants and
quantum Boolean-value history are all stored/counted and released/reused.
The inverse is the reversed exact circuit; no Fourier oracle is assumed.

The actual gradient is only approximately prepared. Its abort probability is
<2^-122 and, conditional on success, its input trace distance from G_t is
<2^-36, by the fully specified preparation in phase-labels.md. The ideal
resource is returned unchanged through all product phases and all sources.
The entire actual computation is within that single initial trace distance
of the ideal comparison computation by contractivity. Independence or refresh
of an imperfect gradient is never assumed. Exact ideal binary QPE still gives
per-label rounding error <1/(2^23 R); its all-acquisitions union is <2^-23.
Hence 2^-23+2^-36+2^-122<1/1024 is the complete source contribution. The
removed truncation introduces no new error budget.

## 5. Exact measured-residue rounding

For measured phase integer Z, compute P=N*Z with Section 1's integer algorithm
using v=O(n), then q=floor((P+2^(t-1)-1)/2^t). This rounds to the nearest
integer with halfway ties toward the smaller, since P is an integer and its
remainder modulo 2^t determines the rounding. Map q=N to zero. The product
uses O(n*2^(20sqrt(log2 n))) logical bit operations, while the shift, addition, comparison
and final correction are O(n). These classical costs, circuit generation,
initialization and all memory/address operations are counted. Together with Sections 3-4 they bound one source extraction by
O(n*2^(21sqrt(log2 n))) logical operations, including all compilation.

## 6. One global rational-coin trial budget, charged on every branch

Each primary/rescued coin is defined in recycle-sieve.md with positive
O(n)-bit denominatorD and numeratorP<=D. Draw clog(D) fair bitsV, retry when
V>=D and otherwise accept whenV<P. Every completed ideal coin implements
its exact probability. Every trial completes with probability at least one
half conditional on every past history and every label-dependent denominator.
The explicit zero/out-of-range cases are handled by the salvage rules.

Replace the per-coin trial cap by ONE counter shared across the entire sieve.
Permit at most 4R sampler trials in total. If a coin remains incomplete after
the last allowed trial, abort the entire algorithm and output zero. If the
last trial completed a coin, permit deterministic remaining steps and abort
only if another trial would be needed. Trial count is thus <=4R on every
branch. The NEW branchwise coin count is<=3L_i/4, notL_i/2, by
recycle-sieve.md Section8. Primary/secondary/tertiary/global-V calls are
<=P1-Z1+P2-Z2+P3-Z3+P4+P_V<=3P1/2<=3L_i/4, including V's nontrivial zero coin.
With sum_i L_i<2L_0 this gives fewer than(3/2)(J+1)L_0<R coins overall.
All denominators are positive O(n)-bit integers with completion probability
at least one half; the same hard cap and following coupling therefore apply.
The counter and every trial, reset and rejected draw are charged.

Analyze uncapped ideal coins and couple until the first global budget abort.
If at most R coins have not all completed after 4R trials, there were fewer
than R completions. Every trial's completion indicator, conditional on the
past, has probability at least one half. To see the required domination,
represent that indicator using a fresh independent uniform U with threshold
its conditional completion probability. It is at least the Bernoulli indicator
[U<=1/2]. Additional outcomes can be conditionally sampled with independent
randomness; this is a proof coupling, not a source operation. Extend an already
finished execution with dummy Bernoulli trials if necessary. The number of
completions therefore stochastically dominates Binomial(4R,1/2), of mean 2R.
The elementary Chernoff inequality already proved in proof.md gives

    Pr(global trial budget causes an abort)<=exp(-R/4)<1/1024.

The last inequality holds uniformly: L_0>=F, J+1>=1, so R>=4F and
F=2^62*clog(1024(n+1))>=2^62. This comparison is additive. We do not
condition on no abort and assert an unbiased or independent successful
instrument; the ideal exact product law is transferred by the coupling.
The bound replaces, rather than adds to, the original 1/1024 coin budget.
All other shortage, outer-phase and verification budgets are unchanged.
The total failure remains at most 5/1024, preserving success1019/1024.

## 7. Complete RS4 charged resources

The retained exact source extraction costs O(n^3 L_0*2^(21sqrt(log2 n)))
in total, including generated constants, reciprocal, rounding, pointer/local
program records and full addresses. The new C_d, degree-seven E_d and global-V J_d kernels
require adaptive arithmetic and adds O(n^3 L_0*2^(20sqrt(log2 n))) ordinary
sieve work, explicitly charged rather than assumed linear per group. The
global4R sampler cap costs O(n^3 L_0). All memory, source-count and error
arguments transfer as proved in recycle-sieve.md, with the new actual L_0.
Its exact capacity and rational log bounds yield coefficient2279247/1000000 and
L_0=O(log2 n*2^((2279247/1000000)sqrt n)). Hence the joint total work is
O(n^3(log2 n)*2^((2279247/1000000)sqrt n+21sqrt(log2 n))), with classical
O(n(log2 n)2^((2279247/1000000)sqrt n)), quantumO((log2 n)2^((2279247/1000000)sqrt n)),
and the same sample envelope as classical memory. Every source/trial,
initialization, failed attempt and allocated scratch is counted. All claims
are for oneRS4 configuration; no predecessor verdict is a premise.

RS4 directly reuses SG6 dc8d6d56-9618-46bc-97a3-e9b18ec65099's
primary/triangular rescue component, but changes pairing to whole-bucket
SUM pooling and proves the new conditional populations and quotas in
recycle-sieve.md. This is the single present configuration.

RS4 directly reuses PS7 cda83fcf-1faa-41d5-b858-d5ec44122fe6's
population framework but adds a third SUM pass and globally recycled PRIMARY
rejects. recycle-sieve.md gives the complete changed channel/count/cost proof;
old pass-specific bounds are not assumed unchanged.

The actual RS4 ordinary-work bound includes all four current count kernels
C_d,E_d,F_d,J_d, including the V zero-label coin. recycle-sieve.md Sections3-4
and9 specify their exact integer evaluation and all branchwise allocations.

## RS4 extension and provenance

This file is adapted from RR8 at ae634c28a7e4a2683087607a83a432adb370b5d7.
The present program adds the fourth SUM channel proved in recycle-sieve.md,
with q=193/32, F=2^62lambda and coefficient 2279247/1000000. The historical
ancestry descriptions above identify inherited material. Any old three-pass
summary is extended by that explicit fourth pass; no predecessor verdict is
used. All four kernels, including the degree-fifteen kernel, have constant
degree and O(n)-bit operands. Their counted adaptive arithmetic fits the
same O(n*2^(20sqrt(log2 n))) logical work per pair with absolute constants.
