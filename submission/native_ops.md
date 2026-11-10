Physical costs use typed_dispatch.md; older allowances here remain valid looser bounds.

# Native operations (normative)

All source rules and caps are retained. A is the full allocated-prefix
address width. The final section specifies the current weighted bound.

## Fixed-word pool operations

Use typed_dispatch.md's complete actual-field word helpers for COPY,
ADD/SUBTRACT/COMPARE and counters. Overlapping sources are staged before
writes;3n labels use three chunks. Commit full frames before calls,
owner activation, renumbering or abort; refresh bindings at entry.
Parent links avoid an ordinary search stack. The supplier recurrence
gives O(C_0) total level input per batch; O(r) levels and O(r) batches
therefore give sum Cin=O(n C_0). All source recursion remains banked.
The complete module ledgers below include the word/control fees.

## Reserved region and allocator

P=2^22 n^3 reserved slots lie INSIDE HQ, with general virgin=P and
head=HQ. Reserved slots never enter the free list. Since
U=rV>=2^21 r^7, n^3<=r^6 and r>=2, P<=U; general live<=3U implies
P+3U<HQ=2^20U. No prefix geometry changes. Native source, tree and FW
are mutually exclusive, with the explicit encoded-window exception
between FW calls only. Every guarded layout includes all used scratch.

## Direct native source transfer and exact fast preprocessing

This replaces the intermediate n+1 general-slot source import and the
schoolbook T1 implementation. ACQ still supplies ONE fresh external
(n+1)-qubit register and counts one source. SWAP its n data bits directly
into the fixed native LE data region, using persistent complete operand
buffers. Keep its control in the external acquisition register during
preprocessing/LE, with its complete address staged for Shift_c. The
external data positions are now zero. No general slot or descriptor is
allocated for these data bits. Execute the SAME T1 then T2 and LE; the
latent label is the transformed data label. At data discard reset the
native data. For a retained phase output allocate ONE general zero slot,
SWAP the external control into it, and write its complete output handle.
Release/reset the whole external register as prescribed. On any abort
reset the same actual data/control regions before normal cleanup.

Conjugation by these explicitly counted SWAPs gives the original source
channel on control/data and arbitrary spectators. No acquisition is made
into an already allocated native zero and no copy is duplicated. Internal
source descriptors for the omitted old zero slots are absent, rather
than uncharged. The general allocator has fewer live slots; its original
capacity proof remains valid. Full P/HQ/DRAW prefix and general virgin=P
are unchanged. The O(n) fixed-address SWAPs cost O(n^(3/2)log n) even
with the older native driver; export/full handles cost O(n^(3/2)).

For exact T1 use the following clean Boolean implementation. The existing
five-product Toom recursion of typed_dispatch.md works at full root
width b, the least power of3 >=3n, with b<=9n. The child width is still
ceil(w/3)+3, base case w<=8, signs and exact interpolation divisions are
unchanged. The same recurrence and5^2<3^3 prove O(n^(3/2)) elementary
Boolean work, including its polynomial-in-log control allowance. To turn
it into a quantum circuit, give EVERY elementary Boolean result its own
fresh native zero wire. Unroll the fixed-size loops and replace signed
comparisons/branches by Boolean muxes. This is an acyclic straight-line
network with data-independent wiring and O(n^(3/2)) gates and used wires;
all operands and interpolation widths are functions of n alone.
Compute forward, CNOT the requested product into its target, and reverse
THE WHOLE network once. Do not recursively clean each child after each
recursive multiplication: that would double the recursive branching.
This global clean XOR oracle has constant times the original size.
Input words remain available until the final inverse, on every basis
input and with arbitrary spectators. Division by3 remains the explicit
constant-remainder bit network, never an arithmetic oracle.

