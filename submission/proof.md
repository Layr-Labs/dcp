# BIF-MGF: streaming pairing under a sample budget, T = O(n^3 log2(n)2^((7111/5000)sqrt n)), Q = O(n^(3/2)log2(n)2^((6497/5000)sqrt n)), S_Q = O(n)

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single algorithm BIF-MGF below receives N in binary and fresh
independent copies of rho_s, and outputs the entire s with unconditional probability at least 1 - 2^-8 > 2/3. On EVERY execution branch
(every failure, discard and abort included) it satisfies jointly

    T = O(n^3 log2(n)2^((7111/5000)sqrt n)),  S_C = O(n^(3/2)2^((2599/2000)sqrt n)),  S_Q = O(n),  Q = O(n^(3/2)log2(n)2^((6497/5000)sqrt n)).

For n=1 logarithmic envelopes use their positive values at n=2.
This finite extension leaves their structured asymptotic forms unchanged.
All constants are absolute. Time, classical space and samples have growth index1/2; the quantum envelope n has index0 (Section15). The fifth claim is the clean-input
tolerance 0 (Section 16). The sharper main-branch bounds, from which these follow, are in Section 14. The envelope coefficients are fixed
exact rationals; no hidden constant sits inside an exponent.

Notation:
- dn = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known nonnegative integer. log means log2 unless stated otherwise.

Main-branch parameters for n>=2^48 are computed exactly:

    r=ceil(sqrt n), H=floor(2599r/2000), dl=ceil(1228r/10000),
    Qtarget=ceil(12994r/10000), A=H-dl,
    L4=ceil((Qtarget-A)/2), Mmax=A+L4, hmax=A+2L4,
    kappa=ceil(log2Mmax)+3, u=ceil(log2n),
    K=Kc=8192(2r+u+30), Kp=8192(u+100).

There is no recycling stream or source bank. Each batch chooses a minimal
prefix of a mixed binary/four-input tree as defined in Section8. Leaf width
dl is nontrivial, and every upper four-input level has input widthH.

## 1. Provenance and exact change

The direct mixed-tree/kernel source is my BIFC-14223,
4b65045f-40b6-4783-a517-bc944d505dd6, candidate
54c016e226cf48f74bbbb84466365cdfb9746dd1. It supplies the exact
minimal-prefix schedule, full four-input windows, implicit pair-fiber
listing and coarse fresh-window factorization. It directly adopts
qzv's IFC1310 MERGE4I and its two-stage moment bound,
4345e05a-0af9-45b7-a7e3-dc253f584dd8, candidate
99f86a4d36edea87936ff9aa77d5596518e4f333, Sections6.3 and8.1.
Full3n-bit labels and the counted kernel operations are retained.

The direct decoder source is my LQF-NEAR,
436c7e25-087d-4f96-a456-a412c0c402b5, candidate
81d61bd25c72f665be4751005ea14266dcbccac3, exact proof.md SHA-256
8ba7650e2003958326350f03f1cb9e07f4ac4c044d3783e866d294462e46a2c4.
It supplies the bounded odd bootstrap, signed near-parity supplier,
small fine/two-adic root budget and cap-aware voting proof.

The exponential-demand method is adapted from my LQF-MGF,
9a77cab2-dc6b-44f3-afd4-e3ba1aad6ffe, candidate
06bdd1395f3348fc61df8a0b7b5078e756a2d30b, exact proof.md SHA-256
0d9133f65cdc6fdd5a85d569e9c5e13b8d9142512c55b1bba0829fbce24cd812.
That source treats binary failure conditional on complete input tables.
Here MERGE4I has only a COARSE-HISTORY failure bound. Section10.2
proves the additional cost-filtration property needed to condition on
child and ghost costs without revealing the unused parent windows.
Section9 then extends the dominating process to arities2 and4.
The binary hypothesis is not assumed for the four-input instrument.

Earlier ancestry includes QLC-14255,SWFC,SPQ-1408,CW1310/CW1,
CS1,HPC-127,SPC-127,SPC-138 and Kuperberg as credited by those
sources. No prior verdict certifies this new coupling, and no kernel,
storage invention, global optimum or literature priority is claimed.

