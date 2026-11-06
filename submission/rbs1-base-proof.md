# RBS1: ramped failure budgets with a square-root index offset

## 0. Theorem and notation

For every integer N >= 2 and s in Z/NZ, let n = ceil(log2 N). The single
algorithm RBS1 defined below recovers the entire s from independent ideal
DCP source copies with unconditional probability at least 1-2^-8 > 2/3.
On EVERY execution branch, including failures, discards, retries and aborts,
its jointly charged resource bounds are

    T   = O(n^4 2^(sqrt(2n))),
    S_C = O(n^2 2^(sqrt(2n) - 2(2n)^(1/4))),
    S_Q = O(n),
    Q   = O(n^(3/2) 2^(sqrt(2n) - (2n)^(1/4))).

Here T includes classical bit operations, quantum gates, circuit generation,
initialization and disposal, source acquisition, and every address charge.
All constants are absolute and independent of N, s and all outcomes. These
are proved upper bounds, not a claim of optimality for this architecture.

Let (u_0,v_0)=(10,7) and (u_(k+1),v_(k+1))=(3u_k+4v_k,2u_k+3v_k).
The identity (3u+4v)^2-2(2u+3v)^2=u^2-2v^2 gives u_k^2-2v_k^2=2.
Thus a=u_333/v_333 is a fixed exact rational greater than sqrt(2).
The exact fraction a is

    8441478004666748666153322414015794961054342923175177808658686557734489303162152388494751245868147491831446292476962720233203201073933816582585276436077865535199430405176591394221939485167179701583924490203278327423413823406808776174974568608124494762509770/5969026340336944451114480739433819709407468170415945417713771714885974444504222882421291476798989652766383498455240579454394404150586732509003361709530480614304768144606668970442415970951831495263198155709406532002051594173677103082229495028847707209502393

The five declared guarantees in submission.json use the SAME configuration:

    B_T(n) = n^4 2^(a sqrt n),
    B_C(n) = 2^(a sqrt n - 2n^(1/4)),
    B_Q(n) = n,
    B_samples(n) = n^(3/2) 2^(a sqrt n - n^(1/4)),
    epsilon(n) = 0 under the exact clean-input model of Section 15.

Growth indices are 1/2, 1/2, 0, 1/2. Section 14 proves these representations
and compares their entire normalized vector with the actual CS1 time leaders.
The improvement is derived at the actual irrational coefficient sqrt(2);
no polynomial or logarithmic saving is inferred from the tiny slack in a.

Notation: d=floor(log2 N); N=2^a2 M with M odd; s1=s mod M;
s=s1+M s2 (mod N), 0<=s2<2^a2; omega=exp(2 pi i/N).
The letter s always denotes the secret; sigma denotes a tree's cap length.
Labels are known integers, W is a known integer frequency, and hd is a
Hamming distance. All integer square roots, ceilings of binary logarithms,
and powers of two are computed exactly, using integer comparisons.

## 1. Provenance and new contribution

Material reuse: this proof reproduces and adapts CS1's explicit source
transforms, verified label extraction, linear merge, top-bit independence,
free-frequency decoder, 2-adic recovery, and finite branch. The exact source
is evaluated commit 4bd1700e634c8b1f2ebcf6cc8126360622e08a1c,
archive path submission/proof.md, published submission
b56c7ceb-de59-42da-9e3b-6ee96e4e4145 (same full time as
f1481815-9577-4990-abe3-7b79fa5d9284). Its proof SHA-256 is
e1b698d021f72cc5fd17f0132a2c30ba213dc2c424e613087d711804f074b528.
The refreshed CS1-C3 proof was also read at exact evaluated commit
f248f9f242c21046223007c9462332b9d738e0bb, archive path
submission/proof.md, SHA-256
c790bf765bcd1dd4cda653656ec9c79bc07520a051c29dcd7d2094fc57121a50.
It increases the cap to floor(sqrt(3mu)) and declares classical exponent
-2n^(1/4), with unchanged full time. The final RBS1 configuration therefore
uses the explicit cap 2floor(sqrt(m)); (7.2) rederives its feasibility with
our different depth and offset, preserving that stronger declared space.
No historical verdict is a mathematical premise: all needed arguments are
included here. The owner harmonic-schedule proposal motivated variable
failure budgets; its exact telescoping cancellation is extended in Section 7.

