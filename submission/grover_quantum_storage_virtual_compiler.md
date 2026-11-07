# Required virtual Dense P appendix

This file specifies ONLY the virtual Dense machine P used by
[the physical storage algorithm](grover_quantum_storage.md) and
[its complete simulator](grover_quantum_storage_transfer.md).
Every algorithm name, resource assertion, allocation statement, controller
assertion, work/space/source bound and physical-implementation description
in the source body below refers to P, its virtual classical memory and
its original quantum registers. None is a claim about this package's
physical classical allocation. P's full mathematical source, success,
guard, primitive, circuit, decoder and finite-case proofs are retained.
The new physical resource and simulation claims are established in the
physical main and transfer files. Every copied local proof filename is
rebound to this package's corresponding virtual appendix. Source provenance,
historical comments and exact source hashes retain their original meaning.
An old acceptance/review statement is provenance, not a proof premise.

## Complete virtual source body

# Required appendix: PSG2-DENSE-E controller and extraction

This appendix, `grover_quantum_storage_virtual.md`, `grover_quantum_storage_virtual_caps.md`,
`grover_quantum_storage_virtual_oracle.md`, `grover_quantum_storage_virtual_dense.md` and
`grover_quantum_storage_virtual_bound.md` define one complete algorithm. Part A gives
all ready-address/direct-row helpers retained for comparison, list,
verification, signed output and reset work. Part B gives the complete
literal stored-tape controller selected for every G1 pass. Part C gives
the complete RUN(F) source-label extractor selected by main Section 3.1.
All source, probability, decoder and cap premises are in this package.

The exact copied construction sources are:

- `grover_stride_retry_l2_compiler.md`, SHA256
  697869d57d7603de1f39e712189cf26dc1cf2f8d8324ef32a103836c3bdf1243:
  complete ready-address helpers and RUN(F) proof.
- `stored_oracle_stream.md`, SHA256
  366497582e1c87ceb0e2e48ecf5aa40e7e3ad52b86ec3e4cf09d2a49da167927:
  the complete physical-tape interpreter, forward/inverse, construction
  account and program-size argument, reproduced in Part B.
- Their earlier actual own-source pins remain in main Section 0 and in
  Part B. They record provenance, not outside mathematical premises.

The exact local compiler before adaptation was
cf4b575204c25ef8a0911fd4ebefca5ce465267acd91931d14569584d9cf551d.
Current helper instructions use k=b+5, at most2048 strings and2^18 trials,
J0<=8*2^v and the exact cyclic postprocessing in dense Section 3.
All source-call error unions below use only Qcap_dense<=Qcap_old; no
comparison with the old auxiliary Qcap_new is asserted. The old q0,C,
precision/pool and Wcap are proved for this dense configuration in the
required dense appendix. Parts A/B count all current helper/program work;
Part C's complete extractor is unchanged except for its actual call bound.
Historical pins and Part D are provenance, not old executable instructions.

## Part A. Ready-address helpers

Put n=ceil(log2 N), L=log2 n. The main profile has
u=floor(sqrt R), u<=v<=R, 0<b<=2v, k=b+5<=2v+5,
n<=2R^2, R<(u+1)^2, R^2=O(nL), and Wcap=O(n2^R).
A zero-width level executes no attempt. In A3, the direct sum circuit is
only the direct helper; grouped G1 is proved in the oracle appendix and
is always replayed by Part B. The other helper bounds below apply to the
actual separate scans of this algorithm. One-off signed output arithmetic
is paid once per attempt, after selection, and is not inferred from G1's
gate count. The retained labels, helper allocation and all abort work
are counted together with the program and grouped pool.

### A2. Address layout and explicit bit controller

Pad each label, residue, found-string and scratch row to the least power
of two at least its actual length. Pad each of the fixed number of field
types separately. A row address is base+(row<<shift)+bit. Fixed local
history/node types have fixed offsets or separate arrays. No product of
two variable address words is required. The padded allocation is a fixed
multiple of the old allocation, so M_alloc=O(n^2) total bits and qubits, and

    a_addr=ceil(log2(M_alloc+2))=O(L).

The source's large conceptual analysis pool is still named A. It is not
allocated and is not included in M_alloc. Here a_addr denotes only the
address width. The source's M remains the odd part of N.

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

