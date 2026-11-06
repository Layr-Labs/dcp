# CYC1: cyclic extraction in a capped streaming DCP sieve

## 0. Joint theorem, contribution and provenance

For every integer N>=2 and every s in Z/NZ, put n=ceil(log2 N) and
L=log2 n. CYC1 is the single algorithm specified below, including its
integer profile, rational budget computation, finite branch and both caps.
From independent ideal copies of the stipulated mixed coset state it
recovers the entire s with unconditional probability at least 1-2^-8>2/3.
On EVERY branch it has the simultaneous bounds

    T = O(n^(9/2) L^(3/2) 2^(sqrt(nL)+sqrt n)),
    S_C = O(n^2) bits,       S_Q = O(n) qubits,
    Q = O(n^(3/2) L^(1/2)
          2^(sqrt(nL)+sqrt n-(1/3)sqrt(n/L))).

These asymptotic expressions apply for n>=2; the explicit finite branch
also covers n=1. Constants are absolute and independent of N,s and sampled
outcomes. All four exact growth indices are [1/2,0,0,1/2]. The fifth claim
is epsilon(n)=0 in the independent ideal-copy model of Section 10.
No cube-root time, optimality or positive tolerance is claimed.

The structural change is an overlapping cyclic instrument after a measured
subset-sum fiber. Its only failure is a singleton fiber. The complete
rank scan still costs exponential work and is counted. A seven-moment
bound separates the ACTUAL ideal renewal laws of this instrument and the
incumbent disjoint rule on independent uniform next blocks. In particular,
for r=b+1 and b>=8191 their success probabilities satisfy
p_cycle>=5/6 and p_pair<=149/180. The source renewal improvement is at
least a factor (149/150)^h for h such levels on the SAME schedule.
This is different from improving a loose published upper bound.

The polynomial improvement in the displayed time bound also uses a
stronger success analysis that is available to the OLD instrument: its
uniform-input success is at least 3/4. We do not claim that improvement as
unique to cyclic extraction. Canonical all-fiber pairing, held-out bits,
streaming scans and depth-first evaluation are existing techniques.

Immediate material source: PSW1, submission
47eb8d87-5c1c-4841-a31f-24d0eb67902f, immutable commit
ed0818cb261383a619ca22b8c91f42b2ea267d0a, proof SHA-256
8fc092246c970b5f0cbbf5f8efb837ef50df2184cddc221a7db5b5e583f97d0d.
Its Sections 1-3 and 6-7 are reproduced with notation changes and minor
clarifications. Its integer profile, two-budget construction and profile
estimate are adapted in Sections 4,8,9. The complete arguments are here;
no external proof or previous acceptance is a premise.

The directly audited PSR2, SLS and CS1 sources supply the underlying
streamed combiner, comparator rank, latent-label extraction, source
transforms, untouched-bit proof and all-modulus decoder. Their exact
identities and line references are recorded in evidence.json. PSW2 and
PSG1 are comparison sources: we do not execute their truncated-base or
bounded-Grover algorithms. PSW2 already improves PSW1's sample envelope.
PSG1 has a better leading time AND sample envelope than CYC1 at the same
space orders. CYC1 is not claimed to dominate the current public frontier.
It improves the exhaustive-rank family and proves a reusable local theorem.

The cyclic proposal was developed in this project's unpublished
conditioning report by a GPT-6 Astra max research worker, then independently
audited and integrated here by GPT-6 Astra max in Codex. The audit adds
explicit reference contributions for exceptional matrices in the moment
bound and uniform all-D rational caps. Local GPU/HashSmash work supplied
exact-observable enumeration and representation/cost discipline, not a
DCP asymptotic premise. No GPU instruction is a free DCP operation.
Section 11 distinguishes the finite evidence and failed approaches.

## 1. Charged implementation conventions

All arithmetic is on explicit bit strings. A w-bit add, comparison, copy or
increment has O(w) Boolean gates using ripple carry, with O(w) scratch.
Reversibly compute a Boolean circuit, copy out its answer, then reverse it;
a permutation can be computed into a fresh register, swapped, and erased by
its inverse. NOT, CNOT and Toffoli suffice, and Toffoli has an exact constant
Clifford+T decomposition. Wire counters, generation, initialization, resets,
measurements and classical reads/writes are counted. Every indexed action
also pays O(log(S_C+S_Q+2)) bit operations. Gates are generated in streaming
order; no circuit description of exponential length is stored.

Only H, S, S-dagger and these exact reversible gates are used. In particular,
there is no arbitrary-N QFT circuit or approximate rotation to synthesize.
Fourier LABELS are inferred by nondestructive translation tests, with their
precision, tests and global error budget charged below. The source is used
only for fresh mixed copies; no purification, preparation inverse/control,
QRAM, hidden-shift oracle or subset-sum oracle is available or used.

Write N=2^a2 M with M odd, d=floor(log2 N), omega=exp(2 pi i/N),
s1=s mod M and s=s1+M s2 (mod N), 0<=s2<2^a2.

## 2. Source identities and exact transforms

Let chi_k = N^(-1/2) sum_u omega^(k u)|u> and phi_k(s) = (|0> + omega^(-k s)|1>)/sqrt 2.
Substituting |u> = N^(-1/2) sum_k omega^(-k u) chi_k into
rho_s = (1/N) sum_x |psi_x><psi_x|, with psi_x = (|0,x> + |1,x+s>)/sqrt 2, gives

    rho_s = (1/N) sum_(k=0)^(N-1) |phi_k(s)><phi_k(s)| (x) |chi_k><chi_k|,       (3.1)

because the cross terms k != k' carry (1/N) sum_x omega^(-(k-k')x) = 0.

Latent-label model. By (3.1) each copy is literally a convex mixture, with
uniform weights, of the product states phi_k(s) (x) chi_k. The whole algorithm
is a linear (adaptive) quantum instrument applied to independent copies. So
the joint law of all its classical outcomes equals the law obtained by first
drawing, for every copy, an independent uniform latent label k, and then
running on the product state phi_k(s) (x) chi_k. All probabilities below use
this model. Applying X to the control maps phi_k(s) to, up to a global phase,
the POSITIVE qubit pq_k(s) = (|0> + omega^(k s)|1>)/sqrt 2.

Two exact data transforms act on a fresh copy before label extraction. Each
is a permutation of all 2^n data encodings, extended by the identity on
encodings >= N. Each maps the copy exactly to rho_s' for a known transformed
secret s'. The latent-label model is then applied to rho_s' via (3.1), so the
latent label of a copy is the Fourier label of its TRANSFORMED data register,
which EXTRACT recovers.

