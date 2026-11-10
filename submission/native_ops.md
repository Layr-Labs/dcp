Physical costs use typed_dispatch.md; older allowances here remain valid looser bounds.

# Native operations (normative)

All source rules and caps are retained. A is the full allocated-prefix
address width. The final section specifies the current weighted bound.

## Fixed-word pool operations

COPY, ADD, SUBTRACT, INCREMENT and COMPARE of a prescribed field are
finite inline bit microprograms. Load their constant many bindings and
complete operand fields with READWORD; stage all inputs, execute the
bit-serial operation in ordinary words, and commit its fields and pc.
For length L<=n, stream ALL L stored bits; n-bit slot/frame fields include
all padding. A short packed field writes only its L positions, preserving
adjacent fields; unused staging bits are zero padding. Three-n-bit labels
use a fixed three chunks. Overlap stages every source chunk before writes.
These macros perform no unit-cost multiplication/division or table scan.
Their n elementary bit steps each cost at most O(A^2), including ordinary
index control and full address fees. Complete field helpers already cost
O(n^2), including row validation and EVERY WROW-bit first-write clearing.
Thus a macro costs O(n^2). No constant is allowed to depend on field values.

Apply these explicit macros to AVL keys/links/counts/flags, labels,
slots, heads and buffer records. Constant many fields of at most3n bits
fit each row. Parent links support ancestor repair without an ordinary
stack. The final window section replaces the old per-request GROUP loop;
all remaining older polynomial allowances here are conservative.
The supplier recurrence bounds each level's input sum by O(C_0) per
batch. O(r) levels and O(r) batches give sum Cin=O(n C_0).
Calls/returns/commits are O(n C_0+Qcap) events: requests remove buffer
rows, FW consumes inputs, and aborted chains have O(r) depth. At each
entry/exit commit all frame fields. Owner activation, renumbering and
abort occur only at aligned boundaries; no owner is allocated midway,
and caches are refreshed after boundaries. Native word arithmetic uses
constant many O(n)-bit words and explicit carry loops. All remaining
pool operations retain mapped fees.

## A fixed native region for LE

Reserve slots 0<=k<P, P=2^22 n^3, INSIDE the existing HQ-slot prefix for
one active source-transform/LE phase or FW call. Initialize general virgin=P and head=HQ; the free list
contains only slots >=P. This changes no HQ, DRAW, h or allocated-prefix
size. Since P<=U and general live<=3U, P+3U<HQ; allocation always succeeds.
The allocator invariant now separates reserved native slots, general live
and free slots below virgin, and untouched zero slots above virgin.
Reserved slots never enter the free list. LE slots are zero outside LE; encoded FW window data obey the final section.
The fixed native layout has n data positions, at most2n QPE positions,
and the retained c0 n carries/work/ancillas, all below P. Its register
bases are fixed multiples of n computed bit serially before use.

KEEP the original acquisition and n+1 mapped slot transfers. Immediately after source slot transfer and BEFORE either Mult_alpha or
Shift_c of virtual.md Section3,
SWAP each of its n mapped data qubits into the corresponding zero native
position. Read the COMPLETE old slot field for each such SWAP, costing
O(n^3) total. Keep the old slots allocated and zero during preprocessing and LE. The control
and arbitrary spectators are untouched. During preprocessing and LE the decoded map sends
data and private ancillas to native positions; the old zero positions
are reserved physical slack. A native gate forms wire address2k+3 from
its staged register base and bit cursor, delivers ALL A bits and pays
O(A^2)=O(n) charged work, using the counted carry-loop/address-buffer
microprogram. Every actual Clifford+T gate, reset and measurement is paid.
No descriptor fetch is needed for a fixed native register position.

