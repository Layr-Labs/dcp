# PS1: bounded polynomial-space combination of dihedral coset states

## 1. Joint theorem and fixed configuration

For every integer N>=2 and every fixed secret s in Z/NZ, put n=ceil(log2 N).
The only quantum input is fresh independent copies of
rho_s=(1/N) sum_(x=0)^(N-1) |psi_(x,s)><psi_(x,s)|, where
psi_(x,s)=(|0,x>+|1,(x+s) mod N>)/sqrt(2). PS1 uses a uniform classical controller, exact
Clifford+T gates, computational measurement and reset. It has no source inverse,
purification, controlled source, hiding-function oracle, subset-sum oracle,
quantum-addressed memory primitive, instance advice or free postselection.

Define clog(x)=ceil(log2 x) by the bit length of x-1. All logarithms are base two.
The following global integers are fixed functions of the ORIGINAL input N:

    h = clog(n+2),
    b = ceil(sqrt((n+1)h)),
    d = ceil(n/(b+1)),
    q = 512(d+2)h,
    r_max = b+q,
    A_retry = 2^40 (n+2)^12,
    F_root = 2^20 (n+2)^8 2^(4(d+2)),
    R = 16 F_root [A_retry(r_max+1)]^(d+2),
    C_coin = clog(256R),
    M_src = 8192 clog(1024R(n+3)),
    M_phase = 8192 clog(1024(n+2)).

Integer square roots, powers, counters and divisions use charged binary
arithmetic. Sections 5--11 specify ONE program and parameter choice. It returns
the entire s with unconditional probability at least 251/256>2/3, for every
N and s. Jointly on EVERY execution branch it has

    T = O((n+2)^12 R 2^r_max),
    S_C = O((n+2)^2) allocated classical bits,
    S_Q = O((n+2)^2) allocated accessible qubits.

All constants are absolute and independent of N, s and outcomes. The work bound
includes bit operations, addressing, gate generation, every original source copy
(cost n+1), preprocessing, gates, measurements, reset and failed attempts.
Both spaces include input ports, all retained states, labels, arithmetic,
tables, recursion frames and current circuit descriptions. Section 12 proves
these bounds and Section 13 proves the exact growth indices [1/2,0,0],
canonically ["1"/"2","0"/"1","0"/"1"]. These are indices of proved upper
envelopes, not lower bounds on actual resources.

This is a polynomial-space tradeoff of the known Regev type. Its work is
2^O(sqrt(n log(n+2))), which is asymptotically worse than FD2's
2^O(sqrt(n)) work envelope. Equal time indices do not make those full time
bounds equivalent. No coordinatewise dominance, novelty, optimality, or
2^O(n^(1/3)) claim is made.

PS1 maintains a known D|N and a known residue a in [0,D). On the event that
a=s mod D, it obtains fresh current coset states of modulus Q=N/D and secret
kappa=(s-a)/D by the exact conversion in Section 9. Initially D=1,a=0.
If any bounded procedure aborts, PS1 releases all registers and returns zero.

In the helper Sections 2--4, Q denotes a current modulus, kappa its current
secret, and n remains the ORIGINAL capacity, so Q<=2^n. Data are zero padded
to n bits. The formulas do not require n=ceil(log2 Q). Their source assumption
is supplied by Section 9 whenever all previously recovered residues are correct.

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
not the PS1 schedule. A Boolean MUX(control,x,y) is

    y XOR (control AND (x XOR y)).

To add a known c in [0,Q) conditionally modulo Q, let X be the n-bit input,
zero padded to width w, and let B be the quantum control bit. Compute

    (_, geN) = SUB(X,Q)
    active = B AND NOT(geN)
    (S,_) = ADD(X,c,0)
    (D,ge) = SUB(S,Q)
    V = MUX(ge,D,S)
    out = low_n_bits(MUX(active,V,X)).

On X<Q and B=1 this is X+c mod Q. On B=0 or X>=Q it fixes X. The inverse uses

    (_,geN) = SUB(Y,Q)
    active = B AND NOT(geN)
    (D,gec) = SUB(Y,c)
    (P,_) = ADD(Y,Q-c,0)
    V = MUX(gec,D,P)
    out = low_n_bits(MUX(active,V,Y)).

For Y<Q this selects Y-c or Y+Q-c and is the inverse; on invalid encodings it
is identity. The formulas include c=0 and Q=2^n. All sums used in comparisons
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
known wire addresses are computed by ordinary binary arithmetic. Section 12
charges their full bit cost. In particular, this construction supplies controlled
cyclic shifts U^c on valid data, U|x>=|x+1 mod Q>, and controlled subtraction for
Section 9. It assumes no unit-cost quantum lookup or arithmetic oracle.

