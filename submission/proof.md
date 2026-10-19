# FD2: bounded flat-difference sieving for dihedral coset states

## 1. Claim, input, and fixed configuration

For every integer N >= 2 and every fixed s in Z/NZ, write n=ceil(log2 N).
The input source supplies independent copies of

    rho_s = (1/N) sum_(x=0)^(N-1) |psi_(x,s)><psi_(x,s)|,
    psi_(x,s) = (|0,x> + |1,(x+s) mod N>)/sqrt(2).

Only these mixed states are supplied. The algorithm has no control over the
source, inverse source circuit, accessible purification, or hiding-function
oracle. Its output is the entire integer secret in [0,N). All success
probabilities below are unconditional over the specified source and all outcomes;
no guarantee for an adversarial replacement source is asserted.

FD2 is the single algorithm specified in Sections 2--10 with the following
parameters, recomputed from N. All logarithms in parameter definitions are base 2.
`clog(q)=ceil(log2 q)` is computed as the bit length of q-1, not by floating point.

    m = floor(log2 N), b = ceil(sqrt(n)),
    ell = ceil((m-1)/(b+1)), with ell=0 when m=1,
    J = m-1-ell,
    M = 8192 clog(128(n+1)),
    F = 2^(b+8)(n+1)^2 + 16M,
    L_i = 32^(ell-i) F, 0 <= i <= ell,
    R = 8(n+1)L_0,
    A_coin = clog(256R),
    M_src = 8192 clog(1024R(n+3)),
    k_verify = n+8.

The integer square root and these counters are computed by bounded ordinary
binary arithmetic. They depend on N only. Every abort returns the n-bit encoding
of zero after releasing its registers. The program has defined behavior on every
measurement string, including strings of probability zero.

The theorem is that FD2 recovers s with probability at least 2/3 and, jointly on
every execution branch, has the following uniform upper-bound envelopes:

    T(N,s) = O(R(n+1)^5 + L_0(n+1)^4 + (2^ell+2)(n+1)^4 + 1),
    S_C(N,s) = O((n+1)L_0 + (n+1)^2 + 1),
    S_Q(N,s) = O(L_0+n+1).

In particular the respective uniform bit-length envelopes are

    B_T(n) = (n+1)^8 2^(6 ceil(sqrt(n))),
    B_C(n) = (n+1)^3 2^(6 ceil(sqrt(n))),
    B_Q(n) = (n+1)^2 2^(6 ceil(sqrt(n))).

Constants are absolute and independent of N, s, outcomes, and memory contents.
T includes classical bit work, gate generation, addressing, all input copies,
quantum gates, measurements, initialization/reset, failures and final output.
S_C and S_Q include every allocated accessible bit/qubit, saved sample, table,
scratch register, input register and retained instruction description. These
bounds are for the same program and parameter choice, not three separate runs.
Their exact growth indices are all 1/2 (canonical strings numerator "1",
denominator "2"); Section 12 proves this. No optimality, novelty, polynomial
space, dominating improvement, or 2^O(n^(1/3)) work claim is made.

## 2. Exact reversible operations on the entire encoded domain

Use temporary arithmetic width w=n+2. A Boolean ripple adder with initial carry
c_0 in {0,1} is the following fixed loop for i=0,...,w-1:

    p_i = a_i XOR b_i
    z_i = p_i XOR c_i
    g_i = a_i AND b_i
    h_i = p_i AND c_i
    c_(i+1) = g_i XOR h_i.

Here g_i and h_i are mutually exclusive. Truth tables prove the sum and carry
identities, and induction proves the w-bit sum and final carry. Retain all
intermediate Boolean wires until reversal. SUB(X,C) means this same ADD loop on
X and the bitwise complement of the w-bit C, WITH INITIAL CARRY ONE. It returns
(X-C) modulo 2^w and final carry [X>=C]. This also holds at C=0: the complemented
zero plus carry-in represents 2^w. Replacing it with the wrapped constant
(-C mod 2^w) and carry-in zero would give the wrong comparison when C=0 and is
not the FD2 schedule. A Boolean MUX(control,x,y) is

    y XOR (control AND (x XOR y)).

To add a known c in [0,N) conditionally modulo N, let X be the n-bit input,
zero padded to width w, and let B be the quantum control bit. Compute

    (_, geN) = SUB(X,N)
    active = B AND NOT(geN)
    (S,_) = ADD(X,c,0)
    (D,ge) = SUB(S,N)
    V = MUX(ge,D,S)
    out = low_n_bits(MUX(active,V,X)).