The uniform emitter traverses the fixed circuit/recursion depth first,
with O(log^2 n) frame/index bits and constant many staged O(n)-bit words.
Use an immutable block layout per recursion node: five child blocks of
size S(ceil(w/3)+3), followed by fixed evaluation/interpolation arrays.
Their bases follow the bit-serial size recurrence S(w)=5S(child)+O(w).
Each ripple/add/compare bit uses a fixed local gate template with bases
plus constant times its position; child outputs have prescribed word
bases. No destructive-memory-to-wire map is stored. A node frame needs
only its width, block base, phase and child index, O(log n) bits, so the
O(log n)-deep emitter uses O(log^2 n) ordinary bits. All intermediate
Boolean wires stay in the counted native block until the WHOLE reverse.
Its gate positions and operand offsets are polynomial in n; their bit
formation can keep the older O(log n) driver per elementary gate. All
complete d-bit native arguments are initialized and consumed, so this
has the complete O(n^2) charged bound proved in the strict-recurrence
refinement below, including this driver. Quantum
scratch is the actual gate list's O(n^(3/2)) wires within the existing
P reservation, not ordinary storage. Reset only those used wires.

For an explicit finite-capacity implementation, compute the fixed circuit
size/layout BEFORE sources, with bit-serial recurrence counters, and use
this fast source path only if its complete used-region bound fits P
with disjoint data/control buffers. Otherwise use the preceding complete
schoolbook T1 controlled modular additions of virtual.md Section3,
the separate controlled QPE translations of approx_estimate.md, and
verifier schoolbook long division of verified_extract.md, at the same
fixed native registers. Direct entry/export and the new source cap still
apply; all fallback circuits have their explicitly retained O(n) scratch. This is a deterministic n-only guard; eventually every layout
fits since O(n^(3/2))=o(P). Its finitely many exceptional n retain the
old exact channel and terminating source caps and affect only absolute
constants. Bootstrap/guard work is polynomial. No unknown threshold is
consulted. The existing whole prefix already contains these positions.
The old local O(n)-scratch allowance is replaced for this fast arithmetic
by the explicit guarded O(n^(3/2)) quantum scratch inside counted P;
ordinary staged work and source recursion space stay as before.

Precompute mu=floor(2^(2n)/N) once per batch, using counted polynomial
schoolbook setup. For u=alpha*x<2^(2n), form
 q=floor(u*mu/2^(2n)), r_u=u-qN.
Because0<=u/N-u*mu/2^(2n)<1, floor(u/N)-q is0 or1. Thus
0<=r_u<2N, and one conditional subtraction produces exactly u mod N.
Three O(n)-width fast products plus linear additions/comparisons suffice.
Define f_alpha(x)=alpha*x mod N for x<N and x otherwise. It is a total
permutation on all n-bit encodings, with inverse f_(alpha^-1), since alpha
is coprime to N. Compute clean XOR f_alpha, swap input/output words and
clean XOR f_(alpha^-1) into the old input. This clears the old word on
ALL padded inputs and implements exact in-place Mult_alpha. Its constants
and inverse come from the unchanged once-per-batch Euclid/CRT setup.
The same constant-time number of full-width products gives charged
O(n^2) per T1 by that same strict bound. T2 stays the exact controlled ripple shift.

## Fused exact QPE translation and counted verifier

In MODE_QPE let m=n+ceil(log2(4096n)) as before. The commuting controlled
translations in approx_estimate.md have product
 |x>|u> -> |x>|u-x mod N>, 0<=u<N.
Compute x mod N by binary long division. Since x has m=n+O(log n) bits
and N>=2^(n-1), only O(log n) quotient positions exist. Each uses an
O(n)-bit subtraction/comparison/mux, giving O(n log n) Boolean gates.
A clean XOR oracle for (u-x mod N), swap and the clean inverse addition
implement the same permutation, extended by identity for u>=N. Copy and
reverse the entire fixed Boolean network, with O(n log n) used native
scratch; data-dependent branches are muxes, not addressed loads. This
uses the same guarded native region. It costs O(n^(3/2)(log n)^2) with
the conservative native driver. This replaces the n separate length-n
translation circuits; it does not approximate their joint unitary.

