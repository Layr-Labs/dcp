# Local gate operands and counted physical resolution

The emitter forms structural owner/index operands instead of materializing
full virtual wire handles that the physical bank would immediately decode.
GROUP snapshots preserve the FW input references. All full physical slot
fields, address arithmetic and gate fees remain charged by the bank helper
ledger. The independent structural count C_S is dominated by retained round
sorting and has no old log-squared factor. Joint time improves to
n^(269/18)(log2 n)^2 2^((7/6)sqrt n), with all other envelopes unchanged.

# IFC-LOCAL-EMIT: implicit-fiber four-input merges above a capped recycling pool, with O(n) classical workspace through a counted basis bank

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N), e = 7/6 and sig = 1. The single physical
algorithm IFC-LOCAL-EMIT below receives N in binary and fresh independent copies of rho_s, and outputs the entire s with
unconditional probability at least 1 - 2^-8. On EVERY execution branch (wrong extracted labels, FW-stage (PREP
included), supplier and pool aborts, failed and retried merges and four-input merges, discarded copies, tag
renumbering, initialization and final cleanup included) it satisfies jointly

    T = O(n^(269/18)(log2 n)^2 2^(e sqrt n)),   S_C = O(n),   S_Q = O(n^(-77/2) 2^(sig sqrt n)),   Q = O(n^(161/18) 2^(e sqrt n)).

The S_Q bound retains the proved negative polynomial factor n^(-77/2) from the 40-ceiling-logarithm trim and the counted square-root-tag prefix (Section 8). All constants are absolute. Logarithmic envelopes are evaluated for n>=2; n=1 is handled by the constant-cost finite branch. The growth indices are 1/2, 0, 1/2
and 1/2 (Section 11). The fifth claim is the clean-input tolerance 0 (Section 12).

IFC-LOCAL-EMIT executes a fixed reference algorithm P specified in the updated virtual files without changing any of its quantum operations, measurements,
source requests or classical decisions. P is IFC-LIMIT-E, whose complete specification and proof are given after the
marker line of virtual.md, in virtual2.md and in distance_decoder.md (Sections 10-13) (P Sections 7.3, 8, A and B). "P Section x" and "P (x.y)" refer to that
text; "Section x" refers to this file. The resource statements inside virtual.md concern P in its own storage model,
in which classical records are ordinary bits; they are not claims of this file. IFC-LOCAL-EMIT compiles transient gate-address generation structurally and changes data storage:
- every classical record of P, except constant many O(n)-bit staged words, is kept in basis-state qubits, which are
  counted in S_Q and are read and written only at classically known addresses (Sections 3-6);
- P's qubits live in a fixed counted array of quantum slots, managed by an indexed free list (Section 4).

Notation for P: r, r0, Lg, ell, dl, H, a, JI, Lam, cb, kappa, K, C_ell, D_i, Yd_i, Rc_i, C_0, Y and Qcap are as in P
Sections 0, 7.3, 8, 11 and 13; w = 2^ceil(log2 n), q = w/2, RHO = 2+8/r and c_F are as in P Sections 7 and 8; and
PP = RHO^ell 2^H (P Section14). C_S counts structural bit/gate/reset
instructions and local emitter bit work before physical slot resolution.
It is distinct from the standalone full-handle C_P of P Section14. The
compiler below removes materialization of transient virtual wire-address
words, not any physical addressing fee. Sections2(P7),7 specify its
operation correspondence and independent count. All logarithms are base2;
all constants are absolute.

Direct source. This physical algorithm retains the square-root-tag bank of the preceding IFC-SQRT-TAGS candidate, derived from the linear-tag bank of submission 258c03db-5e6e-40a8-bb8c-8855bece70ea. Its reference algorithm and the whole retained
construction come from kaankolcu's cf129cf6-61e5-46ad-b3c7-6407246166c2, evaluated
commit 28f1a773adce9dd8b49c8f39b590a53947189b21. The retained logarithmic schedule is ell=dl=H0=ceil(7r/12+(67/9)ceil(log2 r)+64). This variant additionally grows w with n, proves RHO=2+8/r and charges its uniform circuit. Its complete specification and resource proof are reproduced here.
The original source's fixed ratios and numerical snapshot are replaced rather
than used as premises. Historical first-person attribution below belongs to
the original authors. No prior verdict is a mathematical premise.

## 1. Provenance: the storage construction is mpjunior92's

The construction of Sections 3-7 and the original explicit-degree ledger are mpjunior92's. The current growing-group adjustments and revised polynomial ledger are identified above.
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

We restate the construction completely, so that this file and virtual.md are self-contained. The fixed-span construction is credited to those authors; this variant checks smaller polynomial capacity powers explicitly below. Tags and free lists are standard programming techniques. No
earlier verdict on any submission is a premise here.

Ours are:
- the reference algorithm P (IFC-LIMIT-E, specified and proved in full in virtual.md and virtual2.md and not filed on
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
the same banked storage. The original reference was the even-size case at w=2^28; its authors derived it independently. Its realization,
proof and schedule are our own.
mpjunior92's later rows PARTADAPT-193-TAGBANK (cfb1e549-2935-4d3f-a8b2-a01b125134ea, status failed in the
pipeline when checked) and PARTROOT196 (3315027c-4ec3-4352-80e5-f8f384e286f1, validating when checked) let the odd
group size grow with n and claim coefficients just above 2/sqrt 3; they are prior board work on the growing-size
case. We claim no priority over any of these rows.

Base text. This file is the text of our F-LIMIT-BANK (a9a7dcac-3918-44e8-84db-bda6b1dcebdd), itself the text of our
TRIAD-BANK (9a129f0f-e377-466d-b45d-449843d2167e) and unfiled G4-BANK with P replaced. Sections 3-7, 9 and 12 differ from it
only in the algorithm's name, the row bound U (Section 3), the register count of (P4) and the recursion depth.
Sections 0, 1, 2, 8, 10, 11 and 13 carry IFC-LIMIT-E's facts, parameters and exponents. No step relies on any of these
rows' verdicts.