New configuration: kappa_i grows linearly from 3 to 3+ceil(log2 m), so the
leaf uses exactly five source qubits and the retry product stays below 2.
An additional slowly introduced index offset v=floor(sqrt(ceil(sqrt(2B))))
permits depth m=ceil(sqrt(2B))-v+4. Capping the final sigma=2floor(sqrt m)
levels preserves the classical-memory saving. Sections 7, 11 and 13 give
the exact capacity identity and the all-branch source/work accounting.

Primary sources browsed, with applicability limited to these statements:

- G. Kuperberg, arXiv:1112.3333v1, 14 December 2011,
  https://arxiv.org/html/1112.3333v1 . Algorithm 4.1 gives phase-vector
  collimation; Section 4.6 gives distribution-free bucket trimming and
  untouched high-bit reasoning. Proposition 4.2 assumes QRACM and its
  quantum-time bound is NOT imported. Corollary 4.3 treats linear access.
  The sqrt(2n) estimate in Section 4.5 is explicitly heuristic and is NOT
  used. Here explicit linear circuits and deterministic schedules prove
  every required bound without QRAM or a hidden-shift/subset-sum oracle.
- A. Yu. Kitaev, quant-ph/9511026v1, 20 November 1995,
  https://arxiv.org/pdf/quant-ph/9511026v1 . Section 3, equations (16)-(19)
  and Lemmas 9-10 concern eigenvalue tests with controlled known unitaries
  and powers. Here each test is implemented as counted modular translation
  on the supplied data register. No coherent access to, purification of,
  or inverse of the DCP source is assumed. The extraction proof and all
  confidence/bit costs are restated in Section 5.

Remote Wolfram calculations are supporting algebra checks only. Neither
finite checks nor symbolic simplification is a premise about adaptive
quantum independence, success, or worst-case costs.

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
(Cf+1)-st one, RBS1 stops, releases everything and outputs 0 (ABORT).

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
(sqrt n + 1)/n decreases. Also Cf >= 20: Section 11 gives Qcap>=6*1024*nq*, with
nq*=5*2^m*. For integer u*>=2 and v*=floor(sqrt u*), m*=u*-v*+4>=u*/2.
For integer u*>=4, 2^(u*/2)>=u* (induct on u* by 2, checking 4 and 5);
u*=2,3 hold directly with m*. Hence 2^m*>=u*>=sqrt(2n), so
Qcap>=30720 sqrt(2n)>20(sqrt n+1) and Cf>=20.
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

IDEAL run. The ideal run is RBS1 in the latent-label model with every LE output
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

## 7. Exact tree schedule and frequency bound

TREE_D receives independent leaf qubits with labels uniform on [0,2^D),
D>=2. Put B=D-1. Define integer parameters

    u = ceil(sqrt(2B)), v = floor(sqrt(u)), m = u-v+4,
    sigma = 2 floor(sqrt(m)), t = m-sigma, h = ceil(log2 m),
    kappa_i = 3+min(i,h), delta_i = min(max(i-1,0),v)   (0<=i<m),
    lambda_i = min(i,t)+kappa_i+2+delta_i              (0<=i<m),
    lambda_m = 1,
    bmax_i = 2 lambda_i-lambda_(i+1)-kappa_i           (0<=i<m).

The additive offset delta rises from 0 to v, and the base index growth is
capped during the last sigma levels. All choices depend only on D.

### 7.1 Feasibility, including every rounded offset and the root

Since u>=2, 1<=v<=sqrt(u), m>=5, and m>=v+2: indeed
u+2-2v >= v^2+2-2v = (v-1)^2+1 >0. Thus delta_(m-1)=v.
For m=5, sigma=4<m. For m>=6, 2sqrt(m)<=m-1, so again
1<=sigma<m and t>=1. Consecutive kappa and delta increments are
in {0,1}. For 0<=i<m-1, writing their increments as Dk_i and Dd_i,

    bmax_i = i+1-Dk_i+delta_i-Dd_i     if i<t,
    bmax_i = t+2-Dk_i+delta_i-Dd_i     if i>=t.

At i=0, Dk_0=1 and delta_0=delta_1=0, so bmax_0=0.
For i>=1 the first expression is >=i-1+delta_i>=0; the second is
>=t+delta_i>=0. At the root,

    bmax_(m-1) = 2t+kappa_(m-1)+3+2v >0.

