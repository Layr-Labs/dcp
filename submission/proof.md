# CYG1: cyclic extraction after bounded Grover discovery

## 0. Joint theorem and provenance

For every integer N>=2 and every s in Z/NZ, put n=ceil(log2 N) and
L=log2 n. CYG1 is the single algorithm specified below, including its
integer profile, finite branch and exact rational all-D resource caps.
From independent ideal copies of the stipulated mixed coset state it
recovers the entire s with unconditional probability at least 1-2^-8>2/3.
On EVERY branch, including wrong labels, failed searches, retries and aborts,

    T = O(n^(9/2) L^(3/2) 2^((3/4)sqrt(nL))),
    S_C = O(n^2) bits,       S_Q = O(n) qubits,
    Q = O(n^(3/2) L^(1/2)
          2^((3/4)sqrt(nL)-(5/6)sqrt(n/L))).

The expressions apply for n>=2; the explicit finite branch covers n=1.
All outside constants are absolute. The exact resource growth indices are
[1/2,0,0,1/2]. The fifth claim is epsilon(n)=0 with the exact clean-copy
model of Section 10. No cube-root time or positive tolerance is claimed.

Immediate material sources are CYC1, submission
7a4cecdc-7941-4027-8c95-8520de9fbcf3, and PSG1, submission
c2debeff-5a63-4336-9902-6b84cb6e4289. CYC1 supplies the overlapping cyclic
instrument, seven-moment theorem, all-D rational caps and most source/decoder
proof text. Its submitted proof SHA-256 is
e75607fc05101e99cac8480cfbffc23729c64f6f5a03643ee02de917274b4a17.
PSG1 supplies the separate-register bounded-Grover discovery, exact query
circuits, work-balanced profile, averaged termination proof and comparison
instrument. Its immutable commit is 13b1d5d96ffe70ee4caaac1f6da00bbcdb43f687,
and proof SHA-256 is
4cf69b21f0ecb1d6858ef57eeebe9db892e999d0a132a244efc68d901356907e.
CYC1's immutable candidate commit is
cd8f16692833b52dd0fd3a8dd335667eec5a6e61. Its public proof was retrieved
and verified byte-for-byte against the preserved submitted snapshot.
Both sources are material regardless of subsequent review or promotion.
No prior accepted verdict is a mathematical premise.

The new combination projects onto a constant-size VERIFIED list and applies
the cyclic map there. It is exact even when discovery is incomplete. A second
factorial moment gives a sharper size-biased large-fiber tail. Together with
CYC1's survival theorem this gives success >=37/50 at every positive width,
and >=83/100 for b>=8191. Against PSG1 with identical discovery parameters,
actual expected source use improves by at least (745/747)^h for h large
levels on the same schedule. This is an ideal renewal comparison, not a
ratio of realized capped costs or an end-to-end time speedup.

The uniform survival analysis and geometric weighted sum also improve the
old disjoint instrument's certificates. They are not uniquely cyclic gains.
The exact finite budgets, partial-width threshold and negative source term
are proved for one fixed algorithm here. The basic source identities,
streamed arithmetic, low-bit reasoning and decoder originate in PSW1, PSR2,
SLS and CS1 and are inherited through CYC1 and PSG1. Evidence.json records
the exact material features and both-endpoint citations. No previous verdict
or external proof is a premise. Grover and random-iteration search are
established techniques; their needed search formula is derived below.

The refreshed public PSG2 and PSG9 results are comparison sources only.
PSG9 already has better joint time and source envelopes at these space
orders than this PSG1-profile candidate. CYG1 is not claimed to dominate
that frontier. Section 11 compares all resources and the error model.

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

## 4. Work-balanced profile and bounded-search combiner

Main-branch parameters are computed once for n>=256. For a positive integer v,

 delta(v)=ceil(log2(3(2v+1)))=bit_length(3(2v+1)-1).

Starting at R, descend by v<-v-delta(v) until nonpositive. Reverse the
positive values to obtain v_1,...,v_m=R, with terminal v_0 in[-3,0].
Indeed v>=7 has delta(v)<v; v=1,...,6 gives terminal -3,-2,-2,-1,-1,0.
Choose the least positive R with 2sum_i v_i>=n. This is a finite integer
search with R<=ceil(n/2), since its first capacity term is2R. Generate
profiles and counters by ordinary counted bit arithmetic. Put q0=2^(R+3).

