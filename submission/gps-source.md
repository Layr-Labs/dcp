# GPS-BLOCK: signed-leaf multibit decoding with polynomial workspace

## 0. Joint theorem, configuration and provenance

For every N>=2, every s in Z/NZ, n=ceil(log2 N), the single algorithm
specified below recovers the full secret with unconditional probability
at least 1-2^-8>3/4 from independent ideal source copies. On EVERY
branch, including retries, discarded sources, failed attempts and aborts,
its simultaneous resource envelopes, for n>=2, are

    T=O(n^(5/2)(log2 n)^(3/2) 2^((176777/250000)sqrt(n log2 n))),
    S_C=O(n^2), S_Q=O(n),
    Q=O(2^((176777/250000)sqrt(n log2 n))).

All constants are absolute. The explicit n<256 exhaustive branch covers
n=1 as well. The four growth indices are [1/2,0,0,1/2]. Fractional
tolerance is zero; no optimality or positive robustness is asserted.
The actual configuration includes acquisition, weighted-attempt,
high-confidence-extraction and root-frequency hard cutoffs.

Direct source: GPS-HALF, submission b1a7feb1-6ac2-41c4-9e58-2717e5d9f49f,
frozen proof SHA-256 5bc5d5294d8510314a6e087be9885dd9090757e81b43c42a0412de8e1cb6729f.
Its above-half combiner, odd profile, refined product estimate, Grover
instrument, verified extraction, all-modulus architecture and every-branch
ledger are directly adapted here. Its predecessors GPS-VLE
(7bad5bd0-ecb9-4e06-b280-6de30ae3987a), GPS-C3
(03adf191-dda7-47c6-8af8-0a5ead124828), CS1
(f1481815-9577-4990-abe3-7b79fa5d9284) and GPS3
(05a58278-80b6-40ff-9e8b-dcec501b4b10) retain their credited contributions.
Upstream credits to GPS2, GPS, PSR2, PSW2, PSG1, Regev, Kuperberg,
Kitaev and BBHT remain acknowledged. No prior review is a premise;
all required arguments are reproduced here.

New here is the SIGNED leaf law with multiple untouched high bits.
Private sign symmetrization centers each normalized leaf conditional
on its low routing bits. A conditional tail bound gives an n*q0
frequency guard without paying for its deterministic worst-case range.
The untouched high interval gives a Dirichlet-kernel characteristic
bound, letting one decoder stage recover Theta(R) bits when the odd
modulus is large. The guard is omitted in the ideal proof and union
bounded separately, never used to postselect the characteristic law.
Root demand drops from O(nR) to O(n), so weighted work drops by R,
while preserving the coefficient and both polynomial space bounds.
These are asymptotic proofs with an enormous explicit threshold,
not measured practical quantum timings or a cube-root-time result.

## 1. Charged implementation conventions

All arithmetic is on explicit bit strings. A w-bit add, subtract, compare,
copy or increment has O(w) Boolean gates using ripple carry, with O(w)
scratch. Reversibly compute a Boolean circuit, copy out its answer, then
reverse it; a permutation can be computed into a fresh register, swapped,
and erased by its inverse. NOT, CNOT and Toffoli suffice, and Toffoli has
an exact constant-size Clifford+T decomposition. Wire counters, gate
generation, initialization, resets, measurements and classical reads and
writes are counted. Every indexed action also pays O(log(S_C + S_Q + 2))
bit operations; Section 9 shows this is O(log n). Gates are generated in
streaming order from O(n^2) bits of stored data; no circuit description of
exponential length and no table of exponential size is stored.

Only H, S, S-dagger, X, Z, CNOT and Toffoli are used (Z = S^2). There is no
arbitrary-N QFT circuit and no approximate rotation to synthesize. Fourier
LABELS are inferred by nondestructive translation tests (Section 3). The
source is used only for fresh mixed copies; no purification, preparation
inverse or control, QRAM, hidden-shift or subset-sum oracle is available or
used. In particular the Grover oracle of Section 4 is an explicitly
generated, fully charged reversible circuit built from classically stored
labels. Fair coins are obtained by preparing |0>, applying H and measuring;
a uniform integer in [0, 2^u) is u such coins.

Write N = 2^a2 M with M odd, d = floor(log2 N), omega = exp(2 pi i/N),
s1 = s mod M and s = s1 + M s2 (mod N) with 0 <= s2 < 2^a2.

## 2. Source identities and exact transforms

Let chi_k = N^(-1/2) sum_u omega^(k u)|u> and phi_k(s) = (|0> + omega^(-k s)|1>)/sqrt 2.
Substituting |u> = N^(-1/2) sum_k omega^(-k u) chi_k into
rho_s = (1/N) sum_x |psi_x><psi_x|, psi_x = (|0,x> + |1,x+s>)/sqrt 2, gives

    rho_s = (1/N) sum_(k=0)^(N-1) |phi_k(s)><phi_k(s)| (x) |chi_k><chi_k|,     (2.1)

because the cross terms k != k' carry (1/N) sum_x omega^(-(k-k')x) = 0.

Latent-label model. By (2.1) each copy is literally a convex mixture, with
uniform weights, of the product states phi_k(s) (x) chi_k. The whole
algorithm is a linear (adaptive) quantum instrument applied to independent
copies. Hence the joint law of all its classical outcomes equals the law
obtained by first drawing, for every copy, an independent uniform latent
label k in Z/NZ, and then running on the product state phi_k(s) (x) chi_k.
All probabilities below use this model. Applying X to the control maps
phi_k(s) to, up to a global phase, the POSITIVE qubit
pq_k(s) = (|0> + omega^(k s)|1>)/sqrt 2.

Two exact data transforms act on a fresh copy before label extraction. Each
is a permutation of all 2^n data encodings, extended by the identity on
encodings >= N. Each maps the copy exactly to rho_s' for a known transformed
secret s'. The latent-label model is then applied to rho_s' via (2.1), so the
latent label of a copy is the Fourier label of its TRANSFORMED data register,
which EXTRACT recovers.

(T1) Mult_alpha: u -> alpha u mod N, for a known alpha coprime to N. Since
x -> alpha x is a bijection of Z/NZ, the copy becomes exactly rho_(alpha s).
It is implemented with n controlled modular additions of the constants
alpha 2^v mod N into a clean register, a swap, and the inverse computation
with alpha^(-1): O(n^2) core steps and O(n) scratch.

(T2) Shift_c: if the control is |1>, replace u by u - c mod N, for a known c.
Since |1,x+s> becomes |1,x+(s-c)>, the copy becomes exactly rho_(s-c). This
takes O(n) core steps.

Modular addition of a known constant in [0,N) is a ripple comparison with N,
an addition, a comparison and a selector. It is the identity on encodings
>= N, uses O(n) Boolean gates, and is computed cleanly: compute, swap or XOR
the result out, then uncompute.

## 3. Finite-precision classical table and source-label extraction

For v in [0,4096) the controller computes rationals Cos[v], Sin[v] within
2^-20 of cos(2 pi v/4096) and sin(2 pi v/4096):

- Bound pi within 2^-90 using Machin's formula pi = 16 atan(1/5) - 4 atan(1/239),
  summing the first 40 terms of each alternating arctangent series. This
  gives two-sided bounds; the tails are below 16 (1/5)^81/81 + 4 (1/239)^81/81 < 2^-91.
  The identity follows from tan(2 atan(1/5)) = 5/12, tan(4 atan(1/5)) = 120/119
  and tangent subtraction.
- At the angle 2 v p_mid/4096 < 7, where p_mid is the midpoint of the pi
  bounds, sum 80 Taylor terms. The remainder is <= 7^81/81! < 2^-170. The
  angle error is < 2^-89, and sin and cos are 1-Lipschitz.
- Round each value to denominator 2^20.

This is a fixed finite rational computation, charged once as an absolute
constant (not advice). For x in [0,1) put tab_0(x) = Cos[floor(4096x)] and
tab_1(x) = Sin[floor(4096x)], and let cs_0(x) = cos(2 pi x),
cs_1(x) = sin(2 pi x). Since cs is 2pi-Lipschitz,

    |tab_beta(x) - cs_beta(x)| <= 2 pi/4096 + 2^-20 < 1/625.                  (3.1)

