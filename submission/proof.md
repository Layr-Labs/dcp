# RLS-G1M: a one-stage robust low-bit sieve with threshold-ladder robust quantum search, O(2^{n/3} n⁴) work, adaptive malformed-copy tolerance 19/100

This file and `appendix.md` together are the complete proof of all five claims in `submission.json`. They
describe one algorithm, **RLS-G1M** (below simply RLS), with one fixed parameter rule, and prove for every
integer N ≥ 2, every s ∈ Z/NZ, with n = ceil(log₂ N), and every adversary of the error model of Section 5
(which contains the clean problem as the adversary that corrupts nothing):

* the output equals s with unconditional probability at least 9/10 (> 2/3);
* total work T = O(2^{n/3} n⁴);
* peak classical space S_C = O(2^{n/3} n) bits;
* peak quantum space S_Q = O(2^{n/3} n) qubits;
* acquired source copies Q = O(2^{n/3}); Q is a fixed function of N, the same on every branch;
* fractional error tolerance ε(n) = 19/100: at most floor(19Q/100) acquired copies may be malformed, at
  adversarially and adaptively chosen positions, with arbitrary, possibly entangled contents.

All constants are absolute (independent of N, s, the adversary and all outcomes). Every loop of RLS has a
length bounded by a fixed function of N, so the four resource bounds hold on every execution branch
whatever the copies contain. Logarithms are base 2 unless written ln. All four growth indices equal 1; the
time envelope has exponent n/3.

**Idea.** RLS-G1M is our RLS-G1 (4ef5cf09, tolerance 1/7) with a sharper analysis of the malformed records and a
search that can use it. (i) As in our RLS (280a17e4), all Q copies are acquired before the first measurement, so the
adversary, which sees only outcomes obtained before each delivery, chooses blind, and a uniform permutation spreads
its copies over all slot blocks. (ii) The SLS splice (59facd77) turns the copies of the right grid guess g* into exact
coset states of Z/2^nZ with secret s′ = (s − g*) mod N; wrapped copies are treated as malformed. (iii) *Phase 1.* One
sieve stage pairs records whose labels agree on the low b = ceil(n/3) bits and keeps the differences. The outputs are
qubits of labels 2^b·w with w ∈ Z/2^{d₁}, d₁ = n − b, whose phase depends only on σ = s′ mod 2^{d₁}. A sample of K₁ =
O(n) outputs feeds ROB-G2's shadow score (55a6ce76) over the 2^{d₁} candidates for σ, and quantum search finds σ with
O(2^{d₁/2}) = O(2^{n/3}) oracle calls per threshold. (iv) *Phase 2.* The high b bits of s′ are found the same way from
fresh copies, spliced to Z/2^bZ with the known σ removed; this takes 2^{n/6}·poly. (v) *New here.* The output of a
pair with one good and one bad member (a *mixed* record) has a label whose high part is exactly uniform and
independent of the bad side, and its qubit is a state that does not depend on that label, rotated by the label's phase
(Lemma U, phase covariance). So a mixed record's exact-cosine score X̂ has conditional mean exactly 0 at every wrong
candidate, so its table score has mean within η of 0 (Lemma X): it can lower the target's score but raise no other by
more than η. Only *bad-only* records (all leaves bad) can raise a wrong candidate. With n_x mixed and n_o bad-only
records among K, the target's score exceeds every other one by K(1/2 − 2η − 2δ_s) − n_x − (3/2)n_o (Theorem M). This
gap does not fix the level of the target's score, so the search walks down a ladder of thresholds ℓ/256, ℓ = 257, …,
1, and returns at the first threshold where it finds a marked candidate (Lemma Sr). Counting the three record types
through the stage (Lemmas K, S₁) gives tolerance 19/100. The old analysis ("fewer than about 1/3 of the records are
bad", with one stage doubling the bad fraction) allowed 1/7.

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
comparisons with constants, multi-controlled X and table reads), the cosine table (Lemma T), the oracles 𝒪_ℓ and
the diffusion 𝒟 are given in App. A–C of `appendix.md`, which is part of this proof.

**Cost convention.** Let 𝔐 be the number of allocated bits plus qubits. Section 8 shows
𝔐 = O(2^{n/3} n), so a classically indexed access or classically addressed gate costs
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

* **b** = ceil(n/3) (sieve bits and phase-2 width), so n/3 ≤ b ≤ n/3 + 1 and b ≥ 86; **d₁** = n − b ≤ 2n/3
  (phase-1 width) and **d₂** = b; both are ≥ 86.
* **M** = 2^{b+9} (phase-1 leaves per guess).
* **K₁** = 2^{20}(d₁ + 8), **K₂** = 2^{20}(d₂ + 8) (records of the two searches).
* **G** = 2^{12} (grid size); grid points g_i = floor(iN/G) for i = 0, …, G−1. Since N ≥ 2^{255} > G, the
  g_i are distinct.
* **k** = 256·bitlength(100G) = 4864 (copies per test).
* **Q** = G(M + K₂ + k) (copies acquired).
* L₁ = bitlength(1600(n+1)Q); **r₁** = 200L₁ (tests per level and phase in F_t).
* **κ** = 2·bitlength(Q) + 10 (sort-key bits); **κ_W** = 2·bitlength(M) + 10 (sample-key bits).
* Score: **q** = 24 (angle bits); **p** = q + 1 + bitlength(n) (phase bits); for a search with K records, **w** =
  bitlength(K) + 29 (accumulator width); **threshold ladder ϑ_ℓ = ℓ/256** for ℓ = 257, 256, …, 1 (ℓ = 257 never marks;
  it only fixes ϑ_{ℓ*+1} in Lemma Sr).
* Search over d qubits: K_G = floor(2^{d/2}) (the integer square root of 2^d), k_G = floor(785K_G/1000), at most 6
  repetitions per threshold.

Analysis constants (not used by the algorithm): ε = 19/100, δ = 1/1024, τ_h = 2^{−10}, y = ε + 2^{−9} = 2457/12800,
δ_s = 1/400, τ_s = 1/800, τ_T = 2^{−24} (table accuracy), η = 3π2^{−24} + τ_T < 6.22·10^{−7}, R₀ = 1 + τ_T, φ̄ = 0.489.

For **n < 256**: K_s = 2^{20}; Q_s = N·K_s; κ′ = 2·bitlength(Q_s) + 10 (Section 6.10).

## 5. Error model (adaptive malformed copies)

