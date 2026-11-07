# Complete bit-stream generator for the adaptive L2 cache solver

This is the actual online controller and memory layout for the algorithm in
[proof.md](proof.md). All five claims cite this file and the full main,
selector and phase proofs. Sections 1--6 below reproduce the entire bit-stream
construction; Appendix A reproduces the complete aligned layout it uses.
The deterministic complete-scan count includes ready-address construction,
tape-head motion, carry returns, marked loop ends, short-scan setup, public
constants and the actual reverse stream. The count applies to each full
tick on every branch.

Direct sources: critical_third_cache_generator_l2.md, SHA-256
`eb122317b103da59cdd982b29f863da27d1d932313e8b67861d1d212a64088f3`,
and aligned-layout source critical_third_cache_generator.md, SHA-256
`aef20cce6a000e53f437c2e1ebcfa5976a211e8071964cb0380d32ac348e5e49`.
The literal cache/controller source proofs have SHA-256 respectively
`7e3811e6b06023d3a7094fd476503f69c4ce9a1ed9dab4f8efd5c476e8e989ad` and
`25f5bbbefed19f2274decf10eb8812f2cf205362741fb52ec98b86b9461b04bc`.
All needed logical constructions are reproduced in this package. Source
credits, including the note-first peer chain, remain in proof.md Section 9.
No source verdict or external proof is a mathematical premise.

## 1. Statement and fixed premises

Let n=ceil(log2 N), L=log2(n+2). In this generator put J=n+24,
d=ceil(n/2)+32, Bclk=2^d, q=d+2 and r_ctl=ceil(log2(J+1)).
The symbol r_ctl is the selector count width; the malformed-copy budget
is denoted r in the main proof. Use the complete coherent phase-cache circuit in
[critical_third_adaptive_cache_l2_phase.md](critical_third_adaptive_cache_l2_phase.md),
Sections 3--8, and the exact controller in
[critical_third_adaptive_cache_l2_selector.md](critical_third_adaptive_cache_l2_selector.md),
including Appendix R. Use the full aligned layout in Appendix A below.
Their literal gate counts, total Boolean functions and cleanup are proved
inside this package. No external circuit or controller is supplied.

The online generator specified below has the joint bounds

    raw public bit/head actions per complete tick = O(n^2 L),
    charged complete tick = O(n^2 L^2),
    T=O(2^(n/2)n^2 L^2),
    S_C=O(n), S_Q=O(n^2), Q=O(n).                    (H1)

The circuit, phase map, tournament, source model and success proof do not
change. The prefix/cache idea is credited to peer submission
493303b5-06f6-4ee0-9596-d8cae89c8bb4 in the phase proof and main Section 9. The present
generator derivation is local and uses no peer proof as a premise.

Put A=ceil(log2(M+2)), where M includes all allocated classical bits and
qubits in the new implementation. The layout and control space below give
M=O(n^2), hence A=O(L). All indexed operations receive the full A charge.
Every raw action counted below is an actual read, write, fixed-size logic
step, head move, endpoint test, or dispatch of one fixed-arity gate word.
The account does not discard constant-controlled or quantum-inert gates.

## 2. Literal controller and address use

The rules require a uniform classical controller and count bit work,
circuit generation and memory access. They permit classically chosen
gates on arbitrary indexed wires, with the A-bit address charge. They do
not require a new serialized instruction/address tape for each gate.
Choose a uniform finite-program, fixed-multitape bit controller. Its local
operations read/write one bit, move a head one cell, or change finite
control. Each is counted. To be conservative, debit O(A) fully charged
work for every such operation, including a head move or endpoint read,
even if it is a local sequential tape operation. No numerical word
operation is a unit-cost controller instruction.

Keep a fixed number of A-bit operand-address words in fixed fields. A gate
template names those fields, just as an indexed gate names its ready
classical address. Dispatch uses their current values directly and pays
A for each of its fixed number of operand uses. It does not copy them to
a fresh instruction, or serially reread A bits before paying that charge.
If an address must be constructed, copied, changed or inspected, the actual
bit/head operations are counted separately. The address charge is still
paid on each of those indexed bit operations and on the resulting gate.

