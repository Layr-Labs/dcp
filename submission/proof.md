# ROB-G (clean-input statement): quantum search over robust shadow scores, O(2^{n/2} n² log² n) work, O(n) copies, O(n) qubits, O(n²) bits

This file is the complete proof of all five claims in `submission.json`. It
describes one algorithm, **ROB-G**, with one fixed parameter rule, and proves for
every integer N ≥ 2, every s ∈ Z/NZ, with n = ceil(log₂ N), and every adversary
of the error model of Section 5 (which contains the clean problem as the
adversary that corrupts nothing):

* the output equals s with unconditional probability at least 49/64 (> 2/3);
* total work T = O(2^{n/2} n² log² n);
* peak classical space S_C = O(n²) bits;
* peak quantum space S_Q = O(n) qubits;
* acquired source copies: exactly Q = 2^{19}(n+4) = O(n) on every branch;
* the fifth claim of this submission is the clean-input guarantee ε(n) = 0 under the
  baseline model text (all copies independent ideal coset states). The proof below
  establishes more (tolerance 33/100 under the adaptive model of Section 5, the clean problem
  being the adversary that corrupts nothing); that stronger statement is claimed separately in
  our submission a5c17989, not here.

All constants are absolute (independent of N, s, the adversary and all outcomes).
Every loop of ROB-G has a length fixed by n and N alone, except the repetition loop of
Section 4.6, which runs at most 3 times on every branch, so the four resource bounds
hold on every execution branch whatever the copies contain. There are no aborts;
the acquisition phase is never restarted, and the search circuit is repeated at most three times on
the same records, acquiring no copies. Logarithms are base 2 unless written ln.

**Ceiling (Section 6.4, Proposition U; a proved remark, not a claim).** In the adaptive model of Section 5 (not the model of the fifth claim),
for even N, no algorithm with a fixed copy count Q > ln 6/(2(ε − 1/3)²) tolerates a fraction
ε > 1/3: the instances s and s + N/2 can be made indistinguishable. 33/100 = (99/100)(1/3).

**Idea.** Each copy yields a classical record: the binary expansion of its Fourier label
û/N (û estimated exactly, w.h.p.), a uniformly random phase offset m′/8 and one ±1 outcome
(−1)^b. For every candidate t the quantity (−1)^b cos(2π(ût/N − m′/8)) is an estimator of
(1/2)·[t = s] (Lemma C). Because m′ is drawn *after* the copy has been delivered and its
label estimated, an arbitrary malformed copy has conditional expected contribution in
[−1/2 − η, 1/2 + η] to every score (Lemma M). Hence, with probability > 7/8, the score of s
exceeds (67/400)Q and every other score stays below it, for every adversary with ε = 33/100
(Theorem 1). The threshold test is a classical function of the stored records, so it is a
reversible circuit on a quantum candidate register: ROB-G finds the unique marked candidate by
Grover search with O(2^{n/2}) oracle calls. Each call recomputes all Q scores coherently in
O(Q n log n) gates, because frac(ût/N) is accumulated from p-bit truncations of the binary
expansion of û/N (p = O(log n)) with error < 2^{−q−1}.

Notation. frac(φ) ∈ [0,1); |φ|∘ = min_{z∈Z} |φ − z| (circular distance). For an
integer v let

  φ(v) = (|0⟩ + e^{2πi v s/N}|1⟩)/√2   (a *label-v qubit*; only v mod N matters).

bitlength(x) is the number of binary digits of an integer x ≥ 1, so
2^{bitlength(x)} > x and e^{−bitlength(x)} < 2^{−bitlength(x)} < 1/x.
round(z) = floor(z + 1/2).

## 1. Primitive operations (exact Clifford+T)

(The primitives are numbered P1, P2, P3, P5; no other primitive is used, and nothing
outside this file is relied on.) Gates are X, CNOT, H, T, T† and Toffoli. Toffoli with
controls a, b and target c is the exact Clifford+T circuit (applied left to right)
H(c), CNOT(b→c), T†(c), CNOT(a→c), T(c), CNOT(b→c), T†(c), CNOT(a→c), T(b), T(c), H(c),
CNOT(a→b), T(a), T†(b), CNOT(a→b): 15 gates, which equals Toffoli exactly as an 8×8 matrix
(direct multiplication). Z = T⁴. Every released qubit is measured and, if its
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

**P3 (further reversible arithmetic, exact).** All circuits below use X, CNOT and Toffoli
only, return every ancilla to |0⟩, and are emitted gate by gate by a uniform generator.
* *P3a (controlled constant addition mod 2^p, in place).* P1 with the modulus N replaced by
  2^p on a p-qubit register (then e = 1 and the map is y ↦ (y + a) mod 2^p on all of
  [0, 2^p)), with the same control construction. O(p) gates, O(p) ancillas.
* *P3b (register adder mod 2^w, in place).* Out of place, |a⟩|b⟩|0⟩ ↦ |a⟩|b⟩|(a + b) mod 2^w⟩:
  compute the carries carry_{i+1} = MAJ(a_i, b_i, carry_i) into w ancillas by Toffoli/CNOT
  groups, write the sum bits by CNOTs, uncompute the carries by running the carry circuit
  backwards. Since the sum bits are written by CNOTs, the same circuit maps
  |a⟩|b⟩|y⟩ ↦ |a⟩|b⟩|y ⊕ ((a + b) mod 2^w)⟩ for every y. Subtraction b − a = b + (2^w − 1 − a) + 1
  mod 2^w uses X on every a wire (including padding wires) before and after, and carry_0 = 1. In place, b ← (b + a) mod 2^w: add out of place into a fresh
  register S, then XOR (S − a) mod 2^w (= b) into the old b register, which clears it, and
  relabel S as b (unconditionally; no control is needed here). b ← (b − a) mod 2^w is the same
  with the roles of addition and subtraction exchanged. If a has fewer than w wires, its
  missing high wires are fresh |0⟩ ancillas. O(w) gates, O(w) ancillas.