Input: a data register holding chi_k for a latent k, beside arbitrary
spectators. An upper bound Qcap on the number of EXTRACT calls is fixed in advance
(Section 8). EXTRACT makes a cheap estimate (3.2), checks it with a randomized
verification (3.3), and only if the check rejects runs the high-confidence
extraction (3.4). A global counter caps the number of high-confidence runs (3.5).
Parameters:

    J_e = n + 4,   h_e = ceil(log2(Qcap (n+5))) + 18,   h_A = 2 ceil(log2(n+5)) + 14,
    t_V = 64 h_e,  F(h) = 2^21 h,  T_V = ceil(log2(n+20)) + 14,  P_V = n + 40 + T_V.

Translation Tr_c: u -> u + c mod N satisfies Tr_c chi_k = omega^(-k c) chi_k.
A TEST WITH SHIFT c (0 <= c < N) works as follows. Prepare an ancilla in |+>.
Apply Tr_((N - c) mod N) controlled by it, so the |1> branch gets eigenvalue
omega^(k c). Measure the ancilla in X (H then Z) or in Y (S^dagger, H, then Z).
The +-1 outcome has mean cos(2 pi c k/N) or sin(2 pi c k/N). Conditioned on
k, chi_k and every spectator are unchanged and outcomes are independent. A test
at LEVEL j is the test with shift 2^j mod N. Each RUN forms that constant once per level by modular doubling from the preceding constant, O(n) core steps per level, then reuses it for all tests. Each test costs one controlled modular addition, O(n) core steps.

### 3.1 RUN(F): level-wise extraction

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

### 3.2 Estimate

k_A = RUN(F(h_A)). Since e^(-h_A) <= 2^(-h_A) <= 2^-14 (n+5)^-2,

    Pr[k_A != k] <= 4 (n+5) 2^-14 (n+5)^-2 <= 2^-12/(n+5) <= 1/(2n).        (3.E)

Cost O(n^2 log n).

### 3.3 Verification

Precomputation. By long division compute rh = floor(k_A 2^P_V / N), O(n P_V) = O(n^2)
bit operations, so rh 2^-P_V is within 2^-P_V of k_A/N. For i = 0..n+19 let f_i be
the T_V bits of rh in positions P_V-i-1 down to P_V-i-T_V (all exist, since
P_V-i-T_V >= 21). Then f_i 2^-(T_V) is within 2^-(T_V) + 2^(i-P_V) of frac(2^i k_A/N)
in circular distance on R/Z.

Round r = 1..t_V:
- Draw c uniformly from [0, 2^(n+20)) using n+20 fresh fair bits, each obtained by
  measuring H|0> (O(1) core steps, as in Section 9), and
  compute cN = c mod N (at most 21 quotient bits: O(n) bit operations).
- Run one X test and one Y test with shift cN, with outcomes zX, zY in {+1,-1}.
  Their means are cos(2 pi c k/N) and sin(2 pi c k/N).
- Predicted phase: xh = (sum over the 1-bits i of c of f_i) mod 2^(T_V), read as
  the fraction xh 2^-(T_V) in [0,1). Since frac(c k_A/N) = sum_i c_i frac(2^i k_A/N)
  mod 1, its circular distance to frac(c k_A/N) is at most
  (n+20) 2^-(T_V) + sum_(i <= n+19) 2^(i-P_V) <= 2^-14 + 2^-20 < 2^-13. This costs
  O(n T_V) = O(n log n) bit operations.
- Score s_r = zX tab_0(xh 2^-(T_V)) + zY tab_1(xh 2^-(T_V)), with tab from Section 3.

ACCEPT iff s_1 + ... + s_(t_V) >= t_V/2.

Lemma 3.V. Conditioned on k and k_A: if k_A = k, verification rejects with
probability at most e^(-h_e); if k_A != k, it accepts with probability at most
e^(-h_e).

Proof. Rounds are i.i.d. given (k, k_A): each uses fresh coins and fresh tests,
and the data register is unchanged. By (3.1) and 2 pi 2^-13 < 1/1300, each table
value is within 1/625 + 1/1300 < 1/400 of the cosine or sine of 2 pi c k_A/N.
So, given c, E[s_r | c] = cos(2 pi c (k - k_A)/N) + err with |err| <= 2/400 = 1/200.
- If k_A = k, E s_r >= 1 - 1/200.
- If k_A != k, put dl = (k - k_A) mod N, which is nonzero. Write 2^(n+20) = qq N + rr
  with 0 <= rr < N. Over each full period of N consecutive values of c the sum
  of exp(2 pi i c dl/N) is 0, so |E_c exp(2 pi i c dl/N)| <= rr/2^(n+20) < 2^-20.
  Hence E s_r <= 1/200 + 2^-20.
Each |s_r| <= 2 (1 + 2^-20) < 2.01. By Hoeffding, a sum of t_V i.i.d. terms in
an interval of length 4.02 deviates from its mean by at least
Dev = (1/2 - 1/200 - 2^-20) t_V >= 0.494 t_V with probability at most
exp(-2 Dev^2/(4.02^2 t_V)) <= exp(-0.03 t_V) = exp(-1.92 h_e) <= e^(-h_e). QED.

Cost per call: O(n^2) precomputation plus t_V=O(h_e) rounds of O(n log n), hence O(n^2+n h_e log n) core steps. Section 9 proves h_e=O(R)=O(sqrt(n log n)); since R<=n, this is O(n^2 log n). Classical scratch is O(n log n) bits.

### 3.4 High-confidence extraction and output

If verification accepts, EXTRACT outputs k_A. Otherwise it runs k_H = RUN(F(h_e)),
the high-confidence extraction, and outputs k_H, subject to the cap in 3.5.
After the last test of the call, the data register is reset. EXTRACT uses no
Fourier transform, no lookup, and no rotation other than H and S, and O(n)
quantum scratch (n data qubits, one ancilla, arithmetic).

### 3.5 Cap on high-confidence runs

Let sn be the least integer >= sqrt n (computed exactly by integer arithmetic) and Cf = ceil(Qcap/sn). A counter
records the number of RUN(F(h_e)) executions. If a call would start the
(Cf+1)-st one, GPS-BLOCK stops, releases everything and outputs 0 (ABORT).

Lemma 3.F. Pr[ABORT] <= 2^-20.

Proof. A call reaches 3.4's high-confidence branch only if k_A != k, or k_A = k
and verification rejects. Conditioned on the entire history before the call
(including k), by (3.E) and Lemma 3.V this has probability at most
1/(2n) + e^(-h_e) <= 1/n, because the call's tests and coins are fresh. Hence
the indicators of the at most Qcap calls can be coupled with i.i.d. Bernoulli(1/n)
variables that dominate them (compare each indicator with an independent uniform
threshold), and the number of high-confidence runs is stochastically dominated by
X ~ Bin(Qcap, 1/n), with mean EX = Qcap/n. For x > EX the Chernoff bound gives
Pr[X >= x] <= (exp(1) EX/x)^x. With x = Cf >= Qcap/sn >= Qcap/(sqrt n + 1),
exp(1) EX/x <= exp(1) (sqrt n + 1)/n <= exp(1) * 9/64 < 1/2 for n >= 64, since
(sqrt n + 1)/n decreases. Also Cf>=20 because Qcap=1024(2G H0+2n)>=2048n, so Cf>=2048n/(sqrt n+1)>20 on this main branch.
So Pr[ABORT] <= 2^-20. QED.

### 3.6 Correctness and cost of EXTRACT

Per call, the output differs from k only if (k_A != k and verification accepts)
or (a high-confidence run returns a value other than k). By Lemma 3.V and the
concentration bound of 3.1 this has probability at most e^(-h_e) + 4(n+5) e^(-h_e) = (4n+21) e^(-h_e),
uniformly in k and in the adaptive schedule. Over at most Qcap calls,
(4n+21)Qcap e^(-h_e)<=5*2^(h_e-18)e^(-h_e)<=5*2^-18<2^-14.

