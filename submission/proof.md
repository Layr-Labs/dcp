# One-third adaptive tolerance with an exact global-clock selector

## 0. Joint theorem, algorithm and source model

For every integer N>=2 and every secret s in Z/NZ put n=ceil(log2 N), K=2^n.
The algorithm below acquires exactly Q=192 copies when N=2 and exactly
Q=27648(2n+20) copies when N>=3. Put r=Q/3. Under the following error model,
with epsilon(n)=1/3, it outputs the entire s with unconditional probability
at least 11/16>2/3. On every execution branch the SAME algorithm and parameter
rule jointly satisfy

    T=O(2^(n/2)n^(18/5)), S_C=O(n), S_Q=O(n^2), Q=O(n).

All constants are absolute and independent of N, s, the adversary and outcomes.
These are full worst-case bounds in the uniform Clifford+T/bit-operation model,
including source acquisition, gate generation, precision, initialization,
measurements and address charges. The four envelope growth indices are 1,0,0,0.
Put L=log2(n+2) and p=log2 3. The counted implementation first gives
T=O(2^(n/2)n^(2+p)L^3). Since 3^5=243<256=2^8, p<8/5 and the
strict exponent gap absorbs L^3. The declared supported time envelope is
B_T(n)=2^(n/2)n^(18/5). Its base-2 logarithm is n/2+(18/5)log2 n,
with double-logarithmic growth index 1.
The classical-space, quantum-space and sample envelopes are n, n^2 and n,
with index 0. The n=1 case is N=2 and uses a fixed-size exact trit circuit.
The fifth expression is the constant fraction 1/3, with no validity threshold.
The complete selector proof is in the packaged file
[critical_third_adaptive_clock_selector.md](critical_third_adaptive_clock_selector.md);
its exact clock and stage limits are part of this one algorithm.

### Error model: exact adaptive delivery specification

The declared error-model text is exactly the following specification:

Adaptive malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires, and epsilon(n) the tolerated malformed fraction. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm, and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed; on every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. A malformed copy is an arbitrary (n+1)-qubit state (the register shape of an ideal copy) supplied from the adversary's system: it may be pure or mixed, may be entangled with the adversary's remaining system and with other malformed copies, and may depend on all of the information above; it is not entangled with clean copies or with the algorithm's workspace, ancillas or internal random bits. Every copy that is not malformed is clean: at the moment of its delivery, a fresh ideal coset state rho_s = (1/N) sum_x |psi_{x,s}><psi_{x,s}| in tensor product with everything else (the adversary's system, all other copies and the algorithm's workspace), i.e. clean copies are independent ideal coset states. The adversary interacts with the algorithm only by supplying copies; after delivery it has no access to the copy or to the algorithm's quantum or classical systems. All measurements have countably many outcomes. The algorithm is not told which copies are malformed. Quantifiers: the guarantee must hold for every N >= 2 (no validity threshold), every s in Z/NZ and every such adversary, including the adversary that corrupts nothing (the clean problem): the algorithm outputs the entire s with probability at least 2/3, and the four declared resource bounds hold on every execution branch. The fraction bounds the number of malformed copies among acquired copies; it is not a per-copy corruption probability.

Here epsilon(n)=1/3, r=Q/3 is an integer, and the pathwise malformed-copy
cap is floor(epsilon(n)Q)=r. There is no validity threshold. This fraction
is a bound on the number among all acquired copies, not a per-copy corruption
probability. The clean input is included by an adversary that corrupts nothing.
The source state in this specification is

    rho_s=(1/N) sum_(x=0)^(N-1) |psi_(x,s)><psi_(x,s)|,
    |psi_(x,s)>=(|0,x>+|1,(x+s) mod N>)/sqrt(2).

### Lemma 0: the adaptive model gives a mixture of product banks

The first source operation acquires all Q raw registers in deterministic
order 1,...,Q. Each has one row qubit and n position qubits. The algorithm
makes no measurement, private random draw, source transformation or abort
decision before the last register arrives, also when N=2. Public allocation
and source counters are deterministic. Private axes and all circuit operations
in Sections 1--8, Appendix A and the selector file occur only after this acquisition. The bank uses Q(n+1)
qubits and Q(n+1) source work units.

