# LL5-050: five-input prefix composition at low source demand

## 0. Joint theorem and configuration

For every N>=2 and s in Z/NZ, put n=ceil(log2 N). The single LL5-050
algorithm below recovers the full secret with unconditional probability
at least1-2^-8>2/3 from independent ideal copies. On EVERY branch,
including retries, failed attempts, discarded copies and aborts, jointly

 T=O(2^((498/125)sqrt n)), S_C=O(2^((2903/2500)sqrt n)),
 S_Q=O(n), Q=O(2^((1/2)sqrt n)).

All constants are absolute. The four growth indices are[1/2,1/2,0,1/2].
Fractional tolerance is zero under the canonical ideal-copy promise.
The finite exhaustive branch is n<2^32. Otherwise set
r=ceil sqrt n,z=ceil log2r,m=floor(21533r/100000)-10z,
lambda=dl=ceil(11611r/10000)+200z,kappa=ceil log2(m+4)+3.
Section8 gives full five-input widths and four binary remainder levels.
The displayed coefficients are exact rationals with positive proved
slack, not unknown exponential constants or practical timing estimates.

Notation and exact input-derived computations. Given the binary integerN,
setn=ceil(log2N)=bit_length(N-1) and
dn=floor(log2N)=bit_length(N)-1. Herebit_length(x) is the unique
positive integerk with2^(k-1)<=x<2^k forx>=1. Computea2 as the largest integera>=0 such
that2^a dividesN, by repeated exact division by2; setM=N/2^a2. Then
N=2^a2 M withM odd, and2^dn<=N<2^(dn+1). Putomega=exp(2 pi i/N).
All logarithms below are base2 unless explicitly writtenln. A label is
a known nonnegative integer. For analysis only writes1=s modM and
the unique s2 in[0,2^a2) withs=s1+M s2 modN. These unknown analysis
symbols are recovered by the algorithm's two decoders; computing them
from the unknown secret is not an input operation. Every parameter of
the executed circuit is computed fromN and prior recorded outcomes.
The r,z,m,lambda,kappa rules above use exact integer arithmetic and
ceilings, so there is no unspecified real-number rounding rule.

## 1. Provenance and new contribution

Direct framework source: my LL4-050 prototype, proof SHA-256
fac5717bbef7841d66ee93360b830f9d96ef311684999b1e87a1b03d736e980d.
The published mapping is supplied in the final dependency declaration
and public note. It supplies the flat large-leaf framework, full-width
multi-input levels with binary remainder finishing, source-only
primitives, counters, conditional moment proof and resource ledger.
Its credited LL-050F, LL-050R, LL-050C, LL-080C, LL-080, LL-150, CS1,
HPC-127, SPC-138, PSieve, CS1-C3L and Kuperberg sources remain acknowledged.
No prior review, verdict or numerical check is a proof premise.

The direct classical helper source is MW4,
e93f341a-7965-4a93-b5c4-7b0f7a799c37, proof SHA-256
04630827e10b921a8e3888aa5d353670839b1df38eb67d286d0a98708121a5d8,
Section6.3 Part2: its four-list prefix enumerator and exactness argument
are used as a CLASSICAL helper inside a new five-input instrument.
The helper is reproduced in Section6.3 below. Its Schroeppel-Shamir
origin and MW4's preceding framework credits remain acknowledged.

New here is prefix composition: loop classically over each first-table
entry and enumerate a prefix of the remaining four-list fiber, stopping
at a single global Cp. This costs O(nL^3) with polynomial-times-L memory.
The first quantum index is NOT measured by this classical enumeration.
A five-input residue/flag/block instrument uses the resulting tuple list.
The four-input incidence-moment proof extends to five disjoint inputs.
Four binary finishing levels keep every five-input width exact.

The classical leading coefficient drops from4/3 to1.1612, at higher
time coefficient3.984, with source coefficient1/2 and O(n) qubits.
This is a different tradeoff, not dominance of LL4-050 or a sub-half
index claim. Larger-arity public notes were read for context; no
seven-input dissection or step-cap algorithm is used here, and no
priority or independent-origin claim is made.

## 2. Model and counting conventions

A CORE STEP is one of: a NOT/CNOT/Toffoli/H/S/S^dagger gate; a computational-basis
single-qubit measurement or reset; a Boolean operation on at most three classical bits; a
classical bit read or write. Toffoli has an exact constant-size Clifford+T decomposition.
Integers are bit strings; an L-bit addition, comparison or copy costs O(L) core steps.
Generating a gate costs O(1) core steps. Each core step additionally pays its address,
ceil(log2(Mem+2)) bit operations, where Mem <= S_C + S_Q is the number of allocated bits and
qubits. Gates are classically addressed through this charge; there is no
quantum-addressed memory and no QRAM. A source acquisition costs n+1. Hence

    T <= (number of core steps) * (1 + ceil(log2(S_C+S_Q+2))) + (n+1) Q.          (2.1)

## 3. Source identities, the latent-label model and data transforms

Let chi_k = N^(-1/2) sum_u omega^(k u)|u> and phi_k(s) = (|0> + omega^(-k s)|1>)/sqrt 2.
Substituting |u> = N^(-1/2) sum_k omega^(-k u) chi_k into rho_s = (1/N) sum_x |psi_x><psi_x|,
with psi_x = (|0,x> + |1,x+s>)/sqrt 2, gives

    rho_s = (1/N) sum_(k=0)^(N-1) |phi_k(s)><phi_k(s)| (x) |chi_k><chi_k|,          (3.1)

because the cross terms k != k' carry (1/N) sum_x omega^(-(k-k')x) = 0.

