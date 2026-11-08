# TRIAD-BANK: TRIAD-125 with O(n) classical workspace through a counted basis bank and an indexed quantum free list

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N), beta = 156/125 and gamma = 3307/2650
(gamma < beta, since 3307 * 125 = 413375 < 413400 = 156 * 2650). The single physical algorithm TRIAD-BANK below
receives N in binary and fresh independent copies of rho_s, and outputs the entire s with unconditional probability
at least 1 - 2^-8. On EVERY execution branch (wrong extracted labels, TRIAD-stage, supplier and pool aborts, failed
and retried merges, discarded copies, tag renumbering, initialization and final cleanup included) it satisfies jointly

    T = O(n^132 2^(beta sqrt n)),   S_C = O(n),   S_Q = O(n^30 2^(beta sqrt n)),   Q = O(n^3 2^(gamma sqrt n)).

All constants are absolute. The growth indices are 1/2, 0, 1/2 and 1/2 (Section 11). The fifth claim is the
clean-input tolerance 0 (Section 12).

TRIAD-BANK executes a fixed reference algorithm P without changing any of its quantum operations, measurements,
source requests or classical decisions. P is TRIAD-125, whose complete specification and proof are reproduced byte
for byte after the marker line of virtual.md. "P Section x" and "P (x.y)" refer to that text; "Section x" refers to
this file. The resource statements inside virtual.md concern P in its own storage model, in which classical records
are ordinary bits; they are not claims of this file. TRIAD-BANK changes only where data live:
- every classical record of P, except constant many O(n)-bit staged words, is kept in basis-state qubits, which are
  counted in S_Q and are read and written only at classically known addresses (Sections 3-6);
- P's qubits live in a fixed counted array of quantum slots, managed by an indexed free list (Section 4).

Notation for P: r, ell, m, dl, kappa, K, C_i, Y and Qcap are as in P Sections 0, 8, 11 and 13, and
PP = (8/3)^ell 2^m. A "P step" is a core step in the sense of P Section 2, C_P is the number of P steps on a branch,
and T_P is P's charged time (P (2.1)), so C_P <= T_P. All logarithms are base 2. Constants c, c0, c1 are absolute.

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
- the reference algorithm P (TRIAD-125, our submission f5b375dd-1e5c-4728-95dc-b855b2dc5827), which replaces
  HPC-127's pairing stage by a three-qubit instrument;
- the check in Section 2 that P supplies every property the construction uses;
- the lifecycle accounting for P's pool primitive TRIAD (Sections 2 and 4);
- the exponents for P's parameters (Sections 8 and 10), where the coefficient beta is an exact rational of P's
  schedule and needs no logarithm estimate.

## 2. The reference algorithm P and the facts used from it

Finite branch (n < 2^28). P is the exhaustive tester of P Section 13: for cand = 0, ..., N-1 use n+10 fresh copies,
apply Shift_cand, measure the control in X, and reject cand at the first minus; output the first unrejected cand, or
0. TRIAD-BANK runs it with ordinary storage. It holds cand, a copy counter and the current copy, so O(n) bits and
O(n) qubits, and it makes the same acquisitions. There are finitely many such N, so this branch changes only
absolute constants.

Main branch (n >= 2^28). P computes exactly the integers

    r = ceil(sqrt n), ell = ceil(183r/500), m = ceil(73r/100), dl = ceil(259r/500), kappa = ceil(log m) + 1,
    K = 2^13 (2r + ceil(log n) + 30), C_ell = 2^12 n K 2^m dl, C_i = ceil(8 ell C_(i+1)/(3(ell-1))) (i = ell-1..0),
    Y = least integer with 2^Y >= C_0,  Qcap = 4 n C_0 + K,

and runs P Sections 5-13: label extraction LE; the TRIAD stage, ell TRIADLEVELs of Y+1 rounds each; the bit
allocation of P Section 8 for each requested B; BATCH with its linear-merge tree; the free-frequency decoder; and the
2-adic part. Every ABORT outputs 0.

Completion of unspecified orders. P leaves three orders open:
- equal-key ties in its merge sorts;
- the order of LIVE after a TRIADLEVEL round;
- the order of OUTPUT.

