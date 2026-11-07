# COMPLETE ADAPTED virtual IFW-12-32, part1/2

All resource assertions concern VIRTUAL P. Read virtual-phase.md then
virtual-decode.md as ONE source proof. Explicitly ADAPTED from actual
d8c97e5d-b6be-4684-84ea-a20585c455f5,commit
77ea9d1cb9fca3eb62d593e7dde282cc0d1a1547,original full proof SHA256
e1455f0b08ac0a6dce46fd071ac395042cdb74fc51711ebee0ca2fd02e5dbf93.
NOT byte-identical: new Section5.7 defines reduced ideal law; Section8.2
replaces Hp and its factorization/stopping proof; Section11.1 replaces
the retry-cost appeal with explicit conditional fresh-attempt sums.
All original algorithm/profile/guards/decoders and credits remain.
Historical first-person provenance denotes original authors.

--- BEGIN COMPLETE ADAPTED VIRTUAL PART ---

# IFW-12-32: implicit-fiber four-input collimation at constant width n^(1/2), T = O(n^(7/2) 2^((43/18) sqrt n)), S_C = O(n^2 2^((3/4) sqrt n)), Q = O(n^2 2^((8/9) sqrt n)), O(n) qubits

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single algorithm IFW-12-32 below (Sections 3-11: e-man07's CW1 algorithm, public submission cfe82a87, with its collimation tree replaced by the constant-width schedule of Section 7 and the merges MERGE4I of Section 6.3; provenance in Section 1; a = 1/2, A = 3/2, C = 3/4, main-branch threshold n >= 4096) receives N in binary and fresh independent copies of rho_s, and outputs the entire s with unconditional probability at least 1 - 2^-8 > 2/3. On EVERY execution branch (including every failure, retry, discard and abort) it satisfies jointly

    T   = O(n^(7/2) 2^((43/18) sqrt n)),
    S_C = O(n^2 2^((3/4) sqrt n)),
    S_Q = O(n),
    Q   = O(n^2 2^((8/9) sqrt n)).

All outside constants are absolute; the inner coefficients are explicit rationals. These expressions are the structured envelopes of submission.json, with exact growth indices 1/2, 1/2, 0, 1/2, and the fifth claim is the clean-input tolerance 0 (Sections 14, 15).

Notation (CW1's): d = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with s = s1 + M s2 (mod N); omega = exp(2 pi i/N); data basis states |u>, u in [0,N), are stored in n qubits. A "label" is a known integer, a "multiplier" W an integer frequency factor, hd a Hamming distance; T denotes total work only.

## 1. Provenance and what is new

IFW-12-32 is the algorithm and proof of IFCW23 (public submission 19391317-be51-44c1-af9f-7f3dfbf32d28, read at immutable commit 613403fd1bfd1fe25ce6a6e8c6447c60e51d20ce of Layr-Labs/dcp) instantiated at (a, A, C) = (1/2, 3/2, 3/4), the boundary A = 2C of its constraint C < A <= 2C, with a = 1/2 in place of its a = 2/3. As in IFCW23, the direct source read in full: Sections 6.3 (MERGE4I) and 8.1 (Lemma 8.2) are IFC1's text unchanged (public submission 1294d17f-2acf-4e10-9996-6b4375388f49); Sections 2-4, 6.1, 9, 10, 12 and 15 and the Section 6 preamble (except its heading) are the text of e-man07's CW1 (cfe82a87-0d65-454e-b1df-4789dc95aab4), itself a schedule modification of AdamGagol's CS1 (b56c7ceb-de59-42da-9e3b-6ee96e4e4145, identical to f1481815-9577-4990-abe3-7b79fa5d9284); Section 6.2 is CW1's text except its cost sentences, which state the sizes of this regime; Section 8 carries IFC1's edits (recorded outcomes, two citations); Sections 5 and 11 are edited only at the places IFC1 and IFCW23 edit them (algorithm name, Lemma 5.2 numerics, threshold, parameter list, the cost sentences of Lemma 11.2's bullets), restated here for a = 1/2. The collimation step and remainder argument are Kuperberg's (arXiv:1112.3333v1, Algorithm 4.1, Proposition 4.2, Section 4.6). From e-man07's MW4 (33a6df9d-08d8-488b-a3f7-01f5f32373a4): steps 5-8 of MERGE4I, the failure-identity form, the two-heap streams (Schroeppel-Shamir, SIAM J. Comput. 10(3), 1981) and the overflow moment argument. The class-restricted streams are the modular Schroeppel-Shamir enumeration of Howgrave-Graham and Joux (EUROCRYPT 2010); the sigma-field Hp follows the public entry dc3e145e-7ee7-4c4d-ab7e-bbd9a2e9e58a. The constant-width regime (leaves of about n^a qubits, bringing the copies to 2^(O(n^(1-a)))) is the idea of zereraz's CS1-S3 (6d6aef78-ab39-436a-9d5d-771557d6fb9f), whose merges are binary; no text of it is used. No earlier verdict is a premise; every step is proved below.

New here (Sections 0, 7, the cost sentences of Lemma 11.2, 13, 14): the schedule point (a, A, C) = (1/2, 3/2, 3/4), so n^a = n^(1-a) = sqrt n and C < A = 2C. Stored tables have exponent Lam = kappa + 1 + w with w = ceil((3/4) sqrt n); four-input levels stream pair fibers of about 2^l pairs (l = kappa + 1 + lw, lw = ceil((3/2) sqrt n)), never stored as tables. A four-input level cancels w + lw + kappa + 2 bits, so the tree has fewer than (4/9) sqrt n + 1 four-input levels (Lemma 7.0) and the copies number about 4^((4/9) sqrt n), with work about 2^l per copy and stored tables of 2^Lam entries; at most four binary levels absorb the remainder. At a = 1/2 the two exponential scales of T are both powers of sqrt n and combine into the single exact coefficient 43/18 = 3/2 + 8/9 (Section 14). At A = 2C the endpoint fact 2w - lw in {0,1} (proved in S2 below by the exact ceil case analysis) replaces IFCW23's strict-interior reading of its S2; every premise consumed downstream is an identity or a one-sided inequality that survives the endpoint (Sections 6.3, 8.1, 8.2). No first-method, novelty or prior-acceptance claim is made.

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
(Cf+1)-st one, IFW-12-32 stops, releases everything and outputs 0 (ABORT).

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
(sqrt n + 1)/n decreases. Also Cf >= 20, because Qcap >= 6144 * nqmax >= 6144 Lam
>= 6144 C n^a = 4608 sqrt n >= 2304 sn (Section 7; n^a = sqrt n).
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

IDEAL run. The ideal run is IFW-12-32 in the latent-label model with every LE output
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
O(n) bits. With lam, b <= 8 n^a (Section 7), this is O(n^2 (L + L')) core steps.
The quantum scratch is O(n^a) beyond the two index registers. The classical
scratch (order, pos, lo, cnt, off, Dx, aa, bb and the inverse block table) is
O((L + L') n^a) bits, and the output table is L' fields of w' bits plus
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

Throughout, n >= 4096 (the main branch of Section 11), with the fixed rationals a = 1/2, A = 3/2 and C = 3/4, so
C < A = 2C and n^a = n^(1-a) = sqrt n. Input: a supplier of LEAF QUBITS, each a positive qubit with a known label uniform on [0, 2^D), D >= 2,
independently. Put B = D - 1 <= n, the number of bits to collimate. Global parameters, functions of n only, computed by
exact integer arithmetic (y >= c sqrt n is tested by squaring, as (c2 y)^2 >= c1^2 n for c = c1/c2):

    w = least integer with (4 w)^2 >= 9 n, i.e. ceil(C n^a),   lw = least integer with (2 lw)^2 >= 9 n, i.e. ceil(A n^a),
    mu = least integer M >= 1 with (M - 1)(w + lw + 2) + 2w + lw + 2 >= n,
    kappa = ceil(log2(mu + 4)) + 3,   Lam = kappa + 1 + w,   l = kappa + 1 + lw,   r = 2 Lam - l,
    nqmax = 16 * 4^mu * Lam.

So C n^a <= w < C n^a + 1, A n^a <= lw < A n^a + 1 and 8(mu + 4) <= 2^kappa < 16(mu + 4). In Sections 5.5, 6.2, 7, 11, 13
and 14, a, A, C, w, lw, mu, l, r and beta (the number of binary levels, unrelated to beta_i of Section 9) are the
quantities defined here; a is unrelated to a2, and w here is not the field width
of STORAGE (which is w_i below).

Levels. A tree consists, from the bottom, of LEAF tables of Lam qubits (level 0), then beta binary levels (MERGE of
Section 6.2 with input exponent Lam and output exponent Lam, or 1 at a binary root), then m4 four-input levels (MERGE4I
of Section 6.3 with lam = Lam, l_i = l, r_i = r, and output exponent Lam below the root and 1 at the root). Level i has
arity f_i = 2 for i < beta and 4 for i >= beta, and a node of level i has 2^(min(i, beta)) 4^(max(0, i - beta)) leaf
vectors below it. The capacities, by substitution (for four-input levels r + r' with r' = 2l - lam' - kappa), are

    binary below the root:  bin = 2 Lam - Lam - kappa = w + 1,      binary root:  binr = 2 Lam - 1 - kappa = 2w + kappa + 1,
    four-input below root:  bm4 = Lam + l - kappa = w + lw + kappa + 2,   four-input root:  rc4 = 2 Lam + l - 1 - kappa = 2w + lw + 2 kappa + 2.

Per tree, let Phi(0) = 0 and Phi(k) = (k - 1) bm4 + rc4 for k >= 1, and let m4 be the largest k >= 0 with Phi(k) <= B.
- If m4 >= 1: the four-input levels get b = bm4 (rc4 at the root); R = B - Phi(m4) satisfies 0 <= R < bm4 by maximality;
  beta = ceil(R/bin); the binary levels below get b_i = min(bin, still unallocated) from the top.
- If m4 = 0: then B < rc4; beta is the least integer >= 1 with (beta - 1) bin + binr >= B; the top binary level is the
  root, and the binary levels get b_i = min(their capacity, still unallocated) from the top.
Then sum_i b_i = B, every four-input level is full, and every binary b_i is at most its capacity. The tree has
m = beta + m4 levels; put p_0 = 0 and p_(i+1) = p_i + b_i, so p_m = B, and nq_D = 2^beta 4^m4 Lam (leaf qubits per tree).

Lemma 7.0 (depth). (a) Phi(mu) >= n >= B, so m4 <= mu. (b) If kappa <= w and lw <= 2w, then beta <= 4, so
m <= mu + 4 and nq_D <= nqmax. (c) mu < n/(w + lw + 2) + 1 <= n^(1-a)/(C + A) + 1, so
4^mu < 4 * 2^((2/(C + A)) n^(1-a)).

Proof. (a) As kappa >= 0, Phi(mu) >= (mu - 1)(w + lw + 2) + 2w + lw + 2 >= n by the definition of mu, and Phi is
increasing, so the largest k with Phi(k) <= B <= n is at most mu. (b) If m4 >= 1, R < bm4 = w + lw + kappa + 2 <=
3w + kappa + 2 <= 4(w + 1) = 4 bin, so beta = ceil(R/bin) <= 4. If m4 = 0, beta - 1 = ceil(max(0, B - binr)/bin) <=
ceil((rc4 - 1 - binr)/bin) = ceil((lw + kappa)/(w + 1)) <= ceil((2w + kappa)/(w + 1)) <= ceil(3w/(w+1)) <= 3. So beta <= 4, m = beta + m4 <= mu + 4, and
nq_D = 2^beta 4^m4 Lam <= 16 * 4^mu * Lam = nqmax. (c) If mu >= 2, minimality
gives (mu - 2)(w + lw + 2) + 2w + lw + 2 < n, that is (mu - 1)(w + lw + 2) + w < n, so mu - 1 < n/(w + lw + 2); for
mu = 1 this is clear. As w + lw + 2 > (C + A) n^a, mu - 1 < n^(1-a)/(C + A), and 4^mu = 4 * 4^(mu - 1). QED.

Numbers: C + A = 9/4 and 2/(C + A) = 8/9.

Size facts for n >= 4096, each proved at n = 4096 and extended by monotonicity: differences of the form
c sqrt n - c' log2 n - c'' (c > 0) increase once c sqrt n ln 2 > 2c' (their derivative is then positive),
which holds at n = 4096 for every (c, c') used below (largest threshold n > 60); the rest increase in
sqrt n alone, for n >= 16.

- S1. lw - w > (3/4) sqrt n - 1 (as lw >= (3/2) sqrt n and w < (3/4) sqrt n + 1). The function
  (3/4) sqrt n - 2 log2 n - 9 equals 15 at n = 4096 and increases for n > 60, so
  lw - w > 2 log2 n + 8 >= 2 ceil(log2 n) + 6. Hence l = Lam + (lw - w) >= Lam + 1 and
  2^(lw - w) >= 64 n^2.
- S2 (endpoint A = 2C). Write x = (3/4) sqrt n = m + f with m = floor x and 0 <= f < 1, so w = ceil x. If
  f = 0: w = m, lw = ceil(2x) = 2m, 2w - lw = 0. If 0 < f <= 1/2: w = m + 1, lw = ceil(2m + 2f) = 2m + 1,
  2w - lw = 1. If 1/2 < f < 1: w = m + 1, lw = 2m + 2, 2w - lw = 0. Hence lw <= 2w always, and
  2w - lw in {0, 1}, so r = 2 Lam - l = kappa + 1 + (2w - lw) is kappa + 1 or kappa + 2. Also
  l = kappa + 1 + lw <= kappa + 1 + 2w <= 2(kappa + 1 + w) = 2 Lam. Nothing below needs 2w - lw >= 2.
- S3. By Lemma 7.0(c), mu - 1 < n/(w + lw + 2) < n/((C + A) sqrt n) = (4/9) sqrt n. Hence
  mu + 4 < (4/9) sqrt n + 5 <= 2 sqrt n for n >= 11; in integer form (mu + 4)^2 < 4n. Also
  4^mu = 4 * 4^(mu - 1) < 4 * 2^((8/9) sqrt n).
- S4. mu + 4 < (4/9) sqrt n + 5 < 34 < n at n = 4096, and the difference increases, so mu + 4 < n
  for n >= 4096. Hence kappa = ceil(log2(mu + 4)) + 3 < log2(mu + 4) + 4 < log2 n + 4. Also
  (3/4) sqrt n - log2 n - 3 > 30 at n = 4096 and increases for n >= 15, so
  kappa < log2 n + 4 <= w + 1, and kappa <= w. The definitional identities give
  2^kappa < 16(mu + 4) <= 32 sqrt n; in integer form 2^(2 kappa) < 1024 n.
- S5. Lam = kappa + 1 + w < (log2 n + 4) + 1 + ((3/4) sqrt n + 1) = log2 n + (3/4) sqrt n + 6 <= 2 sqrt n
  at n = 4096 (66 <= 128; the difference (5/4) sqrt n - log2 n - 6 increases for n >= 6), so Lam < 2 sqrt n;
  in integer form Lam^2 < 4n. Then l <= 2 Lam < 4 sqrt n, and every capacity is at most
  rc4 <= 4 Lam < 8 sqrt n, so every lam_i, l and b_i is at most 8 sqrt n = 8 n^a.
- S6. The depth-first stack holds at most 4 index registers per level, of at most Lam qubits, over at most
  m + 1 <= mu + 5 levels: 4(mu + 5) Lam <= 4((4/9) sqrt n + 6)(2 sqrt n) = (32/9) n + 48 sqrt n <= 20 n for
  n >= 9, using S3 and S5.

By S2 and S4, Lemma 7.0(b) applies: beta <= 4, m <= mu + 4 and nq_D <= nqmax.

MERGE4I parameters. At a four-input level, l_i = l, r_i = r and r' = b_i - r = 2l - lam' - kappa. The preconditions of
Section 6.3 hold: lam = Lam >= kappa + 2 (Lam >= w + 2), Lam + 1 <= l <= 2 Lam (S1, S2), r = 2 Lam - l, lam' >= 1 and
r' >= 2(Lam + 1) - Lam - kappa = w + 3 >= 1 below the root (by l >= Lam + 1), while at the root
r' = 2l - 1 - kappa = kappa + 1 + 2 lw >= 1; also l >= kappa + 3 (lw >= 2) and p + b <= B.

Failure budgets. For a binary level, b_i + lam_(i+1) - 2 lam_i <= bin + Lam - 2 Lam = -kappa below the root and
binr + 1 - 2 Lam = -kappa at the root, so Lemma 6.1 gives Pr[FAIL] <= 2^-kappa for any input tables. Four-input levels
are bounded by Lemma 8.2.

LEAF: take Lam leaf qubits as the index register (bit j = qubit j). Build the table incrementally, lab[0] = 0 and
lab[x + 2^j] = lab[x] + k_j for x < 2^j: one addition per entry, O(n 2^Lam) core steps. The table has length 2^Lam, is
collimated to p_0 = 0, and in the ideal run is exactly the tensor product state.

Field widths. A label is a sum of at most nq_D <= nqmax leaf labels below 2^(B+1), so it is below
2^(B+1+ceil(log2 nqmax)). Tables of level i are collimated to p_i and stored with w_i = B + 1 + ceil(log2 nqmax) - p_i
bits per high part, at most 3n, as log2 nqmax <= 4 + 2mu + log2 Lam < (8/9) sqrt n + (1/2) log2 n + 7 <= n for
n >= 4096 (S3, S5; at n = 4096 the left side is below 70, with the difference increasing for n >= 16).

VEC(i): if i = 0 return LEAF. Otherwise repeat:
- build the f_(i-1) inputs, each by VEC(i-1);
- out = MERGE(X1, X2; p_(i-1), b_(i-1), lam_i) if f_(i-1) = 2, with lam_i = Lam (or 1 when i = m), and
  out = MERGE4I(X1, X2, X3, X4; p_(i-1), r, b_(i-1) - r, lam_i, l) if f_(i-1) = 4;
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

