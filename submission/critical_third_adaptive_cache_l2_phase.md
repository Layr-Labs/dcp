# Coherent phase cache, error bound and reversible boundary

This is a proof file of the adaptive cache package. Use N,n,Q,r and the exact
adaptive source promise in [proof.md](proof.md). Its Lemma 0 reduces every
allowed adversary to fixed product-bank mixtures. Each component has the
clean product marginal used below. The one-pass QND record construction and
its complete error budget are in proof.md Sections 1--3. The actual aligned
layout and online bit-stream controller are fully proved in
[critical_third_adaptive_cache_l2_generator.md](critical_third_adaptive_cache_l2_generator.md). No label, prefix,
row sign, pivot or cache is measured during the coarse computation.

This file directly adapts critical_third_phase_cache.md, SHA-256
`7e3811e6b06023d3a7094fd476503f69c4ce9a1ed9dab4f8efd5c476e8e989ad`.
Its prefix/cache idea uses the public note for submission
`493303b5-06f6-4ee0-9596-d8cae89c8bb4`,
[Exact one-third tolerance with cached phase comparisons](https://api.yukon.org/api/submissions/493303b5-06f6-4ee0-9596-d8cae89c8bb4).
The actual note read has SHA-256
`5aeeec4b4dcd3c563a6abfc7688b2a3bdbfa3e25c8fee221983b4c3f63c82d41`.
Its full proof was unavailable when the note was read. The later published
source audit is recorded in proof.md Section 9. No peer proof is a premise.
The phase, statistics and controller arguments needed here are reproduced below. The model and
main source credits remain in proof.md Section 9.

## 3. The exact prefix and phase map

Put

    R=32,
    b=ceil(log2 n)+48,
    P=n+b,
    H=2^b, D=2^R.

For any n-bit label word k define k0=k mod N and the P-bit prefix

    E_N(k)=floor(2^P k0/N),         0<=E_N(k)<2^P.

This is a total function on all n-bit words. Since N>2^(n-1), reduction of
such a word needs at most one subtraction. For j=0,...,n-1 define the b-bit
window

    W_j(E)=floor(E/2^(n-j)) mod H.

For any n-bit candidate word t=sum_j t_j 2^j, define

    A_E(t)=(sum_j t_j W_j(E)) mod H,
    C_E(t)=floor(A_E(t)/2^(b-R)),       0<=C_E(t)<D.       (C1)

Every use of a candidate phase uses exactly C1. A saved pivot has no separate
high-precision map. Ties in C1 are resolved by the displayed floor. The whole
map is a fixed Boolean function of N,k,t with no random or measurement input.

### Circular error for every label and candidate word

For alpha=k0/N, nested integer division gives exactly

    floor(E_N(k)/2^(n-j))=floor(2^(b+j)alpha).

Therefore W_j/H is the downward b-bit approximation to frac(2^j alpha),
with error delta_j in [0,2^-b). Before reducing the sum modulo one,

    sum_j t_j W_j/H = t alpha - integer - sum_j t_j delta_j.

The total downward error is less than n2^-b<=2^-48. Removing the low b-R
bits of A adds a further downward error less than 2^-R. Consequently there
is a real e_t with

    0<=e_t<eta=2^-48+2^-32,
    C_E(t)/D = t alpha - integer - e_t.                   (C2)

This is a lift identity; it holds through wraparound, not only away from
zero. It proves the circular-distance bound eta for all k,t, including
k>=N, t>=N and t=0. The zero word has zero error. It is not a probability
bound and does not require uniform labels.

For two candidate caches a=C_E(t), c=C_E(u), use the four R-bit words

    a, c, (2a-c) mod D, (2c-a) mod D.                     (C3)

Their circular distances from the exact phases at t,u,2t-u,2u-t are at
most eta, eta, 3eta, 3eta. Negative values and integer overflow are reduced
modulo D. No approximate multiplication or phase-dependent branch occurs.
For the last two words this follows from the lift errors 2e_t-e_u and
2e_u-e_t. The conservative 3eta bound is sufficient.

For an arbitrary P-bit E not equal to E_N(k), C1 is still a total Boolean
map. The circuit and its inverse remain exact on that word. The accuracy
claim C2 uses the stated consistent prefix, which the initialization circuit
always computes, including on every superposed or malformed input label.

## 4. A fixed bounded score with the old error allowance

Use the original constant-size trigonometric recipe, now evaluated at each
word z/D from C3. Its cosine/sine outputs have denominator D0=2^20.
Generate pi64 by the Machin expression 16 atan(1/5)-4 atan(1/239), with
40 alternating terms each, and round to 64 fractional bits. Its error is
less than 2^-64. For x=2pi64*z/D, x<7, use cosine through degree 64 and
sine through degree 63. Their remainders are below 7^65/65! and 7^64/64!,
each below 2^-100. Generate coefficients and perform Horner operations at
1024 fractional bits. A fixed 256-bit integer part suffices. A bound of
64*8^64 on amplification leaves arithmetic error below 2^-800. Rounding
the final answer to denominator D0 adds at most 2^-21. Thus the recipe's
error relative to sin(2pi z/D) or cos(2pi z/D) is below 2^-20.
All these lengths and degrees are absolute constants; the tables/coefficients
have a finite charged construction. Their large fixed constants do not hide
an n-dependent operation or precision oracle.

Both sine and cosine are 2pi-Lipschitz in the circular phase coordinate.
By C2--C3, the error relative to each desired exact trigonometric component
is at most

    2^-20 + 6pi eta < 2^-19 < 1/2048.                     (C4)

The loose 3eta bound is used for all four components. C4 holds uniformly
on every input word, including all phase discontinuities of C1.

For valid position eigenlabel k, the row reflection is

    R_v(k)=cos(2pi kv/N)X+sin(2pi kv/N)Y.

Use the cubic witness

    M_tu=[11(R_t-R_u)+R_(2t-u)-R_(2u-t)]/20.

For A=(R_t-R_u)/2 this equals (7A-2A^3)/5. Since A has spectrum in [-1,1]
and this odd scalar polynomial increases from -1 to 1, ||M_tu||<=1.
At distinct nonantipodal honest labels t and u its oriented honest means
are 11/20 and -11/20. The scalar complex coefficient h of M has |h|<=1.

Compute its real/imaginary components from the four fixed dyadic values in
C3 with weights 11,-11,1,-1 and denominator 20D0. Clamp each component to
[-1,1]. On private axis X or Y, multiply the corresponding component by
2y, where y is the retained row sign. The implemented score lies in [-2,2]
and has one fixed rational denominator. On padding it is exactly zero.
The score sum and its sign are computed as exact bounded integers.

The absolute coefficient sum is 24/20=6/5. Since the true components lie
in [-1,1], clamping cannot increase their error. C4 implies correct-label
score error at most (12/5)/2048 for each fixed axis and sign. On a wrong
label the score difference is at most four. Thus the mean score observable
for each oriented pair differs from M_tu in operator norm by at most

    beta=((12/5)+4)/2048=1/320.                           (C5)

This is the old allowance, with substantial slack. To see why C5 applies
to arbitrary malformed states, condition on the true position eigenlabel.
The QND effects and all later exact functions are diagonal in that label;
the conditional row state can be arbitrary. Average the independent axis.
The correct-label component errors bound the row observable, and the
wrong-label probability is uniformly below 1/2048. Off-diagonal position
coherences do not contribute. Padding contributes zero. The resulting
blockwise operator bound holds on the full input space and after any
conditioning on other slots. No distributional claim for bad k' is needed.

## 5. Fixed classes, concentration and the endpoint

At odd N a class is one p in [0,N). At even N it is {p,p+N/2} for
p in [0,N/2). Keep two cache vectors per class; at odd N the second is zero.
For each valid member, compute its word using C1 directly. In particular,
do not derive C_E(p+N/2) by shifting C_E(p); direct use of C1 is the rule for
both new and saved classes. For invalid class addresses define member
addition modulo 2^n and reject that class with the exact validity predicate.
This extends all circuits to every word without adding invalid vertices.

For two different valid classes, canonicalize their IDs. The first class
wins if some member has nonnegative empirical score against every member
of the second class; otherwise the second wins. Use at most four exact
score-sum sign tests. The score for every ordered member pair is always
computed from the same two C1 vectors, whatever their storage locations.
Thus each unordered class pair has one fixed orientation on every record
string. Role exchange, search stage, previous pivots and cache creation time
do not change that orientation. Scores need not be transitive. Canonical
orientation makes ties harmless. No random thresholds are used.

Fix the hidden bad set for the proof. The local record instruments commute,
so reveal all good records first and then bad records. Good records have
the independent clean law from the exact product marginal. After their
reveal, each next bad record can have any conditional state; its private
axis is fresh and C5 applies. For t=s and u outside its class, conditional
means over all slots therefore sum to at least

    (Q-|B|)(11/20-beta)-|B|(1+beta)
      >=Q(1/30-beta)=29Q/960.

Centered scores have interval width four. The conditional Hoeffding bound
is E exp(lambda D_i)<=exp(2lambda^2). Iteration and optimization give

    Pr[sum_i D_i<=-delta Q]<=exp(-delta^2 Q/8).

With delta=1/48 this is exp(-Q/18432). Outside it the score is at least
3Q/320. The reverse orientation is at most -3Q/320 by the same upper-tail
bound. A union bound over the needed oriented comparisons is bounded by

    2(2^n)^2 exp(-Q/18432)<2^-19,

using Q=27648(2n+20). On this event's complement the true class beats every
other class under the fixed canonical rule. No independence between good
and bad subsystems, or between empirical comparisons, is used.

Apply the exact global-clock selector with J=n+24,
d=ceil(n/2)+32 and Bclk=2^d. Its exact probe with literal G=D R_f has
uniform marked output after a first-1 probe and inverse correction. The
fixed-tournament relation E|S'|=(|S|-1)/2 and its potential bound give
expected uncapped ticks below 96 sqrt(2^n). The global clock and stage caps
therefore each add less than 2^-24 failure. Cache computation only replaces
the cost of a tick; it inserts no extra logical search step or cap. It is
an exact computation from retained records and pivots. The semantic clock
schedule and selected-pivot distribution remain those of that selector.

Combining the score event and both caps gives coarse failure below 2^-18.
The coarse unitary includes record setup, prefix setup, every cache operation
and the selector. Copy only its final class, then reverse this actual known
unitary. On any purified input, squared distance from the correct class
tensor the original bank/work is twice the coarse error. Average over the
private axes. The trace-distance change is less than 1/256. This is an
unconditional statement; the old work is retained and counted on failure.

At odd N the class gives the secret. At even N apply the original trit test
on the returned class and the same bank, with fresh helpers. On the original
bank and correct class, every good slot gives common/correct trit with equal
probability, and no false trit. At most r bad slots can give false trits.
The correct count dominates Bin(2r,1/2) from the product good marginal.
Return the direction when its count exceeds r, and a fresh fair coin otherwise.
The reference success is

    3/4-binom(2r,r)/(4*4^r)>=23/32,

since r>=64 and binom(2r,r)/4^r<=1/sqrt(r+1)<1/8. Subtract the unconditional
1/256 disturbance. Success is at least 183/256>11/16. At N=2 no coarse
unitary or cache is needed, and the Q=192 exact trit circuit suffices.

## 6. Coherent initialization and cache evaluation

Compute each E_N(k') into its own zero P-bit quantum register after QND
record creation. Use exact restoring binary long division of k0*2^P by N,
copy the low P quotient bits, and reverse the divider. The numerator has
O(n) bits because P=n+O(log(n+2)); the quotient also has O(n) bits.
The total Boolean divider has O(n^2) nodes and admits compute/copy/uncompute
with O(n^2) clean scratch. Reuse this scratch for all Q slots. Reduction
k0=k' mod N is total on the n-bit input as specified above. This initialization
uses O(Qn^2)=O(n^3) literal gates and retains QP=O(n^2) quantum prefix bits.
Its literal inverse clears all prefixes at the end of coarse undo.

To XOR C_E(t) into any R-bit target, start one b-bit accumulator at zero.
For each public j, add W_j(E) modulo 2^b controlled by t_j. Window bits are
fixed wires of E; no lookup is performed. A ripple adder controlled by t_j
has O(b) gates and O(b) reusable carry scratch, and clears that carry scratch
on every word. Copy the high R accumulator bits into the target and reverse
all n additions. The result is the exact total XOR map

    (E,t,z,0)->(E,t,z XOR C_E(t),0)

with O(nb) gates and O(b) reusable scratch. No n-level Boolean history is
retained. The same forward and reverse public j loops generate its word.
This remains valid on superpositions of E,t and on arbitrary target z.

For one class, evaluate both member words by public slot scans. The full
class cache uses at most 2QR=O(n) bits. Its generation needs O(Qnb)=O(n^2 L)
gates. The member addition is computed in a reusable n-bit helper and undone;
it adds at most O(Qn), within that bound. The second member cache is zero for
odd N. Only fixed slot addresses are used. No quantum random-access memory,
source control or measured label is supplied.

At the start of a contender predicate, generate the fresh candidate's class
cache once in clean scratch. For each of J saved banks, scan the Q records
and compare against that bank's two retained member caches. The four R-bit
linear combinations and the trigonometric recipe cost a constant per record.
Adding/subtracting the fixed-width score to a complete Q-record sum uses
O(log Q)=O(L) gates. Clear each record's temporary values after addition;
copy only each score sign and reverse its scan to clear the sum. Combine at
most four signs into the class edge and clear those signs in reverse order.
For each saved bank, use the predicate

    NOT(completion AND verification)
      OR (valid(pivot) AND valid(candidate) AND candidate!=pivot
          AND candidate beats pivot).

The edge uses the canonical class orientation in Section 5. Thus unused
zero banks impose no constraint. Keep one such flag per bank and AND them
with the fresh class validity. Completed-bank candidate and cache fields
are read-only throughout the predicate. Copy the contender bit, then reverse
all edge computations and the fresh class cache. All active fresh-cache
helpers are zero again before the boundary. The total is

    O(Qnb+JQ log Q+Jn)=O(n^2 L) literal gates.             (C6)

The complete XOR-output predicate is exact on every register word and leaves
all reusable work zero. To make it a controlled reflection, compute its
bit, apply the required exact phase controlled on the outer enable, and
uncompute. Controls are never added to a gate certified only up to phase.
The selector's controlled-H and diffusion signs are unchanged.

## 7. Saving the same cache at the reversible stage boundary

Add a 2QR-bit cache field to every stage bank. A bank still has O(n) bits,
since Q=O(n) and R is fixed. The active front cache is zero throughout a
search. Fresh contender caches in Section 6 use separate clean scratch and
are cleared after each call. They are never retained while Grover changes
the candidate. Each archived class cache is immutable after creation.

For completeness the cache update fits the total boundary, rather
than an irreversible write. Treat all record prefixes E as read-only controls.
Add active-cache=0 to the pre-domain A_tau. Keep its original conditions:
i<J; active bank allocated and not complete; end stamp zero; start<=tau;
exactly the first-1 probe at its completion time C_j; verification=1; and bank
1 wholly zero, now including its cache. These extra zero tests cost O(Q).

Define F_(tau,E) on ALL stage-array words as follows:

1. XOR the Section 6 class-cache function of the active candidate into its
   active cache field, for all Q prefix records.
2. Perform the original F_tau: XOR tau+1 into the active end stamp, flip
   completion, rotate all J+1 whole banks left, XOR tau+1 into the new front
   start stamp, flip its allocation, and increment the count modulo its width.

The XOR cache function reads only the active candidate and E, not its target.
It is its own inverse for fixed candidate and E. Step 2 is a total permutation.
Therefore F_(tau,E) is a total permutation on every word. Its inverse first
reverses Step 2, restoring the same candidate to the front, and then performs
Step 1 again. On A_tau, the old zero cache becomes exactly C1, and the fresh
front has zero cache because it was bank 1.

Put B_(tau,E)=F_(tau,E)(A_tau). The two domains are disjoint for every E:
A_tau has front start<=tau, whereas B_(tau,E) has front start=tau+1.
Define T to apply F on A, F^-1 on B and identity elsewhere. For every fixed
E this is a total involution. With E in quantum superposition it is the
corresponding controlled permutation, hence a known unitary preserving E.
No promise about malformed archive words is needed for reversibility.

Use the explicit XOR evaluator: compute A(X) and A(F^-1(X)) on temporary
copies, start output Y with Y XOR X, and XOR the controlled corrections
F(X) XOR X and F^-1(X) XOR X. Clear the flags from unchanged X and E.
Then compute T into clean output, swap, and evaluate T again to clear the
old input. All calls to F or F^-1 use one class-cache computation plus an
O(n^2)-bit fixed bank rotation. There is a fixed number of calls. Thus the
complete physical boundary has O(n^2 L) gates and O(n^2) reusable scratch.
It does not run a full Q-record cache operation separately for each output
bit. One complete temporary cache is generated, used and cleared per F call.

Initially every stage cache is zero. Induction on completed boundaries gives
the following invariant on every computational record block: each accepted
pivot has exactly the C1 vectors that a fresh candidate of its value has;
unused and active bank caches are zero; and the immutable prefixes, signs
and axes determine one fixed tournament. Ordinary ticks read but do not
change saved caches. A boundary creates the exact pivot cache and moves the
whole bank. Thus every contender call agrees with that same tournament,
independently of the search stage or prior pivots. This blockwise statement
extends linearly to coherent records. A stored cache therefore preserves the
fixed edge relation. On arbitrary
unreachable archive words the cached values may be inconsistent; the total
circuit is still exact and reversible. Every reachable history for every
source state starts from zero cache fields, so such inconsistency is not
introduced by malformed source data.

The cache fields move with their whole banks; only public bank addresses
are used. On the actual inverse, the stage boundary is undone before old
ordinary guards, and the inverse cache operation sees its original candidate.
No pivot is measured, erased, copied to classical storage or recovered by
inverting source preparation.

## 8. Full space, generation and work account

The raw source, QND records and prefix records use O(Qn)=O(n^2) qubits.
The J+1 stage banks, including their caches, use O(J(n+Q))=O(n^2).
The boundary temporary arrays and its clean Boolean history use O(n^2).
The prefix divider uses O(n^2) scratch at setup and undo; the reusable cache
adder uses O(b), the fresh class cache O(Q), and exact score sums O(L).
A fixed number of these buffers can coexist, including old residual work
and fresh endpoint helpers. Total peak quantum storage remains O(n^2).
One need not reuse dirty work after answer copying to obtain this bound.
All arrays and their initialization/clearing are counted.

The classical store contains the public N, fixed-width public counters,
one current coefficient or gate word, private axes, and loop indices.
No measured label/prefix/pivot table exists. Each has O(n) bits in total.
Constants b,P,Q,J and all buffer lengths fit O(L)-bit address words.
The global tick has O(n) bits but is data for time comparisons, not an
address into an exponentially large stored schedule.

Use the full bit-stream controller in the packaged generator proof, Sections
1--6, and its complete aligned layout in Appendix A. Fixed field arrays and
power-of-two row/slot dimensions preserve the logical bank map and add only
a constant factor to space. Ready operand-address words, tape-head carry
walks and marked loop strips give O(m+A) raw actions for a complete m-bit
scan, with A=O(L). This includes initial addresses, copies/changes, actual
bit reads/writes, carry tests, all head moves and returns, endpoint tests,
rewinds and short-scan setup. A fixed number of strips uses O(n) bits.
The bound is for complete deterministic scans, including both directions.

C6 and the cache boundary have O(n^2 L) complete raw bit/head actions by
the generator's exhaustive cache/score/controller account. The ordinary
controller and full timing-constant generation have O(n^2) raw actions.
Short setup events number O(n^2) and cost O(A) each. There are exactly
Bclk=O(2^(n/2)) full ticks, including failed and unfinished searches. Apply
the full A indexed debit to every raw action, dispatch and fixed-arity
operand use. The actual reverse stream has the same full-scan count. Thus
repeated full work is

    O(2^(n/2)n^2 L^2).                                    (C7)

The prefix setup/undo costs O(n^3 L^2) charged work. Source acquisition,
QND preparation/undo, initialization, final answer computation and trit
endpoint add fixed polynomials in n. The existing deterministic finite
phase compiler costs 2^O(L^4) in total and uses O(n) classical and O(n^2)
quantum space, as in the cited full proof. There are no new approximate
phase sites: C1, score arithmetic, cache storage and controller extensions
use exact Boolean/Clifford+T gates. Each of those additive costs is absorbed
in C7 since every fixed polynomial and 2^O(L^4) is o(2^(n/2)). This is an
asymptotic comparison with absolute constants and includes all small n by
increasing the bound constant. It is not a free precomputation assumption.

All prefixes, coefficients, inverse words and cache fields are generated by
the stated algorithm. No external program state, random access service,
source inverse, source-dependent classical storage, or success-conditioned
resource bound enters C7. The new envelope changes the polynomial factor;
the time growth index remains one. Fraction 1/3, exact source count, both
space envelopes and unconditional success are unchanged.

