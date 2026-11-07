# HPC127-TAGBANK: linear classical staging with tagged records and an indexed quantum free list

## 0. One physical algorithm and joint theorem

For every N>=2,s in Z/NZ put n=ceil(log2N). The ONE physical
HPC127-TAGBANK algorithm below executes complete reference HPC-127 P
and recovers the WHOLE secret with unconditional probability>=1-2^-8
from independent ideal copies. On EVERY branch, including wrong labels,
failed/recycled pairs, failed merges, supplier/pool aborts, rejected or
discarded copies, initialization, source moves and final cleanup, jointly
 T=O(2^((127/100)*sqrt n)),
 S_C=O(n) ordinary classical bits,
 S_Q=O(2^((127/100)*sqrt n)) allocated qubits,
 Q=O(2^((127/100)*sqrt n)) total acquired DCP copies.
Outside constants are absolute, independent of N,s and outcomes.
Growth indices are[1/2,0,1/2,1/2]; only time scores[1/2].
The fifth supported expression is0 under the exact canonical model

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

Classical records become FULLY COUNTED basis qubits with classically
indexed reads/writes and lazy generation tags. Original P qubits have
an EXPONENTIAL counted pool with a banked indexed free list, not a
polynomial-pool scan per gate/allocation. Exact tag-overflow repair
preserves every logical record at every length with no new failure.
Coherent table queries remain serial circuits. No QRAM, source inverse,
priority, optimality, practical speed or cube-root-time claim is made.
This reduces ordinary classical space while preserving P's three pure
nonpolynomial envelopes. The original n<2^28 finite tester is retained.

## 1. Complete actual sources and scope

The complete selected reference P is HPC-127, actual public submission
2aad498c-d5e9-4f64-a222-3b2f7f961738, commit
d6409650e2278a5223ee123da8129582844c0b98. Its full39031-byte proof
SHA256b38778695dd757e374fbc9e0d45a3c8d853cb7f8158080600578de8c76efc32a
is reproduced BYTE-EXACTLY after the VIRTUAL-ONLY marker in virtual.md.
Every source/label/LE argument, recycling yield, integer schedule and
capacity, batch-exhaustion/fresh-input law, held-out-bit frequencies,
both full-modulus decoders, source cap, finite branch and unconditional
success argument is supplied. Its resource assertions concern virtual
P, not this different physical allocation. No historical JSON, verdict
or opaque theorem supplies mathematical acceptance.

P's headline states success>=1-2^-7. We use the STRONGER explicit
unconditional calculation in its Section13:
 failure<=2*2^-10+2^-20+3*2^-40<2^-8.
Its finite tester has error<=2^-10. Thus1-2^-8 here follows from the
supplied actual argument with no change in configuration or amplification.

The immediate local compiler predecessor is IFCS1310-TAGBANK, main
SHA256a5652df5cb9098207a1d7650aa2eef0cd13b41bcb2dbf8355529d1cba2c0820c.
Its fixed counted tagged spans, lazy arrays, exact finite-length overflow
repair, arbitrary correlated-CQ decoding and polynomial bit interpreter
are carried below. Its different saturated source is NOT run here.
That predecessor has only a polynomial original quantum pool; this
implementation separately supplies the EXPONENTIAL pool, indexed free
list, per-wire lifecycle charge and pointer-storage proof ofSection4.
Its actual public dependency identity must be mapped before upload;
no local verdict is a theorem premise.

The corrected directly consulted measured-bank method is LLV-GBANKQ25,
actualfbb8f36c-3904-4bf0-9ddf-e9f5d83657ae, commit
100a8e307fd90c489c4d90717613869fed576b3b, full main SHA256
08608c19bf8d7ba42b50cf01f86662bc4e38ae0de63a2825ed4f86c8f10ca7d0.
Its direct-wire bit operations, CQ/irreversible forgetting and complete
counted prefix are adapted. Its quarter-square-root source and unused
historical finishing comparison are not adopted. Tags and free lists
are standard programming ideas, not an invention claim.

