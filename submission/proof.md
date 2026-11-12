# PSG4-QLOG-BANK: linear classical control for the quarter-step profile

## 0. One physical program, complete sources and selected theorem

For every N>=2 and s in Z/NZ let n=ceil(log2 N). For n>=2 put
L=log2 n, F=sqrt(nL), G=sqrt(n)L^(-3/8), J=sqrt(n)L^(-7/16).
The ONE physical interpreter in Sections 1-4 executes the COMPLETE V
program supplied byte for byte in virtual.md and family-source.md.
Its unconditional full-secret success is at least 1-2^-8 and its
joint bounds on EVERY branch, including setup, failed attempts, discarded
copies, wrong labels, both aborts, output and cleanup, are

 T=O(2^((3/4)F+(3/4)G-J/12)), S_C=O(n), S_Q=O(n^2),
 Q=O(2^((1/2)F-(3/2)G+3J/16)).

All outside constants are absolute independent of N,s,outcomes. The
explicit finite exhaustive branch of V covers n=1. Exact growth indices
are 1/2,0,0,1/2. Fractional error tolerance is zero under the canonical
independent-ideal-copy model below. No positive tolerance or impossibility
claim is made. This is a memory tradeoff within the known square-root
sieve family, not a cube-root algorithm or generic simulation novelty.

Two direct material sources are used and declared when published:

* PSG4-QLOG, submission 8870de8c-e8dd-4d03-82c7-57842e846e4f, supplies
  the complete selected V, including its new actual integer quarter-step
  schedule, exact capacity expansion, source remainder and charged ledgers.
  Its full proof is copied without modification into virtual.md, SHA-256
  6db1988013b27ef3ce4f266954ebac9c624bbf1989da272c4021ba78027bde09.
  family-source.md is the same complete unmodified source, SHA-256
  11f96191f1ab9c78f070472c4cb5e0552ec25381398ffc13b51d7f9c1b7c3fc7.
  Its direct and historical credits are preserved. These are VIRTUAL
  resource guarantees; they are not the physical memory columns here.
* PSG4-LOGLOG-ENDPOINT-BANK, 115e4fdb-4fcb-45ab-9511-170aafb2fa4b,
  evaluated commit 401a7f4940f32f29ffe72d1c774bf0b761dddbdd, supplies
  the complete seven-region padded layout, bit interpreter, measured
  READ/WRITE, typed ownership, correlated-CQ invariant, source moves and
  output-first cleanup. Sections 1-4 below adapt that physical template.
  Its selected endpoint V and numerical time/source bounds are NOT used.

The bank source credits SECOND-SCALE-BANK, LLV-GBANK300C,
PSG21 and PSG2-QSTORE. These historical credits are retained; no old
acceptance or provisional attribution relationship is a mathematical lemma.
All needed physical operations and correctness are given below, and all
needed V circuits and full all-modulus decoding are in the included proofs.

V uses C4096 verified-pair discovery with b+6 children and beta=21/20.
Its actual integer roots g,j,h,ell,z and first-feasible profile are in
virtual.md Section 1. In particular at EVERY trial R it uses

 u=min(R,max(1,floor(R/3)+2g-floor(j/4)+floor(11h/12))).

Both source acquisition and weighted-attempt caps, decoder, stride,
precision and root counts are recomputed from THIS profile. The physical
interpreter preserves the entire resulting instruction stream, source
sequence and outcome law. Every record, instruction-generation cursor,
return context and owner field is stored in the bank, except the explicitly
bounded short physical control and O(n)-bit input/output/staging.
No uncounted physical classical recursion stack or address map is allowed.

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

Zero-width tree levels have r_i=1 and return their one child without a
combiner. This rule is part of V and is retained. On positive levels the
pending count is B+5m_active+1<=6n+1; labels are not exponentially stored.
Original coherent-register handles are pooled independently of classical
record slots. Ownership/reference metadata is always virtual bank data.

## 2. Explicit fixed capacities, including padding and metadata

Set t=n+2, A=32t, W=2^64 t^2, H=2^24 t. Reserve seven virtual-classical
regions of W bits each, at bases jW for j=0,...,6:

 0 input, parameters, profile, precision, finite constants and cap values;
 1 pending phase labels and their register-handle records;
 2 frames, saved counters, return contexts and pool ownership;
 3 current subset residues, found strings, sort/verification/search state;
 4 source extraction, exact modular arithmetic and common bit scratch;
 5 decoder frequencies, basis/outcomes, candidate/score/CRT scratch;
 6 instruction generation, field locators and allocator metadata.

