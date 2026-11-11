# SPTS-JM-BANK: a directly addressed measured bank at exact one-third noise

For every N>=2, s in Z/NZ and n=ceil(log2N), one uniform physical algorithm
recovers the ENTIRE s with unconditional success strictly greater than11/16.
Its simultaneous EVERY-BRANCH resources, including all failed work, are

 T=O(2^((1/2)n)n(log2n)^6), SC=O(n), SQ=O(n^2),
 Q=3*2^40(n+32) EXACTLY, epsilon(n)=1/3.                     (0.1)

The four growth indices are1,0,0,0. The logarithmic envelope is for n>=2;
the same finite n=1 program has bounded absolute costs. This is a new physical
storage implementation of the full selected virtual program, with separately
paid overhead. Neither the selector nor measured-bank simulation is claimed
as a new generic algorithm. In particular the old log-cubed time is NOT asserted
for this interpreter.

## 0. Complete sources and the actual change

joint-source.md is the complete SPTS-JM proof of submission
06e46478-3922-41fd-b7b6-8eeaaafeb3f1, full SHA-256
f912b269b63e66803912eed6d517ca795731d5439a6616553493d7eba98e8d7f.
Its complete included mathematical members are copied unchanged as
spts-source.md (SHA-256373939d8a0439acd480aad17f85ab9067d474f995a4c720f43af6a2f42bf409e)
and sources/RQ-SPLIT-proof.md
(SHA-2562952a6f52b94dfa9d0e03471b9e7611f185db198dbc9274639dbc03ce7d1ca80).
Together they fully specify the virtual program V selected here, all integer
parameters, finite branches, phase arithmetic, caps and its fixed-joint-state
success theorem. Original adaptive ModelM passages in the older copied members
remain historical scope; ONLY joint-source.md's replacement fixed-bank proof
is selected for current input statistics. No prior review is a proof premise.

bank-source.md is the complete main proof of PSG4-LOGLOG-ENDPOINT-BANK,
115e4fdb-4fcb-45ab-9511-170aafb2fa4b, SHA-256
7542da9ac969a686a72ed4780886b0eb115c92f6d2fd1f21f90b394ad104333d.
We use its Sections3-5 measured basis-bank READ/WRITE method, paired physical
layout, correlated-CQ invariant, one-for-one source moves and output-first
cleanup. Its virtual sieve, allocation parameters and old subexponential
margin are NOT used. The current direct-address polylogarithmic interpreter
and fixed-joint-input invariant are proved below, rather than importing that
source's deliberately loose polynomial interpreter bound or clean-only theorem.
Its historical LLV-GBANK300C, PSG21 and PSG2-QSTORE credits remain acknowledged.

SPTS-JM's actual SPTS1/RQ/PCT and carried historical credits remain in its full
included proof. This uses the complete two immediate sources for these selected
features; no additional ancestor feature outside them is separately imported.
Original algorithms and methods retain their authorship. Historical file pointers,
reviewer remarks and diagnostic results in the source proofs are not current
executable promises, evidence premises or substitutes for any argument below.

## 1. Exact fixed original joint-state model and virtual program

The fifth structured declaration uses EXACTLY this error-model text:

"Among the Q acquired copies, an adversary fixes a set B of at most floor(epsilon(n) Q) malformed positions, possibly depending on N and s. The joint state is arbitrary subject to its reduced state on all other positions being exactly rho_s^{tensor (Q-|B|)}. Malformed systems may be correlated or entangled with each other and with other systems subject to that marginal promise. No source control, purification access, or preparation inverse is supplied."

As in joint-source.md Section1, the entire original bank is fixed BEFORE
passive release in its original order. Unread source-held registers are excluded
from accessible workspace by the challenge rule. They cannot be replaced or
acted on in response to an outcome. Conditional changes in unread states due
to measurement of a delivered register are allowed. No conditional freshness,
purification access, independent bad state or source preparation inverse is
assumed. Mixtures of fixed-B components are included. An inaccessible reference
may purify the original bank. The model is not an interactive adversary that
can react to extra interpreter outcomes.

Select EXACTLY V=the full SPTS-JM physical algorithm as a VIRTUAL algorithm.
It acquires all Q=3*2^40(n+32) original registers; uses the same collective
EXTRACT h,F,J, exact decoding, row X and reset; chooses the same private late
k-subset with the same capped sampler; measures those shadow rows in fresh
axes; executes the same sampled-pivot, frozen-prefix/token-limited search and
full-record champion, or the exact same bounded n<64 fallback; and executes
the same untouched-bank gradient/trit endpoint. Every table, tie rule, sketch,
cap, arithmetic precision, random coin, abort and output remains V's. In
particular no additional source bank or new error event is introduced.

