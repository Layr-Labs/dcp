# CS1-C3L: linear-merge collimation and a free-frequency phase decoder

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single
algorithm CS1-C3L below receives N in binary and fresh independent copies of rho_s,
and outputs the entire s with unconditional probability at least 1 - 2^-8 > 2/3.
On EVERY execution branch (including every failure, retry, discard and abort)
it satisfies jointly

    T   = O(n^4 2^(sqrt(2n))),
    S_C = O(n^2 2^(sqrt(2n) - sqrt(3)*(2n)^(1/4))),
    S_Q = O(n),
    Q   = O(n^(7/4) 2^(sqrt(2n)-(2n)^(1/4))).

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
n^4 2^(a sqrt n), 2^(a sqrt n - 2 n^(1/4)), n, and 2^(a sqrt n-n^(1/4)),
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
CS1-C3L restates and fully reproduces each:
- the Kitaev-test label extraction (Kitaev, quant-ph/9511026);
- the top-bit independence argument;
- the CRT unit multiplier for the odd part of N;
- the exhaustive finite branch.
No earlier verdict is a premise.

The source algorithm, exact verified Kitaev label routine, linear-merge
instrument, free-frequency decoder and controlled source transforms are
retained from CS1 and CS1-C3. The changes are longer initial phase vectors,
a compensating shorter tree and a revised deterministic source cap.
The increased leaf length reduces the required source copies by a
stretched-exponential factor while keeping the total-work and memory bounds
stated in Section 0. It also suppresses label-extraction work below merge
work, without any approximate QFT or new rotation compiler.

Direct material sources: CS1 submission f1481815-9577-4990-abe3-7b79fa5d9284,
archive 200ef0387acb280adcd272f4fbcdb805d1786bbe, and this solver's CS1-C3
submission 6e91de62-9a4f-4f08-bfa8-1beacca11e0f, published archive
f248f9f242c21046223007c9462332b9d738e0bb. The latter contributes the
capacity-slack memory cap; the former supplies almost all algorithmic
components and proof text, reproduced here with attribution. Previous
verdicts are not premises. The CS1-C3Q approximate-QFT and CS1-C3A arithmetic
variants were considered during this research but are not executed here.


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
(Cf+1)-st one, CS1-C3L stops, releases everything and outputs 0 (ABORT).

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
(sqrt n + 1)/n decreases. Also Cf>=20 by the revised cap of Section 11. Indeed, write
n=a2+ceil(log2 M). For M>=3 the definition of J gives
J+1=floor(log2 M)>=ceil(log2 M)/2, and K>=1. For M=1 the term
2a2 alone is 2n. Thus ((J+1)K+2a2)>=n/2 in all cases, and
Qbase>=2^20 gives Qcap>=3*2^30 n. This implies Cf>=20 for n>=64.
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

IDEAL run. The ideal run is CS1-C3L in the latent-label model with every LE output
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

## 7. Longer-leaf tree TREE_D

Input is a supplier of independent positive leaf qubits with known uniform
labels on [0,2^D), D>=2. Put B=D-1. All square roots below are rounded by
integer-square comparisons, not floating arithmetic.

For B<128 retain the C3 parameters:

    mu=ceil(sqrt(2B))+1, kappa=ceil(log2 mu)+1,
    ell=0, s=min(mu-1,floor(sqrt(3mu))).

Choose m minimally with m>=s+1 and
m(m+1)/2-s(s-1)/2+kappa>=B, and put h=m.
For B>=128 use instead

    mu=ceil(sqrt(2B))+2, kappa=ceil(log2 mu)+1,
    ell=floor(sqrt(mu)), s=floor(sqrt(3mu)),
    h=min{h>=ell+s+1:
      h(h+1)/2-[ell(ell-1)+s(s-1)]/2+kappa>=B},
    m=h-ell.

In both cases put ell0=kappa+1+ell and t=m-s>=1. The lengths and stage
capacities are

    lambda_i=ell0+min(i,t) (0<=i<m), lambda_m=1,
    bmax_i=ell+i (0<=i<t),
    bmax_i=ell+t+1 (t<=i<=m-2),
    bmax_(m-1)=kappa+2ell+2t+1.

