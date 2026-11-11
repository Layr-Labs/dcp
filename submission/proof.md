# F-SPQ65Q118: F-LIMIT's recycling instrument in a capped chunked pool with fewer levels, S_Q = O(2^((13/20) sqrt n)), Q = O(2^((59/50) sqrt n)) and T = S_C = O(2^((27/20) sqrt n))

Files. The complete specification and proof of the algorithm F-SPQ65Q118 are this file and virtual.md. They share one section
numbering. This file holds Sections 0, 1, 7.3, 8, 9, 10, 14, 15 and 17. virtual.md holds Sections 2-6.2, 7, 7.1, 7.2, 11,
12, 13 and 16, which are the text of our IFC-LIMIT (Section 1) with one name changed. Every step used is proved in the two
files. No earlier verdict on any submission is a premise.

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N), and let aT = 27/20, aQ = 59/50 and sig = 13/20.
The single algorithm F-SPQ65Q118 below receives N in binary and fresh independent copies of rho_s, and outputs the entire s
with unconditional probability at least 1 - 2^-7 > 2/3. On EVERY execution branch (every failure, discard and abort
included) it satisfies jointly

    T = O(2^(aT sqrt n)),  S_C = O(2^(aT sqrt n)),  S_Q = O(2^(sig sqrt n)),  Q = O(2^(aQ sqrt n)).

All constants are absolute. Each of the four envelopes has growth index exactly 1/2 (Section 15). The fifth claim is the
clean-input tolerance 0 (Section 16). The sharper main-branch bounds, from which these follow, are in Section 14, with
eT = 269/200 = 1.345 < aT and eP = 11751/10000 = 1.1751 < aQ, eP < aT:

    T = O(n^(13/2) 2^(eP sqrt n) + n^(9/2) 2^(eT sqrt n)),  S_C = O(n 2^(eT sqrt n)),
    S_Q <= 4 r 2^cb + O(n) with 2^cb <= n^-40 2^(sig sqrt n),  Q <= Qcap = O(n^(7/2) 2^(eP sqrt n)).

The S_Q bound carries no polynomial factor: the chunked pool holds at most 4 r 2^cb qubits and everything else quantum
is O(n). The envelope coefficients are fixed exact rationals; no hidden constant sits inside an exponent.

Notation:
- dn = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with
  s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known nonnegative integer. log means log2 unless stated otherwise.

Main-branch parameters, computed by exact integer arithmetic for n >= 2^40:

    r = ceil(sqrt n),  r0 = floor(sqrt n),  Lg = ceil(log2 n),  kappa = ceil(log2 r) + 4,
    ell = ceil(27 r/50),  H = ceil(127 r/200),  dl = ceil(71 r/100),  cb = floor(13 r0/20) - 40 Lg.

So there are ell FW LEVELS, each run on CHUNKS of at most 2^cb qubits (Section 7.3); a binary linear-merge collimation
tree of height H whose leaf tables are built from dl qubits; and no cap on the classical tables of the tree. The size
facts (F1)-(F6) of Section 8 give ell >= 2, H >= 600000, dl >= kappa + 2, 2^kappa >= 16 r, C_ell <= 2^cb and Y <= 2r.

## 1. Provenance and what is new

Base row. F-SPQ65Q118 is our F-SPQ (public submission df8c9f96-55b1-4f68-9b26-1c2138975679) at another point of its
schedule: sig = 13/20, ell = ceil(27r/50), H = ceil(127r/200), dl = ceil(71r/100), declared exponents
aT = 27/20 (T, S_C) and aQ = 59/50 (Q); F-SPQ has sig = 7/10, ell = ceil(11r/20), H = ceil(129r/200), dl = ceil(13r/20),
aT = 13/10 and aQ = 6/5. The construction, every algorithmic step and every lemma are F-SPQ's, and so is every reused
section of IFC-LIMIT's text. Only the point parameters and the facts derived from them change: Section 0, the model
numbers of Section 1, (8.5), (F1)-(F6) and Lemma 8.1 in Section 8, the exponents of Sections 14 and 15, and Section 17.
One sentence is added to the proof of Lemma 10.1: the supplier's acceptance decisions read only whether k < 2^(B+1).
No step relies on F-SPQ's verdict.

Base text. F-SPQ65Q118 is our IFC-LIMIT with its four-input merges removed and a new schedule. IFC-LIMIT is the reference
algorithm of our IFC-BANK; it is F-LIMIT (the reference algorithm of our F-LIMIT-BANK) with a capped chunked pool and
implicit-fiber four-input merges above the cap. F-LIMIT is qzv's HPC-127 with its pairing stage replaced by the
instrument FW on w = 2^28 equal-key qubits. Concretely:
- virtual.md Sections 2-6.2, 7, 7.1, 7.2, 11, 12, 13 and 16 are IFC-LIMIT's text unchanged, except that the algorithm
  name in Section 5 is F-SPQ65Q118. These are F-LIMIT's sections (HPC-127's framework: model, source identities and the
  latent-label model, the rational trigonometric table, label extraction LE, phase vectors and the linear merge MERGE
  with its distribution-free failure Lemma 6.1, the instrument FW with Lemma 7.1, Lemma K and the yield Lemma 7.2, the
  free-frequency decoder, the 2-adic endgame, the success sum) with IFC-LIMIT's on-demand supplier in Section 11.