TRIAD-BANK fixes them as follows:
- sorts are stable, with ties in current list order;
- after a round, LIVE lists, in scan order, the qubit the triple returns to LIVE (A_l or A1) at the position of that
  triple and the ungrouped qubits at their own positions;
- OUTPUT is in order of production, so "the first C_(i+1)" of P Section 9 step 2 is defined.

These orders are functions of P's classical history only, never of slot numbers or bank addresses. Every lemma of P
that meets these orders holds for any order that is a function of the past:
- P Lemma 7.2 holds "for ANY labels, and conditional on everything before the level";
- the sigma-field G of P Lemma 10.1 contains all decisions of the controller;
- P Lemmas 6.1, 9.1, 9.2 and 11.1 are conditional on the past.

So this completion is an instance of P.

Facts used. Sections 3-10 use only the following properties of P.

(P1) Success. P outputs s with probability at least 1 - 2^-10 on the finite branch and at least 1 - 2^-8 on the main
branch. P Section 13 bounds the main-branch failure probability by the sum of six terms:

    2^-10 (pool exhaustion, P Lemma 9.1) + 2^-40 (TRIAD-stage abort, P Lemma 9.2) + 2^-40 (supplier abort)
    + 2^-20 (decoder, P Lemma 11.1) + 2^-40 (2-adic miss) + 2^-10 (LE coupling, P (5.1))  <  2^-8.

(P2) Word sizes and loops.
- Y <= 2r <= n (P (8.3)).
- Every label fits a 3n-bit field (P Sections 6 and 9).
- Every parameter above, every position pp_i and tp_i, and every loop limit has O(n) bits.
- Every loop has a length fixed by the parameters or is cut off by the caps on pool qubits and acquisitions
  (P Section 14). This holds on every branch, so every branch terminates.

(P3) Classical records. On every branch P's classical arrays are the following.
- The supplier's pool list, and in a TRIADLEVEL the lists LIVE and OUTPUT and the merge-sort scratch. Each has at most
  C_0 rows, since Cin = C_i <= C_0 and LIVE never grows (P Section 7.2).
- In the tree: at most three retained tables per level, each of at most 2^(dl+m-1) rows. For the one active merge:
  the arrays aa, bb, order, pos, lo, cnt, off, Dx and the block inverse v -> (x_v, y_v), each of at most 2^(dl+m)
  rows (P Sections 6.2 and 14).
- The decoder's K records (Z_i, beta_i, W_i) and K residues (P Section 11).
- LE's 2(J_e + 1) test counters and directions (P Section 5).
- The profiles over i of C_i, pbmax_i, pb_i, pp_i (ell rows) and of lam_i, tbmax_i, tb_i, tp_i (m+1 rows)
  (P Section 8), and the 4096-row table of P Section 4.
- O(1) scalars per loop level and per frame of the depth-first recursion, whose depth is m+1.

Each row of these arrays has at most 12n bits. Lists store a handle to their qubit; P calls it the "wire index", and
here it is a slot number (Section 4).

(P4) Qubits. At any time P holds at most:
- C_0 pool qubits (P Section 14);
- 2(m+1)(dl+m) <= 16n qubits of stacked index registers (P Section 14);
- a fixed set of scratch registers: the current copy (n+1 qubits); the transform, modular-addition and LE scratch of
  P Sections 3 and 5; the merge registers Ru, Rv, Rz, Rp, Rd, R and their Toffoli-chain scratch (P Section 6); the
  TRIAD ancillas e1, e2, c, L1, L0 and O(1) chain scratch (P Section 7.1); and one coin qubit (P Section 11).

These are explicit ripple and Toffoli-chain circuits. (P4) lists fewer than 512 registers, each of at most 4n qubits,
so the scratch totals at most c0 n qubits with c0 <= 2^11.

(P5) Lifecycle. Every P qubit is created in one of two ways:
- by an acquisition, as part of an (n+1)-qubit copy;
- by allocation in |0>, as scratch of a transform, a modular addition, an LE test, a LOOKUP, a MERGE, a TRIAD or a
  coin. Each such operation allocates at most c0 n qubits and contains at least one P step.

