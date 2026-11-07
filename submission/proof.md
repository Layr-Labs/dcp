# IFCS1-IBANK: fresh-input-amortized full clears for a saturated cap-limited sieve

## 0. One physical indexed algorithm and joint theorem

For every N>=2,s in Z/NZ put n=ceil(log2N). The ONE physical
IFCS1-IBANK algorithm below recovers the WHOLE secret with unconditional
probability>=1-2^-8 from independent ideal copies. On EVERY branch,
including wrong labels, failed/discarded inputs, extraction/source/
fallback aborts, initialization and cleanup, jointly
 T=O(2^((47/25)*sqrt n)), S_C=O(n) ordinary classical bits,
 S_Q=O(2^((23/32)*sqrt n)) allocated qubits,
 Q=O(2^(sqrt n)) total acquired DCP copies.
Outside constants are absolute, independent of N,s and outcomes.
Indices are[1/2,0,1/2,1/2]; only time scores[1/2].
The fifth supported expression is0 under the exact canonical model

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

Complete original IFCS1S2332 reference P is supplied in two byte-exact
virtual pieces. Exponential classical records become COUNTED basis
qubits with classically indexed reads/writes. FULL owner-region clears
on allocation/free are NOT omitted: disjoint fresh inputs at each
height charge all their work. Here internal time boost d0 exceeds the
stored cap mu0, so the exact margin tau0-(mu0+H0)=d0-mu0>0 pays for
every full clear. No lazy epoch tags, coherent bank query, free QRAM,
new source reflection or extra abort is introduced. Original finite
branch n<4096 remains. No priority/optimality/practical-speed or
cube-root-time claim is made.

## 1. Actual complete direct sources and scope

The COMPLETE selected virtual program P is IFCS1S2332, actual public
submissionda8cc2af-0ec2-4481-bd6a-5d9f9f856d3f, commit
41c1d63571e59daa5c178456f331716bc5f03e06, full65438-byte proof SHA256
db865a11ce1b0a1b0e060e9fa49af280e55b357526d62b564755fa7a1ad2454e.
Its ENTIRE body is supplied as two consecutive BYTE-EXACT pieces in
virtual-phase.md and virtual-decode.md with VIRTUAL-ONLY scope headers;
concatenating bodies reconstructs the exact full source/hash. Every
LE/source/fallback guard, saturated/unsaturated phase/fiber argument,
cap-limited leaf/depth/capacity calculation, fresh-child/source bound,
odd/2-adic decoder, finite tester and probability proof is supplied.
All body resource statements concern P's original implementation,
not this physical bank. No historical verdict/JSON/opaque theorem is
a mathematical premise.

The immediate indexed full-clear compiler source is actual published
IFCW710-IBANK51cc2fc5-b53e-4861-a59e-14ca5b9afcee, commit
2e5ac929ce1053a2e622d3ae4f656fa09f38d265, full main SHA256
22c4c603c7092c4ee6797ed71d68dfcb9e4375194423fa04ab1fcb240ccef70e.
Its fixed BIG/SMALL layout, classically indexed bit operations, exact
CQ/source coupling, deterministic fresh-input scope charge and whole
counted prefix are adapted to the ACTUAL new P. Its different constant-
width reference is not selected, and its verdict is not a premise.

The distinct directly consulted measured-bank method is corrected
LLV-GBANKQ25, actualfbb8f36c-3904-4bf0-9ddf-e9f5d83657ae, commit
100a8e307fd90c489c4d90717613869fed576b3b, full main SHA256
08608c19bf8d7ba42b50cf01f86662bc4e38ae0de63a2825ed4f86c8f10ca7d0.
Its fixed direct-wire/CQ/irreversible-forgetting/source method is used,
not its quarter-square-root virtual program or historical unused
finishing comparison. This is credited storage accounting, not an
invention claim for measured basis memory.

Full public files, all five official evidence bindings and relevant
current declaration/show/history views were verified. P has13 pending
declarations, indexed predecessor2, no applied edge or cursor in either
current view. All unique rationales/evidence/decision fields were read;
pending is neither verified ancestry nor false. Original source-author
IFC1/IFC-B/BL1/IFC34, CW1/MW4/MWG716K, CS1/CS1-LB/CS1-C3L/LL-150 and
Kuperberg/Schroeppel-Shamir/Howgrave-Graham-Joux credits remain in full.
Historical first-person provenance in virtual bodies denotes their
original authors. Bank PSG21/PSG2-QSTORE credits remain. Material
actual public sources require exact-file both-endpoint citations.

