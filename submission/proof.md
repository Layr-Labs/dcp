# Log-depth interval sieve with a 1/(65536 n^5) malformed-copy tolerance

All logarithms are base 2. N ≥ 2, s ∈ Z/NZ, n = ⌈log N⌉, so 2^{n−1} < N ≤ 2^n.
One algorithm, called **LSIEVE**, with the parameters fixed below, is used for all
five claims. It is the interval sieve of our earlier submission ISIEVE
(bb9fd8ac-073b-4224-87cb-773e841df5eb; a Kuperberg-type collimation sieve, G. Kuperberg,
SIAM J. Comput. 35(1):170–188, 2005) with three changes: (i) the sieve depth is
logarithmic, K = ⌈log n⌉ stages of ⌈n/K⌉ bucket bits, so that every final phase
qubit descends from at most 2^K < 2n source copies; (ii) every decision votes with
*all* of its final qubits, whose number Λ is large compared with the number of
malformed copies the error model allows; (iii) the copy schedule is fixed: every
execution acquires exactly Q_fix copies, in 2n+6 slots of P copies. Everything is
proved below; no statement of the cited papers is used.

## 0. Algorithm and parameters

**Small n.** If n < 32, LSIEVE runs the exhaustive shift test of the baseline: for
t = 0,…,N−1, n+2 X-tests of t (defined below), each on a fresh copy; all N(n+2) tests are
run, and the smallest t all of whose tests give + is output (0 if there is none). It acquires exactly Q = N(n+2) copies and succeeds with
probability > 3/4 on clean copies (a wrong t survives n+2 tests with probability
2^{−n−2}; union bound (N−1)2^{−n−2} < 1/4; the right t always survives).

**X-test of a candidate t.** On a copy (registers q, R) apply controlled (by q)
subtraction of t mod N to R (an exact reversible circuit of O(n) gates on the valid
range, identity on y ≥ N), then H on q and measure q; outcome 0 is "+". On a clean
copy ρ_s = N^{−1}Σ_x |ψ_x⟩⟨ψ_x|, |ψ_x⟩ = (|0,x⟩ + |1,x+s⟩)/√2, the state becomes
(|0,x⟩ + |1,x+s−t⟩)/√2: if t = s it is |+⟩|x⟩ and "+" is certain; if t ≠ s the two
branches are orthogonal and "+" has probability exactly 1/2. Measuring R afterwards
and resetting it (X on each 1) frees the registers. Cost O(n²) bit operations.

**Parameters for n ≥ 32** (computed by the controller from n with O(n²) bit
operations):

| symbol | value |
| --- | --- |
| K | ⌈log n⌉ (maximum number of sieve stages) |
| ℓ | ⌈n/K⌉ (maximum bucket bits per stage); B := 2^ℓ |
| Λ | 2^{20}·B (number of final items of every sieve run) |
| P | 4·16^K·Λ (copies per slot) |
| Q_fix | (2n+6)·P (copies acquired by every execution) |
| t | ⌈log Q_fix⌉ + 10 (precision bits) |
| μ | n + t + 2 (phase-estimation bits); gradient size b := μ |

**Copy schedule.** Copies are acquired in 2n+6 consecutive *slots* of exactly P
copies: decision slots 1,…,2n+5 and the final slot. Decision number k (k ≥ 1) uses
slot k. A copy that a slot does not use, every copy of a decision slot left unused
when the main loop ends early, and every copy acquired after an abort is acquired
and immediately *discarded*: all its n+1 qubits are measured and reset (O(n)
operations). Hence on every branch exactly Q_fix copies are acquired.

**Main loop (n ≥ 32).** Prepare once the phase-gradient register G_b (§2).
Maintain a *cyclic interval* (a, W): integers 0 ≤ a < N, 1 ≤ W ≤ N, with the
invariant s ≡ a + u (mod N) for some integer 0 ≤ u < W. Start a = 0, W = N.

1. Step 0: one decision with labels e = 1, update rule (i) of §5.
2. Steps 1–4: four decisions with e = 1, D = N/32, update rule (ii) of §5.
3. While W ≥ 3: one decision with e = e(W) := max{e : 2^{e+1}W ≤ N} and
   D = W/8, update rule (ii) of §5.
4. Discard the copies of the unused decision slots.
5. Final slot (W ≤ 2): if W = 1, discard the P copies and output a. If W = 2, run
   the X-test of the candidate a on each of the P copies; output a if at least
   3P/4 of them give +, else a+1 mod N.

Each decision first runs one **sieve run** SIEVE(e) (§4) on the first 4L_0 copies of
its slot (L_0 ≤ 16^KΛ, so 4L_0 ≤ P), producing exactly Λ phase qubits with labels in
{−2^{e−1}+1, …, 2^{e−1}}, then the selection and vote of §5 (all selected items vote). **Abort rule:**
whenever a count required below is not met, LSIEVE records "abort", discards all
remaining copies of the schedule, outputs 0 and halts; this is a failure branch
counted in §6. There are at most 2n+5 decisions on every branch (§5), so the slot
schedule is well defined and the resource bounds of §7 hold on every branch.

## 1. Phase qubits

For an integer label λ write |φ_λ⟩ = (|0⟩ + e^{2πiλs/N}|1⟩)/√2; it depends only on
λ mod N, and the controller stores λ as a signed integer with |λ| < N ≤ 2^n.

**Lemma 1 (combination).** Let two qubits be in |φ_α⟩⊗|φ_β⟩. Apply CNOT (control
first, target second) and measure the second qubit. Each outcome has probability
exactly 1/2, independently of α, β and of all other registers; outcome 1 leaves
the first qubit in |φ_{α−β}⟩, outcome 0 in |φ_{α+β}⟩.

