# S31-139: streaming 31-qubit odd-pair recycling before collimation

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single algorithm S31-139 below
receives N in binary and fresh independent copies of rho_s, and outputs the entire s with unconditional
probability at least 1 - 2^-8 > 2/3. On EVERY execution branch (every failure, discard and abort included)
it satisfies jointly

    T = O(2^((139/100) sqrt n)),  S_C = O(2^((139/100) sqrt n)),
    S_Q = O(2^((2/5) sqrt n)),     Q = O(2^((139/100) sqrt n)).

All constants are absolute. Each of the four envelopes has growth index exactly 1/2 (Section 15). The fifth
claim is the clean-input tolerance 0 (Section 16). The sharper main-branch bounds, from which these follow,
are in Section 14. The envelope coefficients are fixed exact rationals; no hidden constant sits inside an exponent.

Notation:
- dn = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known nonnegative integer. log means log2 unless stated otherwise.

Main-branch parameters, computed by exact integer arithmetic for n >= 2^28:

    r = ceil(sqrt n),
    ell = ceil(79 r/200),
    w = floor(399 r/1000),
    m = ceil(929 r/1000),
    dl = ceil(56 r/125),
    kappa = ceil(log2 m) + 1.

So there are ell STREAMING LEVELS, each with a slot table of at most 2^w keys, a collimation tree of depth m,
and leaf tables built from dl qubits. Since r >= 2^14 these satisfy ell >= 2, dl >= kappa + 1, w <= m and
2^kappa >= 2m. The fixed instrument width is k = 31, not a function of n.

## 1. Provenance and what is new

Sections 2-6 and 10-13 follow the latent-label, extraction, linear-merge, free-frequency and 2-adic framework
used by the streaming slot algorithm SPC-138, which itself adapts the same pieces from the linear-merge
collimation framework. Everything needed is restated, so nothing depends on any earlier verdict. Collimation
is from G. Kuperberg, arXiv:1112.3333. Pairing equal low label bits is from G. Kuperberg, SIAM J. Comput.
35(1), 2005. The 31-qubit odd-partition instrument is the fixed cell family whose input/output ratio is
6174015488/2820021981; its completeness identity and dyadic dilation are proved in Section 7, not assumed
from another submission. These citations are context.

New in this submission:
1. Each streaming level holds at most 30 labeled qubits per key, not one. A full group of 31 is consumed by
   one odd-partition instrument call, which can return several good outputs and at most one recycled
   same-level qubit.
2. READY holds only the good outputs of the latest call (at most 14) and is drained before the next call.
   PENDING holds at most one recycled qubit. This keeps every queue inside a constant per key.
3. The schedule uses ell, w, m, dl above. Slot width is about (2/5) sqrt n, and the instrument ratio replaces
   the binary factor 3. Section 8 proves the bit capacity, and Section 14 turns it into the four envelopes.

Why the coefficients. In units of sqrt n let c = log2(6174015488/2820021981) < 113051/100000. A streaming
level of width y removes y bits at cost c in the log of the source, and a tree level removes bits at cost 1.
The explicit choice ell ~ (79/200) r, w ~ (399/1000) r, m ~ (929/1000) r, dl ~ (56/125) r makes both the
source exponent and the table exponent strictly less than 139/100, while the quadratic capacity exceeds n.
This paragraph is motivation; the theorem uses the inequalities of Sections 8 and 14.

## 2. Model and counting conventions

A CORE STEP is one of: a NOT/CNOT/Toffoli/H/S/S^dagger gate; a computational-basis
single-qubit measurement or reset; a Boolean operation on at most three classical bits; a
classical bit read or write. Toffoli has an exact constant-size Clifford+T decomposition.
Integers are bit strings; an L-bit addition, comparison or copy costs O(L) core steps.
Generating a gate costs O(1) core steps. Each core step additionally pays its address,
ceil(log2(Mem+2)) bit operations, where Mem <= S_C + S_Q is the number of allocated bits and
qubits. Gates on slot qubits are classically addressed through this charge; there is no
quantum-addressed memory and no QRAM. A source acquisition costs n+1. Hence

    T <= (number of core steps) * (1 + ceil(log2(S_C+S_Q+2))) + (n+1) Q.          (2.1)

## 3. Source identities, the latent-label model and data transforms

Let chi_k = N^(-1/2) sum_u omega^(k u)|u> and phi_k(s) = (|0> + omega^(-k s)|1>)/sqrt 2.
Substituting |u> = N^(-1/2) sum_k omega^(-k u) chi_k into rho_s = (1/N) sum_x |psi_x><psi_x|,
with psi_x = (|0,x> + |1,x+s>)/sqrt 2, gives

    rho_s = (1/N) sum_(k=0)^(N-1) |phi_k(s)><phi_k(s)| (x) |chi_k><chi_k|,          (3.1)

because the cross terms k != k' carry (1/N) sum_x omega^(-(k-k')x) = 0.

Latent-label model. By (3.1) each copy is a convex mixture, with uniform weights, of the
product states phi_k(s) (x) chi_k. The whole algorithm is a linear adaptive quantum instrument
on independent copies. So the joint law of all classical outcomes equals the law obtained by
first drawing, per copy, an independent uniform latent label k and then running on
phi_k(s) (x) chi_k. All probabilities below use this model. Applying X to the control maps
phi_k(s) to, up to a global phase, the POSITIVE qubit pq_k(s) = (|0> + omega^(k s)|1>)/sqrt 2.

Two exact data transforms act on a fresh copy before label extraction. Each is a permutation
of all 2^n data encodings, extended by the identity on encodings >= N, and maps the copy
exactly to rho_s' for a known s'. The latent label of a copy is the Fourier label of its
TRANSFORMED data register.

(T1) Mult_alpha: u -> alpha u mod N, for known alpha coprime to N. Since x -> alpha x is a
bijection of Z/NZ, the copy becomes exactly rho_(alpha s). It uses n controlled modular
additions of the constants alpha 2^v mod N into a clean register, a swap, and the inverse
computation with alpha^(-1): O(n^2) core steps and O(n) scratch.

(T2) Shift_c: if the control is |1>, replace u by u - c mod N, for known c. Since |1,x+s>
becomes |1,x+(s-c)>, the copy becomes exactly rho_(s-c). This takes O(n) core steps.

Modular addition of a known constant in [0,N) is a ripple comparison with N, an addition, a
comparison and a selector. It is the identity on encodings >= N, uses O(n) Boolean gates, and
is computed cleanly: compute, swap or XOR out, uncompute.

## 4. Rational trigonometric table