- Section 7.3 (the chunked pool, REQUEST and Lemma 7.3) is IFC-LIMIT's text unchanged, except that "P" (IFC-LIMIT's
  name in the file that held it) reads "the algorithm".
- Section 9 is IFC-LIMIT's text with the four-input (Phase I) levels deleted, so the tree is binary; Lemma 9.1 then needs
  only Lemma 6.1. Section 10 is IFC-LIMIT's text with the mentions of the four-input merge deleted.
- New: Sections 0, 1, 8 (parameters, size facts, capacity Lemma 8.1, bit allocation), 14, 15 and 17.
In IFC-LIMIT the tree's stored tables were capped at 2^Lam rows to keep classical memory at the pool's level, which
needed the four-input merges above the cap. F-SPQ65Q118 does not cap classical memory: its tables grow to 2^(dl+H-1) rows and
are counted in S_C, which here equals T in exponent. Only S_Q is capped, by the pool cap cb.

Why this helps (motivation only; the theorem rests on the explicit schedule of Section 8). In units of r, a pool level
whose chunks have size 2^x removes about x label bits, a tree level with input tables of 2^y rows removes about y bits,
and with plain classical storage the tree's tables are classical bits while the quantum state of a phase vector of 2^y
rows is y qubits. With chunks capped at 2^s, ell levels below a tree of height H with leaves of dl qubits, the capacity is
about the integral over the levels of min(s, H + ell - i) plus H dl + H^2/2, Q is about 2^(ell + H) (the FW stage costs
log2 RHO, just above 1, per level) and T about 2^(H + dl). 
At s = 13/20 and Q exponent 11751/10000 the best tree exponent of this model (with H <= s, as C_ell <= 2^cb
requires, and H <= dl) is about 1.338; the schedule below uses ell = 0.54 r, H = 0.635 r, dl = 0.71 r, with
capacity coefficient 20067/20000 and tree exponent 1.345.

Lineage. The trade made here, a capped streaming pool with fewer pool levels below a deeper collimation tree, trading
S_Q and Q against T, is qzv's idea: SPC-127 (0efb267b-c55e-49cb-946b-ea3ced57f221) streams a recycling pool through
capped per-key slot tables, and its SPQ rows (among them SPQ-1413, 36f7ed78-f45d-4ba5-adb3-7b09997f0138, and SPQ-1371,
2069d8a3-4aea-4fb4-99c4-de02e8c9df1f) take fewer pairing levels under a sample budget; SPQ-134, SPQ-139 and SPQ-143
(1201acdd-7646-43e1-b9f5-a9199f3210ea, cc47881a-0e4d-4be3-95d5-a3c058f40f20, 371c911c-27e3-418a-b48e-4973b20d1207) made
the fewer-levels trade for SPC-127 without the cap. No text of those submissions is used. mpjunior92's SPCM1-TAGBANK
(0118d724-3ac4-46a7-bf5b-a63539927aa0) and SPCC90-TAGBANK (f9efd397-8230-4424-9098-2a31d11846c8) are prior board work on
capped streaming pools. Our FLQ110 (87dfc97f-0a57-45d1-8d66-78c23b73518d) made the fewer-levels trade for F-LIMIT with an
uncapped pool, and our G4Q110 (732d6354-097d-4cf9-8e3e-de0f86a54bde) before it for G4-124; the layout of Sections 8, 14
and 15 (two exponents, an analytic capacity lemma) follows FLQ110. The texts used are those of our F-LIMIT-BANK
(a9a7dcac-3918-44e8-84db-bda6b1dcebdd) and IFC-BANK (21a0ca76-5817-4d20-845a-261b2ad481b3); IFC-LIMIT's and F-LIMIT's own
provenance (HPC-127 2aad498c-d5e9-4f64-a222-3b2f7f961738 and the CS1 framework f1481815-9577-4990-abe3-7b79fa5d9284 of
AdamGagol; the cell family of mpjunior92's PART rows; Kuperberg, SIAM J. Comput. 35(1), 2005, and arXiv:1112.3333 for
pairing and collimation) applies to the sections reused. These citations are context; every step used is proved in the
two files, and no earlier verdict is a premise.

