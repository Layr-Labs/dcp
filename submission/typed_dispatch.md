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

Use the inline physical-stream bounds proved in the final section and proof.md (L2): each bank bit,
word, descriptor, owner and RAW-metadata helper costs O(n^2),
including all physical fees. A constant number per dispatch therefore
costs O(n^2). This already counts the full n-bit frame/slot fields,
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
schoolbook arithmetic. Give each its address fee O(A) and the counted carry-loop control described below. The resulting
O(A^3)=O(n^(3/2)) is below O(n^2). Address copies,
constant-arity tuple decoding and n-bit pc/field comparisons are also
below it. All local quantum-register offsets use fixed polynomial-sized layouts.
The permutation-seed FW has no mixed-radix R_N view family.


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
wire event costs at most O(n^2) charged work. This is a typed sum:
a constant number of expensive word helpers plus O(A^2) cheap staged
Boolean operations. Multiplying O(n log n) controller instructions by
the maximum possible whole-word-helper cost would give a valid looser
bound, but is unnecessary for this specified inline implementation.

## Total cost and preserved semantics

Frame events number O(C_S+Qcap+poly(n)), by the retained demand/removal
argument in proof.md (L1). Wire events number O(C_S+nQcap), by (4.3).
Source transfer still has n+1 slot operations and the source/SWAP fees,
so all acquisition work is O(n^3 Qcap). The prefix initialization
and cleanup bound O(n^2 DRAW) is unchanged. Polynomial bootstrap is
absorbed by HQ or prefix preparation, as before. Thus beyond the fixed
no-wrap threshold the new precise bound is

 T <= c n^2 (C_S+HQ+1) + c n^3 Qcap + c n^2 DRAW.    (TD)

Every address fee uses A for the complete fixed allocation. The exact
terminating epoch fallback remains the implementation at exceptional
lengths; its finite set of bounded runs changes only absolute constants.
The logarithm of event/activation counts is still (7/6)sqrt n+O(log n),
so the EW=4r no-wrap proof is unchanged for all sufficiently large n.

Every inline fetch decodes the same current-frame field, and each
operation commits the same reference result before the next aligned
point. Therefore the decoded classical-quantum invariant of proof.md
Section7 holds without a change: source requests, gates, outcomes,
classical decisions and output law coincide. The typed controller itself introduces no extra measurement, noise
promise or abort condition beyond the specified reference program. Capacities, all allocated
qubits, ordinary staging and all probability bounds are unchanged.

For c=alpha=29/4 and e=7/6 the current structural bound is
C_S=O(n^(7/2+alpha) 2^(e sqrt n)). Substituting into (TD) gives
T=O(n^(11/2+alpha) 2^(e sqrt n))
 =O(n^(51/4) 2^((7/6)sqrt n)).
The source term has power 9/2+alpha=47/4, strictly smaller. HQ and DRAW
have leading exponential coefficient1<e and are absorbed. Q remains
O(n^(35/4)2^(e sqrt n)), S_C=O(n), S_Q=O(n^(-77/2)2^(sqrt n)),
and the exact tolerance object remains zero. This gain follows from an
explicit controller/helper implementation and does not rely on a prior
acceptance verdict or an uncharged memory operation.

## Counted cursor-role emission for classical record streams

The compiler emits finite READVAR/WRITEVAR opcodes with operands
(owner-role,row-role,field-format,bit-cursor-role). GATEVAR analogously
uses a finite register/owner role and a bit-cursor role for each of its
constant many operands. A cursor role is a named scalar field of the
current procedure, not its numeric value serialized into each gate tuple.
The finite program has fixed many roles. Each actual bit operation, gate,
measurement and reset is still executed. Cursor updates, branches and
initialization are explicit reference bit steps, included in C_S.

Before a field pass bind the source/destination row roles and initialize
the cursor fields. The finite physical controller resolves these roles by
reading their COMPLETE stored n-bit fields, including padding, and performs
all physical address formation, address delivery and RAW helpers. There
are constant many fields per bounded-arity operation. The inline helper
ledger below therefore still applies with O(n^2) per structural step.
This changes a source operand format, not the address fee or bank model.
No quantum-addressed table load, free word increment or free row lookup
is supplied. The decoded invariant erases the transient old literal tuple;
resolving the roles yields exactly its operand indices and same operation.

