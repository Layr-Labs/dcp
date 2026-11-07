# RLS-G2M: a two-tier robust low-bit sieve with threshold-ladder robust quantum search, O(2^{n/4} n⁴) work, adaptive malformed-copy tolerance 1/10

This file and `appendix.md` together are the complete proof of all five claims in `submission.json`. They
describe one algorithm, **RLS-G2M** (below simply RLS), with one fixed parameter rule, and prove for every
integer N ≥ 2, every s ∈ Z/NZ, with n = ceil(log₂ N), and every adversary of the error model of Section 5
(which contains the clean problem as the adversary that corrupts nothing):

* the output equals s with unconditional probability at least 9/10 (> 2/3);
* total work T = O(2^{n/4} n⁴);
* peak classical space S_C = O(2^{n/4} n) bits;
* peak quantum space S_Q = O(2^{n/4} n) qubits;
* acquired source copies Q = O(2^{n/4}); Q is a fixed function of N, the same on every branch;
* fractional error tolerance ε(n) = 1/10: at most floor(Q/10) acquired copies may be malformed, at
  adversarially and adaptively chosen positions, with arbitrary, possibly entangled contents.

All constants are absolute (independent of N, s, the adversary and all outcomes). Every loop of RLS has a
length bounded by a fixed function of N, so the four resource bounds hold on every execution branch
whatever the copies contain. Logarithms are base 2 unless written ln. All four growth indices equal 1; the
time envelope has exponent n/4.

**Idea.** RLS-G2M is our RLS-G2R (484bc509; tolerance 1/13 at 2^{n/4}·poly) with the same sieve, a sharper analysis of
the malformed records and a search that can use it. (i) All Q copies are acquired before the first measurement, so the
adversary, which sees only outcomes obtained before each delivery, chooses blind, and a uniform permutation spreads
its copies over all slot blocks. (ii) The SLS splice (59facd77) turns the copies of the right grid guess g* into exact
coset states of Z/2^{t}Z for the remaining t high bits of s′ = (s − g*) mod N; wrapped copies are treated as
malformed. (iii) With b = ceil(n/4), tier 1 runs two low-bit sieve stages of b bits on Z/2^nZ and then a robust
shadow-score quantum search (our ROB-G2, 55a6ce76) finds the low d₁ = n − 2b ≤ 2b bits of s′ with O(2^{d₁/2}) ≤
O(2^{n/4}) oracle calls per threshold; tier 2 does the same with zero stages on the remaining 2b bits, finding the
last 2b bits. (iv) *New here.* A record with a good and a bad leaf (a *mixed* record) has a label whose examined high
part is exactly uniform, and its qubit is a state that does not depend on that label, rotated by the label's phase
(Lemma U, phase covariance); so its conditional score mean is exactly 0 at every wrong candidate (Lemma X). Only
*bad-only* records (all leaves bad) can raise a wrong candidate. With n_x mixed and n_o bad-only records among K, the
target's score exceeds every other one by K(1/2 − 2η − 2δ_s) − n_x − (3/2)n_o (Theorem M); the search walks down a
ladder of thresholds ι/256, ι = 257, …, 1, and returns at the first threshold where it finds a marked candidate (Lemma
Sr). Counting good, mixed and bad-only records through the two stages with a weighted potential (Lemma S₁) gives
tolerance 1/10; our earlier count (RLS-G2R, 484bc509) allowed 1/13.

Notation. frac(φ) ∈ [0,1); |φ|∘ = min_{z∈Z}|φ − z| (circular distance). bitlength(x) is the number of
binary digits of an integer x ≥ 1, so 2^{bitlength(x)} > x and e^{−bitlength(x)} < 2^{−bitlength(x)} < 1/x.
round(z) = floor(z + 1/2). For a modulus M′ and an integer v, the *label-v qubit* for secret σ is
φ_σ(v) = (|0⟩ + e^{2πivσ/M′}|1⟩)/√2; only v mod M′ matters.

## 1. Exact primitives (Clifford+T, fresh |0⟩, computational-basis measurement)

The exact primitives A1–A5 (gate set and controlled gates, constant adders and comparators, in-place
permutations and their controlled versions, the phase test, fair bits and the combination step) are
given in App. E of `appendix.md`, which is part of this proof.

**Further primitives.** The register arithmetic P3a–P3e (constant adders mod 2^p, register adders mod 2^w,
comparisons with constants, multi-controlled X and table reads), the cosine table (Lemma T), the oracles 𝒪_ι and
the diffusion 𝒟 are given in App. A–C of `appendix.md`, which is part of this proof.

**Cost convention.** Let 𝔐 be the number of allocated bits plus qubits. Section 8 shows
𝔐 = O(2^{n/4} n), so a classically indexed access or classically addressed gate costs
A = ceil(log₂(𝔐 + 2)) = O(n) bit operations for its address. Every gate, measurement,
initialisation and classical bit operation below is charged O(A).

## 2. Coset states of Z/M′Z as labelled qubits

For a modulus M′ and σ ∈ Z/M′Z let ρ^{M′}_σ = (1/M′)Σ_{z<M′}|ψ_z⟩⟨ψ_z|,
ψ_z = (|0,z⟩ + |1,(z+σ) mod M′⟩)/√2. With χ_k = M′^{−1/2}Σ_y e^{2πiky/M′}|y⟩ we have
|y⟩ = M′^{−1/2}Σ_k e^{−2πiky/M′}χ_k, so ψ_z = (2M′)^{−1/2}Σ_k e^{−2πikz/M′}(|0⟩ + e^{−2πikσ/M′}|1⟩) ⊗ χ_k.
Averaging over z removes the cross terms k ≠ k′, and with u = −k mod M′

  ρ^{M′}_σ = (1/M′) Σ_{u∈Z/M′Z} |φ_σ(u)⟩⟨φ_σ(u)| ⊗ |χ_{−u}⟩⟨χ_{−u}|.                      (2.1)

So ρ^{M′}_σ is exactly a uniformly random classical label u together with the product state
φ_σ(u) ⊗ χ_{−u}; all statistics below are computed in this decomposition by linearity. If
g_a|y⟩ = |(y + a) mod M′⟩, then g_aχ_{−u} = e^{2πiua/M′}χ_{−u}. Hence the **kickback test** "fresh |0⟩,
H, then g_a on the register controlled by this qubit" leaves the register unchanged and puts the
control in (|0⟩ + e^{2πiua/M′}|1⟩)/√2. Repeated tests on one register are independent given u, and
they never touch the first qubit.

## 3. Lemma P (label reading) and procedure F_t

Lemma P, procedure F_t and Corollary F are given in App. F of `appendix.md`, which is part of this proof.

## 4. Parameters (exact integer arithmetic, computed from N)

For **n ≥ 256**:

* **R** = 2 (stages of tier 1); **b** = ceil(n/4) (sieve bits per stage), so n/4 ≤ b ≤ n/4 + 1 and b ≥ 64.
* **T** = 2 tiers ℓ = 1, 2 with R_ℓ = R − 2(ℓ − 1) = 2, 0 stages, d₁ = n − 2b and d_ℓ = 2b for ℓ ≥ 2, low-bit
  counts j₁ = 0 and j_{ℓ+1} = j_ℓ + d_ℓ (so j_ℓ = d₁ + 2b(ℓ − 2) for ℓ ≥ 2), and t_ℓ = n − j_ℓ; then t_ℓ − R_ℓb = d_ℓ,
  j₂ + d₂ = n, n/2 − 2 ≤ d₁ ≤ 2b, d₁ ≥ 127 and 2b ≥ 128, so every d_ℓ ≥ 127.
* **M** = 2^{b+11} (leaves of tier 1 per guess).
* **K_ℓ** = 2^{20}(d_ℓ + 8) (records of the search of tier ℓ).
* **G** = 2^{12} (grid size); grid points g_i = floor(iN/G) for i = 0, …, G−1. Since N ≥ 2^{255} > G, the g_i are
  distinct.
* **k** = 256·bitlength(100G) = 4864 (copies per test).
* **Q** = G(M + K₂ + k) (copies acquired).
* L₁ = bitlength(1600(n+1)Q); **r₁** = 200L₁ (tests per bit level i and offset m′ in F_t).
* **κ** = 2·bitlength(Q) + 10 (sort-key bits); **κ_W** = 2·bitlength(M) + 10 (sample-key bits).
* Score: **q** = 24 (angle bits); **p** = q + 1 + bitlength(n) (phase bits); for a search with K records,
  **w** = bitlength(K) + 29 (accumulator width); **threshold ladder ϑ_ι = ι/256** for ι = 257, 256, …, 1.
* Search over d qubits: K_G = floor(2^{d/2}) (the integer square root of 2^d), k_G = floor(785K_G/1000), at most 7
  repetitions per threshold.

Analysis constants (not used by the algorithm): ε = 1/10, δ = 1/1024, τ_h = 2^{−10}, ȳ = ε + 2·2^{−10} = 261/2560,
δ_s = 1/400, τ_s = 1/800, τ_T = 2^{−24} (table accuracy), η = 3π2^{−24} + τ_T < 6.22·10^{−7}, R₀ = 1 + τ_T,
φ̄ = 0.489.

For **n < 256**: K_s = 2^{20}; Q_s = N·K_s; κ′ = 2·bitlength(Q_s) + 10 (Section 6.10).

## 5. Error model (adaptive malformed copies)

Copies are delivered one at a time in acquisition order j = 1, …, Q (Q is given by Sections 4 and 6.1).
An **adversary** knows N, s, the full description of RLS, and every measurement
outcome obtained by RLS before copy j is delivered; it holds an arbitrary private quantum system E which
it may measure and process. Before copy j is delivered it chooses c_j ∈ {clean, malformed}, as a function
of that information and its own outcomes; on every branch at most floor(εQ) copies are malformed,
ε = 1/10.

