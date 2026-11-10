# LLV-GRF320-BANK-LOG: a smaller fully allocated polynomial quantum bank

## 0. One physical algorithm and complete joint theorem

For every N>=2 and s in Z/NZ, put n=ceil(log2N). In asymptotic formulas
n>=2 and L=log2n; set L=1 at n=1 for the separately finite branch. The ONE
physical interpreter below executes the complete unchanged virtual period-six
LLV-GRF320 program in virtual.md. It recovers the entire secret with
unconditional probability at least1-2^-8 and has on EVERY branch

 T=O(2^((1/2)sqrt(n)log2n)), S_C=O(n),
 S_Q=O(n^(16/5)/log2n), Q=O(2^((1/2)sqrt(n))).

The n=1 case has fixed finite resources. Every outside constant is absolute.
Failed/discarded work, wrong labels, source/leaf aborts, initialization and
cleanup are included. Exact resource indices are1/2,0,0,1/2. The fifth claim
is clean fraction0 in the canonical independent-ideal-copy model. No positive
corruption guarantee or maximal-tolerance claim is made.

The complete immediate algorithm/proof source is LLV-GRF320-BANK,
submission57edafa4-54b0-4e3e-a6ac-da93adb53605, full main SHA-256
1fdec87f928564eede1004b8cf90d1dfd35794b7419ab5057e49ee4009518bd1.
Its entire virtual.md is copied unchanged, and the physical instruction,
source-move, CQ simulation, ownership and paid-work proofs are retained here.
All source/leaf caps, the centered fan-in profile, MERGEF, fixed FIND schedule
and complete all-modulus decoder remain the SAME V. No earlier verdict is a
mathematical premise. The change is the ACTUAL reserved bank and object pools:
we do not apply a smaller upper bound to the older, still-padded allocation.

The immediate parent carries the full virtual LLV-GRF320 proof originally
published asbbb24880-18be-4ca8-8046-8a077fd30b06 and the physical-template
method from115e4fdb-4fcb-45ab-9511-170aafb2fa4b. Their material is used through
the complete immediate archive, including its unchanged virtual source.
The historical LLV-GBANK300C, PSG21 and PSG2-QSTORE credits are retained.
This candidate does not claim independence, a new generic simulation method,
or verified ancestry from provisional references. Its explicit dependency
selects the exact immediate source/use passages, including both full programs.

V's finite branch is n<2^4096. Otherwise it uses its unchanged exact integer
period-six fan-in rules, lambda=ceil(6ceil(log2n)/5), prefix allocation,
one variable-output finishing call, Dbar,Dcap,Ccap,Qcap and fixed schedules.
The virtual n^(16/5) classical and linear quantum memory declarations are
scoped ONLY to V. The simultaneous physical spaces are the new allocation
proved below; physical classical memory is not mixed with a virtual column.

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


## 2. Logarithmically smaller fixed capacities, including every padded cell

Define t=n+2, ell=bit_length(n-1) (zero at n=1), d=max(1,ell),
lambda_bank=ceil(6ell/5), E=2^lambda_bank, and the exact integer layout

 A=2^16 t, W=ceil(2^128 t^2 E/d), H=2^32 t.

Each of seven regions has exactly W virtual-classical bit cells at bases jW,
j=0,...,6. Integer division with remainder implements the ceiling. On V's
main branch lambda_bank is exactly its lambda. For all n>=1, E>=n, E>=d
and E>=lambda_bank. Also E<5n^(6/5). Since t<=3n and d>=log2n for n>=2,

 W=O(n^(16/5)/log2n), and W>=2^128 t^2.

All base addresses have O(logn) bits and are computed exactly. A is a padded
word size. A fixed number of A-bit words is short physical staging; large
fields and all generator/locator/allocator state are basis-bank data. There
is no irrational-power allocation or unknown historical big-O constant.