Cost on every branch. The cheap RUN costs O(n^2 log n). The verifier
costs O(n^2+n h_e log n)=O(n^2 log n). There are at most Qcap calls.
Each high-confidence RUN costs O(n^2 h_e), and the global cap gives
Cf<=Qcap/sn+1<=2Qcap/sqrt n, since Qcap>=sqrt n. Thus all high-confidence
runs together cost O(n^(3/2)h_e Qcap). Section 9 proves
h_e=O(sqrt(n log n)), so this is O(n^2 sqrt(log n) Qcap), contained in
O(n^2 log n Qcap). All EXTRACT calls together therefore cost
O(n^2 log n Qcap) core steps on EVERY actual branch. The O(n) source
charge, transforms and resets per copy fit within the same bound.

IDEAL run. Replace each EXTRACT output by the latent label and omit the
fallback cap. Every internal estimate, test outcome, verification coin,
verification verdict, fallback decision and fallback counter is ignored by
the ideal outer controller. No outer decision uses them, except the
fallback abort which is omitted in this ideal process. The actual and
ideal outer processes can be coupled until a wrong output label or a
fallback abort occurs. Their probability discrepancy is at most
2^-14+2^-20, without conditioning on successful extraction or future cap
survival. The two outer acquisition/weighted caps are analyzed separately
in Section 8. All actual-branch resource bounds use all four caps.

## 4. Width profile, Grover pair search and the depth-first tree

### 4.1 Width profile

Main-branch parameters are computed once for n>=256 by integer arithmetic.
For integer R>=2 put

    Delta(R)=2ceil(log2(4R)),
    m(R)=floor((2R-2)/Delta(R))+1,
    S(R)=sum_(k=0)^(m(R)-1)(2R-1-k Delta(R)).

Let R be the FIRST integer >=2 with S(R)>=n-1, found by sequential scan,
not a monotonicity assumption. Since S(R)>=2R-1, scanning through n
suffices. Fix Delta=Delta(R), m=m(R), and define

    v_i=2R-1-(m-i)Delta, 1<=i<=m,
    q0=product_i(v_i+1), G=product_i 2(v_i+1)=2^m q0.

All v_i are positive ODD integers, with v_m=2R-1 and sum v_i=S(R)>=n-1.
Every parameter is computed by explicit integer operations: for example
ceil(log2(4R)) is the bit length of 4R-1. Section 9 proves
R=O(sqrt(n log n)), G<=8R2^R, and the stronger product estimate used
by the resource ledger.

### 4.2 A fixed-schedule Grover search

Let r >= 2, Nr = 2^r, and let f: {0,1}^r -> {0,1} be given by a classical
description from which a reversible circuit computing f(y) into a fresh
ancilla, with all scratch returned to zero, is generated with O(n^2) gates
(Section 4.3 gives the two instances used). Let tt = #{y : f(y) = 1} be
unknown. Put Mr = ceil(r/2).

SEARCH(f). For u = 0, 1, ..., Mr, and for each u twenty times: draw j
uniformly from [0, 2^u) with u fair coins; prepare r fresh qubits as
H^(x r)|0^r>; apply j Grover iterations Gr = Df Of; measure the r qubits,
obtaining y; compute f(y) classically; reset the r measured search qubits
and all search scratch to |0> and release them; if f(y) = 1 return y,
otherwise continue with the next trial. If every trial fails return the
symbol FAIL. No search qubit survives a trial, so at most one trial's
registers are allocated at any time.

Here Of flips the sign of |y> iff f(y) = 1: compute f(y) into an ancilla,
apply Z, uncompute. Df = H^(x r) (I - 2|0^r><0^r|) H^(x r), implemented as
H^(x r), X^(x r), a Z controlled on all other r - 1 qubits (CZ when r=2; otherwise a Toffoli ladder with r-2 scratch qubits, computed and uncomputed exactly), X^(x r),
H^(x r). Up to a global sign Df = 2|psi><psi| - I with psi = H^(x r)|0^r>.

Lemma 4.1 (deterministic cost). SEARCH(f) performs at most
20 sum_(u=0)^(Mr) 2^u < 40 2^(ceil(r/2)) Grover iterations and at most
20 (Mr + 1) trials on every branch, uses r + O(r) + O(n) qubits, and every
returned y satisfies f(y) = 1. Each iteration costs O(n^2) core operations.
Proof. The schedule is fixed; j < 2^u. The return is classically verified.
The oracle and diffusion circuits have O(n^2) gates by hypothesis and the
Toffoli ladder has O(r) gates. QED.

Lemma 4.2 (success). If tt >= 1 then Pr[SEARCH(f) = FAIL] <= (3/4)^20 < 1/300.
Proof. Let sin^2 theta = tt/Nr with 0 < theta <= pi/2. Write |al> and |be>
for the normalized uniform superpositions over unmarked and marked strings.
Then psi = cos(theta)|al> + sin(theta)|be>, and both Of and Df preserve the
real plane spanned by |al>, |be>: Of is the reflection across |al>, and
2|psi><psi| - I is the reflection across psi, so their product rotates that
plane by 2 theta. Hence after j iterations the state is
cos((2j+1)theta)|al> + sin((2j+1)theta)|be>, and measuring returns a marked
string with probability exactly sin^2((2j+1) theta). The global sign of Df
is irrelevant.

Case tt >= Nr/2. At u = 0 we always have j = 0, so each of the twenty u = 0
trials succeeds with probability tt/Nr >= 1/2.

Case 1 <= tt < Nr/2. Take u = Mr and mm = 2^Mr >= sqrt(Nr). For j uniform in
[0, mm) the success probability is

    P = (1/mm) sum_(j=0)^(mm-1) sin^2((2j+1)theta)
      = 1/2 - (1/(2 mm)) sum_(j=0)^(mm-1) cos((2j+1) 2theta)
      = 1/2 - sin(4 mm theta)/(4 mm sin(2 theta)),

using 2 sin(ph) cos((2j+1)ph) = sin((2j+2)ph) - sin(2j ph), which telescopes
to sum_(j<mm) cos((2j+1)ph) = sin(2 mm ph)/(2 sin ph) for sin ph != 0, with
ph = 2 theta. Here sin(2 theta) = 2 sqrt(tt/Nr) sqrt(1 - tt/Nr)
>= 2 (1/sqrt Nr)(1/sqrt 2) = sqrt(2/Nr) > 0, so
mm sin(2 theta) >= sqrt 2 and P >= 1/2 - 1/(4 sqrt 2) > 1/4.

In both cases some u has twenty independent trials each succeeding with
probability at least 1/4 (the coins and fresh registers of different trials
are independent), so the failure probability is at most (3/4)^20. QED.

### 4.3 The combiner

A PS_TREE(D,B) call, 1 <= D <= n and 0 <= B < D, receives independent
leaf phase qubits with known integer labels. In UNSIGNED mode these are
uniform k in [0,2^D). In SIGNED mode they are a=sigma*k for independent
uniform k in [0,2^D) and private fair signs sigma. Sections 6 and 7 choose
the mode and B. If B=0 return one leaf. Otherwise allocate
widths top-down: for i = m, m-1, ..., 1 put b_i = min(v_i, B - sum_(j>i) b_j).
Since sum_i v_i >= n - 1 >= B this ends with sum_i b_i = B. Put
p_i = sum_(j<i) b_j and r_i = b_i + 1. Level 0 returns a leaf. A level with
b_i = 0 returns its level-(i-1) child unchanged. A level with b_i >= 1 is a
NODE: it obtains r_i independent level-(i-1) outputs one at a time, retaining
earlier siblings, and then runs one ATTEMPT of the combiner below. Before the
attempt, AFTER its r_i inputs have been built, it adds the weight
w_i = 2^(ceil(r_i/2)) to the global weighted-attempt counter, or aborts
(Section 8) if that would exceed Wcap. Every attempt, successful or not, is
charged. Note ceil(r_i/2) <= (v_i + 1)/2 because r_i <= v_i + 1 and v_i + 1 is
even.

The r_i input labels a_1, ..., a_(r_i) are integers divisible by 2^(p_i)
(induction below). Their joint state is

    2^(-r_i/2) sum_(x in {0,1}^(r_i)) exp(2 pi i th A(x)) |x>,   A(x) = sum_j x_j a_j,

where th is the current source secret divided by its effective denominator
(Sections 6, 7), and the r_i qubits form the register x. Write
rho_j = (a_j / 2^(p_i)) mod 2^(b_i) in [0, 2^(b_i)) and
res(y) = sum_j y_j rho_j mod 2^(b_i) for y in {0,1}^(r_i).

