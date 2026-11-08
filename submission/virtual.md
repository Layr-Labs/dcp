# TRIAD-125: HPC-127 with a three-qubit odd-pair recycling instrument in front of linear-merge collimation

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N), and let a0 = 5/4.
The single algorithm TRIAD-125 below receives N in binary and fresh independent copies of
rho_s, and outputs the entire s with unconditional probability at least 1 - 2^-7 > 2/3.
On EVERY execution branch (every failure, discard and abort included) it satisfies jointly

    T = O(2^(a0 sqrt n)),  S_C = O(2^(a0 sqrt n)),  S_Q = O(2^(a0 sqrt n)),  Q = O(2^(a0 sqrt n)).

All constants are absolute. Each of the four envelopes has growth index exactly 1/2
(Section 15). The fifth claim is the clean-input tolerance 0 (Section 16). The sharper
main-branch bounds, from which these follow, are in Section 14: T = O(n^6 2^(e sqrt n)),
S_C = O(n^3 2^(e sqrt n)), S_Q = O(n^2 2^(e sqrt n)) and Q = O(n^3 2^(e sqrt n)) with
e = 156/125 = 1.248 < a0. The envelope coefficient is a fixed exact rational; no hidden
constant sits inside an exponent.

Notation:
- dn = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with
  s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known nonnegative integer. log means log2 unless stated otherwise.

Main-branch parameters, computed by exact integer arithmetic for n >= 2^28:

    r = ceil(sqrt n),   ell = ceil(183 r/500),   m = ceil(73 r/100),   dl = ceil(259 r/500),
    kappa = ceil(log2 m) + 1.

So there are ell TRIAD LEVELS, a collimation tree of depth m, and leaf tables built from
dl qubits. Since r >= 2^14 these satisfy ell >= 2, dl >= kappa + 1, 2^kappa >= 2m.

## 1. Provenance and what is new

TRIAD-125 is qzv's HPC-127 (public submission 2aad498c-d5e9-4f64-a222-3b2f7f961738 on this
challenge) with one change: its pairing stage (HPC-127 Section 7: PAIR, PAIRLEVEL and Lemmas 7.1,
7.2) is replaced by a stage built on a three-qubit instrument, TRIAD, and the schedule is re-derived
for it. The text is HPC-127's wherever the argument is unchanged:
- Sections 2, 3, 4, 6, 11, 12 and 16 are HPC-127's text unchanged. Section 5 differs only in the
  algorithm name.
- Sections 9, 10 and 13 are HPC-127's text with these edits. Section 9: step 2 and Lemma 9.2 use
  TRIADLEVEL and the slot bound C_i/(8 ell). Section 10: the sigma-field, one sentence of the proof
  of Lemma 10.1 and one sentence of the incidence paragraph name TRIAD outcomes and index maps
  instead of PAIR's. Section 13: the stage name and the constant m >= 11000.
- Sections 8 and 14 keep HPC-127's structure and wording with new constants: the recursion
  C_i = ceil(8 ell C_(i+1)/(3(ell-1))), the brackets 58/41 < log2(8/3) < 75/53 (derived from
  HPC-127's two integer facts), the slot rule 2^b 8 ell <= C_i, the capacity Lemma 8.1 for the new
  ratios, sum_i C_i <= (8/5) C_0, and the new exponents. Section 8 also adds one parenthetical sentence
  accounting for the constant 33 in (8.3). Section 14 also adds one S_Q sentence (a TRIAD adds O(1)
  ancillas, all released in |0>, by Lemma 7.1(d)), and its TRIAD-stage cost item uses
  Y + 1 <= 2r + 1 <= 6 ell.
- Sections 1 and 7 are new. Sections 0, 15 and 17 are HPC-127's text with the new name, parameters and
  constants; in addition, Section 0 lists the sharper bounds of Section 14, and Section 17 compares
  with HPC-127 and adds a last item on instruments on more qubits.

HPC-127 itself restates the framework of CS1 (AdamGagol, submission
f1481815-9577-4990-abe3-7b79fa5d9284) in Sections 2-6 and 10-12, and its Lemma 7.2 uses a
distribution-free bucket count of the kind also in PSieve (spariev, submission
4256e671-97b0-4f84-82ce-12aeee17224e); Section 7 here uses the same bucket fact, with at most two
leftovers per key instead of one.
Overlapping, non-projective extraction instruments whose outcome law does not depend on the unknown
phases were introduced on this challenge by 0xplemonade's CYC1 (submission
7a4cecdc-7941-4027-8c95-8520de9fbcf3); TRIAD is an instrument of that kind, with a different cell
family and a different use. The collimation step goes back to G. Kuperberg, "Another
subexponential-time quantum algorithm for the dihedral hidden subgroup problem", arXiv:1112.3333.
Pairing qubits with equal low label bits is from G. Kuperberg, "A subexponential-time quantum
algorithm for the dihedral hidden subgroup problem", SIAM J. Comput. 35(1), 2005. These citations
are context; every step used is proved below, and no earlier verdict is a premise.

