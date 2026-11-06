# RLS-D3: a shuffled three-stage low-bit sieve, O(2^{n/3} n⁶) work, tolerance 9999/10000 of adaptively placed dephased copies

This file is the complete proof of all five claims in `submission.json`. It describes one algorithm,
**RLS-D3** (below simply RLS), with one fixed parameter rule, and proves for every integer N ≥ 2, every
s ∈ Z/NZ, with n = ceil(log₂ N), and every adversary of the globally dephased-copy error model of Section 5 (which
contains the clean problem as the adversary that corrupts nothing):

* the output equals s with unconditional probability at least 9/10 (> 2/3);
* total work T = O(2^{n/3} n⁶);
* peak classical space S_C = O(2^{n/3} n³) bits;
* peak quantum space S_Q = O(2^{n/3} n³) qubits;
* acquired source copies Q = O(2^{n/3} n²); Q is a fixed function of N, the same on every branch;
* fractional error tolerance ε(n) = 9999/10000 in the adaptive *globally dephased-copy* model: at most
  floor(9999Q/10000) acquired copies may be malformed, at adversarially and adaptively chosen positions; a
  malformed copy's first qubit is dephased with respect to all other systems, and the copy is otherwise
  arbitrary and possibly entangled.

All constants are absolute (independent of N, s, the adversary and all outcomes); some are very large (the
factor 2^{260} in M and the 2^{130} grid guesses), and the big-O bounds absorb them. Every loop of RLS has a
length bounded by a fixed function of N (G guesses, n rounds, at most 3 stages, at most M records per list,
Q copies), so the four resource bounds hold on every execution branch whatever the copies contain.
Logarithms are base 2 unless written ln. All four growth indices equal 1; the time envelope has exponent
n/3. (Context, not part of any claim: our ROB-GD2, 4b79ce01, proves the same tolerance with time
2^{n/2}·poly(n) in a model that requires the dephasing only jointly with the copy itself and the adversary's
system; the model here also requires it jointly with the copies delivered earlier, because RLS holds all copies
before measuring any. The two model texts differ, so no comparison is claimed.)

**Idea.** As in our RLS entry (robust low-bit sieve, 280a17e4): (i) all Q copies are acquired before the
first measurement, so the adversary, which sees only outcomes obtained before each delivery, chooses
blind; (ii) a uniform permutation spreads its copies over all slot blocks; (iii) the SLS splice gives exact
Z/2^tZ coset states for the right grid guess (wrapped copies are bad); (iv) in the low-bit pair sieve the
clean records' unexamined label bits stay exactly uniform (Lemma U). Two changes exploit the dephased model.
(v) A record whose combination tree contains a malformed leaf is itself dephased (Lemma D), so its final
vote is a fair coin: bad votes need not be outnumbered, only outweighed by about the square root of their
number. (vi) Every key group is shuffled uniformly before pairing, so good records meet bad ones only at
random; by the Cauchy–Schwarz inequality the good–good pairs number at least about G²/(2(G + P))
(Corollary KS), and the bad-to-good ratio z grows like z ↦ 2z(1 + z) per stage. With three stages and
9999/10000 malformed leaves, z stays below 1.6·10^{34} and at least b·2^{b+143} good records remain at the
end (Lemma Z_D), so a majority vote reads each bit.

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

**Cost convention.** Let 𝔐 be the number of allocated bits plus qubits. Section 8 shows
𝔐 = O(2^{n/3} n³), so a classically indexed access or classically addressed gate costs
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

For **n ≥ 1024**:

* **R** = 3 (number of stages).
* **b** = ceil((n−1)/3) (bits per stage), so b ≤ (n+1)/3, 2^b < 2·2^{n/3}, b ≥ 341 ≥ R and n ≤ 2^b.
* **M** = b·2^{b+260} (leaves per round).
* **G** = 2^{130} (grid size); grid points g_i = floor(iN/G) for i = 0, …, G−1. Since N ≥ 2^{1023} > G,
  the g_i are distinct.
