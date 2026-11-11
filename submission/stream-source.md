# SPTS-JM-BANK-STREAM: a native coarse controller with measured record storage

For all N>=2, s modulo N and n=ceil(log2N), ONE uniform physical algorithm
outputs the complete s with unconditional success STRICTLY greater than11/16.
On EVERY branch, including all aborted and discarded work, jointly

 T=O(2^((1/2)n)n(log2n)^3), SC=O(n), SQ=O(n^2),
 Q=3*2^40(n+32) EXACTLY, epsilon(n)=1/3.                    (0.1)

The four indices are1,0,0,0. The logarithm concerns n>=2; the identical finite
n=1 program has bounded absolute costs. The coefficient1/2 multiplies n.
The storage and controller are the physical implementation selected here.
No old virtual space bound or generic-interpreter time bound is substituted.

## 0. Exact source, scope and implementation change

The complete immediate material source is SPTS-JM-BANK,
057bc5a2-6358-428a-9cf6-85b9c45a478b. Its exact main is included unchanged as
bank-interpreter-source.md, SHA-256
26b64d6eb0471b0e73a66164c39c03d9a5954d9cad120a52729fdd50a2467298.
Its complete four mathematical source members are copied unchanged, preserving
paths: joint-source.md, spts-source.md, sources/RQ-SPLIT-proof.md and
bank-source.md. The five source members together contain the entire virtual
algorithm V, fixed-state one-third theorem, exact arithmetic, finite branches,
caps, allocation families, measured bank and full-reference CQ method.
No prior acceptance is a proof premise. Source diagnostic/review pointers
are historical, not required executable evidence in this archive.

This implementation uses the SAME measured basis-bank and complete V but
replaces the general per-instruction descriptor-fetch interpreter DURING THE
EXPONENTIAL COARSE LOOP by the explicit native controller below. Large record
arrays stay in the counted basis bank. Active word operands, regular gate
descriptors and the newly compressed recursion-return stack stay classical,
with a proved O(n) total allocation. The generic interpreter remains available
for the polynomial pre/post phases; its overhead is paid there. The generic
source's log-six physical envelope is not simply renamed log-three.

The complete source carries the SPTS-JM/PCT/RQ/SPTS/FNS credits and the prior
LLV-GBANK300C/PSG21/PSG2-QSTORE measured-bank credits. No extra ancestor feature
outside that complete source is separately imported or hidden by a path.
The persistent-descriptor bit-generation method is explicitly already in
spts-source.md Section8 and RQ Section6.1. The new part is isolating a linear
active controller, changing its return-frame representation and proving the
banked coarse primitive costs. The mathematical selector is unchanged.

## 1. Fixed joint input and exact virtual algorithm

The fifth object has EXACTLY the same model as the complete source:

"Among the Q acquired copies, an adversary fixes a set B of at most floor(epsilon(n) Q) malformed positions, possibly depending on N and s. The joint state is arbitrary subject to its reduced state on all other positions being exactly rho_s^{tensor (Q-|B|)}. Malformed systems may be correlated or entangled with each other and with other systems subject to that marginal promise. No source control, purification access, or preparation inverse is supplied."

All Q original registers are fixed jointly BEFORE passive release in fixed
order. The supplier cannot replace or act on an unread register in response
to any outcome. Conditional unread-state changes due to earlier measurements
are allowed. Unread passive source state is excluded from accessible memory
by the explicit challenge rule. An inaccessible reference, arbitrary good/bad
entanglement and mixtures of fixed-B components are included. Conditional
freshness, independent bad states and source control/inverse are not assumed.

V is exactly the complete SPTS-JM algorithm in joint-source.md and its two
algorithmic sources: original collective EXTRACT and confidence/decoder; all
Q=3*2^40(n+32) sources; original capped private late split; fresh shadow axes;
sampled-pivot/frozen-prefix/token-limited search; full-record champion; the
same bounded n<64 fallback; and original untouched-bank gradient/trit endpoint.
All labels, roles, thresholds, caps, finite decisions and gates are unchanged.
The current implementation changes classical storage/controller representation,
not V's genuine quantum gates, random laws or logical record updates.

