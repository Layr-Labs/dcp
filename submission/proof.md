# PG5: lower charged work through a reusable Fourier-gradient register

PG5 directly reuses PG4 submission e40f2d5a-68c9-418b-b4e8-64a80305968e,
its exact Fourier/reciprocal framework and global coin budget, and the earlier
PG3/PG2/MDC1 sources acknowledged in Section 13. The actual integer product
now uses an adaptive radix, with all generated matrices and bit costs proved
in adaptive-arithmetic.md. Its supported time envelope is
O(n^(7/2)2^((244949/100000)sqrt(n)+21sqrt(log2 n))). Other declared resources
and success1019/1024 are unchanged. No earlier verdict is a premise.

The inherited VFD3-M4 foundation is submission
6f4423a3-e180-476f-987a-b1c4cdaa898e, candidate
c3719a087388963198f068135526bd69fe3ab877. Its spectral ensemble,
exact arithmetic, outer decoder, flat-difference instrument and quota proof
are reproduced below. Earlier VFD3/FD2 ancestry remains acknowledged in
Section 13. No prior mathematical verdict is a premise.

## 1. The theorem and the exact algorithm configuration

For every integer N >= 2 and fixed s in Z/NZ, let n=ceil(log2 N). PG5
receives only fresh independent copies of the mixed state in rules.md. It
outputs the entire s with unconditional probability at least 1019/1024.
The same execution has, on every branch, including every abort,

    T(N,s)   = O(n^(7/2) 2^((244949/100000) sqrt(n)+21 sqrt(log2 n))),
    S_C(N,s) = O(n^(3/2) 2^((244949/100000) sqrt(n))),
    S_Q(N,s) = O(n^(1/2) 2^((244949/100000) sqrt(n))).

These asymptotic envelopes apply for n>=2. The n=1 cases are explicitly
handled below and have absolute finite costs. Each envelope has growth
index exactly 1/2. Constants are absolute, independent of N, s, outcomes
and memory contents. They include source calls, classical bit work,
addressing, generated gates, measurements, initialization and all failures.
The structured objects declare these exact envelopes. Both time exponent
coefficients 244949/100000 and 21 are explicitly proved; no unspecified
inside big-O coefficient is replaced by a number.

For n<=16, PG5 exhaustively tests t=0,...,N-1 by Section 10 with k=n+10
fresh tests per candidate. It returns the first candidate passing all tests,
or zero if none passes. This is a fixed finite prefix of the single algorithm.
It does not run the sieve or generate the phase table.

For n>=17 put h=n+1, m=floor(log2 N), and define the following integers.
`clog(x)` is the bit length of x-1. Square-root comparisons use exact integers.

    ell = min{u>=1 : 3*u*u-u >= 2*(m-1)},
    J = m-1-ell,
    lambda = clog(1024*h),
    M = 8192*lambda,
    F = 1048576*lambda,
    L_i = F*(2*8^t-4^t)+t*8^t, t=ell-i, i=0,...,ell,
    R = 4*(J+1)*L_0,
    global_coin_trial_limit = 4*R,
    a = clog(2^20*R),
    t_phase = n+a+4,
    k = n+10.

The depth ell is computed by binary search over [1,m-1] with exact integer
comparisons. This interval is nonempty and its upper endpoint satisfies the
inequality for m>=16. Thus ell<=m-1, J>=0, and by definition

    m-1 <= (3*ell^2-ell)/2.

This is exactly the capacity condition needed below. Put c=244949/100000.
An exact integer comparison gives 244949^2=60000012601>60000000000,
so c>sqrt(6). Let v=ceil(sqrt(2*n/3))+1. Then v<=sqrt(2*n/3)+2 and
(3*v^2-v)/2>n>=m-1. Minimality therefore gives

    ell <= sqrt(2*n/3)+2 <= (c/3)*sqrt(n)+2.

Conversely m>=n-1 and the capacity condition imply
ell>=sqrt(2*(n-2)/3). Consequently ell=Theta(sqrt(n)). These inequalities
hold for all n>=17, not merely for tested input lengths. Every choice of
ell below is this minimum for the actual input m, not a rounded rational
slope. The rational c is only a strictly larger supported envelope coefficient.

