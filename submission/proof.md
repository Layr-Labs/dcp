# OMX-ML: an exact offset-mixing sieve with multi-level readout, O(2^{2√n} n^{13/2}/log n) work for every N

This file is the complete proof of all five claims in `submission.json`. It
describes one algorithm, **OMX-ML** (below simply OMX), with one fixed parameter rule, and proves for
every integer N ≥ 2 and every s ∈ Z/NZ, with n = ceil(log₂ N):

* the output equals s with unconditional probability > 3/4 (hence ≥ 2/3);
* total work T = O(2^{2√n} n^{13/2}/log n);
* peak classical space S_C = O(2^{2√n} n^{7/2}) bits;
* peak quantum space S_Q = O(2^{2√n} n^{5/2}) qubits;
* total acquired source copies Q = O(2^{2√n} n^{7/2}/log n); explicitly
  Q < 2^{35}·2^{2√n}·n^{7/2}/log₂ n for n ≥ 256 and Q ≤ N(n+2) < 2^{264} for n < 256;
* malformed-copy fraction ε(n) = 0 (all copies clean).

All constants are absolute (independent of N, s and all outcomes). Every
execution branch obeys the bounds: the algorithm has explicit caps and outputs 0
(an abort, counted as failure) whenever a cap would be exceeded. Logarithms are
base 2 unless written ln; e is Euler's number. All four growth indices equal
1/2; the inner coefficient 2 of √n is proved (fact S5), not a hidden constant.

**Contribution and comparison.** The method is a pairwise label sieve in the
spirit of Kuperberg (SIAM J. Comput. 35 (2005) 170–188), whose complete proof
(Thm 3.1) covers N = 2^n with O(8^{√n}) queries, while its general-N results
(Thms 5.1, 7.1, constant ≈ 1.78 in 2^{c√n}) are stated with proof sketches.
Nothing from that paper is used as a premise here. We claim a complete,
Clifford+T-exact analysis for **every** N with the explicit exponent 2√n. The
new ingredient is **offset mixing** (Lemma M): the partner of each anchor is
taken from a block at a uniformly random offset Δ ∈ {−m,…,m}, and the mixture of
the shifted triangular laws is *exactly* uniform on an interval, accepted with
probability 2m/(2m+1). With a lift u ↦ u + kN that supplies as many exactly
uniform label bits as needed for any N, every stage keeps the label law exactly
uniform without a flattening step and loses only a factor 4(1 + O(1/√n)): two
labels per output and one fair coin. **Multi-level readout:** a finished run with level j
has final cofactors exactly uniform on [−m, m), so the records with ξ = ±2^i for i < μ give
labels 2^{j+i}; each run serves up to μ levels (all but possibly the last serve exactly μ), and
ρ = ceil((n−1)/μ) runs (instead of n − 1) suffice. This saves a factor (n−1)/ρ (asymptotically μ,
with μ ≥ (1/2)log₂ n) in Q and T. It is a logarithmic refinement, not a change of exponent: index
1/2 is already known, by Regev (quant-ph/0406151) with polynomial space for N = 2^n and Kuperberg
(arXiv:1112.3333) with polynomial quantum space using QRACM; our point is a fully proved,
every-N, model-exact explicit bound.

Notation. frac(φ) ∈ [0,1); |φ|∘ = min_{z∈Z} |φ − z| (circular distance). For an
integer v let φ(v) = (|0⟩ + e^{2πi v s/N}|1⟩)/√2 (a *label-v qubit*; only v mod N
matters). bitlength(x) is the number of binary digits of an integer x ≥ 1, so
2^{bitlength(x)} > x and e^{−bitlength(x)} < 2^{−bitlength(x)} < 1/x.

**Memory policy.** Every measured, reset or discarded qubit or classical buffer is
released immediately and may be reused; test controls and P5 coins use one
reusable wire each. Circuits are generated gate by gate and executed as
generated; no circuit description is stored beyond O(n) words of loop state.

## 1. Primitive operations (exact Clifford+T)

**P1 (controlled modular addition of a constant).** For a classical constant
a ∈ [0, N) let g_a(y) = (y + a) mod N for y < N and g_a(y) = y for N ≤ y < 2^n.
Controlled by one qubit, g_a is implemented with O(n) NOT/CNOT/Toffoli gates and
O(n) ancillas: a ripple-carry adder (e.g. Cuccaro–Draper–Kutin–Moulton,
quant-ph/0410184) on n+1 bits computes y + a − N; its sign bit selects, by one
controlled re-addition of N, the value (y + a) mod N; a comparator with N gates
the operation so that every y ≥ N is fixed; scratch bits are cleared by running
the comparisons in reverse. Toffoli has an exact constant-size Clifford+T
decomposition. A uniform generator emits the O(n) gates from the n-bit
constants a, N; each emitted gate names O(1) wires of O(log S) bits, so generation
costs O(n log S) bit operations. Only the action on y < N is used below.

