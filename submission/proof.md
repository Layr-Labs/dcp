# Parity sieve: Kuperberg-style pairing with a held-out parity, for every N

This file proves all five claims of `submission.json` for **one** algorithm,
called **PSieve** below. PSieve is Kuperberg's pairing sieve (G. Kuperberg,
SIAM J. Comput. 35(1):170-188, 2005, arXiv:quant-ph/0302112). Labeled qubits
are paired so that their labels' low bits match, and the difference label is
kept. The new parts let it be proved for **every** modulus N in this challenge's
cost model without rejection sampling or uniformity of intermediate labels:

- pairing counts are analyzed **distribution-free**: they depend only on the
  number of key classes;
- the one distributional fact used is a **held-out parity**: bit j of the leaf
  labels is never consulted, so an output label 2^j w has w odd with
  probability exactly 1/2, independently across outputs;
- odd but large known multipliers w are read off by an **anchored top-down
  decoder**, followed by candidate verification;
- Fourier labels come from exact Hadamard tests, with no rotations. Every gate is
  exact Clifford+T, so no synthesis is needed.

No novelty of the 2^{O(sqrt n)} growth is claimed. With c = 17/6 the proved
bounds are

$$
T=O\!\left(2^{c\sqrt n}n^5\log n\right),\
S_C=O\!\left(2^{c\sqrt n}n^2\log n\right),\
S_Q=O\!\left(2^{c\sqrt n}n\log n\right),\
Q=O\!\left(2^{c\sqrt n}n^2\log n\right),
$$

each with UI growth index exactly 1/2. Success is > 0.97 for every N and s.

All logarithms are base 2. n = ceil(log N), so 2^{n-1} < N <= 2^n. Write
omega = e^{2 pi i/N} and theta = s/N. For an integer K,
|psi_K> = (|0> + omega^{Ks}|1>)/sqrt 2, which depends only on K mod N. Labels are
tracked as exact integers.

## 1. Parameters

**Small instances.** If n <= 15, PSieve runs exhaustive shift testing: for
t = 0, ..., N-1 it runs n+6 shift tests (Section 7.3) and outputs the first t
that passes all of them, or 0. A wrong output has probability
<= (N-1) 2^{-(n+6)} < 1/64. The branch uses at most N(n+6) <= 21 * 2^15 copies
and constant work and space.

For n >= 16, PSieve computes:

1. d = ceil((3/4) sqrt n), the least integer with 16 d^2 >= 9n. Then
   (3/4) sqrt n <= d < (3/4) sqrt n + 1, and d >= 3.
2. l = ceil((n-3)/d). Then 1 <= l < (n-3)/d + 1 < (4/3) sqrt n + 1.
3. The levels are j in {0, ..., n-3}. For level j: d_j = ceil(j/l) <= d stages,
   with g_{j,i} = l for i < d_j and g_{j,d_j} = j - (d_j - 1) l, which is in
   [1, l]. G_{j,i} = g_{j,1} + ... + g_{j,i}, G_{j,0} = 0, and G_{j,d_j} = j.
4. r = 200(ceil(log n) + 10).
5. Stage targets for level j: T^{(j)}_{d_j} = 32(d+1)^2 r and
   T^{(j)}_{i-1} = 2^{g_{j,i}} + ceil(4(d+1) T^{(j)}_i / d).
6. lambda = d + 5, Lambda = 2^lambda (anchors) and k_v = lambda + 8.
7. Q_max = sum_j 4 T^{(j)}_0 + Lambda k_v. V is the bit length of Q_max, and
   r_FS = 200(V + ceil(log n) + 10).

All of these are integers of O(sqrt n) bits, computed in poly(n) time.

## 2. Exact primitives

