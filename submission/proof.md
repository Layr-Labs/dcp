# One-third tolerance under a clean-marginal bank promise

## 0. Joint theorem, algorithm and source model

For every integer N>=2 and every secret s in Z/NZ put n=ceil(log2 N), K=2^n.
The algorithm below acquires exactly Q=192 copies when N=2 and exactly
Q=27648(2n+20) copies when N>=3. Put r=Q/3. Under the following error model,
with epsilon(n)=1/3, it outputs the entire s with unconditional probability
at least 11/16>2/3. On every execution branch the SAME algorithm and parameter
rule jointly satisfy

    T=O(2^(n/2)n^5 (log2(n+2))^4), S_C=O(n), S_Q=O(n^2), Q=O(n).

All constants are absolute and independent of N, s, the bank state and outcomes.
These are full worst-case bounds in the uniform Clifford+T/bit-operation model,
including source acquisition, gate generation, precision, initialization,
measurements and address charges. The four envelope growth indices are 1,0,0,0.
For n>=2, log2(n+2) is within a fixed factor of log2 n. The supported
eventual time envelope is 2^(n/2)n^5(log2 n)^4. Its base-2 logarithm is
n/2+5log2 n+4log2(log2 n), with double-logarithmic growth index 1.
The classical-space, quantum-space and sample envelopes are n, n^2 and n,
with index 0. The n=1 case is N=2 and uses a fixed-size exact trit circuit.
The fifth expression is the constant fraction 1/3, with no validity threshold.

### Error model: clean marginal, arbitrary joint extension

The algorithm first acquires all Q raw registers, each consisting of one row
qubit and n position qubits. No measurement, private random draw, source
transformation or abort occurs before the last register arrives. Write

    rho_s=(1/N) sum_(x=0)^(N-1) |psi_(x,s)><psi_(x,s)|,
    |psi_(x,s)>=(|0,x>+|1,(x+s) mod N>)/sqrt(2).

The exact structured error-model text is:

"Among the Q acquired copies, an adversary fixes a set B of at most floor(epsilon(n) Q) malformed positions, possibly depending on N and s. The joint state is arbitrary subject to its reduced state on all other positions being exactly rho_s^{tensor (Q-|B|)}. Malformed systems may be correlated or entangled with each other and with other systems subject to that marginal promise. No source control, purification access, or preparation inverse is supplied."

Here epsilon(n)=1/3 and floor(epsilon(n) Q)=r. For each input component
sigma, let G be the complementary set to its fixed unknown B. The promise is

    Tr_B sigma = rho_s^(tensor G).

The joint extension on B is arbitrary. It may depend on N,s,B and may be
entangled with G and with an inaccessible reference. Malformed positions
may have any states on their declared n+1 qubits, including padded position
words. The algorithm is not given B and does not need to find it. The source
has no access to the bank or workspace after acquisition. The guarantee also
holds for every convex mixture of these input components with different B.
The bound is on the number of malformed positions, not a per-copy probability.

For every N>=2, every s, and every such input, the algorithm has the success
and four resource bounds stated above. Its fraction is exactly epsilon=1/3:
floor(epsilon Q)=r. The clean problem is the special case B empty. This is a
batch input promise; it does not specify an interactive replacement service.

### Lemma 0: reduction to a fixed malformed set for analysis

It is enough to prove success uniformly for each fixed B and each state sigma
with the stated marginal. A complete algorithm induces a linear probability
functional on its input density operator. Thus a uniform lower bound for all
components also holds for their convex mixtures. Resource bounds below hold
on every branch and are independent of the decomposition. The proof may use
an arbitrary purification of sigma, but the algorithm cannot access it.

The bank uses Q(n+1) qubits and Q(n+1) source work units. All copies are kept
through the coarse computation and its actual known inverse. The marginal
promise does not imply independence between G and B. No step below uses that
stronger assumption. The good-first record order in Section 3 is for the proof
only, and does not give the algorithm B.

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

Fix B for the proof. Local record instruments on different slots commute.
To analyze their common outcome law, reveal all G records first, then the
B records. This order is only a proof device; the algorithm need not know B.
A private axis can be drawn when its local instrument is reached in this
order. Local operations and independent private coins give the same joint
record law as the implemented order. In particular, future bad axes remain
independent of the history.

