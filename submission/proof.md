# SWF-13377: streaming pairing under a sample budget, T = O(2^((13377/10000) sqrt n)), Q = O(2^((13/10) sqrt n)), S_Q = O(2^((1/2) sqrt n))

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single algorithm SWF-13377 below receives N in binary and fresh
independent copies of rho_s, and outputs the entire s with unconditional probability at least 1 - 2^-8 > 2/3. On EVERY execution branch
(every failure, discard and abort included) it satisfies jointly

    T = O(2^((13377/10000) sqrt n)),  S_C = O(2^((13377/10000) sqrt n)),  S_Q = O(2^((1/2) sqrt n)),  Q = O(2^((13/10) sqrt n)).

All constants are absolute. Each of the four envelopes has growth index exactly 1/2 (Section 15). The fifth claim is the clean-input
tolerance 0 (Section 16). The sharper main-branch bounds, from which these follow, are in Section 14. The envelope coefficients are fixed
exact rationals; no hidden constant sits inside an exponent.

Notation:
- dn = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known nonnegative integer. log means log2 unless stated otherwise.

Main-branch parameters, computed by exact integer arithmetic for n >= 2^48:

    r = ceil(sqrt n),  ell = ceil(4614 r/10000),  w = floor(999 r/2000),
    m = ceil(8379 r/10000),  dl = ceil(4997 r/10000),  kappa = ceil(log2 m) + 1.

So there are ell streaming FW levels, each with at most (W0-1)*2^w slot qubits and O(W0) ready/pending qubits, where W0=2^28, a collimation tree of depth m, and leaf tables built from dl
qubits. Since r >= 2^24 these satisfy ell >= 2, dl >= kappa + 1 and 2^kappa >= 2m.

## 1. Provenance and change

The exact fixed-size instrument FW and its yield analysis come directly from
qzv's F-LIMIT-BANK, submission a9a7dcac-3918-44e8-84db-bda6b1dcebdd,
commit7bfa4eb939c9424367f046da302ce7e673abda8c, virtual.md Section7.1.
That section is reproduced below with its group-size symbol changed to W0.
No basis-bank memory wrapper is used here; all label records are ordinary
counted classical bits. The source's exact numeric gate bound is not needed:
we use only a finite, absolute gate/scratch constant for its fixed circuit.

The streaming architecture, source extractor, collimation tree and decoders
come from qzv's SPQ-1408, submission99b483c1-eed5-4398-8459-df749d65d390,
commit66e63c7d853e227b43051c5415b4629408d19f1b. The immediate development
uses my SPQ-14021 (540fc9a7-7a06-4f13-b725-a95c612ba2d0) and STRIAD-13938
(two-slot streaming development; its published identifier will be added before submission).
STRIAD directly reproduced qzv's TRIAD-125
(f5b375dd-1e5c-4728-95dc-b855b2dc5827), whose product-state streaming
principle is generalized here. Earlier provenance is credited through those
sources: SPC-127, HPC-127, SPC-138, CS1, CYC1 and Kuperberg's algorithms.
No previous acceptance or comparison result is a mathematical premise.

The new controller stores W0-1 inputs per key and bounds a READY output queue
and a PENDING recycled input. These queues permit multiple independent good
outputs from one instrument without storing an unbounded batch. The new
stopped-flow inequality includes the READY correction explicitly. Section8
proves that its residue terms fit the acquisition cap; Section13 separately
charges and bounds every capped ancilla-preparation failure.
The configuration claims no instrument invention, optimality or cube-root
algorithm. Its joint time/space/sample theorem is proved for this one stream.

## 2. Model and counting conventions

A CORE STEP is one of: a NOT/CNOT/Toffoli/H/S/S^dagger gate; a computational-basis
single-qubit measurement or reset; a Boolean operation on at most three classical bits; a
classical bit read or write. Toffoli has an exact constant-size Clifford+T decomposition.
Integers are bit strings; an L-bit addition, comparison or copy costs O(L) core steps.
Generating a gate costs O(1) core steps. Each core step additionally pays its address,
ceil(log2(Mem+2)) bit operations, where Mem <= S_C + S_Q is the number of allocated bits and
qubits. Gates on slot qubits are classically addressed through this charge; there is no
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

IDEAL runs. The LABEL-IDEAL run executes this same physical SWF-13377
algorithm, including capped PREP, but replaces every LE output by its
latent k. Coupling to the actual run costs at most2^-10 by(5.1).
For the stopped-flow and decoder analyses also use a FULLY IDEAL run
that supplies every FW uniform ancilla exactly. It is coupled to the
LABEL-IDEAL run until the first PREP abort, whose separate probability
is bounded in Section13. Below, ideal run means FULLY IDEAL unless
otherwise specified. All resource bounds concern actual branches and
follow directly from caps and fixed allocations.

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

## 7. Fixed-size FW in a streaming controller