P's full public proof/manifest and all five official proof bindings were
verified and all584 proof lines read. Current declaration/show/history
views were read in full: two pending declarations, no applied edges or
cursor. Pending is neither verified ancestry nor false. All P credits,
including CS1 f1481815-9577-4990-abe3-7b79fa5d9284, PSieve
4256e671-97b0-4f84-82ce-12aeee17224e and Kuperberg, remain in its full
body. Historical first-person text denotes original authors. The bank
method's PSG21/PSG2-QSTORE credits remain. No IFC phase algorithm,
external quantum walk or positive-corruption theorem is selected.
All material public endpoints require exact-file both-endpoint citations.

## 2. Exactly selected source, schedules and finite branch

For n<2^28 run P's original exhaustive tester. In candidate order0..N-1
use up to n+10 fresh copies, Shift_candidate and X measurement; reject
on the first minus and output the first passing candidate, or0. The
true candidate always passes and each wrong one passes a fresh test
with probability1/2, so error<=2^-10. Stream with O(n) ordinary bits
and O(n) qubits. The finite prefix changes only outside constants.

For n>=2^28 execute EXACTLY full P, with public integer parameters
 r=ceil(sqrt n), ell=ceil(31r/100), m=ceil(389r/500),
 dl=ceil(491r/1000), kappa=ceil(log2m)+1,
 K=2^13*(2r+ceil(log2n)+30),
 C_ell=2^12*n*K*2^m*dl,
 C_i=ceil(3*ell*C_(i+1)/(ell-1)),i=ell-1,...,0,
 Y=ceil(log2C_0),Qcap=4*n*C_0+K.
All are computed by exact integer arithmetic, no real-log/square-root
oracle. Compute C_0 streamed using one current C_i word. Before the
bank exists no ell-word parameter array is stored ordinarily. After
initialization recompute/store any needed C_i profile in the bank.
All intermediate public words have O(n) bits by P's exact boundY<=2r.

Keep the exact greedy pairing-first/reverse-tree bit allocation of P
Section8 for each requested1<=B<=n, each lam_i=dl+i, root exponent1,
PAIR/PAIRLEVEL roundsY+1, sort/recycle/trim order, supplier4C_0 cap,
BATCH exhaustion, K-root measurement schedules, both decoders, and LE
precision sized by the literal Qcap. All original ABORT paths output0.
The source cap needs no new stopping guard. Wrong extracted labels do
not alter fixed capacities or loop limits. Every source request and
original quantum instrument remains at its logical point.

Use finite streamed bit code for arithmetic, stable merge sort, flat
lists, lookup circuit generation and all classical operations. Resolve
unspecified equal-key ties by original LOGICAL list/row order, never
physical pool IDs or bank addresses. Source labels, table indices,
residue keys, domains and masks are unchanged. Full labels have3n-bit
fields; signed differences use O(n) bits. Classical wire handles are
opaque identity tokens, used only to address known original qubits.
Passing a pool qubit/vector transfers its handle; it does not clone it.
Loop/return contexts, code-generation state and all large records are
banked. Only constant-many O(n)-bit operands are staged at once.

## 3. Fixed complete basis capacities for P and pool metadata

Define U=C_0+2^(dl+m)+1. The exact source code gives on EVERY branch:
 - pool/live/output/sort arrays have at most O(C_0) rows;
 - at most3 retained phase tables per tree depth, each<=2^(dl+m) rows;
 - binary merge order,pos,lo,cnt,off,Dx and inverse-block scratch use
   O(2^(dl+m)) rows, never all input pairs;
 - ell,m,K,dl,Y and all logical fields/frame depths are polynomial;
 - source label/difference/address words have O(n) bits;
 - the coherent pool has at most C_0 qubits, tree pending indices at
   most2(m+1)(dl+m), and a fixed number of O(n) scratch registers.
These remain fixed with wrong labels, bad pairing yield, failed merges
and supplier/pool aborts. All original rows are supplied in virtual.md.

Use A=2^16*n^2 reusable named array owners and Wrow=2^16*n^2 logical
bit cells per row. Let
 R=2^24*n^4*U rows per owner,
 H=2^20*n^2*U original quantum slots.