For this schedule, every allowed adaptive adversary produces a bank density
operator in the convex hull of the product banks

    sigma_B=rho_s^(tensor G) tensor tau_B,
    |B|<=r, G={1,...,Q} minus B,

where tensor factors are placed in their named slots. The density tau_B is
arbitrary on the malformed slots and may have an inaccessible purification.
Both the set B and tau_B may depend on N and s. The algorithm does not know B.

Proof. Add a hidden classical register for each clean/malformed decision.
Conditional on a prefix of decisions, its unnormalized joint operator has
rho_s factors on all already delivered clean slots and a positive operator
on the delivered malformed slots together with the remaining adversary
system. This holds initially. A private adversary instrument acts only on
the latter factor. It can steer earlier malformed slots but cannot change
or correlate any clean tensor factor. A malformed delivery transfers a
subsystem of that factor to the next slot. A clean delivery appends a fresh
rho_s in tensor product with everything else, as the specification requires.
There is no algorithm measurement outcome on which the next decision can
depend. This proves the induction without requiring independence among
malformed deliveries.

At the end, sum the private instrument outcomes and trace out the adversary.
Each sum retains the clean tensor factors. Countably many outcomes are
permitted; the corresponding positive sums converge in trace norm. Then
condition only on the final finite set B and normalize its nonzero weight.
There are finitely many possible sets B. The pathwise cap ensures |B|<=r
for each such component. Any later trace-preserving private operation leaves
the reduced bank state unchanged. Thus the result is the stated convex
mixture. The clean-delivery tensor-product clause is essential here: it
forbids the adversary from retaining a purification of a clean delivery and
later supplying its partner as a malformed copy. Bank-first acquisition alone
would not prove that independence.

Every product-bank component in this reduction has the marginal identity

    Tr_B sigma_B=rho_s^(tensor G).                         (0)

The analysis in Sections 1--8, Appendix A and the selector file is proved for every fixed B and any bank sigma
with identity (0), even if the malformed block has an arbitrary joint
extension. Each component produced above is therefore an allowed case of
that analysis. A complete algorithm is a linear probability functional of
its input density. Its uniform success bound for those components extends
to their convex mixtures. The resource bounds use only fixed public loop
limits and allocations, so they also hold on every branch of every mixture.
No conditioning on the algorithm's later measurement success occurs here.

This proves the adaptive delivery guarantee by reduction to the reproduced
bank analysis. It does not provide access to a purification, source inverse,
or controlled source. The same streaming implementation is used throughout.

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

The contender predicate acts on the fixed candidate wires in active bank 0.
It scans the J archived banks at public addresses and includes a pivot only
when both its completion and verification bits are 1. Invalid candidate
addresses are false. Each edge uses the exact arithmetic in Appendix A;
the predicate is a total XOR-output function, with clean helpers on every
input word. It uses O(n^(2+p)) literal gates and O(n^2) reusable helpers.
No larger read-only input or hidden edge table is supplied.

## 5. Exact global-clock selector

For N>=3, put

    J=n+24, d_clock=ceil(n/2)+32, B_clock=2^d_clock.

The complete selector is specified and proved in
[critical_third_adaptive_clock_selector.md](critical_third_adaptive_clock_selector.md).
Instantiate its K with 2^n, its C with the number of classes above, its
B with B_clock and its d with d_clock. Its predicate is exactly the
contender predicate in Section 4. Allocate J+1 stage banks: one fixed active
bank and J archive slots. Each has an n-bit candidate, d_clock probes,
verification/allocation/completion bits and two (d_clock+2)-bit timestamps.
The completed-stage count has ceil(log2(J+1)) bits.

Run exactly B_clock ticks in public order. Each tick performs the guarded
initialization and probe H instructions, one guarded forward G, one guarded
inverse G, fresh verification and then the total boundary involution. All
ordinary guards and their helpers are cleared before that boundary. The
literal Grover operator is G=(2|v><v|-I)(I-2P_S); its controlled diffusion
marks enabled nonzero candidate words between unconditional H layers.
Conditional H uses V=S H T H S^dagger and V Z V^dagger=H. All these selector
gates are exact Clifford+T.

The boundary uses the explicit A_tau/F_tau/B_tau construction and clean
XOR evaluator in selector Sections 5--6. It preserves every completed
history in full stage banks, uses one O(n^2)-bit temporary array at a time,
and is a total involution even on invalid words. No timestamp or history
bit is overwritten irreversibly. Bank 0 always holds the active candidate;
there is no quantum-addressed choice of one of J active workspaces.

