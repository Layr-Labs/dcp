# RLS-3L: a robust low-bit sieve with 3ceil(log₂ n) stages, O(2^{n/(3log₂ n)} n^{14}/log n) work, adaptive malformed-copy tolerance 1/(32n³)

This file is the complete proof of all five claims in `submission.json`. It describes one
algorithm, **RLS-3L** (called RLS below; it is our RLS 280a17e4 with three times as many stages), with one fixed
parameter rule, and proves for every integer N ≥ 2, every
s ∈ Z/NZ, with n = ceil(log₂ N) and L = log₂ n, and every adversary of the error model of
Section 5 (which contains the clean problem as the adversary that corrupts nothing):

* the output equals s with unconditional probability at least 9/10 (> 2/3);
* total work T = O(2^{n/(3L)} n^{14}/L);
* peak classical space S_C = O(2^{n/(3L)} n^{11}) bits;
* peak quantum space S_Q = O(2^{n/(3L)} n^{11} L) qubits;
* acquired source copies Q = O(2^{n/(3L)} n^{10} L); Q is a fixed function of N, the same on every branch;
* fractional error tolerance ε(n) = 1/(32n³): at most floor(Q/(32n³)) acquired copies may be malformed,
  at adversarially and adaptively chosen positions, with arbitrary, possibly entangled contents.

All constants are absolute (independent of N, s, the adversary and all outcomes). Every loop of
RLS has a length bounded by a fixed function of N (G guesses, n rounds, at most R stages, at most M records
per list, Q copies), so the four resource bounds hold on every execution branch whatever the copies contain. Logarithms are base 2 unless written ln. All four growth indices equal 1; the time
envelope 2^{n/(3L)} n^{14}/L has exponent n/(3log₂ n), which is o(n). (Context, not part of any claim: this is our RLS
(280a17e4, R = ceil(log₂ n) stages, tolerance 1/(8n) at 2^{n/L}·poly) with three times as many stages; it divides the
exponent by 3 for a tolerance smaller by a factor 4n².)

**Idea.** (i) *Acquire everything first.* RLS acquires all Q copies before it makes its first
measurement. The adversary of Section 5 sees only measurement outcomes obtained before each delivery,
so it sees none: its choice of the malformed set and contents is made without any information about
RLS's randomness. (ii) *Spread the corruption.* A uniformly random permutation then assigns copies to
slots, so every slot block contains about an ε fraction of malformed copies (Hoeffding's bound for
sampling without replacement). (iii) *Exact power-of-two leaves.* As in our SLS (submission 59facd77),
subtracting a grid guess g turns a copy into an exact coset state of Z/2^tZ unless it "wraps", which it
does with probability < 2/G for the right guess; wrapped copies are treated as malformed. (iv) *A
low-bit sieve whose clean part stays exactly uniform.* Records are labelled qubits of Z/2^tZ. A stage
groups records by the next b label bits, pairs records within each group, combines each pair by one
CNOT and one measurement and keeps the difference. A pair needs no particular partner distribution:
every group of size m yields floor(m/2) pairs, so the yield bound holds for *any* labels. The
difference of two independent uniform elements of a coset of 2^l Z/2^tZ is uniform; hence, whatever the
malformed records do, the clean records' unexamined label bits stay exactly i.i.d. uniform (Lemma U). The
final label is 2^{t−1}, and a clean qubit of that label reveals one bit of the secret with certainty.
(v) *Corruption dies out at rate 1/2.* A record that contains a malformed leaf survives a stage only on a
fair coin when its partner is clean (Lemma C), while clean records shrink by a factor 4. With
R = 3ceil(log₂ n) stages, the bad fraction can grow by about 2^R < 8n³. A potential Φ = 1/z + 1 of the
bad-to-good ratio z halves per stage. So if at most 17/(64·2^R) of a round's leaves are bad, clean
votes outnumber bad votes at the end (Lemma Z), and a majority vote reads the bit.

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
uniform generator emits these gate lists one gate at a time in O(n) bit operations from a, N, t.

**A3 (phase test).** For a qubit (|0⟩ + e^{2πiθ}|1⟩)/√2 and m′ ∈ {0,…,7}, apply (T†)^{m′}, then H,
then measure. Outcome 0 has probability exactly p_{m′}(θ) = (1 + cos 2π(θ − m′/8))/2.

**A4 (fair bits).** A fresh |0⟩, H, measurement: one exact fair bit, O(1) work.

**A5 (combination).** Given qubits a, b, apply CNOT (control a, target b) and measure b. If a and b
are label-v₁ and label-v₂ qubits φ_σ(v₁), φ_σ(v₂) in a product state, with α_i = 2πv_iσ/M′, the state
before the measurement is (|00⟩ + e^{iα₂}|01⟩ + e^{iα₁}|11⟩ + e^{i(α₁+α₂)}|10⟩)/2. Outcome 0
(probability exactly 1/2) leaves a in φ_σ(v₁ + v₂); outcome 1 (probability exactly 1/2) leaves a in
(e^{iα₂}|0⟩ + e^{iα₁}|1⟩)/√2, which is φ_σ(v₁ − v₂) up to a global phase.

**Cost convention.** Let 𝔐 be the number of allocated bits plus qubits. Section 8 shows
𝔐 = O(2^{n/(3L)} n^{11} L), so a classically indexed access or classically addressed gate costs
A = ceil(log₂(𝔐 + 2)) = O(n/L) bit operations for its address. Every gate, measurement,
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

For **n ≥ 2048**:

