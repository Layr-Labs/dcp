# Native extraction and fixed-word pool microprograms (normative)

This completes the current physical implementation. The reference gates,
source law, caps and decisions are retained. The weighted bound below
sharpens the valid but looser product bound in typed_dispatch.md.
All widths and parameters retain their definitions. A=Theta(sqrt n) is
the COMPLETE physical address width, including the entire allocated bank.

## Fixed-word pool operations

COPY, ADD, SUBTRACT, INCREMENT and COMPARE of a prescribed field are
finite inline bit microprograms. Load their constant many bindings and
complete operand fields with READWORD; stage all inputs, execute the
bit-serial operation in ordinary words, and commit its fields and pc.
For length L<=n, stream ALL L stored bits; n-bit slot/frame fields include
all padding. A short packed field writes only its L positions, preserving
adjacent fields; unused staging bits are zero padding. Three-n-bit labels
use a fixed three chunks. Overlap stages every source chunk before writes.
These macros perform no unit-cost multiplication/division or table scan.
Their n elementary bit steps each cost at most O(A^2), including ordinary
index control and full address fees. Complete field helpers already cost
O(n^2), including row validation and EVERY WROW-bit first-write clearing.
Thus a macro costs O(n^2). No constant is allowed to depend on field values.

Use these macros for LIVE/GROUP/FIFO identifiers, label addition/copy,
AVL keys/links/counts/flags, free heads, OUTPUT/buffer record moves and
supplier/demand scalar counters. A fixed record has at most12n bits and
constant many fields. Each dictionary visit/rotation touches constant
many records and uses the specified field macros. The existing parent
links support ancestor repair; no ordinary search stack is stored.
Dictionary work is O(n^2 log(Cin) Cin). A GROUP peek follows w FIFO ids
and copies w id fields, costing O(n^2 w) per request. There are at most
Cin requests per chunk, since every FW consumes at least two inputs.
Consumed-label work is O(n^2 Cin) by sum rho<=Cin; returned labels stay
in place. Thus pool metadata costs O(n^3 Cin) per chunk.

The supplier recurrence bounds each level's input sum by O(C_0) per
batch (the preceding level supplies at least twice its successor).
There are O(r) levels and O(r) batches, hence sum Cin=O(n C_0).
Calls, returns, loop-counter commits and cleanup take O(n C_0) fixed
macro/event operations: completed requests remove distinct buffer records;
FW calls consume inputs; source calls number Qcap; aborted chains have
O(r) depth. Therefore all this work is O(n^4 C_0).

Key attempts and FW Boolean circuits KEEP their counted incremental
emitter and mapped physical dispatch. Their GLOBAL structural bound is
O(n^2(log n)^4 C_0), including actual failed attempts and resets. At
O(n^2) per structural/event step their physical cost is
O(n^4(log n)^4 C_0). Coherent GROUP inputs still load their full slot
fields and use actual gates; no quantum indexed load is introduced.

At macro entry/exit all reference frame fields are committed. Calls,
owner activation, epoch checks, renumbering and abort occur only at these
aligned boundaries. A macro allocates no owner midway and holds no
cache across a boundary. Native arithmetic uses constant many O(n)-bit
words and fixed carry loops, not recursive interpreter dispatch per bit.
All other pool operations retain the mapped implementation and its fees.

## A fixed native region for LE

Reserve slots 0<=k<P, P=2^16 n, INSIDE the existing HQ-slot prefix for
one active source-transform/LE phase. Initialize general virgin=P and head=HQ; the free list
contains only slots >=P. This changes no HQ, DRAW, h or allocated-prefix
size. Since P<=U and general live<=3U, P+3U<HQ; allocation always succeeds.
The allocator invariant now separates reserved native slots, general live
and free slots below virgin, and untouched zero slots above virgin.
Reserved slots are zero outside the source-transform/LE phase and never enter the free list.
The fixed native layout has n data positions, at most2n QPE positions,
and the retained c0 n carries/work/ancillas, all below P. Its register
bases are fixed multiples of n computed bit serially before use.

KEEP the original acquisition and n+1 mapped slot transfers. Immediately after source slot transfer and BEFORE either Mult_alpha or
Shift_c of virtual.md Section3,
SWAP each of its n mapped data qubits into the corresponding zero native
position. Read the COMPLETE old slot field for each such SWAP, costing
O(n^3) total. Keep the old slots allocated and zero during preprocessing and LE. The control
and arbitrary spectators are untouched. During preprocessing and LE the decoded map sends
data and private ancillas to native positions; the old zero positions
are reserved physical slack. A native gate forms wire address2k+3 from
its staged register base and bit cursor, delivers ALL A bits and pays
O(A^2)=O(n) charged work, using the counted carry-loop/address-buffer
microprogram. Every actual Clifford+T gate, reset and measurement is paid.
No descriptor fetch is needed for a fixed native register position.

