# Four-level streaming private banks for polynomial-source DCP

For every N>=2 put n=ceil(log2 N), L=log2 n. Use the four-level solver specified in four-level.md, which modifies
the original BASE13 solver in base13.md. The choice of overrides is
fixed for the entire execution and for all solver banks. It recovers
the entire shift with probability at least 2/3 on ideal input.
The new deterministic padding maximum is P=2^41 n^5 on every
branch. Each bank keeps consuming padding after its solver stops
until it receives P copies. Enforce both solver caps, guarded record
sizes and output range on malformed transcripts, returning 0 on abort.

Let z be the smallest positive integer with z^10>=n, computed by
binary search with exact integer comparisons. Use J=64z solver banks
of size P and one verification bank of size
V=8192(n+8). Acquire exactly Q=JP+V copies, even if a controller
fails or the permutation sampler aborts. The malformed-position set
is fixed before private coins, and the good systems have exactly the
ideal product marginal. The tolerated fraction is
epsilon=L/(35184372088832 n^5), with epsilon(1)=0. In particular
epsilon P=L/16 and epsilon<=1/64 on every length.

The algorithm and the precise proof use the streaming assignment
and the shared classical verification reserve described below.
The alternative exact shifted-X reserves are intermediate constructions
and are not allocated or executed in the selected algorithm.
At each source request the next stream position is assigned using
the bounded weighted-count draw. On sampler abort all subsequent
copies are acquired and discarded and the algorithm outputs 0.
Complete all remaining solver work, then select the first candidate
whose approximate verification score is at least 1/4, or output 0
if there is none. Process all verification records using the native
readout below and the final grid score approximation. The shared
reserve is reserved exclusively for that computation, and solver
controllers never learn its data before their outputs are fixed.

For fixed bad positions, the clean-bank mean and variance proof
applies with Q=JP+V and Q>=2P. For all i<P, Q-i >= (63/64) Q, so x_i=m/(Q-i)<= (64/63)epsilon
<=1/63. The inequality ln(1-x)>=-x/(1-x) therefore gives
ln q >= -(64/62)epsilon P >= -(16/15)epsilon P = -L/15.
Since ln 2>=2/3 by the tangent-line lower bound for the integral
of 1/x on [1,2], q>=n^(-1/10). Thus Jq>=64 and the probability
all clean-bank solvers miss is at most 3/128. The separate unconditional failure bounds
for assignment sampling, excessive reserve contamination,
simultaneous good-score deviations and joint good label-readout
errors are each at most 1/256. Their union with the clean-bank
failure still has probability below 1/8. No event is evaluated
under an assumption that the verifier and solver banks are
independent; the independence used is only for local operations
within the good reduced marginal at fixed assignment.

At most J complete times the four-level clean solver work bound are paid, with
O(log(n+2)) physical address length throughout because all actual
storage is polynomial. The assignment tree, V readouts, all J
score evaluations, padding acquisition and cleanup are polynomial
and are absorbed in O(2^(n/8) n^(51/10) L^(3/2)). Work for n=1 is finite
and the envelope is interpreted asymptotically. Each suspended
controller owns O(n^2) classical bits and O(n) qubits by the
base proof, including its own paused scratch and counters.
The combined classical space is O(J n^2+nV+J log Q)=O(n^(21/10))
and the quantum space is O(Jn+n)=O(n^(11/10)). Store the current
source register and reserve readout scratch once and charge
them explicitly. Address-index additions are ordinary bit
arithmetic, memory access is classical and no coherent bank
lookup is used. The exact Q expression is O(n^(51/10)). The time
growth index is 1 from the positive linear exponent n/8.
The other three indices are zero since they are polynomial.

# Private bank amplification for fixed malformed positions

For deterministic clean solver budget P(n), first acquire a fixed
Q=(J+1)P copies, then privately permute them. Reserve P for
verification and partition the remainder into J disjoint banks
of size P. Analysis is for the fixed-position model in which
the reduced state on all nonmalformed positions is exactly
the product of ideal copies. Each bank runs an independent
complete capped solver with no transfer of its computational
state to the other banks. Retain every proposed classical answer.

Suppose a fixed bad set has size m. The probability q that a
particular solver bank is completely clean is

    q = product_{i=0}^{P-1} (1 - m/(Q-i)).

