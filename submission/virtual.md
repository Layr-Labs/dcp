# Reference algorithm P for OTP-FLQ110-Y2: the complete FLQ110 proof

Everything after the marker line and the blank line following it is the complete specification and proof of
FLQ110, the base algorithm P of OTP-FLQ110-Y2. The text is our FLQ110 proof with one sentence added
to the proof of Lemma 10.1 (the supplier's acceptance decisions), noted in its Section 1.

In this file "the algorithm" is P, run on ideal copies. Its resource statements (Sections 0, 14 and 15), its success
statement (Section 13) and its tolerance statement (Section 16, tolerance 0 on ideal copies) concern P alone; they
are not claims of OTP-FLQ110-Y2. The four resource bounds and the tolerance 1 - 1/(10^128-184)^2 of OTP-FLQ110-Y2 are proved in proof.md.

proof.md uses from this file:
- the algorithm and its correctness in its IDEAL run (Sections 3-13): the latent-label model (3.1), LE (Section 5),
  the supplier of Section 11, the leaf qubits of Section 12 and the success sum of Section 13;
- the counting rule (2.1), the schedule facts (8.2) and (8.3), and the allocation and cost bounds of Section 14 with
  exponents 54999/50000 and 62899/50000.

Historical first-person text below denotes the authors of FLQ110 and of the works it credits. No earlier verdict
on any submission is a premise.

--- BEGIN COMPLETE VIRTUAL SOURCE ---

# FLQ110: F-LIMIT with fewer recycling levels, S_Q = Q = O(2^((11/10) sqrt n)) and T = S_C = O(2^((629/500) sqrt n))

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N), and let aT = 629/500 and aP = 11/10.
The single algorithm FLQ110 below receives N in binary and fresh independent copies of
rho_s, and outputs the entire s with unconditional probability at least 1 - 2^-7 > 2/3.
On EVERY execution branch (every failure, discard and abort included) it satisfies jointly

    T = O(2^(aT sqrt n)),  S_C = O(2^(aT sqrt n)),  S_Q = O(2^(aP sqrt n)),  Q = O(2^(aP sqrt n)).

All constants are absolute. Each of the four envelopes has growth index exactly 1/2
(Section 15). The fifth claim is the clean-input tolerance 0 (Section 16). The sharper
main-branch bounds, from which these follow, are in Section 14: T = O(n^6 2^(eT sqrt n)),
S_C = O(n^3 2^(eT sqrt n)), S_Q = O(n^2 2^(eP sqrt n)) and Q = O(n^3 2^(eP sqrt n)) with
eT = 62899/50000 = 1.25798 < aT and eP = 54999/50000 = 1.09998 < aP. The envelope coefficients are
fixed exact rationals; no hidden constant sits inside an exponent.

Notation:
- dn = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with
  s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known nonnegative integer. log means log2 unless stated otherwise.

Main-branch parameters, computed by exact integer arithmetic for n >= 2^40:

    r = ceil(sqrt n),   ell = ceil(23547 r/50000),   m = ceil(62899 r/100000),   dl = ceil(62899 r/100000),
    kappa = ceil(log2 m) + 1.

So there are ell FW LEVELS, a collimation tree of depth m, and leaf tables built from
dl qubits. Since r >= 2^20 these satisfy ell >= 2, dl >= kappa + 1, 2^kappa >= 2m.

## 1. Provenance and what is new

FLQ110 is the algorithm F-LIMIT run with a different parameter choice, and nothing else. F-LIMIT is the
reference algorithm P of our submission F-LIMIT-BANK (a9a7dcac-3918-44e8-84db-bda6b1dcebdd on this
challenge), whose file virtual.md contains F-LIMIT's complete proof; F-LIMIT is not filed on its own. This
file is that proof with the following changes, and is complete by itself; no verdict on F-LIMIT-BANK is a
premise.
- F-LIMIT uses ell = ceil(2309r/4000) FW levels, a tree of depth m = ceil(57747r/100000) and leaf tables from
  dl = ceil(57731r/100000) qubits, which balances the pool exponent (governing S_Q and Q) and the tree
  exponent (governing T and S_C) at 57739/50000. FLQ110 uses fewer FW levels and a deeper tree with larger
  leaf tables, ell = ceil(23547r/50000) and m = dl = ceil(62899r/100000), so the pool exponent falls to
  eP = 54999/50000 = 1.09998 and the tree exponent rises to eT = 62899/50000 = 1.25798.
- Sections 2-7, 9-13 and 16 are F-LIMIT's text unchanged, except that the algorithm name in Section 5 is
  FLQ110 and that the proof of Lemma 10.1 has one added sentence (the supplier's acceptance
  decisions read only whether k < 2^(B+1)). In particular the instrument FW (w = 2^28), PREP, FWLEVEL and Lemmas 7.1, 7.2 and K, the threshold
  n >= 2^40 and the bound m >= 600000 of Section 13 (here m >= 62899 * 2^20/100000 > 659000) are F-LIMIT's.
- Sections 8, 14 and 15 keep F-LIMIT's structure and wording with the new ratios: fact (8.5) for the new
  ell and m, the size bound (8.3) with eP, the capacity Lemma 8.1 at the new ratios, and two separate
  exponents in place of one. F-LIMIT's facts Y + 1 <= 2r + 1 <= 8 ell and m >= 600000 still hold, as
  ell >= 23547r/50000 > r/4 and m >= 62899r/100000.
- Sections 0, 1 and 17 have the new name, parameters, provenance and scope.

The trade made here, cutting pool levels below a deeper collimation tree so that the source count and the
pool fall while the work rises, is the one qzv made for SPC-127 (submission
0efb267b-c55e-49cb-946b-ea3ced57f221) in SPQ-134, SPQ-139 and SPQ-143 (submissions
1201acdd-7646-43e1-b9f5-a9199f3210ea, cc47881a-0e4d-4be3-95d5-a3c058f40f20 and
371c911c-27e3-418a-b48e-4973b20d1207). We apply it to F-LIMIT's FW stage; no text of those submissions is
used. mpjunior92's PARTROOT197-Q1 (2a60bf68-b473-45cb-ac14-f400f8787b90) is a point of the same kind of
trade for their odd-partition family at a different point (S_Q = Q = 2^(sqrt n)); it is not used here.

F-LIMIT's own provenance, from its Section 1, follows; there "F-LIMIT" is the balanced configuration.

F-LIMIT is qzv's HPC-127 (public submission 2aad498c-d5e9-4f64-a222-3b2f7f961738 on this
challenge) with one change: its pairing stage (HPC-127 Section 7) is replaced by a stage built on an
instrument FW on w = 2^28 equal-key qubits, and the schedule is re-derived for it.
- Sections 2, 3, 4, 6, 11, 12 and 16 are HPC-127's text unchanged. Section 5 differs only in the
  algorithm name.
- Sections 9, 10 and 13 are HPC-127's text with these edits. Section 9: step 2 and Lemma 9.2 use
  FWLEVEL with q(Y+1) rounds, the slot bound C_i/(4 w ell) and the bounds of Lemma 7.2. Section 10:
  the sigma-field, one sentence of the proof of Lemma 10.1 and one sentence of the incidence
  paragraph name FW and PREP outcomes and index maps instead of PAIR's. Section 13: the threshold
  2^40, the stage name, its abort term and the constant m >= 600000.
