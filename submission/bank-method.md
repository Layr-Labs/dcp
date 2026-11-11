## 2. Fixed dense pools and one generic polynomial interpreter

Assign fixed padded classical bit ranges to every V field: input/parameters;
source/count/arithmetic work; all Q labels and shadow signs/axes; both original
N-prefix and dyadic M-prefix banks; shuffle/subsample arrays and filter masks;
frequencies/angle records, streamed trigonometry fields; all pivots/sketches/
thresholds/caches; cap tables, counters, frames, allocator/generator scratch;
and expanded integer-candidate/champion/endpoint fields. Use their stated
EXACT public dimensions and hard stack/counter caps, reuse common scratch
at the stated release points, and assign offsets by prefix sums. Do not
retain expanded circuits, a lifetime-index directory or a G^2 table.
This is a fixed static layout computable from n and the public branch.
Where a logical dimension such as J depends on filtered records, reserve the
public maximum Jmax (the next power of two above8m) and all of its padding;
loops use the actual bounded J. No allocation depends on favourable data.

Let B(n) be the next power of two above that actual total bit capacity,
including every metadata/padding cell. Let H(n) be the next power of two
above the complete coherent pool, including query/gradient/equality and
original source/endpoint roles. From (1.1), B=O(n^2),H=O(n). The finite branch
uses its own original finite-branch layout; it does not allocate irrelevant
large-branch objects. Rounding changes capacity by at most two, not by an
unproved asymptotic threshold. All source-specified constants count.

Place virtual classical bit i on physical wire2i, 0<=i<B, and genuine
coherent slot j on2j+1, 0<=j<H. Reserve the ENTIRE paired prefix through
2max(B,H)+3, including all inactive and unused paired cells. Additionally
reserve one current raw source's n+1 temporary wires. This full physical
allocation is O(n^2), and every operand pays its full O(log(n+2)) address
fee. There is no sparse huge index or classical bank counted as free.

READ(i) measures the known even wire in the computational basis into a
reused physical classical bit. WRITE(i,b) reads it and applies X iff its
old value differs from b, then forgets temporary bits. A Boolean bit step
reads a fixed number of operands, performs the same Boolean action and
writes its result. Long virtual words remain in the bank and are processed
bit by bit. Original quantum gates act on mapped odd slots, preserving
their original quantum controls. A superposed index never addresses this
bank. Reset/discard is measurement, conditional X and forgetting, exactly
trace-out followed by zero even with an arbitrary reference.

For an original call acquire EXACTLY ONE arbitrary raw register on the
n+1 temporary wires, SWAP it to its designated zeroed mapped odd slots with
three CNOTs per qubit, and release the now-zero temporary wires. This is
register relabeling, not an ideal reconstruction of a bad input. No zeros,
source moves, gradient work, resets or bank reads create original samples.
Ownership and slot handles are counted basis-bank fields. Source-held unread
registers remain passive at their original positions until the SAME calls.

Here is a complete conservative GENERIC interpreter sufficient outside the
main search attempts. Expand V's finite controller/arithmetic into finite
Boolean bit operations, gates, measurements, coins, guards and source calls.
Keep its mutable program/loop/return records in the fixed bank. A finite
physical kernel stages only a fixed number of address fields and at most
O(w^2) bit scratch, w=ceil(log2(4B+4H+4n+32))=O(log(n+2)), plus input/output
O(n). For each operation it can fetch its operand fields serially and EVEN
SCAN THE FULL fixed bank to locate any addressed bit; all equality tests,
address construction, generation, measurement and writes are paid bit work.
With polynomial B,H and w-bit indices this gives a fixed polynomial P(n)
physical work per expanded virtual primitive. It has a fixed finite loop
and no physical classical call stack; all long control is virtual data.
No word-RAM, instruction oracle or coherent lookup is used. Thus its entire
classical allocation is O(n)+O(w^2)=O(n). It also clears released fields,
so its records never grow with runtime. Exact primitive channels, not speed,
are the reason this generic interpreter is used in those phases.

