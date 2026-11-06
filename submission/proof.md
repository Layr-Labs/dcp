# Interval-uniform offset sieve with exact Fourier windowing

This file specifies one algorithm, called **the offset sieve**, and proves for
every N ≥ 2 and every s in Z/NZ that it outputs the entire s with unconditional
probability greater than 0.9, jointly with the worst-case bounds

$$
T(N,s)=O\!\left(2^{16\sqrt n}\,n^{9}\right),\quad
S_C(N,s)=O\!\left(2^{8\sqrt n}\,n^{3}\right),\quad
S_Q(N,s)=O\!\left(2^{8\sqrt n}\,n^{2}\right),\quad
Q(N,s)=O\!\left(2^{16\sqrt n}\,n^{4}\right),
$$

where n = ceil(log₂ N). All hidden constants are absolute. The method is a
variant of Kuperberg's subexponential sieve (G. Kuperberg, *A subexponential-time
quantum algorithm for the dihedral hidden subgroup problem*, SIAM J. Comput.
35(1), 2005). No novelty is claimed for the asymptotic index. The argument below
is self-contained for arbitrary N (not only powers of two): label uniformity is
maintained exactly by classical rejection, and the Fourier transform over Z/NZ is
replaced by an exactly-uniform window of a transform over Z/2^mZ.

## 0. Notation and two standard inequalities

* 2^{n−1} < N ≤ 2^n and n ≥ 1. e(θ) = exp(2πiθ). For θ in R, ‖θ‖ is the distance
  from θ to the nearest integer (circular distance on R/Z).
* For an integer k, the **phase qubit with label k** is
  |φ_k⟩ = (|0⟩ + e(ks/N)|1⟩)/√2. It depends only on k mod N.
* I_ℓ = {−ℓ, …, ℓ} ⊂ Z, of size λ = 2ℓ+1.
* D(ρ,σ) = ½‖ρ−σ‖₁ (trace distance). For unitaries U,V and any state ρ,
  D(UρU†,VρV†) ≤ ‖U−V‖ (operator norm).
* (C) Chernoff: if X is a sum of independent {0,1} variables and E X ≥ μ > 0,
  then Pr[X < μ/2] ≤ exp(−μ/8).
* (H) Hoeffding: for r i.i.d. {0,1} variables with mean p and sum X,
  Pr[|X/r − p| > η] ≤ 2 exp(−2rη²).

## 1. Parameters

The controller computes the following from N alone (O(√n)-bit or O(n)-bit integer
arithmetic).

* **P1.** b = ceil(√n), β = 2^b.
* **P2 (schedule).** ℓ₀ = ⌊(N−1)/2⌋. While ℓ_i ≥ 1: λ_i = 2ℓ_i+1,
  β_i = min(β, λ_i), w_i = ⌊λ_i/β_i⌋ ≥ 1, ℓ_{i+1} = ⌊(w_i−1)/2⌋. S is the first
  index with ℓ_S = 0. Stage-i blocks are
  J_{i,q} = {−ℓ_i + q w_i, …, −ℓ_i + (q+1)w_i − 1} for q = 0, …, β_i − 1: disjoint
  sets of w_i consecutive integers inside I_{ℓ_i}. Their union is the covered
  set C_i.
* **P3.** Targets T_j = 2^j mod N for j = 0, …, n. r = 800(n+1), F = 2r.
* **P4.** F_i = F·32^{S−i} and M_i = 16β(n+1)F·128^{S−i} for 0 ≤ i ≤ S;
  K = M₀ + (n+1)F₀.
* **P5.** D = ceil(log₂ K) + 9, δ = 2^{−D}, m = n + D + 1, M = 2^m,
  c = ⌊2^{n+1}/N⌋, R = 8K·2^D.
* **P6.** E = ceil(log₂ R) + 7, ε_Q = 2^{−E}, t = ceil(log₂ K) + 7.
* **P7.** A fixed table of 32 rationals γ_c(u), γ_s(u) (u = 0, …, 15), each with
  denominator 100, satisfying |γ_c(u) − cos(2πu/16)| ≤ 1/100 and
  |γ_s(u) − sin(2πu/16)| ≤ 1/100.

Elementary facts:

* **F1.** β_i w_i ≥ λ_i/2, because λ_i/β_i ≥ 1 and ⌊x⌋ ≥ x/2 for x ≥ 1.
* **F2.** λ_{i+1} = 2⌊(w_i−1)/2⌋+1 ≤ w_i ≤ λ_i/β_i.
* **F3.** S ≤ √n + 1. Indeed λ₀ ≤ N ≤ 2^n. While λ_i > β we have β_i = β, so
  λ_i ≤ 2^{n−bi} by F2. If i₀ stages have λ_i > β, then 2^b < λ_{i₀−1} ≤ 2^{n−b(i₀−1)},
  so i₀ < n/b ≤ √n. A stage with 3 ≤ λ_i ≤ β has β_i = λ_i, w_i = 1 and
  ℓ_{i+1} = 0, so at most one such stage follows.
* **F4.** c ≥ 2 and 2^n ≤ cN ≤ 2^{n+1}: ⌊x⌋ ≥ x − 1 gives cN ≥ 2^{n+1} − N ≥ 2^n.
  Hence cN/M ∈ [δ/2, δ], and cN ≤ 2^{n+1} ≤ M.

## 2. The algorithm

Any ABORT outputs 0 and halts. Whenever an element is discarded its qubit is
measured and released.

**Step 0 (compile).** Write QFT_M|z⟩ = M^{−1/2} Σ_j e(jz/M)|j⟩ on m qubits with the
textbook circuit (Nielsen–Chuang, Section 5.1): Hadamards, controlled phases
CR_d = diag(1,1,1,e(2^{−d})) for 2 ≤ d ≤ m, and a final bit-reversal of SWAPs.
Each CR_d is (P(θ/2)⊗P(θ/2))·CNOT·(I⊗P(−θ/2))·CNOT with θ = 2π/2^d and
P(φ) = diag(1, e^{iφ}); on |a,b⟩ this gives phase e^{iθ(a+b−(a⊕b))/2} = e^{iθab}.
P(±π/4) = T^{±1} is exact. For 3 ≤ d ≤ m compile, once, Clifford+T sequences
W_{d,±} with ‖P(±π/2^d) − e^{iγ}W_{d,±}‖ ≤ ε′ := ε_Q/(2m²) for some phase γ, by
the Solovay–Kitaev algorithm (Section 9). Store the 2m sequences. Substituting
them gives a Clifford+T circuit Ṽ. At most 3m²/2 single-qubit factors are
replaced and each error is at most ε′; telescoping over products of unitaries
gives ‖Ṽ − e^{iγ}QFT_M‖ ≤ ε_Q for one global phase γ. The single-qubit phases
multiply into that global phase because every replaced gate is applied
unconditionally.

**Step 1 (labelled phase qubits).** Repeat R times. Acquire one source copy
(qubit P, n-qubit register X). Adjoin m−n fresh |0⟩ qubits as high-order bits of
X, apply Ṽ, and measure X, obtaining j ∈ [0,M). Compute k = ⌊jN/M⌋ and
a_k = ⌈kM/N⌉. If j − a_k ≥ c, discard P. Otherwise call the copy *kept with label
k*. While fewer than K elements have been stored, give the next stored element
position p: for p < (n+1)F₀ its role is A_j with j = ⌊p/F₀⌋; otherwise B. Let
T = T_j for A_j and T = 0 for B. Let o be the representative of k − T modulo N
in (−N/2, N/2]. If o ∉ I_{ℓ₀} (possible only for even N and o = N/2), discard P
without consuming the position. Otherwise store (role, offset o, qubit P). The
label of an element with role A_j and offset a is T_j + a. The label of a B
element with offset b is b. If fewer than K elements are stored after R copies,
ABORT.

**Step 2 (sieve).** For i = 0, …, S−1 the input has lists A₀, …, A_n of exactly
F_i elements and B of exactly M_i elements, with offsets in I_{ℓ_i}.

1. Discard every element whose offset is outside C_i. Record the block index q of
   every other element.
2. In each block, process the covered A elements in the fixed order (j, list
   position). Pair each with the next unused B element of the same block in list
   order. If they run out, ABORT. Pair the remaining B elements of the block
   consecutively; an odd leftover is discarded.