For v in [0,4096) the controller computes rationals Cos[v], Sin[v] within 2^-20 of
cos(2 pi v/4096) and sin(2 pi v/4096): bound pi within 2^-90 with Machin's formula
pi = 16 atan(1/5) - 4 atan(1/239), summing 40 terms of each alternating series (tails below
2^-91); at the angle 2 v p_mid/4096 < 7, with p_mid the midpoint of the pi bounds, sum 80 Taylor
terms (remainder <= 7^81/81! < 2^-170; angle error < 2^-89; sin and cos are 1-Lipschitz); round
to denominator 2^20. This is a fixed finite computation, an absolute constant, not advice.

For x in [0,1) put tab_0(x) = Cos[floor(4096x)], tab_1(x) = Sin[floor(4096x)], and let
cs_0(x) = cos(2 pi x), cs_1(x) = sin(2 pi x). Since cs is 2pi-Lipschitz,

    |tab_beta(x) - cs_beta(x)| <= 2 pi/4096 + 2^-20 < 1/625.                        (4.1)

## 5. Label extraction LE

Input: a data register holding chi_k for latent k, beside arbitrary spectators. Let Qcap be the
source cap of Section 13. Parameters: J_e = n + 4, h_e = ceil(log2(Qcap (n+5))) + 12,
F = 2^21 h_e.

Translation Tr_c: u -> u + c mod N satisfies Tr_c chi_k = omega^(-k c) chi_k. A TEST AT LEVEL j
prepares an ancilla in |+>, applies Tr_((N - 2^j) mod N) controlled by it, so that the |1> branch
gets eigenvalue omega^(k 2^j), and measures the ancilla in X (H then Z) or Y (S^dagger, H, then Z).
The +-1 outcome has mean cos(2 pi 2^j k/N) or sin(2 pi 2^j k/N). Conditioned on k, chi_k and every
spectator are unchanged and outcomes are independent. Each test costs O(n) core steps.

For each j = 0..J_e take F tests per basis, giving empirical means x_j and y_j.

Decoding a level. Pick the least dr in [0,64) maximizing x_j Cos[64 dr] + y_j Sin[64 dr]. If both
means are within 1/1024 of their expectations, each computed dot product differs from
cos(2 pi (2^j k/N - dr/64)) by at most 2/1024 + 2^-19 < 1/256. The nearest direction has true dot
>= cos(pi/64) >= 511/512. Any direction at circular distance >= 1/16 has dot <= cos(pi/8) <= 31/32.
The gap 15/512 exceeds 2/256, so alpha_j = dr/64 is within circular distance 1/16 of 2^j k/N.

Unwrapping. Set g_(J_e) = alpha_(J_e). For j = J_e - 1 down to 0, let g_j be whichever of g_(j+1)/2
and (g_(j+1)+1)/2 (mod 1) is circularly closer to alpha_j (ties: the first). If g_(j+1) is within
e < 1/16 of 2^(j+1) k/N, the correct preimage is within e/2 of 2^j k/N, hence within
1/16 + e/2 < 3/32 of alpha_j, while the other is more than 13/32 from alpha_j. So the choice is
correct and the error halves. Finally g_0 is within 2^-(n+8) < 1/(2N) of k/N, and LE outputs
floor(N g_0 + 1/2) mod N = k. On any input LE returns a value in [0,N) after its fixed number of
tests, and then resets the data register. It uses no Fourier transform, no lookup, and no rotation
other than H and S.

Concentration. For F independent +-1 variables the centered log-moment generating function has
second derivative at most 1 and vanishes with its first derivative at 0. Hence
Pr(|mean - E mean| > delta) <= 2 exp(-F delta^2/2). With delta = 1/1024 and F = 2^21 h_e this is
2 exp(-h_e). So LE errs with probability at most 4(n+5) e^(-h_e), uniformly in k and in the adaptive
schedule. Over at most Qcap calls, the probability that ANY call returns a wrong label is at most

    4 (n+5) Qcap 2^(-h_e) <= 2^-10.                                                (5.1)

Cost per call: 2(J_e+1)F tests, O(n^2 h_e) core steps. Since log2 Qcap = O(sqrt n) (Section 14),
this is O(n^(5/2)) core steps per call, with O(n) quantum scratch and O(n) classical bits.

IDEAL run. The ideal run is this algorithm in the latent-label model with every LE output replaced by the
latent k. Actual and ideal runs can be coupled to coincide unless some LE call returns a wrong
label, so every event's probability differs by at most 2^-10. Resource bounds are proved for every
ACTUAL branch directly, because they rest only on caps and fixed allocations.

## 6. Phase vectors and the linear merge

A PHASE VECTOR of length 2^lam is a lam-qubit index register with a classical label table
lab[0..2^lam). In the ideal run its state is 2^(-lam/2) sum_x exp(2 pi i lab[x] th) |x>, up to a
global phase, for a fixed real th. Labels are nonnegative integers. The vector is COLLIMATED TO p
if all lab[x] are congruent modulo 2^p. Labels are stored in full, in fixed fields of 3n bits, which
suffices by Section 9 (label bound).

### 6.1 Lookups

LOOKUP(tab), for a classical table of E rows with w-bit entries, XORs tab[x] into a clean w-bit
register, controlled by a lam-qubit index x. For each row x0 it computes the flag [x = x0] with a
Toffoli chain on O(lam) scratch, applies CNOTs from the flag to the output bits where tab[x0] has a
1, and uncomputes the chain. Indices outside [0,E) give output 0. The circuit is its own inverse,
has O(E (lam + w)) gates and O(lam + w) qubits, and is generated by reading each table bit once.

### 6.2 MERGE(X1, X2; p, b, lam'), for b >= 0

Precondition: X1 and X2 are phase vectors from disjoint sets of qubits, both of length 2^lam,
collimated to p, with index registers x, y and tables al, be. Let cA = al[0] mod 2^p,
cB = be[0] mod 2^p, car = floor((cA + cB)/2^p), aa[x] = floor(al[x]/2^p) mod 2^b and
bb[y] = floor(be[y]/2^p) mod 2^b. Then bits p..p+b-1 of al[x] + be[y] equal (aa[x] + bb[y] + car)
mod 2^b. (If b = 0 the residue registers below are empty and e = 0.)

1. LOOKUP aa into a fresh b-bit register Ru and bb into Rv. Add Ru + Rv + car (mod 2^b) cleanly into
   a fresh Rz, and clear Ru and Rv by repeating both lookups. Measure Rz, obtaining e, and reset Rz.
2. Classical. Let S_e = {(x,y) : aa[x] + bb[y] + car = e mod 2^b} and sz = |S_e|. Merge-sort the
   indices y by key (bb[y], y) into order[]; pos[y] is the position of y. For each x the partners y
   form one contiguous run of order[], the class (e - car - aa[x]) mod 2^b; find its start lo[x] and
   length cnt[x] by binary search. Put off[x] = sum_(x' < x) cnt[x'] and
   rank(x,y) = off[x] + pos[y] - lo[x], a bijection from S_e onto [0, sz). If sz < 2^lam', declare FAIL.
