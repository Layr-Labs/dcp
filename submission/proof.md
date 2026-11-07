# RLS-GD4: a three-tier shuffled robust sieve with threshold-ladder quantum search, O(2^{n/6} n⁵) work, tolerance 9999/10000 of adaptively placed dephased copies

This file and `appendix.md` together are the complete proof of all five claims in `submission.json`. They
describe one algorithm, **RLS-GD4** (below simply RLS), with one fixed parameter rule, and prove for every
integer N ≥ 2, every s ∈ Z/NZ, with n = ceil(log₂ N), and every adversary of the error model of Section 5
(which contains the clean problem as the adversary that corrupts nothing):

* the output equals s with unconditional probability at least 9/10 (> 2/3);
* total work T = O(2^{n/6} n⁵);
* peak classical space S_C = O(2^{n/6} n²) bits;
* peak quantum space S_Q = O(2^{n/6} n²) qubits;
* acquired source copies Q = O(2^{n/6} n); Q is a fixed function of N, the same on every branch;
* fractional error tolerance ε(n) = 9999/10000: at most floor(9999Q/10000) acquired copies may be malformed, at
  adversarially and adaptively chosen positions, with contents that are arbitrary except that the first qubit of
  each malformed copy is dephased with respect to everything else (Section 5).

All constants are absolute (independent of N, s, the adversary and all outcomes); several of them are astronomically
large (for instance G = 2^{256} grid guesses). Every loop of RLS has a length bounded by a fixed function of N, so the
four resource bounds hold on every execution branch whatever the copies contain. Logarithms are base 2 unless written
ln. All four growth indices equal 1; the time envelope has exponent n/6.

**Idea.** This entry combines the three-tier sieve-then-search structure of our RLS-G4 (9e0af9a8; adaptive malformed copies,
tolerance 1/64 at work 2^{n/6}·poly) with the dephased-copy analysis of our RLS-D3 (0a76fda2, tolerance 9999/10000
at work 2^{n/3}·poly). (i) All Q copies are acquired before the first measurement and permuted uniformly, so the
adversary chooses blind and its copies spread evenly over all slot blocks. (ii) The SLS splice (59facd77) gives exact
coset states of Z/2^tZ for the right grid guess. (iii) Tier 1 runs four shuffled low-bit sieve stages of b = ceil(n/6)
bits on Z/2^nZ and then searches the low d₁ = n − 4b ≤ 2b bits; tier 2 runs two stages on the next 4b bits and searches
2b bits; tier 3 searches the last 2b bits. (iv) A record with a malformed leaf is dephased (Lemma D), so its shadow
score has conditional mean exactly 0 for every candidate, whatever the table precision (Lemma Z0). Clean records give
1/2 at the target and almost 0 elsewhere. So the target's score is a fixed multiple of the unknown number n_g of clean
records, and every other score is below a sixth of it. Because n_g is unknown and can be as small as 2^{−229.08}K, the
search tries the thresholds 2^{−i}K for i = 1, 2, …, 232 in turn: no candidate is marked until the first threshold
below the target's score, and there the target is the only marked candidate (Theorem M_D, Lemma Sr_D). (v) With the
shuffled pairing of RLS-D3 the ratio z of bad to good records grows like z ↦ 2.03z(1 + z), from z₀ ≈ 10^4 to
z₄ < 4.7·10^{68} after four stages; the constants M = b·2^{b+520} and K = 2^{472}(d + 8) are chosen so that enough clean
records survive (Lemmas Z_D, S₁_D, S₂_D).

Notation. frac(φ) ∈ [0,1); |φ|∘ = min_{z∈Z}|φ − z| (circular distance). bitlength(x) is the number of
binary digits of an integer x ≥ 1, so 2^{bitlength(x)} > x and e^{−bitlength(x)} < 2^{−bitlength(x)} < 1/x.
round(z) = floor(z + 1/2). For a modulus M′ and an integer v, the *label-v qubit* for secret σ is
φ_σ(v) = (|0⟩ + e^{2πivσ/M′}|1⟩)/√2; only v mod M′ matters.

## 1. Exact primitives (Clifford+T, fresh |0⟩, computational-basis measurement)

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
gates), so generation adds O(1) bit operations per gate, which the address charge A per gate dominates.

**A3 (phase test).** For a qubit (|0⟩ + e^{2πiθ}|1⟩)/√2 and m′ ∈ {0,…,7}, apply (T†)^{m′}, then H,
then measure. Outcome 0 has probability exactly p_{m′}(θ) = (1 + cos 2π(θ − m′/8))/2.

**A4 (fair bits).** A fresh |0⟩, H, measurement: one exact fair bit, O(1) work.

**A5 (combination).** Given qubits a, b, apply CNOT (control a, target b) and measure b. If a and b
are label-v₁ and label-v₂ qubits φ_σ(v₁), φ_σ(v₂) in a product state, with α_i = 2πv_iσ/M′, the state
before the measurement is (|00⟩ + e^{iα₂}|01⟩ + e^{iα₁}|11⟩ + e^{i(α₁+α₂)}|10⟩)/2. Outcome 0
(probability exactly 1/2) leaves a in φ_σ(v₁ + v₂); outcome 1 (probability exactly 1/2) leaves a in
(e^{iα₂}|0⟩ + e^{iα₁}|1⟩)/√2, which is φ_σ(v₁ − v₂) up to a global phase.

**Further primitives.** The register arithmetic P3a–P3e (constant adders mod 2^p, register adders mod 2^w,
comparisons with constants, multi-controlled X and table reads), the cosine table (Lemma T), the oracles 𝒪_i and
the diffusion 𝒟 are given in App. A–C of `appendix.md`, which is part of this proof.

**Cost convention.** Let 𝔐 be the number of allocated bits plus qubits. Section 8 shows
𝔐 = O(2^{n/6} n²), so a classically indexed access or classically addressed gate costs
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

**Procedure F_t** reads the label u of a t-qubit register in the state χ_{−u} of Section 2 (modulus 2^t) from r = r₁
kickback tests for each bit level i ∈ {0, …, J}, J = max(1, t − 2), and each offset m′ ∈ {0, …, 7}, each followed by A3,
and outputs û ∈ [0, 2^t). Lemma P, the procedure and **Corollary F** (if the register is χ_{−u}, then û = u with
probability ≥ 1 − 16(J+1)e^{−r/200}) are stated and proved in App. G of `appendix.md`.

## 4. Parameters (exact integer arithmetic, computed from N)

For **n ≥ 2048**:

* **R** = 4 (stages of tier 1); **b** = ceil(n/6) (sieve bits per stage), so n/6 ≤ b ≤ n/6 + 1, b ≥ 342, R ≤ b and
  n ≤ 2^b.
* Tiers ℓ = 1, 2, 3 with (t_ℓ, j_ℓ, R_ℓ, d_ℓ) = (n, 0, 4, d₁), (4b, d₁, 2, 2b), (2b, d₁ + 2b, 0, 2b), where **d₁** = n − 4b;
  so t_ℓ = n − j_ℓ, d_ℓ = t_ℓ − R_ℓb, n/3 − 4 ≤ d₁ ≤ 2b and every d_ℓ ≥ 680.
* **M** = b·2^{b+520} (leaves of tiers 1 and 2 per guess).
* **K_ℓ** = 2^{472}(d_ℓ + 8) (records of the search of tier ℓ).
* **G** = 2^{256} (grid size); grid points g_i = floor(iN/G) for i = 0, …, G−1. Since N ≥ 2^{2047} > G, the g_i are
  distinct.
* **k** = 2^{40} (copies per test).
* **Q** = G(2M + K₃ + k) (copies acquired).
* L₁ = bitlength(1600(n+1)Q); **r₁** = 200L₁ (tests per bit level i and offset m′ in F_t).
* **κ** = 2·bitlength(Q) + 10 (sort-key bits); **κ_s** = 2·bitlength(M) + 2b + 70 (shuffle-key bits);
  **κ_W** = 2·bitlength(M) + 10 (sample-key bits).