**2.1 Controlled modular addition of a classical constant.** For a classical
constant a in [0,N), let f_a(y) = (y+a) mod N for y < N and f_a(y) = y for
N <= y < 2^n. It is a permutation of n-bit strings, with inverse
f_{(N-a) mod N}. The circuit is explicit and has O(n) gates:

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
|0>. Toffoli has an exact 7-T-gate Clifford+T decomposition, so the circuit is
exact. A uniform generator emits it with binary counters. Each gate
names O(1) wires, and each wire index is an O(L_a)-bit number, where L_a is the
addressing charge of Section 8. Generating and applying one controlled addition
therefore costs O(n L_a) bit operations.

**2.2 Hadamard test with a T-power.** Let |chi> = (|0> + e^{i phi}|1>)/sqrt 2
and a in {0,...,7}. Apply T^a (at most 7 T gates; T^a multiplies |1> by
e^{i a pi/4}), then H, then measure. The outcome is 0 with probability exactly

$$
p_a(\phi)=\tfrac12\bigl(1+\cos(\phi+a\pi/4)\bigr).
$$

**2.3 Combination.** For labeled qubits psi_{K1} (qubit 1) and psi_{K2}
(qubit 2), apply CNOT with control 1 and target 2, then measure qubit 2. The
state before measurement is

$$
\tfrac12\sum_{b_1,b_2}\omega^{s(b_1K_1+b_2K_2)}|b_1,\,b_1\oplus b_2\rangle .
$$

Outcome o = b_1 xor b_2. For o = 1 the surviving terms are
omega^{s K2}|0> (b_1 = 0) and omega^{s K1}|1> (b_1 = 1), so qubit 1 becomes
psi_{K1-K2} up to the global phase omega^{s K2}. For o = 0 it becomes
psi_{K1+K2}. Each outcome has probability exactly 1/2 for all K1, K2, s.

**2.4 Random bits.** H on a fresh |0> followed by measurement gives an exactly
uniform bit, independent of everything else.

## 3. Exact Fourier sampling (labels over Z/NZ)

One source copy is the state |psi_{x,s}> = (|0,x> + |1,(x+s) mod N>)/sqrt 2,
with x uniformly mixed. Call the first qubit **B** and the n-qubit register
**Y**. Let U be addition of 1 mod N on Y, restricted to span{|y>: y < N}. Its
eigenvectors are

$$
|\phi_k\rangle=N^{-1/2}\sum_{y<N}\omega^{-ky}|y\rangle,\qquad U|\phi_k\rangle=\omega^{k}|\phi_k\rangle,
$$

and |y> = N^{-1/2} sum_k omega^{ky} |phi_k>. Hence

$$
|\psi_{x,s}\rangle=\sum_{k=0}^{N-1} N^{-1/2}\,\omega^{kx}\,|\psi_k\rangle_B\otimes|\phi_k\rangle_Y. \tag{3.1}
$$

**Procedure FS.** Loop over j in {0,...,n-1} as the outer loop. Keep the
constant c_j = 2^j mod N, updated once per j as c_0 = 1 mod N and
c_{j+1} = 2 c_j mod N (O(n) bit operations). For each j and each a in
{0,...,7}, repeat r_FS times. Prepare a control qubit in |0>, apply H, apply controlled-U^{c_j}
with c_j = 2^j mod N (primitive 2.1, control = this qubit, target = Y), apply
T^a and H, measure, and reset the control. Let Z_{j,a} be the number of
outcomes 0. Then discard Y (reset it), keep B, and compute the reported label
khat by the decoder D below.

**Decoder D (Kitaev-style, all arithmetic exact on dyadic rationals).** Given
counts for j = 0..M-1 with M bits, let a_j be the smallest a maximizing
Z_{j,a}. Set beta_j = ((8 - a_j) mod 8)/8. Let y_{M-1} = beta_{M-1}. For
j = M-2 down to 0, choose y_j among the candidates y_{j+1}/2 and
y_{j+1}/2 + 1/2 as the one at smaller circular distance from beta_j (ties: the
first). Output y_0 in [0,1). In FS, M = n, and khat is the integer nearest to N
y_0 (rounding half-integers down), reduced mod N. Every y_j is a multiple of 2^{-(M+2)}, so all comparisons
are exact integer comparisons on M+3 bits.

