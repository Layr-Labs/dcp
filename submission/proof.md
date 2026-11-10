short_interface.md completes the current configuration with an exact
short LIVE field format, scoped interface and decoder word microprogram.

# IFC-SHORT-INTERFACE: implicit-fiber four-input merges above a capped recycling pool, with O(n) classical workspace through a counted basis bank

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N), e = 7/6 and sig = 1. The single physical
algorithm IFC-SHORT-INTERFACE below receives N in binary and fresh independent copies of rho_s, and outputs the entire s with
unconditional probability at least 1 - 2^-8. On EVERY execution branch (wrong extracted labels, FW-stage (PREP
included), supplier and pool aborts, failed and retried merges and four-input merges, discarded copies, tag
renumbering, initialization and final cleanup included) it satisfies jointly

    T = O(n^(47/4)log2 n 2^(e sqrt n)),   S_C = O(n),   S_Q = O(n^(-77/2) 2^(sig sqrt n)),   Q = O(n^(35/4) 2^(e sqrt n)).

The S_Q bound retains the proved negative polynomial factor n^(-77/2) from the 40-ceiling-logarithm trim and the counted square-root-tag prefix (Section 8). All constants are absolute. Logarithmic envelopes are evaluated for n>=2; n=1 is handled by the constant-cost finite branch. The growth indices are 1/2, 0, 1/2
and 1/2 (Section 11). The fifth claim is the clean-input tolerance 0 (Section 12).

IFC-SHORT-INTERFACE executes a fixed reference algorithm P specified in the updated virtual files without changing any of its quantum operations, measurements,
source requests or classical decisions. P is IFC-LIMIT-E, whose complete specification and proof are given after the
marker line of virtual.md and in virtual2.md, distance_decoder.md (P Sections10–13),
and bucket_level.md (P Section7.2), window_merge.md (P Sections6.2,A,B),
and perm_fw.md (P Section7.1 instrument and circuits),
and verified_extract.md (P Section5 including its capped fallback),
and seed_retry.md (executed global key preparation counters),
and approx_estimate.md (guarded cheap estimate and counted compilation).
The current-frame physical controller is completed in typed_dispatch.md. "P Section x" and "P (x.y)" refer to that
text; "Section x" refers to this file. The resource statements inside virtual.md concern P in its own storage model,
in which classical records are ordinary bits; they are not claims of this file. IFC-SHORT-INTERFACE compiles transient gate-address generation structurally and changes data storage:
- every classical data record of P, except the two guarded ordinary compiler buffers, the bounded native LE workspace of native_ops.md, and constant many O(n)-bit staged words, is kept in basis-state qubits, which are
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
commit 28f1a773adce9dd8b49c8f39b590a53947189b21. The current logarithmic schedule is ell=dl=H0=ceil(7r/12+(29/4)ceil(log2 r)+64). This variant additionally grows w with n, proves RHO=2+8/r and charges its uniform circuit. Its complete specification and resource proof are reproduced here.
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
0. IFC-SHORT-INTERFACE runs it with ordinary storage. It holds cand, a copy counter and the current copy, so O(n) bits and
O(n) qubits, and it makes the same acquisitions. There are finitely many such N, so this branch changes only
absolute constants.

Main branch (n >= 2^40). P computes b0=floor(ell/2)-4 and exactly the integers of P Section 0 (r, r0, Lg, kappa, ell, dl, H0, cb, Lam,
a, JI, H) and of P Sections 7.3 and 8 (K, C_ell, D_i, Yd_i, Rc_i, C_0 = Rc_0 D_0, Y, pbmax_i and the tree capacities),
puts Qcap = 20 r C_0 + K, and runs P Sections 5-13: label extraction LE; the chunked FW stage (work-conserving FWLEVEL on chunks of D_i, with buffers and run caps); the tree shape and bit allocation of P Section 8 for each
requested B; BATCH with its tree of binary MERGEs and four-input MERGE4Is; the free-frequency block decoder; and the 2-adic block part. Every ABORT outputs 0.

