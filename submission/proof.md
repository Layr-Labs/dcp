# CS1-BLC16L: fixed16 leaf boost, backward decoding, exact collective tests, and cap 16

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single
algorithm CS1-BLC16L below receives N in binary and fresh independent copies of rho_s,
and outputs the entire s with unconditional probability at least 1 - 2^-8 > 2/3.
On EVERY execution branch (including every failure, retry, discard and abort)
it satisfies jointly

    T   = O(n^(7/2) (log2 n) 2^(sqrt(2n))),
    S_C = O(n^2 2^(sqrt(2n) - 16 (2n)^(1/4))),
    S_Q = O(n),
    Q   = O(n^(5/4) (log2 n) 2^(sqrt(2n)-16(2n)^(1/4))).

The displayed resource envelopes are asymptotic for n>=2. For bounds at
every n>=1, read each factor log2 n as max(1,log2 n). The n=1 case uses
the finite branch. This does not change any structured asymptotic envelope.

All outside constants are absolute. Define integers by (u_0, v_0) = (10, 7) and
(u_(k+1), v_(k+1)) = (3 u_k + 4 v_k, 2 u_k + 3 v_k). The map preserves u^2 - 2v^2, because
(3u + 4v)^2 - 2(2u + 3v)^2 = 9u^2 + 24uv + 16v^2 - 8u^2 - 24uv - 18v^2 = u^2 - 2v^2.
Hence u_k^2 - 2 v_k^2 = 10^2 - 2*7^2 = 2 > 0 and u_k/v_k > sqrt(2) for every k >= 0.
Let a = u_333/v_333. Written out in decimal (256 digits each),

    u_333 = 8441478004666748666153322414015794961054342923175177808658686557734489303162152388494751245868147491831446292476962720233203201073933816582585276436077865535199430405176591394221939485167179701583924490203278327423413823406808776174974568608124494762509770
    v_333 = 5969026340336944451114480739433819709407468170415945417713771714885974444504222882421291476798989652766383498455240579454394404150586732509003361709530480614304768144606668970442415970951831495263198155709406532002051594173677103082229495028847707209502393

and a = u_333/v_333 is the exponent coefficient in the three structured envelopes of
submission.json. Only a > sqrt(2) is used below.
Since a > sqrt(2), 2^(sqrt(2n)) <= 2^(a sqrt(n)) for all n >= 1. The declared envelopes are
n^(7/2) (log2 n) 2^(a sqrt n), 2^(a sqrt n - 19 n^(1/4)), n, and 2^(a sqrt n - 19 n^(1/4)),
with exact growth indices 1/2, 1/2, 0, 1/2 (Section 14). The fifth claim is the
clean-input tolerance 0 (Section 15).

Notation used throughout:
- d = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known integer. A "multiplier" W is an integer frequency factor.
- hd denotes a Hamming distance. T denotes total work only.

## 1. Sources and changes

This proof combines four public research submissions. No verdict is a premise.

- CS1-LBQ, 603d96b1-a332-49a9-90ca-ef5cb6b8a5f2: linear merge, leaf boost,
  source transforms, and the exact Pell coefficient.
- Exact collective tests, 844c0fd2-9b1c-4e84-a37c-f402e109985f: one modular
  register subtraction performs all level tests in one round.
- CS1-BACKWARD, 70936e29-d357-4713-b84f-47acebe365fd: one terminal phase
  localization followed by two-candidate backward steps.
- CS1-C3L, cafd8e10-c7b0-4b97-ac39-c4bd8e7315b0, evaluated commit
  8d020246585004cdeb25c2906a02dd6512890360: a quarter-power leaf boost
  and cancellation of its larger per-copy merge cost. The exact proof
  has SHA256 9e9799a01eaeb752df4e1b8db1b9934fb0156739197dcb2a6e8eb2be4eb86164;
  the relevant parts are Sections 7, 11 and 13.

The collimation construction comes from G. Kuperberg, arXiv:1112.3333v1,
Algorithm 4.1, Proposition 4.2 and Section 4.6. Its heuristic running time
is not a premise. The level tests are the standard Kitaev tests.

