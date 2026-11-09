# Exact supplier ceiling caps

This variant sets Rc_i=ceil(Rc_(i+1)D_(i+1)/Yd_i). Lemma 7.3 proves
that this tighter deterministic cap always serves every request if yields
meet their minima. Its saturated-prefix analysis gives C_0<=64RHO^ell C_ell,
removing a redundant factor ell from the old estimate. Every acquisition,
abort and failure is still capped. Joint bounds improve to time
n^(305/18)(log2 n)^4 2^((7/6)sqrt n) and samples
n^(85/9)2^((7/6)sqrt n); the row-bank space envelopes remain unchanged.

# IFC-CEILING-CAPS: implicit-fiber four-input merges above a capped recycling pool, with O(n) classical workspace through a counted basis bank

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N), e = 7/6 and sig = 1. The single physical
algorithm IFC-CEILING-CAPS below receives N in binary and fresh independent copies of rho_s, and outputs the entire s with
unconditional probability at least 1 - 2^-8. On EVERY execution branch (wrong extracted labels, FW-stage (PREP
included), supplier and pool aborts, failed and retried merges and four-input merges, discarded copies, tag
renumbering, initialization and final cleanup included) it satisfies jointly

    T = O(n^(305/18)(log2 n)^4 2^(e sqrt n)),   S_C = O(n),   S_Q = O(n^-38 2^(sig sqrt n)),   Q = O(n^(85/9) 2^(e sqrt n)).

The S_Q bound retains the proved negative polynomial factor n^-38 from the 40-ceiling-logarithm trim and the counted square-root-tag prefix (Section 8). All constants are absolute. Logarithmic envelopes are evaluated for n>=2; n=1 is handled by the constant-cost finite branch. The growth indices are 1/2, 0, 1/2
and 1/2 (Section 11). The fifth claim is the clean-input tolerance 0 (Section 12).

IFC-CEILING-CAPS executes a fixed reference algorithm P specified in the updated virtual files without changing any of its quantum operations, measurements,
source requests or classical decisions. P is IFC-LIMIT-E, whose complete specification and proof are given after the
marker line of virtual.md, in virtual2.md and in distance_decoder.md (Sections 10-13) (P Sections 7.3, 8, A and B). "P Section x" and "P (x.y)" refer to that
text; "Section x" refers to this file. The resource statements inside virtual.md concern P in its own storage model,
in which classical records are ordinary bits; they are not claims of this file. IFC-CEILING-CAPS changes only where data live:
- every classical record of P, except constant many O(n)-bit staged words, is kept in basis-state qubits, which are
  counted in S_Q and are read and written only at classically known addresses (Sections 3-6);
- P's qubits live in a fixed counted array of quantum slots, managed by an indexed free list (Section 4).

Notation for P: r, r0, Lg, ell, dl, H, a, JI, Lam, cb, kappa, K, C_ell, D_i, Yd_i, Rc_i, C_0, Y and Qcap are as in P
Sections 0, 7.3, 8, 11 and 13; w = 2^ceil(log2 n), q = w/2, RHO = 2+8/r and c_F are as in P Sections 7 and 8; and
PP = RHO^ell 2^H (P Section 14). A "P step" is a core step in the sense of P Section 2, C_P is the number of P steps on
a branch, and T_P is P's charged time (P (2.1)), so C_P <= T_P. All logarithms are base 2. Constants c, c0, c1 are
absolute.

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
0. IFC-CEILING-CAPS runs it with ordinary storage. It holds cand, a copy counter and the current copy, so O(n) bits and
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

IFC-CEILING-CAPS fixes them as follows:
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
leaf qubits with kk != 1 (P Section 12), and R after a step-4 FAIL of MERGE (P Section 6.2). IFC-CEILING-CAPS completes P
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

(P6) Cost. On every main branch, P Section 14 and (2.1) give:
- C_P=O(n^(7/2)(log n)^2 C_0+n^4 2^(H+dl))+poly(n), and T_P=O(n^6(log n)^2 PP),
  with C_P <= T_P;
- Q_P <= Qcap (P Section 13);
- C_0 <= 64 RHO^ell C_ell (P Lemma 7.3(d)) and C_ell<=3*2^27 r^3 2^H (P (F4));
- PP and 2^(H+dl) are O(n^alpha 2^(e sqrt n)), where alpha = 67/9 (P Section 14);
- cb <= sig sqrt n - 40 log n and Lam + kappa + 4 = cb (P (F1) and Section 0).

