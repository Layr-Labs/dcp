# RPF-8VP16: literal read-only layer XOR and constant-depth variable checkpoint sorting

This is the ACTUAL sort word selected by the current program. The
standard recursive recomputation idea is credited to C.H.Bennett,
Time/space trade-offs for reversible computation (1989),
https://research.ibm.com/publications/timespace-trade-offs-for-reversible-computation .
No external simulation or sorting theorem supplies a native oracle here:
the recurrence, Boolean word, full controller and charged bounds follow.

Record addition/subtraction/comparison uses ripple carry/borrow, mux and
copy use per-bit Boolean words, and powers-of-two shifts use wires.
Each is O(n) gates on constant many O(n)-bit fields. For example borrow
for x-y is ((NOT x) AND y) XOR ((NOT(x XOR y)) AND borrow_in), whose
two terms are disjoint. Copy a result and reverse all evaluator work
with its inputs unchanged. Generic n² multiplication/division is not
executed for each join record. Raw lists use clean IN-PLACE controlled
additions of selected quantum W labels at PUBLIC subset IDs, with no
partial-sum history tape. Signed encodings/invalid defaults are native1.

## 1. One layer as an XOR function with its input retained

A bitonic sort of M=2^k records has D_sort=k(k+1)/2 PUBLIC layers of disjoint
comparisons. A record has constant many O(n)-bit fields with the SAME full
lexicographic padding/signed-key/tag/payload order as the bounded join.
For layer l define F_l(A) as its ordinary compare/swap output on array A.
Implement B <- B XOR F_l(A), preserving the ENTIRE A, with O(Mn) gates
and O(n) CLEAN reusable helpers, no saved comparator flag array.

For each disjoint pair(i,z), compute strict comparison p from READ-ONLY
A_i,A_z with the ripple word, retaining its O(n) borrow work only until the copy below. The final borrow itself can control the copies; there is no persistent history flag. For every record bit a=A_i[j],b=A_z[j],
apply
 B_i[j] ^= a; B_z[j] ^= b;
 B_i[j] ^= p&a; B_i[j] ^= p&b;
 B_z[j] ^= p&a; B_z[j] ^= p&b.
These are two CNOT and four CCX gates; all controls are in A/p and all
outputs are in B. Thus they commute and XOR exactly the selected pair.
Uncompute the predicate from unchanged A BEFORE moving to the next pair.
Descending layers use the reversed strict predicate. Input/output regions
are distinct. Unpaired/identity layers simply XOR A into B. All helper
work is clean afterwards, and the literal inverse reverses every gate.
The map works for arbitrary initial B; it is not an in-place irreversible sort.

## 2. Actual checkpoint parameters, unequal blocks and bridge

Fix t_ck=16 as part of the program, not input/advice. For main n>=4096 put
k_n=ceil(log2 n), B_ck=2^ceil(k_n/t_ck), H_ck=2*t_ck=32.
Thus n^(1/t_ck)<=B_ck<=4n^(1/t_ck), all computed with integer bit lengths and a
shift (t16 is fixed). Each bounded join returns exactly its public cap records: copy the first cap sorted slots into a fixed output region; larger internal padded arrays remain retained helper data until reversal. Each union/marker-query/B-match/output/canonical sort pads to the next power of two of its PUBLIC slot count. Starting with at most4Pcap rows, every subsequent sort needs at most2M_old+Pcap slots, hence at most4M_old+2Pcap padded rows. At mostfive such expansions occur per node, so conservatively M<=2^16 Pcap. Therefore k<=r+176<=n/8+197<=n for n>=4096. Every sort has D_sort=k(k+1)/2<=n²
actual public bitonic layers. DO NOT pad D_sort to B_ck^h: that overshoots by
an n-dependent factor and ruins the intended exact time prefactor.

For a segment with length d>1 choose b=min(B_ck,d), q=floor(d/b), r=d mod b.
Its b NONEMPTY consecutive children have lengths q+1 for i<r, else q,
and starts l+i*q+min(i,r). If d>=B_ck, b=B_ck is a power of two, so q/r use
shifts/masks. If d<B_ck, b=d and all lengths are exactly1 (no division needed).
If d=1 use the READ-ONLY layer XOR primitive; M=1 is identity copy.
Each child's max length is ceil(d/B_ck) unless d<B_ck, when it is1.
Repeated ceiling division gives depth<=ceil(log_(B_ck) D_sort)<=2*t_ck=32.

