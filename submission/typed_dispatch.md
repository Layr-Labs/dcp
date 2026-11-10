# Typed physical dispatch, cursor emission and bit microprograms

This file specifies the ordinary mapped controller and its helpers. The
current native_ops.md adds fixed-word pool macros and native LE, with a
weighted ledger; the mapped product bound below remains a valid looser
upper bound where that implementation is retained.

A structural step is an individual Boolean bit operation, classical read
or write, emitted gate, measurement or reset, including source emission.
Full data arithmetic is its bit-serial program, not a unit-cost step.
The current frame has fixed pc, parent, continuation and scalar/array
binding fields as prescribed in proof.md Section5. For a mapped dispatch,
READWORD its pc and constant many operand/loop/binding fields; resolve
the bounded-arity operation and actual slots with their full helpers;
execute it; WRITEWORD changed local fields and pc. Finite procedure code
has at most2^12 fields and finitely many pc cases independent of n;
numeric loop positions are field values. No variable-size table or open
ancestor chain is read to resolve an operand. READWORD executes its
inline RAW stream, not a recursive interpreter call per transferred bit.

CALL writes the fixed continuation and child parent/arguments/entry,
then changes current id. RETURN commits fixed result/parent pc, frees
one child and restores current. ABORT walks parents with prescribed
cleanup. All fields commit before calls, returns, owner activation and
epoch fallback. Source recursion frames stay banked; no ordinary stack
or cache surviving a frame/epoch boundary is assumed.

The complete-helper bounds proved below include every stored bit and
address fee. Other staged physical-address formation uses O(A^2)
Boolean steps, each paying O(A), hence O(A^3)<=O(n^2). Source n-bit label
multiplication is still its own reference bit algorithm; it is not hidden
inside physical-address arithmetic. Calls and wire events have the
linear counts in proof.md (L1),(L3). Ordinary mapped work therefore has
T<=c n^2(C_S+HQ+1)+c n^3 Qcap+c n^2 DRAW, before the separately specified
native/word refinements. Prefix initialization, all resets, failures and
source moves are included. Exact epoch fallback handles exceptional
finite lengths. This dispatch preserves the decoded state invariant,
because it performs the same operation and commits the same fields.

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

The current physical cost uses native_ops.md's complete weighted ledger.
The cursor formats above remain its reference representation; all physical
resolutions and actual stored fields remain charged there.

## Persistent complete physical address buffers

This is the current inline helper implementation. It retains every RAW
operation and decoded field, but uses the already constructed address as
the indexed primitive's input rather than copying it into a fresh delivery
word at every bit. Let d=ceil(log2(4h+2^22 n+8)) as in short_interface.md.
It upper-bounds the COMPLETE allocated-address width and is Theta(r).

Use constant many ordinary d-bit argument registers, one per bounded
operand role. Initialize ALL bits before the first access. An indexed
bit access, gate or measurement consumes its designated complete argument
and is charged d bit operations for that address, including its reading/
decoding; this is the mandatory addressed primitive of rules.md, not
a zero-cost word read. Every change to the argument is computed and
written bit by bit, with the full address fee charged to each indexed
bit operation as well. The completed argument register IS the delivery
buffer. There is no extra word-copy instruction between an unchanged
argument and that same indexed primitive. Different operands use distinct
constant-many buffers. No address bits or padding are omitted. No word
arithmetic, coherent indexed memory, instruction oracle or parallel work
is introduced. The controller program and register roles are finite;
their bit storage is included in ordinary O(n) staging.

The RAW primitive remains measurement of wire2j for a basis read, and
measurement followed by conditional X for a write. Both pay complete
wire-address fees. A stream initializes its complete first wire address
and then increments that buffer by2 between RAW cells. Ripple carry
inspects/changes at most2L+d bits over L increments from ANY starting
address. Use explicit binary position control costing O(log(d+1)) per
inspected bit, including reset of its short position counter. The complete
stream control therefore costs O((L+d)log n) elementary bit operations,
each charged O(d). Initializing the full buffer costs O(d^2 log n),
included in O(d(L+d)log n). The final iteration stops before accessing a
successor, so addresses stay inside the prescribed field/row. Whole-word
overlap stages all source chunks before any destination write.

For reference cursor passes, the retained stronger carry-run account is
also valid: runs of length k occur at most L/2^(k-1)+1 times, and the
sum of squared run lengths is O(L+q^2) for q-bit counters. Thus a complete
t-bit relative pass with q=ceil(log2(t+1)) has O(t+log^2(t+1))=O(t)
generation, as used by the tree/decoder. To see the boundary term, take
aligned blocks of length2^b with b=ceil(log2(L+1)). The interval meets at
most two blocks and crosses at most one boundary. Inside those blocks
the squared-run sum is bounded by two complete b-bit cycles, O(2^b)=O(L);
the one higher carry contributes at most O(q^2). Physical streams above
use the conservative logarithmic position-control bound instead. Loop
counter initialization, comparisons, carry/borrow and all buffer-bit
accesses are explicit bit code, never a unit-cost growing integer step.

## Row arithmetic and complete helpers