(T1) Mult_alpha: u -> alpha u mod N, for a known alpha coprime to N. Since
x -> alpha x is a bijection of Z/NZ, the copy becomes exactly rho_(alpha s).
It is implemented with n controlled modular additions of the constants
alpha 2^v mod N into a clean register, a swap, and the inverse computation with
alpha^(-1): O(n^2) core steps and O(n) scratch.

(T2) Shift_c: if the control is |1>, replace u by u - c mod N, for a known c.
Since |1,x+s> becomes |1,x+(s-c)>, the copy becomes exactly rho_(s-c). This
takes O(n) core steps.

Modular addition of a known constant in [0,N) is a ripple comparison with N,
an addition, a comparison and a selector. It is the identity on encodings
>= N, uses O(n) Boolean gates, and is computed cleanly: compute, swap or XOR
the result out, then uncompute.

## 3. Finite-precision classical table and source-label extraction

For v in [0,4096) the controller computes rationals Cos[v], Sin[v] within 2^-20
of cos(2 pi v/4096) and sin(2 pi v/4096).

- Bound pi within 2^-90 using Machin's formula pi = 16 atan(1/5) - 4 atan(1/239),
  summing the first 40 terms of each alternating arctangent series. This gives
  two-sided bounds; the tails are below 16 (1/5)^81/81 + 4 (1/239)^81/81 < 2^-91.
- The identity follows from tan(2 atan(1/5)) = 5/12, tan(4 atan(1/5)) = 120/119
  and tangent subtraction.
- At the angle 2 v p_mid/4096 < 7, where p_mid is the midpoint of the pi bounds,
  evaluate the degree-80 Taylor polynomials. Their remainders are <= 7^81/81! < 2^-170. The angle error
  is < 2^-89, and sin and cos are 1-Lipschitz.
- Round each value to the nearest multiple of 2^-20.

This is a fixed finite rational computation, charged once as an absolute
constant (not advice).

For x in [0,1) put tab_0(x) = Cos[floor(4096x)] and tab_1(x) = Sin[floor(4096x)],
and let cs_0(x) = cos(2 pi x), cs_1(x) = sin(2 pi x). Since cs is 2pi-Lipschitz,

    |tab_beta(x) - cs_beta(x)| <= 2 pi/4096 + 2^-20 < 1/625.                    (4.1)


EXTRACT uses Qcap fixed in Section 8. Put J_e=n+4,

    h=ceil(log2(2^16 Qcap (n+5))), F=2^21 h.

It runs RUN(F) below once, without verification, fallback or restart.
Conditional on the latent label k, the data register is unchanged by every
test. Afterward discard that register and keep its control qubit, applying X
when the positive phase convention is needed. The latent-label mixture makes
this procedure valid for the mixed source, without access to its purification.

Translation Tr_c: u -> u + c mod N satisfies Tr_c chi_k = omega^(-k c) chi_k.
A TEST WITH SHIFT c (0 <= c < N) works as follows. Prepare an ancilla in |+>.
Apply Tr_((N - c) mod N) controlled by it, so the |1> branch gets eigenvalue
omega^(k c). Measure the ancilla in X (H then Z) or in Y (S^dagger, H, then Z).
The +-1 outcome has mean cos(2 pi c k/N) or sin(2 pi c k/N). Conditioned on
k, chi_k and every spectator are unchanged and outcomes are independent. A test
at LEVEL j is the test with shift 2^j mod N. Each test costs one controlled
modular addition, O(n) core steps.

### Level-wise extraction RUN(F)

For each j = 0..J_e take F tests at level j per basis, giving empirical means
x_j and y_j. Then decode as follows.

Decoding each level. Pick the least dr in [0,64) maximizing
x_j Cos[64 dr] + y_j Sin[64 dr].
- If |x_j - cos| and |y_j - sin| are at most 1/1024, each computed dot product
  differs from cos(2 pi (2^j k/N - dr/64)) by at most 2/1024 + 2^-19 < 1/256.
- The nearest direction has true dot >= cos(pi/64) >= 511/512.
- Any direction at circular distance >= 1/16 has dot <= cos(pi/8) <= 31/32.
- The gap 15/512 exceeds 2/256. So alpha_j = dr/64 is within circular distance
  1/16 of 2^j k/N.

Unwrapping. Set g_(J_e) = alpha_(J_e). For j = J_e - 1 down to 0, let g_j be
whichever of g_(j+1)/2 and (g_(j+1)+1)/2 (mod 1) is circularly closer to alpha_j
(ties: the first).
- Suppose g_(j+1) is within e < 1/16 of 2^(j+1) k/N. The correct preimage is
  within e/2 of 2^j k/N, hence within 1/16 + e/2 < 3/32 of alpha_j.
- The other preimage is at least 1/2 - e/2 from 2^j k/N, hence more than 13/32
  from alpha_j.
- So the choice is correct and the error halves. Finally g_0 is within
  2^-(J_e)/16 = 2^-(n+8) < 1/(2N) of k/N.

RUN(F) outputs floor(N g_0 + 1/2) mod N, which then equals k. On any input it
returns a value in [0,N) after its fixed number of tests.

Concentration. For F independent +-1 variables, the centered log-moment
generating function has second derivative at most 1 (a tilted variance) and
vanishes with its first derivative at 0. Hence
Pr(|mean - E mean| > delta) <= 2 exp(-F delta^2/2). With delta = 1/1024 and
F = F(h) this is 2 exp(-h). So RUN(F(h)) returns a value other than k with
probability at most 4 (J_e + 1) e^(-h) = 4 (n+5) e^(-h), uniformly in k.
RUN(F(h)) uses 2 (J_e + 1) F(h) tests, that is O(n^2 h) core steps.


Since e^-h <= 2^-h, the per-call probability of an incorrect label is at most
4(n+5)2^-h <= 1/(2^14 Qcap). The union bound for at most Qcap adaptive calls is
2^-14, including discarded copies. Couple to an ideal run which outputs the
true latent label on every call, ignoring EXTRACT's internal test outcomes.
No later choice uses those internal outcomes. This coupling preserves the
untouched-bit argument; one does not condition it on extraction succeeding.
Each call takes O(n^2 h+n^2) core operations, O(n) qubits and O(n^2) classical
bits. For unwrapping store the n+5 six-bit directions; handle one empirical
mean at a time with binary counters. All loops have their stated fixed bounds.

## 4. Integer profile and exact cyclic combiner

