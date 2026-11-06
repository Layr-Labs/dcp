# SLS: spliced low-bit sieve, polynomial space, O(n) qubits, 2^{2√(n log n)+(9/4)√n}·poly(n) work

This file is the complete proof of all five claims in `submission.json`. It describes one
algorithm, **SLS**, with one fixed parameter rule, and proves for every integer N ≥ 2 and every
s ∈ Z/NZ, with n = ceil(log₂ N) and L = log₂ n:

* the output equals s with unconditional probability > 3/4 (≥ 2/3);
* total work T = O(2^{2√(nL) + (9/4)√n} n^{11/2} L^{3/2});
* peak classical space S_C = O(n²) bits;
* peak quantum space S_Q = O(n) qubits;
* acquired source copies Q = O(2^{√(nL) + 2√n} n⁴), counting every copy on every branch;
* fractional error tolerance 0 (all copies are independent ideal coset states).

All constants are absolute. Every loop is capped by a budget fixed by n and N, so the four
resource bounds hold on every execution branch. Logarithms are base 2 unless written ln. Nothing
outside this file is relied on; Section 10 credits the ideas we build on.

**Idea.** (i) *Splice.* Subtract a guess g from the secret. A copy whose hidden x satisfies
x + (s − g) < N then has integer difference s' = (s − g) mod N between its branches, so it can
be read as a coset state of the cyclic group Z/2^tZ. This happens unless the copy "wraps", which
it does with probability s'/N. One of G grid guesses makes s'/N < 2/G. (ii) *Exact labels without a
QFT.* After a uniformly random shift mod 2^t the copy is exactly the Z/2^tZ coset state. Its Fourier
label is read by phase-kickback tests that use only Clifford+T gates and fresh qubits, so no
rotation synthesis is needed. (iii) *Low-bit sieve.* Subset combinations of k = b'+3 labelled
qubits cancel b' low label bits with worst-case success ≥ 7/8. Depth-first evaluation keeps O(n)
qubits. A label 2^{t−1} reveals one bit of s'.

Notation. bitlength(x) is the number of binary digits of an integer x ≥ 1, so 2^{bitlength(x)} > x.
For a modulus M and an integer v, the *label-v qubit* for secret σ is
φ_σ(v) = (|0⟩ + e^{2πi vσ/M}|1⟩)/√2.

## 1. Exact primitives (Clifford+T, fresh |0⟩, computational-basis measurement)

Gates are X, CNOT, H, T, T† and Toffoli. Toffoli with controls a, b and target c is exactly
H(c), CX(b,c), T†(c), CX(a,c), T(c), CX(b,c), T†(c), CX(a,c), T(b), T(c), H(c), CX(a,b), T(a),
T†(b), CX(a,b). Only circuits built from X, CNOT and Toffoli are ever controlled. A source copy is
a first qubit c and an n-qubit register holding a value in [0, N) in binary.
A gate controlled by one extra qubit costs O(1) gates and one ancilla (X → CNOT; CNOT → Toffoli; Toffoli →
three Toffolis with one ancilla). Every released qubit is measured and, if its outcome is 1, reset
by X before reuse, so every "fresh" ancilla below is exactly |0⟩.

**A1 (constant adders and comparators).** For a classical constant a and a t-qubit register y:
(a) |y⟩|0^t⟩ ↦ |y⟩|(y + a) mod 2^t⟩ out of place: compute the carries of y + a into t ancillas
(carry_{i+1} = MAJ(y_i, a_i, carry_i), one Toffoli/CNOT/X group per bit, with a_i classical), write
the sum bits by CNOTs, then uncompute the carries by running the carry circuit backwards. The
carries depend only on y, so they return to 0. (b) The flag [y ≥ c] for a classical c is the carry
out of y + (2^t − c), computed and uncomputed the same way, for 1 ≤ c ≤ 2^t (c = 2^t gives carry 0, the constant 0); for c = 0 the flag
is the constant 1 (an X gate). Equality [y = c] is [y ≥ c] ∧ ¬[y ≥ c+1] (with [y ≥ 2^t] = 0).
All use O(t) gates and O(t) ancillas, all returned to |0⟩.

**A2 (in-place permutations).** Let π be a permutation of [0, 2^t) such that π and π^{−1} have
out-of-place XOR circuits C_π: |y⟩|w⟩ ↦ |y⟩|w ⊕ π(y)⟩ and C_{π^{-1}}. Then C_π, followed by
C_{π^{-1}} with the roles of the two registers exchanged (this maps |y⟩|π(y)⟩ to
|y ⊕ π^{−1}(π(y))⟩|π(y)⟩ = |0⟩|π(y)⟩), followed by relabelling the wires, implements |y⟩ ↦ |π(y)⟩
exactly with clean ancillas.