All source preprocessing is executed in this native mode. Mult_alpha
uses the exact n controlled modular additions, swap and inverse computation
of virtual.md (T1); every data/work/carry wire has a fixed native position.
Its O(n^2) gates and bit-serial constant generation cost O(n^3), with
full native address delivery. Load alpha and its inverse as complete
fields; their Euclid/CRT computation occurs once per batch and is
polynomial setup, not free preprocessing. Repeated modular doubling
generates all alpha*2^v constants in O(n^2) raw bit work, also O(n^3)
charged. Shift_c uses the exact (T2) circuit. Load its control's complete
mapped slot address ONCE, keep that staged physical address fixed during
the transform, and deliver it with all A bits for every controlled gate.
Other operands are native. This costs O(n^2) per Shift_c, including the
full field load; no descriptor is fetched per internal gate. The control
is neither freed nor moved during this phase. Its prescribed later X
also pays its mapped helper. Thus BOTH pre-LE transforms fit O(n^3)
per acquisition. They act before the same LE tests in the same logical
order. After preprocessing the transformed data eigenstate and latent
label are exactly those in the original supplier; no original-label
assumption is used for the extractor. The native-entry SWAP is only a
representation change and commutes with decoding, not a logical reorder.

At the reference data-discard point reset native data, then release the
old zero slots with the existing full-field FREE_Q helpers. This costs
O(n^3) per copy. Reset every used native subblock before return or global
abort, including extraction-cap abort; the fixed LE subregion scan (2^16 n positions) costs O(n^2).
At aligned exit all reserved positions are zero, the label/frame fields
are committed and old data slots are freed. Extra SWAPs change only the
physical representation: conjugating the reference LE by the entry map
and its discard yields the identical channel on control and spectators,
on every input. There is no extra source request or success event.

LE private classical work uses fixed ordinary O(n) workspace. Store
modulus, current modular constant, means/counters, candidate, rh, random
shift, unwrapping value and scores in constant many n-bit chunks. Store
RUN's direction records in 6(n+5) bits. DO NOT store the n*T_V window
table: whenever f_i is read, regenerate its T_V bits at their prescribed
positions in rh. This gives exactly the same bits and O(n T_V) work per
verifier round. G_LE<=2n on the main branch. The fixed4096-entry rational
trigonometric table and the two existing compiler buffers fit the same
workspace. An explicit allowance2^16 n bits covers these records, local
cursors and all constant-arity staging, within the retained2^20 n margin.
There is no ordinary recursive source stack. Native word/bit indices are
polynomially bounded in n but EVERY operation still pays the full bank
address fee. Global fallback/source counters remain banked, loaded and
committed with full-word helpers, O(n^2) per LE. Owner allocation and
epoch renumbering occur at aligned outer boundaries, never halfway
through private native work, which does not advance any owner epoch.

Cheap QPE has O(n^2) structural operations eventually. Native implementation
therefore costs O(n^3) per call. Verification has O(n^2+n h_e log n)=O(n^2)
bit work, also O(n^3) charged. RUN(F(h_e)) costs O(n^3 h_e); its global
cap <=Qcap/r+1 makes aggregate LE work O(n^3 Qcap)+poly(n).
Original source transforms and transfers, entry SWAPs, old-data releases and cleanup
fit this bound. Guarded compilation is unchanged, counting the same
logical compiler bit steps before sources. Its finite MODE_RUN exceptions
retain terminating caps and affect only absolute constants. Tests,
coins, rounding, verdicts and fallback counts are identical, including
wrong-estimate branches. The old coupling and error budgets apply.

## Amortized tree emission

TREE/LOOKUP uses finite READVAR/WRITEVAR/GATEVAR role tuples. Numeric
positions remain explicit scalars, not recopied literal indices. The
physical resolver still reads complete stored fields and forms/delivers
full addresses at mapped O(n^2) cost per structural step.

For a t-bit field pass, initialize its RELATIVE bit cursor and carry
counter, emit constant-size tuples and increment/decrement bit serially.
Field-format roles supply the base offset through the physical resolver,
so source generation does not copy that offset at every bit. Counter/
cursor work is O(t+(log(t+1))^2)=O(t), including initialization and reverse
restoration. Internal ripple control uses the squared carry-run bound
of typed_dispatch.md. A fixed flag field uses implicit relative bit0,
not a fresh log(n)-bit index. Row binding copies its Y<=2r+1 meaningful
bits explicitly; complete physical n-bit binding loads remain paid.

Label construction/copy visits do n-bit passes, absorbing O(r) row
binding. Serial LOOKUP forms/uncomputes the actual quantum index-equality
flag, reads every prescribed table bit and executes controlled output
gates. Row-position bits are READVAR from a scalar, never a quantum bank
address. Full row label/index passes absorb binding and local setup.
Across a complete table scan row-cursor carry work is linear plus O(Y^2)
initialization, absorbed by its at least2^dl rows.

