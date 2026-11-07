# Complete ordinary-controller count and cache-extension cost

This proof file belongs to the marginal cache package. The main proof is
critical_third_cache_l2.md; the full selector and actual boundary are in
critical_third_cache_l2_selector.md; the identical fresh/saved phase map and
cache circuit are in critical_third_cache_l2_phase.md. Each claim cites all
four files. No resource bound assumes an external controller oracle.

Sections 1--8 reproduce critical_third_controller_resources.md, SHA-256
`25f5bbbefed19f2274decf10eb8812f2cf205362741fb52ec98b86b9461b04bc`.
That proof's exact reviewed hash is
`60920387ee118aadd902491c69f969c8df5205fbad0c007dc6cf609410c0259b`;
its review record has SHA-256
`8b724ba2e0e8a716810078d3349681dab451615306ab24064d918cef11dff885`.
The original selector source and its hashes are credited in main Section 9.
These are provenance records. All mathematical arguments follow here.

## 1. Result and scope

Put L=log2(n+2). The ordinary selector controller and its cache-free boundary have the following worst-case
bounds, on every input word and every coherent branch:

    literal controller gates per tick = O(n^2),
    fully charged controller work per tick = O(n^2 L^3),
    clean controller scratch = O(n^2) qubits,
    classical generator storage = O(n) bits.

The ordinary part includes every time test, instruction guard, cache-free boundary
permutation, public clock operation, bank address and inverse instruction.
It excludes the contender predicate itself. There are a constant number of
predicate or Grover macros per tick. If one such macro has fully charged
work W_pred(n), the selector before the cache extension and its literal inverse cost

    O(2^(n/2) [W_pred(n)+n^2 L^3]).                 (1)

If a predicate has P(n) literal gates and the cited O(L^3) generator bound
per local action, (1) is O(2^(n/2) [P(n)+n^2] L^3). Neither statement assumes
that an arbitrary oracle's gate count also bounds its generator work.

The final answer evaluator costs O(n^2 L^3) once in each direction and fits
in (1). No expected-time or amortized estimate is used here. The original
success proof, caps, source count and source model are unchanged.

## 2. Explicit sizes

Use the exact source parameters

    J=n+24, d=ceil(n/2)+32, q=d+2,
    r=ceil(log2(J+1)), B=2^d.

A stage bank has n candidate bits, d probe bits, three flags (allocation,
completion and verification), and two q-bit timestamps. Thus its length is

    b=n+d+3+2q+2QR=O(n).

The added 2QR cache bits per bank are carried in every bank copy and rotation.
Sections 1--8 count these fixed moves and their zero tests. Cache generation
itself is added in Section 9. R=32 and Q=O(n) are the main proof parameters.

The stage array and count have

    M=(J+1)b+r=O(n^2)

bits. All scratch arrays, record banks and addresses in the full circuit
have polynomial length in n. A public wire address therefore has O(L)
bits. The absolute tick tau has q=O(n) bits, but it is DATA for a time
comparison, not a wire address or an index into a B-entry table.

## 3. Ordinary instructions on the active front

Compute the q-bit elapsed time and the common metadata tests by ripple
Boolean circuits. These cost O(q+r) nodes. They can instead be recomputed
a constant number of times with the same bound. Clear them before the
boundary. No elapsed-time calculation is made for every archived bank.

For each j<d, a guard uses a constant number of comparisons of q-bit time
words, a prefix-zero test on at most j probes, and a constant number of
flag operations. Its Boolean size is O(q+j+r). A comparison or subtraction
is a ripple construction with a fixed number of Boolean nodes per bit.
It does not enumerate the represented integer values.

For a probe H, compute its own guard, apply its constant-length controlled
H word, and clear that guard immediately. The guard excludes the target
probe. Recompute a later prefix from the current probe wires; do not keep
a stale prefix across a probe H. There are at most two scheduled H guards
per j (the first and second H). This gives

    sum_(j<d) O(q+j+r)=O(dq+d^2+dr)=O(n^2).       (2)

Equation (2) holds even if malformed words enable several such instructions.
The emitted word still has the same size, and each guard's cleanup is valid
on all words because its operation leaves its read wires unchanged.

Forward-G, inverse-G and verification each use one OR of per-j guards.
Compute all of that macro's per-j flags, compute their OR, apply the macro
once under that OR, and reverse the flags. Each per-j flag has the size in
(2); the OR adds O(d) nodes. There are only three such macros. A macro
changes candidate/helper wires or the verification target, not its own
time/probe/metadata read controls. Thus its cleanup does not require a
second search through archive histories or a retained history per tick.

