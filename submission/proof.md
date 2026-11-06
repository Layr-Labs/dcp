# One-third malformed-copy tolerance with quadratic workspace

## 0. Joint theorem, algorithm and source model

For every integer N>=2 and every secret s in Z/NZ put n=ceil(log2 N), K=2^n.
The algorithm below acquires exactly Q=192 copies when N=2 and exactly
Q=27648(2n+20) copies when N>=3. Put r=Q/3. Under the following error model,
with epsilon(n)=1/3, it outputs the entire s with unconditional probability
at least 11/16>2/3. On every execution branch the SAME algorithm and parameter
rule jointly satisfy

    T=O(2^(n/2)n^10), S_C=O(n^2), S_Q=O(n^2), Q=O(n).

All constants are absolute and independent of N, s, the adversary and outcomes.
These are full worst-case bounds in the uniform Clifford+T/bit-operation model,
including source acquisition, gate generation, precision, initialization,
measurements and address charges. The four envelope growth indices are 1,0,0,0.
Indeed log2(2^(n/2)n^10)=n/2+10log2 n has double-logarithmic index 1;
every fixed positive polynomial envelope has index 0. The fifth expression is
the constant fraction 1/3, with no validity threshold.

### Error model (verbatim specification)

Adaptive malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires, and epsilon(n) the tolerated malformed fraction. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm, and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed; on every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. A malformed copy is an arbitrary (n+1)-qubit state (the register shape of an ideal copy) supplied from the adversary's system: it may be pure or mixed, may be entangled with the adversary's remaining system and with other malformed copies, and may depend on all of the information above; it is not entangled with clean copies or with the algorithm's workspace, ancillas or internal random bits. Every copy that is not malformed is clean: at the moment of its delivery, a fresh ideal coset state rho_s = (1/N) sum_x |psi_{x,s}><psi_{x,s}| in tensor product with everything else (the adversary's system, all other copies and the algorithm's workspace), i.e. clean copies are independent ideal coset states. The adversary interacts with the algorithm only by supplying copies; after delivery it has no access to the copy or to the algorithm's quantum or classical systems. All measurements have countably many outcomes. The algorithm is not told which copies are malformed. Quantifiers: the guarantee must hold for every N >= 2 (no validity threshold), every s in Z/NZ and every such adversary, including the adversary that corrupts nothing (the clean problem): the algorithm outputs the entire s with probability at least 2/3, and the four declared resource bounds hold on every execution branch. The fraction bounds the number of malformed copies among acquired copies; it is not a per-copy corruption probability.

### Lemma 0: acquiring the whole bank removes supplier feedback

The first operation involving sources is to acquire all Q raw (n+1)-qubit
registers into a bank, in the deterministic order 1,...,Q. The algorithm makes
NO measurement, private random draw, source transformation or abort decision
until the last copy has arrived. This also applies to N=2. Public allocation
and source counters are deterministic. Only afterward are private axes drawn
and the operations in Sections 1-8 performed. The initial bank takes Q(n+1)
qubits and Q(n+1) source work units, within the stated bounds.

For this acquisition schedule, every adversary in the stated adaptive model
produces a mixture of fixed-position inputs of the following form: a set B
of at most r malformed slots, an arbitrary joint density on those slots,
and independent rho_s factors on all other slots, tensor-independent of the
malformed subsystem. Here B and its density may depend on N and s.

Proof. Add a hidden classical register recording each clean/malformed decision.
Inductively, conditional on a prefix B of these decisions, the unnormalized
joint operator is a product of rho_s on its clean slots and a positive operator
on the earlier malformed slots and the adversary's remaining system. A private
adversary instrument acts only on the latter factor; it may steer earlier
malformed slots but cannot change any clean factor. A malformed delivery moves
a subsystem of that factor into the next slot. A clean delivery appends a fresh
rho_s tensor factor by the delivery promise. There is no algorithm outcome on
which later decisions could depend. This proves the induction without assuming
independence between malformed deliveries. At the end, trace out the adversary
and condition only on B. Summing private instrument outcomes preserves each
clean tensor factor, including countably many outcomes. There are finitely many
possible sets B; after normalizing their nonzero weights this is the asserted
convex mixture. The pathwise cap gives |B|<=r. Any later trace-preserving private
operation is irrelevant to the algorithm's reduced bank state. Consequently it
suffices to prove uniform success for every such fixed B and bad-block density;
linearity then gives the guarantee under the full adaptive model. No conditioning
on the algorithm's later honest measurements is used in this reduction.

