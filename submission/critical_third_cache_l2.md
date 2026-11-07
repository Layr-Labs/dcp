# Exact phase-cache selection with a counted bit controller

## 0. Joint theorem, algorithm and source model

For every integer N>=2 and every secret s in Z/NZ put n=ceil(log2 N), K=2^n.
The algorithm below acquires exactly Q=192 copies when N=2 and exactly
Q=27648(2n+20) copies when N>=3. Put r=Q/3. Under the following error model,
with epsilon(n)=1/3, it outputs the entire s with unconditional probability
at least 11/16>2/3. On every execution branch the SAME algorithm and parameter
rule jointly satisfy

    T=O(2^(n/2)n^2(log2(n+2))^2), S_C=O(n), S_Q=O(n^2), Q=O(n).

All constants are absolute and independent of N, s, the bank state and outcomes.
These are full worst-case bounds in the uniform Clifford+T/bit-operation model,
including source acquisition, gate generation, precision, initialization,
measurements and address charges. The four envelope growth indices are 1,0,0,0.
Put L=log2(n+2). The supported time envelope is 2^(n/2)n^2 L^2.
Its base-2 logarithm is n/2+2log2 n+2log2 L, with growth index 1.
The classical-space, quantum-space and sample envelopes are n, n^2 and n,
with growth index 0. The n=1 case is N=2 and uses a fixed-size exact trit
circuit. The fifth expression is the constant fraction 1/3, for every n>=1.

The complete package has four proof files. This main file supplies the
source model, witnesses, QND records, good-first statistical argument,
phase compiler, known undo, endpoint and total resource theorem.
[critical_third_cache_l2_selector.md](critical_third_cache_l2_selector.md) supplies
the complete fixed-clock search, uniform pivot law, caps and total boundary.
[critical_third_cache_l2_phase.md](critical_third_cache_l2_phase.md) supplies the
identical phase map, all-word error bound, score, fresh/saved cache algorithm
and cache-extended boundary. [critical_third_cache_l2_controller.md](critical_third_cache_l2_controller.md)
supplies the complete quadratic ordinary-controller count, cache
extension cost and the full literal online generator in Section 10. Each of the five claims cites all four files. Every required
argument is included in this package; source and review notes are provenance.

The selected implementation uses the finite multitape bit controller in
controller Section 10 for every complete public tick and its actual reverse.
That section proves O(n^2 L) raw bit/head actions for the entire tick, then
charges every action and fixed-arity gate/address dispatch by O(L). It proves
O(n^2 L^2) charged tick work. It does not assume O(L) work for an arbitrary
isolated gate. All loop strips, ready operand words and head locations are
counted in S_C. Sections 8.3 and 8.7 retain complete conservative fallback
accounts for the same logical circuit; the actual selected online stream is
specified in Section 8.8 and controller Section 10.

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
through record, prefix, cache and coarse computation and their actual known
inverse. The marginal
promise does not imply independence between G and B. No step below uses that
stronger assumption. The good-first record order in Section 3 is for the proof
only, and does not give the algorithm B.

### Algorithm summary

After acquiring the bank, record one valid-position/QND Fourier-label register
and one private X/Y sign per copy, without measuring the source-dependent
records. Compute exact quantum label prefixes from those records. Compute each new
class cache once per predicate, retain the identical caches with saved pivots,
and run the bounded coherent class selector. Copy only its final class and
undo its actual known circuit.
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

Use the following one fixed phase map for every fresh and saved member.
Put R=32, b=ceil(log2 n)+48, P=n+b, and for every n-bit label k' let

    k0=k' mod N, E=floor(2^P k0/N),
    W_j(E)=floor(E/2^(n-j)) mod 2^b,
    C_E(t)=floor(((sum_(j=0)^(n-1) t_j W_j(E)) mod 2^b)/2^(b-R)).

Retain each E as quantum data. For t,u evaluate the four fixed trigonometric
inputs C_E(t), C_E(u), (2C_E(t)-C_E(u)) mod 2^R and
(2C_E(u)-C_E(t)) mod 2^R, divided by 2^R. The phase appendix proves, for every
label and candidate word, circular error below eta=2^-48+2^-32 for each of
the first two inputs and at most 3eta for the last two. Its literal constant
Taylor recipe has component error below 2^-20 on its input, hence error
below 2^-20+6pi eta<2^-19<1/2048 against every desired exact component.
This is a uniform deterministic bound, including all phase wraparound.
Every saved cache is generated by this identical C_E map. Therefore the
score of a pair is independent of its stage, role or storage position.

Evaluate each sine/cosine with that absolute fixed-point error<=1/2048 and clamp
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
beat every previously accepted pivot. The predicate creates the fresh class cache once, scans the previous pivots
and computes their edges from the Q read-only shadow records and saved caches. It stores no
exponential candidate or edge table. Candidate/pivot labels are ordinary
quantum operands in reversible arithmetic; record addresses are public loops.

The selector uses the exact global-clock construction in the packaged
selector appendix, Sections 1-8. It searches this contender predicate on one fixed
active candidate register, retains completed pivots and selects each next
pivot uniformly from the current nonempty contender set. Its cap analysis
is unconditional; no pivot law is asserted by conditioning on a successful
cap. The final answer is the last completed verified pivot, including one
completed in the last allowed stage. An unfinished stage is ignored.

The row/sign records and prefixes determine one immutable tournament.
Initially every stage cache is zero. Inductively, every accepted boundary
stores the exact C_E vectors of its selected candidate, and every later
predicate only reads them. Thus each reachable contender call agrees with
that same tournament on every fixed record block. Linearity extends this
identity to coherent records. Arbitrary inconsistent archive words need
only the total all-word circuit and inverse proved in the appendices.