New in this submission:
1. TRIAD (Section 7.1). On three labeled qubits with equal keys it is the instrument with Kraus
   operators Pi_{000,111} and 2^(-1/2) Pi_{x_a != x_b} for the three pairs {a,b}, realized exactly by
   CNOT, Toffoli, H and computational-basis measurement, with no rotation synthesis and no
   repeat-until-success loop. Each of its four outcomes has probability exactly 1/4 whatever the
   labels. With probability 3/4 it yields one difference qubit AND returns the third qubit exactly in
   its input state; otherwise it yields one recycled qubit (Lemma 7.1).
2. TRIADLEVEL and its distribution-free yield (Section 7.2). Every operation removes exactly two
   qubits from the live list, so the number of operations is fixed up to at most two leftovers per
   key, and the yield is a sum of i.i.d. Bernoulli(3/4) outcomes (Lemma 7.2). A level costs a net 8/3
   inputs per output, against PAIRLEVEL's 3.
3. The schedule for TRIAD (Section 8) and the accounting (Sections 13-15).

The Lueders instrument of a fractional cover by cells is standard measurement theory; only its use as
the recycling rule of a pairing pool is claimed as new, as far as we found. The instrument comes from
our own unpublished research notes.

Why this helps. A pool level costs log2 q bits of budget, where q is the net number of input qubits
consumed per output that advances. PAIR with recycling has q = 3: two inputs, an output with
probability 1/2, one recycled qubit otherwise. TRIAD has q = 2/(3/4) = 8/3: every operation removes
two qubits net and advances one with probability 3/4. HPC-127's yield integral
n ~ (X^2/2)(1 + 1/(c(c+1))) with c = log2(8/3) instead of log2 3 gives X ~ 1.24388 instead of
1.26792. A projective computational-basis measurement cannot do this: learning which pair is odd
projectively reveals both parities and collapses the third qubit. TRIAD picks one of the two odd
pairs by a coin that is then erased coherently, so its two cells containing a point overlap and the
third qubit is never measured. This paragraph is motivation. The theorem rests only on the explicit
schedule of Section 8. As in HPC-127 the pool is held coherently, so S_Q is exponential in sqrt n.

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

IDEAL run. The ideal run is TRIAD-125 in the latent-label model with every LE output replaced by the
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

## 7. The TRIAD stage

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
TRIAD (Lemma 7.1).

### 7.1 The instrument TRIAD

Input: labeled qubits A1, A2, A3 on disjoint qubits, with tables (t0^j, t1^j), j = 1, 2, 3. Write
x = (x1, x2, x3) in {0,1}^3 for their computational-basis value, Ev = {000, 111}, and for
l in {1,2,3}, with {a, b} = {1,2,3} \ {l} and a < b,

    A_l = {x : x_a != x_b}   (qubit l unconstrained).

Pi_S is the projector onto the span of |x>, x in S, acting on A1, A2, A3. TRIAD is the instrument with
outcomes l in {0,1,2,3} and Kraus operators

    K_0 = Pi_Ev,     K_l = 2^(-1/2) Pi_(A_l)   (l = 1, 2, 3).                            (7.1)

Completeness: a point x outside Ev has exactly one coordinate o(x) that differs from the other two,
which agree, and x_a != x_b iff o(x) is in {a, b}. So x lies in A_l exactly for the two values
l != o(x), and sum_l K_l^dagger K_l = Pi_Ev + (1/2) * 2 (I - Pi_Ev) = I. The sets A_l overlap; the
instrument is not a projective measurement.

Circuit. Ancillas, all fresh |0>: qubits e1, e2, a coin c, a two-qubit outcome register (L1, L0), and
O(1) scratch qubits.
1. XOR x1 xor x2 into e1 and x1 xor x3 into e2 (four CNOTs).
2. Apply H to c.
3. XOR f(e1, e2, c) into (L1, L0), where (juxtaposition is AND, + is XOR)
       L1 = e1 e2 + (e1 + e2) c,     L0 = e1 e2 c + e1 (1 - e2) + (1 - e1) e2 (1 - c).