Fix W0=2^28 and q=W0/2=2^27. These are absolute constants, independent of N.
The symbol w of Section0 remains the growing per-level key width; it is not W0.
A labeled qubit has table(t0,t1), difference Del=t1-t0, and the usual
equal-magnitude two-entry phase vector for the batch parameter th.
Collimation to p means Del=0 mod2^p. Conditional on latent labels and all
past outcomes, all live qubits are product phase vectors on disjoint
source-leaf sets, in tensor product with the tree. The supplier establishes
this invariant. Lemma7.1 below preserves it, including for multiple outputs.
In PREP below, N is a local register-size parameter, not the input modulus.

### 7.1 The instrument FW

Uniform registers. For an integer N with 3 <= N <= W0 - 1 put j_N = ceil(log2 N) <= 28 and
U_N = N^(-1/2) sum_(v<N) |v>, a state of j_N qubits. PREP(N): up to 3r times (r from Section 0), put
j_N fresh qubits in |0>, apply H to each, XOR the flag [v < N] into a fresh qubit (a comparison with a
constant, computed cleanly with O(1) Toffoli/CNOT/NOT gates), measure the flag and reset it; if it was
1, stop: the register R_N holds exactly U_N, because measuring the flag projects the uniform state onto
v < N. Otherwise measure and reset the j_N qubits and try again. If all 3r tries fail, ABORT. Each try
touches only its fresh qubits and succeeds with probability N/2^(j_N) > 1/2, independently of
everything else (probability 1 if N is a power of 2), so PREP(N) aborts with probability below 2^(-3r).

Input: labeled qubits A_0, ..., A_(W0-1) on disjoint qubits, with tables (t0^i, t1^i), and x in {0,1}^W0
for their computational-basis value. Write h = |x|, put mu = 1 if h <= q and mu = 0 otherwise, let
M = {i : x_i = mu} = {m_0 < ... < m_(u-1)}, so u = |M| = min(h, W0 - h), and let
J = {i : x_i != mu} = {j_0 < ... < j_(W0-1-u)}. CELLS are subsets of {0,1}^W0:
- PAIR CELLS P_ab = {x : x_a != x_b} for 0 <= a < b < W0 (the other W0 - 2 qubits unconstrained);
- MATCHING CELLS: for 1 <= u' <= q - 1, u' disjoint pairs {a_k, b_k} and the set Bl of the other W0 - 2u'
  positions, Q = {x : x_(a_k) != x_(b_k) for all k, and x is constant on Bl};
