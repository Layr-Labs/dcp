# CBIFC-18195: streaming pairing under a sample budget, T = O(2^((3639/2000) sqrt n)), Q = O(2^((13/10) sqrt n)), S_Q = O(n)

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single algorithm CBIFC-18195 below receives N in binary and fresh
independent copies of rho_s, and outputs the entire s with unconditional probability at least 1 - 2^-8 > 2/3. On EVERY execution branch
(every failure, discard and abort included) it satisfies jointly

    T = O(2^((3639/2000) sqrt n)),  S_C = O(2^((14/25) sqrt n)),  S_Q = O(n),  Q = O(2^((13/10) sqrt n)).

All constants are absolute. Time, classical space and samples have growth index1/2; the quantum envelope n has index0 (Section15). The fifth claim is the clean-input
tolerance 0 (Section 16). The sharper main-branch bounds, from which these follow, are in Section 14. The envelope coefficients are fixed
exact rationals; no hidden constant sits inside an exponent.

Notation:
- dn = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known nonnegative integer. log means log2 unless stated otherwise.

Main-branch parameters for n>=2^48 are computed exactly:

    r=ceil(sqrt n), H=floor(5595r/10000), dl=ceil(5200r/10000),
    Qtarget=ceil(12994r/10000), A=H-dl,
    L4=ceil((Qtarget-A)/2), Mmax=A+L4, hmax=A+2L4,
    kappa=ceil(log2Mmax)+3.

There is no recycling stream or source bank. Each batch chooses a minimal
prefix of a mixed binary/four-input tree as defined in Section8. Leaf width
dl is nontrivial, and every upper four-input level has input widthH.

## 1. Provenance and exact change

This is a smaller-classical-space extension of my BIFC-14223 development,
4b65045f-40b6-4783-a517-bc944d505dd6 (validation pending). Its
complete exact source extractor, binary/four-input merge construction,
coarse-history proof, full-secret decoder and all-branch accounting are
reproduced. The original MERGE4I source is qzv's IFC1310,
4345e05a-0af9-45b7-a7e3-dc253f584dd8, candidate
99f86a4d36edea87936ff9aa77d5596518e4f333, proof.md Sections6.3 and8.1.
Earlier extractor/cap ancestry includes my QLC-14255,
3ca00587-2350-4943-8f32-ff05b08b024a, qzv's SPQ-1408 and
CW1310/CW1, and CS1/HPC-127/SPC-127/SPC-138/Kuperberg as credited by
those proofs. No earlier verdict is a mathematical premise.

The change caps the auxiliary pair-fiber exponent at2H and chooses a
narrower table width. Late four-input levels then have first windowb0=0.
The exact empty-window circuit behavior and a separate probability case
are supplied below; the positive-window argument is not applied with an
unsupported independence assertion. Section8 gives new clipped-sum,
capacity and full-budget proofs. This trades time for classical memory;
it does not dominate the faster BIFC profile or claim an instrument invention.
No FW/PREP, source bank, QRAM or additional oracle is used.

## 2. Model and counting conventions

A CORE STEP is one of: a NOT/CNOT/Toffoli/H/S/S^dagger gate; a computational-basis
single-qubit measurement or reset; a Boolean operation on at most three classical bits; a
classical bit read or write. Toffoli has an exact constant-size Clifford+T decomposition.
Integers are bit strings; an L-bit addition, comparison or copy costs O(L) core steps.
Generating a gate costs O(1) core steps. Each core step additionally pays its address,
ceil(log2(Mem+2)) bit operations, where Mem <= S_C + S_Q is the number of allocated bits and
qubits. Gates on indexed qubits are classically addressed through this charge; there is no
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
to denominator 2^24. This is a fixed finite computation, an absolute constant, not advice.

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

IDEAL run. Execute this same CBIFC-18195 algorithm but replace each LE
output by its latent labelk. Actual and ideal runs can be coupled until
the first incorrect label, whose probability is at most2^-10 by(5.1).
There are no additional ancilla-preparation trials. Every resource bound
is for actual branches, using fixed caps and allocations.

## 6. Phase vectors and the linear merge

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

### 6.3 MERGE4I(X1, X2, X3, X4; p, b0, b1, lam', aux)

For full label fields, c_t=lab_t[0] mod2^p and h_t[x]=(lab_t[x]-c_t)/2^p; these are classical views, not a compressed storage assumption.