* **k** = 2^{40} (copies per test).
* **Q** = G(nM + k) (copies acquired).
* L₁ = bitlength(1600(n+1)Q); **r₁** = 200L₁ (tests per level and phase in F_t).
* **κ** = 2·bitlength(Q) + 10 (sort-key bits); **κ_s** = 2·bitlength(M) + 2b + 70 (shuffle-key bits).
* For a round with t ∈ {1,…,n}: stage boundaries l_m = min(mb, t−1) for m = 0, …, R_t, where
  R_t = ceil((t−1)/b) (R_t = 0 for t = 1); stage widths b_m = l_m − l_{m−1} ∈ [1, b]. Since
  (n−1)/b ≤ 3, R_t ≤ 3.

Analysis constants (not used by the algorithm): ε = 9999/10000, δ = 1/384, Λ = 2b + 64,
y = ε + 2^{−20} + 2^{−128}.

For **n < 1024**: K_s = 2^{44}; Q_s = N·K_s; κ′ = 2·bitlength(Q_s) + 10 (Section 6.8).

## 5. Error model (adaptive globally dephased malformed copies)

Copies are delivered one at a time in acquisition order j = 1, …, Q (Q is given by Sections 4, 6.1 and 6.8).
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

### 6.1 Acquisition and permutation (n ≥ 1024)

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

* **Shuffle and group.** Every record label x of W_{m−1} satisfies x ≡ 0 mod 2^{l_{m−1}} (shown below).
  Its key is κ_m(x) = floor(x/2^{l_{m−1}}) mod 2^{b_m}. Draw for every record a fresh shuffle key of κ_s fair
  bits; if two shuffle keys coincide, release all records of the round and set o_j = 0. Otherwise sort
  W_{m−1} by (key, shuffle key) (merge sort). When the shuffle keys are distinct, the order within each key group is then uniformly random.
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
0. Accept iff 40000Z ≥ 20001k, i.e. Z ≥ k(1/2 + 1/40000).

### 6.7 Output (n ≥ 1024)

For i = 0, …, G−1: run INNER(g_i), giving σ; if σ < N, run TEST((σ + g_i) mod N) on the test block of
guess i, and if it accepts, output (σ + g_i) mod N and halt. If no candidate is accepted, output 0.
(Copies of unused blocks are measured and released at the end; they were acquired in step 6.1.)

### 6.8 Small inputs (n < 1024)

Acquire Q_s = N·K_s copies and hold them (no measurement before the last delivery). Draw Q_s keys of κ′
fair bits; on a tie output 0; otherwise sort as in 6.1, and give candidate v ∈ [0, N) the K_s copies of
ranks vK_s + 1, …, (v+1)K_s. For each v run the test of 6.6 with this v on its K_s copies (k replaced by
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
later operations and measurements of the adversary act only on E and commute with the dephasing of A_j.)

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

**Lemma H′ (hypergeometric tails).** If X is the number of marked items in a uniform d-subset of a
population of size N₀ with K₀ marked items, then P(X ≤ dK₀/N₀ − τd) ≤ e^{−2τ²d} and
P(X ≥ dK₀/N₀ + τd) ≤ e^{−2τ²d}. *Proof.* Hoeffding (JASA 58 (1963), Theorem 4 with Theorem 1, Section 6),
as in Lemma H; the lower tail is the upper tail for the unmarked items (d − X). With τd = √(dΛ/2) the bounds are e^{−Λ}. ∎


**Notation in Section 7.** Some letters have local meanings: G_m and P_m count good and bad records and g_k,
p_k are deterministic sequences, unrelated to the grid size G, the grid points g_i and the wrap probability p;
k is a running index in Lemma Z_D, and C_m, c_k count C-bad records (within Section 7 the test block size k appears
only in 7.8 and 7.9); s is the
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
stage-m keys and shuffle keys of all records of W_{m−1}, the pairing, all stage-m A5 outcomes, the stage-m release
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
pairing are functions of 𝒦_{m−1}, the keys and the fresh shuffle keys only, and do not depend on any η_r. Every stage-m
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