- Sections 8 and 14 keep HPC-127's structure with new constants: the ratio RHO = 16385/8192, the
  bracket 1 < log2 RHO < HI proved from the series of ln 2, the slot rule, the capacity Lemma 8.1
  for the new ratios, and the exponents. Sections 1 and 7 are new; Sections 0, 15 and 17 carry the
  new name and constants.

Lineage. Our TRIAD-125 (f5b375dd-1e5c-4728-95dc-b855b2dc5827, three qubits) and G4-124
(b48a1af4-3e6b-45d7-8cdb-a414739ddc21, four qubits) make the same kind of replacement; the layout of
Sections 7, 8 and 14 and the phantom-outcome yield argument follow G4-124. HPC-127 restates the
framework of CS1 (AdamGagol, f1481815-9577-4990-abe3-7b79fa5d9284) in Sections 2-6 and 10-12, and its
Lemma 7.2 uses a bucket count of the kind also in PSieve (spariev, 4256e671-97b0-4f84-82ce-12aeee17224e).
Overlapping non-projective instruments with a phase-independent outcome law were introduced on this
challenge by 0xplemonade's CYC1 (7a4cecdc-7941-4027-8c95-8520de9fbcf3). mpjunior92's PART7, PART31 and
PART127 rows (1e083775-5d0a-4070-bcdc-ded8ada75d3a, 38897382-d7d7-44fe-8205-64ad028a41a5,
d444e283-4dcc-4836-a82b-bc1e6866e25b) are prior board work on the same cell family for odd group sizes;
FW is the even-size case, with its own realization and proof here, derived independently. Kuperberg (SIAM J. Comput. 35(1), 2005; arXiv:1112.3333) is the source of pairing and
collimation. These citations are context; every step used is proved below, and no earlier verdict is a
premise.

New in F-LIMIT: the instrument FW for w = 2^28 with its exact realization by a Hadamard ticket and uniform
registers prepared by repeat-until-success before the data is touched (Section 7.1); the closed form of
its yield ratio and the rational bound (7.4) (Lemma K); the distribution-free yield Lemma 7.2 with all
w-dependent constants; and the schedule of Section 8. Motivation only: a pool level costs log2 of the
net inputs per advancing output, 3 for HPC-127's PAIR and below RHO = 2 + 2^-13 here, and the pairing-
then-tree yield integral turns this into a coefficient near 2/sqrt 3 = 1.1547. The theorem rests only
on the explicit schedule of Section 8. As in HPC-127 the pool is held coherently.

New in this submission: only the parameter choice above, fact (8.5) and the capacity Lemma 8.1 at the new
ratios (Section 8), and the exponent accounting (Sections 14-15). The construction is F-LIMIT's. Motivation
only: with ell = l r, m = mu r, dl = d r, Lemma 8.1's capacity is about (l^2/2 + l mu + mu d + mu^2/2) r^2,
the pool exponent about l + mu and the tree exponent mu + d; with pool exponent q and tree exponent X the
best mu is X/2, and the capacity is about (q^2/2 + X^2/4) r^2. F-LIMIT takes q = X (near 2/sqrt 3); here
q = 1.09998 and X = 1.25798, which leaves the capacity coefficient 1.00055 (Lemma 8.1).

## 2. Model and counting conventions

A CORE STEP is one of: a NOT/CNOT/Toffoli/H/S/S^dagger gate; a computational-basis
single-qubit measurement or reset; a Boolean operation on at most three classical bits; a
classical bit read or write. Toffoli has an exact constant-size Clifford+T decomposition.
Integers are bit strings; an L-bit addition, comparison or copy costs O(L) core steps.
Generating a gate costs O(1) core steps. Each core step additionally pays its address,
ceil(log2(Mem+2)) bit operations, where Mem <= S_C + S_Q is the number of allocated bits and
qubits. Gates on pooled qubits are classically addressed through this charge; there is no
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

IDEAL run. The ideal run is FLQ110 in the latent-label model with every LE output replaced by the
latent k. Actual and ideal runs can be coupled to coincide unless some LE call returns a wrong
label, so every event's probability differs by at most 2^-10. Resource bounds are proved for every
ACTUAL branch directly, because they rest only on caps and fixed allocations.

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

## 7. The FW stage

A LABELED QUBIT is a phase vector of length 2 with table (t0, t1); write Del = t1 - t0, an integer that
may be negative. It is COLLIMATED TO p if Del = 0 mod 2^p.