On X<N and B=1 this is X+c mod N. On B=0 or X>=N it fixes X. The inverse uses

    (_,geN) = SUB(Y,N)
    active = B AND NOT(geN)
    (D,gec) = SUB(Y,c)
    (P,_) = ADD(Y,N-c,0)
    V = MUX(gec,D,P)
    out = low_n_bits(MUX(active,V,Y)).

For Y<N this selects Y-c or Y+N-c and is the inverse; on invalid encodings it
is identity. The formulas include c=0 and N=2^n. All sums used in comparisons
are below 2^w. Wrapped subtraction outputs are used only under the appropriate
comparison/MUX. Thus the maps are mutually inverse permutations on ALL n-bit
encodings, not just on the valid residues.

Each ADD/SUB has five Boolean gates per bit before constant simplification;
three arithmetic loops and the MUXes use fewer than 100w Boolean gates per map.
Compute each Boolean output into a fresh clean wire, XOR the final n output bits
into a target, and reverse the Boolean schedule. This implements an XOR oracle
with clean scratch. To implement the in-place permutation f, XOR-compute f(X)
into clean Y, swap X,Y, and XOR-compute f^-1(X) into Y. The latter clears old X.
This proves scratch cleanup on every basis state; linearity proves the unitary
on superpositions. The control B is preserved.

NOT, CNOT and Toffoli implement the Boolean computations exactly. Toffoli has an
exact constant-size Clifford+T realization: for bits a,b,c,

    4abc = a+b+c -(a XOR b)-(a XOR c)-(b XOR c)+(a XOR b XOR c).

Applying T or T-dagger to these seven parities, computed/uncomputed by CNOT,
implements CCZ exactly. Conjugating its target by H implements Toffoli. Eight
bit assignments prove the identity exhaustively; there is no residual relative
or global phase. One reused parity ancilla suffices. Generous bounds of 100000w
elementary gates and 1000w scratch qubits cover a controlled permutation.

The controller streams this finite pattern using bit position, Boolean-operation
index and a constant number of block bases. It stores no circuit list. Classically
known wire addresses are computed by ordinary binary arithmetic. Section 11
charges their full bit cost. In particular, this construction supplies controlled
cyclic shifts U^c on valid data, U|x>=|x+1 mod N>, and controlled subtraction for
Section 10. It assumes no unit-cost quantum lookup or arithmetic oracle.

## 3. A finite rational phase decoder

Let dist be circular distance on R/Z. The fixed table `evidence/phase_grid.json`
contains rational coordinates for the 64 points exp(2*pi*i*r/64), with denominator
2^16. Each coordinate has absolute error <2^-16. The table is fixed independently
of N and s. FD2 generates it once by the finite rational schedule in
`evidence/rational_grid_certificate.py`, charging its entire finite generation
work and allocated memory. The included JSON is reproducibility evidence, not
an uncharged preloaded input. Here is a
self-contained error justification for its specified generator.

For q=5 and 239, sum the first 20 alternating terms of atan(1/q), obtaining a
lower bound; adding the next term gives an upper bound. Machin's identity
pi=16 atan(1/5)-4 atan(1/239) gives rational bounds p_lo,p_hi with width <2^-90
and 3<p_lo<p_hi<22/7. To prove the identity, tan(2 atan(1/5))=5/12 and
 tan(4 atan(1/5))=120/119. Subtracting atan(1/239) gives tangent one, and the
angle lies in (0,pi/2), hence is pi/4. At each argument 2r(p_lo+p_hi)/(2*64),
sum 60 sine or cosine Taylor terms. Its magnitude is below seven; remainder
bounds are respectively 7^121/121! and 7^120/120!, both <2^-200. Replacing pi by
the interval midpoint contributes <2*(p_hi-p_lo) per coordinate. Rounding to
16 fractional bits contributes <=2^-17. Their sum is <2^-16. The certificate
checks these strict inequalities using rational integers and fractions only.

Given empirical means x,y in [-1,1], select the smallest grid index r minimizing
squared Euclidean distance to the rational table point; return alpha=r/64. All
comparisons are exact rational comparisons. If x,y approximate cos(2*pi*theta),
sin(2*pi*theta) within 1/32 each, empirical-vector error is <=sqrt(2)/32. A true
grid point is within chordal distance pi/64 of the true point. Triangle
inequalities for nearest approximate-grid selection give chordal error at most

    p_hi/64 + 3/32 + 3/65536 < 1/4,

