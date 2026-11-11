# GPS-BLOCK-BANK2: dyadic descriptors and persistent bit-field fetch

For every N>=2 and s modulo N, n=ceil(log2N), ONE uniform physical algorithm
recovers the ENTIRE secret with unconditional probability at least1-2^-8.
Jointly on EVERY branch, including every failed/discarded attempt and abort,
its bounds for n>=2 are

 T=O(n^(5/2)(log2n)^(5/2) 2^(a sqrt(n log2n))),
 SC=O(n), SQ=O(n^2), Q=O(2^(a sqrt(n log2n))),
 a=176777/250000, epsilon(n)=0.                            (0.1)

The four growth indices are1/2,0,0,1/2. The finite n=1 program has bounded
absolute costs. SQ counts ALL allocated basis-bank qubits, coherent work,
padding, unused slots and raw temporary source wires. This is a physical
implementation tradeoff, not identification of virtual classical bits with
free quantum storage. All constants are independent of N,s and outcomes.

## 0. Complete immediate sources and actual new controller

The complete immediate program/implementation source is GPS-BLOCK-BANK,
9e6989a1-27fe-4e63-9872-45f4690d1b2d. Its exact main is copied as
previous-bank-source.md, SHA-256
b8a58ced5432baa998432d96450301265d17e83f0998e358895b409b881837f6.
Its COMPLETE algorithmic helpers gps-source.md and bank-interpreter-source.md
are copied unchanged, with respective full SHA-256
3016a821fcc6ae313f0156326e1ca1f7de2f240c18d07bba70eb0db7859519f7 and
26b64d6eb0471b0e73a66164c39c03d9a5954d9cad120a52729fdd50a2467298.
Together these contain every current signed-sieve, private-law, cutoff,
all-N success and measured-bank obligation. No GPS-HALF or earlier source
feature outside that complete selected archive is separately imported.

The directly used persistent known-address/microstep method is
SPTS-JM-BANK-STREAM, b4039ae4-431b-4deb-8f66-e7d9df2ee633, commit
3e7a3d873fc24859d05fc7928996c372a1387c94. Its complete current main is copied
as stream-source.md, SHA-256
5ad693a64b57913c580fbec4798bf021fe9d505f3c2fa2421f4fcf080fd8affd.
We use its resident native address fields, persistent role-pointer sweeps,
amortized bit-carry generation and full address-charge convention. Its old
SPTS program, log-three time, compressed-preparation grammar and one-third
input theorem are not selected. Historical helper/archive paths inside the
exact copied method sources describe THEIR archives, not missing premises.
This main rederives the ENTIRE new typed controller, field fetch, layout,
CQ transfer and actual cost argument for GPS-BLOCK; no old theorem is applied
as if STREAM had already proved a generic quadratic-logarithmic interpreter.

The NEW implementation changes its classical record/descriptor layout to
dyadic strides, uses typed finite field locators and persistent physical
read/staging pointers, and changes fetch-loop termination to ripple borrow.
The earlier cubic-log kernel did not make these choices. We prove the NEW
reference-controller CORE ledger rather than assume an automatic compiler
from an old flat address space preserves that count. Its semantic updates,
true source schedule, four guards, coins and genuine quantum words remain
exactly GPS-BLOCK's. This is an actual controller change, not a better
representative for the unchanged prior machine. Inherited algorithms and
methods retain their credited authorship. No historical acceptance or
finite diagnostic is a mathematical premise or ancestry certificate.

## 1. Exact input, unchanged logical algorithm and source guarantees

The fifth structured object uses EXACTLY the canonical clean-source text:

"Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies."

Thus every acquired original is an independent rho_s. No positive
corruption tolerance or claim of optimal tolerance is made. There is no
interactive supplier, purification access, source control or inverse.
Source-held copies not yet requested are excluded from accessible workspace
by the challenge rule. Independent ideal copies may equivalently be supplied
from a fixed product bank in passive order. Extra implementation readouts
never select a replacement source or become new feedback to a supplier.

