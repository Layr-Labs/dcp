# RLS-G6: a four-tier robust low-bit sieve with robust quantum search, O(2^{n/8} n⁴) work, adaptive malformed-copy tolerance 1/256

This file and `appendix.md` together are the complete proof of all five claims in `submission.json`. They
describe one algorithm, **RLS-G6** (below simply RLS), with one fixed parameter rule, and prove for every
integer N ≥ 2, every s ∈ Z/NZ, with n = ceil(log₂ N), and every adversary of the error model of Section 5
(which contains the clean problem as the adversary that corrupts nothing):

* the output equals s with unconditional probability at least 9/10 (> 2/3);
* total work T = O(2^{n/8} n⁴);
* peak classical space S_C = O(2^{n/8} n) bits;
* peak quantum space S_Q = O(2^{n/8} n) qubits;
* acquired source copies Q = O(2^{n/8}); Q is a fixed function of N, the same on every branch;
* fractional error tolerance ε(n) = 1/256: at most floor(Q/256) acquired copies may be malformed, at
  adversarially and adaptively chosen positions, with arbitrary, possibly entangled contents.

All constants are absolute (independent of N, s, the adversary and all outcomes). Every loop of RLS has a
length bounded by a fixed function of N, so the four resource bounds hold on every execution branch
whatever the copies contain. Logarithms are base 2 unless written ln. All four growth indices equal 1; the
time envelope has exponent n/8.

**Idea.** This entry is the R = 6 member of our sieve-then-search family: RLS-G1 (4ef5cf09, one stage, 1/7 at
2^{n/3}·poly), RLS-G2 (6b206bcf, two stages, 1/16 at 2^{n/4}·poly) and RLS-G4 (9e0af9a8, three tiers, 1/64 at
2^{n/6}·poly), all built on the robust shadow-score search of our ROB-G2 (55a6ce76). (i) All Q copies are acquired
before the first measurement, so the adversary, which sees only outcomes obtained before each delivery, chooses blind,
and a uniform permutation spreads its copies over all slot blocks. (ii) The SLS splice (59facd77) turns the copies of
the right grid guess g* into exact coset states of Z/2^{t}Z for the remaining t high bits of s′ = (s − g*) mod N;
wrapped copies are treated as malformed. (iii) With b = ceil(n/8), tier 1 runs six low-bit sieve stages of b bits on
Z/2^nZ and then a robust shadow-score quantum search finds the low d₁ = n − 6b ≤ 2b bits of s′ in O(2^{d₁/2}) ≤
O(2^{n/8}) oracle calls; tiers 2, 3 and 4 do the same with four, two and zero stages on the remaining 6b, 4b and 2b bits,
each finding 2b more bits. (iv) A stage roughly doubles the bad fraction (exactly: Lemma S₁): a bad record paired with
a clean one survives only on a fair coin and two bad records merge into one, while clean records shrink by 4 (Lemmas C,
K). Followed exactly through six stages (Lemma S₁), 1/256 malformed copies leave a bad-record fraction below 0.274,
below the bound 0.2959 assumed in Theorem M.

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
comparisons with constants, multi-controlled X and table reads), the cosine table (Lemma T), the oracle 𝒪 and
the diffusion 𝒟 are given in App. A–C of `appendix.md`, which is part of this proof.

**Cost convention.** Let 𝔐 be the number of allocated bits plus qubits. Section 8 shows
𝔐 = O(2^{n/8} n), so a classically indexed access or classically addressed gate costs
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

**Lemma P.** Let J, r ≥ 1. Suppose that for each level i ∈ {0,…,J} and each m′ ∈ {0,…,7} we obtain r
independent outcomes of A3 with this m′, applied to qubits (|0⟩ + e^{2πi2^iθ}|1⟩)/√2 for an unknown
real θ. Let Z_{i,m′} be the number of 0 outcomes, m_i the m′ maximising Z_{i,m′} (the smallest on ties),
β_i = m_i/8 and x_J = β_J. For i = J−1 down to 0, of c₀ = x_{i+1}/2 and c₁ = x_{i+1}/2 + 1/2 let x_i be
the one with smaller |c − β_i|∘ (c₀ on ties). Then with probability ≥ 1 − 16(J+1)e^{−r/200},
|x₀ − θ|∘ < 2^{−J}/8.

*Proof.* Write θ_i = frac(2^iθ). By Lemma A (Section 7.2; the r outcomes are independent indicators),
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

**Procedure F_t** (label of a t-qubit register). Let M′ = 2^t, J = max(1, t−2), r = r₁ (Section 4). For
each i ∈ {0,…,J} and m′ ∈ {0,…,7}, perform r kickback tests with a = 2^i mod M′, each followed by A3
with this m′ on its control. Apply Lemma P and output û = round(M′x₀) mod M′.

**Corollary F.** If the register is χ_{−u}, then û = u with probability ≥ 1 − 16(J+1)e^{−r/200}.
*Proof.* The test controls are the qubits of Lemma P with θ = u/M′ (Section 2). M′ ≤ 2^{J+2} (t ≥ 3:
J + 2 = t; t ≤ 2: M′ ≤ 4 < 8). On the success event M′x₀ differs from u + M′z by less than
M′2^{−J}/8 ≤ 1/2, so the rounding returns u, with no tie. ∎

## 4. Parameters (exact integer arithmetic, computed from N)

For **n ≥ 256**:

