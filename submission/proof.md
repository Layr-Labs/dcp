# One-third adaptive tolerance with a complete L2 cache controller

## 0. Joint theorem, algorithm and source model

For every integer N>=2 and every secret s in Z/NZ put n=ceil(log2 N), K=2^n
and L=log2(n+2).
The algorithm below acquires exactly Q=192 copies when N=2 and exactly
Q=27648(2n+20) copies when N>=3. Put r=Q/3. Under the following error model,
with epsilon(n)=1/3, it outputs the entire s with unconditional probability
at least 11/16>2/3. On every execution branch the SAME algorithm and parameter
rule jointly satisfy

    T=O(2^(n/2)n^2 L^2), S_C=O(n), S_Q=O(n^2), Q=O(n).

All constants are absolute and independent of N, s, the adversary and outcomes.
These are full worst-case bounds in the uniform Clifford+T/bit-operation model,
including source acquisition, gate generation, precision, initialization,
measurements and address charges. The four envelope growth indices are 1,0,0,0.
The supported time envelope is
B_T(n)=2^(n/2)n^2 L^2. Its base-2 logarithm is
n/2+2log2 n+2log2 L, with double-logarithmic growth index 1.
The classical-space, quantum-space and sample envelopes are n, n^2 and n,
with index 0. The n=1 case is N=2 and uses a fixed-size exact trit circuit.
The fifth expression is the constant fraction 1/3, with no validity threshold.
The complete selector proof is in the packaged file
[critical_third_adaptive_cache_l2_selector.md](critical_third_adaptive_cache_l2_selector.md);
its exact clock and stage limits are part of this one algorithm.
The complete fixed-cache construction, pointwise error proof and extended
boundary are in [critical_third_adaptive_cache_l2_phase.md](critical_third_adaptive_cache_l2_phase.md).
The exact aligned memory layout and full online bit-stream controller are in
[critical_third_adaptive_cache_l2_generator.md](critical_third_adaptive_cache_l2_generator.md).
All four files form one self-contained proof. Claims 1--5 cite all four.
The controller count is reproduced in selector Appendix R. No source file
outside these four proof files is needed to establish a claim.

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
in Sections 1--8 and all packaged appendices occur only after this acquisition. The bank uses Q(n+1)
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

The analysis in Sections 1--8 and all packaged appendices is proved for every fixed B and any bank sigma
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
records. Compute exact quantum prefixes and identical new/saved class caches
from those records, run the bounded coherent class selector, copy only its final class, and undo its actual known circuit.
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

## 3. Fixed cache scores and simultaneous private-axis estimates

On valid position eigenvalue k, R_v is the row observable

    cos(2pi kv/N) X+sin(2pi kv/N) Y.

Choose a private fair axis X or Y for each copy, store those O(Q) classical
bits, rotate its row into that basis and RETAIN its quantum sign record.
Write y=(-1)^rowbit. The ideal complex coefficient is

    h_tu(k)=[11(e^(2pi ikt/N)-e^(2pi iku/N))
                  +e^(2pi ik(2t-u)/N)-e^(2pi ik(2u-t)/N)]/20.

The ideal statistic is 2y Re h on X and 2y Im h on Y. Its axis-averaged
mean is tr(M_tu rho) for EVERY source state rho, and |h_tu(k)|<=1 by (1).

Use exactly the prefix E_N, candidate cache C_E, four-word phase rule,
fixed trigonometric recipe, clamping and rational score in the packaged
cache proof, Sections 3--4. That proof establishes for EVERY label and
candidate word, through wraparound, circular error below
eta=2^-48+2^-32 for a direct cache and at most 3eta for each linear phase.
New and saved caches use the same Boolean function with the same floors.
There is no candidate-dependent approximation or random threshold.
The score lies in [-2,2], is zero on padding and has a fixed denominator.
Its exact sum uses O(log Q) additional bits. C4 bounds each trigonometric
component error by 1/2048. The QND wrong-label probability is below 1/2048.
The coefficient absolute sum 24/20 and clamping give the blockwise bound

    ||implemented mean observable-M_tu|| <=
    beta=(12/5+4)/2048=1/320.                              (2)