R/H=16n^2. Pool metadata arrays of H rows therefore fit R. There are
fewer than512 named array/frame/helper families per depth; depths<=n,
plus K records, constant profile/decoder/allocator arrays and scalar
scratch. Thus A exceeds their simultaneous count for n>=2^28. Scalar
helpers share fixed families/rows, not one owner per individual pool
qubit or table entry. Every actual source array has at most a constant
multiple of U rows; the conservative n^4 factor also covers polynomial
scratch and all quantum-descriptor/free-list rows. Actual lengths and
field widths stay P's; padded capacity creates no extra tuples.

Constant-many ordinary O(n)-bit fields fit Wrow. A quantum-register
descriptor may contain O(n) slot IDs of O(n) bits each, so its ENTIRE
O(n^2)-bit row is also counted and streamed. Source depth-first frames,
profile arrays, numerical helpers and gate contexts fit the same
counted owners; return contexts never form a duplicate classical stack.
Stable address(owner,row,bit)=owner*R*Wrow+row*Wrow+bit yields maximum
complete logical span
 B=A*R*Wrow=2^56*n^8*U.                            (3.1)
Every inactive owner/row/field and directory binding is counted.
Known owner selection can scan A=O(n^2) entries, a polynomial cost.
Original logical equality/aliasing/ties do not inspect physical IDs.
Per-row metadata initialization clears at most Wrow polynomial cells,
not a whole owner. Source array ALLOC/FREE use lazy tags inSection5.
Quantum slot allocation is a DIFFERENT operation given inSection4.

## 4. All tagged spans and the EXPONENTIAL quantum pool are counted

Set e=(n+2)^20 BITS per epoch value. Every logical bit cell has one
basis value and e basis tag bits. RAW basis regions hold each owner's
epoch and active/binding fields, one global e-bit G_tag, one e-bit
backup and fixed raw interpreter state. These RAW records are not
tag-recursive. Take the conservative complete raw-basis span
 D=B*(e+1)+(A+8)*e+A+2^20*n^4.
For a flattened logical bitc<B, value is RAW slot(e+1)*c and tag
bit t<e is RAW slot(e+1)*c+1+t. Owner epoch words, G_tag and backup
follow the COMPLETE B*(e+1) span at fixed raw offsets; flags/bindings
and raw scratch occupy the remaining explicitly reserved ranges.
These formulas are injective and every endpoint is below D.
All source and quantum free-list/descriptor arrays are logical BIG
records already counted in B, not an additional uncounted map. Epoch
values are never e-bit ordinary classical operands: compare/copy/
increment them bit-serially with reusable bits/carry and O(log e)
loop indices. Owner bindings of O(n) bits fit the counted raw n^4 span.

RAW j is physical even wire2j. Original quantum slot k<H is physical
odd wire2(k+1)+1; reserve odd1 for a fair bit. Let h be the least power
of two at leastmax(D,H+1,2). Allocate and initialize the WHOLE prefix
0,...,2h-1 before running P. All even/odd unused padding and inactive
slots count. The persistent global owner starts at epoch1,G_tag=1.
One additional temporary source register of n+1 wires is counted; each
P request acquires ONE rho_s, SWAPs it into freshly mapped zero source
slots, and releases the zero temporary. SWAP is three CNOTs per qubit,
all addresses charged. Prefix zeros/metadata are not DCP source copies.

Quantum slot allocator. Store head, nonempty flag and virgin counter
in counted global logical fields. Store next[k] and active/ownership
fields in a constant number of fixed BIG metadata arrays, each of H
rows (H<R), not one BIG owner per qubit. Initially head is empty and
virgin=0; no H-entry free list is materialized classically. ALLOC_Q:
if head is nonempty, pop k=head and set head=next[k]; otherwise use
k=virgin and increment virgin. Record the slot ID in the appropriate
P pool/list/vector descriptor. A freed slot has been reset to zero.
FREE_Q(k) traces out/resets ONLY that actual released original qubit,
writes next[k]=head and pushes k. No H scan occurs. All head/next/
virgin operations are known-index banked word operations of O(n) bits.
New metadata row fields are initialized by polynomial bit loops.