All source preprocessing is executed in this native mode. Mult_alpha
uses the exact n controlled modular additions, swap and inverse computation
of virtual.md (T1); every data/work/carry wire has a fixed native position.
Its O(n^2) gates and bit-serial constant generation cost O(n^3), with
full native address delivery. Load alpha and its inverse as complete
fields; their Euclid/CRT computation occurs once per batch and is
polynomial setup, not free preprocessing. Repeated modular doubling
generates all alpha*2^v constants in O(n^2) raw bit work, also O(n^3)
charged. Shift_c uses the exact (T2) circuit. Load its control's complete
mapped slot address ONCE, keep that staged physical address fixed during
the transform, and deliver it with all A bits for every controlled gate.
Other operands are native. This costs O(n^2) per Shift_c, including the
full field load; no descriptor is fetched per internal gate. The control
is neither freed nor moved during this phase. Its prescribed later X
also pays its mapped helper. Thus BOTH pre-LE transforms fit O(n^3)
per acquisition. They act before the same LE tests in the same logical
order. After preprocessing the transformed data eigenstate and latent
label are exactly those in the original supplier; no original-label
assumption is used for the extractor. The native-entry SWAP is only a
representation change and commutes with decoding, not a logical reorder.

At the reference data-discard point reset native data, then release the
old zero slots with the existing full-field FREE_Q helpers. This costs
O(n^3) per copy. Reset every used native subblock before return or global
abort, including extraction-cap abort; the fixed P scan costs O(n^2).
At aligned exit all reserved positions are zero, the label/frame fields
are committed and old data slots are freed. Extra SWAPs change only the
physical representation: conjugating the reference LE by the entry map
and its discard yields the identical channel on control and spectators,
on every input. There is no extra source request or success event.

LE private classical work uses fixed ordinary O(n) workspace. Store
modulus, current modular constant, means/counters, candidate, rh, random
shift, unwrapping value and scores in constant many n-bit chunks. Store
RUN's direction records in 6(n+5) bits. DO NOT store the n*T_V window
table: whenever f_i is read, regenerate its T_V bits at their prescribed
positions in rh. This gives exactly the same bits and O(n T_V) work per
verifier round. G_LE<=2n on the main branch. The fixed4096-entry rational
trigonometric table and the two existing compiler buffers fit the same
workspace. An explicit allowance2^16 n bits covers these records, local
cursors and all constant-arity staging, within the retained2^20 n margin.
There is no ordinary recursive source stack. Native word/bit indices are
polynomially bounded in n but EVERY operation still pays the full bank
address fee. Global fallback/source counters remain banked, loaded and
committed with full-word helpers, O(n^2) per LE. Owner allocation and
epoch renumbering occur at aligned outer boundaries, never halfway
through private native work, which does not advance any owner epoch.

Cheap QPE has O(n^2) structural operations eventually. Native implementation
therefore costs O(n^3) per call. Verification has O(n^2+n h_e log n)=O(n^2)
bit work, also O(n^3) charged. RUN(F(h_e)) costs O(n^3 h_e); its global
cap <=Qcap/r+1 makes aggregate LE work O(n^3 Qcap)+poly(n).
Original source transforms and transfers, entry SWAPs, old-data releases and cleanup
fit this bound. Guarded compilation is unchanged, counting the same
logical compiler bit steps before sources. Its finite MODE_RUN exceptions
retain terminating caps and affect only absolute constants. Tests,
coins, rounding, verdicts and fallback counts are identical, including
wrong-estimate branches. The old coupling and error budgets apply.

## Uniform tree and decoder emission

Use finite row/register roles and bit-cursor roles also inside the fixed
TREE/LOOKUP and decoder loops. A row value is a current-frame scalar,
not serialized anew into a literal tuple per bit/gate. At a pass entry,
initialize its fixed row roles and local bit cursors. Between successive
rows increment/subtract the row cursor with explicit carry/borrow steps;
total changes are linear in the number of rows plus boundary width.
For each row, local n-bit passes use the same carry termination. A pass's
O(r+(log n)^2) setup is absorbed by its nonempty table scan, containing
at least2^dl rows and n raw bit steps per row. Reversed passes restore
cursors with the mirrored code, without storing an instruction transcript.
Bit arithmetic on label/data values is still its individual raw steps.
The conservative allowance O(log n) per raw step covers finite tuple
emission and local cursor control. Numeric row/address formation and
complete stored-field loads remain paid by mapped O(n^2) dispatch.
Serial LOOKUP still reads each classical row and executes actual quantum
index comparisons and flag gates; its quantum index is never a bank address.

The retained raw tree sum per batch is O(n^2 2^(H+dl)), before its old
extra full-n emission allowance. With O(r) batches and the above generator,
its mapped physical cost is O(n^(9/2)log n 2^(H+dl)). Decoder raw work
per batch is O(n K C_0), updating all K residues incrementally per candidate.
Its K polynomially many rows have fixed bases and these same row/cursor
roles; candidates are never used as memory indices. Replacing the old
full-handle r allowance by O(log n), then summing O(r) batches and paying
mapped dispatch, costs O(n^4 log n C_0). At most two interval-boundary
initializations have only polynomial additional cost. Circuits, arithmetic,
candidate ordering and outputs are unchanged.

## Weighted joint result

Combining the disjoint ledgers, every actual branch has

 T<=c[n^4(log n)^4 C_0+n^(9/2)log n 2^(H+dl)+n^3 Qcap
       +n^2(HQ+DRAW+1)]+poly(n).

Use C_0=O(n PP), Qcap=O(n^(3/2)PP), and
PP,2^(H+dl)=O(n^(29/4)2^((7/6)sqrt n)). The first term dominates and gives
T=O(n^(49/4)(log2 n)^4 2^((7/6)sqrt n)). Prefix work has coefficient1
in sqrt n and is absorbed. All caps, success laws and exact epoch fallback
are retained; no event is conditioned on favorable future cutoff survival.
The complete allocated prefix is unchanged and all extra ordinary words
are within O(n). The other four complete structured objects are identical.