There are no negative bit budgets. Telescoping gives exactly

    C = sum_(i=0)^(m-1) bmax_i
      = m(m+3)/2 - sigma(sigma-1)/2 + 4 + vm-v(v+3)/2.             (7.1)

Proof: lambda_0=5 and lambda_m=1, so the sum is
lambda_0-1 + sum_(i=0)^(m-1)(lambda_i-kappa_i).
The capped staircase sums to m(m-1)/2-sigma(sigma-1)/2.
Since m>=v+2, sum delta_i=vm-v(v+3)/2. This proves (7.1), including
the entire root offset and all rounding; no kappa terms remain.

Set q=m+v=u+4. Since sigma(sigma-1)<=4m, expanding (7.1) yields

    C >= u^2/2 + (7/2)u + 10 - v^2 - v
      >= u^2/2 + (5/2)u + 10 - v
      >= u^2/2 + (3/2)u + 10 >= B,                              (7.2)

using v^2<=u and v<=u. Greedily allocate b_(m-1),...,b_0 from the root
downwards: b_i=min(bmax_i, B-sum of already allocated bits). Thus
0<=b_i<=bmax_i and sum b_i=B. Set p_0=0 and p_(i+1)=p_i+b_i.
Then p_m=B and p_i+b_i<=B at every merge.

The depth obeys both

    m <= sqrt(2B)+4,
    m <= sqrt(2B)-(2B)^(1/4)+6,                                  (7.3)

because u<sqrt(2B)+1 and v>sqrt(u)-1. In particular m retains the
requested sqrt(2B)+O(1) envelope; the actual depth is smaller.

### 7.2 Failure budgets and retry product

Lemma 6.1 gives Pr[FAIL | input tables] <= 2^-kappa_i=:pFail_i.
The bound holds for arbitrary tables, not just randomly distributed ones.
Since h=ceil(log2 m),

    sum_(i=0)^(m-1) pFail_i
      <= sum_(i=0)^infinity 2^(-3-i) + m 2^(-3-h)
      <= 1/4+1/8=3/8.

Each pFail_i<=1/8. The inequality -ln(1-x)<=x/(1-x) gives

    product_(i=0)^(m-1) (1-pFail_i)^(-1)
      <= exp((8/7)(3/8))=exp(3/7)<2.                            (7.4)

For example exp(3/7)<1/(1-3/7)=7/4<2 follows termwise from the
power series, so this constant requires no numerical approximation.

### 7.3 Tree algorithm and label fields

LEAF takes exactly five accepted leaf qubits. Its five-bit register indexes
the tensor product, with table lab[0]=0 and
lab[x+2^j]=lab[x]+k_j for j=0,...,4 and 0<=x<2^j.
It is a phase vector of length 32, collimated to p_0=0.

VEC(0) returns LEAF. For i>=1, VEC(i) repeatedly obtains fresh
X1=VEC(i-1) and X2=VEC(i-1), then runs
MERGE(X1,X2;p_(i-1),b_(i-1),lambda_i). On FAIL it discards both
inputs and retries; otherwise it returns the output. TREE_D returns VEC(m).
The global source cap of Section 11 applies even partway through recursion.
No failed input is reused. Finished siblings are stored depth first.

Set nq_D=5*2^m. This is the number of distinct source qubits supporting a
retry-free root, and also an upper bound on the number of leaf coordinates
in the two returned entries: each is a sum using a subset of these nq_D
coordinates. Retries add discarded copies, counted in Section 11.
At level i a label is a sum of at most 5*2^i labels below 2^(B+1), hence
is below 2^(B+i+4). Store the common residue and high parts as in Section 6,
using width w_i=B+i+4-p_i. These fixed positive widths also suffice when
LE outputs erroneous labels, since its outputs still lie in the valid range.

The returned two labels agree modulo 2^B. The root is ideally

    (|0>+exp(2 pi i 2^B W th)|1>)/sqrt(2),
    W=(lab[1]-lab[0])/2^B=hi[1]-hi[0],     |W|<2 nq_D.           (7.5)

Every distinct index has a distinct leaf-incidence vector: at a leaf this
is binary encoding, at a merge it is concatenation on disjoint supports,
and reindexing is injective. This fact is used in Section 8.

### 7.4 Length, monotonicity, and cap estimates

For i<m, 2^kappa_i<=8*2^h<16m. Therefore

    L_i=2^lambda_i <=64 m 2^v 2^min(i,t) <=64 m 2^v 2^i.        (7.6)