### Exact word, lifetime and arbitrary final output

At depth h allocate b-1 arrays C_i within a PUBLIC reserved pool of B_ck arrays,
each M records of O(n) bits. Pools at different depths are distinct.
For children i=0..b-2, execute E(child_i,input_i,C_i) forward, where
input_0=A and input_i=C_(i-1). Execute the LAST child with input
C_(b-2) and final output register Z. Then execute the literal inverse
of each prefix child i=b-2..0, in that order. For d>1, b>=2.
The d=1 primitive is Z XOR F_l(A), retaining A and cleaning its O(n)
ripple/Boolean helper scratch, valid for arbitrary initial Z.

Induction: each C_i is exactly the prefix-composed function of A when
needed by the next child. Last child XORs the entire segment function
into Z. Reverse-prefix children clear C_i from last to first while their
source prefix is still present. ALL lower-depth pools clear after every
child and can be reused. A remains unchanged and Z need not start0.
Linearity gives the coherent/reference version. On dirty pool inputs,
the emitted gates remain a unitary with a LITERAL inverse; no clean
function assertion on dirty extensions is required for the PGM safety proof.

For an inverse parent, the chronological children are the same forward
prefixes, the last child INVERSE, then the same inverse prefixes. This
is the exact reversal of forward word's elementary gates. The ACTUAL native
emitter allocates EXACTLY33 frames:32 internal levels and one base frame; each holds only constant many
O(n)-bit public words. The frame count is fixed by the program, not growing with n. Each frame stores segment start/length, source/target bases, phase/child counter and constant many other O(n)-bit fields; ALL33 frames count in SC. Store only the
current child/phase counter at each of these FIXED32 levels, not a B_ck-entry
classical directory. Quantum C_(depth,i) bases use aligned power-of-two
array strides and the PUBLIC depth/child index.

## 3. Exact recurrence, fixed-frame controller and complete fees

The number of base-layer calls satisfies
 C(d)=2 sum_(i=0)^(b-2) C(d_i)+C(d_(b-1)) <=2 sum_i C(d_i).
Since sum d_i=d and height<=H_ck, C(d)<=2^H_ck d=2^32 d.
Each internal call has at least3 children, so total call/frame setups
are O(C(d)) too. This EXPLICIT huge constant is independent of n,N,s.
No practical speed or moderate crossover claim is made.

The layer XOR primitive uses O(Mn) gates, O(n) reusable helpers, and
O(Mnd) charged record emission with full global fee d=O(n). The public
record/bit pointers, power-of-two strides and minimal underflow counters
are the same actual linear words as supplied in the lean/checkpoint proof.
They avoid a whole n-bit pointer copy on EVERY elementary gate. All gate
addresses still pay the FULL address charge.

Public per-call block/descriptor/base setup can be charged conservatively
as O(n^4) TOTAL work per call using bounded in-place public arithmetic,
all33 frames, and explicit descriptor enumeration. There are O(n²)
base/call nodes per sort, so this overhead is O(n^6), separately counted.
It is not repeated per record or per gate. For the fixed8/16 program
there are constant many nodes/stages and main L>=n^5, so n6 is within
O(L*n^4). This avoids an unproved unit-cost descriptor/offset primitive.
The explicit public descriptor enumeration below is included in this conservative setup budget; no external helper proof is assumed. All public counters/bases have O(n) bits, with no advice.

Therefore complete sort gate work is O(M*n*D_sort)=O(Mn³); full fees and
record generation give O(M*n^4). Base data-array S=O(L) lanes (checkpoint rows are additionally counted as S*B_ck below) across every fixed
node yield O(L*n^4) TOTAL oracle work, including the separately polynomial
metadata work. There is no global padding to a larger layer domain.

At most H_ck(B_ck-1)M records are USED in the pools; the physical allocation reserves H_ck*B_ck*M rows, including every unused slot. Including
original/sorted arrays and all prefix/boundary/raw/root/marker regions,
whole mark space is O(S*n*B_ck)=O(Ln^(17/16)). ALL unused pool arrays count;
initialization and zero apparatus cost fits O(L*n^4) since B_ck<=4n.
Rrec/source/staging/copies and the O(n^4) auxiliary regions also fit
because L>=n^5. All pool registers are fixed mutable V_R wires included
in P's allzero test. No history accumulates over Grover calls/reflections.
Classical frames33 times O(n) plus the source/controller inventory is O(n).