This configuration combines a fixed16 quarter-power leaf boost with the
backward decoder and length cap 16, and uses a direct exact
label extractor: every call uses collective tests at high confidence.
Thus there is no verifier, fallback, approximate Fourier transform, or
rotation compiler. Every component and its cost is specified below.

Relative to CS1-BLC16, the new algorithm change is the larger leaf boost.
It reduces the proved asymptotic source bound while preserving the actual
time and space bounds. The source count need not decrease at each finite N. The declared classical-space coefficient changes from -18
to -19 only because of a tighter rational conversion of the same actual
bound. That conversion is not a further algorithm improvement.

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

    J_e=n+4, h=ceil(log2(Qcap(n+5)))+14, F(h)=2^21 h.

Here Qcap is the exact source cap of Section 11. Each call executes the
fixed procedure RUN(F(h)) once, outputs its integer label, and resets
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
F = F(h) this is 2 exp(-h). So RUN(F(h)) returns a value other than k with
probability at most 4 (J_e + 1) e^(-h) = 4 (n+5) e^(-h), uniformly in k.
A call uses 2F(h) rounds, each with O(n) quantum core steps. Incrementing
all outcome counters costs O(n F(h) log(F(h)+2)) bit operations even without
amortization. There are O(n) counters, each of O(log(F(h)+2)) bits. Each of
the 64 direction scores per level is computed by integer arithmetic on
O(log(F(h)+2)) bits; the fixed table denominator is common to all scores.
Exact dyadic unwrapping and final multiplication and rounding cost O(n^2).
Therefore the total core work per call is

    O(n h log(h+2)+n^2)=O(n^2),

because Section 13 proves h=O(sqrt n), and log n=O(sqrt n). Quantum scratch
is O(n), classical scratch is O(n log n). All work is bounded on every
branch. To make the collective map total on the data encoding, first
compute [u<N] and apply the modular subtraction only on that subspace;
the data validity is preserved, so its flag can be cleared. This changes
neither the O(n) cost per round nor the action on the source.

For each call, conditional on its latent label and all earlier history,
its error probability is at most 4(n+5)e^(-h). Thus over at most Qcap calls,

    Pr[any wrong label] <= 4(n+5)Qcap e^(-h) <= 2^-12.

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

Input: a supplier of LEAF QUBITS. Each is a positive qubit with a known label
uniform on [0, 2^D), D >= 2, independently. Put B = D - 1, the number of bits to
collimate. The parameters are computed by exact integer arithmetic:

    mu = ceil(sqrt(2B)) + 1,  kappa = ceil(log2(mu + 512)) + 1,
    x0 = ceil(log2(kappa + 1)), x = max(x0, 16 floor(sqrt(mu))),
    s = min(mu - 1, 16 floor(sqrt(mu))),
    m = min{ m >= s+1 : m(m+1)/2 - s(s-1)/2 + x(m+1) + kappa >= B },
    lam_i = kappa + 1 + x + min(i, m-s) (0 <= i <= m-1),  lam_m = 1,
    bmax_i = x + i (0 <= i <= m-s-1),  bmax_i = x + m-s+1 (m-s <= i <= m-2),
    bmax_(m-1) = kappa + 2x + 2(m-s) + 1.

So leaves have kappa+1+x qubits (LEAF BOOST: x extra qubits per leaf), lengths grow by
one bit per level up to level m-s and then stay at 2^(kappa+1+x+m-s) for the last s-1
levels below the root (LENGTH CAP).

Lemma 7.1 (fixed16 boost and cap16). Put q=kappa+1+x and A(B)=q2^m.

Put r=sqrt(2B) and u=(2B)^(1/4), only for the proof. For every B>=1,

    16u-16 < x <= 16u+16,
    q <= 64u,
    m <= mu+512,
    2^kappa >= 2m,
    m+x <= r+2048,
    m+x-s <= r-16u+2048,
    A(B) <= 2^2070 u 2^(r-16u).

The exact bit capacities satisfy

    sum_i bmax_i = m(m+1)/2-s(s-1)/2+x(m+1)+kappa >= B,
    bmax_i+lam_(i+1)-2lam_i = -kappa.

Consequently, every merge still fails with probability at most
2^-kappa<=1/(2m), for every pair of input tables. The expected retry
factor along the tree is less than 3.