For n<256, V is EXACTLY the source's bounded exhaustive shift-testing program,
including its n+10 tests, first-passing tie rule and abort/output convention.
For n>=256 use ALL source rules literally. Compute the least integer R>=2
with S(R)>=n-1, with Delta=2ceil(log2(4R)), m=floor((2R-2)/Delta)+1,
v_i=2R-1-(m-i)Delta, q0=product(v_i+1), G=2^m q0. Do not change widths,
profile, count constants or any actual cap to match a displayed envelope.

The logical program has the source's verified translation-label EXTRACT,
private signing, depth-first PS_TREE(D,B), explicit fixed-schedule Grover
pair instrument and above-half conditional return. The odd part uses the
signed multiple-untouched-bit decoder when h>=8, otherwise its specified
unsigned small-mode decoder. The 2-adic part uses the same shifted sources
and fair-parity measurement. All CRT arithmetic, tables, exact Clifford+T
words, searches, measurements, finite loops and streaming candidate grids
are the source's. No new phase or preparation oracle is substituted.

In particular the four hard cutoffs are unchanged: original acquisition
Qcap=1024(2G H0+2n), weighted attempts Wcap=1024(2m2^R H0), high-confidence
fallback Cf=ceil(Qcap/ceil(sqrt n)), and root frequency |W|<=nq0. H0,Smax,K
are EXACT source formulas. The weighted guard occurs AFTER its children
have been built; those acquisitions/work remain counted. A refused source
call acquires no additional original. All source aborts release and output0.
No physical interpreter step restarts V or resets a logical counter.

The complete source proves the following simultaneous semantic facts, with its own
actual instructions and private-record exclusions:

* Exact source decomposition gives independent uniform latent Fourier labels;
  extraction coupling costs at most2^-14+2^-20 without conditioning on a
  numerical label being correct or on future cap survival.
* Routing inspects low residues, not the separately discarded unsigned label,
  sign or extraction-private transcript. The untouched signed high parts
  keep the proved conditional product laws in the unguarded ideal process.
  The deterministic occupancy inequality gives attempt success>1/2.
* Untouched high parts give the stated Dirichlet characteristic bound and
  signed root tail2exp(-n^2/8). The frequency guard is omitted in that ideal
  proof and coupled separately, never used to postselect that law.
* Root demand is O(n), all four actual caps bound EVERY execution branch,
  and full-secret failure is at most
  2^-10+2^-10+2^-14+2^-19+2^-20+2^-20<2^-8. The finite branch also qualifies.
* All retained labels, fields, counters, frames, exact arithmetic, instruction
  generation and decoder records use O(n^2) classical bits; all retained
  source-phase qubits plus shared scratch use O(n) genuine qubits.

These statistical facts are supplied proved mathematics in gps-source.md
Sections2-9, not assertions extracted from a score. Below we choose a new
dyadic reference implementation V* of exactly those semantic operations,
with its complete private erasure and genuine-word correspondence. We
re-establish its expanded CORE count, including generation, as

 A_*=O(n^(5/2)(log2n)^(1/2)2^R).                         (1.1)

The termwise proof appears in Section3.3. The source's pre-address ledger
and actual caps supply the starting charges, not an unproved assumption
that changing a bit layout is a constant-factor compiler for arbitrary
programs. We do not compute the OLD flat-to-new address map by division
on each access. Both source pointer arithmetic and the NEW kernel's full
physical addressing/generation are explicitly accounted for.

The source also proves Q<=Qcap=O(n^-8 2^R), in particular O(2^R), and
2^R=O(2^(a sqrt(n log2n))) with EXACT rational a in (0.1). Its explicit
large threshold n>=2^16777216 and all finite smaller input lengths are
part of that uniform theorem. None of its lower-order factors is silently
absorbed as a constant on an unbounded range.

## 2. Constructive fixed pools for this program

Use the exact finite widths from V and fixed chosen Boolean ripple/
schoolbook templates to assign its classical fields padded bit ranges.
These are arrays with public capacities, NOT an array indexed by Qcap.
The source stores only a bounded current tree and decoder stage even though
Qcap is exponential. Define the static families in the following order:

1. Input N, group decomposition, current secrets/interval endpoints and all
   public profile/cap words; the m widths/offsets and generator constants.