**P2 (phase test).** For a qubit (|0⟩ + e^{2πiφ}|1⟩)/√2 and m′ ∈ {0,…,7}, apply
(T†)^{m′} = diag(1, e^{−2πi m′/8}), then H, then measure. Outcome 0 has probability
exactly p_{m′}(φ) = (1 + cos(2π(φ − m′/8)))/2.

**P3 (combination).** Given label-v₁ and label-v₂ qubits in a product state,
apply CNOT (control the first) and measure the target. With α₁ = 2πv₁s/N and
α₂ = 2πv₂s/N the state before measurement is
(|00⟩ + e^{iα₂}|01⟩ + e^{iα₁}|11⟩ + e^{i(α₁+α₂)}|10⟩)/2. Outcome 0 (probability exactly
1/2) leaves the control in φ(v₁+v₂); outcome 1 (probability exactly 1/2) leaves
it in (e^{iα₂}|0⟩ + e^{iα₁}|1⟩)/√2, which is φ(v₁ − v₂) up to a global phase. The
outcome is a fair coin independent of v₁, v₂, s and of everything else.

**P4 (sign flip).** X maps φ(v) to φ(−v) up to a global phase.

**P5 (fair bits).** A fresh |0⟩, H, measurement: an exact fair bit, O(1) work.

**Cost convention.** Let S be the number of allocated bits plus qubits. Section 8
shows S = O(2^{2√n} n^{7/2}), so a classically indexed access or classically
addressed gate costs A = ceil(log₂(S+2)) = O(√n) bit operations for its address.
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
"control wire prepared in |+⟩, then P1 with a = 2^i mod N on the copy's register"
maps the control to (|0⟩ + e^{2πi 2^i u/N}|1⟩)/√2 and leaves the copy unchanged.
Repeated such tests on one copy are independent given u (the register is an
exact eigenvector and the control wire is re-prepared each time).

## 3. Lemma P (phase reconstruction from dyadic multiples)

Let J, r ≥ 1. Suppose that for each level i ∈ {0,…,J} and each m′ ∈ {0,…,7} we
obtain r independent outcomes of P2 with this m′ applied to qubits
(|0⟩ + e^{2πi 2^i φ}|1⟩)/√2, for an unknown real φ. Let Z_{i,m′} be the number of 0
outcomes. Procedure: m_i = the m′ maximising Z_{i,m′} (smallest on ties),
γ_i = m_i/8; x_J = γ_J; for i = J−1 down to 0, of c₀ = x_{i+1}/2 and
c₁ = x_{i+1}/2 + 1/2 let x_i be the one with smaller |c − γ_i|∘ (c₀ on ties).

**Claim.** With probability at least 1 − 16(J+1)e^{−r/200}, |x₀ − φ|∘ < 2^{−J}/8.

*Proof.* Write φ_i = frac(2^i φ). Hoeffding's inequality (Hoeffding, JASA 58
(1963), Thm 2, for sums of independent [0,1] variables) gives
P(|Z_{i,m′}/r − p_{m′}(φ_i)| ≥ 1/20) ≤ 2e^{−2r/400}; a union bound over the 8(J+1)
pairs gives the failure bound. Assume all deviations are < 1/20.
(a) The nearest grid point m*/8 has |φ_i − m*/8|∘ ≤ 1/16, so
p_{m*} ≥ (1 + cos(π/8))/2 > 0.9619; every m′ with |φ_i − m′/8|∘ ≥ 1/8 has
p_{m′} ≤ (1 + cos(π/4))/2 < 0.8536. The gap exceeds 2/20, so the empirical
maximiser satisfies |γ_i − φ_i|∘ < 1/8.
(b) Induction: |x_i − φ_i|∘ < δ_i := 2^{−(J−i)}/8. True for i = J by (a). Let
|x_{i+1} − φ_{i+1}|∘ < δ_{i+1} ≤ 1/8 and write x_{i+1} − φ_{i+1} = d + z, z ∈ Z,
|d| < δ_{i+1}. Since φ_{i+1} = frac(2φ_i), φ_i ≡ φ_{i+1}/2 + w/2 (mod 1) for some
w ∈ {0,1}, and {c₀, c₁} ≡ {φ_{i+1}/2 + d/2, φ_{i+1}/2 + 1/2 + d/2} (mod 1). So one
candidate is within |d|/2 < δ_i of φ_i and the other is at circular distance
> 1/2 − δ_i ≥ 1/2 − 1/16. By (a) the good candidate is within < 1/16 + 1/8 = 3/16
of γ_i and the bad one at > 1/2 − 1/16 − 1/8 = 5/16, so the good one is chosen. ∎

