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

## 7. Aligned native layout and scoped complete-address emission

The Boolean functions, forward/canonical maps, fresh permutation and
arbitrary-input instrument of Sections1-5 are unchanged. This replaces
the old per-gate numeric-index generator by a physical layout and scoped
emitter. The actual short keys of seed_retry.md have b_K=3ceil(log2 n)+10
bits; every compared/joined word has Theta(log n) bits. No banked pool
index or classical label is shortened by this private layout.

Use a power-of-two slot block for each Boolean comparator/template word:
choose the least power2 at least its constant-times-record-width work,
then fixed power2 subblocks for its finite carry/input/output roles.
Choose each relative word block large enough for t+2 positions: for
slot k+v the actual wire is2(k+v)+3. Its low q+1 wire bits vary while
the aligned higher record coordinates stay fixed, including the two
guards; no odd-wire offset crosses a record.
Pad stage counts to powers2 too; comparator ordinal ranges already have
power2 size. Wire coordinates are CONCAT(stage, comparator ordinal,
finite role, relative bit). Each complete coordinate width is O(log n),
and the whole native span is polynomial. This is a different actual
fixed placement of the same circuit wires, including their initialized
zero padding, not an assumed free multiplication by a general stride.

For bitonic enumeration at stage (p,s), pair (a,b) has b=a XOR2^s,
a<b, and direction the known bit [a AND2^p=0]. Enumerate pair blocks
and lower offsets as in the preceding circuit. A record i's producing
comparator at a preceding substage s_old has ordinal
 ((i>>(s_old+1))<<s_old)+(i AND(2^s_old-1)),
and side bit s_old of i. Thus every needed old-version wire is obtained
by bit masks, shifts and copying O(B) bits, B=O(log n). Concatenate
these coordinate fields directly; no schoolbook B-by-B stride product
is used. Finite subroles and one-bit neighboring offsets have explicit
carry/borrow code. All source and destination bases are classically
known and independent of quantum comparison outcomes. Comparators
produce fixed output versions, so no ordinary wire-map array is stored.

At FW scope entry initialize ALL bits of constant-many complete d-bit
operand argument buffers, d=Theta(r), including every high zero. They
remain within the fixed polynomial native range throughout. Before one
comparator, explicitly write all of each buffer's LOW B bits from its
coordinate fields, costing O(B) bit steps; initialized high d-B bits
remain present and zero. Use separate buffers for the constant-many
operand ports and finite gate-template phases. No complete d-bit
initialization or descriptor/binding fetch is repeated per comparator.
Owners were activated before entry; no private circuit activates an owner.

Inside each comparator's length-t ripple/field pass, t=Theta(log n),
only the low q=ceil(log2(t_pad)) relative-bit positions change, with the
higher aligned record/role coordinates fixed. Advance/reverse those
low counters explicitly by carry/borrow. The existing squared-run
microprogram counts O(t+q^2)=O(t) bit generation and buffer changes,
including initialization/restoration; stop before the out-of-record
successor. Neighbor operands use their own shifted/guarded subblocks,
with their constant-many offsets initialized before the pass. Padding
gives room for a guard position; no carry changes the next record.
A full comparator has O(t) actual gates and fixed-many such passes.
Its O(B) setup is absorbed because t>=cB for an absolute positive c.
Each changed address bit still pays d, and EVERY actual gate/read/reset
consumes the ENTIRE correct d-bit operand and pays d. This does not
omit addressing, assume a unit-time cursor or add a relative-index oracle.

The clean Boolean comparator has fixed finite XOR/AND/NOT/carry gate
templates per bit, including output copies and reversing the compute.
Emit these through the finite phase/port roles above. The quantum flag
only controls its prescribed quantum gates; it never selects the
classical layout, cursor or loop endpoint. Full network reversal visits
stage coordinates in reverse, pair blocks/offsets backwards and each
finite gate template backwards with borrow cursors. All intermediate
quantum bits remain their counted private scratch until uncomputation;
no saved classical comparison transcript or growing instruction list
is used. Constant many ordinary O(log n)-bit coordinate/base words and
constant many d-bit argument buffers fit the existing staging margin.

Prefix-word scans, masked XORs, payload extraction, fixed-array joins
and the compact D(P) code scan use the same padded word template.
Single-bit flag arrays instead scan the complete contiguous array with
one argument buffer; its low-B increments cost O(w+B^2)=O(w), including
arbitrary starting carries. They do not reload B address bits per flag.
Stage setup O(B^2) times a fixed polynomial in log n is absorbed by
w(log w)^3; w>=n and n>=2^40. For B=O(log n), the stage setup is absorbed since any fixed polynomial
in log n is O(n); all main-branch sizes obey the same absolute bound.
No quantum outcome changes the finite program or its circuit function.

The power2 padding enlarges the explicit private-space bound by at most
128: each of stage, comparator-word, role and bit ranges has less than
factor2 padding, with finite template alignment included in this bound.
The inherited bound including extra D(P) is at most
 (5/(4r)+1/(64r))c_F.
After padding it is at most162c_F/r<c_F for r>=2^20. Hence all private
positions stay below c_F, disjoint from persistent X at P-w,...,P-1,
with P=4c_F unchanged. Unused padding stays zero; reset only the
actually used circuit positions on attempt/return/abort, not the whole
capacity. Whole-prefix setup/cleanup already counts all padding.
Fresh-key collisions touch only private registers and never active X.

Consequently each key attempt/body has O(w(log w)^3) elementary gates
AND O(w(log w)^3) actual raw emitter/address-update bit work. Complete
physical charging gives O(n^(3/2)(log n)^3) per attempt/body. The global
executed request/failure caps in seed_retry.md are unchanged; no
per-chunk preparation-work assertion is introduced. Since M_K=O(n C_0),
all private FW work is O(n^(5/2)(log n)^3 C_0). Counter/full binding
events retain their separately counted complete-word helpers.

The other current word-tree/source bounds are in native_ops.md. With
the unchanged PP and Qcap substitutions this yields
 T<=c[n^(5/2)(log n)^3 C_0+n^3(log n)^(3/2)2^(H+dl)
       +n^2(log n)^2 Qcap+n^2(HQ+DRAW+1)]+poly(n)
  =O(n^(43/4)(log2 n)^3 2^((7/6)sqrt n)).
All four non-time objects, exact source laws/caps and unconditional
full-secret success probability remain identical. This changes native
wire placement and its counted emitter, never the FW Kraus instrument.
