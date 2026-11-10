# Typed current-frame dispatch and physical work (normative bank implementation)

This file refines the controller implementation of proof.md Sections5,9.
The reference program, emitted circuits, current-frame layout, physical
bank layout and helper algorithms are unchanged. Fetch a controller word
with the existing READWORD/WRITEWORD helper, rather than treating each bit
of that fetch as a new recursive interpreter dispatch. This distinction
allows the cost proof below. All helpers are fixed inline bit-serial code;
none invoke the current-frame interpreter for their own implementation.
Their bits, generation and physical address fees are counted directly.

## One semantic dispatch

A structural reference step in C_S is a single Boolean bit operation,
classical bit read/write, emitted gate, measurement or reset, including
uniform emission work and explicit wire initialization/release resets.
Classical data-word arithmetic is the bit-serial reference code: it is
not one constant-time semantic step. Wire events and frame calls/returns
have the separately proved linear counts in proof.md (4.3) and (L1).

For each such dispatch:

1. READWORD the current pc and the finite fields containing its operand
   bindings, loop indices, scalar references and local owner ids. Each
   word is a fixed field of a current-frame row or a fixed binding record.
   Dispatch is a finite program-counter switch. It has at most a fixed
   number of tests, since the source program is fixed, independent of n.
   Bit-loop positions are numeric field values, not extra pc cases.
2. Compute the classically known operand addresses in staged words.
   Read any required fixed binding/slot descriptor fields with their
   existing word helpers. A logical classical bit operation then uses
   at most three logical input bits and one output bit, with READ/WRITE
   as in proof.md. A mapped quantum operation resolves its constant
   number of operands and emits that actual operation. A staged Boolean
   operation accesses its specified staged bits. No arbitrary word-valued
   data function is silently included in this case.
3. WRITEWORD only the fixed changed loop/local fields and pc, leaving
   other fields untouched. If a local numeric operation is a reference
   n-bit arithmetic algorithm, its individual bit operations are the
   next semantic steps, counted in C_S. Inline controller arithmetic
   used only for physical addresses is charged separately below.

The number of complete fields fetched/written is bounded by an absolute
constant for each dispatch. Each reference operation has bounded arity,
and the program has a fixed number of local variables/operand roles.
Even scanning the finite list of at most2^12 scalar fields instead of
using a particular pc's shorter operand list would multiply by an
absolute constant, not by n or recursion depth. Each field lies in a
single row. No stage loads a variable-size table or copies a binding map.
Array data are accessed only through the actual semantic READ/WRITE.
Reading n bits of one frame field performs n inline RAW operations,
not n calls each costing an entire word helper.

CALL writes the fixed continuation fields, activates one frame owner,
writes its fixed argument/local/parent fields and changes current id.
RETURN reads/writes its fixed return fields, changes the parent's pc,
frees one child and changes current id. The fixed number of fields per
source procedure makes their word-helper count constant too. ABORT walks
remaining parents with the existing event bound and prescribed cleanup.
No operation walks every ancestor to resolve an operand. It is sufficient
to reload these fields on every dispatch; no cache invariant or delayed
writeback is needed. All fields are committed before calls, returns,
abort or an epoch-renumbering fallback.

## Typed cost instead of the worst-instruction product

Retain the conservative helper bounds of proof.md (L2): each bank bit,
word, descriptor, owner and RAW-metadata helper costs O(n^2 log n),
including all physical fees. A constant number per dispatch therefore
costs O(n^2 log n). This already counts the full n-bit frame/slot fields,
row-tag comparisons and possible first-write clearing. It does not claim
that a word read is unit cost or that only the meaningful low address
bits are transferred.