* A **malformed** copy is an arbitrary (n+1)-qubit system supplied from E. It may be in any state,
  entangled with the rest of E and hence with other malformed copies, and may depend on everything
  listed above. It is not entangled with clean copies or with RLS's workspace, ancillas or fair-bit qubits.
* A **clean** copy is, at the moment of its delivery, a fresh ρ_s in tensor product with everything else
  (E, all other copies, RLS's workspace).
* The adversary interacts with RLS only by supplying copies; after delivery it has no access to the copy
  or to RLS's quantum or classical systems. All measurements (RLS's and the adversary's) have countably
  many outcomes.

RLS is not told which copies are malformed. The clean problem is the case in which no copy is malformed.
This section restates the error_model string of the fifth claim in `submission.json`, which governs.

## 6. Algorithm RLS

### 6.1 Acquisition and permutation (n ≥ 256)

1. Acquire Q copies, one after another, and hold all of them. **No measurement and no fair bit is
   made before the last copy has been delivered.**
2. Draw Q keys Y_1, …, Y_Q of κ fair bits each (A4). If two keys are equal, measure everything and
   output 0. Otherwise sort the copies by key (merge sort on (key, index) pairs) and let π(p) be the
   index of the copy of rank p (p = 1, …, Q). The table p ↦ π(p) is stored.

### 6.2 Slot layout

Ranks are grouped into G consecutive blocks of M + K₂ + k ranks, block i belonging to guess g_i. Inside block i,
the first M ranks form the **tier-1 block**, the next K₂ the **tier-2 block**, and the last k the **test block**.

### 6.3 LEAF_t (one held copy, guess g, low-bit count j, t = n − j, current σ_low)

1. Controlled on the first qubit c, apply P1 with a = (N − g) mod N (subtract g mod N).
2. Controlled on c, add (2^n − σ_low) mod 2^n to the register (A2, mod 2^n).
3. Measure the low j register qubits and release them. Call the remaining t qubits the register.
4. Draw t fair bits (A4) forming ζ ∈ [0, 2^t); add ζ mod 2^t to the register (A2, uncontrolled); then
   erase ζ (no later step reads it, or the outcomes of step 3).
5. Run F_t on the register, giving û ∈ [0, 2^t); measure and release the register.

Return the record (qubit c, label x = û).

### 6.4 TIER(ℓ) (guess g, the copies of its tier-ℓ block, current σ_low ∈ [0, 2^{j_ℓ}))

Let (t, R_ℓ, d) = (t_ℓ, R_ℓ, d_ℓ) of Section 4.

1. *Leaves.* Apply LEAF_t with low-bit count j_ℓ and this σ_low to each copy of the block (t = n − j_ℓ), giving
   records (qubit, label x ∈ Z/2^tZ) in rank order: the list W_0.
2. *Sieve stages.* For m = 1, …, R_ℓ: every label of W_{m−1} is ≡ 0 mod 2^{(m−1)b}; the key of x is
   floor(x/2^{(m−1)b}) mod 2^b. Sort W_{m−1} stably by key (counting sort with 2^b counters). Within each key group,
   in list order, form pairs (1st, 2nd), (3rd, 4th), …, and release a last unpaired record. For each pair (a, a′), in
   list order of a, apply A5 with a as control; on outcome 1 output the record (qubit a, label (x_a − x_{a′}) mod 2^t),
   on outcome 0 release both qubits. W_m = the outputs, in list order of their first members. Every label of W_m is
   ≡ 0 mod 2^{mb}. For a record of W_{R_ℓ} write w = label/2^{R_ℓb} ∈ [0, 2^d) (t − R_ℓb = d).
3. *Sample.* If R_ℓ = 0 (tier 2), keep all K₂ records of W_0, in rank order. If R_ℓ ≥ 1: if |W_{R_ℓ}| < K_ℓ, release
   all records of W_{R_ℓ} and declare the guess failed; otherwise draw a key of κ_W fair bits for every record of
   W_{R_ℓ}; on a tie, release all records of W_{R_ℓ} and declare the guess failed; otherwise keep the K_ℓ records with
   the smallest keys, in key order (a uniformly random K_ℓ-subset in uniformly random order), and release the rest.
4. *Records.* For the j-th kept record (j = 1, …, K_ℓ): draw 3 fair bits forming m′_j; apply P2 (= A3) with m′_j to
   its qubit, giving b_j; store (w_j, m′_j, b_j).
5. *Search* (Section 6.7) with d = d_ℓ and these K_ℓ records, giving θ̂_ℓ ∈ [0, 2^{d_ℓ}) or "fail" (then the guess
   failed). Otherwise replace σ_low by σ_low + 2^{j_ℓ}θ̂_ℓ ∈ [0, 2^{j_ℓ + d_ℓ}).

### 6.5 One guess

For guess g: put σ_low = 0 and run TIER(1) and TIER(2), in this order, on the two tier blocks of the guess, stopping
as soon as the guess failed. As j_{ℓ+1} = j_ℓ + d_ℓ (ℓ = 1), each tier starts with σ_low ∈ [0, 2^{j_ℓ}). If both tiers
succeed, the **candidate** is s̃ = σ_low ∈ [0, 2^n) (j₂ + d₂ = n).

### 6.6 The score of a search

Given d and K records (w_j, m′_j, b_j) with w_j ∈ [0, 2^d): for i = 0, …, d−1 let c_{j,i} = floor(2^p frac(2^i w_j/2^d))
(the controller reads the p bits of w_j at positions d−i−p, …, d−i−1, the missing low positions zero-filled:
c_{j,i} = floor(w_j 2^{p+i−d}) mod 2^p, O(p) indexed bit reads). For τ ∈ [0, 2^d)
with bits τ = Σ_i τ_i 2^i define

  V_j(τ) = (Σ_{i<d} τ_i c_{j,i}) mod 2^p,  h_j(τ) = floor(V_j(τ)/2^{p−q}),  k_j(τ) = (h_j(τ) − 2^{q−3}m′_j) mod 2^q,
  Σ(τ) = Σ_{j=1}^{K} (−1)^{b_j} c_{k_j(τ)} ∈ Z,  S(τ) = Σ(τ)/2^{25} = Σ_j Z̃_j(τ),  Z̃_j(τ) = (−1)^{b_j} table[k_j(τ)],

with the table c_k of App. B (table[k] = c_k/2^{25}), and for ι = 1, …, 257 the marking function f_ι(τ) = 1 iff
256·Σ(τ) > ι·2^{25}·K (i.e. S(τ) > ϑ_ιK). Each f_ι is evaluated classically for one τ in O(K d p) bit operations.

### 6.7 Search

For ι = 257, 256, …, 1, in this order, do the following at most 7 times: prepare d fresh qubits in |0^d⟩, apply H to
each, apply 𝒢_ι = 𝒟·𝒪_ι (App. C, for this score and f_ι) exactly k_G times, and measure, giving τ̂; evaluate f_ι(τ̂)
classically; if f_ι(τ̂) = 1 return τ̂. If no run returns, return "fail". A search makes at most 257·7 = 1799 runs.

### 6.8 TEST(v) (the k copies of the test block of guess i)

For each copy: controlled on its first qubit, apply P1 with a = (N − v) mod N (subtracting v from the register);
apply H to the first qubit and measure it; release the copy. Let Z be the number of outcomes 0. Accept iff 4Z ≥ 3k.

### 6.9 Output (n ≥ 256)

For i = 0, …, G−1: run guess g_i (6.5); if it does not fail and its candidate s̃ satisfies s̃ < N, run
TEST((s̃ + g_i) mod N) on the test block of guess i, and if it accepts, output (s̃ + g_i) mod N and halt. If no
candidate is accepted, output 0. (Copies of unused blocks are measured and released at the end; they were acquired in
step 6.1.)

### 6.10 Small inputs (n < 256)

Acquire Q_s = N·K_s copies and hold them (no measurement before the last delivery). Draw Q_s keys of κ′ fair bits; on a
tie output 0; otherwise sort as in 6.1, and give candidate v ∈ [0, N) the K_s copies of ranks vK_s + 1, …, (v+1)K_s.
For each v run the test of 6.8 with this v on its K_s copies (k replaced by K_s), giving Z_v. Output the smallest v
with 4Z_v ≥ 3K_s, or 0 if there is none.

## 7. Correctness

### 7.1 Delivery before measurement, and the permutation

**Lemma N (no information).** In RLS the adversary's choices c_1, …, c_Q, the contents of the malformed
copies, and its operations on E up to the last delivery are made without any measurement outcome of
RLS. After the last delivery, conditioned on the adversary's own outcomes up to that time (a history h
of positive probability, outcome sets being countable), the malformed set 𝓜_h ⊆ {1,…,Q} is fixed,
|𝓜_h| ≤ floor(εQ), and the joint state of the copies and E is ⊗_{j∉𝓜_h} ρ_s ⊗ ω_h for some state
ω_h of the malformed copies and E, in tensor product with RLS's fresh qubits.

*Proof.* RLS makes no measurement until after the last delivery (6.1 step 1), so "every measurement
outcome obtained by RLS before copy j is delivered" is empty for every j, and each c_j is a function
of the adversary's own outcomes only. Each clean copy is, at its delivery, ρ_s in tensor product with
everything else (Section 5), and RLS holds it untouched until after the last delivery; a later delivery
is a new system and does not act on it. The malformed copies are not entangled with clean copies or with
RLS's systems. The adversary has no access to anything of RLS after delivery, so whatever it does with E
later acts only on E, which RLS never touches; we may trace E out at the end. ∎

We fix such an h from now on; all probabilities below are conditional on h and then averaged, so the
bounds hold for every adversary.

