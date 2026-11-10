# Cyclic-window collimation and constant merge slack

P Section6.2 and SectionsA/B are now window_merge.md. Overlapping cyclic
windows remove incomplete-block failure. Fresh-digit variance bounds give
exponentially small internal failures with kappa=20; the root has a separate
constant-failure allowance in Lemma9.1. Section8 uses c=29/4 and Lam=cb-24.
All changed instruments and proofs are reproduced, not inherited as verdicts.

# Work-conserving key-bucket FW levels

P Section7.2 is now bucket_level.md. It removes round sorting, leaves
returned pair-cell records linked, and stops when no key has w live qubits.
The conditional yield proof, endpoint live bound and all new record costs
are reproduced there. The FW instrument and schedule are unchanged.

# Distance-amplified block recovery

Sections 10-13 strengthen source-coordinate distance and recover blocks of b0
bits rather than one bit per batch. Source labels in 2-adic blocks may have
higher independent bits beyond the held-out bit. The exact new source cap is
20rC_0+K. Section 14 charges O(sqrt n) batches and all candidate enumeration.

# Growing even FW groups

This variant sets w=2^ceil(log2 n) and uses RHO=2+8/r. Section 7 specifies
variable-width cell/ticket registers, a uniform Boolean-circuit generator and
its polynomial cost. Section 8 and Section 14 redo capacity, work and exponent
accounting for this choice. Historical provenance remains credited below.

# Schedule modification for the logarithmic-correction variant

This is the predecessor reference proof with the explicit parameter choice and
its capacity and exponent accounting replaced as stated in Sections 0, 8 and 14.
The coset transformations, instruments, merge algorithms, independence arguments,
cutoffs and decoders are retained. Historical provenance below names original authors.

# Reference algorithm P for IFC-BANK-E: the complete IFC-LIMIT-E proof (virtual storage model)

Everything after the marker line and the blank line following it, together with virtual2.md, distance_decoder.md, bucket_level.md and window_merge.md, is the complete
specification and proof of IFC-LIMIT-E, the reference algorithm P. IFC-LIMIT-E is not filed as a separate submission. Its
text is generated from our F-LIMIT proof (the reference algorithm of F-LIMIT-BANK), itself generated from qzv's HPC-127
proof (submission 2aad498c-d5e9-4f64-a222-3b2f7f961738), with the edits listed in its Section 1. virtual2.md holds the chunk and schedule sections; bucket_level.md holds
Section7.2, and window_merge.md holds current Sections6.2,A,B.

In this file "the algorithm" is P. Its resource statements (its Sections 0, 14 and 15) and its claims about classical
memory concern P in its own storage model, in which classical records are ordinary bits. The physical algorithm
IFC-BANK-E of proof.md executes P without change, but stores P's classical records differently. Its four resource
bounds are proved in proof.md, not here.

proof.md uses the complete reference bundle, including bucket_level.md and window_merge.md:
- the algorithm and its correctness (Sections 3-13, A and B);
- the parameters, the size facts and Y <= 2r (Section 8);
- the explicit success sum (Section 13);
- the allocation and cost bounds of Section 14, with exponent e = 7/6 and cap cb;
- Lemma 7.1(c) and step 5 of Section 7.1, the lifecycle of FW's qubits, and the constant c_F of Section 7.1;
- the register list and lifecycle of MERGE4I (Section A).

Historical first-person text below denotes the authors of IFC-LIMIT-E and of the works it credits. No earlier verdict
on any submission is a premise.

--- BEGIN COMPLETE VIRTUAL SOURCE ---

# IFC-LIMIT-E: F-LIMIT with a capped chunked pool and implicit-fiber four-input merges above the cap

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N), sig = 1 and e = 7/6.
The single algorithm IFC-LIMIT-E below receives N in binary and fresh independent copies of
rho_s, and outputs the entire s with unconditional probability at least 1 - 2^-7 > 2/3.
On EVERY execution branch (every failure, discard and abort included) it satisfies jointly (Section 14)

    T = O(n^(6+alpha)(log n)^2 2^(e sqrt n)),   Q = O(n^(3/2+alpha) 2^(e sqrt n)),   S_Q = O(2^(sig sqrt n)),   S_C = O(2^(sig sqrt n)).