* **R** = 6 (stages of tier 1); **b** = ceil(n/8) (sieve bits per stage), so n/8 ≤ b ≤ n/8 + 1 and b ≥ 32.
* **T** = 4 tiers ℓ = 1, …, 4 with R_ℓ = R − 2(ℓ − 1) = 6, 4, 2, 0 stages, d₁ = n − 6b and d_ℓ = 2b for ℓ ≥ 2, low-bit
  counts j₁ = 0 and j_{ℓ+1} = j_ℓ + d_ℓ (so j₂ = d₁, j₃ = d₁ + 2b, j₄ = d₁ + 4b), and t_ℓ = n − j_ℓ; then
  t_ℓ − R_ℓb = d_ℓ, j₄ + d₄ = n, n/4 − 6 ≤ d₁ ≤ 2b, d₁ ≥ 59 and 2b ≥ 64, so every d_ℓ ≥ 59.
* **M** = 2^{b+21} (leaves of each of tiers 1, 2 and 3 per guess).
* **K_ℓ** = 2^{18}(d_ℓ + 8) (records of the search of tier ℓ).
* **G** = 2^{15} (grid size); grid points g_i = floor(iN/G) for i = 0, …, G−1. Since N ≥ 2^{255} > G, the g_i are
  distinct.
* **k** = 256·bitlength(100G) = 5632 (copies per test).
* **Q** = G(3M + K₄ + k) (copies acquired).
* L₁ = bitlength(1600(n+1)Q); **r₁** = 200L₁ (tests per bit level i and offset m′ in F_t).
* **κ** = 2·bitlength(Q) + 10 (sort-key bits); **κ_W** = 2·bitlength(M) + 10 (sample-key bits).
* Score: **q** = 24 (angle bits); **p** = q + 1 + bitlength(n) (phase bits); for a search with K records,
  **w** = bitlength(K) + 29 (accumulator width); threshold **θ₀ = 7/40**.
* Search over d qubits: K_G = floor(2^{d/2}) (the integer square root of 2^d), k_G = floor(785K_G/1000), at most 7
  repetitions.

Analysis constants (not used by the algorithm): ε = 1/256, δ = 1/768, τ_h = 2^{−13}, ȳ = ε + 2·2^{−13} = 17/4096,
δ_s = 1/200, τ_s = 1/400, τ_T = 2^{−24} (table accuracy), η = 3π2^{−24} + τ_T < 6.22·10^{−7}, R₀ = 1 + τ_T.

For **n < 256**: K_s = 2^{20}; Q_s = N·K_s; κ′ = 2·bitlength(Q_s) + 10 (Section 6.10).

## 5. Error model (adaptive malformed copies)

Copies are delivered one at a time in acquisition order j = 1, …, Q (Q is given by Sections 4 and 6.1).
An **adversary** knows N, s, the full description of RLS, and every measurement
outcome obtained by RLS before copy j is delivered; it holds an arbitrary private quantum system E which
it may measure and process. Before copy j is delivered it chooses c_j ∈ {clean, malformed}, as a function
of that information and its own outcomes; on every branch at most floor(εQ) copies are malformed,
ε = 1/256.

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

Ranks are grouped into G consecutive blocks of 3M + K₄ + k ranks, block i belonging to guess g_i. Inside block i,
the first M ranks form the **tier-1 block**, the next M the **tier-2 block**, the next M the **tier-3 block**, the next
K₄ the **tier-4 block**, and the last k the **test block**.

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
3. *Sample.* If R_ℓ = 0 (tier 4), keep all K₄ records of W_0, in rank order. If R_ℓ ≥ 1: if |W_{R_ℓ}| < K_ℓ, release
   all records of W_{R_ℓ} and declare the guess failed; otherwise draw a key of κ_W fair bits for every record of
   W_{R_ℓ}; on a tie, release all records of W_{R_ℓ} and declare the guess failed; otherwise keep the K_ℓ records with the smallest keys, in key order
   (a uniformly random K_ℓ-subset in uniformly random order), and release the rest.
4. *Records.* For the j-th kept record (j = 1, …, K_ℓ): draw 3 fair bits forming m′_j; apply P2 (= A3) with m′_j to
   its qubit, giving b_j; store (w_j, m′_j, b_j).
5. *Search* (Section 6.7) with d = d_ℓ and these K_ℓ records, giving θ̂_ℓ ∈ [0, 2^{d_ℓ}) or "fail" (then the guess
   failed). Otherwise replace σ_low by σ_low + 2^{j_ℓ}θ̂_ℓ ∈ [0, 2^{j_ℓ + d_ℓ}).

### 6.5 One guess

For guess g: put σ_low = 0 and run TIER(1), …, TIER(4), in this order, on the four tier blocks of the guess, stopping
as soon as the guess failed. As j_{ℓ+1} = j_ℓ + d_ℓ (ℓ = 1, 2, 3), each tier starts with σ_low ∈ [0, 2^{j_ℓ}). If all
four tiers succeed, the **candidate** is s̃ = σ_low ∈ [0, 2^n) (j₄ + d₄ = n).

### 6.6 The score of a search