Write L=max(1,ceil(log2 n)). The complete source ledger proves, uniformly in
all input states and histories, total charged virtual time

 T_V <= C 2^(n/2)n L^3,
 virtual classical allocation B0(n)<=C0(n+32)^2,
 virtual coherent allocation H0(n)<=C1(n+32).                (1.1)

All constants are absolute. The program includes finite initialization and
complete cleanup. These are THEOREMS established by the included mathematics,
not assertions taken from a previous acceptance. Section7 of joint-source.md,
Section8 of spts-source.md and Section9 of the included RQ proof give the
explicit allocation families and deterministic work ledger. The new physical
bounds do not identify a virtual classical bit with an unknown quantum state.

## 2. Fixed bit pools, physical layout and finite control

Use V's stated array and field dimensions and its fixed capped stacks to give
every virtual classical field a fixed padded bit range. Concatenate in this
order: input/parameters and finite constants; source extraction and common
arithmetic scratch; decoded labels and shadow packed words; shuffle array and
measurement fields; all representatives, sketches, thresholds and exact pivot
words; bounded counters, recursion frames, return contexts, allocator fields
and instruction-generation scratch. Reuse common scratch at the release points
specified by V. Assign offsets by prefix sums of these fixed capacities. This
is a fixed static layout computable from n, not a directory growing with time.
All fields, inactive cells, object handles and padding count.

More explicitly the large families are Q n-bit labels; k(n+p) packed source
bits with p=30+ceil(log2n); O(Q log Q) permutation/subset bits; at most Hmax
n-bit representatives and Hmax ell indices/threshold words, with Hmax=O(n)
and ell=O(log n); at most Hmax k r_phi bits for any full exact cache retained
by a selected finite procedure, r_phi=26; O(n log n) recursion/descriptor bits;
and the stated reused source/endpoint/ordinary bit-arithmetic pools. The latter
are O(n^2) by the RQ allocation proof, with no table exponential in n. For
n>=64 the sampled implementation can use its smaller per-pivot caches. Reserving
the larger O(n^2) source-family capacities also covers the n<64 procedure. The
fixed exact constants k,Q and every source confidence field are included.
No frame holds a separately expanded circuit or full candidate history.

Let B(n) be the next power of two above the finite sum of these ACTUAL fixed
classical pool capacities, including their metadata, and H(n) the next power
of two above V's complete coherent-wire pool. The exact dimensions are given
by the selected algorithms, so this defines computable integers without
instance advice or an unknown asymptotic threshold. Rounding multiplies the
proved allocations by at most two: B=O(n^2), H=O(n). Initialization computes
these layout formulas with ordinary charged bit arithmetic. Its polynomial
cost is separately absorbed below. V's original n<64 branch is retained,
not replaced by a clean-only protocol.

Place virtual classical bit i on physical wire 2i, 0<=i<B, and virtual coherent
wire j on physical wire 2j+1, 0<=j<H. Reserve the ENTIRE paired prefix through
2max(B,H)+3, including all unused cells and padding, initialized to zero. One
current source request additionally uses n+1 temporary raw wires. Nothing
requires a physically sparse set of enormous wire indices. The full physical
allocation is O(n^2); all operand address fees use that full allocation.

Define w=ceil(log2(4B+4H+4n+32)). The finite physical kernel keeps only the
input N and final output (O(n) bits), a fixed number of w-bit address/operand
fields, the current finite opcode, and at most O(w^2) reusable schoolbook
layout/staging bits. Since w=O(log(n+2)) and log^2(n+2)=O(n), this is O(n)
physical classical storage. A long V counter, cache, label, call stack, active
virtual scratch word or instruction descriptor lives in the basis bank.
There is no second physical copy of V's classical array, nor a classical
recursive implementation of V_j. Its return context is bank data.

## 3. Explicit directly addressed bit interpreter and its overhead

First expand V's ordinary arithmetic and controller into finite Boolean bit
operations, indexed bit reads/writes, finite branches, elementary Clifford+T
gates, measurements, reset, coins and source calls. Gate generation and all
address-variable operations are part of this expansion, as required by V's
own ledger. There is a fixed finite set of opcodes with a constant number
of operand fields per opcode. A bulk addition, division, loop or compiler
subroutine is a sequence of these bit steps, not a new unit-cost RAM action.
Finite call/return contexts are in the fixed virtual frame pool. The active
opcode and its fixed number of address fields can be decoded in the short
kernel; a return reads its stored frame fields. A known pointer locates the
current virtual frame and its descriptor; no coherent pointer is used.