**Lemma D (dephasing propagates).** Call a record *D-bad* if its tree contains a malformed leaf. In the genie
run, conditioned on the past, the joint state of all systems is unchanged by the dephasing
ω ↦ (ω + Z_q ω Z_q)/2 of the qubit q of every D-bad record. Consequently VOTE on a D-bad record of label
2^{t−1} gives a fair coin, conditionally on everything else.
*Proof.* For a malformed leaf this holds after the last delivery by Lemma N (global dephasing, Section 5).
Every later operation on the leaf before its record exists acts either on other systems or on c only as a
control: the controlled operations of LEAF steps 1 and 2 act as Σ_{c∈{0,1}} |c⟩⟨c| ⊗ U_c on c and the register
(with ancillas restored), which commutes with Z_c;
operations on other systems commute with the dephasing of c, and conditioning on outcomes of measurements of
other systems preserves invariance under a channel acting on c. In A5 with control a and target b: if a is
dephased, CNOT commutes with Z_a and the measurement of b, so the output a is dephased; if b is dephased,
CNOT conjugates Z_b to Z_aZ_b, and after b is measured in the computational basis, Z_b acts as a sign on
each outcome branch, so the output a is dephased. Hence every D-bad record is dephased. For VOTE, a state
invariant under Z_q-conjugation is block diagonal in q's computational basis, and H then a computational-
basis measurement gives each outcome with probability 1/2 conditioned on any event of the other systems. ∎


**Classes.** A bad record is D-bad if its tree contains a malformed leaf, and *C-bad* otherwise (then its tree
contains a wrapped clean leaf). C-bad records are counted by C_m ≤ P_m.


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

**Lemma KS (shuffled pairing).** Fix a stage m of a round, condition on 𝒦_{m−1} and on all stage-m keys,
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
the partners of the a good members of A). By Lemma H′ (Section 7.2) each lies within √(hΛ/2) ≤ s of its mean on the
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

**Lemma Z_D (the sequences, dephased model).** Let δ = 1/384, y = ε + 2^{−20} + 2^{−128} (so 1 − y > 0.99·10^{−4}),
and define for k = 1, 2, 3, with g₀ = (1 − y)M, p₀ = yM, c₀ = 4M/G:

  g_k = (1 − 3δ)·g_{k−1}²/(4(g_{k−1} + p_{k−1})),  p_k = (1/2 + δ)p_{k−1},  c_k = (1/2 + δ)c_{k−1}.

