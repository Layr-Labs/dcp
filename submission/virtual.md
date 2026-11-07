# Complete virtual program V only: GPS-Q13

EVERY algorithm, implementation, resource and allocation assertion in the
source body below concerns virtual V. Its quadratic classical and linear
quantum bounds are not the physical bounds of LLV-GBANKQ13. The current
physical algorithm and claims are defined in proof.md. The entire original
source body is byte-identical to SHA-256 4ec34d3f8f5f3873e882486a34352fe1cc95d1a7585f39273d74369442ed2ff0.
No ancestor JSON or historical verdict is a mathematical premise.

--- BEGIN COMPLETE VIRTUAL SOURCE ---

# GPS-Q13: polynomial workspace with cube-root source growth

## 0. Joint theorem, literal configuration and provenance

For everyN>=2 ands inZ/NZ putn=ceil(log2N),L=log2n. The single
GPS-Q13 algorithm below recovers the full secret with unconditional
probability at least1-2^-8 from independent ideal copies. On EVERY
branch, including retries, failed attempts, discarded copies and aborts,

 T=O(2^((2/3)n^(2/3)log2n+2n^(2/3)sqrt(log2n))),
 S_C=O(n^2),S_Q=O(n),Q=O(2^((1/2)n^(1/3))).

All outside constants are absolute. The indices are[2/3,0,0,1/3].
Fractional tolerance is zero under the canonical independent-ideal-copy
promise. The actual finite exhaustive branch isn<2^64. Otherwise use
u=ceil(n^(1/3)),ell=ceil(log2n),z=ceil(log2ell),
b=ceil(4u^2(ell+2z+9)/3),m=ceil((n-1)/b),v_i=b.
The integeru is the leastu>=1 withu^3>=n, computed by integer binary
search. Every parameter uses exact integer arithmetic fromN.

Direct proof-text and framework source: my GPS-WQLOG prototype, proof
SHA-256 c4c6f345c669e08edf4386cb26ba2f17054ef3868feb3fd9762e563a31cac034.
Its final public mapping appears in the note/dependency declaration.
It supplies the logarithmic-width correction, source-budgeted wide tree,
above-half combiner, verified extraction, all-modulus decoder, two hard
cutoffs and acquisition-based every-branch attempt counting. Its GPS-WQ,
GPS-HALF, GPS-VLE, GPS-C3, CS1, GPS3, GPS2, GPS, PSR2, PSW2, PSG1,
Regev, Kuperberg, Kitaev and BBHT credits remain acknowledged. No
previous review or acceptance is a mathematical premise.

The new actual width grows as(4/3)n^(2/3)(logn+2loglogn+O(1)),
not sqrt n timeslogn. The shallower tree reduces the source growth
index from1/2 to1/3 while raising time from1/2 to2/3. Both workspaces
are retained. The positive lower-order time term upper-bounds the
proved loglog correction in the structured format. This is a joint
resource tradeoff, not dominance, optimality or practical performance.


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
Compute a2 by repeatedly dividing N by2 until the quotient is odd; that
quotient is M. Equivalently n=bit_length(N-1), d=bit_length(N)-1,
where bit_length(x) is the unique k with2^(k-1)<=x<2^k for x>=1.
The symbols s1,s2 in this analysis are unknown until the decoders recover
them; no operation computes an unknown secret from its definition.

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

Cost per call: O(n^2) precomputation plus t_V=O(h_e) rounds of O(n log n), hence O(n^2+n h_e log n) core steps. Section9 proves h_e=O(sqrt n); since sqrt n<=n, this is O(n^2 log n). Classical scratch is O(n log n) bits.

### 3.4 High-confidence extraction and output

If verification accepts, EXTRACT outputs k_A. Otherwise it runs k_H = RUN(F(h_e)),
the high-confidence extraction, and outputs k_H, subject to the cap in 3.5.
After the last test of the call, the data register is reset. EXTRACT uses no
Fourier transform, no lookup, and no rotation other than H and S, and O(n)
quantum scratch (n data qubits, one ancilla, arithmetic).

