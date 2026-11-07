# MW4: Schroeppel-Shamir four-input collimation, S_C ~ 2^((3/4) sqrt n), T and Q ~ 2^((15557/10000) sqrt n), O(n) qubits

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single
algorithm MW4 below, in the configuration with the fixed rational x0 = 14997/20000, receives N in
binary and fresh independent copies of rho_s, and outputs the entire s with unconditional
probability at least 1 - 2^-8 > 2/3. On EVERY execution branch (including every failure, retry,
discard and abort) it satisfies jointly the proved bounds, with c0 = 2/(3 x0) + 8 x0/9 = 174970003/112477500,

    T   = O(n^(9/2) (log2 n) 2^(c0 sqrt n)),
    S_C = O(n^2 2^(x0 sqrt n)),
    S_Q = O(n),
    Q   = O(n^(3/2) (log2 n) 2^(c0 sqrt n)).

Since c0 < 15557/10000 and x0 < 3/4, these imply the declared envelopes (Section 14)

    T = O(2^((15557/10000) sqrt n)),  S_C = O(2^((3/4) sqrt n)),  S_Q = O(n),  Q = O(2^((15557/10000) sqrt n)),

with exact growth indices 1/2, 1/2, 0, 1/2. All outside constants are absolute. The fifth claim is
the clean-input tolerance 0 (Section 15). All logarithms are base 2.

Notation used throughout:
- d = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known integer. A "multiplier" W is an integer frequency factor.
- hd denotes a Hamming distance. T denotes total work only.

## 1. Provenance and what is new

MW4 is the CW1 algorithm (public Yukon submission cfe82a87-0d65-454e-b1df-4789dc95aab4) with a new
merge at the upper tree levels and a new schedule. CW1 is itself a schedule modification of CS1 (public
submission b56c7ceb-de59-42da-9e3b-6ee96e4e4145 by AdamGagol, identical to
f1481815-9577-4990-abe3-7b79fa5d9284). Sections 2-6.2, 9, 10 and 15 are CS1's text, reproduced so the
argument is self-contained. Not new here: the binary linear merge with closed-form rank, the free-frequency
decoder, Kitaev-test label extraction with randomized verification, the source-data shifts and the
top-bit factorization. The collimation step and the distribution-free remainder argument are from
G. Kuperberg, "Another subexponential-time quantum algorithm for the dihedral hidden subgroup problem",
arXiv:1112.3333v1, Algorithm 4.1, Proposition 4.2 and Section 4.6. CS1 credits the earlier COL3 submission
on this challenge for label extraction (Kitaev, quant-ph/9511026), the top-bit argument, the CRT unit
multiplier and the exhaustive finite branch. No earlier verdict is a premise; every step is proved below.

This configuration uses the merge, schedule and proof of my repaired MW4 row at x = 1/2 (3e22e7d7-71e7-41c5-8a64-03b415e0e2a2), with different fixed constants.