- Ev = {0^W0, 1^W0}.
Weights: y = 1/q^2 for a pair cell, y = (q - u')^2 (W0 - 2u')!/(q^2 (W0 - u')!) for a matching cell with
u' pairs, and y = 1 for Ev.

Incidence. (I1) If u >= 1, x lies in P_ab iff exactly one of a, b is in M, so in exactly u(W0 - u) pair
cells. (I2) If x lies in a matching cell Q with u' pairs, let z0 be its value on Bl; x takes the value
z0 on u' + (W0 - 2u') = W0 - u' >= q + 1 positions and 1 - z0 on u' <= q - 1, so 1 - z0 = mu, u = u', and M
consists of one element of each pair. Conversely, if 1 <= u <= q - 1, every injection phi : M -> J gives
the matching cell with pairs {m, phi(m)} and Bl = J \ phi(M), which contains x (x = mu on M and 1 - mu
on J). So the matching cells containing x correspond bijectively to these injections; there are
(W0 - u)!/(W0 - 2u)! of them if 1 <= u <= q - 1 and none otherwise. (I3) Ev contains x iff u = 0, and then x
lies in no other cell. Since u(W0 - u) + (q - u)^2 = q^2, the total weight of the cells containing x is 1
for every x. FW realizes these weights exactly as follows.

Cell register. P has W0 fields of 29 qubits; the code of a cell C is p(C) with p_i = the other element of
i's pair if i is in a pair of C, p_i = W0 if i is unconstrained (pair cells), and p_i = W0 + 1 if i is in Bl
(matching cells) or anywhere (Ev). The code is a function of the cell alone.

Two classical maps. Let t = q a + b with a, b in [0, q), and let R = (R_N) be values R_N in [0, N).
cell(x, t, R): if u = 0, return p(Ev). If a < u, return p(P_(m_a j_b)). If a >= u and b < u, return
  p(P_(m_b j_(q+a-u))). Otherwise (a, b >= u, so u <= q - 1): let L be the list j_0, ..., j_(W0-1-u); for
  k = 0, ..., u-1, remove from L its element of 0-based index R_(W0-u-k) (valid, since L has W0 - u - k
  elements before this removal) and call it pt_k; return the code of the matching cell with pairs
  {m_k, pt_k} and Bl = the rest of L.
back(x, p): if p codes a pair cell {c, d}, c < d, put c' = c if c is in M and c' = d otherwise, let d'
  be the other one, i the rank of c' in M and k the rank of d' in J (0-based, increasing; 0 if absent);
  return t = q i + k if k < q and t = q(k - q + u) + i if k >= q, and all R_N = 0. If p codes a matching
  cell, put L = (j_0, ..., j_(W0-1-u)) and, for k = 0, ..., u-1, let v_k be the index in L of pt = p_(m_k)
  (0 if absent) and remove pt from L; return t = 0, R_(W0-u-k) = v_k for k < u and R_N = 0 otherwise.
  Otherwise return all zeros.

(B1) Let u >= 1. Case a < u gives the pair (m_i, j_k) with (i, k) = (a, b), k < q; case a >= u > b gives
(i, k) = (b, q + a - u) with q <= k < W0 - u, since u <= a < q. Together these qu + (q - u)u = u(W0 - u)
tickets map bijectively onto [0,u) x [0,W0-u), that is onto the pair cells containing x by (I1), and back
returns t. The remaining (q - u)^2 tickets form D_u = {q a + b : a, b >= u}.
(B2) Let 1 <= u <= q - 1 and t in D_u. Removing the elements of indices v_0, ..., v_(u-1) from a list in
turn is a bijection from [0,W0-u) x [0,W0-u-1) x ... x [0,W0-2u+1) onto the sequences (pt_0, ..., pt_(u-1)) of
distinct elements of J, the inverse being v_k = index of pt_k after the earlier removals. So by (I2) the
values of R_N for N in S_u = {W0-u, ..., W0-2u+1} map bijectively onto the matching cells containing x
(pt_k is the partner of m_k), the other registers are not read, and back returns those values.

Circuit. Ancillas, all fresh |0>: a 54-qubit ticket register T, the registers R_3, ..., R_(W0-1)
(together the register R, at most 28 W0 qubits), the cell register P, and scratch.
1. Apply H to each qubit of T. Run PREP(N) for N = 3, ..., W0 - 1.
2. XOR cell(x, t, R) into P.
3. XOR back(x, P) into (T, R).
4. Measure P, obtaining the code of a cell C, and reset P. If C = Ev, apply H to each qubit of T. If C
   is a matching cell, measure T and reset it. Measure and reset every R_N.
5. Post-processing. For each pair {a, b} of C with a < b: apply CNOT with A_a as control and A_b as
   target; A_b is then exactly |1>; apply NOT to it and release it. A_a is a GOOD output with table
   (t0^a + t1^b, t1^a + t0^b). If C has a block Bl = {c_0 < c_1 < ...} (Bl = all of [0,W0) for Ev),
   apply CNOT A_(c_0) -> A_(c_i) for each i >= 1; these are then exactly |0>; release them. A_(c_0) is
   the RECYCLED output with table (sum_(c in Bl) t0^c, sum_(c in Bl) t1^c). The qubits unconstrained by
   C (W0 - 2 of them for a pair cell) are RETURNED with their tables unchanged.
So a pair cell yields one good output and returns W0 - 2 qubits; a matching cell with u pairs yields u
good outputs and one recycled output; Ev yields one recycled output.

Gates. Steps 2 and 3 XOR a fixed Boolean function of the qubits of x, T, R and P into a register that is
not among its inputs. Each function is a fixed classical program: popcount, prefix counts, ranks, and at
most q selections without replacement among W0 positions, so a finite Boolean circuit whose size depends on W0 only. Compute it with Toffoli (AND), CNOT (XOR) and NOT on fresh scratch, CNOT the
result into the target, and uncompute in reverse order, as for modular addition in Section 3. So FW
uses at most c_F NOT/CNOT/Toffoli/H gates, measurements and ancilla qubits, where c_F is an absolute constant, plus the PREP tries (at most 3r of O(1) core steps for each of the W0 - 3 registers)
and O(W0 n) classical steps for the table additions. No rotation synthesis occurs: every amplitude is
produced by H gates and by the projections of PREP.

Lemma 7.1 (FW). Assume every PREP succeeds. (a) and (b) assume that, conditional on the past,
A_0, ..., A_(W0-1) are in the product state psi = (x)_i 2^(-1/2) (exp(2 pi i t0^i th)|0> +
exp(2 pi i t1^i th)|1>), in tensor product with the rest of the system, which is in an arbitrary state.
(a) The measured cell C has probability y_C |C|/2^W0: 2/W0^2 for each pair cell, so (W0 - 1)/W0 in total;
    pi_u = 2 C(W0,u) (q - u)^2/(q^2 2^W0) in total over the matching cells with u pairs, each having the same
    probability; and 2^(1-W0) for Ev. Given C, the other values measured in step 4 are independent of the
    labels and of th: if C is a matching cell with u pairs, T is uniform on D_u and R_N = 0 for N in S_u;
    every other R_N is uniform on [0, N). All this holds whatever the labels, th and the past.
(b) Given a pair cell P_ab, a < b, the good output is exactly the phase vector with table
    (t0^a + t1^b, t1^a + t0^b), label difference Del_a - Del_b, and the W0 - 2 returned qubits are exactly
    in their input states. Given a matching cell, the good output of each pair {a, b}, a < b, is
    exactly the phase vector with table (t0^a + t1^b, t1^a + t0^b), and the recycled output is exactly
    the phase vector with the stated block table, label difference sum_(c in Bl) Del_c; given Ev, the
    recycled output carries the sum of the W0 tables. In each case the outputs are in tensor product
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
For the product input, |R_x> = 2^(-W0/2) exp(2 pi i phi(x)) |R> with phi(x) = th sum_i t_(x_i)^i, so
Pr[C] = y_C ||Pi_C psi||^2 = y_C |C|/2^W0, using only the moduli; |P_ab| = 2^(W0-1), |Q| = 2^(u+1) and
|Ev| = 2; and the junk factors are fixed states. This is (a): the matching cells with u pairs all have
the same weight and size, and summing y_C |C|/2^W0 over them counts, by (I2), each of the 2 C(W0,u) points
of weight u or W0 - u with total weight (q - u)^2/q^2.
For (b): P_ab = {x_a != x_b} x {0,1}^(W0-2), so Pi_(P_ab) psi is
[2^(-1)(exp(2 pi i (t0^a + t1^b) th)|0_a 1_b> + exp(2 pi i (t1^a + t0^b) th)|1_a 0_b>)] (x) (the other
W0 - 2 input states), and CNOT A_a -> A_b maps |0 1> to |0 1> and |1 0> to |1 1>. A matching cell is the
product over its pairs of {x_a != x_b} and of {x constant on Bl}, so Pi_Q psi is the product of the pair
factors above and of 2^(-|Bl|/2)(exp(2 pi i th sum_Bl t0^c)|0...0> + exp(2 pi i th sum_Bl t1^c)|1...1>),
and the CNOTs from A_(c_0) map |y...y> to |y 0...0>. Ev is the case Bl = [0,W0). QED.

Every table produced is a sum of input tables over disjoint inputs: a good output's entry alpha is the
sum of entry alpha of A_a and entry 1 - alpha of A_b, for its pair {a, b}; a recycled output's entry
alpha is the sum of entry alpha over its block; a returned qubit keeps its table. By (b), (P) is
preserved. Only the TYPE of an outcome matters below: (gamma, rho) = (1, 2) for a pair cell, (u, W0 - 1)
for a matching cell with u pairs, (0, W0 - 1) for Ev, where gamma is the number of good outputs and rho the
number of qubits that leave the live list (W0 inputs, W0 - 2 or 1 put back). By (a) the type has the law

    Pr[(1,2)] = (W0-1)/W0,   Pr[(u,W0-1)] = pi_u (1 <= u <= q - 1),   Pr[(0,W0-1)] = 2^(1-W0).          (7.2)

In every type 2 gamma <= rho.

Lemma K (yield ratio). Let gbar = E[gamma], rhobar = E[rho] under (7.2), and b = C(W0, q)/2^W0. Then
rhobar = 3(W0 - 1)/W0, gbar = 3/2 - 1/W0 - b, and so rhobar/gbar = 6(W0 - 1)/(3W0 - 2 - 2W0 b). Moreover
b <= (3q + 1)^(-1/2), and with s = 20066, s^2 = 402644356 <= 402653185 = 3q + 1, so b <= 1/s and

    gbar/rhobar >= 8192/16385,   that is rhobar/gbar <= RHO := 16385/8192 = 2 + 2^-13.        (7.4)

Also 1 <= gbar <= 3/2.

Proof. Under (7.2), the type is a function of h = |x| for x uniform on {0,1}^W0 (Lemma 7.1(a) is the
average over x of the cell weights at x), so h ~ Bin(W0, 1/2). Given h with u = min(h, W0 - h) >= 1, the
pair type has probability u(W0 - u)/q^2 = 4h(W0 - h)/W0^2 and the matching type probability (q - u)^2/q^2.
Since E[h(W0 - h)] = (W0^2 - W0)/4, the pair type has probability (W0 - 1)/W0, and the other types 1/W0; so
rhobar = 2(W0 - 1)/W0 + (W0 - 1)/W0. Put D = h - q, so u = q - |D| and (q - u)^2/q^2 = D^2/q^2. Then
gbar = (W0 - 1)/W0 + E[(D^2/q^2)(q - |D|)] = (W0 - 1)/W0 + E[D^2]/q - E|D|^3/q^2, with E[D^2] = W0/4 = q/2.
For j >= 1, j C(2q, q+j) = q (C(2q-1, q+j-1) - C(2q-1, q+j)), so summing by parts,
sum_(j>=1) j^3 C(2q, q+j) = q sum_(j>=1) (2j - 1) C(2q-1, q+j-1). With N' = 2q - 1 and k = q + j - 1 this is
q sum_(k>=q) (2k - N') C(N', k) = q N' C(2q-2, q-1), because k C(N', k) = N' C(N'-1, k-1),
sum_(k>=q) C(N', k) = 2^(N'-1) and sum_(i>=q-1) C(2q-2, i) = (4^(q-1) + C(2q-2, q-1))/2. Since
C(2q, q) = (2(2q-1)/q) C(2q-2, q-1), this equals q^2 C(2q, q)/2, and by symmetry E|D|^3 = q^2 b. Hence
gbar = (W0 - 1)/W0 + 1/2 - b. For the bound, b_1 = 1/2 and b_(k+1) = b_k (2k+1)/(2k+2) for
b_k = C(2k, k)/4^k, and (2k+1)^2 (3k+4) = (2k+2)^2 (3k+1) - k, so b_k^2 (3k+1) <= 1 for all k by induction.
Then gbar/rhobar >= (3/2 - 1/W0 - 1/s) W0/(3(W0 - 1)) = (3W0 s - 2s - 2W0)/(6s(W0 - 1)), and (7.4) is the integer
inequality 16385 (3W0 s - 2s - 2W0) >= 8192 * 6 s (W0 - 1): the difference of its sides is
(3s - 32770) W0 + 16382 s = 27428 * 2^28 + 16382 * 20066 > 0. Finally 3/2 >= gbar >= 3/2 - 1/W0 - 1/s >= 1. QED.

