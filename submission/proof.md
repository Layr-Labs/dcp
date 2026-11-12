# IFC-BANK-D: seven-input dissection merges above saturated implicit-fiber four-input merges and a capped recycling pool with streamed leaves, with O(n) classical workspace through a counted basis bank

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N), e = 1449/1000 and sig = 459/800. The single physical
algorithm IFC-BANK-D below receives N in binary and fresh independent copies of rho_s, and outputs the entire s with
unconditional probability at least 1 - 2^-8. On EVERY execution branch (wrong extracted labels, FW-stage (PREP
included, final requests included), supplier and pool aborts, failed and retried merges, four-input and seven-input merges, discarded copies, tag
renumbering, initialization and final cleanup included) it satisfies jointly

    T = O(n^127 2^(e sqrt n)),   S_C = O(n),   S_Q = O(2^(sig sqrt n)),   Q = O(n^(7/2) 2^(e sqrt n)).

The S_Q bound has no polynomial factor: every cap of P is trimmed by 40 ceil(log2 n) bits (P Section 0), which
absorbs the bank's polynomial overhead (Section 8). All constants are absolute. The growth indices are 1/2, 0, 1/2
and 1/2 (Section 11). The fifth claim is the clean-input tolerance 0 (Section 12).

IFC-BANK-D executes a fixed reference algorithm P without changing any of its quantum operations, measurements,
source requests or classical decisions. P is IFC-LIMIT-D, whose complete specification and proof are given after the
marker line of virtual.md, in virtual2.md (P Sections 7.3, 8, 9, A and B) and in virtual3.md (P Sections C and D). "P Section x" and "P (x.y)" refer to that
text; "Section x" refers to this file. The resource statements inside virtual.md concern P in its own storage model,
in which classical records are ordinary bits; they are not claims of this file. IFC-BANK-D changes only where data live:
- every classical record of P, except constant many O(n)-bit staged words, is kept in basis-state qubits, which are
  counted in S_Q and are read and written only at classically known addresses (Sections 3-6);
- P's qubits live in a fixed counted array of quantum slots, managed by an indexed free list (Section 4).

Notation for P: r, r0, Lg, ell, dl, H, a, JI, J7, Lam, cb, kappa, K, C_ell, D_i, Yd_i, Rc_i, C_0, Y and Qcap are as in P
Sections 0, 7.3, 8, 11 and 13; w = 2^28, q = 2^27, RHO = 16385/8192, HI and c_F are as in P Sections 7 and 8; and
PP = RHO^ell 2^H (P Section 14). A "P step" is a core step in the sense of P Section 2, C_P is the number of P steps on
a branch, and T_P is P's charged time (P (2.1)), so C_P <= T_P. All logarithms are base 2. Constants c, c0, c1 are
absolute.