### A3. Direct-row and short-scan helpers

A partially used profile level can have b<u. We do not assume b>=u,
or hide row setup in b in that case. Instead, the fixed profile gives

    n<=2R^2<2(u+1)^4,
    L<1+4log2(u+1)<=5u,
    a_addr=O(u)=O(v).                                     (P4)

The last inequality uses u>=1 and log2(u+1)<=u. All constants are absolute.
Thus all b/k strip construction costs O((b+k+1)a_addr)=O(v^2) raw work once
per attempt, even for a short partial row.

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

For the direct-row helper only, computing f(z) uses k controlled b-bit additions. Their forward and
inverse words have P5 cost, including cleared carry scratch. Comparing
with e and its undo cost O(b+a_addr). At most 2048 found strings are excluded
by complete k-bit equality passes, costing O(2048(k+a_addr)). Their marking and
flag cleanup have the same order. Invalid list slots can use fixed inert
templates; all their controller work is counted. No quantum index reads
the list or weights. Therefore one full exact oracle costs

    O(k(b+a_addr)+b+a_addr+2048(k+a_addr))=O(v^2) raw actions.         (P6)

Diffusion uses full H passes, a clean forward/reverse Toffoli chain and
the exact sign gate. Each chain uses ready adjacent pointers and P3, so
its total is O(k+a_addr)=O(v). All gate arities and exact Clifford+T words are
bounded. No approximate phase compilation is required.

The iteration count j uses w=ceil(k/2)<=v+3 bits. Drawing j, initializing
or copying its word, and a full decrement/limit test take O(w+a_addr)=O(v)
raw work. It is acceptable to make a full w-bit stop test after every
Grover iteration: this is time data, with width O(v), and P6 is O(v^2).
Each counter bit access and head return is counted. There is no exponential
unary counter or word-size arithmetic operation.

There are at most 2^18 trials and fewer than J0=2^ceil(k/2)<=2^(v+3)
iterations per trial. Thus all complete oracle/diffusion words and their
iteration control in one discovery have raw work

    O(v^2 2^v).                                      (P7)

The scan bound is applied separately to every complete bit pass inside
each actual iteration, not to the subsequence of gates enabled by unknown
bits. Random j, found-list contents and quantum outcomes cannot increase
P7. A shorter classical trial/block schedule only removes complete words.

### A4. One-off attempt work and failure paths

The selected coherent f(y) word is G1 in the oracle appendix. Its direct
branch has P3/P5 cost. Measurement/reset of its b-bit register and every
fresh k-qubit query initialization, measurement and reset use P3. Classical candidate verification recomputes its exact
residue by full b-bit additions and scans every found k-bit string for
novelty. Its raw cost per trial is O(k(b+a_addr)+2048(k+a_addr))=O(v^2). The 2^18
trial cap is absolute. All fair bits and their counters are included.

Sorting at most2048 strings uses a fixed bounded number of full k-bit
comparisons/copies. Complete membership and eleven-rank-bit scans use
reusable equality helpers. The cyclic instrument, exact all-encoding
rank permutation, changed-rank measurement and x_t/x_next clearing are
fully specified in dense Section 3. Their generated word and resets have
paid polynomial work and O(1) extra rank/permutation quantum helpers.
All cyclic output selection, sorting and cleanup are paid once per attempt;
they are not hidden in G1 or repeated at every Grover iteration.

After selection, compute the full signed output label from at most k child
labels using the selected x_t and x_next strings. It uses O(k) complete w_s-bit signed
add/subtract passes and O(w_s) scratch, with the source proof's guard bits
and leaf-count bound. P3 gives O(k(w_s+a_addr))=O(nk) raw work. This cost is
paid once per attempt, not once per Grover iteration. The profile gives

    R<(u+1)^2<=4*2^u<=4*2^v, k<=2R+5, n<=2R^2,
    nk=O(nR)=O(R^3)=O(R^2 2^v).                      (P8)

The inequality (u+1)^2<=4*2^u holds at u=1,2 and then follows because
((u+2)/(u+1))^2<=2 for u>=2. Negative labels and zero output labels use
the same complete signed scans and are not rejected by a new rule.