## 2. The reference algorithm P and the facts used from it

Finite branch (n < 2^40). P is the exhaustive tester of P Section 13: for cand = 0, ..., N-1 use n+10 fresh copies,
apply Shift_cand, measure the control in X, and reject cand at the first minus; output the first unrejected cand, or
0. IFC-LOCAL-EMIT runs it with ordinary storage. It holds cand, a copy counter and the current copy, so O(n) bits and
O(n) qubits, and it makes the same acquisitions. There are finitely many such N, so this branch changes only
absolute constants.

Main branch (n >= 2^40). P computes b0=floor(ell/2)-4 and exactly the integers of P Section 0 (r, r0, Lg, kappa, ell, dl, H0, cb, Lam,
a, JI, H) and of P Sections 7.3 and 8 (K, C_ell, D_i, Yd_i, Rc_i, C_0 = Rc_0 D_0, Y, pbmax_i and the tree capacities),
puts Qcap = 20 r C_0 + K, and runs P Sections 5-13: label extraction LE; the chunked FW stage (FWLEVEL runs of q(Y+1)
rounds on chunks of D_i, with buffers and run caps); the tree shape and bit allocation of P Section 8 for each
requested B; BATCH with its tree of binary MERGEs and four-input MERGE4Is; the free-frequency block decoder; and the 2-adic block part. Every ABORT outputs 0.

Completion of unspecified orders. P leaves three orders open:
- equal-key ties in its merge sorts;
- the order of LIVE after an FWLEVEL round;
- the order of OUTPUT.

IFC-LOCAL-EMIT fixes them as follows:
- sorts are stable, with ties in current list order;
- after a round, LIVE lists, in scan order, the qubits a group returns to LIVE at the position of that group (for a
  pair cell its w - 2 returned qubits, in group order; for a matching cell or Ev its recycled qubit) and the
  ungrouped qubits at their own positions;
- OUTPUT is in order of production, and buffers are in order of appending, so "the first D_(i+1)" of P Section 7.3
  is defined; MERGE4I's sorts are stable and its streams and heaps break ties by position, as P Section A fixes.

These orders are functions of P's classical history only, never of slot numbers or bank addresses. Every lemma of P
that meets these orders holds for any order that is a function of the past:
- P Lemma 7.2 holds "For ANY labels, and conditional on everything before the level", so P Lemma 7.3 holds for
  every run, and the live count
  S_end <= (w - 1)E of P Section 7.2 holds "whatever the labels and outcomes";
- the sigma-field G of P Lemma 10.1 contains all decisions of the controller;
- P Lemmas 6.1, A.1, 9.2 and 11.1 are conditional on the past, and P Lemmas B.1 and 9.1 on the controller's history
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
  merge-sort scratch and the measured code of the current cell (w rows of ceil(log2 n)+1 bits); and the final pool list. Each has
  at most 2^(cb+1) rows: |Bf_i| < D_(i+1) + D_i/2 (P Lemma 7.3(c)), Cin = D_i <= 2^cb, LIVE never grows, and OUTPUT
  has at most Cin/2 rows since each FW appends gamma <= rho/2 good outputs while it removes rho qubits from LIVE
  (P (7.3)); C_ell <= 2^cb (P (F4)).
- In the tree: at most four retained tables per level, each of at most 2^Lam rows. For the one active MERGE: the
  arrays aa, bb, order, pos, lo, cnt, off, Dx and the block inverse v -> (x_v, y_v), each of at most 2^Lam rows. For
  the one active MERGE4I: the residue and sort-order arrays, runs, the two heaps, Buf, Tl and the block table, each
  of at most max(2^Lam, Cp) <= 2^cb rows (P Section A; Cp <= 2^cb by P Section 8).
- The decoder's K records (Z_i, beta_i, W_i) and K residues (P Section 11).
- LE's 2(J_e + 1) test counters and directions (P Section 5).
- The profiles over i of D_i, Yd_i, Rc_i, run counters, pbmax_i, pb_i, pp_i (ell + 1 rows) and over tree levels of
  their exponents, capacities, bits and positions (a + JI + 1 rows) (P Section 8), and the 4096-row table of P
  Section 4.
- O(1) scalars per loop level and per frame of the depth-first recursions (the tree, depth a + JI + 1, and the
  requests of P Section 7.3, depth ell + 1).

Each row of these arrays has at most 12n bits. Lists store a handle to their qubit; P calls it the "wire index", and
here it is a slot number (Section 4).

(P4) Qubits. At any time P holds at most:
- 4 r 2^cb pool qubits (P Lemma 7.3(c) and Section 14);
- at most K<=n retained root qubits, plus 4(a+JI+1)Lam<=16n qubits of stacked index registers (P Section 14; a + JI + 1 <= r, Lam <= r);
- a fixed set of scratch registers: the current copy (n+1 qubits); the transform, modular-addition and LE scratch of
  P Sections 3 and 5; the merge registers Ru, Rv, Rz, Rp, Rd, R and their Toffoli-chain scratch (P Section 6); the
  MERGE4I registers (the residue, sum and window registers of steps 1 and 3, R and Rf, and their Toffoli-chain
  scratch, fewer than 32 registers of O(sqrt n) qubits, P Section A); the FW registers T, R and P, the PREP try
  qubits and the Boolean-evaluation scratch, at most c_F=2^20 n^3 qubits in all (P Section 7.1); and one
  coin qubit (P Section 11).

These are explicit ripple and Toffoli-chain circuits. Apart from FW's registers, (P4) lists fewer than 1024 registers,
each of at most 4n qubits, so the scratch totals at most c0 n + c_F qubits with c0 <= 2^12 and c_F=2^20 n^3.