READ(i): measure known wire2i in the computational basis into a reused staged
classical bit. WRITE(i,b): READ(i), apply X on2i iff its old value differs from
b, then forget staging when no longer needed. A virtual Boolean step reads
its constant number of bits, performs the same finite Boolean operation and
writes the indicated destination. A long word remains in the bank and is
processed one bit step at a time. Fetching an original known gate constant
uses READ on its virtual classical bit. The actual original coherent controls
remain quantum controls on the mapped odd wires. Known virtual gate addresses
j become2j+1; bit data addresses i become2i. No superposition ever addresses
this bank, and no Boolean value is inferred from an unmeasured coherent wire.

Here is a conservative polylogarithmic bound including ACTUAL address
construction and descriptor fetch, without the earlier source's bank scan.
All bank/slot addresses have at most w bits. Decode a virtual instruction's
constant number of w-bit fields by w separate bit reads per field. For each
such bit, form its known physical address by shift/offset and ordinary w-bit
pointer arithmetic. This takes O(w) core bit actions for addition/shift, or
O(w^2) for a fixed-number field/base product; the latter products can instead
be formed ONCE for the whole field before its sequential bit fetch. A full
field fetch therefore takes O(w^2) core actions: O(w^2) for its base/offset
calculation and O(w) times O(w) for each of its w individually addressed
bits, including pointer updates, instruction emission and staging cleanup.
The fixed finite number of fields, opcode/return bookkeeping and original
bit operation use O(w^2) core actions as well. All indexed actions, quantum
gates and descriptor bit reads/writes pay the full address fee O(w).
Consequently one expanded virtual primitive costs at most C2 w^3 charged
physical work, including the kernel's own gate generation and inverse words.

This is deliberately conservative: no amortized virtual descriptor advantage
is used to drop the new field-fetch cost. The kernel uses fixed finite loops
and its bounded staging. It does not recursively invoke a bank interpreter
to implement the kernel's own address arithmetic. All kernels operate on
these short physical classical fields with ordinary bit operations, whose
addresses also pay O(w). Long logical arithmetic remains a sequence of V's
bit steps. Serial fetch of a descriptor of an original generated instruction
can add O(w) bit reads but is already covered by the w-bit field bound above.
No scan of B cells per access, free word-RAM or instruction oracle is used.

For an original quantum gate emit the identical elementary gate on its mapped
odd wires, using the fetched known addresses. A measured original bit is
written to its bank destination. Coins use the same distribution; their
outcomes are written at the same virtual point. Controlled X uses Clifford+T
and WRITE uses only a known conditional X; no approximate gate is added.
For original reset/discard measure, conditionally X to zero and forget the
outcome, exactly trace-out followed by zero preparation even with a reference.
Never release a shared virtual coherent wire before V's last owner does.

At a source call acquire EXACTLY ONE original n+1-qubit raw register on the
temporary wires, then SWAP its qubits into V's designated zeroed odd slots.
Each SWAP is three CNOTs with known addresses. Clear/release the now-zero
temporary wires before the next request. This is O(n w^3) physical work,
within the above factor applied to the original n+1 source work charge.
Moving a register creates no second original sample and assumes no source
inverse, control, supplied purification or ideal reconstruction of a bad row.

Virtual token debits, rejected draws, failures and guards occur at EXACTLY
the original logical points. They cap V's work; they do not pretend to charge
the added physical kernel for free. After the virtual result is known, copy
the entire s to counted physical output FIRST; only then zero/reset and
release every bank cell, coherent slot and staging bit. Init/cleanup can
scan all allocated cells using the same known-address kernel. Their separate
cost is O((B+H+n+1)w^3), as are all fixed metadata/padding operations.

## 4. Full joint-state CQ invariant, including unread sources

At each aligned virtual step the physical joint state, including arbitrary
reference R and the fixed not-yet-delivered raw systems U, has the form

 sum_(c,z) p(c,z) |z><z|_kernel tensor |c><c|_basis-bank
                     tensor rho_(c,z)_(mapped V coherent registers,U,R). (4.1)

Tracing out short copies of V's data in z and relabeling the odd slots gives
EXACTLY V's full joint state with its original classical record c. This is
not a tensor-independence assumption: rho_(c,z) can depend on all records,
and U, bad rows, good rows and R may be entangled. Extra kernel staging
contains only fetched copies/functions of actual virtual classical bits.