Clearing/freeing the residue array, fixed found list, strips and the
original/query/flag registers costs at most the complete scan counts
already above. If discovery stops on an empty block, or cyclic membership/rank postprocessing
fails, the same bound covers all work before discard and every actual
reset. A completed partial-width level is covered by P4--P8. The source
and weighted caps are checked before their actions. A weighted-cap abort
creates no oracle array or query registers; its children remain charged.
A source-cap abort while building children is covered by the retained
recursion/partial-stack bound in Section 5. There is no cap placed inside
an uncounted arithmetic or oracle word. A prefix of an actual bounded
attempt and its final cleanup cannot exceed these complete counts.

The weighted counter has O(R+L) bits. Its before-attempt addition/compare
can use complete scans in O(R+a_addr) raw work, within O(R^2 2^v). The source
counter is covered by the source-call and recursion bounds below. A single
failed weighted check ends the run and has only polynomial extra cost.
No represented counter value determines an uncharged number of updates.

P5--P8 give conservative polynomial one-off helper bounds and the direct-row
scan bounds. Debit O(a_addr) to every bit/head action and each indexed
operand use in these helpers. The selected G1 word itself is executed by
Part B, including on direct rows. Its grouped workspace/history is bounded
in the oracle appendix. All one-off signed output, reset and cleanup work
here is paid polynomial work; main Section 9.5 absorbs it only after it is
counted. Helper strips, heads, addresses, labels, the residue array and
recursion snapshots fit O(n^2) classical bits and O(n) quantum scratch.


## Part B. Literal stored gate program

### B1. Exact rules and scope

The exact local dcp/rules.md has SHA256
7be4f5f1137aea419a481bf31482bebc5a8f8cbb15dd2296872fce6dbad7a469.
Its computation/resource clauses, lines 25--43, require a uniform
classical controller, count bit work, circuit generation, memory access,
initialization and all attempts, and allow classically chosen gates on
arbitrary indexed wires. The extra address debit is attached to a
"classical indexed access or classically addressed gate". Write

    A_addr=ceil(log2(M_alloc+2)),

where M_alloc counts all allocated classical bits and qubits, including
the stored program. Fixed-size logic is unit cost. Stored descriptions
count in S_C. No stored instruction or source-related table is free.

The relevant fixed supplier source is grover_stride_retry.md, SHA256
515f4eb6b8c02806e8e0f3ba60c3f5a19cb3e13e2b80485dc85347c2e42a007b,
with grover_stride_retry_caps.md, SHA256
97abcaeed66e3d88a200045a1a69128212afc1dd7adbaea237c988ec49b3603e.
The locally derived ready-address stream in grover_stride_compiler.md,
SHA256 4c5bcd59c95fa2c10be21ab610cdfe76f6b8d2d31300582b97417a7f5b7e896f,
is another source for this implementation method. That proof conservatively
debits A_addr to all local tape actions. This part proves the actual cost for physical sequential tape actions.
Part A retains the conservative indexed allowance for its separate helpers.

For n>=256 put L=log2 n. The supplier has

    u=floor(sqrt R), v>=u, n<=2R^2<2(u+1)^4,
    R^2=O(nL), Wcap=O(n2^R).

Consider a complete single Grover-iteration word of G elementary fixed-arity
exact Clifford+T gates. Include the whole membership reflection, its
compute/uncompute word, all found-list tests and diffusion in G, or count
a separately streamed list part explicitly. The compiler lemma requires:

1. G=O(R^2), and at most a fixed number of wire operands per elementary gate.
2. The word has a uniform deterministic polynomial-bit-work constructor
   using O(n^2) classical bits, including any wire-allocation/schedule maps.
3. Its quantum implementation, including all live history, has the claimed
   O(n) qubits. Gate count alone is not a quantum-space proof.
4. Its classical parameters are fixed while the word is reused. The
   known residues and measured e are fixed for one attempt; a changing
   found list has at most 2048 additions in that attempt.

Under these conditions the complete program can be stored in O(n^2)
classical bits and streamed at O(L) fully charged work per elementary gate.
All construction and bounded rebuilds are counted. The following sections
give the literal machine and the limit of this claim.

Here G counts stored elementary instruction slots. A constructor may omit
a known identity operation. If it retains that operation as a tape frame,
the frame counts in G. No omitted gate is allowed an uncounted instruction.

### B2. Current-cell tape action and indexed access