Proof. First r+1<=mu<=r+2. Therefore

    floor(sqrt(mu)) > u-1,
    floor(sqrt(mu)) <= sqrt(r+2) <= u+1.

For mu>=1024, the elementary bound

    log2(mu+512)+5/2 <= sqrt(mu-2)

holds. It holds at 1024, and the right derivative is larger thereafter:
mu+512 > 2sqrt(mu-2)/ln(2). Since x0<=kappa and
kappa<=log2(mu+512)+2, this gives x0<=floor(sqrt(mu)). Thus
x=16floor(sqrt(mu)) in this range. It also gives

    q=kappa+1+x <= 18sqrt(mu) <= 36u.

For mu<1024, kappa<=12 and x0<=4, whereas
16floor(sqrt(mu))>=16. Hence x=16floor(sqrt(mu)) for every B,
and the first bound follows from the displayed floor bounds. Also
q<=13+16sqrt(mu)<=13+32u<=45u<=64u in the small-mu range.
This proves the first two bounds.

The depth proof needs only x>=0 and s^2<=256mu. Let
j0=ceil(sqrt(2B+s^2)). The capacity condition holds at j0, apart from
the lower bound j>=s+1. Concavity gives

    sqrt(2B+s^2) <= r+128mu/r
                       <= r+128+256/sqrt(2) < r+310.

Since s+1<=mu, it follows that m<=mu+512. The definition of kappa
then gives 2^kappa>=2(mu+512)>=2m and 2^kappa<=4(mu+512).

For the stronger depth bound, complete the square. The capacity
condition holds for every j at least

    j1=ceil(sqrt(2B+s^2+(x+1/2)^2)-x-1/2).

Therefore m<=max(s+1,j1). If mu>=1024, then x<=16sqrt(mu), so
(x+1/2)^2<=257mu. To see the last bound, expand the square and use
16sqrt(mu)+1/4<=mu. Also r>=1022. Concavity gives

    s^2/(2r) <= 128mu/r < 129,
    (x+1/2)^2/(2r) <= (257/2)mu/r
                            <=257/2+257/1022 <129.

The ceiling adds at most one, so j1+x<=r+259. Further,

    s+1+x <= 32sqrt(mu)+1 <= mu+1 <= r+3

for mu>=1024. Hence m+x<=r+259 in this range.

If mu<1024, then m<=1535 and x<=496, so m+x<=2031.
This proves the uniform bound m+x<=r+2048.

For mu>=1024 we have s=x=16floor(sqrt(mu))>16u-16. Thus
m+x-s<=r-16u+275. For mu<1024, use the exact relation
s=min(mu-1,x). It gives

    x-s=max(0,x-mu+1)
         <=max(0,16sqrt(mu)-mu+1)<=65.

Thus m+x-s<=1600 in this range. Since u^2-16u>=-64,
both ranges give m+x-s<=r-16u+2048.

Finally, x>16u-16 and q<=64u imply

    A(B)=q2^m <=64u 2^(r+2048-x)
                    <=2^2070 u2^(r-16u).

The two capacity identities follow by adding the capacities and substituting the
growing, capped, and root lengths. The distribution-free merge bound
then applies without any change. Since 2^kappa>=2m,

    (2^kappa/(2^kappa-1))^m <= exp(m/(2^kappa-1)) < 3.

This proves the lemma.


Allocate b_(m-1), b_(m-2), ..., b_0 in that order greedily, b_i = min(bmax_i,
B - (already allocated)). Then sum_i b_i = B. Put p_0 = 0 and p_(i+1) = p_i + b_i,
so p_m = B, and let nq_D = 2^m (kappa+1+x) be the number of leaf qubits per tree.
Substituting directly in all three cases (growing levels: lam_(i+1) = lam_i + 1 and
bmax_i = x + i = lam_i - kappa - 1; capped levels: lam_(i+1) = lam_i and bmax_i = x + m - s + 1
= lam_i - kappa; root: lam_m = 1 and bmax_(m-1) = 2 lam_(m-1) - kappa - 1) gives

    b_i + lam_(i+1) - 2 lam_i <= bmax_i + lam_(i+1) - 2 lam_i = -kappa,        (7.1)

so by Lemma 6.1 every merge fails with probability at most 2^-kappa <= 1/(2m).