using sqrt(2)<3/2. A chord at circular distance d is 2 sin(pi*d)>=4d for
0<=d<=1/2, so dist(alpha,theta)<1/16. This decoder has no real-arithmetic,
angle-estimation, or synthesis oracle.

The following exact rational unwrapping routine is used twice. Given
alpha_0,...,alpha_H estimating 2^h theta modulo one, set z_H=alpha_H. For
h=H-1,...,0 choose, modulo one, from

    z_(h+1)/2, (z_(h+1)+1)/2

the candidate circularly closer to alpha_h, taking the smaller rational on a tie.
If every dist(alpha_h,2^h theta)<=eta=1/16, induction proves

    dist(z_h,2^h theta) <= eta*2^(-(H-h)).

The true nearby preimage has distance <=3eta/2 from alpha_h; the other has distance
>=1/2-3eta/2. These are strictly separated. The nearby preimage halves the prior
fine-scale error. This argument uses circular distance, so it includes wraparound
at zero. All numerators and denominators have O(H+1) bits.

For completeness, the concentration estimate used below is elementary. If
X in {-1,1}, the second derivative of log E exp(t(X-E X)) is a tilted variance,
which is <=1. Its value and first derivative vanish at zero, giving an upper
bound t^2/2. Independence and Markov, optimized over t, then give

    Pr(|sample_mean-E X|>epsilon) <= 2 exp(-M epsilon^2/2).

At epsilon=1/32 the bound is 2 exp(-M/2048).

## 4. Source-only phase labels without an arbitrary-modulus QFT

For analysis define omega=exp(2*pi*i/N),

    chi_y = (1/sqrt(N)) sum_x omega^(-yx)|x>,
    q_y = (|0>+omega^(sy)|1>)/sqrt(2), Q_y=|q_y><q_y|.

Direct expansion of matrix entries gives

    rho_s = (1/N) sum_(y=0)^(N-1) Q_y tensor |chi_y><chi_y|.

Indeed the cross entry indexed by x,z sums omega^(y(z-x-s)), which vanishes
unless z=x+s mod N, and the diagonal blocks agree as well. Also U chi_y=omega^y
chi_y. This is an ensemble identity for the given mixed state; it supplies no
accessible hidden register or additional source operation to the algorithm.

For each h=0,...,n+2, do M_src Hadamard tests of controlled U^(2^h) on the source
DATA register in X, and M_src such tests in Y. Use a fresh/reset ancilla in |+>
for every test. Conditional on latent y in the exact ensemble, the means are
cos(2*pi*2^h*y/N), sin(2*pi*2^h*y/N). The data register remains chi_y; the first
source qubit is untouched. Hence these test outcomes are independent conditional
on y. U^(2^h) is the exact controlled addition by 2^h mod N of Section 2.
Measuring Y means S-dagger then H then a computational-basis measurement;
measuring X means H then that measurement. No approximate rotation is invoked.

Decode the two empirical means at each h by Section 3, then unwrap with H=n+2.
If all means are accurate, the estimate of y/N has circular error
<=1/(16*2^(n+2))<1/(2N). Round N times the estimate to the nearest integer modulo
N (smaller integer on a tie). Report that integer as y_hat and retain the first
source qubit. Dispose/reset the data and ancillas.

For every latent y, the probability that y_hat differs from y is at most

    delta_src = 4(n+3) exp(-M_src/2048) < 1/(256R).

For the last inequality, let A=1024R(n+3), use M_src>=8192 log2 A and ln(2)<1:
exp(-M_src/2048)<=A^-4. The stated inequality follows immediately for R>=1.
The retained qubit, conditional on the latent y, is exactly q_y, even if the
reported label is wrong. We make no perfect-label assertion for this physical
extractor.

An ideal analysis may instead report the latent y. Couple it to the actual
extractor using the exact ensemble and the same test outcomes. Until a wrong
label occurs, their retained classical/quantum states coincide after local test
records are discarded. There are at most R label extractions; a conditional
union bound gives total divergence probability <1/256. This is a proof coupling,
not coherent source access or conditioning the algorithm on an unobservable
correctness event. All later ideal-label arguments are transferred with this
additive error bound.

## 5. Exact flat-difference instrument and safe deletion of old labels