Pool ownership invariant: all indices below virgin partition into
injectively mapped LIVE original P wires and the free stack. The free
stack has no duplicates and contains only zero qubits; indices at or
above virgin are untouched zeros. Distinct P wire identities are
mapped injectively; returning/passing register handles preserves
aliases and transfers ownership. FREE_Q is executed only when the
original logical wire is dead, never merely when another alias is
dropped or a register is returned. A gate reads its operand slot IDs
from banked descriptors and addresses those known odd wires directly.
Stable logical row order, not slot-number order, resolves pairing ties.
Thus no source measurement, phase index or table key is changed.

There is always a slot. Full P bounds its coherent pool by C_0 and
pending indices by2(m+1)(dl+m); current merge/LE/transform scratch is a
fixed set of O(n)-bit registers implemented by ripple bit circuits.
Even reserving512 named scratch registers of4n bits and2n^2 pending
slots is below C_0+2^16*n^2, which is below H. If virgin=H and the free
stack were empty, all H slots would be live, contradicting this bound.
No runtime failure guard or extra source request is introduced.

Lifecycle charge: pool slots are born through acquired source/control
registers; leaf tables TRANSFER existing pooled qubits; PAIR transfers
A and measures/resets B; MERGE transfers/re-indexes its retained index
register and releases only actual dead wires. Extra scratch/registers
have O(n) bits per logical operation/frame. Filling/refreshing source
pool qubits is charged to Q, while a repeated scratch creation or reset
is charged to its source bit/gate/loop operation. Therefore actual
wire allocate/free/reset/descriptor events number at most
 poly(n)*(C_P+Qcap+H+1),
where C_P is P's elementary operation count. Full H padding is prepared
ONCE at initialization and cleared ONCE at termination; it is never
scanned on each gate, object allocation, root, source request or batch.
The original fixed loops bound all helper/frame events. Each actual
wire event and descriptor access costs polynomial tagged bit work.

All complete address words have O(n) bits: log2U=O(sqrt n+log n),
log2(D+H+2)=O(sqrt n+log n). Numeric e and epoch loop indices have
O(log n) bits even though an epoch VALUE has e stored bits. Public
parameter/address computation uses charged schoolbook bit operations
with O(n) staging. The free stack is metadata in counted qubits, not
an uncounted classical or coherent memory oracle. All original coherent
LOOKUPs remain their full serial known-row circuits inSection5.

## 5. Explicit indexed bit and lazy-array operations

RAW_READ(j) measures known even wire2j in Z into one reusable classical
bit. RAW_WRITE(j,b) reads old z, applies X iff z differs from b, then
forgets z after use. All addresses are CLASSICAL known words. No gate
is addressed by a superposed bank index, and no coherent dictionary
or RAM operation is assumed. Bit arithmetic and loop/address generation
are charged. Source classical Boolean gates become a fixed number of
such reads/writes; logical multi-bit operations remain explicit loops.

READ(owner,i): compare that cell's tag with the owner's current epoch,
bit by bit, using a reusable equality bit. On equality return its stored
value; otherwise return0. All temporary raw outcomes are forgotten.
WRITE(owner,i,b): set the value by RAW_WRITE, then copy the owner's
current epoch into the tag bit-serially. Intermediate physical substeps
are internal to this logical primitive; no P step or source call is
interleaved. Initial tags are0 and active epochs are nonzero.

ALLOC chooses a free owner. Before using a new generation, if G_tag is
all ones run the exact renumbering of Section6. Increment G_tag bit-serially
and copy it into the owner's epoch; mark that owner active. NO per-cell
clear is performed. All its old tags differ from the fresh generation,
so every unwritten cell logically reads0. FREE marks the logical owner
inactive and drops the logical reference; its old data/tags remain
counted ignored junk. The next allocation gets a new generation. Do not
erase an exponential array on each free/retry.

This realizes zero-initialized classical arrays. Where source code only
specifies fresh scratch, the zero convention is a valid fixed completion;
every logically used source entry is initialized or checked as specified.
P's row domains, lengths, bounds checks and masks are unchanged: padding
does not create extra tuples or circuit rows. Logical copies/updates
retain their original bit loops and logical aliasing. Return/pass of an
array transfers its owner handle; retained siblings keep distinct live
owners. The source's discard-and-rebuild rule never reuses a released
logical input as an accepted new one.