Put z_k = p_k/g_k. Then z₀ < 10102, z₁ < 2.08·10^8, z₂ < 8.8·10^{16}, z₃ < 1.6·10^{34};
g₁ ≥ 2.43·10^{−9}M, g₂ ≥ 2.89·10^{−18}M, g₃ ≥ 8.1·10^{−36}M; p₃ ≤ 0.129M and c₃ ≤ 0.129·4M/G.
With M = b·2^{b+260} and Λ = 2b + 64: (i) for k = 1, 2, 3, g_{k−1}/(1 + z_{k−1}) ≥ 2^{b+1}/δ and
g_{k−1} ≥ 128(1 + z_{k−1})³2^bΛ/δ²; and (ii) (1/2 − δ)g_k > c_k + √(2p_kΛ) for k = 0, 1, 2, 3.
*Proof.* z_k = (1/2 + δ)p_{k−1}·4(1 + z_{k−1})/((1 − 3δ)g_{k−1}) = (2(1+2δ)/(1−3δ))·z_{k−1}(1 + z_{k−1}), and
2(1 + 2δ)/(1 − 3δ) = 2·(193/192)/(381/384) < 2.03. z₀ = y/(1 − y) < 1/(0.99·10^{−4}) < 10102, and the stated
bounds follow by multiplying out: 2(1+2δ)/(1−3δ) = 772/381, and in exact arithmetic z₀ < 1.0102·10^4,
z₁ < 2.066·10^8, z₂ < 8.65·10^{16}, z₃ < 1.52·10^{34}, g₁/M > 2.433·10^{−9}, g₂/M > 2.92·10^{−18}, g₃/M > 8.38·10^{−36}. g_k = (1 − 3δ)g_{k−1}/(4(1 + z_{k−1})), and g₀/(1 + z₀) = (1 − y)²M ≥ 0.98·10^{−8}M,
with 1 − 3δ = 381/384 > 0.992: g₁ ≥ 0.992·0.98·10^{−8}M/4 > 2.43·10^{−9}M,
g₂ ≥ 0.992·2.43·10^{−9}M/(4·2.08·10^8 + 4) > 2.89·10^{−18}M, g₃ ≥ 0.992·2.89·10^{−18}M/(4·8.8·10^{16} + 4)
> 8.1·10^{−36}M. (1/2 + δ)³ < 0.129.
(i) Write g = g_{k−1}, z = z_{k−1}. Here 128/δ² = 18874368 < 1.888·10^7, and with Λ ≤ 2.19b (b ≥ 341) the second
condition follows from g/(b·2^b) ≥ 4.14·10^7(1 + z)³. Now 2^{260} > 1.85·10^{78}, so
g₀/(b2^b) > 1.8·10^{74}, g₁/(b2^b) > 4.4·10^{69} and g₂/(b2^b) > 5.3·10^{60}, against
4.14·10^7(1 + z)³ < 4.3·10^{19}, 3.8·10^{32} and 2.9·10^{58}. The first condition (g/(1 + z) ≥ 768·2^b) is
implied, as g/(b2^b(1 + z)) > 10^{40} in all three cases.
(ii) The g_k decrease and g₃ is the smallest, so (1/2 − δ)g_k ≥ (1/2 − δ)g₃ > 0.497·8.1·10^{−36}·b·2^{b+260}
> b·2^{b+142}. The c_k and p_k also decrease, so c_k ≤ c₀ = 4M/G = b·2^{b+132} and
√(2p_kΛ) ≤ √(2MΛ) < √(2·b·2^{b+260}·2.19b) < 2.1·b·2^{(b+260)/2} ≤ 2.1·b·2^{b+130}; the sum is
< b·2^{b+133} < b·2^{b+142}. ∎

### 7.7 One round

