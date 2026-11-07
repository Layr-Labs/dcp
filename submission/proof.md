# SPC-1268: SPC-127 retuned toward its framework optimum, T = O(n^6 2^((633967/500000) sqrt n)), declared time envelope E_T below 2^((127/100) sqrt n)

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single algorithm below (SPC-127 with the parameters of this snapshot, called SPC-1268) receives N in binary and fresh
independent copies of rho_s, and outputs the entire s with unconditional probability at least 1 - 2^-8 > 2/3. On EVERY execution branch
(every failure, discard and abort included) it satisfies jointly

    T = O(E_T(n)),  S_C = O(2^((317/250) sqrt n)),  S_Q = O(2^((317/250) sqrt n)),  Q = O(2^((317/250) sqrt n)),

where E_T is the stacked envelope of Section 15 with leading coefficient a_T = 633967/500000 + 10^-255 < 127/100.

All constants are absolute. Each of the four envelopes has growth index exactly 1/2 (Section 15). The fifth claim is the heralded
tolerance 1 - 1/(10^64 - 3)^4 of Section 16; in the clean problem the filter of Section 16 is the identity. The sharper main-branch bounds, from which these follow, are in Section 14. The envelope coefficients are fixed
exact rationals; no hidden constant sits inside an exponent.

Notation:
- dn = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known nonnegative integer. log means log2 unless stated otherwise.

Main-branch parameters, computed by exact integer arithmetic for n >= 2^40:

    r = ceil(sqrt n),  ell = ceil(15473 r/50000),  w = floor(633917 r/500000),
    m = ceil(15549 r/20000),  dl = ceil(122621 r/250000),  kappa = ceil(log2 m) + 1.

In decimal: ell = ceil(0.30946 r), w = floor(1.267834 r), m = ceil(0.77745 r), dl = ceil(0.490484 r).

So there are ell PAIRING LEVELS, each with a slot table of at most 2^w qubits, a collimation tree of depth m, and leaf tables built from dl
qubits. Since r >= 2^20 these satisfy ell >= 2, dl >= kappa + 1 (as 0.490484 r >= log2 r + 3), m <= r and 2^kappa >= 2m.

## 1. Provenance and what is new

Snapshot provenance. This snapshot reproduces public submission 0efb267b-c55e-49cb-946b-ea3ced57f221 (SPC-127, by qzv) unchanged
except: the title; this paragraph and the two paragraphs "New in this submission" and "Why this helps"; the four parameter ratios and
the main-branch threshold in Section 0; the upper bound on log2 3 in Section 8 (485/306 in place of 65/41) and the derived numbers
in (8.1), Lemma 8.1, Sections 13, 14, 15 and 17; the declared envelopes of Section 15, where the time envelope is the stacked
absorbed envelope E_T of my own public submission b867bd2f-8997-459c-9aa6-930bdcb9bc07, restated with Lemma 15.1; and Section 16,
which replaces the clean-input tolerance 0 by the heralded filter FILTER and tolerance 1 - 1/(10^64 - 3)^4 of my own public
submissions aeec33bc-0d38-43b1-a551-14a60353e05e and b867bd2f. The algorithm, its circuits, its lemmas and their proofs are qzv's;
only the parameter ratios, the inequalities that depend on them and the declarations change. No earlier verdict is a premise;
every step needed is restated here. The paragraph below is qzv's description of SPC-127's own provenance.

This combines two of my earlier submissions: HPC-127 (2aad498c-d5e9-4f64-a222-3b2f7f961738), which proved all four resources
O(2^((127/100) sqrt n)) with a batched pool, and SPC-138 (cca84cdb-9909-488b-9f0f-707dd7b4ed5e), which introduced streaming slot tables at a fixed
slot width. Sections 2-6 and 10-12 follow the framework of CS1 (f1481815-9577-4990-abe3-7b79fa5d9284) as adapted there: latent-label model, data
transforms, label extraction, the linear merge and its distribution-free failure bound, top-bit independence, the free-frequency decoder and the 2-adic
endgame. Everything needed is restated, so nothing depends on any earlier verdict. Collimation is from G. Kuperberg, arXiv:1112.3333. Pairing qubits with
equal low label bits is from G. Kuperberg, SIAM J. Comput. 35(1), 2005. These citations are context; every step used is proved below.

