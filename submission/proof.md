# ROB+: robust shadow scoring with 33/100 adaptive malformed-copy tolerance (ceiling 1/3 for even N) and O(n) copies

This file is the complete proof of all five claims in `submission.json`. It
describes one algorithm, **ROB+**, with one fixed parameter rule, and proves for
every integer N ≥ 2, every s ∈ Z/NZ, with n = ceil(log₂ N), and every adversary
of the error model of Section 5 (which contains the clean problem as the
adversary that corrupts nothing):

* the output equals s with unconditional probability at least 7/8 (> 2/3);
* total work T = O(2^n n² log n);
* peak classical space S_C = O(n²) bits;
* peak quantum space S_Q = O(n) qubits;
* acquired source copies: exactly Q = 2^{19}(n+4) = O(n) on every branch;
* fractional error tolerance ε(n) = 33/100: at most floor(33Q/100) copies may be
  malformed, at adversarially and adaptively chosen positions, with arbitrary,
  possibly entangled contents.

All constants are absolute (independent of N, s, the adversary and all outcomes).
Every loop of ROB+ has a length fixed by n and N alone, so the four resource bounds
hold on every execution branch whatever the copies contain. There are no aborts
and no restarts. Logarithms are base 2 unless written ln.

**Near-optimality (Section 6.3, Proposition U; a proved remark, not a claim).** In
this error model no algorithm with a fixed copy count can tolerate any fraction
ε > 1/3 for even N once Q > ln 6/(2(ε − 1/3)²): the instances s and s + N/2 can be made
indistinguishable. The claimed 33/100 is 99% of this ceiling.

**Idea.** Each copy yields a classical record (û, m′, b): its Fourier label û
(estimated exactly, w.h.p.), a uniformly random phase offset m′/8 and one ±1 outcome
(−1)^b. For every candidate t the quantity (−1)^b cos(2π(ût/N − m′/8)) is an
estimator of (1/2)·[t = s] (Lemma C). The new ingredient is Lemma M: because m′ is
drawn by the algorithm *after* the copy has been delivered and its label estimated,
a malformed copy, whatever its state, has conditional expected contribution at least
−(1 + 2η) to the score difference S(s) − S(t) (not the worst-case −2R of a single
outcome). A clean copy adds 1/2 to that expectation. So the expected margin per copy
is (1 − ε)/2 − ε, positive for every ε < 1/3, and a one-sided Azuma–Hoeffding bound
handles the adversary's adaptivity.

Notation. frac(φ) ∈ [0,1); |φ|∘ = min_{z∈Z} |φ − z| (circular distance). For an
integer v let

  φ(v) = (|0⟩ + e^{2πi v s/N}|1⟩)/√2   (a *label-v qubit*; only v mod N matters).

bitlength(x) is the number of binary digits of an integer x ≥ 1, so
2^{bitlength(x)} > x and e^{−bitlength(x)} < 2^{−bitlength(x)} < 1/x.
round(z) = floor(z + 1/2).

## 1. Primitive operations (exact Clifford+T)

(The primitives are numbered P1, P2, P5; no other primitive is used, and nothing
outside this file is relied on.) Gates are X, CNOT, H, T, T† and Toffoli, which has an
exact constant-size Clifford+T circuit. Every released qubit is measured and, if its
outcome is 1, reset by X, so each fresh ancilla is exactly |0⟩; this costs O(1) per qubit.

**P1 (controlled modular addition of a constant).** For a classical constant
a ∈ [0, N), let g_a(y) = (y + a) mod N for y < N and g_a(y) = y for
N ≤ y < 2^n (a permutation of [0, 2^n) with inverse g_{(N−a) mod N}).
*Constant adder:* |y⟩|0⟩ ↦ |y⟩|(y + c) mod 2^n⟩ for a classical c: compute the carries
of y + c into n ancillas (carry_{i+1} = MAJ(y_i, c_i, carry_i), one Toffoli/CNOT/X group
per bit), write the sum bits by CNOTs, and uncompute the carries by running the carry
circuit backwards (they depend only on y). A comparison flag [y ≥ c] is the carry out of
y + (2^n − c), computed and uncomputed the same way. *Out-of-place g_a:* compute
e = [y < N] and f = [y ≥ N − a]; controlled on e, add the constant a if f = 0 and
a − N + 2^n if f = 1, XOR-ed into the output register (sum bits and copies are
written by CNOTs); if e = 0, copy y by CNOTs; uncompute f, e.
*In place:* apply the out-of-place g_a, then the out-of-place g_a^{−1} from the new
register into the old one (which XORs y ⊕ g_a^{−1}(g_a(y)) = 0 into it), and relabel the
wires. *Control:* relabelling wires cannot be controlled, so the controlled g_a is the
in-place construction above applied to the permutation (c, y) ↦ (c, g_a(y)) if c = 1 and
(c, y) if c = 0 of the control c together with y. Its out-of-place circuit runs the
out-of-place g_a with every gate controlled by c (X → CNOT; CNOT → Toffoli; Toffoli → three
Toffolis and one ancilla; on c = 0 its ancillas are never touched), then copies y into the output by
CNOTs controlled by ¬c; its inverse is built the same way from g_a^{−1}, and the final
relabelling is unconditional. Here c is shared, not copied: the out-of-place circuit maps |c⟩|y⟩|w⟩ ↦ |c⟩|y⟩|w ⊕ y′⟩ with y′ = g_a(y) if c = 1 and y′ = y if c = 0; the reverse step applies the circuit of (g_a^{−1})_c, controlled by c itself, from w into y; only the y and w wires are relabelled. In total O(n) gates and O(n) ancillas, all returned to |0⟩, and a uniform generator emits the gate list one gate
at a time in O(n) bit operations from a and N.

