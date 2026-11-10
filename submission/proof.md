# LLV-GRF320-BANK: counted basis storage for the period-six profile

## 0. One physical algorithm and complete joint theorem

For every N>=2 and s in Z/NZ, put n=ceil(log2N) and L=log2n for n>=2.
The ONE physical bit interpreter below executes the exact virtual LLV-GRF320
program V in virtual.md and recovers the entire secret with unconditional
probability at least1-2^-8. On EVERY branch, including failed/discarded work,
wrong extracted labels, source/leaf aborts, initialization and cleanup,

 T=O(2^((1/2)sqrt(n)log2n)), S_C=O(n), S_Q=O(n^(16/5)),
 Q=O(2^((1/2)sqrt(n))).

All outside constants are absolute. The finite n=1 case uses V's explicit
finite branch. Exact resource indices in T,S_C,S_Q,Q order are1/2,0,0,1/2.
The fifth claim is clean fraction0 in the canonical independent-ideal-copy
model. This is not positive error tolerance or a maximal-tolerance assertion.

V is fully supplied, not an opaque historical theorem. Its finite branch is
n<2^4096. Its main branch uses the exact integer rules in virtual.md Section0:
lambda=ceil(6ceil(log2n)/5), the centered floor(5i/6) fan-in ramp, exact prefix
capacity, one variable-arity/output finishing merge, fixed FIND schedule,
Dbar,Dcap,Ccap,Qcap and both all-modulus decoders. We change NONE of these.
Virtual classical and quantum declarations apply only to V. Physical classical
storage and qubits are the separate simultaneous allocation proved here.

The direct virtual source is published submission
bbb24880-18be-4ca8-8046-8a077fd30b06, commit
5dcb33fec0805d1681af853c10143990685a8b38, full proof SHA-256
060077647c623f8ca5678f5ff14ae54ce4d663c782e7ac508274953aa57331c9.
Its complete unchanged proof follows the eight-line scope header in virtual.md.
Its instrument, fresh-child/source/cap laws, incidence and held-out-bit arguments,
full decoder and weighted every-branch time proof are mathematical evidence.
No accepted verdict or verified ancestry is a proof premise.

The separately reused physical-template source is published
115e4fdb-4fcb-45ab-9511-170aafb2fa4b, commit
401a7f4940f32f29ffe72d1c774bf0b761dddbdd, full main proof SHA-256
7542da9ac969a686a72ed4780886b0eb115c92f6d2fd1f21f90b394ad104333d.
Its dense seven-region storage, entire paired prefix, typed ownership,
measured READ/WRITE, correlated-CQ simulation, exact source moves, output-first
cleanup and separately paid interpreter are restated. Its PSG virtual program,
quadratic layout and time/source formulas are NOT executed. We establish new
capacities for the period-six tables and lists and use its different strict
internal sqrt(n) work margin. Historical credits retained by the physical
source include LLV-GBANK300C ae91a0c4-f38a-47d0-b6c1-d3ed0a461b6d,
PSG21 and GordoAR PSG2-QSTORE. No generic simulation novelty is claimed.
Both direct material sources are declared with exact source/use citations.

## 1. Uniform virtual instruction stream and dense records

Take V's exact integer parameter rules, source sequence, fresh coins,
measurements, decoder, finite branch and guards. Expand every classical
arithmetic operation into ordinary finite bit operations, reads and writes,
and every quantum operation into its stated elementary Clifford+T gates.
The finite controller generates and consumes one such operation at a time.
Long loops, branch return states, operands, counters and generator cursors
are virtual records, not a stored exponential circuit or a physical
classical stack. The fixed program contains no instance-dependent advice.

V's record types have ordinary field/array semantics: pending labels and
quantum-register handles; current residues/found solutions; source counters;
profile/frames/caps; decoder records; arithmetic and generator scratch.
Implement them in the dense typed pools specified next. Field locators use
row, field and bit indices with exact schoolbook address arithmetic. A
released object returns its fixed slot to its pool and is cleared. Repeated
attempts reuse slots; no lifetime-index directory or history grows with time.
This is a concrete storage implementation of V's arrays, not a requirement
to retain unused padding from some older source. Values, gate operands,
control flow and the release time of the last owner remain V's.

The pending objects here are phase vectors, not PSG qubit nodes. Every retained
vector keeps its lambda-qubit index and complete table; the finishing vector
has one index qubit and two entries. The exact centered fan-in schedule and
fresh-child discard rule stay V's. Tables and their coherent handles are pooled
independently, and only the current MERGEF call keeps a tuple list. Ancestor
lists were released before their phase-vector result was returned. The explicit
capacities below include all still-owned objects, not just successful roots.


## 2. Explicit period-six capacities, padding and all metadata