The G records are independent with the clean local law: their joint law is
computed from the marginal rho_s^(tensor G). After they are revealed, the B
block can be arbitrarily steered. At each subsequent bad slot its conditional
state is arbitrary, so the operator bound (2) still applies.

Consider an oriented comparison with t=s and u outside the true class.
Let k=Q, g=|G|, b=|B|. In the good-first order, let mu_i be the score mean
conditional on all preceding records. Every good slot has
mu_i >=11/20-beta. Every later bad slot has mu_i >=-1-beta. Thus on every
history the sum of these conditional means is at least

    g(11/20-beta)-b(1+beta)
      >= k(1/30-beta) = 29k/960.

This uses g=k-b and b<=k/3. The centered increments D_i=Z_i-mu_i have
conditional mean zero and interval width 4. The conditional Hoeffding lemma
therefore gives E[exp(lambda D_i) | history] <= exp(2lambda^2).
For completeness, if a centered X lies in an interval of width w, convexity
bounds its exponential moment by that of the two endpoint values with the
same mean. Write p=-a/w for the lower endpoint a. The logarithm of this
endpoint moment, as a function of h=lambda*w, is
psi(h)=-p*h+log(1-p+p*exp(h)). It has psi(0)=psi'(0)=0 and
psi''(h)=q(1-q)<=1/4. Hence psi(h)<=h^2/8 for either sign of h.
Apply this argument conditionally with w=4. The endpoints may depend on
the preceding records; the bound is uniform in them.
Iterating over all k slots and applying Markov's inequality gives

    Pr[sum_i D_i <= -delta*k] <= exp(-delta^2*k/8).

Take delta=1/48. Then the failure bound is exp(-k/18432), and outside
that event the oriented score is at least

    k(29/960-1/48) = 3k/320 > 0.

For a comparison t outside the true class and u=s, reverse the inequalities
and use the upper tail to get a score at most -3k/320. This single martingale
covers both the independent good records and the conditional bad records.

Only comparisons involving s need these signs. There are fewer than K^2
such oriented comparisons, K=2^n, for N>=3. A conservative union bound is

    failure <= 2 K^2 exp(-k/18432)
            <= 2 K^2 exp(-(2n+20)) <= 2^-19.                 (3)

Here k=Q=27648(2n+20), and 27648/18432=3/2.

No claim is made about the orientation of two false candidates. The proof
does not condition on an algorithm success event and then assert that good
copies remain independent.


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
constant. Thus the word length is O(log^4(n+2)), each enumeration costs
2^O(log^4(n+2)) bit work, and its scratch is polylogarithmic in n+2.
Choose deterministic regeneration: fix a total word order, arithmetic
precision rule and acceptance certificate. At each public phase occurrence,
generate one word, emit it, then release its scratch. Keep no phase-word table.
To invert a word, regenerate the same forward word and reverse its actual
letters. No word is synthesized from source-dependent data.

Only polynomially many phase occurrences need this compiler. They occur in
one-pass QPE and its undo, and in the fixed-point boost; none occurs inside
the exponentially repeated exact Grover iterations. Section 8 counts this
additive compiler work and proves the O(n) classical-space bound. All words
are generated by charged computation, not supplied as instance advice.

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

On the ORIGINAL comparison bank, at most r false trits occur on EVERY
branch. The actual gently disturbed bank is handled only by trace-distance
contraction; no exact false-count cap is asserted there. The original good
marginal gives independent good trits and supplies
a correct count dominating Bin(g,1/2),g>=2r. This law follows from
Tr_B sigma=rho_s^(tensor G), even if bad and good slots are entangled.
Return p if L>r, else p+h if U>r,
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

Put L=log2(n+2), J=n+24 and M=2^(ceil(n/2)+2). Let A_boost be the
number of base search calls in one fixed-point boost. Section 5 gives
A_boost=O(L) and recursion depth O(log L). All counts include the final
known undo and apply on every branch, including erroneous selector branches.

The retained Q(n+1) source bank, Q one-pass O(n)-bit label/QPE work, row bits
and O(n) private classical axes use O(n²) qubits and O(n) classical bits.
Each of J stages retains O(n) search/clock/verification/pivot bits. A fixed
number of shared O(n²) exact arithmetic helpers and O(n) phase-AND helpers
fit the same S_Q bound, including actual dirty phase targets. Fresh binary
probes/counters after coarse undo add O(Q+n²). Peak S_Q=O(n²).