The new algorithm combines the mixed implicit-fiber kernel with small
fine-stage budgets and shorter exponential-tail cutoffs. Every source,
cost-measurability, domination and decoder argument is reproduced.
The new cutoff removes the old Markov multiplier n from work and copies.
No QRAM, coherent bank, arbitrary-angle gate or new oracle appears.

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

IDEAL run. Execute this same BIF-MGF algorithm but replace each LE
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

    aux_i=H+1+2j=dl+h_i+1, b0_i=2H-aux_i,
    nonrootcap_i=2H+1+2j-kappa,
    rootcap_i=3H+2j-kappa.

A tree with m levels uses the prefix i=0,...,m-1 and output width
lambda_m=1. Its root height is m if m<=A and A+2(m-A) otherwise, so it is at most hmax. Its total capacity Sum(m) is the sum of non-root capacities
below m-1 plus rootcap_(m-1). Put

    Sbin=A(dl-kappa-1)+A(A-1)/2.

Direct sums give

    Sum(m)=m(dl-kappa)+m(m-1)/2+dl-1                 if m<=A,
    Sum(A+J)=Sbin+J²+2HJ+H-J*kappa-1                if 1<=J<=L4. (8.1)

These are increasing in m: the binary increment is dl+m-kappa,
the transition increment is2H+1-kappa, and each subsequent four-input
increment is2H+2j+3-kappa. All are positive on the main range.

### 8.1 Rounded capacity lower bound

Let q=1.2994,d=.1228,h=1.2995,a=h-d=1.1767,
e=(q-a)/2=.06135 (exact rationals, not hidden parameters).
We have H>=hr-1,dl>=dr,ar-2<=A<=ar,
er<=L4<=er+3, Qtarget<=hmax<=Qtarget+1<=qr+2.
The positive quadratic part of Sum(Mmax) obeys

    A dl+A²/2+2HL4+L4²
      >=C r²-2(h+e)r+2,
    C=a*d+a²/2+2he+e²
      =q*d+q²/2-(q+d-h)²/4
      =400009071/400000000 >1+1/100000.

This uses monotonicity in A,dl,H,L4 and ar-2>0. The remaining loss is
kappa(A+L4)+3A/2-H+1. Since Mmax<=1.25r,kappa<=log2r+5,A<1.2r,
all losses together are less than r(1.3log2r+12).
At r=2^24 this is below r²/100000, and thereafter the difference is
increasing (ln2>2/3). Thus Sum(Mmax)>=r²>=n.
Also A>=r, dl>=kappa+1, H>=kappa+2 and H+1+2(L4-1)<=2H,
by the displayed constants at r>=2^24 and monotonicity. All capacities
are nonnegative; all MERGE4I window sizes are supported.

### 8.2 Minimal prefix and full four-input levels

For B<=n choose m>=1 minimal with Sum(m)>=B; this exists by8.1.
Allocate B bits greedily from root level m-1 downward using these maxima.
Every four-input level gets its FULL capacity. Indeed
Sbin>=A(A-1)/2>=r(r-1)/2>3r, whereas
2H+2L4+1-kappa<3r. For a prefix ending at four-input j, the sum of all
its four-input maxima exceeds Sum(m-1) by exactly

    2H+2j+1-kappa-Sbin <=0.

Minimality gives B>Sum(m-1), so the greedy process has enough bits to
fill all four-input levels. If m<=A there are no such levels. Only
binary levels may have partial budgets. Define tp_0=0,tp_(i+1)=tp_i+b_i;
then tp_m=B and every accessed residue lies strictly below B.

For binary levels, b_i+lambda_(i+1)-2lambda_i<=-kappa. For a four-input
level, put b1_i=b_i-b0_i. The full-budget property gives exactly
b1_i=2aux_i-lambda_(i+1)-kappa. Thus Section6.3 applies with
lam=H,aux=aux_i,b0=b0_i,b1=b1_i and targetlambda_(i+1), including
root target1. Here H+1<=aux_i<=2H,b0_i>=kappa>=1,b1_i>=1.
In fact b0_i>=H+1-2L4>=1.1768r-6>=r>=kappa on the main range.
No truncated four-input merge is assumed to have the same law.

### 8.3 Demand/source caps and label width