Every pool has fixed padded subranges and row/field offsets. A scan or bitmap
chooses a free object slot; the bitmap, cursor and handles live in its region.
Assign the subranges in the listed order by prefix sums of the capacities
below; unused remainder is retained and counted, not silently dropped.
There is no exponentially sparse address or unbounded instruction history.
The maximum bank index is Bbank=7W-1 on every history.

Here are conservative analytic capacities, valid independently of success.
For n>=256 the ordinary profile search gives R<=ceil(n/2), mstar<=R,
u is the exact clipped QLOG threshold in Section 0, with1<=u<=R,
and q0=(2u+6)2^(R-u). Since2u+6<=4*2^u for every integeru>=1,
q0<=4*2^R and consequently log2q0<=n+16. The g/j/h/ell/z root arithmetic uses O(logn)-bit fields in the same
counted parameter/scratch regions. Intermediate selected fixed-power words
have at most32L+32 bits, below A=32(n+2) for n>=256. A fixed number of
additional A-bit fields and at most16A scratch bits fit the existing
256A^2 schoolbook collection; no new address range or uncounted map.
The odd multiplier parameter nq=2^(h-1)q0 has log2 nq<=2n+32,
and V's exact K=2^13(ceil(log2 nq)+ceil(log2 n)+30) is below 2^18 t.
Each physical scale j*stride is at most n: this follows from the minimal
stage J in V, including J=0. Thus every signed label, frequency, dyadic
center, cap/precision value and long counter fits A bits. For example
labels have at most n+ceil(log2 q0)+2 bits; Qcap and Wcap add only fixed
constants and O(log n) bits to R and the root/stage count logarithms.
The generous A covers the finite branch too.

Use 16t pending-label/object slots, each with at most 64A bits for its
label, ownership and handles. At most 6n+1 phase outputs are pending; extra
staging/current objects fit the remaining constant slack. Use t+1 stack
frames of 256A bits each; r_i pending handles are stored with the pending
objects, so no independent r_i-by-n array is copied into every frame.
The public profile has at most t entries with fixed-size A-bit fields.
All these pools require less than 2^24 t^2 bits each.

A current found list has at most 4096 strings of length k<=2R+6<=2t.
A fixed number of copies for sorting, verification and projection, along
with its at-most-k subset constants, fit 2^32 t^2 bits. Only the currently
executing combiner has these lists; an ancestor is not running discovery
while its fresh children are being made. Classical residue arithmetic uses
A-bit strings and at most 256A^2 bits of reusable schoolbook scratch.
Source extraction has O(n) outcome counters, each below A bits, and the
finite trigonometric table has 4096 fixed-size entries. These plus a fixed
number of source/CRT/addition records fit 2^40 t^2 bits per such subfamily.

The decoder retains at most K<=2^18 t records at its current stage. Each
record can have 64A bits for W, the public frequency or scale, basis,
outcome and padding; the entire record pool is below 2^29 t^2 bits.
The streamed candidate, score, rational center, CRT and exact arithmetic
scratch fit another 2^40 t^2 bits. No array of all grid candidates exists.
Source and decoder stages release their current records before a new stage.
For n<256 V's exhaustive testing needs only a fixed number of A-bit fields
and O(n) working data; it fits these same pools.

Reserve H virtual-coherent slots. V has at most 6n+1 pending phase qubits.
Its one active source or query/combiner uses ripple adders, reusable carry
chains, pattern equality flags and Toffoli chains on O(n) wires. Even
retaining a separate flag for every one of the 4096 found strings, and
fixed copies of registers, fewer than 2^20 t slots suffice by these explicit
primitive templates; H leaves a factor-16 slack. The finite branch is
covered as well. A bitmap and an ordered list of these H slot IDs take
O(H log(H+2)) bits, below 2^40 t^2. Store them and every locator/cursor in
region 6. Stream only one known handle into physical control per gate.
No n-entry physical classical map or coherent bank address is present.

Each listed subfamily and its constant number of copies fits far below
W=2^64 t^2. These capacities include metadata, padding, source-moving
scratch records and cleanup cursors. Thus the maximum allocated backing
range is an a-priori polynomial, not a bound on observed occupancy only.

## 3. Counted physical wires, READ/WRITE and exact source calls