* **Add mod 2^t:** π(y) = (y + a) mod 2^t, π^{−1} = add 2^t − a. O(t) gates by A1(a).
* **Add mod N (P1):** for 0 ≤ a < N on n qubits, π(y) = (y + a) mod N if y < N, and y if
  y ≥ N. Out of place: compute e = [y < N] and f = [y ≥ N − a] (A1(b)); controlled on e, add the
  constant a if f = 0, or a − N + 2^n if f = 1, into the output (two controlled A1(a) circuits);
  if e = 0, copy y; uncompute f and e. π^{−1} is the same circuit with a replaced by (N − a) mod N.
  O(n) gates and ancillas.

**Controlled versions.** Relabelling wires cannot be controlled, so a controlled in-place π is
obtained by applying A2 to the permutation π_c(c, y) = (c, π(y)) if c = 1 and (c, y) if c = 0 of
the control together with the register. Its out-of-place circuit runs C_π with every gate controlled
by c (on c = 0 its ancillas are never touched, on c = 1 they are returned to 0), then copies y into
the output by CNOTs controlled by ¬c (X on c, Toffolis, X on c); its inverse is π_c^{−1} = (π^{−1})_c,
built the same way. The final relabelling is then unconditional. Here c is shared, not copied: the out-of-place circuit maps |c⟩|y⟩|w⟩ ↦ |c⟩|y⟩|w ⊕ y′⟩ with y′ = π(y) if c = 1 and y′ = y if c = 0; the reverse step applies the circuit of (π^{−1})_c, controlled by c itself, from w into y; only the y and w wires are relabelled. The size stays O(t) gates and O(t)
ancillas. A uniform generator emits these gate lists one gate at a time in O(n) bit operations from
a, N, t.

**A3 (phase test).** For a qubit (|0⟩ + e^{2πiθ}|1⟩)/√2 and m′ ∈ {0,…,7}, apply (T†)^{m′}, then H,
then measure. Outcome 0 has probability exactly p_{m′}(θ) = (1 + cos 2π(θ − m′/8))/2.

**A4 (fair bits).** A fresh |0⟩, H, measurement: one exact fair bit, O(1) work.

**Cost convention.** Let 𝔐 be the number of allocated bits plus qubits. Section 7 shows 𝔐 = O(n²),
so a classically indexed access or classically addressed gate costs A = ceil(log₂(𝔐+2)) = O(log n)
bit operations for its address. Every gate, measurement, initialisation and classical bit operation
below is charged O(A).

## 2. Coset states of Z/MZ as labelled qubits

For a modulus M and σ ∈ Z/MZ let ρ^M_σ = (1/M) Σ_{z<M} |ψ_z⟩⟨ψ_z|, ψ_z = (|0,z⟩ + |1,(z+σ) mod M⟩)/√2.
With χ_k = M^{−1/2} Σ_y e^{2πiky/M}|y⟩ we have |y⟩ = M^{−1/2} Σ_k e^{−2πiky/M} χ_k, so
ψ_z = (2M)^{−1/2} Σ_k e^{−2πikz/M}(|0⟩ + e^{−2πikσ/M}|1⟩) ⊗ χ_k. Averaging over z removes the
cross terms k ≠ k′, and with u = −k mod M

  ρ^M_σ = (1/M) Σ_{u ∈ Z/MZ} |φ_σ(u)⟩⟨φ_σ(u)| ⊗ |χ_{−u}⟩⟨χ_{−u}|.                     (2.1)

So ρ^M_σ is exactly a uniformly random classical label u together with the product state
φ_σ(u) ⊗ χ_{−u}. If g_a|y⟩ = |(y + a) mod M⟩, then g_a χ_{−u} = e^{2πiua/M} χ_{−u}. Hence the
**kickback test** "fresh |0⟩, H, then g_a on the register controlled by this qubit" leaves the
register unchanged and puts the control qubit in (|0⟩ + e^{2πiua/M}|1⟩)/√2. Repeated tests on one
register are independent given u, and they never touch the first qubit.

## 3. Lemma P (label reading)

Let J, r ≥ 1. Suppose that for each level i ∈ {0,…,J} and each m′ ∈ {0,…,7} we obtain r independent
outcomes of A3 with this m′, applied to qubits (|0⟩ + e^{2πi 2^iθ}|1⟩)/√2 for an unknown real θ.
Let Z_{i,m′} be the number of 0 outcomes. Let m_i be the m′ maximising Z_{i,m′} (the smallest on
ties), β_i = m_i/8 and x_J = β_J. For i = J−1 down to 0, of c₀ = x_{i+1}/2 and
c₁ = x_{i+1}/2 + 1/2 let x_i be the one with smaller circular distance |c − β_i|∘ (c₀ on ties),
where |φ|∘ = min_{z∈Z}|φ − z|.

**Claim.** With probability ≥ 1 − 16(J+1)e^{−r/200}, |x₀ − θ|∘ < 2^{−J}/8.