*Proof.* With θ = 2πs/N the state is ½(|00⟩ + e^{iθα}|10⟩ + e^{iθβ}|01⟩ + e^{iθ(α+β)}|11⟩).
CNOT gives ½(|00⟩ + e^{iθα}|11⟩ + e^{iθβ}|01⟩ + e^{iθ(α+β)}|10⟩). Outcome 0 has
branch ½(|0⟩ + e^{iθ(α+β)}|1⟩)|0⟩ and outcome 1 has ½e^{iθβ}(|0⟩ + e^{iθ(α−β)}|1⟩)|1⟩,
each of squared norm 1/2. ∎

**Lemma 2 (sign and Y-measurement).** X|φ_λ⟩ equals |φ_{−λ}⟩ up to a global phase.
Writing |φ⟩ = (|0⟩ + e^{2πiψ}|1⟩)/√2 for real ψ, measuring after S† and H gives
outcome 0 ("+") with probability (1 + sin 2πψ)/2.

*Proof.* X|φ_λ⟩ = e^{iθλ}(|0⟩ + e^{−iθλ}|1⟩)/√2. After S† the relative phase is
α = 2πψ − π/2, and H then yields 0 with probability |1+e^{iα}|²/4 = (1+cos α)/2 =
(1 + sin 2πψ)/2. ∎

## 2. Phase-gradient register

Let |G_b⟩ = 2^{−b/2} Σ_{y=0}^{2^b−1} e^{2πiy/2^b}|y⟩ on b qubits. Writing y in binary,
|G_b⟩ = ⊗_{r=0}^{b−1} |P_{b−r}⟩ (qubit r holds bit r), where
|P_j⟩ = (|0⟩ + e^{2πi/2^j}|1⟩)/√2.

**Lemma 3 (exact dyadic phases).** For an integer z, let A_z be the controlled
addition |c⟩|y⟩ ↦ |c⟩|y + cz mod 2^b⟩. Then A_z(|c⟩|G_b⟩) = e^{−2πicz/2^b}|c⟩|G_b⟩:
on the ideal register, A_z applies the phase gate diag(1, e^{−2πiz/2^b}) to the
control and leaves |G_b⟩ unchanged. A_z is a reversible Boolean circuit (ripple
carry with the classical constant z), hence an exact Clifford+T circuit of O(b)
NOT/CNOT/Toffoli gates (Toffoli has an exact 7-T decomposition, Nielsen–Chuang,
*Quantum Computation and Quantum Information*, 10th anniv. ed., Fig. 4.9).

*Proof.* Σ_y e^{2πiy/2^b}|y+z⟩ = e^{−2πiz/2^b} Σ_y e^{2πiy/2^b}|y⟩ by y ↦ y − z mod 2^b. ∎

**Preparation (once, exact, b + 3 gates).** Apply H to each of the b qubits of a
fresh register, then Z, S, T to qubits b−1, b−2, b−3 respectively. As Z|+⟩ = |P_1⟩,
S|+⟩ = |P_2⟩ and T|+⟩ = |P_3⟩, this prepares exactly the product state |G̃_b⟩ in
which qubit b−j holds |P_j⟩ for j ≤ 3 and every other qubit holds |+⟩, i.e. |G_b⟩
with every factor |P_j⟩, j ≥ 4, replaced by |+⟩. No approximating gate words, gate
synthesis or stored tables are used. Write ρ̃ := |G̃_b⟩⟨G̃_b|.

**Lemma 4 (one constant budget).** For every b ≥ 3, D_tr(ρ̃, |G_b⟩⟨G_b|) ≤ δ_G :=
π/√192 < 0.2268.

*Proof.* Both states are product states whose factors agree for j ≤ 3, and
⟨+|P_j⟩ = (1 + e^{2πi/2^j})/2 = e^{πi/2^j} cos(π/2^j). Hence the fidelity is
F = |⟨G_b|G̃_b⟩|² = Π_{j=4}^{b} (1 − sin²(π/2^j)) ≥ 1 − Σ_{j≥4} sin²(π/2^j) ≥
1 − π² Σ_{j≥4} 4^{−j} = 1 − π²/192, using Π(1 − x_j) ≥ 1 − Σ x_j for x_j ∈ [0, 1]
and sin² y ≤ y². For pure states D_tr = √(1 − F) ≤ π/√192 < 0.2268. ∎

Since the whole run of LSIEVE is one fixed quantum instrument applied to the
initial gradient register and to the joint initial state of all Q copies (under the
error model of §8 this joint state, including the malformed copies and the
adversary's reference system, is fixed before the run and is independent of the
gradient register), replacing ρ̃ by the ideal
|G_b⟩ changes the distribution of the entire classical transcript (including the
output) by at most δ_G in total variation (contractivity of trace distance).
Below we analyse the run with the ideal |G_b⟩, where every phase produced by
Lemma 3 is exact and the register is reused unchanged for the whole run.

## 3. Fourier sampling by phase estimation

On an n-qubit register let U|y⟩ = |y+1 mod N⟩ for y < N and U|y⟩ = |y⟩ for y ≥ N.
Controlled-U^{2^i} is controlled addition of the constant 2^i mod N on the valid
range, an exact reversible circuit of O(n) gates exactly as in the baseline
construction (compare with N, add, conditionally subtract N; compute–copy–uncompute).
Every reversible subcircuit used here and below (these adders, the A_z, the X-test
subtraction) returns its ancillas to |0⟩ on every computational basis input, including
y ≥ N, hence for every input state, in particular for malformed copies.