Set remaining=J and, in increasing i, set

    b_i = min(3*(ell-i-1), remaining),
    remaining -= b_i.

The capacity inequality implies remaining finishes at zero. Hence
sum_i b_i=J and 0<=b_i<=3*(ell-i-1). For each separate target j=0,...,J,
set need=j and then a_i=min(b_i,need), need-=a_i, c_i=b_i-a_i. Thus
sum_i a_i=j. These choices do not depend on random outcomes.

Every abort outputs the n-bit encoding of zero and releases its workspace.
All loops, allocations and return values are defined on every measurement
string. No unbounded repetition, favorable-outcome conditioning, oracle,
instance-dependent advice or uncharged preparation is part of PG5.

The contribution is an explicit schedule and sharpened joint bound for a
known type of sieve, not a claimed new DCP growth index or the cube-root
goal. Sections 2, 3 and 5 adapt the self-contained foundations of public submission
286f74f7-dd46-4db7-9fe2-031755c76a04 (FD2), candidate commit
773a35a977a66bbe10fa6f8f6ea50c2021f0fba0. That inherited material source remains acknowledged; it is outside the
current challenge attribution scope. The direct reused submission here is
VFD3-M4, named above and declared with this submission.
Acceptance of that submission is not a premise: the needed arguments are
included here, and all new claims require their own review.

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
not the PG5 schedule. A Boolean MUX(control,x,y) is

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
of N and s. PG5 generates it once by the finite rational schedule in
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

## 4. Source-only phase labels through binary phase estimation

For analysis define omega=exp(2*pi*i/N),

    chi_y = (1/sqrt(N)) sum_x omega^(-yx)|x>,
    q_y = (|0>+omega^(sy)|1>)/sqrt(2), Q_y=|q_y><q_y|.

Direct expansion of matrix entries gives

    rho_s = (1/N) sum_(y=0)^(N-1) Q_y tensor |chi_y><chi_y|.

Indeed the cross entry indexed by x,z sums omega^(y(z-x-s)), which vanishes
unless z=x+s mod N, and the diagonal blocks agree as well. Also U chi_y=omega^y
chi_y. This is an ensemble identity for the given mixed state; it supplies no
accessible hidden register or additional source operation to the algorithm.

The actual PG5 extractor is specified in phase-labels.md and fast-labels.md.
Its phase and shared gradient registers both have t_phase=n+clog(2^20 R)+4
bits. A counted reciprocal is generated once, then exact coherent modular
translation implements all powers together. The binary inverse Fourier
transform is exact in the ideal-gradient analysis, using recursive product
phases implemented with clean reversible adaptive multiplication and
additions into the appropriate top bits of the shared gradient. No Fourier
phase is truncated. Measured-residue rounding uses the same explicit fast
integer product. All data permutations extend to invalid encodings, and no
source inverse, QRAM or arithmetic/Fourier oracle is assumed.

Exact ideal QPE has label-error probability less than 1/(2^23 R) per source.
Its union across R acquisitions is less than 2^-23. Actual bounded gradient
preparation contributes input trace distance less than 2^-36 and abort less
than 2^-122. The global channel comparison costs less than 1/1024 in total.
Only the ideal gradient is assumed unchanged; actual errors are not refreshed
or declared independent. The first source phase qubit is retained. Every required circuit identity and charged bit algorithm is in
phase-labels.md, fast-labels.md and adaptive-arithmetic.md.

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

## 6. Exact coins with one global finite trial cap

For 0<d<M0/2 put D=2(M0-d). Draw clog(D) fair bits V; if V<D return [V<M0],
otherwise retry. This ideal uncapped sampler gives the rational acceptance
probability in Section 5; every trial completes with probability at least 1/2.
Fair bits use H and computational measurement on reset qubits. PG5 uses ONE
trial counter across all batches, initialized to zero before the first batch.
At most 4R trials are permitted globally. If another trial would be required,
abort the whole algorithm and output zero. Deterministic work after the final
allowed completed trial remains permitted. No individual coin has an extra
unbounded loop: the shared cap bounds every branch and all draws.