4. XOR h(e1, e2, L1, L0) = e1 e2 L0 + (e1 + e2) L1 into c.
5. Repeat step 1 (this clears e1, e2).
6. Measure L1 and L0, put l = 2 L1 + L0, and reset L1, L0. If l = 0, apply H to c. Release c.
7. If l is in {1,2,3}: apply CNOT with A_a as control and A_b as target; A_b is then exactly |1>; apply
   NOT to it and release it. The GOOD output is qubit A_a with table (t0^a + t1^b, t1^a + t0^b), and
   qubit A_l is RETURNED with its table unchanged. If l = 0: apply CNOT A1 -> A2 and CNOT A1 -> A3; A2
   and A3 are then exactly |0>; release them. The RECYCLED output is qubit A1 with table
   (t0^1 + t0^2 + t0^3, t1^1 + t1^2 + t1^3).

Steps 3 and 4 XOR a fixed Boolean function of at most four qubits into a target that is not one of its
inputs. For each input pattern on which the function is 1, a Toffoli chain on O(1) scratch computes the
flag of that pattern (NOT gates around the 0-controls), a CNOT copies the flag into the target, and the
chain is uncomputed, exactly as in Section 6.1. So TRIAD uses O(1) NOT/CNOT/Toffoli/H gates (each a core
step of Section 2, classically chosen), two measurements and O(1) ancilla qubits, plus O(n) classical
steps for the table additions. Its Kraus weights are 1/2 and 1, produced by the one Hadamard coin; no
rotation synthesis and no repeat-until-success loop occurs, and TRIAD has no failure outcome.

Values of f and h. (e1, e2) = (x1 xor x2, x1 xor x3) is (1,1), (1,0), (0,1) iff o(x) = 1, 2, 3, and
(0,0) iff x is in Ev. The formulas give, with l = 2 L1 + L0:
- (e1, e2) = (1,1): (L1, L0) = (1, c), so l = 2 + c, in {2, 3};
- (e1, e2) = (1,0): (L1, L0) = (c, 1), so l = 1 + 2c, in {1, 3};
- (e1, e2) = (0,1): (L1, L0) = (c, 1 - c), so l = 1 + c, in {1, 2};
- (e1, e2) = (0,0): (L1, L0) = (0, 0).
So for x outside Ev, c = 0 and c = 1 give the two distinct values l != o(x), i.e. the two l with x in
A_l. In the three non-zero cases h(e1, e2, f(e1, e2, c)) = c (it reads L0 = c, L1 = c and L1 = c
respectively), and h(0, 0, 0, 0) = 0.

Lemma 7.1 (TRIAD). (a)-(c) assume that, conditional on the past, A1, A2, A3 are in the product state
psi = (x)_j 2^(-1/2) (exp(2 pi i t0^j th)|0> + exp(2 pi i t1^j th)|1>), in tensor product with the
rest of the system, which is in an arbitrary state.
(a) The outcome l is uniform on {0,1,2,3}, whatever the labels, th and the past.
(b) Given l in {1,2,3}, the good output is exactly the phase vector with table
    (t0^a + t1^b, t1^a + t0^b), whose label difference is Del_a - Del_b; A_l is exactly in its input
    state; they are in tensor product with each other and with the rest, which is unchanged.
(c) Given l = 0, the recycled output is exactly the phase vector with table
    (t0^1 + t0^2 + t0^3, t1^1 + t1^2 + t1^3), whose label difference is Del_1 + Del_2 + Del_3, in tensor
    product with the unchanged rest.
(d) For every input state, ideal or not, steps 1-6 realize the instrument (7.1) tensored with the
    identity on the rest, with every ancilla back in |0>; step 7 then leaves every released qubit in
    |0> on every input.

Proof. Write any joint state (purify the rest if it is mixed) as Psi = sum_x |x> (x) |R_x>, with |R_x>
unnormalized states of the rest.
Steps 1-2 give sum_x |x>|R_x>|e(x)>|+>_c|00>_L. Step 3 maps |x>|e(x)>|c> to
|x>|e(x)>|c>|f(e(x), c)>. Step 4 then clears c when x is outside Ev, by h(e, f(e, c)) = c, and leaves
c untouched when x is in Ev, where L = 00. After step 5 (e cleared, scratch back to |0>):

    sum_(x not in Ev) |x>|R_x> |0>_c 2^(-1/2) sum_(l : x in A_l) |l>_L  +  sum_(x in Ev) |x>|R_x> |+>_c |0>_L.

