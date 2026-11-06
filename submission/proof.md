# A Kuperberg-type qubit sieve for the DCP over Z/NZ, every N ≥ 2, with proved 2^{4√n}·poly(n) bounds

This document is the single evidence file for all five claims of `submission.json`.
It specifies one algorithm, DCP-SIEVE, with one parameter choice (a function of
n = ⌈log₂ N⌉ only), and proves, in the cost model of `rules.md`:

* full-secret recovery with probability ≥ 19/20 for every N ≥ 2 and every s ∈ Z/NZ (Theorem 9.1);
* T(N,s) ≤ C·2^{4√n}·n⁶, S_C(N,s) ≤ C·2^{4√n}·n², S_Q(N,s) ≤ C·2^{4√n}·n², Q(N,s) ≤ C·2^{4√n}·n²
  on every execution branch, for one absolute constant C (Theorem 10.1);
* all four envelopes have growth index exactly 1/2 (Section 10.4);
* the fractional error tolerance ε(n) = 0 under the clean-sample model (Section 11).

The algorithm is Kuperberg's qubit sieve (G. Kuperberg, *A subexponential-time quantum
algorithm for the dihedral hidden subgroup problem*, SIAM J. Comput. 35(1):170–188, 2005,
Algorithms 1–2) adapted so that **every step is proved for arbitrary N**: the Fourier-basis
measurement is realised by phase estimation of the cyclic shift (Section 3), the sieve runs
on *integer* labels with a *designated fair bit* per sample that no sieve decision ever reads
(Sections 4–6), and s is recovered from estimates of the fractions {2^j s/N} by a Kitaev-type
stitching argument (Sections 7–8). Nothing is taken from the literature except two black-box
facts that are stated exactly where they are used: the Solovay–Kitaev theorem (gate
synthesis, Lemma 3.5(c)) and the exact equivalence of the semiclassical inverse QFT with the
coherent one (Griffiths–Niu, Lemma 3.5(b)); all probabilistic estimates are Chebyshev's
inequality, proved inline. We do not claim novelty of the ideas; the contribution is a
complete, rigorous, cost-model-specific proof for all N.

Throughout, "absolute constant" means a constant independent of N, s, n, and of all
random outcomes. Logarithms are base 2 unless written ln. For a real x, {x} = x − ⌊x⌋,
and d(x,y) denotes the circular distance on R/Z, d(x,y) = min_{z∈Z} |x − y − z| ∈ [0, 1/2].
ω = ω_N = e^{2πi/N}. Big-O constants are absolute.

---

## 1. Problem, input, and the two elementary facts

The input is N (in binary, n = ⌈log₂ N⌉ bits, N ≥ 2) and fresh copies of

ρ_s = (1/N) Σ_{x=0}^{N−1} |ψ_{x,s}⟩⟨ψ_{x,s}|,  |ψ_{x,s}⟩ = (|0,x⟩ + |1,(x+s) mod N⟩)/√2,

where the second register is an n-qubit register holding an integer in [0, 2^n) and the
relevant states have support only on [0, N). We call the first register the *phase qubit*
and the second the *value register*.

**Definition 1.1 (phase states).** For an integer k let |φ_k⟩ = (|0⟩ + ω^{ks}|1⟩)/√2.
Since ω^N = 1, |φ_k⟩ depends only on k mod N, but we always carry k as an *integer*
("integer label").

**Lemma 1.2 (combination).** Let k, ℓ be integers. Apply CNOT with control the qubit holding
|φ_k⟩ and target the qubit holding |φ_ℓ⟩, then measure the target in the computational
basis. The outcome is 0 or 1, **each with probability exactly 1/2, independently of k, ℓ and s**;
on outcome 0 the control is left in the state |φ_{k+ℓ}⟩, on outcome 1 in the state |φ_{k−ℓ}⟩
(up to a global phase).

*Proof.* |φ_k⟩|φ_ℓ⟩ = ½(|00⟩ + ω^{ℓs}|01⟩ + ω^{ks}|10⟩ + ω^{(k+ℓ)s}|11⟩). CNOT maps
|10⟩↦|11⟩, |11⟩↦|10⟩ and fixes |00⟩,|01⟩, giving
½(|00⟩ + ω^{ℓs}|01⟩ + ω^{(k+ℓ)s}|10⟩ + ω^{ks}|11⟩)
= ½[(|0⟩ + ω^{(k+ℓ)s}|1⟩)|0⟩ + ω^{ℓs}(|0⟩ + ω^{(k−ℓ)s}|1⟩)|1⟩].
The two branches have squared norm ½ each, and the normalised post-measurement states are
|φ_{k+ℓ}⟩ and ω^{ℓs}|φ_{k−ℓ}⟩. ∎

**Lemma 1.3 (Fourier basis).** Let |k̂⟩ = N^{−1/2} Σ_{y=0}^{N−1} ω^{−ky}|y⟩ for k ∈ Z/NZ.
These N vectors are an orthonormal basis of span{|y⟩ : 0 ≤ y < N}. If the value register of
|ψ_{x,s}⟩ is measured in this basis, every outcome k has probability exactly 1/N, and the
post-measurement state of the phase qubit is exactly |φ_k⟩, for every x. Consequently the
same holds for the mixture ρ_s.

*Proof.* Orthonormality is the standard character identity. ⟨k̂|y⟩ = ω^{ky}/√N, so
(I ⊗ ⟨k̂|)|ψ_{x,s}⟩ = (2N)^{−1/2}(ω^{kx}|0⟩ + ω^{k((x+s) mod N)}|1⟩) = (2N)^{−1/2} ω^{kx}(|0⟩ + ω^{ks}|1⟩),
using ω^{k((x+s) mod N)} = ω^{k(x+s)} because ω^N = 1. Its squared norm is 1/N, and the
normalised vector is ω^{kx}|φ_k⟩. ∎

So, modulo implementing the measurement of Lemma 1.3 (Section 3), each source copy yields a
qubit |φ_k⟩ with a uniformly random *known* label k ∈ [0, N).

**Lemma 1.4 (relabelling).** Let w be an integer coprime to N and w^{−1} its inverse mod N.
For every integer k, |φ_k⟩ for the hidden shift s equals |φ_{wk}⟩ for the hidden shift
s' := w^{−1}s mod N, i.e. (|0⟩ + ω^{ks}|1⟩) = (|0⟩ + ω^{(wk)s'}|1⟩).

*Proof.* (wk)s' ≡ k(w w^{−1})s ≡ ks (mod N). ∎

Thus the algorithm may *classically* replace every label k by k' = wk mod N (still uniform on
[0, N), since multiplication by w is a bijection of Z/NZ) and proceed as if the hidden shift
were s'. The phase qubits are untouched.

---

## 2. The algorithm DCP-SIEVE and its parameters

### 2.1 Small N

If N ≤ 16 the algorithm runs the **exhaustive shift test**: for t = 0, 1, …, N−1 it performs 10
tests, each with a fresh copy: apply to the value register, controlled on the phase qubit,
the permutation y ↦ (y − t) mod N for y < N (identity for y ≥ N), then measure the phase qubit
in the X basis (Hadamard, then computational measurement); if any of the 10 outcomes is −,
reject t. It outputs the first t whose 10 tests all give +, and 0 if there is none.
On a component with offset x the controlled subtraction yields (|0,x⟩ + |1,(x+s−t) mod N⟩)/√2,
which is |+⟩|x⟩ if t = s (so t = s never fails) and has orthogonal value-register states if
t ≠ s (so the X measurement gives + with probability exactly ½). The probability that some
wrong t passes is ≤ (N−1)2^{−10} ≤ 15/1024 < 1/60, so the output is s with probability > 19/20.
At most 10N ≤ 160 copies, O(1) gates and O(1) bits/qubits are used. Everything below concerns N ≥ 17, i.e. n ≥ 5.

### 2.2 Parameters (N ≥ 17)