(P5) Lifecycle. Every P qubit is created in one of two ways:
- by an acquisition, as part of an (n+1)-qubit copy;
- by allocation in |0>, as scratch of a transform, a modular addition, an LE test, a LOOKUP, a MERGE, a MERGE4I, an FW, a PREP
  try or a coin. Each such operation allocates at most c0 n qubits (at most c_F for an FW apart from its PREP tries, and at
  most ceil(log2 n)+1 for a PREP try) and contains at least one P step.

Every P qubit ends by being measured and released, or reset and released, or released in a known basis state. In
four places P leaves the release implicit: the unused final-pool qubits after the K roots (P Section 9), the buffered
qubits after the final pool is formed (P Section 7.3; measured, reset and released), the wd = 1
leaf qubits with kk != 1 (P Section 12), and R after a step-4 FAIL of MERGE (P Section 6.2). IFC-LOCAL-EMIT completes P
there, and wherever else a release is implicit, by one rule: a qubit that P never touches again is reset and released
at that point (a trace-out, so the result is still an instance of P). In detail:
- LE resets the data register of a copy. A rejected copy is released. An accepted copy's control becomes a pool qubit
  (P Sections 5, 11 and 12).
- An FW on pool qubits A_0, ..., A_(w-1) (P Section 7.1) first runs PREP: each try allocates j_N+1 <= ceil(log2 n)+1 fresh
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
  P Lemma 7.1(c) states that step 5 leaves every released qubit in |0> on every input. The explicit Boolean circuit, rather than its looser capacity c_F, uses O(n^2(log n)^2)
  scratch qubits and wire events outside PREP; each PREP try makes O(log n). Thus an FW
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
- A root is measured and released, and unused roots are released (P Sections 11 and 12). At an ABORT or at the end
  every remaining qubit is released.

P includes the explicit reset completion of Section2 of virtual.md. Each
fresh zero-ancilla allocation is paired with its own semantic reset, and
each logical release is paired with a semantic reset, both counted in C_S. Source-copy
allocations contribute at most (n+1)Q_P separately. The added resets and local emission fit the structural bounds of (P7);
P Section14 also proves the looser standalone full-handle bound. Their channels preserve the reference law and peak caps.
FREE_Q may reset an already reset slot; its constant additional work remains
charged as an event, and records no new outcome.

(P6) Cost. The structural compiler in (P7), with P Sections7 and14, gives:
- C_S=O(n^(7/2) C_0+n^4 2^(H+dl))+poly(n);
- Q_P <= Qcap (P Section 13);
- C_0 <= 64 RHO^ell C_ell (P Lemma 7.3(d)) and C_ell<=3*2^21 r^2 2^H (P (F4));
- PP and 2^(H+dl) are O(n^alpha 2^(e sqrt n)), where alpha = 67/9 (P Section 14);
- cb <= sig sqrt n - 40 log n and Lam + kappa + 4 = cb (P (F1) and Section 0).

(P7) Structural compiler. A gate operand is an owner id, a local register
row/bit index and a fixed operation tag. The current-frame program emits
this tuple, and the bank resolver of Sections4,9 reads the full slot field
and computes the complete physical address. The tuple is classical, never
superposed. OWN is polynomial, so owner ids have O(log n) meaningful bits.
FW and LE quantum-register widths and actual scratch sizes are polynomial,
so their local indices also have O(log n) bits. RR offsets use the exact
prefix sum from Section3.

At FW entry form one GROUP array of w rows, copying each selected input's
slot field and two label fields. This costs O(nw)=O(n^2) structural bit
work. A gate on A_i resolves GROUP row i; it does not first copy a full
virtual reference handle into a temporary argument word. Scratch gates use
their scratch owner and local wire index. GROUP is freed at FW end; it adds
one fixed owner per active FW, included in Section3, with at most w<V rows
of at most 7n bits (two 3n-bit labels and one slot field). No pool-sized quantum address is passed to an emitter.

The local nested-loop ripple/scan emitter uses O((log n)^2) bit work per
Boolean gate. Thus FW's O(n^2(log n)^2) Boolean gates, resets, initialization
and uncomputation cost O(n^2(log n)^4) structural work. PREP costs
O(wr(log n)^3), and label/postprocessing/snapshot work fits the same bound.
Every physical slot read, address arithmetic operation and gate fee is
still paid in Sections9–10; it is not charged here and then omitted there.

LE and transforms emit local register indices similarly. Their skeleton
has O(n^2 h_e)=O(n^(5/2)) operations and local emission costs at most
O((log n)^2) each, giving O(n^(5/2)(log n)^2) per acquired copy. Full data
labels and all reference arithmetic retain their original widths. In
particular this compiler does not replace a data-table index by O(log n)
bits: classical rows can still have O(sqrt n)-bit indices, and the complete
physical resolver handles them under the instruction bound below.

Round sorting is retained unchanged. Its structural work remains
O(n^(5/2)Cin) per FWLEVEL (P Section7.2): sum of live lengths over rounds is
O(nCin), with O(n log Cin) work per row and log Cin=O(sqrt n). FW work is
O(n^2(log n)^4 Cin), below a constant times that sorting bound. Indeed
(log2 n)^4/sqrt n decreases for ln n>8 and at n=2^40 equals
40^4/2^20<3. Likewise (log n)^2/sqrt n<1 on the main branch.
Summing ell=O(sqrt n) levels and O(sqrt n) batches gives FW structural
work O(n^(7/2)C_0). LE work across all batches is
O(n^3(log n)^2 C_0), below it. Keep the old conservative tree bound
O(n^4 2^(H+dl)) and decoder bound O(n^3C_0). These dominate their
structural emission as well. Therefore (P6) holds without the old log^2
factor. Reset completion emits local indices and fits the same budgets.

This is a compilation of the same semantic program: emitted gates,
measurements, reset operations, classical data updates, branches and source
requests have the same order and operands as P. Only transient numeric
virtual-handle bit strings are replaced by structural references. Section7
compares semantic states rather than asserting equality of those omitted
compiler intermediates. No full physical pointer or uniform generation
work has been made free.

