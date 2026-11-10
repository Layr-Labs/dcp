# LLV-GRF320-DENSE: counted dense classical records with linear coherent storage

## 0. One physical algorithm and complete joint theorem

For every N>=2 and s in Z/NZ, put n=ceil(log2N). For asymptotic formulas
n>=2 and L=log2n; the case n=1 is separately finite. The ONE physical dense
classical-storage interpreter below executes the complete unchanged virtual
LLV-GRF320 program in virtual.md, with unconditional entire-secret success
at least1-2^-8. On EVERY branch jointly it has

 T=O(2^((1/2)sqrt(n)log2n)), S_C=O(n^(16/5)/log2n),
 S_Q=O(n), Q=O(2^((1/2)sqrt(n))).

Every outside constant is absolute. Wrong extracted labels, failed searches,
discarded copies, source/leaf aborts, setup, output and cleanup are included.
Resource indices in T,S_C,S_Q,Q order are1/2,0,0,1/2. The fifth claim is
clean fraction0 under the canonical independent-ideal-copy model. No positive
robustness or maximal-tolerance assertion is made.

All large records here are ordinary CLASSICAL bits. Genuine phase indices,
query registers, source registers and coherent scratch occupy separate
quantum wires. Numeric table labels and wire handles are classical fields;
they do not contain the unknown phase amplitudes. The program allocates7W
classical bits and H original coherent slots as defined in Section2, with
all padding counted in the corresponding resource. No paired even/odd wire
prefix is allocated. Classical storage and quantum storage are simultaneous
bounds for this single implementation, not columns borrowed from two programs.

The complete immediate source is LLV-GRF320-BANK-LOG,
submission028b51aa-4aa5-43ef-9412-576796e0ef6b, full main proof SHA-256
5af4e2246a865dadce3c3b3c8b7dce759b2dab6c3308f8af9510612c0f5d90c2.
Its source virtual.md has full-file SHA-256
80fcc2af7da4711ea8e5bf03726be5e5caec06b86e98e2d4196ed34d7e50917b.
The entire program/proof body after its eight-line header is copied unchanged;
only that scope header now describes this DENSE classical/coherent allocation. The public source mapping, integrity checks and exact
source/use citations accompany the note/declaration after publication.
The immediate archive supplies the complete V, its strict time/source ledger,
and the smaller dense record capacities and all-size scratch lemma restated
below. Here the physical records are classical, and the original coherent
slots are allocated separately; the execution invariant is proved explicitly.
No historical acceptance is a mathematical premise.

The immediate source carries the period-six virtual proof originally from
bbb24880-18be-4ca8-8046-8a077fd30b06 and the counted storage method through
57edafa4-54b0-4e3e-a6ac-da93adb53605 and115e4fdb-4fcb-45ab-9511-170aafb2fa4b.
Their historical LLV-GBANK300C, PSG21 and PSG2-QSTORE credits are retained.
All material used for this candidate is contained in the complete immediate
archive; no distinct ancestor feature outside it is separately imported.
No new generic simulation principle, independent authorship, priority,
verified ancestry or global optimum is claimed.

V's exact finite branch is n<2^4096. On its main branch all integer parameters,
centered period-six fan-in, variable-arity/output MERGEF, fixed FIND schedule,
source/leaf/global caps, and all-modulus decoder are unchanged. Its earlier
n^(16/5) classical declaration is virtual evidence only; the actual dense
classical allocation below proves the stronger logarithmic representative.

## 1. Uniform virtual instruction stream and dense records

Take V's exact integer parameter rules, source sequence, fresh coins,
measurements, decoder, finite branch and guards. Expand every classical
arithmetic operation into ordinary finite bit operations, reads and writes,
and every quantum operation into its stated elementary Clifford+T gates.
The finite controller generates and consumes one such operation at a time.
Long loops, branch return states, operands, counters and generator cursors
are records in the counted classical backing. The finite controller uses no
additional uncounted array, stack or exponential circuit. The fixed program contains no instance-dependent advice.

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

Reserve7W ordinary classical bits for seven regions, each exactly W cells at bases jW,
j=0,...,6. Reserve H contiguous ORIGINAL COHERENT quantum slots separately,
including their unused padding. Integer division with remainder implements the ceiling. On V's
main branch lambda_bank is exactly its lambda. For all n>=1, E>=n, E>=d
and E>=lambda_bank. Also E<5n^(6/5). Since t<=3n and d>=log2n for n>=2,

 W=O(n^(16/5)/log2n), and W>=2^128 t^2.