Use the carry-overflow loop below also for reference bit cursors. Its
fixed control states choose the next bit operation directly. Total cursor
updates and carry-control work for a length-L pass are O(L+(log n)^2),
including initialization and restoration. Multiple operand cursors have
constant arity. For reversed passes subtract one with the mirrored borrow
loop; it has the same aggregate count. Finite opcode/role tuples have
constant bit length independent of n, so their emission costs O(1), with
numeric cursor-field changes counted separately. A branch or call commits
these cursor fields before changing frames. No growing instruction list
or hidden ordinary recursion stack is stored.

All overlap rules remain: stage an entire source field before writing
its overlapping destination; three-n-bit labels use a fixed three staged
chunks. The constant O(n) staging margin counts these complete words.
Binding a pool row copies its meaningful Y_i bits explicitly, and a
length-L field costs O(Y_i+L+(log n)^2) structural bit operations. For a
full n-bit key/label this is O(n), since Y_i=O(r). For GROUP identifiers,
L=Y_i and w=O(n); even allowing O((log n)^2) initialization for every
one gives O(w(Y_i+(log n)^2))=O(n^(3/2)) per request. This bound does
not require a lower bound on an individual Y_i. Short flags are charged
to the same complete key-record visit. An AVL visit costs O(n), including
its full key, row bindings, pointers and counts. O(log Cin)=O(r) visits
per search/update and O(Cin) total such operations cost O(n^(3/2)Cin).
Consumed-label streams cost O(n Cin), using the unchanged sum-rho bound.
Cleanup, empty/partial streams and metadata initialization are included.

Thus non-key pool work is O(n^(3/2)Cin) per chunk and O(n^(5/2)C_0)
globally. Private key/body sorting retains its old, fully counted emitter
and GLOBAL O(n^2(log n)^4 C_0) bound. For t=log2 n>=40,
t^4/2^(t/2)<=40^4/2^20<3: its logarithmic derivative is
4/t-(ln2)/2<0. Thus that work also fits O(n^(5/2)C_0). This is a
GLOBAL cap argument, not a per-chunk retry-work assertion.
verified_extract.md and approx_estimate.md specify the same cursor-role
format for the linear ripple passes, with aggregate LE work
O(n^2 Qcap)+poly(n). The unchanged tree/decoder terms then give
C_S=O(n^(7/2+29/4)2^((7/6)sqrt n)). The inline physical bank yields
T=O(n^(51/4)2^((7/6)sqrt n)). All storage, source, error-model and
probability objects are unchanged.

## Inline physical bit streams with carry termination

The physical helper refinement in this section sharpens the helper bound;
it does not itself change C_S or the quantum circuit. The cursor-role
source refinement above supplies the separately proved current C_S.
These are fixed finite microprograms executed directly by the physical controller,
not a list of microinstructions stored in the bank and not recursive semantic
dispatches. Numeric bit positions and physical addresses are staged binary
words. The full address fee is charged on every elementary operation. No
word addition, comparison, address generation or indexed access is free.

Here is the loop implementation used for every fixed-length physical stream.
For a length L>=2 set q=ceil(log2 L), initialize a q-bit remaining counter to
2^q-L, execute one body operation and ripple-increment that counter, stopping
on its overflow carry. L=1 is one body execution. Thus exactly L bodies run.
There is no q-bit endpoint comparison at every iteration. The initial counter
is computed bit serially from the staged length, in O(q^2) bit operations;
its initialization is outside the stream. During L increments the total
number of examined/flipped counter bits is at most 2L+q. Each physical bit
address cursor advances by one with the same ripple procedure, whose total
bit work is at most 2L+A, including an arbitrarily aligned starting address.
The top carry is a separate staged bit and is not silently discarded.
Control follows fixed program states for the carry bit and current bit position.
The bit position within a ripple is itself advanced by a ripple counter; its
aggregate cost over all carry runs is O(L+A^2), not a full binary comparison
per address bit. One can verify this by summing over runs: runs of length k
occur at most L/2^(k-1)+1 times, and sum k^2/2^k is finite; the single boundary
run contributes O(A^2). Nested loops use the same construction at each level.

A RAW operation has an already staged A-bit physical address. If the target
instruction format requires a separate address buffer, copy all A bits with
this stream program, then deliver that complete buffer to the indexed physical
operation. The buffer-copy work is O(A) elementary bit operations plus O(A)
initialization (or O((log A)^2), which is smaller). Each such operation pays
its own address fee O(A); the indexed operation also pays its O(A) address
fee. Hence a RAW access costs O(A^2), including preparation and delivery.
Address-delivery buffers themselves are ordinary staged words at fixed
polynomially bounded ordinary-memory positions. Their local bit cursor
has width O(log n), so traversing A buffer bits costs
O(A+(log n)^2)=O(A) elementary steps, including carry-control boundaries.
Each of these steps still pays the complete-allocation fee O(A). This
local-buffer fact is not an assumption about bank-target address width.
An indexed operation here is precisely the bit-memory or quantum-wire primitive
of the charged model with its address supplied explicitly. It is not a
quantum indexed load: every address is classical. RAW_READ measures the
basis-state cell; RAW_WRITE measures then conditionally applies X. Its law
and its handling of zero cells are exactly the retained bank implementation.

