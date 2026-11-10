# Work-conserving FWLEVEL (normative P Section7.2)

This file replaces the round-sort FWLEVEL section of the reproduced source.
The FW instrument and its phase-independent type law remain P Section7.1.
The yield proof below adapts the retained conditional-type argument to an
explicit work-conserving key-bucket implementation; it does not assume a
new outcome law or independence of adaptively selected groups.

## Algorithm and records

FWLEVEL(pool,Cin,p,c) receives Cin labeled qubits collimated to p and puts
E=2^c. The key of (t0,t1) is (t1-t0) mod2^(p+c), an n-bit value. Since the
difference is divisible by2^p, there are at most E keys. Keep a LIVE heap
of item records, one FIFO per nonempty key, and an OUTPUT list. Move input
qubits by handle into the heap; copying a classical handle does not clone
a qubit or release its slot.

Each item row has two 3n-bit labels, one n-bit quantum reference, prev/next
FIFO pointers and its bucket pointer: at most10n bits. Each bucket row has
key, left/right/parent AVL pointers, height, item count, FIFO head/tail and
an augmented eligible flag: at most12n bits. A nullable metadata pointer
is0, and row i is encoded i+1. Free item/bucket rows are managed by indexed
free stacks; freed fields are overwritten before reuse. Put Y_i=ceil(log2(Cin+1))<=2r+1. All nullable item/bucket links,
heights and counts use their Y_i meaningful bits, with the same bounds
and null encoding. Labels and quantum slot fields retain their full
3n/n-bit widths. A GROUP row contains ONLY a Y_i-bit item-row id.
Following the FIFO reads a Y_i-bit next field. GROUP copies neither
labels nor slot fields. OUTPUT rows still fit7n bits.
All of these arrays have at most Cin rows, including GROUP because it is
used only when Cin>=w. Frame fields hold their roots/free heads/counts.
No dense array over all possible keys is allocated.

The bucket dictionary is an AVL binary-search tree on keys. Its augmented
flag is true exactly when its own count is at least w or a child flag is
true. To find the least eligible key, descend first into an eligible left
child, otherwise use the current bucket if its count>=w, otherwise descend
into its eligible right child. A false root flag means there is none.
Peek the first w FIFO records without unlinking them, writing GROUP in
that order. Quantum argument A_i is the borrowed view
GROUP[i].item -> LIVE[item].slot, resolved only at a classically known
gate index. The physical resolver reads the complete stored slot field;
there are a constant two descriptor-word reads. Run FW, then form all
new label tables from the still present consumed LIVE records, before
unlinking or reusing them. Returned records need no label/slot copy.
Then:
- Pair cell {a,b}, a<b: append its good output at A_a with the FW label
  table and unlink only item rows a,b. FW has already reset/released A_b;
  no second quantum release is performed by this metadata operation.
  All w-2 returned item rows stay in their original FIFO positions, with
  identical labels, quantum references and links except neighbor updates
  caused by those two removals. They are not dequeued and reinserted.
- Matching cell or Ev: unlink all w item rows. Append the good outputs
  in increasing first-endpoint order. The recycled block retains its first
  indexed qubit with the FW sum table; insert that one record at the tail
  of its new key bucket. The other consumed qubits have already been released/reset by FW. Freeing item metadata never releases a retained good/recycled
  qubit; ownership is transferred to OUTPUT or the new item record.
Repeat while an eligible bucket exists. Finally measure, reset and release
all LIVE qubits, free heap/bucket/snapshot metadata, and return OUTPUT.
GROUP is a non-owning view, not a new logical register or cloned qubit. LIVE
membership bookkeeping and label fields are frozen through FW and label postprocessing; consumed item references are
not used as gate operands again before unlinking. A PREP abort aborts the level with the specified cleanup; no item updates
occur before its FW has returned a cell. All added record work is classical
and at classically known addresses, with no QRAM or quantum-controlled tree.

## Explicit dictionary operations

To append an item, search by key; if absent, allocate a bucket leaf using
ordinary BST insertion. Write all fixed bucket/item fields before linking.
Set the old tail's next link, the item's prev link, and the head/tail/count
fields. To unlink an item, update its two neighbors or the head/tail,
decrement the bucket count, and return the item row to its free stack.
If the bucket becomes empty, delete it from the AVL tree. Item IDs and
bucket IDs are stable while live.

Recompute height and augmented eligibility along each affected ancestor
path. With balance height(left)-height(right), use a right rotation for
balance+2 and a left rotation for balance-2; first rotate the heavy child
if its balance has the opposite sign. A zero heavy-child balance takes
the single outside rotation. A rotation updates the former parent link
(or root), middle subtree link and child parent links, then recomputes
the lower node's fields and the new root's fields. Continue at the new
subtree root's parent. These rules specify both insert and delete repair.