Here alpha=29/4. The growing-group RHO bound is proved in Section 8.
All constants are absolute. Section 14 also gives the sharper facts used by proof.md: at most 4 r 2^cb pool qubits
are held at once, every classical array has at most 2^(cb+1) rows, and 2^cb <= n^-40 2^(sig sqrt n). The fifth claim
is the clean-input tolerance 0 (Section 16).

Notation:
- dn = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with
  s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known nonnegative integer. log means log2 unless stated otherwise.

Main-branch parameters, computed by exact integer arithmetic for n >= 2^40:

    r = ceil(sqrt n),  r0 = floor(sqrt n),  Lg = ceil(log2 n),  kappa = 20,
    ell = dl = H0 = ceil(7r/12+(29/4)ceil(log2 r)+64),
    cb = floor(1 r0) - 40 Lg,  Lam = cb - kappa - 4,  a = Lam - dl,  JI = ceil((H0 - a)/2),  H = a + 2 JI.

So there are ell FW LEVELS, each run on CHUNKS of at most 2^cb qubits (Section 7.3); a collimation tree with a
binary levels (Phase A) and up to JI four-input levels (Phase I), of height at most H; leaf tables built from dl
qubits; and no stored table longer than 2^Lam. The size facts of Section 8 give a >= 1, JI >= 2, 2 JI <= Lam + 1,
dl >= kappa + 2, H0 <= H <= H0 + 1. Internal/root failure bounds are CorollaryB.3 of window_merge.md.

## 1. Provenance and what is new

F-LIMIT is qzv's HPC-127 (public submission 2aad498c-d5e9-4f64-a222-3b2f7f961738 on this
challenge) with one change: its pairing stage (HPC-127 Section 7) is replaced by a stage built on an
instrument FW on w = w equal-key qubits, and the schedule is re-derived for it.
- Sections 2, 3, 4, 6, 11, 12 and 16 are HPC-127's text unchanged. Section 5 differs only in the
  algorithm name.
- Sections 9, 10 and 13 are HPC-127's text with these edits. Section 9: step 2 and Lemma 9.2 use
  the work-conserving FWLEVEL of bucket_level.md, the slot bound C_i/(4 w ell) and the bounds of Lemma 7.2. Section 10:
  the sigma-field, one sentence of the proof of Lemma 10.1 and one sentence of the incidence
  paragraph name FW and PREP outcomes and index maps instead of PAIR's. Section 13: the threshold
  2^40, the stage name, its abort term and the constant m >= 600000.
- Sections 8 and 14 keep HPC-127's structure with new constants: the growing-group ratio RHO=2+8/r, its uniform bound RHO^ell<=64*2^ell, and the slot rule, the capacity Lemma 8.1
  for the new ratios, and the exponents. Sections 1 and 7 are new; Sections 0, 15 and 17 carry the
  new name and constants.

Lineage. Our TRIAD-125 (f5b375dd-1e5c-4728-95dc-b855b2dc5827, three qubits) and G4-124
(b48a1af4-3e6b-45d7-8cdb-a414739ddc21, four qubits) make the same kind of replacement; the layout of
Sections 7, 8 and 14 (in F-LIMIT) and the phantom-outcome yield argument follow G4-124. HPC-127 restates the
framework of CS1 (AdamGagol, f1481815-9577-4990-abe3-7b79fa5d9284) in Sections 2-6 and 10-12, and its
Lemma 7.2 uses a bucket count of the kind also in PSieve (spariev, 4256e671-97b0-4f84-82ce-12aeee17224e).
Overlapping non-projective instruments with a phase-independent outcome law were introduced on this
challenge by 0xplemonade's CYC1 (7a4cecdc-7941-4027-8c95-8520de9fbcf3). mpjunior92's PART7, PART31 and
PART127 rows (1e083775-5d0a-4070-bcdc-ded8ada75d3a, 38897382-d7d7-44fe-8205-64ad028a41a5,
d444e283-4dcc-4836-a82b-bc1e6866e25b) are prior board work on the same cell family for odd group sizes;
FW is the even-size case, with its own realization and proof here, derived independently; no priority is claimed.
mpjunior92's PARTADAPT-193-TAGBANK (cfb1e549-2935-4d3f-a8b2-a01b125134ea) and PARTROOT196
(3315027c-4ec3-4352-80e5-f8f384e286f1) are prior board work on the case of a group size growing with n. Kuperberg (SIAM J. Comput. 35(1), 2005; arXiv:1112.3333) is the source of pairing and
collimation. These citations are context; every step used is proved below, and no earlier verdict is a
premise.