Represent virtual classical bit i at physical wire 2i and virtual coherent
slot j at physical wire 2j+1. Reserve the WHOLE paired prefix through
2max(7W,H)+3, including every unused even/odd cell and padding, initially
in |0>. Its size is O(n^2). This fixed prefix is the physical allocation;
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

## 5. All physical resources and exact selected bounds

The physical classical input N and output s require O(n) bits. A fixed
number of A-bit staging operands, a finite controller and O(log n)-bit
addresses use O(n) more. Long loop counters, return states, tables,
measurements, labels, locators and allocator metadata reside in counted
basis-state bank records. There is no duplicate physical classical stack.
Thus S_C=O(n), including initialization and cleanup.

The entire fixed paired prefix has O(7W+H)=O(n^2) qubits. This counts every
unused padded cell, all basis-state storage, coherent slots, ownership and
metadata. The n+1 source temporary wires fit the same asymptotic bound.
Consequently S_Q=O(n^2). Address charges use this TOTAL physical allocated
storage, not merely the O(n) virtual phase qubits. The fixed large layout
constants make no practical hardware-size or runtime claim.

All additional work is charged separately. The finite bit interpreter's
record locators, READ/WRITE measurements, reset, source SWAPs and bookkeeping
need a fixed polynomial amount of bit/gate work per V primitive. Even
charging full polynomial-bank scans for accesses and a scan per cell for
initialization/cleanup gives a fixed polynomial bound. Its exact exponent
is irrelevant only because the proof below pays it with a strict margin;
it is not silently dropped from a tight time statement. On every branch,

 T_physical <= poly(n) [T_V+(7W+H)^2+n^2].

The nominal guards in V retain their original positions and values.
Simulation work outside them is included in this displayed ledger, rather
than called free because it does not increment an old virtual counter.
V's primitive count is bounded by its original branchwise charged work.

Write Hlog=sqrt(n)L^(-1/2)log2 L, distinct from physical coherent-slot
capacity H. The COMPLETE stronger intermediate estimate in virtual.md
Sections 3 and 5, before selecting its final supported representative, is

 log2 T_V <= (3/4)F+(3/4)G-(3/32)J+Hlog+O(L+log2 L).

A fixed polynomial interpreter overhead changes only the O(L) term.
The polynomial setup and cleanup are smaller than the same leading
stretched exponential eventually. Since Hlog/J=(log2 L)L^(-1/16)->0
and L/J->0, the COMBINED Hlog and logarithm of ALL virtual/physical
polynomial fees are eventually at most J/96. Therefore, using
3/32-1/96=1/12, the exact supported physical bound is

 T_physical=O(2^((3/4)F+(3/4)G-J/12)).

This argument uses the stronger intermediate ledger, not multiplication
of V's final exact supported envelope by a polynomial followed by its
unjustified removal. Every fixed finite exception executes the same
capped program and finite padded interpreter, enlarging only an outside
absolute constant.

One and only one original source acquisition occurs per V acquisition.
Bank zeros, READ, WRITE, SWAP and cleanup require no DCP copies. The CQ
simulation invariant transfers the full source-request distribution,
including rejected labels and all aborts. Thus V's exact literal cap and
its proof transfer the supported Q=O(2^(F/2-3G/2+3J/16)) unchanged.
The same invariant transfers its unconditional full-secret success bound.

Both exponential logarithms have positive leading multiples of F; G,J=o(F).
Thus their exact growth indices are 1/2. Physical polynomial spaces have
index zero. These are the five claims for ONE physical interpreter running
ONE fixed integer profile. No virtual memory column replaces a physical
memory bound. The family appendix describes other VIRTUAL programs;
virtual.md Section 1 is the sole selected V rule here.

This is complementary to V: classical storage decreases from quadratic
to linear, and quantum storage increases from linear to quadratic.
It does not dominate V. Compared with the published SECOND-SCALE-BANK
representatives with the same physical spaces and canonical clean model,
the selected time ratio is 2^(-J/24) and source ratio 2^(-5J/16), exactly
as in the virtual comparison. This compares published guarantees, not
lower bounds on earlier actual costs or finite elapsed timings.

## 6. Fractional error tolerance

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

The guaranteed fraction is zero for every N and s, jointly with all
physical resource bounds and unconditional success at least 1-2^-8.
No robustness under a model sensitive to extra measurement outcomes is
claimed. No positive corruption tolerance or impossibility is asserted.
