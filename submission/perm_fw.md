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
table is allocated. Section7 emits these fixed networks in O(log n)
aggregate bit work per gate, giving O(n(log n)^4) per attempt/body.
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

## 7. Incremental generator for sorting and join circuits

This refines uniform emission of the SAME Boolean/Clifford+T networks
above. All key widths, ancillas, gates, PREP failure probabilities and
Kraus operators are unchanged. Only the charged classical construction
of their local wire-index tuples changes. The total generation bound
is O(log n) per elementary gate, including initialization amortized
over its comparator or scan block. No gate transcript is stored.

For a bitonic network of L=2^h records, stages are ordinary indices
p=1,...,h, s=p-1,...,0. In a stage, loop over blocks of length2^(s+1)
and offsets a0=0,...,2^s-1. The two compared records are
 a=block+a0, b=a+2^s,
and direction is the known bit [a AND2^p=0]. This enumerates exactly
the fixed network of Section1. These are classically known generator
indices; no comparison outcome chooses a wire or loop endpoint.

Records have a classically known width d. For key sorts d=O(sqrt n),
and for cell/lookup joins d=O(log n). Comparator work and output versions
use fixed rectangular blocks, with ripple bit v and a fixed finite
operation tag as their inner coordinates. A comparator contains at
least d elementary Boolean operations, including its field outputs.
Wire references have the form base plus a fixed stride times a record,
comparator or bit index. The number of array types and loop nesting
depth are bounded constants. All circuit spans are polynomial in n.

At the start of a comparator compute its constant number of input,
output, carry and temporary block bases with schoolbook O((log n)^2)
bit arithmetic. When a previous-stage output record is needed, its
previous comparator ordinal and side are computed with the masks
(i >> (s_old+1)), (i AND(2^s_old-1)), and bit s_old. These take O(log n)
bit work; multiplying by a known block stride is charged at this same
O((log n)^2) setup allowance. Keep separate base/cursor words for the
constant number of operand roles. During its ripple and field-copy
loops, advance these by their known unit or constant strides, costing
O(log n) bit additions/copies per gate. No product is recomputed for
each emitted bit gate. Restoring a saved base at a loop wrap is also
O(log n). The output tuple's actual O(log n) index bits are written
and charged; this is not an assumed zero-cost relative-address opcode.

Every compared record has d>=c log n bits for an absolute positive c
in the current main-branch circuits, except the simple single-bit flag
scans. Thus O((log n)^2) comparator setup is O(d log n), absorbed by
O(log n) times its d or more gates. Single-bit flag scans need only
increment/restore cursors, with no width multiplication; their index
generation directly costs O(log n) per gate. Prefix word scans and
payload extraction have the same rectangular layouts and bound.
Stage/block initialization costs at most O((log n)^2) each and is
absorbed over its record comparisons. A fixed number of sorting/join
networks and fixed-array copies has the same aggregate bound.

To emit the clean reversal, visit its fixed blocks in reverse order,
reverse the stage enumeration (p descending, s ascending), visit pair
blocks/offsets backwards, and reverse the constant ripple templates.
Fresh-scratch ids retreat instead of advance, with the same base/stride
computations. Wire locations in a Boolean network are fixed independently
of its quantum comparison results; the reverse generator therefore
needs no saved comparison transcript in ordinary memory. Comparator
bits themselves remain the quantum scratch already charged above.

All local cursor, stride, ordinal and base words fit
W_e=ceil(log2(2^24 n^4)) bits, with one additional signed temporary bit.
The elementary gate/scratch count is below c_F=2^20n^3; fixed layouts
and their temporary offsets lie within the indicated enlargement.
Only constant many such ordinary words are staged at once, using O(n)
bits; all arrays, algorithm frames and descriptors remain banked.
The local index tuple still passes to the complete physical resolver,
including GROUP's item lookup and its full n-bit slot field. Actual
physical addresses retain their O(sqrt n) width and charged fees.
No exponentially large pool or label-table index is shortened here.

Consequently each current O(n(log n)^3) key/body network costs
O(n(log n)^4) structural work. seed_retry.md sums all actual attempts,
including arbitrary concentration of retries, and combines borrowed GROUP,
dictionary/label streams and verified extraction into the global
O(n^(5/2)(log n)^2 C_0) allowance. It derives the declared log-power-three
time with the unchanged typed bank. No per-chunk retry-cost bound or
condition on favorable private outcomes is used.
