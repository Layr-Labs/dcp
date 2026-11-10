# Permutation-seed FW: exact instrument and counted circuits

This file is the normative circuit realization of the even-size FW cell
family in virtual.md Section7.1. The weights, cells and postprocessing
are retained. Only the realization and its private measured ancillas
change. Put w=2^ceil(log2 n), q=w/2, b_w=log2 w, r=ceil(sqrt n),
and b_K=4r+2b_w+10. This is an exact Clifford+T construction; no
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
measure it. Failure ABORTs and resets/releases all newly allocated
registers; no input A_i has yet been touched. If successful, compute
G(S,pi) into the old K target, where G sorts records (pi_j,S_j) by id
and outputs the key in original-id order. Since G(F(K))=K, this clears
K. Both F and G are clean XOR functions. Reset the measured flag, and
measure/reset/release S. Keep only pi, w words of b_w qubits.

Let Q=2^b_K. The collision probability is at most w(w-1)/(2Q), by a union
bound on key pairs, hence at most2^(-4r-11). Conditional on no collision,
there are exactly w! assignments to each strictly increasing key list S,
one for each permutation pi. All initial amplitudes are positive and
equal, so the postselected state factors as

 (uniform superposition over increasing distinct S) tensor
 |U_perm>,   |U_perm>=(w!)^(-1/2) sum_(pi in S_w)|pi>.

Measuring S therefore leaves the exact pure |U_perm>, with no information
about future input data. PREP has one attempt, with the stated tiny
input-independent abort probability. It acquires no source copies.
Conditioning on its success is used only in the ideal FW channel proof;
its failure remains counted in the unconditional algorithm.

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

The key sort/unsort networks dominate: their Boolean gate and actual
scratch count is O(w(b_K+b_w)(b_w+1)^2)=O(n^(3/2)(log n)^2).
The constant number of joins/compositions above are O(w(log w)^3),
smaller. Taking at most2^16 w(b_K+b_w+1)(b_w+1)^2 Boolean gates covers
all functions, copies, prefix networks and flags with generous ripple
constants. Clean reversal and exact decompositions fit an elementary
gate/ancilla budget2^22 w(b_K+b_w+1)(b_w+1)^2. For r>=2^20,
w<=2r^2, n>=(r-1)^2>=r^2/2, b_K+b_w+1<=5r and
2log2 r+2<=r/16. These inequalities imply this budget is below
2^20n^3=c_F (substitution gives ratio at most 5/(4r)<1).
The ticket, key, sorted-key and permutation registers fit the same
conservative c_F capacity; the displayed bound includes them. No
sorting table of all permutations or key values is allocated.

Keep the conservative O((log n)^2) uniform local-index emission bound
per elementary gate. Sorting stages, comparator positions and ripple
bits have polynomial-sized indices; constant many nested classical
loops generate compare-and-swap networks and their clean reversals.
Offset multiplication/copy is charged. The key width is O(sqrt n),
but its wire indices have O(log n) bits. Resets, allocation initialization,
private measurements and cleanup have the same actual wire-event count.
Thus FW costs O(n^(3/2)(log n)^4) structural work, apart from its label
postprocessing, which is amortized separately in bucket_level.md.

All new descriptor arrays have at most c_F rows, fitting V by the
existing cb>=19+6log2 r capacity inequality. There are fewer than64
fixed additional register/array owners, with at most one active FW.
The fixed-owner margin in proof.md already exceeds these counts; no
OWN, ROWS, WROW, HQ or physical prefix is enlarged. The constant source
scratch bound remains c0 n+c_F. Ordinary generator state is a constant
number of O(n)-bit words; all growing arrays and source frames remain
banked. There is no ordinary circuit transcript.

The new per-FW PREP failure2^(-4r-11) is bounded by the retained
w2^(-3r) allowance. Hence the conditional pool-stage abort bound and
its union over all capped runs remain valid without enlargement.
PREP failures reset all acquired ancillas and then the global abort
cleanup resets/releases the pool; no data is postselected for free.
This changes neither Qcap nor any tree/decoder error allowance.