Order choices. bucket_level.md fully specifies pool order: select the
least eligible key, take its first w FIFO records, leave pair-cell returns
linked in place, and append a recycled record at its new bucket's tail.
OUTPUT follows FW production, with matching pairs ordered by first endpoint;
buffers append in that order. Tree merge sorts are stable with ties in
current list order; MERGE4I streams/heaps break ties by position as in P
SectionA. No numerical slot or bank address is a tie-break key.

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
    + 2^-20 (decoder, P Lemma 11.1) + 2^-40 (2-adic miss) + 2^-10 (LE coupling, verified_extract.md) + 2^-80 (global key cap, seed_retry.md) <  2^-8.

(P2) Word sizes and loops.
- Y <= 2r <= n (P (F6)).
- Every label fits a 3n-bit field (P Sections 6 and 9).
- Every parameter above, every position pp_i and tp_i, and every loop limit has O(n) bits.
- Every loop has a length fixed by the parameters or is cut off by the caps on pool qubits and acquisitions
  (P Section 14). This holds on every branch, so every branch terminates.

(P3) Classical records. On every branch P's classical arrays are the following.
- Per pool level, the buffer Bf_i, the input chunk, and in an FWLEVEL run the LIVE item heap, OUTPUT list, bucket tree,
  metadata free stacks, borrowed GROUP ids and the measured code of the current cell (w rows of ceil(log2 n)+1 bits); and the final pool list. Each has
  at most 2^(cb+1) rows: |Bf_i| < D_(i+1) + D_i/2 (P Lemma 7.3(c)), Cin = D_i <= 2^cb, LIVE never grows, and OUTPUT
  has at most Cin/2 rows since each FW appends gamma <= rho/2 good outputs while it removes rho qubits from LIVE
  (P (7.3)); C_ell <= 2^cb (P (F4)).
- In the tree: at most four retained tables per level, each of at most 2^Lam rows. For the one active MERGE: the
  arrays aa, bb, order, pos, lo, cnt, off, Dx and the window inverse j -> (x_j, y_j), each of at most 2^Lam rows. For
  the one active MERGE4I: the residue and sort-order arrays, runs, the two heaps, Buf, Tl and the block table, each
  of at most max(2^Lam, Cp) <= 2^cb rows (P Section A; Cp <= 2^cb by P Section 8).
- One four-row global key-control array (counters and thresholds),
  whose n-bit rows fit the existing fixed-owner margin.
- The decoder's K records (Z_i, beta_i, W_i) and K residues (P Section 11).
- Verified LE's test counters/directions, n+20 binary windows and one global
  fallback counter (verified_extract.md); all are O(n) rows of O(n) bits.
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
  P Sections3 and5, including the at-most2n-qubit cheap-estimate register; the merge registers Ru, Rv, Rz, Rp, Rd, R and their Toffoli-chain scratch (P Section 6); the
  MERGE4I registers (the residue, sum and window registers of steps 1 and 3, R and Rf, and their Toffoli-chain
  scratch, fewer than 32 registers of O(sqrt n) qubits, P Section A); the FW ticket T, key/sorted-key/permutation/P registers
  and their Boolean-evaluation scratch, at most c_F=2^20 n^3 qubits in all (P Section 7.1); and one
  coin qubit (P Section 11).

These are explicit ripple and Toffoli-chain circuits. Apart from FW's registers, (P4), including the new cheap-estimate register, lists fewer than1024 registers,
each of at most 4n qubits, so the scratch totals at most c0 n + c_F qubits with c0 <= 2^12 and c_F=2^20 n^3.

(P5) Lifecycle. Every P qubit is created in one of two ways:
- by an acquisition, as part of an (n+1)-qubit copy;
- by allocation in |0>, as scratch of a transform, a modular addition, an LE test, a LOOKUP, a MERGE, a MERGE4I, an FW, a key PREP
  or a coin. Each such operation allocates at most c0 n qubits (at most c_F for an FW including its key PREP) and contains at least one P step.

