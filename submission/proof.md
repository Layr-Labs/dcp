# MWG13: Grover-listed many-input collimation at classical-memory growth index 1/3, T and Q = O(2^((4083/10000) sqrt(n log2 n))), S_C = O(n^4 2^((1/65536) n^(1/3))), O(n) qubits

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N) and Vn = sqrt(n log2 n). The single algorithm MWG13 below (the MWG algorithm of
submission 76d06063, specified in full in Sections 5-11 below, in the configuration alpha = 1/3, c1 = 20413/50000, table constant 2^-16), receives N in binary and fresh independent copies of rho_s, and outputs the entire s with unconditional
probability at least 1 - 2^-8 > 2/3. On EVERY execution branch (including every failure, retry, discard and abort) it satisfies jointly, with hmax defined in Section 7 and hmax <= (c1 + 2^-15) Vn,

    T   = O(n^10 2^hmax),
    S_C = O(n^4 2^(n^alpha / 65536)),
    S_Q = O(n),
    Q   = O(n^3 2^hmax).

These imply the declared envelopes (Section 14), where 4083/10000 = c1 + 1/25000:

    T = O(2^((4083/10000) sqrt(n log2 n))),  S_C = O(n^4 2^((1/65536) n^(1/3))),  S_Q = O(n),  Q = O(2^((4083/10000) sqrt(n log2 n))),

with exact growth indices 1/2, 1/3, 0, 1/2. All outside constants are absolute. The fifth claim is the clean-input tolerance 0 (Section 15). All logarithms are base 2.
For n < 2^4194304 the algorithm is exhaustive search (Section 11). These are asymptotic statements with an enormous fixed threshold, which big-O allows but which has no practical meaning.

Notation used throughout:
- d = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known integer. A "multiplier" W is an integer frequency factor.
- hd denotes a Hamming distance. T denotes total work only.

## 1. Provenance and what is new

This entry is the MWG algorithm of e-man07 (public Yukon submission 76d06063-f670-4712-8f30-d52b4c665084), run at memory
exponent alpha = 1/3, with a smaller table constant and a larger threshold. MWG is written for a parameter alpha and its proof
is stated for 1/8 <= alpha <= 3/8; its submission uses alpha = 1/4, and its note records that the leading coefficient is just
above sqrt(1/2 - alpha). Here alpha = 1/3, inside that range, and c1 = 20413/50000, just above sqrt(1/6) = 0.4082483. Everything in
Sections 2-6, 8-10, 12 and 15 is MWG's text, except that Lemma 8.2 now names the sigma-field it conditions on (Hp, which leaves
out the label bits at positions >= p) and one equation reference in Section 8 is corrected; wherever it names the algorithm
MWG, it means MWG13, the same algorithm at the configuration above. Sections 0, 7, 11, 13 and 14 carry the changes listed
below, with every step that depends on alpha, c1, the table constant or the threshold re-derived. The mathematics of the
construction, including MERGEG and the moment argument, is MWG's; what this entry contributes is the parameter choice and the
re-verification of the schedule.

Changes from MWG:
- alpha = 1/3; the parameter X, which bounds the growing part of every table exponent (lam_i <= kappa + 1 + X, Section 7),
  is X = ceil(n^alpha / 65536), defined by (65536 X)^3 >= n^1, instead of ceil(n^alpha / 2). Only (7.1), the fact kappa + 1 <= X, and the explicit constants in the bounds on f, I, h0 and
  G f (kappa + 1) use the lower bound on X; each is re-derived in Sections 7 and 13. The idea of a small constant in this parameter follows the table constant Kc in
  the notes of e-man07's MWQ rows (19b9a699, d8b88987, fa1caa30); no MWQ text is used.
- c1 = 20413/50000, so that c1^2 - (1/2 - alpha) = 71707/7500000000.
- The main branch starts at n = 2^4194304 instead of 2^65536, so that the capacity margin of Section 7, recomputed at
  Lr = 4194304, holds with this c1 and table constant. Every size fact MWG derives from 1/8 <= alpha <= 3/8 and n >= 2^65536
  holds a fortiori.
- Sections 0 and 14: the envelopes are T = Q = 2^((4083/10000) sqrt(n log2 n)) and S_C = n^4 2^((1/65536) n^(1/3)); the absorption step uses
  4083/10000 - c1 = 1/25000 > 2^-15 + 2^-17.
- Inherited slips corrected: the MERGEG precondition (Section 7) now reads b >= (f-2)(kappa+1); Lemma 8.2 conditions on
  the sigma-field Hp and Lemma 11.1 cites it; Section 8 cites (7.5). These corrections first appeared in MWG716 (public
  submission 94240a95-89f9-47ac-8d48-0d8c70ac94d7, the same algorithm at alpha = 7/16).

