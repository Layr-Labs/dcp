# PS2: a pair-combine divisibility sieve and the free-frequency decoder

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). PS2 is one
fully specified algorithm that recovers the whole s with unconditional
probability at least 2/3, with joint worst-case (every-branch) bounds

  T   = O(2^(4 sqrt(n)) n^10)  total work           growth index 1/2
  S_C = O(2^(4 sqrt(n)) n^4)   peak classical bits  growth index 1/2
  S_Q = O(2^(4 sqrt(n)) n^4)   peak qubits          growth index 1/2
  Q   = O(2^(4 sqrt(n)) n^7)   source copies        growth index 1/2

All four hold for this single algorithm and parameter choice, jointly on
every execution branch, under the clean-input tolerance epsilon(n) = 0
(Section 11). Every loop is fixed-length or acquisition-capped; expected
values appear only in the success budget, never in resource bounds.

**Every gate in PS2 is exact.** The complete gate set is H, S, CNOT,
Toffoli-built reversible classical arithmetic, and computational-basis
measurements (plus the fixed X). There is no gate synthesis, no
approximate rotation, and no asserted-but-unspecified routine anywhere in
the algorithm: label extraction (Section 3) reads the latent label by
majority-voted exact-basis coin tests and confirms it by an exact
character-orthogonality test.

