# Required appendix: PSG2-DENSE-E grouped sum

## 1. Scope and source

This appendix, grover_dense.md, grover_dense_caps.md, grover_dense_compiler.md,
grover_dense_dense.md and grover_dense_bound.md define one PSG2-DENSE-E algorithm. Sections
2--7 give its complete exact sum circuit. Section 8 gives its uniform
polynomial constructor. The required new compiler appendix supplies the full
stored-tape execution proof, all other scan helpers and complete RUN(F).
No outside file is a mathematical premise.

The exact construction source files have these SHA256 hashes. The local
original oracle was d34f10863ec822ea9e1153f501eae1e7c1a9337a8d4ac4847f75a060aa2c0414;
its G1 circuit is adapted only to the explicit k=b+5 loops, 2048-list helper
bound and widened O(n) allocation proved in dense Sections 10--11.
Historical source pins below are credits, not outside proof premises.


- `rules.md`: `7be4f5f1137aea419a481bf31482bebc5a8f8cbb15dd2296872fce6dbad7a469`.
- `grover_stride_retry_l2.md`:
  `a24ae207804e3b494ae78d0c260adfc7255f97e637dc15d8f6725bce60d36745`.
- `grover_stride_retry_l2_compiler.md`:
  `697869d57d7603de1f39e712189cf26dc1cf2f8d8324ef32a103836c3bdf1243`.
- `grover_stride_retry_l2_caps.md`:
  `307dacf6e310e0b24878e8133d609528b0cfbb8d88b0be18313bea92d877b263`.

Put L=log2 n and D=log2(L+2). All logarithms below have base two. The source
main branch has n>=256 and

    n<=2R^2, R^2=O(nL), R<=ceil(n/2), u=floor(sqrt R),
    u<=v<=R, 0<b<=2v, k=b+5<=n+4, Wcap=O(n2^R).

The last bound on k follows from b<=D_input-1 and D_input<=n in PS_TREE_D.
The source's finite branches are retained. A zero-width level uses no oracle.

For fixed known residues c_j in [0,2^b), the circuit below implements

    |z>|A>|0> -> |z>|A+sum_j c_j z_j mod 2^b>|0>.       (G1)

It works for every bit string z and every b-bit A. Thus it also works on a
superposition. No data bit or partial sum is measured. The quantum scratch
is O(n). The exact Clifford+T gate count is O(nD), uniformly over all source
levels and residue lists. The exact gate and space bounds use Sections 2--7; Section 8 counts construction.

## 2. Parameters and small rows

Use the source's direct controlled-addition circuit if

    k<max(16,u).

This includes each constant-size row. Its count is O(kb+k)=O(R+1). For the
other rows set

    w=floor(log2(k)/2), d=ceil(log2(w+1)),
    g=ceil(k/w), h=min(b,max(1,floor(n/(g*d)))),
    J=ceil(b/h).                                       (G2)

Split the k query bits into g groups of at most w bits. A missing bit in the
last group is a fixed zero. Split the b weight columns into J consecutive
batches, each of length h except for the last batch. Let p be a batch's
first column, t its length, and r=b-p. Thus 1<=t<=h and t<=r.

All parameters are computed from public integers. They do not depend on
the query, a high label bit, or the unknown phase. Integer divisions,
lengths, masks and layouts are generated in counted polynomial work.

## 3. One group's full count table

For query bits z_0,...,z_(w-1), allocate d-bit zero rows C[m] for
0<=m<2^w. Process m=1,...,2^w-1 in increasing order. Put

    q=m AND (m-1), j=the position of the low 1 in m.

Copy C[q] to the zero row C[m] by d CNOTs. Then add z_j to C[m] with a
clean reversible d-bit ripple adder. Its other source bits are zero.
The query bit and all carry scratch are restored by that adder. This gives

    C[m]=sum_(j: bit_j(m)=1) z_j.

Since the result is at most w<2^d, there is no overflow. The table needs
O(2^w*d) exact gates and qubits. A standard clean ripple adder suffices;
each Toffoli has a fixed exact Clifford+T word. The parent addresses are
classical. Their generation is counted in Section 8, not treated as a
quantum memory lookup.