Given d and K records (w_j, m′_j, b_j) with w_j ∈ [0, 2^d): for i = 0, …, d−1 let c_{j,i} = floor(2^p frac(2^i w_j/2^d))
(the controller reads the p bits of w_j at positions d−i−p, …, d−i−1, the missing low positions zero-filled:
c_{j,i} = floor(w_j 2^{p+i−d}) mod 2^p, O(p) indexed bit reads). For τ ∈ [0, 2^d)
with bits τ = Σ_i τ_i 2^i define

  V_j(τ) = (Σ_{i<d} τ_i c_{j,i}) mod 2^p,  h_j(τ) = floor(V_j(τ)/2^{p−q}),  k_j(τ) = (h_j(τ) − 2^{q−3}m′_j) mod 2^q,
  Σ(τ) = Σ_{j=1}^{K} (−1)^{b_j} c_{k_j(τ)} ∈ Z,  S(τ) = Σ(τ)/2^{25} = Σ_j Z̃_j(τ),  Z̃_j(τ) = (−1)^{b_j} table[k_j(τ)],

with the table c_k of App. B (table[k] = c_k/2^{25}), and the marking function f(τ) = 1 iff 40·Σ(τ) > 7·2^{25}·K
(i.e. S(τ) > θ₀K). f is evaluated classically for one τ in O(K d p) bit operations.

### 6.7 Search

Prepare d fresh qubits in |0^d⟩, apply H to each, apply 𝒢 = 𝒟·𝒪 (App. C, for this score) exactly k_G times, and
measure, giving τ̂; evaluate f(τ̂) classically; if f(τ̂) = 1 return τ̂. Do this at most 7 times; if all fail, return
"fail".

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
linearity) realise every clean copy of the four tier blocks of guess i* as ρ^{nw} or ρ^{w} by an independent coin W
with P(W = 1) = ϖ. A copy of these blocks is **good** if it is clean and W = 0, and **bad** otherwise. For ℓ = 1, …, 4
put θ_ℓ = floor(s′/2^{j_ℓ}) mod 2^{d_ℓ}. As j₁ = 0, j_{ℓ+1} = j_ℓ + d_ℓ and j₄ + d₄ = n, we have
s′ mod 2^{j_ℓ + d_ℓ} = (s′ mod 2^{j_ℓ}) + 2^{j_ℓ}θ_ℓ for each ℓ, and s′ = θ₁ + 2^{j₂}θ₂ + 2^{j₃}θ₃ + 2^{j₄}θ₄. Let E_ℓ be the event
that tier ℓ of guess i* is run and starts with σ_low = s′ mod 2^{j_ℓ} (for ℓ = 1: that guess i* is run).

The **genie run** is the modified process (an analysis device, not an event) in which, in tier ℓ of guess i* on the
event E_ℓ (ℓ = 1, …, 4), the label returned by F_t for every good leaf is replaced by its true label u of Lemma S (F's
tests are still performed and their outcomes ignored); otherwise it follows the rules of RLS. No step of RLS reads ζ,
so in the analysis step 4 of every leaf is replaced by its ζ-average (the same channel): ζ is not a random variable of
either run, and "the past", "all outcomes" and 𝒦_0 never include it. Realise all measurement outcomes of both runs
from one common sequence of independent uniforms, through their conditional laws given the past. The two runs take
the same actions until the first good leaf with û ≠ u. Guess i* processes at most 3M + K₄ ≤ Q leaves, each good leaf
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
stage-m keys of all records of W_{m−1}, the pairing, all stage-m A5 outcomes, the stage-m release
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
pairing are functions of 𝒦_{m−1} and the keys only, and do not depend on any ν_r. Every stage-m
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
tensor product with everything else. For tier 4 (R₄ = 0) these are the leaves themselves, with labels uniform on
[0, 2^{d₄}) given 𝒦_0.

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

**Lemma B₁ (bad leaves).** For guess i*, except with probability < 2e^{−144}: each of the tier-1, tier-2 and tier-3
blocks has at most ȳM bad copies, and the tier-4 block has at most (ε + τ_s + 2^{−8})K₄ < 0.0104K₄ bad copies.
*Proof.* Bad copies are malformed ones or clean ones with W = 1 (wrapped). Tier-1, tier-2 or tier-3 block: by Lemma H
with m_S = M and τ = τ_h, there are fewer than (ε + τ_h)M malformed copies except with probability
e^{−2τ_h²M} = e^{−2^{b−4}}. The coins W of the at most M clean copies are independent with P(W = 1) = ϖ < 2/G = 2^{−14},
so by Lemma A (centred indicators) there are fewer than ϖM + 2^{−14}M < 2^{−13}M wrapped copies except with probability
e^{−2(2^{−14}M)²/M} = e^{−2^{b−6}}. So there are fewer than (ε + 2·2^{−13})M = ȳM bad copies. Tier-4 block: in the same
way, fewer than (ε + τ_s)K₄ malformed copies except with probability e^{−2τ_s²K₄} = e^{−K₄/80000}, and fewer than
ϖK₄ + 2^{−9}K₄ < 2^{−8}K₄ wrapped copies except with probability e^{−2·2^{−18}K₄} = e^{−2(2b+8)}. With b ≥ 32 and
K₄ = 2^{18}(2b + 8) ≥ 2^{18}·72, the exponents are at least 2^{28}, 2^{26}, 235 and 144, and 1/256 + 1/400 + 1/256 < 0.0104. ∎