New here: the instrument FW for w = 2^ceil(log2 n) with its exact realization by a Hadamard ticket and uniform
registers prepared by repeat-until-success before the data is touched (Section 7.1); the closed form of
its yield ratio and the rational bound (7.4) (Lemma K); the distribution-free yield Lemma 7.2 with all
w-dependent constants; and the schedule of Section 8. Motivation only: a pool level costs log2 of the
net inputs per advancing output, 3 for HPC-127's PAIR and at most the variable RHO=2+8/r here, and the pairing-
then-tree yield integral turns this into a coefficient near 2/sqrt 3 = 1.1547. The theorem rests only
on the explicit schedule of Section 8. As in HPC-127 the pool is held coherently.

IFC-LIMIT-E edits. IFC-LIMIT-E is F-LIMIT (the text above, Sections 1-17 of our F-LIMIT proof) with three changes.
(1) Capped chunked pool. The FW stage runs every level on chunks of at most 2^cb qubits, demanded from below
through per-level buffers (new Section 7.3), so the pool holds O(r 2^cb) qubits instead of all C_0. Capping the
recycling windows of a pool at a fixed fraction of sqrt n, inside the counted bank, is prior board work: qzv's streaming
capped-slot pools SPC-127 (0efb267b-c55e-49cb-946b-ea3ced57f221) and SPC-M1 (fdacb3e2-9074-4dcc-9389-887574dd25e3), whose
SPQ rows trade S_Q against Q and T, and mpjunior92's banked versions SPCM1-TAGBANK (0118d724-3ac4-46a7-bf5b-a63539927aa0)
and SPCC90-TAGBANK (f9efd397-8230-4424-9098-2a31d11846c8). The fixed-size chunks with
yield and run caps (Lemma 7.3), proved conditional on everything before each run, are written here.
(2) Implicit-fiber merges above the cap. Above table exponent Lam the binary MERGE is replaced by MERGE4I, the
four-input merge with streamed, unstored pair fibers of our IFC1 (1294d17f-2acf-4e10-9996-6b4375388f49), which descends
from e-man07's CW1 (cfe82a87-0d65-454e-b1df-4789dc95aab4) and MW4 (33a6df9d-08d8-488b-a3f7-01f5f32373a4); its current cyclic-window text and fresh-digit failure bounds are in
window_merge.md, retaining the original implicit-fiber listing lineage. Capped IFC trees inside the counted bank are prior board work: mpjunior92's
IFCS1310-TAGBANK (fc8aa038-cba6-42bf-a317-df1c36c956f7) and its siblings. New here is the composition with a recycling
pool below the tree (Phase A starting at dl rather than at kappa + 1) and its schedule.
(3) Schedule. Section 8 is new (parameters, chunk sizes, tree shapes, capacity Lemma 8.1); Sections 9, 13 and 14 are
re-derived for it; Sections 10 and 11 carry the edits for MERGE4I and the on-demand supplier. Sections 2-6, 7.1, 7.2, 12 and 16
are F-LIMIT's text unchanged.


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

Explicit reset completion. After allocating each fresh ZERO ancilla, reset
each of its qubits before first use, even if its initial state is already
zero. Before every logical release, reset the released qubit with no recorded
outcome. These resets are part of P and its core-step count. Fresh source
copies are exempt from the initialization rule: their supplied state is never
reset before use. Unused capacity padding is not allocated as reference scratch.
Initialization resets act identically on the fresh zero factors, and a reset
followed by release has exactly the same reduced channel on spectators as
tracing out that qubit. Thus this uniform completion preserves all source
requests, recorded outcomes and output laws. Section14 charges every added
reset and its uniform handle generation; the same resource envelopes hold.

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