*Proof.* Write θ_i = frac(2^iθ). By Hoeffding's inequality,
P(|Z_{i,m′}/r − p_{m′}(θ_i)| ≥ 1/20) ≤ 2e^{−2r/400}; a union bound over the 8(J+1) pairs gives the
failure bound. Assume all deviations are < 1/20. (a) The nearest grid point m*/8 has
|θ_i − m*/8|∘ ≤ 1/16, so p_{m*} ≥ (1 + cos(π/8))/2 > 0.9619, while every m′ with
|θ_i − m′/8|∘ ≥ 1/8 has p_{m′} ≤ (1 + cos(π/4))/2 < 0.8536. The gap exceeds 2/20, so
|β_i − θ_i|∘ < 1/8. (b) We show |x_i − θ_i|∘ < δ_i := 2^{−(J−i)}/8 by downward induction. The case
i = J is (a). Let |x_{i+1} − θ_{i+1}|∘ < δ_{i+1} ≤ 1/8 and write x_{i+1} − θ_{i+1} = e + z with
z ∈ Z and |e| < δ_{i+1}. Since θ_{i+1} = frac(2θ_i), θ_i ≡ θ_{i+1}/2 + w/2 (mod 1) for some
w ∈ {0,1}, and {c₀, c₁} ≡ {θ_{i+1}/2 + e/2, θ_{i+1}/2 + 1/2 + e/2} (mod 1). One candidate is within
|e|/2 < δ_i of θ_i; the other is at distance > 1/2 − 1/16. By (a) the good one is within
1/16 + 1/8 = 3/16 of β_i and the bad one is farther than 1/2 − 1/16 − 1/8 = 5/16, so the good one
is chosen. ∎

All x_i are multiples of 2^{−(J+3)}, so the procedure is exact (J+3)-bit integer arithmetic,
O(J²) bit operations, and is defined for every count vector.

**Procedure F_t** (label of a register holding a Z/2^tZ coset state). Let M = 2^t,
J = max(1, t−2) and r = r₁ (Section 4). For each level i ∈ {0,…,J} and m′ ∈ {0,…,7}, perform r
kickback tests with a = 2^i mod M, each followed by A3 with this m′ on its control. Apply Lemma P
and output û = round(M x₀) mod M, where round(z) = floor(z + 1/2).

**Corollary F.** If the register is χ_{−u}, then û = u with probability ≥ 1 − 16(J+1)e^{−r/200}.
*Proof.* The test controls are the qubits of Lemma P with θ = u/M (Section 2). We have M ≤ 2^{J+2}:
for t ≥ 3, J + 2 = t; for t ≤ 2, M ≤ 4 < 8. On the success event, M x₀ differs from u + Mz by less
than M 2^{−J}/8 ≤ 1/2, so the rounding returns u, with no tie. ∎

## 4. Parameters (exact integer arithmetic, computed from n only)

* λ = max(1, ceil(log₂ n)) (= bitlength(n−1) for n ≥ 2); **b** = ceil(√(nλ)), the least integer
  with b² ≥ nλ.
* **D** = ceil((n−1)/b) (D = 0 for n = 1); γ = 8(b+3)/7 (a rational number).
* **B** = ceil(20 n γ^D): the copy budget of one inner run.
* **G** = 40B; G′ = min(G, N); grid points g_i = floor(iN/G′) for i = 0,…,G′−1.
* k_test = bitlength(G′) + 4; L₁ = bitlength(1600(n+1)B); **r₁** = 200 L₁.
* For each t ∈ {1,…,n}: m_t = ceil((t−1)/b) (0 for t = 1); stage boundaries l_s = min(sb, t−1)
  for s = 0,…,m_t; stage widths b_s = l_s − l_{s−1} ≥ 1; arities k_s = b_s + 3 ≤ b + 3.

γ^D is a ratio of two integers with O(D log b) bits, so all parameters cost poly(n) bit operations.

## 5. Algorithm SLS

**Outer loop.** For i = 0,…,G′−1: run INNER(g_i). If it returns σ ∈ [0, N), run
TEST((σ + g_i) mod N). If TEST accepts, output that value and halt. If no candidate is accepted,
output 0.

**TEST(v)** (k_test copies). For each copy: controlled on the first qubit, apply P1 with
a = (N − v) mod N to the register (subtracting v); apply H to the first qubit and measure it.
Accept iff all k_test outcomes are 0.

**INNER(g)** keeps a counter of acquired copies. Whenever a copy is needed and the counter equals B,
INNER aborts: it measures and releases all its qubits and returns "abort". Otherwise it sets
σ_low = 0 and, for j = 0,…,n−1 with t = n − j:

* repeat PRODUCE_t(m_t) until it returns a qubit of label exactly 2^{t−1} (a returned qubit with
  label 0 is measured and discarded); apply H to that qubit and measure it, giving the bit o_j;