For a fixed B, the proof below allows arbitrary entanglement within the bad
block and with an inaccessible purification. The algorithm is not given B.

### Algorithm summary

After acquiring the bank, record one valid-position/QND Fourier-label register
and one private X/Y sign per copy, without measuring the source-dependent
records. Compute scores from these read-only records, run the bounded coherent
class selector, copy only its final class, and undo its actual known circuit.
At even N resolve the remaining half-turn pair by trit measurements on that
same bank. At odd N return the singleton class. N=2 skips coarse selection and
uses the trit decision directly. All loops have the public finite bounds below.

## 1. Bounded rational pair witnesses

Let U_v add v moduloN on row1 of valid positions and act identically on padding.
R_v=U_v X_row U_v^dagger is a known Hermitian involution, equal to X_row on
padding. On valid words rho_v=(P+R_vP)/(2N), with P the valid projector.
For A=(R_t-R_u)/2 define

    M_tu=(7A-2A^3)/5
        =[11(R_t-R_u)+R_(2t-u)-R_(2u-t)]/20.                  (1)

All labels in reflections are reduced moduloN. The identity follows from
R_t R_u R_t=R_(2t-u) and involution squares. The scalar polynomial is increasing
on[-1,1], since its derivative(7-6x²)/5>=1/5, and takes endpoint values+/-1.
Thus ||M_tu||<=1. Padding cancels because all R_v equal X there.

Translation traces give tr(R_v rho_s)=1_[v=s]. For distinct, nonantipodal t,u,
equation(1) therefore has honest expectations+11/20 at rho_t and-11/20 at
rho_u. At antipodes the means are+/-1/2 and those comparisons are omitted.
For at least2/3 honest mass, the true oriented mean against any other class
is at least(2/3)(11/20)-1/3=1/30, and the false orientation against s is
at most-1/30. This operator bound applies to EVERY malformed density matrix.

## 2. One-pass QND label records, without repetition history

Let T1 shift a valid position by1 moduloN and be identity on padded positions.
Its valid eigenvectors are

    |chi_k>=N^-1/2 sum_x exp(-2pi i kx/N)|x>, k in Z_N,

with eigenvalues exp(2pi i k/N). Compute and retain an exact valid-position
flag. Use standard phase estimation of this KNOWN permutation with

    t=n+18 phase bits, B=2^t.

Prepare uniform phase-time, apply controlled T1^(2^j), then an inverse dyadic
QFT on the t ancillas. Controlled shifts are known modular additions, guarded
on the ENTIRE valid-domain circuit. They preserve every eigenvector; no inverse
of source preparation appears. Round the phase word z to

    k'=round(N z/B) modN,

by reversible integer multiplication/shifts/comparison. Retain z,k',flag and
the original source position. This requires O(n) logical bits per copy.

Here is a uniform label-error bound. For eigenphase phi=k/N the ideal amplitude
of z is B^-1 sum_(a=0)^(B-1) exp(2pi i a(phi-z/B)). With circular word-distance
d_z=dist(z,B phi) in[0,B/2], its probability is <=1/(4d_z²) away from d_z0,
because |sin(pi d_z/B)|>=2d_z/B. There are at most two integer words in each
unit distance interval. For integer R>=3 the tail at distances>=R is at most

    1/[2(R-2)].

All word-distances<R=2^(t-n-1)=2^17 round correctly: R/B=2^(-n-1)<=1/(2N).
An inverse-QFT operator-norm error<=2^-14 adds at most2^-14 to a measurement
event's probability. Tail plus this error is<1/2048, uniformly on EVERY
position eigenstate, including phase wraparound. The factor2 slack for a
state-distance convention would also fit the same1/2048 budget.

The implemented QPE is still exactly QND in the position eigenbasis: all
position operations are exact controlled powers of T1; every approximate
Fourier gate acts only on ancillas. In particular the record-score observable
is block diagonal in the actual position eigenvalue, even for malformed
inputs coherent across different k. No ideal clean spectral-copy isometry is
assumed. On padding the retained flag makes the score zero.