Define t=n+2, ell=bit_length(n-1) (ell=0 when n=1),
lambda_bank=ceil(6ell/5), E=2^lambda_bank,

 A=2^16 t, W=2^128 t^2 E, H=2^32 t.

On the main branch lambda_bank is exactly V's lambda. These integer layout
rules apply even when V uses its finite branch. Since E>=n and
E<2^(11/5)n^(6/5)<5n^(6/5), one has t^3<=3t^2 E and W=O(n^(16/5)).
No irrational power is computed to choose an allocation. W and all base
addresses have O(logn) bits and are computed exactly by shifts and products.
A is a padded word size; the physical controller holds only a fixed number
of A-bit words. The whole backing range is allocated before sampling.

Reserve seven virtual-classical regions of W bits each, at bases jW:

 0 input, public parameters, finite constants, profile, precision and caps;
 1 pending phase-vector tables, their coherent handles and typed ownership;
 2 recursion frames, counters, return contexts and pool ownership;
 3 current residues, verified tuple list, rank, sorting and FIND state;
 4 source extraction, exact modular arithmetic and reusable bit scratch;
 5 decoder frequencies, basis/outcomes, candidates, scores and CRT scratch;
 6 instruction generation, dense field locators, allocators and cleanup cursors.

Assign padded subranges by prefix sums in that order. A bitmap or full scan
chooses a free fixed object slot, and all its metadata is bank data. A release
clears its object for reuse. There is no lifetime-indexed history or sparse
unbounded address range. The maximum classical-bank index is7W-1.

Here are explicit bounds for all object families on the main branch. Write
x=sqrt n and L=log2n only for analysis. V Section8 gives
m<=2x/L, lambda<=3L/2, kappa<=lambda, fan_max<=x,
fan_max*lambda<=n, and

 lambda sum_i fan_i<=n+m*kappa+3m*lambda<=n+12x<=2n.

The last inequality holds already at the enormous main threshold. Thus a
depth-first stack of full-level siblings, current inputs and a finishing
call needs fewer than16t retained table slots. Reserve exactly16t such slots,
each64AE bits: E rows of padded A-bit full labels, fixed flags and field
padding, and up to lambda coherent-wire handles of at most A bits each.
E>=lambda covers those handle fields as well. Each source or root two-entry
table is handled by the source/decoder pools or the same padded table slot.
The whole table pool is below2^30 t^2 E bits.

Use t+1 frame slots of256A bits each. A frame stores the level, counters,
return location and object-slot references; a separate array of all child
handles is NOT recopied into every frame. The table objects hold those handles.
The profile has at most t entries of fixed A-bit fields, or is generated from
its period-six formula. These families are below2^40 t^2 E bits including
bitmaps, fixed copies of pointers and scanning cursors.

Only the CURRENT MERGEF holds its verified tuple list. Every full or final
call has U=f*lambda<=n, mu<=2^(lambda+kappa), and
2^kappa<16(m+2)<=32t. Consequently

 Cp=2mu+1<=65tE.

Reserve four arrays of65tE rows of64A bits each for tuples and fixed copies,
verification/projection/rank and exclusion state. A tuple's U bits and all
its O(n)-bit fields fit in those64A bits. The total is below2^40 t^2 E bits.
This bound also covers f=1,b=0 and Cp exceeding the search domain: the
algorithm stops after the domain is exhausted and an empty-predicate call.
It does not allocate or retain a separate list for every ancestor.
The current residue/input/sort arrays have f<=t, E rows per input and a
fixed number of A-bit fields. Four64A-field copies fit below2^40 t^2 E bits.
Serial quantum lookups reuse their flags and scratch, rather than allocating
one coherent flag for every row. No coherent random access is supplied.

Source/parameter bounds are literal, not conditioned on correct extraction.
Full labels have3n bits by V Section9. Qcap<=2^(x/2), Y<=2x<=n on the main
branch, P_j=j+Y+8<=3n+8, all source/call/FIND loop counters and precision
values have O(n) bits. The fixed1024 powers have at most1024(L+1) bits,
which is below A. The power A_bar^m and all Dbar,Dcap,Ccap,Qcap values fit
A by V's source proof; their logarithms are at most x/2+O(L). All exact
signed numbers, CRT values and scores also fit the padded A-bit words.
Use fixed schoolbook arithmetic with at most2^16 A-bit temporary fields,
a fixed number of A^2-bit product/work arrays and reused bit scratch.
Even the looser2^64 t^3-bit allowance for this entire family is below
2^66 t^2 E. It includes source extraction counters and its fixed finite
4096-entry trigonometric table and polynomial generator scratch. Parameter
subroutines use no larger precision and no retained historical transcripts.

