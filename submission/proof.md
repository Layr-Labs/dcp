# VFD3: a variable-width flat-difference sieve for every DCP modulus

## 1. The theorem and the exact algorithm configuration

For every integer N >= 2 and fixed s in Z/NZ, let n=ceil(log2 N). VFD3
receives only fresh independent copies of the mixed state in rules.md. It
outputs the entire s with unconditional probability at least 1019/1024.
The same execution has, on every branch, including every abort,

    T(N,s)   = O(n^5 2^((4899/2000) sqrt(n))),
    S_C(N,s) = O(n^(3/2) 2^((4899/2000) sqrt(n))),
    S_Q(N,s) = O(n^(1/2) 2^((4899/2000) sqrt(n))).

These asymptotic envelopes apply for n>=2. The n=1 cases are explicitly
handled below and have absolute finite costs. Each envelope has growth
index exactly 1/2. Constants are absolute, independent of N, s, outcomes
and memory contents. They include source calls, classical bit work,
addressing, generated gates, measurements, initialization and all failures.
The structured objects declare these very envelopes, with coefficient
4899/2000 inside the exponent, not an unspecified big-O coefficient.

For n<=16, VFD3 exhaustively tests t=0,...,N-1 by Section 10 with k=n+10
fresh tests per candidate. It returns the first candidate passing all tests,
or zero if none passes. This is a fixed finite prefix of the single algorithm.
It does not run the sieve or generate the phase table.

For n>=17 put h=n+1, m=floor(log2 N), and define the following integers.
`clog(x)` is the bit length of x-1. Square-root comparisons use exact integers.

    ell = 1 + min{u>=0 : 4000000*u*u >= 2666689*n},
    J = m-1-ell,
    lambda = clog(1024*h),
    M = 8192*lambda,
    F = 1048576*lambda,
    L_i = F*(2*8^t-4^t)+t*8^t, t=ell-i, i=0,...,ell,
    R = 4*(J+1)*L_0,
    A_coin = clog(1024*R),
    M_src = 8192*clog(1024*R*(n+3)),
    k = n+10.

Thus ell=1+ceil((1633/2000)sqrt(n)). It satisfies ell<=m-1 and

    m-1 <= (3*ell^2-ell)/2.

Indeed (1633/2000)^2 > 2/3, so ell>sqrt(2*n/3)+1, and the right side
exceeds n. Also ell<=(1633/2000)sqrt(n)+2<=n-2 for n>=17, while m>=n-1.
The latter inequality holds at 17 and its right-minus-left difference
is increasing thereafter (or square the positive sides). Therefore J>=0.

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
instance-dependent advice or uncharged preparation is part of VFD3.

The contribution is an explicit schedule and sharpened joint bound for a
known type of sieve, not a claimed new DCP growth index or the cube-root
goal. Sections 2--5 adapt the self-contained foundations of public submission
286f74f7-dd46-4db7-9fe2-031755c76a04 (FD2), candidate commit
773a35a977a66bbe10fa6f8f6ea50c2021f0fba0. That dependency is declared.
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
not the VFD3 schedule. A Boolean MUX(control,x,y) is

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
of N and s. VFD3 generates it once by the finite rational schedule in
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

    delta_src = 4(n+3) exp(-M_src/2048) < 1/(1024R).

For the last inequality, let A=1024R(n+3), use M_src>=8192 log2 A and ln(2)<1:
exp(-M_src/2048)<=A^-4. The stated inequality follows immediately for R>=1.
The retained qubit, conditional on the latent y, is exactly q_y, even if the
reported label is wrong. We make no perfect-label assertion for this physical
extractor.

An ideal analysis may instead report the latent y. Couple it to the actual
extractor using the exact ensemble and the same test outcomes. Until a wrong
label occurs, their retained classical/quantum states coincide after local test
records are discarded. There are at most R label extractions; a conditional
union bound gives total divergence probability <1/1024. This is a proof coupling,
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

## 6. Exact coins with a finite cap and an additive error bound

For 0<d<M0/2 put D=2(M0-d). Draw clog(D) independent fair bits, giving V.
If V<D return [V<M0]; otherwise try again. The ideal uncapped sampler has
uniform accepted V in [0,D), so it implements Section 5's rational probability.
Each trial succeeds with probability at least 1/2. Generate each fair bit
using H and computational measurement on one reset qubit. VFD3 permits at
most A_coin trials and then aborts the entire algorithm.

For every past history the cap-hit probability is at most 2^(-A_coin).
Since L_i>=8L_(i+1), sum_(i<ell) L_i < (8/7)L_0. There are fewer than
(J+1)*(4/7)*L_0 < R coins in all batches. A conditional union bound is thus
at most 1/1024. Couple the actual finite sampler to the ideal sampler until
the first cap is hit. This transfers the ideal instrument law with an
additive error. Do NOT condition on no cap to assert exact uniformity: the
cap probability can depend on the denominator and therefore on d.