### 8.1 Scores and exact Boolean circuits

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

### 8.2 Number of repeated main gates

The base search emits at most M ordinary Grover iterations. Its marking,
diffusion, clock controls, Boolean arithmetic, and exact Toffoli
decompositions contain no approximate one-qubit word. The clock-controlled
implementation uses exact compute/CZ/uncompute and unconditional outer
Hadamards, as specified in Section 5.

Across all pivots, boosting, and the final known undo, the number of
these main gates is therefore

    G_main = O(J A_boost M n^4)
           = O(2^(n/2) n^5 L).                            (W1)

The only approximate phase sites are the one-pass QPE preparation and
its undo, plus the fixed-point boost gadgets. QPE has O(n^3) such sites
over the bank. The boost has O(nL) pi/3 sites. These counts are
polynomial. In particular, the phase compiler is not called once per
exponentially repeated Grover gate.

### 8.3 Address generation

Use one fixed public layout for the quantum bank, records, retained
stage work, and shared arithmetic scratch. It has O(n^2) wires.
The classical storage established below has O(n) bits. Consequently
every charged address has O(L) bits.

The layout consists of consecutive arrays with public lengths bounded
by fixed polynomials in n. A record wire has the form

    base + copy_index * record_width + bit_index.

Pivot wires and arithmetic-DAG wires have the same type of formula,
with a fixed number of public row and column indices. The schoolbook
product, restoring division, ripple adders, and their reversals have
fixed-depth loop descriptions. A gate is generated from these indices;
the generator does not retain the Boolean DAG or simulate its quantum
values.

Each gate address can therefore be computed with a constant number of
additions, multiplications, comparisons, and bit extractions on O(L)-bit
public integers. Schoolbook integer arithmetic costs O(L^2) bit operations.
Charging O(L) for each indexed bit access gives the conservative bound

    O(L^3) classical work per emitted main gate.           (W2)

The physical gate address charge is only O(L) and is covered by (W2).
The finite Toffoli expansion changes this bound by a fixed factor.
An input bit of the public modulus N is read by its O(L)-bit index;
the generator does not perform a new n-bit arithmetic operation for
each emitted gate. Candidate, label, and pivot arithmetic is already
inside the quantum circuit counted in (W1).

### 8.4 Long repeat counters

The Grover clock loop emits `2^ell` complete iterations for clock bit
ell. Its repeat counter can have O(n) bits. It is used to start, finish,
and count whole Grover iterations; its value is not used to compute
the addresses of every arithmetic gate within an iteration.

There are

    I_main = O(J A_boost M) = O(2^(n/2) n L)

such iteration macros. Even a worst-case O(n)-bit increment, comparison,
or reset, with O(L) indexed-access cost per bit, contributes only

    O(I_main n L) = O(2^(n/2) n^2 L^2).                   (W3)

This is below (W1) times (W2). An amortized constant-time counter is not
assumed. Only one long repeat counter is live at a base-search leaf.
The fixed-point recursion retains a level, a branch cursor, and a
direction flag in each of O(log L) frames. It does not retain a second
long repeat counter at every recursive level.

### 8.5 Additive phase compilation

The certified word search in Section 6 has word length O(L^4), work
`2^O(L^4)`, and polylogarithmic memory at every required precision.
The required errors are inverse polynomial in n: the QFT error per
word is proportional to `(n+19)^(-2)`, and the pi/3 error is proportional
to `1/(P_ph+1)` with `P_ph=O(nL)`. No exponentially small word error is
requested by the search loop.

For each public phase occurrence, regenerate its deterministic word,
emit it, and release the compiler scratch. Keep only that word and its
cursor while it is emitted. There are polynomially many such occurrences,
so the total compilation and emission cost is still

    2^O(L^4),                                            (W4)

plus polynomial overhead. Since `L^4=o(n)`, (W4) is
`o(2^(n/2))`. It is additive to the main work, not a factor multiplying
every gate in (W1). The finitely many smaller n are covered by an absolute
outer constant.

Large dyadic phase indices do not require an n-bit-precision matrix.
Once the phase magnitude is below the assigned word error, the
certificate can accept identity using its explicit magnitude bound.
The remaining target entries require O(L) precision. No table of O(n)
phase words is retained.

