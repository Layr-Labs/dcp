# CONSTANT8 CHECKPOINT: complete read-only layer XOR and eight-level unequal bridge

The exact layer/bridge/scan methods are material from published c73fc7ac-8bbf-4351-9613-50b43d15f65f,
immutable8c7415130c888be298cfe7a099bfc273087728d6, sqrtlog-native1--4. Its old growing/sqrt-log pool
parameters and one-pass outer protocol are NOT selected. Bennett1989 Time/space trade-offs for reversible
computation retains credit. All methods are supplied in FULL here; neither source verdict nor a simulation
is a premise. Actual current pools, emitter, metadata and fees follow.

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

## 2. Current exact pool geometry and recursion bounds

For n>=2^40 use eight-group proof3 parameters. Every sort has M=2^k_sort padded records,
k_sort<=r+182<=n/4 and D_sort=k_sort(k_sort+1)/2<n². Set k_n=(n-1).bit_length(),
b_exp=ceil(k_n/4),B_ck=2^b_exp,H_ck=8. n^(1/4)<=B_ck<=2n^(1/4) and B_ck^8>=n²>D_sort.
At most8 levels suffice by repeated ceiling division, with no artificial empty layer. Allocate ALL8B_ck
whole-record arrays per sort and all original/sorted/stage/scan arrays, including unused slots. No persistent
comparator history tape is executed. The base-layer word uses only O(n) predicate scratch and cleans it.

For a segment with length d>1 choose b=min(B_ck,d), q=floor(d/b), rem=d mod b.
Its b NONEMPTY consecutive children have lengths q+1 for i<rem, else q,
and starts l+i*q+min(i,rem). If d>=B_ck, b=B_ck is a power of two, so q/r use
shifts/masks. If d<B_ck, b=d and all lengths are exactly1 (no division needed).
If d=1 use the READ-ONLY layer XOR primitive; M=1 is identity copy.
Each child's max length is ceil(d/B_ck) unless d<B_ck, when it is1.
Repeated ceiling division gives depth<=ceil(log_(B_ck) D_sort)<=H_ck=8.

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


For a length-d segment at remaining depth h, the total base calls are <=2^h*d: the child lengths
sum to d, each prefix child occurs twice and the last once. Induct this inequality from h=0,d=1.
Thus actual base calls<=256D_sort. Upper bound8 is a literal fixed constant, not an n-dependent height
hidden in SC or work. Full quantum M_base=O(S*n*8B_ck+n4)=O(Ln^(5/4)),S=O(L).

## 3. Complete distinct boundary and sequential scan words

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

## 4. Actual fixed-eight-frame emitter and full fees

The current host emitter uses EXACTLY EIGHT frames, each storing public segment start/length, phase child
index, source/output/pool bases and direction. Each field is O(n) bits. Thus this fixed stack is O(n)
classical bits, unlike a growing n-bit-frame stack. It stores NO quantum data or circuit/history table.
The source/current buffers and arithmetic use a constant additional number of O(n)-bit words.

At d>1 compute b=min(B_ck,d),q=floor(d/b),rem=d mod b. Child i has start l+i*q+min(i,rem),
length q+[i<rem], source A ifi0 elseC_(depth,i-1), output Z iflasti elseC_(depth,i).
When d>=B_ck, divide by the public power of two via shifts/masks; when d<B_ck, b=d,q=1,rem=0.
In each frame phases0..2b-2 emit prefix children forward, last child with parent direction, then prefix
children in reverse inverse order. Parent direction INVERSE reverses the ENTIRE elementary word.
Use a bounded phase counter and explicit return-to-parent; stop at actual d=1. EIGHT public frames suffice.
All frame pushes write every field; a pop restores the public parent phase/counters. Frames do not address
quantum wires depending on data. Public sort stage/stride loops recover the exact base-layer descriptor;
no preloaded table or instance advice exists. Fixed depth and O(n)-bit in-place arithmetic give a conservative
O(n4) TOTAL charged metadata per base call, including FULL address fee for each classical bit operation.

Pool base is pool_base+(depth*B_ck+i)*array_stride; array and record/field strides are powers of two.
All shifts/adds/copies use literal bit operations. Within a layer, a constant number of running pointers
move by unit steps through O(n)-gate predicate/copy words. Minimal-width bounded loop counters start at
limit-1, subtract1 and stop on underflow: total changed bits O(limit+log(limit+1)). Pointer/record setup
uses O(n) copied/add bits. EVERY emitted gate and classical bit operation pays FULL d_addr=O(n), derived
from WHOLE allocation. Hence record work O(n*d_addr), layer O(Mn*d_addr), and all joins across <=256D_sort
base calls cost O(S*n*D_sort*d_addr)=O(Ln4). Metadata O(D_sort*n4)=O(n6) fits because L>=n6.
No n-by-n multiplication is performed per elementary gate, but any public setup uses the paid metadata bound.

Constant-many whole compute/query/inverse blocks include EVERY8B_ck array. Original and sorted inputs
remain until their dependent work literally reverses. Full streaming zero apparatus native6 costs
O(M_base*d_addr²)=O(Ln^(13/4)), including unused pool initialization and disposal, below join O(Ln4).
Clean bounded joins compute EXACTLY native3 duplicate pairs, ranks, caps and canonical inverse. Read-only
layer XOR and the bridge preserve source inputs and clear lower pools for arbitrary finalZ, by the induction
above. Every dirty extension remains a unitary with LITERAL inverse; no identity to old LEAN dirty words is
used. Full spectral/Jordan/reachable-range safety is supplied in proof6--7 for THIS actual V and Vdag.
