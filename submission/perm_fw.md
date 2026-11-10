# Permutation-seed FW: exact instrument and counted circuits

This file is the normative circuit realization of the even-size FW cell
family in virtual.md Section7.1. The weights, cells and postprocessing
are retained. Only the realization and its private measured ancillas
change. Put w=2^ceil(log2 n), q=w/2, b_w=log2 w, r=ceil(sqrt n),
and b_K=2b_w+Lg+10, Lg=ceil(log2 n). This is an exact Clifford+T construction; no
approximate rotation, QRAM, sorting oracle or mixed-radix lookup is used.
All data-derived quantities below are coherent Boolean wires. Generator
loop indices are fixed classical indices, and every selection/join is
implemented by the fixed sorting circuits below. A controlled update is
a Boolean expression, never a branch on a quantum value.

## 1. Fixed sorting and joins

A comparison of two d-bit words and a conditional swap of two d-bit
records are O(d) AND/XOR/NOT Boolean gates with ripple comparison.
Use the bitonic network on a power-of-two number of records. Build a
bitonic sequence by sorting its halves in opposite directions, compare
positions separated by half the block with min in the first half, then
merge both halves recursively. The first comparison layer puts all
smaller elements in the first half of a bitonic sequence; each half is
bitonic. Induction proves merging, then sorting. There are at most
L(log2 L)(log2 L+1)/4 comparisons for L records. Include a record id in
tie breaking. Thus this is a fixed Boolean circuit for deterministic
stable sorting, not data-dependent circuit generation.

A join of sources (key,payload) and queries (key,destination) uses the
same network: sort sources before queries of the same key, propagate
the last source payload along the ordered list with a prefix scan, then
sort query results by destination. In our valid domains there is exactly
one source for every requested key. Inactive records have distinct
sentinel keys beyond the real range and a disabled flag. Their extracted
answers are zero; a found bit (or payload+1 encoding) distinguishes an
absent source from a legitimate zero payload. A scan with a word payload copies/selects O(d) bits per
record. Source/query destinations and flags use O(log w) bits here; joins
of O(w) records cost O(w(log w)^3) Boolean gates. Inputs outside the
specified domains receive the total function defined by the same sort,
scan and masking network; correctness of those arbitrary extensions is
not assumed. Padding to 2w,4w or another fixed multiple of w preserves
the same bound.

All these are ordinary acyclic Boolean networks: compute every gate
into a fresh zero bit, copy the desired XOR output, reverse the network.
This cleanly implements |a>|z> -> |a>|z XOR F(a)> for every bit-string a.
AND, XOR and NOT are Toffoli, CNOT and X. Exact constant-size Clifford+T
decomposition is charged. This also gives a clean sorting function even
though comparison sorting by itself loses permutation information.
The original input remains available until it is deliberately cleared
with a separate inverse function on its actual support.

## 2. PREP: a fresh exactly uniform permutation

On w independent b_K-bit zero key registers K_i apply H to every bit.
Compute F(K)=(S,pi), sorting records (K_i,i) by key then id, where S is
the sorted key sequence and pi_j the original id of sorted position j.
Compute the Boolean flag that adjacent S keys are all unequal and
measure it. On collision reset/release all attempt registers and retry
fresh keys, subject to the global failed-attempt cap in seed_retry.md.
That file specifies executed request/failure counters, M_K and F_K and
the global ABORT. No input A_i has yet been touched. If successful, compute
G(S,pi) into the old K target, where G sorts records (pi_j,S_j) by id
and outputs the key in original-id order. Since G(F(K))=K, this clears
K. Both F and G are clean XOR functions. Reset the measured flag, and
measure/reset/release S. Keep only pi, w words of b_w qubits.

Let Q=2^b_K. An attempt's collision probability is at most w(w-1)/(2Q),
hence at most1/(2048n). Conditional on no collision there are exactly w!
assignments to each increasing distinct key list S, one for every pi.
All amplitudes are positive/equal, so the state factors into a uniform
increasing-key state tensor |U_perm>. Measuring S leaves the exact pure
uniform permutation independently of the future input. This factorization
holds conditional on every previous failed attempt. Retrying without a
cap terminates almost surely; actual work is bounded by the executed
global cap, with failure probability below2^-80, proved in seed_retry.md.
No per-call small abort bound near that cap is asserted.

## 3. Forward cell code