After the final tick, the answer is the rightmost completed verified archive
candidate, or zero if none. An unfinished front bank is ignored. Section 7
performs one copy of that n-bit answer, reverses its computation, then reverses
every literal tick and record preparation. A cap inside a probe, inverse
correction or verification preserves that unfinished state for this inverse.
N=2 skips the selector and uses the endpoint test directly.

For every fixed read-only tournament with its Condorcet winner, the selector
proof gives error below 2^-23. It couples the bounded circuit to the same
uncapped measured history before either cap; it does not assert uniform
pivots after conditioning on cap survival. The proof includes exact uniform
marked outputs, expected winner time below 96sqrt(K), the global clock loss
below 2^-24, and the J-stage loss at most 2^-24. All actual branches still
have exactly B_clock bounded ticks. The argument is applied separately to
each computational record block and then integrated, including coherent
input records.

## 6. Paid QFT phase compilation and exact selector work

The selector uses no approximate selective phase. Its probe H, literal
controlled Grover reflections, verification, guards and boundary circuits
are exact Clifford+T. Exact Boolean helpers return to zero for every
logical input and are separate from source QPE registers.

Only the one-pass record QFT and its actual inverse require approximate
phase words. Section 2 gives their complete per-copy error budget and
unconditional three-word/CNOT controlled-phase construction. All approximate
words act only on QPE ancillas, preserving exact QND block structure. Their
data-independent global phases cause no conditional phase error. The actual
known inverse reverses each actual word; it does not compile a new negative
angle. No phase compiler occurs in the B_clock repeated tick stream.

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
equality test. Target phases pi/2^j have uniformly computable interval
entries from Machin's arctangent series and bounded sine/cosine Taylor series. Tiny phases
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
one-pass QPE and its undo; none occurs inside the exponentially repeated
exact selector ticks. Section 8 counts this
additive compiler work and proves the O(n) classical-space bound. All words
are generated by charged computation, not supplied as instance advice.

## 7. Coarse success, known undo, and same-bank endpoint decision

The score failure bound (3) is at most 2^-19. On its complement the
class tournament has the true Condorcet winner. The selector adds less
than 2^-23=2*2^-24 failure, so coarse failure is below 2^-18, even retaining
an unused 2^-30 error allowance. Source QFT approximation is already
included in the score means and their concentration bound.

The source records are read-only. Stage histories move only by the full
reversible bank permutations. They remain orthogonal and are never merged.
The selector's blockwise deferred-measurement proof therefore gives the
stated unconditional class probability on the actual coherent input.
Private axes are independent of the input bank and retained throughout.

For the actual known unitary U of record/selector computation, perform the
single answer-copy and Udagger procedure of Section 5, never inverting source
preparation. On any
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

Put L=log2(n+2), p=log2 3, J=n+24, d_clock=ceil(n/2)+32 and
B_clock=2^d_clock. The selector's complete register layout and inverse are
in its packaged proof. All counts below include that actual inverse and
apply on every branch, including interrupted or incorrect histories.

The Q(n+1) source bank and Q one-pass O(n)-bit QPE/label records use
O(n^2) qubits. The J+1 stage banks have O(n) qubits each. A constant number
of O(n^2) exact controller/boundary buffers and the shared O(n^p) arithmetic
history fit O(n^2) more qubits. QPE ancillas and final endpoint helpers are
also included. Thus peak S_Q=O(n^2); no history is retained per clock tick.
Private axes, public input and controller data are counted below.

### 8.1 Scores and exact Boolean circuits

For one record and pair, use the exact multiplication and public-reciprocal
DAGs in Appendix A to compute k v modulo N and floor(2^32 z/N). They use
O(n^p) literal gates and O(n^p) cleanable helper qubits, p=log2 3. The
reciprocal is computed once after the full raw bank has arrived.
Trigonometric outputs require only CONSTANT absolute precision. The fixed
recipe below, clamp, sign and private axis therefore give the same exact
bounded rational score for every declared input word, including invalid
candidate addresses and padding after its validity mask.