A CYG_TREE_D call,1<=D<=n, has independent ideal leaves with uniform known
labels in[0,2^D). Put B=D-1. When B=0 return one leaf. Otherwise allocate
actual widths b_m,...,b_1 greedily from the root down, b_i=min(2v_i,
B-already_allocated). Then sum_i b_i=B. Let r_i=b_i+1 and
p_i=sum_(j<i)b_j. Level0 returns a leaf. A zero-width level just returns
its child; save the lowest active index and skip leading zero levels. For b_i>0, recursively build r_i fresh child outputs, then check
and add weight2^v_i to the global weighted-attempt counter before executing
the combiner below. If that would exceed Wcap, abort. On FAIL discard ALL
inputs and query scratch, and build fresh children before trying again.
No output label, including zero, is rejected inside the tree merely because
of its higher bits or value.

### 4.1 Exact cyclic output from any verified list

The inputs are phase qubits with full signed labels a_1,...,a_k divisible by
2^p, where k=b+1, b=b_i, p=p_i. Their joint state is

    2^(-k/2) sum_(x in {0,1}^k) exp(2pi i th A(x))|x>,
    A(x)=sum_j a_j x_j.

Set c_j=(a_j/2^p) mod 2^b. Reversibly compute f(x)=sum_j c_j x_j mod 2^b,
measure its residue e, and reset that measured register. The true fiber
F={x:f(x)=e} has size m>=1 and measurement probability m/2^k.
The original phase-index register now has equal magnitudes on F.
Keep it untouched while Section 4.2 discovers H, at most 64 distinct,
classically VERIFIED members of F, on SEPARATE fresh query registers.
Conditioned on classical c_j,e, the entire discovery law is independent of
the original phase amplitudes and uses no higher label bits.

Sort H by original binary subset index, giving x_0<...<x_(h-1).
If h<2, discard the inputs and fail. Otherwise perform these operations.

1. Compute the flag [x in H] by at most 64 equality tests against known
   strings, uncomputing the individual equality scratch. Measure the flag.
   On zero fail and release everything; on one reset it from its known
   value. This is the projector onto H, with success probability h/m.
2. Into a clean six-bit rank register XOR j when x=x_j, using a classical
   loop of at most 64 equality tests and clean equality scratch. On this
   projected subspace the rank is j, and the old x register is retained.
3. Append c=|+>. Apply |j,c> -> |(j-c) mod h,c> on j<h, and the identity
   on j>=h. For each c this is a permutation of all encodings. A controlled
   modular decrement with comparison and compute/swap/inverse arithmetic
   is exact Clifford+T. No unmodified copy of j remains. Measure the new
   rank t, uniformly distributed in [0,h).
4. The remaining normalized state is

   (exp(2pi i th A(x_t))|x_t,0>
    +exp(2pi i th A(x_((t+1) mod h)))|x_((t+1) mod h),1>)/sqrt(2).

   Controlled XOR of the two now-known strings, conditioned on c, clears
   every old subset bit. Reset the measured rank and all scratch. Return c
   with full SIGNED label A(x_((t+1) mod h))-A(x_t), calculated classically.

These operations include h=2 and h=64. On H the Kraus operators are

    K_t=(|0><x_t|+|1><x_((t+1) mod h)|)/sqrt(2).

Every basis element occurs twice, in orthogonal output positions. Thus
sum_t K_t^*K_t=P_H; the failure projector is I-P_H on F. This is a complete
instrument. It is not an overlapping family of projective measurements.
Conditional on any verified H subset of F with h>=2, total success mass is
h/m, while PSG1's adjacent disjoint pairs retain 2 floor(h/2)/m. For h=0,1
both fail. Hence cyclic extraction is pointwise no worse for every list,
including incomplete lists and fibers larger than 64. For a complete fiber
of size >=2 it succeeds with probability one; bounded discovery can add
failure, so the FULL CYG1 combiner is not described as singleton-only.

The returned label is divisible by 2^(p+b). Selected adjacent strings are
distinct, including the wrap edge. They differ in at least one child.
Inductively the label is a signed sum of disjoint original leaf labels,
with coefficients in {-1,0,1}, not all zero. Distinct child leaf sets prevent
symbolic cancellation of a changed child's nonzero incidence vector.
The selection kernel, including membership and rank measurement, uses only
c_j,e, search records and canonical subset indices. It is phase-independent.
Full labels are read for the final arithmetic AFTER selection, without
filtering any output, including zero. This is essential for Section 5.

