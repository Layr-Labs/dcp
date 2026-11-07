# RLS4L-FIXEDBANK: measurement-free delivery followed by counted fixed basis records

## 0. One physical algorithm and joint robust theorem

For every N>=2,s in Z/NZ,n=ceil(log2N), the ONE physical implementation
below executes COMPLETE reference RLS-4L P in virtual.md. It outputs the
WHOLE secret with unconditional probability>=9/10 for EVERY adversary
of the EXACT adaptive malformed-copy model in claim4, tolerating
 epsilon(n)=1/(64n^4).
On EVERY execution branch, including any malformed/entangled contents,
all failures, rejections, unused blocks, initialization and cleanup,
 T=O(n^132*2^(n/(4log2n))),
 S_C=O(n) ordinary classical bits,
 S_Q=O(n^14*(log2n)*2^(n/(4log2n))) allocated qubits,
 Q=O(n^13*(log2n)*2^(n/(4log2n))) acquired source copies.
Constants are absolute, independent of N,s,adversary and outcomes.
The asymptotic expressions are for n>=2; the actual n=1 algorithm is
covered by the finite branch below and fixed absolute constants.
Indices are[1,0,1,1]; only time scores[1]. No clean-input time-frontier
or cube-root result is claimed. This trades polynomial interpreter
work for linear ordinary classical space and retains the SOURCE's
quantum/copy envelopes and positive adaptive tolerance.

The delivery phase has EXACTLY NO MEASUREMENT AND NO FAIR BIT before
LAST source delivery. In particular even deterministic bank READs,
zero-verification tests and allocator measurements are forbidden then.
This preserves the source's no-information premise literally. After
last delivery all large logical classical arrays become fully counted
basis qubits with known classical addresses. All original quantum
registers use fixed original-copy coordinates, not an exponential pool
scan or quantum-addressed memory. Whole inactive padding also counts.

## 1. Complete actual sources and proof scope

Actual RLS-4L is50862886-4e61-4f01-a1fc-f4d1595a7e3b,commit
267a36450be60006ab593b3e4f90a3b444a5db15. Its COMPLETE52905-byte proof,
SHA256c529a75bca94a4c82dec43faa17005b410d40048e53c33faaeeff976a7ef114f,
is reproduced BYTE-EXACTLY after the virtual-only scope marker. Every
Clifford+T primitive, source identity, exact splice/twirl, label-reading
lemma, acquire-first uniform permutation, robust sieve counting and
conditional uniformity, corruption concentration, vote/test, small-input
and unconditional success proof is supplied. Those original ordinary
classical/quantum/work ledgers and references to submission.json mean
VIRTUAL P and its original declaration, not this physical allocation.
This main proves the changed physical resource ledger and adaptive
supplier transfer. No public verdict or graph edge is a theorem premise.

The full source proof, raw manifest and public note were read and all
five official proof-evidence bindings match. Declaration/show/history
were read:5pending references to RLS,RLS3L,adaptive model,SLS,RLS2L,
no applied edge/cursor. Pending is neither verified ancestry nor false.
All original author credits remain in full, including kshitij-hash's
RLS/SLS/OMX/tolerance line and Kuperberg. Historical first-person text
means its original authors. This is a storage completion, not an
independent invention of any source sieve or robustness method.

The distinct directly consulted measured-bank method is corrected
fbb8f36c-3904-4bf0-9ddf-e9f5d83657ae,commit
100a8e307fd90c489c4d90717613869fed576b3b, main SHA256
08608c19bf8d7ba42b50cf01f86662bc4e38ae0de63a2825ed4f86c8f10ca7d0.
It supplies fixed complete spans/direct measured-wire operations,
arbitrary-reference correlated-CQ and irreversible-forgetting/source
channels, online finite bit code and whole paired-prefix accounting.
Its unrelated quarter-square-root virtual algorithm and unused
historical comparison are not selected. PSG21/PSG2-QSTORE credits
remain. No exponential-pool allocator or tag/overflow construction is
needed here. Exact both-endpoint citations and actual dependencies are
required before upload; no source verdict certifies these new claims.