## 2. Exactly selected source profile and finite branch

For n<4096 run P's original exhaustive candidate tester, streaming
candidates0..N-1 and n+10 fresh Shift/X tests per candidate with early
minus rejection. Output the first passing candidate, or0. The true
candidate always passes; each wrong candidate passes a fresh test
with probability1/2, so error<=2^-10. Use O(n) ordinary bits and O(n)
qubits. All finite-prefix costs change only outside constants.

For n>=4096 execute EXACTLY P, using fixed rational
 mu0=7187/10000,d0=703/800,
 H0=1724835929/1724880000,tau0=3240574229/1724880000=H0+d0,
and literal integer parameters
 w_s=least w with100000000*w^2>=51652969*n,
 v_s=least v with640000*v^2>=494209*n,
 nu=w_s-5,gamma=v_s-nu,Astar=(w_s-nu)*(w_s+nu-1)/2,
 G_h=least G>=0 with Sstar(G)>=n,
 Sstar(J)=Astar+sum_(j<J)min(2w_s+2j+gamma+3,3w_s+3),
 mu=w_s-nu+G_h+1,kappa=ceil(log2mu)+3,Lam=kappa+1+w_s,
 hmax=w_s-nu+2G_h+2.
G_h denotes source Section7's height counter G, not LE precision G.
All parameters use exact integer arithmetic, not real oracles. Full
P Section7 gives every variable-width binary/four-input level, saturated
r=0 window, root/partial greedy capacity, cap-limited leaf nu and both
height/capacity lemmas with their exact premises. They are not replaced
by a different profile or favorable-outcome schedule.

Put nqmax=2^hmax*(kappa+1+nu). The UNCHANGED literal cap is
 Q*=6*nqmax*((J+1)*K+2a2)+2a2,Qcap=1024Q*,
where J here is the odd-decoder stage count. Keep original LE precision,
verification/source rejections, Cf=ceil(Qcap/ceil(sqrt n)), every source/
fallback guard, actual failure/retry/ABORT position and both complete
decoders. Exactly one physical source request executes each original.
Compiler work is separately charged, never hidden inside old counters.

Choose fixed finite streamed bit code for ripple/schoolbook arithmetic,
merge sort, flat heaps/lists and circuit generation. Equal-key ties use
original LOGICAL tuple/row order, not physical IDs. Source domains,
labels, fields, aliases and masks remain unchanged; array handles move
on return/pass, not by copying a retained quantum input. Bank every
return frame, numeric scratch, profile/decoder/generator state and
allocator record. Only constant-many O(n)-bit operands are ordinary.
BIG arrays are per phase/merge scope; inner word/row/heap/gate helpers
use polynomial SMALL scratch and reuse existing BIG arrays. They do
not allocate an exponential owner per inner operation.

## 3. Source-specific capacities bound MAXIMUM addresses

Layout symbols A,B,D,H,Ssmall in this main are physical parameters.
Source P's own homonymous logical fields remain exactly its own; with no physical epoch counter introduced.

This is a concrete layout, not an inference from observed occupancy.
Virtual Sections6-7,11,13 prove on EVERY main-branch execution:
 - depth<=mu<=2sqrt n<=n, arity<=4;
 - every phase exponent lam_i<=Lam and table rows<=2^Lam;
 - labels<=3n bits; heap/sort/run arrays O(2^Lam) rows;
 - Buf,Tl<=Cp<=2^(Lam+kappa+3)+1 rows, saturated levels included;
 - constant-many arrays per frame/current merge;
 - K=O(sqrt n) decoder records, no stored candidate grid;
 - original pending/current/source/LE quantum storage uses O(n).
Fixed sizes and cutoffs hold when numerical labels are wrong too.

Use A=2^16*n^2 reusable owner slots. Give each owner R=2^(Lam+kappa+16)
rows, each of Wrow=2^16*n^2 logical bit cells. Actual arrays use their
source lengths and field widths, with the remaining region padding
ignored by the logical program. A global/scalar/frame block can pack
many ordinary fields in rows; a table or stream array receives its own
owner. An owner handle plus row/bit offset is an injective stable address.
Release/reuse returns the SAME owner, not a lifetime-growing address.