For i<m-1, lambda_(i+1)-lambda_i<=3, so L_(i+1)<=8 L_i;
the root is shorter. All lambda_i and b_i are O(sqrt n) when B<=n,
since m+v=u+4=O(sqrt n) and h=O(log n). The sum of stacked index
widths is O(m(u+h))=O(n). The largest width satisfies

    lambda_max <= m-sigma+(3+h)+2+v = u-sigma+h+9.              (7.7)

The function u-floor(sqrt u) is nondecreasing on positive integers.
Consequently m(B) and nq_D are nondecreasing as B grows; v(B) is also
nondecreasing. All trees with B<=n are bounded by the parameters at B=n.
Finally sqrt(u)-sqrt(m)<=1 whenever m<u, since
(u-m)/(sqrt(u)+sqrt(m))=(v-4)/(sqrt(u)+sqrt(m))<=v/sqrt(u)<=1.
When m>=u the same lower bound on sqrt(m) is automatic. Hence

    sigma > 2sqrt(u)-4,
    u-sigma <= sqrt(2B)-2(2B)^(1/4)+5.                            (7.8)

The right side is nondecreasing for B>=1. This is the precise memory cap
estimate; the root-depth offset does not erase the saved n^(1/4) exponent.

## 8. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and
tau_j in {0,1}. Since k_j is uniform on [0, 2^(B+1)), low_j and tau_j are
independent and tau_j is a fair bit. Let Gt be the sigma-field generated by:
- all low_j of the tree's leaves, including those of discarded attempts;
- all measurement outcomes (e, bl) of its merges;
- all selection and retry decisions of the controller (merge parameters, FAIL
  and retry decisions, leaf acceptance tests and which copies are used).
Accepted leaf labels in Section 9 are uniform on the accepted interval;
their high/low decomposition is made after acceptance. Rejected source
labels are independent of later accepted labels. All acceptance indicators
may therefore be included without revealing a retained leaf's top bit.
Fixed schedules (including kappa_i, delta_i, lambda_i and all b_i) depend
only on D. Reading high parts to store or add them is not a selection rule:
only the low-bit sort keys, residue measurements and index ranks influence
which coordinates survive. Fields, iteration counts and allocations have
fixed bounds. Gt does NOT include LE's internal coins, test outcomes, accept/reject verdicts or
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
re-indexing is a bijection. So hd = |x0 xor x1| >= 1. From (7.5),

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

## 11. Complete algorithm, fixed caps, and every-branch charging

Finite branch (n<64). For each cand=0,...,N-1, acquire at most n+10 fresh
copies, apply Shift_cand, and measure the control in X. Reject at the first
minus result; output the first candidate with n+10 plus results, or 0.
The correct candidate always passes. For each wrong candidate a fresh test
is fair, since the data branches are orthogonal. Thus the wrong-output
probability is at most N*2^(-n-10)<=2^-10. Q<=N(n+10). Every resource on
this finite set of bit lengths is bounded by an absolute constant, which
can be included in the uniform big-O bounds.

Main branch (n>=64). Compute d, a2, M and the schedules above. If M>1,
use J and K from Section 9; if M=1, define J=-1 and K=0 and skip Section 9.
Let u*,v*,m*,sigma*,h* be the Section 7 parameters at B=n and put

    nq* = 5*2^m*,
    Q* = 6 nq* ((J+1)K+2a2)+2a2,
    Qcap = 1024 Q*.                                             (11.1)

All are explicit integers computed before the first acquisition. Set LE's
h_e,h_A,t_V,Cf exactly as in Section 5 using this Qcap. Stop and output 0
before a source acquisition would exceed Qcap, or before the number of
high-confidence extractions would exceed Cf. Release live registers on
abort. A binary down-counter has amortized O(1) flips per acquisition.
Otherwise execute Sections 9 and 10 and output their full CRT result.

Lemma 11.1. Expected total acquisitions in the ideal uncapped run are <=Q*.

Proof. A leaf qubit costs at most two acquisitions in expectation, uniformly
over all prior history: rejection in Section 9 has probability <1/2 and
Section 10 accepts each copy. Let A_i bound the expected cost of VEC(i),
uniformly over earlier unrelated history and the stage's transformed secret.
A_0<=10. An attempt at level i+1 has conditional expected cost <=2A_i.
Conditional on its obtained input tables, its failure probability is at
most pFail_i. Thus survival to attempt r is at most pFail_i^(r-1).
Summing conditional expected costs over attempts, without assuming cost
independence from the same attempt's outcome, gives
A_(i+1)<=2A_i/(1-pFail_i). Equation (7.4) yields

    A_m <=2*2^m*10=4 nq_D <=6 nq*.