Copies are delivered one at a time in acquisition order j = 1, …, Q (Q is given by Sections 4 and 6.1).
An **adversary** knows N, s, the full description of RLS, and every measurement
outcome obtained by RLS before copy j is delivered; it holds an arbitrary private quantum system E which
it may measure and process. Before copy j is delivered it chooses c_j ∈ {clean, malformed}, as a function
of that information and its own outcomes; on every branch at most floor(εQ) copies are malformed,
ε = 19/100.

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
2. Draw Q keys K_1, …, K_Q of κ fair bits each (A4). If two keys are equal, measure everything and
   output 0. Otherwise sort the copies by key (merge sort on (key, index) pairs) and let π(p) be the
   index of the copy of rank p (p = 1, …, Q). The table p ↦ π(p) is stored.

### 6.2 Slot layout

Ranks are grouped into G consecutive blocks of M + K₂ + k ranks, block i belonging to guess g_i. Inside block
i, the first M ranks form the **phase-1 block**, the next K₂ the **phase-2 block**, and the last k the **test
block**.

### 6.3 LEAF_t (one held copy, guess g, low-bit count j, t = n − j, current σ_low)

1. Controlled on the first qubit c, apply P1 with a = (N − g) mod N (subtract g mod N).
2. Controlled on c, add (2^n − σ_low) mod 2^n to the register (A2, mod 2^n).
3. Measure the low j register qubits and release them. Call the remaining t qubits the register.
4. Draw t fair bits (A4) forming ζ ∈ [0, 2^t); add ζ mod 2^t to the register (A2, uncontrolled); then
   erase ζ (no later step reads it, or the outcomes of step 3).
5. Run F_t on the register, giving û ∈ [0, 2^t); measure and release the register.

Return the record (qubit c, label x = û).

### 6.4 Phase 1 (guess g, the M copies of its phase-1 block)

1. *Leaves.* Apply LEAF_n (j = 0, σ_low = 0, t = n) to each copy, giving records (qubit, label x ∈ Z/2^nZ) in rank
   order: the list W_0.
2. *One sieve stage.* The key of x is x mod 2^b. Sort W_0 stably by key (counting sort with 2^b counters). Within each
   key group, in list order, form pairs (1st, 2nd), (3rd, 4th), …, and release a last unpaired record. For each pair
   (a, b), in list order of a, apply A5 with a as control; on outcome 1 output the record (qubit a, label
   (x_a − x_b) mod 2^n), on outcome 0 release both qubits. W_1 = the outputs. Every label of W_1 is ≡ 0 mod 2^b; for
   a record of W_1 write w = label/2^b ∈ [0, 2^{d₁}).
3. *Sample.* If |W_1| < K₁, release all records of W_1 and declare the guess failed. Otherwise draw a key of κ_W fair bits
   for every record of W_1; on a tie, release all records of W_1 and declare the guess failed; otherwise keep the K₁ records
   with the smallest keys, in key order (a uniformly random K₁-subset in uniformly random order), and release the rest.
4. *Records.* For the j-th kept record (j = 1, …, K₁): draw 3 fair bits forming m′_j; apply P2 (= A3) with m′_j to
   its qubit, giving b_j; store (w_j, m′_j, b_j).
5. *Search* (Section 6.7) with d = d₁ and these K₁ records, giving σ̂ ∈ [0, 2^{d₁}) or "fail" (then the guess
   failed).

### 6.5 Phase 2 (guess g, the K₂ copies of its phase-2 block, given σ̂)

1. For each copy apply LEAF_{d₂} with j = d₁ and σ_low = σ̂ (t = d₂: the low d₁ register qubits are measured), giving
   a record (qubit, label u ∈ [0, 2^{d₂})); draw m′, apply P2, giving b; store (u, m′, b).
2. *Search* with d = d₂ and these K₂ records, giving ĥ ∈ [0, 2^{d₂}) or "fail". The candidate is
   s′ = σ̂ + 2^{d₁}ĥ ∈ [0, 2^n).

### 6.6 The score of a search

Given d and K records (w_j, m′_j, b_j) with w_j ∈ [0, 2^d): for i = 0, …, d−1 let c_{j,i} = floor(2^p frac(2^i w_j/2^d))
(the controller reads the p bits of w_j at positions d−i−p, …, d−i−1, the missing low positions zero-filled:
c_{j,i} = floor(w_j 2^{p+i−d}) mod 2^p, O(p) indexed bit reads). For τ ∈ [0, 2^d)
with bits τ = Σ_i τ_i 2^i define

  V_j(τ) = (Σ_{i<d} τ_i c_{j,i}) mod 2^p,  h_j(τ) = floor(V_j(τ)/2^{p−q}),  k_j(τ) = (h_j(τ) − 2^{q−3}m′_j) mod 2^q,
  Σ(τ) = Σ_{j=1}^{K} (−1)^{b_j} c_{k_j(τ)} ∈ Z,  S(τ) = Σ(τ)/2^{25} = Σ_j Z̃_j(τ),  Z̃_j(τ) = (−1)^{b_j} table[k_j(τ)],

with the table c_k of App. B (table[k] = c_k/2^{25}), and for ℓ = 1, …, 257 the marking function f_ℓ(τ) = 1 iff
256·Σ(τ) > ℓ·2^{25}·K (i.e. S(τ) > ϑ_ℓK). Each f_ℓ is evaluated classically for one τ in O(K d p) bit operations.

### 6.7 Search

For ℓ = 257, 256, …, 1, in this order, do the following at most 6 times: prepare d fresh qubits in |0^d⟩, apply H to
each, apply 𝒢_ℓ = 𝒟·𝒪_ℓ (App. C, for this score and f_ℓ) exactly k_G times, and measure, giving τ̂; evaluate f_ℓ(τ̂)
classically; if f_ℓ(τ̂) = 1 return τ̂. If no run returns, return "fail". A search makes at most 257·6 = 1542 runs (ℓ =
257 never marks; it only fixes ϑ_{ℓ*+1} in Lemma Sr).

### 6.8 TEST(v) (the k copies of the test block of guess i)

For each copy: controlled on its first qubit, apply P1 with a = (N − v) mod N (subtracting v from the register);
apply H to the first qubit and measure it; release the copy. Let Z be the number of outcomes 0. Accept iff 4Z ≥ 3k.

### 6.9 Output (n ≥ 256)

For i = 0, …, G−1: run phase 1 and, unless it failed, phase 2 for guess g_i; if both succeed and the candidate s′
satisfies s′ < N, run TEST((s′ + g_i) mod N) on the test block of guess i, and if it accepts, output (s′ + g_i) mod N
and halt. If no candidate is accepted, output 0. (Copies of unused blocks are measured and released at the end;
they were acquired in step 6.1.)

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