Every P qubit ends by being measured and released, or reset and released, or released in a known basis state. In
four places P leaves the release implicit: the unused final-pool qubits after the K roots (P Section 9), the buffered
qubits after the final pool is formed (P Section 7.3; measured, reset and released), the wd = 1
leaf qubits with kk != 1 (P Section 12), and R after a step-4 FAIL of MERGE (P Section 6.2). IFC-SHORT-INTERFACE completes P
there, and wherever else a release is implicit, by one rule: a qubit that P never touches again is reset and released
at that point (a trace-out, so the result is still an instance of P). In detail:
- LE resets the data register of a copy. A rejected copy is released. An accepted copy's control becomes a pool qubit
  (P Sections 5, 11 and 12).
- An FW first prepares fresh short-key/permutation registers before touching
  pool inputs. On collision it resets/releases the attempt and retries,
  with the executed global counters/cap of seed_retry.md. A key-cap abort
  resets all remaining registers and outputs0.
  On success the uniform permutation is pure. The cell function, canonical
  relabeling and pair-ticket erasure are clean Boolean circuits. P,T and
  the canonical seed are measured/reset; all temporary key/sort/Boolean
  registers are cleared/reset/released. The actual circuit/wire count is
  O(n(log n)^3) per attempt/body, below c_F; the global cap counts
  every failed attempt. Cell postprocessing is exactly the
  retained CNOT/NOT rule: each released pair/block input becomes zero,
  and good/recycled/returned qubits retain their prescribed states.
  perm_fw.md proves this for every input, with private Kraus factors
  independent of x inside C. Borrowed GROUP views die after label sums;
  record removal never releases a retained output again.
- At the end of an FWLEVEL, LIVE is measured, reset and released. OUTPUT qubits move to the level's buffer by handle,
  and a request moves buffered qubits to the next level by handle (P Sections 7.2 and 7.3).
- LEAF transfers dl pool qubits into an index register and allocates nothing.
- MERGE allocates its rank/window registers. Cyclic-window inverse lookup
  clears x,y; fresh J is the output index, while measured R and old inputs
  are reset/released. FAIL discards all inputs (window_merge.md Section6.2).
- MERGE4I computes the residues/Tl rank and measures Rf. On success its
  cyclic window keeps fresh J, inverse lookup clears x1..x4, and R,Rf and
  old indices are reset/released. Every FAIL discards all inputs, never
  reused. Classical window inverse tables reuse the old block-table capacity.
  The modular circuit adds O(r) fixed scratch within c0 n; its fixed register
  lists/ripple construction and the original fixed families remain below
  c0<=2^12. Window metadata fields/owners fit the existing context allowance.

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
- C_S=O(n^(5/2)C_0+n^(7/2) 2^(H+dl))+poly(n);
- Q_P <= Qcap (P Section 13);
- C_0 <= 64 RHO^ell C_ell (P Lemma 7.3(d)) and C_ell<=3*2^21 r^2 2^H (P (F4));
- PP and 2^(H+dl) are O(n^alpha 2^(e sqrt n)), where alpha = 29/4 (P Section 14);
- cb <= sig sqrt n - 40 log n and Lam + kappa + 4 = cb (P (F1) and Section 0).

(P7) Structural compiler. A gate operand is an owner id, a local register
row/bit index and a fixed operation tag. The current-frame program emits
this tuple, and the bank resolver of Sections4,9 reads the full slot field
and computes the complete physical address. The tuple is classical, never
superposed. OWN is polynomial, so owner ids have O(log n) meaningful bits.
FW and LE quantum-register widths and actual scratch sizes are polynomial,
so their local indices also have O(log n) bits. Permutation/key offsets use their fixed polynomial-sized array layouts.

GROUP contains w borrowed item-row ids of Y_i=ceil(log2(Cin+1))<=2r+1
bits. It copies no label or slot fields. A gate on A_i resolves its
GROUP item id and then that LIVE record's complete d-bit stored slot field (short_interface.md).
These are a constant number of counted word helpers; the typed dispatch
bound still applies. The physical records remain until postprocessing
has formed all consumed-input label sums. Returned items remain linked
and unchanged. bucket_level.md proves O(nCin) amortized label-data bit work, with local emission within the chunk bound,
and O(wY_i(log n)^2) per-call GROUP work, including local emission. No quantum slot is cloned by a view.