Two distinct banks' clean events have joint probability at
most q^2: conditional on the first bank being clean, the
m bad positions in the remaining Q-P locations are uniform,
so a second P-tuple is no likelier to be clean. Conditional
on the permutation, the entire set of clean banks has its
ideal product marginal. The complete run of all solvers
uses a tensor product of bank-local instruments with
independent private coins. Operations on other banks cannot
change the marginal output distribution of the clean banks,
even if malformed systems are entangled with them. Thus if
each clean solver succeeds with fixed probability r>=2/3,
the Z count of clean banks that succeed satisfies

    E Z >= (2/3) J q,    Var Z <= E Z.

For the second bound, for each pair condition on both clean
and the permutation. The successful output events are
independent with the same ideal success probabilities,
which do not depend on the permutation. Combine with the
nonpositive covariance of clean bank indicators. Consequently
Pr[Z=0]<=3/(2 J q).

For J>=n^d, d>=1, Q>=2P, and epsilon(n)=c log2(n)/P,
whenever epsilon<=1/4 we have m/(Q-i)<=2epsilon<=1/2.
Using ln(1-x)>=-2x on [0,1/2], q>=exp(-4epsilon P)
= n^(-4c/ln 2). In particular c<=d/16 guarantees
Jq>=n^(d/2), since ln 2>=1/2. The source budget must pay
all J banks even if the first correct candidate is early.
For a supported monomial one can take a proved hard cap
P<=C n^a (log2 n)^b and declare c/C times n^-a (log2 n)^(1-b),
using a separate all-length precondition and finite fallback
where needed.

The verification bank can be made larger than P or chosen
independently after acquisition if care is taken to keep
a fixed total budget and preserve the lower bound on q.
Its expected corruption fraction equals m/Q, so Markov
bounds the probability it exceeds any specified threshold.
Candidate-verification need not condition on the clean-bank
success event. Instead bound simultaneous false acceptance
over all possible secrets and true acceptance separately using
an independent randomized measurement of the verification
bank, and union-bound these events with Z=0. A union over
only the actual candidates needs additional argument if
those candidates can be correlated with the verification
outcomes through malformed entanglement.

This proof yields a logarithmic factor in the admissible
fraction over constant-repeat clean-bank majority wrapping,
in exchange for a polynomial multiplier in source and total
work caps. It applies to the fixed-position good-marginal
model and its private random permutation. It does not
justify conditioning clean bank contents on an online
adversary's later replacement decisions.

## Verification with one private reserve per candidate

Use Q=2JP and pair every solver bank with a separate reserve of P copies.
Assume epsilon<=1/64. For a uniformly sampled reserve, let X count its
malformed positions. For any fixed subset of l distinct slots, the
probability that all are bad is (m)_l/(Q)_l <= (m/Q)^l <= epsilon^l.
Consequently, for z>=0,
E[(1+z)^X] <= (1+epsilon z)^P by expanding the product of slot
indicators. At z=7 this gives

    Pr[X>P/8] <= (1+7/64)^P * 8^(-P/8) <= exp(-P/8),

using 7/64-3 ln(2)/8 < -1/8. A union bound over J reserves does
not require independent counts.

For a candidate t, run the original exact shifted-X test on each
copy of its corresponding reserve, using the identity extension
for labels outside the valid residue range. Accept if at least
3P/4 outcomes pass. On capped reserves X<=P/8, the true candidate
passes deterministically because all ideal copies pass; possible
effects of the malformed copies on the ideal reduced outcomes do
not change this certainty. For a fixed false t, on a reserve with
g=P-X good copies, their success outcomes are independently fair.
Acceptance requires at least 3P/4-X good successes. Relative to
g/2 this is P/4-X/2 >= 3P/16 above the mean. Hoeffding bounds the
pass probability by exp(-9P/128).

For use with a correlated candidate, analyze a separate circuit
for each (reserve index, t) in which the solver outputs are still
recorded but the verification program always uses the fixed t.
The probability of both observing proposed t and accepting in this
circuit equals the corresponding joint probability in the real
candidate-controlled circuit. In the fixed-t circuit one can
drop the proposed-t condition and just use the marginal verification
bound. This argument multiplies by at most JN in a union bound.
It makes no conditional independence claim for the actual proposed
candidate. After verification return any accepted value or 0 on
failure.

