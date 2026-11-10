# PSG4-SEVENELEVEN-REFINED-BANK: linear classical storage with counted quadratic basis-state storage

## 0. One physical algorithm and joint theorem

For every N>=2 and s in Z/NZ, let n=ceil(log2 N) and L=log2 n. The ONE
physical interpreter below executes the complete virtual program V supplied
in virtual.md and returns the entire s with unconditional probability at
least 1-2^-8. On every branch, including failed tests, discarded copies,
wrong extracted labels, both resource aborts, setup and cleanup, its bounds are

 T=O(2^((11/12)sqrt(nL)+sqrt(n)L^(-3/8))), S_C=O(n), S_Q=O(n^2),
 Q=O(2^((1/3)sqrt(nL)+sqrt(n)L^(-3/8))).

These are uniform Big-O representatives with absolute outside constants.
The finite n=1 prefix is included by the same interpreter and V's finite
branch. The resource indices in T,S_C,S_Q,Q order are 1/2,0,0,1/2.
The guaranteed malformed fraction is exactly the clean-input assertion 0,
under the canonical independent-ideal-copy model in submission.json.
No positive tolerance or impossibility claim is made.

The selected V is the complete PSG4-SEVENELEVEN-REFINED program from this session, with
list cap 4096, b+6 children on positive-width blocks, retry factor 21/20,
seven-elevenths-base first-feasible profile, exact original-copy source/decoder,
and both literal cutoffs. Its full proof is supplied, not an opaque theorem.
Its quadratic classical and linear quantum bounds are VIRTUAL bounds only.
This main specifies the single physical allocation replacing those bounds;
we never combine physical classical memory with V's original quantum memory.

Immediate physical-template source: PSG4-SEVENELEVEN-BANK,
eb96819e-1a15-424b-abe4-883b34255762, published commit
9d3f9d06b0691ae2dd36a8511bed76408c77d1ba. Its exact seven fixed regions,
paired full prefix, typed pools, READ/WRITE, CQ and source-transfer method
are retained. This candidate changes only the analytical lower-order term
and supplies the complete refined virtual proof. The physical operations,
source-request sequence, integer profile and allocation are unchanged.
The new capacity certificate establishes G=sqrt(n)L^(-3/8), leaving the
strict positive internal gap required for all polynomial bank overhead.
The refined virtual source is33a7495f-9510-45b2-b1e4-2b5f82f05b3c.
Verified public artifact identities accompany the note and dependency
declaration before upload; no prior verdict is a mathematical premise.

The generic measured-bank method is credited prior work. The direct
physical source credits LLV-GBANK300C,
ae91a0c4-f38a-47d0-b6c1-d3ed0a461b6d, commit
45584c8219d304381a05dee3ae33476096d0827a, including its uniform bit
interpreter, fixed ownership, correlated-CQ invariant, source moves and
separate paid overhead. Its historical PSG21 and GordoAR PSG2-QSTORE
credits are retained. Neither its LLV virtual sieve nor its cubic/log
backing layout is imported. No generic simulation novelty, priority,
ancestry certification or predecessor-verdict premise is claimed.
Material identifiers for the exact virtual source accompany the public
note/dependency declaration after publication; its full proof is included.

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
u=floor(7R/11), q0=(2u+6)2^(R-u). Consequently log2 q0<=n+16.
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

## 5. All physical resources and exact supported envelopes

The physical classical input N and final output require O(n) bits. A fixed
number of A-bit staged operands, the fixed controller, and O(log n)-bit
address/scan fields add O(n). Every large loop, call frame, table, label,
instruction descriptor, allocator field and measurement record is virtual
bank data. No physical duplicate store or classical recursion stack exists.
Thus S_C=O(n) on every branch, including setup, output and cleanup.

The ENTIRE paired prefix is O(7W+H)=O(n^2) qubits, including unused padding,
all basis storage and coherent slots. Source temporary wires add only n+1.
The address charge uses this full allocated total, not just live virtual
coherent registers. Therefore physical S_Q=O(n^2), jointly with S_C=O(n).
The fixed enormous layout constants make no practical finite-size claim.

All interpreter work is counted. Dense field-location arithmetic, bit
emulation, measurement, reset, virtual-wire handles and source SWAPs require
at most polynomial work per charged virtual primitive; even full scans
and a full scan per initialization/cleanup cell give a polynomial upper
bound. Every array bound is fixed before sampling. The number of virtual
primitives on every branch is bounded by V's branchwise T_V, including its
nominal-attempt and acquisition cutoff work. Added simulation work is not
hidden behind those old nominal guards: it is separately charged, giving

    T_physical <= poly(n) [T_V + (7W+H)^2 + n^2].

This includes every attempt and abort, not only successful virtual runs.
Write F=sqrt(nL) and G=sqrt(n)L^(-3/8), for n>=2. V's stricter
internal theorem is T_V<=poly(n)2^R, with

    R<=ceil((11/12)F+(1/2)G) eventually.

The complete polynomial simulation/setup/cleanup overhead contributes
O(log n) to its exponential logarithm. The fixed positive lower-order
gap from (1/2)G to the declared G absorbs that ENTIRE overhead because
log n=o(G). Consequently the exact full physical time bound is
O(2^((11/12)F+G)). This does not multiply a final pure bound and silently
drop its polynomial; it uses the explicitly stronger internal height
bound. Absolute constants cover the finite exceptional range, with the
same executable interpreter and integer profile search at every length.

There is exactly one original DCP acquisition per virtual acquisition, with
identical complete source-request sequence. Bank zeros, padding and reset
are counted time/qubits but are not source copies. V's full literal cap
therefore proves the same exact sample envelope
O(2^((1/3)sqrt(nL)+sqrt(n)L^(-3/8))), including every discarded copy and abort.
Its success and clean-error proof transfer by the exact CQ invariant above.

For B(n)=2^(aF+G) with either fixed positive rational coefficient
11/12 or 1/3, G=o(F). Thus log2log2 B=log2 F+O(1), whose ratio
to log2n tends to 1/2. Polynomial n and n^2 have index zero. All four
envelopes, indices and fraction 0 concern this same physical configuration,
not a mixture of virtual and physical columns. The complete general-family
appendix in virtual.md is virtual evidence; the selected physical row
fixes the one seven-elevenths configuration throughout.

This is a space trade-off: physical classical storage is smaller than V's
quadratic declaration, and physical quantum storage is larger than V's
linear declaration. Neither configuration dominates the other. No generic
simulation novelty, global optimum, practical timing, or cube-root-time
claim is made. The separate complete virtual evidence is scoped only to V.
