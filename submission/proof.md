# Offset-tracking Kuperberg subtraction sieve with phase estimation

All logarithms are base 2 unless written ln. The algorithm below (called
**OTS**, offset-tracking sieve) is one fixed algorithm with one fixed parameter
choice, used for all five claims.

## 0. Summary of claims

For every N ≥ 2 and every s ∈ Z/NZ, with n = ceil(log₂ N), OTS outputs s with
unconditional probability at least 3/4, and on **every** execution branch

- Q(N,s) ≤ n·L₀ ≤ C_Q · 2^{4√n} · n source copies (L₀ defined in §1),
- T(N,s) = O(2^{5√n}),
- S_C(N,s) = O(2^{4√n} · n) classical bits,
- S_Q(N,s) = O(2^{4√n}) qubits,

with absolute constants. All four envelopes have growth index exactly 1/2
(§8). The proof assumes clean, independent ideal coset states (tolerance 0, §10).

The construction is Kuperberg's subtraction sieve (G. Kuperberg, "A
subexponential-time quantum algorithm for the dihedral hidden subgroup
problem", SIAM J. Comput. 35(1):170–188, 2005; arXiv quant-ph/0302112): label
qubits are combined two at a time by a parity measurement, keeping the
"difference" outcome. Two modifications make a fully distribution-free,
worst-case analysis possible for every N (not only powers of two):
pairs are chosen by pigeonhole on a magnitude bucket (no uniformity of
intermediate labels is used), and the target label is reached through a
random offset bit whose posterior independence is proved in §4. The final
read-out is Kitaev-style phase estimation from labels 2^j mod N (§6). Every
lemma needed is proved in this file; the only cited external results are
the approximate QFT over Z_N and Solovay–Kitaev gate synthesis (§7).

## 1. Notation, parameters and the algorithm

Let ω = e^{2πi/N}. For k ∈ Z/NZ write |φ_k⟩ = (|0⟩ + ω^{ks}|1⟩)/√2
(a "label-k qubit"). For an integer y let cen(y) be the unique representative
of y mod N in the interval (−N/2, N/2]; note |cen(y)| ≤ N/2 ≤ 2^{n−1}.

Fixed parameters (all computed from n by integer arithmetic on O(log n)-bit
numbers):

- m = ceil(2√n) (computed exactly as the least integer m with m² ≥ 4n);
- r = ceil(n/m), the number of sieve stages; 1 ≤ r ≤ √n/2 + 1;
- b_i = max(n − i·m, 0) for i = 0,…,r; so b_0 = n and b_r = 0;
- M = 72·ceil(log₂(48n)) (≥ 72 ln(48n)), the number of qubits per basis in
  phase estimation;
- λ_r = 2^{m+2} + 8M·2^{ceil((r−1)/2)}, and λ_i = 16^{r−i}·λ_r for i < r;
- L₀ = λ_0 = 16^r λ_r, the number of copies used by one sieve run;
- δ = 1/(12 n L₀), the per-copy QFT precision.

**Algorithm OTS.** For j = 0,1,…,n−1:

1. Let t_j = 2^j mod N. Run the target sieve SIEVE(t_j) of §4–§5, which
   acquires exactly L₀ fresh copies. If it reports failure, output 0 and halt.
   Otherwise it returns 2M label-t_j qubits (any further good qubits are
   discarded).
2. Measure M of them in the X basis and M in the Y basis, and compute a
   grid estimate a_j ∈ {0, 1/64, …, 63/64} as in §6.

Finally reconstruct θ̂ from a_0,…,a_{n−1} (§6) and output round(N θ̂) mod N.

The algorithm acquires exactly Q = n·L₀ copies on every branch that does not
halt early, and fewer on branches that halt early. No step is repeated or
restarted, so this is a deterministic cutoff: the only randomness affects
which branch is taken, never the resources (§8).

## 2. Label qubits from coset states (ideal QFT)

In §2–§6 we analyse the **ideal** algorithm, in which the Fourier transform
F_N|y⟩ = N^{−1/2} Σ_k ω^{ky}|k⟩ on the second register (values y < N of an
n-qubit register) is exact. §7 transfers the result to the implemented
Clifford+T circuit.

