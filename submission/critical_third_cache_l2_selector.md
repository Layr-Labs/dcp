# Exact global-clock selector appendix

This is the complete selector construction used by the accompanying main
proof `critical_third_cache_l2.md`. All five claims cite that proof and all three packaged appendices,
whose packaged name is `critical_third_cache_l2_selector.md`. The main proof
supplies the source model, QND records, exact scores, the cached contender
predicate, the one-pass phase compiler and the final endpoint decision.
The selector below uses only that counted predicate interface.

The source text is `critical_third_selector_cost.md`, actual SHA-256
`1cfcac197add3d36a9e74fb59e6956d826af6227e52469db202f82ea0c1d0c37`.
The construction was audited at its earlier source hash
`f732cc76fd5b04e07df1fc44e1ec4063b20d03a65d4167b552019c9ec8570818`.
This packaged text retains all mathematical and controller details, with
package references substituted for working-note links. Review history is
context, not a premise of any proof below.

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
contender predicate with J pivot slots. The concrete cached predicate in the accompanying main proof has these
properties.
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

    O(sqrt(K)*(P(n)+n^2 L)) gates, L=log2(n+2),
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
bit, an allocation bit, a completion bit, start/end timestamps and two
QR-bit member caches, R=32. The second cache is zero at odd N. The cache
appendix proves the total identical fresh/saved map and its circuit. All
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
pivots, as in the accompanying main proof. Each successful marked state is g, so the
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
and every other bank is zero. The active cache stays zero during search.
Fresh predicate caches use separate scratch and clear after each call; only
the verified boundary fills a saved cache.
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
Boolean constructions, as the complete controller appendix proves.
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
- The active member-cache field is zero. Bank 1, including its cache, is entirely zero.

The zero condition on higher probes holds on every reachable boundary.
These tests take O(n^2) Boolean work and space.
They do not inspect or change the source records. No check of an unknown
source state is used.

For every fixed prefix-record word E, let F_(tau,E) be this globally defined
permutation of X. The full prefix bank E is unchanged:

0. XOR the exact class-cache function C_E of the active candidate into its
   active cache. At even N compute both members directly; at odd N the
   second cache stays zero. The phase appendix gives the literal circuit.
1. XOR tau+1 into the active end stamp and flip its completion bit.
2. Cyclically rotate the J+1 entire stage banks left by one bank.
3. XOR tau+1 into the new active start stamp and flip its allocation bit.
4. Increment i on its fixed-width register.

Each step is a permutation on all words, including invalid words. Step 0
is an XOR function of E and the unchanged candidate, so its inverse is
itself. The inverse first decrements i, reverses step 3, rotates right,
reverses step 1, then reverses step 0 on the restored front candidate. On A_tau,
the new front was the zero bank 1. It is therefore fresh with start tau+1.
The completed old front is now at the end with end stamp tau+1. All its
candidate/probe/work data are retained. Its stored cache is now exactly
the same C_E vectors that a fresh candidate with that value would use.

Write F=F_(tau,E) in the rest of this section, and put B_tau=F(A_tau). Membership in B_tau is computed by applying the
known Boolean formula F^(-1) to a temporary copy and testing A_tau.
A_tau and B_tau are disjoint: the former has active start<=tau, while the
latter has active start=tau+1. Define

    T_(tau,E)(X)=F(X)       if X is in A_tau,
             F^(-1)(X) if X is in B_tau,
             X            otherwise.

For every fixed E this is a total involution; with coherent E it is the
corresponding controlled permutation, preserving E exactly. All tests use
known Boolean functions of computational words. This is a total involution. It swaps the two matched sets and fixes their
complement. It is not an irreversible forward transition with a fixed
post-state. On a reachable forward run, only its A_tau direction occurs.
No claim is made that it fixes every globally unreachable archive word:
an unreachable word satisfying A_tau or B_tau is swapped as specified.
At a later public tick, the old end stamp does not equal that later tick
plus one, so the completed boundary is not undone. No stage gates are emitted
after this boundary in the same tick. The next fresh front starts at tau+1.

Here is an explicit streaming XOR evaluator, including its scratch bound.
Keep X unchanged. Compute a=A_tau(X). Copy X into one temporary array,
apply F^(-1) there, compute b=A_tau(F^(-1)(X)), reverse F^(-1),
and clear the temporary copy. Each eligibility computation uses Boolean
DAG compute/copy/uncompute. Thus both flags are available with all their
temporary helpers zero.

For an arbitrary XOR output Y, first apply Y<-Y XOR X. Next form F(X)
in the same temporary array and apply

    Y<-Y XOR a*(F(X) XOR X)

bit by bit, using one reusable difference bit. Reverse F and clear
the copy. Repeat with F^(-1) and b. Finally uncompute a,b from X by
the same routines. Since A_tau and B_tau are disjoint, the result is
Y<-Y XOR T_(tau,E)(X). X is unchanged and every helper is zero, for every
initial X,Y. Only one O(n^2)-bit temporary array is needed at a time.