Inverse-QFT approximation uses finite Clifford+T gate words with a public
operator error budget2^-14. The synthesis/generation costs and possible
phase-helper leakage are addressed below. Known arithmetic helpers for the
position shifts are separate and return clean for every declared source word.

Never CONTROL a one-qubit word certified only up to global phase. For
P_phi=diag(1,exp(i phi)), implement its controlled phase by the physical sequence

    P_(phi/2)(a), P_(phi/2)(b), CX_(a,b),
    P_(-phi/2)(b), CX_(a,b).

The exponent is(phi/2)[a+b-(a XOR b)]=phi*a*b. The three synthesized words
are unconditional, so their global phases multiply to one input-independent
global phase. Choose each one-qubit approximation error<=2^-20/(t+1)^2;
there are fewer than t²/2 controlled-QFT phases, hence their total error is
below2^-14 with slack. H gates and swaps are exact. All approximate gates act
only on phase ancillas, preserving the exact QND block structure.

## 3. Simultaneous private-axis estimates on arbitrary bad inputs

On valid position eigenvalue k, R_v is the row observable

    cos(2pi kv/N) X+sin(2pi kv/N) Y.

Choose a private fair axis X or Y for each copy, store those O(Q) classical
bits, rotate its row into that measurement basis and RETAIN the quantum sign
record. The choices are independent of delivered sources. Write y=(-1)^rowbit.
For every pair t,u form arithmetically

    h_tu(k)=[11(e^(2pi ikt/N)-e^(2pi iku/N))
                  +e^(2pi ik(2t-u)/N)-e^(2pi ik(2u-t)/N)]/20.

The ideal statistic is2y Re h on X,2y Im h on Y. Its mean is tr(M_tu rho)
for EVERY source state rho, and |h_tu(k)|<=1 by the block norm of(1). The
same record estimates all pairs, with no selected pair table or QRAM.

Evaluate each sine/cosine with absolute fixed-point error<=1/2048 and clamp
each resulting real/imaginary h component to[-1,1]. The coefficient absolute
sum is24/20=6/5. On a correct label, a score changes by at most(12/5)/2048;
on a wrong label the score difference is at most4, with probability<=1/2048.
Thus the implemented mean observable differs from M in operator norm by at most

    beta=(12/5+4)/2048=1/320.                                (2)

This is also a bad-input bound: QND label effects are diagonal on position,
the conditional row state is arbitrary, each axis is fresh, and the estimate
holds in every valid block and is zero on padding. Off-diagonal position
coherences do not contribute to that observable. Score values are exactly
computed bounded rational values in[-2,2] with one fixed public denominator, not physical arbitrary rotations.

Condition on the hidden malformed set B furnished by Lemma 0. Counterfactually
reveal each copy's ENTIRE local shadow instrument sequentially: its fresh axis,
QPE label and row-sign records, before moving to the next copy. These local
instruments commute across distinct slots, so this order gives the same joint
record law as the retained coherent implementation. The filtration does not
reveal future axes or future QPE/sign records. Before its fresh axis, copy i
has some conditional density rho_i; an untouched good slot remains exactly
rho_s, while bad slots may be arbitrarily conditioned and entangled. In every
history at least 2Q/3 of the conditional means are honest ones. Hence true/false implemented
means retain magnitude at least1/30-beta=29/960. Centered increments have
absolute bound4 and conditional variance<=4. Scalar conditional Bernstein at
delta=1/48 gives each pair failure at most

    2 exp[-Q/27648],

since 2(4+4delta/3)<12 and delta²=1/2304. This bound follows by expanding the
centered MGF: for |X|<=R, lambda R<3,
E e^(lambda X)<=exp(lambda² E X²/[2(1-lambda R/3)]), using
k!>=2*3^(k-2); iterate and optimize, also applying it to-X.

A union over fewer than K² pairs yields

    failure<=2 K² exp[-(2n+20)]<=2^-19.                       (3)

On the simultaneous event, true oriented scores are STRICTLY positive and
all false-vs-true scores STRICTLY negative, since29/960>1/48. No independence
of malformed records or assumption about two false candidates is used.

## 4. Total class tournament and an implicit contender set