A ripple bit gadget uses a fixed list of operand fields. Initialize all
of them once at the start of its bit scan, using O(A) raw bit actions.
The list includes any neighboring carry/history bits and the fixed outer
enable. Inside the gadget, finite control selects the fields; it does not
construct a new address for each gate. Moving to the next bit adds or
subtracts a fixed power-of-two stride to each ready address. The aligned
layout supplies that stride. A fixed number of fields suffices, since
every bit gadget has fixed size and the template-loop depth is fixed.

Tape heads implement pointer-bit scans. For one pointer increment, start
at its low-bit marker, read and flip its trailing 1 bits, then read and
flip the first 0 bit, or detect the marked high end on full overflow.
Return the head to its low marker. Decrement uses trailing 0 bits instead.
Each visited pointer bit needs a fixed number of reads, writes, head moves
and finite-control tests. There is no separate binary bit cursor to copy,
increment or clear. Every actual head move is charged. The fixed number
of head locations can be included as O(A) bits each in the space account;
the controller does not maintain redundant binary copies of their locations.
This is an explicit bit controller, not an assumed constant-time increment.

## 3. Carries, loop ends and complete scans

For m consecutive increments of any w-bit word, bit h changes at most
floor(m/2^h)+1 times. Summing over h=0,...,w-1 gives at most

    2m+w                                                   (H2)

bit changes. The increment algorithm visits precisely its changed bits,
apart from a fixed end/return test. Thus all its reads, writes, head moves,
carry tests and returns cost O(m+w) raw actions. The same proof applies
to decrement and to a fixed power-of-two stride: ignore the unchanged
low bits. It applies to any starting value and to wraparound. Reversing
a complete sequence gives the same bound. Address words have w<=A.

Loop termination must not make a full A-bit comparison after every gate.
Use marked classical loop strips. A strip for a scan of m positions has
m positions and a marked endpoint. A head visits one position per bit
gadget; the endpoint symbol ends the loop. Its forward or reverse traversal
and rewind use O(m+1) head moves and symbol tests. This includes every
loop termination test. Resetting the scan means returning the head, not
clearing an A-bit counter after each gadget.

All repeated template loop bounds are at most Cn, for an absolute C: they
are record counts Q, bank counts J+1, bit lengths n,q,b,r_ctl, or absolute
constant arithmetic lengths. The only exponential loop is the public
tick, handled separately in Section 5. Fixed loop lengths need only a
fixed number of strips of total O(n) bits, because loop depth and the
number of template families are fixed. They are built once with finite
charged polynomial work; a slow binary construction at setup is allowed.
They are reused, not rebuilt at every scan or tick.

A guard whose prefix scan has length j can use an endpoint moved with its
outer j loop. Alternatively, placing and clearing that endpoint by a full
O(n)-cell walk per guard costs O(n^2) raw work per tick; we include this
larger bound. A full guard splits into its q-, j- and r_ctl-bit scans. No list
of all j-specific strips is allocated. The outer loop can maintain its
numeric j by O(A) raw work per iteration when constants or bases need it.
That cost is included in the per-scan O(A) setup below.

Consequently, a constant number of full sequential bit passes over length
m, using a fixed number of ready operand pointers, costs

    O(m+A) raw actions.                                  (H3)

This includes initial address construction, all carry walks in H2, every
bit gadget, loop endpoints, forward/reverse pointer motion and head returns.
The statement holds also for m=0 or constant m: the O(A) setup remains.
It does not claim constant worst-case work for one gate. An isolated long
carry can cost O(A); H3 counts the complete deterministic scan containing it.

## 4. Exhaustive repeated-template account

The arithmetic circuits are chosen as fixed ripple templates with a fixed
number of gates and history fields per bit. A controlled ripple adder,
comparison, Boolean prefix/OR, copy or swap needs a fixed number of such
passes. Forward and reverse passes are both counted. Their operand fields
have fixed local offsets and power-of-two strides. Padding a fixed number
of history fields per bit only changes space by a constant factor.

### Fresh and saved class-cache evaluation

The phase word has

    b=ceil(log2 n)+48=Theta(L), R=32, P=n+b,
    Q=Theta(n), J=Theta(n), q=Theta(n), r_ctl=O(L).

For each of at most two class members, each of Q records and every public
j=0,...,n-1, the complete controlled b-bit window adder uses H3. Set up its
window, candidate, accumulator and carry addresses in O(A) raw work. The
window start n-j is computed only at this setup. Use the same complete
adder template even if its candidate/control bit is zero. Its forward and
reverse words cost O(b+A) raw actions. Therefore a complete class cache has

    O(Qn(b+A)+Q(n+A)+Q A)=O(n^2 L) raw actions.            (H4)