Every P qubit ends by being measured and released, or reset and released, or released in a known basis state. In
three places P leaves the release implicit: the unused final-pool qubits after the K roots (P Section 9), the wd = 1
leaf qubits with kk != 1 (P Section 12), and R after a step-4 FAIL of MERGE (P Section 6.2). TRIAD-BANK completes P
there, and wherever else a release is implicit, by one rule: a qubit that P never touches again is reset and released
at that point (a trace-out, so the result is still an instance of P). In detail:
- LE resets the data register of a copy. A rejected copy is released. An accepted copy's control becomes a pool qubit
  (P Sections 5, 11 and 12).
- A TRIAD on pool qubits A1, A2, A3 (P Section 7.1) allocates e1, e2, c, L1, L0 and its chain scratch in |0>. Steps
  1-6 return all of them to |0> on every input (P Lemma 7.1(d)), and they are then released.
  - Step 7 with l in {1,2,3}: A_b is brought to |1> by a CNOT, then to |0> by NOT, and released; A_a (the good output)
    and A_l (the returned qubit) stay.
  - Step 7 with l = 0: A2 and A3 are |0> and are released; A1 stays.
  So a TRIAD makes O(1) wire events and keeps one or two of its inputs.
- At the end of a TRIADLEVEL, LIVE is measured, reset and released. BATCH step 2 measures and releases the unused
  outputs (P Sections 7.2 and 9).
- LEAF transfers dl pool qubits into an index register and allocates nothing.
- MERGE allocates its registers. It returns x and y to |0> (step 5) and releases them, keeps the low lam' bits of R as
  the output index register, and on FAIL resets and releases both inputs (P Section 6.2).
- A root is measured and released, and unused roots are released (P Sections 11 and 12). At an ABORT or at the end
  every remaining qubit is released.

(P6) Cost. On every main branch, P Section 14 and (2.1) give:
- C_P = O(n^(7/2) C_0 + n^4 2^(m+dl)) + poly(n) and T_P = O(n^6 2^(beta sqrt n)), with C_P <= T_P;
- Q_P <= Qcap (P Section 13);
- C_0 <= 8 (8/3)^ell C_ell (P (8.2));
- log PP <= gamma r + 128/53 and m + dl <= beta r + 2 (P Section 14).

The pool primitive. The HPC-127 version of this construction differs from the present one only in P's pool primitive
(PAIR there, TRIAD here) and in the schedule constants. The construction uses the pool primitive only through (P4) and
(P5): a bounded number of wire events per primitive, kept qubits transferred by handle, and released qubits reset. By
P Lemma 7.1(d), which holds for every input state, TRIAD satisfies both. Sections 3-10 use P's yield lemmas
(P Lemmas 7.2 and 9.2) only through (P1), and P's schedule only through (P2), (P3) and (P6).

## 3. Fixed capacities of the bank

Put U = C_0 + 2^(dl+m) + 1 and

    OWN = 2^16 n^2 owners,  WROW = 2^16 n^2 bit cells per row,  ROWS = 2^24 n^4 U rows per owner,
    HQ = 2^20 n^2 U quantum slots.

An owner holds one logical array. The logical bit (o, i, j), with o < OWN, i < ROWS and j < WROW, has the address

    c = o ROWS WROW + i WROW + j  <  LSPAN = OWN ROWS WROW = 2^56 n^8 U.               (3.1)

Fit. Every array of (P3) has at most max(C_0, 2^(dl+m), K, 4096, ell, m+1, 2(J_e+1)) <= U <= ROWS rows. The
slot metadata of Section 4 has HQ rows, and HQ <= ROWS because ROWS/HQ = 16 n^2. Every row of P has at most
12n <= WROW bits. A slot number is below HQ < 2^n, so it has at most n bits.

Descriptors of P's qubits (Section 4) have one slot number per row:
- a pool qubit's slot number is a field of its row in the pool list, LIVE or OUTPUT;
- an index register of a phase vector has a descriptor array of at most dl + m rows in the same per-level family as
  its table;