* n = ⌈log₂ N⌉ ≥ 5; note 2^{n−1} < N ≤ 2^n.
* a = the 2-adic valuation of N (N = 2^a·M_odd with M_odd odd).
* m' = ⌈√n⌉ (block width of the sieve).
* η = 1/64 (angle accuracy), J = n − 4 (number of levels minus one).
* M₀ = 10⁶·n (copies per angle estimate).
* For a level j ∈ {0, …, J}: j₀ = min(j, a), h_max = ⌊N / 2^{j₀+1}⌋,
  m_A = ⌈j₀/m'⌉ (divisibility stages), ρ₀ = m_A + n − j₀, m_B = ⌈(ρ₀ − 1)/m'⌉ (magnitude stages),
  m = m_A + m_B (total sieve depth), and
  T_fin = 10⁶·n·2^{⌈3m/2⌉+6}, L₀ = 5^m·T_fin (initial list size).
* The relabelling multiplier w_j: if j < a then w_j = 1. If j ≥ a then w_j is the unique
  integer in [1, N] with w_j ≡ 1 (mod 2^a) and w_j·2^{j−a} ≡ 1 (mod M_odd) (if M_odd = 1 the
  second condition is void; if a = 0 the first is void). It exists by the Chinese remainder
  theorem and is coprime to N; it is computed with the extended Euclidean algorithm.
* Phase-estimation precision: Q_max = 2n·L₀, δ = 2^{−20−2⌈log₂ Q_max⌉}, M = n + 21 + 2⌈log₂ Q_max⌉
  (ancilla qubits), and ε_s = 1/(400·M·Q_max) (synthesis accuracy of every single-qubit rotation).
  All quantities from j₀ onwards (m, T_fin, L₀, Q_max, δ, M, ε_s) are **per level** j; when the level
  matters we write L₀^{(j)} etc. The algorithm computes them from N and j; they are explicit
  functions of N (through n, a and j), not of s.

Lemma 2.1 below records the size relations used later; all of them are elementary.