For1<=R<=Kc requested roots compute before access

    D_R=8dl2^hmax(R+u+16), C_R=4D_R.

Use Dcap,Ccap atR=Kc, Cf atR=Kp, and Y=ceil(log2Ccap).
Cf is distinct from the local tuple-list capacity Cp in6.3.
The exact global Qcap is specified in13. Since Kc>=u+16,

    Ccap<=64Kc dl2^hmax<=3*2^19 r²2^hmax,
    log2Ccap<=1.2994r+2log2r+24<=2r-1.

Here Kc<=3*2^13r,dl<=r,hmax<=1.2994r+2 as before.
Thus Y<=2r<=n,2^Y<=2Ccap,Kc/8192=2r+u+30>=Y+u+30.
Also Kp<=Kc and Y+6<=n. Every fine C_R<=Ccap, so the SAME
global Y bounds its frequencies and full-label fields. The shorter
caps are deterministic guards on all branches, including wrong labels.

## 9. BATCH(supplier, B, R)

Input: a supplier of LEAF QUBITS: positive qubits with phase exp(2 pi i k th) for a fixed real th and a known label k, where in the ideal
run the labels are independent and uniform on [0, 2^(B+1)). Output: R roots, or ABORT. A batch starts with a zeroed counter of
source acquisitions and delivered counterD=0; if an acquisition would exceed C_R, the batch ABORTs. At its end, unused tree/index scratch is reset and released.

TREE. VEC(0)=LEAF requests dl qubits. Before EACH NEXT(0), check
D<D_R, otherwise ABORT before the request; increment D after delivery. They form the
tensor-product phase vector with subset-sum table of length2^dl,
collimated to tp_0=0. For i>=1, VEC(i) repeats:
construct f_(i-1) independent VEC(i-1) inputs on disjoint copies; if arity2,
apply MERGE with p=tp_(i-1),b=b_(i-1),targetlambda_i; if arity4,
apply MERGE4I with p=tp_(i-1),b0=b0_(i-1),b1=b_(i-1)-b0_(i-1),
aux=aux_(i-1),targetlambda_i. On FAIL discard all inputs and retry.
Return the successful vector. Evaluate depth-first and run VEC(m) R times.