Use a 2(b_w-1)-qubit ticket T prepared by H, t=q a+b with a,b in[0,q).
For basis input x compute h, mu, M, J and u as in virtual.md. Prefix
counts of M and J use ripple conditional increments, O(w log w) gates.
These values are never measured. If u=0 choose Ev. The two pair cases
are the original ones: a<u selects (m_a,j_b); a>=u>b selects
(m_b,j_(q+a-u)). One-hot prefix selectors and masked XOR extract the
two endpoint indices in O(w log w) gates. Pair-code fields initially w
are changed at those two positions to their reciprocal partners.

For the remaining case a,b>=u, 1<=u<=q-1, let pt_0,...,pt_(u-1) be the
first u elements of J encountered in permutation order pi. Form the
matching cell with pairs {m_k,pt_k} and the remainder Bl. Initialize
its code fields to w+1 and set reciprocal partners at these endpoints.
Here is an explicit fixed-scan/sort implementation, avoiding an indexed
load on pi or a data-derived rank:

* Join queries pi_j with fixed sources (i,J_i). Prefix-count the returned
  J flags in permutation order. Select those with prefix rank k<u.
* Join those selected rank-k records with sources consisting of the
  M positions and their minority prefix ranks, obtaining m_k.
* Form endpoint assignments (m_k,pt_k) and (pt_k,m_k), with disabled
  sentinels for inactive positions. Sort/join them by original endpoint
  id with fixed queries for every original id. Encode a partner v by
  v+1: query answer0 means no assignment and yields default w+1; a positive
  answer yields partner=answer-1. Thus partner0 is not confused with an
  absent endpoint. This obtains the matching code.

There are a constant number of joins on O(w) records of O(log w) bits.
Thus forward matching costs O(w(log w)^3), including prefix scans and
masked output. Multiplex Ev, pair and matching candidates into the
fresh P target. This is the clean Boolean function cell_perm(x,t,pi).
On prepared pi it always codes exactly a member of the original family
containing x. There is no read from a quantum-addressed memory.

## 4. Canonical seed and ticket erasure

A pair code is recognizable on reachable inputs by its fields equal to
w; matching codes have at least one pair and remainder w+1; Ev has no
paired fields. Comparisons/ORs over fixed fields cost O(w log w). No
quadratic reciprocal validator is needed: P was just computed by the
forward function on its promised prepared input. Off-promise function
values can be arbitrary total Boolean extensions.

For a pair, obtain the minority endpoint's M rank i and majority
endpoint's J rank k by one-hot prefix scans of the paired fields. XOR
q i+k if k<q, otherwise q(k-q+u)+i, into T. This is the unique original
ticket, so T becomes zero. Leave pi unchanged. For Ev leave T and pi
unchanged. For a matching leave T unchanged and transform pi as follows.

Define f=f_(x,P) on original positions by

 f(i)=w-u+rank_M(i)                    if i in M;
 f(i)=rank_M(P_i)                     if i in J and P_i<w;
 f(i)=u+rank_Bl(i)                    if i in Bl.

The three images are [w-u,w), [0,u), [u,w-u), respectively, so f is a
bijection. rank_M(P_i) is obtained by a sort/join of fixed rank sources
and paired-field queries; Bl ranks use prefix scans. To compute
pi'_j=f(pi_j), join fixed sources (i,f(i)) with queries (pi_j,j).
Compute this cleanly into a fresh permutation array, swap the two arrays,
and XOR f^-1 composed with the new array into the old target to clear
it. f^-1 is computed by sorting (f(i),i), and composition uses the same
join. The clean XOR/swap/XOR construction is unitary on every input;
the inverse identity is needed only on the reachable support, where f
is a permutation. Both permutation arrays and all Boolean scratch are
returned to zero except the retained pi'. Pair/Ev use the identity
permutation in this construction. Total work is O(w(log w)^3) gates.

Measure P to obtain C. Measure/reset T and the retained permutation
array; reset/release P and all scratch. Ticket and permutation outcomes
are private ancilla outcomes, included if needed in FW's detailed
instrument. For every pair {a,b} of C, a<b, perform the original CNOT,
NOT and release of A_b, retaining the good A_a with its original sum
table. Perform the original block CNOTs/release and recycled table for
Bl. Returned pair-cell inputs retain their qubits and tables. All
logical releases receive the explicit reset completion of proof.md.

## 5. Arbitrary-input channel equality

Fix x and a matching cell C containing it, with u pairs. For each t in
D_u={q a+b:a,b>=u}, the event E_(x,C) on pi is that its first u J elements
are precisely the partners of m_0,...,m_(u-1), in that order. The relative
order of J in a uniform permutation is uniform, hence

 |E_(x,C)|=w! (w-2u)!/(w-u)! = F_u.

