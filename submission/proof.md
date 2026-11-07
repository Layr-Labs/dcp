# IFCW500-TBANK: typed indexed basis storage and shared merge scratch

## 0. One indexed physical algorithm and joint theorem

For every N>=2,s in Z/NZ putn=ceil(log2N). The ONE physical
IFCW500-TBANK algorithm below recovers the WHOLE secret with
unconditional probability at least1-2^-8 from independent ideal copies.
On EVERY branch, including initialization, extraction/merge failures,
rejected/discarded inputs, original source/fallback aborts and cleanup,
 T=O(n^104*2^((15/7)*sqrt n)),
 S_C=O(n) classical bits,
 S_Q=O(n^2*2^((3/4)n^(1/2))) allocated qubits,
 Q=O(n^2*2^((8/7)n^(1/2))) acquired copies.
Outside constants are absolute, independent ofN,s and outcomes.
Exact growth indices are[1/2,0,1/2,1/2]; only time scores[1/2].
The fifth expression is0 under the exact canonical model

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

The exponential arrays are stored as FULLY COUNTED basis-state qubits,
not free classical storage. Accesses use known classical wire indices;
original coherent table queries remain serial circuits. Large owner
regions are cleared on allocation/free, and their COMPLETE clear cost
is charged to fresh-input scopes in Section6. This uses no epoch tags,
coherent bank query or QRAM. The original n<2^20 finite tester remains.
This is a storage/time/source tradeoff, not a cube-root-time result,
new primitive, lower bound, practical speed or optimality claim.

## 1. Actual complete direct sources and evidence scope

The COMPLETE selected virtual program P is IFCW500, adapted from IFCW710 public submission
c1ce482e-b667-4ce5-8fd3-089db53d46a9, commit
40e41aa711b10a9fa08b4f74a729637532e2bb7f. Its full proof SHA256 is
63bdf933495fa1d6e561b542a4f224636c0a24e5d2f4472eab681b66917c09ce.
The ENTIRE argument is reproduced with explicit ADAPTATIONS after a
virtual-only scope header in virtual.md. Fixed a=1/2 replaces7/10;
integer square-root tests, all numerical base inequalities, resource
powers and equal-power growth-index calculations are updated. This
adapted body is NOT claimed byte-identical to the original source. Every source identity, verified LE and fallback cap,
phase-vector lookup/merge, implicit-fiber stream and cutoff, conditional
incidence/failure argument, depth/fresh-child/source-cap argument, odd
decoder, 2-adic recovery, finite branch and error bound is supplied there.
No predecessor JSON, historical acceptance or opaque imported theorem is
a mathematical premise. Every resource assertion in that body concerns
reference P's implementation, not the physical storage theorem here.
This main proves all four changed physical bounds for the same output law.

The distinct actual direct storage-method source is corrected
LLV-GBANKQ25, public fbb8f36c-3904-4bf0-9ddf-e9f5d83657ae, commit
100a8e307fd90c489c4d90717613869fed576b3b, main proof SHA256
08608c19bf8d7ba42b50cf01f86662bc4e38ae0de63a2825ed4f86c8f10ca7d0.
Its fixed maximum regions/direct wires, measured basis READ/WRITE,
correlated-CQ forgetting/source coupling, uniform bit interpretation and
whole counted paired prefix are reproduced/adapted below. Its different
quarter-square-root virtual program and historical unused erroneous
finishing comparison are NOT adopted. The former conservative full-bank-scan upper estimate PER BIT ACCESS
is replaced by the actual classically indexed wire operations. Full
owner-region clearing on object allocation/release is retained and
its source-specific amortized work is proved in Section6. The direct
wire/CQ method is prior work; this is a sharper indexed accounting
and a new resource configuration, not its independent invention.
The separate local generation-tag prototype is NOT this algorithm.

Both original full source artifacts were read, matched to their published identity
and all five official evidence maps, with relevant declaration/show/history
views inspected before use. Exact source/dependent endpoints must be declared before upload.
Pending declarations are neither certified ancestry nor falsity. All P's
IFC1/IFCW23/IFCW34, CW1, MW4/MWG716K, CS1/CS1-S3, Kuperberg and upstream
credits in its full body remain. The bank source's LLV-GBANK, PSG21
9fdfdb12-834d-441c-8bb1-717ab380abf3 and PSG2-QSTORE
2b2b0036-7bbc-4ce5-80a8-b8928f0ce120 credits also remain. The different
virtual algorithms of those bank ancestors are not selected. No external
quantum-walk/QRAQM construction or positive-corruption theorem is used.