P's standalone envelopes concern its storage model and full-handle generator.
This file uses the independent structural bound (P7), with complete physical
resolution charged separately in Section9.

The pool primitive. The HPC-127 version of this construction differs from the present one only in P's pool primitive
(PAIR there, FW here, G4 in G4-BANK, TRIAD in TRIAD-BANK), in the schedule constants, and here in the chunked pool and the
four-input merge, which add only registers, arrays and lifecycles of the kinds listed in (P3)-(P5). The construction uses the
pool primitive
only through (P4) and (P5): a bounded number of wire events per primitive, kept qubits transferred by handle, and
released qubits reset. By P Lemma 7.1(c), which holds for every input state, FW satisfies both. The number of inputs
an FW releases (between 1 and w - 1) is fixed by its recorded cell; the construction uses only the bound w - 1 on it,
since each release is one FREE_Q of a qubit that P releases. Sections 3-10 use P's yield lemmas
(P Lemmas 7.2, 7.3 and 9.2) only through (P1), and P's schedule only through (P2), (P3) and (P6).

## 3. Fixed capacities of the bank

Put V=2^(cb+2), U=rV and

    OWN=2^24 r owners, WROW=2^16 n bit cells per row, ROWS=2^24 V rows per owner,
    HQ=2^20 U quantum slots.

An owner holds one logical array. The logical bit (o, i, j), with o < OWN, i < ROWS and j < WROW, has the address

    c = o ROWS WROW + i WROW + j  <  LSPAN=OWN ROWS WROW=2^64 r n V=2^64 n U.               (3.1)

Fit. Every reference data array has at most 2^(cb+1)<V rows, below
ROWS=2^24V. Every data row has at most 12n bits, below WROW=2^16n.
Slot indices fit n bits since log2 HQ<=sqrt n+23<n. Persistent allocator
metadata has its own counted RAW region below, so it need not fit a data
owner. The stronger elementary inequality cb>=19+6log2 r follows from
cb>=r-80log2 r-42 and r>=86log2 r+61 for r>=2^20; the latter holds at
the endpoint and then by differentiation. Hence V>=2^21 r^6 covers
c_F=2^20n^3, its descriptor rows and all other polynomial scratch. The
RR views and decoder records also fit V. No owner or slot cap shrinks.

The only growing family of separate scratch-register descriptors is R_m,
3<=m<w, from FW. This implementation gives these registers disjoint views of
one RR descriptor array, not separate owners. Put j_m=ceil(log2 m) and
S(m)=sum_(v=3)^(m-1) j_v. Descriptor bit j of R_m uses RR row S(m)+j.
The intervals are disjoint because S(m+1)=S(m)+j_m, and their total length
S(w)<=w log2 w<=V. RR has one owner per active FW. The PREP flag/try scratch,
cell/ticket registers and Boolean scratch use fixed other descriptor arrays.

Compute S(m) exactly by summing, for k=2,...,log2 w, k times the size of
[3,m-1] intersected with [2^(k-1)+1,2^k]. There are O(log n) terms on
O(log n)-bit integers, costing O((log n)^3) bit operations. No O(w) owner map
or advice table is stored. Every m,j is a classically specified circuit-wire
operand. Quantum-dependent selections in cell/back remain the full Boolean
scan circuit; this view map adds no quantum-addressed access.

At FW entry activate RR, so all its views are logically zero. Each ALLOC_Q
result is written in the corresponding view row before use. A failed PREP try
resets/releases its qubits and clears those pointer fields; all earlier prepared
R_m views remain untouched. On successful FW cleanup each R_m is reset/released
and its view rows cleared. Free RR only after all its views are dead. Thus a
retry has fresh descriptor fields, and all simultaneous qubits have the same
injective slot map as before. Renumbering an active RR owner preserves all its
view values together. No separate epoch per view is required.

After packing this family, at most 514(a+JI+ell+4)+1168 owners are needed for
the nested computation and fixed scratch. Even allowing 64K additional owners
for retained root records and tables, the total is below
2048r+10000+64K <=2048r+10000+3*2^19r <2^24r=OWN.
This conservative allowance does not require streaming root measurements.
Since K<=n, the live-qubit bound may include 17n instead of 16n; still
4r2^cb+17n+c0n+c_F<=3U<HQ. Every capacity and availability invariant therefore
holds on all branches. The owner coefficients are deliberately fixed, not advice.

Views change only implementation descriptors. The decoded logical P records
are unchanged, and a gate on R_m[j] is sent to the slot read from RR[S(m)+j].
Clearing a released view adds O(1) field updates per released qubit. The
O((log n)^3) offset work and O(n) binding reads per operand fit the controller
completion bound in Section 9. All ordinary temporaries remain constant many
O(n)-bit words; the depth-dependent frames remain bank records.

## 4. Physical layout, and the quantum slot allocator

Each epoch has EW=4r bits. This variant has ONE tag per row, not per bit.
Put LROWS=OWN*ROWS=2^48 r V and LSPAN=LROWS*WROW=2^64 n U.
For logical row R=o ROWS+i, its RAW base is B(R)=(WROW+EW)R.
Value bit j is at B(R)+j, and tag bit t is at B(R)+WROW+t.
The RAW span is

    DRAW=LROWS(WROW+EW)+n(HQ+2)+(OWN+8)EW+OWN+2^20n^4.                (4.1)

Immediately after the row blocks is a persistent RAW region of n(HQ+2) bits.
It stores n-bit head, virgin and NEXT[k] at word offsets 0,1,k+2. Then
come ep(o), G, backup and six spare epoch words, OWN active flags and
2^20n^4 interpreter/binding scratch bits. These ranges are disjoint.
No RAW record is lazily tagged. Row values and row tags occupy separate
positions within their block, and different row blocks are disjoint.

