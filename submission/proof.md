# CS1-SBRS: plateau collimation with a strided seed and backward blocks

## 0. Theorem and notation

For every integer N>=2 and every s in Z/NZ, put n=ceil(log2 N).
The single CS1-SBRS algorithm below receives N in binary and fresh
independent copies of rho_s. It outputs the full secret s with
unconditional probability at least 1-2^-8>2/3. On EVERY branch,
including failures, retries, discards, and aborts, it satisfies jointly

    T   = O(n^(13/4) 2^(2 sqrt n - n^(1/4))),
    S_C = O(n^2 2^(sqrt n)),
    S_Q = O(n),
    Q   = O(n^(3/2) 2^(sqrt n)).

All outside constants are absolute and independent of N, s, and all
outcomes. The displayed envelopes are asymptotic. The n=1 case uses the explicit finite branch. For intermediate formulas,
read logarithmic cost factors as max(1,log2 n).
The time envelope has exact rational exponential coefficients 2 at
n^(1/2) and -1 at n^(1/4). Classical space and source copies each have
coefficient 1 at n^(1/2). Their growth
indices are 1/2, 1/2, 0, and 1/2. Source tolerance is zero.

Notation:
- d=floor(log2 N); N=2^a2 M with M odd; L=log2 n.
- s1=s mod M; s2 in [0,2^a2) satisfies s=s1+M s2 modulo N.
- omega=exp(2 pi i/N); a data basis state |u>, 0<=u<N, uses n qubits.
- A label is a known integer. W denotes an integer frequency multiplier.
- T denotes total charged work. hd denotes Hamming distance.

## 1. Sources and direct material use

This proof directly adapts this account's frozen CS1-SBR source snapshot,
with proof SHA-256
`840976d544f7e080960ecc0ae76bb960776536c350633297d14642582eb546a2`
and claims SHA-256
`e738e1532d74ad3a30af7c3ff0a74c7bc56b3ee371166c0a3a34eb1a7b23aa9c`.
It supplies the tree, merge, source operations, ordinary fallback decoder,
cutoffs and resource accounting reproduced below. This exact snapshot
is unsubmitted and has no public URL.