The immediate local storage predecessor is IFCW710-TBANK, main SHA256
a9f9953866aa6b93168c2401e11d78f26a9ab1be05b937dfb634d46c070beb01.
Its indexed accesses, full-clear fresh-input charge, complete reference
selection and CQ proof are carried here. This revision retains its typed phase/shared-scratch spans and
explicit polynomial interpreter overhead, while changing the entire
reference profile to a=1/2 and rederiving all bounds at that profile. Its native or hosted verdict is not
a theorem premise. The public dependency record will identify its
actual published submission before this revision is uploaded.

## 2. Exactly selected instruction stream and finite branch

For n<1048576 run P's explicit exhaustive shift tester: for cand=0..N-1
in order, use at most n+10 fresh copies, apply Shift_cand, measure the
control in X, and reject at the first minus; output the first passing
candidate, or0. Stream candidates and outcomes with O(n) classical bits
and O(n) qubits. The true candidate always passes and each wrong one
passes one fresh test with probability1/2, giving error<=2^-10. All
costs on this fixed finite prefix change only absolute outside constants
in the four displayed envelopes. No list of all candidates is retained.

For n>=1048576 execute PRECISELY P's source/test/merge/tree/decoder/cap
schedule. Its literal parameters, computed by exact integer arithmetic,
are
 w_s=least w with(4w)^2>=9n,
 lw=least v with v^2>=n,
 mu=least M>=1 with(M-1)(w_s+lw+2)+2w_s+lw+2>=n,
 kappa=ceil(log2(mu+4))+3,Lam=kappa+1+w_s,l=kappa+1+lw.
The names w_s,lw distinguish source table precision from the physical arena
parameters below. All ceilings use integer bit lengths/division/binary search;
no real-log oracle is assumed. The full virtual body gives every per-tree
binary/four-input level, exact partial widths, LE/verification/fallback,
source rejection, both decoder schedules and original guards.

In particular nqmax=16*4^mu*Lam and the original source cap is
 Q*=6*nqmax*((J+1)K+2a2)+2a2,Qcap=1024Q*.
The LE fallback counter is capped at Cf=ceil(Qcap/ceil(sqrt n)). Those
guards remain at their original positions; simulator work is separately
charged, not hidden behind an obsolete virtual counter. No virtual source
request, phase operation, abort or retry is omitted or added.

Fix ordinary streamed finite bit code for the stated ripple arithmetic,
merge sorting, array-based heap streams, flat buffers and circuit generation. Resolve any
unspecified heap tie lexicographically by the LOGICAL tuple/row indices;
physical owner addresses never enter that order. The source stream and
phase proofs hold for this deterministic completion. An array is an
opaque logical object with its stated length/fields; unused fresh cells
are zero. Bounds checks and all logical row domains are retained. The
adapter may rename array owners, not logical tuple indices or values.

Multi-bit work is decomposed into bit actions, with loop/call contexts
and generation state kept in the counted virtual records. Original
classical fields have O(n) bits. Only a fixed number of their O(n)-bit
operands or indices may be staged at a time. Current-frame location and
finite program control are short; return frames remain in the bank.
All old quantum measurements, coins, resets and releases retain their
specified instruments. Toffoli uses its constant exact Clifford+T word.
No exponentially long circuit/instruction list is stored.

## 3. Typed fixed capacities and one shared scratch bank

Keep the exact parameters/profile/guards of Section2 and the full
reference. The physical layout differs from the coarse equal-sized
owner layout of the earlier indexed-bank development. It uses TWO
fixed owner classes, one for retained phase tables and one for active
merge scratch. The source Sections6-7,11,13 give, on EVERY branch:
 - depth<=mu+4, arity at most4 and at most5 phase tables per depth;
 - phase tables have <=2^Lam rows and each label <=3n bits;
 - binary sort/heap/run arrays have O(2^Lam) rows;
 - four-input Buf,Tl and block maps have <=Cp rows,
   Cp<=2^(Lam+kappa+3)+1; fixed constant-many arrays per merge;
 - every row has a constant number of O(n)-bit fields; actual tuples
   have four indices, and keys/windows/labels have at most O(n) bits;
 - scalar/frame/LE/decoder/generator records use polynomial SMALL,
   and original coherent storage is O(n).