Cost per call: 2(J_e+1)F tests. The gate/data skeleton uses O(n^2 h_e)
steps. Include O(sqrt n) core work per emitted gate to copy full reference
wire handles and perform uniform index arithmetic. Since h_e=O(sqrt n),
O(n^3) core steps per call is a conservative full allowance, also covering
Mult_alpha and source bookkeeping. Quantum scratch is O(n) and ordinary
reference classical scratch is O(n). Address fees remain charged by (2.1)
and, in the physical implementation, by the bank ledger.

IDEAL run. The ideal run is IFC-LIMIT-E in the latent-label model with every LE output replaced by the
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

### 6.2 MERGE and 6.3 MERGE4I

The complete cyclic-window binary MERGE (P Section6.2), MERGE4I (P SectionA),
measurement/failure identities and fresh-digit LemmasB.1–B.3 are in
window_merge.md, a required part of this reference program. It replaces
incomplete-block rejection by the exact cyclic-window instrument, adds a
lower pair-fiber cutoff and uses constant kappa=20. There is no retained
normative power-of-two block-truncation routine.


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

Throughout, w = 2^ceil(log2 n) is the GROUP SIZE and q = w/2. Thus n <= w < 2n on the main branch. Put b_w=log2 w=ceil(log2 n). This group size is generated from n, not fixed advice.

### 7.1 The instrument FW

Uniform registers. For an integer N with 3 <= N <= w - 1 put j_N = ceil(log2 N) <= b_w and
U_N = N^(-1/2) sum_(v<N) |v>, a state of j_N qubits. PREP(N): up to 3r times (r from Section 0), put
j_N fresh qubits in |0>, apply H to each, XOR the flag [v < N] into a fresh qubit (a comparison with a
constant, computed cleanly with O(b_w) Toffoli/CNOT/NOT gates), measure the flag and reset it; if it was
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

Cell register. P has w fields of b_w+1 qubits; the code of a cell C is p(C) with p_i = the other element of
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

Circuit. Ancillas, all fresh |0>: a 2(b_w-1)-qubit ticket register T, the registers R_3, ..., R_(w-1)
(together the register R, at most b_w w qubits), the cell register P, and scratch.
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

Gates and uniform generation. Steps 2 and 3 XOR Boolean functions of x,T,R,P into
registers not among their inputs. Popcount, prefix counts, ranks, list removal and
selection without replacement are implemented by a fixed family of ordinary Boolean
circuits. One explicit implementation stores each of w positions in b_w+1 bits,
scans all positions for each of at most w removals, and updates comparisons, ranks
and selected values with ripple circuits. It uses O(w^2 b_w^2) <= O(w^3) Boolean gates
for w >= 2^40. Compute every Boolean gate into a fresh scratch bit, copy its output,
then reverse to clear scratch. AND, XOR and NOT use Toffoli, CNOT and X exactly.
For explicit capacities, schoolbook comparators, prefix/rank scans and at most w
list removals give at most 2^12 w^2(b_w+1)^2 Boolean gates. Since (b_w+1)^2<=w
for w>=2^40, reversible compute/copy/uncompute and constant-size gate decompositions
fit c_F=2^20 n^3 gates and scratch qubits (w<2n). These generous constants also
cover the cell/ticket and uniform registers, flags and ordinary ripple scratch.
A uniform nested-loop generator implements the fixed ripple/comparison/scan
circuits using O(log n)-bit local indices. Schoolbook offset arithmetic costs
O((log n)^2) bit operations per emitted gate. Reading or emitting the actual
reference wire handles costs at most O(sqrt n) bit operations, because the
reference address span has O(sqrt n) bits. This is explicitly counted, rather
than assuming that every wire address is polynomial in n. Since (log n)^2
is O(sqrt n), generation costs O(sqrt n) core steps per gate. Thus the
O(n^2(log n)^2) Boolean gates, reversible initialization and cleanup cost
O(n^(5/2)(log n)^2) core steps per FW. The additional address fee is charged
by (2.1), and in the physical implementation by the bank ledger.