3. For each pair (first element offset u and qubit P₁, second offset v and qubit
   P₂): apply CNOT with control P₁ and target P₂, and measure P₂ to get Z. If Z = 0,
   discard. If Z = 1 let d = u − v. If |d| > ℓ_{i+1}, discard. Otherwise
   prepare t fresh qubits, apply H, and measure them, obtaining an integer U ∈
   [0, 2^t). Accept iff U(w_i − |d|) < 2^t(w_i − ℓ_{i+1}). An accepted pair yields
   an output element with offset d, qubit P₁, and the first element's role.
4. If some A_j has fewer than F_{i+1} outputs or B has fewer than M_{i+1},
   ABORT. Otherwise keep the first F_{i+1} (respectively M_{i+1}) outputs in
   production order and discard the rest.

**Step 3 (estimation).** Each A_j now holds F = 2r elements with offsets in
I₀ = {0}. On the first r qubits apply H and measure; let h_X be the number of
outcomes 0. On the other r apply S† then H and measure; let h_Y be the number of
zeros. Set ĉ_j = 2h_X/r − 1 and ŝ_j = 2h_Y/r − 1. Let β_j = u*/16, where u* ∈
{0, …, 15} maximizes ĉ_jγ_c(u) + ŝ_jγ_s(u), taking the smallest maximizer.

**Step 4 (reconstruction).** Set θ_n = β_n. For j = n−1 down to 0, let θ_j be the
candidate among θ_{j+1}/2 and θ_{j+1}/2 + 1/2 with smaller ‖· − β_j‖, taking the
first on ties. Output s* = ⌊Nθ₀ + 1/2⌋ mod N. All θ_j are dyadic rationals with at
most n+5 bits.

## 3. The ideal process

The **ideal process** differs from the algorithm in three replaced components:
(i) Ṽ is replaced by exact QFT_M. (ii) In Step 1 the qubit P of a kept copy with
label k is replaced by exactly |φ_k⟩. (iii) Each Step-2 coin uses a uniform
real V ∈ [0,1): accept iff V < q := (w_i − ℓ_{i+1})/(w_i − |d|). Note q ≤ 1 when
|d| ≤ ℓ_{i+1}. Section 4 bounds the effect of these replacements.

**Lemma 1 (exact Fourier window).** Under exact QFT_M, for every s, j is uniform
on [0,M) and independent of the source's hidden x. For every k ∈ {0, …, N−1},
Pr[kept with label k] = c/M. Hence Pr[kept] = cN/M ∈ [δ/2, δ], and conditioned on
being kept the label is uniform on Z/NZ. For a kept copy the actual state of P
is within trace distance πδ of |φ_k⟩.

*Proof.* For a component |ψ_x⟩ = (|0,x⟩ + |1,y⟩)/√2 with y = (x+s) mod N < N ≤ M,
QFT_M and measuring j gives probability ½·(1/M) + ½·(1/M) = 1/M. The post-state of P
is ∝ e(jx/M)|0⟩ + e(jy/M)|1⟩, that is, (|0⟩ + e(j(y−x)/M)|1⟩)/√2 up to a
global phase. For each k, the integers j ∈ [a_k, a_k + c) satisfy jN ≥ kM and
jN < kM + cN ≤ (k+1)M, since j < kM/N + c and cN ≤ M by F4. They therefore have ⌊jN/M⌋ = k, lie in
[0, M), and are kept. No other j with ⌊jN/M⌋ = k is kept. This gives exactly c
kept values per k. For a kept j, 0 ≤ jN/M − k < cN/M ≤ δ. If y − x = s, the
phase error is j s/M − ks/N = (s/N)(jN/M − k) ∈ [0, δ). If y − x = s − N, it is
(s/N − 1)(jN/M − k) − k, which is ≡ (s/N−1)(jN/M − k) ∈ (−δ, 0] mod 1. For pure
qubits (|0⟩+e(α)|1⟩)/√2 and (|0⟩+e(α′)|1⟩)/√2 the overlap has modulus
|cos π(α−α′)|. Their trace distance is |sin π(α−α′)| ≤ π‖α−α′‖ < πδ. The
actual state is a mixture of these over x, so convexity gives the claim. ∎