Depth-first evaluation invokes a merge primitive ONLY AFTER ALL of its
children have been built. While generating any child, a parent retains
finished child phase vectors and scalar parameters, but no live merge
sort/run/heap/Buf/Tl data. A binary/four-input primitive generates no
recursive child, source subtree or nested merge. It completes or fails
before the next child-generation or merge primitive starts. The same
holds across sequential roots and both decoder stages. Therefore the
ENTIRE execution has at most ONE active merge scratch scope, including
wrong labels, cutoff failure, retry and source-abort branches. This is
a scheduling invariant, not a favorable-outcome or occupancy estimate.
At most5(mu+5) phase vectors coexist. Output vectors use phase owners;
scratch is retained until their labels/quantum output are complete and
then cleared. Handles of retained siblings are never cleared or moved.

Set ordinary row width Wrow=2^16*n basis-bit cells. Reserve
 Aphase=2^16*(mu+5) owners, Rphase=2^(Lam+8) rows each;
 Ascratch=2^16 owners, Rscratch=2^(Lam+kappa+16) rows each.
The constant owner families exceed the fewer-than512 source arrays:
phase/sibling/input/output tables, binary order,pos,lo,cnt,off,Dx and
inverse-block structures, four-input sort/run/heaps/Buf/Tl/block maps.
Their actual domains and row widths are unchanged. All additional
polynomial scratch, scalar records and helper frames are SMALL, never
new exponential owners per row/gate operation. The phase pool exceeds
5(mu+5) live vectors. One scratch owner per named array suffices for
the single active primitive; shared scratch is not reserved per depth.
The field width covers constant-many source words/tuples per row;
streamed pair fibers are never materialized as arrays.

Give phase owner i cells [i*Rphase*Wrow,(i+1)*Rphase*Wrow), and scratch
owner j the same expression with Rscratch after the COMPLETE phase
span. These are disjoint fixed ranges with FULL maximum total span
 B=Wrow*(Aphase*Rphase+Ascratch*Rscratch)
  =2^32*n*((mu+5)*2^(Lam+8)+2^(Lam+kappa+16)).       (3.1)
Every bit, inactive owner/row/field and padding is counted, independent
of retries/lifetime. Typed handles (class,owner,row,field) are stable;
passing a vector transfers its handle. A directory scan has only
Aphase+Ascratch=O(n) entries and is polynomial. Owner IDs are reused
after explicit full-region clears. All directories, metadata, call
frames and arithmetic work arrays live in counted SMALL. Source
bounds/checks/equality/ties use original logical labels/indices, never
physical owner addresses. The new fixed layout changes no source
instrument or failure/guard position.

Reserve the same H=2^32*n^2 original quantum slots as before, including
pending phase indices, current arithmetic/lookup/source/LE/reset scratch.
Only released slots are reset/discarded/reinitialized. Other live
quantum registers are preserved. Quantum-pool metadata is SMALL and
canonical slot offsets do not grow with lifetime. All limits hold on
wrong-label and source-abort branches as well.

## 4. Whole counted BIG, SMALL and original quantum arenas

Use the Section3 BIG spanB. Give every BIG phase owner Rphase*Wrow bit slots and every scratch
owner Rscratch*Wrow bit slots, whether currently used or not. Source actual lengths/field
widths remain unchanged; unused padding is ignored by the algorithm.
Reserve a SMALL raw-basis arena Ssmall=2^48*(n+2)^20 bit slots for
all polynomial-size globals, scalar/word arithmetic, source/LE scratch,
decoder records, call/return frames, finite generator state, owner
bindings/flags and quantum-pool metadata. Source Lemmas7,11,13 give
O(n)-bit ordinary fields, polynomial depth and polynomial-size such
records. Fixed role/depth/field offsets and reusable word scratch fit
this conservative polynomial arena. It does NOT hold the exponential
table/heap/list rows, which are BIG arrays. A SMALL reset only clears
the released/initialized subrange, never other live frames. Even a
full scan of the polynomial arena selecting that range costs poly(n).