All base addresses have O(logn) bits and are computed exactly. A is a padded
word size. A fixed number of A-bit words is short physical staging; large
fields and all generator/locator/allocator state are classical backing data. There
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

## 3. Classical backing operations, mapped coherent wires and source calls

The seven regions are an ordinary dense classical bit array, with bit index
0 through7W-1. The original coherent register pool is a separate contiguous
array of H qubits. Every cell in BOTH arrays is allocated and counted, even
when unused. There is no physical qubit encoding of the large classical array.
Zero initialization of7W classical bits and H qubits is explicitly paid.

READ_C(i) performs one classical bit read from the known integer address i.
WRITE_C(i,b) performs a classical bit write. A virtual Boolean operation reads
its constant number of operand bits, performs the same Boolean logic, and
writes the result. Long integers are processed by the specified finite bit
routines, using the counted backing scratch and a fixed number of A-bit staged
words. Frame state, long counter collections and ownership maps live in the
counted regions. Short staging, physical input N and final output add O(n)
classical bits beyond7W; they are included in the classical bound.

Every bit access and classically addressed quantum gate pays the full
ceil(log2(S_C+S_Q+2)) address charge for the COMBINED physical allocation,
including all classical backing and all coherent padding. The fact that a
quantum wire ID has fewer bits does not remove that combined-memory charge.
Field locators, bit copies, row scans, gate generation, allocator scans and
address arithmetic are implemented by ordinary finite bit operations and
charged separately. Even a full scan of the polynomial classical backing
per virtual primitive gives a conservative polynomial simulation factor.

The original quantum operations act only on their mapped coherent wires.
Their known classical constants and tuple/exclusion strings are read serially
from the classical array to emit the SAME gates as V. In particular, a serial
LOOKUP loops over classically known rows and computes equality against the
original quantum index in coherent scratch; constant row bits control which
flag-controlled gates are emitted. A superposed original index is never used
as a classical-memory address. There is no QRAM or unit-cost coherent lookup.

Original quantum measurements and random coins occur at their original
positions. Their classical outcomes are written to their declared classical
records, so no additional transcript grows outside the allocation. An original
coherent slot is reset/reused only after its last typed owner releases it.
For reset/discard, measure it in the computational basis, conditionally applyX
to set zero, and forget the outcome. As a channel this is trace-out followed
by a fresh zero, even with entangled reference systems.

On a virtual source request, reserve zeroed mapped coherent slots, acquire
exactly ONE independent original DCP copy on n+1 temporary qubits, and SWAP
its qubits into those slots using three CNOTs per SWAP. The now-zero temporary
wires are released before the next request. This adds O(n) qubits and paid
O(n) gates; it neither adds another DCP sample nor invokes source inversion,
purification or controlled preparation. Bank initialization and scratch zeros
never request a source copy.

All guards, source/leaf counts, fixed FIND bounds and return values stay V's.
The final residue is staged into the counted classical output FIRST. Then
clear all7W backing bits, reset and release the entire H coherent pool and
short scratch, paying for every operation. Output and cleanup are included
on failure/abort branches as well. No original unknown coherent state is
stored as a classical table entry; all such states remain in the H pool.

## 4. Exact classical-record/quantum instrument invariant

At aligned virtual steps, including an arbitrary reference R, the hybrid state
has the block form

 sum_(c,z) p(c,z) [c,z]_classical tensor rho_(c,z)_(mapped V registers,R).

Here c is V's complete classical record, represented in the counted classical
backing; z is the finite control and fixed short staging. Classical data may
be correlated with arbitrary conditional quantum states. This is a classical-
quantum decomposition, not a product-state assumption or a conversion of
unknown quantum amplitudes into classical bits.

Initialization establishes the correspondence of all records and zeroed
coherent slots. READ_C returns exactly the represented bit without changing
its conditional quantum state; WRITE_C and Boolean updates change exactly the
classical record V would change. If irreversible overwrite/forgetting combines
records, their conditional states mix exactly as ordinary classical forgetting
does. Locators and allocator metadata implement the same typed ownership and
logical register handles, so they do not change a quantum register's value.