* **R** = 3·bitlength(n−1) = 3ceil(log₂ n), so n³ ≤ 2^R < 8n³, R ≥ 33 and R ≤ 3log₂ n + 3 ≤ (10/3)log₂ n.
* **b** = ceil((n−1)/R) (bits per stage), so b ≤ (n−1)/R + 1 < n/(3log₂ n) + 1, i.e. 2^b < 2·2^{n/(3L)}.
  Also b ≥ (n−1)/(3log₂ n + 3) ≥ 2047/36 > 56 (the middle function is increasing for n ≥ 2048), so b ≥ 57, and
  R ≤ b (R ≤ 3log₂ n + 3 ≤ (n−1)/(3log₂ n + 3) ≤ (n−1)/R ≤ b, as (3log₂ n + 3)² ≤ n − 1 for n ≥ 2048). Also
  n ≤ 2^b (b ≥ (n−1)/(3log₂ n + 3) ≥ log₂ n).
* **M** = R·2^{b+2R+6} (leaves per round).
* **G** = 2^{R+9} (grid size); grid points g_i = floor(iN/G) for i = 0, …, G−1. Since
  N ≥ 2^{n−1} > 4096n³ > G, the g_i are distinct.
* **k** = 64·bitlength(100G) (copies per test).
* **Q** = G(nM + k) (copies acquired).
* L₁ = bitlength(1600(n+1)Q); **r₁** = 200L₁ (tests per level and phase in F_t).
* **κ** = 2·bitlength(Q) + 10 (sort-key bits).
* For a round with t ∈ {1,…,n}: stage boundaries l_m = min(mb, t−1) for m = 0, …, R_t, where
  R_t = ceil((t−1)/b) (R_t = 0 for t = 1); stage widths b_m = l_m − l_{m−1} ∈ [1, b]. Since
  (n−1)/b ≤ R, R_t ≤ R.

Analysis constants (not used by the algorithm): ε = 1/(32n³), δ = 1/(128R), τ_h = 2^{−R}/128,
ȳ = 17/(64·2^R).

For **n < 2048**: K_s = 2^{19}; Q_s = N·K_s; κ_s = 2·bitlength(Q_s) + 10 (Section 6.8).

## 5. Error model (adaptive malformed copies)

Copies are delivered one at a time in acquisition order j = 1, …, Q (Q is given by Sections 4 and 6.1).
An **adversary** knows N, s, the full description of RLS, and every measurement
outcome obtained by RLS before copy j is delivered; it holds an arbitrary private quantum system E which
it may measure and process. Before copy j is delivered it chooses c_j ∈ {clean, malformed}, as a function
of that information and its own outcomes; on every branch at most floor(εQ) copies are malformed,
ε = ε(n) = 1/(32n³).

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

### 6.1 Acquisition and permutation (n ≥ 2048)

1. Acquire Q copies, one after another, and hold all of them. **No measurement and no fair bit is
   made before the last copy has been delivered.**
2. Draw Q keys K_1, …, K_Q of κ fair bits each (A4). If two keys are equal, measure everything and
   output 0. Otherwise sort the copies by key (merge sort on (key, index) pairs) and let π(p) be the
   index of the copy of rank p (p = 1, …, Q). The table p ↦ π(p) is stored.

### 6.2 Slot layout

Ranks are grouped into G consecutive blocks of nM + k ranks, block i belonging to guess g_i. Inside
block i, the first nM ranks form n consecutive **round blocks** of M ranks (round j = 0, …, n−1), and the
last k ranks form the **test block**. "The ℓ-th copy of round (i, j)" means the copy π(p) for the ℓ-th
rank p of that round block.

### 6.3 LEAF_t (one held copy, guess g, round j, t = n − j, current σ_low)

1. Controlled on the first qubit c, apply P1 with a = (N − g) mod N (subtract g mod N).
2. Controlled on c, add (2^n − σ_low) mod 2^n to the register (A2, mod 2^n).
3. Measure the low j register qubits and release them. Call the remaining t qubits the register.
4. Draw t fair bits (A4) forming ζ ∈ [0, 2^t); add ζ mod 2^t to the register (A2, uncontrolled); then
   erase ζ (no later step reads it, or the outcomes of step 3).
5. Run F_t on the register, giving û ∈ [0, 2^t); measure and release the register.

Return the record (qubit c, label x = û).

### 6.4 SIEVE_t and VOTE (one round)

Input: the list W_0 of the M records returned by LEAF_t on the M copies of the round, in rank order.
For m = 1, …, R_t:

* **Group.** Every record label x of W_{m−1} satisfies x ≡ 0 mod 2^{l_{m−1}} (shown below). Its key is
  κ_m(x) = floor(x/2^{l_{m−1}}) mod 2^{b_m}. Sort W_{m−1} stably by key (counting sort with 2^{b_m}
  counters).
* **Pair.** Within each key group, in list order, form pairs (1st, 2nd), (3rd, 4th), …; a last unpaired
  record is released (its qubit measured and released, its label discarded).
* **Combine.** For each pair (a, b), in list order of a, apply A5 with a as control. On outcome 1,
  output the record (qubit a, label (x_a − x_b) mod 2^t). On outcome 0, release both qubits.
* W_m = the outputs, in list order of their first members.

Since paired labels agree on bits [0, l_m), every output label is ≡ 0 mod 2^{l_m}; by induction every
label of W_m is, so the keys are well defined, and every label of W_{R_t} lies in {0, 2^{t−1}}
(l_{R_t} = t − 1; for t = 1 the labels of W_0 lie in {0, 1} = {0, 2^{t−1}}).

**VOTE.** For each record of W_{R_t} with label 2^{t−1}, apply H to its qubit and measure, giving a vote
bit. Release every other record. The round's output o_j is 1 if more votes are 1 than 0, and 0 otherwise
(also when there are no votes).

### 6.5 INNER(g_i)

Set σ_low = 0. For j = 0, …, n−1 (t = n − j): apply LEAF_t to the M copies of round (i, j), run SIEVE_t
and VOTE on the resulting records, and set σ_low ← σ_low + 2^j o_j. Return σ = σ_low ∈ [0, 2^n).

### 6.6 TEST(v) (the k copies of the test block of guess i)

For each copy: controlled on its first qubit, apply P1 with a = (N − v) mod N (subtracting v from the
register); apply H to the first qubit and measure it; release the copy. Let Z be the number of outcomes
0. Accept iff 4Z ≥ 3k.