Measuring L = l != 0 leaves (2^(-1/2) sum_(x in A_l) |x>|R_x>) |0>_c = (K_l (x) I) Psi |0>_c, and L = 0
leaves (Pi_Ev (x) I) Psi |+>_c, and then H returns c to |0>. After outcome l != 0 the state is supported
on x_a != x_b, so after CNOT A_a -> A_b the value of A_b is 1 on every term; after outcome 0 it is
supported on {000, 111}, so after the two CNOTs A2 = A3 = 0 on every term. This is (d).
For the product input, |R_x> = 2^(-3/2) exp(2 pi i phi(x)) |R> with phi(x) = th sum_j t_(x_j)^j. So
Pr[l] = ||K_l psi||^2 = (1/2) |A_l| / 8 = 1/4 for l != 0 (|A_l| = 4) and |Ev| / 8 = 1/4 for l = 0. This
uses only the moduli 2^(-3/2), which is (a). For (b): A_l = {x_a != x_b} x {0,1} on qubit l, so
Pi_(A_l) psi = [2^(-1) (exp(2 pi i (t0^a + t1^b) th)|0_a 1_b> + exp(2 pi i (t1^a + t0^b) th)|1_a 0_b>)]
(x) [2^(-1/2) sum_y exp(2 pi i t_y^l th)|y>_l]. CNOT A_a -> A_b maps |0 1> to |0 1> and |1 0> to |1 1>,
so A_b = |1>, A_a is the phase vector (t0^a + t1^b, t1^a + t0^b), and A_l is untouched. For (c):
Pi_Ev psi = 2^(-3/2) (exp(2 pi i phi(000))|000> + exp(2 pi i phi(111))|111>), and the two CNOTs map
|y y y> to |y 0 0>. QED.

Every table produced is a sum of input tables over disjoint inputs: the good output's entry alpha is
the sum of entry alpha of A_a and entry 1 - alpha of A_b; the recycled output's entry alpha is the sum
of entry alpha of A1, A2 and A3. By (b) and (c), (P) is preserved.

### 7.2 TRIADLEVEL

TRIADLEVEL(pool, Cin, p, c, rounds). Input: Cin labeled qubits collimated to p; integer c >= 0,
E = 2^c. A qubit's KEY is Del mod 2^(p+c), computed from t1 and t0 modulo 2^(p+c). Keep a LIVE list,
initially all inputs, and an OUTPUT list, initially empty. Repeat for exactly `rounds` rounds:
merge-sort LIVE by key; scan it and cut each maximal run of equal keys into consecutive triples,
leaving the last (run length mod 3) <= 2 qubits of the run ungrouped; then apply TRIAD to each triple,
in scan order. A good output is appended to OUTPUT. The returned qubit (outcomes 1, 2, 3) and the
recycled qubit (outcome 0) are put in LIVE for the next round; ungrouped qubits also stay in LIVE.
After the last round measure, reset and release LIVE.

Invariants. Every LIVE qubit is collimated to p: a returned qubit keeps its table, and a recycled one
has Del_1 + Del_2 + Del_3 = 0 mod 2^p. Every OUTPUT qubit is collimated to p+c, because equal keys give
Del_a - Del_b = 0 mod 2^(p+c). The sort keys read only label bits below p+c. The triples of a round are
fixed before its first TRIAD, and the three qubits of a triple are distinct pool qubits.

Operation count. Each TRIAD removes its three inputs from LIVE and puts exactly one qubit back
(returned or recycled), and nothing else changes the size of LIVE. So if A TRIADs are applied and
S_end qubits are live after the last round, then on every branch

    Cin - 2A = S_end.                                                                  (7.2)

Live count. LIVE qubits are collimated to p, so their keys take at most E = 2^c values, and a round leaves
at most two qubits per key ungrouped. In one round with u <= 2E ungrouped qubits, a list of length L
becomes u + (L - u)/3 = (L + 2u)/3 <= (L + 4E)/3, and it never grows. So L_j - 2E <= (Cin - 2E)/3^j.
With 2^rounds > Cin, at the end L_rounds - 2E < 1, that is S_end <= 2E, deterministically, whatever the
labels and outcomes. By (7.2), A >= (Cin - 2E)/2 on every branch.