2. At most n+1 current/retained sibling label slots. Each label has width
   n+ceil(log2q0)+O(1), with the fixed sign/guard padding from source4.3.
   Labels are reused after a node consumes/discards its inputs.
3. The m capped depth-first frames, each with its source O(n)-bit parameter,
   return/loop/child-slot fields; one shared current search description.
4. The exact EXTRACT stage arrays, verifier windows and its reused arithmetic
   fields. There are O(n) levels/windows of O(n) or smaller bit widths.
5. The K decoder records (known frequencies, signs/bases and running residues),
   streamed current/best candidates, and n modular constants of O(n) bits.
6. Common finite-table/rational/schoolbook work, allocation/handle metadata,
   source-private/sign erasure fields, and all source bit-level generation,
   operand and loop scratch. No circuit tree or candidate list is expanded.

Compute the actual finite widths of those public-cap fields and chosen
Boolean templates. Store a word in a slot of the next power-of-two length
at least its width; store a constant-number-of-fields record in a next
power-of-two record stride. Every fixed array family has a public aligned
base. A frame/label/decoder family may use its largest O(n)-bit word width
for all its O(n) records; this is still O(n^2), including padding. The profile
may likewise use O(n)-bit slots for m<=2n records. Banked address/descriptor
fields may use the same global O(n)-bit dyadic word slot; only their bounded
w meaningful bits are fetched. Native short fields use aligned dyadic slots
of O(w) bits. Fixed finite table words
have their fixed next-power-of-two slots. This pads STORAGE, not arithmetic
widths, bit loops, records processed or genuine quantum wires.

There is no circular choice of a bank field width. Start public dyadic slot
size U above the source's maximal ACTUAL numeric/template width, and double
it until the actual padded capacity B(U), H and raw-role bound satisfy
ceil(log2(4B(U)+4H+4n+32))<=U. Address/handle words use these U-bit bank slots.
The actual family sum is bounded by C[(n+K+m+1)U+U^2+1], including fixed
finite table constants. Since K,m and source maximal widths are O(n), this
public test terminates with U=O(n), B(U)=O(n^2). It uses only polynomial
public work and a bounded number of O(n)-bit streaming words. The eventual
w is computed AFTER these capacities; all bounded-address high bits are
zero. Padding changes neither meaningful arithmetic widths nor bit loops.

A bit location is the typed tuple (fixed family/field tag, bounded array
index, bit offset). Its address is

 family_base+(index << log2(record_stride))+field_offset+bit_offset.

All multipliers are powers of two; the tag set/number of fields is fixed.
Addresses are formed by shifts/additions, not arbitrary w-bit products.
The family bases/strides/field offsets are computed once as public prefix
sums and held in a fixed number of w-bit native fields. An actual template's
finite field list determines them, not an unknown big-O coefficient.
Current-frame bases/return state and long data words stay in counted bank
fields; frame movement is addition/subtraction of the known dyadic stride.

The concrete reference controller V* uses these coordinates FROM THE OUTSET.
It is a finite implementation of GPS-BLOCK's array/word program, not a
translator of an existing flat pointer stream. A bit operation/gate opcode
names its operand FAMILY and the locations of the index/bit-counter fields
in place. It does not copy w bits to a new instruction header per gate.
The source's arrays, levels and word loops have fixed syntactic nesting;
locator dependencies have a fixed constant depth: current frame/level,
profile or current-word field, then its addressed bit. A pointer value is
never an unbounded chain of program records. Each extra indirection is an
explicit bounded field fetch, not a word-RAM access.

All indices are proved bounded by public family capacities on EVERY history:
level<=m, sibling counts<=r_i, records<=K, bit loops<=their public word
widths, source/attempt counters obey their hard guards. SEARCH verifies its
output before using a pivot. EXTRACT outputs labels in its fixed range.
Numeric labels/frequencies are data, never unguarded memory pointers. A
bounded index uses its low w bits; its remaining allocated high bits are
zero by these loop invariants. Long numeric words are still processed bit
by bit, never treated as w-bit address words or unit-cost integers.

Assign each actual padded range by its public prefix sum, reusing common
scratch at the source release points. K<=2^15 n, log2q0=O(n), P_j=O(n),
m<=2n and the fixed Boolean templates prove all capacities on abort paths.
The n<256 branch uses its own finite layout. No execution-lifetime directory,
unrolled instruction tape or exponentially indexed source array is added.

