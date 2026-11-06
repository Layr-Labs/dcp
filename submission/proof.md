# CS1: linear-merge collimation and a free-frequency phase decoder

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single
algorithm CS1 below receives N in binary and fresh independent copies of rho_s,
and outputs the entire s with unconditional probability at least 1 - 2^-8 > 2/3.
On EVERY execution branch (including every failure, retry, discard and abort)
it satisfies jointly

    T   = O(n^4 (log2 n)^2 2^(sqrt(2n))),
    S_C = O(n^2 (log2 n)^2 2^(sqrt(2n) - (2n)^(1/4))),
    S_Q = O(n),
    Q   = O(n^(3/2) 2^(sqrt(2n))).

All outside constants are absolute. Define integers by (u_0, v_0) = (10, 7) and
(u_(k+1), v_(k+1)) = (3 u_k + 4 v_k, 2 u_k + 3 v_k). The map preserves u^2 - 2v^2, because
(3u + 4v)^2 - 2(2u + 3v)^2 = 9u^2 + 24uv + 16v^2 - 8u^2 - 24uv - 18v^2 = u^2 - 2v^2.
Hence u_k^2 - 2 v_k^2 = 10^2 - 2*7^2 = 2 > 0 and u_k/v_k > sqrt(2) for every k >= 0.
Let a = u_333/v_333. Written out in decimal (256 digits each),

    u_333 = 8441478004666748666153322414015794961054342923175177808658686557734489303162152388494751245868147491831446292476962720233203201073933816582585276436077865535199430405176591394221939485167179701583924490203278327423413823406808776174974568608124494762509770
    v_333 = 5969026340336944451114480739433819709407468170415945417713771714885974444504222882421291476798989652766383498455240579454394404150586732509003361709530480614304768144606668970442415970951831495263198155709406532002051594173677103082229495028847707209502393

and a = u_333/v_333 is the exponent coefficient in the three structured envelopes of
submission.json. Only a > sqrt(2) is used anywhere below. (Remark, not used: these
fractions are the upper convergents and semiconvergents of sqrt 2, and a is the closest
rational above sqrt 2 whose numerator and denominator have at most 256 digits.)
Since a > sqrt(2), 2^(sqrt(2n)) <= 2^(a sqrt(n)) for all n >= 1. The declared envelopes are
n^4 (log2 n)^2 2^(a sqrt n), 2^(a sqrt n - n^(1/4)), n, and n^(3/2) 2^(a sqrt n),
with exact growth indices 1/2, 1/2, 0, 1/2 (Section 14). The fifth claim is the
clean-input tolerance 0 (Section 15).

Notation used throughout:
- d = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known integer. A "multiplier" W is an integer frequency factor.
- hd denotes a Hamming distance. T denotes total work only.

## 1. Provenance and what is new

The collimation step (measure a residue of summed phase labels, keep the
collimated sub-vector, re-index) and the distribution-free bucket/remainder
argument are from G. Kuperberg, "Another subexponential-time quantum algorithm
for the dihedral hidden subgroup problem", arXiv:1112.3333v1, Algorithm 4.1,
Proposition 4.2 and Section 4.6. Section 4.6 also notes that never-inspected
top label bits stay uniform. Kuperberg's heuristic 2^(sqrt(2n)) estimate
(Section 4.5) is not used as a premise; it is proved here in the challenge model.

The earlier COL3 collimation submission on this challenge supplied four ideas.
CS1 restates and fully reproduces each:
- the Kitaev-test label extraction (Kitaev, quant-ph/9511026);
- the top-bit independence argument;
- the CRT unit multiplier for the odd part of N;
- the exhaustive finite branch.
No earlier verdict is a premise.

New in CS1:
1. Linear-size merges. COL3 enumerated all L^2 pairs of a merge in literal
   lookup tables. CS1 measures only a residue of the summed labels, then
   re-indexes the surviving pairs by a closed-form rank. Every quantum lookup
   has O(L) rows (Section 6).