**Lemma S₁ (the sieve stages).** Let ℓ ∈ {1, 2, 3} and consider tier ℓ of guess i* in the genie run on E_ℓ, given that
its block has at most ȳM bad leaves. Let g̃_m, p̃_m (m = 0, …, 6) and γ_m (m = 1, …, 6) be the numbers of the table below
(in units of M). Except with probability 2R_ℓe^{−2^{b−11}}, G_m ≥ g̃_mM and P_m ≤ p̃_mM for m = 0, …, R_ℓ. In particular
|W_{R_ℓ}| ≥ G_{R_ℓ} ≥ g̃_{R_ℓ}M ≥ K_ℓ, and the bad fraction f^{(ℓ)} = P_{R_ℓ}/|W_{R_ℓ}| of W_{R_ℓ} satisfies f^{(1)} < 0.2736,
f^{(2)} < 0.0678 and f^{(3)} < 0.0168.

| m | γ_m | g̃_m | p̃_m |
| --- | --- | --- | --- |
| 0 | – | 0.99584960 | 0.00415040 |
| 1 | 0.49584936 | 0.24727904 | 0.00208061 |
| 2 | 0.12259897 | 0.06113985 | 0.00104302 |
| 3 | 0.03004817 | 0.01498495 | 0.00052287 |
| 4 | 0.00723080 | 0.00360598 | 0.00026212 |
| 5 | 0.00167169 | 0.00083366 | 0.00013141 |
| 6 | 0.00035088 | 0.00017498 | 0.00006588 |

The entries satisfy, for m = 1, …, 6 (each checked in exact rational arithmetic, with 2^b = M/2^{21}; every margin is at
least 9·10^{−10}, so they can also be checked by hand with 2^{−21} = 0.000000476837158203125):

  g̃_0 ≤ 1 − ȳ, p̃_0 ≥ ȳ;  γ_m ≤ (g̃_{m−1} − p̃_{m−1} − 2^{−21})/2;  g̃_m ≤ (1/2 − δ)γ_m;  p̃_m ≥ (1/2 + δ)p̃_{m−1}.

*Proof.* m = 0: P_0 ≤ ȳM ≤ p̃_0M and G_0 = M − P_0 ≥ (1 − ȳ)M ≥ g̃_0M. Step m−1 → m, on G_{m−1} ≥ g̃_{m−1}M and
P_{m−1} ≤ p̃_{m−1}M: by Lemma K, gg ≥ (G_{m−1} − P_{m−1} − 2^b)/2 ≥ (g̃_{m−1} − p̃_{m−1} − 2^{−21})M/2 ≥ γ_mM. Given 𝒦_{m−1}
and the keys, G_m is a sum of gg fair coins (Lemmas K, C), so by Lemma A, P(G_m < (1/2 − δ)gg) ≤ e^{−2δ²gg}; otherwise
G_m ≥ (1/2 − δ)γ_mM ≥ g̃_mM. P_m ≤ X + bb with X a sum of gb ≤ P_{m−1} fair coins and gb + 2bb ≤ P_{m−1}; by Lemma A,
P(X ≥ gb/2 + δp̃_{m−1}M) ≤ e^{−2δ²p̃_{m−1}²M²/gb} ≤ e^{−2δ²p̃_{m−1}M} (if gb = 0, X = 0); otherwise
P_m ≤ gb/2 + bb + δp̃_{m−1}M ≤ P_{m−1}/2 + δp̃_{m−1}M ≤ (1/2 + δ)p̃_{m−1}M ≤ p̃_mM. Exponents: 2δ² = 2/768² > 2^{−18.17},
γ_mM ≥ γ_6M = 0.00035088·2^{b+21} > 2^{b+9} and p̃_{m−1}M ≥ p̃_5M = 0.00013141·2^{b+21} > 2^{b+8}, so 2δ²gg ≥ 2^{b−10} and
2δ²p̃_{m−1}M ≥ 2^{b−11}. Two events per stage are excluded. Finally, as x/(a + x) increases in x and decreases in a,
f^{(ℓ)} ≤ p̃_{R_ℓ}/(g̃_{R_ℓ} + p̃_{R_ℓ}), which is < 0.2736, 0.0678 and 0.0168 for R_ℓ = 6, 4, 2; and g̃_{R_ℓ}M ≥ g̃₆M =
0.00017498·2^{b+21} > 366·2^b ≥ 2^{18}(2b + 8) ≥ K_ℓ (as d_ℓ ≤ 2b, and 366·2^{b−18} > 2b + 8 for every b ≥ 32: it holds at b = 32 (5996544 > 72), and from b to b + 1 the left
side doubles while the right grows by 2). ∎

**Lemma S₂ (samples).** Let ℓ ∈ {1, 2, 3}. Given W_{R_ℓ}, the sample keys of tier ℓ are distinct except with
probability < 2^{−11}, and then the K_ℓ kept records are a uniformly random K_ℓ-subset of W_{R_ℓ} in uniformly random
order, independent of everything else. Their number of bad records exceeds (f^{(ℓ)} + τ_s)K_ℓ with probability at most
e^{−2τ_s²K_ℓ} < e^{−210}.
*Proof.* As in Lemma Π (|W_{R_ℓ}| ≤ M and κ_W = 2·bitlength(M) + 10). Given 𝒦_{R_ℓ}, over the sample keys, the bad count
is hypergeometric with mean f^{(ℓ)}K_ℓ; apply Lemma H′. 2τ_s²K_ℓ = K_ℓ/80000 = 2^{18}(d_ℓ + 8)/80000 > 3.27(d_ℓ + 8) ≥
3.27·67 > 210 (d_ℓ ≥ 59). ∎

