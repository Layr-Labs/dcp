# Depth-first phase-vector collimation with O(n) qubits

This file proves all five claims of `submission.json` for **one** algorithm,
called **PVSieve** below. PVSieve is a depth-first collimation sieve on phase
vectors, in the line of O. Regev ("A subexponential time algorithm for the
dihedral hidden subgroup problem with polynomial space", arXiv:quant-ph/0406151)
and G. Kuperberg ("Another subexponential-time quantum algorithm for the
dihedral hidden subgroup problem", TQC 2013, arXiv:1112.3333, Algorithm 4.4 and
Proposition 4.5). Both papers present their algorithms for N = 2^n. This file
gives a complete proof for **every** N in this challenge's cost model, with
explicit constants. No novelty of the growth rates is claimed. The new
ingredients are in the proof:

- labels are exact integers. Collimation only ever cancels **low** bits, and the
  probability analysis does not depend on how the labels are distributed
  (Lemma 4.2);
- the single fact that needs a distribution is a **held-out parity**: bit j of
  the leaf labels is never used by any decision. Each output qubit therefore has
  label 2^j w with w odd, with probability exactly 1/2 (Lemma 5.1);
- labels 2^j w with odd but large known w are read off with an
  **odd-multiplier top-down decoder** started from 2^{O(sqrt n)} anchors, and
  the candidates are then verified (Section 6);
- all gates are exact Clifford+T (H, S, T, X, CNOT, Toffoli). No gate synthesis
  is used.

All logarithms are base 2. n = ceil(log N), so 2^{n-1} < N <= 2^n. Write
omega = e^{2 pi i/N}, theta = s/N, and for an integer K let

$$
|\psi_K\rangle=\tfrac{1}{\sqrt2}\bigl(|0\rangle+\omega^{Ks}|1\rangle\bigr).
$$

The proved bounds are:

$$
T=O\!\left(2^{\frac{17}{3}\sqrt n}n^{5/2}\log n\right),\
S_C=O\!\left(2^{\frac32\sqrt n}n^{3/2}\right),\
S_Q=O(n),\
Q=O\!\left(2^{\frac83\sqrt n}n^{3/2}\log n\right).
$$

Their UI indices are 1/2, 1/2, 0 and 1/2.

## 1. Parameters

For n <= 15, PVSieve runs exhaustive shift testing: for t = 0, ..., N-1 it
runs n+6 shift tests (7.3) and outputs the first t that passes all of them, or 0
if none passes. A wrong output has probability <= (N-1) 2^{-(n+6)} < 1/64, so
success is > 63/64. This branch uses at most N(n+6) <= 21 * 2^15 copies and
constant work and space. From here on n >= 16. PVSieve computes:

1. l_c = ceil((3/2) sqrt n), the least integer with 4 l_c^2 >= 9n. Then
   (3/2) sqrt n <= l_c < (3/2) sqrt n + 1.
2. p = l_c + 2 and l_0 = 2^p. l_0 is the length of every phase vector, and p is
   the number of qubits that store one.
3. The levels used are j in {0, 1, ..., n-3}.
4. For level j: D_j = ceil(j/l_c) (so D_0 = 0 and the list below is empty for j = 0), with bit counts g_{j,1} = ... =
   g_{j,D_j-1} = l_c and g_{j,D_j} = j - (D_j - 1) l_c, each in [1, l_c].
   G_{j,i} = g_{j,1} + ... + g_{j,i}, and G_{j,0} = 0, so G_{j,D_j} = j.
   D_max := ceil((n-3)/l_c) <= n/l_c + 1 <= (2/3) sqrt n + 1.
5. A = 8, the attempts per node. r = 200(ceil(log n) + 10). Each level makes
   4r final attempts.
6. lambda = D_max + ceil(log p) + 5 and Lambda = 2^lambda >= 32 p 2^{D_max},
   the anchors. k_v = lambda + 8.
7. Q_max = (n-2) * 4r * 16^{D_max} * 8p + Lambda k_v. V = the bit length of
   Q_max. r_FS = 200(V + ceil(log n) + 10).

## 2. Exact primitives

**2.1 Controlled modular addition of a classical constant.** For a in [0,N),
let f_a(y) = (y+a) mod N for y < N and f_a(y) = y for N <= y < 2^n. This is a
permutation with inverse f_{(N-a) mod N}. Explicit circuit:

- *Ripple primitives with a classical constant b (n+1 bits).* Addition y+b:
  keep carries in fresh ancillas c_1..c_{n+1}. The carry rule is
  c_{i+1} = y_i AND c_i if b_i = 0, and y_i OR c_i = NOT(NOT y_i AND NOT c_i) if
  b_i = 1. Each is one Toffoli plus O(1) X/CNOT. Sum bits are y_i xor b_i xor c_i
  (CNOTs and X). Comparison [u >= b] is the final borrow of u - b, computed the
  same way. Each primitive uses O(n) gates and O(n) ancillas, and its scratch is
  reversible.
- *Out-of-place evaluation E_a: |y>|z> -> |y>|z xor f_a(y)>.* Compute in fresh
  scratch:
  - v = [y >= N];
  - u = y + a (n+1 bits);
  - g = [u >= N];
  - u'' = u - N into a fresh (n+1)-bit register: a ripple subtraction of the
    classical constant N, by the rule above. Then u' = g ? u'' : u, selected
    bit by bit with one Toffoli pair per bit, so no constant is quantum;
  - the multiplexed value v ? y : u', bit by bit with one Toffoli pair per bit.

  CNOT that value into z, then run the scratch gates in reverse (Bennett), which
  returns all scratch to |0>. Cost: O(n) gates and O(n) ancillas.
- *Controlled in-place map on control qubit q.* Run E_a with the final copy
  CNOTs replaced by Toffolis controlled on q. That gives
  |y,0> -> |y, q f_a(y)>. Swap the registers bitwise with Fredkin gates
  controlled on q (O(1) Toffolis each). Then run E_{(N-a) mod N} with its copy
  controlled on q. For q = 1 that maps |f_a(y), y> to |f_a(y), y xor y> =
  |f_a(y), 0>. For q = 0 every step is the identity.

Total: O(n) NOT, CNOT and Toffoli gates and O(n) ancillas, all returned to
|0>. The circuit is exact Clifford+T (Toffoli = 7 gates from {T, T^dagger = T^7} plus H and CNOT). A uniform
generator emits it with counters, at O(L_a) per gate for wire addresses.

**2.2 Multi-controlled XOR of a constant.** "If register R equals the
classical string e, XOR the classical constant v into register S" uses a Toffoli
ladder over |R| bits with |R| - 1 ancillas, followed by CNOTs onto the 1-bits of
v and the reverse ladder. That is O(|R| + |S|) gates, all exact.

**2.3 Hadamard test.** For |chi> = (|0> + e^{2 pi i x}|1>)/sqrt 2 and a in
{0..7}, applying T^a, then H, then measuring gives outcome o = 0 with probability
(1 + cos(2 pi x + a pi/4))/2. So E[1 - 2o] = cos(2 pi x + a pi/4).

**2.4 Random bits.** H on |0> followed by measurement gives an exact fair bit.

## 3. Exact Fourier sampling

PVSieve obtains labeled qubits with the following exact procedure FS. One copy is
(|0,x> + |1,(x+s) mod N>)/sqrt 2 with x uniformly mixed. Call its qubit **B** and
its n-qubit register **Y**. U is addition of 1 mod N on Y, with eigenvectors
|phi_k> = N^{-1/2} sum_y omega^{-ky}|y> satisfying U|phi_k> = omega^k |phi_k>.
Then

$$
|\psi_{x,s}\rangle=\sum_k N^{-1/2}\omega^{kx}\,|\psi_k\rangle_B|\phi_k\rangle_Y .
$$

**FS.** Loop over j < n as the outer loop, with c_0 = 1 mod N and
c_{j+1} = 2 c_j mod N, each updated once in O(n) bit operations. For each j and
each a in {0..7}, repeat r_FS times:
- put a fresh control in |+>;
- apply controlled addition of c_j = 2^j mod N to Y (2.1);
- apply T^a and H, then measure;
- count outcomes 0 as Z_{j,a}.

Then discard Y. Decoder: for each j, let a_j be the smallest maximizer of
Z_{j,a}, and set beta_j = ((8 - a_j) mod 8)/8. Then y_{n-1} = beta_{n-1}. For
j = n-2 down to 0, y_j is whichever of y_{j+1}/2 and y_{j+1}/2 + 1/2 is
circularly closer to beta_j (first on ties). Report khat = round(N y_0) mod N,
rounding half-integers down.

**Lemma 3.1.** Every FS operation is block-diagonal in the basis
{|phi_k>} of Y. B is untouched. Tracing out Y, the joint law of
(outcomes, B) is: draw k uniform in Z/NZ, set B exactly to psi_k, and draw the
outcomes as independent tests with Pr[0] = (1 + cos(2 pi t_j + a pi/4))/2, where
t_j = 2^j k/N mod 1. This holds for every x, hence for the mixture.

*Proof.* Controlled-U^c = |0><0| (x) I + |1><1| (x) U^c is diagonal in phi_k,
with eigenphase omega^{kc} on the |1> branch, and omega^{k c_j} = e^{2 pi i t_j}
because U^N = I. Gates and measurements on controls commute with
|phi_k><phi_k|. Every branch keeps the form sum_k N^{-1/2} omega^{kx}
|psi_k>|phi_k>|gamma_{k,o}>. Tracing out the orthonormal phi_k removes all cross
terms. QED.

**Lemma 3.2.** If every empirical frequency Z_{j,a}/r_FS is within 1/20 of its
mean, then khat = k. Hence Pr[khat != k] <= 16 n 2^{-r_FS/200} <= 2^{-V-6}.

*Proof.* Some a puts 2 pi t_j + a pi/4 within pi/8 of 0. The empirical maximizer
then has true cos > cos(pi/8) - 1/5 > 0.7238 > cos(pi/4), so
d(beta_j, t_j) < 1/8. Standard bitwise reconstruction follows: with
d(y_{j+1}, t_{j+1}) < e_{j+1} <= 1/8, the correct candidate for t_j is within
e_{j+1}/2 and the other is at >= 1/2 - 1/16. Since beta_j is within 1/8 of t_j,
it is within 3/16 of the correct candidate and > 5/16 from the other. So
d(y_0, k/N) < 2^{-(n+2)} <= 1/(4N), and rounding gives k. Hoeffding bounds each
of the 8n frequencies' deviation by 2 exp(-r_FS/200); then use a union bound and
exp(-x) <= 2^{-x}. QED.

A **leaf qubit** is a copy whose FS label satisfies khat < 2^{n-1}. Its qubit B,
with label k, is kept.

## 4. Phase vectors and collimation

A **phase vector** of length l_0 is the p-qubit state

$$
|\Phi\rangle=l_0^{-1/2}\sum_{x\in[l_0]}\omega^{K(x)s}|x\rangle
$$

together with a classical table of integers K(x). Adding a constant to all K
changes only a global phase. A vector has **offset G** if all K(x) are
congruent mod 2^G.

**4.1 Leaf (node level 0).** Acquire copies and run FS on each until p leaf
qubits psi_{k_1}, ..., psi_{k_p} are obtained. Stop after 8p copies; if fewer
are obtained, the leaf **fails**. With x read as the bit string b in {0,1}^p,
their tensor product is exactly the phase vector with
K(b) = sum_t b_t k_t. It has offset 0. Computing the table costs O(l_0 n)
bit operations.

**4.2 Collimation step.** Input: two phase vectors Phi_1, Phi_2 with offset G
and tables K_1, K_2, plus a bit count g in [1, l_c]. Steps:

1. **Key.** key(x_1,x_2) = floor(((K_1(x_1) + K_2(x_2)) mod 2^{G+g}) / 2^G),
   which lies in [0, 2^g). Compute it coherently: look up K_1(x_1) mod 2^{G+g}
   with l_0 multi-controlled XORs (2.2), do the same for K_2(x_2), add, copy the
   g key bits, then uncompute. Measure the key and call the outcome c.
2. **Bucket.** Classically enumerate J_c = {(x_1,x_2): key = c} in
   lexicographic order of (x_1,x_2). If |J_c| < l_0, the step **fails**.
   Otherwise split J_c into consecutive blocks of l_0 elements plus a remainder
   of fewer than l_0. Coherently compute the block code of (x_1,x_2) (one
   multi-controlled XOR per element of J_c). Elements of block b get code b.
   Remainder elements get the reserved code l_0, which differs from every block
   number because there are at most l_0^2/l_0 = l_0 blocks, numbered from 0.
   Measure the code and uncompute. If the code is l_0, the step fails.
   **J_c is never stored.** The controller makes counter-driven passes over all
   l_0^2 index pairs in lexicographic order. The first pass counts |J_c|. The
   second emits each element's block-code XOR, with the block code computed
   from a running counter. The third emits the renumbering for the measured
   block. Each pass uses O(p + n) bits of state.
3. **Renumber.** For the measured block E = (e_0, ..., e_{l_0-1}), XOR the index
   i into a fresh p-qubit register when (x_1,x_2) = e_i. Then XOR e_i into
   (x_1,x_2) when the new register equals i, which returns (x_1,x_2) to zero.
   The new vector has table K(i) = K_1(e_i,1) + K_2(e_i,2).

**Lemma 4.1 (exactness).** On success the output is exactly a phase vector of
length l_0 with the stated table and offset G+g.

*Proof.* Phi_1 (x) Phi_2 = l_0^{-1} sum omega^{(K_1+K_2)s}|x_1,x_2>, with all
amplitudes of equal modulus. The key and the block number are functions of the
basis index, so measuring them projects onto a set of basis indices with equal
moduli. The renumbering maps each basis state e_i to |i>. Elements of J_c share
K_1 + K_2 mod 2^{G+g}, since they share it mod 2^G (offset) and agree on the
next g bits (key). QED.

**Lemma 4.2 (success, distribution-free).** For any tables, the step succeeds
with probability >= 3/8.

*Proof.* Pr[c] = |J_c|/l_0^2. There are at most 2^g <= 2^{l_c} keys, so
Pr[|J_c| < l_0] < 2^{l_c} l_0 / l_0^2 = 1/4. Given |J_c| >= l_0, a full block is
hit with probability l_0 floor(|J_c|/l_0)/|J_c| >= 1/2. QED.

**4.3 Produce(j, i).** This node returns a phase vector with offset G_{j,i}, or
fails. For i = 0 it runs a leaf. For i >= 1 it makes up to A attempts. Each
attempt runs Phi_1 = Produce(j, i-1); on failure it moves to the next attempt.
Then it runs Phi_2 = Produce(j, i-1); on failure it discards Phi_1 and moves on.
Then it collimates with g = g_{j,i}. On success it returns the result; on failure
it moves on. After A failed attempts the node fails. Recursion is depth-first:
only Phi_1 waits while Phi_2 is produced.

**Lemma 4.3.** In the ideal world of Section 7, every Produce call fails with
probability <= 1/5.

*Proof.* Leaf: each FS label is a leaf qubit with probability
2^{n-1}/N >= 1/2. With 8p trials, the success count stochastically dominates a
Binomial(8p, 1/2), whose mean is 4p, so by Chernoff
Pr[< p successes] <= exp(-(3/4)^2 * 4p/2) = e^{-9p/8} < 1/5 for p >= 2. Node:
suppose each child fails with probability <= 1/5, independently, since children
use fresh copies. One attempt then succeeds with probability >= (4/5)^2 * 3/8 =
0.24 (Lemma 4.2), so all 8 attempts fail with probability <= 0.76^8 < 0.112.
Induct on i. QED.

**Lemma 4.4 (worst-case counts).** Produce(j, D) makes at most 16^D leaf calls
and at most 16^D collimation steps on every branch.

*Proof.* Let L(i) be the maximum number of leaf calls. L(0) = 1 and
L(i) <= 2A L(i-1), so L(D) <= 16^D. Level-i nodes number at most
(2A)^{D-i}, each with at most A steps, so the step count is at most
sum_{i=1}^{D} A (2A)^{D-i} <= (2A)^D. QED.

## 5. Output qubits and the held-out parity

**Final attempt at level j.** Run Phi = Produce(j, D_j). For j = 0 (D_0 = 0) this
is a single leaf. If it fails, the attempt fails. Otherwise measure all index
bits except the lowest. This gives y, and the remaining qubit is

$$
\omega^{K(2y)s}|0\rangle+\omega^{K(2y+1)s}|1\rangle\ \propto\ |\psi_{\Delta}\rangle,\qquad \Delta=K(2y+1)-K(2y).
$$

Offset j gives 2^j | Delta. Let w = Delta/2^j. If w is even, discard the qubit:
the attempt fails. Otherwise draw a uniform a in {0..7} (three bits, 2.4),
measure the qubit with T^a and H (2.3), and store the record (j, w, a, o).

**Leaf decomposition.** In the ideal world each leaf label is uniform on
[0, 2^{n-1}). Since j <= n-3, write
k = lo + 2^j beta + 2^{j+1} hi, with lo in [0, 2^j), beta in {0,1} and hi the
rest. The three parts are independent and uniform, and different leaves are
independent.

**Lemma 5.1 (held-out parity).** Work in the ideal world of 7.1, where each
copy contributes only (k, psi_k) and no Fourier-sampling test outcomes. Fix j.
Let F be the following data:
- the acceptance pattern of the copies;
- the lo and hi parts of all accepted leaves used at level j;
- every key, block and y outcome;
- every leaf and step failure;
- the outcomes of resetting discarded registers.

Then, conditional on F, the beta's are still i.i.d. fair bits. For a successful
Produce, w is odd with conditional probability exactly 1/2.

*Proof.* Every decision and every outcome law in Produce(j, .) depends only on
the tables mod 2^{G_{j,i}}, where G_{j,i} <= j. That covers key outcomes (by
Lemma 4.1 their law is |J_c|/l_0^2), bucket membership, block order (index
order, independent of label values), success, and retries. Tables mod 2^j are
sums of leaf labels mod 2^j, so they depend only on the lo parts. The
y-measurement is uniform over pairs and the pair rule is fixed. So the
conditional law of every outcome is unchanged by beta, and the beta's stay i.i.d.
fair given all of it.

Each index of the final vector corresponds to a unique tuple of leaf bit strings,
because leaves map bijectively and renumbering is a bijection. Indices 2y and
2y+1 are distinct, so their tuples differ at some set S != {} of leaf qubits.
Then

$$
\Delta=\sum_{t\in S}\pm k_t=\sum_{t\in S}\pm{\rm lo}_t+2^j\sum_{t\in S}\pm\beta_t+2^{j+1}(\cdots).
$$

The first sum equals 2^j kappa, where kappa is determined by the conditioning,
because 2^j divides Delta and the other terms. So
w = kappa + sum_{t in S} beta_t (mod 2). This is a known bit XOR a nonempty set
of fair independent bits, which is uniform. QED.

**Lemma 5.2 (magnitude).** In a record at level j, |w| <= p 2^{D_j} 2^{n-1-j}.

*Proof.* A successful Produce(j, D_j) tree has exactly 2^{D_j} leaves of p
qubits. Delta is a sum of at most p 2^{D_j} terms ±k_t with |k_t| < 2^{n-1}.
QED.

**Lemma 5.3 (record counts).** In the ideal world, each level's 4r final attempts
yield at least r records, except with probability <= e^{-r/9}.

*Proof.* The attempts use fresh copies. Each succeeds with conditional
probability >= (4/5)(1/2) = 0.4 given all earlier attempts, by Lemmas 4.3 and
5.1. So the success count stochastically dominates a Binomial(4r, 0.4), with
mean 1.6r, and Chernoff gives Pr[< r] <= exp(-(3/8)^2 * 1.6r/2) <= e^{-r/9}.
Only the first r records of each level are used. Section 6 applies Hoeffding
conditionally on which attempts became records and on their w values. Its
per-record bound E[Y] >= 0.146 holds uniformly over every odd w satisfying
Lemma 5.2, so selecting records by the parity of w introduces no bias. QED.

## 6. Recovering s: odd-multiplier decoder with anchors

Let t_j = 2^j theta mod 1. A record (j, w, a, o) comes from the qubit
psi_{2^j w}, whose phase is 2^j w theta = w t_j mod 1. By 2.3,
E[1 - 2o] = cos(2 pi w t_j + a pi/4).

**Sign function.** For a dyadic x and a in {0..7}, let
z = (x + a/8) mod 1. Set sigma(x,a) = +1 if z is in [0, 3/16) or [13/16, 1),
sigma = -1 if z is in [5/16, 11/16), and sigma = 0 otherwise. This is exact
integer arithmetic.

**Decoder.** For each anchor alpha in [0, Lambda):
1. Set y_{n-2} = alpha/Lambda.
2. For j = n-3 down to 0:
   - let c_0 = y_{j+1}/2 and c_1 = c_0 + 1/2;
   - compute S_j = sum over the r records at level j of
     sigma(w c_0, a)(1 - 2o);
   - set y_j = c_0 if S_j >= 0, else y_j = c_1.
3. The candidate is s_alpha = round(N y_0) mod N, rounding half-integers
   down.

Verification runs anchor by anchor. As soon as s_alpha is produced, run k_v
shift tests on t = s_alpha (7.3). If all pass, output it and halt;
otherwise move to the next anchor. Only one candidate is stored at a time. If
no anchor passes, output 0. A run abort leaves no records and counts as a
failure (Section 7.2). The sign bound below holds conditionally on level j's
w values and on y_{j+1}. Here y_{j+1} is a function of records from other
levels, and in the ideal world those come from independent copies. The
(a, o) pairs at level j are fresh.

**Lemma 6.1.** Let alpha* be an anchor with
d(alpha*/Lambda, t_{n-2}) <= 1/(2 Lambda). Unless some S_j has the wrong sign,
the chain started at alpha* gives s_{alpha*} = s.

*Proof.* Let e_j = 2^{-(n-2-j)}/(2 Lambda). By induction d(y_j, t_j) <= e_j. Given
y_{j+1}, t_j is congruent to c_0 or c_1 up to e_{j+1}/2. Call the true candidate
c*, so d(c*, t_j) <= e_{j+1}/2. The other is c* + 1/2.

For a record at level j, w is odd, so w(c* + 1/2) = w c* + 1/2 mod 1. The two
candidates therefore predict opposite signs of every non-zero sigma. By Lemma 5.2,
|w| e_{j+1} <= p 2^{D_max} 2^{n-1-j} 2^{-(n-3-j)}/(2 Lambda)
= 2 p 2^{D_max}/Lambda <= 1/16. So the true phase w t_j is within 1/32 of
w c* mod 1.

If sigma(w c*, a) != 0, then z is at distance >= 1/16 from {1/4, 3/4}. The true
point is at distance >= 1/32, so cos(2 pi w t_j + a pi/4) has the sign
sigma(w c*, a) and modulus >= sin(pi/16) > 0.195. Exactly 2 of the 8 values of a
give sigma = 0, because each excluded arc has length 1/8 and the points
x + a/8 are spaced 1/8 apart. a is uniform and independent of c*, which depends
only on records of higher levels. So each summand Y = sigma(w c_0, a)(1 - 2o)
has E[Y] >= (3/4)(0.195) > 0.146 if c_0 = c*, and E[Y] <= -0.146 if c_1 = c*.
These summands are independent and lie in [-1,1].

Then y_j = c*, and d(y_j, t_j) <= e_{j+1}/2 = e_j. At the end,
d(y_0, s/N) <= 2^{-(n-2)}/(2 Lambda), so the distance from N y_0 to an integer
congruent to s is <= 2/Lambda < 1/2. QED.

By Hoeffding, a wrong sign at level j has probability
<= exp(-(0.146 r)^2/(2r)) < e^{-r/94}. The anchors are spaced 1/Lambda apart, so
alpha* exists.

## 7. Success probability

**7.1 Ideal world and coupling.** The **ideal world** replaces each FS call
with: draw k uniform in Z/NZ, set B exactly to psi_k, and report k. No test
outcomes are exposed to the rest of the algorithm. By Lemma 3.1, the real joint
law of (B, reported label) per copy equals: draw k uniform, set B exactly to
psi_k, draw the test outcomes given k, and report D(outcomes).

So the real run is a fixed function of the per-copy pairs (k, test outcomes)
and of the later quantum and classical randomness. The law of that later
randomness depends only on the stored labels and the qubit states. Couple the
two worlds on k and on the later randomness. Off the event that some copy has
D(outcomes) != k, every stored label and every qubit state is identical in both
worlds at every step. Hence the total-variation distance between the real and
ideal output laws is at most the probability of a mislabel. There are at most
Q_max < 2^V copies, so this has probability <= 2^V 2^{-V-6} = 1/64.

**7.2 Failure in the ideal world.** Failure needs one of the following:
- some level gets fewer than r records: probability
  <= (n-2) e^{-r/9} < 2^{-200};
- some S_j on the alpha* chain has the wrong sign: probability
  <= (n-2) e^{-r/94} <= n 2^{-2(ceil(log n) + 10)} < 2^{-20};
- a wrong candidate passes verification before alpha*'s correct one: probability
  <= Lambda 2^{-k_v} = 2^{-8}.

Adding the 1/64 from coupling, PVSieve outputs s with probability > 1 - 1/64 -
1/256 - 2^{-19} > 0.97 >= 2/3 for every N and s. No postselection is used.

**7.3 Shift test.** Apply controlled subtraction of t mod N, which is
primitive 2.1 with a = (N - t) mod N controlled by the copy's qubit, to the
register of a fresh copy, then measure the qubit in the X basis. If t = s the test always
passes. If t != s it passes with probability exactly 1/2 (the branches are
orthogonal, so the qubit is maximally mixed). The cost is O(n L_a) and O(n)
qubits.

## 8. Resource accounting (every branch)

**Addressing and layout.** For n <= 15 every resource is an absolute constant,
so take n >= 16. Quantum memory is a fixed pool:
- per node level, one waiting-vector slot of p qubits;
- the active-step registers listed under "Quantum space";
- one copy-input area of n+1 qubits plus the FS control and the 2.1 ancillas;
- one final-qubit slot.

An acquired copy is loaded into the copy-input area. An accepted B is swapped
into the current leaf's next qubit, and the rest of the area is reset by
measurement and conditional X, then reused. Discarded registers are reset and
reused. Classical memory is laid out the same way, by node level. S_C + S_Q is
2^{O(sqrt n)} (below), so the per-access charge is
L_a = ceil(log(M+2)) = O(sqrt n).

**Copies.** A final attempt at level j makes at most 16^{D_j} leaf calls of at
most 8p copies each (Lemma 4.4). Levels 0..n-3 make 4r attempts each. Adding
verification:

$$
Q\le (n-2)\cdot4r\cdot16^{D_{\max}}\cdot8p+\Lambda k_v=Q_{\max}\qquad(n\ge16),
$$

and Q <= N(n+6) <= 21 * 2^15 for n <= 15.

16^{D_max} <= 16 * 2^{(8/3) sqrt n}, p = O(sqrt n) and r = O(log n). Also
Lambda k_v = 2^{(2/3) sqrt n + O(log n)}. Hence
Q = O(2^{(8/3) sqrt n} n^{3/2} log n).

**Work per copy.** Per copy, FS costs n+1 for the copy plus 8 n r_FS tests of
O(n L_a) each. r_FS = O(V + log n) = O(sqrt n), giving O(n^3). Decoding adds
O(n^2 L_a). Total per copy: O(n^3). All copies: O(Q n^3) =
O(2^{(8/3) sqrt n} n^{9/2} log n).

**Work per collimation step.**
- Coherent key: 2 l_0 multi-controlled XORs of O(n + p) gates, done and undone.
- Classical enumeration of l_0^2 pairs: O(n) bits each.
- Coherent block number: at most l_0^2 multi-controlled XORs of O(p) gates,
  done and undone.
- Renumbering: 2 l_0 multi-controlled XORs.
- Every gate and bit access is charged L_a.

Total: O(l_0^2 n L_a) = O(2^{2 l_c} n^{3/2}). By Lemma 4.4 there are at most
16^{D_max} steps per final attempt and 4r(n-2) attempts. Since
2^{2 l_c} <= 4 * 2^{3 sqrt n} and 16^{D_max} <= 16 * 2^{(8/3) sqrt n}, all
collimation work is

$$
O\!\left(n\log n\cdot2^{\left(\frac83+3\right)\sqrt n}\,n^{3/2}\right)=O\!\left(2^{\frac{17}{3}\sqrt n}n^{5/2}\log n\right).
$$

**Other work.**
- Leaf tables: O(l_0 n L_a) per leaf, which is dominated.
- Final measurements: O(L_a) per attempt.
- Decoder: Lambda anchors x (n-2) levels x r records x O(n^2 L_a) for computing
  w c_0 mod 1 exactly, which is 2^{(2/3) sqrt n} poly(n).
- Verification: Lambda k_v shift tests.
- Parameter computation: poly(n).

The copy work O(2^{(8/3) sqrt n} n^{9/2} log n) is also dominated, because
2^{3 sqrt n} >= n^2 for n >= 16. Hence

$$
T=O\!\left(2^{\frac{17}{3}\sqrt n}\,n^{5/2}\log n\right).
$$

**Quantum space.** Depth-first recursion keeps at most one waiting vector
(Phi_1) per node level, which is at most D_max p = O(n) qubits, because
D_max p <= ((2/3) sqrt n + 1)((3/2) sqrt n + 3). The active step uses:
- two vectors: 2p qubits;
- the key: <= l_c qubits;
- the label-sum work register: n + O(sqrt n) qubits;
- the block register: <= 2p qubits;
- the new index: p qubits;
- ladder ancillas: O(p) qubits.

A leaf adds p kept qubits plus the FS workspace (n + O(n) qubits), and a final
attempt holds one qubit, which is measured at once. So S_Q = O(n).

**Classical space.**
- Waiting tables: at most one per node level plus three in the active step, each
  with l_0 entries of n + O(sqrt n) bits (|K| <= p 2^{D_max} 2^{n-1}). That is
  O(D_max 2^{l_c} n) = O(2^{(3/2) sqrt n} n^{3/2}).
- Records: (n-2) r of O(n) bits, which is O(n^2 log n).
- FS counters: O(n log r_FS).
- Decoder state, processed per anchor: O(n + lambda).
- Enumeration counters and parameters: O(n).
- No circuit is stored.

So S_C = O(2^{(3/2) sqrt n} n^{3/2}).

## 9. Envelopes and indices

| Resource | Envelope B(n) | Index |
| --- | --- | --- |
| T | 2^{(17/3) sqrt n} n^{5/2} log n | 1/2 |
| S_C | 2^{(3/2) sqrt n} n^{3/2} | 1/2 |
| S_Q | n | 0 |
| Q | 2^{(8/3) sqrt n} n^{3/2} log n | 1/2 |

For T, S_C and Q: log B = a sqrt n + O(log n), where a is the explicit rational
17/3, 3/2 or 8/3 derived in Section 8 from l_c >= (3/2) sqrt n and
D_max <= (2/3) sqrt n + 1. So log log B / log n -> 1/2. For S_Q,
log log n / log n -> 0. The outer big-O constants are absolute, independent of
N, s and outcomes. No exponent coefficient is unknown.

## 10. Error tolerance

The proof assumes that all acquired copies are independent ideal coset states.
The tolerance claim is epsilon(n) = 0. No positive tolerance is asserted, and
this does not prove that positive tolerance is impossible.

## 11. Relation to prior work

- Collimation of phase vectors by measuring low bits of label sums, depth-first
  traversal and the polynomial-quantum-space idea come from Kuperberg 2013
  (arXiv:1112.3333, Sections 4.2-4.6) and Regev 2004 (arXiv:quant-ph/0406151,
  Section 3). Lemma 4.2's distribution-free bucket bound is the argument of
  Kuperberg's Proposition 4.5. The fixed-length blocks are its trimming
  measurement.
- Those papers treat N = 2^n, where the favorable final label 2^{n-1} appears
  with probability 1/2. For general N, PVSieve replaces that step with the
  held-out parity (Lemma 5.1) and the odd-multiplier anchored decoder
  (Section 6). Both are proved here.
- Fourier sampling uses Kitaev-style Hadamard tests (arXiv:quant-ph/9511026)
  with T^a offsets, so no rotation synthesis is needed. The shift test and the
  modular adder follow this repository's baseline.
- The coefficients 17/3, 8/3 and 3/2 are what this proof establishes with
  l_c = ceil((3/2) sqrt n) and A = 8. They are not claimed to be optimal.