A single sufficient choice is P>=32(n+ceil(log2 J)+8). Then both
J exp(-P/8) and JN exp(-9P/128) are <1/256, using N<=2^n and
ln 2<1. The solver is padded to P, and its reserves are padded to P
even after decisive test outcomes. Together with the independent
clean-bank success proof, this verifies the wrapper when Jq>=16.
For all n>=1, J=64n^d and a capped clean count P(n)<=C n^a L^b
with a>=1 and b>=0, include the verification minimum in P(n).
Choose a supported coefficient small enough that
epsilon P <= (d/16) log2 n and epsilon<=1/64 uniformly (with
epsilon=0 at n=1 if the expression has positive log power).
If using log-factor-free counts, a>=1 implies log2 n/n^a<=1.
The earlier bound now gives Jq>=64 n^(d/2). Hence the sum
of all failure probabilities is below 1/8, including a
permutation sampler with failure <=1/256.

For the exact uniform permutation, use classical Fisher-Yates
on Q address records after acquisition. For each bounded draw,
reject out-of-range strings of ceil(log2(range)) fair bits and
stop after ceil(log2(256Q)) attempts. Each step fails with
probability <=1/(256Q). Conditional on complete success the
permutation is uniform, since per-step success is independent of
its accepted value and ranges follow a fixed public schedule.
A physical implementation need only permute handles to stored
n+1-wire sample registers. The entire bank allocation costs
O(n JP) qubits and the ordinary index permutation costs
O(JP log(JP)) bits before the local solver workspace.
Physically move samples into the solver source register on
request, count every register and padded acquisition, and
keep the solver's original caps. Each use relinquishes the old
sample location, and all source wires are analyzed as owned
input registers. All permutation controls are classical; full
address width is paid during swaps, measurement and bank
lookup. These costs can dominate memory and are part of the
wrapper's genuine tradeoff.

## Streaming the bank assignment with a shared classical reserve

Set Q=JP+V and allocate remaining-count leaves for J solver bins of
size P and one verification bin of size V. Before each acquisition
draw a rank uniformly from [0,R), where R is the total remaining
count. Descend a binary tree of count sums to find its bin, subtract
one from that leaf and its ancestors, and send the next register
there. A category assignment has probability P!^J V!/Q! by
multiplying the successive remaining counts divided by R. Thus the
assignment is exactly the image of a uniform permutation. Capped
range sampling as above adds at most 1/256 unconditional failure,
and the state of the count tree needs O(J log Q) classical bits.
The actual indexed arithmetic and O(log J) tree levels are charged.
The fixed-position promise is essential because assignments are
interleaved with local operations.

For a resumable solver, keep J independent copies of its state
waiting at acquisition boundaries. When its bin receives a copy,
run until its next source request or termination; extra copies
after termination are discarded. Initialize each solver up to its
first request and finish pending computation after the final copy.
For each fixed successful assignment the total action on all
banks is the tensor product of their capped local instruments,
because they act on disjoint systems and make no cross-bank
decisions. Interleaving therefore leaves the clean-bank product
marginal and all success probabilities unchanged. Its solver
storage is O(J S_C) classical bits and O(J S_Q+n) qubits, including
saved controllers and one source temporary. Address widths rise
to reflect total memory. No JP-register sample array is required.

For the single shared verification bin, consider ideal measurement
of the Fourier label W in [0,N), followed by a private fair choice
of X or Y axis beta=0 or pi/2 and a row-qubit sign Z. Discard the
register immediately. Store (W,beta,Z); malformed padding may
be mapped to an arbitrary fixed record. The reported score for
candidate a is the average of
Z cos(2pi aW/N-beta), each term bounded by 1 in absolute value.
For every good position the mean is 1/2 when a=s, and 0
otherwise, from averaging the two axes and applying orthogonality
of cyclic characters. Their joint marginal is independent across
good positions even though neither bad measurements nor solver
outputs need be independent. If at most V/8 positions are bad,
the true total expected-good contribution divided by V is at
least 7/16; bad terms lower it by at most 1/8. A false score has
zero expected-good contribution and bad terms raise it by at
most 1/8. Hoeffding for unconditioned good scores shows that all
V-normalized good contributions differ from their means by
at most 1/32 except with probability 2N exp(-V/2048).
Thus the exact scores satisfy true >=9/32 and false <=5/32.
A uniform arithmetic approximation error <=1/64 preserves
separation at threshold 1/4. With V>=8192(n+8), the failure
probability is <1/256. The bad-count tail applies to this
single bin with V in place of P. Its label records cost O(nV)
bits, verification needs only a reusable source-size quantum
register and the label-readout workspace, and testing J
candidates uses JV polynomial-width score evaluations.

