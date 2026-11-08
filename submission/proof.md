# SPQ-143: streaming pairing under a sample budget, T = O(2^((143/100) sqrt n)), Q = S_Q = O(2^((11/10) sqrt n))

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single algorithm SPQ-143 below receives N in binary and fresh
independent copies of rho_s, and outputs the entire s with unconditional probability at least 1 - 2^-8 > 2/3. On EVERY execution branch
(every failure, discard and abort included) it satisfies jointly

    T = O(2^((143/100) sqrt n)),  S_C = O(2^((143/100) sqrt n)),  S_Q = O(2^((11/10) sqrt n)),  Q = O(2^((11/10) sqrt n)).

All constants are absolute. Each of the four envelopes has growth index exactly 1/2 (Section 15). The fifth claim is the clean-input
tolerance 0 (Section 16). The sharper main-branch bounds, from which these follow, are in Section 14. The envelope coefficients are fixed
exact rationals; no hidden constant sits inside an exponent.

Notation:
- dn = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known nonnegative integer. log means log2 unless stated otherwise.

Main-branch parameters, computed by exact integer arithmetic for n >= 2^28:

    r = ceil(sqrt n),  ell = ceil(296 r/2000),  w = floor(2197 r/2000),
    m = ceil(8650 r/10000),  dl = ceil(5568 r/10000),  kappa = ceil(log2 m) + 1.

So there are ell PAIRING LEVELS, each with a slot table of at most 2^w qubits, a collimation tree of depth m, and leaf tables built from dl
qubits. Since r >= 2^14 these satisfy ell >= 2, dl >= kappa + 1 and 2^kappa >= 2m.

## 1. Provenance and what is new

This is my earlier SPC-127 (0efb267b-c55e-49cb-946b-ea3ced57f221) with a different parameter choice. Sections 2-7 and 9-13 are SPC-127's text,
unchanged. SPC-127 combined two earlier submissions of mine: HPC-127 (2aad498c-d5e9-4f64-a222-3b2f7f961738), which introduced the recycling pairing
operation with a batched pool, and SPC-138 (cca84cdb-9909-488b-9f0f-707dd7b4ed5e), which introduced streaming slot tables. Sections 2-6 and 10-12
follow the framework of CS1 (f1481815-9577-4990-abe3-7b79fa5d9284) as adapted there: latent-label model, data transforms, label extraction, the
linear merge and its distribution-free failure bound, top-bit independence, the free-frequency decoder and the 2-adic endgame. Everything needed is
restated, so nothing depends on any earlier verdict. Collimation is from G. Kuperberg, arXiv:1112.3333. Pairing qubits with equal low label bits is
from G. Kuperberg, SIAM J. Comput. 35(1), 2005. These citations are context; every step used is proved below.

New in this submission: the constants of Section 8 and the numbers that follow from them in Sections 8, 14 and 15. SPC-127 puts many pairing
levels below its tree, so its source count equals its work. Here there are fewer pairing levels (ell about 0.148 r instead of 0.3095 r) and a
deeper tree with larger leaf tables (m about 0.865 r, dl about 0.5568 r). The source count is governed by 3^ell 2^m (Section 14), so Q falls
to 2^((11/10) sqrt n) while the tree term 2^(m + dl) sets T = 2^((143/100) sqrt n).

Why this helps. In units of sqrt n, let 2^X be the work budget, 2^y the qubit budget and 2^q the source budget. Pairing at stream size 2^P
removes about P bits for log2 3 of budget, a tree level at stream size 2^P removes about X - P bits for one, and with 2^q sources no stream is
larger than about 2^q. So n ~ integral_0^q max(min(P,y)/c, X-P) dP with c = log2 3. At q = y = 11/10 this gives X about 1.422, while the
tree alone with the same q gives X = 1/q + q/2 = 1.459. This paragraph is motivation only; the theorem rests on the explicit schedule of Section 8.

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

IDEAL run. The ideal run is HPC-127 in the latent-label model with every LE output replaced by the
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

## 7. The streaming pairing stage

