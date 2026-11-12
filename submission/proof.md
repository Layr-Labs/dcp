# IFC-BANK-D-CT: seven-input dissection merges above saturated implicit-fiber four-input merges and a capped recycling pool with streamed leaves, with O(n) classical workspace through a counted basis bank

CURRENT LOWCAP sets ACTUAL sigma=9/50,cb=floor(9r0/50)-40Lg,JI=ceil(3Lam/5),J7=ceil(217r/250),mainn0=2^50. It retains the explicit Y<=3r/K3r confidence budget, r/8 physical fit and refined quantitative PREP/pool-work proof. Actual merge-level count coefficient122/125<1 preserves existing failure/frame limits. Only public cap/stage choices change; all instrument/decoder words, means and half-offsets are EXACT to the quarter-refined source. Full positive-part capacity and every charged native/source/failed-branch bound are supplied; no verdict supplies a premise.

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N), e = 13717412056659/4842323968000 and sig = 9/50. The single physical
algorithm IFC-BANK-D-CT below receives N in binary and fresh independent copies of rho_s, and outputs the entire s with
unconditional probability at least 1 - 2^-8. On EVERY execution branch (wrong extracted labels, FW-stage (PREP
included, final requests included), supplier and pool aborts, failed and retried merges, four-input and seven-input merges, discarded copies, tag
renumbering, initialization and final cleanup included) it satisfies jointly

    T = O(n^(19/2) 2^(e sqrt n)),   S_C = O(n),   S_Q = O(n^(-77/2) 2^(sig sqrt n)),   Q = O(n^(7/2) 2^(e sqrt n)).

All constants are absolute. The growth indices are 1/2, 0, 1/2 and 1/2. The fifth claim is clean-input tolerance 0.

Current source and change. This archive starts from e-man07's published IFC-BANK-D,
5a2644a6-6367-4ec6-95ac-7388372f31fc, immutable commit 4e9e501ad43f56841e3638cf2a34eed62af23c3a.
Its COMPLETE physical bank and logical P construction, including FW, capped pools, MERGE4I, MERGE7,
all failure/sigma-field lemmas and decoders, are supplied here. The three virtual*.md files fully supply the source material. In CURRENT LOG7, virtual.md and virtual2.md revise the numerical upper-bound coefficient and exact8.5/F6 slack proof; virtual3.md remains byte-identical. Per-level logical instrument words are retained, while CURRENT RETUNED changes the stage counts and finite threshold explicitly. Current changes additionally execute an explicit counted RAW continuation dispatcher with cached current-frame/PC words (Section4), charge possible ancestor walks and separate logical-bit accesses from allocation macros (Section9), and pad ACTUAL physical row/metadata strides to powers of two, use the explicit shift/add and sequential-bit-counter generator of Section 9 and an eight-word owner binding, and reduce ACTUAL P-array row capacity to 2^24*2^cb and move the slot NEXT/head/virgin metadata into dedicated counted untagged RAW words. They retain ACTUAL row-level generation tags (ONE epoch per ROW), with EW=ceil(sqrt n), first-write row clearing, and smaller ACTUAL fixed owner/row/field/slot capacities specified in Section 3,
the resulting physical addresses/span and tag loops, and a new explicit native cost ledger. The logical P program,
its per-level quantum instrument words are retained. CURRENT stage counts, source requests and caps use the retuned exact formulas; they are not claimed identical to the predecessor schedule. Sections 1 and the historical paragraphs
below retain the source's credit and first-person voices; original claims of novelty and historical acceptance
refer to those authors at their source time. They do not claim current authorship or current graph verification.
Current physical work develops our linear-word, square-root-word and compact-bank precursors by replacing EACH BIT tag with ONE ROW tag and explicitly clearing the row on its first write in a new activation; the present step additionally separates the quantum-slot free-list metadata from the P owner arrays and removes their extra r factor in row capacity. It keeps compact capacities, the square-root epoch and charged repeated renumbering. That precursor carries the same COMPLETE original P construction. Neither its publication status nor its review supplies a correctness premise. No earlier review is a correctness premise. All FOUR mathematical files are evidence for ALL five current claims;
in particular virtual3.md is included even though the source's original claim evidence arrays omitted it.

IFC-BANK-D-CT executes a fixed reference algorithm P without changing any of its quantum operations, measurements,
source requests or classical decisions. P is IFC-LIMIT-D, whose complete specification and proof are given after the
marker line of virtual.md, in virtual2.md (P Sections 7.3, 8, 9, A and B) and in virtual3.md (P Sections C and D). "P Section x" and "P (x.y)" refer to that
text; "Section x" refers to this file. The resource statements inside virtual.md concern P in its own storage model,
in which classical records are ordinary bits; they are not claims of this file. IFC-BANK-D-CT changes only where data live:
- every classical record of P, except constant many O(n)-bit staged words, is kept in basis-state qubits, which are
  counted in S_Q and are read and written only at classically known addresses (Sections 3-6);
- P's qubits live in a fixed counted array of quantum slots, managed by an indexed free list (Section 4).

Notation for P: r, r0, Lg, ell, dl, H, a, JI, J7, Lam, cb, kappa, K, C_ell, D_i, Yd_i, Rc_i, C_0, Y and Qcap are as in P
Sections 0, 7.3, 8, 11 and 13; w = 2^28, q = 2^27, RHO = 16385/8192, HI and c_F are as in P Sections 7 and 8; and
PP = RHO^ell 2^H (P Section 14). A "P step" is a core step in the sense of P Section 2, C_P is the number of P steps on
a branch, and T_P is P's charged time (P (2.1)), so C_P <= T_P. All logarithms are base 2. Constants c, c0, c1 are
absolute.