Use dyadic sine/cosine outputs with denominator D0=2^20. Store each h
component numerator with common denominator20D0, retaining division by20
symbolically. Clamp numerators at+/-20D0. Score sums are exact integers
with no second rounding and O(log Q) bits beyond this fixed scale. Compute
each term, add it to the sum, and uncompute it; after copying the sign,
reverse the record scan. Each edge uses O(Qn^p)=O(n^(1+p)) gates.
A class comparison needs at most four edges. Membership scans J pivots,
copies its AND and uncomputes all helpers, using O(n^(2+p)) gates.
Only one shared arithmetic history is live, and it is cleared before reuse.

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
oracles; Appendix A implements the n-dependent product and exact quotient
with O(n^p) gates and helper qubits.

For the polynomially many non-score source/QPE operations, use the
following clean-arithmetic construction. Ripple-carry addition and unsigned comparison have O(n)-size
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
this gives O(n²) bounds for those non-score operations. Appendix A uses
the same compute/copy/uncompute rule on its O(n^p)-node score DAGs. Reuse
the appropriate shared scratch
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

Each tick has a constant number of contender/Grover macros on one fixed
candidate, plus O(n^3) conservative controller and boundary work. Section 4
and Appendix A give P(n)=O(n^(2+p)) for the complete contender predicate.
Since p>1, n^3 is smaller. Including actual known undo,

    G_main=O(B_clock*(n^(2+p)+n^3))
          =O(2^(n/2)n^(2+p)).                            (W1)

There is no outer J loop of complete Grover operations per tick. The
J comparisons are already included in P(n). Every selector operation is
exact; the only approximate words occur at polynomially many one-pass
record-QFT sites and their inverse.

### 8.3 Address generation

Use one public layout for the quantum bank, records, retained stage work
and shared scratch. It has O(n^2) wires and O(n) classical bits, so every
charged address has O(L) bits. Nonrecursive template addresses have a fixed
number of public row/column indices, for example

    base+copy_index*record_width+bit_index.

A constant number of additions, products, comparisons and bit extractions
on O(L)-bit public integers generates each such address. Schoolbook public
arithmetic costs O(L^2) bit operations; the indexed-access charge adds O(L).
Thus all nonrecursive templates pay O(L^3) work per literal gate/action.
Input bits of N and the reciprocal are read by their O(L)-bit indices,
without a new n-bit arithmetic operation per emitted gate.

For the recursive score DAG, Appendix A.5 counts every node transition and
local bit position across each whole forward or reverse traversal. It proves
O(n^p L^3) fully charged work per arithmetic call and O(L^2) classical
traversal storage. No constant worst-case number of transitions between
successive physical gates is assumed. Empty constant-folded leaves are also
counted. Multiplying the number of score calls by this traversal bound,
and charging the remaining main gates by the nonrecursive bound, gives

    O(2^(n/2)n^(2+p)L^3) fully charged main work.          (W2)

This includes the physical gate address charge and the finite literal
Toffoli expansion. No circuit list or classical arithmetic history is kept.

### 8.4 The public clock and regenerated schedules

The single public tick counter has O(n) bits and is updated once per
complete tick. Even a full carry/borrow pass costs O(nL) charged work.
Over B_clock ticks this is O(2^(n/2)nL), below (W2).

Regenerate each F_j,V_j,C_j timing constant from its public probe index,
one at a time. Copy the current public tick into known basis qubits when
needed, then clear it at tick end. Ordinary guard loops and all their
intermediate comparison/prefix helpers are cleared before the boundary.
The selector proof counts their O(n^3) operations and O(n^2) reusable
quantum scratch. No classical list of timestamps or B_clock-long gate
stream is retained.

### 8.5 Additive phase compilation

The certified word search in Section 6 has word length O(L^4), work
`2^O(L^4)`, and polylogarithmic memory at every required precision.
The required errors are inverse polynomial in n: the QFT error per
word is proportional to `(n+19)^(-2)`. No exponentially small word error is
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

For undo, public ticks run from B_clock-1 down to zero. Within each tick,
reverse the actual boundary word first, then the ordinary instructions in
reverse order. This restores the prior metadata before clearing earlier
guards. Reverse each exact score DAG as in Appendix A. Regenerate the same
public timing and QPE constants. This emits the exact inverse of the actual
forward circuit, including unfinished probes and all QFT phase words.
No gate stream or source inverse is required.