V's current decoder has K=2^13(2ceil(sqrt n)+ell+30)<=2^18 t root records.
Each record has at most64A bits for its complete signed frequency, phase-vector
handles, basis and outcome fields. Reserve2^18 t rows, below2^40 t^2 E bits.
Its candidate grid is streamed: no array of all2^(Y+8) candidates exists.
Center/score/CRT and modular increment scratch fit another2^64 t^3 bits.
Source and decoder stages reuse their fixed pools. On the finite branch
only the candidate, n+10 counter, modular arithmetic, input and output words
are required; they fit these same padded capacities, including n=1.

For coherent slots, pending index registers need O(lambda sum fan_i)=O(n)
wires. A current query has U<=n, b<=n and reused O(U+b) arithmetic/equality/
Toffoli ladders; source transforms/extraction take O(n) more. Serial row
processing reuses all scratch. Up to K<=2^18 t completed roots are stored.
The elementary ripple/serial templates use fewer than2^24 t coherent wires,
well below H=2^32 t, including source-moving scratch and the finite branch.
A bitmap and ordered list of H wire handles, padded to A bits per handle,
require HA+H<2^50 t^2 bits. Place all of them in region6; only a constant
number of known handles is streamed into physical control for one gate.

Every listed family, its fixed copies and its exact locator fields fit below
2^70 t^2 E bits, even adding all families assigned to one region. W leaves
more than a factor2^58 of slack. All padding, metadata and inactive array
capacity remain allocated and counted. No unknown historical big-O constant
is used to pick W: the explicit fixed arrays and schoolbook templates above
are the chosen implementation. Replacing them by slower scans is permitted
and paid in the time proof. V's values, order and ownership remain unchanged.

## 3. Counted physical wires, READ/WRITE and exact source calls

Represent virtual classical bit i at physical wire 2i and virtual coherent
slot j at physical wire 2j+1. Reserve the WHOLE paired prefix through
2max(7W,H)+3, including every unused even/odd cell and padding, initially
in |0>. Its size is O(t^2 E)=O(n^(16/5)). This fixed prefix is the physical allocation;
no sparse-index assumption or free quantum memory access is used.

READ(i) measures the known even wire in the computational basis into one
reusable physical classical bit. WRITE(i,b) performs READ(i) and applies X
iff its old value differs from b. Releasing a virtual classical field writes
zero to its cells, allowing reuse without a history of old values. For a
classical Boolean operation, READ its constant number of operand bits,
perform that same Boolean logic in short control, and WRITE its result.
Long numbers are processed bit by bit; only counted O(n)-bit staging,
including input/output, may remain classical. Everything else is bank data.

All wire addresses are classically chosen and cost their full logarithmic
address fee. They are computed by the finite bit interpreter, not obtained
from a superposed quantum pointer. For a conservative work upper bound,
even a complete scan of the polynomial bank per access may be charged.
Such a scan is not QRAM. V's existing quantum-controlled subset-sum gates
and source arithmetic keep their original coherent controls. The known
classical constants and exclusion strings are READ one bit at a time to
emit the same gates on their mapped coherent wires. A superposed original
query index never becomes an address into the bank.

Measurements, random coins, resets, releases, guards and returns execute at
exactly their virtual positions. A measured bit is staged only long enough
to WRITE its virtual destination; no physical classical transcript grows.
For a source request, first reserve zeroed mapped coherent slots, acquire
exactly ONE fresh DCP copy on n+1 temporary wires, and stream known slot IDs
to SWAP its qubits into place. Each SWAP uses three CNOTs. The now-zero
temporary wires are released before the next request. This adds O(n) qubits
and counted O(n) gates, not another DCP copy. No bank initialization calls
the source, its inverse, its purification or a controlled source operation.

For reset/discard use computational-basis measurement, conditional X and
forgetting the outcome. This is exactly trace-out followed by a fresh zero,
even with arbitrary entangled references. Do not reset a shared coherent
slot before its last virtual owner releases it. After V returns, stream the
final residue to the counted O(n)-bit classical output FIRST; only then
clear and release the entire paired prefix and scratch. All cleanup is paid.

## 4. Correlated classical-quantum simulation invariant

At aligned virtual steps, including arbitrary reference R, the joint state is

 sum_(c,z) p(c,z) |z><z|_controller tensor |c><c|_bank
                  tensor rho_(c,z)_(mapped V registers,R).

Here c is precisely V's classical record, z its finite physical control and
short staging. The basis-bank values can be classically correlated with
arbitrary coherent states; a label need not be independent of its phase
qubit. This is a CQ decomposition, not an assumption of a product state.

Initialization satisfies the invariant. READ's basis projectors append the
same classical bit value to short control and leave each conditional rho
unchanged. WRITE updates exactly the indicated basis string. If two records
merge after an irreversible overwrite, their conditional states mix exactly
as classical forgetting does. The same holds for Boolean steps, pointers
and field translations. Original gates act identically under the same
controls; original measurements and coins have the same instruments and
update the same virtual c. Reset/discard has the channel identity above.
Each fresh ideal source request supplies the same independent rho_s.
Induction therefore preserves the complete virtual reduced state and output
law on every branch, including failed extraction, wrong labels, partial
children, rejected copies and abort cleanup. Added READ outcomes are
deterministic given the virtual classical record; no favorable event or
accepted verdict is conditioned on.