Choose a uniform finite-program, fixed-multitape bit controller. A local
tape action reads or writes the cell currently under a fixed head, or
moves that head by one cell. It has no numeric address input and does not
select a cell from a binary index. Each read, write, finite-control test
and head move is one fixed-size bit action. Count all of them. A fixed
finite alphabet is encoded by a fixed number of bits per cell, also counted.

This is a concrete implementation of the allowed uniform classical
controller. Reading its current cell is a memory access and costs its
actual bit work. It is not a classical indexed access: the operation
takes no integer index. Therefore the rule's additional address debit
does not apply to this local action. The rule separately names indexed
accesses; charging all current-cell reads as indexed operations is a
different implementation/cost assumption. The proof does not delete an
indexed charge from any operation that actually uses a numeric address.

In particular, a random-access read/write of a source-label bit, known
weight, schedule entry, construction array or found-string bit pays the
full A_addr indexed charge whenever performed that way. Constructing or
changing an indexed pointer is real bit work. The quantum gate's wire
operands always receive their full indexed charge. There is no quantum
lookup into the program, no word-read primitive and no arithmetic opcode
acting on an unbounded integer.

The machine head location is part of its current configuration. Include
O(log(M_alloc+2)) bits of location information per head in the space upper
bound. The implementation does not maintain a redundant binary copy of
each physical head location. Its left/right operation is one counted
local head move, not an omitted update of a numerical address register.

For comparison, if this machine is implemented by indexed RAM reads and
writes, each instruction-bit access pays A_addr. Loading Theta(L) bits
then costs O(L A_addr)=O(L^2), before applying its gate. That implementation
has no O(L)-per-gate conclusion from this lemma. Both the actual physical
tape actions and the indexed-RAM limit are explicit. A claim that merely
calls an indexed array a tape would not establish the lower cost.

### B3. Program representation and counted storage

Choose a public operand width a=O(L) large enough for every allocated
wire/bit address, including the program and interpreter. One may take
a=c0+4ceil(log2(n+2)) for a sufficiently large absolute c0, using the
explicit polynomial allocation bounds of the constructor. Leading zero
bits are stored and read too. In the resulting allocation A_addr<=a.

An instruction has a tag of fixed bit length and a fixed maximum number d
of a-bit operand fields. Unused operand fields contain dummy zero bits;
they are still counted. Store actual elementary gates, with all arithmetic
and control gadgets expanded into finite exact Clifford+T words. The tag
alphabet is fixed, for example H,S,S-dagger,T,T-dagger,CNOT and X. An exact
Toffoli macro can first be expanded by its fixed decomposition. There is
no tag for a variable-width adder, lookup, or whole oracle call.

Use fixed delimiter/marker tracks for field ends, instruction ends and
the two program ends. These tracks are a fixed number of bits per tape
cell. They distinguish structure from arbitrary operand data. A current
symbol read examines only a fixed number of bits. The frame length is

    F=da+O(1)=O(L).

The program occupies O((G+1)a) bits, including its markers, initial/terminal
records and padding. Since G=O(R^2)=O(nL),

    program bits = O(nL^2)=O(n^2).                    (S1)

For n>=256, L^2<=n; the same O(n^2) bound covers any finite smaller range.
The pre-existing labels, residue/list tables and recursion state already
use O(n^2) bits. The constructor's O(n^2) scratch and the new program may
coexist, giving O(n^2) peak bits. A fixed number of a-bit ready operand
words, fixed tag state, local strip markers and head locations add O(L).
The program adds no quantum storage. The source's conceptual pool A is
not allocated and is not included in M_alloc.

There is no circular address assumption in S1. The chosen a is the bit
length of a public polynomial allocation cap. Inserting it into the
program length gives O(nL^2), hence the resulting actual allocation is
O(n^2) and every actual address fits that cap. Enlarging the fixed c0
covers all absolute constants and small n. A_addr is still computed from
the actual entire allocated memory, not just one oracle buffer.

### B4. Literal interpreter, tag decode and inverse

The program head visits its tape in physical order. A fixed number of
operand work tapes have a-bit fields with fixed low/high markers. They
hold the current ready addresses used by the indexed gate primitive.

For each forward instruction:

1. Read its fixed tag bits sequentially. Update a finite decoder state
   once per bit. A tag from a fixed alphabet needs only constant logic.
