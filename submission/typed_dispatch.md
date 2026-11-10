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

## Exact blocked short-stride product

Use this exact row-base multiplier. Let S=WROW+EW=2^16n+4r, B=bitlength(S), and
b=2^ceil(log2 B). For t=log2 n>=40, B<=t+19 and b<=3t. Also d>=r/2,
so b<=d and b^2<=d for all main-branch lengths (the latter follows from
18t^2<=2^(t/2), true at40 and preserved by differentiation).
All strides n,8n and fixed metadata multiples are at most S and use
the same padded b-bit kernel.

Partition the d-bit row R into q=ceil(d/b) base-m digits R_j, m=2^b,
padding the final digit with explicit zeros. Carry C_0=0. In ascending j,
compute T_j=R_j*S+C_j, store D_j=T_j mod m, set C_(j+1)=floor(T_j/m).
Since R_j,S,C_j<m, T_j<m^2 and the next carry is again below m.
The invariant
 S*sum_(i<j)R_i m^i=sum_(i<j)D_i m^i+C_j m^j
proves the exact product. Store the final carry too. This needs O(b)
bit additions/copies per block; it does NOT add each partial product
across a d-bit accumulator. Output uses at most d+2b bits. Compute it
fully; valid RAW-layout bounds imply it fits the required d-bit address.

The unsigned b-bit product uses the exact three-product identity.
For b>1 put a=a_1*u+a_0, e=e_1*u+e_0, u=2^(b/2).
Compute z_0=a_0e_0, z_2=a_1e_1, and
z_D=|a_1-a_0| |e_1-e_0| with the separate difference sign.
Then cross=z_0+z_2-signed(z_D), and
ae=z_0+cross*u+z_2*u^2. The three recursive operands have EXACTLY b/2
bits; using differences avoids an extra input bit. Base b=1 is AND.
All signed additions, comparisons, shifts and copies are their bit code.

Execute depth first with an explicit private worklist: each frame stores
width/phase, its inputs, difference sign and retained partial results;
children return to that frame's next phase. Local workspace offsets have
O(log b) bits. Allowing even O((log b)^4) local bookkeeping per node/bit,
the bit count for b=2^k is O((k+1)^4 3^k). Since3^5=243<256=2^8,
group k=5m+j; (m+1)^4(243/256)^m is bounded. Thus the complete product
uses O(b^(8/5)) elementary bit steps, including its private control.

Reserve W=2^10 b^2 ordinary bits for this PHYSICAL arithmetic worklist,
counted explicitly inside the existing2^20 n margin. Active depth-first
frames have geometrically decreasing widths, and this generous W covers
all inputs/results/phase/offset records: word storage totals at most64b,
and phase/offset storage at most256(k+1)^2<=256b^2. Since b<=3t and9216t^2<2^t
at t=40 with decreasing ratio, W<=n on every main length. Source recursion
remains banked; this separately bounded arithmetic buffer is not an
uncounted source stack. Allocate W once. Initialize/clear its W positions only at the beginning
and end of the ENTIRE long R*S, never between digits or nodes. Each
reused frame writes its inputs/phase and every result before reading
them, within the counted short-product routine. No stale value is used.
The one O(b^2) clear fits O(d) by b^2<=d, with absolute constants.

Initialize complete d-bit argument buffers ONCE per whole R*S. Across
blocks and worklist phases reuse them, updating their polynomial-index
low bits exactly as in the persistent-buffer routine. Each elementary
bit step still pays O(d log n), including full address consumption and
generation. There is no full d-bit reinitialization per recursive node.
Block-index control and carry stores cost O(b) per block; workspace
clearing is already counted. Total raw work is
O(q b^(8/5)+d+b^2)=O(d(log n)^(3/5)).
Its charged cost is O(d^2(log n)^(8/5))=O(n(log n)^(8/5)).
Shift/add forming R and field/even-wire offsets cost O(n log n) and fit.

All complete n-bit helpers keep O(n^(3/2)log n). A valid short field now
costs O(n(log n)^(8/5)), including its unchanged tag and cursor streams.
The scoped interface therefore costs O(n^3(log n)^(8/5) C_0) globally.
Tree, native extraction/source transfers and other word work retain
their O(n^4 log n 2^(H+dl)) and O(n^(5/2)log n Qcap) allowances.
The complete final ledger is stated below.
The product is exact, so every accessed cell, quantum operation, source
request and outcome law is unchanged. No new cap or error event is added.

Complete tag/field streams retain their full persistent-buffer charges.
An n-bit word or first WROW-bit clear costs O(n^(3/2)log n); short fields
use the new row multiplier and cost O(n(log n)^(8/5)). Every stored
padding bit is transferred. Persistent head/virgin/NEXT offsets use
strides <=S and fixed full-word streams. ALLOC_Q/FREE_Q/descriptor
operations use constant many word helpers. Owner activation scans flags,
handles all EW epoch bits and writes eight complete n-bit fields.
Each costs O(n^(3/2)log n). No first initialization is omitted.

Remaining two-d-bit mapped address arithmetic may keep its schoolbook
d^2 bit steps with O(d log n) charges, within O(n^(3/2)log n) per mapped
dispatch. Source-data n-bit multiplication stays its reference bit code.
Calls, wire events, the original n+1 source slot moves, native-entry
SWAPs and release helpers retain their complete counts. All source work
fits O(n^(5/2)log n Qcap). Prefix preparation/cleanup may keep
O(n^2 DRAW); guarded compilation and exact epoch fallback are unchanged.

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

The short interface now costs O(n(log n)^(8/5)) per valid short field/input,
so w=O(n) fields and sum Cin=O(n C_0) give O(n^3(log n)^(8/5) C_0).
Full first clears and complete binding refreshes are additionally paid
and smaller. Full-key dictionary visits, decoder word operations and
mapped tree steps use the complete-word bound above. Consequently the
current weighted ledger is
 T<=c[n^3(log n)^(8/5) C_0+n^4 log n 2^(H+dl)
       +n^(5/2)log n Qcap+n^2(HQ+DRAW+1)]+poly(n)
  =O(n^(45/4)(log2 n)^(8/5) 2^((7/6)sqrt n)).
All state correspondences, exact source/instrument laws, caps, ordinary
storage margins and the full allocated prefix are unchanged.