New in SPC-127 (unchanged here): a slot width that varies by level, min(w, floor(m + (84/53)(ell - i))) at level i (Section 8). Near the leaves the stream is
larger than 2^w, so the width is limited by the memory budget. Nearer the tree the stream is smaller, so the width is limited by the stream size.

New in this snapshot: nothing algorithmic. The four ratios are moved from (619/2000, 2399/2000, 779/1000, 4907/10000) to
(15473/50000, 633917/500000, 15549/20000, 122621/250000), that is, the slot width w is raised to just below the time exponent (y = X in
the framework below), so that the memory budget no longer restricts the slot tables except on the top few levels; the upper bound
65/41 on log2 3 is replaced by the convergent 485/306; and the main-branch threshold is raised from 2^28 to 2^40, which is what makes
the smaller capacity margin of Lemma 8.1 sufficient. The proved main-branch time exponent moves from 1.2697 to
c_T = 633967/500000 = 1.267934, within 1.6 * 10^-5 of the framework optimum X* = 1.26792, at the price of a larger S_Q exponent
(1.267834 against 1.1995). The declared time envelope E_T (Section 15) has leading coefficient a_T = c_T + 10^-255 < 127/100.

Why this helps. In units of sqrt n, let 2^X be the work budget and 2^y the qubit budget. Taking the better option at each stream size 2^P gives
n ~ integral_0^X max(min(P,y)/c, X-P) dP with c = log2 3. Lowering y below X loses only (X-y)^2/(2c) of the integral. With y = X the optimum is
X* = 1/sqrt(I), where P* = c/(1+c) = 0.61315 is the crossover and I = P* - P*^2/2 + (1 - P*^2)/(2c) = 0.62204, so X* = 1.26792; the
optimal ratios are beta = P* X* = 0.77742 (tree input), alpha = X*(1 - P*)/c = 0.30947 (pairing levels) and delta = X* - beta = 0.49050
(leaf), which the Section 0 ratios approximate on a 10^-5 grid with the rounding and margin losses of Lemma 8.1. This paragraph
is motivation only; the theorem rests on the explicit schedule of Section 8.

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

Two exact numerical facts: 3^53 = 19383245667680019896796723 > 2^84 = 19342813113834066795298816, and

    3^306 = 99793888233710926097676673961542382339552034110870991187709058567130998942396826836880350287497238272034603157195937657211050782186192219658614729
    < 2^485 = 99895953610111751404211111353381321783955140565279076827493022708011895642232499843849795298031743077114461795885011932654335221737225129801285632

(146 decimal digits each; 84/53 and 485/306 are convergents of the continued fraction of log2 3 = 1.5849625007...). So
84/53 = 1.58490566... < log2 3 < 485/306 = 1.58496732...

Size bound. Using 3^ell <= 2^(485 ell/306), ell <= 15473 r/50000 + 1, m <= 15549 r/20000 + 1, K <= 3 * 2^13 r (as 2r + ceil(log2 n) + 30 <= 3r for r >= 2^20), dl <= r and n <= r^2,

    log2 Ccap <= (485/306)(15473/50000) r + (15549/20000) r + 4 log2 r + 32 <= 1.267934 r + 4 log2 r + 32 <= 2r - 1.    (8.1)

(The additive constant collects 26 + 2 log2 3 + 485/306 + 1 < 32.) So Y <= 2r <= n (as r <= sqrt n + 1 and n >= 2^40), and 2^Y <= 2 Ccap.

Level capacities.
- Pairing level i (0 <= i < ell): pbmax_i = min(w, floor(m + (84/53)(ell - i))). By 84/53 < log2 3,

      3^i 2^(pbmax_i) <= 3^i 2^m 3^(ell-i) = 3^ell 2^m.                              (8.3)

- Tree: lam_i = dl + i for 0 <= i <= m-1, lam_m = 1; tbmax_i = dl + i - kappa - 1 for 0 <= i <= m-2; tbmax_(m-1) = 2 (dl + m - 1) - kappa - 1.

For every b_i <= tbmax_i, in all cases

    b_i + lam_(i+1) - 2 lam_i <= -kappa.                                            (8.2)

Lemma 8.1 (capacity). For n >= 2^40: sum_i pbmax_i + sum_i tbmax_i >= r^2 >= n.

