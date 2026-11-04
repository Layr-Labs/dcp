# PG4: exact fast Fourier circuits, reciprocal reduction and a global coin budget

This file specifies the new PG4 operations. The spectral ensemble, exact
modular-add permutation, bounded gradient preparation, minimum-depth schedule,
quotas, outer phase decoder and final verification remain as reproduced in
proof.md and phase-labels.md. The constructions below are uniform algorithms,
not additional integer-arithmetic or quantum Fourier oracles.

## 1. A completely specified fixed sixteen-way integer product

For integers A,B of at most v bits, handle their signs explicitly and multiply
their absolute values. For v<=4096 use ordinary binary schoolbook multiplication.
For larger v put k=ceil(v/16), base D0=2^k, and write the operands as sixteen
digits A_i,B_i, 0<=i<=15. Define their degree-15 digit polynomials A(X),B(X).
Recursively compute the thirty-one integer products

    V_j=A(j)*B(j), j=0,...,30.

Polynomial evaluations use Horner's rule, multiplication by a fixed integer
j<=30 via binary shift/add, and ordinary carries. Every evaluation is below
2^k sum_(i=0)^15 30^i <2^(k+80). Consequently recursive operands have at most
ceil(v/16)+80 bits. The bound is independent of the operands' actual digits.

The following finite integer computation supplies exact interpolation; it is
performed once, with its entire constant time and space charged. Set D=30!.
For each j form the integer coefficient vector of

    P_j(X)=prod_(0<=h<=30,h!=j)(X-h),
    d_j=prod_(h!=j)(j-h)=(-1)^(30-j) j! (30-j)!,
    M_(j,i)=(D/d_j)*coefficient_i(P_j), i=0,...,30.

Generate P_j by successive multiplication by X-h, beginning with one. The
integer d_j divides D. These are fixed constants independent of v,N,s. For
any polynomial P of degree at most thirty, the polynomial
sum_j P(j) P_j(X)/d_j agrees with P at thirty-one distinct integers, so their
difference, of degree at most thirty with thirty-one roots, vanishes. Applying
this identity to A(X)B(X) recovers its integer coefficients exactly as

    c_i=(sum_(j=0)^30 M_(j,i)*V_j)/D.

Every division is exact because these are the product's integer coefficients.
Intermediates are signed and processed with sign/magnitude or standard signed
binary arithmetic. Their bit lengths are O(v)+O(1), since there are fixed
thirty-one terms and fixed integer constants. Multiplication by each fixed
M_(j,i) is a fixed number of shifted additions, hence O(v) bit work. Exact
division by the fixed positive D is O(v): scan binary digits, maintain a
remainder less than D, compare/subtract D and emit a quotient bit. D's width
is an absolute constant; no integer division is unit cost. Recombine the
product sum_i c_i D0^i using shifts and carries. All nonrecursive work is O(v).

Thus for a fixed absolute c0 the bit-work recurrence is

    C(v)<=31*C(ceil(v/16)+80)+c0*v.

It proves C(v)=O(v^(5/4)). For v>4096 put z=v-128; the recursive size minus
128 is at most v/16+81-128<=z/16. The coefficient at power 5/4 contracts:
31/16^(5/4)=31/32<1. Induction with a sufficiently large absolute constant
absorbs c0*v in the remaining fraction of z^(5/4); enlarge the constant for
the finite base range. All fixed interpolation generation and base-case costs
are included. This is an upper bound with exact rational exponent, not a
unit-cost invocation of multiplication. Classical depth-first storage is
polynomial (O(v) intermediates along a geometrically shrinking call stack
suffice); even the looser O(v^2) bound fits the declared sieve workspace.

The entire computation can also be a uniform bounded-fan-in Boolean circuit:
use binary addition, comparison, fixed multiplication/division and the fixed
recursive schedule. Evaluation of that Boolean circuit reversibly retains each
Boolean gate output in a fresh wire. NOT/CNOT/Toffoli compute it, with the
exact Clifford+T Toffoli decomposition already given. Copy the final result
if needed and reverse the Boolean schedule to clear all history. There are
O(v^(5/4)) gates and temporary wires. For a phase computation one may retain
the computed product, apply the phase, and reverse once. These are explicit
clean reversible circuits; no quantum integer-product oracle is assumed.

## 2. Unbalanced products with overlap-aware carry propagation