### 6.7 Output (n ≥ 2048)

For i = 0, …, G−1: run INNER(g_i), giving σ; if σ < N, run TEST((σ + g_i) mod N) on the test block of
guess i, and if it accepts, output (σ + g_i) mod N and halt. If no candidate is accepted, output 0.
(Copies of unused blocks are measured and released at the end; they were acquired in step 6.1.)

### 6.8 Small inputs (n < 2048)

Acquire Q_s = N·K_s copies and hold them (no measurement before the last delivery). Draw Q_s keys of κ_s
fair bits; on a tie output 0; otherwise sort as in 6.1, and give candidate v ∈ [0, N) the K_s copies of
ranks vK_s + 1, …, (v+1)K_s. For each v run the test of 6.6 with this v on its K_s copies, giving the
number Z_v of outcomes 0. Output the smallest v with 16Z_v ≥ 13K_s, or 0 if there is none.

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

**Notation in Section 7.** Some letters have local meanings: G_m and P_m count good and bad records and g_k,
p_k are deterministic sequences, unrelated to the grid size G, the grid points g_i and the wrap probability p;
k is a running index in Lemma Z (within Section 7 the test block size k appears only in 7.8 and 7.9); s is the
secret.

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
linearity) realise every clean copy of the blocks of guess i* as ρ^{nw} or ρ^{w} by an independent coin
W with P(W = 1) = p: this is the same state. A copy of a round of guess i* is **good** if it is clean
and W = 0, and **bad** otherwise (malformed, or clean with W = 1).