Proof. Put t = ell - i, omega_0 = 633917/500000, alpha = 15473/50000, beta = 15549/20000, delta = 122621/250000 and c_0 = 84/53. Since w >= omega_0 r - 1 and m >= beta r, each pbmax_i >= f(t) - 1 with
f(t) = min(omega_0 r, beta r + c_0 t), which is increasing. So sum_(t=1)^ell f(t) >= integral_0^ell f(t) dt >= integral_0^(alpha r) f(t) dt, and sum_i pbmax_i >= integral_0^(alpha r) f(t) dt - ell. With
t_0 = (omega_0 - beta)/c_0 = 1624397/5250000 = 0.309408... < alpha = 0.30946, the integral equals

    ( beta t_0 + c_0 t_0^2/2 + (alpha - t_0) omega_0 ) r^2.

Direct expansion gives sum_i tbmax_i = m dl + m^2/2 + dl + m/2 - 1 - m (kappa + 1) >= m dl + m^2/2 - m (kappa + 1). With m >= beta r and dl >= delta r, the positive terms total at least

    ( beta t_0 + c_0 t_0^2/2 + (alpha - t_0) omega_0 + beta delta + beta^2/2 ) r^2 >= 1.0000203 r^2 >= (1 + 1/50000) r^2,

an exact rational inequality (the left coefficient is 1.00002033...). The subtracted terms are ell + m (kappa + 1) with ell <= alpha r + 1, m <= beta r + 1 and
kappa + 1 <= log2 m + 3 <= log2 r + 3 (as m <= r), so they are at most r ( (alpha + 1/r) + (beta + 1/r)(log2 r + 3) ). Finally r/50000 >= (alpha + 1/r) + (beta + 1/r)(log2 r + 3)
at r = 2^20, where 20.97 >= 18.20, and for larger r because the left side grows faster: its derivative is 1/50000, while the right side's derivative is at most
(beta + 1/r)/(r ln 2) <= (beta + 1)/(2^20 ln 2) < 2.5 * 10^-6. QED.

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

Finite branch (n < 2^40). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand at the first minus outcome.
Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For cand != s the two data branches are orthogonal, so each outcome is uniform. A union
bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10. All resources on this branch are bounded by an absolute constant.

Main branch (n >= 2^40). Compute a2, M, dn, J, K, the schedule, Y, and all allocations; put

    Qcap = n Ccap + K.

Run Section 11 and then Section 12 (every acquisition on either branch is served by FILTER, Section 16, the identity in the clean problem). Any ABORT stops the algorithm, releases everything and outputs 0. Since J + 1 + a2 <= log2 M + a2 = log2 N <= n, there are at most n batches,
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
parameters (w <= omega_0 r = (beta + delta) r - r/10000 <= dl + m - r/10000, and r/10000 >= 2 log2 r >= log2 n for r >= 2^20), S_C = O(n 2^(dl+m)). These are fixed allocations.

Core steps, per batch.
- Acquisitions: at most Ccap, each O(n^2) for Mult plus O(n^(5/2)) for LE (log2 Qcap = O(sqrt n) by (8.1), so h_e = O(sqrt n)): O(n^(5/2) Ccap).
- Pairing, Section 7: O(n A_0 + sum_i E_i) = O(n Ccap), since Ccap >= 3^ell 2^m >= 2^(84 ell/53 + m) >= 2^w, as (84/53)(15473/50000) + 15549/20000 = 1.267914... > 1.267834 = 633917/500000.
- Tree: since D <= Dcap on every branch, there are at most Dcap/dl LEAF calls at O(n 2^dl) each. A merge producing level i+1 consumes 2^(i+1) dl delivered qubits that no other merge at that
  level uses, since inputs of a failed merge are discarded. So there are at most Dcap/(2^(i+1) dl) of them, each O(n 2^(dl+i)) by Section 6. Each level costs O(n Dcap 2^dl/dl), and all m+1 levels
  cost O(m n Dcap 2^dl/dl) = O(n Dcap 2^dl) = O(n^3 2^(m+dl)).
- Decoder per stage: at most 2^(Y+8) candidates, K residues each, O(n) bits per addition: O(K n 2^Y) = O(n^(3/2) Ccap).

Over at most n batches, plus poly(n) setup (parameters, CRT, Mult constants, the table of Section 4, shift values, initial residues), core steps total O(n^(7/2) Ccap + n^4 2^(m+dl)) + poly(n). Every
loop is either fixed-length or consumes acquisitions or delivered qubits under a cap, and every PAIR consumes an arrival, so every branch terminates.