The at most 64 strings, comparisons, sort, rank permutation, full-label sum,
measurements, resets and complete register cleanup cost polynomial work.
They are included in the complete attempt allowance of Section 4.2.

### 4.2 Bounded discovery, exact Clifford+T circuits

Fix C=64. If k<=7, enumerate at most128 strings and retain the first64
solutions; this has constant enumeration length. If k>=8, use at most64
search blocks. Each block makes at most64 trials, stopping at its first
new verified solution, which is added to the list. Stop discovery after an
empty block or after64 found solutions. The list never contains a duplicate
or a false solution. On each trial:

 * Set J0=2^ceil(k/2), draw uniform j in[0,J0) with ceil(k/2) fair bits.
 * Prepare a fresh k-qubit query in |+>^k. Apply j Grover iterations for
   membership in C_e minus the found list. Measure its candidate string.
 * Verify its residue and novelty classically. Reset query registers before
   the next trial. The original phase-index register is not touched.

Membership is a COUNTED circuit. Controlled additions of the known b-bit
constants c_j compute f(z) in O(kb) gates; compare with e, exclude at most64
known strings with equality flags, apply Z on the computed flag, then
uncompute. This uses O(kb+64k) gates and O(k+b) scratch up to fixed constants.
Diffusion about |+>^k is H^k, a multi-controlled sign flip and H^k; a clean
Toffoli chain implements the sign flip in O(k) gates and scratch. Z=S^2.
All are exact Clifford+T. Known weights and strings are read by a classical
loop emitting gates; no quantum-addressed lookup, QRAM or stored circuit of
exponential length occurs. Gate generation, verification, fair bits, counters,
measurements, resets and all oracle work are charged.
There are at most4096 trials, each with fewer than J0 iterations. Since
k=b+1<=2v_i+1, J0<=2^(v_i+1). Thus one complete attempt costs
O(n^3 2^v_i) core operations and O(n) quantum scratch. The conservative
n^3 factor includes all arithmetic and streamed address generation.
The fixed-size found list needs O(n) classical bits. All these are
branchwise limits, independent of search success.

### 4.3 Discovery probability for every small true fiber

Suppose the measured fiber has at most64 members. At any search trial with
1<=m<=64 remaining solutions, let A=2^k and sin^2(gamma)=m/A. In the
normalized good/bad two-dimensional basis the marking reflection and
uniform-state reflection rotate by2gamma; therefore success after j
iterations is sin^2((2j+1)gamma). Summing the cosine geometric progression
for uniform j gives

 mean success=1/2-sin(4J0*gamma)/(4J0*sin(2gamma)).

For k>=8, m<=64<=A/2, hence sin(2gamma)>=sqrt(2/A) and J0>=sqrt A.
The mean is at least1/2-1/(4sqrt2)>1/4. A64-trial block consequently misses
while solutions remain with probability at most(3/4)^64<2^-16.
Over at most64 relevant blocks, premature stopping has probability at most
64*2^-16=1/1024. Once no solutions remain a block simply finds none;
no counting oracle is used. Small k is enumerated exactly up to the list cap.

## 5. Survival, unused blocks and actual renewal improvement

### 5.1 Exact planted law and second factorial moment

Put M0=2^b, k=b+1 and K0=2^k=2M0. At this point c_j are independent
uniform residues modulo M0; Section 5.4 proves that fresh recursive attempts
supply this law without circular conditioning. The residue measurement has
the law e=f(X) for an independent uniform subset index X. Write Y=X xor z.
Then f(Y)-f(X)=sum_j (1-2X_j)c_j z_j. Conditional on X, the signed c_j
remain independent uniform residues. Therefore the size-biased fiber obeys

    |F|-1 =_law Z,
    Z=#{z in {0,1}^k, z!=0: sum_j c_j z_j=0 mod M0}.

Any two distinct nonzero binary rows z,z' have a determinant +/-1 minor.
If their supports are disjoint, choose one coordinate from each. If they
overlap, choose a common coordinate and one from their symmetric difference.
These exhaust the cases. Consequently their two linear forms are jointly
uniform modulo 2^b: condition on all other labels and invert that minor.
Linearity over unordered distinct pairs gives the ALL-b exact identity

    E binom(Z,2)=binom(2^(b+1)-1,2)/2^(2b)<2.

This is for the measured, size-biased fiber, not a uniform nonempty residue.
Thus

    Pr[|F|>64]=Pr[Z>=64]
       <= E binom(Z,2)/binom(64,2)<1/1008.                 (5.1)