For explicit conservative counting, fewer than512 named table, heap,
sort, run, list, arithmetic, generator and frame families per depth suffice:
there are at most five retained phase tables per level; binary scratch
has the listed order,pos,lo,cnt,off,Dx,residue and inverse-block arrays;
the four-input step adds two heaps, sort/run fields, Buf,Tl and block
maps; LE/transform, scalar and decoder families are fixed in the supplied
code. Packing each additional scalar family in one row is more than
sufficient. Also
 K<=2^13*(hmax+ceil(log2Lam)+ceil(log2n)+32)<=O(n).
Thus512(mu+5)+K+4096<A on the main branch (even the crude K<=2^16n
suffices). Every row bound, including Cp and sentinels, is below R;
every ordinary row's constant-many O(n)-bit entries fit Wrow. Schoolbook
scratch can use polynomially many rows in these same families. These
are analytic upper capacities, independent of success/retry history.

The complete logical classical address span is therefore at most
 B=A*R*Wrow=2^48*n^4*2^(Lam+kappa).
All allocator bindings, flags and free-owner state are counted below.
BIG arrays use the owner slots; polynomial-size scalar/frame/helper
records use the separate SMALL arena of Section4, not a fresh BIG
owner on every word/gate helper call. Heaps and buffers are flat
array-based structures, not one allocation per streamed pair.
Choosing a free owner can scan the A slots, which costs only poly(n).
Alternatively an active logical object can be found by a scan of this
polynomial owner directory. No scan over B cells is required to find a
classical address. Source array identity/equality and within-array offsets
are preserved; handles are never used as numerical phase labels or tie
breaks. The memory representation adds only polynomial work per logical
object/bit operation. A reference bounded-owner allocator completion,
if needed, adds poly(n) bookkeeping per allocation: at most poly(n)Qcap
allocations occur, by the fresh-input tree and fixed loops. This work is
also below the source's n^2*2^v_s*Qcap core bound eventually, since
2^v_s dominates every fixed polynomial. Its polynomial record space is
below the source's exponential classical envelope. No source probability
argument depends on a physical allocation address.

Pad original quantum objects to a fixed pool of H=2^32*n^2 slots.
This includes the source's at most30n pending index qubits and its
current O(n) arithmetic/lookups, source, extraction, comparison and
reset scratch, with generous polynomial padding. Quantum slot metadata
is counted raw basis data. Quantum free/reinitialize may scan a whole
polynomial-sized register/pool if necessary; that costs poly(n), not B.
Such a scan resets ONLY the released owner slots; all other live P
quantum registers remain untouched.
Original coherent addresses are canonical pool offsets, not lifetime IDs.

## 4. Whole counted BIG, SMALL and original quantum arenas

Use the Section3 BIG spanB. Give every BIG owner exactly R*Wrow bit
slots, whether currently used or not. Source actual lengths/field
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
 Lam+kappa<=mu0*sqrt n+2log2n+O(1),
 log2(B+Ssmall+H+2)=O(sqrt n+log n)=O(n).
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
R*Wrow region through WRITE(j,0), then returns a fresh zero array
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
after rejected ones); every phase-vector LEAF uses kappa+1+nu>=1 such qubits.
Each started binary/four-input merge attempt builds fresh child vectors.
On FAIL its inputs are discarded and NEVER reused. At a FIXED tree
height, the source-copy sets used to build inputs of distinct attempts
are disjoint. This includes attempts in failed ancestors: later retries
regenerate children rather than cloning/reusing their input registers.
Classical duplication of table entries is not duplication of source
quantum inputs. Any one acquisition is charged at most once at that
fixed height. This is the same structural fact used explicitly in the
full virtual Lemma11.2, reproduced here for the new clearing cost.

There are at mostmu<=n merge heights in any requested TREE_D; include
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

## 8. Complete counted classical and quantum envelopes

Input/output coexist with constant-many O(n)-bit operands, known
physical addresses/current-frame words, finite code control and reused
bits/indices. All original tables/heaps/lists, frames, long counters,
numeric/profile/LE/decoder/generator scratch and directory flags are
counted basis records. Arithmetic streams SMALL rather than staging
polynomial arrays ordinarily. No huge classical stack/directory or
measurement history exists. Thus S_C=O(n) on every branch.

The entire paired prefix/source temporaries give
 S_Q<=2h+O(n)=O(B+Ssmall+H+n).