The short-key circuits of perm_fw.md have O(n(log n)^3) actual
quantum gates/wires per attempt and body. Its incremental generator costs
O(log n) aggregate per gate. seed_retry.md executes request/failure caps
M_K=10r(ell+1)(C_0+1) and F_K=M_K/r; total attempts are at most2M_K+2.
Thus their GLOBAL work is O(n^2(log n)^4 C_0), below
O(n^(5/2)C_0) because(log n)^4<=3sqrt n on the main branch.
No per-chunk retry-work bound is assumed.

The cursor-role emitter in typed_dispatch.md counts finite role tuples
and amortized bit-serial cursor updates. GROUP, dictionary and consumed-label
work cost O(n^(3/2)Cin) per chunk, globally O(n^(5/2)C_0). Fixed key/body
work retains O(n^2(log n)^4 C_0), which fits the same envelope because
(log2 n)^4<=3sqrt n above2^40. No per-chunk retry bound is asserted.
The guarded cheap estimator, exact translations and verifier/fallback
have aggregate O(n^2 Qcap)+poly(n) structural work, as proved in
approx_estimate.md and verified_extract.md. Pre-source compilation, two
ordinary n-bit buffers, deterministic guarded mode, all approximation
bounds and exact data/spectator preservation are unchanged. Since
Qcap=O(rC_0), LE fits O(n^(5/2)C_0). Every actual quantum gate is counted.

The ideal outer process omits key retry/cap state and all extraction
private state/caps as specified in their complete proofs. The actual
coupling adds only the separate2^-80 key event to the preceding success
sum. This does not condition a yield or fresh-digit argument on favorable
future cutoff survival. The new four-row global key-control array fits
the existing fixed-owner/row margin; the physical prefix is unchanged.

For tree work retain the full uniform-emission allowance O(n) per old
skeleton step. The exact skeleton sum in P Section14 is
O(r n C_ell 2^dl/dl) per batch. Here dl>=r/2 and C_ell=O(n2^H),
so it is O(n^2 2^(H+dl)), not the older loose n^(5/2) bound.
Multiplying by the retained n emission allowance and O(r) batches gives
O(n^(7/2)2^(H+dl)). No faster tree primitive is assumed. For decoder work use the sharper existing candidate-update bound: the
standalone decoder ledger is O(n^(5/2)C_0) per batch only because of an
extra n handle allowance, whereas structural classical bit arithmetic
and reference row tuples cost at most O(n^2 C_0) per batch, and across
O(r) batches O(n^(5/2)C_0). Explicitly K=O(r), candidates<=2^(Y+8)=O(C_0),
and each candidate uses K additions of O(n) bits; even an O(r) row/handle
emission allowance makes O(n^2 C_0) per batch. Decoder arrays have K polynomially many rows with fixed known bases;
forming a row/bit offset costs O((log n)^2), and copying/incrementing a
full reference handle costs O(r). No candidate is used as a memory index:
candidates update the K residue words incrementally. Thus the stated
O(r) emission allowance per decoder bit step is sufficient for all
large n. Initialization of K residues at the at most two interval
boundaries is polynomial. Thus every component fits (P6).

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
borrowed GROUP views and decoder records also fit V. No owner or slot cap shrinks.

FW now has a fixed number of descriptor arrays for its key, sorted-key,
permutation, ticket, code and Boolean scratch registers, not a growing
family R_m. Each array has at most c_F rows, within V by the inequality
above. Verified LE adds fewer than16 fixed arrays for windows, counters
and directions. These and FW add fewer than128 fixed owners in total.
Only one FW or one LE call is active at a time; inline sorting/ripple
helpers have no growing ordinary stack or extra owner family.