The cache proof supplies the all-input derivation: independent-axis
averaging is valid for an arbitrary conditional row state; off-diagonal
position coherences contribute zero; and padding is masked. Thus (2)
applies to every malformed density and after conditioning on other slots.
All score work is exact Boolean computation on retained quantum records.
There is no selected-pair table or source-dependent classical storage.

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
addresses are false. Each edge uses the identical fixed caches and exact score arithmetic in cache proof Sections 3--6;
the predicate is a total XOR-output function, with clean helpers on every
input word. It first computes the fresh class cache once, then scans Q records against
each of J saved class caches. It uses O(n^2 L) literal gates and O(n^2)
reusable helpers, including all helper cleanup. The full construction is in
cache proof Section 6.
No larger read-only input or hidden edge table is supplied.

## 5. Exact global-clock selector

For N>=3, put

    J=n+24, d_clock=ceil(n/2)+32, B_clock=2^d_clock.

The complete selector is specified and proved in
[critical_third_adaptive_cache_l2_selector.md](critical_third_adaptive_cache_l2_selector.md).
Instantiate its K with 2^n, its C with the number of classes above, its
B with B_clock and its d with d_clock. Its predicate is exactly the
contender predicate in Section 4. Allocate J+1 stage banks: one fixed active
bank and J archive slots. Each has an n-bit candidate, d_clock probes,
verification/allocation/completion bits and two (d_clock+2)-bit timestamps.
The completed-stage count has ceil(log2(J+1)) bits. Each bank also has the
2QR-bit class cache specified in cache proof Section 7, R=32. Its length
is still O(n). The active cache is zero during search; fresh contender
caches use separate scratch. Completed caches move with their full banks.

Run exactly B_clock ticks in public order. Each tick performs the guarded
initialization and probe H instructions, one guarded forward G, one guarded
inverse G, fresh verification and then the total boundary involution. All
ordinary guards and their helpers are cleared before that boundary. The
literal Grover operator is G=(2|v><v|-I)(I-2P_S); its controlled diffusion
marks enabled nonzero candidate words between unconditional H layers.
Conditional H uses V=S H T H S^dagger and V Z V^dagger=H. All these selector
gates are exact Clifford+T.

The boundary uses the cache-extended A_tau/F_(tau,E)/B_(tau,E) construction
in cache proof Section 7 and the clean XOR evaluator in selector Section 6.
That proof defines F on every word, proves disjoint domains for every E,
and gives the controlled total involution with all temporary copies clear.
The class-cache XOR is performed before the archive rotation and undone
after the inverse rotation. It preserves every completed
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

For the actual known unitary U of record/prefix/cache/selector computation, perform the
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

## 8. Joint work, addresses and peak storage

Put L=log2(n+2), J=n+24, d_clock=ceil(n/2)+32 and B_clock=2^d_clock.
The complete repeated-work proof is in cache proof Sections 6--8,
selector Appendix R and the packaged generator proof, Sections 1--6 and Appendix A. It counts all ordinary guards, eligibility histories,
cache-extended boundaries, bank rotations and actual inverse words. All
counts apply to every word and every branch, including a cap inside a probe.

### 8.1 Exact all-input helpers

For the polynomially many source/QPE and prefix-setup operations, use the
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
this gives O(n²) bounds for those operations. The cache ripple templates use
the same compute/copy/uncompute rule. Reuse the shared scratch after each compute/copy/uncompute, including on superpositions and padding.

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

### 8.2 Repeated gates and fully charged generation