Thus the initial vector has ell0 qubits, the table lengths grow until
level t, remain capped for the last s-1 levels below the root, and the
root is one qubit. Allocate b_(m-1),...,b_0 greedily in reverse order:
b_i=min(bmax_i,B-already_allocated). Put p_0=0, p_(i+1)=p_i+b_i.

Parameter/capacity proof. For the small-B case mu>=3, s+1<=mu,
2B<=(mu-1)^2, and s(s-1)<=3mu-1. Thus
mu(mu+1)-s(s-1)>=(mu-1)^2>=2B, proving m<=mu.
For the large-B case mu>=18. The bound
ell+s+1<=3sqrt(mu)+1<=mu holds for mu>=16, since sqrt(mu)<=mu/4.
Also ell(ell-1)+s(s-1)<=4mu and 2B<=(mu-2)^2, so

 mu(mu+1)-ell(ell-1)-s(s-1)
 >=mu(mu+1)-4mu >=(mu-2)^2 >=2B.

The middle inequality uses mu>=4. Therefore h=mu is feasible,
h<=mu and m<=mu-ell. In both cases m>=s+1 and
2^kappa>=2mu>=2m, with 2^kappa<=4mu.
Summing the displayed capacities gives

 sum_i bmax_i
 =m(m+1)/2+(m+1)ell-s(s-1)/2+kappa
 =h(h+1)/2-[ell(ell-1)+s(s-1)]/2+kappa >=B.

Hence the reverse greedy allocation finishes with sum_i b_i=B.
In the growing, capped and root cases, direct substitution gives

    b_i+lambda_(i+1)-2lambda_i <= -kappa.                       (7.1)

Lemma 6.1 therefore bounds each merge failure by 2^-kappa<=1/(2m),
regardless of tables or phases. No random-distribution assumption is used.

LEAF takes ell0 leaf qubits as an ell0-qubit index and builds the table
by repeated subset-sum doubling, lab[0]=0 and
lab[x+2^j]=lab[x]+k_j, j=0,...,ell0-1. The vector is the tensor product
of those qubits and has length 2^ell0, collimated to p_0=0.

A level-i label sums at most 2^i ell0 original labels below 2^(B+1).
Put gw=ceil(log2 ell0) and store high parts with fixed width
w_i=B+1+i+gw-p_i. This bounds every actual label. The quantum index
and all classical arrays have these deterministic widths even on erroneous
label branches; LE always returns a label in range and acceptance enforces
the declared leaf range.

VEC(0) returns LEAF. For i>0 repeatedly build X1=VEC(i-1), X2=VEC(i-1),
and MERGE(X1,X2;p_(i-1),b_(i-1),lambda_i). Return a successful output;
on FAIL both inputs are reset and released before retrying.
TREE_D returns VEC(m), whose known integer multiplier is

    W=(lab[1]-lab[0])/2^B=hi[1]-hi[0],

and whose ideal qubit is (|0>+exp(2pi i 2^B W th)|1>)/sqrt2, up to
an overall phase. Put nq_D=2^m ell0. Then |W|<2nq_D.

Uniform size bounds, B<=n: mu<=sqrt(2n)+3, kappa=O(log n),
ell=O(n^(1/4)), m=O(sqrt n), and every lambda_i,b_i=O(sqrt n).
The depth-first quantum index stack is O(n). For large B,
h<=mu and lambda_max=kappa+1+h-s. For small B, mu<=17 and
nq_D<=2^17*7<2^20. The small branch is a fixed finite tree family,
not an uncharged exhaustive search over source data.

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

Main branch (n>=64). Compute a2,M,d,J,K and tree parameters exactly as
in Sections 9 and 10, using the longer-leaf TREE_D of Section 7. Put

    mu*=ceil(sqrt(2n))+2, ell*=floor(sqrt(mu*)),
    kappa*=ceil(log2 mu*)+1,
    Qbase=max(2^20,2^(mu*-ell*)*(kappa*+1+ell*)),
    Q*=6Qbase*((J+1)K+2a2)+2a2, Qcap=1024Q*.