Latent-label model. By (3.1) each copy is a convex mixture, with uniform weights, of the
product states phi_k(s) (x) chi_k. The whole algorithm is a linear adaptive quantum instrument
on independent copies. So the joint law of all classical outcomes equals the law obtained by
first drawing, per copy, an independent uniform latent label k and then running on
phi_k(s) (x) chi_k. All probabilities below use this model. Applying X to the control maps
phi_k(s) to, up to a global phase, the POSITIVE qubit pq_k(s) = (|0> + omega^(k s)|1>)/sqrt 2.

Two exact data transforms act on a fresh copy before label extraction. Each is a permutation
of all 2^n data encodings, extended by the identity on encodings >= N, and maps the copy
exactly to rho_s' for a known s'. The latent label of a copy is the Fourier label of its
TRANSFORMED data register.

(T1) Mult_alpha: u -> alpha u mod N, for known alpha coprime to N. Since x -> alpha x is a
bijection of Z/NZ, the copy becomes exactly rho_(alpha s). It uses n controlled modular
additions of the constants alpha 2^v mod N into a clean register, a swap, and the inverse
computation with alpha^(-1): O(n^2) core steps and O(n) scratch.

(T2) Shift_c: if the control is |1>, replace u by u - c mod N, for known c. Since |1,x+s>
becomes |1,x+(s-c)>, the copy becomes exactly rho_(s-c). This takes O(n) core steps.

Modular addition of a known constant in [0,N) is a ripple comparison with N, an addition, a
comparison and a selector. It is the identity on encodings >= N, uses O(n) Boolean gates, and
is computed cleanly: compute, swap or XOR out, uncompute.

## 4. Rational trigonometric table

For v in [0,4096) the controller computes rationals Cos[v], Sin[v] within 2^-20 of
cos(2 pi v/4096) and sin(2 pi v/4096): bound pi within 2^-90 with Machin's formula
pi = 16 atan(1/5) - 4 atan(1/239), summing 40 terms of each alternating series (tails below
2^-91); at the angle 2 v p_mid/4096 < 7, with p_mid the midpoint of the pi bounds, sum 80 Taylor
terms (remainder <= 7^81/81! < 2^-170; angle error < 2^-89; sin and cos are 1-Lipschitz); round
to denominator 2^20. This is a fixed finite computation, an absolute constant, not advice.

For x in [0,1) put tab_0(x) = Cos[floor(4096x)], tab_1(x) = Sin[floor(4096x)], and let
cs_0(x) = cos(2 pi x), cs_1(x) = sin(2 pi x). Since cs is 2pi-Lipschitz,

    |tab_beta(x) - cs_beta(x)| <= 2 pi/4096 + 2^-20 < 1/625.                        (4.1)

## 5. Label extraction LE

Input: a data register holding chi_k for latent k, beside arbitrary spectators. Let Qcap be the
source cap of Section 13. Parameters: J_e = n + 4, h_e = ceil(log2(Qcap (n+5))) + 12,
F = 2^21 h_e.

Translation Tr_c: u -> u + c mod N satisfies Tr_c chi_k = omega^(-k c) chi_k. A TEST AT LEVEL j
prepares an ancilla in |+>, applies Tr_((N - 2^j) mod N) controlled by it, so that the |1> branch
gets eigenvalue omega^(k 2^j), and measures the ancilla in X (H then Z) or Y (S^dagger, H, then Z).
The +-1 outcome has mean cos(2 pi 2^j k/N) or sin(2 pi 2^j k/N). Conditioned on k, chi_k and every
spectator are unchanged and outcomes are independent. Each test costs O(n) core steps.

For each j = 0..J_e take F tests per basis, giving empirical means x_j and y_j.

Decoding a level. Pick the least dr in [0,64) maximizing x_j Cos[64 dr] + y_j Sin[64 dr]. If both
means are within 1/1024 of their expectations, each computed dot product differs from
cos(2 pi (2^j k/N - dr/64)) by at most 2/1024 + 2^-19 < 1/256. The nearest direction has true dot
>= cos(pi/64) >= 511/512. Any direction at circular distance >= 1/16 has dot <= cos(pi/8) <= 31/32.
The gap 15/512 exceeds 2/256, so alpha_j = dr/64 is within circular distance 1/16 of 2^j k/N.

Unwrapping. Set g_(J_e) = alpha_(J_e). For j = J_e - 1 down to 0, let g_j be whichever of g_(j+1)/2
and (g_(j+1)+1)/2 (mod 1) is circularly closer to alpha_j (ties: the first). If g_(j+1) is within
e < 1/16 of 2^(j+1) k/N, the correct preimage is within e/2 of 2^j k/N, hence within
1/16 + e/2 < 3/32 of alpha_j, while the other is more than 13/32 from alpha_j. So the choice is
correct and the error halves. Finally g_0 is within 2^-(n+8) < 1/(2N) of k/N, and LE outputs
floor(N g_0 + 1/2) mod N = k. On any input LE returns a value in [0,N) after its fixed number of
tests, and then resets the data register. It uses no Fourier transform, no lookup, and no rotation
other than H and S.

Concentration. For F independent +-1 variables the centered log-moment generating function has
second derivative at most 1 and vanishes with its first derivative at 0. Hence
Pr(|mean - E mean| > delta) <= 2 exp(-F delta^2/2). With delta = 1/1024 and F = 2^21 h_e this is
2 exp(-h_e). So LE errs with probability at most 4(n+5) e^(-h_e), uniformly in k and in the adaptive
schedule. Over at most Qcap calls, the probability that ANY call returns a wrong label is at most

    4 (n+5) Qcap 2^(-h_e) <= 2^-10.                                                (5.1)

Cost per call: 2(J_e+1)F tests, O(n^2 h_e) core steps. Since log2 Qcap = O(sqrt n) (Section 14),
this is O(n^(5/2)) core steps per call, with O(n) quantum scratch and O(n) classical bits.

IDEAL run. The ideal run is LL5-050 in the latent-label model with every LE output replaced by the
latent k. Actual and ideal runs can be coupled to coincide unless some LE call returns a wrong
label, so every event's probability differs by at most 2^-10. Resource bounds are proved for every
ACTUAL branch directly, because they rest only on caps and fixed allocations.