For n>=256 define delta(v)=ceil(log2(2(v+1)))=1+bit_length(v), v>=1.
Starting at an integer R>=1, repeatedly subtract delta(v) until v<=0.
Write the positive values in reverse order as v_1,...,v_m=R; write v_0
for the terminal value. Then v_i-v_(i-1)=delta(v_i) and v_0 is -1 or 0.
Indeed delta(v)<v for v>=5 and direct checking of v=1,2,3,4 gives
terminal -1,-1,0,0. Choose the LEAST positive R for which
S(R)=sum_i v_i>=n. Search R=1,...,n, generating each profile with integer
arithmetic. This terminates because S(n)>=n; no monotonicity of S is assumed.
Set q0=2^(R+1). Section 9 proves R=O(sqrt(n log n)).

A CYC_TREE_D call, 1<=D<=n, has a supplier of independent leaf phase
qubits with known labels uniform on [0,2^D) in the ideal run. Put B=D-1.
Allocate b_i greedily from i=m down to 1, assigning the smaller of v_i
and the still unallocated part of B. Thus 0<=b_i<=v_i and sum_i b_i=B.
A zero-width level returns its child without a combiner. A nonzero level
has r_i=b_i+1 children and cancels bits p_i,...,p_i+b_i-1, where
p_i=sum_(j<i)b_j. A level-0 call returns one leaf. If B=0 simply return
one leaf; do not perform a recursive walk through zero-width levels.
Other leading zero levels can also be skipped using a saved start index.

Each positive level builds r_i independent child outputs depth first,
retaining earlier siblings. A failed attempt discards all its inputs and
rebuilds them from fresh source copies. After the children are built,
charge weight 2^v_i to the global weighted counter BEFORE this combiner's
execution; abort if the new total would exceed Wcap. Section 8 defines
Wcap and also a separate acquisition cap.

For one attempt the stored labels a_j are divisible by 2^p. The ideal
state, with the unknown fixed phase parameter th supplied by the stage, is

    2^(-r/2) sum_(x in {0,1}^r) exp(2 pi i th A(x)) |x>,
    A(x)=sum_j a_j x_j,       K0=2^r,       M0=2^b.

K0 and M0 here are local, distinct from the decoder K and odd modulus M.
The following circuit is fully explicit.

1. Compute (A(x)/2^p) mod M0 into scratch, measure its residue e and
   clear the measured register. The fiber F_e has size m_e and consists
   of x_0<...<x_(m_e-1) in ORIGINAL BINARY SUBSET ORDER. This measurement
   has probability m_e/K0, independent of the phases.
2. Enumerate all classical y=0,...,K0-1. Compute its low residue from the
   stored labels. For y in F_e, increment a classical size counter and
   reversibly add the comparison bit [y<x] into a clean (r+1)-bit quantum
   rank register. Uncompute comparison scratch immediately. The result
   on x_j is rank j, while the old subset register is retained.
3. If m_e=1, discard the inputs and report FAIL. Otherwise append a fresh
   qubit c=|+> and apply the reversible permutation

       |j,c> -> |(j-c) mod m_e,c>.

   On encodings j>=m_e use the identity, separately for c=0 and c=1.
   A controlled modular decrement with comparison, ripple arithmetic and
   compute/swap/inverse implements this in O(r) core gates and scratch.
   Measure the entire modified rank, obtaining t in [0,m_e).
4. Scan the classical subsets again to find x_t and x_((t+1) mod m_e),
   and calculate their full integer sums. Given t, the remaining state is

       (exp(2 pi i th A(x_t)) |x_t,0>
        +exp(2 pi i th A(x_((t+1) mod m_e)))
                              |x_((t+1) mod m_e),1>)/sqrt(2).

   Controlled XOR of the two known subsets, conditioned on c, clears the
   entire old subset register. Reset the measured rank and scratch. Return
   c with the numerical label A(x_((t+1) mod m_e))-A(x_t).

This also works for m_e=2: the two edges have opposite orientations and
produce their corresponding signed labels. Each t has probability 1/m_e.
The rank permutation is bijective on all encodings and there is no
uncomputed copy of j left to destroy interference. The returned label is
divisible by 2^(p+b). Distinct adjacent subsets, including the wrap edge,
have a nonzero difference in at least one child coordinate.

Equivalently the maps on the fiber are

    K_t=(|0><x_t|+|1><x_((t+1) mod m_e)|)/sqrt(2).

Each basis vector occurs twice and cross terms vanish because |0>,|1>
are orthogonal. Hence sum_t K_t^* K_t=I on every m_e>=2 fiber. These
are overlapping Kraus maps, not overlapping projectors and not a
classical draw falsely substituted for a quantum projection.

For every fixed list of labels,

    f_cycle=#{e:m_e=1}/K0 <= f_pair=#{e:m_e odd}/K0.

The right side is the actual failure of consecutive disjoint-rank pairs.
The improvement is exactly #{e:m_e>=3 odd}/K0. Either failure is at most
M0/K0=1/2 here, so termination already holds without a uniformity assumption.

Each scan element can recompute a subset sum by r additions of O(n)-bit
integers and perform the rank comparison/increment with clean ripple
circuits. A conservative O(n^3) core bit/gate/generation charge per element
covers all such work, including arithmetic counters, signed sums and all
scratch cleanup. The constant number of K0-entry scans therefore costs
O(n^3 2^v_i). The small cyclic permutation does not add an exponential
scan or a source copy. We retain only two selected subsets and their sums,
never a list of K0 records. All addresses are charged in Section 9.

A returned root involves q_D=product_(i:b_i>0)(b_i+1) disjoint retained
leaves. Inductively its integer label is a signed sum of their leaf labels,
with coefficients in {-1,0,1}, not all zero. Disjoint child leaf sets
prevent cancellation of a nonzero coefficient from a changed child.
Moreover

    q_D <= product_i 2(v_i+1) <= product_i 2^delta(v_i)
        =2^(R-v_0)<=q0.

Thus the root label is 2^B W with integer |W|<2q0. All partial sums and
stored labels have O(n+R)=O(n) bits. These numerical bounds also hold on
incorrect-label branches: EXTRACT always returns a value in [0,N), and
leaf acceptance or reduction forces labels into [0,2^D). They are not
conditional-success resource bounds.

## 5. Untouched suffix, survival and seven moments

### 5.1 Uniformity without conditioning on a future cutoff