**P2 (phase test).** For a qubit (|0⟩ + e^{2πiφ}|1⟩)/√2 and m′ ∈ {0,…,7}, apply
(T†)^{m′} = diag(1, e^{−2πi m′/8}), then H, then measure. Outcome 0 has probability
exactly p_{m′}(φ) = (1 + cos(2π(φ − m′/8)))/2.

**P5 (fair bits).** A fresh |0⟩, H, measurement: an exact fair bit, O(1) work.

**Cost convention.** Let M be the number of allocated bits plus qubits. Section 7
shows M = O(n²), so a classically indexed access or classically addressed gate
costs A = ceil(log₂(M+2)) = O(log n) bit operations for its address (n ≥ 2).
Every gate, measurement, initialisation and classical bit operation below is
charged O(A).

## 2. Source copies as labelled qubits (exact decomposition)

Let χ_k = N^{−1/2} Σ_{y<N} e^{2πiky/N}|y⟩. Then |y⟩ = N^{−1/2} Σ_k e^{−2πiky/N} χ_k and

  |ψ_{x,s}⟩ = (2N)^{−1/2} Σ_k e^{−2πikx/N}(|0⟩ + e^{−2πiks/N}|1⟩) ⊗ χ_k.

Averaging over x removes the k ≠ k′ cross terms, so with u = −k mod N

  ρ_s = (1/N) Σ_{u ∈ Z/NZ} |φ(u)⟩⟨φ(u)| ⊗ |χ_{−u}⟩⟨χ_{−u}|.          (2.1)

Hence a source copy is **exactly** a uniformly random classical label u ∈ Z/NZ
together with the product state φ(u) ⊗ χ_{−u}; all statistics below are computed
in this model by linearity. Since g_a χ_{−u} = e^{2πiua/N} χ_{−u}, the operation
"fresh control |+⟩, then P1 with a = 2^i mod N on the copy's register" maps the
control to (|0⟩ + e^{2πi 2^i u/N}|1⟩)/√2 and leaves the copy unchanged. Repeated
such tests on one copy are independent given u (the register is an exact
eigenvector and every control is fresh).

## 3. Lemma P (phase reconstruction from dyadic multiples)

Let J, r ≥ 1. Suppose that for each level i ∈ {0,…,J} and each m′ ∈ {0,…,7} we
obtain r independent outcomes of P2 with this m′ applied to qubits
(|0⟩ + e^{2πi 2^i φ}|1⟩)/√2, for an unknown real φ. Let Z_{i,m′} be the number of 0
outcomes. Procedure: m_i = the m′ maximising Z_{i,m′} (smallest on ties),
β_i = m_i/8; x_J = β_J; for i = J−1 down to 0, of c₀ = x_{i+1}/2 and
c₁ = x_{i+1}/2 + 1/2 let x_i be the one with smaller |c − β_i|∘ (c₀ on ties).

**Claim.** With probability at least 1 − 16(J+1)e^{−r/200}, |x₀ − φ|∘ < 2^{−J}/8.

*Proof.* Write φ_i = frac(2^i φ). Hoeffding's inequality gives
P(|Z_{i,m′}/r − p_{m′}(φ_i)| ≥ 1/20) ≤ 2e^{−2r/400}; a union bound over the 8(J+1)
pairs gives the failure bound. Assume all deviations are < 1/20.
(a) The nearest grid point m*/8 has |φ_i − m*/8|∘ ≤ 1/16, so
p_{m*} ≥ (1 + cos(π/8))/2 > 0.9619; every m′ with |φ_i − m′/8|∘ ≥ 1/8 has
p_{m′} ≤ (1 + cos(π/4))/2 < 0.8536. The gap exceeds 2/20, so the empirical
maximiser satisfies |β_i − φ_i|∘ < 1/8.
(b) Induction: |x_i − φ_i|∘ < δ_i := 2^{−(J−i)}/8. True for i = J by (a). Let
|x_{i+1} − φ_{i+1}|∘ < δ_{i+1} ≤ 1/8 and write x_{i+1} − φ_{i+1} = e + z, z ∈ Z,
|e| < δ_{i+1}. Since φ_{i+1} = frac(2φ_i), φ_i ≡ φ_{i+1}/2 + w/2 (mod 1) for some
w ∈ {0,1}, and {c₀, c₁} ≡ {φ_{i+1}/2 + e/2, φ_{i+1}/2 + 1/2 + e/2} (mod 1). So one
candidate is within |e|/2 < δ_i of φ_i and the other is at circular distance
> 1/2 − δ_i ≥ 1/2 − 1/16. By (a) the good candidate is within < 1/16 + 1/8 = 3/16
of β_i and the bad one at > 1/2 − 1/16 − 1/8 = 5/16, so the good one is chosen. ∎

All x_i are multiples of 2^{−(J+3)}: the procedure is exact (J+3)-bit integer
arithmetic, O(J²) bit operations. It is defined for **every** count vector, not
only on the success event.