## 5. Exact globally bounded coherent selection

Put J=n+24, Bclk=2^(ceil(n/2)+32), and d=ceil(n/2)+32. Execute exactly Bclk
public ticks. Use J+1 O(n)-qubit stage banks: one active bank at the fixed
front address, completed banks at the end, and zero unused banks between.
Each stage holds its candidate, d retained probes, fresh verification bit,
allocation/completion bits, (d+2)-bit start/end timestamps and two QR-bit
member caches. At odd N the second member cache is zero. The active cache
is zero during search; a completed cache is read-only. The same C_E map
generates new and saved caches, as the phase appendix proves. The completed
stage count has ceil(log2(J+1)) bits. All of these are quantum data.

For a fixed read-only contender set S, let v be the uniform superposition
on K addresses, R_f=I-2P_S, D=2|v><v|-I and G=D R_f. The signs are literal:
Gv=v when S is empty and Gv=-v when every address is marked. Controlled D
uses unconditional H^n, sign -1 on [enable AND candidate!=0], then H^n.
It must not be replaced by the negative diffusion. Controlled H has the
exact V-CZ-Vdagger construction in appendix Section 7. All selector gates
are exact Clifford+T/Boolean gates; no approximate pi/3 boost is used.

At level j, t_j=2^j, apply H, controlled G^(t_j), H to a retained probe.
After its first outcome 1, apply G^(-t_j) and verify the contender predicate
in a fresh bit. The resulting candidate is exactly uniform on S. A zero
probe continues on the same candidate. These are deferred measurements;
all probe and pivot histories are retained coherently. An empty set never
produces a completed probe 1.

Use the exact schedule F_j=t_j-1+2j, verification V_j=3t_j+2j+1 and boundary
C_j=3t_j+2j+2 relative to the retained stage start. Each global tick emits
candidate/probe preparation, at most one guarded forward G, one guarded
inverse G, fresh verification and the boundary, in that order. All guards
and their helpers are cleared before the boundary. Their target fields
are excluded from their own read predicates. The boundary is the total
clock-dependent involution T_(tau,E) proved in selector Section 6 and phase
Section 7. Its forward F branch first XORs the selected class cache into
the zero front field, then performs the fixed archive permutation. It is not a sticky
halt update or overwritten timestamp. It rotates whole stage banks and
retains every completed record. All scratch, output copies and reverse
maps are counted there for every input word, including unreachable ones.

The appendix proves the exact marked-state identity, the expected total
nonempty-search cost below 96sqrt(K), and the cap coupling. The global time
cap fails before the winner with probability below 2^-24. The finite J cap
adds at most 2^-24. Thus the selector fails with probability below 2^-23 on
every fixed read-only tournament with a Condorcet winner. This includes a
winner in the last stage and caps inside probes, inverse corrections or
verification. The coherent circuit has the same law on its complete
orthogonal history records. The source is used through its retained coherent records throughout this search.

At the end, a fixed scan returns the rightmost completed verified bank's
candidate, or 0 if none. Copy only this n-bit answer, undo that computation,
then reverse every actual tick, the quantum prefix setup, and finally the
record preparation. The
appendix gives the full exact inverse, including interrupted stages. Its
proof and controller are included as evidence, not used as a free oracle.

## 6. Paid one-pass phase compilation and exact selector work

Only the QPE record preparation and its actual inverse need approximate
phase words. Section 2 supplies their complete controlled-phase construction
from unconditional one-qubit words and the total operator-error budget.
Their global phases are independent of data; the actual inverse reverses
the actual word. All position-shift and Boolean helpers are exact and clean
on the complete padded domain. Record phase ancillas remain retained until
that inverse. They are never used as clean arithmetic helpers.

The selector in Section 5 and the selector appendix uses exact Clifford+T gates only.
Its Boolean helpers clear for every logical word. Literal diffusion signs,
conditional H phases and boundary inversion are proved in the appendix.
No per-selector or per-tick approximate phase compiler is needed.

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
equality test. Target phases pi/2^j have uniformly computable interval entries from
Machin's arctangent series and bounded sine/cosine Taylor series. Tiny phases
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
one-pass QPE and its undo; none occurs inside the exact selector tick stream. Section 8 counts this
additive compiler work and proves the O(n) classical-space bound. All words
are generated by charged computation, not supplied as instance advice.

## 7. Coarse success, known undo, and same-bank endpoint decision

On the score event (3), the class tournament has its Condorcet winner.
The appendix's unconditional cap coupling and finite-stage proof add at most
2*2^-24. Even retaining an extra unused 2^-30 allowance gives

    coarse failure <=2^-19+2*2^-24+2^-30 <2^-18.

The QPE error is already included in the score bound of Section 3. On the good-score
event the true class is recovered regardless of all wrong-class edges.
Conceptually measured records/pivots have the stated law because their saved
computational contents are never changed by later gates. The selector is exact; the already budgeted QPE acts only in record
preparation. Classical axis choices are retained independently of the input bank.

For the actual known unitary U of record/prefix/cache/selector computation, copy only the
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

## 8. Literal arithmetic, uniform generation and joint resources

Put L=log2(n+2), J=n+24, d=ceil(n/2)+32 and Bclk=2^d. All counts include
complete final known undo. The selector, phase and controller appendices
supply the full streamed constructions. This section specifies the basic
Boolean templates used by all of them and accounts for the remaining work.

### 8.1 Exact Boolean functions, clean helpers and permutations