### 7.2 READY, PENDING and bounded slots

At each level i<ell allocate SLOT_i with E_i=2^pb_i keys and W0-1 places
per key; READY_i with at most q good output qubits; and PENDING_i with
at most one recycled same-level input. Initially all are empty. The key is

    key_i(item)=floor((Del mod2^(pp_i+pb_i))/2^pp_i).

NEXT(0) requests a leaf from the supplier. NEXT(i+1) executes at level i:

    if READY_i nonempty: remove and return its first qubit
    item = remove PENDING_i if nonempty, else NEXT(i)
    loop:
        k=key_i(item)
        if SLOT_i[k] has fewer than W0-1 qubits:
            append item there; item=NEXT(i); continue
        group=(SLOT_i[k] in arrival order, item)
        clear SLOT_i[k]
        prepare ancillas and run FW on the ordered group
        if PREP aborts: ABORT the whole algorithm
        if pair cell:
            put the W0-2 untouched inputs back into SLOT_i[k]
            append the single good output to READY_i
        if matching cell:
            append all good outputs, ordered by increasing pair endpoint,
                to READY_i
            put the single recycled output into PENDING_i
        if Ev:
            item=the recycled output; continue
        remove and return the first READY_i qubit

Before a new group can be formed, READY_i has been drained and PENDING_i
has been removed. Thus at most one group's outputs are ever in READY_i;
its size is at most q. A returned untouched input has the original key k,
so W0-2 such inputs fit in the cleared slot. A recycled sum may change key:
it is deliberately deferred in PENDING_i, never inserted blindly into a
possibly full slot. An Ev sum is reprocessed by the loop with its new key.
A frame waiting on a lower-level NEXT stored its active input first.