A conservative complete basis-slot limit isD=B+Ssmall+H. This includes
raw directory and scratch padding. For each basis bitj use physical
even wire2j; original quantum q is odd2(q+1)+1; reserve odd1 for a
fresh fair bit. Let h be least power of two at leastmax(D,H+1,2).
Allocate and initialize the WHOLE prefix0,...,2h-1 to zero before P.
Every unused owner/row/field, inactive scalar slot, owner binding,
free flag and paired-prefix padding wire counts inS_Q. No lifetime-
growing address names or sparse omitted directory is used. Owner IDs
and quantum slots are reused after explicit clear/reset.

InputN can coexist with its counted bank copy. Hold only constant-many
O(n)-bit operands, known physical address words/current-frame location,
finite control and loop indices classically. All original frames,
scratch, arrays and allocator records remain in the counted bank.
The instruction stream is generated online by fixed finite bit code;
there is no physical classical recursion stack or exponential circuit
description. Ordinary arithmetic uses explicit ripple/schoolbook bit
loops. Metadata manipulations and SMALL calls may cost poly(n), always
with O(n) classical staging; long scratch is banked and streamed.

For source requests also count n+1 temporary wires. Acquire ONErho_s,
SWAP it into fresh zero mapped source slots, and release the now-zero
temporary wires. Each SWAP is three CNOTs with every address charged.
Fresh padding/arena zeros are not DCP copies. No source inverse,
controlled unknown preparation or purification/reflection is supplied.

All complete addresses have O(n) bits. Indeed
 Lam+kappa+log2(mu+5)<= (3/4)n^(1/2)+3log2n+O(1),
 log2(B+Ssmall+H+2)=O(n^(1/2)+log n)=O(n).
The full reserved ranges, not only live occupancy, justify those words.
Public size computations, indexed offsets and physical wire arithmetic
are charged bit operations on these O(n)-bit words, with O(n) staging.

## 5. Indexed measured operations and array discipline

READ(j) measures known even wire2j in Z into a reusable classical bit.
WRITE(j,b) reads oldz, applies X iffz differs fromb, then forgets z.
Boolean primitives stage a fixed number of bits, compute, write and
erase their temporaries. All addresses are CLASSICAL known words.
No operation sends a superposed bank address to a memory oracle.
Multi-bit fields, indices and arithmetic are explicit bit loops; no
large word/table is a unit-cost fetch. A polynomial owner directory
scan or current-frame/operand decoding is separately charged.

BIG_ALLOC chooses a free stable owner, explicitly clears its entire
typed owner region through WRITE(j,0), then returns a fresh zero array
with P's actual length and field widths. BIG_FREE clears ONLY that
released owner region, forgets its logical object and returns its ID
to the pool. Retained siblings/other arrays are untouched. Clear is
a full loop over all reserved cells, not merely the written ones;
Section6 counts its entire exponential work. It cannot expose stale
values on reuse. Source array copies/updates retain their actual loops
and aliasing; passing/returning a vector transfers its live handle.
Bounds checks and logical row domains remain P's, not padded ones.

Allocate BIG scopes only for phase-table and merge-array families:
one phase-table scope per LEAF, fixed constant-many sort/run/heap/list/
inverse-block/output arrays per binary or four-input merge attempt.
Within that attempt these are flat reused arrays. A heap pop/push,
comparison, row operation, emitted gate, bit arithmetic or loop helper
does NOT allocate a new BIG owner. Its scalar/temporary/call records
use fixed SMALL role/depth offsets and reusable scratch. LE's empirical
counters/directions, parameter/profile fields and streamed decoder
records have polynomial size and also use SMALL. SMALL initialization/
release costs at most poly(n) per logical operation, even on earlier
or wrong-label branches. All source fixed-length/helper loops remain.
This is an explicit storage policy for the supplied array algorithm,
not an assumption that arbitrary malloc traces have few events.