Lemma 7.2 (distribution-free TRIAD yield). Let ell >= 2, E <= Cin/(8 ell) and 2^rounds > Cin. For ANY
labels, and conditional on everything before the level, the size S of OUTPUT satisfies
S >= 3 (ell - 1) Cin/(8 ell) except with probability at most exp(-Cin/(64 ell^2)).

Proof. Number the TRIADs in the order applied. Let F_k be the labels and all outcomes and decisions
before the k-th TRIAD, which include its triple, and let b_k = 1 if its outcome is in {1,2,3}. By (P)
and Lemma 7.1(a), Pr[b_k = 1 | F_k] = 3/4. Put z = ceil((Cin - 2E)/2). Since A >= z on every branch,
b_1, ..., b_z are defined on every branch, and as b_1, ..., b_(k-1) are F_k-measurable, the chain rule
gives Pr[b_1 ... b_z = beta] = prod_k (3/4)^(beta_k) (1/4)^(1 - beta_k) for every beta in {0,1}^z:
these are z independent Bernoulli(3/4) bits. Each b_k = 1 appends one qubit to OUTPUT, so
S >= S_z = b_1 + ... + b_z. Put g = 1/(4 ell) <= 1/8. Since 2E <= g Cin, z >= (1-g) Cin/2 >= 7 Cin/16.
By Hoeffding,

    Pr[S_z < (3/4)(1-g) z] <= exp(-2 (3g/4)^2 z) <= exp(-(9/8)(7/16) g^2 Cin) = exp(-63 Cin/(2048 ell^2)),

which is at most exp(-Cin/(64 ell^2)). Outside this event S >= (3/4)(1-g)(1-g) Cin/2
= (3/8)(1-g)^2 Cin >= (3/8)(1 - 1/(2 ell)) Cin >= 3 (ell - 1) Cin/(8 ell). QED.

No property of the label distribution is used. Returned qubits keep their key and recycled ones get
three times the common key modulo 2^(p+c), so the keys of later rounds are correlated with earlier
outcomes; the proof does not care, since it uses only (7.2), the live count and the outcome law, which
is the same for every triple. By (7.2) the number of operations is fixed up to the at most 2E
leftovers, so no Wald argument is needed at this stage (Wald's identity is used only for the tree,
Lemma 9.1).

Cost. Each list entry stores t0, t1 and the wire index of its qubit, O(n) bits. A round on L live qubits
costs O(L log L) comparisons of O(n)-bit keys and at most L/3 TRIADs, each O(1) gates and O(n)-bit table
additions: O(L n log L) core steps. Reading the three stored wire indices of a triple, each of
O(sqrt n) bits by (8.3), is O(sqrt n) core steps, inside the O(n) per-TRIAD bookkeeping. Since
L_j <= 2E + Cin/3^j, sum_j L_j <= (3/2) Cin + 2 rounds E, and a level costs
O((Cin + rounds E) n log Cin) core steps, with O(1) ancilla qubits beyond the pool. The number of
rounds is fixed, and these bounds hold on every branch.

## 8. The schedule

Pool sizes. Define C_ell = 2^12 n K 2^m dl, with K from (11.0), and for i = ell-1, ..., 0,
C_i = ceil(8 ell C_(i+1) / (3 (ell - 1))). Then, with rho = 8 ell/(3 (ell-1)) >= 8/3 >= 2,

    C_i >= (8/3)^(ell-i) C_ell >= (8/3)^(ell-i) 2^m,                                 (8.1)
    C_0 <= rho^ell (C_ell + 1) <= 2 rho^ell C_ell <= 8 (8/3)^ell C_ell,               (8.2)

since C_i <= rho C_(i+1) + 1, sum_(j<ell) rho^j <= rho^ell, and (1 - 1/ell)^(-ell) <= 4 for ell >= 2.
Let Y be the least integer with 2^Y >= C_0. Each level uses rounds = Y + 1.

Two exact numerical facts: 3^41 = 36472996377170786403 < 2^65 = 36893488147419103232 and
3^53 = 19383245667680019896796723 > 2^84 = 19342813113834066795298816. Hence
(8/3)^41 = 2^123/3^41 > 2^58 and (8/3)^53 = 2^159/3^53 < 2^75, so 58/41 < log2(8/3) < 75/53.