* σ_low ← σ_low + 2^j o_j.

It returns σ = σ_low.

**LEAF_t** (one copy; t = n − j, uses the current g and σ_low). Acquire a copy (first qubit c,
n-qubit register).
1. Controlled on c, apply P1 with a = (N − g) mod N (subtract g mod N).
2. Controlled on c, add (2^n − σ_low) mod 2^n to the register (A2, mod 2^n).
3. Measure the low j register qubits and release them. Call the remaining t qubits the register.
4. Draw t fair bits (A4) forming ζ ∈ [0, 2^t); add ζ mod 2^t to the register (A2, uncontrolled);
   then erase ζ (no later step reads it, or the outcomes of step 3).
5. Run F_t on the register, giving û; measure and release the register.

Return the qubit c with label û.

**PRODUCE_t(s).** If s = 0, return LEAF_t. Otherwise repeat: obtain q_1,…,q_k (k = k_s) by k
sequential calls PRODUCE_t(s−1), holding the finished outputs; run COMBINE(q_1..q_k; l_{s−1} → l_s);
on success return its output, on failure start the next repetition.

**COMBINE.** The inputs have labels x_1,…,x_k ∈ [0, 2^t), all ≡ 0 mod 2^l. Let l′ be the target,
b′ = l′ − l, k = b′ + 3, w_i = x_i/2^l and d(z) = Σ_i z_i w_i mod 2^{b′} for z ∈ {0,1}^k, ordered
as k-bit integers. Write y for the k input qubits read in the computational basis.
1. For each i, controlled on y_i, add w_i mod 2^{b′} into a fresh b′-qubit register (A2, mod 2^{b′}).
   Measure that register, giving d, and release it. Let C_d = {z : d(z) = d}; compute |C_d| by
   classical enumeration of {0,1}^k.
2. Rank sweep: for each z ∈ C_d in increasing order (classical enumeration of {0,1}^k), compute the
   flag [y > z] into an ancilla (A1(b)), add it into a (k+1)-qubit counter by a controlled
   increment (O(k) gates), and uncompute the flag. The counter now holds the rank
   rk(y) = #{z ∈ C_d : z < y}. Copy floor(rk/2) into a fresh (k)-qubit output register by CNOTs, and
   compute into a fresh flag qubit the bit [rk = |C_d| − 1 and |C_d| odd] (A1(b) twice; constant 0
   if |C_d| is even). Run the sweep backwards to return the counter to 0. Measure the output
   register and the flag, giving h and φ.
3. If φ = 1, fail: measure and release the k qubits.
4. Otherwise let z⁰ < z¹ be the elements of C_d of ranks 2h and 2h+1 (by classical enumeration).
   Pick the least i₀ with z⁰_{i₀} ≠ z¹_{i₀}, and name the pair (z⁻, z⁺) so that z⁺_{i₀} = 1. Apply
   CNOT(i₀ → j) for every j ≠ i₀ with z⁻_j ≠ z⁺_j, then X on every j ≠ i₀ with z⁻_j = 1; measure and
   release all qubits except i₀. Return qubit i₀ with label x′ = Σ_i (z⁺_i − z⁻_i) x_i mod 2^t.

## 6. Correctness

**Lemma W (splice).** Fix g and let s′ = (s − g) mod N. After step 1 a copy of ρ_s is the uniform
mixture over x ∈ [0, N) of (|0,x⟩ + |1,(x + s′) mod N⟩)/√2 (since (x + s − g) mod N =
(x + s′) mod N). Hence ρ_s = (1 − p) ρ^{nw} + p ρ^{w} with p = s′/N, where ρ^{nw} (resp. ρ^{w}) is
the uniform mixture of the source's pure states over x < N − s′ (resp. x ≥ N − s′). For x < N − s′
the second branch holds the integer x + s′ < N. The grid contains some g* with s′ < N/G′ + 1. If
G′ = N then g_i = i and s′ = 0 for i = s; otherwise N > G and p < 1/G + 1/N < 2/G.

*Proof of the grid claim.* With g_{G′} := N, s lies in some [g_i, g_{i+1}), and
g_{i+1} − g_i < N/G′ + 1. ∎

**Lemma S (exact leaf).** Fix g, j, t = n − j, and suppose σ_low = s′ mod 2^j. Let σ_hi =
floor(s′/2^j). Feed LEAF_t a copy from ρ^{nw}. Conditionally on the outcomes of step 3, and with ζ
not recorded, the state of (c, register) after step 4 is exactly ρ^{2^t}_{σ_hi}.