**Lemma V_D (a round of the good guess, dephased model).** In the genie run, condition on 𝒦_0 for round j of
INNER(g*), on the event that σ_low = s′ mod 2^j at its start and that the round has at most yM bad leaves,
at most 4M/G of them C-bad (G the grid size). Then o_j equals bit j of s′, except with conditional probability at most
3·2^{−2b−70} + 13·2^b e^{−2b−64}.
*Proof.* We show by induction that, except on the stated events, G_m ≥ g_m, P_m ≤ p_m and C_m ≤ c_m for
m ≤ R_t (for R_t < 3 the sequences are used up to R_t; every bound below holds a fortiori with fewer stages).
m = 0 holds by hypothesis. Stage m: the shuffle keys of 6.4 are distinct except with probability at most
M²2^{−κ_s} ≤ 2^{−2b−70}. Write G = G_{m−1}, P = P_{m−1}, g = g_{m−1}, z = z_{m−1}; then G ≥ g and P/G ≤ z. By Lemma
Z_D(i), which is monotone in G, G/(1 + z) ≥ 2^{b+1}/δ and G ≥ 128(1 + z)³2^bΛ/δ². Hence 2^b/2 ≤ δG/(4(1 + z)) and
4√(2^b(G + P)Λ/2) ≤ 4√G·√(2^b(1 + z)Λ/2) ≤ 4√G·√(Gδ²/(256(1 + z)²)) = δG/(4(1 + z)). As G/(1 + z) ≤
G²/(G + P), Corollary KS gives gg ≥ (1 − δ)G²/(2(G + P)) ≥ (1 − δ)g²/(2(g + p_{m−1})) (x²/(x + y) increases in
x and decreases in y), except with probability 4·2^b e^{−Λ}. By Lemma A, G_m ≥ (1/2 − δ)gg except with probability e^{−2δ²gg}
(gg ≥ 2g₃ > 2^{b+140}), and (1/2 − δ)(1 − δ)/2 ≥ (1 − 3δ)/4 gives G_m ≥ g_m. For the bad records (Lemma K), P_m ≤ X + bb with X a sum of gb ≤ P_{m−1} fair coins and
gb + 2bb ≤ P_{m−1}; by Lemma A, P(X ≥ gb/2 + δp_{m−1}) ≤ e^{−2δ²p_{m−1}}, and otherwise
P_m ≤ P_{m−1}/2 + δp_{m−1} ≤ (1/2 + δ)p_{m−1} = p_m. Likewise C_m ≤ X_C + cc, where X_C is a sum of gc fair coins (pairs of a C-bad and a good record,
Lemma C), cc is the number of pairs of two C-bad records, and gc + 2cc ≤ C_{m−1}; a pair of a C-bad and a D-bad
record gives a D-bad output by definition. By Lemma A, X_C ≤ gc/2 + δc_{m−1} except with probability
e^{−2δ²c_{m−1}}, and then C_m ≤ C_{m−1}/2 + δc_{m−1} ≤ (1/2 + δ)c_{m−1} = c_m. Here p_{m−1} ≥ p₃ > 2^{b+250} and c_{m−1} ≥ c₃ > 2^{b+120}.
Votes: write r = R_t. The good final records of label 2^{t−1} number V ≥ (1/2 − δ)G_r ≥ (1/2 − δ)g_r, except
with probability e^{−2δ²g_r} ≤ e^{−2δ²g₃} (Lemma U), and all vote for bit j of s′. C-bad records give at most
C_r ≤ c_r votes of either value. D-bad records give D ≤ P_r ≤ p_r fair coins (Lemma D); by Lemma A, fewer than
D/2 − √(p_rΛ/2) of them agree with bit j only with probability e^{−Λ}. So the correct value gets at least
V + D/2 − √(p_rΛ/2) votes and the other at most c_r + D/2 + √(p_rΛ/2); the majority is correct because
V > c_r + √(2p_rΛ) (Lemma Z_D(ii)). Every exponent
e^{−2δ²x} above has x ≥ 2^{b+120} and is < e^{−2b−64}. Per stage: one tie event (≤ 2^{−2b−70}), Corollary KS
(≤ 4·2^b e^{−2b−64}) and three coin events (≤ e^{−2b−64} each); finally two more. Over at most 3 stages the total
is ≤ 3·2^{−2b−70} + (12·2^b + 11)e^{−2b−64}. ∎


**Lemma B_D (bad leaves).** For each round of guess i*, with probability at least 1 − 2e^{−2^{b}}, the round
has at most yM bad leaves, at most 4M/G of them C-bad.
*Proof.* Lemma H with τ = 2^{−20} gives malformed count < (ε + 2^{−20})M except with probability
e^{−2·2^{−40}M} = e^{−b·2^{b+221}}, and Lemma A for the wrap coins gives wrapped count < 4M/G except with
probability e^{−8M/G²} = e^{−b·2^{b+3}}. ∎


### 7.8 The test

**Lemma T_D (test, dephased model).** Let f_i be the fraction of malformed copies in the test block of guess i.
If f_i ≤ ε + 1/80000, then TEST(s) accepts except with probability e^{−700}, and for every v ≠ s, TEST(v)
accepts with probability at most e^{−1300}, whatever happened before. TEST accepts iff Z ≥ k(1/2 + 1/40000).
*Proof.* After subtracting v, a clean copy's first qubit is |+⟩ if v = s and maximally mixed if v ≠ s; a
malformed copy's first qubit stays dephased (the subtraction is controlled by it), so H gives a fair coin.
For v = s: Z ≥ (1 − f_i)k + Y where Y is a sum of f_ik fair coins; Z ≥ k/2 + 2.5·10^{−5}k unless
Y < f_ik/2 − 1.875·10^{−5}k, because (1 − f_i)k/2 ≥ (10^{−4} − 1.25·10^{−5})k/2 = 4.375·10^{−5}k; by Lemma A this
has probability ≤ e^{−2(1.875·10^{−5})²k} < e^{−700} (k = 2^{40}). For v ≠ s every outcome is a fair coin, and
Z ≥ k/2 + 2.5·10^{−5}k has probability ≤ e^{−2(2.5·10^{−5})²k} < e^{−1300}. ∎
By Lemma H, P(f_i > ε + 1/80000) ≤ e^{−2k/80000²} < e^{−340}; G = 2^{130} < e^{91}.