The seven dense regions have the same types as the immediate parent:

 0 input, parameters, finite constants, profile, precision and cap values;
 1 pending complete phase-vector tables, coherent handles and ownership;
 2 frames, saved counters, returns and pool ownership;
 3 current residues, verified tuples, sort/rank/projection and FIND state;
 4 source extraction, modular arithmetic and reusable schoolbook scratch;
 5 decoder frequencies, outcomes, candidate/score and CRT scratch;
 6 instruction generation, dense field locators, allocators and cleanup cursors.

Assign the following fixed subranges in listed order by prefix sums, retaining
all unused remainder as counted padding. A bitmap/full scan allocates a fixed
object slot; a release clears it for reuse. The maximum bank index is7W-1.
There is no directory indexed by elapsed time or unbounded past transcript.
Only the current MERGEF keeps its tuple list; ancestors retain their returned
tables after those earlier lists and scratch were released.

All following main-branch inequalities refer to the unchanged V and hold at
n>=2^4096. Put x=sqrt n and L=log2n for analysis. V gives
m<=2x/L, lambda<=3L/2, kappa<=lambda, fan_max<=x,
fan_max*lambda<=n, and lambda*sum_i fan_i<=n+12x<=2n.
Also d<=2L, d<=x, x<=t/2 and n>=8d on this branch.

Pending tables. Source one-qubit records during a LEAF construction stay in
the source pool, whose lambda labels and handles fit its A-bit scratch fields.
Completed one-qubit roots transfer their two labels and handle to the decoder
record pool, releasing the constructor table slot without resetting that still-
owned coherent qubit. Thus Mtab below is the full-table constructor/pending
pool, not an extra directory of all K completed roots or individual source
qubits. Its number, including current full-vector inputs, the finishing call
and temporary output, is at mostsum_i fan_i+fan_max+8. Since lambda>=d,

 sum_i fan_i<=2n/d, fan_max<=x<=n/d,
 sum_i fan_i+fan_max+8<=4n/d.

Reserve Mtab=ceil(8t/d) table slots, each64AE bits exactly as in the parent:
E rows of padded A-bit full labels and flags, plus up to lambda coherent-wire
handles of at most A bits each. E>=lambda covers those handles. Since t/d>=1,
Mtab<=9t/d, and the whole pool is below2^30 t^2E/d bits. No compressibility of
random labels is assumed; the saving is FEWER FULLY ALLOCATED slots.

Frames and public profile. Reserve t+1 frame slots of256A bits and t profile
entries of fixed A-bit fields. A frame has level, counters, return and object
references; pending child handles stay with the table objects and are not
copied as a growing array into each frame. These and their fixed bitmaps and
cursors are O(t^2) bits and fit below2^40 t^2E/d because E>=d. Generating the
period-six profile on demand is also allowed and charged.

Current tuple list. From m<=2x/L, d<=2L, x<=t/2 and t/d>=1,

 m+2<=4t/d, 2^kappa<16(m+2)<64t/d.

Every full or final call has U=f*lambda<=n and mu<=E*2^kappa. Consequently
Cp=2mu+1<=129tE/d. Reserve FOUR arrays of
Mlist=ceil(256tE/d) rows, each64A bits, for the current tuples, fixed copies,
rank/projection/exclusion and verification fields. Each U-bit tuple and its
O(n)-bit fields fits in64A. Since tE/d>=1, Mlist<=257tE/d, and all four arrays
are below2^40 t^2E/d bits. This includes f=1,b=0, premature NONE, and Cp
exceeding the domain: after exhaustion an empty-predicate call stops listing.
No ancestor has another still-live tuple list.

Current input/residue/sort arrays. Here f<=fan_max<=x<=n/d<=t/d, with E rows
per input and a fixed number of A-bit fields. Reserve four arrays of
Mres=ceil(8tE/d) rows of64A bits. All arrays and their fixed flags/cursors fit
below2^40 t^2E/d. Serial quantum row/exclusion scans reuse equality flags;
there is not one coherent flag per row and no quantum-addressed bank access.