*Remark.* Delaying every measurement until the last delivery is part of the algorithm. Its cost (all Q copies
are held) is charged in the quantum-space claim. Nothing is claimed beyond the model of Section 5, whose
adversary sees only outcomes obtained before each delivery.

**Lemma Π (uniform slots).** The tie event of 6.1 step 2 has probability < 2^{−11}. Conditioned on no
tie, the rank map π is a uniformly random permutation of {1,…,Q}, independent of 𝓜_h and ω_h. Hence the
set π^{−1}(𝓜_h) of ranks holding malformed copies is a uniformly random subset of size |𝓜_h|.

*Proof.* The keys are i.i.d. uniform on [0, 2^κ) and independent of the copies and E (fresh qubits).
P(tie) ≤ C(Q,2)2^{−κ} < Q²2^{−κ−1} ≤ 2^{2·bitlength(Q)}2^{−2·bitlength(Q)−11} = 2^{−11}. Given that all
keys are distinct, every ordering of the copies is equally likely by exchangeability of the keys. ∎

### 7.2 Concentration tools

**Lemma A (Azuma–Hoeffding).** Let D_1, …, D_m be random variables adapted to a filtration (ℋ_i),
with E[D_i | ℋ_{i−1}] = 0 and a_i ≤ D_i ≤ a_i + 1 for ℋ_{i−1}-measurable a_i, where m is fixed given
ℋ_0. Then P(Σ_i D_i ≥ λ | ℋ_0) ≤ e^{−2λ²/m} and P(Σ_i D_i ≤ −λ | ℋ_0) ≤ e^{−2λ²/m} for λ > 0.

*Proof.* Fix i and a history; X = D_i ∈ [a, a+1] with E[X] = 0. Convexity of x ↦ e^{θx} gives
E[e^{θX} | ℋ_{i−1}] ≤ (a + 1)e^{θa} − a e^{θ(a+1)} = e^{ψ(θ)}, ψ(h) = −q₀h + ln(1 − q₀ + q₀e^h) with
q₀ = −a ∈ [0,1]; ψ(0) = ψ′(0) = 0 and ψ″ ≤ 1/4, so ψ(θ) ≤ θ²/8. Iterating the tower property,
E[e^{θΣD_i} | ℋ_0] ≤ e^{mθ²/8}; Markov's inequality with θ = ±4λ/m gives both bounds. ∎

We use it for sums of coins: if X_1, …, X_m ∈ {0,1} satisfy P(X_i = 1 | ℋ_{i−1}) = 1/2, then
P(ΣX_i ≥ m/2 + λ) and P(ΣX_i ≤ m/2 − λ) are ≤ e^{−2λ²/m}.

**Lemma H (sampling without replacement).** Let S be a fixed set of m_S ranks and X the number of
malformed ranks in S. Conditioned on no tie, P(X ≥ (ε + τ)m_S) ≤ e^{−2τ²m_S} for τ > 0.
*Proof.* By Lemma Π, X is hypergeometric: the number of marked items in a uniform m_S-subset of Q items of
which |𝓜_h| ≤ εQ are marked. Hoeffding (JASA 58 (1963), Theorem 4 with Theorem 1, Section 6) shows that
the bound P(X/m_S − μ ≥ τ) ≤ e^{−2τ²m_S} for sums of independent [0,1] variables with mean μ also holds for
sampling without replacement; here μ = |𝓜_h|/Q ≤ ε. This is the one external result used. ∎

**Lemma H′ (hypergeometric tails).** If X is the number of marked items in a uniform m-subset of a
population of size N₀ with K₀ marked items, then P(X ≥ mK₀/N₀ + τm) ≤ e^{−2τ²m}. *Proof.* Hoeffding (JASA 58
(1963), Theorem 4 with Theorem 1, Section 6), as in Lemma H. ∎

**Notation in Section 7.** G_m and P_m count good and bad records, unrelated to the grid size G, the grid points
g_i, the phase-bit count p and the wrap probability ϖ; s is the secret, s′ = (s − g*) mod N.

### 7.3 The splice and exact leaves

**Lemma W (splice).** Fix g and let s′ = (s − g) mod N. After LEAF step 1 a clean copy is the uniform
mixture over x ∈ [0,N) of (|0,x⟩ + |1,(x + s′) mod N⟩)/√2. Hence it equals (1 − ϖ)ρ^{nw} + ϖρ^{w}
with ϖ = s′/N, where ρ^{nw} (resp. ρ^{w}) is the uniform mixture of these pure states over
x < N − s′ (resp. x ≥ N − s′; if s′ = 0 then ϖ = 0 and only ρ^{nw} occurs). For x < N − s′ the second branch
holds the integer x + s′ < N. Some grid
point g* = g_{i*} has s′ < N/G + 1, hence ϖ < 1/G + 1/N < 2/G.

*Proof.* (x + s − g) mod N = (x + s′) mod N. With g_G := N, s lies in some [g_i, g_{i+1}), and
g_{i+1} − g_i < N/G + 1; take i* = that i. As N > G, 1/N < 1/G. ∎

**Lemma S (exact leaf).** Fix g, j, t = n − j, and suppose σ_low = s′ mod 2^j. Let σ_hi = floor(s′/2^j).
Feed LEAF_t a copy whose state after step 1 is ρ^{nw}. Conditionally on the outcomes of step 3, and with ζ not
recorded, the state of (c, register) after step 4 is exactly ρ^{2^t}_{σ_hi}.

*Proof.* Fix x < N − s′. After step 2 the state is |0,x⟩ + |1, x + s′ − σ_low⟩ (normalised), where
s′ − σ_low = 2^jσ_hi ≥ 0 and x + s′ − σ_low < N ≤ 2^n, so the addition mod 2^n does not wrap. Both
branches share the low j bits x mod 2^j, so step 3 leaves |0, x_h⟩ + |1, x_h + σ_hi⟩ with x_h = floor(x/2^j)
and x_h + σ_hi < 2^t. For each fixed x_h, averaging step 4 over uniform ζ gives (1/2^t)Σ_z|ψ_z⟩⟨ψ_z| with
ψ_z = (|0,z⟩ + |1,(z + σ_hi) mod 2^t⟩)/√2, which is ρ^{2^t}_{σ_hi}. Conditionally on the step-3 outcome
the state is a mixture of such x_h-states, so it equals ρ^{2^t}_{σ_hi}. No later step reads ζ or the
step-3 outcome, so by linearity the law of everything that follows is the one obtained from this
averaged state. ∎

By (2.1), such a leaf is a uniform label u ∈ Z/2^tZ with c in the state φ_{σ_hi}(u) and the register in
χ_{−u}. F_t touches only the register and fresh qubits, so after LEAF_t, c is still φ_{σ_hi}(u), in
product with everything else given u, and by Corollary F with r = r₁,
P(û ≠ u | u, past) ≤ 16(J+1)e^{−L₁} < 16(n+1)/2^{L₁} < 1/(100Q).

### 7.4 The good guess, good leaves and the genie run

Fix the guess g* = g_{i*} of Lemma W and put s′ = (s − g*) mod N, ϖ = s′/N < 2/G. By Lemma W we may (by
linearity) realise every clean copy of the two tier blocks of guess i* as ρ^{nw} or ρ^{w} by an independent coin W
with P(W = 1) = ϖ. A copy of these blocks is **good** if it is clean and W = 0, and **bad** otherwise. For ℓ = 1, 2
put θ_ℓ = floor(s′/2^{j_ℓ}) mod 2^{d_ℓ}. As j₁ = 0, j_{ℓ+1} = j_ℓ + d_ℓ and j₂ + d₂ = n, we have
s′ mod 2^{j_ℓ + d_ℓ} = (s′ mod 2^{j_ℓ}) + 2^{j_ℓ}θ_ℓ for each ℓ, and s′ = Σ_{ℓ=1}^{2} 2^{j_ℓ}θ_ℓ. Let E_ℓ be the event
that tier ℓ of guess i* is run and starts with σ_low = s′ mod 2^{j_ℓ} (for ℓ = 1: that guess i* is run).

The **genie run** is the modified process (an analysis device, not an event) in which, in tier ℓ of guess i* on the
event E_ℓ (ℓ = 1, 2), the label returned by F_t for every good leaf is replaced by its true label u of Lemma S (F's
tests are still performed and their outcomes ignored); otherwise it follows the rules of RLS. No step of RLS reads ζ,
so in the analysis step 4 of every leaf is replaced by its ζ-average (the same channel): ζ is not a random variable of
either run, and "the past", "all outcomes" and 𝒦_0 never include it. Realise all measurement outcomes of both runs
from one common sequence of independent uniforms, through their conditional laws given the past. The two runs take
the same actions until the first good leaf with û ≠ u. Guess i* processes at most M + K₂ ≤ Q leaves, each good leaf
whose label is replaced with P(û ≠ u | past) < 1/(100Q), so the runs differ with probability < 1/100.

### 7.5 Structure of the tiers in the genie run

Consider tier ℓ of guess i* on the event E_ℓ, in the genie run: t = t_ℓ, R_t = R_ℓ stages, and stage m (1 ≤ m ≤ R_t)
reads the label bits l_{m−1}, …, l_m − 1 with l_m = mb, so its width is b_m = b and l_0 = 0; W_0 is the list of leaves
and W_m the output of stage m. In 7.5–7.7, "the past" and every conditioning exclude, in addition, the F_t outcomes of
the tier's good leaves (the genie run never reads them, so by linearity we may average over them); step-3 outcomes may
be included or not (Lemma S holds conditionally on them, with σ_low = s′ mod 2^{j_ℓ} and σ_hi = floor(s′/2^{j_ℓ})). A
record is **good** if every leaf of its combination tree is a good leaf, **bad-only** if every leaf of its tree is bad,
and **mixed** otherwise; it is **bad** if it is not good, and **free** if it is not bad-only (its tree has a good leaf).
G_m, X_m and B_m are the numbers of good, mixed and bad-only records of W_m, and P_m = X_m + B_m. A leaf is good or
bad-only, and the output of a pair is good iff both members are good, bad-only iff both are bad-only, and mixed otherwise.