T. By (8.1), log2(S_C + S_Q + 2) = O(sqrt n). By (2.1),

    T = O(n^4 Ccap + n^(9/2) 2^(m+dl) + n Q) = O(n^6 PP + n^(9/2) 2^(m+dl)).

Exponents. Put c_T = 15549/20000 + 122621/250000 = 633967/500000 = 1.267934 exactly. Since 3^ell <= 2^(485 ell/306) and r <= sqrt n + 1,

    log2 PP <= (485/306)(15473 r/50000 + 1) + 15549 r/20000 + 1 <= 1.2679340 r + 2.59 <= c_T r + 2.59 <= c_T sqrt n + 3.86,
    m + dl <= (15549/20000 + 122621/250000) r + 2 = c_T r + 2 <= c_T sqrt n + 3.27,
    w <= (633917/500000) r <= 1.267834 sqrt n + 1.27.

(Exactly, (485/306)(15473/50000) + 15549/20000 = 1939939/1530000 = 1.26793398... < c_T.) Therefore, jointly, on every branch of the main branch,

    T = O(n^6 2^(c_T sqrt n)),  S_C = O(n 2^(c_T sqrt n)),  S_Q = O(sqrt n 2^(1.267834 sqrt n)),  Q = O(n^3 2^(c_T sqrt n)),   c_T = 633967/500000.

The S_Q term n is absorbed, since n = O(sqrt n 2^(1.267834 sqrt n)). Under the heralded model of Section 16 the same four bounds hold with raw
acquisitions counted (Theorem 16.3).

## 15. Exact growth indices and declared envelopes

Declared envelopes. For T declare the stacked envelope E_T below; for S_C, S_Q and Q declare B(n) = 2^((317/250) sqrt n), where
317/250 = 1.268 exceeds c_T = 1.267934 and 1.267834. Since n^3 2^(-(0.000066) sqrt n) and sqrt n 2^(-(0.000166) sqrt n) are bounded over
n >= 1, the bounds of Section 14 give S_C, S_Q, Q = O(2^((317/250) sqrt n)). The finite branch contributes only an absolute constant.
For B(n) = 2^(a sqrt n) with fixed a > 0, log2 log2 B = (1/2) log2 n + log2 a, so g(B) = lim log2 log2 max(4, B(n)) / log2 n = 1/2 exactly.

The time envelope. Let a_T = c_T + 10^-255 = 633967/500000 + 1/10^255, an exact rational whose reduced numerator and denominator each have
256 decimal digits (numerator 1267934 followed by 248 zeros and a final 1; denominator 10^255); a_T < 127/100. Let

    K = 10^256 - 1  (256 nines),   J = 10^58 - 1  (58 nines),
    d_i = 10^256 - i for i = 1, ..., 28  (so d_1 = K > ... > d_28 > 0),
    k_i = K for i = 1, ..., 27,  k_28 = J  (so 1 <= k_i <= K),

and for integers n >= 2, with L = log2 n >= 1,

    E_T(n) = 2^( a_T sqrt(n) - sum_(i=1..28) k_i n^(1/2) L^(-1/d_i) ).

The structured object of claim 0 lists E_T exactly: outer coefficient 1, outer nPower 0, outer logPower 0, the exponent term
(coefficient a_T, nPower 1/2, logPower 0), and for i = 1, ..., 28 the term (coefficient -k_i, nPower 1/2, logPower -1/d_i). This is the
envelope form of my public submission b867bd2f-8997-459c-9aa6-930bdcb9bc07 with its leading coefficient replaced by a_T.

Lemma 15.1 (absorption). Let delta_T = a_T - c_T = 10^-255 > 0. For every fixed real p >= 0, n^p 2^(c_T sqrt(n)) = O(E_T(n)).

Proof. For n >= 2,

    log2( n^p 2^(c_T sqrt n) / E_T(n) ) = -delta_T sqrt(n) + sqrt(n) sum_i k_i L^(-1/d_i) + p log2 n.

Every 1/d_i >= 1/K, every k_i <= K and L >= 1, so k_i L^(-1/d_i) <= K L^(-1/K). Let L_0 = (56 K/delta_T)^K. For L >= L_0, L^(1/K) >= 56 K/delta_T
and so sqrt(n) sum_i k_i L^(-1/d_i) <= 28 K L^(-1/K) sqrt(n) <= (delta_T/2) sqrt(n). The logarithm is then at most -(delta_T/2) sqrt(n) + p log2 n,
which tends to -infinity. Hence the ratio tends to 0, is bounded for all sufficiently large n, and finitely many smaller n contribute a finite
maximum. QED. The threshold is astronomically large; only its existence is used. All constants are independent of N, s and outcomes.