The unchanged quota sums imply fewer than R coins in total. Coupling to ideal
coins until global-budget abort, the probability of needing more than 4R trials
is at most exp(-R/4)<1/1024: each trial's completion indicator conditionally
dominates an independent fair Bernoulli, so fewer than R completions in 4R
trials is bounded by the binomial Chernoff tail. fast-labels.md Section 6
supplies the complete adaptive coupling and finite-size threshold proof.
This replaces the former per-coin cap and its error budget, not an additional
unaccounted retry. Never condition on no cap and assert the ideal coin law;
transfer that law by the additive global coupling instead.

## 7. Variable-width batches and the complete sieve

An ideal initial label y uniform in [0,N) qualifies if y<2^m. This has
probability 2^m/N>=1/2; conditional qualified labels are uniform in [0,2^m).
Their phase denominator stays N. Generate the rational table of Section 3
once, with its fixed generation cost counted. Prepare the single gradient of
phase-labels.md once, before any source acquisitions, counting all capped
attempts. If this preparation aborts, output zero.

For each j=0,...,J, independently, do the following in order.

1. Obtain exactly 4L_0 source copies and their reported phase labels by
   Section 4. Keep the first L_0 qualified qubits. Discard any others and
   abort if fewer qualify. Initialize A=1 and B=2^m.
2. For each i=0,...,ell-1 use exactly L_i records. Apply the bucket rule
   of Section 5 with a=a_i, c=c_i and M0=B/2^b_i. Pair only by bucket and
   original input position, never by middle value. Reset unmatched qubits.
   Process all pairs in that fixed order. Use Section 6's capped coin.
   Retain the first L_(i+1) successes and discard extras. Abort on shortage.
   Replace A by A*2^a_i and B by B/2^(b_i+1). Erase old records and scratch.
3. Now A=2^j and B=2. Keep the first 2M label-one qubits, aborting on
   shortage, and discard the rest. Measure M of them in X and M in Y;
   Section 3 gives alpha_j. Release this batch and retain only alpha_j.
4. After the last batch, use Sections 9 and 10 to reconstruct and verify s.

To check the parameters of every stage, its width is
w_i=m-i-sum_(t<i)b_t. Then

    w_i-b_i = 1+(ell-i)+sum_(t>i)b_t >= 2.

In particular M0 is an even power of two of at least four. The final width is
m-ell-J=1. The intermediate frequencies A*u are always ordinary integers:
A*B starts at 2^m<=N and decreases by 2^(c_i+1) at each stage. No reduction
modulo a fictitious power of two, or promise that N is even, is used.
The construction therefore includes odd N and arbitrary composite N.

The number of buckets at stage i is

    K_i=2^b_i <= 8^(ell-i-1) <= L_(i+1)/F.

This shrinking bucket budget permits explicit per-level shortage margins.
The quotas replace a blanket factor-32 loss with a proved, smaller allocation
that covers both unmatched bucket entries and random fluctuations.

## 8. Uniform laws, shortages, and the probability budget

For a sum X of independent Bernoulli variables of mean mu, the elementary
Chernoff bound is

    Pr(X <= (1-delta)*mu) <= exp(-mu*delta^2/2), 0<delta<1.

One proof uses E exp(-tX)<=exp(mu*(exp(-t)-1)), Markov's inequality,
t=-ln(1-delta), and
(1-delta)*ln(1-delta)+delta >= delta^2/2. The last inequality follows
by differentiation, with equality at zero. This needs no asymptotic
independence assumption beyond the product laws actually proved.

First analyze exact latent source labels and ideal uncapped coins.
The initial qualification count has mean at least 2L_0, so a batch's
initial shortage probability is <=exp(-L_0/4). Qualification indicators
are independent of the conditional qualified values. Keeping the first
L_0 values, conditional on enough of them, preserves their iid uniform law.

At stage i put t=ell-i>=1 and r=L_(i+1). At most K_i records are
unmatched, so the number P of pairs is at least (L_i-K_i)/2. Conditional on
the complete bucket vector, Section 5 gives independent Bernoulli(1/4)
successes, with mean mu=P/4. The exact quota identity is

    L_i - 8r = F*4^t + 8^t.

Using K_i<=8^(t-1), this gives

    mu-r >= F*4^t/8 + (7/8)*8^(t-1) > 0,
    mu <= L_i/8 <= 8^(t-1)*(2F+t).