The GROUP owner has a view format: backing-owner is the LIVE item array,
and row i stores its Y_i-bit nullable item id. To resolve quantum operand
A_i, read this id, subtract1, then read the LIVE row's complete d-bit stored slot
field, logically zero-extended as specified in short_interface.md. The two row/word operations and their address arithmetic are paid
by Section9 and typed_dispatch.md. GROUP owns no second qubit. A released
input's slot field may be cleared; its classical labels remain until the
amortized postprocessing. Retained slots move exactly once to an output
record before old views die. All descriptor clearing is counted as a
wire event, and record freeing performs no additional quantum release.

Including the added fixed owners, at most 2^12(a+JI+ell+4)+1296 owners are needed for
the nested computation and fixed scratch. Even allowing 64K additional owners
for retained root records and tables, the total is below
8192r+20000+64K <=8192r+20000+3*2^19r <2^24r=OWN.
This conservative allowance does not require streaming root measurements.
Since K<=n, the live-qubit bound may include 17n instead of 16n; still
4r2^cb+17n+c0n+c_F<=3U<HQ. Every capacity and availability invariant therefore
holds on all branches. The owner coefficients are deliberately fixed, not advice.

Borrowed views change only implementation descriptors. The decoded
logical qubits/records and all source/measurement laws are unchanged.
Every full physical reference, row initialization and descriptor write
is charged; ordinary temporaries remain constant many O(n)-bit words.
Depth-dependent program frames and all arrays remain bank records.

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

Let h be the least power of two with h >= max(DRAW, HQ + 2). On the main branch IFC-SHORT-INTERFACE first computes the
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
pool qubit, a register with its descriptor array, or a borrowed GROUP view;
its descriptor rows hold one slot number per qubit. Lists carry slot numbers
where P carries wire indices. head = HQ means empty.
- ALLOC_Q: if head != HQ, put k := head and head := NEXT[k]; otherwise put k := virgin and virgin := virgin + 1.
  Return k.
- FREE_Q(k): reset wire 2k+3 (the reset core step, which records no outcome); then NEXT[k] := head and head := k.

Initially head := HQ and virgin := P=2^22n^3; slots below P are the
reserved native region of native_ops.md. The general allocator never
allocates or frees those slots. NEXT[k] is read only after FREE_Q(k) has written it. No operation scans the
slots. Every head, NEXT and virgin access is a known-address READMETA/WRITEMETA
operation, costing O(n^2) with the inline RAW fees below.

Invariant (I). The general slots P<=k<virgin are partitioned into two sets; reserved
slots k<P follow the native zero/outside-call invariant in native_ops.md:
- slots holding live P qubits, one slot per qubit, mapped injectively by the descriptors;
- slots on the free stack, which has no repetitions and whose slots are in |0>, in tensor product with everything.

Slots at or above virgin are untouched |0>. ALLOC_Q removes a free or untouched slot from those sets and gives it to
exactly one new P qubit. FREE_Q is called only when P releases that qubit, never when a handle is merely passed or
copied, and it returns the slot to |0>. A P qubit keeps its slot from allocation until release, and passing a
register passes its descriptor, never a copy of its qubits. So (I) is preserved. Gates read their operands' slot
numbers from the descriptors and act on the corresponding odd wires.

The pool is never full. By (P4), with the completion rule of (P5), at most 4r2^cb+17n+c0n+c_F slots are live
at once. Since c0 <= 2^12 and c_F=2^20n^3 <= 2^cb (cb >= r/2 by P (F1)),

    live<=4r2^cb+17n+2^12n+2^20n^3<=3U+P<HQ,   because HQ=2^20 U=2^22 r2^cb.

If virgin = HQ and the free stack were empty, all HQ-P general slots would be live, a contradiction. So ALLOC_Q always
succeeds, and no abort or guard is added.

Wire events. Call every ALLOC_Q, FREE_Q and descriptor-row update a wire event. By (P5):
- allocations number at most C_S+(n+1)Q_P, since each non-source
  allocation has its own explicit counted initialization reset;