2. Read each of the fixed d operand fields one cell at a time. For each
   bit, read the program cell, write the corresponding current operand
   cell and move the two heads. Field markers terminate the scan. Return
   the operand head to its low marker by actual head moves. Overwriting
   the old field counts every bit; no full word is loaded in one step.
3. Apply the named fixed gate using those ready operand words. Pay the
   full A_addr debit for each of its at most d operands, as a conservative
   charge, as well as the elementary gate's unit work.
4. Read the instruction-end marker and move to the next frame. A program
   end marker terminates the pass. No numerical instruction counter or
   full-address comparison is performed after each instruction.

Step 2 uses O(a) actual bit reads, writes, marker tests and head moves.
The other local actions cost O(1). The quantum operation costs O(A_addr).
Thus one instruction costs O(a+A_addr)=O(L) fully charged work. The actual
operand bits are copied; direct ready-address use avoids a second copy
after that load. Its address-use debit is still paid on every gate.

At the end of a forward pass, rewind the program head until its left-end
marker is reached. Read that marker track at every visited cell. This is
O((G+1)a) actual reads/head moves. It is included once per reused word;
it is not a unit reset. Quantum data are not accessed during this rewind.
Clearing the current operand words, if required, costs O(a) local actions.

To execute the exact inverse, begin at the right-end marker and read
complete frames backward. Operand fields arrive in reverse order and
are copied high-to-low into their corresponding fixed fields; markers
stop each copy. Read the fixed tag bits in reverse and apply the fixed
inverse-tag map after loading the operands. This emits the inverse gates
in reversed order. H and CNOT are self-inverse; S/T exchange with their
inverse tags. If an inverse is represented by a fixed longer word, count
all of its constant number of instructions/gates and address uses.

The tag map is finite and uniform. There is no reversal of an unknown
source state or source-preparation circuit. It is the literal inverse
of the compiled known unitary. Repositioning either tape head and clearing
work after a reverse pass have the same counted scan length. Therefore
each complete forward or reverse pass, including its actual head return,
has charged work

    O((G+1)L).                                       (S2)

Every program gate is executed even if its quantum control is zero. A
template compiled under a classical zero bit can include an inert slot;
its instruction-bit reads and head work remain counted. The bound is over
complete actual scans and does not average over enabled quantum gates.

### B5. Uniform construction, changing lists and counters

Build the program only after the attempt's weighted check passes. The
constructor reads its known residues, e and current found strings by
counted accesses. Each actual indexed access pays A_addr. Generate every
tag and every operand-address bit, write all program and marker bits,
initialize ready fields and clear any previous program explicitly. All
work, including allocation maps, offset arithmetic, source-array access
and tape seeks, belongs to construction. It is bounded by a fixed
polynomial P(n) under condition 2 of B1.

This does not infer construction cost from gate count. For the original
bounded oracle, the existing ripple/row constructor is explicit. For this grouped oracle, required oracle Section 8 supplies the full
uniform polynomial-work schedule and allocator with O(n^2) classical
storage, including explicit O((H+kb+n)a^3) charged construction. A
conservative compiler with short-word arithmetic and indexed lookups is
used in that construction. For example O(G L^3) charged construction
work is polynomial and is not charged at every replayed gate. Writing
O(G L) output bits is always included.

One complete word includes its own compute/uncompute instructions and
diffusion. It can be reused for all j iterations of a trial. Here
j<2^ceil(k/2)<=2^(v+3). The program has polynomial size; the exponential
number of iterations is represented only by the existing small binary
iteration counter, not by a repeated stored program.

The counter has ceil(k/2) bits. A full sequential zero test, carry/borrow
update, copy or reset costs O(k) actual tape actions. Its loop control
is fully counted. A complete diffusion contains Omega(k) elementary
gates, so G+1=Omega(k); these counter steps fit O((G+1)L) per iteration.
Sampling its fair bits, query initialization, measurements, verification
and resets remain counted. They have bounded polynomial work per trial.
There are at most 2^18 trials per attempt, an absolute constant.

The measured e and residue weights are fixed for the whole attempt. A
new verified solution changes the found list at most 2048 times. Rebuild
the whole program after each change, or stream the O(2048k) exact list
tests separately with their existing complete-scan proof. In the full
rebuild version there are at most 2049 list states, hence at most 2049 complete
constructions/clears. Diffusion depends only on the fixed k. Trial coins
do not require rebuilding the word. Even rebuilding per trial would give
only a fixed 2^18 factor, but the stated implementation reuses by list state.