The constants and counters are generated by counted integer algorithms.
Set LE confidence and fallback parameters using this Qcap as in Section 5.
Stop, release registers and output zero before an acquisition would exceed
Qcap; otherwise run Sections 9 and 10. All setup is polynomial in n.

Lemma 11.1. Every tree has nq_D<=Qbase, and expected ideal uncapped total
acquisitions are at most Q*.

Proof. If B<128, Section 7 gives nq_D<2^20. Otherwise mu<=mu*, and the
integer function x-floor(sqrt x) is nondecreasing, so
m<=mu-floor(sqrt mu)<=mu*-ell*. Also ell0<=kappa*+1+ell*.
Thus nq_D<=Qbase. An accepted leaf qubit requires at most two acquisitions
in expectation. As in the inherited distribution-free retry argument,
Qv_(i+1)<=2 rt Qv_i, where rt=2^kappa/(2^kappa-1).
Since 2^kappa>=2m, rt^m<=exp(m/(2^kappa-1))<=e<3.
Therefore E Qv_m<=6*2^m ell0<=6Qbase. There are (J+1)K odd-part trees.
Each 2-adic bit needs two trees in expectation, or two direct acquisitions
when wd=1. Summing yields Q*. This is uniform over all histories; no
favorable-table conditioning or free retry is used. QED.

Lemma 11.2. On every actual branch, core work is at most

 O(n^(7/4)2^ell*)Qcap + O(n^2 log n)Qcap + O(n^(5/2)nq_d)+poly(n).

Proof. LE and data transforms use O(n^2 log n) per acquired copy in total,
plus O(n^(5/2)), by Section 5.6. This includes all high-confidence fallback
runs under their original cap. Copies, resets, leaf acceptance and counters
are also covered.
A merge at level i+1 costs O(n*2^(kappa+1+ell+i)) core steps. Its two
inputs consumed at least 2^(i+1)ell0 accepted leaf qubits, hence at least
that many acquisitions. Each acquisition pays at most one merge attempt
per level, since failed inputs are discarded. The share per acquisition,
summed over at most m levels, is O(n*m*2^(kappa+ell)/ell0).
For B>=128, m=O(sqrt B), 2^kappa=O(sqrt B), and
ell0>=floor(sqrt mu)=Omega(B^(1/4)). Thus this charge is
O(n B^(3/4)2^ell)<=O(n^(7/4)2^ell*).
For B<128, all tree parameters are bounded constants, so the share is O(n).
Leaf-table building costs O(n*2^ell0) shared by ell0 acquisitions, smaller
than the same bound. This is deterministic branchwise charging, not an
expected-time estimate. It covers abandoned partial trees.

Root measurements cost O(n) per tree. The unchanged decoder costs
O(n^(5/2)nq_d), omitting its term when the odd part is absent. All setup,
CRT arithmetic, parameters, confidence caps and rational tables are polynomial
in n. Every other loop is fixed-length or consumes counted acquisitions.
QED.

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

## 13. Joint resources on every branch

Asymptotic estimates below use n>=128; the finite prefix is absorbed by
absolute constants under the same explicitly bounded algorithms. We have
mu*<=sqrt(2n)+3 and ell*>=sqrt(mu*)-1>=(2n)^(1/4)-1.
Also kappa*+1+ell*=O(n^(1/4)). Since Qbase is the maximum of a fixed
constant and a positive growing term, it obeys

 Qbase=O(n^(1/4)2^(mu*-ell*)),
 Qcap=O(n^(7/4)2^(mu*-ell*))
     =O(n^(7/4)2^(sqrt(2n)-(2n)^(1/4))).

Here K=O(sqrt n), J+1<=n and a2<=n, as before. On every branch Q<=Qcap,
so this proves the claimed source-copy bound, including all discarded copies.
The logarithm of Qcap remains O(sqrt n), so h_e=O(sqrt n), while h_A,T_V=O(log n).