2. Growing lengths, 2^(kappa_i+1+i) at level i. The depth is m ~ sqrt(2B) for B
   collimated bits, and the total cost is 2^(sqrt(2n)) poly(n) (Sections 7, 13).
3. A free-frequency decoder. COL3 kept a root only when its frequency
   multiplier was exactly +-1, which lost a factor of about the number of
   leaves. CS1 uses every root with its known frequency (Section 9).
4. The 2-adic part shifts the SOURCE DATA by known values. No approximate
   phase gradient and no rotation synthesis is used anywhere. All gates are
   NOT, CNOT, Toffoli, H, S, S^dagger and computational-basis measurement
   (Section 10).
5. Verified label extraction. A cheap estimate with O(log n) tests per level
   is checked by O(sqrt n) tests with random shifts c. The predicted phase
   frac(c k/N) is a sum of precomputed binary-expansion windows, so a check round
   costs O(n log n). Kitaev's high-confidence extraction runs only after a
   rejection, and a global cap bounds those runs. LE costs O(n^2 log n) per call,
   amortized over all calls on every branch, instead of O(n^(5/2)), so
   T = O(n^4 (log2 n)^2 2^(sqrt(2n))) (Section 5).
6. Length cap. Lengths stop growing s = floor(sqrt(mu)) levels below the root.
   The capped levels still collimate as many bits per level, losing only
   s(s-1)/2 <= mu/2 bits in total, so the depth bound m <= mu, and with it T and
   Q, is unchanged, while every table is shorter by a factor 2^s. Hence
   S_C = O(n^2 (log2 n)^2 2^(sqrt(2n) - (2n)^(1/4))) (Sections 7, 13). Tables also store
   only a common residue and high parts (Section 6).
7. Level-dependent slack. The merge producing level i+1 is given slack
   kappa_i = kap(16+i), which grows like log2 i, instead of one slack of about
   log2 m at every level. The failure probabilities still sum to less than 1/40,
   but every leaf now has a constant 15 qubits instead of about log2 m. This
   removes the log2 n factor from Q, while the extra merge work per acquisition
   stays inside the time bound (Sections 7, 11, 13).

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
(Cf+1)-st one, CS1 stops, releases everything and outputs 0 (ABORT).

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
(sqrt n + 1)/n decreases. Also Cf >= 20, because Qcap >= 6144 * 2^(sqrt(2n)) >= 20 (sqrt n + 1).
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

IDEAL run. The ideal run is CS1 in the latent-label model with every LE output
replaced by the latent k and without the cap of 5.5. The actual and ideal runs
can be coupled to coincide unless some LE call returns a wrong label or ABORT
occurs, so every event's probability differs between them by less than
2^-11 + 2^-20. Resource bounds are proved for every ACTUAL branch directly,
because they rest only on caps and fixed allocations.

## 6. Phase vectors and the linear merge

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

## 7. The tree TREE_D

Input: a supplier of LEAF QUBITS. Each is a positive qubit with a known label
uniform on [0, 2^D), D >= 2, independently. Put B = D - 1, the number of bits to
collimate. The parameters are computed by exact integer arithmetic:

    t(j) = ceil(log2(j+1)),   kap(j) = t(j) + 2 ceil(log2(t(j)+1)) + 3   (j >= 1),
    mu = ceil(sqrt(2B)) + 1,  s = floor(sqrt(mu)),  kappa_i = kap(16+i) (i >= 0),
    m = min{ m >= s+1 : m(m+1)/2 - s(s-1)/2 + 14 >= B },
    lam_i = kappa_i + 1 + min(i, m-s) (0 <= i <= m-1),  lam_m = 1,
    bmax_i = 2 lam_i - lam_(i+1) - kappa_i (0 <= i <= m-1).

Here kappa_0 = kap(16) = 5 + 6 + 3 = 14, so lam_0 = 15. Lengths grow by one bit per
level (plus slack increments) up to level m-s and then grow only by slack
increments for the last s-1 levels below the root (LENGTH CAP). For s = 1 this is
the plain growing schedule.