On chi_k with the source's positive-exponent convention it leaves data
and spectators unchanged and multiplies the |x> amplitude by
exp(2pi i xk/N), exactly the previous phase-estimation state. The inverse
QFT, truncation, synthesized ancilla rotations, template guards, rounding
and uniform1/(512n) error bound are unchanged. Their n poly(log n) work
may retain the older native driver and is O(n^2) charged eventually;
finitely many guarded MODE_RUN exceptions retain the preceding exact
routine. No approximation is applied to source data.

For verifier rh=floor(k_A2^G/N), set M=2n+T_V+48 and precompute
mu_M=floor(2^M/N) once. Since G=n+40+T_V and k_A<N,
u=k_A2^G<2^M. The exact quotient q=floor(u*mu_M/2^M) is at most
one below floor(u/N); test u-qN>=N and increment once. Full-width
Toom products implement this exactly. Their depth-first ordinary
worklist has active data <=4096b<=36864n plus O(log^2 n) metadata,
inside2^16 n bits under its deterministic size guard. Initialize/clear
that worklist once per product; keep source recursion banked.

verified_extract.md Section5.7 now implements the EXACT same prediction
sum by its counted private basis block cache. It proves O(n^2) per
verifier including all table construction/lookup/erasure, coins, modular
tests and scores. Ordinary fields remain rh/constants/candidates/counters
in constant-many n-bit chunks, RUN directions6(n+5), and one small
B*T_V window block. The cache itself is counted QUANTUM memory inside
P, with its n-only layout guard; no n*T_V ordinary table is introduced.
Private LE fields and the ordinary arithmetic worklist each use2^16 n;
compiler buffers and all other staging keep the total below2^20 n.

High-confidence RUN keeps its exact old translations and regular-pass
O(n^(5/2)h_e) per-call bound. The tighter EXECUTED fallback cap in
verified_extract.md is now ceil(4Qcap/n), with its separately proved
abort probability. Since h_e=O(r), its aggregate worst-case work is
O(n^2 Qcap)+poly(n). It is not an expected-runtime argument. The fast
cheap estimate and verifier cost O(n^2) per source, uniformly
over wrong-label branches; all per-copy frame/import/export costs fit.
Thus total source/preprocessing/extraction work is
 O(n^2 Qcap)+poly(n).
All ideal-source and spectator laws are exact except the unchanged
certified estimate-ancilla approximation. The new fallback cap is the
only changed success event, with the explicit coupling bound below.

## Full-width product with its complete physical driver

Retain the strict recurrence instead of first boxing it as a loose
O(n^(3/2)) raw bound. At root b=3^k=O(n), the existing full-width
five-product construction has at most C(k+1)^c 5^k elementary Boolean
gates/work bits and raw control steps, for a fixed absolute c.
Native/ordinary operand formation and generation use only polynomial
width coordinates and therefore add another fixed polynomial in k,
including all low-address bits, cursor control and complete buffer
updates. High physical address bits are initialized once per product/
source scope, as already specified. Every actual operation still pays
the COMPLETE d=Theta(r) addressed fee.

For ANY fixed exponent a, (k+1)^a 5^k=O((3^k)^(3/2)):
group k=2h+i and use25/27<1 to bound polynomial(h)*(25/27)^h.
Thus all raw gates AND their complete physical-driver bit steps
together are O(n^(3/2)); multiplying the mandatory fee d gives
O(n^2) charged work per full-width product. No physical fee vanishes:
the older separate logarithmic bound was absorbed by the strict
multiplication exponent gap BEFORE that mandatory fee is applied.
The same reasoning covers the ordinary depth-first product and the
whole clean SSA compute/copy/reverse construction, which still has
five children, not ten recursively cleaned children.

