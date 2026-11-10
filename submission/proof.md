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
  (L = B + 1 for odd-part leaves, where B = d0 - 1 and M >= 3; L = n - 1
  for 2-adic leaves, for every N - level n-1 is degenerate when
  N = 2^n, sin(2 pi 2^(n-1) k / N) = sin(pi k) = 0, and is skipped):
  Tex = 2^19 (L+1)^2 ceil(log2(32 (L+1)))  (coins of each type per level),
  V = 1024 n + 1600   (verification rounds), Rtry = 16  (attempts);
  the offset R is a block of 2L+16 fresh fair bits (Section 3).
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

**Controller randomness is dyadic and bounded.** Every random choice the
controller makes is a fixed-length block of fair coin flips, read off one
by one: the offset R (2L+16 bits), the verification multipliers c_r
(n+3 bits each), the decoder bits beta_i (1 bit each). No rejection
sampling, no unbounded draws; the count of flips per attempt is fixed.

**Primitive: coin test.** tau := the permutation of {0,...,2^n-1} adding 1
mod N on [0,N), fixing [N,2^n). tau chi_k = omega^(-k) chi_k. A *coin test
T(w)* on a copy with latent label k prepares one clean ancilla in |+>
(one H), applies tau^w to the data register controlled on the ancilla
(a Toffoli-built modular addition of the constant w: O(n) gates; w = c
mod N for the drawn c), and measures the ancilla in the X basis, or in
the Y basis (one S gate, one H, then a computational measurement). Exact
matrix computation on the ancilla state (|0> + omega^(-wk)|1>)/sqrt 2
gives

  E[X-coin outcome] = cos(2 pi w k / N),   E[Y-coin outcome] = sin(2 pi w k / N),