So, outside these events, the K₁ records of tier 1 contain fewer than (0.2736 + 1/400)K₁ = 0.2761K₁ bad records, those of
tiers 2 and 3 fewer than (0.0678 + 1/400)K₂ < 0.071K₂ and (0.0168 + 1/400)K₃ < 0.02K₃, and the K₄ records of tier 4 fewer
than 0.0104K₄ (Lemma B₁); each fraction is below 0.2959.

### 7.7 Records and scores

Fix a search of guess i* in the genie run: the search of tier ℓ on the event E_ℓ, with d = d_ℓ, target θ = θ_ℓ and the
K = K_ℓ records of step 4. Define the record filtration as follows. If R_ℓ ≥ 1 (tiers 1, 2 and 3), let ℋ_0 be generated by
𝒦_{R_ℓ} (Lemma U: it contains the keys, pairings, A5 outcomes and bad labels, but not the labels w of the good records
of W_{R_ℓ}), the sample keys of step 3 and the release outcomes of the records not kept; if R_ℓ = 0 (tier 4), let
ℋ_0 = 𝒦_0. For j ≥ 1 let ℋ_j = ℋ_{j−1} ∨ σ(w_j, m′_j, b_j). Then the record (w_j, m′_j, b_j) is ℋ_j-measurable, and
whether record j is good is ℋ_0-measurable (it is fixed by the malformed set, the coins W, the sieve structure and the
sample). The release of a record not kept is a computational-basis measurement: for a good record it is a fair coin for
every label (φ(x) has diagonal (1/2, 1/2)), and for a bad record it acts only on Ω (invariant (J)).

**Lemma R (record laws).** Let record j be good. Conditioned on ℋ_{j−1}, w_j is uniform on [0, 2^d), m′_j is uniform on
{0,…,7} and independent of w_j, and given (w_j, m′_j), b_j = 0 with probability exactly p_{m′_j}(w_jθ/2^d).
*Proof.* By Lemma U (and its corollary at the end of 7.5) the labels of the good records are independent and uniform given
𝒦_{R_ℓ} (𝒦_0 in tier 4). The sample keys (Lemma S₂) are fresh, the release outcomes of the records not kept are fair
coins or act on Ω (see above), and the (w_i, m′_i, b_i) of earlier records involve other good labels, fresh bits and other
qubits, so conditioning on ℋ_{j−1} leaves w_j uniform; by (J) the qubit of record j is
(|0⟩ + e^{2πi w_jθ/2^d}|1⟩)/√2 in tensor product with everything else, and P2 gives the stated law (A3). ∎

**Lemma B (bounded influence).** For every record and every τ, |Z̃(τ)| ≤ 1 + 2^{−24} = R₀. *Proof.* Lemma T (App. B). ∎

**Lemma D (discretisation).** For every record j and every τ ∈ [0, 2^d), let X̂_j(τ) = (−1)^{b_j}cos(2π(w_jτ/2^d − m′_j/8)).
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
otherwise (a sum of 2^d-th roots of unity). Lemma D gives the second statement. ∎

**Lemma M (any record).** For every record j, every τ and every history in ℋ_{j−1} of positive probability,
−(1/2 + η) ≤ E[Z̃_j(τ) | ℋ_{j−1}] ≤ 1/2 + η.
*Proof.* Every generator of ℋ_{j−1} is obtained before the P2 of record j (steps 1–3 of 6.4 precede step 4, and records
are measured in the order j = 1, …, K). Fix an outcome g of ℋ_{j−1}
together with w_j (fixed before m′_j is drawn). Let σ_g be the reduced state of record
j's qubit given g, written (I + xX + yY + zZ)/2 with x + iy = re^{iα}, 0 ≤ r ≤ 1. m′_j is drawn from fresh qubits, so it
is uniform and independent of g, and P2 with θ′ = 2πm′/8 has outcome 0 exactly when it projects onto
(|0⟩ + e^{iθ′}|1⟩)/√2; so E[(−1)^b | g, m′] = x cos θ′ + y sin θ′ = r cos(θ′ − α). With v = w_jτ/2^d and θ′_{m′} = 2πm′/8,
E[X̂_j(τ) | g] = (1/8)Σ_{m′} r cos(θ′_{m′} − α)cos(2πv − θ′_{m′}) = (r/2)cos(2πv − α) + (r/16)Σ_{m′}cos(2θ′_{m′} − α − 2πv)
= (r/2)cos(2πv − α) ∈ [−1/2, 1/2], because Σ_{m′=0}^{7} e^{2iθ′_{m′}} = Σ_{m′} i^{m′} = 0. Lemma D and the tower property give
the claim. ∎

### 7.8 The marking function isolates the target