Candidate initialization adds O(n) constant-size controlled H words and
O(q+r) guard work. A controlled diffusion on the active candidate uses
O(n) gates for its zero/nonzero test and constant-size gates per qubit;
these are also within (2). The contender predicate in a Grover reflection
is counted in W_pred. All front-only control work is O(n^2) gates.

Full Boolean histories for a macro's guards have O(n^2) nodes. They can be
retained for that macro and reversed afterward. The H guards may instead
reuse one O(n)-size history at a time. Both schedules use at most O(n^2)
clean scratch and leave it zero before the boundary.

## 4. Boundary eligibility and fixed permutations

The pre-domain A_tau tests the count, front metadata, bank 1 being zero,
and the single-1 probe condition with elapsed time C_j. The metadata and
bank-zero tests have O(q+r+b) nodes. For each j, one can check probe j=1,
all other probes zero, and elapsed time C_j with O(d+q) nodes. Their OR
has O(d) nodes. Even this simple repeated implementation gives

    size(A_tau)=O(q+r+b+d(d+q))=O(n^2).            (3)

An optimized shared prefix/suffix test is unnecessary. The argument does
not assume that valid history words are the only inputs to A_tau.

F_tau is the cache-free part of the exact permutation: XOR tau+1 into front end, flip
completion, rotate the whole bank array left, XOR tau+1 into the new front
start, flip allocation, and increment the r-bit count modulo 2^r.
The rotation uses J adjacent whole-bank swaps, each with b bit swaps.
Each bit swap has three CNOTs. Consequently F_tau and its inverse cost

    O(Jb+q+r)=O(M)=O(n^2) gates.                  (4)

Ripple increment/decrement costs O(r) gates with O(r) reusable scratch.
It is a permutation on every r-bit word. There is no counter-sized loop.
All swaps and timestamp bit operations have public fixed wire operands.

To test B_tau=F_tau(A_tau), copy X to an M-bit temporary Z, apply F_tau^-1
to Z, evaluate A_tau(Z), undo that permutation, and clear Z against X.
Equations (3)-(4) give O(n^2) gates and O(n^2) scratch. X is unchanged.
The predicate result is computed once, not once for each output bit.

## 5. Total XOR evaluator and clean in-place boundary

Use the explicit evaluator in selector Section 6, first without its cache XOR. Compute a=A_tau(X) and
b=A_tau(F_tau^-1(X)) with clean helpers. XOR X into the arbitrary output Y.
Form F_tau(X) in the reusable temporary array and, bit by bit, XOR

    a AND (F_tau(X)_k XOR X_k)

into Y_k. One reusable difference bit needs a constant number of exact
gates per k. Reverse F_tau and clear the temporary. Do the same with
F_tau^-1 and b. Finally clear a and b by their original evaluators.

There are a fixed number of calls to (3), (4), and M-bit copy/correction
loops. Thus the complete XOR evaluator has O(n^2) literal gates. Its
scratch consists of one M-bit temporary array, O(n^2) eligibility history,
two retained flags, and O(n) arithmetic helpers. These can coexist within
O(n^2). No separate M-bit copy is allocated for each output bit.

Compute T_tau into one clean M-bit output, swap the input and output, then
XOR-evaluate T_tau once more. Since T_tau is a total involution, the old
input clears on every word. Two evaluations and one M-bit swap retain the
O(n^2) gate and scratch bounds. This is also the exact linear extension
on superpositions. It needs no measurement, reset or source inverse.

## 6. Archive access and final answer

Only the contender predicate scans the J archived pivots for tournament
edges. Its cost is already in W_pred. It reads each pivot from a fixed
public bank address. The controller does not wrap this predicate in another
J-fold loop of complete Grover calls. Every saved cache is read-only in this scan.

The final answer is the candidate in the rightmost archived bank with both
completion and verification flags 1, or zero. Compute the J joint flags
and their suffix ORs with O(J) nodes. For each bank, one selection flag
controls n CNOT/Toffoli output operations. Clear all flags afterward.
This gives O(Jn+J)=O(n^2) gates and at most O(n^2) clean scratch on every
word, including words with several marked banks. The suffix test makes
the output rule total and unique.

## 7. Fully charged public generation

Maintain tau as one q-bit public counter. Compute tau+1 in one q-bit public
buffer and copy any needed bits into known basis wires with a public bit
loop. Updates, copies and clearing cost O(q) local bit actions per tick.

For a guard loop, regenerate t_j, F_j, V_j and C_j one j at a time. A fixed
number of q-bit buffers is enough. A power of two is placed by its public
bit position. Fixed multiples and sums use O(q) ripple bit actions. Even
regenerating each constant from scratch at every j costs O(dq)=O(n^2)
public bit actions per full loop. Only a constant number of full loops is
needed. Reversing a loop regenerates the same constant for each j in
descending order. It does not store a d-by-q classical table.