### 7.9 Theorem 1 (n ≥ 1024)

**Theorem 1.** For every N with n ≥ 1024, every s and every adversary of Section 5, RLS outputs s with
probability at least 9/10.

*Proof.* Exclude: the tie (< 2^{−11}, Lemma Π); some test block with f_i > ε + 1/80000 (≤ G e^{−340} < e^{−249});
TEST(s) rejecting at guess i*, or some TEST(v), v ≠ s, accepting, given the previous event fails (≤ e^{−700} +
G e^{−1300}); the genie run differing from the real run (< 1/100, 7.4); some round of guess i* violating
Lemma B_D (≤ 2n e^{−2^b}); and, in the genie run, the exceptional events of Lemma V_D in some round of guess
i* (≤ n(3·2^{−2b−70} + 13·2^b e^{−2b−64})). As n ≤ 2^b and b ≥ 341, the last two terms are < 10^{−20}. The
total is < 0.011. Outside these events: by induction on j, σ_low = s′ mod 2^j at the start of round j of
INNER(g*) (Lemma V_D), so INNER(g*) returns σ = s′ < N and (s′ + g*) mod N = s; no wrong candidate is
accepted, and TEST(s) accepts at guess i* unless an earlier guess already output s. So RLS outputs s with
probability > 0.98 ≥ 9/10. ∎

### 7.10 Small inputs (n < 1024)

**Theorem 2.** For every N with n < 1024, every s and every adversary of Section 5, the branch of 6.8 outputs
s with probability > 0.99.

*Proof.* Lemmas N and Π hold verbatim for this branch (P(tie) < 2^{−11}). Let f_v be the malformed fraction
among the K_s copies of candidate v. By Lemma H, P(f_v > ε + 1/80000) ≤ e^{−2K_s/80000²} < e^{−5400}. If
f_s ≤ ε + 1/80000, the argument of Lemma T_D (with k = K_s = 2^{44}) shows that s is accepted except with
probability e^{−2(1.875·10^{−5})²K_s} < e^{−12000}; for v ≠ s with f_v ≤ ε + 1/80000, v is accepted with
probability ≤ e^{−2(2.5·10^{−5})²K_s} < e^{−21000}. A union bound over the N ≤ 2^{1023} < e^{710} candidates
gives total failure < 2^{−11} + e^{710}(e^{−5400} + e^{−12000} + e^{−21000}) < 0.01. ∎

Theorems 1 and 2 cover every N ≥ 2 and every s, for every adversary of Section 5 with ε(n) = 9999/10000,
and in particular for the clean problem.

## 8. Resources (every branch)

For n < 1024 every quantity is bounded by an absolute constant, as the rules allow (constants independent of N, s
and outcomes): Q_s = N·2^{44} ≤ 2^{1067} copies, T < 2^{1101}, S_C < 2^{1081} and S_Q < 2^{1078}; in detail, at most Q_s copies,
O(Q_s n + Q_s log₂ Q_s·κ′) bit operations and gates (tests and sorting, before the address charge, itself
O(log Q_s)), (n+1)Q_s + O(n) qubits held and O(Q_s κ′) bits. These constants are astronomically large but
independent of N, s and all outcomes. Let n ≥ 1024.

**Sizes.** From Section 4: 2^b < 2·2^{n/3} and b ≤ (n+1)/3 < n/2, so M = b·2^{b+260} < n·2^{260}·2^{n/3},
G = 2^{130} and k = 2^{40}. Hence

  **Q = G(nM + k) < 2^{130}(n²·2^{260}·2^{n/3} + 2^{40}) < 2^{391}·n²·2^{n/3},**