An empty bucket with at most one child is replaced by that child. With two
children, take the leftmost node y of its right subtree. Transplant y as
a node, not by copying y's key/FIFO into the deleted bucket. If y is not
the immediate child, replace y at its old parent by y.right, attach the
old right subtree to y, and start repair at y's former parent. Otherwise
start repair at y. Replace the deleted node by y and attach its left
subtree. The resulting repair path reaches y and then its new ancestors.
Return only the deleted row to the free stack. This preserves every other
bucket ID, so no scan of item back-pointers is needed.

The usual height recurrence is included for the cost bound: a nonempty AVL tree
of height h has at least1+N_(h-1)+N_(h-2) nodes. With N_1=1 and N_2>=2,
induction gives at least2^((h-1)/2) nodes for h>=1, hence
h<=2log2(nodes+1)+1. The empty tree has height0. Search, eligible selection,
insert and delete visit O(log Cin) nodes and use O(1) fixed-field work per
node/rotation. With n-bit field arithmetic/comparisons, each operation
costs O(n log Cin) structural bit steps. Physical row/word addressing and
fees are additionally charged by proof.md; none is a unit-cost oracle.

## Deterministic invariants and operation count

LIVE records stay collimated to p: returned records are unchanged and a
recycled difference is the sum of its block's input differences. Every
good output has difference Del_a-Del_b, divisible by2^(p+c) for equal keys.
FIFO order and least-eligible selection are functions only of these low
keys and the already recorded FW outcomes. Each group has w distinct live
qubits and is measurable from the history before that FW. All product-state
and disjoint-source invariants of P Section7.1 therefore continue to hold.

Number FWs whose step4 is executed k=1,...,A, with good count gamma_k and
net LIVE removal rho_k. Pair cells have (gamma,rho)=(1,2); matching cells
have (u,w-1), Ev has (0,w-1). Thus rho>=2, gamma<=rho/2 and

    A<=Cin/2, |OUTPUT|<=Cin/2,
    Cin-S_end=sum_(k<=A)rho_k, S=sum_(k<=A)gamma_k.       (7.3)

Termination is certain unless PREP aborts, because each completed FW
strictly decreases LIVE. At normal termination every key has fewer than
w records, so S_end<=(w-1)E deterministically, with no round-count premise.

Let M count matching/Ev outcomes. Pair cells unlink2 records and matching
cells unlink w then reinsert1, so total unlinks=sum rho_k+M. Since
M(w-1)<=sum rho_k<=Cin, this is at most Cin+Cin/(w-1)<2Cin. Recycled
insertions number M, and initial insertions number Cin. Returned pair-cell
items incur no insertion/deletion. All dictionary/FIFO updates together
are therefore O(Cin), and there are at most Cin/2 eligible-key searches.
No amortization over an unbounded random run is used: these are branchwise
counts. During recycling unlinks happen first, so an item/bucket free row
is always available. Nonempty buckets never outnumber LIVE records.

## Lemma7.2: distribution-free yield

Let ell>=2 and E<=Cin/(4w ell). Work in the ideal outer process
omitting the global key cap and all private retry/counter state. For
any labels and conditional on the logical past, normal termination
with S<(ell-1)Cin/(RHO ell) has probability at most
2exp(-Cin/(10ell^2w^2)). The actual global key-cutoff event is separately
bounded in seed_retry.md; no per-call preparation-abort bound is used.