After the logical result is available, copy the entire output to counted
classical output FIRST. Then clear/reset/release the ENTIRE prefix, genuine
pool, padding and staging. Full scans and initialization are paid. This
construction applies on bad inputs and aborted histories, without an
assumption that a flag/label/state is honest.

## 3. Which phases may use that generic cost

For n>=n0, acquisition/extraction, private source/shadow/subsample/anchor
sampling, filter and coefficient/angle preparation, public constant/cap
calculation, at-most-Hmax accepted-pivot cache/sketch bookkeeping, final
integer expansion/full-record tournament and endpoint have polynomial TOTAL
virtual work, as profile-source.md proves. This includes the streamed G^2
angle search: G=O(n^2) up to a fixed constant, and it stores only short
counters/scratch and the chosen angles. Generic multiplication by P(n)
and full scans leaves these phases polynomial, absorbed by (0.1).

That assertion does NOT cover the exponentially many FAILED search attempts.
They use the tight native controller in Sections4-6. In particular clocks,
B/A_j/Budget updates, verification and reset on every failed history are
native, not delegated to this slow interpreter. At most Hmax=O(n) accepted
pivots can trigger the slower polynomial bookkeeping. Query work is already
measured/reset at those acceptance boundaries; the ordinary catalyst stays
in its dedicated live coherent slots until V releases it.

For n<n0 execute the SAME complete selected V finite branch through the
generic interpreter. A polynomial slowdown of a tight exponential envelope
cannot be ignored for unbounded n. Here the range is a FIXED finite prefix:
P(n)<=max_(1<=h<n0)P(h), an absolute finite program constant. Thus its cost
is at most that constant times V's (1.1) representative, plus polynomial
allocation/cleanup. The noisy-input output law and actual guards remain V's;
there is no substituted clean-only finite solver. This finite-prefix
argument is separate from the polynomial-total large-branch argument.

At mode entry/exit stream the currently active logical word fields between
basis cells and physical classical fields, zeroing obsolete duplicate cells.
All other records remain banked. This is measured COPY/known WRITE on truly
classical data, with paid O(n) or polynomial transfers. There is no live
recursive query at a generic bookkeeping boundary. No transcript of all
failed candidates, old values or nested physical classical frames is kept.

## 4. Linear native active state and exact return grammar

During the repeated coarse attempts keep only a FIXED NUMBER of n+O(1)-bit
classical words: Budget, B,A_j,Bcap,t and reused arithmetic, current measured
candidate, known pivot/label/frequency when needed, input/output. Current
stage/count/record/bit indices, coefficient words of g bits and a fixed
number of regular address/microstep descriptors use O(L^2) bits or less.
Every large table, label history, frequency/angle array and pivot cache
remains in the basis bank. Precomputed A_j/cap words are loaded serially
into the reused active word fields, not copied as an n-entry classical array.

Native code names active physical word fields directly; it does not run a
generic virtual-address dispatch on each bit. Basis READ is used only for
its explicitly banked arrays. R0 acts ONLY on mapped genuine query/helper
wires initially zero, excluding retained rows, the basis bank and catalyst.

The source preparation grammar is exactly

 V_j=Vprev R0 Vprev^dagger O_(P_j) Vprev,
 P_j=S_(128j), with V0 the entire flagged Fourier word.   (4.1)

Chronological forward pieces are Vprev,O_(P_j),Vprev^dagger,R0,Vprev;
adjoint pieces are Vprev^dagger,R0,Vprev,O_(P_j)^dagger,Vprev^dagger.
A frame needs only its direction and next one of FIVE pieces. Reserve8 padded
bits per level, including inactive frames. The current j, root level and
depth are single active fields; a child decrements j, a return increments it,
so ancestor levels are implicit. The immutable128j prefix is reconstructed
at each leaf from current j, never from a later history.

The new V0 is a LEAF. Its frequency/index/angle/QFT/ripple loops complete
before return and never invoke a recursive V child. The same is true for
phase-oracle and R0 leaves. Their local loop positions need not survive
on ancestor frames. Therefore 8(K+1)=O(n) physical return bits suffice.
Induction over the two fixed piece orders gives EXACTLY V_j and its actual
adjoint, including the whole new base, rather than a cached state or inverse
of an original source. Updating current level/depth/stack fields may cost
O(L^2) charged work per node; the O(3^j) nodes fit the stated preparation
bound below. No O(n log n) physical classical frame array is allocated.