All x_i are multiples of 2^{−(J+3)}: the procedure is exact (J+3)-bit integer
arithmetic, O(J²) bit operations.

**Corollary P′.** Take J = n − 2 and φ = a/N for an integer a. On the success
event N x₀ differs from a + Nz (some z ∈ Z) by less than N·2^{−(n−2)}/8 =
N/2^{n+1} ≤ 1/2, so round(N x₀) mod N = a mod N, with no tie. N x₀ is an exact
rational with denominator 2^{n+1}; rounding costs O(n²) bit operations.

## 4. Lemma M (offset mixing)

Let m, K ≥ 1 be integers. Let Δ be uniform on {−m,…,m} and σ, σ′ uniform on
{0,…,K−1}, all three independent, and ξ = ΔK + σ − σ′. Then

  P(ξ = y) = 1/((2m+1)K)  for every integer y with −mK ≤ y < mK,

so P(−mK ≤ ξ < mK) = 2m/(2m+1), and conditioned on that event ξ is exactly
uniform on the 2mK integers of [−mK, mK).

*Proof.* x = σ − σ′ has P(x = z) = (K − |z|)/K² for |z| ≤ K−1. Write y = qK + ρ with
0 ≤ ρ < K; then −m ≤ q ≤ m − 1. ξ = y requires x = y − ΔK ∈ [−(K−1), K−1], i.e.
Δ = q (x = ρ) or, if ρ ≥ 1, Δ = q+1 (x = ρ − K). Both values of Δ lie in
{−m,…,m}. Hence (2m+1)·P(ξ = y) = (K − ρ)/K² + ρ/K² = 1/K (for ρ = 0 the second
case is absent and its term ρ/K² is 0). Summing over the 2mK values gives
2m/(2m+1). ∎

## 5. Algorithm OMX

**Small inputs.** If n < 256, run exhaustive shift testing (Section 5.6). This is
a fixed finite prefix of the algorithm (N ≤ 2^{255}); its costs are absolute
constants.

### 5.1 Parameters (n ≥ 256)

All are integers computed exactly from n:

* g = the least integer with g² ≥ n, so 16 ≤ g ≤ √n + 1 ≤ (17/16)√n;
* μ = ceil(log₂ g) and **m = 2^μ**, so g ≤ m < 2g and m ≥ 16;
* p₀ = 2μ + 2 (minimum block bits), so 2^{p₀} = 4m²;
* λ = 2g + 4·bitlength(n) + 48;
* **ν = 256 g² λ** (minimum mean bucket load);
* L = bitlength(256n), r = 200L;
* **R = g** stages per run; **M_R = 2^{p₀+1} ν = 8m²ν**;
  M_{t−1} = ceil((4 + 32/g) M_t) + 8 for t = R, …, 1;
* b_t = floor(log₂(M_{t−1}/ν)) for t = 1, …, R (bucket bits of stage t);
* H = Σ_{t=1}^{R} (b_t − μ − 1) + μ + 1 and E = H − n + 1;
* **ρ = ceil((n−1)/μ)** runs, with targets j = qμ for q = 0, …, ρ−1;
* Q* = 4ρ M_0; L₁ = bitlength(256 n Q*); r₁ = 200 L₁.

### 5.2 Procedure F (a fresh lifted label)

Acquire one source copy (cost n+1). For i = 0..n−2 and m′ = 0..7 perform r₁ phase
tests (Section 2, with a = 2^i mod N) followed by P2 with this m′. Apply Lemma P
(J = n−2, r = r₁) and Corollary P′ to obtain û ∈ [0, N). Measure the copy's
n-qubit register, reset and release it and all ancillas; keep its first qubit.
Draw E fair bits forming k ∈ [0, 2^E) (P5) and set d = û + kN. If d < 2^H, **keep**:
the first qubit with cofactor c = d (level ℓ = 0, offset c₀ = 0). Otherwise
measure, reset and release that qubit too.

### 5.3 List records

A record is a qubit index and a cofactor c ∈ [0, X), stored with the run-wide
level ℓ and offset c₀; its label value is v = 2^ℓ(c − c₀), and its qubit is meant
to be φ(v). A kept copy has v = d, and φ(d) = φ(û) because d ≡ û (mod N).

### 5.4 Stage t of a run (input list W_{t−1} of M_{t−1} records, all with X = X_{t−1})

The stage has integers w = w_t ≥ 0 (low bits) and p = p_t = b_t − w ≥ p₀ (block
bits), with X = 2^w 2^p K for an integer K = K_t ≥ 1 (a power of two). Put P = 2^p
and B = 2^{b_t} = 2^w P. Write each cofactor uniquely as

  c = 2^w (hK + σ) + κ,   κ ∈ [0, 2^w), h ∈ [0, P), σ ∈ [0, K).