Proof. In this ideal process seed preparation returns the exact uniform
permutation almost surely, so Lemma7.1 applies at each actual FW.
For the yield, for k>A let the type of the k-th FW
be drawn from an independent source with the law (7.2) (phantom outcomes, which the algorithm never
draws). Let F_k be the sigma-field of the history immediately before the type/cell measurement of the k-th FW of the level,
with already measured logical history but no key retry/cap state and not the current type, or up to the end or ABORT of the level if A < k, joined with the phantom types for
A < j < k. Then F_1 contains everything before the level and the labels, F_k is contained in F_(k+1), and
the event A >= k and, on it, the k-th group are F_k-measurable. By (P) and Lemma 7.1(a) on {A >= k}, and
by construction on {A < k}, the k-th type has law (7.2) given F_k for every k. Since the earlier types are
F_k-measurable, the tower property gives, for every fixed z and every sequence o of z types,
Pr[types 1..z = o | F_1] = Pr[types 1..z-1 = o' | F_1] Pr_(7.2)[o_z], so by induction on z the first z
types are independent with law (7.2), conditional on everything before the level.
Put g = 1/(4 ell) <= 1/8, so (w - 1)E <= g Cin and Cin >= 4 w ell, and z = floor((1 - 2g) Cin/rhobar).
Since 2 <= rhobar < 3, Cin/5 <= Cin/4 - 1 <= z <= Cin/2. Let Vz = gamma_1 + ... + gamma_z and
Wz = rho_1 + ... + rho_z. If the level ends without ABORT and A <= z, then by (7.3), S_end <= (w - 1)E and
rho_k > 0, Wz >= Cin - S_end >= (1 - g) Cin, so Wz - rhobar z >= g Cin. The rho_k lie in [2, w - 1], so
by Hoeffding

    Pr[Wz - rhobar z >= g Cin] <= exp(-2 (g Cin)^2/(z w^2)) <= exp(-4 g^2 Cin/w^2) = exp(-Cin/(4 ell^2 w^2)).

If A > z then gamma_1, ..., gamma_z are actual and S >= Vz. The gamma_k lie in [0, q], so by Hoeffding

    Pr[Vz < (1 - g) gbar z] <= exp(-2 (g gbar z)^2/(z q^2)) <= exp(-8 g^2 z/w^2) <= exp(-Cin/(10 ell^2 w^2)),

using gbar >= 1 and z >= Cin/5. Outside the two events, by (7.4) and gbar <= 3/2,
S >= (1 - g) gbar z >= (1 - g) gbar ((1 - 2g) Cin/rhobar - 1) >= (1 - 3g) Cin/RHO - 3/2
= (ell - 1) Cin/(RHO ell) + Cin/(4 RHO ell) - 3/2 >= (ell - 1) Cin/(RHO ell), since Cin >= 4 w ell. QED.


This proof uses only the phase-independent conditional FW type law,
measurability of the next group, (7.3) and the endpoint LIVE bound. The
work-conserving implementation supplies all four. Earlier types can change
which bucket is selected next; the conditional law and tower argument
already include that adaptivity. No round independence or label-distribution
assumption is added.

## Costs, capacities and higher-bit conditioning

Initial and recycled insertions, unlinks, bucket repair and eligible searches
cost O(n log Cin Cin) structural work. Each GROUP peek/copy uses O(wY_i) bit transfers, and costs
O(wY_i log n)=O(n^(3/2)log n) including local loop/index emission, at most Cin/2+1 times including abort. perm_fw.md
proves O(n(log n)^4) structural work per fixed cell/canonical body;
private key attempts are counted globally in seed_retry.md.

Full label processing is amortized by consumed inputs. A pair reads only
its two consumed records, leaving every returned label/reference untouched.
A matching/Ev may read all w records, but w<=2rho since rho=w-1.
Good/recycled output rows and transferred slots cost O(nrho) as well.
The LIVE balance gives sum rho<=Cin; extra recycled insertions and full
unlinks have already been bounded by2Cin. Thus full label reads, sums, writes and slot transfers use O(nCin)
bit operations per chunk; a conservative local emission allowance gives
O(n log n Cin), still below the chunk bound. Metadata records
are freed only after these sums and surviving slot transfers; record
unlinking never performs another quantum release. Logical FREE_Q may
clear a released input's slot field, but its labels remain until this
point; no released input is used by a later gate. Surviving slots move
once to OUTPUT/recycled records, and old views then die.

These word/field streams are explicit inline bit loops. They bind the
source/destination row variables once and iterate their bit positions;
a reference to a row variable is a fixed field of the current frame,
not a fresh serialization of its full value for every transferred bit.
The finite field-role stream generator of typed_dispatch.md counts
all transferred bits and O(log n) local index emission per bit, including
row binding as specified there. The physical interpreter reloads/resolves full
row values with its counted helpers as often as needed. This is no free
word operation: a Y_i-bit metadata field contributes Y_i bit steps, and
an n-bit slot/label contributes n. The complete physical word-helper
cost is separately present in the typed ledger. Dictionary work with
the same conservative local allowance is O(n log Cin log n Cin),
also within the chunk bound because log Cin=O(r).

Excluding private key attempts, one chunk costs
O(n^(3/2)log n Cin), including cell/canonical bodies, metadata,
labels, cleanup and emission. The body contribution O(n(log n)^4 Cin)
fits because(log n)^3<=sqrt n. The total PRIVATE key-attempt work is
bounded globally by seed_retry.md and may concentrate in one chunk;
there is no per-chunk preparation-work assertion. Combining that global
bound with all chunks gives the joint structural count there.

There are only a fixed number of new item/bucket/free/snapshot arrays per
active level, fewer than32. Each has at most Cin<=2^cb rows and at most12n
bits per row. No quantum qubits beyond FW's original scratch and live pool
are added. The physical owner bound in proof.md includes these arrays.
The virtual classical-space envelope remains O(n r2^cb), with only a fixed
constant-factor change.

Full label fields can be copied as data, but group-selection decisions
inspect only keys below p+c, counts, FIFO links and measured FW outcomes.
AVL rotations and free-row choices are deterministic functions of this
same history. Therefore the logical higher-bit conditioning in P Sections9
and10 is unchanged: no bit at or above the next collimation boundary is
used to select a group. The stronger distance proof applies to actual roots,
not phantom leaves, exactly as in the complete retained source.