If 1<=t<=F, then 2mu<=6F*8^(t-1), and therefore

    (mu-r)^2/(2mu) >= (F*4^t/8)^2/(6F*8^(t-1))
                   = F*2^t/48 >= F/24.

If t>F, then 2mu<=6t*8^(t-1), and therefore

    (mu-r)^2/(2mu) >= 49*8^(t-1)/(384t) >= 49t/384 > F/24.

Here 8^(t-1)>=t^2 for every integer t>=1: it holds at one and is preserved
because 8t^2>=(t+1)^2. Chernoff consequently gives the same uniform bound

    Pr(stage shortage | bucket vector) <= exp(-F/24).

The exact successful instrument in Section 5 proves that, conditional on
any success-flag pattern, the retained labels are independent uniform
with the correct conditional qubits. Conditioning only on availability
and retaining a specified prefix therefore preserves that product law.
This justifies the next stage inductively. We do not condition on the
fully revealed middle labels and then pretend success remains 1/4.

At the end, F iid binary labels yield mean F/2 ones. Since
F/M=128>=8, a shortage of 2M ones has probability <=exp(-F/16).
There are at most h batches and at most h+2 shortage checks per batch.
Every such probability is bounded by exp(-F/32); therefore

    Pr(any first shortage)
        <= h*(h+2)*exp(-32768*lambda) < 1/1024.

For the strict last inequality use exp(-x)<=2^(-x),
2^lambda>=1024h, and h>=18. These enormous constant margins are for a
simple rigorous finite-size proof, not a practical runtime estimate.

For outer phase measurements, the probability that all batches are available
but any required empirical mean is inaccurate is at most

    4*(J+1)*exp(-M/2048)
       <= 4h*(1024h)^(-4) < 1/1024.

This is an intersection-event bound; no estimate is asserted to exist on
an aborted branch. Transfer the ideal execution to the physical program by
Section 4's source-label coupling and Section 6's coin coupling. Their
failure probabilities are each <=1/1024. They need not be independent of
shortages or of phase-estimation errors.

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

For each candidate t in C, test at most n+10 independent fresh source copies.
On one copy conditionally subtract t on its data register when the FIRST source
qubit is one, using Section 2, then measure that qubit in X. Reject the candidate
at its first minus; output the first candidate passing all n+10 tests. If none
passes, output zero.

For t=s every source component becomes |+> tensor |x>, so the true candidate
always passes. For t!=s, its two data basis states are distinct for every x;
the first qubit is I/2 and passes with probability 1/2. Fresh source copies
make the all-pass probability 2^(-(n+10)), conditional on any past transcript
that reaches that wrong candidate. Union over at most N candidates bounds any
false early acceptance by N*2^(-(n+10))<=1/1024. This verifies the entire secret,
not only parity, and counts failed attempts as well.

For n>=17 there are five bad-event budgets, each <=1/1024: a wrong spectral label, a coin
cap, a batch shortage, an outer phase error on an available batch, and a false
verification acceptance. Outside their union, the true candidate is generated,
all earlier wrong candidates fail, and the program returns s. Thus

    Pr(output=s) >= 1-5/1024 = 1019/1024 > 2/3.

No lower bound on a postselected or average-secret success rate is substituted
for this statement. All stage, trial and source limits are fixed beforehand.

For the n<=16 exhaustive branch the true candidate is in the enumerated
set and the only possible failure is an earlier false acceptance. Its
probability is <=1/1024 by the same argument. It therefore satisfies the
stated uniform 1019/1024 guarantee as well.

## 11. Joint worst-case resources in the charged model

All estimates in this section apply to the concrete execution just specified,
not merely to an average-success branch. Bit accesses as well as quantum gates
pay their full address charge. Work is sequential; no concurrency is credited.
Let L=L_0. The quotas obey L_i>=8L_(i+1), since their difference is the
positive quantity F*4^(ell-i)+8^(ell-i). They have the exact bound

    L = F*(2*8^ell-4^ell)+ell*8^ell
      <= (2F+ell)*8^ell,
    F = O(log(n)),      ell <= (244949/300000)*sqrt(n)+2,
    2F+ell = O(sqrt(n)),
    L = O(sqrt(n) 2^((244949/100000)*sqrt(n))).                    (11.1)