Root. VEC(m) is a two-entry table with lab[0] = lab[1] mod 2^B, so its ideal state is, up to global phase,

    (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2,   W = (lab[1] - lab[0])/2^B, a known integer.     (9.1)

Label bound. Each leaf qubit enters a table entry at most once, and a batch has at most C_R leaves. So every label in the batch is a sum of at most C_R
leaf labels below 2^(B+1). Thus every label is below 2^(Y+n+1), which fits in 3n bits by Y <= n, and

    |W| <= 2 C_R <= 2 Ccap <= 2^(Y+1).                                                       (9.2)

Lemma9.1(no abort). In the ideal run a batch aborts with probability
at most2^-16/n+2^-12/n. Supplier acceptance is at least1/2 given its past.

Proof. Let p=4*2^-kappa<=1/(2Mmax)<=1/10. Binary attempts fail
with probability at most2^-kappa, even given full inputs. Four-input
attempts fail with probability at mostp conditional on their coarse
fresh-window history (10.1). Lemma10.3 proves that child delivered
costs and the upper coupling costs below can be adjoined to that coarse
history while preserving the unused-window law. This step is essential;
we do not condition the four-input bound on full high label fields.

Domination. After constructing f_i children for an attempt, condition on
the enlarged cost-relevant history of10.3, and let q<=p be its conditional
failure probability. Represent this failure by a fresh uniform U, independent
of that history, as U<=q; conditional on failure/success sample the current
new windows and computational measurement outcomes with their actual
conditional law. Those windows are not yet exposed in this analysis.
Unqueried higher bits remain independently deferred. This finite conditional
sampling representation preserves the actual joint law. It is an analytical
coupling, not a changed quantum algorithm or an oracle for computing q.

The event U<=p dominates actual failure and is independent of all upper
child costs in that attempt. When actual success occurs with U<=p,
continue the upper process with ghost attempts on fresh analytical copies.
Assign independent uniforms to every potential node/attempt. By10.3, all
child/ghost costs use only lower windows, so conditioning on them does not
invalidate the next fresh uniform or parent failure bound. Induction yields

    Z_0=dl,
    Z_i=sum_(j=1)^G sum_(v=1)^f_(i-1) Z_(i-1,j,v),
    Pr(G=g)=(1-p)p^(g-1),g>=1,

with independent upper child copies and independent parent G. The first
parent U>p forces actual success, so actual attempts are no more numerous
than that first index. G uses parent uniforms only; upper child costs are
functions of separate independent lower uniforms. Their independence is
part of this constructed upper process, not a claim about actual costs
and actual failures. The coupling is uniform conditional on the history
before a fresh root. Finite height and geometric G give almost-sure finiteness.

Moments. Let h_0=0,h_i=h_(i-1)+log2(f_(i-1)), and
y_i(s)=ln E exp(sZ_i/(dl2^h_i)). Then y_0(s)=s. With f=f_(i-1),
the independent geometric sum gives

    y_i(s)=F_p(f y_(i-1)(s/f)),
    F_p(a)=a+ln(1-p)-ln(1-p exp(a)).

For0<=s<=1/8, put c_i=(1+2p)^i<=exp(2*p*i)<=e<3, i<=Mmax.
Inductively a=f y_(i-1)(s/f)<=c_(i-1)s<=3/8<1/2. On this
interval exp(a)<5/3 and p<=1/10 give

    F'_p(a)<=1/(1-5p/3)<=1+2p,

the final inequality being p/3-10p²/3>=0. Thus denominators are
positive, every moment exists, and y_i(s)<=c_i s. The argument applies
to f=2 AND f=4 without changing constants. Actual root height is at
mosthmax, so conditional on its past,

    E exp(D_root/(8dl2^hmax))<=exp(3/8).

Tower conditioning over R roots gives
E exp(D_inf/(8dl2^hmax))<=exp(3R/8). Exponential Markov yields

    Pr(D_inf>D_R)<=exp(-5R/8-u-16)<=2^-16/n.          (9.3)

No independence of actual root costs is required.

Acquisitions. Extend potential acceptance indicators after stopping only
for analysis. Their conditional success probability is at least1/2.
For A acceptances over C_R=4D_R potential acquisitions, tower conditioning
gives E[3^-A]<=(2/3)^C_R. Source-cap abort before demand-cap abort
or completion implies A<=D_R. Therefore

    Pr(source-cap abort before demand-cap abort)
      <=3^D_R(2/3)^(4D_R)=(16/27)^D_R
      <=2^(-D_R/2)<=2^-12/n.                        (9.4)

Use(16/27)^2<1/2 and D_R>=2(u+12). Actual and uncapped ideal runs
agree until a guard triggers. These tail bounds establish success only;
all actual branches directly obey the source/delivered caps. QED.

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

Pairwise independence. Let Sigma be Hp or Hp', s >= 1, and let the elements e of a finite Sigma-measurable family have
pairwise distinct Sigma-measurable incidence sets I(e) and residues R(e) = (f(e) + sum_(j in I(e)) z_j) mod 2^s, with f(e)
Sigma-measurable and the z_j i.i.d. uniform on [0, 2^s) given Sigma. For fixed c let S count the e with I(e) nonempty and
R(e) = c. Each such R(e) is uniform, so E[S | Sigma] is their number over 2^s. For distinct nonempty I(e), I(e')
take j in the symmetric difference, say j in I(e') \ I(e), and i' in I(e); the map (z_(i'), z_j) ->
(R(e), R(e')), other coordinates fixed, has matrix [[1,0],[1,1]] if i' in I(e') and the identity otherwise, both
invertible over Z/2^s. So the indicators are pairwise independent and Var[S | Sigma] <= E[S | Sigma].

Stage 1. A pair's label sum is the sum of the k_j over its incidence set I, so vX = (f0 + sum_(j in I) g_j) mod 2^b0 with f0 = floor((sum_(j in I) lo_j)/2^p),
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

### 10.2 Cost-relevant filtration for mixed-tree domination

Lemma10.3. For a parent attempt at precision p=tp_i, the coarse Hp
of10.2 may be enlarged by the delivered costs of all constructed child
calls and their dominating ghost costs, without changing the conditional
independence/uniformity of that attempt's unused W0/W1 windows.
Consequently its failure probability remains at most4*2^-kappa given
this enlarged history. For binary attempts the full-input bound also applies.

Proof. Use the latent-label model3.1 and defer unqueried classical label
bits in the probability analysis. The quantum algorithm still extracts and
stores full labels; those unused values are excluded from this filtration.
Every construction outcome before a vector reaches collimation precision
p is determined by accepted-label bits strictly belowp and independent
measurement-choice randomness: all its residue reads and selection,
listing-cut, block and retry decisions lie belowp. Their computational-basis
measurement laws are counts independent of the unknown phase. Output
full-label additions have fixed field widths, make no overflow/selection
test, and do not choose another copy by their unused high values.
Delivered cost counts requests/decisions, not the content of stored high
fields or the classical bit-operation transcript. The only guards count
acquisitions and delivered qubits, not elapsed work.

Induct simultaneously on subtree level with the coupling in9. At level0
delivered cost is exactlydl and no label bit chooses it. For a child call
ending atprecisionp, all its actual attempts, lower-window outcomes and
delivered costs can therefore be generated from bits belowp. Its coupling
uniforms are generated using those same lower-window conditional laws
and independent auxiliary randomness. Conditional sampling of a failure
or success only constrains the window that this attempt reads; accepted
bits above its end precision remain iid uniform. This follows from10.2's
factorization, or its binary analogue: the failure/outcome law depends
only on the read low windows, so the conditional distribution of higher
bits factors independently.

Upper ghost attempts use fresh analytical copies and lower uniforms;
their cost counters depend on those copies' bits belowp and independent
auxiliary randomness only. Ghost copies are disjoint from the current
actual input footprints. Adding their history and all lower coupling
coins thus adds no observation of current leaves' bits at or abovep.
This closes the simultaneous induction: actual and upper delivered costs
for the child are measurable in an enlargement using only its accepted
low bits, independent auxiliary coins and data on disjoint copies.

Acceptance/rejection counts can also be adjoined. As shown in10.1,
each accepted power-of-two label is uniform and independent of the
preceding rejected labels/count; direct modular suppliers already have
that uniformity. They do not expose accepted unused windows. Raw LE
outcomes, full label fields and root X/Y measurements remain excluded.
Across root calls, earlier roots' data involve disjoint copies and are
allowed as external history. No root measurement controls construction
inside its batch.

At the current parent, input incidence sets and all these child/ghost
costs are functions of the belowp history and permitted independent
enlargements. Conditional on that enlarged Hp, each current leaf's
W0 and W1 coordinates are still iid uniform, independently across leaves.
Indeed they were never used to select these incidence sets or costs,
and the added ghost copies/auxiliary coins reveal no such coordinate.
The two-stage proof of10.2 now applies word for word, first conditioning
on W0, then on W1. The same count/variance bounds give failure<=p_dom
with p_dom=4*2^-kappa. The uniform U at the parent in9 is introduced
AFTER this enlarged history; it is independent of every upper child cost.
The higher bits above the parent's end precision remain deferred, proving
the induction statement for its own parent too. This establishes exactly
the conditional property needed for the mixed-arity upper process.
It never asserts a failure bound conditional on full completed high
input tables. QED.

## 11. Odd part: bootstrap followed by signed near-parity

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so dn - 1 >= a2. Put theta = s1/M. Every coarse stage uses
B = dn - 1 (B >= 1 on the main branch) and

    K = Kc = 2^13 (2r + u + 30), u=ceil(log2n).                                              (11.0)

Put J_full=min{j>=0:2^(j+3)>2M} and J0=min(J_full,Y+5).
Run the following coarse stages j=0,...,J0, each with Kc roots.
There are at most Y+6 stages, and at most log2 M stages.

Supplier for stage j. Compute alpha_j by extended Euclid and CRT so that alpha_j = 1 (mod 2^a2) and
alpha_j = 2^j (2^(dn-1-a2))^(-1) (mod M); it is a unit modulo N. To supply one leaf qubit, repeat until accepted: acquire a fresh
copy, apply Mult_(alpha_j), run LE to obtain k, accept iff k < 2^dn (otherwise discard), and on acceptance apply X to the
control. The batch's acquisition cap applies. In the ideal run accepted labels are i.i.d. uniform on [0, 2^dn), and each copy
is accepted with probability 2^dn/N > 1/2. The qubit has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^(dn-1) W th = W 2^(dn-1-a2) alpha_j s / M = 2^j W s1 / M   (mod 1),           (11.1)

so a root is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known frequency f = 2^j W.

Measurement. Run BATCH(supplier,dn-1,Kc) for stage j. For each root i = 1..K obtain a fair bit beta_i by measuring H|0>, and measure the
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
events, one per candidate (the near point is itself a candidate), and exp(-K/8192) <= 2^-(2r+u+30) <= 2^-(Y+u+30), using8.3. The failure
probability is at most 2^(8-30)/n <= 2^-20/n. QED.

The hypothesis for stage j+1 is the conclusion of stage j. There are at
most n stages, so all coarse conclusions hold except with probability
2^-20 (apart from batch aborts counted separately). If J0=J_full,
round M z_J0 to the nearest integer modulo M, obtaining s1 as before,
and skip the fine stages. The error is strictly below1/(2M).

Otherwise J_full>Y+5. Since j=Y+5 does not satisfy the defining strict
inequality, M>=2^(Y+7). Put the known integer

    chat=floor(M z_J0+1/2) mod M,
    R0=M2^(-Y-8)+1/2.

On correct coarse conclusions the circular error of z_J0 is at most
2^(-Y-8). Therefore a unique signed lift t0 congruent to s1-chat
modulo M satisfies |t0|<=R0. Also R0>=1, R0/M<=2^(-Y-7)<1/2.
Indeed rounding adds at most1/2, and M>=2^(Y+7) bounds that term
by M2^(-Y-8). This is a mathematical bound, not a measurement of t0.
It also proves |t0|<M/2, including rounding and circular wraparound.

Fine stages j=0,...,n-1. Initialize low=0. At stage j let
cj=(chat+low) mod M, K0=(M-1)/2 and gamma=2^(dn-1-a2) mod M.
Compute by extended Euclid and CRT a unit alpha_j modulo N such that

    alpha_j=1 mod2^a2,
    gamma alpha_j=K0 2^(-j) mod M.

These inverses exist: M is odd and gcd(K0,M)=1. Apply Shift_cj
and then Mult_alpha_j to each fresh copy, run LE, accept k<2^dn,
and apply X to the control. The actual batch cap counts every rejected
copy. The ideal accepted labels are independent uniform on[0,2^dn),
with conditional acceptance probability2^dn/N>1/2.
Run BATCH(this supplier,dn-1,Kp), using its smaller local caps.

For analysis on a correct past, t_j=(t0-low)/2^j is an integer.
The exact modular transform gives root phase

    exp(2pi i 2^(dn-1)W alpha_j(s-cj)/N)
       =exp(2pi i K0 W t_j/M)
       =(-1)^(W t_j) exp(-pi i W t_j/M).                (11.2)

The first equality modulo one uses dn-1>=a2 and
s-cj=2^j t_j mod M; the unknown two-adic component cancels.
No gate implements the final small angle: it is the resulting physical
phase of the exact modular supplier and collimation instrument.

Measure every root in X, obtaining Z_i in{+1,-1}. Define V_i=Z_i
if its known W_i is odd, and V_i=0 otherwise. Set b_j=0 if
sum_i V_i>=0 and b_j=1 otherwise; update low+=b_j2^j.
The rule is specified even on an incorrect past or tie.

Lemma11.2. Conditional on a correct past and successful bootstrap,
each fine bit is incorrect with probability at most2^-30/n, apart from
batch aborts and label-extraction error already charged globally.

Proof. Induction gives |t_j|<=R0: after a correct bit
 t_(j+1)=(t_j-(t_j mod2))/2 has absolute value at most(|t_j|+1)/2.
This applies to negative integers too, with residues0,1. Since R0>=1,
the claimed interval is invariant. Every completed root satisfies
|W_i|<=2Ccap<=2^(Y+1), so |W_i t_j/M|<=1/64. Consequently
cos(pi W_i t_j/M)>=3/4, using pi<4 and cos x>=1-x²/2.
Condition on the batch coarse sigma-field G of10, together with the
correct preceding stages. Top bits remain independent across roots,
and Pr(W_i odd|G)=1/2. By equation(11.2), the independent variables
(-1)^t_j V_i in[-1,1] have means at least3/8 each.
Hoeffding thus bounds a wrong sign, including a harmful tie, by

    exp(-9Kp/128)<=exp(-Kp/16)<=2^(-u-30)<=2^-30/n.

The completion/abort decision is G-measurable: every delivery, retry,
source rejection and cap guard depends only on the coarse controller
history included in10. On each completed G, the deterministic frequency
bound applies and top-bit independence remains as stated in10. Thus the
bound holds conditional on every such G, and integration bounds the event
of an incorrect bit together with batch completion. Aborted histories are
charged separately; no independence of root costs and cap success is used. QED.

After n correct fine bits, low=t0 mod2^n. Since |t0|<=R0<M/2
and M<=N<=2^n, recover its unique signed n-bit value by
 t=low if low<2^(n-1), else t=low-2^n.
Output s1=(chat+t) mod M. This completes the odd secret, including
negative residuals, circular boundary cases and unknown two-adic parts.
The total fine-bit failure probability is at most2^-30.

## 12. 2-adic part: s2 bit by bit

If a2 = 0, put s2 = 0 and skip this section. Otherwise s - s1 = M s2 (mod N) for a unique s2 in [0, 2^a2). Find its bits at levels
g = 0..a2-1. Let s2low be the known low g bits, sh_g = s1 + M s2low (mod N), wd = a2 - g, and rem = (s2 - s2low)/2^g in Z/2^wd, so
s - sh_g = M 2^g rem (mod N).

A leaf qubit for level g: acquire a copy, apply Shift_(sh_g), which makes the secret s - sh_g; run LE to obtain k; apply X to the
control. Ideally the phase is exp(2 pi i k M 2^g rem/N) = exp(2 pi i kk rem/2^wd), with kk = k mod 2^wd. Since 2^wd divides N and k
is uniform on Z/NZ, kk is uniform on [0, 2^wd). Use kk as the label.

- If wd = 1: make up to Kp leaf qubits, stopping at the first with kk = 1; measure it in X. The outcome is + iff rem is even. If
  none has kk = 1, set the bit to 0.
- If wd >= 2: run BATCH(this supplier,wd-1,Kp). Take the first root with W odd, and measure it in X. By (9.1) it is
  (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2, which gives rem mod 2 exactly. Release the other roots. If no root
  has W odd, set the bit to 0.

By (10.3), and independence of distinct roots given G, each such level misses with probability at most 2^-Kp, even if s1 was wrong.
Set bit g of s2. In the ideal run with s1 correct and no miss, every bit is correct. Output (s1 + M s2) mod N.

## 13. The complete algorithm and its success probability

Finite branch (n < 2^48). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand at the first minus outcome.
Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For cand != s the two data branches are orthogonal, so each outcome is uniform. A union
bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10. All resources on this branch are bounded by an absolute constant.

Main branch (n >= 2^48). Compute a2,M,dn,r,all mixed-tree dimensions,
Kc,Kp,Ccap,Cf,Y before source access. Put

    Qcap=(Y+6)Ccap+2nCf+Kp.

Size LE with this Qcap. Run11 then12. Any ABORT stops, releases
everything and outputs0. There are at mostY+6 coarse batches,
n odd fine batches and n two-adic batches, plus at mostKp copies
for the direct wd=1 step. Thus Q<=Qcap on EVERY branch.
There are at most3n batches sinceY+6<=n. Each batch with R roots
uses its ownD_R,C_R from8.3.

Success. By9.1 each ideal batch aborts with probability at most
(2^-16+2^-12)/n. Over3n batches this is3(2^-16+2^-12).
Add coarse decoding2^-20, fine votes2^-30, two-adic misses2^-40
and label-extraction coupling2^-10. The sum is less than2^-8.
Uniform estimates conditional on correct preceding stages and a first-error
union bound prove unconditional whole-secret recovery. The finite branch
has error at most2^-10 and at mostN(n+10) acquisitions. Exact main caps
are not asserted on that finite branch.

## 14. Resources on every main-branch execution

All arrays, counters and retries are capped. Kc,dl,H,Mmax,hmax=O(sqrt n),
Kp=O(log n). Coarse caps obey Dcap,Ccap=O(n2^hmax).
Fine caps obey D_Kp,Cf=O(sqrt(n)log(n)2^hmax).
As Y+6=O(sqrt n), summing ALL batches' caps gives

    Q<=Qcap=O(n^(3/2)log(n)2^hmax).                  (14.0)

The sum of delivered-demand caps has the same envelope. Every rejected
copy, failed input and abort is counted; no success conditioning appears.

S_Q. At most four index registers per recursion level occupy at most
4(Mmax+1)H qubits, hence O(n). The source/modular/LE and implemented
lookup scratch are O(n), and Kc roots use O(sqrt n). All wires are reused.
Thus S_Q=O(n) on every actual branch, with no QRAM or coherent bank.

S_C. Input and selected output label tables have O(n2^H) bits per frame.
MERGE4I has Cp=8*2^(lambda_out+kappa)+1=O(sqrt n*2^H) tuples of
O(sqrt n)-bit coordinates. Those tuples do not store full labels.
Its heaps, runs and orders have O(2^H) such rows. All scratch per frame
is O(n2^H). At most O(Mmax) frames gives S_C=O(n^(3/2)2^H), including
parameter, free-handle, LE and decoder data. Every retained frame counts.

Work. Binary attempts at heighti cost O(n2^(dl+i)); four-input
attempts at heighth_i cost O(n2^aux_i)=O(n2^(dl+h_i+1)).
An attempt consumes a canonical footprint of2^(h_i+log2 f_i)dl
delivered leaves. Distinct attempts at the same level have disjoint
footprints, even when child subtrees had earlier failures. Therefore
each level costs O(nD_R2^dl/dl) per batch. SinceMmax/dl=O(1),
tree core work is O(nD_R2^dl). Summing every D_R using14.0 gives
O(n^(5/2)log(n)2^(hmax+dl)) core steps. Every core step additionally
pays O(sqrt n) address bits. Thus total tree work is

    O(n^3 log(n)2^(hmax+dl)).

Extraction and source transforms cost O(n^(5/2)) core steps per copy,
since logQcap=O(sqrt n). Using14.0 gives charged acquisition work
O(n^(9/2)log(n)2^hmax). Coarse scoring costs O(Kc n2^Y) per
stage; at mostY+6=O(sqrt n) stages give O(n³2^hmax) core steps,
or O(n^(7/2)2^hmax) with addresses. Fine votes, signed updates,
CRT constants and direct parity selection add only polynomial work
per stage/root. Source charges(n+1)Q and gate generation are included.

All fixed-array initialization, including full-label frames and capped
tuple scratch on short-prefix branches, is bounded bypoly(n)2^H.
The exponents hmax and H are strictly below hmax+dl by fixed positive
multiples ofsqrt n on the main range. Their polynomial terms are therefore
absorbed into the tree envelope. Lookups, arithmetic, listing, resets,
discarded acquisitions and actual wrong-label branches are charged.
Consequently

    T=O(n^3 log(n)2^(hmax+dl)).                      (14.1)

By r<=sqrt n+1 and the exact rounded schedule,

    hmax<=1.2994sqrt n+3.3,
    hmax+dl<=1.4222sqrt n+4.423,
    H<=1.2995sqrt n+1.3.

The uniform envelopes, with only absolute outer constants, follow in15.

## 15. Uniform envelopes and exact indices

Substitute the rounded inequalities from14. Jointly on every branch,

    T=O(n^3 log2(n)2^((7111/5000)sqrt n)),
    S_C=O(n^(3/2)2^((2599/2000)sqrt n)), S_Q=O(n),
    Q=O(n^(3/2)log2(n)2^((6497/5000)sqrt n)).

These declare the full polynomial factors rather than absorbing them into
larger pure exponential coefficients. The finite exhaustive branch contributes
absolute constants. At n=1 logarithmic envelopes use their positive values
at n=2; exact main caps apply only when n>=2^48. All N,s are covered.
The four exact indices are[1/2,1/2,0,1/2]; positive fixedsqrt(n)
exponents have index1/2 and the linear quantum envelope has index0.
The sole numeric time score is[1/2]. This improves the parent's joint
structured envelopes without asserting a new growth class.

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
