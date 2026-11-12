# RPF-TAIL-SQRT-ONEPASS: literal read-only layer XOR and packed square-root-log checkpoint sorting

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

## 2. Growing packet geometry and actual used depth

## Exact growing allocation, actual layer depth and full fees

Main n>=2^20 uses the growing tree EXACTLY in proof3. ALL G-2 nonroot
packets and the separate root packet are counted in base rows S=O(G²L)=O(nL).
For a nonroot sort use public capPcap, and at root use max(Pcap,K).
Each bounded join returns exactly its cap records by copying the first cap
slots, retaining all padded helper arrays until reversal. At mostfive
public padding expansions from4cap give M<=2^16cap. Consequently
k_sort<=r+D_grp+179<=3sqrt n and D_sort=k_sort(k_sort+1)/2<=6n.
All input/output/helper regions have public sizes, independent of data.

Let k_n=ceil(log2n), r_ck=ceil(sqrt(k_n)), H_ck=r_ck, B_ck=2^(2r_ck).
These are computed by integer bit lengths/square-root/shift and are distinct
from group r, preimage H, effect B and witness D. Reserve EVERY H_ck*B_ck
array, including unused slots, per packet. Use only ACTUAL nonempty unequal
blocks; there is no padding of the layer domain. Actual used height
 h<=ceil(log_(B_ck)D_sort)
 <=(log2n+log2 6)/(2r_ck)+1<=sqrt(log2n)/2+2.
Hence actual base calls<=2^h D_sort<=24n*2^(sqrt(log2n)/2), even though the
reserved height remains r_ck. The physical program stops at d=1.

One base layer uses O(Mn) gates and O(n) reusable helpers. The ENTIRE
allocation O(S n H_ck B_ck+n^4) has full global address fee O(sqrt n),
not a changed charging rule: logM_alloc<=r+O(logn+sqrt(logn)) and
r<2sqrt n+1. Linear record words/pointer changes pay this FULL fee.
Thus total whole-oracle gates O(Sn²2^(sqrt(log2n)/2)) and full record/
native work O(Sn^(5/2)2^(sqrt(log2n)/2))<=O(Ln^(7/2)2^(sqrt(log2n)/2)).
Conservatively charged O(n4) metadata per leaf, across allG joins and
O(n*2^(sqrt(log2n)/2)) calls each, fits this budget since L>=n^6.

All unused arrays count in initialization/allzero/disposal. For r_ck>=5,
2r_ck+ceil(log2r_ck)<=(r_ck-1)² (base5 and integer induction), while
log2n>(r_ck-1)² by the actual ceilings. Thus H_ck*B_ck<n, and total
array initialization/zero/disposal O(Sn*sqrt n*H_ck B_ck)<=O(Ln^(7/2))
fits the oracle cost. Quantum peak is O(L n² r_ck4^r_ck), giving exactly
O(n²(log2n)^(1/2)2^(2sqrt n+2sqrt(log2n))). Source/Rrec/probe/score/
selector/routing/target/hash polynomial auxiliaries fit because L>=n^6.

The SAME packed phase-path controller below stores O(logn) phase bits plus
constantmany O(n)-bit root/current fields and pays EVERY reconstruction/
descriptor/full-address step. Caller tree generation is proof9's public
level/node/heap loops, not a growing pointer stack or classical directory.
The actual ONE-pass selector/decoder/score protocol is proof6--7, with
EXACTQ3*2^40(n+32) and full fixed-joint fraction1/(32n). Its public nominal
j=O(2^(t/2)L^(F/2)sqrt n) and one-pass column give proof9's entire charged
T=O(n^(17/4)2^(n/2-(1/4)sqrt n log2n+sqrt n+(1/2)sqrt(log2n))).

For a segment with length d>1 choose b=min(B_ck,d), q=floor(d/b), rem=d mod b.
Its b NONEMPTY consecutive children have lengths q+1 for i<rem, else q,
and starts l+i*q+min(i,rem). If d>=B_ck, b=B_ck is a power of two, so q/r use
shifts/masks. If d<B_ck, b=d and all lengths are exactly1 (no division needed).
If d=1 use the READ-ONLY layer XOR primitive; M=1 is identity copy.
Each child's max length is ceil(d/B_ck) unless d<B_ck, when it is1.
Repeated ceiling division gives depth<=ceil(log_(B_ck) D_sort)<=r_ck.

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


