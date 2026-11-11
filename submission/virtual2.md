# Reference algorithm P for IFC-BANK-D, part 2: the chunked pool, the schedule, BATCH, MERGE4I and its failure bound

This file is part of the complete specification and proof of IFC-LIMIT-D, the reference algorithm P of proof.md; the
other parts are virtual.md and virtual3.md (Sections C and D: MERGE7 and Lemma D.1). "P Section x" and "P (x.y)" refer
to virtual.md. Sections A and B are our IFC1's Sections 6.3
and 8.1 (submission 1294d17f-2acf-4e10-9996-6b4375388f49), whose four-input merge follows e-man07's MW4
(33a6df9d-08d8-488b-a3f7-01f5f32373a4) and CW1 (cfe82a87-0d65-454e-b1df-4789dc95aab4), with these edits: the carry
called dl in IFC1 is called cq here; tables are stored with labels in full (P Section 6); kappa is that of P Section 0;
and Lemma B.1 is restated for pool-output leaves (its first two paragraphs). In Sections A and B the letters r and r' are the
two window widths of MERGE4I, not ceil(sqrt n), and L = 2^lam is the input length.

## 7.3 The chunked pool (P Section 7.3)

Sizes (Section 8): D_i = 2^cb for every i = 0, ..., ell; YIELDS Yd_i = ceil((ell - 1) D_i/(RHO ell)); RUN CAPS
Rc_ell = ceil(C_ell/(2^cb - dl)) and Rc_i = floor(Rc_(i+1) D_(i+1)/Yd_i) + 1 for i = ell-1, ..., 0. Put
rho = RHO ell/(ell - 1) = 16385 ell/(8192 (ell - 1)), so D_i/Yd_i <= rho.

Each level i < ell keeps a BUFFER Bf_i, a list of labeled qubits, initially empty, and a counter of its runs.
REQUEST(i+1), for 0 <= i < ell, returns exactly D_(i+1) qubits:
- while |Bf_i| < D_(i+1): if level i has already run Rc_i times, ABORT; obtain an input chunk of D_i qubits, from the
  supplier if i = 0 (leaf qubits, Section 11) and by REQUEST(i) otherwise; run FWLEVEL on it with Cin = D_i,
  p = pp_i, c = pb_i and q(Y+1) rounds; if its OUTPUT has fewer than Yd_i qubits, ABORT; otherwise append OUTPUT,
  in order of production, to Bf_i;
- remove the first D_(i+1) qubits of Bf_i and return them, in order.
FINAL REQUESTS. Level ell keeps no buffer. The tree (Section 9) obtains its leaf qubits by FINAL REQUESTS: each is a
call REQUEST(ell), which returns D_ell = 2^cb qubits collimated to pp_ell, placed in the LEAF BUFFER of Section 9. At
most Rc_ell final requests are made per batch; a LEAF call that would need another one ABORTs the batch instead (pool
exhaustion, Lemma 9.1). The final requests are interleaved with the tree. When the batch's tree ends, every qubit left
in the leaf buffer or in a buffer Bf_i is measured, reset and released.

Lemma 7.3 (chunked pool). (a) Every run at level i has exactly D_i inputs, all collimated to pp_i, and satisfies the
hypotheses of Lemma 7.2; every returned qubit of REQUEST(i+1) is collimated to pp_(i+1).
(b) If no run yields fewer than its Yd_i, the run-cap ABORT does not occur: level i runs at most Rc_i times.
(c) At all times |Bf_i| < D_(i+1) + D_i/2, and P holds at most 3(ell + 1) 2^cb pool qubits (leaf buffer included).
(d) At most C_0 := Rc_0 D_0 leaf qubits are requested from the supplier, N_i := Rc_i D_i <= C_0 for every i, and
C_0 <= 4 rho^ell C_ell <= 8 (ell + 1) RHO^ell C_ell.
(e) Conditional on everything before it, a run at level i ABORTs with probability at most
w D_i 2^(-3r) + 2 exp(-2^cb/(10 ell^2 w^2)). So the batch's pool stage ABORTs (other than by the supplier) with
probability at most (ell + 1) C_0 (w 2^(-3r) + 2 exp(-2^cb/(10 ell^2 w^2))).