* *P3c (comparison with a classical constant).* For a w-qubit register y and a classical
  constant c ∈ [1, 2^w], the flag [y ≥ c] is the carry out of y + (2^w − c), computed into a
  fresh qubit and its carries uncomputed as in P1. O(w) gates.
* *P3d (multi-controlled X).* C^m X (m ≥ 2 controls) by the standard Toffoli chain: m − 2
  ancillas hold the partial ANDs, one Toffoli onto the target, and the chain is uncomputed.
  O(m) gates.
* *P3e (table read, QROM).* For a q-qubit index register k, a 24-qubit register v = |0⟩ and a
  classical table of 2^q words d_κ: for each κ = 0, …, 2^q − 1, apply X to the index wires where
  κ has a 0 bit, compute the AND of the q index wires into a fresh flag by P3d, apply CNOT from
  the flag to each wire of v at which d_κ has a 1 bit, uncompute the flag and undo the X gates.
  This maps |k⟩|v⟩ ↦ |k⟩|v ⊕ d_k⟩ on every basis state; applied twice it is the identity.
  O(2^q (q + 24)) gates (an absolute constant for fixed q) and O(q) ancillas.

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

## 4. Algorithm ROB-G

### 4.1 Parameters

All are integers computed exactly from n (constants in brackets are used only in
the analysis):

* J = max(1, n − 2); L₁ = bitlength(16(J+1)·10⁶); **r₁ = 200 L₁**;
* **Q = 2^{19}(n + 4)**; **q = 16** (angle bits); **p = q + 1 + bitlength(n)** (phase bits);
  w = bitlength(Q) + 26 (accumulator width);
* [p_F = 10^{−6}, δ = 1/500, ε = 33/100 (the Section 5 analysis fraction; the fifth claim is ε(n) = 0, Section 9), τ = 2^{−22}, η = 3π2^{−q} + τ, R = 1 + τ,
  κ = 2R p_F + η].

### 4.2 Cosine table (computed at run time, independent of N)

Let π̃ = 103993/33102. For k = 0, …, 2^q − 1: x̃_k = 2π̃k/2^q (exact rational),
P_k = Σ_{i=0}^{20} (−1)^i x̃_k^{2i}/(2i)! (exact rational arithmetic), and
c_k = round(2^{22} P_k) ∈ Z. Store c_k as a 24-bit two's-complement integer and
d_k = c_k + 2^{22} + 1 as a 24-bit unsigned integer.

**Lemma T.** |c_k/2^{22} − cos(2πk/2^q)| < τ = 2^{−22} for every k, hence
|c_k| ≤ 2^{22}(1 + 2^{−22}) = 2^{22} + 1 < 2^{23} and 0 ≤ d_k ≤ 2^{23} + 2 < 2^{24}.

*Proof.* 3.1415926 < π < 3.1415927 and 3.14159265301 < π̃ < 3.14159265302 (long
division), so |π − π̃| < 5.31·10^{−8}; with x_k = 2πk/2^q and k < 2^q,
|x_k − x̃_k| < 2·5.31·10^{−8} = 1.062·10^{−7}, and |cos x_k − cos x̃_k| < 1.062·10^{−7} (cos is
1-Lipschitz). Since 0 ≤ x̃_k < 2π̃ < 6.3 and |cos^{(42)}| ≤ 1, Taylor's theorem
with Lagrange remainder (P_k, of degree 40, is also the Taylor polynomial of degree 41, since the x^{41}
coefficient of cos is 0) gives |cos x̃_k − P_k| ≤ 6.3^{42}/42! < 3.8·10^{33}/(1.4·10^{51})
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
6. Compute e_j = floor(2^{n+p} û_j/N) by binary long division (n + p shift–compare–subtract
   steps on (n + 1)-bit remainders) and store the record (e_j, m′_j, b_j); û_j is discarded.

The order matters for Lemma M: m′_j is drawn after copy j has been delivered and
after F has finished on it.

### 4.5 The score and the marking function

For a record j and i ∈ {0, …, n − 1} let c_{j,i} = floor(e_j/2^{n−i}) mod 2^p. Since
floor(floor(2^{n+p}x)/2^{n−i}) = floor(2^{p+i}x) for real x ≥ 0 and floor(2^{p+i}x) mod 2^p =
floor(2^p frac(2^i x)), we have c_{j,i} = floor(2^p frac(2^i û_j/N)). For t ∈ [0, 2^n) with bits
t = Σ_i t_i 2^i define

  V_j(t) = (Σ_{i=0}^{n−1} t_i c_{j,i}) mod 2^p,  h_j(t) = floor(V_j(t)/2^{p−q}),
  k_j(t) = (h_j(t) − 2^{q−3} m′_j) mod 2^q,
  Σ(t) = Σ_{j=1}^{Q} (−1)^{b_j} c_{k_j(t)} ∈ Z,  S(t) = Σ(t)/2^{22} = Σ_j Z̃_j(t),
  Z̃_j(t) = (−1)^{b_j} table[k_j(t)],

and the marking function

  f(t) = 1 if t < N and 400·Σ(t) > 67·2^{22}·Q, and f(t) = 0 otherwise.

(Equivalently S(t) > θ₀Q with θ₀ = 67/400.) f depends only on the stored records and is
evaluated *classically* for a given t in O(Q n p) bit operations: for each j, accumulate
V_j(t) over the set bits of t (p-bit additions), take the top q bits, subtract 2^{q−3}m′_j mod
2^q, read c_k and add or subtract it.