Base row and what changes. IFC-BANK-D is IFC-BANK-F (kshitij-hash's public submission
f7b12b14-f990-4ff5-b513-63e55e39344c; this archive starts from the text of kaankolcu's re-tuned snapshot
04f7e018-7297-49c6-b704-5c774a8b8ebe of it) with its reference algorithm P changed from IFC-LIMIT-F to IFC-LIMIT-D, so
that the construction runs at the cap ratio sig = 459/800, where IFC-LIMIT-F's schedule is infeasible. The physical
construction of Sections 3-9 here is unchanged and is applied to the new P without change, except that the counts
of (P3)-(P5) and of Section 4 now include the seven-input merges (seven index registers per tree level, so 28n in
place of 16n, and MERGE7's registers and arrays). The changes to P are
listed at the start of P Section 1 and are:
- a new schedule (P Section 0 and P Section 8 in virtual2.md): ell = Lam pool levels on chunks of exactly 2^cb qubits,
  one binary tree level (a = 1, dl = Lam - 1), four-input fibers l_j = min(Lam + 1 + 2j, 2 Lam), so that the four-input
  levels j >= ceil((Lam - 1)/2) are saturated (r_j = 0), followed by J7 = ceil(149 r/2000) seven-input levels (below), and
  e = 1449/1000; Lemma 8.1 is
  reproved for this shape and the size facts (F1)-(F6) are rederived;
- a streamed leaf supply (P Sections 7.3 and 9): as 2^H > 2^cb the tree takes its leaves from a leaf buffer refilled
  by final requests of 2^cb qubits, at most Rc_ell per batch, instead of one final pool of C_ell qubits; Lemma 7.3,
  Lemma 9.1 and Lemma 9.2 are restated for it;
- the explicit statement of MERGE4I's case r = 0 (P Section A, Lemma B.1 Stage 1);
- fibered seven-input dissection merges (P Sections C and D of virtual3.md, new): the four-input levels stop at
  JI = ceil((29/50) Lam) and are followed by J7 Phase M levels of MERGE7, level k with fiber width
  w_k = max(0, 3 Lam - 2 JI - floor(14 (k+1)/5)), each collimating 6 Lam - kappa - w_k bits from seven inputs of 2^Lam
  entries (7 Lam - 1 - kappa - w_k at the root), with failure bound 2^(2 - kappa) (P Lemma D.1); 2^H = 2^(a + 2 JI) 7^J7.
The first three changes make IFC-BANK-S (e-man07, 3b49ab04-1ede-4baf-9802-79c3dfa95b06 and its siblings at other cap
ratios); the fourth is new in IFC-BANK-D.
Here those facts of P that this file uses are unchanged in form: at most 4 r 2^cb pool qubits at once, every array of
P at most 2^(cb+1) rows, C_0 <= 8 (ell + 1) RHO^ell C_ell, C_ell <= 3 * 2^25 r^4 2^H, Y <= 2r, log PP <= e r + 3 and
H + dl <= e r + 2. Only (P3) and (P5) of this file mentioned the final pool; they now name the leaf buffer. In the text below "we" and "our" refer to kshitij-hash, the authors of IFC-BANK-F; the changes above are
e-man07's. No step relies on any verdict.

Where this sits. With S_C = O(n), the four-input saturated schedule of IFC-BANK-S gives
T = 2^((2/(3 sig) + sig/2 + o(1)) sqrt n) at cap ratio sig; at sig = 459/800 that is 1.4488. The seven-input levels lower
this; for the fiber rule of P Section 8 my continuous model of the schedule (optimized split, exact fiber loss) gives
1.4426 at sig = 459/800, and the proved schedule declares 1449/1000 (P (8.5) and Lemma 8.1, which uses the simpler loss bound
5 Y1^2/28 and the integer rule JI = ceil((29/50) Lam)).

## 1. Provenance: the storage construction is mpjunior92's

The construction of Sections 3-7 and the explicit-degree ledger of Section 9 are mpjunior92's idea, not ours.
mpjunior92 applied them to qzv's HPC-127 (public submission 2aad498c-d5e9-4f64-a222-3b2f7f961738):
- HPC127-TAGBANK (6c0e2efd-41bd-4018-a24e-e386f3069c9b). It introduced the indexed free list and banked descriptors
  for an exponential coherent pool, the per-wire-event charge and the fixed spans (A, R, Wrow, H, B, e, D there; OWN,
  ROWS, WROW, HQ, LSPAN, EW, DRAW here) for HPC-127; it carries the tagged bank, exact renumbering and decoded
  classical-quantum invariant from IFCS1310-TAGBANK.
- HPC127-SHARP (73741b63-bfa1-4d24-b254-ca6fd0549221). The same construction with explicit polynomial degrees
  (n^4 control completion, n^16 wire events, n^100 per charged event, total power 132) in place of a pure envelope.
- Earlier rows by the same author that these build on: PSG21 (9fdfdb12-834d-441c-8bb1-717ab380abf3, a measured
  basis-state bank), LLV-GBANK (dc3ece2a-3068-487a-829f-29d5c9139f89, their first direct-wire bank), LLV-GBANKQ25
  (fbb8f36c-3904-4bf0-9ddf-e9f5d83657ae, direct-wire bank operations, classical forgetting and the complete counted
  prefix) and IFCS1310-TAGBANK (fc8aa038-cba6-42bf-a317-df1c36c956f7, lazy generation tags with exact renumbering).
- GordoAR's PSG2-QSTORE (2b2b0036-7bbc-4ce5-80a8-b8928f0ce120), on which that bank lineage builds: the direct stable
  wire map and the fixed-region maximum-address argument. Our Section 4 wire map and whole-prefix count descend from
  it.

We restate the construction completely, so that this file and virtual.md are self-contained. We keep mpjunior92's
constants so that the two can be compared line by line. Tags and free lists are standard programming techniques. No
earlier verdict on any submission is a premise here.

Ours are:
- the reference algorithm P (IFC-LIMIT-D, specified and proved in full in virtual.md and virtual2.md and not filed on
  its own). It is our F-LIMIT (the reference algorithm of our F-LIMIT-BANK, a9a7dcac-3918-44e8-84db-bda6b1dcebdd) with
  a capped chunked pool (P Section 7.3) and, above the cap, the four-input merge MERGE4I with streamed, unstored pair
  fibers of our IFC1 (1294d17f-2acf-4e10-9996-6b4375388f49), whose lineage is e-man07's CW1 and MW4;
- the check in Section 2 that P supplies every property the construction uses, including MERGE4I's registers and
  arrays and the pool buffers;
- the trimmed caps that make S_Q a pure 2^(sig sqrt n) envelope (Section 8), and the exponents (Sections 8 and 10).

Prior board work on the trade-off. Capping a recycling pool's windows to trade S_Q against T is qzv's (SPC-127
0efb267b-c55e-49cb-946b-ea3ced57f221, SPC-M1 fdacb3e2-9074-4dcc-9389-887574dd25e3, and the SPQ rows that also lower Q);
mpjunior92's SPCM1-TAGBANK (0118d724-3ac4-46a7-bf5b-a63539927aa0) and SPCC90-TAGBANK
(f9efd397-8230-4424-9098-2a31d11846c8) put such a pool inside this storage construction. Capped IFC trees inside this
storage construction are mpjunior92's IFCS rows, IFCS1310-TAGBANK (fc8aa038-cba6-42bf-a317-df1c36c956f7) among them. New
here is the composition: implicit-fiber merges above a capped recycling pool, with the schedule of P Section 8.

Prior board work on the same cell family. mpjunior92's PART7-189-TAGBANK (1e083775-5d0a-4070-bcdc-ded8ada75d3a),
PART31-190-TAGBANK (38897382-d7d7-44fe-8205-64ad028a41a5) and PART127-191-TAGBANK
(d444e283-4dcc-4836-a82b-bc1e6866e25b) use odd-pair cells with an all-equal remainder for odd group sizes, inside
the same banked storage. P is the even-size case at w = 2^28; we derived it independently, and its realization,
proof and schedule are our own.
mpjunior92's later rows PARTADAPT-193-TAGBANK (cfb1e549-2935-4d3f-a8b2-a01b125134ea, status failed in the
pipeline when checked) and PARTROOT196 (3315027c-4ec3-4352-80e5-f8f384e286f1, validating when checked) let the odd
group size grow with n and claim coefficients just above 2/sqrt 3; they are prior board work on the growing-size
case. We claim no priority over any of these rows.

Base text. This file is the text of our F-LIMIT-BANK (a9a7dcac-3918-44e8-84db-bda6b1dcebdd), itself the text of our
TRIAD-BANK (9a129f0f-e377-466d-b45d-449843d2167e) and unfiled G4-BANK with P replaced. Sections 3-7, 9 and 12 differ from it
only in the algorithm's name, the row bound U (Section 3), the register count of (P4) and the recursion depth.
Sections 0, 1, 2, 8, 10, 11 and 13 carry IFC-LIMIT-D's facts, parameters and exponents. No step relies on any of these
rows' verdicts.

## 2. The reference algorithm P and the facts used from it

Finite branch (n < 2^40). P is the exhaustive tester of P Section 13: for cand = 0, ..., N-1 use n+10 fresh copies,
apply Shift_cand, measure the control in X, and reject cand at the first minus; output the first unrejected cand, or
0. IFC-BANK-D runs it with ordinary storage. It holds cand, a copy counter and the current copy, so O(n) bits and
O(n) qubits, and it makes the same acquisitions. There are finitely many such N, so this branch changes only
absolute constants.

Main branch (n >= 2^40). P computes exactly the integers of P Section 0 (r, r0, Lg, kappa, ell, dl, H0, cb, Lam,
a, JI, J7, H) and of P Sections 7.3 and 8 (K, C_ell, D_i, Yd_i, Rc_i, C_0 = Rc_0 D_0, Y, pbmax_i and the tree capacities),
puts Qcap = 4 n C_0 + K, and runs P Sections 5-13: label extraction LE; the chunked FW stage (FWLEVEL runs of q(Y+1)
rounds on chunks of D_i, with buffers and run caps); the tree shape and bit allocation of P Section 8 for each
requested B; BATCH with its tree of binary MERGEs, four-input MERGE4Is and seven-input MERGE7s; the free-frequency decoder; and the 2-adic
part. Every ABORT outputs 0.