## 3. A finite rational phase decoder

Let dist be circular distance on R/Z. The fixed table `evidence/phase_grid.json`
contains rational coordinates for the 64 points exp(2*pi*i*r/64), with denominator
2^16. Each coordinate has absolute error <2^-16. The table is fixed independently
of Q and kappa. PS1 generates it once by the finite rational schedule in
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

For analysis define omega=exp(2*pi*i/Q),

    chi_y = (1/sqrt(Q)) sum_x omega^(-yx)|x>,
    q_y = (|0>+omega^(kappa*y)|1>)/sqrt(2), Q_y=|q_y><q_y|.

Direct expansion of matrix entries gives

    rho_kappa = (1/Q) sum_(y=0)^(Q-1) Q_y tensor |chi_y><chi_y|.

Indeed the cross entry indexed by x,z sums omega^(y(z-x-kappa)), which vanishes
unless z=x+kappa mod Q, and the diagonal blocks agree as well. Also U chi_y=omega^y
chi_y. This is an ensemble identity for the given mixed state; it supplies no
accessible hidden register or additional source operation to the algorithm.

For each h=0,...,n+2, do M_src Hadamard tests of controlled U^(2^h) on the source
DATA register in X, and M_src such tests in Y. Use a fresh/reset ancilla in |+>
for every test. Conditional on latent y in the exact ensemble, the means are
cos(2*pi*2^h*y/Q), sin(2*pi*2^h*y/Q). The data register remains chi_y; the first
source qubit is untouched. Hence these test outcomes are independent conditional
on y. U^(2^h) is the exact controlled addition by 2^h mod Q of Section 2.
Measuring Y means S-dagger then H then a computational-basis measurement;
measuring X means H then that measurement. No approximate rotation is invoked.

Decode the two empirical means at each h by Section 3, then unwrap with H=n+2.
If all means are accurate, the estimate of y/Q has circular error
<=1/(16*2^(n+2))<1/(2N). Round Q times the estimate to the nearest integer modulo
Q (smaller integer on a tie). Report that integer as y_hat and retain the first
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

## 5. A polynomial-space multiway instrument

Write p_f(theta)=(|0>+exp(2*pi*i*theta*f)|1>)/sqrt(2), and P_f for its density.
This section holds for EVERY fixed real theta; its denominator need not be a
power of two. Suppose the r input labels u_i are independent uniform in [0,B),
B a power of two, and their conditional states are the product of p_(A*u_i).
Let l>=0 with K=2^l and B'=B/(2K)>=2. Put

    r=l+q, D_mask=2^r, lambda=D_mask/K=2^q, H=16lambda.

The multiplier A is classically known. Tensor the r qubits; its computational
basis mask v has amplitude exp(2*pi*i*theta*A*S_v)/sqrt(D_mask), where
S_v=sum_i v_i u_i is the EXACT integer sum.

Coherently compute (weight(v), S_v mod K), and measure it.
The weight register has clog(r+1) bits. Exact classical subset sums use
n+clog(r+1)+1 bits; the hash sum is accumulated modulo K. The ripple formulas
are instantiated at these explicit widths, with clean work registers. The observed bucket
has m masks. Enumerate all D_mask masks in increasing integer order to count m.
If m<2 or m>H, fail this attempt and reset its states. No bucket list is stored.

Otherwise put P=2^clog(m). Draw a uniform nonzero z in [1,P), with the bounded
sampler of Section 7. Let j(v) be the lexicographic rank of v in its bucket.
Compute j(v) coherently by enumeration; each enumerated constant mask is tested
by a multi-controlled Boolean equality before XORing its known rank into scratch.
This costs O(D_mask*poly(n)) work and polynomial space, not a lookup oracle.

For j in [0,m), its proposed partner is j XOR z. Measure whether that partner
is <m; fail if not. Measure the canonical pair key min(j,j XOR z). Each successful key leaves exactly TWO basis masks v,w with equal amplitude
magnitudes. If a reported key does not specify two distinct existing ranks,
the program fails the attempt. Enumeration always runs its fixed finite range;
no missing rank can create an unbounded search.
Reverse the rank, comparison and key computations on that two-point support;
their measured registers are now known constants and can be cleared. Enumerate
again to find the two masks, without storing the bucket.

For any two distinct masks x,y, the unique nonzero XOR mask pairing them is
z=j(x) XOR j(y). Thus, including bucket and pair measurements, each unordered
pair in a bucket has probability

    2/[D_mask(P-1)].