### 4.6 Output phase

* **n ≤ 3** (N ≤ 8): evaluate f(t) classically for t = 0, …, N − 1 and output the smallest t
  with f(t) = 1 (output 0 if there is none).
* **n ≥ 4**: let K = floor(2^{n/2}) (the integer square root of 2^n, computed exactly by
  the bitwise integer square-root method in O(n²) bit operations) and k_G = floor(785K/1000).
  Repeat at most three times: prepare n fresh qubits |0^n⟩, apply H to each, apply
  G = 𝒟·𝒪 exactly k_G times (Section 4.7), measure all n qubits to obtain t̂ ∈ [0, 2^n), and
  evaluate f(t̂) classically; if f(t̂) = 1, output t̂ and stop. If the three repetitions all
  fail, output 0.

k_G and every loop length except the repetition count depend on n and N only; the repetition
count is at most 3 on every branch.

### 4.7 The circuits 𝒪 and 𝒟

**𝒟 (diffusion).** H on each of the n search qubits, then X on each, then the phase flip of
|1^n⟩ (a fresh target qubit is prepared in |1⟩, conjugated by H, and P3d with the n search
qubits as controls is applied to it; then the target is conjugated by H and reset — this
multiplies |1^n⟩ by −1 and every other basis state by 1), then X on each and H on each. As a
matrix this is −(2|ψ₀⟩⟨ψ₀| − I) with ψ₀ = H^{⊗n}|0^n⟩; the global sign −1 is irrelevant.

**𝒪 (phase oracle).** On the search register |t⟩ (n qubits) and fresh ancillas:

1. *Accumulate.* A w-qubit register U starts at |0⟩. For j = 1, …, Q:
   (a) V ← 0 (p fresh qubits); for i = 0, …, n − 1, controlled on t_i, apply P3a with the
       classical constant c_{j,i} (computed from e_j by the controller: a shift and a mask).
       Now V = V_j(t).
   (b) k ← top q wires of V, copied by CNOTs into q fresh qubits; then P3a (uncontrolled; the
       control wire is a fresh qubit set to |1⟩ by X and reset afterwards) with the constant
       (2^q − 2^{q−3}m′_j) mod 2^q on k. Now k = k_j(t).
   (c) v ← d_k by P3e (24 fresh qubits).
   (d) If b_j = 0, U ← (U + v) mod 2^w; if b_j = 1, U ← (U − v) mod 2^w (P3b; b_j is
       classical, so the controller chooses the circuit).
   (e) Uncompute (c), (b), (a) by applying their circuits in reverse order (P3e is its own
       inverse; the inverse of P3a with constant c is P3a with the constant (2^p − c) mod 2^p).
   After the loop U = (Σ_{j: b_j=0} d_{k_j(t)} − Σ_{j: b_j=1} d_{k_j(t)}) mod 2^w. Since
   Σ(t) = Σ_j (−1)^{b_j}(d_{k_j(t)} − 2^{22} − 1), the integer
   U* = Σ(t) + (2^{22} + 1)(n₀ − n₁), with n₀ = #{j : b_j = 0} and n₁ = Q − n₀, satisfies
   |U*| ≤ Q(2^{23} + 2) < 2^{25}Q < 2^{w−1} (as 2^{w−1} = 2^{bitlength(Q)+25} > 2^{25}Q), so U
   holds U* in two's complement.
2. *Flag.* Classically let C* = 67·2^{22}·Q + 400(2^{22} + 1)(n₀ − n₁) and Θ = floor(C*/400); then
   400Σ(t) > 67·2^{22}Q ⇔ 400U* > C* ⇔ U* > Θ ⇔ U* ≥ Θ + 1, and, since |C*| ≤ Q(67·2^{22} + 400(2^{22} + 1)),
   |Θ + 1| ≤ |C*|/400 + 2 < 1.18·2^{22}Q + 2 < 2^{w−1}. Compute
   g = [U* ≥ Θ + 1] by flipping the top wire of U (X; this maps two's complement order to
   unsigned order, U* ↦ U* + 2^{w−1}), applying P3c with the constant Θ + 1 + 2^{w−1} ∈ [1, 2^w),
   and flipping the top wire back. Compute e = [t < N] = 1 − [t ≥ N] by P3c on the search
   register and an X. Compute f = e ∧ g into a fresh qubit by a Toffoli.
3. *Phase.* Apply Z (= T⁴) to the f qubit.
4. *Clean up.* Uncompute f, e, g by their circuits in reverse, then run step 1 in reverse
   (j = Q, …, 1, each with the inverse operations), returning U and every ancilla to |0⟩.

Every operation in steps 1–2 is a permutation of computational basis states that leaves
|t⟩ unchanged and computes f(t) exactly, so steps 1–4 implement
𝒪 = Σ_t (−1)^{f(t)} |t⟩⟨t| ⊗ I on the ancillas (all returned to |0⟩).

## 5. Error model (adaptive malformed copies)

Copies are delivered one at a time in acquisition order j = 1, …, Q; Q is fixed
by n before the first acquisition. An **adversary** knows N, s, the full
description of ROB-G, and every measurement outcome obtained by ROB-G before copy j
is delivered; it holds an arbitrary private quantum system E which it may measure
and process. Before copy j is delivered it chooses c_j ∈ {clean, malformed}, as a
function of that information and its own outcomes; on every branch at most
floor(εQ) copies are malformed, ε = 33/100.

* A **malformed** copy is an arbitrary (n+1)-qubit system supplied from E. It may
  be in any state, entangled with the rest of E and hence with other malformed
  copies, and may depend on everything listed above. It is not entangled with
  clean copies or with ROB-G's workspace, ancillas or fair-bit qubits.