Completion of unspecified orders. P leaves three orders open:
- equal-key ties in its merge sorts;
- the order of LIVE after an FWLEVEL round;
- the order of OUTPUT.

IFC-BANK-D fixes them as follows:
- sorts are stable, with ties in current list order;
- after a round, LIVE lists, in scan order, the qubits a group returns to LIVE at the position of that group (for a
  pair cell its w - 2 returned qubits, in group order; for a matching cell or Ev its recycled qubit) and the
  ungrouped qubits at their own positions;
- OUTPUT is in order of production, and buffers are in order of appending, so "the first D_(i+1)" of P Section 7.3
  is defined; MERGE4I's sorts are stable and its streams and heaps break ties by position, as P Section A fixes, and MERGE7's
  sorts are stable and its lists are in the orders P Section C fixes.

These orders are functions of P's classical history only, never of slot numbers or bank addresses. Every lemma of P
that meets these orders holds for any order that is a function of the past:
- P Lemma 7.2 holds "For ANY labels, and conditional on everything before the level", so P Lemma 7.3 holds for
  every run, and the live count
  S_end <= (w - 1)E of P Section 7.2 holds "whatever the labels and outcomes";
- the sigma-field G of P Lemma 10.1 contains all decisions of the controller;
- P Lemmas 6.1, A.1, C.2, 9.2 and 11.1 are conditional on the past, and P Lemmas B.1, D.1 and 9.1 on the controller's history
  (outcomes and decisions; LE's internal records excluded); the orders above read only list positions, keys and
  outcomes, so they lie in that history.

So this completion is an instance of P.

Facts used. Sections 3-10 use only the following properties of P.

(P1) Success. P outputs s with probability at least 1 - 2^-10 on the finite branch and at least 1 - 2^-8 on the main
branch. P Section 13 bounds the main-branch failure probability by the sum of six terms:

    2^-10 (pool exhaustion, P Lemma 9.1) + 2^-40 (pool-stage abort, P Lemma 9.2) + 2^-40 (supplier abort)
    + 2^-20 (decoder, P Lemma 11.1) + 2^-40 (2-adic miss) + 2^-10 (LE coupling, P (5.1))  <  2^-8.

(P2) Word sizes and loops.
- Y <= 2r <= n (P (F6)).
- Every label fits a 3n-bit field (P Sections 6 and 9).
- Every parameter above, every position pp_i and tp_i, and every loop limit has O(n) bits.
- Every loop has a length fixed by the parameters or is cut off by the caps on pool qubits and acquisitions
  (P Section 14). This holds on every branch, so every branch terminates.

(P3) Classical records. On every branch P's classical arrays are the following.
- Per pool level, the buffer Bf_i, the input chunk, and in an FWLEVEL run the lists LIVE and OUTPUT, the
  merge-sort scratch and the measured code of the current cell (w rows of 29 bits); and the leaf-buffer list (P Section 9). Each has
  at most 2^(cb+1) rows: |Bf_i| < D_(i+1) + D_i/2 (P Lemma 7.3(c)), Cin = D_i <= 2^cb, LIVE never grows, and OUTPUT
  has at most Cin/2 rows since each FW appends gamma <= rho/2 good outputs while it removes rho qubits from LIVE
  (P (7.3)); the leaf buffer has at most D_ell = 2^cb rows (P Sections 7.3 and 9).
- In the tree: at most seven retained tables per level, each of at most 2^Lam rows. For the one active MERGE: the
  arrays aa, bb, order, pos, lo, cnt, off, Dx and the block inverse v -> (x_v, y_v), each of at most 2^Lam rows. For
  the one active MERGE4I: the residue and sort-order arrays, runs, the two heaps, Buf, Tl and the block table, each
  of at most max(2^Lam, Cp) <= 2^cb rows (P Section A; Cp <= 2^cb by P Section 8). For the one active MERGE7: the
  three sort orders, T3(g) with its keys, P45(h), P67(h2), Tl and the block table, each of at most
  max(2^(Lam+2), Cp) <= 2^cb rows (P Section C; Cq = 2^(Lam+1) + 1 and Cp <= 2^cb by P Section 8).
- The decoder's K records (Z_i, beta_i, W_i) and K residues (P Section 11).
- LE's 2(J_e + 1) test counters and directions (P Section 5).
- The profiles over i of D_i, Yd_i, Rc_i, run counters, pbmax_i, pb_i, pp_i (ell + 1 rows) and over tree levels of
  their exponents, capacities, bits and positions (a + JI + J7 + 1 rows) (P Section 8), and the 4096-row table of P
  Section 4.
- O(1) scalars per loop level and per frame of the depth-first recursions (the tree, depth a + JI + J7 + 1, and the
  requests of P Section 7.3, depth ell + 1).

Each row of these arrays has at most 12n bits. Lists store a handle to their qubit; P calls it the "wire index", and
here it is a slot number (Section 4).

(P4) Qubits. At any time P holds at most:
- 4 r 2^cb pool qubits (P Lemma 7.3(c) and Section 14);
- 7 (a + JI + J7 + 1) Lam <= 7r^2 <= 28n qubits of stacked index registers (P Section 14; a + JI + J7 + 1 <= r, Lam <= r);
- a fixed set of scratch registers: the current copy (n+1 qubits); the transform, modular-addition and LE scratch of
  P Sections 3 and 5; the merge registers Ru, Rv, Rz, Rp, Rd, R and their Toffoli-chain scratch (P Section 6); the
  MERGE4I registers (the residue, sum and window registers of steps 1 and 3, R and Rf, and their Toffoli-chain
  scratch, fewer than 32 registers of O(sqrt n) qubits, P Section A); the MERGE7 registers (the lookup
  registers, Rz, Rw and Ru of steps 1 and 2, R and Rf, and their Toffoli-chain scratch, fewer than 32 registers of O(sqrt n) qubits,
  P Section C); the FW registers T, R and P, the PREP try
  qubits and the Boolean-evaluation scratch, at most c_F qubits in all, an absolute constant (P Section 7.1); and one
  coin qubit (P Section 11).

These are explicit ripple and Toffoli-chain circuits. Apart from FW's registers, (P4) lists fewer than 1024 registers,
each of at most 4n qubits, so the scratch totals at most c0 n + c_F qubits with c0 <= 2^12 and c_F <= 2^90 <= n^3.

(P5) Lifecycle. Every P qubit is created in one of two ways:
- by an acquisition, as part of an (n+1)-qubit copy;
- by allocation in |0>, as scratch of a transform, a modular addition, an LE test, a LOOKUP, a MERGE, a MERGE4I, a MERGE7, an FW, a PREP
  try or a coin. Each such operation allocates at most c0 n qubits (at most c_F for an FW apart from its PREP tries, and at
  most 29 for a PREP try) and contains at least one P step.

Every P qubit ends by being measured and released, or reset and released, or released in a known basis state. In
four places P leaves the release implicit: the leaf-buffer qubits that a LEAF call leaves over or that remain after
the K roots, and the buffered qubits that remain when the tree ends (P Sections 7.3 and 9; measured, reset and
released), the wd = 1
leaf qubits with kk != 1 (P Section 12), and R after a step-4 FAIL of MERGE (P Section 6.2). IFC-BANK-D completes P
there, and wherever else a release is implicit, by one rule: a qubit that P never touches again is reset and released
at that point (a trace-out, so the result is still an instance of P). In detail:
- LE resets the data register of a copy. A rejected copy is released. An accepted copy's control becomes a pool qubit
  (P Sections 5, 11 and 12).
- An FW on pool qubits A_0, ..., A_(w-1) (P Section 7.1) first runs PREP: each try allocates j_N + 1 <= 29 fresh
  qubits, measures and resets the flag, and on failure measures, resets and releases the try qubits; on success they
  become R_N. It allocates T, P and the Boolean-evaluation scratch in |0>. Steps 1-4 return T, R, P and all scratch
  to |0> on every input (P Lemma 7.1(c)): steps 2-3 compute and uncompute cleanly, step 4 measures and resets P,
  every R_N and, for a matching cell, T, and for Ev returns T to |0> by H. They are then released. Step 5 depends
  on the recorded cell C:
  - for each pair {a, b} of C, a < b: A_b is brought to |1> by a CNOT, then to |0> by NOT, and released; A_a (a
    good output) stays;
  - if C has a block Bl = {c_0 < c_1 < ...} (a matching cell or Ev): after the CNOTs A_(c_0) -> A_(c_i) the qubits
    A_(c_i), i >= 1, are |0> and are released; A_(c_0) (the recycled output) stays;
  - the w - 2 qubits unconstrained by a pair cell stay, unchanged.
  P Lemma 7.1(c) states that step 5 leaves every released qubit in |0> on every input. So an FW, apart from its
  PREP tries, makes at most c_F + 2w wire events, an absolute constant, and each PREP try makes at most 58; an FW
  releases between 1 and w - 1 of its inputs, each in |0>, and keeps the others.
- At the end of an FWLEVEL, LIVE is measured, reset and released. OUTPUT qubits move to the level's buffer by handle,
  and a request moves buffered qubits to the next level by handle (P Sections 7.2 and 7.3).
- LEAF transfers dl pool qubits into an index register and allocates nothing.
- MERGE allocates its registers. It returns x and y to |0> (step 5) and releases them, keeps the low lam' bits of R as
  the output index register, and on FAIL resets and releases both inputs (P Section 6.2).
- MERGE4I allocates its registers; steps 1, 3 and 5 compute and uncompute cleanly and reset every measured register;
  step 7 returns x1, ..., x4 to |0>, which are released, and resets Rf and the high bits of R from known values; the
  low lam' bits of R are the output index register; on FAIL all inputs and registers are reset and released
  (P Section A). Its classical arrays are fixed-size and freed at its end.
- MERGE7 allocates its registers; steps 1, 2 and 4 compute and uncompute cleanly and reset every measured register;
  step 6 returns x1, ..., x7 to |0>, which are released, and resets Rf and the high bits of R from known values; the
  low lam' bits of R are the output index register; on FAIL all inputs and registers are reset and released
  (P Section C). Its classical arrays are fixed-size and freed at its end.
- A root is measured and released, and unused roots are released (P Sections 11 and 12). At an ABORT or at the end
  every remaining qubit is released.

(P6) Cost. On every main branch, P Section 14 and (2.1) give:
- C_P = O(n^(7/2) C_0 + n^4 2^(H+dl)) + poly(n) and T_P = O(n^(13/2) PP + n^(9/2) 2^(H+dl)) = O(n^(13/2) 2^(e sqrt n)),
  with C_P <= T_P;
- Q_P <= Qcap (P Section 13);
- C_0 <= 8 (ell + 1) RHO^ell C_ell (P Lemma 7.3(d)) and C_ell <= 3 * 2^25 r^4 2^H (P (F4));
- log PP <= e r + 4 and H + dl <= e r + 3 (P Section 14, which gives e r + 3 and e r + 2);
- cb <= sig sqrt n - 40 log n and Lam + kappa + 4 = cb (P (F1) and Section 0).

P's own envelopes (P Sections 0 and 14) concern its storage model. This file uses the bounds listed above, which P
proves with explicit polynomial factors.

The pool primitive. The HPC-127 version of this construction differs from the present one only in P's pool primitive
(PAIR there, FW here, G4 in G4-BANK, TRIAD in TRIAD-BANK), in the schedule constants, and here in the chunked pool and the
four-input and seven-input merges, which add only registers, arrays and lifecycles of the kinds listed in (P3)-(P5). The construction uses the
pool primitive
only through (P4) and (P5): a bounded number of wire events per primitive, kept qubits transferred by handle, and
released qubits reset. By P Lemma 7.1(c), which holds for every input state, FW satisfies both. The number of inputs
an FW releases (between 1 and w - 1) is fixed by its recorded cell; the construction uses only the bound w - 1 on it,
since each release is one FREE_Q of a qubit that P releases. Sections 3-10 use P's yield lemmas
(P Lemmas 7.2, 7.3 and 9.2) only through (P1), and P's schedule only through (P2), (P3) and (P6).

## 3. Fixed capacities of the bank

Put U = r 2^(cb+2) and

    OWN = 2^16 n^2 owners,  WROW = 2^16 n^2 bit cells per row,  ROWS = 2^24 n^4 U rows per owner,
    HQ = 2^20 n^2 U quantum slots.

An owner holds one logical array. The logical bit (o, i, j), with o < OWN, i < ROWS and j < WROW, has the address

    c = o ROWS WROW + i WROW + j  <  LSPAN = OWN ROWS WROW = 2^56 n^8 U.               (3.1)

Fit. Every array of (P3) has at most max(2^(cb+1), K, 4096, ell + 1, a + JI + J7 + 1, 2(J_e+1)) <= U <= ROWS rows. The
slot metadata of Section 4 has HQ rows, and HQ <= ROWS because ROWS/HQ = 16 n^2. Every row of P has at most
12n <= WROW bits. A slot number is below HQ < 2^n, so it has at most n bits.

Descriptors of P's qubits (Section 4) have one slot number per row:
- a pool qubit's slot number is a field of its row in the pool list, LIVE or OUTPUT;
- an index register of a phase vector has a descriptor array of at most Lam rows in the same per-level family as
  its table;
- each of P's named scratch registers (P4) has its own descriptor array of at most c0 n + c_F <= U rows.

Fewer than 64 arrays are live per tree level and per FW level. The others are fewer than 64 + 1100: fewer than 64
for the decoder, LE, profiles, table, slot metadata and frame arrays, and fewer than 1100 scratch descriptors (the
registers of (P4), MERGE4I's and MERGE7's included, and of FW). So at most 64(a + JI + J7 + 1) + 64 (ell + 1) + 1164 <= 512(a + JI + J7 + ell + 4)
<= OWN arrays are live at once. Frames of
P's depth-first recursion and its loop counters are rows of fixed frame arrays indexed by depth; they are not
ordinary memory. Owners are reused through FREE_OWNER and ALLOC_OWNER (Section 5). These capacities are fixed before
P starts and do not depend on the branch.

## 4. Physical layout, and the quantum slot allocator

Each epoch has EW = (n+2)^20 tag bits. Every logical bit has one value bit and EW tag bits. The RAW span is

    DRAW = LSPAN (EW + 1) + (OWN + 8) EW + OWN + 2^20 n^4,                                (4.1)

laid out in RAW indices as follows:
- logical bit c < LSPAN: value at RAW index (EW+1)c, and tag bit t < EW at (EW+1)c + 1 + t;
- then OWN + 8 words of EW bits: the epoch ep(o) of each owner o, the global generation G, the backup word of
  Section 6, and six spare words;
- then OWN active flags;
- then 2^20 n^4 RAW scratch bits, which hold the owner bindings (which logical array an owner holds) and the fixed
  RAW state of the interpreter.

These ranges are disjoint and end below DRAW. RAW records carry no tags.

Physical wires:
- RAW index j is wire 2j;
- quantum slot k < HQ is wire 2k + 3;
- wire 1 is spare.

Let h be the least power of two with h >= max(DRAW, HQ + 2). On the main branch IFC-BANK-D first computes the
parameters with O(n) staging (Section 8). It then allocates wires 0, ..., 2h-1 in |0> once, and releases them once at
the very end, after the output is written. In between it allocates only an (n+1)-qubit acquisition register, one at
a time. Hence on every main branch

    S_Q <= 2h + n + 1.                                                                    (4.2)

Bank wires are acted on only by computational-basis measurements and by X gates conditioned on classical bits.

Slot allocator. The bank holds the logical words head and virgin (O(n) bits each), the logical array NEXT of HQ rows,
and the descriptors of Section 3. Every P quantum register is a pool qubit or a register with its own descriptor
array, and its descriptor rows list its slot numbers, one per row. P's lists store slot numbers where P stores wire
indices. head = HQ means empty.
- ALLOC_Q: if head != HQ, put k := head and head := NEXT[k]; otherwise put k := virgin and virgin := virgin + 1.
  Return k.
- FREE_Q(k): reset wire 2k+3 (the reset core step, which records no outcome); then NEXT[k] := head and head := k.

Initially head := HQ and virgin := 0. NEXT[k] is read only after FREE_Q(k) has written it. No operation scans the
slots. Every head, NEXT and virgin access is a known-address word operation.

Invariant (I). The slots below virgin are partitioned into two sets:
- slots holding live P qubits, one slot per qubit, mapped injectively by the descriptors;
- slots on the free stack, which has no repetitions and whose slots are in |0>, in tensor product with everything.

Slots at or above virgin are untouched |0>. ALLOC_Q removes a free or untouched slot from those sets and gives it to
exactly one new P qubit. FREE_Q is called only when P releases that qubit, never when a handle is merely passed or
copied, and it returns the slot to |0>. A P qubit keeps its slot from allocation until release, and passing a
register passes its descriptor, never a copy of its qubits. So (I) is preserved. Gates read their operands' slot
numbers from the descriptors and act on the corresponding odd wires.

The pool is never full. By (P4), with the completion rule of (P5), at most 4 r 2^cb + 28n + c0 n + c_F slots are live
at once. Since c0 <= 2^12 and c_F <= n^3 <= 2^cb (cb >= r/2 by P (F1)),

    live  <=  5 r 2^cb + 2^12 n + 28n  <  HQ,   because HQ = 2^20 n^2 U = 2^22 n^2 r 2^cb.

If virgin = HQ and the free stack were empty, all HQ slots would be live, a contradiction. So ALLOC_Q always
succeeds, and no abort or guard is added.

Wire events. Call every ALLOC_Q, FREE_Q and descriptor-row update a wire event. By (P5):
- allocations number at most (c0 n + c_F) C_P + (n+1) Q_P;
- releases number at most the allocations;
- each allocation or release updates at most c1 descriptor rows;
- moving a qubit between lists costs nothing extra: its slot number is a field of the list row, and P copies that row
  itself, in P steps already counted in C_P;
- only LEAF, MERGE step 6, MERGE4I step 8 and MERGE7 step 7 move slot numbers into descriptor rows, at most c1 rows per moved qubit. LEAF moves dl
  qubits and builds 2^dl table rows, and MERGE step 6, MERGE4I step 8 and MERGE7 step 7 each move lam' qubits and write 2^lam' table rows, so each such
  move is charged to at least 2^dl or 2^lam' table rows, hence to at least one P step per moved qubit.

Hence a branch has at most

    c n (C_P + Qcap)  =  O(n^16 (C_P + Qcap + HQ + 1))                                   (4.3)

wire events. The HQ slots are prepared once and cleared once, and are never scanned for an allocation, a gate, a
root, a request or a batch.

## 5. Bank operations

RAW_READ(j) measures wire 2j in the computational basis into one staged bit. RAW_WRITE(j, v) does RAW_READ(j) into a
staged bit z, applies X to wire 2j if z != v, and forgets z. The address j is always a classically known staged word;
no gate is ever controlled by a superposed address.

Epoch words ep(o), G and the backup are EW-bit RAW words. They are compared, copied and incremented bit-serially, with
one staged carry or equality bit and an O(log n)-bit bit counter. An epoch value is never held as an ordinary word.

- READ(o, i, j): compute c by (3.1), then compare the tag of c with ep(o) bit by bit. Return the stored value if they
  are equal, and 0 otherwise.
- WRITE(o, i, j, v): RAW_WRITE the value bit of c to v, then copy ep(o) into the tag of c bit by bit.
- ALLOC_OWNER: find an inactive owner o by scanning the OWN active flags. If G is all ones, run Section 6 first. Then
  G := G + 1, ep(o) := G, set o's active flag, and record its binding in RAW scratch.
- FREE_OWNER(o): clear o's active flag. No cell is cleared.

Initially every RAW bit is 0, so G = 0 and every tag is 0. Every active owner has an epoch >= 1.

Lemma 5.1 (lazy arrays). At all times every stored tag is at most G, and the epoch of an active owner exceeds every
tag that was stored in its cells before its activation. Consequently READ(o, i, j) returns the value of the last
WRITE to (o, i, j) during o's current activation, and 0 if there was none.

Proof. G does not decrease between renumberings. ALLOC_OWNER sets ep(o) = G + 1, which exceeds all stored tags
because they are at most G by induction. WRITE stores the tag ep(o) <= G. A cell (o, i, j) is written only through
owner o. If it was written during the current activation, its tag is ep(o), since every write in that activation
stores ep(o). Otherwise its tag was stored earlier, so it is 0 or a tag stored before the activation, and in both
cases it is smaller than ep(o). Section 6 preserves every decoded value and re-establishes both invariants. QED.

So the bank realizes zero-initialized arrays with O(1)-cost FREE and ALLOC: an exponential array is never cleared on
each free or retry. Where P only specifies fresh scratch, zero initialization is a valid fixed completion.

Words, loops and LOOKUP.
- An O(n)-bit field of a row is a run of logical bits. Word operations are bit-serial, with a staged carry.
- P's classical computations run as fixed bit-serial code whose operands are READ from and WRITTEN to the bank. These
  are the comparisons, additions, merge sorts and binary searches; table construction; the residue updates of the
  decoder; and parameter arithmetic, with schoolbook multiplication and division. Only constant many O(n)-bit words
  are staged at once.
- P's loop counters, recursion frames and profiles are bank rows. There is no ordinary call stack, no growing
  transcript and no stored circuit; the fixed program generates P's gates online.
- P's LOOKUP (P Section 6.1) remains its serial circuit. For each row x0 and output bit, the program READs that bit
  of tab[x0] and emits the CNOT from the flag if it is 1. A superposed P index is never used as a bank address.

## 6. Exact renumbering when G is full

IFC-BANK-D never assumes that G cannot wrap. If ALLOC_OWNER finds G all ones (a bit-serial test), P is paused, and the
following is done for o = 0, ..., OWN-1.
- If o is active: copy ep(o) into the backup word. For every cell (o, i, j), compute its decoded value against the
  backup, write that value and set the tag to o + 1, padded to EW bits. Finally set ep(o) := o + 1.
- If o is inactive: set all its values, all its tags and ep(o) to 0.

Then G := OWN, and the pending ALLOC_OWNER resumes.

Afterwards:
- every tag is at most OWN = G;
- an active owner's cells carry the tag o + 1 = ep(o) and decode to their previous values (unwritten cells decode to
  0, as before);