The second term allows even an n-bit class-member addition and its undo
once per record. The last term includes every constant-width R-bit cache
copy and its full address setup. They are not assumed to have constant raw
setup. A fixed number of H4 calls occurs at a tick's cache boundary. There
is no call per boundary-output bit. This is the total XOR evaluator and
cache permutation in the fixed packaged proof, with the same call structure.

### Scores and class edges

There are O(JQ) record terms per complete contender predicate, with a fixed
number of member/orientation scans. The trigonometric word has an absolute
fixed gate count K, including its fixed precision and degree. Generating
every one of these K gates by the conservative O(A) raw address method
costs O(KA)=O(A) per record term. All K gates and all constant generation
are charged. Their large absolute constant does not depend on n. This
bound also covers the four R-bit linear combinations, record validity,
private-axis access and clearing of each term's constant-width helpers.

The full score-sum width is s=Theta(log(Q+2))=Theta(L). One addition or
subtraction and its complete inverse cost O(s+A) raw work by H3. The sign
copy is O(A) including setup. Thus every record term costs O(L+A), and all
score scans, copied signs and their undo cost

    O(JQ(L+A))=O(n^2 L).                                (H5)

Class validity, canonical ID order, equality and the per-bank contender
flags add O(J(n+A))=O(n^2) raw work. Flag OR/AND history and its reverse
add O(J+A). Axis-tape rewinds add O(JQ). Every saved bank is visited by
public row/slot indices, with O(A) setup per record or scan already in H5.
No source-dependent address is used. The full fresh contender cache and
its undo contribute H4 once each, not once per saved pivot.

### Ordinary controller, boundary copies and final answer

The ordinary controller has O(n) guards, each with a fixed number of scans
of total length O(q+j+r_ctl). Applying H3 and including O(n) endpoint placement
per guard gives

    sum_(j<d) O(q+j+r_ctl+A+n)=O(n^2).                       (H6)

The macro guard flags and their OR, front-only initialization, controlled
diffusion and their cleanup have the same bound. No guard skips its bit
scans because of a quantum control. Per-j time-constant generation is
counted in Section 5, not hidden in a unit word operation here.

The boundary's additional cache-zero test has O(Q) bits. Its other
eligibility tests have H6 size. Each bank permutation, temporary copy,
swap and XOR correction has a fixed number of J row scans of O(n) bits.
These cost O(J(n+A))=O(n^2) raw work by H3. Full-array scans can use these
two loops; there is no O(n^2)-cell classical loop strip. A fixed number
of those calls is used by the total XOR evaluator and involution. Add
the fixed number of H4 cache calls for a total O(n^2 L) boundary bound.
The final rightmost-marked-bank answer evaluator has O(Jn) bit actions
in complete scans and O(J) suffix/flag actions, so it costs O(n^2) raw
work once in each direction.

These cases cover every repeated template: b- and s-bit arithmetic,
q/j/r_ctl-bit guards, n-bit member/ID operations, row copies/swaps/corrections,
constant-width score words, and single flags. Extra setup for a short or
single-bit action is explicitly O(A); there are at most O(n^2) such record,
bank, candidate-bit or guard events per tick. Their O(n^2 A) raw total is
inside O(n^2 L). All outer-loop resets and address/base changes are among
these events. No per-gate A-bit address reset remains inside a bit scan.

## 5. Public constants, full clock and reverse execution

The public time words have q=O(n) bits. Maintain tau and tau+1 in a fixed
number of q-bit buffers. Even a full q-bit increment/copy/clear at every
tick costs O(q+A)=O(n) raw work. The tick limit is exactly 2^d. A binary
overflow/end-marker test, or one complete q-bit limit test, costs O(q)
per tick and is included. No exponential loop strip or schedule is stored.

For each public j, generate

    t_j=2^j, F_j=t_j-1+2j,
    V_j=3t_j+2j+1, C_j=3t_j+2j+2,

and any required interval endpoints in a fixed number of q-bit buffers.
Zeroing a buffer, putting its power-of-two bit in place, and fixed multiples
or sums take a fixed number of complete q-bit scans. Even walking to bit j
or resetting a marker costs O(q). Every public bit read/write, carry,
comparison and buffer reset is included. This is O(q+A) raw work per j and
O(n^2) per complete guard loop. Only a fixed number of full loops occurs
per tick. A constant buffer is consumed one addressed bit at a time inside
its guard; it is not regenerated or fully copied before each guard gate.