*Phase rotations.* For real α let D(α) = |0⟩⟨0| + e^{iα}|1⟩⟨1| (one qubit), and for a label x let α_x = 2πxσ_hi/2^t, so
φ_{σ_hi}(x) = D(α_x)|+⟩ with |+⟩ = (|0⟩ + |1⟩)/√2; α_x mod 2π depends only on x mod 2^t, and α_{x−x′} ≡ α_x − α_{x′}.
Two identities hold on every basis state: (I1) for a computational-basis outcome c, ⟨c|D(α) = e^{iαc}⟨c|; (I2) for A5 on
a pair (a, a′) with outcome o, ⟨o|_{a′}·CNOT_{a→a′}·(D(α) ⊗ D(α′)) = e^{iα′o}·D(α + (−1)^oα′)·⟨o|_{a′}·CNOT_{a→a′}, the
D on the right acting on a (both sides map |c, e⟩ to e^{i(αc + α′e)}|c⟩ if e = o ⊕ c = o + (−1)^o c, and to 0 otherwise).
So the phase factor of a measured qubit changes neither outcome probabilities nor the post-measurement state of the other
systems, and on outcome 1 A5 turns the factors of its inputs into the factor D(α_{x_a − x_{a′}}) of its output, up to a
global phase.

**Lemma C (fair coins).** Let a pair contain at least one good record. Conditioned on the past (in the sense
above) and on the labels of all free records, the outcome of its A5 measurement is 0 or 1 with probability
exactly 1/2; in particular it is independent of the good members' labels. If both records are good, then on
outcome 1 the output qubit is φ_{σ_hi}(x_a − x_{a′}), in tensor product with everything else.

*Proof.* By invariant (J) of Lemma U at the preceding stage (Lemma U at stage m uses Lemma C only for the
pairs of stage m, so there is no circularity), a good record's qubit is φ_{σ_hi}(x) for its label x, in
tensor product with all other systems given the past and the free labels. Its computational-basis diagonal is (1/2,
1/2). Let ρ be the joint state of the pair (and the rest) before the CNOT, and let o be the measured value. If a′ is
good, P(o) = Σ_c ⟨c|ρ_a|c⟩·⟨o⊕c|ρ_{a′}|o⊕c⟩ = Σ_c ⟨c|ρ_a|c⟩/2 = 1/2; if a is good, P(o) = Σ_c (1/2)⟨o⊕c|ρ_{a′}|o⊕c⟩ =
1/2. Because the good qubit is in tensor product with everything else, the same computation holds conditioned on any
event of the other systems. For two good qubits A5 gives the stated outputs with probability 1/2 each,
whatever x_a, x_{a′} are. ∎

Let 𝒦_0 be the σ-algebra generated by: h; the rank map; everything before the tier (all outcomes of
earlier guesses and tiers); the coins W; the identity of the good leaves; and every outcome and label
of the bad leaves of the tier. It does not contain the step-3 outcomes, ζ or F's outcomes of the good
leaves of this tier, which no later step reads in the genie run. For m ≥ 1, let 𝒦_m be generated by 𝒦_{m−1}, the
stage-m keys of all records of W_{m−1}, the pairing, all stage-m A5 outcomes, the stage-m release
outcomes, and the labels of the bad-only records of W_m (not those of the mixed ones). The type (good, mixed or
bad-only) of every record of W_m is 𝒦_m-measurable.

**Lemma U (exact uniformity and phase covariance).** For m = 0, …, R_t: (U) conditioned on 𝒦_m, the values
floor(x_r/2^{l_m}) for the free records r of W_m are independent and uniform on [0, 2^{t−l_m}); and (J) conditioned on
𝒦_m and on the labels of the free records of W_m, the joint state of all systems is V(⊗_{r good in W_m}|+⟩⟨+|_r ⊗
Ω_m)V† with V = ⊗_{r free in W_m} D_r(α_{x_r}), where Ω_m (the mixed and bad-only records of W_m, all held copies,
released systems other than the step-3 qubits and F_t test qubits of the tier's good leaves, which are averaged out, and
E) does not depend on the labels of the free records of W_m. In particular each good record's qubit is φ_{σ_hi}(x_r),
in tensor product with everything else.

*Proof.* m = 0: by Lemma S and (2.1) the true labels of the good leaves are independent uniform on Z/2^tZ, independent
of everything in 𝒦_0 (good copies are in tensor product with all other systems and the genie run ignores F's outcomes
on them; the coins W are independent of the labels); given the labels, each good leaf's first qubit is φ_{σ_hi}(u) =
D(α_u)|+⟩ in tensor product with everything else, and the free leaves are the good ones. Step m−1 → m: for every
record r of W_{m−1} write floor(x_r/2^{l_{m−1}}) = κ_r + 2^{b_m}ν_r with κ_r ∈ [0, 2^{b_m}) its stage-m key and ν_r ∈
[0, 2^{t−l_m}). For free records all κ_r, ν_r are independent and uniform given 𝒦_{m−1} (hypothesis); for bad-only
records they are 𝒦_{m−1}-measurable. So the grouping and the pairing are functions of 𝒦_{m−1} and the keys only, and
do not depend on any ν_r. Fix 𝒦_{m−1}, the keys and the labels of the free records of W_{m−1}. Replacing Ω_{m−1} by its
conjugate under D_r(−α_{x_r}) on every bad-only record r (a 𝒦_{m−1}-measurable unitary), the state of (J) at m−1
becomes VΞV† with V = ⊗_{r ∈ W_{m−1}} D_r(α_{x_r}) over all records and Ξ = ⊗_{r good}|+⟩⟨+|_r ⊗ Ω̃ independent of the
free labels. The stage applies, in an order fixed by the pairing, A5 to each pair and computational-basis measurements
to the unpaired records and to the controls of pairs with outcome 0. By (I1) and (I2), and since a factor on one qubit
commutes with an instrument on other qubits, these instruments with outcomes ω map VΞV† to V′Ξ_ωV′† up to a global
phase, where Ξ_ω is the result of the same instruments and outcomes on Ξ and V′ = ⊗_r D_r(α_{x_r}) over the outputs r
(labels x_a − x_{a′}). Hence, given 𝒦_{m−1} and the keys, the probability Tr Ξ_ω of every outcome sequence does not
depend on the ν_r of the free records (for a pair with a good member it is a fair coin, Lemma C), and conditioning on
the outcomes leaves these ν_r independent and uniform. Undo the conjugation on the bad-only outputs (their labels are
𝒦_m-measurable). A good–good pair with outcome 1 leaves ⟨1|_{a′}CNOT(|+⟩|+⟩) = |+⟩/√2 on its output, in tensor
product; every other output and every released system goes into Ω_m, which is built from Ξ_ω and so depends on the keys
and outcomes (both in 𝒦_m) but on no ν_r of a free record. This is (J) at m. For (U) at m: the two members of a pair
have κ_a = κ_{a′} and labels ≡ 0 mod 2^{l_{m−1}}, so x_a − x_{a′} ≡ 2^{l_m}(ν_a − ν_{a′}) (mod 2^t) and the output's
value floor(x′/2^{l_m}) is (ν_a − ν_{a′}) mod 2^{t−l_m}. For a free output some member is free, so over disjoint pairs
these values are independent and uniform, also given the outcomes. ∎

In particular, at the end of the sieve (m = R_ℓ, t − l_{R_ℓ} = d_ℓ) the values w_r = x_r/2^{R_ℓb} of the free records
of W_{R_ℓ} are independent and uniform on [0, 2^{d_ℓ}) given 𝒦_{R_ℓ}; as α_{2^{R_ℓb}w} ≡ 2πwθ_ℓ/2^{d_ℓ} (modulus
2^{t_ℓ}; only σ_hi mod 2^{d_ℓ} = θ_ℓ matters), by (J) a good record's qubit is (|0⟩ + e^{2πi w_r θ_ℓ/2^{d_ℓ}}|1⟩)/√2 in
tensor product with everything else, and each mixed record carries the factor D(2πw_rθ_ℓ/2^{d_ℓ}) on a state Ω_{R_ℓ}
that does not depend on any w_r. For tier 2 (R₂ = 0) the records are the leaves themselves, good or bad-only,
with the labels of the good ones uniform on [0, 2^{d₂}) given 𝒦_0.

### 7.6 Counting

**Lemma K (per stage).** At stage m let gg be the number of pairs with two good members, h_x and h_b the numbers of
pairs of a good record with a mixed, resp. bad-only one, h = h_x + h_b, and xx, xb, bb the numbers of pairs with two
mixed, one mixed and one bad-only, and two bad-only members; let u be the number of unpaired good records. Then,
deterministically, 2gg + h + u = G_{m−1}, u ≤ 2^b, h_x + 2xx + xb ≤ X_{m−1}, h_b + xb + 2bb ≤ B_{m−1}, and so
gg ≥ (G_{m−1} − P_{m−1} − 2^b)/2 and h + 2(xx + xb + bb) ≤ P_{m−1}. Given 𝒦_{m−1} and the keys, G_m is a sum of gg
conditionally fair coins, X_m ≤ X′ + xx + xb where X′ is a sum of h conditionally fair coins, and B_m ≤ bb.

*Proof.* Each record lies in at most one pair. A key group leaves at most one record unpaired, and at most 2^{b_m} ≤ 2^b
groups are nonempty, so u ≤ 2^b; as h ≤ P_{m−1}, gg = (G_{m−1} − h − u)/2 ≥ (G_{m−1} − P_{m−1} − 2^b)/2. A pair with two
good members gives a good output exactly on outcome 1, a pair with one good member a mixed output exactly on outcome 1, a
pair of two bad-only records a bad-only output or none, and any other pair a mixed output or none. The coins are fair by
Lemma C. ∎