- an inactive owner's cells carry the tag 0, below any later epoch.

So the invariants of Lemma 5.1 hold again. Since OWN + 2 < 2^EW, generations remain available, and repeated wraps are
handled in the same way.

During renumbering no P operation, source request or quantum operation occurs, and the old epoch is held only in the
RAW backup. The decoded record and every P qubit are unchanged, so no abort, failure, request or probability change is
introduced. One renumbering costs at most c n^22 DRAW charged steps.

Renumbering is eventually absent. The number of ALLOC_OWNER calls on a branch is at most the number of instructions
counted in (L1)-(L3) of Section 9, outside renumbering. By (P6) and (8.1) that number is at most 2^(c sqrt n). A
renumbering needs at least 2^EW - OWN - 1 generations since the start or since the last renumbering. Also
log(2^(c sqrt n)) = c sqrt n < (n+2)^20 - 1 for n >= c^2. So there is an absolute n1 such that no renumbering occurs
on any branch for n >= n1. For each of the finitely many lengths 2^40 <= n < n1 every branch is finite, because all
loops of P are bounded. So renumbering there changes only an absolute constant.

## 7. Correctness: the decoded classical-quantum invariant

An aligned point is any point between two P steps or acquisitions. Define a map pi from the physical state to P's
logical state at aligned points:
- decode the cells of every active owner through its epoch (Lemma 5.1);
- keep P's control position and bindings;
- map each slot that holds a live P qubit to that qubit, using the descriptors (injective by (I));
- trace out free slots, padding wires, tags, inactive owners, allocator fields and every other physical-only record.

