# Verified label extraction with a global fallback cap

This is the normative LE for the current configuration. It adapts the
RUN, random-shift verification, binary-window prediction and capped
fallback arguments of CS1-C3Q, submission32076cd3-77d5-4058-813d-7e66be4714f8,
proof.md Sections5.1 and5.3–5.6, evaluated source
c80fdd7c40bac9f0f594c66fa0781457ae673e5d. That source credits CS1,
f1481815-9577-4990-abe3-7b79fa5d9284, for these components. Here the cheap
estimate is RUN(F(h_A)); the source's approximate-QFT estimate is not
used. All needed arguments are reproduced below; verdicts are not premises.

Input: the data eigenstate chi_k for a latent label k, with arbitrary
spectators, as in virtual.md Section3. Fix Qcap=20rC_0+K in advance.
Set J_e=n+4, h_e=ceil(log2(Qcap(n+5)))+18,
h_A=2ceil(log2(n+5))+14, F(h)=2^21 h, t_V=64h_e,
T_V=ceil(log2(n+20))+14 and G_LE=n+40+T_V.
Use the rational Cos/Sin table and tab functions of virtual.md Section4.

Translation Tr_c:u->u+c mod N has eigenvalue omega^(-kc) on chi_k.
A test with shift c prepares a |+> ancilla, applies controlled
Tr_((N-c)modN), then measures X (H,Z) or Y (S^dagger,H,Z).
Its mean is cos(2pi ck/N) or sin(2pi ck/N). Conditional on k,
the data and all spectators are exactly unchanged, even after the
outcome; fresh tests/coins are independent. Each test costs O(n)
exact core gates and O(n) scratch. Every ancilla initialization,
measurement, reset/release and gate emission is counted.

The algorithm is: compute k_A=RUN(F(h_A)), verify it as in5.3,
output k_A if accepted; otherwise run RUN(F(h_e)) on the SAME data
register and output that value, subject to the global cap5.5.
The fixed RUN bound gives
4(n+5)e^(-h_A)<=1/(2n) for n>=64. This uniform estimate is (5.E).
After the final test reset/release the data register.

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

### 5.3 Verification

Precomputation. By long division compute rh = floor(k_A 2^G_LE / N), O(n G_LE) = O(n^2)
bit operations, so rh 2^-G_LE is within 2^-G_LE of k_A/N. For i = 0..n+19 let f_i be
the T_V bits of rh in positions G_LE-i-1 down to G_LE-i-T_V (all exist, since
G_LE-i-T_V >= 21). Then f_i 2^-(T_V) is within 2^-(T_V) + 2^(i-G_LE) of frac(2^i k_A/N)
in circular distance on R/Z.

Round v = 1..t_V:
- Draw c uniformly from [0, 2^(n+20)) using n+20 fresh fair bits, each obtained by
  measuring H|0> (O(1) core steps, as in virtual.md Section9), and
  compute cN = c mod N (at most 21 quotient bits: O(n) bit operations).
- Run one X test and one Y test with shift cN, with outcomes zX, zY in {+1,-1}.
  Their means are cos(2 pi c k/N) and sin(2 pi c k/N).
- Predicted phase: xh = (sum over the 1-bits i of c of f_i) mod 2^(T_V), read as
  the fraction xh 2^-(T_V) in [0,1). Since frac(c k_A/N) = sum_i c_i frac(2^i k_A/N)
  mod 1, its circular distance to frac(c k_A/N) is at most
  (n+20) 2^-(T_V) + sum_(i <= n+19) 2^(i-G_LE) <= 2^-14 + 2^-20 < 2^-13. This costs
  O(n T_V) = O(n log n) bit operations.
- Score s_v = zX tab_0(xh 2^-(T_V)) + zY tab_1(xh 2^-(T_V)), with tab from Section 4.

ACCEPT iff s_1 + ... + s_(t_V) >= t_V/2.

Lemma 5.1. Conditioned on k and k_A: if k_A = k, verification rejects with
probability at most e^(-h_e); if k_A != k, it accepts with probability at most
e^(-h_e).

Proof. Rounds are i.i.d. given (k, k_A): each uses fresh coins and fresh tests,
and the data register is unchanged. By (4.1) and 2 pi 2^-13 < 1/1300, each table
value is within 1/625 + 1/1300 < 1/400 of the cosine or sine of 2 pi c k_A/N.
So, given c, E[s_v | c] = cos(2 pi c (k - k_A)/N) + err with |err| <= 2/400 = 1/200.
- If k_A = k, E s_v >= 1 - 1/200.
- If k_A != k, put dl = (k - k_A) mod N, which is nonzero. Write 2^(n+20) = qq N + rr
  with 0 <= rr < N. Over each full period of N consecutive values of c the sum
  of exp(2 pi i c dl/N) is 0, so |E_c exp(2 pi i c dl/N)| <= rr/2^(n+20) < 2^-20.
  Hence E s_v <= 1/200 + 2^-20.
Each |s_v| <= 2 (1 + 2^-20) < 2.01. By Hoeffding, a sum of t_V i.i.d. terms in
an interval of length 4.02 deviates from its mean by at least
Dev = (1/2 - 1/200 - 2^-20) t_V >= 0.494 t_V with probability at most
exp(-2 Dev^2/(4.02^2 t_V)) <= exp(-0.03 t_V) = exp(-1.92 h_e) <= e^(-h_e). QED.

Cost per call: O(n^2) precomputation plus t_V rounds of O(n log n), that is
O(n^2 + n^(3/2) log n) = O(n^2) core steps. Classical scratch O(n log n) bits.

### 5.4 High-confidence extraction and output