Application. Section 14 proves T = O(n^6 2^(c_T sqrt n)) on every main-branch execution, and the finite branch is an absolute constant.
Lemma 15.1 with p = 6 gives T = O(E_T(n)) on every branch, jointly with the other three envelopes and the success probability of Section 13.
Under the heralded model of Section 16, Theorem 16.3 gives the same raw bound T = O(n^6 2^(c_T sqrt n)), hence again T = O(E_T).

Growth index of E_T. Each sqrt(n) L^(-1/d_i) is o(sqrt n), so log2 E_T(n) = (a_T + o(1)) sqrt(n) and log2 log2 E_T(n) = (1/2) log2 n + log2 a_T + o(1).
The exact growth index is 1/2. E_T is a comparator-ordered restatement of the same raw bound; it adds no algorithmic content. The structured
objects in submission.json are exactly these envelopes; every coefficient is a fixed exact rational, and no hidden constant sits inside an exponent.

## 16. Error tolerance: heralded filter

Error model of the fifth structured claim (exact text):

Heralded malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires on an execution branch, and epsilon(n) the tolerated malformed fraction. Each acquired copy consists of an (n+1)-qubit register of the ideal copy's shape together with one classical herald bit f delivered with it. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed. A well-formed copy has f = 0 and its register is a fresh copy of rho_s, in tensor product with every other system (earlier copies, the adversary's system and the algorithm's registers). A malformed copy has f = 1 and its register is in an arbitrary state chosen by the adversary, possibly entangled with the adversary's private system and with other malformed copies. On every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. The herald is always correct, so malformation is detectable (an erasure-type error); its timing, its number within the promise and the malformed register contents are adversarial. In the clean problem no herald is supplied and every copy is well-formed. No source control, purification access or preparation inverse is supplied.

Let x = 10^64 - 3 = 9999999999999999999999999999999999999999999999999999999999999997, D = x^4 and epsilon_H = 1 - 1/D. D is a fixed absolute integer (log2 D < 851).

FILTER. Every source acquisition requested anywhere in Sections 11-13 (the suppliers of Sections 11 and 12 and the candidate tests of the
finite branch) is served as follows: acquire one raw copy and read its herald bit f; if f = 1, reset its n+1 qubits to |0> without any other
operation and acquire again; otherwise hand the register to the requesting step. When copies carry no herald bit (the clean problem),
FILTER is the identity. Let Qcap* be the exact clean acquisition bound of the branch: Qcap* = Qcap = n Ccap + K on the main branch
(Section 13), and Qcap* = N (n+10) on the finite branch, whose candidate tests request at most n+10 copies for each of the N candidates.
A classical raw-acquisition counter enforces the literal cutoff Qraw = D Qcap* on both branches: if the next raw acquisition would exceed
Qraw, stop, release everything and output 0. Qcap* still bounds the number of well-formed copies handed to the algorithm, exactly as
before; it does not bound raw acquisitions under the heralded model, which are bounded by Qraw instead.

Lemma 16.1 (the cutoff never binds). Under the heralded model with fraction epsilon_H, the Qraw cutoff is never reached before the
algorithm itself stops.

Proof. On either branch the clean algorithm never requests more than Qcap* copies: on the main branch each of the at most n batches stops
at its Ccap acquisition counter and the single wd = 1 level requests at most K (Section 13); on the finite branch by its explicit loop
bounds. Suppose the raw cutoff is reached while the algorithm still awaits a requested copy, so R <= Qcap* - 1 well-formed copies have been
handed over. Then Q = Qraw = D Qcap* raw copies were acquired and Q - R >= D Qcap* - Qcap* + 1 of them are malformed. The promise gives
at most floor(epsilon_H Q) = floor((1 - 1/D) D Qcap*) = D Qcap* - Qcap*, a contradiction. QED.

Lemma 16.2 (clean law). Under the heralded model, the joint law of every measurement outcome of the algorithm and of its output equals
that of the clean run.

