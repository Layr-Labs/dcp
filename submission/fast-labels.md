# PG5: exact fast Fourier circuits, reciprocal reduction and a global coin budget

This file specifies the new PG4 operations. The spectral ensemble, exact
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
The restoring division specified for PG3, with t-m+1=O(sqrt(n)) subtract/compare
stages of O(t) bit work, is sufficient. This O(n^(3/2)) logical preprocessing,
its full addressing and stored C are charged once, and fit the total sieve
work and classical memory envelopes. It is not instance-dependent advice.

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

No Fourier truncation is used in PG4. Prepare a single actual t-bit gradient
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

The exact flat-difference acceptance coin still draws clog(D) fair bits V,
with D=2(M0-d), retries when V>=D, and otherwise accepts the pair precisely
when V<M0. A completed ideal coin implements exactly its rational probability.
Each trial completes a coin with probability at least one half for every
history and every denominator. Denominators may depend on preceding outcomes.

Replace the per-coin trial cap by ONE counter shared across the entire sieve.
Permit at most 4R sampler trials in total. If a coin remains incomplete after
the last allowed trial, abort the entire algorithm and output zero. If the
last trial completed a coin, permit deterministic remaining steps and abort
only if another trial would be needed. Trial count is thus <=4R on every
branch. The number of coins is still less than R: the unchanged quotas give
sum_(i<ell)L_i<8L_0/7, at most L_i/2 pairs per stage, and J+1 batches, hence
fewer than (J+1)(4/7)L_0<R coins. Some pairs need no coin and only lower this
bound. The counter and every trial, reset and rejected draw are charged.

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
F=1048576*clog(1024(n+1))>=1048576. This comparison is additive. We do not
condition on no abort and assert an unbiased or independent successful
instrument; the ideal exact product law is transferred by the coupling.
The bound replaces, rather than adds to, the original 1/1024 coin budget.
All other shortage, outer-phase and verification budgets are unchanged.
The total failure remains at most 5/1024, preserving success1019/1024.

## 7. Complete charged resources

adaptive-arithmetic.md Section 5 supplies the joint PG5 substitution. Per-source
logical work O(n*2^(21sqrt(log2 n))) pays the full O(A_addr^2)=O(n) charge,
so all R=O(nL_0) sources cost O(n^3 L_0*2^(21sqrt(log2 n))). The unchanged
hard global4R trial cap and ordinary sorting/pair work cost O(n^3 L_0);
verification and all preprocessing fit the source envelope. Thus

    T=O(n^(7/2)2^((244949/100000)sqrt(n)+21sqrt(log2 n))).

Local scratch and current compiled-program/pointer records have size
polynomial/subpolynomial times n, and fit O(L_0) quantum and O(nL_0)
classical. This establishes the same address length before charging access.
All finite caps, resets, source acquisitions and aborts are included. The
same ideal-source success1019/1024, exact sample count and zero tolerance
apply jointly. The n<=16 branch stays exhaustive. Full new arithmetic,
structured representation, exact index and asymptotic comparison are proved
in adaptive-arithmetic.md. Direct sources include PG4
 e40f2d5a-68c9-418b-b4e8-64a80305968e and the earlier explicitly acknowledged
PG3/PG2/MDC1/VFD3 foundation. No prior verdict is a premise.
