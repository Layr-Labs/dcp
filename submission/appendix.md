# Appendix to proof.md (RLS-G4M): reversible arithmetic, cosine table, oracle circuits, quantum search

This file is part of the proof of the claims in `submission.json`; proof.md refers to its sections as
App. A–F. App. E and F are proof.md's former Sections 1 and 3 (primitives A1–A5, Lemma P, F_t; from our SLS
59facd77 and OMX-ML 31c2d043), moved verbatim except cross-references. The material of App. A–D is taken from our
ROB-G2 entry (55a6ce76), with the search over a register of d
qubits (d = d₁, …, d₃ of proof.md, Section 4) in place of n qubits and with the label constants c_{j,i} of
proof.md Section 6.6. It uses the gates, the primitive P2 (= A3) and the fair bits of App. E.

## A. Further reversible arithmetic (exact)

All circuits below use X, CNOT and Toffoli
only, return every ancilla to |0⟩, and are emitted gate by gate by a uniform generator.
* *P3a (controlled constant addition mod 2^p, in place).* the controlled constant adder A2 (App. E) ("add mod 2^t" with t = p, controlled
  version) on a p-qubit register. O(p) gates, O(p) ancillas.
* *P3b (register adder mod 2^w, in place).* Out of place, |a⟩|b⟩|0⟩ ↦ |a⟩|b⟩|(a + b) mod 2^w⟩:
  compute the carries carry_{i+1} = MAJ(a_i, b_i, carry_i) into w ancillas by Toffoli/CNOT
  groups, write the sum bits by CNOTs, uncompute the carries by running the carry circuit
  backwards. Since the sum bits are written by CNOTs, the same circuit maps
  |a⟩|b⟩|y⟩ ↦ |a⟩|b⟩|y ⊕ ((a + b) mod 2^w)⟩ for every y. Subtraction b − a = b + (2^w − 1 − a) + 1
  mod 2^w uses X on every a wire (including padding wires) before and after, and carry_0 = 1. In place, b ← (b + a) mod 2^w: add out of place into a fresh
  register S, then XOR (S − a) mod 2^w (= b) into the old b register, which clears it, and
  relabel S as b (unconditionally; no control is needed here). b ← (b − a) mod 2^w is the same
  with the roles of addition and subtraction exchanged. If a has fewer than w wires, its
  missing high wires are fresh |0⟩ ancillas. O(w) gates, O(w) ancillas.
* *P3c (comparison with a classical constant).* For a w-qubit register y and a classical
  constant c ∈ [1, 2^w], the flag [y ≥ c] is the carry out of y + (2^w − c), computed into a
  fresh qubit and its carries uncomputed as in A1(b) (App. E). O(w) gates.
* *P3d (multi-controlled X).* C^m X (m ≥ 2 controls) by the standard Toffoli chain: m − 2
  ancillas hold the partial ANDs, one Toffoli onto the target, and the chain is uncomputed.
  O(m) gates.
* *P3e (table read, QROM).* For a q-qubit index register k, a 27-qubit register v = |0⟩ and a
  classical table of 2^q words d_κ: for each κ = 0, …, 2^q − 1, apply X to the index wires where
  κ has a 0 bit, compute the AND of the q index wires into a fresh flag by P3d, apply CNOT from
  the flag to each wire of v at which d_κ has a 1 bit, uncompute the flag and undo the X gates.
  This maps |k⟩|v⟩ ↦ |k⟩|v ⊕ d_k⟩ on every basis state; applied twice it is the identity.
  O(2^q (q + 27)) gates (an absolute constant for fixed q) and O(q) ancillas.


## B. Cosine table

Let π̃ = 103993/33102. For k = 0, …, 2^q − 1: x̃_k = 2π̃k/2^q (exact rational),
P_k = Σ_{i=0}^{20} (−1)^i x̃_k^{2i}/(2i)! (exact rational arithmetic), and
c_k = round(2^{25} P_k) ∈ Z. Store c_k as a 27-bit two's-complement integer and
d_k = c_k + 2^{25} + 1 as a 27-bit unsigned integer.

**Lemma T.** |c_k/2^{25} − cos(2πk/2^q)| < τ_T = 2^{−24} for every k, hence
|c_k| ≤ 2^{25} < 2^{26} and 1 ≤ d_k ≤ 2^{26} + 1 < 2^{27}.

