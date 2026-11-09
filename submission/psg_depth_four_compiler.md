# Complete online compiler and joint resources for PSG-D4

This required appendix selects the ONE actual PSG-D4 program in
psg_depth_four.md, with psg_depth_four_base.md and
psg_depth_four_family.md. All five claims cite all four proof files.
The program fixes d=4; all constants below are absolute. Its complete
local controller source is psg_depth_two_compiler.md, hash
ec581df033589d913337deebc4bb2f2bdb57b2b364720999b85ed83c2a0f37ff.
The G.2--G.4 implementation is retained with the proved n<=8R<=64u
substitution. The exact full S371 controller source has hash
4ff058eb9aa0f631126cd8443b691aa72d3d1ec7884dec06a5236542f71f79c1.
Public/local/inherited chronology is in main Section 6 and the family
source record. No gate-generation oracle or prior verdict is assumed.

## 1. Exact selected profile and counts

For n>=n_4=2^256, put ell=ceil(log2 n). Scan integer trials starting
at R=ceil(n/8). For each trial compute

    c=ceil(log2(3(2R+1))), v_i=R-(4-i)c, i=1,...,4.

Take the first trial with v_1>=ceil(R/2) and 8R-12c>=n. No capacity
monotonicity is used. The feasible trial
Rtest=ceil(n/8)+ceil(3(ell+2)/2) proves

    n/8<=R<=n/8+(3/2)log2 n+13/2,
    2^R<=2^(13/2)n^(3/2)2^(n/8), R<n/3,
    v_i>=R/2>=u=floor(R/4)>=R/8,
    n<=8R<=64u, 2R+1<=n, q0=(2R+1)^4<=n^4.

All ceilings, positivity and scalar bounds are proved for this entire
range in psg_depth_four_family.md Section 3 with fixed d=4. The search
uses O(log(n+2)) trials and explicit integer arithmetic. For each
1<=D<=n and 0<=B<D, allocate b_i=min(2v_i,remaining) from i=4 down
to 1, then reduce remaining. Capacity makes the final remainder zero.
Set r_i=b_i+1 and p_i=sum_(j<i)b_j. Skip a zero width; B=0 returns
one leaf. Each positive width uses k=b_i+1 children, the exact primitive
below, and its nominal weight 2^v_i. Every returned tree has at most
product_active r_i<=q0 nominal leaves. Its full signed label is 2^B W,
with |W|<2^(D-B)q0 and a nonzero signed incidence on disjoint leaves.
All fields have n+ceil(log2 q0)+4=O(n) bits. High and zero labels are
not filtered. These rules cover every partial and zero-width tree.

    d=4, n_4=2^256, C_4=7, q0=(2R+1)^4,
    Qroot=7168q0, Wroot=8192*2^R,
    K=2^17n, Proot=7168n^4, Hmax=8192K=2^30n,
    Qtot=7*2^40n^5=7696581394432n^5 exactly,
    epsilon(n)=1/(7*2^33n^4)=1/(60129542144n^4).

Root EXTRACT uses P_label=Qroot. Finite EXTRACT uses the distinct
P_label_old=2^40n^4. Root, weight, record-padding and whole-run counters
are distinct. An overflow aborts only that root, gives a neutral score,
pads to Proot and resets. The whole fixed schedule continues. All
literal source transforms and finite helpers are in the base appendix.

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

A partially used PSG-D4 level can have b<u. Use its actual profile
u=max(1,floor(R/4)), n<=8R, and u<=v<=R. For R>=4, u>=R/8, hence
n<=64u. The finite smaller cases have absolute bounds. Consequently

    a_addr=O(log2(n+2))=O(u)=O(v).                         (P4)

This is the PSG-D4 substitution for the generic profile estimate. Thus
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
paid once per attempt, not once per Grover iteration. The actual PSG-D4
profile has n<=8R and k<=2R+1, so

    nk=O(R^2)=O(R^2 2^v).                                (P8)

This is the PSG-D4 substitution for the generic full-label estimate.
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
number of operand uses. Since a_addr=O(L), this proves the charged attempt bound in Section 4 below. The resulting
classical allocation remains O(n^2), including all loop strips, heads,
ready addresses, signed labels, the one active residue array and recursion
snapshots. Quantum allocation remains O(n).



## 4. Hard local work and total combiner time

The complete scans above give O(R^2 A2^v_i) charged work for every paid
attempt, with A=O(log2(n+2)). Every bit/head action, known-bit access,
exact gate, inverse and fixed-arity ready-operand use pays the full
indexed debit. Partial rows keep O(A) setup. No instruction tape is
stored and no free address emission is assumed. Children in failed
ancestors and final cleanup remain charged. Each positive attempt is
charged its nominal 2^v_i before execution. The hard root sum is at most
Wroot=8192*2^R; one root therefore costs O(R^2 log2(n+2)2^R).

There are at most 770K actual roots, K=2^17n. Dummy records only
acquire/discard. Thus

    T_comb=O(nR^2 log2(n+2)2^R)
          =O(n^(9/2)log2(n+2)2^(n/8)).