P's own envelopes (P Sections 0 and 14) concern its storage model. This file uses the bounds listed above, which P
proves with explicit polynomial factors.

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

Put U = r 2^(cb+2) and

    OWN=2^24 r owners, WROW=2^16 n bit cells per row, ROWS=2^24 U rows per owner,
    HQ=2^20 U quantum slots.

An owner holds one logical array. The logical bit (o, i, j), with o < OWN, i < ROWS and j < WROW, has the address

    c = o ROWS WROW + i WROW + j  <  LSPAN=OWN ROWS WROW=2^64 r n U.               (3.1)

Fit. Every reference data array has at most U rows; the metadata array for
head, virgin and NEXT has at most HQ+2 rows, below ROWS=16HQ. Every data row
has at most 12n bits, below WROW=2^16n, and each slot index fits n bits since
log2 HQ<=sqrt n+23<n. Growing Boolean scratch has at most c_F=2^20n^3
qubits and descriptor rows, below U by cb>=19+5log2 r.

The only growing family of separate scratch-register descriptors is R_m,
3<=m<w, from FW. This implementation gives these registers disjoint views of
one RR descriptor array, not separate owners. Put j_m=ceil(log2 m) and
S(m)=sum_(v=3)^(m-1) j_v. Descriptor bit j of R_m uses RR row S(m)+j.
The intervals are disjoint because S(m+1)=S(m)+j_m, and their total length
S(w)<=w log2 w<=U. RR has one owner per active FW. The PREP flag/try scratch,
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

After packing this family, at most 512(a+JI+ell+4)+1168 owners are needed for
the nested computation and fixed scratch. Even allowing 64K additional owners
for retained root records and tables, the total is below
1024r+5000+64K <=1024r+5000+3*2^19r <2^24r=OWN.
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
Put LROWS=OWN*ROWS=2^48 r U and LSPAN=LROWS*WROW=2^64 r n U.
For logical row R=o ROWS+i, its RAW base is B(R)=(WROW+EW)R.
Value bit j is at B(R)+j, and tag bit t is at B(R)+WROW+t.
The RAW span is

    DRAW=LROWS(WROW+EW)+(OWN+8)EW+OWN+2^20n^4.                (4.1)

The remaining disjoint ranges contain ep(o), G, backup and six spare epoch
words, then OWN active flags, then 2^20n^4 interpreter/binding scratch bits.
No RAW record is lazily tagged. Row values and row tags occupy separate
positions within their block, and different row blocks are disjoint.

These ranges are disjoint and end below DRAW. RAW records carry no tags.

Physical wires:
- RAW index j is wire 2j;
- quantum slot k < HQ is wire 2k + 3;
- wire 1 is spare.

Let h be the least power of two with h >= max(DRAW, HQ + 2). On the main branch IFC-CEILING-CAPS first computes the
parameters with O(n) staging (Section 8). It then allocates wires 0, ..., 2h-1 in |0> once, and releases them once at
the very end, after the output is written. In between it allocates only an (n+1)-qubit acquisition register, one at
a time. Hence on every main branch

    S_Q <= 2h + n + 1.                                                                    (4.2)

Bank wires are acted on only by computational-basis measurements and by X gates conditioned on classical bits.

Slot allocator. The bank holds n-bit head and virgin words in rows0 and1 of a persistent META owner; NEXT[k] is rowk+2 of that owner. These HQ+2 rows fit ROWS. All field accesses use READWORD/WRITEWORD below, as do slot descriptor fields. Every P quantum register is a pool qubit, a register with its descriptor array, or an R_m view of RR, and its descriptor rows list its slot numbers, one per row. P's lists store slot numbers where P stores wire
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

The pool is never full. By (P4), with the completion rule of (P5), at most 4r2^cb+17n+c0n+c_F slots are live
at once. Since c0 <= 2^12 and c_F=2^20n^3 <= 2^cb (cb >= r/2 by P (F1)),

    live<=4r2^cb+17n+2^12n+2^20n^3<=3U<HQ,   because HQ=2^20 U=2^22 r2^cb.

If virgin = HQ and the free stack were empty, all HQ slots would be live, a contradiction. So ALLOC_Q always
succeeds, and no abort or guard is added.

Wire events. Call every ALLOC_Q, FREE_Q and descriptor-row update a wire event. By (P5):
- allocations number at most O(n^2(log n)^2 C_P)+(n+1) Q_P;
- releases number at most the allocations;
- each allocation or release updates at most c1 descriptor rows;
- moving a qubit between lists costs nothing extra: its slot number is a field of the list row, and P copies that row
  itself, in P steps already counted in C_P;
