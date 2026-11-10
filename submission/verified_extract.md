# Verified label extraction with a global fallback cap

This is the normative LE for the current configuration. It adapts the
RUN, random-shift verification, binary-window prediction and capped
fallback arguments of CS1-C3Q, submission32076cd3-77d5-4058-813d-7e66be4714f8,
proof.md Sections5.1–5.6, evaluated source
c80fdd7c40bac9f0f594c66fa0781457ae673e5d. That source credits CS1,
f1481815-9577-4990-abe3-7b79fa5d9284, for these components. The cheap estimator now uses the guarded approximate-QFT variant of
approx_estimate.md; RUN(F(h_A)) remains its deterministic compilation-
resource fallback. All needed arguments are reproduced; verdicts are
not premises.

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

Before sources, initialize guarded compilation mode and bounded ordinary
template/workspace buffers as in approx_estimate.md. For each copy,
compute k_A with that guarded CHEAP estimator, then verify it as in5.3,
output k_A if accepted; otherwise run RUN(F(h_e)) on the SAME data
register and output that value, subject to the global cap5.5.
The fixed RUN bound gives4(n+5)e^(-h_A)<=1/(2n) in MODE_RUN;
approx_estimate.md proves the stronger1/(512n) bound in MODE_QPE.
Thus the same uniform1/(2n) estimate (5.E) holds in either mode.
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
After the last test of the call, the data register is reset. The verifier and high-confidence RUN use exact translations,H,S.
Only the guarded cheap estimate can use compiled approximate rotations,
on fresh estimate ancillas; its data translations remain exact and
spectators unchanged. All gates are actual counted Clifford+T words,
with O(n) quantum scratch and no QRAM.

### 5.5 Cap on high-confidence runs

Set Cf=ceil(4Qcap/n). Before starting a (Cf+1)-st high-confidence
RUN, stop with normal cleanup and output0. This is an executed cap.

Lemma5.2. Its abort probability is <=2^-80 on the main branch.
Given the entire past and latent label, reaching RUN has probability
<=1/(2n)+exp(-h_e)<=1/n. Fresh tests/coins give stochastic domination
by Bin(Qcap,1/n), without assuming adaptive groups independent.
Writing mu=Qcap/n and x=Cf>=4mu, the exponential-moment bound is
 Pr[X>=x]<=(exp(1)mu/x)^x<=(exp(1)/4)^(4mu)<=2^-mu.
Here H>=2log2 n on the main branch, and Qcap>=20r2^H imply mu>=80.
The bound follows; abort requires at least Cf such indicators. All
ceilings only increase the threshold. The finite exhaustive branch is
unchanged. The new event is coupled separately; its bound is smaller
than the previous2^-20 allocation, so the full success budget is retained.

### 5.6 Correctness and cost of LE

Per call, the output differs from k only if (k_A != k and verification accepts)
or (a high-confidence run returns a value other than k). By Lemma 5.1 and the
concentration bound of 5.1 this has probability at most e^(-h_e) + 4(n+5) e^(-h_e) = (4n+21) e^(-h_e),
uniformly in k and in the adaptive schedule. Over at most Qcap calls the
probability that ANY call returns a wrong label is at most
(4n+21) Qcap e^(-h_e) <= 5 * 2^(h_e-18) e^(-h_e) < 2^-15.

Cost. native_ops.md implements the cheap estimate/verifier with charged
O(n^2) per source eventually (Section5.7 and native_ops.md), and high-confidence RUN with
O(n^(5/2)h_e) per execution. Cf=ceil(4Qcap/n), h_e=O(r), hence aggregate
RUN work is O(n^2 Qcap)+poly(n). All wrong-label branches, guards and
cleanup are counted. Finitely many deterministic guarded exceptions
retain the complete old implementation and affect only absolute constants.
The exact source/estimator channels, fresh tests, verifier probabilities,
wrong-label union bound and decoder conditioning remain unchanged.

The ideal extraction coupling replaces every output by latent k and omits
the fallback counter and ALL extraction-private coins, estimates, scores,
verdicts and loop records from outer conditioning. Wrong labels have
union probability below2^-15 by the displayed bound, while the new
fallback abort is <=2^-80. Hence actual/ideal event laws differ by at
most2^-15+2^-80<2^-10. This is a coupling, not conditioning on correct
estimates or successful cutoff survival. Exact source transforms yield
the same independent uniform latent labels in the ideal run. The other
source/pool/tree/decoder/key budgets are unchanged; finite exhaustive
inputs do not call LE.