Use this evaluator to compute T_(tau,E) into a clean full-size output register,
swap input and output, then XOR-evaluate T_(tau,E) again into the old input.
Since T_(tau,E) is its own inverse, that old input returns exactly to zero.
The array size, temporary copy, eligibility tests and output buffers are
all O(n^2).
This is also an O(n^2) bound on the ordinary Boolean-DAG history: prefix probe
tests and d=O(n) timestamp comparisons use O(n^2) nodes, a bank-zero
test uses O(n) nodes, and a fixed rotation/XOR of O(n^2) bits uses O(n^2)
nodes. Testing A_tau after the explicit inverse view uses a fixed number
of these same constructions. Output selection adds O(n^2) Boolean nodes.
The cache calls use the clean ripple adders of main Section 8.1 and clear
each carry block before the next addition. Their gate streams do not retain
one Boolean history bit for every gate. A fixed number of O(n^2) arrays
and the reusable O(b) cache-adder block therefore suffice simultaneously.
Its fixed bank operations and tests cost O(n^2). Each F or inverse call
adds one full class-cache XOR at O(Qnb)=O(n^2 L) gates and O(n^2) scratch.
Only a fixed number of calls is made; none repeats for every output bit.
Thus the complete boundary costs O(n^2 L) gates and needs no retained
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
use the exact Toffoli compilation in main Section 8.1.

No approximate selective pi/3 phase is used by this selector. In particular
there is no phase compiler in the exponentially repeated tick stream.
The existing one-pass record QPE and its literal undo keep their existing
paid compilation and error budgets.

## 8. Work, storage, reverse execution and coarse error

Each public tick emits a constant number of contender-predicate/Grover
macros on one fixed candidate. Main Section 8 and phase Section 6 prove
P(n)=O(n^2 L) literal gates for the complete fresh-cache predicate, with
L=log2(n+2). The ordinary controller has O(n^2) local actions by the complete
controller appendix. The actual total cache boundary above has O(n^2 L)
actions. Thus forward execution and actual known undo have

    O(B*(P(n)+n^2 L))=O(2^(n/2)n^2 L) literal gates.

Each local action has O(L^3) fully charged generation and indexed-access
work by main Section 8.3 and controller Section 7, including loop steps,
public timing constants, all address arithmetic and skipped templates.
This conservative charge gives O(2^(n/2)n^2 L^4). The complete aligned
generator in main Section 8.7 replaces it by O(L^2) per local action,
including all padding, address construction, loops and indexed uses. Thus
the L3 fallback is O(2^(n/2)n^2 L^3). The selected actual online
controller is proved in full in controller Section 10 and selected by main
Section 8.8. It counts O(n^2 L) raw bit/head actions over every complete
tick, including ready-address setup, all carry walks, endpoints, loops,
full cache/boundary calls and reverse generation. Each action and fixed
number of address operands receives the full O(L) debit. The supported
repeated work is O(2^(n/2)n^2 L^2). This is a whole-tick count, not an
O(L) worst-case claim for each isolated gate. No gate stream is stored.
The one-pass QND/prefix setup and endpoint add polynomial work. The full
one-pass QPE compiler of main Section 6 adds 2^O(L^4) work; it is additive
and o(2^(n/2)). No approximate phase occurs in a selector tick.

All expanded stage banks, timestamps/probes/caches, retained QND/prefix
records, one fresh cache and a fixed number of full O(n^2) boundary/helper
buffers fit O(n^2) qubits. No repeated Grover step retains its arithmetic
history. The classical controller keeps public N, independent private axes,
one O(n)-bit tick counter, fixed timing buffers, public loop/address words
a fixed number of O(n)-cell loop strips, ready operand words and head
locations, and one current QPE word/compiler scratch, all within O(n) bits. Pivots and
caches stay quantum. Every wire address is public; no QRAM is required.

At public tick B, compute a total answer function by a fixed scan of banks
1,...,J: return the rightmost bank's candidate among those with both completion
and verification bits 1, or 0 if none exists. On reachable histories this is
the latest completed pivot. An unfinished
front stage is ignored. Copy only that n-bit answer. Reverse the actual
answer computation and then all ticks tau=B-1,...,0, using the exact inverse
of every emitted gate. Regenerate the same public constants. In particular
reverse the actual boundary permutation circuit, not an informal classical
forward rule. Then undo quantum prefix setup and record preparation as in the main proof. This is
an actual known inverse and never an inverse of source preparation.

The score event in the main proof fails with probability at most 2^(-19).
On that event's complement the class tournament has its Condorcet winner.
The selector adds at most two terms 2^(-24), for time and stage caps. Even
retaining the old extra 2^(-30) norm-error allowance gives

    coarse error <=2^(-19)+2*2^(-24)+2^(-30)<2^(-18).

All source/record conclusions are unconditional by the same orthogonal
read-only-block analysis. The original final-answer-copy/known-undo argument
therefore keeps its stated bank disturbance and endpoint bounds. No claim
that the bank is exactly restored on an erroneous answer is needed.

## 9. Verification status

Independent reviews passed the search identities, literal gate signs,
uniform-pivot law, clock schedule, cap coupling, boundary involution,
instruction cleanup, known undo and resource accounting. The strategy and controller audit texts have SHA-256 hashes
`a8c6a2e9c1031166e2a42b2cf8c74d0d6b1e6e01cee608fb8b04bc2221eed7e0` and
`4efa8ea1ddd44a81b6accaa83552acf8cbe5797dc4524bd5d34dcc017fad552e`.
These audit records are context; Sections 1-8 contain the construction and
proof in full.

The finite controller audit passed 544,522 boundary-word tests, 1,089,044
forward/inverse checks, 5,582 fresh/archive transitions, 544,522 copy/swap
cleanup checks, 36,350 schedule-guard cases and 69 cutoff states. These
checks supplement the proofs above. This appendix is part of the new package. It changes no earlier file or
submission stage, and it makes no upload.