- only LEAF, MERGE step 6 and MERGE4I step 8 move slot numbers into descriptor rows, at most c1 rows per moved qubit. LEAF moves dl
  qubits and builds 2^dl table rows, and MERGE step 6 and MERGE4I step 8 each move lam' qubits and write 2^lam' table rows, so each such
  move is charged to at least 2^dl or 2^lam' table rows, hence to at least one P step per moved qubit.

Hence a branch has at most

    c n^2(log2 n)^2 (C_P + Qcap)                                   (4.3)

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
  The allocator uses these routines for its head/NEXT/virgin/descriptor fields.
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

## 6. Exact renumbering when G is full

IFC-CEILING-CAPS never assumes that G cannot wrap. If ALLOC_OWNER finds G all ones (a bit-serial test), P is paused, and the
following is done for o=0,...,OWN-1.
- If o is active, copy ep(o) to backup. For each row, retain its value bits if
  its tag equals backup; otherwise clear all its value bits. Set that row's
  tag to o+1. Finally set ep(o)=o+1.
- If o is inactive, clear all its value bits, row tags and epoch.
Then set G=OWN and resume the pending activation. Every active row decodes
as before; invalid rows become explicit zeros. Inactive rows are below every
future fresh epoch. OWN+2<2^EW, so generations remain available. RR view
boundaries are unchanged. P executes no operation while this is done, and its
quantum slots are untouched. One full scan has polynomial overhead times DRAW;
O(n^3 DRAW) remains a sufficient charged bound. All finite exceptional wraps
are implemented rather than assumed away.

Renumbering is eventually absent. Owner activations are polynomial in n times
the core-step and source caps. The reference proof gives
C_P=O(n^(5+alpha)(log n)^2 2^((7/6)sqrt n)) and
Qcap=O(n^(2+alpha)2^((7/6)sqrt n)), alpha=67/9.
Their logarithms are at most (7/6)sqrt n+O(log n). Since EW=4r>=4sqrt n,
no wrap occurs on any branch for all sufficiently large n. The fixed exact
renumbering fallback remains correct below that absolute threshold. Each
exceptional length has bounded P loops and terminating renumbering with
OWN+2<2^(4r), so the finite set changes only an absolute constant.

## 7. Correctness: the decoded classical-quantum invariant

An aligned point is any point between two P steps or acquisitions. Define a map pi from the physical state to P's
logical state at aligned points:
- decode the cells of every active owner through its epoch (Lemma 5.1);
- keep P's control position and bindings;
- map each slot that holds a live P qubit to that qubit, using the descriptors (injective by (I));
- trace out free slots, padding wires, tags, inactive owners, allocator fields and every other physical-only record.

IFC-CEILING-CAPS has no randomness of its own. Its staged decisions and every RAW_READ outcome are fixed functions of N and
of the outcomes of P's own measurements so far: by induction over steps, the basis content z of all bank wires and
staged bits is such a function, and a RAW_READ returns a bit of z. So at each aligned point the physical state is

    sum_z p_z |z><z| (x) rho_z,

where rho_z is a state of the mapped P qubits and of any reference system, possibly entangled and correlated with z,
and p_z is the probability of P's outcome history behind z. We show that pi(Phi_phys(X)) = Phi_P(pi(X)) for each step,
where Phi_P is P's channel for that step and Phi_phys is IFC-CEILING-CAPS's.

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

By induction from P's initial state (input N, all scratch zero), the reduced logical state of IFC-CEILING-CAPS equals
P's at every aligned point, on every branch: extraction errors, returned and recycled FW outputs, failed merges, partial
children, rejected copies and aborts included. Its source-request sequence and its output law equal P's. By (P1) it
outputs s with probability at least 1 - 2^-8 for every N and s.

The held-out-bit argument of P Section 10 and the coupling of P Section 5 are statements about P's logical law, which
pi preserves. The held-out-bit argument is applied to the decoded logical law, conditioning
only on its specified G. In particular it does not condition on a physical RAW
transcript that might include high label bits. Equality of decoded output laws,
not an assertion that such a transcript reveals no bits, transfers correctness.

## 8. Classical and quantum space

S_C. IFC-CEILING-CAPS's ordinary classical storage consists of:
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

S_Q. Count the entire new row-tag prefix. U<=8n^(-79/2)2^sqrt n,
HQ=2^20U, and LROWS=2^48rU. Its value span satisfies

    LSPAN=2^64 r n U <=2^68 n^-38 2^sqrt n.