*Proof.* 3.1415926535 < π < 3.1415926536 (the standard decimal expansion of π, used here as a known
constant; it can be re-derived from Machin's formula π = 16 arctan(1/5) − 4 arctan(1/239) with
alternating-series remainders) and
3.1415926530 < π̃ < 3.1415926531 (long division), so |π − π̃| < 6·10^{−10}; with x_k = 2πk/2^q and
k < 2^q, |x_k − x̃_k| < 2·6·10^{−10} = 1.2·10^{−9}, and |cos x_k − cos x̃_k| < 1.2·10^{−9} (cos is
1-Lipschitz). Since 0 ≤ x̃_k < 2π̃ < 6.3 and |cos^{(42)}| ≤ 1, Taylor's theorem with Lagrange
remainder (P_k, of degree 40, is also the Taylor polynomial of degree 41, since the x^{41}
coefficient of cos is 0) gives |cos x̃_k − P_k| ≤ 6.3^{42}/42! < 3.8·10^{33}/(1.4·10^{51})
< 2.8·10^{−18}. Rounding adds at most 2^{−26} < 1.5·10^{−8}. Total
< 1.2·10^{−9} + 2.8·10^{−18} + 1.5·10^{−8} < 1.7·10^{−8} < 2^{−24}. For the range: |P_k| ≤ |cos x̃_k| +
2.8·10^{−18} < 1 + 2^{−26}, so −2^{25} − 1/2 < 2^{25}P_k < 2^{25} + 1/2, and round(z) = floor(z + 1/2) then lies in
[−2^{25}, 2^{25}]: |c_k| ≤ 2^{25}, hence 1 ≤ d_k = c_k + 2^{25} + 1 ≤ 2^{26} + 1. ∎

Write table[k] = c_k/2^{25}. The construction is a fixed finite computation on
rationals of fixed size: it uses an absolute constant number of bit operations
and bits.


## C. The circuits 𝒪 and 𝒟 for a search over d qubits

Fix a search with d qubits and K stored records (w_j, m′_j, b_j), j = 1, …, K, with w_j ∈ [0, 2^d)
(proof.md 6.6). The controller computes the constants c_{j,i} = floor(2^p frac(2^i w_j/2^d)) ∈ [0, 2^p) for
i = 0, …, d−1 (a shift and a mask of w_j: c_{j,i} = floor(w_j 2^{p+i−d}) mod 2^p), and w = bitlength(K) + 29.

**𝒟 (diffusion).** H on each of the d search qubits, then X on each, then the phase flip of |1^d⟩ (a fresh
target qubit is prepared in |1⟩, conjugated by H, and P3d with the d search qubits as controls is applied to
it; then the target is conjugated by H and reset — this multiplies |1^d⟩ by −1 and every other basis state
by 1), then X on each and H on each. As a matrix this is −(2|ψ₀⟩⟨ψ₀| − I) with ψ₀ = H^{⊗d}|0^d⟩; the global
sign −1 is irrelevant.

**𝒪_ι (phase oracle of threshold ι ∈ {1, …, 257}).** On the search register |τ⟩ (d qubits) and fresh ancillas:

1. *Accumulate.* A w-qubit register U starts at |0⟩. For j = 1, …, K:
   (a) V ← 0 (p fresh qubits); for i = 0, …, d − 1, controlled on τ_i, apply P3a with the classical constant
       c_{j,i}. Now V = V_j(τ).
   (b) k ← top q wires of V, copied by CNOTs into q fresh qubits; then P3a (uncontrolled; the control wire is a
       fresh qubit set to |1⟩ by X and reset afterwards) with the constant (2^q − 2^{q−3}m′_j) mod 2^q on k.
       Now k = k_j(τ).
   (c) v ← d_k by P3e (27 fresh qubits).
   (d) If b_j = 0, U ← (U + v) mod 2^w; if b_j = 1, U ← (U − v) mod 2^w (P3b; b_j is classical, so the
       controller chooses the circuit).
   (e) Uncompute (c), (b), (a) by applying their circuits in reverse order (P3e is its own inverse; the inverse
       of P3a with constant c is P3a with the constant (2^p − c) mod 2^p).
   After the loop U = (Σ_{j: b_j=0} d_{k_j(τ)} − Σ_{j: b_j=1} d_{k_j(τ)}) mod 2^w. Since
   Σ(τ) = Σ_j (−1)^{b_j}(d_{k_j(τ)} − 2^{25} − 1), the integer U* = Σ(τ) + (2^{25} + 1)(n₀ − n₁), with
   n₀ = #{j : b_j = 0} and n₁ = K − n₀, satisfies |U*| ≤ K(2^{26} + 1) < 2^{27}K < 2^{w−1} (as
   2^{w−1} = 2^{bitlength(K)+28} > 2^{28}K), so U holds U* in two's complement.