Let A have at most v bits and B at most w bits, 1<=w<=v. Write A as h=ceil(v/w)
base-2^w digits A_i. Compute each product A_i B with the preceding balanced
routine at cost O(w^(5/4)). Write that 2w-bit product as u_i+2^w v_i.
To combine them, emit u_0 as the lowest digit, then for i=1,...,h-1 compute
u_i+v_(i-1)+carry. Emit its low w bits and pass its single carry bit. Finish
with v_(h-1)+carry, allowing its final carry. This is ordinary column addition;
each column has only the two indicated terms and one carry. Its total bit work
is O(hw), rather than h full-length additions. The resulting product is exact.
Total complexity, including all carries, is

    O(h*w^(5/4)+v)=O(v*w^(1/4)+w^(5/4)+v).

For w=O(sqrt(n)), v=O(n), this is O(n^(9/8)+n), in particular O(n^(5/4)).
The same Boolean evaluation and reversal give that gate/scratch upper bound
for quantum operands. Known constants are allowed as one operand, but every
fixed multiplication/addition is still explicitly computed.

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
Section 2 computes them with O(n^(9/8)+n) logical gates, including overlap
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
All operations are uniform counted Clifford+T gates. Their logical count and
scratch are O(n^(5/4)), a conservative bound for the rectangular products.

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
costs O(v), not O(t) at every recursive node. The product circuit costs
O(v^(5/4)), including cleanup, and needs that many temporary wires.

The recurrence is

    Q(v)<=Q(floor(v/2))+Q(ceil(v/2))+O(v^(5/4)),

so Q(v)=O(v^(5/4)). For example summing costs by recursion levels gives a
convergent ratio 2/2^(5/4)<1, with the finitely many odd-size adjustments
absorbed; equivalently use a constant-shift induction. Peak scratch is
O(v^(5/4)): the first child completes before the middle product is allocated,
and that scratch is cleared before the second child. All recursion, Boolean
schedule, block reversals and wire addresses are generated uniformly. The
inverse circuit is its reverse. There are no arbitrary rotations and no
unaccounted FFT or Fourier primitive.

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
uses O(n^(5/4)) logical bit operations, while the shift, addition, comparison
and final correction are O(n). These classical costs, circuit generation,
initialization and all memory/address operations are counted. Together with
Sections 3-4 they bound one source extraction by O(n^(5/4)) logical operations.

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

## 7. Complete charged resources and what improves

The source extractor's O(n^(5/4)) logical operations each pay the full
O(A_addr^2)=O(n) streamed address/generation allowance. Thus each acquired
source costs O(n^(9/4)) charged work. Across R=O(nL_0) sources this is
O(n^(13/4)L_0). The one-time reciprocal and fixed interpolation constants,
parameter schedule, initialization, fixed rational tables and gradient
preparation all fit this envelope, with absolute outer constants.

Stable bucket sorting and ordinary pair arithmetic have O(n) logical bit
work per record and full O(n) charged work per logical operation, hence
O(n^2) charged work per record. Summing stage quotas and batches gives
O(n^3 L_0). Each rational-sampler trial likewise costs O(n^2) charged work,
but the total trial cap is now 4R=O(nL_0). Their entire worst-case cost is
O(n^3 L_0), including every failed draw. Thus the old extra square-root
factor from a separate worst-case cap at every coin has been removed by an
explicit globally bounded program and its probability argument.

Final verification costs O(n^3 L_0), and all remaining operations fit the
source envelope. Therefore on every branch of the one PG4 configuration,

    T=O(n^(13/4)L_0)=O(n^(15/4) 2^((244949/100000)sqrt(n))).

Peak quantum scratch is polynomial O(n^(5/4)), plus O(n) source/gradient
registers, and is O(L_0). Classical scratch, stored generated constants,
recursion/controller state and records fit O(nL_0). The memory envelopes
remain O(n^(3/2)2^(c sqrt n)) classical and O(sqrt n 2^(c sqrt n)) quantum.
Allocated memory is still O(nL_0), so the same O(sqrt n) address length is
justified before charging operations. Every acquisition remains counted by
the unchanged exact sample bound. No source copies are acquired by the
new preprocessing, arithmetic, Fourier circuit or sampler. The finite
n<=16 branch remains the original exhaustive verifier and runs none of
this preprocessing. Absolute constants cover that finite set.

The time polynomial is now 15/4, compared with PG3's 4 and PG2's 9/2.
The index remains exactly 1/2 and the explicit exponential coefficient is
unchanged. This is a smaller joint upper guarantee for a specified program,
not an optimality result or a matching lower bound. The construction directly
reuses the previous PG3/PG2 gradient and sieve framework, with the retained
MDC1/VFD3 foundation attribution in proof.md. Fast polynomial interpolation
and Fourier factorization are standard identities; every required identity,
constant-generation schedule, reversible implementation and error bound is
provided above, so no external oracle or inaccessible theorem is a premise.