This is also an exact count: fix the remaining J order arbitrarily,
interleave the u arbitrary M positions and order M arbitrarily.
Canonical f maps E_(x,C) bijectively onto the same set G_u for every
x in C: permutations whose first u members of the canonical J set
[0,w-u) are 0,1,...,u-1 in that order. Its inverse relabels symbols by
f^-1 and recovers the original event. Thus the conditional seed is the
same normalized positive superposition |U_(G_u)> for all such x,
depending only on u, not on x, labels, C or secret phase.

After computing C and erasing as above, its unnormalized private factor
for a matching cell is

 (1/q) sqrt((w-2u)!/(w-u)!) sum_(t in D_u)|t> tensor |U_(G_u)>.

Its squared norm is exactly y_C=(q-u)^2(w-2u)!/[q^2(w-u)!]. For a pair
cell, the unique ticket has been cleared, pi is still |U_perm>, and
its factor is q^-1|0> tensor |U_perm>, squared norm1/q^2. For Ev the
factor is the original uniform ticket tensor |U_perm>, norm1. Every
factor is independent of x within its cell.

Apply this identity to an arbitrary purification sum_x |x>|R_x>.
Conditioned on PREP success, measuring C therefore implements Kraus
operators c_(C,z) Pi_C tensor I on spectators, with
sum_z |c_(C,z)|^2=y_C; private measurements/reset do not distinguish
x inside C. This proves equality of the coarse cell instrument to the
retained FW, on every input state, not just equality of classical type
probabilities. For product equal-amplitude phase inputs, Pr[C]=y_C|C|/2^w.
The projector and unchanged CNOT postprocessing give exactly the original
independent good/recycled/returned phase outputs and zero released
inputs. Thus the type law (7.2), LemmaK, conditional yield, disjoint
source incidence and every downstream proof remain applicable.

## 6. Explicit gates, emission, capacities and failure

With b_K=O(log n), each key attempt and each fixed cell/canonical-map
network has O(w(log w)^3)=O(n(log n)^3) Boolean gates and actual scratch.
At most2^16 w(b_K+b_w+1)(b_w+1)^2 Boolean gates cover the fixed
number of sort/join/scan functions, with generous ripple constants.
Clean reversal/copies and exact decompositions fit2^22 times that
polynomial without its2^16 coefficient, including ticket/key/permutation
registers and scratch. For r>=2^20, w<=2r^2, n>=r^2/2,
b_K+b_w+1<=5r and b_w+1<=2log2(r)+2<=r/16. Substitution bounds the
ratio to c_F=2^20n^3 by5/(4r)<1. Thus the entire attempt/body fits
that fixed capacity, including all auxiliary registers. No key-space or permutation
table is allocated. Sections7-8 give the current complete physical
emitter and lazy pair/matching implementation.
Global attempt counts and all reset/counter work are in seed_retry.md.
Private retries can concentrate in one call; only their global work
bound is used. Labels/GROUP are counted separately in bucket_level.md.

All new descriptor arrays have at most c_F rows, fitting V by the
existing cb>=19+6log2 r capacity inequality. There are fewer than64
fixed additional register/array owners, with at most one active FW.
The fixed-owner margin in proof.md already exceeds these counts; no
OWN, ROWS, WROW, HQ or physical prefix is enlarged. The constant source
scratch bound remains c0 n+c_F. Ordinary generator state is a constant
number of O(n)-bit words; all growing arrays and source frames remain
banked. There is no ordinary circuit transcript.

Preparation failures are now fresh-key retries with an executed GLOBAL
cap. seed_retry.md proves its2^-80 cutoff probability and actual whole-run
work. The ideal outer pool analysis omits this cap and its private retry
counter; it does not condition on cutoff survival. The previous per-FW
PREP-abort allowance is not used. On a cutoff every remaining qubit is
reset/released; failed attempts acquire no source copies.

## 7. Complete aligned bitonic native realization

This remains the full instrument implementation and the matching-body
implementation used by Section8. Boolean functions and all private
Kraus factors are those of Sections1-6.

