# Complete reference source

Current replacements: virtual2.md (schedule/supplier), distance_decoder.md
(block recovery), bucket_level.md (pool), window_merge.md (merges),
perm_fw.md (instrument), verified_extract.md and approx_estimate.md (LE),
seed_retry.md (key cap), proof.md (bank), typed_dispatch.md (controller),
native_ops.md (physical source/tree/windows). All proofs are reproduced.
Historical credits below refer to original authors; no verdict is a premise.
Standalone reference costs are conservative, separate from the physical ledger.

--- BEGIN COMPLETE VIRTUAL SOURCE ---

# IFC-LIMIT-E: F-LIMIT with a capped chunked pool and implicit-fiber four-input merges above the cap

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N), sig = 209/181 and e = 262087/226974.
The single algorithm IFC-LIMIT-E below receives N in binary and fresh independent copies of
rho_s, and outputs the entire s with unconditional probability at least 1 - 2^-7 > 2/3.
On EVERY execution branch (every failure, discard and abort included) it satisfies jointly (Section 14)

    T = O(n^(6+alpha)(log n)^2 2^(e sqrt n)),   Q = O(n^(3/2+alpha) 2^(e sqrt n)),   S_Q = O(2^(sig sqrt n)),   S_C = O(2^(sig sqrt n)).

Here alpha=1252597/2620860 (a conservative common bound); source exponent uses9843/873620. The growing-group RHO bound is proved in Section 8.
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
    z=ceil(log2 r), A=ceil(262087r/453948+(9843/873620)z+64), v=(14z+14)//15, ell=H0=A, dl=A+v,
    cb = floor(209r0/181) - 40 Lg,  Lam = cb - kappa - 4,  a = Lam - dl,  JI = ceil((H0 - a)/2),  H = a + 2 JI.

So there are ell FW LEVELS, each run on CHUNKS of at most 2^cb qubits (Section 7.3); a collimation tree with a
binary levels (Phase A) and up to JI four-input levels (Phase I), of height at most H; leaf tables built from dl
qubits; and no stored table longer than 2^Lam. The size facts of Section 8 give a >= 1, JI >= 2, 2 JI <= Lam + 1,
dl >= kappa + 2, H0 <= H <= H0 + 1. Internal/root failure bounds are CorollaryB.3 of window_merge.md.

## 1. Provenance

The complete retained bank, framework, cell, capped-pool, tree and merge
lineage is consolidated in proof.md Section1, including every original
submission locator and feature/author credit. Historical first-person
claims refer to original authors. The current replacements are explicit;
no prior verdict or motivational yield integral is a proof premise.

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

## 5. Current label extraction LE

verified_extract.md gives the complete normative high-confidence
catalytic Fourier estimate, its exact source channel, uniform guards
and global error coupling. approx_estimate.md reproduces its one-time
constant-angle Clifford+T compiler/certification. No verifier, local
RUN fallback or fallback counter is executed. Before ANY source a
failed current guard selects the complete exhaustive problem branch.
The fast branch acquires no extra copies for LE. Its one-time gradient
preparation, all estimate ancillas and all internal outcomes are omitted
from outer logical conditioning; ideal-gradient/reference-label coupling
costs less than2^-40, within the retained2^-10 allowance.

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
FW (Lemma 7.1), whose logical cell instrument is proved unchanged in perm_fw.md.

Throughout, w = 2^ceil(log2 n) is the GROUP SIZE and q = w/2. Thus n <= w < 2n on the main branch. Put b_w=log2 w=ceil(log2 n). This group size is generated from n, not fixed advice.

### 7.1 The permutation-seed instrument FW

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

The exact current realization is perm_fw.md Section8: a coarse kind
measurement followed by the linear pair/Ev circuit or a fresh uniformly
prepared permutation and original canonical matching circuit. The joint
kind-plus-cell instrument is exactly the same cell family. There are no R_N registers or mixed-radix PREP retries.
PREP retries fresh short keys with the global counters/cutoff of seed_retry.md.
Accepted seeds are exact; the global cutoff event has probability below2^-80.
The full coherent circuit, explicit sorting/joins, arbitrary-input Kraus
proof, c_F capacity and structural-work bound are reproduced there.