**Lemma B₁ (bad leaves).** For guess i*, except with probability < 2e^{−445}: the tier-1 block has at most ȳM bad
copies, and the tier-2 block has at most (ε + τ_s + 2^{−8})K₂ < 0.1052K₂ bad copies. *Proof.* Bad copies are malformed
ones or clean ones with W = 1 (wrapped). Tier-1 block: by Lemma H with m_S = M and τ = τ_h, there are fewer than (ε +
τ_h)M malformed copies except with probability e^{−2τ_h²M} = e^{−2^{b−8}}. The coins W of the at most M clean copies
are independent with P(W = 1) = ϖ < 2/G = 2^{−11}, so by Lemma A (centred indicators) there are fewer than ϖM +
2^{−11}M < 2^{−10}M wrapped copies except with probability e^{−2(2^{−11}M)²/M} = e^{−2^{b−10}}. So there are fewer
than (ε + 2·2^{−10})M = ȳM bad copies. Tier-2 block: in the same way, fewer than (ε + τ_s)K₂ malformed copies except
with probability e^{−2τ_s²K₂} = e^{−K₂/320000}, and fewer than ϖK₂ + 2^{−9}K₂ < 2^{−8}K₂ wrapped copies except with
probability e^{−2·2^{−18}K₂} = e^{−8(2b+8)}. With b ≥ 64 and K₂ = 2^{20}(2b + 8) ≥ 2^{20}·136, the exponents are at
least 2^{56}, 2^{54}, 445 and 1088, and 1/10 + 1/800 + 1/256 < 0.1052. ∎

**Lemma S₁ (the sieve stages).** Let ℓ = 1 and consider tier ℓ of guess i* in the genie run on E_ℓ, given that its
block has at most ȳM bad leaves. Let g̃_m, p̃_m (m = 0, 1, 2) and γ_m (m = 1, 2) be the numbers of the first table
below (in units of M), and A_i, C_i, E_i (i = 0, 1, 2) those of the second. Except with probability 2R_ℓe^{−2^{b−13}},
G_m ≥ g̃_mM and P_m ≤ p̃_mM for m = 0, …, R_ℓ. In particular |W_{R_ℓ}| ≥ G_{R_ℓ} ≥ g̃_{R_ℓ}M ≥ K_ℓ, and the weighted
bad fraction Φ^{(ℓ)} = (X_{R_ℓ} + (3/2)B_{R_ℓ})/|W_{R_ℓ}| of W_{R_ℓ} satisfies Φ^{(ℓ)} < φ̄ = 0.489.

| m | γ_m | g̃_m | p̃_m |
| --- | --- | --- | --- |
| 0 | – | 0.898046875 | 0.101953125 |
| 1 | 0.397802734 | 0.198512887 | 0.051076127 |
| 2 | 0.073474239 | 0.036665367 | 0.025587943 |

The entries satisfy, for m = 1, 2 (each checked in exact rational arithmetic, with 2^b = M/2^{11}; every margin is
0 or at least 3·10^{−10}, so they can also be checked by hand with 2^{−11} = 0.00048828125):

  g̃_0 ≤ 1 − ȳ, p̃_0 ≥ ȳ;  γ_m ≤ (g̃_{m−1} − p̃_{m−1} − 2^{−11})/2;  g̃_m ≤ (1/2 − δ)γ_m;  p̃_m ≥ (1/2 + δ)p̃_{m−1}.

| i | A_i | C_i | E_i |
| --- | --- | --- | --- |
| 0 | 0.489000000000 | 0.511000000000 | 1.011000000000 |
| 1 | 0.122011230468 | 0.377511230468 | 0.505500000000 |
| 2 | 0.030443231820 | 0.219198847054 | 0.252750000000 |

Here A_0 = φ̄, C_0 = 1 − φ̄, E_0 = 3/2 − φ̄, and for i = 1, 2 (exact rational checks) A_i ≤ (1 − 2δ)A_{i−1}/4,
C_i ≥ A_i + C_{i−1}/2, E_i ≥ C_i and 2E_i ≥ E_{i−1}; these imply 2C_i ≥ C_{i−1} and C_i + E_i ≥ C_{i−1}. For R_ℓ = 2,
β_ℓ = A_{R_ℓ} − (A_{R_ℓ} + E_{R_ℓ})ȳ − Σ_{m=1}^{R_ℓ}(A_{R_ℓ−m+1}2^{−11} + C_{R_ℓ−m}δp̃_{m−1}) exceeds 1·10^{−3} (exact).

*Proof.* m = 0: P_0 ≤ ȳM ≤ p̃_0M and G_0 = M − P_0 ≥ (1 − ȳ)M ≥ g̃_0M. Step m−1 → m, on G_{m−1} ≥ g̃_{m−1}M and
P_{m−1} ≤ p̃_{m−1}M: by Lemma K, gg ≥ (G_{m−1} − P_{m−1} − 2^b)/2 ≥ (g̃_{m−1} − p̃_{m−1} − 2^{−11})M/2 ≥ γ_mM.
Given 𝒦_{m−1} and the keys, G_m is a sum of gg fair coins (Lemmas K, C), so by Lemma A, P(G_m < (1/2 − δ)gg) ≤
e^{−2δ²gg}; otherwise G_m ≥ (1/2 − δ)γ_mM ≥ g̃_mM. P_m ≤ X′ + xx + xb + bb with X′ a sum of h ≤ P_{m−1} fair coins
and h + 2(xx + xb + bb) ≤ P_{m−1}; by Lemma A, P(X′ ≥ h/2 + δp̃_{m−1}M) ≤ e^{−2δ²p̃_{m−1}²M²/h} ≤ e^{−2δ²p̃_{m−1}M}
(if h = 0, X′ = 0); otherwise P_m ≤ h/2 + xx + xb + bb + δp̃_{m−1}M ≤ P_{m−1}/2 + δp̃_{m−1}M ≤ (1/2 + δ)p̃_{m−1}M ≤
p̃_mM. Exponents: 2δ² = 2^{−19}, γ_mM ≥ γ_2M = 0.073474239·2^{b+11} > 2^{b+7} and p̃_{m−1}M ≥ p̃_1M =
0.051076127·2^{b+11} > 2^{b+6}, so 2δ²gg ≥ 2^{b−12} and 2δ²p̃_{m−1}M ≥ 2^{b−13}. Two events per stage are excluded.
*Weighted count.* For 0 ≤ m ≤ R_ℓ put i = R_ℓ − m and Λ_m = A_iG_m − C_iX_m − E_iB_m. On the events above, at stage
m: G_m ≥ (1/2 − δ)gg with 2gg ≥ G_{m−1} − h − 2^b (Lemma K) and A_{i+1} ≤ (1 − 2δ)A_i/4, so A_iG_m ≥
A_{i+1}(G_{m−1} − h − 2^b) (also when the right side is negative); X_m ≤ h/2 + δp̃_{m−1}M + xx + xb; and B_m ≤ bb.
Hence Λ_m ≥ A_{i+1}G_{m−1} − (A_{i+1}2^{−11} + C_iδp̃_{m−1})M − [(A_{i+1} + C_i/2)h + C_i(xx + xb) + E_i·bb], and
as h = h_x + h_b, h_x + 2xx + xb ≤ X_{m−1} and h_b + xb + 2bb ≤ B_{m−1}, the table's inequalities bound the bracket
by C_{i+1}X_{m−1} + E_{i+1}B_{m−1}. So Λ_m ≥ Λ_{m−1} − (A_{i+1}2^{−11} + C_iδp̃_{m−1})M. At m = 0, X_0 = 0 and G_0
= M − B_0 with B_0 ≤ ȳM, so Λ_0 ≥ (A_{R_ℓ} − (A_{R_ℓ} + E_{R_ℓ})ȳ)M. Summing over the R_ℓ stages gives Λ_{R_ℓ} ≥
β_ℓM > 0; as (A_0, C_0, E_0) = (φ̄, 1 − φ̄, 3/2 − φ̄), this says X_{R_ℓ} + (3/2)B_{R_ℓ} < φ̄(G_{R_ℓ} + X_{R_ℓ} +
B_{R_ℓ}) = φ̄|W_{R_ℓ}|. Finally g̃_{R_ℓ}M ≥ g̃₂M = 0.036665367·2^{b+11} > 75·2^b ≥ 2^{20}(2b + 8) ≥ K_ℓ (as d_ℓ ≤
2b, and 75·2^{b−20} > 2b + 8 for every b ≥ 64: it holds at b = 64 (1319413953331200 > 136), and from b to b + 1 the
left side doubles while the right grows by 2). ∎

**Lemma S₂ (samples).** Let ℓ = 1. Given W_{R_ℓ}, the sample keys of tier ℓ are distinct except with probability <
2^{−11}, and then the K_ℓ kept records are a uniformly random K_ℓ-subset of W_{R_ℓ} in uniformly random order,
independent of everything else. The number of bad records among them exceeds (P_{R_ℓ}/|W_{R_ℓ}| + τ_s)K_ℓ, or the
number of bad-only records among them exceeds (B_{R_ℓ}/|W_{R_ℓ}| + τ_s)K_ℓ, with probability at most 2e^{−2τ_s²K_ℓ} <
2e^{−440}. *Proof.* As in Lemma Π (|W_{R_ℓ}| ≤ M and κ_W = 2·bitlength(M) + 10). Given 𝒦_{R_ℓ}, over the sample keys,
each count is hypergeometric with mean (P_{R_ℓ}/|W_{R_ℓ}|)K_ℓ, resp. (B_{R_ℓ}/|W_{R_ℓ}|)K_ℓ; apply Lemma H′ to each.
2τ_s²K_ℓ = K_ℓ/320000 = 2^{20}(d_ℓ + 8)/320000 > 3.27(d_ℓ + 8) ≥ 3.27·135 > 440 (d_ℓ ≥ 127). ∎