ATTEMPT.
1. Reversibly compute res(x) into a clean b_i-bit register by r_i controlled
   additions of the classical constants rho_j, measure it, obtaining e, and
   clear it by XOR with e (on the surviving support it holds the constant e).
   The remaining state is the equal-magnitude superposition, with the same
   phases, over the FIBER X_e = {y : res(y) = e}; since x itself lies in X_e,
   |X_e| >= 1.
2. x0 := SEARCH(f_e) with f_e(y) = [res(y) = e]. If FAIL, go to FAIL.
   The oracle computes res(y) by r_i controlled additions of b_i-bit
   constants into a b_i-bit accumulator, compares with e, and uncomputes:
   O(r_i b_i+b_i)=O(R^2) gates and O(R) quantum scratch.
3. x1 := SEARCH(f_(e,x0)) with f_(e,x0)(y) = [res(y) = e and y != x0]; the
   oracle adds one comparison with the constant x0. If FAIL, go to FAIL.
4. Compute the indicator [x = x0 or x = x1] into a fresh ancilla (two
   comparisons with constants, O(r_i) gates), measure it, and uncompute the
   scratch. On outcome 0 go to FAIL. On outcome 1 the state is proportional
   to exp(2 pi i th A(x0))|x0> + exp(2 pi i th A(x1))|x1>.
5. Compression. XOR the constant x0 into the register, so the two basis
   states become 0 and del = x0 xor x1 != 0. Choose a position at which del
   has a 1 (the pivot) and apply CNOTs from the pivot to every other position
   where del has a 1. This invertible affine map sends 0 to 0 and del to the
   unit vector at the pivot. All non-pivot qubits are now |0> and are
   released. The pivot qubit is, up to a global phase,
   (|0> + exp(2 pi i th [A(x1) - A(x0)])|1>)/sqrt 2, and the node returns it
   with the integer label A(x1) - A(x0).
FAIL: measure and reset every register of this node and of its inputs,
discard them, build r_i fresh level-(i-1) outputs (fresh copies throughout
those child calls), and run a new ATTEMPT (charged again).

The output label A(x1) - A(x0) is divisible by 2^(p_i + b_i) = 2^(p_(i+1)),
because res(x1) = res(x0) = e and all a_j are divisible by 2^(p_i). Signed
integer additions and shifts of the known labels have the stated bit costs.

Lemma 4.3 (correctness of an attempt). Whatever the outcomes of the
searches, a returned qubit has exactly the stated phase and label: x0 and x1
are classically verified members of X_e, distinct by construction, and
steps 4-5 act on the fiber state by a projective measurement followed by an
exact permutation of basis states. A search FAIL or a test outcome 0 only
causes a retry, never a wrong label. QED.

Lemma 4.4 (every-branch cost of an attempt). Its quantum instrument,
searches and residue-only classical verification cost O(R^2 w_i) core
steps, where w_i=2^ceil(r_i/2). Its full signed-label preparation,
output arithmetic and counter/loop work cost O(n r_i) additional core
steps. Quantum scratch is O(R) beyond the retained input qubits, and
classical scratch is O(n) beyond the stored input labels.

Proof. The actual predicates use r_i,b_i<=2R, so each residue oracle,
comparison and diffusion costs O(R^2). There are at most 80w_i Grover
iterations. The O(r_i) trials are O(w_i); initialization, fresh coins,
measurement, reset and classical predicate verification per trial also
fit O(R^2). The residue measurement and pair compression cost O(R^2).
Extracting residue fields and computing A(x1)-A(x0) use r_i full signed
O(n)-bit labels, so O(n r_i) further core steps suffice. Counter checks
fit that term. All generated circuits are streamed. QED.

Leaf structure. A returned tree contains prod_i r_i <= q0 distinct leaves,
although its construction may consume many more through failures. Every
returned label is a signed sum of the labels of its distinct surviving
leaves, with each coefficient in {-1, 0, 1} and at least one coefficient
nonzero: a leaf has coefficient 1; a node returns A(x1) - A(x0) where x0 != x1
differ in some input, and the leaf sets of different inputs are disjoint, so
some leaf of that input keeps a nonzero coefficient. Consequently every
label handled in a PS_TREE(D,B) call has absolute value below q0 2^D and
O(n + log2 q0) = O(n) bits, including on branches with incorrect extracted
labels. All decisions of a level-i attempt (the measured residue, both
searches, the test outcome, the pivot) depend only on the residues rho_j,
that is on the input labels modulo 2^(p_i + b_i), and on fresh coins and
fresh search registers. The tree is evaluated depth first and keeps no full
recursion tree.

## 5. Untouched bits, conditional fiber statistics and success probability

Fix a PS_TREE(D,B) call in the ideal run of Section 3. At a position
p<=B write a=u+2^p tau, u=a mod 2^p in [0,2^p), and put Lp=2^(D-p).
For UNSIGNED leaves, u is uniform and tau is independent uniform on [0,Lp).
For SIGNED leaves u is also uniform. Conditional on u!=0, tau is uniform
on [-Lp,Lp); conditional on u=0, tau is the independent fair-sign version
of a uniform integer in [0,Lp). In particular its zero has double the mass
of any other supported signed value. These assertions follow by enumerating
the two preimages (sigma,k), each of probability 1/(2*2^D).

In the ideal run EXTRACT returns the true latent label. All its internal
translation-test outcomes, verification verdicts, fallback coins, counters
and loop indices are private discarded records; its fallback cap is omitted.
In SIGNED mode the original unsigned k and private sign sigma are likewise
overwritten after forming a, and no routing reads them separately. The
sigma-fields below EXCLUDE these private records and exclude the current
leaf high parts. The ideal process also omits the frequency guard of
Section 6. No argument conditions on numerical extraction correctness,
fallback-cap survival or frequency-guard survival.

Lemma 5.1 (untouched high parts). Just before a level-i ATTEMPT, let Fs
contain the low parts modulo 2^p_i of its surviving leaves, all their
combiner routing outcomes, all nonprivate routing/search coins, and all
information about copies outside this subtree, including previous decoder
outcomes. It contains neither the leaf high parts nor the excluded records
above. Conditional on Fs, the surviving leaf high parts are independent
with exactly the laws stated above for their fixed low parts.

Proof. A routing decision at a lower level inspects only residues of the
input labels modulo 2^(p_i), together with fresh search coins and registers.
The measured residue law |X_e|/2^r and projection law 2/|X_e| depend only
on these residues, independently of the phases and of high parts. Search
outputs depend only on the same residues and private search randomness.
Inducting over the depth-first construction, including failed attempts,
therefore selects surviving leaves using low parts alone. Sign generation
is not itself a recorded routing coin. The accepted unsigned k is uniform
before independent symmetrization. Independent product high-part laws
conditional on their low parts are preserved by every such selection.
Disjoint fresh copies outside the subtree reveal no high part inside it.
There is no hidden condition on a cap passing. QED.

Lemma 5.2 (conditional residues). Given Fs, the r_i input residues
rho_j=(a_j/2^p_i) mod 2^b_i are independent uniform on [0,2^b_i).
Proof. Each input is a signed sum of disjoint surviving leaf labels with
coefficients in {-1,0,1}, at least one nonzero. Its quotient is a known
integer plus the corresponding signed sum of high parts. Because
p_i+b_i<=B<D, each of the high-part laws above is uniform modulo 2^b_i:
the unsigned interval and the symmetric interval have lengths divisible
by 2^b_i; a signed uniform interval is uniform modulo it as well. One
coefficient of magnitude one makes the entire sum uniform. Disjoint
leaf sets give independence across inputs. QED.

Lemma 5.3 (conditional success). In the ideal run, conditional on Fs,
every level-i ATTEMPT returns a qubit with probability strictly above 1/2.

Proof. Write b=b_i>=1, r=b+1, M_b=2^b and alpha=1-(3/4)^20>299/300.
Exactly as for the pair instrument, for fixed residues

    Pr[return|Fs,residues]>=alpha^2 2^(1-r) #{e:Y_e>=2}.       (5.1a)