3. Let R have 2 lam + 1 bits. LOOKUP pos into Rp and Dx[x] = (off[x] - lo[x]) mod 2^(2lam+1) into Rd.
   Add Rp + Rd (mod 2^(2lam+1)) cleanly into a fresh R, and clear Rp and Rd by repeating the lookups.
   On S_e, R = rank(x,y).
4. Measure bl = floor(R / 2^lam'). If (bl+1) 2^lam' > sz, declare FAIL.
5. Classical. For v in [0, 2^lam'), find the unique (x_v, y_v) with rank bl 2^lam' + v, in one scan
   over x with running offsets. Apply LOOKUP v -> (x_v, y_v) on the low lam' bits of R, XORing into the
   registers x and y, which become |0>. Reset the high bits of R from their known value bl.
6. Output the low lam' bits of R as the index register, with table lab[v] = al[x_v] + be[y_v].

On FAIL, both inputs are reset and released and never reused.

Correctness (ideal run). Before step 1 the state is X1 (x) X2: equal magnitudes over all pairs (x,y),
with phases 2 pi (al[x] + be[y]) th. Steps 1 and 3 compute functions of (x,y) into clean registers and
measure them. So after step 4 the state is the equal-magnitude superposition over the 2^lam' pairs of
block bl, with their original phases. Step 5 maps (x_v, y_v) to v bijectively. The output is a phase
vector with table lab, and every label is congruent to cA + cB + 2^p ((e - car) mod 2^b) modulo
2^(p+b), so it is collimated to p+b.

Lemma 6.1 (distribution-free failure). For ANY input tables collimated to p, the measurement law in
steps 1 and 4 depends only on aa, bb and car (label bits below p+b), and Pr[FAIL] <= 2^(b + lam' - 2 lam).

Proof. Each measurement is a computational-basis measurement of a function of (x,y) on an
equal-magnitude superposition, so its outcome probabilities are ratios of counts, independent of the
phases. Outcome e has probability sz_e / 2^(2lam). Given e, the measured rank is uniform on [0, sz_e).
So FAIL has conditional probability rem_e / sz_e with rem_e = sz_e mod 2^lam' (this also covers
sz_e < 2^lam'). Hence Pr[FAIL] = sum_e rem_e / 2^(2lam) <= 2^b (2^lam' - 1) / 2^(2lam). QED.

Cost. Write L = 2^lam, L' = 2^lam'. With lam, b = O(sqrt n): nine lookup passes of O(L + L') rows with
O(sqrt n)-bit fields; O(L lam) comparisons of O(sqrt n)-bit keys; O(L) binary searches; O(L') additions
of 3n-bit labels. In total O(n (L + L')) core steps. Quantum scratch is O(sqrt n) beyond the index
registers. Classical scratch is O((L + L') n) bits.

## 7. The 31-qubit streaming instrument

A LABELED QUBIT is a phase vector of length 2 with table (t0, t1); write Del = t1 - t0. It is COLLIMATED TO p
if Del = 0 mod 2^p. Throughout a level, pp is that level's collimation and c = pb is its key width. The key of
a qubit is floor((Del mod 2^(pp+c)) / 2^pp), read from the low pp+c bits of the two table entries.

### 7.1. The cell family

Fix k = 31 and h = 15, and w_cell-weight w = 1/(h(h+1)) = 1/240, once and for all. An A-cell chooses one
unordered pair of coordinates and leaves the other 29 free. There are C(31,2) = 465 such cells, each of weight
w. For j = 0, ..., 14, a J_j-cell partitions all 31 coordinates into j unordered pairs and one all-equal group
of size 31 - 2j. Its weight is

    w_j = (1 - w j (31 - j)) (31 - 2j)! / (31 - j)!.

The sixteen weights w and w_0, ..., w_14 are the fixed positive rationals

    1/240, 1, 7/240, 13/13920, 1/30240, 11/8424000, 1/17222400, 1/340032000,
    1/5814547200, 1/84726259200, 1/1031450112000, 1/10239486566400,
    1/80453108736000, 1/482718652416000, 1/2134124568576000, 1/7113748561920000

in the order A, then j = 0 through 14. The cell count is N_j = 31! / (2^j j! (31-2j)!). Cells are enumerated
by that order and then by lexicographic pair lists; the remaining group is the complement. This names each
cell once.

Pi_cell is the computational-basis projector onto the cell's constraints. Completeness is an identity, not a
search. For a basis vector x of minority Hamming weight t <= 15 there are t(31-t) A-cells containing x. A
J_j-cell contains x only for j = t when t < 15, and the number of such cells is (31-t)! / (31-2t)!. For t = 15,
w * 15 * 16 = 1 and no J-cell contains x. For t < 15,

    w t (31-t) + ((31-t)! / (31-2t)!) w_t = w t (31-t) + (1 - w t (31-t)) = 1,

by substituting the formula for w_t. All weights are nonnegative, so sum_cell w_cell Pi_cell = I on every
basis vector and hence on every joint state with a reference. The operators sqrt(w_cell) Pi_cell are the
instrument.

On a product of 31 equatorial phase qubits the probability of a fixed cell with L free binary components is
w_cell 2^(L-31), independent of the phases, the labels, the secret and the past. For an A-cell, L = 30, so the
total A probability is 465 w / 2 = 31/32. For J_j, L = j+1 and

    P_j = N_j w_j 2^(j+1-31) = 2^(-30) C(31,j) (1 - w j (31-j)).

These sixteen probabilities, P_A = 31/32 and P_0, ..., P_14, sum to 1 because the projectors resolve the
identity. Directly, they are the rationals

    31/32,
    1/1073741824, 217/8589934592, 2821/8589934592, 11687/4294967296,
    69223/4294967296, 623007/8589934592, 2208843/8589934592, 1577745/2147483648,
    3681405/2147483648, 28224105/8589934592, 44352165/8589934592, 28224105/4294967296,
    28224105/4294967296, 41250615/8589934592, 17678835/8589934592

and their sum is 1. Write p = E[G] and mu = E[C] for the random type drawn with these probabilities, where an
A outcome has G = 1 and C = 2, and a J_j outcome has G = j and C = 30. Summing the sixteen terms gives

    p = 2820021981/2147483648,   mu = 23/8,
    q = mu/p = 6174015488/2820021981.

The two comparisons

    6174015488^2000 > 2^2261 * 2820021981^2000,
    6174015488^100000 < 2^113051 * 2820021981^100000

are fixed integer facts (verified by binary exponentiation). They are exactly

    2261/2000 < log2 q < 113051/100000.

G lies in {0, 1, ..., 14}. No independence of G and C is used beyond this joint law.

On a constrained group the canonical pattern b is: in a pair, the smaller index is 0 and the larger is 1; in an
all-equal group, b is all zeros. The output table on the surviving wire v (the smallest index of the group) is
the sum of the selected input tables. CNOT from v onto the other wires of the group, with X on wires whose
pattern bit differs, zeros those wires and leaves v holding the output phase qubit. Different groups are
disjoint, and free inputs of an A-cell are untouched. An odd pair is GOOD: equal keys make the output
difference divisible by 2^(pp+c), so the output is collimated to pp+c. An all-equal group is RECYCLED at the
old collimation pp. Thus an A outcome emits one good qubit and returns 29 unchanged qubits of the same key; a
J_j outcome emits j good qubits and one recycled qubit, and zeros the other wires. Every output entry is a sum
of input entries on a disjoint set of leaves, and the pattern map on each group is injective. Product inputs
remain a product of phase qubits.

### 7.2. Dyadic dilation

Let D be the least common multiple of 240 and the fifteen denominators of w_j. Integer Euclid gives
D = 270457606575636480000. Set M = 2^70, scale = floor(M/D) = 4 and R = M - scale D = 98761194414865383424.
Give each cell scale D w_cell distinct tokens, and add R global identity tokens. Each basis vector lies in
exactly M tokens. The number of non-identity outcome ids is below 2^86.

Prepare a 70-qubit coin r and an 86-qubit outcome j in zero, and apply 70 Hadamard gates to r. Let f(x, r) be
the r-th token containing x, and h(x, j) its rank among tokens containing x (or 0 if j does not contain x).
XOR f into j, XOR h into r, uncompute scratch, and measure j. An identity token leaves the 31 data qubits
unchanged. Any other token applies the group cleanup of Section 7.1 for its cell.

Both f and h are fixed Boolean functions of at most 117 bits. For each target bit, enumerate the fixed input
patterns, compute the equality flag by a NOT/Toffoli chain, copy the bit, and uncompute the flag. At most
86 * 2^101 + 70 * 2^117 such terms, each of length at most 5*117+1, occur, which is < 2^144 elementary gates.
Scratch is at most 256 qubits, so the private coin, outcome and scratch together use fewer than 512 qubits.
All of them are reset. There is no QRAM and no rotation outside Clifford+T. Toffoli has its standard
constant-size Clifford+T completion. A trial also spends at most 2^512 n core steps on the fixed enumeration
counters, gate emission and O(n)-bit wire staging; this constant does not grow with N.

The rank bijection makes each non-identity Kraus operator exactly Pi_cell / sqrt(M), and the aggregate
identity operator I/sqrt(M) with R/M < 1/4. Conditioning on a non-identity token restores the weights w_cell.

Each macro tries the dilation at most Ltry = Y + ceil(log2 n) + 64 times and then ABORTs the batch if every
trial was an identity. Y is defined in Section 8 and satisfies Y <= 2r on the main branch, so Ltry <= 4r.
The probability of Ltry identities on one macro is < 4^(-Ltry). On the main branch Ltry >= Y + 64 and
2^Y >= Ccap, so 4^(Ltry) >= 2^(2Y + 128) >= Ccap^2 * 2^128. At most n(Ccap + 1) macros start on a branch
that has not already aborted, and

    n (Ccap + 1) 4^(-Ltry) <= 2 n / (Ccap 2^128).

Also Ccap >= 2^13 n 2^m and m >= 929 r/1000 >= r/2, so 2n/Ccap <= 2^(-12 - r/2) <= 2^-128. An abort stops
the batch. The analysis ideal run deletes only
this identity cap; its conditional law on non-identity is Section 7.1. No trial acquires a source copy.

### 7.3. Streaming levels

Level i, 0 <= i < ell, has collimation position pp_i, width pb_i <= w, and E_i = 2^(pb_i) keys. SLOT_i[key]
holds at most 30 labeled qubits. READY_i holds at most 14 good outputs of the latest macro. PENDING_i holds
at most one recycled qubit. All three start empty.

NEXT(0) asks the batch supplier for one leaf qubit, table (0, k). NEXT(i) for i >= 1 does the following,
with lev = i-1.

    if READY_i is nonempty: pop and return its front qubit
    if PENDING_i is nonempty: item = PENDING_i; clear PENDING_i
    else: item = NEXT(lev)
    append item to SLOT_i[key(item)]
    if that list now has fewer than 31 qubits: repeat from the top
    take those 31 qubits (the list is now empty) and run one macro
    append its good outputs to READY_i, at most 14
    if the outcome is an A-cell: write its 29 unchanged qubits back into that same key
    if the outcome is a J-cell: store its single recycled qubit in PENDING_i
    repeat from the top

The same-key write of an A-cell happens only after that key was emptied, and 29 <= 30, so the list does not
immediately fire again. PENDING_i is read only when READY_i is empty, so a later insertion fires at most one
new macro into an empty READY_i. Therefore READY_i never holds more than one macro's goods, and no slot list
ever holds more than 30 qubits after a line of this procedure returns.

Lemma 7.1 (outputs). In the ideal run, conditional on the 31 input qubits being a product of labeled phase
qubits and on the entire past, a non-identity macro has the type law of Section 7.1. Each good output is
collimated to pp_i + pb_i. Each unchanged or recycled qubit is collimated to pp_i. The type is independent of
all labels and of the secret.

Proof. Section 7.1 gives the type law and the collimation of a difference of two equal keys, and of an
unchanged wire. The dilation of Section 7.2 implements that law. QED.

Lemma 7.2 (memory). On every branch: (a) every stored, pending or ready qubit at level i is collimated to
pp_i, and every qubit returned by NEXT(i) for i >= 1 is collimated to pp_i = pp_(i-1) + pb_(i-1), with
pp_0 = 0. (b) Level i holds at most 30 E_i + 14 + 1 + 31 data qubits, plus fewer than 512 instrument
ancillas while a macro is in progress. (c) Across the depth-first stack of levels, at most one NEXT frame
is inside a macro, so the pairing stage holds at most

    512 + sum_(i<ell) (30 E_i + 46)

qubits. (d) Keys and pattern bits read only label bits below pp_i + pb_i.

Proof. (a) is Lemma 7.1 and induction down the supplier. (b) and (c) are the queue bounds above: a caller
stores its item or empties READY before the recursive call, and only one macro runs at a time. (d) is the
definition of the key. QED.

Lemma 7.3 (flow). On any branch let A_i be the number of qubits that enter level i from below (supplier calls
for i = 0, returns of NEXT(i-1) for i > 0), let M_i be the number of non-identity macros at that level, let
d_j and gamma_j be the removal count C and the good-output count G of macro j, let L_i be the number of qubits
sitting in SLOT_i or PENDING_i or the current item, and let R_i = |READY_i|. Then

    A_i = sum_(j<=M_i) d_j + L_i,     L_i <= 30 E_i + 2,
    sum_(j<=M_i) gamma_j = A_(i+1) + R_i,     R_i <= 14,

with A_ell equal to the number of qubits delivered to the tree. In particular A_(i+1) <= A_i, and
sum_i A_i <= ell A_0. In the ideal run, for any stopping time at which the number of macros is bounded,

    E[A_i] <= q E[A_(i+1)] + 14 q + 30 E_i + 2.                                  (7.3)

Proof. Every arrival is either still in the level (L_i) or was removed by a macro. A macro's removal count
is exactly C: 2 for A (31 enter, 29 return to the slot) and 30 for J (31 enter, 1 is pending). Good outputs
are either still in READY or have been returned upward, which is the definition of A_(i+1). The numerical
caps are Lemma 7.2. For the expectation, each non-identity macro has E[d_j - q gamma_j] = 0 and the pair
(d_j, gamma_j) is independent of the past and of the labels, by Lemma 7.1. The centered sum up to a bounded
stopping time is a martingale with mean zero, so E[sum d] = q E[sum gamma]. Substitute the two identities
and R_i <= 14, L_i <= 30 E_i + 2. QED.

No property of the label distribution is used. Recycled sums may have even residues; they are just new
arrivals at the same level.

Cost. A store, a key computation or a table update is O(n) core steps and is charged to an arrival. A macro
costs at most Ltry trials, each < 2^144 gates and at most 2^512 n core steps, hence at most 2^520 n r core
steps on the main branch. Since each macro removes at least 2 qubits, M_i <= A_i/2. The stage therefore
costs O(2^520 n r A_0 + n sum_i E_i) core steps. The factor 2^520 is an absolute constant.

## 8. The schedule

Demand constants, with K from (11.0):

    Dbar = 3 K 2^m dl,    Dcap = 2^12 n Dbar,
    Ccap = 2^13 n * 2^(ceil(113051 ell / 100000)) * Dbar.

Let Y be the least integer with 2^Y >= Ccap. The exponent ceil(113051 ell / 100000) is computed by integer
division. Because log2 q < 113051/100000,

    q^ell < 2^(113051 ell / 100000) <= 2^(ceil(113051 ell / 100000)).               (8.0)

Size bound. ell <= 79 r/200 + 1 and m <= 929 r/1000 + 1, and K <= 3 * 2^13 r because
2r + ceil(log2 n) + 30 <= 3r for r >= 2^14. Also dl <= r and n <= r^2. Hence

    log2 Ccap <= (113051/100000)(79/200) r + 113051/100000 + 929 r/1000 + 1
                 + log2(Dbar / 2^m) + log2(2^13 n) + 1.

And log2(Dbar / 2^m) = log2(3 K dl) <= 2 log2 r + 20. For r >= 2^14,

    log2 Ccap <= (27511029/20000000) r + 6 log2 r + 40 <= (7/5) r.                 (8.1)

The coefficient 27511029/20000000 = 1.37555145 is (113051/100000)*(79/200) + 929/1000. Thus Y <= 2r <= n
and 2^Y <= 2 Ccap. Also 2^m >= 64 ell, so every slot bound below is nonnegative.

Level capacities.
- Streaming level i (0 <= i < ell): width at most w.
- Tree: lam_i = dl + i for 0 <= i <= m-1, lam_m = 1; tbmax_i = dl + i - kappa - 1 for 0 <= i <= m-2;
  tbmax_(m-1) = 2(dl + m - 1) - kappa - 1.

For every b_i <= tbmax_i,

    b_i + lam_(i+1) - 2 lam_i <= -kappa.                                            (8.2)

Lemma 8.1 (capacity). For n >= 2^28, hence r >= 2^14: ell w + sum_i tbmax_i >= r^2 >= n.

Proof. The same expansion as a depth-m merge tree gives

    sum_i tbmax_i = m dl + m^2/2 + dl + m/2 - 1 - m (kappa + 1)
                  >= m dl + m^2/2 - m (kappa + 1).

Also ell >= 79 r/200 and w >= 399 r/1000 - 1, so

    ell w >= (79/200)(399/1000) r^2 - 79 r/200.

With m >= 929 r/1000 and dl >= 56 r/125 the quadratic terms total at least

    ( (79/200)(399/1000) + (929/1000)(56/125) + (929/1000)^2 / 2 ) r^2
      = (402127/400000) r^2.

The subtracted terms are at most 79 r/200 + m (kappa + 1). For r >= 2^14 one has m <= r,
kappa + 1 <= log2 r + 3, and 79/200 < 1, so the loss is at most r (log2 r + 4). The surplus coefficient
is 402127/400000 - 1 = 2127/400000, and

    (2127/400000) r >= log2 r + 4

holds at r = 2^14 (348.5 >= 18) and thereafter because its derivative 2127/400000 exceeds 1/(r ln 2).
Therefore the net capacity is at least r^2. QED.

Bit allocation. Given integer B with 1 <= B <= n, allocate exactly B bits greedily: first pb_0, ..., pb_(ell-1),
each pb_i = min(w, bits still unallocated), then tb_(m-1), ..., tb_0 with tb_i = min(tbmax_i, bits still
unallocated). By Lemma 8.1 this exhausts B. Positions: pp_0 = 0, pp_(i+1) = pp_i + pb_i; tp_0 = pp_ell,
tp_(i+1) = tp_i + tb_i; so tp_m = B. Every bit read below has position below B.

## 9. BATCH(supplier, B)

Input: a supplier of leaf qubits, positive qubits with phase exp(2 pi i k th) for a fixed real th and a known
label k. In the ideal run the labels are independent and uniform on [0, 2^(B+1)). Output: K roots, or ABORT.
A batch starts with empty slots, READY and PENDING, and an acquisition counter. If an acquisition would exceed
Ccap, the batch ABORTs. At the end, every stored qubit is measured and released.

TREE. VEC(0) requests dl qubits by calling NEXT(ell) dl times, counting each in a counter D. If D would exceed
Dcap, ABORT. These qubits form the index register. With tables (t0_j, t1_j), set lab[0] = sum_j t0_j and
lab[x + 2^j] = lab[x] + t1_j - t0_j for x < 2^j. The table has length 2^dl and, in the ideal run, is the
tensor product. It is collimated to tp_0 because every difference is 0 mod 2^(tp_0). VEC(i) for i >= 1
repeats X1 = VEC(i-1), X2 = VEC(i-1), out = MERGE(X1, X2; tp_(i-1), tb_(i-1), lam_i) until out != FAIL, and
returns out. A root is VEC(m), evaluated depth-first, K times.

Root. VEC(m) is a two-entry table with lab[0] = lab[1] mod 2^B, so its ideal state is, up to global phase,

    (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2,   W = (lab[1] - lab[0])/2^B.            (9.1)

Label bound. Each leaf enters at most one output line of each macro, and a batch has at most Ccap leaves.
Every label is a sum of at most Ccap leaf labels, each below 2^(B+1), so every label is below 2^(Y+n+1).
This fits in 3n bits because Y <= n, and

    |W| <= 2 Ccap <= 2^(Y+1).                                                       (9.2)

Lemma 9.1 (no abort). Suppose each supplied acquisition yields a leaf qubit independently with probability at
least 1/2, given the past. In the ideal run a batch ABORTs with probability at most 2^-12/n + 2^-11/n.

Proof. Consider the same process with no caps. Every NEXT call returns after finitely many macros: each macro
that emits no good output still removes at least 2 qubits from a finite arrival stream once the supplier is
uncapped, and a macro with a good output fills READY. By (8.2) and Lemma 6.1 each merge fails with conditional
probability at most 2^(-kappa) given everything before it, including all streaming activity. Let V_i bound the
expected number of qubits requested by VEC(i). Then V_0 = dl and, by Wald, V_(i+1) <= tt * 2 V_i with
tt = 2^kappa / (2^kappa - 1). Since 2^kappa >= 2m, tt^m <= exp(m/(2m-1)) <= e < 3. So the demand D_inf of K
roots has E[D_inf] <= Dbar, and Markov gives Pr[D_inf > Dcap] <= 2^-12/n.

Stop the uncapped process when the batch finishes or the acquisition counter reaches Ccap. This bounds the
number of macros. At that time A_ell <= D_inf. Iterate (7.3). For w >= 4 and q < 3,

    E[A_0] <= q^ell E[D_inf] + (14 q + 30 * 2^w + 2) (q^ell - 1)/(q - 1)
           <= q^ell Dbar + 33 * 2^w * q^ell
           <= q^ell Dbar (1 + 33 / (3 dl)).

On the main branch dl >= 56 * 2^14 / 125 > 2^12, so 33/(3 dl) < 1/100 and E[A_0] <= (101/100) q^ell Dbar.
Accepted acquisitions are at most twice that in expectation, by Wald and the 1/2 acceptance bound:
E[acq] <= (101/50) q^ell Dbar < 3 q^ell Dbar. By (8.0),

    Ccap >= 2^13 n q^ell Dbar,

so Markov gives Pr[acq > Ccap] <= 3 / (2^13 n) < 2^-11/n. The real run coincides with the uncapped one until a
cap triggers. The identity-abort event of Section 7.2 is at most 2^-128 and is absorbed in the same 2^-11/n.
QED.

## 10. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and tau_j in {0,1}. Since k_j is uniform on
[0, 2^(B+1)), low_j and tau_j are independent and tau_j is a fair bit. For a batch let G be the sigma-field generated
by: all low_j of its leaves; all instrument outcome ids and cell types; all merge outcomes (e, bl); and all decisions of the controller in
that batch (slot stores, READY and PENDING updates, FAIL and retries, aborts, assignment of qubits). G does not include
root measurement outcomes, which no decision in the batch reads. It also excludes LE's internal coins and outcomes,
which in the ideal run feed no decision.

Lemma 10.1. In the ideal run, conditional on G and on all independent randomness outside the batch, the top bits tau_j
are i.i.d. fair.

Proof. Induct over the controller's steps. Every slot key, residue, sort, rank and block partition reads only label bits
strictly below position B, because all positions used are below B (Section 8). Bits below B of a sum of leaf labels,
and of a difference modulo 2^(pp_i+pb_i) with pp_i+pb_i <= B, depend only on the low_j, since multiples of 2^B do not change them.
Instrument types are independent of all labels (Lemma 7.1). By Lemma 6.1 each merge outcome's conditional law, given
labels and earlier outcomes, is a function of the low_j and earlier outcomes only. So the joint law factorizes as
law(tau) x law(low) x law(outcomes and decisions | low). QED.

Incidence. An entry of a table is the sum over leaves j of x_j k_j, for a 0/1 incidence vector x. Distinct indices of a
table have distinct incidence vectors: this holds for a leaf qubit, table (0, k_j); a macro writes each output as an injective pattern-sum on a disjoint
group of inputs (Section 7.1), so each leaf appears in an output with coefficient +1 or -1 at most once; a LEAF table concatenates disjoint coordinates; and a merge re-indexes injectively pairs on disjoint
coordinates. So the two root entries have x0 != x1, and with hd = |x0 xor x1| >= 1,

    W = cst + sum_(j in Sp) tau_j - sum_(j in Sm) tau_j,                            (10.1)

where cst = (sum_j low_j (x1_j - x0_j))/2^B is a G-measurable integer, and Sp, Sm are disjoint G-measurable sets with
|Sp| + |Sm| = hd. Each leaf enters at most one root, so given G the W's of distinct roots of a batch are independent.
Since E exp(2 pi i phi tau) = e^(i pi phi) cos(pi phi) for a fair bit, for every real phi

    | E[ exp(2 pi i phi W) | G ] | = |cos(pi phi)|^hd <= |cos(pi phi)|,             (10.2)

and, with phi = 1/2, Pr[W odd | G] = 1/2.                                           (10.3)

## 11. Odd part: s1 = s mod M by free-frequency decoding

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so dn - 1 >= a2. Put theta = s1/M. Every stage uses
B = dn - 1 (B >= 1 on the main branch) and

    K = 2^13 (2r + ceil(log2 n) + 30).                                              (11.0)

The stages are j = 0, ..., J, where J = min{ j >= 0 : 2^(j+3) > 2M }. Then J + 1 <= log2 M.

Supplier for stage j. Compute alpha_j by extended Euclid and CRT so that alpha_j = 1 (mod 2^a2) and
alpha_j = 2^j (2^(dn-1-a2))^(-1) (mod M); it is a unit modulo N. To supply one leaf qubit, repeat until accepted: acquire a fresh
copy, apply Mult_(alpha_j), run LE to obtain k, accept iff k < 2^dn (otherwise discard), and on acceptance apply X to the
control. The batch's acquisition cap applies. In the ideal run accepted labels are i.i.d. uniform on [0, 2^dn), and each copy
is accepted with probability 2^dn/N > 1/2. The qubit has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^(dn-1) W th = W 2^(dn-1-a2) alpha_j s / M = 2^j W s1 / M   (mod 1),           (11.1)

so a root is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known frequency f = 2^j W.

Measurement. Run BATCH for stage j. For each root i = 1..K obtain a fair bit beta_i by measuring H|0>, and measure the
root in X (beta_i = 0) or Y (beta_i = 1), recording Z_i in {+1,-1} with W_i and beta_i. Given W_i and beta_i,
E Z_i = cs_(beta_i)(f_i theta) with f_i = 2^j W_i.

Candidates. Put P_j = j + Y + 8 and identify an integer c with the point zeta = c/2^(P_j) on R/Z. Stage 0 uses every c in
[0, 2^(P_0)). Stage j >= 1 uses every c within circular distance rad_j = 2^-(j+2) of the previous center z_(j-1); both
z_(j-1) and rad_j are multiples of 2^-(P_j), so the arc endpoints are candidates. There are at most 2^(Y+8) candidates.

Score. For each candidate, with exact integer arithmetic,

    score(c) = sum_i Z_i * tab_(beta_i)( ((f_i c) mod 2^(P_j)) / 2^(P_j) ).

Enumerate candidates in increasing order, keeping the K residues (f_i c) mod 2^(P_j), updating each with one addition per
step, and keep a running maximum. Let z_j = c*/2^(P_j) for the least maximizer c*. All loops have fixed lengths.

Lemma 11.1. Suppose theta is within circular distance rad_j of z_(j-1) (no condition when j = 0). In the ideal run,
conditional on BATCH not aborting, with probability at least 1 - 2^-20/n, theta is within circular distance 2^-(j+3) of z_j.

Proof. Condition on the past of the stage and on G. For a candidate point zeta let Delta = theta - zeta as a circular
difference, and xi_i = Z_i cs_(beta_i)(f_i zeta). Given G, the roots use disjoint leaves and independent coins, and their
measurements are on separate qubits, so xi_1, ..., xi_K are independent with values in [-1,1]. Averaging over beta_i,

    E[xi_i | G, W_i] = (1/2)[cos(2 pi f_i theta) cos(2 pi f_i zeta) + sin(2 pi f_i theta) sin(2 pi f_i zeta)] = (1/2) cos(2 pi f_i Delta).

By (4.1) the computed score differs from sum_i xi_i by at most K/625.

Near point. The candidate zeta0 nearest theta has |Delta0| <= 2^-(P_j + 1). By (9.2), |f_i| <= 2^(j+Y+1), so
|f_i Delta0| <= 2^-8 and E[xi_i | G] >= (1/2) cos(pi/128).

Far points. Call zeta far if |Delta| >= 2^-(j+3). In stage 0, |Delta| <= 1/2. In stage j >= 1, theta and zeta lie within rad_j of
z_(j-1), so |Delta| <= 2^-(j+1). So xx = 2^j |Delta| is in [1/8, 1/2]. By Lemma 10.1 and (10.2) with phi = 2^j Delta,

    E[xi_i | G] = (1/2) Re E[exp(2 pi i 2^j Delta W_i) | G] <= (1/2) cos(pi xx) <= (1/2) cos(pi/8).

Concentration. By Hoeffding each fixed candidate's sum deviates from its conditional mean by at least K/64 with probability
at most exp(-K/8192). Outside these events,

    score(zeta0) >= (K/2) cos(pi/128) - K/64 - K/625 > (K/2) cos(pi/8) + K/64 + K/625 >= score(far zeta),

because (1/2)(cos(pi/128) - cos(pi/8)) > 0.0379 > 2/64 + 2/625 = 0.03445. So the maximizer is not far. There are at most 2^(Y+8)
events, one per candidate (the near point is itself a candidate), and exp(-K/8192) <= 2^-(2r + ceil(log2 n) + 30) <= 2^-(Y + ceil(log2 n) + 30), using Y <= 2r. The failure
probability is at most 2^(8-30)/n <= 2^-20/n. QED.

The hypothesis for stage j+1 is the conclusion of stage j, since 2^-(j+3) = rad_(j+1). By induction, with probability at least
1 - 2^-20, theta is within 2^-(J+3) < 1/(2M) of z_J. Output s1 = floor(M z_J + 1/2) mod M.

## 12. 2-adic part: s2 bit by bit

If a2 = 0, put s2 = 0 and skip this section. Otherwise s - s1 = M s2 (mod N) for a unique s2 in [0, 2^a2). Find its bits at levels
g = 0..a2-1. Let s2low be the known low g bits, sh_g = s1 + M s2low (mod N), wd = a2 - g, and rem = (s2 - s2low)/2^g in Z/2^wd, so
s - sh_g = M 2^g rem (mod N).

A leaf qubit for level g: acquire a copy, apply Shift_(sh_g), which makes the secret s - sh_g; run LE to obtain k; apply X to the
control. Ideally the phase is exp(2 pi i k M 2^g rem/N) = exp(2 pi i kk rem/2^wd), with kk = k mod 2^wd. Since 2^wd divides N and k
is uniform on Z/NZ, kk is uniform on [0, 2^wd). Use kk as the label.

- If wd = 1: make up to K leaf qubits, stopping at the first with kk = 1; measure it in X. The outcome is + iff rem is even. If
  none has kk = 1, set the bit to 0.
- If wd >= 2: run BATCH with B = wd - 1, with this supplier. Take the first root with W odd, and measure it in X. By (9.1) it is
  (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2, which gives rem mod 2 exactly. Release the other roots. If no root
  has W odd, set the bit to 0.

By (10.3), and independence of distinct roots given G, each such level misses with probability at most 2^-K, even if s1 was wrong.
Set bit g of s2. In the ideal run with s1 correct and no miss, every bit is correct. Output (s1 + M s2) mod N.

## 13. The complete algorithm and its success probability

Finite branch (n < 2^28). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand at the first minus outcome.
Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For cand != s the two data branches are orthogonal, so each outcome is uniform. A union
bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10. All resources on this branch are bounded by an absolute constant.

Main branch (n >= 2^28). Compute a2, M, dn, J, K, the schedule, Y, and all allocations; put

    Qcap = n Ccap + K.

Run Section 11 and then Section 12. Any ABORT stops the algorithm, releases everything and outputs 0. Since J + 1 + a2 <= log2 M + a2 = log2 N <= n, there are at most n batches,
each using at most Ccap acquisitions, plus at most K for the single wd = 1 level. So Q <= Qcap on every branch. LE is sized by this Qcap, which is computed before h_e.

Success. In the ideal run the failure events are: a batch ABORT, at most n (2^-12 + 2^-11)/n = 2^-12 + 2^-11 (Lemma 9.1); a decoder error, at most 2^-20 (Lemma 11.1); and a 2-adic miss,
at most n 2^-K <= 2^-40. Adding the LE coupling (5.1):

    Pr[output = s] >= 1 - 2^-12 - 2^-11 - 2^-20 - 2^-40 - 2^-10 >= 1 - 2^-8 > 2/3.

The finite branch succeeds with probability at least 1 - 2^-10. These are additive couplings; there is no conditioning on favorable labels or outcomes.

## 14. Resources on every main-branch execution

Throughout, K, dl, m, ell, w = O(sqrt n). Write U = 2^(ceil(113051 ell / 100000)) and PP = U * 2^m. Then
Dcap = O(n^2 2^m) and Ccap = O(n^2 PP). All fixed loops, caps and aborts below hold on every branch. The
factor 2^520 from Section 7 is an absolute constant and is absorbed in the O notation below; Section 15
checks that it does not escape the declared exponent.

Q. Q <= Qcap = n Ccap + K = O(n^3 PP).

S_Q. By Lemma 7.2 the streaming stage holds at most 512 + sum_i (30 E_i + 46) <= O(ell 2^w) qubits. The
depth-first stack holds at most two index registers per level, at most 2(m+1)(dl+m) = O(n) qubits. A merge
adds O(sqrt n) qubits. LE and transforms use O(n), reset between uses. So S_Q = O(ell 2^w + n).

S_C. Slot records use O(ell 2^w n) bits. Depth-first tables: at most three tables per level, each of
2^(lam_i) fields of 3n bits, plus merge scratch O((L+L') n). Since lam_i <= dl+m-1, this is O(n 2^(dl+m)).
The decoder stores K triples and K residues of O(n) bits. Hence S_C = O(n 2^(dl+m) + n ell 2^w). For these
parameters w + log2(ell) <= dl+m, so S_C = O(n 2^(dl+m)).

Core steps, per batch.
- Acquisitions: at most Ccap, each O(n^2) for Mult plus O(n^(5/2)) for LE: O(n^(5/2) Ccap).
- Streaming, Section 7: O(2^520 n r A_0 + n sum_i E_i) = O(2^520 n r Ccap).
- Tree: D <= Dcap on every branch. The same charging as a depth-first merge tree, using that a failed merge
  discards its inputs, bounds the tree by O(n^3 2^(m+dl)).
- Decoder per stage: O(K n 2^Y) = O(n^(3/2) Ccap).

Over at most n batches, core steps total O(2^520 n^2 r Ccap + n^4 2^(m+dl)). Every loop is either
fixed-length or consumes a capped acquisition, a capped delivered qubit, or a macro that removes two
qubits from a capped arrival count, so every branch terminates.

T. By (8.1), log2(S_C + S_Q + 2) = O(sqrt n). By (2.1),

    T = O(2^520 n^3 r Ccap + n^5 2^(m+dl)).

Exponents. r <= sqrt n + 1, but for n >= 2^28 one has r <= sqrt n + 1 <= (65/64) sqrt n and also
sqrt n >= r * 63/64; the explicit comparisons below use r <= sqrt n + 1 and sqrt n >= r - 1 >= (63/64) r
only through the final O. Directly:

    ell <= 79 r/200 + 1,   m <= 929 r/1000 + 1,   dl <= 56 r/125 + 1,   w <= 399 r/1000.

    log2 PP <= (113051/100000) ell + m
             <= (27511029/20000000) r + 113051/100000 + 1
             <= (27511029/20000000) r + 3,

    m + dl <= (1377/1000) r + 2,

    w <= (399/1000) r.

Therefore, using K <= 3 * 2^13 r, dl <= r and n <= r^2,

    log2 Ccap <= (27511029/20000000) r + 4 log2 r + 40.

The macro contribution then satisfies

    log2(2^520 n^3 r Ccap) <= (27511029/20000000) r + 560 + 12 log2 r,

and the tree contribution satisfies

    log2(n^5 2^(m+dl)) <= (1377/1000) r + 12 log2 r + 10.

Since sqrt n >= r - 1,

    (139/100) sqrt n >= (139/100) r - 139/100.

The macro excess over this quantity is at most

    560 + 12 log2 r + 139/100 - (288971/20000000) r,

because 139/100 - 27511029/20000000 = 288971/20000000. At r = 2^14 this excess is at most 500, and it
decreases for larger r: the coefficient 288971/20000000 exceeds 12/(r ln 2) at that endpoint. The tree
excess (13/1000) r - 12 log2 r - 12 is already positive at r = 2^14 and increases. Hence both
contributions are O(2^((139/100) sqrt n)), and so is T.

The same comparison gives S_C = O(2^((139/100) sqrt n)) and Q = O(2^((139/100) sqrt n)): their logarithms
are at most (1377/1000) r + 2 log2 r + 5 and (27511029/20000000) r + 6 log2 r + 5 respectively, both of
which sit under (139/100) sqrt n by a positive margin that grows with r.

For S_Q, log2(ell 2^w + n) <= 399 r/1000 + log2(ell) + 8. Since sqrt n >= r - 1,

    (2/5) sqrt n - (399 r/1000 + log2(ell) + 8) >= r/1000 - 2/5 - log2(ell) - 8.

At r = 2^14, ell = ceil(79 r/200) = 6472 and the right-hand side is greater than -5. For r > 2^14 the
expression increases. Thus S_Q <= 32 * 2^((2/5) sqrt n) on the main branch, so
S_Q = O(2^((2/5) sqrt n)).

## 15. Exact growth indices and declared envelopes

Section 14 gives T, S_C, Q = O(2^((139/100) sqrt n)) and S_Q = O(2^((2/5) sqrt n)) on the main branch. The
finite branch contributes one absolute constant, because each fixed n has a finite exhaustive cost and there
are finitely many n < 2^28. The declared envelopes are B(n) = 2^((139/100) sqrt n) for T, S_C and Q, and
B(n) = 2^((2/5) sqrt n) for S_Q. For B(n) = 2^(a sqrt n) with fixed a > 0,

    log2 log2 B = (1/2) log2 n + log2 a,

so g(B) = 1/2 exactly. The index uses these fixed coefficients. The structured objects in submission.json
are exactly these envelopes.

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset
state. Everything above is proved under this model. No positive tolerance for malformed copies is claimed,
and zero does not assert that robustness is impossible.

## 17. Scope and limitations

- This does not reach the research goal 2^(O(n^(1/3))). The time growth index is 1/2.
- The qubit envelope 2^((2/5) sqrt n) is below the streaming width 1/2 used by binary slot tables, and the
  work envelope 2^((139/100) sqrt n) is below the pure collimation envelope 2^(sqrt(2n)). Classical memory
  and the sample count remain 2^(Theta(sqrt n)).
- The instrument is a fixed 31-qubit dilation. Its gate count is an absolute constant, not a practical
  runtime. The main-branch threshold n >= 2^28 is unoptimized.
- One configuration is claimed. No other slot width is claimed here.
