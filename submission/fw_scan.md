# Fixed-register scans for FW (normative P Section7.1 circuit implementation)

The cell family, ticket preparation, maps on prepared inputs, measured cell
code and postprocessing are those in virtual.md Section7.1. This file gives
a cheaper Boolean circuit for steps2–3. Put B=b_w+1. All indices N,i,v
in circuit-generation loops below are ordinary fixed loop indices. Values
x,h,mu,u, ticket bits, flags, ranks and partners are quantum circuit wires.
No such value is measured or used to branch the generator. An instruction
“if flag” means a Boolean controlled expression computed into fresh wires.
All loops run their full stated ranges, including inactive iterations.

## Shared Boolean primitives

Compute h by a ripple accumulator, mu=[h<=q], M_i=[x_i=mu], J_i=1-M_i,
u=sum_i M_i and prefix ranks m_i=sum_(j<i) M_j and j_i=sum_(j<i) J_j.
Store ranks and indices in B bits. A prefix scan of w flags uses O(wB)
Boolean gates: one B-bit conditional increment per position. A comparison
of B-bit words uses O(B) gates. Select a unique flagged word by XORing its
bits masked by the flag, with O(wB) gates, and return zero if no flag is
set. Compute each selector once and reuse its wire for all B word bits;
there is no extra B factor from recomputing selectors for each bit.
All addition, subtraction, popcount, comparisons and multiplexing below
are ripple Boolean networks of AND/XOR/NOT. Inputs are never overwritten.
A new version of every updated flag or word is stored in fresh wires.
This specifies an ordinary acyclic Boolean network, rather than a RAM
program or an irreversible update to quantum data.

## Forward map

Write t=q a+b. Compute the two pair-case flags [u>0,a<u] and
[u>0,a>=u,b<u]. In the first case select the unique positions with
M_i and m_i=a, and J_i and j_i=b. In the second replace those rank targets
by b and q+a-u. Extract their indices by masked XOR. Initialize a pair
code to w in each field and at the two selected positions XOR w XOR
partner. All scans are over fixed i=0,...,w-1. This costs O(wB).

For the matching case initialize alive_i=J_i and a separate candidate
code Pmatch_i=w+1. For each fixed N=w-1,w-2,...,3 do the following:

* Compute active=[1<=u<=q-1,a>=u,b>=u,w-2u+1<=N<=w-u] and k=w-u-N.
* Compute prefix ranks A_i=sum_(j<i) alive_j. Set
  g_i=active AND M_i AND [m_i=k] and
  f_i=active AND alive_i AND [A_i=R_N]. R_N is the fixed register for
  this iteration; it is not selected by a quantum address.
* Extract mstar=XOR_i(g_i times i), pstar=XOR_i(f_i times i).
  For every i,v update the code bit by XORing
  g_i AND ((w+1) XOR pstar)_v and
  f_i AND ((w+1) XOR mstar)_v. Set new alive_i=alive_i AND NOT f_i.

Here “times” is bitwise masking, not arithmetic multiplication. Each pass
uses O(wB) gates. On the prepared domain R_N<N, an active pass has
exactly N alive positions, one g and one f. The successive active N are
w-u,...,w-2u+1, so k=0,...,u-1. The selected partner is exactly the
R_(w-u-k)-th remaining majority position in the original map. Chosen
minority and majority positions never recur. Therefore the XOR updates
set precisely their reciprocal partner fields and leave all other fields
w+1. A final multiplexer chooses the appropriate pair candidate, matching
candidate or the constant Ev code according to u,a,b. Inactive scans do
not change the candidate. For off-preparation bit patterns the same fixed
Boolean formulas define a total function; their values are immaterial.

## Inverse map and validity

First compute validity of P once, outside the N loop. For each i inspect
all j=0,...,w-1 and check that a field P_i<w has a reciprocal P_j=i at
j=P_i and x_i!=x_j. Check every field is either <w, w or w+1. Count
paired positions. The pair flag requires exactly two paired positions
and all other fields w; the matching flag requires 1<=u<=q-1, exactly
2u paired positions and all other fields w+1. The full reciprocal/cross
scan costs O(w^2 B). For a valid matching these tests imply that every
minority position is paired: each cross pair uses one minority position,
and there are u disjoint pairs. The remaining positions are all majority.
Thus this test is equivalent to membership of x in a coded matching cell.
The pair test likewise verifies membership. Invalid inputs return zeros;
this chooses a total extension of back outside its reachable domain.