Its **key** is (κ, h); h is its block.

1. *Split.* Anchors 𝒜 = the first |𝒜| = floor((1/2 − η)M_{t−1}) records, with
   η = 1/(8g); reservoir ℛ = the other records. Sort ℛ stably by key into B
   buckets (counting sort).
2. *Pair.* For each anchor a in list order: if h_a < m or h_a ≥ P − m, discard it
   (measure, reset, release). Otherwise draw Δ uniform on {−m,…,m}: repeatedly
   draw μ+2 fair bits forming ζ ∈ [0, 4m) and stop at the first ζ ≤ 2m, setting
   Δ = ζ − m; **abort** if λ draws fail. Take the first unused reservoir record b
   with key (κ_a, h_a − Δ); **abort** if there is none. Apply P3 with a as control
   and b as target. Outcome 0: discard both. Outcome 1: compute
   ξ = (c_a − c_b)/2^w (exact, since κ_a = κ_b); then ξ = ΔK + σ_a − σ_b. If
   −mK ≤ ξ < mK, *accept*: output the anchor's qubit with new cofactor
   c′ = ξ + mK. Otherwise discard it.
3. *Output.* W_t = the first M_t accepted outputs in anchor order; **abort** if
   there are fewer; discard the rest and all unused reservoir records. Set
   X_t = 2mK, ℓ ← ℓ + w, c₀ ← mK.

The new label value is 2^{ℓ+w}(c′ − mK) = 2^{ℓ+w} ξ = 2^ℓ(c_a − c_b) = v_a − v_b,
which is exactly the label of the anchor's qubit after outcome 1 of P3.

### 5.5 Run j and output

For a target j = qμ (q ∈ {0, …, ρ−1}, so 0 ≤ j ≤ n−2): choose w_t greedily, w_t = min(b_t − p₀, j − Σ_{s<t} w_s),
and p_t = b_t − w_t. (Fact S3 gives Σ_t w_t = j.)

1. Call F until M_0 copies are kept or 4M_0 copies have been acquired; abort if
   fewer than M_0 are kept. This is W_0 (X_0 = 2^H, ℓ = 0, c₀ = 0).
2. Run stages t = 1, …, R.
3. Now ℓ = j, X_R = 2m and c₀ = m: every final record has ξ = c − m ∈ [−m, m).
   Let I_j = {i : 0 ≤ i < μ, j + i ≤ n − 2}. For each i ∈ I_j the values ±2^i are two
   distinct elements of [−m, m) (2^i ≤ m/2). Abort if for some i ∈ I_j fewer than 8r
   records have ξ ∈ {−2^i, 2^i}. For each i ∈ I_j take the first 8r of them (these sets
   are disjoint) and apply X (P4) to those with ξ = −2^i; each now carries label
   exactly 2^{j+i}, since X maps φ(v) to φ(−v) up to a global phase. For m′ = 0..7
   apply P2 with this m′ to r of them and record Z_{j+i,m′}. Release all qubits of
   the run.

The levels j + i (q < ρ, i ∈ I_{qμ}) are exactly 0, …, n−2, each once. After the ρ runs,
apply Lemma P (J = n−2, this r) and Corollary P′ to the counts with φ = s/N and output
round(N x₀) mod N.

### 5.6 Exhaustive shift testing (n < 256 only)

For t′ = 0, …, N−1 perform n+2 tests, each on a fresh copy: controlled on the first
qubit, apply y ↦ (y − t′) mod N (y < N; identity on y ≥ N), i.e. P1 with
a = (N − t′) mod N, to the register, then measure the first qubit in the X basis.
Reject t′ at the first outcome −; output t′ if all n+2 outcomes are +; output 0 if
no t′ passes. For t′ = s each component becomes |+⟩|x⟩, so every test passes; for
t′ ≠ s the two register basis states differ, the first qubit is I/2 and each test
passes with probability exactly 1/2. A wrong t′ passes with probability 2^{−(n+2)},
so by a union bound the output is wrong with probability ≤ (N−1)2^{−(n+2)} < 1/4.
At most N(n+2) < 2^{264} copies are used, with O(N n²) work and O(n) bits and
qubits: absolute constants, since n < 256.

## 6. Schedule facts (n ≥ 256)

**S1.** M_{t−1} ≥ 4M_t ≥ 4M_R, so M_{t−1} ≥ 4^{R−t+1} M_R; and M_t ≥ M_R ≥ 9g.

