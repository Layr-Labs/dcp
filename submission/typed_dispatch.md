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

## Complete physical buffers

The d-bit argument registers ARE the delivery buffers consumed by the
addressed primitive. All bits, including high zeros, are initialized and
available; every access pays the complete d fee and each changed bit is
charged. Different operands have distinct constant-many buffers. RAW
reads measure wire2j, RAW writes measure then conditionally X; quantum
slots use wire2k+3. Every field/tag bit is transferred. Stream overlap
stages all source chunks before writing. The final section replaces
conservative position-control costs for long streams and regular passes;
tagged short rows use the aligned complete-address bounds below.

## Full-width exact product retained for source arithmetic

This kernel is independent of physical RAW row strides. Pad full-width
operands to b=3^k, the least such power >=3n, so b<=9n.
Here is the unsigned product of two unsigned w-bit integers. For w<=8
use bit-serial schoolbook multiplication. Otherwise m=ceil(w/3) and
a=a_0+a_1*u+a_2*u^2, e=e_0+e_1*u+e_2*u^2, u=2^m, with zero-padded
top digits. Evaluate at0,1,-1,2,infinity and compute five products:
 v_0=a_0 e_0, v_inf=a_2 e_2,
 v_1=(a_0+a_1+a_2)(e_0+e_1+e_2),
 v_minus=(a_0-a_1+a_2)(e_0-e_1+e_2),
 v_2=(a_0+2a_1+4a_2)(e_0+2e_1+4e_2).
Each factor's magnitude is below7*2^m, so recurse on unsigned magnitudes
of width w'=ceil(w/3)+3, retaining the sign separately. Write c_0=v_0,
c_4=v_inf, and perform exact interpolation:
 A=(v_1-v_minus)/2,
 c_2=(v_1+v_minus)/2-c_0-c_4,
 D=(v_2-c_0-16c_4)/2-2c_2,
 c_3=(D-A)/3, c_1=A-c_3.
Return sum_(j=0..4)c_j u^j. Expanding the two degree2 polynomials gives
A=c_1+c_3 and D=c_1+4c_3, proving these identities and divisibility.
Signed additions/shifts use bit code with extended precision, e.g.
8w+64 bits for a temporary; input range proves the final product fits2w.
Division by2 copies shifted bits. Division by3 scans bits left to right
with remainder0,1,2: append a bit, compare/subtract3 if necessary, emit
one quotient bit. This is O(w) bit work with fixed-size remainder logic,
not a division oracle. Interpolation divisions have zero remainder.

The rounded child size is accounted for: for w>8,
w'-6=ceil(w/3)-3<=(w-6)/3. Recursion terminates at w<=8. At root b=3^k,
height is at most k+2; widths at level j are at most6+b/3^j.
Five-child traversal with O((k+1)^4) local phase/index overhead therefore
costs O((k+1)^4 5^k) bit steps. Since5^2=25<27=3^3, group k=2h+i:
polynomial(h)*(25/27)^h is bounded. The full unsigned product costs
O(b^(3/2)), with absolute constants and all private control included.

Use a depth-first ordinary worklist with <=1024w data bits per frame
and1024(k+1) phase/offset bits. The active width sum is <=4b because
w+4(ceil(w/3)+3)<=4w for w>=9. Thus data<=4096b<=36864n;
metadata1024(k+2)^2<=2^14 n eventually. The guarded2^16 n ordinary
worklist fits both, with all fields written before use. Initialize/clear
it once per ENTIRE product, never per recursive node. The native clean
SSA variant records all Boolean results, copies outputs and reverses
the WHOLE network once. native_ops.md proves its exact channel, guarded
used-qubit layout and full physical-driver bound O(n^2); source recursion
remains banked. No physical row multiplication depends on this lemma.

## Power2 physical rows and complete scoped helpers (normative)

This changes physical RAW placement and its microprogram, not logical
records, source laws, measurements or classical algorithm decisions.
Keep the logical WROW, ROWS, OWN, HQ, P, U, epochs and bank interfaces.
Logical c=R*WROW+j and LSPAN=LROWS*WROW remain mathematical logical
identifiers; they are not materialized numeric operands of the current
row-role emitter. Actual READ/WRITE takes (owner,row,field,bit) roles.

Put s_R=ceil(log2(WROW+EW)), S_R=2^s_R. Physical row R=owner*ROWS+row
has RAW base R*S_R, VALUE bit j at base+j, TAG bit t at base+WROW+t,
and unused padding through base+S_R-1. ROWS is already a power2;
owner/row and zero low stride bits concatenate to form row addresses.
No long-by-short product by WROW+EW is used for a tagged row.
Other RAW metadata starts at RSPAN=LROWS*S_R; preserve its previous
relative order and sizes. Thus
 DRAW=RSPAN+n(HQ+2)+(OWN+8)EW+OWN+2^20 n^4.
h is the least power2 >=max(DRAW,HQ+2), and
d=ceil(log2(4h+2^22 n+8)) is the complete delivered address width.

proof.md Sections4/8 establish DRAW<=2DRAW_old and h<=2h_old,
including all new padding and unchanged metadata/native capacities.
RAW even wires2j and quantum-slot odd wires2k+3 are still disjoint;
the external acquisition register is placed beyond the new prefix.
Every such physical address is formed/delivered in full. d differs
from the old width by at most2 and is Theta(r), with d<n on the main
branch. LIVE uses this exact updated d-bit stored format, with the
same full n-bit import/export. No array, logical owner or slot cap grows.

For every first write to an invalid row, clear ALL S_R raw cells,
including values/tag/padding, then write its correct epoch and field.
This O(n)-length clear costs O(n^(3/2)); it occurs only on the actual
first write of a row in that activation. A valid row write preserves
all other fields/padding. Reads compare the complete tag and return
zero for an invalid tag. The same row-lazy induction is exact.
Renumbering scans the same logical tags and rewrites them at their new
addresses. Unused padding is counted whether or not later touched.