At odd N the C=N classes are singletons. At even N the C=N/2 classes are
{p,p+N/2},0<=p<C. For two different class IDs canonicalize their order. The
first class wins iff SOME member has nonnegative empirical score against EVERY
member of the second; otherwise the second wins. This defines one orientation
for each edge, even with ties or arbitrary wrong-class scores. On event(3),
the true class is a Condorcet winner: its actual s row beats all members of
every wrong class; no wrong row can beat s. Only this strong-winner property
is used, not transitivity.

Represent the current contender set implicitly as valid class addresses that
beat every previously accepted pivot. The predicate scans the previous pivots
and computes their edges from the Q read-only shadow records. It stores no
exponential candidate or edge table. Candidate/pivot labels are ordinary
quantum operands in reversible arithmetic; record addresses are public loops.

For a uniform pivot p from a nonempty contender set S, keep S'=vertices in S
beating p. For ANY tournament,

    E_p |S'|=(|S|-1)/2.

The global winner remains in S until chosen, whereupon S' is empty. After
J=n+24 rounds, the ideal always-successful uniform-pivot process misses it
with probability<=K/2^J=2^-24. Empty-set detection returns the preceding pivot;
if the finite rounds end without an empty-set report, return the most recent
accepted pivot (0 if none). This includes selecting the true class in the
LAST round; a fallback0 there would require an off-by-one change to the miss
bound. All halted
histories execute only inert fixed-loop predicates thereafter.

## 5. Uniform random-time search with known-work fixed-point boosting

For a fixed classical record/pivot history let f(x) be the contender predicate
on K addresses, invalid addresses false. A KNOWN unitary U_f starts from zero
search work: Hadamards prepare uniform candidate and uniform iteration clock
j in{0,...,M-1}, M=2^(ceil(n/2)+2). Apply j ordinary Grover iterations,
controlled by clock bits (emit2^ell iterations for bit ell), then compute a
validity bit f(x). Source records/history are READ-ONLY controls in this circuit.

If a=|S|/K, sin²theta=a, conditional success is sin²((2j+1)theta). Its uniform
clock average is

    1/2-sin(4Mtheta)/[4M sin(2theta)] >=1/4                  (4)

for every0<|S|<K, since M>=4sqrtK and sin(2theta)>=sqrt(2/K).
The endpoints a0/a1 give success0/1. Within each clock branch every marked
candidate has the same amplitude. Thus the normalized good output has an
EXACTLY uniform candidate marginal. The clock and validity registers are
retained; all Boolean predicate helpers uncompute exactly.

Let z=exp(i pi/3). Use a selective phase z on the known all-zero SEARCH WORK
and a selective phase z on the good validity subspace. Define recursively

    U_(ell+1)=U_ell R_zero U_ell^dagger R_good U_ell,
    U_0=U_f.

These are known circuit inverses, not source inverses. For each fixed read-only
data block let p be U_ell's success and q=1-p. On the two-dimensional span of
its normalized good/bad components, the new bad amplitude is the old one
times z+p(z-1)²=z q, since(z-1)²=-z. Therefore failure becomes EXACTLY q³,
while the normalized good vector is unchanged up to phase. Conditional marked
indices stay uniform. This works with arbitrary read-only data in superposition
because the circuits and work-zero reflection are block diagonal in that data;
no reflection about the unknown data state is provided.

Take k least with3^k>=4(40+ceil(log2J)). Since(3/4)^4<1/2, the ideal failure
after boosting is at most epsilon=2^-40/J. The number of base U_f/U_fdagger
calls is3^k=O(logn); all reuse the SAME O(n) logical search work. The phase
recursion requires no trial/result register per repetition.

After boosting compute a FRESH exact verified bit f(x), rather than trusting
the amplifier validity bit that approximate phase gates can perturb. Save
this bit, the pivot when valid, and all O(n) logical search work for this
stage. Do not measure/reset source-dependent work. Across J=O(n) stages this
uses O(n²) retained bits. Boolean arithmetic helpers are reusable and return
zero for ALL candidate/data words and arbitrary XOR-output target values.

Analyze ideal phases first. Couple this finite process to the ideal uniform
pivot process, using its uniform pivot when a boosted call succeeds. Each
nonempty set has false-empty probability<=epsilon, so the total discrepancy
is<=J epsilon=2^-40. Do NOT condition on successful caps and then assume the
pivots remain unbiased. Empty-set verified flags are0 exactly in the ideal
process; wrong-path outputs remain total under fixed public caps.

