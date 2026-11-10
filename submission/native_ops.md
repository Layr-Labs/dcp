Physical costs use typed_dispatch.md; older allowances here remain valid looser bounds.

# Native operations (normative)

All source rules and caps are retained. A is the full allocated-prefix
address width. The final section specifies the current weighted bound.

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

At macro entry/exit all reference frame fields are committed. Calls,
owner activation, epoch checks, renumbering and abort occur only at these
aligned boundaries. A macro allocates no owner midway and holds no
cache across a boundary. Native arithmetic uses constant many O(n)-bit
words and fixed carry loops, not recursive interpreter dispatch per bit.
All other pool operations retain the mapped implementation and its fees.

## A fixed native region for LE

Reserve slots 0<=k<P, P=2^22 n^3, INSIDE the existing HQ-slot prefix for
one active source-transform/LE phase or FW call. Initialize general virgin=P and head=HQ; the free list
contains only slots >=P. This changes no HQ, DRAW, h or allocated-prefix
size. Since P<=U and general live<=3U, P+3U<HQ; allocation always succeeds.
The allocator invariant now separates reserved native slots, general live
and free slots below virgin, and untouched zero slots above virgin.
Reserved slots are zero outside native calls and never enter the free list.
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
abort, including extraction-cap abort; the fixed LE subregion scan (2^16 n positions) costs O(n^2).
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

## Amortized tree emission

TREE/LOOKUP uses finite READVAR/WRITEVAR/GATEVAR role tuples. Numeric
positions remain explicit scalars, not recopied literal indices. The
physical resolver still reads complete stored fields and forms/delivers
full addresses at mapped O(n^2) cost per structural step.

For a t-bit field pass, initialize its RELATIVE bit cursor and carry
counter, emit constant-size tuples and increment/decrement bit serially.
Field-format roles supply the base offset through the physical resolver,
so source generation does not copy that offset at every bit. Counter/
cursor work is O(t+(log(t+1))^2)=O(t), including initialization and reverse
restoration. Internal ripple control uses the squared carry-run bound
of typed_dispatch.md. A fixed flag field uses implicit relative bit0,
not a fresh log(n)-bit index. Row binding copies its Y<=2r+1 meaningful
bits explicitly; complete physical n-bit binding loads remain paid.

Label construction/copy visits do n-bit passes, absorbing O(r) row
binding. Serial LOOKUP forms/uncomputes the actual quantum index-equality
flag, reads every prescribed table bit and executes controlled output
gates. Row-position bits are READVAR from a scalar, never a quantum bank
address. Full row label/index passes absorb binding and local setup.
Across a complete table scan row-cursor carry work is linear plus O(Y^2)
initialization, absorbed by its at least2^dl rows.

Use bottom-up stable merge-sort on the retained (key,position) records.
Every comparison scans its complete padded word: O(lam+b) bits, at least
lam because the position tie breaker is included. Copy the selected
record with the same field templates. Heap sift steps compare/update
complete O(lam+b) keys/pointers. Since lam>=dl>=r/2, O(r) row binding
and short flag tests fit each node's existing word-work allowance.
Copying a nonsequential row pointer is explicit O(r) DATA work already
in the heap/run skeleton, not O(r^2) generation. Heap-depth counters
have O(log r) bits and their setup fits the complete key pass. Empty/
short runs use fixed tests within that record visit; no new row binding
per flag is needed. Table orders and semantic quantum operations are preserved.

The cyclic-window arithmetic module may KEEP its old polynomial uniform
generator, absorbed per primitive by n(L+L') because input exponents
are at least dl>=r/2. No faster generator is assumed for that module.
The field/row/sort/heap templates add only a constant to the retained raw
binary skeleton and four-input listing bound of window_merge.md.
Thus raw tree work per batch O(n^2 2^(H+dl)), O(r) batches and mapped
O(n^2) dispatch give O(n^(9/2)2^(H+dl)) with no extra logarithm.
Substitute this tree count in short_interface.md's retained ledger.

## Fixed native FW and amortized decoder refinement

The current reservation is P=2^22 n^3, within the SAME HQ-slot prefix;
general virgin starts at P and no reserved slot enters the free list.
V>=2^21 r^6, U=rV and n^3<=r^6 imply P<=U. Thus general live+P<HQ,
with no change to DRAW, h or the full allocated-space envelope.
LE uses only its original2^16 n subregion and clears only that region.
FW uses its fixed key/sort/join/ticket/permutation/code/Boolean register
layout of perm_fw.md, plus w input-copy bits. Actual scratch is
O(n(log n)^3) and is below c_F+w<P. All native regions are zero outside
calls. Reset ONLY actually used FW positions on each attempt/return/abort;
unused capacity stays zero. Final prefix clearing retains its DRAW charge.

Prepare keys/permutation with exactly the same gates and global retry
cutoffs, now at fixed native positions. Collisions still occur before
touching inputs. After PREP success, CNOT each mapped A_i into a native
zero X_i. Every such gate resolves its complete GROUP/item slot fields
and pays O(n^2); all w gates cost O(n^3). Execute the clean Boolean
cell/ticket/canonical-seed circuits on X in place of A. Their boundary
map leaves the input basis word unchanged, as proved in perm_fw.md.
Before ANY P/T/seed measurement CNOT A_i into X_i again, clearing X.

For every basis x and seed, the composite map is
 |x>|seed>|0>_X -> |x>|F(x,seed)>|x>_X
               -> |x>|F(x,seed)>|0>_X.
Linearity proves equality of the entire arbitrary-input instrument,
including spectator coherences and the private seed outcomes. X is
cleared scratch, not additional source incidence. The old conditional
cell law and all yield/distance proofs are unchanged. Actual CNOT/NOT
postprocessing on mapped A_i stays mapped and costs at most O(n^3)
per request. Labels retain the fixed-word macros.

Activate the fixed code owner before native entry; inside commits use
that existing owner without owner activation.

Private gate operands have fixed native register bases and the Section7
incremental polynomial-width cursors. Form/deliver EVERY A-bit physical
address, at O(A^2)=O(n) per gate/structural step, including local generator
control. The existing GLOBAL n^2(log n)^4 C_0 key/body structural bound
therefore costs O(n^3(log n)^4 C_0)=O(n^4 C_0). Counter updates use full
word helpers, at most O(n C_0) events. Measure each output item-code field
into one staged word and commit its actual field with a full helper:
w fields cost O(n^3), not a helper per measured bit. Unused sorted-key/
private-seed outcomes are measured/reset and discarded; no growing
transcript is stored. Required ticket/code fields use the same staged
word rule. All initialization, measurement, reset and actual output-field
bits remain charged. There are at most Cin requests per chunk and sum
Cin=O(n C_0), so mapped interfaces/postprocessing cost O(n^4 C_0).

Decoder word work is specified in short_interface.md.
