# Ramp-then-cap collimation with linear-cost merges: DCP in 2^{(2577/1472) sqrt n} poly(n) work, O(n) qubits

## 0. Theorem and key idea

Theorem. Fix N >= 2 and s in Z_N; n = ceil(log2 N). Algorithm TC below (all parameters computed from N
by integer arithmetic) receives N and fresh copies of rho_s, outputs s with probability > 0.99, and on
EVERY branch uses, with absolute constants, for all n >= 1:
  T   = O(n^8 2^{(2577/1472) sqrt n}),   S_C = O(n^{3/2} 2^{(23/32) sqrt n}),   S_Q = O(n),
  Q   = O(n^3 2^{(2577/1472) sqrt n})          (2577/1472 = 32/23 + 23/64).
The growth indices of these envelopes are 1/2, 1/2, 0, 1/2. (Polynomial degrees are not optimised; Section 9
derives them.)

Key idea. A collimation sieve whose register width doubles per level while the number of cancelled bits grows
by one per level, until the width reaches a cap 2^{Rcap}, Rcap ~ (23/32) sqrt n; from then on the width stays
2^{Rcap} and each merge cancels Rcap - v bits (v = O(log n)). The ramp cancels about (23/32)^2 n/2 bits in about
(23/32) sqrt n levels, the capped part the rest in about (1 - (23/32)^2/2)(32/23) sqrt n levels, so the depth is
D ~ (32/23 + 23/64) sqrt n, while every register has at most 2^{Rcap} entries. Every register has an EXACT
power-of-two width: a merge keeps one full block of the measured fiber and fails otherwise, and the failure
probability is bounded for ANY label tables (Lemma 3), so no concentration argument is needed. This full-block
retention and its distribution-free bound, the width (23/32) sqrt n and the all-moduli pattern (integer labels,
an unused random top bit per copy, known-frequency estimation; Sections 5, 6, 8) are those of the public submission
QSR16 (Layr-Labs/dcp PR #100), whose merges enumerate all W1 W2 index pairs. Here a merge costs time LINEAR in the table lengths up to
polynomial factors in the word widths: the measured fiber is indexed bijectively through a classically sorted
order and table lookups (no QRAM, no enumeration of pairs). Every level then costs 2^{D + R0 + O(log n)}, so
T = 2^{D + O(log n)}. The estimator stores no table (Section 6), so classical memory stays 2^{Rcap} poly(n).
No concentration, anti-concentration or near-uniformity of list sizes or frequencies is needed: beyond the exact
fair-bit representation of Lemmas 7 and 8, the estimator's contrast needs only |supp c| >= 1, and |W| < q holds on
every odd-part branch, the only place where the estimator uses it (end of Section 5).

Gate set: X, CNOT, Toffoli, H, S, S^dagger, with each Toffoli counted as 15 gates of its exact Clifford+T
circuit (7 T/T^dagger, 6 CNOT, 2 H); computational-basis measurement; fresh |0>. No other rotation, no QFT
over Z_N, no QRAM.

## 1. Parameters

d = floor(log2 N) (so 2^d <= N < 2^{d+1}, d >= 1); N = 2^a M with M odd.
Widths. x = 23/32; R_x = isqrt((529 n - 1) // 1024) + 1 (= ceil(x sqrt n): R^2 >= ceil(529 n/1024) iff
1024 R^2 >= 529 n); Dmax = 4 isqrt(n) + 40; v = max(4, ceil(log2(16 (Dmax + 1)))); R0 = v + 2;
Rcap = max(R_x, 2v + 2); L = Rcap - R0 (>= v); R_j = min(R0 + j, Rcap) for j >= 0; eps = 2^{-v}, f0 = 2^v/(2^v - 1).
Per-level budgets: B_j = j + 1 for j < L and B_j = Rcap - v for j >= L; then B_j = 2 R_j - R_{j+1} - v for all j.
Schedule Sched(P), integer P >= 0. If P = 0: D = 0 and no merges. If P >= 1: D is the least D >= 1 with
B_0 + ... + B_{D-1} >= P; b_j = B_j for j <= D-2 and b_{D-1} = P - (B_0 + ... + B_{D-2}) (so 1 <= b_{D-1} <= B_{D-1},
sum_j b_j = P). m = 2^D R0.
Facts. (F1) Rcap - v >= Rcap/2 and Rcap - v >= v + 2 (as Rcap >= 2v + 2).
(F2) Let S = L(L+1)/2 and rc = Rcap - v. If P <= S then D <= L; if P > S then D = L + ceil((P - S)/rc) (the levels
j < L carry their full budgets j + 1, and only the last level may be partial). So in all cases, if P <= n,
D <= L + ceil(P/rc) <= L + ceil(2P/Rcap) <= L + (64/23) sqrt n + 1 (F1, and Rcap >= R_x >= x sqrt n). If Rcap = R_x then
L <= x sqrt n + 1 and D <= 3.51 sqrt n + 2; otherwise L = v and D <= v + 2.79 sqrt n + 1. In both cases D <= 4 sqrt n + 36
<= Dmax (isqrt(n) > sqrt n - 1), since v <= log2(32(Dmax + 1)) <= log2(32(4 sqrt n + 41)) <= 1.2 sqrt n + 35 for all n >= 1. Hence
16 (D + 1) <= 2^v <= max(16, 32(Dmax + 1)) <= 32(4 sqrt n + 41).
(F3) f0^D <= (1 - 1/(16(D+1)))^{-D} <= e^{D/(16D+15)} < e^{1/16} < 2.
(F4) Let n >= 1444 (sqrt n >= 38). The function x s - 2 log2(32(4s + 41)) - 2 is increasing for s >= 4 and positive at
s = 38, so R_x >= x sqrt n >= 2v + 2: Rcap = R_x <= x sqrt n + 1, L = rc - 2 with rc = Rcap - v, and t = v/(x sqrt n) < 1/2.
If D <= L then D <= x sqrt n. Otherwise D = L + ceil(E/rc) with E = P - L(L+1)/2 <= n - (rc - 2)^2/2, so
D < rc - 1 + n/rc - (rc - 2)^2/(2 rc) < rc/2 + n/rc + 1. As g/2 + n/g decreases for 0 < g < sqrt(2n) and
x sqrt n - v <= rc <= x sqrt n + 1 < sqrt(2n), using 1/(1-t) <= 1 + t + 2t^2:
D < (x sqrt n - v)/2 + n/(x sqrt n - v) + 1 <= (1/x + x/2) sqrt n + (1/x^2 - 1/2) v + 2v^2/(x^3 sqrt n) + 1,
with 1/x + x/2 = 2577/1472, 1/x^2 - 1/2 = 1519/1058, and 2v^2/(x^3 sqrt n) <= 2 log2(32(4 sqrt n + 41))^2/(x^3 sqrt n) <= 23
(decreasing in sqrt n >= 38). So 2^D <= 2^{24} (32(4 sqrt n + 41))^{1519/1058} 2^{(2577/1472) sqrt n} = O(n^{1519/2116} 2^{(2577/1472) sqrt n}).
For n < 1444 every parameter is bounded by an absolute constant.
D and m are non-decreasing in P; v, R0, Rcap depend on n only. D*, R0*, m* denote the values for
P* = max(n-1, 0) (R0* = R0); every tree below has P <= P*, hence D <= D*, m <= m*.
Word bound: Lambda = 2(n + D* + R0*) + 256.
Statistical parameters (defined for every N): q = 2 m*, Mgrid = 2^20 (q + 1),
hstat = ceil(log2(Mgrid + 1)) + ceil(log2(n + 7)) + 20, Kstat = 2^32 hstat, J = n + 4,
r_maj = 4 ceil(log2(n + 1)) + 41 (odd).
Odd part, used iff M > 1: P_o = d - 1, F = 2^{d-1}, f = 2^{d-1-a} (an integer: N >= 3 2^a gives d >= a + 1).
Two-adic part, used iff a >= 1. Initially r = 0 and u = 0.
Caps (Section 9): Q*, W*, Qcap = 2^11 Q*, Wcap = 2^11 W*. Label tests: H_lab = ceil(log2(Qcap + 2))
+ ceil(log2(n + 5)) + 14, F_lab = 512 H_lab. All are integers (or exact rationals) computed before the
first acquisition.

Lemma 0 (words). Every integer the algorithm stores (table entries, labels, W, z, counters, caps, records)
has absolute value < 2^Lambda; every product is formed in a 2 Lambda-bit scratch word.
Proof. Table entries are sums of at most m* labels < 2N: < 2^{n + 1 + D* + log2 R0*}. Write k = D* + R0*. From the
definitions above, n + 5, r_maj, hstat, H_lab and D* + 2 are < Lambda, m* <= 2^k, Mgrid <= 2^{k+22} and Kstat < 2^32 Lambda.
Hence Q* = 2 m* (2(n+5) Kstat + 2n r_maj) < 2^{k+35} Lambda^2 and R* = (n+5) Kstat + 2n r_maj < 2^{33} Lambda^2 (Section 9),
and, term by term in the formula for W* (Section 9): Q* c_copy < 2^{k+71} Lambda^7, the tree term < 2^{k+55} Lambda^7,
(n+5) c_est < 2^{k+84} Lambda^6 and c_set < 2^{20} Lambda^5, so W* < 2^{k+85} Lambda^7. Counters are at most
Wcap + (largest allowance) <= 2 Wcap, so log2(2 Wcap) < k + 97 + 7 log2 Lambda < Lambda (as 7 log2 Lambda <
159 + (Lambda - 256)/2 for Lambda >= 256 and Lambda - 256 = 2(n + k)).
The normalised fixed-point values of the decoder (Section 6) have 128 fractional bits and absolute value < 64 (by
the evaluation order given there); its integer operands (c^2 <= 239^2, Taylor denominators, iota' 2^128, C_iota,
S_iota) are below 2^Lambda. []

## 2. Source copies and labels

Let chi_k = N^{-1/2} sum_y e^{2 pi i k y/N} |y>. Writing |x> in this basis and averaging over x:
  rho_s = (1/N) sum_k |phi_{k,s}><phi_{k,s}| (x) |chi_k><chi_k|,  phi_{k,s} = (|0> + e^{-2 pi i k s/N}|1>)/sqrt2.
(Cross terms k != k' vanish because sum_x e^{-2 pi i (k-k') x/N} = 0.)