**Lemma 2.1.** Apply F_N to the second register of a copy of ρ_s and measure
it in the computational basis, obtaining k. Then k is uniform on Z/NZ and the
first qubit is left in |φ_k⟩ (up to a global phase). Different copies give
independent pairs (k, |φ_k⟩).

*Proof.* For a component |ψ_{x,s}⟩,
F_N|ψ_{x,s}⟩ = (2N)^{−1/2} Σ_k ω^{kx}(|0⟩ + ω^{ks}|1⟩)|k⟩. The probability of
outcome k is 1/N for every x, and the post-measurement first qubit is
ω^{kx}|φ_k⟩. Averaging over x (the source mixture) changes only an
unobservable global phase, so the outcome is uniform and the residual qubit is
|φ_k⟩, independently of x. Copies are independent by the source promise. ∎

**Negation.** X|φ_k⟩ = (|1⟩ + ω^{ks}|0⟩)/√2 = ω^{ks}|φ_{−k}⟩. So a Pauli X
(an exact Clifford gate) turns a label-k qubit into a label-(−k) qubit.

## 3. The subtraction combination

**Lemma 3.1.** Given |φ_{k₁}⟩ ⊗ |φ_{k₂}⟩ with known k₁, k₂, apply CNOT with
control qubit 1 and target qubit 2, then measure qubit 2. The outcome is 1 with
probability exactly 1/2, for every k₁, k₂, s; on outcome 1, qubit 1 is left in
|φ_{k₁−k₂}⟩ (up to global phase).

*Proof.* The product is (|00⟩ + ω^{k₁s}|10⟩ + ω^{k₂s}|01⟩ + ω^{(k₁+k₂)s}|11⟩)/2.
After the CNOT it is (|00⟩ + ω^{k₁s}|11⟩ + ω^{k₂s}|01⟩ + ω^{(k₁+k₂)s}|10⟩)/2.
The outcome-1 part is (ω^{k₂s}|0⟩ + ω^{k₁s}|1⟩)⊗|1⟩/2, of squared norm 1/2,
and normalises to ω^{k₂s}|φ_{k₁−k₂}⟩. ∎

