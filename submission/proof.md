# Interval sieve with phase-estimation Fourier sampling

All logarithms are base 2. N ≥ 2, s ∈ Z/NZ, n = ⌈log N⌉, so 2^{n−1} < N ≤ 2^n.
One algorithm, called **ISIEVE**, with the parameters fixed below, is used for all
five claims. It is a Kuperberg-type collimation sieve (G. Kuperberg, "A
subexponential-time quantum algorithm for the dihedral hidden subgroup problem",
SIAM J. Comput. 35(1):170–188, 2005), re-derived here for arbitrary N with integer
labels sieved by intervals; nothing below relies on that paper's statements.

## 0. Algorithm and parameters

**Small n.** If n < 64, ISIEVE runs the exhaustive shift test of the baseline
(for t = 0,…,N−1, n+2 controlled-subtraction X-tests). Since N < 2^{64}, its
cost is an absolute constant and it succeeds with probability > 3/4 (baseline
proof: a wrong t survives n+2 tests with probability 2^{−n−2}; union bound
(N−1)2^{−n−2} < 1/4; the right t always survives).

**Parameters for n ≥ 64** (all computed by the controller from n with O(n²)
bit operations):

| symbol | value |
| --- | --- |
| ℓ | ⌈√n⌉ (bucket bits per sieve stage); B := 2^ℓ |
| m | 2048(⌈log n⌉ + 10) (votes per decision); M := 4m |
| Λ | max(17B, M) (sieve output size) |
| Q_max | 3(2n+5)·17^ℓ·Λ + 10 |
| t | ⌈log Q_max⌉ + 10 (precision bits) |
| μ | n + t + 2 (phase-estimation bits); gradient size b := μ |

**Main loop (n ≥ 64).** Prepare once the phase-gradient register G_b (§2).
Maintain a *cyclic interval* (a, W): integers 0 ≤ a < N, 1 ≤ W ≤ N, with the
invariant s ≡ a + u (mod N) for some integer 0 ≤ u < W. Start a = 0, W = N.

1. Step 0: one decision with labels e = 1, update rule (i) of §5.
2. Steps 1–4: four decisions with e = 1, D = N/32, update rule (ii) of §5.
3. While W ≥ 3: one decision with e = e(W) := max{e : 2^{e+1}W ≤ N} and
   D = W/8, update rule (ii) of §5.
4. Final test (W ≤ 2): if W = 1 output a. Otherwise apply 10 baseline X-tests
   for the candidate a (fresh copies, controlled subtraction of a); output a if all give
   +, else a+1 mod N.

Each decision first runs one **sieve run** SIEVE(e) (§4) producing M phase qubits
with labels in {−2^{e−1}+1, …, 2^{e−1}}, then the vote of §5. **Abort rule:**
whenever a count required below is not met, ISIEVE outputs 0 and halts; this is
a failure branch counted in §6. Every loop has a length bounded by an explicit function of n (§5: at most 2n+5 decisions), so the
resource bounds of §7 hold on every branch.

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

Since the whole run of ISIEVE is one fixed quantum instrument applied to the
input copies and to the initial gradient register, replacing ρ̃ by the ideal
|G_b⟩ changes the distribution of the entire classical transcript (including the
output) by at most δ_G in total variation (contractivity of trace distance).
Below we analyse the run with the ideal |G_b⟩, where every phase produced by
Lemma 3 is exact and the register is reused unchanged for the whole run.

## 3. Fourier sampling by phase estimation

On an n-qubit register let U|y⟩ = |y+1 mod N⟩ for y < N and U|y⟩ = |y⟩ for y ≥ N.
Controlled-U^{2^i} is controlled addition of the constant 2^i mod N on the valid
range, an exact reversible circuit of O(n) gates exactly as in the baseline
construction (compare with N, add, conditionally subtract N; compute–copy–uncompute).

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
gradient, one execution of FS has the following joint law: a label λ uniform on
{0,…,N−1}; the kept qubit is exactly |φ_λ⟩; and P(λ̂ ≠ λ | λ) ≤ 2^{−t}. Distinct
executions are independent.

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
since N ≤ 2^n. Then jN/2^μ is within 1/4 of λ modulo N, so λ̂ = λ. Fresh copies
and fresh registers give independence. ∎