## 6. Paid phase approximation and invariant implementation work

The pi/3 phases above are NOT exact Clifford+T primitives. Compute the desired
Boolean predicate into a phase target, apply a finite Clifford+T approximation
to Rz(pi/3), and uncompute. This gives the selective phase up to a GLOBAL phase
independent of data. All loops execute unconditionally; active/halted bits are
predicate inputs, so a skipped branch does not silently omit that global phase.
Actual known inverses use the inverse of the actual gate word, not a different
approximation.

Reserve phase targets separately from exact Boolean arithmetic helpers. Ideal
phase compute/rotate/uncompute leaves its implementation work zero for EVERY
logical word. Actual approximation may leave a phase target dirty; retain and
count it. Never reuse it as an assumed-clean arithmetic helper. AND-chain
scratch itself clears independently of the phase target, which is never used
to control its compute/uncompute. The ideal proof stays in the invariant clean
phase-work subspace. For actual gates, compare full physical gadgets with their
ideal full-unitary extensions by operator norm; the usual telescoping norm
hybrid includes leakage. No claim that actual phase helpers remain exactly0
is needed.

The good phase acts on the current stage's logical validity bit. The work-zero
phase has a separate target initialized0 for that stage and retained afterward,
even if imperfect. Exact pi marking in base Grover uses a target touched only
by compute/Z/uncompute, which stays exactly0. Boolean score/AND arithmetic
uses separate clean scratch. Source QFT phases use the unconditional
three-word/CNOT construction above. The final verified membership bit is fresh
and is never rotated. Over all stages this adds O(n) phase/verification bits;
a leaked approximate-phase target is never treated as clean arithmetic work.

Let P_ph be the public number of pi/3 phase occurrences in the forward selector,
O(n logn). Approximate each to error<=2^-40/(P_ph+1), up to its data-independent
global phase. The complete selector differs from the ideal one by norm<2^-40.
Thus this changes output probabilities by<2^-30 with ample slack. The same
style of approximation supplies the public inverse-QFT budget in section2.

The following standard short-word argument and explicit finite search account
for public gate generation. This is a uniform existence/resource construction with charged finite search.

**Short words, up to a common global phase.** H,T generate a dense projective
SU(2) group: Rz(pi/4)Rx(pi/4) has trace1+1/sqrt2, not an algebraic integer,
so its angle is irrational in pi. Conjugation gives a second nonparallel
rotation axis; their infinitesimal generators and commutator span su(2).
Compactness gives a finite epsilon0-net of words, with constant maximum length.
For ||Delta-I||<=epsilon, balanced rotations V,W have
Delta=VWVdagWdag and ||V-I||,||W-I||<=2sqrt(epsilon). Indeed the X/Y
commutator has trace2(1-2sin^4(phi)); choose sin²phi=|sin(theta/2)| for
Delta's eigenangle theta, then conjugate its axis. Replacing V,W by unitary epsilon-approximations V',W' changes the
commutator by at most

    2epsilon(||V-I||+||W-I||)+18epsilon²<=10epsilon^(3/2),

for epsilon<=10^-4. To see this, write
VWVdagWdag=I+[V,W]VdagWdag. The change in [V,W] is at most
2epsilon(||V-I||+||W-I||)+2epsilon²; the change in VdagWdag is
at most2epsilon, while ||[V,W]||<=2||V-I||||W-I||<=8epsilon.
These inequalities give the displayed bound. Correct
the residual U U0dag by this commutator and then apply U0. Consequently
epsilon_next<=10epsilon^(3/2), length_next<=5length. Choose epsilon0<10^-4;
iteration gives word length O(log^4(1/error)), since log_(3/2)5<4. Inverse
letters cost a constant factor (Tdagger=7T). All net constants are absolute.

For clarity, the non-integrality assertion above follows from the irreducible
minimal polynomial2x²-4x+1 of1+1/sqrt2; a rational-angle unitary would have
root-of-unity eigenvalues and algebraic-integer trace. Two nonparallel full
rotation circles generate SU(2): the corresponding Pauli axes and their cross
product span its tangent space, hence give an open subgroup of the connected
group. The balanced-commutator formula follows by multiplying
(cosphi I+i sinphi X) and(cosphi I+i sinphi Y) and their inverses. No desired
source state or source gate is used in this argument. It is the familiar
Solovay–Kitaev existence proof, stated here for the exact gate set needed.