Historical source base and original changes (this paragraph describes the P change in the ORIGINAL IFC-BANK-D source, before the CURRENT shorter epoch and compact physical capacities of Sections 3-10). IFC-BANK-D is IFC-BANK-F (kshitij-hash's public submission
f7b12b14-f990-4ff5-b513-63e55e39344c; this archive starts from the text of kaankolcu's re-tuned snapshot
04f7e018-7297-49c6-b704-5c774a8b8ebe of it) with its reference algorithm P changed from IFC-LIMIT-F to IFC-LIMIT-D, so
that the construction runs at the cap ratio sig = 9/50, where IFC-LIMIT-F's schedule is infeasible. The physical
construction of Sections 3-9 here is unchanged and is applied to the new P without change, except that the counts
of (P3)-(P5) and of Section 4 now include the seven-input merges (seven index registers per tree level, so 28n in
place of 16n, and MERGE7's registers and arrays). The changes to P are
listed at the start of P Section 1 and are:
- a new schedule (P Section 0 and P Section 8 in virtual2.md): ell = Lam pool levels on chunks of exactly 2^cb qubits,
  one binary tree level (a = 1, dl = Lam - 1), four-input fibers l_j = min(Lam + 1 + 2j, 2 Lam), so that the four-input
  levels j >= ceil((Lam - 1)/2) are saturated (r_j = 0), followed by J7 = ceil(217 r/250) seven-input levels (below), and
  e = 13717412056659/4842323968000; Lemma 8.1 is
  reproved for this shape and the size facts (F1)-(F6) are rederived;
- a streamed leaf supply (P Sections 7.3 and 9): as 2^H > 2^cb the tree takes its leaves from a leaf buffer refilled
  by final requests of 2^cb qubits, at most Rc_ell per batch, instead of one final pool of C_ell qubits; Lemma 7.3,
  Lemma 9.1 and Lemma 9.2 are restated for it;
- the explicit statement of MERGE4I's case r = 0 (P Section A, Lemma B.1 Stage 1);
- fibered seven-input dissection merges (P Sections C and D of virtual3.md, new): the four-input levels stop at
  JI = ceil((3/5) Lam) and are followed by J7 Phase M levels of MERGE7, level k with fiber width
  w_k = max(0, 3 Lam - 2 JI - floor(14 (k+1)/5)), each collimating 6 Lam - kappa - w_k bits from seven inputs of 2^Lam
  entries (7 Lam - 1 - kappa - w_k at the root), with failure bound 2^(2 - kappa) (P Lemma D.1); 2^H = 2^(a + 2 JI) 7^J7.
The first three changes make IFC-BANK-S (e-man07, 3b49ab04-1ede-4baf-9802-79c3dfa95b06 and its siblings at other cap
ratios); the fourth is new in IFC-BANK-D.
Here those facts of P that this file uses are unchanged in form: at most 4 r 2^cb pool qubits at once, every array of
P at most 2^(cb+1) rows, C_0 <= 8 (ell + 1) RHO^ell C_ell, C_ell <= 4 * 2^25 r^4 2^H, Y <= 3r, log PP <= e r + 3 and
H + dl <= e r + 2. Only (P3) and (P5) of this file mentioned the final pool; they now name the leaf buffer. In the text below "we" and "our" refer to kshitij-hash, the authors of IFC-BANK-F; the changes above are
e-man07's. No step relies on any verdict.

Current memory/time tradeoff uses sig=9/50 and a longer seven-input stage extending past fiber extinction. The complete NEW capacity bound integrates max(0,Y1-14x/5) over its whole support, instead of requiring all final fibers positive. All per-level FW/merge/failure/decoder and native simulation obligations are supplied; the exact resource theorem is not a source verdict.

## 1. Provenance: the storage construction is mpjunior92's

The construction of Sections 3-7 and the explicit-degree ledger of Section 9 are mpjunior92's idea, not ours.
mpjunior92 applied them to qzv's HPC-127 (public submission 2aad498c-d5e9-4f64-a222-3b2f7f961738):
- HPC127-TAGBANK (6c0e2efd-41bd-4018-a24e-e386f3069c9b). It introduced the indexed free list and banked descriptors
  for an exponential coherent pool, the per-wire-event charge and the fixed spans (A, R, Wrow, H, B, e, D there; OWN,
  ROWS, WROW, HQ, LSPAN, EW, DRAW here) for HPC-127; it carries the tagged bank, exact renumbering and decoded
  classical-quantum invariant from IFCS1310-TAGBANK.
- HPC127-SHARP (73741b63-bfa1-4d24-b254-ca6fd0549221). The same construction with explicit polynomial degrees
  (n^4 control completion, n^16 wire events, n^(19/2)0 per charged event, total power 132) in place of a pure envelope.
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

Finite branch (n < 2^50). P is the exhaustive tester of P Section 13: for cand = 0, ..., N-1 use n+10 fresh copies,
apply Shift_cand, measure the control in X, and reject cand at the first minus; output the first unrejected cand, or
0. IFC-BANK-D-CT runs it with ordinary storage. It holds cand, a copy counter and the current copy, so O(n) bits and
O(n) qubits, and it makes the same acquisitions. There are finitely many such N, so this branch changes only
absolute constants.

Main branch (n >= 2^50). P computes exactly the integers of P Section 0 (r, r0, Lg, kappa, ell, dl, H0, cb, Lam,
a, JI, J7, H) and of P Sections 7.3 and 8 (K, C_ell, D_i, Yd_i, Rc_i, C_0 = Rc_0 D_0, Y, pbmax_i and the tree capacities),
puts Qcap = 4 n C_0 + K, and runs P Sections 5-13: label extraction LE; the chunked FW stage (FWLEVEL runs of q(Y+1)
rounds on chunks of D_i, with buffers and run caps); the tree shape and bit allocation of P Section 8 for each
requested B; BATCH with its tree of binary MERGEs, four-input MERGE4Is and seven-input MERGE7s; the free-frequency decoder; and the 2-adic
part. Every ABORT outputs 0.

Completion of unspecified orders. P leaves three orders open:
- equal-key ties in its merge sorts;
- the order of LIVE after an FWLEVEL round;
- the order of OUTPUT.

IFC-BANK-D-CT fixes them as follows:
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
- Y <= 3r <= n (P (F6)).
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
leaf qubits with kk != 1 (P Section 12), and R after a step-4 FAIL of MERGE (P Section 6.2). IFC-BANK-D-CT completes P
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
- C_0 <= 8 (ell + 1) RHO^ell C_ell (P Lemma 7.3(d)) and C_ell <= 4 * 2^25 r^4 2^H (P (F4));
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

    OWN = 2^16 r owners,  WROW = 2^16 n bit cells per row,  ROWS = 2^24 * 2^cb rows per owner,
    HQ = 2^20 U quantum slots.

An owner holds one logical array. The logical bit (o, i, j), with o < OWN, i < ROWS and j < WROW, has the address

    c = o ROWS WROW + i WROW + j  <  LSPAN = OWN ROWS WROW = 2^56 r n 2^cb.               (3.1)

Fit. Every actual P array in (P3) fits ROWS=2^24*2^cb. Pool/tree/merge arrays have at most
2^(cb+1) rows (the explicit P3 list). Other P arrays and scratch descriptors have polynomially many rows:
K=2^13(3r+ceil(log2 n)+30), 2(J_e+1)=2(n+5), profiles of O(r) rows,4096 fixed rows, and
c0n+c_F<=2^12 n+n^3<n^4. For n >= 2^50, cb>=r/8 and n^4<=2^cb (check 4log2 n<=r/8 at the endpoint
and monotonicity). K<=2^18r<=n^4. Thus all these arrays fit as well. Every P row has at most12n bits,
so WROW=2^16n suffices. Slot descriptors store numbers below HQ<2^n. NEXT is NOT a P array:
its separate dedicated RAW region of HQ n-bit words is counted in (4.1) and has no owner or row tag.

Descriptors of P's qubits (Section 4) have one slot number per row:
- a pool qubit's slot number is a field of its row in the pool list, LIVE or OUTPUT;
- an index register of a phase vector has a descriptor array of at most Lam rows in the same per-level family as
  its table;
- each of P's named scratch registers (P4) has its own descriptor array of at most c0 n + c_F <= U rows.

Fewer than 64 arrays are live per tree level and per FW level. The others are fewer than 64 + 1100: fewer than 64
for the decoder, LE, profiles, table, slot metadata and frame arrays, and fewer than 1100 scratch descriptors (the
registers of (P4), MERGE4I's and MERGE7's included, and of FW). So at most 64(a + JI + J7 + 1) + 64 (ell + 1) + 1164 <= 512(a + JI + J7 + ell + 4)
<=512(2r+4)<=2048r<2^16 r=OWN arrays are live at once (r >= 2^25). Frames of
P's depth-first recursion and its loop counters are rows of fixed frame arrays indexed by depth; they are not
ordinary memory. Owners are reused through FREE_OWNER and ALLOC_OWNER (Section 5). These capacities are fixed before
P starts and do not depend on the branch.

## 4. Physical layout, and the quantum slot allocator

Epoch words have EW=ceil(sqrt n) significant bits. Each logical row has ONE ROW TAG.
Let NP(x) be the least power of two >=x (positive integer), and put

 VS=NP(WROW+EW), NS=NP(n), ES=NP(EW), BS=NP(8n), LROWS=OWN*ROWS.

All four strides are explicit powers of two; ROWS=2^(cb+24) is a power of two as well.
The ACTUAL RAW layout, including ALL padding, is:
- LROWS physical rows of VS bits. Row u=o*ROWS+i has base b=u*VS; values are b+j,0<=j<WROW,
  and its tag is b+WROW+t,0<=t<EW. All other bits up to the VS boundary are counted zero padding.
- HQ dedicated NEXT words of NS bits, first n significant bits each; remaining bits count as padding.
- two NS-bit words for head and virgin, first n significant bits each.
- OWN+8 ES-bit epoch words for ep(o),G,backup and six spare words, EW significant bits each.
- OWN active flags.
- OWN binding records of BS bits, first 8n significant bits each, unused positions counted padding.
- 2^20n^4 RAW interpreter scratch bits (separate from the explicit binding region);
- FRAMECAP=8r RAW continuation frames, FS=NP(16n) physical bits each, including all frame padding.

Thus the exact RAW span is

 FRAMECAP=8r, FS=NP(16n),
 DRAW=LROWS*VS+(HQ+2)*NS+(OWN+8)*ES+OWN+OWN*BS+2^20n^4+FRAMECAP*FS.               (4.1)

The whole prefix is initialized to zero once; padding remains untouched until final reset/disposal.
Every segment start is the sum of preceding sizes, computed once by the streamed public generator.
For row addressing form u by CONCATENATING owner bits with the fixed (cb+24)-bit row field, then shift by
log2 VS (copying bits and zeros explicitly), then add the desired value/tag offset bit-serially.
NEXT, epoch and binding records likewise use a shift by log2 NS,ES,BS and an addition of their segment start.
No repeated long multiplication, unit-cost shift, word lookup or superposed RAW address is used.
All public offsets fit O(n) bits and are held in constant-many staged words.

Binding encoding. The typed fixed controller assigns a <2^16 family number to each array role in the explicit P3
list (fewer than64 per level and1164 others; child positions and scratch roles are part of the family).
A binding consists of eight n-bit words: family, level/depth, caller-frame owner, caller-frame row,
caller field, row bound, field bound, and zero reserve. The P3 family/level plus the live caller frame identifies
an active logical array; its owner ID is stored in that caller's bank field and is used for later accesses.
All quantities fit n bits on the main branch. Nested invocations retain their own banked frame rows;
freeing/reusing a frame occurs only after its arrays are released. No global search or full call-path copy is needed.
ALLOC_OWNER writes all8n significant binding bits sequentially and updates its caller's O(n)-bit owner field;
padding is never part of the payload. This is the actual chosen physical dispatch encoding, not an assumption
that arbitrary unbounded context records have unit cost. All frame access is through charged logical bit operations.

Explicit continuation dispatcher. The ACTUAL physical controller compiles the complete fixed P syntax to
static program-counter states. Its ordinary cache holds current PC, RAW frame index, current P-frame owner/row
and constant-many operands/pointers, all O(n) bits; all continuations and local records live in counted qubits.
Each RAW frame has sixteen n-bit fields, then zero padding to FS: parent index, return PC, procedure/loop site,
P-frame owner, P-frame row, loop-counter binding owner/row/field, phase/branch flags and zero reserve fields.
The variable-size local data and array handles are P's existing banked frame rows and arrays, not copied into
a classical stack. A static field identifies each local/formal name in those rows. A reference to a nonlocal
binding may FOLLOW PARENT LINKS, at most FRAMECAP times, reading the corresponding banked field at each frame;
no constant-time lexical environment or RAM lookup is assumed.

On CALL, evaluate/pass the same P arguments through charged P-bit/handle operations, write ALL sixteen n-bit
fields of the next RAW frame before use, including zero reserves, set parent/return site and P-frame binding,
then advance the cached frame index and PC to the callee. Returned phase-vector handles transfer by their
banked descriptors; no quantum state is copied. On RETURN, read parent index and return PC, transfer the same
P result/handle, and update the ordinary cache. Popped records need not be cleared: a later PUSH overwrites all
significant fields. On loop entry use a frame for the loop binding; iteration updates/tests reuse that frame
and the banked counter, rather than push another frame per iteration. Conditional branches read the SAME P
bits/outcomes; arithmetic expressions and quantum primitives expand to the SAME P core-step code, never a free
word predicate. A primitive core-step emits precisely its P gate/measurement/reset/classical-bit operation
on the mapped operands, then advances PC. FAIL, retry and ABORT continuations follow P's specified control;
at termination output is written before the whole prefix is reset/disposed.

Only the tree and pool supplier recurse to input-dependent depth: at most r and r respectively. The remaining
listed P loops/generator procedures have bounded static nesting, conservatively at most4096; nonrecursive
calls can be statically inlined, and finite fixed FW gate generators are emitted by flat iterative code.
Thus active control depth<=2r+4096<3r for r >= 2^25, below FRAMECAP=8r. Uniform n-bit arithmetic/gate-generation
loops are iterative, not hidden recursive stacks. This rule specifies an implementation with a fixed finite
control graph and all dynamic continuations in the RAW region. Parent walks are capped by the actual depth;
no owner/slot allocation is performed by a PUSH itself. P's logical frame arrays remain the P3 inventory.
Every RAW frame access uses the public power-of-two FS stride and the fully charged streaming generator. A static field ordinal f<16 has offset f*n, computed with at most four shift/add passes on O(n)-bit operands; these operations are included in address setup.

Physical wires:
- RAW index j is wire 2j;
- quantum slot k < HQ is wire 2k + 3;
- wire 1 is spare.

Let h be the least power of two with h >= max(DRAW, HQ + 2). On the main branch IFC-BANK-D-CT first computes the
parameters with O(n) staging (Section 8). It then allocates wires 0, ..., 2h-1 in |0> once, and releases them once at
the very end, after the output is written. In between it allocates only an (n+1)-qubit acquisition register, one at
a time. Hence on every main branch

    S_Q <= 2h + n + 1.                                                                    (4.2)

Bank wires are acted on only by computational-basis measurements and by X gates conditioned on classical bits.

Slot allocator. Dedicated RAW regions hold head, virgin and NEXT (n bits per word), independent of P owners and generation tags. Every metadata word READ/WRITE streams all n bits through constant-many staged words, using only RAW operations at known addresses. The P-bank arrays hold the descriptors of Section 3. Every P quantum register is a pool qubit or a register with its own descriptor
array, and its descriptor rows list its slot numbers, one per row. P's lists store slot numbers where P stores wire
indices. head = HQ means empty.
- ALLOC_Q: if head != HQ, put k := head and head := NEXT[k]; otherwise put k := virgin and virgin := virgin + 1.
  Return k.
- FREE_Q(k): reset wire 2k+3 (the reset core step, which records no outcome); then NEXT[k] := head and head := k.

Initially head := HQ and virgin := 0. FREE_Q writes EVERY n-bit position of NEXT[k], including leading zeros. NEXT[k] is read only after FREE_Q(k) has written that ENTIRE word. Untouched NEXT words are never read. Consequently NEXT needs no generation tag and no clearing on owner reuse. head and virgin are initialized explicitly, remain persistent RAW words, and are updated in full. No operation scans the
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
at once. Since c0 <= 2^12 and c_F <= n^3 <= 2^cb (cb >= r/8 by P (F1)),

    live <= 5 r 2^cb + 2^12 n + 28n < 3U < HQ=2^20 U.

Indeed 5r2^cb=(5/4)U, and (2^12+28)n<U follows from U>=n^3 and n >= 2^50. These live counts include all P scratch and recycled inputs, on every branch. The NEW smaller slot array therefore never overflows.

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

- READ(o,i,j): form its row base b, compare that ROW tag to ep(o) bit-serially, and return RAW b+j
  if equal, otherwise 0. It writes nothing and performs no row initialization.
- WRITE(o,i,j,v): compare the ROW tag to ep(o). If unequal, RAW_WRITE ALL WROW value bits of that row
  to zero, one at a time, then copy ep(o) into its tag. Finally RAW_WRITE b+j to v. If the tag was equal,
  change only b+j. The whole first-write clear is ACTUAL work and is charged in Section 9 even if v=0.
- ALLOC_OWNER: scan active flags for an inactive owner; if G is full, execute Section 6. Then increment G,
  copy it into ep(o), set the active flag and record its binding. No row is eagerly initialized at allocation.
- FREE_OWNER(o): clear its active flag. No row is cleared at free.

Initially all RAW bits are zero and active owners always have positive epochs.

Lemma 5.1 (row-lazy arrays). At aligned points every row tag is at most G; a freshly activated owner's epoch
exceeds every tag previously stored in its rows. For each active row, every READ returns the last bit value
written in the current activation, or zero if none, including bits never written in a partially written row.

Proof. Allocation picks a generation strictly above all old row tags. Until a row's first WRITE, the tag
mismatches and every READ returns zero, including old dirty values. The first WRITE clears ALL value bits
before assigning the current tag and desired bit. Thus all unmodified bits are now genuine zeros. Later
WRITEs in that row preserve every other bit, and READ returns its stored value. There is no way to install
an equal tag without first zeroing the row (except value-preserving exact renumbering in Section 6).
WRITE tags never exceed G. FREE changes no active logical record; a later allocation gets a fresh epoch.
Section 6 preserves the full decoded row and restores these invariants. Induction proves the assertion.

A row clear uses only a staged value bit/counter and the fixed raw span, never an ordinary row buffer.
Allocation/free do not clear exponential arrays. All owner scans, tag loops and first-write row clears
are paid, with no amortized omission in Section 9.

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

IFC-BANK-D-CT never assumes G cannot wrap. When owner allocation sees G full, pause P and visit every owner.
For an active owner, copy its OLD ep into RAW backup. For each row, compare its tag to backup: if they differ,
RAW_WRITE ALL WROW values to zero; if they match, preserve ALL stored values. Then set the row tag to ownerID+1.
After ALL rows of this owner have been processed, set that owner's ep=ownerID+1. For an inactive owner clear all P-row values/tags and ep to zero. The dedicated RAW NEXT/head/virgin records are outside these owner regions and are NEVER touched by renumbering. The RAW continuation region and cached PC/frame pointer are also unchanged; the paused logical control resumes at the same next P operation.
Finally set G=OWN and resume the pending owner allocation. No P operation or quantum gate/request is made
while this maintenance is in progress. Partial row/owner updates are not aligned P points.

Every active decoded value is preserved: a matching row already contains the complete current logical row;
a mismatching row decodes entirely to zeros and is materialized as zeros before tagging. Inactive arrays
remain absent. Afterwards every tag is <=OWN=G, active tags match their new ep, and later generations remain fresh.
For n >= 2^50, OWN+2<2^(EW-1), since OWN=2^16r and log2(2(OWN+2))<19+2log2 n<sqrt n.
Thus at least 2^(EW-1) outside owner allocations separate successive renumberings, and the first interval is longer.

Each value/tag/epoch/scratch iterator visit uses at most O(n^3) charged work, including all address formation;
there are O(DRAW) such visits. So one renumbering costs O(n^3 DRAW), conservatively <=C n^22 DRAW as used below.
No additional quantum wire, source acquisition, failure or abort is introduced.

Unlike the linear-width variant, this program does NOT assert eventual absence of renumbering.
Let A be the number of outside ALLOC_OWNER calls on a branch. Renumbering itself calls none.
The logical control caps below give A<=C n^2(C_P+Qcap+poly(n))<=poly(n)2^(e sqrt n).
Every interval before a renumber has at least 2^(EW-1) outside allocations, hence the number R of
renumberings obeys R<=2A 2^-EW, without an additive one: if A is too small, R=0.
Their TOTAL charged work is at most

    C n^22 DRAW A 2^-EW <= poly(n) 2^((e+sig-1)sqrt n).

Since sig=9/50<1, this is o(2^(e sqrt n)). This is a distinct amortized physical maintenance phase,
charged on EVERY branch using deterministic caps, with no probability/favorable-event assumption.
The renumberings need no new wires or snapshots besides the already counted backup.
The finite exhaustive branch remains finite. No unknown eventual threshold is used for this bound.

## 7. Correctness: the decoded classical-quantum invariant

An aligned point is a boundary after a COMPLETE compiled P step/acquisition or a completed structural control transition, before the next begins. Intermediate RAW bit loops and partial frame updates are not alignment points. Define a map pi from the physical state to P's
logical state at aligned points:
- decode the cells of every active owner through its epoch (Lemma 5.1);
- decode the cached PC plus RAW continuation parent/return records into P's control position, pending calls/loops and bindings; keep its existing banked local records;
- map each slot that holds a live P qubit to that qubit, using the descriptors (injective by (I));
- trace out free slots, padding wires, tags, inactive owners, allocator fields and every other physical-only record.

IFC-BANK-D-CT has no randomness of its own. Its staged decisions and every RAW_READ outcome are fixed functions of N and
of the outcomes of P's own measurements so far: by induction over steps, the basis content z of all bank wires and
staged bits is such a function, and a RAW_READ returns a bit of z. So at each aligned point the physical state is

    sum_z p_z |z><z| (x) rho_z,

where rho_z is a state of the mapped P qubits and of any reference system, possibly entangled and correlated with z,
and p_z is the probability of P's outcome history behind z. We show that pi(Phi_phys(X)) = Phi_P(pi(X)) for each step,
where Phi_P is P's channel for that step and Phi_phys is IFC-BANK-D-CT's.

- Controller steps. Each PUSH/CALL, loop enter/update/test, branch and POP/RETURN realizes the identical
  syntactic P transition with the identical local/formal/handle bindings. Parent walks read only P's specified
  environments, even when they span O(r) frames. Induct on the compiled finite syntax and the RAW parent chain:
  the decoded next P core operation and operands equal P's at every aligned point. Metadata-only transitions
  are identity on the mapped P data/qubits and references; results/flags use the same charged bit operations.
  Aborts, failed child returns and retry loops obey the same induction. Never trace away a continuation needed
  for future P control: pi decodes it before discarding physical representation. No randomness is added.
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

By induction from P's initial state (input N, all scratch zero), the reduced logical state of IFC-BANK-D-CT equals
P's at every aligned point, on every branch: extraction errors, returned and recycled FW outputs, failed merges, partial
children, rejected copies and aborts included. Its source-request sequence and its output law equal P's. By (P1) it
outputs s with probability at least 1 - 2^-8 for every N and s.

The held-out-bit argument of P Section 10 and the coupling of P Section 5 are statements about P's logical law, which
pi preserves. Apply those arguments to exactly P's logical sigma-fields, without enlarging them by the physical RAW transcript; see Section 13. Equality of the decoded logical instrument suffices for its unconditional output guarantee.

## 8. Classical and quantum space

S_C. IFC-BANK-D-CT's ordinary classical storage consists of:
- the input N and the output, n bits each;
- constant many staged words of O(n) bits each (a RAW index or wire number, an owner, row and bit index, a slot
  number, an operand of a word operation);
- O(1) staged bits, and O(log n)-bit counters of the bit-serial loops;
- the finite control of the fixed program.

A wire number needs at most log(2h) + 1 bits, which is at most sig sqrt n + 90 <= n by (8.2) below.

Before the prefix exists, the parameters are computed by streaming:
- C_ell directly, then D_i, Yd_i and Rc_i by the downward recurrences of P Section 7.3 (one pass, O(1) current words
  of at most Y + 1 <= 3r + 1 bits and the counter i), giving C_0 = Rc_0 D_0, and cb, Lam and the tree capacities;
- then U, DRAW, HQ and h, each of O(n) bits.

Once the prefix exists, the profiles are recomputed into the bank. The finite branch uses O(n) bits. So S_C = O(n) on
every branch.

S_Q. Bounds from P. By P (F1), r <= sqrt n + 1 <= 2 sqrt n and 2^cb <= n^-40 2^(sig sqrt n). Hence

    U = r 2^(cb+2) <= 8 n^-39 2^(sig sqrt n).                                              (8.1)

Bounds on the NEW PADDED layout. r<=2sqrt n and 2^cb<=n^-40 2^(sig sqrt n).
VS<2(WROW+EW)<=2^18n; NS<2n; ES<2EW; BS<16n. Hence

 LROWS*VS+HQ*NS<=2^60 n^(3/2)2^cb
                 <=2^60 n^(-77/2)2^(sig sqrt n).

ALL other RAW terms, including explicit binding records, epoch padding, flags and scratch, total
at most2^23n^4, including FRAMECAP*FS<=256r*n=O(n^(3/2)). Since n^(85/2)<=2^(sig sqrt n) for n >= 2^50 (endpoint2125<(9/50)2^25 and
subsequent monotonicity),

 DRAW<=2^62 n^(-77/2)2^(sig sqrt n),
 S_Q<=2h+n+1<=4DRAW+n+1<=2^71 n^(-77/2)2^(sig sqrt n).               (8.2)

HQ+2<=DRAW so h<2DRAW. Every P value/row tag, all row/word/binding padding, epochs/backup/flags/scratch,
NEXT/head/virgin bit, live/free/unvisited slot and acquisition register is counted. The global address fee
is O(sqrt n); constant-many O(n)-bit staged words keep classical space O(n). The finite branch changes constants.

## 9. Explicit polynomial ledger for the SHORT physical words

Every elementary core step pays ADDR=ceil(log2(S_C+S_Q+2))=O(sqrt n), using the ENTIRE padded
prefix in (8.2). This bounds all phases including initialization, generating addresses, failed attempts and cleanup.
Staged arithmetic and every classical pointer update are paid bit operations.

Native counter lemma. For a d-bit pointer traversing L consecutive valid addresses, literal ripple-increment
flips at most2L+d bits: bit j flips at most L/2^j+1 times, and sum_j L/2^j<2L. The read/test/write of each
visited carry bit costs constant-many elementary bit operations. Charge the loop tests and RAW read/write as well.
Including pointer initialization/copy, a segment of L consecutive RAW addresses costs

 O((n+L)*sqrt n),                                                     (9.0)

because d=O(sqrt n) and setup uses at most O(n) staged bit operations. This is deterministic for ANY starting
address, values and carry pattern; it is not an expected increment cost. Multiple streams use constant-many
staged pointers. A final pointer increment may be omitted. Sequential RAW_WRITE measures a bit, applies a
conditional X and forgets the old bit, constant work per visited bit plus the explicit address fee.

Address generator. The literal row/NS/ES/BS/FS mapping of Section4 uses bit copying, zero extension and additions
on O(n)-bit staged operands. Each multiply by a public power of two is implemented as a bit shift/copy;
each addition is a ripple pass. All this costs O(n) bit operations, hence O(n^(3/2)) charged work. Segment
starts are public precomputed words, not a RAM. VS padding makes this generator different from the old
WROW+EW nonpower row-stride multiplication. Global P mod-N arithmetic is UNCHANGED and remains P steps.

Instruction prices retained from the literal generator above. A LOGICAL row-bit READ/WRITE costs
O(n^(3/2)), including a FULL first-WRITE clear of WROW values on every WRITE, conservatively. A RAW/staged
bit or mapped P gate costs at most O(n^(3/2)) including address setup. A SLOT/DESCRIPTOR or OWNER allocation
macro costs O(n^(5/2)): O(n) logical-bit accesses, constant-many RAW words/flag streams and caller updates.
One acquisition with its O(n) slot moves costs O(n^(7/2)). The different instruction types are not all priced
at the allocation macro's maximum. Every core/address/generation/carry operation pays ADDR=O(sqrt n).

Direct P steps. One P core step touches at most three classical bits or qubits. Resolving its operands may
visit O(r) ancestor environments; at each, constant-many O(n)-bit binding/frame/descriptor fields are read
through O(n) LOGICAL-bit accesses, plus linear native address formation. Its COMPLETE cost is therefore
O(r*n*n^(3/2))=O(n^3), including emission of the actual P operation. This explicitly allows nonlocal walks;
no constant-time environment access is claimed. In the cached local case the cost is smaller. The semantic
compiler never treats a word arithmetic/comparison expression as one such bit step; P's full bit expansion
and generation are already in C_P and in these instruction prices.

Structural control events. The complete source's context counting gives
 E<=C*r*(C_P+Qcap+poly(n)) calls/returns/loop entries/updates/tests/branches outside core operations.
Each opened iteration/call contains an inner P step or source event. Charge its constant-many structural
transitions to its first such event; at most O(r) simultaneously containing contexts receive a charge.
Empty tests and final propagation of FAIL/ABORT are covered by the fixed statement count of the enclosing
context, or by the polynomial initialization/terminal term. This is the SAME conservative depth charge;
it does not assume each ancestor of a failed child has its own successful merge.

A structural event may itself resolve nonlocal operands by visiting O(r) frames. At each frame,
constant-many O(n)-bit fields take O(n) logical-bit accesses; RAW record streams and possible constant-many
OWNER macros are charged too. Thus charge O(r*n*n^(3/2))=O(n^3) for EVERY structural event, including
all nonlocal walks, copies, tests, push/pop and caller-result binding. Combined with E=O(r(C_P+Qcap))+poly(n),
this is O(n^(7/2)(C_P+Qcap))+poly(n). No assumption that nonlocal work can be transferred to another
operation's account is required. The cached parent/return restoration is cheaper, but this uniform bound
permits full ancestor walks for every event. Significant RAW frame fields are overwritten before use;
all frame padding is counted and never interpreted.

Wire events. KEEP the source's first bound (4.3), O(n(C_P+Qcap)) events, each O(n^(5/2)), totaling
O(n^(7/2)(C_P+Qcap)). No unproved reduction of allocations to C_P is assumed. Acquisition instructions cost
O(n^(7/2)Qcap), separately counted. These safe wire-event terms share the n^(7/2)(C_P+Qcap) envelope with the fully charged structural controller; direct core work O(n^3 C_P) is smaller.

Prefix and maintenance. Initialize EVERY padded RAW/bank/control/slot wire and reset/dispose it after output:
O(sqrt n DRAW). Parameter, segment-offset and static dispatch generation take poly(n), with O(n) staging;
all later generated bit/gate operations are charged above. Exact renumbering pauses the dispatcher and
preserves its RAW continuation/cache as well as decoded P values. With outside owner count bounded by a
polynomial times exp(e sqrt n), total renumbering remains <=poly(n)exp((e+sig-1)sqrt n), strictly smaller
than the main phase. FRAME PUSH never calls ALLOC_OWNER. All bounds use deterministic caps on EVERY branch.

Consequently

 T<=C[n^(7/2)(C_P+Qcap)+sqrt n DRAW+poly(n)]+T_renumber.                 (9.1)

This is an actual new continuation/cache representation with its complete counted prefix and dispatcher;
it permits ancestor walks and retains the inherited conservative wire-event count. Improved instruction-
specific accounting does not assert that a predecessor's declared envelope was a lower bound on its runtime.
No main-step polynomial is absorbed using an exponential slack. The finite exhaustive branch is unchanged.

## 10. Time and samples

T. Use the stronger core-step statement (P6), not the already address-charged T_P:

    C_P = O(n^(7/2) C_0 + n^4 2^(H+dl)) + poly(n).

The same source proves C_0=O(n^(5/2) PP), log2 PP<=e r+3, H+dl<=e r+2,
and r<=sqrt n+1. Therefore C_P=O(n^6 2^(e sqrt n))+poly(n).
Substitution in (9.1) gives

    T = O(n^(19/2) 2^(e sqrt n)), e=13717412056659/4842323968000.

The n^(7/2) C_P term is charged explicitly and gives degree19/2. The source term n^(7/2) Qcap has degree
7 at the SAME coefficient e. Prefix/setup/storage terms have coefficient sig<e, so are smaller;
these are distinct setup phases, not a device for hiding the main P-step polynomial in an exponential gap.
All P quantum gates/instruments and source counts are unchanged; the inherited continuation improvement is the shorter physical word and its actual instruction/whole-prefix costs. CURRENT LOG7 additionally strengthens the upper-bound exponent for this SAME continuation program by the exact8.5/F6 inequality; no current physical source-count reduction is claimed.

The coefficient e is exact. Set h=2716467/1024000=2(3/5)(9/50)+(11499/4096)(217/250).
P(8.5) proves log2 7<11499/4096 by finite rational logarithm-series bounds. Full rounded schedule gives
H<=h*r+6,dl<=(9/50)r-1. Since (e-h-9/50)r>=6 for r >= 2^25, H+dl<=e*r-1<=e*r+2.
On the pool side log2 PP<=HI(9/50)r+h*r+6<=e*r, because e-HI(9/50)-h=3/16777216.
Thus all rounding constants are paid at the ACTUAL threshold, and r<=sqrt n+1 gives the claimed envelopes.

With r <= sqrt n + 1 these give
2^(e r) <= 2^e 2^(e sqrt n). Initialization, every failed or recycled branch, every abort, all bank, descriptor and
slot work, the source moves and the output-first cleanup are included.

Q. IFC-BANK-D-CT makes exactly one acquisition for each request of P and none other (Section 7). On the main branch,
Qcap = 4 n C_0 + K counts every rejected copy, every pool-stage, supplier and pool abort, and every discarded merge
input of every batch (P Section 13). By (P6), C_0 <= 8 (ell + 1) RHO^ell C_ell <= 3 * 2^29 r^5 PP = O(n^(5/2) 2^(e sqrt n)),
so

    Q = Q_P <= Qcap = O(n^(7/2) 2^((13717412056659/4842323968000) sqrt n)).

The finite branch uses at most N(n+10) copies, a constant over its finitely many N. Bank zeros, tags, slot
bookkeeping, SWAPs and renumbering are charged as work and storage, never as copies.

## 11. Growth indices

For fixed c > 0 and fixed real a, log(n^a 2^(c sqrt n)) = c sqrt n + a log n. Then
log log max(4, n^a 2^(c sqrt n)) = (1/2) log n + log c + o(1), and the index g = 1/2 exactly. This holds for each of
the declared envelopes of T (a = 19/2, c = 13717412056659/4842323968000), S_Q (a = -77/2, c = 9/50) and Q (a = 7/2, c = 13717412056659/4842323968000).
For S_C = O(n),
log log max(4, n) = log log n, so g = 0. The indices are those of the proved upper envelopes; no lower bound is
claimed. The structured objects in submission.json are exactly these four envelopes.

## 12. Error tolerance

The fifth claim is epsilon(n) = 0, under the model in which every acquired copy is an independent ideal coset state.
Everything above is proved under this model. No positive tolerance for malformed copies is claimed, and zero does not
assert that robustness is impossible. Under a different, adaptive malformed-supplier model the extra bank
measurements could matter; no such transfer is claimed.

## 13. Scope and limitations

The current joint bounds are T=O(n^(19/2) 2^((13717412056659/4842323968000)sqrt n)), S_C=O(n),
S_Q=O(n^(-77/2) 2^((9/50)sqrt n)), Q=O(n^(7/2)2^((13717412056659/4842323968000)sqrt n)), clean tolerance 0.
Time still has growth index 1/2; no index-1/3 result or positive corruption tolerance is claimed.
The complete schedule, capped pools, FW, MERGE4I/MERGE7 and logical correctness come from the fully supplied
source and its credited authors. Current work changes the ACTUAL per-bit tags to per-row tags with explicit first-write clearing, uses EW=ceil(sqrt n), and shrinks capacities, separates dedicated RAW slot metadata, pads physical strides and executes the literal shift/add/streaming-pointer generator with eight-word owner bindings plus a counted RAW continuation dispatcher/current-frame cache; it proves their fit, row-bank,
renumbering, all-branch amortized maintenance cost and simultaneous resource ledger. All three virtual*.md files concern P in its
original storage model and are unchanged. Their historical credits are retained. Earlier verdicts are not premises.

One distinction in the CQ transfer matters. Section 7 proves equality of the decoded logical P instrument
for arbitrary references and ALL P outcomes. RAW bit reads, tag-loop timing and physical bookkeeping add a finer
implementation transcript. We do NOT adjoin those extra records to P's sigma-fields Hp or G, nor claim its
conditional high-label independence under arbitrary enlargement. Apply P's failure/yield/merge lemmas to the
unchanged decoded LOGICAL law with exactly the logical histories specified in virtual2.md and virtual3.md.
The finer deterministic implementation transcript changes no logical operation, distribution or unconditioned
success probability. This is sufficient for joint all-branch resources and the clean input guarantee.