The included proofs establish full-secret success >11/16 in this model,
virtual charged T_V=O(2^(n/2)n L^3), full virtual classical allocation O(n^2)
and coherent allocation O(n), L=max(1,ceil(log2n)). The proof of the physical
controller below uses the actual source recurrence and ledgers; it does not
rely on an inherited review. Historical adaptive ModelM passages in old copied
sources remain historical; joint-source.md supplies the current statistics.

## 2. Fixed banks, two execution modes and linear active classical state

Use EXACTLY the source's static padded B(n)=O(n^2) classical bit pool and
H(n)=O(n) genuine coherent pool from bank-interpreter-source.md Section2.
Virtual bit i is on wire2i and coherent slot j on2j+1. Allocate the ENTIRE
paired prefix through2max(B,H)+3, including every unused/inactive cell, plus
n+1 temporary raw source wires. All combined-memory address fees use this
full O(n^2) allocation, so w=O(log(n+2)). This is an ordinary dense physical
allocation; known addresses are never coherently indexed.

The generic source interpreter, with O(n) physical classical staging and
O(w^3) charged work per virtual bit primitive, executes acquisition, collective
extraction, the private split, shadow preparation and any finite n<64 branch.
It also executes final champion, endpoint and complete output/cleanup. These
phases have polynomial total work for n>=64: the source ledger explicitly
bounds extraction/phase preparation by polynomial n^3 L^2 and full-bank pivot
cache/champion/endpoint by polynomial n^4 L^2. Adding the generic w^3 factor
and fixed allocation/cleanup is still polynomial. All n<64 branches have a
uniform finite maximum cost and the unchanged success theorem. No second
source bank is introduced by changing execution mode.

At n>=64 the repeated search attempts use a NATIVE known-address classical
controller. Store ALL large labels, packed shadow words, full pivot caches,
representatives, sketch lists, thresholds, shuffle data and the precomputed
A_j/cap table as measured basis-bank records. Only the following remain
physically classical during this coarse loop:

* a fixed number of n+O(1)-bit words: the measured candidate and current known
  pivot/label when needed, Budget, A_j, B, clock t and their reused arithmetic;
* current stage, accepted-count, list/record/bit indices, pointer bases,
  constant-number persistent regular gate descriptors and finite flags;
* the constant-bit-per-level return stack constructed in Section3;
* one current record's fixed r_phi=26-bit exact/fresh known values when the
  candidate is classical, and a fixed number of short accumulator/threshold
  and field-address staging words.

Thus their total is O(n)+O(w^2)+O(K), with K<=n. There is no Hmax-entry
classical pivot table, no k-entry classical label/cache array and no old
O(n log n)-bit recursion-frame store retained in physical classical memory.
All coefficient tables are either the fixed finite compiler or basis-bank
data. Source/endpoint arithmetic uses the generic interpreter, so an O(n^2)
virtual arithmetic pool is never silently kept classically.

Before/after entering this native coarse phase, stream the active word fields
between the bank and classical fields by measured READ/known WRITE, zeroing
obsolete duplicate cells; all nonactive fields remain banked. The entry/exit
transfer is polynomial. Native accepted-pivot bookkeeping may use the generic
interpreter because there are at most Hmax=O(n) accepted pivots in the ENTIRE
run: exact pivot cache computation, fresh sketch generation and storage have
polynomial total work, including mode transfers. THIS does not apply to the
exponentially many failed attempts. Their clocks, token debits, counters,
verification and reset are explicitly native and bounded below.

## 3. Constant-bit return frames for the exact preparation word