MWG's own provenance, restated: MWG keeps the framework of CW1 (public Yukon submission cfe82a87-0d65-454e-b1df-4789dc95aab4,
by e-man07), itself a schedule modification of CS1 (public submission b56c7ceb-de59-42da-9e3b-6ee96e4e4145 by AdamGagol,
identical to f1481815-9577-4990-abe3-7b79fa5d9284). Sections 2-6.2, 9, 10 and 15 are that text with the cost statements of
Section 5 widened for larger h_e. Not new in MWG: the binary linear merge, the free-frequency decoder, label extraction,
source-data shifts and the top-bit factorization. The collimation step and the distribution-free remainder argument are from
G. Kuperberg, arXiv:1112.3333v1, Algorithm 4.1, Proposition 4.2 and Section 4.6. CS1 credits COL3 for label extraction
(Kitaev, quant-ph/9511026), the top-bit argument, the CRT unit multiplier and the exhaustive finite branch. The steps after the
list in Section 6.3, and the moment argument of Section 8.1, come from e-man07's MW4 (33a6df9d-08d8-488b-a3f7-01f5f32373a4),
which uses four inputs and classical enumeration. Finding fiber members by Grover search on separate registers, with classical
verification, is the idea of the Regev-type rows on this challenge; MWG took it from the note of GPS3 (05a58278-80b6-40ff-9e8b-dcec501b4b10 by
ercumentyildirim) and its predecessors, without reusing their text. O. Regev, quant-ph/0406151, is the original polynomial-space sieve. Grover search with an unknown number
of marked items is from M. Boyer, G. Brassard, P. Hoyer and A. Tapp, "Tight bounds on quantum searching", Fortschr. Phys. 46
(1998). New in MWG (its Sections 6.3, 7, 8.1, 11, 13 and 14): MERGEG, an f-input collimation step for f growing with n that
lists a whole fiber of about 2^(lam') tuples by repeated Grover search over the stored input tables and then projects on that
list, and a schedule whose table exponent grows linearly in the tree height, up to about n^alpha/2 (here about X), with Grover-listed levels at fan-in 2^delta and
delta about (1/2 - alpha) log2 n.

The result is a row with classical memory index 1/3 and time index 1/2, with leading coefficient near sqrt(1/2 - alpha) =
sqrt(1/6). It is not a sub-1/2 time result. No claim is made that the construction is absent from
the wider literature.

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

Cost per call: O(n^2) precomputation plus t_V rounds of O(n log n). Here h_e = O(sqrt(n log n)) (Section 13), so this is O(n^2) core steps. Classical scratch O(n log n) bits.

### 5.4 High-confidence extraction and output

If verification accepts, LE outputs k_A. Otherwise it runs k_H = RUN(F(h_e)),
the high-confidence extraction, and outputs k_H, subject to the cap in 5.5.
After the last test of the call, the data register is reset. LE uses no
Fourier transform, no lookup, and no rotation other than H and S, and O(n)
quantum scratch (n data qubits, one ancilla, arithmetic).

### 5.5 Cap on high-confidence runs

Let sn be the least integer >= sqrt n (computed exactly by integer arithmetic) and Cf = ceil(Qcap/sn). A counter
records the number of RUN(F(h_e)) executions. If a call would start the
(Cf+1)-st one, MWG stops, releases everything and outputs 0 (ABORT).

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
(sqrt n + 1)/n decreases. Also Cf >= 20, because Qcap >= 6144 * 2^hmax >= 6144 * 2^(sqrt n) >= 20 (sqrt n + 1), with hmax from Section 7.
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
core steps in total. Since h_e = O(sqrt(n log n)) = O(n) (Section 13), on every branch all LE calls
together cost O(n^(5/2)) Qcap + O(n^3) core steps.

IDEAL run. The ideal run is MWG in the latent-label model with every LE output
replaced by the latent k and without the cap of 5.5. The actual and ideal runs
can be coupled to coincide unless some LE call returns a wrong label or ABORT
occurs, so every event's probability differs between them by less than
2^-11 + 2^-20. Resource bounds are proved for every ACTUAL branch directly,
because they rest only on caps and fixed allocations.

## 6. Phase vectors, the linear merge and the Grover-listed merge

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

### 6.3 MERGEG(X_1, ..., X_f; p, b, lam', kap)

Precondition: X_1..X_f are phase vectors from pairwise disjoint sets of copies, all of length L = 2^lam, collimated to p, with index registers x_1..x_f and tables lab_t[x] = c_t + 2^p h_t[x], 0 <= c_t < 2^p. Here f is a power of two, kap >= 1, b = f lam - lam' - kap >= 3 and lam' >= 1. Put Nt = L^f = 2^(f lam),

    muF = 2^(lam' + kap) = Nt / 2^b,   Cp = 2 muF + 1,   Ng = 4 Cp kap,   Jm = 2^(ceil((b+1)/2)),

car = floor((c_1 + ... + c_f)/2^p) in [0, f), and residues a_t[x] = h_t[x] mod 2^b. Bits p..p+b-1 of a tuple's label sum are
r(x_1, ..., x_f) = (a_1[x_1] + ... + a_f[x_f] + car) mod 2^b.

Sum circuit SUM: for t = 1..f, LOOKUP a_t into a temporary b-bit register, add it into a b-bit accumulator modulo 2^b, and repeat the LOOKUP to clear the temporary. Finally add car. It uses O(f L (lam + b)) gates and O(lam + b) scratch.

1. Run SUM on the index registers with a fresh accumulator Rz. Measure Rz, obtaining e, and reset it from the known value. Let S_e be the set of tuples with r = e, and sz_e = |S_e|.
2. List building, on separate registers. Start with an empty sorted list Tl of tuples. Repeat Ng times, or until |Tl| = Cp:
   - prepare f lam fresh qubits in the uniform superposition with H gates;
   - draw j uniformly in [0, Jm), by measuring H|0> on ceil((b+1)/2) fresh qubits;
   - apply j Grover iterations: the oracle (SUM, a comparison with e, Z on the result, and the inverse of the first two) followed by the inversion about the uniform state (H gates, a multi-controlled Z by a Toffoli chain, H gates);
   - measure the f lam qubits, obtaining a tuple. Compute its residue classically. If r = e and the tuple is not in Tl, insert it. Reset the qubits.
   These registers never touch the phase vectors, so the list depends only on the a_t, car, e and fresh coins. Let tl = |Tl|.
3. Let R have ceil(log2(Cp + 1)) bits, with a one-qubit flag Rf. Both start at 0. For each row rho of Tl compute the flag [(x_1, ..., x_f) = Tl[rho]] on the index registers with a Toffoli chain on O(f lam) scratch, CNOT it into Rf and onto the bits of R where rho has a 1, and uncompute the chain. Since rows are distinct, on Tl R = rho and Rf = 1, and elsewhere R = Rf = 0. Measure Rf. If Rf = 0 declare FAIL.
4. Measure bl = floor(R / 2^lam'). If (bl + 1) 2^lam' > tl declare FAIL.
5. For v in [0, 2^lam'), LOOKUP v -> Tl[bl 2^lam' + v] on the low lam' bits of R, XORing into x_1..x_f, which become |0>. Reset those registers, Rf and the high bits of R from known values.
6. Output the low lam' bits of R as the index register, with table lab[v] the sum of the f input labels of Tl[bl 2^lam' + v], stored as in STORAGE with p+b in place of p: put sv = h_1 + ... + h_f + car at that tuple, congruent to e modulo 2^b, and store the common residue c' = c_1 + ... + c_f - car 2^p + 2^p e in [0, 2^(p+b)) and the high parts hi'[v] = floor(sv/2^b).

On FAIL all inputs and registers are reset and released, and the inputs are never reused. All registers and classical arrays have fixed sizes.

Correctness (ideal run). Before step 1 the state is the product of the inputs: equal magnitudes over all Nt tuples with phases 2 pi (sum of labels) th. Steps 1, 3 and 4 compute functions of the tuple into clean registers and measure them, and step 2 acts on nothing in this state. So after step 4 the state is the equal-magnitude superposition over the 2^lam' tuples of block bl, with their original phases. Step 5 maps each to its v bijectively, so the output is a phase vector with table lab, collimated to p+b.

Grover search. Let Fm = sz_e and suppose muF/2 <= Fm <= Cp. Let sin^2 th0 = Fm/Nt. After j iterations a measurement returns a uniformly random element of S_e with probability sin^2((2j+1) th0), and otherwise a tuple outside S_e. This is the standard two-dimensional rotation; symmetry among marked tuples gives uniformity. For j uniform in [0, Jm) the mean success probability is

    (1/Jm) sum_(j < Jm) sin^2((2j+1) th0) = 1/2 - sin(4 Jm th0)/(4 Jm sin(2 th0)) >= 1/2 - 1/(4 Jm sin(2 th0)).

Since b >= 3, Fm/Nt <= (2 muF + 1)/Nt <= 3/8, so cos th0 >= 1/2 and sin(2 th0) >= sin th0 = sqrt(Fm/Nt) >= sqrt(muF/(2 Nt)) = 2^(-(b+1)/2) >= 1/Jm. So the mean is at least 1/4, and each attempt lists any fixed element of S_e with probability at least 1/(4 Fm) >= 1/(4 Cp), independently given the tables and e. Therefore, if muF/2 <= Fm <= Cp, each element of S_e is missing from the final list with probability at most

    (1 - 1/(4 Cp))^Ng <= exp(-kap) <= 2^(-kap).                                         (6.3)

(A list that reaches Cp entries already contains all of S_e in this case.)

Lemma 6.2 (failure identity). For ANY input tables collimated to p, the laws of all measurements in steps 1 to 4 depend only on the a_t and car, that is on label bits below p+b, and

    Pr[FAIL] = E sum_e [ (sz_e - tl_e) + (tl_e mod 2^lam') ] / Nt <= 2^(-kap) + E sum_e (sz_e - tl_e) / Nt,

where tl_e is the size of the list that would be built for e, and E averages over the list's coins.

Proof. Each measurement on the index registers is a computational-basis measurement of a function of the tuple on an equal-magnitude superposition, so its law is a ratio of counts, independent of phases. The outcome e has probability sz_e/Nt. Given e and Tl (a subset of S_e, built independently of the phase vectors), Rf = 0 has probability (sz_e - tl_e)/sz_e. Given Rf = 1, R is uniform on [0, tl_e), and step 4 fails with probability (tl_e mod 2^lam')/tl_e. Multiplying and summing gives the identity. The second term sums to less than 2^b 2^lam'/Nt = 2^(-kap). QED.

Cost on every branch. Each attempt makes at most Jm iterations of O(f L (lam + b)) gates plus O(f lam) gates for preparation and measurement, and O(f (lam + b) + log(Cp) f lam) classical bit operations for verification and insertion. Steps 1 and 3 to 6 take O(f L (lam + b) + Cp f lam + 2^lam' f lam + 2^lam' f n) core steps. With Jm <= 2^(b/2 + 2) and Ng <= 4 kap (2^(lam' + kap + 1) + 1), the total is

    O( kap f (lam + b + log2(Cp) lam) 2^(b/2 + lam' + kap + lam) + 2^(lam' + kap) f (lam + n) )     core steps.

Quantum scratch is O(f lam + b) beyond the index registers. Classical scratch is O(Cp f lam + f L b) bits, in addition to the input tables.

## 7. The tree TREE_D

Throughout, n >= 2^4194304 (the main branch of Section 11). Write Lr = log2 n and Vn = sqrt(n Lr). Input: a supplier of LEAF QUBITS. Each is a positive qubit with a known label uniform on [0, 2^D), D >= 2, independently. Put B = D - 1 <= n, the number of bits to collimate.

Global parameters, functions of n only, computed by exact integer arithmetic:

    Lc = ceil(log2 n),   kappa = Lc + 4,
    X = least integer with (65536 X)^3 >= n^1  (so X = ceil(n^alpha / 65536), alpha = 1/3),
    R = least integer with R^2 >= c1^2 n Lc  (c1 = 20413/50000),
    delta = least integer with 2^delta X >= 4 R,   f = 2^delta,
    h0 = ceil(f (kappa + 1)/2),   I = X + 2f + 2,
    G = ceil(R/delta) + 2,   mu = I + h0 + G,
    ell_g = floor(2 g delta/(f + 4)) for g >= 0.

Levels i = 0, ..., mu - 1 have arity f_i and input table exponent lam_i. Put bmax_i = f_i lam_i - lam_(i+1) - kappa. By direct substitution:

    Phase A, 0 <= i <= I-1:           f_i = 2,  lam_i = kappa + 1 + min(i, X),
                                      bmax_i = i (i < X), bmax_i = X + 1 (X <= i < I-1), bmax_(I-1) = 2X + 1.
    Phase B, I <= i <= I+h0-1:        f_i = 2,  lam_i = kappa + 1,  bmax_i = 1.
    Phase G, i = I + h0 + g, g >= 0:  f_i = f,  lam_i = kappa + 1 + ell_g.

Heights: h_i = i for i <= I + h0, and h_(I+h0+g) = I + h0 + g delta. A node of level i has 2^(h_i) leaf vectors below it.

A tree with m levels (1 <= m <= mu) uses level m-1 as its ROOT with lam_m := 1, capacity rootcap_(m-1) = f_(m-1) lam_(m-1) - 1 - kappa, and total capacity Sum(m) = sum_(i < m-1) bmax_i + rootcap_(m-1). Per tree, m is the least m with Sum(m) >= B.

Size facts. Since 2^(delta-1) X < 4R, we have 4R/X <= f < 8R/X. Here n^alpha/65536 <= X <= n^alpha, and 1/8 <= alpha <= 3/8, so n^alpha >= 2^8192 and n^(1/2 - alpha) >= 2^8192. Since c1 < 9/10, we have c1 Vn <= R <= c1 sqrt(n (Lr + 1)) + 1 <= (c1 + 2^-16) Vn <= Vn. In particular:
- f >= 4R/X >= 4 c1 Vn/n^alpha >= n^(1/2 - alpha), using 4 c1 >= 1, so 5/(f + 4) <= 2^-8000. Also f < 8R/X <= 2^19 Vn/n^alpha, so f <= n.
- delta <= log2(8R/X) <= 3 + (Lr + log2 Lr)/2 + 16 - alpha Lr = (1/2 - alpha) Lr + (1/2) log2 Lr + 19.   (7.1)
- delta >= log2(4R/X) >= (1/2 - alpha) Lr.
- kappa + 1 <= Lr + 6 <= 2^(alpha Lr - 16) <= n^alpha/65536 <= X. So f X < 8R and f (kappa + 1 + X) <= 2 f X < 16 R.
- I = X + 2f + 2 <= n^alpha + 2^20 Vn/n^alpha + 2 and h0 <= f (kappa+1)/2 + 1 <= 2^18 Vn (Lr + 6)/n^alpha + 1. Since alpha <= 3/8, n^alpha <= 2^-4000 Vn. Therefore

      I + h0 + 3 delta <= 2^-40 Vn.                                                        (7.2)

- mu <= I + h0 + R/delta + 3 <= 2 Vn <= n. Hence 16 n <= 2^kappa <= 32 n, and 2^kappa >= 16 mu.
- Binary levels have lam_i <= kappa + 1 + X and bits at most 2X + 1, both O(sqrt n), as Section 6.2 assumes, since X <= n^(3/8).

Capacity. For 0 <= g <= G - 2, using ell_(g+1) <= ell_g + 1 (because 2 delta <= f + 4),
bmax_(I+h0+g) >= f(kappa+1+ell_g) - (kappa+2+ell_g) - kappa = (f-1) ell_g + (f-2) kappa + f - 2 >= (f-1)(ell_g + 1) >= (f-1) 2 g delta/(f+4). Since all capacities are nonnegative,

    Sum(mu) >= ((f-1)/(f+4)) delta (G-1)(G-2) >= (1 - 5/(f+4)) R^2/delta,

because G-1 and G-2 are at least R/delta. Now R^2 >= c1^2 n Lr. By (7.1), it suffices that (1 - 2^-8000) c1^2 Lr >= (1/2 - alpha) Lr + (1/2) log2 Lr + 19. Here c1^2 - (1/2 - alpha) = (20413/50000)^2 - 1/6 = 71707/7500000000, so at Lr = 4194304 the left minus the right has the
term 71707/7500000000 * 4194304 = 40.101, which exceeds (1/2) log2 4194304 + 19 = 30 plus 2^-8000 c1^2 Lr. The derivative
of the difference in Lr is at least 71707/7500000000 - 1/(2 Lr ln 2) - 2^-8000 > 0 for Lr >= 4194304. The difference increases with Lr. So Sum(mu) >= n >= B, and m <= mu for every tree.

Height. Put hmax = h_mu = I + h0 + G delta. Then G delta <= R + 3 delta, so by (7.2) and R <= (c1 + 2^-16) Vn,

    R <= hmax <= (c1 + 2^-15) Vn,                                                          (7.3)

and h_m <= hmax for every tree. Also R >= sqrt n.

Table sizes. For g <= G, ell_g <= 2 G delta/(f+4) <= 2 (R + 3 delta)/f <= 4R/f <= X. So every level has lam_i <= lam_max := kappa + 1 + X.

Budget. Let i = I + h0 + g be a Phase G level, with lam = lam_i, output exponent lam' <= lam + 1 (lam' = 1 at the root) and bits b = f lam - lam' - kappa. Then

    b/2 + lam' + lam + kappa = (f/2 + 1) lam + lam'/2 + kappa/2 <= (f/2 + 2) lam + kappa + 1
        = (f/2)(kappa+1) + (f/2 + 2) ell_g + 3 kappa + 3 <= h_i + 3 kappa + 3,                (7.4)

because (f/2 + 2) ell_g <= g delta by the definition of ell_g, and h_i >= h0 + g delta. Binary levels satisfy lam_i <= kappa + 1 + h_i.

Allocation. Allocate b_(m-1), ..., b_0 in that order greedily, with b_(m-1) = min(rootcap_(m-1), B) and then b_i = min(bmax_i, B - already allocated). Then sum_i b_i = B, and some low levels may get smaller values or 0. Put p_0 = 0 and p_(i+1) = p_i + b_i, so p_m = B. Let nq_D = 2^(h_m) (kappa + 1) be the number of leaf qubits per tree.

Lemma 7.1 (Phase G levels are full). In any tree with a Phase G level, every level i >= I gets its full capacity. So every MERGEG has b_i = f lam_i - lam_(i+1) - kappa exactly, with lam_m = 1 at the root.

Proof. Here m >= 2, so Sum(m-1) < B by minimality of m. The deficit Sum(m) - B is less than Sum(m) - Sum(m-1) = bmax_(m-2) + rootcap_(m-1) - rootcap_(m-2) = rootcap_(m-1) + 1 - lam_(m-1) <= rootcap_(m-1) <= f (kappa + 1 + X) <= 2 f X. Phase A contains the 2f + 1 levels X <= i <= I-2, each of capacity X + 1, so its total capacity is at least (2f + 1)(X + 1) >= 2 f X. The greedy allocation therefore meets all levels i >= I in full before it reaches Phase A. QED.

Preconditions of MERGEG at a Phase G level: b = f lam - lam' - kappa >= (f-1)(kappa+1) - 1 - kappa = (f-2)(kappa+1) >= 3, using lam' <= lam + 1; lam' >= 1; kap = kappa >= 1. Here muF = 2^(lam' + kappa) in the notation of Section 6.3. For a binary level, b_i + lam_(i+1) - 2 lam_i <= -kappa, so Lemma 6.1 gives Pr[FAIL] <= 2^-kappa for any input tables.

LEAF: take kappa+1 leaf qubits as the index register (bit j = qubit j). Build the table incrementally, lab[0] = 0 and lab[x + 2^j] = lab[x] + k_j for x < 2^j: one addition per entry. The table has length 2^(lam_0), is collimated to p_0 = 0, and in the ideal run is exactly the tensor product state.

Field widths. A level-i label is a sum of at most 2^(h_i) (kappa+1) leaf labels below 2^(B+1), so it is below 2^(B+1+h_i+gw) with gw = ceil(log2(kappa+1)). Level-i tables are collimated to p_i and stored with w_i = B + 1 + h_i + gw - p_i bits per high part, at most 3n.

VEC(i): if i = 0 return LEAF. Otherwise repeat:
- build the f_(i-1) inputs, each by VEC(i-1);
- out = MERGE(X1, X2; p_(i-1), b_(i-1), lam_i) if f_(i-1) = 2, and out = MERGEG(X_1, ..., X_f; p_(i-1), b_(i-1), lam_i, kappa) otherwise;
- if out != FAIL, return out.

TREE_D returns VEC(m), a one-qubit phase vector with labels lab[0] and lab[1], congruent modulo 2^B. Its ideal state is, up to global phase, (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2 with the known integer

    W = (lab[1] - lab[0]) / 2^B = hi[1] - hi[0],                              (7.5)

because the root table is collimated to p_m = B. Each label is a sum of at most nq_D leaf labels below 2^(B+1), so |W| < 2 nq_D. Depth-first evaluation holds at most f_i - 1 finished siblings per level.

## 8. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and
tau_j in {0,1}. Since k_j is uniform on [0, 2^(B+1)), low_j and tau_j are
independent and tau_j is a fair bit. Let Gt be the sigma-field generated by:
- all low_j of the tree's leaves, including those of discarded attempts;
- all measurement outcomes (e, Rf, bl) of its merges, and the coins and outcomes of MERGEG's list building;
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
sort key, list, rank and block partition uses only label bits below position B,
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
re-indexing is a bijection. So hd = |x0 xor x1| >= 1. From (7.5),

    W = cst + sum_(j in Sp) tau_j - sum_(j in Sm) tau_j,                        (8.1)

where cst = (sum_j low_j (x1_j - x0_j)) / 2^B is a Gt-measurable integer, and Sp and
Sm are disjoint Gt-measurable sets with |Sp| + |Sm| = hd. A fair bit tau has
E exp(2 pi i phi tau) = e^(i pi phi) cos(pi phi). Hence, for every real phi,

    | E[ exp(2 pi i phi W) | Gt ] | = |cos(pi phi)|^hd <= |cos(pi phi)|,       (8.2)

and, with phi = 1/2, Pr[W odd | Gt] = 1/2.                                     (8.3)

### 8.1 Mid-tree factorization and the fiber moments of MERGEG

Lemma 8.2. In the ideal run, consider a MERGEG attempt at level i, with p = p_i, b = b_i, lam = lam_i, lam' = lam_(i+1) (or 1 at the root), f inputs. Let Hp be the sigma-field generated by everything that happened before its step 1 except the label bits at positions >= p of the leaves of its f inputs: the bits below p of those labels, the measurement outcomes, lists, coins and controller decisions of all earlier steps, and everything on other copies. (The input tables also record the higher bits; Hp does not contain them.) Then Pr[FAIL | Hp] <= 2^(3 - kappa).

Proof. Let Lv be the set of leaves of the f inputs, a union of pairwise disjoint sets. For j in Lv write k_j = l_j + 2^p g_j + 2^(p+b) u_j with 0 <= l_j < 2^p and 0 <= g_j < 2^b. This is possible as p + b <= B < D, and k_j uniform makes l_j, g_j, u_j independent and uniform.

Factorization. Every earlier step of the tree that involves a leaf of Lv is a merge at a lower level, with p' + b' <= p, or a leaf-acceptance test or a controller decision. By Lemmas 6.1 and 6.2 those laws, residues, sort keys, ranks, lists and block choices read only label bits below p, and bits below p of a sum of leaf labels depend only on the l_j. Steps elsewhere use disjoint copies. So, exactly as in the proof of Lemma 8.1 with p in place of B, conditional on Hp the g_j (j in Lv) are i.i.d. uniform on [0, 2^b). The incidence vector I(tau), a subset of Lv, of each tuple tau and the integer f0(tau) = floor((sum_(j in I(tau)) l_j)/2^p) are Hp-measurable. Distinct tuples have distinct incidence vectors, by the concatenation and re-indexing argument above, so at most one tuple has I(tau) empty.

Moments. The residue of a tuple is r(tau) = (f0(tau) + sum_(j in I(tau)) g_j) mod 2^b. Fix e, and let S count the tuples with I(tau) nonempty and r(tau) = e. For nonempty I(tau), r(tau) is uniform, so muF - 1 <= E S <= muF, with muF = Nt/2^b = 2^(lam' + kappa) by Lemma 7.1. For distinct nonempty I and I', there is j in the symmetric difference, say j in I' \ I, and there is i' in I. The map (g_(i'), g_j) -> (r, r'), with other coordinates fixed, has matrix [[1,0],[1,1]] if i' in I', and the identity otherwise. Both are invertible over Z/2^b, so (r, r') is uniform on (Z/2^b)^2. The indicators are thus pairwise independent, and Var S <= E S <= muF. Also sz_e <= S + 1, and sz_e >= S. By Chebyshev, Pr[S > 2 muF] <= Var S / muF^2 <= 1/muF and Pr[S < muF/2] <= Var S/(muF/2 - 1)^2 <= 16/muF, as muF >= 4.

Three cases for each e, using sz_e - tl_e <= sz_e.
(a) sz_e > Cp = 2 muF + 1. Then S > 2 muF, and sz_e <= S + 1 = (S - 2 muF)_+ + 2 muF + 1 on this event. If S > 2 muF, then S - E S >= S - muF > muF and S - 2 muF <= S - E S <= (S - E S)^2/muF. So E[sz_e ; case (a)] <= Var S/muF + (2 muF + 1)/muF <= 4.
(b) sz_e < muF/2. Then S < muF/2. So E[sz_e ; case (b)] <= (muF/2)(16/muF) = 8.
(c) muF/2 <= sz_e <= Cp. By (6.3), E[sz_e - tl_e | tables, e] <= sz_e 2^(-kappa).

Summing over the 2^b values of e and dividing by Nt, cases (a) and (b) contribute at most 12 * 2^b/Nt = 12/muF <= 6 * 2^(-kappa), since muF >= 2^(kappa + 1). Case (c) contributes at most 2^(-kappa) sum_e sz_e / Nt = 2^(-kappa). With Lemma 6.2, Pr[FAIL | Hp] <= 2^(-kappa) + 6 * 2^(-kappa) + 2^(-kappa) = 2^(3 - kappa). QED.

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

Finite branch (n < 2^4194304). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand at the first minus outcome. Output the first cand with no rejection, or 0.
- For cand = s every outcome is plus.
- For cand != s the two data branches are orthogonal, so each outcome is uniform.
- A union bound over cand gives Pr[wrong] <= N 2^-(n+10) <= 2^-10.
- Since n < 2^4194304, all resources on this branch are bounded by absolute constants.

Main branch (n >= 2^4194304). Compute a2, M, d, J, K and all tree parameters. The values mu, kappa and hmax are those of Section 7, with m <= mu and h_m <= hmax for every B <= n used. Let Rs = J + 1, or Rs = 0 if M = 1. Put

    Q* = 6 * 2^hmax (kappa+1) (Rs K + 2 a2) + 2 a2,    Qcap = 1024 Q*,

and then h_e, h_A, t_V and Cf from Section 5. Here K in Section 9 is computed with nq = nq_d. A binary down-counter of acquisitions is kept, at amortized O(1) bit flips per acquisition. MWG13 stops, releases everything and outputs 0 before an acquisition would exceed Qcap. Otherwise it runs Section 9 and then Section 10. Parameter, CRT and table computations are polynomial in n.

Lemma 11.1 (expected ideal acquisitions). In the ideal UNCAPPED run, the expected number of acquisitions is at most Q*.

Proof. An accepted leaf qubit needs at most 2 acquisitions in expectation (acceptance probability > 1/2 in Section 9, and 1 in Section 10). Let Qv_i be the expected number of acquisitions until VEC(i) returns. By Lemma 6.1 at binary levels and Lemma 8.2 at Phase G levels, each merge attempt succeeds with conditional probability at least 1 - 2^(3-kappa) >= 1 - 1/(2 n) >= 1 - 1/(2 mu), given Hp of Lemma 8.2 at Phase G levels and given everything before its step 1 at binary levels (Lemma 6.1 holds for any input tables, so all labels may be included). Both sigma-fields contain the outcomes of all earlier attempts, which use disjoint copies, so the same bound holds given those outcomes. By Wald's identity, Qv_(i+1) <= rt f_i Qv_i, where rt = 1/(1 - 1/(2 mu)). Moreover rt^m <= exp(m/(2 mu - 1)) <= e < 3 for m <= mu. So Qv_m <= 3 * 2^(h_m) * 2(kappa+1) <= 6 * 2^hmax (kappa+1). The odd part runs Rs K trees. Section 10 needs, per bit, an expected 2 trees by (8.3), or, when wd = 1, an expected 2 single acquisitions since kk is uniform on {0,1}. Summing gives the bound. QED.

Lemma 11.2 (work per branch). On every actual branch of the main branch, the number of core steps is at most O(n^6) Qcap + O(n^3 nq) + poly(n), where nq = nq_d.

Proof. Charge every core step to an acquisition, or to the fixed-length loops.
- All LE calls together take O(n^(5/2)) Qcap + O(n^3) core steps on every branch (Section 5.6). Each acquisition's other work (transform, acceptance test, X, counter update) is O(n^2).
- A leaf table of 2^(kappa+1) entries costs O(n 2^(kappa+1)). Charged to its kappa+1 acquisitions, that is O(n 2^kappa) = O(n^2) per acquisition.
- A binary merge attempt at level i costs O(n (2^(lam_i) + 2^(lam_(i+1)))) = O(n 2^(kappa + 1 + h_i)) by Section 6.2, since lam_i <= kappa + 1 + h_i and lam_(i+1) <= lam_i + 1 (or smaller). Its inputs were built from 2^(h_i + 1)(kappa+1) acquisitions that no other attempt at that level uses, since inputs of a failed merge are discarded and never reused. That is O(n 2^kappa) = O(n^2) per acquisition per level.
- A MERGEG attempt at level i has lam, b and log2 Cp all at most n, because b <= f lam_i <= 2 f X < 16 R <= n. By Section 6.3 and (7.4), it costs O(kappa f n^2 2^(h_i + 3 kappa + 3)) core steps, and this includes the second term of Section 6.3 because lam' + kappa <= b/2 + lam' + kappa + lam. Its f inputs were built from f 2^(h_i) (kappa+1) acquisitions that no other attempt at that level uses. That is O(n^2 2^(3 kappa)) = O(n^5) per acquisition per level, because 2^kappa <= 32 n.
- Each acquisition lies below at most mu merge attempts, one per level, with mu <= n. So the total merge share is O(n^6) per acquisition.
- Root measurements and bookkeeping are O(n) per tree, and each tree uses at least one acquisition.
- The decoder's fixed loops cost Rs * 2^(ceil(log2 nq)+8) * K * O(n) = O(n * nq * n * n) core steps, since Rs <= n and K = O(n).
- Setup is poly(n) and runs once. It covers the parameters, extended Euclid and CRT for at most n stages, the Mult constants, Q*, h_e, the table of Section 4, the Section 10 shift values, and the decoder's initial residues (f_i c) mod 2^(P_j).

Every loop is either fixed-length or consumes acquisitions, so every branch terminates with this many core steps. QED.

## 12. Success probability

In the ideal UNCAPPED run, the odd part errs with probability at most 2^-20 (Section 9), and Section 10 then never errs. By Markov and Lemma 11.1, the source cap is reached in the ideal run with probability at most 1/1024. Capping changes the run only on that event. The actual run differs from the ideal one only if some LE call returns a wrong label or the high-confidence cap aborts, which has probability below 2^-11 + 2^-20 (Section 5.6, Lemma 5.2). So

    Pr[output = s] >= 1 - 2^-20 - 2^-10 - 2^-11 - 2^-20 >= 1 - 2^-8 > 2/3.

The finite branch succeeds with probability at least 1 - 2^-10. These are additive couplings. There is no conditioning on favorable labels, caps or outcomes.

## 13. Resources on every branch

Throughout, n >= 2^4194304; the finite branch is O(1). From Section 7: hmax <= (c1 + 2^-15) Vn, kappa + 1 = O(log2 n), 2^kappa <= 32 n, f <= n, mu <= n, and every lam_i <= lam_max = kappa + 1 + X.

Sizes. log2 nq <= hmax + log2(kappa+1) <= n, so K = O(n). Also Rs <= n and a2 <= n. So (kappa+1)(Rs K + 2 a2) = O(n^3), and Q* = O(n^3 2^hmax). Also log2 Qcap = O(Vn), so h_e = O(Vn), and h_A, T_V = O(log n).

Q. On every branch, Q <= Qcap = 1024 Q* = O(n^3 2^hmax).

Core steps. By Lemma 11.2 they number O(n^6) Qcap + O(n^3 nq) + poly(n) = O(n^9 2^hmax).

S_Q. In Phase G the depth-first stack holds at most f index registers per level, so at most sum_(g < G) f (kappa + 1 + ell_g) <= G f (kappa+1) + delta G^2 qubits, using f ell_g <= 2 g delta. Here G f (kappa + 1) <= (2 Vn/delta)(2^19 Vn/n^alpha)(Lr + 6) = o(n), because n^alpha >= 2^8192 and delta >= Lr/8. And delta G^2 <= (R + 3 delta)^2/delta <= 2 R^2/delta <= 2 n (Lr + 1) c1^2 /((1/2 - alpha) Lr) + o(n) = O(n), by delta >= (1/2 - alpha) Lr. Phases A and B add at most 2 (I + h0)(kappa + 1 + X) qubits. That is o(n), because (X + f + h0) X = O(n^(3/4) + R (log n)) by f X < 8R and X <= n^(3/8), and h0 (kappa + 1) = O(f (log n)^2). A merge adds O(f lam + b) qubits for its registers and Grover scratch, and f lam + b <= 2 f lam <= 4 f X < 32 R = o(n). LE uses O(n) qubits, and the data register is reset after each call. Transforms use O(n), and each root qubit is measured at once. Released registers are reused. So S_Q = O(n).

S_C. At any time the depth-first stack holds at most f_i + 1 tables per level, so at most (mu + 1)(f + 1) tables, each of at most 2^(lam_max) entries of at most 3n bits plus an n-bit residue. These use O(mu f n 2^(kappa + X)) = O(n^4 2^X) bits.
- Binary merge scratch is O(2^(lam_max) sqrt n) bits (Section 6.2).
- MERGEG scratch is O(Cp f lam + f L b) bits (Section 6.3), with Cp <= 2^(lam_max + kappa + 1) + 1 and f lam, b <= n, which is O(n^4 2^X).
- The decoder stores K triples (W_i, beta_i, Z_i) and K running residues, O(n^2) bits. Its candidates are enumerated, never stored.
- The table of Section 4 is O(1). Counters and parameters are O(n) bits. LE uses O(n log n) classical scratch (Section 5.3) and the fallback counter.

So S_C = O(n^4 2^X) with X < n^alpha/65536 + 1, that is S_C = O(n^4 2^(n^alpha/65536)). These are fixed allocations, so the bound holds on every branch, including when labels are wrong.

T. By (2.1), with log2(S_C + S_Q + 2) = O(n), T = O(n^9 2^hmax) * O(n) + (n+1) Qcap = O(n^10 2^hmax).

All four bounds hold simultaneously for the same execution, with absolute constants independent of N, s and outcomes.

## 14. Exact growth indices and declared envelopes

The declared envelopes are

    B_T(n) = 2^((4083/10000) sqrt(n log2 n)),   B_C(n) = n^4 2^((1/65536) n^(1/3)),   B_Q(n) = n,   B_samples(n) = 2^((4083/10000) sqrt(n log2 n)).

Absorption. By Section 7, hmax <= (c1 + 2^-15) Vn, and 4083/10000 - c1 = 1/25000 > 2^-15 + 2^-17. So for any fixed K, n^K 2^hmax <= 2^(K Lr - 2^-17 Vn) 2^((4083/10000) Vn), and K Lr - 2^-17 Vn tends to minus infinity. So T = O(B_T) and Q = O(B_samples). Also S_C = O(n^4 2^(n^alpha/65536)) = O(B_C) at alpha = 1/3. And S_Q = O(B_Q). The finite branch is O(1) and is absorbed. Thus each resource is O of its envelope, uniformly over N and s of bit length n.

The Section 13 bounds are the sharper statements proved; the declared envelopes are their upper bounds in the supported family. For B(n) = 2^(a sqrt(n log2 n)) with a > 0, log2 log2 B = (1/2) log2 n + (1/2) log2 log2 n + log2 a, so g(B) = 1/2. For B_C(n) = n^4 2^((1/65536) n^p) with p = 1/3, log2 log2 B_C = p log2 n - 16 + o(1), so g(B_C) = p = 1/3. For B_Q(n) = n, log2 log2 n / log2 n -> 0, so g = 0. The structured objects in submission.json are exactly these envelopes.

## 15. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy
is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does
not assert that robustness is impossible.
