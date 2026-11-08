# COMPLETE new LOGARITHMIC-BOOST virtual reference

This full source is ADAPTED from corrected saturated IFCS60_LOWBOOST,
IFCS1310_FILTERED_P124H and IFCS1310_FILTERED_SHARP, ultimately actual
7bd3dabc-c131-48b7-a46d-30fe2e1301fb,commit
4a86c6fc47fab61ec0eec71ebe756f9a2404606b,original65237-byteSHA256
1ebbab84308e96da2d6f8f148ccabd9bf6822cd7539c9b07efece2e69800cb3b.
The real new schedule has
mu0=5999/10000,w=ceil(mu0sqrt n),v=bitlength(n),nu=v,gamma0.
There is NO fixed positive d0sqrt n boost. Section7 supplies full new
capacity/height/B1-B7 proofs;13 rederives sharper raw copy/work powers.
All source/instrument/LE/merge/window/cap/decoder and corrected
filtration/retry-cost arguments are supplied fully. Original credits
and immutable source identities remain provenance, not verdicts.
All resource statements concern VIRTUAL P; physical main implements
its complete counted bank and separately proves physical bounds.

# LOGBOOST saturated implicit-fiber reference P

For everyN>=2,s,n=ceil(log2N), the single algorithm below has whole-secret
success>=1-2^-8 from independent ideal copies, jointly on every branch
with raw T=O(n^4log2n*2^(H00sqrt n)),S_C=O(n²2^(mu0sqrt n)),
S_Q=O(n),Q=O(n^(1/2)log2n*2^(H00sqrt n)),where
mu0=5999/10000,H00=5mu0/6+2/(3mu0)=38662667/23996000.
The actual schedule hasv=bitlength(n),notconstant*d0sqrt n.
Finite branch n<4096 and all complete source primitives/caps/decoders
remain; canonical independent-ideal-copy tolerance is0. Source14's
pure upper envelopes are virtual only. Every original author credit
and corrected proof method is retained below.

<!-- COMPLETE_PUBLIC_SETUP_BEGIN -->
## 0.1. Complete public setup and decoder notation

For EVERY integer N>=2, compute public integers
 n=bitlength(N-1)=ceil(log2N), d=bitlength(N)-1=floor(log2N),
 a2=max{a>=0:2^a dividesN}, M=N/2^a2.
Count trailing zero bits of N for a2 and shift for M. These are exact
integer bit operations using O(n) staged words, not a factoring oracle.
Thus M is odd, N=2^a2*M, 2^d<=N<2^(d+1), and d<=n<=d+1.
The notation below for s1,s2 refers to TRUE secret components in the
proof, not unknown values required by public setup; the decoders
compute their estimates. If M=1 the odd decoder sets s1=0 and skips;
if a2=0 the 2-adic decoder sets s2=0 and skips. Otherwise for M>=3,
 d=a2+floor(log2M)>=a2+1,
so d-1>=a2 and the CRT exponent d-1-a2 is nonnegative. Powers of2
are units modulo odd M. A fresh latent label k uniform on[0,N)
passes k<2^d with probability2^d/N>1/2, and the accepted label is
uniform on[0,2^d); this is the actual range used in decoder9.

On the MAIN branch n>=4096, after computing Section7's literal
profile, define the unused-as-needed public decoder parameters too:
 m_d=min{m in[1,mu]:Sum(m)>=d-1}, nq_d=2^(h_(m_d))*(kappa+1+nu),
 J=min{j>=0:2^(j+3)>2*M},
 K=2^13*(ell(nq_d)+ell(n)+30),
where ell(x)=min{r>=0:2^r>=x}, ell(1)=0, and forx>=2 it is
bitlength(x-1). The tree at D=d exists since d>=4095 on this branch;
Section7 proves m_d<=mu and h_(m_d)<=hmax. These definitions apply
EVEN WHEN M=1 and decoder9 is skipped: then J=0, the unused nq_d/K
are still computed for the declared Q* cap. Thus J+1<=n in every
main case, and all cap/precision/fallback parameters are unambiguously
computed before acquisitions. They agree with decoder9 when M>=3.
For n<4096 only the complete finite tester is executed; its setup
requires the public n,N and has no tree or odd-decoder call.

Notation (CW1's): d = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with
s = s1 + M s2 (mod N); omega = exp(2 pi i/N); data basis states |u>, u in [0,N), are stored in n qubits. A
"label" is a known integer, a "multiplier" W an integer frequency factor, hd a Hamming distance; T denotes
total work only.

<!-- COMPLETE_PUBLIC_SETUP_END -->

## 1. Provenance and what is new

IFCS1310S60 is our IFC-B (IFCB45, 98f6f481-d436-4f37-8134-ff8ddc29b467: our IFC1, 1294d17f-2acf-4e10-9996-6b4375388f49, on
the boosted leaves of our BL1, 4c168837-b12b-47cb-b69c-41ea7e9c0124) in the saturated regime of our IFC34
(759dd9ae-ea6a-413a-8dcb-55e239533985). Sections 6.3 and 8.1 are IFC1's text unchanged (their reading at r = 0 is in
Section 7), Section 8 carries IFC1's edits, and Sections 5 and 11 are edited at IFC1's edit points. As in IFC1, Sections
2-4, 6.1, 6.2, 9, 10, 12, 15 and the Section 6 preamble (except its heading) are e-man07's CW1
(cfe82a87-0d65-454e-b1df-4789dc95aab4), a schedule modification of AdamGagol's CS1
(b56c7ceb-de59-42da-9e3b-6ee96e4e4145 = f1481815-9577-4990-abe3-7b79fa5d9284). Leaf boosts: AdamGagol's CS1-LB and
mpjunior92's CS1-C3L (through BL1); qzv's LL-150 (2db348f1-6660-48c8-8e10-b056131f6baa) published the boosted-leaf
trade-off point first. From e-man07's MW4 (33a6df9d-08d8-488b-a3f7-01f5f32373a4): MERGE4I's steps 5-8, the failure
identity, the two-heap streams (Schroeppel-Shamir, SIAM J. Comput. 1981), the moment argument, the absorption of
Section 14 and the merge at r = 0 (up to Cp and which run is buffered). Class-restricted streams: Howgrave-Graham and
Joux (EUROCRYPT 2010); Hp: our dc3e145e-7ee7-4c4d-ab7e-bbd9a2e9e58a; collimation: Kuperberg (arXiv:1112.3333v1). No
earlier verdict is a premise.

New (Sections 7, 11, 13, 14): the leaf boost nu and the time boost v = bitlength(n) are separate. Above the binary
levels every level is a MERGE4I with fiber exponent l = min(kappa + 2 + v + h, 2 Lam) at height h, its pair fibers
streamed, never stored; a saturated level (l = 2 Lam, r = 0) cancels 3 Lam - kappa bits per two heights. In case B the leaf boost is v < w, as in IFC-B.
Lemma 7.0 bounds the height by H00sqrt n-v+7. The comparison is with public rows on this challenge only.

## 2. Model and counting conventions

A CORE STEP is one of the following:
- one NOT/CNOT/Toffoli/H/S/S^dagger gate;
- one computational-basis single-qubit measurement or reset;
- one Boolean operation on at most three classical bits;
- one classical bit read or write.