There is no independence assumption involving three or more rows here.
Section 4.3 bounds discovery miss uniformly conditional on any fixed fiber
of size <=64. It can therefore be averaged under this size-biased law.
The exact enumeration branch k<=7 finds every member when |F|<=64;
when |F|>64 the same tail bound still applies, so no small-k gap remains.

### 5.2 Complete-fiber survival shared with disjoint pairing

For independent uniform labels and r=b+1, complete disjoint pairing has
mean failure at most 1/4. Before the last label is added, let S be the set
of residues with odd subset counts, |S|=w. Adding an independent uniform
shift changes S to S symmetric-difference (S+a), whose conditional mean
size is 2w(1-w/M0)<=M0/2. Divide by 2^(b+1)=2M0.
Complete cyclic failure counts singleton fibers instead of odd fibers and
is pointwise no larger. Both complete rules therefore succeed with
probability >=3/4 for EVERY b>=1. This is a fresh-uniform-label assertion,
not a lower bound conditional on an arbitrary fixed list of child labels.

### 5.3 Seven moments for the complete instruments, and bounded-list survival

Let a_j be independent uniform residues modulo M0=2^b, r=b+1, K0=2^r.
Choose a uniform subset X. For Y=X xor z, A(Y)-A(X) is the subset sum
of z with labels (1-2X_j)a_j, which are still independent uniform residues.
The number of OTHER members of the measured fiber therefore has the law

    Z=#{z in {0,1}^r, z!=0 : sum_j a_j z_j=0 mod M0}.

Here f_cycle and f_pair refer to the COMPLETE fiber rules.
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
b>=8191, the COMPLETE cyclic rule succeeds with probability >=5/6, and
the COMPLETE disjoint rule succeeds with probability <=149/180.

For CYG1, loss relative to complete cyclic extraction is at most one on
large-fiber or incomplete-discovery events and zero otherwise. No independence
between these events and singleton failure is needed. The union bound gives

    p_CYG >=3/4-1/1008-1/1024=48257/64512>37/50,
    p_CYG >=5/6-1/1008-1/1024=53633/64512>83/100  (b>=8191).

Fix the following rational certificates for the algorithm and exact caps:

    sigma(b)=37/50 for 1<=b<8191, and 83/100 for b>=8191.   (5.7)

The same small-width >=37/50 certificate also applies to PSG1's disjoint
bounded-list instrument by Section 5.2 and the same two bad-event bounds.
This shared improvement over its old 1/3 certificate is disclosed separately
from the strict actual-law comparison below.

### 5.4 Unused-block uniformity and termination, proved jointly

Lemma U (joint induction). In the ideal uncapped process, every tree-level
call terminates almost surely. If it cancels p bits, its returned label
x/2^p mod2^(D-p) is uniform, conditional on any external past before the
fresh call. Distinct fresh child calls give independent such quotients.

Proof. The leaf statement is the exact uniform latent-label source law.
Assume the statement at the lower level. Before a new node attempt starts,
its freshly generated children have independent uniform quotients modulo
2^(D-p). Their residues c_j modulo the next2^b are thus independent uniform.
Section 5.3 gives conditional success at least37/50 before child generation,
whatever the earlier external past. Every failure releases its inputs and
restarts with fresh children. The geometric bound proves almost-sure
termination and finite expected attempts at this level.

It remains to prove the output law that closes the induction. Fix any
finite successful selection transcript through this level, containing all
used leaf values modulo2^(p+b), search choices/outcomes, residue and cyclic-rank
measurements, and retry choices. Its probability kernel is a function ONLY
of those low parts, by Sections 4.1 and 4.2; quantum searches used separate registers.
Write each original leaf as k_l=u_l+2^(p+b)H_l, with H_l independent uniform
in Z/2^(D-p-b). The selected output has a symbolic signed incidence vector
z_l in{-1,0,1}, not allzero, determined by the low transcript. Consequently

 x/2^(p+b) mod2^(D-p-b)=c+sum_l z_l H_l mod2^(D-p-b).

Here c is an integer determined by the low parts. At least one z_l is a
unit +1 or-1, so the sum is uniform on that cyclic group. Marginalizing over
all finite successful low transcripts proves the output law. Fresh disjoint
leaf sets give the conditional independence for successive child calls.
This conditioning does NOT include irrelevant high-valued EXTRACT records
or all full labels stored by the controller; the ideal process marginalizes
those records and uses exact latent labels. It does not condition on the
event that all actual extractions were correct. The real/ideal comparison
later uses an additive error coupling. Computing/storing full labels does
not change that marginal law: decisions at this level use only the stated
low residues, and do not filter a zero or other high output value. QED.