The exact prefix E_N(k)=floor(2^(n+b)(k mod N)/N), b=ceil(log2 n)+48,
is computed once per retained label after record setup. Restoring division
has an O(n^2)-size fixed Boolean DAG per record and O(n^2) reusable scratch.
Its O(Qn^2)=O(n^3) gates and Q(n+b)=O(n^2) retained prefix bits are fully
counted. Prefix undo reverses the same actual circuit.

Cache proof Sections 6--7 give O(n^2 L) local operations for one contender
predicate, including its fresh cache, all J archived edges and all cleanup,
and O(n^2 L) for a complete cache-extended boundary. The boundary makes only
a fixed number of full cache calls; it does not recompute one per output bit.
The ordinary controller uses O(n^2) local operations per tick by selector
Appendix R. Each tick has only a constant number of contender/Grover macros,
on the one active workspace. Therefore, including actual undo,

    G_main=O(B_clock n^2 L)=O(2^(n/2)n^2 L).              (W1)

The algorithm selects exactly the online finite-program multitape bit
controller in the packaged generator proof, Sections 1--6, with its complete
aligned layout in Appendix A. Each fixed row/slot dimension is padded to a
power of two and each field type has a separate array. This adds only a
constant factor to allocation and preserves the entire logical bank map.
A fixed number of ready operand-address words serves each ripple bit
gadget. Dispatch uses those words and pays the full A=ceil(log2(M+2)) debit
per operand use, with M=O(n^2), hence A=O(L). All construction, changes,
copies, inspections, bit accesses and head moves are counted separately.

The controller executes full deterministic scans. Tape heads perform the
carry and return walks, and marked loop strips give each local loop its
endpoint and rewind. A fixed number of strips uses O(n) classical bits.
For m consecutive increments or decrements of any w-bit pointer, including
wraparound and any starting value, at most 2m+w bits change. Counting the
actual reads, writes, carry tests, head moves and returns therefore gives
O(m+w) raw actions. Each complete fixed-stride scan of m positions, including
setup of its ready operands and all loop ends, costs O(m+A) raw actions.
This bound applies to a complete scan; one long carry can cost O(A) raw
actions. The full proof also counts short and empty scans, variable guard
endpoint placement and reverse endpoint setup.

Cache evaluation costs O(Qn(b+A))=O(n^2 L) raw actions. All JQ score terms,
constant-width trigonometric words, O(L)-bit exact sum updates and their
undo cost O(JQ(L+A))=O(n^2 L). Guards, controller metadata, bank copies,
rotations and correction scans cost O(n^2), apart from a fixed number of
complete cache calls at each boundary. Public q=O(n)-bit tick and timing
constants cost O(n^2) raw actions per tick, including full limit tests and
buffer clearing. All remaining short setup events number O(n^2), each with
O(A) raw work. Every full tick therefore uses O(n^2 L) raw bit/head/gate
actions, on every branch. Charging A for each such action, gate dispatch
and its fixed number of ready-address uses gives

    O(n^2 L A)=O(n^2 L^2) charged work per full tick,
    O(2^(n/2)n^2 L^2) total repeated work.                (W2)

The same complete-scan proof counts descending loops and the actual inverse.
The deterministic scan bound is over public forward/reverse words, including
inert controls and failed or unfinished searches. It uses no probability law
or success-conditioned execution length.

There is no stored exponential instruction list, free address generation,
quantum-addressed lookup or compiler call inside these exact selector ticks.
All source-dependent prefixes, signs, candidates and caches stay quantum.

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
guards. Reverse every exact prefix/cache/score template in its literal order.
Regenerate the same public timing and QPE constants. This emits the exact inverse of the actual
forward circuit, including unfinished probes and all QFT phase words.
No gate stream or source inverse is required.

### 8.7 Peak storage and all remaining work