The elementary bound log2(n)=O(sqrt(n)) is used only for this polynomial
factor; it changes no coefficient inside an exponential. The estimate is an upper envelope: no constant-factor equivalence to the
rational exponential is asserted. The exact minimum-depth allocation has
3*ell=sqrt(6*m)+O(1). In particular, the slight rational slack in c is
intentional and is not a lower bound on actual cost.
All constants are absolute and independent of s or outcomes. The envelope
is derived from the actual chosen rational schedule. Also
log(L)=O(sqrt(n)), log(R)=O(sqrt(n)), t_phase=O(n),
M=O(log(n)), and R=O(nL), for n>=17.

Space and addressing. Store a label and classical wire index for each live
qubit, in old/new arrays, together with bucket counts and stable prefix pointers.
There are O(L) records and O(L) buckets. A label uses O(n) bits and each pointer
uses O(log L)=O(sqrt(n)) bits. The quotas, schedule, phase estimates, controller,
classical arithmetic and fixed rational table use O(n^2)+O(1) further bits.
The quantum arrays hold at most a constant multiple of L single phase qubits.
Only one source sample and O(n*2^(21sqrt(log2 n))) arithmetic/QPE scratch
qubits are live at a time. Classical pointer/local-program records use
O(n*2^(21sqrt(log2 n))*A_addr) further bits. Both fit the stated envelopes,
as proved in adaptive-arithmetic.md; they are not assumed free.
Batches are sequential. Classical scratch and quantum scratch are reused.
Thus

    S_C = O(nL),     S_Q=O(L),

including the subpolynomial-times-linear local scratch and pointer records.

This includes allocated spare output arrays, input/output buffers, counters,
all table data and the generator's storage. Freed/reset registers are reused;
only current local arithmetic/Fourier descriptions and Boolean-value
history are retained, fully counted, then released/reused. No instruction
log of the exponentially many whole-sieve operations is kept. The total allocated bit-plus-qubit
count is O(nL); its address length is therefore

    A_addr = ceil(log2(allocated bits and qubits + 2))=O(sqrt(n)).

Address-generation work is charged explicitly, including the indexed bit
accesses used while constructing an address. A constant number of address
buffers, loop counters and block bases suffice. For each logical instruction,
ordinary binary addition/subtraction/multiplication by a fixed small stride
constructs its O(A_addr)-bit wire addresses using O(A_addr) elementary bit
accesses. Charge O(A_addr) for each such access as well as the gate's own
addressing cost. Copying or emitting a complete address buffer also costs
O(A_addr^2) by this accounting. We use this straightforward worst-case
O(A_addr^2) cost per instruction, not an unproved amortized O(A_addr) generator.
The fixed modular Boolean template can be streamed. For the adaptive
arithmetic, padded pointer records and current local gate lists, with all
O(A_addr)-bit instruction copies charged, give the same O(A_addr^2) allowance.
Their explicit layout, sizing and memory proof is in adaptive-arithmetic.md;
no multiplication of two variable wire indices is assumed free.

Thus an O(n)-gate modular permutation from Section 2 is generated and applied
in O(n*A_addr^2)=O(n^2) charged work. Controlled translations by 2^q mod N
use precomputed classical shifts obtained by modular doubling. They do not
iterate U 2^q times. The optional constant simplifications in the diagnostic
circuit builder are unnecessary in the streamed implementation.

Source labels. The exact reciprocal/Fourier framework in fast-labels.md uses
adaptive-arithmetic.md's fully counted integer product. Including all generated
matrices and uniform local circuit/pointer records, per-source logical work is
O(n*2^(21sqrt(log2 n))). Every instruction pays the full O(A_addr^2)=O(n)
bit/address-generation allowance, giving charged work
O(n^2*2^(21sqrt(log2 n))) per source and
O(n^3*L*2^(21sqrt(log2 n))) across R=O(nL) acquisitions. Exact rounding,
preprocessing, source charge, resets, scratch and failures are included.
All extra local records have log size O(log n+sqrt(log n))=o(sqrt n), so
fit O(nL) classical/O(L) quantum before the address bound is used.