These ranges are disjoint and end below DRAW. RAW records carry no tags.

Physical wires:
- RAW index j is wire 2j;
- quantum slot k < HQ is wire 2k + 3;
- wire 1 is spare.

Let h be the least power of two with h >= max(DRAW, HQ + 2). On the main branch IFC-LOCAL-EMIT first computes the
parameters with O(n) staging (Section 8). It then allocates wires 0, ..., 2h-1 in |0> once, and releases them once at
the very end, after the output is written. In between it allocates only an (n+1)-qubit acquisition register, one at
a time. Hence on every main branch

    S_Q <= 2h + n + 1.                                                                    (4.2)

Bank wires are acted on only by computational-basis measurements and by X gates conditioned on classical bits.

Slot allocator. Persistent head, virgin and NEXT live directly in the RAW
metadata region, which is initialized with the complete prefix. READMETA(k)
and WRITEMETA(k,v) stream all n RAW bits at the known word offset; no tag
comparison or unit-cost word operation is assumed. NEXT[k] uses offset k+2.
The region is never freed, recycled or renumbered. Slot descriptors retain
READWORD/WRITEWORD in the tagged data rows. Every P quantum register is a
pool qubit, a register with its descriptor array, or an R_m view of RR;
its descriptor rows hold one slot number per qubit. Lists carry slot numbers
where P carries wire indices. head = HQ means empty.
- ALLOC_Q: if head != HQ, put k := head and head := NEXT[k]; otherwise put k := virgin and virgin := virgin + 1.
  Return k.
- FREE_Q(k): reset wire 2k+3 (the reset core step, which records no outcome); then NEXT[k] := head and head := k.

Initially head := HQ and virgin := 0. NEXT[k] is read only after FREE_Q(k) has written it. No operation scans the
slots. Every head, NEXT and virgin access is a known-address READMETA/WRITEMETA
operation, costing O(n^2 log n) with the RAW fees below.

Invariant (I). The slots below virgin are partitioned into two sets:
- slots holding live P qubits, one slot per qubit, mapped injectively by the descriptors;
- slots on the free stack, which has no repetitions and whose slots are in |0>, in tensor product with everything.

Slots at or above virgin are untouched |0>. ALLOC_Q removes a free or untouched slot from those sets and gives it to
exactly one new P qubit. FREE_Q is called only when P releases that qubit, never when a handle is merely passed or
copied, and it returns the slot to |0>. A P qubit keeps its slot from allocation until release, and passing a
register passes its descriptor, never a copy of its qubits. So (I) is preserved. Gates read their operands' slot
numbers from the descriptors and act on the corresponding odd wires.

The pool is never full. By (P4), with the completion rule of (P5), at most 4r2^cb+17n+c0n+c_F slots are live
at once. Since c0 <= 2^12 and c_F=2^20n^3 <= 2^cb (cb >= r/2 by P (F1)),

    live<=4r2^cb+17n+2^12n+2^20n^3<=3U<HQ,   because HQ=2^20 U=2^22 r2^cb.

If virgin = HQ and the free stack were empty, all HQ slots would be live, a contradiction. So ALLOC_Q always
succeeds, and no abort or guard is added.

Wire events. Call every ALLOC_Q, FREE_Q and descriptor-row update a wire event. By (P5):
- allocations number at most C_S+(n+1)Q_P, since each non-source
  allocation has its own explicit counted initialization reset;
- releases number at most C_S plus source bookkeeping, since every logical
  release has its own counted reset; the allocation bound is also sufficient;
- each allocation or release updates at most c1 descriptor rows;
- moving a qubit between lists costs nothing extra: its slot number is a field of the list row, and P copies that row
  itself, in semantic data steps already counted in C_S;
- only LEAF, MERGE step 6 and MERGE4I step 8 move slot numbers into descriptor rows, at most c1 rows per moved qubit. LEAF moves dl
  qubits and builds 2^dl table rows, and MERGE step 6 and MERGE4I step 8 each move lam' qubits and write 2^lam' table rows, so each such
  move is charged to at least 2^dl or 2^lam' table rows, hence to at least one P step per moved qubit.

Hence a branch has at most

    c (C_S + n Qcap)                                   (4.3)

wire events. The HQ slots are prepared once and cleared once, and are never scanned for an allocation, a gate, a
root, a request or a batch.

## 5. Bank operations

RAW_READ(j) measures wire 2j in the computational basis into one staged bit. RAW_WRITE(j, v) does RAW_READ(j) into a
staged bit z, applies X to wire 2j if z != v, and forgets z. The address j is always a classically known staged word;
no gate is ever controlled by a superposed address.

Epoch words ep(o), G and the backup are EW-bit RAW words. They are compared, copied and incremented bit-serially, with
one staged carry or equality bit and an O(log n)-bit bit counter. An epoch value is never held as an ordinary word.

- READ(o,i,j): compare the row tag with ep(o), bit by bit. If equal, return
  its value bit; otherwise return zero.
- WRITE(o,i,j,v): compare the row tag with ep(o). If unequal, clear all WROW
  value bits of this row to zero and copy ep(o) to its row tag. Then RAW_WRITE
  value bit j to v. A matching-tag write does not clear other values.
- READWORD(o,i,j,l), l<=n, j+l<=WROW: compare the tag once, then stream the
  l value bits into a staged word; return l zeros if the tag is invalid.
- WRITEWORD(o,i,j,l,v): validate/initialize the row exactly as WRITE, then
  stream the l bits of v into that field. It is not a unit-cost word operation.
  Slot descriptor fields use these routines; persistent allocator metadata
  uses the direct RAW helpers of Section4.
- ALLOC_OWNER scans for an inactive owner, runs Section6 if G is full, increments
  G, copies it to ep(o), records the binding and activates o. FREE_OWNER clears
  its active flag. Neither scans the exponential rows of an owner.

Initially all RAW bits are zero, G=0, and active epochs start at one.