### 3.5 Cap on high-confidence runs

Let sn be the least integer >= sqrt n (computed exactly by integer arithmetic) and Cf = ceil(Qcap/sn). A counter
records the number of RUN(F(h_e)) executions. If a call would start the
(Cf+1)-st one, GPS-Q13 stops, releases everything and outputs 0 (ABORT).

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
h_e=O(sqrt n), so this is O(n^2 Qcap), contained in
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
survival. The outer acquisition cap is analyzed separately in Section8. All actual-branch
resource bounds use both the acquisition and fallback caps.

## 4. Width profile, Grover pair search and the depth-first tree

### 4.1 A constant wide profile for the cube-root source budget

For n>=2^64 use the exactu,ell,z,b,m ofSection0. For any requested
D with2<=D<=n putB=D-1, and allocate its bits from the top down:
fori=m,...,1 setb_i=min(b,remaining), then subtractb_i. Thus
sum_i b_i=B, since mb>=n-1. Setr_i=b_i+1 on nonzero levels;
zero levels pass through unchanged. Put

 q0=(b+1)^m,G=(2(b+1))^m. SetR=b+1 for cost bounds.

These literal upper-bound products include trimmed and pass-through
levels. Their actual product factors are no larger. Section9 proves
b+1<=n,log2G=O(n^(1/3)), and the required joint source/work bounds.
The rest of the tree, explicit combiner, decoder and two-cutoff
algorithm is unchanged. No weighted-attempt cutoff is executed.

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

A PS_TREE_D call, 1 <= D <= n, receives independent leaf phase qubits whose
known integer labels are uniform on [0, 2^D) (Sections 6 and 7 say how a
leaf is made). Put B = D - 1. If B = 0 return one leaf. Otherwise allocate
widths top-down: for i = m, m-1, ..., 1 put b_i = min(v_i, B - sum_(j>i) b_j).
Since sum_i v_i >= n - 1 >= B this ends with sum_i b_i = B. Put
p_i = sum_(j<i) b_j and r_i = b_i + 1. Level 0 returns a leaf. A level with
b_i = 0 returns its level-(i-1) child unchanged. A level with b_i >= 1 is a
NODE: it obtains r_i independent level-(i-1) outputs one at a time, retaining
earlier siblings, and then runs one ATTEMPT of the combiner below.
There is NO weighted-attempt counter or cutoff. Every child and every
attempt is charged through its acquisitions and the per-level disjoint
source accounting of Section9. For cost analysis definew_i=2^ceil(r_i/2),
so w_i<=2^ceil((b+1)/2); this is not an algorithmic counter.

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
label handled in a PS_TREE_D call has absolute value below q0 2^D and
O(n + log2 q0) = O(n) bits, including on branches with incorrect extracted
labels. All decisions of a level-i attempt (the measured residue, both
searches, the test outcome, the pivot) depend only on the residues rho_j,
that is on the input labels modulo 2^(p_i + b_i), and on fresh coins and
fresh search registers. The tree is evaluated depth first and keeps no full
recursion tree.

## 5. Untouched bits, conditional fiber statistics and success probability

Fix a PS_TREE_D call in the ideal run of Section 3. Each leaf label is an
independent uniform k in [0, 2^D). For an integer position p < D write
k = u + 2^p tau with u = k mod 2^p and tau = floor(k/2^p) uniform on
[0, 2^(D-p)) and independent of u.

In the ideal run of Section 3, EXTRACT is replaced by an oracle that
performs the same charged steps and returns the true latent label; its
internal translation-test outcomes and verification/fallback records are excluded from every sigma-field below. In the ideal outer process all EXTRACT-internal coins, estimates, verification verdicts, fallback decisions, fallback counters and loop indices are private discarded records, and the fallback cap is omitted. No argument conditions on that cap surviving or on numerical extraction succeeding. Outer acquisition counts and combiner weights do not depend on those private records when the true latent label is supplied.