Lemma 1 (label extraction; the Kitaev test design follows RLQGR2/QSR16, the decoder is trig-free).
Let T_b: |y> -> |y + b mod N> for y < N, identity for N <= y < 2^n. T_b chi_k = e^{-2 pi i k b/N} chi_k.
Procedure on the data register of one copy: for j = 0..J run F_lab tests in the X basis and F_lab in the Y
basis. A test prepares |+> = H|0>, applies T_{-2^j mod N} controlled by it (P3), applies H (X basis) or
S^dagger then H (Y basis), measures (+1/-1) and resets the ancilla. Let x_j, y_j be the two means.
Quadrant decoder: c_j = 1/8, 3/8, 5/8, 7/8 for (x_j >= 0, y_j >= 0), (< 0, >= 0), (< 0, < 0), (>= 0, < 0).
Unwrap: g_J = c_J; for j = J-1..0, g_j = whichever of g_{j+1}/2 and (g_{j+1}+1)/2 is circularly closer to c_j
(tie: the first). Output k^ = round(N g_0) mod N (dyadic rationals with J + 3 bits; exact).
Claim: on input chi_k (with any spectator), k^ = k except w.p. <= 4(n+5) e^{-F_lab/512}; the eigenstate and
spectators are unchanged.
Proof. Conditioned on k the tests are i.i.d. with means cos(2 pi 2^j k/N) (X) and sin(2 pi 2^j k/N) (Y):
controlled T_{-2^j} maps |+>|chi_k> to (|0> + e^{2 pi i 2^j k/N}|1>)/sqrt2 |chi_k>. By Hoeffding each mean is
within 1/16 of its expectation except w.p. 2 e^{-F_lab/512}; union over 2(J+1) means. On that event, with
lambda_j = 2^j k/N mod 1, at most one of x_j, y_j has the wrong sign (|cos| and |sin| cannot both be < 1/16),
and a wrong sign forces lambda_j within arcsin(1/16)/(2 pi) < 0.01 of the axis on which the wrongly signed
coordinate vanishes (e.g. a wrong sign of x_j puts 2 pi lambda_j within arcsin(1/16) of +-pi/2); so c_j has
circular error e_dec <= 1/8 + 0.01 = 0.135. Unwrapping: if g_{j+1} has error e <= 0.135, one candidate is
within e/2 of lambda_j and the other is 1/2 away from that one; the right one is chosen because
e/2 + e_dec < 1/2 - e/2 - e_dec (0.405 < 1/2), and the error halves. So |g_0 - k/N|_circ <= 0.135 2^{-J}, and
N 0.135 2^{-n-4} < 1/2 gives k^ = k. Tests act on chi_k by phases only. []
With F_lab = 512 H_lab and at most Qcap calls, the union bound is <= 4(n+5) Qcap e^{-H_lab}
= 4(n+5) Qcap 2^{-H_lab} (2/e)^{H_lab} <= 2^{-12} (2/e)^{14} < 2^{-18} (as 2^{H_lab} >= 2^{14}(Qcap + 2)(n + 5) and H_lab >= 14).
Cost per copy: 2(J+1) F_lab tests, each a controlled modular addition (P3) plus at most 5 gates, so at most
1024 (n+5) H_lab (600(n+2) + 5) <= 2^{18} Lambda^2 H_lab gates and measurements; classically, the J + 1
constants -2^j mod N (by modular doubling), the 2(J+1) outcome counts, the decoder and the relabelling below
(one product and one division of Lambda-bit words) take at most 2^{13} Lambda^2 H_lab bit operations.