**Lemma 2.1.** For N ≥ 17 and every level j: (i) 2^{j₀+1} ≤ 2^{n−3} < N/4, hence h_max ≥ 4 and
2^{j₀+1}h_max > N − 2^{j₀+1} > 3N/4; (ii) √n − 1 ≤ m ≤ √n + 3; (iii) 5·T_fin ≥ 100·2^{m'+1};
(iv) log₂ L₀ ≤ 3.83√n + log₂ n + 39, so
log₂ Q_max ≤ 3.83√n + 2 log₂ n + 40 and M ≤ n + 7.66√n + 4 log₂ n + 103 ≤ 12n + 103.

*Proof.* (i) j₀ ≤ j ≤ n − 4 and N > 2^{n−1}. (ii) Lower bound: m_A ≥ j₀/m' and
m_B ≥ (ρ₀−1)/m' ≥ (n − j₀ − 1)/m' + m_A/m' ≥ (n − j₀ − 1)/m', so m ≥ (n−1)/m' ≥ (n−1)/(√n+1) = √n − 1.
Upper bound: m_A ≤ j₀/m' + 1 and m_B ≤ (m_A + n − j₀ − 1)/m' + 1 ≤ (j₀/m' + n − j₀)/m' + 1, so
m ≤ n/m' + j₀/m'² + 2 ≤ √n + 1 + 2. (iii) T_fin ≥ 10⁶·2^{(3/2)(√n−1)+6} and 2^{m'+1} ≤ 2^{√n+2};
the ratio 5T_fin/(100·2^{m'+1}) ≥ 5·10⁴·2^{√n/2+2.5} > 1. (iv) log₂ L₀ = m log₂5 + log₂T_fin ≤
2.322(√n+3) + 20 + log₂n + 1.5(√n+3) + 7 ≤ 3.83√n + 39 + log₂ n; then log₂ Q_max = 1 + log₂ n +
log₂ L₀ and M = n + 21 + 2⌈log₂ Q_max⌉ ≤ n + 21 + 2(3.83√n + 2log₂ n + 41). ∎

Note also that m ≥ m_B ≥ 1 for every level, because ρ₀ ≥ n − j₀ ≥ 4 > 1; so 2^{m−1} is an integer
and Lemma 5.4 (which needs k = 2^{m−1} ≥ 1) applies.

### 2.3 The algorithm

DCP-SIEVE runs, for each level j = 0, 1, …, J, an independent **run** R_j (fresh copies, fresh
classical and quantum workspace); each run outputs an angle estimate β_j ∈ [0,1) (a dyadic
rational with 16 fractional bits) or aborts. If any run aborts, the algorithm outputs 0 (this
branch is a failure, counted in the error probability). Otherwise it applies the stitching
procedure of Section 8 to (β_0, …, β_J) and outputs s. One run R_j consists of:

**Step A (acquisition).** Repeat at most 2L₀ times, stopping as soon as L₀ qubits have been
*kept*: acquire one fresh copy of ρ_s; perform the Fourier measurement of Section 3 on its
value register (this yields a label k ∈ [0, N) and leaves the phase qubit in a state close to
|φ_k⟩); measure and release the value register and all phase-estimation ancillas; set
k' = w_j·k mod N; if k' ≥ 2^{j₀+1}h_max, release the phase qubit (*discarded*); otherwise
*keep* the phase qubit and write k' = 2^{j₀+1}h + 2^{j₀}b + r with 0 ≤ r < 2^{j₀}, b ∈ {0,1},
0 ≤ h < h_max, and store the list entry (qubit address, K, K̃) with
**true label** K = k' and **coarse label** K̃ = k' − 2^{j₀}b = 2^{j₀+1}h + r.
If fewer than L₀ qubits are kept after 2L₀ acquisitions, abort.

**Step B (sieve).** The list L_t at the start of stage t (t = 0, …, m−1) is a list of entries
(qubit, K, K̃). The stage does: sort the list by a *bucket key* κ_t(K̃) (defined below, a function
of the coarse label only), ties broken by the current list position (i.e. sort by the pair (κ_t(K̃), position)); pair
consecutive entries having equal keys, so that at most one entry per key value is left unpaired; release every unpaired qubit; for every pair (first entry e,
second entry e'), apply Lemma 1.2 with control e and target e'; on outcome 1 (label K − K'),
release the target qubit and put the entry (qubit of e, K − K', K̃ − K̃') into L_{t+1}; on
outcome 0, release both qubits (the entry is dropped). If |L_{t+1}| < |L_t|/5, abort.
The bucket keys:

* *Divisibility stages* t = 0, …, m_A − 1 (only if j₀ ≥ 1): κ_t(K̃) = K̃ mod 2^{min((t+1)m', j₀)}
  (non-negative residue). Since the entering coarse labels are ≡ 0 (mod 2^{min(tm', j₀)})
  (invariant, Lemma 4.1), the key takes at most 2^{m'} values.
* *Magnitude stages* u = 0, …, m_B − 1 (stage t = m_A + u): with ρ_u := max(ρ₀ − u·m', 1)
  — equivalently ρ_{u+1} = max(ρ_u − m', 1) — the key is κ_t(K̃) = ⌊K̃ / 2^{j₀+ρ_{u+1}}⌋
  (floor division of integers, negative values allowed). Since the entering coarse labels
  satisfy |K̃/2^{j₀}| < 2^{ρ_u} (Lemma 4.1), the key lies in [−2^{ρ_u−ρ_{u+1}}, 2^{ρ_u−ρ_{u+1}} − 1]
  and takes at most 2^{m'+1} values.

**Step C (selection).** After stage m−1 the final list L_m has ≥ T_fin entries (else abort) and,
by Lemma 4.1, every coarse label is K̃ ∈ {−2^{j₀}, 0, 2^{j₀}} and every true label K is a
multiple of 2^{j₀}; write K̄ = K/2^{j₀}. Compute, over the multiset of values K̄ in L_m, an
integer v maximising min(c(v), c(v+1)), where c(x) is the number of entries with K̄ = x. If
min(c(v), c(v+1)) < 2M₀, abort.

**Step D (angle estimation).** Take 2M₀ entries with K̄ = v: measure M₀ of them in the X basis
(H, then computational measurement) and M₀ in the Y basis (S†, then H, then computational
measurement). Let p̂_X, p̂_Y be the fractions of outcome 0. Compute, in fixed-point arithmetic with
20 fractional bits, ĉ = 2p̂_X − 1, ŝ = 2p̂_Y − 1, and an angle α_v ∈ [0,1) (in turns) with
|α_v − atan2(ŝ, ĉ)/(2π)| ≤ 2^{−16} (mod 1). Do the same for 2M₀ entries with K̄ = v+1, giving
α_{v+1}. Output β_j = (α_{v+1} − α_v) mod 1, rounded to 16 fractional bits. Release all qubits.

**Final step (stitching, Section 8).** From (β_0, …, β_J) compute a dyadic θ̂ ∈ [0,1) and output
s = ⌊θ̂·N + ½⌋ mod N.

All loops have fixed bounds (2L₀ acquisitions per run, m stages, list sizes ≤ L₀), so every
execution branch terminates within the bounds of Section 10; aborts only affect the success
probability, which is analysed in Section 9.

---

## 3. The Fourier-basis measurement by phase estimation

Let U be the unitary on the n-qubit value register defined by U|y⟩ = |(y+1) mod N⟩ for
0 ≤ y < N and U|y⟩ = |y⟩ for N ≤ y < 2^n (a permutation of basis states, hence unitary).
For 0 ≤ l < M let c_l = 2^l mod N; then U^{2^l}|y⟩ = |(y + c_l) mod N⟩ for y < N.

**Lemma 3.1 (eigenvectors).** U|k̂⟩ = ω^k|k̂⟩ for every k ∈ Z/NZ.

*Proof.* U|k̂⟩ = N^{−1/2}Σ_y ω^{−ky}|y+1 mod N⟩ = N^{−1/2}Σ_y ω^{−k(y−1)}|y⟩ = ω^k|k̂⟩. ∎

**The circuit PE (ideal gates).** On the value register (supported on [0,N)) and M fresh
ancilla qubits a_0, …, a_{M−1}:
1. apply H to each ancilla;
2. for each l, apply U^{2^l} to the value register controlled on a_l;
3. apply the inverse quantum Fourier transform F⁻¹ over Z/2^M to the ancillas, where
   F|y⟩ = 2^{−M/2}Σ_{j=0}^{2^M−1} e^{2πi yj/2^M}|j⟩ and the ancilla string (a_{M−1}…a_0) is read as
   the integer y = Σ_l a_l 2^l;
4. measure the ancillas in the computational basis, obtaining j ∈ [0, 2^M);
5. output k = r(j) := ⌊jN/2^M + ½⌋ mod N; measure the value register in the computational
   basis and release it and the ancillas.

**Lemma 3.2 (PE on an eigenvector).** On input |k̂⟩ ⊗ |0…0⟩, after step 3 the state is
|k̂⟩ ⊗ |a_k⟩ with |a_k⟩ = Σ_j A_k(j)|j⟩, A_k(j) = 2^{−M}Σ_{y=0}^{2^M−1} e^{2πi y(θ_k − j/2^M)},
θ_k = k/N.

*Proof.* After step 2 the ancillas hold ⊗_l (|0⟩ + e^{2πi 2^l θ_k}|1⟩)/√2 = 2^{−M/2}Σ_y e^{2πi yθ_k}|y⟩
by Lemma 3.1, the value register being unchanged; F⁻¹ gives the stated amplitudes. ∎

**Lemma 3.3 (tail bound).** For every k, Σ_{j : r(j) ≠ k} |A_k(j)|² ≤ 2N/2^M ≤ δ.

*Proof.* Write d_j := 2^M θ_k − j reduced into (−2^{M−1}, 2^{M−1}] modulo 2^M, and
δ_j = d_j/2^M ∈ (−½, ½]. If d_j = 0 then |A_k(j)| = 1 (and r(j) = k). Otherwise, summing the
geometric series, |A_k(j)| = 2^{−M}|sin(π 2^M δ_j)/sin(π δ_j)| ≤ 2^{−M}/(2|δ_j|) = 1/(2|d_j|),
using |sin πδ| ≥ 2|δ| for |δ| ≤ ½. If |d_j| < 2^M/(2N) =: e then |jN/2^M − k| < ½ modulo N,
so r(j) = k. Hence the bad outcomes satisfy |d_j| ≥ e, and as j ranges over [0, 2^M) the
numbers d_j are 2^M reals spaced exactly 1 apart; those with d_j ≥ e are ≥ e, ≥ e+1, …, and
those with d_j ≤ −e are ≤ −e, ≤ −e−1, …. Therefore
Σ_{r(j)≠k}|A_k(j)|² ≤ 2·Σ_{i≥0} 1/(4(e+i)²) ≤ ½(1/e² + ∫_e^∞ dx/x²) = ½(1/e² + 1/e) ≤ 1/e = 2N/2^M,
using e ≥ 1 (M ≥ n+1). Finally 2N/2^M ≤ 2^{n+1−M} = 2^{−20−2⌈log₂Q_max⌉} = δ. ∎

**Lemma 3.4 (PE is close to the ideal Fourier measurement).** Let 𝓜 be the ideal
instrument of Lemma 1.3 (project the value register onto |k̂⟩⟨k̂|, output k, discard the
register), and let 𝓔 be the instrument "run PE with ideal gates, output r(j), discard
everything but the phase qubit". Then for every input state of (phase qubit ⊗ value register
supported on [0,N)), possibly entangled with a reference system, the joint output
(classical k, residual quantum state) of 𝓔 and of 𝓜 differ by at most 4√δ in trace distance;
i.e. ‖𝓔 − 𝓜‖_⋄ ≤ 4√δ.

*Proof.* Let Π_k be the projector onto {|j⟩ : r(j) = k}. By Lemma 3.3,
‖Π_k a_k‖² ≥ 1 − δ. Put |g_k⟩ = Π_k|a_k⟩/‖Π_k a_k‖. Then
‖a_k − g_k‖ ≤ ‖(1−Π_k)a_k‖ + (1 − ‖Π_k a_k‖) ≤ √δ + δ ≤ 2√δ.
Steps 1–3 of PE act on span{|k̂⟩} ⊗ |0…0⟩ as the isometry V|k̂⟩ = |k̂⟩|a_k⟩ (Lemma 3.2); define
the isometry W|k̂⟩ = |k̂⟩|g_k⟩. For any unit vector Σ_k c_k|k̂⟩ (tensored with anything on the
phase qubit and a reference), ‖(V−W)Σ_k c_k|k̂⟩‖² = Σ_k|c_k|²‖a_k − g_k‖² ≤ 4δ because the |k̂⟩
are orthonormal; hence ‖V − W‖ ≤ 2√δ and, for every state σ, ‖VσV† − WσW†‖₁ ≤ 2‖V−W‖ ≤ 4√δ
(write VσV† − WσW† = (V−W)σV† + Wσ(V−W)† and use ‖XσY‖₁ ≤ ‖X‖‖Y‖‖σ‖₁).
Now consider W followed by steps 4–5. Since |g_k⟩ is supported on {j : r(j) = k}, outcome
r(j) = k occurs with probability Σ_{j: r(j)=k}|⟨j|g_k⟩|²·Tr[(1⊗|k̂⟩⟨k̂|)σ] = Tr[(1⊗|k̂⟩⟨k̂|)σ],
and the residual state after discarding j and the value register is
Tr_val[(1⊗|k̂⟩⟨k̂|)σ(1⊗|k̂⟩⟨k̂|)]/Tr[(1⊗|k̂⟩⟨k̂|)σ]: exactly the instrument 𝓜. The map "steps 4–5"
is trace-non-increasing on each outcome branch and the sum over branches is trace preserving,
so applying it to VσV† and WσW† changes the trace distance by at most a factor 1. ∎

**Lemma 3.5 (Clifford+T realisation of PE).** There is an implementation PE' of PE with
Clifford+T gates, computational-basis measurements and classically chosen gates, such that
(i) the instrument 𝓔' realised by PE' satisfies ‖𝓔' − 𝓔‖_⋄ ≤ 2Mε_s;
(ii) PE' uses at most c₁(Mn + M·log⁴(1/ε_s)) gates and measurements, at most c₁(n + M) qubits,
and at most c₁(Mn + M·log⁴(1/ε_s))·⌈log₂(𝖬+2)⌉ bit operations of classical control (𝖬 = total
allocated bits and qubits), for an absolute constant c₁.

*Proof.* (a) *Controlled additions.* U^{2^l} is the permutation y ↦ (y + c_l) mod N on [0,N),
identity on [N, 2^n). Its controlled version is the classical reversible map
(a, y) ↦ (a, f_a(y)), f_1 = U^{2^l}, f_0 = id. Fix a Boolean circuit for f_1 of size ≤ c₂ n with
fan-in-2 AND/XOR/NOT gates (compare y with N; add the (n+1)-bit constant c_l; compare with N;
conditionally subtract N; each is a linear-size ripple circuit), and likewise for f_1^{−1}
(subtract c_l mod N). Compute f_a(y) into a fresh zero register by Bennett's method: each AND
gate becomes a Toffoli writing into a fresh ancilla, each XOR a CNOT, each NOT an X; all gates
are additionally controlled on a (a Toffoli controlled on a becomes a 3-controlled Toffoli,
which is a constant number of Toffolis with one ancilla); then copy the result with CNOTs and
run the gates backwards to clear the ancillas. Then swap the registers and, using the circuit
for f_a^{−1} in the same way, clear the old input (which equals f_a^{−1} of the new register).
Each Toffoli is an exact constant-size Clifford+T circuit. Total: ≤ c₃ n gates and ≤ c₃ n
ancillas per controlled addition, for an absolute constant c₃; over M values of l, ≤ c₃Mn gates.
(b) *Inverse QFT.* Steps 3–4 are implemented in the semiclassical form (Griffiths–Niu):
the bits j_0, j_1, …, j_{M−1} of j are obtained in this order from the ancillas
a_{M−1}, a_{M−2}, …, a_0. For i = 0, 1, …, M−1: apply to a_{M−1−i} the phase gate
P(α_i) = diag(1, e^{iα_i}) with α_i = −2π·Σ_{t=0}^{i−1} j_t·2^{t−i−1} (a dyadic rational multiple
of 2π; α_0 = 0), then H, then measure a_{M−1−i} in the computational basis, and call the outcome
j_i. (Motivation: a_{M−1−i} carries the relative phase e^{2πi 2^{M−1−i}θ}; if 2^Mθ were the
integer j = Σ_t j_t 2^t, this phase would be exp(2πi(j_i/2 + Σ_{t<i} j_t 2^{t−i−1})), and
removing the second summand with P(α_i) leaves (−1)^{j_i}, read out by H and a measurement.)
This is the standard circuit for F⁻¹ followed by measurement, in which each
controlled phase gate whose control is measured later has been replaced by a classically
controlled phase gate applied after the control's measurement; by the principle of deferred
measurement the joint distribution of (j, residual state) is identical to that of PE. All
angles are dyadic rationals computed exactly from measured bits in O(M²) bit operations.
(c) *Synthesis.* Each P(α) is, up to the unobservable global phase e^{iα/2}, the element
R_z(α) = diag(e^{−iα/2}, e^{iα/2}) ∈ SU(2). The Solovay–Kitaev theorem [C. M. Dawson and
M. A. Nielsen, *The Solovay–Kitaev algorithm*, Quantum Inf. Comput. 6(1):81–95, 2006, Theorem 1
and Section 3, applied to the instruction set {H, T, T†} ⊂ SU(2) (up to phases), which is
closed under inverses and generates a dense subgroup] gives a deterministic classical algorithm
which, for a target V ∈ SU(2) specified to O(log(1/ε)) bits and any ε > 0, outputs a word of
length O(log^{3.97}(1/ε)) in H, T, T† whose product is within operator-norm distance ε of V,
using O(log^{2.71}(1/ε)) arithmetic operations on O(log(1/ε))-bit numbers; it needs a fixed
finite ε₀-net of short words, which our controller computes once at start-up by enumerating
all words of a fixed constant length (constant work and space independent of N). We invoke it
with ε = ε_s for each of the M gates P(α_l), at classical cost O(log^{2.71}(1/ε_s)·log²(1/ε_s))
bit operations and gate count O(log⁴(1/ε_s)) each. Since the gate is uncontrolled, replacing
P(α) by e^{iα/2}·(synthesised R_z) changes the physical operation by operator norm ≤ ε_s.
(d) *Error.* 𝓔 (ideal gates, coherent) equals the ideal semiclassical instrument by (b). The
semiclassical instrument is a composition of M steps of the form "measure some qubits, then
apply a gate chosen by the outcomes"; replacing in one step every possible chosen gate G_o by
G̃_o with ‖G_o − G̃_o‖ ≤ ε_s changes that step, as a map on states, by at most 2ε_s in diamond
norm (for ρ = Σ_o ρ_o with ρ_o the outcome-o branch, ‖Σ_o(G_oρ_oG_o† − G̃_oρ_oG̃_o†)‖₁ ≤
Σ_o 2ε_s‖ρ_o‖₁ = 2ε_s, also with a reference system). By the triangle inequality over the M
steps, ‖𝓔' − 𝓔‖_⋄ ≤ 2Mε_s. (e) Resource counts follow by adding (a)–(c); each gate and each
classical memory access is charged its address cost ⌈log₂(𝖬+2)⌉. ∎

**Corollary 3.6.** The instrument 𝓔' realised on each acquired copy satisfies
‖𝓔' − 𝓜‖_⋄ ≤ 4√δ + 2Mε_s ≤ 1/(200 Q_max) + 1/(200 Q_max) = 1/(100 Q_max).

*Proof.* 4√δ = 4·2^{−10−⌈log₂Q_max⌉} ≤ 2^{−8}/Q_max ≤ 1/(200Q_max); 2Mε_s = 1/(200Q_max). ∎

**Convention for the rest of the proof (ideal experiment).** Let 𝒟_real be the output
distribution of DCP-SIEVE as implemented (with 𝓔'), and 𝒟_ideal the output distribution of the
same algorithm with every 𝓔' replaced by 𝓜. Run R_j applies its instrument (built with the
level-j parameters) at most 2L₀^{(j)} = Q_max^{(j)}/n times (the cap of Step A), and all other
operations are identical quantum channels and classical computations; by the standard hybrid
argument (replace the instruments one at a time, in all runs; each replacement changes the final
joint distribution by at most ‖𝓔' − 𝓜‖_⋄ in total variation),
‖𝒟_real − 𝒟_ideal‖_TV ≤ Σ_{j=0}^{J} (Q_max^{(j)}/n)·1/(100 Q_max^{(j)}) ≤ (J+1)/(100n) ≤ 1/100. Sections 4–9 analyse the ideal experiment,
in which every kept phase qubit is *exactly* |φ_k⟩ with k uniform on [0,N) (Lemma 1.3),
independent across copies.

---

## 4. Sieve invariants and yield

Fix a run R_j and consider the ideal experiment. Every list entry e has an associated binary
*tree*: a kept sample is a leaf; an entry produced at stage t from the pair (e, e') has the two
subtrees of e and e'. We write Λ_e for the set of leaves (kept samples) of e. Each leaf i
carries its data (k'_i, h_i, b_i, r_i) from Step A.

**Lemma 4.1 (invariants).** In the ideal experiment, every entry e of the list L_t (t = 0, …, m)
satisfies:
(a) |Λ_e| = 2^t, and there are signs ε_i ∈ {+1, −1} (i ∈ Λ_e) such that
    K_e = Σ_{i∈Λ_e} ε_i k'_i and K̃_e = Σ_{i∈Λ_e} ε_i K̃_i, hence K_e − K̃_e = 2^{j₀} Σ_{i∈Λ_e} ε_i b_i;
(b) the phase qubit of e is in the state |φ_{K_e}⟩ (hidden shift s_j := w_j^{−1}s mod N);
(c) K̃_e ≡ 0 (mod 2^{min(t m', j₀)}) if t ≤ m_A, and K̃_e ≡ 0 (mod 2^{j₀}) if t ≥ m_A;
(d) |K̃_e| < 2^t·N if t ≤ m_A, and |K̃_e / 2^{j₀}| < 2^{ρ_u} if t = m_A + u with 0 ≤ u ≤ m_B;
(e) in particular every entry of L_m has K̃_e/2^{j₀} ∈ {−1, 0, 1} and K_e ≡ 0 (mod 2^{j₀}).
Distinct entries of the same list have disjoint leaf sets.

*Proof.* Induction on t. For t = 0 everything holds by Step A: K̃_i = 2^{j₀+1}h_i + r_i,
|K̃_i| ≤ k'_i < N, and the qubit is |φ_{k'_i}⟩ by Lemma 1.3 and Lemma 1.4 (the measured label is
k, the relabelled one k' = w_j k mod N, and |φ_k⟩ for s equals |φ_{k'}⟩ for s_j). Disjointness
is clear. Step t → t+1: an entry of L_{t+1} comes from a pair (e, e') of L_t with equal keys
and outcome 1 in Lemma 1.2, so it is |φ_{K_e − K_{e'}}⟩ with K = K_e − K_{e'} and
K̃ = K̃_e − K̃_{e'}; (a), (b) and disjointness follow (signs of e' are negated). (c): in a
divisibility stage, equal keys mean K̃_e ≡ K̃_{e'} (mod 2^{min((t+1)m', j₀)}), so the difference
is ≡ 0 modulo it; after stage m_A − 1 the modulus is 2^{min(m_A m', j₀)} = 2^{j₀} (as m_A m' ≥ j₀),
and magnitude stages preserve divisibility by 2^{j₀} (differences of multiples). (d): in a
divisibility stage |K̃_e − K̃_{e'}| < 2·2^tN. Entering the first magnitude stage,
|K̃/2^{j₀}| < 2^{m_A}N/2^{j₀} ≤ 2^{m_A + n − j₀} = 2^{ρ₀}. In magnitude stage u, equal keys mean
⌊K̃_e/2^{j₀+ρ_{u+1}}⌋ = ⌊K̃_{e'}/2^{j₀+ρ_{u+1}}⌋, so |K̃_e/2^{j₀} − K̃_{e'}/2^{j₀}| < 2^{ρ_{u+1}}.
(e): ρ_{m_B} = max(ρ₀ − m_B m', 1) = 1 because m_B m' ≥ ρ₀ − 1; so |K̃/2^{j₀}| < 2. ∎

Lemma 4.1 also justifies the key counts stated in Section 2.3: in a divisibility stage the key
is a residue modulo 2^{min((t+1)m',j₀)} of a multiple of 2^{min(tm',j₀)}, hence takes ≤ 2^{m'}
values; in a magnitude stage the key lies in [−2^{ρ_u−ρ_{u+1}}, 2^{ρ_u−ρ_{u+1}} − 1] with
ρ_u − ρ_{u+1} ≤ m', hence takes ≤ 2^{m'+1} values. In every stage β := (number of keys) ≤ 2^{m'+1}.

**Lemma 4.2 (one stage).** Consider a stage applied to a list of L entries whose keys take
at most β values, with L ≥ 100β. Then at least P ≥ (L − β)/2 pairs are formed, the number X of
entries of the next list satisfies X ~ Bin(P, 1/2) conditionally on the pairing, and
Pr[X < L/5] ≤ 57/L.

*Proof.* Sorting by key and pairing consecutive equal keys leaves at most one unpaired entry
per key value, so P ≥ (L − β)/2 ≥ 0.495 L. By Lemma 1.2 the P outcomes are independent fair
coins whatever the labels are, so X ~ Bin(P, ½), E X = P/2, Var X = P/4. Since
L/5 ≤ P/2 − 0.0959 P (because 0.2L ≤ 0.2P/0.495 ≤ 0.4041P), Chebyshev's inequality gives
Pr[X < L/5] ≤ (P/4)/(0.0959P)² ≤ 27.2/P ≤ 27.2/(0.495 L) ≤ 57/L. ∎

**Lemma 4.3 (no abort in Steps A–C, except the count condition).** Let E_AB be the event that
in none of the J+1 runs does Step A or Step B abort. Then Pr[E_AB] ≥ 1 − 10^{−6}, and on E_AB every
run has |L_t| ≥ 5^{m−t}T_fin for all t, in particular |L_m| ≥ T_fin.

*Proof.* Step A: each acquisition is kept with probability 2^{j₀+1}h_max/N > 3/4 (Lemma 2.1(i)),
independently. The number Y of kept samples among 2L₀ acquisitions has E Y ≥ 1.5L₀ and
Var Y ≤ 2L₀/4, so Pr[Y < L₀] ≤ Pr[|Y − EY| ≥ L₀/2] ≤ (L₀/2)/(L₀²/4) = 2/L₀.
Step B: if |L_t| ≥ 5^{m−t}T_fin then |L_t| ≥ 5T_fin ≥ 100·2^{m'+1} ≥ 100β (Lemma 2.1(iii)), so by
Lemma 4.2 the stage aborts with probability ≤ 57/|L_t| ≤ 57/(5T_fin), and otherwise
|L_{t+1}| ≥ |L_t|/5 ≥ 5^{m−t−1}T_fin. Summing over m stages and J+1 ≤ n runs,
Pr[not E_AB] ≤ n(2/L₀ + 57m/(5T_fin)) ≤ n(2 + 11.4m)/T_fin ≤ (36.2 + 11.4√n)/(10⁶·2^{⌈3m/2⌉+6}),
using L₀ ≥ T_fin and m ≤ √n + 3. Since m ≥ √n − 1, 2^{⌈3m/2⌉+6} ≥ 2^{1.5√n + 4.5}, and
(36.2 + 11.4√n)/2^{1.5√n} ≤ 17 for all n ≥ 1 (the left side is decreasing in n for n ≥ 1 and
equals 16.9 at n = 1), the bound is ≤ 17/(10⁶·2^{4.5}) < 10^{−6}. ∎

---

## 5. The designated bit, and the distribution of the final true labels

**Lemma 5.1 (coins can be drawn in advance).** In the ideal experiment of one run, the joint
distribution of all classical data (labels, keys, pairings, abort flags, true and coarse labels
of all entries) is the same as in the following *classical model*: draw iid uniform labels
k_1, k_2, … ∈ [0,N) (one per acquisition) and iid fair coins γ_1, γ_2, … (one per combination);
let the algorithm use k_i as the i-th measured label and γ_t as the outcome of the t-th
combination; keep the quantum states only as bookkeeping (|φ_K⟩ for the entry with true label K).

*Proof.* In the ideal experiment, conditionally on the entire past, the i-th measured label is
uniform on [0,N) (Lemma 1.3: the probability is 1/N for every k, whatever happened before, since
each copy is a fresh ρ_s), and the t-th combination outcome is a fair coin (Lemma 1.2: the
probability is exactly ½ for all labels), while the post-measurement states are deterministic
functions of the labels and outcomes. The two processes therefore have identical one-step
conditional distributions and identical initial conditions. ∎

Fix a run R_j. In the classical model let k'_i = w_j k_i mod N (uniform on [0,N)), and define for
every acquisition i: h_i = ⌊k'_i/2^{j₀+1}⌋, b_i = ⌊k'_i/2^{j₀}⌋ mod 2, r_i = k'_i mod 2^{j₀}.
The sample is kept iff h_i < h_max. Let 𝓕 be the σ-algebra generated by
(h_i, r_i)_{i ≥ 1} and (γ_t)_{t ≥ 1}.

**Lemma 5.2 (the designated bits are fair given everything the sieve looks at).**
Conditionally on 𝓕, the bits (b_i)_{i kept} are independent and uniform on {0,1}. Moreover,
the keep/discard decisions, the coarse labels, all bucket keys, all pairings, all abort flags of
Steps A and B, the leaf sets Λ_e and the signs (ε_i) of every entry are 𝓕-measurable.

*Proof.* The map k' ↦ (h, b, r) is a bijection from [0, 2^{j₀+1}h_max) onto
[0, h_max) × {0,1} × [0, 2^{j₀}), and k' is uniform on [0,N) ⊇ [0, 2^{j₀+1}h_max). Hence for each i,
conditionally on {h_i < h_max}, the triple (h_i, b_i, r_i) is uniform on the product set, so b_i is
uniform and independent of (h_i, r_i); and conditionally on {h_i ≥ h_max}, b_i is some function of
k'_i that is never used. Different acquisitions are independent, and the coins are independent
of all labels. Therefore, conditionally on 𝓕, the kept b_i are iid uniform.
Measurability: the keep decision is "h_i < h_max"; the coarse label of a leaf is
K̃_i = 2^{j₀+1}h_i + r_i; the coarse labels of all later entries are signed sums of leaf coarse
labels, with the pairings determined by the keys (functions of coarse labels) and the surviving
entries determined by the coins; the abort flags depend on list sizes. None of these involves
any b_i. ∎

**Lemma 5.3 (final true labels are shifted binomials).** On the event that the run reaches
Step C, conditionally on 𝓕, the values K̄_e = K_e/2^{j₀} of the entries e ∈ L_m are independent,
and K̄_e = c_e + B_e where c_e := K̃_e/2^{j₀} − q_e is 𝓕-measurable, q_e := #{i ∈ Λ_e : ε_i = −1},
and B_e ~ Bin(2^m, 1/2).

*Proof.* By Lemma 4.1(a), K̄_e = K̃_e/2^{j₀} + Σ_{i∈Λ_e} ε_i b_i. Write
Σ_{i∈Λ_e} ε_i b_i = Σ_{ε_i=+1} b_i + Σ_{ε_i=−1} (1 − b_i) − q_e. Given 𝓕, the 2^m summands
b_i (ε_i = +1) and 1 − b_i (ε_i = −1) are iid uniform bits by Lemma 5.2, so their sum is
Bin(2^m, ½). Independence across e follows from the disjointness of the leaf sets. ∎

**Lemma 5.4 (central binomial probabilities).** For every integer k ≥ 1,
C(2k, k)/4^k ≥ 1/(2√k) and C(2k, k+1)/4^k ≥ 1/(4√k).

*Proof.* Let P_k = C(2k,k)/4^k = Π_{i=1}^{k} (2i−1)/(2i). For i ≥ 1, (2i−1)² = 4i² − 4i + 1 ≥
(2i)(2i−2), so ((2i−1)/(2i))² ≥ (i−1)/i for i ≥ 2, and the i = 1 factor is (1/2)² = 1/4. Hence
P_k² ≥ (1/4)·Π_{i=2}^{k}(i−1)/i = 1/(4k). For the second claim, C(2k,k+1) = C(2k,k)·k/(k+1) ≥
C(2k,k)/2. ∎

Consequently, for B ~ Bin(2^m, ½) with m ≥ 1 (k = 2^{m−1}):
Pr[B = 2^{m−1}] ≥ 2^{−(m+1)/2} and Pr[B = 2^{m−1} + 1] ≥ 2^{−(m+3)/2} =: p₂.

**Lemma 5.5 (Step C does not abort).** Let E_C be the event that, in every run, Step C finds v
with min(c(v), c(v+1)) ≥ 2M₀. Then Pr[E_AB ∩ E_C] ≥ 1 − 10^{−6} − 2·10^{−6}.

*Proof.* Work in one run on E_AB (so |L_m| ≥ T_fin), conditionally on 𝓕. Each e ∈ L_m has the
𝓕-measurable *centre* z_e := c_e + 2^{m−1}. Since K̃_e/2^{j₀} ∈ {−1,0,1} and 0 ≤ q_e ≤ 2^m,
z_e ∈ [−1 − 2^{m−1}, 1 + 2^{m−1}], a set of 2^m + 3 integers. By pigeonhole some integer z is the
centre of a group G of g ≥ T_fin/(2^m + 3) ≥ T_fin/2^{m+2} entries. For e ∈ G, by Lemma 5.3 and
Lemma 5.4, Pr[K̄_e = z | 𝓕] = Pr[B_e = 2^{m−1}] ≥ p₂ and Pr[K̄_e = z+1 | 𝓕] ≥ p₂, independently
over e ∈ G. Let X = #{e ∈ G : K̄_e = z}, a sum of g independent indicators with success
probabilities ≥ p₂: E X ≥ g p₂ and Var X ≤ E X. Now
g p₂ ≥ T_fin·2^{−m−2}·2^{−(m+3)/2} = 10⁶ n·2^{⌈3m/2⌉+6−m−2−(m+3)/2} ≥ 10⁶ n·2^{2.5} ≥ 5.6·10⁶ n ≥ 4M₀,
so Pr[X < 2M₀] ≤ Pr[X ≤ EX/2] ≤ Var X/(EX/2)² ≤ 4/EX ≤ 4/(5.6·10⁶ n). The same holds for
X' = #{e ∈ G : K̄_e = z+1}. If both X, X' ≥ 2M₀ then c(z), c(z+1) ≥ 2M₀, and the maximiser v of
Step C satisfies min(c(v), c(v+1)) ≥ 2M₀. Summing the two failure probabilities over J+1 ≤ n
runs gives ≤ 8/(5.6·10⁶) < 2·10^{−6}; add Pr[not E_AB] from Lemma 4.3. ∎

---

## 6. What the final qubits encode: the level-j fraction

Let θ := s/N ∈ [0,1) and, for j ≥ 0, t_j := {2^j θ} = (2^j s mod N)/N.

**Lemma 6.1.** In run R_j, every entry e of L_m has phase qubit |φ_{K_e}⟩ (for the shift s_j) equal to
(|0⟩ + e^{2πi K̄_e t_j}|1⟩)/√2, where K̄_e = K_e/2^{j₀} ∈ Z.

*Proof.* By Lemma 4.1(b),(e) the qubit is (|0⟩ + e^{2πi K_e s_j/N}|1⟩)/√2 with K_e = 2^{j₀}K̄_e.
Case j < a: w_j = 1, s_j = s, j₀ = j, so K_e s_j/N = K̄_e 2^j s/N ≡ K̄_e t_j (mod 1) (K̄_e is an
integer). Case j ≥ a: j₀ = a and s_j = w_j^{−1}s mod N. Write N = 2^a M_odd. Then
K_e s_j/N = K̄_e s_j/M_odd, and modulo 1 this depends only on s_j mod M_odd. Since
w_j·2^{j−a} ≡ 1 (mod M_odd), w_j^{−1} ≡ 2^{j−a} (mod M_odd), so s_j ≡ 2^{j−a}s (mod M_odd), and
K̄_e s_j/M_odd ≡ K̄_e 2^{j−a}s/M_odd = K̄_e 2^j s/(2^a M_odd) = K̄_e 2^j s/N ≡ K̄_e t_j (mod 1). ∎

---

## 7. Angle estimation (Step D)

**Lemma 7.1 (X and Y statistics).** For the qubit (|0⟩ + e^{2πi τ}|1⟩)/√2, the X-basis measurement
(H then computational measurement) gives outcome 0 with probability (1 + cos 2πτ)/2, and the
Y-basis measurement (S†, then H, then computational measurement) gives outcome 0 with probability
(1 + sin 2πτ)/2.

*Proof.* ⟨+|ψ⟩ = (1 + e^{2πiτ})/2 has squared modulus (2 + 2cos 2πτ)/4. S† maps the qubit to
(|0⟩ − i e^{2πiτ}|1⟩)/√2, and |(1 − i e^{2πiτ})/2|² = (2 + 2 sin 2πτ)/4. ∎

**Lemma 7.2 (angle from a noisy point).** Let u = (cos 2πτ, sin 2πτ) and let v ∈ R² satisfy
|v − u| ≤ d < 1. Then the angle of v (in turns, i.e. atan2(v₂,v₁)/2π) is within circular
distance d/4 of τ.

*Proof.* ⟨u, v⟩ = 1 + ⟨u, v − u⟩ ≥ 1 − d > 0, so the angle α ∈ [0, π) between u and v is < π/2.
The distance from u to the line R·v is |u| sin α = sin α, and it is ≤ |u − v| ≤ d since v lies on
that line. As sin α ≥ 2α/π on [0, π/2], α ≤ (π/2)·d radians = d/4 turns. ∎

**Lemma 7.3 (one estimate).** Let τ ∈ [0,1) and let 2M₀ copies of (|0⟩ + e^{2πiτ}|1⟩)/√2 be
measured as in Step D, M₀ in each basis, giving p̂_X, p̂_Y and the fixed-point angle α̂ with
|α̂ − atan2(ŝ, ĉ)/2π| ≤ 2^{−16} (mod 1), where ĉ = 2p̂_X − 1, ŝ = 2p̂_Y − 1 are computed exactly
(they are rationals with denominator M₀) and only the final angle is rounded. Then with
probability ≥ 1 − 5000/M₀, d(α̂, τ) ≤ 1/128.

*Proof.* p̂_X is the mean of M₀ independent Bernoulli variables with mean p_X = (1 + cos 2πτ)/2
(Lemma 7.1); Var p̂_X ≤ 1/(4M₀), so Pr[|p̂_X − p_X| ≥ 1/100] ≤ 2500/M₀ by Chebyshev, and likewise
for p̂_Y. On the complementary event, |ĉ − cos 2πτ| ≤ 0.02 and |ŝ − sin 2πτ| ≤ 0.02, so
d := |(ĉ, ŝ) − u| ≤ 0.02√2 < 0.0283, and by Lemma 7.2 the exact angle of (ĉ, ŝ) is within
0.0283/4 < 0.00708 turns of τ; adding the rounding error 2^{−16} < 0.00002 gives < 0.0071 < 1/128. ∎

The fixed-point computation of α̂ (an angle to 16 fractional bits from two rationals with
O(log n)-bit numerators and denominators) is a constant-precision task: for instance, compare
(ĉ, ŝ) against the 2^{17} grid points (cos 2πℓ/2^{17}, sin 2πℓ/2^{17}) computed to 24 bits by
Taylor series, by binary search on the angle using the sign of a 2×2 determinant. It needs
O(log² n) bit operations (arithmetic on O(log n)-bit integers, a constant number of times) and
O(log n) bits.

**Lemma 7.4 (the run output).** In run R_j, if Steps A–C did not abort, then with probability
≥ 1 − 10⁴/M₀ the output β_j satisfies d(β_j, t_j) ≤ 1/64 = η.

*Proof.* By Lemma 6.1 the 2M₀ entries with K̄ = v are copies of (|0⟩ + e^{2πi{v t_j}}|1⟩)/√2
(exactly, in the ideal experiment, and independent of each other since they are distinct
qubits whose states are determined by their labels), and those with K̄ = v+1 have τ = {(v+1)t_j}.
Lemma 7.3 applied twice: with probability ≥ 1 − 10⁴/M₀, d(α_v, {v t_j}) ≤ 1/128 and
d(α_{v+1}, {(v+1)t_j}) ≤ 1/128, and in fact both errors are < 0.0071 (proof of Lemma 7.3).
Since (v+1)t_j − v t_j = t_j and d is a metric on R/Z, d(α_{v+1} − α_v, t_j) < 0.0142; the
final rounding of β_j to 16 fractional bits adds ≤ 2^{−17}, so d(β_j, t_j) < 0.0143 < 1/64 = η. ∎

---

## 8. Stitching the levels

**Lemma 8.1 (stitching).** Let θ ∈ [0,1), t_j = {2^jθ}, and let β_0, …, β_J ∈ [0,1) satisfy
d(β_j, t_j) ≤ η = 1/64 for all j. Define θ̂_J := β_J and, for j = J−1 down to 0: let
c_0 := θ̂_{j+1}/2 and c_1 := θ̂_{j+1}/2 + 1/2, and let θ̂_j be whichever of c_0, c_1 is closer
(in d) to β_j. Then d(θ̂_j, t_j) ≤ η·2^{−(J−j)} for all j; in particular d(θ̂_0, θ) ≤ 2^{−6−J}.

*Proof.* Induction downward with ε_j := η 2^{−(J−j)} ≤ η. Base: d(θ̂_J, t_J) ≤ η. Step: suppose
d(θ̂_{j+1}, t_{j+1}) =: |e| ≤ ε_{j+1}, i.e. θ̂_{j+1} ≡ t_{j+1} + e (mod 1). The doubling map
x ↦ 2x on R/Z is exactly two-to-one, and the two preimages of θ̂_{j+1} are t_j + e/2 and
t_j + e/2 + 1/2 (mod 1), since 2t_j ≡ t_{j+1}; the two preimages are also c_0, c_1. So one
candidate c* satisfies d(c*, t_j) = |e|/2 ≤ ε_{j+1}/2, and the other satisfies
d(·, t_j) = 1/2 − |e|/2 ≥ 1/2 − ε_{j+1}/2. Then d(c*, β_j) ≤ ε_{j+1}/2 + η and the other candidate
has d(·, β_j) ≥ 1/2 − ε_{j+1}/2 − η. Because ε_{j+1} + 2η ≤ 3/64 < 1/2, the closer candidate is
c*, so d(θ̂_j, t_j) ≤ ε_{j+1}/2 = ε_j. ∎

All quantities here are dyadic rationals with at most 16 + J fractional bits (β_j has 16; each
halving adds one), so the computations are exact integer operations on O(n)-bit numbers:
O(n) comparisons and shifts of O(n)-bit integers, O(n²) bit operations in total.

**Lemma 8.2 (recovering s).** If d(θ̂_0, s/N) < 1/(2N), then ⌊θ̂_0 N + ½⌋ mod N = s.

*Proof.* θ̂_0 N is within circular distance (modulo N) less than ½ of the integer s, and the
integers are spaced 1 apart modulo N; the nearest-integer rounding of the real number θ̂_0N ∈ [0, N)
is therefore s or s ± N, and reduction modulo N gives s. ∎

With J = n − 4 and η = 1/64: d(θ̂_0, θ) ≤ 2^{−6−(n−4)} = 2^{−n−2} < 2^{−n−1} ≤ 1/(2N), since N ≤ 2^n. ∎

---

## 9. Correctness

**Theorem 9.1.** For every N ≥ 2 and every s ∈ Z/NZ, DCP-SIEVE outputs s with probability
at least 19/20.

*Proof.* For N ≤ 16 this is Section 2.1. Let N ≥ 17. In the ideal experiment (Section 3,
convention), the output is s whenever (i) E_AB ∩ E_C holds (Lemma 5.5: probability ≥ 1 − 3·10^{−6}),
and (ii) every run's output satisfies d(β_j, t_j) ≤ η. Given (i), by Lemma 7.4 each run fails
(ii) with probability ≤ 10⁴/M₀ = 1/(100n), so all J+1 ≤ n runs satisfy (ii) with probability
≥ 1 − 1/100. On (i) ∧ (ii), Lemma 8.1 gives d(θ̂_0, s/N) ≤ 2^{−n−2} < 1/(2N) and Lemma 8.2 gives the
output s. Thus Pr_ideal[output = s] ≥ 1 − 3·10^{−6} − 1/100. By the convention of Section 3,
Pr_real[output = s] ≥ Pr_ideal[output = s] − 1/100 ≥ 0.979 > 19/20. The bound is uniform in N
and s: no quantity above depends on s, and all dependence on N is through n (and through the
exact parameter values, which are functions of N computed by the algorithm). ∎

---

## 10. Resource accounting in the challenge model

All counts are worst case over every execution branch (including aborted runs: an abort only
stops a run early, so it never increases any count). Let 𝖬 denote the total number of allocated
bits and qubits at any time; every classically chosen gate, measurement and indexed classical
memory access is charged its address cost ⌈log₂(𝖬+2)⌉ in addition to its unit cost. By
Section 10.2 below, 𝖬 ≤ c·n²·2^{4√n} for an absolute c, so ⌈log₂(𝖬+2)⌉ ≤ 4√n + 2log₂ n + O(1) ≤ c'·n.
For N ≤ 16 all resources are O(1) (Section 2.1); below N ≥ 17.

### 10.1 Samples

Run R_j acquires at most 2L₀^{(j)} copies (the cap in Step A, counted whether kept or discarded).
There are J + 1 = n − 3 ≤ n runs. Hence, on every branch,
Q(N,s) ≤ Σ_j 2L₀^{(j)} ≤ 2n·max_j L₀^{(j)} ≤ 2n·2^{39}·n·2^{3.83√n} ≤ 2^{40}·n²·2^{4√n},
using Lemma 2.1(iv), which bounds L₀^{(j)} for every level j. This includes every discarded copy
and every copy of an aborted run. (In Sections 10.2–10.3, L₀ denotes max_j L₀^{(j)}.)
**Q(N,s) ≤ C·2^{4√n}·n².**

### 10.2 Space

*Quantum.* Qubits are allocated only for: (α) kept phase qubits, at most L₀ at any time (a
released qubit is deallocated; combinations only reduce the count); (β) the workspace of one
PE' instance at a time: the n-qubit value register of the copy being processed, M ancillas and
≤ c₃n arithmetic ancillas (Lemma 3.5), i.e. ≤ c(n + M) ≤ 13c·n + c'' qubits; (γ) nothing else
(Steps C, D act on existing qubits). Hence S_Q ≤ L₀ + c(13n + 103) ≤ 2^{39}n 2^{3.83√n} + O(n)
≤ C·2^{4√n}·n². **S_Q(N,s) ≤ C·2^{4√n}·n².**

*Classical.* (α) The list: at most L₀ entries, each holding a qubit address (≤ ⌈log₂ S_Q⌉ ≤ c n
bits), a true label K and a coarse label K̃ (|K|, |K̃| < 2^m N ≤ 2^{m+n}, so ≤ n + m + 2 ≤ 2n + 5
bits each), and the bucket key (≤ n + m + 2 bits): ≤ c n bits per entry, ≤ c n L₀ in total;
sorting is done by in-place heapsort (O(1) extra words). (β) Step A/C/D counters and the
multiset counts c(x) (obtained by sorting the list by K̄ and scanning; the maximisation over v
keeps O(1) words): O(n) bits. (γ) The classical description of PE': N, the constants c_l, the
Boolean circuits for the controlled additions (O(n) gates, each described by O(n) bits of
addresses), the M synthesised words of length O(log⁴(1/ε_s)) = O(n²) each (log₂(1/ε_s) ≤
3.83√n + 3 log₂ n + 60 by Lemma 2.1(iv)), the fixed Solovay–Kitaev net (O(1) bits), and O(n)-bit
dyadic angles: O(n³) bits. (δ) Stitching: J + 1 dyadic numbers of O(n) bits: O(n²) bits.
Hence S_C ≤ c n L₀ + O(n³) ≤ C·2^{4√n}·n². **S_C(N,s) ≤ C·2^{4√n}·n².**

### 10.3 Time

(α) *Per acquired copy.* Source cost n + 1. PE': ≤ c₁(Mn + M log⁴(1/ε_s)) ≤ c n³ gates and
measurements, each charged ≤ c'n address cost: ≤ c n⁴; classical control: generating the
arithmetic circuits (O(n) gates with O(n)-bit addresses per controlled addition, M of them:
O(n³) bit operations), computing the M angles (O(M²) = O(n²) bit operations), running
Solovay–Kitaev M times (O(log^{2.71}(1/ε_s)·log²(1/ε_s)) = O(n^{2.4}) each, O(n^{3.4}) in total),
each bit operation that touches memory charged ≤ c'n: ≤ c n^{4.4}; relabelling k' = w_j k mod N
and the decomposition (h, b, r): O(n²) bit operations with addresses: O(n³). Total per copy
≤ c n^{4.4} ≤ c n⁵.
(β) *Per sieve stage.* Heapsort of ≤ L₀ entries by a key of ≤ 2n+5 bits: O(L₀ log L₀) comparisons
of O(n)-bit integers, each comparison O(n) memory accesses with address cost ≤ c'n:
O(L₀·√n·n·n) = O(L₀ n³) (log L₀ = O(√n)). Pairing and the ≤ L₀/2 combinations (one CNOT, one
measurement, the label updates on O(n)-bit integers): O(L₀ n²). Per stage O(L₀ n³); m ≤ √n + 3
stages per run.
(γ) *Steps C–D per run.* Sorting by K̄ and scanning: O(L₀ n³) as in (β). 4M₀ = 4·10⁶n
measurements with O(1) Clifford gates each and address cost: O(n²); the fixed-point angle
computations: O(log² n) bit operations.
(δ) *Stitching and output.* O(n²) bit operations with addresses: O(n³).
(ε) *Start-up.* Computing n, a, M_odd, the w_j (extended Euclid, O(n²) each, n of them), the
parameters (all O(n)-bit integers; 5^m and 2^{…} are computed by repeated squaring of O(√n)-bit
exponents into ≤ 4√n + O(log n)-bit integers): O(n³). The Solovay–Kitaev net: O(1).

Summing with Q ≤ 2nL₀ copies, m ≤ √n + 3 stages and ≤ n runs:
T ≤ 2nL₀·c n⁵ + n(√n + 4)·c L₀ n³ + O(n³) ≤ c'' n⁶ L₀ ≤ c'' n⁶·2^{39}·n·2^{3.83√n} = c''2^{39}·n⁷·2^{3.83√n}.
To pass from n⁷ 2^{3.83√n} to the declared envelope n⁶ 2^{4√n} we use the elementary inequality
log₂ n ≤ 0.17√n + 30 for all n ≥ 1: the function f(n) = 0.17√n + 30 − log₂ n satisfies f(1) = 30,
f(n) → ∞, and its only stationary point is where 0.085/√n = 1/(n ln 2), i.e. √n = 1/(0.085 ln 2)
< 17, n < 289, where f(n) ≥ 30 − log₂ 289 > 21 > 0. Hence n ≤ 2^{30}·2^{0.17√n} and
T ≤ c''·2^{69}·n⁶·2^{4√n}. **T(N,s) ≤ C·2^{4√n}·n⁶.**

### 10.4 Growth indices

For B(n) = 2^{4√n} n^r with r ∈ {2, 6}: log₂ B(n) = 4√n + r log₂ n, so
log₂ log₂ B(n) = ½ log₂ n + log₂(4 + r log₂ n/√n) for n ≥ 2, and the second term lies in
[2, log₂(4 + 2r)] because 0 ≤ log₂ n/√n ≤ 2 for all n ≥ 1 (the maximum of log₂ n/√n is
2 log₂ e/e < 1.07, attained at n = e²). Therefore
g(B) = limsup (½ log₂ n + O(1))/log₂ n = 1/2 exactly. Multiplying B by an absolute constant C
does not change g. The four resource indices are [1/2, 1/2, 1/2, 1/2]; only time is a numeric
objective, so the published vector is [1/2].

### 10.5 Theorem

**Theorem 10.1.** There is an absolute constant C such that for every N ≥ 2 and every s ∈ Z/NZ,
on every execution branch of DCP-SIEVE,
T(N,s) ≤ C·2^{4√n}·n⁶, S_C(N,s) ≤ C·2^{4√n}·n², S_Q(N,s) ≤ C·2^{4√n}·n², Q(N,s) ≤ C·2^{4√n}·n²,
with n = ⌈log₂ N⌉, jointly with Theorem 9.1. The structured declarations of `submission.json`
(coefficient 1, exponent term 4·n^{1/2}, nPower 6 resp. 2, logPower 0) are exactly these
envelopes, read in big-O notation.

*Proof.* Sections 10.1–10.3 for N ≥ 17; for N ≤ 16 all quantities are O(1) and are covered by
enlarging C. ∎

---

## 11. Fractional error tolerance

The correctness and resource proofs above assume that every acquired copy is an independent
ideal coset state ρ_s for the same N and s (Lemma 1.3 and the independence used in Lemmas 4.3,
5.1–5.3, 7.3 rely on it). They therefore establish the fractional guarantee ε(n) = 0 for the
same algorithm and configuration, jointly with all four bounds. No positive tolerance is
claimed; this does not assert that the algorithm's true tolerance is zero.

---

## 12. Remarks for the reviewer

* *Where the general-N difficulty is handled.* Kuperberg's Algorithm 2 (2005) sieves on the
  high bits of the labels and says the final parity analysis is "a bit tricky". We avoid the
  parity analysis entirely: the sieve reads only the coarse labels K̃ (Lemma 5.2), so the final
  true label is a known integer plus a Bin(2^m, ½) variable (Lemma 5.3), and the pair (v, v+1)
  needed for Step D is found by pigeonhole over the 2^m + 3 possible centres (Lemma 5.5).
  The 2-part of N is handled by the divisibility stages, the odd part by relabelling (Lemma 6.1).
* *Why no reduction mod N inside the sieve.* Labels are integers; Lemma 1.2 holds for integer
  labels because ω^N = 1. This is what makes "divisible by 2^{j₀}" and "small" meaningful for
  every N.
* *Constants.* The exponent 4 and the degrees are deliberately loose upper bounds (e.g. the
  factor 5^m could be 4^m(1+o(1)) with a Chernoff bound, and T_fin could lose a 2^{m/2} factor).
  They do not affect the growth index.