- releases number at most C_S plus source bookkeeping, since every logical
  release has its own counted reset; the allocation bound is also sufficient;
- each allocation or release updates at most c1 descriptor rows;
- moving a qubit between lists costs nothing extra: its slot number is a field of the list row, and P copies that row
  itself, in semantic data steps already counted in C_S;
- only LEAF and the cyclic-window merge output transfers move slot numbers into descriptor rows, at most c1 rows per moved qubit. LEAF moves dl
  qubits and builds 2^dl table rows, and the cyclic-window outputs each move lam' qubits and write 2^lam' table rows, so each such
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
semantics for every bit, including borrowed GROUP views and partial-row writes. QED.

A first write clears only WROW=O(n) bits, not all ROWS. This work is charged in
Section9. This explicit clearing is essential: sharing a row tag without it
would expose old values in unwritten fields and would be incorrect.

Words, loops and LOOKUP.
- An O(n)-bit field of a row is a run of logical bits. Word operations are bit-serial, with a staged carry.
- P's classical computations run as fixed bit-serial code whose operands are READ from and WRITTEN to the bank. These
  are the comparisons, additions, merge sorts and binary searches; table construction; the residue updates of the
  decoder; and parameter arithmetic, with schoolbook multiplication and division. Only constant many O(n)-bit words
  are staged at once.
- P's source loop counters, recursion frames and profiles are bank rows.
  Only the compiler's separately guarded n-bit workspace and n-bit rotation-
  template buffer are ordinary, counted in Section8. Source recursion has
  no ordinary call stack; other circuits are generated online without an
  unbounded stored transcript.
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
replaced. GROUP views use the backing-owner field and a finite view-format id.
They resolve the item id and LIVE slot field as specified in Section3.
All record reads/writes stream the n bits with RAW_READ/RAW_WRITE. There
are a fixed number per operand/activation, so binding work costs O(n^2),
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

The extra one frame owner per context is included in the 2^12 coefficient
of Section3; the enlarged 8192r+20000 bound still fits OWN. Thus the
representation uses no ordinary source-recursion stack (the separately
guarded compiler workspace is counted) and changes no decoded
reference operation, decision, source call or output.

## 6. Exact renumbering when G is full

IFC-SHORT-INTERFACE never assumes that G cannot wrap. If ALLOC_OWNER finds G all ones (a bit-serial test), P is paused, and the
following is done for o=0,...,OWN-1.
- If o is active, copy ep(o) to backup. For each row, retain its value bits if
  its tag equals backup; otherwise clear all its value bits. Set that row's
  tag to o+1. Finally set ep(o)=o+1.
- If o is inactive, clear all its value bits, row tags and epoch.
Then set G=OWN and resume the pending activation. Every active row decodes
as before; invalid rows become explicit zeros. Inactive rows are below every
future fresh epoch. OWN+2<2^EW, so generations remain available. GROUP view
bindings are unchanged. P executes no operation while this is done, and its
quantum slots and persistent RAW allocator metadata are untouched. One full scan has polynomial overhead times DRAW;
O(n^3 DRAW) remains a sufficient charged bound. All finite exceptional wraps
are implemented rather than assumed away.

Renumbering is eventually absent. Owner activations are polynomial in n times
the core-step and source caps. The reference proof gives
C_S=O(n^(7/2+alpha) 2^((7/6)sqrt n)) and
Qcap=O(n^(3/2+alpha)2^((7/6)sqrt n)), alpha=29/4.
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
P's full-handle emitter. This follows directly from GROUP views and fixed
binding definitions; no numerical handle value is a source of randomness.

IFC-SHORT-INTERFACE has no randomness of its own. Its staged decisions and every RAW_READ outcome are fixed functions of N and
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

By induction from P's initial state (input N, all scratch zero), the decoded semantic state of IFC-SHORT-INTERFACE equals
P_sem at every aligned point, on every branch: extraction errors, returned and recycled FW outputs, failed merges, partial
children, rejected copies and aborts included. Its source-request sequence and its output law equal P's. By (P1) it
outputs s with probability at least 1 - 2^-8 for every N and s.