A ripple addition has c0=0 and, for each bit i,

    s_i=a_i XOR b_i XOR c_i,
    c_(i+1)=(a_i AND b_i) XOR ((a_i XOR b_i) AND c_i).

Subtraction uses x+NOT(y)+1. Its final carry gives unsigned x>=y. Bit
selection is v XOR (choice AND (u XOR v)). These are O(w)-node Boolean
DAGs on w-bit words, with all carries and intermediate bits retained.
For an arbitrary Boolean DAG F and arbitrary XOR target z:

1. Compute every node into a fresh zero helper in topological order.
2. CNOT the selected output bits into z.
3. Reverse the actual emitted node word, inverting each letter.

A fresh-target NOT uses X then CNOT; XOR uses two CNOTs; AND uses Toffoli.
Repeated-input AND is CNOT; repeated-input XOR is zero. Constants use X,
CNOT or no gate. This gives the exact all-word interface

    (x,z,0_history) -> (x,z XOR F(x),0_history)

with O(number of nodes) literal gates and helpers. It is exact for arbitrary
quantum inputs and joint extensions, because it holds on every basis word.
One shared block is reused only after this exact cleanup. No arithmetic
helper is a QPE target or a retained source-dependent record.

One exact Toffoli on controls a,b and target c is the ordered word

    H(c), CX(b,c), Tdag(c), CX(a,c), T(c), CX(b,c), Tdag(c),
    CX(a,c), T(b), T(c), H(c), CX(a,b), T(a), Tdag(b), CX(a,b).

Its parity phase identity is
4abc=a+b+c-(a XOR b)-(a XOR c)-(b XOR c)+(a XOR b XOR c).
Thus it is phase-free on all eight basis inputs. Replacing Tdag by seven T
uses 33 literal gates, including 25 T gates. Every Boolean circuit above
therefore has an exact finite Clifford+T implementation.

For a known permutation f on the entire declared word domain, compute
f(x) into a clean register, swap, then XOR-evaluate f^-1 into the old input.
This gives (x,0)->(f(x),0), including every padded word. For controlled
addition modulo 2^w, use f(a,y,c)=(a,y+c*a mod 2^w,c), where c is one bit;
compute c*a with Boolean masks. The forward and inverse ripple DAGs have
O(w) nodes. This constructs an in-place controlled adder with O(w) clean
scratch and O(w) exact gates, clearing all carries on every word. Its inverse
subtracts the same masked operand. The phase cache can consequently reverse
each b-bit addition without retaining n separate carry histories.

A guarded translation adds a public v modulo N only on a valid position
word in the selected row, and fixes all other words. Compute validity by
comparison, use addition and a fixed number of compare/subtract-N steps
in a wide enough word, then select the output. Its inverse uses -v modulo N.
The whole declared padded domain is a permutation. This implements the QND
position shifts, R_v circuits and endpoint shifts with exact clean helpers.

For the additive QND rounding, schoolbook multiplication is a literal
Boolean circuit: initialize a 2w-bit zero sum and add the shifted first
operand under each of the w bits of the second. Each ripple addition has
O(w) nodes, so the full multiplication has O(w^2) nodes and history.
With B=2^(n+18), form Nz+B/2, select the bits giving
floor((Nz+B/2)/B), and compare/subtract N once. This implements the stated
nearest rounding k' modulo N on every phase word z, with a fixed tie rule.
All of this work and its full O(n^2) history are polynomial and additive.

### 8.2 Literal prefix division and fixed score arithmetic

Let k' be any n-bit QND label word. Since k'<2^n<2N for N>2^(n-1), one
compare/subtract computes k0=k' mod N. This also covers N=2^n. Store N
in n+1 public bits. Form the binary numerator X=k0*2^P by appending P zero
bits. It has n+P=O(n) bits. Perform restoring division on its bits from
most to least significant. Start R0=0. For each next numerator bit x_l use

    U_l=2R_l+x_l,
    q_l=[U_l>=N],
    R_(l+1)=U_l-q_l*N.

Induction gives 0<=R_l<N and the usual processed-prefix identity
prefix_l=N*quotient_l+R_l. Since U_l<2N, each iteration needs just one
comparison and subtraction on n+2 bits. The final quotient is exactly
floor(k0*2^P/N)<2^P. Copy its P low bits into the retained prefix E,
then reverse every divider and k0-reduction node. The whole Boolean DAG
has O((n+P)n)=O(n^2) nodes and helpers. Its XOR-output form is exact for
every input label word. The same shared divider scratch serves all Q
records, so initialization and its literal undo use O(Qn^2)=O(n^3) gates,
O(n^2) scratch and QP=O(n^2) retained quantum bits.

The phase appendix gives the complete exact C_E algorithm: add each public
b-bit window under its candidate bit, copy the top R=32 bits, and reverse
all additions. The controlled ripple construction of Section 8.1 proves
its O(nb) gates, O(b) clean scratch and total XOR-output behavior. Candidate
members use an n-bit helper for p+N/2 modulo 2^n and its inverse; class
validity rejects every invalid address. For valid classes all members
are the intended residues. At odd N the second cache stays zero.

Every trigonometric value is a constant-width dyadic integer with denominator
D0=2^20. The phase appendix specifies the full Machin/Taylor recipe and
its generation and rounding bounds. Retain division by 20 symbolically.
Clamp the component numerator to +/-20D0, then multiply by the signed
factor 2 from the row/axis record. Score sums are exact signed integers
of absolute value at most 40D0*Q, so their width is O(log Q) plus an
absolute constant. Ripple addition is a permutation on its full fixed
word. Compute each term, add it, and clear the term; copy only the sign
and reverse the entire record scan to clear the sum. A fixed number of
signs determines one canonical class edge. The complete XOR-output
predicate and all-word cleanup are in phase Section 6.