This sum is O(n^2), by the source9.3 list and the elementary dimensions above.
All handles/padding count. A map for O(n) genuine slots uses O(n log n) bank
bits and fits the same bound; no directory for every bit or every lifetime
is added. A field has an address in this one fixed pool, not a heap object
whose descriptions accumulate with time. Recursion contexts and long loop
counters remain pool data. Program code is a fixed finite controller; its
opcodes are not an exponentially unrolled instruction tape.

For genuine quantum work reserve the source's retained-sibling ranges by
level, of total at most sum_i b_i+1<=n+1, plus the ONE current source-phase
output. Reserve its shared maxima for search/Boolean arithmetic/extraction/
transforms and clean ancillas, using the actual chosen linear-size templates.
A parent holds only its retained phase siblings while a child runs; it does
not hold a separate full scratch pool. Released roles are reused, as source9.3
specifies. The resulting fixed pool is O(n), with all inactive helpers counted.

Genuine quantum roles are NOT padded to a word pool per frame. Retained
phase siblings use the source's compact per-level bit-slot bases plus child
index (stride1); common search/carry/extraction words use shared fixed role
bases plus bit index. A moved output has a direct bounded slot handle in
the counted classical bank. Fetching that handle is one field fetch. Thus
actual genuine gate operands require only shifts/additions and a constant
number of bounded field reads, without a general word-stride product or
an O(n)-qubit workspace retained at every recursive level.

Let B be the next power of two above the actual classical capacity sum and
H the next power of two above this complete genuine quantum pool. Thus
B=O(n^2),H=O(n). Their exact dimensions and offsets are computable without
instance advice or an unknown threshold. Before acquisition a bounded number
of O(n)-bit physical words can stream the public integer profile/cap/layout
calculation; it need not store an m-entry classical array. Schoolbook
arithmetic and sequential scans use O(n) temporary classical bits here.
This public setup is polynomial work, paid separately. The fixed finite
trigonometric recipe is computed, not supplied as preloaded data.

Map virtual classical bit i to physical wire2i, 0<=i<B, and genuine wire j
to2j+1, 0<=j<H. Reserve the ENTIRE prefix through2max(B,H)+3, including all
unused pairings and padding. One current raw source request additionally
uses n+1 temporary wires. The full physical allocation is O(n^2). There is
no sparse set of enormous wire indices or uncounted quantum classical data.

Put w=ceil(log2(4B+4H+4n+32))=O(log(n+2)). The finite kernel stores only the
input/output O(n) bits, a fixed number of w-bit address/operand fields,
its finite opcode, and O(w^2) bounded staging/layout scratch. All long source
words, return contexts, caches and mutable generation descriptors stay in
the basis bank. Since log^2(n+2)=O(n), physical classical space is O(n).

## 3. New typed interpreter, persistent fetch and complete CORE ledger

### 3.1 What one virtual bit action specifies

Expand V*'s specified word routines into actual Boolean bit actions,
indexed bit reads/writes, elementary Clifford+T gates, measurements, coins,
source calls and finite branches. No bulk word is one action. The finite
opcode selects a fixed number of operand field locators. Each locator has
a fixed family/field tag and a constant-depth list of current bounded
index/bit-counter fields. Those existing fields are read IN PLACE; no new
w-bit instruction/operand copy is constructed by the reference per gate.
It is the concrete finite controller for this source program, not an
instance-dependent instruction oracle or universal semantic word primitive.
Call arguments are FLATTENED typed location tuples, not references to a
parent's argument tuple. A tree frame stores direct sibling slot indices;
level/profile bases and current child count resolve them without traversing
ancestors. Ordinary word-library calls store a fixed number of resolved
(tag,index,bit-start) tuples ONCE at word entry. Their call-graph nesting is
fixed (schoolbook loops are loops, not a recursive chain of operand aliases).
Copying/initializing those O(w)-bit tuples is charged in the O(z+w) word
setup of Section3.3, never repeated per emitted elementary gate. The shared
current tuple fields and its finite fixed-depth saved contexts are bank
records; physical staging remains bounded. Consequently locator depth is
an absolute constant even when the source tree depth grows with n.