- each of P's named scratch registers (P4) has its own descriptor array of at most c0 n <= U rows.

Fewer than 64 arrays are live per tree level and per TRIAD level. The others are fewer than 64 + 512: fewer than 64
for the decoder, LE, profiles, table, slot metadata and frame arrays, and fewer than 512 scratch descriptors, one per
register of (P4). So at most 64(m + 1) + 64 ell + 576 <= 512(m + ell + 2) <= OWN arrays are live at once. Frames of
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

Let h be the least power of two with h >= max(DRAW, HQ + 2). On the main branch TRIAD-BANK first computes the
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

The pool is never full. By (P4), with the completion rule of (P5), at most C_0 + 16n + c0 n slots are live at
once. Since c0 <= 2^11 and C_0 >= 1,

    live  <=  n C_0 + 2^11 n + 16n  <  HQ,   because HQ = 2^20 n^2 U >= 2^20 n^2 C_0.

If virgin = HQ and the free stack were empty, all HQ slots would be live, a contradiction. So ALLOC_Q always
succeeds, and no abort or guard is added.

Wire events. Call every ALLOC_Q, FREE_Q and descriptor-row update a wire event. By (P5):
- allocations number at most c0 n C_P + (n+1) Q_P;
- releases number at most the allocations;
- each allocation or release updates at most c1 descriptor rows;
- moving a qubit between lists costs nothing extra: its slot number is a field of the list row, and P copies that row
  itself, in P steps already counted in C_P;
- only LEAF and MERGE step 6 move slot numbers into descriptor rows, at most c1 rows per moved qubit. LEAF moves dl
  qubits and builds 2^dl table rows, and MERGE step 6 moves lam' qubits and writes 2^lam' table rows, so each such
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

TRIAD-BANK never assumes that G cannot wrap. If ALLOC_OWNER finds G all ones (a bit-serial test), P is paused, and the
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
on any branch for n >= n1. For each of the finitely many lengths 2^28 <= n < n1 every branch is finite, because all
loops of P are bounded. So renumbering there changes only an absolute constant.

## 7. Correctness: the decoded classical-quantum invariant

An aligned point is any point between two P steps or acquisitions. Define a map pi from the physical state to P's
logical state at aligned points:
- decode the cells of every active owner through its epoch (Lemma 5.1);
- keep P's control position and bindings;
- map each slot that holds a live P qubit to that qubit, using the descriptors (injective by (I));
- trace out free slots, padding wires, tags, inactive owners, allocator fields and every other physical-only record.

TRIAD-BANK has no randomness of its own. Its staged decisions and every RAW_READ outcome are fixed functions of N and
of the outcomes of P's own measurements so far: by induction over steps, the basis content z of all bank wires and
staged bits is such a function, and a RAW_READ returns a bit of z. So at each aligned point the physical state is

    sum_z p_z |z><z| (x) rho_z,

where rho_z is a state of the mapped P qubits and of any reference system, possibly entangled and correlated with z,
and p_z is the probability of P's outcome history behind z. We show that pi(Phi_phys(X)) = Phi_P(pi(X)) for each step,
where Phi_P is P's channel for that step and Phi_phys is TRIAD-BANK's.

- Bank steps. On a state of this form, RAW_READ leaves the state unchanged and reveals a bit of z. RAW_WRITE maps z to
  a known z'. By Lemma 5.1 and Section 6, READ, WRITE, ALLOC_OWNER, FREE_OWNER and renumbering change the decoded
  record exactly as P's classical read, write, allocation or forgetting would. A forgotten staged bit mixes the
  conditional states rho_z as P's own forgetting does. By linearity this holds for arbitrary rho_z and references.
- Quantum steps. P's gate, measurement or reset on at most three qubits is applied to the slots holding those qubits.
  The classical controls of P's classically controlled gates are READ from the bank. LOOKUP is P's serial circuit,
  with table bits read from the bank. So, conditional on z, the action on rho_z is P's.
  In particular TRIAD's steps 1-7 are applied gate by gate on the slots of A1, A2, A3 and of its ancillas. By
  P Lemma 7.1(d), which holds for every input state, the instrument (7.1) of P is realized on the mapped qubits
  whatever the correlations, and its outcome l is recorded in the bank.