An executable uniform generator need not compute that commutator recursion.
Enumerate H/T words in increasing length, evaluating2-by-2 matrices with
certified dyadic intervals. For desired one-qubit phase V, use

    min_alpha ||U-exp(i alpha)V||_F²=4-2|tr(Udag V)|.

Accept a word only when the interval lower bound on the trace modulus
certifies a Frobenius distance<=error; operator distance is then also bounded.
At length l, precision O(log((l+1)/error²)) suffices to make the total interval
uncertainty<error²/100. A word approximating to error/10 exists by the lemma,
so the conservative certificate eventually accepts without an undecidable
equality test. Target phases pi/3 and pi/2^j have uniformly computable interval
entries: square roots/integer arithmetic for pi/3, or Machin's arctangent
series and bounded sine/cosine Taylor series for dyadic phases. Tiny phases
can be certified against identity. These are counted bit operations, not
real-number unit-cost primitives.

Use a norm-stable enclosure, not repeated rectangular interval products.
Store a rounded dyadic matrix center C_j and a certified operator-error radius
r_j. For an exact unitary letter G, a dyadic approximation Ghat with error<=u,
and product rounding error<=u, set C_(j+1)=round(Ghat C_j). Since
||C_j||<=1+r_j, its radius obeys

    r_(j+1)<=(1+u)r_j+2u.

When lu<=1/2, the explicit radius4ju bounds every prefix j<=l. Choose
u<=error²/[10^5(l+1)] and round each fixed-size matrix entry to sufficient
dyadic precision. This is O(log((l+1)/error²)) bits. Target-entry radii and
trace/modulus rounding are allocated the same error²/100 slack. Integer
square-root enclosures give certified modulus bounds. Thus interval wrapping
does not cause an exponential loss of precision; only one center and radius
and the current word are retained.

Every accuracy used here is inverse polynomial in n times an absolute fixed
constant. Thus l=O(log^4(n+2)), enumeration costs2^O(log^4(n+2)) bit work and
uses polylog(n+2) memory. The latter is O(n²), and the former is
o(2^(n/2)); its finite-prefix cost is absorbed by an absolute outside constant.
Generate at most O(n) public phase words and keep them, or regenerate them
before use. Their stored descriptions also fit O(n polylogn)=O(n²). They are
generated by charged startup computation, not preloaded instance advice.
No word is synthesized from source-dependent data. 

## 7. Coarse success, known undo, and same-bank endpoint decision

Combining(3), the2^-24 ideal pivot miss,2^-40 false-empty coupling and the
phase approximation budget gives coarse failure<2^-18. On the good-score
event the true class is recovered regardless of all wrong-class edges.
Conceptually measured records/pivots have the stated law because their saved
computational contents are never changed by later gates. The ideal-phase
process has this property; actual phase deviations are covered by the norm
hybrid. Classical axis choices are retained independently of the input bank.

For the actual known unitary U of record/selector computation, copy only the
coarse answer and apply Udagger, never inverting source preparation. On any
purification, copying a correct fixed answer with probability1-e gives squared
vector distance2e from that answer tensor the unchanged bank/work, because
the conjugated answer projectors are orthogonal and complete. Average over
private axes, or purify their independent classical mixture. Thus bank plus
coarse class is within trace distance sqrt(2*2^-18)<1/256 of the original bank
and correct deterministic class. Retain/count residual old work and use fresh
binary helpers. This is unconditional, not conditioning on accurate records.

At odd N return the singleton. At even N subtract its canonical p on row1.
Ideal honest states become rho0 or rho_h,h=N/2. Probe the known position
involution add h moduloN (identity on padding), with sign bit v, then measure
the row in X with bit a. Trit C is v0, L is v1,a0, U is v1,a1. On rho0 the
probabilities C/L are1/2 each and U0; on rho_h C/U are1/2 each and L0, since
the valid +/- position eigenspaces have equal rankN/2.