2. *Flag.* Classically let C*_ι = ι·2^{25}·K + 256(2^{25} + 1)(n₀ − n₁) and Θ_ι = floor(C*_ι/256); then
   256Σ(τ) > ι·2^{25}K ⇔ 256U* > C*_ι ⇔ U* > Θ_ι ⇔ U* ≥ Θ_ι + 1, and |Θ_ι + 1| ≤ |C*_ι|/256 + 2 ≤
   (257/256)2^{25}K + (2^{25} + 1)K + 2 < 2.01·2^{25}K + 2 < 2^{w−1}. Compute f_ι = [U* ≥ Θ_ι + 1] by flipping the top
   wire of U (X; this maps two's complement order to unsigned order, U* ↦ U* + 2^{w−1}), applying P3c with the constant
   Θ_ι + 1 + 2^{w−1} ∈ [1, 2^w) into a fresh qubit, and flipping the top wire back.
3. *Phase.* Apply Z (= T⁴) to the f_ι qubit.
4. *Clean up.* Uncompute f_ι by its circuit in reverse, then run step 1 in reverse (j = K, …, 1, each with the
   inverse operations), returning U and every ancilla to |0⟩.

Every operation in steps 1–2 is a permutation of computational basis states that leaves |τ⟩ unchanged and
computes f_ι(τ) = [256Σ(τ) > ι·2^{25}K] (equivalently S(τ) > ϑ_ιK with ϑ_ι = ι/256, S = Σ/2^{25}) exactly, so steps
1–4 implement 𝒪_ι = Σ_τ (−1)^{f_ι(τ)} |τ⟩⟨τ| ⊗ I on the ancillas (all returned to |0⟩).

## D. Quantum search

**Lemma G (one marked item).** Let d ≥ 1 and let f: [0, 2^d) → {0, 1} have exactly one w with f(w) = 1. Let
ψ₀ = H^{⊗d}|0^d⟩, 𝒪 = Σ_τ (−1)^{f(τ)}|τ⟩⟨τ| and 𝒟′ = 2|ψ₀⟩⟨ψ₀| − I, and let β ∈ (0, π/2] with sin β = 2^{−d/2}.
Then for every k ≥ 0, (𝒟′𝒪)^k ψ₀ = sin((2k+1)β)|w⟩ + cos((2k+1)β)|w̄⟩, where |w̄⟩ = (ψ₀ − sin β|w⟩)/cos β (for
d ≥ 1, cos β > 0) is a unit vector orthogonal to |w⟩, so measuring gives w with probability sin²((2k+1)β).

*Proof.* ψ₀ = cos β|w̄⟩ + sin β|w⟩ with |w̄⟩ the normalised uniform superposition of the 2^d − 1 unmarked basis
states. On the plane P = span{|w̄⟩, |w⟩}, 𝒪 is the reflection that fixes |w̄⟩ and negates |w⟩, and 𝒟′ is the
reflection that fixes ψ₀ and negates the unit vector of P orthogonal to ψ₀; both map P to itself. In the basis
(|w̄⟩, |w⟩), 𝒪 = diag(1, −1) and 𝒟′ = [[cos 2β, sin 2β], [sin 2β, −cos 2β]] (the reflection fixing
(cos β, sin β)), so 𝒟′𝒪 = [[cos 2β, −sin 2β], [sin 2β, cos 2β]], the rotation by 2β, which rotates ψ₀ (angle
β from |w̄⟩ towards |w⟩) to the angle (2k+1)β after k steps. ∎

The circuit 𝒟 equals −𝒟′, so 𝒢_ι^k = (−1)^k (𝒟′𝒪_ι)^k with 𝒢_ι = 𝒟𝒪_ι, and the measurement law is the same
(with f = f_ι).

**Lemma I (iteration count).** For d ≥ 4, k_G = floor(785K_G/1000) with K_G = floor(2^{d/2}) satisfies
π/4 < (2k_G + 1)β < 3π/4, so sin²((2k_G + 1)β) > 1/2.

*Proof.* Let x = 2^{−d/2} ≤ 1/4. Then x ≤ β = arcsin x ≤ x/√(1 − x²) ≤ x(1 + x²) ≤ (17/16)x, using
arcsin x = ∫₀^x dz/√(1 − z²) and (1 + x²)²(1 − x²) = 1 + x² − x⁴ − x⁶ ≥ 1 for x² ≤ 1/16. Also
1/x − 1 < K_G ≤ 1/x and 0.785K_G − 1 < k_G ≤ 0.785K_G. Upper: (2k_G + 1)β ≤ (1.57K_G + 1)(17/16)x ≤
(1.57 + x)(17/16) ≤ 1.82·1.0625 < 1.94 < 3π/4. Lower: (2k_G + 1)β ≥ (1.57K_G − 1)x > 1.57 − 2.57x ≥
1.57 − 0.6425 > 0.92 > π/4. On [π/4, 3π/4], sin² ≥ 1/2. ∎

## E. Exact primitives (proof.md Section 1)

Gates are X, CNOT, H, T, T† and Toffoli. Toffoli with controls a, b and target c is exactly
H(c), CX(b,c), T†(c), CX(a,c), T(c), CX(b,c), T†(c), CX(a,c), T(b), T(c), H(c), CX(a,b), T(a), T†(b),
CX(a,b). Only circuits built from X, CNOT and Toffoli are ever controlled. A source copy is a first
qubit c and an n-qubit register holding a value in [0, N) in binary. A gate controlled by one extra
qubit costs O(1) gates and one ancilla (X → CNOT; CNOT → Toffoli; Toffoli → three Toffolis with one
ancilla). Every released qubit is measured and, if its outcome is 1, reset by X before reuse, so every
"fresh" ancilla is exactly |0⟩.

**A1 (constant adders and comparators).** For a classical constant a and a t-qubit register y:
(a) |y⟩|0^t⟩ ↦ |y⟩|(y + a) mod 2^t⟩ out of place: compute the carries of y + a into t ancillas
(carry_{i+1} = MAJ(y_i, a_i, carry_i), one Toffoli/CNOT/X group per bit, a_i classical), write the sum
bits by CNOTs, then uncompute the carries by running the carry circuit backwards; the carries depend
only on y, so they return to 0. (b) The flag [y ≥ c] for a classical c is the carry out of y + (2^t − c),
computed and uncomputed the same way, for 1 ≤ c ≤ 2^t (c = 2^t gives the constant 0); for c = 0 it is
the constant 1. All use O(t) gates and O(t) ancillas, all returned to |0⟩.

**A2 (in-place permutations).** Let π be a permutation of [0, 2^t) such that π and π^{−1} have
out-of-place XOR circuits C_π: |y⟩|w⟩ ↦ |y⟩|w ⊕ π(y)⟩ and C_{π^{−1}}. Then C_π, followed by C_{π^{−1}}
with the roles of the two registers exchanged (|y⟩|π(y)⟩ ↦ |y ⊕ π^{−1}(π(y))⟩|π(y)⟩ = |0⟩|π(y)⟩),
followed by relabelling the wires, implements |y⟩ ↦ |π(y)⟩ exactly with clean ancillas.
* **Add mod 2^t:** π(y) = (y + a) mod 2^t, π^{−1} = add 2^t − a. O(t) gates by A1(a).
* **Add mod N (P1):** for 0 ≤ a < N on n qubits, π(y) = (y + a) mod N if y < N, and y if y ≥ N. Out
  of place: compute e = [y < N] and f = [y ≥ N − a] (A1(b)); controlled on e, add the constant a if
  f = 0, or a − N + 2^n if f = 1, into the output (two controlled A1(a) circuits); if e = 0, copy y;
  uncompute f and e. π^{−1} is the same circuit with a replaced by (N − a) mod N. O(n) gates and ancillas.

**Controlled versions.** Relabelling wires cannot be controlled, so a controlled in-place π is
obtained by applying A2 to the permutation π_c(c, y) = (c, π(y)) if c = 1 and (c, y) if c = 0 of the
control together with the register. Its out-of-place circuit runs C_π with every gate controlled by c
(on c = 0 its ancillas are never touched, on c = 1 they are returned to 0), then copies y into the
output by CNOTs controlled by ¬c; its inverse is (π^{−1})_c, built the same way. The final relabelling
is then unconditional, and c is shared, not copied. The size stays O(t) gates and O(t) ancillas. A
uniform generator emits these gate lists one gate at a time: each next gate's type and wire indices follow
from the previous ones by O(1) amortized counter and offset updates (O(n) bit operations per list of O(n)
gates), so generation adds O(1) bit operations per gate, which the address charge A (proof.md Section 1) per gate dominates.

**A3 (phase test).** For a qubit (|0⟩ + e^{2πiθ}|1⟩)/√2 and m′ ∈ {0,…,7}, apply (T†)^{m′}, then H,
then measure. Outcome 0 has probability exactly p_{m′}(θ) = (1 + cos 2π(θ − m′/8))/2.

**A4 (fair bits).** A fresh |0⟩, H, measurement: one exact fair bit, O(1) work.

**A5 (combination).** Given qubits a, b, apply CNOT (control a, target b) and measure b. If a and b
are label-v₁ and label-v₂ qubits φ_σ(v₁), φ_σ(v₂) in a product state, with α_i = 2πv_iσ/M′, the state
before the measurement is (|00⟩ + e^{iα₂}|01⟩ + e^{iα₁}|11⟩ + e^{i(α₁+α₂)}|10⟩)/2. Outcome 0
(probability exactly 1/2) leaves a in φ_σ(v₁ + v₂); outcome 1 (probability exactly 1/2) leaves a in
(e^{iα₂}|0⟩ + e^{iα₁}|1⟩)/√2, which is φ_σ(v₁ − v₂) up to a global phase.

## F. Lemma P (label reading) and procedure F_t (proof.md Section 3)

**Lemma P.** Let J, r ≥ 1. Suppose that for each level i ∈ {0,…,J} and each m′ ∈ {0,…,7} we obtain r
independent outcomes of A3 with this m′, applied to qubits (|0⟩ + e^{2πi2^iθ}|1⟩)/√2 for an unknown
real θ. Let Z_{i,m′} be the number of 0 outcomes, m_i the m′ maximising Z_{i,m′} (the smallest on ties),
β_i = m_i/8 and x_J = β_J. For i = J−1 down to 0, of c₀ = x_{i+1}/2 and c₁ = x_{i+1}/2 + 1/2 let x_i be
the one with smaller |c − β_i|∘ (c₀ on ties). Then with probability ≥ 1 − 16(J+1)e^{−r/200},
|x₀ − θ|∘ < 2^{−J}/8.

*Proof.* Write θ_i = frac(2^iθ). By Lemma A (proof.md Section 7.2; the r outcomes are independent indicators),
P(|Z_{i,m′}/r − p_{m′}(θ_i)| ≥ 1/20) ≤ 2e^{−2r/400}; a union bound over the 8(J+1) pairs gives the
failure bound. Assume all deviations are < 1/20. (a) The nearest grid point m*/8 has
|θ_i − m*/8|∘ ≤ 1/16, so p_{m*} ≥ (1 + cos(π/8))/2 > 0.9619, while every m′ with |θ_i − m′/8|∘ ≥ 1/8 has
p_{m′} ≤ (1 + cos(π/4))/2 < 0.8536. The gap exceeds 2/20, so |β_i − θ_i|∘ < 1/8. (b) We show
|x_i − θ_i|∘ < δ_i := 2^{−(J−i)}/8 by downward induction; i = J is (a). Let |x_{i+1} − θ_{i+1}|∘ <
δ_{i+1} ≤ 1/8 and write x_{i+1} − θ_{i+1} = e + z, z ∈ Z, |e| < δ_{i+1}. Since θ_{i+1} = frac(2θ_i),
θ_i ≡ θ_{i+1}/2 + w/2 (mod 1) for some w ∈ {0,1}, and {c₀, c₁} ≡ {θ_{i+1}/2 + e/2, θ_{i+1}/2 + 1/2 + e/2}
(mod 1). One candidate is within |e|/2 < δ_i of θ_i, the other at distance > 1/2 − 1/16. By (a) the good
one is within 1/16 + 1/8 = 3/16 of β_i and the bad one farther than 1/2 − 1/16 − 1/8 = 5/16, so the good
one is chosen. ∎

All x_i are multiples of 2^{−(J+3)}, so the procedure is exact (J+3)-bit integer arithmetic, O(J²) bit
operations, defined for every count vector.

**Procedure F_t** (label of a t-qubit register). Let M′ = 2^t, J = max(1, t−2), r = r₁ (proof.md Section 4). For
each i ∈ {0,…,J} and m′ ∈ {0,…,7}, perform r kickback tests with a = 2^i mod M′, each followed by A3
with this m′ on its control. Apply Lemma P and output û = round(M′x₀) mod M′.

**Corollary F.** If the register is χ_{−u}, then û = u with probability ≥ 1 − 16(J+1)e^{−r/200}.
*Proof.* The test controls are the qubits of Lemma P with θ = u/M′ (proof.md Section 2). M′ ≤ 2^{J+2} (t ≥ 3:
J + 2 = t; t ≤ 2: M′ ≤ 4 < 8). On the success event M′x₀ differs from u + M′z by less than
M′2^{−J}/8 ≤ 1/2, so the rounding returns u, with no tie. ∎