Section 9 uses exactly (J+1)K roots. Section 10 uses an expected two roots
per bit, or two single copies when wd=1, by the untouched top-bit argument.
This remains a cost bound if earlier decoding is wrong: every physical
index amplitude still has equal magnitude, so the diagonal merge outcome
law is independent of its phases. The labels kk are uniform modulo 2^wd
and root oddness still has probability 1/2. Correctness of the phase-bit
measurement itself is asserted only when previous decoded bits are correct.
Summing these costs proves (11.1). Each finite-level retry loop terminates
almost surely; the finite expected bound also establishes this. QED.

Lemma 11.2. Every ACTUAL main-branch run uses at most

    O(n^2 log n + n (m*)^2 2^v*) Qcap
       + O(n^(5/2) nq_d) + poly(n)                             (11.2)

core steps, where nq_d uses B=d-1 (defined even if Section 9 is skipped).

Proof. Transforms, acceptance, X and bookkeeping cost O(n^2) per copy.
Section 5 charges ALL LE calls and their capped fallbacks at
O(n^2 log n)Qcap+O(n^(5/2)), on every branch.
Each leaf table has exactly 32 entries and costs O(n), charged to its five
accepted acquisitions. A merge attempt at level i+1 costs O(n L_i), by
Section 6 and L_(i+1)<=8 L_i. By (7.6) this is
O(n m 2^v 2^i). Its two completed inputs have at least 5*2^(i+1)
distinct acquisitions supporting them, so charge O(n m 2^v) to each.
No acquisition supports two attempted merges at the SAME level: each
input is consumed once, including when the merge fails. An acquisition
supports at most m such charges, one per level. Therefore the total merge
share per acquisition is O(n m^2 2^v)<=O(n(m*)^2 2^v*).
Failed subtrees and a partial subtree at abort obey the same accounting;
discard/initialization costs fit the corresponding table and merge costs.

Root measurement costs O(n) per completed root. The decoder examines
O(nq_d) candidates per stage, K=O(sqrt n) samples per candidate, O(n)
stages, and O(n) bit operations per score update, giving
O(n^(5/2)nq_d). Setup, including at most n tree parameter lists, CRT,
translations, counters and initial decoder residues, is poly(n).
All non-fixed loops require fresh acquisitions, so the source cap ensures
termination on EVERY branch. This is deterministic accounting, not an
expected number of merge attempts substituted into a worst-case claim. QED.

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

## 13. Simultaneous resources on every branch

Use parameters at B=n and write u=u*, v=v*, m=m*, sigma=sigma* here.
They satisfy u<sqrt(2n)+1, v=floor(sqrt u), m+v=u+4, m=O(sqrt n).
Thus nq*=5*2^m and log2(nq*)=O(sqrt n). The fixed K in Section 9 is
O(sqrt n), there are at most n stages, and a2<=n. Equation (11.1) gives

    Qcap = O(n^(3/2) 2^m)
         = O(n^(3/2) 2^(sqrt(2n)-(2n)^(1/4))).                   (13.1)

The second bound follows directly from (7.3), with outer factor at most 64
for 2^m. No number of discarded copies or retries is omitted.
Also log2 Qcap=O(sqrt n), so h_e=O(sqrt n), while h_A,T_V=O(log n).

Core work. Applying (11.2), the merge term is

    O(n m^2 2^v) Qcap
       = O(n^(7/2) 2^(m+v)) = O(n^(7/2) 2^(sqrt(2n))).         (13.2)

The label-extraction term is O(n^(7/2) log n 2^m), no larger than
the same bound. For completeness log2 n=O(2^v): put x=n^(1/4)>=1.
We have v>=x-1, log2 n=4 log2 x<=4x/ln 2, and x=O(2^x)
(for instance 2^x>=x for x>=1). Hence log2 n=O(2^v).
The decoder term O(n^(5/2)nq_d) is smaller; nq_d<=nq*.
Any fixed polynomial setup is O(2^(sqrt(2n))), since
log2 n/sqrt n tends to zero. Thus total core work is
O(n^(7/2) 2^(sqrt(2n))).