Proof. (a) A chunk of level 0 is leaf qubits, collimated to pp_0 = 0; a chunk of level i >= 1 is OUTPUT of level
i - 1 runs, collimated to pp_(i-1) + pb_(i-1) = pp_i (Section 7.2). E_i = 2^(pb_i) <= D_i/(4 w ell) by the definition of
pbmax_i, and (1 - 2/w)^(q(Y+1)) D_i < 2^(-(Y+1)) D_i < 1 as D_i = 2^cb <= C_0 <= 2^Y. ell >= 2.
(b) Induct downward. Level ell is requested at most Rc_ell times (final requests, Section 9). Suppose level i + 1 runs (or, for i + 1 = ell, is requested)
at most Rc_(i+1) times, so level i receives at most R' <= Rc_(i+1) requests of D_(i+1). If level i runs R times, then
when its last run starts, the requests completed before the current one removed at most (R' - 1) D_(i+1) qubits, the
R - 1 earlier runs appended at least (R - 1) Yd_i, and the buffer held fewer than D_(i+1). So (R - 1) Yd_i < R' D_(i+1),
R <= floor(R' D_(i+1)/Yd_i) + 1 <= Rc_i.
(c) A run appends at most D_i/2 qubits (Section 7.2: |OUTPUT| <= Cin/2) and starts only while |Bf_i| < D_(i+1). At
any time each level holds its buffer and at most one chunk in process (its LIVE and OUTPUT lists, at most D_i
qubits), and the leaf buffer holds at most D_ell = 2^cb qubits; with D_i = 2^cb the total is below
sum_(i<ell) (D_(i+1) + D_i/2 + D_i) + D_ell <= 3 (ell + 1) 2^cb.
(d) The supplier serves at most Rc_0 chunks of D_0. N_(i-1) = (floor(N_i/Yd_(i-1)) + 1) D_(i-1) >= N_i D_(i-1)/Yd_(i-1) >= N_i,
so N_i <= N_0 = C_0; and N_(i-1) <= rho N_i + D_(i-1), with N_ell = Rc_ell 2^cb <= C_ell 2^cb/(2^cb - dl) + 2^cb
<= 2 C_ell + 2^cb <= 3 C_ell, as 2^cb >= 2 dl (F1, F2) and C_ell >= 2^H >= 2^cb (F4). Unrolling with D_i = 2^cb and
rho >= 2, C_0 = N_0 <= rho^ell N_ell + sum_(i<ell) rho^i 2^cb <= rho^ell (N_ell + 2^cb) <= 4 rho^ell C_ell, and
rho^ell <= 4 RHO^ell ((1 - 1/ell)^(-ell) <= 4), so C_0 <= 16 RHO^ell C_ell <= 8 (ell + 1) RHO^ell C_ell.
(e) Lemma 7.2 with Cin = D_i holds conditional on everything before the run, for ANY labels; its yield event is
S < (ell - 1) D_i/(RHO ell), and S is an integer, so S < Yd_i is the same event, and D_i = 2^cb.
Number the runs of level i in order; the k-th, if it occurs, aborts with conditional probability at most the stated
bound, and there are at most Rc_i runs before the first abort by (b). Summing over k <= Rc_i and i, with
sum_i Rc_i <= sum_i N_i <= (ell + 1) C_0, gives the batch bound. QED.

Fixed input sizes are the point of (e): each run's input count D_i is fixed by the schedule, not by the outcomes of the
level, so Lemma 7.2 applies verbatim to every run. The demand pattern (which runs occur, and when) depends on earlier
outcomes; the bound conditions on all of it.

## 8. The schedule (P Section 8)

Constants. RHO = 16385/8192 = 2 + 2^-13 (Lemma K). K is as in (11.0), C_ell = 2^12 n K 2^H dl, the sizes D_i = 2^cb,
Yd_i and Rc_i are those of Section 7.3, C_0 = Rc_0 D_0, and Y is the least integer with 2^Y >= C_0. Each FWLEVEL uses
rounds = q (Y + 1), q = 2^27. Here 2^H = 2^(a + 2 JI) 7^J7 (P Section 0) is an integer and H = a + 2 JI + J7 log2 7 is
a real number; "output height" below means log2 of the number of LEAF calls under one output.

Brackets. Since RHO > 2, log2 RHO > 1. Since ln 2 = sum_(k>=1) 1/(k 2^k) and all its terms are positive,
ln 2 > sum_(k=1)^8 1/(k 2^k) = 148969/215040 > 6927/10000. Since ln(1 + x) < x for x > 0,
log2 RHO = 1 + ln(1 + 2^-14)/ln 2 < 1 + 2^-14 * 10000/6927 =: HI. Since 7^16 = 33232930569601 < 35184372088832 = 2^45,
log2 7 < 45/16. So

    1 < log2 RHO < HI,   14/5 < log2 7 < 45/16,   and   HI (151/400) + 2 (11/20)(151/400) + (45/16)(667/2000) < 1731/1000 = e,     (8.5)

the last because HI (151/400) - 151/400 = 3775/113491968 < 9/32000 = e - (151/400 + 2 (11/20)(151/400) + (45/16)(667/2000)); and 14/5 < log2 7 because
7^5 = 16807 > 16384 = 2^14. Moreover (e - HI (151/400) - 2 (11/20)(151/400) - (45/16)(667/2000)) r >= 6 for r >= 2^20.

Size facts (F1)-(F6), for r >= 2^20 (n >= 2^40). Each linear inequality c r >= c' log2 r + c'' below holds at r = 2^20 and
then for all larger r, because c > c'/(r ln 2) there. Write Js = ceil((Lam - 1)/2).
(F1) n <= r^2, Lg <= 2 log2 r + 1, kappa <= log2 r + 5, 2^kappa >= 16 r, r0 >= r - 1, and
     (151/400) r - 80 log2 r - 42 <= cb <= (151/400) sqrt n - 40 log2 n (as floor((151/400) r0) >= (151/400) r - 2); in particular
     cb >= r/4 >= 2^18 and 2^cb >= 2 r.
(F2) Lam = cb - kappa - 4 satisfies (151/400) r - 81 log2 r - 51 <= Lam <= (151/400) r. ell = Lam, dl = Lam - 1 and a = 1, so
     dl >= kappa + 2, Lam >= kappa + 3, dl <= r and 2^cb >= 2 dl. JI = ceil((11/20) Lam) satisfies
     (11/20) Lam <= JI <= (11/20) Lam + 1.
(F3) JI >= (11/20) Lam >= Lam/2 + 2 >= Js + 2, so JI >= 2 and JI - 1 >= Js + 1. J7 = ceil((667/2000) r) satisfies
     (667/2000) r <= J7 <= (667/2000) r + 1, so J7 >= 1, a + JI + J7 + 1 <= (4329/8000) r + 4 <= r and
     a + JI + J7 + ell + 2 <= (7349/8000) r + 5 <= 2r. Also
     2 (11/20) Lam <= a + 2 JI <= H <= 2 (11/20) Lam + 3 + (45/16)((667/2000) r + 1) <= (43303/32000) r + 6, and
     H >= 2 (11/20) Lam >= Lam + kappa + 5 = cb + 1. The fibers w_k = max(0, 3 Lam - 2 JI - floor(14 (k+1)/5)) satisfy
     0 <= w_k <= w_0 <= (3 - 2 (11/20)) Lam - 2 <= 2 Lam and 6 Lam - kappa - 2 w_0 >= 2 Lam.
(F4) C_ell <= 3 * 2^25 r^4 2^H (K <= 3 * 2^13 r, dl <= r, n <= r^2), so log2 C_ell <= (43303/32000) r + 4 log2 r + 33;
     also C_ell >= 2^H >= 2^cb.
(F5) dl >= kappa + 2, and Lam >= kappa + 2.
(F6) log2 C_0 <= log2 (8 (ell + 1)) + HI ell + log2 C_ell <= (HI (151/400) + 43303/32000) r + 5 log2 r + 37 <= e r + 6 log2 r + 40
     <= 2r - 1, so Y <= 2r <= n.

Level capacities.
- FW level i (0 <= i < ell): pbmax_i is the largest integer b with 2^b * 4 w ell <= D_i = 2^cb, so pbmax_i = cb - g
  with g = ceil(log2 (4 w ell)) <= log2 r + 31 <= kappa + 27.
- Phase A, binary, one level (a = 1): input exponent lam_0 = dl, output exponent lam_1 = Lam = dl + 1, capacity
  tbmax_0 = dl - kappa - 1; as the ROOT of a binary tree (output exponent 1) the level has capacity
  rootA = 2 dl - kappa - 1.
- Phase I, four-input, 0 <= j <= JI-1: input exponent Lam, fiber exponent l_j = min(Lam + 1 + 2j, 2 Lam),
  r_j = 2 Lam - l_j; capacity bI_j = Lam + l_j - kappa with output exponent Lam, or rootI_j = 2 Lam + l_j - 1 - kappa
  as the root (output exponent 1). These are substitutions: bI_j = r_j + (2 l_j - Lam - kappa),
  rootI_j = r_j + (2 l_j - 1 - kappa). For j < Js, l_j = Lam + 1 + 2j and bI_j = 2 Lam + 1 + 2j - kappa. For
  j >= Js the level is SATURATED: l_j = 2 Lam, r_j = 0, bI_j = 3 Lam - kappa and rootI_j = 4 Lam - 1 - kappa.
- Phase M, seven-input (MERGE7, Section C of virtual3.md), 0 <= k <= J7-1: input exponent Lam, fiber width
  w_k = max(0, 3 Lam - 2 JI - floor(14 (k+1)/5)), capacity bM_k = 6 Lam - kappa - w_k with output exponent Lam, or
  rootM_k = 7 Lam - 1 - kappa - w_k as the root (output exponent 1). These are b = 7 lam - lam' - kappa - w of
  Section C with lam = Lam, w = w_k and lam' = Lam or 1. The fiber is set by the time accounting of Section 14:
  4 Lam - w_k <= dl + a + 2 JI + floor(14 (k+1)/5) (with equality while w_k > 0, as dl + a = Lam).

Put CP = sum_i pbmax_i = ell (cb - g), CA = tbmax_0, CA0 = rootA, for 1 <= JI' <= JI
SI(JI') = sum_(j<JI'-1) bI_j + rootI_(JI'-1), SIF = sum_(j<JI) bI_j, and for 1 <= J' <= J7
SM(J') = SIF + sum_(k<J'-1) bM_k + rootM_(J'-1). As rootI_j = bI_j + Lam - 1 and rootM_k = bM_k + Lam - 1,
SI(JI') = sum_(j<JI') bI_j + Lam - 1 and SM(J') = SIF + sum_(k<J') bM_k + Lam - 1. Hence SI(1) = 3 Lam - kappa < 4 Lam,
SI(JI') - SI(JI'-1) = bI_(JI'-1) <= 3 Lam for JI' >= 2, SM(1) - SI(JI) = bM_0 <= 6 Lam, and
SM(J') - SM(J'-1) = bM_(J'-1) <= 6 Lam for J' >= 2.

For the binary level with b_0 <= tbmax_0, and for the binary root with b <= rootA,

    b_i + lam_(i+1) - 2 lam_i <= -kappa.                                            (8.4)

(For the level, (dl - kappa - 1) + (dl + 1) - 2 dl = -kappa; for the root, (2 dl - kappa - 1) + 1 - 2 dl = -kappa.)

Lemma 8.1 (capacity). For n >= 2^40: CP + CA + SM(J7) >= r^2 >= n, and CP >= 7 Lam.

Proof. CA >= 0 by (F2). Pool. cb - g = Lam + kappa + 4 - g >= Lam - 23, so CP = Lam (cb - g) >= Lam^2 - 23 Lam, and in
particular CP >= 7 Lam as Lam >= 30.
Four-input levels. By (F3), JI - 1 >= Js, so the levels j < Js are unsaturated and the levels Js <= j < JI saturated.
Then SIF = sum_(j<Js) (2 Lam + 1 + 2j) + (JI - Js) 3 Lam - kappa JI = 3 Lam JI - Js (Lam - Js) - kappa JI, using
sum_(j<Js) (2j + 1) = Js^2. As Js (Lam - Js) <= Lam^2/4 and JI >= (11/20) Lam (F2),
SIF >= 3 (11/20) Lam^2 - Lam^2/4 - kappa JI.
Seven-input levels. SM(J7) - SIF = sum_(k<J7) (6 Lam - kappa - w_k) + Lam - 1 >= 6 Lam J7 - kappa J7 - sum_(k<J7) w_k.
Put Y1 = 3 Lam - 2 JI + 1 <= (3 - 2 (11/20)) Lam + 1 (F2). As floor(14 m/5) >= 14 m/5 - 1,
w_(m-1) <= u(m) := max(0, Y1 - 14 m/5) for m >= 1, and u is nonincreasing, so u(m) <= integral_(m-1)^m u and
sum_(k<J7) w_k <= integral_0^infinity u = 5 Y1^2/28. As (3 - 2 (11/20)) <= 2,
Y1^2 <= (3 - 2 (11/20))^2 Lam^2 + 4 Lam + 1, and (5/28)(4 Lam + 1) <= Lam. With J7 >= (667/2000) r (F3) and JI + J7 <= r,

    CP + CA + SM(J7) >= f(Lam) - kappa r,   f(x) = (983/560) x^2 + (6 (667/2000) r - 24) x,

where 983/560 = 3/4 + 3 (11/20) - (5/28)(3 - 2 (11/20))^2; the linear terms are -23 Lam (pool) and -Lam (fibers).
f is increasing for x >= 0, as 6 (667/2000) r >= 24, and (151/400) r >= Lam >= (151/400) r - X > 0 with X = 81 log2 r + 51 (F2). So,
expanding and dropping the positive terms (983/560) X^2 and 24 X,

    f(Lam) >= f((151/400) r - X) >= (983/560)((151/400)^2 r^2 - 2 (151/400) r X) + 6 (667/2000) r ((151/400) r - X) - 24 (151/400) r
           = (90095207/89600000) r^2 - (74509/22400) r X - (453/50) r.

With kappa <= log2 r + 5 (F1) this gives

    CP + CA + SM(J7) >= r^2 + r [ (495207/89600000) r - (6057629/22400) log2 r - 4114903/22400 ].

At r = 2^20 the bracket is 5795.3... - 5408.6... - 183.7... > 0 (about 203), and its derivative
(495207/89600000) - (6057629/22400)/(r ln 2) is positive there and beyond. QED.

Bit allocation. Given an integer B with 1 <= B <= n, the TREE SHAPE and the bits are fixed as follows.
- If B <= CP + CA0, the tree is BINARY: the Phase A level 0 is its root (output height a = 1). Allocate exactly B
  bits greedily: first pb_0, ..., pb_(ell-1) in that order, pb_i = min(pbmax_i, bits still unallocated), then
  tb_0 = min(rootA, still unallocated).
- Otherwise, if B <= CP + CA + SI(JI), let JI' be the least integer in [1, JI] with CP + CA + SI(JI') >= B. The tree is
  FULL4: the Phase A level 0 (not a root) and Phase I levels 0, ..., JI'-1 with root JI' - 1, output height
  1 + 2 JI'. Phase I level j gets exactly bI_j bits for j < JI' - 1 and the root gets rootI_(JI'-1). The other
  B' = B - SI(JI') bits are allocated greedily to pb_0, ..., pb_(ell-1), then tb_0 with tbmax_0.
  Here 0 <= B' <= CP + CA: the upper bound is the choice of JI'; for JI' = 1, B > CP + CA0 >= CP >= 4 Lam > SI(1); for
  JI' >= 2, minimality gives B > CP + CA + SI(JI' - 1) and SI(JI') - SI(JI' - 1) <= 3 Lam <= CP.
- Otherwise let J' be the least integer in [1, J7] with CP + CA + SM(J') >= B (it exists by Lemma 8.1). The tree is
  FULL7: the Phase A level 0 and all Phase I levels 0, ..., JI-1 (none of them a root), then Phase M levels
  0, ..., J'-1 with root J' - 1, output height a + 2 JI + J' log2 7. Phase I level j gets exactly bI_j bits, Phase M
  level k gets exactly bM_k bits for k < J' - 1, and the root gets rootM_(J'-1). The other B' = B - SM(J') bits are allocated
  greedily to pb_0, ..., pb_(ell-1), then tb_0 with tbmax_0. Here 0 <= B' <= CP + CA: the upper bound is the choice
  of J'; for J' = 1, B > CP + CA + SI(JI) and SM(1) - SI(JI) = bM_0 <= 6 Lam <= CP; for J' >= 2, minimality gives
  B > CP + CA + SM(J' - 1) and SM(J') - SM(J' - 1) = bM_(J'-1) <= CP.
So every allocation exhausts B, every Phase I and Phase M level is FULL, and every other level gets at most its
capacity. Positions: pp_0 = 0, pp_(i+1) = pp_i + pb_i; tp_0 = pp_ell, then the tree levels in order of height (Phase A
level 0, then the Phase I levels in order, then the Phase M levels in order), each starting where the previous ends.
The last ends at B, so every bit read below has position below B.

MERGE4I parameters. At Phase I level j put lam = Lam, l = l_j, r = r_j, r' = b_j - r_j and lam' = Lam (if level j is
not the root) or 1 (the root); since the level is full, r' = 2 l_j - lam' - kappa. The preconditions of Section A hold: Lam >= kappa + 2
(F5); Lam + 1 <= l_j <= 2 Lam by the definition of l_j; r_j = 2 Lam - l_j >= 0 (r_j = 0 exactly at the saturated
levels, the case r = 0 of Section A); lam' >= 1; r' >= 2 (Lam + 1) - Lam - kappa >= 3 (F5); l_j >= kappa + 3. kappa here
is the kappa of Section 0 (so 2^kappa >= 16r), and mu4 = 2^(lam' + kappa), Cp = 8 mu4 + 1 <= 2^(Lam + kappa + 4) = 2^cb.

MERGE7 parameters. At Phase M level k put lam = Lam, w = w_k, lam' = Lam (if level k is not the root) or 1 (the
root), and b = b_k; since the level is full, b = 7 Lam - lam' - kappa - w_k (bM_k or rootM_k). The preconditions of
Section C hold: Lam >= kappa + 2 (F5); 0 <= w_k <= 2 Lam and b - w_k >= 6 Lam - kappa - 2 w_0 >= 2 Lam (F3); lam' >= 1. Here mu7 = 2^(lam' + kappa),
Cp = 8 mu7 + 1 <= 2^(Lam + kappa + 4) = 2^cb, and Cq = 2^(Lam+1) + 1 <= 2^cb.