P's LOOKUP is STILL its original SERIAL known-row circuit. For each
known row/bit, READ that logical table bit and emit the SAME controlled
gate on P's original quantum index/equality/output registers. A
superposed P index is not a bank address. Heap and stream accesses are
classically selected. Every source gate, coin, measurement, guard,
failure and retry executes at the specified logical point. No subtree
construction or source request is placed inside a quantum lookup.

Only constant-many O(n)-bit operands, public address words/current frame
location, finite control and bit-serial helper counters are ordinary
classical storage. All original long arrays, scalar records, recursion/
return frames, generator contexts, loop/cap counters and allocator state
remain in counted basis memory. The fixed code generates instructions
online. There is no growing classical transcript or physical call stack.

## 6. Exact overflow renumbering, with no additional failure

We do NOT assume a counter can never wrap at every input length.
The e-bit G_tag represents0,...,2^e-1, tested by a bit-serial all-ones scan;
2^e need not be materialized as an ordinary classical integer. If ALLOC
needs a new generation when G_tag is maximal, PAUSE P and do the following.

For each owner j=0,...,A-1:
 - If active, copy its OLD epoch into the counted raw backup word.
   For every one of its R*Wrow cells, compute the OLD decoded value
   using that backup; store this value and replace its tag by j+1,
   padded to e bits. Only after all cells set its owner epoch to j+1.
 - If inactive, set all its values/tags and epoch to0.
Then set G_tag=A, clear/reuse the backup, and resume the requested ALLOC.

A+2<2^e, so there is room for another generation. This is a finite
exact reencoding of the SAME logical record, including unwritten cells;
it adds no abort, accepted event, source request or probability error.
It clears stale generations even in inactive owners. Afterward every
stored tag is at most A, current active epochs are j+1, and G_tag=A.
Until the next renumbering every new generation exceeds all prior tags.
Inductively ALLOC's unwritten cells always decode0; WRITE stamps the
current owner generation; FREE cannot expose stale data. Repeated wraps
are handled in exactly the same way. It makes progress after every wrap
and does not rely on unknown constants in a resource estimate.

During this scan store the old epoch only in the raw backup, not in
an e-bit classical register. Loop indices for owners/cells/epoch bits
are O(n)-bit words. No P quantum operation or source query occurs until
the reencoding ends. The source's live original quantum registers can
remain untouched throughout. Cost is D*poly(n); space is the fixed
prefix plus the already counted backup/short staging. It is NOT claimed
to be a cheap operation if triggered at a finite small length.

## 7. Decoded correlated-CQ invariant and full correctness

At aligned logical steps, including any arbitrary reference R, the
physical state is of the form
 sum_z p_z |z><z|_(basis bank/raw metadata) tensor rho_z_(mapped P quantum,R),
with short finite control/staged classical fields included as necessary.
The basis records may be correlated with the phase/query registers and
R. No product-state assumption between bank and quantum data is made.
Tags, obsolete values, unused padding and released records are included
in z and remain counted; they need not be independent of retained data.

The quantum component of pi also uses the counted live descriptor map
to relabel each injectively assigned physical slot as its original P
wire, and traces out free/padding slots. Section4 proves this map
remains injective and respects ownership/aliasing through every actual
quantum allocation, transfer and release. Allocate pops a zero free slot
or uses a virgin zero; release applies the same trace-out/zero channel.
These identities hold with arbitrary entangled references, by linearity.

Define pi by decoding active logical arrays through their current epochs,
keeping P's logical control/object bindings and mapped quantum registers,
and forgetting all physical-only tags/allocator details/junk. Thus the
conditional P state for logical record c is the mixture over every z
with decoded record c, not one selected physical history.

Initially this gives P's prescribed input and zero scratch. On a basis
branch, each logical READ returns exactly its decoded bit. RAW Z reads
leave a CQ state unchanged nonselectively; they may reveal a branch
label to a short helper, which is then forgotten. Boolean updates and
WRITE change the decoded record just as P requests. When old records
merge after overwriting or forgetting, their conditional quantum states
mix exactly as classical irreversible forgetting requires. ALLOC decodes
to a fresh zero array; FREE drops just the logical object; renumbering
has the same decoded record on every basis branch. Extra obsolete
records are never passed as logical operands. By linearity these
identities hold for arbitrary conditional rho_z and arbitrary R.