## 3. Actual packed phase-path controller and full emission fees

A naive recursive host stack would use O(n sqrt(logn)) classical bits and
would NOT prove SCn. The mathematical recursion is only a word definition.
The actual emitter stores a path of at mostH_ck phase digits, each of
width ceil(log2(2B_ck))=2r_ck+1. Total O(r_ck²)=O(logn) bits.
It uses constant many O(n)-bit current segment/start/source/target/stride/
direction/loop/arithmetic fields, reconstructing metadata instead of saving
one n-bit frame per level. Every digit/field access pays the full fee.

Reconstruct a path prefix from the root. In segment d>1 letb=min(B_ck,d),
q=floor(d/b),rem=dmodb. For phase0..2b-2:
 ifphase<b-1: i=phase,directionFORWARD;
 ifphase=b-1: i=b-1,directionPARENT;
 ifphase>b-1: i=2b-2-phase,directionINVERSE.
Child start is l+i*q+min(i,rem), length q+[i<rem], source A ifi0
otherwiseC_(depth,i-1), output Z iflasti otherwiseC_(depth,i).
These are PUBLIC wire-array bases, never quantum data-selected addresses.
When d>=B_ck, q/rem use shifts/masks; when d<B_ck all lengths are1.

Start with all path digits0. Reconstruct until d=1 and emit that base word
(or its LITERAL inverse per reconstructed direction). To advance, examine
ancestors deepest-to-root: reconstruct that parent prefix, test whether its
phase digit can increment below2b-1. On the first possible increment,
increment it and zero all deeper digits, then descend again to the next
leaf. If none can increment, finish. This lexicographic variable-radix DFS
visits EXACTLY the recursive word's leaves. Root directionINVERSE uses the
same rule and yields the exact reversed elementary word by induction on
prefix/last/uncompute structure; inverse base words reverse every gate.

At most r_ck ancestors each require at most r_ck reconstructed steps per
leaf. r_ck²=O(logn)<=O(n); generic in-place On-bit arithmetic with full
fees costs at mostO(n³) per step, hence O(n4) setup per leaf. Recover a
bitonic layer descriptor by enumerating its PUBLIC stage/stride schedule,
also withinO(n4); no table stored. The packed path plus current fields and
source/score/controller inventory gives SC=O(n). All quantum pools include
EVERY H_ck*B_ck array and ALL unused zero slots in P and the peak.


The pool physically reserves H_ck*B_ck arrays, including unused slots. A base is pool_base+(depth*B_ck+i)*stride, with power-of-two padded full-array stride. Every base/counter/setup step pays the FULL global fee. Within a layer, aligned padded record/field strides and running pointers avoid a fresh n-by-n multiply per elementary gate. Every O(n)-gate ripple/mux/copy word has O(n) changed-pointer/setup bits, each paying d_addr. Minimal-width counters start at limit-1, emit, subtract1 and stop on underflow; summed ripple work is O(limit+log(limit+1)). Thus charged record work is O(n*d_addr), with no n-bit zero-test per bit gate. Public descriptor recovery enumerates bitonic stage/stride loops in O(n^4) TOTAL per base call. All arithmetic uses constant many O(n)-bit in-place schoolbook/restoring-division buffers; no circuit table, n-bit frame per level or instance advice exists. The exact inverse reverses EVERY elementary Clifford+T gate and scalar.

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
children. Constant many PER-NODE sort/stage arrays across ALL G nodes, ALL H_ck*B_ck checkpoint arrays and
all new helpers are in proof9's WHOLE peak, along with raw/root/padding,
Rrec/source/probe/score/selector/routing, output/inverse and zero apparatus.
The actual public nominal Grover count and positive scalar are native2/3.
No global count estimator, free QRAM or source inverse is supplied.

For clean inputs every bounded g/F/join computes EXACTLY the duplicate
pairs, ranks, caps and canonical inverse of proof3. Read-only layer XOR
preserves its input while the bridge clears its internal checkpoints;
compute/copy/reverse removes every temporary before X changes. The ACTUAL new V_R and literal inverse are fully known words; the main makes ONLY its one clean-input score/PGM flag measurement. Every executed zero test includes all of its required mutable helper wires. Sections4--7's column/error/one-pass-safety
proof therefore uses this word, not an old globally dirty extension or
an earlier verdict. ExactlyQ and the full fraction1/(32n) promise are unchanged.