Toffoli has an exact constant-size Clifford+T decomposition. Integers are bit
strings, and an L-bit addition, comparison or copy costs O(L) core steps.
Generating a gate costs O(1) core steps. Each core step additionally pays its
address, ceil(log2(Mem+2)) bit operations, where Mem <= S_C + S_Q is the
number of allocated bits and qubits. A source acquisition costs n+1. Hence

    T <= (number of core steps) * (1 + ceil(log2(S_C+S_Q+2))) + (n+1) Q.     (2.1)

There is no QRAM: every lookup is the explicit circuit of Section 6.1.

## 3. Source identities, the latent-label model and data transforms

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
which LE recovers.

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

## 4. Rational trigonometric table

For v in [0,4096) the controller computes rationals Cos[v], Sin[v] within 2^-20
of cos(2 pi v/4096) and sin(2 pi v/4096).

- Bound pi within 2^-90 using Machin's formula pi = 16 atan(1/5) - 4 atan(1/239),
  summing the first 40 terms of each alternating arctangent series. This gives
  two-sided bounds; the tails are below 16 (1/5)^81/81 + 4 (1/239)^81/81 < 2^-91.
- The identity follows from tan(2 atan(1/5)) = 5/12, tan(4 atan(1/5)) = 120/119
  and tangent subtraction.
- At the angle 2 v p_mid/4096 < 7, where p_mid is the midpoint of the pi bounds,
  sum 80 Taylor terms. The remainder is <= 7^81/81! < 2^-170. The angle error
  is < 2^-89, and sin and cos are 1-Lipschitz.
- Round each value to denominator 2^20.

This is a fixed finite rational computation, charged once as an absolute
constant (not advice).

For x in [0,1) put tab_0(x) = Cos[floor(4096x)] and tab_1(x) = Sin[floor(4096x)],
and let cs_0(x) = cos(2 pi x), cs_1(x) = sin(2 pi x). Since cs is 2pi-Lipschitz,

    |tab_beta(x) - cs_beta(x)| <= 2 pi/4096 + 2^-20 < 1/625.                    (4.1)

## 5. Label extraction LE

Input: a data register holding chi_k for a latent k, beside arbitrary
spectators. An upper bound Qcap on the number of LE calls is fixed in advance
(Section 11). LE makes a cheap estimate (5.2), checks it with a randomized
verification (5.3), and only if the check rejects runs the high-confidence
extraction (5.4). A global counter caps the number of high-confidence runs (5.5).
Parameters:

    J_e = n + 4,   h_e = ceil(log2(Qcap (n+5))) + 14,   h_A = 2 ceil(log2(n+5)) + 14,
    t_V = 64 h_e,  F(h) = 2^21 h,  T_V = ceil(log2(n+20)) + 14,  G = n + 40 + T_V.

Translation Tr_c: u -> u + c mod N satisfies Tr_c chi_k = omega^(-k c) chi_k.
A TEST WITH SHIFT c (0 <= c < N) works as follows. Prepare an ancilla in |+>.
Apply Tr_((N - c) mod N) controlled by it, so the |1> branch gets eigenvalue
omega^(k c). Measure the ancilla in X (H then Z) or in Y (S^dagger, H, then Z).
The +-1 outcome has mean cos(2 pi c k/N) or sin(2 pi c k/N). Conditioned on
k, chi_k and every spectator are unchanged and outcomes are independent. A test
at LEVEL j is the test with shift 2^j mod N. Each test costs one controlled
modular addition, O(n) core steps.

### 5.1 RUN(F): level-wise extraction

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

### 5.2 Estimate

k_A = RUN(F(h_A)). Since e^(-h_A) <= 2^(-h_A) <= 2^-14 (n+5)^-2,

    Pr[k_A != k] <= 4 (n+5) 2^-14 (n+5)^-2 <= 2^-12/(n+5) <= 1/(2n).        (5.E)

Cost O(n^2 log n).

### 5.3 Verification

Precomputation. By long division compute rh = floor(k_A 2^G / N), O(n G) = O(n^2)
bit operations, so rh 2^-G is within 2^-G of k_A/N. For i = 0..n+19 let f_i be
the T_V bits of rh in positions G-i-1 down to G-i-T_V (all exist, since
G-i-T_V >= 21). Then f_i 2^-(T_V) is within 2^-(T_V) + 2^(i-G) of frac(2^i k_A/N)
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
  (n+20) 2^-(T_V) + sum_(i <= n+19) 2^(i-G) <= 2^-14 + 2^-20 < 2^-13. This costs
  O(n T_V) = O(n log n) bit operations.
- Score s_r = zX tab_0(xh 2^-(T_V)) + zY tab_1(xh 2^-(T_V)), with tab from Section 4.

ACCEPT iff s_1 + ... + s_(t_V) >= t_V/2.

Lemma 5.1. Conditioned on k and k_A: if k_A = k, verification rejects with
probability at most e^(-h_e); if k_A != k, it accepts with probability at most
e^(-h_e).

Proof. Rounds are i.i.d. given (k, k_A): each uses fresh coins and fresh tests,
and the data register is unchanged. By (4.1) and 2 pi 2^-13 < 1/1300, each table
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

Cost per call: O(n^2) precomputation plus t_V rounds of O(n log n), that is
O(n^2 + n^(3/2) log n) = O(n^2) core steps. Classical scratch O(n log n) bits.

### 5.4 High-confidence extraction and output

If verification accepts, LE outputs k_A. Otherwise it runs k_H = RUN(F(h_e)),
the high-confidence extraction, and outputs k_H, subject to the cap in 5.5.
After the last test of the call, the data register is reset. LE uses no
Fourier transform, no lookup, and no rotation other than H and S, and O(n)
quantum scratch (n data qubits, one ancilla, arithmetic).

### 5.5 Cap on high-confidence runs

Let sn be the least integer >= sqrt n (computed exactly by integer arithmetic) and Cf = ceil(Qcap/sn). A counter
records the number of RUN(F(h_e)) executions. If a call would start the
(Cf+1)-st one, IFCS1310S60 stops, releases everything and outputs 0 (ABORT).

Lemma 5.2. Pr[ABORT] <= 2^-20.

Proof. A call reaches 5.4's high-confidence branch only if k_A != k, or k_A = k
and verification rejects. Conditioned on the entire history before the call
(including k), by (5.E) and Lemma 5.1 this has probability at most
1/(2n) + e^(-h_e) <= 1/n, because the call's tests and coins are fresh. Hence
the indicators of the at most Qcap calls can be coupled with i.i.d. Bernoulli(1/n)
variables that dominate them (compare each indicator with an independent uniform
threshold), and the number of high-confidence runs is stochastically dominated by
X ~ Bin(Qcap, 1/n), with mean EX = Qcap/n. For x > EX the Chernoff bound gives
Pr[X >= x] <= (exp(1) EX/x)^x. With x = Cf >= Qcap/sn >= Qcap/(sqrt n + 1),
exp(1) EX/x <= exp(1) (sqrt n + 1)/n <= exp(1) * 65/4096 < 1/2 for n >= 4096, since
(sqrt n + 1)/n decreases. Also Cf >= 20, because Qcap >= 6144 * 2^hmax >= 6144 (1 + hmax) >= 6144 + 6144 sqrt n/(4 (mu0 + 1)) >= 20 (sqrt n + 1), as hmax > mu >= sqrt n/(4 (mu0 + 1)) and 1536 >= 20 (mu0 + 1) (Section 7, B3 and B5).
So Pr[ABORT] <= 2^-20. QED.

### 5.6 Correctness and cost of LE