Proof. A malformed register is reset without interacting with any algorithm register, so it is traced out; whatever the adversary does on
its private system and on malformed registers acts on systems disjoint from the algorithm's. Each well-formed copy is, at delivery, a fresh
rho_s in tensor product with every other system, irrespective of the adversary's adaptive decisions. By induction over requests, the
sequence of handed-over copies is distributed exactly as independent ideal copies supplied on request, which is the clean problem, and by
Lemma 16.1 the extra cutoff never changes the run. QED.

Theorem 16.3. Under the heralded model with fraction epsilon_H, for every N >= 2 and every s, the algorithm with FILTER outputs s with
probability at least 1 - 2^-8 > 2/3, and on every branch, counting every raw acquisition, T = O(n^6 2^(c_T sqrt n)), S_C = O(n 2^(c_T sqrt n)),
S_Q = O(sqrt n 2^(1.267834 sqrt n)) and Q <= D Qcap* = O(n^3 2^(c_T sqrt n)); hence the four declared envelopes of Section 15 hold jointly.

Proof. Success: Lemma 16.2 and Section 13. Resources: by the literal cutoff at most D Qcap* raw copies are acquired on every branch, with D
an absolute constant, so Q = O(Qcap) = O(n^3 2^(c_T sqrt n)) on the main branch and an absolute constant on the finite branch. Each raw copy
costs n+1, one herald read and, if malformed, a reset of n+1 qubits, O(n) core steps at the address charge O(sqrt n) of (2.1), plus an
increment and comparison of the counter, which has O(log2 Qcap* + log2 D) = O(sqrt n) bits; the extra work is O(D Qcap* n^(3/2)) = O(n^(9/2) 2^(c_T sqrt n)),
below the Section 14 bound. The counter adds O(sqrt n) classical bits. A malformed register occupies the n+1 qubits of the one copy the
supplier holds, already counted in Section 14, and is reset before the next acquisition. All other steps run exactly as in Section 14 on
the handed-over copies. QED.

Tolerance integers. With x as above, the displayed integers t_i satisfy t_1 * ... * t_3 = x^2 + 1 exactly (direct integer
multiplication; they need not be prime):

    t_1 = 5909009547859618446014307935656485996455360061473289284034355157
    t_2 = 8461654968574415353741992088106541809421651544931744139485636465
    t_3 = 2

Each of x - 1, x, x + 1 and every t_i has at most 64 decimal digits. The supported expression

    9999999999999999999999999999999999999999999999999999999999999996*9999999999999999999999999999999999999999999999999999999999999998*5909009547859618446014307935656485996455360061473289284034355157*8461654968574415353741992088106541809421651544931744139485636465*2/9999999999999999999999999999999999999999999999999999999999999997^4

equals (x - 1)(x + 1)(x^2 + 1)/x^4 = (x^4 - 1)/x^4 = 1 - 1/x^4 = epsilon_H, a constant in (0, 1), with normalized numerator and denominator
of 256 digits. This guarantee covers detectable (heralded) malformed copies only; no tolerance of undetectable corruption is claimed, and
this does not assert that greater tolerance is impossible. With no malformed copies the algorithm is the clean algorithm of Sections 0-14.

## 17. Scope and limitations

- This does not reach the research goal 2^(O(n^(1/3))); the time growth index is 1/2.
- Compared with SPC-127 (0efb267b), the proved time exponent improves from 1.2697 to c_T = 1.267934 and the declared time envelope from 2^((127/100) sqrt n) to E_T,
  whose leading coefficient a_T = 1.267934 + 10^-255 is below 127/100. The S_Q exponent worsens from 1.1995 to 1.267834 (declared 317/250 against 6/5), because the
  slot width is raised to the time exponent; S_C and Q are declared 317/250 against 127/100. This is a parameter retuning of qzv's algorithm toward the optimum of
  its own framework (Section 1), plus a comparator-ordered restatement of the time bound; it contains no new asymptotic idea.
- Within this framework the time exponent cannot go below X* = 1.26792 by changing ratios alone; the remaining gap 1.6 * 10^-5 is the rounding of the ratios to a
  10^-5 grid, the capacity margin 1/50000 of Lemma 8.1 and the gap between 84/53, 485/306 and log2 3.
- S_C and Q remain 2^(Theta(sqrt n)). The main-branch threshold n >= 2^40 and all polynomial factors are unoptimized; the finite branch below the threshold costs an
  absolute (astronomically large) constant, as in SPC-127.
- The ratios (15473/50000, 633917/500000, 15549/20000, 122621/250000) are one explicit parameter choice. No other point is claimed here.