Original quantum gates and classically controlled serial LOOKUP have
P's same conditional action on its quantum registers. Original
measurements/coins have the same instruments. Reset/discard is trace-out
followed by fresh zero even with references; use that allowed channel,
or Z measurement, conditional X and forgetting, on mapped slots.
Every ideal fresh source supplies the same independent rho_s and the
SWAP map preserves it exactly. Consequently at aligned steps
 pi o Phi_physical = Phi_P o pi,
including all actual extraction-error, recycled/failed pairing, failed-merge, partial-child,
rejected-source and abort branches. The complete reduced logical state,
unconditional output law and source-request sequence equal P's.

In particular the FULL virtual Sections3-13 establish unconditional
whole-secret recovery at least1-2^-8 for every N,s: their latent-label
and LE coupling, recycling yield, conditional incidence/root-frequency
law, supplier/pool/source caps, both all-modulus decoders and finite tester
are all present. No prior review is a theorem premise. We do NOT claim
their held-out-bit failure bounds conditional on every new helper
measurement transcript; those extra outcomes are marginalized by pi.
The logical distribution is what is preserved. Under a different
adaptive malformed supplier model such extra measurements could matter;
no positive robustness or such transfer is asserted here.

## 8. Complete physical classical and quantum bounds

Ordinary input/output, constant-many O(n)-bit operands/addresses/current
frame words, finite code control and reusable bits/indices require
O(n) ordinary classical bits. Every source label, pool/list/table,
frame, long counter, profile/decoder/generator state and quantum
free-list/descriptor field is banked. Epoch values are processed in
place, not held as e-bit classical operands. Whole parameter profiles
are recomputed/streamed until the bank exists. Thus S_C=O(n) on every
branch, including source staging and final output coexistence.

The WHOLE prefix and temporary source wires give
 S_Q<=2h+O(n)=O(D+H+n).
Put b0=126947/100000, an EXACT rational1.26947. P Sections8,14 prove
 PP=3^ell*2^m=O(2^(b0*sqrt n)),
 C_0=O(n^2*PP), 2^(dl+m)=O(2^((1269/1000)*sqrt n)).
Thus U=O(n^2*2^(b0*sqrt n)), B=O(n^10*2^(b0*sqrt n)),
D=O(n^30*2^(b0*sqrt n)), H=O(n^4*2^(b0*sqrt n)).
The STRICT rational gap127/100-b0=53/100000 absorbs30log2n and all
fixed polynomial factors. Hence the exact PURE quantum envelope
 S_Q=O(2^((127/100)*sqrt n)).
Original coherent states, full tag/raw metadata, free-list pointer
arrays, inactive values, unused owners/rows/fields/pool slots, backup,
input copies, all prefix rounding/padding and source temporaries count.
This is a maximum-address-span guarantee, not expected occupancy or
a successful-label branch estimate. Source wrong-label/cap/abort paths
have the same fixed spans. No lifetime-growing physical addresses exist.

## 9. Charged known-index operations and exact overflow handling

Every physical gate/measurement/bit action pays its FULL address debit
ceil(log2(S_C+S_Q+2))=O(sqrt n+log n)<=O(n). All operand/wire/owner
indices are O(n)-bit known classical words. Address arithmetic uses
schoolbook bit loops with O(n) ordinary staging. A logical bank bit
uses e=O(n^20) raw tag comparisons/copies; a logical O(n)-bit word
repeats those bit operations. A=O(n^2) owner-directory scans and row
field decoding are polynomial. Original serial array/gate-generation
loops remain actual P loops, never a unit-cost coherent fetch.

A quantum gate obtains its current operand IDs from banked descriptor
fields, then uses the SAME original gate on the corresponding known
odd wires. Quantum slot/free-list/ownership operations have polynomial
known-index word overhead bySection4. They do NOT scan the exponential
H pool. All long descriptor lists, arithmetic and recursion scratch are
streamed from the bank. No ordinary huge call stack, free list, epoch
word or gate/circuit description is stored. Fixed ripple/bit templates,
epoch loops, A-directory scans and slot operations fit a conservative
O(n^100) charged overhead per old elementary/helper or actual wire event.