A LABELED QUBIT is a phase vector of length 2 with table (t0, t1); write Del = t1 - t0, an integer that may be negative.
It is COLLIMATED TO p if Del = 0 mod 2^p.

PAIR(A, B). Given labeled qubits A = (t0, t1), B = (u0, u1) on disjoint qubits, apply CNOT with A as control and B as
target, measure B obtaining o in {0,1}, and reset B. The output is qubit A with table

    (t0 + u1, t1 + u0) if o = 1,     (t0 + u0, t1 + u1) if o = 0.                   (7.1)

Lemma 7.1. In the ideal run the output is exactly a phase vector with table (7.1), and o is uniform, conditional on every
label, th and the entire past. Its label differences are Del_A - Del_B (o = 1) and Del_A + Del_B (o = 0).

Proof. Before measurement the state has equal magnitudes on (a, b) in {0,1}^2 with phases exp(2 pi i (t_a + u_b) th).
After CNOT the second register holds o = a xor b. Each value of o is carried by exactly two of the four equal-magnitude
terms, so it has probability 1/2. For o = 1 the surviving terms are (a,b) = (0,1), (1,0), and for o = 0 they are (0,0),
(1,1); indexing by a gives (7.1). QED.

Slot tables. Pairing level i (0 <= i < ell) has bit position pp_i, width pb_i <= pbmax_i <= w (Section 8), and a table SLOT_i with
E_i = 2^(pb_i) entries, each empty or holding one labeled qubit: its table (t0, t1) and the index of its wire. The key of a
qubit collimated to pp_i is key_i = floor((Del mod 2^(pp_i + pb_i)) / 2^(pp_i)), computed from t1 and t0 modulo 2^(pp_i+pb_i).

NEXT(i) returns one qubit collimated to pp_i, where pp_0 = 0. NEXT(0) asks the batch's supplier for one leaf qubit, a labeled
qubit with table (0, k). For i >= 1, NEXT(i) with lev = i-1 runs:

    item = NEXT(lev)
    loop:
        if SLOT_lev[key_lev(item)] is empty:
            store item there; item = NEXT(lev)
        else:
            partner = that slot's qubit; empty the slot
            result = PAIR(partner, item) with outcome o
            if o = 1: return result
            item = result

Lemma 7.2 (invariants and memory). On every branch: (a) every qubit stored in SLOT_i, and every item at level i, is
collimated to pp_i, and every qubit returned by NEXT(i+1) is collimated to pp_(i+1) = pp_i + pb_i. (b) SLOT_i never holds more
than E_i qubits, whatever the labels. (c) Across all levels, at most one qubit is outside the slot tables at any time: while
a frame waits on a recursive call it holds no qubit, because it stored or returned its item first. So at most
1 + sum_i E_i qubits are held by the pairing stage. (d) Keys read only label bits below pp_i + pb_i.

Proof. (a) Del_A + Del_B preserves collimation to pp_i. If both have the same key, then Del_A = Del_B mod 2^(pp_i + pb_i), so
Del_A - Del_B = 0 mod 2^(pp_(i+1)). (b) and (c) are immediate from the code, and (d) from the definition of the key. QED.

Lemma 7.3 (flow). Consider any point of a batch. For level i let A_i be the number of calls to NEXT(i) that have returned into
level i, O_i and F_i the numbers of level-i PAIRs with o = 1 and o = 0, L_i the current occupancy of SLOT_i, and H_i in {0,1} the
number of current items at that level. Then deterministically

    A_i = 2 O_i + F_i + L_i + H_i,   with L_i <= E_i,                              (7.2)

and O_i is the number of completed calls to NEXT(i+1), so O_i = A_(i+1), with A_ell defined as the number of qubits delivered to
the tree. Hence A_(i+1) <= A_i/2 on every branch, and sum_i A_i <= 2 A_0. Moreover, for any stopping time with a bounded number of
PAIRs, in the ideal run

    E[A_i] <= 3 E[A_(i+1)] + E_i + 1.                                              (7.3)

