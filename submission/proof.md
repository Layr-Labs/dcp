# IFC2120: implicit-fiber four-input collimation with streamed, unstored pair fibers, T and Q = O(poly(n) 2^((14411/10000) sqrt n)), S_C = O(n^2 2^((21/20) sqrt n)), O(n) qubits

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single algorithm IFC2120 below
(Sections 3-11: e-man07's CW1 algorithm, public submission cfe82a87, with its collimation tree replaced by
the schedule of Section 7, whose upper levels use the four-input merge MERGE4I of Section 6.3, and with
main-branch threshold n >= 1024) receives N in binary and fresh independent copies of rho_s, and outputs
the entire s with unconditional probability at least 1 - 2^-8 > 2/3. On EVERY execution branch (including
every failure, retry, discard and abort) it satisfies jointly

    T   = O(n^4 (log2 n)^2 2^((14411/10000) sqrt n)),
    S_C = O(n^2 2^((21/20) sqrt n)),
    S_Q = O(n),
    Q   = O(n^(3/2) (log2 n) 2^((14411/10000) sqrt n)).

All outside constants are absolute. The tree height is below tau sqrt n + 4 with tau = sqrt(1241/200) - 21/20 < 14411/10000
(Lemma 7.0), so the inner coefficients 14411/10000 and 21/20 are explicit rationals. These expressions are the
structured envelopes of submission.json, with exact growth indices 1/2, 1/2, 0, 1/2 (Section 14). The fifth
claim is the clean-input tolerance 0 (Section 15).