The label measurement described here is ideal. To use this
in a candidate proof, instantiate a counted native Fourier
label instrument with an unconditional full-reference
comparison error <=1/256 for the V reserve measurements.
This must preserve the actual joint good marginal and allow
arbitrary correlated malformed records. It does not require
an approximation guarantee on a bad label report if the
implemented score stays in [-1,1] on every report. For the
coefficient bound on fully clean solver banks, the previous
estimate m/(Q-i)<=2epsilon still holds since Q>=2P. No other
part of that estimate relies on a one-to-one allocation of
reserves to solver banks.

## Counted native readout for the shared verification reserve

The shared verifier only uses the joint marginal of the good reserve
records, and all bad record scores are bounded. Its proof therefore does
not need a full-reference comparison of good Fourier labels with an
unchanged bad/reference state. More precisely, fix the successful private
assignment. Each reserve copy is processed by its own local circuit, whose
coins are not derived from the solver outcomes. The reduced state on the
good reserve copies is the ideal product by assumption; operations on the
other systems preserve this marginal. Inside the proof of that marginal
alone we may sample independent uniform hidden labels k and condition
on the Fourier eigenstate and its matching row phase. This resolves the
native readout requirement without adding a dephasing circuit on the
actual inputs or conditioning a good outcome on any bad output.

Use A_j = ADD(2^j mod N) on the position register for 0<=j<=n+3,
acting as identity on binary padding. On the Fourier eigenstate with
phase k/N, its eigenvalue is exp(2 pi i 2^j k/N). Prepare a probe
in |+>, apply controlled A_j, and measure the probe in X or Y.
The expectations are respectively the cosine and sine of the indicated
angle, with Fourier signs chosen so that the row phase is +2 pi k s/N.
This convention uses Fourier ket proportional to sum_x exp(-2 pi i k x/N)|x>.
Neither test changes the eigenstate, and the row is untouched until its
final private X/Y measurement. Fixed shifts use ordinary modular
addition and comparison with O(n) Boolean gates and O(n) temporary
bits for a ripple-carry construction. To implement the bijection with
padding and an extra control, evaluate it into a fresh register,
swap registers, then XOR its explicitly inverse controlled subtraction
into the old register. Uncompute scratch in both evaluations. The
result is exact over Clifford+T using Toffoli and the X/Y bases.

Use R=2^16 ceil(log2(4096 V(n+4))) repetitions per axis per j,
with the empirical mean of each axis. Hoeffding and a union bound
over all good probes imply that every mean differs from its value
by at most 1/32 with failure <=1/256. The estimate does not require
any condition on the malformed outputs. Finite fixed rational
sine/cosine samples at angles 2 pi l/128 within 1/1024 of their
values suffice for rounding. Take a nearest point to the empirical
vector among those fixed samples. If both means are accurate, the
chosen exact circle point has chordal distance from the true point
at most 2 sqrt(2)/32 + pi/128 + 2 sqrt(2)/1024 <1/4.
An angular distance of at least 1/16 turns has chord at least
2 sin(pi/16)>=1/4 by the chord bound on sine. Thus this gives a
dyadic estimate z_j within 1/16 turns of 2^j k/N on the circle.

Starting with z_(n+3), descend j. Given the refined estimate at
j+1, form its two inverse doubling images on the circle, a half
turn apart. Choose the image nearer z_j. The correct lift is within
1/32 turns of the true value at j; its distance to z_j is <=3/32,
while the other image's distance is >=13/32. This induction halves
the error at every descent. The estimate at j=0 therefore has
circular error <=2^(-n-3)/16. Multiply by N and choose the nearest
integer modulo N, which returns k because N<=2^n. This also gives
a full deterministic decoding rule on every possible malformed
probe transcript by fixed tie breaks. The row probe is measured
independently of the reported label, so on the good marginal its
sign law coincides with the ideal record law whenever all good
labels were decoded correctly under the hidden-label coupling.

Generate shifts by repeated doubling with modular reduction. Keep
the O(n) dyadic z_j as constant-width words, their running refined
estimate in O(n) bits, and the repeat counters in O(log(Vn)) bits.
There is no need to store any eigenvector or prepare an inverse
source. For V=8192(n+8), the readout performs O(n log(n+2))
probes per copy and uses O(n) working bits and qubits before its
stored verification records. Its arithmetic and gate emission
cost O(n^2 log(n+2)) per copy before the address-width charge.
Nearest-point comparison uses integer comparisons with the
fixed rational table. The candidate score itself needs only a
constant angular accuracy: compute aW modulo N by schoolbook
arithmetic, and round the fractional turn on a fixed grid of
at least 1024 points, with cosine values precomputed to within
1/1024. This gives less than 1/64 worst-case term error on every
report. Each candidate costs O(V n^2) unaddressed operations.
