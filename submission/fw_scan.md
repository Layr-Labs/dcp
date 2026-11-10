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

Uniform generation uses fixed nested loops for scans and ripple gates.
Every circuit wire has a polynomial-sized local index and its arithmetic
is charged O((log n)^2) bit operations per gate, as in proof.md (P7).
Thus the O(n^2 log n) Boolean gates, initialization, resets and clean
reversal use O(n^2(log n)^3) structural work per FW. PREP still costs
O(wr(log n)^3) and GROUP/label postprocessing O(n^2), within this bound.
Full physical operand resolution and fees remain in the bank ledger.
The separately counted standalone implementation may retain its previous
looser full-handle O(n^(5/2)(log n)^2) bound. This file changes no
parameters, supplier caps, space envelope, source count or error model.
