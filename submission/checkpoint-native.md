# RPF-16CP: literal read-only layer XOR and recursive checkpoint sorting

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

A bitonic sort of M=2^k records has D=k(k+1)/2 PUBLIC layers of disjoint
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

## 2. Actual bridge word and checkpoint allocation

Pad the layer count to D0=2^h, h=ceil(log2 D), using identity layers after D.
For M=1 use the identity copy directly, with h=0. Allocate ONE record-array
checkpoint C_j per recursion depth j<h, each M records of O(n) bits.
For a segment of length2^j beginning at layer l, define E(l,j,A,B):
 j=0: execute the layer XOR word above.
 j>0, with fresh C_(j-1)=0:
   E(l,j-1,A,C_(j-1));
   E(l+2^(j-1),j-1,C_(j-1),B);
   literal inverse of E(l,j-1,A,C_(j-1)).
Deeper checkpoints are reused sequentially after each child cleans them.
Induction gives B XOR (F_(l+2^j-1) composed ... composed F_l)(A),
with A unchanged and ALL checkpoints/scratch0, for arbitrary B and all
basis values of A. By linearity the statement holds against an arbitrary
reference and superposition. The final B is exactly the original sorted
function on clean B, while A is retained until dependent work reverses.
On dirty helpers the emitted word is still a unitary, with its literal inverse;
no claim that it globally equals an older dirty extension is needed.

There are exactly3^h base-layer calls and peak(h+2)Mn+O(n) qubits per
sort, including input/output. Since3^5=243<256=2^8,
3^h<=3D^(log2 3)<=3D^(8/5). For k=O(n), D=O(n²), so complete sort
has O(M n^(21/5)) gates and O(Mn log n) qubits. Whole bounded joins
have CONSTANT many sorts/stages per node and fixed16/15 nodes. With whole
lane count S=O(L), gate count is O(S n^(21/5)), space O(Sn log n).
Corrected sequential scans retain O(Sn) states plus separate HEAD/TAIL flags,
and raw list filling is O(Ln²) gates; both are within these bounds.

## 3. Uniform emission without a classical recursion stack

Enumerate the ternary leaf path counter with h trits (O(h) bits), not
O(n)-bit recursion frames. Recompute each leaf's PUBLIC layer and region
bases by scanning the path from root to leaf using constant many O(n)-bit
words: source A, destination B, segment start, half-length, checkpoint base
and direction. At each descent the public checkpoint base decrements by
one common array stride. For child0 set destination to current checkpoint
and direction forward; child1 sets source to checkpoint, advances segment
start by half-length and inherits direction; child2 sets destination to
checkpoint and direction inverse. This emits the correct chronological
children of either a bridge or its inverse: left forward, right with the
parent direction, left inverse. No quantum value selects an address.
For the global literal inverse enumerate leaves in reverse and reverse each
base word. The private source/score/unknown-witness region is unchanged.

Extracting h trits and updating full pointers takes O(hn) raw bit accesses
per layer call. Its full global address fee is d=O(n) for the fixed16 word.
For M>=2, h<=M, so path setup O(hnd) fits the base layer O(Mnd) work.
Public node/field/array strides are power-of-two; running pointers and
minimal-width underflow counters give the explicit O(nd) record operation below, not a full n-bit address copy per gate.
Initialization, allzero apparatus, gate generation, output/inverse copies,
failed branches and cleanup are counted. Host storage is O(n) bits.


For completeness, the ternary path has O(h) bits. Divide its O(h)-bit
counter by the FIXED integer3 using a left-to-right remainder in{0,1,2},
O(h) bit operations per trit. Thus all h trits cost O(h²)<=O(hn).
A running checkpoint base decrements by one common stride at each path
step, avoiding a new multiplication for every pointer. For M=2^k>=2,
D<=2^k by base cases and induction, hence h<=k<=M. Main k<=n and
h<=n for the actual fixed16 packets. The path scan uses constant many
O(n)-bit buffers and one O(h)-bit packed path, never h O(n)-bit frames.

Within each layer emit constant Boolean/Clifford+T templates directly.
Record/field/array strides are powers of two. Keep constant many running
bit/field pointers. A bounded loop initializes its MINIMAL-width counter
to limit-1, emits the body, subtracts1 and stops on UNDERFLOW. It never
performs a whole-counter zero comparison on each gate. Total bit changes
are O(limit+log(limit+1))=O(limit); reverse words use bounded reverse
counters. Per-record boundary setup may copy/add O(n) bits at FULL fee d.
On-bit ripple/mux/selected-copy gates and pointer changes also pay d,
so the charged record work is O(nd). The O(hnd) path reconstruction
fits one whole layer's O(Mnd) as above. Every gate address is serialized
at the FULL allocated address width. No quantum data selects a host read,
no stored circuit is traversed, and all initialization/disposal costs count.

Recover the public bitonic (K0,J0) descriptor from the base-layer index l by enumerating the listed k(k+1)/2 PUBLIC stage/stride descriptors, without storing a table. Counters and shifted strides use O(k) significant bits, so this takes O(Dk)<=O(k³) raw bit operations. For every k>=1, k²<=2*2^k=2M (check k1..3 and use induction from4), and k<=n. Thus descriptor recovery is O(Mn) raw work and fits the complete O(Mnd) charged base-layer budget, including the FULL fee d. Identity padding is selected by one bounded public l>=D comparison. No hidden layer-index oracle is used.

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
children. Constant many sort/stage arrays, the full h checkpoints and
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