This argument would be false for an arbitrary coherently superposed bank,
and it makes no such claim. It also does not transfer an adversarial noisy
supplier model in which extra public measurements could alter future inputs.
Only the exact independent-ideal-copy model and fraction 0 are claimed here.
The complete V argument in virtual.md therefore proves full-secret success
at least 1-2^-8 for every N and s for this ONE physical interpreter.


## 5. Simultaneous physical resources and the strict work margin

The physical classical input and final output use O(n) bits. A fixed number
of A-bit staged operands, finite control and O(logn)-bit address/scan fields
also use O(n). Every large loop counter collection, recursion frame, table,
label, tuple list, instruction descriptor, ownership field and measurement
record is virtual bank data. No duplicate classical array or physical
classical call stack exists. Therefore S_C=O(n) on EVERY branch, including
setup, output and cleanup.

The ENTIRE paired prefix through2max(7W,H)+3 is allocated. Its size is
O(W+H)=O(t^2 E)=O(n^(16/5)), including unused even and odd cells, all basis
storage, coherent slots, metadata and padding. A temporary fresh source uses
n+1 additional wires, and short arithmetic/source-moving scratch is O(n).
All addresses pay the full charge for this entire allocation. Hence physical
S_Q=O(n^(16/5)) jointly with physical S_C=O(n). There is no claim that the
quantum bank fits V's original linear quantum bound.

For a conservative charged work bound, field-location arithmetic, bit
emulation, measured storage access, mapped gate generation, wire ownership
and source SWAPs take at most a fixed polynomial in n per virtual primitive.
Even a full scan of the polynomial bank per primitive can be charged. Fixed
allocations, initialization and clearing the whole prefix take polynomial
work, as does output staging. V's existing source/leaf caps and fixed FIND
schedule are unchanged. Extra interpretation is separately paid, not hidden
by enlarging any of those guards. With fixed absolute polynomial P,

 T_physical<=P(n)[T_V+(7W+H)^2+n^2].                (5.1)

This holds branchwise including incomplete children, wrong labels, failed
queries, rejected copies, overflow/leaf aborts and cleanup. Weighted source
and level charging in V is an upper bound on EVERY virtual branch, so it
also bounds the number of emitted virtual instructions. No expected-time
claim is substituted for (5.1).

It remains essential that (5.1) preserve the exact pure exponential time,
rather than multiply a tight representative by an unjustified polynomial.
V Section14 proves, uniformly over all literal profiles and branches,

 log2(T_V/C)<=xL/2-(487/51200)x+o(x), x=sqrt n.

This includes the virtual polynomial/address/source/cleanup ledger and all
finishing-call cases. Put eta=487/102400>0. By the definition of the uniform
o(x) remainder, eventually T_V<=C*2^(xL/2-eta*x). All costs in P(n), W and H
are polynomial, and log2 n=o(sqrt n). Thus the added polynomial multiplier
uses at most eta*x/2 in the exponent eventually. The standalone polynomial
setup/cleanup term is also smaller than2^(xL/2). Therefore

 T_physical=O(2^((1/2)sqrt(n)log2n)).               (5.2)

Every remaining input length lies in a fixed finite set and has finite
literal caps and the same padded storage implementation. Such lengths,
including V's explicit finite branch, change only the absolute outer
constant. This is an asymptotic proof, not a practical finite-size timing
claim. It uses the source's proved strict gap after charged work, not its
historical acceptance as a premise.

Each virtual acquisition is simulated by exactly ONE original source
acquisition. Bank zeros, padding, measurements and resets are not DCP copies.
The complete source-request sequence is unchanged, so V's literal main cap

 Q<=Qcap=n*Ccap+K<=2^((1/2)sqrt n)

transfers branchwise, counting every failed/discarded attempt and abort.
The finite branch is absorbed by an absolute outside constant, yielding the
same declared Q=O(2^((1/2)sqrt n)) for all N and s. The correlated-CQ invariant
preserves V's full output law, hence success at least1-2^-8 and clean fraction0.

For n>=2, the time logarithm has leading(1/2)sqrt(n)log2n and the source
logarithm has leading(1/2)sqrt(n); both have exact growth index1/2. Physical
polynomial spaces have exact index0. All five statements concern this ONE
interpreter and its counted allocation. They are a memory trade-off against
V: smaller classical memory, larger quantum memory. No global optimality,
new generic simulation principle, practical timing or cube-root-time claim
is made. The complete virtual proof remains scoped to V and is mathematical
evidence for this separately proved physical execution.