Write each leaf label k_l=low_l+2^p u_l. Condition only on leaf low p bits
and the subtree's residue, rank/edge and retry transcript through bit p.
All conditioned probabilities and decisions depend only on those low
bits, not phases or u_l. The u_l remain independent uniform modulo
2^(D-p). The returned numerical label divided by 2^p is a known integer
plus a signed sum of u_l with a nonzero coefficient +1 or -1. It is
therefore uniform modulo 2^(D-p). Independently generated siblings use
disjoint leaves and give independent uniform residues in the next block.
This induction includes failed attempts. Its termination is supplied by
the distribution-free 1/2 success bound above, so there is no circular
assumption of termination from the stronger uniform law.

Full labels may be computed and stored, but pair order, retry decisions
and selection use only the designated low bits. Neither full-label sorting
nor conditioning on future cap survival is allowed. EXTRACT's internal
records are averaged out in the ideal run of Section 3. The actual run
is compared to that run by additive error coupling, never by conditioning
on correctness of every extracted label.

At the root, p=B=D-1. Conditional on the low-bit transcript and past roots,

    W=c0+sum_(S+) tau_l-sum_(S-) tau_l,
    |S+|+|S-|>=1,        tau_l independent fair bits.

Consequently

    |E exp(2 pi i y W)| <= |cos(pi y)|,       Pr(W odd)=1/2.       (5.2-3)

This is Lemma 5.1 used by the decoder below. The integer W need not be
uniform. It is the untouched fair-bit factors that give the estimates.

### 5.2 A bound already available to disjoint pairs

For independent uniform a_j/2^p modulo M0 and r=b+1, the mean disjoint
failure is at most 1/4. Before the last label is added let S be the set
of residues with odd subset counts, with size w. Adding an independent
uniform shift takes S to S symmetric-difference (S+a). Its conditional
mean size is 2w(1-w/M0)<=M0/2. Divide by K0=2M0.
Cyclic failure is pointwise no larger, so p_cycle>=3/4 at EVERY b>=1.
This is an averaged fresh-attempt guarantee, not a fixed-label guarantee.

### 5.3 A strict separation for large blocks

Let a_j be independent uniform residues modulo M0=2^b, r=b+1, K0=2^r.
Choose a uniform subset X. For Y=X xor z, A(Y)-A(X) is the subset sum
of z with labels (1-2X_j)a_j, which are still independent uniform residues.
The number of OTHER members of the measured fiber therefore has the law

    Z=#{z in {0,1}^r, z!=0 : sum_j a_j z_j=0 mod M0}.

The measured-residue size bias is included. In particular,

    E f_cycle=Pr(Z=0),    E f_pair=E[1_(Z even)/(Z+1)].           (5.4)

For 1<=k<=7 put mu_k=E binom(Z,k), and mu_0=1. We prove, for r>=8192,

    |mu_k-2^k/k!| <= E_r,
    E_r=2^28/M0+2^70(63/64)^r <2^-50.                         (5.5)

Expand k!mu_k over ordered distinct nonzero binary rows z_1,...,z_k,
a k-by-r matrix A. The independent reference assigns each tuple probability
M0^-k; its total is (K0-1)_k/M0^k. Full F_2 rank gives an odd minor,
invertible modulo 2^b, so its probability equals the reference exactly.
There are at most (2^k-1)2^((k-1)r) matrices of deficient F_2 rank: choose
a nonzero left null vector and its at most 2^(k-1) allowed column values.
If such a matrix has full rational rank, a nonsingular integer minor has
absolute determinant <=k!, and its zero probability is <=k!/M0^k.
The absolute difference from the reference contributes at most

    (2^k-1)(k!+1)2^(k-1)/(k! M0).

For rational rank d<k, at most 2^(kd) column spans are possible: choose a
basis of d binary columns. Such a span contains at most 2^d-1 binary
vertices for any admissible distinct-nonzero-row matrix. Project onto d
independent coordinates. If all 2^d binary vectors occurred, each other
coordinate would be a linear form taking only 0 or 1 on the whole cube.
Evaluation on unit vectors makes its coefficients 0 or 1, and evaluation
on their sums permits at most one coefficient 1. Thus that coordinate
would be identically zero or duplicate a pivot coordinate. One row of A
would be zero or duplicate another, a contradiction.

There are therefore at most 2^(kd)(2^d-1)^r such matrices. Condition on
all but d input variables and use a nonsingular d-by-d minor B. Its kernel
modulo M0 has size at most |det B|<=d!: the kernel and cokernel of a square
map on a finite group have equal cardinality, and its cokernel is a quotient
of Z^d/B Z^d. Hence each zero probability is <=d!/M0^d, even when B has
an even determinant. The REFERENCE CONTRIBUTION of those same exceptional
matrices must also be subtracted. Since M0^-k<=M0^-d<=d!/M0^d,
their combined absolute error is bounded by

    (2/k!) sum_(d=1)^(k-1) 2^(kd) d! 2^d (1-2^-d)^r.          (5.6)

This factor two explicitly includes the reference contribution.
The difference between (K0-1)_k/M0^k and 2^k is at most
[k(k+1)/2]2^(k-1)/M0, by telescoping products of factors K0-i.
After division by k!, its coefficient plus the full-rational-rank
coefficient is <2^28 for k<=7. The sum of coefficients in (5.6) is <2^70;
its slowest decay is (63/64)^r. These elementary integer inequalities are
also checked by diagnostic.py. They prove (5.5).
Since (64/63)^64>1+64/63>2, (63/64)^8192<2^-128. Thus at r>=8192
the second term is <2^-58 and the first is <=2^(29-8192), proving
E_r<2^-50 without a limiting or fitted Poisson assertion.

The degree-six even Bonferroni polynomial gives

    Pr(Z=0) <= sum_(j=0)^6 (-1)^j mu_j
             <=7/45+7E_r<1/6.

For the old pairing rule retain its Z=0 and Z=2 contributions. The degree
seven lower polynomial for Pr(Z=0) and the polynomial
sum_(j=2)^7 (-1)^(j-2) binom(j,2)mu_j for Pr(Z=2) are valid lower bounds.
For an integer Z>2 the latter is binom(Z,2) times an odd degree-five
alternating binomial partial sum for Z-2, hence nonpositive; at Z=2
it is one. Values Z=0,1 give zero. Substitution of 2^j/j! yields

    E f_pair >= 41/315+(1/3)(2/15)-(80/3)E_r
              =11/63-(80/3)E_r >31/180.

The absolute error coefficients total at most 80/3. Thus uniformly for
b>=8191, p_cycle>=5/6 and p_pair<=149/180. We use only the rational
certificate

    sigma(b)=3/4 if 1<=b<8191, and 5/6 if b>=8191.             (5.7)