The ONE external premise in P is the without-replacement Hoeffding
bound (virtual LemmaH). It was checked in the ORIGINAL Hoeffding1963,
JASA58,Section6,Theorem4,printed28-29, primary copy
https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf.
For a fixed finite population, the sum sampled without replacement has
no larger expectation of any convex function than an equal-size
independent with-replacement sum. Apply the result to exp(hx), then
the standard bounded-variable exponential estimate of Theorem1 and
Markov to obtain Pr[X>=(mu+t)m]<=exp(-2mt^2). This directly supplies
the stated hypergeometric bound. P proves the other martingale MGF
bound itself. No unverified paper claim or graph supplies a premise.

## 2. Exactly selected source, fixed parameters and finite branch

For n>=4096 use EXACT P's literal integer profile:
 R=4*bitlength(n-1), b=ceil((n-1)/R), M=R*2^(b+2R+6),
 G=2^(R+9), k=64*bitlength(100G), Q0=G*(n*M+k),
 r1=200*bitlength(1600*(n+1)*Q0),kappa=2*bitlength(Q0)+10.
Every source guess, slot/rank partition, stage boundary l_m, width b_m,
exact grid, label reader F_t, cutoff, tie, vote, test and early-output
rule is unchanged. Q0 is acquired ENTIRELY before the first measurement;
unused blocks are still acquired and counted even on an early output.
At most R stages per round, G guesses and n rounds per guess remain.
Source coin/measurement instruments and every original discard/reset
are unchanged at aligned logical steps.

For n<4096 execute P's COMPLETE robust exhaustive branch, NOT a clean
shift tester: Ks=2^20,Q0=N*Ks,kappa_s=2*bitlength(Q0)+10. Acquire ALL
Q0 copies with no measurement before LAST delivery. Then draw keys,
abort on ties, sort to uniform permutation, allocate Ks ranked copies
per candidate, test each candidate with the original13/16 threshold,
return the first passing candidate or0. All finite-branch adversarial
success/concentration arguments in virtual7.10 are supplied. Its fixed
finite domain N<=2^4095 changes only absolute outside constants in all
four envelopes, uniformly over s, adversary and every outcome branch.
No validity or runtime threshold is added.

Use fixed bottom-up stable merge sort on(key,index) for the initial
permutation; P's counting sort on low-label stage keys is stable. Tie
orders always use LOGICAL original row/copy indices. No physical wire
identity determines a sort key or logical branch. The chosen fixed
ripple/schoolbook/bit-serial implementation streams primitive gate
words and does not store a growing circuit or measurement transcript.

## 3. Fixed full basis spans and original-copy quantum coordinates

Let
 B=2^30*n*(Q0+(n+2)^20),
 H=(n+1)*Q0+2^20*(n+2)^4,
 D=B+H+2^20*(n+2)^4.
B is the COMPLETE number of reserved logical basis cells, not live
occupancy. H includes all original held copies and a conservative
polynomial original-primitive scratch pool. D includes both arenas'
metadata/padding and additional finite-generator fields. Overlap-free
role offsets define all arrays in B. One can use fewer than2^10 fixed
families with field width at most2^10*n bits:
 - constant-many Q0-row key/index input/output merge-sort buffers,
   rank-to-original-copy permutation and temporary index arrays;
 - constant-many M-row round label/copy-index input/output buffers;
 - one2^b-row counting-sort counter/offset buffer and fixed work buffer;
 - polynomial parameter/stage/F_t counter/x_i, grid/candidate/vote,
   arithmetic/generator and call/frame records.