**Lemma 2 (combination).** For integers k₁,k₂, applying CNOT (control first) to
|φ_{k₁}⟩|φ_{k₂}⟩ and measuring the target gives Z = 0 and Z = 1 with
probability ½ each, independently of k₁, k₂ and s. On Z = 1 the control is
|φ_{k₁−k₂}⟩ up to global phase. On Z = 0 it is |φ_{k₁+k₂}⟩.

*Proof.* Write θ_i = 2πk_is/N. The state ½(|00⟩ + e^{iθ₂}|01⟩ + e^{iθ₁}|10⟩ +
e^{i(θ₁+θ₂)}|11⟩) becomes ½[(|0⟩ + e^{i(θ₁+θ₂)}|1⟩)|0⟩ +
e^{iθ₂}(|0⟩ + e^{i(θ₁−θ₂)}|1⟩)|1⟩]. ∎

**Lemma 3 (rejection to a uniform interval).** Let J be a set of w ≥ 1
consecutive integers and ℓ′ = ⌊(w−1)/2⌋. Let u, v be uniform on J and Z a fair
bit. Let V be uniform on [0,1), with u, v, Z and V independent. Let d = u − v and
let Acc be the event
Z = 1 ∧ |d| ≤ ℓ′ ∧ V < (w−ℓ′)/(w−|d|). Then Pr[Acc ∧ d = e] = (w−ℓ′)/(2w²) for
every e ∈ I_{ℓ′}. Hence d is uniform on I_{ℓ′} given Acc, and
p_w := Pr[Acc] = (2ℓ′+1)(w−ℓ′)/(2w²) ≥ 1/4.

*Proof.* Pr[d = e] = (w−|e|)/w² for |e| ≤ w−1. Multiplying by ½ and by
(w−ℓ′)/(w−|e|) ≤ 1 gives a value independent of e. If w = 2ℓ′+1, then
(2ℓ′+1)(w−ℓ′)/w² = (w+1)/(2w) ≥ ½. If w = 2ℓ′+2 ≥ 2, then it is
(w−1)(w+2)/(2w²) ≥ ½ because w² + w − 2 ≥ w². ∎

**Lemma 4 (invariant).** Let 𝒢_i be the σ-algebra generated by every Step-1
keep/discard decision and role, every block index from stages before i, all Z
outcomes, all acceptance indicators, and all selection and abort events before
stage i. Condition on 𝒢_i and on no abort before stage i. In the ideal process
the stage-i input offsets are then independent, each uniform on I_{ℓ_i}, and the
quantum memory is the tensor product of |φ_label⟩ over the input elements.

*Proof.* For i = 0, Lemma 1 gives each kept label uniform on Z/NZ, independent
of everything earlier because copies are fresh. The role is a function of
earlier decisions. The map k ↦ o is a bijection Z/NZ → (−N/2, N/2] ∩ Z, and
I_{ℓ₀} = (−N/2, N/2) ∩ Z for both parities of N. Thus a stored offset is uniform
on I_{ℓ₀}. The ideal process stores |φ_k⟩ = |φ_{T+o}⟩.

Assume the claim for i. Conditioned also on the stage-i block indices, covered
offsets are independent and uniform on their blocks. These indices determine the
pairing. Each pair has (u, v) i.i.d. uniform on one block of size w_i, a Z that
is a fair bit independent of all labels by Lemma 2, and a fresh V. These tuples
are independent across pairs. By Lemma 3, conditioning on all acceptance
indicators makes accepted d's independent and uniform on I_{ℓ_{i+1}}. Step 2.4
selects using only indicators and production order. For an A_j–B pair, Lemma 2
gives the label (T_j+u) − v = T_j + d. For a B–B pair it gives u − v = d. ∎

**Lemma 5 (no abort in the ideal process).** Pr[ABORT] ≤ e^{−K/4} + 10^{−6}.

*Proof.* *Step 1.* Copies are independent. Each yields a stored element with
probability (cN/M)(1 − [N even]/N) ≥ δ/4, the same for every role. The expected
count is at least Rδ/4 = 2K, so by (C) Pr[count < K] ≤ e^{−K/4}.