On the ORIGINAL IDEAL comparison bank, at most r false trits occur on EVERY
branch. The actual gently disturbed bank is handled only by trace-distance
contraction; no exact false-count cap is asserted there. Independent good copies supply
a correct count dominating Bin(g,1/2),g>=2r. Return p if L>r, else p+h if U>r,
else a fair coin; give L priority if both exceed on an erroneous coarse branch.
Reference success is at least

    1/2+(1/2)Pr[Bin(2r,1/2)>r]
      =3/4-(1/4)binom(2r,r)/4^r>=23/32.

Here r>=64, and the central-binomial ratio<=1/sqrt(r+1)<1/8 follows by induction
with ratio(2r+1)/(2r+2). Subtracting the gentle1/256 gives>=183/256>11/16.
N2 skips all coarse work and uses this decision atQ192,r64. Fair coins and
all trit measurements have exact H/computational-basis implementations. Known
modular subtraction/involutions have clean valid-range arithmetic on all words.

## 8. Joint gates, addresses and peak storage

The retained Q(n+1) source bank, Q one-pass O(n)-bit label/QPE work, row bits
and O(n) private classical axes use O(n²) qubits and O(n) classical bits.
Each of J stages retains O(n) search/clock/verification/pivot bits. A fixed
number of shared O(n²) exact arithmetic helpers and O(n) phase-AND helpers
fit the same S_Q bound, including actual dirty phase targets. Fresh binary
probes/counters after coarse undo add O(Q+n²). Peak S_Q=O(n²).

For one record and pair, compute k v moduloN by schoolbook reversible product
and division in O(n²) gates and O(n²) scratch. Trigonometric outputs require
only CONSTANT absolute precision: truncate the fraction to a fixed number of
bits, use a fixed-degree fixed-point Taylor routine and clamp, with a rigorous
1/2048 error budget. Its precision/degree constants do not grow with n. Use dyadic sine/cosine outputs with denominator D0=2^20; store each h
component numerator with the common denominator20D0, retaining the division
by20 symbolically. Clamp numerators at+/-20D0. Scores and their sums then
use exact integer arithmetic, with no unbudgeted second rounding of h. Signed
score sums need O(logQ) bits beyond this fixed scale. Compute each term, add
to the sum, and uncompute the term; after copying the sum's sign, reverse the
record scan. Each edge costs O(Qn²)=O(n³) gates, constant-size class comparison
requires at most four edges. Membership scans J pivots with O(n) Boolean flags,
copying its AND and uncomputing everything. Its cost is O(n^4) gates, with
shared O(n²) workspace, not stored O(n^4) computation history.

For a fixed finite trigonometric recipe, compute r=floor(2^32 z/N)/2^32 from
z=k v modN. Generate pi64 by rounding16atan(1/5)-4atan(1/239) to64 fractional
bits, using40 alternating terms per arctangent. Their tail is<2^-100; pi's
error is<2^-64. Set x=2pi64*r. Then x<7 and its angular error is<2^-29.
Use the degree64 cosine and degree63 sine Taylor polynomials: remainders are
at most7^65/65! and7^64/64!, both<2^-100. Generate factorial coefficients to
1024 fractional bits and use Horner arithmetic with1024 fractional bits,
rounding each operation. Even bounding amplification by64*8^64 gives arithmetic
error<2^-800; a fixed256-bit integer part suffices. Final20-bit rounding adds
<=2^-21, so the total is<1/2048. Every width/degree here is an absolute
constant. Charge their finite generation and the fixed evaluation history
needed for reversible compute/copy/uncompute. These are not real-number
oracles; the n-dependent product/division costs remain O(n²).

U_f costs O(M n^4) gates. Fixed-point boosting multiplies by O(logn), J stages
by O(n); global undo doubles the result. This is O(2^(n/2)n^5 logn) gates plus
polynomial source/phase preparation. A deterministic streaming generator uses
O(n²) classical bits for public bounds/counters, private axes, wire addresses
and local arithmetic templates. It stores no gate list of length M, score
table or selected-candidate RAM. Each bit operation and indexed access is
charged. An intentionally loose O(n³) generation/address allowance per gate
fits T=O(2^(n/2)n^10), with margin for logn and the subexponential-in-n public
phase compiler. Public source count Q and all cutoffs are generated by counted
arithmetic. Tdagger is7 literal T, Toffoli33 literal gates/25 T. No quantum-
addressed memory is supplied: every shadow/pivot scan is explicit.

