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

**Provenance and dependency.** PS2 is a deliberate simplification and
independent verification of the frontier result CS1 (AdamGagol, submission
f148181 on this benchmark, whose restored proof was read), which builds on
G. Kuperberg's sieves (SIAM J. Comput. 35(1):170-188, 2005; LIPIcs
22:20-34, 2013, arXiv:1112.3333). Used from CS1 with credit and declared
dependency: the latent-label model and the exact transforms Mult/Shift
(their Section 3); the rational cosine/sine table (their Section 4); the
top-bit independence lemma and its sigma-field proof pattern (their Section
8); the free-frequency decoder - unit multipliers, dyadic candidate arcs,
near/far decomposition, Azuma concentration (their Section 9); and the
Shift-based 2-adic bit extraction (their Section 10). New here: the sieve.
CS1 merges phase-vector registers through residue measurements with
renumbering permutations and quantum table lookups; PS2 sieves plain qubits:
each combine is one CNOT, one computational-basis measurement and at most
one X, and all bookkeeping is classical integer label arithmetic. The label
law the decoder needs then follows from a shorter argument (Section 6:
every leaf of a surviving qubit enters its label with coefficient +-1, so
the fair top bits of its disjoint leaves dephase the root frequency), and
the only non-elementary quantum component in the algorithm is one phase
estimation (Section 3) with an explicit error budget. The price is a
strictly worse exponential constant (about 3.6 sqrt(n) in the exponents of
the intermediate bounds, versus CS1's sqrt(2) sqrt(n)) and quantum space
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
most M_max = 2^(2 sqrt(2n) + 17) (Section 10), so every surcharge is at
most 2 sqrt(2n) + 17.

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
* Qcap as fixed in Section 8.

Size facts (n >= 64, B <= d0 - 1 <= n - 2): B/b <= B/sqrt(2B) = sqrt(2B)/2
(since b >= sqrt(2(d0-1)) >= sqrt(2B)), so

  q(B) <= sqrt(2n)/2 + 1 = sqrt(n/2) + 1,                               (1.1)
  log2 C0(B) = 3q(B) + b + 8 <= 3(sqrt(n/2) + 1) + sqrt(2n) + 1 + 8,
  i.e.      log2 C0(B) <= (3/sqrt(2) + sqrt(2)) sqrt(n) + 12
                      = (5/sqrt(2)) sqrt(n) + 12,                        (1.2)
  log2 Wmax = q(d0-1) + 3 <= sqrt(n/2) + 4.                             (1.3)

runs: K/2^(b+1) = 2^13(X + Y + 51)/2^(b+1) with X = ceil(log2 C0(d0-1)) and
Y = ceil(log2 n). log2(K/2^(b+1)) = 13 + log2(X + Y + 51) - (b+1), and
X + Y + 51 <= (5/sqrt 2) sqrt(n) + log2 n + 63 grows more slowly than
b + 1 >= sqrt(2n), so the ratio is decreasing in n for n >= 64; at n = 64
(X = 37, Y = 6) it is 94. Hence runs <= 94 for all n >= 64.

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

## 3. Label extraction LE

**Construction LE.** tau := the permutation of {0,...,2^n-1} adding 1 mod N
on [0,N), fixing [N,2^n). On a (possibly transformed) copy with latent state
(|0,x> + |1,(x+s') mod N>)/sqrt 2:

1. Prepare Lpe = 3n + 4 qubits T in |0>; apply H^(x) Lpe.
2. For i = 0..Lpe-1, controlled on T_i, apply tau^(2^i) to the data
   register (reversible classical arithmetic, Section 2).
3. Apply the inverse QFT over Z_2^Lpe to T approximately: each non-Clifford
   R_z(pi/2^j) is synthesized to operator norm delta_LE = 2^-(5n+16) with
   T-count at most 3 ceil(log2(1/delta_LE)) + c_s <= 16n + 20 (standard
   ancilla-free Clifford+T z-rotation synthesis, e.g. Ross-Selinger; any
   published polylog(1/delta) bound suffices for the envelopes).
4. Measure T, obtaining t in [0,2^Lpe); compute
   khat = (-round(t N / 2^Lpe)) mod N. Output label khat, apply X to the
   control, release everything else.

**Lemma 3.1 (LE).** One call costs at most c_E n^4 core steps *including
its internal addressing surcharges* (allocation <= 6n + O(1); c_E = 2^12
suffices), uses at most 6n + O(1) qubits beyond the copy, and is *clean* -
khat equals the latent label k - with probability >= 1 - 2^(-2n-2).

*Proof.* tau chi_k = omega^(-k) chi_k and
|psi> = (2N)^(-1/2) sum_k omega^(-kx)(|0> + omega^(k s')|1>) chi_k, so on
the chi_k component step 2 is textbook phase estimation of phi = (-k mod
N)/N. The amplitude of outcome t before the inverse QFT is the geometric
sum a(t) = 2^(-Lpe) sum_j e^(2 pi i j(phi - t/2^Lpe)), whence for the
circular deficit v = t - 2^Lpe phi, |v| <= 2^Lpe/2,

  |a(t)|^2 <= 1/(4 v^2)                                              (3.1)

(using |sin(pi u)| <= 1 in the numerator and |sin(pi u')| >= 2|u'| for
|u'| <= 1/2 in the denominator). Summing (3.1):
P[|t - 2^Lpe phi| >= 2^(n+3)] <= 1/(2^(n+3) - 1) <= 2^(-n-3). Whenever
|t - 2^Lpe phi| <= 2^(n+3),
|t N/2^Lpe - (-k mod N)| <= N 2^(n+3)/2^(3n+4) <= 2^n 2^(n+3) 2^(-3n-4)
= 2^(-n-1) < 1/2, so rounding returns khat = k, and the post-measurement
control is pq_k(s') up to leakage mass <= 2^(-n-3). Gate error: at most
(3n+4)(3n+3)/2 < 5n^2 rotations, each within delta_LE, perturb the POVM by
<= 5n^2 delta_LE <= 2^(-5n-12). Clean probability >= 1 - 2^(-n-3) -
2^(-n-3) - 2^(-5n-12) >= 1 - 2^(-n-2) > 1 - 2^(-2n-2). Cost: Lpe+1
Hadamards, Lpe controlled permutations at O(n^2) core steps each, < 5n^2
rotations at O(n) T-count, one Lpe-bit measurement, and O(n^2) classical
rounding; with per-gate surcharges <= log2(10n) this is <= c_E n^4. QED.

**Leaves.** A leaf for a sieve of depth B is an LE output on a transformed
copy, accepted iff khat < 2^(B+1). The latent label k is uniform on Z_N and
its bits are independent, so the acceptance event (a function of bits at
positions >= B+1, of probability 2^(B+1)/N >= 2^d0/N >= 1/2) is
independent of the bits below position B+1; conditional on acceptance, k is
uniform on [0,2^(B+1)), all its bits are fair and independent, and the
qubit is pq_k(s'). Expected acquisitions per accepted leaf: at most 2.

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

Input: a supplier of leaves for depth B (labels uniform on [0,2^(B+1)), by
Section 3). Levels j = 0..q-1 (q = q(B)): a *level-j qubit* has label a
nonnegative integer divisible by 2^(p_j), p_j = jb; the final level q-1 has
width b_(q-1) = B - (q-1)b in [1,b] and outputs labels divisible by 2^B.

**Level step.** Given a list of C level-j qubits (j <= q-1):
1. Partition into residue classes of (label / 2^(p_j)) mod 2^(b_j),
   b_j = p_(j+1) - p_j; pair within each class in arrival order. At most
   one qubit per class is unpaired, so at least (C - 2^(b_j))/2 pairs are
   formed, and (C - 2^(b_j))/2 >= (15/32) C whenever C >= 2^(b+4).
2. For each pair (q1,k1),(q2,k2): apply CNOT(q1 -> q2), measure q2.
   Outcome 0 (probability exactly 1/2): discard both. Outcome 1: q1 carries
   label |k1 - k2| (Lemma 5.1; fold the sign with an X on q1 if needed);
   keep it. Class-sharing inputs give k1 - k2 = 2^(p_j) 2^(b_j)(u1 - u2),
   so output labels are divisible by 2^(p_(j+1)).

**Lemma 5.1 (combine algebra).** For ideal (q1,k1),(q2,k2): after
CNOT(q1 -> q2) and measuring q2, outcome 0 (probability exactly 1/2) leaves
q1 with label k1 + k2, and outcome 1 (probability exactly 1/2) leaves q1
with label k1 - k2, in both cases up to a global phase; the probabilities
are exactly 1/2 regardless of s', k1, k2. X-conjugation maps a labelled
qubit with label k to one with label -k.

*Proof.* (|0> + w1|1>)(|0> + w2|1>)/2 with w_i = omega^(k_i s') maps under
CNOT to (1/2)(|00> + w2|01> + w1|11> + w1w2|10>); the q2 = 0 branch of q1
is (|0> + w1w2|1>)/sqrt 2 (label k1 + k2), the q2 = 1 branch is
w2(|0> + (w1/w2)|1>)/sqrt 2 (label k1 - k2); the two branches have
probability exactly 1/2 each. X(|0> + w|1>) = w(|0> + w^(-1)|1>). QED.

**Label invariant.** A level-j label is a folded (nonnegative) signed sum
of at most 2^j leaf labels, each < 2^(B+1) <= 2^n; hence it is < 2^(n+1+j)
and divisible by 2^(p_j). A final label is < 2^(n+1+q) and divisible by
2^B.

**Lemma 5.2 (survival).** Run SIEVE(B) from C0 = 2^(3q + b + 8) level-0
qubits. With probability >= 1 - 2^(-400) the final list has at least
2^(b+5) qubits.

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

**Corollary 5.3 (run cost).** One run consumes exactly C0 leaves (at most
2 C0 acquisitions in expectation; hard-capped by Section 8) and
O(C0 (n + b)(q+1)) core steps: per level, a radix partition into 2^(b_j)
classes costs O(C0 (n + b_j)), pairing and label arithmetic O(n) per pair,
and the quantum work is one CNOT and one measurement per pair plus folding
X's. All loops are fixed-length.

## 6. Top-bit independence

Fix one run of depth B. Write each consumed leaf label k = low + 2^B tau
with 0 <= low < 2^B and tau in {0,1}; by Section 3, low and tau are
independent and tau is fair. Let G be the sigma-field generated by: all low
parts of the run's consumed leaves (accepted and rejected); all level
measurement outcomes (the keep coins); and the controller's decisions
(arrival-order pairing, class partitions, retry and pooling decisions,
which select by index).

**Lemma 6.1 (top-bit independence; after CS1 Lemma 8.1).** Conditional on
G and all other independent randomness, the top bits tau of the leaves
consumed by any given final qubit are i.i.d. fair. Every final label is

  label = 2^B W,   W = cst + sum_(S+) tau - sum_(S-) tau,                (6.1)

where cst = (signed low sum)/2^B is a G-measurable integer (the label is
divisible by 2^B), S+ and S- are disjoint G-measurable sets, and
|S+| + |S-| equals the number of the qubit's leaves, namely 2^q·(each kept
combine subtracts two labels over disjoint leaf sets, so a final label is
sum eps_ell k_ell with eps_ell in {+-1} on exactly its 2^q leaves; q >= 1,
so |S+| + |S-| >= 2). For every real phi,

  |E[ e^(2 pi i phi W) | G ]| = |cos(pi phi)|^(2^q) <= |cos(pi phi)|,   (6.2)

  Pr[ W odd | G ] = 1/2.                                               (6.3)

*Proof.* A level-j combine reads only the residue class of label/2^(p_j)
mod 2^(b_j) - label bits in [p_j, p_(j+1)) - and p_(j+1) <= B by
construction (the widths sum to exactly B). Bits below B of a signed sum of
labels depend only on the low parts (carries propagate upward only: adding
2^B tau changes bits at positions >= B). The keep coin has probability
exactly 1/2 regardless of phases (Lemma 5.1). Arrival-order pairing,
partitions, retries and pooling are functions of low bits and indices
only. Hence the joint law of (tau, low, coins, decisions) factorizes as
law(tau) x law(low) x law(coins, decisions | low): conditional on G the
tau's are i.i.d. fair. Expanding (6.1) and multiplying the independent
fair-bit characteristic functions E e^(2 pi i phi tau) = e^(i pi phi)
cos(pi phi) gives (6.2); phi = 1/2 gives (6.3). cst is an integer because
the final label is divisible by 2^B, and is G-measurable because it is a
fixed function of low parts and signs. QED.

**Roots.** A *root* of a run is a final qubit with its known W = label/2^B.
For the odd part (B = d0 - 1 >= n - 2) the label invariant gives
|W| < 2^(n+1+q)/2^B <= 2^(q+3) <= Wmax. Roots of one run have pairwise
disjoint leaf sets (the pairing is a matching), and roots of different runs
are independent; the decoder pools at most K roots per stage, chosen by
index. For the 2-adic use (Section 8) only the parity of W matters.

## 7. Odd part: s1 = s mod M by free-frequency decoding

This section adapts CS1 Section 9 (used with credit); roots replace tree
outputs and Lemma 6.1 replaces their Lemma 8.1. If M = 1 put s1 = 0 and
skip. Otherwise M >= 3, so N >= 3·2^a2 and B := d0 - 1 >= a2 + 1. Put
theta = s1/M in [0,1). Every stage uses depth B (leaves: labels uniform on
[0,2^(B+1)) = [0,2^d0), acceptance probability 2^d0/N >= 1/2).

**Stage source.** Compute alpha_j (extended Euclid + CRT) with
alpha_j = 1 (mod 2^a2) and alpha_j = 2^j (2^(B - a2))^(-1) (mod M); this is
a unit mod N (a unit mod both prime-power-free factors: 1 mod 2^a2, and
2^(B-a2) is invertible mod the odd M). A leaf: acquire a copy; apply
Mult_(alpha_j); run LE; accept iff k < 2^(B+1); apply X. In the ideal run
accepted labels are i.i.d. uniform on [0,2^(B+1)) and the qubit is
pq_k(alpha_j s). For every integer W,

  2^B W (alpha_j s / N) = W 2^(B - a2) alpha_j s / M
                        = 2^j W s1 / M   (mod 1),                      (7.1)

because 2^(B - a2) alpha_j = 2^j (mod M) makes the difference
W s (2^(B - a2) alpha_j - 2^j)/M an integer multiple of W s, and
s = s1 (mod M) makes W 2^j (s - s1)/M an integer. So a root of stage j is
ideally (|0> + e^(2 pi i f theta)>|1>)/sqrt 2 with the KNOWN frequency
f = 2^j W. (7.1) is CS1's (9.1) with d0 - 1 in place of their d - 1.

**Stage execution.** Obtain K roots by pooling runs = ceil(K/2^(b+1)) runs
(each run supplies >= 2^(b+1) roots by Lemma 5.2; the pool succeeds with
probability >= 1 - runs·2^(-400)). For i = 1..K: draw a fair bit beta_i;
measure root i in X (beta_i = 0) or Y (beta_i = 1); record Z_i in {+1,-1}
and (f_i, beta_i). Ideally E[Z_i | f_i, beta_i] = cs_(beta_i)(f_i theta).

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
stage. Root i's leaves are disjoint from all earlier roots' leaves and from
all conditioning data, so conditional on Fs_(i-1) and the run's G, W_i
still has independent fair top bits (Lemma 6.1). For a candidate zeta put
Delta = theta - zeta (circular difference) and
xi_i = Z_i cs_(beta_i)(f_i zeta). Averaging the fair basis bit:

  E[xi_i | Fs_(i-1), G, W_i] = (1/2) cos(2 pi f_i Delta).

By (4.1) the computed score differs from sum_i xi_i by at most K/625.

*Near point.* Some candidate zeta0 has |Delta0| <= 2^-(P_j+1) (stage 0:
the grid covers the circle at spacing 2^(-P_j); stage j >= 1: theta lies in
the candidate arc). Since |f_i| <= 2^j Wmax,

  |f_i Delta0| <= 2^j Wmax·2^-(j + ceil(log2 Wmax) + 10) <= 2^(-10),

so E[xi_i | Fs_(i-1)] >= (1/2) cos(2 pi 2^(-10)) >= (1/2) cos(pi/128).

*Far points.* Call zeta far if |Delta| >= 2^-(j+3). In stage 0,
|Delta| <= 1/2; in stage j >= 1 both theta and zeta lie within rad_j of
z_(j-1), so |Delta| <= 2^-(j+1). Hence xx := 2^j |Delta| lies in [1/8,
1/2] for every far zeta. By (6.2) with phi = 2^j Delta (f_i = 2^j W_i),
and real part at most modulus,

  E[xi_i | Fs_(i-1)] <= (1/2) Re E[e^(2 pi i 2^j Delta W_i) | ·]
                      <= (1/2) |cos(pi·2^j Delta)| <= (1/2) cos(pi/8).

*Concentration.* For each fixed candidate, sum_i (xi_i - E[xi_i|Fs_(i-1)])
is a martingale whose increments lie in intervals of length 2; by
Azuma-Hoeffding it deviates by at least K/64 with probability at most
exp(-2(K/64)^2/(2·2·K))·= exp(-K/8192). Outside these events for zeta0 and
every far candidate,

  score(zeta0) >= (K/2)cos(pi/128) - K/64 - K/625
                > (K/2)cos(pi/8) + K/64 + K/625 >= score(far zeta),

because (1/2)(cos(pi/128) - cos(pi/8)) > 0.0379 > 2/64 + 2/625 = 0.03445.
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
Shift_(sh_g), which makes the secret s - sh_g = M 2^g rem; run LE (label
k uniform on Z_N); apply X. With kk = k mod 2^wd (uniform on [0,2^wd)
since 2^wd | N), the phase is

  e^(2 pi i k M 2^g rem / N) = e^(2 pi i kk rem / 2^wd),

the extra factor being e^(2 pi i h·rem) = 1 for the integer h = k div 2^wd
(because 2^wd 2^g M = N). Use kk as the leaf label (no acceptance).

* wd = 1: kk = 1 with probability 1/2: an X measurement gives + iff rem is
  even; kk = 0: discard and repeat.
* wd >= 2: run SIEVE(wd - 1) on kk-leaves (depth B = wd - 1, labels
  uniform on [0,2^wd)); a root has label 2^(wd-1) W and phase
  e^(2 pi i 2^(wd-1) W rem / 2^wd) = e^(pi i W rem). If W is odd this is
  (-1)^rem and an X measurement yields rem mod 2 exactly; if W is even,
  discard the root and take another (each root's W is odd with probability
  exactly 1/2 by (6.3); a run supplies >= 2^(b+1) roots, so no odd W
  appears with probability <= 2^(-2^10)).

Set bit g of s2; in the ideal run with s1 correct, all bits are correct.
Output s = (s1 + M s2) mod N.

**Assembly.** Main branch n >= 64: compute a2, M, d0, b, all q(B), C0(B),
Wmax, all P_j, all alpha_j, all sh_g, and the Section 4 table - polynomial
exact setup, charged once. A binary acquisition counter is maintained at
amortized O(1) flips per acquisition. Expected acquisitions: the odd part
runs <= n stages x runs(<= 94) runs x <= 3 attempts x C0(d0-1) leaves x 2
acquisitions, for <= 564·n·C0(d0-1); the 2-adic part needs, per bit, an
expected <= 2 trees x 3 attempts x 2 acquisitions x C0(wd-1) plus <= 4
wd = 1 acquisitions, for <= 12n·C0(d0-1) + 4n in total. Define

  Q* := 600·n·C0(d0-1),   Qcap := 2^10·Q*.

Before an acquisition would exceed Qcap, PS2 stops, releases everything,
and outputs 0. Every branch terminates: all loops are fixed-length or
acquisition-capped.

## 9. Success probability

Ideal uncapped run: the odd part fails with probability <= 2^(-57)
(Lemma 7.1 union); given correct s1, the 2-adic part fails only if some
bit's run yields no odd-W root (<= a2·2^(-2^10) <= 2^(-1000)) - the wd = 1
repeats succeed a.s. and are hard-capped by Qcap. Sieve retry exhaustion
over all stages: <= 2n·2^(-1200) <= 2^(-1180). By Markov and Section 8,
the ideal run reaches Qcap with probability <= 1/1024; capping changes the
run only on that event. The actual run differs from the ideal one only
through unclean LE calls; by Lemma 3.1 and a union bound over <= Qcap
calls, P[some unclean call] <= Qcap·2^(-2n-2). By (1.2) and Section 8
(Qcap = 2^10·600·n·C0, and log2(600·2^10) <= 20),
log2 Qcap <= 3.54 sqrt(n) + 32 + log2 n, and
2n + 2 - log2 Qcap >= 130 - 66.4 > 63 at n = 64, increasing in n (the left
side grows linearly, the right as sqrt n); hence P[some unclean call]
<= 2^(-63). Total failure probability <= 2^(-57) + 2^(-1000) + 2^(-1180) +
2^(-10) + 2^(-63) < 2^(-9.99) < 1/3. So Pr[output = s] > 2/3 for every
N, s with n >= 64; the finite branch succeeds with probability >=
1 - 2^(-10). QED.

## 10. Resources on every branch (n >= 64)

Sizes, from (1.1)-(1.3) and Section 8: q <= sqrt(n/2)+1;
log2 C0 <= (5/sqrt 2)·sqrt(n) + 12; log2 Wmax <= sqrt(n/2)+4;
log2 K <= 13 + log2(3.54 sqrt n + log2 n + 63) <= 21 + (1/2) log2 n;
runs <= 94; stages <= (J+1) + a2 <= 2n;
log2 Qcap <= 3.54 sqrt(n) + 32 + log2 n.

**Q.** On every branch Q <= Qcap, so log2 Q <= 3.54 sqrt(n) + 32 + log2 n
<= 4 sqrt(n) + 7 log2 n for all n >= 64 (the slack
0.46 sqrt(n) + 6 log2 n - 32 equals 7.7 at n = 64 and increases). So
Q = O(2^(4 sqrt n) n^7).

**S_Q.** Peak allocation: one active run's live qubits (current list <=
C0, next list <= C0/2, LE scratch <= 6n + O(1)), plus the pooled roots (K,
each measured immediately). So S_Q <= 2 C0 + K + 6n + O(1), and by (1.2)
and the size bounds, log2 S_Q <= (5/sqrt 2)·sqrt(n) + 14. This is at most
4 sqrt(n) + 4 log2 n for all n >= 64 (the slack
0.46 sqrt(n) + 4 log2 n - 14 equals 13.7 at n = 64 and increases). So
S_Q = O(2^(4 sqrt n) n^4).

**S_C.** Live classical data: the active run's list (<= C0 labels, stored
in 2n-bit fields: <= 2n C0 bits), the acquisition counter (O(sqrt n)
bits), decoder records (K roots x (log2 Wmax + 2) bits and K running
residues of <= n + sqrt(n/2) + 13 bits - by the size bounds this is
O(n^2)), LE classical scratch O(n^2), and the one-off setup (poly(n),
including the Section 4 table). The dominant term is 2n C0, so
log2 S_C <= (5/sqrt 2)·sqrt(n) + 14 + log2 n, which is at most
4 sqrt(n) + 4 log2 n for all n >= 64 (the slack
0.46 sqrt(n) + 3 log2 n - 14 equals 7.7 at n = 64 and increases). So
S_C = O(2^(4 sqrt n) n^4).

**T.** Four components; each is (operation count) x (per-operation cost
including its addressing surcharge <= log2(M_max + 2) <= 2 sqrt(2n) + 18).

(i) *Per acquisition* (at most Qcap of them): a transform O(n^2) plus LE
(c_E n^4 with internal surcharges included, Lemma 3.1) plus O(n^2)
bookkeeping; with the global surcharge factor, the acquisition component
is at most Qcap·2 c_E n^4·(2 sqrt(2n) + 19), so its log2 is at most
3.54 sqrt(n) + 32 + log2 n + 13 + 4 log2 n + 1 + 1.6 + log2 n
= 3.54 sqrt(n) + 5.5 log2 n + 48.6. For n >= 1024 this is below
4 sqrt(n) + 10 log2 n (slack 0.46 sqrt n + 4.5 log n - 48.6 = 6.8 at
n = 1024, increasing); for 64 <= n < 1024 the excess is at most
2^21 and is absorbed by the absolute constant of the O().

(ii) *Sieve*: one run does q+1 levels, each level O(C0) list operations
on (n+b)-bit keys with label arithmetic; the total operation count over
all runs and attempts is at most 2n·94·3·C0·(q+1) <= 2^(3.54 sqrt n +
2.5 log2 n + 11) (using q+1 <= sqrt(n/2)+2 and the size bounds), each
operation costing at most (n + b) + (2 sqrt(2n) + 18) <= 2n + 2.83 sqrt(n)
<= 3n bit steps (n >= 64, surcharge at allocation <= M_max). Component
log2 <= 3.54 sqrt n + 2.5 log2 n + 11 + 1.6 + log2 n <= 3.54 sqrt n +
3.5 log2 n + 13 - well inside 4 sqrt(n) + 10 log2 n (slack
0.46 sqrt n + 6.5 log2 n - 13 = 38 at n = 64, increasing).

(iii) *Decoder*: at most 2n stages, each with <= 2^(sqrt(n/2)+14)
candidates (Section 7) and K·O(n) residue updates with surcharges; per
stage log2 <= 0.5 log2 n + 14 + (21 + 0.5 log2 n) + 1 + log2 n + 2 <=
2 log2 n + 38.5, and 2n stages give log2 <= 3 log2 n + 39.5 - inside
4 sqrt(n) + 10 log2 n for all n >= 64.

(iv) *Setup*: poly(n), dominated by (ii).

Total: T = O(2^(4 sqrt n) n^10) with an absolute constant (the finite
64 <= n < 1024 shortfall of component (i) is absorbed). All four bounds
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