If verification accepts, LE outputs k_A. Otherwise it runs k_H = RUN(F(h_e)),
the high-confidence extraction, and outputs k_H, subject to the cap in 5.5.
After the last test of the call, the data register is reset. LE uses only exact translations, H and S throughout, with O(n) quantum
scratch and no QRAM. No Fourier circuit or rotation compiler is used.

### 5.5 Cap on high-confidence runs

Let sn be the least integer >= sqrt n (computed exactly by integer arithmetic) and Cf = ceil(Qcap/sn). A counter
records the number of RUN(F(h_e)) executions. If a call would start the
(Cf+1)-st one, IFC-GLOBAL-SEED stops, releases everything and outputs 0 (ABORT).

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
(sqrt n + 1)/n decreases. Also Cf >= 20, because Qcap>=C_ell>=2^H>=2^D>=20r on the main branch.
So Pr[ABORT] <= 2^-20. QED.

### 5.6 Correctness and cost of LE

Per call, the output differs from k only if (k_A != k and verification accepts)
or (a high-confidence run returns a value other than k). By Lemma 5.1 and the
concentration bound of 5.1 this has probability at most e^(-h_e) + 4(n+5) e^(-h_e) = (4n+21) e^(-h_e),
uniformly in k and in the adaptive schedule. Over at most Qcap calls the
probability that ANY call returns a wrong label is at most
(4n+21) Qcap e^(-h_e) <= 5 * 2^(h_e-18) e^(-h_e) < 2^-15.

Cost. The cheap RUN(F(h_A)) costs O(n^2 log n) core steps per
call. Verification costs O(n^2+n h_e log n)=O(n^2), since h_e=O(r).
Each fallback costs O(n^2 h_e), and at most
Cf<=Qcap/r+1 are executed on EVERY branch. Their total is
O(n^2 Qcap+n^2 r). Thus the aggregate core work is
O(n^2 log n Qcap)+poly(n). Give local quantum circuit emission its
incremental O(log n) per-gate bit allowance specified below; arithmetic/table
construction are already bit-serial. The aggregate structural bound is
O(n^2(log n)^2 Qcap)+poly(n). Every data/slot physical address is
still resolved and charged by proof.md's typed bank implementation.

Ordinary reference scratch includes n+20 binary windows of T_V bits,
RUN's n+5 direction records and the global fallback counter. The physical
implementation stores these in fixed bank arrays of O(n) rows and at
most O(n) bits per row, with constant many O(n)-bit staged words. Long
rh and G_LE-bit values occupy a fixed number of n-bit chunks. Their
arrays fit V and the existing fixed-owner/scratch margins. Test/coin
ancillas are reset and released; source data are reset only after LE
finishes. No extra source copy is acquired for estimation or fallback.

IDEAL run. The ideal run is IFC-GLOBAL-SEED in the latent-label model with every LE output
replaced by the latent k and without the cap of 5.5. The actual and ideal runs
can be coupled to coincide unless some LE call returns a wrong label or ABORT
occurs, so every event's probability differs between them by less than
2^-15 + 2^-20. Resource bounds are proved for every ACTUAL branch directly,
because they rest only on caps and fixed allocations.

The IDEAL OUTER run also omits the fallback counter and every extraction-
private coin, estimate, score, outcome, verdict and loop state from its
conditioning sigma-fields. Replacing LE outputs by latent k gives exactly
the independent uniform labels required by the suppliers. This is a
coupling, not conditioning on numerical success or cutoff survival.
Wrong labels plus fallback abort have total probability below
2^-15+2^-20<2^-14<2^-10, within the retained LE coupling allowance.
All other source, pool, tree and decoder caps and error allowances are
unchanged. The finite exhaustive branch does not invoke this routine.


## Incremental uniform generation of exact translation tests

The tests, RUN estimates, verification verdicts, high-confidence cap and
ideal/actual coupling above are unchanged. Only local gate-index emission
uses the following explicit refinement. A controlled modular addition
of a known classical constant has a fixed finite collection of ripple
passes on n-bit data/carry registers, with operands at bit v or v+/-1.
Compute its constant number of register/block bases once per translation
in O((log n)^2) local-index arithmetic. During each bit pass maintain
constant many operand cursors and advance/restore them by known strides
in O(log n) bit operations per gate. Emit the actual O(log n)-bit local
indices, counting their copies. Each translation has O(n) gates, so its
setup is absorbed by this O(log n) aggregate gate allowance. Reverse
passes subtract strides and reverse the fixed templates; no gate list
is stored. Widths and cursor arithmetic are polynomial in n.

Known constant bits of c and N are ordinary classical values. Reading
one to choose a fixed gate template does not branch on quantum input
bits. Level shifts 2^j mod N are updated by modular doubling once per
level, O(n^2) total; a random verifier shift is reduced as already
specified. All modular addition/compare/swap/inverse circuits still use
exact Clifford+T. No quantum-addressed memory or controlled approximate
rotation is introduced. Full physical slots and address fees are still
handled by the same bank helpers.

Thus cheap RUN costs O(n^2(log n)^2) structural work per call rather
than the previous conservative n^2(log n)^3. Verification's O(n^2)
precomputation and O(n h_e log n) rounds remain within this bound even
with conservative local loop overhead. Fallback work has aggregate
O(n^2 h_e log n)(Qcap/r+1)=O(n^2 log n Qcap)+poly(n).
The complete aggregate is therefore O(n^2(log n)^2 Qcap)+poly(n).
Counter/direction/window storage is exactly the same; only a fixed
number of O(log n)-bit cursor words are added to existing ordinary
staging. The generator changes no probability, gate or source request.