After extraction apply X to the control: it becomes q_k(s/N) = (|0> + e^{2 pi i k s/N}|1>)/sqrt2 up to a
global phase; the data register is reset. Ideal reference process: the same algorithm, running the same
tests at the same cost, but with each extraction's output k^ replaced by the true eigenlabel k (in the
analysis one may insert, at acquisition, the projective measurement {|chi_k><chi_k|} on the data register: it
leaves rho_s unchanged (rho_s is block diagonal in this basis), and every later operation on that register
(controlled T_b, then reset) is diagonal in the chi basis or discards the register, so the joint law of all
outcomes is unchanged; k is then a classical random variable, uniform on [0, N) and independent of the past).
Coupling the two processes (same
eigenlabels, test outcomes and later measurement outcomes), they agree, counters and outputs included, until
the first extraction whose output k^ differs from k. On every branch at most Qcap extractions happen, each
errs w.p. <= 4(n+5) e^{-F_lab/512} given the past, so the two runs coincide except w.p. < 2^{-18}. Sections 3-8 analyse the ideal
process: there each freshly acquired copy has a label uniform on [0, N) and independent of the history
before its acquisition.

Units (classical relabelling). For a known unit alpha mod N and an extracted label k put k' = alpha^{-1} k mod N.
Since k s == k' (alpha s) mod N, the qubit q_k(s/N) equals q_{k'}((alpha s mod N)/N): it is a copy with label k'
for the secret alpha s mod N, and k' is uniform on [0, N) and independent of the history when k is. No quantum
operation is needed.

## 3. Phase vectors and the merge

A register of width 2^R is a classical pair of integer tables (K_i, L_i), i in [0, 2^R), and the R-qubit
state 2^{-R/2} sum_i e^{2 pi i K_i theta} |i> up to a global phase.
Invariant (I): entry i corresponds to a binary incidence vector x^{(i)} over the copies used by the register;
distinct entries have distinct vectors; K_i = sum_j x_j k_j and L_i = sum_j x_j l_j as UNREDUCED integers,
where copy j carries its integer label k_j and its low part l_j (defined in Sections 6 and 8).
"P pinned bits" means all L_i are congruent modulo 2^P.
Leaf: R0 copies, qubit e holding q_{k_e}(theta); a register of width 2^{R0} with x^{(i)} = binary digits of i
(tables by doubling); 0 pinned bits.

