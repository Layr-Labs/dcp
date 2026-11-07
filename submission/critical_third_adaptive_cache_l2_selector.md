# A globally bounded coherent tournament selector

This file proves the exact search, public clock, cap coupling and baseline
controller. The complete adaptive solver is in [proof.md](proof.md). It uses
the cache predicate and cache-extended boundary in
[critical_third_adaptive_cache_l2_phase.md](critical_third_adaptive_cache_l2_phase.md),
Sections 6--7, in place of the baseline predicate cost and F_tau/T_tau below.
That file proves the extension is a total controlled involution and preserves
the pivot law. The semantic tick schedule and caps below are unchanged.
The complete ordinary-controller count is proved in Appendix R below.
The actual aligned layout and full online bit-stream controller are proved in
[critical_third_adaptive_cache_l2_generator.md](critical_third_adaptive_cache_l2_generator.md).

The direct source is critical_third_adaptive_clock_selector.md, SHA-256
`757849df60d8f2efb5eb151e6bf09abe1f02a33ec9866b0cad0070103b09a98b`,
which reproduces critical_third_selector_cost.md at SHA-256
`1cfcac197add3d36a9e74fb59e6956d826af6227e52469db202f82ea0c1d0c37`.
Appendix R directly adapts critical_third_controller_resources.md, SHA-256
`25f5bbbefed19f2274decf10eb8812f2cf205362741fb52ec98b86b9461b04bc`.
No source verdict is a premise. All algorithms and counts needed here are
included in these packaged proof files. Symbols B,d,r below are local.

## 1. Statement and public caps

Let K=2^n, n>=1. A known exact reversible predicate gives the orientation
of a tournament on C<=K valid addresses. The tournament has a Condorcet
winner: one vertex beats every other vertex. No ordering or transitivity
of the other edges is assumed. Predicate data are coherent read-only
computational registers. An edge is computed from them by known gates;
no source inverse or extra source copy is supplied.

The predicate implementation is assumed to have total XOR-output Boolean
circuits, O(n^2) clean reusable workspace, and a streamed known forward and
inverse generator using O(n) classical space. P(n) below counts the complete
contender predicate with J pivot slots. The predicate in proof.md Sections 4 and 8 and the packaged cache proof
has these properties.
The read-only quantum data themselves occupy O(n^2) qubits; no larger input
oracle or table is excluded from the storage bound.

Put

    J=n+24,
    B=2^(ceil(n/2)+32),
    d=ceil(n/2)+32=log_2 B.

The physical selector is one known unitary with exactly B public ticks.
It retains at most J completed pivot stages and one unfinished stage.
It copies only its final n-bit answer and then admits its literal known
inverse. For every fixed read-only tournament, its answer is the Condorcet
winner except with probability less than 2^(-23). Each selected pivot is
exactly uniform in its current contender set. This is an unconditional
coupling statement; pivots are not declared uniform after conditioning
on a successful global cap.

If P(n) is the gate cost of the exact contender predicate with J pivot
slots, the selector and its actual inverse use

    O(sqrt(K)*(P(n)+n^3)) gates,
    S_Q=O(n^2), S_C=O(n).

All loops have their stated public bounds. These are worst-case circuit
and space bounds, including interrupted searches. Expected search costs
are used only to prove the probability of an interruption before the
winner is selected.

## 2. An exact unknown-size marked search

Fix one read-only history. Let S be its contender set, a=|S|/K, and

    v=K^(-1/2) sum_x |x>,
    P_S=sum_{x in S}|x><x|,
    R_f=I-2P_S,
    D=2|v><v|-I,
    G=D R_f.

These signs are literal. When 0<a<1, put sin(theta)=sqrt(a) and let g,b
be the normalized uniform marked and unmarked vectors. In that basis,

    G=[ cos(2theta),  sin(2theta)]
      [-sin(2theta),  cos(2theta)].

For a=0, Gv=v. For a=1, Gv=-v. A controlled implementation must preserve
these signs. Replacing G by -G would make the empty case incorrect.

Start the candidate at v. For j=0,1,..., set t=2^j and use one fresh probe:

1. Apply H to the probe, controlled G^t from the probe, then H.
2. If the probe is 0, continue to j+1.
3. On its first value 1, apply G^(-t) to the candidate and stop the search.

These outcomes are only conceptual measurements in the analysis. The
implementation retains every probe and uses coherent controls.

After all earlier probes are 0, the normalized candidate has angle t*theta:
its marked and unmarked amplitudes are sin(t*theta),cos(t*theta). The two
new branches are obtained by (I+G^t)/2 and (I-G^t)/2. The 0 branch has
norm factor cos(t*theta) and doubles that angle. The 1 branch is

    sin(t*theta)*[-cos(2t*theta)g+sin(2t*theta)b].

Applying G^(-t) makes this exactly -sin(t*theta)g. Thus every successful
branch ends in the exact uniform marked state, independent of its stopping
level. All other stage work can remain as a retained history. Fresh exact
verification of f(x) is 1 with certainty on such a branch.

The probability of reaching level j is

    s_j=product_{l<j}cos^2(2^l theta)
       =sin^2(2^j theta)/(4^j sin^2(theta))
       <=min(1,1/(4^j a)).

The formula follows by repeated use of sin(2z)=2sin(z)cos(z), with its
continuous endpoint values. For a>0, survival tends to zero. For a=0,
every completed probe is 0 and the search continues forever in the
uncapped mathematical process. The physical process is cut off at B.

## 3. A fixed clock schedule for one stage

Each stage has one candidate register, d probe bits, a fresh verification
bit, an allocation bit, a completion bit, and start/end timestamps. All
of these need O(n) qubits per stage. Timestamp width is d+2, so values
through B+1 do not wrap. No timestamp is stored per probe.

Let e be the public global tick minus this stage's retained start time.
For level j put t_j=2^j and F_j=t_j-1+2j. The schedule, when all earlier
probes are 0, is:

| Operation | Elapsed tick |
| --- | --- |
| Prepare candidate v, at the first level only | 0 |
| First H on probe j | F_j |
| Probe-controlled forward G ticks | F_j+1,...,F_j+t_j |
| Second H on probe j | F_j+t_j+1 |
| If this is the first probe 1: inverse G ticks | F_j+t_j+2,...,F_j+2t_j+1 |
| Fresh exact verification | V_j=3t_j+2j+1 |
| Archive the completed stage | C_j=3t_j+2j+2 |

After an archive, the next stage starts at the next public tick. A successful
stage at level j therefore uses D_j=3t_j+2j+3 ticks. If no probe has yet
reported 1, later levels are used. Since F_j>=2^j-1, the d stored probes
include every level that can begin before the global cap B: specifically,
F_d=B-1+2d>B-1. The mathematical
uncapped process may use more probes, but its first B ticks agree with this
finite circuit.

Charge at most 2t_j+4 ticks for every reached level, including all possible
inverse, verification and boundary work. This overcounts the displayed
D_j. For x=1/sqrt(a) and t_0 the first power of two at least x,

    sum_j 2^j s_j
      <=sum_{2^j<t_0}2^j + x^2 sum_{2^j>=t_0}2^(-j)
      <4x.

As 2t+4<=6t, the expected stage ticks for a nonempty set satisfy

    E D <24/sqrt(a)=24sqrt(K/|S|).                 (S1)

No measurement/reset or new trial register is hidden in this bound. A
failed probe is one retained bit; the same candidate continues evolving.

## 4. Uniform pivots and the one global cap

After a successful search, append its pivot p and set

    S'={x in S:x beats p}.

Invalid addresses are always false. Membership in S scans the completed
pivots, as in the original note. Each successful marked state is g, so the
selected pivot is exactly uniform in S. Probe histories can be measured
conceptually without changing the law of later read-only computation.

For every tournament, if m=|S|>0 and p is uniform,
E|S'|=(m-1)/2. A useful total-cost bound follows from

    V(m)=1/sqrt(m+1), V(0)=1.