For the small branch use Q0-row keys/permutation/test counters.
The source gives M*n<Q0,2^b<Q0 and every key/index/label field O(n)
on the main branch. All actual array families and constant numbers of
fields fit the2^30*n*Q0 term by explicit role reuse; scalar helpers fit
the generous polynomial2^30*n*(n+2)^20 term. No new owner is allocated
per entry, bit, operation or source copy. Parameter tables and logical
return/control frames are banked; source's O(n^2) logical scalar
workspace is not silently retained classically. For concreteness reserve1024 families, each with Rowcap=Q0+(n+2)^20
rows and Wrow=1024*n bit fields. Rolef,rowj,bitu has fixed basis index
 ((f*Rowcap+j)*Wrow+u),0<=f<1024,0<=j<Rowcap,0<=u<Wrow.
Their total2^20*n*Rowcap is BELOW B; all remaining B padding also
counts. Actual source row/field domains retain their original bounds;
clears per round visit only actual M/2^b rows, not all Rowcap.
All unused owner/row/field and raw metadata padding count, even before
any cell is written.

Original copyj,bitf (0<=j<Q0,0<=f<=n) has logical slot
 q=(n+1)*j+f in the first(n+1)Q0 positions of H. Every retained sieve
qubit is the first qubit of one original copy; its handle is its
original-copy index. LEAF's data subregister is the remaining known
bits of that copy; partial releases keep the same coordinate names.
A5 transfers the retained control's handle and releases only the dead
partner. No state is cloned, aliases are not silently dropped, and a
still-live original wire is never reset. Passing a record transfers
its index handle. Primitive A1/A2/F_t uses only polynomial ancillary
registers in fixed roles after the source slots; it emits finite gate
lists online and returns/reinitializes scratch as P specifies. These
primitives have no recursive quantum-register expansion. An ancillary
role can be found by scanning polynomial metadata if necessary.
When original A2 finishes by RELABELLING its output wires, implement
that logical relabelling by O(n) known-address SWAPs returning the
result (including a shared control when applicable) to its designated
fixed original-copy/scratch coordinates. A2 has uncomputed its old
input to zero; these SWAPs return the auxiliary result positions to
product zero while preserving the complete unknown logical state
and references. Reuse them only afterward. Thus fixed copy coordinates
remain true at primitive boundaries even on arbitrary malformed input;
no growing per-copy wire-map table or uncounted dynamic pool is needed.
All intermediate original and ancillary slots are in H, and these
extra O(n) gates per original primitive are charged in Section8.
There is NO H-wide scan per gate, label, allocation, round, vote or
source request. Original-copy addresses are computed directly from
j,f, not looked up by coherent addresses. Original P does not call
an oracle on a superposed bank address.

Basis cellj uses physical wire2j. Original slotq uses odd wire
2(q+1)+1; odd1 is reserved for a reused fresh fair-bit qubit AFTER
last source delivery. Let h be the least power of2 at leastmax(D,H+1,2).
Allocate the WHOLE prefix0..2h-1 as FRESH ZERO qubits. The source
receiving temporary uses at mostn+1 additional wires. The whole prefix,
all inactive rows, unused headers, source slots, basis fields, fair
slot, original scratch and unused paired padding count in S_Q.
All physical address words have O(n) bits:
 log2(Q0+B+H+2)=O(n/log2n+log2n)=O(n) on the main branch,
and O(n+20) on the finite branch. Size arithmetic uses constant-many
such words. Input/output coexist with those O(n)-bit words.

## 4. A literally measurement-free delivery phase

Compute the public Q0,B,H,D,h and all fixed offsets needed for delivery
by exact integer bit arithmetic on constant-many O(n)-bit classical
operands. Powers2^x are formed by their binary representation; their
bit length is O(n), not their numerical value. R,G,M,Q0 and grid-size
words also have O(n) bits. For the small branch Q0=N*2^20 has O(n+20)
bits. No exponential ordinary array or long ordinary stack is created.
The finite program uses streamed loops, with j and elementary carry/
operand fields only. Polynomial parameter arrays are filled into the
basis bank AFTER the last delivery, rather than read during this phase.