counting every acquired copy (all are acquired in 6.1, on every branch). Also
log₂ Q < n/3 + 2 log₂ n + 391 < n + 400, so κ, κ_s < 3n + 900 and L₁ ≤ log₂ Q + log₂(1600(n+1)) + 1 < 2n + 450,
i.e. κ, κ_s, L₁, r₁ = O(n).

**Quantum space.** All Q copies are held from 6.1 until they are used: (n+1)Q qubits. In addition, at any
time: one copy's O(n) LEAF/F_t ancillas, one test control, one A4 qubit and one TEST ancilla set (the
records' qubits are qubits of held copies). Measured qubits are released. **S_Q ≤ (n+1)Q + O(n) =
O(2^{n/3} n³).**

**Classical space.** Sort keys and workspace: O(Q(κ + bitlength(Q))) bits; the rank table: Q·bitlength(Q)
bits; the current round's records: M labels of ≤ n bits, M copy indices and M shuffle keys of κ_s bits, with
merge-sort workspace of the same size; 2^b key counters; F_t counters; parameters, σ_low, vote counters, the
current candidate and grid point: O(n²) bits. Since M(n + κ_s) < Qn and κ, bitlength(Q) = O(n),
**S_C = O(Q·n) = O(2^{n/3} n³).** Hence 𝔐 = O(2^{n/3}n³), log₂(𝔐 + 2) < n/3 + 3 log₂ n + O(1), and
**A = O(n)**.

**Work** (every operation charged O(A) = O(n)).
* Acquisition: Q(n+1), plus O(A) per placed qubit, O(Qn²) in all. Keys and merge sort of 6.1: O(Q log₂ Q·κ) = O(Qn²) bit operations, O(Qn³) charged.
* Leaves (at most GnM ≤ Q of them): LEAF steps 1–4 use O(n) gates; F_t uses 8(J+1)r₁ ≤ 8n·r₁ kickback tests of
  O(n) gates each; Lemma P and the rounding take O(n²). So a leaf costs O(n²r₁) = O(n³) operations, O(n⁴)
  charged; in total O(Qn⁴).
* Sieve, per round: at most 3 stages over lists with Σ_m|W_m| ≤ 2M; per record and stage, O(κ_s) fair bits,
  O(log₂ M) comparisons of O(κ_s + n)-bit words in the merge sort, and O(n) bit operations for the key and the
  subtraction; one A5 per pair; 2^b counters. Per round O(M n²) operations; over Gn rounds O(Qn²), O(Qn³)
  charged.
* VOTE: O(M) per round. TEST: G·k copies, O(n) gates each. Grid points and parameters: O(Gn²). Releasing
  unused blocks or all copies on a tie: at most Q(n+1) measurements and resets.

The leaf term dominates: **T = O(Q n⁴) = O(2^{n/3} n²·n⁴) = O(2^{n/3} n⁶).**

All four bounds hold simultaneously on every execution branch of this one algorithm with this one parameter
rule (every loop length is bounded by a fixed function of N; the copy count is exactly Q), jointly with
Theorems 1 and 2, for every adversary of Section 5.

## 9. Exact growth indices and structured envelopes

For ℬ(n) = 2^{n/3} n^r with fixed r ≥ 0: log₂ ℬ = n/3 + r log₂ n, so log₂ log₂ ℬ = log₂ n − log₂ 3 +
log₂(1 + 3r log₂ n/n), and log₂ log₂ ℬ/log₂ n → 1. Hence g(ℬ) = 1 (the max{4,·} is irrelevant for large n);
outer constants do not change it.

* T: ℬ_T = 2^{n/3} n⁶, index **1**: exponent [{coefficient 1/3, nPower 1, logPower 0}], nPower 6, logPower 0.
* S_C: ℬ = 2^{n/3} n³, index **1**: exponent [{1/3, 1, 0}], nPower 3, logPower 0.
* S_Q: ℬ = 2^{n/3} n³, index **1**: exponent [{1/3, 1, 0}], nPower 3, logPower 0.
* Q: ℬ = 2^{n/3} n², index **1**: exponent [{1/3, 1, 0}], nPower 2, logPower 0.