Convexity and the preceding mean give

    E[V(|S'|)-V(m)]
      >=(sqrt(2)-1)/sqrt(m+1)
      >=(1-1/sqrt(2))/sqrt(m).

The size decreases strictly, so the process reaches zero in at most C
pivots. Telescoping conditional expectations proves

    E sum_{nonempty stages}1/sqrt(|S|) <=2+sqrt(2).

Combining this with (S1), the expected ticks to select the last pivot are
less than 96sqrt(K). Under the Condorcet promise this last pivot is exactly
the winner: it remains in every nonempty contender set until selected,
and no vertex beats it afterward.

There is no local empty-set detector. After choosing the winner, its next
search has a=0 and every completed probe is 0. The last completed pivot
therefore stays equal to the winner until the global cap. If T_win is the
completion time for selecting it in the uncapped process, Markov gives

    Pr[T_win>B] <96sqrt(K)/B <=2^(-24).           (S2)

The finite pivot cap J adds at most 2^(-24) failure. Indeed E|S_J|<=K/2^J,
and missing the winner after J successful pivots implies |S_J|>=1. A
winner selected in the last allowed stage is returned, not replaced by 0.

The finite circuit returns the last completed pivot, or 0 if there is none.
It agrees with the successful uncapped process whenever T_win<=B and the
winner has rank at most J in that process. A cap in the middle of a probe,
inverse correction, or verification returns only an earlier completed pivot.
All these interruptions are included in (S2). Union bounding (S2) and the
pivot cap gives selector error less than 2^(-23).

More explicitly, first define the unbounded conceptually measured process:
measure a probe only after its second H, and measure a selected pivot only
after its inverse correction and verification. Couple the bounded process
to that same sample path until the first cap. The coherent fixed-clock
circuit is its deferred-measurement implementation on this interval.
It retains every completed probe and pivot in computational registers.
Later gates only read these values, except for bank permutations that move
the full records without merging them. Start/end timestamps are retained
as well. Distinct histories therefore stay orthogonal. The cap can leave
the current probe in a superposition; that unfinished bank is ignored by
the answer function. No probability law for pivots is obtained by first
conditioning on survival of a cap.

This analysis works for every fixed read-only data block. It therefore also
holds for arbitrary coherent records by their orthogonal computational
decomposition. No conditioning on successful caps is used to change a
pivot distribution.

## 5. One active workspace and invariant instruction controls

Allocate J+1 stage banks of O(n) qubits each. Bank 0 is the one active
workspace. Completed banks occupy the end of the array. The intervening
banks are unused zero banks. A quantum counter i records the number of
completed stages. Initially i=0, bank 0 is allocated with start time 0,
and every other bank is zero.
The count width is r=ceil(log_2(J+1)); count increments are modulo 2^r.
Reachable increments have i<J and therefore do not wrap. Elapsed-time
subtraction uses d+2 bits and is enabled only when start<=tau.

Every ordinary Grover tick acts on the fixed candidate wires of bank 0.
Membership scans the J other banks by public addresses and includes a
pivot exactly when its retained completion and verification bits are 1.
There is no quantum-addressed choice of a candidate workspace and no outer
J loop of complete Grover operations per tick. The J membership comparisons
are the same comparisons already charged in P(n).

For public global tick tau=0,...,B-1, use this fixed order:

1. Candidate initialization and separate guarded H operations for each probe.
2. One guarded forward G.
3. One guarded inverse G.
4. Fresh guarded verification.
5. The boundary permutation of Section 6, last in the tick.

All instruction guards include i<J, allocation and tau>=start. A probe-H
guard for j uses only its scheduled time and the earlier probes, never its
target probe. Thus compute/act/uncompute of that guard is exact. Forward-G
guards use the scheduled forward interval, earlier zero probes, and the
current probe as the enable. G changes only the candidate and its clean
arithmetic helpers, so these guard inputs do not change. The inverse-G
guard identifies a first 1 and its scheduled correction interval; its read
controls also stay unchanged. A verification guard does not read its target
verification bit. The oracle helpers return zero on every Boolean input.

A probe is used as a completed decision only after its second H. Equivalently,
the correction and boundary guards include their explicit elapsed times,
which are later than that H. A probe still inside its test may be in a
superposition and is not treated as a stopping outcome.

The per-probe guards can be emitted in a public j loop. Their targets are
excluded from their own read predicates. For a reachable branch, the public
times select at most one probe H per tick. The forward/inverse OR guards
are computed once and cleared before the boundary. All of their controls
are unchanged by the corresponding operation. There is no attempt to clear
a pre-boundary selector from moved post-boundary registers.
All elapsed-time, prefix, comparison and OR helpers are also cleared before
the boundary, not only the final guard bits. The public tick copy may stay
live because the boundary does not change it; it is cleared at tick end.

The time comparisons, first-1 tests and public loops have O(n^2)-size
Boolean constructions, or O(n^3) with a conservative streaming bound.
They reuse O(n^2) clean helpers. Only the current global public tick has an
O(n)-bit classical counter. It may also be copied into O(n) known basis
qubits for Boolean controls and cleared after the tick.
Regenerate F_j,V_j,C_j one at a time from the public loop index. No table
of d separate n-bit timing constants is retained.

## 6. A total reversible boundary map

A sticky halt update or an overwritten start time would not be reversible.
Use the following explicit clock-dependent involution instead. All timestamp
arithmetic is on the stated fixed unsigned width, without wrap on reachable
values. Let X denote the complete stage-bank array and its count i.

Define A_tau by these Boolean conditions:

- i<J; the active bank is allocated, not completed, and has end stamp 0.
- Its start stamp is at most tau. Exactly probe j is 1, all other probes
  are 0, and the elapsed time is C_j. Its fresh verification bit is 1.
- Bank 1 is entirely zero.

The zero condition on higher probes holds on every reachable boundary.
These tests take O(n^2) Boolean work and space.
They do not inspect or change the source records. No check of an unknown
source state is used.

Let F_tau be this globally defined permutation of X:

1. XOR tau+1 into the active end stamp and flip its completion bit.
2. Cyclically rotate the J+1 entire stage banks left by one bank.
3. XOR tau+1 into the new active start stamp and flip its allocation bit.
4. Increment i on its fixed-width register.

Each step is a permutation on all words, including invalid words. Its inverse
decrements i, reverses step 3, rotates right, and reverses step 1. On A_tau,
the new front was the zero bank 1. It is therefore fresh with start tau+1.
The completed old front is now at the end with end stamp tau+1. All its
candidate/probe/work data are retained.

Put B_tau=F_tau(A_tau). Membership in B_tau is computed by applying the
known Boolean formula F_tau^(-1) to a temporary copy and testing A_tau.
A_tau and B_tau are disjoint: the former has active start<=tau, while the
latter has active start=tau+1. Define

    T_tau(X)=F_tau(X)       if X is in A_tau,
             F_tau^(-1)(X) if X is in B_tau,
             X            otherwise.

This is a total involution. It swaps the two matched sets and fixes their
complement. It is not an irreversible forward transition with a fixed
post-state. On a reachable forward run, only its A_tau direction occurs.
No claim is made that it fixes every globally unreachable archive word:
an unreachable word satisfying A_tau or B_tau is swapped as specified.
At a later public tick, the old end stamp does not equal that later tick
plus one, so the completed boundary is not undone. No stage gates are emitted
after this boundary in the same tick. The next fresh front starts at tau+1.

Here is an explicit streaming XOR evaluator, including its scratch bound.
Keep X unchanged. Compute a=A_tau(X). Copy X into one temporary array,
apply F_tau^(-1) there, compute b=A_tau(F_tau^(-1)(X)), reverse F_tau^(-1),
and clear the temporary copy. Each eligibility computation uses Boolean
DAG compute/copy/uncompute. Thus both flags are available with all their
temporary helpers zero.

For an arbitrary XOR output Y, first apply Y<-Y XOR X. Next form F_tau(X)
in the same temporary array and apply

    Y<-Y XOR a*(F_tau(X) XOR X)

bit by bit, using one reusable difference bit. Reverse F_tau and clear
the copy. Repeat with F_tau^(-1) and b. Finally uncompute a,b from X by
the same routines. Since A_tau and B_tau are disjoint, the result is
Y<-Y XOR T_tau(X). X is unchanged and every helper is zero, for every
initial X,Y. Only one O(n^2)-bit temporary array is needed at a time.

Use this evaluator to compute T_tau into a clean full-size output register,
swap input and output, then XOR-evaluate T_tau again into the old input.
Since T_tau is its own inverse, that old input returns exactly to zero.
The array size, temporary copy, eligibility tests and output buffers are
all O(n^2).
This is also an O(n^2) bound on the full Boolean-DAG history: prefix probe
tests and d=O(n) timestamp comparisons use O(n^2) nodes, a bank-zero
test uses O(n) nodes, and a fixed rotation/XOR of O(n^2) bits uses O(n^2)
nodes. Testing A_tau after the explicit inverse view uses a fixed number
of these same constructions. Output selection adds O(n^2) Boolean nodes.
The boundary costs O(n^3) conservatively and does not require one retained
bit per global tick. Its actual inverse is the reverse of its literal gate
word, as for every other step.

## 7. Literal gate phases

Controlled R_f changes sign exactly on [enable AND f(candidate)]. For the
literal controlled D, apply H^n unconditionally, change sign on
[enable AND candidate!=0], and apply H^n again. The middle phase is +1 on
zero and -1 on nonzero when enabled, so this is exactly D, including the
control-relative global sign. When disabled it is exactly I. Controlled
G^-1 reverses the two literal reflection gadgets.

Conditional H also has an exact Clifford+T circuit. With S=diag(1,i), let
V=S H T H S^dagger as a matrix product. Then V Z V^dagger=H, so controlled
H is (I tensor V) CZ (I tensor V^dagger). The actual gate word applies
V^dagger first and V last. Their scalar phases cancel. All Boolean gates
use the exact Toffoli compilation in proof.md Section 8.1.

No approximate selective pi/3 phase is used by this selector. In particular
there is no phase compiler in the exponentially repeated tick stream.
The existing one-pass record QPE and its literal undo keep their existing
paid compilation and error budgets.

## 8. Work, storage, reverse execution and coarse error

Each public tick emits a constant number of contender-predicate/Grover
macros on one candidate, plus the controller and boundary work. Thus the
main gate count, including actual undo, is

    O(B*(P(n)+n^3))=O(sqrt(K)*(P(n)+n^3)).

All stage banks, all timestamps/probes, the retained record bank and a
constant number of O(n^2) controller/Boolean buffers fit in O(n^2) qubits.
There are no trial/result registers per repeated Grover iteration. The
classical controller retains public N, the old private axes, one O(n)-bit
tick counter, local O(log n)-bit loop/address variables and the existing
phase-compiler scratch. This is O(n) classical bits. Stage data and pivots
are quantum registers, not a hidden classical table.

Public layout addresses have O(log(n+2)) bits. The actual online controller
is the complete bit-stream construction in the packaged generator proof,
Sections 1--6 and Appendix A. Ready operands, tape-head carry walks and
marked loop strips count full deterministic scans, including all address
setup, loop ends, rewinds, public constants and reverse words. Its complete
raw count is O(n^2 L) per tick, L=log2(n+2). Every raw action, gate dispatch
and fixed-arity ready-address use pays the full O(L) indexed debit.

For this cached implementation, use the ordinary literal controller count
in Appendix R and the cache-extended boundary in the phase proof. Expanded
stage banks have 2QR extra bits, still O(n). All copies/rotations and
eligibility histories retain their stated size. The full cache predicate
and boundary use a fixed number of whole-cache calls. Their complete scan
account in the generator proof gives

    O(n^2 L^2) charged work per tick,
    O(2^(n/2)n^2 L^2) total repeated work.

The additive one-pass QPE compiler and setup remain below this repeated-work
bound. The main proof gives all costs and peak allocations jointly.

At public tick B, compute a total answer function by a fixed scan of banks
1,...,J: return the rightmost bank's candidate among those with both completion
and verification bits 1, or 0 if none exists. On reachable histories this is
the latest completed pivot. An unfinished
front stage is ignored. Copy only that n-bit answer. Reverse the actual
answer computation and then all ticks tau=B-1,...,0, using the exact inverse
of every emitted gate. Regenerate the same public constants. In particular
reverse the actual boundary permutation circuit, not an informal classical
forward rule. Then undo record preparation as in proof.md Section 7. This is
an actual known inverse and never an inverse of source preparation.

The score event in proof.md Section 3 fails with probability at most 2^(-19).
On that event's complement the class tournament has its Condorcet winner.
The selector adds at most two terms 2^(-24), for time and stage caps. Even
retaining the old extra 2^(-30) norm-error allowance gives

    coarse error <=2^(-19)+2*2^(-24)+2^(-30)<2^(-18).

All source/record conclusions are unconditional by the same orthogonal
read-only-block analysis. The final-answer-copy/known-undo argument in proof.md Section 7
therefore keeps its stated bank disturbance and endpoint bounds. No claim
that the bank is exactly restored on an erroneous answer is needed.


## Appendix R. Complete quadratic ordinary-controller count

### R.1. Result and scope

Put L=log2(n+2). The exact selector controller has the following worst-case
bounds, on every input word and every coherent branch:

    literal controller gates per tick = O(n^2),
    fully charged controller work per tick = O(n^2 L^3),
    clean controller scratch = O(n^2) qubits,
    classical generator storage = O(n) bits.

The controller includes every time test, instruction guard, boundary
permutation, public clock operation, bank address and inverse instruction.
It excludes the contender predicate itself. There are a constant number of
predicate or Grover macros per tick. If one such macro has fully charged
work W_pred(n), the full selector and its literal inverse therefore cost

    O(2^(n/2) [W_pred(n)+n^2 L^3]).                 (R1)

If a predicate has P(n) literal gates and the cited O(L^3) generator bound
per local action, (R1) is O(2^(n/2) [P(n)+n^2] L^3). Neither statement assumes
that an arbitrary oracle's gate count also bounds its generator work.

The final answer evaluator costs O(n^2 L^3) once in each direction and fits
in (R1). No expected-time or amortized estimate is used here. The original
success proof, caps, source count and source model are unchanged.

### R.2. Explicit sizes

Use the exact source parameters

    J=n+24, d=ceil(n/2)+32, q=d+2,
    r=ceil(log2(J+1)), B=2^d.

A stage bank has n candidate bits, d probe bits, three flags (allocation,
completion and verification), and two q-bit timestamps. Thus its length is

    b=n+d+3+2q=O(n).

The stage array and count have

    M=(J+1)b+r=O(n^2)

bits. All scratch arrays, record banks and addresses in the full circuit
have polynomial length in n. A public wire address therefore has O(L)
bits. The absolute tick tau has q=O(n) bits, but it is DATA for a time
comparison, not a wire address or an index into a B-entry table.

### R.3. Ordinary instructions on the active front

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

    sum_(j<d) O(q+j+r)=O(dq+d^2+dr)=O(n^2).       (R2)

Equation (R2) holds even if malformed words enable several such instructions.
The emitted word still has the same size, and each guard's cleanup is valid
on all words because its operation leaves its read wires unchanged.

Forward-G, inverse-G and verification each use one OR of per-j guards.
Compute all of that macro's per-j flags, compute their OR, apply the macro
once under that OR, and reverse the flags. Each per-j flag has the size in
(R2); the OR adds O(d) nodes. There are only three such macros. A macro
changes candidate/helper wires or the verification target, not its own
time/probe/metadata read controls. Thus its cleanup does not require a
second search through archive histories or a retained history per tick.

Candidate initialization adds O(n) constant-size controlled H words and
O(q+r) guard work. A controlled diffusion on the active candidate uses
O(n) gates for its zero/nonzero test and constant-size gates per qubit;
these are also within (R2). The contender predicate in a Grover reflection
is counted in W_pred. All front-only control work is O(n^2) gates.

Full Boolean histories for a macro's guards have O(n^2) nodes. They can be
retained for that macro and reversed afterward. The H guards may instead
reuse one O(n)-size history at a time. Both schedules use at most O(n^2)
clean scratch and leave it zero before the boundary.

### R.4. Boundary eligibility and fixed permutations

The pre-domain A_tau tests the count, front metadata, bank 1 being zero,
and the single-1 probe condition with elapsed time C_j. The metadata and
bank-zero tests have O(q+r+b) nodes. For each j, one can check probe j=1,
all other probes zero, and elapsed time C_j with O(d+q) nodes. Their OR
has O(d) nodes. Even this simple repeated implementation gives

    size(A_tau)=O(q+r+b+d(d+q))=O(n^2).            (R3)

An optimized shared prefix/suffix test is unnecessary. The argument does
not assume that valid history words are the only inputs to A_tau.

F_tau is the exact source permutation: XOR tau+1 into front end, flip
completion, rotate the whole bank array left, XOR tau+1 into the new front
start, flip allocation, and increment the r-bit count modulo 2^r.
The rotation uses J adjacent whole-bank swaps, each with b bit swaps.
Each bit swap has three CNOTs. Consequently F_tau and its inverse cost

    O(Jb+q+r)=O(M)=O(n^2) gates.                  (R4)

Ripple increment/decrement costs O(r) gates with O(r) reusable scratch.
It is a permutation on every r-bit word. There is no counter-sized loop.
All swaps and timestamp bit operations have public fixed wire operands.

To test B_tau=F_tau(A_tau), copy X to an M-bit temporary Z, apply F_tau^-1
to Z, evaluate A_tau(Z), undo that permutation, and clear Z against X.
Equations (R3)-(R4) give O(n^2) gates and O(n^2) scratch. X is unchanged.
The predicate result is computed once, not once for each output bit.

### R.5. Total XOR evaluator and clean in-place boundary

Use the exact evaluator in the source. Compute a=A_tau(X) and
b=A_tau(F_tau^-1(X)) with clean helpers. XOR X into the arbitrary output Y.
Form F_tau(X) in the reusable temporary array and, bit by bit, XOR

    a AND (F_tau(X)_k XOR X_k)

into Y_k. One reusable difference bit needs a constant number of exact
gates per k. Reverse F_tau and clear the temporary. Do the same with
F_tau^-1 and b. Finally clear a and b by their original evaluators.

There are a fixed number of calls to (R3), (R4), and M-bit copy/correction
loops. Thus the complete XOR evaluator has O(n^2) literal gates. Its
scratch consists of one M-bit temporary array, O(n^2) eligibility history,
two retained flags, and O(n) arithmetic helpers. These can coexist within
O(n^2). No separate M-bit copy is allocated for each output bit.

Compute T_tau into one clean M-bit output, swap the input and output, then
XOR-evaluate T_tau once more. Since T_tau is a total involution, the old
input clears on every word. Two evaluations and one M-bit swap retain the
O(n^2) gate and scratch bounds. This is also the exact linear extension
on superpositions. It needs no measurement, reset or source inverse.

### R.6. Archive access and final answer

Only the contender predicate scans the J archived pivots for tournament
edges. Its cost is already in W_pred. It reads each pivot from a fixed
public bank address. The controller does not wrap this predicate in another
J-fold loop of complete Grover calls.

The final answer is the candidate in the rightmost archived bank with both
completion and verification flags 1, or zero. Compute the J joint flags
and their suffix ORs with O(J) nodes. For each bank, one selection flag
controls n CNOT/Toffoli output operations. Clear all flags afterward.
This gives O(Jn+J)=O(n^2) gates and at most O(n^2) clean scratch on every
word, including words with several marked banks. The suffix test makes
the output rule total and unique.

### R.7. Baseline public generation and actual aligned layout

The following source count gives a conservative O(L^3) charge per local
action. The actual package uses the full bit-stream controller and aligned
layout in critical_third_adaptive_cache_l2_generator.md. It proves O(n^2 L)
raw actions and O(n^2 L^2) charged work for a complete tick by deterministic
scan counts. The literal local-action counts and all cleanup below are
unchanged. The cache-extended boundary is counted in the phase proof and
the complete generator account.


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

Each local action in (R2)-(R4), each copy/swap/correction bit, each Boolean
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

### R.8. Caps and reverse execution

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

The factor B=2^(ceil(n/2)+32)=O(2^(n/2)) now yields (R1). The sharper result
removes an unnecessary factor n from the controller allowance. It makes
no claim that the contender predicate itself has quadratic work.