Cost of FS: μ rounds, each with O(n + b) = O(n) gates plus O(n²) classical bit
operations for 2^i mod N (by i < μ doublings modulo N) and z; plus O(n²) for λ̂.
"Discard R" means: measure R and apply X to each qubit that gave 1, so R's n qubits
are reused (O(n) operations). Peak extra space O(n) qubits.

## 4. Interval sieve

**SIEVE(e)**, for 1 ≤ e ≤ n−2. Let E = n−1−e ≥ 1, R = ⌈E/ℓ⌉ ≤ ℓ, and split
E = ℓ_1 + … + ℓ_R with each ℓ_i ∈ {⌊E/R⌋, ⌈E/R⌉}, so 1 ≤ ℓ_i ≤ ℓ. Put
w_0 = 2^{n−1}, w_i = w_{i−1}/2^{ℓ_i} (so w_R = 2^e ≥ 2), I_0 = {0,…,w_0−1},
I_i = {−w_i/2+1, …, w_i/2} (|I_i| = w_i), and L_i = 17^{R−i}Λ.

* Stage 0. Run FS 3L_0 times. Discard (measure) each qubit with λ̂ ≥ 2^{n−1};
  keep the first L_0 others (measure and discard the rest); abort if fewer than L_0.
* Stage i = 1,…,R. The input is L_{i−1} items with labels in I_{i−1}. Let v = w_i (bucket size).
  Bucket index of λ: ⌊(λ − min I_{i−1})/v⌋ ∈ {0,…,2^{ℓ_i}−1}. Stably sort items by
  bucket index and pair consecutive items inside each bucket. For each pair
  (λ_1, λ_2) apply Lemma 1. On outcome 0 discard. On outcome 1 let d = λ_1 − λ_2;
  if d ∉ I_i discard; otherwise draw a uniform t-bit integer U (each bit by measuring H|0⟩ on a fresh
  qubit: one gate and one measurement) and keep the
  qubit with label d iff U·(v−|d|) < (v/2)·2^t. Keep the first L_i survivors (in
  pair order; measure and discard the rest); abort if fewer.
* Output: the first M of the L_R = Λ ≥ M final items.

The *coarse data* of the run consists of: which stage-0 labels are < 2^{n−1}, all
bucket indices, the pairing, all Lemma-1 outcomes, all keep/discard decisions,
and the order of survivors. It contains no label of a live item beyond its
bucket index. Call a run *ideal* if its labels are the true labels λ of Lemma 5
(λ̂ = λ always) and each keep coin is an exact Bernoulli(q(d)) with
q(d) = (v/2)/(v−|d|) ≤ 1 (|d| ≤ v/2 on I_i).

**Lemma 6 (uniformity and independence).** In an ideal run, for every i, conditioned
on the coarse data up to the end of stage i, the live items are in the product
state ⊗|φ_λ⟩ and their labels are i.i.d. uniform on I_i.