**Provenance and dependency.** PS2 is a deliberate simplification and
independent verification of the frontier result CS1 (AdamGagol,
submission f148181 on this benchmark, whose restored proof was read),
which builds on G. Kuperberg's sieves (SIAM J. Comput. 35(1):170-188,
2005; LIPIcs 22:20-34, 2013, arXiv:1112.3333). Used from CS1 with credit
and declared dependency: the latent-label model and the exact transforms
Mult/Shift (their Section 3); the rational cosine/sine table (their
Section 4); the free-frequency decoder - unit multipliers, dyadic
candidate arcs, near/far decomposition, Azuma concentration (their
Section 9); and the Shift-based 2-adic bit extraction (their Section
10). New here: the sieve and the label law feeding the decoder. CS1
merges phase-vector registers through residue measurements with
renumbering permutations and quantum table lookups; PS2 sieves plain
qubits: each combine is one CNOT, one computational-basis measurement
and at most one X, and all bookkeeping is classical integer label
arithmetic. Label extraction is a direct exact-gate measurement scheme
(no inverse QFT, no phase-estimation circuit), and the label law the
decoder needs follows from a short acceptance-bias analysis (Section 6)
instead of CS1's top-bit independence lemma. The price is a strictly
worse exponential constant (about 3.6 sqrt(n) in the exponents of the
intermediate bounds, versus CS1's sqrt(2) sqrt(n)) and quantum space
2^(Theta(sqrt n)) versus their O(n): PS2 is dominated by CS1 on the full
bound vector and claims only the simpler, fully elementary proof of the
same frontier index 1/2.

## 1. Model, conventions, parameters, finite branch

The model is `rules.md`: uniform classical controller; Clifford+T gates;
computational-basis measurements; fresh |0> qubits; a source of fresh
independent copies of rho_s, each acquisition costing n+1 work; classically
addressed gates and indexed accesses additionally cost ceil(log2(M+2)) at
current allocation M; no QRAM; no instance-dependent advice.
omega = e^(2 pi i). Work is accounted as core steps times the current
addressing surcharge, plus n+1 per acquisition. The peak allocation is at
most M_max = 2^((5/sqrt(2)) sqrt(n) + 20) (Section 10), so every surcharge
is at most (5/sqrt(2)) sqrt(n) + 21. (M_max dominates the peak quantum
allocation log2 S_Q <= (5/sqrt 2) sqrt(n) + 13 of Section 10.)

Write N = 2^(a2) M with M odd, d0 = floor(log2 N) (2^d0 <= N < 2^(d0+1),
d0 >= 1). Fixed parameters, computed exactly from N:

* b = ceil(sqrt(2(d0 - 1)))   (sieve residue width; b >= 11 for n >= 64);
* for a sieve of depth B (each use fixes B, always B <= d0 - 1):
  q(B) = ceil(B/b) levels with widths b_j = min(b, B - jb) in [1, b] and
  collimated prefixes p_j = jb (j < q; p_j < B), p_q = B;
  C0(B) = 2^(3 q(B) + b + 8)  (qubits per run);
* Wmax = 2^(q(d0 - 1) + 3);   P_j = j + ceil(log2 Wmax) + 9;
* K = 2^13 (ceil(log2 C0(d0-1)) + ceil(log2 n) + 51)   (roots per stage);
* runs = ceil(K / 2^(b+1))   (runs pooled per odd-part stage);
* J = min{ j >= 0 : 2^(j+3) > 2M }   (odd-part stages; J + 1 <= n);
* label-extraction parameters (Section 3), for a call of arc depth L
  (L = B + 1 for odd-part leaves, L = n for 2-adic leaves):
  Tex = 16384 (L+1)^2 ceil(log2(32 (L+1)))  (coins per arc level),
  V = 384 n + 1600   (verification rounds), Rtry = 16  (attempts);
* Qcap as fixed in Section 8.

Size facts (n >= 64, B <= d0 - 1 <= n - 2): B/b <= B/sqrt(2B) = sqrt(2B)/2
(since b >= sqrt(2(d0-1)) >= sqrt(2B)), so

  q(B) <= sqrt(2n)/2 + 1 = sqrt(n/2) + 1,                               (1.1)
  log2 C0(B) = 3q(B) + b + 8 <= 3(sqrt(n/2) + 1) + sqrt(2n) + 1 + 8,
  i.e.      log2 C0(B) <= (3/sqrt(2) + sqrt(2)) sqrt(n) + 12
                      = (5/sqrt(2)) sqrt(n) + 12,                        (1.2)
  log2 Wmax = q(d0-1) + 3 <= sqrt(n/2) + 4.                             (1.3)

Lower bound (used by Sections 6 and 7): B = d0 - 1 >= n - 2 and
b <= sqrt(2(d0-1)) + 1 <= sqrt(2n) + 1, so

  q(d0-1) = ceil(B/b) >= B/b >= (n-2)/(sqrt(2n)+1) > 5   (n >= 64),    (1.4)

since n - 2 > 5(sqrt(2n)+1) at n = 64 (62 > 61.6) and increasingly for
larger n; being an integer, q(d0-1) >= 6, i.e. every odd-part root has
2^q >= 64 leaves.

runs: K/2^(b+1) = 2^13(X + Y + 51)/2^(b+1) with
X = ceil(log2 C0(d0-1)) = 3 q(d0-1) + b + 8 exactly (C0 is a power of 2)
and Y = ceil(log2 n). For 64 <= n <= 74 (b = 12, q(d0-1) = 6): X = 38
and Y <= 7, so runs <= 38 + 7 + 51 = 96 (here 2^(b+1) = 2^13). For
n >= 75 (b >= 13): n <= d0 + 1 <= b^2/2 + 2 <= (0.72 b)^2, so
X + Y + 51 <= (5/sqrt 2)(0.72 b) + 2 log2 b + 65 <= 2.55 b + 2 log2 b + 65,
and 2^(13-b-1)(2.55 b + 2 log2 b + 65) + 1 is decreasing in b >= 13
(each unit of b halves the leading factor while the bracket grows by less
than 3%), with value (2.55·13 + 2·3.7 + 65)/2 + 1 < 54 at b = 13. Hence
runs <= 96 for all n >= 64.

### 1.1 Finite branch (n < 64)

For cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand
(Section 2), measure the control in the X basis, and reject cand at the
first minus outcome; output the first candidate with no rejection, else 0.
For cand = s the shifted copy is a product of |+> with a data state and
every outcome is plus; for cand != s the two data branches are orthogonal,
the control is I/2, and outcomes are uniform. So Pr[wrong] <=
N 2^-(n+10) <= 2^-10. This branch uses Q <= N(n+10) copies and polynomial
work and space; all its ratios to the declared envelopes over 2 <= n < 64
are bounded by absolute constants absorbed by the O()-constants.
Henceforth n >= 64.

## 2. Source identities, latent labels, exact transforms

This section restates CS1 Section 3 (used with credit); proofs are included
for self-containedness. Let chi_k = N^(-1/2) sum_u omega^(k u)|u> and
phi_k(s) = (|0> + omega^(-k s)|1>)/sqrt 2. From
|u> = N^(-1/2) sum_k omega^(-k u) chi_k,
rho_s = N^(-1/2) sum_x |psi_x><psi_x|,
psi_x = (|0,x> + |1,x+s>)/sqrt 2, the cross terms cancel:

  rho_s = (1/N) sum_(k=0)^(N-1) |phi_k(s)><phi_k(s)| (x) |chi_k><chi_k|.  (2.1)

**Latent-label model.** By (2.1) each copy is a convex mixture, with
uniform weights, of the product states phi_k(s) (x) chi_k. The algorithm is
a linear (adaptive) quantum instrument applied to independent copies, so
the joint law of all its classical outcomes equals the law obtained by
drawing an independent uniform latent label k per copy and running on
phi_k(s) (x) chi_k. All probabilities below use this model. Applying X to
the control maps phi_k(s), up to a global phase, to the POSITIVE qubit
pq_k(s) = (|0> + omega^(k s)|1>)/sqrt 2; PS2 applies this X after every
extraction. A *labelled qubit* is pq_k(s') with a known integer label k,
for the current secret s' (initially s).

**(T1) Mult_alpha.** For alpha coprime to N: the permutation u -> alpha u
mod N on [0,N), identity on [N,2^n), maps the copy exactly to rho_(alpha s)
(both branches are relabelled by the bijection). Implemented with n
controlled modular additions of the constants alpha 2^v mod N into a clean
register, a swap, and uncomputation with alpha^(-1): O(n^2) core steps,
O(n) scratch.

**(T2) Shift_c.** On the |1> branch replace u by u - c mod N (identity
elsewhere): |1,x+s> becomes |1,x+(s-c)>, so the copy becomes exactly
rho_(s-c): O(n) core steps. Modular addition of a known constant is a
ripple comparison with N, an addition, a comparison and a select: O(n)
Boolean gates, computed cleanly (compute, XOR the result out, uncompute).
Both transforms are exact permutations; no synthesis error arises.

## 3. Label extraction LE (exact gates only)

**Primitive: coin test.** tau := the permutation of {0,...,2^n-1} adding 1
mod N on [0,N), fixing [N,2^n). tau chi_k = omega^(-k) chi_k. A *coin test
T(w)* on a copy with latent label k prepares one clean ancilla in |+>
(one H), applies tau^w to the data register controlled on the ancilla
(a Toffoli-built modular addition of the fixed constant w in [0,N): O(n)
gates), and measures the ancilla in the X basis, or in the Y basis (one S
gate, one H, then a computational measurement). Exact matrix computation
on the ancilla state (|0> + omega^(-wk)|1>)/sqrt 2 gives

  E[X-coin outcome] = cos(2 pi w k / N),   E[Y-coin outcome] = sin(2 pi w k / N),

outcome in {+1,-1}; the data register is left in chi_k exactly (it is an
eigenstate of tau^w), so arbitrarily many coin tests can be run on one
copy, and the control qubit phi_k(s') is untouched throughout. All gates
are exact; tau^(2^i) for i <= n-1 adds the constant 2^i < N, an O(n)-gate
network; tau^c for a precomputed c in [0,N) likewise.

**Construction LE(L) (arc decode + verification).** Input: one (possibly
transformed) copy, latent state phi_k(s') (x) chi_k with k uniform on
Z_N; a depth L in {B+1, n}. Put Tex = 16384(L+1)^2 ceil(log2(32(L+1))).

1. *(Arc decode.)* Maintain a dyadic arc [j/2^i, (j+1)/2^i) containing
   x = k/N, starting from [0,1) at i = 0. At level i = 0..L-1 run Tex
   Y-coin tests at w = 2^i and take their majority. Writing u = 2^i x - j
   in [0,1), the mean of each Y-coin is sin(2 pi (j+u)) = sin(2 pi u), so
   the true majority sign identifies the child (u < 1/2 vs u > 1/2); set
   the arc to the majority child. After L levels output the candidate set
   C = {integers in [j N/2^L, (j+1) N/2^L)}; the interval has length
   N/2^L in (1/2, 2), so 1 <= |C| <= 2.
2. *(Verification.)* For each khat in C, run V = 384n+1600 rounds; round r
   uses a fresh uniform c_r in [0,N) (drawn by the controller) and one
   X-coin and one Y-coin at w = c_r. Score

     score(khat) = sum_r [ Z^X_r tab_0({c_r khat/N}) + Z^Y_r tab_1({c_r khat/N}) ],

   with tab_0, tab_1 the rational table of Section 4 ({c khat/N} computed
   as (c_r khat mod N)/N by exact integer arithmetic). If
   max_khat score(khat) >= V/4, output (a) the maximizing khat, (b) the
   control qubit with X applied (the exact state pq_khat(s') if khat = k),
   and release the data register; the attempt *succeeds*. Otherwise the
   attempt *fails*.
3. *(Retry.)* On failure discard the copy and repeat on a fresh copy, at
   most Rtry = 16 attempts per requested leaf; if all fail the leaf is not
   produced (the invoking supplier then restarts, under the global
   acquisition cap of Section 8).

**Lemma 3.1 (LE).** One attempt uses at most (L+1) Tex + 2|C| V <=
2^17 (L+1)^3 (2 + log2(L+1)) coin tests, each costing O(n)
Toffoli/Clifford gates plus one one-qubit measurement: per attempt
<= c_E n^4.5 (1 + log2 n) core steps including internal addressing
surcharges (c_E = 2^29; allocation n + O(1) beyond the copy), and all 16
attempts of one leaf together <= 2^33 n^4.5 (1 + log2 n). If the
attempt succeeds then khat = k with probability >= 1 - 2^(-4n+1) (over
the verification coins), and then the output qubit is EXACTLY pq_k(s').
The
attempt succeeds with probability >= 1 - (1/8 + 1/M + 2^(-4n+2)).

*Proof.* **Correct-arc case.** If all L majorities are correct then
k in C. For fixed khat, over the uniform c_r and the coin outcomes the
score is a sum of V independent bounded terms; by character orthogonality
(E_c[cos(2 pi c k/N) cos(2 pi c k'/N)] = (1/2) 1[k' = +-k mod N],
E_c[sin sin] = (1/2) 1[k' = k], E_c[cos sin] = 0, and the tab error
(4.1) of 1/625 per term),

  E[score(khat)] >= V (1 - 2/625)   if khat = k,
  |E[score(khat)]| <= 2V/625        if khat != k  (including khat = -k).

Each round contributes score in an interval of length 4, so Hoeffding
gives, with V = 384n + 1600 (n >= 64),

  P[ score(k) < V/2 ] <= exp(-2 (V/2 - 2V/625)^2 / (16 V)) <= 2^(-17n),
  P[ score(khat) >= V/4 ] <= exp(-2 (V/4 - 2V/625)^2 / (16 V)) <= 2^(-4n)

for every wrong khat. So: if k in C, a wrong khat in C beats it with
probability <= 2^(-4n), and the true k fails verification with
probability <= 2^(-17n). On success with khat = k the output qubit is
exactly pq_k(s') (the coin tests never touched the control; X is exact):
no approximation enters anywhere.

**Wrong-arc case.** If some majority was wrong the final arc does not
contain x, k is not in C, and every candidate is wrong; the attempt still
"succeeds" only on the event score >= V/4 for a wrong khat, probability
<= 2 |C| 2^(-4n) <= 2^(-4n+1). Together with the correct-arc case this
proves the "khat = k with probability >= 1 - 2^(-4n+1)" claim.

**Failure mass.** Split labels into the mod-M stall class S = {k : M | k}
(mass 1/M; for k in S all deep-level coin means are exactly 0 and the
arc performs an unbiased walk; these attempts are priced at full failure
below, an upper bound - if the walk happens to end on k, verification
still outputs k correctly and nothing downstream degrades). For k not in
S: at level i, given the arc correct so far, u = {2^i k/N} is fixed and
each of the Tex coins is iid with mean sin(2 pi u), so the majority errs
with probability <= exp(-(Tex/2) sin^2(2 pi u)) (Hoeffding). Put
c0 = sqrt(2 ln(17(L+1))/Tex); the choice of Tex gives (using
ln(17(L+1)) <= ln 2 * log2(32(L+1)) <= ln 2 * ceil(log2(32(L+1)))):

  c0 <= sqrt(2 ln 2) / (128 (L+1)) < 0.0093/(L+1),  and
  exp(-(Tex/2) c0^2) <= 1/(17 (L+1)).

For one level, the labels k with |sin(2 pi 2^i k/N)| <= c0 form the
preimage of three arcs of total length 3 c0 N/pi of the circle [0,N)
under k -> 2^i k mod N; for k uniform on a region of size K (K = 2^(B+1)
in [N/2, N) for odd-part leaves, K = N for 2-adic leaves), the preimage
has mass at most (3 c0/pi)(N/g_i + 1)(K g_i/N + 1)/K with
g_i = 2^min(i,a2) (bad residues are multiples of g_i, each hit by at
most K g_i/N + 1 labels), i.e. at most

  (3 c0/pi)(1 + N/(K g_i) + g_i/N + 1/K) <= (3 c0/pi)·5 <= 5 c0

(using N/K <= 2, g_i >= 1, g_i <= N, K >= 1; for K = N the bound is
(3 c0/pi) exactly). Union bound over the L levels:

  P[arc diverges, k not in S] <= sum_i (5 c0 + 1/(17(L+1)))
                               <= 5·0.0093·L/(L+1) + 1/17 < 0.106.

So the attempt fails with probability <= 1/8 + 1/M + 2^(-4n+2)
(stall class + off-stall divergence + verification errors), i.e.
P[attempt succeeds] >= 1 - 1/8 - 1/M - 2^(-4n+2) >= 0.54 (M >= 3).

**Cost.** Coin tests per attempt: (L+1) Tex + 2|C| V = (L+1)·16384
(L+1)^2 ceil(log2(32(L+1))) + 2|C|(384n+1600) <= 2^17 (L+1)^3
(2 + log2(L+1)) (using ceil(log2(32m)) <= 4(2 + log2 m) and |C| <= 2).
Each test is <= 8n + 8 elementary gates (a Toffoli-built modular addition
of the round's fixed constant: <= 4n Toffoli + O(n) CNOT; H, S, H; one
measurement) with addressing surcharge <= (5/sqrt 2) sqrt(n) + 21, hence
<= (8n+8)(3.54 sqrt(n) + 21) <= 2^6 n^1.5 core steps (n >= 2). Per
attempt: <= 2^17 (L+1)^3 (2 + log2(L+1)) · 2^6 n^1.5 <= 2^23 (n+1)^4.5
(2 + log2(n+1)) <= 2^24 n^4.5 (1 + log2 n) (n >= 2: n+1 <= 1.5n,
2 + log2(n+1) <= 3 + log2 n <= 1.5(1 + log2 n)). The per-round classical
work (c_r khat mod N and one tab lookup, with surcharges) is at most
2^21 n^2 bit steps per round, hence <= 2^21 n^5 (2 + log2 n) per attempt,
which is at most 2^29 n^4.5 (1 + log2 n) for all n <= 2^26 (using
n^0.5 <= 2^13 there) and is dominated by the quantum count for larger n.
One attempt therefore costs at most c_E n^4.5 (1 + log2 n) core steps
with c_E = 2^29; 16 attempts <= 2^33 n^4.5 (1 + log2 n). QED.

**Leaves.** A *leaf* for a sieve of depth B is a successful LE(B+1) output
on a transformed copy. For the odd part the leaf is then *accepted* iff
khat < 2^(B+1) (both children of every low pattern lie in [0,2^(B+1)), so
the filter does not favour a top bit); for the 2-adic part the leaf label
is kk = khat mod 2^wd. Conditional on acceptance the odd-part label lies
in [0,2^(B+1)); its law is close to uniform - but NOT exactly uniform,
because the attempt-failure probability depends on k (near-boundary and
stall labels fail more often). Section 6 quantifies exactly how far from
uniform, and shows the decoder tolerates it. Expected acquisitions per
accepted odd-part leaf: <= 2/0.54 < 3.8 <= 4 (filter probability
>= 1/2, attempt success >= 0.54); per 2-adic leaf <= 1/0.54 <= 2.

## 4. Rational trigonometric table

CS1 Section 4, reproduced with credit. For v in [0,4096) compute rationals
Cos[v], Sin[v] within 2^-20 of cos(2 pi v/4096), sin(2 pi v/4096): bound pi
within 2^-90 via Machin's formula with 40 alternating arctangent terms per
series (tails < 2^-91), then sum 80 Taylor terms at angles < 7 (remainder
<= 7^81/81! < 2^-170). A fixed finite computation, charged once as an
absolute constant. For x in [0,1): tab_0(x) = Cos[floor(4096 x)],
tab_1(x) = Sin[floor(4096 x)], cs_0 = cos(2 pi .), cs_1 = sin(2 pi .);

  |tab_beta(x) - cs_beta(x)| <= 2 pi/4096 + 2^-20 < 1/625.             (4.1)

## 5. The pair-combine sieve SIEVE(B)

Input: a supplier of leaves for depth B (labels in [0,2^(B+1)) with the
accepted-leaf law of Section 3; the sieve's guarantees do not depend on
the label law beyond independence across leaves). Levels j = 0..q-1
(q = q(B)): a *level-j qubit* has label an INTEGER (possibly negative)
divisible by 2^(p_j), p_j = jb; the final level q-1 has width
b_(q-1) = B - (q-1)b in [1,b] and outputs labels divisible by 2^B.
**No folding.** After LE, level-0 labels are nonnegative; every combine
keeps the SIGNED difference k1 - k2, and no X-conjugation is ever applied
inside the sieve. (Folding |k1 - k2| would make the folded label's low
bits depend on the top bits and would break the dephasing lemma;
signed arithmetic avoids exactly this.)

**Level step.** Given a list of C level-j qubits (j <= q-1):
1. Partition into residue classes of u = label / 2^(p_j) (exact signed
   division; labels are divisible by 2^(p_j)) modulo 2^(b_j),
   b_j = p_(j+1) - p_j: the class of a label is u mod 2^(b_j) in
   [0, 2^(b_j)). Pair within each class in arrival order. At most one
   qubit per class is unpaired, so at least (C - 2^(b_j))/2 pairs are
   formed, and (C - 2^(b_j))/2 >= (15/32) C whenever C >= 2^(b+4).
2. For each pair (q1,k1),(q2,k2): apply CNOT(q1 -> q2), measure q2.
   Outcome 0 (probability exactly 1/2): discard both. Outcome 1: q1 carries
   the SIGNED label k1 - k2 (Lemma 5.1); keep it. Two labels in one class
   have u1 = u2 mod 2^(b_j), so k1 - k2 = 2^(p_j)(u1 - u2) with
   u1 - u2 divisible by 2^(b_j): output labels are divisible by
   2^(p_(j+1)). (Signed differences of same-class labels: class membership
   is u mod 2^(b_j), which is well defined for negative u, and equal
   classes give u1 - u2 = 0 mod 2^(b_j) regardless of sign.)

**Lemma 5.1 (combine algebra).** For ideal (q1,k1),(q2,k2): after
CNOT(q1 -> q2) and measuring q2, outcome 0 (probability exactly 1/2) leaves
q1 with label k1 + k2, and outcome 1 (probability exactly 1/2) leaves q1
with label k1 - k2 (signed, no conjugation), in both cases up to a global
phase; the probabilities are exactly 1/2 regardless of s', k1, k2.

*Proof.* (|0> + w1|1>)(|0> + w2|1>)/2 with w_i = omega^(k_i s') maps under
CNOT to (1/2)(|00> + w2|01> + w1|11> + w1w2|10>); the q2 = 0 branch of q1
is (|0> + w1w2|1>)/sqrt 2 (label k1 + k2), the q2 = 1 branch is
w2(|0> + (w1/w2)|1>)/sqrt 2 (label k1 - k2); the two branches have
probability exactly 1/2 each. QED.

**Label invariant.** A level-j label is a signed sum of at most 2^j leaf
labels, each in [0, 2^(B+1)) with 2^(B+1) <= 2^n; hence |label| <
2^(n+1+j) and label is divisible by 2^(p_j). A final label has
|label| < 2^(n+1+q) and is divisible by 2^B.

**Lemma 5.2 (survival).** Run SIEVE(B) from C0 = 2^(3q + b + 8) level-0
qubits. With probability >= 1 - 2^(-400) the final list has at least
2^(b+5) qubits. (This lemma uses only the exact 1/2 keep coins of Lemma
5.1 and counting; it holds for every leaf law, in particular the biased
accepted-leaf law of Section 6.)

*Proof.* Induction claim: for j = 0..q, with probability >= 1 - j·D the
level-j list has >= 2^(3(q-j)+b+5) qubits, where
D := exp(-2^(b+2)) <= 2^(-2^(b-1)) <= 2^(-1024) (b >= 11). The case j = 0
holds since C0 = 2^(3q+b+8) >= 2^(3q+b+5). Suppose the level-j list has
count_j >= 2^(3(q-j)+b+5) qubits (j <= q-1). Since 3(q-j)+b+5 >= b+5 >=
b_j + 4, pairs number m_j >= (15/32) count_j. The output count is
Bin(m_j, 1/2) (disjoint pairs, exact fair coins by Lemma 5.1) with mean
m_j/2 >= (15/64) count_j >= (15/8)·2^(3(q-j-1)+b+5), i.e. at least 15/8
times the target for level j+1. By the multiplicative Chernoff bound,
P[Bin(m_j,1/2) <= (8/15)(m_j/2)] <= exp(-(1-8/15)^2 m_j / 4) =
exp(-49 m_j/450). The smallest level input in the chain is
count_{q-1} >= 2^(b+8), so m_j >= (15/32)2^(b+8) > 2^(b+3.9) for every
level in the chain, giving failure <= exp(-2^(b+2)) =: D per level. A union
over the q <= sqrt(n/2)+1 levels proves the claim at j = q; the final count
is >= 2^(b+5), and q·D <= 2^(b/2)·2^(-2^(b-1)) <= 2^(-400) for b >= 11
(using sqrt(n/2)+1 <= 2^(b/2) for n >= 64, from (1.1) and b ~ sqrt(2n)).
QED.

**Retries.** If a run ends with < 2^(b+1) qubits the invoking stage retries
with fresh copies, at most 3 attempts; each attempt fails with probability
<= 2^(-400), so retries are exhausted with probability <= 2^(-1200) per
stage, whereupon the stage outputs 0 (Section 8).

**Corollary 5.3 (run cost).** One run consumes exactly C0 leaves (an
expected <= 4 acquisitions per leaf, hard-capped globally by Section 8)
and O(C0 (n + b)(q+1)) core steps: per level, a radix partition into
2^(b_j) classes costs O(C0 (n + b_j)), pairing and signed label arithmetic
O(n) per pair, and the quantum work is one CNOT and one measurement per
pair. All loops are fixed-length.

## 6. The accepted-leaf law and root dephasing

Fix one run of depth B <= d0 - 1 and its stage transform (Mult_alpha for
the odd part, Shift for the 2-adic part). For each consumed odd-part leaf
write the label k = low + 2^B tau with 0 <= low < 2^B and tau in {0,1}
(for a 2-adic leaf of width wd, k = low + 2^(wd-1) tau mod 2^wd; the
same analysis applies verbatim with B replaced by wd-1 and the two
children taken inside Z_N - see the end of the section). Let G be the
sigma-field generated by: all low parts of the run's consumed leaves;
all level measurement outcomes (the keep coins); and the controller's
decisions (arrival-order pairing, class partitions, retry and pooling
decisions, which select by index).

For a fixed latent label k let p_k := P[an LE attempt on a copy with
latent label k fails to output k] (the complement of "succeeds with
khat = k"; by Lemma 3.1, p_k <= P[arc diverges | k] + 2^(-16n)). Call a
leaf *good* if p_(k_0) + p_(k_1) <= 1/8, where k_0 = low,
k_1 = low + 2^B tau are its two children in [0,2^(B+1)).

**Lemma 6.1 (failure mass).** For k uniform on [0,2^(B+1)) (odd part) or
on Z_N (2-adic part), P[p_k > 1/16] <= 1/M + 1/15. Hence a leaf is not
good with probability <= 2/15 + 2/M <= 0.8 =: P_b (M >= 3), and the
unconditional attempt-failure mass E_k[p_k] <= 1/8 + 1/M + 2^(-4n).

*Proof.* p_k > 1/16 forces sum_i exp(-(Tex/2) sin^2(2 pi u_i(k))) >
1/16 - 2^(-17n) - 2^(-4n+1), so some level i has
|sin(2 pi u_i(k))| <= c0 with c0 = sqrt(2 ln(17(L+1))/Tex) < 0.0093/(L+1)
(Lemma 3.1's computation). For one level, the labels k of the odd-part
region [0,K), K = 2^(B+1) in [N/2, N), with 2^i k mod N in the three bad
arcs (total length 3 c0 N/pi of the circle) number at most
(3 c0/pi)(N/g_i + 1)(K g_i/N + 1), where g_i = 2^min(i,a2): the bad
residues are multiples of g_i, and each residue is hit by at most
K g_i/N + 1 of the K labels. Dividing by K and expanding,

  (3 c0/pi)(1 + N/(K g_i) + g_i/N + 1/K) <= (3 c0/pi)(1 + 2 + 1 + 1)
                                          <= 5 c0,

using N/K <= 2, g_i >= 1, g_i <= N, K >= 1. In the 2-adic region
(k uniform on Z_N, K = N) the same count is (3 c0/pi) per level exactly.
Summing over the L levels: bad mass <= 5 L c0 < 0.047 <= 1/15 in the
odd-part region, and <= 3 L c0/pi <= 0.009 in Z_N. Additionally the
mod-M stall class {k : M | k} has p_k arbitrarily close to 1 (deep-level
means all 0) and mass exactly 1/M. So P[p_k > 1/16] <= 1/15 + 1/M in
both regions. Not-good leaves: P[p_(k_0) + p_(k_1) > 1/8] <=
P[p_(k_0) > 1/16] + P[p_(k_1) > 1/16] <= 2(1/15 + 1/M) <= 2/15 + 2/3
= 0.8. E_k[p_k]: the stall class contributes at most 1/M; off the stall
class, p_k <= 1/16 off a set of mass <= 1/15 and p_k <= 1 always, so
E_k[p_k] <= 1/M + 1/15 + 1/16 + 2^(-4n) <= 1/8 + 1/M + 2^(-4n). QED.

**Lemma 6.2 (root dephasing).** Conditional on G and all other
independent randomness, the top bits tau of the leaves consumed by any
given final qubit are independent, with per-leaf law

  P[tau = 1 | low = g, G] = (1 - p_(g + 2^B)) / (2 - p_(g) - p_(g + 2^B))
                           =: 1/2 + delta(g),
  |delta(g)| <= (p_(g) + p_(g+2^B)) / (2 (2 - p_(g) - p_(g+2^B)))
              <= 1/30   for good leaves (and <= 1/2 always).

Every final label is

  label = 2^B W,   W = cst + sum_(S+) tau - sum_(S-) tau,                (6.1)

where cst = (signed low sum)/2^B is a G-measurable integer (the label is
divisible by 2^B), S+ and S- are disjoint G-measurable sets, and
|S+| + |S-| equals the number of the qubit's leaves, namely 2^q (q >= 1,
so |S+| + |S-| >= 2; for the odd part q >= 6 by (1.4), 2^q >= 64). For
every real
phi,

  |E[ e^(2 pi i phi W) ]| <= m(phi)^(2^q),                               (6.2)
  m(phi) := P_b + (1 - P_b) sqrt( cos^2(pi phi) + 4 (1/30)^2 sin^2(pi phi) )

  so, for |phi| in [1/8, 1/2] (where cos^2(pi phi) <= cos^2(pi/8)):
m(phi) <= 0.8 + 0.2 * 0.9264 <= 0.986 and

  |E[ e^(2 pi i phi W) ]| <= 0.986^(2^q) <= 0.986^64 < 0.41,             (6.3)

  |E[ (-1)^W ]| <= (E_g m0(g))^(2^q),   m0(g) := |1 - 2 P[tau = 1 | g]|,

with m0(g) <= min(1, s_g), s_g := (failure mass of g's two children);
and E over consumed lows of s_g <= E over uniform lows of s_g
= 2 E_k[p_k] <= 2(1/8 + 1/M + 2^(-4n)) <= 0.92 (Lemma 6.1; the second
step is Jensen's inequality for the concave s(2-s) applied to the
consumption weight, see proof). Hence for 2^q >= 2:

  Pr[ W odd ] >= (1 - 0.92^2)/2 > 0.076 >= 1/16.                         (6.4)

*Proof.* (a) *What a level reads.* A level-j combine reads only the
residue class of u = label/2^(p_j) mod 2^(b_j) - i.e. label bits in
[p_j, p_(j+1)) - and p_(j+1) <= B by construction (the widths b_j sum to
exactly B). Because labels are SIGNED sums of leaf labels with no folding
(Section 5), bits below position B of any level-j label depend only on the
low parts of the leaves: for integers, (a + c) mod 2^t = (a mod 2^t +
c mod 2^t) mod 2^t for every sign of a and c - carries and borrows
propagate strictly upward - and each leaf label k = low + 2^B tau
contributes tau only at positions >= B.

(b) *What the coins are.* The keep coin has probability exactly 1/2
regardless of phases and labels (Lemma 5.1), and different pairs act on
disjoint qubits. Arrival-order pairing, class partitions, retry decisions
and pooling are functions of low bits and indices only, by (a).

(c) *Conditional leaf law.* The copies are independent, so the pairs
(low_ell, tau_ell, coins_ell) are independent across leaves ell, and the
attempt/acceptance/retry events and the filter are functions of each
leaf's own data. Conditioning on G (lows, coins, decisions - hence on
which leaves were consumed and with which lows) leaves the tau_ell
conditionally independent with the stated two-children Bernoulli law:
given low = g, the consumed leaf's tau is 1 exactly when the attempt was
made on the child g + 2^B, which happens with probability proportional to
1 - p_(g+2^B) among the two children. (For the 2-adic part the "children"
of a low g are the two label classes {k = g mod 2^wd} and
{k = g + 2^(wd-1) mod 2^wd} of Z_N, and the same formula holds with
p_k replaced by the class average pbar; note that class averages need
NOT be close to the global average - the near-boundary and stall labels
can concentrate in the class {k = 0 mod 2^wd} - which is exactly why the
2-adic part uses only the parity bound (6.4), which is proved below from
the averaged bound alone and holds under arbitrary concentration.)

*Conclusion.* Every kept combine replaces two labels over disjoint leaf
sets by their signed difference, so by induction a final label is
sum_ell eps_ell k_ell over its exactly 2^q leaves with every eps_ell in
{+1,-1} (a leaf's coefficient is the product of the +-1's along its path,
never 0: the two inputs' leaf sets are disjoint). Substituting
k_ell = low_ell + 2^B tau_ell gives (6.1) with S+ = {eps = +1},
S- = {eps = -1}, and cst = (sum eps low)/2^B, an integer because the
final label is divisible by 2^B; both the eps signs and the low parts are
G-measurable. Then, conditioning on G and evaluating the per-leaf
Bernoulli characteristic functions |E e^(2 pi i phi eps tau)| =
sqrt(cos^2 (pi phi) + 4 delta(g)^2 sin^2 (pi phi)) and averaging over the
lows (independent across leaves),

  |E[e^(2 pi i phi W)]| <= E_G[ prod_ell sqrt(cos^2(pi phi) + 4 delta(g_ell)^2 sin^2(pi phi)) ]
                         = ( E_g sqrt(cos^2(pi phi) + 4 delta(g)^2 sin^2(pi phi)) )^(2^q)
                         <= m(phi)^(2^q),

the last step splitting good leaves (delta <= 1/30, contributing
<= sqrt(cos^2 + 4 sin^2/900)) from not-good leaves (contributing <= 1),
by Lemma 6.1's P_b. For (6.4): at phi = 1/2 the per-leaf factor is
|E e^(i pi eps tau)| = |1 - 2 P[tau = 1 | g]| =: m0(g), and from the
conditional law

  m0(g) = |p_(g) - p_(g+2^B)| / (2 - s_g)  <=  min(1, s_g),
  s_g := p_(g) + p_(g + 2^B),

(because s/(2-s) <= s whenever s <= 1, and m0 <= 1 always; for the
2-adic part the same holds with s_g the sum of the two class averages).
The consumed lows are distributed as w_g (2 - s_g)/Z with w_g = 2^-B
uniform and Z = E_w[2 - s] >= 2 - 0.92 > 1.08, so by concavity of
s(2-s) on [0,2] (Jensen's inequality),

  E_consumed[s_g] = E_w[s(2-s)] / E_w[2-s]
                  <= E_w[s]·(2 - E_w[s]) / (2 - E_w[s])
                  =  E_w[s] <= 2 E_k[p_k] <= 2(1/8 + 1/M + 2^(-4n)) <= 0.92.

Since min(1, s) <= s, also E_consumed[m0] <= E_consumed[s_g] <= 0.92,
and the same product argument as above gives
|E[(-1)^W]| <= (E_consumed[m0])^(2^q) <= 0.92^(2^q), proving (6.4).
QED.

**Roots.** A *root* of a run is a final qubit with its known signed
W = label/2^B. For the odd part (B = d0 - 1 >= n - 2) the label invariant
gives |W| < 2^(n+1+q)/2^B <= 2^(q+3) = Wmax. Roots of one run have
pairwise disjoint leaf sets (the pairing is a matching), so their tau
sets are disjoint and their W's are independent given the run's G; roots
of different runs are independent outright. The decoder pools at most K
roots per stage, chosen by index. Signed W's are harmless downstream:
the odd part uses f_i = 2^j W_i (cos is even, sin odd, so the basis-
averaged expectation (1/2)cos(2 pi f Delta) holds for negative f
verbatim), and the 2-adic part uses only the parity of W.

**Total variation remark.** The accepted-leaf law on [0,2^(B+1)) is
within total variation E_k[p_k]/(2(1-E_k[p_k])) <= 0.23 of uniform; this
is not needed by the sieve or the decoder (both use only Lemma 6.2), but
it confirms that nothing pathological is hidden in the label law.

## 7. Odd part: s1 = s mod M by free-frequency decoding

This section adapts CS1 Section 9 (used with credit); roots replace tree
outputs and Lemma 6.2 replaces their top-bit independence lemma. If M = 1
put s1 = 0 and skip. Otherwise M >= 3, so N >= 3·2^a2 and B := d0 - 1 >=
a2 + 1. Put theta = s1/M in [0,1). Every stage uses depth B (leaves:
labels in [0,2^(B+1)) = [0,2^d0), acceptance probability 2^d0/N >= 1/2;
q = q(B) = q(d0-1) >= 6 by (1.4), so every root has 2^q >= 64 leaves).

**Stage source.** Compute alpha_j (extended Euclid + CRT) with
alpha_j = 1 (mod 2^a2) and alpha_j = 2^j (2^(B - a2))^(-1) (mod M); this is
a unit mod N (a unit mod both prime-power-free factors: 1 mod 2^a2, and
2^(B-a2) is invertible mod the odd M). A leaf: acquire a copy; apply
Mult_(alpha_j); run LE(B+1) (whose output is already the positive qubit
pq_k with label k - no further conjugation is applied anywhere); accept
iff k < 2^(B+1). Accepted labels are iid with the leaf law of Section 6
and the qubit is pq_k(alpha_j s) exactly whenever khat = k (the only
other possibility, probability <= 2^(-4n+1) per attempt, is priced in
Section 9). For every integer W,

  2^B W (alpha_j s / N) = W 2^(B - a2) alpha_j s / M
                        = 2^j W s1 / M   (mod 1),                      (7.1)

because 2^(B - a2) alpha_j = 2^j (mod M) makes the difference
W s (2^(B - a2) alpha_j - 2^j)/M an integer multiple of W s, and
s = s1 (mod M) makes W 2^j (s - s1)/M an integer. So a root of stage j is
(|0> + e^(2 pi i f theta)>|1>)/sqrt 2 with the KNOWN frequency
f = 2^j W. (7.1) is CS1's (9.1) with d0 - 1 in place of their d - 1.

**Stage execution.** Obtain K roots by pooling runs = ceil(K/2^(b+1)) runs
(each run supplies >= 2^(b+1) roots by Lemma 5.2; the pool succeeds with
probability >= 1 - runs·2^(-400)). For i = 1..K: draw a fair bit beta_i;
measure root i in X (beta_i = 0) or Y (beta_i = 1); record Z_i in
{+1,-1} and (f_i, beta_i). E[Z_i | f_i, beta_i] = cs_(beta_i)(f_i theta)
exactly.

**Candidates.** P_j = j + ceil(log2 Wmax) + 9; identify an integer c with
the point zeta = c/2^(P_j) on R/Z. Stage 0 uses every c in [0, 2^(P_0)).
Stage j >= 1 uses every c whose point lies within circular distance
rad_j = 2^-(j+2) of the previous center z_(j-1) (one or two explicit
integer intervals; both z_(j-1), whose denominator is 2^(P_(j-1)) with
P_(j-1) < P_j, and rad_j, since j + 2 <= P_j by (1.3), are multiples of
2^(-P_j), so the arc endpoints are candidates). At most
2^(ceil(log2 Wmax)+10) candidates per stage.

**Score.** For each candidate, using exact integer arithmetic,

  score(c) = sum_i Z_i tab_(beta_i)( ((f_i c) mod 2^(P_j)) / 2^(P_j) ),

by enumerating candidates in increasing order and updating the K residues
f_i c mod 2^(P_j) with one addition each; z_j := the least maximizer's
point.

**Lemma 7.1 (stage; after CS1 Lemma 9.1).** If theta is within rad_j of
z_(j-1) (no condition at j = 0), then in the ideal run, with probability
>= 1 - 2^(-56), theta is within circular distance 2^-(j+3) of z_j.

*Proof.* Let Fs_i be the sigma-field of everything through root i of the
stage. Root i's leaves are disjoint from all earlier roots' leaves and
from all conditioning data, so conditional on Fs_(i-1) the root's W_i
still satisfies Lemma 6.2. For a candidate zeta put
Delta = theta - zeta (circular difference) and
xi_i = Z_i cs_(beta_i)(f_i zeta). Averaging the fair basis bit:

  E[xi_i | Fs_(i-1), W_i] = (1/2) cos(2 pi f_i Delta).

By (4.1) the computed score differs from sum_i xi_i by at most K/625.

*Near point.* Some candidate zeta0 has |Delta0| <= 2^-(P_j+1) (stage 0:
the grid covers the circle at spacing 2^(-P_j); stage j >= 1: theta lies in
the candidate arc). Since |f_i| <= 2^j Wmax,

  |f_i Delta0| <= 2^j Wmax·2^-(j + ceil(log2 Wmax) + 10) <= 2^(-10),

so E[xi_i | Fs_(i-1)] >= (1/2) cos(2 pi 2^(-10)) >= (1/2) cos(pi/128).

*Far points.* Call zeta far if |Delta| >= 2^-(j+3). In stage 0,
|Delta| <= 1/2; in stage j >= 1 both theta and zeta lie within rad_j of
z_(j-1), so |Delta| <= 2^-(j+1). Hence xx := 2^j |Delta| lies in [1/8,
1/2] for every far zeta, so phi := 2^j Delta satisfies |phi| in
[1/8, 1/2], and by (6.3) (f_i = 2^j W_i, and real part at most modulus),

  E[xi_i | Fs_(i-1)] <= (1/2) Re E[e^(2 pi i 2^j Delta W_i) | Fs_(i-1)]
                      <= (1/2) · 0.986^(2^q) <= (1/2) · 0.41 < 0.21.

*Concentration.* For each fixed candidate, sum_i (xi_i - E[xi_i|Fs_(i-1)])
is a martingale whose increments lie in intervals of length 2; by
Azuma-Hoeffding it deviates by at least K/64 with probability at most
exp(-2(K/64)^2/(2·2·K)) = exp(-K/8192). Outside these events for zeta0 and
every far candidate,

  score(zeta0) >= (K/2)cos(2 pi 2^(-10)) - K/64 - K/625
                > (K/2)·0.41 + K/64 + K/625 >= score(far zeta),

because (1/2)(cos(2 pi 2^(-10)) - 0.41) > 0.29 > 2/64 + 2/625 = 0.0345.
So the maximizer is not far. The number of candidate events is at most
2^(ceil(log2 Wmax)+10); with E := ceil(log2 Wmax) + 10 and
X := ceil(log2 C0(d0-1)), we have E <= q + 13 and X >= 3q + b + 8, so
E - X <= 5 - 2q - b <= -2q - 6 (b >= 11). Since
exp(-K/8192) <= 2^(-K/8192) = 2^-(X + ceil(log2 n) + 51) and K/8192 =
(X + ceil(log2 n) + 51) (because K = 2^13(...)), the total failure is at
most 2^(E - X - ceil(log2 n) - 51) <= 2^(-57 - ceil(log2 n)) (using the
weak bound E - X <= -6). So the stage failure is <= 2^(-57)/n. QED.

By induction over j (2^-(j+3) = rad_(j+1); the hypothesis of stage j+1 is
the conclusion of stage j), and a union bound over the <= n stages, the odd
part fails with probability <= 2^(-57). On success theta lies within
2^-(J+3) < 1/(2M) of z_J, and s1 = floor(M z_J + 1/2) mod M equals
s mod M. Stages: J + 1 <= n.

## 8. 2-adic part, assembly, source cap

**2-adic part (after CS1 Section 10).** If a2 = 0 put s2 = 0. Otherwise
s - s1 = M s2 (mod N) for a unique s2 in [0,2^a2). For g = 0..a2-1: let
s2low be the known low g bits, sh_g = s1 + M s2low (mod N), wd = a2 - g,
rem = (s2 - s2low)/2^g in Z/2^wd. A leaf: acquire a copy; apply
Shift_(sh_g), which makes the secret s - sh_g = M 2^g rem; run LE(n)
(label k uniform on Z_N; LE's output is pq_k, and no further conjugation
is applied). With kk = k mod 2^wd (the Section 6 law reduced mod 2^wd,
nearly uniform on [0,2^wd)), the phase is

  e^(2 pi i k M 2^g rem / N) = e^(2 pi i kk rem / 2^wd),

the extra factor being e^(2 pi i h·rem) = 1 for the integer h = k div 2^wd
(because 2^wd 2^g M = N). Use kk as the leaf label (no acceptance
filter; the kk-law is the Z_N-region leaf law of Section 6, reduced
mod 2^wd).

* wd = 1: kk = 1 with probability 1/2: an X measurement gives + iff rem is
  even; kk = 0: discard and repeat.
* wd >= 2: run SIEVE(wd - 1) on kk-leaves (depth B = wd - 1, labels in
  [0,2^wd)); a root has label 2^(wd-1) W and phase
  e^(2 pi i 2^(wd-1) W rem / 2^wd) = e^(pi i W rem). By (6.4) each root's
  W is odd with probability >= 1/16; if W is odd the phase is (-1)^rem and
  an X measurement yields rem mod 2 exactly; if W is even, discard the
  root and take another. A run supplies >= 2^(b+1) roots (Lemma 5.2), so
  no odd W appears with probability <= (15/16)^(2^(b+1)) <= 2^(-0.17·2^b).

Set bit g of s2; in the ideal run with s1 correct, all bits are correct.
Output s = (s1 + M s2) mod N.

**Assembly.** Main branch n >= 64: compute a2, M, d0, b, all q(B), C0(B),
Wmax, all P_j, all alpha_j, all sh_g, and the Section 4 table - polynomial
exact setup, charged once. A binary acquisition counter is maintained at
amortized O(1) flips per acquisition. Expected acquisitions: the odd part
runs <= n stages x runs(<= 96) runs x <= 3 attempts x C0(d0-1) leaves x 4
acquisitions, for <= 1152·n·C0(d0-1); the 2-adic part needs, per bit, an
expected <= 2 trees x 3 attempts x 2 acquisitions x C0(wd-1) plus <= 4
wd = 1 acquisitions, for <= 12n·C0(d0-1) + 4n in total. Define

  Q* := 1200·n·C0(d0-1),   Qcap := 2^10·Q*.

Before an acquisition would exceed Qcap, PS2 stops, releases everything,
and outputs 0. Every branch terminates: all loops are fixed-length or
acquisition-capped.

**The finite branch is exempt from Qcap.** The counter of the previous
paragraph exists only on the main branch (n >= 64). The finite branch
(n < 64) is a separate fixed algorithm whose acquisitions are bounded by
N(n+10) <= 2^63·73 on every branch (each of the N candidates uses at most
n+10 <= 73 tests, each one acquisition). The universal sample bound of
Section 10 is therefore Q(N,s) <= max(Qcap, N(n+10)) for all N >= 2, and
Section 10 verifies that BOTH branches fit the declared envelope
B_samples(n) = 2^(4 sqrt n) n^7 (the main branch for n >= 64, the finite
branch for 2 <= n <= 63, where N(n+10) <= 2^n(n+10) <= 2^(4 sqrt n) n^7:
the log2 ratio difference g(n) := n + log2(n+10) - 4 sqrt n - 7 log2 n
satisfies g(63) = 63 + 6.2 - 31.75 - 41.8 = -4.4 and g(2) = 2 + 3.6 -
5.7 - 7 = -7.1, and its dominant part n - 7 log2 n is decreasing on
[2,10] and increasing on [10,63], so g is maximized at an endpoint of
[2,63] and is <= -4.4 < 0 throughout). Similarly the finite branch's work
fits B_T: at n = 63 its core work is at most N·73·16·n^2·8 (addressing at
allocation O(n)) whose log2 is <= 63 + 6.2 + 4 + 12 + 3 = 88.2 < 91.5 =
4 sqrt(63) + 10 log2(63), and smaller n only gain slack. Its space is
O(n^2) throughout.

## 9. Success probability

Ideal uncapped run: the odd part fails with probability <= 2^(-57)
(Lemma 7.1 union); given correct s1, the 2-adic part fails only if some
bit's run yields no odd-W root, probability <=
a2·2^(-0.17·2^b) <= n·2^(-0.17·2^(b)) <= 2^(-n) for n >= 64: indeed
b = ceil(sqrt(2(d0-1))) >= sqrt(2n) - 1 >= 10.3, so
0.17·2^b >= n + 1 + log2 n + 1 (at n = 64 the left side is
0.17·2^10.3 > 215 while the right side is 72; the left side grows
exponentially in sqrt n, the right polynomially). The wd = 1 repeats
succeed a.s. and are hard-capped by Qcap. Sieve retry exhaustion
over all stages: <= 2n·2^(-1200) <= 2^(-n) for n >= 64 (1200 - log2(2n)
>= n). By Markov and Section 8, the ideal run reaches Qcap with
probability <= 1/1024; capping changes the run only on that event. The
actual run differs from the ideal one only through unclean LE calls
(verification accepted a wrong label); by Lemma 3.1 and a union bound
over <= Qcap attempts, P[some unclean call] <= Qcap·2^(-4n+1). By (1.2)
and Section 8 (Qcap = 2^10·1200·n·C0, log2(1200·2^10) <= 21),
log2 Qcap <= 3.54 sqrt(n) + 33 + log2 n, and
4n - 1 - log2 Qcap >= 255 - 68 > 180 at n = 64, increasing in n; hence
P[some unclean call] <= 2^(-180). Total failure probability <=
2^(-57) + 2^(-n) + 2^(-n) + 2^(-10) + 2^(-180) < 2^(-9.99) < 1/3. So
Pr[output = s] > 2/3 for every N, s with n >= 64; the finite branch
succeeds with probability >= 1 - 2^(-10). QED.

## 10. Resources on every branch (n >= 64)

Sizes, from (1.1)-(1.3) and Section 8: q <= sqrt(n/2)+1;
log2 C0 <= (5/sqrt 2)·sqrt(n) + 12; log2 Wmax <= sqrt(n/2)+4;
log2 K <= 13 + log2(3.54 sqrt n + log2 n + 63) <= 21 + (1/2) log2 n;
runs <= 96; stages <= (J+1) + a2 <= 2n;
log2 Qcap <= 3.54 sqrt(n) + 33 + log2 n.

**Q.** Main branch (n >= 64): every branch has Q <= Qcap, so
log2 Q <= 3.54 sqrt(n) + 33 + log2 n <= 4 sqrt(n) + 7 log2 n (the slack
0.46 sqrt(n) + 6 log2 n - 33 equals 6.7 at n = 64 and increases). Finite
branch (n <= 63): Q <= N(n+10) <= 2^(4 sqrt n) n^7, as verified in Section
8 (g(n) <= -4.4 throughout [2,63]). So Q = O(2^(4 sqrt n) n^7) for all
N >= 2, jointly with the other bounds.

**S_Q.** Peak allocation: one active run's live qubits (current list <=
C0, next list <= C0/2, LE ancilla O(1)), plus the pooled roots (K, each
measured immediately). So S_Q <= 2 C0 + K + O(n), and by (1.2) and the
size bounds, log2 S_Q <= (5/sqrt 2)·sqrt(n) + 13. This is at most
4 sqrt(n) + 4 log2 n for all n >= 64 (the slack 0.46 sqrt(n) + 4 log2 n -
13 equals 14.7 at n = 64 and increases). So S_Q = O(2^(4 sqrt n) n^4).
The peak allocation M_max = 2^((5/sqrt 2) sqrt(n) + 20) of Section 1
dominates this (and the classical list), so the surcharge bound
(5/sqrt 2) sqrt(n) + 21 is valid on every branch.

**S_C.** Live classical data: the active run's list (<= C0 labels, stored
in 2n-bit fields: <= 2n C0 bits), the acquisition counter (O(sqrt n)
bits), decoder records (K roots x (log2 Wmax + 2) bits and K running
residues of <= n + sqrt(n/2) + 13 bits - by the size bounds this is
O(n^2)), LE classical scratch O(n^2) (running arc index, scores), and the
one-off setup (poly(n), including the Section 4 table and the constants
alpha_j, c_r-lookup structure). The dominant term is 2n C0, so
log2 S_C <= (5/sqrt 2)·sqrt(n) + 13 + log2 n, which is at most
4 sqrt(n) + 4 log2 n for all n >= 64 (the slack 0.46 sqrt(n) + 3 log2 n -
13 equals 8.7 at n = 64 and increases). So S_C = O(2^(4 sqrt n) n^4).

**T.** Four components; each is (operation count) x (per-operation cost
including its addressing surcharge <= log2(M_max + 2) <=
(5/sqrt 2) sqrt(n) + 21).

(i) *Per acquisition* (at most Qcap of them): a transform O(n^2) plus at
most Rtry = 16 LE attempts, together <= 2^33 n^4.5 (1 + log2 n) core
steps with internal surcharges included (Lemma 3.1; this also dominates
the per-round classical arithmetic). Acquisition component <= Qcap ·
2^33 n^4.5 (1 + log2 n), whose log2 is at most 3.54 sqrt(n) + 33 + log n
+ 33 + 4.5 log2 n + 1 = 3.54 sqrt(n) + 5.5 log2 n + 67. For n >= 2^12
this is below 4 sqrt(n) + 10 log2 n (slack 0.46 sqrt n + 4.5 log2 n - 67
= 16.4 at n = 2^12, increasing); for 64 <= n < 2^12 the excess is at most
2^67 and is absorbed by the absolute constant of the O().

(ii) *Sieve*: one run does q+1 levels, each level O(C0) list operations
on (n+b)-bit keys with label arithmetic; the total operation count over
all runs and attempts is at most 2n·96·3·C0·(q+1), whose log2 is at
most log2(576 n) + log2 C0 + log2(q+1) <= 9.2 + log2 n + (3.54 sqrt n +
12) + (0.5 log2 n + 1) <= 3.54 sqrt n + 2.5 log2 n + 18 (using (1.2)
and q+1 <= 2 sqrt(n/2)), each operation
costing at most (n + b) + (5/sqrt 2 sqrt(n) + 21) <= 3n bit steps
(n >= 64: b + 3.54 sqrt(n) + 21 <= 0.18 n + 0.5 n + 0.4 n, surcharge at
allocation <= M_max). Component log2 <= 3.54 sqrt n + 2.5 log2 n + 18 +
1.6 + log2 n <= 3.54 sqrt n + 3.5 log2 n + 20 - well inside 4 sqrt(n) +
10 log2 n (slack 0.46 sqrt n + 6.5 log2 n - 20 = 19.7 at n = 64,
increasing).

(iii) *Decoder*: at most 2n stages, each with <= 2^(sqrt(n/2)+14)
candidates (Section 7) and K·O(n) residue updates with surcharges; per
stage log2 <= 0.5 log2 n + 14 + (21 + 0.5 log2 n) + 1 + log2 n + 2 <=
2 log2 n + 38.5, and 2n stages give log2 <= 3 log2 n + 39.5 - inside
4 sqrt(n) + 10 log2 n for all n >= 64.

(iv) *Setup*: polynomial exact arithmetic only (Section 4 table, CRT and
extended-Euclid parameters, the modular-adder constants; there is NO
gate-synthesis setup anymore) - dominated by (ii).

Total: T = O(2^(4 sqrt n) n^10) with an absolute constant (the finite
64 <= n < 2^11 shortfall of component (i) is absorbed). All four bounds
are simultaneous fixed allocations and caps, so they hold on every
branch.

## 11. Envelopes, growth indices, tolerance

Declared envelopes (the structured objects in submission.json are exactly
these):

  B_T(n) = 2^(4 sqrt(n)) n^10    g = 1/2
  B_C(n) = 2^(4 sqrt(n)) n^4     g = 1/2
  B_Q(n) = 2^(4 sqrt(n)) n^4     g = 1/2
  B_samples(n) = 2^(4 sqrt(n)) n^7    g = 1/2

For B(n) = 2^(4 n^(1/2)) n^p (p = 10, 4, 4, 7): log2 B = 4 n^(1/2) +
p log2 n, so log2 log2 B = (1/2) log2 n + log2 4 + o(1) and g(B) = 1/2
for each of the four. The four claims share this one proof and algorithm;
the published numeric vector is [1/2] (time only, per the scoring policy).

**Fractional error tolerance.** The fifth claim is epsilon(n) = 0 under
the model in which every acquired copy is an independent ideal coset
state; the whole proof is carried out under this model, jointly with all
four resource bounds and success > 2/3. No positive tolerance for
malformed copies is claimed; zero does not assert that robustness is
impossible. (Structural remark, not a claim: each root descends from
2^q = 2^(Theta(sqrt n)) leaves, so one adversarially malformed copy per
root costs malformed fraction 2^(-Theta(sqrt n)), outside the supported
fraction grammar c n^a (log2 n)^b.)