**Theorem M.** Fix a search of guess i* as in 7.7 with K records of which at most f_bK are bad, f_b ≤ 0.2959. Then,
except with probability < 2^{−40}, the marking function f of 6.6 satisfies f(θ) = 1 and f(τ) = 0 for every τ ≠ θ.
*Proof.* For τ ∈ [0, 2^d) let m_j(τ) = E[Z̃_j(τ) | ℋ_{j−1}] and D_j(τ) = Z̃_j(τ) − m_j(τ). Then E[D_j(τ) | ℋ_{j−1}] = 0
and D_j(τ) ∈ [a_j, a_j + 2R₀] with a_j = −R₀ − m_j(τ) ℋ_{j−1}-measurable. Lemma A (rescaled by 2R₀) gives
P(Σ_j D_j(θ) ≤ −δ_sK) ≤ e^{−δ_s²K/(2R₀²)} and, for τ ≠ θ, P(Σ_j D_j(τ) ≥ δ_sK) ≤ e^{−δ_s²K/(2R₀²)}. Now
δ_s²K/(2R₀²) > 2^{18}(d + 8)/80001 > 3.27(d + 8), so each probability is < e^{−3.27(d+8)} < 2^{−4.7(d+8)}, and a union
bound over the 2^d candidates gives < 2^{d−4.7(d+8)} < 2^{−40}. On the complement, with n_b ≤ f_bK bad and n_c = K − n_b
good records, Lemmas C* and M give
S(θ) > −δ_sK + n_c(1/2 − η) − n_b(1/2 + η) ≥ K(1/2 − η − f_b − δ_s) > 0.1990K > (7/40)K, and for τ ≠ θ,
S(τ) < δ_sK + n_cη + n_b(1/2 + η) ≤ K(δ_s + η + f_b/2) < 0.1531K < (7/40)K. Since f(τ) = 1 ⇔ S(τ) > θ₀K, the claim
follows. ∎

**Lemma Sr (search).** If f marks exactly one τ, the search of 6.7 returns it except with probability ≤ 2^{−7}, and it
never returns another value. *Proof.* d ≥ 59 ≥ 4. Each repetition is an independent run of the circuit of App. C on
fresh qubits, which applies H^{⊗d} and 𝒢^{k_G}; by Lemmas G and I (App. D) it returns the marked τ with probability
> 1/2, and the classical check f(τ̂) = 1 rejects every other τ̂. Seven repetitions fail with probability < 2^{−7}. ∎

### 7.9 The test

**Lemma T* (test).** Let X_i be the number of malformed copies in the test block of guess i. If X_i ≤ k/5, then
TEST(s) on that block accepts with certainty, and for every v ≠ s, TEST(v) accepts with probability at most e^{−k/200},
whatever happened before.
*Proof.* After subtracting v, a clean copy is the mixture over x of (|0,x⟩ + |1,(x + s − v) mod N⟩)/√2. If v = s the first
qubit is |+⟩ and H gives 0, so Z ≥ k − X_i ≥ 4k/5 ≥ 3k/4. If v ≠ s, the two register values differ, the first qubit is
maximally mixed, and its outcome is a fair coin given everything else (the clean copy is in tensor product with all other
systems). So Z ≤ X_i + Y with Y a sum of k′ ≤ k conditionally fair coins, and Z ≥ 3k/4 forces Y ≥ 11k/20 ≥ k′/2 + k/20;
by Lemma A this has probability ≤ e^{−2(k/20)²/k′} ≤ e^{−k/200}. ∎

By Lemma H with τ = 1/5 − 1/256 = 251/1280, P(X_i > k/5) ≤ e^{−2(251/1280)²k} < e^{−k/14}. With k = 256·bitlength(100G) = 5632,
e^{−k/14} < e^{−402} and e^{−k/200} < e^{−28} < 2^{−40} < 1/(400G).

### 7.10 Theorem 1 (n ≥ 256)

**Theorem 1.** For every N with n ≥ 256, every s and every adversary of Section 5 with ε = 1/256, RLS outputs s with
probability at least 9/10.
*Proof.* Exclude: the tie of 6.1 (< 2^{−11}, Lemma Π); some test block with X_i > k/5 (≤ G e^{−402} < 2^{−560}); some
TEST(v), v ≠ s, accepting (≤ G e^{−28} < 2^{−25}); the genie run differing from the real run (< 1/100, 7.4); for guess
i*, the events of Lemma B₁ (< 2e^{−144}), of Lemma S₁ in tiers 1, 2 and 3 (< 24e^{−2^{21}}) and of Lemma S₂ in tiers 1, 2
and 3 (< 3·2^{−11} + 3e^{−210}); the failure of Theorem M in the search of tier ℓ of guess i* on E_ℓ, ℓ = 1, …, 4
(< 4·2^{−40}); and the failure of Lemma Sr in these four searches (< 4·2^{−7}). The total is
< 0.0005 + 2^{−25} + 0.01 + 0.0015 + 0.0313 + 10^{−9} < 0.044.
Outside these events, suppose no earlier guess has output s (otherwise RLS has output s). No earlier guess output
anything else (no wrong candidate is accepted), so guess i* is run and E₁ holds. If E_ℓ holds (ℓ ∈ {1, …, 4}), the tier
does not fail in step 3 (for ℓ ≤ 3 by Lemmas S₁, S₂: |W_{R_ℓ}| ≥ K_ℓ and no tie; for ℓ = 4 step 3 keeps all K₄
leaves and cannot fail), and its K_ℓ records contain fewer than 0.2959K_ℓ bad
records (the summary after Lemma S₂), so f marks exactly θ_ℓ (Theorem M) and the search returns θ̂_ℓ = θ_ℓ (Lemma Sr).
Then σ_low becomes (s′ mod 2^{j_ℓ}) + 2^{j_ℓ}θ_ℓ = s′ mod 2^{j_ℓ + d_ℓ} (7.4), so E_{ℓ+1} holds for ℓ ≤ 3, and after tier 4
the candidate is s̃ = s′ mod 2^n = s′ < N, with (s̃ + g*) mod N = s. TEST(s) accepts on the test block of guess i*
(Lemma T*). So RLS outputs s with probability > 0.95 ≥ 9/10. ∎