So, outside these events, the K_ℓ records of tier 1 contain n_x mixed and n_o bad-only records with n_x + (3/2)n_o =
(n_x + n_o) + n_o/2 ≤ (Φ^{(ℓ)} + (3/2)τ_s)K_ℓ < (0.489 + 0.001875)K_ℓ < 0.491K_ℓ, since Φ^{(ℓ)} = (P_{R_ℓ} +
B_{R_ℓ}/2)/|W_{R_ℓ}|; and the K₂ records of tier 2 contain no mixed record and n_o < 0.1052K₂ bad-only records (Lemma
B₁), so n_x + (3/2)n_o < 0.1579K₂ < 0.491K₂.

### 7.7 Records and scores

Fix a search of guess i* in the genie run: the search of tier ℓ on the event E_ℓ, with d = d_ℓ, target θ = θ_ℓ and the
K = K_ℓ records of step 4. Define the record filtration as follows. If R_ℓ ≥ 1 (tier 1), let ℋ_0 be generated by
𝒦_{R_ℓ} (Lemma U: it contains the keys, pairings, A5 outcomes and the labels of the bad-only records, but not the labels w
of the free records of W_{R_ℓ}), the sample keys of step 3 and the release outcomes of the records not kept; if R_ℓ = 0
(tier 2), let ℋ_0 = 𝒦_0. For j ≥ 1 let ℋ_j = ℋ_{j−1} ∨ σ(w_j, m′_j, b_j). Then the record (w_j, m′_j, b_j) is
ℋ_j-measurable, and the type of record j (good, mixed or bad-only) is ℋ_0-measurable (it is fixed by the malformed set,
the coins W, the sieve structure and the sample). The release of a record not kept is a computational-basis
measurement; by (I1) its outcome law and its effect on the other systems do not depend on the labels of the free
records.

**Lemma R (record laws).** Let record j be free and β_j = 2πw_jθ/2^d. Conditioned on ℋ_{j−1}, w_j is uniform on
[0, 2^d), and m′_j is uniform on {0,…,7} and independent of w_j. If record j is good, then given (w_j, m′_j), b_j = 0
with probability exactly p_{m′_j}(w_jθ/2^d). If record j is mixed, then given ℋ_{j−1} and w_j the reduced state of its
qubit is D(β_j)ω_jD(β_j)† for a qubit state ω_j that depends on the history but not on w_j.
*Proof.* By Lemma U and its corollary at the end of 7.5, given 𝒦_{R_ℓ} (𝒦_0 in tier 2) the labels of the free records
are independent and uniform, and given them the joint state carries the factor D_r(β_r) on each free record r over a
state that does not depend on them, |+⟩ in tensor product for each good record. The sample keys (Lemma S₂) and m′_j are
fresh. Every other generator of ℋ_{j−1} comes from a measurement on systems other than record j's qubit: the releases
of the records not kept and the P2 of the records i < j. By (I1), and because a unitary on a system that is not measured
cancels from the probabilities, the probability of each history of ℋ_{j−1} given the free labels depends on them only
through w_1, …, w_{j−1}, which belong to the history. So given ℋ_{j−1}, w_j is still uniform, and record j's qubit is
D(β_j) applied to a state that does not depend on w_j: for a good record this is (|0⟩ + e^{2πi w_jθ/2^d}|1⟩)/√2 in
tensor product with everything else, and P2 gives the stated law (A3). ∎

**Lemma B (bounded influence).** For every record and every τ, |Z̃(τ)| ≤ 1 + 2^{−24} = R₀. *Proof.* Lemma T (App. B). ∎

**Lemma D (discretisation).** For every record j and every τ ∈ [0, 2^d), let X̂_j(τ) = (−1)^{b_j}cos(2π(w_jτ/2^d −
m′_j/8)). Then |Z̃_j(τ) − X̂_j(τ)| ≤ η. *Proof.* Write x = w_j/2^d and φ = frac(xτ). For each i, 2^p frac(2^i x) −
c_{j,i} ∈ [0, 1). Since Σ_i τ_i 2^i x = xτ, Σ_i τ_i 2^p frac(2^i x) ≡ 2^p φ (mod 2^p), so V_j(τ) ≡ 2^pφ − ζ′ (mod 2^p)
with ζ′ = Σ_i τ_i(2^p frac(2^i x) − c_{j,i}) ∈ [0, d). Hence |V_j(τ)/2^p − φ|∘ < d/2^p < 2^{−q−1} (as d ≤ n <
2^{bitlength(n)}). Also 0 ≤ V_j(τ)/2^p − h_j(τ)/2^q < 2^{−q}. So |h_j(τ)/2^q − φ|∘ < (3/2)2^{−q}, and as x ↦ cos 2πx
has period 1 and is 2π-Lipschitz,
|cos(2π(h_j(τ)/2^q − m′_j/8)) − cos(2π(φ − m′_j/8))| < 3π2^{−q}. Since 2^{q−3}m′_j is an integer and table[k] approximates
cos(2πk/2^q), which has period 2^q in k, |table[k_j(τ)] − cos(2π(h_j(τ)/2^q − m′_j/8))| < τ_T (Lemma T). Adding the bounds
gives the claim. ∎

**Lemma C* (clean correlation).** If record j is good, then for τ ∈ [0, 2^d), E[X̂_j(τ) | ℋ_{j−1}] = 1/2 if τ = θ and 0
otherwise; hence E[Z̃_j(τ) | ℋ_{j−1}] ≥ 1/2 − η if τ = θ and ≤ η otherwise.
*Proof.* By Lemma R, E[(−1)^{b_j} | w_j, m′_j] = 2p_{m′_j}(w_jθ/2^d) − 1 = cos(2π(w_jθ/2^d − m′_j/8)). With
cos A cos B = (cos(A − B) + cos(A + B))/2, E[X̂_j(τ) | w_j, m′_j] = (1/2)cos(2πw_j(θ − τ)/2^d) +
(1/2)cos(2πw_j(θ + τ)/2^d − πm′_j/2). Averaging over m′_j: Σ_{m′=0}^{7} cos(α − πm′/2) = Re(e^{iα}Σ_{m′}(−i)^{m′}) = 0.
Averaging over w_j uniform on [0, 2^d): (1/2^d)Σ_w cos(2πw(θ − τ)/2^d) is 1 if θ ≡ τ (mod 2^d), i.e. τ = θ, and 0
otherwise (a sum of 2^d-th roots of unity). Lemma D gives the second statement. ∎

**Lemma M (any record).** For every record j, every τ and every history in ℋ_{j−1} of positive probability, −(1/2 + η)
≤ E[Z̃_j(τ) | ℋ_{j−1}] ≤ 1/2 + η. *Proof.* Every generator of ℋ_{j−1} is obtained before the P2 of record j (steps 1–3
of 6.4 precede step 4, and records are measured in the order j = 1, …, K). Fix an outcome g of ℋ_{j−1} together with
w_j (fixed before m′_j is drawn). Let σ_g be the reduced state of record j's qubit given g, written (I + xX + yY +
zZ)/2 with x + iy = re^{iα}, 0 ≤ r ≤ 1. m′_j is drawn from fresh qubits, so it is uniform and independent of g, and P2
with θ′ = 2πm′/8 has outcome 0 exactly when it projects onto (|0⟩ + e^{iθ′}|1⟩)/√2; so E[(−1)^b | g, m′] = x cos θ′ +
y sin θ′ = r cos(θ′ − α). With v = w_jτ/2^d and θ′_{m′} = 2πm′/8, E[X̂_j(τ) | g] = (1/8)Σ_{m′} r cos(θ′_{m′} −
α)cos(2πv − θ′_{m′}) = (r/2)cos(2πv − α) + (r/16)Σ_{m′}cos(2θ′_{m′} − α − 2πv) = (r/2)cos(2πv − α) ∈ [−1/2, 1/2],
because Σ_{m′=0}^{7} e^{2iθ′_{m′}} = Σ_{m′} i^{m′} = 0. Lemma D and the tower property give the claim. ∎

**Lemma X (mixed records).** If record j is mixed, then for τ ≠ θ, E[X̂_j(τ) | ℋ_{j−1}] = 0; hence
|E[Z̃_j(τ) | ℋ_{j−1}]| ≤ η.
*Proof.* Fix a history g of ℋ_{j−1} and w_j, and write 2⟨1|ω_j|0⟩ = re^{iψ} with 0 ≤ r ≤ 1 (ω_j of Lemma R, which
depends on g but not on w_j). The qubit's state D(β_j)ω_jD(β_j)† has 2⟨1|·|0⟩ = re^{i(β_j + ψ)}, so the computation in
the proof of Lemma M (which uses only this coherence and the fresh m′_j) gives E[X̂_j(τ) | g, w_j] =
(r/2)cos(2πw_jτ/2^d − β_j − ψ) = (r/2)cos(2πw_j(τ − θ)/2^d − ψ). By Lemma R, w_j is uniform on [0, 2^d) given g, while r
and ψ do not depend on w_j, and (1/2^d)Σ_w cos(2πw(τ − θ)/2^d − ψ) = Re(e^{−iψ}2^{−d}Σ_w e^{2πiw(τ−θ)/2^d}) = 0 for
τ ≠ θ (a sum of 2^d-th roots of unity). Lemma D gives the second statement. ∎

A mixed record cannot steer this: its label's high part comes from a good leaf (Lemma U), the adversary fixed every
malformed copy before any outcome existed (Lemma N), and the pairing reads only keys.

### 7.8 The score separates the target