New here (Sections 6.3, 7, 8.1, 11, 13 and 14):
- MERGE4, a four-input collimation step. Its fiber is enumerated by the Schroeppel-Shamir two-heap method
  (R. Schroeppel and A. Shamir, "A T = O(2^(n/2)), S = O(2^(n/4)) algorithm for certain NP-complete
  problems", SIAM J. Comput. 10(3), 1981), in time about the square of the table length and in memory
  about the table length, on every branch.
- Lemma 8.2, a pairwise-independence bound on the unstored part of a fiber.
- A four-phase schedule. At table length 2^w, a four-input level cancels about 3w bits per doubling pair
  (1.5 w bits per doubling of the tree), where a capped binary level cancels about w bits per doubling.

This improves the binary width-capped trade-off coefficient 1/x + x/2 to 2/(3x) + 8x/9 at the same memory
exponent x, for x^2 <= 3/5. It does not improve the uncapped sqrt(2) coefficient of Kuperberg's collimation
sieve and is not a sub-1/2 result. The comparison is with public rows on this challenge. No claim is
made that the combination is absent from the wider literature.

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
(Cf+1)-st one, MW4 stops, releases everything and outputs 0 (ABORT).

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
exp(1) EX/x <= exp(1) (sqrt n + 1)/n <= exp(1) * 9/64 < 1/2 for n >= 64, since
(sqrt n + 1)/n decreases. Also Cf >= 20, because Qcap >= 6144 * 2^hmax >= 6144 * 2^(6t) >= 20 (sqrt n + 1), with hmax and t from Section 7, since t >= sqrt(n)/27 and sqrt n >= 1024.
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

IDEAL run. The ideal run is MW4 in the latent-label model with every LE output
replaced by the latent k and without the cap of 5.5. The actual and ideal runs
can be coupled to coincide unless some LE call returns a wrong label or ABORT
occurs, so every event's probability differs between them by less than
2^-11 + 2^-20. Resource bounds are proved for every ACTUAL branch directly,
because they rest only on caps and fixed allocations.

## 6. Phase vectors, the linear merge and the four-input merge

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

### 6.3 MERGE4(X1, X2, X3, X4; p, b, lam', kap)

Precondition: X1..X4 are phase vectors from pairwise disjoint sets of copies, all of length L = 2^lam, collimated
to p, with index registers x1..x4 and tables lab_t[x] = c_t + 2^p h_t[x], 0 <= c_t < 2^p. Also
b = 4 lam - lam' - kap >= 1, kap >= 0 and lam >= kap + 2 and lam' <= lam + 1. Put

    mu4 = 2^(4 lam - b) = 2^(lam' + kap),   Cp = 2 mu4 + 1,   car = floor((c_1 + c_2 + c_3 + c_4)/2^p) in {0,1,2,3},

and residues a_t[x] = h_t[x] mod 2^b. Bits p..p+b-1 of a tuple's label sum are
r(x1,x2,x3,x4) = (a_1[x1] + a_2[x2] + a_3[x3] + a_4[x4] + car) mod 2^b.

1. LOOKUP each a_t into a fresh b-bit register, add the four registers and car (mod 2^b) cleanly into a fresh
   register Rz, and clear the four registers by repeating the lookups. Measure Rz, obtaining e, and reset Rz from
   that known value. Let S_e be the set of tuples with r = e, and sz = |S_e|. Put tau = (e - car) mod 2^b.
2. Classical enumeration of a list Tl of tuples.
   - STREAM A produces all L^2 pairs (x1,x2) in nondecreasing order of the integer a_1[x1] + a_2[x2]: merge-sort
     the x2 by (a_2[x2], x2), then keep a binary min-heap holding, for each x1, its next unread position in
     that order. STREAM B produces all pairs (x3,x4) in nonincreasing order of a_3[x3] + a_4[x4], in the same way
     with a max-heap. Each stream holds O(L) heap entries of O(b + lam) bits.
   - The integer a_1 + a_2 + a_3 + a_4 lies in [0, 4 * 2^b) and is congruent to tau modulo 2^b exactly on S_e, so it
     equals tau_g = tau + g 2^b for one g in {0,1,2,3}. For g = 0,1,2,3 in order, restart both streams and
     run a two-pointer scan with heads vA and vB: if vA + vB < tau_g pop A; if vA + vB > tau_g pop B;
     if they are equal, read the whole run of A with value vA, keeping its first min(run length, Cp) pairs in a
     buffer Buf, and then read the run of B with value vB, and for each read pair (x3,x4) and each entry (x1,x2) of Buf
     append (x1,x2,x3,x4) to Tl. Stop the whole enumeration as soon as |Tl| = Cp. A scan ends when a stream is exhausted.
   Claim: if sz <= Cp then Tl lists S_e exactly once each; if sz > Cp then Tl is a list of exactly Cp
   distinct elements of S_e. Indeed every element of S_e belongs to exactly one (g, vA, vB) with vA + vB = tau_g
   and is formed from one pair of that A run and one pair of that B run. A run of A is truncated only if it
   has more than Cp pairs, and then the first pair read from its nonempty B run fills Tl to Cp, in which case
   sz > Cp. So with no stop all of S_e is listed, and with a stop exactly Cp distinct elements are.
   The memory used is deterministic; only residues and index order are read.
   Let tl = |Tl| = min(sz, Cp).
3. Let R have ceil(log2(Cp + 1)) bits, with a one-qubit flag Rf. Both start at 0. For each row rho of Tl compute the flag
   [(x1,x2,x3,x4) = Tl[rho]] with a Toffoli chain on O(lam) scratch, CNOT it into Rf and CNOT it onto the bits of R where
   rho has a 1, and uncompute the chain. Since the rows are distinct, on Tl R = rho and Rf = 1, and elsewhere R = Rf = 0.
   Measure Rf. If Rf = 0 declare FAIL.
4. Measure bl = floor(R / 2^lam'). If (bl + 1) 2^lam' > tl declare FAIL.
5. For v in [0, 2^lam'), LOOKUP v -> Tl[bl 2^lam' + v] on the low lam' bits of R, XORing into x1..x4, which become |0>.
   Reset those registers, Rf and the high bits of R from their known values.
6. Output the low lam' bits of R as the index register, with table lab[v] the sum of the four input labels of
   Tl[bl 2^lam' + v], stored as in STORAGE with p+b in place of p: put sv = h_1 + h_2 + h_3 + h_4 + car at that tuple, which is
   congruent to e modulo 2^b, and store the common residue c' = c_1 + c_2 + c_3 + c_4 - car 2^p + 2^p e in [0, 2^(p+b)) and
   the high parts hi'[v] = floor(sv/2^b).

On FAIL all inputs and registers are reset and released, and the inputs are never reused. All registers have fixed
widths.

Correctness (ideal run). Before step 1 the state is the product of the four inputs: equal magnitudes over all L^4 tuples,
with phases 2 pi (sum of labels) th. Steps 1, 3 and 4 compute functions of the tuple into clean registers and measure
them. So after step 4 the state is the equal-magnitude superposition over the 2^lam' tuples of block bl, with their
original phases. Step 5 maps each to its v bijectively. The output is thus a phase vector with table lab, and every label
is congruent to c' modulo 2^(p+b), so it is collimated to p+b.

Lemma 6.2 (failure identity). For ANY input tables collimated to p, the measurement laws of steps 1, 3 and 4 depend
only on the a_t and car, that is on label bits below p+b, and

    Pr[FAIL] = sum_e [ (sz_e - tl_e) + (tl_e mod 2^lam') ] / L^4,    tl_e = min(sz_e, Cp).

Hence Pr[FAIL] <= 2^(-kap) + sum_e (sz_e - tl_e) / L^4.

Proof. Each measurement is a computational-basis measurement of a function of the tuple on an equal-magnitude
superposition, so its law is a ratio of counts, independent of phases. The outcome e has probability sz_e/L^4. Given e,
Rf = 0 has probability (sz_e - tl_e)/sz_e. Given Rf = 1, R is uniform on [0, tl_e), and step 4 fails with probability
(tl_e mod 2^lam')/tl_e. Multiplying and summing gives the identity. The second term sums to at most
2^b (2^lam' - 1)/L^4 < 2^(b + lam' - 4 lam) = 2^(-kap). QED.

Cost. Each stream makes at most 4 L^2 pops over the four scans, each with O(lam) comparisons of O(b + lam)-bit keys.
Appends total at most Cp, and each Buf write and each Tl write is O(lam) bits. There are eight lookup passes of L rows with O(b + lam)-bit
fields, one pass of tl <= Cp rows with O(lam) control bits, one pass of 2^lam' rows, and 2^lam' additions of high parts of
O(n) bits. With lam, b = O(sqrt n) (Section 7) and Cp <= 2^(lam + kap + 2) + 1 <= 2 L^2 this is O(n L^2) core steps on every
branch. Quantum scratch is O(sqrt n) beyond the four index registers. Classical scratch, including Tl and Buf, is
O((L + Cp) sqrt n) bits.

## 7. The tree TREE_D

Throughout, n >= 2^20 (the main branch of Section 11), so rho := sqrt n >= 1024. Input: a supplier of LEAF QUBITS. Each is a
positive qubit with a known label uniform on [0, 2^D), D >= 2, independently. Put B = D - 1 <= n, the number of bits to collimate.

Global parameters, functions of n only, computed by exact integer arithmetic:

    x0 = 14997/20000,   t = least integer with 3t >= x0 rho,
    y* = 0 if n <= 15 t^2, else ceil((n - 15 t^2)/(9 t)),
    mu = 5t + y* + 1,   kappa = ceil(log2 mu) + 2.

So 4 mu <= 2^kappa <= 8 mu. Levels are numbered i = 0, 1, ..., mu - 1. Level i has arity f_i and input table
exponent lam_i. Define these and the capacities bmax_i = f_i lam_i - lam_(i+1) - kappa by:

    Phase A, 0 <= i <= 3t-1:   f_i = 2, lam_i = kappa + 1 + i,           bmax_i = i.
    Phase B, 3t <= i <= 4t-1:  f_i = 2, lam_i = kappa + 1 + 3t,          bmax_i = 3t + 1 (i < 4t-1), bmax_(4t-1) = 4t + 1.
    Phase C, 4t <= i <= 5t-1:  f_i = 4, lam_i = kappa + 1 + 2t + (i-4t), bmax_i = 2 kappa + 2 + 6t + 3(i-4t).
    Phase D, i >= 5t:          f_i = 4, lam_i = kappa + 1 + 3t,          bmax_i = 2 kappa + 3 + 9t.

The values bmax_i are direct substitutions. For instance at i = 4t-1: 2(kappa+1+3t) - (kappa+1+2t) - kappa = 4t + 1. In Phase C:
4 lam_i - (lam_i + 1) - kappa = 3 lam_i - 1 - kappa. In Phase D: 3 lam_i - kappa.

Heights: h_0 = 0 and h_(i+1) = h_i + log2 f_i. So h_i = i for i <= 4t and h_i = 4t + 2(i - 4t) for i >= 4t. A node of level i
has 2^(h_i) leaf vectors below it. Two facts hold, by substitution:

    binary levels:      lam_i <= kappa + 1 + h_i;
    four-input levels:  2 lam_i <= 2 kappa + 2 + h_i.                                 (7.0)

The second is an equality in Phase C. In Phase D it holds because h_i >= 6t.

A tree with m levels (1 <= m <= mu) uses level m-1 as its ROOT, with output exponent lam_m := 1 and capacity
rootcap_(m-1) = f_(m-1) lam_(m-1) - 1 - kappa. Its total capacity is Sum(m) = sum_(i < m-1) bmax_i + rootcap_(m-1). Per tree, m is the least m with Sum(m) >= B.

Capacity of the full schedule. The three phases sum to S_A = 3t(3t-1)/2, S_B = (t-1)(3t+1) + 4t + 1 = 3t^2 + 2t and
S_C = t(2 kappa + 2 + 6t) + 3t(t-1)/2 >= 15 t^2/2 + t/2. Their total is at least 15 t^2. Each Phase D level adds at least 9t, so
Sum(mu) >= 15 t^2 + 9 t y* >= n >= B. Hence m <= mu for every tree.

Height bound. Put hmax = h_mu = 6t + 2 y* + 2. Note x0 rho/3 <= t < x0 rho/3 + 1. If n > 15 t^2 then y* < (n - 15 t^2)/(9t) + 1, so

    hmax < 6t + 4 + 2n/(9t) - 10t/3 = (8/3) t + 2n/(9t) + 4 < (8/9) x0 rho + 8/3 + (2/(3 x0)) rho + 4 < c0 rho + 7.

If n <= 15 t^2 then y* = 0 and hmax = 6t + 2 < 2 x0 rho + 8 <= c0 rho + 8, because c0 - 2 x0 = 2/(3 x0) - (10/9) x0 >= 0 when
x0^2 <= 3/5, which holds here. So in all cases

    h_m <= hmax < c0 rho + 8,   and   2^(h_m) <= 2^hmax < 2^8 2^(c0 rho).              (7.1)

Size bounds. Here 1/9 <= x0 <= 3/4 and c0 <= 31/5, so:
- rho/27 <= t <= x0 rho/3 + 1 <= (0.26) rho, and y* <= rho/(3 x0) + 1 <= 3 rho + 1, hence mu <= 5 rho.
- 2^kappa <= 8 mu <= 40 rho. Also kappa <= log2(5 rho) + 3 <= rho/64, which holds at rho = 1024 (15.33 <= 16) and thereafter. So kappa <= t.
- Every lam_i <= kappa + 1 + 3t <= rho. Every bit count is at most rootcap <= 4 lam_i - 1 - kappa <= 3 kappa + 3 + 12t <= 4 rho. So lam_i, b_i = O(sqrt n).
- hmax <= 7 rho.

Allocation. Allocate b_(m-1), b_(m-2), ..., b_0 in that order greedily, with b_(m-1) = min(rootcap_(m-1), B) and then
b_i = min(bmax_i, B - already allocated). Then sum_i b_i = B, and some low levels may get smaller values or 0. Put p_0 = 0 and p_(i+1) = p_i + b_i, so p_m = B.
Let nq_D = 2^(h_m) (kappa + 1) be the number of leaf qubits per tree.

Lemma 7.1 (four-input levels are full). In any tree with a level i >= 4t, all levels i >= 3t get their full capacity. In particular every four-input
level has b_i = f_i lam_i - lam_(i+1) - kappa exactly, with lam_m = 1 at the root.

Proof. Here m >= 4t + 1 >= 2, so Sum(m-1) < B by minimality of m. Hence the deficit Sum(m) - B is less than Sum(m) - Sum(m-1) =
bmax_(m-2) + rootcap_(m-1) - rootcap_(m-2) = rootcap_(m-1) + 1 - lam_(m-1) <= rootcap_(m-1) <= 3 kappa + 3 + 12 t <= 15 t + 3. And the levels i < 3t have total
capacity S_A = (9 t^2 - 3t)/2 >= 15 t + 3 since t >= 37. The greedy allocation meets all levels i >= 3t in full before it reaches
Phase A, since B minus their total capacity is S_A minus the deficit, which is >= 0. QED.

Failure budgets. For a binary level, b_i + lam_(i+1) - 2 lam_i <= -kappa, so Lemma 6.1 gives Pr[FAIL] <= 2^-kappa for any input tables. For a
four-input level, Lemma 7.1 gives the exact precondition of MERGE4 with kap = kappa. Its other preconditions are direct: lam_i >= kappa + 1 + 2t >= kappa + 2, and lam_(i+1) <= lam_i + 1.

LEAF: take kappa+1 leaf qubits as the index register (bit j = qubit j). Build the table incrementally, lab[0] = 0 and lab[x + 2^j] = lab[x] + k_j for x < 2^j:
one addition per entry. The table has length 2^(lam_0), is collimated to p_0 = 0, and in the ideal run is exactly the tensor product state.

Field widths. A level-i label is a sum of at most 2^(h_i) (kappa+1) leaf labels below 2^(B+1), so it is below 2^(B+1+h_i+gw) with gw = ceil(log2(kappa+1)). Level-i tables are
collimated to p_i and stored with w_i = B + 1 + h_i + gw - p_i bits per high part, at most 3n.

VEC(i): if i = 0 return LEAF. Otherwise repeat:
- build the f_(i-1) inputs X1, ..., X_(f_(i-1)), each by VEC(i-1);
- out = MERGE(X1, X2; p_(i-1), b_(i-1), lam_i) if f_(i-1) = 2, and out = MERGE4(X1, X2, X3, X4; p_(i-1), b_(i-1), lam_i, kappa) if f_(i-1) = 4;
- if out != FAIL, return out.

TREE_D returns VEC(m), a one-qubit phase vector with labels lab[0] and lab[1], congruent modulo 2^B. Its ideal state is, up to global phase,
(|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2 with the known integer

    W = (lab[1] - lab[0]) / 2^B = hi[1] - hi[0],                              (7.2)

because the root table is collimated to p_m = B. Each label is a sum of at most nq_D leaf labels below 2^(B+1), so |W| < 2 nq_D.
Depth-first evaluation holds at most f_i - 1 <= 3 finished siblings per level.

## 8. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and
tau_j in {0,1}. Since k_j is uniform on [0, 2^(B+1)), low_j and tau_j are
independent and tau_j is a fair bit. Let Gt be the sigma-field generated by:
- all low_j of the tree's leaves, including those of discarded attempts;
- all measurement outcomes (e, Rf, bl) of its merges;
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
sort key, enumeration, rank and block partition uses only label bits below position B,
since Sections 6.2 and 6.3 read bits p..p+b-1 with p + b <= B, together with index
order. Bits below B of a sum of leaf labels depend only on the low_j: adding
multiples of 2^B does not change them. By Lemmas 6.1 and 6.2, each measurement's
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

### 8.1 Mid-tree factorization and the unstored part of a MERGE4 fiber

Lemma 8.2. In the ideal run, consider a MERGE4 attempt at level i, with p = p_i, b = b_i, lam = lam_i and lam' = lam_(i+1), and let Fp be the sigma-field generated by the bits below position p of the leaf labels of its inputs, all decisions, measurement outcomes and FAIL or retry events in the subtrees of its inputs, and everything from other copies. Fp does NOT contain any label bit at or above position p, so it does not determine the completed input tables. Then Pr[FAIL | Fp] <= 2^(-kappa) + 2^(-kappa - lam') <= 2^(1 - kappa).

The bound is not claimed conditional on the completed tables, and it would be false there: if all residues and the carry were zero, one fiber would contain every tuple and the merge would fail with probability close to 1. It holds after averaging over bits p..p+b-1, and that is all Lemma 11.1 uses.

Proof. Let Lv be the set of leaves of the four inputs, a union of four pairwise disjoint sets. For j in Lv write k_j = l_j + 2^p g_j + 2^(p+b) u_j with 0 <= l_j < 2^p and 0 <= g_j < 2^b. This is possible as p + b <= B < D, and k_j uniform makes l_j, g_j, u_j independent and uniform.

Factorization. Every earlier step of the tree that involves a leaf of Lv is a merge at a lower level, with p' + b' <= p, or a leaf-acceptance test or a controller decision. By Lemmas 6.1 and 6.2 and Section 6, those laws, residues, sort keys, ranks, enumerations and block choices read only label bits below p, and bits below p of a sum of leaf labels depend only on the l_j. Steps elsewhere use disjoint copies. So, exactly as in the proof of Lemma 8.1 with p in place of B, conditional on Fp the g_j (j in Lv) are i.i.d. uniform on [0, 2^b). The incidence vector I(tau) subset of Lv of each tuple tau and the integer f(tau) = floor((sum_(j in I(tau)) l_j)/2^p) are Fp-measurable. Distinct tuples have distinct incidence vectors, by the concatenation and re-indexing argument above, so at most one tuple has I(tau) empty.

Moments, all conditional on Fp. The value measured in step 1 for a tuple tau is r(tau) = (f(tau) + sum_(j in I(tau)) g_j) mod 2^b. Fix e, and let S count the tuples with I(tau) nonempty and r(tau) = e. For nonempty I(tau), r(tau) is uniform, so E S <= L^4 2^-b = mu4 (with mu4 = 2^(4 lam - b) = 2^(lam' + kappa) by Lemma 7.1). For distinct nonempty I and I', there is j in the symmetric difference, say j in I' \ I, and there is i' in I. The map (g_(i'), g_j) -> (r, r'), with other coordinates fixed, has matrix [[1,0],[1,1]] if i' in I', and the identity otherwise. Both are invertible over Z/2^b, so (r, r') is uniform on (Z/2^b)^2. The indicators are thus pairwise independent, and Var S <= E S <= mu4.

Overflow. sz_e <= S + 1, and Cp = 2 mu4 + 1, so sz_e - tl_e = (sz_e - Cp)_+ <= (S - 2 mu4)_+. If S > 2 mu4, then S - E S >= S - mu4 > mu4 and S - 2 mu4 <= S - E S <= (S - E S)^2 / mu4. So E (sz_e - tl_e) <= Var S / mu4 <= 1. Summing over the 2^b values of e, E sum_e (sz_e - tl_e) / L^4 <= 2^b / L^4 = 2^(-lam' - kappa). Lemma 6.2 holds for every table. Averaging it over the g_j given Fp gives the bound. QED.

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

Finite branch (n < 2^20). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand
at the first minus outcome. Output the first cand with no rejection, or 0.
- For cand = s every outcome is plus.
- For cand != s the two data branches are orthogonal, so each outcome is uniform.
- A union bound over cand gives Pr[wrong] <= N 2^-(n+10) <= 2^-10.
- Since N <= 2^(2^20), Q <= N(n+10) and all other resources are bounded by absolute constants.

Main branch (n >= 2^20). Compute a2, M, d, J, K and all tree parameters. The values t, y*, mu, kappa and hmax are those of Section 7, and m <= mu and h_m <= hmax for every B <= n used.
Let Rs = J + 1, or Rs = 0 if M = 1. Put

    Q* = 6 * 2^hmax (kappa+1) (Rs K + 2 a2) + 2 a2,    Qcap = 1024 Q*,

and then h_e, h_A, t_V and Cf from Section 5. Here K in Section 9 is computed with nq = nq_d. A binary down-counter of acquisitions is kept,
at amortized O(1) bit flips per acquisition. MW4 stops, releases everything and outputs 0 before an acquisition would exceed Qcap. Otherwise it runs
Section 9 and then Section 10. Parameter, CRT and table computations are polynomial in n.

Lemma 11.1 (expected ideal acquisitions). In the ideal UNCAPPED run, the expected number of acquisitions is at most Q*.

Proof. An accepted leaf qubit needs at most 2 acquisitions in expectation (acceptance probability > 1/2 in Section 9, and 1 in Section 10). Let Qv_i be the
expected number of acquisitions until VEC(i) returns. Each attempt at a level uses only fresh copies and fixed parameters, and its decisions, acquisitions and FAIL event are functions of those copies' labels and fresh coins. So, in the ideal run, successive attempts at a level are i.i.d. and independent of everything before them, whatever the past. Let p_i be the failure probability of one attempt, averaged over its own copies. Then p_i <= 2^(1-kappa) <= 1/(2 mu): at a binary level by Lemma 6.1, which holds for all tables, and at a level with more inputs by taking the expectation of Lemma 8.2 over Fp. No bound conditional on completed tables is used. By Wald's identity for the i.i.d. attempts, Qv_(i+1) <= rt f_i Qv_i, where rt = 1/(1 - 1/(2 mu)). Moreover
rt^m <= exp(m/(2 mu - 1)) <= e < 3 for m <= mu. So Qv_m <= 3 * 2^(h_m) * 2(kappa+1) <= 6 * 2^hmax (kappa+1). The odd part runs Rs K trees. Section 10 needs, per bit, an expected 2 trees by (8.3), or,
when wd = 1, an expected 2 single acquisitions since kk is uniform on {0,1}. Summing gives the bound. QED.

Lemma 11.2 (work per branch). On every actual branch of the main branch, the number of core steps is at most O(n^(5/2)) Qcap + O(n^(5/2) nq) + poly(n), where nq = nq_d.

Proof. Charge every core step to an acquisition, or to the fixed-length loops.
- Each acquisition (transform, acceptance test, X, counter update) takes O(n^2) core steps. All LE calls together take O(n^2 log n) Qcap + O(n^(5/2)) core steps on every branch (Section 5.6), since there is one LE call per acquisition and Q <= Qcap.
- A leaf table of 2^(kappa+1) entries costs O(n 2^(kappa+1)). Charged to its kappa+1 acquisitions, that is O(n 2^kappa), which lies in O(n^2), per acquisition.
- A binary merge attempt at level i costs O(n (2^(lam_i) + 2^(lam_(i+1)))) = O(n 2^(kappa + 1 + h_i)) by Section 6.2 and (7.0), since lam_(i+1) <= lam_i + 1. Its two inputs were built from 2^(h_i + 1)(kappa+1) acquisitions that no other attempt at that level uses, since inputs of a failed merge are discarded and never reused. That is O(n 2^kappa) = O(n^(3/2)) per acquisition per level.
- A four-input merge attempt at level i costs O(n 2^(2 lam_i)) = O(n 2^(2 kappa + 2 + h_i)) by Section 6.3 and (7.0). Its four inputs were built from 2^(h_i + 2)(kappa+1) acquisitions that no other attempt at that level uses. That is O(n 2^(2 kappa)) = O(n^2) per acquisition per level, because 2^kappa <= 40 sqrt n.
- Each acquisition lies below at most mu merge attempts, one per level, with mu = O(sqrt n). So the total merge share is O(n^(5/2)) per acquisition.
- Root measurements and bookkeeping are O(n) per tree, and each tree uses at least one acquisition.
- The decoder's fixed loops cost Rs * 2^(ceil(log2 nq)+8) * K * O(n) = O(n * nq * sqrt n * n) core steps, since Rs <= n and K = O(sqrt n).
- Setup is poly(n) and runs once. It covers the parameters, extended Euclid and CRT for at most n stages, the Mult constants, Q*, h_e, the table of Section 4, the Section 10 shift values, and the decoder's initial residues (f_i c) mod 2^(P_j).

Every loop is either fixed-length or consumes acquisitions, so every branch terminates with this many core steps. QED.

## 12. Success probability

In the ideal UNCAPPED run, the odd part errs with probability at most 2^-20 (Section 9), and Section 10 then never errs. By Markov and Lemma 11.1, the source cap is reached
in the ideal run with probability at most 1/1024. Capping changes the run only on that event. The actual run differs from the ideal one only if some LE call
returns a wrong label or the high-confidence cap aborts, which has probability below 2^-11 + 2^-20 (Section 5.6, Lemma 5.2). So

    Pr[output = s] >= 1 - 2^-20 - 2^-10 - 2^-11 - 2^-20 >= 1 - 2^-8 > 2/3.

The finite branch succeeds with probability at least 1 - 2^-10. These are additive couplings. There is no conditioning on favorable labels, caps or outcomes.

## 13. Resources on every branch

Throughout, n >= 2^20; the finite branch is O(1). We use Section 7: mu <= 5 rho, 2^hmax < 2^8 2^(c0 rho), kappa + 1 = O(log2 n), 2^kappa <= 40 rho, and lam_i, b_i = O(rho).

Sizes. log2 nq = O(sqrt n), K = O(sqrt n), Rs <= n and a2 <= n. So (kappa+1)(Rs K + 2 a2) = O((log2 n) n^(3/2)) and Q* = O(n^(3/2) (log2 n) 2^(c0 sqrt n)). Also log2 Qcap = O(sqrt n), so h_e = O(sqrt n), and h_A, T_V = O(log n).

Q. On every branch, Q <= Qcap = 1024 Q* = O(n^(3/2) (log2 n) 2^(c0 sqrt n)).

Core steps. By Lemma 11.2, O(n^(5/2)) Qcap = O(n^4 (log2 n) 2^(c0 sqrt n)). The decoder term O(n^(5/2) nq) = O(n^(5/2) (log2 n) 2^(c0 sqrt n)) is smaller, and the poly(n) setup is O(2^(c0 sqrt n)).

S_Q. The depth-first stack holds at most 4 index registers per level, of at most lam_i <= rho qubits each, so at most 4 mu rho <= 20 n index qubits (Section 7). A merge adds O(sqrt n) qubits of registers and scratch. LE uses O(n) qubits (data, ancilla, arithmetic), and the data register is reset after each call. Transforms use O(n), and each root qubit is measured at once. Released registers are reused. So S_Q = O(n).

S_C. At any time the depth-first stack holds at most five tables per level (up to three finished siblings, the table being built or merged, and one merge output).
Every table has at most 2^(lam_max) entries with lam_max = kappa + 1 + 3t, since every lam_i is at most that. Each stored high part has at most 3n bits, and each common residue at most n bits. So the tables use at most
5(mu+1)(3n 2^(lam_max) + n) = O(n^(3/2) 2^(kappa + 3t)) = O(n^2 2^(3t)) bits, using mu = O(rho) and 2^kappa = O(rho).
- Binary merge scratch is O(2^(lam_max) sqrt n) bits (Section 6.2). MERGE4 scratch is O((2^(lam_max) + Cp) sqrt n) bits (Section 6.3), with Cp <= 2^(lam_max + kappa + 1) + 1, which is O(n^(3/2) 2^(3t)) bits because 2^(2 kappa) = O(n).
- The decoder stores K triples (W_i, beta_i, Z_i) and K running residues, all O(n) bits each. Its candidates are enumerated, never stored.
- The table of Section 4 is O(1). Counters and parameters are O(n) bits. LE uses O(n log n) classical scratch (Section 5.3) and the fallback counter.

Since 3t < x0 rho + 3, we get S_C = O(n^2 2^(x0 sqrt n)). These are fixed allocations, so the bound holds on every branch, including when labels are wrong: the enumeration of Section 6.3 uses the same memory for every input table.

T. By (2.1), with log2(S_C + S_Q + 2) = O(sqrt n), T = O(n^4 (log2 n) 2^(c0 sqrt n)) * O(sqrt n) + (n+1) Qcap = O(n^(9/2) (log2 n) 2^(c0 sqrt n)).

All four bounds hold simultaneously for the same execution, with absolute constants independent of N, s and outcomes.

## 14. Exact growth indices and declared envelopes

The declared envelopes are

    B_T(n) = 2^((15557/10000) sqrt n),   B_C(n) = 2^((3/4) sqrt n),   B_Q(n) = n,   B_samples(n) = 2^((15557/10000) sqrt n).

Absorption. Here c0 = 174970003/112477500 < 15557/10000 and x0 = 14997/20000 < 3/4. For fixed reals a < a' and fixed P, the quantity n^P (log2 n)^P 2^(a sqrt n) / 2^(a' sqrt n) tends to 0, so n^P (log2 n)^P 2^(a sqrt n) = O(2^(a' sqrt n)).
Applying this to Section 13 gives T = O(B_T), S_C = O(B_C), Q = O(B_samples) and S_Q = O(B_Q). The finite branch is O(1) and is absorbed. Thus each resource is O of its envelope, uniformly over N and s of bit length n.

The Section 13 bounds are the sharper statements proved; the declared envelopes are their pure exponential upper bounds. For B(n) = 2^(a sqrt n) with a > 0, log2 log2 B = (1/2) log2 n + log2 a, so g(B) = 1/2. For B_Q(n) = n, log2 log2 n / log2 n -> 0, so g = 0. The structured objects in submission.json are exactly these envelopes.

## 15. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy
is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does
not assert that robustness is impossible.