RUN uses fixed forward/reverse ripple gate templates with positions
v or v+/-1 and finite cursor-role opcodes. Initialize constant-many local
cursors in O(log^2 n) reference bit operations per pass. Carry/borrow
updates and restoration cost O(n+log^2 n) per length-n pass. Constant
bits are explicit reads; modular doubling costs O(n) per level. Thus
RUN's O(n^2 h_e) structural work includes uniform gate generation,
resets and all tests, not copied literal indices or free cursor updates.
The complete physical native/address driver is counted separately in
native_ops.md and typed_dispatch.md. No growing gate transcript is stored.

## 5.7 Exact private block cache

This computes the IDENTICAL xh=sum_i c_i f_i mod2^T_V, with unchanged
rh/windows, random bits, tests, scores and thresholds, including wrong
k_A values. Put B=floor(log2 n/2), G=ceil((n+20)/B); explicitly pad the
last c group and missing f values with zeros. For every g and v<2^B,
 V[g,v]=sum_(j<B) v_j f_(gB+j) mod2^T_V.
It follows by grouping the original sum that reading V[g,c_group]
and adding over groups gives exactly the old prediction, not a new
approximation or confidence argument.

Store V in PRODUCT BASIS qubits at fixed native positions, with
power2 stride S_T>=T_V+2. B>=20, 2^B<=r and bounded T_V/B imply
G2^B S_T=O(nr). Round this span to a power2; take an aligned power2
base at least the span and the original2^16 n data/translation region.
The resulting O(nr) used cache is disjoint from data/test scratch.
The n-only source-layout guard checks its whole span inside P before
sources; otherwise keep the explicit old window-regeneration path.
O(nr)=o(P), so exceptional lengths are finite, with no new abort or
source event. T1/QPE scratch is cleaned before cache construction.
Tests and fallback RUN never clear the live cache region.

Build one group at a time, staging only B*T_V=O(log^2 n) window bits
and a T_V-bit running sum. Enumerate v=t XOR(t>>1); the changed bit is
j=ctz(t). Update the sum by plus/minus f_(gB+j) according to its new
bit and write EVERY T_V bit at record(g,v). Mask0 starts with sum0.
Each f_i window is read ONCE: even its old driver costs at most
O(n^(3/2)(log n)^2)=O(n^2). No n*T_V ordinary array is stored.

Every cache bit is initialized and reset on each LE return/abort,
including a partial build. Sweep its ENTIRE used/padded region once,
not P per entry. A single native low-width cursor has carry/borrow
work O(L+B_native^2)=O(L) across L=O(nr) positions, as in the whole
flag-array stream of perm_fw.md Section7. Every reset consumes its
full d-bit address. This costs O(nr*d)=O(n^2).

For each Gray entry, computing its mask, ctz/direction and ALL low
O(log n) physical argument bits costs O(log n), absorbed by T_V.
Power2 strides concatenate coordinates. The aligned word driver
executes all ordinary group-word reads, modular additions and native
payload writes in O(T_V) raw bit/control work, including cursor
initialization/restoration. Group-word indices are CLASSICALLY known.
Every changed argument bit pays d, and every access consumes ALL d
bits; high zeros stay initialized throughout the private LE scope.
Thus construction costs O(G2^B T_V)=O(nr) raw work and O(n^2) charged.

In each round read ALL B random c bits per group, form its actual
classical index, measure/read ALL T_V basis payload bits without
changing them, and add the full T_V-bit word modulo2^T_V. This is
known-address native bit access, not QRAM or a row-read oracle.
G*(B+T_V+log n)=O(n) raw work gives O(n^(3/2)) charged per round;
64h_e=O(r) rounds give O(n^2). Coins, c mod N (at most21 quotient
positions), exact translation tests, scores and counters fit O(n^2)
under the retained complete native ripple routines.

The cache depends only on already measured private records and is
cleared before leaving LE; its exact prediction/decision channel is
the old one on arbitrary inputs/spectators. Outer conditioning still
excludes extraction-private state. Its whole quantum capacity already
lies in the counted P prefix. Only the O(log^2 n) current group is
ordinary; both2^16 n arithmetic/LE blocks, compiler buffers and all
staging remain below2^20 n. All cutoffs and coupling budgets are unchanged.