Use power2 strides for comparator-word blocks, their finite Boolean
roles, bit coordinates and stage regions. Every compared record has
t=Theta(log n) bits. Pad a word for t+2 positions; actual wire2(k+v)+3
then varies only in its low relative coordinate, without a carry into
the next aligned record. Coordinates are stage/comparator ordinal/role/
relative bit. Padding enlarges private spans by at most128, including
finite templates/guards. The explicit Section6 bound plus compact D(P)
is (5/(4r)+1/(64r))c_F; after padding it is <=162c_F/r<c_F.
X at P-w,...,P-1 stays disjoint. Only USED positions are reset on each
attempt/body, with all unused padding zero and full prefix counted.

At bitonic stage(p,s), enumerate a<b=a XOR2^s, direction[a AND2^p=0].
A record i's preceding comparator ordinal at substage s_old is
 ((i>>(s_old+1))<<s_old)+(i AND(2^s_old-1)),
with side bit s_old of i. Masks/shifts/copies and concatenated power2
coordinates cost O(B), B=O(log n), per comparator; there is no general
B-by-B stride multiplication. This setup is absorbed by its t gates.
Different fixed input/output versions have prescribed blocks; no ordinary
wire-version map or comparison transcript is stored.

Initialize constant-many COMPLETE d-bit operand buffers once at native
entry, with ALL high zeros. Per comparator write ALL low B bits for
the constant-many finite gate-phase/port roles. High d-B bits remain
correct and available. Within each word pass only q=ceil(log2 t_pad)
relative bits change; squared carry/borrow runs cost O(t+q^2)=O(t),
including setup, reverse restoration and guards. Stop before a successor
outside the record. Each changed argument bit pays d; each actual
gate/read/reset consumes ALL d bits and pays d. No owner is activated
inside the scope; outer bindings/epochs refresh at entry as before.

Clean reverse visits stages, pair blocks/offsets and finite Boolean
templates in reverse, with borrow cursors and quantum scratch retained
until uncomputed. Quantum comparisons never select a classical address.
Word prefix/join/masked-output scans use the same template. Single-bit
flags use one contiguous full-array stream, O(w+B^2)=O(w), without B
setup per flag. Stage setup polynomial in log n fits w(log w)^3.
Constant-many coordinate words and full argument buffers fit ordinary
staging. Thus an attempt/full body costs O(w(log w)^3) gates AND raw
emitter/address changes, physically O(n^(3/2)(log n)^3).
This retains all complete physical fees and constant-capacity proofs;
Section8 changes which requests need this full implementation.

## 8. Lazy permutation preparation and linear pair cells (current)

This realizes EXACTLY the instrument of Sections2-5 with a different
measurement/preparation order. Section7's full bitonic native realization
is retained for matching cells; no new sorting theorem is used.

### Coarse outcome before permutation preparation

Prepare the same uniform ticket T=q*a+b. Let u be the minority count
with the same majority/tie convention as Section3. Compute CLEANLY
from X,T a two-bit kind: Ev if u=0; pair if a<u or a>=u>b; matching
otherwise. All count/comparison ancillas are uncomputed before kind
is measured. No count, majority bit, selection path or residual rank
is measured. The measured kind is a function of the FINAL cell code:
it is independent of pi. The forward/canonical computation intertwines
its early projector with that final-code function, so this coarse
measurement does not refine any cell or discard within-cell coherence.

Only after kind=matching prepare a fresh exactly uniform permutation
using Section2. Its random keys are independent of the post-kind input
and ticket. The original independent preparation could commute past this
pi-independent kind measurement. All matching forward/canonical circuits
therefore realize precisely the original conditional instrument. Pair
and Ev never use pi, so their unused input-independent permutation factor
is omitted altogether. No permutation is reused. This explicitly replaces
the earlier physical order in which ALL key attempts preceded data access.
Collisions still touch only private key registers, never encoded X.

The logical FW primitive is the ENTIRE kind-plus-cell macro. Conditional
type laws and yield martingales condition on history BEFORE its first
coarse measurement, not on its current kind before its later cell
measurement. Past kinds are functions of already recorded cells. There
is no new high-label/group-selection decision or private-state conditioning.

### Linear-size exact pair functions

Use balanced trees with w leaves. A subtree of size2^j stores its
count in j+1 bits. Ripple adds/comparisons use O(j+1) Boolean gates, and
 sum_(j>=0) (w/2^j)(j+1)=O(w).
Thus full popcount, majority/tie bit and all minority/majority subtree
counts cost O(w). Minority leaf bits are X_i XOR majority; computing
all of them also costs O(w). Ancillas are private coherent Boolean
work, not extra source incidence.