### 7.11 Small inputs (n < 256)

**Theorem 2.** For every N with n < 256, every s and every adversary with ε = 1/256, the branch of 6.10 outputs s with
probability > 0.99.
*Proof.* Lemmas N and Π hold verbatim for this branch (P(tie) < 2^{−11}). Let X_v be the number of malformed copies among
the K_s copies of candidate v. Lemma H with τ = 1/5 − 1/256 = 251/1280 gives P(X_v > K_s/5) ≤ e^{−2(251/1280)²K_s}
< e^{−80000}. If X_s ≤ K_s/5, then Z_s ≥ 4K_s/5 ≥ 3K_s/4 (as in Lemma T*). For v ≠ s with X_v ≤ K_s/5, Z_v ≥ 3K_s/4 has
probability ≤ e^{−K_s/200} < e^{−5200}. A union bound over the N ≤ 2^{255} candidates gives total failure
< 2^{−11} + 2^{256}(e^{−80000} + e^{−5200}) < 0.01. ∎

Theorems 1 and 2 cover every N ≥ 2 and every s, for every adversary of Section 5 with ε(n) = 1/256, and in particular
for the clean problem.

## 8. Resources (every branch)

For n < 256 every quantity is an absolute constant: at most Q_s ≤ 2^{255}·2^{20} copies, O(Q_s n + Q_s log₂ Q_s·κ′) bit
operations and gates before the address charge (itself O(log Q_s)), (n+1)Q_s + O(n) qubits held and O(Q_s κ′) bits.
These constants are astronomically large but independent of N, s and all outcomes. Let n ≥ 256.

**Sizes.** b ≤ n/8 + 1, so M = 2^{b+21} ≤ 2^{22}·2^{n/8}; K₁, …, K₄ ≤ 2^{18}(n + 8); G = 2^{15}; k = 5632. Hence

  **Q = G(3M + K₄ + k) < 2^{15}(3·2^{22}·2^{n/8} + 2^{18}(n + 8) + 5632) < 2^{39}·2^{n/8},**

counting every acquired copy (all are acquired in 6.1, on every branch; 2^{n/8} ≥ 2^{32} dominates the other terms).
Also log₂ Q < n/8 + 39, so κ, κ_W < n/4 + 90 < n and L₁ ≤ log₂ Q + log₂(1600(n+1)) + 1 < n, i.e. κ, κ_W, L₁, r₁ = O(n).

**Quantum space.** All Q copies are held from 6.1 until they are used: (n+1)Q qubits. In addition, at any time: one
copy's O(n) LEAF/F_t ancillas, one test control, one A4 qubit and one TEST ancilla set; in a search, the d search qubits,
U (w qubits), V (p) with O(p) ancillas, k (q), v (27) with O(q) ancillas, the O(w) ancillas of P3b, the flag with O(w)
carry ancillas, the diffusion target and its d − 2 ancillas: O(n) qubits, one fixed pool reused for every record, call and
repetition. Measured qubits are released. **S_Q ≤ (n+1)Q + O(n) = O(2^{n/8} n).**

**Classical space.** Sort keys and workspace and the rank table: O(Q(κ + bitlength(Q))) = O(Qn) bits. The current tier
of the current guess: at most M labels of n bits and M copy indices, the 2^b key counters, the sample keys of κ_W bits
with merge-sort workspace: O(Mn) bits. The stored search records: K(d + 4) = O(n²) bits. The table: 27·2^{24} bits (an
absolute constant). F_t counters, parameters, σ_low, the Grover controller (K_G, k_G, counters) and one gate
description: O(n²) bits. **S_C = O(Qn) = O(2^{n/8} n).** Hence 𝔐 = O(2^{n/8}n), log₂(𝔐 + 2) < n/8 + 2 log₂ n + O(1),
and **A = O(n)**.

**Work** (every operation charged O(A) = O(n)).
* Acquisition: Q(n+1). Keys and merge sort of 6.1: O(Q log₂ Q·κ) = O(Qn²) bit operations, O(Qn³) charged.
* Leaves (at most G(3M + K₄) ≤ Q of them): LEAF uses O(n) gates; F_t uses 8(J+1)r₁ ≤ 8n·r₁ kickback tests of O(n) gates;
  Lemma P and the rounding O(n²). A leaf costs O(n²r₁) = O(n³) operations, O(n⁴) charged; in total O(Qn⁴).
* Sieve stages and samples, per guess: R₁ + R₂ + R₃ = 12 stages, each on at most M records, with O(Mn) bit operations for
  keys, counting sort and subtractions, one A5 per pair and O(2^b log M) for the counters; three samples with
  O(M log₂ M·κ_W) for the keys and their sort: O(Mn²), O(Mn³) charged; over G guesses O(Qn³).
* Table (App. B): an absolute constant number of operations. Records: O(K) operations per search.
* Searches, per guess: four searches, each with at most 7 repetitions of at most k_G ≤ 0.785·2^{d/2} ≤ 2^b ≤ 2·2^{n/8}
  Grover iterations (d₁ ≤ 2b and d_ℓ = 2b for ℓ ≥ 2). One call of 𝒪 costs, per record, d applications of P3a on p qubits
  (O(dp)), O(p + q), one table read (O(2^q(q + 27)), an absolute constant) and one P3b (O(w)), done and undone, so
  O(K(dp + w)) = O(n² log n) gates; 𝒟 costs O(d). A repetition also evaluates f(τ̂) classically in O(Kdp) = O(n² log n).
  So each search costs O(2^{n/8} n² log n) operations, O(2^{n/8} n³ log n) charged; over G guesses the same order.
