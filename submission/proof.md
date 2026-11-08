# LG32-793: full leaf tables and 32-input merges listed by Grover, Q = O(2^((3/10) sqrt n)), S_C = S_Q = O(2^((3/5) sqrt n)), T = O(2^((793/100) sqrt n))

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single algorithm LG32-793 below receives N in binary and fresh independent copies of rho_s, and outputs the entire s with
unconditional probability at least 1 - 2^-8 > 2/3. On EVERY execution branch (every failure, discard and abort included) it satisfies jointly

    T = O(2^((793/100) sqrt n)),  S_C = O(2^((3/5) sqrt n)),  S_Q = O(2^((3/5) sqrt n)),  Q = O(2^((3/10) sqrt n)).

All constants are absolute. The growth indices are all exactly 1/2 (Section 15). The fifth claim is the clean-input tolerance 0 (Section 16). The sharper main-branch bounds, from which these follow, are in
Section 14. The envelope coefficients are fixed exact rationals; no hidden constant sits inside an exponent.

Notation:
- dn = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known nonnegative integer. log means log2 unless stated otherwise.

Main-branch parameters, computed by exact integer arithmetic for n >= 2^28:

    r0 = ceil(sqrt n),  w = floor(1199 r0/2000),  y32 = ceil(598 r0/10000),  Hb = ceil(7621 r0/1000),
    mu = 32 + y32,  kappa = ceil(log2 mu) + 3,  c0 = kappa + 1,  lam = c0 + w.

So the collimation tree has mu levels: 32 binary levels, then 32-input levels, all with tables of exactly 2^lam entries, and its leaf tables are built directly from lam qubits (Sections 8 and 9). Since r0 >= 2^14: w >= 2000, mu <= r0, 8 mu <= 2^kappa <= 16 mu, and c0 <= log2 r0 + 6 <= w/64, so lam <= r0.

## 1. Provenance and what is new

Sections 2-6.2 and 10-12 follow the framework of CS1 (f1481815-9577-4990-abe3-7b79fa5d9284) as adapted in my submissions HPC-127 (2aad498c-d5e9-4f64-a222-3b2f7f961738), LL-150 (2db348f1-6660-48c8-8e10-b056131f6baa) and PM4-146 (2c82753c-68eb-449e-85b0-5b21e7c37eba). Sections 6.3, 8 and 10.1 follow my GP16-191 (72b6a06d-acd3-4f7c-a2a9-7e9dadbd3031), and its measurement steps and overflow count follow my WD11-210 (438efd04-e4d1-4b4a-bb03-de909e42ab7e). Searching for fiber members by Grover on separate registers appeared first in GPS3 (05a58278-80b6-40ff-9e8b-dcec501b4b10) and MWG (76d06063-f670-4712-8f30-d52b4c665084), with lookup in classical tables and O(n) qubits. Tree heights and the overflow argument follow MW4 (e93f341a-7965-4a93-b5c4-7b0f7a799c37). Measuring a window before listing a four-input fiber was published first by IFC1 (1294d17f-2acf-4e10-9996-6b4375388f49). Dissection is from Dinur, Dunkelman, Keller and Shamir, CRYPTO 2012, and collimation from G. Kuperberg, arXiv:1112.3333. These citations are context; every step used is proved below.

New in this submission: the schedule. It moves the 32-input merges of my GP32-219 (35703982-0bbc-4ffc-b9a9-2de3dfcde35d) to the full-size leaf tables and node budget of my LW7-388 (e2a7f822-2791-4679-b069-9de16f632f56). With few samples and small tables, each doubling must remove many bits, and 32-input levels remove the most per doubling among the merges proved here. The technique is that of GP16-191: guess-dependent lists in about L qubits, fixed-length Grover runs over hashed blocks, and a merge that projects onto the tuples found.

## 2. Model and counting conventions

A CORE STEP is one of: a NOT/CNOT/Toffoli/H/S/S^dagger gate; a computational-basis
single-qubit measurement or reset; a Boolean operation on at most three classical bits; a
classical bit read or write. Toffoli has an exact constant-size Clifford+T decomposition.
Integers are bit strings; an L-bit addition, comparison or copy costs O(L) core steps.
Generating a gate costs O(1) core steps. Each core step additionally pays its address,
ceil(log2(Mem+2)) bit operations, where Mem <= S_C + S_Q is the number of allocated bits and
qubits. Gates are classically addressed through this charge; there is no
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

## 6. Phase vectors, the linear merge and multi-input merges

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

### 6.3 MERGEG(X1, ..., Xf; p, b, lam', kap, r), for f = 2^h, h = 3, 4 or 5