### 8.7 Peak classical storage

The live classical registers are the public modulus, one O(n)-bit
reciprocal, O(n) private axis bits, one O(n)-bit tick counter, a constant
number of public values, O(L)-bit local indices, the O(L^2) arithmetic
traversal frames/footprints and one compiler word with polylogarithmic
scratch. Their total is

    O(n+polylog(n+2))=O(n).                               (W5)

The stage count, pivots, timestamps, probes and coherent branch history are
quantum data. Source-dependent values are not copied into classical memory
during selection. After answer copying and actual undo, its measured n-bit
class and endpoint counts also fit O(n) classical bits. Fixed trigonometric
constants have an absolute fixed generation/storage cost. The compiler's
fixed polylogarithmic memory is O(n), with an absolute finite-prefix constant.
There is no quantum-addressed memory or excluded source-data table.

### 8.8 Total work

The complete traversal account in (W2), plus the clock-counter work of Section 8.4,
additive compiler cost (W4), source acquisition, initialization, measurements
and polynomial startup, gives on every branch

    T=O(2^(n/2)n^(2+p)L^3), S_C=O(n), S_Q=O(n^2), Q=O(n).

All replaced Boolean functions equal the score functions on every declared
word and return their helpers to zero. Exact arithmetic reversals use the actual emitted node gates. QPE ancillas
are separate. The selector has the exact global-clock construction proved
in the packaged selector file. Its coarse bound and the unchanged known-undo,
endpoint and adaptive-source arguments in Sections 0--7 give success 11/16.

For the rational declaration put delta=8/5-p>0. Since
(log2(n+2))^3=O(n^delta), the sharper bound gives

    T=O(2^(n/2)n^(2+p+delta))=O(2^(n/2)n^(18/5)).

For example the logarithm of L^3/n^delta is
3log L-delta log n, which tends to negative infinity. No constant is moved
inside an exponential. The finite N=2 circuit is covered by an absolute
constant. The declared time index is 1, and the polynomial space/sample
envelopes have index 0. All loops retain their original fixed public bounds.

## 9. Attribution and source scope

This package directly adapts the frozen adaptive fast-arithmetic proof,
SHA-256 `bc3a680b26f15313e7a0a1052b505ddbba78b324945066950190fd14bccd5e2d`,
and its claims, SHA-256
`57c2af903915e4cc9572da43608877296b5c3a44464e88310846d638b8b24b30`.
Its exact source, arithmetic and probability credits are retained below.

The clock selector directly adapts critical_third_selector_cost.md,
SHA-256 `1cfcac197add3d36a9e74fb59e6956d826af6227e52469db202f82ea0c1d0c37`.
Its mathematical version has SHA-256
`f732cc76fd5b04e07df1fc44e1ec4063b20d03a65d4167b552019c9ec8570818`;
the later change records review status. Its complete construction appears
in critical_third_adaptive_clock_selector.md. Reviews are not premises.