Lemma 5.1 (row-lazy arrays). Every row tag is at most G, and an owner's fresh
activation has an epoch larger than its stale tags. A row with a matching tag
contains exactly its current-activation writes; all other bits are zero.
An invalid-tag row decodes entirely to zero.

Proof. New owner epochs exceed all old row tags. Until the first write to a
row, READ returns zero. The first bit/word write clears the entire row before
making its tag valid, so unwritten fields are genuinely zero. Subsequent writes
preserve the other fields. Word routines merely group consecutive bit operations
while testing the same row tag once. Section6 preserves every decoded row and
re-establishes the invariants. Induction proves fresh-zero logical-array
semantics for every bit, including RR views and partial-row writes. QED.

A first write clears only WROW=O(n) bits, not all ROWS. This work is charged in
Section9. This explicit clearing is essential: sharing a row tag without it
would expose old values in unwritten fields and would be incorrect.

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

Fixed bindings. Reserve the first 8n*OWN bits of the existing RAW interpreter
scratch for owner-indexed binding records, eight n-bit fields each: owner id,
format id, row bound, row width, view base, backing owner, scope-frame id and
flags. They fit 2^20n^4 since 8n*OWN=2^27rn<=2^28n^(3/2) on the main branch.
Format ids select a finite list of row encodings in P; numerical tuple/table
contents remain bank data. A frame holds the owner ids of its fixed array
variables in ordinary tagged rows. For a new owner ALLOC_OWNER writes only
these eight fields and the frame's corresponding word; it does not copy a
binding map or initialize unrelated records. FREE_OWNER clears its active
flag; stale binding records are ignored until their eight fields are
replaced. RR views use the backing-owner and view-base convention, with
S(m) computed online, and need no separate owner binding per R_m.
All record reads/writes stream the n bits with RAW_READ/RAW_WRITE. There
are a fixed number per operand/activation, so binding work costs O(n^2 log n),
including physical fees. The already allocated scratch span is unchanged.

Current-frame interpreter. The fixed program compiles each reference
procedure to finitely many program-counter cases. A banked frame has parent
owner id, return pc, current pc, operation tag, scalar locals and local array
owner ids, one n-bit field per row. There are fewer than 2^12 such fields
per procedure in this fixed source; array contents remain separate bank
arrays. An O(n)-bit scalar occupies its fixed number of n-bit chunks;
an n+1-bit endpoint uses two fields, and the input N remains available. Each frame is one owner, not one owner per scalar. It fits ROWS.
Nonrecursive bit/gate-generation helpers use fixed inline loops. Only the
recursive pool/tree calls require a growing chain of these frames.

The controller stages current frame id and a constant number of words.
Its loop is:
- dispatch the current frame's pc; execute that local bit/gate operation;
  update only that frame's local fields and pc;
- CALL: write the caller continuation pc, activate one child frame, write
  its parent/arguments/entry pc, and set current to the child;
- RETURN: write the fixed output ids/words into the parent, set its pc to
  the saved continuation, free the child frame and set current to parent;
- ABORT/finish: follow parent links to release the remaining frame owners,
  with the prescribed quantum cleanup charged separately.
A pc test touches only finitely many n-bit fields. No step walks all open
ancestors. Loops alter the frame containing their own loop variable. A
frame passed through the epoch fallback is preserved as any active bank
array; parent ids do not change. Source/quantum operands keep the fixed
bindings and slot descriptors of the preceding sections.

The extra one frame owner per context is included in the 514 coefficient
of Section3; the enlarged 2048r+10000 bound still fits OWN. Thus the
representation uses no ordinary recursive stack and changes no decoded
reference operation, decision, source call or output.

## 6. Exact renumbering when G is full

IFC-LOCAL-EMIT never assumes that G cannot wrap. If ALLOC_OWNER finds G all ones (a bit-serial test), P is paused, and the
following is done for o=0,...,OWN-1.
- If o is active, copy ep(o) to backup. For each row, retain its value bits if
  its tag equals backup; otherwise clear all its value bits. Set that row's
  tag to o+1. Finally set ep(o)=o+1.
- If o is inactive, clear all its value bits, row tags and epoch.
Then set G=OWN and resume the pending activation. Every active row decodes
as before; invalid rows become explicit zeros. Inactive rows are below every
future fresh epoch. OWN+2<2^EW, so generations remain available. RR view
boundaries are unchanged. P executes no operation while this is done, and its
quantum slots and persistent RAW allocator metadata are untouched. One full scan has polynomial overhead times DRAW;
O(n^3 DRAW) remains a sufficient charged bound. All finite exceptional wraps
are implemented rather than assumed away.

Renumbering is eventually absent. Owner activations are polynomial in n times
the core-step and source caps. The reference proof gives
C_S=O(n^(9/2+alpha)2^((7/6)sqrt n)) and
Qcap=O(n^(3/2+alpha)2^((7/6)sqrt n)), alpha=67/9.
Their logarithms are at most (7/6)sqrt n+O(log n). Since EW=4r>=4sqrt n,
no wrap occurs on any branch for all sufficiently large n. The fixed exact
renumbering fallback remains correct below that absolute threshold. Each
exceptional length has bounded P loops and terminating renumbering with
OWN+2<2^(4r), so the finite set changes only an absolute constant.

## 7. Correctness: the decoded classical-quantum invariant

An aligned point is a boundary between semantic data/gate operations or
acquisitions. Erase P's transient numeric emitter-address words and treat
its wire handles as logical references, retaining their identity and
aliasing. P does not branch on numerical wire addresses: they are used
only to emit the indicated gates. Let P_sem be this semantic state. Define
pi from the physical bank to P_sem:
- decode ordinary data cells, labels, scalar values and frame state;
- interpret descriptors and structural owner/index tuples as logical
  references using the injective live-slot map;
- keep semantic control position and meaningful bindings;
- trace out free slots, padding, tags, allocator fields, inactive owners
  and physical/compiler-only intermediates.