Precondition: X1..Xf are phase vectors on pairwise disjoint qubits, all of length L = 2^lam >= 64, collimated to p, with index registers x1..xf and tables lab_t. Also lam >= 3 kap + 14, lam' <= lam + 1, 0 <= r <= (h - 1) lam, and b = f lam - lam' - kap - r, so b >= h lam. Put G_3 = 4, G_4 = 11, G_5 = 26, G = G_h, g = G lam - r, and

    mu = 2^(f lam - b - r) = 2^(lam' + kap),   Cp = 2^(kap + 2) mu,   Cap = 2^(kap + 7) L,   D = 2^(kap + 9).

Let bb be whichever of lam' + 2 kap + 4 and lam' + 2 kap + 5 makes am = g - bb even, and M = 2^am. Since g >= 2 lam, am >= kap + 8. Let c_t = lab_t[0] mod 2^p, h_t[x] = floor(lab_t[x]/2^p), a_t[x] = h_t[x] mod 2^b and car = floor((c_1 + ... + c_f)/2^p). Bits p..p+b-1 of a tuple's label sum are res(x1,...,xf) = (a_1[x1] + ... + a_f[xf] + car) mod 2^b. Its WINDOW is win = (a_1[x1] + ... + a_(f/2)[x_(f/2)]) mod 2^r.

The tree. Arrange the tables as the leaves of a perfect binary tree of height h. A node v of level j has 2^j tables below it. For a tuple u let s_v(u) be the sum of its a_t over the tables below v, mod 2^b.

Targets. Fix tau in [0, 2^b) and c in [0, 2^r), and let z be a g-bit integer. Z determines a target T_v mod 2^(j lam) for each node v of level j >= 1, top-down. The root has T = tau mod 2^(h lam). A node v of level j >= 2 with children vl, vr takes T_vl, of (j - 1) lam bits, directly from fresh bits of z, and T_vr = (T_v - T_vl) mod 2^((j - 1) lam). At the root only, the low r bits of T_vl are c, and the other bits come from z. The number of bits used is the sum over j >= 2 of 2^(h - j) (j - 1) lam, minus r, which is exactly g.

TREE(z), a fixed Boolean circuit. Each node of level j >= 1 computes a LIST of Cap slots, each a valid bit, a tuple of indices, and its sum mod 2^b. A level-0 node has one slot per table entry. A node v of level j with child lists A, B and target T_v does this:
1. Give each valid slot of A the key s mod 2^(j lam), and each valid slot of B the key (T_v - s) mod 2^(j lam), with one bit recording its side.
2. Sort all these slots by (invalid bit, key) with a Batcher odd-even merge sorting network.
3. For each position q and each d in [1, D], form an output slot, valid if positions q and q + d are valid, have equal keys and have opposite sides, holding the two parts' indices and the sum of their sums.
4. Sort the output slots with valid ones first, again by a Batcher network, and keep the first Cap.

MARK(z) is the OR over the root's slots of (valid and sum = tau mod 2^b). A slot satisfying this is a ROOT RECORD. TREE(z) has O(2^(2 kap) L n) comparators of O(sqrt n) gates each, using lam, b = O(sqrt n) and log2(Cap D) = O(sqrt n), so O(2^(2 kap) L n^(3/2)) Boolean gates, and it can be evaluated classically on O(2^(2 kap) L sqrt n) bits. Table entries are fixed constants, and only z is an input.

Lemma 6.3 (records). A root record of TREE(z) is a tuple with res = e and win = c for tau = (e - car) mod 2^b, whose left-child sums are the left targets given by z. So each tuple is a root record for at most one z, and at most once. Conversely, let u have res = e and win = c. It has a unique z(u), namely its left-child sums. If in TREE(z(u)) no node's list of tuples meeting all targets below and at that node exceeds Cap, and no node has more than D slots with one key, then u is a root record.

Proof. For the first part, every kept slot meets its node's target by construction, the root's left child gives win = c, and the filter gives res = e. Left-child sums mod 2^((j-1) lam) equal the left targets, so z is determined, and a pair is formed at most once. For the converse, res = e gives s_root(u) = tau mod 2^(h lam), since h lam <= b. By induction down the tree, every subtuple of u meets its target. By induction up the tree, each subtuple is in its node's list: its two parts have equal keys, the group holds at most D slots so they lie within distance D after sorting, and the valid outputs are at most Cap, so all are kept. QED.

The merge.

1. LOOKUP each a_t into a fresh b-bit register, add these and car (mod 2^b) cleanly into a fresh register Rz, and clear the f registers by repeating the lookups. Measure Rz, obtaining e, and reset Rz from that known value. In the same way compute win into a fresh r-bit register by lookups, measure it, obtaining c, and reset it. Let S be the set of tuples with res = e and win = c, and sz = |S|. Put tau = (e - car) mod 2^b.
2. Listing, on fresh qubits and coins that do not touch the input registers. Draw alpha uniform and odd in [0, 2^g), by measuring H|0> g - 1 times. Start with an empty list Tl. For each block value B0 in [0, 2^bb):
   (a) Prepare am qubits in uniform superposition over v. Put z(v) = alpha^(-1) (B0 2^am + v) mod 2^g, computed cleanly by additions of constants.
   (b) Apply t = floor(pt 2^(am/2)/4) GROVER ITERATIONS, where pt <= pi is a rational within 2^(-am-8) of pi, from Machin's formula as in Section 4. An iteration computes z(v), TREE and MARK reversibly, applying each AND as a Toffoli onto a fresh ancilla; applies Z (that is S S) to the MARK bit; uncomputes; applies H to all am qubits; flips the sign of |0...0> by a Toffoli chain; and applies H to all am qubits again.
   (c) Measure v, evaluate TREE(z(v)) classically, and append its root records to Tl. If |Tl| would exceed Cp, declare FAIL.
   Every part of this has a fixed length.
3. Let R have ceil(log2(Cp + 1)) bits, with a one-qubit flag Rf. Both start at 0. For each row rho of Tl compute the flag [(x1,...,xf) = Tl[rho]] with a Toffoli chain on O(lam) scratch, CNOT it into Rf and CNOT it onto the bits of R where rho has a 1, and uncompute the chain. Since rows are distinct, on Tl R = rho and Rf = 1, and elsewhere R = Rf = 0. Measure Rf. If Rf = 0 declare FAIL. Let tl = |Tl|.
4. Measure bl = floor(R / 2^lam'). If (bl + 1) 2^lam' > tl declare FAIL.
5. For v in [0, 2^lam'), LOOKUP v -> Tl[bl 2^lam' + v] on the low lam' bits of R, XORing into x1..xf, which become |0>. Reset those registers, Rf and the high bits of R from their known values.
6. Output the low lam' bits of R as the index register, with table lab[v] the sum of the f input labels of Tl[bl 2^lam' + v].

On FAIL all inputs and registers are reset and released, and the inputs are never reused. All registers have fixed widths.

Correctness (ideal run). Before step 1 the state is the product of the inputs: equal magnitudes over all L^f tuples, with phases 2 pi (sum of labels) th. Step 2 acts on separate registers, so it does not disturb them. By Lemma 6.3, Tl is a set of distinct members of S. Steps 1, 3 and 4 compute functions of the tuple into clean registers and measure them. So after step 4 the state is the equal-magnitude superposition over the 2^lam' tuples of block bl, with their original phases. Step 5 maps each to its v bijectively. The output is thus a phase vector with table lab, and every label has the same residue modulo 2^(p+b), since all tuples in the block have res = e. So it is collimated to p+b.

Lemma 6.4 (Grover). If exactly one v in the block is marked, the measurement in step 2(c) returns it with probability at least 1 - 5/M.

Proof. Put s = 2^(-am/2) <= 1/16 and th0 = arcsin s, so s <= th0 <= s + s^3. The iterations act in the plane of the marked state and the uniform state as usual, and the marked amplitude after t iterations is sin((2 t + 1) th0). Here t <= pi/(4 s) < t + 1.01, so this angle is within 2 th0 of pi/2. So the probability is at least cos^2(2 th0) >= 1 - 4 th0^2 >= 1 - 5 s^2. QED.

Lemma 6.5 (blocks). For distinct z, z' in [0, 2^g), the top bb bits of alpha z mod 2^g and alpha z' mod 2^g agree with probability at most 2^(1 - bb) over alpha.

Proof. Write z - z' = 2^i m with m odd and i < g. Then alpha (z - z') mod 2^g is uniform on the 2^(g - i - 1) odd multiples of 2^i. Agreement forces its circular absolute value below 2^am, which holds for at most 2^(am - i) of them. The ratio is 2^(1 + am - g) = 2^(1 - bb). QED.