These q-bit arithmetic tasks are already counted as O(q) bit actions.
They are not treated as unit-cost arithmetic and are not repeated for
each emitted gate within the corresponding guard. Once a constant is in
a buffer, an individual template uses one addressed bit of it.

Each local action in (2)-(4), each copy/swap/correction bit, each Boolean
DAG node and each answer bit has a fixed template. Its operand addresses
are obtained from bank bases and local offsets using a fixed number of
O(L)-bit additions or multiplications. For example, a bank bit has address
base+j*b+k. Compute the bank base once for its public loop or use that
formula directly. Schoolbook arithmetic on these short public integers
costs O(L^2) bit operations. Applying the model's O(L) indexed-access charge
gives O(L^3) fully charged work per local action, including gate addresses.

For Boolean histories, give each guard a fixed padded block with local
node offsets. A ripple template visits its nodes in forward or reverse
order using those offsets. Across j, reserve O(q+j+r) nodes per guard;
the cumulative base is a public polynomial in j, q and r, or is updated
by the same short-address addition. No gate address requires a fresh
traversal through earlier guards. Eligibility and output templates have
the same fixed block layout. Thus the bound also counts skipped constant
gates and loop transitions; it does not infer generation cost solely from
the number of physical gates that remain after simplification.

The total number of local actions is O(n^2) per tick, including constant
generation. This proves O(n^2 L^3) fully charged controller work. Retained
classical data consist of a fixed number of q-bit counters/constants and
O(L)-bit loop indices, bases and lengths. The fixed number of nested loops
does not create an n-level call stack. Their storage is O(n).

## 8. Caps and reverse execution

Every tick 0<=tau<B emits the same bounded families of templates. Quantum
control bits determine their action, not how many templates are generated.
The count therefore holds for failed searches, malformed archive words,
empty contender sets, and a cap during a probe or inverse correction.

For the known inverse, run public ticks backward and emit the inverse of
each template in reverse order. Regenerate the constants and addresses.
This has the same local-action count and scratch bound. The boundary is
reversed before the ordinary guards, so their old metadata is restored
before guard cleanup. No B-length instruction list or per-tick retained
history is required.

The factor B=2^(ceil(n/2)+32)=O(2^(n/2)) now yields (1). The sharper result
removes an unnecessary factor n from the controller allowance. It makes
no claim that the contender predicate itself has quadratic work.

## 9. Full cache boundary and total repeated work

The actual selector uses the cache extension proved in full in phase
Section 7 and selector Section 6. Add active-cache=0 to A_tau. Its O(Q)
zero test remains within (3), and bank 1's zero test includes its cache.
Let C_E be the exact whole class-cache XOR function, with unchanged E and
candidate. The actual F_(tau,E) first applies C_E at the front, then the
cache-free F_tau above. Its inverse restores the front by F_tau^-1 before
applying C_E again. Each C_E call costs O(Qn b_phase)=O(n^2 L) local actions,
b_phase=ceil(log2 n)+48, and uses O(n^2) clean scratch by the phase proof.

The total A/B XOR evaluator performs only a fixed number of calls to F
and F^-1. It computes each whole transformed temporary once and corrects
the output in one public bit loop. It does not recompute C_E per output
bit. Eligibility scratch, temporary/output arrays and C_E's shared helpers
coexist within O(n^2). Thus the actual boundary has O(n^2 L) literal actions,
and the full tick has O(n^2 L) including the complete contender predicate.
With the charged O(L^3) generation bound in Section 7, the complete selector
and actual inverse have the conservative cost O(2^(n/2)n^2 L^4). Main
Section 8.7 supplies the full aligned layout and generator with O(L^2)
charged work per local action, replacing general address products by fixed
shifts and additions. Its full loop/index charge gives the supported total
O(2^(n/2)n^2 L^3), with S_Q=O(n^2), S_C=O(n).
Main Section 8 includes all additive QND/prefix/compiler/endpoint work.

## 10. Complete selected online bit-controller proof

This is the actual classical controller chosen for the L2 package. The
preceding local-action and L3 fallback bounds establish the same circuit
semantics and conservative costs. The following complete whole-stream proof
replaces their public-generation allowance. It does not change a phase,
score, source operation, quantum boundary or success event.

The source critical_third_cache_generator_l2.md has exact SHA-256
`eb122317b103da59cdd982b29f863da27d1d932313e8b67861d1d212a64088f3`.
Sections 1--6 are reproduced below with local package cross-references.
Main Section 8.7 reproduces the complete aligned layout needed by this proof;
main Sections 8.1--8.2 give the literal exact arithmetic templates. The
selector and phase appendices give the total cached boundary and its fixed
number of complete cache calls. These are all required evidence files.

### 10.1. Statement and fixed premises