Main arithmetic and extraction scratch. The parent field bounds are unchanged:
full labels have3n bits, Qcap<=2^(x/2), Y<=2x<=n, decoder precision P_j<=3n+8,
and every source/FIND loop counter and score has O(n) bits. The two fixed1024
powers fit inA, as do A_bar^m and every cap/precision value. Use the same fixed
schoolbook templates: at most2^16 A-bit temporary fields, a fixed number of
A^2-bit product arrays and reused scratch. The deliberately loose total bound
2^64 t^3 includes source extraction counters, fixed finite trigonometric data
and polynomial generator scratch. It fits the smaller bank UNIFORMLY in n
because the exact public dimensions obey

 d*t<=12E, hence t^3<=12t^2E/d.                     (2.1)

Here is an all-size proof, including n=1. For ell>=1 the elementary bound
ell^5<=2^(ell+9) holds: check ell=1,...,8, after which the ratio ell^5/2^ell
decreases since(9/8)^5<2. Since n>=2^(ell-1), this gives d^5<=1024n.
Also E^5>=n^6 by the exact ceiling rule. Therefore4E>=n*d, and t<=3n
proves(2.1). At n=1, d=E=1 and t=3 satisfy it directly. Consequently the
entire loose scratch family is below2^68 t^2E/d, including its reserved
unused padding. All main intermediate widths and exact locators remain
within the same padded A-bit fields.

Decoder and coherent ownership. K<=2^18t root records of64A bits require
below2^40 t^2 bits, hence below2^40 t^2E/d. The candidate grid is streamed;
there is no array of all2^(Y+8) candidates. Its main center/score/CRT scratch
fits another2^64t^3 bits by the all-size inequality(2.1). Original coherent
slots remain H=2^32t: pending indices, current O(U+b) scratch with U,b<=n,
source/extraction wires and completed root qubits use fewer than2^24t by the
same elementary serial/ripple templates. H A-bit wire handles and a bitmap
occupy HA+H<2^50t^2 bits in region6, also covered by E>=d. Only a constant
number of known handles is streamed into physical control for one gate.

Finite branch. For n<2^4096 V uses only its candidate, n+10 counter, modular
addition, input and output with fixed A-bit words and O(t^2) reusable scratch.
It does NOT run the main profile or main decoder. The same bank satisfies
W>=2^128t^2, so these operations fit for EVERY such n, including n=1. Even
the fully reserved unused main scratch padding fits by(2.1); it is not
silently removed from the physical allocation. The public layout's own integer computation uses O(logn)-bit values
and fits the same short-word/bank implementation.

Adding every family and its fixed copies assigned to any one region is below
2^70 t^2E/d. W is at least2^128 t^2E/d and leaves a factor2^58 of slack.
Ceilings, padding, allocator maps, source-moving records and cleanup cursors
are included. Repeated failures reuse these FIXED smaller capacities. The
saving is not an observed average, a favorable-history condition or a dropped
logarithmic metadata term. Values, order, source calls and last-owner release
stay exactly V's.

## 3. Counted physical wires, READ/WRITE and exact source calls

Represent virtual classical bit i at physical wire 2i and virtual coherent
slot j at physical wire 2j+1. Reserve the WHOLE paired prefix through
2max(7W,H)+3, including every unused even/odd cell and padding, initially
in |0>. Its size is O(t^2 E/d)=O(n^(16/5)/log2n). This fixed prefix is the physical allocation;
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
O(W+H)=O(t^2 E/d)=O(n^(16/5)/log2n), including unused even and odd cells, all basis
storage, coherent slots, metadata and padding. A temporary fresh source uses
n+1 additional wires, and short arithmetic/source-moving scratch is O(n).
All addresses pay the full charge for this entire allocation. Hence physical
S_Q=O(n^(16/5)/log2n) jointly with physical S_C=O(n). There is no claim that the
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