## 9. BATCH(supplier, B) (P Section 9)

Input: a supplier of LEAF QUBITS: positive qubits with phase exp(2 pi i k th) for a fixed real th and a known label k,
where in the ideal run the labels are independent and uniform on [0, 2^(B+1)), served in chunks of D_0 on request.
Output: K measured-ready roots, or ABORT. A leaf qubit is a labeled qubit with table (0, k).

1. LEAF SUPPLY. The tree draws leaf qubits from a LEAF BUFFER, a list of labeled qubits collimated to pp_ell,
   initially empty. A LEAF call that finds fewer than dl qubits in the leaf buffer first measures, resets and releases
   them, and then makes a FINAL REQUEST, REQUEST(ell) of Section 7.3, which puts D_ell = 2^cb qubits collimated to
   pp_ell into the leaf buffer; if Rc_ell final requests have already been made in this batch, the batch ABORTs
   instead (POOL EXHAUSTION). An ABORT of the supplier or of Section 7.3 is an ABORT of the batch. After the K roots
   (or an ABORT) the leaf buffer and every buffer of Section 7.3 are measured, reset and released.
2. TREE (shape and bits from Section 8). VEC(0) = LEAF: take the next dl qubits of the leaf buffer (step 1). Their qubits form the index register, bit j = qubit j. With tables (t0_j, t1_j), build lab[0] = sum_j t0_j
   and lab[x + 2^j] = lab[x] + t1_j - t0_j for x < 2^j. The table has length 2^dl, is exactly the tensor product state
   in the ideal run, and is collimated to tp_0 because every difference is 0 mod 2^(tp_0).
   A binary level i (input exponent dl + i) produces its output by: repeat X1, X2 = two outputs of the level below
   (LEAF for i = 0), out = MERGE(X1, X2; p, b_i, lam'), with p its start position, lam' = lam_(i+1) or 1 at the
   binary root, until out != FAIL.
   A Phase I level j produces its output by: repeat X1, X2, X3, X4 = four outputs of the level below (Phase A level
   a - 1 for j = 0), out = MERGE4I(X1, X2, X3, X4; p, r_j, b_j - r_j, lam', l_j) (Section A, parameters of Section 8),
   until out != FAIL.
   A Phase M level k produces its output by: repeat X1, ..., X7 = seven outputs of the level below (Phase I level
   JI - 1 for k = 0), out = MERGE7(X1, ..., X7; p, w_k, b_k, lam') (Section C, parameters of Section 8), until out != FAIL.
   A root is an output of the root level, evaluated depth-first. Run it K times (unless the batch ABORTs).

Root. A root is a two-entry table with lab[0] = lab[1] mod 2^B, so its ideal state is, up to global phase,

    (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2,   W = (lab[1] - lab[0])/2^B, a known integer.     (9.1)

Label bound. Each leaf qubit enters a table entry at most once and all pool qubits are distinct, so every label in
the batch is a sum of at most C_0 leaf labels below 2^(B+1) (Lemma 7.3(d)). Thus every label is below 2^(Y+n+1), which
fits in 3n bits by Y <= n, and

    |W| <= 2 C_0 <= 2^(Y+1).                                                        (9.2)

Lemma 9.1 (no pool exhaustion). In the ideal run, conditional on everything before the batch (as in Section 10, LE's
internal coins and test outcomes, which in the ideal run feed no decision, are not conditioned on), the batch ends in
POOL EXHAUSTION with probability at most 2^-10/n.

Proof. Each final request contributes floor(2^cb/dl) LEAF calls, so before an exhaustion the batch's LEAF calls have
taken at least Rc_ell (2^cb - dl) >= C_ell qubits while fewer than K roots are finished. Extend the leaf supply by
phantom qubits: once Rc_ell final requests are used, let each further LEAF call take dl phantom qubits, each with a
fresh table (0, 2^(pp_ell) u), u independent and uniform on [0, 2^(B+1-pp_ell)), instead of aborting, so that Lemma 6.1
and Lemmas B.1 and D.1 apply throughout (a phantom is a source coordinate whose label bits at positions >= pp_ell are uniform). By (8.4) and Lemma 6.1 each binary merge fails with conditional probability
at most 2^-kappa given everything before it, by Lemma B.1 each MERGE4I and by Lemma D.1 each MERGE7 with probability below 2^(2-kappa). Let A_h
bound the expected number of pool qubits consumed by one output of the level of output height h. Then A_0 = dl and,
by Wald's identity, A_(h+1) <= 2 A_h/(1 - 2^-kappa) for a binary level and A_(h+2) <= 4 A_h/(1 - 2^(2-kappa)) for a
Phase I level and A_(h + log2 7) <= 7 A_h/(1 - 2^(2-kappa)) for a Phase M level (heights are real numbers, Section 8). Wald's identity needs each attempt's failure bound conditional on the controller's history (the
outcomes and decisions before the attempt, together with the conditioning above). That history excludes LE's internal
records and reads leaf-label bits of the attempt's inputs only below its start position p (apart from the supplier's
acceptance events k < 2^dn of Section 11, which Hp contains and which leave each accepted label uniform on
[0, 2^(B+1))), so it lies in the
attempt's sigma-field Hp of Lemma B.1 or D.1, and the tower property gives the bound given the history. This includes the
FW-stage runs that final requests trigger between tree attempts: they act on qubits other than the attempt's inputs or
on their ancestors before the attempt, and read label bits only below pp_(i+1) <= pp_ell <= p (Section 7.2), so they lie
in Hp; Lemma B.1's factorization covers them as FW-stage steps. There are at most a + JI + J7 <= r levels and 4 * 2^-kappa <= 1/(4r), so the product of the factors
1/(1 - .) is at most (1 - 1/(4r))^(-r) <= 2. So K roots consume at most 2 K 2^H dl qubits in expectation, and Markov
against C_ell = 2^12 n K 2^H dl bounds by 2^-11/n the probability that they consume C_ell or more. The phantom run
coincides with the real run until exhaustion, and an exhaustion needs C_ell or more qubits taken before K roots
finish. QED.

Lemma 9.2 (pool yield). In the ideal run, the FW stage of a batch (all its runs, final requests included) aborts other
than by the supplier with probability at most (ell + 1) C_0 (w 2^(-3r) + 2 exp(-2^cb/(10 ell^2 w^2))).

Proof. Lemma 7.3(e). QED.

## A. MERGE4I(X1, X2, X3, X4; p, r, r', lam', l)

Precondition: X1..X4 are phase vectors from pairwise disjoint sets of copies, of length L = 2^lam, collimated
to p, with index registers x1..x4; write lab_t[x] = c_t + 2^p h_t[x] (0 <= c_t < 2^p), as collimation allows; lam >= kappa + 2,
lam + 1 <= l <= 2 lam, r = 2 lam - l, lam' >= 1, r' = 2l - lam' - kappa >= 1 (kappa as in Section 0). Put
b = r + r', mX = 2^l = L^2/2^r, mu4 = 2^(lam' + kappa), Cp = 8 mu4 + 1; so 2r + r' = 4 lam - lam' - kappa.
SATURATED case r = 0 (l = 2 lam): window W0 and every r-bit register below are empty, rho_t = 0, vX = vY = 0,
gX = cAB, gY = cCD, step 1 measures nothing (v = v2 = 0), X_0 and Y_0 are all L^2 = mX pairs, so step 2 never
declares FAIL, and for each x1 the run of x2 is all of [0, L). Everything below holds verbatim with r = 0. Residues:
rho_t = h_t mod 2^r (window W0: bits p..p+r-1) and sg_t = floor(h_t/2^r) mod 2^r' (window W1: bits p+r..p+b-1). Carries: cAB = floor((c_1 + c_2)/2^p),
cCD = floor((c_3 + c_4)/2^p), cq = floor(((c_1 + c_2) mod 2^p + (c_3 + c_4) mod 2^p)/2^p), and
car = floor((c_1 + c_2 + c_3 + c_4)/2^p) = cAB + cCD + cq. For a pair (x1, x2) let
vX = (rho_1 + rho_2 + cAB) mod 2^r (bits p..p+r-1 of lab_1 + lab_2), gX = floor((rho_1 + rho_2 + cAB)/2^r) in
{0,1}, and the key kX = sg_1 + sg_2 + gX in [0, 2^(r'+1)); define vY, gY, kY for (x3, x4) with cCD.

Window identity. With h_t = rho_t + 2^r sg_t + 2^b u_t and S = lab_1 + lab_2 + lab_3 + lab_4 for a tuple,

    floor(S/2^p) = car + h_1 + h_2 + h_3 + h_4 = (vX + vY + cq) + 2^r (kX + kY) + 2^b (u_1 + u_2 + u_3 + u_4),   (6.4)

as cAB + rho_1 + rho_2 = vX + 2^r gX and cCD + rho_3 + rho_4 = vY + 2^r gY. So bits p..p+r-1 of S are
(vX + vY + cq) mod 2^r, and bits p+r..p+b-1 are (kX + kY + c0) mod 2^r', c0 = floor((vX + vY + cq)/2^r) in {0,1}.

1. LOOKUP rho_1, rho_2 into fresh registers, add them and cAB mod 2^r cleanly into a fresh Rz, clear the two by
   repeating the lookups, measure Rz (outcome v), reset it. Same on x3, x4 with cCD (outcome v2). Let the pair fibers
   X_v and Y_v2 be the sets of pairs (x1, x2) with vX = v and (x3, x4) with vY = v2.
2. Cutoff (classical). Merge-sort the x2 by (rho_2, x2) and the x4 by (rho_4, x4). For each x1 the x2 with
   rho_2 = (v - cAB - rho_1[x1]) mod 2^r form one contiguous run, found by binary search; the run lengths sum to
   |X_v|, and likewise for |Y_v2|. If |X_v| > 2 mX or |Y_v2| > 2 mX, declare FAIL.
3. LOOKUP h_t mod 2^b (t = 1..4), add them and car mod 2^b cleanly into a fresh Rw, clear the lookups, CNOT bits
   r..b-1 of Rw into a fresh r'-bit Ru, and uncompute Rw. Ru holds bits p+r..p+b-1 of S. Measure Ru (outcome v'),
   reset it. Let Z = {tuples of X_v x Y_v2 with bits p+r..p+b-1 of S equal to v'}, sz = |Z|.
4. Listing (classical). Re-sort the x2 by (rho_2, sg_2, x2) and the x4 by (rho_4, sg_4, x4): the runs are the
   same sets (their ends found again by binary search on rho_2), with sg nondecreasing along each, and gX is constant on the run of x1. STREAM X, a class-restricted Schroeppel-Shamir stream: a min-heap holds, for
   each x1 with a nonempty run, the key kX of x1 with its next unread run position; pop the minimum, output that
   pair, push the next position of that run. As kX is nondecreasing along runs, STREAM X outputs X_v once each in
   nondecreasing kX. STREAM Y outputs Y_v2 in nonincreasing kY likewise (runs read backwards, max-heap). Each heap
   holds at most L entries of O(lam + r') bits. Neither X_v nor Y_v2 is stored as a table: the stored data are the
   sort orders, runs, heaps, Buf (at most Cp pairs of one run) and Tl.
   Put c0 = floor((v + v2 + cq)/2^r) and tg = ((v' - c0) mod 2^r') + g 2^r' (g = 0..3). As
   0 <= kX + kY <= 2^(r'+2) - 2, by (6.4) a tuple of X_v x Y_v2 is in Z iff kX + kY = tg for exactly one g. For
   g = 0..3 in order, restart both streams and scan with heads hx, hy: if kX(hx) + kY(hy) < tg read the next X
   pair (rule 1); if > tg read the next Y pair (rule 2); if = tg (rule 3) read the whole run of Y pairs with key
   kY(hy), keeping the first min(run length, Cp) of them in a buffer Buf, then the whole run of X pairs with key
   kX(hx), appending to a list Tl the 4-tuple of each X pair read with each Buf entry. Stop the listing as soon
   as |Tl| = Cp; a scan ends when a stream is exhausted.
   Claim: if sz <= Cp, Tl lists Z exactly once each; otherwise Tl lists exactly Cp distinct elements of Z.
   Proof. Appended tuples have kX + kY = tg, so they lie in Z; they are distinct, as a scan reads each pair once and
   a tuple has only one g. Let (xi, eta) be in Z with
   kX(xi) + kY(eta) = tg, in a scan without stop. While eta is unread, kY(eta) <= kY(hy), so rule 1 cannot pass
   over xi; while xi is unread, kX(xi) >= kX(hx), so rule 2 cannot pass over eta. So the first step reading xi or
   eta is a rule 3 step with both unread before it; there kX(xi) >= kX(hx), kY(eta) <= kY(hy) and equal sums give
   kX(xi) = kX(hx) and kY(eta) = kY(hy), so both lie in the runs read whole, and (xi, eta) is appended unless Buf
   cut its Y run. Buf cuts a run only if it has more than Cp pairs; its X run is nonempty, so the first X pair
   read fills Tl to Cp, and then sz > Cp. QED. Let tl = |Tl| = min(sz, Cp).
   Before the measurement of v', no branch or FAIL decision of this merge depends on label bits at positions
   >= p + r: the only one, in step 2, depends on bits below p + r.
5-8. (These follow e-man07's MW4.) (5) R has ceil(log2(Cp + 1)) bits and Rf one qubit, both 0. For each row rho of Tl compute
   [(x1,x2,x3,x4) = Tl[rho]] with a Toffoli chain on O(lam) scratch, CNOT it into Rf and onto the bits of R where
   rho has a 1, and uncompute; rows being distinct, R = rho and Rf = 1 on Tl, R = Rf = 0 elsewhere. Measure Rf; if
   Rf = 0 declare FAIL. (6) Measure bl = floor(R/2^lam');
   if (bl + 1) 2^lam' > tl declare FAIL. (7) For y in [0, 2^lam'), LOOKUP y -> Tl[bl 2^lam' + y] on the low lam'
   bits of R, XORing into x1..x4, which become |0>; reset them, Rf and the high bits of R from known values.
   (8) Output the low lam' bits of R as the index register, with lab[y] the sum of the four input labels of
   Tl[bl 2^lam' + y], stored in full (P Section 6): by (6.4), on Z the integer car + h_1 + ... + h_4 is congruent to
   E = ((v + v2 + cq) mod 2^r) + 2^r v' modulo 2^b, so every lab[y] is congruent to
   c' = c_1 + c_2 + c_3 + c_4 - car 2^p + 2^p E modulo 2^(p+b).

On FAIL all inputs and registers are reset and released, and the inputs are never reused. All registers and
arrays have fixed sizes, set by L, r, r', lam' and kappa.

Correctness (ideal run). Before step 1 the state is the product of the inputs: equal magnitudes over the L^4
tuples, with phases 2 pi (sum of labels) th. Steps 1, 3, 5 and 6 compute functions of the tuple into clean
registers and measure them; steps 2 and 4 act on nothing in this state. So after step 6 the state is the
equal-magnitude superposition over the 2^lam' tuples of block bl with their original phases, and step 7 maps
each to its y bijectively. The output is a phase vector with table lab, collimated to p+b, since every label is
congruent to c' modulo 2^(p+b).

Lemma A.1 (failure identity). For ANY input tables collimated to p, the laws of the measurements of steps 1, 3,
5 and 6 depend only on label bits below p+b, and with sz = sz(v,v2,v') and tl = min(sz, Cp),

    Pr[FAIL] = sum_((v,v2) cut) |X_v| |Y_v2| / L^4 + sum_((v,v2) not cut) sum_(v') [ (sz - tl) + (tl mod 2^lam') ] / L^4,

where "(v,v2) cut" means that step 2 declares FAIL. The terms (tl mod 2^lam') sum to less than
2^(2r + r' + lam')/L^4 = 2^(-kappa).

Proof. Each measurement is a computational-basis measurement of a function of the tuple on an equal-magnitude
superposition, so its law is a ratio of counts, independent of phases. Step 1's two measurements act on
disjoint registers, so (v, v2) has probability |X_v| |Y_v2|/L^4; given (v, v2) not cut, v' has probability
sz/(|X_v| |Y_v2|); given v', Rf = 0 has probability (sz - tl)/sz; given Rf = 1, R is uniform on [0, tl) and step
6 fails with probability (tl mod 2^lam')/tl. Multiplying and summing gives the identity. There are 2^(2r + r')
triples (v, v2, v'), and tl mod 2^lam' < 2^lam'. QED.

Cost on every branch. Steps 1, 3: 24 lookup passes of L rows with O(lam + b)-bit fields. Steps 2, 4: O(L lam)
comparisons of O(lam + b)-bit keys and O(L) binary searches; after step 2 each of the four scans reads at most
|X_v| + |Y_v2| <= 4 mX pairs, each a heap operation of O(lam) comparisons of O(lam + r')-bit keys, with at most one
Buf write per Y pair and at most Cp appends of O(lam) bits. Steps 5-8: one pass of tl <= Cp rows with O(lam)
control bits, one lookup pass of 2^lam' rows, 2^lam' additions of O(n)-bit high parts. Total
O((L + mX) lam (lam + b) + Cp lam + 2^lam' (lam + n)) core steps; quantum scratch O(lam + b) beyond the index
registers; classical scratch (sort orders, runs, heaps, Buf, Tl, block table) O((L + Cp)(lam + b)) bits, fixed.


## B. Failure bound for MERGE4I on pool-output leaves


Lemma B.1. In the ideal run, consider a MERGE4I attempt at Phase I level j of a batch, with p its start position,
lam = Lam, l = l_j, r = r_j, r' = b_j - r_j and lam' = Lam (or 1 at the root). Let Hp be the sigma-field generated by everything that
happened before its step 1 that a controller decision can read, except the label bits at positions >= p of the
leaves of its four inputs: the bits below p of those labels; the FW and PREP outcomes, the merge, MERGE4I and MERGE7
outcomes with their counts, runs and lists, the coins and the controller decisions of all earlier steps; and
everything on other copies. Exactly as for the sigma-field G of P Section 10, Hp does NOT contain LE's internal coins
and test outcomes on the copies of these leaves (in the ideal run LE returns the latent label itself, and its internal
records feed no decision; they do reveal label bits, which is why they are excluded), nor root measurement outcomes
of the current batch, which are taken after BATCH returns (those of earlier batches are on other copies). (The input tables also record the higher bits; Hp does not contain them.)
Then Pr[FAIL | Hp] <= 6 * 2^(-l) + 2^(-kappa - lam') + 2^(-kappa) < 2^(2 - kappa).

Proof. Here a LEAF means a source coordinate of P Section 10: a leaf qubit of the supplier, with label k_j uniform on
[0, 2^(B+1)), or a phantom qubit of Lemma 9.1, with label 2^(pp_ell) u_j and u_j uniform. By the incidence paragraph of
P Section 10, every table entry of the four inputs is the sum of the labels over a 0/1 incidence set of leaves, distinct
entries of one table have distinct incidence sets, and the four inputs use pairwise disjoint sets of leaves (pool
qubits are distinct). Let Lv be the set of leaves of the four inputs. For j in Lv write
k_j = lo_j + 2^p g_j + 2^(p+r) g'_j + 2^(p+b) u_j with 0 <= lo_j < 2^p, 0 <= g_j < 2^r, 0 <= g'_j < 2^r'. This is
possible as p + b <= B, and since p >= pp_ell the digits g_j, g'_j are uniform and independent of each other and of
lo_j, also for phantoms.

Factorization. Every earlier step that involves a leaf of Lv is an FW-stage step (keys modulo 2^(pp_i + pb_i) with
pp_i + pb_i <= pp_ell <= p, PREP and FW outcomes whose laws do not depend on labels, P Lemma 7.1(a)), a merge,
MERGE4I or MERGE7 at a lower level, with p' + b' <= p, an LE acceptance test, or a controller decision. (An acceptance test
only conditions the leaf label to the uniform law on [0, 2^(B+1)) stated above, so it carries no information on the
digits beyond that law. Given k, LE's tests leave chi_k and every spectator unchanged (P Section 5), so dropping their
outcomes leaves the joint law of the labels and all other records unchanged.) By P Lemmas 6.1 and 7.1(a)
and Lemmas A.1 and C.2 those laws, keys, residues, sort keys, counts, ranks, lists and block choices read only label bits below
p, and bits below p of a sum of leaf labels depend only on the lo_j. Steps elsewhere use disjoint copies. So, exactly
as in the proof of P Lemma 10.1 with p in place of B, conditional on Hp the pairs (g_j, g'_j) (j in Lv) are i.i.d. uniform on
[0, 2^r) x [0, 2^r'). Let Hp' be generated by Hp and the g_j (j in Lv); conditional on Hp' the g'_j are i.i.d.
uniform. The incidence set I(.) of each pair and each tuple is Hp-measurable; distinct pairs, and distinct
tuples, have distinct incidence sets (concatenation and re-indexing, as above), so at most one pair (x1, x2),
one pair (x3, x4) and one tuple have an empty one.

Pairwise independence. Let H be Hp or Hp', s >= 1, and let the elements e of a finite H-measurable family have
pairwise distinct H-measurable incidence sets I(e) and residues R(e) = (f(e) + sum_(j in I(e)) z_j) mod 2^s, with f(e)
H-measurable and the z_j i.i.d. uniform on [0, 2^s) given H. For fixed c let S count the e with I(e) nonempty and
R(e) = c. Each such R(e) is uniform, so E[S | H] is their number over 2^s. For distinct nonempty I(e), I(e')
take j in the symmetric difference, say j in I(e') \ I(e), and i' in I(e); the map (z_(i'), z_j) ->
(R(e), R(e')), other coordinates fixed, has matrix [[1,0],[1,1]] if i' in I(e') and the identity otherwise, both
invertible over Z/2^s. So the indicators are pairwise independent and Var[S | H] <= E[S | H].

Stage 1. (If r = 0 this stage is vacuous: X_0 and Y_0 have L^2 = mX elements, no cut occurs, and the cut term below
is 0.) A pair's label sum is the sum of the k_j over its incidence set I, so vX = (f0 + sum_(j in I) g_j) mod 2^r with f0 = floor((sum_(j in I) lo_j)/2^p),
Hp-measurable. Fix v; with H = Hp, s = r, z = g, the count S of pairs with nonempty incidence and vX = v has
E[S | Hp] <= L^2/2^r = mX, and |X_v| <= S + 1. If |X_v| > 2 mX then S >= 2 mX, so Dv := S - E[S | Hp] >= mX >= 1
and |X_v| <= Dv + mX + 1 <= 3 Dv <= 3 Dv^2/mX. Hence E[ |X_v| [|X_v| > 2 mX] | Hp ] <= 3 Var[S | Hp]/mX <= 3.
The same holds for Y_v2.

Stage 2. All X_v, Y_v2 are Hp'-measurable. Fix (v, v2) with |X_v|, |Y_v2| <= 2 mX, and fix v'. Likewise, bits
p+r..p+b-1 of the label sum of a tuple e are (f1 + sum_(j in I(e)) g'_j) mod 2^r' with
f1 = floor((sum_(j in I(e)) (lo_j + 2^p g_j))/2^(p+r)), Hp'-measurable. With H = Hp', s = r', z = g', the count S'
of tuples of X_v x Y_v2 with nonempty incidence and W1 value v' has E[S' | Hp'] <= |X_v| |Y_v2|/2^r' <=
4 mX^2/2^r' = 4 mu4 (as 2l - r' = lam' + kappa). Since sz <= S' + 1 and Cp = 8 mu4 + 1,
sz - tl = (sz - Cp)_+ <= (S' - 8 mu4)_+. If S' > 8 mu4 then Dz := S' - E[S' | Hp'] > 4 mu4 and
S' - 8 mu4 <= Dz <= Dz^2/(4 mu4). So E[sz - tl | Hp'] <= Var[S' | Hp']/(4 mu4) <= 1.

Summing. Take E[. | Hp] of Lemma A.1. As sum_(v2) |Y_v2| = sum_v |X_v| = L^2, the cut term is at most
sum_v |X_v| [|X_v| > 2 mX]/L^2 + sum_(v2) |Y_v2| [|Y_v2| > 2 mX]/L^2, of expectation at most
6 * 2^r/L^2 = 6 * 2^(-l). The overflow term sums (sz - tl)/L^4 over at most 2^(2r + r') triples with (v, v2) not
cut, an Hp'-measurable condition, so conditioning on Hp' first bounds it by 2^(2r + r')/L^4 = 2^(-kappa - lam').
The block term is below 2^(-kappa) (Lemma A.1). As l >= kappa + 3 and lam' >= 1, the total is at most
(3/4 + 1/2 + 1) 2^(-kappa) < 2^(2 - kappa). QED.

The bound conditions on no outcome of the attempt itself: within the attempt, v' is measured before the listing of
step 4, and no branch or FAIL decision before it reads label bits at positions >= p + r. It holds for every attempt,
retries included, since a retry uses fresh pool qubits whose leaves are not in any earlier attempt's input. It is used
in P Lemma 9.1.