The **genie run** is the modified process (an analysis device, not an event) in which, during each round
of INNER(g*) that starts with σ_low = s′ mod 2^j, the label returned by F_t for every good leaf is replaced by
its true label u of Lemma S (F's tests are still performed and their outcomes ignored). From the first
round that starts with σ_low ≠ s′ mod 2^j on, the genie run follows the rules of RLS (no replacement).
No step of RLS reads ζ, so in the analysis step 4 of every leaf is replaced by its ζ-average (the same
channel): ζ is not a random variable of either run, and "the past", "all outcomes" and 𝒦_0 never include it. Realise all measurement outcomes of the real run and of the
genie run from one common sequence of independent uniforms, through their conditional laws given the
past. The two runs take the same actions and have the same quantum state until the first good leaf with
û ≠ u. INNER(g*) processes nM ≤ Q leaves, and each good one in a round where u is defined has
P(û ≠ u | past) < 1/(100Q), so the runs differ with probability < 1/100 (sum of conditional probabilities over the ≤ Q leaves).

### 7.5 Structure of a round in the genie run

Consider round j of INNER(g*) in the genie run, on the event that σ_low = s′ mod 2^j at its start. In
7.5–7.7, "the past" and every conditioning exclude, in addition, the F_t outcomes of the round's good leaves
(the genie run never reads them, so by linearity we may average over them); step-3 outcomes may be included or
not (Lemma S holds conditionally on them).
A record is **good** if every leaf of its combination tree is a good leaf, and **bad** otherwise; G_m and
P_m are the numbers of good and bad records of W_m.

**Lemma C (fair coins).** Let a pair contain at least one good record. Conditioned on the past (in the sense
above) and on the labels of all good records, the outcome of its A5 measurement is 0 or 1 with probability
exactly 1/2; in particular it is independent of the good members' labels. If both records are good, then on
outcome 1 the output qubit is φ_{σ_hi}(x_a − x_b), in tensor product with everything else.

*Proof.* By invariant (J) of Lemma U at the preceding stage (Lemma U at stage m uses Lemma C only for the
pairs of stage m, so there is no circularity), a good record's qubit is φ_{σ_hi}(x) for its label x, in
tensor product with all other systems given the past and the good labels. Its computational-basis diagonal is (1/2, 1/2). Let ρ be the joint state of the pair
(and the rest) before the CNOT, and let o be the measured value. If b is good, P(o) = Σ_c ⟨c|ρ_a|c⟩·
⟨o⊕c|ρ_b|o⊕c⟩ = Σ_c ⟨c|ρ_a|c⟩/2 = 1/2; if a is good, P(o) = Σ_c (1/2)⟨o⊕c|ρ_b|o⊕c⟩ = 1/2. Because the
good qubit is in tensor product with everything else, the same computation holds conditioned on any
event of the other systems. For two good qubits A5 gives the stated outputs with probability 1/2 each,
whatever x_a, x_b are. ∎

Let 𝒦_0 be the σ-algebra generated by: h; the rank map; everything before the round (all outcomes of
earlier guesses and rounds); the coins W; the identity of the good leaves; and every outcome and label
of the bad leaves of the round. It does not contain the step-3 outcomes, ζ or F's outcomes of good
leaves, which no later step reads in the genie run. For m ≥ 1, let 𝒦_m be generated by 𝒦_{m−1}, the
stage-m keys of all records of W_{m−1}, the pairing, all stage-m A5 outcomes, the stage-m release
outcomes, and the labels of the bad records of W_m.

**Lemma U (exact uniformity).** For m = 0, …, R_t: (U) conditioned on 𝒦_m, the values
floor(x_r/2^{l_m}) for the good records r of W_m are independent and uniform on [0, 2^{t−l_m}); and (J)
conditioned on 𝒦_m and on the labels of the good records of W_m, the joint state of all systems is
⊗_{r good in W_m} φ_{σ_hi}(x_r) ⊗ Ω_m, where Ω_m (the bad records of W_m, all held copies, released
systems other than the step-3 qubits and F_t test qubits of the round's good leaves, which are averaged out,
and E) does not depend on the labels of the good records of W_m.

*Proof.* m = 0: by Lemma S and (2.1) the true labels of the good leaves are independent uniform on
Z/2^tZ, independent of everything in 𝒦_0 (good copies are in tensor product with all other systems and
the genie run ignores F's outcomes on them; the coins W are independent of the labels); given the labels,
each good leaf's first qubit is φ_{σ_hi}(u) in tensor product with everything else, which is (J).
Step m−1 → m: for a good record r of W_{m−1} write floor(x_r/2^{l_{m−1}}) = κ_r + 2^{b_m}η_r with
κ_r ∈ [0, 2^{b_m}) its stage-m key and η_r ∈ [0, 2^{t−l_m}). By hypothesis all κ_r, η_r are independent
and uniform given 𝒦_{m−1}. The keys of bad records are 𝒦_{m−1}-measurable, so the grouping and the
pairing are functions of 𝒦_{m−1} and the keys only, and do not depend on any η_r. Every stage-m
measurement acts on records that are consumed or released at stage m, and its outcome law is independent
of the labels of the good records that survive into W_m. (i) A5 on a pair with a good member: a fair coin
(Lemma C). (ii) A5 on a bad–bad pair, and every release of a bad qubit outside a mixed pair: by (J) at m−1 these act
on Ω_{m−1} only. (iii) Release of an unpaired good record, or of the control of a good–good pair with outcome 0: a
computational-basis measurement of φ(x), a fair coin for every x. (iv) Release after a mixed pair with
outcome 0: before the CNOT the good qubit is φ(x) ⊗ (the bad side and E). The joint computational-basis
diagonal of the two qubits and the post-measurement state of E depend only on the bad side, because
the phase of φ(x) multiplies whole branches and drops out of every diagonal term. So these outcomes are
independent of x too. After a mixed pair with outcome 1 nothing is released; the bad output's state depends on
the consumed good label x only through off-diagonal terms, and x is determined by 𝒦_m (the output label minus
the bad member's label), so Ω_m may depend on it. The labels of the bad outputs of W_m involve only bad-record labels and the labels
of good records consumed in mixed pairs (x_a − x_b with one known term), and none of these belong to W_m.
Hence (J) at m: the surviving good qubits are untouched, except good–good outputs, which are
φ(x_a − x_b) in tensor product (A5), and Ω_m collects everything else. For a good–good pair (a, b)
with outcome 1, κ_a = κ_b and both labels are ≡ 0 mod 2^{l_{m−1}}, so x_a − x_b ≡ 2^{l_m}(η_a − η_b)
(mod 2^t) and the new value floor(x′/2^{l_m}) is (η_a − η_b) mod 2^{t−l_m}. Over disjoint pairs these are
independent, each uniform because η_a, η_b are independent and uniform. ∎

In particular (m = R_t) the labels of the good records of W_{R_t} are independent and uniform on
{0, 2^{t−1}} given 𝒦_{R_t}, and a good record of label 2^{t−1} is the qubit
(|0⟩ + (−1)^{σ_hi}|1⟩)/√2, so VOTE gives it the vote σ_hi mod 2, which is bit j of s′, with certainty.

### 7.6 Counting

**Lemma K (one stage).** At stage m let gg, gb, bb be the numbers of good–good, good–bad and bad–bad
pairs. Then, deterministically, gg ≥ (G_{m−1} − P_{m−1} − 2^b)/2 and gb + 2bb ≤ P_{m−1}. Given 𝒦_{m−1}
and the keys, G_m is a sum of gg conditionally fair coins, and P_m ≤ X + bb where X is a sum of gb
conditionally fair coins.

*Proof.* A key group with c records yields floor(c/2) ≥ (c − 1)/2 pairs, and at most 2^{b_m} ≤ 2^b
groups are nonempty, so there are at least (G_{m−1} + P_{m−1} − 2^b)/2 pairs. Each bad record lies in at
most one pair, so gb + 2bb ≤ P_{m−1} and gg ≥ #pairs − (gb + bb) ≥ #pairs − P_{m−1}. A good output arises
exactly from a good–good pair with outcome 1, and a bad output from a mixed pair with outcome 1 or from a
bad–bad pair. The coins are fair by Lemma C. ∎

Define deterministic sequences (real numbers) for k = 0, …, R:

  p₀ = ȳM, g₀ = (1 − ȳ)M; p_k = (1/2 + δ)p_{k−1}, g_k = (1/2 − δ)(g_{k−1} − p_{k−1} − 2^b)/2.

**Lemma Z (the sequences).** Let ν = δ = 1/(128R). For every k ∈ {0,…,R}: (a) g_k > 0 and
(1/2 − δ)g_k > p_k; (b) g_k ≥ 208R·2^b (in particular g_k ≥ 128R·2^b) for k ≤ R−1; (c) g_k ≥ 42R·2^b and p_k ≥ 17R·2^b.

*Proof.* Put ρ = 2(1+2δ)/(1−2δ), θ = (1−ν)/ρ, z_k = p_k/g_k and Φ_k = 1/z_k + 1. Numerical facts, with
δ ≤ 1/1024 (R ≥ 8): (i) ln((1+2δ)/((1−2δ)(1−δ))) ≤ 2δ + 2δ/(1−2δ) + δ/(1−δ) ≤ 5.006δ (using
ln(1+x) ≤ x and −ln(1−x) ≤ x/(1−x)), so θ^{−j} = 2^j((1+2δ)/((1−2δ)(1−δ)))^j ≤ 2^j e^{5.006/128}
< 1.04·2^j for every j ≤ R. (ii) Φ₀ = (1−ȳ)/ȳ + 1 = 1/ȳ = (64/17)2^R > 3.764·2^R.
(iii) 1/(1/2−δ) + 1 = (3−2δ)/(1−2δ) < 3.004.
We prove by induction on k the statements Φ_k ≥ θ^kΦ₀ and (b). For k = 0 both hold
(g₀ ≥ (1 − 17/16384)M > 0.998·R·2^{b+2R+6} ≥ 128R·2^b). Step k−1 → k (1 ≤ k ≤ R): by (b) at k−1,
2^b ≤ νg_{k−1}. By the hypothesis and (i),(ii), Φ_{k−1} ≥ θ^{k−1}Φ₀ > 3.764·2^R/(1.04·2^{k−1})
> 3.619·2^{R−k+1}, so z_{k−1} = 1/(Φ_{k−1} − 1) < 1/(3.1·2^{R−k+1}) ≤ 0.162 (since 0.519·2^{R−k+1} ≥ 1).
Then g_{k−1} − p_{k−1} − 2^b ≥ g_{k−1}(1 − z_{k−1} − ν) > 0, and

  z_k = ρ·z_{k−1}·g_{k−1}/(g_{k−1} − p_{k−1} − 2^b) ≤ ρz_{k−1}/(1 − z_{k−1} − ν).

Hence 1/z_k ≥ ((1−ν)/z_{k−1} − 1)/ρ and Φ_k ≥ θΦ_{k−1} + (ρ − 2 + ν)/ρ ≥ θΦ_{k−1} ≥ θ^kΦ₀, as ρ > 2.
For (b) at k ≤ R−1: g_k ≥ ((1−2δ)/4)(1 − z_{k−1} − ν)g_{k−1}, and iterating,

  g_k ≥ 4^{−k}(1−2δ)^k (1 − Σ_{i=1}^{k}(z_{i−1} + ν)) g₀.

With z_{i−1} < 1/(3.1·2^{R−i+1}), Σ_{i≤k} z_{i−1} < (1/3.1)Σ_{m≥R−k+1}2^{−m} = 2^{−(R−k)}/3.1, and
Σ ν ≤ Rν = 1/128, (1−2δ)^k ≥ 1 − 2Rδ = 63/64. For k ≤ R−1, 2^{−(R−k)} ≤ 1/2, so
g_k ≥ 4^{−k}(63/64)(1 − 0.1613 − 0.0079)(0.998)M ≥ 0.815·R·2^{b+2(R−k)+6} ≥ 0.815·R·2^{b+8}
> 208R·2^b. This completes the induction.
(a): z_k = 1/(Φ_k − 1) and Φ_k ≥ θ^kΦ₀ ≥ θ^RΦ₀ > 3.764/1.04 > 3.619 > 3.004 > (3−2δ)/(1−2δ), i.e.
z_k < 1/2 − δ; g_k > 0 was shown in the step.
(c): the same product bound with k = R (2^{−(R−k)} = 1) gives g_R ≥ 4^{−R}(63/64)(1 − 0.3226 − 0.0079)
(0.998)R·2^{b+2R+6} > 42R·2^b, and g_k ≥ g_R for k ≤ R because g_k ≤ g_{k−1}/4. Finally
p_k ≥ p_R ≥ 2^{−R}ȳM = 17R·2^b. ∎

### 7.7 One round

**Lemma V (a round of the good guess).** In the genie run, condition on 𝒦_0 for round j of INNER(g*), on the
event that σ_low = s′ mod 2^j at its start and that the round has at most ȳM bad leaves. Then o_j equals
bit j of s′, except with conditional probability at most (2R + 1)e^{−2^{b/2}}.

*Proof.* We show that, except on the stated probability, G_m ≥ g_m and P_m ≤ p_m for m = 0, …, R_t, and
the number V of good final records of label 2^{t−1} is at least (1/2 − δ)G_{R_t}. Then VOTE has at least
V ≥ (1/2−δ)g_{R_t} > p_{R_t} ≥ P_{R_t} votes equal to bit j of s′ (Lemma U) and at most P_{R_t} other
votes (every vote comes from a good or a bad final record; Lemma Z(a)), so the majority is correct.
m = 0: P₀ ≤ ȳM = p₀ and G₀ = M − P₀ ≥ g₀. Step m−1 → m (on G_{m−1} ≥ g_{m−1}, P_{m−1} ≤ p_{m−1}):
By Lemma K, gg ≥ (g_{m−1} − p_{m−1} − 2^b)/2 = g_m/(1/2 − δ) ≥ 2g_m ≥ 84R·2^b (Lemma Z(c)). By Lemma A,
P(G_m < (1/2 − δ)gg) ≤ e^{−2δ²gg}, and otherwise G_m ≥ g_m. For the bad records, X is a sum of gb ≤ P_{m−1}
fair coins; by Lemma A, P(X ≥ gb/2 + δp_{m−1}) ≤ e^{−2δ²p²_{m−1}/gb} ≤ e^{−2δ²p_{m−1}} (if gb = 0, X = 0).
Otherwise P_m ≤ gb/2 + bb + δp_{m−1} ≤ P_{m−1}/2 + δp_{m−1} ≤ (1/2 + δ)p_{m−1} = p_m.
Final: given 𝒦_{R_t}, V is a sum of G_{R_t} independent fair bits (Lemma U), so
P(V < (1/2 − δ)G_{R_t}) ≤ e^{−2δ²G_{R_t}} ≤ e^{−2δ²g_R}.
Exponents: with δ² = 1/(16384R²), 2δ²gg ≥ 2δ²·84R2^b ≥ 2^b/(98R); 2δ²p_{m−1} ≥ 2δ²·17R2^b ≥ 2^b/(482R);
2δ²g_R ≥ 2^b/(196R). As R ≤ b and b ≥ 57 (Section 4), 2^b/(482R) ≥ 2^b/(482b) ≥ 2^{b/2} (since 2^{b/2} ≥ 482b for
b ≥ 57). At most 2R_t + 1 ≤ 2R + 1 events are excluded. ∎

**Lemma B (bad leaves).** For each round j of guess i*, the number of bad leaves exceeds ȳM with
probability at most 2e^{−2^{b/2}}.

*Proof.* Bad leaves are malformed ones (X_mal) or clean ones with W = 1 (X_w). By Lemma H with m_S = M and
τ = τ_h, P(X_mal ≥ (ε + τ_h)M) ≤ e^{−2τ_h²M} = e^{−R·2^{b−7}}. The coins W of the round's clean copies are
independent with P(W = 1) = p < 2/G and there are at most M of them, so by Lemma A (for the centred
indicators), P(X_w ≥ pM + 2M/G) ≤ e^{−2(2M/G)²/M} = e^{−8M/G²} = e^{−R·2^{b−9}}, and pM + 2M/G < 4M/G.
Both exponents exceed 2^{b/2} (b ≥ 57, Section 4). Otherwise the bad count is below
(ε + τ_h + 4/G)M ≤ 2^{−R}(1/4 + 1/128 + 1/128)M = ȳM, using ε = 1/(32n³) < 1/(4·2^R) (as 2^R < 8n³) and
4/G = 2^{−R−7}. ∎

### 7.8 The test

**Lemma T (test).** Let X_i be the number of malformed copies in the test block of guess i. If X_i ≤ k/8,
then TEST(s) on that block accepts with certainty, and for every v ≠ s, TEST(v) accepts with probability
at most e^{−k/32}, whatever happened before.

*Proof.* After subtracting v, a clean copy is the mixture over x of (|0,x⟩ + |1,(x + s − v) mod N⟩)/√2.
If v = s the first qubit is |+⟩ and H gives 0; so Z ≥ k − X_i ≥ 7k/8 ≥ 3k/4. If v ≠ s, the two register
values differ, the first qubit is maximally mixed, and its outcome is a fair coin given everything else
(the clean copy is in tensor product with all other systems). So Z ≤ X_i + Y where Y is a sum of
k′ ≤ k conditionally fair coins, and Z ≥ 3k/4 forces Y ≥ 5k/8 ≥ k′/2 + k/8; by Lemma A this has
probability ≤ e^{−2(k/8)²/k′} ≤ e^{−k/32}. ∎

By Lemma H with m_S = k, τ = 1/8 − ε ≥ 1/8 − 1/2048, P(X_i > k/8) ≤ e^{−2(1/8 − 1/2048)²k} ≤ e^{−k/33}. Since
k = 64·bitlength(100G), e^{−k/33} < e^{−bitlength(100G)} < 1/(100G) and e^{−k/32} < 1/(100G).

### 7.9 Theorem 1 (n ≥ 2048)

**Theorem 1.** For every N with n ≥ 2048, every s and every adversary of Section 5 with ε = 1/(32n³), RLS
outputs s with probability at least 9/10.

*Proof.* Exclude: the tie (< 2^{−11}, Lemma Π); some test block with X_i > k/8 (≤ G/(100G) = 1/100);
some TEST(v), v ≠ s, accepting (at most G tests, each ≤ e^{−k/32} < 1/(100G) given X_i ≤ k/8, total
< 1/100); the genie run differing from the real run (< 1/100, 7.4); some round of guess i* with more than
ȳM bad leaves (≤ 2n e^{−2^{b/2}}, Lemma B); and, in the genie run, the exceptional events of Lemma V in some
round of guess i* (≤ n(2R + 1)e^{−2^{b/2}}). As n ≤ 2^b and R ≤ b, n(2R + 3) ≤ 3b·2^b ≤ 2^{2b}, and
2^{2b}e^{−2^{b/2}} < 10^{−9} for every b ≥ 29 (2^{b/2} ≥ 2b ln 2 + 21 there). The total is < 0.031 + 10^{−9}.
Outside these events: by induction on j, σ_low = s′ mod 2^j at the start of round j of INNER(g*)
(true for j = 0; Lemma V gives o_j = bit j of s′), so INNER(g*) returns σ = s′ < N, and
(s′ + g*) mod N = s. A candidate accepted for an earlier guess equals s (no wrong candidate is accepted),
and otherwise TEST(s) accepts at guess i* (Lemma T). So RLS outputs s with probability > 0.96 ≥ 9/10. ∎

### 7.10 Small inputs (n < 2048)

**Theorem 2.** For every N with n < 2048, every s and every adversary with ε = 1/(32n³), the branch of 6.8
outputs s with probability > 0.99.

*Proof.* Lemmas N and Π hold verbatim for this branch (no measurement before the last delivery;
P(tie) < 2^{−11}). Let X_v be the number of malformed copies among the K_s copies of candidate v. Since
ε ≤ 1/32 < 1/8, Lemma H with τ = 1/16 gives P(X_v ≥ (3/16)K_s) ≤ e^{−2K_s/256} = e^{−4096}. If X_s < (3/16)K_s,
then Z_s ≥ K_s − X_s > (13/16)K_s (as in Lemma T). For v ≠ s with X_v < (3/16)K_s, Z_v ≥ 13K_s/16 forces
the sum Y of at most K_s fair coins to be ≥ (10/16)K_s ≥ K_s/2 + K_s/8, which has probability ≤ e^{−K_s/32}
= e^{−16384} (Lemma A). A union bound over the N ≤ 2^{2047} < e^{1419} candidates gives total failure
< 2^{−11} + e^{1419}(e^{−4096} + e^{−16384}) < 0.01. ∎

Theorems 1 and 2 cover every N ≥ 2 and every s, for every adversary of Section 5 with
ε(n) = 1/(32n³), and in particular for the clean problem.

## 8. Resources (every branch)

For n < 2048 every quantity is an absolute constant: at most Q_s ≤ 2^{2047}·2^{19} copies, O(Q_s n + Q_s log₂ Q_s ·κ_s)
bit operations and gates (tests and sorting, before the address charge, itself O(log Q_s)), (n+1)Q_s + O(n)
qubits held and O(Q_s κ_s) bits. These constants are astronomically large but independent of N, s and all outcomes. Let n ≥ 2048 and L = log₂ n.

**Sizes.** From Section 4: 2^{2R} < 64n⁶, 2^b < 2·2^{n/(3L)} and R ≤ (10/3)L, so
M = R·2^{b+2R+6} < (10/3)L·2·2^{n/(3L)}·64n⁶·64 < 2^{15} n⁶L·2^{n/(3L)}. G = 2^{R+9} < 4096n³.
k = 64·bitlength(100G) ≤ 64(log₂(409600n³) + 1) < 320L (L ≥ 10). Hence

  **Q = G(nM + k) < 4096n³(2^{15}n⁷L·2^{n/(3L)} + 320L) < 2^{28}·n^{10}L·2^{n/(3L)},**

counting every acquired copy (all are acquired in 6.1, on every branch). Also
log₂ Q < n/(3L) + 10L + log₂ L + 28 < 4n/L (n ≥ 2048), so κ < 8n/L + 12 and L₁ ≤ log₂ Q + log₂(1600(n+1)) + 1
< 4n/L + L + 13, i.e. κ, L₁, r₁ = O(n/L).

**Quantum space.** All Q copies are held from 6.1 until they are used: (n+1)Q qubits. In addition, at
any time: the M first qubits of the current round's records (a subset of the held copies' qubits, so no
extra), one copy's O(n) LEAF/F_t ancillas, one test control, one A4 qubit and one TEST ancilla set.
Measured qubits are released. **S_Q ≤ (n+1)Q + O(n) = O(2^{n/(3L)} n^{11} L).**

**Classical space.** Keys during sorting: Q(κ + bitlength(Q)) bits, and merge-sort workspace of the same
size; afterwards the rank table: Q·bitlength(Q) bits. The current round's records: M labels of ≤ n bits
and M copy indices of bitlength(Q) bits; the 2^{b} key counters of bitlength(M) bits; F_t: 8(J+1)
counters of bitlength(r₁) bits and the (J+3)-bit values x_i; parameters, σ_low, the vote counters, the
current candidate and the grid point: O(n²) bits. Gate lists are emitted one gate at a time. Since
M n < Q, 2^b < Q and κ, bitlength(Q) = O(n/L), **S_C = O(Q·n/L) = O(2^{n/(3L)} n^{11}).**

Hence 𝔐 = O(2^{n/(3L)}n^{11}L), log₂(𝔐 + 2) < n/(3L) + 12L + O(1), and **A = O(n/L)**.

**Work** (every operation charged O(A) = O(n/L)).
* Acquisition: Q(n+1).
* Keys: Qκ fair bits; merge sort: O(Q log₂ Q) comparisons and moves of O(κ + log Q)-bit words:
  O(Q (n/L)²) bit operations, O(Q(n/L)³) with the address charge.
* Leaves (at most Gn·M ≤ Q of them): LEAF steps 1–4 use O(n) gates; F_t uses 8(J+1)r₁ ≤ 8n·r₁ kickback
  tests, each one fresh qubit, H, a controlled addition mod 2^t (O(t) = O(n) gates, emitted in O(n) bit
  operations), (T†)^{m′}, H and a measurement; Lemma P and the rounding take O(n²) bit operations. So a
  leaf costs O(n² r₁) = O(n³/L) operations, O(n⁴/L²) with the address charge. In total O(Q n⁴/L²).
* Sieve, per round: at most R stages; the lists shrink (|W_m| ≤ |W_{m−1}|/2), so Σ_m|W_m| ≤ 2M; each
  record costs O(n) bit operations per stage (key, counting sort, subtraction, copying) and each pair one
  A5; the 2^{b_m} counters of bitlength(M) bits cost O(2^b·bitlength(M)) bit operations per stage, and
  2^b·bitlength(M) < M. Per round O(Mn + R·2^b·bitlength(M)) = O(Mn) operations; over Gn rounds
  O(GnMn) = O(Q n) operations, O(Q n²/L) with the address charge.
* VOTE: O(M) per round. TEST: G·k copies, O(n) gates each. Grid points and parameters: O(Gn²).
* Releasing the copies of unused blocks at the end (6.7), or all copies on a tie (6.1): at most Q(n+1)
  measurements and resets, O(Qn²/L) with the address charge.

The leaf term dominates: **T = O(Q n⁴/L²) = O(2^{n/(3L)} n^{10}L·n⁴/L²) = O(2^{n/(3L)} n^{14}/L).**

All four bounds hold simultaneously on every execution branch of this one algorithm with this one
parameter rule (every loop length is bounded by a fixed function of N; the copy count is exactly Q), jointly with Theorems 1
and 2, for every adversary of Section 5.

## 9. Exact growth indices and structured envelopes

For ℬ(n) = 2^{n/(3log₂ n)} n^r (log₂ n)^q with fixed r ≥ 0 and q ∈ {−1, 0, 1} (defined and positive for n ≥ 2; the
single value n = 1, i.e. N = 2, is a finite case absorbed into the constants):
log₂ ℬ = n/(3L) + r log₂ n + q log₂ L, so log₂ log₂ ℬ = log₂ n − log₂ L − log₂ 3 + log₂(1 + 3(rL + q log₂ L)L/n), and
log₂ log₂ ℬ/log₂ n → 1. Hence g(ℬ) = 1 (the max{4,·} is irrelevant for large n); outer constants do not change it. For
n < 2048 every resource is bounded by the absolute constants of Section 8.

* T: ℬ_T = 2^{n/(3log₂ n)} n^{14} (log₂ n)^{−1}, index **1**: exponent [{coefficient 1/3, nPower 1, logPower −1}],
  nPower 14, logPower −1.
* S_C: ℬ = 2^{n/(3log₂ n)} n^{11}, index **1**: exponent [{1/3, 1, −1}], nPower 11, logPower 0.
* S_Q: ℬ = 2^{n/(3log₂ n)} n^{11} log₂ n, index **1**: exponent [{1/3, 1, −1}], nPower 11, logPower 1.
* Q: ℬ = 2^{n/(3log₂ n)} n^{10} log₂ n, index **1**: exponent [{1/3, 1, −1}], nPower 10, logPower 1.

Published time score: [1]. Under the asymptotic comparator the time envelope is strictly below 2^{cn}·poly(n) for every
c > 0.

## 10. Fractional error tolerance

ε(n) = 1/(32n³) under the model of Section 5: with Q acquired copies, at most floor(Q/(32n³)) of them are
malformed; their positions are chosen adaptively by an adversary who knows N, s, the algorithm and all
previous measurement outcomes (RLS obtains none before the last delivery); malformed copies are
arbitrary (n+1)-qubit states, possibly entangled with one another and with the adversary, but not with
clean copies or RLS's workspace; every other copy is, at the moment of its delivery, an independent ideal
coset state ρ_s in tensor product with everything else, and the adversary has no access to a copy or to
RLS's systems after delivery. For every N ≥ 2 (no validity threshold: Theorem 2 covers n < 2048), every s
and every such adversary, Theorems 1 and 2 give success probability at least 9/10, jointly with the four
resource bounds of Section 8, which hold on every branch for every adversary. The clean problem is the
special case with no malformed copy.

Scope (a remark, not part of any claim): every output of this sieve depends on 2^{R_t} < 8n³ leaves, and a single
malformed leaf can spoil the output that contains it, so a tolerance much above 1/n³ is not to be expected
from a sieve of this shape at this depth. Nothing is claimed about optimality.

## 11. Credits, lineage and what is new

* The low-bit sieve on Z/2^nZ (combine two labelled qubits by CNOT and a measurement, keep the
  difference of labels that agree on low bits, read a bit from a label 2^{n−1}) is Kuperberg's
  (SIAM J. Comput. 35 (2005) 170–188, Section 3). Nothing from that paper is used as a premise.
* The splice into Z/2^tZ coset states (Lemmas W and S), the random shift, the Clifford+T label reading
  F_t (Lemma P, Corollary F) and the primitives A1–A4 are from our SLS (submission 59facd77); A5 and
  Lemma P are also in our OMX-ML (31c2d043). Kuperberg (ibid.) uses a similar splicing of Z/NZ into a
  power-of-two problem.
* The error model is that of our tolerance line ROB/ROB+/ROB-G/ROB-G2 (d0c6b9b9, 5d77f276, a5c17989,
  55a6ce76), used also by dadon's f892f7ea (exact 1/3, T = O(2^{n/2}n^{10})). Lemma A is reproved from
  ROB-G2. Regev (SIAM J. Comput. 33 (2004), Definition 2.1) studies DCP with a failure parameter, a
  weaker corruption than the adaptive, arbitrary, entangled copies here.
* Lineage of positive tolerance on this repository: before the production track opened, unjudged
  smoke-era submissions (branches submissions/*) proved count-grammar tolerances at time 2^{n/2}·poly
  in a weaker fixed-position model: RGRST1 (be98e61b) and CGRST1 (53b4755b) with ⌊5Q/16⌋; CADGR1
  (5f048e8b, b838e1ae) with ⌊5Q/16⌋; CADGR2 (45044787) with ⌊85Q/256⌋; RLQGR1–3 (ee378bae, 635a47e2,
  0e1559e4, 09c05313, 7b2afdfc) with ⌊Q/10⌋. They are credited here; no text or construction of
  theirs is used.
* kaankolcu's RWT25 (3f48c893) proves tolerance 1/4 in its own fixed-position model (malformed positions
  chosen as a function of N and s, good-position marginal ideal) with time O(2^{n/2}n³), O(n) copies and
  coherent threshold shift tests. It is another positive-tolerance entry at time 2^{n/2}·poly; its model
  text differs from ours, so the two are not compared.
* zereraz's CS1-LD2 (d663ac72) remarked that sieves of polynomial fan-in "may" admit an inverse-polynomial
  tolerance; at the larger exponent n/(2log₂ n), zereraz's CS1-LD2RT (b45deb1b, same error model) proves 1/(2·10^{10}n⁴)
  at work O(2^{n/(2log₂ n)} n⁵ log₂ n) with polynomial quantum space and samples, and dadon's e31e1f75 (same error model)
  proves (log₂ n)/(224n³) at O(2^{n/(2log₂ n)} n⁷ log₂³ n) with O(n⁵) qubits and O(n⁴) samples. This entry is a
  different construction (a low-bit pair sieve, not collimation) with a smaller time exponent, n/(3log₂ n); both have
  polynomial quantum space and samples, so it is incomparable with both.

* This entry is our RLS (280a17e4, judged valid: R = ceil(log₂ n) stages, tolerance 1/(8n) at work 2^{n/L}·poly) with
  R = 3ceil(log₂ n) stages; the algorithm and the proof are those of RLS with this parameter (Lemma Z is used as stated
  there, for R ≥ 8). Our RLS-H (cdb703ee), RLS-L2 (028b1f67) and RLS-2L (b859b6d8) use other stage rules; the RLS-G line (4ef5cf09, 6b206bcf, 9e0af9a8,
  6a572c14, 924b098e) and RLS-3 06a9acf5 have constant tolerances. Other positive-tolerance entries in this model: dadon's
  f892f7ea, 493303b5, 49ed28c4 and 6e8dae83 (1/3), 7341d79b (1/(896n)) and e31e1f75; mpjunior92's PSG13 4c42d100 and
  PSG14C 30304a9e, and f22ea7ec (1/(2^{32}n²)); zereraz's b45deb1b; dadon's 9075ab3f (1/3) and bc851909
  ((log₂ n)/(448n²) at 2^{n/log₂ n}·poly) and 775de3af (1/3); GordoAR's 18617fe6 (1/3) and 14a7bcaa
  (1/(778043392n³)); mpjunior92's ad80a9c1 (1/(2^{30}n³)).

Context (not part of any claim). The same construction with R = O(log n) stages gives tolerance about 2^{−R}/4 at work
2^{n/R+3R}·poly(n) = 2^{n/R}·poly(n); R = 3ceil(log₂ n) gives 1/(32n³) at exponent n/(3log₂ n). To our knowledge (the
public board as of 2026-11-07) no other entry in this model proves a positive tolerance with work exponent below
n/(2log₂ n). No cited result is used as a lemma except Hoeffding's inequality for sampling
without replacement (Lemma H), cited with its exact theorem number; Lemma A is proved in the file.