P's coherent LOOKUP is STILL the original SERIAL known-row circuit.
For every classical row/bit, READ that logical table bit and emit the
SAME controlled gate on the ORIGINAL P index/equality/output registers.
A superposed table index never becomes a bank wire address. Heap/stream
accesses are classically selected. No source query or child construction
is inserted into a quantum lookup. All gate descriptors and indices
are generated online. Original Toffoli expands into its exact constant
Clifford+T word; other gates/measurements/coins retain their instruments.

Execute every original failure, retry, source/fallback guard and decoder
step at its logical position. Reset/discard original quantum slots by
the same trace-out/reinitialize channel, even with references. A
polynomial pool scan resets ONLY the released slots. Other live P
quantum registers remain untouched. At termination stream the final
residue to the counted O(n)-bit ordinary classical output FIRST, then
clear/release the WHOLE prefix and helper fields. All work is counted.

## 6. Deterministic fresh-input charge for every BIG clear

We bound object scopes without an expected-runtime or favorable-label
argument. A source leaf qubit comes from a fresh acquisition (possibly
after rejected ones); every phase-vector LEAF uses Lam>=1 such qubits.
Each started binary/four-input merge attempt builds fresh child vectors.
On FAIL its inputs are discarded and NEVER reused. At a FIXED tree
height, the source-copy sets used to build inputs of distinct attempts
are disjoint. This includes attempts in failed ancestors: later retries
regenerate children rather than cloning/reusing their input registers.
Classical duplication of table entries is not duplication of source
quantum inputs. Any one acquisition is charged at most once at that
fixed height. This is the same structural fact used explicitly in the
full virtual Lemma11.2, reproduced here for the new clearing cost.

There are at mostmu+4<=n merge heights in any requested TREE_D; include
height0 for LEAF. These height labels can be used across successive
root/decoder calls, whose inputs are fresh. Each completed/failed scope
has at least one acquisition in its construction. A final unfinished
source-abort path has at mostn+1 frames/scopes; allowing an extra1
per height covers scopes allocated before their first acquisition.
The original deterministic Qcap therefore gives at most
 C*(n+1)*(Qcap+1)
BIG scopes/array events, for one fixed constantC accounting for the
fewer-than512 named families per attempt. Free events are bounded by
allocations plus final live owners. Different root precisions/partial
binary widths do not change fresh-input ownership or the n-height
upper bound. Wrong extracted labels affect values/outcomes, not this
allocation discipline. Global abort terminates, not a new retry loop.

All inner stream, heap, sort, gate-generation and word helper calls
reuse their scope's BIG arrays and SMALL scratch, as fixed inSection5.
Thus an exponential row loop does NOT create exponentially many BIG
scopes independent of fresh inputs. Source/LE/decoder polynomial-sized
helpers use SMALL and need no BIG reset charge. This distinction is
essential for the bound and is part of the actual implementation.

Clearing an owner touches at mostB basis bits, each by explicit known-
address WRITE(0); even using the largest region bound is conservative.
Full address/loop work is poly(n) per bit. Hence TOTAL BIG allocation/
free/abort clear work on EVERY branch is at most
 poly(n)*B*(Qcap+1).                              (6.1)
No B scan is charged on each logical bit access; (6.1) accounts for
every actual region clear. One-time arena initialization/final cleanup
adds poly(n)*(B+Ssmall+H). No failure probability is spent to obtain
these branchwise limits.

## 7. Correlated-CQ invariant, forgetting and whole-secret correctness

At aligned logical steps, with any arbitrary referenceR, the physical
state has the form
 sum_z p_z |z><z|_(basis records/metadata) tensor rho_z_(mapped P quantum,R).
The bank records may be correlated with phase/query registers andR.
No product-state assumption is made. Let pi retain P's decoded logical
arrays/control/object bindings and mapped quantum registers, forgetting
physical-only directory/padding. Different z with the same logical
record contribute the corresponding MIXTURE of conditional rho_z.