The source defines the known preparation

 V_0=H^n,
 V_j=V_(j-1) R0 V_(j-1)^dagger O_(P_j) V_(j-1),
 P_j=S_(128j), R0=2|0^n><0^n|-I.                           (3.1)

Each O_(P_j) is a clean EXACT phase oracle at the IMMUTABLE recorded prefix;
later histories never redefine it. The chronological word for (3.1), which
acts rightmost first, has five fixed pieces:

 forward: Vprev, O_(P_j), Vprev^dagger, R0, Vprev;
 adjoint: Vprev^dagger, R0, Vprev, O_(P_j)^dagger, Vprev^dagger. (3.2)

The phase oracles and R0 are self-adjoint, but the kernel can retain explicit
inverse flags. At j=0 emit H gates in forward/reverse order as appropriate.
For j>0 a frame needs only the direction bit and which of these five pieces
is next: a constant number of bits, say8 padded bits. There is no variable
loop running across a recursive child. The phase oracle and R0 are leaves
and do not call V recursively. Their local record/adder loops finish before
another child is entered, so those indices need not survive on ancestor frames.

Maintain root level j0, current level j, depth d and one finite program counter.
Push only direction/next-piece on a child call, decrement j and increment d.
On return increment j, decrement d and read the constant-size parent frame.
Every edge in this grammar changes the level by exactly one, so the parent
level is implicit; no n-entry array of log n-bit level numbers is needed.
The frozen cutoff128j is recomputed from the current j at a leaf. All stack
positions are ordinary classical addresses; the 8(K+1) reserved bits, including
inactive frames, are O(n). The fixed node word and adjoint order imply by
induction that the emitted genuine quantum gate word is EXACTLY V_j or its
actual adjoint, not a cached state, inverse of a source or recomputed modified
predicate. At most a constant times3^j grammar nodes occur.

An update of the current O(log n)-bit j/depth/address fields can conservatively
cost O(w) core bit operations and O(w^2) charged work per node, including
push/pop/finite branching. This avoids any claim of free word updates. Over
one preparation this adds O(3^j w^2), and fits O(3^j n L^3). The leaves' own
active indices are covered next. Nested O(n log n) physical classical frames
are neither allocated nor temporarily materialized.

## 4. Native measured-array access and the actual coarse leaf cost

READ(i) measures known even wire2i; WRITE(i,b) reads it and applies known X
iff needed. The bank is always computational-basis data, possibly correlated
with the genuine state. Each extra bank-bit READ/WRITE costs a constant number
of actual gates/measurements and emission steps, each with full O(w) address
charge. It does not fetch a complete virtual instruction descriptor from the
bank. The small current instruction and regular role addresses are already
physical classical fields. Their ACTUAL bit generation is included below.
Original controlled operations retain coherent controls on mapped odd wires.
No candidate-controlled classical address, QRAM or coherent lookup appears.

For one sampled constraint scan its ell=O(L) indexed records in stored order.
Read the next O(w)-bit index and its row base with ordinary paid bit arithmetic,
at most O(w^2) core work per record. If a full known n-bit label/pivot is needed,
stream its n bits once into a reused active word. More usually only the p-bit
sliding phase windows of the packed source word are read. Here
p=30+ceil(log2n)=O(L), r_phi=26. The row base is fixed throughout its n controlled
constant additions; its window start changes consecutively with candidate bit
position. There is no full offset multiplication per emitted gate.

For each p-bit ripple adder keep a fixed number of physical classical persistent
microstep descriptors and consecutive pointer fields. Initialization costs
O(w+p) core bit actions per adder. Across a p-stage sweep, binary pointer
increment/decrement and carry walks cost O(p+w) actual bit reads/writes: bit h
is visited O(p/2^h+1) times, summing to O(p+w). Fixed strides are a fixed number
of updates. Public sentinel underflow ends a sweep. Reading the p consecutive
CLASSICAL constant bits from the basis bank adds O(p) actual READ primitives,
not copies of an n-bit address per quantum gate. Emit the same fixed ripple
Clifford+T templates and actual reverse passes as the source. Each emitted gate
or pointer action still pays its O(w) address charge. This is the native
persistent-descriptor construction already stated in SPTS/RQ, now with basis
READ instead of classical data READ; it introduces a constant gate overhead
per bit access, not the generic field-fetch factor per generated instruction.