* Score: **q** = 24 (angle bits); **p** = q + 1 + bitlength(n) (phase bits); for a search with K records,
  **w** = bitlength(K) + 29 (accumulator width); ladder length **I** = 232.
* Search over d qubits: K_G = floor(2^{d/2}) (the integer square root of 2^d), k_G = floor(785K_G/1000), at most 7
  repetitions per ladder level.

Analysis constants (not used by the algorithm): ε = 9999/10000, δ = 1/384, Λ = 2b + 64, y = ε + 2^{−20} + 2^{−254},
γ = 2^{−228.08}, δ_s = γ/64, τ_T = 2^{−24} (table accuracy), η = 3π2^{−24} + τ_T < 6.22·10^{−7}, R₀ = 1 + τ_T.

For **n < 2048**: K_s = 2^{44}; Q_s = N·K_s; κ′ = 2·bitlength(Q_s) + 10 (Section 6.10).

## 5. Error model (adaptive globally dephased malformed copies)

Copies are delivered one at a time in acquisition order j = 1, …, Q (Q is given by Sections 4, 6.1 and 6.10).
An **adversary** knows N, s, the full description of RLS, and every measurement outcome obtained by RLS
before copy j is delivered; it holds an arbitrary private quantum system E which it may measure and process.
Before copy j is delivered it chooses c_j ∈ {clean, malformed}, as a function of that information and its
own outcomes; on every branch at most floor(εQ) copies are malformed, ε = 9999/10000.

* A **malformed** copy is an (n+1)-qubit system supplied from E whose first qubit A is *dephased with respect to
  all other systems*: conditioned on every outcome of every measurement made before its delivery (by RLS or by
  the adversary), the joint state of A, the rest of the copy, every copy delivered before it, RLS's workspace and
  E (including every system E later delivers) is unchanged by the dephasing channel ω ↦ (ω + Z_A ω Z_A)/2 on A, i.e. it has no |0⟩⟨1| or |1⟩⟨0| blocks in A.
  Otherwise it is arbitrary: the second register may be in any state, entangled with the rest of E and with
  other malformed copies, and the copy may depend on everything listed above. Examples: Regev's bad
  registers |b, x⟩ (b, x arbitrary), mixtures of them, and a coset state whose first qubit has fully
  decohered with no record of the decoherence retained in E. It is in tensor product with clean copies,
  with RLS's workspace and with every qubit RLS prepares after its delivery (in particular the fair-bit
  qubits).
* A **clean** copy is, at the moment of its delivery, a fresh ρ_s in tensor product with everything else
  (E, all other copies, RLS's workspace).
* The adversary interacts with RLS only by supplying copies. It learns RLS's measurement outcomes as stated
  above, but after delivery it cannot act on the copy or on RLS's quantum or classical systems. All
  measurements (RLS's and the adversary's) have countably many outcomes.

RLS is not told which copies are malformed. The clean problem is the case in which no copy is malformed.
This section restates the error_model string of the fifth claim in `submission.json`, which governs.

## 6. Algorithm RLS

### 6.1 Acquisition and permutation (n ≥ 2048)

1. Acquire Q copies, one after another, and hold all of them. **No measurement and no fair bit is
   made before the last copy has been delivered.**
2. Draw Q keys Y_1, …, Y_Q of κ fair bits each (A4). If two keys are equal, measure everything and
   output 0. Otherwise sort the copies by key (merge sort on (key, index) pairs) and let π(p) be the
   index of the copy of rank p (p = 1, …, Q). The table p ↦ π(p) is stored.

### 6.2 Slot layout

Ranks are grouped into G consecutive blocks of 2M + K₃ + k ranks, block i belonging to guess g_i. Inside block i,
the first M ranks form the **tier-1 block**, the next M the **tier-2 block**, the next K₃ the **tier-3 block**, and the
last k the **test block**.

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
2. *Sieve stages.* For m = 1, …, R_ℓ:
   * **Shuffle and group.** Every label of W_{m−1} is ≡ 0 mod 2^{(m−1)b}; the key of x is floor(x/2^{(m−1)b}) mod 2^b.
     Draw for every record a fresh shuffle key of κ_s fair bits; if two shuffle keys coincide, release everything and
     declare the guess failed. Otherwise sort W_{m−1} by (key, shuffle key) (merge sort). When the shuffle keys are
     distinct, the order within each key group is uniformly random.
   * **Pair.** Within each key group, in list order, form pairs (1st, 2nd), (3rd, 4th), …; a last unpaired record is
     released (its qubit measured and released, its label discarded).
   * **Combine.** For each pair (a, a′), in list order of a, apply A5 with a as control; on outcome 1 output the record
     (qubit a, label (x_a − x_{a′}) mod 2^t), on outcome 0 release both qubits. W_m = the outputs, in list order of
     their first members.

   Every label of W_m is ≡ 0 mod 2^{mb}. For a record of W_{R_ℓ} write w = label/2^{R_ℓb} ∈ [0, 2^d) (t − R_ℓb = d).
3. *Sample.* If R_ℓ = 0 (tier 3), keep all K₃ records of W_0, in rank order. If R_ℓ ≥ 1: if |W_{R_ℓ}| < K_ℓ, release
   everything and declare the guess failed; otherwise draw a key of κ_W fair bits for every record of W_{R_ℓ}; on a tie,
   release everything and declare the guess failed; otherwise keep the K_ℓ records with the smallest keys, in key order
   (a uniformly random K_ℓ-subset in uniformly random order), and release the rest.
4. *Records.* For the j-th kept record (j = 1, …, K_ℓ): draw 3 fair bits forming m′_j; apply P2 (= A3) with m′_j to
   its qubit, giving b_j; store (w_j, m′_j, b_j).
5. *Search* (Section 6.7) with d = d_ℓ and these K_ℓ records, giving θ̂_ℓ ∈ [0, 2^{d_ℓ}) or "fail" (then the guess
   failed). Otherwise replace σ_low by σ_low + 2^{j_ℓ}θ̂_ℓ ∈ [0, 2^{j_ℓ + d_ℓ}).

### 6.5 One guess

For guess g: put σ_low = 0 and run TIER(1), TIER(2) and TIER(3), in this order, on the three tier blocks of the guess,
stopping as soon as the guess failed. As j_{ℓ+1} = j_ℓ + d_ℓ (ℓ = 1, 2), each tier starts with σ_low ∈ [0, 2^{j_ℓ}). If all
three tiers succeed, the **candidate** is s′ = σ_low ∈ [0, 2^n) (j₃ + d₃ = n).

### 6.6 The score of a search

Given d and K records (w_j, m′_j, b_j) with w_j ∈ [0, 2^d): for i = 0, …, d−1 let c_{j,i} = floor(2^p frac(2^i w_j/2^d))
(the controller reads the p bits of w_j at positions d−i−p, …, d−i−1, the missing low positions zero-filled:
c_{j,i} = floor(w_j 2^{p+i−d}) mod 2^p, O(p) indexed bit reads). For τ ∈ [0, 2^d)
with bits τ = Σ_i τ_i 2^i define

  V_j(τ) = (Σ_{i<d} τ_i c_{j,i}) mod 2^p,  h_j(τ) = floor(V_j(τ)/2^{p−q}),  k_j(τ) = (h_j(τ) − 2^{q−3}m′_j) mod 2^q,
  Σ(τ) = Σ_{j=1}^{K} (−1)^{b_j} c_{k_j(τ)} ∈ Z,  S(τ) = Σ(τ)/2^{25} = Σ_j Z̃_j(τ),  Z̃_j(τ) = (−1)^{b_j} table[k_j(τ)],

with the table c_k of App. B (table[k] = c_k/2^{25}), and the marking functions f_i of 6.7.

### 6.7 Search (threshold ladder)

For i = 1, …, I (level i) let f_i(τ) = 1 iff 2^i·Σ(τ) > 2^{25}·K (i.e. S(τ) > 2^{−i}K); f_i is evaluated classically for
one τ in O(K d p + I) bit operations. For i = 1, …, I: do the following at most 7 times: prepare d fresh qubits in
|0^d⟩, apply H to each, apply 𝒢_i = 𝒟·𝒪_i (App. C, with the marking function f_i) exactly k_G times, and measure,
giving τ̂; evaluate f_i(τ̂) classically; if f_i(τ̂) = 1, return τ̂. If no level returns a value, return "fail".

### 6.8 TEST(v) (the k copies of the test block of guess i)

For each copy: controlled on its first qubit, apply P1 with a = (N − v) mod N (subtracting v from the
register); apply H to the first qubit and measure it; release the copy. Let Z be the number of outcomes
0. Accept iff 40000Z ≥ 20001k, i.e. Z ≥ k(1/2 + 1/40000).

### 6.9 Output (n ≥ 2048)

For i = 0, …, G−1: run guess g_i (6.5); if it does not fail and its candidate s̃ satisfies s̃ < N, run
TEST((s̃ + g_i) mod N) on the test block of guess i, and if it accepts, output (s̃ + g_i) mod N and halt. If no
candidate is accepted, output 0. (Copies of unused blocks are measured and released at the end; they were acquired in
step 6.1.)

### 6.10 Small inputs (n < 2048)

Acquire Q_s = N·K_s copies and hold them (no measurement before the last delivery). Draw Q_s keys of κ′
fair bits; on a tie output 0; otherwise sort as in 6.1, and give candidate v ∈ [0, N) the K_s copies of
ranks vK_s + 1, …, (v+1)K_s. For each v run the test of 6.8 with this v on its K_s copies (k replaced by
K_s), giving the number Z_v of outcomes 0. Output the smallest v with 40000Z_v ≥ 20001K_s, or 0 if there is
none.

## 7. Correctness

### 7.1 Delivery before measurement, and the permutation

**Lemma N (no information).** In RLS the adversary's choices c_1, …, c_Q, the contents of the malformed
copies, and its operations on E up to the last delivery are made without any measurement outcome of
RLS. After the last delivery, conditioned on the adversary's own outcomes up to that time (a history h
of positive probability, outcome sets being countable), the malformed set 𝓜_h ⊆ {1,…,Q} is fixed,
|𝓜_h| ≤ floor(εQ), and the joint state of the copies and E is ⊗_{j∉𝓜_h} ρ_s ⊗ ω_h for some state
ω_h of the malformed copies and E, in tensor product with RLS's fresh qubits; and the joint state of all copies
and E is unchanged by the dephasing of the first qubit A_j of every malformed copy j. (At its delivery A_j is
dephased jointly with every earlier copy, the rest of its copy and E, which contains every later copy;
later operations and measurements of the adversary act only on E and commute with the dephasing of A_j, and
conditioning on their outcomes preserves the invariance.)

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
(1963), Theorem 4 with Theorem 1, Section 6), as in Lemma H. Applied to the unmarked items it gives the same bound
for P(X ≤ mK₀/N₀ − τm). ∎