### 8.3 Every repeated operation and address is charged

Use a fixed public polynomial-size layout for source, QND and prefix
records, expanded stage banks, the fresh cache, one shared arithmetic block,
and a fixed number of full controller arrays. Every wire address has O(L)
bits. A record wire is base+slot*width+offset. A window wire is its prefix
base+n-j+bit. A cache wire is its bank base plus member/slot/bit offsets.
The generator uses a fixed number of additions or schoolbook products of
O(L)-bit public integers to obtain each address. This costs O(L^2) raw bit
operations. Each indexed access has the model's O(L) charge. Thus O(L^3)
fully charged work per local action is sufficient, including gate operands,
public reads, skipped constant templates, loop tests and transitions.
It is a bound on the complete generator, not just the physical gate count.

All templates have fixed loop depth: bank, member, record, candidate bit,
local adder/divider bit and fixed trigonometric degree. Histories have
fixed padded blocks; a node address follows from its public iteration and
local node offset. No generator traverses preceding records to find an
address. Every loop reverses with the same bounds and addresses. The
constant-width trigonometric circuit has absolute constant size and finite
charged generation. Its large fixed constants are independent of n.

The full contender predicate generates the fresh class cache once. It costs

    O(Qnb+JQ log Q+Jn)=O(n^2 L)

literal local actions, including all score scans and their reverse scans.
There is no saved per-edge arithmetic history. A fixed number of these
predicate/Grover/verification macros is emitted per tick. The controller
appendix proves O(n^2) ordinary local actions, including all q-bit time
constants, guards, public clock operations, rotations and final-answer scan.
The actual cache boundary makes a fixed number of O(Qnb) complete cache
calls plus O(n^2) copies and permutations, hence O(n^2 L) actions. Its
XOR evaluator computes each full transformed temporary once per branch,
not once per output bit. Phase Section 7 proves this construction for every
word, with O(n^2) scratch, including inconsistent unreachable cache words.

Therefore each full tick has O(n^2 L) local actions and O(n^2 L^4) fully
charged work. Exactly Bclk ticks run on every branch. The literal inverse
has the same cost. Thus the complete repeated work is

    T_repeat=O(2^(n/2)n^2 L^4).                           (W1)

The exact selector contains no approximate phase occurrence. Its controlled
H, diffusion, score reflections and Boolean gates have the literal words
proved here and in selector Section 7.

### 8.4 Public timing constants and actual reverse execution

Maintain one q=d+2 bit public tick counter. Copy its needed bits to known
basis wires once per tick and clear this copy at tick end. Compute tau+1
in a fixed q-bit buffer. The update, copies, clearing and reset use O(q)
local bit actions. For each public j, regenerate t_j,F_j,V_j,C_j using a
fixed number of q-bit ripple operations. Even recomputing each from zero
costs O(dq)=O(n^2) actions per full loop. No table of d timing words is kept.
A constant is generated once for its guard, rather than once per score gate.
All actual reads have the address charge in Section 8.3. Quantum timestamps
remain data; their O(n) value is not an address into an exponential schedule.

At the cutoff, the exact total answer function scans all J saved banks,
returns the rightmost completed verified candidate, or zero. It ignores
the unfinished active bank. Its suffix-selection flags are computed,
used to XOR the n-bit answer and cleared. Copy only that answer. Reverse
the answer function, then emit the inverse of every actual tick in order
tau=Bclk-1,...,0. Within a tick reverse the actual boundary circuit before
the ordinary guards. Old metadata and the old front candidate are thereby
restored before earlier controls are used. The cache inverse sees the same
E and candidate that generated its cache. No informal forward archive rule
is substituted for the literal inverse, even at an incomplete probe,
inverse correction or verification. Prefix setup and the retained record
preparation are then reversed, including their actual QPE letters.

### 8.5 Additive one-pass work and deterministic phase-word regeneration

The source bank costs exactly Q(n+1) work units and qubits. Prefix setup
and undo cost O(n^3 L^3) charged work by the explicit divider. QND preparation
and undo contain only polynomially many known modular operations and QFT
phase occurrences. Regenerate a modular-shift constant from its public
index by repeated doubling modulo N, keeping one O(n)-bit word. This work
is polynomial, including reverse loops. Every modular operation uses the
all-word guarded translation of Section 8.1. Initialization and final
measurements and endpoint helpers also have polynomial total work.

Section 6's certified word search uses O(L^4)-length words, polylogarithmic
scratch and 2^O(L^4) work at the inverse-polynomial accuracy needed for QPE.
There are only polynomially many sites. For each site, generate the word,
emit it and release its scratch. Fix the exact word order, arithmetic
precision and acceptance certificate. For an inverse, regenerate that same
forward word and reverse its actual letters; do not synthesize a different
word for the negative angle. Tdag is seven T letters. This gives total
additive compiler work 2^O(L^4), with O(n) classical storage. Phase indices
whose magnitude is below the assigned error use the certified identity;
remaining entries need O(L) numerical precision. No phase-word table is kept.
The position eigenbasis remains exact because these gates act on retained
phase ancillas only. Their helpers are distinct from clean arithmetic work.

Every fixed polynomial and 2^O(L^4) is o(2^(n/2)), since L^4=o(n). Thus
these setup, reverse, compiler and endpoint costs are absorbed in (W1).
Absolute outer constants cover the finite smaller n, including N=2.
No setup is free and no additive compiler cost is multiplied by Bclk.