outcome in {+1,-1}; the data register is left in chi_k exactly (it is an
eigenstate of tau^w), so arbitrarily many coin tests can be run on one
copy, and the control qubit phi_k(s') is untouched throughout. All gates
are exact.

**Construction LE(L) (offset arc decode + verification).** Input: one
(possibly transformed) copy, latent state phi_k(s') (x) chi_k with k
uniform on Z_N; a depth L as fixed in Section 1. Put
Tex = 2^19 (L+1)^2 ceil(log2(32(L+1))). Draw the offset block
R in [0, 2^(2L+16)) (2L+16 fair bits) and put r = R/2^(2L+16).

1. *(Offset arc decode.)* Maintain a dyadic arc containing
   (x + r) mod 1, starting from [0,1) at i = 0. At level i = 0..L-1 let
   t_i = {2^i r} (exact dyadic) and theta_i = (1/2 - t_i) mod 1, and run
   Tex X-coin and Tex Y-coin tests at w = 2^i. With tabulated-in-exact-
   arithmetic rationals a_i, b_i within 2^-(L+10) of cos(2 pi theta_i),
   sin(2 pi theta_i) (Taylor series at the dyadic angle, O(n^2) classical
   work per level), form Z_j = a_i Y_j - b_i X_j per pair (one of each
   type). Writing u = {2^i x}, E[Z_j] is within 2^-(L+8) of
   sin(2 pi (u - theta_i)) + eps with |eps| <= 2^-(L+8) (weight error
   2 x 2^-(L+10)). The sign of sum_j Z_j decides which
   child of the current arc contains x + r: child 0 iff
   {2^i(x + r)} < 1/2, i.e. iff u - theta_i in (-1/2, 0] mod 1. After L
   levels output the candidate set C = {integers k' in [0,N) with
   k'/N + r in the final arc}; the arc has width 2^-L in x + r, i.e.
   width N/2^L in [1, 2] in k', so 1 <= |C| <= 2 and k in C whenever
   every level decision was correct.
2. *(Verification.)* For each khat in C, run V = 1024n+1600 rounds; round
   r draws a fresh block c_r in [0, 2^(n+3)) (n+3 fair bits) and runs one
   X-coin and one Y-coin at w = c_r (equivalently c_r mod N). Score

     score(khat) = sum_r [ Z^X_r tab_0({c_r khat/N}) + Z^Y_r tab_1({c_r khat/N}) ],

   with tab_0, tab_1 the Section 4 table ({c khat/N} = (c_r khat mod N)/N
   by exact integer arithmetic; c_r khat is an (2n+3)-bit product). If
   max_khat score(khat) >= V/2, output the maximizing khat together with
   the control qubit with X applied (the exact state pq_khat(s') if
   khat = k), and release the data register; the attempt *succeeds*.
   Otherwise the attempt *fails*.
3. *(Retry.)* On failure discard the copy and R and repeat on a fresh
   copy with a fresh offset, at most Rtry = 16 attempts per requested
   leaf; if all fail the leaf is not produced (the invoking supplier
   restarts, under the global acquisition cap of Section 8).

**Lemma 3.1 (LE).** One attempt uses at most 2 L Tex + 2|C|·2V coin
tests, and one attempt (including all classical arithmetic and internal
addressing surcharges) costs at most 2^46 n^5.5 (2 + log2 n) core steps;
16 attempts cost 2^50 n^5.5 (2 + log2 n). If an attempt succeeds then
khat = k with probability >= 1 - 2^(-11n) (over the verification coins),
and then the output qubit is EXACTLY pq_k(s'). Moreover the attempt
failure probability, averaged over the offset R, is bounded UNIFORMLY:

  pbar_k := E_R[ P[attempt on a copy with latent label k fails] ] <= 1/32

for EVERY k in [0,N) and EVERY N >= 2 (no dependence on M, no stall
class, no boundary class). In particular P[attempt succeeds] >= 31/32 -
2^(-11n) >= 0.96.

*Proof.* **Per-level decision.** At level i, given all earlier decisions
correct, the arc contains x + r and u = {2^i x} is fixed; each pair
(Z^X_r, Z^Y_r) is independent with means cos(2 pi u), sin(2 pi u), so
E[Z_j] = sin(2 pi (u - theta_i)) + eps, |eps| <= 2^-(L+8). If
|sin(2 pi (u - theta_i))| >= c0 with c0 := 1/(120(L+1)) then
E[sum Z_j] has magnitude >= Tex(c0 - 2^-(L+8)) >= (7/8) Tex c0
(since 2^-(L+8) <= c0/8 for L >= 5), each Z_j lies in [-2,2], and
Hoeffding bounds the wrong-sign majority by
exp(-2 (Tex (7/8) c0)^2 / (Tex·16)) = exp(-Tex (7c0/8)^2 / 8). By the
choice of Tex (using ln(64(L+1)) <= ln 2 ceil(log2(32(L+1)))),
Tex (7c0/8)^2/8 >= 34 > ln(64(L+1)), so the level failure probability is
at most 1/(64(L+1)) on such levels.

**Averaging over R (the uniform bound).** For fixed k and level i, the
offset contribution {2^i r} = {R/2^(2L+16-i)} is uniform on the dyadic
grid of g_i = 2^(2L+16-i) >= 2^(L+17) points, and u - theta_i =
u - 1/2 + {R / 2^(2L+16-i)} mod 1. The values of {R/2^(2L+16-i)} with
|sin(2 pi (u - 1/2 + rho))| < c0 form three arcs of total measure
3 c0 / pi of the circle; a grid of g_i >= 2^(L+17) points meets them in
at most (3 c0/pi) g_i + 3 points. So, averaged over R, the probability
that level i is "boundary" (|sin| < c0) is at most 3 c0/pi + 3/g_i, and

  E_R[P[arc decision at level i wrong | k]]
      <= 3 c0/pi + 3·2^(-L-17) + 1/(64(L+1)).

Summing over the L levels: L·(3 c0/pi) <= 3/(120 pi) <= 0.0080;
3L·2^(-L-17) <= 2^(-16); L/(64(L+1)) <= 1/64 = 0.0156. Total
E_R[P[arc diverges | k]] <= 0.0080 + 2^(-16) + 0.0157 <= 0.024.
This bound is independent of k and of N - for a label with degenerate
k-content at some level (e.g. k = 0 mod M, or N = 2^n at level n-1,
which is why that level is skipped) the offset term carries the arc
along x + r and the same estimate holds verbatim.

**Verification.** c_r is uniform on [0,2^m), m = n+3; w = c_r mod N
induces the pushforward law on Z_N, whose characters satisfy, for
j not= 0 mod N,

  |E[e^(2 pi i j c_r / N)]| = 2^(-m)|1 - e^(2 pi i j 2^m/N)|/|1 - e^(2 pi i j/N)|
                            <= 2^(-m)/|sin(pi j/N)|
                            <= N/2^(m+1) <= 2^n/2^(n+4) = 1/8,

using |sin| >= (2/pi)(pi/N) = 2/N at j and N/2^m <= 1/8. Hence for the
true label E[cos^2] = (1 + E[cos(2c_r k/N)·2pi-argument])/2 >= (1 -
1/8)/2 = 7/16 unless 2k = 0 mod N, in which case cos^2 = 1; likewise
E[sin^2] >= 7/16; with the tab error (4.1),

  E[score(khat = k)] >= V(7/16 + 7/16 - 2/625) > 0.87 V.

For khat not= k: E[cos(c_r k)cos(c_r khat)] and E[sin·sin] are half-sums
of characters at k + khat and k - khat (neither 0 mod N, except
khat = -k where the cosine term is E[cos^2] and the sine term is
-E[sin^2], combining to ~0), each of modulus <= 1/8, so

  |E[score(khat)]| <= 2 V (1/8 + 1/625) < 0.26 V  for every wrong khat.

Each round contributes to score - its mean an increment in an interval
of length 4; Hoeffding with deviations (0.87 - 1/2)V and (1/2 - 0.26)V:

  P[ score(k) < V/2 ] <= exp(-2(0.37V)^2/(16V)) <= 2^(-25n),
  P[ score(khat) >= V/2 ] <= exp(-2(0.246V)^2/(16V)) <= 2^(-11n)

(n >= 64, V = 1024n+1600: 2·0.37^2/16·V >= 0.0171V >= 25 ln 2·n and
2·0.246^2/16·V >= 0.00756(1024n+1600) >= 11 ln 2·n). So if k in C, a wrong khat beats it with
probability <= 2^(-11n); if k not in C (arc diverged) every candidate is
wrong and the attempt still "succeeds" with probability
<= 2 |C| 2^(-11n) <= 2^(-11n+1). Combining with the arc analysis:

  pbar_k <= 0.024 + 2^(-11n+1) <= 0.024 + 2^(-703) <= 1/32,
and on success the output is the exact state pq_k(s') whenever khat = k. Cost:
2LTex + 4V <= 2^21 (L+1)^3 (2 + log2(L+1)) coin tests, each <= 8n + 8
gates with surcharge <= (5/sqrt 2) sqrt n + log2 n + 22 (per test
<= 2^7 n^1.5),
quantum total <= 2^28 (n+1)^4.5 (2 + log2 n); classical per round
O(n^2) (one (2n+3)-bit product mod N and one tab lookup) with
surcharges included, total per attempt <=
2^45 n^5.5 (2 + log2 n) per attempt. One attempt <= 2^46 n^5.5 (2+log2 n);
sixteen <= 2^50 n^5.5 (2+log2 n). QED.

**Leaves.** A *leaf* for a sieve of depth B is a successful LE(B+1)
output on a transformed copy, accepted (odd part) iff khat < 2^(B+1)
(both children of every low pattern lie in [0,2^(B+1)), so the filter
does not favour a top bit); 2-adic leaves use LE(n-1) with label
kk = khat mod 2^wd, no filter. Expected acquisitions per accepted
odd-part leaf <= 2/(31/32 - 2^(-11n)) <= 2.1 <= 3; per 2-adic leaf
<= 1.1 <= 2. The accepted-leaf label law is close to uniform but not
exactly uniform (pbar_k varies with k by at most 1/32 in total mass);
Section 6 proves exactly what the decoder consumes, and needs only the
UNIFORM bound pbar_k <= 1/32.

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
write the label k = low + 2^B tau with 0 <= low < 2^B and tau in {0,1};
for a 2-adic leaf of width wd, low = kk mod 2^(wd-1) and tau = bit wd-1
of kk, with the two children of a low g being the two label classes
{g mod 2^wd} and {g + 2^(wd-1) mod 2^wd} of Z_N. Let G be the sigma-field
generated by: all low parts of the run's consumed leaves; all level
measurement outcomes (the keep coins); and the controller's decisions
(arrival-order pairing, class partitions, retry and pooling decisions,
which select by index and never read bits at positions >= B - see (a)
below).

**Lemma 6.1 (uniform failure bound).** pbar_k <= 1/32 for every k in
[0,N) and every N >= 2 (Lemma 3.1, averaged over the offset R). This is
the ONLY property of the label law used below; it holds uniformly, with
no stall class and no M-dependence.

**Lemma 6.2 (root dephasing).** Conditional on G and all other
independent randomness, the top bits tau of the leaves consumed by any
given final qubit are independent, and for EVERY low pattern g the
conditional law obeys

  P[tau = 1 | low = g, G] = (1 - pbar_(g + 2^B)) / (2 - pbar_(g) - pbar_(g + 2^B))
                           =: 1/2 + delta(g),
  |delta(g)| <= (pbar_(g) + pbar_(g+2^B)) / (2 (2 - pbar_(g) - pbar_(g+2^B)))
              <= (1/16) / (2 (2 - 1/16)) < 1/60                       (6.0)

for every g, both children included - uniformly over the label space, for
the odd part (children in [0,2^(B+1))) and the 2-adic part (children
averaged over their classes in Z_N; class averages of quantities bounded
by 1/32 are bounded by 1/32). Every final label is

  label = 2^B W,   W = cst + sum_(S+) tau - sum_(S-) tau,                (6.1)

where cst = (signed low sum)/2^B is a G-measurable integer, S+ and S- are
disjoint G-measurable sets, and |S+| + |S-| = 2^q (q >= 1; for the odd
part q >= 6 by (1.4), 2^q >= 64). For every real phi,

  |E[ e^(2 pi i phi W) | G ]| <= mu(phi)^(2^q),                          (6.2)
  mu(phi) := sqrt( cos^2(pi phi) + 4 (1/60)^2 sin^2(pi phi) ),

so for |phi| in [1/8, 1/2] (where cos^2(pi phi) <= cos^2(pi/8)):

  |E[ e^(2 pi i phi W) ]| <= mu^(2^q) <= 0.925^(2^q) <= 0.925^64 < 0.007,(6.3)

  |E[ (-1)^W ]| <= mu(1/2)^(2^q) <= (1/30)^(2^q) <= 1/900,
  so  Pr[ W odd ] >= (1 - 1/900)/2 > 0.499 for 2^q >= 2.               (6.4)

*Proof.* (a) *What a level reads.* A level-j combine reads only the
residue class of u = label/2^(p_j) mod 2^(b_j) - i.e. label bits in
[p_j, p_(j+1)) - and p_(j+1) <= B by construction (the widths b_j sum to
exactly B). Because labels are SIGNED sums of leaf labels with no folding
(Section 5), bits below position B of any level-j label depend only on
the low parts of the leaves: for integers, (a + c) mod 2^t = (a mod 2^t +
c mod 2^t) mod 2^t for every sign of a and c - carries and borrows
propagate strictly upward - and each leaf label k = low + 2^B tau
contributes tau only at positions >= B. Although the controller stores
full labels, every decision (pairing, partition, retry, pooling) is a
function of class bits below B, of arrival order, and of keep coins
only, so G as defined does not read any tau.

(b) *What the coins are.* The keep coin has probability exactly 1/2
regardless of phases and labels (Lemma 5.1), and different pairs act on
disjoint qubits.

(c) *Conditional leaf law.* The copies are independent, and each attempt
uses a fresh copy and a fresh offset block R, so the triples
(low_ell, tau_ell, coins_ell, R_ell) are independent across leaves ell.
The attempt success event of leaf ell is a function of its own copy,
offset and coins; the filter k < 2^(B+1) is a function of its own label
and treats the two children of every low symmetrically (both lie in
[0,2^(B+1))). Conditioning on G (hence on which leaves were consumed and
with which lows) therefore leaves the tau_ell conditionally independent,
with the stated two-children Bernoulli law: given low = g, the consumed
leaf's tau is 1 exactly when the successful attempt was made on the
child g + 2^B, which happens with probability proportional to
1 - pbar_(g+2^B) among the two children (the R-average pbar enters
because R is fresh and independent per attempt). The bound (6.0) is
elementary algebra from pbar <= 1/32.

(d) *Conclusion.* Every kept combine replaces two labels over disjoint
leaf sets by their signed difference, so by induction a final label is
sum_ell eps_ell k_ell over its exactly 2^q leaves with every eps_ell in
{+1,-1}. Substituting k_ell = low_ell + 2^B tau_ell gives (6.1) with
S+ = {eps = +1}, S- = {eps = -1}, cst G-measurable. Now the decisive
point: by (6.0), for EVERY phi and EVERY leaf - whatever its low, so
regardless of which leaves the sieve's value-based selection happened to
consume -

  |E[ e^(2 pi i phi eps tau_ell) | G ]|
     = | cos(pi phi eps) + 2 i delta(g_ell) sin(pi phi eps) |
     = sqrt( cos^2(pi phi) + 4 delta(g_ell)^2 sin^2(pi phi) )
     <= sqrt( cos^2(pi phi) + 4 (1/60)^2 sin^2(pi phi) ) = mu(phi) < 1.

Since the tau_ell are conditionally independent given G (step (c)),

  |E[ e^(2 pi i phi W) | G ]| = |e^(2 pi i phi cst)| · prod_ell |E[e^(2 pi i phi eps tau_ell)|G]|
                              <= mu(phi)^(2^q),

which is (6.2) - a DETERMINISTIC bound given G, with no averaging over
lows and no independence claim about the selected lows themselves (the
sieve's selection may correlate the low parts arbitrarily; each
per-leaf factor is bounded regardless). Taking expectation over G gives
(6.3); at phi = 1/2, mu(1/2) = 2·(1/60) = 1/30 (since
cos(pi/2) = 0), giving (6.4). QED.

**Roots.** A *root* of a run is a final qubit with its known signed
W = label/2^B. For the odd part (B = d0 - 1 >= n - 2) the label invariant
gives |W| < 2^(n+1+q)/2^B <= 2^(q+3) = Wmax. Roots of one run have
pairwise disjoint leaf sets (the pairing is a matching), so conditional
on G their remaining tau randomness is independent; roots of different
runs are independent outright. The decoder pools at most K roots per
stage, chosen by index. Signed W's are harmless downstream: the odd part
uses f_i = 2^j W_i (cos is even, sin odd, so the basis-averaged
expectation (1/2)cos(2 pi f Delta) holds for negative f verbatim), and
the 2-adic part uses only the parity of W.

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
other possibility, probability <= 2^(-11n+1) per attempt, is priced in
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
[1/8, 1/2], and by (6.2)-(6.3) (f_i = 2^j W_i; root i's leaves are
disjoint from Fs_(i-1), so (6.2) holds conditionally on Fs_(i-1) as
well, and real part is at most modulus),

  E[xi_i | Fs_(i-1)] <= (1/2) Re E[e^(2 pi i 2^j Delta W_i) | Fs_(i-1)]
                      <= (1/2) · 0.925^(2^q) <= (1/2) · 0.007 < 0.004.

*Concentration.* For each fixed candidate, sum_i (xi_i - E[xi_i|Fs_(i-1)])
is a martingale whose increments lie in intervals of length 2; by
Azuma-Hoeffding it deviates by at least K/64 with probability at most
exp(-2(K/64)^2/(2·2·K)) = exp(-K/8192). Outside these events for zeta0 and
every far candidate,

  score(zeta0) >= (K/2)cos(2 pi 2^(-10)) - K/64 - K/625
                > (K/2)·0.007 + K/64 + K/625 >= score(far zeta),

because (1/2)(cos(2 pi 2^(-10)) - 0.007) > 0.49 > 2/64 + 2/625
= 0.0345.
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
Shift_(sh_g), which makes the secret s - sh_g = M 2^g rem; run LE(n-1)
(label k uniform on Z_N; LE's output is pq_k, and no further conjugation
is applied; depth n-1 for EVERY N, including N = 2^n where M = 1 and
level n-1 is degenerate - Lemma 3.1's uniform bound has no M-dependence,
so nothing here changes at M = 1). With kk = k mod 2^wd (the Section 6
law reduced mod 2^wd, nearly uniform on [0,2^wd)), the phase is

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
  W is odd with probability > 0.499; if W is odd the phase is (-1)^rem
  and an X measurement yields rem mod 2 exactly; if W is even, discard
  the root and take another. A run supplies >= 2^(b+1) roots (Lemma
  5.2), so no odd W appears with probability <= 0.501^(2^(b+1)) <
  2^(-2^b).

Set bit g of s2; in the ideal run with s1 correct, all bits are correct.
Output s = (s1 + M s2) mod N.

**Assembly.** Main branch n >= 64: compute a2, M, d0, b, all q(B), C0(B),
Wmax, all P_j, all alpha_j, all sh_g, and the Section 4 table - polynomial
exact setup, charged once. A binary acquisition counter is maintained at
amortized O(1) flips per acquisition. Expected acquisitions: the odd part
runs <= n stages x runs(<= 96) runs x <= 3 attempts x C0(d0-1) leaves x 3
acquisitions, for <= 864·n·C0(d0-1); the 2-adic part needs, per bit, an
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
bit's run yields no odd-W root, probability <= a2·2^(-2^b) <= n·2^(-n)
for n >= 64 (b = ceil(sqrt(2(d0-1))) >= 11 and 2^b >= 2n there: at
n = 64, b = 12, 2^b = 4096 >= 2·64; and 2^b grows exponentially in
sqrt n while n grows linearly). The wd = 1 repeats succeed a.s. and are
hard-capped by Qcap. Sieve retry exhaustion over all stages:
<= 2n·2^(-1200) <= 2^(-n) for n >= 64 (1200 - log2(2n) >= n). By Markov
and Section 8, the ideal run reaches Qcap with probability <= 1/1024;
capping changes the run only on that event. The actual run differs from
the ideal one only through unclean LE calls (verification accepted a
wrong label); by Lemma 3.1 and a union bound over <= Qcap attempts,
P[some unclean call] <= Qcap·2^(-11n+1). By (1.2) and Section 8
(Qcap = 2^10·1200·n·C0, log2(1200·2^10) <= 21),
log2 Qcap <= 3.54 sqrt(n) + 33 + log2 n, and
11n - 1 - log2 Qcap >= 703 - 68 > 600 at n = 64, increasing in n; hence
P[some unclean call] <= 2^(-600). Total failure probability <=
2^(-57) + 2^(-n) + 2^(-n) + 2^(-10) + 2^(-600) < 2^(-9.99) < 1/3. So
Pr[output = s] > 2/3 for every N, s with n >= 64 - including
N = 2^n (M = 1), where the odd part is vacuous and the 2-adic part runs
unchanged (Sections 3, 6 and 8 have no M-dependence); the finite branch
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
(5/sqrt 2) sqrt(n) + log2 n + 22 is valid on every branch.

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
(5/sqrt 2) sqrt(n) + log2 n + 22).

(i) *Per acquisition* (at most Qcap of them): a transform O(n^2) plus at
most Rtry = 16 LE attempts, together <= 2^50 n^5.5 (2 + log2 n) core
steps
with internal surcharges included (Lemma 3.1's cost: the quantum coin
tests and the classical per-round arithmetic). Acquisition component
<= Qcap · 2^50 n^5.5 (2 + log2 n), whose log2 is at most
3.54 sqrt(n) + 33 + log n + 50 + 5.5 log2 n + 2
= 3.54 sqrt(n) + 6.5 log2 n + 85. For n >= 2^13 this is below
4 sqrt(n) + 10 log2 n (slack 0.46 sqrt n + 3.5 log2 n - 85 = 2.1 at
n = 2^13, increasing); for 64 <= n < 2^13 the excess is at most 2^85 and
is absorbed by the absolute constant of the O().

(ii) *Sieve*: one run does q+1 levels, each level O(C0) list operations
on (n+b)-bit keys with label arithmetic; the total operation count over
all runs and attempts is at most 2n·96·3·C0·(q+1), whose log2 is at
most log2(576 n) + log2 C0 + log2(q+1) <= 9.2 + log2 n + (3.54 sqrt n +
12) + (0.5 log2 n + 1) <= 3.54 sqrt n + 2.5 log2 n + 18 (using (1.2)
and q+1 <= 2 sqrt(n/2)), each operation
costing at most (n + b) + (5/sqrt 2 sqrt(n) + log2 n + 22) <= 3n bit
steps (n >= 64: b + 3.54 sqrt(n) + log2 n + 22 <= 0.18 n + 0.5 n +
0.14 n + 0.4 n, surcharge at allocation <= M_max). Component log2 <= 3.54 sqrt n + 2.5 log2 n + 18 +
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