Per call, the output differs from k only if (k_A != k and verification accepts)
or (a high-confidence run returns a value other than k). By Lemma 5.1 and the
concentration bound of 5.1 this has probability at most e^(-h_e) + 4(n+5) e^(-h_e) = (4n+21) e^(-h_e),
uniformly in k and in the adaptive schedule. Over at most Qcap calls the
probability that ANY call returns a wrong label is at most
(4n+21) Qcap e^(-h_e) <= 5 * 2^(h_e-14) e^(-h_e) < 2^-11.

Cost. Without its high-confidence branch, a call costs O(n^2 log n) core steps
(5.2 dominates). Each high-confidence run costs O(n^2 h_e), and on EVERY branch
there are at most Cf <= Qcap/sqrt(n) + 1 of them, for O(n^(3/2) h_e) Qcap + O(n^2 h_e)
= O(n^2) Qcap + O(n^(5/2)) core steps in total. So on every branch, all LE calls
together cost O(n^2 log n) Qcap + O(n^(5/2)) core steps.

IDEAL run. The ideal run is IFCS1310S60 in the latent-label model with every LE output
replaced by the latent k and without the cap of 5.5. The actual and ideal runs
can be coupled to coincide unless some LE call returns a wrong label or ABORT
occurs, so every event's probability differs between them by less than
2^-11 + 2^-20. Resource bounds are proved for every ACTUAL branch directly,
because they rest only on caps and fixed allocations.

### 5.7 Reduced ideal law used for every conditioning below

This section is a repair of an inherited filtration ambiguity, not a
new source algorithm. In the IDEAL UNCAPPED analysis every LE output is
the latent label, and LE's internal accept/reject/fallback outcomes feed
no retained decision. Conditional on the latent k the untouched first
qubit and the data register are a product (Section3); LE acts only on
the data register and fresh ancillas. Marginalizing its entire internal
transcript leaves the first-qubit state unchanged. Thus for correctness
and source-count analysis use the following EQUIVALENT reduced ideal law.
Do not condition on the marginalized transcript, its timing/branch,
or any unused high-label arithmetic or table contents.

For the odd-part supplier, fresh independent k uniform on Z/NZ is
accepted iff k<2^d. The rejection count before an acceptance is geometric
with success2^d/N>1/2, independent of the accepted k, which is uniform on
[0,2^d). Discarded copies and their unused information can be integrated
out; the acquisition count is retained. For the2-adic supplier, kk=k mod
2^wd is uniform because2^wd dividesN; unused quotient and LE outcomes
are integrated out. First-qubit states are exactly the phase states
stated in Sections9-10. Copies are fresh and independent of every past
completed attempt and any retained sibling. These facts follow by the
product latent-label identity and elementary conditioning on acceptance.

After these erasures the controller's tree construction depends on
accepted labels only through the bits consumed by completed merge
levels and their prescribed measurement outcomes. LE accept/reject
verdicts in Section5 are distinct from the source range test k<2^d.
In the ideal law the latter retains only acceptance/counts and restricts
the accepted label to its full uniform interval; it supplies no further
information about bits inside that interval. Every merge outcome,
FAIL and retry rule still has its original instrument. Neither logical
algorithm nor actual source cap is changed. The actual/ideal coupling
and LE-error/fallback budget of Section5.6 are unchanged; resource
bounds concern actual branches with literal caps independently.

External histories may contain full transcripts of earlier completed
calls on disjoint copies. Conditional on such a history the next fresh
source labels have the same product law. Current-call LE transcripts
must be marginalized before claiming the low/high factorization; they
are NOT added to that conditioning by the phrase 'all previous steps'.

## 6. Phase vectors, the linear merge and the four-input merge MERGE4I

A PHASE VECTOR of length 2^lam is a lam-qubit index register with a classical
label table lab[0..2^lam). In the ideal run its state is
2^(-lam/2) sum_x exp(2 pi i lab[x] th) |x>, up to a global phase, for a fixed
real th. Labels are nonnegative integers. The vector is COLLIMATED TO p if all
lab[x] are congruent modulo 2^p.

STORAGE. A table collimated to p is stored as its common residue
c = lab[0] mod 2^p (one p-bit number) and the HIGH PARTS hi[x] = floor(lab[x]/2^p),
so lab[x] = c + 2^p hi[x]. Each high part is stored in a fixed field of w bits,
where w is any bound with lab[x] < 2^(p+w) for all x (Section 7 fixes w per
level). Every quantity used below is computed from (c, hi) exactly; lab[x] is
never written out in full except in LEAF, where p = 0 and hi = lab.

### 6.1 Lookups

LOOKUP(tab), for a classical table of E rows with w-bit entries, XORs tab[x]
into a clean w-bit register, controlled by a lam-qubit index x. For each row
x0 = 0..E-1 it computes the flag [x = x0] with a Toffoli chain on O(lam)
scratch, applies CNOTs from the flag to the output bits where tab[x0] has a 1,
and uncomputes the chain. Indices outside [0,E) give output 0. The circuit is
its own inverse, has O(E (lam + w)) gates and O(lam + w) qubits, and is
generated by reading each table bit once.

### 6.2 MERGE(X1, X2; p, b, lam')

Precondition: X1 and X2 are phase vectors from disjoint sets of copies, both of
length 2^lam, collimated to p, with index registers x and y and tables al and be.
Both are stored as in STORAGE: al[x] = cA + 2^p hA[x] and be[y] = cB + 2^p hB[y],
with 0 <= cA, cB < 2^p. Let car = floor((cA + cB)/2^p) in {0,1}.
Define residues aa[x] = hA[x] mod 2^b and bb[y] = hB[y] mod 2^b.
Then bits p..p+b-1 of al[x] + be[y] equal (aa[x] + bb[y] + car) mod 2^b.

1. LOOKUP aa into a fresh b-bit register Ru and bb into Rv. Add Ru + Rv + car
   (mod 2^b) cleanly into a fresh register Rz, and clear Ru and Rv by repeating
   both lookups. Measure Rz, obtaining e, and reset Rz from that known value.
2. Classical. Let S_e = {(x,y) : aa[x] + bb[y] + car = e mod 2^b} and sz = |S_e|.
   - Merge-sort the indices y by the key (bb[y], y) into order[]; pos[y] is the
     position of y.
   - For each x the partners y form one contiguous run of order[], namely the
     residue class cls[x] = (e - car - aa[x]) mod 2^b. Find its start lo[x] and
     length cnt[x] by binary search.
   - Put off[x] = sum_(x' < x) cnt[x'] and rank(x,y) = off[x] + pos[y] - lo[x].
     The rank is a bijection from S_e onto [0, sz).
   - If sz < 2^lam', declare FAIL.
3. Let R have 2 lam + 1 bits. LOOKUP pos into Rp and Dx[x] = (off[x] - lo[x]) mod 2^(2lam+1)
   into Rd. Add Rp + Rd (mod 2^(2lam+1)) cleanly into a fresh R, and clear Rp
   and Rd by repeating the lookups. On S_e, R = rank(x,y).