The EXACT chronological child emitter is explicit. In a frame with b children,
its phase counter runs0..2b-2. For phase<b-1 emit child_i with i=phase
FORWARD. At phase=b-1 emit the LAST child with the frame direction. For
phase>b-1 set i=2b-2-phase and emit child_i INVERSE. Child_i has length
q+[i<r] and start l+i*q+min(i,r). Its source is A if i=0, otherwise C_(i-1);
its target is Z for the last child, otherwise C_i. Push this public child
frame, process it, then resume its parent counter. Frames are bounded by33.
The reverse frame direction changes only the last-child direction, which
is exactly the literal inverse of the stated prefix/last/uncompute word.
All inverse base words reverse EVERY native Clifford+T gate and scalar.

The pool physically reserves H_ck*B_ck arrays, including the unused last
slot per level. A level/child array base is pool_base+(level*B_ck+i)*stride,
with stride the POWER-OF-TWO padded full array size. Thus address setup
uses shifts/additions or the separately charged public arithmetic, never
an unknown quantum index. B_ck,H_ck belong ONLY to this sorting layout;
the preimage search-domain H and score effect B keep their original meaning.
Recover (K0,J0) for layer l by enumerating the D_sort listed PUBLIC bitonic
stage/stride descriptors without storing a table; fixed-width integer loops
and their full fees are within the O(n^4) public setup budget per call.
No public real root or instance-dependent advice is supplied.

All33 frames and public arithmetic use constant many O(n)-bit buffers per
frame, in-place schoolbook accumulation/restoring division and bounded loops.
They never store a full circuit or a growing product of denominators.
Within a read-only layer use the ACTUAL padded power-of-two field/record
strides and constant many running pointers. Every O(n)-gate ripple/mux/copy
word has O(n) changed-pointer/setup bits and pays FULL d_addr per gate/bit.
Minimal-width counters initialize limit-1, emit the body, subtract1 and stop
on UNDERFLOW; summed ripple visits are O(limit+log(limit+1)), without an
n-bit zero test for every gate. This gives O(n*d_addr) per record operation,
not free address arithmetic or per-gate n-by-n multiplication. All repeated
padding, initialization/disposal and the separate allzero apparatus count.
## 4. Corrected scans, full allocation and actual clean functions

Use native3's DISTINCT head_i=(i=0 OR key_i!=key_(i-1)) and
tail_i=(i=M-1 OR key_i!=key_(i+1)), with JOIN-KEY/padding equality only.
Forward inputs are(B_i,head_i), reversed inputs(B_i,tail_i); never reuse
forward heads for suffixes. The associative operation is
(x,h) star(y,k)=(y if k else x+y,h OR k). Sequential recurrence stores
ONE fresh prefix state per lane, preserving original inputs; inverse
erases states last-to-first from previous state/input. Induction gives
inclusive bucket-prefix and bucket-suffix B sums, hence their sum minus
B_i is the whole bucket count. B_rank=forward-1. Both boundary arrays
remain until scans reverse and are then uncomputed from unchanged rows.
Global counts/starts and rightmost PRESENT marker propagation use the
same sequential recipe, preserving all needed inputs until reversal.
No parallelism or stable ordering of equal keys is assumed.

The sort's original inputs and sorted outputs both remain allocated;
only intermediate checkpoint arrays are cleaned/reused between recursive
children. Constant many sort/stage arrays, ALL32B_ck checkpoint arrays and
all new helpers are in proof9's WHOLE peak, along with raw/root/padding,
Rrec/source/probe/score/selector/routing, output/inverse and zero apparatus.
The actual public nominal Grover count and positive scalar are native2/3.
No global count estimator, free QRAM or source inverse is supplied.

For clean inputs every bounded g/F/join computes EXACTLY the duplicate
pairs, ranks, caps and canonical inverse of proof3. Read-only layer XOR
preserves its input while the bridge clears its internal checkpoints;
compute/copy/reverse removes every temporary before X changes. The ACTUAL
new V_R and literal inverse define Qv. P=I_(D,Rrec) tensor zeroA includes
EVERY new mutable wire. Sections4--7's column/error/spectral/reachable
proof therefore uses this word, not an old globally dirty extension or
an earlier verdict. ExactlyQ and the full fraction1/32 promise are unchanged.