The native active fields occupy O(n)+O(L^2)+8(K+1)=O(n) bits. Generic staging
may even be reserved simultaneously; it still adds only O(n). Every inactive
field, ordinary address descriptor and output is counted. All genuine query,
catalyst, equality and arithmetic states stay on their mapped odd wires;
basis-bank cells contain only V's classical records, never quantum amplitudes.

## 5. Exact NEW base bank reads and complete inner-loop costs

Fix a classical record/history. A basis READ produces its existing bit,
independent of every coherent query candidate, preparation flag or index.
The NATIVE controller emits the complete original controlled gate word,
including gates whose quantum controls are inactive. It never conditionally
fetches a classical row by MEASURING a query control. Thus the base and
phase-oracle remain the same unitary/actual adjoint on the genuine pool
conditional on records. Full mixed/reference correctness follows in Section7.

For sampled constraints, leaf list indices are classical known loop values.
Read their shadow word/cache entries by measured READ and write an accepted
logical record by WRITE. The row base is formed once per record. Sliding
p-bit constants are read consecutively, and regular ripple role pointers
are persistent physical classical fields. Over a length-p sweep, binary
increments/decrements/carry walks and descriptor initialization require
O(p+L) actual bit actions, as in the complete native source. Fixed strides
are fixed numbers of updates; a public sentinel avoids a full word test
per gate. All forward/inverse templates, constant reads, control/AND scratch
and emitted gates pay their full O(L) address fees. Each additional basis
READ is only a constant number of such actual primitives.

For constraint i there are ell_i=2^17(32+2ceil(log2(i+1))) records,
q=O(n) additions per record, and p=O(L). Each stored index/exact pivot word
is fetched at its CLASSICAL loop index. The actual record count is ell_i,
not ell_max. Native accumulator width may be padded to O(log ell_max),
which fits the same per-record bound. Computing the public ell_i from the
current i field and O(L^3) record/base setup fit O(nL^2) per record. Thus
one complete constraint costs O((1+log2(i+1))nL^2), including canonical
comparisons, exact finite interpolation/common denominators, flags/AND,
carry/uncompute and all measured-bank reads. No virtual bit is free and
no serialized full descriptor is fetched anew per elementary gate.

The NEW WFP3 Fourier base also uses only CLASSICAL outer record indices:

1. For each classical loop j, READ the q-bit frequency f_j from its known
   basis-bank row into one reused active word, or stream its bits. Emit the
   original known-pattern XOR on the genuine frequency wires, controlled on
   the QUANTUM branch/index equality. The latter is computed coherently by
   Toffoli/AND words; it does not select a classical bank address. Every row
   is read and its whole controlled word emitted. Forward and inverse-index
   lookup cost O(J nL), with reused O(n) genuine equality scratch.
2. Coefficient angle/scalar words are read at the CLASSICAL loop j and their
   g known bits control the exact catalyst addition templates. Index/flag
   controls remain coherent; AND work uncomputes. READs reveal no which-index
   information. These words, actual inverse words and scalar corrections
   have the same amplitudes as V0. Their native cost is O(J(g+log J)L), plus
   at worst O(JL^3) for record-address setup and finite counters.
3. The NEW block QFT loops have public classical wire/width indices. For
   target r after H, w=min(b_F,r+1). The lower genuine query wires represent
   y=sum_(d=1,...,w-1) f_(r-d)2^(w-d-1), with one fixed clean zero top bit.
   Emit V's controlled variable-register SUBTRACTION of y modulo2^w into
   the TOP w genuine gradient qubits, controlled by genuine query r. The
   addend/query bits are NEVER READ as classical data. The block executes
   its complete Boolean ripple/constant-control Clifford+T word regardless
   of their quantum values, uncomputes carries/scratch and reverses exactly
   on adjoints. Source-window, gradient-top, zero and carry-role pointers
   have regular fixed strides, O(w+L) actual core descriptor/gate-generation
   work per block and full O(L) address fees on every action. The q blocks,
   final wire reversal and all initialization/inverse work cost O(nL^2).
   The catalyst is dedicated genuine work, excluded from R0 and never reset
   at a recursive/accepted-pivot boundary. This emits EXACTLY V's NEW word
   even on a failed gradient component. Equality with the OLD reference
   kernel only on the ideal-gradient event is used in V's mathematical
   success theorem, not in this physical channel-transfer proof.