LEAF: take kappa+1+x leaf qubits as the index register (bit j = qubit j). Build
the table incrementally, lab[0] = 0 and lab[v + 2^j] = lab[v] + k_j for v < 2^j:
one addition per entry. The table has length 2^(lam_0), is collimated to p_0 = 0,
and in the ideal run is exactly the tensor product state.

Field widths. A level-i label (output of VEC(i)) is a sum of at most
2^i (kappa+1+x) leaf labels below 2^(B+1), so it is below 2^(B+1+i+gw) with
gw = ceil(log2(kappa+1+x)). Level-i tables are collimated to p_i and stored with
w_i = B + 1 + i + gw - p_i bits per high part.

VEC(i): if i = 0 return LEAF. Otherwise repeat:
- X1 = VEC(i-1);
- X2 = VEC(i-1);
- out = MERGE(X1, X2; p_(i-1), b_(i-1), lam_i);
- if out != FAIL, return out.

TREE_D returns VEC(m), a one-qubit phase vector with labels lab[0] and lab[1],
congruent modulo 2^B. Its ideal state is, up to global phase,
(|0> + exp(2 pi i 2^B W th)|1>)/sqrt 2 with the known integer

    W = (lab[1] - lab[0]) / 2^B = hi[1] - hi[0],                              (7.2)

because the root table is collimated to p_m = B.

Each label is a sum of at most nq_D leaf labels below 2^(B+1), so |W| < 2 nq_D.
Depth-first evaluation holds at most one finished sibling per level.

For B<=n and n>=64, the bounds above give m=O(sqrt n),
kappa=O(log n), x=O(n^(1/4)), and 2^kappa=O(sqrt n), with absolute
constants. Therefore every lam_i and b_i is O(sqrt n), every label has
O(n) bits, and sum_i lam_i=O(n). These are fixed width allocations.

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

## 9. High-scale seed and exact backward two-candidate decoder

If M=1 set s1=0 and skip this section. Otherwise M>=3, D=d, B=d-1>=a2,
R=nq_d and ell=ceil(log2 R). Write theta=s1/M. For ANY nonnegative physical
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
also at all terminal seed scales beyond the old stopping exponent.

The ONLY distributional root hypothesis used is exactly proved in Section8:
conditional on fresh-root low-only history G and independent past,
W=c_G+sum epsilon_l*tau_l with iid fair top bits, nonzero signed coefficients,
and |W|<2R. Thus |E exp(2pi i zW)|<=|cos(pi z)| and
Pr(W odd|G,past)=1/2. No stronger support lower bound, uniform W law, or
independent-subset-sum premise is assumed. Private extractor transcripts are
averaged out in the ideal run. Section12 couples the actual implementation.

### 9.1 Exact two-candidate backward lemma

Write ||x|| for circular distance to 0. Suppose a known dyadic center
z in [0,1) satisfies

    ||2x - z|| <= e,             e <= 1/(64R).

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
as decoding proceeds backward. It does not degrade by R per step.

### 9.2 One terminal seed, followed by the backward decoder

Assume n >= 64 and M >= 3. Set exactly

    H = ceil(log2 M),
    L = ell+3,
    nu = ceil(log2(n+ell+4)),
    K_seed = 8192(ell+nu+30),
    K_back = 512(nu+30).

#### 9.2.1 Seed at scale H

Apply the explicit localization algorithm below to the phase

    phi = 2^H theta mod 1

for local stages u = 0,1,...,L. Local stage u obtains roots at physical
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

    ||phi-z_H|| <= e_H = 2^-(ell+6) <= 1/(64R).

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

    ||theta-z_0|| <= 2^-(H+ell+6) <= 1/(64 R M) < 1/(2M).

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

    F = (ell+4) K_seed + H K_back.

Hence F = O(ell^2 + ell log n + n log n) = O(n log n).
After the seed, there are two candidates at each step, not O(R) candidate
suffixes. Initialization enumerates at most 2^(ell+8) <= 512R candidates
per stage, keeping only a running maximum and the measured root records.

For general independent parameters, this proof gives the quadratic-in-ell
initialization bound stated in Section 1. The step making it meet the
requested target is the PROVED CS1 bound ell^2=O(n); it is not an assumed
support-concentration property.

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