The equality uses R<=n/8+(3/2)log2 n+13/2 and n=Theta(R).
It retains the literal R^2 cost; no smaller outside power is selected.
All arbitrary source states, neutral records, failed projections and
wrong earlier scalar estimates obey these same literal hard bounds.

## 5. Every remaining charged operation

The full same proof is included in psg_depth_four_family.md Section 10,
with d=4 fixed. It gives explicit finite absorption of every following
charged term; none is a successful-branch or expected-resource argument.

There are exactly Qtot=7*2^40n^5 source events. Charging the conservative
complete O(n^2 log2(n+2)^2) source/transform/extraction/reset/counter
bound to all of them gives O(n^7 log2(n+2)^2). Padding runs only
acquire/discard, raw n+1 cost, initialization/reset and bounded counters;
this conservative overcharge covers it. Main precision Qroot=O(n^4)
and finite precision 2^40n^4 both give precision parameter h=O(log(n+2)).
All fixed collective rounds, numerical tests and unwrapping are retained.

Recursion, zero-width returns, metadata, source/weight guards, partial
stack release, dirty resets and cap propagation use polynomial(n) work
per source/attempt event. Source events have a polynomial total. Positive
attempts have weight >=2^u; their total number is O(n2^(R-u)), with
u>=n/64. A fixed polynomial times this count fits the combiner bound
by the positive 2^-u gap. At most one failed final source/weighted
check ends each root and propagates over four frames. Already built
children remain charged; no parent query/strip buffers are kept while
replacement children are built.

Odd grids have O(q0 2^h) candidates, including full stage zero. Multi-bit
grids have exactly 2^h candidates and no odd-W filter. Each score reads
K records and performs exact O(n)-bit arithmetic, table access, clamping,
least-tie comparison and streamed remainder updates. With h<=1+R/32,
all grid work is polynomial(n)2^(R/32). Its positive 31R/32 gap absorbs
the fixed polynomial. Profile search, CRT, source parameters, table
construction, memory layout, counters, strips and head setup are charged
polynomial work. No numerical oracle or uncounted preprocessing is used.

For each p>=0 and a>0, x^p exp(-ax) on x>=1 is bounded by
max(1,(p/(ae))^p). Use a=ln2/64, 31ln2/256 or ln2/8 for the above
absorptions. All polynomial degrees and coefficients are finite and
absolute now that d=4. On n<2^256 the actual finite procedure makes mF
one-copy records, scans t=0,...,N-1, saves its least maximizer and pads
to Qtot before returning. The maximum primitive loop count over the
finite input-size range is finite and computable, independent of input
states/outcomes. Multiplying the positive whole-domain representative
by that finite constant covers the branch, including N=2. There is no
stored solution, advice or validity threshold.

## 6. Simultaneous space, exact source count and output

The depth-first held/current sibling count is B+1<=n. Original-index,
separate query, reused row carries, source/transform/extraction, one
padding slot and resets add O(n) live qubits. No parent query array is
allocated during child generation, no kb-node quantum history is kept,
and the collective remainder uses only six O(n)-scratch passes. Thus
S_Q=O(n) on all branches.

O(n) full signed labels of O(n) bits, one compact k-by-b residue DATA
array, the fixed found list, four metadata frames, K=O(n) bounded
records, streamed candidate residues, exact arithmetic, counters,
O(n) strips, O(log(n+2)) head locations and a fixed number of ready
operand fields use O(n^2) classical bits together. Banks are reused
between stages. No exponential grid table, gate-description tape or
symbolic leaf tree is stored. Source counters have O(log(n+2)) bits;
the weighted counter has O(R+log(n+2)). The finite branch has O(n)
records and the same peaks. Padding addresses changes only a constant.
This proves A=O(log(n+2)) self-consistently for the actual allocation.

All roots use Qroot<=Proot on every state. At most 770K actual records
are followed by enough Proot-copy dummy records to make Hmax=8192K.
Consequently every main branch acquires exactly

    Hmax*Proot=(2^30n)(7*2^10n^4)=7*2^40n^5.

The finite branch pads to the same count, which exceeds mF for every
n>=1. The stated fraction gives exactly 128n permitted bad copies.
Quantum resets and later padding cannot change the saved classical
candidate. Odd outputs are reduced modulo M, a 2-adic update appends
one h-bit residue, and the final result is (s1+M*t0) mod N. Local
aborts give neutral records and do not skip stages or final padding.
All malformed-state and wrong-scalar branches have bounded encodings.

The exact source, selection, decoder, model and success proofs are
contained in the other three required files. Together these proofs
establish, for this one program and every N,s,allowed adversary,

    T=O(n^(9/2)log2(n+2)2^(n/8)), S_C=O(n^2), S_Q=O(n),
    Q=7*2^40n^5 exactly, epsilon=1/(7*2^33n^4),
    unconditional full-secret success>=1-2^-8.

Growth indices are 1,0,0,0. All constants are absolute. No result from
another algorithm or source verdict is used as a proof premise.