The Q(n+1) raw registers, Q one-pass O(n)-bit QPE/label records and Q(n+b)
prefix bits use O(n^2) qubits. The J+1 stage banks, each with n candidate
bits, O(n) probes/timestamps and 2QR cache bits, use O(n^2). A fixed number
of O(n^2) temporary arrays and clean Boolean histories suffice for division,
controller eligibility and cache boundaries. Fresh cache and score scratch
use O(n) and O(L) qubits apart from the fixed trigonometric history.
These buffers and residual old work after answer copying can coexist with
fresh endpoint helpers within O(n^2). Every allocation and initialization
is charged. There is no retained history per tick.

The classical store contains N, O(n) private axis bits, the public O(n)-bit
tick and a fixed number of public time constants, O(n) marked loop strips,
a fixed number of O(L)-bit ready operand words, indices and head locations,
one regenerated phase word and its polylogarithmic compiler scratch.
No label, pivot, prefix or cache table is measured into classical storage.
The finite trigonometric constants have absolute fixed storage. Thus
S_C=O(n+polylog(n+2))=O(n). The measured final class and endpoint counts fit
in that store. The prefix divider and cache loops have fixed nesting depth.

Source acquisition costs exactly Q(n+1). QND preparation and actual undo,
all modular shifts, prefix setup/undo (O(n^3 L^2) charged work), initialization,
answer copying/undo, measurements and the endpoint add fixed polynomials in n.
Section 8.5 adds 2^O(L^4) charged compiler work. Each fixed polynomial and
2^O(L^4) is o(2^(n/2)), so these additive costs fit (W2). This comparison
uses absolute constants and includes all smaller n by increasing one outer
constant. It does not treat precomputation or gate generation as free.

All Q raw copies arrive before private axes or measurements. There are no
later source calls or restarts. The exact N=2 branch uses Q=192, and all
other N use Q=27648(2n+20). Therefore every execution branch jointly satisfies

    T=O(2^(n/2)n^2 L^2), S_C=O(n), S_Q=O(n^2), Q=O(n).

Sections 0--7 and all packaged appendices give epsilon=1/3 and full-secret
success at least 11/16 for the exact adaptive model. The envelope indices
are 1,0,0,0. The selector's two limits and an unfinished probe affect success
only through the proved unconditional bound; they never increase resources.

## 9. Attribution and source scope

This package directly adapts critical_third_adaptive_clock.md, SHA-256
`c423bebbc2a14e3b04c79b348df0440e170680ca39c5665cd19019866cbd0f75`,
and its selector, SHA-256
`757849df60d8f2efb5eb151e6bf09abe1f02a33ec9866b0cad0070103b09a98b`.
It retains their exact adaptive error model, bank-first reduction, source
circuit, QND analysis, finite compiler, known undo and endpoint decision.
The earlier adaptive fast-arithmetic proof/claims have SHA-256 respectively
`bc3a680b26f15313e7a0a1052b505ddbba78b324945066950190fd14bccd5e2d` and
`57c2af903915e4cc9572da43608877296b5c3a44464e88310846d638b8b24b30`.