* A **clean** copy is, at the moment of its delivery, a fresh ρ_s in tensor product
  with everything else (E, all other copies, ROB-G's workspace).
* The adversary interacts with ROB-G only by supplying copies; after delivery it has no
  access to the copy or to ROB-G's quantum or classical systems. All measurements
  (ROB-G's and the adversary's) have countably many outcomes.

ROB-G is not told which copies are malformed. The clean problem is the case in
which no copy is malformed.

**Filtration.** Let H_j be the classical history generated by all outcomes of
ROB-G on copies 1, …, j and all outcomes of the adversary up to and including its
choice c_{j+1} (H_0: the adversary's outcomes up to the choice of c_1; H_Q: all outcomes). Then c_j is
H_{j−1}-measurable and the record (û_j, m′_j, b_j) is H_j-measurable.

**Let L** be the law of the record (û, m′, b) produced by steps 2–4 of 4.4 when
applied to a fresh ρ_s.

**Fact E.** On every history in H_{j−1} with c_j = clean, the conditional law of
the record of copy j is L.

*Proof.* Steps 2–5 for copy j form one fixed instrument {ℰ_r} (r ranging over all
outcomes of the step, including m′_j) acting on copy j and on fresh |0⟩ ancillas
only; it does not depend on the history, because ROB-G's schedule depends only on N
and on outcomes obtained on copy j itself, and ROB-G keeps no quantum state between
copies (step 5). Conditioned on a history h of positive probability with c_j = clean
(outcome sets are countable, so these histories carry all the probability), the joint state when
copy j is delivered is ρ_s ⊗ ω_h, where ω_h is the conditional state of all other
systems. Hence P(r | h) = Tr[(ℰ_r ⊗ id)(ρ_s ⊗ |0…0⟩⟨0…0| ⊗ ω_h)] = Tr[ℰ_r(ρ_s ⊗ |0…0⟩⟨0…0|)],
which is the clean law. ∎

## 6. Correctness

Numerical constants (from π < 22/7 and exact rational bounds):
τ = 2^{−22} < 2.385·10^{−7}; η = 3π2^{−16} + τ < 1.4412·10^{−4}; R = 1 + τ < 1.0000003;
κ = 2Rp_F + η < 1.4613·10^{−4}.

**Lemma B (bounded influence).** For every record and every t, |Z̃(t)| ≤ 1 + 2^{−22} = R.
*Proof.* Lemma T. ∎

**Lemma D (discretisation).** For every record j (with û_j the label from which e_j was
computed) and every t ∈ [0, 2^n), let X̂_j(t) = (−1)^{b_j} cos(2π(û_j t/N − m′_j/8)). Then
|Z̃_j(t) − X̂_j(t)| ≤ η.

*Proof.* Write x = û_j/N and φ = frac(xt). For each i, 2^p frac(2^i x) − c_{j,i} ∈ [0, 1)
(Section 4.5). Since Σ_i t_i 2^i x = xt, Σ_i t_i 2^p frac(2^i x) ≡ 2^p φ (mod 2^p), so
V_j(t) ≡ 2^p φ − ζ (mod 2^p) with ζ = Σ_i t_i (2^p frac(2^i x) − c_{j,i}) ∈ [0, n). Hence the
circular distance |V_j(t)/2^p − φ|∘ < n/2^p < 2^{−q−1} (as 2^{bitlength(n)} > n). Also
0 ≤ V_j(t)/2^p − h_j(t)/2^q < 2^{−q}. So |h_j(t)/2^q − φ|∘ < (3/2)2^{−q}. As x ↦ cos(2πx) has
period 1 and is 2π-Lipschitz,
|cos(2π(h_j(t)/2^q − m′_j/8)) − cos(2π(φ − m′_j/8))| < 3π2^{−q}, and
cos(2π(φ − m′_j/8)) = cos(2π(xt − m′_j/8)). Since 2^{q−3}m′_j is an integer and table[k] approximates
cos(2πk/2^q), which has period 2^q in k, |table[k_j(t)] − cos(2π(h_j(t)/2^q − m′_j/8))| < τ
(Lemma T). Adding the two bounds gives the claim. ∎

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

**Lemma K (clean mean).** Let μ(t) = E_L[Z̃(t)] for t ∈ [0, N). Then μ(s) ≥ 1/2 − κ and
μ(t) ≤ κ for every t ≠ s.

*Proof.* Let G be the event û = u. Given u, the 8(J+1)r₁ test outcomes of F are
independent and the tests at level i with phase m′ have outcome-0 probability
p_{m′}(frac(2^i u/N)) (Section 2, P2); this is the hypothesis of Lemma P with
φ = u/N. So, for **every** u, with conditional probability at least
1 − 16(J+1)e^{−r₁/200} = 1 − 16(J+1)e^{−L₁} the success event of Lemma P holds, and
then Corollary P′ (a = u) gives û = u. As e^{−L₁} < 2^{−L₁} < 1/(16(J+1)·10⁶),
P(G^c | u) < 10^{−6} = p_F for every u, hence P_L(G^c) < p_F. On G, X̂ = X, so
|Z̃ − X| ≤ η by Lemma D. On G^c, |Z̃ − X| ≤ R + 1 ≤ 2R by Lemma B and |X| ≤ 1.
Therefore |μ(t) − E_L X(t)| ≤ η + 2R p_F = κ, and Lemma C gives the claim. ∎

### 6.1 Arbitrary copies: bounded expected influence

**Lemma M (expected influence of an arbitrary copy).** For every j, every t ∈ [0, 2^n),
every adversary, and every history in H_{j−1} of positive probability (clean or
malformed c_j),

  −(1/2 + η) ≤ E[Z̃_j(t) | H_{j−1}] ≤ 1/2 + η.

*Proof.* Let G_j be the σ-algebra generated by H_{j−1} and all outcomes of step 2
(procedure F) on copy j; û_j is G_j-measurable and H_{j−1} ⊆ G_j ⊆ H_j. The adversary
has no access to copy j or to ROB-G's systems after delivery. Any operation the adversary
performs after delivery of copy j acts only on E, which is disjoint from copy j and from
ROB-G's systems; it may depend on ROB-G's earlier outcomes, but nothing ROB-G does on copy j
depends on the adversary's later outcomes. Postponing such operations past step 4 therefore
leaves the joint law of H_{j−1}, the outcomes of F, m′_j and b_j unchanged. Adversary outcomes
recorded after the choice c_j are not in G_j; σ_g averages over them. Fix an outcome g of G_j of positive probability (all outcome sets are countable).
Let σ_g be the reduced state of the first (coset) qubit of copy j after step 2,
conditioned on g. F acts only on the second register of the copy and on fresh controls, so
the first qubit has not been acted on; σ_g is an arbitrary qubit state. Write
σ_g = (I + xX + yY + zZ)/2 with x + iy = r e^{iα}, 0 ≤ r ≤ 1.

Step 3 draws m′ from fresh qubits, so m′ is uniform on {0,…,7} and independent of g,
and it does not touch the copy. Step 4 (P2 with θ = 2πm′/8) has outcome 0 exactly when it
projects onto |θ⟩ = (|0⟩ + e^{iθ}|1⟩)/√2 (as |⟨0|H diag(1, e^{−iθ})|ψ⟩| = |⟨θ|ψ⟩|). Since
⟨θ|X|θ⟩ = cos θ, ⟨θ|Y|θ⟩ = sin θ and ⟨θ|Z|θ⟩ = 0,

  E[(−1)^b | g, m′] = 2⟨θ|σ_g|θ⟩ − 1 = x cos θ + y sin θ = r cos(θ − α).

Let v = û_j t/N (G_j-measurable). With θ_{m′} = 2πm′/8 and
cos A cos B = (cos(A+B) + cos(A−B))/2,

  E[X̂_j(t) | g] = (1/8) Σ_{m′=0}^{7} r cos(θ_{m′} − α) cos(2πv − θ_{m′})
              = (r/2) cos(2πv − α) + (r/16) Σ_{m′=0}^{7} cos(2θ_{m′} − α − 2πv)
              = (r/2) cos(2πv − α) ∈ [−1/2, 1/2],

because Σ_{m′=0}^{7} e^{2iθ_{m′}} = Σ_{m′=0}^{7} i^{m′} = 0. By Lemma D,
|Z̃_j(t) − X̂_j(t)| ≤ η for every record, so −(1/2 + η) ≤ E[Z̃_j(t) | g] ≤ 1/2 + η for every
g, and the tower property (H_{j−1} ⊆ G_j) gives the claim. ∎

For a clean copy and t < N, Fact E gives the sharper E[Z̃_j(t) | H_{j−1}] = μ(t)
(Lemma K). (Lemma C is the case r = 1, α = 2πus/N of the identity above.)

### 6.2 Concentration and the marking function

**Lemma A (Azuma–Hoeffding, interval form).** Let D_1, …, D_Q be real random
variables, D_j H_j-measurable, with E[D_j | H_{j−1}] = 0 and a_j ≤ D_j ≤ a_j + w′, where
a_j is H_{j−1}-measurable and w′ > 0 is a constant. Then for λ > 0,
P(Σ_j D_j ≤ −λ) ≤ exp(−2λ²/(Q w′²)) and P(Σ_j D_j ≥ λ) ≤ exp(−2λ²/(Q w′²)).

*Proof.* (Conditional Hoeffding lemma.) Fix j and a history of H_{j−1}; write a = a_j,
b = a + w′, X = D_j. E[X | H_{j−1}] = 0 forces a ≤ 0 ≤ b. For real θ, convexity of
x ↦ e^{θx} on [a, b] gives e^{θX} ≤ ((b − X)e^{θa} + (X − a)e^{θb})/w′; taking E[· | H_{j−1}],
E[e^{θX} | H_{j−1}] ≤ (b e^{θa} − a e^{θb})/w′. With p₀ = −a/w′ ∈ [0, 1] and h = θw′ this equals
e^{ψ(h)}, ψ(h) = −p₀h + ln(1 − p₀ + p₀e^h). Now ψ(0) = 0, ψ′(0) = 0 and
ψ″(h) = ρ(1 − ρ) ≤ 1/4 with ρ = p₀e^h/(1 − p₀ + p₀e^h) ∈ [0, 1], so ψ(h) ≤ h²/8 by Taylor's
theorem: E[e^{θD_j} | H_{j−1}] ≤ e^{θ²w′²/8} for every real θ. With M_j = D_1 + … + D_j,
E[e^{θM_j}] = E[e^{θM_{j−1}} E[e^{θD_j} | H_{j−1}]] ≤ e^{θ²w′²/8} E[e^{θM_{j−1}}], so
E[e^{θM_Q}] ≤ e^{Qθ²w′²/8}. Markov's inequality with θ = −4λ/(Qw′²) gives
P(M_Q ≤ −λ) ≤ e^{−2λ²/(Qw′²)}, and with θ = 4λ/(Qw′²) gives P(M_Q ≥ λ) ≤ e^{−2λ²/(Qw′²)}. ∎

**Theorem 1 (the marking function isolates s).** For every N ≥ 2, every s ∈ Z/NZ and every
adversary of Section 5 with ε = 33/100, the event 𝒢 = {f(s) = 1 and f(t) = 0 for every
t ∈ [0, 2^n) with t ≠ s} (a function of the stored records) has probability > 7/8.

*Proof.* f(t) = 0 for t ≥ N by definition. For t ∈ [0, N) let m_j(t) = E[Z̃_j(t) | H_{j−1}]
and D_j(t) = Z̃_j(t) − m_j(t). D_j(t) is H_j-measurable, E[D_j(t) | H_{j−1}] = 0, and since
Z̃_j(t) ∈ [−R, R], D_j(t) ∈ [a_j, a_j + 2R] with a_j = −R − m_j(t) H_{j−1}-measurable.
Lemma A with w′ = 2R and λ = δQ gives P(Σ_j D_j(s) ≤ −δQ) ≤ exp(−δ²Q/(2R²)) and, for
t ≠ s, P(Σ_j D_j(t) ≥ δQ) ≤ exp(−δ²Q/(2R²)). Now 2R²/δ² = 500000·R² <
500000·(1 + 2^{−20}) < 500001 < 2^{19}, so δ²Q/(2R²) > n + 4 > (n + 3) ln 2 ≥ ln(8N), and each
probability is < 1/(8N). A union bound over the N events gives probability > 7/8 for

  𝒢₀ = {Σ_j D_j(s) > −δQ} ∩ ⋂_{t<N, t≠s} {Σ_j D_j(t) < δQ}.

Fix a branch in 𝒢₀; let n_b ≤ floor(εQ) ≤ εQ be its number of malformed copies and
n_c = Q − n_b. By Fact E and Lemma K (clean copies) and Lemma M (malformed copies),

  S(s) = Σ_j D_j(s) + Σ_j m_j(s) > −δQ + n_c(1/2 − κ) − n_b(1/2 + η)
       ≥ Q·[(1 − ε)(1/2 − κ) − ε(1/2 + η) − δ] =: Q·Lo,

since the middle expression decreases in n_b, and for t ∈ [0, N), t ≠ s,

  S(t) = Σ_j D_j(t) + Σ_j m_j(t) < δQ + n_c κ + n_b(1/2 + η)
       ≤ δQ + Qκ + n_b(1/2 + η − κ) ≤ Q·[κ + ε(1/2 + η) + δ] =: Q·Hi.

With the bounds above, Lo > 0.167802 > θ₀ = 67/400 = 0.1675 > 0.167262 > Hi. Since
f(t) = 1 ⇔ t < N and 400·2^{22}S(t) > 67·2^{22}Q ⇔ t < N and S(t) > θ₀Q, every branch of 𝒢₀
lies in 𝒢. ∎

### 6.3 Search

**Lemma G (one marked item).** Let n ≥ 1 and let f: [0, 2^n) → {0, 1} have exactly one
w with f(w) = 1. Let ψ₀ = H^{⊗n}|0^n⟩, 𝒪 = Σ_t (−1)^{f(t)}|t⟩⟨t| and 𝒟′ = 2|ψ₀⟩⟨ψ₀| − I, and let
β ∈ (0, π/2] with sin β = 2^{−n/2}. Then for every k ≥ 0, (𝒟′𝒪)^k ψ₀ = sin((2k+1)β)|w⟩ +
cos((2k+1)β)|w̄⟩, where |w̄⟩ = (ψ₀ − sin β|w⟩)/cos β for n ≥ 1 (cos β > 0) is a unit vector
orthogonal to |w⟩, so measuring gives w with probability sin²((2k+1)β).

*Proof.* ψ₀ = cos β|w̄⟩ + sin β|w⟩ with |w̄⟩ the normalised uniform superposition of the
2^n − 1 unmarked basis states. On the plane P = span{|w̄⟩, |w⟩}, 𝒪 is the reflection that fixes
|w̄⟩ and negates |w⟩, and 𝒟′ is the reflection that fixes ψ₀ and negates the unit vector of P
orthogonal to ψ₀; both map P to itself. In the basis (|w̄⟩, |w⟩), 𝒪 = diag(1, −1) and
𝒟′ = [[cos 2β, sin 2β], [sin 2β, −cos 2β]] (the reflection fixing (cos β, sin β)), so
𝒟′𝒪 = [[cos 2β, −sin 2β], [sin 2β, cos 2β]], the rotation by 2β, so (𝒟′𝒪) rotates ψ₀ (angle β from |w̄⟩ towards
|w⟩) to the angle (2k+1)β after k steps. ∎

The circuit 𝒟 of Section 4.7 equals −𝒟′, so G^k = (−1)^k (𝒟′𝒪)^k and the measurement law
is the same.

**Lemma I (iteration count).** For n ≥ 4, k_G = floor(785K/1000) with K = floor(2^{n/2})
satisfies π/4 < (2k_G + 1)β < 3π/4, so sin²((2k_G + 1)β) > 1/2.

*Proof.* Let x = 2^{−n/2} ≤ 1/4. Then x ≤ β = arcsin x ≤ x/√(1 − x²) ≤ x(1 + x²) ≤ (17/16)x,
using arcsin x = ∫₀^x dz/√(1 − z²) and (1 + x²)²(1 − x²) = 1 + x² − x⁴ − x⁶ ≥ 1 for x² ≤ 1/16.
Also 1/x − 1 < K ≤ 1/x and 0.785K − 1 < k_G ≤ 0.785K. Upper:
(2k_G + 1)β ≤ (1.57K + 1)(17/16)x ≤ (1.57 + x)(17/16) ≤ 1.82·1.0625 < 1.94 < 3π/4.
Lower: (2k_G + 1)β ≥ (1.57K − 1)x > 1.57 − 2.57x ≥ 1.57 − 0.6425 > 0.92 > π/4. On
[π/4, 3π/4], sin² ≥ 1/2. ∎

**Theorem 2.** For every N ≥ 2, every s ∈ Z/NZ and every adversary of Section 5 with
ε = 33/100, ROB-G outputs s with probability at least 49/64 > 2/3.

*Proof.* Condition on the stored records; the output phase uses only them and fresh
qubits. On 𝒢 (Theorem 1), f marks exactly s. If n ≤ 3, the scan outputs the smallest t with
f(t) = 1, which is s. If n ≥ 4, each repetition is an independent run of the circuit on fresh
qubits; by Section 4.7 it applies H^{⊗n} and G^{k_G} with G = −𝒟′𝒪, so by Lemmas G and I it
returns t̂ = s with probability > 1/2, and then f(t̂) = 1 and s is output. A t̂ ≠ s has
f(t̂) = 0 on 𝒢 and is never output. So P(output = s | records) ≥ 1 − (1/2)³ = 7/8 on 𝒢, and
P(output = s) ≥ (7/8)·P(𝒢) > (7/8)² = 49/64. ∎

This holds for every N ≥ 2 (no threshold), every s and every admissible adversary,
in particular for the clean problem (n_b = 0). The success probability is
unconditional: no postselection.

### 6.4 The ceiling 1/3 (proved remark, not part of any claim)

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
an upper bound only (even N, fixed copy count); it locates the 33/100 analysis of Theorems 1–2 (not claimed in this
submission) and is not used anywhere else.

## 7. Resources (every branch)

The loop lengths of Sections 4.4–4.7 (Q, J, r₁, 2^q, n, k_G) depend on n and N only, the
repetition count is at most 3, and every step processes malformed copies exactly like clean
ones, so the bounds below hold on every execution branch, for every adversary.

**Samples.** Step 1 of 4.4 runs exactly Q times and nothing else acquires copies:
**Q = 2^{19}(n + 4) ≤ 5·2^{19} n = O(n)** (n ≥ 1), counting every copy.

**Quantum space.** Acquisition: at most one copy (n + 1 qubits), one test control, the
O(n) ancillas of P1 and one P5 qubit, all released after each test or copy. Output phase:
the n search qubits; U (w qubits); V (p) with the O(p) ancillas of P3a; k (q); v (24) with
the O(q) ancillas of P3e; the O(w) ancillas of P3b; the flags e, g, f with the O(n + w)
carry ancillas of P3c; the diffusion target and its n − 2 ancillas. All search-phase registers form one fixed pool of O(n) wires, allocated once;
"fresh" in Section 4.7 means a pool wire in |0⟩, reused for every j, every call and every repetition. Since p, w = O(log n)
and q is fixed, every item is O(n), and there are O(1) items, **S_Q = O(n)**; every ancilla is
returned to |0⟩ or measured and reset.

**Classical space.**
* Records: Q(n + p + 4) bits (e_j: n + p, m′_j: 3, b_j: 1).
* Table: 2^q·24 = 3·2^{19} bits (the c_k; d_k = c_k + 2^{22} + 1 is formed when read);
  construction workspace: an absolute constant (Section 4.2).
* F workspace, reused per copy: 8(J+1) counters of bitlength(r₁) bits, one x_i of J + 3 bits,
  the constant 2^i mod N, rounding and long-division scratch: O(n log log n + n).
* Output phase controller: K and k_G (n bits each), the iteration and repetition counters
  (O(n)), the loop indices j, i (O(log n)), the current constant c_{j,i} (p bits), n₀, C*, Θ
  (O(log n) bits each), integer-square-root scratch O(n), one gate description (O(log n));
  the classical evaluation of f(t̂) needs O(p + w + log n) bits. Gates are emitted and applied
  one at a time.
* Parameters N, n, J, L₁, r₁, Q, p, w: O(n).

**S_C ≤ 2^{19}(n + 4)(n + p + 4) + 3·2^{19} + O(n log log n + n) = O(n²).** Hence M (allocated
bits plus qubits) = O(n²) and the address charge is A = ceil(log₂(M + 2)) = O(log n).

**Work.** Each counted operation costs O(A).
* Parameters and table: O(n A) and an absolute constant number of operations, i.e. O(A).
* Acquisition, per copy: acquiring the copy costs n + 1. F runs 8(J+1)r₁ tests, and
  r₁ = 200 L₁ with L₁ < log₂(n + 1) + 25, so O(n log n) tests. Each test allocates a control
  (O(1)), generates and applies the O(n)-gate P1 circuit (O(n)), applies P2 (O(1)) and increments
  a counter (O(log log n)): O(n A) per test. The constants 2^i mod N come from doubling with a
  conditional subtraction (O(n) per level). Lemma P reconstruction is O(J² + J log r₁) and
  rounding O(n²). Steps 3–5 cost O(n A), and the long division for e_j (n + p steps on
  (n + 1)-bit numbers) O(n² A). Per copy O(n² log n · A); over Q copies O(n³ log² n).
* n ≤ 3: the scan evaluates f at most 8 times on Q = O(1) records: O(1) operations, O(A).
* n ≥ 4, per call of 𝒪: for each j, step (a) is n applications of P3a on p qubits with a
  classically extracted constant (shift and mask of e_j, O(p) bit operations): O(np); step (b):
  O(p + q); step (c): P3e, O(2^q(q + 24)) = O(1); step (d): P3b, O(w); step (e) repeats (a)–(c).
  So O(np + w) = O(n log n) per j and O(Q n log n) = O(n² log n) for step 1; the flag and phase
  steps cost O(n + w), and the clean-up repeats step 1. Per call O(n² log n · A).
* Per call of 𝒟: O(n A). Per Grover iteration O(n² log² n). Per repetition at most
  k_G ≤ 0.785·2^{n/2} iterations plus the classical evaluation of f(t̂), O(Q n p · A) =
  O(n² log² n). Three repetitions: O(2^{n/2} n² log² n). K and k_G: O(n² A); n₀, n₁, C*, Θ: O(Q log n + log² n)
  bit operations, once.
* Allocation and initialisation of all memory: O(M A) = O(n² log n).

Since n³ log² n ≤ 2^{n/2} n² log² n for n ≥ 4 (as n ≤ 2^{n/2}), and instances with n ≤ 3 cost
an absolute constant, **T = O(2^{n/2} n² log² n)** with an absolute constant, for all n ≥ 2; the only
instance with n = 1 is N = 2, whose cost is an absolute constant.
All four bounds hold simultaneously on every execution branch of this single algorithm with
this single parameter rule, jointly with Theorem 2.

## 8. Exact growth indices and structured envelopes

For B(n) = 2^{cn} n^a (log n)^b with fixed c > 0 and a, b ≥ 0: log₂ B = cn + a log n + b log log n,
so log₂ log₂ B / log₂ n = 1 + log₂(c + (a log n + b log log n)/n)/log₂ n → 1, and g(B) = 1. For
B(n) = n^a with fixed a > 0 the ratio tends to 0 and g(B) = 0. Fixed outer constants do not change
either value.

* T: B_T(n) = 2^{n/2} n² (log₂ n)², index **1**; structured: coefficient 1, exponent
  [{coefficient 1/2, nPower 1, logPower 0}], nPower 2, logPower 2.
* S_C: B_C(n) = n², index **0**; exponent [], nPower 2, logPower 0.
* S_Q: B_Q(n) = n, index **0**; exponent [], nPower 1, logPower 0.
* Q: B_samples(n) = n, index **0**; exponent [], nPower 1, logPower 0 (explicitly
  Q = 2^{19}(n + 4)).

Published time score: [1]. ROB-G's contribution is the joint guarantee: work 2^{n/2} up to
polynomial factors, O(n) copies, O(n) qubits, O(n²) bits, on clean input (the fifth claim); the same proof also tolerates a
fraction 33/100 of adaptively placed, arbitrarily entangled malformed copies under the model of
Section 5, just under the 1/3 ceiling of Proposition U, which is claimed in a5c17989, not here. Prior work: O(log N) clean copies suffice information-theoretically
(Ettinger–Høyer, Adv. Appl. Math. 25 (2000); Ettinger–Høyer–Knill, IPL 91 (2004)); quantum
search is Grover's (STOC 1996), with the standard two-reflection analysis (Boyer–Brassard–
Høyer–Tapp, Fortschr. Phys. 46 (1998)), reproved here as Lemma G; Lemma P is a Kitaev-style
iterative phase estimation; Regev (SIAM J. Comput. 33 (2004), Definition 2.1) studies DCP with a
failure parameter, where a bad register is a computational-basis state, a weaker corruption
than the adaptive, arbitrary, entangled copies here. Grover search over candidate shifts with
O(n) saved clean copies already appears on this challenge's board (submission 613ca17b: coherent
shift tests on n + 24 saved copies, T = O(2^{n/2} n⁵), O(n²) qubits, tolerance 0); ROB-G instead
searches over a classical score built from measured records, which is what makes the adaptive
tolerance provable. Sections 1–3, 5, 6.1 (Lemma M) and 6.4 (Proposition U), the cosine table and the
record format are carried over, with the same author, from our ROB+ submission (5d77f276, a
classical scan claiming 33/100 under the adaptive model text of Section 5). New here are the threshold form of the
concentration argument (Theorem 1, with individual rather than difference bounds), the bit-sliced
score V_j with its error bound (Lemma D), the exact reversible oracle 𝒪 and diffusion 𝒟
(Section 4.7, primitives P3a–P3e) and the search analysis (Lemmas G, I, Theorem 2). No cited
result is used in the proof.