## 6. Phase vectors, the linear merge and four-input enumeration

A PHASE VECTOR of length 2^lam is a lam-qubit index register with a classical label table
lab[0..2^lam). In the ideal run its state is 2^(-lam/2) sum_x exp(2 pi i lab[x] th) |x>, up to a
global phase, for a fixed real th. Labels are nonnegative integers. The vector is COLLIMATED TO p
if all lab[x] are congruent modulo 2^p. Labels are stored in full, in fixed fields of 3n bits, which
suffices by Section 9 (label bound).

### 6.1 Lookups

LOOKUP(tab), for a classical table of E rows with w-bit entries, XORs tab[x] into a clean w-bit
register, controlled by a lam-qubit index x. For each row x0 it computes the flag [x = x0] with a
Toffoli chain on O(lam) scratch, applies CNOTs from the flag to the output bits where tab[x0] has a
1, and uncomputes the chain. Indices outside [0,E) give output 0. The circuit is its own inverse,
has O(E (lam + w)) gates and O(lam + w) qubits, and is generated by reading each table bit once.

### 6.2 MERGE(X1, X2; p, b, lam'), for b >= 0

Precondition: X1 and X2 are phase vectors from disjoint sets of qubits, both of length 2^lam,
collimated to p, with index registers x, y and tables al, be. Let cA = al[0] mod 2^p,
cB = be[0] mod 2^p, car = floor((cA + cB)/2^p), aa[x] = floor(al[x]/2^p) mod 2^b and
bb[y] = floor(be[y]/2^p) mod 2^b. Then bits p..p+b-1 of al[x] + be[y] equal (aa[x] + bb[y] + car)
mod 2^b. (If b = 0 the residue registers below are empty and e = 0.)

1. LOOKUP aa into a fresh b-bit register Ru and bb into Rv. Add Ru + Rv + car (mod 2^b) cleanly into
   a fresh Rz, and clear Ru and Rv by repeating both lookups. Measure Rz, obtaining e, and reset Rz.
2. Classical. Let S_e = {(x,y) : aa[x] + bb[y] + car = e mod 2^b} and sz = |S_e|. Merge-sort the
   indices y by key (bb[y], y) into order[]; pos[y] is the position of y. For each x the partners y
   form one contiguous run of order[], the class (e - car - aa[x]) mod 2^b; find its start lo[x] and
   length cnt[x] by binary search. Put off[x] = sum_(x' < x) cnt[x'] and
   rank(x,y) = off[x] + pos[y] - lo[x], a bijection from S_e onto [0, sz). If sz < 2^lam', declare FAIL.
3. Let R have 2 lam + 1 bits. LOOKUP pos into Rp and Dx[x] = (off[x] - lo[x]) mod 2^(2lam+1) into Rd.
   Add Rp + Rd (mod 2^(2lam+1)) cleanly into a fresh R, and clear Rp and Rd by repeating the lookups.
   On S_e, R = rank(x,y).