**Corollary P′.** Take J = max(1, n − 2) and φ = a/N for an integer a. Then
N ≤ 2^n ≤ 2^{J+2} (for n ≥ 3, J + 2 = n; for n ≤ 2, 2^n ≤ 4 < 2^3). On the success
event N x₀ differs from a + Nz (some z ∈ Z) by less than N 2^{−J}/8 ≤ 1/2, so
round(N x₀) mod N = a mod N, with no tie. N x₀ is an exact rational with
denominator 2^{J+3}; rounding and reduction mod N cost O(n²) bit operations and
always return a value in [0, N).

## 4. Algorithm ROB+

### 4.1 Parameters

All are integers computed exactly from n (constants in brackets are used only in
the analysis):

* J = max(1, n − 2); L₁ = bitlength(16(J+1)·10⁶); **r₁ = 200 L₁**;
* **Q = 2^{19}(n + 4)**; **q = 16** (angle bits);
* [p_F = 10^{−6}, δ = 1/250, ε = 33/100, τ = 2^{−22}, η = 2π2^{−q} + τ, R = 1 + τ,
  κ = 2R p_F + η].

### 4.2 Cosine table (computed at run time, independent of N)

Let π̃ = 103993/33102. For k = 0, …, 2^q − 1: x̃_k = 2π̃k/2^q (exact rational),
P_k = Σ_{i=0}^{20} (−1)^i x̃_k^{2i}/(2i)! (exact rational arithmetic), and
c_k = round(2^{22} P_k) ∈ Z. Store c_k as a 24-bit two's-complement integer.

**Lemma T.** |c_k/2^{22} − cos(2πk/2^q)| < τ = 2^{−22} for every k, hence
|c_k| ≤ 2^{22}(1 + 2^{−22}) = 2^{22} + 1 < 2^{23}.

*Proof.* 3.1415926 < π < 3.1415927 and 3.14159265301 < π̃ < 3.14159265302 (long
division), so |π − π̃| < 5.31·10^{−8}; with x_k = 2πk/2^q and k < 2^q,
|x_k − x̃_k| < 2·5.31·10^{−8} = 1.062·10^{−7}, and |cos x_k − cos x̃_k| < 1.062·10^{−7} (cos is
1-Lipschitz). Since 0 ≤ x̃_k < 2π̃ < 6.3 and |cos^{(42)}| ≤ 1, Taylor's theorem
with Lagrange remainder (P_k is the Taylor polynomial of degree 41, whose x^{41}
coefficient is 0) gives |cos x̃_k − P_k| ≤ 6.3^{42}/42! < 3.8·10^{33}/(1.4·10^{51})
< 2.8·10^{−18}. Rounding adds at most 2^{−23} < 1.193·10^{−7}. Total
< 1.062·10^{−7} + 2.8·10^{−18} + 1.193·10^{−7} < 2.26·10^{−7} < 2^{−22}. ∎

Write table[k] = c_k/2^{22}. The construction is a fixed finite computation on
rationals of fixed size: it uses an absolute constant number of bit operations
and bits.

### 4.3 Procedure F (label estimation, no lift)

Given an acquired copy: for i = 0..J and m′ = 0..7 perform r₁ phase tests
(Section 2, with a = 2^i mod N) followed by P2 with this m′. Apply Lemma P
(J, r = r₁) and Corollary P′ to the counts to obtain **û ∈ [0, N)**.

### 4.4 Acquisition phase

For j = 1, …, Q:

1. Acquire copy j (cost n+1).
2. Run F on it, giving û_j.
3. Draw 3 fair bits (P5) forming m′_j ∈ {0,…,7}.
4. Apply P2 with m′_j to the copy's first (coset) qubit; let b_j be the outcome.
5. Measure and discard every qubit of the copy and all ancillas.
6. Store the record (û_j, m′_j, b_j).

The order matters for Lemma M: m′_j is drawn after copy j has been delivered and
after F has finished on it.

### 4.5 Scoring phase (classical)

Set Σ_best ← −Q(2^{22} + 1) − 1 (below every possible Σ), best ← 0, and y_j ← 0 for
all j. For t = 0, …, N − 1:

* Σ ← 0. For j = 1, …, Q:
  h_j = floor(2^q y_j / N) ∈ [0, 2^q); k_j = (h_j − 2^{q−3} m′_j) mod 2^q;
  Σ ← Σ + (−1)^{b_j} c_{k_j}; then y_j ← y_j + û_j, and y_j ← y_j − N if y_j ≥ N.
* If Σ > Σ_best: Σ_best ← Σ, best ← t.

Output best. By induction y_j = û_j t mod N while t is processed, so
Σ = 2^{22} S(t) with

  S(t) = Σ_{j=1}^{Q} Z̃_j(t),   Z̃_j(t) = (−1)^{b_j} table[k_j(t)],
  k_j(t) = (floor(2^q (û_j t mod N)/N) − 2^{q−3} m′_j) mod 2^q.

The output is the smallest t maximising S(t); all arithmetic is exact integer
arithmetic.

## 5. Error model (adaptive malformed copies)

Copies are delivered one at a time in acquisition order j = 1, …, Q; Q is fixed
by n before the first acquisition. An **adversary** knows N, s, the full
description of ROB+, and every measurement outcome obtained by ROB+ before copy j
is delivered; it holds an arbitrary private quantum system E which it may measure
and process. Before copy j is delivered it chooses c_j ∈ {clean, malformed}, as a
function of that information and its own outcomes; on every branch at most
floor(εQ) copies are malformed, ε = 33/100.

