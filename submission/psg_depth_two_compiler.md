# Complete online compiler for PSG-D2

This required appendix selects the actual controller used by psg_depth_two.md and
psg_depth_two_base.md with psg_depth_two_budget.md. All five claims
cite all four proof files. The immediate complete local template is
psg14c_streamed_compiler.md, SHA256
`4ff058eb9aa0f631126cd8443b691aa72d3d1ec7884dec06a5236542f71f79c1`.
Its complete implementation source is psg14c_compiler_transfer.md, SHA-256
`0524ec65f682efc625237ad074d71430cfdfdf60d6e80cc1ecb6167b82e61224`.
Its full G.2--G.4 implementation and remaining-work proof are reproduced,
with the selected two-level profile, root/record guards, counts and finite-precision separation
adapted by the complete fixed new-budget proof. No source verdict or
external compiler is a premise. No O(n^2 log n) stored instruction tape
is allocated; the fixed-field online generator is specified below.

## 1. Exact sources and checked interface

Direct public material source: PSG14C, submission
`30304a9e-15d5-4b58-9998-d5a4ccc1a67e`, immutable commit
`398d8457f6c25e29a941403e4e75eccb290dda79`,
[proof](https://github.com/Layr-Labs/dcp/blob/398d8457f6c25e29a941403e4e75eccb290dda79/submission/proof.md)
and [claims](https://github.com/Layr-Labs/dcp/blob/398d8457f6c25e29a941403e4e75eccb290dda79/submission/submission.json).
The exact saved proof/JSON SHA-256 hashes are respectively
`2abeb473f0ea10cd5f7305cf58f8696dddd148967337a851183bfc55254ce0b6` and
`626dd5115b1e5bf45f6fac74e659a902708ae1a580918daa1daa9b4b684b53d6`.
Read the actual Sections 0,4,6--11 and exact JSON. The compiler transfer is
checked against that corrected source, not against a private alias or a
similarly named older algorithm. In particular, its M=1 case preserves a positive shared record count. The selected new
K=2^17n keeps that correction for 2-adic stages and dummy padding; only
Sodd is zero when the odd part is absent.

The complete generic stream source is `grover_stride_compiler.md`, SHA-256
`4c5bcd59c95fa2c10be21ab610cdfe76f6b8d2d31300582b97417a7f5b7e896f`.
The previous three-level transfer was read in `psg13_compiler_transfer.md`,
SHA-256 `bcc4156e5aba2b6c7ec9e687c204aec97bbf903b16c72bca1c2c3dd71dc4c699`.
The fixed fully reproduced implementation in `psg13_verified_compiler.md`,
SHA-256 `948a1d348359f808d7a5e726262f8bd8adb3315447c1027d6e5706f620cfce4a`,
is copied in G.2--G.4 below with this package's two-level profile and root-budget meanings.
Its actual source method is the ready-address/tape-head/marked-loop
construction from `critical_third_cache_generator_l2.md`, SHA-256
`eb122317b103da59cdd982b29f863da27d1d932313e8b67861d1d212a64088f3`.
All required generic implementation details are reproduced; none is a
supplied gate-generation oracle. No source review verdict is a premise.

PSG14C directly credits the CYG1 public note
`70564803-3637-426f-9587-e1333aa07b39` for parity-support disjoint-pair
mass and the two-row factorial-moment fiber tail. It in turn credits CYC1.
The earlier compiler-transfer author read those proofs as reproduced in
PSG14C Section 4.3, without reading the CYG1/CYC1 originals for that
calculation. That historical read statement is retained. The present
packager later read CYG1 for separate cyclic work; this exact disjoint-pair
controller uses only the reproduced PSG14C arguments. Their indirect credits
are preserved without an invented archive identity. No cyclic instrument
or seven-moment success theorem is used by this compiler. The complete
PSG14C inherited source chain, model credit and local-alias distinctions
remain required in any future full package.

## 2. Select exactly this implementation and fixed profile

Put n=ceil(log2 N), L=log2 n on n>=256. All symbols here are the
actual local root/record meanings in psg_depth_two.md. The exact primitive
is unchanged: k=b+1, separate queries, known b-bit weights, at most 64
verified strings and 64 blocks of 64 trials, exact adjacent-pair output
and fresh children after failure. The profile and guards are this package's
selected two-level rule, not the earlier public three-level parameters.

The main branch n>=256 uses sequential positive trials R. Put
l=ceil(log2 n), delta(R)=ceil(log2(3(2R+1))), and
Rtest=ceil((n+2l+4)/4). Since Rtest<=n/2 and
3(2Rtest+1)<=4n, its decrement is at most l+2. Its second value is
positive because Rtest>=n/4>l+2. Its capacity is at least
4Rtest-2(l+2)>=n. Therefore the first feasible trial satisfies

    n/4<=R<=Rtest<=n/4+(1/2)L+5/2,
    2^R<8sqrt(n)2^(n/4), R=Theta(n).                  (P-D2)

These bounds use no monotonicity of capacity. At n=256 and thereafter,
L+5<=n/4 and L+3<=n/8. Their real differences increase on this range.
Thus R<=3n/8 and delta(R)<=l+2<=L+3<=n/8<=R/2. Both retained
values are positive: mstar=2, v_1=R-delta(R)>=R/2 and v_2=R.
With u=max(1,floor(R/4)), every v_i>=u and, since R>=4,

    n<=4R<=32u, 2R+1<=n, q0=(2R+1)^2<=n^2.

All ceiling slack is included. For every 1<=D<=n and 0<=B<D, set
b_2=min(2R,B), b_1=B-b_2. Capacity gives 0<=b_1<=2v_1.
Zero widths return their child and B=0 returns a leaf. Each active
r_i=b_i+1<=2R+1, so product_active r_i<=q0. The full signed output
is divisible by 2^B and has |W|<2^(D-B)q0 after division by 2^B.
Its nonzero signed incidence over distinct leaf sets is proved by the
exact pair instrument. No high or zero label is filtered. Consequently
all fields have O(n+log q0)=O(n) bits, also after numerical errors.

The complete same all-integer proof is in the required budget appendix
Section 3. It covers every partial b and every root D,B. All attempts have
v_i>=u and address width A=O(log(n+2))=O(v_i), while full-label sums
have nk=O(R^2). Power-of-two padding changes addresses only.

The exact actual root/record parameters are

    Qroot=4096q0, Wroot=4096*2^R,
    Proot=4096n^2, K=2^17n, Hmax=2048K=2^28n,
    Qtot=Hmax*Proot=2^40n^3.

Qroot<=Proot is an integer parameter bound on all supplied states.
Every root starts fresh source/weighted counters. Check a copy before
acquisition. Check/charge a positive attempt after children are built
and before its array/query is initialized. A failed check ends only that
root and gives a neutral record, with prior children still counted.
Pad afterward with its separate Proot counter, then reset every nonrecord
buffer. All scheduled records/stages continue. Root EXTRACT uses P_label
Qroot; finite EXTRACT keeps the distinct old P_label_old=2^40n^4.

## G.2. Address layout and explicit bit controller

Pad each label, residue, found-string and scratch row to the least power
of two at least its actual length. Pad each of the fixed number of field
types separately. A row address is base+(row<<shift)+bit. Fixed local
history/node types have fixed offsets or separate arrays. No product of
two variable address words is required. The padded allocation is a fixed
multiple of the old allocation, so M_alloc=O(n^2) total bits and qubits, and

    a_addr=ceil(log2(M_alloc+2))=O(L).

Here a_addr denotes only the physical address width. The base proof's M
remains the odd part of N. All allocation and source symbols are local to
their stated proof; no analysis-only pool is allocated.

Padding is for addresses; arithmetic uses the stated signed/unsigned
widths. Unused padding is initialized and counted. It changes no residues,
sign bits, string length, candidate, source copy, or state transformation.
Quantum scratch remains O(n); classical allocation remains O(n^2).
Use the source's in-place reversible ripple adders and comparisons. Each
row clears and reuses O(b) carry scratch; the query and list-comparison
helpers use O(k). The original index, separate query and all active
helpers total O(k+b) qubits. No kb-node Boolean history is retained.
History/node fields above refer only to this reusable scratch.

Choose a uniform fixed-program bit controller with a fixed number of local
work tapes/heads for address words, loop strips and current bit arithmetic.
Count every bit read/write, head move, control test and fixed-size logic
step. Conservatively debit O(a_addr) fully charged work for each such raw step,
including local head moves. A known-label, residue, found-string or measured
bit can be read by the rules' classical indexed-bit access from its current
ready address, with the full a_addr debit. No serial walk across an unrelated
label or the whole data table is needed to fetch one indexed bit.

Keep a fixed number of current operand-address words in fixed fields. An
indexed gate directly uses those ready values and pays a_addr for each of its
fixed number of operand uses. The rule permits this; it does not require
a fresh serialized address/instruction copy before each gate. Every actual
address construction, copy, bit read or change is counted separately and
also receives the full indexed charge. There is no word-arithmetic unit
operation or free gate emission.

A fixed ripple bit gadget names a fixed list of these operand fields.
Set up all fields once at the start of a complete bit scan by O(a_addr) raw
bit actions: a fixed number of shifts, copies, additions or subtractions.
Their addresses include neighboring carries/history nodes and fixed outer
controls. Finite control selects those fields for each local exact
Clifford+T gate. To move to the next bit, update each pointer by its fixed
power-of-two stride. There is no full address copy at each local gate.

For a binary increment, a tape head starts at the pointer's low-bit marker,
reads/flips trailing 1 bits and the first 0 bit, then returns to the marker.
Decrement uses trailing 0 bits. A high-end marker detects full wraparound.
Each visited bit costs a fixed number of reads, writes, tests and head
moves. No separate binary bit cursor is copied, updated or cleared. All
actual head movements are counted. Including the fixed number of head
locations as O(a_addr) bits each does not change either space bound.

For m consecutive unit steps of a w-bit pointer from any start, bit h
changes at most floor(m/2^h)+1 times. The total is at most 2m+w. This
counts the carry walk and return up to a fixed factor. The same estimate
holds for decrement, reverse order and power-of-two stride. Therefore
all pointer-bit work for one complete m-position pass is O(m+a_addr) raw work.
This is deterministic amortization over the full generated scan, including
inert operations, and does not assert constant worst-case delay per gate.

Use marked loop strips for bit scans. A head moves one position for each
bit gadget and stops on the endpoint marker. Traversal, endpoint tests,
and rewind cost O(m+1) raw actions. No a_addr-bit equality test is made after
every bit. A fixed number of strips serves the one active attempt. Their
total length is O(n), within the existing classical space bound.

The signed-label width

    w_s=n+ceil(log2 q0)+4=O(n)

is fixed for the whole run. Build its strip, and fixed global counter/word
strips, once during charged polynomial setup. For the variable b-, k- and
short-counter strips of a new attempt, even a conservative O((b+k+1)a_addr)
raw construction is allowed below. They are built only after that
attempt's weighted check passes and reused for every iteration. Rewind
them by actual head moves. Never place an endpoint by an O(n)-cell walk
inside a b/k row or Grover iteration.

Consequently, one fixed number of complete m-bit ripple/copy/comparison
passes, including all loop ends, reverse passes and pointer setup, costs

    O(m+a_addr) raw actions.                              (P3)

Short scans retain the a_addr setup term. Pointer and loop state have fixed
template depth; no exponential instruction tape is stored.

## G.3. Short rows and the complete oracle iteration

A partially used PSG14C level can have b<u. Use its actual profile
u=max(1,floor(R/4)), n<=4R, and u<=v<=R. For R>=4, u>=R/8, hence
n<=32u. The finite smaller cases have absolute bounds. Consequently

    a_addr=O(log2(n+2))=O(u)=O(v).                         (P4)

This is the PSG14C substitution for the generic profile estimate. Thus
all b/k strip construction costs O((b+k+1)a_addr)=O(v^2) raw work once
per attempt, including a short partial row. No lower bound b>=u is used.

Form the k by b residue array by setting each child-label row address,
adding offset p once, and reading bits p,...,p+b-1. Read them by actual
indexed bit accesses. Signed two's-complement bits give the correct
(a_j/2^p) mod 2^b, including a negative divisible label. The original
signed field is long enough because p+b<=n-1. Copy each bit to its padded
residue row. By P3 this costs

    O(k(b+a_addr))=O(v^2) raw actions.                     (P5)

No full n-bit scan is made to seek each bit p; ready indexed addresses
are used. Row bases are set once per row in O(a_addr) raw work. Known-weight
reads inside an oracle use the same complete b-bit row scans. Every
residue bit is actually read. A zero constant bit can select an identity
slot, but its read, loop position and pointer work are still counted.

Computing f(z) uses k controlled b-bit additions. Their forward and
inverse words have P5 cost, including cleared carry scratch. Comparing
with e and its undo cost O(b+a_addr). At most 64 found strings are excluded
by complete k-bit equality passes, costing O(64(k+a_addr)). Their marking and
flag cleanup have the same order. Invalid list slots can use fixed inert
templates; all their controller work is counted. No quantum index reads
the list or weights. Therefore one full exact oracle costs

    O(k(b+a_addr)+b+a_addr+64(k+a_addr))=O(v^2) raw actions.         (P6)

Diffusion uses full H passes, a clean forward/reverse Toffoli chain and
the exact sign gate. Each chain uses ready adjacent pointers and P3, so
its total is O(k+a_addr)=O(v). All gate arities and exact Clifford+T words are
bounded. No approximate phase compilation is required.

The iteration count j uses w=ceil(k/2)<=v+1 bits. Drawing j, initializing
or copying its word, and a full decrement/limit test take O(w+a_addr)=O(v)
raw work. It is acceptable to make a full w-bit stop test after every
Grover iteration: this is time data, with width O(v), and P6 is O(v^2).
Each counter bit access and head return is counted. There is no exponential
unary counter or word-size arithmetic operation.

There are at most 4096 trials and fewer than J0=2^ceil(k/2)<=2^(v+1)
iterations per trial. Thus all complete oracle/diffusion words and their
iteration control in one discovery have raw work

    O(v^2 2^v).                                      (P7)

The scan bound is applied separately to every complete bit pass inside
each actual iteration, not to the subsequence of gates enabled by unknown
bits. Random j, found-list contents and quantum outcomes cannot increase
P7. A shorter classical trial/block schedule only removes complete words.

## G.4. All one-off attempt work and failure paths

The initial coherent f(y) computation, measurement/reset of its b-bit
register, and every fresh k-qubit query initialization, measurement and
reset use P3/P5. Classical candidate verification recomputes its exact
residue by full b-bit additions and scans every found k-bit string for
novelty. Its raw cost per trial is O(k(b+a_addr)+64(k+a_addr))=O(v^2). The 4096
trial cap is absolute. All fair bits and their counters are included.

Sorting and pairing at most 64 strings can use a fixed bounded number
of full k-bit comparisons and copies, each O(k+a_addr). Complete original-index
equality tests compute the success flag and constant-size pair ID by the
same templates. Their measurements, known-value resets and failed-projection
cleanup are counted. XOR by y0, a differing-pivot choice and affine clearing
use complete k-bit scans. Even O(k*a_addr) raw work to select/store that pivot
once is O(v^2). All of this fits P7.

After selection, compute the full signed output label from at most k child
labels using the two known strings. It uses O(k) complete w_s-bit signed
add/subtract passes and O(w_s) scratch, with the source proof's guard bits
and leaf-count bound. P3 gives O(k(w_s+a_addr))=O(nk) raw work. This cost is
paid once per attempt, not once per Grover iteration. The actual PSG14C
profile has n<=4R and k<=2R+1, so

    nk=O(R^2)=O(R^2 2^v).                                (P8)

This is the PSG14C substitution for the generic full-label estimate.
Negative labels and zero output labels use
the same complete signed scans and are not rejected by a new rule.

Clearing/freeing the residue array, fixed found list, strips and the
original/query/flag registers costs at most the complete scan counts
already above. If discovery stops on an empty block, or pair projection
fails, the same bound covers all work before discard and every actual
reset. A completed partial-width level is covered by P4--P8. The source
and weighted caps are checked before their actions. A weighted-cap abort
creates no oracle array or query registers; its children remain charged.
A source-cap abort while building children is covered by the retained
recursion/partial-stack bound in Section 5 below. There is no cap placed inside
an uncounted arithmetic or oracle word. A prefix of an actual bounded
attempt and its final cleanup cannot exceed these complete counts.

The weighted counter has O(R+L) bits. Its before-attempt addition/compare
can use complete scans in O(R+a_addr) raw work, within O(R^2 2^v). The source
counter is covered by the source-call and recursion bounds in Section 5. A single
failed weighted check ends that root call/record and has only polynomial extra cost.
No represented counter value determines an uncharged number of updates.

Combining P5--P8 gives O(R^2 2^v) raw work for every paid attempt. Debit
O(a_addr) to every bit/head action, every indexed gate and each of its fixed
number of operand uses. Since a_addr=O(L), this proves the charged attempt bound D1 below. The resulting
classical allocation remains O(n^2), including all loop strips, heads,
ready addresses, signed labels, the one active residue array and recursion
snapshots. Quantum allocation remains O(n).



## 4. Complete charged attempt and local-root sum

Sections G.2--G.4 use a uniform fixed-tape controller, ready operand words,
physical carry/head returns and marked strips. Every pointer operation,
known-bit access, head move, marker test, gate and fixed-arity address use
receives the full A indexed debit. A complete m-position pass costs O(m+A)
raw actions, including setup, all carries, endpoints, rewinds and inverse
passes. One isolated long carry can cost O(A); no O(L) worst-case charge
for each individual emitted gate is inferred from that full-scan bound.

For this source, local P4 is n<=32u and A=O(v_i); local P8 is
n k_i=O(R^2) since n=O(R). Thus the full attempt including residue-row
setup, discovery, all false trials, verification, finite exact gate words,
original-index projection, signed output, resets and release has

    O(R^2 A 2^v_i)=O(R^2 L2^v_i)
                 =O(n^2 L2^v_i) charged work.           (D1)

A short partially used row keeps its O(A) setup term. No n-cell endpoint
walk is made inside such a row or an iteration. The iteration's random
length and its O(v_i)-bit decrement/limit test are fully counted. Numeric
weights and found-list bits are actually read, including identity slots.
All quantum enables and malformed-state outcomes use the same bounded
literal templates. The claim is branchwise, not an expected search cost.

Each executed positive attempt was charged its nominal weight 2^v_i to
that record's local Wroot before execution. Its sum is at most Wroot on
every branch. With mstar=2, the complete combiner work in one record is

    O(R^2 L Wroot)=O(R^2 L2^R).                         (D2)

This includes all paid attempts in failed ancestors and all executed child
attempts before a parent cap or failed projection. There is at most one
failed weighted guard per root record; it ends the record, with only
bounded-depth release afterward. A source cap during child generation
also ends that root and releases its partial depth-first stack.

## 5. Fixed records, partial work and every remaining cost

There are at most 1536 odd stages. For h<hmax, log2 M<h+1 gives at most
8 stages. For h=hmax and R>=256, stride>=R/64 and n/R<=4 give at most
257; when R<256, Sodd<=n<=4R<1024. There are at most 192 multi-bit
2-adic stages because hmax=1+floor(R/32)>R/32, n<=4R, and their number
is ceil(a2/hmax)<=192. These bounds also cover a missing odd or 2-adic part.
Every stage obtains exactly K=2^17n isolated records, even after a wrong
prior estimate. Hence the number of actual root records is at most
1728K<Hmax=2048K=O(n). Dummy records only acquire/discard Proot copies;
they do not execute a root search. Sum (D2) over all actual records:

    T_comb=O(nR^2 L2^R)=O(n^3 L2^R)
          =O(n^(7/2)L2^(n/4)),                             (D3)

using (P-D2). Every bound here is for the fixed deterministic stage counts.
It does not depend on root success, record cleanliness or correct prefixes.

Recursion movement, zero-width returns, full-label metadata, source/work
counter checks, dirty reset, cap propagation and partial-stack release
retain their old conservative polynomial cost per source/attempt event.
All source events are bounded by Qtot=O(n^3), including rejected labels
and padding. Across all roots the number of paid attempts is at most

    O(n Wroot/2^u)=O(n2^(R-u)).

Since u=floor(R/4)>=floor(n/16), any fixed polynomial multiplying this
count is absorbed by (D3): divide by n^3 L2^R and use the bounded sequence
polynomial(n)2^-floor(n/16). The finite exceptional n enlarge one absolute
constant. This also covers work before a failed parent guard. Children
already executed remain in the local weighted sum; no parent query/strip
buffers are retained while new children are built. Failed final guard
checks add only O(n) polynomial events. No expected-resource assumption
is needed to charge these branches.

Root EXTRACT uses the exact P_label=Qroot. The finite branch keeps
P_label_old=2^40n^4, distinct from the new actual Qtot. Both precision budgets are O(n^4), so h_extract=O(log(n+2));
all original finite test rounds and numerical decoding are retained.
The old conservative O(n^2 L^2) charged source-call bound, source transform,
acquisition counter and reset work can be kept. Across at most Qtot copies
this is O(n^5 L^2), polynomial and absorbed by (D3). Padding copies do not
run EXTRACT, but even that conservative overcharge is safe. No label-error
parameter, local probability or conditional mean is changed by the stream.

Odd stages enumerate O(q0 2^h) candidates with K=O(n) stored records.
Frequencies, grid indices, all candidate residues and score sums use O(n)
bits. Exact classical arithmetic, table access, clamping, score comparison,
least-tie selection and each streamed residue update therefore cost a
fixed polynomial in n per candidate, including all indexed/generator work.
The new 2-adic decoder enumerates exactly 2^h candidates with the same
fixed K and arithmetic widths; it performs no odd-W rejection or parity
postselection. Its update g<-g+h is deterministic and stops after at most
192 blocks. A wrong previous scalar changes the shift/candidate values,
but no loop length, register width or guarded resource limit.

For either grid h<=hmax<=1+R/32. The full grid work over the constant
number of stages is at most polynomial(n)2^(R/32). Against (D3) its
positive 31R/32 exponential gap absorbs every fixed polynomial, since
R>=n/4. All product setup, inverse/residue arithmetic, direction/table
construction, source precision setup, profile search and CRT remain
charged polynomial computation. No grid enumeration or precision lookup
is removed by an asymptotic assertion.

All root padding and dummy records are physical acquisitions. They are
processed sequentially using one raw slot. Initialization, source n+1 cost,
reset, counters, branch tests and every index debit give at most
O(Qtot[(n+1)L+L^2])=O(n^4 L) charged padding work. Clearing scratch between
O(n) records adds a polynomial as well. These terms fit (D3). A neutral
root abort still pads to Proot and keeps the remaining scheduled loops;
there is no whole-run early abort to hide costs or change Qtot.

For n<256 keep the actual original one-copy shadow-record branch. It makes
mF=2^20(n+16)<=2^25n<=Qtot acquisitions for numerical records, enumerates
t=0,...,N-1 with its explicit exact scores, and pads to Qtot. Its quantum
workspace is reset between records. The finite N-search is charged
O(N polynomial(n)); the range n<256 has a finite resource maximum, so one
absolute outer constant covers it in the displayed time envelope. This is
an executable finite branch, not nonuniform advice. It includes N=2.

## 6. Simultaneous memory, exact counts and semantic transfer

The padded active labels, compact residue rows, found list and two
recursion frames use O(n^2) classical bits. Full signed labels have
O(n+log q0)=O(n) bits on all branches. The stage's K=O(n) classical
frequency/basis/sign records and streamed candidate residues use O(n^2)
more. A fixed number of O(n) strips, O(L)-bit ready operands/head locations,
root/global/padding counters and exact arithmetic buffers fits that same
peak. Reuse the record bank at the next stage; no exponential candidate
or gate-description table is stored. The O(R^2) low-residue array stores
b-bit DATA rows, not one instruction or O(L)-bit address per oracle gate.
Only a fixed number of ready operand fields is live. A stored O(R^2)-gate
instruction tape is not this controller and is not charged here.

The held sibling/current phases use at most B+1<=n qubits. Original-index,
separate query, each row's cleared/reused O(b) carry, source extraction and
arithmetic use O(n) live qubits. No O(kb) Boolean history is retained.
One source/padding slot and record resets fit the same peak. Physical
address padding multiplies these allocations by an absolute constant.
Thus S_C=O(n^2), S_Q=O(n), A=O(log(n+2)) self-consistently. Every such
address was charged in the complete stream above.

The compiler changes wire addresses/public generation only and executes
the identical controlled additions, comparisons, Grover words, pair
projection, measurements and numeric functions. It does not inspect a high
label in a new selection rule, reject a new value, reuse a root or measure
a root twice. It changes no root Qroot/Wroot guard, source transform,
EXTRACT precision, neutral abort record, clamped score or fresh basis.
The separate budget proof selects the new record padding and K; their
changed concentration and exact source/fault count are proved there.
The complete semantic root, source, selection and martingale proofs are
reproduced in psg_depth_two_base.md. The full new record/count/concentration
proof is reproduced in psg_depth_two_budget.md. These establish the
complete success/model statement for the selected implementation without
using a prior verdict.

In particular the actual positive K remains 2^17n when M=1. Only the odd
stage count is zero then; the power-of-two stages and fixed padding remain.
After the actual stages, dummy records fill the total to Hmax=2048K, each
with Proot=4096n^2 acquisitions. Main-branch total acquisitions are exactly

    Hmax*Proot=2048*2^17*n*4096*n^2=2^40n^3.

The finite branch pads to the same Qtot. These are branchwise identities,
including neutral roots and dummy copies. The exact unchanged adaptive
model with the selected fraction permits floor(Qtot/(8589934592n^2))=128n
bad copies. It is a
count among every acquired copy, not an independent corruption probability.
No source/reference/workspace promise is widened by this compiler transfer.

The output rule also stays total. Root failure yields a neutral flag, not
a substitute unmeasured phase. Odd scalar estimates are reduced modulo M
or set to 0 when skipped. Each 2-adic least maximizer has h bits; updating
t0 and g preserves their declared finite widths. The final residue is
(s1+M*t0) mod N. The finite branch returns its least maximizing t in [0,N).
No malformed outcome can enlarge the following allocation or index range.

Using the complete reproduced semantic and new-budget proofs, this
selected implementation has jointly for every N,s and allowed
adaptive adversary

    T=O(n^(7/2)L2^(n/4)), S_C=O(n^2), S_Q=O(n),
    Q=1099511627776n^3 exactly,
    epsilon(n)=1/(8589934592n^2), success>=1-2^-8.              (D4)

Use L=log2 n for n>=2; n=1 is the finite branch, or regularize by log2(n+2).
The representative growth indices remain [1,0,0,0], and time logPower is 1.
The main proof and required base/budget appendices contain the full
semantic model and success proof; this file contains the complete selected
controller and all work/space charges. All five claims cite all four files.