### Scope-local epoch and short-value staging

At entry of a fixed helper/dictionary/tree/native scope, load the
complete active flag, epoch and prescribed full binding fields for
its constant-many owners. Epoch caches have ACTUAL EW-bit ordinary
formats and are charged O(r) bits per owner. This explicitly replaces
the previous convention that an epoch was never staged as a word.
At most2^12 cache roles use2^14 r bits, inside the existing2^20 n
ordinary margin together with compiler/arithmetic/LE blocks.
These caches are valid only while no owner activation/free/renumbering
occurs. Commit frames and invalidate all caches before any such event,
external call/return or abort; reload at the next scope entry. Global epoch
records remain their counted basis-state RAW words. No epoch check
or active-owner read is omitted: complete entry loads cost
O(n^(3/2)) per scope and are already in the current binding ledger.
They are not repeated for each visited dictionary node.

Stage short fields/tag comparisons in actual D=16r+64-bit ordinary
roles, clearing all D bits before reuse, rather than clearing an n-bit
padding word per short field. All current short formats fit D: LIVE d,
metadata Y_i, tree D_T, keys c and epoch EW. Their logical decoding
zero-extends; full n-bit consumers/import/export use the retained
complete-word helper. Full labels and frame fields keep their full
formats. This is an explicit storage/control format, not reading only
a useful prefix of an unchanged n-bit record.

For a complete MERGE activate all fixed-role owners BEFORE entry and
keep them active through sorting/listing and native arithmetic; helpers
are inline. No full binding reload occurs per comparison or heap node.
Temporary resets overwrite complete used fields or scan their logical
bounds, O(L+Cp) at each constant stream restart; Cp=O(L), since kappa
is fixed. Sort records are fully overwritten before reuse. These scans
and first clears are included in record counts. At most128 preactivated
roles fit the stated owner margin; source/tree calls occur outside scope.

### Actual bit loops and address charges

Ordinary fixed helper strips and short/argument roles are power2-aligned
within the existing staging margin. Their complete physical-bit-address
buffers retain initialized high zeros; only their polynomial-width low
indices vary. A contiguous t-bit copy/clear pass has relative-counter
width q=O(log(t+1)), with squared carry/borrow work O(t+q^2).
For t=d or D=Theta(r), this is O(r), since log^2 n=O(r).
Every actual bit read/write and changed argument bit pays the complete
d fee. Constructing ALL d bits of a bank operand therefore costs
O(d^2)=O(n), not a free word copy. Scope entry first reads the complete
old n-bit bindings, then stores their bounded owner/index geometry in
the explicit short roles; no n-bit field is silently truncated per node.

Form R by concatenating owner and row (ROWS power2), append s_R zeros,
and add the field/tag offset, whose width is O(log n). Its bit-serial
schoolbook additions cost O((log n)^2) raw work, charged
O(r(log n)^2)=O(n). No division by WROW is performed: logical flattened
c is only a proof identifier and actual row roles supply R,j directly.

For the RAW field stream, S_R is a power2 and the whole field lies
within one row. Hence the owner/row coordinates of wire2j stay FIXED;
only q_R=s_R+1=O(log n) low wire bits carry. For ANY starting field
offset a length-L stream has squared-run work O(L+q_R^2), with the
existing explicit carry/borrow microprogram; stop before leaving its
field. Crucially its boundary term is q_R^2, not d^2, because actual
row alignment prevents a carry into the high row coordinates.
All high bits remain present in each complete argument consumed.

A short field or full tag has L=O(r); its raw stream plus staging and
epoch comparison cost O(r+log^2 n)=O(r). Complete d-bit initialization
adds O(n) charged work as above. Thus a VALID short helper costs O(n),
including every stored bit/tag/address/control operation. A full n-bit
field or first S_R-bit clear costs O(n^(3/2)). Persistent allocator and
binding regions retain their original fixed layouts: their general
d-bit schoolbook address arithmetic costs O(d^3)=O(n^(3/2)) and their
full-word streams fit the same bound. They are not mistaken for aligned
tagged rows. Epoch/active-field entry loads may also keep that full
bound, once per scope. Source full-width Toom arithmetic is unchanged.

### Decoding, whole space and current total

The bank decoding maps each new padded physical row to exactly its old
logical values/tag; the row-lazy invariant, copying and renumbering
therefore preserve all classical-quantum states. Epoch caches are
deterministic copies of current basis words and are invalidated at
every specified boundary. All logical source, FW, merge, decoder and
cutoff decisions are identical. No physical address is a tie-break key.

The full-prefix bound is proved in proof.md Section8. Ordinary scope
caches fit the retained margin; source/private slots are unchanged.
Every fee uses new d and every prefix clear is counted. Epoch event
exponents are unchanged; exact renumbering still handles finite lengths.

The helpers give dictionary O(n^(3/2)Cin), hence O(n^(5/2)C_0),
and word-tree O(n^(3/2)) per record, hence O(n^3 2^(H+dl)).
native_ops.md supplies their exact record counts, source and slot work;
perm_fw.md gives the complete current pair/matching weighted total.

Full n-bit COPY/ADD/SUBTRACT/COMPARE use fixed forward/reverse word
passes with O(n) raw bit/control work, charged O(n^(3/2));3n labels use
three chunks and overlap stages all sources. A mapped dispatch uses
constant-many full helpers plus d^2 schoolbook address bit steps,
each paying d, so also costs O(n^(3/2)). CALL/RETURN commits full fields
with the same helpers; its event count is proof.md Section9.