*Proof.* Fix x < N − s′. After step 2 the state is |0,x⟩ + |1, x + s′ − σ_low⟩ (normalised), where
s′ − σ_low = 2^j σ_hi ≥ 0 and x + s′ − σ_low < N ≤ 2^n, so the mod-2^n addition does not wrap.
Both branches share the low j bits x mod 2^j, so step 3 leaves |0, x_h⟩ + |1, x_h + σ_hi⟩ with
x_h = floor(x/2^j) and x_h + σ_hi < 2^t. For each fixed x_h, averaging step 4 over uniform ζ gives
(1/2^t) Σ_z |ψ_z⟩⟨ψ_z| with ψ_z = (|0,z⟩ + |1,(z + σ_hi) mod 2^t⟩)/√2, which is ρ^{2^t}_{σ_hi}.
Conditionally on the step-3 outcome, the state is a mixture of such x_h-states, so it equals
ρ^{2^t}_{σ_hi}. No later step reads ζ or the step-3 outcome, so by linearity the law of everything
that follows is the one obtained from this averaged state. ∎

By (2.1), such a leaf is a uniform label u ∈ Z/2^tZ with c in the state φ_{σ_hi}(u) and the register
in χ_{−u}. F_t touches only the register and fresh qubits, so after LEAF_t, c is still φ_{σ_hi}(u),
in product with everything else given u, and by Corollary F with r = r₁
P(û ≠ u | u, past) ≤ 16(n+1)e^{−L₁} < 16(n+1)/2^{L₁} < 1/(100B).

**The genie run.** Fix the good guess g*. The *genie run* is a modified process (not an event; no
conditioning is applied): INNER(g*) in which (a) every acquired copy is drawn from ρ^{nw}, and
(b) the output of each F_t is replaced by the true label u of the leaf (F's tests are still
performed and their outcomes ignored). Lemmas H and E concern the genie run *without* the cap B;
the capped and uncapped versions agree until the cap is reached. In the genie run every qubit held
is an exact labelled qubit φ_σ(x) for the current σ = σ_hi, with known label x, in product with
all other systems. (On every branch of the real algorithm, whatever the labels, the classical update
x′ = Σ(z⁺ − z⁻)_i x_i keeps every recorded label ≡ 0 mod 2^{l_s} after stage s, so COMBINE is
always well defined, and a final with any label other than 2^{t−1} is discarded.)

**Lemma C (COMBINE).** Let the k inputs be labelled qubits φ_σ(x_i) for one σ, with
x_i ≡ 0 mod 2^l, in product with everything else. Then:
(i) the outcome law is a fixed kernel K(d, h, φ | x mod 2^{l′}): P(d) = |C_d|/2^k; given d, the
rank rk(y) is uniform on {0,…,|C_d| − 1};
(ii) P(fail) = Σ_d [|C_d| odd]/2^k ≤ 2^{b′}/2^k = 1/8;
(iii) on success the output is exactly φ_σ(x′), in product with everything else, and
x′ ≡ 0 mod 2^{l′}.

*Proof.* The joint input state is 2^{−k/2} Σ_y e^{2πiσ(y·x)/2^t}|y⟩. Step 1 entangles y with d(y)
and measures d, so P(d) = |C_d|/2^k and the state becomes |C_d|^{−1/2} Σ_{y∈C_d} e^{iθ(y)}|y⟩,
θ(y) = 2πσ(y·x)/2^t. Since d(z) depends only on w mod 2^{b′}, that is on x mod 2^{l′}, so do C_d and
all further outcome laws. The counter holds rk(y) for each basis state, so step 2 measures
(floor(rk/2), [rk = |C_d| − 1, |C_d| odd]) of a uniformly weighted superposition and then returns
the counter to 0 exactly. This gives (i). The flag is 1 exactly for the single last element of each
odd class, so P(fail) = Σ_d [|C_d| odd]/2^k. At most 2^{b′} values of d occur and k = b′ + 3,
giving (ii). On φ = 0 the state is (e^{iθ(z⁻)}|z⁻⟩ + e^{iθ(z⁺)}|z⁺⟩)/√2. The CNOTs controlled by
i₀ fix z⁻ (z⁻_{i₀} = 0) and turn z⁺ into z⁻ off i₀; the X gates then clear every qubit j ≠ i₀. What
remains is qubit i₀ in (|0⟩ + e^{i(θ(z⁺) − θ(z⁻))}|1⟩)/√2 = φ_σ(x′). Finally
(z⁺ − z⁻)·w ≡ d − d ≡ 0 (mod 2^{b′}), so x′ = 2^l (z⁺ − z⁻)·w ≡ 0 (mod 2^{l+b′}). ∎

So in the genie run every output of PRODUCE_t(s) has label ≡ 0 mod 2^{l_s}. The final stage has
l_{m_t} = t − 1, so final labels lie in {0, 2^{t−1}} (for t = 1, m_1 = 0 and labels lie in {0,1}).
A final qubit with label 2^{t−1} is (|0⟩ + (−1)^{σ_hi}|1⟩)/√2, and H then measurement returns
σ_hi mod 2, which is bit j of s′, with certainty.