**S2.** b_t ≥ 2(R−t+1) + p₀ + 1 for every t, since M_{t−1}/ν ≥ 4^{R−t+1} 2^{p₀+1} by
S1. In particular p_t = b_t − w_t ≥ p₀, because w_t ≤ b_t − p₀.

**S3.** Σ_{t=1}^{R} (b_t − p₀) ≥ Σ_t 2(R−t+1) = R(R+1) ≥ g² ≥ n > j, so the greedy rule
reaches Σ_t w_t = j exactly.

**S4.** By induction from log₂ X_0 = H and log₂ X_t = log₂ X_{t−1} − b_t + μ + 1,
log₂ X_{t−1} = b_t + Σ_{s>t}(b_s − μ − 1) ≥ b_t (each term is ≥ p₀ + 1 − μ − 1 > 0
by S2). So K_t = X_{t−1}/2^{b_t} is an integer power of two ≥ 1, X_t = 2mK_t, and
log₂ X_R = μ + 1, i.e. X_R = 2m and K_R = 1. Also H ≥ Σ_t(b_t − p₀) ≥ n, so E ≥ 1.

**S5 (size).** M_{t−1} ≤ (4 + 32/g)M_t + 9 ≤ (4 + 33/g)M_t (as M_t ≥ 9g), so
M_0 ≤ (4 + 33/g)^g M_R = 4^g (1 + 33/(4g))^g M_R ≤ e^{33/4} 4^g M_R < 3900·4^g M_R.
Since g ≤ √n + 1, 4^g ≤ 4·2^{2√n}. With m < 2g, g⁴ ≤ (17/16)⁴ n² ≤ 1.28 n² and
λ ≤ 8√n (for n ≥ 256: 2g ≤ 2.125√n, 4·bitlength(n) ≤ 4 log₂ n + 4 ≤ 2√n + 4 and
52 ≤ 3.25√n), M_R = 8m²·256g²λ ≤ 8192 g⁴ λ < 2^{17} n^{5/2}. Hence

  M_0 < 2^{31} · 2^{2√n} · n^{5/2}.

  Runs: m = 2^μ ≥ g ≥ √n gives μ ≥ (1/2)log₂ n, so ρ ≤ (n−1)/μ + 1 < 2n/log₂ n + 1
  ≤ (9/4)n/log₂ n (as n ≥ 4 log₂ n), and also ρ ≤ n − 1 (μ ≥ 1). Hence
  Q* = 4ρM_0 < 2^{35} · 2^{2√n} · n^{7/2}/log₂ n, and also Q* < 2^{33} · 2^{2√n} · n^{7/2}.

**S6 (union-bound budget).** 2^{−λ} = 2^{−2g}·2^{−4 bitlength(n)}·2^{−48}
≤ 2^{−2√n} n^{−4} 2^{−48}, so 8 Q* 2^{−λ} < 2^{36−48} n^{−1/2} < 2^{−12}.

**S7 (widths).** b_t ≤ log₂ M_0 ≤ 2√n + 31 + (5/2)log₂ n ≤ 5.2√n for n ≥ 256, so
H ≤ Σ_t b_t ≤ g·5.2√n ≤ 6n, and every cofactor has at most 6n bits; E ≤ 6n.

As a sanity check only (not used in the proof), S1–S7 were also evaluated exactly for n = 256, 300, 10³, 4096, 10⁴, 10⁵, 10⁶.

## 7. Correctness

**Chernoff bounds used** (Mitzenmacher–Upfal, *Probability and Computing*, 2nd
ed., Thms 4.4 and 4.5). For X a sum of independent indicators with mean μ and
0 < δ ≤ 1: P(X ≤ (1−δ)μ) ≤ e^{−δ²μ/2}, and P(X ≥ (1+δ)μ⁺) ≤ e^{−δ²μ⁺/3} for every
μ⁺ ≥ μ (add independent indicators with total mean μ⁺ − μ; this only increases X).

**Ideal process.** Let I be the same procedure except that (i) every decision uses
the true label u of each copy from (2.1) in place of û; (ii) Δ draws are unlimited;
(iii) if an anchor's target bucket has no unused reservoir record, the partner is
a *phantom* record with that key, an independent uniform σ ∈ [0, K) and a
fictitious qubit in state φ(v_b) for its label value v_b. I need not be physically
realisable; it is a well-defined random process on labels, coins, offsets and
outcomes, in which every P3 coin is a fair bit and every final P2 outcome on a
record of label v is 0 with probability p_{m′}(vs/N), independently given the
history, exactly as in A by P2, P3 and the product-state claim of Lemma U.
Couple the actual algorithm A and I on one probability space: draw one i.i.d.
sequence of uniform [0,1) variables and generate every label u of (2.1), fair bit
and measurement outcome of A, in order, by inverse-CDF from its conditional law
given the history; I uses the same variables for the same steps, and a separate
independent stream for phantom remainders and for steps after the first bad
event. A and I take identical actions until the first **bad event**: (B1) some
acquired copy has û ≠ u; (B2) some Δ needs more than λ draws; (B3) some anchor finds
its target bucket empty (phantoms occur only at B3). Hence
P_A(success) ≥ P_I(success) − P(B1 ∪ B2 ∪ B3).

