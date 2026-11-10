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
short fields retain their exact Toom and complete-address bounds below.

## Row arithmetic and complete helpers

## Exact three-way short-stride product

Use this exact row-base kernel with the retained complete address buffers.
Put S=WROW+EW=2^16n+4r, B=bitlength(S), and let b be the least power of3
at least B. For t=log2 n>=40, b<=5t. Since d>=r/2 and
50t^2<=2^(t/2) (endpoint40 and decreasing ratio), b^2<=d.
All smaller metadata strides use this same padded b-bit kernel.

Partition R into q=ceil(d/b) base-M digits R_j, M=2^b, padding the top
digit explicitly. Starting C_0=0, compute T_j=R_j*S+C_j, store
D_j=T_j mod M, and set C_(j+1)=floor(T_j/M). All digits and carries are
below M, hence T_j<M^2. The exact invariant
 S*sum_(i<j)R_i M^i=sum_(i<j)D_i M^i+C_j M^j
proves the final product after storing the last carry. Combination and
digit copies cost O(b) per block, not a d-bit addition per block. Compute
all d+2b possible result bits; RAW range bounds imply the address fits d.

Here is the short product of two unsigned w-bit integers. For w<=8
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
polynomial(h)*(25/27)^h is bounded. The full short product costs
O(b^(3/2)), with absolute constants and all private control included.

Use a depth-first ordinary worklist. A frame holds its phase/width,
evaluations, signs, five returned products and interpolation fields;
initialize every field before reading it. It needs at most1024w data
bits plus1024(k+1) phase/offset bits. The active width sum is <=4b:
w+4(ceil(w/3)+3)<=4w for w>=9, and the base case closes induction.
Thus data use<=4096b; phase/offset use<=1024(k+2)^2<=4096b^2.
Reserve W=2^14 b^2 bits, covering both. It is explicitly ordinary
physical-arithmetic storage; source recursion remains banked.
Since W<=409600t^2<2^t for t>=40, it fits inside the retained O(n) margin.

Allocate W once. Initialize/clear its used positions only before and
after the ENTIRE long R*S, never between digits or recursive nodes.
Reused frames overwrite inputs/phase/results before use. This O(b^2)
initialization fits O(d). Complete d-bit argument buffers are likewise
initialized once for the long product, then reused; every low-index
update and full address consumption retains O(d log n) charge.
Block-index control and carry stores cost O(b) per block.
Total raw work is O(q b^(3/2)+d+b^2)=O(d(log n)^(1/2)), hence charged
cost O(d^2(log n)^(3/2))=O(n(log n)^(3/2)). Forming R by shift/add and
the field/even-wire offsets cost O(n log n) and fit. Products are exact;
every cell address, quantum operation, source request and law is retained.

Complete n-bit helpers keep O(n^(3/2)log n); a valid short field now
costs O(n(log n)^(3/2)), including unchanged tags/cursor streams.
The final weighted ledger below uses this row-base refinement.

Complete tag/field streams retain their full persistent-buffer charges.
An n-bit word or first WROW-bit clear costs O(n^(3/2)log n); short fields
use the new row multiplier and cost O(n(log n)^(3/2)). Every stored
padding bit is transferred. Persistent head/virgin/NEXT offsets use
strides <=S and fixed full-word streams. ALLOC_Q/FREE_Q/descriptor
operations use constant many word helpers. Owner activation scans flags,
handles all EW epoch bits and writes eight complete n-bit fields.
Each costs O(n^(3/2)log n). No first initialization is omitted.

Remaining two-d-bit mapped address arithmetic may keep its schoolbook
d^2 bit steps with O(d log n) charges, within O(n^(3/2)log n) per mapped
dispatch. Source-data n-bit multiplication stays its reference bit code.
The preceding source import/slot ledger remains a valid larger bound;
native_ops.md explicitly replaces it by direct native entry/export and
the current fast source/preprocessing ledger. All actual calls, moves,
release helpers and complete argument bits are counted there. Prefix preparation/cleanup may keep
O(n^2 DRAW); guarded compilation and exact epoch fallback are unchanged.

## Amortized physical control (current refinement)

The complete physical-address input and its mandatory fee are unchanged.
This section replaces the conservative logarithmic position-control cost
for LONG full-word streams, mapped schoolbook address arithmetic and
regular native LE passes. Short row products retain the exact Toom kernel
and its O(n(log n)^(3/2)) bound. There is no new operation or free index.