An original gate under the same classical controls is the identical unitary
on its mapped coherent operands. An original measurement or coin has the
same instrument and writes the same classical result. Reset/discard has the
channel identity in Section3 and cannot reset a still-owned state. A source
request supplies the same independent rho_s and the SWAP relocation preserves
its full state. Induction proves equality of the complete output law and the
reduced state of every original coherent register/reference on EVERY branch,
including wrong extraction, partial children, failed queries and abort cleanup.
No event is selected as favorable, and no prior verdict is conditioned on.

Consequently the complete virtual proof in virtual.md establishes full-secret
success at least1-2^-8 for every N,s under the stated independent ideal-copy
promise for this ONE dense classical-storage execution. The source cap and
all branchwise work/scratch schedules are unchanged. The fifth claim is only
fraction0 under that exact model; no stronger supplier/noise promise is assumed.

## 5. All simultaneous physical resources and exact envelopes

The physical classical allocation is7W plus O(n) bits for input/output, finite
control, a fixed number of A-bit staged words and logarithmic addresses. All
larger records, frame state, field maps, labels, tuples, source/decoder records,
allocator metadata and temporary arithmetic are in those explicitly counted
regions. Their inactive capacity and padding are included. Since E<5n^(6/5),
t<=3n and d>=log2n for n>=2,

 S_C=7W+O(n)=O(n^(16/5)/log2n).

The n=1 case has fixed finite resources. This is a bound for the actual dense
classical allocation; the older n^(16/5) virtual declaration is not its proof.

The ENTIRE original coherent pool H=2^32t, including every unused slot, is
allocated separately. Its genuine phase-index, query, source and reset scratch
occupancy is bounded in Section2 using the supplied elementary primitives.
Temporary fresh-source wires add n+1 and other short quantum staging is O(n).
No qubits are allocated for the large classical backing, and there is no
paired-wire bank prefix. Thus

 S_Q=H+O(n)=O(n)

jointly with the stated classical bound on every branch, including setup,
source relocation, output and cleanup. Quantum source states, phase indices
and query amplitudes stay quantum throughout. Their classical handles and
known numeric labels are not additional uncounted storage.

All actual work is paid. The complete combined-memory address fee is used
for classical operations and original gates. Finite field-location arithmetic,
serial reads, Boolean emulation, branch/allocator management, gate/circuit
generation, source SWAPs and even full backing scans per virtual primitive
have a fixed polynomial cost in n. Initialization, zeroing and output-first
cleanup of the WHOLE classical and coherent allocation are polynomial too.
With a fixed absolute polynomial P, branchwise

 T_dense<=P(n)[T_V+(7W+H)^2+n^2].                  (5.1)

No cap or search schedule is enlarged to conceal this overhead. V's weighted
per-level consumed-leaf ledger bounds EVERY virtual branch, not just its
expected work. It supplies the stronger internal theorem, with x=sqrt n,

 log2(T_V/C)<=xL/2-(487/51200)x+o(x).

Put eta=487/102400. Eventually T_V<=C*2^(xL/2-eta*x). All new allocations
and costs in(5.1) are polynomial. Their added exponent is O(logn)=o(sqrt n),
which fits inside half the eta*x margin eventually. The standalone setup/
cleanup polynomial is smaller still. All remaining finite lengths have the
same literal finite caps and change only an absolute outside constant. Hence

 T_dense=O(2^((1/2)sqrt(n)log2n)).                  (5.2)

Every virtual acquisition corresponds to exactly one original independent DCP
source request; no backing cell or scratch zero is a sample. Therefore V's
literal main capQ<=n*Ccap+K<=2^((1/2)sqrt n) transfers branchwise, counting
all failures and rejected copies. The explicit finite branch is covered by an
absolute constant. Jointly Q=O(2^((1/2)sqrt n)) and full-secret success is at
least1-2^-8 under the exact clean model.

The time and source envelopes have exact growth index1/2. Polynomial
classical n^(16/5)/(log2n) and quantum n have exact index0. All five objects
concern the SAME dense classical execution and its real simultaneous storage.
Relative to the original LLV-GRF320 virtual representative, the classical
representative improves by1/log2n with the same T,Q,S_Q and clean guarantee.
Relative to the immediate quantum-bank parent this is a complementary memory
configuration, with larger classical storage and fewer qubits. No new generic
simulation theorem, global optimum, practical timing or cube-root exponent is
claimed. All mathematical proof premises are supplied, not historical reviews.