For n>=64 compute the parameters in Sections 7 and 9. If M=1, set s1=0
and F=0. Otherwise set

    F=(ell+4)K_seed+H K_back.

Set K2=ceil(log2 n)+30. In Section 10 allow at most K2 root attempts per
2-adic bit (or K2 single-label attempts at width one). If none has odd W,
or label one at width one, abort and output 0. Every ideal attempt passes
with probability 1/2 conditional on the past. This adds at most
n 2^-K2<=2^-30 to failure. This cap applies even after an incorrect
odd-part answer and ensures at most a2 K2 returned roots on every branch.

Compute all tree parameters for 1<=B<=n by integer arithmetic, and set

    A*=max_(1<=B<=n) 2^m(B)(kappa(B)+1+x(B)),
    Q*=6 A*(F+2a2)+2a2,
    Qcap=1024 Q*.

The main branch stops and outputs 0 before an acquisition would exceed
Qcap. This includes all rejected labels, failed merges and discarded
roots. There is one LE call per acquisition; its parameter h is from
Section 5 with this Qcap. Every loop is fixed in length or consumes
acquisitions, so every branch terminates.

Expected ideal cost. A leaf needs at most two original acquisitions in
expectation. A merge has conditional success at least 1-2^-kappa for
every pair of input tables. Put r=1/(1-2^-kappa). The expected cost C_i
of VEC(i) satisfies C_(i+1)<=2r C_i: each new attempt uses fresh copies;
conditional on the history, its expected input cost is bounded by 2C_i
and its failure chance is at most 2^-kappa. Summing over the probability
of reaching each attempt gives this recurrence without an independence
assumption between its cost and its outcome. Moreover

    r^m <= exp(m/(2^kappa-1)) <= e <3,

since 2^kappa>=2m. Each ideal tree therefore costs at most 6A* originals
in expectation. The odd decoder uses exactly F trees. Each truncated
2-adic search uses at most two trees in expectation; width-one searches
use at most two originals. Thus the total expected source use before the
global source cap is at most Q*. Markov's inequality bounds the source
cap loss by 2^-10. The analysis couples capped and uncapped runs; it does
not condition a returned root on the cap not being reached.

## 12. Success for all orders and all secrets

For n>=64, the ideal seed fails with probability at most 2^-20, the
backward choices add at most 2^-30, and the 2-adic attempt cap adds at
most 2^-30. With the correct odd residue, each odd-root X measurement
recovers the next 2-adic bit exactly. The global source cap adds at most
2^-10. The actual label extractor adds at most 2^-12. Hence

    Pr[wrong answer or abort]
      <=2^-20+2^-30+2^-30+2^-10+2^-12 <2^-8.

These are additive first-error and coupling bounds. No source label law
is conditioned on correct extraction or favorable outcomes. Fresh mixed
copies are used after every prior history. The finite branch has failure
at most 2^-10. Thus full-secret success is at least 1-2^-8>2/3 for every
N>=2 and every s, under the independent ideal source promise.

## 13. Every-branch resource bounds

For this section put Y=(2n)^(1/4), E=2^sqrt(2n), and, for each
tree width B, u=(2B)^(1/4).

### 13.1 Source cap over all tree widths

Define the exact integer

    A*=max_(1<=B<=n) A(B).

This finite maximum is computed by the stated integer parameter algorithm;
it does not assume that A(B), m(B) or x(B) is monotone. In fact,
u 2^(u^2-16u) is not monotone for all small u, so a monotonicity argument
would be invalid. Instead, u<=Y and convexity give

    u^2-16u <= max(0,Y^2-16Y) <= Y^2-16Y+64.

The second inequality follows from Y^2-16Y>=-64. Thus Lemma 7.1
implies

    A*=O(Y 2^(Y^2-16Y))
      =O(n^(1/4) 2^(sqrt(2n)-16(2n)^(1/4))).              (1)

This is uniform over every tree used in either part of the algorithm,
including small-width 2-adic trees. Width one uses single source qubits
and is handled separately.

Use the same all-N reduction. Put N=2^a2 M, with M odd, and
n=ceil(log2 N), d=floor(log2 N). If M>1, the odd-part trees have D=d,
B=d-1, R=A(d-1), and ell=ceil(log2 R). Set

    H=ceil(log2 M), L=ell+3, nu=ceil(log2(n+ell+4)),
    K_seed=8192(ell+nu+30), K_back=512(nu+30),
    F=(ell+4)K_seed+H K_back.