* A **malformed** copy is an arbitrary (n+1)-qubit system supplied from E. It may
  be in any state, entangled with the rest of E and hence with other malformed
  copies, and may depend on everything listed above. It is not entangled with
  clean copies or with ROB+'s workspace, ancillas or fair-bit qubits.
* A **clean** copy is, at the moment of its delivery, a fresh ρ_s in tensor product
  with everything else (E, all other copies, ROB+'s workspace).
* The adversary interacts with ROB+ only by supplying copies; after delivery it has no
  access to the copy or to ROB+'s quantum or classical systems. All measurements
  (ROB+'s and the adversary's) have countably many outcomes.

ROB+ is not told which copies are malformed. The clean problem is the case in
which no copy is malformed.

**Filtration.** Let H_j be the classical history generated by all outcomes of
ROB+ on copies 1, …, j and all outcomes of the adversary up to and including its
choice c_{j+1} (H_0: the adversary's outcomes up to the choice of c_1; H_Q: all outcomes). Then c_j is
H_{j−1}-measurable and the record (û_j, m′_j, b_j) is H_j-measurable.

**Let L** be the law of the record (û, m′, b) produced by steps 2–4 of 4.4 when
applied to a fresh ρ_s.

**Fact E.** On every history in H_{j−1} with c_j = clean, the conditional law of
the record of copy j is L.

*Proof.* Steps 2–5 for copy j form one fixed instrument {ℰ_r} (r ranging over all
outcomes of the step, including m′_j) acting on copy j and on fresh |0⟩ ancillas
only; it does not depend on the history, because ROB+'s schedule depends only on N
and on outcomes obtained on copy j itself, and ROB+ keeps no quantum state between
copies (step 5). Conditioned on a history h of positive probability with c_j = clean
(outcome sets are countable, so these histories carry all the probability), the joint state when
copy j is delivered is ρ_s ⊗ ω_h, where ω_h is the conditional state of all other
systems. Hence P(r | h) = Tr[(ℰ_r ⊗ id)(ρ_s ⊗ |0…0⟩⟨0…0| ⊗ ω_h)] = Tr[ℰ_r(ρ_s ⊗ |0…0⟩⟨0…0|)],
which is the clean law. ∎

## 6. Correctness

Numerical constants (from π < 22/7 and exact rational bounds; all re-derivable by hand):
τ = 2^{−22} < 2.385·10^{−7}; η = 2π2^{−16} + τ < 9.616·10^{−5}; R = 1 + τ < 1.0000003;
κ = 2Rp_F + η < 9.82·10^{−5}.

**Lemma B (bounded influence).** For every record (from any copy, clean or
malformed) and every t, |Z̃(t)| ≤ 1 + 2^{−22} = R. *Proof.* Lemma T. ∎

**Lemma D (discretisation).** For every record and t let
X̂(t) = (−1)^b cos(2π(ût/N − m′/8)). Then |Z̃(t) − X̂(t)| ≤ η.

*Proof.* Let y = ût mod N and h = floor(2^q y/N), so 0 ≤ y/N − h/2^q < 2^{−q}. Since
2^{q−3}m′ is an integer and table[k] approximates cos(2πk/2^q), which has period
2^q in k, |table[k(t)] − cos(2π(h/2^q − m′/8))| < τ (Lemma T). As cos is
1-Lipschitz, |cos(2π(h/2^q − m′/8)) − cos(2π(y/N − m′/8))| ≤ 2π2^{−q}, and
cos(2π(y/N − m′/8)) = cos(2π(ût/N − m′/8)) because y ≡ ût (mod N). ∎

**Lemma C (clean correlation).** Under L, let u be the label of the copy in (2.1)
and X(t) = (−1)^b cos(2π(ut/N − m′/8)). For t ∈ [0, N):
E_L[X(t)] = 1/2 if t = s and E_L[X(t)] = 0 if t ≠ s.

*Proof.* Under L, u is uniform on Z/NZ (2.1) and m′ is uniform on {0,…,7}
independently of u (fresh fair bits). In the decomposition (2.1) the copy is the
product φ(u) ⊗ χ_{−u}; F acts only on the register χ_{−u} and on fresh controls,
so given (u, m′) (and given all outcomes of F) the first qubit is still φ(u), and
by P2, E[(−1)^b | u, m′] = 2p_{m′}(us/N) − 1 = cos(2π(us/N − m′/8)). With
cos A cos B = (cos(A−B) + cos(A+B))/2,

  E[X(t) | u, m′] = (1/2)cos(2πu(s−t)/N) + (1/2)cos(2πu(s+t)/N − πm′/2).

Averaging over m′: Σ_{m′=0}^{7} cos(θ − πm′/2) = Re(e^{iθ} Σ_{m′=0}^{7} (−i)^{m′}) = 0,
since 1 + (−i) + (−1) + i = 0. Averaging over u: with d = s − t ∈ (−N, N),
(1/N) Σ_{u=0}^{N−1} cos(2πud/N) = Re((1/N) Σ_u e^{2πiud/N}), a sum of N-th roots of
unity, which is 1 if d ≡ 0 (mod N), i.e. t = s, and 0 otherwise. ∎

**Lemma K (clean mean).** Let μ(t) = E_L[Z̃(t)]. Then |μ(s) − 1/2| ≤ κ and
|μ(t)| ≤ κ for every t ≠ s. Also |μ(t)| ≤ R.

*Proof.* Let G be the event û = u. Given u, the 8(J+1)r₁ test outcomes of F are
independent and the tests at level i with phase m′ have outcome-0 probability
p_{m′}(frac(2^i u/N)) (Section 2, P2); this is the hypothesis of Lemma P with
φ = u/N. So, for **every** u, with conditional probability at least
1 − 16(J+1)e^{−r₁/200} = 1 − 16(J+1)e^{−L₁} the success event of Lemma P holds, and
then Corollary P′ (a = u) gives û = u. As e^{−L₁} < 2^{−L₁} < 1/(16(J+1)·10⁶),
P(G^c | u) < 10^{−6} = p_F for every u, hence P_L(G^c) < p_F. (Only F's own
outcomes, which depend on u and F's fresh controls, enter G; the bound needs no
independence between G and b.) On G, X̂ = X, so |Z̃ − X| ≤ η by Lemma D. On G^c,
|Z̃ − X| ≤ R + 1 ≤ 2R by Lemma B and |X| ≤ 1. Therefore
|μ(t) − E_L X(t)| ≤ η + 2R p_F = κ, and Lemma C gives the claim. |μ| ≤ R by Lemma B. ∎

### 6.1 Malformed copies: bounded expected influence

For a copy j and a candidate t write Y_j(t) = Z̃_j(s) − Z̃_j(t), so |Y_j(t)| ≤ 2R
(Lemma B) and S(s) − S(t) = Σ_j Y_j(t).

**Lemma M (expected influence of an arbitrary copy).** For every j, every t, every
adversary, and every history in H_{j−1} of positive probability (clean or malformed c_j),

  E[Y_j(t) | H_{j−1}] ≥ −(1 + 2η).

*Proof.* Let G_j be the σ-algebra generated by H_{j−1} and all outcomes of step 2
(procedure F) on copy j; û_j is G_j-measurable and H_{j−1} ⊆ G_j ⊆ H_j. The adversary
has no access to copy j or to ROB+'s systems after delivery. Any operation the adversary
performs after delivery of copy j acts only on E, which is disjoint from copy j and from
ROB+'s systems; it may depend on ROB+'s earlier outcomes, but nothing ROB+ does on copy j
depends on the adversary's later outcomes. Postponing such operations past step 4 therefore
leaves the joint law of H_{j−1}, the outcomes of F, m′_j and b_j unchanged. Adversary outcomes
recorded after the choice c_j are not in G_j; σ_g averages over them. Fix an outcome g of G_j of positive probability (all outcome sets are countable).
Let σ_g be the reduced state of the first (coset) qubit of copy j after step 2,
conditioned on g. F acts only on the second register of the copy and on fresh controls, so
the first qubit has not been acted on; σ_g is still an arbitrary qubit state. Write
σ_g = (I + xX + yY + zZ)/2 with x + iy = r e^{iα}, 0 ≤ r ≤ 1.

Step 3 draws m′ from fresh qubits, so m′ is uniform on {0,…,7} and independent of g,
and it does not touch the copy. Step 4 (P2 with θ = 2πm′/8) has outcome 0 with
probability |⟨0|H diag(1, e^{−iθ})|·⟩|², i.e. it projects onto |θ⟩ = (|0⟩ + e^{iθ}|1⟩)/√2.
Since ⟨θ|X|θ⟩ = cos θ, ⟨θ|Y|θ⟩ = sin θ and ⟨θ|Z|θ⟩ = 0,

  E[(−1)^b | g, m′] = 2⟨θ|σ_g|θ⟩ − 1 = x cos θ + y sin θ = r cos(θ − α).

Let v_t = û_j t/N (G_j-measurable). Then, with θ_{m′} = 2πm′/8 and
cos A cos B = (cos(A+B) + cos(A−B))/2,

  E[X̂_j(t) | g] = (1/8) Σ_{m′=0}^{7} r cos(θ_{m′} − α) cos(2πv_t − θ_{m′})
              = (r/2) cos(2πv_t − α) + (r/16) Σ_{m′=0}^{7} cos(2θ_{m′} − α − 2πv_t)
              = (r/2) cos(2πv_t − α),

because Σ_{m′=0}^{7} e^{2iθ_{m′}} = Σ_{m′=0}^{7} i^{m′} = 0. Hence

  E[X̂_j(s) − X̂_j(t) | g] = (r/2)(cos(2πv_s − α) − cos(2πv_t − α)) ≥ −r ≥ −1.

By Lemma D, |Y_j(t) − (X̂_j(s) − X̂_j(t))| ≤ 2η for every record, so
E[Y_j(t) | g] ≥ −1 − 2η for every g, and the tower property (H_{j−1} ⊆ G_j) gives the
claim. ∎

For a clean copy Fact E and Lemma K give the stronger E[Y_j(t) | H_{j−1}] =
μ(s) − μ(t) ≥ 1/2 − 2κ for t ≠ s. (Lemma C is the case r = 1, α = 2πus/N.)

### 6.2 Concentration and the main theorem

**Lemma A (one-sided Azuma–Hoeffding, interval form).** Let D_1, …, D_Q be real random
variables, D_j H_j-measurable, with E[D_j | H_{j−1}] = 0 and a_j ≤ D_j ≤ a_j + w, where
a_j is H_{j−1}-measurable and w > 0 is a constant. Then for λ > 0,
P(Σ_j D_j ≤ −λ) ≤ exp(−2λ²/(Q w²)).

*Proof.* (Conditional Hoeffding lemma.) Fix j and a history of H_{j−1}; write a = a_j,
b = a + w, X = D_j. E[X | H_{j−1}] = 0 forces a ≤ 0 ≤ b. For real θ, convexity of
x ↦ e^{θx} on [a, b] gives e^{θX} ≤ ((b − X)e^{θa} + (X − a)e^{θb})/w; taking E[· | H_{j−1}],
E[e^{θX} | H_{j−1}] ≤ (b e^{θa} − a e^{θb})/w. With p = −a/w ∈ [0, 1] and h = θw this equals
e^{ψ(h)}, ψ(h) = −ph + ln(1 − p + p e^h). Now ψ(0) = 0, ψ′(0) = 0 and
ψ″(h) = ρ(1 − ρ) ≤ 1/4 with ρ = pe^h/(1 − p + pe^h) ∈ [0, 1], so ψ(h) ≤ h²/8 by Taylor's
theorem, i.e. E[e^{θD_j} | H_{j−1}] ≤ e^{θ²w²/8}. With M_j = D_1 + … + D_j and θ < 0,
E[e^{θM_j}] = E[e^{θM_{j−1}} E[e^{θD_j} | H_{j−1}]] ≤ e^{θ²w²/8} E[e^{θM_{j−1}}], so
E[e^{θM_Q}] ≤ e^{Qθ²w²/8}. Markov's inequality gives P(M_Q ≤ −λ) ≤ e^{θλ + Qθ²w²/8}; take
θ = −4λ/(Qw²). ∎

**Theorem 1.** For every N ≥ 2, every s ∈ Z/NZ and every adversary of Section 5
with ε = 33/100, ROB+ outputs s with probability at least 7/8.

*Proof.* (Concentration.) Fix t ≠ s and let m_j = E[Y_j(t) | H_{j−1}] and
D_j = Y_j(t) − m_j. D_j is H_j-measurable, E[D_j | H_{j−1}] = 0, and since
Y_j(t) ∈ [−2R, 2R], D_j ∈ [a_j, a_j + 4R] with a_j = −2R − m_j H_{j−1}-measurable.
Lemma A with w = 4R and λ = δQ gives

  P(Σ_j D_j ≤ −δQ) ≤ exp(−2δ²Q/(16R²)) = exp(−δ²Q/(8R²)).

Now 8R²/δ² = 500000·R² < 500000·(1 + 2^{−20}) < 500001 < 2^{19}, so
δ²Q/(8R²) > 2^{19}(n + 4)/2^{19} = n + 4 > (n + 3) ln 2 ≥ ln(8N) (as N ≤ 2^n). Each
probability is therefore < 1/(8N), and by a union bound over the at most N − 1
candidates t ≠ s, the event 𝒢 = {Σ_j D_j(t) > −δQ for all t ≠ s} has probability > 7/8.

(Deterministic margin.) Fix a branch in 𝒢 and t ≠ s. Let n_b ≤ floor(εQ) ≤ εQ be the
number of malformed copies on this branch and n_c = Q − n_b. By Fact E with Lemma K
(clean copies) and Lemma M (malformed copies), m_j ≥ 1/2 − 2κ for clean j and
m_j ≥ −(1 + 2η) for malformed j. Hence

  S(s) − S(t) = Σ_j D_j + Σ_j m_j > −δQ + f(n_b),
  f(x) := (Q − x)(1/2 − 2κ) − x(1 + 2η).

f is decreasing (slope −(3/2 − 2κ + 2η) < 0), so f(n_b) ≥ f(εQ) and
S(s) − S(t) > Q·Γ with

  Γ = (1 − ε)(1/2 − 2κ) − ε(1 + 2η) − δ.

With the bounds above: (67/100)(1/2 − 2κ) > 0.334868, (33/100)(1 + 2η) < 0.330064 and
δ = 0.004, so Γ > 0.0008 > 0. Hence on 𝒢, S(s) > S(t) for every t ≠ s: s is the unique
maximiser and ROB+ outputs it. So P(output = s) ≥ P(𝒢) > 7/8. ∎

This holds for every N ≥ 2 (no threshold), for every s and every admissible
adversary, in particular for the clean problem (n_b = 0). The success probability
is unconditional: no postselection, no abort. The margin bound Γ is linear in ε and,
with these constants, vanishes near ε ≈ 0.3305; nothing is claimed for larger ε.

### 6.3 The ceiling 1/3 (proved remark, not part of any claim)

**Proposition U.** Let N be even, s ∈ Z/NZ, s′ = (s + N/2) mod N and ε > 1/3. Let 𝒜
be any algorithm (any quantum and classical processing) that acquires exactly Q copies on
every branch, where Q > ln 6/(2(ε − 1/3)²). Then there are adversaries of the Section 5
model with fraction ε, 𝒱 for s and 𝒱′ for s′, such that P_{s,𝒱}(𝒜 outputs s) < 2/3 or
P_{s′,𝒱′}(𝒜 outputs s′) < 2/3.

*Proof.* By (2.1), ρ_s = (1/N)Σ_u |φ_s(u)⟩⟨φ_s(u)| ⊗ |χ_{−u}⟩⟨χ_{−u}|, where
φ_s(u) = (|0⟩ + e^{2πius/N}|1⟩)/√2. As e^{2πius′/N} = (−1)^u e^{2πius/N}, φ_{s′}(u) = φ_s(u)
for even u, while for odd u, φ_{s′}(u) is orthogonal to φ_s(u). Put
E₀ = (1/N)Σ_{u even} |φ_s(u)⟩⟨φ_s(u)| ⊗ |χ_{−u}⟩⟨χ_{−u}|, A₀ = (1/N)Σ_{u odd} |φ_s(u)⟩⟨φ_s(u)| ⊗ |χ_{−u}⟩⟨χ_{−u}|,
B₀ = (1/N)Σ_{u odd} |φ_{s′}(u)⟩⟨φ_{s′}(u)| ⊗ |χ_{−u}⟩⟨χ_{−u}|. Then ρ_s = E₀ + A₀, ρ_{s′} = E₀ + B₀, and
Tr A₀ = Tr B₀ = 1/2 (N/2 odd labels). So σ := 2B₀ and σ′ := 2A₀ are states of the copy
register, and

  ω := (2/3)ρ_s + (1/3)σ = (2/3)(E₀ + A₀ + B₀) = (2/3)ρ_{s′} + (1/3)σ′.

Adversary 𝒱 (instance s): independently for each j, a private coin marks copy j with
probability 1/3; a marked copy is malformed and equal to a fresh σ, unless floor(εQ)
copies are already malformed, in which case it is clean. 𝒱′ (instance s′) is the same
with σ′. Both are admissible (oblivious, cap respected on every branch). Let 𝒱_∞ and 𝒱′_∞
be the same without the cap (used only for comparison). These adversaries never use
𝒜's outcomes and never act again after supplying a copy, so 𝒜's output law depends only on
the joint state of the Q delivered copies with the coins (held in E) discarded. Under 𝒱_∞
that state is ω^{⊗Q}, and the same holds under 𝒱′_∞. So the output law of 𝒜 is identical
under (s, 𝒱_∞) and (s′, 𝒱′_∞). Using the same coins, 𝒱 and
𝒱_∞ deliver identical copies unless more than floor(εQ) of the Q coins mark, which has
probability γ ≤ P(Bin(Q, 1/3) − Q/3 > (ε − 1/3)Q) ≤ exp(−2(ε − 1/3)²Q) < 1/6 (Hoeffding);
likewise for 𝒱′. Hence P_{s,𝒱}(out = s) + P_{s′,𝒱′}(out = s′) ≤ P_ω(out = s) + P_ω(out = s′) + 2γ
< 1 + 1/3, so the two probabilities cannot both be ≥ 2/3. ∎

For Q = 2^{19}(n + 4) and even N this rules out every ε > 1/3 + 2^{−10}, since then
Q ≥ 5·2^{19} > 2^{19} ln 6 > ln 6/(2(ε − 1/3)²). Thus 33/100 = (99/100)·(1/3). Proposition U is
an upper bound only (even N, fixed copy count); it is stated to locate the claim and is not
used anywhere else.

## 7. Resources (every branch)

The loop lengths of 4.4–4.5 (Q, J, r₁, 2^q, N) depend on n and N only, and every
step processes malformed copies exactly like clean ones, so the bounds below hold
on every execution branch, for every adversary.

**Samples.** Step 1 of 4.4 runs exactly Q times and nothing else acquires copies:
**Q = 2^{19}(n + 4) ≤ 5·2^{19} n = O(n)** (n ≥ 1), counting every copy.

**Quantum space.** At any time ROB+ holds at most one copy (n + 1 qubits), one test
control, the O(n) ancillas of P1 and one P5 qubit; all are measured and released
after each test or copy. The scoring phase uses no qubits.
**S_Q ≤ n + 3 + O(n) = O(n).**

**Classical space.**
* Records: Q(n + 4) bits (û_j: n, m′_j: 3, b_j: 1); y_j registers: Qn bits.
* Table: 2^q·24 = 3·2^{19} bits; construction workspace: an absolute constant (Section 4.2).
* F workspace, reused per copy: 8(J+1) counters of bitlength(r₁) = O(log log n) bits,
  the 3-bit m_i, one x_i of J + 3 bits, the constant 2^i mod N, rounding scratch:
  O(n log log n). Gate lists are emitted and applied one gate at a time; only one gate
  description (O(log M) = O(log n) bits) is stored at a time.
* Scoring: |Σ| ≤ Q(2^{22} + 1), so Σ, Σ_best have ≤ bitlength(Q) + 25 = O(log n) bits;
  t, best, h_j scratch: O(n); loop counter j: O(log n).
* Parameters N, n, J, L₁, r₁, Q: O(n).

**S_C ≤ 2^{19}(n + 4)(2n + 4) + 3·2^{19} + O(n log log n + log n + 1) = O(n²).** Hence M = O(n²) and
the address charge is A = ceil(log₂(M + 2)) ≤ 2 log₂ n + O(1) = O(log n) for n ≥ 2.

**Work.** Each counted operation costs O(A).
* Parameters (bit lengths and products of O(log n)-bit integers, Q): O(n A).
* Table (Section 4.2): an absolute constant number of operations: O(A).
* Per copy, acquisition: n + 1. F: 8(J+1)r₁ tests, and r₁ = 200 L₁ with
  L₁ ≤ log₂(16·10⁶(J + 1)) + 1 < log₂(n + 1) + 25, so O(n log n) tests. Each test allocates
  a control (O(1)), generates and applies the O(n)-gate P1 circuit (O(n)), applies
  P2 (O(1)) and increments a counter (O(log log n)): O(n A) per test. The constants
  2^i mod N are obtained by doubling with a conditional subtraction (O(n) per level).
  Lemma P reconstruction O(J² + J log r₁) and rounding O(n²): O(n² A). Steps 3–6:
  O(n A). Per copy O(n² log n · A) = O(n² log² n); over Q copies O(Q n² log² n) =
  O(n³ log² n).
* Scoring, per pair (t, j): the division h_j = floor(2^q y_j/N) by q = 16 steps of
  shift, compare with N and conditional subtract on (n + q)-bit numbers: O(nq) = O(n);
  k_j: O(q) = O(1); the indexed table read of a 24-bit word: O(1) accesses with
  address cost A; the signed addition into Σ: O(log Q) = O(log n); the modular
  increment of y_j (n-bit add, compare, conditional subtract): O(n); the counter j:
  O(log n). Total O(n A) per pair. Per t additionally O(n A) (comparison of Σ with
  Σ_best, update of best, counter t). Initialising the y_j: O(Qn A). Over the
  N ≤ 2^n values of t: O(N Q n A) = O(2^n · n · n · log n) = O(2^n n² log n).
* Allocation and initialisation of all memory: O(M A) = O(n² log n).

Since n³ log² n ≤ 2^n n² log n for all n ≥ 2 (as n log n ≤ 2^n),
**T = O(N Q n A + Q n² log² n) = O(2^n n² log n)**, with an absolute constant, for
all n ≥ 2; the only instance with n = 1 is N = 2, whose cost is an absolute
constant. All four bounds hold simultaneously on every execution branch of this
single algorithm with this single parameter rule, jointly with Theorem 1.

## 8. Exact growth indices and structured envelopes

For B(n) = 2^n n^a (log n)^b with fixed a, b ≥ 0: log₂ B = n + a log n + b log log n,
so log₂ log₂ B / log₂ n = 1 + log₂(1 + (a log n + b log log n)/n)/log₂ n → 1, and
g(B) = 1. For B(n) = n^a with fixed a > 0: log₂ log₂ B = log₂ a + log₂ log₂ n, so the
ratio tends to 0 and g(B) = 0. Fixed outer constants do not change either value
(the max{4,·} is irrelevant for large n).

* T: B_T(n) = 2^n n² log₂ n, index **1**; structured: coefficient 1, exponent
  [{coefficient 1, nPower 1, logPower 0}], nPower 2, logPower 1.
* S_C: B_C(n) = n², index **0**; exponent [], nPower 2, logPower 0.
* S_Q: B_Q(n) = n, index **0**; exponent [], nPower 1, logPower 0.
* Q: B_samples(n) = n, index **0**; exponent [], nPower 1, logPower 0 (explicitly
  Q = 2^{19}(n + 4)).

Published time score: [1]. The time bound is exponential; the contribution of
ROB+ is the joint guarantee of O(n) copies, O(n) qubits, O(n²) bits and a constant
fraction 33/100 of adaptively placed, arbitrarily entangled malformed copies, within 1%
of the 1/3 ceiling of Proposition U. Using O(log N) clean coset states with exponential
classical post-processing is known (Ettinger–Høyer, Adv. Appl. Math. 25 (2000);
Ettinger–Høyer–Knill, IPL 91 (2004)). Lemma P is a standard Kitaev-style iterative phase
estimation, written out for exact Clifford+T gates. Regev (SIAM J. Comput. 33 (2004),
Definition 2.1) studies DCP with a failure parameter, where a bad register is a
computational-basis state; the model here is stronger (adaptive positions, arbitrary
entangled states, a fraction rather than a per-register probability). ROB+ is not claimed to
improve on prior algorithms for clean inputs; its contributions are the jointly charged
resource bounds in this cost model, the proved adaptive 33/100 tolerance (Lemma M) and the
1/3 ceiling (Proposition U). No cited result is used in the proof.

## 9. Fractional error tolerance

ε(n) = 33/100 under the model of Section 5: with Q = 2^{19}(n + 4) acquired copies,
at most floor(33Q/100) of them are malformed; their positions are
chosen adaptively by an adversary who knows N, s, the algorithm and all previous
measurement outcomes; malformed copies are arbitrary (n+1)-qubit states, possibly
entangled with one another and with the adversary, but not with clean copies or
ROB+'s workspace; every other copy is, at the moment of its delivery, an independent
ideal coset state ρ_s in tensor product with everything else, and the adversary has no
access to a copy or to ROB+'s systems after delivery (Section 5). For
every N ≥ 2, every s and every such adversary, Theorem 1 gives success probability
at least 7/8 > 2/3, jointly with the four resource bounds of Section 7, which hold
on every branch for every adversary. The clean problem is the special case with no
malformed copy. Proposition U (Section 6.3) shows that no fraction above 1/3 can be
tolerated for even N by any algorithm with a fixed copy count Q > ln 6/(2(ε − 1/3)²);
it is a remark, not part of the claim.

## 10. Constant summary

q = 16; table precision τ = 2^{−22}; π̃ = 103993/33102; Taylor degree 40; r₁ = 200 L₁ with
L₁ = bitlength(16(J+1)·10⁶), so p_F < 10^{−6}; J = max(1, n−2); Q = 2^{19}(n+4);
δ = 1/250; ε = 33/100; η < 9.616·10^{−5}; R = 1 + 2^{−22}; κ < 9.82·10^{−5};
8R²/δ² < 500001 < 2^{19}; Γ > 0.0008. Each inequality is derived in the text above; no
step depends on computation outside this file.