For every stage, 3r_i<=3(2v_i+1)<=2^delta(v_i). Thus a returned tree has
q_D=product_i r_i<=product_i(3r_i)<=2^(R-v_0)<=2^(R+3)=q0
nominal distinct leaves. Its label is2^B W with integer |W|<2q0. Every
stored label or intermediate sum has O(n+log q0)=O(n) bits, including
incorrect numerical-label branches. No incidence vector is actually stored.

For the root, retain the stronger full-frequency argument as well as Lemma U.
Write each accepted leaf label k_l=u_l+2^B tau_l, with independent fair bits
tau_l. Condition on all low u_l, residue/search/cyclic-rank outcomes and retry
choices, and independent previous roots. All these kernels use bits below
B and are phase-independent, so the tau_l of the returned root remain iid
fair. Its nonzero incidence vector gives

 W=c+sum_(l in S+)tau_l-sum_(l in S-)tau_l, |S+|+|S-|>=1.

Lemma5.1. For every real y, conditional on that low transcript,

 |E exp(2pi i yW)|<=|cos(pi y)|,                            (5.2)
 Pr[W odd]=1/2.                                           (5.3)

Each independent fair bit contributes absolute factor|cos(pi y)|; at least
one is present. The integer c is low-transcript measurable. With y=1/2 the
parity is fair. This is a characteristic-function statement about the full
signed W, not a claim that its integer distribution is uniform.

### 5.5 Actual renewal comparison on the same discovery schedule

For a fixed profile, actual width and identical discovery parameters, let
p_i^C and p_i^P be the fresh-attempt success probabilities of CYG1 and PSG1.
Section 5.4 shows that these are functions of the width and discovery rule,
independent of external history. For each fixed low-label list, residue and
realized discovered H, Section 4.1 gives cyclic success >= disjoint success.
Moreover, disjoint retained mass 2 floor(|H|/2)/|F| is at most
2 floor(|F|/2)/|F|. Averaging and Section 5.3 therefore give

    p_i^P<=p_i^C at every width,
    p_i^P/p_i^C <= (149/180)/(83/100)=745/747  (b_i>=8191).

Let E_i count expected accepted leaf acquisitions per returned level-i
output and V_i expected weighted attempts. With r_i=b_i+1, a fresh-restart
renewal equation gives

    E_i=r_i E_(i-1)/p_i,
    V_i=(r_i V_(i-1)+2^v_i)/p_i.                          (5.8)

The first-attempt cost can correlate with success; no independence between
that cost and its own success is used. Add its unconditional expectation
and then the failure probability times the fresh future expectation.
Joint induction gives finite expectations before these equations are solved.
Thus with the SAME profile, leaf supplier and bounded discovery procedure,

    E_CYG/E_PSG1 <= (745/747)^h,

where h counts active widths >=8191. This includes partial D profiles.
At most one active width is partial. Full widths below 8191 have distinct
nominal v<=4095 and total width <=2sum_(v=1)^4095 v. The additional partial
small width is <=8190. Their total is less than 2^25, an absolute constant.
Every other width is <=2R. Hence h>=(D-1-2^25)/(2R), and for D of order n,
h=Omega(sqrt(n/log n)). This compares actual IDEAL expected source counts
per root, not just improved certificates. With the same independent source
acceptance supplier it also compares fresh source copies per root.
It is not a ratio of realized capped totals, nor an end-to-end work speedup.

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

because 2^(d-1-a2) alpha_j = 2^j (mod M) and s = s1 (mod M). So a CYG_TREE_d root of
stage j is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known
frequency f = 2^j W.

Measurement. For i = 1..K:
- run CYG_TREE_d;
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
- If wd >= 2: run CYG_TREE_wd (D = wd). If W is even, discard and repeat. If W is
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

For n>=256 compute the profile in Section 4. Use q0=2^(R+3) and

    K=2^13(R+3+ceil(log2 n)+30),       H0=nK+2n.

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
running its residue/discovery/cyclic circuit, add 2^v_i or abort if this exceeds Wcap.
A started combiner executes its whole finite circuit. EXTRACT uses this
fixed Qcap in its fixed precision rule from Section 3. Run Section 6 for
the odd part, then Section 7 for the two-adic part, then output
(s1+M*s2) mod N. Source transforms, label extraction, rejection, retries,
parent circuits, all root measurements and decoder work are executed as
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