The phase seed uses physical scales H through H+L. The backward steps
use scales H-1 through 0. If M=1, skip the odd decoder and set F=0.
The 2-adic decoder permits K2=ceil(log2 n)+30 attempts per bit. Set

    Q*=6A*(F+2a2)+2a2,       Qcap=1024Q*.

Abort before acquiring original copy Qcap+1. Every rejected Fourier
label, discarded leaf, failed merge and discarded root counts. The cap
is enforced before acquisition on every branch, including a branch with
wrong labels or wrong decoded bits.

By (1), log R=O(sqrt n), so ell=O(sqrt n), nu=O(log n),
K_seed=O(sqrt n), K_back=O(log n), and H<=n. Therefore

    F=O(ell^2+ell log n+n log n)=O(n log n).

Consequently

    Q<=Qcap=O(n^(5/4) (log2 n)
                2^(sqrt(2n)-16(2n)^(1/4))).              (2)

For bounds at all n>=1, use max(1,log2 n); the structured representatives
are asymptotic. The unchanged finite branch covers n<64, including N=2.


### 13.2 Work with the larger leaf charge

The old O(n^2) merge charge per acquisition cannot be reused. The larger
leaf table costs more, and that factor must be retained until it is
multiplied by the new source cap.

A leaf table uses O(n 2^q) core operations. Divide this cost by its q
consumed originals. A merge producing level i+1 costs at most
O(n 2^(kappa+1+x+i)); its ancestry consumed at least 2^(i+1)q originals.
Its cost per such original is O(n 2^(kappa+x)/q). At one level, the
ancestry sets of distinct merge attempts are disjoint, since failed
inputs are discarded and never reused. Each original has at most m
ancestors. This is deterministic accounting, including abandoned partial
trees and abort paths. The total charge per acquisition from its tree is

    O(n(m+1)2^kappa 2^x/q).

Uniformly for B<=n, m+1=O(sqrt n) and 2^kappa=O(sqrt n). Also q>=x+1,
x>=1 and x<=16Y+16. The function g(z)=2^z/(z+1) increases for z>=1, since
its logarithmic derivative is ln(2)-1/(z+1)>0. Therefore

    2^x/q <= 2^x/(x+1)
           <= 2^(16Y+16)/(16Y+17)<=2^12*2^(16Y)/Y.

Every acquisition, at every tree width, consequently receives at most

    C(n)=O(n^2 2^(16Y)/Y)=O(n^(7/4)2^(16Y))                      (3)

core work from leaf construction and all merges. This bound uses a
single maximum over all widths. It does not multiply a cap at one B by
an incompatible width-dependent estimate.

Source transforms, label extraction and control work add O(n^2) per
acquisition. Indeed log Qcap=O(sqrt n), so direct collective LE uses
O(n h log(h+2)+n^2)=O(n^2) core work. This is included in (3), because
2^(16Y)/Y is bounded below for Y>=1. Root measurement costs O(n), and each
root consumes at least one counted original.

Multiplying (2) and (3) now gives

    C(n)Qcap=O(n^3 (log2 n) E).                          (4)

The two quartic exponent factors cancel. No positive slack in the Pell
coefficient is used in this work estimate.

### 13.3 Decoder work and setup

The seed enumerates at most 512R candidates at each of ell+4 stages,
with K_seed records. Initializing each of at most two intervals uses
schoolbook multiplication. Within an interval, each record's residue
updates by one O(n)-bit addition per candidate. Thus its core work is

    O(n R(ell+4)K_seed)+poly(n)
       =O(n^2 R)+poly(n)
       =O(n^(9/4) E 2^(-16Y))+poly(n),

which is below (4). The decoder stores only the current root records,
residues and running maximum; it does not allocate a table of R scores.
The backward steps have two candidates each and cost O(n^3 log n)
core work with schoolbook arithmetic. Their scores can be streamed.