Suppose a stage has the product classical/quantum input ensemble with labels
u independent uniform in [0,B), B a power of two, and conditional qubits q_(A*u).
Choose a,c>=0 with M0=B/2^(a+c) an even integer. Uniquely decompose

    u = r + 2^a(v + M0*h),
    0<=r<2^a, 0<=v<M0, 0<=h<2^c.

The bucket key is (r,h), leaving a middle label v. Condition on the complete
bucket vector for the input list. The middle labels remain independent uniform
in [0,M0). Stable-sort records by bucket and original list position ONLY, then
pair consecutive records in each bucket. Never sort or pair by middle values.
The evidence gives an explicit counterexample to that invalid optimization.

For two same-bucket inputs u1,u2, apply CNOT (first phase qubit controls second),
measure the second in the computational basis, and proceed only on outcome one.
Its probability is exactly 1/2 for every u1,u2,s. The remaining first qubit is

    [omega^(s*A*u2)|0> + omega^(s*A*u1)|1>]/sqrt(2).

If u1<u2 apply X. Its density matrix is then exactly Q_(A*abs(u1-u2)). Since
buckets match, abs(u1-u2)=2^a*d with d=abs(v1-v2). Thus the retained density
matrix is Q_(A*2^a*d). Histories with the same new record (A*2^a,d) give IDENTICAL
conditional density matrices; the history-dependent scalar is only a global
phase. Consequently erasing the old labels, discarded qubit and local records
cannot add dephasing to this retained conditional state. A dummy unused label
register is not the justification: the exact channel identity is.

Independent uniform v1,v2 have

    Pr(d=0)=1/M0,
    Pr(d=t)=2(M0-t)/M0^2, 1<=t<M0.

Reject d>=M0/2. Keep d=0 with probability one. For 1<=d<M0/2, use the rational
acceptance probability M0/[2(M0-d)]. For every d in [0,M0/2), including zero,
the unconditional classical keep probability assigned to d is exactly 1/M0.
After also including the target-one probability, the SUCCESS component of the
one-pair output instrument is the subnormalized classical/quantum state

    (1/(2M0)) sum_(d=0)^(M0/2-1) |d><d| tensor Q_(A*2^a*d).

Its trace is 1/4. Normalizing gives the uniform new label in [0,M0/2) and its
correct phase qubit. This expression is independent of the bucket key. It proves
both the success rate and the precise retained quantum information.

Disjoint pairs have independent input middle values and operations. Conditional
on the bucket vector, their success flags are independent Bernoulli(1/4).
Conditional on ANY flag pattern, the retained successful records have the product
of the normalized ensemble just displayed. In particular, they remain independent
uniform after conditioning on enough successes and taking the first specified
number in the fixed pair order. Discard all old records before the next stage;
the next program decisions use only the new ensemble, its list positions and
classically known wire addresses. This proves the stage-to-stage invariant by
induction. No claim of a constant success rate conditional on the exact revealed
middle-label vector is needed or made.

This is a bounded heralded-rejection computation. All measurement outcomes and
discarded inputs are included in the program and its failure/work accounting;
there is no free postselection or success conditioned on favorable outcomes.

## 6. Rational coins with a fixed branch bound

For 0<d<M0/2 put D=2(M0-d). Draw clog(D) independent fair bits. If their integer
V is <D, return the coin outcome [V<M0]; otherwise retry. The ideal uncapped
sampler has a uniform accepted V in [0,D), so it implements the required coin.
Each trial accepts the range with probability at least 1/2. Generate each fair
bit with H and measurement on a reset qubit if the controller lacks native
random bits; all gates and resets are charged.

The ACTUAL program allows at most A_coin trials, then aborts the whole algorithm.
For any D and any past history this abort probability is <=2^(-A_coin). There
are fewer than R coins: at most (J+1)/2 times sum_(i<ell)L_i, and
sum_(i<ell)L_i <= (32/31)L_0. Thus union probability is <=1/256.
Couple actual coins to the ideal uncapped sampler until the first cap is hit.
Apply Section 5 in the ideal model, and transfer with this additive error.
Conditioning on no cap is NOT used to assert exactly uniform labels, because
cap probabilities can depend on D. No unbounded sampler exists in the actual
program.

## 7. All-modulus schedule and explicit batch algorithm

Restrict an ideal initial y uniform in [0,N) to y<2^m. Qualification probability
is 2^m/N>=1/2, and qualified labels are exactly uniform in [0,2^m). This does not
change their phase denominator N.