Proof. Identity (7.2) is conservation at level i: an arrival adds one qubit; storing it moves it from H_i to L_i; a PAIR with o = 1
removes two qubits from the level and a PAIR with o = 0 removes one, the result staying as the item. For (7.3): by Lemma 7.1 each
outcome is fair given the past, whatever the labels, so O_i - F_i is a martingale along level-i PAIRs, and optional stopping with
a bounded number of PAIRs gives E[F_i] = E[O_i]. Now take expectations in (7.2). QED.

No property of the label distribution is used, so the correlated keys of recycled qubits, such as even residues after a sum, need
no separate analysis.

Cost. A store or a PAIR costs O(n) core steps: key computation on 3n-bit labels, one indexed slot access, a constant number of gates
on addressed wires, and an O(n)-bit table update. Each is charged to an arrival, since every store and every PAIR consumes one arrival
or one recycled item that a previous PAIR produced, and the number of PAIRs at level i is at most A_i. So the stage costs O(n A_0) core
steps. Emptying the tables at the start of a batch costs O(sum_i E_i).

## 8. The schedule

Demand constants, with K from (11.0):

    Dbar = 3 K 2^m dl,     Dcap = 2^12 n Dbar,     Ccap = 2^13 n 3^ell Dbar.

Let Y be the least integer with 2^Y >= Ccap.

Two exact numerical facts: 3^41 = 36472996377170786403 < 2^65 = 36893488147419103232 and 3^53 = 19383245667680019896796723 > 2^84 = 19342813113834066795298816. So
84/53 < log2 3 < 65/41.

Size bound. Using 3^ell <= 2^(65 ell/41), ell <= 296r/2000 + 1, m <= 8650r/10000 + 1, K <= 3 * 2^13 r (as 2r + ceil(log2 n) + 30 <= 3r), dl <= r and n <= r^2,

    log2 Ccap <= (65/41)(296/2000) r + (8650/10000) r + 4 log2 r + 32 <= 1.0997 r + 4 log2 r + 32 <= 2r - 1.    (8.1)

So Y <= 2r <= n (as r <= sqrt n + 1 and n >= 2^28), and 2^Y <= 2 Ccap.

Level capacities.
- Pairing level i (0 <= i < ell): pbmax_i = min(w, floor(m + (84/53)(ell - i))). By 84/53 < log2 3,

      3^i 2^(pbmax_i) <= 3^i 2^m 3^(ell-i) = 3^ell 2^m.                              (8.3)

- Tree: lam_i = dl + i for 0 <= i <= m-1, lam_m = 1; tbmax_i = dl + i - kappa - 1 for 0 <= i <= m-2; tbmax_(m-1) = 2 (dl + m - 1) - kappa - 1.

For every b_i <= tbmax_i, in all cases

    b_i + lam_(i+1) - 2 lam_i <= -kappa.                                            (8.2)

Lemma 8.1 (capacity). For n >= 2^28: sum_i pbmax_i + sum_i tbmax_i >= r^2 >= n.

Proof. Put t = ell - i, omega_0 = 2197/2000, alpha = 296/2000, beta = 8650/10000 and c_0 = 84/53. Since w >= omega_0 r - 1 and m >= beta r, each pbmax_i >= f(t) - 1 with
f(t) = min(omega_0 r, beta r + c_0 t), which is increasing. So sum_(t=1)^ell f(t) >= integral_0^ell f(t) dt >= integral_0^(alpha r) f(t) dt, and sum_i pbmax_i >= integral_0^(alpha r) f(t) dt - ell. With
t_0 = (omega_0 - beta)/c_0 = 24751/168000 < alpha, the integral equals

    ( beta t_0 + c_0 t_0^2/2 + (alpha - t_0) omega_0 ) r^2.

Direct expansion gives sum_i tbmax_i = m dl + m^2/2 + dl + m/2 - 1 - m (kappa + 1) >= m dl + m^2/2 - m (kappa + 1). With m >= beta r and dl >= (5568/10000) r, the positive terms total at least

    ( beta t_0 + c_0 t_0^2/2 + (alpha - t_0) omega_0 + beta (5568/10000) + beta^2/2 ) r^2 >= 1.00112 r^2.

