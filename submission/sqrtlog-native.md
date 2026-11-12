# RPF-8SQRTLOG-TIGHT: literal read-only layer XOR and packed square-root-log checkpoint sorting

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

## 2. Actual unequal bridge and public pool

Each bounded join returns EXACTLY its public cap records by copying the first cap sorted slots into a fixed output region, retaining larger internal padded arrays until reversal. Each union/marker-query/B-match/output/canonical sort pads its PUBLIC slot count to the next power of two. Starting at4Pcap rows, each expansion is at most4M_old+2Pcap; at mostfive expansions give M<=2^16Pcap and k<=r+176<=n/8+197<=n for n>=4096. Thus D_sort=k(k+1)/2<=n².

## Exact public parameters and whole allocation

For main n>=4096, v=log2 n, k_n=ceil(log2 n), set
 r_ck=ceil(sqrt(k_n)), B_ck=2^(2r_ck), H_ck=r_ck.
Integer square root/bit lengths implement them exactly. Keep these names
DISTINCT from preimage H, score effect B, group width r and witness D.
Use ONLY actual D_sort layers, never pad to B_ck^h. The existing bounded
join packet schedule gives M<=2^16Pcap, k=log2M<=n, D_sort<=n².
Since B_ck^H_ck=2^(2r_ck²)>=2^(2k_n)>=n², unequal bridge height<=r_ck.
The same nonempty split b=min(B_ck,d), child lengths floor/ceil(d/b),
exact offsets and forward-prefix/last-child/reverse-prefix word apply.

If C(d) counts base calls, C(d)<=2^H_ck*d<=2^r_ck*d. Each internal node
has at least3 children, so total call-node setups are O(base calls).
Thus whole quantum layer work is O(L n³ 2^r_ck), full record/address
work O(L n4 2^r_ck). Original/sorted/raw/prefix/checkpoint/zero regions
are counted, no repetition history accumulates.

r_ck<=sqrt(v)+2, so2^r_ck<=4*2^sqrt(v), and r_ck<=2sqrt(v) for v>=12.
The physical pool has H_ck*B_ck arrays per packet, including unused slots,
so quantum peak is O(L n*r_ck*2^(2r_ck))
 =O(2^(n/8)*n*(log2n)^(1/2)*2^(2sqrt(log2n))).
Source/Rrec/staging and O(n4) auxiliaries fit since L>=n5.

Initialization and allzero apparatus are NOT free. For k_n>=12,r_ck>=4,
 (r_ck-1)²<=k_n-1, 2r_ck<=(r_ck-1)², log2r_ck<=r_ck,
so r_ck*2^r_ck<=2^(k_n-1)<n. Hence full initialization/zero work
O(L n²*r_ck*2^(2r_ck))<=O(L n³2^r_ck), within the oracle budget.
A coarse allocation Ln³ proves FULL global fee O(n) without circularity.

Public metadata arithmetic/descriptor recovery may be charged O(n4)
TOTAL per base/call, separately from per-record emission. O(n²2^r_ck)
call count gives O(n6 2^r_ck), within Ln4 2^r_ck by L>=n5.
All public fields fit constant many O(n)-bit buffers; see controller below.

For actual8-group nominal j=O(L²sqrt n), outer2^(291m/12706), the joint
actual tuple is
 T=O(2^(20223/50824*n)*n^(9/2)*2^sqrt(log2n)), SC=O(n),
 SQ=O(2^(n/8)*n*(log2n)^(1/2)*2^(2sqrt(log2n))),
 EXACTQ=3*2^40(n+32), fullfixedjoint epsilon1/32.
No irrational enclosure/Pell gap is needed for these EXACT lower-order
coefficients1 and2. Indices remain1,0,1,0. Compared with binary8CP,
time is eventually smaller, space larger; compared with8VP16 time is
larger, space eventually smaller. No finite-size crossover or optimum claim.
The sixteen-list analogue uses leadingT87245/203296 and leadingSQ1/16 with the SAME new actual outer291/12706.


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
children. Constant many sort/stage arrays, ALL H_ck*B_ck checkpoint arrays and
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