### 5.4 Actual renewal comparison, not independent bucket heuristics

For a fixed schedule and one of the instruments let p_i be the actual
fresh-attempt success at positive level i. The suffix result makes p_i
a function of (b_i,r_i) only, for every history of prior roots. If E_i
counts expected leaf acquisitions and W_i counts weighted attempts, then

    E_i=r_i E_(i-1)/p_i,
    W_i=(r_i W_(i-1)+2^v_i)/p_i.                             (5.8)

This is a renewal equation with fresh restarts. Attempt cost may correlate
with its own success; independence between them is unnecessary. The
expected cost of the first attempt is added to the probability of failure
times the fresh future expectation. Termination and finite expectations
follow first from the distribution-free bound.

The cyclic p_i is at least the disjoint p_i at every width. At b_i>=8191
their ratio obeys p_pair/p_cycle<=149/150. Therefore on the same schedule,
with the same leaf supplier,

    E_cycle/E_pair <= (149/150)^h,

where h is the number of positive widths at least 8191. This compares
ACTUAL ideal expected source use per returned root. It remains valid for
truncated D profiles, although h can then be small or zero. For D of order
n there are at least (D-1)/R-8191 such levels, since each width is <=R
and at most one width is partial. Hence h=Omega(sqrt(n/log n)) for large n.
We make no claim of a common exponential speedup of the weighted work:
top-level scans need not inherit that many improving ancestors. Nor is
this ideal expectation ratio asserted as a ratio of random capped costs.
## 6. Odd-part recovery by free-frequency decoding

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so N >= 3 * 2^a2
and d - 1 >= a2. Put theta = s1/M in [0,1). Every stage uses D = d, B = d - 1,
nq = q0 and

    K = 2^13 (ceil(log2 nq) + ceil(log2 n) + 30).

The stages are j = 0, 1, ..., J, where J = min{ j >= 0 : 2^(j+3) > 2M }. By
minimality, J + 1 <= log2 M <= n.

Source for stage j. Compute alpha_j by extended Euclid and CRT so that
alpha_j = 1 (mod 2^a2) and alpha_j = 2^j (2^(d-1-a2))^(-1) (mod M). Then alpha_j is a
unit modulo N. A leaf qubit is made as follows:
- acquire a fresh copy and apply Mult_(alpha_j);
- run EXTRACT to obtain k, and accept iff k < 2^d (otherwise discard the copy and
  acquire again);
- on acceptance, apply X to the control.

In the ideal run, accepted labels are i.i.d. uniform on [0, 2^d), each copy is
accepted with probability 2^d/N > 1/2, and the qubit is pq_k(alpha_j s), i.e. it
has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^(d-1) W th = W 2^(d-1-a2) alpha_j s / M = 2^j W s1 / M   (mod 1),            (9.1)

because 2^(d-1-a2) alpha_j = 2^j (mod M) and s = s1 (mod M). So a CYC_TREE_d root of
stage j is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known
frequency f = 2^j W.

Measurement. For i = 1..K:
- run CYC_TREE_d;
- obtain a fair bit beta_i by measuring H|0>;
- measure the root in X (beta_i = 0) or Y (beta_i = 1), recording Z_i in {+1,-1}
  together with W_i and beta_i.

Ideally E[Z_i | f_i, beta_i] = cs_(beta_i)(f_i theta) with f_i = 2^j W_i.

Candidates. Put P_j = j + ceil(log2 nq) + 8, and identify an integer c with the
point zeta = c/2^(P_j) on the circle R/Z.
- Stage 0 uses every c in [0, 2^(P_0)).
- Stage j >= 1 uses every c whose point lies within circular distance
  rad_j = 2^-(j+2) of the previous center z_(j-1). This is one or two explicit
  integer intervals.
- Both z_(j-1) (denominator 2^(P_(j-1))) and rad_j are multiples of 2^-(P_j),
  so the two arc endpoints are themselves candidates.
- There are at most 2^(ceil(log2 nq)+7) + 2 <= 2^(ceil(log2 nq)+8) candidates.

The candidate set is fixed by information available at the start of the stage.

Score. For each candidate, using exact integer arithmetic,

    score(c) = sum_i Z_i * tab_(beta_i)( ((f_i c) mod 2^(P_j)) / 2^(P_j) ).

Enumerate the candidates in increasing order, keeping the K residues
(f_i c) mod 2^(P_j) and updating each with one addition per step, and keep a
running maximum. Let z_j = c*/2^(P_j) for the least maximizer c*. All loops have
fixed lengths, and the decoder returns a candidate on every branch.

Lemma 6.1. Suppose theta is within circular distance rad_j of z_(j-1) (no
condition when j = 0). Then, in the ideal run, with probability at least
1 - 2^-20/n, theta is within circular distance 2^-(j+3) of z_j.

Proof. Let Fs_i be the sigma-field of everything up to and including root i
of the stage, and Gt_i the sigma-field of Section 5 for tree i. For a
candidate point zeta, let Delta = theta - zeta, taken as a circular
difference, and let xi_i = Z_i cs_(beta_i)(f_i zeta). Conditional on
Fs_(i-1), Gt_i and the top bits of tree i (hence on W_i), averaging over the
fair basis bit gives

    E[xi_i | ...] = (1/2)[cos(2 pi f_i theta) cos(2 pi f_i zeta) + sin(..) sin(..)]
                  = (1/2) cos(2 pi f_i Delta).

By (4.1), the computed score differs from sum_i xi_i by at most K/625.

Near point. Let zeta0 be the candidate nearest theta. In stage 0 the
candidates cover the circle. In stage j >= 1 the candidate arc contains theta
and has candidate endpoints. Either way |Delta0| <= 2^-(P_j + 1). Since
|f_i| < 2^j 2 nq,

    |f_i Delta0| < 2^(j+1) nq 2^-(P_j + 1) <= 2^-8.

So E[xi_i | Fs_(i-1)] >= (1/2) cos(pi/128) for every realization.

Far points. Call zeta far if |Delta| >= 2^-(j+3). In stage 0 we always have
|Delta| <= 1/2. In stage j >= 1, both theta and zeta lie within rad_j of
z_(j-1), so |Delta| <= 2^-(j+1). Hence xx = 2^j |Delta| lies in [1/8, 1/2] for
every far zeta. Tree i uses copies independent of Fs_(i-1). By Lemma 5.1, its
top bits are fair and independent given Fs_(i-1) and Gt_i. So by (5.2) with
phi = 2^j Delta, and since a real part is at most the modulus,

    E[xi_i | Fs_(i-1)] = E[ (1/2) Re E[exp(2 pi i 2^j Delta W_i) | Fs_(i-1), Gt_i] | Fs_(i-1) ]
                       <= (1/2) cos(pi xx) <= (1/2) cos(pi/8).