All arithmetic creating/advancing its loop/pointer values consists of the
same counted bit routines. The source genuine gate sequences are unchanged.

Maintain the current finite opcode and a fixed number of active native
frame/field/pointer words. All long loop/call contexts are bank records.
Public bases, strides and offsets occupy a fixed finite collection of w-bit
fields, counted even when inactive. Each field location is formed with a
fixed number of w-bit additions/shifts: O(w) core bit actions. Family-index
or frame multiplication is a shift by its public dyadic stride exponent,
NOT the former arbitrary word product. A constant-depth indirect locator
therefore requires only a constant number of the field fetches below.

### 3.2 Actual field-fetch microprogram

READ(i) measures the known even wire2i into one reused staged classical bit.
WRITE(i,b) reads and conditionally X-corrects that basis value, then forgets
unneeded staging. Quantum coherent controls always remain genuine odd-wire
controls. Extra READs never select a quantum-addressed row.

To fetch a w-bit address/index field, form its FIRST physical read address
ONCE in a resident pointer P; form its first staged destination address S
ONCE. Then emit READ at P, put that existing bit at S, advance P by2 and
S by1 with actual ripple carry, and repeat. Native emission names those
resident known fields; it does not serialize another w-bit descriptor into
bank data before every bit. Each emitted access STILL pays the FULL O(w)
address fee. This is the selected persistent-address convention, not free
word arithmetic or uncharged gate generation.

Here is the complete bit-action bound. For u consecutive increments of a
binary word, total carry-bit reads/flips are at most2u+O(w), including any
initial alignment; sum over bit positions of their carry frequency is a
geometric series. The same holds for decrements and a fixed stride2. Thus
w accesses have O(w) actual carry/descriptor actions, not w independent
O(w) address reconstructions. A finite carry microprogram keeps its bit
position and tests the current bit; its short position increments/reset
cost at most a constant times the carry walk. Native counter fields are
aligned dyadic bit arrays: selecting a counter bit concatenates its fixed
field prefix and short index, with the full address fee paid. It requires
no separate arbitrary product or full-pointer copy at each carry bit.

Termination also has an actual O(w) total bound. Start short count c=w-1;
emit a bit, then ripple-decrement c and stop on BORROW. The borrow is the
existing carry flag. There is no full-field end comparison per bit, nor a
log(w)-bit equality test at each step. Its total reads/flips and final
reset are O(w+log w). The same construction works for inverse-direction
field walks. Every address setup/copy, staged bit write, index read, carry,
loop test, instruction and cleanup is included. A fetched field has O(w)
core actions and O(w) actual indexed accesses; EACH pays O(w). Therefore

 charged cost per field fetch <=C w^2.                   (3.1)

A fixed number/constant-depth collection of fields, opcode/branch/return
logic, shifts/additions and the indicated bit action or mapped gate has
cost<=C' w^2. The kernel uses O(w^2) staging at most, with a fixed number
of active words, not a physical classical recursion stack. It is a fixed
finite microprogram and does not invoke another bank interpreter for its
own addresses. No original quantum wire is read as a classical value.

Emit original actual Clifford+T words on the same genuine roles; their
controls stay quantum. Measurements/coins have the same distributions and
write the same semantic record. Reset/discard is measurement, conditional
X to zero and forgetting: the exact reference-safe trace-and-zero channel.
All source-private/sign/EXTRACT records and extra staged copies are erased
at their original logical release. No kernel readout/address trajectory
is new routing data, a new random coin or source feedback.

At each source request acquire EXACTLY ONE n+1-qubit original, SWAP it into
its designated zeroed genuine slots using three CNOTs per qubit, and release
the zeroed raw temporary wires. All quantum correlations move with it.
Its O(nw^2) work is charged against the original n+1 source CORE fee.
No original is acquired by a zero, extra READ, SWAP or inverse gate word.
All four source guards occur at their exact semantic points, including
already-built children before a refused weighted attempt.