5. Post-processing. For each pair {a, b} of C with a < b: apply CNOT with A_a as control and A_b as
   target; A_b is then exactly |1>; apply NOT to it and release it. A_a is a GOOD output with table
   (t0^a + t1^b, t1^a + t0^b). If C has a block Bl = {c_0 < c_1 < ...} (Bl = all of [0,w) for Ev),
   apply CNOT A_(c_0) -> A_(c_i) for each i >= 1; these are then exactly |0>; release them. A_(c_0) is
   the RECYCLED output with table (sum_(c in Bl) t0^c, sum_(c in Bl) t1^c). The qubits unconstrained by
   C (w - 2 of them for a pair cell) are RETURNED with their tables unchanged.
So a pair cell yields one good output and returns w - 2 qubits; a matching cell with u pairs yields u
good outputs and one recycled output; Ev yields one recycled output.


Lemma7.1 (FW). Conditional on this seed request returning a seed, for every joint input
state the measured cell instrument has Kraus operators c_(C,z) Pi_C on
the data and identity on spectators, with sum_z |c_(C,z)|^2=y_C. Every
private ancilla is reset/released. On equal-amplitude product phase
inputs, (a) Pr[C]=y_C|C|/2^w, giving pair total(w-1)/w, matching total
pi_u=2 C(w,u)(q-u)^2/(q^2 2^w) and Ev probability2^(1-w).
Private outcomes conditional on C are independent of labels and phase:
for a pair T=0 and the seed is uniform S_w; for a matching T is uniform
D_u and its canonical seed is uniform G_u of perm_fw.md; for Ev both
original ticket and seed are uniform. (b) The retained postprocessing
gives exactly the original independent good, recycled and returned
phase qubits with the stated tables. (c) This instrument and zero-release
claim hold on arbitrary input states, not merely product phase states.

Proof. perm_fw.md Section5 proves each Kraus factor and that its private
state is independent of x within C, by an explicit bijection of seed
fibers onto G_u. Applied to sum_x|x>|R_x>, this gives c Pi_C directly.
For product phases every computational-basis amplitude has magnitude
2^(-w/2), so Pr[C]=y_C|C|/2^w; |P_ab|=2^(w-1), |Q|=2^(u+1), |Ev|=2.
Incidence(I2) gives the displayed matching total. A pair enforces
x_a!=x_b, so its CNOT makes the released target exactly1; the subsequent
NOT makes0. Bl enforces all its bits equal, so its CNOTs make every
released nonfirst bit0. This holds for arbitrary spectators/input.
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

Lemma9.2 (pool yield). In the ideal outer run, omitting the global key
cap and private retry state, a batch's pool-yield abort probability is
at most2(ell+1)C_0 exp(-2^H/(10 ell^2 w^2)).
Proof. Lemma7.3(e), with C_ell>=2^H. The global key-cap failure is a
separate2^-80 event, not a conditional per-run bound. QED.

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

S_Q. By Lemma 7.3(c) the pool, buffers and final pool hold at most 3 (ell + 1) 2^cb <= 4 r 2^cb qubits. An FW including its key PREP adds at
most c_F ancillas, all reset/released in |0> (Lemma7.1(c), perm_fw.md). The depth-first stack
holds at most four index registers per tree level, each of at most Lam <= r qubits, so at most 4 (a + JI + 1) r <= 4 r^2
qubits. A merge or MERGE4I adds O(sqrt n) qubits (its residue, rank, fresh window ticket and modular-arithmetic registers). LE including its guarded estimate and transforms use O(n),
reset between uses. So S_Q <= 4r2^cb+O(n^3) = O(2^(sig sqrt n)) by (F1).

S_C. Each pool level stores its buffer, chunk, LIVE heap, OUTPUT list and fixed key-bucket/item scratch arrays, each at most 2^(cb+1) rows of O(n)
bits (Lemma 7.3(c)); the final pool list has C_ell <= 2^cb rows. The tree stores at most four finished tables per level,
each of at most 2^Lam rows of 3n bits, MERGE scratch of O(2^Lam) rows, and MERGE4I scratch (sort orders, runs, heaps,
Buf, Tl and block table) of at most 4 L + 2 Cp + 2^lam' <= 2^(cb+1) rows (Section A; L = 2^Lam, Cp <= 2^cb). The
decoder stores K triples and K residues of O(n) bits; verified LE uses
O(n log n) ordinary reference scratch, including windows and counters. So every array has at most 2^(cb+1) rows of at
most 12n bits, and S_C = O(n r 2^cb) = O(2^(sig sqrt n)).