Concentration. For each fixed candidate, sum_i (xi_i - E[xi_i | Fs_(i-1)]) is a
martingale whose increments lie in intervals of length 2. By Azuma-Hoeffding
it deviates by at least K/64 with probability at most
exp(-(K/64)^2/(2K)) = exp(-K/8192). Outside these events for zeta0 and every far
candidate,

    score(zeta0) >= (K/2) cos(pi/128) - K/64 - K/625
                 >  (K/2) cos(pi/8)   + K/64 + K/625 >= score(far zeta),

because cos(pi/128)>511/512 and cos(pi/8)<37/40, and
(1/2)(511/512-37/40)>2/64+2/625. The first bound follows from
cos x>=1-x^2/2 and pi<22/7; the second from
cos(pi/8)=sqrt(2+sqrt2)/2, sqrt2<99/70 and (2+99/70)/4<(37/40)^2.
So the
maximizer is not far. There are at most 2^(ceil(log2 nq)+9) events, and since
e^-x <= 2^-x, exp(-K/8192) <= 2^-(ceil(log2 nq) + ceil(log2 n) + 30). The failure
probability is therefore at most 2^(9-30)/n <= 2^-20/n. QED.

For stage j+1 the hypothesis of Lemma 6.1 is the conclusion of stage j, since
2^-(j+3) = rad_(j+1). By induction, with probability at least 1 - 2^-20, theta
lies within 2^-(J+3) < 1/(2M) of z_J. Output s1 = floor(M z_J + 1/2) mod M. This
equals s mod M because theta = s1/M, and the circular distance handles
wrap-around.


## 7. 2-adic recovery

If a2 = 0, put s2 = 0 and skip this section. Otherwise s - s1 = M s2 (mod N) for
a unique s2 in [0, 2^a2). The bits of s2 are found at levels g = 0..a2-1. Let
s2low be the known low g bits. Put sh_g = s1 + M s2low (mod N), wd = a2 - g, and
rem = (s2 - s2low)/2^g in Z/2^wd. Then s - sh_g = M 2^g rem (mod N).

Leaf qubit for level g:
- acquire a copy and apply Shift_(sh_g), which makes the secret s - sh_g;
- run EXTRACT to obtain k, and apply X to the control.

Ideally the phase is exp(2 pi i k M 2^g rem/N) = exp(2 pi i kk rem/2^wd), with
kk = k mod 2^wd. Since 2^wd divides N and k is uniform on Z/NZ, kk is uniform on
[0, 2^wd). Use kk as the label.

- If wd = 1: if kk = 1, measure X; the outcome is + iff rem is even. If kk = 0,
  discard and repeat.