Precondition: X1..X4 are phase vectors from pairwise disjoint sets of copies, of length L = 2^lam, collimated
to p, stored as lab_t[x] = c_t + 2^p h_t[x] (0 <= c_t < 2^p), index registers x1..x4; lam >= kappa + 2,
lam + 1 <= aux <= 2 lam, b0 = 2 lam - aux, lam' >= 1, b1 = 2aux - lam' - kappa >= 1 (kappa >= 1 from Section 0). Put
b = b0 + b1, mX = 2^aux = L^2/2^b0, mu4 = 2^(lam' + kappa), Cp = 8 mu4 + 1; so 2b0 + b1 = 4 lam - lam' - kappa. Residues:
rho_t = h_t mod 2^b0 (window W0: bits p..p+b0-1) and sg_t = floor(h_t/2^b0) mod 2^b1 (window W1: bits p+b0..p+b-1). Carries: cAB = floor((c_1 + c_2)/2^p),
cCD = floor((c_3 + c_4)/2^p), carrylow = floor(((c_1 + c_2) mod 2^p + (c_3 + c_4) mod 2^p)/2^p), and
car = floor((c_1 + c_2 + c_3 + c_4)/2^p) = cAB + cCD + carrylow. For a pair (x1, x2) let
vX = (rho_1 + rho_2 + cAB) mod 2^b0 (bits p..p+b0-1 of lab_1 + lab_2), gX = floor((rho_1 + rho_2 + cAB)/2^b0) in
{0,1}, and the key kX = sg_1 + sg_2 + gX in [0, 2^(b1+1)); define vY, gY, kY for (x3, x4) with cCD.

Window identity. With h_t = rho_t + 2^b0 sg_t + 2^b u_t and S = lab_1 + lab_2 + lab_3 + lab_4 for a tuple,

    floor(S/2^p) = car + h_1 + h_2 + h_3 + h_4 = (vX + vY + carrylow) + 2^b0 (kX + kY) + 2^b (u_1 + u_2 + u_3 + u_4),   (6.4)

as cAB + rho_1 + rho_2 = vX + 2^b0 gX and cCD + rho_3 + rho_4 = vY + 2^b0 gY. So bits p..p+b0-1 of S are
(vX + vY + carrylow) mod 2^b0, and bits p+b0..p+b-1 are (kX + kY + c0) mod 2^b1, c0 = floor((vX + vY + carrylow)/2^b0) in {0,1}.

When b0=0, omit its empty-register lookup/add/measurement gates and set
v=v2=0. Then X_0=Y_0 are the complete pair sets of sizeL²=mX, so step2
cannot cut. Carries and the second window remain as defined; there is no
modulus-zero arithmetic because2^b0=1.

1. LOOKUP rho_1, rho_2 into fresh registers, add them and cAB mod 2^b0 cleanly into a fresh Rz, clear the two by
   repeating the lookups, measure Rz (outcome v), reset it. Same on x3, x4 with cCD (outcome v2). Let the pair fibers
   X_v and Y_v2 be the sets of pairs (x1, x2) with vX = v and (x3, x4) with vY = v2.
2. Cutoff (classical). Merge-sort the x2 by (rho_2, x2) and the x4 by (rho_4, x4). For each x1 the x2 with
   rho_2 = (v - cAB - rho_1[x1]) mod 2^b0 form one contiguous run, found by binary search; the run lengths sum to
   |X_v|, and likewise for |Y_v2|. If |X_v| > 2 mX or |Y_v2| > 2 mX, declare FAIL.
3. LOOKUP h_t mod 2^b (t = 1..4), add them and car mod 2^b cleanly into a fresh Rw, clear the lookups, CNOT bits
   b0..b-1 of Rw into a fresh b1-bit Ru, and uncompute Rw. Ru holds bits p+b0..p+b-1 of S. Measure Ru (outcome v'),
   reset it. Let Z = {tuples of X_v x Y_v2 with bits p+b0..p+b-1 of S equal to v'}, sz = |Z|.
4. Listing (classical). Re-sort the x2 by (rho_2, sg_2, x2) and the x4 by (rho_4, sg_4, x4): the runs are the
   same sets (their ends found again by binary search on rho_2), with sg nondecreasing along each, and gX is constant on the run of x1. STREAM X, a class-restricted Schroeppel-Shamir stream: a min-heap holds, for
   each x1 with a nonempty run, the key kX of x1 with its next unread run position; pop the minimum, output that
   pair, push the next position of that run. As kX is nondecreasing along runs, STREAM X outputs X_v once each in
   nondecreasing kX. STREAM Y outputs Y_v2 in nonincreasing kY likewise (runs read backwards, max-heap). Each heap
   holds at most L entries of O(lam + b1) bits. Neither X_v nor Y_v2 is stored as a table: the stored data are the
   sort orders, runs, heaps, Buf (at most Cp pairs of one run) and Tl.
   Put c0 = floor((v + v2 + carrylow)/2^b0) and tg = ((v' - c0) mod 2^b1) + g 2^b1 (g = 0..3). As
   0 <= kX + kY <= 2^(b1+2) - 2, by (6.4) a tuple of X_v x Y_v2 is in Z iff kX + kY = tg for exactly one g. For
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
   >= p + b0: the only one, in step 2, depends on bits below p + b0.
5-8. (5) R has ceil(log2(Cp + 1)) bits and Rf one qubit, both 0. For each row rho of Tl compute
   [(x1,x2,x3,x4) = Tl[rho]] with a Toffoli chain on O(lam) scratch, CNOT it into Rf and onto the bits of R where
   rho has a 1, and uncompute; rows being distinct, R = rho and Rf = 1 on Tl, R = Rf = 0 elsewhere. Measure Rf; if
   Rf = 0 declare FAIL. (6) Measure bl = floor(R/2^lam');
   if (bl + 1) 2^lam' > tl declare FAIL. (7) For y in [0, 2^lam'), LOOKUP y -> Tl[bl 2^lam' + y] on the low lam'
   bits of R, XORing into x1..x4, which become |0>; reset them, Rf and the high bits of R from known values.
   (8) Output the low lam' bits of R as the index register. For each selected row y of its block,
   compute lab[y] as the sum of the four full input labels at Tl[bl 2^lam'+y]. Store this sum in a
   3n-bit classical field. Only these 2^lam' selected output labels are computed and stored; Tl and Buf
   retain tuple indices only, not full summed labels. The window identity proves collimation to p+b.


On FAIL all inputs and registers are reset and released, and the inputs are never reused. All registers and
arrays have fixed sizes, set by L, b0, b1, lam' and kappa.

Correctness (ideal run). Before step 1 the state is the product of the inputs: equal magnitudes over the L^4
tuples, with phases 2 pi (sum of labels) th. Steps 1, 3, 5 and 6 compute functions of the tuple into clean
registers and measure them; steps 2 and 4 act on nothing in this state. So after step 6 the state is the
equal-magnitude superposition over the 2^lam' tuples of block bl with their original phases, and step 7 maps
each to its y bijectively. The output is a phase vector with table lab, collimated to p+b, since every label is
congruent modulo2^(p+b) by the window identity.

Lemma 6.3 (failure identity). For ANY input tables collimated to p, the laws of the measurements of steps 1, 3,
5 and 6 depend only on label bits below p+b, and with sz = sz(v,v2,v') and tl = min(sz, Cp),

    Pr[FAIL] = sum_((v,v2) cut) |X_v| |Y_v2| / L^4 + sum_((v,v2) not cut) sum_(v') [ (sz - tl) + (tl mod 2^lam') ] / L^4,

where "(v,v2) cut" means that step 2 declares FAIL. The terms (tl mod 2^lam') sum to less than
2^(2b0 + b1 + lam')/L^4 = 2^(-kappa).

Proof. Each measurement is a computational-basis measurement of a function of the tuple on an equal-magnitude
superposition, so its law is a ratio of counts, independent of phases. Step 1's two measurements act on
disjoint registers, so (v, v2) has probability |X_v| |Y_v2|/L^4; given (v, v2) not cut, v' has probability
sz/(|X_v| |Y_v2|); given v', Rf = 0 has probability (sz - tl)/sz; given Rf = 1, R is uniform on [0, tl) and step
6 fails with probability (tl mod 2^lam')/tl. Multiplying and summing gives the identity. There are 2^(2b0 + b1)
triples (v, v2, v'), and tl mod 2^lam' < 2^lam'. QED.

Cost on every branch. Steps 1, 3: 24 lookup passes of L rows with O(lam + b)-bit fields. Steps 2, 4: O(L lam)
comparisons of O(lam + b)-bit keys and O(L) binary searches; after step 2 each of the four scans reads at most
|X_v| + |Y_v2| <= 4 mX pairs, each a heap operation of O(lam) comparisons of O(lam + b1)-bit keys, with at most one
Buf write per Y pair and at most Cp appends of O(lam) bits. Steps 5-8: one pass of tl <= Cp rows with O(lam)
control bits, one lookup pass of 2^lam' rows, 2^lam' additions of O(n)-bit high parts. Total
O((L + mX) lam (lam + b) + Cp lam + 2^lam' (lam + n)) core steps; quantum scratch O(lam + b) beyond the index
registers; classical scratch (sort orders, runs, heaps, Buf, Tl, block table) O((L + Cp)(lam + b)) bits, fixed.

The views h_t=(lab_t-c_t)/2^p, their b-window residues and keys are computed
classically from full label fields. Preprocessing costs O(nL) core steps and
O(nL) bits, included below. Only bounded-width residues are quantum-looked up.
The displayed cost becomes O(n2^aux) for our parameters: aux>=lam+1,
2^kappa=O(sqrt n), Cp=O(sqrt n*2^lam'), lam'=H or1, and aux>=H+1.
Classical scratch including full input/output tables is O(n2^H), since
Cp tuples have O(sqrt n)-bit coordinates and only selected output labels
use full n-bit fields. Quantum scratch remains O(sqrt n). All constants
and addresses are charged in Section14.

## 7. Direct phase-qubit supplier and quantum allocation

NEXT(0) simply requests the next accepted phase qubit from the batch
supplier. There are no other NEXT levels, slots, READY or PENDING queues.
The source and Section5 establish that, conditional on latent labels and
past outcomes, every delivered qubit is the two-entry phase vector(0,k)
in tensor product with all other live registers, on a fresh source-leaf set.
The supplier's acquisition counter includes rejected labels and failed tests.
All source/data scratch is reused. Each supplied control qubit is transferred
into a free location in the current leaf index register by counted SWAPs.

Use a fixed O(n)-qubit array with at most four stacked index registers
per tree level, global O(n) modular/LE scratch, O(n) lookup scratch and
K=O(sqrt n) roots. Reuse wires with a counted classically addressed
free-handle stack or fixed recursive layout. Section14 charges every
register; no exponential coherent bank or QRAM is allocated.

## 8. Boosted mixed tree: prefix, capacity and full four-input budgets

Use the Section0 parameters. All numbers are computed by exact integer
arithmetic. H,dl,A,L4,Mmax,hmax=O(r), and kappa=O(log n).
For i<A define input width lambda_i=dl+i, arity f_i=2 and height h_i=i;
its non-root capacity is dl+i-kappa-1 and root capacity2(dl+i)-kappa-1.
For i=A+j,0<=j<L4, define lambda_i=H,f_i=4,h_i=A+2j,

    aux_i=min(H+1+2j,2H)<=dl+h_i+1, b0_i=2H-aux_i,
    nonrootcap_i=H+aux_i-kappa,
    rootcap_i=2H+aux_i-1-kappa.

A tree with m levels uses the prefix i=0,...,m-1 and output width
lambda_m=1. Its root height is m if m<=A and A+2(m-A) otherwise, so it is at most hmax. Its total capacity Sum(m) is the sum of non-root capacities
below m-1 plus rootcap_(m-1). Put

    Sbin=A(dl-kappa-1)+A(A-1)/2.

For J>=0 let t=min(J,floor(H/2)) and

    AuxSum(J)=sum_(0<=j<J)min(H+1+2j,2H)=2HJ-Ht+t².

Direct sums give

    Sum(m)=m(dl-kappa)+m(m-1)/2+dl-1                    if m<=A,
    Sum(A+J)=Sbin+J(H-kappa)+AuxSum(J)+H-1             if 1<=J<=L4. (8.1)

The binary increment is dl+m-kappa. Adding a four-input level has
increment H+aux_new-kappa, including the transition from binary levels.
All increments are positive. These formulas also cover the first clipped
level and both parities ofH.

### 8.1 Rounded capacity lower bound

Let q=1.2994,d=.52,h=.5595,a=h-d=.0395,e=(q-a)/2=.62995,
all exact rationals. H>=hr-1,dl>=dr,ar-2<=A<=ar,
er<=L4<=er+3,Qtarget<=hmax<=Qtarget+1<=qr+2.
For g(t)=min(hr+2t,2hr), aux_j>=g(j)-2. The increasing2-Lipschitz
g satisfies sum_(j<L4)g(j)>=integral_0^L4g(t)dt-2L4, hence

    AuxSum(L4)>=r² integral_0^e min(h+2u,2h)du-4L4.

As e>h/2, this integral is2he-h²/4. By monotonicity of the other
positive quadratic terms,

    A dl+A²/2+L4H+AuxSum(L4)
      >=C r²-(2h+e)r-4L4+2,
    C=ad+a²/2+eh+integral_0^e min(h+2u,2h)du
      =qd+q²/2-(q+d-h)²/4-(q+d-2h)²/4
      =80034491/80000000 >1+1/100000.

The remaining negative terms are kappa(A+L4)+3A/2-H+1.
Mmax<=r,kappa<=log2r+4,A<=r,L4<=r, so all losses together
are less thanr(2log2r+20). This is belowr²/100000 at2^24 and
thereafter (ln2>2/3). Thus Sum(Mmax)>=r²>=n.
Also A>=r/32, dl>=kappa+1,H>=kappa+2, and every
H+1<=aux_i<=2H. All capacities are nonnegative and both merge
windows are supported, including an empty first window.

### 8.2 Minimal prefix and full four-input levels

For B<=n choose m>=1 minimal with Sum(m)>=B; this exists by8.1.
Allocate B bits greedily from root level m-1 downward using these maxima.
Every four-input level gets its FULL capacity. Since dl>=kappa+1,

    Sbin>=A(A-1)/2>=r²/4096>2r>3H.

Here A>=r/32 and r>=2^24 justify the middle inequality. For a prefix
ending at a four-input levelj, the total of its four-input maxima
exceeds Sum(m-1) by exactly

    H+aux_j-kappa-Sbin <0.

Minimality gives B>Sum(m-1), leaving enough bits to fill all those
levels. If m<=A there are none. Only binary levels may be partial.
Set tp_0=0,tp_(i+1)=tp_i+b_i, so tp_m=B and all residue reads are
strictly belowB.

Binary levels satisfy b_i+lambda_(i+1)-2lambda_i<=-kappa.
For each four-input level put b1_i=b_i-b0_i; full budgets give
b1_i=2aux_i-lambda_(i+1)-kappa. Thus6.3 applies with lam=H,
aux=aux_i,b0=b0_i,b1=b1_i,targetlambda_(i+1), including root1.
Here b0_i>=0,b1_i>=1. If b0_i=0, the empty-window behavior and
probability case in6.3/10.1 apply explicitly.

### 8.3 Demand/source caps and label width

Set Dbar=3Kdl2^hmax,Dcap=2^12nDbar,Ccap=2^13nDbar,
Qcap=nCcap+K,Y=ceil(log2Ccap). These are computed before source access.
Using K<=3*2^13r,dl<=r,n<=r²,hmax<=1.2994r+2,

    log2Ccap<=1.2994r+4log2r+34<=2r-1,

so Y<=2r<=n and2^Y<=2Ccap. Label fields of3n bits suffice as in9.2.
Every count is deterministic on actual branches, including wrong labels.

## 9. BATCH(supplier, B)

Input: a supplier of LEAF QUBITS: positive qubits with phase exp(2 pi i k th) for a fixed real th and a known label k, where in the ideal
run the labels are independent and uniform on [0, 2^(B+1)). Output: K roots, or ABORT. A batch starts with a zeroed counter of
source acquisitions; if an acquisition would exceed Ccap, the batch ABORTs. At its end, unused tree/index scratch is reset and released.

TREE. VEC(0)=LEAF requests dl qubits from NEXT(0), increasing the
delivered counterD and aborting if D would exceedDcap. They form the
tensor-product phase vector with subset-sum table of length2^dl,
collimated to tp_0=0. For i>=1, VEC(i) repeats:
construct f_(i-1) independent VEC(i-1) inputs on disjoint copies; if arity2,
apply MERGE with p=tp_(i-1),b=b_(i-1),targetlambda_i; if arity4,
apply MERGE4I with p=tp_(i-1),b0=b0_(i-1),b1=b_(i-1)-b0_(i-1),
aux=aux_(i-1),targetlambda_i. On FAIL discard all inputs and retry.
Return the successful vector. Evaluate depth-first and run VEC(m) K times.

Root. VEC(m) is a two-entry table with lab[0] = lab[1] mod 2^B, so its ideal state is, up to global phase,

    (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2,   W = (lab[1] - lab[0])/2^B, a known integer.     (9.1)

Label bound. Each leaf qubit enters a table entry at most once, and a batch has at most Ccap leaves. So every label in the batch is a sum of at most Ccap
leaf labels below 2^(B+1). Thus every label is below 2^(Y+n+1), which fits in 3n bits by Y <= n, and

    |W| <= 2 Ccap <= 2^(Y+1).                                                       (9.2)

Lemma 9.1 (no abort). Suppose each supplied acquisition yields a leaf qubit independently with probability at least 1/2, given the past. In the ideal run a
batch ABORTs with probability at most 2^-12/n + 2^-11/n.

Proof. Binary attempts have conditional failure at most2^-kappa.
For each fresh four-input attempt Section10.1 gives failure below
4*2^-kappa, conditional on its coarse input history. Averaging that
bound before construction of its fresh input subtrees gives the same
bound conditional on all past attempts. Since2^kappa>=8Mmax, both are
at most1/(2Mmax).

Induct on tree level for the expected delivered-leaf demand of a call
started on fresh copies, conditional on the past. Before each retry the
new inputs are fresh, so their conditional mean demand is bounded by
the sum of the child bounds. The probability of reaching retryt is at
most(1-1/(2Mmax))^(t-1). Summing expected costs over reached retries
requires no independence between a retry's cost and its own failure.
A root of height at mosthmax therefore has expected demand at most
2^hmax dl*(1-1/(2Mmax))^(-Mmax)<3*2^hmax dl.
Thus E[D_inf]<=Dbar and the demand-cap tail is at most2^-12/n.

At the bounded source-cap stopping point, accepted arrivals feed the
tree directly and are at mostD_inf. Supplier acceptance probability is
at least1/2 given the past, so expected stopped acquisitions are at
most2Dbar. Markov gives a source-cap tail at most2^-12/n, hence at
most the stated conservative2^-11/n. Actual resources are directly
capped; this analysis establishes success, not an expected-only bound.
QED.

## 10. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and tau_j in {0,1}. Since k_j is uniform on
[0, 2^(B+1)), low_j and tau_j are independent and tau_j is a fair bit. For a batch let G be the sigma-field generated
by: all low_j of its leaves; all merge outcomes and the selection/rank/retry/abort/assignment decisions affecting that batch. These decisions read only low bits. Saved full-label fields and any records revealing the unused top bits are excluded. G does not include
root measurement outcomes, which no decision in the batch reads. It also excludes LE's internal coins and outcomes,
which in the ideal run feed no decision.

Lemma 10.1. In the ideal run, conditional on G and on all independent randomness outside the batch, the top bits tau_j
are i.i.d. fair.

Proof. Induct over the controller's steps. Every residue, sort, rank and block partition reads only label bits
strictly below position B, because all positions used are below B (Section 8). Bits belowB of a sum of leaf labels depend only on the low_j, since multiples of2^B do not change them.
By Lemmas6.1 and6.3 each merge outcome's conditional law, given
labels and earlier outcomes, is a function of the low_j and earlier outcomes only. So the joint law factorizes as
law(tau) x law(low) x law(outcomes and decisions | low). QED.

Incidence. An entry of a table is the sum over leaves j of x_j k_j, for a 0/1 incidence vector x. Distinct indices of a
table have distinct incidence vectors: this holds for a leaf qubit, table (0, k_j); a LEAF table concatenates disjoint coordinates; and a merge re-indexes injectively pairs on disjoint
coordinates. So the two root entries have x0 != x1, and with hd = |x0 xor x1| >= 1,

    W = cst + sum_(j in Sp) tau_j - sum_(j in Sm) tau_j,                            (10.1)

where cst = (sum_j low_j (x1_j - x0_j))/2^B is a G-measurable integer, and Sp, Sm are disjoint G-measurable sets with
|Sp| + |Sm| = hd. Each leaf enters at most one root, so given G the W's of distinct roots of a batch are independent.
Since E exp(2 pi i phi tau) = e^(i pi phi) cos(pi phi) for a fair bit, for every real phi

    | E[ exp(2 pi i phi W) | G ] | = |cos(pi phi)|^hd <= |cos(pi phi)|,             (10.2)

and, with phi = 1/2, Pr[W odd | G] = 1/2.                                           (10.3)

### 10.1 Mid-tree factorization and the two-stage fiber moments of MERGE4I

Lemma 10.2. In the ideal run, consider a MERGE4I attempt at a four-input level i, with p = tp_i, lam = H, aux = aux_i, b0 = b0_i,
b1 = b_i - b0_i and lam' = lambda_(i+1) (or 1 at the root). Let Hp be the COARSE sigma-field of the four current input footprints' accepted
leaf labels below p, their completed lower-merge outcomes and selection/rank/retry/abort/assignment
history, the fixed batch/prefix parameters, and history on disjoint copies. It excludes those leaves'
higher label bits, saved full-label fields, raw LE measurements and any other records revealing the
unused higher bits. Thus Hp is not the full physical computer record. All lower-subtree choices use
bits strictly below p; full labels may be stored but are not used to select their input incidence sets.
Source rejection history may be included: for iid uniform labels, a first value accepted in the
fixed interval[0,2^D) is uniform there and independent of the preceding rejected values and their
number. Indeed the probability of each fixed rejected-value sequence followed by an accepted valuea
is the same for everya in that interval. Apply this fact successively; direct modular suppliers
already have uniform power-of-two labels. Consequently source counters and acceptance history do
not expose unused bits of accepted leaves. Raw LE outcomes on those leaves remain excluded.
Then Pr[FAIL | Hp] <= 6 * 2^(-aux) + 2^(-kappa - lam') + 2^(-kappa) < 2^(2 - kappa).

Proof. Let Lv be the set of leaves of the four inputs, a union of four pairwise disjoint sets. For j in Lv write
k_j = lo_j + 2^p g_j + 2^(p+b0) g'_j + 2^(p+b) u_j with 0 <= lo_j < 2^p, 0 <= g_j < 2^b0, 0 <= g'_j < 2^b1. This is
possible as p + b <= B < D, and k_j uniform makes lo_j, g_j, g'_j, u_j independent and uniform.

Factorization. Every earlier selection step of the tree that involves a leaf of Lv is a merge at a lower level, with
p' + b' <= p, or a leaf-acceptance test or a selection decision. Acceptance history is independent of the accepted label values as just proved. By Lemmas 6.1 and 6.3 the lower-merge laws, residues,
sort keys, counts, ranks, lists and block choices read only label bits below p, and bits below p of a sum of
leaf labels depend only on the lo_j. Steps elsewhere use disjoint copies. So, exactly as in the proof of Lemma
10.1 with p in place of B, conditional on Hp the pairs (g_j, g'_j) (j in Lv) are i.i.d. uniform on
[0, 2^b0) x [0, 2^b1). Let Hp' be generated by Hp and the g_j (j in Lv); conditional on Hp' the g'_j are i.i.d.
uniform. The incidence set I(.) of each pair and each tuple is Hp-measurable; distinct pairs, and distinct
tuples, have distinct incidence sets (concatenation and re-indexing, as above), so at most one pair (x1, x2),
one pair (x3, x4) and one tuple have an empty one.

Zero first-window case. If b0=0, g_j is the fixed zero value,
Hp'=Hp, X_0=Y_0 are all pairs and the cut contribution is zero.
The Stage2 argument below applies unchanged to the fresh b1>=1 bits
and these fixed pair families. Its overflow and block bounds give failure
at most2^(-kappa-lam')+2^(-kappa), below2^(2-kappa).
For b0>=1 use both stages below. Thus the stated uniform bound covers
both cases without applying the s>=1 lemma to s=0.

Pairwise independence. Let Sigma be Hp or Hp', s >= 1, and let the elements e of a finite Sigma-measurable family have
pairwise distinct Sigma-measurable incidence sets I(e) and residues R(e) = (f(e) + sum_(j in I(e)) z_j) mod 2^s, with f(e)
Sigma-measurable and the z_j i.i.d. uniform on [0, 2^s) given Sigma. For fixed c let S count the e with I(e) nonempty and
R(e) = c. Each such R(e) is uniform, so E[S | Sigma] is their number over 2^s. For distinct nonempty I(e), I(e')
take j in the symmetric difference, say j in I(e') \ I(e), and i' in I(e); the map (z_(i'), z_j) ->
(R(e), R(e')), other coordinates fixed, has matrix [[1,0],[1,1]] if i' in I(e') and the identity otherwise, both
invertible over Z/2^s. So the indicators are pairwise independent and Var[S | Sigma] <= E[S | Sigma].

Stage 1 (b0>=1). A pair's label sum is the sum of the k_j over its incidence set I, so vX = (f0 + sum_(j in I) g_j) mod 2^b0 with f0 = floor((sum_(j in I) lo_j)/2^p),
Hp-measurable. Fix v; with Sigma = Hp, s = b0, z = g, the count S of pairs with nonempty incidence and vX = v has
E[S | Hp] <= L^2/2^b0 = mX, and |X_v| <= S + 1. If |X_v| > 2 mX then S >= 2 mX, so Dv := S - E[S | Hp] >= mX >= 1
and |X_v| <= Dv + mX + 1 <= 3 Dv <= 3 Dv^2/mX. Hence E[ |X_v| [|X_v| > 2 mX] | Hp ] <= 3 Var[S | Hp]/mX <= 3.
The same holds for Y_v2.

Stage 2. All X_v, Y_v2 are Hp'-measurable. Fix (v, v2) with |X_v|, |Y_v2| <= 2 mX, and fix v'. Likewise, bits
p+b0..p+b-1 of the label sum of a tuple e are (f1 + sum_(j in I(e)) g'_j) mod 2^b1 with
f1 = floor((sum_(j in I(e)) (lo_j + 2^p g_j))/2^(p+b0)), Hp'-measurable. With Sigma = Hp', s = b1, z = g', the count S'
of tuples of X_v x Y_v2 with nonempty incidence and W1 value v' has E[S' | Hp'] <= |X_v| |Y_v2|/2^b1 <=
4 mX^2/2^b1 = 4 mu4 (as 2aux - b1 = lam' + kappa). Since sz <= S' + 1 and Cp = 8 mu4 + 1,
sz - tl = (sz - Cp)_+ <= (S' - 8 mu4)_+. If S' > 8 mu4 then Dz := S' - E[S' | Hp'] > 4 mu4 and
S' - 8 mu4 <= Dz <= Dz^2/(4 mu4). So E[sz - tl | Hp'] <= Var[S' | Hp']/(4 mu4) <= 1.

Summing. Take E[. | Hp] of Lemma 6.3. As sum_(v2) |Y_v2| = sum_v |X_v| = L^2, the cut term is at most
sum_v |X_v| [|X_v| > 2 mX]/L^2 + sum_(v2) |Y_v2| [|Y_v2| > 2 mX]/L^2, of expectation at most
6 * 2^b0/L^2 = 6 * 2^(-aux). The overflow term sums (sz - tl)/L^4 over at most 2^(2b0 + b1) triples with (v, v2) not
cut, an Hp'-measurable condition, so conditioning on Hp' first bounds it by 2^(2b0 + b1)/L^4 = 2^(-kappa - lam').
The block term is below 2^(-kappa) (Lemma 6.3). As aux >= kappa + 3 and lam' >= 1, the total is at most
(3/4 + 1/2 + 1) 2^(-kappa) < 2^(2 - kappa). QED.

The bound conditions on no outcome of the attempt itself. Within the attempt, v' is measured before the
listing of step 4, and no branch or FAIL decision before it reads label bits at positions >= p + b0.

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

Finite branch (n < 2^48). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand at the first minus outcome.
Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For cand != s the two data branches are orthogonal, so each outcome is uniform. A union
bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10. All resources on this branch are bounded by an absolute constant.

Main branch (n >= 2^48). Compute a2, M, dn, J, K, the schedule, Y, and all allocations; put

    Qcap = n Ccap + K.

Run Section 11 and then Section 12. Any ABORT stops the algorithm, releases everything and outputs 0. Since J + 1 + a2 <= log2 M + a2 = log2 N <= n, there are at most n batches,
each using at most Ccap acquisitions, plus at most K for the single wd = 1 level. So Q <= Qcap on every branch. LE is sized by this Qcap, which is computed before h_e.

Success. The failure budgets are batch aborts2^-12+2^-11,
odd decoding2^-20, parity missesn2^-K<=2^-40, and label-extraction
coupling2^-10. Their total is less than2^-8. There is no FW or PREP
subroutine or additional corresponding error. The finite branch has
failure at most2^-10. Thus entire-secret recovery succeeds with probability
at least1-2^-8 for everyN,s. Resources below are direct all-branch bounds,
not conditioned on this success event.

## 14. Resources on every main-branch execution

Throughout K,dl,H,Mmax,hmax=O(sqrt n),Dcap=O(n²2^hmax),
Ccap=O(n²2^hmax). All counters, arrays and attempts are capped.

Q. Q<=Qcap=nCcap+K=O(n³2^hmax), including all rejected and failed copies.

S_Q. At most four index registers per recursion level occupy at most
4(Mmax+1)H qubits, hence O(n). The source/modular/LE and implemented
lookup scratch are O(n), and K roots use O(sqrt n). All wires are reused.
Thus S_Q=O(n) on every actual branch, with no QRAM or coherent bank.

S_C. Input and selected output label tables have O(n2^H) bits per frame.
MERGE4I has Cp=8*2^(lambda_out+kappa)+1=O(sqrt n*2^H) tuples of
O(sqrt n)-bit coordinates. Those tuples do not store full labels.
Its heaps, runs and orders have O(2^H) such rows. All scratch per frame
is O(n2^H). At most O(Mmax) frames gives S_C=O(n^(3/2)2^H), including
parameter, free-handle, LE and decoder data. Every retained frame counts.

Work. A binary attempt at input heighti costs O(n2^(dl+i)). A four-input
attempt at input heighth_i costs O(n2^aux_i)<=O(n2^(dl+h_i+1)), by6.3.
Each attempt consumes disjoint inputs whose canonical footprint contains
2^(h_i+log2f_i)dl delivered leaves. Footprints of distinct attempts at the
same level are disjoint even when child construction had earlier failures.
Thus the number of attempts at that level is at mostDcap divided by that
quantity. Each level therefore costs O(nDcap2^dl/dl); Mmax/dl=O(1), so
tree core work per batch is O(nDcap2^dl).

Acquisitions cost O(n^(5/2)Ccap) core steps per batch. The decoder costs
O(n^(3/2)Ccap) per stage by9.2 and Y<=2r. Across at mostn batches,
and charging O(sqrt n) address bits per core step, total work is

    T=O(n^6 2^hmax+n^(9/2)2^(hmax+dl)+poly(n)2^H).

The last term charges all fixed-array initialization, including capped
scratch even on short-prefix branches. Gate generation, arithmetic,
lookups, resets and source costs are included. This is a worst-case bound.

Since r<=sqrt n+1,

    hmax<=1.2994r+2<=1.2994sqrt n+3.3,
    hmax+dl<=1.8194r+3<=1.8194sqrt n+4.82,
    H<=.5595r<=.5595sqrt n+.56.

Hence jointly on every main-branch execution,

    T=O(n^6 2^(1.8194sqrt n)), S_C=O(n^(3/2)2^(.5595sqrt n)),
    S_Q=O(n), Q=O(n³2^(1.2994sqrt n)).

Both source exponent and initialization exponent are below1.8194.

## 15. Uniform envelopes and exact indices

Margins .0001 forT,.0005 forSC,.0006 forQ absorb their polynomial
factors into the declared pure exponential envelopes, since for fixed
c,k>0,n^k2^(-c sqrt n) is bounded. Quantum space is O(n).
The finite n<2^48 branch contributes uniform absolute constants.
Thus the four exact indices are[1/2,1/2,0,1/2]: exponential envelopes
2^(c sqrt n),c>0 have index1/2, while the envelopen has index0.
The sole numeric time score is[1/2].

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does not assert that robustness is impossible.

## 17. Scope and limitations

This is a source/time/classical-space tradeoff with O(n) accessible qubits,
not a cube-root algorithm or global optimum. Classical memory and samples
remain square-root exponential. The finite cutoff and absolute constants
may be large. Zero fractional tolerance means independent ideal copies;
it is neither a positive robustness claim nor an impossibility theorem.
All statements concern the one specified configuration.