IFC-BANK-D has no randomness of its own. Its staged decisions and every RAW_READ outcome are fixed functions of N and
of the outcomes of P's own measurements so far: by induction over steps, the basis content z of all bank wires and
staged bits is such a function, and a RAW_READ returns a bit of z. So at each aligned point the physical state is

    sum_z p_z |z><z| (x) rho_z,

where rho_z is a state of the mapped P qubits and of any reference system, possibly entangled and correlated with z,
and p_z is the probability of P's outcome history behind z. We show that pi(Phi_phys(X)) = Phi_P(pi(X)) for each step,
where Phi_P is P's channel for that step and Phi_phys is IFC-BANK-D's.

- Bank steps. On a state of this form, RAW_READ leaves the state unchanged and reveals a bit of z. RAW_WRITE maps z to
  a known z'. By Lemma 5.1 and Section 6, READ, WRITE, ALLOC_OWNER, FREE_OWNER and renumbering change the decoded
  record exactly as P's classical read, write, allocation or forgetting would. A forgotten staged bit mixes the
  conditional states rho_z as P's own forgetting does. By linearity this holds for arbitrary rho_z and references.
- Quantum steps. P's gate, measurement or reset on at most three qubits is applied to the slots holding those qubits.
  The classical controls of P's classically controlled gates are READ from the bank. LOOKUP is P's serial circuit,
  with table bits read from the bank. So, conditional on z, the action on rho_z is P's.
  In particular FW's PREP tries and steps 1-5 are applied gate by gate on the slots of A_0, ..., A_(w-1) and of its
  ancillas. By P Lemma 7.1(c), which holds for every input state, the instrument of P is realized on the mapped
  qubits whatever the correlations, and its measured cell code is recorded in the bank.