**Notation in Section 7.** G_m, X_m, B_m and P_m count good, mixed, bad-only and bad records (7.5), unrelated to the grid
size G, the grid points g_i, the wrap probability p and the test counts X_i, X_v of 7.9 and 7.11; s is the secret,
s′ = (s − g*) mod N.

### 7.3 The splice and exact leaves

**Lemma W (splice).** Fix g and let s′ = (s − g) mod N. After LEAF step 1 a clean copy is the uniform
mixture over x ∈ [0,N) of (|0,x⟩ + |1,(x + s′) mod N⟩)/√2. Hence it equals (1 − p)ρ^{nw} + pρ^{w}
with p = s′/N, where ρ^{nw} (resp. ρ^{w}) is the uniform mixture of these pure states over
x < N − s′ (resp. x ≥ N − s′; if s′ = 0 then p = 0 and only ρ^{nw} occurs). For x < N − s′ the second branch
holds the integer x + s′ < N. Some grid
point g* = g_{i*} has s′ < N/G + 1, hence p < 1/G + 1/N < 2/G.

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

Fix the guess g* = g_{i*} of Lemma W and put s′ = (s − g*) mod N, p = s′/N < 2/G. By Lemma W we may (by
linearity) realise every clean copy of the blocks of guess i* as ρ^{nw} or ρ^{w} by an independent coin W with
P(W = 1) = p. A copy of these blocks is **good** if it is clean and W = 0, and **bad** otherwise. Put
σ = s′ mod 2^{d₁} and h* = floor(s′/2^{d₁}), so s′ = σ + 2^{d₁}h*.