*Stage i.* Write F_tot = (n+1)F_i. By P4, M_i = 16β(n+1)F·128^{S−i} ≥
16β·F_tot ≥ 8β(F_tot+1). By Lemma 4 the number X_q of B offsets in block q is
Binomial(M_i, w_i/λ_i). Its mean is μ_q ≥ M_i/(2β) by F1. Let G be the event
X_q ≥ μ_q/2 for all q. By (C) and a union bound, Pr[¬G] ≤ β e^{−M_i/(16β)}.
On G every block has X_q ≥ M_i/(4β) ≥ 2(F_tot+1) B elements. That exceeds the
number of A elements in the block, so step 2.2 does not abort. The B–B pair
count is at least
Σ_q (X_q − A_q − 1)/2 ≥ (M_i/4 − F_tot − β)/2 ≥ (M_i/4 − M_i/8)/2 = M_i/16,
using Σ_q μ_q = M_iβ_iw_i/λ_i ≥ M_i/2 (F1). Pair successes are independent with
probability p_{w_i} ≥ 1/4 (Lemmas 2–4), so by (C) fewer than M_i/128 = M_{i+1}
outputs has probability at most e^{−M_i/512}. For each j, Lemma 4 makes the
number of covered A_j elements Binomial with mean ≥ F_i/2 (F1). It is below F_i/4
with probability at most e^{−F_i/16}. On G each covered A element is paired, and
the successes are independent with probability ≥ 1/4. So fewer than
F_i/32 = F_{i+1} outputs has conditional probability at most e^{−F_i/128}. Here
M_i/(16β) ≥ (n+1)F ≥ 3200(n+1), M_i/512 ≥ 50β(n+1)² ≥ 100(n+1), F_i/16 ≥ 100(n+1) and F_i/128 ≥ 12.5(n+1).
Summing over at most √n + 1 stages (F3) with β ≤ 2^{√n+1} gives less than 10^{−6}
for every n ≥ 1. ∎

**Lemma 6 (one estimate).** For copies of |φ_T⟩, let α ∈ [0,1) be the
representative of Ts/N modulo 1. Then H followed by measurement gives 0 with probability
(1+cos 2πα)/2. S† then H gives 0 with probability (1+sin 2πα)/2. If
|ĉ − cos 2πα| ≤ 1/10 and |ŝ − sin 2πα| ≤ 1/10, the chosen β satisfies
‖β − α‖ < 5/32.

*Proof.* The probabilities are |1 + e^{iθ}|²/4 and |1 − ie^{iθ}|²/4 with θ = 2πα.
Write u_β = (cos 2πβ, sin 2πβ) and v̂ = (ĉ, ŝ). Then ‖v̂ − u_α‖₂ ≤ √2/10 <
0.1415, and the table value differs from ⟨v̂, u_β⟩ by at most
(|ĉ| + |ŝ|)/100 ≤ 0.02. Some grid point β₀ has ‖β₀ − α‖ ≤ 1/32, so
⟨v̂, u_{β₀}⟩ ≥ cos(π/16) − 0.1415 ≥ 0.838. The maximizer therefore has
⟨v̂, u_β⟩ ≥ 0.798 and cos(2π‖β−α‖) = ⟨u_α, u_β⟩ ≥ 0.656 > 0.556 > cos(5π/16). ∎

In the ideal process, Lemma 4 makes the qubits measured for target j in Step 3
exactly 2r independent copies of |φ_{T_j}⟩. By (H) with η = 1/20, each of the
2(n+1) estimates fails its 1/10 bound with probability at most 2e^{−r/200}. The
total is at most 4(n+1)e^{−4(n+1)} ≤ 8e^{−8} < 0.003 for n ≥ 1. On success
‖β_j − α_j‖ < 5/32 for all j, where α_j is the representative of 2^j s/N mod 1
in [0,1), because T_j ≡ 2^j (mod N).

**Lemma 7 (reconstruction).** If ‖β_j − α_j‖ < 5/32 for 0 ≤ j ≤ n, then
‖θ_j − α_j‖ ≤ (5/32)2^{−(n−j)} for all j, and s* = s.