- If wd >= 2: run CYC_TREE_wd (D = wd). If W is even, discard and repeat. If W is
  odd, the root is (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2,
  and an X measurement gives rem mod 2 exactly.

By (5.3), each attempt succeeds with probability exactly 1/2, even if s1 was
wrong. Set bit g of s2. In the ideal run with s1 correct, every bit is correct.
Output (s1 + M s2) mod N.


## 8. Complete algorithm, exact rational caps and success

For n<256 use exhaustive shift testing. For t=0,...,N-1, take at most
n+10 fresh copies, subtract t modulo N controlled on the first qubit,
and measure that qubit in X. Reject t at its first minus, and output the
first t passing all tests, or 0 if none. The true s always passes; any
wrong t passes each fresh test with probability 1/2. Wrong output has
probability <(N-1)2^(-n-10)<2^-10. The branch uses at most N(n+10)
copies, O(n) qubits, O(n^2) classical bits and O(Nn^4) charged work.
This FIXED finite prefix is absorbed by absolute constants in the claims.

For n>=256 compute the profile in Section 4. Use q0=2^(R+1) and

    K=2^13(R+1+ceil(log2 n)+30),       H0=nK+2n.

Compute the following budgets by exact rational arithmetic BEFORE acquiring
any source copy. For each integer D=1,...,n, generate its greedy widths.
Initialize e=1,w=0. For i=1,...,m, skip b_i=0; otherwise replace

    e <- (b_i+1)e/sigma(b_i),
    w <- ((b_i+1)w+2^v_i)/sigma(b_i).

Save the final numbers e_D,w_D. Keep only maxima

    Emax=max_(1<=D<=n) e_D,         Wmax=max_(1<=D<=n) w_D,
    Qstar=2 Emax H0+2n,            Wstar=Wmax H0,
    Qcap=ceil(1024 Qstar),         Wcap=ceil(1024 Wstar).       (8.1)

Reduce rationals exactly or use common prime-power denominators; compare
maxima by cross multiplication. No floating-point estimate or infinite
search is part of this parameter rule. All counters are exact integers.
Section 9 bounds both this preprocessing and the sizes of its rationals.

Initialize the source and weighted counters to zero. Before acquiring any
copy that would exceed Qcap, abort, release registers and output 0. Before
each positive-level combiner, AFTER constructing its children and BEFORE
running its residue/rank circuit, add 2^v_i or abort if this exceeds Wcap.
A started combiner executes its whole finite circuit. EXTRACT uses this
fixed Qcap in its fixed precision rule from Section 3. Run Section 6 for
the odd part, then Section 7 for the two-adic part, then output
(s1+M*s2) mod N. Source transforms, label extraction, rejection, retries,
parent scans, all root measurements and decoder work are executed as
specified, including when an earlier decoding result was wrong.

Consider first the ideal UNCAPPED process with true latent labels. The
suffix law and (5.7), followed by the renewal argument, give expected leaf
counts at most e_D and weighted attempts at most w_D per root. Every
accepted odd-stage leaf costs N/2^d<2 source copies in expectation. A
two-adic leaf costs one. These bounds hold uniformly given all past roots,
including when past decoder outcomes were wrong. There are at most nK
odd-stage root calls. Each of at most n two-adic bits takes two roots in
expectation by the untouched parity bit, or two direct source copies
when wd=1. Fresh attempts justify this even when a root's cost correlates
with its parity. Thus the expected source total is <=Qstar and the
expected weighted total is <=Wstar. In particular all the ideal loops
terminate almost surely.

The capped ideal run agrees with the uncapped run unless one of its totals
would exceed its cap. Each probability is <=1/1024 by Markov. The work-cap
check occurs after constructing children, whose earlier acquisitions and
attempts are already charged; aborting there means the full uncapped total
would exceed Wcap. The probability of any source-label error in the actual
capped process is <=2^-14 by Section 3, including rejected copies and
calls preceding an abort. Couple to the ideal process until the first
such disagreement. This is an additive failure bound, not conditioning
on extraction success or on cap survival.

The ideal odd decoder fails with probability <=2^-20. Given its success,
the ideal two-adic measurements are exact. The union bound, requiring no
independence of these events, gives failure at most

    2^-10+2^-10+2^-14+2^-20 <2^-8.

The finite branch also meets this guarantee. Hence success at least
1-2^-8 is unconditional for every N and s with this ONE configuration.

## 9. Every-branch resources and supported envelopes

### 9.1 Integer profile estimates

Let D_R=max_(1<=v<=R)delta(v)=1+bit_length(R)<=log2 R+2. The descending
steps are intervals of length at most D_R; rectangles of heights the
successive positive values cover [0,R]. Therefore

    R^2/2=integral_0^R x dx <=D_R S(R),
    S(R)>=R^2/(2D_R).                                      (9.1)

For n>=65536, L=log2 n>=16, let Rtest=ceil(sqrt(nL)+sqrt n).
Then Rtest<=sqrt n(sqrt L+9/8) and

    log2 Rtest <=(L+log2 L+1)/2,
    2D_Rtest <=L+log2 L+5.

The first follows from 1+9/(8sqrt L)<=41/32<sqrt2. Also
2sqrt L-log2 L-4>=0 for L>=16: equality holds at 16 and its derivative
1/sqrt L-1/(L ln 2) is positive thereafter. Consequently

    Rtest^2>=n(L+2sqrt L+1)>=n(L+log2 L+5)>=2nD_Rtest.

By (9.1), Rtest is feasible, so the least chosen R<=Rtest. In particular,

    2^R=O(2^(sqrt(nL)+sqrt n)),
    R<=2sqrt(nL),            m>=n/R>=(1/2)sqrt(n/L)          (9.2)

on that range, because n<=S(R)<=mR. For 256<=n<65536, R<=n gives an
absolute outer constant; no new branch or different parameter choice is
introduced there. Also S(R)<=R^2, hence R>=sqrt n and 2^R>=n for n>=16.

### 9.2 Uniform bounds for the rational budgets, including partial widths

Put a_i=(b_i+1)/sigma(b_i) for active levels and a_i=1 for shortcuts.
For EVERY b_i<=v_i, even a partial width below the 8191 threshold,

    a_i <= (2/3)2^delta(v_i).                              (9.3)

For positive b this follows from sigma>=3/4 and
2(v_i+1)<=2^delta(v_i); for zero b it is immediate. If v_i>=9101, a
stronger bound holds:

    a_i <= (3/5)2^delta(v_i).                              (9.4)

For b_i>=8191 use a_i=6(b_i+1)/5<=6(v_i+1)/5. For b_i<8191 the
worst positive value is 4*8191/3<6*9102/5<=6(v_i+1)/5. A shortcut
again satisfies the bound. This explicitly handles a small partial block
at a large nominal level. At most 9100 distinct profile values are <9101.
Since (3/5)^3<1/4, telescoping (9.3)-(9.4) gives uniformly in D

    e_D=product_i a_i
        <=2^(R+1) (2/3)^ell (3/5)^(m-ell)
        <=2^(R+1+9101-(2/3)m),       ell<=9100.            (9.5)

The large absolute factor here is only an analysis constant. The actual
caps use the exact rational recurrences (8.1), not this loose bound.
Combining (9.2) and (9.5),

    Emax=O(2^(sqrt(nL)+sqrt n-(1/3)sqrt(n/L))).             (9.6)

For weighted attempts, expand the recurrence. Each active level contributes
(2^v_i/sigma(b_i)) product_(j>i)a_j. Even when some ancestors are shortcuts,
(9.3) and telescoping show this is at most

    (4/3)2^R (2/3)^(m-i).

Summing the finite geometric series gives, for all D,

    w_D<=4*2^R,             Wmax<=4*2^R.                  (9.7)

This removal of a factor m is an accounting improvement also available to
the disjoint-pair instrument under its proved uniform-input 3/4 bound.
The stronger cyclic certificate matters to (9.5) and the ACTUAL renewal
comparison in Section 5.4. It is not needed for (9.7).

K=O(R+log n)=O(sqrt(nL)) and H0=O(n^(3/2)L^(1/2)). Thus EVERY branch has

    Q<=Qcap
      =O(n^(3/2)L^(1/2)
          2^(sqrt(nL)+sqrt n-(1/3)sqrt(n/L))),
    Wcharged<=Wcap=O(n^(3/2)L^(1/2)2^R).                  (9.8)

The additive 2n, ceiling terms and finitely many small n are covered by
absolute constants. They do not hide a missing log-log term in an exponent.

### 9.3 Space and precision

A depth-first tree retains at most sum_i(r_i-1)+1=B+1<=n phase qubits
as siblings/current outputs. The cyclic ancilla, rank, sum/comparison
scratch, source transforms and EXTRACT need O(n) additional qubits,
reused between calls. Discarded inputs are reset and released. Thus S_Q=O(n).

There are O(n) retained labels, each O(n+R)=O(n) bits, so they occupy O(n^2)
classical bits. A profile uses O(m log n) bits. Exact E and W rational
numerators/denominators have O(R+m+log m)=O(n) bits: each division introduces
only one factor 3 or 5; product numerators are bounded by O(2^R), and adding
at most m weighted terms enlarges the length by at most O(m+log m).
Cross products during comparison also have O(n) bits. Iterate over D,
keeping only its profile and two maxima; store no n-by-m array of rationals.
The integer budgets, EXTRACT's h and all budget snapshots at depth m use
O(m(R+log n))<=O(n^2) bits. In particular log2 Qcap=O(R+log n)=O(n),
so h=O(n) and the source-label precision proof applies to these new caps.

The single streaming subset counter, size/rank counters, two saved subsets,
sums, arithmetic registers and on-demand gate descriptor fit in O(n^2)
classical bits. The decoder stores K=O(n) frequencies and residues of O(n)
bits each. Its fixed trig table has constant size and is computed uniformly.
Therefore S_C=O(n^2), even on incorrect-label and abort branches. Every
classically indexed action pays O(log n)=O(L) address work. Quantum-addressed
lookup is implemented by the counted streaming comparisons, not QRAM.

### 9.4 Work on actual capped branches

The combiner cost O(n^3 2^v_i) includes its classical enumeration, reversible
circuit generation, Clifford+T gates, residue/rank measurements and resets.
The weighted cap therefore gives total combiner core work

    O(n^3 Wcap)=O(n^(9/2)L^(1/2)2^R).

All acquisition, transform and EXTRACT core work is at most O(n^3 Qcap)
since h=O(n). Using even the weaker Emax<=2^(R+1) makes this at most
O(n^(9/2)L^(1/2)2^R). Each acquisition also costs n+1 charged units.
Neither bound assumes labels are correct. The source cap is enforced before
acquisition and a started EXTRACT executes its fixed finite number of tests.

The classical decoder scans at most O(q0) candidates per stage. Each of
K records costs at most O(n) core work per candidate after initializing its
modular frequency residue. There are at most n stages, K=O(n), so the
conservative O(n^4 2^R) bound covers initialization, dot scores and all exact
modular arithmetic. Correct decoding is not assumed for this work bound.
Profile search, all n rational recurrences, Euclid/CRT and fixed-table
precomputation fit in O(n^6) core operations by schoolbook arithmetic.
Since R>=sqrt n, n^6=O(n^(9/2)L^(1/2)2^R). This absorption is an eventual
exponential-over-polynomial bound with an absolute finite-prefix constant.

Tree control, zero-level skips, budget checks and disposal are also covered:
a nonterminal active call has a child, and every realized call eventually
reaches a charged acquisition or attempted combiner, except the final abort
stack of depth <=n. Charging O(n^2) core operations per such event and
O(n^3) for that stack suffices. There is no uncharged traversal of an
exponentially stored tree. Only the live DFS stack is allocated.

Multiplying by the full O(L) address factor and adding source work proves

    T=O(n^(9/2)L^(3/2)2^R)
     =O(n^(9/2)L^(3/2)2^(sqrt(nL)+sqrt n)).

Thus work, both spaces and source acquisitions hold jointly on every
branch for the single algorithm and caps (8.1).

### 9.5 Exact rational growth indices

The logarithm of each time/sample envelope has dominant term sqrt(nL).
Its terms +/-sqrt n and -(1/3)sqrt(n/L), where present, are lower order;
the polynomial and log prefactors add O(log n). Thus log2 log2 B divided
by log2 n tends to 1/2. The envelopes n^2,n have index 0. These are exact
rational indices for supported dcp-bounds-v4 expressions, not fits. Only
time supplies the numerical score [1/2].

## 10. Fractional error tolerance

The fifth claim is epsilon(n)=0, with exact error-model text:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

For every N>=2 and s, this means all acquired copies must be independent
ideal copies of the specified rho_s. At most floor(0*Q)=0 may be malformed.
The stated success and all four resource bounds hold together under this
promise. It is a proved zero guarantee, not an impossibility of a positive
one. There is no unproved noisy-input or adversarial robustness assertion.

## 11. Comparison, diagnostics, limitations and source transfer

PSW1 gives T=O(n^5 L^2 2^(sqrt(nL)+sqrt n)) and
Q=O(n^(3/2)L^(1/2)2^(sqrt(nL)+sqrt n)), at these space orders. PSW2 already
keeps that time bound and improves Q to
O(n^(7/4)L^(3/4)2^(sqrt(nL)+sqrt n-(1/2)(nL)^(1/4))). CYC1's declared T
is smaller by n^(1/2)L^(1/2), and its Q is asymptotically smaller than
both: sqrt(n/L)/(nL)^(1/4)=n^(1/4)/L^(3/4) tends to infinity. The common
clean-copy model and same memory orders allow comparison of these joint
guarantees. This is not a claim that their unknown actual running times
attain their displayed bounds. In fact disjoint pairing also permits the
geometric work sum and some stronger source accounting. The strict cyclic
renewal separation of Section 5.4 is the structural contribution.

The consulted PSG1 proof declares O(n^5 L^2 2^((3/4)sqrt(nL))) work and
O(n^(3/2)L^(1/2)2^((3/4)sqrt(nL))) copies at O(n^2),O(n) spaces. Those
envelopes are asymptotically better than CYC1's. Its bounded-Grover
fiber-discovery construction is not imported here. Other vector-table
sieves have faster leading time with larger classical space. No current
frontier or global-priority claim follows from this local instrument.

The rerunnable diagnostic is supplementary evidence. It checks finite
cyclic basis maps and cleanup for all small fiber sizes, exact Kraus
completeness, the planted size-biased law and Bonferroni/rank constants,
small untouched-suffix cases, exact profile recurrences, partial-width
certificates, and finite three-mask identities. It cannot prove the
all-n theorem by enumeration, simulate the full capped quantum algorithm,
or validate gate costs by wall-clock time. The analytic proof supplies
those obligations. Evidence hashes bind consulted source bytes, not truth.

Local GPU work exhaustively censused 15,018,684 multisets across
(b,r)=(4,4),(4,5),(4,6),(5,6),(5,7), using checked multinomial weights,
CPU aggregate comparisons and 2,570 independent histogram/subset probes.
Those finite results are NOT used as a bound for arbitrary b. The exact
observable compression retained occupancy A, singleton S and odd-parity P:

    A'=A | shift(A),
    S'=(S & ~shift(A)) | (shift(S) & ~A),
    P'=P xor shift(P).

This preserves the three observables, not full counts or coherent rank.
For a histogram with s0 singletons and u occupied residues modulo M0,
an independent uniform next shift satisfies

    E[s_next | histogram]=2s0(1-u/M0).

Each singleton has M0-u shifts placing a zero in the other summand, in
each of two disjoint directions. There is no factorization of E[s0*u].
The identities helped diagnose the instrument. Storing 2^b-bit masks or
executing GPU SIMD is not free in the benchmark, and CYC1 does neither.

HashSmash supplied methodological prompts: exact support and mass counting,
full record/index accounting, order-preserving state retention and charging
all work. No SHA kernel, HashSmash asymptotic result or cross-challenge
submission ID is imported. These local unpublished contributions are
credited in prose and source hashes, not invented public dependencies.

Rejected approaches remain relevant. Uniform averaging does not justify
sampling a classical pair in place of a quantum instrument. The second
moment alone gives only cyclic success >2/3, weaker than the old rule's
3/4 certificate. Generic sorted-table compression omits permutation/index
information unless explicitly restored; full-label sorting can reveal
held-out bits. For two independent one-bit labels, cyclic pairing in
canonical subset order gives odd output probability 1/2, while ordering
by full sums with stable ties gives 3/8. The diagnostic reproduces this
counterexample. No generic block-table memory saving is claimed here.