Apply an independent classical coin of probability (P-1)/(H-1).
Since m<=H and H is a power of two, P<=H. After that coin the probability
assigned to EACH unordered same-bucket pair is exactly

    c_pair = 2/[D_mask(H-1)].

Masks in the same bucket have the same weight. If their common bits are removed,
w-v has j positive and j negative entries, for some j>=1. Compress their
two-point quantum support exactly: XOR the constant v into the mask register,
choose a pivot where v XOR w is one, and CNOT that pivot into every other one
position of v XOR w. All nonpivot qubits become zero. The pivot is a phase
qubit with relative phase A*(S_w-S_v). Apply X if this difference is negative.
For delta=abs(S_w-S_v), the retained density is exactly P_(A*delta).

Reject unless delta<B/2. The hash guarantees K divides delta; write t=delta/K.
The final flattening coin in Section 6 makes the output labels nearly uniform
in [0,B'), with a rigorously bounded discrepancy. Every successful history with
the same new frequency A*K*t has the same conditional density P_(A*K*t).
The history-dependent scalar is only a global phase. Old input labels, masks,
rank records and discarded qubits are then erased. Unused saved labels are not
the reason this erasure is safe: it follows from the explicit two-point state.

## 6. Exact flattening and the only distributional approximation

Let j>=1 and let F_j(x) be the distribution of the difference of two sums of
j independent uniforms on [0,B). It is symmetric. For k=2j, define

    C_k(z) = sum_(a=0)^k (-1)^a binom(k,a) binom(z-aB+k-1,k-1),

where a binomial with top below its nonnegative bottom is zero. Expanding
(1-X^B)^k/(1-X)^k proves, coefficient by coefficient,

    F_j(x) = C_(2j)(x+j(B-1)) / B^(2j).

This is a polynomial number of exact integer operations on polynomial-length
integers, even though B is large.

We need a lower bound on these probabilities for |x|<B/2. The difference of
two uniforms is the symmetric triangular distribution
Pr(U-V=x)=(B-|x|)/B^2 for |x|<B. Sums of symmetric unimodal integer
distributions are symmetric unimodal: decompose each such sequence into a
nonnegative sum of centered interval indicators. The convolution of two
centered interval indicators is symmetric and nonincreasing in |x|, which
proves the assertion by bilinearity.

Let Y be the sum of j-1 triangular differences. Its support has at most 2jB
integers, and its central interval [-B/4,B/4] has at least B/2 integers.
Unimodality makes the average probability in a centered interval at least
the average on the whole support. Hence Pr(|Y|<=B/4)>=1/(4j).
For |x|<B/2 and |Y|<=B/4, the remaining triangular probability is >1/(4B).
Thus F_j(x)>=1/(16jB). The case j=1 has Y=0 and satisfies the same bound.
Here B>=4, as required by B'>=2.

Put a_flat=1/(64rB). After a retained pair with delta<B/2, apply the exact coin

    a_flat/F_j(0)                    if delta=0,
    a_flat/[2 F_j(delta)]            if delta>0.

These probabilities lie in [0,1] by the preceding lower bound. The factors of
two account for absolute differences. The coin uses the coefficient formula;
it does not assume an oracle for the distribution.

For analysis first REMOVE only the condition m<=H while retaining the
constant pair weight c_pair. This is a formal ensemble measure, not a physical
operation on arbitrary fixed inputs. Averaging independent uniform labels, any
fixed balanced unordered mask pair contributes exactly c_pair*a_flat to each
t in [0,B'). Its support has delta=K*t, so the low-bit congruence is automatic.

The number of balanced unordered distinct pairs is

    P_bal = [binom(2r,r)-2^r]/2.

Indeed sum_w binom(r,w)^2=binom(2r,r), by counting an r-subset of two r-sets.
Removing the diagonal and dividing by two gives the formula.
The formal success measure is therefore the EXACT flat ensemble

    c_pair*a_flat*P_bal sum_(t=0)^(B'-1) |t><t| tensor P_(A*K*t).

Its trace is

    p_star = P_bal/[64r D_mask(H-1)K].

Cauchy-Schwarz on the r+1 weight classes and 2^r>=2(r+1), valid for r>=3,
give P_bal>=D_mask^2/[4(r+1)]. Since H=16D_mask/K, it follows that

    1/(8192r^2) <= p_star <= 1.

For the upper bound use P_bal<=D_mask^2/2 and H-1>=15D_mask/K,
which even give p_star<=1/(1920r).

The formal measure plus a failure flag of mass 1-p_star defines a legitimate
ABSTRACT output ensemble. We next compare the physical instrument to it;
we never assign probability >1 to a physical coin.

Fix one balanced distinct pair v,w. Condition on its low-bit collision.
For every other mask x of the same weight, let I_x indicate that x is in
the same bucket. Put a=v XOR w and c=v XOR x. Differences w-v and x-v are
obtained from the binary vectors a,c by the same coordinate sign changes.
The distinct nonzero vectors a,c are linearly independent over F_2, and have
a 2-by-2 minor odd. Therefore their two linear forms on independent uniform
labels modulo K=2^l are jointly uniform. Conditional on the pair collision,
E I_x=1/K.

For two different additional masks x,y, the three forms are independent unless
a, v XOR x, v XOR y are dependent over F_2. An odd full-rank minor is invertible
modulo 2^l, so independent triples give covariance zero. Given x, the only
possible dependent y has v XOR y=a XOR(v XOR x); there is at most one.
Its covariance is at most 1/K. Consequently the conditional bucket count obeys

    E m = 2+[binom(r,weight(v))-2]/K <= 2+lambda,
    Var(m) <= 2lambda.

These identities also hold at K=1 with zero actual variance. Since lambda>=1,

    Pr(m>16lambda | pair collision)
        <= 2lambda/(13lambda)^2 < 1/(64lambda).

The condition m<=H removes only nonnegative mass from each ideal output label;
it cannot change its conditional quantum state. The total removed success mass,
even before the final coin, is at most

    c_pair*P_bal*(1/K)*(1/(64lambda))
        <= 1/(960lambda) <= 2^(-q).

Here Pr(pair collision)=1/K because the difference has a coefficient +/-1.
Thus the PHYSICAL averaged instrument and the abstract flat output ensemble,
each with its failure flag, have total-variation/trace distance at most 2^-q.
This is an additive error bound, not an unproved exact-uniformity assertion
after clipping. It holds uniformly for every phase parameter theta.

For use in a recursive generator, the input label records and all internal
histories are consumed and erased before returning. Fresh sibling inputs are
independent conditional on the fixed secret. An induction replaces children
by their abstract output ensembles, then applies this averaged instrument to
their product uniform inputs. The error is at most the sum of the child errors
and 2^-q for the current attempt. This does not assert a channel-distance bound
for arbitrary adversarial fixed label tables. The generator construction below
requires, and supplies, exactly the product-uniform ensemble in this argument.

## 7. Bounded rational samplers and recursive generation

A rational coin a/c in [0,1] is implemented by drawing clog(c) independent
fair bits, interpreting V in [0,2^clog(c)), and accepting a range trial if V<c.
On a valid range trial return [V<a]. Each range trial succeeds with probability
at least 1/2. A uniform nonzero XOR mask is sampled by rejecting zero from
clog(m) fair bits, again with range success at least 1/2. Fair bits are H and
measurement on a reset qubit. The ACTUAL program allows at most C_coin trials,
then aborts the whole computation. It is coupled to the ideal uncapped sampler
until that cap, with error at most 2^-C_coin per sampler. Conditioning on no
cap is not used to infer exactly uniform output labels.

For one current modulus Q>=2 put m=floor(log2 Q). Partition m-1 into positive
parts e_i<=b+1 by greedily taking min(b+1,remaining), and put l_i=e_i-1.
There are ell=ceil((m-1)/(b+1)) parts, ell=0 if m=1. Define

    B_0=2^m, B_i=B_(i-1)/2^(l_i+1),
    A_0=1, A_i=A_(i-1)*2^l_i,
    J=sum_i l_i=m-1-ell.

Then ell<=d, B_ell=2 and A_ell=2^J. Every stage has B_i>=2, and
A_i*B_i=2^(m-i)<=Q. All sums/differences used in the physical phase are exact
integers; the phase denominator stays Q. No reduction modulo B_i is applied
to an unknown phase.

Choose a unit t modulo Q. The base generator G_0 repeats at most A_retry times:
obtain a fresh converted coset state, extract its label y by Section 4,
put u=t*y mod Q, and keep it if u<2^m. Otherwise reset and retry.
With ideal spectral labels, qualification has probability >=1/2 and the
returned u is uniform in [0,B_0). Its state is
p_u(theta), theta=(kappa*t^(-1) mod Q)/Q, exactly.
If the retry cap is reached, abort the whole program.

G_i, for i>=1, repeats at most A_retry attempts. Each attempt obtains
r_i=l_i+q independent records from G_(i-1), and runs Sections 5--6 with
B=B_(i-1), l=l_i, A=A_(i-1). A child abort aborts the program. A failed
combination resets its inputs and retries; a successful one returns only
its new label and phase qubit. Discard local histories and retry counters
upon return. No global history or observed work counter is used as advice.

To prepare one copy of p_(2^J)(theta), call G_ell at most A_retry times,
keep the first returned label one and reset the others. Reaching this cap
also aborts. We call this procedure Qubit(Q,t). In the abstract recursion, availability and retry count are independent of a
returned uniform label: each attempt has a constant success mass times that
same normalized ensemble. This proves the assertion inductively, including
conditioning on child availability. The label-one event has probability 1/2 and its retained state is exactly the
named qubit. The same finite bounds govern the actual program.

## 8. Phase measurements and finite-precision classical constants

The constant 64-point decoder and unwrapping in Section 3 supply coarse
estimates at frequencies 2^h. With M_phase X measurements and M_phase Y
measurements per frequency, the probability of an error >1/16 is
<=4 exp(-M_phase/2048).

All tomography is streamed: prepare one qubit, measure/reset it immediately,
and update a classical counter before preparing the next. No array of shots
is stored.

We also need direct fine tomography of a phase z/K for a KNOWN integer K.
Use M_phase*K^2 X measurements and the same number in Y. The probability
that either empirical mean errs by >1/(32K) is
<=4 exp(-M_phase/2048).

For this fine decoder enumerate G=2^clog(64K) grid indices, one at a time;
retain only the closest index and its squared distance. Approximate each
sine/cosine coordinate within 2^-p, p=clog(2^20 K), by exact rational arithmetic.
The following explicit finite generator does so without any real-arithmetic
or rotation oracle.

Use T=2(p+10) terms in each alternating arctangent series for 1/5 and 1/239;
the even partial sum is a lower bound and adding the next term is an upper.
Machin's identity from Section 3 gives a pi interval of width <2^(-p-30).
Round the pi-interval midpoint to denominator 2^(p+40), then use it in
each argument 2*pi*index/G with L=p+100 Taylor terms for sine/cosine.
Finally round each coordinate to denominator 2^(p+4).
The argument is <7. The omitted Taylor term bounds are at most
7^(2L)/(2L)! and 7^(2L+1)/(2L+1)!.
Since (2L)!>=L^L and L>=121, these are bounded by 7*(49/L)^L<2^(-p-90).
The pi replacement, including dyadic rounding, contributes <2^(-p-29),
and coordinate rounding <=2^(-p-5).
Their sum is <2^-p. All inequalities use integer powers/factorials.
No grid is preloaded: its generation and all allocated integers are charged.

If empirical coordinates are accurate, nearest-grid selection has chord error

    <= pi/G + 3/(32K) + 3/(2^20 K) < 1/(4K).

As in Section 3, circular phase error is <1/(16K), so rounding K times that
grid phase to the nearest integer modulo K recovers z exactly. Ties use the
smaller integer; on the good event there is no tie. Enumeration and exact
rational comparisons use polynomial space, even if G is large.

## 9. Exact source conversion after a known residue

Suppose D|N and a=s mod D in [0,D). Write Q=N/D and s=a+D*kappa.
On a FRESH ORIGINAL source copy, subtract a modulo N on its data controlled
by its first qubit. This maps each component to

    (|0,x>+|1,(x+D*kappa) mod N>)/sqrt(2).

Compute quotient and remainder of the data by D. Both branches have the same
remainder. For x=D*z+c, the component becomes

    (|0,z>+|1,(z+kappa) mod Q>)/sqrt(2) tensor |c>.

Original x is uniform in [0,N), so c and z are independent uniforms in
[0,D) and [0,Q). Measure/reset c. The remaining mixed state is EXACTLY the
challenge coset state of modulus Q and secret kappa. This uses one original
copy, no source inverse or coherent source control.

Here is an exact polynomial circuit for quotient/remainder, rather than a
division oracle. Scan the n input bits from most to least significant.
Maintain remainder V initially zero. At each bit form W=2V+x_i, compute
e=[W>=D], replace V by W-eD and append e to the quotient. Induction gives
0<=V<D and the quotient/remainder identity, including invalid encoded inputs
above N. Ripple arithmetic of Section 2 yields O(n^2) Boolean operations/wires.
Reversible evaluation XORs quotient/remainder into clean targets and uncomputes
scratch. Compute qD+c back into the old n-bit input by schoolbook multiplication
and addition, XORing to clear it. The identity qD+c=x clears it on every
encoded input. This is an isometry into quotient/remainder registers with
clean old input, not an assumed permutation on unequal-sized spaces.

This source constructor has O(n^2) accessible ancillas, a streamed polynomial
number of exact gates, polynomial classical work/space, and a fixed schedule.
If a preceding estimate is wrong the source need not have the claimed secret;
the same finite circuit and all branchwise resource limits still apply.
Correctness below conditions only on earlier estimates being correct.

## 10. All-modulus full-secret recovery

Maintain D,a,Q as in Section 1. Whenever Q=1, return a. Otherwise write

    Q=2^v M, with M odd,
    m=floor(log2 Q), ell=ceil((m-1)/(b+1)), J=m-1-ell.

The power-of-two valuation v is found by ordinary bit scans. There are two cases.

Case I: v<=J. Then M>1. Recover z=kappa mod M by the coarse method.
For each h=0,...,n+2 choose

    c = 2^(J-v-h) mod M,
    t = c if c is odd, otherwise c+M, reduced modulo Q.

Negative powers of two are computed using the extended Euclidean algorithm
modulo odd M. This t is a unit modulo Q and t=c mod M. Therefore

    2^J * t^(-1) == 2^v * 2^h  (mod Q).

Qubit(Q,t) is consequently the phase qubit with phase
exp(2*pi*i*2^h*z/M). Use M_phase copies in X and M_phase in Y at each h,
apply the 64-grid decoder and unwrap. Its error is at most
1/(16*2^(n+2))<1/(2M) on the good event. Round M times the result to recover z.
Update a <- a+D*z, D <- D*M, Q <- 2^v. If v=0 the secret is complete.
No factorization of M, hiding-function restriction, or arbitrary phase rotation
is used.

Case II: v>J. Here A=2^J divides Q. Put K=Q/A. Then

    2 <= K < 2^(ell+2) <= 2^(d+2).

Qubit(Q,1) has phase exp(2*pi*i*kappa/K). Fine tomography of Section 8
recovers z=kappa mod K using M_phase*K^2 copies per basis and polynomial
space. Update a <- a+D*z, D <- D*K, Q <- 2^J.

In either case the updated D divides N and a is its correct secret residue
when the estimate is correct. After Case I the remaining Q is a power of two;
Case II also leaves a power of two and reduces Q by a factor at least two.
Thus there is at most one Case I and at most n+1 fine steps. The loop terminates
for EVERY measurement string, including erroneous estimates: every rounded
residue is chosen in [0,K) or [0,M), so 0<=a<D and the modulus decreases.

The output is the entire original s, not merely parity or a residue of
unspecified size. Exact coset-state conversion in Section 9 replaces any
unavailable hiding-function oracle reduction.

## 11. Deterministic caps, error transfer and unconditional success

There are at most F_root calls to Qubit in the full algorithm on every branch.
Indeed clog(1024(n+2))<=n+11<=4(n+2). The one coarse recovery uses at most
2^17(n+2)^2 qubits. All fine steps use at most
2^16(n+2)^2 2^(2(d+2)). Their sum is smaller than the declared F_root.

One Qubit call uses at most [A_retry(r_max+1)]^(d+2) times an absolute factor
of six for source calls, node attempts and rational/nonzero-mask samplers.
A geometric sum bounds the recursion tree: each node makes at most
A_retry*r_max child calls, depth <=d, with A_retry base trials and an extra
A_retry label-one loop. The factor 16 in R covers six and all loop endpoints.
Thus EACH of these total counts is at most R on every branch.

For completeness the following global inequalities hold:

    r_max+1 <= 2^10 (n+2)^2,
    log2 R <= 64(d+2)h,
    R*2^-q < 1/256.

The first follows from b<=n+1, d<=n and h<=n+1.
For the second, use log2(n+2)<=h, h>=2 and
log2[A_retry(r_max+1)]<=50+14h in R's definition.
Then log2 R<=24+8h+(d+2)(54+14h)<=64(d+2)h.
The last follows from q=512(d+2)h.

In the abstract recursive computation, every combination has success
p_star>=1/(8192 r_max^2), base qualification and final label one have success
at least 1/2, and each attempt uses fresh children. Hence any retry cap has
probability at most exp(-A_retry/(8192r_max^2)).
Using the first displayed inequality, its exponent is at least
2^7(n+2)^8, which exceeds ln(256R), since
log2 R<=64(n+2)^2. A union bound over at most R caps is <1/256.

Replace abstract stages by actual clipped instruments. The recursive
induction in Section 6, or a telescoping hybrid over the bounded consumed
subcalls, bounds output trace distance by R*2^-q<1/256.
The virtual uniform-output generator is only an ensemble analysis; no
unphysical per-input coin is executed by PS1.

Next replace uncapped rational/nonzero samplers by their actual C_coin caps:
at most R*2^-C_coin<=1/256 error. Replace ideal latent labels by the source-only
extractor in Section 4: at most 1/256 error. No independence between these
events is assumed, and no exact-uniformity claim is conditioned on no cap.

Finally, conditional on all earlier residue estimates being correct and on
the abstract phase-qubit preparers, each tomography mean has the stated
Hoeffding bound. A union over at most n+3 coarse estimates and n+1 fine
estimates is at most

    8(n+3) exp(-M_phase/2048) < 1/256.

The inequality follows from M_phase=8192 clog(1024(n+2)).
This is a first-error/intersection bound: it does not claim a phase estimate
exists on an aborted branch or a converted source is correct after a wrong
earlier estimate.

All source and stage comparisons are stopped at the first erroneous residue
estimate; before it Section 9 supplies the required exact current source.
After it the tomography error is already charged.

There are therefore five budgets, each <=1/256: retry caps, clipped-instrument
distance, rational-sampler caps, spectral-label errors, and tomography errors.
Outside them all residues and the final full secret are correct. By transfer,

    Pr(PS1 returns s) >= 1-5/256 = 251/256 > 2/3.

All guarantees are uniform over fixed N,s. No average-secret or postselected
success probability is substituted for this statement.

## 12. Joint bit-work and allocated-space analysis

Every gate is exact Clifford+T. Counters, empirical means, constants and coins
are finite integers/rationals; no synthesis oracle or real unit cost is used.
The address of a classically chosen wire is charged at the rule's
ceil(log2(M_alloc+2)) bit cost, as is every indexed classical bit access.

Useful asymptotic estimates are

    h=Theta(log(n+2)), b=Theta(sqrt(n log(n+2))),
    d=O(sqrt(n/log(n+2))+1),
    q,r_max=O(sqrt(n log(n+2))),
    r_max(d+1)=O(n+1).

For the last, d<=n/b+1 gives
b(d+1)<=n+2b and
(d+2)(d+1)h<=n^2 h/b^2+5nh/b+6h=O(n+1).
Also b,h<=n+1, so q,r_max=O(n+1). This controls storage at small n as well.

A depth-first call keeps at most r_max pending phase qubits per recursion
level. Labels and known addresses have O(n+1) bits each. Across all frames,
the phase-qubit count is O(n+1) and classical record storage O((n+1)^2).
No pile of exponentially many qubits, subset table, rank table or circuit list
is retained. Recursive calls release all local records before returning.

The largest coefficient calculation uses integers of O(r_max(n+log r_max))
=O((n+1)^2) bits. Compute binomials by product/exact division in a streaming
loop; only a constant number of such integers is needed at once. Fractions,
Euclidean gcd and uniform-range coins use linear space in their operand length.
A bounded coin stores one trial integer plus its numerator/denominator, and
generates random bits on one reset qubit.

For fine grids, p<=d+22=O(sqrt(n+1)+1). Alternating arctangent sums have a common
denominator dividing a power of 5 or 239 times a factorial of O(p) argument.
They have O(p log(p+2)) bits. The sine/cosine argument and its O(p) powers have
O(p^2 log(p+2)) bits, which is O((n+1)^2). Stream the points; do not store G
coordinates. Empirical counts, the best point and coarse unwrapping arrays fit
the same bound.

Quantum source conversion retains O((n+1)^2) Boolean wires, and spectral
labeling needs O(n+1) scratch in addition to the source port. Hashing/ranking
uses at most O((n+1)^2) Boolean wires: the rank lookup is emitted one constant
mask at a time, with a cleaned AND-chain, rather than a coherent memory query.
Two-mask compression is only O(r_max) CNOT/NOT gates with known wire addresses.

Thus BOTH S_C and S_Q are O((n+2)^2), including all allocated inputs, labels,
tables/working constants, ancillas, recursion records and instruction buffers.
These are simultaneous branchwise bounds; abort cleanup fits them.

Here is a conservative explicit work envelope. A node attempt enumerates at
most O(2^r_max) masks a constant number of times for bucket size, rank generation,
rank reversal and the selected pair. Each iteration uses polynomially many
ordinary bit operations or exact Boolean gates. Hash sums and equality/AND
chains, coin distribution coefficients, source conversion, spectral estimation,
grid generation and all counters can be implemented by regular finite loops.

For a concrete polynomial bound, operands have O((n+2)^2) bits; schoolbook
multiplication/division and Euclidean gcd take at most O((n+2)^6) bit steps
and linear space. At most O((n+2)^3) such arithmetic operations are needed per
enumeration iteration or grid point under the explicit product/series loops.
Address and gate-emission costs add at most O(n+2) per bit step. This gives
O((n+2)^10); O((n+2)^12) also covers loop initialization, original-copy cost,
hash circuits, all C_coin trials, measurement, reset and output. Source-label
Hadamard tests fit this degree because M_src=O(n+1).

There are at most R node/source/sampler units, and grid-point enumeration is
also covered: G<128K<2^(d+9), at most n+2 decodings, smaller than F_root times
a polynomial factor. Therefore the entire finite program has

    T = O((n+2)^12 R 2^r_max).

Every failed attempt is included. This is total sequential work, not parallel
depth, query count, expected time or a simulation measurement. The finite caps
give the same bound on all measurement strings regardless of correctness.

## 13. Exact canonical growth indices and comparison

Use the rule's definition
g(B)=limsup_(n->infinity) log2(log2(max(4,B(n))))/log2 n.

Let B_T(n)=(n+2)^12 R 2^r_max, with the fixed integer functions in Section 1.
The estimates above and log2 R=O((d+2)h) imply

    log2 B_T = Theta(sqrt(n log(n+2))).

The lower bound already follows from r_max>=b. Consequently
log2(log2(max(4,B_T))) =
(1/2)log2 n + (1/2)log2 log2(n+2) + O(1), and g(B_T)=1/2.
For B_C=B_Q=(n+2)^2 the numerator is O(log log n), so both indices are zero.
The canonical fractions in T,S_C,S_Q order are 1/2,0/1,0/1.

The polynomial space bounds are a substantial reduction from FD2's proved
subexponential space envelopes. The full time envelopes are different:
PS1 has a sqrt(log n) factor in its exponent. Thus the UI vector is improved
in two coordinates with equal time index, but we do not infer a scientific
no-worse relation for time or declare full-bound dominance.

## 14. Provenance, paper comparison and evidence limits

This is a bounded all-modulus, source-state implementation of a polynomial-space
combination approach of the Regev type. The reference is O. Regev,
A Subexponential Time Algorithm for the Dihedral Hidden Subgroup Problem with
Polynomial Space, arXiv:quant-ph/0406151v1 (21 June 2004), Section 3.
No theorem from that paper is imported to supply a missing resource, source
conversion, output distribution or cutoff lemma. The balanced-mask instrument,
coefficient thinning, bucket variance estimate, depth-first bounds and
full-secret all-modulus reconstruction are proved here. No new best-known
asymptotic algorithm is claimed.

The comparison to A. Gupte, S. Ragavan and M. Zhandry,
A Fourier-Label Information-Loss Barrier for Dihedral Coset Algorithms,
arXiv:2609.40062v1 (30 September 2026), is to Theorem 2.1 and Remark 2.3.
In its specified power-of-two setup, after a global subset-sum prefix measures
the low n-1 sum bits, retaining only fixed coordinatewise label digests of
range K bounds parity advantage by m_paper*sqrt(K/N). Unused saved labels or
delayed measurement can have an output-equivalent implementation within the
barrier.

PS1 instead retains full current labels through exact sum evaluation, pair
selection, sign correction and distribution thinning; only a two-mask quantum
support is then compressed. Section 5 gives its retained state, and Section 6
bounds its entire ensemble law. The information is not protected by a dummy
label register. Neither syntax nor sample count alone is asserted to evade a
quantitative information bound.

The development base is the published FD2 submission
286f74f7-dd46-4db7-9fe2-031755c76a04, candidate commit
773a35a977a66bbe10fa6f8f6ea50c2021f0fba0. Its exact arithmetic, source-only
spectral extractor, rational coarse decoder and accounting approach are reused
with the proofs included here. Its earlier SEST-1 dependency remains part of
the provenance. The public submission dependency declaration records actual
reused submissions; no declaration of no dependencies is appropriate.

The included evidence/ps_kernel_checks.py tests exact flattening, conditional
bucket moments, clipped-kernel domination, XOR matching, two-mask compression,
coset conversion, CRT frequencies and full-secret residue reconstruction.
evidence/fine_grid_certificate.py certifies the specified fine constant
generator. Their saved JSON records finite scope. The former materializes
small tables for diagnostics; the theorem's algorithm streams recomputation.

All experiments are finite diagnostics, not asymptotic proof, physical quantum
implementation, independent expert certification, novelty verification or an
official score. The proof supplies every lemma needed for the three claims.