Source exact bounds2^kappa<=32sqrt n,2^w_s<2*2^(mu0*sqrt n),
Lam=kappa+1+w_s yield2^(Lam+kappa)=O(n*2^(mu0*sqrt n)).
Consequently B=2^48*n^4*2^(Lam+kappa)=O(n^5*2^(mu0*sqrt n)).
SMALL and original coherent pool H are additive fixed polynomials.
The EXACT positive rational gap23/32-mu0=1/20000 absorbs every such
polynomial into the declared PURE envelope
 S_Q=O(2^((23/32)*sqrt n)).
Whole unused owners/rows/fields, metadata, scalar/quantum/prefix padding,
fair bit, source temporaries and final/abort cleanup count. These are
fixed maximum address spans independent of retry lifetime and labels,
not just occupied or successful-path cells. All remaining finite n
change only an absolute outside constant, not a runtime threshold.

## 9. Charged indexed accesses and generated bit code

Complete physical addresses have O(n) bits (Section4). Every physical
gate/measurement/Boolean/bit action pays its FULL debit
ceil(log2(S_C+S_Q+2))=O(sqrt n+logn)<=O(n).
Known owner/row/field arithmetic and index decoding use explicit
schoolbook operations on O(n)-bit words with O(n) ordinary scratch.
Owner-directory scans have A=O(n^2) entries; no scan over B is needed
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

## 10. All full clears fit the exact pure time and source bounds

The COMPLETE reference proves on every actual branch
 T_P=O(n^(9/2)*2^(tau0*sqrt n)),
 Qcap=O(n^2*2^(H0*sqrt n)),
where tau0=3240574229/1724880000<47/25,
H0=1724835929/1724880000<1,mu0=7187/10000.
Section6's deterministic O(n*(Qcap+1)) BIG scope count uses the source's
disjoint fresh children at every fixed level, including discarded/
failed attempts and a final unfinished source-abort path. The source
variable widths and cap-limited leaf affect lengths, not this ownership
fact. Every complete owner clear is performed and counted. Inner
row/bit/gate helpers use SMALL and existing BIG scopes, never new
exponential clear events per access.

The indexed interpreter, complete clears, source moves, initialization
and output-first final cleanup therefore give
 T_physical<=poly(n)*(T_P+B*(Qcap+1)+Ssmall+H+1).
The clear term has leading coefficientmu0+H0, whereas tau0=H0+d0.
The EXACT positive margin
 tau0-(mu0+H0)=d0-mu0=3201/20000>0
pays every clear polynomial. Thus it does NOT multiply an exponential
bank size onto every old operation; it charges the actual object scopes.
This selected caseC satisfies d0>mu0; the same full-clear certificate
must NOT be silently applied to profiles with d0<mu0.

All remaining polynomial interpreter/source factors fit the additional
EXACT positive gap47/25-tau0. Hence, with no hidden polynomial,
 T=O(2^((47/25)*sqrt n)).
Finite earlier main lengths and the original n<4096 tester have finite
uniform branchwise cost ratios and change only an outside constant.
The SAME fixed clearing protocol runs throughout; no added abort or
asymptotic sufficient-range branch is introduced.

Exactly ONE physical copy executes each P request. Full raw arrays,
SMALL/quantum pool initialization and clearing are charged gates and
storage, not source calls. The unchanged literal source cap includes
EVERY rejected, failed/discarded input, fallback and source abort.
Since H0<1 with a separate exact positive rational gap,
 Q=Q_P=O(n^2*2^(H0*sqrt n))=O(2^(sqrt n)).
Both all-modulus recovery stages and all other resources hold jointly
for this SAME physical implementation, not separate configurations
or favorable measurement branches.

## 11. Exact indices and scope

Time2^((47/25)*sqrt n), complete quantum2^((23/32)*sqrt n) and
acquired-copy2^(sqrt n) envelopes each have growth index1/2. Ordinary
classical n has index0. Only time scores[1/2]. These are proved upper
envelopes, not lower bounds. The fifth supported fraction0 has the
exact independent-ideal-copy model stated above, jointly with WHOLE-
secret success>=1-2^-8 and every physical bound. No positive corruption
or impossibility claim is made.

The entire saturated cap-limited reference and measured/direct-wire/CQ
methods are credited prior work. This supplies a counted indexed
linear-classical configuration with FULL charged clears, using the
actual fresh-input scopes and d0>mu0 margin of this selected source.
It uses no epoch/tag machinery, free QRAM, hidden memory, source
reflection, priority/optimality claim or cube-root-time breakthrough.