4. Measure bl = floor(R / 2^lam'). If (bl+1) 2^lam' > sz, declare FAIL.
5. Classical. For v in [0, 2^lam'), find the unique (x_v, y_v) with rank bl 2^lam' + v, in one scan
   over x with running offsets. Apply LOOKUP v -> (x_v, y_v) on the low lam' bits of R, XORing into the
   registers x and y, which become |0>. Reset the high bits of R from their known value bl.
6. Output the low lam' bits of R as the index register, with table lab[v] = al[x_v] + be[y_v].

On FAIL, both inputs are reset and released and never reused.

Correctness (ideal run). Before step 1 the state is X1 (x) X2: equal magnitudes over all pairs (x,y),
with phases 2 pi (al[x] + be[y]) th. Steps 1 and 3 compute functions of (x,y) into clean registers and
measure them. So after step 4 the state is the equal-magnitude superposition over the 2^lam' pairs of
block bl, with their original phases. Step 5 maps (x_v, y_v) to v bijectively. The output is a phase
vector with table lab, and every label is congruent to cA + cB + 2^p ((e - car) mod 2^b) modulo
2^(p+b), so it is collimated to p+b.

Lemma 6.1 (distribution-free failure). For ANY input tables collimated to p, the measurement law in
steps 1 and 4 depends only on aa, bb and car (label bits below p+b), and Pr[FAIL] <= 2^(b + lam' - 2 lam).

Proof. Each measurement is a computational-basis measurement of a function of (x,y) on an
equal-magnitude superposition, so its outcome probabilities are ratios of counts, independent of the
phases. Outcome e has probability sz_e / 2^(2lam). Given e, the measured rank is uniform on [0, sz_e).
So FAIL has conditional probability rem_e / sz_e with rem_e = sz_e mod 2^lam' (this also covers
sz_e < 2^lam'). Hence Pr[FAIL] = sum_e rem_e / 2^(2lam) <= 2^b (2^lam' - 1) / 2^(2lam). QED.

Cost. Write L = 2^lam, L' = 2^lam'. With lam, b = O(sqrt n): nine lookup passes of O(L + L') rows with
O(sqrt n)-bit fields; O(L lam) comparisons of O(sqrt n)-bit keys; O(L) binary searches; O(L') additions
of 3n-bit labels. In total O(n (L + L')) core steps. Quantum scratch is O(sqrt n) beyond the index
registers. Classical scratch is O((L + L') n) bits.

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
6. Output the low lam' bits of R as the index register. Store the FULL label
   lab[v]=sum_t lab_t[x_t] of tuple Tl[bl 2^lam'+v], in a fixed3n-bit field.
   Every sum is congruent to c'=(sum_t c_t)+2^p((e-car) mod2^b)
   modulo2^(p+b). This is full-label storage; no compressed STORAGE convention
   or unstated table representation is assumed.

On FAIL all inputs and registers are reset and released, and the inputs are never reused. All registers have fixed
widths.

Correctness (ideal run). Before step 1 the state is the product of the four inputs: equal magnitudes over all L^4 tuples,
with phases 2 pi (sum of labels) th. Steps 1, 3 and 4 compute functions of the tuple into clean registers and measure
them. So after step 4 the state is the equal-magnitude superposition over the 2^lam' tuples of block bl, with their
original phases. Step 5 maps each to its v bijectively. The output is thus a phase vector with table lab, and every label
is congruent to c' modulo 2^(p+b), so it is collimated to p+b. The common residue is understood modulo2^(p+b).

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
fields, one pass of tl <= Cp rows with O(lam) control bits, one pass of 2^lam' rows, and 2^lam' additions of full labels of
O(n) bits. With lam, b = O(sqrt n) (Section 8) and Cp <= 2^(lam + kap + 2) + 1 <= 2 L^2 this is O(n L^2) core steps on every
branch. Quantum scratch is O(sqrt n) beyond the four index registers. Classical scratch, including Tl and Buf, is
O((L + Cp) sqrt n) bits.

Computing c_t and h_t from the full input tables, preparing the b-bit
residue arrays, and writing output full labels cost O(nL+n2^lam')
additional core steps. These fit the displayed O(nL^2) bound. The
fixed3n-bit widths remain valid on branches with extraction errors,
by Section9's acquisition bound and Section5's output-range rule.

### 6.4 MERGE5: classical prefix composition, quantum rank projection

Inputs are five disjoint phase vectors of lengthL=2^lam, collimated to p,
with full labels lab_t[x]=c_t+2^p h_t[x],0<=c_t<2^p. Require
b=5lam-lam'-kap>=1,lam>=kap+2,lam'<=lam+1. Put
mu5=2^(5lam-b)=2^(lam'+kap),Cp=2mu5+1,car=floor(sum_t c_t/2^p)
in{0,1,2,3,4}, and a_t[x]=h_t[x] mod2^b.

1. LOOKUP the five residue arrays, compute their sum pluscar modulo2^b,
   measure it as e, clear the residue scratch. The surviving five-index
   state is the equal-magnitude fiber S_e of size sz>=1, with original phases.
2. CLASSICAL ONLY. Let tau=(e-car) mod2^b. Start an empty tuple listTl.
   For x1=0..L-1, run ENUM4 on arraysa_2..a_5, target
   (tau-a_1[x1]) mod2^b, and limitCp-|Tl|. ENUM4 is exactly the
   pair-stream prefix routine of Section6.3 Part2, with the requested
   limit in place ofCp. Prefix each resulting four-tuple withx1 and
   append it. Stop the entire loop as soon as|Tl|=Cp.
   No quantum index is measured or read by this enumeration.

   ENUM4's DISTINCT-prefix proof holds for arbitrary modulus and
   positive list limit, independently of the four-input instrument's
   relation betweenb andlam'. It uses the four integer lifts of its
   target and paired ascending/descending heaps. It returns exactly
   min(four-fiber-size,limit) distinct tuples. Across differentx1 the
   five-tuples are disjoint. Thereforetl=|Tl|=min(sz,Cp), with the full
   fiber listed whenever it fits. Memory is O((L+Cp)(lam+b)) bits.
   Each ENUM4 run scans at mostO(L^2) heap pairs and appends at most
   its limit;Cp<=2L^2 follows fromlam>=kap+2. Hence the whole loop
   costs O(nL^3), including all heap/key/index work, on EVERY branch.
3. Build rank registerR and a flagRf by scanningTl. For each listed
   five-tuple compute equality with the FIVE quantum index registers,
   toggleRf and XOR the row number intoR, then uncompute scratch.
   Distinctness makes R its unique list rank onTl and Rf=1 there;
   elsewhere both are zero. MeasureRf and declare FAIL if zero.
4. Measurebl=floor(R/2^lam'). If(bl+1)2^lam'>tl declare FAIL.
5. LOOKUP the selected2^lam' tuples to XOR-clear all five original
   index registers; resetRf and the measured high bits ofR. Return
   the lowlam' bits ofR and full labels equal to the five input-label
   sums of the selected tuples. All output labels are congruent
   modulo2^(p+b), since their measured residues all equale.

On FAIL discard/reset every input and register and obtain fresh inputs.
All rank/flag operations are explicit reversible classical circuits and
measurements, using no source oracle or quantum-addressed lookup.
The list-index register has O(lam+kap) bits, equality usesO(lam) scratch,
and the list, heaps and buffers are classical. Withlam,b=O(sqrt n)
andCp=O(2^(lam+kap)), total core cost is O(nL^3) and classical
scratch O((L+Cp)sqrt n). Input full-label preparation and output sums
cost O(nL+n2^lam') and fit. The output phase vector is exact in the
ideal run, because all operations before reindexing are projections
onto computational-basis functions and the reindexing is injective.

Lemma6.3 (five-input failure identity). For arbitrary input tables,
all structural outcome laws depend only on the residue arrays and index
order, and

 Pr[FAIL]=sum_e[(sz_e-tl_e)+(tl_e mod2^lam')]/L^5,
 tl_e=min(sz_e,Cp).

Indeed the measured e has probabilitysz_e/L^5, flag survivaltl_e/sz_e,
and complete-block rejection(tl_e mod2^lam')/tl_e. Multiplying and
summing proves the identity, includingtl_e=0 cases by continuity.
The remainder part is at most2^b2^lam'/L^5=2^-kap. QED.

## 7. Leaf qubits

A LEAF QUBIT is a phase vector of length 2 with table (0, k), for its known label k: a positive qubit whose state in the ideal run is (|0> + exp(2 pi i k th)|1>)/sqrt 2, up to global phase, for a fixed real th. There is no pairing stage in this algorithm; leaf qubits go directly into leaf tables.

## 8. Full five-input widths, remainder schedule and budgets

For n>=2^32 use the Section0 integers and

 Dbar=32K lambda * 5^m,Dcap=2^12 nDbar,Ccap=2^13 nDbar.

Let Y be least with2^Y>=Ccap. Putq=21533/100000,d=11611/10000.
For r>=2^16,z<=log2r+1<=r/1000, by the threshold and derivative
argument in the flat-profile sources. Hence m>=qr-10z-1>=1,
lambda<=dr+1+r/5<=2r,m+4<=r,kappa<=z+3,
andlambda>=3kappa+1. All parameters are literal integer rules.

Capacity. Put c=4lambda-kappa>=4dr+799z-3. Exact arithmetic gives
4qd=250019663/250000000>1. Expanding the positive lower factors,

 m c >=4qd r^2+(799q-40d)rz-(3q+4d)r-7990z^2-769z+3.

Here799q-40d=125.60467>125 and3q+4d=5.29039<6,
exact terminating rationals. Sincez<=r/1000 andr>=65536,
7990z^2+769z<=9rz. Thus m c>=r^2+116rz-6r+3>=r^2>=n.

For any requested1<=B<=n takeu=floor(B/c)<=m complete five-input
levels, each widthc and output log-lengthlambda. Setrem=B-u*c<c.
Append FOUR binary levels with output log-lengthslambda,lambda,lambda,1.
Their width maxima arelambda-kappa three times, then2lambda-kappa-1.
Their sum5lambda-4kappa-1>=c bylambda>=3kappa+1. Allocate rem
greedily from the final level downward. Let a=u+4 be the height,
f_i=5 on the firstu levels and2 on the finishing levels, and p_i
be prefix sums of the resulting widths b_i. Thenp_a=B exactly.
Every five-input width is5lambda_i-lambda_(i+1)-kappa, with
lambda_(i+1)=lambda_i=lambda; no five-input width is ever trimmed.
All binary widths satisfyb_i+lambda_(i+1)-2lambda_i<=-kappa.

A rational logarithm bound for the source and work exponents is

    log2 5 < A=232193/100000.                              (8.1)

Here is a finite rational certificate rather than a decimal assumption.
For w in(0,1), ln((1+w)/(1-w))=2sum_(j>=0)w^(2j+1)/(2j+1),
by integrating the geometric series. Let
U=2sum_(j=0..11)(1/9)^(2j+1)/(2j+1)
  +2(1/9)^25/[25(1-(1/9)^2)],
V=2sum_(j=0..11)(1/3)^(2j+1)/(2j+1).
Positive geometric tail bounding gives ln(5/4)<=U andln2>=V>0.
Exact common-denominator arithmetic gives2+U/V<232193/100000
(the positive gap numerator after reduction is10879232891504867778504163207).
Since log2 5=2+ln(5/4)/ln2, this proves(8.1).

K<=2^15r,lambda<=2r,n<=r^2 yield
log2Ccap<=m log2 5+4log2r+34<=r/2+4log2r+34<=2r-1,
because qA=4999811869/10000000000<1/2. ThusY<=2r<=n,
2^Y<=2Ccap, and all cap/extraction fields are finite and known upfront.

## 9. BATCH(supplier, B)

Input: a supplier of leaf qubits, where in the ideal run the labels are independent and uniform on [0, 2^(B+1)). Output: K roots, or ABORT. A batch has a counter of source acquisitions; if an acquisition would exceed Ccap, the batch ABORTs.

TREE. VEC(0)=LEAF obtains lambda independent supplier qubits,
counting each before request againstDcap, and constructs their subset
label table. VEC(i+1) repeatedly builds f_i fresh VEC(i) outputs on
disjoint source copies, then usesMERGE5(p_i,b_i,lambda_(i+1),kappa)
whenf_i=5, otherwise the binaryMERGE. On FAIL all inputs are discarded
and the next trial obtains fresh children. A root isVEC(a), evaluated
depth first, and a batch requestsK roots.

Root. VEC(a) is a two-entry table with lab[0] = lab[1] mod 2^B, so its ideal state is, up to global phase,

    (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2,   W = (lab[1] - lab[0])/2^B, a known integer.     (9.1)

Label bound. Each leaf qubit enters a table entry at most once, and a batch has at most Ccap leaves. So every label in the batch is a sum of at most Ccap leaf labels below 2^(B+1). Thus every label is below 2^(Y+n+1), which fits in 3n bits by Y <= n, and

    |W| <= 2 Ccap <= 2^(Y+1).                                                       (9.2)

Lemma9.1 (no abort). In the ideal run a batch aborts with
probability at most2^-11/n.

Proof. Lemma10.2 below bounds each five-input trial's failure,
averaged over its untouched current residues, byeta=2^(1-kappa).
Binary failure is at most2^-kappa<=eta. Sinceeta<=1/[4(m+4)]
and heighta<=m+4, Bernoulli's inequality gives(1-eta)^a>=3/4.
These success bounds apply conditional on history BEFORE building
the fresh children of each trial: all their future copies are disjoint.
They are not assertions conditional on full numeric current input tables.
The restricted low-routing conditioning in Lemma10.2 includes child
construction decisions and costs; averaging it proves the stated trial
bound. Failed trials never reuse inputs.

Inductively, if E_i bounds expected delivered leaf-qubit demand of
VEC(i) uniformly over histories before its fresh-copy call, then
E_0=lambda and E_(i+1)<=f_i E_i/(1-eta). Indeed trial j is
started with probability at mosteta^(j-1), and its conditional expected
child demand is at mostf_i E_i. Summing the nonnegative trial costs
proves the recurrence without conditioning on a trial's success.
Thus E_a<=lambda * 5^u*16/(1-eta)^a<=32lambda * 5^m,
and K roots have expected demand at mostDbar.

Each accepted leaf costs at most two acquisitions in conditional
expectation. Summing over successive leaf calls, whose occurrence is
determined before each call, gives expected acquisitions at most2Dbar.
Markov againstDcap andCcap gives2^-12/n each. The real capped
process agrees until one cap fails; a union bound gives2^-11/n.
Both counters include copies from failed/discarded subtrees. QED.

## 10. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and tau_j in {0,1}. Since k_j is uniform on
[0, 2^(B+1)), low_j and tau_j are independent and tau_j is a fair bit. For a batch let G be the sigma-field generated
by: all low_j of its leaves; all merge outcomes (e, Rf, bl); and all decisions of the controller in
that batch (FAIL and retries, aborts, assignment of qubits). G does not include
root measurement outcomes, which no decision in the batch reads. It also excludes LE's internal coins and outcomes,
which in the ideal run feed no decision.

Lemma 10.1. In the ideal run, conditional on G and on all independent randomness outside the batch, the top bits tau_j
are i.i.d. fair.

Proof. Induct over the controller's steps. Every key, residue, sort, rank and block partition reads only label bits
strictly below position B, because all positions used are below B (Section 8). Bits below B of a sum of leaf labels
depend only on the low_j, since multiples of 2^B do not change them.
By Lemmas6.1 and6.3 each merge outcome's conditional law, given
labels and earlier outcomes, is a function of the low_j and earlier outcomes only. So the joint law factorizes as
law(tau) x law(low) x law(outcomes and decisions | low). QED.

Incidence. An entry of a table is the sum over leaves j of x_j k_j, for a 0/1 incidence vector x. Distinct indices of a
table have distinct incidence vectors: this holds for a leaf qubit, table (0, k_j); a LEAF table concatenates disjoint coordinates; and a merge re-indexes injectively pairs or five-tuples on disjoint
coordinates. So the two root entries have x0 != x1, and with hd = |x0 xor x1| >= 1,

    W = cst + sum_(j in Sp) tau_j - sum_(j in Sm) tau_j,                            (10.1)

where cst = (sum_j low_j (x1_j - x0_j))/2^B is a G-measurable integer, and Sp, Sm are disjoint G-measurable sets with
|Sp| + |Sm| = hd. Each leaf enters at most one root, so given G the W's of distinct roots of a batch are independent.
Since E exp(2 pi i phi tau) = e^(i pi phi) cos(pi phi) for a fair bit, for every real phi

    | E[ exp(2 pi i phi W) | G ] | = |cos(pi phi)|^hd <= |cos(pi phi)|,             (10.2)

and, with phi = 1/2, Pr[W odd | G] = 1/2.                                           (10.3)

### 10.1 Conditional overflow bound for a five-input level

Lemma10.2. Every ideal five-input trial fails with probability at most
2^-kappa+2^(-lambda-kappa)<=2^(1-kappa), conditional on its low-routing
history before revealing its current residue fields.

Proof. Let Lv be the surviving leaves of its five disjoint child inputs,
p=p_i,b=b_i. Decompose k_j=l_j+2^p g_j+2^(p+b)t_j, with l_j the low
p bits and g_j the next b bits. Let Fs contain these low parts l_j,
child routing outcomes, discarded-attempt records and costs, independent
outside-copy information and previous root outcomes. EXCLUDE full stored
input labels above p, all current g_j,t_j, and LE's private records.
All earlier routing within the child inputs reads positions below p.
Both merge failure identities show that the laws of measured residues,
projections and rank blocks depend only on such low bits and index order.
Induction therefore leaves the g_j independent uniform modulo2^b given
Fs. The fact that high labels are physically stored does not authorize
conditioning on them. No extraction-error or cap-survival conditioning
is used in this ideal argument.

Given Fs, each tuple has a fixed incidence set I of distinct leaves
and a fixed carry floor(sum_(j in I)l_j/2^p). Different tuples have
different incidence sets, as leaf tables have all distinct bit strings,
children have disjoint coordinates and every merge reindexes injectively.
At most one tuple has an empty set. Fix a residue e and let S count
nonempty tuples whose sum has that residue. Each nonempty sum is uniform,
so E[S|Fs]<=L^5/2^b=mu5=2^(lambda+kappa). For distinct nonempty sets
I,I', choose j in their symmetric difference (swap the sets if needed
so j in I'\I) and an i in I. With all other g fixed, the map from
(g_i,g_j) to the two residues has matrix[[1,0],[1,1]] if i in I',
and identity otherwise. It is invertible over Z/2^b. The indicators
are pairwise independent, hence Var(S|Fs)<=E[S|Fs]<=mu5.

Since sz_e<=S+1 and Cp=2mu5+1, overflow is at most(S-2mu5)_+.
When S>2mu5 one has S-E S>mu5 and
S-2mu5<=S-E S<=(S-E S)^2/mu5. Thus expected overflow is
at mostVar(S)/mu5<=1. Summing over the2^b possible e and dividing
byL^5 bounds the expected discarded mass by2^b/L^5=2^(-lambda-kappa).
Lemma6.3 adds the remainder failure2^-kappa. This proves the bound
on each fresh trial after averaging Fs, without fixing full high labels
or the actually measured e. QED.

## 11. Odd part: s1 = s mod M by free-frequency decoding

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so dn - 1 >= a2. Put theta = s1/M. Every stage uses
B = dn - 1 (B >= 1 on the main branch) and

    K = 2^13 (2r + ceil(log2 n) + 30).                                              (11.0)

The stages are j = 0, ..., J, where J = min{ j >= 0 : 2^(j+3) > 2M }. Then J + 1 <= log2 M.

Supplier for stage j. Compute alpha_j by extended Euclid and CRT so that alpha_j = 1 (mod 2^a2) and
alpha_j = 2^j (2^(dn-1-a2))^(-1) (mod M); it is a unit modulo N. To supply one leaf qubit, repeat until accepted: acquire a fresh
copy, apply Mult_(alpha_j), run LE to obtain k, accept iff k < 2^dn (otherwise discard), and on acceptance apply X to the
control. The batch's acquisition cap applies. In the ideal run accepted labels are i.i.d. uniform on [0, 2^dn), and each copy
is accepted with probability 2^dn/N > 1/2. The qubit has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^(dn-1) W th = W 2^(dn-1-a2) alpha_j s / M = 2^j W s1 / M   (mod 1),           (11.1)

so a root is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known frequency f = 2^j W.

Measurement. Run BATCH for stage j. For each root i = 1..K obtain a fair bit beta_i by measuring H|0>, and measure the
root in X (beta_i = 0) or Y (beta_i = 1), recording Z_i in {+1,-1} with W_i and beta_i. Given W_i and beta_i,
E Z_i = cs_(beta_i)(f_i theta) with f_i = 2^j W_i.

Candidates. Put P_j = j + Y + 8 and identify an integer c with the point zeta = c/2^(P_j) on R/Z. Stage 0 uses every c in
[0, 2^(P_0)). Stage j >= 1 uses every c within circular distance rad_j = 2^-(j+2) of the previous center z_(j-1); both
z_(j-1) and rad_j are multiples of 2^-(P_j), so the arc endpoints are candidates. There are at most 2^(Y+8) candidates.

Score. For each candidate, with exact integer arithmetic,

    score(c) = sum_i Z_i * tab_(beta_i)( ((f_i c) mod 2^(P_j)) / 2^(P_j) ).

Enumerate candidates in increasing order, keeping the K residues (f_i c) mod 2^(P_j), updating each with one addition per
step, and keep a running maximum. Let z_j = c*/2^(P_j) for the least maximizer c*. All loops have fixed lengths.

Lemma 11.1. Suppose theta is within circular distance rad_j of z_(j-1) (no condition when j = 0). In the ideal run,
conditional on BATCH not aborting, with probability at least 1 - 2^-20/n, theta is within circular distance 2^-(j+3) of z_j.

Proof. Condition on the past of the stage and on G. For a candidate point zeta let Delta = theta - zeta as a circular
difference, and xi_i = Z_i cs_(beta_i)(f_i zeta). Given G, the roots use disjoint leaves and independent coins, and their
measurements are on separate qubits, so xi_1, ..., xi_K are independent with values in [-1,1]. Averaging over beta_i,

    E[xi_i | G, W_i] = (1/2)[cos(2 pi f_i theta) cos(2 pi f_i zeta) + sin(2 pi f_i theta) sin(2 pi f_i zeta)] = (1/2) cos(2 pi f_i Delta).

By (4.1) the computed score differs from sum_i xi_i by at most K/625.

Near point. The candidate zeta0 nearest theta has |Delta0| <= 2^-(P_j + 1). By (9.2), |f_i| <= 2^(j+Y+1), so
|f_i Delta0| <= 2^-8 and E[xi_i | G] >= (1/2) cos(pi/128).

Far points. Call zeta far if |Delta| >= 2^-(j+3). In stage 0, |Delta| <= 1/2. In stage j >= 1, theta and zeta lie within rad_j of
z_(j-1), so |Delta| <= 2^-(j+1). So xx = 2^j |Delta| is in [1/8, 1/2]. By Lemma 10.1 and (10.2) with phi = 2^j Delta,

    E[xi_i | G] = (1/2) Re E[exp(2 pi i 2^j Delta W_i) | G] <= (1/2) cos(pi xx) <= (1/2) cos(pi/8).

Concentration. By Hoeffding each fixed candidate's sum deviates from its conditional mean by at least K/64 with probability
at most exp(-K/8192). Outside these events,

    score(zeta0) >= (K/2) cos(pi/128) - K/64 - K/625 > (K/2) cos(pi/8) + K/64 + K/625 >= score(far zeta),

because (1/2)(cos(pi/128) - cos(pi/8)) > 0.0379 > 2/64 + 2/625 = 0.03445. So the maximizer is not far. There are at most 2^(Y+8)
events, one per candidate (the near point is itself a candidate), and exp(-K/8192) <= 2^-(2r + ceil(log2 n) + 30) <= 2^-(Y + ceil(log2 n) + 30), using Y <= 2r. The failure
probability is at most 2^(8-30)/n <= 2^-20/n. QED.

The hypothesis for stage j+1 is the conclusion of stage j, since 2^-(j+3) = rad_(j+1). By induction, with probability at least
1 - 2^-20, theta is within 2^-(J+3) < 1/(2M) of z_J. Output s1 = floor(M z_J + 1/2) mod M.

## 12. 2-adic part: s2 bit by bit

If a2 = 0, put s2 = 0 and skip this section. Otherwise s - s1 = M s2 (mod N) for a unique s2 in [0, 2^a2). Find its bits at levels
g = 0..a2-1. Let s2low be the known low g bits, sh_g = s1 + M s2low (mod N), wd = a2 - g, and rem = (s2 - s2low)/2^g in Z/2^wd, so
s - sh_g = M 2^g rem (mod N).

A leaf qubit for level g: acquire a copy, apply Shift_(sh_g), which makes the secret s - sh_g; run LE to obtain k; apply X to the
control. Ideally the phase is exp(2 pi i k M 2^g rem/N) = exp(2 pi i kk rem/2^wd), with kk = k mod 2^wd. Since 2^wd divides N and k
is uniform on Z/NZ, kk is uniform on [0, 2^wd). Use kk as the label.

- If wd = 1: make up to K leaf qubits, stopping at the first with kk = 1; measure it in X. The outcome is + iff rem is even. If
  none has kk = 1, set the bit to 0.
- If wd >= 2: run BATCH with B = wd - 1, with this supplier. Take the first root with W odd, and measure it in X. By (9.1) it is
  (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2, which gives rem mod 2 exactly. Release the other roots. If no root
  has W odd, set the bit to 0.

By (10.3), and independence of distinct roots given G, each such level misses with probability at most 2^-K, even if s1 was wrong.
Set bit g of s2. In the ideal run with s1 correct and no miss, every bit is correct. Output (s1 + M s2) mod N.

## 13. The complete algorithm and its success probability

Finite branch (n < 2^32). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand at the first minus outcome. Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For cand != s the two data branches are orthogonal, so each outcome is uniform. A union bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10.
All resources on this branch are bounded by an absolute constant.

Main branch (n >= 2^32). Compute a2, M, dn, J, K, the schedule, Y, and all allocations; put

    Qcap = n Ccap + K.

Run Section 11 and then Section 12. Any ABORT stops the algorithm, releases everything and outputs 0. Since J + 1 + a2 <= log2 M + a2 = log2 N <= n, there are at most n batches, each using at most Ccap acquisitions, plus at most K for the single wd = 1 level. So Q <= Qcap on every branch. LE is sized by this Qcap, which is computed before h_e.

Success. In the ideal run the failure events are: a batch ABORT, at most n*2^-11/n=2^-11 (Lemma9.1); a decoder error, at most 2^-20 (Lemma 11.1); and a 2-adic miss, at most n 2^-K <= 2^-40. Adding the LE coupling (5.1):

    Pr[output = s] >= 1 - 2^-11 - 2^-20 - 2^-40 - 2^-10 >= 1 - 2^-8 > 2/3.

The finite branch succeeds with probability at least 1 - 2^-10. These are additive couplings; there is no conditioning on favorable labels or outcomes.

## 14. Every-branch resources and exact envelope coefficients

K,lambda,m=O(sqrt n),heighta<=m+4 andDcap,Ccap=O(n^2 5^m).
The hard counters count every delivered leaf and acquisition, including
failed subtrees and partial work before an abort. Therefore
Q<=Qcap=nCcap+K=O(n^3 5^m), andlog2Qcap=O(sqrt n).

Quantum. A five-input level retains at most four lambda-qubit siblings
plus its current register; there are at mostm levels and four binary
finishing levels. This usesO(m lambda)=O(n) index qubits. MERGE5 has
O(sqrt n) scratch beyond its five inputs; its list is classical.
LE, source data transforms and fresh copies useO(n) more, reset and
reused between calls. ThusS_Q=O(n) on every branch.

Classical. At most SIX full tables per level are simultaneously retained,
including siblings, current input and output, each with at most2^lambda
fields of3n bits. This isO(n^(3/2)2^lambda). Cp=2^(lambda+kappa+1)+1
=O(r2^lambda), since2^kappa<16(m+4)=O(r). Lists, heaps, buffers
and residue keys costO(n2^lambda), and all binary scratch, counters,
LE records, CRT constants and streamed decoder data fit as well.
ThusS_C=O(n^(3/2)2^lambda), with fixed dimensions even on extraction
error branches. The address cost isO(sqrt n).

Time. Each five-input level-(i+1) attempt consumes5^(i+1)lambda
nonreused delivered leaves, so there are at mostDcap/(5^(i+1)lambda)
completed attempts at that level. Partial construction before an abort
is charged to its leaves/acquisitions; at mosta pending frames add
polynomial bookkeeping. Each MERGE5 costsO(n2^(3lambda)), including
its full classical prefix loop, projections and full-label work.
Summing the geometric5^-i bound gives conservative batch tree cost
O(nDcap2^(3lambda)). The four binary finishing levels and leaf table
construction cost less. Across at mostn batches, core tree cost is
O(n^4 5^m2^(3lambda)). All source transforms and LE calls cost
O(n^(5/2)Qcap)=O(n^(11/2)5^m); the decoder costsO(n^(9/2)5^m)
core steps, usingY's bound and candidate streaming as before.
The exponential2^(3lambda) absorbs every fixed polynomial eventually,
so these terms and polynomial preprocessing fit the tree bound with
an absolute outside constant over the capped finite prefix. Circuit
generation, key/heap sorting, initialization, reset, measurement and
all controller actions are included. After theO(sqrt n) address charge
and explicit source costs,

    T=O(n^(9/2)5^m2^(3lambda)).

Letq=21533/100000,d=11611/10000,A=232193/100000. The exact rational
bounds of Section8 give

    qA=4999811869/10000000000<1/2,
    qA+3d=39832811869/10000000000<498/125,
    d=11611/10000<2903/2500.

Since m<=qr andlambda<=dr+200log2r+201,
Q<=poly(n)2^(qA sqrt n),
T<=poly(n)2^((qA+3d)sqrt n),
S_C<=poly(n)2^(d sqrt n).
All polynomial powers are fixed, independent ofN,s and outcomes.
Each displayed rational gap is strictly positive; for any fixedepsilon>0
andk, n^k=O(2^(epsilon sqrt n)) because log2n/sqrt n->0.
Absorbing these factors in the respective gaps proves JOINTLY

 T=O(2^((498/125)sqrt n)), S_C=O(2^((2903/2500)sqrt n)),
 S_Q=O(n), Q=O(2^((1/2)sqrt n)).

The fixed finite exhaustive branch adds only an absolute outside constant.
All four are worst-case branch bounds, not expected running times.

## 15. Exact growth indices

The three exponential envelopes are2^(c sqrt n) for the stated fixed
positive rationalc. Thus log2log2B=(1/2)log2n+log2c, giving index
exactly1/2. The polynomial quantum envelope n has index0. These
are exactly the four structured objects and only time supplies score[1/2].

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does not assert that robustness is impossible.

## 17. Scope and limitations

This is a lower-classical-space tradeoff at source coefficient1/2 with
linear quantum space. Time3.984 is slower than LL4-050's19/6, while
classical space1.1612 is below4/3. No dominance, sub-half time index,
practical runtime, positive robustness, optimality or priority is claimed.