Partition m-1 into positive integers d_i: repeatedly take min(b+1,remaining)
until the remainder is zero. There are ell parts. Let l_i=d_i-1, so
sum_i l_i=J. For each target exponent j=0,...,J separately, distribute j low bits
greedily: a_i=min(l_i,still_needed), subtract it from still_needed, and set
c_i=l_i-a_i. These are fixed functions of N and j.

The batch for exponent j is the following finite program:

1. Acquire exactly 8L_0 source copies using Section 4. Keep the first L_0 phase
   qubits whose reported labels are <2^m; discard/reset the rest. If fewer than
   L_0 qualify, release the batch and abort with zero. Start A=1, B=2^m.
2. At stage i, use exactly L_i input records. Compute the keys and stable-sort
   by key and original position. Pair in order within each key; reset unmatched
   qubits. Process every pair by Sections 5 and 6, keeping the first L_(i+1)
   successes and disposing of extras. On a shortage abort. Replace
   A by A*2^a_i and B by B/2^(l_i+1), erase old records and release scratch.
3. At the end B=2 and A=2^j. Keep the first 2M label-one qubits; dispose of the
   rest. Abort if there are too few. These are copies of q_(2^j). Measure M in
   X and M in Y; decode their empirical means to alpha_j by Section 3.
4. Release that batch before starting the next j. Save only alpha_j.

At every stage the coefficient-domain bit length drops by d_i, and the multiplier
increases by 2^a_i. Therefore final B=2 and A=2^j as stated. Moreover A*B starts
at 2^m<=N and changes to A*B/2^(c_i+1); integer frequencies never need to be
reduced modulo a fictitious power-of-two modulus. The phase denominator is always
the original N. This handles odd and composite N without a hidden subgroup
restriction or an arbitrary-modulus Fourier-transform assumption.

If m=1 then ell=0, J=0 and B already equals two; no stage is run. Thus the
configuration includes N=2 and 3. In general J>=0 and ell<=b-1 because
m-1<=n-1<=b^2-1=(b-1)(b+1).

## 8. Batch shortage probabilities and conditioning

For a Bernoulli sum Z of mean mu, independence and 1+t<=exp(t) give
E exp(-tZ)<=exp(mu(exp(-t)-1)). Markov with t=ln(2) shows
Pr(Z<=mu/2)<=exp(-mu/8). With t=ln(4), threshold mu/4 gives <=exp(-mu/4).

Analyze ideal labels and ideal uncapped coins first. Initial qualification count
has mean >=4L_0; a shortage has probability <=exp(-L_0). Its indicators are
independent of the qualified label values, so the first L_0 qualified values,
conditional on availability, are independent uniform in [0,2^m).

Stage i has K_i=2^l_i buckets. At most K_i records are unmatched, so it has
P_i >= (L_i-K_i)/2 >= L_i/4 pairs, since L_i>=2K_i. Conditional on the bucket
vector, Section 5 gives a binomial success count of mean P_i/4>=L_i/16.
A shortage below L_(i+1)=L_i/32 therefore has probability <=exp(-L_i/128).
The exact instrument law preserves the product-label invariant conditional on
availability. Hence this argument applies successively; it does not condition
on the exact input label values or assume that individual realized pairs always
have success probability 1/4.

At the final selection, F independent labels in {0,1} give mean F/2 ones.
F>=16M, so fewer than 2M ones has probability <=exp(-F/16).
A union bound on each first failing shortage, over all batches and stages, is
at most

    2(n+1)^2 exp(-F/128) < 1/256,

using F>=512(n+1)^2. For example, with x=n+1>=2, the left side is at most
2x^2 exp(-4x^2) <=2^(1-3x^2)<=2^-11<1/256.

Conditional on a successful batch, its selected qubits are the product of 2M
copies of q_(2^j); the batch-success flags carry no residual bias in these
states. Section 3 and Hoeffding give

    Pr(all batches available AND any outer phase estimate is bad)
       <=4(J+1) exp(-M/2048) <1/256.

This is an intersection-event bound. It does not falsely claim estimates exist
on branches that already aborted. The last inequality follows with
A=128(n+1) and exp(-M/2048)<=A^-4.

Transfer the ideal execution to the actual source extractor and capped coins
by the two couplings. Their error probabilities are each <=1/256. No
independence between these errors and the shortages is assumed.

## 9. Coarse phase reconstruction and a short exact candidate interval

Apply Section 3's unwrapping routine to alpha_0,...,alpha_J with theta=s/N.
When the outer estimates are good,

    dist(z,s/N) <= 2^(-J)/16.