**Bad events.** On every branch at most Q* copies are acquired (Section 8). Given u,
F is Lemma P with J = n−2, r = r₁, φ = u/N, so
P(û ≠ u) ≤ 16(n−1)e^{−L₁} < 16n/(256nQ*) = 1/(16Q*); over ≤ Q* copies P(B1) ≤ 1/16.
Each Δ draw succeeds with probability (2m+1)/(4m) > 1/2, so one anchor fails with
probability < 2^{−λ}; anchors are distinct records and Σ_t M_{t−1} ≤ (4/3)M_0 per run
(M_{t−1} ≥ 4M_t), so there are ≤ Q* anchors and P(B2) ≤ Q* 2^{−λ}. P(B3) is bounded
in Lemma X below. By S6, P(B1 ∪ B2 ∪ B3) ≤ 1/16 + 2^{−11}.

**Lemma U (exact uniformity in I).** For a run and t ∈ {0,…,R}, let 𝒢_t be the
σ-algebra generated by everything before the run, the keep decisions of step 1,
and, for every stage s ≤ t, the keys of all records of W_{s−1}, the interior
indicators and P3 coins of the anchors, and the acceptance indicators of the
interior anchors with outcome 1 (anchors that are not interior or have outcome 0
have no acceptance indicator). It does **not** contain the outcomes of the
current run's F tests, the offsets Δ, their draw counts, the partner map or the
remainders σ. (a) Conditioned on 𝒢_t, the cofactors of W_t are independent and
uniform on [0, X_t). (b) Conditioned on the full classical history (including
cofactors and offsets), the qubits of W_t are in the product state ⊗ φ(v) of
their label values.

*Proof.* t = 0: a kept copy has d = u + kN with (u, k) uniform on [0,N) × [0,2^E);
(u,k) ↦ d is a bijection onto [0, 2^E N), so d is uniform there and, conditioned on
d < 2^H (note 2^H = 2^E 2^{n−1} < 2^E N), uniform on [0, 2^H). Copies are
independent, and the first M_0 kept are selected by order only.
Step t ≥ 1. By hypothesis and the bijection c ↔ (κ, h, σ) of [0, X) onto
[0, 2^w) × [0, P) × [0, K), the remainders (σ_r) over the records r of W_{t−1} are
i.i.d. uniform on [0, K) and independent of the σ-algebra ℱ generated by 𝒢_{t−1},
all keys of W_{t−1}, the offsets Δ and the coins of stage t: the offsets and coins
are fresh, and P3's outcome law is 1/2 whatever the labels. Anchors and reservoir
are fixed by list order; the partner map a ↦ b(a) is injective and ℱ-measurable
(it depends on keys and offsets only; a phantom brings its own fresh σ). Hence,
conditioned on ℱ, the pairs (σ_a, σ_{b(a)}) over the paired anchors are i.i.d.
uniform on [0, K)². This conditional law does not depend on the offsets, so these
pairs are independent of the offsets given the keys and coins, and the offsets are
i.i.d. uniform on {−m,…,m}. Therefore, conditioned on 𝒢_{t−1}, the keys and the
coins, the values ξ = ΔK + σ_a − σ_b of the interior anchors with outcome 1 are
i.i.d. with the law of Lemma M. Acceptance only restricts ξ to [−mK, mK), so
conditioned in addition on the acceptance decisions (i.e. on 𝒢_t) the accepted
values are i.i.d. uniform on [−mK, mK), and c′ = ξ + mK is uniform on [0, X_t).
W_t is selected by order and acceptance only. Claim (b) follows from P3 (applied
to disjoint pairs of a product state) and (2.1), the fictitious phantom qubits of
I having the same form. ∎

In particular each anchor independently yields an accepted output with probability
exactly p* = ((P − 2m)/P)·(1/2)·(2m/(2m+1)) (interior test on h_a, fair coin,
Lemma M).

**Lemma X (no exhaustion).** At a stage with M = M_{t−1}, P(some target bucket is
empty in I) ≤ 2B e^{−λ}.