For r >= 2^14 we have ell <= 0.16 r, m <= 0.87 r and kappa + 1 <= log2 m + 3 <= log2 r + 3. So the subtracted terms are at most r (0.87 log2 r + 2.77). Finally 0.00112 r >= 0.87 log2 r + 2.77 at r = 2^14, where
18.35 >= 14.95, and for larger r because the left side grows faster (its derivative exceeds 0.87/(r ln 2)). QED.

Bit allocation. Given integer B with 1 <= B <= n, allocate exactly B bits greedily: first pb_0, ..., pb_(ell-1) in that order, pb_i = min(pbmax_i, bits still unallocated), then tb_(m-1), ..., tb_0 with
tb_i = min(tbmax_i, bits still unallocated). By Lemma 8.1 this exhausts B. Positions: pp_0 = 0, pp_(i+1) = pp_i + pb_i; tp_0 = pp_ell, tp_(i+1) = tp_i + tb_i; so tp_m = B. Every bit read below has position below B.

## 9. BATCH(supplier, B)

Input: a supplier of LEAF QUBITS: positive qubits with phase exp(2 pi i k th) for a fixed real th and a known label k, where in the ideal
run the labels are independent and uniform on [0, 2^(B+1)). Output: K roots, or ABORT. A batch starts with empty slot tables and a counter of
source acquisitions; if an acquisition would exceed Ccap, the batch ABORTs. At its end, slot qubits are measured and released.

TREE. VEC(0) = LEAF: request dl qubits by calling NEXT(ell) dl times, counting each in a counter D; if D would exceed Dcap, ABORT. These qubits form
the index register, bit j = qubit j. With tables (t0_j, t1_j), build lab[0] = sum_j t0_j and lab[x + 2^j] = lab[x] + t1_j - t0_j for x < 2^j. The
table has length 2^dl, is exactly the tensor product state in the ideal run, and is collimated to tp_0 because every difference is 0 mod 2^(tp_0).
VEC(i), i >= 1: repeat X1 = VEC(i-1), X2 = VEC(i-1), out = MERGE(X1, X2; tp_(i-1), tb_(i-1), lam_i), until out != FAIL; return out. A root is VEC(m),
evaluated depth-first. Run it K times.