Size bound. From (8.2), using (8/3)^ell <= 2^(75 ell/53), ell <= 183r/500 + 1, m <= 73r/100 + 1,
K <= 3 * 2^13 r (as 2r + ceil(log2 n) + 30 <= 3r), dl <= r and n <= r^2,

    log2 C_0 <= (75/53)(183/500) r + (73/100) r + 4 log2 r + 33 <= 1.24793 r + 4 log2 r + 33 <= 2r - 1.   (8.3)

(The constant: 3 from (8.2), 75/53 + 1 from the roundings of ell and m, and 12 + 13 + log2 3 from
2^12, K and n dl <= r^3, a total below 33.) So Y <= 2r <= n (as r <= sqrt n + 1 and n >= 2^28), and
2^Y <= 2 C_0.

Level capacities.
- TRIAD level i (0 <= i < ell): pbmax_i is the largest integer b with 2^b * 8 ell <= C_i.
- Tree: lam_i = dl + i for 0 <= i <= m-1, lam_m = 1; tbmax_i = dl + i - kappa - 1 for 0 <= i <= m-2;
  tbmax_(m-1) = 2 (dl + m - 1) - kappa - 1.

For every b_i <= tbmax_i, in all cases

    b_i + lam_(i+1) - 2 lam_i <= -kappa.                                            (8.4)

Lemma 8.1 (capacity). For n >= 2^28: sum_i pbmax_i + sum_i tbmax_i >= r^2 >= n.

Proof. By maximality 2^(pbmax_i) * 16 ell > C_i, so by (8.1) and log2(8/3) > 58/41,
pbmax_i > (58/41)(ell - i) + m - log2(16 ell). Summing over i < ell,

    sum_i pbmax_i >= (29/41) ell^2 + ell m - ell log2(16 ell).

Direct expansion gives sum_i tbmax_i = m dl + m^2/2 + dl + m/2 - 1 - m (kappa + 1) >= m dl + m^2/2 - m (kappa + 1).
With ell >= 183r/500, m >= 73r/100, dl >= 259r/500, the positive terms total at least

    ( (29/41)(183/500)^2 + (183/500)(73/100) + (73/100)(259/500) + (73/100)^2/2 ) r^2 = (20633647/20500000) r^2 >= 1.0065 r^2.

For r >= 2^14 we have ell <= 0.3661 r, m <= 0.7301 r, log2(16 ell) <= log2 r + 2.56 and
kappa + 1 <= log2 m + 3 <= log2 r + 2.55. So the subtracted terms are at most r (1.0962 log2 r + 2.81).
Finally 0.0065 r >= 1.0962 log2 r + 2.81 at r = 2^14, where 106.4 >= 18.2, and for larger r because the
left side grows faster (its derivative 0.0065 exceeds 1.0962/(r ln 2)). QED.

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
2. TRIAD STAGE. For i = 0, ..., ell-1 run TRIADLEVEL(pool, C_i, pp_i, pb_i, Y+1). If it yields fewer than C_(i+1)
   qubits, ABORT; otherwise keep the first C_(i+1) and measure and release the rest. By the invariants the final
   pool qubits are collimated to pp_ell, and E_i = 2^(pb_i) <= C_i/(8 ell) by definition of pbmax_i, while
   2^(Y+1) > C_i.
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

Lemma 9.2 (TRIAD-stage yield). In the ideal run, step 2 aborts with probability at most ell exp(-2^m/(64 ell^2)).

Proof. Lemma 7.2 applies at each level, conditional on the earlier levels, with Cin = C_i >= 2^m and
3 (ell - 1) C_i/(8 ell) >= C_(i+1). QED.

## 10. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and tau_j in {0,1}. Since k_j is uniform on
[0, 2^(B+1)), low_j and tau_j are independent and tau_j is a fair bit. For a batch let G be the sigma-field generated
by: all low_j of its leaves; all TRIAD outcomes l; all merge outcomes (e, bl); and all decisions of the controller in
that batch (sort orders, groupings into triples, trimming, FAIL and retries, aborts, assignment of qubits). G does not include
root measurement outcomes, which no decision in the batch reads. It also excludes LE's internal coins and outcomes,
which in the ideal run feed no decision.

Lemma 10.1. In the ideal run, conditional on G and on all independent randomness outside the batch, the top bits tau_j
are i.i.d. fair.