Frequency-row pointers and quantum wire-role pointers use fixed known strides;
reading a q-bit row is O(q+L) core actions after initialization, not copying
an L-bit address for each bit. Polynomially many rows are not a quantum RAM:
index j in these loops is a CLASSICAL controller value, while the quantum
index only controls gates on the genuine frequency register. Conditional
on the frozen records, all extra READ outcomes are deterministic regardless
of the query superposition. There is no candidate-dependent measurement
record, even on failure-flag branches or during inverse lookup.

Here J<=8m=O(L). Sparse mapping JnL=O(nL^2), and coefficient/metadata
work JL^3=O(L^4)<=O(nL^2) for n>=n0. The same holds for J(g+log J)L.
A complete native base/inverse therefore costs U*=O(nL^2), including all
bank access and actual generator work. The slower generic interpreter is
NOT multiplied into these exponential loops.

At level j a frozen prefix has128j constraints; its full native cost is
O(j(1+log2(j+1))U*). The same bound with j+1 covers a current root prefix.
The grammar therefore gives, for both actual directions,

 C(V_0)<=C U*,
 C(V_j)<=3C(Vprev)+Cj(1+log2(j+1))U*,
 C(V_j),C(V_j^dagger)<=C'3^j U*.                          (5.1)

Divide by3^j and sum: sum_(j>=1)j(1+log2(j+1))/3^j is finite, bounded
by sum j(1+j)/3^j=9/4. Also (j+1)(1+log2(j+2))<=C3^j uniformly, so a root
predicate/verification fits C3^j U*. This charges late longer sketches in
their actual places instead of charging ell_max at every early recursion.

Only one genuine query/helper pool is used recursively. On arbitrary
non-gradient/failed-base components the same finite words, physical bank
reads and descriptor walks still have these costs. No statistical event
is used for the instruction-count or allocation bounds.

## 6. Native attempt bookkeeping and the actual joint resource theorem

A_j and Bcap are active n+O(1)-bit words loaded from their bank table. A full
load costs O(nL), even if done per attempt. Budget,B,t remain active words.
A debit B A_j is the original known shift followed by ordinary n-bit
comparison/subtraction, with O(n) core bit actions and O(nL) charged work.
Clocks, dyadic changes, sixteen-attempt counters and private clock bits have
the same bound; none is a free word operation. Same-predicate verification
on the measured candidate costs O((j+1)(1+log2(j+2))U*)<=O(A_j U*). Root calls, validity,
query measurement/reset and diffusion also fit the per-attempt charge.

Before each attempt check/debit the EXACT V amount B A_j; stop if it does
not fit. With the current recomputed public D=ceil(2^80*2^(n+32)/m),
m=2^100 L, the actual word cost is at most C B A_j U*. Therefore

 T_attempts<=C U* sum_(admitted attempts)B A_j
            <=C U* 2^28 ceil(sqrt(D))
            =O(2^(n/2)nL^(3/2)).                              (6.1)

This is deterministic on ALL inputs/outcomes, not an expected hitting-cost
resource claim. V's original success proof uses expectations only to bound
failure before a near visit, not to bound actual work after it. Later failed
attempts still consume tokens and retain the visited list. Accepted-pivot
bookkeeping has polynomial TOTAL work because Hmax=O(n), and every generic
large-branch phase from Section3 remains polynomial even with full scans.
All mode transfers, static layout arithmetic, source SWAPs, guard work,
initialization and complete output-first clearing are separately paid and
absorbed. The fixed finite branch is bounded as explained in Section3.