For a d-bit argument increment by1 or2 let k be the number of inspected
carry positions, including the final zero. Start the relative carry head
at0; explicitly inspect/change successive bits and then restore the head.
Its local phase is finite. Store its position in binary with initialized
zero padding and its active bit length; only the active low bits change.
For positions <=k, copying/updating/testing that local position and its
length uses O((log(k+2))^2)<=O(k) bit operations per visit, by ordinary
schoolbook bit code, not a complete log(d)-bit serialization at each
visit. A zero/termination flag is updated by the carry/borrow operation;
there is no fresh full-width zero comparison per visit. One may keep a
one-hot head marker in an O(d)-bit ordinary scratch strip: the fixed
position0 flag detects return to the start without a width-d zero scan.
It is initialized once and only the old/new marker bits change per move.
This yields a conservative O(k^2) bit-control bound per carry run,
including head restoration, loop/counter updates and local generation.

Use constant many power-of-two aligned ordinary strips for argument,
head/control and temporary words, with constant-factor padding. Complete
address buffers contain their fixed aligned bases and all high bits;
initialize those bits once per scope. Form the variable low offset for
a visit explicitly from the active position bits, costing at most the
same O((log(k+2))^2). Restore overwritten low positions before reusing a
buffer for a smaller offset. High bits remain initialized and available;
the addressed primitive reads/decodes its ENTIRE d-bit argument and pays
d, including on bit accesses to ordinary scratch. Changed buffer bits
also pay d each. Alignment is only to avoid re-forming a fixed base for
each visit: all padding bits and the additional O(d) head strips are
counted in the existing ordinary2^20 n staging margin. No high address
bit is ignored and no position is a unit-cost arithmetic operation.
This is the carry-role emitter of typed_dispatch.md made into a scoped
physical microprogram, with its actual low-address changes included.

For any starting value and L successive increments that stay in range,
long runs obey the squared-run bound
 sum k^2 = O(L+d^2).
To verify it, take b=ceil(log2(L+1)); the interval intersects at most two
aligned 2^b blocks and crosses at most one higher boundary. The lower
cycles have sum O(2^b)=O(L) since sum_(j>=1)j^2/2^j is finite; the one
higher carry contributes O(d^2). Increment by2 just omits the fixed low
bit. Reversed decrement streams use the identical borrow argument.
Initialize the complete first argument and its fixed buffers in O(d^2)
bit work. A fixed-length loop uses a remaining-count borrow flag, with
all counter changes and its one terminal underflow included, rather
than rescanning its full counter for zero each iteration. Thus a long
RAW field stream costs O(d(L+d^2)) including all address consumption,
initialization, updates, restored heads and actual bit operations.
For L a fixed positive multiple of n, d=Theta(sqrt n) gives O(n^(3/2)).
This applies to complete n-bit words, 3n labels and WROW first clears.
EW tag operations and short control fields may keep their older
O(n(log n)^(3/2)) helper bound, also O(n^(3/2)) on the main branch.
The short row-base product is O(n(log n)^(3/2))<=O(n^(3/2)); complete
word helpers therefore cost O(n^(3/2)), with every stored bit preserved.
Short valid helpers keep O(n(log n)^(3/2)); no stronger claim is needed.

ADD/SUBTRACT/COMPARE/COPY on full staged words use forward/reverse
ripple passes of length Theta(n), with constant many operand cursors,
flags and fixed offsets. The same run count charges O(n) raw control
work, hence O(n^(3/2)) including address fees. Three-n-bit labels use
three explicit chunks as before. Mapped address arithmetic may keep
schoolbook multiplication/addition on two d-bit words. Its d regular
length-d rows cost O(d^2) raw bit work: row initialization uses only the
O(log d) position bits and O((log d)^2) bit setup, with whole d-bit
argument buffers initialized once for the entire product. The total
row-start cost O(d(log d)^2) fits O(d^2); operand passes use relative
cursors, not repeated whole-field setup. With fee d, staged address
arithmetic costs O(d^3)=O(n^(3/2)). Consequently a mapped dispatch,
CALL/RETURN or complete binding refresh costs O(n^(3/2)). All field
commits, epoch checks and first writes remain. The exact finite fallback
is unchanged and covers any finitely many lengths before these fixed
inequalities; the asymptotic constants absorb them.

## Current source, tree and weighted ledger

native_ops.md now specifies direct native source transfer, clean fast
exact T1 arithmetic, fused QPE translation, exact verifier quotients,
actual short dictionary/tree formats and scoped word/tree interfaces.
verified_extract.md specifies the executed tighter fallback cap and its
coupling probability. These replace the old regular-LE weighted total;
all helper/control microprograms above remain counted. The current total is
 T<=c[n^(5/2)(log n)^(3/2) C_0+n^2(log n)^3 C_0+n^3(log n)^(3/2)2^(H+dl)
       +n^2(log n)^2 Qcap+n^2(HQ+DRAW+1)]+poly(n),
hence O(n^(43/4)(log2 n)^2 2^((7/6)sqrt n)).