Allocate the full prefix in fresh|0> states without measurements,
zero-verification reads, reset tests or fair bits. For j=0..Q0-1,
request ONE ordinary source copy into n+1 receiving wires and SWAP
its bits into the fixed zero source slots for copyj. Every SWAP is
three CNOTs with counted known addresses. The receiving wires are now
EXACT product zeros, independently of the delivered state and E,
because the target slots were fresh product zeros. Discard those
known zeros WITHOUT measuring them, or keep/reuse that zero receiving
scratch; no reset outcome is required or generated. This is just a
relabelled ordinary delivery channel, not an inverse, reflection,
coherent control or purification of the source. At mostn+1 receiving
wires coexist. Advancing j and slot offsets uses ordinary exact bit
operations and produces no quantum measurement outcome.

Thus the ENTIRE physical measurement-outcome history before copyj is
empty, for EVERY j, even for arbitrarily entangled malformed copies.
The adversary may know the full physical program, N,s and public size
words but obtains no measurement or fair-bit information. Its delivery
choices are functions only of its own private outcomes as in virtual
LemmaN. Every clean delivery is fresh independent rho_s by the stated
model; a malformed delivery's possibly E-entangled state is simply
SWAPped into the corresponding held slot. Swaps do not act on E or
alter the logical tensor state and reveal nothing. The fixed source
copy count and allowed malformed budget are exactly P's Q0 and
floor(Q0/(64n^4)), on every branch. At LAST delivery the logical state
of all Q0 copies and E is exactly P's, with independent zero helper
padding. Source no-information and uniform-rank assumptions therefore
apply to this physical algorithm, not to a changed adversary model.

Do NOT replace the preceding proof by a claim that deterministic bank
measurements would be harmless. None are performed. This phase is
part of the one fixed implementation at every N, including n<4096.
Only after last delivery may READ/WRITE, fresh fair bits, labels,
permutation keys, source resets, or any logical measurement occur.

## 5. Direct measured storage, reuse and exact scope costs

AFTER LAST delivery, READ(j) measures known even wire2j in Z into one
reusable ordinary bit. WRITE(j,b) reads oldz, applies X iff z differs
fromb, then forgets z. Fixed Boolean primitives read/stage constant-many
bits and write/erase their outputs. Logical words and descriptors are
streamed bit loops; an O(n)-bit field is not a unit-cost fetch. Gate
addresses are CLASSICAL known indices, never superposed bank queries.
Generate the SAME original gate on each corresponding source/scratch
coordinate; preserve logical row/tuple order. Coins use fresh zero,H,
Z measurement only after last delivery, with the same logical law.
All original qubit release/reset instruments act only on released
coordinates, preserving all other held copies and live registers.

The raw arrays use fixed role offsets and reused buffer names; no tag,
owner counter, lifetime-growing address or full quantum pool directory
is needed. Initial BIG zeroing is ONCE. Initial key/index buffers and
rank table receive their original full writes/sort moves. A bottom-up
merge-sort pass uses the two fixed Q0-row buffers, swapped in role,
not a new array per comparison or recursive call. At most O(logQ0)
passes occur; source's full sorting work is retained.

Round record buffers have M rows, overwritten or explicitly cleared
when a new round begins; subsequent stable counting-sort stages use
reused input/output record buffers. Each counter/offset range has at
most2^b rows, initialized as needed at a stage. Fixed F_t and scalar
scratch may be cleared by polynomial scans while preserving live
record/copy state. No Q0-row or B-wide clear is performed per LEAF,
gate or bit, and no Q0-row clear is performed per guess or round.
A stage clears only its M/2^b families. These are concrete allocation
rules for THIS static-array algorithm, not an arbitrary malloc trace.

There are at mostG*n*R round-stages. Since G*n*M<=Q0 and2^b<=M,
all their full clear/write row events cost at most O(R*Q0) rows, or
O(n^2*Q0) bit events for O(n)-bit fields. Fixed key/rank Q0-row buffers
have at mostO(logQ0) full passes, O(n^2*Q0) bit events. Add polynomial
scalar fields and primitive scratch separately. Conservative extra
nonpolynomial scope/metadata events are O(n^4*(Q0+1)); no Q0^2 term
or exponential clear per original operation is hidden. Initial and
output-first final cleanup touch the COMPLETE fixed prefix once each.
Copies unused on early halt or ties are measured/released as P requires;
all were already acquired and remain counted. Source copy count stays
exactly Q0. Padding and known-zero source SWAPs are gates/storage,
not additional DCP samples.