### 8.6 Simultaneous peak allocations and joint theorem

The raw bank, QND records and Q prefixes use O(Qn)=O(n^2) qubits. Each of
J+1 stage banks has n candidate bits, d probes, three flags, two q-bit
timestamps and 2QR cache bits; its length is O(n), so all banks cost O(n^2).
The active fresh cache has O(Q) bits. Score sums have O(L) bits. The exact
cache adder has O(b) reusable scratch. Prefix division has O(n^2) helpers.
The boundary has a fixed number of full O(n^2)-bit input/output/copy arrays
and O(n^2) eligibility history. A fixed number of these buffers can coexist
within O(n^2); none is allocated per tick, edge or repeated Grover step.
Source/QPE records and any residual work after answer copying remain live
and counted. Fresh endpoint helpers fit O(n^2) as well. No proof needs dirty
helpers to be reused as zero helpers after an erroneous coarse answer.

Classical storage includes O(n) marked loop strips and public N, Q private
axis bits, one O(n)-bit
public tick counter, a fixed number of O(n)-bit arithmetic/timing words,
a fixed number of O(L)-bit ready operand words, layout/address bases and
counted tape-head locations, one current
phase word and its polylogarithmic compiler scratch. It is O(n), since
any fixed polylogarithm is O(n). Fixed trigonometric constants have absolute
constant storage. The final measured class and endpoint counts use O(n)
further bits. All labels, prefixes, sign records, probes, stage timestamps,
pivots and caches are quantum data; no source-dependent classical table
is stored. Public addresses are streamed and every indexed use is charged.

Using the complete online controller in Section 8.8 and controller Section
10 with the aligned layout in Section 8.7, literal predicate, total cached
boundary, actual inverse and additive costs proves, jointly on every
execution branch and every allowed input,

    T=O(2^(n/2)n^2 L^2), S_C=O(n), S_Q=O(n^2), Q=O(n).

Section 7 proves unconditional full-secret success at least 11/16. Source
acquisition is exactly Q=192 at N=2 and 27648(2n+20) otherwise. The fraction
is exactly 1/3 under the clean-marginal promise in Section 0. No cap-conditioned
resource or pivot law is used.

### 8.7 Complete aligned generator and the L3 bound

The complete conservative generator proof below is reproduced from
critical_third_cache_generator.md, Sections 1--5, exact SHA-256
`aef20cce6a000e53f437c2e1ebcfa5976a211e8071964cb0380d32ac348e5e49`.
The independent review record sol_review.md, at its then-current SHA-256
`4f451d2f6689b4648debf9f0f1e99b9c9a81f343aeed255b67ebd3550a158f8e`,
records the Sections 1--5 check. This is provenance; the proof follows here.
It replaces only the conservative address-generation allowance in Section
8.3; circuit semantics, logical gate counts and peak storage orders stay
as proved above. Its full layout and every charge are included here.

#### 8.7.1 Exact scope and source pins

Let n=ceil(log2 N), L=log2(n+2). This construction changes only the public circuit
generator and memory layout for the circuit reproduced here from:

- critical_third_phase_cache.md, SHA256
  7e3811e6b06023d3a7094fd476503f69c4ce9a1ed9dab4f8efd5c476e8e989ad;
- critical_third_controller_resources.md, SHA256
  25f5bbbefed19f2274decf10eb8812f2cf205362741fb52ec98b86b9461b04bc.

The complete proofs reproduced in this package prove O(n^2 L) literal gates per complete selector tick,
O(n^2) quantum space and O(n) classical space. A constant number of complete
predicate/cache/controller templates is run at each of exactly
Bclk=2^(ceil(n/2)+32) ticks. The reverse word has the same bounded form.
The circuit, source model, source count, phase map, fixed tournament,
total reversible boundary and success bound are unchanged here.

The phase-cache note credits submission
493303b5-06f6-4ee0-9596-d8cae89c8bb4 for the binary-prefix/cache idea.
The following proof derives the generator cost locally. It uses no unavailable peer
proof, peer generator claim or review verdict as a mathematical premise.

The rules state that classically chosen gates may act on arbitrary indexed
wires, and charge ceil(log2(M+2)) bit operations for each classical indexed
access or classically addressed gate. They also count circuit generation,
classical bit work, initialization and all failed attempts. Put

    A=ceil(log2(M+2)).

The layout below has M=O(n^2), hence A=O(L). Every indexed use, including
access to a bit of a public counter or address word, receives this charge.
No uncharged word arithmetic or stored exponential instruction word is used.

#### 8.7.2 Aligned fields and direct addresses

Replace each finite row/slot field length m by the least power of two at
least max(1,m). Its new length is less than 2 max(1,m). Use separate arrays
for the fixed number of field types when a heterogeneous bank would make
a direct bit address need a general product. Pad the record count, bank
count and member count to powers of two for address layout only. The loops
can still use the actual counts. At most a fixed number of dimensions is
used. This multiplies total allocation by only a fixed constant.

For example, a prefix bit address is

    prefix_base + (record << prefix_row_shift) + bit,

and an archived cache bit address is

    cache_base + (bank << bank_shift)
               + (member << member_shift) + (record << R_shift) + bit.

Here 2^R_shift is the fixed power-of-two width R=32; each other shift is a
public layout constant. Empty padded slots are allocated and initialized,
but are not new tournament vertices or new source copies. A window bit is
prefix_base+(record << prefix_row_shift)+(n-j)+i. The subtraction and
addition use O(A) bit actions. No product of two variable address words is
needed. Bank rotations use the same permutation on each field array.