Initially the bank is zero, the copied input is classical and the original
joint source state is the selected arbitrary allowed sigma; (4.1) holds.
READ's computational-basis projectors reveal a bit already present in c,
and leave each conditional rho unchanged. A redundant READ creates another
copy of that classical value, which is later forgotten. WRITE updates that
basis value exactly; irreversible overwrites mix the conditional coherent
states just as V's classical forgetting does. Boolean operations, field
fetches and finite branches therefore preserve the invariant. Original
gates/measurements/coins have exactly the same instruments and probabilities
under the same records; original coherent controls are never replaced by
classical outcomes. Physical source SWAP is just a register relabeling of
the original joint state. Discard/reset has the exact channel identity above.
Induction gives (4.1) on every history, without postselecting on a successful
label, search, favourable error pattern or coarse answer.

Unlike the old bank-source theorem, this induction explicitly includes U,R
and applies to the current fixed joint-marginal input. Extra reads cannot
cause the supplier to change an unread register, since the original bank is
fixed and delivery passive. Measurement-induced conditional changes in U
are already represented in rho_(c,z); duplicated reads reveal no new variable
beyond the existing c. Erasing extra staged copies recovers exactly V's
joint channel. No fresh-good conditional-state assertion is introduced.
This would not justify an interactive reacting-supplier model, which is not
the selected model. It also makes no claim for a coherently superposed data
bank: these bank cells encode V's genuinely CLASSICAL bits.

The physical output distribution is consequently exactly V's distribution,
for every fixed B, arbitrary allowed sigma/reference and convex mixture.
The complete joint-source proof of label coupling <=2^-62, late hypergeometric
count event, good-first score concentration, conditional-record selector and
unconditional endpoint binomial comparison applies without changing any of
its constants. It proves full-secret success STRICTLY greater than11/16 at
fraction1/3, including all N, all clean inputs and the finite n<64 fallback.
No original adaptive-freshness proof or earlier acceptance is substituted.

## 5. One algorithm's complete physical joint resource ledger

The physical classical input, final output and bounded O(w^2) kernel staging
occupy O(n) bits, including all unused fields/padding. Every other classical
record of V, allocator, stack, sample label, exact phase word, pivot or
instruction descriptor occupies counted basis-bank quantum cells. Thus
SC=O(n) on every branch. The entire paired prefix is O(B+H)=O(n^2) qubits,
not its smaller currently coherent subset; n+1 raw source wires and all
helper flags add O(n). Therefore SQ=O(n^2) on EVERY branch. The full combined
address width remains O(w)=O(log(n+2)). The source's more economical virtual
SC=O(n^2),SQ=O(n) are only virtual facts, not the actual declared pair.

Each expanded virtual primitive incurs at most C2 w^3 physical charged work.
Their number is at most T_V because every one has at least unit original
charge and all original instruction generation is included. Source moves
are paid as above. The separately charged fixed layout computation and
initialization/cleanup are polynomial; in particular finite prefix-sum,
capacity and address calculations involve only fixed-degree O(log n)-bit
integers and at most O(n^2) allocated cells. They fit O(poly(n)) and can be
absorbed by the exponential envelope. More tightly the actual paired-bank
initialization and final scan cost O((B+H+n+1)w^3). Hence uniformly,

 T_phys <= C3 w^3(T_V+B+H+n+1)+poly(n)
        = O(2^(n/2)n(log2n)^6).                             (5.1)

The last step uses w=O(log(n+2)), V's proved nL^3 charged envelope, and the
fact that every fixed polynomial is O(2^(n/2)n(log2n)^6). A finite exception
changes an absolute constant, not the algorithm or its success promise.
Every nominal cap still executes V's original guard. Physical work after
that cap and on abort cleanup is included in (5.1), with no assumption on
expected hitting time of the actual input or the outcome of a failed stage.
The exact time growth index is1: log2 of this representative is
n/2+log2n+6log2log2n. The three polynomial resource indices are0.

Exactly ONE original register is acquired per V request. Its deterministic
Q=3*2^40(n+32) therefore transfers unchanged on all branches; bank zeros,
extra basis measurements, SWAPs and cleanup are not source copies. Fraction
1/3 and its exact fixed-joint context transfer by equality of full output
channels, jointly with (5.1), SCn and SQn^2 for this SAME implementation.
This is an actual counted storage/implementation tradeoff. It neither
asserts a new maximal tolerance nor infers a frontier comparison across
different models. It uses no free coherent memory lookup, uncontrolled
source primitive, free rotation or discarded logarithmic overhead.