**Procedure FS (one fresh copy).** Acquire a copy (registers: qubit q, n-qubit
register R). For i = μ−1 down to 0: prepare a control qubit in |+⟩, apply
controlled-U^{2^i} to R, then, with j' = Σ_{r<μ−1−i} j_r 2^r built from the bits
already measured, apply A_z with z = j'·2^{b−(μ−i)} controlled by the control
qubit (phase diag(1, e^{−2πij'/2^{μ−i}}), Lemma 3), then H, measure, and record
the bit j_{μ−1−i}. Let j = Σ_r j_r 2^r, report the label λ̂ = round(jN/2^μ) mod N
(ties down), discard R, and keep q.

**Kraus form of FS (proved here; no citation is used).** Let ω = e^{2πi/N} and
χ_k = N^{−1/2}Σ_{y<N} ω^{ky}|y⟩; then Uχ_k = ω^{−k}χ_k = e^{2πiλ/N}χ_k with
λ = −k mod N. Fix a round i and the bits already measured, and put
c_i = e^{−2πij'/2^{μ−i}}. For any state |ξ⟩ of (q, R), the control in |+⟩, then
controlled-U^{2^i} and diag(1, c_i), give (|0⟩|ξ⟩ + c_i|1⟩U^{2^i}|ξ⟩)/√2, and H then
gives ½|0⟩(I + c_iU^{2^i})|ξ⟩ + ½|1⟩(I − c_iU^{2^i})|ξ⟩. So reading bit b applies
K_{i,b} = (I + (−1)^b c_iU^{2^i})/2 to R (identity on q), and the outcome string j
applies K_j = K_{0,j_{μ−1}} ⋯ K_{μ−1,j_0}, a polynomial in U. Hence K_jχ_k = α_j(λ)χ_k
with α_j(λ) = Π_{i=0}^{μ−1} (1 + (−1)^{j_{μ−1−i}} c_i e^{2πi2^iλ/N})/2. Put
δ = λ/N − j/2^μ. The bits fixed after round i are j mod 2^{μ−i} = j' + j_{μ−1−i}2^{μ−1−i},
and 2^i j/2^μ ≡ (j mod 2^{μ−i})/2^{μ−i} (mod 1); since |1 + e^{2πiθ}|/2 = |cos πθ|
and |cos| has period π, the i-th factor has modulus |cos(π2^iδ)|. By
2 sin x cos x = sin 2x, 2^μ sin(πδ) Π_{i<μ} cos(π2^iδ) = sin(π2^μδ), so
|α_j(λ)| = |sin(π2^μδ)|/(2^μ|sin πδ|) (and |α_j(λ)| = 1 if δ ∈ Z). Finally
Σ_j |α_j(λ)|² = 1, because Σ_{b∈{0,1}} |1 + (−1)^b z|²/4 = 1 whenever |z| = 1 (sum
over the last measured bit first). This is the semiclassical form of phase
estimation (Griffiths–Niu, Phys. Rev. Lett. 76:3228, 1996, cited for provenance only).

**Lemma 5 (exact phase qubit, uniform label, rare mislabel).** With the ideal
gradient, one execution of FS on a clean copy (a copy in state ρ_s, in tensor
product with everything else) has the following joint law: a label λ uniform on
{0,…,N−1}; the kept qubit is exactly |φ_λ⟩; and P(λ̂ ≠ λ | λ) ≤ 2^{−t}. Distinct
executions on clean copies are independent, and the pair (λ, kept qubit) of a clean
copy is in tensor product with every other system.

*Proof.* Let ω = e^{2πi/N} and χ_k = N^{−1/2}Σ_{y<N} ω^{ky}|y⟩. Then Uχ_k = ω^{−k}χ_k,
the χ_k are orthonormal, and |y⟩ = N^{−1/2}Σ_k ω^{−ky}χ_k. For a component
x of the source, (|0,x⟩ + |1,x+s⟩)/√2 = N^{−1/2} Σ_k ω^{−kx} |φ_{−k}⟩ ⊗ χ_k, with
|φ_{−k}⟩ = (|0⟩ + ω^{−ks}|1⟩)/√2. Put λ = −k mod N; χ_k has U-eigenphase λ/N.
By the Kraus form above, outcome j maps this component to
N^{−1/2} Σ_k ω^{−kx} α_j(λ)|φ_{−k}⟩ ⊗ χ_k, with α_j(λ) depending only on λ. Tracing R,
the cross terms between distinct k vanish (χ_k orthogonal), so q
with outcome j is Σ_λ N^{−1}|α_j(λ)|² |φ_λ⟩⟨φ_λ|, independent of x, hence also for
the mixture ρ_s. Thus λ is uniform, j has law |α_j(λ)|² given λ, and q = |φ_λ⟩.
Tail: with δ_j the signed circular distance between λ/N and j/2^μ, |α_j| =
|sin(π2^μδ_j)|/(2^μ|sin πδ_j|) ≤ 1/(2^{μ+1}|δ_j|) as |sin πx| ≥ 2|x| for |x| ≤ 1/2.
With d_j = 2^μ|δ_j|, the d_j exceeding h form, on each side of 2^μλ/N, a sequence
with r-th term ≥ h + r − 1, so P(d_j > h) ≤ 2Σ_{r≥1} 1/(4(h+r−1)²) ≤ 1/(2(h−1))
(the standard bound, Nielsen–Chuang §5.2.1). Take h = 2^t: with probability
≥ 1 − 1/(2(2^t−1)) ≥ 1 − 2^{−t}, |λ/N − j/2^μ| ≤ 2^t/2^{n+t+2} = 2^{−n−2} < 1/(2N),
since N ≤ 2^n. Then jN/2^μ is within 1/4 of λ modulo N, so λ̂ = λ. The copy is in tensor
product with everything else and the registers are fresh, which gives independence. ∎

Cost of FS. Once per run, before the first FS, the controller computes the table
c_i = 2^i mod N, i < μ, by μ successive doublings modulo N (O(n²) bit operations,
O(n³) with address costs; O(n²) stored bits). Each round reads c_i to generate its
adder and forms z = j'·2^{b−(μ−i)} by a shift: O(n + b) = O(n) gates and O(n)
classical bit operations; plus O(n²) bit operations for λ̂.
"Discard R" means: measure R and apply X to each qubit that gave 1, so R's n qubits
are reused (O(n) operations). Peak extra space O(n) qubits.


## 4. Interval sieve of depth at most K

**SIEVE(e)**, for 1 ≤ e ≤ n−2. Let E = n−1−e ≥ 1, R = ⌈E/ℓ⌉, and split
E = ℓ_1 + … + ℓ_R with each ℓ_i ∈ {⌊E/R⌋, ⌈E/R⌉}, so 1 ≤ ℓ_i ≤ ℓ. Since E < n ≤ Kℓ,
R ≤ K. Put w_0 = 2^{n−1}, w_i = w_{i−1}/2^{ℓ_i} (so w_R = 2^e ≥ 2),
I_0 = {0,…,w_0−1}, I_i = {−w_i/2+1, …, w_i/2} (|I_i| = w_i), and L_i = 16^{R−i}Λ.

* Stage 0. Run FS (§3) on each of the first 4L_0 copies of the slot. Discard
  (measure) each qubit with λ̂ ≥ 2^{n−1}; keep the first L_0 others (measure and
  discard the rest); abort if fewer than L_0.
* Stage i = 1,…,R. The input is L_{i−1} items with labels in I_{i−1}. Let v = w_i.
  Bucket index of λ: ⌊(λ − min I_{i−1})/v⌋ ∈ {0,…,2^{ℓ_i}−1}. Stably sort items by
  bucket index and pair consecutive items inside each bucket (an odd item out is
  discarded). For each pair (λ_1, λ_2) apply Lemma 1. On outcome 0 discard. On
  outcome 1 let d = λ_1 − λ_2; if d ∉ I_i discard; otherwise draw a uniform t-bit
  integer U (each bit by measuring H|0⟩ on a fresh qubit) and keep the qubit with
  label d iff U·(v−|d|) < (v/2)·2^t. Keep the first L_i survivors (in pair order;
  measure and discard the rest); abort if fewer.
* Output: the L_R = Λ final items.

*Lineage.* A stage-0 item descends from one copy; an item produced from a pair
descends from the union of its two parents' copies. Since every item enters at
most one pair, **distinct live items of one sieve run descend from disjoint sets of
copies**, of size at most 2^R ≤ 2^K. An item is *clean* if every copy it descends
from is clean (§8) and *contaminated* otherwise.

The *coarse data* of a run consists of: which stage-0 labels are < 2^{n−1}, all
bucket indices, the pairing, all Lemma-1 outcomes, all keep/discard decisions and
the order of survivors. In the *ideal run* (§6) the gradient is ideal, the label of
every item descending from clean copies is its true label (the λ of Lemma 5) and
each keep coin is an exact Bernoulli(q(d)) with q(d) = (v/2)/(v−|d|) ∈ [1/2, 1]
(|d| ≤ v/2 on I_i). Contaminated items carry the labels the algorithm computes.

**Lemma 6 (clean items, any pairing).** Fix a decision and consider the ideal run.
For i = 0,…,R let ℋ_i be the whole classical record of the run up to the end of
stage i of this decision, except the labels of the live clean items and of the
items they descend from, together with the Fourier-sampling outcomes j and the
keep-coin integers U from which those labels were computed or tested (all of these
are never used again; only the keep/discard bit of each coin is in ℋ_i). Conditioned on any
value of ℋ_i, the live clean items have labels i.i.d. uniform on I_i, and the joint
state is Σ_{λ⃗} |I_i|^{−g}|λ⃗⟩⟨λ⃗| ⊗ (⊗_c |φ_{λ_c}⟩⟨φ_{λ_c}|) ⊗ σ, where g is their
number and σ, the state of all other systems (contaminated items, unused copies, the
adversary's reference system), does not depend on λ⃗.

*Proof.* Stage 0: clean copies are in tensor product with everything (§8), in
particular with the malformed copies, the reference and all earlier systems; by
Lemma 5 each yields a uniform label on {0,…,N−1} and the exact qubit |φ_λ⟩ in
tensor product with all else. The pass event λ < 2^{n−1} and the order are coarse;
given a pass the label is uniform on I_0 (w_0 ≤ N); a failed clean item's label may
be revealed, as it is independent of the rest. Stage i: assume the claim for i−1.
Revealing bucket indices, a live clean label is, given its index, uniform on its
bucket (v consecutive integers; the buckets partition I_{i−1}), independently. The
pairing and order are functions of coarse data, whatever the contaminated labels
are. (1) Clean–clean pair: the offsets u_1, u_2 are i.i.d. uniform on {0,…,v−1}, so
P(d = x) = (v−|x|)/v²; by Lemma 1 (both qubits pure, so in product with all else)
the outcome is a fair coin independent of everything and outcome 1 leaves |φ_d⟩.
Hence P(outcome 1, kept, d = x) = ½·(v−|x|)/v²·(v/2)/(v−|x|) = 1/(4v) for every
x ∈ I_i: the pair survives with probability exactly 1/4, independently of all other
pairs, and given survival d is uniform on I_i and the qubit is |φ_d⟩, pure. If it
does not survive, its labels may be revealed. (2) A pair with a contaminated member
yields a contaminated item or nothing; all its data depend only on that clean
member (consumed) and contaminated systems, hence are independent of the other live
clean labels. (3) Truncation is by coarse order. ∎

**Lemma 7 (counts under contamination).** Fix a decision; let C be the number of
malformed copies among the first 4L_0 copies of its slot, and assume C ≤ Λ/257. In
the ideal run: (a) at every stage at most C live items are contaminated; (b) stage
0 aborts with probability ≤ e^{−L_0/12}, and otherwise at least L_0 − C kept items
are clean; (c) given no earlier abort, stage i ≥ 1 aborts with probability
≤ e^{−L_{i−1}/65}, and otherwise at least L_i − C of its L_i outputs are clean.

*Proof.* We use the Chernoff bound P(X ≤ (1−δ)κ) ≤ e^{−δ²κ/2} for X binomial with
mean κ (M. Mitzenmacher and E. Upfal, *Probability and Computing*, 2005, Thm. 4.5),
also valid when the mean is ≥ κ (stochastic domination). (a) A stage-0 contaminated
item is a malformed copy; a contaminated item of stage i has a contaminated parent,
and parents are distinct. (b) At least 4L_0 − C ≥ 3.99L_0 copies are clean; their
pass events are independent with probability 2^{n−1}/N ≥ 1/2, so the number X of
passing clean items dominates Binomial(⌈3.99L_0⌉, 1/2); with κ = 1.995L_0 and
(1−δ)κ = L_0, δ ≥ 0.49, so P(X < L_0) ≤ e^{−0.24·1.995L_0/2} ≤ e^{−L_0/12}. If X ≥ L_0
there is no abort and at most C of the L_0 kept items are contaminated. (c) Let G
and C' ≤ C be the clean and contaminated live inputs, G + C' = L_{i−1}, so
G ≥ L_{i−1} − C. In a bucket with g clean and c contaminated items there are
⌊(g+c)/2⌋ pairs, at most c of which contain a contaminated item, so at least
(g − c − 1)/2 clean–clean pairs; summing over the 2^{ℓ_i} ≤ B buckets, the number of
clean–clean pairs is K' ≥ (L_{i−1} − 2C − B)/2. As L_{i−1} ≥ 16Λ, C ≤ Λ/257 and
B = 2^{−20}Λ, 2C + B ≤ 0.0079Λ ≤ 0.0005L_{i−1}, so K' ≥ 0.4997L_{i−1}. By Lemma 6,
given ℋ_{i−1} and the pairing, the number S of surviving clean–clean pairs is
Binomial(K', 1/4), mean κ ≥ 0.1249L_{i−1}. With (1−δ)κ = L_{i−1}/16, δ ≥ 0.499 and
P(S < L_i) ≤ e^{−0.249·0.1249L_{i−1}/2} ≤ e^{−L_{i−1}/65}. If S ≥ L_i there is no abort,
and at most C of the first L_i survivors are contaminated, by (a). ∎

**Coins.** The actual keep probability is ⌈(v/2)2^t/(v−|d|)⌉/2^t, within 2^{−t} of
q(d); couple each actual coin with an exact one so they differ with probability
≤ 2^{−t}.

## 5. Decisions and interval shrinking

**Selection and Vote(D).** After SIEVE(e), an output item is *selected* if its
label λ satisfies λ = 1 (when e = 1) or 2^{e−2} ≤ |λ| ≤ 2^{e−1} (when e ≥ 2); a
selected item with negative label is flipped by X (Lemma 2) and its label negated.
Abort if no item is selected. Given the invariant (a, W) and the S ≥ 1 selected
qubits |φ_{λ_k}⟩ with known integers λ_k ≥ 1 (all other output items are measured
and discarded): for each k let r_k = λ_k(2a+W) mod 2N and z_k = round(2^b r_k/(2N));
apply A_{z_k} controlled by qubit k (Lemma 3), then S†, H, measure. Decide "+" iff
more than S/2 outcomes are 0. With exact phases e^{−2πir_k/(2N)} a qubit in state
|φ_{λ_k}⟩ becomes (|0⟩ + e^{2πiψ_k}|1⟩)/√2 with ψ_k ≡ λ_k(s − a − W/2)/N ≡
λ_k(u − W/2)/N (mod 1), as λ_k is an integer and s ≡ a + u. The rounded phase
differs by an operator-norm error ≤ π2^{−b} per qubit.

**Lemma 8 (robust vote, exact phases).** Let 0 < ψ_0 ≤ 1/16 and β = sin(2πψ_0)/2.
Suppose the selected set consists of G ≥ 1 *clean* qubits, which conditioned on the
classical record are exactly ⊗_k |φ_{λ_k}⟩ with known labels and in tensor product
with all other systems, and of C' ≤ βG further qubits in an arbitrary joint state
(possibly entangled with each other and with any other system).
(a) If λ_kW ≤ 7N/8 and λ_kD ≥ ψ_0N for every clean k, then: if u ≤ W/2 − D the
decision is "+" with probability ≤ e^{−β²G/2}; if u ≥ W/2 + D it is "−" with
probability ≤ e^{−β²G/2}.
(b) If a = 0, W = N and every clean λ_k = 1: if u ∈ [N/8, 3N/8] the decision is
"+", and if u ∈ [5N/8, 7N/8] it is "−", each with probability ≤ e^{−G/16}.

*Proof.* (a) For a clean k the real number ψ_k = λ_k(u − W/2)/N satisfies
|ψ_k| ≤ λ_kW/(2N) ≤ 7/16 and, when |u − W/2| ≥ D, |ψ_k| ≥ ψ_0. On [2πψ_0, 7π/8],
sin ≥ min(sin 2πψ_0, sin(π/8)) = sin 2πψ_0. By Lemma 2 each clean outcome is 0 with
probability ≤ 1/2 − β (if u ≤ W/2 − D) or ≥ 1/2 + β (if u ≥ W/2 + D). The clean
qubits are pure and in product with everything, so their outcomes X_k (indicator of
0) are independent of each other and of all other outcomes. Let X = Σ_clean X_k.
Case u ≤ W/2 − D: "+" requires more than (G + C')/2 zeros, hence
X > (G + C')/2 − C' = G/2 − C'/2, while EX ≤ G/2 − βG; the deviation exceeds
βG − C'/2 ≥ βG/2, so by Hoeffding's inequality (W. Hoeffding, J. Amer. Statist.
Assoc. 58:13–30, 1963, Thm. 2, variables in [0,1]) the probability is
≤ e^{−2(βG/2)²/G} = e^{−β²G/2}. Case u ≥ W/2 + D: "−" requires at most (G + C')/2
zeros, hence X ≤ G/2 + C'/2, while EX ≥ G/2 + βG; same bound. (b) Here ψ = (u − N/2)/N;
u ∈ [N/8, 3N/8] gives 2πψ ∈ [−3π/4, −π/4], so sin 2πψ ≤ −1/√2 and β = 1/(2√2)
(> 1/64, so C' ≤ βG holds whenever C' ≤ G/64); e^{−β²G/2} = e^{−G/16}. The other case
is symmetric. ∎

**Update rules.** (i) Step 0 (Lemma 8(b)): on "+" set a' = ⌊3N/8⌋,
W' = N + ⌈N/8⌉ − ⌊3N/8⌋; on "−" set a' = ⌊7N/8⌋, W' = ⌈5N/8⌉ + N − ⌊7N/8⌋. Both have
W' ≤ 3N/4 + 2. (ii) General (Lemma 8(a)): with g = max(0, ⌊W/2 − D⌋), on "+" set
a' = a + g mod N, W' = W − g; on "−" set a' = a, W' = min(W, ⌈W/2 + D⌉). Always
W' ≤ W/2 + D + 1.

**Lemma 9 (invariant).** If the decision is not one of the "wrong" events of
Lemma 8, the invariant holds for (a', W').

*Proof.* (ii) "+" was not wrong, so u > W/2 − D, hence u ≥ g and s ≡ a' + (u − g)
with 0 ≤ u − g < W'. "−" was not wrong, so u < W/2 + D and u < W, hence u < W'.
(i) "+" not wrong gives u ∉ [N/8, 3N/8]: if u > 3N/8 then v = u − ⌊3N/8⌋ ∈ [0, W');
if u < N/8 then v = u + N − ⌊3N/8⌋ < W'; in both cases s ≡ a' + v (mod N).
"−" not wrong gives u ∉ [5N/8, 7N/8]: if u > 7N/8, v = u − ⌊7N/8⌋; if u < 5N/8,
v = u + N − ⌊7N/8⌋ < W'. ∎

**Schedule and its parameters.**
* Steps 1–4: e = 1 (labels in {0,1}); use labels λ = 1 only; D = N/32, ψ_0 = 1/32,
  β ≥ (1/2)(2/π)(π/16) = 1/16. From W_0 ≤ 3N/4 + 2 and W' ≤ W/2 + N/32 + 1:
  W_1 ≤ 13N/32 + 2, W_2 ≤ 15N/64 + 2, W_3 ≤ 19N/128 + 2, W_4 ≤ 27N/256 + 2 ≤ N/8
  (N > 2^{31} ≥ 103); and λW ≤ 3N/4 + 2 ≤ 7N/8. Step 0 also uses e = 1 and λ = 1.
* Loop (W ≤ N/8, W ≥ 3): e = max{e : 2^{e+1}W ≤ N}, so 2 ≤ e ≤ n−3 and 2^{e+2}W > N.
  Use labels with 2^{e−2} ≤ |λ| ≤ 2^{e−1} (flipped to positive); D = W/8. Then
  λW ≤ N/4 and λD/N ≥ 2^{e−2}W/(8N) > 1/128 =: ψ_0, β ≥ (1/2)(2/π)(π/64) = 1/64,
  and W' ≤ 5W/8 + 1. With V = W − 8/3, V' ≤ 5V/8, so after k iterations
  V ≤ (5/8)^k N/8, and W < 3 once k > log_{8/5}(3N/8); as log(8/5) > 0.678 this
  takes at most ⌊1.48n⌋ + 1 ≤ 2n iterations, on every branch.
* Selection: in every decision of the ideal run (§6) a clean output item is selected with probability
  ≥ 1/2 given its coarse data (e = 1: λ = 1 is half of I_R = {0,1}; e ≥ 2: 2^{e−1}+1
  of the 2^e values of I_R), independently (Lemma 6). In all cases β ≥ 1/64.
* There are at most 1 + 4 + 2n = 2n + 5 decisions, matching the 2n+5 decision slots.

**Lemma 10 (one decision).** Consider a decision of the ideal run (§6) whose slot
contains C ≤ Λ/257 malformed copies among its first 4L_0 copies, and condition on the
record before it. Then, outside an event of probability ≤ η := (K+3)e^{−32n}, the
decision does not abort and its outcome is not one of the "wrong" events of Lemma 8.

*Proof.* By Lemma 7 there is no abort in SIEVE(e) except with probability
≤ e^{−L_0/12} + Σ_{i≥1} e^{−L_{i−1}/65} ≤ (K+1)e^{−Λ/65}, and then at least Λ − C ≥
(256/257)Λ output items are clean and at most C are contaminated. By Lemma 6 the clean
outputs have i.i.d. uniform labels on I_R given ℋ_R, so the number G of selected clean
items dominates Binomial(⌈0.996Λ⌉, 1/2); by the Chernoff bound of Lemma 7 with
κ = 0.498Λ and (1−δ)κ = Λ/4, P(G < Λ/4) ≤ e^{−0.247·0.498Λ/2} ≤ e^{−Λ/17}. If
G ≥ Λ/4 then the selected contaminated items number C' ≤ C ≤ Λ/257 < Λ/256 ≤ G/64 ≤ βG,
the selected clean qubits are exactly ⊗|φ_{λ_k}⟩ in product with all else (Lemma 6),
and their labels satisfy the hypotheses of Lemma 8 by the schedule above. Lemma 8 then
bounds a wrong decision by e^{−β²G/2} ≤ e^{−Λ/32768} = e^{−32B}. For n ≥ 32,
B = 2^ℓ ≥ 2^{n/K} ≥ 2^{n/(log n + 1)} ≥ n (at n = 32, 2^{32/6} > 32, and n/(log n + 1) −
log n is increasing), and Λ/65, Λ/17 ≥ 32B, so every term above is ≤ e^{−32n}. ∎

## 6. Success probability under malformed copies

**Theorem 1.** Let ε(n) = 1/(65536 n^5). For every N ≥ 2, every s ∈ Z/NZ and every
adversary of the error model of §8 (at most ⌊ε(n)Q⌋ of the Q acquired copies
malformed), LSIEVE outputs s with probability > 0.77 if n ≥ 32 and > 3/4 if n < 32;
in all cases > 2/3. The adversary that corrupts nothing is included, so this also
proves the clean-input guarantee.

*Proof (n < 32).* Q = N(n+2) ≤ 2^n(n+2) < 65536n^5 for 1 ≤ n ≤ 31 (direct check;
at n = 31, 7.2·10^{10} < 1.9·10^{12}), so ⌊ε(n)Q⌋ = 0: every copy is clean and the
baseline argument of §0 gives success > 3/4.

*Proof (n ≥ 32).* *Budget.* Q = Q_fix on every branch (§0). As K ≤ log n + 1,
16^K ≤ 16n^4, and (2n+6)/n ≤ 2.1875, so ε(n)Q_fix = (2n+6)·4·16^K·Λ/(65536n^5) ≤
(2n+6)Λ/(1024n) < Λ/468. Hence every slot contains fewer than Λ/257 malformed copies,
whatever the adversary does.

*Gradient.* With the ideal register |G_b⟩, Lemma 3 is an operator identity for every
state of the control qubit, so every A_z, applied to clean, malformed or
contaminated qubits alike, leaves |G_b⟩ unchanged and in tensor product with all
other systems. Under the model of §8 the initial state is (gradient) ⊗ (joint state of
all copies and the reference), and the run is a fixed instrument on it; by Lemma 4
and contractivity, replacing ρ̃ by |G_b⟩ changes the law of the output by ≤ δ_G < 0.2268.

Compare four runs. The numbers of FS executions, keep coins and vote
qubits are each at most Q_fix (each consumes or descends from distinct copies).
(1) Real run vs. ideal gradient: ≤ 0.2268. (2) Rounded vote phases → exact phases:
≤ Q_fix·π2^{−b} ≤ 2^{−n} (b > t, Q_fix2^{−t} ≤ 2^{−10}), since
D_tr(UρU†, VρV†) ≤ ‖U − V‖ and errors add. (3) Keep coins → exact coupled coins:
≤ Q_fix2^{−t} ≤ 2^{−10}. (4) For clean copies only, reported labels λ̂ → true labels λ
(genie run): by Lemma 5 the state of (j, q) after FS on a clean copy is
Σ_{λ,j} N^{−1}|α_j(λ)|²|j⟩⟨j| ⊗ |φ_λ⟩⟨φ_λ|, in tensor product with everything else, the
marginal of the same expression with an added classical register |λ⟩⟨λ| that the
algorithm never reads; adjoining it changes no distribution, and the runs differ only
if some clean FS has λ̂ ≠ λ, which has conditional probability ≤ 2^{−t} each time;
summing over ≤ Q_fix executions, ≤ 2^{−10}. The resulting run is the ideal run of §4.

*Ideal run.* By Lemma 9 and induction over decisions, the invariant holds when the
final slot is reached unless some decision aborts or is wrong; by Lemma 10 (every slot
has C < Λ/257) and a union bound over ≤ 2n+5 decisions this has probability
≤ (2n+5)(K+3)e^{−32n} < 10^{−400}. *Final slot.* If W = 1 then s ≡ a. If W = 2 then
s ∈ {a, a+1}; at most C_f < Λ/257 < P/1000 of its P copies are malformed. Each clean
X-test is performed on a copy in tensor product with everything, so its outcome is
independent of all other outcomes, "+" with certainty if s = a and with probability
exactly 1/2 if s = a+1 (§0). If s = a, at least P − C_f ≥ 3P/4 tests give + and the
output is a. If s = a+1, the number Y of clean "+" has mean (P − C_f)/2 ≤ P/2, and a
wrong output needs Y ≥ 3P/4 − C_f ≥ EY + P/5; by Hoeffding this has probability
≤ e^{−2P/25} < 10^{−400}. Altogether the failure probability is at most
0.2268 + 2^{−n} + 2·2^{−10} + 2·10^{−400} < 0.229, so success > 0.77 > 2/3. ∎

The model allows M and the joint malformed state to be chosen at random; the bound
above holds conditioned on every fixed choice (for which the tensor-product clause of
§8 holds), hence for the mixture by convexity. Note that the proof never uses which positions the adversary chose: only the count
bound per slot, the tensor-product independence of clean copies from the malformed
systems (Lemma 6 needs it to keep clean labels uniform under any pairing), and the
fact that the adversary does not act after the run starts.

## 7. Resources and growth indices

For n ≥ 32 let L* = 16^KΛ; every sieve run has L_0 ≤ L* and Σ_i L_i ≤ 2L_0. As
K ≥ log n, ℓ = ⌈n/K⌉ ≤ n/log n + 1, so B ≤ 2·2^{n/log n}; with 16^K ≤ 16n^4,
L* ≤ 2^{25}n^4·2^{n/log n}, P = 4L* ≤ 2^{27}n^4·2^{n/log n}, and Q_fix = (2n+6)P ≤
2^{29}n^5·2^{n/log n}. Also t = ⌈log Q_fix⌉ + 10 ≤ n/log n + 5log n + 40 = O(n), so
μ = b = O(n). Below, F(n) := 2^{n/log n} (for n ≥ 2).

**Samples.** On every branch exactly Q = Q_fix = O(n^5 F(n)) copies are acquired
(§0), including discarded copies, unused slots and the final slot.

**Quantum space.** Live sieve qubits ≤ L_0 ≤ L* (stage-0 rejects and unused copies
are measured at once; stages work in place; a vote measures its qubits one by one),
plus one source copy (n+1 qubits), one control qubit, one coin qubit, the gradient
(b qubits) and O(n) adder ancillas: S_Q ≤ L* + O(n) = O(n^4 F(n)).

**Classical space.** Labels (n+1 bits each), bucket keys and a merge-sort buffer for
≤ L* items: O(nL*) bits; the table c_i, i < μ: O(n²) bits; parameters, slot/copy counters, vote and X-test counters
(O(log Q_fix) bits each) and the gate currently being generated: O(n). No circuit is
stored. S_C = O(n^5 F(n)).

**Total work.** All allocated bits and qubits number M_A = S_C + S_Q = O(n^5F(n)), so
every indexed access and every classically addressed gate pays ⌈log(M_A + 2)⌉ = O(n).
Charges:
* FS (one copy): source n+1; μ = O(n) rounds, each O(n) gates and measurements
  (adder mod N, A_z on b qubits, H) and O(n) classical bit operations (reading c_i,
  forming z), each with O(n) address cost: O(n²) per round; λ̂ by one O(n)×O(n)-bit
  product with O(n) address per bit operation: O(n³) per copy.
* Discarding a copy: O(n) measurements and resets, O(n) address each: O(n²).
* Sieve stage i: bucket keys O(n) per item; stable merge sort of L_{i−1} records of
  O(n) bits: O(L_{i−1}log L_{i−1}) comparisons/moves of O(n) bits with O(n) address
  cost each, and log L_{i−1} = O(n): O(L_{i−1}n³); per pair one CNOT, one measurement,
  d, and a t×(n+1)-bit product: O(n²) bit operations, O(n³) with address cost, and
  there are at most L_0 pairs. Per sieve run, with its 4L_0 FS copies: O(L*n³).
* Vote: per selected qubit r_k, z_k (O(n·b) bit operations) and A_{z_k} (O(n) gates,
  O(n) address each): O(n³) with address cost; per decision O(Λn³) ≤ O(L*n³).
* Final slot: P X-tests, O(n) gates with O(n) address each: O(Pn²). Gradient
  preparation and parameter arithmetic: O(n²); the table c_i: O(n³), once per run.
Summing over the 2n+6 slots, T = O(n·L*·n³ + Q_fix·n²) = O(n^8 F(n)).
For n < 32 all four quantities are bounded by absolute constants (N < 2^{32}).

**Envelopes and indices.** B_T = 2^{n/log n}n^8, B_C = 2^{n/log n}n^5,
B_Q = 2^{n/log n}n^4, B_samples = 2^{n/log n}n^5 (n ≥ 2; at n = 1, N = 2, every
resource is an absolute constant). For each, log B = n/log n + r log n with
r ∈ {8, 5, 4, 5}, so log log B = log n − log log n + o(1) and
g(B) = limsup_{n→∞} log log max{4, B(n)} / log n = 1. Multiplicative constants do not
change this. All four bounds hold jointly for the one configuration LSIEVE, on every
branch and for every adversary of §8, together with success > 2/3 (Theorem 1). In the
structured grammar each envelope is 2^{1·n^1(log n)^{−1}}·n^r: one exponent term with
coefficient 1, nPower 1, logPower −1, and outer nPower r, logPower 0. The score vector
is [1].

## 8. Error model and fractional error tolerance

The error model of claim 5, verbatim:

> Oblivious adversarial malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires, and epsilon(n) the tolerated malformed fraction; copies are indexed 1, ..., Q in acquisition order. Before the algorithm starts, an adversary that knows N, s and the full description of the algorithm, but none of the algorithm's random bits or measurement outcomes, chooses (possibly at random) a set M of positions and a joint state of |M| systems of n+1 qubits each (the register shape of an ideal copy) together with a private reference system; on every execution branch at most floor(epsilon(n) Q) of the Q acquired copies have positions in M. The copy at a position in M is malformed: it is the corresponding system of that joint state, which is arbitrary (pure or mixed, entangled with the other malformed copies and with the reference system). Every other copy is clean: an ideal coset state rho_s = (1/N) sum_x |psi_{x,s}><psi_{x,s}|. Conditioned on M and on the adversary's random choices, the clean copies, the joint system of all malformed copies and the reference, and the algorithm's initial workspace are in tensor product; in particular the clean copies are independent ideal coset states, uncorrelated with every malformed copy. After this choice the adversary takes no further action: it does not observe the run and acts on no system. The algorithm is not told which copies are malformed; the labels it reports and the outcomes of its measurements on malformed copies, and on anything combined with them, are determined by that fixed state and obey no promised law. Quantifiers: for every N >= 2 (no validity threshold), every s in Z/NZ and every such adversary, including the one with M empty (the clean problem), the algorithm outputs the entire s with probability at least 2/3, and the four declared resource bounds hold on every execution branch. The fraction bounds the number of malformed copies among acquired copies; it is not a per-copy corruption probability.

For LSIEVE, Q = Q_fix on every branch if n ≥ 32 and Q = N(n+2) if n < 32, so the
budget ⌊ε(n)Q⌋ is a fixed number. Theorem 1 proves, jointly with the four resource
bounds of §7 (which hold on every branch for every adversary, since the copy schedule,
the loop lengths and all counts are fixed functions of n), that LSIEVE tolerates the
fraction

  ε(n) = 1/(65536 n^5) = \frac{1}{65536 n^5}

for every N ≥ 2. The proof uses three features of the model: (i) the count bound
(per slot, fewer than Λ/257 malformed copies, Theorem 1); (ii) clean copies are in
tensor product with all malformed systems, so clean labels stay i.i.d. uniform under
any pairing the malformed labels induce (Lemma 6) and clean qubits stay pure;
(iii) the adversary does not act after the run starts, so it cannot choose malformed
states as functions of clean labels. An adaptive adversary that sees the Fourier-
sampling outcomes would know every clean label and could choose malformed labels to
steer which clean items are paired; that model is not claimed here.

The value is not optimised: each final qubit descends from at most 2^K < 2n copies,
but the slot structure and the 1/16 per-stage yield cost the factor n^5. No maximal-
tolerance claim is made.