Lemma 6.6 (failure bound). For ANY input tables collimated to p, the measurement laws and every decision depend only on the a_t, car and independent coins, that is on label bits below p+b. With sums over all outcome pairs (e, c), and with lost(e, c) the number of members of S missing from Tl,

    Pr[FAIL] <= 2^(-kap) + sum_(sz > Cp) sz/L^f + E sum_(sz <= Cp) lost(e, c)/L^f.

Proof. Each input-register measurement is a computational-basis measurement of a function of the tuple on an equal-magnitude superposition, so its law is a ratio of counts, independent of phases. Outcomes (e, c) have probability sz/L^f. If sz <= Cp, step 2 does not FAIL, Rf = 0 has conditional probability lost/sz, and given Rf = 1, R is uniform on [0, tl), so step 4 fails with probability (tl mod 2^lam')/tl. Multiplying and summing over the 2^(b + r) outcome pairs, this last term contributes at most 2^(b + r) (2^lam' - 1)/L^f < 2^(-kap). QED.

Cost. Step 2 has 2^bb blocks of at most 2 t + 1 evaluations of TREE, on every branch, with t = O(2^(am/2)). That is O(2^((g + bb)/2)) = O(2^kap L^((G + 1)/2) 2^(-r/2)) evaluations, so O(2^(3 kap) L^((G + 3)/2) 2^(-r/2) n^(3/2)) core steps. The other steps are at most 4f lookup passes of L rows with O(sqrt n)-bit fields, one pass of at most Cp rows with O(lam) control bits, one pass of 2^lam' rows and 2^lam' additions of 3n-bit labels, which is no more. Quantum scratch is O(2^(2 kap) L n^(3/2)) beyond the f index registers. Classical scratch, including Tl and classical TREE evaluation, is O((2^(2 kap) L + Cp) sqrt n + 2^lam' n) bits.

## 7. Leaf qubits

A LEAF QUBIT is a phase vector of length 2 with table (0, k), for its known label k: a positive qubit whose state in the ideal run is (|0> + exp(2 pi i k th)|1>)/sqrt 2, up to global phase, for a fixed real th. There is no pairing stage in this algorithm; leaf qubits go directly into leaf tables.

## 8. The schedule

Tree levels are numbered i = 0, ..., mu - 1. Every level has input table exponent lam_i = lam. Level i has arity f_i and window width r_i:

    Phase A, 0 <= i < 32:                 f_i = 2,   r_i = 0;
    Phase T, i = 32 + j, 0 <= j < y32:    f_i = 32,  r_i = max(0, 29 w - 2 Hb - 10 j).

This row uses only the arities f = 2 and f = 32 of Section 6. Let N_0 = 1 and N_(i+1) = f_i N_i, so a node of level i has N_i leaf tables below it, and put h_i = log2 N_i and Nmax = N_mu. So h_i = i for i <= 32, and h_(32+j) = 32 + 5 j. By substitution,

    binary: lam <= c0 + Hb + h_i;   32-input: 29 lam - r_i <= 29 c0 + 2 Hb + 2 h_i.     (8.0)

The windows are chosen for exactly this. Also r_i <= 29 w - 2 Hb <= 4 w <= 4 lam, as 2 Hb >= 25 w.

Capacities. For i < mu - 1 put tbmax_i = f_i lam - lam - kappa - r_i, and for every i put rootcap_i = f_i lam - 1 - kappa - r_i >= tbmax_i. Since c0 = kappa + 1, Phase A has tbmax_i = w + 1, and Phase T has tbmax_i >= 31 w - r_i.

Exponent bound. With y32 <= 598 r0/10000 + 1,

    log2 Nmax = 32 + 5 y32 <= 0.299 r0 + 37.                                         (8.1)

Demand constants, with K from (11.0):

    Dbar = 3 K Nmax lam,     Dcap = 2^12 n Dbar,     Ccap = 2^13 n Dbar.

Let Y be the least integer with 2^Y >= Ccap. Using K <= 4 * 2^13 r0 (as 3 r0 + ceil(log2 n) + 30 <= 4 r0), lam <= r0 and n <= r0^2,

    log2 Ccap <= r0 + 4 log2 r0 + 40 <= 3 r0 - 1.                                   (8.1')

So Y <= 3 r0 <= n (as r0 <= sqrt n + 1 and n >= 2^28), and 2^Y <= 2 Ccap.

A tree of m levels. For 1 <= m <= mu, a tree with m levels uses level m-1 as its root, with lam_m := 1 and capacity Sum(m) = sum_(i < m-1) tbmax_i + rootcap_(m-1). Since Sum(m+1) - Sum(m) = (f_m - 1) lam - kappa - r_m > 0, Sum is increasing.

Lemma 8.1 (capacity). For n >= 2^28: Sum(mu) >= r0^2 >= n.

Proof. Put gam0 = 299/5000, alp = 1199/2000 and v = 7621/1000. Every window is positive, since 29 w - 2 Hb - 10 y32 >= (29 alp - 2 v - 10 gam0) r0 - 32 > 0, as 29 alp - 2 v - 10 gam0 >= 0.01 and 0.01 r0 >= 32. So r_(32+j) = 29 w - 2 Hb - 10 j. Summing over j < y32, Sum(mu) >= y32 (2 w + 2 Hb) + 5 y32 (y32 - 1). With y32 >= gam0 r0, w >= alp r0 - 1 and Hb >= v r0,

    Sum(mu) >= (gam0 (2 alp + 2 v) + 5 gam0^2) r0^2 - (7 gam0) r0 >= C r0^2 - 16 r0,

with C = 250263/250000 >= 1.001. Finally 0.001 r0 >= 16 for r0 >= 2^14. QED.

Bit allocation. Given integer B with 1 <= B <= n, each batch fixes its tree: m is least with Sum(m) >= B. Allocate tb_(m-1) = min(rootcap_(m-1), B), and then for i = m-2, ..., 0, tb_i = min(tbmax_i, bits still unallocated). Then sum_i tb_i = B. Positions: tp_0 = 0, tp_(i+1) = tp_i + tb_i, so tp_m = B. Every bit read below has position below B. All allocation is computed classically before the batch.

Lemma 8.2 (multi-input levels are full). In any tree with a level i >= 32, every level i >= 32 gets its full capacity. In particular, each multi-input level has tb_i = f_i lam_i - lam_(i+1) - kappa - r_i exactly, with lam_m = 1.

Proof. Here m >= 33, so Sum(m-1) < B by minimality. Hence the deficit Sum(m) - B is less than Sum(m) - Sum(m-1) <= 31 (c0 + w). Phase A has total capacity 32 (w + 1) >= 31 (c0 + w), since c0 <= w/64. So the greedy allocation meets every level i >= 32 in full before it reaches Phase A. QED.

Failure budgets. For a binary level, b_i + lam_(i+1) - 2 lam_i <= -kappa for every allowed b_i, so Lemma 6.1 gives Pr[FAIL] <= 2^-kappa for any input tables. For multi-input levels, Lemma 8.2 gives the exact precondition of MERGEG with kap = kappa. Its other preconditions are direct: lam = c0 + w >= 3 kappa + 14 and L >= 64, lam_(i+1) <= lam, and the bounds on r_i above. Failure in those levels is bounded by Lemma 10.2.

## 9. BATCH(supplier, B)

Input: a supplier of leaf qubits, where in the ideal run the labels are independent and uniform on [0, 2^(B+1)). Output: K roots, or ABORT. A batch has a counter of source acquisitions; if an acquisition would exceed Ccap, the batch ABORTs.

TREE. VEC(0) = LEAF: request lam leaf qubits from the supplier, counting each in a counter D; if D would exceed Dcap, ABORT. These qubits form the index register, bit j = qubit j. With labels k_j, build lab[0] = 0 and lab[x + 2^j] = lab[x] + k_j for x < 2^j. The table has length 2^lam, is exactly the tensor product state in the ideal run, and is collimated to tp_0 = 0.

VEC(i), 1 <= i <= m: repeat: build f_(i-1) inputs, each by VEC(i-1); put out = MERGE(X1, X2; tp_(i-1), tb_(i-1), lam_i) if f_(i-1) = 2, and otherwise out = MERGEG(X1, ..., X_(f_(i-1)); tp_(i-1), tb_(i-1), lam_i, kappa, r_(i-1)); until out != FAIL; return out. A root is VEC(m), evaluated depth-first. Run it K times.

Root. VEC(m) is a two-entry table with lab[0] = lab[1] mod 2^B, so its ideal state is, up to global phase,

    (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2,   W = (lab[1] - lab[0])/2^B, a known integer.     (9.1)

Label bound. Each leaf qubit enters a table entry at most once, and a batch has at most Ccap leaves. So every label in the batch is a sum of at most Ccap leaf labels below 2^(B+1). Thus every label is below 2^(Y+n+1), which fits in 3n bits by Y <= n, and

    |W| <= 2 Ccap <= 2^(Y+1).                                                       (9.2)

Lemma 9.1 (no abort). Suppose each supplied acquisition yields a leaf qubit independently with probability at least 1/2, given the past. In the ideal run a batch ABORTs with probability at most 2^-12/n + 2^-11/n.

Proof. Consider the same process with no caps. By the failure budgets of Section 8 and Lemma 10.2, each merge fails with conditional probability at most ep = 2^(2-kappa) given everything before it. Let V_i bound the expected number of qubits requested by VEC(i). Then V_0 = lam and, by Wald's identity, V_(i+1) <= tt f_i V_i with tt = 1/(1 - ep). Since 2^(kappa-2) >= 2 mu, tt^mu <= exp(mu ep/(1 - ep)) <= e < 3. So V_m <= 3 N_m lam <= 3 Nmax lam, the total demand D_inf of K roots has E[D_inf] <= Dbar, and Markov gives Pr[D_inf > Dcap] <= 2^-12/n. Each acquisition is accepted with conditional probability at least 1/2, so by Wald the expected number of acquisitions up to any bounded stopping time is at most 2 E[D_inf] <= 2 Dbar. Markov against Ccap = 2^13 n Dbar gives probability at most 2^-12/n <= 2^-11/n. The real run coincides with the uncapped one until a cap triggers. QED.

## 10. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and tau_j in {0,1}. Since k_j is uniform on
[0, 2^(B+1)), low_j and tau_j are independent and tau_j is a fair bit. For a batch let G be the sigma-field generated
by: all low_j of its leaves; all merge outcomes (e, c, Rf, bl); and all decisions of the controller in
that batch (listing coins, Grover outcomes, the lists Tl, FAIL and retries, aborts, assignment of qubits). G does not include
root measurement outcomes, which no decision in the batch reads. It also excludes LE's internal coins and outcomes,
which in the ideal run feed no decision.

Lemma 10.1. In the ideal run, conditional on G and on all independent randomness outside the batch, the top bits tau_j
are i.i.d. fair.

Proof. Induct over the controller's steps. Every key, residue, sort, enumeration, rank and block partition reads only label bits
strictly below position B, because all positions used are below B (Section 8). Bits below B of a sum of leaf labels
depend only on the low_j, since multiples of 2^B do not change them.
By Lemmas 6.1 and 6.6 each merge outcome's conditional law, given
labels and earlier outcomes, is a function of the low_j and earlier outcomes only. So the joint law factorizes as
law(tau) x law(low) x law(outcomes and decisions | low). QED.

Incidence. An entry of a table is the sum over leaves j of x_j k_j, for a 0/1 incidence vector x. Distinct indices of a
table have distinct incidence vectors: this holds for a leaf qubit, table (0, k_j); a LEAF table concatenates disjoint coordinates; and a merge re-indexes injectively pairs or tuples on disjoint
coordinates. So the two root entries have x0 != x1, and with hd = |x0 xor x1| >= 1,

    W = cst + sum_(j in Sp) tau_j - sum_(j in Sm) tau_j,                            (10.1)

where cst = (sum_j low_j (x1_j - x0_j))/2^B is a G-measurable integer, and Sp, Sm are disjoint G-measurable sets with
|Sp| + |Sm| = hd. Each leaf enters at most one root, so given G the W's of distinct roots of a batch are independent.
Since E exp(2 pi i phi tau) = e^(i pi phi) cos(pi phi) for a fair bit, for every real phi

    | E[ exp(2 pi i phi W) | G ] | = |cos(pi phi)|^hd <= |cos(pi phi)|,             (10.2)

and, with phi = 1/2, Pr[W odd | G] = 1/2.                                           (10.3)

### 10.1 The failure bound for MERGEG

Lemma 10.2. In the ideal run, consider a MERGEG attempt at tree level i, with f = f_i, h = log2 f, p = tp_i, b = tb_i, lam = lam_i and lam' = lam_(i+1), conditional on the selection and control history before its step 1, meaning all measurement outcomes and decisions so far and the label bits they read. Then Pr[FAIL] <= 2^(2-kappa).

Proof. Let Lv be the set of leaves entering the f inputs, a union of f pairwise disjoint sets. For j in Lv write k_j = l_j + 2^p c_j + 2^(p+b) u_j with 0 <= l_j < 2^p and 0 <= c_j < 2^b. This is possible as p + b <= B < B + 1, and k_j uniform makes l_j, c_j, u_j independent and uniform.

Factorization. Use deferred decisions on label bits, per leaf and per position. Merges at lower levels of the subtrees of the inputs have p' + b' <= p, and by Lemmas 6.1 and 6.6 their laws and all their decisions read only label bits below p of those leaves. All other steps read only leaves outside Lv, because leaves are not shared. The identity of the next step and of the leaves it touches is a function of the outcomes so far. So by induction over the controller's steps, conditional on that history, every label bit not read by it is still uniform and independent. The history reads only bits below p of leaves in Lv, although full labels are stored. Hence, conditional on the history and also on all l_j, the c_j (j in Lv) are i.i.d. uniform on [0, 2^b), and the f inputs depend on disjoint sets of them.

Uniform differences. Each table entry has a 0/1 incidence vector over leaves, and its residue is a known constant plus the sum of c_j over that vector, modulo 2^b. A tuple of entries from several inputs has incidence equal to the disjoint union, and distinct tuples have distinct incidence vectors, by the argument of Section 10. So:

    (U) for two distinct tuples from the same tables, the difference of their residue sums is uniform mod 2^b, because some c_j has coefficient +1 or -1.

Overflow of S. Write an f-tuple as (A, A'), with A from the first k = f/2 tables and A' from the others, and let s(A), s(A') be its two residue sums. Let Z = sum_(e,c) sz^2/L^f, which is 1/L^f times the number of ordered pairs of tuples with the same outcome. There are four kinds of pair:
- Equal tuples: L^f pairs, contributing 1.
- Both parts differ: the same outcome needs the first parts to agree mod 2^r and then the second parts' difference to equal a value fixed by the first parts mod 2^b. By (U) and independence of the parts this has probability at most 2^-(b + r), contributing at most L^f 2^-(b + r) = mu.
- Same first part: by (U) the probability is 2^-b. At most L^(2f - k) pairs contribute at most L^k 2^-b = mu 2^r L^-k.
- Same second part: res equal needs the first parts to agree mod 2^b, probability 2^-b, contributing the same.

Since r <= (h - 1) lam <= (k - 1) lam, each of the last two is at most mu/L. So E Z <= 1 + mu + 2 mu/L <= 3 mu. Since sum_(sz > Cp) sz/L^f <= Z/Cp and Cp = 2^(kappa + 2) mu,

    E sum_(sz > Cp) sz/L^f <= (3/4) 2^(-kappa).                                     (10.4)

Lost tuples. Sum over tuples u, with its outcome (e, c): sum_(e,c) lost/L^f is the sum over u of [u is missing from Tl]/L^f. If u is missing, then by Lemmas 6.3 and 6.4 one of three things happened.

(i) A list or key group overflowed in TREE(z(u)). Fix u. For a node v of level j and l >= 0, let X_j(l) bound, over any shift d, the expected number of subtuples w != u_v below v that meet every target of z(u) at proper descendants of v, and have s_v(w) = s_v(u) + d mod 2^l. Level 0 gives X_0(l) <= L 2^-l by (U). At level j, w = (wl, wr). Either wl equals u's part, or wr does, or both differ, and then the parts are independent. So

    X_j(l) <= (2 + X_(j-1)((j - 1) lam)) X_(j-1)(l).

Let A_0 = 1 and A_j = A_(j-1) (A_(j-1) + 2/L). By induction X_j(l) <= A_j L 2^(j lam - l), and since L >= 64, A_1 to A_4 are at most 2 and A_5 <= 5/2. So a node's list, with u's own subtuple, has expected size at most 1 + X_j(j lam) <= 3 L, and a key group holds u's two parts and on each side at most X_(j-1)(j lam) <= 2 others in expectation, so at most 6. By Markov and a union over at most 31 nodes, this has probability at most 31 (3 L/Cap + 6/D) = 31 (3/128 + 6/512) 2^(-kappa).

(ii) Another marked guess lies in u's block. By Lemma 6.3 it comes from some w in S with z(w) != z(u). By Lemma 6.5, summing over u, this contributes at most Z 2^(1 - bb), with expectation at most 3 mu 2^(1 - bb) <= (6/16) 2^(-kappa), since 2^bb >= 2^(kappa + 4) mu.

(iii) u's guess is alone and marked in its block, and Grover misses it: probability at most 5/M <= (5/64) 2^(-kappa), by Lemma 6.4.

Failure. By Lemma 6.6 and (10.4), Pr[FAIL] <= (1 + 3/4 + 31 (3/128 + 6/512) + 6/16 + 5/64) 2^(-kappa) <= 2^(2 - kappa). QED.

## 11. Odd part: s1 = s mod M by free-frequency decoding

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so dn - 1 >= a2. Put theta = s1/M. Every stage uses
B = dn - 1 (B >= 1 on the main branch) and

    K = 2^13 (3 r0 + ceil(log2 n) + 30).                                              (11.0)

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
events, one per candidate (the near point is itself a candidate), and exp(-K/8192) <= 2^-(3 r0 + ceil(log2 n) + 30) <= 2^-(Y + ceil(log2 n) + 30), using Y <= 3 r0. The failure
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

Finite branch (n < 2^28). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand at the first minus outcome. Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For cand != s the two data branches are orthogonal, so each outcome is uniform. A union bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10.
All resources on this branch are bounded by an absolute constant.

Main branch (n >= 2^28). Compute a2, M, dn, J, K, the schedule, Y, and all allocations; put

    Qcap = n Ccap + K.

Run Section 11 and then Section 12. Any ABORT stops the algorithm, releases everything and outputs 0. Since J + 1 + a2 <= log2 M + a2 = log2 N <= n, there are at most n batches, each using at most Ccap acquisitions, plus at most K for the single wd = 1 level. So Q <= Qcap on every branch. LE is sized by this Qcap, which is computed before h_e.

Success. In the ideal run the failure events are: a batch ABORT, at most n (2^-12 + 2^-11)/n = 2^-12 + 2^-11 (Lemma 9.1); a decoder error, at most 2^-20 (Lemma 11.1); and a 2-adic miss, at most n 2^-K <= 2^-40. Adding the LE coupling (5.1):

    Pr[output = s] >= 1 - 2^-12 - 2^-11 - 2^-20 - 2^-40 - 2^-10 >= 1 - 2^-8 > 2/3.

The finite branch succeeds with probability at least 1 - 2^-10. These are additive couplings; there is no conditioning on favorable labels or outcomes.

## 14. Resources on every main-branch execution

Throughout, K, c0, mu, w, Hb, lam = O(sqrt n), 2^c0, 2^kappa = O(sqrt n), Dcap/lam = O(n^(3/2) Nmax) and Ccap = O(n^2 Nmax). All fixed loops, caps and aborts below hold on every branch.

Q. Q <= Qcap = n Ccap + K = O(n^3 Nmax).

S_Q. The depth-first stack holds at most f_i <= 32 index registers per level, each of at most c0 + w qubits, at most 32 mu (c0 + w) = O(n) qubits. A binary merge adds O(sqrt n) qubits. MERGEG adds O(2^(2 kappa) L n^(3/2)) = O(n^3 2^w) qubits, with 2^kappa = O(sqrt n) and L = 2^(c0 + w). Only one merge is active at a time. LE and transforms use O(n), reset between uses. Each root is measured at once. So S_Q = O(n^3 2^w).

S_C. Depth-first tables: at most 33 tables per level, each of 2^(lam_i) <= 2^(c0 + w) fields of 3n bits, so O(mu n 2^(c0 + w)) = O(n^2 2^w) over all levels. Merge scratch is O(n 2^(c0 + w)) for binary merges. For MERGEG it is O((2^(2 kappa) L + Cp) sqrt n + 2^lam' n), where Cp = 2^(lam' + 2 kappa + 2) = O(n^(3/2) 2^w), so it is O(n^2 2^w) as well. The decoder stores K triples and K residues of O(n) bits. LE uses O(n) bits. So S_C = O(n^2 2^w). These are fixed allocations.

Core steps, per batch.
- Acquisitions: at most Ccap, each O(n^2) for Mult plus O(n^(5/2)) for LE (log2 Qcap = O(sqrt n) by (8.1'), so h_e = O(sqrt n)): O(n^(5/2) Ccap).
- Tree: since D <= Dcap on every branch, there are at most Dcap/lam LEAF calls at O(n 2^lam) each, O(n^3 Nmax 2^w) in all. A merge producing level i+1 consumes N_(i+1) lam delivered qubits that no other merge at that level uses, since inputs of a failed merge are discarded. So there are at most Dcap/(N_(i+1) lam) of them. By Sections 6.2-6.3 and (8.0), each costs at most O(2^(3 kappa) n^(3/2) 2^((29/2) c0) 2^Hb N_i) = O(n^(41/4) 2^Hb N_i), for both arities, since 2^kappa <= 32 r0 makes 2^(3 kappa + (29/2) c0) = O(n^(35/4)). Each level costs O(n^(41/4) 2^Hb Dcap/lam), and all mu + 1 levels cost O(n^(43/4) 2^Hb Dcap/lam) = O(n^(49/4) Nmax 2^Hb).
- Decoder per stage: at most 2^(Y+8) candidates, K residues each, O(n) bits per addition: O(K n 2^Y) = O(n^(3/2) Ccap).

Over at most n batches, plus poly(n) setup (parameters, CRT, Mult constants, the table of Section 4, shift values, initial residues), core steps total O(n^(53/4) Nmax 2^Hb) + poly(n). Every loop is either fixed-length or consumes acquisitions or delivered qubits under a cap, so every branch terminates.

T. By (8.1'), log2(S_C + S_Q + 2) = O(sqrt n). By (2.1),

    T = O(n^14 Nmax 2^Hb + n Q) = O(n^14 Nmax 2^Hb).

Exponents. By (8.1) and r0 <= sqrt n + 1,

    log2 Nmax <= 0.299 sqrt n + 38,
    Hb <= (7621/1000) r0 + 1 <= 7.621 sqrt n + 8.621,
    w <= (1199/2000) r0 <= 0.5995 sqrt n + 1.

Therefore, jointly, on every branch of the main branch,

    T = O(n^14 2^(7.92 sqrt n)),  S_C = O(n^2 2^(0.5995 sqrt n)),  S_Q = O(n^3 2^(0.5995 sqrt n)),  Q = O(n^3 2^(0.299 sqrt n)).

## 15. Exact growth indices and declared envelopes

Since n^14 2^(-a sqrt n) is bounded over n >= 1 for each fixed a > 0, as are its analogues with n^3 and n^2, the bounds of Section 14 give T = O(2^((793/100) sqrt n)), Q = O(2^((3/10) sqrt n)) and S_C, S_Q = O(2^((3/5) sqrt n)). The finite branch contributes only an absolute constant. The declared envelopes are B(n) = 2^((793/100) sqrt n) for T, B(n) = 2^((3/10) sqrt n) for Q, and B(n) = 2^((3/5) sqrt n) for S_C and S_Q. For B(n) = 2^(a sqrt n) with fixed a > 0, log2 log2 B = (1/2) log2 n + log2 a, so g(B) = 1/2 exactly. The indices hold for these fixed exact coefficients; they do not rely on a guessed constant. The structured objects in submission.json are exactly these envelopes.

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does not assert that robustness is impossible.

## 17. Scope and limitations

- This does not reach the research goal 2^(O(n^(1/3))); the time growth index is 1/2.
- It is a tradeoff: it uses exponentially many qubits, 2^((1/8) sqrt n), where O(n)-qubit rows at this classical memory have larger T.
- The main-branch threshold n >= 2^28 and all polynomial factors are unoptimized.
- One parameter choice is claimed. The schedule favors simple arithmetic over the best constant.