Same-key inputs have equal differences mod2^(pp_i+pb_i), so every good
pair difference is collimated to pp_(i+1). Recycled sums remain collimated
to pp_i. Returned inputs are unchanged. All key and grouping decisions
read only low bits below the prescribed positions. By Lemma7.1(b), good
outputs, returned inputs and recycled outputs are product phase vectors
on disjoint source-leaf sets. Their separate queues preserve this property.

The streaming data allocation is at most (W0-1)sum_iE_i+O(W0 ell), with
additional source/data, tree and FW scratch counted in Section14. Use a
fixed slot array and an indexed classical free-handle stack. Each handle
has O(n) bits; allocation/release requires one push/pop and O(n) core work,
not a linear search. Queue and slot bookkeeping also costs O(n) per qubit.
The constant factor W0 is absolute and is charged, not taken to be one.

### 7.3 Stopped flow including queued outputs

Use logical checking points between completed instruments and source or
demand acquisitions. Let A_i be arrivals from NEXT(i), d_j the net number
of inputs removed from level i by its j-th completed group, gamma_j its
number of produced good outputs, L_i the same-level inputs in its slots,
pending place and possible active item, and R_i the READY occupancy.
READY qubits are excluded from L_i. Then deterministically

    A_i=sum_j d_j+L_i, L_i<=(W0-1)E_i+1,
    sum_j gamma_j=A_(i+1)+R_i, 0<=R_i<=q.                 (7.5)

Here d_j=2 for pair cells and W0-1 for matching/Ev cells. Lemma7.1 and
LemmaK imply E[d_j-RHO gamma_j|past]<=0 for RHO=16385/8192.
The ideal run in this argument supplies exact uniform ancillas; its
coupling to the capped physical PREP is bounded in Section13. At any
bounded stopping point optional stopping yields

    E[A_i] <= RHO E[A_(i+1)]+(W0-1)E_i+1+RHO q.           (7.6)

No uniform-key or independence-of-recycled-label assumption is used.
Also 2gamma_j<=d_j on every branch. Hence
2A_(i+1)<=sum_j d_j<=A_i and sum_iA_i<=2A_0. Every completed group
has d_j>=2, so at most A_0 groups complete across all levels. At most
one additional group can start and abort in PREP. The finite source cap
therefore bounds all stopping times used in(7.6).