Copy the ENTIRE output to counted physical classical output FIRST. Then
trace/zero/release the entire paired prefix, genuine pool, temporary roles,
padding and staged private copies. The same finite kernel pays
O((B+H+n+1)w^2) for initialization and complete scans/release. It stores
no hidden transcript or directory growing with elapsed execution time.

### 3.3 The new reference controller has the required CORE bound

Changing layouts is not assumed to preserve a generic flat-RAM CORE count.
We verify this GPS controller term by term. All word families are dyadic;
within a known ripple/add/copy/gate template, resident role counters sweep
consecutive slots. A length-z sweep has O(z+w) actual initialization,
carry-pointer, sentinel/borrow and instruction-generation core actions.
No w-bit gate descriptor is copied anew at each gate. All pointer/counter
bit actions are part of this reference ledger BEFORE the physical fee.
The chosen exact Boolean templates implement the same arithmetic/quantum
word as the source, with its actual inverse and clean scratch.

On the main branch w=O(log n)=O(R), by the source profile bounds. For a
residue predicate r_i controlled b_i-bit additions plus comparisons cost
O(r_i(b_i+w)+r_i+w)=O(R^2) core actions including source constants, pointer
initialization and all forward/reverse words. This remains valid for a
small bottom b_i: the bound is the source's GLOBAL R^2, not a claim that
setup fits b_i^2. Diffusion, fresh trials, fair clock bits, measurement/reset
and classical verification have O(R^2) core charge as well. Therefore all
combiner residue/Grover work is O(R^2 Wcap).

Full signed-label words have O(n) bits. Their add/shift/copy/loop/counter
and handle bookkeeping, with O(w) pointer setup per word, cost O(n r_i)
per supplied node input batch as before. Delivered inputs at a fixed level
have disjoint nonempty acquisition sets, even on failed/refused attempts;
the source charge O(nmQcap)+poly(n) remains valid. Records/caches are reused.

EXTRACT/transform words have length O(n), so O(w) pointer initialization
fits their linear core arithmetic. Its cheap runs/verification and globally
capped high-confidence fallbacks therefore retain the complete every-branch
O(n^2 log n Qcap) CORE charge. Long counters are actual ripple bit actions;
no exponentially large cap value is one machine operation. Fair coin output
locations are existing bounded counter fields, fetched by (3.1), not copied
to an additional reference header per coin. All such coin/gate bit actions
remain in the reference trace and are physically charged by (3.1).

Decoder modular residues/frequencies/endpoints have O(n) bits. Pointer setup
and the fixed finite table selection cost O(w)<=O(n) per updated record and
fit its existing O(n)-bit update charge; first-candidate products retain
O(n^2). The frequency guard and roots have the same O(n) charge. Thus the
source's conservative decoder bound O(n^3 K q0+n^3 K) still covers this
actual controller. Dyadic public layout/offset/padding construction adds
only polynomial bit work, within a conservative O(n^6) CORE setup bound
or the separately paid polynomial physical setup; it uses streaming O(n)
physical words and counted bank work, not an uncounted metadata table.

Now use the SAME literal cap/profile estimates proved in gps-source.md9:
R^2Wcap=O(n^(5/2)(log n)^(1/2)2^R), Qcap=O(n^-8 2^R),
m<=2R<=2n, K=O(R), q0=O(n^-10 2^R), and 2^R eventually exceeds every
fixed polynomial. All remaining terms above are smaller than the first,
with fixed finite exceptions contributing an absolute constant. Hence
(1.1) holds for THIS concrete dyadic reference, including all address-value
arithmetic and generation. Its semantic state/word/channel is the original
GPS algorithm's; changing its physical controller creates no new statistical
assumption or event. We have neither translated old flat pointers for free
nor assumed a free universal word-RAM compiler.

## 4. Full channel identity, including private-sign erasure

At aligned logical times, include fixed unread product originals U and an
arbitrary inaccessible reference R. The actual state has the CQ form

 sum_(c,z) p(c,z)|z><z|_kernel tensor |c><c|_basis-bank
                      tensor rho_(c,z)_(genuine,U,R).      (4.1)

Here c is V's genuine classical record and z is only bounded fetched copies/
finite functions of its fields. Conditional rho can depend on every record;
no state independence is asserted by this invariant. Forget duplicate
kernel values and relabel odd slots: the result is EXACTLY V's full state.