**Notation in Section 7.** Some letters have local meanings: G_m, P_m, C_m count good, bad and C-bad records and
g_k, p_k, c_k are the sequences of Lemma Z_D (k a running index), unrelated to the grid size G = 2^{256}, the grid
points g_i, the phase-bit count p, the test-block size k, the table entries c_k of App. B and the wrap probability ϖ;
in Corollary KS and the proof of Lemma S₁_D, G and P abbreviate G_{m−1} and P_{m−1}. s is the secret,
s′ = (s − g*) mod N.

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
linearity) realise every clean copy of the three tier blocks of guess i* as ρ^{nw} or ρ^{w} by an independent coin W
with P(W = 1) = ϖ. A copy of these blocks is **good** if it is clean and W = 0, and **bad** otherwise. For ℓ = 1, 2, 3
put θ_ℓ = floor(s′/2^{j_ℓ}) mod 2^{d_ℓ}. As j₁ = 0, j_{ℓ+1} = j_ℓ + d_ℓ and j₃ + d₃ = n, we have
s′ mod 2^{j_ℓ + d_ℓ} = (s′ mod 2^{j_ℓ}) + 2^{j_ℓ}θ_ℓ for each ℓ, and s′ = θ₁ + 2^{j₂}θ₂ + 2^{j₃}θ₃. Let E_ℓ be the event
that tier ℓ of guess i* is run and starts with σ_low = s′ mod 2^{j_ℓ} (for ℓ = 1: that guess i* is run).

The **genie run** is the modified process (an analysis device, not an event) in which, in tier ℓ of guess i* on the
event E_ℓ (ℓ = 1, 2, 3), the label returned by F_t for every good leaf is replaced by its true label u of Lemma S (F's
tests are still performed and their outcomes ignored); otherwise it follows the rules of RLS. No step of RLS reads ζ,
so in the analysis step 4 of every leaf is replaced by its ζ-average (the same channel): ζ is not a random variable of
either run, and "the past", "all outcomes" and 𝒦_0 never include it. Realise all measurement outcomes of both runs
from one common sequence of independent uniforms, through their conditional laws given the past. The two runs take
the same actions until the first good leaf with û ≠ u. Guess i* processes at most 2M + K₃ ≤ Q leaves, each good leaf
whose label is replaced with P(û ≠ u | past) < 1/(100Q), so the runs differ with probability < 1/100.

### 7.5 Structure of the tiers in the genie run

Consider tier ℓ of guess i* on the event E_ℓ, in the genie run: t = t_ℓ, R_t = R_ℓ stages, and stage m (1 ≤ m ≤ R_t)
reads the label bits l_{m−1}, …, l_m − 1 with l_m = mb, so its width is b_m = b and l_0 = 0; W_0 is the list of leaves
and W_m the output of stage m. In 7.5–7.7, "the past" and every conditioning exclude, in addition, the F_t outcomes of
the tier's good leaves (the genie run never reads them, so by linearity we may average over them); step-3 outcomes may
be included or not (Lemma S holds conditionally on them, with σ_low = s′ mod 2^{j_ℓ} and σ_hi = floor(s′/2^{j_ℓ})). A
record is **good** if every leaf of its combination tree is a good leaf, and **bad** otherwise; G_m and P_m are the
numbers of good and bad records of W_m.

**Lemma C (fair coins).** Let a pair contain at least one good record. Conditioned on the past (in the sense
above) and on the labels of all good records, the outcome of its A5 measurement is 0 or 1 with probability
exactly 1/2; in particular it is independent of the good members' labels. If both records are good, then on
outcome 1 the output qubit is φ_{σ_hi}(x_a − x_{a′}), in tensor product with everything else.

*Proof.* By invariant (J) of Lemma U at the preceding stage (Lemma U at stage m uses Lemma C only for the
pairs of stage m, so there is no circularity), a good record's qubit is φ_{σ_hi}(x) for its label x, in
tensor product with all other systems given the past and the good labels. Its computational-basis diagonal is (1/2, 1/2). Let ρ be the joint state of the pair
(and the rest) before the CNOT, and let o be the measured value. If a′ is good, P(o) = Σ_c ⟨c|ρ_a|c⟩·
⟨o⊕c|ρ_{a′}|o⊕c⟩ = Σ_c ⟨c|ρ_a|c⟩/2 = 1/2; if a is good, P(o) = Σ_c (1/2)⟨o⊕c|ρ_{a′}|o⊕c⟩ = 1/2. Because the
good qubit is in tensor product with everything else, the same computation holds conditioned on any
event of the other systems. For two good qubits A5 gives the stated outputs with probability 1/2 each,
whatever x_a, x_{a′} are. ∎

Let 𝒦_0 be the σ-algebra generated by: h; the rank map; everything before the tier (all outcomes of
earlier guesses and tiers); the coins W; the identity of the good leaves; and every outcome and label
of the bad leaves of the tier. It does not contain the step-3 outcomes, ζ or F's outcomes of the good
leaves of this tier, which no later step reads in the genie run. For m ≥ 1, let 𝒦_m be generated by 𝒦_{m−1}, the
stage-m keys and shuffle keys of all records of W_{m−1}, the pairing, all stage-m A5 outcomes, the stage-m release
outcomes, and the labels of the bad records of W_m.