### 8.6 Constant regeneration and the actual inverse

For QPE, keep one n-bit modular-shift constant at a time. It can be
generated by repeated doubling modulo N. Recompute it from its public
index when a reverse loop needs it. The O(n) possible shift constants
are never stored together. This work occurs only in polynomially many
QPE preparation and undo steps and is covered by (W4) and a polynomial.

Fix a total order on candidate words and the interval arithmetic used
by the compiler. Its input is the public phase identifier, its assigned
error, and n. Deterministic regeneration returns exactly the same
literal word. To emit an inverse, regenerate the forward word, read
its letters in reverse, and invert each actual letter. Do not compile
a new approximation to the negative target angle. Inverse T is seven
literal T gates; the other elementary letters have the exact inverses
specified above.

Public loop counters run downward for the reverse record, score,
membership, pivot, and repeat schedules. Fixed-point subcalls reverse
their order and direction. Thus this controller emits the exact inverse
of the actual forward physical circuit, including its common global
phases and any approximate phase-helper leakage. It requires no saved
gate stream and no source inverse.

### 8.7 Peak classical storage

The live classical registers are the n-bit public modulus, O(n) private
axis bits, a constant number of n-bit public values or long counters,
the final measured class, O(L)-bit local template indices, the small
fixed-point recursion stack, and one current compiler word with its
polylogarithmic scratch. Their total is

    O(n + polylog(n+2)) = O(n).                           (W5)

The O(n) retained pivots, each of n bits, are quantum data. So are the
QPE labels, source-dependent signs, search clocks, validity flags, and
coherent branch history. The phrase 'fixed record/pivot history' in the
search analysis does not turn them into a classical stored table.
No source-dependent value is copied into classical memory during the
coherent selector.

After the coarse answer is copied and the actual circuit is undone,
measuring its n-bit class and keeping endpoint counts uses O(n) further
classical bits. The old private axes remain stored through undo.
Fixed trigonometric constants and their finite generation have an
absolute fixed storage cost. The compiler's fixed polylogarithmic
storage is O(n), with a larger absolute constant if needed for small n.

The quantum allocations are those counted at the start of Section 8.
No classical data are hidden in additional qubits, and no quantum-addressed
memory is assumed.

### 8.8 Total work

Multiplying G_main in (W1) by the per-gate work in (W2), then adding the
macro-counter cost (W3), compiler cost (W4), source acquisition, initialization,
measurements and polynomial startup gives

    T=O(2^(n/2)n^5 L^4),  S_C=O(n),  S_Q=O(n^2),  Q=O(n).

Every parameter is computed by counted arithmetic. No phase compiler runs
per exponentially repeated arithmetic gate. No gate stream or exponential
score table is stored. All loops have fixed public limits. The controller
uses public parameters and retained private axes, so the bounds hold on every
execution branch for every state in the promised model. For N=2 all bounds
are covered by its fixed-size exact endpoint computation.

## 9. Attribution and scope

