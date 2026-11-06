# Capped sequential shift testing (CST-128)

For every integer N >= 2 and every s in Z/NZ, put n=ceil(log2 N).
CST-128 uses k=n+4 tests per candidate and a single global acquisition
budget B=128N. This is one fixed configuration for all five claims.
Its success probability is greater than 29/32, and its branchwise bounds are

    T=O(N n^2) <= O(2^n n^2), S_C=O(n), S_Q=O(n), Q<=128N<=128*2^n.

Constants are absolute. The first four declared representative envelopes are
2^n n^2, n, n, and 2^n, with exact indices 1,0,0,1.

## 1. Complete algorithm and explicit cutoff

Store N, candidate t, a test counter j, and a global acquisition counter q.
Initialize t=q=0. For t=0,...,N-1, attempt k independent tests, stopping this
candidate at its first minus result. Immediately before acquiring any copy,
if q=B, output 0 and halt. Otherwise acquire one fresh source copy, increment
q, perform the test below, and discard/reset its registers after the test.
If k tests for t return plus, output t and halt. If every candidate is rejected,
output 0. All loop and acquisition bounds apply even on unsuccessful branches.
There are no restarts and no unbounded sampling or postselection loops.

A test on (b,y) applies the permutation

    (b,y) -> (b,G_b(y)),
    G_0(y)=y,
    G_1(y)=(y-t) mod N for y<N, and G_1(y)=y for y>=N.

Then apply H to b and measure b in the computational basis; outcome 0 means
plus. This uses only the supplied mixed state, exact arithmetic, and Clifford+T.
No Fourier transform, approximate rotation, source inverse, controlled source,
purification, subset-sum routine, or quantum addressed memory is used.

## 2. Exact test law and unconditional success

For a source component with offset x, the permutation produces

    (|0,x> + |1,(x+s-t) mod N>)/sqrt(2).

For t=s this is |+>|x>, so the result is always plus. For t!=s the two data
basis states are different, and the reduced state of b is I/2. Thus each wrong
candidate's test returns plus with probability exactly 1/2, for every x and
hence for the mixture as well. Fresh independent copies give independent
results conditional on reaching any test.

Analyze first the identical program with its budget check removed, calling
its total acquisitions X. It always stops by t=s. Conditional on reaching a
wrong t, the expected number of tests is

    sum_{j=0}^{k-1} 2^(-j) < 2.

The correct candidate requires at most k tests. Therefore, uniformly in N,s,

    E[X] <= 2(N-1)+k = 2N+n+2 <= 4N.

The last inequality uses n<=N and 2<=N, valid for every integer N>=2.
The probability that any wrong candidate is accepted is at most

    (N-1)*2^(-k) < 2^n*2^(-n-4) = 1/16.

Couple the capped and uncapped programs using identical source copies and
measurement randomness up to the capped stopping time. They produce the same
answer whenever X<=B. Markov's inequality gives

    Pr[X>B] <= E[X]/B <= 1/32.

Consequently the actual capped program outputs s with probability greater
than 1-1/16-1/32=29/32>2/3. The union bound needs no independence between
false acceptance and exceeding the budget. For s=0 the budget fallback can
only improve this lower bound. This is a bound for every fixed secret,
not an average-secret claim or a conditional-on-completion claim.

## 3. Uniform exact arithmetic with linear peak workspace

Here are sufficient gate and controller details, including invalid binary
encodings for arbitrary N. Build a Boolean circuit for G_b using a fixed
number of ripple carry/borrow additions, subtractions, comparisons and
bitwise selections on n+2-bit strings. First test y<N. On valid y and b=1,
select y-t if y>=t and y+N-t otherwise; on all other inputs select y.
Each ripple circuit has O(n) Boolean gates with bounded fan-in, and the whole
circuit has O(n) gates and intermediate bits. Constants N,t and n are supplied
by the classical controller, never by advice. The inverse uses modular addition:
on valid y choose y+t if y+t<N and y+t-N otherwise, and act identically on
invalid encodings. It too has O(n) Boolean gates and intermediate bits.

Reversibly compute each Boolean gate into a new zero scratch bit, XOR its
output into a separate target register, and reverse the computation to clear
all scratch. AND uses Toffoli; XOR and NOT use CNOT and X. Toffoli has an exact
constant-size Clifford+T implementation with a constant number of clean
ancillas, so no accuracy-dependent synthesis is required. This gives exact
XOR evaluation of G_b and G_b^{-1}, each with O(n) gates and O(n) scratch.
To implement the permutation in place, evaluate G_b from Y into zero Z,
swap Y and Z, and XOR G_b^{-1}(Y) into Z. Since G_b is a permutation of all
2^n encodings for each fixed b, the final Z is zero. Linearity makes this
valid when b and Y are entangled with each other or with the environment.
The control register is read but never erased during the arithmetic.