**Lemma H (top bit).** In the genie run, conditionally on everything that happened before a call
of PRODUCE_t(m_t), its output label equals 2^{t−1} with probability exactly 1/2.

*Proof.* Realise the call on a probability space carrying, for its leaves in order of acquisition,
iid uniform labels u_κ = a_κ + 2^{t−1}τ_κ (a_κ < 2^{t−1}, τ_κ ∈ {0,1}), independent of the past.
Realise each COMBINE outcome from fresh independent uniforms through the kernel K of Lemma C(i).
F's own outcomes do not influence the genie run. Since every l′ ≤ t − 1, every kernel depends only
on the labels mod 2^{t−1}, which are integer combinations of the a_κ. Hence the transcript, the set
of leaves used, and the coefficient vector c ∈ {−1,0,1}^𝒦 (𝒦 the set of leaves of the call) with output label Σ c_κ u_κ mod 2^t
(by induction from x′ = Σ(z⁺ − z⁻)_i x_i) are all functions of (a, uniforms), which are independent
of τ. The vector c ≠ 0: at each node z⁺ ≠ z⁻, and distinct inputs have disjoint leaf sets. Since the
output is ≡ 0 mod 2^{t−1}, Σ c_κ a_κ = 2^{t−1}e for an integer e determined by (a, uniforms), and
the top bit is e + Σ_{c_κ≠0} τ_κ mod 2, which is uniform given (a, uniforms). ∎

**Lemma E (expected copies).** In the genie run, for every past, a call of PRODUCE_t(s) uses in
expectation at most V_s = Π_{i=1}^{s} (8k_i/7) leaves. Each bit uses at most 2V_{m_t} in
expectation, and INNER(g*) uses at most E = Σ_{t=1}^{n} 2V_{m_t} ≤ 2nγ^D ≤ B/10 copies in
expectation.

*Proof.* Induction on s, with V_0 = 1. Let A be the number of repetitions, Y_{a,i} the leaves of the
i-th subcall in repetition a, and H_{a,i} the past before that subcall. The event {A ≥ a} is fixed
before repetition a starts, and P(A ≥ a | past) ≤ 8^{−(a−1)} by Lemma C(ii), which holds whatever
the input labels are. So E[Σ_a Σ_i Y_{a,i}1{A≥a}] = Σ_a Σ_i E[1{A≥a} E[Y_{a,i} | H_{a,i}]]
≤ k_s V_{s−1} Σ_{a≥1} 8^{−(a−1)} = (8k_s/7)V_{s−1}. The bit loop is the same argument with
success probability 1/2 (Lemma H), giving 2V_{m_t}. Also k_i ≤ b + 3 and m_t ≤ D, so
V_{m_t} ≤ γ^D, and B ≥ 20nγ^D. ∎

**Lemma I (inner run).** P(INNER(g*) returns s′) ≥ 1 − 1/10 − 1/20 − 1/100.

*Proof.* (Genie.) By induction on j, the genie run has σ_low = s′ mod 2^j before bit j (each bit is
read with certainty, as shown after Lemma C), so it outputs s′ unless it needs more than B copies.
By Markov's inequality and Lemma E that has probability ≤ E/(B+1) < 1/10.
(Coupling.) Write each acquired copy as ρ^{nw} or ρ^{w} by an independent coin W with
P(W = 1) = p (Lemma W); this is the same state. For a leaf from ρ^{nw}, write the prepared state as
its uniform label u with φ(u) ⊗ χ_{−u} (Lemma S and (2.1)); since F_t acts only on the register,
which is in the eigenstate χ_{−u}, u is a well-defined classical random variable of the real run.
Realise all later measurement outcomes of the real run and of the genie run from one common
sequence of independent uniforms, through their conditional laws given the past. The two runs then
have the same history and the same quantum state up to the first copy with W = 1 or the first leaf
with û ≠ u. Let bad_i be the event that the i-th acquired copy has W = 1 or (as a leaf) û ≠ u.
INNER acquires at most B copies, and P(bad_i | past before copy i) ≤ p + 1/(100B) on the event that
copy i is acquired, so P(∪_i bad_i) ≤ Σ_{i≤B} E[1{copy i acquired}·P(bad_i | past)] ≤
B(p + 1/(100B)) < 2B/G + 1/100 = 1/20 + 1/100 (using p < 2/G, or p = 0, from Lemma W). ∎

**Lemma T (test).** TEST(s) accepts with certainty, and for v ≠ s TEST(v) accepts with probability
exactly 2^{−k_test}, whatever happened before.

*Proof.* After the controlled subtraction of v a fresh copy is the mixture over x of
(|0,x⟩ + |1,(x + s − v) mod N⟩)/√2. If v = s, c is |+⟩ and H gives 0. If v ≠ s, the two register
values differ, so c is maximally mixed and outcome 0 has probability 1/2. The copies are fresh and
independent. ∎