*Proof.* Fix a key (κ, b). Its supply Sup, the number of reservoir records with that
key, is Bin(|ℛ|, 1/B) with |ℛ| ≥ (1/2 + η)M. Its demand Dem, the number of interior
anchors with κ_a = κ and h_a − Δ_a = b, is a sum of independent indicators, each
with probability 2^{−w} Σ_Δ (2m+1)^{−1} P(h_a = b + Δ) ≤ 2^{−w}/P = 1/B; Dem is
independent of Sup (disjoint records, fresh offsets). Put τ = M/(2B). Then
E Sup ≥ (1/2+η)M/B and τ ≤ E Sup/(1+2η) ≤ (1−η)E Sup, so
P(Sup < τ) ≤ e^{−η² E Sup/2}; with μ⁺ = (1/2 − η)M/B ≥ E Dem and
τ = μ⁺/(1−2η) ≥ (1+2η)μ⁺, P(Dem ≥ τ) ≤ e^{−4η²μ⁺/3}. As M/B ≥ ν (definition of b_t)
and η ≤ 1/4, both exponents are ≥ η²ν/4 = λ. If Sup ≥ τ > Dem the bucket never
empties: anchors are served in list order and each takes the first unused record
of its target key, so that bucket is exhausted exactly when Dem > Sup. Hence
P(Dem > Sup) ≤ 2e^{−λ}; sum over the B keys. ∎

The total number of buckets over all stages and runs is ≤ Q*, so with S6,
P(B3) ≤ 2Q*e^{−λ} < 2^{−12}.

**Shortfall events in I.**

* Step 1: each acquired copy is kept independently with probability
  2^H/(2^E N) = 2^{n−1}/N ≥ 1/2; with 4M_0 acquisitions,
  P(fewer than M_0 kept) ≤ e^{−M_0/4}.
* Stage t: the number of accepted outputs is Bin(|𝒜|, p*). Since P ≥ 2^{p₀} = 4m²
  ≥ 4mg and m ≥ g, p* ≥ (1/2)(1 − 1/(2g))². Also |𝒜| ≥ (1/2)(1 − 1/(4g))M_{t−1} − 1.
  With δ = 1/(8g) and (1 − 1/(8g))(1 − 1/(4g)) ≥ (1 − 1/(2g))²,
  (1−δ)|𝒜|p* ≥ (1−δ)p*·(1/2)(1 − 1/(4g))M_{t−1} − (1−δ)p* ≥ (1/4)(1 − 1/(2g))⁴ M_{t−1} − 1 ≥ (1/4)(1 − 2/g)(4 + 32/g)M_t − 1
  ≥ (1 + 5/g)M_t − 1 ≥ M_t (using g ≥ 16 and M_t ≥ 9g). So P(fewer than M_t) ≤
  e^{−δ²|𝒜|p*/2} ≤ e^{−M_t/(128g²)} ≤ e^{−M_R/(128 g²)} ≤ e^{−λ}, as M_R = 8m²·256g²λ.
* Step 3: by Lemma U the final values ξ are i.i.d. uniform on [−m, m), so for each
  i ∈ I_j, #{ξ ∈ {±2^i}} ~ Bin(M_R, 1/m) with mean θ = 8mν ≥ 16r (ν ≥ 256λ and λ ≥ L);
  P(fewer than 8r) ≤ P(fewer than θ/2) ≤ e^{−θ/8} ≤ e^{−2r}; a union bound over the
  |I_j| ≤ μ values gives ≤ μe^{−2r}.

Per run these sum to ≤ e^{−M_0/4} + g e^{−λ} + μe^{−2r}; over ρ ≤ n−1 runs this is
< 1/64 (e^{−λ} < 2^{−λ} < 2^{−48}/n⁴ and e^{−2r} < (256n)^{−400}).

**Final estimate in I.** Let I′ extend I so that a run that would abort for a
shortfall instead continues and, for every level j + i (i ∈ I_j) that lacks 8r real records, or
for every level of the run if it stops before step 3, supplies 8r dummy fresh ideal qubits of label
2^{j+i} (an analysis device); I and I′ agree off the shortfall events. In I′, for every level
i′ ∈ {0, …, n−2} the unique run with i′ = j + i, i ∈ I_j, supplies 8r qubits exactly equal
to (|0⟩ + e^{2πi 2^{i′} s/N}|1⟩)/√2, r for each m′, in a product state given the full
classical history (Lemma U(b), P4). Lemma P needs only that each count Z_{i′,m′} is a sum
of r independent indicators with mean p_{m′}(frac(2^{i′}s/N)) given the history, which this
gives. This is Lemma P with J = n−2, r = 200L, φ = s/N: failure
≤ 16(n−1)e^{−L} < 16n/(256n) = 1/16, and on success Corollary P′ outputs s. Hence
P_I(failure) ≤ P(shortfall) + P_{I′}(Lemma P fails).