EW<=WROW, so row tags add at most another value span. The epoch/flag/scratch
terms are O(n^4), absorbed because 42log2 n<=sqrt n above the main threshold.
Thus DRAW=O(n^-38 2^sqrt n). As HQ+2<=DRAW and h<2DRAW,

    S_Q<=2h+n+1=O(n^-38 2^sqrt n).                            (8.2)

For example 2^80 n^-38 2^sqrt n bounds this main-branch allocation after the
explicit coefficients are enlarged. It includes unused rows, tags, empty
slots, all padding, shared-view descriptors, scratch and the acquisition
register. The finite branch only affects the uniform asymptotic constant.
Classical staging is bounded by 2^20n bits using a fixed number of bit-serial
word registers; no recursion stack or circuit transcript is stored there.
Set A=ceil(log2(2h+(2^20+2)n+10))+1. It upper-bounds every physical address
fee and A=O(sqrt n). Address roles and RAW cursors use A-bit words; data values
retain their full O(n)-bit fields. All arithmetic is bit-serial.

## 9. Explicit polynomial ledger

Every core step of IFC-CEILING-CAPS pays its address fee ADDR = ceil(log(S_C + S_Q + 2)), and ADDR <= n by (8.2). An
instruction is one of the following:
(i) a logical READ or WRITE;
(ii) a RAW_READ or RAW_WRITE;
(iii) a bit operation on staged words;
(iv) one gate, measurement or reset of P on mapped slots;
(v) an ALLOC_Q or FREE_Q, or a descriptor field update;
(vi) an ALLOC_OWNER or FREE_OWNER;
(vii) one acquisition, with its SWAP.

(L1) Control completion uses O(n^(3/2)log2 n) instructions per P step.
A step touches at most three bits/qubits. Fetching its n-bit bindings takes
O(n) instructions. Arithmetic uses O(A)-bit indices and O(A^2) bit
operations, with at most logarithmic loop-emission overhead. RR prefix
arithmetic uses O((log n)^3). Each term fits O(n log n).
For the fixed program there are at most O(r) open pool/tree contexts;
each has O(n) bit-serial field work and at most logarithmic generation
work per listed step. Keep their product O(r n log n), rather than
relaxing it to O(n^2). Bank frames implement these contexts and only a
constant number of words are staged at once. Since r<=2sqrt n, the
claimed instruction count follows. This retains the conservative charge
to every open context and requires no amortized stack assumption.

(L2) All instructions cost O(n^3 log2 n), including physical address fees.
Use straightforward binary-loop helpers, retaining a conservative log n
factor for index/emission control. A RAW access and its A-bit cursor/address
copy cost O(A^2 log n)=O(n log n). Computing a row base uses schoolbook
O(A^2) bit work and fee O(A), within O(n^(3/2)log n).
- A bit READ compares O(sqrt n) tag/epoch bits: O(n^(3/2)log n).
- A first bit WRITE clears WROW=O(n) values, stamps the tag and writes the
  bit: O(n^2 log n), with later writes no larger.
- A word helper streams at most n RAW values and initializes at most one
  row, so costs O(n^2 log n). Every bit is read or written and charged.
- ALLOC_Q, FREE_Q and a descriptor-field update use only a fixed number of
  word helpers, plus bit-serial n-bit arithmetic: O(n^2 log n).
- ALLOC_OWNER scans OWN=O(sqrt n) flags and copies/increments EW=O(sqrt n)
  epoch bits; its at-most-O(n^2)-bit RAW binding costs O(n^3 log n).
- One source move uses n+1 slot operations, source fee and SWAP gates:
  O(n^3 log n). Mapped gates/resets and staged logic are smaller.
No word, row clearing, view computation or address generation is free.

(L3) Count actual scratch allocations, not unused capacity. The explicit
FW circuit uses O(w^2(log w)^2)=O(n^2(log n)^2) Boolean gates and fresh
scratch bits per call; compute/copy/uncompute and fixed cell/ticket
registers have the same bound. Its PREP tries are separate operations:
each allocates only O(log n) bits and contains P steps. Every other primitive
allocates O(n) scratch, and each call contains P steps. Source copies have
n+1 qubits. Thus (4.3) gives O(n^2(log n)^2(C_P+Qcap)) wire events,
including descriptor updates and RR view clears. Keeping c_F=2^20n^3
as a safe simultaneous-space capacity does not require allocating its
unused wires. Each event uses word/slot operations of O(n^2 log n), so
event work is O(n^4(log n)^3(C_P+Qcap)). Since log n=O(sqrt n), this
is O(n^(9/2)(log n)^2(C_P+Qcap)).