For a pair, select the minority endpoint's prefix rank i and majority
endpoint's rank k by masked XOR. Return t=q i+k for k<q, otherwise
q(k-q+u)+i, with all R fields zero. Multiplication by q is a fixed shift.

For a matching set alive=J and start all output fields zero. Loop through
fixed N=w-1,...,3. Set active=matching AND [w-2u+1<=N<=w-u], k=w-u-N.
Set g_i=active AND M_i AND [m_i=k] and extract
partner=XOR_i(g_i times P_i). This is a full fixed scan, not an indexed
load P[m_k]. Compute prefix ranks A_i of alive, then
f_i=active AND alive_i AND [i=partner]. Extract v=XOR_i(f_i times A_i),
write its low j_N bits to the fixed output R_N, and set
new alive_i=alive_i AND NOT f_i. Inactive iterations output zero.
Each pass costs O(wB). A valid matching has exactly one selected partner
in every active pass; its rank is in [0,N). Induction over decreasing N
shows that this is exactly the original list-removal inverse. Return
T=0. Ev and invalid codes give zero throughout. The pair and matching
flags are disjoint, so a final bitwise multiplexer combines the outputs.

## Coherent correctness, gates and space

For every basis x, every t and every R in the support of successful PREP,
the forward function equals the original cell(x,t,R). On all its outputs,
the inverse equals the original back(x,P), by the two inductions above.
Compute each Boolean gate into a fresh zero bit, copy the designated
output to its XOR target, and reverse all Boolean gates. This implements
|input>|target> -> |input>|target XOR function(input)> exactly, with all
scratch zero. Inputs to each function exclude its target. Linearity
therefore proves equality of steps2–3 on the whole prepared coherent
support, for arbitrary input density matrices and external entanglement,
not merely equality of classical cell distributions. PREP and all later
steps are unchanged. Any total Boolean extension off this support gives
a unitary XOR implementation and cannot affect the channel here.
In particular all Kraus operators, phase independence, conditional type
laws, recycled/returned qubits and cleanup statements of Lemma7.1 remain
exactly valid. This is no new outcome-law assumption.

For explicit generous capacities take at most64wB Boolean gates for shared
prefix preprocessing; at most128wB for each fixed-N forward or inverse
pass; at most128w^2B for the once-only validity scan; and at most128wB
for pair cases, multiplexing and word arithmetic. Standard ripple
comparators/increments and masked XORs satisfy these constants directly:
a pass consists of one prefix increment scan, at most eight word
comparisons/additions per position, two masked word extractions and two
masked field updates. Even including both maps and fresh copies of each
intermediate, a budget2^12 w^2B Boolean gates suffices. Clean reversal,
output copies, and constant-size exact Clifford+T decompositions fit
2^19 w^2B elementary gates and qubits. For n>=2^40, w<=2n and 2B<=n,
so this is at most2^20 n^3=c_F. Ticket, cell and PREP registers fit the
same conservative cap by the ample constant slack in the preceding
bounds. Actual scratch and allocation/reset events are O(w^2B), not
c_F events. There is no hidden table of w^3 bits.

The incremental local-index generator specified below emits the same fixed
networks in O(log n) bit operations per gate. It includes preparation,
resets, reversal and cleanup. Its FW structural cost is O(n^2(log n)^2),
with full physical resolution still charged separately. The standalone
reference may retain its previous looser full-handle bound. Parameters,
source count, error model and space bounds are unchanged.

## Incremental uniform local-index emitter (additional normative implementation)

Use the same fixed-register Boolean networks above, now with the following
explicit index generator. This changes their uniform emission work, not
their gates or semantic channel. It applies only to FW's polynomial-sized
registers. LE retains its existing O(n^(5/2)(log n)^2) structural bound.
Full n-bit label/slot fields and O(sqrt n)-bit pool/bank indices retain
the widths and physical fees in proof.md.