### 9.1 Deterministic profile estimates

Let S(R) be the sum of the full positive profile. Every descending step is
at most D_R=max delta(v)<=log2 R+5, using 3(2v+1)<=9v and ceil(log2 t)<log2 t+1.
Upper rectangles over [0,R], truncating the final step at zero, give

    R^2/2<=D_R S(R),             2S(R)>=R^2/D_R.

For L=log2 n>=256, test Rtest=ceil((3/4)sqrt(nL)). It satisfies
Rtest<=sqrt(nL), so D_Rtest<=L/2+(log2 L)/2+5. The inequality
8log2 L+80<=L holds at 256 and thereafter: the difference has positive
derivative 1-8/(L ln 2). Hence D_Rtest<=9L/16, while
Rtest^2>=9nL/16. The profile is feasible and minimality gives

    R<=Rtest,       2^R=O(2^((3/4)sqrt(nL))),
    m>=n/(2R)>=(2/3)sqrt(n/L)-8/(9L)
                   >=(2/3)sqrt(n/L)-1.                  (9.1)

The depth bound uses n<=2S(R)<=2mR and
1/(x+1)>=1/x-1/x^2 for x>0, with x=(3/4)sqrt(nL).
The finite main-branch range below L=256 uses the SAME integer search,
with R<=ceil(n/2), and is absorbed by an absolute outside constant.
No new exhaustive branch or favorable-outcome assumption is introduced.
Also 2S(R)<=2R^2 gives R>=sqrt(n/2), so 2^R eventually exceeds every
fixed polynomial. All finite exceptions are absorbed by outside constants.

### 9.2 Uniform all-D bounds, including shortcuts and partial blocks

Set a_i=(b_i+1)/sigma(b_i) for active levels, and a_i=1 for zero-width
shortcuts. For every b_i<=2v_i,

    a_i <= (50/111)2^delta(v_i) < (1/2)2^delta(v_i).       (9.2)

For active levels this follows from sigma>=37/50 and
3(2v_i+1)<=2^delta(v_i). For shortcuts, delta(v_i)>=4 and the inequality
is immediate. If v_i>=4428, a stronger bound holds:

    a_i <= (5/12)2^delta(v_i).                            (9.3)

When b_i>=8191, a_i=100(b_i+1)/83<=100(2v_i+1)/83
<=5(2v_i+1)/4. When 1<=b_i<=8190, a_i<=50*8191/37,
and this is <=5(2v_i+1)/4 at v_i>=4428, since
200*8191=1638200 <=185*8857=1638545.
Shortcut a_i=1 also satisfies (9.3). This covers a small partial actual
width at a large nominal level; no monotonicity across sigma's jump is used.

At most 4427 distinct nominal profile values lie below 4428. Telescoping
sum_i delta(v_i)=R-v_0, with v_0>=-3, gives for every D,

    e_D=product_i a_i
       <=2^(R+3)(1/2)^ell(5/12)^(m-ell),   ell<=4427.

Because (5/12)^4=625/20736<1/32,

    Emax <=2^(R+1110-(5/4)m)
         =O(2^((3/4)sqrt(nL)-(5/6)sqrt(n/L))).           (9.4)

The factor 2^1110 is only a conservative analysis constant. The implemented
caps are the exact rational recurrences in Section 8, not this expression.

For weighted attempts, expand the recurrence. An active level i contributes

    (2^v_i/sigma(b_i)) product_(j>i) a_j
       <=(50/37)2^R (1/2)^(m-i),

since sum_(j>i) delta(v_j)=R-v_i, including shortcut ancestors.
Summing the geometric series proves uniformly for ALL D,

    w_D <=(100/37)2^R,       Wmax<=(100/37)2^R.           (9.5)

The shared >=37/50 certificate gives the same geometric bound to the old
pair instrument under matching new caps. We do not attribute removal of
the depth factor exclusively to cyclic extraction. The large-width cyclic
certificate yields (9.4); the actual comparison is separately Section 5.5.

K=O(R+log n)=O(sqrt(nL)) and H0=O(n^(3/2)L^(1/2)). Therefore

    Q<=Qcap=O(n^(3/2)L^(1/2)
                 2^((3/4)sqrt(nL)-(5/6)sqrt(n/L))),
    Wcharged<=Wcap=O(n^(3/2)L^(1/2)2^R).                 (9.6)