## 7. Variable-width batches and the complete sieve

An ideal initial label y uniform in [0,N) qualifies if y<2^m. This has
probability 2^m/N>=1/2; conditional qualified labels are uniform in [0,2^m).
Their phase denominator stays N. Generate the rational table of Section 3
once, with its fixed generation cost counted.

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
    F = O(log(n)),      ell <= (1633/2000)*sqrt(n)+2,
    2F+ell = O(sqrt(n)),
    L = O(sqrt(n) 2^((4899/2000)*sqrt(n))).                    (11.1)

The elementary bound log2(n)=O(sqrt(n)) is used only for this polynomial
factor; it changes no coefficient inside an exponential. In fact ell is
Theta(sqrt(n)) and 8^ell differs from 2^((4899/2000)*sqrt(n)) by at most
a constant factor, so (11.1) retains the asymptotic order of this allocation.
All constants are absolute and independent of s or outcomes. The envelope
is derived from the actual chosen rational schedule. Also
log(L)=O(sqrt(n)), log(R)=O(sqrt(n)), M_src=O(sqrt(n)),
A_coin=O(sqrt(n)), M=O(log(n)), and R=O(nL), for n>=17.

Space and addressing. Store a label and classical wire index for each live
qubit, in old/new arrays, together with bucket counts and stable prefix pointers.
There are O(L) records and O(L) buckets. A label uses O(n) bits and each pointer
uses O(log L)=O(sqrt(n)) bits. The quotas, schedule, phase estimates, controller,
classical arithmetic and fixed rational table use O(n^2)+O(1) further bits.
The quantum arrays hold at most a constant multiple of L single phase qubits.
Only one n+1-qubit source sample and O(n) arithmetic ancillas are live at a time.
Batches are sequential. Classical scratch and quantum scratch are reused.
Thus

    S_C = O(nL+n^2+1)=O(nL),     S_Q=O(L+n+1)=O(L).

This includes allocated spare output arrays, input/output buffers, counters,
all table data and the generator's storage. Freed/reset registers are reused;
no circuit or operation history is retained. The total allocated bit-plus-qubit
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
The finite Boolean template and its reverse use a constant number of these
address computations per generated elementary gate; no circuit list is stored.

Thus an O(n)-gate modular permutation from Section 2 is generated and applied
in O(n*A_addr^2)=O(n^2) charged work. Controlled translations by 2^q mod N
use precomputed classical shifts obtained by modular doubling. They do not
iterate U 2^q times. The optional constant simplifications in the diagnostic
circuit builder are unnecessary in the streamed implementation.

Source labels. Each source has 2(n+3)M_src=O(n^(3/2)) Hadamard tests. The
preceding O(n^2) bound per controlled translation therefore gives
O(n^(7/2)) charged work per extracted source label. This includes address
arithmetic rather than just gate addressing. Generating the O(n) modular
doubling constants, resetting a sample and accumulating counts fit this bound.
For exact phase decoding, counts have O(log(n)) bits; 64 comparisons per
level use schoolbook integer arithmetic. The n+3 unwrapping steps manipulate
O(n)-bit integers. Even charging O(A_addr^2) per logical bit operation gives
at most O(n^3) for these classical operations, below the source-label bound.
No arbitrary real operation or approximate-rotation synthesis is used.
The R source extractions cost O(R*n^(7/2))=O(n^(9/2)*L).

Sieve work. Use stable classical counting sort, reading keys and writing
records/pointers in original order. Phase qubits remain on their physical
wires; classically constructed addresses select their gates. A stage has
K_i bucket counters, and K_i<=L_i. Computing a key, copying a label, updating
a counter and computing a difference use O(n) logical bit operations per
record. With the full O(A_addr^2) address-generation allowance, sorting and
ordinary per-pair work cost O(n^2 L_i). A coin has at most
A_coin=O(sqrt(n)) trials of at most n+2 bits, each trial costing at most
O(n*A_addr^2)=O(n^2). Thus all pair processing, including every rejected
trial, costs O(n^(5/2)*L_i). Since sum_i L_i<=8L/7 and there are O(n)
batches, total sieve work is O(n^(7/2)*L), within the source-work envelope.

Final reconstruction and verification. The candidate interval always has at
most 2^ell+2 integers. Its endpoints require O(n)-bit rational arithmetic;
with the same conservative charging, O(n^3) work suffices. Each of at most
(n+10)(2^ell+2) verification copies uses one O(n)-gate permutation, costing
O(n^2) including generation, addressing and its n+1 source charge. Therefore
O(n^3*(2^ell+2)) bounds final verification. Since L>=8^ell F, this is
O(n^3 L), also within source work. Saving phase estimates, generating the
integer parameter schedule, initializing arrays and writing the final output
fit O(n^(9/2)*L). The rational table is a fixed finite computation with an
absolute time/space constant charged to these bounds.