**Theorem M (separation).** Fix a search of guess i* as in 7.7 with K records, of which n_x are mixed and n_o
bad-only, with n_x + (3/2)n_o ≤ 0.491K. Then, except with probability < 2^{−40}, S(θ) > K/256 and S(τ) < S(θ) − K/256 for
every τ ≠ θ.
*Proof.* For τ ∈ [0, 2^d) let m_j(τ) = E[Z̃_j(τ) | ℋ_{j−1}] and D_j(τ) = Z̃_j(τ) − m_j(τ). Then E[D_j(τ) | ℋ_{j−1}] = 0
and D_j(τ) ∈ [a_j, a_j + 2R₀] with a_j = −R₀ − m_j(τ) ℋ_{j−1}-measurable. Lemma A (rescaled by 2R₀) gives
P(Σ_j D_j(θ) ≤ −δ_sK) ≤ e^{−δ_s²K/(2R₀²)} and, for τ ≠ θ, P(Σ_j D_j(τ) ≥ δ_sK) ≤ e^{−δ_s²K/(2R₀²)}. Now
δ_s²K/(2R₀²) > 2^{20}(d + 8)/320001 > 3.27(d + 8), so each probability is < e^{−3.27(d+8)} < 2^{−4.7(d+8)}, and a union
bound over the 2^d candidates gives < 2^{d−4.7(d+8)} < 2^{−40}. On the complement, with n_c = K − n_x − n_o good records,
Lemmas C*, X and M give S(θ) > −δ_sK + n_c(1/2 − η) − (n_x + n_o)(1/2 + η) = K(1/2 − η − δ_s) − (n_x + n_o) ≥
K(1/2 − η − δ_s − 0.491) > 0.0064K > K/256, and for τ ≠ θ, S(τ) < δ_sK + (n_c + n_x)η + n_o(1/2 + η) = K(δ_s + η) +
n_o/2. Hence S(θ) − S(τ) > K(1/2 − 2η − 2δ_s) − (n_x + (3/2)n_o) ≥ K(1/2 − 2η − 2δ_s − 0.491) > 0.00399K > K/256. ∎

**Lemma Sr (ladder search).** If S(θ) > K/256 and S(τ) < S(θ) − K/256 for every τ ≠ θ, the search of 6.7 returns θ
except with probability ≤ 2^{−7}.
*Proof.* d ≥ 127 ≥ 4. By Lemma B, S(θ) ≤ R₀K < (257/256)K = ϑ_{257}K. Let ι* be the largest ι ∈ {1, …, 257} with
ϑ_ιK < S(θ); it exists because ϑ_1K = K/256 < S(θ), and ι* ≤ 256, so ϑ_{ι*+1}K ≥ S(θ). For ι > ι* and every τ,
S(τ) ≤ S(θ) ≤ ϑ_ιK, so f_ι marks nothing: every measured τ̂ fails the check f_ι(τ̂) = 1, and the search goes on without
returning. At ι = ι*, f_{ι*}(θ) = 1, and for τ ≠ θ, S(τ) < S(θ) − K/256 ≤ ϑ_{ι*+1}K − K/256 = ϑ_{ι*}K, so f_{ι*} marks
exactly θ. Each of the at most 7 runs at this threshold is an independent run of the circuit of App. C on fresh qubits,
which applies H^{⊗d} and 𝒢_{ι*}^{k_G}; by Lemmas G and I (App. D) it returns θ with probability > 1/2, and the classical
check accepts only θ. So the search returns θ unless all seven runs at threshold ι* fail, which has probability
< 2^{−7}. ∎

### 7.9 The test

**Lemma T* (test).** Let X_i be the number of malformed copies in the test block of guess i. If X_i ≤ k/5, then
TEST(s) on that block accepts with certainty, and for every v ≠ s, TEST(v) accepts with probability at most e^{−k/200},
whatever happened before.
*Proof.* After subtracting v, a clean copy is the mixture over x of (|0,x⟩ + |1,(x + s − v) mod N⟩)/√2. If v = s the first
qubit is |+⟩ and H gives 0, so Z ≥ k − X_i ≥ 4k/5 ≥ 3k/4. If v ≠ s, the two register values differ, the first qubit is
maximally mixed, and its outcome is a fair coin given everything else (the clean copy is in tensor product with all other
systems). So Z ≤ X_i + Y with Y a sum of k′ ≤ k conditionally fair coins, and Z ≥ 3k/4 forces Y ≥ 11k/20 ≥ k′/2 + k/20;
by Lemma A this has probability ≤ e^{−2(k/20)²/k′} ≤ e^{−k/200}. ∎

By Lemma H with τ = 1/5 − 1/10 = 1/10, P(X_i > k/5) ≤ e^{−2(1/10)²k} < e^{−k/51}. With k = 256·bitlength(100G) = 4864,
e^{−k/51} < e^{−95} and e^{−k/200} < e^{−24} < 2^{−34} < 1/(400G).

### 7.10 Theorem 1 (n ≥ 256)

**Theorem 1.** For every N with n ≥ 256, every s and every adversary of Section 5 with ε = 1/10, RLS outputs s with
probability at least 9/10.
*Proof.* Exclude: the tie of 6.1 (< 2^{−11}, Lemma Π); some test block with X_i > k/5 (≤ G e^{−95} < 2^{−120}); some
TEST(v), v ≠ s, accepting (≤ G e^{−24} < 2^{−22}); the genie run differing from the real run (< 1/100, 7.4); for guess
i*, the events of Lemma B₁ (< 2e^{−445}), of Lemma S₁ in tier 1 (< 4e^{−2^{51}}) and of Lemma S₂ in tier 1
(< 2^{−11} + 2e^{−440}); the failure of Theorem M in the search of tier ℓ of guess i* on E_ℓ, ℓ = 1, 2
(< 2·2^{−40}); and the failure of Lemma Sr in these two searches (< 2·2^{−7}). The total is
< 0.0005 + 2^{−22} + 0.01 + 0.0005 + 0.0157 + 10^{−9} < 0.027.
Outside these events, suppose no earlier guess has output s (otherwise RLS has output s). No earlier guess output
anything else (no wrong candidate is accepted), so guess i* is run and E₁ holds. If E_ℓ holds (ℓ ∈ {1, 2}), the tier
does not fail in step 3 (for ℓ = 1 by Lemmas S₁, S₂: |W_{R_ℓ}| ≥ K_ℓ and no tie; for ℓ = 2 step 3 keeps all K₂
leaves and cannot fail), and its K_ℓ records satisfy n_x + (3/2)n_o < 0.491K_ℓ
(the summary after Lemma S₂), so the gap of Theorem M holds at θ = θ_ℓ and the search returns θ̂_ℓ = θ_ℓ (Lemma Sr).
Then σ_low becomes (s′ mod 2^{j_ℓ}) + 2^{j_ℓ}θ_ℓ = s′ mod 2^{j_ℓ + d_ℓ} (7.4), so E_{ℓ+1} holds for ℓ = 1, and after tier 2
the candidate is s̃ = s′ mod 2^n = s′ < N, with (s̃ + g*) mod N = s. TEST(s) accepts on the test block of guess i*
(Lemma T*). So RLS outputs s with probability > 0.97 ≥ 9/10. ∎

### 7.11 Small inputs (n < 256)

**Theorem 2.** For every N with n < 256, every s and every adversary with ε = 1/10, the branch of 6.10 outputs s with
probability > 0.99.
*Proof.* Lemmas N and Π hold verbatim for this branch (P(tie) < 2^{−11}). Let X_v be the number of malformed copies among
the K_s copies of candidate v. Lemma H with τ = 1/5 − 1/10 = 1/10 gives P(X_v > K_s/5) ≤ e^{−2(1/10)²K_s}
< e^{−20000}. If X_s ≤ K_s/5, then Z_s ≥ 4K_s/5 ≥ 3K_s/4 (as in Lemma T*). For v ≠ s with X_v ≤ K_s/5, Z_v ≥ 3K_s/4 has
probability ≤ e^{−K_s/200} < e^{−5200}. A union bound over the N ≤ 2^{255} candidates gives total failure
< 2^{−11} + 2^{256}(e^{−20000} + e^{−5200}) < 0.01. ∎

Theorems 1 and 2 cover every N ≥ 2 and every s, for every adversary of Section 5 with ε(n) = 1/10, and in particular
for the clean problem.

## 8. Resources (every branch)

For n < 256 every quantity is an absolute constant: at most Q_s ≤ 2^{255}·2^{20} = 2^{275} copies, O(Q_s n + Q_s log₂
Q_s·κ′) bit operations and gates before the address charge (itself O(log Q_s)), (n+1)Q_s + O(n) qubits held and O(Q_s
κ′) bits. These constants are astronomically large but independent of N, s and all outcomes. Let n ≥ 256.

**Sizes.** b ≤ n/4 + 1, so M = 2^{b+11} ≤ 2^{12}·2^{n/4}; K₁, K₂ ≤ 2^{20}(n + 8); G = 2^{12}; k = 4864. Hence

  **Q = G(M + K₂ + k) < 2^{12}(2^{12}·2^{n/4} + 2^{20}(n + 8) + 4864) < 2^{25}·2^{n/4},**

counting every acquired copy (all are acquired in 6.1, on every branch; 2^{n/4} ≥ 2^{64} dominates the other terms).
Also log₂ Q < n/4 + 25, so κ, κ_W < n/2 + 62 < n and L₁ ≤ log₂ Q + log₂(1600(n+1)) + 1 < n, i.e. κ, κ_W, L₁, r₁ = O(n).