Pool invariant (P). In the ideal run, conditional on all latent labels and on every classical outcome
and decision so far, the qubits held in the pool are in a pure product state: each is exactly the phase
vector of its recorded table (for the fixed real th of the batch, up to a global phase), in tensor
product with every other pool qubit and with all other registers. (P) holds for leaf qubits: by
Section 3 a transformed copy is exactly rho_(s') for a known s', so conditional on its latent label k
it is the pure product phi_k(s') (x) chi_k; LE (Section 5) leaves the control qubit, a spectator,
unchanged; the data register is then reset; and X on the control gives the positive qubit of the
supplier's specification (Section 9). (P) is preserved by measuring or releasing a pool qubit and by
FW (Lemma 7.1), whose PREP steps touch only fresh ancillas.

Throughout, w = 2^28 is the GROUP SIZE and q = w/2 = 2^27. w is an absolute constant.

### 7.1 The instrument FW

Uniform registers. For an integer N with 3 <= N <= w - 1 put j_N = ceil(log2 N) <= 28 and
U_N = N^(-1/2) sum_(v<N) |v>, a state of j_N qubits. PREP(N): up to 3r times (r from Section 0), put
j_N fresh qubits in |0>, apply H to each, XOR the flag [v < N] into a fresh qubit (a comparison with a
constant, computed cleanly with O(1) Toffoli/CNOT/NOT gates), measure the flag and reset it; if it was
1, stop: the register R_N holds exactly U_N, because measuring the flag projects the uniform state onto
v < N. Otherwise measure and reset the j_N qubits and try again. If all 3r tries fail, ABORT. Each try
touches only its fresh qubits and succeeds with probability N/2^(j_N) > 1/2, independently of
everything else (probability 1 if N is a power of 2), so PREP(N) aborts with probability below 2^(-3r).

Input: labeled qubits A_0, ..., A_(w-1) on disjoint qubits, with tables (t0^i, t1^i), and x in {0,1}^w
for their computational-basis value. Write h = |x|, put mu = 1 if h <= q and mu = 0 otherwise, let
M = {i : x_i = mu} = {m_0 < ... < m_(u-1)}, so u = |M| = min(h, w - h), and let
J = {i : x_i != mu} = {j_0 < ... < j_(w-1-u)}. CELLS are subsets of {0,1}^w:
- PAIR CELLS P_ab = {x : x_a != x_b} for 0 <= a < b < w (the other w - 2 qubits unconstrained);
- MATCHING CELLS: for 1 <= u' <= q - 1, u' disjoint pairs {a_k, b_k} and the set Bl of the other w - 2u'
  positions, Q = {x : x_(a_k) != x_(b_k) for all k, and x is constant on Bl};
- Ev = {0^w, 1^w}.
Weights: y = 1/q^2 for a pair cell, y = (q - u')^2 (w - 2u')!/(q^2 (w - u')!) for a matching cell with
u' pairs, and y = 1 for Ev.

Incidence. (I1) If u >= 1, x lies in P_ab iff exactly one of a, b is in M, so in exactly u(w - u) pair
cells. (I2) If x lies in a matching cell Q with u' pairs, let z0 be its value on Bl; x takes the value
z0 on u' + (w - 2u') = w - u' >= q + 1 positions and 1 - z0 on u' <= q - 1, so 1 - z0 = mu, u = u', and M
consists of one element of each pair. Conversely, if 1 <= u <= q - 1, every injection phi : M -> J gives
the matching cell with pairs {m, phi(m)} and Bl = J \ phi(M), which contains x (x = mu on M and 1 - mu
on J). So the matching cells containing x correspond bijectively to these injections; there are
(w - u)!/(w - 2u)! of them if 1 <= u <= q - 1 and none otherwise. (I3) Ev contains x iff u = 0, and then x
lies in no other cell. Since u(w - u) + (q - u)^2 = q^2, the total weight of the cells containing x is 1
for every x. FW realizes these weights exactly as follows.

Cell register. P has w fields of 29 qubits; the code of a cell C is p(C) with p_i = the other element of
i's pair if i is in a pair of C, p_i = w if i is unconstrained (pair cells), and p_i = w + 1 if i is in Bl
(matching cells) or anywhere (Ev). The code is a function of the cell alone.

Two classical maps. Let t = q a + b with a, b in [0, q), and let R = (R_N) be values R_N in [0, N).
cell(x, t, R): if u = 0, return p(Ev). If a < u, return p(P_(m_a j_b)). If a >= u and b < u, return
  p(P_(m_b j_(q+a-u))). Otherwise (a, b >= u, so u <= q - 1): let L be the list j_0, ..., j_(w-1-u); for
  k = 0, ..., u-1, remove from L its element of 0-based index R_(w-u-k) (valid, since L has w - u - k
  elements before this removal) and call it pt_k; return the code of the matching cell with pairs
  {m_k, pt_k} and Bl = the rest of L.
back(x, p): if p codes a pair cell {c, d}, c < d, put c' = c if c is in M and c' = d otherwise, let d'
  be the other one, i the rank of c' in M and k the rank of d' in J (0-based, increasing; 0 if absent);
  return t = q i + k if k < q and t = q(k - q + u) + i if k >= q, and all R_N = 0. If p codes a matching
  cell, put L = (j_0, ..., j_(w-1-u)) and, for k = 0, ..., u-1, let v_k be the index in L of pt = p_(m_k)
  (0 if absent) and remove pt from L; return t = 0, R_(w-u-k) = v_k for k < u and R_N = 0 otherwise.
  Otherwise return all zeros.

(B1) Let u >= 1. Case a < u gives the pair (m_i, j_k) with (i, k) = (a, b), k < q; case a >= u > b gives
(i, k) = (b, q + a - u) with q <= k < w - u, since u <= a < q. Together these qu + (q - u)u = u(w - u)
tickets map bijectively onto [0,u) x [0,w-u), that is onto the pair cells containing x by (I1), and back
returns t. The remaining (q - u)^2 tickets form D_u = {q a + b : a, b >= u}.
(B2) Let 1 <= u <= q - 1 and t in D_u. Removing the elements of indices v_0, ..., v_(u-1) from a list in
turn is a bijection from [0,w-u) x [0,w-u-1) x ... x [0,w-2u+1) onto the sequences (pt_0, ..., pt_(u-1)) of
distinct elements of J, the inverse being v_k = index of pt_k after the earlier removals. So by (I2) the
values of R_N for N in S_u = {w-u, ..., w-2u+1} map bijectively onto the matching cells containing x
(pt_k is the partner of m_k), the other registers are not read, and back returns those values.

Circuit. Ancillas, all fresh |0>: a 54-qubit ticket register T, the registers R_3, ..., R_(w-1)
(together the register R, at most 28 w qubits), the cell register P, and scratch.
1. Apply H to each qubit of T. Run PREP(N) for N = 3, ..., w - 1.
2. XOR cell(x, t, R) into P.
3. XOR back(x, P) into (T, R).
4. Measure P, obtaining the code of a cell C, and reset P. If C = Ev, apply H to each qubit of T. If C
   is a matching cell, measure T and reset it. Measure and reset every R_N.
5. Post-processing. For each pair {a, b} of C with a < b: apply CNOT with A_a as control and A_b as
   target; A_b is then exactly |1>; apply NOT to it and release it. A_a is a GOOD output with table
   (t0^a + t1^b, t1^a + t0^b). If C has a block Bl = {c_0 < c_1 < ...} (Bl = all of [0,w) for Ev),
   apply CNOT A_(c_0) -> A_(c_i) for each i >= 1; these are then exactly |0>; release them. A_(c_0) is
   the RECYCLED output with table (sum_(c in Bl) t0^c, sum_(c in Bl) t1^c). The qubits unconstrained by
   C (w - 2 of them for a pair cell) are RETURNED with their tables unchanged.
So a pair cell yields one good output and returns w - 2 qubits; a matching cell with u pairs yields u
good outputs and one recycled output; Ev yields one recycled output.

Gates. Steps 2 and 3 XOR a fixed Boolean function of the qubits of x, T, R and P into a register that is
not among its inputs. Each function is a fixed classical program: popcount, prefix counts, ranks, and at
most q selections without replacement among w positions, so a Boolean circuit of at most w^3 gates whose
size depends on w only. Compute it with Toffoli (AND), CNOT (XOR) and NOT on fresh scratch, CNOT the
result into the target, and uncompute in reverse order, as for modular addition in Section 3. So FW
uses at most c_F NOT/CNOT/Toffoli/H gates, measurements and ancilla qubits, where c_F <= 2^90 is an
absolute constant, plus the PREP tries (at most 3r of O(1) core steps for each of the w - 3 registers)
and O(w n) classical steps for the table additions. No rotation synthesis occurs: every amplitude is
produced by H gates and by the projections of PREP.

Lemma 7.1 (FW). Assume every PREP succeeds. (a) and (b) assume that, conditional on the past,
A_0, ..., A_(w-1) are in the product state psi = (x)_i 2^(-1/2) (exp(2 pi i t0^i th)|0> +
exp(2 pi i t1^i th)|1>), in tensor product with the rest of the system, which is in an arbitrary state.
(a) The measured cell C has probability y_C |C|/2^w: 2/w^2 for each pair cell, so (w - 1)/w in total;
    pi_u = 2 C(w,u) (q - u)^2/(q^2 2^w) in total over the matching cells with u pairs, each having the same
    probability; and 2^(1-w) for Ev. Given C, the other values measured in step 4 are independent of the
    labels and of th: if C is a matching cell with u pairs, T is uniform on D_u and R_N = 0 for N in S_u;
    every other R_N is uniform on [0, N). All this holds whatever the labels, th and the past.
(b) Given a pair cell P_ab, a < b, the good output is exactly the phase vector with table
    (t0^a + t1^b, t1^a + t0^b), label difference Del_a - Del_b, and the w - 2 returned qubits are exactly
    in their input states. Given a matching cell, the good output of each pair {a, b}, a < b, is
    exactly the phase vector with table (t0^a + t1^b, t1^a + t0^b), and the recycled output is exactly
    the phase vector with the stated block table, label difference sum_(c in Bl) Del_c; given Ev, the
    recycled output carries the sum of the w tables. In each case the outputs are in tensor product
    with each other and with the unchanged rest.
(c) For every input state, ideal or not, steps 1-4 realize the instrument with outcomes
    omega = (C, z), z the other values measured in step 4, and Kraus operators c_omega Pi_C, where Pi_C
    is the projector onto the span of |x>, x in C, and sum over z of c_omega^2 = y_C; tensored with the
    identity on the rest, with every ancilla back in |0>. Step 5 then leaves every released qubit in
    |0> on every input.

Proof. Write any joint state (purify the rest if it is mixed) as Psi = sum_x |x> (x) |R_x>. After step
1, Psi carries q^(-1) sum_t |t> (x) (x)_N U_N. Steps 2 and 3 act on each term |x>|t>|R> as
|x>|t>|R>|0> -> |x>|t xor back_T>|R xor back_R>|cell(x,t,R)>. By (B1), (B2) and (I3):
- the terms with u >= 1 and t not in D_u give sum_(pair cells C containing x) q^(-1)|0>_T ((x)_N U_N) |p(C)>;
- the terms with 1 <= u <= q - 1 and t in D_u give q^(-1) sum_(t in D_u) |t>_T times
  prod_(N in S_u) N^(-1/2) sum_(matching C containing x) |0>_(S_u) ((x)_(N not in S_u) U_N) |p(C)>;
- the terms with x in Ev give |+>^54_T ((x)_N U_N) |p(Ev)>.
Every x in a matching cell with u pairs has u(x) = u by (I2), so after measuring P = p(C) the state is
- q^(-1) (Pi_C (x) I) Psi (x) |0>_T (x)_N U_N for a pair cell,
- q^(-1) prod_(N in S_u) N^(-1/2) (Pi_C (x) I) Psi (x) (sum_(t in D_u) |t>) |0>_(S_u) (x)_(N not in S_u) U_N
  for a matching cell, and
- (Pi_Ev (x) I) Psi (x) |+>^54 (x)_N U_N for Ev.
The ancilla factor does not depend on x in each case, so measuring T (matching cells) and the R_N gives
Kraus operators c Pi_C, with c^2 summed over the junk equal to 1/q^2, to (q - u)^2/q^2 prod_(N in S_u) 1/N
= y_C, and to 1. The H gates return T to |0> for Ev, and every measured ancilla is reset. In step 5, a
pair {a, b} of C has x_a != x_b on the support, so after CNOT A_a -> A_b the value of A_b is 1 on every
term; Bl is constant on the support, so after the CNOTs from A_(c_0) the others are 0. This is (c).
For the product input, |R_x> = 2^(-w/2) exp(2 pi i phi(x)) |R> with phi(x) = th sum_i t_(x_i)^i, so
Pr[C] = y_C ||Pi_C psi||^2 = y_C |C|/2^w, using only the moduli; |P_ab| = 2^(w-1), |Q| = 2^(u+1) and
|Ev| = 2; and the junk factors are fixed states. This is (a): the matching cells with u pairs all have
the same weight and size, and summing y_C |C|/2^w over them counts, by (I2), each of the 2 C(w,u) points
of weight u or w - u with total weight (q - u)^2/q^2.
For (b): P_ab = {x_a != x_b} x {0,1}^(w-2), so Pi_(P_ab) psi is
[2^(-1)(exp(2 pi i (t0^a + t1^b) th)|0_a 1_b> + exp(2 pi i (t1^a + t0^b) th)|1_a 0_b>)] (x) (the other
w - 2 input states), and CNOT A_a -> A_b maps |0 1> to |0 1> and |1 0> to |1 1>. A matching cell is the
product over its pairs of {x_a != x_b} and of {x constant on Bl}, so Pi_Q psi is the product of the pair
factors above and of 2^(-|Bl|/2)(exp(2 pi i th sum_Bl t0^c)|0...0> + exp(2 pi i th sum_Bl t1^c)|1...1>),
and the CNOTs from A_(c_0) map |y...y> to |y 0...0>. Ev is the case Bl = [0,w). QED.

Every table produced is a sum of input tables over disjoint inputs: a good output's entry alpha is the
sum of entry alpha of A_a and entry 1 - alpha of A_b, for its pair {a, b}; a recycled output's entry
alpha is the sum of entry alpha over its block; a returned qubit keeps its table. By (b), (P) is
preserved. Only the TYPE of an outcome matters below: (gamma, rho) = (1, 2) for a pair cell, (u, w - 1)
for a matching cell with u pairs, (0, w - 1) for Ev, where gamma is the number of good outputs and rho the
number of qubits that leave the live list (w inputs, w - 2 or 1 put back). By (a) the type has the law

    Pr[(1,2)] = (w-1)/w,   Pr[(u,w-1)] = pi_u (1 <= u <= q - 1),   Pr[(0,w-1)] = 2^(1-w).          (7.2)

In every type 2 gamma <= rho.

Lemma K (yield ratio). Let gbar = E[gamma], rhobar = E[rho] under (7.2), and b = C(w, q)/2^w. Then
rhobar = 3(w - 1)/w, gbar = 3/2 - 1/w - b, and so rhobar/gbar = 6(w - 1)/(3w - 2 - 2wb). Moreover
b <= (3q + 1)^(-1/2), and with s = 20066, s^2 = 402644356 <= 402653185 = 3q + 1, so b <= 1/s and

    gbar/rhobar >= 8192/16385,   that is rhobar/gbar <= RHO := 16385/8192 = 2 + 2^-13.        (7.4)

Also 1 <= gbar <= 3/2.

Proof. Under (7.2), the type is a function of h = |x| for x uniform on {0,1}^w (Lemma 7.1(a) is the
average over x of the cell weights at x), so h ~ Bin(w, 1/2). Given h with u = min(h, w - h) >= 1, the
pair type has probability u(w - u)/q^2 = 4h(w - h)/w^2 and the matching type probability (q - u)^2/q^2.
Since E[h(w - h)] = (w^2 - w)/4, the pair type has probability (w - 1)/w, and the other types 1/w; so
rhobar = 2(w - 1)/w + (w - 1)/w. Put D = h - q, so u = q - |D| and (q - u)^2/q^2 = D^2/q^2. Then
gbar = (w - 1)/w + E[(D^2/q^2)(q - |D|)] = (w - 1)/w + E[D^2]/q - E|D|^3/q^2, with E[D^2] = w/4 = q/2.
For j >= 1, j C(2q, q+j) = q (C(2q-1, q+j-1) - C(2q-1, q+j)), so summing by parts,
sum_(j>=1) j^3 C(2q, q+j) = q sum_(j>=1) (2j - 1) C(2q-1, q+j-1). With N' = 2q - 1 and k = q + j - 1 this is
q sum_(k>=q) (2k - N') C(N', k) = q N' C(2q-2, q-1), because k C(N', k) = N' C(N'-1, k-1),
sum_(k>=q) C(N', k) = 2^(N'-1) and sum_(i>=q-1) C(2q-2, i) = (4^(q-1) + C(2q-2, q-1))/2. Since
C(2q, q) = (2(2q-1)/q) C(2q-2, q-1), this equals q^2 C(2q, q)/2, and by symmetry E|D|^3 = q^2 b. Hence
gbar = (w - 1)/w + 1/2 - b. For the bound, b_1 = 1/2 and b_(k+1) = b_k (2k+1)/(2k+2) for
b_k = C(2k, k)/4^k, and (2k+1)^2 (3k+4) = (2k+2)^2 (3k+1) - k, so b_k^2 (3k+1) <= 1 for all k by induction.
Then gbar/rhobar >= (3/2 - 1/w - 1/s) w/(3(w - 1)) = (3ws - 2s - 2w)/(6s(w - 1)), and (7.4) is the integer
inequality 16385 (3ws - 2s - 2w) >= 8192 * 6 s (w - 1): the difference of its sides is
(3s - 32770) w + 16382 s = 27428 * 2^28 + 16382 * 20066 > 0. Finally 3/2 >= gbar >= 3/2 - 1/w - 1/s >= 1. QED.

### 7.2 FWLEVEL

FWLEVEL(pool, Cin, p, c, rounds). Input: Cin labeled qubits collimated to p; integer c >= 0,
E = 2^c. A qubit's KEY is Del mod 2^(p+c), computed from t1 and t0 modulo 2^(p+c). Keep a LIVE list,
initially all inputs, and an OUTPUT list, initially empty. Repeat for exactly `rounds` rounds:
merge-sort LIVE by key; scan it and cut each maximal run of equal keys into consecutive groups of w,
leaving the last (run length mod w) <= w - 1 qubits of the run ungrouped; then apply FW to each group,
in scan order, with A_0, ..., A_(w-1) its qubits in scan order. Good outputs are appended to OUTPUT;
returned and recycled qubits are put in LIVE for the next round; ungrouped qubits also stay in LIVE.
After the last round measure, reset and release LIVE.

Invariants. Every LIVE qubit is collimated to p: a returned qubit keeps its table, and a recycled one
has label difference sum_(c in Bl) Del_c = 0 mod 2^p. Every OUTPUT qubit is collimated to p+c, because
equal keys give Del_a - Del_b = 0 mod 2^(p+c). The sort keys read only label bits below p+c. The groups
of a round are fixed before its first FW, and the w qubits of a group are distinct pool qubits.

Operation count. Number the FWs of the level whose step 4 is executed k = 1, ..., A, in order, with
types (gamma_k, rho_k). The k-th removes its w inputs from LIVE and puts back w - rho_k qubits, and
nothing else changes the size of LIVE; it appends gamma_k <= rho_k/2 qubits to OUTPUT. So A <= Cin/2 and
|OUTPUT| <= Cin/2, and if the level ends without ABORT, with S_end qubits live after the last round and S
the size of OUTPUT,

    Cin - S_end = sum_(k=1)^A rho_k,     S = sum_(k=1)^A gamma_k.                                 (7.3)

Live count. LIVE qubits are collimated to p, so their keys take at most E = 2^c values, and a round
leaves at most w - 1 qubits per key ungrouped. In one round with ug <= (w - 1)E ungrouped qubits, a list of
length L becomes at most ug + (L - ug)(1 - 2/w) <= (1 - 2/w) L + 2(w - 1)E/w, and it never grows. So
L_j - (w - 1)E <= (1 - 2/w)^j Cin. With (1 - 2/w)^rounds Cin < 1, at the end L_rounds - (w - 1)E < 1, that
is S_end <= (w - 1)E, deterministically, whatever the labels and outcomes.

Lemma 7.2 (distribution-free FW yield). Let ell >= 2, E <= Cin/(4 w ell) and (1 - 2/w)^rounds Cin < 1.
For ANY labels, and conditional on everything before the level, the level ABORTs with probability at
most w Cin 2^(-3r), and it ends without ABORT with S < (ell - 1) Cin/(RHO ell) with probability at most
2 exp(-Cin/(10 ell^2 w^2)).

Proof. At most A + 1 <= Cin/2 + 1 FWs start, each runs PREP for the w - 29 values of N in [3, w-1] that
are not powers of 2, and (w - 29)(Cin/2 + 1) <= w Cin; each such PREP aborts with probability below
2^(-3r) given the past, which gives the abort bound. For the yield, for k > A let the type of the k-th FW
be drawn from an independent source with the law (7.2) (phantom outcomes, which the algorithm never
draws). Let F_k be the sigma-field of the history up to the measurement of the k-th FW of the level, its
PREP outcomes included, or up to the end or ABORT of the level if A < k, joined with the phantom types for
A < j < k. Then F_1 contains everything before the level and the labels, F_k is contained in F_(k+1), and
the event A >= k and, on it, the k-th group are F_k-measurable. By (P) and Lemma 7.1(a) on {A >= k}, and
by construction on {A < k}, the k-th type has law (7.2) given F_k for every k. Since the earlier types are
F_k-measurable, the tower property gives, for every fixed z and every sequence o of z types,
Pr[types 1..z = o | F_1] = Pr[types 1..z-1 = o' | F_1] Pr_(7.2)[o_z], so by induction on z the first z
types are independent with law (7.2), conditional on everything before the level.
Put g = 1/(4 ell) <= 1/8, so (w - 1)E <= g Cin and Cin >= 4 w ell, and z = floor((1 - 2g) Cin/rhobar).
Since 2 <= rhobar < 3, Cin/5 <= Cin/4 - 1 <= z <= Cin/2. Let Vz = gamma_1 + ... + gamma_z and
Wz = rho_1 + ... + rho_z. If the level ends without ABORT and A <= z, then by (7.3), S_end <= (w - 1)E and
rho_k > 0, Wz >= Cin - S_end >= (1 - g) Cin, so Wz - rhobar z >= g Cin. The rho_k lie in [2, w - 1], so
by Hoeffding

    Pr[Wz - rhobar z >= g Cin] <= exp(-2 (g Cin)^2/(z w^2)) <= exp(-4 g^2 Cin/w^2) = exp(-Cin/(4 ell^2 w^2)).

If A > z then gamma_1, ..., gamma_z are actual and S >= Vz. The gamma_k lie in [0, q], so by Hoeffding

    Pr[Vz < (1 - g) gbar z] <= exp(-2 (g gbar z)^2/(z q^2)) <= exp(-8 g^2 z/w^2) <= exp(-Cin/(10 ell^2 w^2)),

using gbar >= 1 and z >= Cin/5. Outside the two events, by (7.4) and gbar <= 3/2,
S >= (1 - g) gbar z >= (1 - g) gbar ((1 - 2g) Cin/rhobar - 1) >= (1 - 3g) Cin/RHO - 3/2
= (ell - 1) Cin/(RHO ell) + Cin/(4 RHO ell) - 3/2 >= (ell - 1) Cin/(RHO ell), since Cin >= 4 w ell. QED.

No property of the label distribution is used. Returned qubits keep their key and recycled ones get
|Bl| times the common key modulo 2^(p+c), so the keys of later rounds are correlated with earlier
outcomes; the proof does not care, since it uses only (7.3), the live count and the outcome law, which
is the same for every group. The number A of operations is random, because the cells consume 2 or w - 1
live qubits; the phantom extension and the deterministic bound S_end <= (w - 1)E handle this, and no Wald
argument is needed at this stage (Wald's identity is used only for the tree, Lemma 9.1).

Cost. Each list entry stores t0, t1 and the wire index of its qubit, O(n) bits. A round on L live qubits
costs O(L log L) comparisons of O(n)-bit keys and at most L/w FWs, each at most c_F gates plus at most
3rw PREP tries of O(1) core steps and O(w n)-bit table additions and wire-index reads: O(L n log L) core
steps, since w and c_F are absolute constants and r = O(n). Since L_j <= (w - 1)E + (1 - 2/w)^j Cin,
sum_j L_j <= (w/2) Cin + w rounds E, and a level costs O((Cin + rounds E) n log Cin) core steps, with
O(1) ancilla qubits beyond the pool. The number of rounds is fixed, and these bounds hold on every branch.
## 8. The schedule

Pool sizes. Put RHO = 16385/8192 = 2 + 2^-13 (Lemma K). Define C_ell = 2^12 n K 2^m dl, with K from (11.0),
and for i = ell-1, ..., 0, C_i = ceil(16385 ell C_(i+1) / (8192 (ell - 1))). Then, with
rho = RHO ell/(ell-1) >= RHO >= 2,

    C_i >= RHO^(ell-i) C_ell >= 2^(ell-i) 2^m,                                         (8.1)
    C_0 <= rho^ell (C_ell + 1) <= 2 rho^ell C_ell <= 8 RHO^ell C_ell,                  (8.2)

since C_i <= rho C_(i+1) + 1, sum_(j<ell) rho^j <= rho^ell, and (1 - 1/ell)^(-ell) <= 4 for ell >= 2.
Let Y be the least integer with 2^Y >= C_0. Each level uses rounds = q (Y + 1), q = 2^27; since
1 - 2/w < exp(-2/w), (1 - 2/w)^q < 1/e < 1/2, so (1 - 2/w)^rounds C_i < 2^-(Y+1) C_0 < 1 for every i.

Bracket for log2 RHO. Since RHO > 2, log2 RHO > 1. Since ln 2 = sum_(k>=1) 1/(k 2^k) (the series of
-ln(1 - 1/2)) and all its terms are positive, ln 2 > sum_(k=1)^8 1/(k 2^k) = 148969/215040 > 6927/10000.
Since ln(1 + x) < x for x > 0, log2 RHO = 1 + ln(1 + 2^-14)/ln 2 < 1 + 2^-14 * 10000/6927 =: HI. So

    1 < log2 RHO < HI,   and   HI (23547/50000) + 62899/100000 < eP := 54999/50000.         (8.5)

(The last fact is exact rational arithmetic: HI (23547/50000) = 23547/50000 + 235470000/(50000 * 6927 * 2^14).)

Size bound. From (8.2), using RHO^ell <= 2^(HI ell), ell <= 23547r/50000 + 1, m <= 62899r/100000 + 1,
K <= 3 * 2^13 r (as 2r + ceil(log2 n) + 30 <= 3r), dl <= r and n <= r^2, and (8.5),

    log2 C_0 <= eP r + 4 log2 r + 32 <= 2r - 1.                                            (8.3)

(The constant: 3 from (8.2), HI + 1 from the roundings of ell and m, and 12 + 13 + log2 3 from 2^12, K and
n dl <= r^3, a total below 32.) So Y <= 2r <= n (as r <= sqrt n + 1 and n >= 2^40), and 2^Y <= 2 C_0.

Level capacities.
- FW level i (0 <= i < ell): pbmax_i is the largest integer b with 2^b * 4 w ell <= C_i.
- Tree: lam_i = dl + i for 0 <= i <= m-1, lam_m = 1; tbmax_i = dl + i - kappa - 1 for 0 <= i <= m-2;
  tbmax_(m-1) = 2 (dl + m - 1) - kappa - 1.

For every b_i <= tbmax_i, in all cases

    b_i + lam_(i+1) - 2 lam_i <= -kappa.                                            (8.4)

Lemma 8.1 (capacity). For n >= 2^40: sum_i pbmax_i + sum_i tbmax_i >= r^2 >= n.

Proof. By maximality 2^(pbmax_i) * 8 w ell > C_i, so by (8.1), pbmax_i > (ell - i) + m - log2(8 w ell).
Summing over i < ell,

    sum_i pbmax_i >= ell^2/2 + ell m - ell log2(8 w ell).

Direct expansion gives sum_i tbmax_i = m dl + m^2/2 + dl + m/2 - 1 - m (kappa + 1) >= m dl + m^2/2 - m (kappa + 1).
With ell >= 23547r/50000, m >= 62899r/100000, dl >= 62899r/100000, the positive terms total at least

    ( (23547/50000)^2/2 + (23547/50000)(62899/100000) + (62899/100000)^2 + (62899/100000)^2/2 ) r^2
    = (20011028451/20000000000) r^2 >= (1 + 5.51 * 10^-4) r^2.

For r >= 2^20 we have ell <= 0.470941 r, m <= 0.628991 r, log2(8 w ell) <= log2 r + 29.92 and
kappa + 1 <= log2 m + 3 <= log2 r + 2.34. So the subtracted terms are at most r (1.09994 log2 r + 15.57).
Finally 5.51 * 10^-4 r >= 1.09994 log2 r + 15.57 at r = 2^20, where 577.7 >= 37.6, and for larger r because the
left side grows faster (its derivative 5.51 * 10^-4 exceeds 1.09994/(r ln 2), which is below
1.09994 * 1.5/2^20 < 1.6 * 10^-6). QED.

Bit allocation. Given integer B with 1 <= B <= n, allocate exactly B bits greedily: first pb_0, ..., pb_(ell-1)
in that order, pb_i = min(pbmax_i, bits still unallocated), then tb_(m-1), ..., tb_0 likewise. By Lemma 8.1 this
exhausts B. Positions: pp_0 = 0, pp_(i+1) = pp_i + pb_i; tp_0 = pp_ell, tp_(i+1) = tp_i + tb_i; so tp_m = B. Every
bit read below has position below B.
## 9. BATCH(supplier, B)

Input: a supplier of LEAF QUBITS: positive qubits with phase exp(2 pi i k th) for a fixed real th and a known
label k, where in the ideal run the labels are independent and uniform on [0, 2^(B+1)). Output: K measured-ready
roots, or ABORT. A leaf qubit is a labeled qubit with table (0, k).

1. POOL. Obtain C_0 leaf qubits (qubits held in the quantum pool, labels in a classical list). The supplier may
   ABORT.
2. FW STAGE. For i = 0, ..., ell-1 run FWLEVEL(pool, C_i, pp_i, pb_i, q(Y+1)). If it yields fewer than C_(i+1)
   qubits, ABORT; otherwise keep the first C_(i+1) and measure and release the rest. By the invariants the final
   pool qubits are collimated to pp_ell, and E_i = 2^(pb_i) <= C_i/(4 w ell) by definition of pbmax_i, while
   (1 - 2/w)^(q(Y+1)) C_i < 1 (Section 8).
3. TREE. VEC(0) = LEAF: take the next dl qubits of the final pool (ABORT if fewer remain). Their qubits form the
   index register, bit j = qubit j. With tables (t0_j, t1_j), build lab[0] = sum_j t0_j and
   lab[x + 2^j] = lab[x] + t1_j - t0_j for x < 2^j. The table has length 2^dl, is exactly the tensor product state in
   the ideal run, and is collimated to tp_0 because every difference is 0 mod 2^(tp_0).
   VEC(i), i >= 1: repeat X1 = VEC(i-1), X2 = VEC(i-1), out = MERGE(X1, X2; tp_(i-1), tb_(i-1), lam_i), until
   out != FAIL; return out. A root is VEC(m), evaluated depth-first. Run it K times, or ABORT if the pool runs out.

Root. VEC(m) is a two-entry table with lab[0] = lab[1] mod 2^B, so its ideal state is, up to global phase,

    (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2,   W = (lab[1] - lab[0])/2^B, a known integer.     (9.1)

Label bound. Each leaf qubit enters a table entry at most once and all pool qubits are distinct, so every label in
the batch is a sum of at most C_0 leaf labels below 2^(B+1). Thus every label is below 2^(Y+n+1), which fits in 3n
bits by Y <= n, and

    |W| <= 2 C_0 <= 2^(Y+1).                                                        (9.2)

Lemma 9.1 (no pool exhaustion). Conditional on any final-pool contents, in the ideal run the pool runs out before K
roots finish with probability at most 2^-10/n.

Proof. Extend the pool by phantom qubits with Del = 0, so that Lemma 6.1 applies throughout. By (8.4) and Lemma 6.1
each merge fails with conditional probability at most 2^-kappa given everything before it. Let A_i bound the
expected number of pool qubits consumed by VEC(i). Then A_0 = dl and, by Wald's identity,
A_(i+1) <= tt * 2 A_i with tt = 2^kappa/(2^kappa - 1). Since 2^kappa >= 2m, tt^m <= exp(m/(2m-1)) <= e < 3. So K roots
consume at most 3 K 2^m dl qubits in expectation, and Markov against C_ell = 2^12 n K 2^m dl gives the bound. The
phantom run coincides with the real run until exhaustion. QED.

Lemma 9.2 (FW-stage yield). In the ideal run, step 2 aborts with probability at most
2 ell exp(-2^m/(10 ell^2 w^2)) + ell w C_0 2^(-3r).

Proof. Lemma 7.2 applies at each level, conditional on the earlier levels, with Cin = C_i, 2^m <= C_i <= C_0 and
(ell - 1) C_i/(RHO ell) >= C_(i+1). QED.

## 10. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and tau_j in {0,1}. Since k_j is uniform on
[0, 2^(B+1)), low_j and tau_j are independent and tau_j is a fair bit. For a batch let G be the sigma-field generated
by: all low_j of its leaves; all FW outcomes (cells and the other values measured in step 4) and all PREP outcomes; all merge outcomes (e, bl); and all decisions of the controller in
that batch (sort orders, groupings into w-tuples, trimming, FAIL and retries, aborts, assignment of qubits). G does not include
root measurement outcomes, which no decision in the batch reads. It also excludes LE's internal coins and outcomes,
which in the ideal run feed no decision.

Lemma 10.1. In the ideal run, conditional on G and on all independent randomness outside the batch, the top bits tau_j
are i.i.d. fair.

Proof. Induct over the controller's steps. Every key, residue, sort, rank and block partition reads only label bits
strictly below position B, because all positions used are below B (Section 8). The supplier's acceptance
decisions (Section 11) read only whether k < 2^(B+1); given acceptance k is uniform on [0, 2^(B+1)), the law used
above. Bits below B of a sum of leaf labels,
and of a difference modulo 2^(p+c) with p+c <= B, depend only on the low_j, since multiples of 2^B do not change them.
PREP outcomes touch only fresh ancillas and depend on no label, and FW outcomes have the law of
Lemma 7.1(a) whatever the labels and the past (it applies at every FW by (P)); returned and recycled
qubits carry explicit tables, sums of leaf labels, so their later keys again read only bits below B. By Lemma 6.1 each merge outcome's conditional law, given
labels and earlier outcomes, is a function of the low_j and earlier outcomes only. So the joint law factorizes as
law(tau) x law(low) x law(outcomes and decisions | low). QED.

Incidence. An entry of a table is the sum over leaves j of x_j k_j, for a 0/1 incidence vector x. Distinct indices of a
table have distinct incidence vectors: this holds for a leaf qubit, table (0, k_j); in FW the index maps
alpha -> (alpha, 1 - alpha) on the pair (A_a, A_b) of a good output and alpha -> (alpha, ..., alpha) on the block
Bl of a recycled output are injective on disjoint coordinates, and a returned qubit keeps its table; a LEAF table
concatenates disjoint coordinates; and a merge re-indexes injectively pairs on disjoint coordinates. So the two root entries have x0 != x1, and with hd = |x0 xor x1| >= 1,

    W = cst + sum_(j in Sp) tau_j - sum_(j in Sm) tau_j,                            (10.1)

where cst = (sum_j low_j (x1_j - x0_j))/2^B is a G-measurable integer, and Sp, Sm are disjoint G-measurable sets with
|Sp| + |Sm| = hd. Each leaf enters at most one root, so given G the W's of distinct roots of a batch are independent.
Since E exp(2 pi i phi tau) = e^(i pi phi) cos(pi phi) for a fair bit, for every real phi

    | E[ exp(2 pi i phi W) | G ] | = |cos(pi phi)|^hd <= |cos(pi phi)|,             (10.2)

and, with phi = 1/2, Pr[W odd | G] = 1/2.                                           (10.3)

## 11. Odd part: s1 = s mod M by free-frequency decoding

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so dn - 1 >= a2. Put theta = s1/M. Every stage uses
B = dn - 1 (B >= 1 on the main branch) and

    K = 2^13 (2r + ceil(log2 n) + 30).                                              (11.0)

The stages are j = 0, ..., J, where J = min{ j >= 0 : 2^(j+3) > 2M }. Then J + 1 <= log2 M.

Supplier for stage j. Compute alpha_j by extended Euclid and CRT so that alpha_j = 1 (mod 2^a2) and
alpha_j = 2^j (2^(dn-1-a2))^(-1) (mod M); it is a unit modulo N. Make at most 4 C_0 acquisitions, stopping at C_0 accepted
qubits: acquire a fresh copy, apply Mult_(alpha_j), run LE to obtain k, accept iff k < 2^dn (otherwise discard) and on
acceptance apply X to the control. If 4 C_0 acquisitions do not give C_0 accepted qubits, ABORT. In the ideal run accepted
labels are i.i.d. uniform on [0, 2^dn), each copy is accepted with probability 2^dn/N > 1/2, so by Hoeffding the abort has
probability at most exp(-C_0/2). The qubit has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

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
- If wd >= 2: run BATCH with B = wd - 1 and C_0 leaf qubits. Take the first root with W odd, and measure it in X. By (9.1) it is
  (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2, which gives rem mod 2 exactly. Release the other roots. If no root
  has W odd, set the bit to 0.

By (10.3), and independence of distinct roots given G, each such level misses with probability at most 2^-K, even if s1 was wrong.
Set bit g of s2. In the ideal run with s1 correct and no miss, every bit is correct. Output (s1 + M s2) mod N.

## 13. The complete algorithm and its success probability

Finite branch (n < 2^40). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and
reject cand at the first minus outcome. Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For
cand != s the two data branches are orthogonal, so each outcome is uniform. A union bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10.
All resources on this branch are bounded by an absolute constant.

Main branch (n >= 2^40). Compute a2, M, dn, J, K, the schedule, Y, and all allocations; put

    Qcap = 4 n C_0 + K.

Run Section 11 and then Section 12. Any ABORT stops the algorithm, releases everything and outputs 0. Since J + 1 + a2 <= log2 M + a2
= log2 N <= n, there are at most n batches, each using at most 4 C_0 acquisitions, plus at most K per wd = 1 level, of which there is
at most one. So Q <= Qcap on every branch, without any counter being needed. LE is sized by this Qcap, which is computed before h_e.

Success. In the ideal run the failure events are: a pool exhaustion, at most n * 2^-10/n = 2^-10 (Lemma 9.1); an FW-stage abort, at most
n (2 ell exp(-2^m/(10 ell^2 w^2)) + ell w C_0 2^(-3r)) (Lemma 9.2), and a supplier abort, at most n exp(-C_0/2), both below 2^-40
because m >= 600000, w = 2^28, C_0 <= 2^(2r-1) and ell, n are
at most polynomial in r; a decoder error, at most 2^-20 (Lemma 11.1); a 2-adic miss, at most n 2^-K <= 2^-40. Adding the LE coupling (5.1):

    Pr[output = s] >= 1 - 2^-10 - 2^-40 - 2^-40 - 2^-20 - 2^-40 - 2^-10 >= 1 - 2^-8 > 1 - 2^-7 > 2/3.

The finite branch succeeds with probability at least 1 - 2^-10. These are additive couplings; there is no conditioning on favorable
labels or outcomes.

## 14. Resources on every main-branch execution

Throughout, K = O(sqrt n), dl, m, ell = O(sqrt n), C_ell = O(n^2 2^m) and, writing PP = RHO^ell 2^m, C_0 = O(n^2 PP) by (8.2). Also
sum_i C_i <= 2 C_0, since C_i >= RHO C_(i+1) >= 2 C_(i+1). All fixed loops, caps and aborts below hold on every branch.

Q. Q <= Qcap = O(n^3 PP).

S_Q. The pool holds at most C_0 qubits. An FW adds at most c_F ancillas, an absolute constant, all released in |0> (Lemma 7.1(c)), and
PREP uses O(1) fresh qubits per try, reset after it. The depth-first stack holds at most two index registers per level, at most 2 (m+1)(dl+m) = O(n) qubits. A merge adds O(sqrt n) qubits. LE and transforms use O(n), reset
between uses. So S_Q = O(C_0 + n) = O(n^2 PP).

S_C. Pool tables and sort scratch use O(n C_0) bits. Depth-first tables: at most three tables per level, each of 2^(lam_i) fields of
3n bits, plus merge scratch O((L + L') n). Since lam_i <= dl + m - 1 and these geometric sizes sum, this is O(n 2^(dl+m)). The decoder stores
K triples and K residues of O(n) bits. LE uses O(n) bits. So S_C = O(n^3 PP + n 2^(dl+m)). These are fixed allocations.

Core steps, per batch.
- Acquisitions: at most 4 C_0, each O(n^2) for Mult plus O(n^(5/2)) for LE (log2 Qcap = O(sqrt n) by (8.3), so h_e = O(sqrt n)): O(n^(5/2) C_0).
- FW stage, Section 7: at level i the cost is O((C_i + rounds E_i) n log C_i) with E_i <= C_i/(4 w ell) and rounds = q (Y + 1), so
  rounds E_i <= (Y + 1) C_i/(8 ell) <= C_i as Y + 1 <= 2r + 1 <= 8 ell, and log C_i <= Y = O(sqrt n). So a level costs O(n^(3/2) C_i),
  and the stage O(n^(3/2) C_0), using sum_i C_i <= 2 C_0.
- Tree: there are at most C_ell/dl LEAF calls at O(n 2^dl) each. A merge producing level i+1 consumes 2^(i+1) dl pool qubits that no other merge at that level uses,
  since inputs of a failed merge are discarded. So there are at most C_ell/(2^(i+1) dl) of them, each O(n 2^(dl+i)) by Section 6. Each level thus costs
  O(n C_ell 2^dl/dl), and all m+1 levels cost O(m n C_ell 2^dl/dl) = O(n C_ell 2^dl) = O(n^3 2^(m+dl)).
- Decoder per stage: at most 2^(Y+8) candidates, K residues each, O(n) bits per addition: O(K n 2^Y) = O(n^(3/2) C_0).

Over at most n batches, plus poly(n) setup (parameters, CRT, Mult constants, the table of Section 4, shift values, initial residues), core steps total
O(n^(7/2) C_0 + n^4 2^(m+dl)) + poly(n). Every loop is either fixed-length or consumes pool qubits or acquisitions, so every branch terminates.

T. By (8.3), log2(S_C + S_Q + 2) = O(sqrt n). By (2.1),

    T = O(n^4 C_0 + n^(9/2) 2^(m+dl) + n Q) = O(n^6 PP + n^(9/2) 2^(m+dl)).

Exponents. Since RHO^ell <= 2^(HI ell), r <= sqrt n + 1 and (8.5), with eP = 54999/50000 and eT = 62899/50000,

    log2 PP <= HI (23547 r/50000 + 1) + 62899 r/100000 + 1 <= eP r + HI + 1 <= eP sqrt n + 3.11,
    m + dl <= (62899/100000 + 62899/100000) r + 2 = eT r + 2 <= eT sqrt n + 3.26.

The pool exponent eP = 1.09998 is below the tree exponent eT = 1.25798, so the n^6 PP and n^3 PP terms of T and S_C
are O(n^6 2^(eT sqrt n)) and O(n^3 2^(eT sqrt n)), and jointly, on every branch of the main branch,

    T = O(n^6 2^(eT sqrt n)),  S_C = O(n^3 2^(eT sqrt n)),  S_Q = O(n^2 2^(eP sqrt n)),  Q = O(n^3 2^(eP sqrt n)).

## 15. Exact growth indices and declared envelopes

Since 629/500 - 62899/50000 = 1/50000, 11/10 - 54999/50000 = 1/50000 and n^6 2^(-(1/50000) sqrt n) is bounded over n >= 1, the bounds of
Section 14 give T, S_C = O(2^(aT sqrt n)) and S_Q, Q = O(2^(aP sqrt n)), with aT = 629/500 and aP = 11/10. The finite branch contributes
only an absolute constant. The declared envelopes are B_T(n) = B_C(n) = 2^((629/500) sqrt n) and B_Q(n) = B_samples(n) = 2^((11/10) sqrt n).
For B(n) = 2^(a sqrt n) with a = 629/500 or 11/10, log2 B = a sqrt n, log2 log2 B = (1/2) log2 n + log2 a, and
g(B) = lim log2 log2 max(4, B(n)) / log2 n = 1/2 exactly. The index holds for these fixed exact coefficients; it does not rely on a
guessed constant. The structured objects in submission.json are exactly these envelopes.

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does not assert that robustness is impossible.

## 17. Scope and limitations

- This does not reach the research goal 2^(O(n^(1/3))); the time growth index is 1/2, as in HPC-127. The improvement is in the
  coefficients of sqrt n: this is a tradeoff point of F-LIMIT, with S_Q and Q at 11/10 and T and S_C at 629/500. At pool exponent
  q the construction approaches tree exponent 2 sqrt(1 - q^2/2) as w grows (motivation only; 1.25698 at q = 1.1).
- S_Q, S_C and Q are 2^(Theta(sqrt n)), as in HPC-127. The result is a different tradeoff, not a dominance claim over rows with
  smaller memory.
- The group size w = 2^28, the threshold n >= 2^40 and all constants (the gate count c_F of FW in particular) are unoptimized absolute
  constants.