The fixed phase-cache proof is critical_third_phase_cache.md, SHA-256
`7e3811e6b06023d3a7094fd476503f69c4ce9a1ed9dab4f8efd5c476e8e989ad`.
Its full cache map, error, statistics, total boundary and resource arguments
are reproduced in critical_third_adaptive_cache_l2_phase.md. Its material
cache/prefix idea came from the actual public note for submission
`493303b5-06f6-4ee0-9596-d8cae89c8bb4`,
[Exact one-third tolerance with cached phase comparisons](https://api.yukon.org/api/submissions/493303b5-06f6-4ee0-9596-d8cae89c8bb4).
The exact note read has SHA-256
`5aeeec4b4dcd3c563a6abfc7688b2a3bdbfa3e25c8fee221983b4c3f63c82d41`.
The note was read before the evaluated commit was published. The submission
is now published at commit `d1d5a491f9b908ada5de2c7937fdf4732aede43d`.
Material use to build this package was the actual note. After construction,
we inspected the published peer [proof](https://github.com/Layr-Labs/dcp/blob/d1d5a491f9b908ada5de2c7937fdf4732aede43d/submission/proof.md),
SHA-256 `e659fd631482bac4d1977d0463d9951df6eaf8ec325e811c45e7646f71687074`,
Sections 4 and 10, for source attribution. It credits ROB-G2, submission
`55a6ce76-34af-468f-b735-a1197f3d3459`, for uniform phase tests, classical
prefix words, coherent truncated accumulation and counted constant-table
lookup, and R24/f892 for the cubic witness, coarse classes, known undo and
same-bank endpoint. This records the dependencies stated in that proof;
ROB-G2 itself was not read for this package. The present cache proof is
reproduced in full and uses the identical fixed map in both roles. No peer
proof or review verdict is a mathematical premise. The present cache uses coherent quantum prefixes and the identical
fixed map for both new and saved candidates. The complete derivation is here.

The complete bit-stream controller directly adapts
critical_third_cache_generator_l2.md, SHA-256
`eb122317b103da59cdd982b29f863da27d1d932313e8b67861d1d212a64088f3`.
Its full controller, tape/marker/scan construction, all template charges,
space and reverse-stream proof appear in the packaged generator Sections
1--6. Its complete aligned layout, reproduced in generator Appendix A,
comes from critical_third_cache_generator.md, Sections 1--5, SHA-256
`aef20cce6a000e53f437c2e1ebcfa5976a211e8071964cb0380d32ac348e5e49`.

This package directly copies the complete L3 adaptive cache source before
selecting the bit-stream controller. Those source main/selector/phase/
generator/claims hashes are respectively
`1c3e2f48fe6fd33bc1b175686d40f620eaad32c258a3a0cfa54d5209ebee8e30`,
`9070a62090c636fe00ad379f632d21d54cd494f08afdd1f63134ae941ff4f0d1`,
`5ec6e72d48084a3e78076c77a935d74c689213c2b4b3dea5c9ded9ec8d62b2ac`,
`8bafe15d29d353cd4e1ac05d666a307a1d67bccb9b4f1fa3eabcdb6de0545e04`, and
`336a471164674ee8341fe911596b456466b087b71253d23a6484803d8780d271`.
All mathematical arguments needed for the present claims are reproduced.

The clock selector directly adapts critical_third_selector_cost.md, SHA-256
`1cfcac197add3d36a9e74fb59e6956d826af6227e52469db202f82ea0c1d0c37`.
Its mathematical version has SHA-256
`f732cc76fd5b04e07df1fc44e1ec4063b20d03a65d4167b552019c9ec8570818`.
The selector and its full source hash existed before the peer note was read.
The ordinary-controller count comes from critical_third_controller_resources.md,
SHA-256 `25f5bbbefed19f2274decf10eb8812f2cf205362741fb52ec98b86b9461b04bc`,
and is reproduced in selector Appendix R. No review or verdict is a premise.

The fast-arithmetic source directly adapts this account's earlier adaptive companion,
with proof SHA-256
`d407d0b6ad9ce997d8bcdd3a77fc199b258c9db2af02517be53d8cf09d8ae6af`
and claims SHA-256
`bfe5cc4c4fb41e8e16823f7bd1bfe9dd997b03c6acf1514903fb02246db99018`.
It supplies the exact adaptive model, bank-first reduction, complete circuit,
probability proof and counted streaming controller. This exact source
snapshot is retained locally; no public URL is available at this writing.

The earlier exact score arithmetic and generator came from
critical_third_fast_arithmetic.md, SHA-256
`88fe208d8fb3fa9dbf167af8a8a2283aa3c4d9c38c4b606c0150317929f25c26`.
The present repeated predicate is the fixed cache construction reproduced
in the packaged cache proof. The retained source credits record the source
chain; no old repeated-arithmetic bound is a premise of this theorem.

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