- Allocation and release. ALLOC_Q supplies a slot in |0> in tensor product with everything (by (I)), which is P's
  fresh qubit. FREE_Q applies reset, that is trace-out followed by |0>, to a qubit that P has just released, and pi
  forgets that qubit in both cases.
- Sources. Each request of P triggers exactly one acquisition of a fresh copy into the (n+1)-qubit acquisition
  register. Its qubits are SWAPped, with three CNOTs per qubit, into n+1 slots obtained by ALLOC_Q, and the register,
  now |0>, is released. SWAP is exact, so the mapped qubits hold the same rho_s. Prefix zeros and metadata are not
  source copies.

By induction from P's initial state (input N, all scratch zero), the reduced logical state of IFC-BANK-D equals
P's at every aligned point, on every branch: extraction errors, returned and recycled FW outputs, failed merges, partial
children, rejected copies and aborts included. Its source-request sequence and its output law equal P's. By (P1) it
outputs s with probability at least 1 - 2^-8 for every N and s.

The held-out-bit argument of P Section 10 and the coupling of P Section 5 are statements about P's logical law, which
pi preserves. The extra RAW_READ outcomes are functions of P's outcome history, so conditioning on them adds nothing.

## 8. Classical and quantum space

S_C. IFC-BANK-D's ordinary classical storage consists of:
- the input N and the output, n bits each;
- constant many staged words of O(n) bits each (a RAW index or wire number, an owner, row and bit index, a slot
  number, an operand of a word operation);