Initialization copies classical input and starts the same zero pools and
original source. READ projectors reveal a value already classical in c,
leaving conditional rho unchanged; a duplicate is forgotten when released.
WRITE and irreversible overwrite mix conditional states exactly as logical
classical forgetting does. Boolean logic and field decoding then preserve
the invariant. Mapped gates, measurements, coins, guards and return contexts
have the SAME instruments/probabilities as V. A source SWAP is only register
relabeling and reset has the exact reference-safe identity above. Induction
establishes (4.1) on every history, without any ideal-label, cap-survival,
high-part or decoder-success postselection.

For GPS-BLOCK the private exclusions matter. Original unsigned k and sign
sigma are overwritten after making signed a, and extraction-private records
are not routing data. Kernel copies may be used ONLY to implement V's own
specified update, and all extra copies are forgotten at that update's
release. No readout log, address trajectory or kernel transcript becomes a
new routing input. Thus logical low-residue routing and private erasure are
unchanged; a full-label-dependent implementation detail cannot introduce an
extra selection of leaves or alter the ideal untouched-high-part proof.
One can simply apply V's COMPLETE unconditional theorem to the identical
logical channel, instead of reproving a conditional law after new readouts.
The passive independent source cannot react to these extra deterministic
record copies. No stronger interactive-supplier statement is selected.

The final output distribution is EXACTLY V's for every N,s. All source label,
private signed-fiber, root tail, fallback/acquisition/weight/frequency-cutoff
and decoder events are already counted in that theorem, with ZERO additional
failure loss. This transfers success at least1-2^-8 including the full finite
branch. It does not add a positive malformed fraction or condition success
on a favorable acquired subset.

## 5. Actual every-branch resources, exact envelopes and indices

The physical allocation is SC=O(n)+O(w^2)=O(n) bits and ENTIRE
SQ=O(B+H+n+1)=O(n^2) qubits, including inactive/padded cells, all genuinely
coherent roles and current raw source wires. Virtual SCn^2,SQn are not the
actual declared pair. All combined-memory address fees are O(w)=O(log(n+2)).

Using the NEW CORE count (1.1), not only quantum gates or an uncharged word count,

 T_phys<=C w^2(A_*+B+H+n+1)+poly(n)
       =O(n^(5/2)(log2n)^(5/2)2^R)+poly(n)
       =O(n^(5/2)(log2n)^(5/2)2^(a sqrt(n log2n))).        (5.1)

The additional poly(n) is the paid public layout computation and fixed
control initialization. Every fixed polynomial is absorbed by the displayed
positive subexponential for all sufficiently large n; finite remaining
lengths have bounded explicit caps and contribute one absolute constant.
The exponent coefficient a is the source's proved exact rational, unchanged.
Its explicit threshold and uniform finite-prefix argument are included.
No inner unknown big-O coefficient or unbounded logarithm is guessed away.

All four source cutoffs remain literal logical guards, not an attempt to
charge physical kernel work for free. (5.1) bounds that work, ALL source
moves, original preparation, descriptor fetches, failed searches, private
coins, repeated instructions, refusal and complete cleanup on EVERY branch.
The ideal expectations in V's proof are used only for cutoff failure, never
as an actual-branch work bound here. Runtime is sequential work, not depth.

Exactly ONE original register is acquired for each V request, so its literal
Qcap and finite-branch acquisition rules transfer unchanged. In particular
Q=O(2^(a sqrt(n log2n))). Discarded copies and every unsuccessful tree/search
are included. No bank initialization or extra READ creates original samples.
The canonical independent-ideal-source promise and exact fraction0 transfer
by output-channel equality. The same all-N physical algorithm has ALL FIVE
guarantees jointly.

For time and samples, log2 of either representative is
a sqrt(n log2n)+O(log n), hence their exact growth index is1/2. The two
polynomial space representatives have index0. The supported declarations
are EXACTLY (0.1), with no claimed numeric objective for Q or fraction.
This is not a cube-root algorithm, a maximal tolerance result, a free-memory
simulation or an inference across different error-model contexts.