Generate exactly the integers

    C = { t in [0,N): dist(t/N,z) <= 2^(-J)/8 }.

Use exact rational endpoints and ceil/floor, splitting a circle interval crossing
zero into two ordinary intervals and excluding N. Enumerate only integers in
these intervals, in increasing order. Never loop through all N integers. For
any z, including erroneous estimates, its cardinality is at most

    N/(4*2^J)+2 < 2^ell+2.

This uses N<2^(m+1) and J=m-1-ell. The weak bound <=2^ell+2 is used for resources.
The true s belongs to C on the good event. The all-outcome candidate bound is
important: an erroneous phase estimate cannot produce an unbounded search.

## 10. Full-secret verification and unconditional success

For each candidate t in C, test at most n+8 independent fresh source copies.
On one copy conditionally subtract t on its data register when the FIRST source
qubit is one, using Section 2, then measure that qubit in X. Reject the candidate
at its first minus; output the first candidate passing all n+8 tests. If none
passes, output zero.

For t=s every source component becomes |+> tensor |x>, so the true candidate
always passes. For t!=s, its two data basis states are distinct for every x;
the first qubit is I/2 and passes with probability 1/2. Fresh source copies
make the all-pass probability 2^(-(n+8)), conditional on any past transcript
that reaches that wrong candidate. Union over at most N candidates bounds any
false early acceptance by N*2^(-(n+8))<=1/256. This verifies the entire secret,
not only parity, and counts failed attempts as well.

There are five bad-event budgets, each <=1/256: a wrong spectral label, a coin
cap, a batch shortage, an outer phase error on an available batch, and a false
verification acceptance. Outside their union, the true candidate is generated,
all earlier wrong candidates fail, and the program returns s. Thus

    Pr(output=s) >= 1-5/256 = 251/256 > 2/3.

No lower bound on a postselected or average-secret success rate is substituted
for this statement. All stage, trial and source limits are fixed beforehand.

## 11. Joint branchwise work and allocated-space bounds

The fixed program's gates are exact Clifford+T. There is no continuous gate
precision parameter. Classical empirical means, table entries, counters, list
indices, addresses and all phase estimates are finite rationals/integers.

Here are useful explicit parameter bounds. Since clog(128(n+1))<=n+7 and
n+7<=2(n+1)^2, the definition gives

    F < 2^(b+18)(n+1)^2,
    L_0 <= 2^18 (n+1)^2 2^(6b),
    R <= 2^21 (n+1)^3 2^(6b).

Thus log2 R<=21+3log2(n+1)+6b=O(n+1), A_coin=O(n+1), and
M_src=O(n+1). Every stored record and address has O(n+1) bits. In particular
addressing cannot be charged as a unit-cost operation on an unbounded word.

A controlled permutation has O(n+1) elementary gates and retained wires by
Section 2. Give each arithmetic macro a block base and constant-stride slots
for its five per-bit Boolean outputs. Each operand address is a block base plus
a constant multiple of the bit position (possibly the preceding position).
Forward and reverse emission therefore use only a constant number of additions
and constant shifts on O(n+1)-bit indices per emitted gate, not a general
multiplication or a search through a stored circuit. The emitted Toffoli parity
pattern has fixed size and reuses one slot. Such index arithmetic takes O(n+1)
Boolean bit steps; charging O(n+1) for access at each step gives O((n+1)^2)
charged bit work per gate. This deliberately conservative schedule costs O((n+1)^3)
charged work per permutation. It stores current instruction/block bases and
counters only. Inputs, constants, comparisons and reversals are included.

A raw source extraction uses 2(n+3)M_src=O((n+1)^2) such tests/permutations;
empirical counters, fixed-grid exact comparisons and unwrapping fit the same
conservative O((n+1)^5) per-copy bound. R extractions therefore cost
O((n+1)^8 2^(6b)). Source acquisition itself costs n+1 per copy and is included.
The rational constant table has fixed finite generation cost, charged once.

For a stage list, stable mergesort costs O(L_i log L_i) comparisons and record
moves. Reading/comparing/moving an O(n+1)-bit record, charging O(n+1) per bit
access, costs O((n+1)^2); log L_i=O(n+1). Sorting is therefore
O(L_i (n+1)^3). Grouping, pairing, integer differences and classical selection
fit that bound. A rational coin has at most O(n+1) range trials, each generating,
addressing and comparing O(n+1) bits, giving O((n+1)^3) per pair. All failures
are counted. Quantum CNOT/X/measurement/reset and all discarded states are
charged as well.