Proof. Induct over the controller's steps. Every key, residue, sort, rank and block partition reads only label bits
strictly below position B, because all positions used are below B (Section 8). Bits below B of a sum of leaf labels,
and of a difference modulo 2^(p+c) with p+c <= B, depend only on the low_j, since multiples of 2^B do not change them.
TRIAD outcomes are uniform on {0,1,2,3} whatever the labels and the past (Lemma 7.1(a), which applies at every
TRIAD by (P)), and returned and recycled qubits carry explicit tables, sums of leaf labels, so their later
keys again read only bits below B. By Lemma 6.1 each merge outcome's conditional law, given
labels and earlier outcomes, is a function of the low_j and earlier outcomes only. So the joint law factorizes as
law(tau) x law(low) x law(outcomes and decisions | low). QED.

Incidence. An entry of a table is the sum over leaves j of x_j k_j, for a 0/1 incidence vector x. Distinct indices of a
table have distinct incidence vectors: this holds for a leaf qubit, table (0, k_j); in TRIAD the index maps
alpha -> (alpha, 1 - alpha) on (A_a, A_b) and alpha -> (alpha, alpha, alpha) on (A1, A2, A3) are injective on
disjoint coordinates, and a returned qubit keeps its table; a LEAF table concatenates disjoint coordinates; and a
merge re-indexes injectively pairs on disjoint coordinates. So the two root entries have x0 != x1, and with hd = |x0 xor x1| >= 1,

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

Finite branch (n < 2^28). For each cand = 0..N-1 in order, use n+10 fresh copies: apply Shift_cand, measure the control in X, and
reject cand at the first minus outcome. Output the first cand with no rejection, or 0. For cand = s every outcome is plus. For
cand != s the two data branches are orthogonal, so each outcome is uniform. A union bound gives Pr[wrong] <= N 2^-(n+10) <= 2^-10.
All resources on this branch are bounded by an absolute constant.

Main branch (n >= 2^28). Compute a2, M, dn, J, K, the schedule, Y, and all allocations; put

    Qcap = 4 n C_0 + K.

Run Section 11 and then Section 12. Any ABORT stops the algorithm, releases everything and outputs 0. Since J + 1 + a2 <= log2 M + a2
= log2 N <= n, there are at most n batches, each using at most 4 C_0 acquisitions, plus at most K per wd = 1 level, of which there is
at most one. So Q <= Qcap on every branch, without any counter being needed. LE is sized by this Qcap, which is computed before h_e.

Success. In the ideal run the failure events are: a pool exhaustion, at most n * 2^-10/n = 2^-10 (Lemma 9.1); a TRIAD-stage abort, at most
n ell exp(-2^m/(64 ell^2)) (Lemma 9.2), and a supplier abort, at most n exp(-C_0/2), both below 2^-40 because m >= 11000 and ell, n are
at most polynomial in r; a decoder error, at most 2^-20 (Lemma 11.1); a 2-adic miss, at most n 2^-K <= 2^-40. Adding the LE coupling (5.1):

    Pr[output = s] >= 1 - 2^-10 - 2^-40 - 2^-40 - 2^-20 - 2^-40 - 2^-10 >= 1 - 2^-8 > 1 - 2^-7 > 2/3.

The finite branch succeeds with probability at least 1 - 2^-10. These are additive couplings; there is no conditioning on favorable
labels or outcomes.

## 14. Resources on every main-branch execution

Throughout, K = O(sqrt n), dl, m, ell = O(sqrt n), C_ell = O(n^2 2^m) and, writing PP = (8/3)^ell 2^m, C_0 = O(n^2 PP) by (8.2). Also
sum_i C_i <= (8/5) C_0, since C_i >= (8/3) C_(i+1). All fixed loops, caps and aborts below hold on every branch.

Q. Q <= Qcap = O(n^3 PP).

S_Q. The pool holds at most C_0 qubits. A TRIAD adds O(1) ancillas, all released in |0> (Lemma 7.1(d)). The depth-first stack holds at
most two index registers per level, at most 2 (m+1)(dl+m) = O(n) qubits. A merge adds O(sqrt n) qubits. LE and transforms use O(n), reset
between uses. So S_Q = O(C_0 + n) = O(n^2 PP).