## 6. Full correlated-CQ and adaptive-source correctness

At the end of delivery, fixed slot relabelling identifies every source
copy with P's, including arbitrary correlations of malformed copies
with E. From then on the adversary has no access and there are NO
more source deliveries, so extra helper outcomes cannot guide any
future corruption. At aligned logical steps the physical state is
 sum_z p_z |z><z|_basis-records tensor rho_z_(mappedPquantum,E,R),
with any arbitrary referenceR. No product assumption on records and
rho_z is made. Let pi retain P's decoded logical record, original
source/scratch coordinates and logical control, while MARGINALIZING
all physical-only helper readings, unused fields and forgotten data.
Different physical records with the same logical value contribute
the appropriate mixture of conditional quantum states.

Known-index Z reads are nondestructive on CQ basis records. WRITE and
classical bit code implement exactly P's classical update; overwriting
or erasing mixes old conditional states, as irreversible forgetting
requires. Fresh keys/coins, fixed source gates, twirls and forgetting,
A5, label readout, stable grouping, votes, tests and source resets have
the SAME original instruments and logical branches. Reset/discard
preserves arbitrary reference marginals by the same trace-out and
fresh-zero channel. Slot-index handles only rename known wires and
never create a coherent memory oracle or duplicate an unknown state.
Thus pi composed with each physical channel equals P's logical channel
composed with pi, on arbitrary conditional rho_z,E,R, including wrong
labels and arbitrary malformed contents. At termination output is
streamed FIRST, then the full prefix is cleaned/released.

This channel statement does NOT assert any source latent-label or
robust-sieve conditional independence given the enlarged helper
transcript. In particular P's twirl variable zeta and ignored F_t
outcomes remain marginalized exactly as in virtual7.3-7.5; helper
READs of banked fields are not inserted into the sigma-fields of
LemmaU or LemmaC. P's full reduced logical law and original source
history are preserved. No interleaved-supplier transfer is claimed.
The acquire-first property is the separate Section4 proof enabling
this EXACT adaptive model. All finite-input source-model requirements
are retained with the robust finite branch, not borrowed from a clean
finite tester. By virtual Theorems1-2, WHOLE-secret success>=9/10 for
every N,s and every permitted adversary, jointly with the branchwise
resource accounting below.

## 7. Exact full quantum envelope and linear ordinary workspace

Only input/output, constant-many O(n)-bit operands and slot/row/frame
address words, finite control, and reusable bits/indices are ordinary
classical. The source's O(n^2) parameter/numerical/return records and
all key/rank/label/counter/sort arrays are in the counted fixed basis
bank and streamed. Bottom-up sorting uses constant-many streamed loop
indices; logical call state is banked. Before the bank is used, public
size words and deliveryj also use this same O(n) ordinary staging.
No duplicate ordinary table/stack/directory/circuit or growing transcript
exists. Therefore S_C=O(n) on every branch for every adversary.

Write L=log2n for n>=4096. The full literal source formulas give
 Q0<2^32*n^13*L*2^(n/(4L)).
Thus B+H+D=O(n*Q0+n^21). A positive n/(4log2n) exponential eventually
dominates every fixed polynomial, so n^21=O(n^14*L*2^(n/(4L))). This
is an analysis bound, not a new runtime switch; its finite earlier
ratios are bounded by an absolute outside constant. Full paired-prefix
rounding gives2h<4max(D,H+1,2), with at mostO(n) source temporaries.
Hence ALL source, basis, unused field/header/role and paired padding,
primitive quantum scratch and scalar arithmetic are included in
 S_Q=O(n^14*(log2n)*2^(n/(4log2n))).