## 9. Fractional error tolerance (fifth claim: ε = 0, clean input)

The fifth claim is ε(n) = 0 with the baseline model text: all Q = 2^{19}(n + 4) acquired copies
are independent ideal coset states ρ_s. This is the special case of Section 5 in which the
adversary marks no copy malformed (n_b = 0), so Theorems 1 and 2 give full-secret success
probability at least 49/64 > 2/3 for every N ≥ 2 and every s, jointly with the four resource
bounds of Section 7, which hold on every execution branch. No positive tolerance is asserted in
this submission; this is not a proof that greater tolerance is impossible.

Lineage. Unjudged smoke-era submissions on this repository (branches submissions/*) already
combined per-copy classical records, a robust threshold score, O(n) copies and quantum search,
under the historical count grammar and a fixed-position corruption model: RGRST1 (be98e61b),
CGRST1 (53b4755b), CADGR1 (5f048e8b, b838e1ae), CADGR2 (45044787), RLQGR1–3 (ee378bae, 635a47e2,
0e1559e4, 09c05313, 7b2afdfc). The production entry 613ca17b uses Grover over coherent shift
tests on n + 24 saved clean copies (T = O(2^{n/2} n⁵), O(n²) qubits). None of their text is
used here.

## 10. Constant summary

q = 16; p = q + 1 + bitlength(n); w = bitlength(Q) + 26; table precision τ = 2^{−22};
π̃ = 103993/33102; Taylor degree 40; r₁ = 200 L₁ with L₁ = bitlength(16(J+1)·10⁶), so
p_F < 10^{−6}; J = max(1, n−2); Q = 2^{19}(n+4); δ = 1/500; ε = 33/100; θ₀ = 67/400;
η < 1.4412·10^{−4}; R = 1 + 2^{−22}; κ < 1.4613·10^{−4}; 2R²/δ² < 500001 < 2^{19};
Lo > 0.167802 > θ₀ > 0.167262 > Hi; K = floor(2^{n/2}), k_G = floor(785K/1000); success
≥ 49/64. Each inequality is derived in the text above; no step depends on computation outside
this file.