*Proof.* The case j = n holds. Suppose ‖θ_{j+1} − α_{j+1}‖ ≤ ε ≤ 5/32. The
candidates {θ/2, θ/2+½} and {α/2, α/2+½} match in pairs within ε/2. If |θ−α| ≤ ε
this is immediate. Otherwise θ − α = ±(1−e) with e ≤ ε, and θ/2 is within e/2 of
α/2 ± ½. Because 2α_j ≡ α_{j+1}, α_j is one of α_{j+1}/2 and α_{j+1}/2 + ½. One
candidate is within ε/2 ≤ 5/64 of α_j, hence within 5/32 + 5/64 = 15/64 of β_j.
The other is within ε/2 of α_j + ½, hence at least ½ − 15/64 = 17/64 from β_j.
The correct candidate is chosen. Finally ‖θ₀ − s/N‖ ≤ (5/32)2^{−n} < 2^{−n−1} ≤
1/(2N), so Nθ₀ is within less than ½ of s modulo N, and rounding returns s. ∎

**Ideal success.** Pr_ideal[s* ≠ s] ≤ e^{−K/4} + 10^{−6} + 0.003 < 0.004.

## 4. From the ideal process to the algorithm

*(i) and (ii): Fourier window.* Each copy is a fresh product factor ρ_s. Before
any later operation, the actual algorithm maps it to the cq-state
Φ(ρ_s) = Σ_j |j⟩⟨j| ⊗ (state of P). Let Φ_id be the corresponding map in the
ideal process. By the operator-norm bound for Ṽ, changing Ṽ to QFT_M moves the
cq-state by at most ε_Q in trace distance. Replacing kept post-states by
|φ_k⟩ moves it by Σ_{kept j}(1/M)·πδ = πδ·cN/M ≤ πδ² (Lemma 1; trace distance of
block-diagonal cq-states is the probability-weighted sum). All later processing
is a fixed instrument on the tensor product with the rest of memory. A hybrid
argument over the R copies changes the output distribution by at most
R(ε_Q + πδ²). By P5–P6, Rε_Q ≤ 1/128 and Rπδ² = 8πK·2^{−D} ≤ 8π/512 < 0.05.

*(iii): coins.* Let V be uniform on [0,1) and U = ⌊2^tV⌋. U is exactly the t
fair coins of step 2.3. For integer U, U(w−|d|) < 2^t(w−ℓ′) iff U/2^t < q. The
ideal coin is V < q. The two disagree only if q ∈ (U/2^t, (U+1)/2^t), which has
probability at most 2^{−t}. There are at most K coin uses, because there are at
most ½Σ_i(M_i + (n+1)F_i) ≤ K pairs. Coupling therefore changes the output
distribution by at most K2^{−t} ≤ 1/128.

**Theorem (correctness).** For every N ≥ 2 and s, Pr[s* = s] ≥ 1 − 0.004 −
1/128 − 0.05 − 1/128 > 0.92 > 2/3. There is no postselection: aborts count as
failures and were included.

## 5. Resources (every execution branch)

Bounds on the parameters: β ≤ 2^{√n+1}, and 128^S ≤ 2^{7√n+7} by F3. So

$$
K \le 17\beta(n+1)F\cdot128^{S} = 27200\,\beta(n+1)^2 128^{S}
\le 2^{23}(n+1)^2\,2^{8\sqrt n},
$$

with 2^D ≤ 1024K and R = 8K·2^D ≤ 2^{13}K² ≤ 2^{59}(n+1)^4 2^{16√n}. Hence
log₂ R, D, E, t = O(√n + log n) and m = n + D + 1 = O(n).

**Q.** Step 1 acquires exactly R copies, and no other step acquires copies, so
Q ≤ R = O(2^{16√n} n^4). This counts discarded and aborted copies.

**S_Q.** Step 1 holds at most K stored qubits plus m+1 working qubits. Step 2
holds at most K element qubits plus t coin qubits, and Step 3 holds fewer. So
S_Q ≤ K + m + t + 1 = O(2^{8√n} n²).

**S_C.** Each stored element record holds a role (O(log n) bits), an offset
(n+1 bits) and a qubit index (O(log K) = O(n) bits). K records plus a sorting
buffer of the same size use O(Kn) bits. Parameters, counters, U, h_X, h_Y and the
θ_j use O(n) bits. The P7 table is constant size. The SK table stores 2m
sequences of length O(n²) (below), O(n³) bits. Total
S_C = O(Kn) = O(2^{8√n} n³).