Give every Boolean guard history a padded row of O(n) bits, with one row
per public j. This is O(n^2) qubits even when a shorter guard needs fewer
nodes. A ripple node has a fixed number of fields per bit. Its address is
obtained by a fixed shift and a fixed number of additions. Fixed-size
gadgets use fixed local offsets. Copies, swaps and output corrections use
the same fixed row/bit coordinates. The controller proof already limits
the number of live Boolean histories to O(n^2).

Setup computes the shifts and bases by bounded bit scans, counts all padded
initialization, and uses only polynomial work. The quantum allocation stays
O(n^2). Addresses, layout constants and a fixed number of loop indices use
O(L) bits each. Public N, axes and O(n)-bit time constants still use O(n)
bits in total. Padding creates no classical record table.

#### 8.7.3 A conservative explicit stream

Use the same fixed ripple-adder, comparison, Boolean-history and exact
fixed-width trigonometric templates as the two source notes. For each local
gate or elementary classical action, compute every required wire/bit address
by the Section 8.7.2 concatenations and a fixed number of A-bit additions or
subtractions. Copy a full address if needed. This costs O(A) raw bit actions,
not O(A^2): all multiplications in a flattened row formula have been replaced
by fixed shifts. Each gate has a fixed number of operands.

Maintain a fixed number of A-bit public loop words. Increment, decrement,
compare, copy, reset and test each of them by full bit scans. Even charging
O(A) raw actions for every loop transition or constant-field selection fits
O(A) raw work per local template action. A fixed number of nested loops is
enough. There is no n-deep call stack or enumeration of a represented integer.
Reverse execution reverses each loop and each elementary gate template.
It computes the same addresses with the same bound.

The q=O(n)-bit absolute time is data, not an exponentially wide address.
The controller appendix explicitly constructs tau+1 and each t_j,F_j,V_j,C_j
by O(q) bit actions and a constant number of q-bit buffers. At most O(n)
values are regenerated per tick, so this is O(n^2) raw bit actions before
local addressing. Regeneration occurs once per guard template, not once per
gate inside that template. Direct accesses to these q-bit buffers have the
same A-bit addresses. Thus their complete charged cost is O(n^2 A^2).

A local bit action, or an emitted indexed gate, has a fixed number of
indexed accesses. Charging A to each gives O(A^2) fully charged work per
local gate/template action. This includes address construction, its own
indexed bit reads/writes, loop control, gates which have a constant control,
and gates in inert quantum branches. No constant-delay gate-emission claim
is used. One complete tick therefore has charged work

    O((n^2 L+n^2) A^2)=O(n^2 L^3).                 (G1)

This is a literal online controller: it stores a current opcode, a fixed
number of current operand addresses, its public loop state and current
constant. It emits/executes one bounded gate word at a time. There is no
stored Bclk-entry schedule, circuit oracle or source-dependent lookup.

#### 8.7.4 Complete solver account

There are exactly Bclk=O(2^(n/2)) ticks. Every tick emits the full bounded
families, even if the quantum enable is zero. Both cap failure and a cap in
the middle of logical search work still execute this word and its actual
inverse. Thus G1 proves the unconditional bound

    T=O(2^(n/2)n^2 L^3),
    S_C=O(n), S_Q=O(n^2), Q=O(n).                  (G2)

Prefix setup/undo has O(n^3) literal gates and at most O(n^3 L^2) charged
work with this layout. Source acquisition, QND preparation/undo, layout
setup, final answer computation, all initialization and the trit endpoint
add fixed polynomials. The unchanged finite phase compiler adds
2^O(L^4) work. All are additive; none is free preprocessing. Each fixed
polynomial and 2^O(L^4) is o(2^(n/2)), so G2 absorbs them with an absolute
constant. N=2 uses the original exact trit endpoint and is covered by
increasing that constant. No extra approximate phase site is introduced.

The complete success and source-model arguments are in Sections 0--7 and
the packaged appendices. G2 is the supported bound for this package.

#### 8.7.5 Scope of the charged bound

The construction requires no amortized counter assumption. It replaces
the conservative O(L^3) per-action charge in Section 8.3 by O(L^2), using
aligned addresses and linear bit arithmetic. All gates, classical loops,
address operations and indexed uses are charged above. Sections 8.1--8.6
supply the literal arithmetic, all-word interfaces, inverse and additive
work. This proves G2 for the same fully specified marginal-bank algorithm.


### 8.8 Selected online bit stream and total per-tick bound

Use the entire construction in controller Section 10 with the aligned
field layout in Section 8.7. Its exact source is
critical_third_cache_generator_l2.md, SHA-256
`eb122317b103da59cdd982b29f863da27d1d932313e8b67861d1d212a64088f3`.
The full literal finite-program multitape controller, ready operand fields,
head moves, carry scans, endpoint strips, exhaustive repeated-template
account and reverse stream are reproduced in that required appendix.

A complete m-bit pass with a fixed number of ready pointers costs O(m+A)
raw bit/head actions, A=ceil(log2(M+2))=O(L), including initial addresses,
all carry walks, endpoints, head returns, short scans and reverse motion.
This is a deterministic whole-pass bound; a single carry may take O(A).
There are O(Qn) full b-bit additions for fresh/saved caches, O(JQ) score
terms with Theta(L)-bit sums, O(n) full guard scans, and fixed row scans
for all boundary copies and permutations. Constant-width score words pay
O(A) raw address setup per term. The full accounting, including all time
constants, public exponential-loop tests, cache calls and cleanup, gives
O(n^2 L) raw actions per complete tick. Each action, gate dispatch and
use of its fixed number of operand-address fields receives the full A debit.
Thus the selected stream has O(n^2 L^2) charged work per tick.