Reset-completion work. A key attempt or FW Boolean body uses
O(n(log n)^3) actual wires, not the unused c_F capacity. All are
initialized/reset/released explicitly. Their global count and uniform
emission are included in seed_retry.md; private retries may concentrate
in one call, so no fixed per-FW retry-work bound is used.
Transforms and LE have O(n) scratch and source-cleanup qubits per
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

Core steps, globally rather than a per-chunk retry estimate. The exact
attempt/request bounds of seed_retry.md and the local circuits in
perm_fw.md/verified_extract.md give structural work
C_str=O(n^(5/2)log n C_0+n^(7/2)2^(H+dl))+poly(n).
This includes all source tests, failed keys, counters, metadata/label
bit work, tree skeletons and decoder enumeration. It holds on every
actual branch; private retries may concentrate in one call.

For completeness the tree raw sum is as follows. At most C_ell/dl
LEAF calls cost O(n2^dl) each. Binary level i attempts consume disjoint
2^(i+1)dl pool inputs and cost O(n2^(dl+i)) each; PhaseI level j consumes
disjoint4^(j+1)2^a dl inputs and costs O(n2^l_j). The identity
l_j-2j-2-a=dl-1 gives O(n C_ell 2^dl/dl) per level. Summing at most r
levels and using dl>=r/2, C_ell=O(n2^H), yields O(n^2 2^(H+dl)) per
batch. Keeping an extra n full uniform-emission allowance and O(r)
batches yields the conservative n^(7/2) term above. Current exact
short-residue decoding is specified in distance_decoder.md; its weighted
cost is O(n^2 C_0)+poly(n), with all interval initialization charged.
The conservative structural reference bound above still covers it.
No candidate integer selects a memory address.

A full standalone reference handle has O(r) bits; even allowing O(n)
extra uniform address/argument bit work for every structural step is
sufficient, including schoolbook address arithmetic and full data-field
copies. Therefore C_P<=O(n C_str)+poly(n)
=O(n^(9/2+c+1/2)(log n)^2 2^((262087/226974)sqrt n)). The structural count itself is
proved from deterministic raw counts in seed_retry.md and the displayed
tree/decoder sums, independently of this loose reference relaxation.
The physical algorithm uses that direct count, not this full-handle
standalone upper bound. Peak and source bounds above remain unchanged.

T. By(F6), the standalone address fee is O(r). Thus
T_P=O(n^(5+c+1/2)(log n)^2 2^((262087/226974)sqrt n)+nQ),
which in particular satisfies the retained looser O(n^(6+c+1/2)(log n)^2
2^((262087/226974)sqrt n)) envelope. All pointer/field work and failures are counted.

Exponents. Put c=9843/873620, z=ceil(log2r), A=ceil(262087r/453948+c z+64).
v=(14z+14)//15, ell=H0=A, dl=A+v, H<=A+1, RHO^ell<=64*2^A.
Since A<=262087r/453948+c log2r+c+65,
 PP=O(n^c 2^((262087/226974)sqrt n)),
 2^(H+dl)=O(n^(c+7/15)2^((262087/226974)sqrt n)).
The conservative standalone bounds therefore are
 C_P=O(n^(9/2+c+1/2)(log n)^2 2^((262087/226974)sqrt n)),
 T_P=O(n^(6+c+1/2)(log n)^2 2^((262087/226974)sqrt n)),
 Q=O(n^(3/2+c)2^((262087/226974)sqrt n)),
 S_Q=O(2^(sig sqrt n)), S_C=O(2^(sig sqrt n)).

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
  trade-off: P's memories are 2^((1) sqrt n) while T and Q are 2^((262087/226974) sqrt n), against 2^((2887/2500) sqrt n) on all
  four for F-LIMIT.
- The group size w = 2^ceil(log2 n), the trim 40 Lg, the threshold n >= 2^40 and all constants (the per-attempt circuit capacity c_F of FW in particular) are unoptimized absolute
  constants.