PREP uses O(w r log w) gates and at most O(w r log w sqrt n) core work
including emission. Label-table updates and handle bookkeeping also fit
O(n^(5/2)(log n)^2). Scratch remains bounded by c_F=2^20n^3; the actual
circuit need not allocate every wire in this conservative capacity. The
controller emits its circuit online and stores no growing ordinary transcript.

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
- the terms with x in Ev give |+>^(2(b_w-1))_T ((x)_N U_N) |p(Ev)>.
Every x in a matching cell with u pairs has u(x) = u by (I2), so after measuring P = p(C) the state is
- q^(-1) (Pi_C (x) I) Psi (x) |0>_T (x)_N U_N for a pair cell,
- q^(-1) prod_(N in S_u) N^(-1/2) (Pi_C (x) I) Psi (x) (sum_(t in D_u) |t>) |0>_(S_u) (x)_(N not in S_u) U_N
  for a matching cell, and
- (Pi_Ev (x) I) Psi (x) |+>^(2(b_w-1)) (x)_N U_N for Ev.
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

Lemma K (yield ratio). For the n-dependent even power-of-two w above, let
gbar=E[gamma], rhobar=E[rho] under (7.2), and b=C(w,w/2)/2^w. Then
rhobar=3(w-1)/w and gbar=3/2-1/w-b. The same binomial argument below proves
b <= (3w/2+1)^(-1/2). Since w>=n>(r-1)^2, r>=2^20,

    b <= 2/r, 1/w <= 4/r^2, gbar >= 3/2-3/r >= 1,
    rhobar/gbar <= 2/(1-2/r) <= 2+8/r =: RHO.                 (7.4)

Also gbar<=3/2. RHO is the exact rational 2+8/r, computed by integer arithmetic.

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
Finally, the displayed bound gives gbar>=3/2-2/r-4/r^2>=3/2-3/r.
Since rhobar<=3, rhobar/gbar<=2/(1-2/r). For r>=4, multiplying by the
positive denominator shows 2/(1-2/r)<=2+8/r. This proves (7.4) uniformly. QED.

### 7.2 Work-conserving FWLEVEL

The complete specification, explicit AVL/FIFO implementation, Lemma7.2
yield proof, cost and capacity analysis are in bucket_level.md, a required
part of this same reference program. There are no fixed sorting rounds.

### 7.3 The chunked pool

Section 7.3 (the chunked pool, REQUEST and Lemma 7.3) is in virtual2.md.

## 8. The schedule

Section 8 (constants, the bracket (8.5), the size facts (F1)-(F6), level capacities, (8.4), Lemma 8.1, the tree shapes and
bit allocation, and the MERGE4I parameters) is in virtual2.md.


## 9. BATCH(supplier, B)

Input: a supplier of LEAF QUBITS: positive qubits with phase exp(2 pi i k th) for a fixed real th and a known label k,
where in the ideal run labels are independent uniform on [0,2^d_src), with B+1<=d_src<=n. The odd part uses d_src=B+1, while a 2-adic block uses d_src=wd. Leaves are served in chunks of D_0 on request.
Output: K measured-ready roots, or ABORT. A leaf qubit is a labeled qubit with table (0, k).

1. POOL. Form the final pool, C_ell qubits collimated to pp_ell, by REQUEST(ell) (Section 7.3), and release the
   buffers. An ABORT of the supplier or of Section 7.3 is an ABORT of the batch.