Physical classical space is O(n) for the counted native active fields and
compressed frames or generic staging, with all unused words and output.
Physical quantum space is the ENTIRE paired prefix O(B+H)=O(n^2), not just
the O(n) genuinely coherent portion, plus temporary raw source wires and
all current work. Every basis bit, inactive cell and unused pairing counts.
Both source prefix banks, all frequencies/angles/labels, long virtual scratch,
metadata and history live in those counted basis cells. The full combined
address length stays O(L), as used above. Thus the ACTUAL joint pair is
SCn,SQn^2, rather than the virtual SCn^2,SQn.

There is EXACTLY one original raw acquisition per V request. Each state is
moved with its full arbitrary correlations; zeroing a bank cell, additional
basis READs, known work-gradient preparation and mode transfers never call
an original source. All Q=3*2^40(n+32) requests precede new aborts, exactly
as V specifies. Original source work and every original reset/discard remain
charged. No uncontrolled/controlled source construction, purification access,
quantum-addressed classical lookup, uncounted instruction oracle or arbitrary
rotation primitive appears.

## 7. Full-reference CQ invariant and exact output-law transfer

At each aligned logical step include arbitrary inaccessible R and the fixed
not-yet-delivered original systems U. The physical state is a classical
mixture of actual native/kernel classical fields z and measured basis records
c, tensored with a conditional state rho_(c,z) on mapped genuine V registers,
U,R. Conditional rho may depend on ALL records and need not factor among
good, bad, unread or reference systems. Decode currently active native words
and constant-size return frames to their logical V values; relabel odd slots
and forget duplicate kernel copies. The resulting FULL joint state is
EXACTLY V's logical state. The extra encoded return levels are reconstructed
mathematically from current level/depth, never allocated physically.

Initialization has zero bank and helpers and the same arbitrary original
joint state. READ's basis projectors reveal a value already classical and
leave each conditional rho unchanged. WRITE updates that value; merging
records after irreversible forgetting mixes the conditional states exactly
as logical classical forgetting does. Native mode moves copy/zero genuinely
classical fields with the same identity. Compressed frames emit exactly the
same genuine gate word by Section4; all native new-base reads are independent
of query data conditional on existing records by Section5. Thus they neither
dephase a candidate nor change relative amplitudes/catalyst phases, and the
actual generated inverse is still the correct inverse on the genuine pool.

All original gates, measurements, coins, guards and source calls have the
same instruments/probabilities under that decoded logical state. Source
SWAPs just relabel the actual raw joint register. Reset/discard is the exact
reference-safe trace-and-zero channel. Extra old/staged record copies are
forgotten at their paid release points, so no unbounded transcript or hidden
which-candidate memory survives. This induction is valid on every actual
history, including wrong labels, failed work gradients and arbitrary malformed
records. It does not postselect on a correct Fourier start or coarse answer.

The fixed passive source assumption is essential: unread U cannot be
replaced or operated on in response to the additional readout copies.
Measurement-induced conditional U changes are already part of rho_(c,z).
There is no inference of conditional fresh-good states. This argument would
not justify treating a coherently superposed bank as classical, nor a new
interactive supplier promise. Only V's exact fixed original joint model is
selected. All original retained row and ordinary catalyst correlations are
preserved in the logical channel, including its off-success components.
In particular V is the NEW WFP3 physical word: the induction emits its NEW
controlled register-subtraction QFT on ANY gradient input, rather than
assuming that its old reference-kernel identity holds on a bad component.
The single ideal-gradient discrepancy is already charged in V's complete
success proof and is not recharged or postselected here.

The final classical output law is consequently EXACTLY V's law for every
allowed fixed-B input/reference and mixture. Its complete mathematical
>2/3 theorem transfers with ZERO additional statistical loss, jointly with
our physical allocation/work bounds. Source count/fraction, label-only filter,
anchor guard, actual flagged Fourier state, weighted first-near analysis,
full integer expansion/champion and unconditional retained endpoint need no
new probabilistic assumption. The n<n0 noisy-input branch transfers too.

All five objects are therefore established for this SAME physical program:
actual T2^(n/2)n(log2n)^(3/2), SCn, ENTIRE SQn^2, literal Q linear and fraction1/3
in the stated fixed joint context. Local review, source identity or finite
diagnostics are not mathematical premises for any of these statements.