For logical row R=o*ROWS+i, ROWS is a power of two. Form R by shift/copy
and addition. Its RAW base is (WROW+EW)R. The multiplier WROW+EW=
2^16 n+4r has O(log n) bits. Schoolbook multiplication therefore takes
O(d log n) Boolean bit steps, not d^2 steps with two arbitrary operands.
Giving EVERY step its d-bit fee and a conservative O(log n) local-index
control allowance yields O(d^2(log n)^2)=O(n(log n)^2).
Field offsets and the physical even-wire conversion have smaller cost.
Owner/row ids and all intermediate addresses retain their full d-bit
representations. Geometry is staged once per scope as specified for the
native interface; this is not a shortened read of its full stored fields.

Comparing every EW tag bit and reading/writing every stored L-bit field
costs O(n(log n)^2+d(L+d)log n). For L=O(r), a valid-row short helper
therefore costs O(n(log n)^2). For L=O(n), a complete word helper costs
O(n^(3/2)log n), since log n<=sqrt n on the main branch. A first write
STILL clears ALL WROW=2^16 n cells, stamps the complete tag and writes its
field: O(n^(3/2)log n). Row capacity, unused cells and logical zeros are
unchanged. Each actual padding bit in an n-bit field is transferred.
Short packed fields touch only their declared positions.

Persistent n-bit head/virgin/NEXT fields use the same full RAW streams.
Their offset multiplies a slot id by n, another O(log n)-bit stride.
ALLOC_Q/FREE_Q and descriptors use fixed many complete helpers plus
bit-serial addition. ALLOC_OWNER scans all flags, updates all EW epoch
bits and writes eight full n-bit binding fields. Each costs
O(n^(3/2)log n). First-row initialization and stale-tag handling are
included. Native/word macros commit before owner activation, call/return,
abort or exact renumbering, preserving their scoped caches. Long-lived
data/frames remain banked.

Other mapped-controller address arithmetic may conservatively use two
d-bit schoolbook operands: d^2 steps, each paying d and O(log n) control,
cost O(d^3 log n)=O(n^(3/2)log n). Complete n-bit staged copies, pc tests,
adds and compares fit this bound. Source label multiplication remains
its counted reference bit algorithm, not one helper. Each mapped
structural/frame/wire event thus costs O(n^(3/2)log n).
The original source transfers and native entry/exit still perform O(n)
full slot operations per copy, now O(n^(5/2)log n) in total, including
actual source/SWAP fees. No change to their decoded representation is
needed. Prefix preparation/cleanup may KEEP O(n^2 DRAW), and polynomial
bootstrap/guard work stays charged. Exact finite epoch fallback is retained.
The resulting valid mapped upper bound is
 T<=c n^(3/2)log n(C_S+HQ+1)+c n^(5/2)log n Qcap+c n^2 DRAW.

## Native operand buffers and weighted total

The fixed native regions use slots below P=2^22 n^3. Let
B=ceil(log2(4P+8))=O(log n). All their odd wire indices are below2^B;
P<=U and HQ=2^20U<=h ensure2^B<=h. Initialize the complete d-bit
operand buffers, including every high ZERO, once per native scope.
Only the low B bits then change with the polynomial-width register
cursors. Updating/copying them, including local uniform generation,
uses O(log n) explicit bit steps per native elementary step; each pays d.
The gate STILL consumes its entire correct d-bit buffer and pays d.
High bits stay available and correct; they are not regenerated or ignored.
Thus native elementary work costs O(sqrt n log n). Ordinary native
workspace indices are polynomially bounded and use the same argument.

For an old mapped slot used at native entry or by Shift_c, initialize
ALL d address bits from its complete stored slot value with the helper
charges above. Shift's control address stays fixed through that transform.
Each source-data entry SWAP and eventual old-slot release is paid; n of
them fit O(n^(5/2)log n) per copy. T1 modular multiplication, T2 shifts,
cheap QPE and verification have their retained O(n^2) elementary count;
native work is O(n^(5/2)log n) per call. Exact RUN has the extra h_e,
whose global cap gives the same aggregate O(n^(5/2)log n Qcap)+poly(n).
The compiler's logical bit-step guard, estimator modes and error proofs
are unchanged. Native FW's global n^2(log n)^4 C_0 structural count costs
O(n^(5/2)(log n)^5 C_0)<=O(n^3 C_0): for t=log2 n>=40,
t^5/2^(t/2) decreases and its endpoint is below100.

The short interface now costs O(n(log n)^2) per valid short field/input,
so w=O(n) fields and sum Cin=O(n C_0) give O(n^3(log n)^2 C_0).
Full first clears and complete binding refreshes are additionally paid
and smaller. Full-key dictionary visits, decoder word operations and
mapped tree steps use the complete-word bound above. Consequently the
current weighted ledger is
 T<=c[n^3(log n)^2 C_0+n^4 log n 2^(H+dl)
       +n^(5/2)log n Qcap+n^2(HQ+DRAW+1)]+poly(n)
  =O(n^(45/4)(log2 n)^2 2^((7/6)sqrt n)).
All state correspondences, exact source/instrument laws, caps, ordinary
storage margins and the full allocated prefix are unchanged.