The inverse controller runs tau=Bclk-1,...,0 and reverses all macro, loop
and gate orders. It can prepare each reverse scan's endpoint addresses by
O(A) raw bit work. H2 holds for decrements and for arbitrary starting
addresses, so H3--H6 apply without an average over input states or ticks.
Descending j loops regenerate the same public time constants. Boundary
undo precedes the older ordinary guards, as in the exact source circuit.
No history across ticks, success-conditioned stop, or expected-time
argument enters this generator account.

All Bclk ticks emit the complete bounded template word on every quantum
branch, including unused banks, failed probes and a final incomplete search.
H4--H6 and the explicit public constants therefore give O(n^2 L) raw
actions per tick. Debit O(A) to each action, to each gate dispatch and to
every use of its fixed number of ready address operands. Thus a tick has

    O(n^2 L A)=O(n^2 L^2) fully charged work.             (H7)

The deterministic carry amortization is over complete forward/reverse
public scans. It is never over sampled data, successful searches or the
enabled subsequence of a quantum-controlled word.

## 6. Space and additive work

The fixed number of loop strips uses O(n) classical bits. Public N, private
axes and a fixed number of q-bit buffers use O(n). Current operand words,
layout constants, finite loop state and head locations add O(A) each for
a fixed number of fields/heads. The fixed program has no n-deep call stack.
The full classical peak is O(n). No measured label, prefix, pivot or cache
table is created. All padded quantum banks, prefixes, current caches,
histories and reusable scratch remain O(n^2). The new loop strips do not
alter source acquisition, so Q=O(n).

Initialization of the strips, aligned layout and fixed coefficients is
charged polynomial work. Prefix setup/undo can retain the conservative
O(n^3 L^2) charged implementation; it is not repeated at every tick.
Source acquisition, QND preparation/undo, answer copying, fresh helpers,
all allocated zero bits and the trit endpoint remain charged additive
polynomials. The unchanged finite phase compiler has 2^O(L^4) total work
and the source construction's space bounds. There is no new approximate
phase site or synthesis requirement.

Multiplying H7 by Bclk=O(2^(n/2)), and including the actual reverse word,
proves H1. Every additive polynomial and 2^O(L^4) is o(2^(n/2)); an absolute
constant covers the remaining small n, including the separate exact N=2
endpoint. This is a counted asymptotic absorption, not free preprocessing.


## Appendix A. Complete aligned layout

Replace each finite row/slot field length m by the least power of two at
least max(1,m). Its new length is less than 2 max(1,m). Use separate arrays
for the fixed number of field types when a heterogeneous bank would make
a direct bit address need a general product. Pad the record count, bank
count and member count to powers of two for address layout only. The loops
can still use the actual counts. At most a fixed number of dimensions is
used. This multiplies total allocation by only a fixed constant.

For example, a prefix bit address is

    prefix_base + (record << prefix_row_shift) + bit,

and an archived cache bit address is

    cache_base + (bank << bank_shift)
               + (member << member_shift) + (record << R_shift) + bit.

Here 2^R_shift is the fixed power-of-two width R=32; each other shift is a
public layout constant. Empty padded slots are allocated and initialized,
but are not new tournament vertices or new source copies. A window bit is
prefix_base+(record << prefix_row_shift)+(n-j)+i. The subtraction and
addition use O(A) bit actions. No product of two variable address words is
needed. Bank rotations use the same permutation on each field array.

Give every Boolean guard history a padded row of O(n) bits, with one row
per public j. This is O(n^2) qubits even when a shorter guard needs fewer
nodes. A ripple node has a fixed number of fields per bit. Its address is
obtained by a fixed shift and a fixed number of additions. Fixed-size
gadgets use fixed local offsets. Copies, swaps and output corrections use
the same fixed row/bit coordinates. Selector Appendix R already limits
the number of live Boolean histories to O(n^2).

Setup computes the shifts and bases by bounded bit scans, counts all padded
initialization, and uses only polynomial work. The quantum allocation stays
O(n^2). Addresses, layout constants and a fixed number of loop indices use
O(L) bits each. Public N, axes and O(n)-bit time constants still use O(n)
bits in total. Padding creates no classical record table.