Consequently the one program, before assuming successful measurements, obeys

    T=O(n^(9/2)*L),       S_C=O(nL),       S_Q=O(L).             (11.2)

Substitution of (11.1) gives the envelopes in Section 1. The finitely many
n<=16 cases have bounded input sets and at most 2^16*26 tests. Enlarging
absolute outer constants covers those instances as well, including n=1.

## 12. Exact indices and what the optimization establishes

For fixed c=4899/2000>0 and fixed r in {5,3/2,1/2}, let
B_r(n)=2^(c*sqrt(n))*n^r for n>=2. Then

    log2(B_r(n)) = c*sqrt(n)+r*log2(n),
    log2(log2(B_r(n))) = (1/2)*log2(n)+log2(c)+o(1).

The max{4,B_r(n)} in the definition does not change the tail. Dividing by
log2(n) proves the limit, hence the limsup, is exactly 1/2. Finite extensions
at n=1 and constant outer multipliers do not affect it. This proves the
canonical rational index 1/2 for all three claims, not a matching lower bound
on the algorithm's actual work or a general DCP lower bound.

The substantive changes from FD2 are the shrinking stage capacities
b_i<=3*(ell-i-1), the explicit quota curve
L_i=F*(2*8^(ell-i)-4^(ell-i))+(ell-i)*8^(ell-i), and the reduced total
source budget. The sum of capacities is quadratic in ell, allowing ell
approximately sqrt(2n/3). The quota differences allocate an F*4^t margin
for fluctuations and an 8^t margin for unmatched bucket entries. This
avoids multiplying a worst-case surplus through every stage.

The chosen rational slope 1633/2000 is slightly greater than sqrt(2/3);
its inside-exponent coefficient is exactly 4899/2000. We do not round an
unknown constant to one. The endpoint capacity is proved for all n,
not extrapolated from experiments. The n^5, n^(3/2) and n^(1/2)
factors are retained in both prose and structured bounds. There is no
log factor in these asymptotic representatives: the exact allocation
factor 2F+ell is Theta(sqrt(n)), as proved in Section 11.

FD2 declared a time envelope (n+1)^8*2^(6*ceil(sqrt(n))) and the analogous
6*ceil(sqrt(n)) exponential memory envelopes. VFD3's proved envelopes are
asymptotically smaller than those particular declared envelopes. This is a
comparison of guarantees. It is not a lower bound on FD2, a claim to
outperform every Kuperberg implementation, or a new fastest-known DCP theorem.
Polynomial-space algorithms are a different tradeoff and are not dominated
in all resources by these exponential-space bounds.

## 13. Provenance, literature and finite evidence

The public FD2 submission listed in Section 1 is a material dependency for the
flat instrument, exact spectral-label extraction, finite rational decoder,
verification strategy and supporting diagnostic programs. Its public note and
candidate tree are the source, not an inference from its score. The proof
here re-establishes those components and changes the schedule, quotas, error
budgets, source allocation and resource accounting. The separate historical
polynomial-space submission was not used as an implementation or proof premise.

Greg Kuperberg, *A subexponential-time quantum algorithm for the dihedral hidden
subgroup problem*, arXiv:quant-ph/0302112v2, Theorem I.1 and Sections III and V,
establishes the known square-root growth regime. Greg Kuperberg, *Another
subexponential-time quantum algorithm for the dihedral hidden subgroup problem*,
arXiv:1112.3333v1, Sections 4.3 and 4.6, discusses collimation, quantum-space
savings and a rigorous square-root bound. Its Section 4.5 labels its sharper
leading-constant estimate heuristic; that estimate is not used here. These
citations supply context, not unproved subroutine assumptions of VFD3.

All proof premises needed for review are included above. No external page
fetch is required to validate the three claims. The exact input labels are
used before each compression, and Section 5 proves the retained density
matrix and product law. This is not a scheme that discards Fourier-label
information before attempting to uncompute a subset-sum register.

The evidence directory contains reproducible finite diagnostics, not a proof
of the asymptotic statement and not a claim of executing a quantum device:

- arithmetic_audit.py: Boolean carries, modular permutations including invalid
  encodings and zero shifts, inverse cleanup, and the Toffoli parity identity.
- batch_instrument_audit.py: exact small joint instrument laws and prefix
  truncation, including a negative control for sorting by middle value.
- rational_grid_certificate.py: exact rational generation and error inequalities
  for phase_grid.json, with its grid_certificate.json receipt.
- schedule_audit.py: integer schedule/capacity, quota/slack and reconstruction
  checks for the VFD3 changes, plus comparisons of explicit sample budgets.

The first three programs and fixed grid are copied with attribution from the
FD2 candidate. Their mathematical foundations remain identical. The new
schedule diagnostic does not simulate the exponentially large production
lists or certify a success probability experimentally. The manifest declares
no hosted experiments; local evidence runs and the proof have separate roles.