**Theorem 1.** For every N ≥ 2 and s, SLS outputs s with probability > 3/4.

*Proof.* Some wrong candidate is accepted with probability at most G′ 2^{−k_test} < 1/16, since
2^{bitlength(G′)} > G′. If none is, SLS outputs s whenever INNER(g*) returns s′, because then the
candidate (s′ + g*) mod N = s is tested and accepted (Lemma T). An earlier correct acceptance also
outputs s. So P(failure) ≤ 1/16 + 1/10 + 1/20 + 1/100 = 0.2225 < 1/4. ∎

## 7. Resources (every branch)

**Copies.** INNER uses at most B copies (hard cap) and TEST k_test, over G′ ≤ G guesses:
Q ≤ G′(B + k_test) ≤ 40B(B + k_test) ≤ 80B², since k_test ≤ bitlength(40B) + 4 ≤ B.

**Bounding B (n ≥ 16).** Then λ = ceil(L) ≥ 4, L ≤ λ < L + 1, and √(nλ) ≥ 8, so
b + 3 ≤ √(nλ) + 4 ≤ (3/2)√(nλ) and log₂ γ ≤ log₂(12/7) + (L + log₂ λ)/2 with log₂(12/7) < 0.778.
Also D < (n−1)/b + 1 ≤ √(n/λ) + 1. Hence

D log₂ γ < √(n/λ)·L/2 + √n·(log₂ λ/2 + 0.778)/√λ + (L + log₂ λ)/2 + 0.778.

The first term is ≤ √(nL)/2 because λ ≥ L. In the second, (log₂ λ/2 + 0.778)/√λ ≤ 0.89 < 1 for every
real λ ≥ 4 (it equals 0.889 at λ = 4 and decreases, since its derivative has the sign of
1/ln 2 − log₂ λ/2 − 0.778 < 0 for λ ≥ 4). Since 20nγ^D ≥ 20, B ≤ 21nγ^D, and with log₂ 21 < 4.4
and log₂ λ ≤ L,

  **log₂ B < √(nL)/2 + √n + 2L + 6**   (n ≥ 16).                                       (7.1)

Similarly b ≤ √(nλ) + 1 ≤ √(nL + n) + 1 ≤ √(nL) + √n/(2√L) + 1 ≤ √(nL) + √n/4 + 1.    (7.2)

**Quantum space.** In INNER, depth-first evaluation holds at most k_s − 1 finished outputs per
stage while a subcall runs, plus one more during the COMBINE of a stage, so at most
Σ_s (k_s − 1) + 1 ≤ (t − 1) + 2m_t + 1 ≤ n + 2D qubits are held. In addition there are: one copy
being prepared (n + 1 qubits); the O(n) ancillas of A1/A2; one test control and one A4 qubit; and
the COMBINE workspace (b′ + (k+1) + k + 1 + O(k) = O(b) qubits). TEST uses one copy and O(n)
ancillas. All measured qubits are released. **S_Q ≤ 2n + 2D + O(n) + O(b) = O(n).**

**Classical space.** Labels of held qubits: ≤ (n + 2D)·n = n² + 2Dn bits, and 2Dn = O(n^{3/2}).
Parameters N, n, λ, b, D, B, G, G′, k_test, L₁, r₁, g_i, σ_low, the copy counter and the
candidate: O(D log n + n) bits, plus the O(D log b)-bit numerator and denominator of γ^D during
its computation. F_t: 8(J+1) counters of bitlength(r₁) = O(log n) bits, the 3-bit values m_i, and
one (J+3)-bit x_i: O(n log n). Recursion stack: the repetition counter (≤ B) and subcall index per
stage: O(D log B) = O(n). COMBINE: the k values w_i mod 2^{b′}, the current z, d, |C_d|, h, z⁻, z⁺:
O(kb + k) = O(n log n). Gate lists are emitted one gate at a time, and a gate description
(O(log 𝔐) bits) is the only one stored. **S_C ≤ n² + 2Dn + O(n log n) = O(n²).** Hence
𝔐 = O(n²) and A = O(log n).

**Work.** Every operation is charged O(A) = O(log n).
* Parameters: poly(n) bit operations; each grid point g_i = floor(iN/G′): O(n²).
* One leaf: acquisition n + 1; steps 1–4: O(n) gates. F_t: 8(J+1)r₁ tests of O(n) gates each.
  Here r₁ = 200L₁ and, by (7.1), L₁ ≤ log₂ B + log₂(1600(n+1)) + 1 = O(√(nL)), so F_t costs
  O(n·√(nL)·n) operations, plus O(n²) for Lemma P and the rounding. So C_leaf = O(n^{5/2} L^{3/2})
  after the A factor.