If the list changes, finish the current measured trial before clearing
its program; no gate word is modified during its coherent execution.
All failed searches, empty blocks, discarded queries and failed cyclic
postprocessing still execute a bounded sequence of complete words. Their
classical/quantum resets and final program erase are included in P(n).
A weighted-cap failure starts no program construction. A source-cap
failure during child construction is covered by the existing child/stack
account. A final incomplete attempt and its cleanup cost at most the
same bounded construction/trial counts. No success-conditioned cost is used.

### B6. Absorbing construction and applying the gate bound

The global profile gives n<2(u+1)^4, R<(u+1)^2 and L<=5u. Therefore any
fixed polynomial P(n), including all 2049 constructions and 2^18 one-off
trial/verification/reset costs, is at most C(u+1)^c for fixed constants.
Since (u+1)^c 2^-u is bounded on positive integers,

    P(n)=O(2^u)=O(2^v).                              (S3)

This is an absolute asymptotic absorption, including its finite prefix.
It is not free preprocessing. It applies to all partial b<u levels too:
the same nominal v>=u is charged before their construction. Zero-width
levels create no program and remain in the existing recursion account.

Let G_max(n) bound the actual complete single-iteration gate count for all
positive-width attempts of one configuration, with G_max+1>=1. S2, S3 and
the fixed trial cap give the complete program/discovery cost per attempt

    O((G_max+1)L2^v).                                (S4)

All source-array construction accesses and instruction output bits are
in the paid P(n). No hidden indexed read occurs at replay. Summing S4
over attempts whose nominal weights were already charged yields

    O((G_max+1)L Wcap)
      =O(n(G_max+1)L2^R).                            (S5)

The supplier's other previously charged terms consist of fixed polynomials
plus polynomial(n)2^(R-u) bounds for source calls, recursion/reset/abort
movement and the seed, as detailed in its full work account. Their ratio
to the S5 upper envelope is bounded by polynomial(u)2^-u, using
n<2(u+1)^4 and G_max+1>=1. They therefore remain absorbed even after a
fixed polynomial reduction in the single-iteration gate bound. The
backward decoder and finite setup remain polynomial. Any full new package
must reproduce the exact remaining-term account for its chosen circuit.

For this configuration the required oracle appendix proves the specific
G1 word with H=O(n log2(L+2)) elementary slots, O(n) quantum space and a
uniform polynomial constructor with O(n^2) classical storage. Every mask,
selected-copy address and bit-heap wire address is materialized in that
constructor. These are proved package-local facts, not external inputs.

Store G1 once per attempt. For the initial coherent f(y), main Section 4.1
and oracle Section 9 specify k CNOTs y->clean z, replay G1(z,A), then the
same k CNOTs to clear z, before measuring/resetting A. G1 preserves z,
so this gives the exact original-register map with the fixed query-wire
addresses and with arbitrary reference systems. The separate query is
already allocated and is reused for discovery. Count all 2k indexed gates
and their address debits as paid one-off work under S3.
For a membership reflection, execute G1 forward, perform the complete
comparison/list phase, and read it backward for the exact inverse.
The c_j and wire map are fixed. Neither e nor a changed found list changes
G1, so no rebuild is needed in the selected implementation. Parts A3/A4
supply all separate comparisons, list tests, diffusion, trial control,
verification, signed output and reset scans. Their per-iteration charge
is O((k+b+a_addr)L), including pointer setup, actual known-bit reads and
the full indexed fee. Since k+b=O(R)=O(n) and a_addr=O(L), this is O(nL).

Thus both stored G1 passes, all extra scans and loop control cost
O(nL log2(L+2)) charged work per iteration. The tape uses
O(Ha)=O(nL log2(L+2))=O(n^2) classical bits. S3 counts all one-off
construction/verification/signed-label/reset costs, not just replay.
With Wcap=O(n2^R), S5 gives total attempt work

    O(n^2 L log2(L+2)2^R).

Main Section 9.5 explicitly checks every remaining source, recursion,
seed, decoder and setup term against this smaller envelope. It then
supplies the pre-envelope work used by the complete rational bound appendix. The complete statistical,
source and cap arguments are inside main, the cap and dense appendices.