*Proof.* Stage 0: by Lemma 5 labels are i.i.d. uniform on {0,…,N−1}; conditioning
on the events λ < 2^{n−1} (and on the others' values, which are discarded) leaves
the kept labels i.i.d. uniform on I_0, since w_0 ≤ N. Stage i: assume the claim
for i−1. Revealing bucket indices, each label is, given its index σ, uniform
on the full bucket {c+σv, …, c+σv+v−1} (c = min I_{i−1}; |I_{i−1}| = 2^{ℓ_i}v), independently.
The pairing and order are functions of bucket indices. Inside a pair, offsets
u_1, u_2 are i.i.d. uniform on {0,…,v−1} and d = u_1 − u_2 has
P(d) = (v−|d|)/v². By Lemma 1 the outcome is a fair coin independent of
everything and outcome 1 leaves |φ_d⟩. Hence P(outcome 1, kept, d = x) =
½·(v−|x|)/v²·(v/2)/(v−|x|) = 1/(4v) for every x ∈ I_i, which is uniform on I_i;
so P(pair survives) = 1/4 exactly, independent of other pairs, and given survival
d is uniform on I_i. Distinct pairs involve disjoint independent items and
independent coins; truncation to the first L_i is by coarse order. ∎

**Lemma 7 (counts).** In an ideal run, stage 0 aborts with probability
≤ e^{−L_0/12}, and stage i ≥ 1 with probability ≤ e^{−B/4} ≤ e^{−8√n}.

*Proof.* We use the Chernoff bound P(X ≤ (1−δ)κ) ≤ e^{−δ²κ/2} for X binomial with
mean exactly κ (M. Mitzenmacher and E. Upfal, *Probability and Computing*, 2005, Thm. 4.5); a binomial with the same number of trials and larger success probability stochastically dominates it, so the bound also holds when the mean is ≥ κ.
Stage 0: the kept count is Binomial(3L_0, 2^{n−1}/N) with 2^{n−1}/N ≥ 1/2; take
κ = 3L_0/2, δ = 1/3. Stage i: with c_σ items in bucket σ, the number of pairs is
K = Σ⌊c_σ/2⌋ ≥ (L_{i−1} − 2^{ℓ_i})/2 ≥ (L_{i−1} − B)/2 ≥ 8B, because
L_{i−1} ≥ 17Λ ≥ 17B. Survivors are Binomial(K, 1/4) by Lemma 6; with δ = 1/2,
P(survivors < K/8) ≤ e^{−K/32} ≤ e^{−B/4}. Otherwise survivors ≥ K/8 ≥ (L_{i−1} − B)/16 ≥
L_{i−1}/17 = L_i (as L_{i−1} ≥ 17B). Finally 2^x/4 ≥ 8x for x ≥ 8, so
e^{−B/4} ≤ e^{−8ℓ} ≤ e^{−8√n}. ∎

**Coins.** The actual keep probability is ⌈(v/2)2^t/(v−|d|)⌉/2^t, within 2^{−t} of
q(d); couple each actual coin with an exact one so they differ with probability
≤ 2^{−t}.

## 5. Decisions and interval shrinking

**Vote(D).** Given the invariant (a, W) and m qubits |φ_{λ_k}⟩ with known integers
λ_k ≥ 1 (negative labels were flipped by X, Lemma 2): for each k let
r_k = λ_k(2a+W) mod 2N and z_k = round(2^b r_k/(2N)); apply A_{z_k} controlled by
qubit k (Lemma 3), then S†, H, measure. Decide "+" iff more than m/2 outcomes are 0.
With exact phases e^{−2πir_k/(2N)} the qubit becomes (|0⟩ + e^{2πiψ_k}|1⟩)/√2 with
ψ_k ≡ λ_k(s − a − W/2)/N ≡ λ_k(u − W/2)/N (mod 1), as λ_k is an integer and
s ≡ a + u. The rounded phase differs by an operator-norm error ≤ π2^{−b} per qubit.

**Lemma 8 (vote reliability, exact phases).** Let 0 < ψ_0 ≤ 1/16 and β = sin(2πψ_0)/2.
(a) If λ_kW ≤ 7N/8 and λ_kD ≥ ψ_0N for all k, then: if u ≤ W/2 − D the decision is
"+" with probability ≤ e^{−2mβ²}; if u ≥ W/2 + D it is "−" with probability ≤ e^{−2mβ²}.
(b) If a = 0, W = N and all λ_k = 1: if u ∈ [N/8, 3N/8] the decision is "+", and
if u ∈ [5N/8, 7N/8] it is "−", each with probability ≤ e^{−m/4}.

*Proof.* (a) The real number ψ_k = λ_k(u − W/2)/N satisfies |ψ_k| ≤ λ_kW/(2N) ≤ 7/16
and, when |u − W/2| ≥ D, |ψ_k| ≥ ψ_0. On [2πψ_0, 7π/8], sin ≥ min(sin 2πψ_0,
sin(π/8)) = sin 2πψ_0. By Lemma 2 each outcome is 0 with probability ≤ 1/2 − β
(if u ≤ W/2 − D) or ≥ 1/2 + β (if u ≥ W/2 + D), independently given the labels
(product state). Hoeffding's inequality for independent bounded variables
(W. Hoeffding, J. Amer. Statist. Assoc. 58:13–30, 1963, Thm. 2, variables in [0,1]) bounds the wrong
majority by e^{−2mβ²}. (b) Here ψ = (u − N/2)/N; u ∈ [N/8, 3N/8] gives
2πψ ∈ [−3π/4, −π/4], so sin 2πψ ≤ −1/√2 and β = 1/(2√2); e^{−2mβ²} = e^{−m/4}.
The other case is symmetric. ∎

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
  (N ≥ 2^{63}); and λW ≤ 3N/4 + 2 ≤ 7N/8. Step 0 also uses e = 1 and λ = 1.
* Loop (W ≤ N/8, W ≥ 3): e = max{e : 2^{e+1}W ≤ N}, so 2 ≤ e ≤ n−3 and 2^{e+2}W > N.
  Use labels with 2^{e−2} ≤ |λ| ≤ 2^{e−1} (flipped to positive); D = W/8. Then
  λW ≤ N/4 and λD/N ≥ 2^{e−2}W/(8N) > 1/128 =: ψ_0, β ≥ (1/2)(2/π)(π/64) = 1/64,
  and W' ≤ 5W/8 + 1. With V = W − 8/3, V' ≤ 5V/8, so after k iterations
  V ≤ (5/8)^k N/8, and W < 3 once k > log_{8/5}(3N/8); as log(8/5) > 0.678 this
  takes at most ⌊1.48n⌋ + 1 ≤ 2n iterations, on every branch.
* Selection: each final sieve label is selected with probability ≥ 1/2 (e = 1:
  λ = 1 is half of {0,1}; e ≥ 2: 2^{e−1}+1 of the 2^e values of I_R). Among M = 4m
  i.i.d. labels at least m are selected except with probability ≤ e^{−m/4}
  (Mitzenmacher–Upfal Thm. 4.5, κ = 2m, δ = 1/2); the first m selected are used.
* In all cases β ≥ 1/64, so each vote is wrong with probability ≤ e^{−m/2048}
  = e^{−⌈log n⌉−10} ≤ e^{−10}/n. There are at most 1 + 4 + 2n = 2n + 5 decisions.

## 6. Success probability

**Theorem 1.** For every N ≥ 2 and s, ISIEVE outputs s with probability > 0.769 if
n ≥ 64 and > 3/4 if n < 64; in all cases at least 3/4 > 2/3, unconditionally.

*Proof (n ≥ 64).* The number of FS executions, keep coins and vote qubits are each
at most Q_max (fixed counts; abort only shortens a run). Compare four runs.
(1) Real run vs. run with ideal gradient: ≤ δ_G < 0.2268 (Lemma 4).
(2) Replace each rounded vote phase by the exact phase: ≤ Q_max·π2^{−b} ≤ 2^{−n}
(b > t, Q_max2^{−t} ≤ 2^{−10}), since D_tr(UρU†, VρV†) ≤ ‖U − V‖ and errors add.
(3) Replace each keep coin by its exact coupled coin: ≤ Q_max2^{−t} ≤ 2^{−10}.
(4) Replace each reported label λ̂ by the true label λ (genie run): the two runs
agree unless some λ̂ ≠ λ; by Lemma 5 and a union bound, ≤ Q_max2^{−t} ≤ 2^{−10}.
(Formally, by Lemma 5 the state of (j, q) after FS is Σ_{λ,j} N^{−1}|α_j(λ)|² |j⟩⟨j| ⊗
|φ_λ⟩⟨φ_λ|, the marginal of the same expression with an added classical register
|λ⟩⟨λ| that the algorithm never reads; adjoining it changes no distribution, and the
genie run reads it in place of λ̂.)
The last run is ideal in the sense of §4. In it, by induction over decisions
(Lemma 9), the invariant holds at the final test unless one of these events
occurs in one of the ≤ 2n+5 decisions: a stage abort (Lemma 7: ≤ e^{−L_0/12} +
ℓe^{−8√n} ≤ (√n+2)e^{−8√n}, as L_0/12 ≥ 17B/12 ≥ B/4), a selection shortfall
(≤ e^{−m/4} ≤ e^{−5120}n^{−512}), or a wrong vote (Lemma 8 with the schedule of §5:
≤ e^{−10}/n). Labels entering each vote are i.i.d. uniform on I_R and the qubits
are exact |φ_λ⟩ in product (Lemma 6), as the lemmas require. With x = √n ≥ 8,
(2x²+5)(x+2)e^{−8x} is decreasing and below 10^{−20} at x = 8, and
(2n+5)e^{−10}/n ≤ 2.1e^{−10} < 10^{−4}; so these events have total probability
≤ 10^{−3}. Final test: with W = 1, s ≡ a. With W = 2,
s ∈ {a, a+1}; if s = a every X-test gives + (baseline proof), else each gives +
with probability 1/2 independently, so the output is wrong with probability
≤ 2^{−10}. Altogether failure ≤ 0.2268 + 2^{−n} + 2·2^{−10} + 10^{−3} + 2^{−10} < 0.231,
so success > 0.769 > 3/4. ∎

## 7. Resources and growth indices

Let L* = 17^ℓΛ; every run has L_0 ≤ L*, and Σ_i L_i ≤ 2L_0. With ℓ ≤ √n + 1,
L* ≤ 17·17^{√n}(34·2^{√n} + 8192(log n + 11)) ≤ 17·8226·34^{√n} = 139842·34^{√n},
because log n + 11 ≤ 2^{√n} for n ≥ 64 (17 ≤ 256 at n = 64, and the right side grows
faster). Since 34^8 = 1785793904896 < 2199023255552 = 2^{41}, 34 < 2^{41/8}, so
L* < 139842·2^{(41/8)√n} = O(2^{(41/8)√n}).
Also t = ⌈log Q_max⌉ + 10 = O(√n), so μ = b = O(n).

**Samples.** Each decision uses 3L_0 ≤ 3L* FS copies; the final test uses ≤ 10.
On every branch Q ≤ 3(2n+5)L* + 10 = Q_max = O(n·2^{(41/8)√n}).

**Quantum space.** Live sieve qubits ≤ L_0 ≤ L* (stage-0 rejects are measured at
once; stages work in place), plus one source copy (n+1 qubits), one control
qubit, the gradient (b qubits) and O(n) adder ancillas:
S_Q ≤ L* + O(n) = O(2^{(41/8)√n}).

**Classical space.** Labels (n+1 bits each), bucket keys and a merge-sort buffer
for ≤ L* items: O(nL*) bits; parameters, counters and the gate currently being
generated: O(n). No circuit is stored. S_C = O(n·2^{(41/8)√n}).

**Total work.** All allocated bits and qubits number M_A = S_C + S_Q =
O(n·2^{(41/8)√n}), so every indexed access and every classically addressed gate
pays ⌈log(M_A + 2)⌉ = O(√n) ≤ O(n). Charges:
* FS (one copy): source n+1; μ = O(n) rounds, each O(n) gates and measurements
  (adder mod N, A_z on b qubits, H) with O(n) address cost each, and O(n²) classical
  operations for 2^i mod N and z; λ̂ by one O(n)×O(n)-bit product: O(n³) per copy.
* Sieve stage i: bucket keys O(n) per item; stable merge sort of L_{i−1} records
  of O(n) bits: O(L_{i−1} log L_{i−1}) comparisons/moves of O(n) bits, each with
  O(n) address cost, and log L_{i−1} = O(√n): O(L_{i−1}n³); per pair one CNOT,
  one measurement, d, and a t×(n+1)-bit product: O(n²). Per run: O(L* n³)
  for stages, plus 3L_0 FS copies: O(L* n³).
* Vote: per qubit r_k, z_k (O(n·b) bit operations) and A_{z_k} (O(n) gates,
  O(n) address each): O(n²); per decision O(mn²).
* Final test: ≤ 10 baseline tests, O(n³) each. Gradient preparation: O(n²).
  Parameter arithmetic: O(n²).
Summing over ≤ 2n+5 decisions, T = O(n·L*·n³) = O(n⁴·2^{(41/8)√n}).
For n < 64 all four quantities are bounded by absolute constants, absorbed by
the hidden constants.

**Envelopes and indices.** B_T = 2^{(41/8)√n}n⁴, B_C = 2^{(41/8)√n}n,
B_Q = 2^{(41/8)√n}, B_samples = 2^{(41/8)√n}n. For each, log B = (41/8)n^{1/2} +
r log n with r ∈ {4, 1, 0, 1}, so log log B = (1/2)log n + log(41/8) + o(1) and
g(B) = limsup_{n→∞} log log max{4, B(n)} / log n = 1/2 exactly (B(n) ≥ 4 for all n ≥ 1,
and the limit exists). Multiplicative constants do not change
this. All four bounds hold jointly for the one configuration ISIEVE, on every
branch, together with success ≥ 3/4 (Theorem 1). The score vector is [1/2].

## 8. Fractional error tolerance

The analysis assumes that every acquired copy is an independent ideal coset
state ρ_s. It therefore establishes the malformed-sample fractional tolerance
epsilon(n) = 0 jointly with the four bounds for the same algorithm. No positive
tolerance is claimed; this is not a proof that the algorithm tolerates none.