4. Measure bl = floor(R / 2^lam'), the bits of R above the low lam'. If
   (bl+1) 2^lam' > sz, declare FAIL.
5. Classical. For v in [0, 2^lam'), find the unique (x_v, y_v) with rank
   bl 2^lam' + v, in one scan over x with running offsets. Apply LOOKUP
   v -> (x_v, y_v) on the low lam' bits of R, XORing into the registers x and y,
   which become |0>. Reset the high bits of R from their known value bl.
6. Output the low lam' bits of R as the index register, with table
   lab[v] = al[x_v] + be[y_v], stored as in STORAGE with p+b in place of p:
   put sv = hA[x_v] + hB[y_v] + car, which is congruent to e modulo 2^b. Then
   lab[v] = (cA + cB - car 2^p + 2^p e) + 2^(p+b) floor(sv/2^b). The first term
   c' = cA + cB - car 2^p + 2^p e lies in [0, 2^(p+b)) and does not depend on v.
   So the stored output is the common residue c' and the high parts
   hi'[v] = floor(sv/2^b).

On FAIL, both inputs are reset and released and never reused. All registers
have fixed widths, so memory is allocated deterministically.

Correctness (ideal run). Before step 1 the state is X1 (x) X2: equal
magnitudes over all pairs (x,y), with phases 2 pi (al[x] + be[y]) th. Steps 1
and 3 compute functions of (x,y) into clean registers and measure them. So
after step 4 the state is the equal-magnitude superposition over the 2^lam'
pairs of block bl, with their original phases. Step 5 maps (x_v, y_v) to v
bijectively. The output is therefore a phase vector with table lab. Every
label is congruent to cA + cB + 2^p ((e - car) mod 2^b) modulo 2^(p+b), so the
output is collimated to p+b.

Lemma 6.1 (distribution-free failure). For ANY input tables collimated to p,
the measurement law in steps 1 and 4 depends only on aa, bb and car (that is,
on label bits below p+b), and Pr[FAIL] <= 2^(b + lam' - 2 lam).

Proof. Each measurement is a computational-basis measurement of a function of
(x,y) on an equal-magnitude superposition. Its outcome probabilities are
therefore ratios of counts, independent of the phases. The outcome e has
probability sz_e / 2^(2lam). Given e, the measured rank is uniform on [0, sz_e).
So FAIL has conditional probability rem_e / sz_e, where rem_e = sz_e mod 2^lam'
(this also covers sz_e < 2^lam'). Hence
Pr[FAIL] = sum_e rem_e / 2^(2lam) <= 2^b (2^lam' - 1) / 2^(2lam). QED.

Cost. Write L = 2^lam and L' = 2^lam'. A merge makes eight lookup passes of L
rows and one of L' rows, each with O(lam + b) bit fields. Classically it
performs O(L lam) comparisons of (b + lam)-bit keys, O(L) binary searches of
O(lam) steps on b-bit keys, and O(L') additions of high parts of at most
O(n) bits. With lam, b = O(sqrt n) (Section 7), this is O(n (L + L')) core steps.
The quantum scratch is O(sqrt n) beyond the two index registers. The classical
scratch (order, pos, lo, cnt, off, Dx, aa, bb and the inverse block table) is
O((L + L') sqrt n) bits, and the output table is L' fields of w' bits plus
p + b bits for c'.

### 6.3 MERGE4I(X1, X2, X3, X4; p, r, r', lam', l)

Precondition: X1..X4 are phase vectors from pairwise disjoint sets of copies, of length L = 2^lam, collimated
to p, stored as lab_t[x] = c_t + 2^p h_t[x] (0 <= c_t < 2^p), index registers x1..x4; lam >= kappa + 2,
lam + 1 <= l <= 2 lam, r = 2 lam - l, lam' >= 1, r' = 2l - lam' - kappa >= 1 (kappa >= 1 from Section 7). Put
b = r + r', mX = 2^l = L^2/2^r, mu4 = 2^(lam' + kappa), Cp = 8 mu4 + 1; so 2r + r' = 4 lam - lam' - kappa. Residues:
rho_t = h_t mod 2^r (window W0: bits p..p+r-1) and sg_t = floor(h_t/2^r) mod 2^r' (window W1: bits p+r..p+b-1). Carries: cAB = floor((c_1 + c_2)/2^p),
cCD = floor((c_3 + c_4)/2^p), dl = floor(((c_1 + c_2) mod 2^p + (c_3 + c_4) mod 2^p)/2^p), and
car = floor((c_1 + c_2 + c_3 + c_4)/2^p) = cAB + cCD + dl. For a pair (x1, x2) let
vX = (rho_1 + rho_2 + cAB) mod 2^r (bits p..p+r-1 of lab_1 + lab_2), gX = floor((rho_1 + rho_2 + cAB)/2^r) in
{0,1}, and the key kX = sg_1 + sg_2 + gX in [0, 2^(r'+1)); define vY, gY, kY for (x3, x4) with cCD.

Window identity. With h_t = rho_t + 2^r sg_t + 2^b u_t and S = lab_1 + lab_2 + lab_3 + lab_4 for a tuple,

    floor(S/2^p) = car + h_1 + h_2 + h_3 + h_4 = (vX + vY + dl) + 2^r (kX + kY) + 2^b (u_1 + u_2 + u_3 + u_4),   (6.4)

as cAB + rho_1 + rho_2 = vX + 2^r gX and cCD + rho_3 + rho_4 = vY + 2^r gY. So bits p..p+r-1 of S are
(vX + vY + dl) mod 2^r, and bits p+r..p+b-1 are (kX + kY + c0) mod 2^r', c0 = floor((vX + vY + dl)/2^r) in {0,1}.

1. LOOKUP rho_1, rho_2 into fresh registers, add them and cAB mod 2^r cleanly into a fresh Rz, clear the two by
   repeating the lookups, measure Rz (outcome v), reset it. Same on x3, x4 with cCD (outcome v2). Let the pair fibers
   X_v and Y_v2 be the sets of pairs (x1, x2) with vX = v and (x3, x4) with vY = v2.
2. Cutoff (classical). Merge-sort the x2 by (rho_2, x2) and the x4 by (rho_4, x4). For each x1 the x2 with
   rho_2 = (v - cAB - rho_1[x1]) mod 2^r form one contiguous run, found by binary search; the run lengths sum to
   |X_v|, and likewise for |Y_v2|. If |X_v| > 2 mX or |Y_v2| > 2 mX, declare FAIL.
3. LOOKUP h_t mod 2^b (t = 1..4), add them and car mod 2^b cleanly into a fresh Rw, clear the lookups, CNOT bits
   r..b-1 of Rw into a fresh r'-bit Ru, and uncompute Rw. Ru holds bits p+r..p+b-1 of S. Measure Ru (outcome v'),
   reset it. Let Z = {tuples of X_v x Y_v2 with bits p+r..p+b-1 of S equal to v'}, sz = |Z|.
4. Listing (classical). Re-sort the x2 by (rho_2, sg_2, x2) and the x4 by (rho_4, sg_4, x4): the runs are the
   same sets (their ends found again by binary search on rho_2), with sg nondecreasing along each, and gX is constant on the run of x1. STREAM X, a class-restricted Schroeppel-Shamir stream: a min-heap holds, for
   each x1 with a nonempty run, the key kX of x1 with its next unread run position; pop the minimum, output that
   pair, push the next position of that run. As kX is nondecreasing along runs, STREAM X outputs X_v once each in
   nondecreasing kX. STREAM Y outputs Y_v2 in nonincreasing kY likewise (runs read backwards, max-heap). Each heap
   holds at most L entries of O(lam + r') bits. Neither X_v nor Y_v2 is stored as a table: the stored data are the
   sort orders, runs, heaps, Buf (at most Cp pairs of one run) and Tl.
   Put c0 = floor((v + v2 + dl)/2^r) and tg = ((v' - c0) mod 2^r') + g 2^r' (g = 0..3). As
   0 <= kX + kY <= 2^(r'+2) - 2, by (6.4) a tuple of X_v x Y_v2 is in Z iff kX + kY = tg for exactly one g. For
   g = 0..3 in order, restart both streams and scan with heads hx, hy: if kX(hx) + kY(hy) < tg read the next X
   pair (rule 1); if > tg read the next Y pair (rule 2); if = tg (rule 3) read the whole run of Y pairs with key
   kY(hy), keeping the first min(run length, Cp) of them in a buffer Buf, then the whole run of X pairs with key
   kX(hx), appending to a list Tl the 4-tuple of each X pair read with each Buf entry. Stop the listing as soon
   as |Tl| = Cp; a scan ends when a stream is exhausted.
   Claim: if sz <= Cp, Tl lists Z exactly once each; otherwise Tl lists exactly Cp distinct elements of Z.
   Proof. Appended tuples have kX + kY = tg, so they lie in Z; they are distinct, as a scan reads each pair once and
   a tuple has only one g. Let (xi, eta) be in Z with
   kX(xi) + kY(eta) = tg, in a scan without stop. While eta is unread, kY(eta) <= kY(hy), so rule 1 cannot pass
   over xi; while xi is unread, kX(xi) >= kX(hx), so rule 2 cannot pass over eta. So the first step reading xi or
   eta is a rule 3 step with both unread before it; there kX(xi) >= kX(hx), kY(eta) <= kY(hy) and equal sums give
   kX(xi) = kX(hx) and kY(eta) = kY(hy), so both lie in the runs read whole, and (xi, eta) is appended unless Buf
   cut its Y run. Buf cuts a run only if it has more than Cp pairs; its X run is nonempty, so the first X pair
   read fills Tl to Cp, and then sz > Cp. QED. Let tl = |Tl| = min(sz, Cp).
   Before the measurement of v', no branch or FAIL decision of this merge depends on label bits at positions
   >= p + r: the only one, in step 2, depends on bits below p + r.
5-8. (MW4's steps 3-6.) (5) R has ceil(log2(Cp + 1)) bits and Rf one qubit, both 0. For each row rho of Tl compute
   [(x1,x2,x3,x4) = Tl[rho]] with a Toffoli chain on O(lam) scratch, CNOT it into Rf and onto the bits of R where
   rho has a 1, and uncompute; rows being distinct, R = rho and Rf = 1 on Tl, R = Rf = 0 elsewhere. Measure Rf; if
   Rf = 0 declare FAIL. (6) Measure bl = floor(R/2^lam');
   if (bl + 1) 2^lam' > tl declare FAIL. (7) For y in [0, 2^lam'), LOOKUP y -> Tl[bl 2^lam' + y] on the low lam'
   bits of R, XORing into x1..x4, which become |0>; reset them, Rf and the high bits of R from known values.
   (8) Output the low lam' bits of R as the index register, with lab[y] the sum of the four input labels of
   Tl[bl 2^lam' + y], stored as in STORAGE with p+b in place of p: by (6.4), on Z the integer
   car + h_1 + ... + h_4 is congruent to E = ((v + v2 + dl) mod 2^r) + 2^r v' modulo 2^b, so store
   c' = c_1 + c_2 + c_3 + c_4 - car 2^p + 2^p E in [0, 2^(p+b)) and hi'[y] = floor((car + h_1 + ... + h_4)/2^b).

On FAIL all inputs and registers are reset and released, and the inputs are never reused. All registers and
arrays have fixed sizes, set by L, r, r', lam' and kappa.

Correctness (ideal run). Before step 1 the state is the product of the inputs: equal magnitudes over the L^4
tuples, with phases 2 pi (sum of labels) th. Steps 1, 3, 5 and 6 compute functions of the tuple into clean
registers and measure them; steps 2 and 4 act on nothing in this state. So after step 6 the state is the
equal-magnitude superposition over the 2^lam' tuples of block bl with their original phases, and step 7 maps
each to its y bijectively. The output is a phase vector with table lab, collimated to p+b, since every label is
congruent to c' modulo 2^(p+b).

Lemma 6.3 (failure identity). For ANY input tables collimated to p, the laws of the measurements of steps 1, 3,
5 and 6 depend only on label bits below p+b, and with sz = sz(v,v2,v') and tl = min(sz, Cp),

    Pr[FAIL] = sum_((v,v2) cut) |X_v| |Y_v2| / L^4 + sum_((v,v2) not cut) sum_(v') [ (sz - tl) + (tl mod 2^lam') ] / L^4,

where "(v,v2) cut" means that step 2 declares FAIL. The terms (tl mod 2^lam') sum to less than
2^(2r + r' + lam')/L^4 = 2^(-kappa).

Proof. Each measurement is a computational-basis measurement of a function of the tuple on an equal-magnitude
superposition, so its law is a ratio of counts, independent of phases. Step 1's two measurements act on
disjoint registers, so (v, v2) has probability |X_v| |Y_v2|/L^4; given (v, v2) not cut, v' has probability
sz/(|X_v| |Y_v2|); given v', Rf = 0 has probability (sz - tl)/sz; given Rf = 1, R is uniform on [0, tl) and step
6 fails with probability (tl mod 2^lam')/tl. Multiplying and summing gives the identity. There are 2^(2r + r')
triples (v, v2, v'), and tl mod 2^lam' < 2^lam'. QED.

Cost on every branch. Steps 1, 3: 24 lookup passes of L rows with O(lam + b)-bit fields. Steps 2, 4: O(L lam)
comparisons of O(lam + b)-bit keys and O(L) binary searches; after step 2 each of the four scans reads at most
|X_v| + |Y_v2| <= 4 mX pairs, each a heap operation of O(lam) comparisons of O(lam + r')-bit keys, with at most one
Buf write per Y pair and at most Cp appends of O(lam) bits. Steps 5-8: one pass of tl <= Cp rows with O(lam)
control bits, one lookup pass of 2^lam' rows, 2^lam' additions of O(n)-bit high parts. Total
O((L + mX) lam (lam + b) + Cp lam + 2^lam' (lam + n)) core steps; quantum scratch O(lam + b) beyond the index
registers; classical scratch (sort orders, runs, heaps, Buf, Tl, block table) O((L + Cp)(lam + b)) bits, fixed.

## 7. The tree TREE_D

Throughout, n >= 4096 (the main branch of Section 11), rho := sqrt n >= 64, and mu0 = 5999/10000; v=bitlength(n), with no constant d0.
Input: a supplier of LEAF QUBITS, each a positive qubit with a known label uniform on [0, 2^D),
D >= 2, independently. Put B = D - 1 <= n, the number of bits to collimate. Global parameters, functions of n only,
computed by exact integer arithmetic:

    w = least integer with 100000000 w^2 >= 35988001 n, i.e. ceil(mu0 sqrt n),   v = bitlength(n),
    nu = v,   gamma = v - nu,   Astar = (w - nu)(w + nu - 1)/2,   Jw = ceil((w - gamma)/2),
    G = least integer G >= 0 with S*(G) >= n, where S*(J) = Astar + sum_(j < J) min(2w + 2j + gamma + 3, 3w + 3),
    mu = w - nu + G + 1,   kappa = ceil(log2 mu) + 3,   Lam = kappa + 1 + w.

So mu0 rho <= w < mu0 rho + 1, log2n <= v <= log2n+1 and 8 mu <= 2^kappa < 16 mu. Case B: nu = v < w (B1), gamma = 0. In Sections 7, 11, 13 and 14, G, Jw, rho, mu0, w, v, nu and gamma are defined here (G
is not the precision G of Section 5.3, rho not rho_t or the row index rho of Section 6.3, w not the STORAGE field width,
which is w_i below, and v not the outcome v or fibers X_v of Sections 6.3 and 8.1 or the loop indices v of Sections 3
and 6.2); the J of Q*, Lemma 11.1 and Section 13 is the stage count of Section 9, and in Section 7 J and j are indices.

Levels i = 0, ..., mu - 1 have arity f_i, input exponent lam_i, height h_i (a node of level i has 2^(h_i) leaf
vectors below it) and capacities bmax_i (non-root) and rootcap_i (as the root, output exponent 1):

    Phase A, 0 <= i <= w-nu-1:            f_i = 2, lam_i = kappa + 1 + nu + i, h_i = i, bmax_i = nu + i,
                                          rootcap_i = kappa + 2 nu + 2i + 1;
    Phase I, i = w - nu + j, 0 <= j <= G:  f_i = 4, lam_i = Lam, h_i = w - nu + 2j,
                                          l_i = min(Lam + 1 + gamma + 2j, 2 Lam) = min(kappa + 2 + v + h_i, 2 Lam),
                                          r_i = 2 Lam - l_i, bmax_i = Lam + l_i - kappa
                                          = min(2w + 2j + gamma + kappa + 3, 3w + 2 kappa + 3), rootcap_i = Lam + bmax_i - 1.

These are substitutions as in IFC1 (binary bmax_i = 2 lam_i - lam_(i+1) - kappa with lam_(i+1) = kappa + 2 + nu + i,
which is Lam at i = w - nu - 1, and rootcap_i = 2 lam_i - 1 - kappa; four-input bmax_i = r_i + (2 l_i - Lam - kappa) and
rootcap_i = r_i + (2 l_i - 1 - kappa)). So Lam + 1 <= l_i <= 2 Lam. A four-input level with 2j >= kappa + w - gamma has l_i = 2 Lam and r_i = 0; we call it SATURATED. The other four-input
levels have r_i >= 1. Every capacity is at most 4 Lam, as rootcap_i <= Lam + 3w + 2 kappa + 2.

A tree with m levels (1 <= m <= mu) has ROOT level m-1, lam_m := 1, capacity Sum(m) = sum_(i < m-1) bmax_i +
rootcap_(m-1) and output height h_m = m (m <= w - nu) or 2m - (w - nu) (m >= w - nu); m is the least m >= 1 with
Sum(m) >= B. Phase A has total capacity sum_(i < w-nu) bmax_i = Astar. By substitution, Sum(m+1) - Sum(m) is
nu + m + 1 for 1 <= m < w - nu and bmax_m for w - nu <= m < mu, so Sum is increasing. As kappa >= 0, for
i = w - nu + j,

    bmax_i >= min(2w + 2j + gamma + 3, 3w + 3),                                                      (7.0)

so Sum(w - nu + 1 + J) = Astar + sum_(j < J) bmax_(w-nu+j) + rootcap_(w-nu+J) >= S*(J) for 0 <= J <= G.

Lemma 7.0 (capacity and logarithmic-boost height). Put
H00=5mu0/6+2/(3mu0)=38662667/23996000<1612/1000<13/8.
For the literal schedule and everyrho=sqrt n>=64:
(a) Sum(mu)>=S*(G)>=n>=B,m<=mu,h_m<=hmax=w-v+2G+2;
(b) hmax<H00rho-v+7, andhmax+v<H00rho+7.

Proof. (a) follows from(7.0),definitionG and monotoneSum,h_m.
Forj<Jw,2j<=2Jw-2<w and termsS* equal2w+2j+3;
forj>=Jw terms equal3w+3. Therefore
S*(Jw)=Astar+Jw(2w+2+Jw),w<=2Jw<=w+1.
IfG<=Jw,hmax<=2w-v+3<2mu0rho-v+5<=H00rho-v+5,
sinceH00-2mu0=(4-7mu0²)/(6mu0)>0.
IfG>=Jw+1,minimality gives
S*(G-1)=S*(Jw)+(G-1-Jw)(3w+3)<n,
soG-1-Jw<(n-S*(Jw))/(3w) and
hmax<2w-v+5+2(n-S*(Jw))/(3w).
HereAstar=(w²-v²-w+v)/2,Jw>=w/2, hence
S*(Jw)>=Astar+(w/2)(5w/2+2), and
2(n-S*(Jw))<2n-7w²/2+v². Thus
hmax<Fh(w,v)+5,Fh(y,t)=5y/6-t+(2n+t²)/(3y).
ByB2,5w²<4n+2v²,soFh is decreasing in y for mu0rho<=y<=w.
ConsequentlyFh(w,v)<=H00rho-v+v²/(3mu0rho).
Writeu=2log2rho+1,so v<=u. Forrho>=64,u²/rho decreases:
its derivative has sign4/ln2-u<6-13<0,using1/ln2<3/2.
Thusv²/(3mu0rho)<=169/(3mu0*64)<2.
Combining giveshmax<H00rho-v+7. Every stated condition is
proved below directly at this same main threshold. QED.

Window r = 0. At a saturated level Section 6.3 runs as written: W0 is empty, step 1 measures empty registers
(6.3's outcomes v, v2 are 0), X_v and Y_v2 are all L^2 = 2^l = mX pairs and step 2 never cuts; the rest holds verbatim (gX = cAB,
gY = cCD; 2^r' triples in Lemma 6.3). In Lemma 8.2 the g_j are 0, Hp' = Hp, and Stage 1's bound holds as the indicator
[|X_v| > 2 mX] is 0 (likewise for Y_v2), so the pairwise-independence step is used only with s = r >= 1 (Stage 1) and
s = r' >= w + 3 (Stage 2); Lemma 8.2 holds as stated, as in our IFC34.

Size facts for n>=4096,rho>=64. Writeu=2log2rho+1>=v.
B1. v+1<=u+1<mu0rho: at64,14<38.3936, and derivative
mu0-2/(rho ln2)>0 thereafter. Thusv+1<w and PhaseA nonempty.
B2. 5w²<5(mu0rho+1)²<=4rho²<=4n+2v².
The positive quadratic difference(4-5mu0²)rho²-10mu0rho-5
and its derivative are positive at64 and grow thereafter.
Also2v<=2u<3mu0rho (base26<115.1808); derivative
3mu0-4/(rho ln2)>0, and7mu0²<4. These prove7.0's premises.
B3. mu<hmax<H00rho-v+7<H00rho+7<2rho, since
H00<13/8 and(2-13/8)*64=24>7. Fields are atmost3n bits.
B4. kappa<log2mu+4<=log2rho+5<=rho/2, true at64 and
monotone thereafter. Also2^kappa<16mu<=32rho,kappa>=4.
B5. Lam=kappa+1+w<rho/2+mu0rho+2<=(mu0+1)rho.
Alllam_i,l_i,b_i=O(sqrt n), andn<=Sum(mu)<=4muLam
impliesmu>=rho/(4(mu0+1)).
B6. Astar=(w²-w-v²+v)/2>=(mu0²rho²-mu0rho-u²)/2.
This exceeds(3mu0+1)rho+6 at64 by direct rational arithmetic
(u64=13). Its difference has derivative
mu0²rho-mu0/2-2u/(rho ln2)-(3mu0+1)>0 at64 and thereafter:
mu0²rho increases andu/rho decreases. ByB4,
3w+2kappa+3<(3mu0+1)rho+6<=Astar. The full-level/root lemma follows.
B7. 2^v>=n>=2rho>=log2n. All exact source guards requiring
logn<=2^v remain. No new runtime threshold is introduced.

Allocation. Allocate b_(m-1), b_(m-2), ..., b_0 in that order greedily, with b_(m-1) = min(rootcap_(m-1), B) and then
b_i = min(bmax_i, B - already allocated). Then sum_i b_i = B, and some low levels may get smaller values or 0. Put
p_0 = 0 and p_(i+1) = p_i + b_i, so p_m = B. Let nq_D = 2^(h_m) (kappa + 1 + nu) be the number of leaf qubits per tree.

Lemma 7.1 (four-input levels are full). In any tree with m >= w - nu + 1, every level i >= w - nu gets its full
capacity: b_i = bmax_i for w - nu <= i < m-1, and b_(m-1) = rootcap_(m-1).

Proof. Here m >= 2, so Sum(m-1) < B by minimality, and the deficit Sum(m) - B is below Sum(m) - Sum(m-1) =
bmax_(m-1) <= 3w + 2 kappa + 3 <= Astar (B6). So the levels i >= w - nu have total capacity Sum(m) - Astar < B, and the
greedy allocation, serving levels from the top, gives each its full capacity before reaching Phase A. QED.

MERGE4I parameters. At a four-input level i put l = l_i, r = r_i and r' = b_i - r_i, which by Lemma 7.1 equals
2 l_i - lam_(i+1) - kappa with lam_(i+1) = Lam below the root and lam_m = 1. The preconditions of Section 6.3 hold:
lam = Lam >= kappa + 2, Lam + 1 <= l <= 2 Lam, r = 2 Lam - l, lam' >= 1 and r' >= 2(Lam + 1) - Lam - kappa = w + 3;
also kappa + 3 <= l <= kappa + 2 + v + h_i and p + b <= B.

Failure budgets. For a binary level, b_i + lam_(i+1) - 2 lam_i <= -kappa by substitution (nu + i + (kappa + 2 + nu + i) -
2(kappa + 1 + nu + i) = -kappa below the root, rootcap_i + 1 - 2 lam_i = -kappa at the root), so Lemma 6.1 gives
Pr[FAIL] <= 2^-kappa for any input tables. Four-input levels, saturated or not, are bounded by Lemma 8.2.

LEAF: take kappa + 1 + nu leaf qubits as the index register (bit j = qubit j). Build the table incrementally,
lab[0] = 0 and lab[x + 2^j] = lab[x] + k_j for x < 2^j: one addition per entry. The table has length 2^(lam_0),
lam_0 = kappa + 1 + nu <= Lam, is collimated to p_0 = 0, and in the ideal run is exactly the tensor product state.

Field widths. A level-i label is a sum of at most 2^(h_i) (kappa + 1 + nu) leaf labels below 2^(B+1), so it is below
2^(B+1+h_i+gw), gw = ceil(log2(kappa + 1 + nu)). Level-i tables are collimated to p_i and stored with
w_i = B + 1 + h_i + gw - p_i bits per high part, at most 3n, as h_i <= 2 rho (B3) and gw <= log2(2 rho) + 1.

VEC(i): if i = 0 return LEAF. Otherwise repeat:
- build the f_(i-1) inputs, each by VEC(i-1);
- out = MERGE(X1, X2; p_(i-1), b_(i-1), lam_i) if f_(i-1) = 2, and
  out = MERGE4I(X1, X2, X3, X4; p_(i-1), r_(i-1), b_(i-1) - r_(i-1), lam_i, l_(i-1)) if f_(i-1) = 4
  (lam_i means lam_m = 1 when i = m);
- if out != FAIL, return out.

TREE_D returns VEC(m), a one-qubit phase vector with labels lab[0] and lab[1],
congruent modulo 2^B. Its ideal state is, up to global phase,
(|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2 with the known integer

    W = (lab[1] - lab[0]) / 2^B = hi[1] - hi[0],                              (7.2)

because the root table is collimated to p_m = B. Each label is a sum of at most nq_D leaf labels below 2^(B+1),
so |W| < 2 nq_D. Depth-first evaluation holds at most f_i - 1 <= 3 finished siblings per level.

## 8. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and
tau_j in {0,1}. Since k_j is uniform on [0, 2^(B+1)), low_j and tau_j are
independent and tau_j is a fair bit. Let Gt be the sigma-field generated by:
- all low_j of the tree's leaves, including those of discarded attempts;
- all measurement outcomes (e, bl, v, v2, v', Rf) of its merges, and the counts and lists of Section 6.3;
- all tree-construction decisions of the controller (merge parameters, FAIL
  and retry decisions, leaf acceptance tests and which copies are used).
Gt does NOT include LE's internal coins, test outcomes, accept/reject verdicts or
fallback decisions (Section 5). In the ideal run these feed no decision: every LE
output is replaced by the latent k and there is no fallback cap. Given k, they are
independent of everything else, so they are averaged out and never conditioned on.

Lemma 8.1. In the ideal run, conditional on Gt and on all other independent
randomness (other copies, controller coins, earlier root outcomes), the top
bits tau_j of the leaves of the returned root are i.i.d. fair.

Proof, by induction over the controller's steps. Every tree-construction decision, residue,
sort key, count, list, rank and block partition uses only label bits below position B,
since Sections 6.2 and 6.3 read bits p..p+b-1 with p + b <= B, together with index
order. Bits below B of a sum of leaf labels depend only on the low_j: adding
multiples of 2^B does not change them. By Lemmas 6.1 and 6.3, each measurement's
conditional law, given the labels and the earlier outcomes, is a function of
the low_j and the earlier outcomes only. Inductively, the joint law of
(all tau, all low, all outcomes and decisions) factorizes as
law(tau) x law(low) x law(outcomes and decisions | low). Retries use fresh
copies, whose labels enter the same factorization. QED.

Let x0 and x1 be the leaf-incidence vectors of the two root entries. Distinct
indices at a node correspond to distinct incidence vectors: this holds at
leaves, is preserved by concatenating disjoint coordinate sets, and
re-indexing is a bijection. So hd = |x0 xor x1| >= 1. From (7.2),

    W = cst + sum_(j in Sp) tau_j - sum_(j in Sm) tau_j,                        (8.1)

where cst = (sum_j low_j (x1_j - x0_j)) / 2^B is a Gt-measurable integer, and Sp and
Sm are disjoint Gt-measurable sets with |Sp| + |Sm| = hd. A fair bit tau has
E exp(2 pi i phi tau) = e^(i pi phi) cos(pi phi). Hence, for every real phi,

    | E[ exp(2 pi i phi W) | Gt ] | = |cos(pi phi)|^hd <= |cos(pi phi)|,       (8.2)

and, with phi = 1/2, Pr[W odd | Gt] = 1/2.                                     (8.3)

### 8.1 Mid-tree factorization and the two-stage fiber moments of MERGE4I

Lemma 8.2. In the ideal run, consider a MERGE4I attempt at level i, with p = p_i, lam = Lam, l = l_i, r = r_i,
r' = b_i - r_i and lam' = lam_(i+1) (or 1 at the root). Define Hp precisely in the reduced ideal law of Section5.7.
First condition on the full external history BEFORE starting construction
of these four fresh input vectors, including every earlier completed
attempt at this same parent height. All those copies are disjoint from
this construction. Within construction of these four inputs, Hp contains:
(1) the identities and bits BELOW p of every accepted leaf label used by
any lower-level attempt, including discarded attempts;
(2) source acceptance/rejection COUNTS and the chosen public parameters;
(3) lower-level merge outcomes, logical row/index lists and incidence
sets, FAIL/retry/return decisions and stopping/selection of the four
returned inputs. Every such merge consumes positions strictly below p.
Hp DOES NOT contain ANY internal LE coin/test/verification/fallback
transcript of these constructions, any accepted-label bit at or above p,
any higher input-table value/arithmetic scratch, or any physical-only
bank helper outcome. Lower-bit arrays/lists are included; full label
tables are expressly excluded. The range of accepted labels is the
complete uniform[0,2^D) interval supplied above. Its acceptance flag
and acquisition count give no information about its inner label bits.
The precise factorization and random-stopping argument are below.
Then Pr[FAIL | Hp] <= 6 * 2^(-l) + 2^(-kappa - lam') + 2^(-kappa) < 2^(2 - kappa).

Proof. Let Lv be the set of leaves of the four inputs, a union of four pairwise disjoint sets. For j in Lv write
k_j = lo_j + 2^p g_j + 2^(p+r) g'_j + 2^(p+b) u_j with 0 <= lo_j < 2^p, 0 <= g_j < 2^r, 0 <= g'_j < 2^r'. This is
possible as p + b <= B < D, and k_j uniform makes lo_j, g_j, g'_j, u_j independent and uniform.

Factorization, with random stopping. Fix the external history E above.
Generate an infinite sequence of fresh independent uniform accepted
D-bit labels, with independent odd-supplier geometric rejection counts
(or one acquisition each in the2-adic case). Split each accepted label
into its low p bits and its remaining D-p bits. On any FINITE
construction trace, every lower-level law, sort key, residue, count,
rank, list, block and decision is a function of these low bits and its
merge outcomes only. Indeed p'+b'<=p for each lower-level merge;
Lemmas6.1 and6.3 show that the measurement probabilities depend only
on those bits and earlier outcomes, even though phase states contain
higher bits. Output high label values are computed but do not determine
selection/ties/abort below this level; logical index order breaks ties.
Cleanup/release outcomes obey the same rule: lower merge circuits are
computational-basis permutations followed by Z measurements on a
uniform-magnitude phase vector. Conditional support/counts determine
all such Z probabilities, including sequential release; high phases
cannot affect them. Label-high arithmetic is deterministic classical
scratch and is marginalized, not conditioned on as an extra trace.
LE transcripts have ALREADY been integrated out under Section5.7.

Induction over the finite trace therefore gives the joint kernel
 P(low,high,counts,trace | E)
 =P_product_uniform(high)*P(low,counts,trace | E).
For a random finite trace, apply this identity on each fixed acquisition
length and trace cylinder and take the countable disjoint union. The
construction returns almost surely: this follows by induction on height
from the positive return probability established at lower heights
(base LEAF has finite geometric acquisitions; binary Lemma6.1 and the
present four-input bound at each completed induction step are positive).
Equivalently apply the finite identity before each truncated length
and then monotone limits; no unproved conditioning on termination is
needed. The selected four leaf-incidence sets are functions of the
low/count/merge trace, so selecting their random disjoint coordinates
preserves independent uniform unexamined blocks.

Consequently, conditional on Hp, the(g_j,g'_j)for j in Lv are i.i.d.
uniform on[0,2^r) x[0,2^r'). Hp'=sigma(Hp,g_j:j in Lv) leaves the g'_j
i.i.d. uniform. Each pair/tuple incidence set is Hp-measurable; distinct
pairs/tuples have distinct incidence sets by concatenation/reindexing,
so at most one in each family has empty incidence. No claim is made
conditional on the discarded LE transcript. An all-plus LE transcript
can force k=0 and would INVALIDATE that stronger conditional claim;
it is deliberately absent, rather than called harmless information.

Pairwise independence. Let H be Hp or Hp', s >= 1, and let the elements e of a finite H-measurable family have
pairwise distinct H-measurable incidence sets I(e) and residues R(e) = (f(e) + sum_(j in I(e)) z_j) mod 2^s, with f(e)
H-measurable and the z_j i.i.d. uniform on [0, 2^s) given H. For fixed c let S count the e with I(e) nonempty and
R(e) = c. Each such R(e) is uniform, so E[S | H] is their number over 2^s. For distinct nonempty I(e), I(e')
take j in the symmetric difference, say j in I(e') \ I(e), and i' in I(e); the map (z_(i'), z_j) ->
(R(e), R(e')), other coordinates fixed, has matrix [[1,0],[1,1]] if i' in I(e') and the identity otherwise, both
invertible over Z/2^s. So the indicators are pairwise independent and Var[S | H] <= E[S | H].

Stage 1. A pair's label sum is the sum of the k_j over its incidence set I, so vX = (f0 + sum_(j in I) g_j) mod 2^r with f0 = floor((sum_(j in I) lo_j)/2^p),
Hp-measurable. Fix v; with H = Hp, s = r, z = g, the count S of pairs with nonempty incidence and vX = v has
E[S | Hp] <= L^2/2^r = mX, and |X_v| <= S + 1. If |X_v| > 2 mX then S >= 2 mX, so Dv := S - E[S | Hp] >= mX >= 1
and |X_v| <= Dv + mX + 1 <= 3 Dv <= 3 Dv^2/mX. Hence E[ |X_v| [|X_v| > 2 mX] | Hp ] <= 3 Var[S | Hp]/mX <= 3.
The same holds for Y_v2.

Stage 2. All X_v, Y_v2 are Hp'-measurable. Fix (v, v2) with |X_v|, |Y_v2| <= 2 mX, and fix v'. Likewise, bits
p+r..p+b-1 of the label sum of a tuple e are (f1 + sum_(j in I(e)) g'_j) mod 2^r' with
f1 = floor((sum_(j in I(e)) (lo_j + 2^p g_j))/2^(p+r)), Hp'-measurable. With H = Hp', s = r', z = g', the count S'
of tuples of X_v x Y_v2 with nonempty incidence and W1 value v' has E[S' | Hp'] <= |X_v| |Y_v2|/2^r' <=
4 mX^2/2^r' = 4 mu4 (as 2l - r' = lam' + kappa). Since sz <= S' + 1 and Cp = 8 mu4 + 1,
sz - tl = (sz - Cp)_+ <= (S' - 8 mu4)_+. If S' > 8 mu4 then Dz := S' - E[S' | Hp'] > 4 mu4 and
S' - 8 mu4 <= Dz <= Dz^2/(4 mu4). So E[sz - tl | Hp'] <= Var[S' | Hp']/(4 mu4) <= 1.

Summing. Take E[. | Hp] of Lemma 6.3. As sum_(v2) |Y_v2| = sum_v |X_v| = L^2, the cut term is at most
sum_v |X_v| [|X_v| > 2 mX]/L^2 + sum_(v2) |Y_v2| [|Y_v2| > 2 mX]/L^2, of expectation at most
6 * 2^r/L^2 = 6 * 2^(-l). The overflow term sums (sz - tl)/L^4 over at most 2^(2r + r') triples with (v, v2) not
cut, an Hp'-measurable condition, so conditioning on Hp' first bounds it by 2^(2r + r')/L^4 = 2^(-kappa - lam').
The block term is below 2^(-kappa) (Lemma 6.3). As l >= kappa + 3 and lam' >= 1, the total is at most
(3/4 + 1/2 + 1) 2^(-kappa) < 2^(2 - kappa). QED.

The bound conditions on no outcome of the attempt itself. Within the attempt, v' is measured before the
listing of step 4, and no branch or FAIL decision before it reads label bits at positions >= p + r.