For a pair ticket, if a<u select minority rank a and majority rank b;
otherwise select minority rank b and majority rank q+a-u. A selection
propagates an active flag and residual rank to BOTH children at every
node, comparing with the left count and subtracting it for the right
child. All gates execute on fixed wires. At an active subtree its rank
is strictly below that subtree's count, so truncating the child residual
to its j-bit range is valid. Inactive children are masked and have an
arbitrary fixed total extension. Node rank widths are proportional to
subtree height; the same summed-width identity gives O(w) gates.
No superposed rank is a physical memory index.

Leaf indicators form one-hot endpoints. A bottom-up selected-child mux
computes their binary indices in O(w) gates: a node's index word has
only its subtree-height width. Sort the two endpoint indices by one
O(log w) comparison, producing the prescribed unordered pair code.
The complete acyclic Boolean function is implemented as clean XOR:
compute all its Boolean results into fresh native zeros, copy just the
two indices to their targets, reverse the WHOLE computation. Its gate
and used-scratch counts stay O(w), including all signs/flags/counts.
There is no recursive doubling of the algorithm at every tree node.

To erase T, compute its unique old inverse from X and the two endpoints.
A balanced prefix-flag decoder converts a binary endpoint into its
one-hot leaf indicators in O(w) gates. At each tree node compute its
rank-before-endpoint by
 rank_parent = rank_left if endpoint is left,
               count_left+rank_right otherwise.
Counts/ranks use local subtree widths, so the summed cost is O(w).
Compute the selected leaf's minority bit too; this identifies which
endpoint is minority. Let i be its minority rank and k the other
endpoint's majority rank. The exact old inverse is
 q*i+k                 if k<q,
 q*(k-q+u)+i           otherwise.
These are shifts and O(log w)-bit arithmetic since q is a power2.
Clean XOR this into T and reverse its entire auxiliary computation.
The old uniqueness proof in Section4 shows T is exactly zero.

For every basis x with opposite endpoint bits, precisely ONE original
ticket selects this pair: the first formula covers k<q and the second
covers k>=q. The uniform ticket amplitude is1/q. Consequently measuring
only the two binary endpoints has Kraus operator q^(-1)Pi_pair,
exactly the original cell, for arbitrary inputs and spectators. Within
a cell all private bits are zero; no majority/count information remains.
The full w-field P array is NEVER built for a pair. Its two endpoints
uniquely determine the old P code, so this is its exact compact encoding,
not a missing output-field write.

For Ev, kind=Ev restricts X to the old all-zero/all-one cell and leaves
T in its independent uniform state. Apply H to all T bits to clear it;
no pi or full P is needed. This gives Pi_Ev, followed by the unchanged
recycled-block postprocessing. Matching instead runs the full original
clean circuit on its conditional support and writes every matching-code
field before the matching tag. Pair writes both endpoints and its tag;
Ev needs only its tag. Old matching fields remain ignored on other tags.
All tags/payloads obey the same commit-last and no-owner-activation rules.
Transversal A/X CNOT/NOT operations, export decoding, released-slot
zeroing and consumed-label sequencing are unchanged.

### Level-wise complete native pair emitter

Keep the identical O(w)-gate Boolean functions above. Emit counts/ranks
bottom-up and selectors/decoders top-down. A height-j node has O(j+1)
bits and finitely many Boolean/ripple roles. Let b_j be the required low wire-coordinate width for its finite
roles, words and guards. Choose H_j the least power2 >=b_j+1, and
slot stride2^(H_j-1). It is O((j+1)^2), so the physical node field
begins at address-bit H_j, itself aligned. Each level span is a power2;
align its base to that span, wasting less than another span. Total
used/padded space is O(sum_j(w/2^j)(j+1)^2)=O(w).
Pack matching/ticket/code buffers below c_F/2: their Section7 padded
bound162c_F/r is below that limit. Place level regions above c_F/2;
only O(w) work spans, not the unused gap, are reset. Pair endpoint
targets use the separate code buffers and survive work resets. The guard
checks their aligned end below c_F. X stays at P-w, disjoint.
The existing n-only c_F guard checks this actual layout before sources;
on overflow select the exact full FW of Section7 at that n. Since
O(w)=o(c_F), only finitely many lengths take that terminating fallback.

Give every finite gate-phase/operand role its OWN COMPLETE d-bit
argument buffer. Initialize all bits at FW entry, including high zeros;
initialize low B=O(log n) coordinates once per LEVEL. Coordinates
stage/role/node/bit concatenate because each level base and stride is
aligned. A node i addresses children2i,2i+1. The actual delivery buffers
hold these counters: advance their node fields by1 or2 bit serially,
without copying/rebuilding B bits per node or per gate.