Use bottom-up stable merge-sort on the retained (key,position) records.
Every comparison scans its complete padded word: O(lam+b) bits, at least
lam because the position tie breaker is included. Copy the selected
record with the same field templates. Heap sift steps compare/update
complete O(lam+b) keys/pointers. Since lam>=dl>=r/2, O(r) row binding
and short flag tests fit each node's existing word-work allowance.
Copying a nonsequential row pointer is explicit O(r) DATA work already
in the heap/run skeleton, not O(r^2) generation. Heap-depth counters
have O(log r) bits and their setup fits the complete key pass. Empty/
short runs use fixed tests within that record visit; no new row binding
per flag is needed. Table orders and semantic quantum operations are preserved.

The cyclic-window arithmetic module may KEEP its old polynomial uniform
generator, absorbed per primitive by n(L+L') because input exponents
are at least dl>=r/2. No faster generator is assumed for that module.
The field/row/sort/heap templates add only a constant to the retained raw
binary skeleton and four-input listing bound of window_merge.md.
Thus raw tree work per batch O(n^2 2^(H+dl)), O(r) batches and mapped
O(n^2) dispatch give O(n^(9/2)2^(H+dl)) with no extra logarithm.
Substitute this tree count in short_interface.md's retained ledger.

# Persistent coherent FW windows (normative)

This replaces per-request GROUP rebuilding, input copy/clear, full code
writes and immediate least-key reselection in the inherited implementation.
Call the resulting logical algorithm P*. It uses the same parameters,
source modules, FW cells, caps and conditional laws as P, but a different
past-measurable group policy. Its trajectory can differ.
All references to P's pool below mean this P* replacement. Other modules
are unchanged. This file supplies the quantum invariant and weighted cost;
bucket_level.md supplies the unchanged dictionary and yield calculation.

## Sticky windows and complete metadata

At FWLEVEL entry import all Cin records as before. Choose the least
eligible bucket. Activate its first w FIFO records, writing their IDs to
GROUP[0..w-1], and save outside=NEXT of the last one. Stay with this bucket
until its count falls below w; then deactivate and select the least
eligible bucket again. GROUP order is its actual physical tuple order,
initially FIFO order and subsequently hole order. No reordering is implicit.
An active window's set of members is precisely the first w FIFO records.
Only GROUP IDs, an active flag, bucket ID and outside pointer are needed.
The last three are constant many banked frame fields; no extra LIVE array
or inverse membership map is introduced. Commit them before any call or
owner activation; entry refreshes full owner, epoch, geometry and format
bindings. A renumbering changes only bank representation, not quantum data.

Run a fresh independently prepared FW on this ordered window. Form all
consumed labels from still present records before unlinking or reuse.
For a pair {a,b}, a<b, export its good output, release the reset partner,
unlink just those two items and set the two GROUP IDs to zero. Other
members retain their positions, labels and slots. If the bucket still has
at least w items, fill the two holes in increasing index order by taking
outside, saving its NEXT and advancing outside. Otherwise deactivate.
For matching/Ev, form all sums, export good outputs, and stage the one
recycled label/slot in constant many full-word temporaries. Unlink all w
consumed records, zero their GROUP IDs, then insert the staged recycled
record at its new bucket tail. Metadata freeing never releases a retained
qubit. No stale ID is read after freeing. If the original bucket still
has at least w records, refill all w holes from its outside pointer;
otherwise deactivate. If it was deleted it cannot stay eligible.

The prefix-set invariant follows by removing only members of the prefix
and taking replacements from the first unencoded FIFO suffix. Recycle
insertion appends at a tail. If outside was zero, after removing any
positive number of window records and appending at most one, the old
bucket has fewer than w records; no suffix pointer discovery is needed.
If outside was nonzero, following the suffix NEXT chain includes a new
append to that bucket. On deactivation scan all w GROUP IDs, decode every
nonnull member as below and zero every ID. PREP abort performs this same
cleanup before the ordinary level abort. At normal termination reset and
release the remaining LIVE items as before. No call to LE, TREE, a source
or another native user occurs inside this FWLEVEL; all such calls see a
fully decoded state after level return.

## Quantum state and exact instrument

Use reserved slots P-w,...,P-1 for X[0..w-1], disjoint from all private
FW positions below c_F. The old P=2^22 n^3 reservation suffices. Outside
an active window X is zero; during a window X is encoded DATA, not scratch
that may be discarded. For its ordered logical qubits A define
 E_W |x>_A = |x>_A |x>_X.
Activate or fill a hole by CNOT A_i -> X_i from a zero X_i. This is an
isometry on arbitrary states including entangled spectators, not cloning
an arbitrary qubit into a separate state. The encoding's image is a
subspace, with correlations retained throughout. Decoding a member is
the same CNOT, returning its X_i exactly to zero before exporting it.
At any committed window boundary decode all members conceptually by
E_W^dagger to define pi. Neither A nor X is traced out while encoded.
This replaces the previous pi rule that simply ignored native scratch.

The exact clean Boolean FW circuit of perm_fw.md leaves its input basis
word unchanged at its measurement boundary. If U_X is that computation
on X and zero private scratch, basis expansion gives
 U_X E_W = (E_W tensor I_private) U_A.
Thus measuring the existing seed/ticket/cell registers while leaving X
encoded realizes the same conditional Kraus map on the logical A. The
identity holds for every density matrix and spectator; it is not a
product-state assumption. Fresh PREP attempts and collision resets touch
ONLY private key/sort storage, never X. Every request has a fresh seed;
no permutation is reused. After a cell, each logical CNOT A_i->A_j is
implemented on both A and X, and each logical NOT on both. Direct basis
calculation gives (CNOT_A CNOT_X)E_W=E_W CNOT_A and
(NOT_A NOT_X)E_W=E_W NOT_A. These two-gate macros are atomic semantic
operations. A partner that the logical FW resets/releases is first put
in its prescribed zero state by this exact postprocessing; the encoded
partner is then |0>_A|0>_X. Exported good/recycled qubits are decoded
before their slot handles are transferred. The total transversal work
and export decoding is O(rho) for a cell, including Ev, since w<=2rho
for matching/Ev and pair has rho=2. Released slots follow full FREE_Q.
If an abort requires destroying a live encoded qubit, decode it first,
then apply the original trace/reset. No which-input information leaks
through a discarded X or an extra measurement.

Private native scratch is zero outside each FW computation, except these
explicit encoded X positions. LE's separate region remains zero outside
LE. Window metadata is committed before any outer bank operation; RAW
renumbering leaves A and X untouched and preserves the decoded member
IDs. No private FW circuit activates an owner. Refresh bindings at each
entry as before. Full prefix preparation/cleanup still counts every slot.
The decoded-state induction of proof.md applies to P* at atomic boundaries,
using E_W^dagger when active. Bank operations stutter or update classical
records, FW follows the intertwining identity, source and other modules
operate after decoding. Physical window maintenance adds no source.

## Compact classical cell code

The inherited P array is a canonical function of the selected cell. For
main-branch w>=4, its pair/matching/Ev distinctions are those explicitly
recognized in perm_fw.md Section4. Compute a clean extra register D(P)
containing a kind and, only for a pair, its two endpoints. A serial scan
of all w fields uses Boolean equality/prefix flags and masked XORs to
accumulate the least endpoint and its partner; it uses no quantum-indexed
load. Use O(w(b_w+1)^2) gates and O(w(b_w+1)^2) scratch, conservatively
bounded by2^22 w(b_w+1)^3. D is a deterministic function of the existing
P, so measuring it does not refine any cell projector. For a pair its
endpoints determine the entire old P array. For Ev the kind does. Only
matching requires the complete w-field P payload. Measure/reset private
P/ticket/seed as before; discarded fields give no additional logical
information because their conditional Kraus scalar is input-independent
inside each cell. Additional D ancillas are reset too.

The banked output is a tagged union: pair has two staged endpoint words,
matching has w code rows, Ev has no payload. On matching overwrite EVERY
matching code field before committing its matching tag. On pair overwrite
both endpoints before its tag; old matching fields are ignored unless
tag=matching. Tag commits last, no owner activation intervenes, and next
entry refreshes bindings. This is a specified stale-payload discipline,
not an assumption that unwritten rows are zero. Matching label processing
reads the just committed full code; pair reads only its endpoints. Old
unused matching rows are cleared on owner deactivation, already charged.

The extra clean circuit fits the same private bound: w<=2r^2,
b_w+1<=r/16 and c_F>=2^17 r^6 imply its ratio to c_F is <=1/(64r).
The retained private circuit bound is5/(4r) of c_F. Their sum is less
than one for r>=2^20; X's w high slots are disjoint. This constant extra
circuit fits the global native gate count and does not change P, HQ,
DRAW, the owner count or any of the four other structured bounds.

## Branchwise amortization and probabilistic premises

Let M be the number of matching/Ev outcomes. As before,
 sum rho<=Cin, requests<=Cin/2, M<=Cin/(w-1), total unlinks<2Cin.
Initially at most Cin/w buckets are eligible. After import, only recycled
insertions can increase a count, and each can create at most one new
false-to-true eligibility transition. An activation continues until its
bucket is ineligible, so it consumes one initial/transition token; there
is no preemption. Therefore completed plus active activations are at
most Cin/w+M (one unfinished activation on abort obeys the same count).
Consequently w times activations is O(Cin), wM<=2Cin, and pair hole
fills are at most2 times requests. All GROUP writes, window copies,
decodes, postprocessing operands and compact code writes total O(Cin).
Deactivation scans are also O(Cin), including an aborted activation.
This holds branchwise.

The logical policy is changed, but each ordered window is distinct live
inputs, fixed before its current fresh seed and measurable from logical
past. Lemma7.1's arbitrary-label conditional type law therefore holds.
The bucket-level yield proof uses exactly that law, net-removal identity
and normal terminal bound S_end<=(w-1)E; sticky selection supplies all
three unchanged. Hence every displayed inequality in Lemma7.2 applies
to P*. Conditional product/disjoint-source and source-distance invariants
are statements about DECODED logical qubits; X adds no independent source.
Choices inspect only low p+c keys, FIFO links, counts, hole IDs and past
cell outcomes. Neither higher labels nor numerical physical slot values
select a group. Thus the same held-out-bit sigma-field G, independence
of unused higher bits and actual-root distance proof apply. Fresh seed
coupling, key cutoff, pool/source caps, all merges, extraction/compiler
fallbacks and decoder success budgets are unchanged. This proves P*'s
full-shift success >=1-2^-8; no literal coupling to P's different FIFO
tuple trajectory is claimed.

## Weighted physical ledger

Use exactly the complete persistent-address helpers: a valid short field
costs O(n(log n)^(3/2)), a full n-bit field/first WROW clear costs
O(n^(3/2)log n). Their argument buffers remain complete and each gate
consumes all address bits. Short window/code/member work is now O(Cin)
helpers, not w per request. Complete entry/return bindings occur O(Cin)
times and cost O(n^(3/2)log n Cin). First clears of GROUP/code are at
most O(w) per chunk and fit the same bound since Cin>=w; rows remain
active between requests. Imports, exports, released slots and full label
word work cost O(n^(3/2)log n Cin). AVL operations visit O(log Cin)
full-key nodes per O(Cin) updates/searches, hence cost
 O(n^(3/2)log n log(Cin) Cin)=O(n^2 log n Cin).
Here log(Cin)=O(r), and (log n)^(1/2)<=O(r), so this dominates window
short helpers. No full owner binding is reloaded for each member bit.
The existing private native global count including D is
O(n^(5/2)(log n)^5 C_0)<=O(n^3 C_0).
Using sum Cin=O(n C_0), tree and source ledgers unchanged, gives
 T<=c[n^3 log n C_0+n^4 log n 2^(H+dl)
       +n^(5/2)log n Qcap+n^2(HQ+DRAW+1)]+poly(n)
  =O(n^(45/4)log2 n 2^((7/6)sqrt n)).
The same algorithm has all four identical non-time structured objects:
S_C=O(n), S_Q=O(n^(-77/2)2^sqrt n),
Q=O(n^(35/4)2^((7/6)sqrt n)), and epsilon=0.
