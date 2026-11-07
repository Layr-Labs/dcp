# Appendix to proof.md (RLS-G6R): reversible arithmetic, cosine table, oracle circuits, quantum search

This file is part of the proof of the claims in `submission.json`; proof.md refers to its sections as
App. A–D. The material is taken from our ROB-G2 entry (55a6ce76), with the search over a register of d
qubits (d = d₁, …, d₄ of proof.md, Section 4) in place of n qubits and with the label constants c_{j,i} of
proof.md Section 6.6. It uses the gates, the primitive P2 (= A3 of proof.md) and the fair bits of proof.md
Section 1.

## A. Further reversible arithmetic (exact)

All circuits below use X, CNOT and Toffoli
only, return every ancilla to |0⟩, and are emitted gate by gate by a uniform generator.
* *P3a (controlled constant addition mod 2^p, in place).* the controlled constant adder A2 of proof.md ("add mod 2^t" with t = p, controlled
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
  fresh qubit and its carries uncomputed as in A1(b) of proof.md. O(w) gates.
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

**𝒪 (phase oracle).** On the search register |τ⟩ (d qubits) and fresh ancillas:

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
2. *Flag.* Classically let C* = 17·2^{25}·K + 100(2^{25} + 1)(n₀ − n₁) and Θ = floor(C*/100); then
   100Σ(τ) > 17·2^{25}K ⇔ 100U* > C* ⇔ U* > Θ ⇔ U* ≥ Θ + 1, and |Θ + 1| ≤ |C*|/100 + 2 < 1.2·2^{25}K + 2 <
   2^{w−1}. Compute f = [U* ≥ Θ + 1] by flipping the top wire of U (X; this maps two's complement order to
   unsigned order, U* ↦ U* + 2^{w−1}), applying P3c with the constant Θ + 1 + 2^{w−1} ∈ [1, 2^w) into a fresh
   qubit, and flipping the top wire back.
3. *Phase.* Apply Z (= T⁴) to the f qubit.
4. *Clean up.* Uncompute f by its circuit in reverse, then run step 1 in reverse (j = K, …, 1, each with the
   inverse operations), returning U and every ancilla to |0⟩.

Every operation in steps 1–2 is a permutation of computational basis states that leaves |τ⟩ unchanged and
computes f(τ) = [100Σ(τ) > 17·2^{25}K] (equivalently S(τ) > θ₀K with θ₀ = 17/100, S = Σ/2^{25}) exactly, so steps
1–4 implement 𝒪 = Σ_τ (−1)^{f(τ)} |τ⟩⟨τ| ⊗ I on the ancillas (all returned to |0⟩).

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

The circuit 𝒟 equals −𝒟′, so 𝒢^k = (−1)^k (𝒟′𝒪)^k with 𝒢 = 𝒟𝒪, and the measurement law is the same.

**Lemma I (iteration count).** For d ≥ 4, k_G = floor(785K_G/1000) with K_G = floor(2^{d/2}) satisfies
π/4 < (2k_G + 1)β < 3π/4, so sin²((2k_G + 1)β) > 1/2.

*Proof.* Let x = 2^{−d/2} ≤ 1/4. Then x ≤ β = arcsin x ≤ x/√(1 − x²) ≤ x(1 + x²) ≤ (17/16)x, using
arcsin x = ∫₀^x dz/√(1 − z²) and (1 + x²)²(1 − x²) = 1 + x² − x⁴ − x⁶ ≥ 1 for x² ≤ 1/16. Also
1/x − 1 < K_G ≤ 1/x and 0.785K_G − 1 < k_G ≤ 0.785K_G. Upper: (2k_G + 1)β ≤ (1.57K_G + 1)(17/16)x ≤
(1.57 + x)(17/16) ≤ 1.82·1.0625 < 1.94 < 3π/4. Lower: (2k_G + 1)β ≥ (1.57K_G − 1)x > 1.57 − 2.57x ≥
1.57 − 0.6425 > 0.92 > π/4. On [π/4, 3π/4], sin² ≥ 1/2. ∎