Inside a node only q=O(log(j+2)) relative bits change. The proved
carry/borrow word driver costs O(j+1+q^2)=O(j+1), including terminal
tests, restoration and guard positions. Then advance the node field.
Preset carry-head addresses once per level at H_j. The existing
active-width bit head code restores that head after a run. Because
H_j is a power2, its movement/control for a length-k carry is bounded
by a fixed polynomial in k, without a per-node B-bit reconstruction.
Summing over a binary counter cycle is O(number_of_nodes), since
sum_k k^a/2^k is finite for every fixed a. Ordinary loop counters use
the same counted code.
No successor is accessed after the last node. Low-relative-field reset
O(q) per node is O(j+1). All changed bits pay d; every gate/access
consumes ALL d bits and pays d. There is no free increment or pointer.

Stage-base computation may keep O(B^2) work per level, polynomial in
log n over all levels and therefore O(w). Root-only ticket/inverse/
minmax arithmetic may retain its previous polynomial-log driver too.
Majority and endpoint-bit control addresses are fixed for a whole level.
The encoded X leaf array need not be aligned: its ENTIRE contiguous
w-bit pass uses only low-native-width addresses, with carry work
O(w+B^2)=O(w). Quantum active flags control gates, never a physical index.

The SSA template depends only on (level,node,bit,finite-role), with
children in already completed levels. No ordinary wire-version map or
instruction list is stored; O(log^2 n) level/base/control bits and
constant-many full argument buffers fit staging. Reverse levels/nodes/
finite bit templates with borrow cursors to clean exactly the same
scratch/flags. Dependencies and the clean XOR function are unchanged.

Thus ALL actual generation/address changes AND Boolean gates total
O(w), charged O(n^(3/2)) per request. Full binding/argument entry and
used-region clearing fit O(n^(3/2)) once per FW, never per node.
The early-kind instrument, ticket erasure and spectator channel are
identical. With O(n C_0) requests pair/control work is O(n^(5/2)C_0).
The unchanged matching/key bound is O(n^2(log n)^3 C_0), smaller
because (log n)^3=O(sqrt n); the executed cap still counts every failure.
Dictionary/labels/slots cost O(n^(5/2)C_0), source O(n^2 Qcap), tree
O(n^3 2^(H+dl)). Including prefix/init/abort cleanup gives
 T<=c[n^(5/2)C_0+n^2(log n)^3 C_0+n^3 2^(H+dl)
       +n^2 Qcap+n^2(HQ+DRAW+1)]+poly(n)
  =O(n^(127/12)2^((7/6)sqrt n)).
Space/tolerance and success >=1-2^-8 are identical; the new schedule
also improves the source envelope to n^(103/12)2^((7/6)sqrt n).

### Global keys, work and correctness

Keep the executed request bound M_K=10r(ell+1)(C_0+1) and failed-attempt
cap F_K=M_K/r. Increment the request counter on EVERY FW entry, even
when no key is prepared. Only matching needs a successful preparation.
Across all chunks, completed matching/Ev cells M satisfy
 M(w-1)<=sum Cin=O(n C_0), hence M=O(C_0).
There is at most one incomplete matching request on a global abort.
Successful key attempts therefore number at most M+1; failures are
actually capped by F_K=O(r C_0). Total actual attempts are O(r C_0),
not the former O(n C_0). The full Section7 cost per attempt/matching
body is O(n^(3/2)(log n)^3), giving global
O(n^2(log n)^3 C_0). No favorable-outcome expectation is used.

The collision probability stays <=1/(2048n) conditional on ANY past,
including kind, because fresh keys are independent of current data.
The original global cutoff tail using the larger M_K trial allowance
still bounds the fewer actual attempts. Thus the ideal exact-channel
coupling adds the same <=2^-80 key event. On an actual cutoff after
kind, decode the active window and perform normal abort cleanup; all
partially initialized private regions are reset. The yield proof is
applied to the ideal logical cell macro, never conditioned on survival.
All source, held-out-bit, source-distance and decoder arguments therefore
retain precisely their prior premises and success budget.

The level-wise ledger above includes every request, failed preparation,
full binding, measured payload, reset and abort. It has the identical
complete cell instrument and four non-time structured objects; all
source/held-out-bit/decoder/cap couplings remain as proved.