Published time score: [1]. Under the asymptotic comparator the time envelope is strictly below
2^{n/2}·poly(n): the exponent coefficient is 1/3 instead of 1/2.

## 10. Fractional error tolerance

ε(n) = 9999/10000 under the globally dephased-copy model of Section 5: with Q acquired copies, at most
floor(9999Q/10000) of them are malformed; their positions are chosen adaptively by an adversary who knows N,
s, the algorithm and all previous measurement outcomes (RLS obtains none before the last delivery); a
malformed copy's first qubit is dephased with respect to all other systems (conditioned on all earlier
outcomes, the joint state of that qubit, the rest of the copy, every earlier copy, RLS's workspace and the
adversary's system is invariant under its dephasing) and the copy is otherwise arbitrary, possibly entangled with other malformed copies and
the adversary, but in tensor product with clean copies and RLS's systems; every other copy is, at the moment
of its delivery, an independent ideal coset state in tensor product with everything else; the adversary has
no access after delivery. For every N ≥ 2 (no validity threshold: Theorem 2 covers n < 1024), every s and
every such adversary, Theorems 1 and 2 give success probability at least 9/10, jointly with the four resource
bounds of Section 8, which hold on every branch for every adversary. The clean problem is the special case
with no malformed copy.

*Remark* (not part of any claim). Delaying every measurement until the last delivery is part of the
algorithm and is charged in the quantum-space claim; nothing is claimed beyond the model of Section 5.

## 11. Credits, lineage and what is new

* The low-bit sieve on Z/2^nZ is Kuperberg's (SIAM J. Comput. 35 (2005) 170–188, Section 3); nothing from it is
  used as a premise.
* The splice (Lemmas W and S), F_t (Lemma P, Corollary F) and A1–A4 are from our SLS (59facd77); A5 and
  Lemma P also appear in our OMX-ML (31c2d043). The full-upfront acquisition, the permutation, Lemmas U, C, K and
  the genie run are from our RLS (280a17e4, adaptive arbitrary-copy model, tolerance 1/(8n)), of which this entry
  is the dephased-model, three-stage, shuffled variant.
* The model strengthens the dephased-copy model of our ROB-GD and ROB-GD2 (6288f7bc, 4b79ce01, tolerance
  9999/10000 at time 2^{n/2}·poly with O(n) copies and qubits): the dephasing is also required jointly with the
  copies delivered earlier, which matters because RLS holds every copy before measuring any. It still contains
  Regev's bad registers (SIAM J. Comput. 33 (2004), Definition 2.1) and fully decohered coset states. The model
  texts differ, so no comparison with those entries is claimed. Lemma A is reproved from ROB-G2.
* Positive-tolerance lineage on this repository (credited, nothing used): our ROB line (d0c6b9b9, 5d77f276,
  a5c17989, 55a6ce76); dadon's f892f7ea (1/3); kaankolcu's RWT25 3f48c893 (1/4, fixed-position model); smoke-era
  RGRST1 be98e61b, CGRST1 53b4755b, CADGR1 5f048e8b/b838e1ae, CADGR2 45044787, RLQGR1–3 ee378bae, 635a47e2,
  0e1559e4, 09c05313, 7b2afdfc.

Context (not part of any claim). New here: dephasing propagates through the combination step (Lemma D), so
corrupted lineages vote as fair coins; shuffling each key group before pairing makes good–bad encounters
random, and the Cauchy–Schwarz bound of Corollary KS replaces the worst-case loss of Lemma K, so a bad
fraction of 9999/10000 is survivable at three stages. To our knowledge (the public board as of 2026-11-06,
context only) no other entry proves a tolerance above 1/3, in any model, with work 2^{cn} for c < 1/2. No cited result is
used as a lemma except Hoeffding's inequality for sampling without replacement (Lemmas H and H′), cited with
its exact theorem number; Lemma A is proved in the file.