The selector construction and its source hash were complete before the team
read the public [peer note](https://api.yukon.org/api/submissions/493303b5-06f6-4ee0-9596-d8cae89c8bb4)
for submission `493303b5-06f6-4ee0-9596-d8cae89c8bb4`. No proof from that
submission was read for this package, and no material from it is used here.
This records chronology, not a priority or resource comparison claim.

The fast-arithmetic source directly adapts this account's earlier adaptive companion,
with proof SHA-256
`d407d0b6ad9ce997d8bcdd3a77fc199b258c9db2af02517be53d8cf09d8ae6af`
and claims SHA-256
`bfe5cc4c4fb41e8e16823f7bd1bfe9dd997b03c6acf1514903fb02246db99018`.
It supplies the exact adaptive model, bank-first reduction, complete circuit,
probability proof and counted streaming controller. This exact source
snapshot is retained locally; no public URL is available at this writing.

The repeated score arithmetic and its counted generator directly adapt
critical_third_fast_arithmetic.md, SHA-256
`88fe208d8fb3fa9dbf167af8a8a2283aa3c4d9c38c4b606c0150317929f25c26`.
Appendix A reproduces its exact all-input construction. Sections 8.1--8.8
integrate that implementation into the complete algorithm and resource proof.
The numerical score, source model and selector parameters remain those
specified in this archive.

The adaptive source in turn directly adapted this account's marginal-bank
proof, submission `c730b22b-cd6b-49fa-aeff-743346b595f0`, evaluated commit
`b8514e80a2f1d8607df9ba13a53393bb287774f5`. Its exact public
[proof](https://github.com/Layr-Labs/dcp/blob/b8514e80a2f1d8607df9ba13a53393bb287774f5/submission/proof.md)
and [claims](https://github.com/Layr-Labs/dcp/blob/b8514e80a2f1d8607df9ba13a53393bb287774f5/submission/submission.json)
have SHA-256 respectively
`5f65293c777ed7d46f1a2e09ae165f0bab315d8cf39ac88b59747f14976d587b`
and `91ca3254a4355b032f4e495f8d015f0dd122bb40ff15f5f22b6c3570a0b36d5c`.
Its common circuit, good-first analysis, phase compiler, deterministic word
regeneration and streaming resource account are used here through the
adaptive source. All needed arguments are reproduced; no prior verdict is
a proof premise.

The circuit, cubic witness, QND recording, class tournament, coherent selector,
phase compiler, known undo, endpoint decision and exact adaptive error-model
text come from submission `f892f7ea-957b-4dde-8374-dab2736231d0`, evaluated at
commit `3f9e53c2a129e9ff95b5d1754dcd5587331fbcf1`. Its exact public sources are
[proof](https://github.com/Layr-Labs/dcp/blob/3f9e53c2a129e9ff95b5d1754dcd5587331fbcf1/submission/proof.md)
and [claims](https://github.com/Layr-Labs/dcp/blob/3f9e53c2a129e9ff95b5d1754dcd5587331fbcf1/submission/submission.json).
Their SHA-256 hashes are respectively
`c492a4f842e114110805b2de648d1004b12f0367ddbaa9fee8dcb5f3fdf66379`
and `0ae39b5aff47f7be6d7373cda268ea8bc9ed1107e641fe2bc95e74b2823b8fc6`.
The source's bank-first induction is reproduced in Lemma 0. All needed
circuit arguments are reproduced here; no external algorithm oracle or
prior validity judgment is a premise.

RWT25, submission `3f48c893-2d1b-4e9b-ac9e-e9d318149910`, supplied the
clean-marginal model wording used in the own-source proof. The marginal
condition is retained here as the intermediate identity (0), obtained from
the adaptive delivery reduction. Its
[exact proof](https://github.com/Layr-Labs/dcp/blob/dd6041a0fc1cfe8c29b2af14c5ffc7b29b18ee75/submission/proof.md)
has SHA-256
`6e83a34c0c2283f0acbfab9bf523accebec2cdf4f81b2eb5f32706224d78fd47`.
This records use of the model description through the own-source proof;
RWT25's algorithm is not used in this construction.

The original circuit source credits its reflection-testing and
retained-register search framework to DEV-era RGRST1,
[Layr-Labs/dcp pull request 54](https://github.com/Layr-Labs/dcp/pull/54).
No result from that pull request is needed to verify the circuit reproduced
here. No historical comparison is part of the five formal claims.

## Appendix A. Exact repeated score arithmetic

### A.1 A multiplication DAG with O(w^p) nodes

First pad the operand length w to a power of two, at a factor less than two.
For w=2v, write x=x0+2^v x1 and y=y0+2^v y1, with v-bit parts. Compute

    z0=x0 y0, z2=x1 y1,
    d=(x1-x0)(y1-y0),
    z1=z0+z2-d,
    xy=z0+2^v z1+2^(2v)z2.                               (A3)

Compute the two differences as a sign and a v-bit absolute magnitude.
Compute their magnitude product recursively, and retain its sign. Thus there
are exactly three recursive v-bit products. Comparisons, magnitude selection,
signed addition and assembly use a fixed number of ripple Boolean circuits
on O(w)-bit words, hence O(w) Boolean nodes. Use w+3 bits for the signed
intermediate arithmetic and 2w+3 bits for final assembly. The true product
fits in 2w bits; no input-dependent overflow branch is omitted.

The base case is a one-bit AND. If B(w) counts all Boolean nodes, including
copies and all carry nodes, then

    B(w)<=3B(w/2)+Cw+C0=O(w^p).                           (A4)

This is a straight-line Boolean DAG. Each intermediate bit has its own
allocated target; no bit is erased during forward evaluation. In contrast
to a space-efficient classical recursion, this construction keeps the full
O(w^p) history until it is reversed. It uses O(w^p) bits, not O(w) bits.
The inputs and the final 2w-bit output are included in that bound.

Every operation has a fixed Boolean circuit, with no branch on an unknown
data bit. Comparators select outputs by Boolean masks. Zero padding and
public constant operands are literal Boolean inputs. Repeated input wires
and constant bits can be reduced by the exact rules in Appendix A.2.
Equation (A3) therefore gives the exact product for every declared input word.

### A.2 Exact reversible evaluation and its actual inverse

For a Boolean DAG F and an arbitrary XOR target y, do the following:

1. Compute each DAG node into its own fresh zero qubit.
2. CNOT the selected output bits into y.
3. Emit the actual node gates in reverse order and invert each gate.

A fresh-target NOT uses X(target), CX(input,target); XOR uses two CNOTs;
AND uses one Toffoli. Repeated-input AND is CNOT, repeated-input XOR is zero,
and constant inputs use X, CNOT or no gate as appropriate. Use the exact finite Toffoli expansion in Section 8.1. Thus this realizes

    |x>|y>|0_history> -> |x>|y XOR F(x)>|0_history>         (A5)

with O(B) literal Clifford+T gates and O(B) helper qubits. It is exact for
every x and y, so it is also exact on superpositions and arbitrary joint
extensions. The reverse is the inverse of the actual emitted gate stream.
There is no approximate arithmetic word or source-dependent compilation.

All helpers in (A5) return to zero. They are separate from the retained
QPE ancillas in Sections 2 and 6. No approximate phase gadget acts on these
arithmetic helpers. The selector reflections, guards and verified bits are
exact and use the total implementation in the packaged selector proof.

### A.3 Exact quotient and remainder with one public reciprocal

The score needs both k v mod N and floor(2^32 z/N), where 0<=z<N. Put

    w=n+32, B=2^w, mu=floor(B^2/N).                        (A6)

After the full raw bank has arrived, compute mu once, classically, by binary
long division. Its length is at most 2w bits since N>=2. This takes O(n^2)
arithmetic bit operations and O(n) classical scratch. Keep this one public
O(n)-bit constant; no reciprocal table is required. Its setup and address
costs are polynomial and additive. The bank-first acquisition order is kept.

For ANY unsigned 2w-bit X, compute the following Boolean function:

    q0=floor(X mu/B^2), r0=X-q0 N,
    b=[r0>=N], q=q0+b, r=r0-bN.                           (A7)

All products in (A7) use (A3), with exact lengths O(w). Division by B^2 is
only bit selection. Write mu=B^2/N-theta, 0<=theta<1. Since X<B^2,

    X/N-1 < X mu/B^2 <= X/N,
    floor(X/N)-1 <= q0 <= floor(X/N).                     (A8)

Hence 0<=r0<2N, and (A7) returns exactly

    q=floor(X/N), r=X mod N.                              (A9)

Use full product widths, O(w)-bit quotient registers and sufficiently wide
unsigned subtractions. All widths can be bounded by 4w+4. No leading bits,
borrow, correction or output is assumed zero without (A8). In particular,
(A7) is total for every declared X, even on wrong algorithm branches.

There are a fixed number of products, additions and comparisons. Their
combined DAG has O(n^p) nodes. Reversible evaluation by (A5) therefore costs
O(n^p) literal gates and O(n^p) reusable helpers. Both quotient and remainder
may be copied out before the same history is uncomputed.

For arbitrary n-bit k,v, their product is below 2^(2n)<=B^2. First use (A7)
to return z=k v mod N. This does not require k or v to be less than N.
Next set X=2^32 z<B, and use (A7) again to return the exact integer
floor(2^32 z/N). Its value is in [0,2^32), so the existing fixed-width
trigonometric recipe receives exactly the same input. The n+32 choice
handles all n>=1; no asymptotic small-n assumption is hidden here.

### A.4 All score inputs and helper lifetimes

Candidate and pivot words can be any n-bit values. For 2t-u modulo N,
form the unsigned integer v'=2t+2N-u. Since N>2^(n-1),

    0<=v'<6N.

Five fixed compare/subtract-N steps reduce it exactly to [0,N). This uses
O(n) Boolean nodes and handles all t,u, including invalid class addresses.
Use the same construction for 2u-t. The other operands t and u may be used
directly, since the modular product already accepts all n-bit operands.

For each record, evaluate the same four phases at t,u,2t-u,2u-t. Keep the
existing 32-bit fraction, fixed Taylor recipe, dyadic denominator D0=2^20,
symbolic division by 20, clamp, sign and private-axis choice. Every numerical
output is therefore IDENTICAL to the score specified in Sections 3 and 8.1 on every computational input.
On source padding, the retained validity flag still makes the score zero.
The arithmetic is total before that mask is applied; it does not attempt
to divide by a source-dependent denominator or assume a valid label.

The fixed trigonometric circuit has absolute constant width, degree and
history size. The n-dependent work per record is O(n^p). Score accumulation
uses the same O(log Q) extra bits and exact signed scale as before. In-place
addition is a permutation on its full declared word, with its exact inverse.
The copied-score/sign operation and reverse record scan are unchanged.

One shared helper block is live for a complete arithmetic compute/copy/
uncompute at a time. Its FULL DAG history is counted in O(n^p). After (A5)
the block is zero and can be reused for the next modular product, term,
record or pivot. A fixed number of O(n)-bit term/output registers and the
score accumulator coexist with it. They add only O(n^p) space. No record,
edge, pivot or repeated search iteration retains a private arithmetic history.

The bank, QND records and retained selector history use O(n^2) qubits.
Adding the shared O(n^p) arithmetic block and the separate phase targets
still gives S_Q=O(n^2), since p<2. This is a simultaneous peak bound, not a
sum of scratch bounds from different lifetimes.

### A.5 A counted forward and reverse DAG generator

The generator stores no gate list and does not evaluate quantum data.
Give every product node a fixed number of local word buffers of O(w) bits,
then three disjoint child blocks. Pad the local allocation to a fixed size
a w+b. Its history footprint obeys the exact public recurrence

    H(w)=3H(w/2)+a w+b.                                  (A10)

Reserve a contiguous 2w-bit output slice at a fixed position of each node.
Every child input is a contiguous view of its parent's inputs or of a local
difference-magnitude buffer. The three child bases follow from (A10). All
wire addresses, subtree footprints and template indices have O(L) bits,
because total allocated quantum and classical memory is polynomial in n.

For each internal node the forward generator executes:

    enter; local differences; child0; child2; childD;
    local signed sum/assembly; exit.

For an inverse it executes the reversed local templates and children in the
order childD, child2, child0. Every node is entered once and exited once in
either direction. There are at most six child push/pop transitions and a
fixed number of base/footprint calculations per node. The one-bit leaf is
a fixed template. No address is found by a new traversal from the root.

Let d=log2 w for the padded length. The traversal has

    (3^(d+1)-1)/2 nodes,
    sum_(j=0)^d 3^j(w/2^j)=O(w^p) local bit positions.     (A11)

Each local ripple template has a fixed number of Boolean actions per bit
position. Each action and each node transition needs a fixed number of
additions, comparisons, shifts or multiplications of O(L)-bit PUBLIC
integers. Even using schoolbook multiplication gives O(L^2) bit operations.
The global indexed-access charge is O(L), so each such public generator
event costs O(L^3) fully charged work. This includes the literal gate's
address charge. Reads of public N or mu use O(L)-bit indices; they do not
perform n-bit arithmetic to generate an individual gate.

Equations (A10)-(A11) thus bound ALL generator work for a whole forward or
reverse product stream by O(n^p L^3). This sums explicit node transitions;
it does not assume a worst-case constant number of stack operations between
successive emitted gates. The bound holds even if public constant folding
causes a leaf to emit no physical gate. Every quantum-data branch has the
same counted traversal. The nonrecursive Barrett and score templates add
only a fixed number of such traversals and O(n) local actions.

Depth is O(L). A frame has a fixed number of O(L)-bit interval bases,
operand descriptors, lengths, child cursors and direction bits. All frames
use O(L^2) classical bits. Footprints can be generated once per depth with
(A10), also in O(L^2) storage. No O(n^p)-bit CLASSICAL history is retained.
One n-bit public modulus, the one O(n)-bit reciprocal and the retained public
axes/counters/compiler workspace still give S_C=O(n).