The fixed finite collection of ripple circuits can be generated gate by gate.
Assign each carry and intermediate result a wire number given by a constant
base offset plus a fixed multiple of the ripple position. A gate descriptor
then contains O(log(n+2)) bits. A forward or reverse pass needs only the ripple
position, pass identifier and a constant number of such wire indices. Constant
bits of N,t are accessed by that position. Retaining intermediate quantum
values does not require retaining a classical circuit listing: regenerate the
reverse pass from its pass identifier and descending position.

The permanent classical data N,t,q,B,j,k, binary counters and current gate
descriptor occupy O(n) bits. Here q and B have at most n+8 bits. Temporary
classical arithmetic is ripple arithmetic in O(n) bits; the controller never
allocates a table or stores previous samples or transcripts. Including the
source's n+1 accessible qubits, permutation target, retained Boolean-gate
values and constant-size decomposition ancillas, peak accessible qubits are
O(n). After each test all accessible qubits are measured/reset or discarded
and their allocation is reused. The inaccessible source is not charged as
storage, but every acquired copy is charged as both acquisition work and Q.

At most O(n) elementary arithmetic and decomposition gates occur per test.
The total allocated memory M is O(n), so the stipulated address length is
O(log(n+2)). Generating each descriptor, doing its small-index arithmetic,
reading a constant bit and applying the addressed gate costs conservatively
O((log(n+2))^2) classical bit operations including address charges on the
controller's own accesses. Initialization, measurement, reset and source cost
n+1 satisfy the same O(n (log(n+2))^2) work bound. Updating n-bit global or
candidate counters costs at most O(n log(n+2)) per test or candidate. There
are at most B tests and at most N candidate-loop iterations, even when a
candidate is rejected after its first test. Thus the entire uniform program
has

    T=O(N n (log(n+2))^2)=O(N n^2),

using (log(n+2))^2=O(n) for n>=1. All storage, addressing, circuit generation,
source acquisition and unsuccessful work have been counted. No uncharged
RAM access or real-number arithmetic is present. Small n, including N=2,
are covered by an enlarged absolute outer constant; the success argument
itself already holds at those inputs. The claimed n^2 time factor is a proved
conservative upper bound, not an assertion that log^2 n equals n.

## 4. Joint bounds, indices, and clean-input error model

On every execution branch, Q<=B=128N, independent of how often tests fail.
Combining this literal cap with the preceding implementation proves all four
resource bounds simultaneously for the same program and success probability.
For B_T=2^n n^2 and B_samples=2^n, the inner binary logarithms are respectively
n+2 log2 n and n. The definition in rules.md therefore gives exact growth
index 1 in each case. For B_C=B_Q=n, the double-logarithmic expression tends
to zero. The n=1 value does not affect any asymptotic limit. Multiplicative
outer constants do not affect these indices.

The fifth claim is epsilon(n)=0. Its error-model text is exactly the seed's:
"Malformed fraction among acquired copies. The proved guarantee requires every
copy to be an independent ideal coset state; no behavior is promised for
malformed copies."
Thus floor(epsilon(n) Q)=0 malformed copies are permitted, for every N and s.
Under this promise the same success and all resource guarantees hold. No
positive robustness theorem or maximal-tolerance theorem is asserted.

## 5. Provenance, comparison, and limits

The exact shift test and its controlled-permutation construction come from the
prepared repository seed, source cdb1ebff130d861e2c61e9cf517ab66c0a56ca7a.
CST-128 changes the algorithm by imposing a global acquisition cutoff and
increasing per-candidate tests from n+2 to n+4. The expectation/cutoff argument
is why the worst-case sample envelope loses a factor n; this is not merely
rewriting the old uncapped algorithm's existing guarantee. Streaming its
linear arithmetic establishes linear peak spaces and the time bound above.
Against the seed's declared envelopes 2^n n^4, n^2, n^2, 2^n n and the exact
same zero-tolerance model, all four guarantees improve asymptotically.
This is an incremental algorithm/accounting improvement, not a claim of a
new literature-best DCP time exponent or a proof of the cube-root target.

For research context, original primary references inspected are Greg Kuperberg,
"A subexponential-time quantum algorithm for the dihedral hidden subgroup
problem", arXiv:quant-ph/0302112, Theorem 1.1 and Section 5 Algorithm 2,
https://arxiv.org/pdf/quant-ph/0302112 ; and Greg Kuperberg, "Another
subexponential-time quantum algorithm for the dihedral hidden subgroup
problem", arXiv:1112.3333v1, Corollary 4.3 and Proposition 4.5,
https://arxiv.org/pdf/1112.3333 . The former addresses all moduli via a separate
general-N construction. The latter distinguishes quantum-access memory from
its counted classical-access simulation. Neither theorem is a premise of
CST-128; its proof above is self-contained. In particular no cube-root bound,
heuristic leading constant or free quantum-addressed lookup is inferred from
these papers. Square-root-time sieves can have incomparable storage guarantees.

Format validation is not mathematical certification. Hosted acceptance is
fallible mathematical review, not a formal proof. There is no measured local
score or quantum implementation asserted by this proof.