Let n=ceil(log2 N), L=log2(n+2). Use the complete coherent phase-cache
circuit in critical_third_phase_cache.md, SHA256
7e3811e6b06023d3a7094fd476503f69c4ce9a1ed9dab4f8efd5c476e8e989ad,
and the exact controller in critical_third_controller_resources.md,
SHA256 25f5bbbefed19f2274decf10eb8812f2cf205362741fb52ec98b86b9461b04bc.
Use the complete aligned layout reproduced in main Section 8.7 from
Sections 1--5 of critical_third_cache_generator.md,
SHA256 aef20cce6a000e53f437c2e1ebcfa5976a211e8071964cb0380d32ac348e5e49.
That last note proves the independent fallback
T=O(2^(n/2)n^2 L^3), S_C=O(n), S_Q=O(n^2), Q=O(n).

The stronger generator specified below has the joint bounds

    raw public bit/head actions per complete tick = O(n^2 L),
    charged complete tick = O(n^2 L^2),
    T=O(2^(n/2)n^2 L^2),
    S_C=O(n), S_Q=O(n^2), Q=O(n).                    (H1)

The circuit, phase map, tournament, source model and success proof do not
change. The prefix/cache idea is credited to peer submission
493303b5-06f6-4ee0-9596-d8cae89c8bb4 in the phase-cache note. The present
generator derivation is local and does not use an unavailable peer proof.

Put A=ceil(log2(M+2)), where M includes all allocated classical bits and
qubits in the new implementation. The layout and control space below give
M=O(n^2), hence A=O(L). All indexed operations receive the full A charge.
Every raw action counted below is an actual read, write, fixed-size logic
step, head move, endpoint test, or dispatch of one fixed-arity gate word.
The account does not discard constant-controlled or quantum-inert gates.

### 10.2. Literal controller and address use

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

### 10.3. Carries, loop ends and complete scans

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
are record counts Q, bank counts J+1, bit lengths n,q,b,r, or absolute
constant arithmetic lengths. The only exponential loop is the public
tick, handled separately in Section 10.5. Fixed loop lengths need only a
fixed number of strips of total O(n) bits, because loop depth and the
number of template families are fixed. They are built once with finite
charged polynomial work; a slow binary construction at setup is allowed.
They are reused, not rebuilt at every scan or tick.

A guard whose prefix scan has length j can use an endpoint moved with its
outer j loop. Alternatively, placing and clearing that endpoint by a full
O(n)-cell walk per guard costs O(n^2) raw work per tick; we include this
larger bound. A full guard splits into its q-, j- and r-bit scans. No list
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

### 10.4. Exhaustive repeated-template account

The arithmetic circuits are chosen as fixed ripple templates with a fixed
number of gates and history fields per bit. A controlled ripple adder,
comparison, Boolean prefix/OR, copy or swap needs a fixed number of such
passes. Forward and reverse passes are both counted. Their operand fields
have fixed local offsets and power-of-two strides. Padding a fixed number
of history fields per bit only changes space by a constant factor.

#### Fresh and saved class-cache evaluation

The phase word has

    b=ceil(log2 n)+48=Theta(L), R=32, P=n+b,
    Q=Theta(n), J=Theta(n), q=Theta(n), r=O(L).

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
cache permutation in phase Section 7 and selector Section 6, with the same call structure.

#### Scores and class edges

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

#### Ordinary controller, boundary copies and final answer

The ordinary controller has O(n) guards, each with a fixed number of scans
of total length O(q+j+r). Applying H3 and including O(n) endpoint placement
per guard gives

    sum_(j<d) O(q+j+r+A+n)=O(n^2).                       (H6)

The macro guard flags and their OR, front-only initialization, controlled
diffusion and their cleanup have the same bound. No guard skips its bit
scans because of a quantum control. Per-j time-constant generation is
counted in Section 10.5, not hidden in a unit word operation here.

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
q/j/r-bit guards, n-bit member/ID operations, row copies/swaps/corrections,
constant-width score words, and single flags. Extra setup for a short or
single-bit action is explicitly O(A); there are at most O(n^2) such record,
bank, candidate-bit or guard events per tick. Their O(n^2 A) raw total is
inside O(n^2 L). All outer-loop resets and address/base changes are among
these events. No per-gate A-bit address reset remains inside a bit scan.

### 10.5. Public constants, full clock and reverse execution

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

### 10.6. Space and additive work

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
and the main construction's space bounds. There is no new approximate
phase site or synthesis requirement.

Multiplying H7 by Bclk=O(2^(n/2)), and including the actual reverse word,
proves H1. Every additive polynomial and 2^O(L^4) is o(2^(n/2)); an absolute
constant covers the remaining small n, including the separate exact N=2
endpoint. This is a counted asymptotic absorption, not free preprocessing.