The held-out-bit argument of P Section 10 and the coupling of P Section 5 are statements about P's logical law, which
pi preserves. The held-out-bit argument is applied to the decoded logical law, conditioning
only on its specified G. In particular it does not condition on a physical RAW
transcript that might include high label bits. Equality of decoded output laws,
not an assertion that such a transcript reveals no bits, transfers correctness.

## 8. Classical and quantum space

S_C. IFC-SHORT-INTERFACE's ordinary classical storage consists of:
- the input N in at most n+1 bits and the output in n bits;
- two bounded ordinary n-bit buffers for compiled rotation templates and
  compiler workspace (the latter released after preprocessing);
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
word registers; no source recursion stack or unbounded circuit transcript is stored there;
the guarded O(n)-bit compiler workspace and template buffer are explicitly
included in this same allowance.
Set A=ceil(log2(2h+(2^20+2)n+10))+1. It upper-bounds every physical address
fee and A=O(sqrt n). Address roles and RAW cursors use A-bit words; data values
retain their full O(n)-bit fields. All arithmetic is bit-serial.

## 9. Explicit polynomial ledger

Every core step of IFC-SHORT-INTERFACE pays its address fee ADDR = ceil(log(S_C + S_Q + 2)), and ADDR <= n by (8.2). An
instruction is one of the following:
(i) a logical READ or WRITE;
(ii) a RAW_READ or RAW_WRITE;
(iii) a bit operation on staged words;
(iv) one gate, measurement or reset of P on mapped slots;
(v) an ALLOC_Q or FREE_Q, or a descriptor field update;
(vi) an ALLOC_OWNER or FREE_OWNER;
(vii) one acquisition, with its SWAP.

(L1) Typed current-frame control completion is fully specified in
typed_dispatch.md. A dispatch, CALL or RETURN uses a constant number of
whole-field bank helpers, plus O(A^2) staged address-arithmetic bit
operations and smaller copies/tests. Helpers are fixed inline code and
do not dispatch recursively per transferred bit. Whole n-bit fields
remain streamed and charged. Reference data arithmetic still contributes
its individual bit steps to C_S. No operand resolution walks ancestors.

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

(L2) Every non-acquisition instruction costs O(n^2), including complete
physical address fees. The final section of typed_dispatch.md specifies
finite inline bit microprograms with carry-overflow termination and proves
this bound. A RAW access costs O(A^2), including full address-buffer copying
and delivery. Schoolbook row-base formation costs O(A^3). Tag comparison
costs O(r A^2+A^3), and a first write clears every WROW=O(n) cell, stamps
the tag and writes the bit in O(n A^2+A^3)=O(n^2). Complete n-bit word and
RAW metadata helpers stream all bits and perform at most one row validation.
ALLOC_Q/FREE_Q and descriptors use fixed many full-word helpers; owner
activation scans flags, handles every epoch bit and writes eight full n-bit
binding fields. All cost O(n^2), including staged arithmetic. The n+1 slot
operations of one source move cost O(n^3); source/SWAP fees are included.
No address, word operation, reset, row clearing or padding bit is free.

(L3) Wire events are O(C_S+nQcap), by (4.3). Initialization and release
resets are actual structural operations, not a promise about whether an unused scratch
wire might eventually be touched. (P7) independently charges their
per-primitive local emission within its structural upper bound.
Descriptor updates for moved qubits are charged to the table steps as in
Section4; resetting a released view is included. Each event costs
O(n^2), so event work is O(n^2 C_S+n^3 Qcap).
This charging uses the completed reference count and is not inferred from
the larger simultaneous-space capacity c_F.

(L4) Prefix preparation and cleanup cost at most O(n^2 DRAW), including
all index emission. Bootstrap/profile computation costs polynomial O(n^6).
It is covered by the expression below since HQ>=n^3 on the main branch.

Summing the typed controller, events and source charges, for n beyond
the fixed no-wrap threshold, typed_dispatch.md proves

    T<=c n^2 (C_S+HQ+1)+c n^3 Qcap+c n^2 DRAW.    (9.1)