For completeness, the clean-arithmetic gates above have the following uniform
construction. Ripple-carry addition and unsigned comparison have O(n)-size
Boolean DAGs. Schoolbook product adds n shifted rows; restoring division of a
2n-bit numerator performs 2n shift/compare/subtract steps on O(n)-bit words.
Both therefore have O(n²)-size DAGs. For division reduce the numerator modulo
the positive public N; leading zero bits and overflow widths are included.
All their bit loops have public bounds. Generate each DAG locally from wire
indices rather than retain a global gate list.

For an XOR-output function y<-y XOR f(x), store the intermediate Boolean DAG
values in fresh bits, CNOT its output into y, then reverse the DAG. For each
fresh zero target z, implement NOT(a) by X(z),CX(a,z); XOR(a,b) by
CX(a,z),CX(b,z); and AND(a,b) by CCX(a,b,z) when a and b are distinct wires.
For repeated-input AND(a,a), use CX(a,z); repeated XOR cancels. Constants
use no gate or X(z). The scratch returns to zero for EVERY
x and every initial y. A size-L DAG thus costs O(L) gates and O(L) scratch;
schoolbook arithmetic gives the claimed O(n²) bounds. Reuse that same scratch
after each compute/copy/uncompute, including on superpositions and padding.

A known permutation f on all declared words is implemented in place by
(x,0)->(x,f(x)), swapping these registers, and XOR-evaluating f^(-1) into the
second register: (f(x),x)->(f(x),0). Controlled versions use the same full
permutation with the control among the unchanged operands. The guarded
translation f_v adds v moduloN only to valid words in the selected row and
fixes every other word; its inverse is f_(-v). The arithmetic first computes
validity, so the complete declared padded domain is a permutation. No copy
or inverse of a source-preparation circuit is used.

One exact Toffoli on controls a,b and target c is the ordered word

    H(c), CX(b,c), Tdag(c), CX(a,c), T(c), CX(b,c), Tdag(c),
    CX(a,c), T(b), T(c), H(c), CX(a,b), T(a), Tdag(b), CX(a,b).

Checking its eight computational basis inputs gives the phase-free Toffoli;
equivalently use the parity phase identity
4abc=a+b+c-(a XOR b)-(a XOR c)-(b XOR c)+(a XOR b XOR c).
Expanding each Tdag as seven T gives 33 literal gates, including 25 T gates.
This also compiles all Boolean DAGs into the stated gate set.

The forward gate stream and its inverse have public schedules. Retain private
axes and generated public phase words. Reverse per-copy record, score
and pivot loops by descending public counters, and invert the ACTUAL letters
(H/CX/CCX self-inverse; T inverse is7T). Emit fixed-point recursion from its
level/direction syntax, reversing subcalls for its inverse; depth is
O(loglog(n+2)). Arithmetic templates emit local bit loops without saved gate
lists. Controlled base Grover uses exact compute/CZ/uncompute marking and
unconditional outer Hadamards for diffusion; its controlled global minus is
Z on the clock control. No controlled-H or controlled synthesized word is
needed. The public2^ell repeat loop is counted in full even when its clock
bit is0. Stack frames, cursors, addresses and phase descriptions fit O(n²)
classical bits and supply the exact known inverse after coarse copying.

All loops have public fixed bounds, and the resource bounds hold on every
execution branch, including erroneous class and verification outcomes.


## 9. Prior work and comparison context

The error-model specification in Section 0 and the fifth structured claim is
reproduced verbatim from the published ROB submission
d0c6b9b9-d80e-4bd7-95e1-e6267b61f2f0, by kshitij-hash. This fixes identical
parameter meanings and corruption assumptions for fractional comparison.
Only the comparison-model wording is reused from ROB; no ROB algorithm,
correctness lemma or resource proof is used.

The known reflection-testing and retained-register search framework has prior
in the DEV-era RGRST1 result, Layr-Labs/dcp pull request 54:
https://github.com/Layr-Labs/dcp/pull/54 . That work has no production submission
identifier on this track. Every lemma needed here is proved above; no external
document is needed to check correctness or the joint resource bounds.
