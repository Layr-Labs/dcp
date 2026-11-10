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

## Physical interfaces

The final persistent-window section of native_ops.md replaces the old
per-request GROUP/code rewrite and coherent input-copy/clear loops.
The exact short-field format above remains. The complete persistent
address routine of typed_dispatch.md costs O(n) per valid
short tagged field, O(n^(3/2)) per n-bit word or S_R first clear.
Every EW tag and stored bit is streamed; every complete address is
initialized, updated and consumed with its mandatory fee. GROUP and
code owners persist for a chunk, with full first clears, complete binding
refresh at each native scope and no owner activation inside it. Native
postprocessing, release and code writes follow the explicit window
amortization and tagged-union discipline in native_ops.md.

## Current decoder implementation

distance_decoder.md specifies the normative scoped short-residue
algorithm. The odd-stage factor2^j cancels exactly, leaving Y+8-bit
residues. Candidate bases stay full-width at interval entry/exit;
per-candidate cursor, signed W, residue and score fields have explicit
short formats. All K records remain banked, and complete binding/epoch
loads occur once per fixed scope. Scores/order/ties are unchanged.
Each candidate costs O(n^(3/2)); all batches cost O(n^2 C_0)+poly(n).
No candidate is a memory index and no ordinary K*n-bit table is added.