The strided terminal seed, backward blocks and analysis pool directly use
this session's stride_decoder_transfer.md Sections 1--7, proof SHA-256
`abe770f323abf2b161678df4ee06d6dd39e09f7bfe71ce643863b52b3ef0eb3f`.
The direct public distance-event source is CW1S, submission
`32303149-73e3-4acd-af1f-4a6052d73869`, evaluated commit
`174d649db7c03b0619a486e9ce515c7b95e8ff2d`. Its
[exact proof](https://github.com/Layr-Labs/dcp/blob/174d649db7c03b0619a486e9ce515c7b95e8ff2d/submission/proof.md)
has SHA-256
`f680e71657013d62c319a71e48ed20c2f0670072b9f494e156101fca0501df84`.
Sections 9A.1--9A.4 supply the low-bit pool event and stride score argument.
CW1S credits these to HS2, `8b85be12-4b9c-40e6-a62f-d2d232d62402`;
that credit is retained. No prior verdict is a proof premise.

The ramp source directly adapts this account's scope-repaired CS1-SB proof.
Its exact proof snapshot has SHA-256
007f76b20f81a12f622018f604b349166a6a82cc0294b30c7435d20f2bdfd609.
Its claims file has SHA-256
60a8214fe535a3fad36b0fa503d5c18a08d6cfa26cc6476a5a878bc966dd0b29.
That snapshot is submission `1f043ca4-12d1-40bb-9d22-739f11ec8411`,
evaluated commit `b3545f5836f6cf4f443c8b5a79258a18cfd2d2c7`. Its exact
[public proof](https://github.com/Layr-Labs/dcp/blob/b3545f5836f6cf4f443c8b5a79258a18cfd2d2c7/submission/proof.md)
has the source hash above. The ramp source directly adapts its model,
source transforms, label extraction, linear merge, top-bit argument,
backward decoder, source cap, finite branch, and success proof.
Sections 7 and 13 reproduce the ramp schedule and its full resource proof.
The ramp schedule is proved in this session's plateau_next_resources.md.

The source text also directly adapts this account's CS1-BLC16L combined
proof, submission 905876c3-034c-4a87-a4fd-e64708303d71, evaluated commit
47315ee4e856c38777257dab75acf48da49991cf. That proof has SHA-256
1246ae26fd4e94335613efe870aee910031be7a542133c894ccd80d1ef278868.
It supplies the common model, transforms, extractor, merge, decoder,
caps and success argument. Its exact public source is
[CS1-BLC16L proof](https://github.com/Layr-Labs/dcp/blob/47315ee4e856c38777257dab75acf48da49991cf/submission/proof.md).

- CS1-S, 82566cc9-b278-4303-99a3-b22aa3e09155, evaluated commit
  ac51ac6e79ceb7bf79e9e50d3b1a7dde9385fca5: plateau collimation,
  its capacity calculation, and the per-acquisition merge charge.
  The source proof has SHA-256
  269ef0e03cc96455ffacdefdb48e269745dbf669221093ad44e1b65730cc72b5.
  [Exact source proof](https://github.com/Layr-Labs/dcp/blob/ac51ac6e79ceb7bf79e9e50d3b1a7dde9385fca5/submission/proof.md),
  Sections 7, 11, and 13.
- CS1-LBQ, 603d96b1-a332-49a9-90ca-ef5cb6b8a5f2, evaluated commit
  4456e60ff6e0edec393bc48478e03495b0767869: the linear reversible
  merge, explicit lookups, exact source transforms, and top-bit proof.
  Its proof has SHA-256
  1509a51e074b9a3f5f91fec57dd550cd192b26fca98e1da7340191d2dc374241.
  [Exact source proof](https://github.com/Layr-Labs/dcp/blob/4456e60ff6e0edec393bc48478e03495b0767869/submission/proof.md).
- Exact collective tests, 844c0fd2-9b1c-4e84-a37c-f402e109985f,
  evaluated commit 7c4b4ed099799e146213c1e3c43a50151482dc6b: one
  modular register subtraction for all level tests in one round.
  Its proof has SHA-256
  c0c011d54153f5e9c8f7436e581a42942e820689e0f52cef6cb8e02e7f1fce96.
  [Exact source proof](https://github.com/Layr-Labs/dcp/blob/7c4b4ed099799e146213c1e3c43a50151482dc6b/submission/proof.md).
- CS1-BACKWARD, 70936e29-d357-4713-b84f-47acebe365fd, evaluated
  commit d50e5146cf9f3c924c1cf26e0e725a3f3d2e5ad3: the terminal
  phase seed and exact two-candidate backward decoder.
  Its proof has SHA-256
  40dcb36879994c071f43235c1f2ce28080020265c7c514c8e179ad1f51a73e3f.
  [Exact source proof](https://github.com/Layr-Labs/dcp/blob/d50e5146cf9f3c924c1cf26e0e725a3f3d2e5ad3/submission/leap-research/decoder-wave/CS1-BACKWARD/proof.md).

The collimation method comes from G. Kuperberg,
[arXiv:1112.3333v1](https://arxiv.org/abs/1112.3333v1), Algorithm 4.1,
Proposition 4.2, and Section 4.6. Its heuristic time estimate is not a
premise. The level tests are the standard Kitaev tests.

## 2. Model and counting conventions

A CORE STEP is one of the following:
- one NOT/CNOT/Toffoli/H/S/S^dagger/T/T^dagger gate;
- one computational-basis single-qubit measurement or reset;
- one Boolean operation on at most three classical bits;
- one classical bit read or write.

Toffoli has an exact constant-size Clifford+T decomposition. Integers are bit
strings, and an L-bit addition, comparison or copy costs O(L) core steps.
Generating a gate costs O(1) core steps. Each core step additionally pays its
address, ceil(log2(Mem+2)) bit operations, where Mem <= S_C + S_Q is the
number of allocated bits and qubits. A source acquisition costs n+1. Hence

    T <= (number of core steps) * (1 + ceil(log2(S_C+S_Q+2))) + (n+1) Q.     (2.1)

There is no QRAM: every lookup is the explicit circuit of Section 6.1.

## 3. Source identities, the latent-label model and data transforms

Let chi_k = N^(-1/2) sum_u omega^(k u)|u> and phi_k(s) = (|0> + omega^(-k s)|1>)/sqrt 2.
Substituting |u> = N^(-1/2) sum_k omega^(-k u) chi_k into
rho_s = (1/N) sum_x |psi_x><psi_x|, with psi_x = (|0,x> + |1,x+s>)/sqrt 2, gives

    rho_s = (1/N) sum_(k=0)^(N-1) |phi_k(s)><phi_k(s)| (x) |chi_k><chi_k|,       (3.1)

because the cross terms k != k' carry (1/N) sum_x omega^(-(k-k')x) = 0.

Latent-label model. By (3.1) each copy is literally a convex mixture, with
uniform weights, of the product states phi_k(s) (x) chi_k. The whole algorithm
is a linear (adaptive) quantum instrument applied to independent copies. So
the joint law of all its classical outcomes equals the law obtained by first
drawing, for every copy, an independent uniform latent label k, and then
running on the product state phi_k(s) (x) chi_k. All probabilities below use
this model. Applying X to the control maps phi_k(s) to, up to a global phase,
the POSITIVE qubit pq_k(s) = (|0> + omega^(k s)|1>)/sqrt 2.

Two exact data transforms act on a fresh copy before label extraction. Each
is a permutation of all 2^n data encodings, extended by the identity on
encodings >= N. Each maps the copy exactly to rho_s' for a known transformed
secret s'. The latent-label model is then applied to rho_s' via (3.1), so the
latent label of a copy is the Fourier label of its TRANSFORMED data register,
which LE recovers.

(T1) Mult_alpha: u -> alpha u mod N, for a known alpha coprime to N. Since
x -> alpha x is a bijection of Z/NZ, the copy becomes exactly rho_(alpha s).
It is implemented with n controlled modular additions of the constants
alpha 2^v mod N into a clean register, a swap, and the inverse computation with
alpha^(-1): O(n^2) core steps and O(n) scratch.

(T2) Shift_c: if the control is |1>, replace u by u - c mod N, for a known c.
Since |1,x+s> becomes |1,x+(s-c)>, the copy becomes exactly rho_(s-c). This
takes O(n) core steps.

Modular addition of a known constant in [0,N) is a ripple comparison with N,
an addition, a comparison and a selector. It is the identity on encodings
>= N, uses O(n) Boolean gates, and is computed cleanly: compute, swap or XOR
the result out, then uncompute.

## 4. Rational trigonometric table

For v in [0,4096) the controller computes rationals Cos[v], Sin[v] within 2^-20
of cos(2 pi v/4096) and sin(2 pi v/4096).

- Bound pi within 2^-90 using Machin's formula pi = 16 atan(1/5) - 4 atan(1/239),
  summing the first 40 terms of each alternating arctangent series. This gives
  two-sided bounds; the tails are below 16 (1/5)^81/81 + 4 (1/239)^81/81 < 2^-91.
- The identity follows from tan(2 atan(1/5)) = 5/12, tan(4 atan(1/5)) = 120/119
  and tangent subtraction.
- At the angle 2 v p_mid/4096 < 7, where p_mid is the midpoint of the pi bounds,
  sum 80 Taylor terms. The remainder is <= 7^81/81! < 2^-170. The angle error
  is < 2^-89, and sin and cos are 1-Lipschitz.
- Round each value to denominator 2^20.

This is a fixed finite rational computation, charged once as an absolute
constant (not advice).

For x in [0,1) put tab_0(x) = Cos[floor(4096x)] and tab_1(x) = Sin[floor(4096x)],
and let cs_0(x) = cos(2 pi x), cs_1(x) = sin(2 pi x). Since cs is 2pi-Lipschitz,

    |tab_beta(x) - cs_beta(x)| <= 2 pi/4096 + 2^-20 < 1/625.                    (4.1)

## 5. Label extraction LE

Input: a data register holding chi_k beside arbitrary spectators. Set

    J_e=n+4, h_extract=ceil(log2(2^16 Qcap(n+5))),
    F(h_extract)=2^21 h_extract.

Here Qcap is the exact source cap of Section 11. Each call executes the
fixed procedure RUN(F(h_extract)) once, outputs its integer label, and resets
the data and test registers. No rejection or fallback is used.

Translation Tr_c: u -> u + c mod N satisfies Tr_c chi_k = omega^(-k c) chi_k.
A TEST WITH SHIFT c (0 <= c < N) works as follows. Prepare an ancilla in |+>.
Apply Tr_((N - c) mod N) controlled by it, so the |1> branch gets eigenvalue
omega^(k c). Measure the ancilla in X (H then Z) or in Y (S^dagger, H, then Z).
The +-1 outcome has mean cos(2 pi c k/N) or sin(2 pi c k/N). Conditioned on
k, chi_k and every spectator are unchanged and outcomes are independent. A test
at LEVEL j is the test with shift 2^j mod N. Each test costs one controlled
modular addition, O(n) core steps.

A ROUND (in basis X or Y) is one test at every level j = 0..J_e at once, built as
follows. Prepare ancillas r_0..r_(J_e) in |+> and read them as the integer
x = sum_j r_j 2^j < 2^(J_e+1) = 2^(n+5). Since N > 2^(n-1), x < 64 N.
- Copy x into a zeroed (n+5)-qubit scratch z with CNOTs. For i = 5 down to 0:
  compute the bit a_i = [z >= N 2^i] into a fresh qubit by a comparator with a
  classical constant, and controlled on a_i subtract N 2^i from z. Before step i,
  z < N 2^(i+1), so afterwards z < N 2^i; at the end z = x mod N. Each step is
  O(n) NOT/CNOT/Toffoli gates with O(n) reusable carry qubits.
- Subtract z from the data register modulo N (u -> u - z mod N on u in [0, N),
  a standard O(n) register subtraction with a borrow-controlled add-back of N
  and a comparator to clean the borrow flag).
- Undo the reduction step by step and the copy, returning z, the a_i and all
  carries to |0> exactly.
The net map is |x>|u> -> |x>|u - x mod N> on basis states, which equals the
product over j of Tr_((N - 2^j) mod N) controlled by r_j, because translations
compose additively. Since Tr_(-x) chi_k = omega^(k x) chi_k and
omega^(k x) = prod_j (omega^(k 2^j))^(r_j), the ancillas end in the product state
tensor_j (|0> + omega^(k 2^j)|1>)/sqrt 2 with chi_k and every spectator unchanged.
Measuring every r_j in the round's basis therefore gives, conditioned on k,
independent outcomes with exactly the law of separate tests at levels
j = 0..J_e. A round costs O(n) core steps and n+5 ancillas plus O(n) scratch,
all reset afterwards, so the quantum space stays O(n).

### 5.1 RUN(F): level-wise extraction

For each j = 0..J_e take F tests at level j per basis, as F X-rounds and F
Y-rounds, giving empirical means x_j and y_j. Then decode as follows.

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
F = F(h_extract) this is 2 exp(-h_extract). So RUN(F(h_extract)) returns a value other than k with
probability at most 4 (J_e + 1) e^(-h_extract) = 4 (n+5) e^(-h_extract), uniformly in k.
A call uses 2F(h_extract) rounds, each with O(n) quantum core steps. Incrementing
all outcome counters costs O(n F(h_extract) log(F(h_extract)+2)) bit operations even without
amortization. There are O(n) counters, each of O(log(F(h_extract)+2)) bits. Each of
the 64 direction scores per level is computed by integer arithmetic on
O(log(F(h_extract)+2)) bits; the fixed table denominator is common to all scores.
Exact dyadic unwrapping and final multiplication and rounding cost O(n^2).
Therefore the total core work per call is

    O(n h_extract log(h_extract+2)+n^2)=O(n^2),

because Section 13 proves h_extract=O(sqrt n), and log n=O(sqrt n). Quantum scratch
is O(n), classical scratch is O(n log n). All work is bounded on every
branch. To make the collective map total on the data encoding, first
compute [u<N] and apply the modular subtraction only on that subspace;
the data validity is preserved, so its flag can be cleared. This changes
neither the O(n) cost per round nor the action on the source.

For each call, conditional on its latent label and all earlier history,
its error probability is at most 4(n+5)e^(-h_extract). Thus over at most Qcap calls,

    Pr[any wrong label] <= 4(n+5)Qcap e^(-h_extract) <= 2^-14.

The IDEAL run replaces every returned label by its independent latent
label. All test results are private and affect no other control decision.
Actual and ideal runs can be coupled until the first wrong label. This
comparison does not condition the root law on successful extraction.



## 6. Phase vectors and the linear merge

A PHASE VECTOR of length 2^lam is a lam-qubit index register with a classical
label table lab[0..2^lam). In the ideal run its state is
2^(-lam/2) sum_x exp(2 pi i lab[x] th) |x>, up to a global phase, for a fixed
real th. Labels are nonnegative integers. The vector is COLLIMATED TO p if all
lab[x] are congruent modulo 2^p.

STORAGE. A table collimated to p is stored as its common residue
c = lab[0] mod 2^p (one p-bit number) and the HIGH PARTS hi[x] = floor(lab[x]/2^p),
so lab[x] = c + 2^p hi[x]. Each high part is stored in a fixed field of w bits,
where w is any bound with lab[x] < 2^(p+w) for all x (Section 7 fixes w per
level). Every quantity used below is computed from (c, hi) exactly; lab[x] is
never written out in full except in LEAF, where p = 0 and hi = lab.

### 6.1 Lookups

LOOKUP(tab), for a classical table of E rows with w-bit entries, XORs tab[x]
into a clean w-bit register, controlled by a lam-qubit index x. For each row
x0 = 0..E-1 it computes the flag [x = x0] with a Toffoli chain on O(lam)
scratch, applies CNOTs from the flag to the output bits where tab[x0] has a 1,
and uncomputes the chain. Indices outside [0,E) give output 0. The circuit is
its own inverse, has O(E (lam + w)) gates and O(lam + w) qubits, and is
generated by reading each table bit once.

### 6.2 MERGE(X1, X2; p, b, lam')

Precondition: X1 and X2 are phase vectors from disjoint sets of copies, both of
length 2^lam, collimated to p, with index registers x and y and tables al and be.
Both are stored as in STORAGE: al[x] = cA + 2^p hA[x] and be[y] = cB + 2^p hB[y],
with 0 <= cA, cB < 2^p. Let car = floor((cA + cB)/2^p) in {0,1}.
Define residues aa[x] = hA[x] mod 2^b and bb[y] = hB[y] mod 2^b.
Then bits p..p+b-1 of al[x] + be[y] equal (aa[x] + bb[y] + car) mod 2^b.

1. LOOKUP aa into a fresh b-bit register Ru and bb into Rv. Add Ru + Rv + car
   (mod 2^b) cleanly into a fresh register Rz, and clear Ru and Rv by repeating
   both lookups. Measure Rz, obtaining e, and reset Rz from that known value.
2. Classical. Let S_e = {(x,y) : aa[x] + bb[y] + car = e mod 2^b} and sz = |S_e|.
   - Merge-sort the indices y by the key (bb[y], y) into order[]; pos[y] is the
     position of y.
   - For each x the partners y form one contiguous run of order[], namely the
     residue class cls[x] = (e - car - aa[x]) mod 2^b. Find its start lo[x] and
     length cnt[x] by binary search.
   - Put off[x] = sum_(x' < x) cnt[x'] and rank(x,y) = off[x] + pos[y] - lo[x].
     The rank is a bijection from S_e onto [0, sz).
   - If sz < 2^lam', declare FAIL.
3. Let R have 2 lam + 1 bits. LOOKUP pos into Rp and Dx[x] = (off[x] - lo[x]) mod 2^(2lam+1)
   into Rd. Add Rp + Rd (mod 2^(2lam+1)) cleanly into a fresh R, and clear Rp
   and Rd by repeating the lookups. On S_e, R = rank(x,y).
4. Measure bl = floor(R / 2^lam'), the bits of R above the low lam'. If
   (bl+1) 2^lam' > sz, declare FAIL.
5. Classical. For v in [0, 2^lam'), find the unique (x_v, y_v) with rank
   bl 2^lam' + v, in one scan over x with running offsets. Apply LOOKUP
   v -> (x_v, y_v) on the low lam' bits of R, XORing into the registers x and y,
   which become |0>. Reset the high bits of R from their known value bl.
6. Output the low lam' bits of R as the index register, with table
   lab[v] = al[x_v] + be[y_v], stored as in STORAGE with p+b in place of p:
   put sv = hA[x_v] + hB[y_v] + car, which is congruent to e modulo 2^b. Then
   lab[v] = (cA + cB - car 2^p + 2^p e) + 2^(p+b) floor(sv/2^b). The first term
   c' = cA + cB - car 2^p + 2^p e lies in [0, 2^(p+b)) and does not depend on v.
   So the stored output is the common residue c' and the high parts
   hi'[v] = floor(sv/2^b).

On FAIL, both inputs are reset and released and never reused. All registers
have fixed widths, so memory is allocated deterministically.

Correctness (ideal run). Before step 1 the state is X1 (x) X2: equal
magnitudes over all pairs (x,y), with phases 2 pi (al[x] + be[y]) th. Steps 1
and 3 compute functions of (x,y) into clean registers and measure them. So
after step 4 the state is the equal-magnitude superposition over the 2^lam'
pairs of block bl, with their original phases. Step 5 maps (x_v, y_v) to v
bijectively. The output is therefore a phase vector with table lab. Every
label is congruent to cA + cB + 2^p ((e - car) mod 2^b) modulo 2^(p+b), so the
output is collimated to p+b.

Lemma 6.1 (distribution-free failure). For ANY input tables collimated to p,
the measurement law in steps 1 and 4 depends only on aa, bb and car (that is,
on label bits below p+b), and Pr[FAIL] <= 2^(b + lam' - 2 lam).

Proof. Each measurement is a computational-basis measurement of a function of
(x,y) on an equal-magnitude superposition. Its outcome probabilities are
therefore ratios of counts, independent of the phases. The outcome e has
probability sz_e / 2^(2lam). Given e, the measured rank is uniform on [0, sz_e).
So FAIL has conditional probability rem_e / sz_e, where rem_e = sz_e mod 2^lam'
(this also covers sz_e < 2^lam'). Hence
Pr[FAIL] = sum_e rem_e / 2^(2lam) <= 2^b (2^lam' - 1) / 2^(2lam). QED.

Cost. Write L = 2^lam and L' = 2^lam'. A merge makes eight lookup passes of L
rows and one of L' rows, each with O(lam + b) bit fields. Classically it
performs O(L lam) comparisons of (b + lam)-bit keys, O(L) binary searches of
O(lam) steps on b-bit keys, and O(L') additions of high parts of at most
O(n) bits. With lam, b = O(sqrt n) (Section 7), this is O(n (L + L')) core steps.
The quantum scratch is O(sqrt n) beyond the two index registers. The classical
scratch (order, pos, lo, cnt, off, Dx, aa, bb and the inverse block table) is
O((L + L') sqrt n) bits, and the output table is L' fields of w' bits plus
p + b bits for c'.

## 7. The tree TREE_D

Input: a supplier of LEAF QUBITS. Each is a positive qubit with a known
label uniform on [0,2^D), D>=2, independently. Put B=D-1>=1. Compute
these exact integers:

    r=ceil(sqrt B), kappa=ceil(log2 r)+1,
    d0=min(r-1,floor(sqrt r)), x=r-d0, q=kappa+1+x,
    C(j)=(j+1)(r+1)+kappa-1-d0(d0+3)/2,
    m=min{j>=d0+1:C(j)>=B},
    lam_i=q+min(i,d0) for 0<=i<m, lam_m=1.

The integer d0 is the number of growing levels. It differs from
d=floor(log2 N). Each leaf has q qubits. Each growing merge adds one
index bit. The following nonroot vectors have width kappa+1+r. The root
has one qubit. Set the capacities

    bmax_i=x+i                  for 0<=i<d0,
    bmax_i=r+1                  for d0<=i<m-1,
    bmax_(m-1)=kappa+2r+1.

A range can be empty. If B=1, then r=1, d0=0 and m=1, so only the root
capacity is present. The parameter m is defined because C(j) grows
strictly with j.

### 7.1 Capacity and depth

For every r>=1, kappa>=1, kappa<=r, 2^kappa>=2r and 2^kappa<4r.
The capacity sum is exactly

    sum_i bmax_i
      =d0(r-d0)+d0(d0-1)/2
         +(m-d0-1)(r+1)+kappa+2r+1
      =(m+1)(r+1)+kappa-1-d0(d0+3)/2=C(m)>=B.

Also 1<=m<=r. To prove the upper bound, d0<=r-1 gives r>=d0+1,
so r is in the search range. Since d0<=sqrt r and B<=r^2,

    C(r)-r^2=2r+kappa-d0(d0+3)/2
      >=(3/2)r-(3/2)sqrt r+kappa>=0.

Thus j=r is feasible. In particular 2^kappa>=2r>=2m.

Allocate b_(m-1),b_(m-2),...,b_0 in that order, by

    b_i=min(bmax_i,B-(already allocated)).

The capacity sum proves sum_i b_i=B. Put p_0=0 and
p_(i+1)=p_i+b_i, so p_m=B. A zero b_i is permitted; the merge then
measures an empty residue register. Its rank and block steps are still
the same finite operations. Let nq_D=2^m q.

For growing levels i<d0, lam_(i+1)=lam_i+1 and
bmax_i=x+i=lam_i-kappa-1. For fixed-width nonroot levels,
bmax_i=r+1=lam_i-kappa and lam_(i+1)=lam_i. At the root,
lam_(m-1)=kappa+1+r and bmax_(m-1)=2lam_(m-1)-kappa-1.
These three identities give, at every level,

    b_i+lam_(i+1)-2lam_i<=-kappa.                    (7.1)

By Lemma 6.1 each merge therefore fails with probability at most
2^-kappa<=1/(2r)<=1/(2m), for every pair of input tables.

### 7.2 Leaves, field widths and evaluation

LEAF: take q leaf qubits as the index register, bit j equal to qubit j.
Build lab[0]=0 and lab[x+2^j]=lab[x]+k_j for x<2^j, by one addition per
entry. The table has length 2^q, is collimated to p_0=0, and is exactly
the tensor product state in the ideal run.

A level-i label is a sum of at most 2^i q leaf labels below 2^(B+1).
Put gw=ceil(log2 q). The label is below 2^(B+1+i+gw). Store its high
part in a fixed field of

    w_i=B+1+i+gw-p_i

bits. These are valid widths on every branch, also with wrong extracted
labels, because each label used by a tree is restricted to its stated
D-bit range before LEAF.

VEC(i): if i=0 return LEAF. Otherwise repeat:
- X1=VEC(i-1);
- X2=VEC(i-1);
- out=MERGE(X1,X2;p_(i-1),b_(i-1),lam_i);
- if out is not FAIL, return out.

TREE_D returns VEC(m), a one-qubit phase vector whose labels are
congruent modulo 2^B. Its ideal state, up to a global phase, is
(|0>+exp(2 pi i 2^B W th)|1>)/sqrt 2, where

    W=(lab[1]-lab[0])/2^B=hi[1]-hi[0].                (7.2)

A returned tree has 2^m q distinct retained leaf qubits. Its labels are
sums of at most nq_D leaf labels below 2^(B+1), so |W|<2nq_D.
Failed inputs are reset, released, and never reused. Evaluation in
depth-first order holds at most one finished sibling per level.

### 7.3 Uniform size bounds

For B<=n and n>=64 put

    r*=ceil(sqrt n), kappa*=ceil(log2 r*)+1,
    lam*=kappa*+1+r*, A*=2^(r*)lam*.

Every tree has r<=r*, kappa<=kappa*, m<=r*, and lam_i<=lam*.
These bounds do not require m or q to be monotone in B. Since sqrt n>=8,

    r*<sqrt n+1, 2^(r*)<2*2^(sqrt n),
    2^(kappa*)<4r*<4sqrt n+4<=(9/2)sqrt n,
    lam*<=2r*+1<2sqrt n+3<3sqrt n.

Consequently every b_i<=kappa+2r+1=O(sqrt n), and

    nq_D=2^m q<=A*<6sqrt n 2^(sqrt n).

The stack holds at most one finished sibling at each of m levels
and one active index register. Its index registers therefore use at most

    (m+1)lam*<=(r*+1)lam*
      <(sqrt n+2)3sqrt n<4n

qubits. Temporary registers of an active merge are counted separately
in Section 13.4. The high-part fields w_i are O(n) bits. Also

    2^(lam*)<18sqrt n 2^(sqrt n),
    2^(lam*)/lam*<18*2^(sqrt n),

where the last bound uses lam*>=r*>=sqrt n.

## 8. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and
tau_j in {0,1}. Since k_j is uniform on [0, 2^(B+1)), low_j and tau_j are
independent and tau_j is a fair bit. Let Gt be the sigma-field generated by:
- all low_j of the tree's leaves, including those of discarded attempts;
- all measurement outcomes (e, bl) of its merges;
- all tree-construction decisions of the controller (merge parameters, FAIL
  and retry decisions, leaf acceptance tests and which copies are used).
Gt does NOT include LE's private test outcomes (Section 5). In the ideal run these feed no
decision: every LE output is replaced by the latent k. Given k, they are
independent of everything else, so they are averaged out and never conditioned on.

Lemma 8.1. In the ideal run, conditional on Gt and on all other independent
randomness (other copies, controller coins, earlier root outcomes), the top
bits tau_j of the leaves of the returned root are i.i.d. fair.

Proof, by induction over the controller's steps. Every tree-construction decision, residue,
sort key, rank and block partition uses only label bits below position B,
since Section 6.2 reads bits p..p+b-1 with p + b <= B, together with index
order. Bits below B of a sum of leaf labels depend only on the low_j: adding
multiples of 2^B does not change them. By Lemma 6.1, each measurement's
conditional law, given the labels and the earlier outcomes, is a function of
the low_j and the earlier outcomes only. Inductively, the joint law of
(all tau, all low, all outcomes and decisions) factorizes as
law(tau) x law(low) x law(outcomes and decisions | low). Retries use fresh
copies, whose labels enter the same factorization. QED.

Let x0 and x1 be the leaf-incidence vectors of the two root entries. Distinct
indices at a node correspond to distinct incidence vectors: this holds at
leaves, is preserved by concatenating disjoint coordinate sets, and
re-indexing is a bijection. So hd = |x0 xor x1| >= 1. From (7.2),

    W = cst + sum_(j in Sp) tau_j - sum_(j in Sm) tau_j,                        (8.1)

where cst = (sum_j low_j (x1_j - x0_j)) / 2^B is a Gt-measurable integer, and Sp and
Sm are disjoint Gt-measurable sets with |Sp| + |Sm| = hd. A fair bit tau has
E exp(2 pi i phi tau) = e^(i pi phi) cos(pi phi). Hence, for every real phi,

    | E[ exp(2 pi i phi W) | Gt ] | = |cos(pi phi)|^hd <= |cos(pi phi)|,       (8.2)

and, with phi = 1/2, Pr[W odd | Gt] = 1/2.                                     (8.3)

## 9. Odd-part source, fallback decoder, and strided decoder

If M=1 set s1=0 and skip this section. Otherwise M>=3, D=d, B=d-1>=a2,
q_odd=nq_d and ell=ceil(log2 q_odd). Write theta=s1/M. For ANY nonnegative physical
scale j, compute the CRT unit alpha_j by

    alpha_j=1 mod2^a2,
    alpha_j=2^j*(2^(d-1-a2))^-1 mod M.

Acquire a fresh original copy, apply Mult_alpha_j, extract k with LE, reject
k>=2^d, and on acceptance apply X to the first qubit. In the ideal reference,
accepted labels are iid uniform in[0,2^d), with original acquisition acceptance
2^d/N>1/2. The retained phase is k*alpha_j*s/N. A TREE_d root is consequently
(|0>+exp(2pi i W 2^j theta)|1>)/sqrt2, because
2^(d-1-a2)*alpha_j=2^j modulo M and s=s1 modulo M. This identity uses the
original modulus, not a fictitious dyadic coset-state source. CRT units exist
at every physical scale used by this decoder.

The following root law is proved in Section 8:
conditional on fresh-root low-only history G and independent past,
W=c_G+sum epsilon_l*tau_l with iid fair top bits, nonzero signed coefficients,
and |W|<2q_odd. Thus |E exp(2pi i zW)|<=|cos(pi z)| and
Pr(W odd|G,past)=1/2. The fallback decoder needs only this law. The strided decoder below
proves its stronger support estimate from an explicit finite pool. Private extractor transcripts are
averaged out in the ideal run. Section12 couples the actual implementation.

### 9.1 Ordinary fallback: exact two-candidate backward lemma

Write ||x|| for circular distance to 0. Suppose a known dyadic center
z in [0,1) satisfies

    ||2x - z|| <= e,             e <= 1/(64q_odd).

The inverse images of z under doubling are

    u_0 = z/2,                  u_1 = (z+1)/2.

Exactly one of them, denoted u_*, lies within e/2 of x; the other is 1/2
away from u_*. This is a statement on the circle, so it includes z=0,
wraparound, and x arbitrarily close to any binary boundary.

Produce k fresh roots with phase W_i x. For each independently choose
beta_i uniformly from {0,1}, measure X or Y respectively, and record
Z_i in {+1,-1}. Use the source's constant-size trigonometric table:

    score(b) = sum_i Z_i tab_beta_i(W_i u_b mod 1).

The table error is uniformly less than 1/625. Output the smaller index
maximizing score, making the algorithm total even on failure branches.

**Lemma.** Conditional on the incoming center satisfying the displayed
accuracy hypothesis, the wrong candidate is chosen with probability at
most exp(-k/512). No stronger root law is needed.

Proof. Let delta = x-u_* be the circular representative with
|delta| <= e/2. Define the exact score difference for one root by

    X_i = Z_i [cs_beta_i(W_i u_*) - cs_beta_i(W_i u_other)],
    cs_0(t)=cos(2 pi t),          cs_1(t)=sin(2 pi t).

Averaging over the fresh basis coin and root outcome, conditional on W_i,
gives

    E[X_i | W_i,past]
      = (cos(2 pi W_i delta)
         - cos(2 pi W_i(delta +/- 1/2)))/2
      = 1_{W_i odd} cos(2 pi W_i delta).

The sign in +/- 1/2 does not matter for integer W_i. Pointwise,

    |2 pi W_i delta| < pi/32.

By the conditional parity law, E[X_i | past] >= mu = cos(pi/32)/2.
In particular, the useful cosine need not be independent of parity.
It is bounded below for EVERY W in the prescribed support.

Each |X_i| <= 2, so the martingale increments
X_i-E[X_i|past] have absolute value at most 4. The computed score difference
differs from sum_i X_i by at most 2k/625. Since

    mu - 2/625 > 1/4,

Azuma gives

    Pr[computed true-minus-false score <= 0]
       <= exp(-(k/4)^2/(2*16*k)) = exp(-k/512).

For an entirely rational numerical margin, pi < 22/7 and
cos(v) >= 1-v^2/2 imply

    (1-(22/7)^2/(2*32^2))/2 - 2/625 - 1/4
       = 7664023/31360000 > 0.

All conditioning is before the new root or on the allowed lower-bit
transcript. This is not a favorable-label or successful-extraction
conditioning argument. QED.

If the correct lift is selected, its error is e/2. Thus accuracy improves
as decoding proceeds backward. It does not degrade by q_odd per step.

### 9.2 Ordinary fallback: one terminal seed and backward steps

Use this ordinary decoder when 64<=n<256, or when the exact distance
parameter h in Section 9.3 is below 16. Assume M>=3. Set exactly

    H = ceil(log2 M),
    J_old = ell+3,
    nu = ceil(log2(n+ell+4)),
    K_seed = 8192(ell+nu+30),
    K_back = 512(nu+30).

#### 9.2.1 Seed at scale H

Apply the explicit localization algorithm below to the phase

    phi = 2^H theta mod 1

for local stages u = 0,1,...,J_old. Local stage u obtains roots at physical
scale H+u, using the same TREE_d and K_seed roots. At every local stage, measure its K_seed roots in independent fair X/Y
bases and record (W_i,beta_i,Z_i). On its dyadic candidate grid compute
score(c)=sum_i Z_i tab_beta_i(((2^u W_i c) mod2^P_u)/2^P_u), with the
Section4 table. Stream candidates and return the least maximizing one.
At stage u, the
dyadic denominator is 2^(P_u), where P_u = u+ell+8.
Stage 0 enumerates the whole grid. Each later stage enumerates the grid
points in the closed circular arc of radius 2^-(u+2) around the previous
center. The arc endpoints are grid points, so nearest-point guarantees
hold even at boundaries.

For completeness, the source proof of this localization uses only the
contract above. A nearest candidate zeta_0 obeys

    |2^u W (phi-zeta_0)| <= 2^-8.

A far candidate, at distance at least 2^-(u+3), has
2^u ||phi-zeta|| in [1/8,1/2] inside the incoming arc. Thus its expected
per-root score is at most cos(pi/8)/2, while the near candidate has score
at least cos(pi/128)/2. Martingale concentration at deviation K_seed/64,
table error K_seed/625, and the at most 2^(ell+9) near/far events imply
failure at most 2^-20/(n+ell+4) per stage. The strict score margin can be checked
without floating point using pi > 3, pi < 22/7, and the alternating
cosine bounds:

    [9/128 - (22/7)^2/(2*128^2)
       - (22/7)^4/(24*8^4)]/2 - 2/64 - 2/625
      = 4372721/73758720000 > 0.

At the last seed stage, obtain z_H satisfying, except on seed failure,

    ||phi-z_H|| <= e_H = 2^-(ell+6) <= 1/(64q_odd).

There are ell+4 seed stages. In the concentration bound use the present
nu=ceil(log2(n+ell+4)). The failure per seed stage is at most
2^-20/(n+ell+4). Thus the total seed failure is at most 2^-20 for every
n>=64, including all small trees affected by the longer cap. No bound
ell+4<=n is needed.

The seed's exact denominator is 2^(2ell+11). The seed is an ordinary
localization of a real phase on the circle. It does NOT presume phi is a
dyadic rational or try to round phi to a secretly known rational grid.

#### 9.2.2 Backward steps

For j = H-1,H-2,...,0:

1. Form the exact dyadic candidates z_(j+1)/2 and (z_(j+1)+1)/2.
2. Acquire K_back fresh TREE_d roots at physical scale j.
3. Apply the two-candidate scoring rule of Section 9.1 and set z_j to its
   deterministic maximizer.

If all preceding choices were correct, the true phase x_j = 2^j theta
has distance at most e_H/2^(H-j) from z_j. Every such incoming radius is
small enough for the lemma. Since exp(-K_back/512) <= 2^-30/n and H <= n,
the conditional error union bound is at most 2^-30.

This union bound is over first-error events, not conditioning the complete
run on success. Previous branch decisions can be adaptive; every newly
called source uses fresh independent mixed copies.

#### 9.2.3 Exact rounding and boundary digits

The output center z_0 has denominator 2^(H+2ell+11), and

    ||theta-z_0|| <= 2^-(H+ell+6) <= 1/(64 q_odd M) < 1/(2M).

Return

    s1 = floor(M z_0 + 1/2) mod M.

It equals s mod M on the stated good event. The strict distance rules out
a rounding tie. If z_0 lies near 1 and theta=0, reduction modulo M gives
0 correctly. The same circular argument handles every binary boundary;
we never identify the chosen lift with a fragile convention about a
terminating expansion of theta.

No repeated numerical phase truncation is used. Each lift is an exact
integer numerator over a power-of-two denominator. Each backwards step
adds one denominator bit. The only approximation in the scores is the
source's fixed trigonometric table, already budgeted in both lemmas.

#### 9.2.4 The actual root budget

The odd-part root count is the deterministic integer

    F_old = (ell+4) K_seed + H K_back.

Hence F_old=O(ell^2+ell log n+n log n)=O(n log n).
After the seed, there are two candidates at each step, not O(q_odd) candidate
suffixes. Initialization enumerates at most 2^(ell+8) <= 512q_odd candidates
per stage, keeping only a running maximum and the measured root records.

The Section 7 bound q_odd<=A* gives ell=O(sqrt n), hence ell^2=O(n).
This proves the displayed root budget for the specified schedule. No
support-concentration assumption is used.

### 9.3 Exact strided parameters, finite pool, and fallback

Assume M>1 and n>=256. Here D=d, B=d-1>=n-2, independent
of the size of the odd factor M. Put C=6A*, using the exact uniform tree
upper bound A* of Section 7. This C bounds expected originals per tree
after every earlier history, including small 2-adic tree widths.
The odd tree has q_odd=nq_d and |W|<2q_odd. Its selected signed incidence
vector is nonzero, has coefficients in {-1,0,1} on distinct leaves,
and is chosen using only low label data. Different root calls use
disjoint fresh leaves. These properties follow from Sections 6--8.
The finite range 64<=n<256 uses the ordinary decoder above. Set

    ell=ceil(log2 q_odd), U=n+ell+40,
    A=2^40 (C+1) U^3,
    g=ceil(log2(2A)), h=floor(B/(8g)).

All these are explicit integers with polynomial bit length. If h<16,
use the preceding one-bit backward decoder and its exact caps. The
new asymptotic bounds still hold on this fallback: uniformly over all
odd-part trees, ell=O(sqrt n) and log2 C=O(sqrt n), so h tends
to infinity. Thus this branch applies to only finitely many bit lengths,
uniformly over all N and s of a given length. Its finite resource
maximum changes only an absolute outside constant. It is an executable
predicate, not an uncomputed asymptotic threshold. M=1 uses no decoder
and causes no fallback issue.

For h>=16 put

    Delta=floor(floor(log2 h)/2)-1,
    H=ceil(log2 M), nu=ceil(log2(n+ell+4)),
    Kseed=8192(ell+nu+30),
    Kback=8192(Delta+nu+30),
    Sseed=ceil((ell+3)/Delta), Sback=ceil(H/Delta),
    F=Sseed Kseed+Sback Kback.

Then Delta>=1 and 2^(Delta+3)<=4sqrt h. Sections 9.4--9.5 describe exactly
these F roots. For a pure 2-power set F=0 without computing odd parameters.

Use the exact source budget

    Qstar=C(F+2n)+2n, Qcap=1024 Qstar.

Keep the existing before-action cap checks. Keep K2=ceil(log2 n)+30
attempts at each 2-adic bit and the existing direct width-one case.
A root's source cost and outcome need not be independent. The uniform
fresh-attempt arguments in the supplier proofs give expected total
sources <=Qstar.
The global cap therefore costs at most 2^-10 failure by Markov.

The analysis pool really contains the capped run. Since Delta>=1,
Sseed<=ell+3 and Sback<=n. Also Kseed,Kback<=2^15 U. Consequently

    F<=2^15 U^2,
    Qcap<=2^27(C+1)U^2<=A.

Extend the accepted odd-leaf sequence to an infinite independent uniform
sequence. This is possible because source transforms depend only on the
fixed physical scale sequence, never on decoder centers. Given the
waiting counts and rejected values, the next accepted label still has
the same uniform law. Independent fresh arrays per fixed root call give
an equivalent construction; concatenating their used prefixes gives this
pool. Adaptive failures only determine how many new coordinates are used.
For a fixed waiting time t, rejected values z_1,...,z_(t-1)>=2^d and
accepted value y<2^d, the ideal latent-label probability is exactly N^-t.
Summing over y gives waiting/rejection probability 2^d N^-t. Thus y is
uniform and independent of that entire waiting/rejection record. Root
switches are stopped prefixes determined by consumed low construction
data, never accepted top bits. Induction over those switches preserves
the independent accepted sequence; unused independent coordinates extend
it to the finite analysis pool.

Let E be the low-bit event that no nonempty signed sum on fewer than h
distinct coordinates among the first A low labels vanishes modulo 2^B.
Each coefficient on its support is +1 or -1. A fixed
nonempty signed sum is uniform modulo 2^B: expose all but one coordinate,
whose coefficient is a unit. Thus

    Pr[E fails] <= 2^-B sum_(t=1)^(h-1) binom(A,t)2^t
                <= h(2A)^h 2^-B
                <= 2^(-3B/4).

For the last inequality, h g<=B/8 and log2 h<=log2 B<=B/8 for B>=64.
Here B>=n-2>=254. The bound is therefore less than 2^-190.

Let Llow be defined in the ideal latent-label process. Include all low
pool coordinates, waiting counts and rejected latent labels, and all
construction/search/bucket/pair outcomes in the fixed odd-root schedule.
Marginalize the extractor's internal records; they are not in Llow and
do not control this ideal process. Do not include decoder outcomes,
X/Y basis coins, or accepted top bits. The joint probability kernels
for construction depend only on
low data. Conditional on Llow, the accepted tau_v remain independent
fair bits, and every root uses a fixed disjoint subset of them. This
statement follows by induction over finite fresh attempts and then by
almost-sure termination; it does not condition label extraction on
success. Extraction errors are treated by an additive coupling later.

Let Fitodd say that the complete ideal odd schedule fits its source cap.
This event is Llow-measurable. On E and Fitodd, every root's nonzero
support has at least h coordinates: its full signed label is divisible by 2^B, so a smaller support would give
a forbidden signed low relation. In particular, for every real x,

    |E[exp(2 pi i x W) | Llow]| <= |cos(pi x)|^h.       (9.S1)

Earlier decoder outcomes only reveal top bits of disjoint earlier root
sets. Hence (9.S1) remains valid with those outcomes exposed. This is the
fresh-root conditioning needed below. We never condition on the full
source cap event of the later adaptive 2-adic procedure.

### 9.4 The strided terminal seed

The unknown terminal phase is phi=2^H theta mod1. There are exactly
Sseed stages. Stage t=0,...,Sseed-1 sets j=t Delta and acquires Kseed
roots at physical scale H+j. Measure each in an independent fair X/Y
basis; store (W_i,beta_i,Z_i), Z_i in {+1,-1}.

Use grid denominator exponent P_j=j+ell+8. Stage zero uses the whole
grid c/2^P_j. Later stages use all grid points in the closed circular
arc of radius 2^-(j+3) about the preceding center. Its endpoints are
grid points: the previous denominator divides 2^P_j and P_j>=j+3.
Thus the candidate set has at most 2^(ell+8)<=512q_odd elements, and a
nearest candidate is within 2^-(P_j+1) of phi whenever the incoming
accuracy condition holds. Stream the grid in one or two integer
intervals. Do not store the candidate list.

Score a candidate zeta by

    score(zeta)=sum_i Z_i tab_beta_i(2^j W_i zeta mod1),

with the existing fixed rational sine/cosine table, uniform error less
than 1/625. Choose the least maximizing grid index, also on bad events.
The ideal exact per-root score xi has expectation

    E[xi | W_i,past]=(1/2)cos(2 pi 2^j W_i(phi-zeta)).

For the nearest point, |2^j W_i(phi-zeta)|<2^-8, so its conditional
mean is at least cos(pi/128)/2>499/1000.

A far candidate has circular distance at least 2^-(j+Delta+3) from phi.
At stage zero the distance is at most 1/2. At later stages both points
lie in the incoming arc, so their distance is at most 2^-(j+2).
Therefore x=2^j(phi-zeta), with its relevant signed representative,
has 2^-(Delta+3)<=|x|<=1/2. Since sin(pi|x|)>=2|x|,

    |cos(pi x)|^h <= exp(-2h x^2)<=exp(-1/8).

By (9.S1), a far candidate's expected exact score is at most
exp(-1/8)/2<=4/9. For each fixed candidate, the exact single-root score
lies in [-1,1]. Its centered conditional range has length two, so the
conditional Hoeffding bound is E exp(lambda(xi-E[xi|past]))<=exp(lambda^2/2).
Iteration and exponential Markov give a one-sided deviation t over Kseed
records with probability at most exp(-t^2/(2Kseed)). At t=Kseed/64 this
is exp(-Kseed/8192). The score
comparison is strict, since

    499/1000-4/9 > 2/64+2/625.

There are at most 2^(ell+9) near/far events. Their union probability
is at most 2^-20/(n+ell+4), by the exact Kseed and nu above. Hence the
output center has error less than 2^-(j+Delta+3), which is exactly the
next incoming radius. This argument is conditional on any Llow in
E and Fitodd and on earlier stages. It includes adaptive centers.

At the final stage obtain z_H with

    ||2^H theta-z_H|| <= e=2^-(Sseed Delta+3)
                         <=2^-(ell+6)<=1/(64q_odd).

The seed's largest local physical scale is (Sseed-1)Delta<ell+3.
Its final denominator exponent is (Sseed-1)Delta+ell+8<2ell+11.

### 9.5 A backward block of up to Delta bits

Suppose a dyadic z approximates 2^j theta with circular error e_j<=e.
Take r=min(Delta,j), set j'=j-r, and form all 2^r exact lifts

    u_a=(z+a)/2^r, 0<=a<2^r.

Exactly one lift ustar has circular distance at most e_j/2^r from
x=2^j' theta. Acquire Kback fresh roots at physical scale j'. Measure
each in an independent fair X/Y basis and record (W_i,beta_i,Z_i), as in
the seed. Score these lifts with sum_i Z_i tab_beta_i(W_i u_a mod1) and choose the
least maximizing a. Repeat until j=0. This uses exactly Sback blocks.
The physical scale sequence and root counts are fixed by N, not scores.

For the correct lift delta=x-ustar, every |W delta|<1/64, because
|W|<2q_odd, e_j<=1/(64q_odd), and r>=1. Its expected exact per-root score is
at least cos(pi/32)/2>49/100. For any other lift, the circular distance
from x is at least

    (1-e_j)/2^r >= 1/2^(r+1) >= 1/sqrt h.

The last bound follows from 2^Delta<=sqrt h/2. Its distance is also at
most 1/2. Thus (9.S1) bounds its expected score by exp(-1/8)/2<=4/9.
This looser exponent is sufficient and avoids a dependence on r.

The same concentration calculation has at most 2^(Delta+1) events.
Kback gives error at most 2^-20/(n+ell+4) per block. The margin is
strict since

    49/100-4/9 > 2/64+2/625.

On a correct choice, the new error is exactly bounded by e_j/2^r.
There is no rounding or loss of denominator bits in a lift. After all
blocks, ||theta-z_0||<=e/2^H<1/(2M). Return

    floor(M z_0+1/2) mod M.

This returns s mod M, including wraparound and binary-boundary cases.

There are at most ell+3+n<n+ell+4 seed stages and backward blocks.
A union bound over first incorrect stages therefore gives total decoder
failure <=2^-20 conditional on every Llow in E and Fitodd. Integrate
this bound, add Pr[E fails], the global cap bounds, and the unchanged
exact-extraction error <=2^-14. The 2-adic attempt cap adds <=2^-30.
For this plateau algorithm the total is less than

    2^-190+2^-20+2^-10+2^-14+2^-30 < 2^-8.

### 9.6 Exact roots, grid work, and memory

The exact count is

    F=ceil((ell+3)/Delta)*8192(ell+nu+30)
       +ceil(H/Delta)*8192(Delta+nu+30).               (9.S2)

For the plateau tree, ell=O(sqrt n), log2 C=O(sqrt n), and ell^2=O(n).
Thus log2 A=O(sqrt n), h=Omega(sqrt n), and

    Delta=Omega(L), Delta=O(L), nu=O(L).

These estimates concern only odd trees with B>=n-2. They are uniform
in M and s. Formula (9.S2) consequently gives

    F=O(ell^2/L+ell+n)=O(n).                           (9.S3)

M=1 has F=0. For small M, H is smaller, and the same bound applies.

Seed work. There are at most 512q_odd grid candidates per stage and
Kseed records. Initialize exact residues at each interval's first
candidate by schoolbook multiplication. Then update each residue with
one O(n)-bit addition per candidate. All exponents, signed frequency
fields, scales, and dyadic numerators have O(n) bits. The logical work is

    O(n q_odd Sseed Kseed)+poly(n)
       =O(n q_odd(ell^2/L+ell))+poly(n).                  (9.S4)

For this plateau configuration, even a further fixed polynomial factor
on (9.S4) is absorbed: q_odd=O(sqrt n 2^sqrt n), whereas its dominant
merge term has exponent 2sqrt n-n^(1/4). Section 13 gives the full charge.

Backward work. There are at most 2^Delta<=sqrt h/2<=sqrt n candidates
per block, Sback<=n, and Kback=O(L) records. Direct exact products,
comparisons, table evaluation, and streaming scores therefore take
polynomial work. Using schoolbook multiplication gives the conservative
logical bound O(n^(7/2)L); extra address/generation charges remain
polynomial. No uncounted candidate oracle is used.

Only one stage's records and running residues are stored: Kseed=O(ell+L)
records of O(n) bits, or Kback=O(L) records during backward blocks.
Candidate lists are streamed. Thus decoder storage is O(n(ell+L)),
inside the plateau space bound. Quantum
storage is the existing one-root workspace; measure each root at once.
The final denominator has at most H+2ell+11 bits, as before.

## 10. 2-adic part: s2 bit by bit

If a2 = 0, put s2 = 0 and skip this section. Otherwise s - s1 = M s2 (mod N) for
a unique s2 in [0, 2^a2). The bits of s2 are found at levels g = 0..a2-1. Let
s2low be the known low g bits. Put sh_g = s1 + M s2low (mod N), wd = a2 - g, and
rem = (s2 - s2low)/2^g in Z/2^wd. Then s - sh_g = M 2^g rem (mod N).

Leaf qubit for level g:
- acquire a copy and apply Shift_(sh_g), which makes the secret s - sh_g;
- run LE to obtain k, and apply X to the control.

Ideally the phase is exp(2 pi i k M 2^g rem/N) = exp(2 pi i kk rem/2^wd), with
kk = k mod 2^wd. Since 2^wd divides N and k is uniform on Z/NZ, kk is uniform on
[0, 2^wd). Use kk as the label.

- If wd = 1: if kk = 1, measure X; the outcome is + iff rem is even. If kk = 0,
  discard and repeat.
- If wd >= 2: run TREE_wd (D = wd). If W is even, discard and repeat. If W is
  odd, the root is (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2,
  and an X measurement gives rem mod 2 exactly.

By (8.3), each attempt has odd W with probability exactly 1/2, even after
an incorrect odd residue or earlier bit. On such a history, the stored kk
labels need not describe the actual phases. However, every leaf product
still has equal basis magnitudes. Each merge measures basis functions and
reindexes a full block, so equal magnitudes persist. Its outcome and retry
law depends only on stored low labels. The top-bit and odd-W laws thus
remain valid. The displayed phase identity and exact parity conclusion
are used only when the odd residue and earlier bits are correct. Set bit
g of s2. In the ideal run with s1 correct, every accepted bit is correct.
Output (s1 + M s2) mod N.

## 11. Complete algorithm and branch limits

For n<64 use this finite procedure. For cand=0,...,N-1 in order, take up
to n+10 fresh copies, apply Shift_cand, and measure the control in X.
Reject cand at its first minus. Output the first candidate never rejected,
or 0. The correct candidate always passes. For every wrong candidate the
two data branches are orthogonal; each independent test is fair. Hence
failure is at most N 2^(-(n+10))<=2^-10. All costs on this finite range
have an absolute bound and are absorbed in the resource constants.

For n>=64 compute the uniform tree upper parameters first:

    r*=ceil(sqrt n), kappa*=ceil(log2 r*)+1,
    lam*=kappa*+1+r*, A*=2^(r*)lam*, C=6A*.

Choose the following deterministic decoder branch.

- If M=1, set s1=0, F=0 and Qstar=C(2n)+2n. No odd-pool or decoder
  parameters are needed.
- If M>1 and 64<=n<256, use the complete ordinary decoder of
  Sections 9.1--9.2. Put F=F_old and
  Qstar=6A*(F+2a2)+2a2, exactly its ordinary source-cap rule.
- If M>1 and n>=256, compute q_odd=nq_d, ell, U,A,g,h from Section 9.3.
  If h<16, use the same ordinary decoder and exact ordinary cap above.
  If h>=16, use Sections 9.4--9.5 and their exact integer count

      F=ceil((ell+3)/Delta)Kseed+ceil(H/Delta)Kback,
      Qstar=C(F+2n)+2n.

In every case set Qcap=1024Qstar before any acquisition. The analysis pool
A is never allocated. Only its integer representation and the parameters
computed from it are retained. No support test or rejection based on E
is part of the algorithm.

Set K2=ceil(log2 n)+30. Section 10 allows at most K2 root attempts per
2-adic bit, or K2 direct single-label attempts at width one. If none has
odd W or label one, abort and output zero. Each ideal attempt passes with
conditional probability 1/2, adding at most n2^-K2<=2^-30 failure.
This cap also applies after an incorrect odd residue or earlier bit.

Stop before an acquisition would exceed Qcap, release the allocated
registers and output zero. Count all rejected labels, failed merges,
discarded roots and partial trees. There is one LE call per acquisition,
with h_extract from Section 5 and this exact Qcap. Every loop is fixed
in length or consumes acquisitions, so every branch terminates.

Expected ideal cost. A retained leaf qubit needs at most two original
acquisitions in expectation. A level-zero vector thus costs at most
2q acquisitions. A merge has conditional success at least 1-2^-kappa for
every pair of input tables. Put eta=1/(1-2^-kappa). The expected cost C_i
of VEC(i) satisfies C_(i+1)<=2eta C_i: each new attempt uses fresh copies;
conditional on the history, its expected input cost is bounded by 2C_i
and its failure chance is at most 2^-kappa. Summing over the probability
of reaching each attempt gives this recurrence without an independence
assumption between its cost and its outcome. Moreover

    eta^m <= exp(m/(2^kappa-1)) <= e <3,

since 2^kappa>=2m. Each ideal tree therefore costs at most 6A* originals
in expectation. The odd decoder uses exactly F trees. Each truncated
2-adic search uses at most two trees in expectation; width-one searches
use at most two originals. Thus the total expected source use before the
global source cap is at most Qstar. Markov's inequality bounds the source
cap loss by 2^-10. The analysis couples capped and uncapped runs; it does
not condition a returned root on the cap not being reached.

## 12. Success for all orders and all secrets

On the strided branch, Section 9.3 proves Pr[E fails]<2^-190.
Conditional on each Llow in E and Fitodd, Sections 9.4--9.5 give total
odd decoder failure at most 2^-20. Avoiding the global source cutoff
implies Fitodd. Thus that conditional bound can be integrated and then
combined with the unconditional source-cap loss. We do not condition the
root law on the later adaptive 2-adic cap event.

The global source cap has failure at most 2^-10 by Section 11. All actual
label extractions together add at most 2^-14. The 2-adic attempt cap adds
at most 2^-30. With the correct odd residue and earlier bits, each
accepted 2-adic X measurement recovers the next bit exactly. Therefore

    Pr[wrong answer or abort]
      <=2^-190+2^-20+2^-10+2^-14+2^-30<2^-8.

These are additive pool, first-error, cutoff and coupling bounds. No law
is obtained by conditioning the actual run on correct extraction. The
ideal low construction record excludes accepted high bits and extractor
transcripts; earlier measured roots use disjoint top-bit sets.

The ordinary fallback retains its seed and one-bit bounds, hence failure
at most 2^-20+2^-30+2^-30+2^-10+2^-14<2^-8 with the present extractor.
For M=1 there is no odd decoding error. The n<64 exhaustive branch has
failure at most 2^-10. Thus for every N>=2 and every s, including all
finite fallback cases, unconditional full-secret success is at least
1-2^-8>2/3 under the independent ideal source promise.

## 13. Every-branch resource bounds

In this section n>=64. The finite branch has an absolute bound and is
absorbed in the constants. Put E=2^(sqrt n). Section 7 gives

    m<=r*, lam_i<=lam*, nq_D=2^m q<=A*,
    A*<6sqrt(n)E, 2^(lam*)<18sqrt(n)E.

The bounds are uniform over all tree sizes, including small 2-adic
trees. No monotonicity of m or q in B is assumed.

### 13.1 Source cap and exact extraction

For M>1, q_odd=nq_d<=A*, ell=ceil(log2 q_odd)=O(sqrt n) and
C=6A*. Thus log2 C=O(sqrt n), log2 A=O(sqrt n) and h=Omega(sqrt n)
uniformly over all odd-part trees of bit length n. In particular h tends
to infinity uniformly. The executable h<16 fallback can therefore occur
at only finitely many bit lengths. The interval 64<=n<256 is also finite.
Each such length has finitely many moduli and secrets, and all its branch
costs have explicit caps. Their finite maximum changes only an absolute
outside constant in each asymptotic bound below.

On the eventual strided branch, Delta=Theta(log n), nu=O(log n),
Kseed=O(sqrt n), Kback=O(log n), and Section 9.6 gives F=O(n).
The ordinary finite cases are absorbed as above, while M=1 has F=0.
Consequently the selected exact source cap satisfies uniformly

    Qcap=O(n A*+n)=O(n^(3/2)2^sqrt n).                 (13.1)

For the strided branch this is exactly
1024[6A*(F+2n)+2n]. Every acquisition is checked before it occurs, so
Q<=Qcap on every branch. Expected ideal acquisitions are used only to
bound the probability of reaching the cap.

Since log2 Qcap=O(sqrt n), h_extract=O(sqrt n). The core work per
original copy for exact collective extraction is
O(n h_extract log(h_extract+2)+n^2)=O(n^2). Source transforms also cost
O(n^2) per copy. Control, measurement, reset, counters and gate generation
are included in these counts.

### 13.2 Deterministic charge for leaves and merges

Consider a tree of width B with parameters r,d0,q. At merge level i+1,
the input width is lam_i=q+min(i,d0). The output table has at most twice
the input length, or two rows at the root. Section 6 therefore gives
O(n2^lam_i) core work for this merge. This includes its arithmetic,
sorting, lookup passes, output labels and reset. All fields are O(n)
bits, and each index and residue width is O(sqrt n).

The two input ancestries contain at least 2^(i+1)q distinct acquired
original copies. Divide the merge cost equally among those copies.
At a fixed level, the ancestry sets of different attempts are disjoint.
Failed inputs are discarded and never reused. Each original copy can
therefore receive at most one such charge at each level, even when the
run stops during a failed or partial tree. Its total merge charge is
bounded by a constant times

    (n2^q/q) sum_(i=0)^(m-1) 2^(min(i,d0)-i).

The sum is at most d0+2: it has d0 unit terms before the fixed-width
segment and a geometric tail of sum at most two. A leaf table costs
O(n2^q), and consumes q retained originals, so it adds O(n2^q/q) per
original. The total charge per acquired original is thus

    O(n(d0+3)2^q/q).

Rejected copies that never enter a leaf have no table charge. The charge
also includes all successful ancestors, failed attempts, discarded root
attempts, and partial work at the source cap.

For r=1,2,3 direct calculation gives d0<=r/2. For r>=4 use
sqrt r<=r/2. Thus q>=r-d0>=r/2. Since 2^kappa<4r,

    2^q/q=2^(kappa+1+r-d0)/q=O(2^(r-d0)).

The charge per original is consequently

    O(n(d0+3)2^(r-d0)).                              (13.2)

For every r>=1, sqrt r-1<=d0<=sqrt r. Define

    f(t)=(sqrt t+3)2^(t-sqrt t), t>=1.

Both factors increase: the derivative of t-sqrt t is
1-1/(2sqrt t)>0. Therefore

    (d0+3)2^(r-d0)<=2f(r*)
      =O(n^(1/4)2^(sqrt n-n^(1/4))).

The last estimate uses r*<sqrt n+1 and sqrt(r*)>=n^(1/4). It is
uniform over B<=n, including all floors and small tree widths.
Multiply (13.2) by (13.1). The full leaf and merge core work is

    O(n^(11/4)2^(2sqrt n-n^(1/4))).          (13.3)

### 13.3 Decoder, source work and setup

All acquired copies together need

    O(n^2 Qcap)=O(n^(7/2)2^sqrt n)

core work for extraction and source transforms. This fits (13.3), since
the ratio of these representative envelopes is
n^(3/4)2^(-sqrt n+n^(1/4)), which tends to zero. Root bookkeeping costs
O(n) per returned root; every root consumes at least one acquisition.

On the strided branch, the seed has Sseed stages and Kseed records.
Section 9.6 gives its streamed core work as

    O(n q_odd(ell^2/L+ell))+poly(n)
       <=O(n^2 q_odd)+poly(n)=O(n^(5/2)E)+poly(n).

This fits (13.3), even after the address charge below. The finite ordinary
fallback is absorbed in the absolute constants. A backward block streams
at most 2^Delta<=sqrt n candidates; all its exact products, table scores
and comparisons have polynomial core work, conservatively
O(n^(7/2)log n). Physical scales and dyadic denominator exponents remain
O(n).

Parameter computation, counters, exact CRT, source-transform constants,
trigonometric table generation and final rounding use polynomial work
and space. Each fixed polynomial fits (13.3); its finite prefix is
absorbed in the absolute constant. Circuits are generated from the
explicit arithmetic and tables. All initialization, measurements,
resets and memory access are charged.

### 13.4 Space and total charged work

The depth-first index stack uses fewer than 4n qubits by Section 7.
An active merge adds O(sqrt n) scratch. The extractor and source
transforms each use O(n) qubits. Each returned root is measured at once,
and released registers are reused. Thus S_Q=O(n) on every branch.

There are O(m+1) live classical tables, each with at most 2^lam* rows.
A stored high part has at most B+1+i+ceil(log2 q)-p_i=O(n) bits.
Common residues have at most n bits. Hence

    S_C=O((m+1)n2^lam*)+poly(n)=O(n^2 E).

Merge scratch is O(2^lam* sqrt n)=O(nE). The current seed records,
running scores, extraction counters and circuit-generation scratch
have polynomial size. They are included in the displayed space bound.
All field widths and allocations also apply on wrong-label and abort
branches. No circuit descriptions for the whole run are stored.

The address charge is log2(S_C+S_Q+2)=O(sqrt n). Apply (2.1) to (13.3)
and add the smaller literal source charge (n+1)Qcap. The total charged
sequential work is

    T=O(n^(13/4)2^(2sqrt n-n^(1/4))).        (13.4)

## 14. Structured envelopes

The declared representative envelopes are

    B_T(n)=n^(13/4)2^(2sqrt n-n^(1/4)),
    B_C(n)=n^2 2^sqrt n,
    B_Q(n)=n,
    B_samples(n)=n^(3/2)2^sqrt n.

The time exponent has coefficient 2 at power 1/2 and coefficient -1 at
power 1/4. The classical and sample exponents each have coefficient 1
at power 1/2. These are exact rationals, as are the outer powers.
The four structured objects in submission.json state these envelopes.

For time,

    log2 B_T=2sqrt n-n^(1/4)+(13/4)log2 n,
    (log2 B_T)/sqrt n ->2.

For classical space and source copies, (log2 B)/sqrt n tends to 1.
It follows for each of these three envelopes that

    log2(log2(max(4,B(n))))/log2 n ->1/2.

For B_Q=n the limit is zero. Thus the exact growth indices are
1/2, 1/2, 0 and 1/2.

## 15. Source error tolerance

For every N>=2 and s in Z/NZ the tolerance is epsilon(n)=0, where
n=ceil(log2 N). The exact declared error-model text is:

    Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

Thus the allowed malformed count is floor(0 Q)=0. Under this promise,
Sections 11--13 give unconditional full-secret success at least 1-2^-8
and all four resource bounds jointly, on every execution branch. The
finite n<64 branch has the same promise. No positive malformed fraction
is covered by this theorem.
