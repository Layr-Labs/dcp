# Streaming private banks with centered coherent terminal decoding

For every N>=2 put n=ceil(log2 N), L=log2 n. Use the terminal-block solver specified in terminal-block.md, which modifies
the original BASE13 solver in base13.md. The choice of overrides is
fixed for the entire execution and for all solver banks. It recovers
the entire shift with probability at least 2/3 on ideal input.
The new deterministic padding maximum is P=2^25 n^3 on every
branch. Each bank keeps consuming padding after its solver stops
until it receives P copies. Enforce both solver caps, guarded record
sizes and output range on malformed transcripts, returning 0 on abort.

Let z be the smallest positive integer with z^11>=n, computed by
binary search with exact integer comparisons. Use J=4096z solver banks
of size P and one verification bank of size
V=8192(n+8). Acquire exactly Q=JP+V copies, even if a controller
fails or the permutation sampler aborts. The malformed-position set
is fixed before private coins, and the good systems have exactly the
ideal product marginal. The tolerated fraction is
epsilon=L/(536870912 n^3), with epsilon(1)=0. In particular
epsilon P=L/16 and epsilon<=1/64 on every length.

The algorithm and the precise proof use the streaming assignment
and the shared classical verification reserve described below.
At each source request the next stream position is assigned using
the bounded weighted-count draw. On sampler abort all subsequent
copies are acquired and discarded and the algorithm outputs 0.
Complete all remaining solver work, then select the first candidate
whose approximate verification score is at least 1/4, or output 0
if there is none. Process all verification records using the native
readout below and the final grid score approximation. The shared
reserve is reserved exclusively for that computation, and solver
controllers never learn its data before their outputs are fixed.

For fixed bad positions the hypergeometric probability q for a clean
solver bank applies with Q=JP+V. Since J>=4096,
x_i=m/(Q-i)<=epsilon*4096/4095 for i<P. Here epsilon<=2^-20
on every length, so x_i<1/4096. Then ln(1-x)>=-x/(1-x) gives
ln q >= -(4096/4095)^2 epsilon P. The inequality ln 2>69/100
follows from the first three positive terms of the log series
2(1/3+1/(3^3*3)+1/(3^5*5)) for ln 2. Since
(4096/4095)^2 < 16*(69/100)/11 and epsilon P=L/16,
we have q>=n^(-1/11), so Jq>=4096 and in particular >=64.
The clean-bank variance bound gives failure at most 3/128. The separate unconditional failure bounds
for assignment sampling, excessive reserve contamination,
simultaneous good-score deviations and joint good label-readout
errors are each at most 1/256. Their union with the clean-bank
failure still has probability below 1/8. No event is evaluated
under an assumption that the verifier and solver banks are
independent; the independence used is only for local operations
within the good reduced marginal at fixed assignment.

At most J complete times the terminal-block clean solver work bound are paid, with
O(log(n+2)) physical address length throughout because all actual
storage is polynomial. The assignment tree, V readouts, all J
score evaluations, padding acquisition and cleanup are polynomial
and are absorbed in O(2^(n/6) n^(259/66) L). Work for n=1 is finite
and the envelope is interpreted asymptotically. Each suspended
controller owns O(n^2) classical bits and O(n) qubits by the
base proof, including its own paused scratch and counters.
The combined classical space is O(J n^2+nV+J log Q)=O(n^(23/11))
and the quantum space is O(Jn+n)=O(n^(12/11)). Store the current
source register and reserve readout scratch once and charge
them explicitly. Address-index additions are ordinary bit
arithmetic, memory access is classical and no coherent bank
lookup is used. The exact Q expression is O(n^(34/11)). The time
growth index is 1 from the positive linear exponent n/6.
The other three indices are zero since they are polynomial.

# Private bank amplification for fixed malformed positions

For the specified streaming assignment, analyze an equivalent
uniform partition of the stream positions into fixed-size banks.
Each solver acts locally with independent private coins. Its
classical output is retained for the shared reserve test.

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

For the selected schedule, the preceding hypergeometric bound
q>=n^(-1/11) and the nonpositive pair covariances show a clean
successful candidate exists with failure at most 3/128.

The verification count X for any reserve of V copies obeys
E[(1+z)^X] <= (1+epsilon z)^V for z>=0: expand over subsets
of slots and use (m)_l/(Q)_l <= epsilon^l for each term.
At z=7, Pr[X>V/8] <= exp(-V/8) because
7/64-3 ln(2)/8 <= -1/8. Candidate tests use one shared
reserve and bound errors simultaneously over all candidate values.

## Streaming the bank assignment with a shared classical reserve

Set Q=JP+V and allocate remaining-count leaves for J solver bins of
size P and one verification bin of size V. Before each acquisition
draw a rank uniformly from [0,R), where R is the total remaining
count. Descend a binary tree of count sums to find its bin, subtract
one from that leaf and its ancestors, and send the next register
there. A category assignment has probability P!^J V!/Q! by
multiplying the successive remaining counts divided by R. Thus the
assignment is exactly the image of a uniform permutation. For each nontrivial range draw, reject out-of-range binary strings
of ceil(log2 R) bits, stopping after ceil(log2(256Q)) tries.
The chance of failing that draw is at most 1/(256Q). Complete
success has failure at most 1/256 by union bound and preserves
the stated uniform law because the individual failure probabilities
depend only on the public ranges. The count tree is unchanged,
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

The next section implements this scoring measurement on the
good reduced marginal, with a joint comparison error of at most
1/256. Every malformed transcript is mapped to a bounded score.

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