S_C. Pool tables and sort scratch use O(n C_0) bits. Depth-first tables: at most three tables per level, each of 2^(lam_i) fields of
3n bits, plus merge scratch O((L + L') n). Since lam_i <= dl + m - 1 and these geometric sizes sum, this is O(n 2^(dl+m)). The decoder stores
K triples and K residues of O(n) bits. LE uses O(n) bits. So S_C = O(n^3 PP + n 2^(dl+m)). These are fixed allocations.

Core steps, per batch.
- Acquisitions: at most 4 C_0, each O(n^2) for Mult plus O(n^(5/2)) for LE (log2 Qcap = O(sqrt n) by (8.3), so h_e = O(sqrt n)): O(n^(5/2) C_0).
- TRIAD stage, Section 7: at level i the cost is O((C_i + (Y+1) E_i) n log C_i) with E_i <= C_i/(8 ell) and Y + 1 <= 2r + 1 <= 6 ell, and
  log C_i <= Y = O(sqrt n). So a level costs O(n^(3/2) C_i), and the stage O(n^(3/2) C_0), using sum_i C_i <= (8/5) C_0.
- Tree: there are at most C_ell/dl LEAF calls at O(n 2^dl) each. A merge producing level i+1 consumes 2^(i+1) dl pool qubits that no other merge at that level uses,
  since inputs of a failed merge are discarded. So there are at most C_ell/(2^(i+1) dl) of them, each O(n 2^(dl+i)) by Section 6. Each level thus costs
  O(n C_ell 2^dl/dl), and all m+1 levels cost O(m n C_ell 2^dl/dl) = O(n C_ell 2^dl) = O(n^3 2^(m+dl)).
- Decoder per stage: at most 2^(Y+8) candidates, K residues each, O(n) bits per addition: O(K n 2^Y) = O(n^(3/2) C_0).

Over at most n batches, plus poly(n) setup (parameters, CRT, Mult constants, the table of Section 4, shift values, initial residues), core steps total
O(n^(7/2) C_0 + n^4 2^(m+dl)) + poly(n). Every loop is either fixed-length or consumes pool qubits or acquisitions, so every branch terminates.

T. By (8.3), log2(S_C + S_Q + 2) = O(sqrt n). By (2.1),

    T = O(n^4 C_0 + n^(9/2) 2^(m+dl) + n Q) = O(n^6 PP + n^(9/2) 2^(m+dl)).

Exponents. Since (8/3)^ell <= 2^(75 ell/53) and r <= sqrt n + 1,

    log2 PP <= (75/53)(183 r/500 + 1) + 73 r/100 + 1 = (3307/2650) r + 128/53 <= 1.24793 sqrt n + 3.67,
    m + dl <= (73/100 + 259/500) r + 2 = (156/125) r + 2 <= 1.248 sqrt n + 3.25.

Since 3307/2650 < 156/125 = 1.248 (3307 * 125 = 413375 < 413400 = 156 * 2650), jointly, on every branch of the main branch,

    T = O(n^6 2^((156/125) sqrt n)),  S_C = O(n^3 2^((156/125) sqrt n)),  S_Q = O(n^2 2^((156/125) sqrt n)),  Q = O(n^3 2^((156/125) sqrt n)).

## 15. Exact growth indices and declared envelopes

Since 5/4 - 156/125 = 1/500 and n^6 2^(-(1/500) sqrt n) is bounded over n >= 1, the bounds of Section 14 give each resource = O(2^(a0 sqrt n)),
with a0 = 5/4. The finite branch contributes only an absolute constant. The four declared envelopes are all B(n) = 2^((5/4) sqrt n). Then
log2 B = (5/4) sqrt n, log2 log2 B = (1/2) log2 n + log2(5/4), and g(B) = lim log2 log2 max(4, B(n)) / log2 n = 1/2 exactly. The index holds
for this fixed exact coefficient; it does not rely on a guessed constant. The structured objects in submission.json are exactly these envelopes.

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does not assert that robustness is impossible.

## 17. Scope and limitations

- This does not reach the research goal 2^(O(n^(1/3))); the time growth index is 1/2, as in HPC-127 and the earlier accepted submissions
  at this level. The improvement over HPC-127 is in the coefficient of sqrt n: 5/4 against 127/100, on all four resources.
- It is not an improvement in every resource over every row: S_Q is 2^(Theta(sqrt n)), as in HPC-127, whereas pure collimation uses O(n)
  qubits, and S_C and Q are also 2^(Theta(sqrt n)). The result is a different tradeoff, not a dominance claim over those submissions.
- The main-branch threshold n >= 2^28 and all polynomial factors are unoptimized.
- The value a0 = 5/4 is one explicit choice. The same construction with other parameter ratios should allow coefficients down to about
  1.24388, but that is motivation only and is not claimed here.
- Only the three-qubit instrument TRIAD is used. Nothing is claimed about instruments on more qubits.