**Lemma U (exact uniformity).** For m = 0, …, R_t: (U) conditioned on 𝒦_m, the values
floor(x_r/2^{l_m}) for the good records r of W_m are independent and uniform on [0, 2^{t−l_m}); and (J)
conditioned on 𝒦_m and on the labels of the good records of W_m, the joint state of all systems is
⊗_{r good in W_m} φ_{σ_hi}(x_r) ⊗ Ω_m, where Ω_m (the bad records of W_m, all held copies, released
systems other than the step-3 qubits and F_t test qubits of the tier's good leaves, which are averaged out,
and E) does not depend on the labels of the good records of W_m.

*Proof.* m = 0: by Lemma S and (2.1) the true labels of the good leaves are independent uniform on
Z/2^tZ, independent of everything in 𝒦_0 (good copies are in tensor product with all other systems and
the genie run ignores F's outcomes on them; the coins W are independent of the labels); given the labels,
each good leaf's first qubit is φ_{σ_hi}(u) in tensor product with everything else, which is (J).
Step m−1 → m: for a good record r of W_{m−1} write floor(x_r/2^{l_{m−1}}) = κ_r + 2^{b_m}ν_r with
κ_r ∈ [0, 2^{b_m}) its stage-m key and ν_r ∈ [0, 2^{t−l_m}). By hypothesis all κ_r, ν_r are independent
and uniform given 𝒦_{m−1}. The keys of bad records are 𝒦_{m−1}-measurable, so the grouping and the
pairing are functions of 𝒦_{m−1}, the keys and the fresh shuffle keys only, and do not depend on any ν_r. Every stage-m
measurement acts on records that are consumed or released at stage m, and its outcome law is independent
of the labels of the good records that survive into W_m. (i) A5 on a pair with a good member: a fair coin
(Lemma C). (ii) A5 on a bad–bad pair, and every release of a bad qubit outside a mixed pair: by (J) at m−1 these act
on Ω_{m−1} only. (iii) Release of an unpaired good record, or of the control of a good–good pair with outcome 0: a
computational-basis measurement of φ(x), a fair coin for every x. (iv) Release after a mixed pair with
outcome 0: before the CNOT the good qubit is φ(x) ⊗ (the bad side and E). The joint computational-basis
diagonal of the two qubits and the post-measurement state of E depend only on the bad side, because
the phase of φ(x) multiplies whole branches and drops out of every diagonal term. So these outcomes are
independent of x too. After a mixed pair with outcome 1 nothing is released; the bad output's state depends on
the consumed good label x only through off-diagonal terms, and x is determined by 𝒦_m (x = out + x_{a′} if the
good member is a, and x = x_a − out if it is a′, where out is the output label; both are 𝒦_m-measurable), so Ω_m may
depend on it. The labels of the bad outputs of W_m involve only bad-record labels and the labels
of good records consumed in mixed pairs (x_a − x_{a′} with one known term), and none of these belong to W_m.
Hence (J) at m: the surviving good qubits are untouched, except good–good outputs, which are
φ(x_a − x_{a′}) in tensor product (A5), and Ω_m collects everything else. For a good–good pair (a, a′)
with outcome 1, κ_a = κ_{a′} and both labels are ≡ 0 mod 2^{l_{m−1}}, so x_a − x_{a′} ≡ 2^{l_m}(ν_a − ν_{a′})
(mod 2^t) and the new value floor(x′/2^{l_m}) is (ν_a − ν_{a′}) mod 2^{t−l_m}. Over disjoint pairs these are
independent, each uniform because ν_a, ν_{a′} are independent and uniform. ∎

In particular, at the end of the sieve (m = R_ℓ, t − l_{R_ℓ} = d_ℓ) the values w_r = x_r/2^{R_ℓb} of the good records
of W_{R_ℓ} are independent and uniform on [0, 2^{d_ℓ}) given 𝒦_{R_ℓ}, and by (J) a good record's qubit is
φ_{σ_hi}(2^{R_ℓb}w_r) = (|0⟩ + e^{2πi w_r θ_ℓ/2^{d_ℓ}}|1⟩)/√2 (modulus 2^{t_ℓ}; only σ_hi mod 2^{d_ℓ} = θ_ℓ matters), in
tensor product with everything else. For tier 3 (R₃ = 0) these are the leaves themselves, with labels uniform on
[0, 2^{d₃}) given 𝒦_0.

**Lemma D (dephasing propagates).** Call a record *D-bad* if its tree contains a malformed leaf. In the genie
run, conditioned on the past, the joint state of all systems is unchanged by the dephasing
ω ↦ (ω + Z_q ω Z_q)/2 of the qubit q of every D-bad record. This also holds conditioned in addition on the labels
of the good leaves (by (2.1) each good leaf is a mixture over its label of product states in tensor product with the
malformed copies, and the argument applies to each component), and hence, by averaging, conditioned on any coarser
σ-algebra such as ℋ_{j−1} ∨ σ(m′_j) of 7.7.
*Proof.* For a malformed leaf this holds after the last delivery by Lemma N (global dephasing, Section 5).
Every later operation on the leaf before its record exists acts either on other systems or on c only as a
control: the controlled operations of LEAF steps 1 and 2 act as Σ_{c∈{0,1}} |c⟩⟨c| ⊗ U_c on c and the register
(with ancillas restored), which commutes with Z_c;
operations on other systems commute with the dephasing of c, and conditioning on outcomes of measurements of
other systems preserves invariance under a channel acting on c. In A5 with control a and target a′: if a is
dephased, CNOT commutes with Z_a and the measurement of a′, so the output a is dephased; if a′ is dephased,
CNOT conjugates Z_{a′} to Z_aZ_{a′}, and after a′ is measured in the computational basis, Z_{a′} acts as a sign on
each outcome branch, so the output a is dephased. Hence every D-bad record is dephased. ∎


**Classes.** A bad record is D-bad if its tree contains a malformed leaf, and *C-bad* otherwise (then its tree
contains a wrapped clean leaf). C-bad records are counted by C_m ≤ P_m.


### 7.6 Counting

**Lemma K (per stage).** At stage m let gg, gb, bb be the numbers of good–good, good–bad and bad–bad
pairs. Then, deterministically, gg ≥ (G_{m−1} − P_{m−1} − 2^b)/2 and gb + 2bb ≤ P_{m−1}. Given 𝒦_{m−1}
and the keys, G_m is a sum of gg conditionally fair coins, and P_m ≤ X + bb where X is a sum of gb
conditionally fair coins.

*Proof.* A key group with c records yields floor(c/2) ≥ (c − 1)/2 pairs, and at most 2^{b_m} ≤ 2^b
groups are nonempty, so there are at least (G_{m−1} + P_{m−1} − 2^b)/2 pairs. Each bad record lies in at
most one pair, so gb + 2bb ≤ P_{m−1} and gg ≥ #pairs − (gb + bb) ≥ #pairs − P_{m−1}. A good output arises
exactly from a good–good pair with outcome 1, and a bad output from a mixed pair with outcome 1 or from a
bad–bad pair. The coins are fair by Lemma C. ∎

Lemma KS (shuffled pairing, one key group) and Corollary KS (one stage: with G good and P bad records in at most 2^b
groups and Λ = 2b + 64, gg ≥ G²/(2(G + P)) − 2^b/2 − 4√(2^b(G + P)Λ/2) except with probability 4·2^b e^{−Λ}) are
stated and proved in App. F of `appendix.md`.

**Lemma Z_D (the sequences, dephased model).** Let δ = 1/384 and y = ε + 2^{−20} + 2^{−254} (so 1 − y > 0.9898·10^{−4}),
and define for k = 1, …, 4, with g₀ = (1 − y)M, p₀ = yM, c₀ = 4M/G = 2^{−254}M:

  g_k = (1 − 3δ)·g_{k−1}²/(4(g_{k−1} + p_{k−1})),  p_k = (1/2 + δ)p_{k−1},  c_k = (1/2 + δ)c_{k−1}.

Put z_k = p_k/g_k. Then, for k = 0, …, 4:

| k | z_k < | log₂(g_k/M) > |
| --- | --- | --- |
| 0 | 1.011·10^4 | −13.302 |
| 1 | 2.067·10^8 | −28.615 |
| 2 | 8.651·10^{16} | −58.248 |
| 3 | 1.515·10^{34} | −116.522 |
| 4 | 4.646·10^{68} | −232.076 |

Moreover p_k ≥ p₄ > 0.0638M, c_k ≤ c₀, c₂/g₂ < 2^{−197} and c₄/g₄ < 2^{−25}. With M = b·2^{b+520} and Λ = 2b + 64
(b ≥ 342): (i) for k = 1, …, 4, g_{k−1}/(1 + z_{k−1}) ≥ 2^{b+1}/δ and g_{k−1} ≥ 128(1 + z_{k−1})³2^bΛ/δ²; and (ii)
g_k ≥ g₄ > b·2^{b+287}, p_k > b·2^{b+516} and c_k ≥ c₄ > b·2^{b+262} for k ≤ 4.
*Proof.* z_k = (1/2 + δ)p_{k−1}·4(1 + z_{k−1})/((1 − 3δ)g_{k−1}) = ρ·z_{k−1}(1 + z_{k−1}) with ρ = 2(1 + 2δ)/(1 − 3δ) =
772/381 < 2.0263, and g_k = (1 − 3δ)g_{k−1}/(4(1 + z_{k−1})), so log₂(g_k/M) = log₂(g_{k−1}/M) − 2 − log₂(1 + z_{k−1}) +
log₂(381/384) with log₂(381/384) > −0.0114. z₀ = y/(1 − y) and g₀ = (1 − y)M > 0.9898·10^{−4}M; the table follows
by iterating these two identities (each entry was also computed in exact rational arithmetic, and every printed
bound holds). p₄ = (1/2 + δ)⁴yM > 0.0638M. c_k/g_k = (c_{k−1}/g_{k−1})·(1/2 + δ)·4(1 + z_{k−1})/(1 − 3δ), so
log₂(c_k/g_k) increases by log₂ρ + log₂(1 + z_{k−1}) < 1.019 + log₂(1 + z_{k−1}) per step, from log₂(c₀/g₀) < −240.69; this gives
c₂/g₂ < 2^{−197} and c₄/g₄ < 2^{−25}. (i) Write g = g_{k−1}, z = z_{k−1}. Here 128/δ² = 18874368 < 2^{24.17} and
Λ ≤ 2.19b (b ≥ 342), so the second condition follows from log₂(g/(b2^b)) ≥ 25.30 + 3 log₂(1 + z). With
log₂(g/(b2^b)) = 520 + log₂(g/M), the margins for k = 1, …, 4 exceed 441, 383, 267 and 37 bits. The first condition,
g/(1 + z) ≥ 768·2^b, is implied (it needs log₂(g/(b2^b)) ≥ 9.6 − log₂b + log₂(1 + z)). (ii) g₄ > 2^{−232.076}·b·2^{b+520}
> b·2^{b+287}; p_k ≥ p₄ > 0.0638·b·2^{b+520} > b·2^{b+516}; c₄ = (1/2 + δ)⁴c₀ > 0.0638·2^{−254}M > b·2^{b+262}. ∎

**Lemma B_D (bad leaves).** For guess i*, except with probability < 4e^{−2^{b}} + e^{−2^{433}} + e^{−300}: each of the tier-1 and tier-2 blocks has
at most yM bad leaves, at most 4M/G of them C-bad (wrapped); and the tier-3 block has at most (ε + 2^{−20})K₃
malformed and at most 2^{−24}K₃ wrapped leaves.
*Proof.* Tier-1 or tier-2 block: Lemma H with τ = 2^{−20} gives fewer than (ε + 2^{−20})M malformed copies except with
probability e^{−2·2^{−40}M} = e^{−b·2^{b+481}}, and Lemma A for the wrap coins (independent, P(W = 1) < 2/G, at most M
of them) gives fewer than 4M/G wrapped copies except with probability e^{−2(2M/G)²/M} = e^{−8M/G²} = e^{−b·2^{b+11}}.
Tier-3 block: Lemma H with τ = 2^{−20} gives fewer than (ε + 2^{−20})K₃ malformed copies except with probability
e^{−2^{−39}K₃} = e^{−2^{433}(2b+8)}; the expected number of wrapped copies is < 2K₃/G, and by Lemma A at most
2K₃/G + √(150K₃) < 2^{−24}K₃ of them are wrapped except with probability e^{−300} (K₃ > 2^{472}). ∎

**Lemma S₁_D (the sieve stages, dephased model).** Let ℓ ∈ {1, 2} and consider tier ℓ of guess i* in the genie run
on E_ℓ, given the conclusion of Lemma B_D for its block. Except with probability R_ℓ(2^{−2b−70} + (4·2^b + 3)e^{−2b−64}),
G_m ≥ g_m, P_m ≤ p_m and C_m ≤ c_m for m = 0, …, R_ℓ (Lemma Z_D). Consequently the good fraction of W_{R_ℓ} is
f_g = G_{R_ℓ}/|W_{R_ℓ}| ≥ 2^{R_ℓ}g_{R_ℓ}/M ≥ γ := 2^{−228.08} (tier 1: 16g₄/M > 2^{−228.076}; tier 2: 4g₂/M > 2^{−56.248}),
the C-bad fraction is f_C = C_{R_ℓ}/|W_{R_ℓ}| ≤ (c_{R_ℓ}/g_{R_ℓ})f_g < 2^{−25}f_g, and |W_{R_ℓ}| ≥ G_{R_ℓ} ≥ g₄ > K_ℓ.
*Proof.* The induction follows RLS-D3 (0a76fda2) and is given in full here, stage by stage. m = 0 holds by hypothesis
(G₀ ≥ (1 − y)M = g₀, P₀ ≤ yM = p₀, C₀ ≤ 4M/G = c₀). Stage m: the shuffle keys of 6.4 are distinct except with
probability at most M²2^{−κ_s} ≤ 2^{−2b−70}. Write G = G_{m−1}, P = P_{m−1}, g = g_{m−1}, z = z_{m−1}; then G ≥ g
and P/G ≤ z. By Lemma Z_D(i), which is monotone in G, G/(1 + z) ≥ 2^{b+1}/δ and G ≥ 128(1 + z)³2^bΛ/δ². Hence
2^b/2 ≤ δG/(4(1 + z)) and 4√(2^b(G + P)Λ/2) ≤ 4√G·√(2^b(1 + z)Λ/2) ≤ 4√G·√(Gδ²/(256(1 + z)²)) = δG/(4(1 + z)). As
G/(1 + z) ≤ G²/(G + P), Corollary KS gives gg ≥ (1 − δ)G²/(2(G + P)) ≥ (1 − δ)g²/(2(g + p_{m−1})) (x²/(x + y)
increases in x and decreases in y), except with probability 4·2^b e^{−Λ}. By Lemma A, G_m ≥ (1/2 − δ)gg except with
probability e^{−2δ²gg}, and (1/2 − δ)(1 − δ)/2 ≥ (1 − 3δ)/4 gives G_m ≥ g_m. For the bad records (Lemma K),
P_m ≤ X + bb with X a sum of gb ≤ P_{m−1} fair coins and gb + 2bb ≤ P_{m−1}; by Lemma A, P(X ≥ gb/2 + δp_{m−1}) ≤
e^{−2δ²p_{m−1}}, and otherwise P_m ≤ P_{m−1}/2 + δp_{m−1} ≤ (1/2 + δ)p_{m−1} = p_m. Likewise C_m ≤ X_C + cc, where X_C
is a sum of gc fair coins (pairs of a C-bad and a good record, Lemma C), cc is the number of pairs of two C-bad
records, and gc + 2cc ≤ C_{m−1}; a pair of a C-bad and a D-bad record gives a D-bad output by definition. By Lemma A,
X_C ≤ gc/2 + δc_{m−1} except with probability e^{−2δ²c_{m−1}}, and then C_m ≤ (1/2 + δ)c_{m−1} = c_m. By Lemma Z_D(ii),
gg ≥ 2g_m, p_{m−1} and c_{m−1} all exceed 2^{b+262}, so every e^{−2δ²x} above is < e^{−2^{b+245}} < e^{−2b−64}; and
Λ = 2b + 64. Finally |W_m| ≤ |W_{m−1}|/2 (every output uses two records), so |W_{R_ℓ}| ≤ 2^{−R_ℓ}M, and the fractions
follow from G_{R_ℓ} ≥ g_{R_ℓ}, C_{R_ℓ} ≤ c_{R_ℓ} ≤ (c_{R_ℓ}/g_{R_ℓ})G_{R_ℓ} and Lemma Z_D; g₄ > b·2^{b+287} > 2^{472}(n + 8) ≥ K_ℓ. ∎

**Lemma S₂_D (samples).** Let ℓ ∈ {1, 2}. Given W_{R_ℓ} with the conclusion of Lemma S₁_D, the sample keys of tier ℓ
are distinct except with probability < 2^{−11}, and then the K_ℓ kept records are a uniformly random K_ℓ-subset of
W_{R_ℓ}, independent of everything else. Except with probability 2e^{−2^{14}}, the kept records contain
n_g ≥ γK_ℓ/2 good records and n_C ≤ n_g/16 C-bad records.
*Proof.* As in Lemma Π (|W_{R_ℓ}| ≤ M, κ_W = 2·bitlength(M) + 10). Given 𝒦_{R_ℓ}, the good and the C-bad counts are
hypergeometric with means f_gK_ℓ and f_CK_ℓ. By Lemma H′ (applied to the count of non-good records for the lower tail) with deviation γK_ℓ/64, n_g ≥ (f_g − γ/64)K_ℓ ≥ (63/64)f_gK_ℓ
≥ γK_ℓ/2 and n_C ≤ (f_C + γ/64)K_ℓ ≤ (2^{−25} + 1/64)f_gK_ℓ ≤ (2^{−25} + 1/64)(64/63)n_g < n_g/16, each except with
probability e^{−2(γ/64)²K_ℓ} ≤ e^{−2^{−467.2}·2^{472}(d_ℓ + 8)} < e^{−2^{14}} (d_ℓ + 8 ≥ 688). ∎

For tier 3 (no stage, no sample) Lemma B_D gives directly n_g ≥ (1 − ε − 2^{−20} − 2^{−24})K₃ > 0.9898·10^{−4}K₃ ≥ γK₃/2
good records and n_C ≤ 2^{−24}K₃ < n_g/16 C-bad records.

### 7.7 Records and scores

Fix a search of guess i* in the genie run: the search of tier ℓ on the event E_ℓ, with d = d_ℓ, target θ = θ_ℓ and the
K = K_ℓ records of step 4. Define the record filtration as follows. If R_ℓ ≥ 1 (tiers 1 and 2), let ℋ_0 be generated by
𝒦_{R_ℓ} (Lemma U: it contains the keys, pairings, A5 outcomes and bad labels, but not the labels w of the good records
of W_{R_ℓ}), the sample keys of step 3 and the release outcomes of the records not kept; if R_ℓ = 0 (tier 3), let
ℋ_0 = 𝒦_0. For j ≥ 1 let ℋ_j = ℋ_{j−1} ∨ σ(w_j, m′_j, b_j). Then the record (w_j, m′_j, b_j) is ℋ_j-measurable, and
whether record j is good, C-bad or D-bad is ℋ_0-measurable (it is fixed by the malformed set, the coins W, the sieve structure and the
sample). The release of a record not kept is a computational-basis measurement: for a good record it is a fair coin for
every label (φ(x) has diagonal (1/2, 1/2)), and for a bad record it acts only on Ω (invariant (J)).

Lemmas R (record laws: a good record's w_j is uniform given ℋ_{j−1}, m′_j uniform and independent, b_j with the law
of A3 for the phase w_jθ/2^d), B (bounded influence: |Z̃_j(τ)| ≤ R₀), E (discretisation: |Z̃_j(τ) − X̂_j(τ)| ≤ η with
X̂_j(τ) = (−1)^{b_j}cos(2π(w_jτ/2^d − m′_j/8))), C* (clean correlation: for a good record E[X̂_j(τ) | ℋ_{j−1}] is 1/2 at
τ = θ and 0 elsewhere) and M (any record: E[Z̃_j(τ) | ℋ_{j−1}] ∈ [−(1/2 + η), 1/2 + η]) are stated and proved, for the
filtration just defined, in App. E of `appendix.md`.

**Lemma Z0 (dephased records have mean zero).** If record j is D-bad, then for every τ ∈ [0, 2^d) and every history
in ℋ_{j−1} of positive probability, E[Z̃_j(τ) | ℋ_{j−1}] = 0.
*Proof.* w_j is ℋ_0-measurable (a label of a bad record) and m′_j is drawn from fresh qubits, so it is uniform and
independent of ℋ_{j−1}; every generator of ℋ_{j−1} is obtained before the P2 of record j (as in Lemma M). By Lemma D, conditioned on ℋ_{j−1} and m′_j, the joint state is unchanged by the
dephasing of record j's qubit; P2 applies the diagonal unitary (T†)^{m′_j}, which commutes with Z, and then H and a
computational-basis measurement, so b_j is a fair coin given ℋ_{j−1} and m′_j. Since table[k_j(τ)] is a function of
w_j, m′_j and τ, E[(−1)^{b_j}table[k_j(τ)] | ℋ_{j−1}, m′_j] = 0. ∎

### 7.8 The ladder isolates the target

**Theorem M_D (the scores separate the target).** Fix a search of guess i* as in 7.7, with K records of which
n_g ≥ γK/2 are good and n_C ≤ n_g/16 are C-bad (all others D-bad). Then, except with probability < 2^{−40},
S(θ) > 0.437n_g > 2^{−I}K and S(τ) < 0.063n_g < S(θ)/2 for every τ ≠ θ; in particular S(τ) < K/2.
*Proof.* For τ ∈ [0, 2^d) let m_j(τ) = E[Z̃_j(τ) | ℋ_{j−1}] and D_j(τ) = Z̃_j(τ) − m_j(τ). Then E[D_j(τ) | ℋ_{j−1}] = 0
and D_j(τ) ∈ [a_j, a_j + 2R₀] with a_j = −R₀ − m_j(τ) ℋ_{j−1}-measurable. With δ_s = γ/64, Lemma A (rescaled by 2R₀)
gives P(Σ_j D_j(θ) ≤ −δ_sK) ≤ e^{−δ_s²K/(2R₀²)} and, for τ ≠ θ, P(Σ_j D_j(τ) ≥ δ_sK) ≤ e^{−δ_s²K/(2R₀²)}. Now
δ_s²K/(2R₀²) ≥ 2^{−468.17}·2^{472}(d + 8)/2.0001 > 6.9(d + 8), so a union bound over the 2^d candidates gives
< 2^{d}e^{−6.9(d+8)} < 2^{−40}. On the complement, Lemmas C*, M and Z0 give (the good records contribute ≥ 1/2 − η at
θ and ≤ η elsewhere, the C-bad ones at least −(1/2 + η) and at most 1/2 + η, the D-bad ones 0), with δ_sK = γK/64 ≤ n_g/32:
S(θ) > n_g(1/2 − η) − n_C(1/2 + η) − δ_sK ≥ n_g(1/2 − η − (1/2 + η)/16 − 1/32) > 0.437n_g, and for τ ≠ θ,
S(τ) < n_gη + n_C(1/2 + η) + δ_sK ≤ n_g(η + (1/2 + η)/16 + 1/32) < 0.063n_g. Finally 0.437n_g ≥ 0.437·2^{−229.08}K >
2^{−232}K = 2^{−I}K, and 0.063n_g ≤ 0.063K < K/2. ∎

**Lemma Sr_D (ladder search).** If S(θ) > 2^{−I}K and S(τ) < min(S(θ)/2, K/2) for every τ ≠ θ, the search of 6.7
returns θ except with probability ≤ 2^{−7}.
*Proof.* d ≥ 680 ≥ 4. Let ι be the least i ∈ {1, …, I} with S(θ) > 2^{−i}K. For i < ι, S(θ) ≤ 2^{−i}K and every
S(τ) < S(θ), so f_i marks nothing and every τ̂ fails the classical check: level i returns nothing. At level ι, f_{ι}
marks θ, and no τ ≠ θ: if ι = 1, S(τ) < K/2; if ι ≥ 2, S(τ) < S(θ)/2 ≤ 2^{−(ι−1)}K/2 = 2^{−ι}K. With exactly one
marked value, each repetition is an independent run of the circuit of App. C on fresh qubits and returns θ with
probability > 1/2 (Lemmas G and I, App. D), and the classical check accepts exactly θ. So level ι returns θ unless all
seven repetitions fail, which has probability < 2^{−7}. ∎

### 7.9 The test

**Lemma T_D (test, dephased model).** Let μ_i be the fraction of malformed copies in the test block of guess i.
If μ_i ≤ ε + 1/80000, then TEST(s) accepts except with probability e^{−700}, and for every v ≠ s, TEST(v)
accepts with probability at most e^{−1300}, whatever happened before. TEST accepts iff Z ≥ k(1/2 + 1/40000).
*Proof.* After subtracting v, a clean copy's first qubit is |+⟩ if v = s and maximally mixed if v ≠ s; a
malformed copy's first qubit stays dephased (the subtraction is controlled by it), so H gives a fair coin.
For v = s: Z ≥ (1 − μ_i)k + Y where Y is a sum of μ_ik fair coins; Z ≥ k/2 + 2.5·10^{−5}k unless
Y < μ_ik/2 − 1.875·10^{−5}k, because (1 − μ_i)k/2 ≥ (10^{−4} − 1.25·10^{−5})k/2 = 4.375·10^{−5}k; by Lemma A this
has probability ≤ e^{−2(1.875·10^{−5})²k} < e^{−700} (k = 2^{40}). For v ≠ s every outcome is a fair coin, and
Z ≥ k/2 + 2.5·10^{−5}k has probability ≤ e^{−2(2.5·10^{−5})²k} < e^{−1300}. ∎
By Lemma H, P(μ_i > ε + 1/80000) ≤ e^{−2k/80000²} < e^{−340}; G = 2^{256} < e^{178}, so G e^{−340} < e^{−162}.

### 7.10 Theorem 1 (n ≥ 2048)

**Theorem 1.** For every N with n ≥ 2048, every s and every adversary of Section 5, RLS outputs s with probability at
least 9/10.
*Proof.* Exclude: the tie of 6.1 (< 2^{−11}, Lemma Π); some test block with μ_i > ε + 1/80000 (≤ G e^{−340} < e^{−162});
TEST(s) rejecting at guess i*, or some TEST(v), v ≠ s, accepting, given the previous event fails (≤ e^{−700} +
G e^{−1300}); the genie run differing from the real run (< 1/100, 7.4); for guess i*, the events of Lemma B_D
(< 4e^{−2^b} + e^{−2^{433}} + e^{−300}), of Lemma S₁_D in tiers 1 and 2 (< 6(2^{−2b−70} + (4·2^b + 3)e^{−2b−64})) and of Lemma S₂_D in
tiers 1 and 2 (< 2(2^{−11} + 2e^{−2^{14}})); the failure of Theorem M_D in the search of tier ℓ of guess i* on E_ℓ,
ℓ = 1, 2, 3 (< 3·2^{−40}); and the failure of Lemma Sr_D in these three searches (< 3·2^{−7}). As b ≥ 342, the total is
< 0.0005 + 0.01 + 0.001 + 0.0235 + 10^{−9} < 0.036.
Outside these events, suppose no earlier guess has output s (otherwise RLS has output s). No earlier guess output
anything else (no wrong candidate is accepted), so guess i* is run and E₁ holds. If E_ℓ holds (ℓ ∈ {1, 2, 3}), the tier
does not fail in steps 2–3 (Lemmas S₁_D and S₂_D: no shuffle or sample tie, and |W_{R_ℓ}| ≥ K_ℓ), and its K_ℓ records
contain n_g ≥ γK_ℓ/2 good and n_C ≤ n_g/16 C-bad records (Lemma S₂_D; for tier 3, the remark after it). So the scores
separate the target (Theorem M_D) and the search returns θ̂_ℓ = θ_ℓ (Lemma Sr_D). Then σ_low becomes
(s′ mod 2^{j_ℓ}) + 2^{j_ℓ}θ_ℓ = s′ mod 2^{j_ℓ + d_ℓ} (7.4), so E_{ℓ+1} holds for ℓ ≤ 2, and after tier 3 the candidate is
s̃ = s′ mod 2^n = s′ < N, with (s̃ + g*) mod N = s. TEST(s) accepts on the test block of guess i* (Lemma T_D). So RLS
outputs s with probability > 0.96 ≥ 9/10. ∎

### 7.11 Small inputs (n < 2048)

**Theorem 2.** For every N with n < 2048, every s and every adversary of Section 5, the branch of 6.10 outputs s with
probability > 0.99.
*Proof.* Lemmas N and Π hold verbatim for this branch (P(tie) < 2^{−11}). Let f_v be the malformed fraction among the
K_s copies of candidate v. By Lemma H, P(f_v > ε + 1/80000) ≤ e^{−2K_s/80000²} < e^{−5400}. If f_s ≤ ε + 1/80000, the
argument of Lemma T_D (with k = K_s = 2^{44}) shows that s is accepted except with probability
e^{−2(1.875·10^{−5})²K_s} < e^{−12000}; for v ≠ s with f_v ≤ ε + 1/80000, v is accepted with probability
≤ e^{−2(2.5·10^{−5})²K_s} < e^{−21000}. A union bound over the N ≤ 2^{2047} < e^{1419} candidates gives total failure
< 2^{−11} + e^{1419}(e^{−5400} + e^{−12000} + e^{−21000}) < 0.01. ∎

Theorems 1 and 2 cover every N ≥ 2 and every s, for every adversary of Section 5 with ε(n) = 9999/10000, and in
particular for the clean problem.

## 8. Resources (every branch)

For n < 2048 every quantity is an absolute constant: at most Q_s ≤ 2^{2047}·2^{44} copies, O(Q_s n + Q_s log₂ Q_s·κ′)
bit operations and gates before the address charge (itself O(log Q_s)), (n+1)Q_s + O(n) qubits held and O(Q_s κ′) bits.
These constants are astronomically large but independent of N, s and all outcomes. Let n ≥ 2048.

**Sizes.** b ≤ n/6 + 1 and b ≤ n/2, so M = b·2^{b+520} ≤ (n/2)·2^{521}·2^{n/6}; K₁, K₂, K₃ ≤ 2^{472}(n + 8); G = 2^{256};
k = 2^{40}. Hence

  **Q = G(2M + K₃ + k) < 2^{256}(n·2^{521}·2^{n/6} + 2^{472}(n + 8) + 2^{40}) < 2^{778}·n·2^{n/6},**

counting every acquired copy (all are acquired in 6.1, on every branch; 2^{n/6} ≥ 2^{341} dominates the other terms).
Also log₂ Q < n/6 + log₂ n + 778, so κ, κ_s, κ_W < n + 2000 and L₁ < n/6 + 2 log₂ n + 800, i.e. κ, κ_s, κ_W, L₁, r₁ = O(n).

**Quantum space.** All Q copies are held from 6.1 until they are used: (n+1)Q qubits. In addition, at any time: one
copy's O(n) LEAF/F_t ancillas, one test control, one A4 qubit and one TEST ancilla set; in a search, the d search qubits,
U (w qubits), V (p) with O(p) ancillas, k (q), v (27) with O(q) ancillas, the O(w) ancillas of P3b, the flag with O(w)
carry ancillas, the diffusion target and its d − 2 ancillas: O(n) qubits, one fixed pool reused for every record, call,
repetition and ladder level. Measured qubits are released. **S_Q ≤ (n+1)Q + O(n) = O(2^{n/6} n²).**

**Classical space.** Sort keys and workspace and the rank table: O(Q(κ + bitlength(Q))) = O(Qn) bits. The current tier
of the current guess: at most M labels of n bits and M copy indices, the 2^b key counters, the shuffle keys and the
sample keys with merge-sort workspace: O(Mn) bits. The stored search records: K(d + 4) = O(n²) bits. The table:
27·2^{24} bits (an absolute constant). F_t counters, parameters, σ_low, the ladder and Grover controller (I, K_G, k_G,
counters, Θ_i) and one gate description: O(n²) bits. **S_C = O(Qn) = O(2^{n/6} n²).** Hence 𝔐 = O(2^{n/6}n²),
log₂(𝔐 + 2) < n/6 + 3 log₂ n + O(1), and **A = O(n)**.

**Work** (every operation charged O(A) = O(n)).
* Acquisition: Q(n+1). Keys and merge sort of 6.1: O(Q log₂ Q·κ) = O(Qn²) bit operations, O(Qn³) charged.
* Leaves (at most G(2M + K₃) ≤ Q of them): LEAF uses O(n) gates; F_t uses 8(J+1)r₁ ≤ 8n·r₁ kickback tests of O(n) gates;
  Lemma P and the rounding O(n²). A leaf costs O(n²r₁) = O(n³) operations, O(n⁴) charged; in total O(Qn⁴).
* Sieve stages and samples, per guess: R₁ + R₂ = 6 stages, each on at most M records, with O(Mκ_s) fair bits for the
  shuffle keys, a merge sort on (key, shuffle key) in O(M log₂ M·(b + κ_s)) bit operations, O(Mn) for subtractions and
  one A5 per pair; two samples with O(M log₂ M·κ_W): O(Mn²), O(Mn³) charged; over G guesses O(Qn³).
* Table (App. B): an absolute constant number of operations. Records: O(K) operations per search.
* Searches, per guess: three searches, each with I = 232 ladder levels of at most 7 repetitions of at most
  k_G ≤ 0.785·2^{d/2} ≤ 2^b ≤ 2·2^{n/6} Grover iterations (d₁ ≤ 2b and d₂ = d₃ = 2b). One call of 𝒪_i costs, per record,
  d applications of P3a on p qubits (O(dp)), O(p + q), one table read (O(2^q(q + 27)), an absolute constant) and one
  P3b (O(w)), done and undone, so O(K(dp + w)) = O(n² log n) gates (K ≤ 2^{472}(n + 8)); 𝒟 costs O(d). A repetition
  also evaluates f_i(τ̂) classically in O(Kdp) = O(n² log n). So each search costs O(2^{n/6} n² log n) operations,
  O(2^{n/6} n³ log n) charged; over G guesses the same order.
* TEST: G·k copies, O(n) gates each. Grid points and parameters: O(Gn²). Releasing unused blocks, or all copies on a
  tie: at most Q(n+1) measurements and resets.

The leaf term dominates: **T = O(Qn⁴ + 2^{n/6}n³ log n) = O(2^{n/6} n⁵).**

All four bounds hold simultaneously on every execution branch of this one algorithm with this one parameter rule
(every loop length is bounded by a fixed function of N; the copy count is exactly Q), jointly with Theorems 1 and 2,
for every adversary of Section 5.

## 9. Exact growth indices and structured envelopes

For ℬ(n) = 2^{n/6} n^r with fixed r ≥ 0: log₂ ℬ = n/6 + r log₂ n, so log₂ log₂ ℬ = log₂ n − log₂ 6 + log₂(1 + 6r log₂ n/n),
and log₂ log₂ ℬ/log₂ n → 1. Hence g(ℬ) = 1 (the max{4,·} is irrelevant for large n); outer constants do not change it.

* T: ℬ_T = 2^{n/6} n⁵, index **1**: exponent [{coefficient 1/6, nPower 1, logPower 0}], nPower 5, logPower 0.
* S_C: ℬ = 2^{n/6} n², index **1**: exponent [{1/6, 1, 0}], nPower 2, logPower 0.
* S_Q: ℬ = 2^{n/6} n², index **1**: exponent [{1/6, 1, 0}], nPower 2, logPower 0.
* Q: ℬ = 2^{n/6} n, index **1**: exponent [{1/6, 1, 0}], nPower 1, logPower 0.

Published time score: [1]. Under the asymptotic comparator every envelope is strictly below the corresponding
2^{n/3}·poly(n) envelope.

## 10. Fractional error tolerance

ε(n) = 9999/10000 under the model of Section 5: with Q acquired copies, at most floor(9999Q/10000) of them are malformed;
their positions are chosen adaptively by an adversary who knows N, s, the algorithm and all previous measurement outcomes
(RLS obtains none before the last delivery); a malformed copy is arbitrary except that its first qubit is dephased
jointly with everything else (the rest of the copy, every earlier copy, RLS's workspace and the adversary's system,
including every system the adversary later delivers), and it is in tensor product with clean copies and RLS's
workspace; every other copy is, at the moment of its delivery, an independent ideal coset state ρ_s in tensor product
with everything else, and the adversary has no access to a copy or to RLS's systems after delivery. For every N ≥ 2 (no
validity threshold: Theorem 2 covers n < 2048), every s and every such adversary, Theorems 1 and 2 give success
probability at least 9/10, jointly with the four resource bounds of Section 8, which hold on every branch for every
adversary. The clean problem is the special case with no malformed copy.

