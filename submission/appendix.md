# Appendix to proof.md (RLS-GD4): reversible arithmetic, cosine table, oracle circuits, quantum search

This file is part of the proof of the claims in `submission.json`; proof.md refers to its sections as
App. A–G. App. A–E are taken from our ROB-G2 entry (55a6ce76) (App. F from our RLS-D3 0a76fda2, App. G from our
SLS 59facd77 and OMX-ML 31c2d043), with the search over a register of d
qubits (d = d₁, d₂ or d₃ of proof.md, Section 4) in place of n qubits and with the label constants c_{j,i} of
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


## C. The circuits 𝒪_i and 𝒟 for a search over d qubits

Fix a search with d qubits and K stored records (w_j, m′_j, b_j), j = 1, …, K, with w_j ∈ [0, 2^d)
(proof.md 6.6). The controller computes the constants c_{j,i} = floor(2^p frac(2^i w_j/2^d)) ∈ [0, 2^p) for
i = 0, …, d−1 (a shift and a mask of w_j: c_{j,i} = floor(w_j 2^{p+i−d}) mod 2^p), and w = bitlength(K) + 29.

**𝒟 (diffusion).** H on each of the d search qubits, then X on each, then the phase flip of |1^d⟩ (a fresh
target qubit is prepared in |1⟩, conjugated by H, and P3d with the d search qubits as controls is applied to
it; then the target is conjugated by H and reset — this multiplies |1^d⟩ by −1 and every other basis state
by 1), then X on each and H on each. As a matrix this is −(2|ψ₀⟩⟨ψ₀| − I) with ψ₀ = H^{⊗d}|0^d⟩; the global
sign −1 is irrelevant.