Lemma 5.1 (untouched high parts). Consider a level-i node attempt and the
moment just before step 1 of its ATTEMPT, after its r_i inputs are built.
Let Fs be the sigma-field generated by: all coins outside EXTRACT; all combiner outcomes
(measured residues, search outputs, test outcomes, pivots) and all decoder
and 2-adic measurement outcomes recorded so far; the labels modulo 2^(p_i)
of the leaves below this node; and everything (full labels included)
concerning copies outside the subtree of this node. Fs contains neither the
high parts of the leaves below this node nor any EXTRACT-internal outcome.
Then conditional on Fs, the high parts tau_l = floor(k_l / 2^(p_i)) of the
surviving leaves l below this node are independent and uniform on
[0, 2^(D - p_i)).

Proof. The leaves below this node are disjoint from all other copies, whose
labels and outcomes are independent of them. Within the subtree, the inputs
were built by levels i-1, ..., 1. By the last paragraph of Section 4.3 and
induction over levels, every decision and every measurement-outcome law at a
level i' < i is a function of the labels modulo 2^(p_(i') + b_(i')) <= 2^(p_i)
of its own inputs, of fresh coins and of fresh search registers; the
measured residues and the indicator in step 4 are computational-basis
measurements of deterministic functions of x, whose outcome laws
(|X_e|/2^(r_(i')) and 2/|X_e|) do not depend on the phases. EXTRACT's
internal outcomes do not occur in the ideal run and no decision uses
them; the acceptance test of Section 6 (k < 2^d) precedes the tree and
leaves the accepted label uniform on [0, 2^D). Hence the conditional law of
every observed quantity given all leaf labels depends on the leaves below
this node only through their low parts modulo 2^(p_i), and the high parts,
being independent of those low parts and of everything else, remain
conditionally i.i.d. uniform. Leaves of discarded attempts never influence a
later decision. QED.

Lemma 5.2 (conditional residues). In the setting of Lemma 5.1, conditional
on Fs, the residues rho_1, ..., rho_(r_i) of the inputs are i.i.d. uniform on
[0, 2^(b_i)).
Proof. Input j has label a_j = sum_l c_(jl) k_l over its surviving leaves,
with Fs-measurable coefficients c_(jl) in {-1,0,1}, not all zero (Section 4.3),
and the leaf sets of different inputs are disjoint. Then
a_j / 2^(p_i) = C_j + sum_l c_(jl) tau_l where C_j = sum_l c_(jl) u_l / 2^(p_i)
is an Fs-measurable integer (a_j is divisible by 2^(p_i)). Since
p_i + b_i <= B < D, 2^(b_i) divides 2^(D - p_i), so each tau_l mod 2^(b_i) is
uniform given Fs, and adding +-1 times one such uniform variable to an
independent quantity gives a uniform residue. Disjointness gives independence
across j. QED.

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

Lemma 5.4 (root frequency). In the ideal run, for a returned PS_TREE_D root
write each surviving leaf label as k_l = u_l + 2^B tau_l with tau_l in {0,1}.
Conditional on the sigma-field Gt generated by all coins outside EXTRACT, all combiner,
decoder and 2-adic outcomes recorded up to the completion of the tree, the
labels modulo 2^B of its surviving leaves, and everything concerning other
copies (EXTRACT-internal outcomes and the top bits tau_l excluded, as in
Lemma 5.1), the tau_l are independent fair bits, the root has label 2^B W
with

    W = c + sum_(l in S+) tau_l - sum_(l in S-) tau_l,   |S+| + |S-| >= 1,
    |E[exp(2 pi i y W) | Gt]| <= |cos(pi y)|  for every real y,            (5.2)
    Pr[W odd | Gt] = 1/2,                                                 (5.3)

where c is a Gt-measurable integer and S+, S- are the Gt-measurable sets of
leaves with coefficient +1 and -1.
Proof. Apply Lemma 5.1 with p = B to the root node (all decisions at every
level inspect labels modulo 2^(p_i + b_i) <= 2^B only). The label is the signed
leaf sum, its low part sum c_l u_l is divisible by 2^B with quotient c, and
some coefficient is nonzero. Each fair bit contributes an independent factor
of modulus |cos(pi y)| to the characteristic function, and one fair bit with
coefficient +-1 makes the parity of W fair. No uniformity of W itself is
claimed. QED.

## 6. Odd-part recovery by free-frequency decoding

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so
N >= 3 2^a2 and d - 1 >= a2. Put theta = s1/M in [0,1). Every stage uses
D = d, B = d - 1, nq = q0 and

    K = 2^13 (ceil(log2 nq) + ceil(log2 n) + 30).

The stages are j = 0, 1, ..., J, where J = min{ j >= 0 : 2^(j+3) > 2M }. By
minimality, J + 1 <= log2 M <= n.

Source for stage j. Compute alpha_j by extended Euclid and CRT so that
alpha_j = 1 (mod 2^a2) and alpha_j = 2^j (2^(d-1-a2))^(-1) (mod M). Then
alpha_j is a unit modulo N. A leaf qubit is made as follows:
- acquire a fresh copy and apply Mult_(alpha_j);
- run EXTRACT to obtain k, and accept iff k < 2^d (otherwise discard the
  copy and acquire again);
- on acceptance, apply X to the control.

In the ideal run, accepted labels are i.i.d. uniform on [0, 2^d), each copy
is accepted with probability 2^d/N > 1/2, and the qubit is pq_k(alpha_j s),
i.e. it has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^(d-1) W th = W 2^(d-1-a2) alpha_j s / M = 2^j W s1 / M   (mod 1),       (6.1)

because 2^(d-1-a2) alpha_j = 2^j (mod M) and s = s1 (mod M). So a PS_TREE_d
root of stage j is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the
known frequency f = 2^j W.

Measurement. For i = 1..K:
- run PS_TREE_d;
- obtain a fair bit beta_i by measuring H|0>;
- measure the root in X (beta_i = 0) or Y (beta_i = 1), recording Z_i in
  {+1,-1} together with W_i and beta_i.

Ideally E[Z_i | f_i, beta_i] = cs_(beta_i)(f_i theta) with f_i = 2^j W_i.

Candidates. Put P_j = j + ceil(log2 nq) + 8, and identify an integer c with
the point zeta = c/2^(P_j) on the circle R/Z.
- Stage 0 uses every c in [0, 2^(P_0)).
- Stage j >= 1 uses every c whose point lies within circular distance
  rad_j = 2^-(j+2) of the previous center z_(j-1). This is one or two
  explicit integer intervals.
- Both z_(j-1) (denominator 2^(P_(j-1))) and rad_j are multiples of
  2^-(P_j), so the two arc endpoints are themselves candidates.
- There are at most 2^(ceil(log2 nq)+7) + 2 <= 2^(ceil(log2 nq)+8) candidates.

The candidate set is fixed by information available at the start of the
stage.

Score. For each candidate, using exact integer arithmetic,

    score(c) = sum_i Z_i * tab_(beta_i)( ((f_i c) mod 2^(P_j)) / 2^(P_j) ).

Enumerate the candidates in increasing order, keeping the K residues
(f_i c) mod 2^(P_j) and updating each with one addition per step, and keep a
running maximum. Let z_j = c*/2^(P_j) for the least maximizer c*. All loops
have fixed lengths, and the decoder returns a candidate on every branch.

Lemma 6.1. Suppose theta is within circular distance rad_j of z_(j-1) (no
condition when j = 0). Then, in the ideal run, with probability at least
1 - 2^-20/n, theta is within circular distance 2^-(j+3) of z_j.

Proof. Let Fs_i be the sigma-field of everything up to and including root i
of the stage, and Gt_i the sigma-field of Lemma 5.4 for tree i. For a
candidate point zeta, let Delta = theta - zeta, taken as a circular
difference, and let xi_i = Z_i cs_(beta_i)(f_i zeta). Conditional on
Fs_(i-1), Gt_i and the top bits of tree i (hence on W_i), averaging over the
fair basis bit gives

    E[xi_i | ...] = (1/2)[cos(2 pi f_i theta) cos(2 pi f_i zeta) + sin(..) sin(..)]
                  = (1/2) cos(2 pi f_i Delta).

By (3.1), the computed score differs from sum_i xi_i by at most K/625.

Near point. Let zeta0 be the candidate nearest theta. In stage 0 the
candidates cover the circle. In stage j >= 1 the candidate arc contains theta
and has candidate endpoints. Either way |Delta0| <= 2^-(P_j + 1). Since
|f_i| < 2^j 2 nq (Section 4.3: |W| < 2 q0),

    |f_i Delta0| < 2^(j+1) nq 2^-(P_j + 1) <= 2^-8.

So E[xi_i | Fs_(i-1)] >= (1/2) cos(pi/128) for every realization.

Far points. Call zeta far if |Delta| >= 2^-(j+3). In stage 0 we always have
|Delta| <= 1/2. In stage j >= 1, both theta and zeta lie within rad_j of
z_(j-1), so |Delta| <= 2^-(j+1). Hence xx = 2^j |Delta| lies in [1/8, 1/2] for
every far zeta. Tree i uses copies independent of Fs_(i-1). By Lemma 5.4, its
top bits are fair and independent given Fs_(i-1) and Gt_i. So by (5.2) with
y = 2^j Delta, and since a real part is at most the modulus,

    E[xi_i | Fs_(i-1)] = E[ (1/2) Re E[exp(2 pi i 2^j Delta W_i) | Fs_(i-1), Gt_i] | Fs_(i-1) ]
                       <= (1/2) cos(pi xx) <= (1/2) cos(pi/8).

Concentration. For each fixed candidate, sum_i (xi_i - E[xi_i | Fs_(i-1)]) is
a martingale whose increments lie in intervals of length 2. By
Azuma-Hoeffding it deviates by at least K/64 with probability at most
exp(-(K/64)^2/(2K)) = exp(-K/8192). Outside these events for zeta0 and every
far candidate,

    score(zeta0) >= (K/2) cos(pi/128) - K/64 - K/625
                 >  (K/2) cos(pi/8)   + K/64 + K/625 >= score(far zeta),

because (1/2)(cos(pi/128) - cos(pi/8)) > 0.0379 > 2/64 + 2/625 = 0.03445. So
the maximizer is not far. There are at most 2^(ceil(log2 nq)+9) events, and
since e^-x <= 2^-x, exp(-K/8192) <= 2^-(ceil(log2 nq) + ceil(log2 n) + 30).
The failure probability is therefore at most 2^(9-30)/n <= 2^-20/n. QED.

For stage j+1 the hypothesis of Lemma 6.1 is the conclusion of stage j, since
2^-(j+3) = rad_(j+1). By induction, with probability at least 1 - 2^-20,
theta lies within 2^-(J+3) < 1/(2M) of z_J. Output s1 = floor(M z_J + 1/2)
mod M. This equals s mod M because theta = s1/M, and the circular distance
handles wrap-around.

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
- If wd >= 2: run PS_TREE_wd (D = wd). If W is even, discard and repeat. If
  W is odd, the root is (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2,
  and an X measurement gives rem mod 2 exactly.

In the ideal run, by (5.3), each attempt succeeds with probability exactly
1/2, even if s1 was wrong. Set bit g of s2. In the ideal run with s1 correct, every bit is
correct. Output (s1 + M s2) mod N.

## 8. Complete algorithm, two cutoffs and unconditional success

For n<2^64 use exhaustive shift testing. For eachcand=0..N-1,
subtractcand from the controlled data as inT2, and measure the first
qubit inX on at mostn+10 fresh copies. Rejectcand at its first minus,
output the first candidate with all pluses, or0. The true candidate
always passes; each wrong one passes a fresh test with probability1/2.
The total wrong-output probability is at mostN2^(-n-10)<=2^-10.
The source/work counts are finite, S_Q=O(n),S_C=O(n^2), and the
fixed finite prefix contributes absolute constants to all envelopes.

For n>=2^64 compute the Section4.1 profile and the Section6 decoder
K=8192(ceil log2q0+ceil log2n+30), and set

 H0=nK+2n,Qstar=2G H0+2n,Qcap=1024Qstar.

Fix Section3's extraction parameters and fallback capCf from thisQcap.
Initialize the acquisition and high-confidence-fallback counters.
Before an acquisition exceedingQcap, release every register and output0.
InsideEXTRACT, a requested high-confidence run exceedingCf likewise
aborts the whole algorithm. There is no weighted-attempt cutoff.
Execute the odd decoder of Section6 then the 2-adic procedure of Section7,
returning(s1+M s2) modN. Every retry consumes fresh source calls, all
internal search loops have fixed lengths, and the two counters enforce
termination on every branch.

Expected ideal acquisitions. Analyze the same process with both caps
omitted, true latent labels returned byEXTRACT, and its private records
excluded as inSection5. IfE_i bounds expected copies of a level-i call,
uniformly over history before its fresh-source call, thenE_0<=2 and
E_i<=2r_i E_(i-1) by the above-one-half conditional success lemma.
To justify this without conditioning on favorable outcomes, trialj
starts with probability at most2^(-(j-1)); its fresh children have
conditional expected demand at mostr_i E_(i-1). Summing nonnegative
trial costs gives the recurrence. Pass-through levels reduce demand.
ThereforeE_m<=2prod_i2r_i<=2G.
The odd decoder requests at mostnK roots. Every 2-adic bit uses an
expected two roots (or copies atwd=1), by fair parity. This demand statement holds even after a wrong odd answer:
all structural projections are phase blind and the reduced labels keep
their conditional uniform routing law; only final bit correctness needs
the odd answer to be right. The tower property gives total expected acquisitions at mostQstar. Markov
againstQcap changes the run with probability at most2^-10.

The ideal odd decoder fails with probability at most2^-20, and the
2-adic procedure makes no error conditional on its correctness. Section3
bounds any extraction-label error by2^-14 and extra fallback-cap abort
by2^-20. Couple until the first label error or cutoff, never conditioning
on either cap surviving. Total failure is at most

    2^-10+2^-14+2^-20+2^-20<2^-8.

The exhaustive finite branch also meets this bound. This proves the
unconditional full-secret success guarantee for the SAME two-cutoff
configuration whose worst-case resources are bounded next.

## 9. Every-branch resources and explicit envelopes

### 9.1 Explicit cube-root source bound

LetL=log2n>=64,x=n^(1/3),y=n^(2/3)=x^2. SetD=L+2log2L+9.
The exact integers obeyx<=u<=x+1,L<=ell<=L+1,
log2L<=z<=log2L+2. Therefore

 D<=ell+2z+9<=L+2log2L+14<=3L,
 (4/3)yD<=b<=(4/3)(x+1)^2*3L+1<=9yL.

The last inequality uses(x+1)^2<=2y andx>=2. Since18L<=x for
L>=64 (true at64 and the exponential-to-linear ratio increases),
one has2(b+1)<=32yL andb+1<=n. WriteA=log2(2(b+1)). Then

 A<=(2/3)L+log2L+5<=(2/3)D-1, and A<=L.

The second inequalities follow fromlog2L>=0 and
L/3-log2L-5>=0 forL>=64 by threshold and increasing derivative.
As m<=3x/(4D)+1,

 log2G=mA<=x/2-3x/(4D)+A<=x/2-x/(4L)+L<=2x.

The same decoder/cap arithmetic givesK<=2^15x,H0<=2^16n^2
andQcap<=2^28G n^2. Thus

 log2Qcap<=x/2-x/(4L)+3L+28<=x/2-x/(4L)+4L.

For everyL>=64,x=2^(L/3)>=16L^2: at64 alreadyx>2^21
while16L^2=65536; the logarithmic derivative of2^(L/3)/L^2
is(ln2)/3-2/L>0 thereafter. Consequently

 Qcap<=2^((1/2)n^(1/3)) on EVERY main-branch input.

The finite exhaustive branch changes only an absolute outside constant.
The cap's binary length isO(n^(1/3)), so extraction parameters and
all full-label/counter fields remain polynomial-sized as required.


### 9.2 Space

Quantum. The depth-first tree retains at mostsum_i(r_i-1)+1=B+1<=n+1
phase qubits, since r_i-1=b_i. Search/residue scratch isO(b+1)<=O(n),
and source transforms andEXTRACT addO(n). Registers are reset/reused,
soS_Q=O(n), including every abort branch.

Classical. Every signed label has magnitude belowq0*2^D and thus
O(n+log2q0)=O(n) bits. TheO(n) retained labels consumeO(n^2) bits.
The m-frame stack, profile, source/fallback counters and caps, search
descriptions, modular constants and extraction/verifier scratch all fit
O(n^2). DecoderK=O(sqrt n) records each haveO(n) bits, and candidates
are streamed rather than stored. ConsequentlyS_C=O(n^2), and the
full address charge isO(log n). No circuit of exponential length,
fiber list, oracle table or full recursion tree is stored.

### 9.3 Time on EVERY branch

At each nonzero level, delivered inputs descend from disjoint nonempty
acquisition sets. Inputs of failed attempts are not reused. Thus at
mostQcap inputs are delivered at any fixed level and at mostmQcap
completed/refused node actions occur across the tree. At a global abort,
the at mostm pending frames have their children charged and only
polynomial cleanup. This is a deterministic bound from the hard cap.

Lemma4.4 costsO(R^2 w_i)+O(nr_i) per action, withR=b+1<=n
andw_i<=2^ceil((b+1)/2). Source transforms, verified extraction,
decoder streaming, circuit generation, source charges, measurements,
initialization, resets, addresses and preprocessing all fit the same
conservative uniform bound for absoluteC,

 T<=C n^10 Qcap 2^ceil((b+1)/2).                    (9.2)

ForL>=64,b<=(4/3)(x+1)^2(L+2log2L+14)+1.
UsingQcap<=2^(x/2) andceil((b+1)/2)<=b/2+1 gives

 log2(T/C)<=(2/3)yL+(4/3)y log2L+40y.             (9.3)

Indeed the leadingy contribution fromb/2 is
(2/3)yL+(4/3)y log2L+(28/3)y. The rounding term from
(x+1)^2-y=2x+1 is at most(2x+1)*2L<=6xL<=6y,
usingL<=x. Alsox/2<=y/2,10L<=10y, and rounding constants
are at most3y. Their sum is below40y. Every polynomial cost in
(9.2) is included; no unknown exponential coefficient is used.

ForL>=4096,log2L<=sqrt L and40<=(2/3)sqrt L.
Hence(4/3)log2L+40<=2sqrt L, proving

 T<=C 2^((2/3)n^(2/3)log2n+2n^(2/3)sqrt(log2n)).

All main lengths below2^4096 have literal finite caps and contribute
only an absolute outside constant. The actual branch threshold stays
n=2^64. These are joint bounds for the same width and two cutoffs.


### 9.4 Exact growth indices and comparison

For time,log2B=(2/3)n^(2/3)L+2n^(2/3)sqrt L
=(2/3)n^(2/3)L*(1+3/sqrt L), giving exact growth index2/3.
Sources2^((1/2)n^(1/3)) have index1/3. Polynomial spacesn^2,n
have index0. These are exactly the submitted structured objects.
Only time supplies the numeric score[2/3].
GPS-Q13 trades greater time for lower source demand than GPS-WQLOG,
retaining both workspace envelopes and the clean-copy promise. It
does not dominate the square-root-time family and claims no optimality.


## 10. Error tolerance and limits

The fractional tolerance is epsilon(n) = 0 under the exact error-model text:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

All N >= 2 and s meet the success and resource guarantees above under this
promise. No positive tolerance or impossibility of greater tolerance is
asserted. The result is a source-budgeted polynomial-space tradeoff. It does not
claim practical performance, positive robustness or optimality.