**Total.** P_I(failure) ≤ 1/16 + 1/64, so P_A(success) ≥ 1 − 1/16 − 1/64 − 1/16 −
2^{−11} > 3/4 for every N ≥ 2 and s (Section 5.6 gives > 3/4 for n < 256).
This is unconditional: no postselection; every abort counts as failure.

## 8. Resources (every branch)

For n < 256 all costs are absolute constants (Section 5.6). Let n ≥ 256.

**Samples.** Each run acquires at most 4M_0 copies and there are ρ runs and no
other acquisitions: Q ≤ Q* = 4ρM_0 < 2^{35} 2^{2√n} n^{7/2}/log₂ n (S5), counting every
discarded copy and every aborted run. So **Q = O(2^{2√n} n^{7/2}/log n)**.

**Quantum space.** By the memory policy, live qubits at any time are at most the
M_0 label qubits of the current run's list (lists only shrink), one copy's n+1
qubits, one control wire, one coin wire and O(n) adder ancillas; everything is
released between runs. **S_Q ≤ M_0 + O(n) = O(2^{2√n} n^{5/2})**.

**Classical space.** A record has a cofactor of ≤ 6n bits (S7) and a qubit index of
O(√n) bits: lists take O(n M_0) bits. Bucket arrays have B ≤ M/ν entries of O(√n)
bits; the counters Z_{i,m′} (8(n−1) of O(log r₁) bits), the (n+1)-bit x_i, the
parameters (R+1 values M_t of O(√n) bits), the table 2^i mod N (O(n²) bits) and the
gate-by-gate generator state take O(n²). **S_C = O(n M_0) = O(2^{2√n} n^{7/2})**.
Hence S = O(2^{2√n} n^{7/2}) and A = O(√n).

**Work.**
* Procedure F per copy: 8(n−1)r₁ = O(n L₁) = O(n^{3/2}) tests (L₁ = O(√n) because
  log₂ Q* = 2√n + O(log n)). Each test generates and applies O(n) gates at O(log S)
  generation cost and O(A) execution cost each: O(n^{3/2}) per test, O(n³) per copy.
  Lemma P and rounding: O(n² A); the lift d = û + kN (E ≤ 6n) and the comparison
  with 2^H: O(n² A) = O(n^{5/2}). Over ≤ Q* copies: O(n³ Q*) = O(2^{2√n} n^{13/2}/log n).
* Sieve: per record and stage, key extraction, counting sort, ≤ λ draws of μ+2 bits,
  one P3, an O(n)-bit subtraction and comparison, copying and releasing:
  O((n + λ log n)A) = O(n^{3/2}). Records per run Σ_t M_{t−1} ≤ (4/3)M_0; bucket
  arrays add O(B) ≤ O(M) per stage; ρ ≤ n runs: O(n^{5/2} M_0) = O(2^{2√n} n^5).
* Step 3 (scan of M_R records, 8rμ tests), final reconstruction, the table
  2^i mod N, parameter computation: O(M_R n A + n r A + n² A) per run.
* Allocation, initialisation and release, repeated in each of the ρ ≤ n runs:
  O(n·S·A) = O(2^{2√n} n^5).

**T = O(n³ Q*) = O(2^{2√n} n^{13/2}/log n)** (the other terms are O(2^{2√n} n^5)). All four bounds hold simultaneously on every
execution branch of this single algorithm with this single parameter rule.

## 9. Exact growth indices and structured envelopes

For B(n) = 2^{2√n} n^k (log₂ n)^e with fixed k ≥ 0 and e ∈ {−1, 0}:
log₂ B = 2√n + k log₂ n + e log₂ log₂ n, and log₂(log₂ B) = (1/2)log₂ n +
log₂(2 + (k log₂ n + e log₂ log₂ n)/√n). The last term tends to
log₂ 2 = 1, so log₂(log₂ B)/log₂ n → 1/2 and g(B) = 1/2 (the max{4,·} in the
definition is irrelevant for large n). Fixed outer constants do not change it.
Indices: T 1/2, S_C 1/2, S_Q 1/2, Q 1/2; published score [1/2].

Structured envelopes (big-O, outer coefficient 1, one exponent term with
coefficient 2, nPower 1/2, logPower 0):
T: nPower 13/2, logPower −1; S_C: nPower 7/2, logPower 0; S_Q: nPower 5/2, logPower 0;
Q: nPower 7/2, logPower −1.

## 10. Fractional error tolerance

The analysis assumes that every acquired copy is an independent ideal coset state
(2.1). It proves the malformed-fraction guarantee ε(n) = 0, i.e. at most
floor(0·Q) = 0 malformed copies, for all N ≥ 2 with no validity threshold and no
adversary model, jointly with the four bounds above for the same algorithm. No
positive tolerance is claimed; this is not a claim that positive tolerance is
impossible.