## 11. Credits, lineage and what is new

* The low-bit sieve step on Z/2^nZ is Kuperberg's (SIAM J. Comput. 35 (2005) 170–188, Section 3). Quantum search is
  Grover's (STOC 1996) with the two-reflection analysis of Boyer–Brassard–Høyer–Tapp (Fortschr. Phys. 46 (1998)),
  reproved in App. D. Nothing cited in this bullet is used as a premise.
* Our own components, re-proved here: the splice, F_t and A1–A4 (SLS, 59facd77); A5 and Lemma P (OMX-ML, 31c2d043); the
  full-upfront acquisition, the permutation and Lemmas N, Π, U, C, K and the genie run (RLS, 280a17e4); the globally
  dephased model, Lemma D, the shuffled pairing (Lemma KS, Corollary KS) and the stage induction (RLS-D3, 0a76fda2);
  the shadow score, the cosine table, the oracle circuits and Lemmas B, E, C*, M (ROB-G2, 55a6ce76; adapted to labels
  in Z/2^dZ); the three-tier sieve-then-search structure (our RLS-G1 4ef5cf09, RLS-G2 6b206bcf and RLS-G4 9e0af9a8 on this track). The
  dephased-copy line started with our ROB-GD and ROB-GD2 (6288f7bc, 4b79ce01).