Slack facts. kap is nondecreasing. t(j+1) > t(j) only when j+1 is a power of two,
and then t grows by 1 and ceil(log2(t+1)) by at most 1, so dk_i = kappa_(i+1) -
kappa_i lies in {0,1,2,3}, and dk_i > 0 only when 17+i is a power of two, so only
for i >= 15. Since 2^(t(j)-1) < j+1 <= 2^(t(j)) and (t+1)^2 <= 4^(ceil(log2(t+1))) < 4(t+1)^2,

    8 (j+1) (t(j)+1)^2 <= 2^(kap(j)) < 64 (j+1) (t(j)+1)^2.                   (7.0)

The j >= 16 with t(j) = t are at most 2^(t-1) integers, each with j+1 > 2^(t-1), and
t >= 5. So by (7.0)
sum_(i>=0) 2^-(kappa_i) <= sum_(t>=5) 1/(8(t+1)^2) = (1/8) sum_(u>=6) 1/u^2 < 1/(8*5.5) < 1/40,
using sum_(u>=6) 1/u^2 < integral from 5.5 to infinity of dx/x^2 (convexity).

Basic facts:
- mu >= 3, so 1 <= s <= sqrt(mu) and mu >= s + 1.
- s(s-1)/2 <= mu/2, so mu(mu+1)/2 - s(s-1)/2 + 14 >= mu^2/2 >= B. Hence s+1 <= m <= mu.
- Telescoping, sum_i bmax_i = lam_0 - lam_m + sum_(i<m) (lam_i - kappa_i)
  = 14 + sum_(i<m) (1 + min(i, m-s)) = m(m+1)/2 - s(s-1)/2 + 14 >= B
  (with t = m - s: m + t(t+1)/2 + (s-1)t = t^2/2 + t/2 + st + s on both sides).
- Explicitly, bmax_i = i - dk_i on growing levels (i <= m-s-1),
  bmax_i = m-s+1-dk_i on capped levels (m-s <= i <= m-2), and
  bmax_(m-1) = kappa_(m-1) + 2(m-s) + 1 at the root. Every bmax_i >= 0: if dk_i = 0
  this is clear. If dk_i > 0 then i >= 15, so growing levels have bmax_i >= 12. A
  capped level with dk_i > 0 has m >= i+2 >= 17. Then 2B <= m(m+1) + 28 <= (m+2)^2
  (as m >= 8), so mu <= m+4 and s <= sqrt(m+4) <= m-2, so bmax_i >= m-s-2 >= 0.

Allocate b_(m-1), b_(m-2), ..., b_0 in that order greedily, b_i = min(bmax_i,
B - (already allocated)). Then sum_i b_i = B. Put p_0 = 0 and p_(i+1) = p_i + b_i,
so p_m = B, and let nq_D = 15 * 2^m be the number of leaf qubits per tree.
By the definition of bmax_i,

    b_i + lam_(i+1) - 2 lam_i <= bmax_i + lam_(i+1) - 2 lam_i = -kappa_i,      (7.1)

so by Lemma 6.1 the merge producing level i+1 fails with probability at most
2^-(kappa_i) <= 2^-14, and these probabilities sum to less than 1/40.

LEAF: take 15 = kappa_0 + 1 leaf qubits as the index register (bit j = qubit j). Build
the table incrementally, lab[0] = 0 and lab[x + 2^j] = lab[x] + k_j for x < 2^j:
one addition per entry. The table has length 2^(lam_0), is collimated to p_0 = 0,
and in the ideal run is exactly the tensor product state.

Field widths. A level-i label (output of VEC(i)) is a sum of at most
15 * 2^i leaf labels below 2^(B+1), so it is below 2^(B+1+i+gw) with
gw = 4. Level-i tables are collimated to p_i and stored with
w_i = B + 1 + i + gw - p_i bits per high part.

VEC(i): if i = 0 return LEAF. Otherwise repeat:
- X1 = VEC(i-1);
- X2 = VEC(i-1);
- out = MERGE(X1, X2; p_(i-1), b_(i-1), lam_i);
- if out != FAIL, return out.