New here: the composition (FW instrument, chunked capped pool, binary tree with uncapped classical tables), the schedule
of Section 8 with its capacity Lemma 8.1 for a pool whose lower levels are capped and whose upper levels are not, and
the resource ledger of Section 14 in which the pool cap alone sets S_Q.

Historical first-person text in virtual.md denotes the authors of IFC-LIMIT and of the works it credits.

### 7.3 The chunked pool

Sizes (Section 8): D_ell = C_ell and D_i = min(2^cb, ceil(16385 ell D_(i+1)/(8192 (ell - 1)))) for i = ell-1, ..., 0;
YIELDS Yd_i = ceil((ell - 1) D_i/(RHO ell)); RUN CAPS Rc_ell = 1 and Rc_i = floor(Rc_(i+1) D_(i+1)/Yd_i) + 1. Put
rho = RHO ell/(ell - 1) = 16385 ell/(8192 (ell - 1)), so D_i <= ceil(rho D_(i+1)) and D_i/Yd_i <= rho.

Each level i < ell keeps a BUFFER Bf_i, a list of labeled qubits, initially empty, and a counter of its runs.
REQUEST(i+1), for 0 <= i < ell, returns exactly D_(i+1) qubits:
- while |Bf_i| < D_(i+1): if level i has already run Rc_i times, ABORT; obtain an input chunk of D_i qubits, from the
  supplier if i = 0 (leaf qubits, Section 11) and by REQUEST(i) otherwise; run FWLEVEL on it with Cin = D_i,
  p = pp_i, c = pb_i and q(Y+1) rounds; if its OUTPUT has fewer than Yd_i qubits, ABORT; otherwise append OUTPUT,
  in order of production, to Bf_i;
- remove the first D_(i+1) qubits of Bf_i and return them, in order.
The FINAL POOL is REQUEST(ell), so C_ell qubits. Then every qubit left in a buffer is measured, reset and released.

Lemma 7.3 (chunked pool). (a) Every run at level i has exactly D_i inputs, all collimated to pp_i, and satisfies the
hypotheses of Lemma 7.2; every returned qubit of REQUEST(i+1) is collimated to pp_(i+1).
(b) If no run yields fewer than its Yd_i, the run-cap ABORT does not occur: level i runs at most Rc_i times.
(c) At all times |Bf_i| < D_(i+1) + D_i/2, and the algorithm holds at most 3(ell + 1) 2^cb pool qubits.
(d) At most C_0 := Rc_0 D_0 leaf qubits are requested from the supplier, N_i := Rc_i D_i <= C_0 for every i, and
C_0 <= (ell + 1) rho^ell (C_ell + 1) <= 8 (ell + 1) RHO^ell C_ell.
(e) Conditional on everything before it, a run at level i ABORTs with probability at most
w D_i 2^(-3r) + 2 exp(-C_ell/(10 ell^2 w^2)). So the batch's pool stage ABORTs (other than by the supplier) with
probability at most (ell + 1) C_0 (w 2^(-3r) + 2 exp(-C_ell/(10 ell^2 w^2))).