The controller does not first serialize the numeric position into a literal
instruction string for every internal bit. Its finite microprogram directly
executes the indexed primitive using the staged pointer and pays the full
address fee above. Structural circuit emission uses the separately specified cursor-role
format above; this physical microprogram proof does not assume its
address delivery is free. The finite physical program, staged pointers,
carry bits and loop counters occupy constant many O(n)-bit ordinary words.
It has no growing ordinary stack, no oracle instruction, no packed unit-cost
arithmetic, and no extra quantum storage. A stream that copies an overlapping
field first stages its entire source word, as already required for field-role
streams. The constant staging margin includes these complete n-bit words.

For the main branch r/2<=A<=c r for a fixed c, from the fixed allocated prefix
and cb=floor(sqrt n)-40ceil(log2 n). Also (log2 n)^2=O(A). Initializing length,
field offset and cursor controls therefore costs O(A^2) elementary bit work
at worst, or O(A^3) after address fees. This is below O(n^2). Streams whose
length is A, EW or a fixed multiple of n use the same code. A field crossing
a prescribed fixed boundary is split into a constant number of streams;
no helper crosses an unbounded number of rows.

Schoolbook A-bit row-base/address formation uses its explicit nested bit
loops. Each outer iteration initializes the inner cursor once and scans at
most A bits. There are O(A^2) Boolean/cursor operations in total, including
carry addition and initialization; the carry-sentinel loops avoid an extra
logarithm. Giving every operation its complete O(A) fee yields O(A^3).
Full n-bit staged data copies, increments and comparisons cost at most
O(nA+A^3), with any source-level data arithmetic still separately in C_S.
The finitely many pc cases are fixed control states, not growing lookup tables.

The resulting helper ledger is explicit. A row tag comparison reads EW=O(r)
bits, costing O(r A^2+A^3)=O(n^(3/2)). A first write clears all WROW=O(n)
RAW cells, stamps all EW tag bits and performs the requested write, costing
O(n A^2+A^3)=O(n^2). A READWORD/WRITEWORD visits every one of its at most n
stored bits, including padding, and performs one row validation/initialization;
it therefore also costs O(n^2). Direct head/virgin/NEXT metadata streams
read and write every n-bit field at this same cost. ALLOC_Q, FREE_Q and
slot descriptor updates use a fixed number of those full-field helpers plus
staged arithmetic. ALLOC_OWNER scans all O(r) flags, increments/copies every
EW epoch bit and writes the fixed eight complete n-bit binding fields; its
cost is O(n^2) as well. A mapped gate resolves its complete physical slot
fields with the same constant helper count and pays its actual gate fee.
Initialization/release wire resets, descriptor maintenance and frame
call/return events are charged, with exactly the retained event counts.

Consequently each structural dispatch, frame event and wire event costs
O(n^2), and one acquired source still incurs n+1 complete slot operations
and actual source/SWAP fees, costing O(n^3). This proves the refined bound

 T <= c n^2 (C_S+HQ+1) + c n^3 Qcap + c n^2 DRAW.             (TD-inline)

Prefix clearing keeps its old O(n^2 DRAW) bound. Bootstrap and the guarded
rotation compiler retain all their bit-operation and storage charges;
their fixed polynomial setup is absorbed by the existing prefix/HQ terms.
The numerical guard counts logical compiler bit operations as before and
therefore selects exactly the same deterministic estimator mode. There is
no new success event, failure cutoff, source request or circuit approximation.
Each stream performs the same physical accesses in the same logical order,
so the decoded invariant and all joint error bounds are retained. Exact
renumbering at exceptional lengths is unchanged, with its finite-length
cost absorbed only in the absolute constants as in the parent.

Substituting the current C_S=O(n^(7/2+29/4) 2^((7/6)sqrt n))
into (TD-inline) gives T=O(n^(51/4)2^((7/6)sqrt n)). Source work has
smaller polynomial power 47/4, and prefix work has smaller exponential
coefficient. The other four structured objects are identical to the parent.