2. TREE (shape and bits from Section 8). VEC(0) = LEAF: take the next dl qubits of the final pool (ABORT if fewer
   remain). Their qubits form the index register, bit j = qubit j. With tables (t0_j, t1_j), build lab[0] = sum_j t0_j
   and lab[x + 2^j] = lab[x] + t1_j - t0_j for x < 2^j. The table has length 2^dl, is exactly the tensor product state
   in the ideal run, and is collimated to tp_0 because every difference is 0 mod 2^(tp_0).
   A binary level i (input exponent dl + i) produces its output by: repeat X1, X2 = two outputs of the level below
   (LEAF for i = 0), out = MERGE(X1, X2; p, b_i, lam'), with p its start position, lam' = lam_(i+1) or 1 at the
   binary root, until out != FAIL.
   A Phase I level j produces its output by: repeat X1, X2, X3, X4 = four outputs of the level below (Phase A level
   a - 1 for j = 0), out = MERGE4I(X1, X2, X3, X4; p, r_j, b_j - r_j, lam', l_j) (Section A, parameters of Section 8),
   until out != FAIL.
   A root is an output of the root level, evaluated depth-first. Run it K times, or ABORT if the pool runs out.

Root. A root is a two-entry table with lab[0] = lab[1] mod 2^B, so its ideal state is, up to global phase,

    (|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2,   W = (lab[1] - lab[0])/2^B, a known integer.     (9.1)

Label bound. Each leaf qubit enters a table entry at most once and all pool qubits are distinct, so every label in
the batch is a sum of at most C_0 leaf labels below 2^d_src, with d_src<=n (Lemma 7.3(d)). Thus every label is below 2^(Y+n+1), which
fits in 3n bits by Y <= n, and

    |W| <= 2 C_0 <= 2^(Y+1) for odd-part batches. For a 2-adic block, |W|<=C_0*2^b; only W mod2^b is used.                                                        (9.2)

Lemma9.1 (no pool exhaustion). In the ideal run, conditional on the
logical history before tree construction except label bits at or above
pp_ell of the final pool leaves, exhaustion before K roots has probability
at most r^-63. LE internal records are excluded, as in the held-out-bit
proof; physical RAW transcripts and high input-table fields are not part
of this conditioning.

Proof. Extend the pool by phantom leaves with independent uniform digits
above pp_ell, as in the retained argument. CorollaryB.3 of window_merge.md
bounds each internal attempted merge by p<=1/(4r), conditional on its
logical past, and the unique root by p_root<=1/16. Past failures consume
fresh inputs that are never reused. The applicable history is contained
in the lemmas' Hp sigma-field: only lower collimation digits of current
inputs have driven previous decisions. The tower property therefore gives
these conditional failure bounds at every attempt. Phantom leaves are
used only for consumption, not for the stronger real-root distance claim.

List d<=a+JI<=r merge levels from root downward, with arities b_v in{2,4}
and product at most2^H. Set m_0=K and analysis allowance A_0=2K for the
root; m_1=b_0 A_0. Among its first2K potential attempts, conditional failure
indicators have mean bound1/16. Iterated conditional moment bounds give
probability of at leastK failures at most(2 exp(1)/16)^K<2^-K<=r^-64.
Thus that root allowance produces K successes except on this event.

For v=1,...,d-1 define z=ceil(log2 r),
A_v=ceil((1+2/r)m_v+64z), m_(v+1)=b_v A_v. With u_v=A_v-m_v,
conditional failure bounds give E exp(tF)<=(1-p+p exp(t))^A_v.
Exponential Markov and u_v>=2m_v/r+64z show

 Pr(F>=u_v)<=(exp(1)A_v/(4r u_v))^u_v<=2^-u_v<=r^-64,

since A_v/(4r u_v)<=1/8+1/(4r)<1/7 and exp(1)<11/4. Indicators
may be padded by zeros after completion; no independence of adaptive
attempts is required. A union over d<=r levels costs at most r^-63.
On the complementary event each level supplies its requested outputs
within its allowance, by demand induction from the root.

Let P_v be the product of the first v arities. P_v>=2^v, and after the
root m_1/P_1=2K. For internal levels,
m_(v+1)/P_(v+1)<=(1+2/r)m_v/P_v+(64z+1)/P_v.
The geometric sum and d<=r give m_d/P_d<8(2K+128z+2)<17K,
using exp(2)<8, z<=r and K>=2^14r. Therefore fewer than17K2^Hdl
pool qubits suffice, below C_ell=256K2^Hdl. The real and phantom runs
coincide until exhaustion, so exhaustion implies a tail event. Over at
most5r batches its contribution is at most5r^-62<2^-10. These allowances
are analysis-only; the actual finite pool still caps every branch. QED.

Lemma 9.2 (pool yield). In the ideal run, step 1 aborts other than by the supplier with probability at most
(ell + 1) C_0 (w 2^(-3r) + 2 exp(-2^H/(10 ell^2 w^2))).

Proof. Lemma 7.3(e), with C_ell >= 2^H. QED.

## 10-13. Distance, decoders and complete algorithm

Sections 10-13 are in distance_decoder.md, a required part of this same
reference specification and proof. They establish the source-coordinate
distance, strengthened held-out-bit law, odd-stage jumps, blockwise 2-adic
likelihood recovery and source cap Qcap=20rC_0+K. No old single-bit decoder
is selected in this configuration.

## 14. Resources on every main-branch execution

Throughout, K = O(sqrt n); dl, ell, Lam, H, a, JI = O(sqrt n); C_ell = O(n 2^H) by (F4); and, writing PP = RHO^ell 2^H,
C_0 <= 64 RHO^ell C_ell = O(n PP) by Lemma 7.3(d). All fixed loops, caps and aborts below hold on every
branch.

Q. Q<=Qcap=20rC_0+K=O(n^(3/2) PP).

S_Q. By Lemma 7.3(c) the pool, buffers and final pool hold at most 3 (ell + 1) 2^cb <= 4 r 2^cb qubits. An FW adds at
most c_F ancillas, all released in |0> (Lemma 7.1(c)), and PREP uses O(1) fresh qubits per try. The depth-first stack
holds at most four index registers per tree level, each of at most Lam <= r qubits, so at most 4 (a + JI + 1) r <= 4 r^2
qubits. A merge or MERGE4I adds O(sqrt n) qubits (its residue, rank, fresh window ticket and modular-arithmetic registers). LE and transforms use O(n),
reset between uses. So S_Q <= 4r2^cb+O(n^3) = O(2^(sig sqrt n)) by (F1).

S_C. Each pool level stores its buffer, chunk, LIVE heap, OUTPUT list and fixed key-bucket/item scratch arrays, each at most 2^(cb+1) rows of O(n)
bits (Lemma 7.3(c)); the final pool list has C_ell <= 2^cb rows. The tree stores at most four finished tables per level,
each of at most 2^Lam rows of 3n bits, MERGE scratch of O(2^Lam) rows, and MERGE4I scratch (sort orders, runs, heaps,
Buf, Tl and block table) of at most 4 L + 2 Cp + 2^lam' <= 2^(cb+1) rows (Section A; L = 2^Lam, Cp <= 2^cb). The
decoder stores K triples and K residues of O(n) bits, and LE O(n) bits. So every array has at most 2^(cb+1) rows of at
most 12n bits, and S_C = O(n r 2^cb) = O(2^(sig sqrt n)).

Reset-completion work. The actual FW scratch/cell/ticket family has
O(n^2(log n)^2) wires, not its unused c_F capacity. Initializing and releasing
these wires by explicit resets, with O(sqrt n) handle generation per reset,
costs O(n^(5/2)(log n)^2) per FW, already within its listed allowance.
PREP adds O(log n) reset wires per try, within its existing gate/emission
budget. Transforms and LE have O(n) scratch and source-cleanup qubits per
copy; their extra O(n^(3/2)) reset/emission work fits the O(n^3) per-copy
allowance. Binary/four-input merges use O(sqrt n) scratch and input-index
qubits per attempt, whose added reset/emission work is O(n), below their
listed table/lookup budgets even when a FAIL takes an early exit. The
full primitive upper bound is charged to every attempted call as before.
LEAF allocates no qubits. Coins have constant scratch. Pool/buffer cleanup
resets at most the bounded number of supplied pool qubits, within the
supplier/FW allowances. No added reset has an uncharged uniform address.
The additional cyclic-window modular circuit and local inverse table are
polynomial per merge and fit the existing table-work budget at lam>=r/2
(window_merge.md). Summing with the same deterministic call/consumption
caps preserves the core ledger below, with a larger absolute constant.

Core steps, per batch.
- Acquisitions: at most 4 C_0, each O(n^3) core work including LE and uniform emission: O(n^3 C_0).
- FW stage: a chunk costs O(n^(5/2)(log n)^2 D_i) core steps by Section 7.2,
  including every gate-generation bit operation. Sum Rc_i D_i<=C_0 across
  ell=O(sqrt n) levels: one batch costs O(n^3(log n)^2 C_0).
- Tree: at most C_ell/dl LEAF calls at O(n 2^dl) each. An attempt at binary level i consumes 2^(i+1) dl pool qubits and
  an attempt at Phase I level j consumes 4^(j+1) 2^a dl, which no other attempt at that level uses (inputs of a failed
  attempt are discarded). A binary attempt costs O(n 2^(dl+i)) (Section 6.2) and a Phase I attempt O(n 2^(l_j))
  (Section A: (L + mX) lam (lam + b) = O(n 2^(l_j)), Cp lam = O(n 2^Lam), 2^lam' (lam + n) = O(n 2^Lam)). Since
  l_j - 2j - 2 - a = dl - 1, every level costs O(n C_ell 2^dl/dl), and all a + JI <= r levels cost
  O(r n C_ell 2^dl/dl)=O(n^(5/2)2^(H+dl)) skeleton steps.
  Allow an extra O(n) factor for full uniform wire emission and control in
  the binary/four-input primitives: O(n^(7/2)2^(H+dl)) per batch. This generous
  allowance covers even a full O(n)-bit argument copy for every listed step.
- Decoder per stage: at most 2^(Y+8) odd-part candidates or 2^b 2-adic candidates.
  Since b<=ell/2<=H<=Y, both are within the same bound. K residues of O(n) bits
  are updated per candidate, giving O(K n 2^Y)=O(n^(3/2)C_0) core steps. The
  new b0/bit-progress arithmetic uses only polynomial work. An additional O(n)
  controller/address-emission allowance gives O(n^(5/2)C_0) per batch; over
  O(sqrt n) batches this remains below the FW term.

Over at most 5r=O(sqrt n) batches, plus polynomial setup, core steps total O(n^(7/2)(log n)^2 C_0+n^4 2^(H+dl)) + poly(n). Every loop is either
fixed-length or consumes pool qubits or acquisitions, so every branch terminates.

T. By (F6) and the space bounds, log2(S_C + S_Q + 2) = O(sqrt n). By (2.1),

    T_P=O(n^4(log n)^2 C_0+n^(9/2)2^(H+dl)+nQ)=O(n^6(log n)^2 PP).

Exponents. Put c=29/4, z=ceil(log2 r), D=ceil(7r/12+c z+64), e=7/6,
alpha=c. Since RHO=2+8/r and ell=D<=r, RHO^ell<=64*2^ell. Also H<=D+1
and D<=7r/12+c log2 r+c+65. Both PP and 2^(H+dl) are therefore
O(r^(2c)2^((7/6)r))=O(n^c 2^((7/6)sqrt n)). Combining the exact core
ledger and deterministic source cap gives

    C_P=O(n^(9/2+c)(log n)^2 2^((7/6)sqrt n)),
    T_P=O(n^(6+c)(log n)^2 2^((7/6)sqrt n)),
    Q=O(n^(3/2+c)2^((7/6)sqrt n)),
    S_Q=O(2^sqrt n), S_C=O(2^sqrt n).

which implies the bounds of Section 0.

## 15. Exact growth indices and declared envelopes

The proof.md envelopes are not P's. For P, the bounds of Section 14 have growth index 1/2 each: for fixed c > 0 and
any fixed rational a,q, log2 log2 max(4,n^a(log2 n)^q 2^(c sqrt n))=(1/2)log2 n+log2 c+o(1). The finite branch contributes only an
absolute constant.

## 16. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does not assert that robustness is impossible.


## 17. Scope and limitations

- This does not reach the research goal 2^(O(n^(1/3))); the time growth index is 1/2, as in HPC-127. The result is a
  trade-off: P's memories are 2^((1) sqrt n) while T and Q are 2^((7/6) sqrt n), against 2^((2887/2500) sqrt n) on all
  four for F-LIMIT.
- The group size w = 2^ceil(log2 n), the trim 40 Lg, the threshold n >= 2^40 and all constants (the gate count c_F of FW in particular) are unoptimized absolute
  constants.