No acquisition-sized metadata is omitted; it is explicitly O(nQ0),
and source's OWN held-copy space already has this scale. Every branch
uses this fixed allocation, independently of lifetime and contents.
Small inputs have the actual robust finite branch and finite uniform
resource maxima, absorbed into outside constants as P proves.

## 8. Explicit charged bit-code time and all source copies

Source's COMPLETE raw every-branch time is
 T_P=O(n^17/L*2^(n/(4L))).
Every original gate/measurement/Boolean bit instruction, word-field
operation and fixed loop is implemented by explicit finite bit code.
O(n)-bit arithmetic uses ripple/schoolbook loops, fixed role offset
computation, known original-copy index arithmetic and polynomial
scratch/frame records. Source primitives' emitted gate templates have
finite fixed nesting. A conservative O(n^4) completion per original
bit/gate/control step covers streamed loops/field/operand generation.
Each encoded elementary step may cost O(n^100) CHARGED bit work:
this includes complete address debit<=O(n), O(n^2) arithmetic, row/field
selection and a polynomial scalar scan of at mostO(n^21) cells,
polynomial original scratch roles and current-context generation.
These fixed loop products are far below n^100. No loop over Q0,H,B,
M or2^b is inside that helper. Operations on those arrays retain their
original explicit lengths or Section5's separate scope charge.
The powers are repeated operations, NOT ordinary classical work arrays.

Consequently work after delivery is bounded conservatively by
 O(n^104*T_P)+O(n^104*(B+H+1))+O(n^104*(Q0+1)).
The last term pays the extra O(n^4 Q0) scope events with n^100 helpers;
using n^104 on B/H also generously covers their exact initialization
and cleanup. Delivery size computations are polynomial and source
SWAP/slot-generation work is at mostpoly(n)*Q0, covered by these terms;
no measurement-free delivery overhead is omitted. Word/frame scratch
construction stays within Section3's fixed polynomial part.

Substituting source T_P,Q0,B,H gives degrees at most121 with logPower-1,
118 with logPower1,117 with logPower1, plus a polynomial degree125.
Since log2n<=n for n>=2 and exp(n/(4log2n))>=1, all fit the single
explicit conservative envelope
 T=O(n^132*2^(n/(4log2n))).
No unspecified polynomial degree or hidden exponent coefficient is
assigned. All arithmetic, address costs, initialization, cleanup,
arbitrary bad branches and finite inputs are charged jointly. No old
source time cap is used to hide physical compiler work.

Exactly ONE physical source request executes each original request.
There are Q0 requests on every branch, before all measurements,
including blocks unused on early output or key ties. The literal
source formula proves
 Q=O(n^13*(log2n)*2^(n/(4log2n))).
No zero padding, helper measurement, full clear or source SWAP is an
additional DCP request. The malformed allowance is therefore still
floor(Q/(64n^4)), with EXACTLY the unchanged error-model text.

## 9. Exact indices, tolerance expression and comparison scope

For fixed a>0 and finite polynomial/log powers,
 log2(2^(n/(4log2n))*n^r*(log2n)^q)=n/(4log2n)+O(log2n),
so log2log2 of the envelope divided by log2n tends to1. Thus time,
quantum and sample indices are1; ordinary n has index0. The finite
n=1 case does not alter these asymptotic indices or all-N success.
The fifth expression is EXACT1/(64n^4), with the source's long adaptive
malformed-copy model copied verbatim, not a new clean-only context.
It bounds the number of corrupted ACQUIRED copies, not a per-copy
error probability. All guarantees are joint for this one implementation.

This is a credited measured-storage completion and adaptive-history
preservation proof for an acquire-first source. It reduces the source's
exponential ordinary classical space to linear while keeping its full
quantum/sample/tolerance envelopes and paying a larger explicit time
polynomial. No dominance of all four original resource bounds is
claimed. No source reflection, free QRAM, uncounted classical cache,
priority, optimality, practical speed or clean time-frontier improvement
is asserted. Source robustness and its method belong to its authors;
actual publication and own fresh atomic review remain separate gates.