Without caps each NEXT terminates almost surely: if inputs continue,
finite slots force further groups; each group has a positive constant
chance of producing a good output, independent of the past. A pending
or READY qubit never blocks progress. The bounded-stop argument below,
not an assumed expected-time execution, supplies the resource theorem.

Each group costs O(n) core steps: W0 is fixed, the inherited finite circuit
has absolute cost c_F, PREP has at most3rW tries, and table updates cost
O(W0 n), with r=O(sqrt n). Stores and READY deliveries are charged to an
arrival or group. Conservation bounds the entire streaming work by
O(nA_0), plus O(sum_iE_i) occupancy initialization, with absolute constants.

## 8. Schedule, capacity and explicit residue budget

Write RHO=16385/8192. Since ln2>2/3 (the first three positive terms
of sum_(k>=1)1/(k2^k) sum to2/3) and ln(1+x)<x for x>0,

    1<log2 RHO=1+log2(1+2^-14)<1+3/32768<10001/10000.

Use Dbar=3K2^mdl, Dcap=2^12nDbar,
Ccap=ceil(2^13n RHO^ell Dbar), Y=ceil(log2Ccap).
All parameters are computed by exact integer arithmetic with O(sqrt n)
bit words. For r>=2^24, K<=3*2^13r, dl<=r, n<=r², so

    log2Ccap <=[(10001/10000)(4614/10000)+8379/10000]r+4log2r+34
              =(64967307/50000000)r+4log2r+34
              <1.3r+4log2r+34<=2r-1.                        (8.1)

Thus Y<=2r<=n and2^Y<=2Ccap. The last inequality holds at2^24
and thereafter because .7r-4log2r-35 is increasing.
Use

    pbmax_i=min(w,m+ell-i),
    lam_i=dl+i for i<m, lam_m=1,
    tbmax_i=dl+i-kappa-1 for i<m-1,
    tbmax_(m-1)=2(dl+m-1)-kappa-1.

Every tree capacity gives b_i+lam_(i+1)-2lam_i<=-kappa. (8.2)
Since RHO>2,

    RHO^i 2^pbmax_i <= RHO^ell 2^m.                      (8.3)

Here w<m, so pbmax_i=w exactly. Put alpha=.4614, beta=.8379,
delta=.4997, omega_0=.4995 (these are exact rationals). Then

    alpha omega_0+beta delta+beta²/2
      =200041227/200000000 >1+1/10000.

The exact tree capacity is m dl+m²/2+dl+m/2-1-m(kappa+1).
Slot capacity is ell*w>=alpha omega_0r²-ell. For r>=2^24,
ell<=.462r,m<=.839r,kappa+1<=log2r+3. Losses are therefore at most
r(.839log2r+2.979)<r(log2r+4)<r²/10000. The endpoint and derivative
checks are immediate from r>=2^24 and ln2>2/3. All capacities are
nonnegative because dl>=kappa+1. Total capacity exceeds r²>=n.

Allocate exactly B<=n bits greedily to pb_0,...,pb_(ell-1), then
tb_(m-1),...,tb_0, each capped by its maximum. Put pp_0=0,
pp_(i+1)=pp_i+pb_i,tp_0=pp_ell,tp_(i+1)=tp_i+tb_i. Then tp_m=B;
all key/merge readings are strictly belowB.

For the additional stopped-flow residues in(7.6), (8.3) and RHO>2 give

    sum_(i<ell)RHO^i[(W0-1)E_i+1+RHO q]
      <=RHO^ell[(W0-1)ell2^m+(1+RHO q)/(RHO-1)]
      <=RHO^ell[(W0-1)ell2^m+1+3q]
      <=RHO^ell Dbar.                                    (8.4)

Indeed W0=2^28<=16r,ell<r/2,1+3q<=2W0<=32r, so the bracket is at
most40r²2^m. In contrast K>=2^14r and dl>=.4997r yield
Dbar>24000r²2^m. This supplies the residue budget uniformly, including
the READY correction; it is not omitted as a lower-order heuristic.

## 9. BATCH(supplier, B)

Input: a supplier of LEAF QUBITS: positive qubits with phase exp(2 pi i k th) for a fixed real th and a known label k, where in the ideal
run the labels are independent and uniform on [0, 2^(B+1)). Output: K roots, or ABORT. A batch starts with empty slot tables and a counter of
source acquisitions; if an acquisition would exceed Ccap, the batch ABORTs. At its end, slot qubits are measured and released.

TREE. VEC(0) = LEAF: request dl qubits by calling NEXT(ell) dl times, counting each in a counter D; if D would exceed Dcap, ABORT. These qubits form
the index register, bit j = qubit j. With tables (t0_j, t1_j), build lab[0] = sum_j t0_j and lab[x + 2^j] = lab[x] + t1_j - t0_j for x < 2^j. The
table has length 2^dl, is exactly the tensor product state in the ideal run, and is collimated to tp_0 because every difference is 0 mod 2^(tp_0).
VEC(i), i >= 1: repeat X1 = VEC(i-1), X2 = VEC(i-1), out = MERGE(X1, X2; tp_(i-1), tb_(i-1), lam_i), until out != FAIL; return out. A root is VEC(m),
evaluated depth-first. Run it K times.