Represent the fixed scan network in rectangular blocks: preprocessing;
pair code; validity over (i,j,v); then a block per N for prefixes,
selectors, masked extraction and new state fields. The dimensions are
w, B and a fixed constant number of gate stages. All ripple comparisons
and additions have B stages. A word extraction is the explicit parity
prefix over positions for each bit, so its references are at position i
or i-1 of the same block. Alive and partner-state versions refer to the
preceding N block at the same position/bit. Cross validation refers to
P_i, P_j and x_i,x_j; these are scanned fixed indices. Reserve a fresh
bit for every Boolean gate and intermediate state, within the previously
proved2^12w^2B gate/bit allowance. Constant-size gate templates can have
different rectangular blocks; no padding gates are added. The constant
number of block types have classically computable strides. References
are affine combinations of the loop indices and their block bases.
Offsets such as i-1, v+1 or the preceding N block are fixed neighbor
strides. No computed quantum value enters a wire-address formula.

Compute all strides/bases once per FW with schoolbook O((log n)^2)
bit arithmetic for each of a constant number of block types. An entire
family of N blocks has the same stride. Keep current base addresses
and a constant number of cursor words for each operand role. When an
inner loop advances, add its fixed stride to the cursor; when it wraps,
restore the saved outer base, advance that base by its stride, and
restart. Nested-loop depth and operand count are bounded constants.
Thus each gate needs only a constant number of O(log n)-bit additions,
comparisons, copies or increments, taking O(log n) bit operations.
Schoolbook multiplication by loop indices is not repeated per gate.

More formally, for an access base+sum_(d=1)^k s_d i_d with fixed k,
initialize k base/cursor words. At an inner-loop step cursor+=s_k;
at wrap assign cursor=outer_base, update the next outer_base by its
stride, and restart the inner loop. Zero-length loops are skipped by
ordinary endpoint tests. Reversing a block reverses its index order and
subtracts its strides. Therefore compute/copy/reverse can emit the same
acyclic Boolean network backwards without storing a gate transcript.
Gate scratch ids themselves advance or retreat by one. Repeated use
of a previously computed selector refers to its fixed stored bit.
Each emitted tuple explicitly includes its local wire indices; writing
these O(log n) bits is included, not treated as a zero-cost macro.

R_N views require a small variable-width exception, still within the
same bound. Let S(N)=sum_(v=3)^(N-1) ceil(log2 v). Initialize S(w-1)
by the exact grouped formula of proof.md Section3, taking O((log n)^3)
bit work once per FW. Descending N uses
S(N-1)=S(N)-ceil(log2(N-1)). The j_N width is known classically; compare
the bit-loop index with j_N and use the fixed zero input for padded
high bits. Access to a real R_N bit is the cursor S(N)+v. Updating the
prefix, width and loop endpoints takes O(log n) per N or emitted gate;
no table of S(N) is stored. PREP scans N upward with the inverse prefix
recurrence. Endpoint initialization can be repeated for the constant
number of passes, including reversal; it costs O((log n)^3) in total,
which is below O(w^2(log w)^2). All offsets have polynomial magnitude.

Every such ordinary emitter word fits
W_e=ceil(log2(2^24 n^4)) bits. Indeed the total circuit scratch and
fixed operands are bounded by2^20 n^3, and all the rectangular strides,
neighbor offsets and prefix views lie within a fixed enlargement of
that span. Signed temporary differences use one further bit. Ordinary
staging holds only a fixed number of W_e-bit cursors, loop counters,
block bases and stride words, fitting O(n) bits. Data-dependent program
frames and recursive contexts remain basis-state bank data, as before.
The local wire number is resolved by owner/register descriptors to the
complete physical slot field; the physical resolver and address fee
are unchanged. No classical array over the exponentially large pool
has acquired a short address through this construction.

The O(n^2 log n) Boolean gate network now costs O(n^2(log n)^2)
structural work, including resets, copies, cleanup and their emission.
The O(wr log w) PREP gate bound also has O(log n) emission and is
O(n^(3/2)(log n)^2), within the same allowance. Label work and GROUP
snapshots fit O(n^2). This sharper bound includes failed PREP tries
and all abort cleanup, since the existing fixed try cap is unchanged.
Work-conserving dictionary costs remain smaller. Summing levels and
batches gives O(n^3(log n)^2 C_0) FW work. The unchanged LE contribution
is already O(n^3(log n)^2 C_0). Thus no separate optimization of LE
is needed. Tree/decoder costs and all probability proofs remain those
of the complete preceding configuration. The physical bank factor is
still n^3(log n)^2, yielding the logarithmic power four in total time.