Initialization gives P's input and prescribed zero scratch. On each
basis branch, READ returns the same logical bit; nonselective Z reads
leave a CQ state unchanged. WRITE and Boolean operations implement P's
same update. Overwriting or forgetting merges old records by mixing
their conditional quantum states, exactly as classical irreversible
forgetting requires. Clearing a released BIG/SMALL region erases just
that logical record/ignored padding, even if it was correlated with
retained phases; it does not assume independence. ALLOC supplies a fresh
zero array, and handle renaming preserves logical identities/row order.
Original controlled gates, serial LOOKUP, measurements, fresh fair coins
and resets have the same instruments. Quantum release is trace-out then
fresh zero with arbitrary references. One ideal source request and its
SWAP supply exactly the same independent rho_s as P, with no duplicates.

Consequently pi o Phi_physical=Phi_P o pi at aligned steps. By linearity
this holds for arbitrary conditional rho_z/R, including failed extraction
labels, measured fibers, partial children, source rejection, FAIL and
both original cap exits. Streamed helper outcomes are forgotten rather
than accumulated in ordinary classical memory. Complete logical state,
unconditional output distribution and source-request sequence equal P's.

The ENTIRE virtual Sections3-12 establish P's unconditional full-secret
success>=1-2^-8 for everyN,s: source diagonalization and verified LE
coupling, phase-preserving rank/stream/block instruments, conditional
incidence/fiber bounds, fresh-child/source and fallback caps, odd and
2-adic decoders, and finite tester are all supplied. Prior verdicts do
not supply any theorem. We do NOT assert those held-out-bit bounds
conditional on every additional bank helper transcript: pi marginalizes
those outcomes and preserves the required LOGICAL law. No transfer to
a different adaptive malformed-supplier model is claimed. The proof
uses only independent ideal copies and the canonical fraction0.

## 8. Complete physical storage with exact polynomial power2

Input/output coexist with constant-many O(n)-bit operands, physical
addresses/current-frame words, finite control and reusable bits/indices.
Every original array, numeric scratch, call/return frame, long counter,
decoder, generator and allocator record is in the counted bank. SMALL
arithmetic streams its scratch rather than staging polynomial arrays
classically. No ordinary classical recursion stack or large directory
exists. Thus S_C=O(n) on every branch.

By full prefix counting, S_Q<=2h+O(n)=O(B+Ssmall+H+n).
The exact source estimates give
 mu+5=O(n^(1/2)), 2^kappa=O(n^(1/2)),
 2^Lam=2^(kappa+1+w_s)=O(n^(1/2)*2^((3/4)n^(1/2))).
Substituting BOTH complete spans in(3.1),
 B=O(n*((mu+5)+2^kappa)*2^Lam)
  =O(n^2*2^((3/4)n^(1/2))).
All fixed phase owners, shared scratch owners, actual/sentinel rows,
fields and unused padding are counted. This relies on the proved
single-active-merge scheduling discipline; it does not allocate a Cp
scratch bank per depth and silently omit its capacity. Polynomial
SMALL/H/source-temporary and prefix rounding terms are additive and
smaller eventually; all finite earlier lengths change only an absolute
outside constant. The exact declared polynomial power2 and inside
exponential coefficient3/4 therefore hold for the entire physical
allocation on every branch, independent of numerical label correctness.

## 9. Charged indexed accesses and generated bit code

Complete physical addresses have O(n) bits (Section4). Every physical
gate/measurement/Boolean/bit action pays its FULL debit
ceil(log2(S_C+S_Q+2))=O(n^(1/2)+logn)<=O(n).
Known owner/row/field arithmetic and index decoding use explicit
schoolbook operations on O(n)-bit words with O(n) ordinary scratch.
Typed owner-directory scans have O(n) entries; no scan over B is needed
to access a known logical bit. Logical words contain O(n) bits and are
fetched/updated through such bit actions. BIG row loops remain P's
own loops, with their original lengths, not an oracle lookup.

SMALL resets/word scratch can conservatively scan a polynomial-size
subrange while preserving other live records. Quantum pool resets are
also polynomial. Finite opcode/control and gate templates are generated
online, with frame/return contexts banked. For concreteness a generous
O(n^100) CHARGED overhead per old logical bit/gate/SMALL operation
covers directory search, O(n)-bit arithmetic/operand decoding, fixed
SMALL helper loops, original quantum slot mapping, addresses and
temporary source moves. Only a fixed number of O(n)-bit operands are
staged; long scratch is streamed in SMALL, so this time bound does not
introduce O(n^100) ordinary classical memory. Fixed helper loop nesting
is polynomial; no BIG clear is hidden inside it.