Per record the n additions therefore take O(n(p+w)) core bit/generation/bank
access actions, plus O(w^2+n) for index/base/full known-word setup. Fixed-width
interpolation scans the source's fixed2^14 grid with exact fixed-width arithmetic;
it adds a constant depending only on that fixed grid and O(L) accumulator work,
plus its O(w^2) descriptor setup per record. Accumulators have width
bit_length(ell)+50 and the same nonoverflow/common-denominator proof as V.
Current known exact pivot words are fetched at their classical record indices.
Canonical order/equality requires O(n) gates/bit actions with regular descriptors.

Since w,p=O(L), w^2=O(nL) uniformly after enlarging an absolute constant for a
finite prefix, the complete ONE-constraint charged cost is

 O(ell [n(p+w)+w^2+n+L] w+n w)=O(n L^3).                  (4.1)

Only its one constraint flag remains between constraints. Candidate-member
fresh words, all score arithmetic, membership flags/AND scratch and reverse
words are the SAME original exact coherent circuits, with O(n) genuine wires.
Bank queries depend only on the classical history and public leaf loop indices;
they never reveal a candidate bit or a quantum-dependent score. Conditional
on fixed history, every extra bank outcome is deterministic independently of
the candidate. Thus these extra reads cannot dephase the contender superposition,
change amplitudes or invalidate using the actual generated adjoint. The phase
oracle and its cleanup remain exact on the query/helper system.

A leaf S_r has at most C(j+1) constraints and P_j has Cj, so their cost is
O((j+1)U), U=nL^3. Grammar overhead from Section3 is absorbed into U. The SAME
recurrence holds for the actual physical preparations:

 C(V_j)<=3C(V_(j-1))+C4(j+1)U,
 C(V_j),C(V_j^dagger)<=C5 3^j U,                           (4.2)

because sum_(j>=1)(j+1)/3^j is finite. All genuine work and native controller
bit/gate generation, bank accesses and full addresses are counted here.
The proof does not apply the generic w^3 simulator inside this exponential loop.

## 5. Attempt controller, original hard guards and total resources

The original source already precomputes A_j=3^j and dyadic caps in polynomial
time; keep the O(n)-bit values in basis-bank tables. Load current A_j and cap
into the fixed number of active word fields with O(n) basis reads and ordinary
O(nw) paid work. It can be loaded once per stage, or even per attempt without
changing the bound. Budget, B and t are active n+O(1)-bit words. A debit B A_j
is the original known shift followed by comparison/subtraction. Implement it
by ordinary n-bit ripple/bit loops with O(n) core actions and O(nw) charged
work, using reused O(n) classical scratch. No n-bit word action is unit cost.
The same holds for dyadic-B changes, fixed sixteen-attempt counters and failed
history bookkeeping. No virtual long counter is interpreted bit by bit with
an extra w^3 fetch factor in these repeated operations.

Uniform t in[0,B) uses the original private bits for a dyadic B. Initialize
at most O(n) active bits, and decrement/test the clock with O(nw) paid work
per Grover iteration if necessary. Original fair branches, query measurement,
reset/release and same-predicate classical verification are native. Verification
uses the SAME leaf computation on the measured classical candidate, at cost
O((j+1)U); it fits O(A_j U) since j+1<=C3^j. Diffusion, valid-class checks and
full query resets cost O(nw), within U. Root calls of V_j and adjoints use the
constant-bit stack above. The actual cost of an attempt at clock B is therefore
at most C6 B A_j U, INCLUDING all failed attempts and controller work.