Quantum space. The depth-first stack has O(sum lambda_i)=O(n) index
qubits. One merge adds O(sqrt n) scratch. LE and transforms add O(n),
and each root is measured and released before constructing the next.
Hence S_Q=O(n), also on abort and incorrect-label branches.

Classical space. Each high-part field has width at most B+i+4<=3n
for n>=64, and each common residue has at most n bits. At most a constant
number of tables per level are live, plus one merge scratch table.
Equation (7.7) and 2^h<2m give

    S_C <= O(m n 2^(u-sigma+h+9)) + O(n^2)
        = O(n^2 2^(u-sigma)) + O(n^2)
        = O(n^2 2^(sqrt(2n)-2(2n)^(1/4))).                       (13.3)

For a smaller B, use (7.8) and monotonicity of sqrt(2B)-2(2B)^(1/4).
Merge scratch has O(2^lambda_max sqrt n) bits and fits this envelope.
Decoder triples and running residues use O(K n)=O(n^(3/2)); LE scratch
uses O(n log n). The at most n precomputed parameter lists use O(n^2)
bits, and all counters/constants are polynomial space already covered.
Gates are generated and streamed; no exponential circuit description is
stored. Fixed field widths and bounds hold on every actual branch.

Full charged work. Equation (13.3) gives
ceil(log2(S_C+S_Q+2))=O(sqrt n). Multiplying ALL core work by this address
cost, and adding the source cost (n+1)Qcap, yields

    T = O(n^4 2^(sqrt(2n))).                                   (13.4)

Thus all four bounds hold for one algorithm on every branch; the success
statement is unconditional by Section 12.

## 14. Exact declared envelopes, indices, and comparison

The rational a=u_333/v_333>sqrt(2) from Section 0 is exactly CS1's
published coefficient. Therefore 2^(sqrt(2n))<=2^(a sqrt n).
The time, quantum space and sample declarations follow immediately from
(13.1)-(13.4), using (2n)^(1/4)>=n^(1/4). For classical space we absorb
n^2 using the STRICT quarter-power gap, without using any sqrt-power slack:

    n^2 2^(sqrt(2n)-2(2n)^(1/4)) / 2^(a sqrt n-2n^(1/4))
       <= 2^(2 log2 n-2(2^(1/4)-1)n^(1/4)) = O(1).

Indeed 2^(1/4)-1>189/1000, since (1189/1000)^4<2. At n=2^36,
(189/1000)n^(1/4)>2 log2 n; n^(1/4)/log2 n is increasing thereafter
by differentiation. Smaller n form a finite set and change only the
outer constant. This proves exactly the declared classical-space envelope.

For the time, classical-space and sample envelopes,
log2 B = a sqrt n + O(n^(1/4)+log n), so
log2 log2 B=(1/2)log2 n+log2 a+o(1). Their growth indices equal 1/2.
For B_Q=n, log2 log2 n/log2 n tends to zero, so its index is 0.

Comparison uses normalized exact rational logarithmic terms, not numeric
index ties, sort order or memory-only Pareto membership. Relative to the
published CS1 full vector, the declared time ratio is
1/(log2 n)^2 -> 0, the classical-space ratio is 2^(-n^(1/4)) and the quantum bound is identical,
and the sample ratio is 2^(-n^(1/4))/log2 n -> 0. The tolerance fraction
and its error-model text are IDENTICAL. Thus these candidate guarantees,
if accepted as proved, strictly dominate that vector in time, classical
space and samples. Relative to the newly published CS1-C3 rows
15f1d1c3-0ec1-45a3-92ea-f99fcefaef49 and
6e91de62-9a4f-4f08-bfa8-1beacca11e0f, the classical-space envelopes are
identical while the same strict time and sample improvements apply.
They do not merely choose a different leading rational exponent or loosen
an old bound. Equal normalized vectors would be deduplicated by the
prescribed earliest-publication/time-and-ID rule, but these vectors differ.
No assertion about actual publication or a pending submission is made.

## 15. Error tolerance

The fifth claim is epsilon(n)=0 under this exact text:

    Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

Every acquired copy is therefore an independent ideal coset state. Sections
3-12 establish unconditional full-secret success jointly with all resource
bounds under precisely that model. Zero is a clean-input guarantee, not a
claim that any positive tolerance is impossible.