## Part C. Complete RUN(F) source-label extraction

This is the full procedure and proof selected by main Section 3.1.
Its Section 3, Section 8 and Section 9 references refer to the main file.
The collective ROUND, table, J_e, h_ext and F(h_ext) are defined in main
Section 3. This text is reproduced from the exact retry source, with no
change to its algorithm or inequalities.

### C1. RUN(F): level-wise extraction

For each j = 0..J_e take F tests at level j per basis, as F X-rounds and F
Y-rounds, giving empirical means x_j and y_j. Then decode as follows.

Decoding each level. Pick the least dr in [0,64) maximizing
x_j Cos[64 dr] + y_j Sin[64 dr].
- If |x_j - cos| and |y_j - sin| are at most 1/1024, each computed dot product
  differs from cos(2 pi (2^j k/N - dr/64)) by at most 2/1024 + 2^-19 < 1/256.
- The nearest direction has true dot >= cos(pi/64) >= 511/512.
- Any direction at circular distance >= 1/16 has dot <= cos(pi/8) <= 31/32.
- The gap 15/512 exceeds 2/256. So alpha_j = dr/64 is within circular distance
  1/16 of 2^j k/N.

Unwrapping. Set g_(J_e) = alpha_(J_e). For j = J_e - 1 down to 0, let g_j be
whichever of g_(j+1)/2 and (g_(j+1)+1)/2 (mod 1) is circularly closer to alpha_j
(ties: the first).
- Suppose g_(j+1) is within e < 1/16 of 2^(j+1) k/N. The correct preimage is
  within e/2 of 2^j k/N, hence within 1/16 + e/2 < 3/32 of alpha_j.
- The other preimage is at least 1/2 - e/2 from 2^j k/N, hence more than 13/32
  from alpha_j.
- So the choice is correct and the error halves. Finally g_0 is within
  2^-(J_e)/16 = 2^-(n+8) < 1/(2N) of k/N.

RUN(F) outputs floor(N g_0 + 1/2) mod N, which then equals k. It always returns a value in [0,N) after its fixed tests.

Concentration. For F independent +-1 variables, the centered log-moment
generating function has second derivative at most 1 (a tilted variance) and
vanishes with its first derivative at 0. Hence
Pr(|mean - E mean| > delta) <= 2 exp(-F delta^2/2). With delta = 1/1024 and
F = F(h_ext) this is 2 exp(-h_ext). So RUN(F(h_ext)) returns a value other than k with
probability at most 4 (J_e + 1) e^(-h_ext) = 4 (n+5) e^(-h_ext), uniformly in k.
A call uses 2F(h_ext) rounds of O(n) quantum core steps. Counter updates cost O(n F(h_ext) log(F(h_ext)+2)) bit operations even without
amortization. There are O(n) counters, each of O(log(F(h_ext)+2)) bits. Each of
the 64 direction scores per level is computed by integer arithmetic on
O(log(F(h_ext)+2)) bits; the fixed table denominator is common to all scores.
Exact dyadic unwrapping and final multiplication and rounding cost O(n^2).
Therefore the total core work per call is

    O(n h_ext log(h_ext+2)+n^2)=O(n^2),

because Section 9 proves h_ext=O(sqrt(nL)). The term
n h_ext log(h_ext+2) is O(n^(3/2)L^(3/2))=O(n^2), since L^3=O(n).
Quantum scratch
is O(n), classical scratch is O(n log n). All work is bounded on every
branch. To make the collective map total on the data encoding, first
compute [u<N] and apply the modular subtraction only on that subspace;
the data validity is preserved, so its flag can be cleared. This changes
neither the O(n) cost per round nor the action on the source.

For each call, conditional on its latent label and all earlier history,
its error probability is at most 4(n+5)e^(-h_ext). Thus over at most Qcap_dense<=Qcap_old calls,

    Pr[any wrong label] <= 4(n+5)Qcap_old e^(-h_ext) <= 2^-14.

The IDEAL run replaces every returned label by its independent latent
label. All test results are private and affect no other control decision.
Actual and ideal runs can be coupled until the first wrong label. This
comparison does not condition the root law on successful extraction.

## Part D. Complete earlier source credits