For group a and weight column q, form the known mask

    m_(a,q)=sum_(j in group a) bit_q(c_j) 2^(j's group position).

Copy the d bits of C[m_(a,q)] by CNOTs to a separate zero record B[a,q].
This is a copy in the computational basis, valid also on a superposition.
The copies remain entangled with the query as required. Reverse the full
table circuit. It clears C and its helpers while B[a,q] remains. There is
no quantum address or QRAM operation.

## 4. Prepare and sum one batch

For each of the g groups, build its table, copy the t selected counts into
B[a,p],...,B[a,p+t-1], then reverse the table. There are g*t*d record bits.
The table for only one group is present at a time.

The required batch sum, before its shift by p, is

    V=sum_(q=0)^(t-1) 2^q sum_(a=0)^(g-1) B[a,p+q].    (G3)

Use a reversible binary sum on the record bits. Here is a complete
linear-size sum method with an explicit space bound. A record bit in
position j of B[a,p+q] is a live bit of weight 2^(q+j). Set

    ell=min(r,t+ceil(log2(k+1))).

Live bits at weights at least 2^ell are omitted from the sum. They remain
unchanged in their record. They are multiples of 2^r when ell=r. When
ell<r, the nonnegative integer in G3 is less than k2^t<2^ell, so omitting
those weights is also valid.

At each column from low to high, take any three live bits a,b,c in that
column and put these values in two fresh zero target bits:

    s=a XOR b XOR c,
    e=(a AND b) XOR (a AND c) XOR (b AND c).

Three CNOTs compute s. Three Toffolis compute e. All three inputs are
retained without change. Mark them inactive; make s live at this column
and e live at the next column. If that next column is ell, omit the e
target and its gates. There is no computed bit that is erased. Repeat
until each column has at most two live bits.

Let B0=g*t*d. Each full step reduces the number of live bits by one. A
top-column step reduces it by two. Thus there are at most B0 steps. They
allocate at most 2B0 target/history bits in total. Retaining every input
and intermediate value therefore uses at most 3B0 bits before the final
rows. This bound does not assume that an inactive bit was cleared.

Copy the at most two live bits per column into two separate ell-bit zero
rows, with absent bits set to zero. Copy the first row to an ell-bit zero
V register, then add the second row to V with a clean ripple adder modulo
2^ell. This uses O(ell) gates and qubits. The complete sum stage has

    O(g*t*d+b) gates and qubits.                        (G4)

The compressor order, row copies and addresses depend only on the public
record layout. All gates are exact. The source records stay present.

## 5. Add, then clear the whole batch

Add V into accumulator bits p,...,b-1 modulo 2^r, with zero source padding
above V if needed. This changes A to A+2^p V mod 2^b. It costs O(b) gates
and O(b) reusable scratch. It preserves V.

Now reverse the sum circuit in Section 4, including its final adder and
row copies. This clears V, both rows, and every compressor target. It
leaves all B records present. For each group:

1. Build its full count table again.
2. Apply the same selected CNOT copies to its B records. Each becomes zero.
3. Reverse the table circuit and clear its scratch.

The accumulator is the only changed register apart from its prescribed
translation. No old batch record or partial sum survives. Apply these
steps to all batches in increasing p. The result is exactly G1, because

    sum_(p batches) 2^p V = sum_j c_j z_j mod 2^b.

Running this entire circuit backwards gives its clean inverse. The proof
holds on every computational basis input, so linearity proves coherence.

## 6. Gate and quantum space bounds

For a grouped row, the complete G1 circuit and its inverse, a comparison
with e, the at most 2048 found-string tests, and Grover diffusion have
total count

    G=O(J*g*2^w*d + g*b*d + J*b + k+b).                 (G5)

All forward and reverse table runs are included. Count preparation and
its clearing each build and reverse each table; this changes only the
absolute constant. G4 includes all retained history and its reverse.

For x=n/(g*d), floor(x)>=x/2 when x>=2. For x<2, h>=1. In both cases,

    J<=1+2b*g*d/n.                                    (G6)

The source bounds give log R=Theta(L). On the grouped branch k>=u and
u>=sqrt(R)/2 for R>=4, while k<=2R+5. Consequently

    w=Theta(L), d=Theta(D), g=O(R/L),
    2^w<=sqrt k=O(sqrt R), J=O(d).

Insert these in G5. Its terms are bounded by

    O(R^2*d/L + R^(3/2)*d^2/L + R*d + R).

Since d/sqrt R is bounded, this is O(R^2*d/L)=O(nD). Direct rows cost
O(R+1), and have the same upper bound. Finite small values are covered
by absolute outside constants. There is no distributional assumption.

For space, g*d<=(k/w+1)d<=k+d<=k+w=O(n), using d<=w and k<=n+4.
If g*d<=n, the h choice gives g*h*d<=n. If g*d>n then h=1 and
record bits are g*d=O(n). Thus every batch has at most max(n,g*d)=O(n)
record bits, including the h=1 case. Also2^w*d<=sqrt(k)*d<=k<=n+4
for grouped k>=16. G4, the table, all retained history, records,
accumulator, ripple scratch and query therefore total O(n) qubits.
The original phase register and dense depth-first source stack add only
O(n), as proved in the required dense appendix Section 11. Every retry
clears or releases the attempt before new children are built.

The construction is valid for every partial row. It does not assume
b>=u. Rows with k<u use the direct circuit. The last short group and
batch use the zero padding and actual t specified above. All zero, full,
and repeated column masks are allowed.

## 7. Exact source and selection behavior

The only label data used in this circuit are the same known c_j as in
the source. Each c_j is the same b-bit residue of the same signed child
label. G1 computes precisely the same f(z), for every input, including
negative child labels after their prescribed residue conversion.

Use Section 9's explicit copy/G1/uncopy wrapper for the first coherent
f(y) computation and measurement, with G1's fixed query addresses. In each
search trial use it on the separate query, compare with the same e,
exclude the same found strings, mark, and apply its inverse. The original
phase register remains untouched by search. All trial limits, random
iteration counts, classical verification, cyclic selection and phase
clearing remain those of the source.

Thus the state map, every measured distribution, and every success/failure
probability are unchanged. In particular the source's low-residue
selection law and unused-high-label argument remain exact. This is not
an approximation to f, and no empirical residue law is used. This arithmetic
replacement adds no source calls. Main/caps and dense Section 9 prove the
actual Qcap_dense guard, old precision/pool, model and full-secret success.

## 8. Complete uniform constructor and allocator

The constructor is a uniform classical bit program. It takes n, b, u and
the actual known k by b residue bits. It runs only after the main weighted
check. Its only label data are those low residues. The following fixed
loops specify its wire allocation and every emitted operation.

Reserve the query and b-bit accumulator, then a reusable zero scratch
pool. An allocation pointer gives the next pool wire number. A saved
pointer marks the start of each table or batch. Assign consecutive wire
numbers to a requested row and update the pointer by ordinary bit
arithmetic. Maintain the largest pointer as the physical pool bound.
After a clean reverse, reset the allocation pointer to its saved value;
this changes only the classical map. It does not erase a quantum bit.
All pool bits reused at that point have been proved zero in Sections 3--5.
The maximum pool is O(n) by Section 6. No query-dependent allocator is used.

For a batch of actual length t, assign its g*t*d record wires first. Loop
through the groups in increasing order. Save the allocation pointer,
assign 2^w count rows and the O(d) clean ripple helpers, and emit the
Section 3 table word in increasing mask order. The parent m AND(m-1)
and its low-bit position are computed by bit scans of the m counter.
For each of this batch's columns, read all w corresponding known residue
bits, form its mask by shifts/bit copies, and emit its d selected CNOTs.
Emit the table word's exact inverse in reverse order. Restore the saved
allocation pointer. This completes the group, with its records retained.
For the partial group, nonexistent query bits are fixed zeros and use
fixed inert or omitted templates; every retained template slot is counted.

Next create one classical list per sum column 0,...,ell-1. Each list item
is a wire number. Append the record bit wire numbers at their prescribed
weights. Ignore only the high weights justified in Section 4. Process
columns in increasing order. While a list has at least three live items,
remove its last three items, allocate the sum/carry target wires, emit
exactly the three CNOTs and up to three Toffolis of Section 4, then append
the new live wire numbers to the current and next lists. A list length
counter decides this public loop. At most B0 such steps are performed,
by the live-bit proof. The original wire numbers remain in the emitted
word and allocation map, even after their list item is removed. They are
never treated as cleared. A top carry target/gate is omitted as specified.

Allocate the two dense rows and V. Emit the surviving row CNOTs, V copy
and ripple sum. Save this sum subword, then emit the padded ripple add
of V into the accumulator. Emit the saved sum subword's inverse. Reset
the pool pointer to just after the records, since all later pool wires
are now zero. Run the same group-table construction and selected copies
again to clear the records. Reverse each table and restore its pointer.
At the batch end restore the pointer to the batch mark. Continue with the
next p. This emits the complete G1 word, with actual reusable wire numbers.

There is no arbitrary-width arithmetic instruction in the output. Every
copy, clean adder and comparison is expanded into NOT/CNOT/Toffoli gates;
each Toffoli is expanded by a fixed exact Clifford+T word. A finite
program generates the ripple word described in compiler Part A. One may
also use the following explicit clean Cuccaro word for an m-bit add:
with source a, target b and a zero carry c, let c_i=a_(i-1) for i>0 and
c_0=c. For i increasing emit CNOT(a_i,b_i), CNOT(a_i,c_i),
Toffoli(c_i,b_i;a_i). Then for i decreasing emit
Toffoli(c_i,b_i;a_i), CNOT(a_i,c_i), CNOT(c_i,b_i).
This changes b to a+b mod2^m and restores a,c. It has O(m) gates.
It also implements the add of one query bit in Section 3 by using that
bit as a_0 and fixed zero source bits above it. All these source bits
and carry are restored. A missing top carry is never produced and erased.

For reversal, keep an explicitly written temporary copy of each table or
sum subword, then read its instructions in reverse and emit their finite
inverse tags. No unknown quantum state or source preparation is reversed.
The temporary copies have at most the final word's polynomial length.
All temporary tapes, tags, operand bits and markers are written, read and
cleared by actual bit operations. Their construction work is counted even
if the main program later reuses the resulting word many times.

Here are complete storage and work bounds for this constructor. A wire
number, list length, mask, address or public loop counter has a=O(L) bits.
The table/record/list maps have O(n) active entries. They occupy O(nL)
bits. Residues have O(kb)=O(nL) bits. The output and temporary subwords
have O((H+1)a)=O(nL log2(L+2)) bits, where H=O(n log2(L+2)) is the proved
G1 slot bound. A fixed number of output/subword copies is sufficient:
process one group and one sum subword at a time. No J-fold history tape
is retained. Thus the constructor uses O(n^2) classical bits while all
source labels, the output program and quantum pool are also allocated.

This work bound is separate from gate count. Each public loop listed
above makes O(H+kb+n) list, mask-bit, instruction or local index actions.
Use schoolbook O(a^2) raw bit work for any required short-word shift,
add, multiplication, comparison, map access or queue update; a direct
indexed entry read/write uses O(a) bits. Conservatively debit O(a) to
each raw operation during construction, including all actual indexed
reads/writes. Writing every O(a)-bit gate frame is included in the same
allowance. A complete conservative charged construction bound is

    O((H+kb+n)*a^3)=O(n L^4).                         (G10)

A list operation touches a fixed number of indexed entries, not an
uncounted list scan. Each column's endpoint and every loop-counter test
are included. An elementary opcode has a fixed number of operands, so
its literal serialization needs no variable-arity operation. Ordinary
classical indexed memory is used only with its full address debit. No
QRAM or free preloaded description is used. Direct rows use the same allocator/output procedure. For each c_j,
prepare a b-bit zero source as c_j*z_j by CNOTs from z_j in the known 1
positions of c_j. Apply the clean ripple add into A, then undo those
CNOTs. The adder restores its source and carry. This is the direct
controlled-addition word, with O(b) gates and reusable qubits per row.
Its weight reads and all instruction bits fit G10 as well.

Initialize the physical zero pool in O(n) quantum actions, with every
indexed gate/address cost charged. At the end of an attempt clear every
program/marker bit explicitly and reset or release every quantum bit.
Program erasure and pool resets have polynomial charged work and the
same peak-space bounds. The complete one-off signed output arithmetic,
classical verification, cyclic rank projection, measurements and cap work is
also paid polynomial work, as specified in main Section 4.2 and compiler
Part A. Main Section 9.5 absorbs these counted polynomials using v>=u.

## 9. Integration with the exact stored program

The G1 word is fixed by n, b, u and the known residues. Build it once per
attempt. Its query-wire addresses stay fixed. For the initial f(y) map on
the original phase register, initialize this separate query z and the
accumulator A to zero. Apply k CNOTs from y to z, replay G1 on z,A, then
apply those same k CNOTs again. Since G1 preserves z and clears all its
helpers, the result is |y>|0>_z|f(y)>_A with clean scratch. This identity
holds with every reference system by linearity. Only then measure/reset A.
The query is now zero and is reused for discovery. The wrapper costs
exactly 2k additional indexed gates, with their full address debit, and
uses the already allocated query register. It needs no second G1 program,
wire remapping or uncounted address change. Its one-off charge fits the
polynomial work in Section 8 and main Section 9.5.

The measured e and each new found string affect only the separate
comparison/list scans, not G1. Compiler Part B reads every stored frame's
O(L) bits, copies its operand words, emits the gate with its full indexed
debit, and counts all tags, markers, head moves and reverse steps. Two
G1 passes and the separate helper scans have O(nL log2(L+2)) charged work
per full iteration. All quantum and classical bounds in Sections 6 and 8
hold jointly. Main Section 9.5 proves all other full-solver terms against
the actual pre-envelope work. The required bound appendix then proves
the selected 177/250 time and source envelopes with kappa=5/32.

The exact source hashes above record reuse. All circuit, allocator,
controller, probability and cap arguments required by this configuration
are inside the six package proof files. No research-note condition or
review verdict is a premise.