All complete input constants, first-worklist initialization, used-region
clearing, source direct entry/export and actual quantum resets fit this
bound or retain smaller polynomial per-copy terms. The guarded native
span and O(n) ordinary worklists are unchanged. The constant-number
Barrett products for exact T1 and rh therefore cost O(n^2) each.
Fused QPE plus compiled Fourier words have n poly(log n) core/driver
work and cost O(n^(3/2)poly(log n))=O(n^2) eventually. RUN with the
executed Cf=ceil(4Qcap/n) contributes O(n^2 Qcap)+poly(n) as before.
The block-table verifier has O(n^2) charged work per copy. Hence
the complete source/extraction total is O(n^2 Qcap)+poly(n).


## Actual short keys and scoped pool dictionary

Store a bucket key as the ACTUAL c-bit quotient
((t1-t0)/2^p) mod2^c, with one zero field when c=0, rather than an
n-bit residue with p zero low bits. Here c<=cb=O(r), and division by
2^p is a bit slice of a known divisible difference. Form that difference
from full 3n labels with counted word arithmetic once per insertion.
Numeric quotient order equals the old low-residue order, so bucket/FIFO
selection and every quantum input tuple are unchanged. All keys/counts/
links/heights/flags of the dictionary have actual O(r)-bit formats.
Key conversion preserves complete logical values; record padding remains
allocated and full first-write WROW clearing is paid per new row.

A dictionary search/update is one inline scope. Load all complete binding,
epoch/geometry/pc fields before entry; commit them before owner activation,
renumbering, call, return or abort. Activate owners before the traversal;
no owner is activated inside it. Each visit reads/writes constant many
actual short fields, including balance repair. Stable parent/item IDs and
the explicit rotations/transplants of bucket_level.md remain. There is
no full n-bit binding refresh PER node or a hidden recursive dispatcher.
All dynamic bit/cursor/address work retains the complete short-helper
O(n(log n)^(3/2)) bound. A traversal visits O(log Cin)=O(r) nodes, so
O(Cin) updates/searches cost O(n^(3/2)(log n)^(3/2) Cin).
Complete entry/exit bindings, labels, releases and first clears cost
O(n^(3/2) Cin), by the existing branchwise counts. Window/member/code
short work is O(n(log n)^(3/2) Cin), and is smaller. No unused or newly
allocated row is assumed prevalidated.

## Word-level tree tables and native serial lookups

Use actual D_T=8r+32-bit fields for all MERGE/MERGE4I residues, sort
keys, positions, counts, offsets, ranks, heap pointers and tuple indices.
All their values lie below2^(4Lam+4) or2^(4r+4): lam<=Lam<=r,
b<=4Lam, and four-tuple counts are <=2^(4Lam). Thus the new padded D_T
format is exact on EVERY branch. Full phase labels remain3n-bit words.
This changes the stored physical formats, not which bits are secretly
read from an unchanged n-bit field. All complete D_T bits/tags are
transferred. Wider p-bit collimation constants, label differences and
supplier scalars retain their full formats and counted word arithmetic.
WROW, all owner/row capacities and full allocated prefix remain unchanged.

Implement one record comparison/copy, heap sift, binary search or modular
short-word update as an inline scope: stage complete bindings once,
perform the actual-field bit code and commit before any external boundary.
Owners are activated before the fixed row traversal; renumbering occurs
only after commits and requires a fresh complete binding load at the next
entry. No full n-bit pc/descriptor fetch occurs per arithmetic bit or
per sift-node. Each key/tuple comparison and copy costs a constant number
of short helpers, O(n(log n)^(3/2)), including bit arithmetic and complete
addresses. Stable bottom-up merge-sort and heap operations visit
O(log L)=O(r) nodes/keys per emitted record. Binary searches also have
O(r) visits. Thus they cost O(n^(3/2)(log n)^(3/2)) per record. Full
label reads/sums/writes cost O(n^(3/2)) per record. First clears and
scope entry/exit/full binding commits also fit that record cost. Arbitrary
nonsequential row bindings read their complete actual stored row indices;
there is no QRAM, free word comparison or uncounted numeric tie breaker.
The original orders, tuple listing and cyclic window are identical.