Let C_P count the original P core actions and fixed-loop instructions.
Full P gives C_P<=poly(n)*2^(b0*sqrt n) on every branch. The finite
interpreter and Section4 lifecycle bound add only polynomially many
logical allocations per C_P+Qcap+H+1. Their logarithm is O(sqrt n),
uniformly over ALL branches. The e=(n+2)^20-bit generation capacity
therefore eventually exceeds every generation used in the whole run;
for all sufficiently large n NO overflow renumbering occurs. This is
an analytical eventual statement, not a runtime threshold or assertion
that small lengths can never wrap.

At ALL remaining finite lengths actual overflow invokes Section6:
backup old epochs, decode each whole owner before stamping its new
epoch, clear inactive stale tags, set G_tag=A and make progress. It
preserves every logical record and counted free-list pointer while
leaving ALL live original quantum slots untouched. It adds no source,
failure, postselection or success conditioning. Its finite charged
scan costs D*poly(n), using the same counted backup/prefix and short
staging. Finite deterministic source/loop budgets bound the number
of such actual events. No verdict or manufactured acknowledgment is
used as a mathematical premise for any of these bounds.

## 10. Exact time and one-for-one acquired copies

Eventually renumbering is absent and all charged physical work is
 T_physical<=poly(n)*(T_P+Qcap+D+H+1).
This includes complete initialization, original unsuccessful work,
all indexed bit/gate/descriptor/pool work, every source move, and
output-first whole-prefix cleanup. It does not multiply a bank size
onto each P operation or charge H on every quantum allocation.
The full supplied P proves, on EVERY branch,
 T_P=O(n^6*2^(b0*sqrt n)), Qcap=O(n^3*2^(b0*sqrt n)),
where b0=126947/100000<127/100. D,H have the same strictly smaller
leading coefficient b0 and polynomial factors bySection8. The exact
gap53/100000 times sqrt n dominates EVERY fixed c log2n. Hence
 T=O(2^((127/100)*sqrt n))
with the EXACT declared rational coefficient and no unspecified
polynomial. Each remaining fixed finite length has finite uniform
branchwise work, including actual overflow repair and the original
finite tester. Their finite maximum ratio changes only one outside
constant. No altered sufficient-range branch, hidden advice or
postselected fast execution is used.

Exactly ONE physical DCP acquisition executes each P request, and no
others. The original literal capQcap=4*n*C_0+K counts every rejected
supplier sample, failed/recycled pairing, discarded merge input and
batch/supplier abort. Tag repair, fresh bank/pool padding zeros,
metadata and source SWAPs are counted gates/storage, not extra source
copies. Thus Q=Q_P=O(n^3*2^(b0*sqrt n)), and the SAME strict rational
gap gives
 Q=O(2^((127/100)*sqrt n)).
All source precision, fixed rounds, cap and output/abort laws are
preserved. Every resource and unconditional success concern this
SAME physical implementation, never separately tuned configurations.

## 11. Exact indices and scope

Time, full quantum allocation and acquired-copy envelopes each equal
2^((127/100)*sqrt n) and have exact growth index1/2. Ordinary classical
n has index0. Only time scores[1/2]. These are indices of proved upper
envelopes, not lower bounds or optimality. The fifth supported fraction0
has the exact independent-ideal-copy model stated above; all five
claims hold jointly with unconditional WHOLE-secret success>=1-2^-8.
No positive robustness or impossibility of greater tolerance is inferred.

The entire recycling-pairing/collimation source and measured-basis/CQ
methods are credited prior work. This supplies an explicit counted
linear-classical implementation, extending the tagged bank to an
exponential ORIGINAL quantum pool through an indexed banked free list
and separately charged wire lifecycles. Standard tags/free lists are
not claimed as inventions. The three pure nonpolynomial envelopes of
P are preserved, while its exponential ordinary classical allocation
becomes O(n). No dominance over linear-quantum-space algorithms,
practical forecast, priority, optimality or cube-root-time claim is made.