The controller keeps a fixed number of O(n)-cell marked loop strips, a
fixed number of O(A)-bit operand fields and head locations, public axes,
modulus and O(n)-bit clock/constant buffers. Their simultaneous classical
peak is O(n). The quantum circuit and aligned padding remain O(n^2).
Exactly Bclk ticks and their actual literal reverse run on all branches,
including inert controls, failed probes and an unfinished final search.
Adding the explicitly charged setup, QND/prefix work, compiler and endpoint
therefore proves T=O(2^(n/2)n^2 L^2) with the same other bounds and success.
No per-gate shortcut, free address, gate oracle, source inverse or
success-conditioned amortization is used.

## 9. Attribution and scope

The direct algorithm and source-model dependency is accepted submission
`c730b22b-cd6b-49fa-aeff-743346b595f0`, evaluated at commit
`b8514e80a2f1d8607df9ba13a53393bb287774f5`. Its exact
[proof](https://github.com/Layr-Labs/dcp/blob/b8514e80a2f1d8607df9ba13a53393bb287774f5/submission/proof.md)
has SHA-256 `5f65293c777ed7d46f1a2e09ae165f0bab315d8cf39ac88b59747f14976d587b`;
its exact
[claim manifest](https://github.com/Layr-Labs/dcp/blob/b8514e80a2f1d8607df9ba13a53393bb287774f5/submission/submission.json)
has SHA-256 `91ca3254a4355b032f4e495f8d015f0dd122bb40ff15f5f22b6c3570a0b36d5c`.
These bytes were read and verified against the accepted local stage. Its bank
model, cubic witness, record bounds, good-first argument, copy counts and
same-bank undo/endpoint proof are reproduced here. Its selector is replaced
by the complete construction in the packaged appendix. No external circuit
oracle is needed.

The immediate complete L3 package is critical_third_cache.md, SHA-256
`8b07a27798102f1d5431965c2362f56f1514a056e545705601aab615cea72bf4`;
its declaration critical_third_cache.json has SHA-256
`e389689e1e46ed2d2351c03e60dac3945e49acf3f8784f3cadd3c1e444884652`.
Its selector, phase and controller appendices have SHA-256, respectively,
`6259b3263d52a5630ec93aa21bd7e2ca78fce2abba3029216a747a5689fe0e45`,
`d54e9ad911f7523b0d5f93add7f79ac597cdec7e40085b3070b2334a8592e1f7`,
and `905bb90c9657106cbb7976a004879fb341c37f253a93b2a558902549ca628c12`.
Those exact files remain unchanged. This package copies their complete
proofs and chooses the counted online bit controller reproduced in full
in critical_third_cache_l2_controller.md Section 10. The fixed L2 source
hash and complete algorithm are given in Section 8.8. The resource review
record sol_review.md, version SHA-256
`6e0312b87d66540c7c0137dc14577abda6d51cc3e801ab241f9534dc131c7599`,
contains its independent audit. The proofs here establish the result
without using that verdict as a premise.

The earlier arithmetic intermediate was critical_third_fast.md, SHA-256
`fc12617ab2c89abcb28936e1e785555779944f696c01615d976d17924910bd49`.
Its fast-arithmetic source critical_third_fast_arithmetic.md has SHA-256
`88fe208d8fb3fa9dbf167af8a8a2283aa3c4d9c38c4b606c0150317929f25c26`.
The complete prior global-clock package critical_third_clock.md, SHA-256
`1c5b0fe6e83e2aad077c6c01fe18bbd810d590765ee57cdcedf7856f70284ef7`,
and selector critical_third_clock_selector.md, SHA-256
`87482c100f2dd597389d5fbcb1a16a032a30d4619599a9e24416c703939ce1ba`,
supply the copied QND, compiler, selector, endpoint and attribution structure.
The phase-cache construction below replaces its repeated modular products.

The material binary-prefix/saved-phase idea is from the public note for
submission `493303b5-06f6-4ee0-9596-d8cae89c8bb4`,
[Exact one-third tolerance with cached phase comparisons](https://api.yukon.org/api/submissions/493303b5-06f6-4ee0-9596-d8cae89c8bb4).
The exact note read has SHA-256
`5aeeec4b4dcd3c563a6abfc7688b2a3bdbfa3e25c8fee221983b4c3f63c82d41`.
At the bounded source lookup on 2026-11-06 23:13 UTC, its full proof and commit
were unpublished. The later reported public commit is
`d1d5a491f9b908ada5de2c7937fdf4732aede43d`. The material source actually read
for this construction remains the exact note above. No unread proof or review
verdict is used as a premise.
That note is credited for the prefix/cache proposal. After this local
construction was complete, Sections 4 and 10 of the public
[peer proof](https://github.com/Layr-Labs/dcp/blob/d1d5a491f9b908ada5de2c7937fdf4732aede43d/submission/proof.md)
were read for attribution. Its exact SHA-256 is
`e659fd631482bac4d1977d0463d9951df6eaf8ec325e811c45e7646f71687074`.
That proof credits ROB-G2, submission `55a6ce76-34af-468f-b735-a1197f3d3459`,
for uniform phase tests, classical prefix words, coherent truncated phase
accumulation and counted constant-table lookup. This is an indirect credit;
the ROB-G2 proof was not read for this package. The peer also credits R24,
`f892f7ea-957b-4dde-8374-dab2736231d0`, for the bounded cubic witness, coarse
classes, answer copying/undo and endpoint. The direct R24 source read and
hash are recorded below. These earlier primitives are prior work.

The local construction
retains prefixes coherently, uses identical fresh/saved C_E maps, and proves
the full marginal-bank, fixed-tournament and cache-boundary arguments here.
The prior global-clock selector was complete before that note was read.

The phase source critical_third_phase_cache.md has final SHA-256
`7e3811e6b06023d3a7094fd476503f69c4ce9a1ed9dab4f8efd5c476e8e989ad`.
Its proof was reviewed at SHA-256
`669d87ae991b6e1ccea59da314c53fb7485a07e5dec2bb212f034fe95b9c459d`;
its statistical and controller review records respectively have SHA-256
`7318a50c42667fe1c3fd5d0f538daf363def20546185d7ca3f1f9d62e2f236a4` and
`2e2f8c57920c0d68e71444a7143caee072441ae67828437f5c0b2e32f333040f`.
The complete phase map, error proof, score, cache implementation and boundary
are reproduced in critical_third_cache_l2_phase.md. The quadratic ordinary
controller source critical_third_controller_resources.md has SHA-256
`25f5bbbefed19f2274decf10eb8812f2cf205362741fb52ec98b86b9461b04bc`;
it was reviewed at `60920387ee118aadd902491c69f969c8df5205fbad0c007dc6cf609410c0259b`.
Its review record has SHA-256
`8b724ba2e0e8a716810078d3349681dab451615306ab24064d918cef11dff885`.
That proof is included in critical_third_cache_l2_controller.md, with the full
cache-extension charge. These hashes preserve actual source and review
history; the package supplies the full proofs independently of their verdicts.

The exact global-clock selector comes from `critical_third_selector_cost.md`,
current SHA-256
`1cfcac197add3d36a9e74fb59e6956d826af6227e52469db202f82ea0c1d0c37`.
Its complete search, schedule, cap, boundary and resource proof is reproduced
in the packaged appendix `critical_third_cache_l2_selector.md`. The source was
independently audited at hash
`f732cc76fd5b04e07df1fc44e1ec4063b20d03a65d4167b552019c9ec8570818`;
the strategy and controller audit hashes are respectively
`a8c6a2e9c1031166e2a42b2cf8c74d0d6b1e6e01cee608fb8b04bc2221eed7e0` and
`4efa8ea1ddd44a81b6accaa83552acf8cbe5797dc4524bd5d34dcc017fad552e`.
These are provenance records; no review verdict substitutes for the full
proofs in this package. The selector replaces the earlier boosted search.
The source model, fraction, copy count and endpoint are kept from the direct
source; the exact selector changes the time envelope.

The direct source in turn takes the circuit, cubic witness, QND recording,
class tournament, bounded coherent selector, phase compiler, known undo and
endpoint decision from the earlier submission
`f892f7ea-957b-4dde-8374-dab2736231d0`, evaluated at commit
`3f9e53c2a129e9ff95b5d1754dcd5587331fbcf1`. The exact source is
[submission/proof.md](https://github.com/Layr-Labs/dcp/blob/3f9e53c2a129e9ff95b5d1754dcd5587331fbcf1/submission/proof.md),
SHA-256 `c492a4f842e114110805b2de648d1004b12f0367ddbaa9fee8dcb5f3fdf66379`.
That source was read. Its cubic witness, retained-record framework and
endpoint construction are reproduced above; its selector is replaced here.
Exact one-third tolerance is prior work under that source's input model.

The direct accepted source supplies the good-first order and martingale
that extend the earlier circuit to the clean-marginal promise, and the
one-word compiler/controller construction. Sections 3 and 6 reproduce those
arguments. The phase appendix supplies the cached score arithmetic; Sections 4-5 and
the appendix replace the earlier selector. No tolerance
above one third is claimed. These historical statements are outside the atomic resource and tolerance
guarantees in Section 0.

RWT25, submission `3f48c893-2d1b-4e9b-ac9e-e9d318149910`, already gives
one-quarter tolerance under the same clean-marginal promise, including
arbitrary correlations with malformed systems. Its
[exact proof](https://github.com/Layr-Labs/dcp/blob/dd6041a0fc1cfe8c29b2af14c5ffc7b29b18ee75/submission/proof.md)
has SHA-256 `6e83a34c0c2283f0acbfab9bf523accebec2cdf4f81b2eb5f32706224d78fd47`.
Thus the bank model itself is prior work. The direct accepted source raises
tolerance from one quarter to one third using the earlier cubic-witness
circuit. Its attribution states that RWT25 was first read after that
standalone proof was complete. Section 0 keeps its credited exact structured
error-model wording. RWT25 supplies historical comparison evidence; its
algorithm is not used by this arithmetic improvement.

The prior source credits the reflection-testing and retained-register search
framework to DEV-era RGRST1, [Layr-Labs/dcp pull request 54](https://github.com/Layr-Labs/dcp/pull/54).
This file makes no priority claim for that framework. No result from that
pull request is needed to verify the construction reproduced here.

## 10. Verification

The source phase-cache finite check passed 811076 window identities,
54052 cache-error/cleanup cases, 311512 linear-phase pairs and 155756 role swaps,
including 2560 actual 32-bit cache words through 1024 input bits. The selector's
finite check passed 544522 boundary words, 1089044 inverse checks, 5582 archive
transitions, 544522 copy/swap checks, 36350 guards and 69 cutoffs. These checks
support the all-word algebra and construction. They do not replace the proofs.