Root. VEC(m) is a two-entry table with lab[0] = lab[1] mod 2^B, so its ideal state is, up to global phase,

    (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2,   W = (lab[1] - lab[0])/2^B, a known integer.     (9.1)

Label bound. Each leaf qubit enters a table entry at most once, and a batch has at most Ccap leaves. So every label in the batch is a sum of at most Ccap
leaf labels below 2^(B+1). Thus every label is below 2^(Y+n+1), which fits in 3n bits by Y <= n, and

    |W| <= 2 Ccap <= 2^(Y+1).                                                       (9.2)

Lemma 9.1 (no abort). Suppose each supplied acquisition yields a leaf qubit independently with probability at least 1/2, given the past. In the ideal run a
batch ABORTs with probability at most 2^-12/n + 2^-11/n.

Proof. Work in the ideal run with exact labels and exact uniform FW
ancillas. In the unbounded virtual tree every NEXT terminates almost surely.
The distribution-free merge failure bound gives conditional failure at
most2^-kappa. With tt=2^kappa/(2^kappa-1), a root's expected delivered
leaf demand is at most(2tt)^m dl, and tt^m<=e<3 by2^kappa>=2m.
For K roots, E[D_inf]<=Dbar. Thus Pr[D_inf>Dcap]<=2^-12/n.

Stop this uncapped process when the batch finishes or its source acquisition
counter reaches Ccap. All group counts are bounded, and A_ell<=D_inf.
Iterating(7.6) and using(8.4) gives E[A_0]<=2RHO^ellDbar.
The supplier accepts each acquisition with conditional probability at least1/2;
its bounded stopped sum therefore gives expected acquisitions at most
2E[A_0]<=4RHO^ellDbar. Markov against Ccap yields at most2^-11/n.
The capped run agrees with this process until a cap triggers. PREP aborts
are handled by a separate coupling in Section13, not by conditioning the
stopped argument on a favorable PREP event. QED.

## 10. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and tau_j in {0,1}. Since k_j is uniform on
[0, 2^(B+1)), low_j and tau_j are independent and tau_j is a fair bit. For a batch let G be the sigma-field generated
by: all low_j of its leaves; all FW cell/junk outcomes; all merge outcomes (e, bl); and all decisions of the controller in
that batch (slot stores and matches, FAIL and retries, aborts, assignment of qubits). G does not include
root measurement outcomes, which no decision in the batch reads. It also excludes LE's internal coins and outcomes,
which in the ideal run feed no decision.

Lemma 10.1. In the ideal run, conditional on G and on all independent randomness outside the batch, the top bits tau_j
are i.i.d. fair.

Proof. Induct over the controller's steps. Every slot key, residue, sort, rank and block partition reads only label bits
strictly below position B, because all positions used are below B (Section 8). Bits below B of a sum of leaf labels,
and of a difference modulo 2^(pp_i+pb_i) with pp_i+pb_i <= B, depend only on the low_j, since multiples of 2^B do not change them.
FW outcomes have the phase- and label-independent law in Lemma7.1(a), including their junk values. Exact PREP ancillas are independent of labels. By Lemma 6.1 each merge outcome's conditional law, given
labels and earlier outcomes, is a function of the low_j and earlier outcomes only. So the joint law factorizes as
law(tau) x law(low) x law(outcomes and decisions | low). QED.

Incidence. An entry of a table is the sum over leaves j of x_j k_j, for a 0/1 incidence vector x. Distinct indices of a
table have distinct incidence vectors: this holds for a leaf qubit, table (0, k_j); in FW each returned or combined output has an injective incidence map on disjoint input sets (Section 7.1); a LEAF table concatenates disjoint coordinates; and a merge re-indexes injectively pairs on disjoint
coordinates. So the two root entries have x0 != x1, and with hd = |x0 xor x1| >= 1,

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

Success. The ideal-run failure budgets are batch aborts2^-12+2^-11,
odd decoding2^-20, and parity misses n2^-K<=2^-40. LE coupling costs
at most2^-10 by(5.1). The physical PREP phase begins before touching the
group data. Each started group has fewer than W0 independent PREP calls,
each with conditional failure below2^-3r. At most n(Ccap+1) groups start,
so a union bound on PREP aborts is at most

    n(Ccap+1)W0 2^-3r <=2n W0Ccap2^-3r
      <=2^(-r+2log2r+29) <=2^-10.

Here log2Ccap<=2r-1,n<=r²,W0=2^28,r>=2^24. Each successful PREP produces
the exact required ancilla; a physical run can be coupled to the ideal
stream until its first PREP abort or LE error, with the stated additive
budgets. There is no conditioning on all future successes.
The total2^-12+2^-11+2^-20+2^-40+2^-10+2^-10 is less than2^-8.
The finite branch has failure at most2^-10. Thus full-secret recovery
succeeds with probability at least1-2^-8 for every input.

## 14. Resources on every main-branch execution

Throughout, K, dl, m, ell, w = O(sqrt n). Writing PP = RHO^ell 2^m, we have Dcap = O(n^2 2^m) and Ccap = O(n^2 PP). All fixed loops, caps and aborts below hold on every branch.

Q. Q <= Qcap = O(n^3 PP).

S_Q. By Section7.2 the streaming stage uses (W0-1)sum_iE_i+O(W0 ell)+c_F = O(sqrt n 2^w+n) qubits. The depth-first stack holds at most two index registers per level, at most
2 (m+1)(dl+m) = O(n) qubits. A merge adds O(sqrt n) qubits. LE and transforms use O(n), reset between uses. So S_Q = O(sqrt n 2^w + n).

S_C. Slot tables use O(ell 2^w n) = O(n^(3/2) 2^w) bits. Depth-first tables: at most three tables per level, each of 2^(lam_i) fields of 3n bits, plus merge scratch O((L + L') n). Since
lam_i <= dl + m - 1 and these geometric sizes sum, this is O(n 2^(dl+m)). The decoder stores K triples and K residues of O(n) bits. LE uses O(n) bits. Since w <= dl + m - log2 n for these
parameters (0.8 r >= log2 n), S_C = O(n 2^(dl+m)). These are fixed allocations.

Core steps, per batch.
- Acquisitions: at most Ccap, each O(n^2) for Mult plus O(n^(5/2)) for LE (log2 Qcap = O(sqrt n) by (8.1), so h_e = O(sqrt n)): O(n^(5/2) Ccap).
- Pairing, Section 7: O(n A_0 + sum_i E_i) = O(n Ccap), since Ccap >= RHO^ell 2^m >= 2^m >= 2^w.
- Tree: since D <= Dcap on every branch, there are at most Dcap/dl LEAF calls at O(n 2^dl) each. A merge producing level i+1 consumes 2^(i+1) dl delivered qubits that no other merge at that
  level uses, since inputs of a failed merge are discarded. So there are at most Dcap/(2^(i+1) dl) of them, each O(n 2^(dl+i)) by Section 6. Each level costs O(n Dcap 2^dl/dl), and all m+1 levels
  cost O(m n Dcap 2^dl/dl) = O(n Dcap 2^dl) = O(n^3 2^(m+dl)).
- Decoder per stage: at most 2^(Y+8) candidates, K residues each, O(n) bits per addition: O(K n 2^Y) = O(n^(3/2) Ccap).

Over at most n batches, plus poly(n) setup (parameters, CRT, Mult constants, the table of Section 4, shift values, initial residues), core steps total O(n^(7/2) Ccap + n^4 2^(m+dl)) + poly(n). Every
loop is either fixed-length or consumes acquisitions or delivered qubits under a cap, and every FW consumes an arrival, so every branch terminates.

T. By (8.1), log2(S_C + S_Q + 2) = O(sqrt n). By (2.1),

    T = O(n^4 Ccap + n^(9/2) 2^(m+dl) + n Q) = O(n^6 PP + n^(9/2) 2^(m+dl)).

Exponents. From log2RHO<10001/10000,r<=sqrt n+1,

    log2PP <=(64967307/50000000)r+10001/10000+1
             <1.2994sqrt n+4,
    m+dl<=1.3376r+2<=1.3376sqrt n+3.338,
    w<=.4995sqrt n+.5.

Hence jointly on every main-branch execution,

    T=O(n^6 2^(1.3376sqrt n)), S_C=O(n2^(1.3376sqrt n)),
    S_Q=O(sqrt n2^(.4995sqrt n)), Q=O(n³2^(1.2994sqrt n)).

All W0,c_F-dependent factors are absolute outside constants. Since
m+dl-w>=.8381r>=log2n, tree records absorb slot/queue/free-handle records.
The source exponent is strictly below the tree exponent. Initializing all
fixed slots and ancillas is also below this work bound and is charged.

## 15. Indices and uniform declared envelopes

For fixed k,c>0,n^k2^(-c sqrt n) is bounded on n>=1. Margins .0001
for T/SC,.0005 for SQ,.0006 for Q absorb the polynomial factors.
The finite branch n<2^48 contributes absolute constants. Thus the joint
uniform envelopes are those in Section0. Every representative2^(c sqrt n),
c>0, has exact double-log growth index1/2, giving the numeric score[1/2].

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does not assert that robustness is impossible.

## 17. Scope and limitations

This does not reach the cube-root target and has time index1/2.
Classical memory, quantum memory and sample acquisition remain
square-root exponential. W0 and every circuit constant are absolute but
large. The theorem concerns this one specified stream, not a practical
runtime experiment or global optimum. The zero fractional tolerance is
only the independent-ideal-copy promise; no robustness impossibility is
asserted. Earlier verdicts are not used as mathematical premises.