Root. VEC(m) is a two-entry table with lab[0] = lab[1] mod 2^B, so its ideal state is, up to global phase,

    (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2,   W = (lab[1] - lab[0])/2^B, a known integer.     (9.1)

Label bound. Each leaf qubit enters a table entry at most once, and a batch has at most Ccap leaves. So every label in the batch is a sum of at most Ccap
leaf labels below 2^(B+1). Thus every label is below 2^(Y+n+1), which fits in 3n bits by Y <= n, and

    |W| <= 2 Ccap <= 2^(Y+1).                                                       (9.2)

Lemma 9.1 (no abort). Suppose each supplied acquisition yields a leaf qubit independently with probability at least 1/2, given the past. In the ideal run a
batch ABORTs with probability at most 2^-12/n + 2^-11/n.

Proof. Consider the same process with no caps. Every NEXT call returns with probability 1, since slots are finite and each PAIR has o = 1 with probability
1/2. By (8.2) and Lemma 6.1 each merge fails with conditional probability at most 2^-kappa given everything before it, including all pairing activity. Let
V_i bound the expected number of qubits requested by VEC(i). Then V_0 = dl and, by Wald's identity, V_(i+1) <= tt * 2 V_i with tt = 2^kappa/(2^kappa - 1). Since
2^kappa >= 2m, tt^m <= exp(m/(2m-1)) <= e < 3. So the total demand D_inf of K roots has E[D_inf] <= Dbar, and Markov gives Pr[D_inf > Dcap] <= 2^-12/n.

Now stop the uncapped process at the first time the batch finishes or the acquisition counter reaches Ccap. This bounds the number of PAIRs, by (7.2). At that time
A_ell <= D_inf, so iterating (7.3) gives

    E[A_0] <= 3^ell Dbar + sum_(i<ell) 3^i (E_i + 1) <= 3^ell (Dbar + ell 2^m + 1) <= 2 * 3^ell Dbar,

using E_i <= 2^(pbmax_i), (8.3), sum_(i<ell) 3^i <= 3^ell, and ell 2^m + 1 <= 3 K 2^m dl = Dbar, which holds since K >= ell. Since each acquisition is accepted with conditional probability at least 1/2, Wald gives expected
acquisitions at most 2 E[A_0] <= 4 * 3^ell Dbar. Markov against Ccap = 2^13 n 3^ell Dbar gives probability at most 2^-11/n. The real run coincides with the uncapped one
until a cap triggers. QED.

## 10. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and tau_j in {0,1}. Since k_j is uniform on
[0, 2^(B+1)), low_j and tau_j are independent and tau_j is a fair bit. For a batch let G be the sigma-field generated
by: all low_j of its leaves; all PAIR outcomes; all merge outcomes (e, bl); and all decisions of the controller in
that batch (slot stores and matches, FAIL and retries, aborts, assignment of qubits). G does not include
root measurement outcomes, which no decision in the batch reads. It also excludes LE's internal coins and outcomes,
which in the ideal run feed no decision.

Lemma 10.1. In the ideal run, conditional on G and on all independent randomness outside the batch, the top bits tau_j
are i.i.d. fair.

Proof. Induct over the controller's steps. Every slot key, residue, sort, rank and block partition reads only label bits
strictly below position B, because all positions used are below B (Section 8). Bits below B of a sum of leaf labels,
and of a difference modulo 2^(pp_i+pb_i) with pp_i+pb_i <= B, depend only on the low_j, since multiples of 2^B do not change them.
PAIR outcomes are uniform whatever the labels (Lemma 7.1). By Lemma 6.1 each merge outcome's conditional law, given
labels and earlier outcomes, is a function of the low_j and earlier outcomes only. So the joint law factorizes as
law(tau) x law(low) x law(outcomes and decisions | low). QED.

Incidence. An entry of a table is the sum over leaves j of x_j k_j, for a 0/1 incidence vector x. Distinct indices of a
table have distinct incidence vectors: this holds for a leaf qubit, table (0, k_j); in PAIR the map a -> (a, a xor o)
is injective; a LEAF table concatenates disjoint coordinates; and a merge re-indexes injectively pairs on disjoint
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

Throughout, K, dl, m, ell, w = O(sqrt n). Writing PP = 3^ell 2^m, we have Dcap = O(n^2 2^m) and Ccap = O(n^2 PP). All fixed loops, caps and aborts below hold on every branch.

Q. Q <= Qcap = O(n^3 PP).

S_Q. By Lemma 7.2 the pairing stage holds at most 1 + sum_i E_i <= 1 + ell 2^w qubits. The depth-first stack holds at most two index registers per level, at most
2 (m+1)(dl+m) = O(n) qubits. A merge adds O(sqrt n) qubits. LE and transforms use O(n), reset between uses. So S_Q = O(sqrt n 2^w + n).

S_C. Slot tables use O(ell 2^w n) = O(n^(3/2) 2^w) bits. Depth-first tables: at most three tables per level, each of 2^(lam_i) fields of 3n bits, plus merge scratch O((L + L') n). Since
lam_i <= dl + m - 1 and these geometric sizes sum, this is O(n 2^(dl+m)). The decoder stores K triples and K residues of O(n) bits. LE uses O(n) bits. Since w <= dl + m - log2 n for these
parameters (0.07 r >= log2 n), S_C = O(n 2^(dl+m)). These are fixed allocations.

Core steps, per batch.
- Acquisitions: at most Ccap, each O(n^2) for Mult plus O(n^(5/2)) for LE (log2 Qcap = O(sqrt n) by (8.1), so h_e = O(sqrt n)): O(n^(5/2) Ccap).
- Pairing, Section 7: O(n A_0 + sum_i E_i) = O(n Ccap), since Ccap >= 3^ell 2^m >= 2^(84 ell/53 + m) >= 2^w, as (84/53)(296/2000) + 8650/10000 > 2197/2000.
- Tree: since D <= Dcap on every branch, there are at most Dcap/dl LEAF calls at O(n 2^dl) each. A merge producing level i+1 consumes 2^(i+1) dl delivered qubits that no other merge at that
  level uses, since inputs of a failed merge are discarded. So there are at most Dcap/(2^(i+1) dl) of them, each O(n 2^(dl+i)) by Section 6. Each level costs O(n Dcap 2^dl/dl), and all m+1 levels
  cost O(m n Dcap 2^dl/dl) = O(n Dcap 2^dl) = O(n^3 2^(m+dl)).
- Decoder per stage: at most 2^(Y+8) candidates, K residues each, O(n) bits per addition: O(K n 2^Y) = O(n^(3/2) Ccap).

Over at most n batches, plus poly(n) setup (parameters, CRT, Mult constants, the table of Section 4, shift values, initial residues), core steps total O(n^(7/2) Ccap + n^4 2^(m+dl)) + poly(n). Every
loop is either fixed-length or consumes acquisitions or delivered qubits under a cap, and every PAIR consumes an arrival, so every branch terminates.

T. By (8.1), log2(S_C + S_Q + 2) = O(sqrt n). By (2.1),

    T = O(n^4 Ccap + n^(9/2) 2^(m+dl) + n Q) = O(n^6 PP + n^(9/2) 2^(m+dl)).

Exponents. Since 3^ell <= 2^(65 ell/41) and r <= sqrt n + 1,

    log2 PP <= (65/41)(296 r/2000 + 1) + 8650 r/10000 + 1 <= 1.09964 r + 2.59 <= 1.09964 sqrt n + 3.69,
    m + dl <= (8650/10000 + 5568/10000) r + 2 = 1.4218 r + 2 <= 1.4218 sqrt n + 3.43,
    w <= (2197/2000) r <= 1.0985 sqrt n + 1.1.

Therefore, jointly, on every branch of the main branch,

    T = O(n^6 2^(1.4218 sqrt n)),  S_C = O(n 2^(1.4218 sqrt n)),  S_Q = O(sqrt n 2^(1.0985 sqrt n)),  Q = O(n^3 2^(1.09964 sqrt n)).

The S_Q term n is absorbed, since n = O(sqrt n 2^(1.0985 sqrt n)). Here T is governed by the tree term, since log2 PP < m + dl.

## 15. Exact growth indices and declared envelopes

Since n^6 2^(-(0.0082) sqrt n), n^3 2^(-(0.0003) sqrt n) and sqrt n 2^(-(0.0015) sqrt n) are bounded over n >= 1, the bounds of Section 14 give T, S_C = O(2^((143/100) sqrt n)) and Q, S_Q = O(2^((11/10) sqrt n)). The finite branch
contributes only an absolute constant. The declared envelopes are B(n) = 2^((143/100) sqrt n) for T and S_C, and B(n) = 2^((11/10) sqrt n) for Q and S_Q. For B(n) = 2^(a sqrt n) with fixed a > 0,
log2 log2 B = (1/2) log2 n + log2 a, so g(B) = lim log2 log2 max(4, B(n)) / log2 n = 1/2 exactly. The index holds for these fixed exact coefficients; it does not rely on a guessed constant. The
structured objects in submission.json are exactly these envelopes.

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does not assert that robustness is impossible.

## 17. Scope and limitations

- This does not reach the research goal 2^(O(n^(1/3))); the time growth index is 1/2.
- Compared with SPC-127, Q improves from 2^((127/100) sqrt n) to 2^((11/10) sqrt n) and S_Q is smaller (11/10 against 6/5), while T and S_C are worse (143/100 against
  127/100). Neither dominates the other.
- Compared with collimation at O(n) qubits and the same source budget, T is better and S_Q is worse.
- S_C remains 2^(Theta(sqrt n)). The main-branch threshold n >= 2^28 and all polynomial factors are unoptimized.
- The pair (143/100, 11/10) is one explicit parameter choice. No other point is claimed here.