* TEST: G·k copies, O(n) gates each. Grid points and parameters: O(Gn²). Releasing unused blocks, or all copies on a
  tie: at most Q(n+1) measurements and resets.

The leaf term dominates: **T = O(Qn⁴ + 2^{n/8}n³ log n) = O(2^{n/8} n⁴).**

All four bounds hold simultaneously on every execution branch of this one algorithm with this one parameter rule
(every loop length is bounded by a fixed function of N; the copy count is exactly Q), jointly with Theorems 1 and 2,
for every adversary of Section 5.

## 9. Exact growth indices and structured envelopes

For ℬ(n) = 2^{n/8} n^r with fixed r ≥ 0: log₂ ℬ = n/8 + r log₂ n, so log₂ log₂ ℬ = log₂ n − log₂ 8 + log₂(1 + 8r log₂ n/n),
and log₂ log₂ ℬ/log₂ n → 1. Hence g(ℬ) = 1 (the max{4,·} is irrelevant for large n); outer constants do not change it.

* T: ℬ_T = 2^{n/8} n⁴, index **1**: exponent [{coefficient 1/8, nPower 1, logPower 0}], nPower 4, logPower 0.
* S_C: ℬ = 2^{n/8} n, index **1**: exponent [{1/8, 1, 0}], nPower 1, logPower 0.
* S_Q: ℬ = 2^{n/8} n, index **1**: exponent [{1/8, 1, 0}], nPower 1, logPower 0.
* Q: ℬ = 2^{n/8}, index **1**: exponent [{1/8, 1, 0}], nPower 0, logPower 0.

Published time score: [1]. Under the asymptotic comparator the time envelope is strictly below 2^{n/6}·poly(n).

## 10. Fractional error tolerance

ε(n) = 1/256 under the model of Section 5: with Q acquired copies, at most floor(Q/256) of them are malformed; their
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
* Our own components, re-proved here: the splice, F_t and A1–A4 (SLS, 59facd77); A5 and Lemma P (OMX-ML, 31c2d043); the
  full-upfront acquisition, the permutation and Lemmas N, Π, U, C, K and the genie run (RLS, 280a17e4); the shadow score,
  the cosine table, the oracle circuits and Lemmas B, D, C, M (ROB-G2, 55a6ce76; adapted to labels in Z/2^dZ); the
  sieve-then-search template of our RLS-G1 (4ef5cf09; one stage, tolerance 1/7 at work 2^{n/3}·poly), RLS-G2 (6b206bcf; two stages, 1/16 at
  2^{n/4}·poly) and RLS-G4 (9e0af9a8; three tiers, 1/64 at 2^{n/6}·poly) entries on this track, which this entry extends to
  four tiers. The model is that of our ROB line
  (d0c6b9b9, 5d77f276, a5c17989, 55a6ce76).
* Our RLS-3 (06a9acf5): a three-stage robust low-bit sieve with tolerance 1/32 at work 2^{n/3}·poly, same model. mpjunior92's
  PSG12 (cac3285d): a clean three-level bounded Grover sieve that already reaches work O(n⁴L^{3/2}2^{n/6}) without
  corruption; zereraz's PSR-W3 (a08e8f51). Credited; nothing is used.
* Positive-tolerance prior work in this model or others (credited, nothing used): dadon's f892f7ea and 493303b5 (1/3, same
  model);
  mpjunior92's PSG13 4c42d100 (same model, tolerance 1/(2^{39}n⁴), time 2^{n/6}·poly with polynomial memory) and
  PSG14C 30304a9e (inverse-cubic tolerance); dadon's 7341d79b (1/(896n) at 2^{n/3}·poly); zereraz's
  b45deb1b (1/(2·10^{10}n⁴));
  kaankolcu's RWT25 3f48c893 (1/4, fixed-position model); GordoAR's c730b22b (1/3, own model); ercumentyildirim's
  LSIEVE f2cb3153/0f4adc93 (oblivious model, inverse-polynomial tolerance at 2^{n/log n}·poly); smoke-era RGRST1
  be98e61b, CGRST1 53b4755b, CADGR1 5f048e8b/b838e1ae, CADGR2 45044787, RLQGR1–3 ee378bae, 635a47e2, 0e1559e4, 09c05313,
  7b2afdfc. Regev (SIAM J. Comput. 33 (2004), Definition 2.1) studies DCP with a failure parameter.

Context (not part of any claim). New here: four tiers of sieve-then-search with six, four, two and zero sieve stages,
so that each search runs over at most 2^{2b} ≈ 2^{n/4} candidates and costs 2^{n/8}·poly(n); six stages, followed exactly
(Lemma S₁), leave a bad-record fraction below 0.274 from 1/256 malformed copies, below the bound 0.2959 of Theorem M. The
family RLS-G1/G2/G4/G6 gives tolerance 2^{−(R+2)} at work 2^{n/(R+2)}·poly(n) for R = 1, 2, 4, 6 (with 1/7 for R = 1).
To our knowledge (the public board as of 2026-11-07) no other entry proves a constant tolerance in this model with work
2^{cn}, c < 1/6. No cited result is used as a lemma except Hoeffding's inequality for sampling without replacement
(Lemmas H, H′), cited with its exact theorem number; Lemma A is proved in the file.