**Lemma 3.1 (block structure).** Fix any x. Every operation of FS acts on Y and
the control qubits as sum_k |phi_k><phi_k| (x) O_k, where O_k acts on controls
only, or measures controls. B is never touched. Hence the joint law of
(classical outcomes, state of B) after Y is discarded is: choose k uniform in
Z/NZ; B is exactly psi_k; the outcomes are distributed as the tests run with Y
replaced by the eigenvector phi_k. In that eigenvector case the tests are
independent, and test (j,a) gives 0 with probability p_a(2 pi t_j), where
t_j = 2^j k/N mod 1. This law does not depend on x, so it also holds for the
mixed source.

*Proof.* controlled-U^c = |0><0| (x) I + |1><1| (x) U^c is diagonal in the
phi_k basis, with eigenvalue omega^{kc} on |1>|phi_k>. Gates and measurements on
controls commute with |phi_k><phi_k|. Starting from (3.1), an induction over
operations shows that each unnormalized post-measurement branch for outcome
string o has the form sum_k N^{-1/2} omega^{kx} |psi_k>|phi_k>|gamma_{k,o}>,
where gamma_{k,o} is the control state that the same operations produce from
phi_k. Tracing Y, which is orthonormal in k, removes all cross terms. The result
is Pr[o] = N^{-1} sum_k ||gamma_{k,o}||^2 with B in the mixture of psi_k weighted
by ||gamma_{k,o}||^2. In the phi_k branch the control of test (j,a) is
(|0> + omega^{k c_j}|1>)/sqrt 2 with omega^{k c_j} = e^{2 pi i t_j}, because
U^N = I. Then 2.2 applies. Controls are fresh and reset, and phi_k is unchanged,
so the tests are independent. QED.

**Lemma 3.2 (estimation).** Let phi in R and let a* maximize p_a(phi). Suppose
the empirical frequencies satisfy |Z_a/r - p_a(phi)| < 1/20 for all a. Then the
chosen ahat satisfies d(phi/(2 pi), -ahat/8) < 1/8, where d is circular distance
on R/Z.

*Proof.* Some a puts phi + a pi/4 within pi/8 of 0 mod 2 pi, so
p_{a*} >= (1 + cos(pi/8))/2. Then
p_ahat > Z_ahat/r - 1/20 >= Z_{a*}/r - 1/20 > p_{a*} - 1/10, so
cos(phi + ahat pi/4) > cos(pi/8) - 1/5 > 0.9238 - 0.2 > 0.7072 > cos(pi/4).
Hence phi + ahat pi/4 lies within pi/4 of 0 mod 2 pi, which is the claim. QED.