Core work. The first term of Lemma 11.2 is
O(n^(7/4)2^ell*)*O(n^(7/4)2^(mu*-ell*))=O(n^(7/2)2^mu*).
The LE term is O(n^(15/4)log n 2^(mu*-ell*)), which is smaller because
n^(1/4)log n/2^ell* is bounded and tends to zero. The decoder and polynomial
setup are also smaller. Thus total core work is O(n^(7/2)2^(sqrt(2n))).
This cancellation of the leaf-boost exponent is exact in the charged bound;
no slack in a-sqrt2 is used.

Quantum space. Section 7 gives O(sqrt n) levels with index lengths O(sqrt n),
hence O(n) stacked qubits. A merge uses O(sqrt n) additional scratch.
LE and the original data transforms use O(n) qubits. Released registers are
reused. Therefore S_Q=O(n) on every branch.

Classical space. Labels sum at most 2^i ell0 leaf labels, so each full label
or high part has O(n) bits by Section 7. A depth-first stack keeps at most
two tables per level plus one merge output. All large-B tables have at most
2^(kappa+1+h-s) entries with h<=mu; their total storage is
O(n^(3/2)2^(kappa+mu-s))=O(n^2 2^(mu-s)). Merge scratch is smaller.
For integers x>=18 the function x-floor(sqrt(3x)) is nondecreasing.
Since mu<=mu*, and s=floor(sqrt(3mu))>=sqrt(3mu)-1,

 mu-s<=mu*-floor(sqrt(3mu*))
      <=sqrt(2n)+4-sqrt(3)*(2n)^(1/4).

For small B<128, the C3 parameters have mu<=17, kappa<=6 and
lambda_max<=17; their stack storage is only O(n) with a fixed absolute
constant. LE, counters and decoder add at most polynomial scratch.
The resulting total is

 S_C=O(n^2 2^(sqrt(2n)-sqrt(3)*(2n)^(1/4))).

All allocations have deterministic widths, including error and abort branches.
The peak address width is O(sqrt n), so Eq. (2.1) finally gives

 T=O(n^(7/2)2^(sqrt(2n)))*O(sqrt n)+(n+1)Qcap
  =O(n^4 2^(sqrt(2n))).

These four guarantees apply jointly to the same longer-leaf configuration.

## 14. Exact growth indices and declared envelopes

With a = u_333/v_333 > sqrt 2 (Section 0) the envelopes are

    B_T(n) = n^4 2^(a sqrt n),     B_C(n) = 2^(a sqrt n - 2 n^(1/4)),
    B_Q(n) = n,                               B_samples(n) = 2^(a sqrt n-n^(1/4)).

For samples the proved bound divided by the declared envelope is at most
n^(7/4)2^(-(2^(1/4)-1)n^(1/4)), since a>sqrt2. It tends to zero,
so the structured sample envelope holds independently of the gap a-sqrt2.
Its logarithm is a sqrt n-n^(1/4), giving growth index 1/2.
By Sections 0 and 13 the resources are O of these. For B_C, write
c=sqrt(3)*2^(1/4)>2, because c^4=18>16. Since a>sqrt(2),

 n^2 2^(sqrt(2n)-c n^(1/4)) / 2^(a sqrt n-2 n^(1/4))
 <= 2^(2 log2 n-(c-2)n^(1/4)).

This tends to zero, since log2 n/n^(1/4) tends to zero; it is bounded on
all positive integer n after enlarging the absolute outside constant.
This conversion uses the strict subleading margin c>2, independently of
how close a is to sqrt(2). For B_C, log2 B_C=a sqrt n-2 n^(1/4),
so log2 log2 B_C=(1/2)log2 n+log2 a+o(1), proving g(B_C)=1/2. For
B(n) = 2^(a sqrt n) n^pw (log2 n)^lw with pw, lw >= 0, we have
log2 B = a sqrt n + O(log n). So log2 log2 B = (1/2) log2 n + log2 a + o(1), and
g(B) = 1/2. For B_Q(n) = n, log2 log2 n / log2 n -> 0, so g = 0. The structured
objects in submission.json are exactly these envelopes.

## 15. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy
is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does
not assert that robustness is impossible.