Ceilings, direct calls, the 2n summand and finite exceptions are included
in absolute constants. No unspecified coefficient inside an exponent is
being suppressed.

### 9.3 Space, exact rational arithmetic and precision

A depth-first tree retains at most sum_i(r_i-1)+1=B+1<=n phase qubits as
siblings and current outputs. The original subset register, separate fresh
query register, residue and equality scratch, cyclic control/rank, source
transform and EXTRACT registers use O(n) more. Registers are reset and
reused, including on failed discovery or membership. Hence S_Q=O(n).

There are O(n) retained full labels of O(n+R)=O(n) bits, or O(n^2) total.
The profile needs O(m log n) bits. Exact e,w numerators and denominators have
O(R+m+log m)=O(n) bits: denominators divide 37^m 83^m, and the value bounds
above bound the numerator after use of that common denominator. Comparison
cross products and schoolbook reduction keep O(n)-bit operands. Iterate over
D, storing only its widths, two recurrence values and maxima; no table of
n profiles is allocated. Budget counters and depth snapshots need
O(m(R+log n))<=O(n^2) bits. In particular log2 Qcap=O(R+log n)=O(n),
so h=O(n) in EXTRACT and its stated precision proof applies.

The found list has at most 64 strings, each O(n) bits; its sort, search
counters, full-label sums and streamed gate descriptors fit O(n^2) bits.
Keep K=O(n) decoder frequencies and residues of O(n) bits each. The fixed
trig table is computed, not supplied as advice. Thus S_C=O(n^2) even on
wrong-label and cutoff branches. Every indexed bit access and gate pays
O(log n)=O(L); quantum-addressed membership uses the counted equality and
arithmetic circuits, not QRAM. The abstract symbolic incidence vectors
used in proofs are never stored by the algorithm.

### 9.4 Total charged work on every actual branch

Each bounded attempt uses at most 4096 trials of fewer than 2^(v_i+1)
Grover iterations, or at most 128 enumerated strings in the small branch.
The low-residue oracle, exclusions, diffusion, verification, membership,
cyclic rank circuit and all cleanup are counted in O(n^3 2^v_i) core work.
The exact counter update takes O(R+log n)=O(n) bit work per attempt and
fits that allowance. Thus total combiner core work is

    O(n^3 Wcap)=O(n^(9/2)L^(1/2)2^R).

A started combiner was charged first and finishes its finite circuit.
If a cutoff occurs before it starts, the children built so far have already
been charged. DFS allocation, returns and resets cost polynomial work per
acquired leaf or executed attempt: after skipping zero-width chains, the
visited positive-arity tree has O(number of visited leaves and attempts)
nodes. A single abort can leave at most m unfinished stack frames. Their
polynomial cleanup is covered as well; it does not initiate new queries.

Each acquisition, exact data transform and EXTRACT costs O(n^3) core work
because h=O(n). Even the weaker bound Emax<=2^(R+3) therefore bounds all
source work by O(n^(9/2)L^(1/2)2^R). Each copy also costs n+1 units.
The source cap is checked BEFORE acquisition; all rejected and partially
constructed children count. No step assumes numerical labels are correct.

The decoder scans O(q0)=O(2^R) candidates per stage, with K=O(n) records
and at most n stages. The conservative O(n^4 2^R) core bound covers exact
arithmetic, initialization and all returned centers, including wrong ones.
Profile search, the n rational recurrences, Euclid/CRT and fixed trig-table
computation fit O(n^6) core operations by schoolbook arithmetic. Since
R>=sqrt(n/2), this is O(n^(9/2)L^(1/2)2^R) eventually. Finite exceptions
only enlarge the absolute constant. Gate generation and all memory reads,
writes, measurements, initialization and reset work are included.
Multiplying by the full O(L) address debit gives

    T=O(n^(9/2)L^(3/2)2^R)
     =O(n^(9/2)L^(3/2)2^((3/4)sqrt(nL))).

All four bounds hold jointly for the ONE algorithm and caps of Section 8.

### 9.5 Exact rational growth indices

The logarithms of both time and sample envelopes have dominant term
(3/4)sqrt(nL). The -(5/6)sqrt(n/L) source term is lower order, and the
polynomial/log prefactors add O(log n). Hence their exact index is 1/2.
The space envelopes n^2 and n have index 0. These are supported exact
rational dcp-bounds-v4 declarations, not fitted rates. Only time supplies
the numerical score [1/2].

## 10. Fractional error tolerance