- O(1) staged bits, and O(log n)-bit counters of the bit-serial loops;
- the finite control of the fixed program.

A wire number needs at most log(2h) + 1 bits, which is at most sig sqrt n + 90 <= n by (8.2) below.

Before the prefix exists, the parameters are computed by streaming:
- C_ell directly, then D_i, Yd_i and Rc_i by the downward recurrences of P Section 7.3 (one pass, O(1) current words
  of at most Y + 1 <= 2r + 1 bits and the counter i), giving C_0 = Rc_0 D_0, and cb, Lam and the tree capacities;
- then U, DRAW, HQ and h, each of O(n) bits.

Once the prefix exists, the profiles are recomputed into the bank. The finite branch uses O(n) bits. So S_C = O(n) on
every branch.

S_Q. Bounds from P. By P (F1), r <= sqrt n + 1 <= 2 sqrt n and 2^cb <= n^-40 2^(sig sqrt n). Hence

    U = r 2^(cb+2) <= 8 n^-39 2^(sig sqrt n).                                              (8.1)

Bounds on the layout. These follow from (8.1), EW + 1 <= 2^21 n^20 (n >= 2), and n^22 <= 2^(sig sqrt n) for n >= 2^40:
- HQ = 2^20 n^2 U <= 2^23 2^(sig sqrt n);
- LSPAN = 2^56 n^8 U <= 2^59 2^(sig sqrt n);
- DRAW <= 2^80 n^-11 2^(sig sqrt n) + 2^40 n^22 <= 2^81 2^(sig sqrt n), since the terms after LSPAN (EW+1) in (4.1)
  total at most 2^40 n^22.

By (4.2),

    S_Q <= 2h + n + 1 <= 4 DRAW + n + 1 <= 2^84 2^(sig sqrt n),                            (8.2)

using HQ + 2 <= LSPAN <= DRAW, so that h < 2 DRAW.

This counts every physical wire: bank values, tags, epochs, flags, RAW scratch, every slot (live, free or never used),
the padding up to 2h, and the acquisition register. It is a fixed span, the same on every branch. The finite branch
uses O(n) qubits. So S_Q = O(2^((459/800) sqrt n)), with no polynomial factor: the trim of 40 ceil(log2 n) bits in cb
(P Section 0) absorbs the n^30 of the bank layout.

## 9. Explicit polynomial ledger

Every core step of IFC-BANK-D pays its address fee ADDR = ceil(log(S_C + S_Q + 2)), and ADDR <= n by (8.2). An
instruction is one of the following:
(i) a logical READ or WRITE;
(ii) a RAW_READ or RAW_WRITE;
(iii) a bit operation on staged words;
(iv) one gate, measurement or reset of P on mapped slots;
(v) an ALLOC_Q or FREE_Q, or a descriptor field update;
(vi) an ALLOC_OWNER or FREE_OWNER;
(vii) one acquisition, with its SWAP.

(L1) Control completion: at most c n^4 instructions per P step.
- A P step touches at most three classical bits or three qubits.
- Locating a classical bit takes the owner of its array (a field of the current frame row) and its row and bit index
  (O(n)-bit words held by P). Forming (3.1) and the RAW index (EW+1)c takes O(n^2) staged bit operations.
- Locating a qubit takes one slot number from a descriptor field.
- Bookkeeping. P is a fixed program with s0 statements, s0 an absolute constant. Let D <= c(r+2) bound the
  iterations and calls open at once (bounded static nesting, recursion depth at most a + JI + J7 + ell + 2 <= 2r). Every innermost body consists of
  P steps, so every opened iteration or call runs at least one P step. Charge each control event to the first P step
  of the innermost context containing it. The events are: counter update and test, frame push or pop, the at most s0
  allocate/free statements of a body (ALLOC_OWNER and FREE_OWNER, instruction (vi); slot operations are wire events,
  counted in (4.3)), and the at most s0 loop-exit tests of a body. A P step is the first step of at most D contexts,
  each charged at most 2 s0 + 2 events of at most 13n instructions. So bookkeeping is at most c' n^2 instructions per
  P step.

(L2) Cost per instruction: at most c n^24 charged bit operations, which is at most n^100 for n >= n1, where we also
take the threshold n1 of Section 6 to be at least c.
- (i): 2EW + 1 <= 2^22 n^20 RAW accesses (EW tag bits, EW epoch bits and the value bit). Each access is one core step
  plus ADDR, plus an O(n)-bit increment of a RAW index, which is O(n) staged bit operations with their fees; so each
  access costs O(n^2). Add O(n^2) staged bit operations of address arithmetic, each of cost at most c n. At most
  c n^22.