**Quantum space.** All Q copies are held from 6.1 until they are used: (n+1)Q qubits. In addition, at any time: one
copy's O(n) LEAF/F_t ancillas, one test control, one A4 qubit and one TEST ancilla set; in a search, the d search qubits,
U (w qubits), V (p) with O(p) ancillas, k (q), v (27) with O(q) ancillas, the O(w) ancillas of P3b, the flag with O(w)
carry ancillas, the diffusion target and its d − 2 ancillas: O(n) qubits, one fixed pool reused for every record, call and
repetition. Measured qubits are released. **S_Q ≤ (n+1)Q + O(n) = O(2^{n/4} n).**

**Classical space.** Sort keys and workspace and the rank table: O(Q(κ + bitlength(Q))) = O(Qn) bits. The current tier
of the current guess: at most M labels of n bits and M copy indices, the 2^b key counters, the sample keys of κ_W bits
with merge-sort workspace: O(Mn) bits. The stored search records: K(d + 4) = O(n²) bits. The table: 27·2^{24} bits (an
absolute constant). F_t counters, parameters, σ_low, the Grover controller (K_G, k_G, counters) and one gate
description: O(n²) bits. **S_C = O(Qn) = O(2^{n/4} n).** Hence 𝔐 = O(2^{n/4}n), log₂(𝔐 + 2) < n/4 + 2 log₂ n + O(1),
and **A = O(n)**.

**Work** (every operation charged O(A) = O(n)).
* Acquisition: Q(n+1). Keys and merge sort of 6.1: O(Q log₂ Q·κ) = O(Qn²) bit operations, O(Qn³) charged.
* Leaves (at most G(M + K₂) ≤ Q of them): LEAF uses O(n) gates; F_t uses 8(J+1)r₁ ≤ 8n·r₁ kickback tests of O(n) gates;
  Lemma P and the rounding O(n²). A leaf costs O(n²r₁) = O(n³) operations, O(n⁴) charged; in total O(Qn⁴).
* Sieve stages and samples, per guess: R₁ = 2 stages, each on at most M records, with O(Mn) bit operations for
  keys, counting sort and subtractions, one A5 per pair and O(2^b log M) for the counters; one sample with
  O(M log₂ M·κ_W) for the keys and their sort: O(Mn²), O(Mn³) charged; over G guesses O(Qn³).
* Table (App. B): an absolute constant number of operations. Records: O(K) operations per search.
* Searches, per guess: two searches, each with at most 1799 runs (257 thresholds, at most 7 each) of at most k_G ≤
  0.785·2^{d/2} ≤ 2^b ≤ 2·2^{n/4} Grover iterations (d₁ ≤ 2b and d_ℓ = 2b for ℓ ≥ 2). One call of 𝒪_ι costs, per
  record, d applications of P3a on p qubits (O(dp)), O(p + q), one table read (O(2^q(q + 27)), an absolute constant)
  and one P3b (O(w)), done and undone, so O(K(dp + w)) = O(n² log n) gates; 𝒟 costs O(d); the flag constant of each
  threshold costs O(w). A run also evaluates f_ι(τ̂) classically in O(Kdp) = O(n² log n). As 1799 is an absolute
  constant, each search costs O(2^{n/4} n² log n) operations, O(2^{n/4} n³ log n) charged; over G guesses the same
  order.
* TEST: G·k copies, O(n) gates each. Grid points and parameters: O(Gn²). Releasing unused blocks, or all copies on a
  tie: at most Q(n+1) measurements and resets.

The leaf term dominates: **T = O(Qn⁴ + 2^{n/4}n³ log n) = O(2^{n/4} n⁴).**

All four bounds hold simultaneously on every execution branch of this one algorithm with this one parameter rule
(every loop length is bounded by a fixed function of N; the copy count is exactly Q), jointly with Theorems 1 and 2,
for every adversary of Section 5.

## 9. Exact growth indices and structured envelopes

For ℬ(n) = 2^{n/4} n^r with fixed r ≥ 0: log₂ ℬ = n/4 + r log₂ n, so log₂ log₂ ℬ = log₂ n − log₂ 4 + log₂(1 + 4r log₂ n/n),
and log₂ log₂ ℬ/log₂ n → 1. Hence g(ℬ) = 1 (the max{4,·} is irrelevant for large n); outer constants do not change it.

* T: ℬ_T = 2^{n/4} n⁴, index **1**: exponent [{coefficient 1/4, nPower 1, logPower 0}], nPower 4, logPower 0.
* S_C: ℬ = 2^{n/4} n, index **1**: exponent [{1/4, 1, 0}], nPower 1, logPower 0.
* S_Q: ℬ = 2^{n/4} n, index **1**: exponent [{1/4, 1, 0}], nPower 1, logPower 0.
* Q: ℬ = 2^{n/4}, index **1**: exponent [{1/4, 1, 0}], nPower 0, logPower 0.

Published time score: [1]. Under the asymptotic comparator the time envelope is strictly below 2^{n/2}·poly(n).

## 10. Fractional error tolerance

ε(n) = 1/10 under the model of Section 5: with Q acquired copies, at most floor(Q/10) of them are malformed; their
positions are chosen adaptively by an adversary who knows N, s, the algorithm and all previous measurement outcomes
(RLS obtains none before the last delivery); malformed copies are arbitrary (n+1)-qubit states, possibly entangled with
one another and with the adversary, but not with clean copies or RLS's workspace; every other copy is, at the moment
of its delivery, an independent ideal coset state ρ_s in tensor product with everything else, and the adversary has no
access to a copy or to RLS's systems after delivery. For every N ≥ 2 (no validity threshold: Theorem 2 covers n < 256),
every s and every such adversary, Theorems 1 and 2 give success probability at least 9/10, jointly with the four resource
bounds of Section 8, which hold on every branch for every adversary. The clean problem is the special case with no
malformed copy.

## 11. Credits, lineage and what is new

* The low-bit sieve step on Z/2^nZ is Kuperberg's (SIAM J. Comput. 35 (2005) 170–188, Section 3). Quantum search is
  Grover's (STOC 1996) with the two-reflection analysis of Boyer–Brassard–Høyer–Tapp (Fortschr. Phys. 46 (1998)),
  reproved in App. D. Nothing cited in this bullet is used as a premise.
* New here: the phase-covariance form (J) of Lemma U, Lemma X (mixed records have mean 0 at every wrong candidate),
  the three-type count of Lemmas K and S₁ with its weighted potential, Theorem M in gap form and the threshold ladder
  (Lemma Sr). The algorithm is our RLS-G2R (484bc509) with the ladder search in place of its single threshold 17/100;
  everything else (sieve, M, G, k, K_ℓ, δ_s, τ_s, the test) is unchanged, and the tolerance rises from 1/13 to 1/10.
* Our own components, re-proved here: the splice, F_t and A1–A4 (SLS, 59facd77); A5 and Lemma P (OMX-ML, 31c2d043);
  the full-upfront acquisition, the permutation and Lemmas N, Π, U, C, K and the genie run (RLS, 280a17e4); the shadow
  score, the cosine table, the oracle circuits and Lemmas B, D, C*, M (ROB-G2, 55a6ce76; adapted to labels in Z/2^dZ);
  the sieve-then-search template and the text of our RLS-G1 (4ef5cf09; one stage, tolerance 1/7 at work 2^{n/3}·poly),
  RLS-G2 (6b206bcf; two stages, 1/16 at 2^{n/4}·poly), RLS-G4 (9e0af9a8; three tiers, 1/64 at 2^{n/6}·poly), RLS-G6
  (6a572c14; four tiers, 1/256 at 2^{n/8}·poly) and RLS-G8 (924b098e; five tiers, 1/1024 at 2^{n/10}·poly) entries on
  this track. The model is that of our ROB line (d0c6b9b9, 5d77f276, a5c17989, 55a6ce76).
* Our RLS-3 (06a9acf5): a three-stage robust low-bit sieve with tolerance 1/32 at work 2^{n/3}·poly, same model. mpjunior92's
  PSG12 (cac3285d): a clean three-level bounded Grover sieve that already reaches work O(n⁴L^{3/2}2^{n/6}) without
  corruption; zereraz's PSR-W3 (a08e8f51). Credited; nothing is used.
* Rows in this error-model text (credited, nothing used): mpjunior92's RQ-SPLIT 38d66dc0 (1/3 at work 2^{n/2}·poly);
  mpjunior92's PSG16 f22ea7ec and PSG18 af0a13dd and GordoAR's PSG-D2 3faef527 (inverse-quadratic tolerances at work
  2^{n/4}·poly).
* Positive-tolerance prior work in this model or others (credited, nothing used): dadon's f892f7ea and 493303b5 (1/3, same
  model);
  mpjunior92's PSG13 4c42d100 (same model, tolerance 1/(2^{39}n⁴), time 2^{n/6}·poly with polynomial memory) and
  PSG14C 30304a9e (inverse-cubic tolerance); dadon's 7341d79b (1/(896n) at 2^{n/3}·poly); zereraz's
  b45deb1b (1/(2·10^{10}n⁴));
  kaankolcu's RWT25 3f48c893 (1/4, fixed-position model); GordoAR's c730b22b (1/3, own model); ercumentyildirim's
  LSIEVE f2cb3153/0f4adc93 (oblivious model, inverse-polynomial tolerance at 2^{n/log n}·poly); smoke-era RGRST1
  be98e61b, CGRST1 53b4755b, CADGR1 5f048e8b/b838e1ae, CADGR2 45044787, RLQGR1–3 ee378bae, 635a47e2, 0e1559e4, 09c05313,
  7b2afdfc. Regev (SIAM J. Comput. 33 (2004), Definition 2.1) studies DCP with a failure parameter.

Context (not part of any claim). As all slack constants tend to 0 the two-stage count allows every ε < 1/(2^{3} + 1),
the old one every ε < 1/(3·2^{2}). No cited result is used as a lemma except Hoeffding's inequality for sampling
without replacement (Lemmas H, H′), cited with its exact theorem number; Lemma A is proved in the file.