Every physical scale and dyadic denominator exponent is O(n). Exact
CRT and modular multipliers, source-shift constants, parameter and cap
computations, trigonometric table generation, counters and final rounding
use polynomial work and space. Computing A* examines n exact schedules;
all their integers have O(n) bits. Every fixed polynomial is O(E) as n grows. Thus
these costs are absorbed in (4), with finite prefixes covered by an
absolute constant. There is no uncounted numerical or circuit oracle.

### 13.4 Quantum space, classical space and addresses

Every level has lam_i=O(sqrt n), since m=O(sqrt n),
kappa=O(log n), and x=O(n^(1/4)). The depth-first index stack has

    sum_i lam_i <= O(m(kappa+1+x+m))=O(n)

qubits. One active merge uses O(sqrt n) scratch. The exact label extractor
and each source transform use O(n). Measure each root when it is returned
and reuse released registers. Thus S_Q=O(n) on every branch.

A level-i label has at most B+1+i+ceil(log2 q)=O(n) bits. The fixed table
stack has O(m) tables, each of length at most 2^(kappa+1+x+m-s). Hence
its classical space is

    O(n^(3/2)2^(kappa+x+m-s))=O(n^2 2^(x+m-s)).

Merge scratch is smaller. For every B<=n Lemma 7.1 gives
x+m-s<=u^2-16u+O(1). The convex function u^2-16u on [0,Y] is at most
max(0,Y^2-16Y)<=Y^2-16Y+64. Uniformly over all tree widths, therefore,

    S_C=O(n^2 2^(sqrt(2n)-16(2n)^(1/4))).                (5)

The seed's K_seed records use O(n^(3/2)) bits. LE uses O(n log n)
classical bits. All remaining setup, counters and decoder storage are
polynomial. They are absorbed in (5). These are fixed field widths and
allocations, so wrong labels and failed paths satisfy the same bound.

The total memory address length is O(sqrt n). Charge it to every core
operation in (4), including circuit generation, and add the (n+1)Qcap
source cost. This proves

    T=O(n^(7/2) (log2 n) 2^sqrt(2n)).                    (6)

All four bounds hold jointly for this one configuration and on every
execution branch.


## 14. Exact structured envelopes and comparison

Keep the exact Pell coefficient a=u_333/v_333 from Section 0, with
u_0=10, v_0=7 and (u,v)->(3u+4v,2u+3v). It satisfies a>sqrt(2).
Declare

    B_T=n^(7/2)(log2 n)2^(a sqrt n),
    B_C=2^(a sqrt n-19n^(1/4)),
    B_Q=n,
    B_samples=2^(a sqrt n-19n^(1/4)).

The time and quantum bounds follow from (6) and Section 13.4. For both
classical space and source copies, 19^4=130321<131072=2*16^4, so
c=16*2^(1/4)-19>0. The ratio of the raw source bound (2) to B_samples is at most

    n^(5/4)(log2 n) 2^(-c n^(1/4)),

which tends to zero and is bounded. For classical space the corresponding
ratio is n^2 2^(-c n^(1/4)), also bounded. These conversions use only the strict
quartic margin; they do not hide a polynomial in a-sqrt(2).

The structured source object therefore has coefficient 1, exponent terms
(a,nPower=1/2,logPower=0) and (-19,nPower=1/4,logPower=0), and outer
nPower=logPower=0. Its exact growth index is 1/2. All other indices remain
(1/2,1/2,0), and tolerance is zero.

At the same exact a, compared with approved CS1-BLC16, time and quantum
space envelopes are unchanged. The actual classical-space bound is also
unchanged; its new declared coefficient -19 is a tighter rational
conversion of that existing bound. The actual new resource improvement
is the lower asymptotic source bound. This does not assert a smaller
source count at each finite N. The source-envelope ratio is

    2^(-19n^(1/4))/(n log2 n) ->0.

Compared with the cited C3L raw source bound n^(7/4)2^(sqrt(2n)-(2n)^(1/4)),
(2) gains a factor sqrt n*2^(15(2n)^(1/4))/log2 n. The combined time bound
gains a factor sqrt n/log2 n over C3L's n^4 2^sqrt(2n), and cap 16
improves its space term.

## 15. Source error tolerance

The tolerance is epsilon(n)=0. All acquired copies must be independent
ideal coset states. No positive fraction of malformed copies is allowed
by this proof. This is a limit of the claim, not an impossibility result.