sum_(i<ell) L_i <= (32/31)L_0, so all stages over at most n+1 batches cost
O(L_0(n+1)^4). Initialization, cleanup even on abort, and releasing both current
and output lists fit this bound. Final candidate enumeration has at most
2^ell+2 entries on EVERY branch, each with at most n+8 verification copies and
O((n+1)^3) work per test. Its work is O((2^ell+2)(n+1)^4), smaller than the raw
extraction bound. Retaining the parameter-dependent guarantee gives

    T = O(R(n+1)^5 + L_0(n+1)^4 + (2^ell+2)(n+1)^4 + 1).

Using the displayed parameter inequalities yields O((n+1)^8 2^(6b)),
which is O(B_T(n)). This accounts
for all sequential work, not just query count, circuit depth or expected time.

Only a constant number of lists and a mergesort auxiliary array are needed at
once. Classical list records contain labels, original positions, bucket keys
and known qubit addresses, O(n+1) bits each. Controller, source-estimator and
arithmetic scratch add O((n+1)^2) bits, apart from fixed constant-table
generation space. Hence S_C=O((n+1)L_0+(n+1)^2+1) is within
O((n+1)^3 2^(6b)) and therefore O(B_C(n)).

Sorting moves classical records and known qubit addresses; it does not query a
quantum-addressed memory. A successful output qubit is the surviving first
qubit of its input pair, recorded at its existing wire address; there is no
copy of an unknown quantum state. Discarded phase qubits are measured/reset
and their wire slots reused.

Quantum memory holds at most O(L_0) saved phase qubits, one n+1-qubit source
port, and O(n+1) arithmetic/test ancillas. Reset and reuse released registers;
run batches sequentially. Thus S_Q=O(L_0+n+1)=O((n+1)^2 2^(6b)), hence O(B_Q(n)).
There is no excluded saved input, hidden circuit list or quantum-addressed table.
The source's inaccessible environment is not allocated by this program.

These bounds are structural bounds on finite loops, arrays and gate patterns.
They hold for all secrets and every execution branch, independently of the
probabilistic correctness analysis and whether the algorithm aborts.

## 12. Exact indices of the declared envelopes

For c=8,3,2 let B(n)=(n+1)^c 2^(6 ceil(sqrt(n))). Then

    log2 B(n)=6 ceil(sqrt(n))+c log2(n+1)=Theta(sqrt(n)).

It follows that log2(log2(max(4,B(n))))=(1/2)log2 n+O(1), so the required limsup
is exactly 1/2. The canonical nonnegative rational numerator and denominator
are "1" and "2" for T, S_C and S_Q, in that order. These are indices of the
proved upper-bound envelopes, not lower bounds on actual resource use.

## 13. Information-loss audit against arXiv:2609.40062v1

The comparison is to Gupte--Ragavan--Zhandry, v1 of 30 September 2026,
Theorem 2.1 and Remark 2.3. In its Section 2.1 polynomial-sample setup,
N=2^n. Its prefix starts with m_paper independent uniform labels y_i and their phase qubits. Define
f_y(v)=sum_i y_i v_i modulo N for v in {0,1}^m_paper, and measure
z=f_y(v) modulo N/2 in superposition. The remaining quantum state is
proportional to

    sum_(h=0,1) sum_(v: f_y(v)=z+hN/2) (-1)^(s*h) |v,h>.

If the only retained classical label information is
(H_1(y_1),...,H_m_paper(y_m_paper),z), where each H_i:Z_N->[K] is fixed
independently of secret and samples, the theorem bounds parity-distinguishing
advantage by m_paper*sqrt(K/N), including unbounded downstream computation.
Here advantage means the total-variation distance of output distributions for
opposite parity secrets. Remark 2.3 warns that unused retained labels or delayed
label measurements can have an output-equivalent implementation within the
barrier. This is a constraint to check, not an assumption in FD2 correctness.

FD2 keeps the full current label while selecting pairs, computing their exact
difference, deciding the sign correction and evaluating the acceptance coin.
It performs pairwise quantum operations before deleting old labels. Section 5
proves the entire retained conditional state depends only on the new exact
record, and proves its subnormalized instrument law, rather than arguing from
physical presence of a label register. New records jointly depend on paired
inputs and their channel, rather than being fixed coordinatewise digests
substituted into the paper's unchanged post-measurement state.