* Positive-tolerance prior work in this model or others (credited, nothing used): dadon's f892f7ea (1/3, adaptive
  malformed-copy model); mpjunior92's PSG13 4c42d100; kaankolcu's RWT25 3f48c893 (1/4, fixed-position model); GordoAR's
  c730b22b (1/3, own model); ercumentyildirim's LSIEVE f2cb3153/0f4adc93 (oblivious model); smoke-era RGRST1 be98e61b, CGRST1
  53b4755b, CADGR1 5f048e8b/b838e1ae, CADGR2 45044787, RLQGR1–3 ee378bae, 635a47e2, 0e1559e4, 09c05313, 7b2afdfc. Regev
  (SIAM J. Comput. 33 (2004), Definition 2.1) studies DCP with a failure parameter; his bad registers are examples of
  malformed copies of Section 5.

Context (not part of any claim). New here: in the dephased model a corrupted record's shadow score has conditional mean
exactly zero, so the target's score is proportional to the number of clean records, however small, and a ladder of
2^{−i} thresholds finds the right scale without knowing that number. This lets sieve-then-search work with a vanishing
(but constant) fraction of clean records after four stages, and the tolerance 9999/10000 of RLS-D3 carries over from
work 2^{n/3}·poly to 2^{n/6}·poly. The error-model text is byte-identical to that of RLS-D3, so this entry is comparable
with it, and all four of its envelopes are strictly smaller. No cited result is used as a lemma except Hoeffding's
inequality for sampling without replacement (Lemmas H, H′), cited with its exact theorem number; Lemma A is proved in
the file.