On outcome 0 (also probability 1/2) the qubit is discarded ("subtraction
sieve"). Because the outcome probabilities are 1/2 regardless of the labels,
the outcome of each combination is a fair coin independent of all labels,
all other outcomes and all classical choices made before it.
## 4. The offset-tracking target sieve (correctness)

SIEVE(t), for a target t ∈ Z/NZ, manipulates *items*. An item is a qubit in
some state |φ_k⟩ together with two classical integers (u, c) satisfying the
invariant

$$ k \equiv u + c\,t \pmod N. \tag{I} $$

The integer k itself is never needed after an item is created.

**Leaves (stage 0).** For each of L₀ fresh copies: obtain (k, |φ_k⟩) by
Lemma 2.1; draw a fair bit o by measuring H|0⟩; set u = cen(k − o t) and
c = o. Then (I) holds and |u| ≤ N/2 ≤ 2^{n−1} < 2^{b_0}.

**Stage i (i = 0,…,r−1).** Every current item has |u| < 2^{b_i}. Put an item
in bucket β = floor(u / 2^{b_{i+1}}). Since −2^{b_i} < u < 2^{b_i} and
b_i − b_{i+1} ≤ m, β ranges over at most 2^{b_i−b_{i+1}+1} ≤ 2^{m+1} values.
Inside each bucket pair the items in index order (first with second, third
with fourth, …); an unpaired last item of a bucket is discarded. For each pair
(item 1, item 2) apply Lemma 3.1 with item 1 as qubit 1. On outcome 1 create
the new item with (u, c) = (u₁ − u₂, c₁ − c₂); on outcome 0 discard. The new
qubit has label k₁ − k₂ ≡ (u₁−u₂) + (c₁−c₂)t, so (I) is preserved; items in
one bucket satisfy |u₁ − u₂| < 2^{b_{i+1}}, so the new item has |u| < 2^{b_{i+1}}.

**Output.** After stage r every item has |u| < 2^{b_r} = 1, i.e. u = 0, so by
(I) its qubit is exactly |φ_{ct}⟩. Keep items with c = 1; apply X to items
with c = −1 (giving label t by the negation rule of §2); discard the rest.
Call the kept qubits *good*. Each good qubit is exactly |φ_t⟩ in the ideal
algorithm.

Each item at stage r is the root of a complete binary tree of depth r whose
2^r leaves are distinct copies; different items have disjoint leaf sets.
By induction on depth, c = Σ_l ε_l o_l over its leaves, where ε_l = ±1 is
fixed by the tree (item 2 of every pair gets a sign flip), and exactly
2^{r−1} leaves have ε_l = +1 and 2^{r−1} have ε_l = −1 (true at depth 1, and a
depth-(d+1) tree is a depth-d tree minus another, which swaps the sign
counts of the second one).

**Lemma 4.1 (posterior independence of offsets).** Let F be the
collection of all leaf values u_l, all measurement outcomes in the sieve,
and hence all pairing decisions. Conditioned on F, the offset bits o_l are
independent fair bits.

*Proof.* For one leaf, (k, o) is uniform on Z/NZ × {0,1} (k by Lemma 2.1, o by
construction, independent). The map (k, o) ↦ (cen(k − o t), o) is a bijection
of Z/NZ × {0,1} onto (its image) × {0,1}, so u_l is uniform and independent
of o_l, and leaves are mutually independent. By Lemma 3.1 each combination
outcome is a fair bit conditioned on all labels and all earlier outcomes and
choices; hence the outcome string is independent of all (k_l, o_l). Pairing
decisions are deterministic functions of the current u-values, which are
functions of the leaf u_l and earlier outcomes. Thus F is a function of
((u_l), outcomes), which is independent of (o_l), and (o_l) are i.i.d. fair. ∎

**Lemma 4.2.** Conditioned on F, the final items are good independently, each
with the same probability p_r ≥ p* := 2^{−(r−1)/2}/2.

*Proof.* Independence follows from Lemma 4.1 and disjointness of leaf sets.
Let K = 2^{r−1}. For one item, c = X − Y where X, Y are independent
Binomial(K, 1/2) (sums of o_l over the + and − leaves). Then K − Y is again
Binomial(K, 1/2), so c = 1 iff X + (K − Y) = K + 1, an event of probability
P(Bin(2K, 1/2) = K+1) = binom(2K, K+1)/4^K. By symmetry c = −1 has the same
probability. Using binom(2K, K) ≥ 4^K/(2√K) (valid for all K ≥ 1) and
binom(2K, K+1) = binom(2K, K)·K/(K+1) ≥ binom(2K, K)/2, we get
p_r = 2·binom(2K, K+1)/4^K ≥ 1/(2√K) = p*. ∎
## 5. Sieve counting and the worst-case cutoff

Let L_i be the number of items entering stage i (L_0 = L₀ = λ_0) and B ≤ 2^{m+1}
the number of buckets. **Cutoff rule:** if L_i < λ_i for some i ≤ r, or the
number G of good qubits is < 2M, SIEVE reports failure (and OTS halts with
output 0). No copy is ever re-acquired; a run uses exactly L₀ copies.

**Lemma 5.1.** If L_i ≥ λ_i, then the number P_i of pairs formed in stage i
satisfies P_i ≥ L_i/4, and P(L_{i+1} < λ_{i+1}) ≤ exp(−λ_r/32) conditioned on
everything before stage i.

*Proof.* P_i = Σ_β floor(|bucket β|/2) ≥ Σ_β (|bucket β| − 1)/2 ≥ (L_i − B)/2,
and λ_i ≥ λ_r ≥ 2^{m+2} ≥ 2B, so B ≤ L_i/2 and P_i ≥ L_i/4. This pigeonhole
bound holds for **every** configuration of u-values; no distribution of the
intermediate labels is used. By Lemma 3.1, L_{i+1} is Binomial(P_i, 1/2)
given the past. Hoeffding's inequality gives
P(L_{i+1} < P_i/4) ≤ exp(−2P_i(1/4)²) = exp(−P_i/8) ≤ exp(−λ_i/32). Since
P_i/4 ≥ L_i/16 ≥ λ_i/16 = λ_{i+1}, the event L_{i+1} < λ_{i+1} is contained in it,
and λ_i ≥ λ_r. ∎

**Lemma 5.2.** If L_r ≥ λ_r then P(G < 2M) ≤ exp(−M/2) conditioned on F.

*Proof.* By Lemma 4.2, G ~ Binomial(L_r, p_r) with p_r ≥ p* given F. Since
λ_r ≥ 8M·2^{(r−1)/2} = 4M/p*, the mean μ = L_r p_r ≥ λ_r p* ≥ 4M, so 2M ≤ μ/2.
The multiplicative Chernoff bound P(G ≤ μ/2) ≤ exp(−μ/8) gives the claim. ∎

**Corollary 5.3.** One run of SIEVE(t) fails with probability at most
r·exp(−λ_r/32) + exp(−M/2) ≤ (r+1)·exp(−M/4), because λ_r ≥ 8M. On success it
returns 2M qubits, each exactly |φ_t⟩, in a product state (the qubits are
disjoint subsystems that never interacted after their last combination, and
each is in a pure state), independent of the bits used to pick them.

Since M ≥ 72 ln(48n), exp(−M/4) ≤ (48n)^{−18}. Over the n runs of OTS the
total sieve failure probability is at most n(r+1)(48n)^{−18} ≤ 1/12 (using
r + 1 ≤ n + 1 and n ≥ 1).

**Explicit size.** r ≤ √n/2 + 1 and m + 2 ≤ 2√n + 3 give
16^r ≤ 16·2^{2√n} and λ_r ≤ 2^{2√n+3} + 16M·2^{√n/4}. As M = O(log n),
λ_r ≤ C₁ 2^{2√n} for an absolute C₁, hence

$$ L_0 = 16^r\lambda_r \le 16C_1\,2^{4\sqrt n},\qquad Q = nL_0 \le 16C_1\,n\,2^{4\sqrt n}. $$
## 6. Phase estimation from labels 2^j mod N

Let θ = s/N ∈ [0,1) and, for a real x, let ‖x‖ be the distance from x to the
nearest integer (circular distance in turns). A label-t_j qubit with
t_j = 2^j mod N is |φ_{t_j}⟩ = (|0⟩ + e^{2πiα_j}|1⟩)/√2 with
α_j = 2^jθ mod 1, because t_j s/N ≡ 2^j s/N (mod 1).

**Estimating one phase.** Measure M copies in the X basis (H, then measure),
and M copies in the Y basis (S†, H, then measure); both are exact Clifford
operations. For a phase α, P(outcome 0) is (1 + cos 2πα)/2 and (1 + sin 2πα)/2
respectively. Let p̂_X, p̂_Y be the empirical frequencies, ĉ = 2p̂_X − 1,
ŝ = 2p̂_Y − 1, v̂ = (ĉ, ŝ), v = (cos 2πα, sin 2πα). By Hoeffding,
P(|p̂ − p| > 1/12) ≤ 2exp(−2M/144) = 2exp(−M/72) for each basis. On the
complement, |ĉ − cos 2πα|, |ŝ − sin 2πα| ≤ 1/6 and |v̂ − v| ≤ √2/6 < 0.236.
For a unit vector v and |v̂ − v| ≤ d < 1, the angle between v and v̂ is at most
arcsin d; so the angle of v̂ is within arcsin(0.236)/(2π) < 0.038 turns of α.

The estimate a_j is a grid point g/64 (g = 0,…,63) maximising
ĉ·cos(2πg/64) + ŝ·sin(2πg/64), where the 128 constants are fixed 20-bit
fixed-point approximations (absolute constants, computed once by the uniform
controller in O(1) work) and ĉ, ŝ are exact rationals with denominator M.
Every dot product is computed within 2^{−17} of its exact value, and
|v̂| ≥ 0.76. The exact maximiser is within 1/128 turn of the angle of v̂; the
computed maximiser has |v̂|cos(Δ) within 2^{−16} of the exact maximum, so its
angular distance Δ exceeds the exact maximiser's by less than 0.002 turns.
Hence ‖a_j − α_j‖ < 0.038 + 1/128 + 0.002 < 1/16.

Over all j there are 2n Hoeffding events, so all estimates satisfy
‖a_j − α_j‖ < 1/16 except with probability ≤ 4n·exp(−M/72) ≤ 4n/(48n) = 1/12.

**Reconstruction (Kitaev).** Set β_{n−1} = a_{n−1}. For j = n−2 down to 0, of
the two candidates β_{j+1}/2 and β_{j+1}/2 + 1/2 (mod 1) let β_j be the one
nearer to a_j (ties: the first). All β_j are dyadic rationals with at most
n + 6 bits, so this is O(n) bit operations per step.

**Lemma 6.1.** If ‖a_j − α_j‖ < 1/16 for all j, then ‖β_j − α_j‖ ≤ 2^{−(n−1−j)}/16 for every j, and output
round(Nβ_0) mod N equals s.

*Proof.* Downward induction; true for j = n−1. Suppose ‖β_{j+1} − α_{j+1}‖ = ε ≤ 1/16.
Since 2α_j ≡ α_{j+1}, one candidate γ satisfies ‖γ − α_j‖ ≤ ε/2 and the other
is at circular distance ≥ 1/2 − ε/2 from α_j. Then ‖γ − a_j‖ < 1/16 + ε/2 ≤ 3/32,
while the other candidate is at distance > 1/2 − ε/2 − 1/16 ≥ 13/32 from a_j;
so β_j = γ and ‖β_j − α_j‖ ≤ ε/2. Thus ‖β_0 − θ‖ ≤ 2^{−(n−1)}/16 = 2^{−n−3},
and ‖Nβ_0 − s‖ ≤ N 2^{−n−3} ≤ 1/8 (as N ≤ 2^n). Hence round(Nβ_0) ≡ s mod N
(the rounding of a dyadic rational with n+6 bits, times the n-bit N, is exact
integer arithmetic). ∎
## 7. Approximate QFT precision and the total failure bound

Every quantum operation of OTS other than F_N is an exact Clifford+T circuit:
CNOT, X, H, S†, measurement, fresh |0⟩, and (in §8) classically addressed
versions of these. Only F_N needs approximation.

**Cited Theorem 7.1 (approximate QFT over an arbitrary cyclic group).**
A. Yu. Kitaev, "Quantum measurements and the Abelian Stabilizer Problem",
arXiv quant-ph/9511026v1 (20 Nov 1995): Theorem 1 (Sec. 3; the eigenvalue of a
permutation on n bits is measured exactly with error probability ≤ ε by an
operation sequence of length poly(n) + O(n) log(1/ε)), Theorem 2 (Sec. 5; that
measurement is performed reversibly, representing the target operator with
precision 2(|Ω|ε)^{1/2}), and the construction of the QFT V_q over Z_q for
arbitrary q ≤ 2^n at the end of Sec. 5, Eqs. (22)–(25) together with the
recursive preparation of |ψ_{q,0}⟩. Applying Theorem 2 with |Ω| ≤ 2^n and
error probability ε₁ = ε²/2^{n+4} gives the precision stated below at cost
polynomial in n + log(1/ε). For every N ≥ 2 (n bits) and every
ε ∈ (0,1) there is a circuit of at most poly(n, log(1/ε)) gates, each a CNOT,
Hadamard or single-qubit phase rotation whose angle is specified by
O(n + log(1/ε)) bits, on poly(n, log(1/ε)) qubits, which maps |y⟩|0…0⟩ to
within ε (Euclidean norm) of (F_N|y⟩)|0…0⟩ for every y < N, and which is
produced by a uniform classical algorithm in poly(n, log(1/ε)) bit operations.
The polynomial has absolute degree; we do not need its value.

**Cited Theorem 7.2 (Solovay–Kitaev).** C. M. Dawson and M. A. Nielsen, "The
Solovay–Kitaev algorithm", Quantum Inf. Comput. 6(1):81–95, 2006 (arXiv
quant-ph/0505030v2), Theorem 1 (Solovay–Kitaev), Sec. 2, with the exponents
ln5/ln(3/2) ≈ 3.97 and ln3/ln(3/2) ≈ 2.71 derived in Sec. 3: any single-qubit unitary is approximated to
operator-norm error ε' by a sequence of O(log^{3.97}(1/ε')) gates from {H, T, T†}
(a fixed finite generating set of a dense subgroup of SU(2)), found classically
in O(log^{2.71}(1/ε')) operations on numbers of O(log(1/ε')) bits after an O(1)
precomputation of a fixed ε₀-net. All of these are poly(log(1/ε')) bit operations.

Combining them with ε = δ/2 and ε' = δ/(2G) (G the gate count of Theorem 7.1)
gives a Clifford+T circuit V_{N,δ} with

$$ \text{gates, ancillas, generation work} \;\le\; C_F\,(n+\log(1/\delta))^{d_F} $$

for absolute constants C_F, d_F, satisfying ‖V_{N,δ}(|y⟩|0⟩) − (F_N|y⟩)|0⟩‖ ≤ δ
for every y < N (errors of sequential gates add by the triangle inequality).
The ancillas are measured and discarded together with the copy's register.

**Transfer to the implemented algorithm.** The implemented OTS is the ideal
OTS with each of its at most Q = nL₀ applications of F_N replaced by V_{N,δ}.
Each replacement moves the state by at most δ in trace distance. Each pure
component (|0⟩|x⟩ + |1⟩|x+s⟩)/√2 of a source copy has orthogonal first-qubit
branches, each supported on y < N, so replacing F_N by V_{N,δ} on the second
register moves that component by at most δ in Euclidean norm (the two error
vectors lie in orthogonal subspaces: ‖(e₀ + e₁)/√2‖ ≤ max(‖e₀‖, ‖e₁‖) ≤ δ),
hence by at most δ in trace distance; by convexity the same holds for the
copy's mixed state ρ_s. F_N is applied while the copy is in tensor product
with everything else, so the global state moves by at most δ. By the hybrid
argument (trace distance is contractive under all later operations,
measurements and classical control included), the distributions of the final
output differ in total variation by at most Q·δ = nL₀/(12nL₀) = 1/12.

With L₀ ≤ 16C₁2^{4√n}, log(1/δ) = log(12nL₀) ≤ 4√n + O(log n), so each
V_{N,δ} costs O(n^{d_F}) gates, qubits and generation work (absolute constants).

**Theorem 7.3 (correctness).** For every N ≥ 2 and every s, implemented OTS
outputs s with probability at least 1 − 1/12 − 1/12 − 1/12 = 3/4 ≥ 2/3.

*Proof.* In the ideal algorithm, the sieves all succeed except with
probability ≤ 1/12 (§5); on success each run returns 2M exact, independent
copies of |φ_{t_j}⟩, so the phase-estimation events fail with probability ≤ 1/12
(§6), and otherwise Lemma 6.1 outputs s. So the ideal algorithm errs with
probability ≤ 1/6; the transfer adds ≤ 1/12. The probability is
unconditional: failed sieves are counted as errors, never postselected. ∎
## 8. Joint resource accounting and growth indices

All counts below hold on every execution branch (early halts only reduce
them). Write A = ceil(log₂(S+2)) for the address cost, where S is the total
number of allocated bits and qubits; by the space bounds below
A ≤ 4√n + O(log n).

**Samples.** Each of the n runs acquires exactly L₀ copies, including copies
whose items are later discarded (unpaired, outcome 0, c ∉ {±1}, surplus good
qubits) and copies of runs that end in failure. Hence

$$ Q(N,s) \le nL_0 \le 16C_1\,n\,2^{4\sqrt n} = O(2^{4\sqrt n}\,n). $$

**Quantum space.** Copies are processed one at a time at the leaves: the
(n+1)-qubit copy plus the O(n^{d_F}) ancillas of V_{N,δ} are used, the second
register and ancillas are measured, and only the label qubit is kept. At most
L₀ item qubits exist at any time (pairing only reduces their number), and
phase estimation uses ≤ 2M of them. So S_Q ≤ L₀ + n + 1 + O(n^{d_F}) = O(2^{4√n}).

**Classical space.** Each item stores its qubit's index (≤ log₂ S + 1 bits),
u (n + 1 bits) and c (r + 2 bits, |c| ≤ 2^r): O(n) bits per item since
log S = O(√n). Bucketing uses a second array of the same size (merge sort by
key), and the leaf generator needs O(n^{d_F}) bits for producing V_{N,δ}
(the circuit is regenerated for each copy, not stored in bulk). Phase
estimation stores 2n counters and n grid values. So
S_C = O(L₀ n) + O(n^{d_F}) = O(2^{4√n} n).

**Time.** Per copy: source cost n + 1; generation and execution of V_{N,δ},
O(n^{d_F}) gates each with a classically chosen wire address, so
O(n^{d_F}·A) work; the fair coin, cen(k − o t) and storing the item, O(nA).
Per stage, sorting L_i items by their (m+2)-bit bucket key costs
O(L_i log L_i) comparisons, each O(n + A) bit operations including addresses;
each pair costs one addressed CNOT, one measurement and an O(n)-bit
subtraction, plus addresses. The output step and phase estimation are
O(L_r(n+A)) and O(nM·A + n²). The parameter computation is O(n) bit operations
on O(log n)-bit numbers. Since r ≤ n stages and Σ_i L_i ≤ 2L₀,

$$ T(N,s) \le C_2\, n L_0\, n^{d_F+2} \le C_3\, 2^{4\sqrt n} n^{d_F+3}
\le C_4\,2^{5\sqrt n}, $$

because n^{d_F+3} ≤ C 2^{√n} for every n ≥ 1 with C depending only on the
absolute constant d_F. This is the declared O(2^{5√n}); we deliberately do
not claim a polynomial factor, since d_F is not determined here.

**Growth indices.** For B_T = 2^{5√n}: log₂ log₂ B_T = log₂ 5 + (1/2) log₂ n,
so g = 1/2. For B_C = B_samples = 2^{4√n} n: log₂ B = 4√n + log₂ n, whose
log₂ divided by log₂ n tends to 1/2. For B_Q = 2^{4√n}, g = 1/2. Fixed
multiplicative constants do not change these limits, and the envelopes
are valid for all n ≥ 1 after enlarging absolute constants. Index vector
[1/2, 1/2, 1/2, 1/2]; only the time index 1/2 is the numeric score.
## 9. The case N = 2^n and relation to the literature

For N = 2^n, Kuperberg's original algorithm sieves on the low bits of the
label (pairs agree on the next block of low bits, so differences lie in a
smaller subgroup 2^{im}Z/2^nZ and stay uniform there), reaches label 2^{n−1},
whose qubit (|0⟩ + (−1)^s|1⟩)/√2 gives s mod 2 by an X measurement, and then
recurses on (s − (s mod 2))/2 in Z/2^{n−1}Z. OTS covers this case without
special treatment: t_j = 2^j for j < n, and t_{n−1} = 2^{n−1} is exactly the
parity-revealing label, with the higher-order labels playing the role of
the recursion through Lemma 6.1. We use the single uniform OTS for every N
so that one analysis covers all N.

For general N there is no subgroup chain to sieve along (e.g. N prime), and
the distribution of magnitude-sieved labels is not uniform. Kuperberg (2005)
also states his result for arbitrary N; we do not rely on that part of his
analysis. Our analysis avoids every distributional assumption on intermediate labels:
pairing uses only the pigeonhole bound (Lemma 5.1), and the exact target t is
reached by the offset bits whose posterior law is computed exactly
(Lemmas 4.1–4.2), at the cost of the factor 1/p* ≤ 2^{(r+1)/2} absorbed in λ_r.
Small-label end games are not used: a label k with |k| ≪ N gives fidelity
|cos(πk/N)| between secrets s and s+1, so only the exact labels 2^j mod N,
up to 2^{n−1}, are read out.

## 10. Fractional error tolerance

The analysis above assumes that all acquired copies are independent ideal
coset states (Lemma 2.1 and the independence used in §4–§6). It therefore
establishes the malformed-sample fractional guarantee epsilon(n) = 0, jointly
with all four resource bounds and success ≥ 3/4, for this same algorithm and
configuration. No positive tolerance is claimed; this is not a proof that the
algorithm tolerates no corruption.