**T.** Every classical indexed access and every classically addressed gate pays
⌈log₂(S_C+S_Q+2)⌉ = O(√n). Per Step-1 copy, Ṽ has O(m²) Hadamard/CNOT/SWAP
gates and O(m²) compiled sequences. Each sequence has length
O(log^{3.97}(1/ε′)) = O(n^{1.99}) because log(1/ε′) = E + O(log m) = O(√n).
Emitting each gate from the stored table and addressing it costs O(√n), so one
copy costs O(n^{4.5}). The source cost n+1, the m measurements, and the
arithmetic computing k and a_k are O(m²) per copy. Step 1 therefore costs
O(R n^{4.5}) = O(2^{16√n} n^{8.5}). Step 0 costs poly(n) bit operations
(Section 9), which is O(2^{16√n}). Each sieve stage sorts O(K) records by block
with O(K log K) comparisons of O(n)-bit keys, performs O(K) CNOTs and
measurements, and uses O(K) coin groups of t qubits plus O(n)-bit comparisons.
Over S = O(√n) stages this is O(K n^3) = O(2^{8√n} n^5). Steps 3–4 cost
O(n² log n). Hence

$$
T(N,s) = O\!\left(2^{16\sqrt n}\, n^{9}\right).
$$

All constants are absolute, and the enlarged constants cover the finitely many
small n.

## 6. Growth indices

With g(B) = limsup log₂ log₂ max{4,B(n)} / log₂ n:

* B_T = 2^{16√n} n^9: log₂ B_T = 16√n + 9 log₂ n, so g = 1/2.
* B_C = 2^{8√n} n^3 and B_Q = 2^{8√n} n^2: log₂ B = 8√n + O(log n), so g = 1/2.
* B_samples = 2^{16√n} n^4: g = 1/2.

Each index is 1/2 for every positive choice of the hidden outer constant. The
inner exponent coefficients 16 and 8 are explicit, as required by the structured
family. The resource index vector is [1/2, 1/2, 1/2, 1/2]. The published numeric
score is the time index 1/2.

## 7. Fractional error tolerance

The analysis assumes that every acquired copy is an independent ideal coset
state ρ_s. It establishes the clean-input guarantee epsilon(n) = 0 jointly with
all four bounds above, for this same algorithm and parameter choice. No positive
tolerance is claimed. This is not a claim that positive tolerance is impossible.

## 8. What is used from outside

The only external results are standard inequalities (C) and (H), the textbook
QFT_M circuit, and the Solovay–Kitaev theorem in Section 9. Lemmas 1–7 are proved
in full above. Kuperberg's paper is credited for the sieve idea. Its analysis is
not used.

## 9. Gate synthesis (Solovay–Kitaev)

Applicability: H and T generate a dense subgroup of SU(2) modulo global phase
(Boykin–Mor–Pulver–Roychowdhury–Vatan 1999; Nielsen–Chuang Section 4.5.3).
Adding the inverses T† and S† = T⁶ closes the set under inverses. The
Solovay–Kitaev theorem in the algorithmic form of C. M. Dawson and
M. A. Nielsen, *The Solovay–Kitaev algorithm*, Quantum Inf. Comput. 6(1):81–95
(2006), main theorem, applies to such a finite inverse-closed set. For any target
in SU(2) and ε > 0 it produces a sequence of length O(log^{c}(1/ε)) with
c = log 5/log(3/2) < 3.97 approximating the target within ε up to global phase,
in classical time O(log^{2.71}(1/ε)) operations on 2×2 matrices. The same
construction appears in Kitaev–Shen–Vyalyi, *Classical and Quantum Computation*,
AMS 2002, Section 8.3. Running the arithmetic at O(log(1/ε))-bit fixed-point
precision gives poly(log(1/ε)) bit operations per target. We call it once for each
of the 2m targets P(±π/2^d) with ε′ = ε_Q/(2m²). Here log(1/ε′) = O(√n), so Step 0
costs poly(n) bit operations and O(n³) stored bits. Only the global-phase-free
operator-norm guarantee is used, as explained in Step 0.