There are constant many expensive word helpers per dispatch, and the
remaining O(A^2) staged Boolean operations cost O(A^3), below
O(n^2). Frame events have the proved linear count, and wire events
obey (L3). Source transfers are the separate second term. Initialization,
bootstrap and cleanup are included. Every fee uses the complete A.

Exceptional finite lengths retain the terminating exact renumbering fallback.

## 10. Time and samples

Let alpha=29/4 and e=7/6. All schedule and source facts are unchanged:
PP,2^(H+dl)=O(n^alpha 2^(e sqrt n)), C_ell=O(n2^H),
C_0=O(n PP), Qcap=20rC_0+K=O(n^(3/2)PP).
The scoped implementation of short_interface.md gives the sharper ledger

 T<=c[n^(7/2)C_0+n^(9/2)log2 n 2^(H+dl)+n^3 Qcap
       +n^2(HQ+DRAW+1)]+poly(n).

All stored fields are read completely in their actual format, with full
bindings loaded once per scope, full first-write row clears and every
address/reset fee charged. Decoder word arithmetic is counted bit serially.
Substitution gives T=O(n^(9/2+alpha)log2 n 2^(e sqrt n))
=O(n^(47/4)log2 n 2^(e sqrt n)). Prefix/HQ work has coefficient1<e;
polynomial setup and finite guarded exceptions affect only constants.
Source requests are unchanged:
Q<=Qcap=O(n^(3/2+alpha)2^(e sqrt n))=O(n^(35/4)2^(e sqrt n)).

The reduced pool C_ell=2^8K2^Hdl has exhaustion probability at most
r^-63 per batch; at most 5r batches give at most 5r^-62<2^-10 overall. Thus
the smaller pool and source count retain the same success law.

## 11. Growth indices and exact envelopes

For any fixed rational b,q and fixed positive d,
log2(n^b(log2 n)^q 2^(d sqrt n))=d sqrt n+b log2 n+q log2 log2 n.
The rule's index is therefore exactly 1/2, even for negative b.
Apply this to time b=47/4,q=1,d=7/6; quantum space b=-77/2,q=0,d=1;
and samples b=35/4,q=0,d=7/6. Classical space n has index zero.
These are the exact four declared envelopes, with no matching lower bound.

## 12. Error tolerance

The fifth claim is epsilon(n) = 0, under the model in which every acquired copy is an independent ideal coset state.
Everything above is proved under this model. No positive tolerance for malformed copies is claimed, and zero does not
assert that robustness is impossible. Under a different, adaptive malformed-supplier model the extra bank
measurements could matter; no such transfer is claimed.

## 13. Scope and limitations

- The time growth index is 1/2, as for P and the earlier versions of this construction. The research goal
  2^(O(n^(1/3))) is not reached. This is a trade-off row: S_Q=O(n^(-77/2) 2^sqrt n) and T=O(n^(47/4)log2 n 2^((7/6)sqrt n))
  and Q = O(n^(35/4) 2^((7/6) sqrt n)), with S_C = O(n). Against it, our F-LIMIT-BANK has 2887/2500 on T, S_Q and Q.
- The memory construction is not ours, capped recycling pools are qzv's, and capped IFC trees in this storage are
  mpjunior92's (Section 1). What this file adds is their composition through P and the check that P exposes the
  interface the construction needs.
- S_Q is 2^(Theta(sqrt n)), because classical records are moved into counted qubits. This is not an improvement over
  algorithms with O(n) or 2^(o(sqrt n)) qubits.
- All polynomial powers, the trim 40 ceil(log2 n), the threshold n >= 2^40, the growing group size w = 2^ceil(log2 n), FW's gate and
  scratch constant c_F are unoptimized; this variant uses the shorter tag width 4r.
- P's own statements in virtual.md (its Sections 0, 14 and 15) concern P's storage model. The four bounds of this file
  concern IFC-SHORT-INTERFACE.