The **genie run** is the modified process (an analysis device, not an event) in which, in phase 1 of guess i*, and
in phase 2 of guess i* when σ̂ = σ, the label returned by F_t for every good leaf is replaced by its true label u of
Lemma S (F's tests are still performed and their outcomes ignored); otherwise it follows the rules of RLS. No step of
RLS reads ζ, so in the analysis step 4 of every leaf is replaced by its ζ-average (the same channel): ζ is not a
random variable of either run, and "the past", "all outcomes" and 𝒦_0 never include it. Realise all measurement
outcomes of both runs from one common sequence of independent uniforms, through their conditional laws given the
past. The two runs take the same actions until the first good leaf with û ≠ u. Guess i* processes at most
M + K₂ ≤ Q leaves, each good leaf whose label is replaced with P(û ≠ u | past) < 1/(100Q), so the runs differ with
probability < 1/100.

### 7.5 Structure of the phases in the genie run

Consider phase 1 of guess i* (t = n, one stage with l_0 = 0, l_1 = b and stage width b_1 = b; in the notation below
R_t = 1, and W_1 is the output of the stage), and phase 2 of guess i* on the event σ̂ = σ (t = d₂, no stage, l_0 = 0,
R_t = 0), in the genie run. In 7.5–7.7, "the past" and every conditioning exclude, in addition, the F_t outcomes of the
phase's good leaves (the genie run never reads them, so by linearity we may average over them); step-3 outcomes may be
included or not (Lemma S holds conditionally on them, with σ_low = 0 in phase 1 and σ_low = σ = s′ mod 2^{d₁} in phase 2).
A record is **good** if every leaf of its combination tree is a good leaf, **bad-only** if every leaf of its tree is bad,
and **mixed** otherwise; it is **bad** if it is not good, and **free** if it is not bad-only (its tree has a good leaf).
G_m, X_m and B_m are the numbers of good, mixed and bad-only records of W_m, and P_m = X_m + B_m. A leaf is good or
bad-only, and the output of a pair is good iff both members are good, bad-only iff both are bad-only, and mixed otherwise.

*Phase rotations.* For real α let D(α) = |0⟩⟨0| + e^{iα}|1⟩⟨1| (one qubit), and for a label x let α_x = 2πxσ_hi/2^t, so
φ_{σ_hi}(x) = D(α_x)|+⟩ with |+⟩ = (|0⟩ + |1⟩)/√2; α_x mod 2π depends only on x mod 2^t, and α_{x−x′} ≡ α_x − α_{x′}.
Two identities hold on every basis state: (I1) for a computational-basis outcome c, ⟨c|D(α) = e^{iαc}⟨c|; (I2) for A5 on
a pair (a, a′) (written (a, b) in 6.4 and Lemma C) with outcome o, ⟨o|_{a′}·CNOT_{a→a′}·(D(α) ⊗ D(α′)) = e^{iα′o}·D(α +
(−1)^oα′)·⟨o|_{a′}·CNOT_{a→a′}, the D on the right acting on a (both sides map |c, e⟩ to e^{i(αc + α′e)}|c⟩ if e = o ⊕ c
= o + (−1)^o c, and to 0 otherwise). So the phase factor of a measured qubit changes neither outcome probabilities nor
the post-measurement state of the other systems, and on outcome 1 A5 turns the factors of its inputs into the factor
D(α_{x_a − x_{a′}}) of its output, up to a global phase.

**Lemma C (fair coins).** Let a pair contain at least one good record. Conditioned on the past (in the sense
above) and on the labels of all free records, the outcome of its A5 measurement is 0 or 1 with probability
exactly 1/2; in particular it is independent of the good members' labels. If both records are good, then on
outcome 1 the output qubit is φ_{σ_hi}(x_a − x_b), in tensor product with everything else.

*Proof.* By invariant (J) of Lemma U at the preceding stage (Lemma U at stage m uses Lemma C only for the pairs of
stage m, so there is no circularity), a good record's qubit is φ_{σ_hi}(x) for its label x, in tensor product with all
other systems given the past and the free labels. Its computational-basis diagonal is (1/2, 1/2). Let ρ be the joint state
of the pair (and the rest) before the CNOT, and let o be the measured value. If b is good, P(o) = Σ_c ⟨c|ρ_a|c⟩·
⟨o⊕c|ρ_b|o⊕c⟩ = Σ_c ⟨c|ρ_a|c⟩/2 = 1/2; if a is good, P(o) = Σ_c (1/2)⟨o⊕c|ρ_b|o⊕c⟩ = 1/2. Because the
good qubit is in tensor product with everything else, the same computation holds conditioned on any
event of the other systems. For two good qubits A5 gives the stated outputs with probability 1/2 each,
whatever x_a, x_b are. ∎

Let 𝒦_0 be the σ-algebra generated by: h; the rank map; everything before the phase (all outcomes of
earlier guesses and phases); the coins W; the identity of the good leaves; and every outcome and label
of the bad leaves of the phase. It does not contain the step-3 outcomes, ζ or F's outcomes of good
leaves, which no later step reads in the genie run. For m ≥ 1, let 𝒦_m be generated by 𝒦_{m−1}, the
stage-m keys of all records of W_{m−1}, the pairing, all stage-m A5 outcomes, the stage-m release
outcomes, and the labels of the bad-only records of W_m (not those of the mixed ones). The type (good, mixed or bad-only)
of every record of W_m is 𝒦_m-measurable.

**Lemma U (exact uniformity and phase covariance).** For m = 0, …, R_t: (U) conditioned on 𝒦_m, the values
floor(x_r/2^{l_m}) for the free records r of W_m are independent and uniform on [0, 2^{t−l_m}); and (J) conditioned on
𝒦_m and on the labels of the free records of W_m, the joint state of all systems is V(⊗_{r good in W_m}|+⟩⟨+|_r ⊗ Ω_m)V†
with V = ⊗_{r free in W_m} D_r(α_{x_r}), where Ω_m (the mixed and bad-only records of W_m, all held copies, released
systems other than the step-3 qubits and F_t test qubits of the phase's good leaves, which are averaged out, and E) does
not depend on the labels of the free records of W_m. In particular each good record's qubit is φ_{σ_hi}(x_r), in tensor
product with everything else.

*Proof.* m = 0: by Lemma S and (2.1) the true labels of the good leaves are independent uniform on Z/2^tZ, independent
of everything in 𝒦_0 (good copies are in tensor product with all other systems and the genie run ignores F's outcomes on
them; the coins W are independent of the labels); given the labels, each good leaf's first qubit is φ_{σ_hi}(u) =
D(α_u)|+⟩ in tensor product with everything else, and the free leaves are the good ones. Step m−1 → m: for every record
r of W_{m−1} write floor(x_r/2^{l_{m−1}}) = κ_r + 2^{b_m}ν_r with κ_r ∈ [0, 2^{b_m}) its stage-m key and ν_r ∈ [0,
2^{t−l_m}). For free records all κ_r, ν_r are independent and uniform given 𝒦_{m−1} (hypothesis); for bad-only records
they are 𝒦_{m−1}-measurable. So the grouping and the pairing are functions of 𝒦_{m−1} and the keys only, and do not
depend on any ν_r. Fix 𝒦_{m−1}, the keys and the labels of the free records of W_{m−1}. Replacing Ω_{m−1} by its
conjugate under D_r(−α_{x_r}) on every bad-only record r (a 𝒦_{m−1}-measurable unitary), the state of (J) at m−1 becomes
VΞV† with V = ⊗_{r ∈ W_{m−1}} D_r(α_{x_r}) over all records and Ξ = ⊗_{r good}|+⟩⟨+|_r ⊗ Ω̃ independent of the free
labels. The stage applies, in an order fixed by the pairing, A5 to each pair and computational-basis measurements to the
unpaired records and to the controls of pairs with outcome 0. By (I1) and (I2), and since a factor on one qubit commutes
with an instrument on other qubits, these instruments with outcomes ω map VΞV† to V′Ξ_ωV′† up to a global phase, where
Ξ_ω is the result of the same instruments and outcomes on Ξ and V′ = ⊗_r D_r(α_{x_r}) over the outputs r (labels x_a −
x_{a′}). Hence, given 𝒦_{m−1} and the keys, the probability Tr Ξ_ω of every outcome sequence does not depend on the ν_r
of the free records (for a pair with a good member it is a fair coin, Lemma C), and conditioning on the outcomes leaves
these ν_r independent and uniform. Undo the conjugation on the bad-only outputs (their labels are 𝒦_m-measurable). A
good–good pair with outcome 1 leaves ⟨1|_{a′}CNOT(|+⟩|+⟩) = |+⟩/√2 on its output, in tensor product; every other output
and every released system goes into Ω_m, which is built from Ξ_ω and so depends on the keys and outcomes (both in 𝒦_m)
but on no ν_r of a free record. This is (J) at m. For (U) at m: the two members of a pair have κ_a = κ_{a′} and labels ≡
0 mod 2^{l_{m−1}}, so x_a − x_{a′} ≡ 2^{l_m}(ν_a − ν_{a′}) (mod 2^t) and the output's value floor(x′/2^{l_m}) is (ν_a −
ν_{a′}) mod 2^{t−l_m}. For a free output some member is free, so over disjoint pairs these values are independent and
uniform, also given the outcomes. ∎

In particular, for phase 1 (one stage, l_1 = b), the values w_r = x_r/2^b of the free records of W_1 are independent and
uniform on [0, 2^{d₁}) given 𝒦_1; as α_{2^bw} ≡ 2πwσ/2^{d₁} (σ = s′ mod 2^{d₁}), by (J) a good record's qubit is
(|0⟩ + e^{2πi w_r σ/2^{d₁}}|1⟩)/√2 in tensor product with everything else, and each mixed record carries the factor
D(2πw_rσ/2^{d₁}) on a state Ω_1 that does not depend on any w_r. For phase 2 (no stage, t = d₂), the labels u_r of the good
leaves are independent and uniform on [0, 2^{d₂}) given 𝒦_0, with qubits (|0⟩ + e^{2πi u_r h*/2^{d₂}}|1⟩)/√2,
h* = floor(s′/2^{d₁}); phase 2 has no mixed records.

### 7.6 Counting

**Lemma K (the stage).** In phase 1, W_0 has only good and bad-only records. Let gg, gb and bb be the numbers of pairs
with two, one and no good member, and u the number of unpaired good records. Then, deterministically, 2gg + gb + u = G_0,
u ≤ 2^b and gb + 2bb ≤ P_0. Given 𝒦_0 and the keys, G_1 is a sum of gg conditionally fair coins, X_1 is a sum of gb
conditionally fair coins, and B_1 ≤ bb.

*Proof.* Each record of W_0 lies in at most one pair. A key group leaves at most one record unpaired, and at most
2^{b_1} = 2^b groups are nonempty, so u ≤ 2^b. A pair with two good members gives a good output exactly on outcome 1, a
pair with one good member a mixed output exactly on outcome 1, and a pair with no good member a bad-only output or none.
The coins are fair by Lemma C. ∎

**Lemma B₁ (bad leaves).** For guess i*, except with probability < 2e^{−300}: the phase-1 block has at most yM bad
copies, and the phase-2 block has at most (y + τ_s)K₂ bad copies.
*Proof.* Phase 1: by Lemma H with τ = 2^{−10}, there are fewer than (ε + 2^{−10})M malformed copies except with
probability e^{−2·2^{−20}M} = e^{−2^{b−10}}. The coins W of the at most M clean copies are independent with
P(W = 1) < 2/G = 2^{−11}, so by Lemma A (centred indicators) there are fewer than 2^{−11}M + 2^{−11}M = 2^{−10}M
wrapped copies except with probability e^{−2(2^{−11}M)²/M} = e^{−2^{b−12}}. So there are fewer than
(ε + 2^{−9})M = yM bad copies. Phase 2: in the same way, fewer than (ε + τ_s)K₂ malformed copies except with
probability e^{−2τ_s²K₂} = e^{−K₂/320000}, and fewer than 2^{−11}K₂ + 3·2^{−11}K₂ = 2^{−9}K₂ wrapped copies except with
probability e^{−2(3·2^{−11}K₂)²/K₂} = e^{−18·2^{−22}K₂}; so fewer than (y + τ_s)K₂ bad copies. With b ≥ 86 and
K₂ = 2^{20}(d₂ + 8) ≥ 2^{20}·94, the four exponents are at least 2^{74}, 2^{74}, 308 and 423. ∎

**Lemma S₁ (the stage).** In phase 1 of guess i* in the genie run, given at most yM bad leaves, except with probability
2e^{−2^{70}}: |W_1| ≥ G_1 > 0.153235M ≥ K₁, and the weighted bad fraction Φ₁ = (X_1 + (3/2)B_1)/|W_1| of W_1 satisfies
Φ₁ < φ̄ = 0.489.
*Proof.* G_0 = M − P_0 with P_0 ≤ yM, and 2^b = M/512. By Lemma K, gg = (G_0 − gb − u)/2 ≥ (G_0 − gb − 2^b)/2 ≥
(G_0 − P_0 − 2^b)/2 ≥ (1 − 2y − 1/512)M/2 > 0.307070M. Given 𝒦_0 and the keys, by Lemma A, G_1 ≥ (1/2 − δ)gg except
with probability e^{−2δ²gg} ≤ e^{−2^{b−12}}, and X_1 ≤ gb/2 + δM except with probability e^{−2δ²M²/gb} ≤ e^{−2δ²M} =
e^{−2^{b−10}} (if gb = 0, X_1 = 0). On the complement, G_1 ≥ (1/2 − δ)·0.307070M > 0.153235M, and Δ = φ̄G_1 −
(1 − φ̄)X_1 − (3/2 − φ̄)B_1 satisfies, by G_1 ≥ (1/2 − δ)(G_0 − gb − 2^b)/2, X_1 ≤ gb/2 + δM and B_1 ≤ bb ≤ (P_0 − gb)/2,

  Δ ≥ φ̄(1/2 − δ)(G_0 − 2^b)/2 − (1 − φ̄)δM − (3/2 − φ̄)P_0/2 + ((1 − φ̄)/4 + φ̄δ/2)·gb.

The coefficient of gb is positive, and G_0 = M − P_0 with P_0 ≤ yM, so

  Δ ≥ M[φ̄(1/2 − δ)(1 − 2^{−9})/2 − (1 − φ̄)δ − y(φ̄(1/2 − δ) + 3/2 − φ̄)/2] > (0.12177 − 0.00050 − 0.12046)M > 0.

Hence X_1 + (3/2)B_1 < φ̄(G_1 + X_1 + B_1) = φ̄|W_1|. Finally 0.1532M = 0.1532·2^{b+9} > 78·2^b ≥ 2^{20}(n + 8) ≥ K₁ for
n ≥ 256 (n ≤ 3b and 78·2^{b−20} > 3b + 8 for b ≥ 86). ∎

The bound is weakest at gb = 0: a bad–bad pair turns two bad leaves into at most one bad-only record (weight 3/2), which
may survive with certainty, while a good–bad pair uses up a good leaf and yields a mixed record (weight 1) only on a fair
coin.

**Lemma S₂ (sample).** Given W_1, the sample keys are distinct except with probability < 2^{−11}, and then the K₁ kept
records are a uniformly random K₁-subset of W_1 in uniformly random order, independent of everything else. The number of
bad records among them exceeds (P_1/|W_1| + τ_s)K₁, or the number of bad-only records among them exceeds
(B_1/|W_1| + τ_s)K₁, with probability at most 2e^{−2τ_s²K₁} < 2e^{−300}.
*Proof.* As in Lemma Π (|W_1| ≤ M and κ_W = 2·bitlength(M) + 10). Given 𝒦_1, over the sample keys, each count is
hypergeometric with mean (P_1/|W_1|)K₁, resp. (B_1/|W_1|)K₁; apply Lemma H′ to each. 2τ_s²K₁ = K₁/320000 =
2^{20}(d₁ + 8)/320000 > 3.27(d₁ + 8) > 300. ∎

So, outside these events, the K₁ records of phase 1 contain n_x mixed and n_o bad-only records with
n_x + (3/2)n_o = (n_x + n_o) + n_o/2 ≤ (Φ₁ + (3/2)τ_s)K₁ < (0.489 + 0.001875)K₁ < 0.491K₁, since
Φ₁ = (P_1 + B_1/2)/|W_1|; and the K₂ records of phase 2 contain no mixed record and n_o < (y + τ_s)K₂ < 0.1933K₂
bad-only records (Lemma B₁), so n_x + (3/2)n_o < 0.29K₂ < 0.491K₂.

### 7.7 Records and scores

Fix a search of guess i* in the genie run: phase 1 (d = d₁, target θ = σ, the K₁ sampled records) or phase 2 on the
event σ̂ = σ (d = d₂, target θ = h*, the K₂ records). Define the record filtration as follows. In phase 1 let ℋ_0 be
generated by 𝒦_1 (Lemma U: it contains the keys, pairings, A5 outcomes and the labels of the bad-only records, but not the
labels w of the free records of W_1), the sample keys of step 3 and the release outcomes of the records not kept; in
phase 2 let ℋ_0 = 𝒦_0. For j ≥ 1 let ℋ_j = ℋ_{j−1} ∨ σ(w_j, m′_j, b_j). Then the record (w_j, m′_j, b_j) is
ℋ_j-measurable, and the type of record j (good, mixed or bad-only) is ℋ_0-measurable (it is fixed by the malformed set,
the coins W, the sieve structure and the sample). The release of a record not kept is a computational-basis measurement;
by (I1) its outcome law and its effect on the other systems do not depend on the labels of the free records.

**Lemma R (record laws).** Let record j be free and β_j = 2πw_jθ/2^d. Conditioned on ℋ_{j−1}, w_j is uniform on
[0, 2^d), and m′_j is uniform on {0,…,7} and independent of w_j. If record j is good, then given (w_j, m′_j), b_j = 0
with probability exactly p_{m′_j}(w_jθ/2^d). If record j is mixed, then given ℋ_{j−1} and w_j the reduced state of its
qubit is D(β_j)ω_jD(β_j)† for a qubit state ω_j that depends on the history but not on w_j.
*Proof.* By Lemma U and its corollary at the end of 7.5, given 𝒦_1 (phase 1) or 𝒦_0 (phase 2) the labels of the free
records are independent and uniform, and given them the joint state carries the factor D_r(β_r) on each free record r
over a state that does not depend on them, |+⟩ in tensor product for each good record. The sample keys (Lemma S₂) and
m′_j are fresh. Every other generator of ℋ_{j−1} comes from a measurement on systems other than record j's qubit: the
releases of the records not kept, the P2 of the records i < j, and in phase 2 the F_t tests of bad leaves. By (I1), and
because a unitary on a system that is not measured cancels from the probabilities, the probability of each history of
ℋ_{j−1} given the free labels depends on them only through w_1, …, w_{j−1}, which belong to the history. So given
ℋ_{j−1}, w_j is still uniform, and record j's qubit is D(β_j) applied to a state that does not depend on w_j: for a good
record this is φ(w_j) = (|0⟩ + e^{2πi w_jθ/2^d}|1⟩)/√2 in tensor product with everything else, and P2 gives the stated
law (A3). ∎

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
*Proof.* ℋ_{j−1} may contain outcomes of measurements made after the P2 of record j (in phase 2, 𝒦_0 contains the F_t
outcomes of later bad leaves); those instruments act on other systems and do not depend on (m′_j, b_j), so moving them
before the P2 of record j leaves the joint law unchanged, and we may treat them as earlier. Fix an outcome g of ℋ_{j−1}
together with w_j (fixed before m′_j is drawn). Let σ_g be the reduced state of record
j's qubit given g, written (I + xX + yY + zZ)/2 with x + iy = re^{iα}, 0 ≤ r ≤ 1. m′_j is drawn from fresh qubits, so it
is uniform and independent of g, and P2 with θ′ = 2πm′/8 has outcome 0 exactly when it projects onto
(|0⟩ + e^{iθ′}|1⟩)/√2; so E[(−1)^b | g, m′] = x cos θ′ + y sin θ′ = r cos(θ′ − α). With v = w_jτ/2^d and θ′_{m′} = 2πm′/8,
E[X̂_j(τ) | g] = (1/8)Σ_{m′} r cos(θ′_{m′} − α)cos(2πv − θ′_{m′}) = (r/2)cos(2πv − α) + (r/16)Σ_{m′}cos(2θ′_{m′} − α − 2πv)
= (r/2)cos(2πv − α) ∈ [−1/2, 1/2], because Σ_{m′=0}^{7} e^{2iθ′_{m′}} = Σ_{m′} i^{m′} = 0. Lemma D and the tower property give
the claim. ∎

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

**Theorem M (separation).** Fix a search of guess i* as in 7.7 with K records, of which n_x are mixed and n_o bad-only,
with n_x + (3/2)n_o ≤ 0.491K. Then, except with probability < 2^{−40}, S(θ) > K/256 and S(τ) < S(θ) − K/256 for every
τ ≠ θ.
*Proof.* For τ ∈ [0, 2^d) let m_j(τ) = E[Z̃_j(τ) | ℋ_{j−1}] and D_j(τ) = Z̃_j(τ) − m_j(τ). Then E[D_j(τ) | ℋ_{j−1}] = 0
and D_j(τ) ∈ [a_j, a_j + 2R₀] with a_j = −R₀ − m_j(τ) ℋ_{j−1}-measurable. Lemma A (rescaled by 2R₀) gives
P(Σ_j D_j(θ) ≤ −δ_sK) ≤ e^{−δ_s²K/(2R₀²)} and, for τ ≠ θ, P(Σ_j D_j(τ) ≥ δ_sK) ≤ e^{−δ_s²K/(2R₀²)}. Now
δ_s²K/(2R₀²) > 2^{20}(d + 8)/320001 > 3.27(d + 8), so each probability is < e^{−3.27(d+8)} < 2^{−4.7(d+8)}, and a union
bound over the 2^d candidates gives < 2^{d−4.7(d+8)} < 2^{−40}. On the complement, with n_c = K − n_x − n_o good
records, Lemmas C*, X and M give
S(θ) > −δ_sK + n_c(1/2 − η) − (n_x + n_o)(1/2 + η) = K(1/2 − η − δ_s) − (n_x + n_o) ≥ K(1/2 − η − δ_s − 0.491) >
0.0064K > K/256, and for τ ≠ θ, S(τ) < δ_sK + (n_c + n_x)η + n_o(1/2 + η) = K(δ_s + η) + n_o/2. Hence
S(θ) − S(τ) > K(1/2 − 2η − 2δ_s) − (n_x + (3/2)n_o) ≥ K(1/2 − 2η − 2δ_s − 0.491) > 0.00399K > K/256. ∎

*Remark (used in no proof).* The two bounds, K(1/2 − η − δ_s) − (n_x + n_o) for the target and K(δ_s + η) + n_o/2 for
the others, move with the adversary's mix: at ε = 19/100 the first is about 0.11K when the bad records of phase 1 are
all mixed, the second about 0.16K when they are all bad-only, so no single threshold lies between them for every mix.
The ladder of 6.7 needs only the gap.

**Lemma Sr (ladder search).** If S(θ) > K/256 and S(τ) < S(θ) − K/256 for every τ ≠ θ, the search of 6.7 returns θ
except with probability ≤ 2^{−6}.
*Proof.* d ≥ 86 ≥ 4. By Lemma B, S(θ) ≤ R₀K < (257/256)K = ϑ_{257}K. Let ℓ* be the largest ℓ ∈ {1, …, 257} with
ϑ_ℓK < S(θ); it exists because ϑ_1K = K/256 < S(θ), and ℓ* ≤ 256, so ϑ_{ℓ*+1}K ≥ S(θ). For ℓ > ℓ* and every τ,
S(τ) ≤ S(θ) ≤ ϑ_ℓK, so f_ℓ marks nothing: every measured τ̂ fails the check f_ℓ(τ̂) = 1, and the search goes on without
returning. At ℓ = ℓ*, f_{ℓ*}(θ) = 1, and for τ ≠ θ, S(τ) < S(θ) − K/256 ≤ ϑ_{ℓ*+1}K − K/256 = ϑ_{ℓ*}K, so f_{ℓ*} marks
exactly θ. Each of the at most 6 runs at this threshold is an independent run of the circuit of App. C on fresh qubits,
which applies H^{⊗d} and 𝒢_{ℓ*}^{k_G}; by Lemmas G and I (App. D) it returns θ with probability > 1/2, and the classical
check accepts only θ. So the search returns θ unless all six runs at threshold ℓ* fail, which has probability < 2^{−6}. ∎

### 7.9 The test

**Lemma T* (test).** Let X_i be the number of malformed copies in the test block of guess i. If X_i ≤ k/4, then
TEST(s) on that block accepts with certainty, and for every v ≠ s, TEST(v) accepts with probability at most e^{−k/32},
whatever happened before.
*Proof.* After subtracting v, a clean copy is the mixture over x of (|0,x⟩ + |1,(x + s − v) mod N⟩)/√2. If v = s the first
qubit is |+⟩ and H gives 0, so Z ≥ k − X_i ≥ 3k/4. If v ≠ s, the two register values differ, the first qubit is
maximally mixed, and its outcome is a fair coin given everything else (the clean copy is in tensor product with all other
systems). So Z ≤ X_i + Y with Y a sum of k′ = k − X_i conditionally fair coins, and Z ≥ 3k/4 forces Y ≥ 3k/4 − X_i =
k′/2 + (k − 2X_i)/4 ≥ k′/2 + k/8; by Lemma A this has probability ≤ e^{−2(k/8)²/k′} ≤ e^{−k/32}. ∎

By Lemma H with τ = 1/4 − 19/100 = 3/50, P(X_i > k/4) ≤ e^{−2(3/50)²k} = e^{−18k/2500}. With k = 256·bitlength(100G) =
4864, e^{−18k/2500} < e^{−35} and e^{−k/32} = e^{−152} < 2^{−219} < 1/(400G).

### 7.10 Theorem 1 (n ≥ 256)

**Theorem 1.** For every N with n ≥ 256, every s and every adversary of Section 5 with ε = 19/100, RLS outputs s with
probability at least 9/10.
*Proof.* Exclude: the tie of 6.1 (< 2^{−11}, Lemma Π); some test block with X_i > k/4 (≤ G e^{−35} < 2^{−38}); some
TEST(v), v ≠ s, accepting (≤ G e^{−152} < 2^{−200}); the genie run differing from the real run (< 1/100, 7.4); the events
of Lemma B₁ (< 2e^{−300}), Lemma S₁ (< 2e^{−2^{70}}) and Lemma S₂ (< 2^{−11} + 2e^{−300}) for guess i*; the failure of
Theorem M in phase 1 and, on σ̂ = σ, in phase 2 (< 2·2^{−40}); and the failure of Lemma Sr in the two searches
(< 2·2^{−6}). The total is < 0.0005 + 0.01 + 0.0005 + 0.0313 + 10^{−9} < 0.043.
Outside these events, in phase 1 of guess i* the K₁ records satisfy n_x + (3/2)n_o < 0.491K₁ (Lemmas S₁, S₂), so the gap
of Theorem M holds at θ = σ and σ̂ = σ (Lemma Sr). Then the K₂ records of phase 2 satisfy n_x + (3/2)n_o < 0.29K₂ (Lemma
B₁), so ĥ = h* in the same way, and the candidate is σ + 2^{d₁}h* = s′ < N, with (s′ + g*) mod N = s. No wrong candidate
is accepted, and TEST(s) accepts at guess i* unless an earlier guess already output s (Lemma T*). So RLS outputs s with
probability > 0.95 ≥ 9/10. ∎

### 7.11 Small inputs (n < 256)

**Theorem 2.** For every N with n < 256, every s and every adversary with ε = 19/100, the branch of 6.10 outputs s with
probability > 0.99.
*Proof.* Lemmas N and Π hold verbatim for this branch (P(tie) < 2^{−11}). Let X_v be the number of malformed copies among
the K_s copies of candidate v. Lemma H with τ = 3/50 gives P(X_v > K_s/4) ≤ e^{−2(3/50)²K_s} < e^{−7500}. If X_s ≤ K_s/4,
then Z_s ≥ 3K_s/4 (as in Lemma T*). For v ≠ s with X_v ≤ K_s/4, Z_v ≥ 3K_s/4 has probability ≤ e^{−K_s/32}
< e^{−32000}. A union bound over the N ≤ 2^{255} candidates gives total failure < 2^{−11} + 2^{256}(e^{−7500} + e^{−32000})
< 0.01. ∎

Theorems 1 and 2 cover every N ≥ 2 and every s, for every adversary of Section 5 with ε(n) = 19/100, and in particular
for the clean problem.

## 8. Resources (every branch)

For n < 256 every quantity is an absolute constant: exactly Q_s = N·2^{20} ≤ 2^{255}·2^{20} = 2^{275} copies (N ≤ 2^n
≤ 2^{255}), O(Q_s n + Q_s log₂ Q_s·κ′) bit operations and gates before the address charge (itself O(log Q_s)),
(n+1)Q_s + O(n) qubits held and O(Q_s κ′) bits. These constants are astronomically large but independent of N, s and
all outcomes. Let n ≥ 256.

**Sizes.** b ≤ n/3 + 1, so M = 2^{b+9} ≤ 2^{10}·2^{n/3}; K₁, K₂ ≤ 2^{20}(n + 8); G = 2^{12}; k = 4864. Hence

  **Q = G(M + K₂ + k) < 2^{12}(2^{10}·2^{n/3} + 2^{20}(n + 8) + 4864) < 2^{23}·2^{n/3},**

counting every acquired copy (all are acquired in 6.1, on every branch; 2^{n/3} ≥ 2^{85} dominates the other terms).
Also log₂ Q < n/3 + 23, so κ, κ_W < n + 60 and L₁ ≤ log₂ Q + log₂(1600(n+1)) + 1 < n, i.e. κ, κ_W, L₁, r₁ = O(n).

**Quantum space.** All Q copies are held from 6.1 until they are used: (n+1)Q qubits. In addition, at any time: one
copy's O(n) LEAF/F_t ancillas, one test control, one A4 qubit and one TEST ancilla set; in a search, the d search qubits,
U (w qubits), V (p) with O(p) ancillas, k (q), v (27) with O(q) ancillas, the O(w) ancillas of P3b, the flag with O(w)
carry ancillas, the diffusion target and its d − 2 ancillas: O(n) qubits, one fixed pool reused for every record, call and
repetition. Measured qubits are released. **S_Q ≤ (n+1)Q + O(n) = O(2^{n/3} n).**

**Classical space.** Sort keys and workspace and the rank table: O(Q(κ + bitlength(Q))) = O(Qn) bits. Phase 1 of the
current guess: M labels of n bits and M copy indices, the 2^b key counters, the sample keys of κ_W bits with merge-sort
workspace: O(Mn) bits. The stored search records: K(d + 4) = O(n²) bits. The table: 27·2^{24} bits (an absolute
constant). F_t counters, parameters, the Grover controller (K_G, k_G, counters) and one gate description: O(n²) bits.
**S_C = O(Qn) = O(2^{n/3} n).** Hence 𝔐 = O(2^{n/3}n), log₂(𝔐 + 2) < n/3 + 2 log₂ n + O(1), and **A = O(n)**.

**Work** (every operation charged O(A) = O(n)).
* Acquisition: Q(n+1). Keys and merge sort of 6.1: O(Q log₂ Q·κ) = O(Qn²) bit operations, O(Qn³) charged.
* Leaves (at most G(M + K₂) ≤ Q of them): LEAF uses O(n) gates; F_t uses 8(J+1)r₁ ≤ 8n·r₁ kickback tests of O(n) gates;
  Lemma P and the rounding O(n²). A leaf costs O(n²r₁) = O(n³) operations, O(n⁴) charged; in total O(Qn⁴).
* Phase-1 stage and sample, per guess: O(Mn) bit operations for keys, counting sort and subtractions, one A5 per pair,
  O(2^b log M) for the counters, and O(M log₂ M·κ_W) for the sample keys and their sort: O(Mn²), O(Mn³) charged; over
  G guesses O(Qn³).
* Table (App. B): an absolute constant number of operations. Records: O(K) operations per search.
* Searches, per guess: phase 1 has at most 1542 runs (257 thresholds, at most 6 each) of at most k_G ≤ 0.785·2^{d₁/2} ≤
  2^{n/3} Grover iterations. One call of 𝒪_ℓ costs, per record, d applications of P3a on p qubits (O(dp)),
  O(p + q), one table read (O(2^q(q + 27)), an absolute constant) and one P3b (O(w)), done and undone, so
  O(K(dp + w)) = O(n² log n) gates;
  𝒟 costs O(d); the flag constant of each threshold costs O(w). A run also evaluates f_ℓ(τ̂) classically in
  O(Kdp) = O(n² log n). As 1542 is an absolute constant, phase 1 costs
  O(2^{n/3} n² log n) operations, O(2^{n/3} n³ log n) charged, and phase 2 O(2^{d₂/2} n³ log n) = O(2^{n/6+1} n³ log n).
  Over G guesses the same orders.
* TEST: G·k copies, O(n) gates each. Grid points and parameters: O(Gn²). Releasing unused blocks, or all copies on a
  tie: at most Q(n+1) measurements and resets.

The leaf term dominates: **T = O(Qn⁴ + 2^{n/3}n³ log n) = O(2^{n/3} n⁴).**

All four bounds hold simultaneously on every execution branch of this one algorithm with this one parameter rule
(every loop length is bounded by a fixed function of N; the copy count is exactly Q), jointly with Theorems 1 and 2,
for every adversary of Section 5.

## 9. Exact growth indices and structured envelopes

For ℬ(n) = 2^{n/3} n^r with fixed r ≥ 0: log₂ ℬ = n/3 + r log₂ n, so log₂ log₂ ℬ = log₂ n − log₂ 3 + log₂(1 + 3r log₂ n/n),
and log₂ log₂ ℬ/log₂ n → 1. Hence g(ℬ) = 1 (the max{4,·} is irrelevant for large n); outer constants do not change it.

* T: ℬ_T = 2^{n/3} n⁴, index **1**: exponent [{coefficient 1/3, nPower 1, logPower 0}], nPower 4, logPower 0.
* S_C: ℬ = 2^{n/3} n, index **1**: exponent [{1/3, 1, 0}], nPower 1, logPower 0.
* S_Q: ℬ = 2^{n/3} n, index **1**: exponent [{1/3, 1, 0}], nPower 1, logPower 0.
* Q: ℬ = 2^{n/3}, index **1**: exponent [{1/3, 1, 0}], nPower 0, logPower 0.

Published time score: [1]. Under the asymptotic comparator the time envelope is strictly below 2^{n/2}·poly(n).

## 10. Fractional error tolerance

ε(n) = 19/100 under the model of Section 5: with Q acquired copies, at most floor(19Q/100) of them are malformed; their
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
* New here: the phase-covariance form (J) of Lemma U, Lemma X (a mixed record's score has conditional mean within η of
  0 at every wrong candidate), the three-type count of Lemmas K and S₁, Theorem M in gap form and the threshold ladder
  (Lemma Sr). The algorithm is our RLS-G1 (4ef5cf09) with the ladder search in place of its single threshold 7/40; the
  slack δ_s = 1/400 with K = 2^{20}(d + 8) records and τ_s = 1/800 follows our RLS-G2R (484bc509).
* Our own components, re-proved here: the splice, F_t and A1–A4 (SLS, 59facd77); A5 and Lemma P (OMX-ML, 31c2d043); the
  full-upfront acquisition, the permutation and Lemmas N, Π, U, C, K and the genie run (RLS, 280a17e4); the shadow score,
  the cosine table, the oracle circuits and Lemmas B, D, C*, M (ROB-G2, 55a6ce76; adapted to labels in Z/2^dZ). The model
  is that of our ROB line (d0c6b9b9, 5d77f276, a5c17989, 55a6ce76).
* Rows in this error-model text (credited, nothing used): mpjunior92's RQ-SPLIT 38d66dc0 and dadon's f892f7ea (1/3 at
  2^{n/2}·poly with polynomial memory and samples); dadon's 7341d79b (1/(896n) at work 2^{n/3}·poly).
* Other positive-tolerance prior work (credited, nothing used):
  mpjunior92's PSG13 4c42d100 (same model, tolerance 1/(2^{39}n⁴), time 2^{n/6}·poly with polynomial memory);
  kaankolcu's RWT25 3f48c893 (1/4, fixed-position model); GordoAR's c730b22b (1/3, own model); smoke-era RGRST1
  be98e61b, CGRST1 53b4755b, CADGR1 5f048e8b/b838e1ae, CADGR2 45044787, RLQGR1–3 ee378bae, 635a47e2, 0e1559e4, 09c05313,
  7b2afdfc. Regev (SIAM J. Comput. 33 (2004), Definition 2.1) studies DCP with a failure parameter.

Context (not part of any claim). New here: a good–bad pair's output is phase covariant with an exactly uniform label,
so the shadow score sees it as noise at every wrong candidate; only bad–bad outputs can create a false peak, and the
search needs only the score gap, which the threshold ladder exploits. This lifts the one-stage tolerance from 1/7 to
19/100 at the same envelopes (the exact maximum with these constants and φ̄ = 0.489 is about 0.1913; as all slack
constants tend to 0 the one-stage count allows every ε < 1/5, the old count every ε < 1/6). No cited result is used as
a lemma except Hoeffding's inequality for sampling without replacement (Lemmas H, H′), cited with its exact theorem
number; Lemma A is proved in the file.