BIG allocation/free is the separate explicit region loop ofSection6,
not called on each streamed row/gate. Its total work is(6.1). Initial
and final prefix work is poly(n)*(B+Ssmall+H). Original source/fallback
guards are checked at their original logical points. All extra compiler
costs are counted separately rather than hidden in those old counters.

## 10. Exact time envelope with the exact combined leading coefficient15/7

Let x=sqrt n, y=sqrt n. The complete virtual proof gives
 T_P=O(n^(7/2)*2^(x+(8/7)y)),
 Qcap=O(n^2*2^((8/7)y))
on every branch, including wrong labels, all failed/discarded work,
source/LE/fallback caps, finite streams and both full-modulus decoders.
No historical review or score is a premise for these source facts.

Section9 supplies the explicit generous O(n^100) CHARGED overhead per
old logical bit/gate/helper operation. Its finite loop templates use
O(n)-bit schoolbook operands and at most a complete polynomial SMALL
scan, with banked long scratch. The largest SMALL span is O(n^20);
adding serial arithmetic/decoding, polynomial directory and quantum
pool scans, nested bit loops and the O(n) address debit is covered by
n^100. No array-sized BIG loop occurs inside this overhead: original
array/serial-lookup loops are P operations and full owner clear loops
are separately counted by Section6. Original charged T_P upper bounds
its elementary operation count, so the simulated contribution is
 O(n^(207/2)*2^(x+(8/7)y))
 <=O(n^104*2^(x+(8/7)y)).

Each clear bit may also conservatively cost O(n^100); Section6 gives
at most O(n*(Qcap+1)) complete owner scopes. Thus clear, initialization
and final cleanup together cost at most
 O(n^101*B*(Qcap+1)+n^100*(Ssmall+H+1)).
Because B=O(n^2*2^((3/4)x)), this is a fixed polynomial times
2^((3/4)x+(8/7)y), plus a polynomial. Its STRICT x/4 exponent gap
absorbs every excess polynomial into 2^(x+(8/7)y), even with no slack
in the combined leading time coefficient15/7. Consequently the JOINT exact bound is
 T=O(n^104*2^((15/7)*sqrt n)).
Its polynomial104 is explicit, not an unspecified hidden exponential
coefficient. The same fixed main algorithm is used for every n>=2^20;
no eventual asymptotic threshold or extra abort is a runtime guard.
The original finite tester and remaining finite prefix have finite
uniform branchwise cost ratios and change only outside constants.

Exactly ONE physical request executes each P DCP request and no others.
Every failure/rejected/discarded input and source/fallback abort counts.
A source SWAP, fresh zero bank wire, full clear or metadata operation
is charged work/storage, not a fresh DCP copy. Thus Q=Q_P and the
literal unchanged source cap proves Q=O(n^2*2^((8/7)y)) with exact
polynomial power2 and inside coefficient8/7. All guarantees concern
this SAME implementation, never separate parameter choices or only
favorable source/measurement branches.

## 11. Exact indices, clean-copy scope and source tradeoff

The time envelope n^104*2^((15/7)sqrt n) has exact growth index1/2.
Classical n has index0. Quantum n^2*2^((3/4)sqrt n) and sample
n^2*2^((8/7)sqrt n) each have index1/2. Equal time exponential powers
are combined exactly; no second lower-order exponent is presumed.
These are indices of proved upper envelopes, not lower bounds. Only
time scores[1/2]. The fifth supported fraction0 has the exact stated
independent-ideal-copy model, jointly with WHOLE-secret success and
all four physical envelopes. No positive corruption or impossibility
claim is made.

The complete inherited implicit-fiber phase/LE/decoder methods, fixed
bank/direct-wire/CQ techniques and immediate typed indexed-bank
predecessor are credited. This changes the fixed width/depth profile
and rederives all probabilities, caps, integer inequalities and physical
bounds for the resulting SAME implementation. Smaller time index than
the a=7/10 profile trades against more acquired copies; it is not a
four-coordinate dominance claim over that predecessor. No free QRAM,
source reflection, uncounted memory, priority, practical performance,
optimality or cube-root-time breakthrough is asserted.