**Lemma 3.3 (reconstruction).** Let t_j = 2^j theta' mod 1 for j < M, for some
real theta'. If d(beta_j, t_j) < 1/8 for every j, the decoder's y_0 satisfies
d(y_0, theta') < 2^{-(M+2)}.

*Proof.* Induction downward with e_j := 2^{-(M-1-j)}/8: claim d(y_j, t_j) < e_j.
For j = M-1 this is the hypothesis. Assume it for j+1 and write
t_{j+1} = y_{j+1} + delta + z with |delta| < e_{j+1} <= 1/8 and z an integer.
Since 2 t_j = t_{j+1} mod 1, t_j is congruent mod 1 to t_{j+1}/2 or
t_{j+1}/2 + 1/2. Both are congruent to y_{j+1}/2 + delta/2 + (a multiple of 1/2).
So one candidate c* has d(c*, t_j) <= |delta|/2 < e_j <= 1/16, and the other is
at distance >= 1/2 - 1/16 from t_j. With d(beta_j, t_j) < 1/8, c* is within 3/16
of beta_j and the other candidate is at distance > 5/16 from it, so the decoder
picks c*. At j = 0, e_0 = 2^{-(M+2)}. QED.

**Lemma 3.4 (FS error).** Under FS with M = n, Pr[khat != k] <= delta_FS :=
16 n 2^{-r_FS/200}.

*Proof.* By Hoeffding, each of the 8n frequencies deviates by >= 1/20 with
probability <= 2 exp(-2 r_FS/400) <= 2 * 2^{-r_FS/200}. Outside this union
event, Lemmas 3.2 and 3.3 give d(y_0, k/N) < 2^{-(n+2)} <= 1/(4N). Then N y_0
is within 1/4 of an integer congruent to k mod N, so khat = k. QED.

With r_FS from Section 1, delta_FS <= 16 n 2^{-V - ceil(log n) - 10} <=
2^{-V-6}.

## 4. The sieve for level j

A **record** is (K, slot): an integer label K and the address of a pool qubit
in state psi_K.

**Leaves.** Acquire up to 4 T_0 copies (T_0 = T^{(j)}_0), one at a time, and
run FS on each. Accept a copy iff khat < 2^{n-1}, and move its B qubit into the
next free pool slot. Stop once T_0 copies are accepted. If fewer than T_0 are
accepted, the run **aborts**.

**Stage i (1 <= i <= d_j), from exactly T_{i-1} records.** Every label at this
point is divisible by 2^{G_{j,i-1}} (vacuous for i = 1). The key of a label K is

$$
\kappa_i(K)=\bigl\lfloor (K \bmod 2^{G_{j,i}})/2^{G_{j,i-1}}\bigr\rfloor\in[0,2^{g_{j,i}}),
$$

with mod taken as the nonnegative residue. Merge-sort the records by key, with
ties broken by record index. In each key class, pair consecutive records. For
each pair (K_1, slot_1), (K_2, slot_2), apply the combination 2.3 with slot_1 as
qubit 1. If o = 1, emit (K_1 - K_2, slot_1). If o = 0, reset both slots.
Unpaired records are reset. Keep the first T_i emitted records in pair order and
reset the rest. If fewer than T_i are emitted, the run aborts. Since
K_1 = K_2 mod 2^{G_{j,i}}, every emitted label is divisible by 2^{G_{j,i}}.

**Outputs.** After stage d_j (for j = 0 there are no stages, and the outputs are
the leaves), every label is K = 2^j w. Keep the records with w odd. If fewer
than r exist, the run aborts. For the first r of them, draw a uniform a in
{0..7} (three random bits, 2.4), apply T^a and H to the slot, measure it, and
store (j, w, a, o). Reset every slot. Runs for different j are sequential and
share the pool.

**Abort rule.** If any run aborts, PSieve outputs 0 and halts. This counts
as a failure in Section 7.

## 5. Analysis in the ideal world

In the **ideal world**, each FS call is replaced by: draw k uniform in Z/NZ,
set B exactly to psi_k, and report k. No test outcomes are exposed to the rest
of the algorithm. Section 7.1 bounds the difference from the real algorithm.

**Lemma 5.1 (labels and states).** In the ideal world:
- every accepted leaf has a label uniform on [0, 2^{n-1}), independent of the
  other leaves and of the acceptance pattern, and is exactly psi_k;
- every emitted record's qubit is exactly psi_K for its stored K, in a product
  state with all other slots;
- a record at stage i is K = sum_t eps_t k_t over its 2^i leaves, with every
  eps_t in {+1, -1}.

*Proof.* Lemma 3.1 gives i.i.d. uniform k with B = psi_k. Acceptance is the
event k < 2^{n-1}. The combination 2.3 maps psi_{K_1} (x) psi_{K_2} to
psi_{K_1 - K_2} on outcome 1. Pairs act on disjoint slots. Induct on i. QED.

**Lemma 5.2 (magnitude).** An output at level j has |w| <= 2^{d} 2^{n-1-j}.

*Proof.* |K| <= 2^{d_j} max |k_t| < 2^{d} 2^{n-1}. QED.

**Lemma 5.3 (held-out parity).** Fix j. Write each accepted leaf label as
k = lo + 2^j beta + 2^{j+1} hi, with lo < 2^j and beta in {0,1}. This is
possible since j <= n-3. Let F be the following data:
- all lo and hi parts;
- the acceptance pattern;
- all combination outcomes.

Every decision of the run (keys, pairing, truncation, aborts) is a function of
F. The stored labels are functions of F together with the betas. Conditional on
F, the betas are i.i.d. fair, and the output parities w mod 2 are i.i.d. fair
bits.

*Proof.* Each leaf is uniform on [0, 2^{n-1}), and n-1 >= j+2, so lo, beta and
hi are independent and uniform, independently across leaves. Keys depend only
on labels mod 2^{G_{j,i}} with G_{j,i} <= j. Labels are signed sums of leaves,
so keys depend only on the lo parts. The pairing depends only on keys and
indices. Each combination outcome is exactly 1/2-1/2 whatever the labels
(2.3). Truncation to the first T_i records depends only on outcomes and order.
So the conditional law of F does not depend on the betas, and the betas stay
i.i.d. fair given F.

An output's label is K = sum_{t in L} eps_t k_t, where L is its leaf set, which
is nonempty. Write sum eps_t lo_t = 2^j kappa, with kappa determined by F,
because 2^j divides K and the other two terms. Then
w = kappa + sum_{t in L} eps_t beta_t (mod 2) = kappa + XOR_{t in L} beta_t.
Distinct outputs have disjoint leaf sets, so their parities are independent
fair bits given F. QED.

**Lemma 5.4 (no abort).** In the ideal world, a run aborts with probability at
most (d+2) e^{-2r}.

*Proof.* Chernoff: Pr[X <= (1-delta) mu] <= exp(-delta^2 mu/2) for binomial X.

Leaves: each copy is accepted with probability 2^{n-1}/N >= 1/2. With 4T_0
copies, mu >= 2T_0, and Pr[fewer than T_0] <= e^{-T_0/4}.

Stage i: a key class with c records gives floor(c/2) >= (c-1)/2 pairs, and at
most 2^{g_{j,i}} classes are nonempty. So the pair count is
P >= (T_{i-1} - 2^{g_{j,i}})/2. Emissions are Binomial(P, 1/2) given F
restricted to keys, with mu = P/2 >= (T_{i-1} - 2^{g_{j,i}})/4 >= (d+1) T_i/d.
So Pr[X < T_i] <= exp(-mu/(2(d+1)^2)) <= exp(-T_i/(2(d+1)^2)) <= e^{-16r},
because T_i >= T_{d_j} = 32(d+1)^2 r.

Outputs: by Lemma 5.3 the number of odd w is Binomial(T_{d_j}, 1/2), with mean
16(d+1)^2 r >= 16r, so it is < r with probability <= e^{-2r}. QED.

## 6. Recovering s: anchored odd-multiplier decoder

Let t_j = 2^j theta mod 1. The record (j, w, a, o) comes from psi_{2^j w}, whose
phase is 2^j w theta = w t_j mod 1. By 2.2, E[1 - 2o] = cos(2 pi w t_j + a pi/4).

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
shift tests on t = s_alpha (Section 7.3). If all pass, output it and halt;
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
|w| e_{j+1} <= 2^{d} 2^{n-1-j} 2^{-(n-3-j)}/(2 Lambda) = 2^{d+1}/Lambda <= 1/16. So the true phase w t_j is within 1/32 of
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

**7.1 Coupling.** By Lemma 3.1, the real joint law of each FS call
(B, reported label) equals: draw k uniform, set B exactly to psi_k, draw the
test outcomes given k, and report the decoder output. So the real run is a
fixed function of the per-copy pairs (k, outcomes) and of later randomness,
whose law depends only on stored labels and qubit states. Couple the real and
ideal worlds on k and on the later randomness. Off the event that some copy has
khat != k, every stored label and every qubit state agree at every step. So
the total-variation distance between the two output laws is at most the
probability of that event. At most Q_max < 2^V copies are acquired, so by Lemma 3.4 this has
probability <= 2^V 2^{-V-6} = 1/64.

**7.2 Total.** In the ideal world, failure needs one of the following:
- an abort in one of n-2 runs: probability <= n(d+2) e^{-2r} < 2^{-4000};
- a wrong sign on the alpha* chain: probability
  <= (n-2) e^{-r/94} < n 2^{-3(ceil(log n) + 10)} < 2^{-30};
- a wrong candidate passing verification before alpha*'s: probability
  <= Lambda 2^{-k_v} = 2^{-8}.

The real algorithm therefore fails with probability < 1/64 + 1/256 + 2^{-29}
< 0.03 (the bullet bounds sum to less than 2^{-8} + 2^{-29}). So it outputs s
with probability > 0.97 >= 2/3 for every N and s
(> 63/64 for n <= 15). No postselection is used, and aborts count as failures.

**7.3 Shift test.** Given a fresh copy, apply primitive 2.1 with
a = (N - t) mod N, controlled by the copy's qubit, then measure that qubit in
the X basis. If t = s, the test always passes. If t != s, the two branches are
orthogonal and the qubit is maximally mixed, so it passes with probability
exactly 1/2. Tests on fresh copies are independent. Cost: O(n L_a) work and O(n)
qubits.

## 8. Resource accounting (every branch, n >= 16)

**Layout and addressing.** Quantum memory is a pool of T_max := max_j T^{(j)}_0
slots, plus one copy-input area (n+1 qubits), one FS control, the O(n)
ancillas of 2.1, and one random-bit qubit. Copies are loaded into the input
area. An accepted B is swapped into a pool slot, and the rest of the area is
reset (measure, conditional X) and reused. Classical memory is the record arrays
of the current stage (input <= T_max, output <= T_max, merge buffer <= T_max),
the records (j, w, a, o) of Section 6, counters and parameters. This fixes
M = S_C + S_Q = 2^{O(sqrt n)}, so the address charge is
L_a = ceil(log(M+2)) = O(sqrt n).

**Constants.** Let mu' = 4(d+1)/d. The recurrence gives
T_{i-1} <= mu' T_i + 2^l + 1, so T^{(j)}_0 <= mu'^d (T_d + 2^l + 1), with
T_d := 32(d+1)^2 r, using mu' >= 2 and d_j <= d. Since (1 + 1/d)^d < e < 3 and
d < (3/4) sqrt n + 1, mu'^d < 3 * 4^d < 12 * 2^{(3/2) sqrt n}. Also
2^l < 2 * 2^{(4/3) sqrt n}. Hence

$$
T_{\max}<12\,(T_d+3)\,2^{\left(\frac32+\frac43\right)\sqrt n}=12\,(T_d+3)\,2^{\frac{17}{6}\sqrt n}.
$$

For n >= 16: d+1 < (3/4) sqrt n + 2 <= (5/4) sqrt n and r <= 750 log n, so
T_d < 32 (25/16) n * 750 log n = 37500 n log n. Thus
T_max = O(2^{(17/6) sqrt n} n log n).

**Samples.**
Q <= sum_j 4 T^{(j)}_0 + Lambda k_v <= 4(n-2) T_max + 2^{d+5}(d+13) = Q_max.
So Q = O(2^{(17/6) sqrt n} n^2 log n). For n <= 15, Q <= N(n+6) <= 21 * 2^15.

**Work.**
- Per copy: n+1 for the copy, plus FS. FS runs 8n r_FS Hadamard tests, each
  O(n L_a) (2.1 and O(1) gates). c_j is updated once per j. r_FS = O(sqrt n),
  since V = log Q_max + O(1) = O(sqrt n). Decoding and rounding cost
  O(n^2 L_a). Total per copy: O(n^3). Over all copies, including verification
  copies (whose shift tests cost O(n L_a)): O(Q_max n^3).
- Sieve, per run:
  - merge sorts: O(T_{i-1} log T_{i-1}) record operations of O(n) bits at
    O(L_a) each. Labels have at most n + d bits. That is O(T_{i-1} n^2) per
    stage;
  - per pair: one CNOT, one measurement, one subtraction and two resets,
    O(n L_a).

  Since T_i <= T_{i-1}/4, the sum of T_i is at most (4/3) T_0, so a run costs
  O(T_max n^2). All n-2 runs: O(T_max n^3).
- Outputs and decoder:
  - output tests: O((n-2) r L_a);
  - the decoder: Lambda anchors x (n-2) levels x r records x O(n^2 L_a) for the
    exact products w c_0 mod 1. This is 2^{(3/4) sqrt n + O(log n)}, which is
    negligible;
  - parameter computation: poly(n).
- Total:

$$
T=O(Q_{\max}n^3)+O(T_{\max}n^3)+2^{\frac34\sqrt n}{\rm poly}(n)=O\!\left(2^{\frac{17}{6}\sqrt n}n^5\log n\right).
$$

**Quantum space.** S_Q <= T_max + O(n) = O(2^{(17/6) sqrt n} n log n).

**Classical space.** Three record arrays of <= T_max records, each with
n + d + O(1) label bits and an O(log T_max) = O(sqrt n)-bit slot address, give
O(T_max n). Add (n-2) r stored records of O(n) bits, FS counters
(O(n log r_FS)), decoder state processed per anchor (O(n + lambda)), and
parameters (O(n sqrt n)). So S_C = O(T_max n) = O(2^{(17/6) sqrt n} n^2 log n).
No circuit is stored, since gates are generated on the fly.

## 9. Envelopes and indices

| Resource | Envelope B(n) |
| --- | --- |
| T | 2^{(17/6) sqrt n} n^5 log n |
| S_C | 2^{(17/6) sqrt n} n^2 log n |
| S_Q | 2^{(17/6) sqrt n} n log n |
| Q | 2^{(17/6) sqrt n} n^2 log n |

Each satisfies log B = (17/6) sqrt n + O(log n), so log log B / log n -> 1/2,
and every index is exactly 1/2. The exponent coefficient 17/6 is the explicit
rational proved in Section 8. Outer big-O constants are absolute, independent of
N, s and outcomes.

## 10. Error tolerance

The proof assumes that all acquired copies are independent ideal coset states.
The tolerance claim is the clean-input fraction epsilon(n) = 0. No positive
tolerance is asserted, and this is not a proof that positive tolerance is
impossible.

## 11. Relation to prior work

- Pairing labeled qubits on matching low bits and keeping the difference is
  Kuperberg's sieve (SIAM J. Comput. 2005, Sections 3-4). For N = 2^n, the final
  label 2^{n-1} appears with probability 1/2 because labels stay uniform mod
  2^n. For general N, Kuperberg sketches an interval sieve, where the bit
  balance is "a bit tricky". Here that step is replaced by the held-out parity
  (Lemma 5.3) and the anchored odd-multiplier decoder (Section 6). Both are
  proved above, and intermediate labels need no uniformity.
- The distribution-free counting of pairs follows the bucket argument of
  Kuperberg (arXiv:1112.3333, Proposition 4.5).
- Fourier labels use Kitaev-style Hadamard tests (arXiv:quant-ph/9511026) with
  T^a offsets. The shift test and the modular adder follow this repository's
  baseline.
- Only the constant 17/6 as proved here is claimed. It is not claimed to be
  optimal.