- The exact own PSG2-SBG proof in submission
  321bac1d-9e52-408f-b257-30d36939e972, commit
  da0dae531d1bf317d093478c7c37ebe592a4bd97, SHA-256
  ab233182c257989f5b6592c20f33b7f2ccf8e1996ae6301c893981a5f5857923:
  the complete strided supplier, decoder, implementation and coarse budgets.
  [Exact public proof](https://github.com/Layr-Labs/dcp/blob/da0dae531d1bf317d093478c7c37ebe592a4bd97/submission/proof.md).
- PSG13, 4c42d100-f644-429d-b50d-7b3e5d226af8, commit
  abf41b73e429dfa332ed263db78bf29363a499fc, exact `submission/proof.md`
  SHA-256 fca9c2959397ba2dba8bf71f5a9284335335ff9a41db750623785fd54ca5afd6:
  its verified-pair success margin motivated the sharper retry accounting.
  The local audit `psg13_saved_source_audit.md`, SHA-256
  f6d6eac685a43af520846c25031c4db6a13051a16e0d0fa4f12f7a91ce12d89c,
  derives the nominal-product bound used in the required appendix.

- PSG2, b267909b-a859-49d3-9c64-18eca846b18c, evaluated commit
  5292134d56d56a849d16d42063379905bfd297d6: the bounded Grover
  discovery procedure, exact projection onto verified pairs, fresh-label
  induction, truncated profile, and two-cutoff framework. Its exact proof
  has SHA-256
  6dab91a37961032b862229cb80850eadb54979541c7ef34c4141802f4ea69ee9.
- CS1-BACKWARD, 70936e29-d357-4713-b84f-47acebe365fd: terminal phase
  localization followed by two-candidate backward recovery.
- Exact collective tests, 844c0fd2-9b1c-4e84-a37c-f402e109985f:
  one reversible modular subtraction performs all level tests in a round.
- The prior local PSG2-BG configuration, grover_backward.md, SHA-256
  feddaf5b5ba6610b0d6491e104b509cf70d668f4ceed4d23ec76c36a4d042431:
  the exact supplier, collective extractor, one-bit fallback, all-N
  composition, signed fields, profile, and the two geometric caps.
- CW1S, 32303149-73e3-4acd-af1f-4a6052d73869, evaluated commit
  174d649db7c03b0619a486e9ce515c7b95e8ff2d, exact proof SHA-256
  f680e71657013d62c319a71e48ed20c2f0670072b9f494e156101fca0501df84,
  Sections 9A.1--9A.4: the low-bit distance event, top-bit factorization,
  and stride score argument. CW1S credits the distance and stride idea to
  HS2, 8b85be12-4b9c-40e6-a62f-d2d232d62402; that credit is retained.
- The local note stride_decoder_transfer.md, SHA-256
  abe770f323abf2b161678df4ee06d6dd39e09f7bfe71ce643863b52b3ef0eb3f,
  Sections 1--7: the exact finite pool, joint strided terminal seed and
  backward decoder, and the root-count and cap changes proved here.
- The local complete PSW2-B proof, polyspace_backward.md, supplies the
  collective extractor, backward decoder, all-N composition, and capped
  recursive-control accounting used here. The local unsubmitted note
  polyspace_next.md supplies the extra-decrement geometric-cost argument.
  All required arguments are reproduced below.

The exact unpublished PSW2-B snapshot has SHA-256
3f0c3b538040326bef5e488c9034b57ec35972baa6a3f3da00684e4e27ad572f.
The exact completed polyspace_next.md resource note has SHA-256
6d150b201f434be267e6c21daf7cc9978690770da666388b0f5b4820fd7f9799.
These are actual own-source uses with no eligible published submission IDs;
every needed argument is reproduced here.

PSG2 credits PSR2
16bb6065-c3ca-45fb-b514-86106a310646, SLS
59facd77-4082-40d9-910e-9060c197e72a, and CS1
f1481815-9577-4990-abe3-7b79fa5d9284 for its streaming framework,
subset pairing, source transforms, and label arguments. Historical sources are Regev quant-ph/0406151,
Kuperberg 1112.3333, Kitaev quant-ph/9511026, Grover quant-ph/9605043,
and Boyer--Brassard--Hoyer--Tapp quant-ph/9605034v1. No prior verdict
is a premise and no oracle is left uncounted.