**𝒪_i (phase oracle of ladder level i).** On the search register |τ⟩ (d qubits) and fresh ancillas:

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
2. *Flag.* For level i (proof.md 6.7) let C*_i = 2^{25}·K + 2^i(2^{25} + 1)(n₀ − n₁) and Θ_i = floor(C*_i/2^i), computed
   classically; then 2^iΣ(τ) > 2^{25}K ⇔ 2^iU* > C*_i ⇔ U* > C*_i/2^i ⇔ U* ≥ Θ_i + 1, and
   |Θ_i + 1| ≤ 2^{25−i}K + (2^{25} + 1)K + 2 < 2^{27}K < 2^{w−1}. Compute f = [U* ≥ Θ_i + 1] by flipping the top wire of U
   (X; this maps two's complement order to unsigned order, U* ↦ U* + 2^{w−1}), applying P3c with the constant
   Θ_i + 1 + 2^{w−1} ∈ [1, 2^w) into a fresh qubit, and flipping the top wire back.
3. *Phase.* Apply Z (= T⁴) to the f qubit.
4. *Clean up.* Uncompute f by its circuit in reverse, then run step 1 in reverse (j = K, …, 1, each with the
   inverse operations), returning U and every ancilla to |0⟩.

Every operation in steps 1–2 is a permutation of computational basis states that leaves |τ⟩ unchanged and
computes f_i(τ) = [2^iΣ(τ) > 2^{25}K] (equivalently S(τ) > 2^{−i}K, S = Σ/2^{25}) exactly, so steps
1–4 implement 𝒪_i = Σ_τ (−1)^{f_i(τ)} |τ⟩⟨τ| ⊗ I on the ancillas (all returned to |0⟩).

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

The circuit 𝒟 equals −𝒟′, so for every ladder level i, 𝒢_i^k = (−1)^k (𝒟′𝒪_i)^k with 𝒢_i = 𝒟𝒪_i (Lemma G with f = f_i
and 𝒪 = 𝒪_i), and the measurement law is the same.

**Lemma I (iteration count).** For d ≥ 4, k_G = floor(785K_G/1000) with K_G = floor(2^{d/2}) satisfies
π/4 < (2k_G + 1)β < 3π/4, so sin²((2k_G + 1)β) > 1/2.

*Proof.* Let x = 2^{−d/2} ≤ 1/4. Then x ≤ β = arcsin x ≤ x/√(1 − x²) ≤ x(1 + x²) ≤ (17/16)x, using
arcsin x = ∫₀^x dz/√(1 − z²) and (1 + x²)²(1 − x²) = 1 + x² − x⁴ − x⁶ ≥ 1 for x² ≤ 1/16. Also
1/x − 1 < K_G ≤ 1/x and 0.785K_G − 1 < k_G ≤ 0.785K_G. Upper: (2k_G + 1)β ≤ (1.57K_G + 1)(17/16)x ≤
(1.57 + x)(17/16) ≤ 1.82·1.0625 < 1.94 < 3π/4. Lower: (2k_G + 1)β ≥ (1.57K_G − 1)x > 1.57 − 2.57x ≥
1.57 − 0.6425 > 0.92 > π/4. On [π/4, 3π/4], sin² ≥ 1/2. ∎

## E. Record laws and score lemmas (proof.md 7.7)

Notation and the filtration (ℋ_j) are those of proof.md 7.7; θ is the target of the search.

**Lemma R (record laws).** Let record j be good. Conditioned on ℋ_{j−1}, w_j is uniform on [0, 2^d), m′_j is uniform on
{0,…,7} and independent of w_j, and given (w_j, m′_j), b_j = 0 with probability exactly p_{m′_j}(w_jθ/2^d).
*Proof.* By Lemma U (proof.md 7.5, with its corollary at the end of 7.5) the labels of the good records are independent and uniform given
𝒦_{R_ℓ} (𝒦_0 in tier 3). The sample keys (Lemma S₂_D) are fresh, the release outcomes of the records not kept are fair
coins or act on Ω (proof.md 7.7), and the (w_i, m′_i, b_i) of earlier records involve other good labels, fresh bits and other
qubits, so conditioning on ℋ_{j−1} leaves w_j uniform; by (J) the qubit of record j is
(|0⟩ + e^{2πi w_jθ/2^d}|1⟩)/√2 in tensor product with everything else, and P2 gives the stated law (A3). ∎

**Lemma B (bounded influence).** For every record and every τ, |Z̃(τ)| ≤ 1 + 2^{−24} = R₀. *Proof.* Lemma T (App. B). ∎

**Lemma E (discretisation).** For every record j and every τ ∈ [0, 2^d), let X̂_j(τ) = (−1)^{b_j}cos(2π(w_jτ/2^d − m′_j/8)).
Then |Z̃_j(τ) − X̂_j(τ)| ≤ η.
*Proof.* Write x = w_j/2^d and φ = frac(xτ). For each i, 2^p frac(2^i x) − c_{j,i} ∈ [0, 1). Since Σ_i τ_i 2^i x = xτ,
Σ_i τ_i 2^p frac(2^i x) ≡ 2^p φ (mod 2^p), so V_j(τ) ≡ 2^pφ − ζ′ (mod 2^p) with ζ′ = Σ_i τ_i(2^p frac(2^i x) − c_{j,i})
∈ [0, d). Hence |V_j(τ)/2^p − φ|∘ < d/2^p < 2^{−q−1} (as d ≤ n < 2^{bitlength(n)}). Also 0 ≤ V_j(τ)/2^p − h_j(τ)/2^q < 2^{−q}.
So |h_j(τ)/2^q − φ|∘ < (3/2)2^{−q}, and as x ↦ cos 2πx has period 1 and is 2π-Lipschitz,
|cos(2π(h_j(τ)/2^q − m′_j/8)) − cos(2π(φ − m′_j/8))| < 3π2^{−q}. Since 2^{q−3}m′_j is an integer and table[k] approximates
cos(2πk/2^q), which has period 2^q in k, |table[k_j(τ)] − cos(2π(h_j(τ)/2^q − m′_j/8))| < τ_T (Lemma T). Adding the bounds
gives the claim. ∎

**Lemma C* (clean correlation).** If record j is good, then for τ ∈ [0, 2^d), E[X̂_j(τ) | ℋ_{j−1}] = 1/2 if τ = θ and 0
otherwise; hence E[Z̃_j(τ) | ℋ_{j−1}] ≥ 1/2 − η if τ = θ and ≤ η otherwise.
*Proof.* By Lemma R, E[(−1)^{b_j} | w_j, m′_j] = 2p_{m′_j}(w_jθ/2^d) − 1 = cos(2π(w_jθ/2^d − m′_j/8)). With
cos A cos B = (cos(A − B) + cos(A + B))/2, E[X̂_j(τ) | w_j, m′_j] = (1/2)cos(2πw_j(θ − τ)/2^d) +
(1/2)cos(2πw_j(θ + τ)/2^d − πm′_j/2). Averaging over m′_j: Σ_{m′=0}^{7} cos(α − πm′/2) = Re(e^{iα}Σ_{m′}(−i)^{m′}) = 0.
Averaging over w_j uniform on [0, 2^d): (1/2^d)Σ_w cos(2πw(θ − τ)/2^d) is 1 if θ ≡ τ (mod 2^d), i.e. τ = θ, and 0
otherwise (a sum of 2^d-th roots of unity). Lemma E gives the second statement. ∎

**Lemma M (any record).** For every record j, every τ and every history in ℋ_{j−1} of positive probability,
−(1/2 + η) ≤ E[Z̃_j(τ) | ℋ_{j−1}] ≤ 1/2 + η.
*Proof.* Every generator of ℋ_{j−1} is obtained before the P2 of record j (steps 1–3 of 6.4 precede step 4, and records
are measured in the order j = 1, …, K). Fix an outcome g of ℋ_{j−1}
together with w_j (fixed before m′_j is drawn). Let σ_g be the reduced state of record
j's qubit given g, written (I + xX + yY + zZ)/2 with x + iy = re^{iα}, 0 ≤ r ≤ 1. m′_j is drawn from fresh qubits, so it
is uniform and independent of g, and P2 with θ′ = 2πm′/8 has outcome 0 exactly when it projects onto
(|0⟩ + e^{iθ′}|1⟩)/√2; so E[(−1)^b | g, m′] = x cos θ′ + y sin θ′ = r cos(θ′ − α). With v = w_jτ/2^d and θ′_{m′} = 2πm′/8,
E[X̂_j(τ) | g] = (1/8)Σ_{m′} r cos(θ′_{m′} − α)cos(2πv − θ′_{m′}) = (r/2)cos(2πv − α) + (r/16)Σ_{m′}cos(2θ′_{m′} − α − 2πv)
= (r/2)cos(2πv − α) ∈ [−1/2, 1/2], because Σ_{m′=0}^{7} e^{2iθ′_{m′}} = Σ_{m′} i^{m′} = 0. Lemma E and the tower property give
the claim. ∎

## F. Shuffled pairing (proof.md 7.6)

**Lemma KS (shuffled pairing).** Fix a stage m of a tier, condition on 𝒦_{m−1} and on all stage-m keys,
and consider one key group with n_β records, c_β of them good. After the uniform shuffle of 6.4, let gg_β be
the number of good–good pairs formed in the group. Then for every Λ > 0, with conditional probability at least
1 − 4e^{−Λ},

  gg_β ≥ c_β²/(2n_β) − 1/2 − 4 s_β,  where s_β = √(n_β Λ/2).

*Proof.* If n_β ≤ 1, then c_β ≤ 1, gg_β = 0 and the right side is ≤ 0. Let n_β ≥ 2, h = floor(n_β/2), c = c_β,
n = n_β. The shuffle makes the order of the group uniformly random and independent of everything else. Pairs
are (A_i, B_i), the records at positions 2i−1 and 2i, i = 1, …, h. A uniform order is generated by: a uniform
h-subset A of the group (odd positions), then a uniform h-subset B of the rest (even positions), then a
uniform bijection between A and B (who sits next to whom). Hence: (1) a = #good in A is hypergeometric
(population n, c marked, h draws); (2) given A, b′ = #good in B is hypergeometric (population n − h, c − a
marked, h draws); (3) given A and B, gg_β is hypergeometric (population B of size h with b′ marked, a draws:
the partners of the a good members of A). By Lemma H′ (proof.md Section 7.2) each lies within √(hΛ/2) ≤ s of its mean on the
required side, except with probability e^{−Λ} each, where s = s_β; for (1) we use both sides. On these events,
a ≥ hc/n − s, c − a ≥ c − hc/n − s, b′ ≥ h(c − a)/(n − h) − s ≥ hc/n − hs/(n − h) − s ≥ hc/n − 2s (as
h ≤ n − h), and gg_β ≥ ab′/h − s. If hc/n ≤ 2s, then hc²/n² ≤ 2s·(c/n) ≤ 2s and the claim is trivial.
Otherwise both factors are positive and gg_β ≥ (hc/n − s)(hc/n − 2s)/h − s ≥ hc²/n² − 3s(c/n) − s
≥ hc²/n² − 4s. Finally hc²/n² ≥ ((n−1)/2)c²/n² = c²/(2n) − c²/(2n²) ≥ c²/(2n) − 1/2. ∎


**Corollary KS (one stage).** Under the same conditioning, with G = G_{m−1} good and P = P_{m−1} bad
records in at most 2^b nonempty groups, and Λ = 2b + 64,

  gg ≥ G²/(2(G + P)) − 2^b/2 − 4√(2^b (G + P) Λ/2),

except with conditional probability at most 4·2^b e^{−Λ}.
*Proof.* Sum Lemma KS over the groups (union bound). Σ_β c_β²/n_β ≥ (Σ c_β)²/Σ n_β = G²/(G + P) by the
Cauchy–Schwarz inequality, and Σ_β √n_β ≤ √(2^b Σ n_β) = √(2^b(G + P)). ∎

## G. Lemma P (label reading), procedure F_t and Corollary F (proof.md Section 3)

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