- Allocation and release. ALLOC_Q supplies a slot in |0> in tensor product with everything (by (I)), which is P's
  fresh qubit. FREE_Q applies reset, that is trace-out followed by |0>, to a qubit that P has just released, and pi
  forgets that qubit in both cases.
- Sources. Each request of P triggers exactly one acquisition of a fresh copy into the (n+1)-qubit acquisition
  register. Its qubits are SWAPped, with three CNOTs per qubit, into n+1 slots obtained by ALLOC_Q, and the register,
  now |0>, is released. SWAP is exact, so the mapped qubits hold the same rho_s. Prefix zeros and metadata are not
  source copies.

By induction from P's initial state (input N, all scratch zero), the reduced logical state of TRIAD-BANK equals P's
at every aligned point, on every branch: extraction errors, recycled TRIAD outcomes, failed merges, partial children,
rejected copies and aborts included. Its source-request sequence and its output law equal P's. By (P1) it outputs s
with probability at least 1 - 2^-8 for every N and s.

The held-out-bit argument of P Section 10 and the coupling of P Section 5 are statements about P's logical law, which
pi preserves. The extra RAW_READ outcomes are functions of P's outcome history, so conditioning on them adds nothing.

## 8. Classical and quantum space

S_C. TRIAD-BANK's ordinary classical storage consists of:
- the input N and the output, n bits each;
- constant many staged words of O(n) bits each (a RAW index or wire number, an owner, row and bit index, a slot
  number, an operand of a word operation);
- O(1) staged bits, and O(log n)-bit counters of the bit-serial loops;
- the finite control of the fixed program.

A wire number needs at most log(2h) + 1 bits, which is at most 2r + 30 log n + 120 <= n by (8.2) below.

Before the prefix exists, the parameters are computed by streaming:
- C_0 by the recurrence from C_ell, with one current word of at most Y + 1 <= 2r + 1 bits and the counter i;
- then U, DRAW, HQ and h, each of O(n) bits.

Once the prefix exists, the profiles are recomputed into the bank. The finite branch uses O(n) bits. So S_C = O(n) on
every branch.

S_Q. Bounds from P. By P Sections 8, 11 and 14, K <= 3 * 2^13 r, dl <= r and r^2 <= (sqrt n + 1)^2 <= 4n. Hence
C_ell <= 3 * 2^27 n^2 2^m and C_0 <= 8 (8/3)^ell C_ell <= 3 * 2^30 n^2 PP. Since r <= sqrt n + 1 and
gamma + 128/53 < 4, log PP <= gamma sqrt n + 4. Likewise m + dl <= beta sqrt n + beta + 2 < beta sqrt n + 4.

Hence, with gamma < beta,

    C_0 <= 3 * 2^34 n^2 2^(gamma sqrt n),   U <= 2^36 n^2 2^(beta sqrt n).                (8.1)

Bounds on the layout. These follow from (8.1) and EW + 1 <= 2^21 n^20 (n >= 2):
- HQ = 2^20 n^2 U <= 2^56 n^4 2^(beta sqrt n);
- LSPAN = 2^56 n^8 U <= 2^92 n^10 2^(beta sqrt n);
- DRAW <= 2^114 n^30 2^(beta sqrt n), since the terms after LSPAN (EW+1) in (4.1) are O(n^22).

By (4.2),

    S_Q <= 2h + n + 1 <= 4 DRAW + n + 1 <= 2^117 n^30 2^(beta sqrt n),                    (8.2)

using HQ + 2 <= LSPAN <= DRAW, so that h < 2 DRAW.

This counts every physical wire: bank values, tags, epochs, flags, RAW scratch, every slot (live, free or never used),
the padding up to 2h, and the acquisition register. It is a fixed span, the same on every branch. The finite branch
uses O(n) qubits. So S_Q = O(n^30 2^(beta sqrt n)).

## 9. Explicit polynomial ledger