The local emitter steps stutter on this semantic state until an operation
is emitted. Resolved operands are the same logical qubits/data fields as
P's full-handle emitter. This follows directly from GROUP, RR and fixed
binding definitions; no numerical handle value is a source of randomness.

IFC-LOCAL-EMIT has no randomness of its own. Its staged decisions and every RAW_READ outcome are fixed functions of N and
of the outcomes of P's own measurements so far: by induction over steps, the basis content z of all bank wires and
staged bits is such a function, and a RAW_READ returns a bit of z. So at each aligned point the physical state is

    sum_z p_z |z><z| (x) rho_z,

where rho_z is a state of the mapped P qubits and of any reference system, possibly entangled and correlated with z,
and p_z is the probability of P's outcome history behind z. We show that pi(Phi_phys(X)) = Phi_Psem(pi(X)) for each semantic operation macro,
where Phi_Psem is P's operation after its transient emitter work and
Phi_phys includes local emission and full bank resolution. Internal local
bit-generation steps are counted in C_S even when they stutter under pi.

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

By induction from P's initial state (input N, all scratch zero), the decoded semantic state of IFC-LOCAL-EMIT equals
P_sem at every aligned point, on every branch: extraction errors, returned and recycled FW outputs, failed merges, partial
children, rejected copies and aborts included. Its source-request sequence and its output law equal P's. By (P1) it
outputs s with probability at least 1 - 2^-8 for every N and s.

The held-out-bit argument of P Section 10 and the coupling of P Section 5 are statements about P's logical law, which
pi preserves. The held-out-bit argument is applied to the decoded logical law, conditioning
only on its specified G. In particular it does not condition on a physical RAW
transcript that might include high label bits. Equality of decoded output laws,
not an assertion that such a transcript reveals no bits, transfers correctness.

## 8. Classical and quantum space

S_C. IFC-LOCAL-EMIT's ordinary classical storage consists of:
- the input N in at most n+1 bits and the output in n bits;
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

S_Q. Count data rows, row tags and the persistent RAW metadata separately.
U<=8n^(-79/2)2^sqrt n and HQ=2^20U. The value span is

    LSPAN=2^64 n U <=2^67 n^(-77/2)2^sqrt n.

Row tags add at most another value span since EW<=WROW. Persistent RAW
metadata uses n(HQ+2)=O(nU) bits and has the same negative-polynomial
power. Epochs, flags and interpreter scratch are O(n^4), absorbed using
(85/2)log2 n<=sqrt n above the main threshold. Thus
DRAW=O(n^(-77/2)2^sqrt n). Since h<2DRAW and HQ+2<=DRAW,

    S_Q<=2h+n+1=O(n^(-77/2)2^sqrt n).                 (8.2)

For example a fixed enlargement of 2^80 n^(-77/2)2^sqrt n bounds the
main prefix. It counts every unused row, tag, slot, metadata field, padding
wire and acquisition register. The finite branch changes only the absolute
asymptotic constant. The metadata region is persistent RAW data, never an
uncharged ordinary array and never quantum-addressed.
Classical staging is bounded by 2^20n bits using a fixed number of bit-serial
word registers; no recursion stack or circuit transcript is stored there.
Set A=ceil(log2(2h+(2^20+2)n+10))+1. It upper-bounds every physical address
fee and A=O(sqrt n). Address roles and RAW cursors use A-bit words; data values
retain their full O(n)-bit fields. All arithmetic is bit-serial.

## 9. Explicit polynomial ledger

Every core step of IFC-LOCAL-EMIT pays its address fee ADDR = ceil(log(S_C + S_Q + 2)), and ADDR <= n by (8.2). An
instruction is one of the following:
(i) a logical READ or WRITE;
(ii) a RAW_READ or RAW_WRITE;
(iii) a bit operation on staged words;
(iv) one gate, measurement or reset of P on mapped slots;
(v) an ALLOC_Q or FREE_Q, or a descriptor field update;
(vi) an ALLOC_OWNER or FREE_OWNER;
(vii) one acquisition, with its SWAP.

(L1) Current-frame control completion uses O(n log2 n) instructions per
structural step, plus the same allowance per call/return. Fetching n-bit
bindings takes O(n) instructions; O(A^2) index arithmetic with logarithmic
emission and O((log n)^3) RR offsets fit O(n log n). A dispatch accesses
only the current frame, with a fixed number of local fields. CALL/RETURN
also touch only fixed fields and one new/old frame owner. These operations
use the bit/word/owner helpers of (L2); no ancestor scan is required.

The number of frame events is O(C_S+Qcap+poly(n)), independently of depth.
Tree calls are charged to their own LEAF table write or merge attempt;
child calls per merge have arity at most four. Completed REQUEST calls each
remove at least one output row from their own buffer, a distinct counted
reference operation, even when they make no FW call. A batch abort leaves
at most O(r) unfinished calls. Supplier, LE, FW and PREP invocations have
their own primitive steps; the source invocation count is at most Qcap.
Nonrecursive arithmetic/Boolean helpers are inline loops rather than an
unbounded chain of silent calls. The finite fixed-statement program and
bounded aborted chains contribute only polynomial setup/cleanup. Hence
charging a call/return separately does not multiply the core count by the
number of open frames. This explicit event count replaces the former
conservative O(r) charge to every open context at each step.

(L2) Every non-acquisition instruction costs O(n^2 log2 n), including
physical address fees. Source moves are counted separately below.
Use straightforward binary-loop helpers, retaining a conservative log n
factor for index/emission control. A RAW access and its A-bit cursor/address
copy cost O(A^2 log n)=O(n log n). Computing a row base uses schoolbook
O(A^2) bit work and fee O(A), within O(n^(3/2)log n).
- A bit READ compares O(sqrt n) tag/epoch bits: O(n^(3/2)log n).
- A first bit WRITE clears WROW=O(n) values, stamps the tag and writes the
  bit: O(n^2 log n), with later writes no larger.