At each binary/four-input MERGE, AFTER its children have returned and
before its first quantum step, move their O(r) index qubits by counted
SWAPs into fixed native positions. Read their complete general-slot
handles and keep the old slots allocated/zero until the merge completes.
Other quantum merge workspaces have fixed native layouts. No child,
source, LE or FW call occurs inside this native MERGE scope. On success
SWAP its output J into general output slots and free other old slots;
on failure/abort reset native data and release the original inputs.
All actual used scratch positions are cleared, never an uncounted whole
capacity. Quantum transfer/slot bookkeeping is polynomial per merge and
absorbed below; general capacity remains bounded by the original input/
output/scratch maximum. The same P prefix reserves all native positions,
which are zero before/after each merge. Suspended parent frames and child
tables stay banked; no growing ordinary source/merge stack is introduced.

For serial LOOKUP, table rows remain basis bank records at classically
known addresses. Read the complete O(r)-bit table payload via short
helpers. In fixed native index registers compute equality with the known
row index using its explicit O(r) clean Boolean circuit, apply controlled
XOR on payload bits, then uncompute equality. No superposed table index
is used as a physical bank address. Each row has O(r) actual native gates,
with full native driver O(r log n), hence O(n log n) plus its complete
short-field reads O(n(log n)^(3/2)). Polynomial register/cursor setup per
row fits the record allowance. Native operands are fixed-register bases
and known bit positions. Cyclic-window arithmetic may KEEP the original
polynomial circuit/generator per merge. Conjugating by entry/exit SWAPs
proves the same arbitrary-input instrument and Kraus maps, including
spectators. No source incidence or measurement law changes.

The precise inherited table skeleton is O(r C_ell 2^dl/dl) record-work
units per batch: its O(n) reference bit-work multiplier counts full label
passes and O(r) key visits of O(r) bits. The explicit word microprograms
above replace that bit multiplier with charged
O(n^(3/2)(log n)^(3/2)) per unit. Since dl>=r/2 and
C_ell=O(n2^H), each batch costs O(n^(5/2)(log n)^(3/2)2^(H+dl));
O(r) batches give O(n^3(log n)^(3/2)2^(H+dl)). Constant-many scratch/
owner/slot setup and the native window circuit are polynomial per actual
merge. Each merge's input length is at least2^dl, so any fixed polynomial
setup is absorbed by this row-work bound eventually. Retain the old
complete implementation at finitely many smaller lengths if a deterministic
size guard fails, exactly as for source layout; no success event is lost.
FW and tree native regions never overlap in time.

## Current weighted total

perm_fw.md Section8 replaces the private term by counted linear pair
functions O(n^(5/2)log n C_0) and full matching/key work
O(n^2(log n)^3 C_0). Pool word/short dictionary work is
O(n^(5/2)(log n)^(3/2) C_0), using sum Cin=O(n C_0).
Source preprocessing/extraction costs O(n^2 Qcap), with the
executed tighter fallback cap and its separate failure probability.
Decoder full-word work remains below these terms. Prefix work stays
O(n^2(HQ+DRAW+1)). Thus
 T<=c[n^(5/2)(log n)^(3/2) C_0+n^2(log n)^3 C_0
       +n^3(log n)^(3/2)2^(H+dl)
       +n^2 Qcap+n^2(HQ+DRAW+1)]+poly(n)
  =O(n^(43/4)(log2 n)^(3/2) 2^((7/6)sqrt n)).
This is o(n^(45/4)2^((7/6)sqrt n)). All four other complete structured
objects are identical. Exact finite guards do not consult a theoretical
threshold and affect only absolute constants. The new cap's coupling is
included in the same unconditional full-shift success budget.

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

The current source/tree/short-key sections above give the complete
n^(43/4)(log2 n)^(3/2) exponential-time ledger. These encoded-window
branchwise counts remain its transfer/metadata premises. All four other
complete structured objects and success >=1-2^-8 remain unchanged.
