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
per batch and O(n^(5/2)C_0) over O(r) batches. At the at most two interval
boundaries compute initial products with the original counted schoolbook
bit algorithm: K times polynomial work per batch, polynomial in total.
The 2-adic decoder uses the same incremental residues. No candidate is
a memory index, and no source or arithmetic outcome is assumed correct
for the work bound.