- A word helper streams at most n RAW values and initializes at most one
  row, so costs O(n^2 log n). Every bit is read or written and charged.
- ALLOC_Q, FREE_Q and a descriptor-field update use a fixed number of
  tagged word or direct RAW metadata helpers, plus bit-serial n-bit
  arithmetic: O(n^2 log n). Each metadata helper streams all n values.
- ALLOC_OWNER scans OWN=O(sqrt n) flags, copies/increments EW=O(sqrt n)
  epoch bits and writes its fixed eight-field binding record: O(n^2 log n).
  The record format in Section5 explicitly limits writes to O(n) RAW bits.
- One source move uses n+1 slot operations, source fee and SWAP gates:
  O(n^3 log n). Mapped gates/resets and staged logic are smaller.
No word, row clearing, view computation or address generation is free.

(L3) Wire events are O(C_S+nQcap), by (4.3). Initialization and release
resets are actual structural operations, not a promise about whether an unused scratch
wire might eventually be touched. (P7) independently charges their
per-primitive local emission within its structural upper bound.
Descriptor updates for moved qubits are charged to the table steps as in
Section4; resetting a released view is included. Each event costs
O(n^2 log n), so event work is O(n^2 log n C_S+n^3 log n Qcap).
This charging uses the completed reference count and is not inferred from
the larger simultaneous-space capacity c_F.

(L4) Prefix preparation and cleanup cost at most O(n^2 DRAW), including
all index emission. Bootstrap/profile computation costs polynomial O(n^6).
It is covered by the expression below since HQ>=n^3 on the main branch.

Summing, for n beyond the fixed no-wrap threshold,

    T<=c n^3(log2 n)^2(C_S+Qcap+HQ+1)+c n^2 DRAW.                (9.1)

Control and frame events cost O(n log n) instructions times the
O(n^2 log n) non-source allowance. Linear wire events from (L3) fit this
bound, and source moves cost O(n^3 log n Qcap), also below it. Polynomial
bootstrap/frame cleanup is covered by HQ>=n^3 or the prefix term. Every
fee uses A, which bounds the complete physical allocation.

Exceptional finite lengths retain the terminating exact renumbering fallback.

## 10. Time and samples

Let alpha=67/9 and e=7/6. The critical schedule proves
PP and 2^(H+dl) are O(n^alpha 2^(e sqrt n)). The sharper pool budget gives
C_ell=O(n 2^H), C_0=O(n PP), and Qcap=20rC_0+K=O(n^(3/2) PP).
The structural emitter and retained sorting ledger give

    C_S=O(n^(9/2+alpha)2^(e sqrt n)).

Use this core count directly in (9.1). The bank instructions already pay their
physical address fees in (L2); replacing C_S with the separately charged
reference time T_P would be an unnecessary extra upper-bound relaxation.
Consequently

    T=O(n^(15/2+alpha)(log2 n)^2 2^(e sqrt n))
     =O(n^(269/18)(log2 n)^2 2^(e sqrt n)).

The source-move term has power 9/2+alpha, smaller than 15/2+alpha. HQ and DRAW
have coefficient 1 in sqrt n, strictly below e, so their polynomial factors
are absorbed. All initialization, failure branches, generation, source moves,
exact overflow handling and cleanup remain counted. Acquisitions are exactly
P's requests, so

    Q<=Qcap=O(n^(3/2+alpha)2^(e sqrt n))
           =O(n^(161/18)2^(e sqrt n)).

The reduced pool C_ell=2^8K2^Hdl has exhaustion probability at most
r^-63 per batch; at most 5r batches give at most 5r^-62<2^-10 overall. Thus
the smaller pool and source count retain the same success law.

## 11. Growth indices and exact envelopes

For any fixed rational b,q and fixed positive d,
log2(n^b(log2 n)^q 2^(d sqrt n))=d sqrt n+b log2 n+q log2 log2 n.
The rule's index is therefore exactly 1/2, even for negative b.
Apply this to time b=269/18,q=2,d=7/6; quantum space b=-77/2,q=0,d=1;
and samples b=161/18,q=0,d=7/6. Classical space n has index zero.
These are the exact four declared envelopes, with no matching lower bound.

## 12. Error tolerance

The fifth claim is epsilon(n) = 0, under the model in which every acquired copy is an independent ideal coset state.
Everything above is proved under this model. No positive tolerance for malformed copies is claimed, and zero does not
assert that robustness is impossible. Under a different, adaptive malformed-supplier model the extra bank
measurements could matter; no such transfer is claimed.

## 13. Scope and limitations

- The time growth index is 1/2, as for P and the earlier versions of this construction. The research goal
  2^(O(n^(1/3))) is not reached. This is a trade-off row: S_Q=O(n^(-77/2) 2^sqrt n) and T=O(n^(269/18)(log2 n)^2 2^((7/6)sqrt n))
  and Q = O(n^(161/18) 2^((7/6) sqrt n)), with S_C = O(n). Against it, our F-LIMIT-BANK has 2887/2500 on T, S_Q and Q.
- The memory construction is not ours, capped recycling pools are qzv's, and capped IFC trees in this storage are
  mpjunior92's (Section 1). What this file adds is their composition through P and the check that P exposes the
  interface the construction needs.
- S_Q is 2^(Theta(sqrt n)), because classical records are moved into counted qubits. This is not an improvement over
  algorithms with O(n) or 2^(o(sqrt n)) qubits.
- All polynomial powers, the trim 40 ceil(log2 n), the threshold n >= 2^40, the growing group size w = 2^ceil(log2 n), FW's gate and
  scratch constant c_F are unoptimized; this variant uses the shorter tag width 4r.
- P's own statements in virtual.md (its Sections 0, 14 and 15) concern P's storage model. The four bounds of this file
  concern IFC-LOCAL-EMIT.