The fifth claim is epsilon(n)=0, with exact error-model text:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

For every N>=2 and s, this means all acquired copies must be independent
ideal copies of the specified rho_s. At most floor(0*Q)=0 may be malformed.
The stated success and all four resource bounds hold together under this
promise. It is a proved zero guarantee, not an impossibility of a positive
one. There is no unproved noisy-input or adversarial robustness assertion.

## 11. Comparisons, finite evidence and limitations

PSG1's public joint envelopes are O(n^5 L^2 2^((3/4)sqrt(nL))) time,
O(n^(3/2)L^(1/2)2^((3/4)sqrt(nL))) source copies, O(n^2) classical bits,
and O(n) qubits, with the identical zero-fraction clean-copy model.
CYG1 improves those declared time and sample envelopes, keeping both space
orders and that model. These are comparisons of proved guarantees, not
claims that prior actual costs attain their published upper bounds.

PSG2, b267909b-a859-49d3-9c64-18eca846b18c, keeps PSG1's time and spaces
and declares Q=O(n^(7/4)L^(3/4)2^((3/4)sqrt(nL)-(1/2)(nL)^(1/4))).
CYG1's negative term is asymptotically larger in magnitude because
sqrt(n/L)/(nL)^(1/4)=n^(1/4)/L^(3/4) tends to infinity; it also dominates
the difference in polynomial prefactors. Thus CYG1 improves this older
joint vector as well. PSG2 is a comparison only; CYG1 uses no truncated
base or PSG2 algorithm.

The refreshed result PSG9, e74645e4-aa15-4084-a89f-9f5b0a32993c, declares

    T=O(n^(5/2)L^2 2^((47/64)sqrt(nL))),
    Q=O(n^(3/2)L^(1/2)2^((141/256)sqrt(nL))),
    S_C=O(n^2), S_Q=O(n), epsilon=0 with the same error model.

Both its leading exponential coefficients are smaller than CYG1's 3/4,
so its declared vector dominates CYG1's despite CYG1's negative lower-order
sample term. Its immutable proof/metric hashes and exact source passages
are bound in evidence.json. This is not a global-frontier improvement or a
claim about numeric-score separation: both have time index 1/2. CYG1's
local cyclic improvement is useful at PSG1's Grover leading envelope;
extending it to PSG9's other mechanisms remains separate work.

CYC1 supplies the instrument and seven-moment theorem but has slower leading
time and sample envelopes sqrt(nL)+sqrt n. CYG1 removes its exponential
full-fiber rank scan by importing PSG1's bounded independent queries. The
new cyclic projection costs only constant-list polynomial work. No source
preparation inverse, purification, coherent source control, hidden subset-
sum oracle, free Grover call, QRAM or free rank operation is assumed.

Diagnostic.py is rerunnable exact finite evidence, not an all-n proof or
full quantum simulation. It checks incomplete discovered lists for every
H subset of exact small fibers, cyclic Kraus completeness and original-index
cleanup, suffix uniformity, determinant minors, planted factorial moments,
search-tail rational inequalities, survival guards, profile thresholds,
all-D rational budgets and cap margins. The analytic arguments above carry
the infinite-domain and charged-work obligations.

The local GPU report and results from earlier work verified 15,018,684
multisets. They supplied finite evidence only, including the exact occupancy,
singleton and odd-parity mask updates and singleton/support conditional
identity. None is a premise for the all-b moment theorem, and no additional
GPU sweep or GPU instruction is part of CYG1. Source hashes preserve this
provenance without treating the census as an asymptotic proof.

The parent proposal required two clarifications, not a counterexample.
First, bounded discovery adds failure beyond singleton fibers; the h/m
identity is conditional on a verified H and the true size-biased fiber.
Second, CYC1's fixed-label termination argument does not carry over directly
to bounded discovery. Section 5.4 uses PSG1's joint induction, proving fresh
uniform blocks and almost-sure termination together. No proof conditions
on future cutoff survival, all high labels, or correct EXTRACT records.
All-D caps explicitly cover the sigma jump and a small partial width at
large nominal v. The threshold is 4428, and the source exponent reduction
is 5/6, proved from the SAME integer profile rather than a reoptimized one.

The structural result does not claim a constant-factor improvement of every
complete circuit or every capped source realization. Cyclic rank processing
can add gates; its source-renewal benefit is amortized in the stated bounds.
High-label sorting is invalid for the suffix proof. Unknown-state amplitude
amplification cannot replace these known-constant independent query oracles.