- (ii), (iii) and (iv): at most c n.
- (v): three O(n)-bit fields (head, NEXT[k] and virgin), or one descriptor row (a slot number of at most n bits), so
  O(n) logical READs and WRITEs, plus one reset. At most c n^23.
- (vi): a scan of OWN flags (OWN RAW accesses, c n^4), the all-ones test, the increment and the copy of G (at most
  5 EW RAW accesses), and a binding of O(n^2) RAW bits. At most c n^22, plus Section 6 if it is triggered.
- (vii): the source cost n+1, then 3(n+1) CNOTs with fees, and n+1 ALLOC_Q with descriptor updates. At most c n^24.

The bounds n^4 and n^100 are the degrees used by mpjunior92. The items above show that they hold with room.

(L3) Wire events. By (4.3) there are O(n^16 (C_P + Qcap + HQ + 1)) of them, each of cost at most n^100 by (L2).

(L4) Prefix. HQ + 2 <= LSPAN <= DRAW, so h < 2 DRAW. Allocating wires 0, ..., 2h-1 in |0>, writing head := HQ, and at
the end resetting and releasing the 2h wires costs at most c n h <= c n DRAW. The streamed parameter computation and the profiles cost poly(n), which is
included in the next display.

Total. Take n >= n1, so that no renumbering occurs (Section 6), and any branch. The charged work is at most the sum
of four terms:
- c n^4 C_P instructions from (L1), each of cost at most n^100;
- O(n^16 (C_P + Qcap + HQ + 1)) wire events, each of cost at most n^100 (L3);
- at most Qcap acquisitions, each of cost at most n^100;
- c n DRAW for the prefix, plus poly(n) for the parameters (L4).

With C_P <= T_P, and allowing (L1) a second factor n^4 of slack, so that n^4 * n^4 * n^100 <= n^120,

    T <= c n^120 (T_P + Qcap + HQ + 1) + c n^100 DRAW.                                     (9.1)

The derivation above gives c n^28 per P step and c n^24 per wire event, far below these degrees. For 2^40 <= n < n1,
and on the finite branch, the work is bounded on every branch, so these lengths change only the constant.

## 10. Time and samples

T. Substitute (P6), (8.1) and Section 8 into (9.1):
- T_P = O(n^(13/2) 2^(e sqrt n)) gives degree 253/2 <= 127;
- Qcap = 4 n C_0 + K = O(n^(7/2) 2^(e sqrt n)) gives degree 247/2;
- HQ = O(2^(sig sqrt n)) and DRAW = O(2^(sig sqrt n)) give n^120 HQ + n^100 DRAW = o(2^(e sqrt n)), as sig < e.

So

    T = O(n^127 2^(e sqrt n)),   e = 1449/1000.

The coefficient e is exact. On the tree side, H + dl <= e r + 2 follows from P's integer schedule
(H <= (140013/160000) r + 3 by log2 7 < 45/16, dl <= (459/800) r - 1, and 231813/160000 < 1449/1000). On the pool side, log PP <= e r + 3 uses
ell = Lam <= (459/800) r and P's bracket log2 RHO < HI, which P proves from the series of ln 2, and the exact inequality
HI (459/800) + 140013/160000 < 1449/1000 (P (8.5)).
With r <= sqrt n + 1 these give
2^(e r) <= 2^e 2^(e sqrt n). Initialization, every failed or recycled branch, every abort, all bank, descriptor and
slot work, the source moves and the output-first cleanup are included.

Q. IFC-BANK-D makes exactly one acquisition for each request of P and none other (Section 7). On the main branch,
Qcap = 4 n C_0 + K counts every rejected copy, every pool-stage, supplier and pool abort, and every discarded merge
input of every batch (P Section 13). By (P6), C_0 <= 8 (ell + 1) RHO^ell C_ell <= 3 * 2^29 r^5 PP = O(n^(5/2) 2^(e sqrt n)),
so

    Q = Q_P <= Qcap = O(n^(7/2) 2^((1449/1000) sqrt n)).

The finite branch uses at most N(n+10) copies, a constant over its finitely many N. Bank zeros, tags, slot
bookkeeping, SWAPs and renumbering are charged as work and storage, never as copies.

## 11. Growth indices

For fixed c > 0 and fixed a >= 0, log(n^a 2^(c sqrt n)) = c sqrt n + a log n. Then
log log max(4, n^a 2^(c sqrt n)) = (1/2) log n + log c + o(1), and the index g = 1/2 exactly. This holds for each of
the declared envelopes of T (a = 127, c = 1449/1000), S_Q (a = 0, c = 459/800) and Q (a = 7/2, c = 1449/1000).
For S_C = O(n),
log log max(4, n) = log log n, so g = 0. The indices are those of the proved upper envelopes; no lower bound is
claimed. The structured objects in submission.json are exactly these four envelopes.

## 12. Error tolerance

The fifth claim is epsilon(n) = 0, under the model in which every acquired copy is an independent ideal coset state.
Everything above is proved under this model. No positive tolerance for malformed copies is claimed, and zero does not
assert that robustness is impossible. Under a different, adaptive malformed-supplier model the extra bank
measurements could matter; no such transfer is claimed.

## 13. Scope and limitations

- The time growth index is 1/2, as for P and the earlier versions of this construction. The research goal
  2^(O(n^(1/3))) is not reached. This is a trade-off row: S_Q = O(2^((459/800) sqrt n)) below T = O(n^127 2^((1449/1000) sqrt n))
  and Q = O(n^(7/2) 2^((1449/1000) sqrt n)), with S_C = O(n). The schedule family of P gives T = 2^((2/(3 sig) + sig/2 + o(1)) sqrt n)
  for every cap ratio sig <= 2/3; at sig = 459/800 that is 3192043/2203200 = 1.4488..., and 1449/1000 keeps the slack for n >= 2^40.
- The memory construction is not ours, capped recycling pools are qzv's, and capped IFC trees in this storage are
  mpjunior92's (Section 1). What this file adds is their composition through P and the check that P exposes the
  interface the construction needs.
- S_Q is 2^(Theta(sqrt n)), because classical records are moved into counted qubits. This is not an improvement over
  algorithms with O(n) or 2^(o(sqrt n)) qubits.
- All polynomial powers, the trim 40 ceil(log2 n), the threshold n >= 2^40, the group size w = 2^28, FW's gate and
  scratch constant c_F and the tag width (n+2)^20 are unoptimized.
- P's own statements in virtual.md (its Sections 0, 14 and 15) concern P's storage model. The four bounds of this file
  concern IFC-BANK-D.
