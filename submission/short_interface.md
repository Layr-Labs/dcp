# Short stored LIVE slots and a scoped native interface (normative)

This refines the complete native_ops.md implementation. All circuits,
source transformations, caps, probability bounds and prefix capacities
are unchanged. Only a physical LIVE field format, the interface/record
microprogram and decoder word implementation change.

## Exact short field format

Compute d=ceil(log2(4h+2^22 n+8)) from the same predefined h. It is an
explicit upper bound on the complete physical address width, d=O(r),
d<=n, and HQ<2^d on the main branch. Store the LIVE item's physical
quantum slot number in exactly d bits, replacing that physical field's
old n-bit format. Its logical decoding zero-extends to n bits. This is
a new actual stored field, not a read of only the meaningful bits of
an unchanged n-bit record. Every allocated slot is below HQ on all
branches; induction on imports, handle transfers and releases establishes
exact decoding, without assuming extracted labels are correct.

Labels remain 3n-bit fields and nullable links keep Y_i bits. Other pool/
OUTPUT/buffer slot fields, general register descriptors and persistent
head/virgin/NEXT may KEEP their full n-bit formats. Importing a pool
record reads its complete old n-bit slot field and writes the d-bit LIVE
field; exporting a retained output zero-extends and writes the complete
old n-bit field. These conversions cost O(n^2) per record. The finite
row-format id specifies each new field offset/length from n,d,Y_i.
Adjacent fields are preserved; full WROW remains allocated and cleared
on a fresh-row write. ROWS, OWN, HQ, DRAW, h and every counted prefix
bit are unchanged. LIVE rows still fit the old10n-bit upper allowance.

## Fixed scope and persistent short streams

GROUP and the measured item-code arrays belong to the FWLEVEL chunk,
with their owners activated before the first FW entry and retained
until that chunk ends. Allocate them only if a w-input request occurs;
then Cin>=w. They have w rows and constant many fields per row, as before.
Reuse their valid rows without deactivation between FW calls. Every FW
writes EVERY GROUP id and every complete item-code field, including
sentinel/default values, before those fields are used. There is no
stale partial-code promise. First writes still clear every WROW bit.

At EACH native FW call entry, commit the outer frame and load complete
pc, owner-binding, format and epoch fields, including the full eight-field
binding records, at O(n^2) cost. Stage GROUP/LIVE/code owner ids, geometry,
epochs and fixed format parameters in constant many O(n)-bit words.
Refresh these fields after every possible outer renumbering. The native
interface is a fixed loop microprogram, not a sequence of recursive
mapped dispatches that reloads n-bit pc/binding fields for each input
CNOT. No owner is activated inside this scope. Commit all changed frame
fields before return, call, abort or an epoch fallback; caches never
survive a scope boundary.

A valid short field uses the exact blocked short-stride multiplier and
complete persistent-address routine of typed_dispatch.md. Its row product
costs O(n(log n)^(8/5)), including the bounded ordinary worklist.
Every EW tag bit and all L=O(r) stored bits are streamed through a fully
initialized d-bit argument buffer. Carry updates and mandatory address
consumption cost O(d(L+d)log n). Thus a short helper costs
O(n(log n)^(8/5)); complete n-bit fields cost O(n^(3/2)log n). Full scope
bindings are loaded before entry and caches obey the retained boundaries.
A GROUP Y_i id followed by its LIVE d-bit slot uses these helpers;
actual wire2k+3 formation/delivery is fully charged too.

On the FIRST write to a GROUP/code row in this chunk, clearing WROW
costs O(n^(3/2)log n). There are only w such rows per array: the initialization
charge is O(n^(3/2)log n w)<=O(n^(3/2)log n Cin), once per chunk, not per FW. Later writes
to valid rows use the short bound. Code fields have b_w+1 bits; measure
one complete field into a staged word and write it as one actual-field
stream. There is no bank helper for each measured bit. Source/code
overlap stages the complete field before writes. Renumbering preserves
active row meanings and refreshes bindings at the next aligned entry;
the finite exceptional-length fallback remains exact.