The actual program does not perform that global subset-sum-measurement prefix.
We do not claim that this syntactic observation alone proves safety against all
output-equivalent reformulations; the independent channel/invariant and success
proofs above are essential. Nor is a superpolynomial sample count alone claimed
as an escape from the quantitative bound. If a proposed modification admits a
simulation satisfying the theorem's hypotheses with a restrictive bound, its
correctness must be reconsidered. In particular, replacing exact current labels
with bucket keys, dropping middle values before computing differences, or
claiming coherent erasure by ignoring a register is not part of FD2.

The finite counterexample in `evidence/batch_results.json` illustrates a separate
fragility: sorting middle labels changes the conditional output distribution to
57/91 versus 34/91 in a small case. The stable input-order rule is mandatory.
The analytic instrument identity, not that finite diagnostic, justifies FD2.

## 14. Evidence, provenance, and limits

The proof above supplies its arithmetic, quantum channel, probability, resource
and growth-index arguments. No external paper is required to fill an algorithmic
lemma. Auxiliary evidence uses Python's standard library only:

* `evidence/arithmetic_audit.py` checks comparator carry-in, controlled maps on
  valid and invalid encodings, their inverse, compute/swap/inverse-XOR cleanup,
  and all eight assignments of the Clifford+T parity identity.
* `evidence/batch_instrument_audit.py` enumerates finite exact joint laws and
  truncation, and detects the invalid middle-label sorting negative control.
* `evidence/rational_grid_certificate.py`, `phase_grid.json` and
  `grid_certificate.json` specify and certify the fixed rational constants.
* Additional diagnostics, when included, exercise source spectral identities,
  phase unwrapping, candidate coverage, finite label streams and pair-state
  identities. Their floating-point portions are supplementary, not proof steps.

The diagnostic arithmetic program materializes a small Boolean circuit to check
it; FD2's resource theorem uses the streamed loop schedule described here. The
label simulations are classical probability diagnostics, not a full physical
quantum execution. Passing them is not an asymptotic proof, novelty result,
independent expert certification or official benchmark score.

Background references, with no unproved imported resource claim:

1. G. Kuperberg, *A subexponential-time quantum algorithm for the dihedral hidden
   subgroup problem*, SIAM J. Comput. 35(1), 170--188 (2005), DOI
   10.1137/S0097539703436345. Label-guided phase-state pairing is established
   background; FD2 does not claim a new asymptotic DCP breakthrough.
2. O. Regev, *A Subexponential Time Algorithm for the Dihedral Hidden Subgroup
   Problem with Polynomial Space*, arXiv:quant-ph/0406151v1 (21 June 2004).
   FD2 does not claim that paper's polynomial-space tradeoff.
3. G. Kuperberg, *Another Subexponential-time Quantum Algorithm for the Dihedral
   Hidden Subgroup Problem*, TQC 2013, pp. 20--34, DOI
   10.4230/LIPIcs.TQC.2013.20. Its heuristic leading-exponent analysis is not
   used to prove FD2's bounds.
4. A. Gupte, S. Ragavan, M. Zhandry, *A Fourier-Label Information-Loss Barrier for
   Dihedral Coset Algorithms*, arXiv:2609.40062v1 (30 September 2026), specifically
   Theorem 2.1 and Remark 2.3. Section 13 states the relevant hypotheses and
   explains the comparison without requiring an external fetch.

The published SEST-1 submission 525e0659-3635-49da-b055-df06aca45f97 by
mooselumph was consulted through its public note. The elementary final candidate
test, all-encoding reversible permutation strategy and streamed resource
accounting are related to the techniques described there; Sections 2, 10 and 11
reprove everything used here. A dependency declaration for that full submission
UUID accompanies the staged package. The pinned included baseline also supplies exhaustive shift testing; the
separate SEST-1 note was materially consulted for its explicit implementation
and accounting, so it is declared even though the basic final-testing idea is
already in the baseline. No declaration of no dependencies is made. The pinned DCP README.md, rules.md, benchmark.json, verifier.json and
included submission were read at a74599ed97e222c1872e254e36592277ba631935 before
candidate edits. The included baseline proof SHA-256 is a0b90230d34c0b08152ea38e7d9edb9b1009017442a8a35d74c4df13f3ebd9a3.
It already supplies the exhaustive final-testing idea; the SEST-1 dependency is
also declared for its independently consulted implementation/accounting note.
Local mechanical checks and hosted-review status are recorded separately in the
public note, without treating them as mathematical certification.