Merge(A, B, P, b, W') with A = (K, L) of width W1 = 2^{R1}, B = (K', L') of width W2 = 2^{R2}, both with P pinned
bits, 1 <= b, W' = 2^{R'} <= W1 W2. Let c = L_0 mod 2^P, c' = L'_0 mod 2^P, rho(i) = ((L_i - c)/2^P) mod 2^b,
rho'(j) = ((L'_j - c')/2^P) mod 2^b (exact: L_i == c mod 2^P and 0 <= c <= L_i).
Classical preprocessing: stable sort of j by rho'(j) (ties by index j); pos(j) = rank of j; for each residue
sigma < 2^b, start(sigma) and size(sigma) of its block (start = 0 if empty).
Quantum steps on |i>|j> (lookups are P2; every table is defined on its whole address space, 0 at unused
addresses):
 (a) Look up rho(i) into a b-qubit register A and rho'(j) into a b-qubit register B; add B into A mod 2^b;
     MEASURE A, outcome y; clear B by the same lookup on j; reset A using y. The state is uniform over
     S_y = {(i,j): rho(i) + rho'(j) == y mod 2^b} with unchanged phases. Classically compute
     off(i) = sum_{i'<i} size(y - rho(i')) and G(i) = off(i) - start(y - rho(i)).
 (b) Look up pos(j) into a fresh register p of R1 + R2 qubits; look up pos^{-1}(p) (W2 entries) and XOR it into
     the j register, which becomes 0.
 (c) Look up G(i) (as a residue mod 2^{R1+R2}) into a scratch register, add it into p mod 2^{R1+R2}, clear the
     scratch by the same lookup. On S_y, p now holds idx(i,j) = off(i) + pos(j) - start(y - rho(i)), a
     bijection S_y -> [0, |S_y|) (for fixed i it maps the partners of i onto [off(i), off(i+1))).
 (d) MEASURE the top R1 + R2 - R' qubits of p, outcome beta. If (beta + 1) W' > |S_y| the merge FAILS (all its
     registers are measured and discarded). Otherwise reset the measured qubits using beta; the low R'
     qubits of p hold t = idx - beta W'.
 (e) Look up I_beta(t) = (the i of the pair with index beta W' + t) and XOR it into the i register:
     |i, t> -> |i XOR I_beta(t), t>, a permutation that clears i on the support.
Output: the register of width W' on the t qubits with K''_t = K_{i(t)} + K'_{j(t)}, L''_t = L_{i(t)} + L'_{j(t)},
P + b pinned bits (L_i + L'_j == c + c' + 2^P y mod 2^{P+b} on S_y). Each step is a permutation of basis states
or a computational-basis measurement, so the output state is exactly 2^{-R'/2} sum_t e^{2 pi i K''_t theta}|t>
up to a global phase, and (I) holds (an output entry is a pair of entries of registers on disjoint copies).

Lemma 2 (cost of a scheduled merge). For R1 = R2 = R, R' in {R, R + 1} and b <= R - 1 (all merges of Section 4),
one attempt uses at most 2^{R+13} (R + 1) quantum gates and measurements, at most 2^{R+9} Lambda^2 classical
bit operations, O(R) scratch qubits and at most 2^{R+6} Lambda classical bits.
Proof. Eight lookups (three in (a), two in (b), two in (c), one in (e)), each over at most 2^{R+1} entries with
index width <= 2R and data width <= 2R + 1: by P2 at most 2^{R+1}(128 R + 2R + 1) gates each, total
<= 2^{R+12}(R + 1); two adders of width <= 2R (P3), at most 4R measurements and resets, and at most 64(R + 1)
operations to initialise scratch and, on failure, to measure and discard all registers. Classically:
sort 2^R keys of <= 2R bits (P3), the arrays start, size (2^b <= 2^R entries), pos, pos^{-1}, off, G (prefix sums
of Lambda-bit numbers), I_beta and the output tables (scan r = beta W', ..., (beta + 1) W' - 1 in order, keeping the i
with off(i) <= r < off(i) + size(y - rho(i)), skipping empty intervals, and setting j = pos^{-1}(start(y - rho(i)) + r - off(i));
only the retained block is visited, with two Lambda-bit additions per output entry): each O(Lambda) bit operations per entry, at most 2^{R+9} Lambda^2 in total. []

Lemma 3 (distribution-free yield). For ANY tables, Pr[merge fails] < 2^b W'/(W1 W2).
Proof. Magnitudes are uniform, so y has probability |S_y|/(W1 W2), and given y the value idx is uniform on
[0, |S_y|). Failure means idx falls in the last, partial block, of size |S_y| mod W' < W'.
Hence Pr[fail] = sum_y (|S_y| mod W')/(W1 W2) < 2^b W'/(W1 W2). []

## 4. The ramp-then-cap tree

Tree(P): a level-0 node is a leaf; a level-(j+1) node runs Merge(A, B, P_j, b_j, 2^{R_{j+1}}) on two
independently built level-j nodes, P_j = b_0 + ... + b_{j-1}; on failure it builds two fresh level-j nodes and
retries. Evaluation is depth-first. The root node has level D, width 2^{R_D} and exactly P pinned bits.
Since b_j <= B_j = 2R_j - R_{j+1} - v (so also b_j <= R_j - 1), Lemma 3 gives failure
< 2^{b_j + R_{j+1} - 2R_j} <= 2^{-v} = eps for every attempt, conditioned on any history.

Lemma 4 (expected counts). In one Tree(P), the expected number of leaves built is <= (2 f0)^D, the expected
number of copies used is <= f0^D m < 2m, and the expected number of merge attempts at child level j is
<= 2^{D-j-1} f0^{D-j} < 2^{D-j}.
Proof. A level-(j+1) node makes A >= 1 attempts, each with two fresh level-j children, and each attempt
succeeds w.p. >= 1 - eps given the past, so E A <= f0; each attempt builds its children from fresh copies, so the
cost of an attempt is independent of the earlier attempts and Wald's identity gives the counts recursively. []

Lemma 5 (space). Depth-first evaluation holds at most one finished register per level. At any time the
qubits in use are: held registers, sum_{j<D} R_j <= D R0 + sum_{j<min(D,L)} j + (D - L)^+ Rcap <= D* R0 + P + 2P + Rcap
(every full level j < L cancels j + 1 bits and every full level j >= L cancels Rcap - v >= Rcap/2 bits; the one possible
partial last level is charged the extra Rcap), i.e. <= D* R0 + 3n + Rcap; and either one merge
(two inputs, p, A, B, lookup data and flag ancillas: <= 12 R_D qubits) or one leaf under assembly (<= R0 held
copies) plus one copy under extraction (control, n data qubits, one test ancilla and the P3 scratch of a
controlled modular addition, at most 4n + 12 qubits); plus O(1) qubits of a root. So S_Q <= 7n + D* R0 + 13 Rcap + 16 = O(n)
(D* R0 = O(sqrt n log n), Rcap = O(sqrt n)).
Classically: held tables <= sum_{j<D} 2^{R_j+1} Lambda <= (D + 2) 2^{Rcap+1} Lambda bits, merge tables <= 2^{Rcap+6} Lambda.

Lemma 6 (structural transcript). Fix a tree and condition on the history H before it starts. Realise the
ideal process from the following independent ingredients.
 (i) Accepted labels. The tree's copies are the successive outputs k_1, k_2, ... of its source calls (each
     call's output after its rejections). Given H they are i.i.d. with the source's law (Sections 6 and 8):
     k_i = l_i + F' T_i + 2F' h_i with T_i a fair bit independent of (l_i, h_i).
 (ii) Rejection record G: the number of rejected trials of each source call and their labels. Given H, G is
     independent of the accepted labels (odd part: a trial is accepted iff bit d of its label is 0, i.e.
     k < 2^d, never reading T = bit d-1; this happens w.p. 2^d/N whatever happened before, and an accepted
     label is uniform on [0, 2^d); the two-adic source rejects nothing, so G is empty there).
 (iii) Measurement randomness. U_1, U_2, ... i.i.d. uniform on [0, 1): the e-th computational-basis
     measurement of the tree (residues y, blocks beta, the root index t, in time order) returns the outcome
     obtained from U_e by inverse-CDF sampling of its conditional law given the past. (Measurements whose
     outcomes are discarded unread, as on a merge failure, are omitted.)
The tree's structural transcript consists of the low parts l_i of its copies, G, the outcomes of these
measurements, and all classical choices (which copies enter which leaf, residues, sorting with ties by index,
block tests, retries, pairings, the final entries x, y). It EXCLUDES the extraction tests' outcomes, the K
tables, Delta, W and the root qubit's outcome Z.
Claim: the conditional law of each such measurement, given H, ALL labels and the earlier transcript, is a
function of the L tables and the earlier transcript only. Hence (iii) realises the correct joint law, and the
transcript is a deterministic function of (H, (l_i), G, (U_e)).
Proof. Before the root qubit is measured, every register has uniform magnitudes on an index set defined by L
tables (Section 3), and each of these measurements is a computational-basis measurement of a function of the
index registers. Its outcome probabilities are therefore ratios of sizes of sets defined by L tables (as in
Lemma 3), whatever the phases. Every classical choice reads only L tables and earlier outcomes; induct over
the steps. The ideal process never reads its extraction tests' outcomes (it uses the true label, and the
tests leave the copy's qubit q_k(theta) unchanged), so leaving them out does not change the joint law of the
labels and the transcript. []
What each decision reads (all from the structural transcript; none reads T, h, K, W or Z):
  acceptance of a copy ............ bit d of its label (odd part only; recorded in G)
  leaf composition ................ the order of acceptance
  residues rho, rho' .............. L tables and P
  sort order, pos, start, size .... rho' (ties by index)
  measured residue y .............. law: |S_y|/(W1 W2), a function of rho, rho'
  off, G .......................... rho, y, sizes
  block beta, failure test ........ law: uniform idx on [0, |S_y|); test reads |S_y|
  retry ........................... the failure test
  root index t .................... law: uniform on [0, W_D/2)
  root entries x = 2t, y = 2t + 1 . t
  caps, aborts .................... absent in the uncapped process U analysed here (Section 9); in the capped
                                    process the counters are H plus fixed allowances of the tree's blocks

## 5. Root and the unused top bits

Root(P): build Tree(P), MEASURE the top R_D - 1 qubits of the root register (outcome t, uniform). The
remaining qubit is (e^{2 pi i K_x theta}|0> + e^{2 pi i K_y theta}|1>)/sqrt2 for the entries x = 2t, y = 2t + 1,
i.e. q_Delta(theta) with Delta = K_y - K_x up to a global phase. W_D is even, so the root never fails.

Labels in the analysis (Sections 6 and 8 instantiate this): every copy used by a tree has an integer label
k = l + F' T + 2F' h with 0 <= l < F' = 2^P, T in {0,1}, h >= 0; the tree uses only l (the stream of Lemma 6).

Lemma 7 (top bits). In the uncapped ideal process U (the capped algorithm is reached through the couplings of Section 9):
conditioned on H, the tree's structural transcript and all l's and h's of the copies acquired by its source calls
(including rejected ones), the top bits T of the copies in the final tree are i.i.d. fair bits.
Proof. Given H, the stream (T_i) is i.i.d. fair and independent of ((l_i), (h_i), G, (U_e)) (Lemma 6 (i)-(iii)).
By Lemma 6 the index set I of the copies in the final tree is a function of (H, (l_i), G, (U_e)). Conditioning
on ((l_i), (h_i), G, (U_e)) fixes I and leaves (T_i) i.i.d. fair, so (T_i)_{i in I} is i.i.d. fair given these.
I is a function of the transcript, so the same holds given the coarser
information (transcript, l's, h's). []

Lemma 8 (root frequency). Let c = x^{(y)} - x^{(x)} in {-1,0,1}^m (nonzero by (I)) and h = |supp c| >= 1.
Then Delta = F' W with the integer W = De + sum_j c_j T_j + 2 sum_j c_j h_j, where De = (L_y - L_x)/F' is an
integer (P pinned bits). Conditioned as in Lemma 7, W minus a known integer equals sum_{supp c} c_j T_j, so
 (i) W mod 2 is a fair bit, and
 (ii) E e^{2 pi i W delta} = e^{2 pi i mu delta} cos(pi delta)^h for a real mu fixed by the conditioning and
     every real delta.
Proof. Expand Delta = sum c_j k_j. (i): sum_{supp c} T_j has fair parity. (ii): E e^{2 pi i c_j T_j delta}
= e^{pi i c_j delta} cos(pi delta) for c_j = +-1, and independence (Lemma 7). []
In the odd part every k_j < 2F', so |W| = |Delta|/F' < 2m <= q.

## 6. Odd part: r = s mod M (only if M > 1)

For stage j = 0..J let alpha_j be the unit with alpha_j == 2^j mod M and alpha_j == 1 mod 2^a (CRT by
extended Euclid), and compute alpha_j^{-1} mod N. Stage source: acquire a copy, extract its label, relabel it
to k = alpha_j^{-1} (label) mod N (Section 2); if k >= 2^d discard the copy and repeat (success probability
2^d/N > 1/2); otherwise l = k mod F, T = k >> (d-1), h = 0. A kept label is uniform
on [0, 2F), so l and T are independent and T is fair (P = P_o, F' = F).
Each stage collects Kstat records: Root(P_o) on the stage source, W = Delta/F (exact division), a fresh fair
coin (measure H|0>) chooses the basis, measure X (H, then Z) or Y (S^dagger, H, then Z), record (W, basis, Z). The root qubit
is q_{FW}(theta_j) with theta_j = (alpha_j s mod N)/N, i.e. its phase is W phi_j with
phi_j = F alpha_j s/N mod 1 = f (alpha_j s mod M)/M mod 1 = 2^j vartheta, vartheta = f r/M mod 1.

Lemma 9 (known-frequency scores). For a record and u in [0,1) let S_u = 2Z cos(2 pi W u) (X) or 2Z sin(2 pi W u) (Y).
 (a) E[S_u | W] = cos(2 pi W (phi - u)); for the grid point u0 = k0/Mgrid nearest to phi, E S_{u0} >= 1 - 2^{-37}
     (|W| < q gives |2 pi W (phi - u0)| < pi/2^20).
 (b) If the circular distance of u from phi is >= 1/32, then E S_u <= cos(pi/32) <= 1 - 1/512.
Proof. (a) averaging the basis coin. (b) Lemma 8(ii) with delta the representative of phi - u in (-1/2, 1/2]:
E S_u = E[cos(2 pi mu delta) cos(pi delta)^h] <= cos(pi delta) <= cos(pi/32), since 0 <= cos(pi delta) <= 1 and
h >= 1; 1 - cos(pi/32) = 2 sin^2(pi/64) >= 2 (1/32)^2 = 1/512 (sin x >= 2x/pi on [0, pi/2]). []

Decoder. For iota in [0, Mgrid), integers C_iota, S_iota with |C_iota - 2^30 cos(2 pi iota/Mgrid)| <= 1 and
|S_iota - 2^30 sin(2 pi iota/Mgrid)| <= 1, computed on demand (no table is stored) as follows. Octant reduction: A = Mgrid/8 (an integer),
o = floor(8 iota/Mgrid) (by comparisons of 8 iota with multiples of Mgrid), r = iota - o A, iota' = r for even o and
A - r for odd o; with (c, s) = (cos x, sin x), x = 2 pi iota'/Mgrid in [0, pi/4], the pair (cos, sin)(2 pi iota/Mgrid) is
(c, s), (s, c), (-s, c), (-c, s), (-c, -s), (-s, -c), (s, -c), (c, -s) for o = 0, ..., 7. Fixed-point values carry 128 fractional bits; every multiplication or division by an
integer or fixed-point value is rounded down (error <= 2^{-128} each); no factorial is stored.
 - pi^ = 16 A_5 - 4 A_239, A_c = sum_{k<40} (-1)^k p_k/(2k+1) with p_0 = 1/c, p_{k+1} = p_k/c^2 (all terms <= 1).
   Truncation < 2^{-190}; each p_k has error <= 2^{-127} and each term <= 2^{-126}, so |pi^ - pi| <= 20 * 40 * 2^{-126} + 2^{-188} < 2^{-115}.
 - y = iota'/Mgrid (one division, y in [0, 1/8]); x = 2 pi^ y in [0, pi/4 + 2^{-114}]; error of x <= 2^{-113}; x2 = x^2,
   error <= 2^{-111}.
 - cos: t_0 = 1, t_{k+1} = t_k x2/((2k+1)(2k+2)); sin: t_0 = x, t_{k+1} = t_k x2/((2k+2)(2k+3)); 24 terms with
   alternating signs. All t_k <= 1. The error e_k of t_k obeys e_{k+1} <= e_k/2 + 2^{-111} + 2^{-127}, so e_k < 2^{-109},
   and each sum has rounding error < 24 * 2^{-109} < 2^{-104}; truncation < 2^{-219}; the error of x adds <= 2^{-113}.
 - C_iota = round(2^30 cos^), S_iota = round(2^30 sin^): error <= 1/2 + 2^{30} 2^{-103} = 1/2 + 2^{-73}.
Every normalised fixed-point value has absolute value < 64. Cost per entry: 8 comparisons and one division of
<= 2 Lambda-bit words and <= 1024 operations (pi^ included) on <= 400-bit words, each <= 8 * 400^2 bit operations:
<= 2^{28} Lambda^2 bit operations in total (Lambda >= 256).
For each grid index k in increasing order compute Sigma_k = sum over the Kstat stored records of 2Z C_iota (X)
or 2Z S_iota (Y) with iota = (W k) mod Mgrid (kept per record and updated by adding W mod Mgrid as k increases),
computing each C_iota or S_iota on demand; keep only the best pair (k*, Sigma_{k*}) so far, replacing it only on
a strict increase. Output u^ = k*/Mgrid for the least maximiser k*. Sigma_k/(2^30 Kstat) differs from the empirical mean of S_{k/Mgrid} by <= 2^{-29}.
Lemma 10. In the uncapped ideal process U, within a stage the records are i.i.d. with S_u in [-2, 2] (fresh
copies and coins; a stage's trees do not depend on its earlier records). By Hoeffding
(Pr[|mean - E| >= t] <= 2 e^{-K t^2/8} for K independent values in [-2, 2]), the empirical means of S_u for all
Mgrid grid points and all J + 1 stages are within 2^{-13} of their expectations except w.p.
2 (J+1) Mgrid e^{-Kstat 2^{-29}} = 2 (n+5) Mgrid e^{-8 hstat} < 2^{-150}. On this event the nearest grid point has
normalised score >= 1 - 2^{-37} - 2^{-13} - 2^{-29} and every point at distance >= 1/32 has <= 1 - 2^{-9} + 2^{-13}
+ 2^{-29}, which is smaller; so |u^ - phi_j|_circ < 1/32 in every stage. []
Unwrapping (as in Lemma 1 with e_dec = 1/32, which satisfies e + 2 e_dec < 1/2): G_J = u^_J; G_j = the closer of
G_{j+1}/2 and (G_{j+1}+1)/2 to u^_j; then |G_0 - vartheta|_circ < 2^{-J}/32 = 2^{-n-9}, so round(M G_0) mod M = f r mod M
(M <= 2^n), and r = (f r) f^{-1} mod M.

## 7. (reserved)

## 8. Two-adic part: s = r + M u, u in [0, 2^a) (only if a >= 1)

For level l = 0..a-1 the low l bits t_low of u have been set; w = a - l, P = w - 1, s0 = r + M t_low. If r and
t_low are correct then s - s0 = M 2^l u' with u' = u >> l. Source: acquire a copy, extract k (no unit, no
rejection); low part k mod 2^{w-1}, T = bit w-1 of k, h = k >> w; these are independent and T is fair because
2^w | N (F' = 2^{w-1}). Repeat Root(P): it gives the qubit with phase Delta s/N = Delta s0/N + Delta u'/2^w and
Delta = 2^{w-1} W (Lemma 8). If W is even, measure and discard the qubit. If W is odd, Delta u'/2^w == u'/2 ==
u'_0/2 mod 1, where u'_0 is bit l of u, so the phase is gamma + u'_0/2 with gamma = z/N, z = Delta s0 mod N.
Vote: o = floor(8z/N). If o in {0,3,4,7} measure X and let sigma = +1 for o in {0,7}, -1 for o in {3,4};
otherwise measure Y and let sigma = +1 for o in {1,2}, -1 for o in {5,6}. The vote is 0 if Z sigma = +1, else 1.
Stop after r_maj odd-W roots; set bit l of u to the majority vote.
Lemma 11. In U, suppose r and bits 0..l-1 of u are correct. Conditioned on everything before a vote (including
its gamma), the vote equals u'_0 w.p. (1 + |g|)/2 >= (1 + 2^{-1/2})/2 > 0.853, where g = cos(2 pi gamma) (X) or
sin(2 pi gamma) (Y), and |g| >= 2^{-1/2} on the chosen octants. Hence the number of correct votes among the
r_maj counted ones stochastically dominates Binomial(r_maj, 0.853), and by Hoeffding the level errs w.p.
<= e^{-2 r_maj 0.353^2} <= e^{-0.249 r_maj}. Bounding the first wrong level: in total <= n e^{-0.249 r_maj} < 2^{-14}.
Output s = r + M u. []

## 9. Accounting, caps and failure budget

Per-operation charge. Allocated bits and qubits S <= 2^{D* + R0* + 36} Lambda^2 at all times (every register has
width <= 2^{R_{D*}} <= 2^{D* + R0*}; Lemma 5, records
Kstat (2 Lambda + 2) bits for the records and their running iota, Mgrid <= 2^{22} m*), so each gate, measurement,
reset, classical bit operation or indexed access (at most three addresses) costs at most 1 + 3 ceil(log2(S + 2))
<= 2 Lambda.
Blocks and allowances. Each allowance bounds the charged cost of its block, including address charges, the
accumulator update and comparison below, and the generation of every gate by the controller. Gates are
streamed, never stored: the controller emits a gate as its type and at most three qubit addresses, computed
from loop counters and the table entry being read in at most 8 Lambda bit operations, each charged <= 2 Lambda.
So one gate costs at most 2 Lambda + 16 Lambda^2 <= 18 Lambda^2 in total; this is why the allowances carry Lambda^4.
  copy (acquire n+1, extraction Lemma 1, relabel, reset):       c_copy = 2^36 Lambda^4 H_lab,
  leaf (tables of one leaf from held copies):                  c_leaf = 2^20 Lambda^4 2^{R0},
  merge attempt at child level j (Lemma 2):                    c_j    = 2^20 Lambda^4 2^{R_{j+1}},
  root (index measurement, W, record or vote, z, octant):      c_root = 2^20 Lambda^4,
  decoder stage (Kstat Mgrid on-demand entries and updates):  c_est  = 2^30 Lambda^4 Mgrid Kstat,
  setup and finish (parameters, CRT, units and inverses,
    f^{-1} mod M, unwrapping, output):                          c_set  = 2^20 Lambda^4 (n + 5),
  cleanup (release everything):                                c_cl   = 2^37 Lambda^3 2^{D* + R0*} (>= 2 Lambda S).
(Check: a merge attempt has <= 2^{R_j+14} Lambda gates (Lemma 2), at <= 18 Lambda^2 each, plus <= 2^{R_j+9} Lambda^2
bit operations at <= 2 Lambda each: <= 2^{R_j+19} Lambda^3 + 2^{R_j+10} Lambda^3 <= c_j. A copy has <= 2^{18} Lambda^2 H_lab
gates and <= 2^{13} Lambda^2 H_lab bit operations (Lemma 1), plus n + 1 for the acquisition: <= 2^{24} Lambda^4 H_lab.
A root needs O(1) products of 2 Lambda-bit words. A decoder stage needs Mgrid Kstat on-demand entries of
<= 2^{28} Lambda^2 bit operations each (Section 6) and <= 32 Lambda per score update:
<= 2^{29} Lambda^3 Mgrid Kstat + 64 Lambda^2 Mgrid Kstat <= c_est. Setup: each extended Euclid on words < 2^Lambda takes
<= 2 Lambda division steps of <= 16 Lambda^2 bit operations, so <= 2^6 Lambda^4 charged per Euclid and O(1) Euclids
and products per stage. Parameters: isqrt by binary search (<= Lambda steps), v as the least v >= 4 with
2^v >= 16(Dmax+1), D by summing the budgets B_j while the sum is < P (<= n steps), ceil(log2 .) by bit lengths,
the caps as O(1) products: O(n) word operations of <= 16 Lambda^2 bit operations each. Unwrapping is O(J) word operations. All within c_set. Bookkeeping: the recursion and retry control of a merge
attempt (O(1) counters of <= Lambda bits) is inside c_j; per two-adic level the update of s0, the schedule and the
majority count (O(1) word operations; n levels) are inside c_set; the basis coin and vote of a root are inside c_root.)
Control: the controller first runs the setup (deterministic, charged cost <= c_set; it computes all parameters,
caps and units) and sets A = c_set, which also reserves the finish (unwrapping, CRT, output). Afterwards, before
a block starts, it adds the block's allowance to the accumulator A and, before an acquisition, 1 to a copy
counter; if A > Wcap or the counter > Qcap it runs cleanup and outputs 0. (c_set <= W* < Wcap, so setup never
aborts. The uncapped process U of the analysis uses mathematical counters; Lemma 0 concerns the algorithm.)
So on every branch Q <= Qcap and T <= Wcap + max allowance + c_cl.
Expected allowance in the uncapped ideal process U. Let R* = (n + 5) Kstat + 2 n r_maj (expected roots:
(n + 5) Kstat in the odd part, 2 r_maj per two-adic level since W is odd w.p. 1/2). By Lemma 4 and F3
  Q* = 2 m* (2 (n+5) Kstat + 2 n r_maj)   (< 2 expected acquisitions per kept odd-part copy),
  W* = Q* c_copy + R* (2^{21} Lambda^4 (D* + 2) 2^{D* + R0*} + c_root) + (n + 5) c_est + c_set,
since by Lemma 4 one tree's expected allowance is <= sum_{j<D} 2^{D-j} c_j + 2^{D+1} c_leaf, where for j < L
2^{D-j} c_j = 2^{20} Lambda^4 2^{D+R0+1}, for j >= L the terms 2^{D-j} 2^{20} Lambda^4 2^{Rcap} sum to < 2^{20} Lambda^4 2^{D-L+Rcap+1}
= 2^{20} Lambda^4 2^{D+R0+1}, and 2^{D+1} c_leaf = 2^{20} Lambda^4 2^{D+R0+1}: in total <= 2^{21} Lambda^4 (D + 2) 2^{D+R0},
increasing in D (for D = 0: one leaf, c_leaf).
Hence E_U[A] <= W* and E_U[copies] <= Q*.
Asymptotics (F4): for n >= 1444, 2^{D*} = O(n^{1519/2116} 2^{(2577/1472) sqrt n}), 2^{R0*} = 4 2^v <= 128 (Dmax + 1) = O(sqrt n),
2^{Rcap} <= 2 2^{(23/32) sqrt n}, D* = O(sqrt n), Lambda = O(n), log2 Mgrid = D* + O(log n), hstat, Kstat, H_lab = O(sqrt n). So
  Q   <= Qcap = O(m* n Kstat) = O(n^{3/2 + 1519/2116} log n 2^{(2577/1472) sqrt n}) = O(n^3 2^{(2577/1472) sqrt n}),
  T   = O(Q* Lambda^4 H_lab + n Kstat Lambda^4 D* 2^{D* + R0*} + n Lambda^4 Mgrid Kstat)
      = O(n^{6 + 1519/2116} log n + n^{13/2 + 1519/2116} + n^{11/2 + 1519/2116} log n) 2^{(2577/1472) sqrt n} = O(n^8 2^{(2577/1472) sqrt n}),
  S_C = O(Lambda D* 2^{Rcap} + Kstat Lambda) = O(n^{3/2} 2^{(23/32) sqrt n}),   S_Q = O(n) (Lemma 5).
For n < 1444 all quantities are bounded by absolute constants. (Asymptotically, the dominant term of this universal bound is the odd-part tree term.)
Failure budget. U never aborts; the capped ideal process coincides with U until U's accumulator or copy
counter first exceeds its cap, so Pr[capped ideal fails] <= Pr[U fails] + Pr[A_U > Wcap] + Pr[copies_U > Qcap].
(This also removes any dependence of the abort decision on the top bits, e.g. through the number of two-adic
roots.) In U: odd part < 2^{-150} (Lemma 10), two-adic part < 2^{-14} (Lemma 11); Markov gives each cap
probability <= 2^{-11}. The actual algorithm differs from the capped ideal process w.p. < 2^{-18} (Lemma 1).
Total < 2^{-9}: success > 0.99.

## Appendix P: primitive circuits (exact, gate set of Section 0)
P1 (equality flag). flag ^= [x == e] for an l-qubit x and classical e: X on the zero bits of e, an AND of l qubits
by l - 1 Toffolis into l - 1 ancillas, CNOT to the flag, uncompute: <= 30(l - 1) + 2l + 1 <= 32 l gates.
P2 (lookup). For a classical table tau: [0, E) -> {0,1}^w, |x>|z> -> |x>|z XOR tau(x)> (identity for x >= E) is the
product over e < E of: P1 for e into a flag, CNOTs from the flag to the 1-bits of tau(e), P1 again. Cost
<= E (64 l + w) gates, l ancillas; an involution. Its emission reads each table entry once.
P3 (arithmetic, w-bit words). Ripple-carry addition mod 2^w (Cuccaro et al.): <= 40w gates, one ancilla.
Comparator g ^= [y < c] with a classical c: load c into a w-bit scratch by X gates, carry chain of the
subtraction y - c with one borrow ancilla, copy the borrow to g, uncompute, unload: <= 80 w gates.
Controlled modular addition y -> y + c mod N of a classical c < N on an n-bit y, controlled by a qubit ctrl,
identity when y >= N or ctrl = 0. Work on Y = (y, 0) with w = n + 1 bits, a w-bit scratch and flags g, h, t, e:
  1. g ^= [Y < N];  2. h ^= ctrl AND g;  3. load c into the scratch controlled by h, add it into Y, unload
  (now Y = y + c < 2N if h = 1);  4. e ^= [Y < N], t ^= h AND (NOT e), e ^= [Y < N];  5. load N controlled by t,
  subtract it from Y, unload (now Y = y + c - tN < N);  6. e ^= [Y < c], t ^= h AND e, e ^= [Y < c] (this clears t:
  if h = 1, t = 1 iff y + c >= N iff the new Y < c);  7. h ^= ctrl AND g (clears h; g is unchanged);
  8. g ^= [Y < N] (clears g: a valid y stays < N, an invalid y is untouched).
  Count: 6 comparators, 2 adders, 4 w controlled loads, 4 Toffolis and 2 X: <= 564 w + 70 <= 600 (n + 2) gates;
  ancillas <= 2n + 8.
Classical: w-bit addition/comparison <= 4w, multiplication/division <= 8w^2 bit operations; merge sort of E
records of w bits <= 4 E ceil(log2 E) w bit operations.