The circuit, cubic witness, QND recording, class tournament, bounded coherent
selector, phase compiler, known undo and endpoint decision are taken from
the prior submission
`f892f7ea-957b-4dde-8374-dab2736231d0`, evaluated at commit
`3f9e53c2a129e9ff95b5d1754dcd5587331fbcf1`. The exact source is
[submission/proof.md](https://github.com/Layr-Labs/dcp/blob/3f9e53c2a129e9ff95b5d1754dcd5587331fbcf1/submission/proof.md),
SHA-256 `c492a4f842e114110805b2de648d1004b12f0367ddbaa9fee8dcb5f3fdf66379`.
That source was read and its circuit is reproduced above so this proof does
not require an external algorithm oracle. Exact one-third tolerance is prior
work under that source's input model.

The good-first proof order and martingale in Section 3 extend that circuit
to the clean-marginal promise. Sections 6 and 8 choose one-word compiler
regeneration and give the complete controller cost and storage proof for the
resource bounds stated here. No tolerance above one third is claimed. These
historical statements are outside the atomic resource and tolerance
guarantees in Section 0.

RWT25, submission `3f48c893-2d1b-4e9b-ac9e-e9d318149910`, already gives
one-quarter tolerance under the same clean-marginal promise, including
arbitrary correlations with malformed systems. Its
[exact proof](https://github.com/Layr-Labs/dcp/blob/dd6041a0fc1cfe8c29b2af14c5ffc7b29b18ee75/submission/proof.md)
has SHA-256 `6e83a34c0c2283f0acbfab9bf523accebec2cdf4f81b2eb5f32706224d78fd47`.
Thus the bank model itself is prior work. The result here raises tolerance
from one quarter to one third under that promise, using the circuit credited
above. RWT25 was first read after this standalone proof was complete. Its
exact structured error-model wording is now reused in Section 0 and credited
here. It also supplies comparison evidence. Its algorithm was not used to
derive this construction.

The prior source credits the reflection-testing and retained-register search
framework to DEV-era RGRST1, [Layr-Labs/dcp pull request 54](https://github.com/Layr-Labs/dcp/pull/54).
This file makes no priority claim for that framework. No result from that
pull request is needed to verify the construction reproduced here.

## 10. Separate bank-state model comparison

This comparison is for the bank-first schedule used by both algorithms.
It is not an inclusion claim about arbitrary interactive source services.

The prior model's exact clean-delivery clause is: "in tensor product with
everything else (the adversary's system, all other copies and the algorithm's
workspace)". Thus the adversary cannot retain a purification of a clean
delivery and emit its other part later. Bank-first acquisition alone would
not imply the claimed reduction without this independence clause.

Let A_m be the convex hull of all prior fixed-position banks
rho_s^(tensor G) tensor tau_B with |B|<=m. Let M_m be the convex hull of the
marginal-promise banks in Section 0, with Q=k=3m. The cited prior bank-first lemma gives A_m as
the set of banks allowed by its adaptive source model for this schedule:
one inclusion is that lemma; the other follows by choosing the set B and
its joint bad state privately in advance. Directly, A_m is a subset of M_m.

For the reduction, condition on the hidden prefix of clean/bad decisions.
Inductively the unnormalized state is the tensor product of rho_s factors
on all clean slots and a positive operator on the bad slots and adversary.
A private adversary instrument acts only on the latter factor. A bad
delivery transfers part of that factor. A clean delivery appends a fresh
independent rho_s by the quoted clause. The bank-first schedule supplies no
algorithm measurement outcome that could break this induction. Summing
private outcomes, tracing out the adversary, and then mixing over the final
sets B gives A_m. This verifies the cited lemma in its actual source model.

The inclusion is strict for N>=2 and m>=1, with k=3m. The ideal rho_s has
rank N with N equal nonzero eigenvalues. Choose a purification |Omega_s>
of rho_s on two raw-register spaces; it has Schmidt rank N and is entangled.
Construct a bank of m disjoint pure pairs |Omega_s>, followed by m independent
rho_s slots. Designate one endpoint of each pair as bad. The other m pair
endpoints and the m independent slots have marginal rho_s^(tensor 2m).
This bank therefore belongs to M_m.

It cannot belong to A_m. In any positive mixture decomposition, the marginal
on each of these pairs is the same pure |Omega_s><Omega_s| in every component
of nonzero weight. This follows since a convex mixture equals a rank-one
projector only if every component has that projector as its marginal. In a
prior component, any endpoint declared good is a rho_s tensor factor, so its
pair marginal is separable. It cannot equal the entangled pure pair. Both
endpoints of every pair must therefore lie in that component's B. This needs
at least 2m bad slots, which violates |B|<=m. Thus the constructed bank is in
M_m minus A_m.

Without convexification, a fixed-B promise need not contain prior mixtures
with different bad sets. The theorem nevertheless applies to those mixtures
by linearity, which is why M_m is the correct bank-state comparison. The
extension permits good-bad entanglement in the supplied bank; it does not
claim that the prior adaptive delivery specification itself already permits
such entanglement.

## 11. Verification status

Two independent agents checked the good-first argument and the strict convex
bank-state inclusion proof. They found no defect within the stated scope.
The proof reviewer also checked that the undo and endpoint arguments use only
the marginal promise. The copied prior circuit was inspected, and its exact
source byte hash was checked before incorporation. A separate compiler and
controller audit was reviewed before its construction was incorporated into
Sections 6 and 8.

Finite checks passed for the rational drift, concentration and success
constants. The cubic witness norm and honest mean were checked for 1,984
non-antipodal differences through N=64. These checks support the algebra;
they do not replace the proof. No upload is made by this file.