BEFORE the attempt, debit the original B A_j tokens from
Budget=2^28 ceil(sqrt(2^n)). If the debit does not fit, stop as V does; otherwise
perform the unchanged attempt. Summing over ALL admitted attempts gives

 T_attempts <= C6 U sum_(admitted attempts) B A_j
            <= C6 U Budget=O(2^(n/2)nL^3).                 (5.1)

This is a deterministic bound on every input and outcome, even empty sets or
failed-size paths. No expectation of physical work is substituted. The at-most
Hmax accepted-pivot events and the pre/post/source/full champion/endpoint phases
incur only their separately paid polynomial generic work. All initialization,
mode transfers and output-first bank/coherent reset/cleanup are polynomial.
They fit (5.1) after enlarging an absolute constant. Native total physical time
is the declared log-three bound. Its exact growth index is1, and the other
three polynomial indices are0. Finite branches keep the source's actual guards
and output law, with no unreviewed noisy fallback or asymptotic advice.

Classical physical memory is the generic O(n) staging in generic phases, or
Section2's fixed-number O(n)-bit active words/descriptors plus 8(K+1)=O(n)
return bits in native phases. If allocated simultaneously both are still O(n),
including all inactive fields and output. Every other record remains in the
counted basis bank. ENTIRE physical quantum allocation is the unchanged whole
paired prefix O(B+H)=O(n^2), plus one raw source register and O(n) genuine
query/helper/endpoint wires, with all padding retained and charged. These are
JOINT SCn,SQn^2 bounds for ONE physical implementation, on every branch.
Source count remains EXACTLY3*2^40(n+32): one original per V source call,
with source SWAPs as in the complete bank source and no new originals.

## 6. Full-reference correctness of the hybrid storage representation

Extend the complete bank source's CQ invariant by permitting a fixed linear
set of currently active virtual classical word fields to be encoded in actual
physical classical fields. The compressed stack decodes to the old generator's
logical return context: current level/direction/next-piece uniquely determine
all gate-word choices. Old redundant frame level numbers are reconstructed
mathematically, not stored physically. Section3 proves equality of every emitted
original gate word, including adjoints and frozen prefix choices. Generator
bookkeeping has no other effect on the mathematical algorithm.

At aligned logical operations the state, with inaccessible R and unread fixed
original bank U, is a mixture of actual classical/basis records and a conditional
state rho of the genuine mapped coherent registers,U,R. Tracing out kernel
copies and decoding those records yields EXACTLY V's full joint state. No
independence between records and rho is assumed. Mode-entry/exit copies and
zeros only actual classical fields. Native READ/WRITE copies/functions of
classical history and ordinary overwrites act exactly as classical records;
all genuine operations have V's instruments under that history. Extra leaf
reads have no quantum-candidate-dependent outcome, as explicitly proved in
Section4, so the preparation really remains a unitary and actual adjoint on
the genuine query pool conditional on that history. Source SWAP relabels the
actual arbitrary raw register, without replacing or idealizing bad states.

The induction includes conditional unread-state changes, original good/bad
entanglement and references. No interactive supplier can react to extra
outcomes: delivery is passive from the fixed original bank. Reset/discard is
the same full-reference trace-and-zero channel. All short copies and obsolete
fields are cleared with paid work; output is copied first. Thus the final
output distribution is EXACTLY V's for every allowed fixed-B component and
convex mixture. The complete source's >11/16 theorem at fraction1/3 transfers,
including the clean case and every finite branch, without conditioning on
successful label extraction, favourable errors or correct coarse answer.

All five declared objects therefore hold simultaneously: log-three time,
linear classical storage, quadratic ENTIRE quantum storage, exact linear Q
and exact one-third fraction in the SAME fixed joint-marginal context. No
source inverse, coherent classical address lookup, free word arithmetic or
unpaid compiler is introduced. This implementation tightens the physical
controller rather than dropping a factor from a generic simulator theorem.