Proof. (a) A chunk of level 0 is leaf qubits, collimated to pp_0 = 0; a chunk of level i >= 1 is OUTPUT of level
i - 1 runs, collimated to pp_(i-1) + pb_(i-1) = pp_i (Section 7.2). E_i = 2^(pb_i) <= D_i/(4 w ell) by the definition of
pbmax_i, and (1 - 2/w)^(q(Y+1)) D_i < 2^(-(Y+1)) D_i < 1 as D_i <= D_0 <= C_0 <= 2^Y (D_i >= D_(i+1) whenever
D_(i+1) <= 2^cb, and C_ell <= 2^cb by (F4)). ell >= 2.
(b) Induct downward. Level ell is requested once (Rc_ell = 1). Suppose level i + 1 runs (or, for i + 1 = ell, is requested)
at most Rc_(i+1) times, so level i receives at most R' <= Rc_(i+1) requests of D_(i+1). If level i runs R times, then
when its last run starts, the requests completed before the current one removed at most (R' - 1) D_(i+1) qubits, the
R - 1 earlier runs appended at least (R - 1) Yd_i, and the buffer held fewer than D_(i+1). So (R - 1) Yd_i < R' D_(i+1),
R <= floor(R' D_(i+1)/Yd_i) + 1 <= Rc_i.
(c) A run appends at most D_i/2 qubits (Section 7.2: |OUTPUT| <= Cin/2) and starts only while |Bf_i| < D_(i+1). At
any time each level holds its buffer and at most one chunk in process (its LIVE and OUTPUT lists, at most D_i
qubits), and the final pool has C_ell <= 2^cb qubits; with D_i <= 2^cb the total is below
sum_i (D_(i+1) + D_i/2 + D_i) + C_ell <= 3 (ell + 1) 2^cb.
(d) The supplier serves at most Rc_0 chunks of D_0. N_(i-1) = (floor(N_i/Yd_(i-1)) + 1) D_(i-1) >= N_i D_(i-1)/Yd_(i-1) >= N_i,
so N_i <= N_0 = C_0; and N_(i-1) <= rho N_i + D_(i-1), with N_ell = C_ell. From D_i <= rho D_(i+1) + 1 and rho >= 2,
D_i + 1 <= rho (D_(i+1) + 1), so D_i <= rho^(ell-i) (C_ell + 1). Hence
C_0 <= rho^ell C_ell + sum_(i<ell) rho^i D_i <= (ell + 1) rho^ell (C_ell + 1), and rho^ell <= 4 RHO^ell
((1 - 1/ell)^(-ell) <= 4) and C_ell + 1 <= 2 C_ell.
(e) Lemma 7.2 with Cin = D_i holds conditional on everything before the run, for ANY labels; its yield event is
S < (ell - 1) D_i/(RHO ell), and S is an integer, so S < Yd_i is the same event. D_i >= C_ell, since D_i >= min(2^cb, 2 D_(i+1)).
Number the runs of level i in order; the k-th, if it occurs, aborts with conditional probability at most the stated
bound, and there are at most Rc_i runs before the first abort by (b). Summing over k <= Rc_i and i, with
sum_i Rc_i <= sum_i N_i <= (ell + 1) C_0, gives the batch bound. QED.

Fixed input sizes are the point of (e): each run's input count D_i is fixed by the schedule, not by the outcomes of the
level, so Lemma 7.2 applies verbatim to every run. The demand pattern (which runs occur, and when) depends on earlier
outcomes; the bound conditions on all of it.

## 8. The schedule

Constants. RHO = 16385/8192 = 2 + 2^-13 (Lemma K). K is as in (11.0), C_ell = 2^12 n K 2^H dl, the sizes D_i, Yd_i and
Rc_i are those of Section 7.3, C_0 = Rc_0 D_0, and Y is the least integer with 2^Y >= C_0. Each FWLEVEL uses
rounds = q (Y + 1), q = 2^27; since 1 - 2/w < exp(-2/w), (1 - 2/w)^q < 1/e < 1/2.

Bracket for log2 RHO. Since RHO > 2, log2 RHO > 1. Since ln 2 = sum_(k>=1) 1/(k 2^k) and all its terms are positive,
ln 2 > sum_(k=1)^8 1/(k 2^k) = 148969/215040 > 6927/10000. Since ln(1 + x) < x for x > 0,
log2 RHO = 1 + ln(1 + 2^-14)/ln 2 < 1 + 2^-14 * 10000/6927 =: HI. So

    1 < log2 RHO < HI,   and   HI (27/50) + 127/200 < eP = 11751/10000,                       (8.5)

the last because 27/50 + 127/200 = 11750/10000 and HI (27/50) - 27/50 = 270000/(50 * 6927 * 16384) < 1/10000.

Size facts (F1)-(F6), for r >= 2^20 (n >= 2^40). Each linear inequality c r >= c' log2 r + c'' below holds at r = 2^20 and
then for all larger r, because c > c'/(r ln 2) there.
(F1) n <= r^2, Lg <= 2 log2 r + 1, kappa <= log2 r + 5, 2^kappa >= 16 r, r0 >= r - 1, and
     13r/20 - 80 log2 r - 42 <= cb <= (13/20) sqrt n - 40 log2 n. (cb >= 13(r - 1)/20 - 1 - 40 (2 log2 r + 1).)
(F2) 27r/50 <= ell <= 27r/50 + 1, 127r/200 <= H <= 127r/200 + 1 and 71r/100 <= dl <= 71r/100 + 1; so ell >= 2,
     H >= 665845 >= 600000, H <= dl, H + 1 <= r and 3 (ell + 1) <= 4r.
(F3) g := ceil(log2 (4 w ell)) <= log2 r + 31, since 4 w = 2^30 and ell <= r.
(F4) C_ell <= 3 * 2^25 r^4 2^H (K <= 3 * 2^13 r as Lg + 30 <= r, dl <= r, n <= r^2), so
     log2 C_ell <= H + 4 log2 r + 27 <= 127r/200 + 4 log2 r + 28 <= cb, because (3/200) r >= 84 log2 r + 70; so
     C_ell <= 2^cb. Also C_ell >= 2^H, so cb >= H, and cb - H <= 13r/20 - 127r/200 = 3r/200 <= ell.
(F5) dl >= kappa + 2.
(F6) By Lemma 7.3(d), (8.5) and (F4), log2 C_0 <= log2 (8 (ell + 1)) + HI ell + log2 C_ell
     <= (HI (27/50) + 127/200) r + 5 log2 r + 33 <= eP r + 5 log2 r + 33 <= 2r - 1. So Y <= 2r <= n (as r <= sqrt n + 1
     and n >= 2^40), 2^Y <= 2 C_0, Y + 1 <= 2r + 1 <= 8 ell, and 2^H <= C_ell <= C_0 <= 2^(2r-1).

Level capacities.
- FW level i (0 <= i < ell): pbmax_i is the largest integer b with 2^b * 4 w ell <= D_i.
- Tree, binary, levels 0 <= i <= H-1: input exponent lam_i = dl + i, output exponent lam_(i+1), with lam_H = 1 (level
  H - 1 is the ROOT); capacity tbmax_i = dl + i - kappa - 1 for i <= H - 2 and tbmax_(H-1) = 2 (dl + H - 1) - kappa - 1.

For every b_i <= tbmax_i, in all cases (substitute)

    b_i + lam_(i+1) - 2 lam_i <= -kappa.                                            (8.4)

Put CP = sum_(i<ell) pbmax_i and CT = sum_(i<H) tbmax_i.

Lemma 8.1 (capacity). For n >= 2^40: CP + CT >= r^2 >= n.

Proof. Pool. D_ell = C_ell >= 2^H, C_ell <= 2^cb (F4), and D_i = min(2^cb, ceil(rho D_(i+1))) >= min(2^cb, 2 D_(i+1)), so by
downward induction D_i >= 2^(min(cb, H + ell - i)). Since 2^g >= 4 w ell, the integer min(cb, H + ell - i) - g (which is
nonnegative by (F3), (F4)) is admissible in the definition of pbmax_i, so pbmax_i >= min(cb, H + ell - i) - g. As
t -> min(cb, H + t) is nondecreasing, sum_(t=1)^ell min(cb, H + t) >= integral_0^ell min(cb, H + t) dt = ell cb - (cb - H)^2/2,
since 0 <= cb - H <= ell (F4). With ell >= 27r/50, cb >= 13r/20 - x where x = 80 log2 r + 42 (F1), and cb - H <= 3r/200 (F4),

    CP >= (27r/50)(13r/20 - x) - (3r/200)^2/2 - ell g.

Tree. Direct expansion gives CT = (H - 1)(dl - kappa - 1) + (H - 1)(H - 2)/2 + 2 dl + 2H - 3 - kappa
= H dl + H^2/2 + dl + H/2 - 1 - H (kappa + 1) >= H dl + H^2/2 - H (kappa + 1). With H >= 127r/200 and dl >= 71r/100,
H dl + H^2/2 >= ((127/200)(71/100) + (127/200)^2/2) r^2.

Sum. The positive terms total at least

    ( (27/50)(13/20) - (3/200)^2/2 + (127/200)(71/100) + (127/200)^2/2 ) r^2 = (20067/20000) r^2 = (1 + 67/20000) r^2

(exact: (28080 - 9 + 36068 + 16129)/80000 = 80268/80000). The subtracted terms are (27r/50) x + ell g + H (kappa + 1).
For r >= 2^20, ell <= 0.5401 r and H <= 0.6351 r (F2), g <= log2 r + 31 (F3) and kappa + 1 <= log2 r + 6 (F1), so they are
at most r (43.2 log2 r + 22.68 + 0.5401 (log2 r + 31) + 0.6351 (log2 r + 6)) <= r (45 log2 r + 44). Hence

    CP + CT >= r^2 + r [ (67/20000) r - 45 log2 r - 44 ],

and the bracket is nonnegative for r >= 2^20: at r = 2^20 it is 3512.7... - 944 > 0, and its derivative 67/20000 exceeds
45/(r ln 2) < 10^-4 there and beyond. Finally r^2 >= n. QED.

Bit allocation. Given an integer B with 1 <= B <= n, allocate exactly B bits greedily: first pb_0, ..., pb_(ell-1) in that
order, pb_i = min(pbmax_i, bits still unallocated), then tb_(H-1), ..., tb_0 likewise with tbmax_i. By Lemma 8.1 this
exhausts B, and every level gets at most its capacity (possibly 0). The tree is always the binary tree of height H.
Positions: pp_0 = 0, pp_(i+1) = pp_i + pb_i; tp_0 = pp_ell, tp_(i+1) = tp_i + tb_i; so tp_H = B. The FW level i runs
FWLEVEL with p = pp_i and c = pb_i (Section 7.3), and tree level i runs MERGE with p = tp_i and b = tb_i (Section 9). Every
bit read below has position below B.

The exact-integer check checks/sched.py of this submission evaluates every quantity above for both extreme n with
ceil(sqrt n) = r, over r from 2^20 to 2^24, and confirms (F1)-(F6), (8.4), (8.5) and Lemma 8.1, both through the lower-bound
chain of the proof and (for r <= 2^22) with the exact chunk sizes D_i. It is a check, not a premise.

## 9. BATCH(supplier, B)

Input: a supplier of LEAF QUBITS: positive qubits with phase exp(2 pi i k th) for a fixed real th and a known label k,
where in the ideal run the labels are independent and uniform on [0, 2^(B+1)), served in chunks of D_0 on request.
Output: K measured-ready roots, or ABORT. A leaf qubit is a labeled qubit with table (0, k).

1. POOL. Form the final pool, C_ell qubits collimated to pp_ell, by REQUEST(ell) (Section 7.3), and release the
   buffers. An ABORT of the supplier or of Section 7.3 is an ABORT of the batch.
2. TREE (bits from Section 8; the binary tree of height H). VEC(0) = LEAF: take the next dl qubits of the final pool (ABORT if fewer
   remain). Their qubits form the index register, bit j = qubit j. With tables (t0_j, t1_j), build lab[0] = sum_j t0_j
   and lab[x + 2^j] = lab[x] + t1_j - t0_j for x < 2^j. The table has length 2^dl, is exactly the tensor product state
   in the ideal run, and is collimated to tp_0 because every difference is 0 mod 2^(tp_0).
   A binary level i (input exponent dl + i) produces its output by: repeat X1, X2 = two outputs of the level below
   (LEAF for i = 0), out = MERGE(X1, X2; p, b_i, lam'), with p its start position, lam' = lam_(i+1) or 1 at the
   binary root, until out != FAIL.
   A root is an output of the root level, evaluated depth-first. Run it K times, or ABORT if the pool runs out.

Root. A root is a two-entry table with lab[0] = lab[1] mod 2^B, so its ideal state is, up to global phase,

    (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2,   W = (lab[1] - lab[0])/2^B, a known integer.     (9.1)

Label bound. Each leaf qubit enters a table entry at most once and all pool qubits are distinct, so every label in
the batch is a sum of at most C_0 leaf labels below 2^(B+1) (Lemma 7.3(d)). Thus every label is below 2^(Y+n+1), which
fits in 3n bits by Y <= n, and

    |W| <= 2 C_0 <= 2^(Y+1).                                                        (9.2)

Lemma 9.1 (no pool exhaustion). In the ideal run, conditional on everything before step 2 except the label bits at
positions >= pp_ell of the leaves of the final pool (so on all FW-stage outcomes and decisions and on the final-pool
tables modulo 2^(pp_ell)), the pool runs out before K roots finish with probability at most 2^-10/n.

Proof. Extend the final pool by phantom qubits, each with a fresh table (0, 2^(pp_ell) u), u independent and uniform
on [0, 2^(B+1-pp_ell)), so that Lemma 6.1 applies throughout (a phantom is a source coordinate whose label
bits at positions >= pp_ell are uniform). By (8.4) and Lemma 6.1 each merge fails with conditional probability
at most 2^-kappa given everything before it. Let A_h
bound the expected number of pool qubits consumed by one output of the level of output height h. Then A_0 = dl and,
by Wald's identity, A_(h+1) <= 2 A_h/(1 - 2^-kappa); Lemma 6.1 applies to each attempt for ANY input tables, so the
conditioning above is harmless. There are H <= r levels and 2^-kappa <= 1/(16r) <= 1/(4r), so the product of the factors
1/(1 - .) is at most (1 - 1/(4r))^(-r) <= 2. So K roots consume at most 2 K 2^H dl qubits in expectation, and Markov
against C_ell = 2^12 n K 2^H dl gives the bound. The phantom run coincides with the real run until exhaustion. QED.

Lemma 9.2 (pool yield). In the ideal run, step 1 aborts other than by the supplier with probability at most
(ell + 1) C_0 (w 2^(-3r) + 2 exp(-2^H/(10 ell^2 w^2))).

Proof. Lemma 7.3(e), with C_ell >= 2^H. QED.

## 10. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and tau_j in {0,1}. Since k_j is uniform on
[0, 2^(B+1)), low_j and tau_j are independent and tau_j is a fair bit. For a batch let G be the sigma-field generated
by: all low_j of its leaves; all FW outcomes (cells and the other values measured in step 4) and all PREP outcomes; all merge outcomes (e, bl); and all decisions
of the controller in that batch (sort orders, groupings into w-tuples, chunk requests and buffer moves, trimming, FAIL
and retries, aborts, assignment of qubits). G does not include
root measurement outcomes, which no decision in the batch reads. It also excludes LE's internal coins and outcomes,
which in the ideal run feed no decision.

Lemma 10.1. In the ideal run, conditional on G and on all independent randomness outside the batch, the top bits tau_j
are i.i.d. fair.

Proof. Induct over the controller's steps. Every key, residue, sort, rank and block partition reads only label bits
strictly below position B, because all positions used are below B (Section 8). The supplier's acceptance decisions
(Section 11) read only whether k < 2^(B+1); given acceptance k is uniform on [0, 2^(B+1)), the law used above. Bits below B of a sum of leaf labels,
and of a difference modulo 2^(p+c) with p+c <= B, depend only on the low_j, since multiples of 2^B do not change them.
PREP outcomes touch only fresh ancillas and depend on no label, and FW outcomes have the law of
Lemma 7.1(a) whatever the labels and the past (it applies at every FW by (P)); returned and recycled
qubits carry explicit tables, sums of leaf labels, so their later keys again read only bits below B. By Lemma 6.1 each merge outcome's conditional law, given
labels and earlier outcomes, is a function of the low_j and earlier outcomes only. So the joint law factorizes as
law(tau) x law(low) x law(outcomes and decisions | low). QED.

Incidence. An entry of a table is the sum over leaves j of x_j k_j, for a 0/1 incidence vector x. Distinct indices of a
table have distinct incidence vectors: this holds for a leaf qubit, table (0, k_j); in FW the index maps
alpha -> (alpha, 1 - alpha) on the pair (A_a, A_b) of a good output and alpha -> (alpha, ..., alpha) on the block
Bl of a recycled output are injective on disjoint coordinates, and a returned qubit keeps its table; a LEAF table
concatenates disjoint coordinates; and a merge re-indexes injectively pairs on disjoint coordinates. So the two root entries have x0 != x1, and with hd = |x0 xor x1| >= 1,

    W = cst + sum_(j in Sp) tau_j - sum_(j in Sm) tau_j,                            (10.1)

where cst = (sum_j low_j (x1_j - x0_j))/2^B is a G-measurable integer, and Sp, Sm are disjoint G-measurable sets with
|Sp| + |Sm| = hd. Each leaf enters at most one root, so given G the W's of distinct roots of a batch are independent.
Since E exp(2 pi i phi tau) = e^(i pi phi) cos(pi phi) for a fair bit, for every real phi

    | E[ exp(2 pi i phi W) | G ] | = |cos(pi phi)|^hd <= |cos(pi phi)|,             (10.2)

and, with phi = 1/2, Pr[W odd | G] = 1/2.                                           (10.3)

## 14. Resources on every main-branch execution

Throughout, K = O(sqrt n); dl, ell, H = O(sqrt n); C_ell = O(n^2 2^H) by (F4); and, writing PP = RHO^ell 2^H,
C_0 <= 8 (ell + 1) RHO^ell C_ell = O(n^(5/2) PP) by Lemma 7.3(d). All fixed loops, caps and aborts below hold on every
branch.

Q. Q <= Qcap = 4 n C_0 + K = O(n^(7/2) PP) (Section 13).

S_Q. By Lemma 7.3(c) the pool, buffers and final pool hold at most 3 (ell + 1) 2^cb <= 4 r 2^cb qubits at any time (F2);
the buffers are released before the tree starts, and the tree's leaves are final-pool qubits. An FW adds at most c_F
ancillas, an absolute constant, all released in |0> (Lemma 7.1(c)), and PREP uses O(1) fresh qubits per try, reset after
it. A phase vector of length 2^lam is a lam-qubit index register (its table is classical), and lam <= dl + H - 1 <= 2r. The
depth-first evaluation holds at most three phase vectors per tree level (a finished output waiting for its sibling and
the two inputs of the merge in progress), so at most 3 (H + 1) 2r <= 6 r^2 <= 24 n qubits. A merge adds O(sqrt n)
qubits (its residue, sum and rank registers). LE and the transforms use O(n), reset between uses. So

    S_Q <= 4 r 2^cb + O(n) <= 4 r n^-40 2^((13/20) sqrt n) + O(n) = O(2^((13/20) sqrt n)),

using 2^cb <= n^-40 2^((13/20) sqrt n) (F1) and 4 r <= 8 sqrt n <= n^40.

S_C. Each pool level stores its buffer, chunk, LIVE and OUTPUT lists and sort scratch, each at most 2^(cb+1) rows of O(n)
bits (Lemma 7.3(c)), and the final pool list has C_ell <= 2^cb rows: O(n r 2^cb) bits over the ell + 1 levels. The tree
stores at most three tables per level, each of 2^(lam_i) fields of 3n bits, plus MERGE scratch of O((L + L') n) bits for
the merge in progress (Section 6.2). Since lam_i <= dl + H - 1 and these geometric sizes sum, this is O(n 2^(dl+H)). The
decoder stores K triples and K residues of O(n) bits, and LE O(n) bits. So S_C = O(n r 2^cb + n 2^(H+dl)) = O(n 2^(H+dl)),
as cb <= H + dl. These are fixed allocations.

Core steps, per batch.
- Acquisitions: at most 4 C_0, each O(n^(5/2)) with LE (log2 Qcap = O(sqrt n) by (F6)): O(n^(5/2) C_0).
- FW stage: a run at level i costs O((D_i + rounds E_i) n log D_i) (Section 7.1, Cost) with E_i = 2^(pb_i) <= D_i/(4 w ell),
  so rounds E_i <= q (Y + 1) D_i/(4 w ell) = (Y + 1) D_i/(8 ell) <= D_i by (F6), and log D_i <= cb = O(sqrt n): a run costs
  O(n^(3/2) D_i). Level i runs at most Rc_i times, so the stage costs O(n^(3/2) sum_i N_i) = O(n^2 C_0), since
  N_i <= C_0 (Lemma 7.3(d)) and ell + 1 = O(sqrt n). Request bookkeeping and buffer moves cost O(n) per qubit moved,
  within the same bound.
- Tree: at most C_ell/dl LEAF calls at O(n 2^dl) each. An attempt at level i consumes 2^(i+1) dl pool qubits that no
  other attempt at that level uses (inputs of a failed attempt are discarded), so there are at most C_ell/(2^(i+1) dl)
  attempts, each O(n 2^(dl+i)) by Section 6.2. Each level thus costs O(n C_ell 2^dl/dl), and all H + 1 levels cost
  O(H n C_ell 2^dl/dl) = O(n C_ell 2^dl) = O(n^3 2^(H+dl)), as H <= dl (F2).
- Decoder per stage: at most 2^(Y+8) candidates, K residues each, O(n) bits per addition: O(K n 2^Y) = O(n^(3/2) C_0).

Over at most n batches, plus poly(n) setup (parameters, CRT, Mult constants, the table of Section 4, shift values, initial
residues), core steps total O(n^(7/2) C_0 + n^4 2^(H+dl)) + poly(n). Every loop is either fixed-length or consumes pool
qubits or acquisitions, so every branch terminates.

T. By (F6) and the space bounds, log2(S_C + S_Q + 2) = O(sqrt n). By (2.1),

    T = O(n^4 C_0 + n^(9/2) 2^(H+dl) + n Q) = O(n^(13/2) PP + n^(9/2) 2^(H+dl)).

Exponents. Since RHO^ell <= 2^(HI ell), r <= sqrt n + 1 and (8.5), with eP = 11751/10000 and eT = 269/200,

    log2 PP <= HI (27 r/50 + 1) + 127 r/200 + 1 <= eP r + 3 <= eP sqrt n + 5,
    H + dl <= (127/200 + 71/100) r + 2 = eT r + 2 <= eT sqrt n + 4.

So jointly, on every branch of the main branch,

    T = O(n^(13/2) 2^(eP sqrt n) + n^(9/2) 2^(eT sqrt n)),  S_C = O(n 2^(eT sqrt n)),
    S_Q = O(2^((13/20) sqrt n)),  Q = O(n^(7/2) 2^(eP sqrt n)).

## 15. Exact growth indices and declared envelopes

Since 27/20 - 269/200 = 1/200, 27/20 - 11751/10000 = 1749/10000, 59/50 - 11751/10000 = 49/10000, and n^(13/2) 2^(-(1/200) sqrt n),
n^(13/2) 2^(-(1749/10000) sqrt n) and n^(7/2) 2^(-(49/10000) sqrt n) are bounded over n >= 1, the bounds of Section 14 give
T, S_C = O(2^((27/20) sqrt n)) and Q = O(2^((59/50) sqrt n)); S_Q = O(2^((13/20) sqrt n)) directly. The finite branch
contributes only an absolute constant. The declared envelopes are B_T(n) = B_C(n) = 2^((27/20) sqrt n),
B_Q(n) = 2^((13/20) sqrt n) and B_samples(n) = 2^((59/50) sqrt n). For B(n) = 2^(a sqrt n) with a in {27/20, 13/20, 59/50},
log2 B = a sqrt n, log2 log2 B = (1/2) log2 n + log2 a, and g(B) = lim log2 log2 max(4, B(n)) / log2 n = 1/2 exactly. The
index holds for these fixed exact coefficients; it does not rely on a guessed constant. The structured objects in
submission.json are exactly these envelopes.

## 17. Scope and limitations

- This does not reach the research goal 2^(O(n^(1/3))); the time growth index is 1/2. The result is a trade-off point:
  S_Q at 13/20, Q at 59/50, and T and S_C at 27/20, in the coefficient of sqrt n.
- S_C is exponential and equal to T in exponent: the tree's classical tables are not capped. No claim is made about
  classical memory below T.
- The group size w = 2^28, the trim 40 Lg, the threshold n >= 2^40 and all constants (the gate count c_F of FW in
  particular) are unoptimized absolute constants, and the ratios 27/50, 127/200, 71/100 are short rationals, not tuned to the limit of the
  model (whose optimum at these S_Q and Q exponents is near 1.338).