The two coherent input-copy passes of native_ops.md now cost
O(w n(log n)^(8/5))=O(n^2(log n)^(8/5)) per request. The same scoped interface resolves
the actual CNOT/NOT postprocessing operands at that bound; LIVE fields
are frozen through input copy/clear and instrument computation. Reset/
release uses the existing full FREE_Q helper, O(n^(3/2)log n) per CONSUMED qubit.
Returned qubits are never released. The sum-rho bound charges these
releases and label word operations by O(n^(3/2)log n Cin), not w per request.

GROUP and code streams also cost O(n^2(log n)^(8/5)) per request after their
once-per-chunk clear. At most Cin requests occur. AVL visits retain complete n-bit keys and word helpers, costing
O(n^(3/2)log n log(Cin) Cin)<=O(n^2 log n Cin).
Including imports, exports, scope commits, first clears and cleanup,
all metadata/interfaces cost O(n^2(log n)^(8/5) Cin) per chunk, globally
O(n^3(log n)^(8/5) C_0). Native key/body work is
O(n^(5/2)(log n)^5 C_0)<=O(n^3 C_0), as proved in typed_dispatch.md.

## Decoder word implementation

Keep the exact candidate order, score, tie rule and incremental residue
algorithm of distance_decoder.md. Each candidate visits K banked records.
Load complete frequency/residue fields, update each residue by one
bit-serial word addition modulo2^P_j (or2^b), and commit its actual field.
P_j=j+Y+8<=2n on the main branch; signed frequencies and fixed larger
records use at most three n-bit chunks. Carries and top-bit masking are
explicit and preserve adjoining fields. Each record therefore costs
O(n^(3/2)log n) with the persistent-address word microprogram, not a mapped dispatch per
arithmetic bit. This does not give a free n-bit multiplication.

The tab score uses the high12 residue bits and the fixed4096-entry
20-bit rational table, computed by the retained preprocessing. That
constant table fits the ordinary staging allowance for n>=2^40. Read
its bits with their full physical fees; even a linear scan of its fixed
size introduces only an absolute constant. Score sums, candidate scalar
and current maximum use constant many staged n-bit words, with explicit
word additions/comparisons, with every bit/address charged. All K frequencies/residues stay banked; no
O(Kn)-bit ordinary array is introduced. LE/FW private workspace is inactive
and reused. All ordinary staging remains within the old2^20 n margin.

There are O(C_0) candidates per batch. Hence decoding costs O(n^(3/2)log n K C_0)
per batch and O(n^(5/2)log n C_0) over O(r) batches. At the at most two interval
boundaries compute initial products with the original counted schoolbook
bit algorithm: K times polynomial work per batch, polynomial in total.
The 2-adic decoder uses the same incremental residues. No candidate is
a memory index, and no source or arithmetic outcome is assumed correct
for the work bound.

## Joint result and correspondence

The decoder and field changes preserve each logical value exactly.
Native FW still clears its coherent input copy BEFORE measurements,
with the identical arbitrary-input instrument. All source, held-out-bit,
distance, fallback/key couplings and success budgets remain unchanged.
Owner/slot availability is unchanged; persistent chunk arrays add no
new family beyond the retained fixed GROUP/code owners. Their w rows
fit Cin<=2^cb. Scope changes preserve the decoded state at every committed
boundary and perform all required zeroing. The full quantum prefix is
still counted, including unused and shortened-field padding capacity.

The current weighted ledger is

 T<=c[n^3(log n)^(8/5) C_0+n^4 log n 2^(H+dl)+n^(5/2)log n Qcap
       +n^2(HQ+DRAW+1)]+poly(n).

Use C_0=O(n PP), Qcap=O(n^(3/2)PP) and
PP,2^(H+dl)=O(n^(29/4)2^((7/6)sqrt n)).
This gives T=O(n^(45/4)(log2 n)^(8/5) 2^((7/6)sqrt n)).
All actual unsuccessful branches, initialization, reset, address
generation, preprocessing and exact finite fallbacks are included.
The other four complete structured objects are identical to the parent.