* One COMBINE (k ≤ b + 3, b′ ≤ b): at most four classical enumerations of {0,1}^k, each computing
  d(z) in O(kb′) bit operations; at most 2^k sweep elements of O(k) gates, run twice; O(kb′) gates
  in step 1; O(k) in step 4. So C_comb = O(2^b b² L).
* Number of COMBINE attempts per INNER: for each stage index s, the attempts at index s (over all
  bits j) consume disjoint sets of earlier outputs, each of which used at least one leaf, so there
  are ≤ B of them, and ≤ DB in total.
* Per INNER: ≤ B(C_leaf + D·C_comb) + O(BnL) for the bit loop (≤ B finals, each checked and
  discarded in O(n) operations). TEST: k_test(n + 1 + O(nL)).

Over G′ ≤ 40B guesses,
T ≤ 40B·[B·C_leaf + DB·C_comb + O(BnL + n²L) + k_test·O(nL)] + poly(n)
  = O(B²(n^{5/2}L^{3/2} + D 2^b b² L)).
By (7.2), D b² L ≤ (2√(n/λ))(4nλ)L = O(n^{3/2}L^{3/2}) and 2^b = O(2^{√(nL) + √n/4}). For n ≥ 16,
b ≥ √(nL) ≥ (3/2)L, so 2^b ≥ n^{3/2}, and with b² ≥ nL this gives C_leaf = O(D 2^b b² L): the leaf
term is dominated. By (7.1),

T = O(2^{√(nL) + 2√n} n⁴ · 2^{√(nL) + √n/4} n^{3/2} L^{3/2}) = **O(2^{2√(nL) + (9/4)√n} n^{11/2} L^{3/2})**,

and from Q ≤ 80B² and (7.1), **Q = O(2^{√(nL) + 2√n} n⁴)**. Instances with n < 16 are finitely many
values of N, each with finite cost, so they are absorbed into the constants. All four bounds hold
simultaneously on every execution branch of this one algorithm with this one parameter rule,
jointly with Theorem 1.

## 8. Exact growth indices and structured envelopes

For ℬ(n) = 2^{a√(nL) + c√n} n^r L^q, with a > 0, c ≥ 0 and r, q ≥ 0 fixed:
log₂ ℬ = √n(a√L + c) + r log₂ n + q log₂ L, so log₂ log₂ ℬ / log₂ n = 1/2 + (log₂(a√L + c + o(1)))/log₂ n
→ 1/2, and g(ℬ) = 1/2. For ℬ = n^a (a > 0), g = 0. Outer constants do not change either value.

* T: ℬ_T(n) = 2^{2√(n log₂ n) + (9/4)√n} n^{11/2} (log₂ n)^{3/2}, index **1/2**. Exponent terms
  {coefficient 2, nPower 1/2, logPower 1/2} and {coefficient 9/4, nPower 1/2, logPower 0};
  nPower 11/2, logPower 3/2.
* S_C: ℬ = n², index **0**. S_Q: ℬ = n, index **0**.
* Q: ℬ = 2^{√(n log₂ n) + 2√n} n⁴, index **1/2**. Exponent terms {1, 1/2, 1/2} and {2, 1/2, 0};
  nPower 4, logPower 0.

Published time score: [1/2]. Like Regev's algorithm, SLS trades a √(log n) factor in the time
exponent for polynomial memory, compared with sieves whose memory is 2^{Θ(√n)}.

## 9. Fractional error tolerance

ε(n) = 0: at most floor(0·Q) = 0 acquired copies may be malformed. The guarantee assumes every
acquired copy is an independent ideal coset state ρ_s. No corruption model is assumed and no
behaviour is promised for malformed copies. Under this promise Theorem 1 holds for every N ≥ 2 and s
jointly with the bounds of Section 7. This is not a claim that positive tolerance is impossible.

## 10. Credits and what is new

The asymptotic class (time 2^{O(√(n log n))} with poly(n) space) is known: Regev
(quant-ph/0406151) for N = 2^n, and Childs–Jao–Soukharev (arXiv:1012.4019, Appendix A) for
general N. This submission claims no new complexity class. The combination of about b′ labelled
qubits through a measured low-bit sum with depth-first evaluation follows Regev; the low-bit pairing
follows the "lsbcomb" step of Childs–Jao–Soukharev; the splice of Z/NZ into a power-of-two problem
follows Kuperberg's spliced approximation (SIAM J. Comput. 35 (2005)); the uniform top bit follows
Kuperberg (arXiv:1112.3333). No cited result is used as a lemma: every step is proved above. The
contributions here are: (i) a self-contained Kitaev-style phase-estimation readout that uses only
Clifford+T gates together with a random shift, so no QFT or rotation synthesis is needed
(Lemma S, Corollary F); (ii) a pairing whose failure probability is at most 1/8 for every input;
(iii) a complete joint charge of all four resources in this cost model, with explicit exponent
constants, for every N.