TREE_D returns VEC(m), a one-qubit phase vector with labels lab[0] and lab[1],
congruent modulo 2^B. Its ideal state is, up to global phase,
(|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2 with the known integer

    W = (lab[1] - lab[0]) / 2^B = hi[1] - hi[0],                              (7.2)

because the root table is collimated to p_m = B.

Each label is a sum of at most nq_D leaf labels below 2^(B+1), so |W| < 2 nq_D.
Depth-first evaluation holds at most one finished sibling per level.

Size bounds for B <= n and n >= 64:
- Let kmax = kap(mu+15). Since m <= mu and kap is nondecreasing, kappa_i <= kmax
  for every level i <= m-1 used.
- Put x = sqrt(2n) >= sqrt(128) > 11.3. Then mu <= x + 2, t(mu+15) < log2(x+18) + 1 and,
  from the definition, kmax <= log2(x+18) + 2 log2(log2(x+18) + 2) + 6. At x = 11.3 the
  right side is below 4.88 + 5.57 + 6 < 16.5, and its derivative in x is below 0.2 for
  x >= 11.3. Hence kmax + 3 <= 2x and kmax + m + 1 <= kmax + x + 3 <= 3 sqrt(2n).
- Every lam_i is at most kmax + 1 + m <= 3 sqrt(2n), and every b_i <= bmax_i <= 2 lam_i
  <= 6 sqrt(2n) = O(sqrt n).
- The stacked index registers total sum_i lam_i <= (m+1)(kmax+m+1)
  <= (x+3) 3x = 6n + 9 sqrt(2n) <= 8n, since sqrt(2n) >= 9.
- 2^m <= 2^mu <= 4 * 2^(sqrt(2n)).
- By (7.0), 2^(kmax) < 64 (x+18) (log2(x+18) + 2)^2 = O(sqrt(n) (log2 n)^2), so
  sum_(i<m) 2^(kappa_i) <= mu 2^(kmax) = O(n (log2 n)^2).

## 8. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and
tau_j in {0,1}. Since k_j is uniform on [0, 2^(B+1)), low_j and tau_j are
independent and tau_j is a fair bit. Let Gt be the sigma-field generated by:
- all low_j of the tree's leaves, including those of discarded attempts;
- all measurement outcomes (e, bl) of its merges;
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
sort key, rank and block partition uses only label bits below position B,
since Section 6.2 reads bits p..p+b-1 with p + b <= B, together with index
order. Bits below B of a sum of leaf labels depend only on the low_j: adding
multiples of 2^B does not change them. By Lemma 6.1, each measurement's
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

Finite branch (n < 64, i.e. N <= 2^63). For each cand = 0..N-1 in order, use
n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand
at the first minus outcome. Output the first cand with no rejection, or 0.
- For cand = s every outcome is plus.
- For cand != s the two data branches are orthogonal, so each outcome is uniform.
- A union bound over cand gives Pr[wrong] <= N 2^-(n+10) <= 2^-10.
- Q <= N(n+10), and all other resources are bounded by absolute constants.

Main branch (n >= 64). Compute a2, M, d, J, K and all tree parameters. Let mu*
be mu at B = n. Then m(B) <= mu(B) <= mu* for every B <= n used. Put

    Q* = 90 * 2^(mu*) ((J+1)K + 2 a2) + 2 a2,    Qcap = 1024 Q*,

and then h_e, h_A, t_V and Cf from Section 5. A binary down-counter of acquisitions is kept,
at amortized O(1) bit flips per acquisition. CS1 stops, releases everything
and outputs 0 before an acquisition would exceed Qcap. Otherwise it runs
Section 9 and then Section 10. Parameter, CRT and table computations are
polynomial in n.

Lemma 11.1 (expected ideal acquisitions). In the ideal UNCAPPED run, the
expected number of acquisitions is at most Q*.

Proof. An accepted leaf qubit needs at most 2 acquisitions in expectation
(acceptance probability > 1/2 in Section 9, and 1 in Section 10). Let Qv_i be the
expected number of acquisitions until VEC(i) returns, so Qv_0 <= 2 * 15 = 30.
By Lemma 6.1 and (7.1), each merge attempt producing level i+1 succeeds with
conditional probability at least 1 - 2^-(kappa_i) given everything before it. By
Wald's identity, Qv_(i+1) <= rt_i * 2 Qv_i, where rt_i = 1/(1 - 2^-(kappa_i)). Since
every 2^-(kappa_i) <= 2^-14 and their sum is below 1/40 (Section 7),
rt_0 ... rt_(m-1) <= exp(sum_i 2^-(kappa_i)/(1 - 2^-14)) < 1.03 < 3. So
Qv_m <= 3 * 2^m * 30 <= 90 * 2^(mu*). Section 9 runs (J+1)K trees.
Section 10 needs, per bit, an expected 2 trees by (8.3), or, when wd = 1, an
expected 2 single acquisitions since kk is uniform on {0,1}. Summing gives the bound. QED.

Lemma 11.2 (work per branch). On every actual branch of the main branch, the
number of core steps is at most
O(n^2 (log2 n)^2) Qcap + O(n^(5/2) nq) + poly(n),
where nq = nq_d.

Proof. Charge every core step to an acquisition, or to the fixed-length loops.
- Each acquisition (transform, acceptance test, X, counter update) takes O(n^2)
  core steps. All LE calls together take O(n^2 log n) Qcap + O(n^(5/2)) core
  steps on every branch (Section 5.6), since there is one LE call per
  acquisition and Q <= Qcap.
- A leaf table of 2^15 entries costs O(n 2^15) = O(n) core steps, charged to its
  15 acquisitions.
- A merge attempt producing level i+1 costs O(n (2^(lam_i) + 2^(lam_(i+1)))) =
  O(n 2^(kappa_i+1+i)) (Section 6), since lam_(i+1) <= lam_i + 1 + dk_i <= lam_i + 4
  and lam_i <= kappa_i + 1 + i. Its two inputs were built from 2^(i+1) * 15
  acquisitions that no other attempt at that level uses, since inputs of a
  failed merge are discarded and never reused. That is O(n 2^(kappa_i)) per
  acquisition at level i. Each acquisition lies below at most one merge attempt
  per level, so its total share is O(n sum_(i<m) 2^(kappa_i)) = O(n^2 (log2 n)^2)
  per acquisition, by the last size bound of Section 7.
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

Throughout, n >= 64; the finite branch is O(1). We use
m <= mu* <= sqrt(2n) + 2 and 2^(mu*) <= 4 * 2^(sqrt(2n)). Put kmax* = kap(mu*+15); every
kappa_i of every tree is at most kmax*, and by (7.0) with x = sqrt(2n),
2^(kmax*) < 64 (x+18) (log2(x+18) + 2)^2 = O(sqrt(n) (log2 n)^2).

Sizes. log2 nq = O(sqrt n), K = O(sqrt n), J + 1 <= n and a2 <= n. So
(J+1)K + 2 a2 = O(n^(3/2)), and Q* = O(n^(3/2) 2^(sqrt(2n))). Also
log2 Qcap = O(sqrt n), so h_e = O(sqrt n), and h_A, T_V = O(log n).

Q. On every branch, Q <= Qcap = 1024 Q* = O(n^(3/2) 2^(sqrt(2n))).

Core steps. By Lemma 11.2, O(n^2 (log2 n)^2) Qcap = O(n^(7/2) (log2 n)^2 2^(sqrt(2n))).
The decoder term O(n^(5/2) nq) = O(n^(5/2) 2^(sqrt(2n))) is smaller, and the
poly(n) setup is O(2^(sqrt(2n))).

S_Q. The depth-first stack holds at most 8n index qubits (Section 7). A merge
adds O(sqrt n) qubits of registers. LE uses O(n) qubits (data, ancilla,
arithmetic), and the data register is reset after each call. Transforms use
O(n), and each root qubit is measured at once. Released registers are reused.
So S_Q = O(n).

S_C. At any time the depth-first stack holds at most two tables per level (a
finished sibling and the table being built or merged) plus one merge output.
Every table has at most 2^(lam_max) entries, lam_max = kmax* + 1 + m - s (the
LENGTH CAP of Section 7). Each stored label or high part has at most 3n bits,
because a level-i label is below 2^(B+1+i+gw) and B + 1 + i + gw <= 3n. Each
residue has at most n bits. So the tables use at most
3(m+1)(3n 2^(lam_max) + n) = O(n^(3/2) 2^(kmax*+m-s)) bits.
- Merge scratch is O((2^lam + 2^lam') sqrt n) = O(2^(lam_max) sqrt n) bits (Section 6.2).
- The decoder stores K triples (W_i, beta_i, Z_i) and K running residues, all
  O(n) bits each.
- The table of Section 4 is O(1). Counters and parameters are O(n) bits. LE
  uses O(n log n) classical scratch (Section 5.3) and the fallback counter.

Hence S_C = O(n^(3/2) 2^(kmax*+m-s)) + O(n^2) = O(n^2 (log2 n)^2 2^(m-s)), using
2^(kmax*) = O(sqrt(n) (log2 n)^2).
Now bound m - s over all trees, which have B <= n. For a tree, m - s <= mu - floor(sqrt mu).
The map x -> x - floor(sqrt x) is nondecreasing on positive integers (the floor of the
square root grows by at most 1 per step), and mu <= mu* = ceil(sqrt(2n)) + 1. So
m - s <= mu* - floor(sqrt(mu*)) <= (sqrt(2n) + 2) - (sqrt(mu*) - 1) <= sqrt(2n) + 3 - (2n)^(1/4),
using mu* >= sqrt(2n). Therefore

    S_C = O(n^2 (log2 n)^2 2^(sqrt(2n) - (2n)^(1/4))).

These are fixed allocations, so the bound holds on every branch.

T. By (2.1), with log2(S_C + S_Q + 2) = O(sqrt n),
T = O(n^(7/2) (log2 n)^2 2^(sqrt(2n))) * O(sqrt n) + (n+1) Qcap = O(n^4 (log2 n)^2 2^(sqrt(2n))).

All four bounds hold simultaneously for the same execution, with absolute
constants independent of N, s and outcomes.

## 14. Exact growth indices and declared envelopes

With a = u_333/v_333 > sqrt 2 (Section 0) the envelopes are

    B_T(n) = n^4 (log2 n)^2 2^(a sqrt n),     B_C(n) = 2^(a sqrt n - n^(1/4)),
    B_Q(n) = n,                               B_samples(n) = n^(3/2) 2^(a sqrt n).

By Sections 0 and 13 the resources are O of these. For B_C this uses
n^2 (log2 n)^2 2^(sqrt(2n) - (2n)^(1/4))
    <= 2^(a sqrt n - n^(1/4)) * 2^(2 log2 n + 2 log2 log2 n - (2^(1/4) - 1) n^(1/4)),
where 2^(1/4) - 1 > 0.189 and 0.189 n^(1/4) >= 2 log2 n + 2 log2 log2 n for all
n >= 2^40 (at n = 2^40 it is 193.5 >= 80 + 10.7, and the ratio of the right side to
n^(1/4) decreases there); smaller n only affect the
constant. For B_C, log2 B_C = a sqrt n - n^(1/4), so log2 log2 B_C = (1/2) log2 n +
log2 a + o(1) and g(B_C) = 1/2. For
B(n) = 2^(a sqrt n) n^pw (log2 n)^lw with pw, lw >= 0, we have
log2 B = a sqrt n + O(log n). So log2 log2 B = (1/2) log2 n + log2 a + o(1), and
g(B) = 1/2. For B_Q(n) = n, log2 log2 n / log2 n -> 0, so g = 0. The structured
objects in submission.json are exactly these envelopes.

## 15. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy
is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does
not assert that robustness is impossible.