Sieve work. Stable bucket sorting, key/record copying, counter updates and
ordinary pair arithmetic use O(n) logical bit work per record. The full
address-generation allowance makes this O(n^2) charged work. Summing the
geometrically decreasing stage lengths and O(n) batches gives O(n^3 L).
Each sampler trial costs O(n^2) charged work, including random bits, comparison,
resets and addresses. There are at most 4R=O(nL) trials globally, so all
successful and rejected draws also cost O(n^3 L). fast-labels.md Section 6
establishes success with this hard global cap. No expected-only trial count
is substituted for a branchwise cap. Both terms fit the stated source-work envelope.

Final reconstruction and verification. The candidate interval always has at
most 2^ell+2 integers. Its endpoints require O(n)-bit rational arithmetic;
with the same conservative charging, O(n^3) work suffices. Each of at most
(n+10)(2^ell+2) verification copies uses one O(n)-gate permutation, costing
O(n^2) including generation, addressing and its n+1 source charge. Therefore
O(n^3*(2^ell+2)) bounds final verification. Since L>=8^ell F, this is
O(n^3 L), also within source work. Saving phase estimates, generating the
integer parameter schedule, initializing arrays and writing the final output
fit O(n^3*L*2^(21sqrt(log2 n))). The rational table is a fixed finite computation with an
absolute time/space constant charged to these bounds.

Consequently the one program, before assuming successful measurements, obeys

    T=O(n^3*L*2^(21sqrt(log2 n))),       S_C=O(nL),       S_Q=O(L).             (11.2)

Substitution of (11.1) gives the envelopes in Section 1. The finitely many
n<=16 cases have bounded input sets and at most 2^16*26 tests. Enlarging
absolute outer constants covers those instances as well, including n=1.

## 12. Exact indices and comparison

Put c=244949/100000. The logarithm of the time envelope is
c sqrt n+21sqrt(log2 n)+(7/2)log2 n. Its iterated logarithm is
(1/2)log2 n+log2 c+o(1), so the exact index is 1/2. For each other resource,
the logarithm is c sqrt n+r log2 n with r=3/2 or1/2, giving the same index.
Outer constants and the finite n=1 extension do not change those limits.
The time exponent term with nPower0/logPower1/2 is expressly supported by
the structured family. Both its coefficient21 and c are proved, not guessed.

Relative to PG4's n^(15/4)2^(c sqrt n), the new time envelope ratio is
2^(21sqrt(log2 n)-(1/4)log2 n), tending to zero. This is an asymptotically
smaller upper guarantee for the specified adaptive program, not a matching
lower bound, finite practical timing improvement, smaller index or the
cube-root research goal.

## 13. Provenance and finite evidence

Direct sources include PG4 e40f2d5a-68c9-418b-b4e8-64a80305968e and PG3 5a99915d-bf94-4f6a-8969-5cc6e601a1a9,
PG2 873cba1f-780f-4fad-bd5b-9cf12b8de874 (unpublished after failed review),
MDC1 7c30b190-e90b-492c-b52c-29cf1a9da1a7 and the directly consulted
VFD3-M4 6f4423a3-e180-476f-987a-b1c4cdaa898e. Their retained material and
changes are identified at the beginning and in fast-labels.md. Earlier
VFD3 c2e60e34-e31d-4a65-8f18-a420030cf3e4 and VFD3-M
42e58ec0-80c2-4963-9539-c4fdb27e3ea5 remain acknowledged; the inherited
FD2 source is 286f74f7-dd46-4db7-9fe2-031755c76a04, candidate
773a35a977a66bbe10fa6f8f6ea50c2021f0fba0, outside this challenge scope.

Known square-root-growth context includes Kuperberg,
arXiv:quant-ph/0302112v2 Theorem I.1/Sections III,V and
arXiv:1112.3333v1 Sections 4.3,4.6. Its Section 4.5 heuristic constant
is not used. Nam/Su/Maslov arXiv:1803.04933v2 Section II motivates the
reusable gradient idea; all actual needed circuit proofs are reproduced.
No external retrieval or accepted verdict is a proof premise.

Current finite diagnostics cover the adaptive product and retained exact Fourier framework,
exact preparation amplitude formulas, QPE tails, quota schedules and rational
outer-decoder table. They are reproducibility evidence, not asymptotic proof
or physical quantum execution. Superseded arithmetic/instrument diagnostic
programs were removed to reduce duplicate evidence; their complete analytic
arguments remain in Sections 2 and 5. No hosted experiments are declared.