(L4) Prefix preparation and cleanup cost at most O(n^2 DRAW), including
all index emission. Bootstrap/profile computation costs polynomial O(n^6).
It is covered by the expression below since HQ>=n^3 on the main branch.

Summing, for n beyond the fixed no-wrap threshold,

    T<=c n^(9/2)(log2 n)^2(C_P+Qcap+HQ+1)+c n^2 DRAW.                (9.1)

Control costs O(n^(3/2)log n C_P) times the common O(n^3 log n) allowance;
events fit the same bound by (L3), and source moves are smaller. Every fee is counted using A, which
bounds the actual total allocated memory, not just the addressed subarray.
Exceptional finite lengths retain the terminating exact renumbering fallback.

## 10. Time and samples

Let alpha=67/9 and e=7/6. The critical schedule proves
PP and 2^(H+dl) are O(n^alpha 2^(e sqrt n)). The sharper pool budget gives
C_ell=O(n^(3/2)2^H), C_0=O(n^(3/2) PP), and Qcap=20rC_0+K=O(n^2 PP).
The fully charged uniform-generation core ledger gives

    C_P=O(n^(5+alpha)(log2 n)^2 2^(e sqrt n)).

Use this core count directly in (9.1). The bank instructions already pay their
physical address fees in (L2); replacing C_P with the separately charged
reference time T_P would be an unnecessary extra upper-bound relaxation.
Consequently

    T=O(n^(19/2+alpha)(log2 n)^4 2^(e sqrt n))
     =O(n^(305/18)(log2 n)^4 2^(e sqrt n)).

The source-cap term has power 13/2+alpha, smaller than 19/2+alpha. HQ and DRAW
have coefficient 1 in sqrt n, strictly below e, so their polynomial factors
are absorbed. All initialization, failure branches, generation, source moves,
exact overflow handling and cleanup remain counted. Acquisitions are exactly
P's requests, so

    Q<=Qcap=O(n^(2+alpha)2^(e sqrt n))
           =O(n^(85/9)2^(e sqrt n)).

The reduced pool C_ell=2^14rK2^Hdl has exhaustion probability at most
2^-13/r per batch; at most 5r batches give less than 2^-10 overall. Thus
the smaller pool and source count retain the same success law.

## 11. Growth indices and exact envelopes

For any fixed rational b,q and fixed positive d,
log2(n^b(log2 n)^q 2^(d sqrt n))=d sqrt n+b log2 n+q log2 log2 n.
The rule's index is therefore exactly 1/2, even for negative b.
Apply this to time b=305/18,q=4,d=7/6; quantum space b=-38,q=0,d=1;
and samples b=85/9,q=0,d=7/6. Classical space n has index zero.
These are the exact four declared envelopes, with no matching lower bound.

## 12. Error tolerance

The fifth claim is epsilon(n) = 0, under the model in which every acquired copy is an independent ideal coset state.
Everything above is proved under this model. No positive tolerance for malformed copies is claimed, and zero does not
assert that robustness is impossible. Under a different, adaptive malformed-supplier model the extra bank
measurements could matter; no such transfer is claimed.

## 13. Scope and limitations

- The time growth index is 1/2, as for P and the earlier versions of this construction. The research goal
  2^(O(n^(1/3))) is not reached. This is a trade-off row: S_Q=O(n^-38 2^sqrt n) and T=O(n^(305/18)(log2 n)^4 2^((7/6)sqrt n))
  and Q = O(n^(85/9) 2^((7/6) sqrt n)), with S_C = O(n). Against it, our F-LIMIT-BANK has 2887/2500 on T, S_Q and Q.
- The memory construction is not ours, capped recycling pools are qzv's, and capped IFC trees in this storage are
  mpjunior92's (Section 1). What this file adds is their composition through P and the check that P exposes the
  interface the construction needs.
- S_Q is 2^(Theta(sqrt n)), because classical records are moved into counted qubits. This is not an improvement over
  algorithms with O(n) or 2^(o(sqrt n)) qubits.
- All polynomial powers, the trim 40 ceil(log2 n), the threshold n >= 2^40, the growing group size w = 2^ceil(log2 n), FW's gate and
  scratch constant c_F are unoptimized; this variant uses the shorter tag width 4r.
- P's own statements in virtual.md (its Sections 0, 14 and 15) concern P's storage model. The four bounds of this file
  concern IFC-CEILING-CAPS.