Notation (CW1's): d = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with
s = s1 + M s2 (mod N); omega = exp(2 pi i/N); data basis states |u>, u in [0,N), are stored in n qubits. A
"label" is a known integer, a "multiplier" W an integer frequency factor, hd a Hamming distance; T denotes
total work only.

## 1. Provenance and what is new

IFC2120 is CW1 (public Yukon submission cfe82a87-0d65-454e-b1df-4789dc95aab4, e-man07) with a new upper-level merge
and schedule; CW1 is a schedule modification of CS1 (b56c7ceb-de59-42da-9e3b-6ee96e4e4145 by AdamGagol, identical to
f1481815-9577-4990-abe3-7b79fa5d9284). Sections 2-4, 6.1, 6.2, 9, 10, 12 and 15 and the Section 6 preamble (except its
heading) are CW1's text unchanged; Section 5 differs only in the algorithm name (twice) and two numeric lines of
Lemma 5.2; Section 8 before 8.1 only in the recorded outcomes, the list of quantities read and two citations; Section
11 in its threshold, parameter list, Q*, algorithm name, Lemma 11.1 and the merge bullets of Lemma 11.2. Sections 0,
1, 6.3, 7, 8.1, 13 and 14 are new or rewritten (Section 7 keeps CW1's LEAF and root text). The collimation step
and distribution-free remainder argument are Kuperberg's (arXiv:1112.3333v1, Algorithm 4.1, Proposition 4.2, Section
4.6). MERGE4I builds on e-man07's MW4 (33a6df9d-08d8-488b-a3f7-01f5f32373a4): steps 5-8 are MW4's steps 3-6, Lemma 6.3
has the form of MW4's failure identity, the streams are MW4's two-heap streams (Schroeppel-Shamir, SIAM J. Comput.
10(3), 1981), and the overflow bound of Lemma 8.2 is MW4's moment argument. Streaming one residue class of a measured
window is the modular Schroeppel-Shamir enumeration of Howgrave-Graham and Joux (EUROCRYPT 2010). The sigma-field Hp
of Lemma 8.2 and its use in Lemma 11.1 follow our entry dc3e145e-7ee7-4c4d-ab7e-bbd9a2e9e58a. No earlier verdict is a
premise; every step is proved below.

New (Sections 6.3, 7, 8.1, 11, 13, 14): MERGE4I measures a window W0 on each input pair, then the next window W1 of
the four-sum, and lists the final fiber from the two pair fibers without storing them, streaming each with one heap
entry per stored row (MW4's merge is, up to the constant in Cp and which run is buffered, the case r = 0). We call X_v, Y_v2 of Section 6.3 the pair fibers; they are streamed,
never stored as tables. Above the binary levels every level is a MERGE4I whose pair
fibers have about 2^(kappa+2+h) pairs at height h while every stored phase-vector table has length at most 2^Lam (the list Tl has at most Cp
rows), so two heights cancel
about w + h bits instead of 2w. Lemma 7.0 bounds the height by (sqrt(4 + 2x^2) - x) sqrt n + 4 at x = 21/20, against
CW1's capped 1/x + x/2 = 1241/840. The comparison is with public rows on this challenge; no claim is made about the wider
literature, and Kuperberg's uncapped sqrt 2 is not improved.

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
(Cf+1)-st one, IFC2120 stops, releases everything and outputs 0 (ABORT).

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
exp(1) EX/x <= exp(1) (sqrt n + 1)/n <= exp(1) * 33/1024 < 1/2 for n >= 1024, since
(sqrt n + 1)/n decreases. Also Cf >= 20, because Qcap >= 6144 * 2^hmax >= 6144 * 2^(sqrt n) >= 20 (sqrt n + 1), with hmax >= sqrt n from Section 7.
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

IDEAL run. The ideal run is IFC2120 in the latent-label model with every LE output
replaced by the latent k and without the cap of 5.5. The actual and ideal runs
can be coupled to coincide unless some LE call returns a wrong label or ABORT
occurs, so every event's probability differs between them by less than
2^-11 + 2^-20. Resource bounds are proved for every ACTUAL branch directly,
because they rest only on caps and fixed allocations.

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

Throughout, n >= 1024 (the main branch of Section 11), rho := sqrt n >= 32, and x = 21/20. Input: a
supplier of LEAF QUBITS, each a positive qubit with a known label uniform on [0, 2^D), D >= 2, independently.
Put B = D - 1 <= n, the number of bits to collimate. Global parameters, functions of n only, computed by exact
integer arithmetic:

    w = the least integer with 400 w^2 >= 441 n, i.e. ceil((21/20) sqrt n),
    G = least integer G >= 0 with 2 (G + w)^2 >= 2n + w^2,
    mu = w + G + 1,   kappa = ceil(log2 mu) + 3,   Lam = kappa + 1 + w.

So x rho <= w < x rho + 1 and 8 mu <= 2^kappa < 16 mu. In Sections 7, 11, 13 and 14, G, rho, tau and x are the
quantities defined here, and in Section 7 J is the index of (7.0); they are unrelated to the precision
G = n + 40 + T_V of Section 5.3, the residues rho_t and row index rho of Section 6.3, the top bits tau_j of Section
8 and the index registers x. The J of Q*, Lemma 11.1 and Section 13 is the stage count of Section 9.

Level i has arity f_i, input exponent lam_i, height h_i
(a node of level i has 2^(h_i) leaf vectors below it), capacity bmax_i as a non-root level and rootcap_i as the
root (output exponent 1):

    Phase A, 0 <= i <= w-1:          f_i = 2, lam_i = kappa + 1 + i, h_i = i, bmax_i = i, rootcap_i = kappa + 2i + 1;
    Phase I, i = w + j, 0 <= j <= G:  f_i = 4, lam_i = Lam, h_i = w + 2j, l_i = Lam + 1 + 2j = kappa + 2 + h_i,
                                     r_i = 2 Lam - l_i = kappa + w - 2j,
                                     bmax_i = 2w + 2j + kappa + 3, rootcap_i = 3w + 2j + 2 kappa + 3.

These are substitutions: for binary levels bmax_i = 2 lam_i - lam_(i+1) - kappa with lam_(i+1) = kappa + 2 + i
(= Lam at i = w-1) and rootcap_i = 2 lam_i - 1 - kappa; for four-input levels bmax_i = r_i + (2 l_i - Lam - kappa)
and rootcap_i = r_i + (2 l_i - 1 - kappa).

A tree with m levels (1 <= m <= mu) has ROOT level m-1, lam_m := 1, capacity Sum(m) = sum_(i < m-1) bmax_i +
rootcap_(m-1) and output height h_m = m (m <= w) or 2m - w (m >= w); m is the least m >= 1 with Sum(m) >= B. Explicitly Sum(m) = (m-1)(m-2)/2 + kappa + 2m - 1 for m <= w, and

    Sum(w + 1 + J) = w(w-1)/2 + J (2w + kappa + 3) + J (J - 1) + 3w + 2J + 2 kappa + 3   (0 <= J <= G).   (7.0)

So Sum(m+1) - Sum(m) is m + 1 for m < w, 2w + kappa + 3 for m = w, and 2w + 2J + kappa + 3 for m = w + J with
1 <= J <= G; Sum is increasing.

Lemma 7.0 (capacity and height). (a) Sum(mu) > n + 2w >= B, so m <= mu and h_m <= hmax := h_mu = w + 2G + 2 for
every tree. (b) If w^2 < 2n, then G < cJ rho + 1 and hmax < tau rho + 4, with cJ = sqrt(1 + x^2/2) - x and
tau = sqrt(4 + 2x^2) - x.

Proof. (a) By definition (G + w)^2 >= n + w^2/2, so G^2 + 2wG >= n - w^2/2, and (7.0) with J = G is
Sum(mu) = w(w-1)/2 + G^2 + 2wG + (kappa + 2) G + 3w + 2G + 2 kappa + 3 >= n + 5w/2 + 3. As Sum is increasing and
B <= n, the least m with Sum(m) >= B is at most mu, and h_m is increasing in m. (b) If G >= 1, minimality gives
2(G - 1 + w)^2 < 2n + w^2, so G < sqrt(n + w^2/2) - w + 1; if G = 0 this holds too, as w^2 < 2n gives
sqrt(n + w^2/2) > w. Since y -> sqrt(n + y^2/2) - y is decreasing (derivative (y/2)/sqrt(n + y^2/2) - 1 < 0) and
w >= x rho, G < sqrt(n + x^2 n/2) - x rho + 1 = cJ rho + 1. Then hmax = w + 2G + 2 < 2 sqrt(n + w^2/2) - w + 4
= Fh(w) + 4 with Fh(y) = sqrt(4n + 2y^2) - y, whose derivative 2y/sqrt(4n + 2y^2) - 1 is negative for
0 <= y < sqrt(2n); as x rho <= w < sqrt(2n), Fh(w) <= Fh(x rho) = tau rho. QED.

Numbers at x = 21/20: tau = sqrt(1241/200) - 21/20 < 14411/10000, as 4 + 2x^2 = 1241/200 < (14411/10000 + 21/20)^2 = 620557921/100000000; and
cJ < 391/2000, as 1 + x^2/2 = 1241/800 < (391/2000 + 21/20)^2 = 6205081/4000000.

Size facts for n >= 1024 (rho >= 32). Each condition c rho >= c' with c > 0 is checked at rho = 32;
the bounds on kappa and on w(w-1)/2 carry their own argument.
- w < x rho + 1 <= (7071/5000) rho < sqrt(2n), since (7071/5000 - x) 32 >= 1 and (7071/5000)^2 < 2. So Lemma 7.0(b)
  applies: G < (391/2000) rho + 1, hmax < tau rho + 4 < (14411/10000) rho + 4 and 2^hmax < 16 * 2^((14411/10000) sqrt n). Also
  hmax >= w >= x rho >= rho.
- mu = w + G + 1 < (x + 391/2000) rho + 3 <= 2 rho, since (2 - x - 391/2000) 32 >= 3.
- kappa < log2 mu + 4 <= log2 rho + 5 <= rho/2, true at rho = 32 (log2(32) + 5 = 10 <= 16) and thereafter, as
  rho/2 - log2 rho increases. Also 2^kappa < 16 mu <= 32 rho and kappa >= 4.
- 2G < 2 (391/2000) rho + 2 <= x rho <= w, since (x - 2 * 391/2000) 32 >= 2. So for j <= G,
  r_(w+j) = kappa + w - 2j >= kappa and Lam + 1 <= l_(w+j) <= 2 Lam.
- Lam = kappa + 1 + w < rho/2 + x rho + 2 <= 2 rho, since (3/2 - x) 32 >= 2. So lam_i <= Lam <= 2 rho,
  l_i <= 2 Lam <= 4 rho, and every capacity is at most 3w + 2G + 2 kappa + 3 <= 4 Lam <= 8 rho.
- 2w + 2G + kappa + 3 <= 3w + w/(2x) + 3 <= w(w-1)/2, as kappa <= rho/2 <= w/(2x), and the last step is
  w - 1 >= 6 + 1/x + 6/w, true as w >= x 32 >= 8 + 1/x.
- hmax < (14411/10000) rho + 4 <= 2 rho, since (2 - 14411/10000) 32 >= 4.

Allocation. Allocate b_(m-1), b_(m-2), ..., b_0 in that order greedily, with b_(m-1) = min(rootcap_(m-1), B) and
then b_i = min(bmax_i, B - already allocated). Then sum_i b_i = B, and some low levels may get smaller values or
0. Put p_0 = 0 and p_(i+1) = p_i + b_i, so p_m = B. Let nq_D = 2^(h_m) (kappa + 1) be the number of leaf qubits
per tree.

Lemma 7.1 (four-input levels are full). In any tree with m >= w + 1, every level i >= w gets its full capacity:
b_i = bmax_i for w <= i < m-1, and b_(m-1) = rootcap_(m-1).

Proof. Here m >= 2, so Sum(m-1) < B by minimality, and the deficit Sum(m) - B is below
Sum(m) - Sum(m-1) <= 2w + 2G + kappa + 3 <= w(w-1)/2 = sum_(i < w) bmax_i (size facts). So the levels i >= w have
total capacity Sum(m) - w(w-1)/2 < B, and the greedy allocation, serving levels from the top, gives each its full
capacity before reaching Phase A. QED.

MERGE4I parameters. At a four-input level i put l = l_i, r = r_i and r' = b_i - r_i, which by Lemma 7.1 equals
2 l_i - lam_(i+1) - kappa with lam_(i+1) = Lam below the root and lam_m = 1. The preconditions of Section 6.3
hold: lam = Lam >= kappa + 2, Lam + 1 <= l <= 2 Lam, r = 2 Lam - l, lam' >= 1 and r' >= 2(Lam + 1) - Lam - kappa
= w + 3; also l >= kappa + 3 and p + b <= B.

Failure budgets. For a binary level b_i + lam_(i+1) - 2 lam_i <= -kappa by substitution (i + (kappa + 2 + i) -
2(kappa + 1 + i) = -kappa below the root, rootcap_i + 1 - 2 lam_i = -kappa at the root), so Lemma 6.1 gives
Pr[FAIL] <= 2^-kappa for any input tables. Four-input levels are bounded by Lemma 8.2.

LEAF: take kappa+1 leaf qubits as the index register (bit j = qubit j). Build
the table incrementally, lab[0] = 0 and lab[x + 2^j] = lab[x] + k_j for x < 2^j:
one addition per entry. The table has length 2^(lam_0), is collimated to p_0 = 0,
and in the ideal run is exactly the tensor product state.

Field widths. A level-i label is a sum of at most 2^(h_i) (kappa+1) leaf labels below 2^(B+1), so it is below
2^(B+1+h_i+gw), gw = ceil(log2(kappa+1)). Level-i tables are collimated to p_i and stored with
w_i = B + 1 + h_i + gw - p_i bits per high part, at most 3n, as h_i <= 2 rho and gw <= kappa <= rho/2.

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
r' = b_i - r_i and lam' = lam_(i+1) (or 1 at the root). Let Hp be the sigma-field generated by everything that
happened before its step 1 except the label bits at positions >= p of the leaves of its four inputs: the bits
below p of those labels, the measurement outcomes, lists, coins and controller decisions of all earlier steps,
and everything on other copies. (The input tables also record the higher bits; Hp does not contain them.)
Then Pr[FAIL | Hp] <= 6 * 2^(-l) + 2^(-kappa - lam') + 2^(-kappa) < 2^(2 - kappa).

Proof. Let Lv be the set of leaves of the four inputs, a union of four pairwise disjoint sets. For j in Lv write
k_j = lo_j + 2^p g_j + 2^(p+r) g'_j + 2^(p+b) u_j with 0 <= lo_j < 2^p, 0 <= g_j < 2^r, 0 <= g'_j < 2^r'. This is
possible as p + b <= B < D, and k_j uniform makes lo_j, g_j, g'_j, u_j independent and uniform.

Factorization. Every earlier step of the tree that involves a leaf of Lv is a merge at a lower level, with
p' + b' <= p, or a leaf-acceptance test or a controller decision. By Lemmas 6.1 and 6.3 those laws, residues,
sort keys, counts, ranks, lists and block choices read only label bits below p, and bits below p of a sum of
leaf labels depend only on the lo_j. Steps elsewhere use disjoint copies. So, exactly as in the proof of Lemma
8.1 with p in place of B, conditional on Hp the pairs (g_j, g'_j) (j in Lv) are i.i.d. uniform on
[0, 2^r) x [0, 2^r'). Let Hp' be generated by Hp and the g_j (j in Lv); conditional on Hp' the g'_j are i.i.d.
uniform. The incidence set I(.) of each pair and each tuple is Hp-measurable; distinct pairs, and distinct
tuples, have distinct incidence sets (concatenation and re-indexing, as above), so at most one pair (x1, x2),
one pair (x3, x4) and one tuple have an empty one.

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

## 9. Odd part: s1 = s mod M by free-frequency decoding

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so N >= 3 * 2^a2
and d - 1 >= a2. Put theta = s1/M in [0,1). Every stage uses D = d, B = d - 1,
nq = nq_d and

    K = 2^13 (ceil(log2 nq) + ceil(log2 n) + 30).

The stages are j = 0, 1, ..., J, where J = min{ j >= 0 : 2^(j+3) > 2M }. By
minimality, J + 1 <= log2 M <= n.

Source for stage j. Compute alpha_j by extended Euclid and CRT so that
alpha_j = 1 (mod 2^a2) and alpha_j = 2^j (2^(d-1-a2))^(-1) (mod M). Then alpha_j is a
unit modulo N. A leaf qubit is made as follows:
- acquire a fresh copy and apply Mult_(alpha_j);
- run LE to obtain k, and accept iff k < 2^d (otherwise discard the copy and
  acquire again);
- on acceptance, apply X to the control.

In the ideal run, accepted labels are i.i.d. uniform on [0, 2^d), each copy is
accepted with probability 2^d/N > 1/2, and the qubit is pq_k(alpha_j s), i.e. it
has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^(d-1) W th = W 2^(d-1-a2) alpha_j s / M = 2^j W s1 / M   (mod 1),            (9.1)

because 2^(d-1-a2) alpha_j = 2^j (mod M) and s = s1 (mod M). So a TREE_d root of
stage j is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known
frequency f = 2^j W.

Measurement. For i = 1..K:
- run TREE_d;
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

Lemma 9.1. Suppose theta is within circular distance rad_j of z_(j-1) (no
condition when j = 0). Then, in the ideal run, with probability at least
1 - 2^-20/n, theta is within circular distance 2^-(j+3) of z_j.

Proof. Let Fs_i be the sigma-field of everything up to and including root i
of the stage, and Gt_i the sigma-field of Section 8 for tree i. For a
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
every far zeta. Tree i uses copies independent of Fs_(i-1). By Lemma 8.1, its
top bits are fair and independent given Fs_(i-1) and Gt_i. So by (8.2) with
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

because (1/2)(cos(pi/128) - cos(pi/8)) > 0.0379 > 2/64 + 2/625 = 0.03445. So the
maximizer is not far. There are at most 2^(ceil(log2 nq)+9) events, and since
e^-x <= 2^-x, exp(-K/8192) <= 2^-(ceil(log2 nq) + ceil(log2 n) + 30). The failure
probability is therefore at most 2^(9-30)/n <= 2^-20/n. QED.

For stage j+1 the hypothesis of Lemma 9.1 is the conclusion of stage j, since
2^-(j+3) = rad_(j+1). By induction, with probability at least 1 - 2^-20, theta
lies within 2^-(J+3) < 1/(2M) of z_J. Output s1 = floor(M z_J + 1/2) mod M. This
equals s mod M because theta = s1/M, and the circular distance handles
wrap-around.

## 10. 2-adic part: s2 bit by bit

If a2 = 0, put s2 = 0 and skip this section. Otherwise s - s1 = M s2 (mod N) for
a unique s2 in [0, 2^a2). The bits of s2 are found at levels g = 0..a2-1. Let
s2low be the known low g bits. Put sh_g = s1 + M s2low (mod N), wd = a2 - g, and
rem = (s2 - s2low)/2^g in Z/2^wd. Then s - sh_g = M 2^g rem (mod N).

Leaf qubit for level g:
- acquire a copy and apply Shift_(sh_g), which makes the secret s - sh_g;
- run LE to obtain k, and apply X to the control.

Ideally the phase is exp(2 pi i k M 2^g rem/N) = exp(2 pi i kk rem/2^wd), with
kk = k mod 2^wd. Since 2^wd divides N and k is uniform on Z/NZ, kk is uniform on
[0, 2^wd). Use kk as the label.

- If wd = 1: if kk = 1, measure X; the outcome is + iff rem is even. If kk = 0,
  discard and repeat.
- If wd >= 2: run TREE_wd (D = wd). If W is even, discard and repeat. If W is
  odd, the root is (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2,
  and an X measurement gives rem mod 2 exactly.

By (8.3), each attempt succeeds with probability exactly 1/2, even if s1 was
wrong. Set bit g of s2. In the ideal run with s1 correct, every bit is correct.
Output (s1 + M s2) mod N.

## 11. The complete algorithm and its source cap

Finite branch (n < 1024, i.e. N <= 2^1023). For each cand = 0..N-1 in order, use
n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand
at the first minus outcome. Output the first cand with no rejection, or 0.
- For cand = s every outcome is plus.
- For cand != s the two data branches are orthogonal, so each outcome is uniform.
- A union bound over cand gives Pr[wrong] <= N 2^-(n+10) <= 2^-10.
- Q <= N(n+10), and all other resources are bounded by absolute constants.

Main branch (n >= 1024). Compute a2, M, d, J, K and all tree parameters. The values
w, G, mu, kappa, Lam and hmax are those of Section 7, and m <= mu and h_m <= hmax for every B <= n used. Put

    Q* = 6 * 2^hmax (kappa+1) ((J+1)K + 2 a2) + 2 a2,    Qcap = 1024 Q*,

and then h_e, h_A, t_V and Cf from Section 5. A binary down-counter of acquisitions is kept,
at amortized O(1) bit flips per acquisition. IFC2120 stops, releases everything
and outputs 0 before an acquisition would exceed Qcap. Otherwise it runs
Section 9 and then Section 10. Parameter, CRT and table computations are
polynomial in n.

Lemma 11.1 (expected ideal acquisitions). In the ideal UNCAPPED run, the
expected number of acquisitions is at most Q*.

Proof. An accepted leaf qubit needs at most 2 acquisitions in expectation
(acceptance probability > 1/2 in Section 9, and 1 in Section 10). Let Qv_i be the
expected number of acquisitions until VEC(i) returns. By Lemma 6.1 and Section 7 at binary levels, and by
Lemma 8.2 at four-input levels, each merge attempt succeeds with conditional probability at least
1 - 2^(2-kappa) >= 1 - 1/(2 mu), given Hp of Lemma 8.2 at four-input levels and given everything before its
step 1 at binary levels (Lemma 6.1 holds for any input tables, so all labels may be included). Both
sigma-fields contain the outcomes of all earlier attempts, which use disjoint copies, so the same bound holds
given those outcomes. By Wald's identity, Qv_(i+1) <= rt f_i Qv_i, where rt = 1/(1 - 1/(2 mu)). Moreover
rt^m <= exp(m/(2 mu - 1)) <= e < 3 for m <= mu. So Qv_m <= 3 * 2^(h_m) * 2(kappa+1) <= 6 * 2^hmax (kappa+1).
Section 9 runs (J+1)K trees. Section 10 needs, per bit, an expected 2 trees by (8.3), or, when wd = 1, an
expected 2 single acquisitions since kk is uniform on {0,1}. Summing gives the bound. QED.

Lemma 11.2 (work per branch). On every actual branch of the main branch, the
number of core steps is at most
O(n^2 log n) Qcap + O(n^(5/2) nq) + poly(n),
where nq = nq_d.

Proof. Charge every core step to an acquisition, or to the fixed-length loops.
- Each acquisition (transform, acceptance test, X, counter update) takes O(n^2)
  core steps. All LE calls together take O(n^2 log n) Qcap + O(n^(5/2)) core
  steps on every branch (Section 5.6), since there is one LE call per
  acquisition and Q <= Qcap.
- A leaf table of 2^(kappa+1) entries costs O(n 2^(kappa+1)). Charged to its
  kappa+1 acquisitions, that is O(n 2^kappa/(kappa+1)), which lies in O(n^2), per
  acquisition.
- A binary merge attempt producing level i+1 <= w costs O(n 2^(kappa+1+i)) (Section 6.2), since both
  its input length and its output length are at most 2^(kappa+2+i). Its two inputs were built from
  2^(i+1)(kappa+1) acquisitions that no other attempt at that level uses, since inputs of a failed merge are
  discarded and never reused. That is O(n 2^kappa/(kappa+1)) per acquisition per level.
- A MERGE4I attempt at level i >= w costs O(n 2^(l_i)) = O(n 2^(kappa+2+h_i)) core steps by Section 6.3, on
  every branch: there L = 2^Lam <= 2^(l_i) = mX, 2^(lam_(i+1)) <= 2^Lam, lam (lam + b) <= 2 rho * 10 rho = 20 n,
  and Cp lam <= (2^(Lam+kappa+3) + 1) 2 rho = O(rho 2^kappa 2^(l_i)) = O(n 2^(l_i)), as Lam + 1 <= l_i and
  2^kappa <= 32 rho. Its four inputs were built from 2^(h_i+2)(kappa+1) acquisitions that no other attempt at
  that level uses: O(n 2^kappa) per acquisition per level.
- Each acquisition lies below at most m <= mu merge attempts, one per level, so the total share is
  O(n mu 2^kappa) = O(n^2) per acquisition, as mu <= 2 rho and 2^kappa <= 32 rho.
- Root measurements and bookkeeping are O(n) per tree, and each tree uses at
  least one acquisition.
- The decoder's fixed loops cost (J+1) * 2^(ceil(log2 nq)+8) * K * O(n)
  = O(n * nq * sqrt n * n) core steps.
- Setup is poly(n) and runs once. It covers the parameters, extended Euclid and
  CRT for at most n stages, the Mult constants, Q*, h_e, the table of Section 4,
  the Section 10 shift values, and the decoder's initial residues
  (f_i c) mod 2^(P_j).

Every loop is either fixed-length or consumes acquisitions, so every branch
terminates with this many core steps. QED.

## 12. Success probability

In the ideal UNCAPPED run, Section 9 errs with probability at most 2^-20, and
Section 10 then never errs. By Markov and Lemma 11.1, the source cap is reached
in the ideal run with probability at most 1/1024. Capping changes the run only
on that event. The actual run differs from the ideal one only if some LE call
returns a wrong label or the high-confidence cap aborts, which has probability
below 2^-11 + 2^-20 (Section 5.6, Lemma 5.2). So

    Pr[output = s] >= 1 - 2^-20 - 2^-10 - 2^-11 - 2^-20 >= 1 - 2^-8 > 2/3.

The finite branch succeeds with probability at least 1 - 2^-10. These are
additive couplings. There is no conditioning on favorable labels, caps or
outcomes.

## 13. Resources on every branch

Throughout, n >= 1024; the finite branch is O(1). From Section 7: m <= mu <= 2 rho, h_m <= hmax,
2^hmax < 16 * 2^((14411/10000) sqrt n), kappa + 1 = O(log2 n), 2^kappa <= 32 rho, Lam <= 2 rho, w < x rho + 1, and every
lam_i, l_i, b_i is at most 8 rho.

Sizes. log2 nq <= hmax + log2(kappa + 1) = O(sqrt n), K = O(sqrt n), J + 1 <= n and a2 <= n, so
(kappa+1)((J+1)K + 2 a2) = O(n^(3/2) log2 n) and Q* = O(n^(3/2) (log2 n) 2^((14411/10000) sqrt n)). Also
log2 Qcap = O(sqrt n), so h_e = O(sqrt n), and h_A, T_V = O(log n).

Q. On every branch, Q <= Qcap = 1024 Q* = O(n^(3/2) (log2 n) 2^((14411/10000) sqrt n)).

Core steps. By Lemma 11.2, O(n^2 log n) Qcap = O(n^(7/2) (log2 n)^2 2^((14411/10000) sqrt n)). The decoder term
O(n^(5/2) nq) = O(n^(5/2) (log2 n) 2^((14411/10000) sqrt n)) is smaller, and the poly(n) setup is O(2^((14411/10000) sqrt n)).

S_Q. The depth-first stack holds at most 4 index registers per level (3 finished siblings and the vector being
built), each of at most Lam <= 2 rho qubits, over at most mu + 1 <= 2 rho + 1 levels: at most
8 rho (2 rho + 1) <= 20 n qubits. A merge adds O(sqrt n) qubits of registers and scratch. LE uses O(n) qubits
(data, ancilla, arithmetic), and the data register is reset after each call. Transforms use O(n), and each
root qubit is measured at once. Released registers are reused. So S_Q = O(n).

S_C. The depth-first stack holds at most five tables per level (up to three finished siblings, the table being
built or merged, and one merge output), each of at most 2^Lam entries with high parts of at most 3n bits and a
common residue of at most n bits: 5(mu+1)(3n 2^Lam + n) = O(n^(3/2) 2^(kappa + w)) = O(n^2 2^w) bits, as
mu = O(sqrt n) and 2^kappa = O(sqrt n). Binary merge scratch is O(2^Lam sqrt n) bits (Section 6.2); MERGE4I
scratch is O((2^Lam + Cp)(Lam + b)) bits (Section 6.3) with Cp <= 2^(Lam + kappa + 3) + 1, which is
O(sqrt n 2^(2 kappa + w)) = O(n^(3/2) 2^w). The decoder stores K triples (W_i, beta_i, Z_i) and K running
residues of O(n) bits each, and enumerates its candidates without storing them. The table of Section 4 is O(1),
counters and parameters are O(n) bits, and LE uses O(n log n) classical scratch (Section 5.3) and the fallback
counter. Since 2^w < 2 * 2^((21/20) sqrt n), S_C = O(n^2 2^((21/20) sqrt n)). These are fixed allocations, so the bound holds on
every branch, including when labels are wrong; the work of each MERGE4I attempt is bounded through its step 2.

T. By (2.1), with log2(S_C + S_Q + 2) = O(sqrt n),
T = O(n^(7/2) (log2 n)^2 2^((14411/10000) sqrt n)) * O(sqrt n) + (n+1) Qcap = O(n^4 (log2 n)^2 2^((14411/10000) sqrt n)).

All four bounds hold simultaneously for the same execution, with absolute constants independent of N, s and
outcomes.

## 14. Exact growth indices and declared envelopes

The envelopes are

    B_T(n) = n^4 (log2 n)^2 2^((14411/10000) sqrt n),     B_C(n) = n^2 2^((21/20) sqrt n),
    B_Q(n) = n,                                   B_samples(n) = n^(3/2) (log2 n) 2^((14411/10000) sqrt n).

By Section 13 the resources are O of these; the finite branch n < 1024 is O(1). The coefficient 14411/10000 is a
rational upper bound for the height coefficient tau = sqrt(1241/200) - 21/20 of Lemma 7.0; no larger exponent is absorbed,
because 2^hmax < 16 * 2^((14411/10000) sqrt n) directly. For B(n) = 2^(a sqrt n) n^pw (log2 n)^lw with a > 0 and
pw, lw >= 0, log2 B = a sqrt n + O(log n), so log2 log2 B = (1/2) log2 n + log2 a + o(1) and g(B) = 1/2. For
B_Q(n) = n, log2 log2 n / log2 n -> 0, so g = 0. The structured objects in submission.json are exactly these
envelopes.

## 15. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy
is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does
not assert that robustness is impossible.