Other controller work uses staged bits, not a word helper per bit.
Let A be the complete physical address width of proof.md Section8,
A=O(sqrt n). The existing physical-address roles use A-bit arithmetic;
data fields retain their full n-bit encodings. Row/owner/slot bounds and
the bank invariant ensure their interpreted indices fit A bits, even
though reading their stored n-bit fields costs the full word helper.
A row base or binding address takes O(A^2) staged Boolean operations by
schoolbook arithmetic. Give each its address fee O(A) and an additional
conservative O(log n) uniform-index allowance. The resulting
O(A^3 log n)=O(n^(3/2)log n) is below O(n^2 log n). Address copies,
constant-arity tuple decoding and n-bit pc/field comparisons are also
below it. The RR-view grouped prefix computation uses O((log n)^3)
bit operations and fits after the same fee/index allowances. FW's
incremental RR cursor can alternatively supply it directly.

A source-data label multiplication is not physical address arithmetic:
its n-bit schoolbook algorithm has its own counted reference bit steps.
No n-bit data multiplication is inserted into a supposedly constant
controller dispatch. Similarly a comparison/search of a variable-size
reference table is the reference loop already charged in C_S, not a
scan over all possible operands by the controller. These distinctions
are why the staged-work bound uses A^2 for address multiplication without
changing the widths or costs of data-table arithmetic.

A mapped gate/reset itself pays its physical quantum-wire address fee;
its constant descriptor reads and physical slot computations are among
the above helpers. Staged-only Boolean operations are cheaper than a
word helper. The ordinary controller holds only constant many O(n)-bit
staged words and current-frame id. Banked frames retain all growing
recursive contexts, as in the original implementation.

It follows that each reference structural step, frame event or ordinary
wire event costs at most O(n^2 log n) charged work. This is a typed sum:
a constant number of expensive word helpers plus O(A^2) cheap staged
Boolean operations. Multiplying O(n log n) controller instructions by
the maximum possible whole-word-helper cost would give a valid looser
bound, but is unnecessary for this specified inline implementation.

## Total cost and preserved semantics

Frame events number O(C_S+Qcap+poly(n)), by the retained demand/removal
argument in proof.md (L1). Wire events number O(C_S+nQcap), by (4.3).
Source transfer still has n+1 slot operations and the source/SWAP fees,
so all acquisition work is O(n^3 log n Qcap). The prefix initialization
and cleanup bound O(n^2 DRAW) is unchanged. Polynomial bootstrap is
absorbed by HQ or prefix preparation, as before. Thus beyond the fixed
no-wrap threshold the new precise bound is

 T <= c n^2 log n (C_S+HQ+1) + c n^3 log n Qcap + c n^2 DRAW.    (TD)

Every address fee uses A for the complete fixed allocation. The exact
terminating epoch fallback remains the implementation at exceptional
lengths; its finite set of bounded runs changes only absolute constants.
The logarithm of event/activation counts is still (7/6)sqrt n+O(log n),
so the EW=4r no-wrap proof is unchanged for all sufficiently large n.

Every inline fetch decodes the same current-frame field, and each
operation commits the same reference result before the next aligned
point. Therefore the decoded classical-quantum invariant of proof.md
Section7 holds without a change: source requests, gates, outcomes,
classical decisions and output law coincide. No new measurement, noise
promise or abort condition is introduced. Capacities, all allocated
qubits, ordinary staging and all probability bounds are unchanged.

For c=alpha=29/4 and e=7/6 the retained incremental structural bound is
C_S=O(n^(4+alpha)(log n)^2 2^(e sqrt n)). Substituting into (TD) gives
T=O(n^(6+alpha)(log n)^3 2^(e sqrt n))
 =O(n^(53/4)(log n)^3 2^((7/6)sqrt n)).
The source term has power 9/2+alpha=47/4, strictly smaller. HQ and DRAW
have leading exponential coefficient1<e and are absorbed. Q remains
O(n^(35/4)2^(e sqrt n)), S_C=O(n), S_Q=O(n^(-77/2)2^(sqrt n)),
and the exact tolerance object remains zero. This gain follows from an
explicit controller/helper implementation and does not rely on a prior
acceptance verdict or an uncharged memory operation.
