# Linear-cost collimation for phase vectors: O(n) qubits, time 2^{(67/18) sqrt n}

This file proves all five claims of `submission.json` for **one** algorithm,
called **LPVSieve** below. LPVSieve is the depth-first phase-vector collimation
sieve PVSieve of our earlier submission 4db17801-215e-4bb1-8e67-f4135b1ecd8d,
with two changes. First, each collimation step now costs O(l_0 + 2^g) table
operations instead of O(l_0^2): the bucket is never enumerated pair by pair.
Second, phase vectors are twice as long relative to the collimated bit count
(l_0 = 2^{l_c+3}). That raises the distribution-free step success to 7/16 and
allows A = 5 attempts per node instead of 8, so the recursion tree has
branching 10 instead of 16. The method
follows O. Regev ("A subexponential time algorithm for the dihedral hidden
subgroup problem with polynomial space", arXiv:quant-ph/0406151) and
G. Kuperberg ("Another subexponential-time quantum algorithm for the dihedral
hidden subgroup problem", TQC 2013, arXiv:1112.3333). Kuperberg's Section 4.3
(Proposition 4.2 and Corollary 4.3) does collimation in time quasi-linear in
max(l_1, l_2, |J|) by sorted lookup and the two-permutation renumbering U_2 U_1. That renumbering
lists the whole measured set J, whose size can approach l_0^2 when the labels
are concentrated. Section 4.2 below replaces the listing with a **mixed-radix
rank** over key classes. Ranks, block selection and renumbering then cost
O(l_0 + 2^g) table operations for **every** label distribution, the
concentrated case included. Both papers state their algorithms for N = 2^n.
This file gives a complete proof for **every** N in this challenge's cost model,
with explicit constants. No novelty of the growth rate is claimed. The
ingredients are:

- labels are exact integers. Collimation only ever cancels **low** bits, and the
  probability analysis does not depend on how the labels are distributed
  (Lemma 4.2);
- linear-cost collimation by class histograms, a mixed-radix rank, a measured
  block code and a two-permutation renumbering. Every quantum table read is an
  explicit sequence of multi-controlled XORs, with no QRAM (Section 4.2,
  Lemma 4.0);
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
T=O\!\left(2^{\frac{67}{18}\sqrt n}n^{5/2}\log n\right),\
S_C=O\!\left(2^{\frac32\sqrt n}n^{3/2}\right),\
S_Q=O(n),\
Q=O\!\left(2^{\frac{20}{9}\sqrt n}n^{3/2}\log n\right).
$$

Their UI indices are 1/2, 1/2, 0 and 1/2.

## 1. Parameters

For n <= 15, LPVSieve runs exhaustive shift testing: for t = 0, ..., N-1 it
runs n+6 shift tests (7.3) and outputs the first t that passes all of them, or 0
if none passes. A wrong output has probability <= (N-1) 2^{-(n+6)} < 1/64, so
success is > 63/64. This branch uses at most N(n+6) <= 21 * 2^15 copies and
constant work and space. From here on n >= 16. LPVSieve computes:

1. l_c = ceil((3/2) sqrt n), the least integer with 4 l_c^2 >= 9n. Then
   (3/2) sqrt n <= l_c < (3/2) sqrt n + 1.
2. p = l_c + 3 and l_0 = 2^p. l_0 is the length of every phase vector, and p is
   the number of qubits that store one.
3. The levels used are j in {0, 1, ..., n-3}.
4. For level j: D_j = ceil(j/l_c) (so D_0 = 0 and the list below is empty for j = 0), with bit counts g_{j,1} = ... =
   g_{j,D_j-1} = l_c and g_{j,D_j} = j - (D_j - 1) l_c, each in [1, l_c].
   G_{j,i} = g_{j,1} + ... + g_{j,i}, and G_{j,0} = 0, so G_{j,D_j} = j.
   D_max := ceil((n-3)/l_c) <= n/l_c + 1 <= (2/3) sqrt n + 1.
5. A = 5, the attempts per node. r = 200(ceil(log n) + 10). Each level makes
   4r final attempts.
6. lambda = D_max + ceil(log p) + 5 and Lambda = 2^lambda >= 32 p 2^{D_max},
   the anchors. k_v = lambda + 8.
7. Q_max = (n-2) * 4r * 10^{D_max} * 8p + Lambda k_v. V = the bit length of
   Q_max. r_FS = 200(V + ceil(log n) + 10).

## 2. Exact primitives

**2.1 Controlled modular addition of a classical constant.** For a in [0,N),
let f_a(y) = (y+a) mod N for y < N and f_a(y) = y for N <= y < 2^n. This is a
permutation with inverse f_{(N-a) mod N}. Explicit circuit:

- *Ripple primitives with a classical constant b (m bits; m = n+1, or m = 2p in
  4.2 step 3).* Addition y+b: keep carries in fresh ancillas c_1..c_{m+1}. The carry rule is
  c_{i+1} = y_i AND c_i if b_i = 0, and y_i OR c_i = NOT(NOT y_i AND NOT c_i) if
  b_i = 1. Each is one Toffoli plus O(1) X/CNOT. Sum bits are y_i xor b_i xor c_i
  (CNOTs and X). Comparison [u >= b], for a classical b with 1 <= b <= 2^m and an
  m-bit register u (m = n+1 here, and m = 2p in 4.2 step 3), is the final carry c_{m+1} of the addition
  u + (2^m - b) by the carry rule above, with 2^m - b written in m bits. Truth
  table: u + 2^m - b >= 2^m iff u >= b, so c_{m+1} = 1 exactly when u >= b, and
  c_{m+1} = 0 exactly when u < b. (The final borrow of u - b is [u < b], the
  complement of this bit; it is not used.) Only c_{m+1} is copied out. The other
  carries are uncomputed by running the carry chain in reverse. Every
  comparison in this file has b = N with 1 <= N <= 2^n < 2^{n+1} = 2^m, or
  b = R_full with 1 <= R_full <= 2^{2p} = 2^m (4.2 step 3). Each primitive uses O(n) gates and O(n) ancillas, and its scratch is
  reversible.
- *Out-of-place evaluation E_a: |y>|z> -> |y>|z xor f_a(y)>.* Compute in fresh
  scratch:
  - v = [y >= N];
  - u = y + a (n+1 bits);
  - g = [u >= N];
  - u'' = u - N into a fresh (n+1)-bit register: the m-bit addition
    u + (2^m - N) mod 2^m of a classical constant, by the rule above, which
    equals u - N whenever g = 1. Then u' = g ? u'' : u, selected
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

**2.5 Addition of two quantum registers.** For m-bit registers A and B holding
a and b, the out-of-place map |a>|b>|0> -> |a>|b>|(a+b) mod 2^m> uses fresh
ancillas c_0 = 0, c_1..c_m and a fresh m-bit sum register S. For i = 0..m-1,
the carry is c_{i+1} = MAJ(a_i, b_i, c_i) = a_i b_i xor a_i c_i xor b_i c_i,
computed with three Toffolis targeting the fresh c_{i+1}. Then
S_i = a_i xor b_i xor c_i, computed with three CNOTs into S_i. Truth table:
c_{i+1} is 1 iff at least two of a_i, b_i, c_i are 1, and S_i is their sum
mod 2, which is exactly schoolbook addition. After the caller has copied what it
needs out of S, it runs all these gates in reverse order. Every gate is its own
inverse, so this returns S and every c_i to |0>. Cost: 12m Toffolis and CNOTs
for compute plus uncompute, each charged O(L_a) for its wire addresses, and
2m + 1 ancillas. Every use in this proof has m <= n or m = 2p <= 2n, so the
ancillas are O(n).

## 3. Exact Fourier sampling

LPVSieve obtains labeled qubits with the following exact procedure FS. One copy is
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
   into a fresh (G+g)-bit register A with l_0 multi-controlled XORs (2.2), and
   do the same for K_2(x_2) into a fresh register B. Add them with 2.5
   (m = G+g <= n) into S, copy bits G..G+g-1 of S into a fresh g-bit key
   register with g CNOTs, then uncompute the adder (2.5) and both lookups in
   reverse order. Only the key register is left entangled with (x_1,x_2).
   Measure the key and call the outcome c.

   **Class form of the key.** All K_1(x) are congruent mod 2^G (offset), so
   let rho_1 = K_1(x) mod 2^G, rho_2 = K_2(x) mod 2^G and
   gamma = floor((rho_1 + rho_2)/2^G), which is 0 or 1. For x in [l_0] let
   u(x) = floor((K_1(x) mod 2^{G+g})/2^G) and
   v(x) = floor((K_2(x) mod 2^{G+g})/2^G), both in [0, 2^g). Here mod is the
   nonnegative residue. Since K_1(x_1) mod 2^{G+g} = 2^G u(x_1) + rho_1 and
   likewise for K_2,

   $$
   {\rm key}(x_1,x_2)=\bigl(u(x_1)+v(x_2)+\gamma\bigr)\bmod 2^g. \qquad (4.1)
   $$

2. **Class data (classical, no pair enumeration).** One pass over x_1 in
   increasing order computes u(x_1), the class sizes
   n_1[a] = |C_1(a)| with C_1(a) = {x_1 : u(x_1) = a}, and
   pos_1(x_1) = |{x' < x_1 : u(x') = u(x_1)}|, using one running counter per
   class. A second pass over x_2 gives v, C_2(b), n_2 and pos_2 in the same way. For a in
   [0, 2^g) let a* = (c - gamma - a) mod 2^g be the matching class, and let
   m[a] = n_2[a*]. Let P[0] = 0 and P[a+1] = P[a] + n_1[a] m[a]. By (4.1),

   $$
   J_c=\{(x_1,x_2):{\rm key}=c\}=\bigsqcup_{a<2^g} C_1(a)\times C_2(a^*),
   \qquad |J_c|=P[2^g].
   $$

   If |J_c| < l_0, the step **fails**. A counting sort (one pass, with start
   offsets from the prefix sums of n_1 and n_2) stores each class in increasing
   index order, so the element at position q of C_1(a) is read in one access.
   The rank table is R_1(x_1) = P[u(x_1)] + pos_1(x_1) m[u(x_1)]. It is filled
   without multiplication by walking each sorted class C_1(a) and adding m[a] at
   each step, starting from P[a]. Every value fits in 2p bits: if m[a] > 0 then
   R_1(x_1) < P[a+1] <= P[2^g] <= l_0^2 = 2^{2p}, and if m[a] = 0 then
   R_1(x_1) = P[a] <= l_0^2 - l_0 (pairs outside J_c get a value too, but the
   lookup circuit is a fixed reversible circuit and only J_c is in the support).
   Every table
   has l_0 or 2^g <= l_0/8 entries of O(p) bits.

   **Lemma 4.0 (rank).** Order J_c by class a, then pos_1(x_1), then
   pos_2(x_2). For (x_1, x_2) in J_c, its 0-based rank in this order is
   rank(x_1,x_2) = R_1(x_1) + pos_2(x_2). The map rank is a bijection from J_c
   onto [0, |J_c|), and |J_c| <= l_0^2 = 2^{2p}.

   *Proof.* Let a = u(x_1). Then v(x_2) = a* by (4.1). The classes before a
   contribute P[a] elements. Inside the product C_1(a) x C_2(a*), whose second
   factor has m[a] elements, lexicographic position is the mixed-radix number
   pos_1(x_1) m[a] + pos_2(x_2), with 0 <= pos_2(x_2) < m[a]. QED.

3. **Block code.** Let B = floor(|J_c|/l_0) >= 1 and R_full = B l_0. So
   1 <= l_0 <= R_full <= 2^{2p}. Block b < B is the rank interval
   [b l_0, (b+1) l_0). The remainder is [R_full, |J_c|). Since l_0 = 2^p and
   rank < 2^{2p}, the block of rank rho is its top p bits, rho >> p. Coherently:
   - look up R_1(x_1) into a fresh 2p-qubit register with l_0 multi-controlled
     XORs (2.2, controls x_1). Look up pos_2(x_2) into a fresh 2p-qubit register
     with l_0 multi-controlled XORs (controls x_2);
   - add the two with 2.5 (m = 2p) into a fresh register Rk. On J_c the sum is
     rank < 2^{2p} (Lemma 4.0), so the addition mod 2^{2p} is exact;
   - run the carry chain of the comparator of 2.1 on Rk (register width
     m = 2p, classical b = R_full with 1 <= b <= 2^m), CNOT its final carry
     [Rk >= R_full] directly into the flag qubit f of a fresh (p+1)-qubit code
     register, and run the carry chain in reverse, which clears every carry;
   - CNOT the top p bits of Rk into the other p qubits of the code register;
   - undo the adder and both lookups, in reverse order.

   Only the code register is left entangled with (x_1, x_2). Measure it,
   getting (f, b). If f = 1, the step **fails**. Otherwise b < B is the
   measured block. Reset the code register with X gates on its known 1-bits.
4. **Renumber (two permutations).** Recompute Rk as in step 3 (both lookups and
   the adder). CNOT its low p bits into a fresh p-qubit register I. Then undo
   the adder and the lookups. On block b the low p bits equal
   i = rank - b l_0, which is in [0, l_0). This is the forward permutation
   U_1 : |x_1, x_2>|0> -> |x_1, x_2>|i>.
   For the backward permutation U_2, the controller lists the block
   E = (e_0, ..., e_{l_0 - 1}) with e_i = rank^{-1}(b l_0 + i) in increasing i,
   **without storing it**:
   - find the class a with P[a] <= b l_0 < P[a+1] by one scan of P;
   - set q = b l_0 - P[a] and the start positions
     (pos_1, pos_2) = (floor(q / m[a]), q mod m[a]);
   - then step through the ranks: increment pos_2. At m[a], reset pos_2 to 0
     and increment pos_1. At n_1[a], move to the next class a with
     n_1[a] m[a] > 0 and set (pos_1, pos_2) = (0, 0);
   - read e_i = (C_1(a)[pos_1], C_2(a*)[pos_2]) from the sorted class arrays.

   For each i, apply the multi-controlled XOR "if I = i, XOR e_i into
   (x_1, x_2)". On the block this maps |e_i>|i> to |0>|i>, so (x_1, x_2) returns
   to |0> and is freed. Register I holds the new vector. Its table is
   K(i) = K_1(e_{i,1}) + K_2(e_{i,2}), written as e_i is produced.

   Nothing in steps 2-4 enumerates J_c or any set of l_0^2 pairs. In the most
   concentrated case (all u equal and all v equal) there is one class product,
   R_1(x_1) = pos_1(x_1) l_0 and rank = pos_1 l_0 + pos_2. The block listing
   still visits exactly l_0 elements, plus a scan of at most 2^g classes.

**Lemma 4.1 (exactness).** On success the output is exactly a phase vector of
length l_0 with the stated table and offset G+g.

*Proof.* Phi_1 (x) Phi_2 = l_0^{-1} sum omega^{(K_1+K_2)s}|x_1,x_2>, with all
amplitudes of equal modulus. The key and the block number are functions of the
basis index (Lemma 4.0), so measuring them projects onto a set of basis
indices with equal moduli. U_1 then U_2 map each basis state |e_i>|0> to
|0>|i>, so the new register is exactly the renumbered vector. Elements of J_c share
K_1 + K_2 mod 2^{G+g}, since they share it mod 2^G (offset) and agree on the
next g bits (key). QED.

**Lemma 4.2 (success, distribution-free).** For any tables, the step succeeds
with probability >= 7/16.

*Proof.* Pr[c] = |J_c|/l_0^2. There are at most 2^g <= 2^{l_c} keys, so
Pr[|J_c| < l_0] < 2^{l_c} l_0 / l_0^2 = 2^{l_c}/2^{l_c+3} = 1/8. Given
|J_c| >= l_0, a full block is
hit with probability l_0 floor(|J_c|/l_0)/|J_c| >= 1/2. So the step succeeds
with probability >= (1/2)(1 - 1/8) = 7/16. Only |J_c| and the
fact that the blocks partition J_c are used, so the bound holds for the
canonical order of 4.2. QED.

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
use fresh copies. One attempt then succeeds with probability >= (4/5)^2 * 7/16 =
0.28 (Lemma 4.2), so all 5 attempts fail with probability <= 0.72^5 < 0.1935
< 1/5.
Induct on i. QED.

**Lemma 4.4 (worst-case counts).** Produce(j, D) makes at most 10^D leaf calls
and at most 10^D collimation steps on every branch.

*Proof.* Let L(i) be the maximum number of leaf calls. L(0) = 1 and
L(i) <= 2A L(i-1), so L(D) <= (2A)^D = 10^D. Level-i nodes number at most
(2A)^{D-i}, each with at most A steps, so the step count is at most
sum_{i=1}^{D} A (2A)^{D-i} = A((2A)^D - 1)/(2A - 1) <= (2A)^D. QED.

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

*Proof.* The lemma concerns one final attempt: the call Produce(j, D_j) and
the y-measurement. F does not contain the parity test on w (which comes after y),
the T^a bases or the measurement outcomes o, and it does not contain anything
from other attempts, which use fresh copies. In the ideal world the accepted
leaf labels are i.i.d. uniform on [0, 2^{n-1}), independent of the acceptance
pattern, and since j + 1 <= n - 2 the parts lo, beta and hi of each leaf are
independent and uniform. Write beta = (beta_t) and L = (lo_t, hi_t).

List the events of the attempt in the order they happen: E_1, E_2, ..., E_m.
Each E_u is an acceptance or rejection of a copy, a key outcome, a block-code
outcome, a leaf or step failure, a reset outcome, or (last) y. Their number m
and their kinds are determined by the earlier events. F is the full sequence
(E_1, ..., E_m) together with L.

*Claim.* For every u, the conditional law of E_u given (E_1, ..., E_{u-1}, L,
beta) does not depend on beta.

*Proof of the claim, by induction on u.* Assume E_1, ..., E_{u-1} are fixed.
Then the quantum state before E_u is a product of phase vectors whose tables are
fixed signed sums of leaf labels, chosen by E_1..E_{u-1}. Every vector built
before E_u at level j has offset G <= j. Consider the kinds of E_u in turn.
- An acceptance outcome has probability 2^{n-1}/N, which does not depend on
  any label.
- A key outcome c has probability |J_c|/l_0^2 (Lemma 4.1). J_c is determined by
  the tables mod 2^{G+g}, where G + g = G_{j,i} <= j.
- A block-code outcome (f, b) has probability l_0/|J_c| for each b < B and
  (|J_c| - R_full)/|J_c| for f = 1. Which pairs form block b is fixed by the
  canonical order of 4.2. That order depends only on u, v (the tables mod
  2^{G+g}) and on indices.
- Failures are deterministic functions of the earlier outcomes.
- A reset measures, in the computational basis, a register that is either in a
  known basis state or a phase vector (or qubit) whose basis amplitudes all have
  the same modulus. Its law is fixed or uniform, so it does not depend on any
  label.
- The y outcome is uniform over pairs, because all amplitudes of a phase vector
  have modulus l_0^{-1/2}.

A table mod 2^j is a signed sum of leaf labels mod 2^j, and k mod 2^j = lo. So
every law above is a function of (E_1, ..., E_{u-1}) and the lo parts only.
This proves the claim.

By the chain rule,
Pr[F = f | beta] = Pr[L] * prod_u Pr[E_u = e_u | e_1, ..., e_{u-1}, L],
which does not depend on beta. Hence beta is independent of F, so the beta's are
i.i.d. fair given F.

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

Adding the 1/64 from coupling, LPVSieve outputs s with probability > 1 - 1/64 -
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

**Copies.** A final attempt at level j makes at most 10^{D_j} leaf calls of at
most 8p copies each (Lemma 4.4). Levels 0..n-3 make 4r attempts each. Adding
verification:

$$
Q\le (n-2)\cdot4r\cdot10^{D_{\max}}\cdot8p+\Lambda k_v=Q_{\max}\qquad(n\ge16),
$$

and Q <= N(n+6) <= 21 * 2^15 for n <= 15.

Since 10 <= 2^{10/3} (2^{10} = 1024 >= 1000) and D_max <= (2/3) sqrt n + 1,
10^{D_max} <= 10 * 2^{(20/9) sqrt n}. Also p = O(sqrt n) and r = O(log n), and
Lambda k_v = 2^{(2/3) sqrt n + O(log n)}. Hence
Q = O(2^{(20/9) sqrt n} n^{3/2} log n).

**Work per copy.** Per copy, FS costs n+1 for the copy plus 8 n r_FS tests of
O(n L_a) each. r_FS = O(V + log n) = O(sqrt n), giving O(n^3). Decoding adds
O(n^2 L_a). Total per copy: O(n^3). All copies: O(Q n^3) =
O(2^{(20/9) sqrt n} n^{9/2} log n).

**Work per collimation step.** Here 2^g <= 2^{l_c} = l_0/8.
- Coherent key: 2 l_0 multi-controlled XORs of O(n + p) gates and one
  two-register addition (2.5) of O(n) gates, done and undone.
- Class data: two passes over l_0 table entries, each extracting g bits of an
  (n + O(sqrt n))-bit label and updating O(p)-bit counters. Prefix sums over
  2^g classes with one O(p)-bit product each, O(2^g p^2) = O(l_0 n). Counting
  sorts and the incremental fill of R_1: O(l_0) additions and copies of
  O(p)-bit words, O(l_0 p) bit operations.
- Block code (step 3) and the recomputation in step 4: 2 x 2 x 2 l_0
  multi-controlled XORs of O(p) gates (lookups done and undone, twice), plus
  O(p) gates for 2.5 and the comparator.
- Erasure U_2: l_0 multi-controlled XORs of O(p) gates. Block listing:
  O(l_0 + 2^g) steps on O(p)-bit counters, plus one O(p)-bit division.
- New table: l_0 additions of (n + O(sqrt n))-bit integers.
- Every gate and every bit operation is charged an extra L_a for addressing.

Total: O(l_0 n L_a) = O(2^{l_c} n^{3/2}), since l_0 = 8 * 2^{l_c} and
L_a = O(sqrt n). By Lemma 4.4 there are at most 10^{D_max} steps per final
attempt, and there are 4r(n-2) attempts. Since 2^{l_c} <= 2 * 2^{(3/2) sqrt n}
and 10^{D_max} <= 10 * 2^{(20/9) sqrt n}, all collimation work is

$$
O\!\left(n\log n\cdot2^{\left(\frac{20}{9}+\frac32\right)\sqrt n}\,n^{3/2}\right)=O\!\left(2^{\frac{67}{18}\sqrt n}n^{5/2}\log n\right).
$$

**Other work.**
- Leaf tables: O(l_0 n L_a) per leaf (Gray-code order), and at most 10^{D_max}
  leaves per attempt (Lemma 4.4). This is the same bound as the collimation
  work.
- Final measurements: O(L_a) per attempt.
- Decoder: Lambda anchors x (n-2) levels x r records x O(n^2 L_a) for computing
  w c_0 mod 1 exactly, which is 2^{(2/3) sqrt n} poly(n).
- Verification: Lambda k_v shift tests.
- Parameter computation: poly(n).

The copy work O(2^{(20/9) sqrt n} n^{9/2} log n) is also within the bound,
because 2^{(3/2) sqrt n} >= n^2 for n >= 64. Equality holds at n = 64, and
(3/2) sqrt n - 2 log n is increasing for n >= 16. The finitely many n in
[16, 64) change only the absolute constant. Hence

$$
T=O\!\left(2^{\frac{67}{18}\sqrt n}\,n^{5/2}\log n\right).
$$

**Quantum space.** Depth-first recursion keeps at most one waiting vector
(Phi_1) per node level, which is at most D_max p = O(n) qubits, because
D_max p <= ((2/3) sqrt n + 1)((3/2) sqrt n + 4). The active step uses:
- two vectors: 2p qubits;
- the key: <= l_c qubits;
- the label-sum work registers A, B, S and the 2.5 carries: at most 4n + 1
  qubits;
- the rank lookups, Rk, the 2.5 carries and the comparator carries:
  at most 4(2p) + 2(2p + 1) qubits;
- the code register: p + 1 qubits;
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
- Per-step class data: u, v, pos_1, pos_2, R_1 and the two sorted class arrays
  (l_0 entries each), plus n_1, n_2, m and P (2^g entries each), all of O(p)
  bits. That is O(l_0 p) = O(2^{(3/2) sqrt n} n^{1/2}).
- Listing counters and parameters: O(n).
- No circuit is stored.

So S_C = O(2^{(3/2) sqrt n} n^{3/2}).

## 9. Envelopes and indices

| Resource | Envelope B(n) | Index |
| --- | --- | --- |
| T | 2^{(67/18) sqrt n} n^{5/2} log n | 1/2 |
| S_C | 2^{(3/2) sqrt n} n^{3/2} | 1/2 |
| S_Q | n | 0 |
| Q | 2^{(20/9) sqrt n} n^{3/2} log n | 1/2 |

For T, S_C and Q: log B = a sqrt n + O(log n), where a is the explicit rational
67/18, 3/2 or 20/9 derived in Section 8 from
(3/2) sqrt n <= l_c < (3/2) sqrt n + 1 (the lower bound gives
D_max <= (2/3) sqrt n + 1, the upper bound gives 2^{l_c} <= 2 * 2^{(3/2) sqrt n})
and from 10 <= 2^{10/3}. So log log B / log n -> 1/2. For S_Q,
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
- Collimation in time quasi-linear in l_max = max(l_1, l_2, |J|) is
  Kuperberg 2013, Proposition 4.2 (with QRACM) and Corollary 4.3 (without
  QRACM, via his Proposition 2.2), with the renumbering U_2 U_1. Because l_max
  includes |J|, that bound is quadratic in l_0 for concentrated buckets. The mixed-radix rank over key classes (Lemma 4.0),
  the measured block code and the streamed block listing are written here. They
  keep each step at O(l_0 + 2^g) operations even when |J_c| is close to l_0^2.
- Those papers treat N = 2^n, where the favorable final label 2^{n-1} appears
  with probability 1/2. For general N, the held-out parity (Lemma 5.1) and the
  odd-multiplier anchored decoder (Section 6) replace that step. Both are taken
  from our PVSieve submission 4db17801 and re-proved here.
- Fourier sampling uses Kitaev-style Hadamard tests (arXiv:quant-ph/9511026)
  with T^a offsets, so no rotation synthesis is needed. The shift test and the
  modular adder follow this repository's baseline.
- The coefficients 67/18, 20/9 and 3/2 are what this proof establishes with
  l_c = ceil((3/2) sqrt n), l_0 = 2^{l_c+3} and A = 5. They are not claimed to
  be optimal.

## 12. Comparison with other tuples

**Where the coefficients come from.** With l_c = alpha sqrt n and A attempts
per node, D_max is about sqrt n / alpha and the step cost is 2^{l_c}. So
S_C = alpha, Q = log(2A)/alpha and T = alpha + log(2A)/alpha. A must keep
Lemma 4.3 closed. With l_0 = 2^{l_c+t}, the proved lower bound on
step success is (1 - 2^{-t})/2 < 1/2. The proved per-attempt bound is then below (4/5)^2/2 = 0.32,
and 0.68^4 > 1/5, so A >= 5 for every t. This proof takes t = 3 and A = 5,
giving log(2A) <= 10/3. Requiring S_C <= 3/2 (no worse than PVSieve) and
minimizing T = alpha + (10/3)/alpha over alpha <= 3/2 gives alpha = 3/2,
T = 3/2 + 20/9 = 67/18 and Q = 20/9. This is a statement about this proof's
analysis (child-failure bound 1/5, distribution-free step bound), not a lower
bound for the algorithm.

| Tuple | T | S_C | S_Q | Q | eps |
| --- | --- | --- | --- | --- | --- |
| LPVSieve (this file) | 2^{(67/18) sqrt n} n^{5/2} log n | 2^{(3/2) sqrt n} n^{3/2} | n | 2^{(20/9) sqrt n} n^{3/2} log n | 0 |
| PVSieve, 4db17801 | 2^{(17/3) sqrt n} n^{5/2} log n | 2^{(3/2) sqrt n} n^{3/2} | n | 2^{(8/3) sqrt n} n^{3/2} log n | 0 |
| CS1, f1481815 (claimed, under review) | n^4 log^2 n 2^{a sqrt n}, a just above sqrt 2 | 2^{a sqrt n - n^{1/4}} | n | n^{3/2} log n 2^{a sqrt n} | 0 |
| TC, 04669374 (claimed, under review) | n^7 2^{(1553/736) sqrt n} | n^{3/2} 2^{(23/32) sqrt n} | n | n^3 2^{(32/23) sqrt n} | 0 |

LPVSieve dominates PVSieve. T is strictly smaller (67/18 < 17/3), Q is strictly
smaller (20/9 < 8/3), and S_C, S_Q and the tolerance are identical. It does
**not** dominate CS1 or TC. If either of those proofs is accepted, it is
strictly better than LPVSieve on T, S_C and Q (67/18 > 1553/736 > a and
20/9 > 32/23, a), and equal on S_Q. The CS1 and TC rows are copied from their
public notes. They are not verified here.