Condition on the first b input residues. Their M_b subset sums, including
the empty subset, have counts C_e with mean ONE across the M_b residues.
Define z=#{e:C_e=0}/M_b, o=#{e:C_e=1}/M_b and
w=(1/M_b)sum_e(C_e-1)^2. These count vectors are analytic variables only; the algorithm never builds their exponential table. The last residue a is independent uniform,
and Y_e=C_e+C_(e-a), so exact cyclic-shift averaging gives

    E_a[#{e:Y_e<=1}/M_b |C]=z^2+2zo.                        (5.1b)

We prove the deterministic inequality z^2+2zo<=w/4+2/9 for any such
count vector. If o=1, all counts are one and the assertion is immediate.
Otherwise put u=1-o>0. The remaining nonzero/nonunit counts are at least
two, so mean one implies 2z+o>=1. Also z+o<1: otherwise mean one
would force o=1. Consequently t=z/u satisfies 1/2<=t<1.
Cauchy-Schwarz on the remaining buckets gives

    w>=o+(1-o)^2/(1-z-o)-1
      =z(1-o)/(1-z-o)=tu/(1-t).

Writing F=z^2+2zo=2tu-t(2-t)u^2, we obtain

    F-w/4 <= t[A u-(2-t)u^2], A=2-1/[4(1-t)].

If t>=7/8, then A<=0 and the right side is nonpositive. Otherwise
1/2<=t<=7/8 and completing the square bounds it by

    t A^2/[4(2-t)] <=2/9.

The last inequality is equivalent to
P(t)=256-1081t+1520t^2-704t^3>=0 on [1/2,7/8]. Here are explicit
positive decompositions covering that whole interval. For 0<=x<=1,

    P((4+x)/8)=(15/2)(1-x)^3+(91/8)x(1-x)^2
                  +(15/2)x^2(1-x)+(9/4)x^3,
    P((5+2x)/8)=(9/4)(1-x)^3+(21/4)x(1-x)^2
                  +(65/4)x^2(1-x)+(9/4)x^3.

Thus the deterministic bound is proved without an optimization oracle.
Now average over the first b residues, conditional on Fs. Distinct subset
strings have equal sums with probability exactly 1/M_b because their
difference contains a coefficient +1 or -1. Counting ordered pairs yields

    E[(1/M_b)sum_e C_e^2 |Fs]=1+M_b(M_b-1)/M_b^2=2-1/M_b,
    E[w|Fs]=1-1/M_b<=1.

By (5.1b), the expected fraction of fibers with at least two members is
at least 1-1/4-2/9=19/36. Since 2^(1-r)M_b=1 here, (5.1a) gives

    Pr[return|Fs]>=alpha^2 (19/36)
       >(299/300)^2 (19/36)>1/2.                            (5.1)

Uniform independent residues follow from Lemma 5.2. No Poisson law,
independent-bucket hypothesis or favorable-outcome conditioning is used.
The pair instrument still classically verifies its two members. QED.

Lemma 5.4 (root frequency and signed concentration). Write H=D-B,
Lh=2^H, and each surviving leaf as a_l=u_l+2^B tau_l. Let Gt contain
all routing information, leaf low parts modulo 2^B, previous decoder
outcomes and outside-copy information, with the private exclusions of
Lemma 5.1. A returned root has label 2^B W where

    W=c+sum_l c_l tau_l, c_l in {-1,0,1}, some c_l nonzero.

Conditional on Gt the high parts are independent. For
D_L(y)=L^(-1)sum_(t=0)^(L-1) exp(2 pi i y t), each active high-part
factor has modulus at most |D_Lh(y)|. Indeed the three possible laws
have characteristic functions D_Lh, a phase times D_(2Lh), or
Re D_Lh; and |D_(2Lh)|=|D_Lh cos(pi Lh y)|<=|D_Lh|. Therefore

    |E exp(2 pi i y W)| <= |D_Lh(y)|
       <= min(1, 1/(2 Lh ||y||)) for 0<||y||<=1/2.        (5.2)

The second inequality follows from the geometric sum and
|sin(pi y)|>=2||y||. For H=1 it also gives the exact useful bound
|D_2(y)|=|cos(pi y)|. Since Lh is even, W has fair parity.
These statements are conditional on Gt, not on W itself.

In SIGNED mode, if Lh^2<=q0, a further bound is

    Pr[|W|>n q0 |Gt] <= delta_n := 2 exp(-n^2/8).          (5.4)

To prove it, use W=sum_l c_l a_l/2^B. Given u_l!=0 the conditional
mean of a_l/2^B is u_l/2^B-1/2, of absolute value at most 1/2;
given u_l=0 the mean is zero. There are at most q0 active leaves,
so |E W|<=q0/2. Every summand has range of length at most 2Lh.
For an independent bounded variable of range length 2Lh the centered
log-mgf is at most t^2 Lh^2/2: its second derivative is a tilted
variance at most Lh^2, and integrating twice proves this bound.
Multiplying mgfs and optimizing the exponential Markov bound gives
two-sided tail at displacement x at most 2exp(-x^2/(2q0 Lh^2)).
Take x=nq0-q0/2>=nq0/2 and Lh^2<=q0. This proves (5.4) without
conditioning on any frequency-guard acceptance. QED.

## 6. Odd-part recovery by multibit free-frequency decoding

If M=1, set s1=0 and skip this section. Otherwise M>=3. Define

    Hcap=floor(floor(log2 q0)/2), ell=floor(log2 M),
    h=min(Hcap,ell-6), Fmax=n q0,
    K=8192(ceil(log2 Fmax)+ceil(log2 n)+30).

If h>=8 use LARGE mode: SIGNED leaves, D=d, B=d-h,
pdec=h-3, step=h-5. Otherwise use SMALL mode: UNSIGNED leaves,
D=d, B=d-1, pdec=3, step=1. In both cases pdec=step+2.
In LARGE mode B>=a2+6, because d=a2+ell and h<=ell-6;
in SMALL mode B>=a2 because M>=3. Thus CRT below is valid.
All these choices depend only on N,n and the explicit profile.

Stages have indices j=0,step,2step,...,J, stopping at the first
index with 2^(j+pdec)>2M. For stage j compute the unit alpha_j by
CRT and extended Euclid so that

    alpha_j=1 mod 2^a2,
    alpha_j=2^j (2^(B-a2))^(-1) mod M.

A fresh leaf is obtained by acquiring a copy, applying Mult_alpha_j,
extracting k, accepting iff k<2^d, and applying X for positive phase.
In LARGE mode draw a private fair sign sigma, apply another X when
sigma=-1, set a=sigma*k, and discard k,sigma as separate records.
In SMALL mode set a=k. Ideal accepted labels have exactly the laws
in Section 5; acceptance probability exceeds one half. The resulting
phase is exp(2 pi i a alpha_j s/N), and for every integer W,

    2^B W alpha_j s/N = 2^j W s1/M mod 1.                 (6.1)

For each of K records run PS_TREE(D,B), obtaining label 2^B W.
The ACTUAL algorithm checks |W|<=Fmax; if it fails, release all
registers and abort the entire algorithm with output zero. This is
the fourth cutoff. Otherwise measure the root in an independently
fair X/Y basis beta and record the sign Z and frequency f=2^j W.
The analysis uses unguarded ideal roots and adds the guard error
by a union bound; it never analyzes roots conditional on passing.

Put theta=s1/M and P_j=j+ceil(log2 Fmax)+8. Candidates are the
dyadic grid c/2^P_j on the circle. At stage zero use the whole grid.
At each later stage retain candidates within circular distance
rad_j=2^(-j-2) of the previous center. The endpoints are grid
points: the previous center has a coarser dyadic denominator and
rad_j is a multiple of 2^-P_j. The candidate set consists of one
or two explicit integer intervals, with at most
2^(ceil(log2 Fmax)+8)<=512 Fmax elements at every stage.

For each candidate compute the exact-integer-table score

    score(c)=sum_i Z_i tab_beta_i(((f_i c) mod 2^P_j)/2^P_j).

Stream candidates in increasing order, maintaining K modular
residues, updating by addition and keeping the least maximizer
z_j. Never store the whole candidate set. Return at the final
stage floor(M z_J+1/2) mod M.

Lemma 6.1 (stage success). If theta belongs to the input arc (the
whole circle at stage zero), the unguarded ideal stage returns
z_j at circular distance less than 2^(-j-pdec) from theta with
probability at least 1-2^-20/n.

Proof. For a fixed candidate zeta, put Delta=theta-zeta circularly,
xi_i=Z_i cs_beta_i(f_i zeta). Given W_i, fair-basis averaging gives
E xi_i=(1/2)cos(2 pi 2^j W_i Delta). The score differs from sum xi_i
by at most K/625. All conditional means below include the past
of the stage; the new tree has fresh independent source copies.
The nearest candidate has |Delta0|<=2^(-P_j-1). In SMALL mode
|W|<2q0<=Fmax. In LARGE mode (5.4) gives the bound |W|<=Fmax
except with conditional probability delta_n, since 2^(2h)<=q0.
Consequently its conditional mean is at least

    (1/2)cos(pi/128)-delta_n.

Indeed on the bounded event |f Delta0|<=2^-9 and off it xi's
conditional mean is at least -1/2. This uses an unconditional
mean with a tail estimate, not a postselected distribution.

For a far candidate |Delta|>=2^(-j-pdec). At stage zero
|Delta|<=1/2; later both candidate and theta belong to the
input arc, so |Delta|<=2^(-j-1). Thus y=2^j Delta can be chosen
with |y|<=1/2. In SMALL mode |y|>=1/8 and (5.2) with H=1
bounds its conditional mean by (1/2)cos(pi/8). In LARGE mode
|y|>=2^(-h+3)=8/Lh and (5.2) gives modulus at most 1/16,
hence a still smaller conditional mean. Use the common upper
bound (1/2)cos(pi/8).

For each fixed candidate the centered xi sum is a martingale
with increments in intervals of length two. Azuma-Hoeffding
bounds deviation K/64 by exp(-K/8192). For n>=256,
delta_n<2^-40, and

 (1/2)(cos(pi/128)-cos(pi/8))-delta_n>0.0378
       >2/64+2/625.

So outside the deviation events the near point strictly beats
every far point. There are at most 2^(ceil(log2 Fmax)+9) events.
The chosen K and exp(-x)<=2^-x bound their total probability
by 2^-21/n<=2^-20/n. QED.

The previous output radius is exactly the next input radius,
because pdec=step+2. The stopping rule ensures final error
less than 1/(2M); circular nearest rounding then returns s1.
The following bound controls all possible moduli:

    Smax=n                         if Hcap<8,
    Smax=ceil(n/(Hcap-5))+16        if Hcap>=8.             (6.2)

If h=Hcap>=8, step=Hcap-5 and at most ceil(n/step)+2
stages occur. If 8<=h=ell-6<Hcap, then ell>=14 and step=ell-11;
the stopping inequality is j>ell+2-pdec=11, so at most
ceil(12/(ell-11))+1<=5 stages suffice (the loose bound seven
also suffices). If h<8 while Hcap>=8, ell<=13 and SMALL mode
uses at most ell+1<=14 stages. If Hcap<8 SMALL mode has at
most n stages. In all cases the number of stages is at most
2n, so total ideal decoder error is at most 2^-19. For a
uniform clean global budget we will use this slightly larger
bound rather than 2^-20.

Frequency guard. SMALL roots never fail it. In LARGE mode
each root fails it with conditional probability at most delta_n.
For n>=256, R<=n (capacity), log2 q0<=R+3+log2 R, so
ceil(log2 Fmax)+ceil(log2 n)+30<=4n and K<=2^15 n.
There are at most 2n K<=2^16 n^2 odd roots. Their union
bound is 2^16 n^2 *2exp(-n^2/8)<=2^-20 for n>=256:
exp(-n^2/8)<=2^(-n^2/8), and
17+2log2 n-n^2/8<=-20 at 256 and decreases thereafter.
This bound concerns unguarded ideal roots. Coupling to the
actual guard stops at its first failure; no survival condition
is introduced into Lemma 5.4 or the stage proof.

## 7. 2-adic recovery

If a2 = 0, put s2 = 0 and skip this section. Otherwise s - s1 = M s2 (mod N)
for a unique s2 in [0, 2^a2). The bits of s2 are found at levels
g = 0..a2-1. Let s2low be the known low g bits. Put sh_g = s1 + M s2low
(mod N), wd = a2 - g, and rem = (s2 - s2low)/2^g in Z/2^wd. Then
s - sh_g = M 2^g rem (mod N).

Leaf qubit for level g:
- acquire a copy and apply Shift_(sh_g), which makes the secret s - sh_g;
- run EXTRACT to obtain k, and apply X to the control.

Ideally the phase is exp(2 pi i k M 2^g rem/N) = exp(2 pi i kk rem/2^wd),
with kk = k mod 2^wd. Since 2^wd divides N and k is uniform on Z/NZ, kk is
uniform on [0, 2^wd). Use kk as the label.

- If wd = 1: if kk = 1, measure X; the outcome is + iff rem is even. If
  kk = 0, discard and repeat.
- If wd >= 2: run PS_TREE(wd,wd-1) in UNSIGNED mode. If W is even, discard and repeat. If
  W is odd, the root is (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2,
  and an X measurement gives rem mod 2 exactly.

In the ideal run, by fair parity in Lemma 5.4, each attempt succeeds with probability exactly
1/2, even if s1 was wrong. Set bit g of s2. In the ideal run with s1 correct, every bit is
correct. Output (s1 + M s2) mod N.

## 8. Complete algorithm, four cutoffs and success

For n < 256 use exhaustive shift testing. For t' = 0, ..., N-1 use at most
n+10 fresh copies, subtract t' modulo N controlled by the first qubit, and
measure that qubit in X. Reject t' at the first minus and output the first
candidate passing every test, or 0 if none. The true t' = s always passes;
each wrong candidate passes a fresh test with probability 1/2. Thus a wrong
output has probability < (N-1) 2^(-n-10) < 2^-10. It uses at most N(n+10)
copies, O(n) qubits and O(n^2) classical bits, and all charged work is
O(N n^4). This fixed finite prefix is absorbed in the stated asymptotic
bounds; it covers N = 2 and n = 1.

For n >= 256 compute R, Delta, m, the profile, q0, G, K (Section 6) and

    H0 = Smax K + 2n,
    Qstar = 2 G H0 + 2n,          Qcap = 1024 Qstar,
    Wstar = 2 m 2^R H0,           Wcap = 1024 Wstar.

After Qcap is fixed, compute the Section 3 parameters sn and Cf and initialize the acquisition, weighted-attempt and high-confidence-fallback counters to zero. The fallback cap is checked by EXTRACT before starting a high-confidence RUN; exceeding it aborts the whole algorithm with output 0.
Before any acquisition that would exceed Qcap, abort: release all
registers and output 0. Before a combiner attempt, after building its
inputs, check whether adding w_i would exceed Wcap; if so abort likewise,
otherwise add it and execute the complete attempt. EXTRACT uses this fixed
Qcap. Check the fourth, root-frequency cutoff in Section 6. Run the odd-part decoder of Section 6 followed by the 2-adic procedure
of Section 7, then output (s1 + M s2) mod N. All loops have fixed explicit
bounds, so the algorithm halts on every branch.

Expected acquisitions in the ideal uncapped run. Each accepted leaf costs
at most two source copies in expectation (acceptance probability > 1/2 in
Section 6, exactly one copy in Section 7). Let E_i be a uniform bound on the
expected number of copies consumed by one level-i call, conditional on any
history before the call. A level-i node makes attempts until one returns;
by Lemma 5.3 and the tower property each attempt returns with conditional
probability at least 1/2, so the event that attempt a is started has
probability at most (1/2)^(a-1), and the r_i fresh child calls of attempt a
cost at most r_i E_(i-1) in conditional expectation. Summing,
E_i <= 2 r_i E_(i-1) with E_0 <= 2, and since r_i <= v_i + 1,

    E_m <= 2 prod_i 2(v_i + 1) = 2 G.

Pass-through levels only reduce this. The decoder uses at most Smax K
root calls; each of the at most n 2-adic bits uses an expected two root
calls (or two copies when wd = 1) by fair parity in Lemma 5.4, and the indicator that a given
root call occurs is determined by the history before it. By the tower
property the expected total is at most 2G (Smax K + 2n) + 2n = Qstar.

Expected weighted attempts. Let X_i bound the expected number of level-i
attempts in one root call, uniformly over the history before it. A root
makes at most two attempts in expectation, each level-(i+1) attempt builds
r_(i+1) level-i nodes, and each such node makes at most two attempts in
expectation, so X_i <= 2 prod_(j>i) 2r_j <= 2(4R)^(m-i) <= 2*2^((m-i) Delta/2),
using r_j <= 2R and log2(4R) <= Delta/2. A level-i attempt weighs
w_i <= 2^((v_i+1)/2) = 2^(R - (m-i) Delta/2). Hence the expected weight
charged at level i per root is at most 2*2^R, at most 2m2^R over all
levels, and at most Wstar over all root calls by the same tower argument.

Success. Apply Markov separately to the acquisition count and the weighted
total of the ideal uncapped process: each cutoff changes the run only on an
event of probability at most 1/1024. The odd-part error is at most 2^-19 by
Section 6, and conditional on its correctness the 2-adic measurements make
no error. On the actual run, the probability of any EXTRACT label error is
at most 2^-14 by Section 3, and the extra fallback cap changes the run with probability at most 2^-20. Couple the actual and ideal outer processes until a wrong label or any of the four cutoffs. The fourth cutoff adds at most 2^-20 by Section 6. Total failure is at most

    2^-10 + 2^-10 + 2^-14 + 2^-19 + 2^-20 + 2^-20 < 2^-8.

The finite branch meets that bound as well. This proves unconditional
full-secret success at least 1 - 2^-8 > 3/4 for every N >= 2 and s. All
trials, failures and aborts remain in the resource counts; nothing is
postselected free of charge, and no expected-only resource statement is
used for the declared bounds.

## 9. Every-branch resources and explicit envelopes

### 9.1 Profile estimates

Lemma 9.1 (capacity). For every R >= 2, S(R) >= (R-1)(2R-3)/Delta(R), and
m(R) <= 2R.
Proof. Put X=2R-1 and Dl=Delta(R). The positive arithmetic progression
has m=floor((X-1)/Dl)+1 terms. Thus S>=mX/2>=X(X-1)/(2Dl)
=(R-1)(2R-1)/Dl>=(R-1)(2R-3)/Dl. Since Dl>=2, m<=2R. QED.

Lemma 9.2 (explicit threshold). Let c be a POSITIVE real number with 1/2 < c^2 <= 1
and let L0(c) be the least integer L >= max{16, 1/((2c^2 - 1) ln 2)} with

    (c^2 - 1/2) L >= log2(8 c) + (1/2) log2 L + 1.                      (9.2)

Then for every n >= 2^(L0(c)), R <= ceil(c t) <= c sqrt(n log2 n) + 1.
Proof. First, (9.2) holds for every real L >= L0(c): the function
(c^2 - 1/2) L - (1/2) log2 L has derivative (c^2 - 1/2) - 1/(2 L ln 2), which
is positive for L > 1/((2c^2 - 1) ln 2), so it is increasing on
[L0(c), infinity). Now fix n >= 2^(L0(c)), so L = log2 n >= 16 satisfies
(9.2), and t = sqrt(nL) >= sqrt(2^16 16) = 1024, hence c t >= 3/2 (as
c > 0.7). Put R' = ceil(c t) >= c t. By minimality of R it suffices to show
S(R') >= n - 1, and by Lemma 9.1 it suffices that
(R'-1)(2R'-3) >= (n-1) Delta(R'). Since
Delta(R') = 2 ceil(log2(4R')) <= 2 log2(4R') + 2 = 2 log2(8R'), it
suffices that

    (R'-1)(2R'-3) >= 2 n log2(8 R').                                     (9.1)

Left side: (R'-1)(2R'-3) = 2(R' - 3/2)^2 + (R' - 3/2) >= 2(R' - 3/2)^2
>= 2(c t - 3/2)^2 >= 2 c^2 t^2 - 6 c t = 2 c^2 nL - 6 c t.
Right side: R' < c t + 1 = c t (1 + 1/(c t)), so
log2(8 R') < log2(8 c) + log2 t + log2(1 + 1/(c t))
= log2(8 c) + (L + log2 L)/2 + log2(1 + 1/(c t)).
Hence (9.1) follows from
2 c^2 nL - 6 c t >= 2n [log2(8 c) + (L + log2 L)/2 + log2(1 + 1/(c t))],
that is, after dividing by 2n and using t/n = sqrt(L/n), from

    (c^2 - 1/2) L >= log2(8 c) + (1/2) log2 L + 3 c sqrt(L/n) + log2(1 + 1/(c t)).

For L >= 16 the two last terms are small: sqrt(L/n) = sqrt L 2^(-L/2) is
decreasing in L (its logarithmic derivative 1/(2L) - (ln 2)/2 is negative
for L >= 2) and equals 2^-6 at L = 16, so 3 c sqrt(L/n) <= 3/64 < 0.05; and
log2(1 + 1/(c t)) <= 1/(c t ln 2) <= 1/(0.7 1024 ln 2) < 0.003. Both
together are below 1, so the display follows from (9.2). QED.

Corollary 9.2' (c=176777/250000). For every n>=2^16777216,
R<=ceil((176777/250000)t).

Proof. The exact square gap is c^2-1/2=107729/62500000000>0.
Using ln2>1/2, the derivative requirement is smaller than
62500000000/107729<1000000. At L=16777216=2^24 the left side
of (9.2) is greater than 28, while log2(8c)<3 makes its right side
less than 3+12+1=16. Therefore L0(c)<=16777216. QED.

Lemma 9.3 (limit). R(n)^2/(n log2 n) -> 1/2, so for every rational
c > 1/sqrt 2 one has 2^R = O(2^(c t)); and R = O(t) uniformly for n >= 256.
Proof. Write X = 2R - 1 and Dl = Delta(R). The last summand of S(R) is at
most Dl and m <= (X-1)/Dl + 1 = (X + Dl - 1)/Dl, so the arithmetic-series
value gives S(R) = m (X + last)/2 <= (X + Dl)^2/(2 Dl). With Lemma 9.1 at
R-1, the defining inequalities S(R-1) < n - 1 <= S(R) give

    (R-2)(2R-5)/Delta(R-1) < n - 1 <= (2R - 1 + Dl)^2/(2 Dl).            (9.3)

From S(R) <= 4R^2 (m <= 2R terms, each at most 2R) and (9.3) we get
(n-1)/4 <= R^2 <= n Delta(R-1) + O(R) = O(n log2 n), hence
log2 R = (1/2) log2 n + O(log2 log2 n). Since 2 log2(4R) <= Delta(R)
<= 2 log2(8R), both Delta(R) and Delta(R-1) equal log2 n + O(log2 log2 n),
and in particular Dl = o(R). Now (R-2)(2R-5) >= 2R^2 - 9R and
(2R - 1 + Dl)^2 <= 4R^2 (1 + Dl/(2R))^2 = 4R^2 (1 + o(1)), so (9.3) yields
(2R^2 - 9R)/Delta(R-1) < n - 1 <= 2R^2 (1 + o(1))/Delta(R). Dividing by
n log2 n and using Delta/log2 n -> 1 on both sides gives
R^2/(n log2 n) -> 1/2. For the second statement apply Lemma 9.2 to c when
c <= 1, and to the coefficient 1 when c > 1 (then R <= ceil(t) <= ceil(c t));
in both cases the coefficient used satisfies 1/2 < c^2 <= 1, and (9.2) holds
for all large L because its left side grows linearly, so L0 is finite. The
third statement holds because R <= n for all n and the finitely many
n < 2^16777216 contribute an absolute constant. QED.

Consequences. By Corollary 9.2', 2^R <= 2 2^((176777/250000)t) for n >= 2^16777216, and
for 256 <= n < 2^16777216 the bound R <= n gives an absolute outside constant: every
loop of the algorithm is capped by explicit functions of n, so for each of
these finitely many bit lengths the worst case of every resource is a finite
number, and the maximum over them of its ratio to the envelope is absolute.
Further, log2 q0 <= log2 G <= R + 3 + log2 R (Lemma 9.4), so
K = O(R + log n) = O(R). The additional estimate below gives H0=O(n). Also 2^R >= n for every n >= 256:
S(8) = 20 < 255 <= n - 1 gives R >= 9, which settles n in {256, 257}; for
n >= 258, S(R) <= 4R^2 (at most 2R summands, each at most 2R) and
S(R) >= n - 1 give R >= sqrt((n-1)/4) >= log2 n, because
sqrt(257/4) > 8.015 > log2 258 and the derivative difference
1/(4 sqrt(n-1)) - 1/(n ln 2) is positive for n >= 34. Hence log n = O(R)
and n^6 = O(n^5 2^R).

Lemma 9.4 (profile product and caps). One has G<=8R2^R,
m=Theta(R/log R), Wcap=O(n R/log n *2^R), and for EVERY fixed A>0,
G=O(n^(-A)2^R). In particular Qcap=O(n^(-8)2^R).

Proof. Let h=floor(m/2). Since m Delta>2R-2, at each of the bottom h
levels v_i+1=2R-(m-i)Delta<R+1<=(3/2)R. The other factors satisfy
v_i+1<=2R. Therefore

    G<= (4R)^m (3/4)^h.

Also m Delta/2<=R-1+Delta/2 and 2^(Delta/2)<8R, so
(4R)^m<=2^(m Delta/2)<4R2^R, giving the coarse bound G<8R2^R.
Since (4/3)^5>4, the stronger estimate is

    (3/4)^floor(m/2)<=2*2^(-m/5),
    G<=8R2^(R-m/5).                                        (9.4a)

The exact expression for m and Delta=Theta(log R) give
m=Theta(R/log R). Since R>=sqrt(n-1)/2 and R<=n, one has
m/log n>=Omega(sqrt n/(log n)^2)->infinity. Consequently
n^A R2^(-m/5) tends to zero for every fixed A, proving the product claim.
Taking A=10 and the coarse bound H0=O(nR)<=O(n^2), and R/log n->infinity yields

    Qcap=1024(2G H0+2n)=O(n^(-8)2^R+n)=O(n^(-8)2^R).

The last absorption is valid because 2^R exceeds every fixed polynomial
in n eventually. Every smaller finite range contributes only an absolute
constant, with literal finite caps on all branches.

For a matching lower bound on log2 q0, the top ceil(m/2)
factors v_i+1 are at least R for all sufficiently large R:
(m-1)Delta<=2R-2, so their indices satisfy
(m-i)Delta<=R-1. Hence log2 q0>=ceil(m/2)log2 R=Omega(R).
Together with the upper bound this gives log2 q0=Theta(R),
Hcap=Theta(R), and eventually Hcap>=8. Formula (6.2) yields
Smax=O(n/R+1), K=O(R), and H0=O(n+R)=O(n).
The finitely many smaller n have an absolute constant.
Therefore the literal weighted cap obeys

    Wcap=1024(2m2^R H0)
         =O(n R/log n *2^R).

These are estimates for the ACTUAL integer profile and literal caps.
They do not change the cap algorithm or assume an expected-only resource
bound. QED.

### 9.2 Source copies

On every actual branch Q<=Qcap=O(n^(-8)2^R), in particular O(2^R).
By Corollary 9.2' and finite-prefix absorption this gives the declared
uniform envelope

    Q=O(2^((176777/250000)sqrt(n log2 n))).

Every rejected, discarded, failed and aborted acquisition is counted.
The literal cap's binary length is O(R+log n)=O(R), so h_e=O(R) as
required by Section 3. No negative-power representative is needed in
the structured declaration; the stronger literal-cap estimate is retained
here for the work analysis.

### 9.3 Space

Quantum. A depth-first tree keeps at most sum_i (r_i - 1) + 1 <= B + 1
<= n + 1 = O(n) source-phase qubits as retained siblings and current
outputs (r_i-1=b_i on nonzero levels and sum_i b_i=B). An attempt uses O(n) scratch (Lemma 4.4),
including the r_i-qubit search register, the b_i-bit accumulator, the
Toffoli ladder and comparison ancillas; EXTRACT and the transforms use O(n)
more. Released registers are reused, so S_Q = O(n).

Classical. Every retained label has O(n) bits (Section 4.3), and O(n) labels
are retained, giving O(n^2) bits. The profile (m = O(R) entries of O(log n)
bits), the four counters/checks and their caps (O(n) bits), the current search
description (x0, x1, e, a loop counter: O(n) bits), the recursion stack
(O(m) frames of O(n) bits), EXTRACT scratch and verifier windows (O(n^2)), the K decoder records
with O(n)-bit frequencies and residues (K = O(R) <= O(n), so O(n^2)), and
the modular constants (n numbers of O(n) bits) all fit in O(n^2). No list of
subsets, fiber members or candidates is ever stored. Therefore S_C = O(n^2),
and every addressing charge is O(log(S_C + S_Q + 2)) = O(log n).

### 9.4 Work, on every actual branch

Combiners and full labels. By Lemma 4.4, residue predicates, searches
and the quantum pair instrument cost O(R^2 w_i) per charged attempt.
Their total is at most

    O(R^2 Wcap)=O(n R^3/log n *2^R)
      =O(n^(5/2)(log n)^(1/2)2^R).

Charge full-label and controller work at O(n) per supplied input plus
O(n) per node/counter action. At a fixed level, delivered child outputs
descend from disjoint nonempty sets of acquisitions: inputs are not reused
after a failed attempt. Thus at most Qcap input qubits are delivered at
that level. Completed and refused attempts each need at least two such
inputs. A global abort leaves at most m pending frames; their supplied
inputs are already charged, and remaining bookkeeping is polynomial.
Consequently all full-label/setup work costs O(nmQcap)+poly(n). This
includes preparation before a weight check; already built children remain
charged. Since m<=2R<=2n and Qcap=O(n^(-8)2^R), that cost is smaller than
the displayed search-work envelope. No full-label generation is free.

Verified extraction and source processing. Section 3 gives
O(n^2 log n Qcap) core steps on EVERY branch, including cheap estimates,
verification, all capped fallbacks, source charges, transforms and aborts.
By Lemma 9.4 this is O(n^(-6)log n 2^R), also smaller.

Decoder. There are at most 2n stages, at most 512Fmax=512nq0
candidates per stage, and K records. Multiplying f_i by the first
candidate numerator costs O(n^2) per record per interval; later
candidates update by O(n)-bit additions and constant table lookup.
The frequency guard and all absolute values/quotients cost O(n)
per root. Thus O(n^3 K q0+n^3 K) core steps is a conservative
bound. Since q0<=G=O(n^(-10)2^R) and K=O(R)<=O(n),
this is O(n^(-6)2^R+n^4), contained in the search-work envelope.
Even unguarded labels have O(n) bits. The largest j is at most
log2 M+O(1) by minimality and pdec=step+2, so all stored
frequencies, candidate numerators and modular residues have O(n)
bits. No exponential table or uncharged decoding step is used.

Preprocessing and bookkeeping cost O(n^6) core steps by the conservative
schoolbook estimate. Since R/log n->infinity, 2^R eventually exceeds n^4,
so O(n^6) fits O(n^(5/2)(log n)^(1/2)2^R). All smaller finitely many bit lengths
have explicit finite caps and contribute an absolute outside constant.
Measurements, initialization, resets, classically generated gates and
all loop/counter actions are included in the preceding ledgers.

Finally multiply by the full O(log n) address charge. The result is

    T=O(n^(5/2) (log2 n)^(3/2) 2^R)
     =O(n^(5/2) (log2 n)^(3/2) 2^((176777/250000)sqrt(n log2 n))).

All four bounds apply jointly to this single parameter rule and all four caps,
on every execution branch.

### 9.5 Exact growth indices

For either exponential envelope, log2 B = (176777/250000) sqrt(n log2 n) + O(log n), so
log2 log2 B = (1/2) log2 n + (1/2) log2 log2 n + O(1), whose ratio to log2 n
tends to 1/2. The two space envelopes n^2 and n have index 0. The supported
resource structures are exactly the displayed expressions; no coefficient is
inferred from a heuristic or from an unspecified inner big-O. Only time
contributes the numeric score [1/2].

## 10. Error tolerance and limits

The fractional tolerance is epsilon(n) = 0 under the exact error-model text:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

All N >= 2 and s meet the success and resource guarantees above under this
promise. No positive tolerance or impossibility of greater tolerance is
asserted. The result is a rigorous implementation and accounting tradeoff
of known sieve and search ideas, not a cube-root-time result. Hosted
mathematical acceptance, if obtained, remains fallible review rather than
formal proof.