Every core step of TRIAD-BANK pays its address fee ADDR = ceil(log(S_C + S_Q + 2)), and ADDR <= n by (8.2). An
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
- Bookkeeping. P is a fixed program with s0 statements, s0 an absolute constant. Let D <= c(m+2) bound the
  iterations and calls open at once (bounded static nesting, recursion depth m+1). Every innermost body consists of
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

The derivation above gives c n^28 per P step and c n^24 per wire event, far below these degrees. For 2^28 <= n < n1,
and on the finite branch, the work is bounded on every branch, so these lengths change only the constant.

## 10. Time and samples

T. Substitute (P6), (8.1) and Section 8 into (9.1):
- T_P = O(n^6 2^(beta sqrt n)) gives degree 126;
- Qcap = 4 n C_0 + K = O(n^3 2^(gamma sqrt n)), which is O(n^3 2^(beta sqrt n)), gives degree 123;
- HQ = O(n^4 2^(beta sqrt n)) gives degree 124;
- DRAW = O(n^30 2^(beta sqrt n)) gives degree 130.

So T = O(n^130 2^(beta sqrt n)), and in particular

    T = O(n^132 2^((156/125) sqrt n)).

The declared power 132 is mpjunior92's conservative choice, kept for comparability. The coefficient 156/125 is the
exact rational m + dl <= (156/125) r + 2 of P's integer schedule: no logarithm estimate enters it, and it is the
larger of P's two exponents (gamma for the pool, beta for the tree). Initialization, every failed or recycled branch,
every abort, all bank, descriptor and slot work, the source moves and the output-first cleanup are included.

Q. TRIAD-BANK makes exactly one acquisition for each request of P and none other (Section 7). On the main branch,
Qcap = 4 n C_0 + K counts every rejected copy, every TRIAD-stage, supplier and pool abort, and every discarded merge
input of every batch (P Section 13). By (8.1),

    Q = Q_P <= Qcap <= 3 * 2^36 n^3 2^(gamma sqrt n) + K = O(n^3 2^((3307/2650) sqrt n)).

The finite branch uses at most N(n+10) copies, a constant over its finitely many N. Bank zeros, tags, slot
bookkeeping, SWAPs and renumbering are charged as work and storage, never as copies.

## 11. Growth indices

For fixed c > 0 and fixed a >= 0, log(n^a 2^(c sqrt n)) = c sqrt n + a log n. Then
log log max(4, n^a 2^(c sqrt n)) = (1/2) log n + log c + o(1), and the index g = 1/2 exactly. This holds for each of
T (a = 132, c = 156/125), S_Q (a = 30, c = 156/125) and Q (a = 3, c = 3307/2650). For S_C = O(n),
log log max(4, n) = log log n, so g = 0. The indices are those of the proved upper envelopes; no lower bound is
claimed. The structured objects in submission.json are exactly these four envelopes.

## 12. Error tolerance

The fifth claim is epsilon(n) = 0, under the model in which every acquired copy is an independent ideal coset state.
Everything above is proved under this model. No positive tolerance for malformed copies is claimed, and zero does not
assert that robustness is impossible. Under a different, adaptive malformed-supplier model the extra bank
measurements could matter; no such transfer is claimed.

## 13. Scope and limitations

- The time growth index is 1/2, as for P and the HPC-127 versions of this construction. The research goal
  2^(O(n^(1/3))) is not reached. Against the HPC-127 version with explicit degrees, the exponent coefficient drops from
  4950737/3900250 (about 1.26934) to 156/125 = 1.248 for T and S_Q, and to 3307/2650 (about 1.24792) for Q. The
  polynomial powers are the same, and S_C = O(n) as there.
- The memory construction is not ours (Section 1). What this file adds is its application to TRIAD-125 and the check
  that P's TRIAD-based pool exposes the interface it needs.
- S_Q is 2^(Theta(sqrt n)), because classical records are moved into counted qubits. This is not an improvement over
  algorithms with O(n) or 2^(o(sqrt n)) qubits.
- All polynomial powers, the threshold n >= 2^28 and the tag width (n+2)^20 are unoptimized.
- P's own statements in virtual.md (its Sections 0, 14 and 15) concern P's storage model, in which S_C is exponential.
  The four bounds of this file concern TRIAD-BANK.
