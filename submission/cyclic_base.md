# CS1-WINDOW: cyclic-window collimation with source-aligned decoding

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single
algorithm CS1-WINDOW below receives N in binary and fresh independent copies of rho_s,
and outputs the entire s with unconditional probability at least 1 - 2^-8 > 2/3.
On EVERY execution branch (including every failure, retry, discard and abort)
it satisfies jointly

    T   = O(n^3 2^(sqrt(2n))),
    S_C = O(n^2 2^(sqrt(2n) - 16 (2n)^(1/4))),
    S_Q = O(n),
    Q   = O(n^(5/4) 2^(sqrt(2n)-16(2n)^(1/4))).

The displayed resource envelopes are asymptotic for n>=2. All logarithms
inside the controller mean their stated integer ceilings; the n=1 case uses
the finite branch. A fixed absolute constant covers every n>=1.

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
n^3 2^(a sqrt n), 2^(a sqrt n - 19 n^(1/4)), n, and 2^(a sqrt n - 19 n^(1/4)),
with exact growth indices 1/2, 1/2, 0, 1/2 (Section 14). The fifth claim is the
clean-input tolerance 0 (Section 15).

Notation used throughout:
- d = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known integer. A "multiplier" W is an integer frequency factor.
- hd denotes a Hamming distance. T denotes total work only.

## 1. Sources and the algorithmic change

CS1-WINDOW modifies CS1-SAB, public submission
d06db402-97ca-43ce-8337-715e6152eebc, evaluated at commit
316a11cc7143fd483b578ec5cf23622f861f67d9. It retains its source-aligned
backward decoding and fixed16 schedule, but replaces discarded-remainder
block selection by the cyclic-window instrument in Section 6. The lower
failure bound proved there permits the fixed choice kappa=2 and removes a
sqrt(n) factor from the tree ledger. The complete construction is below.

The predecessor CS1-SAB cites CS1-BLC16L, public submission
effe7602-1685-4fd7-b6a2-b2be4d191c4d, evaluated commit
084eca871169a15a171fa1bbfe2fd30e0e9de997. Its actual submission/proof.md has
SHA256 ba0dc0a4fcfe3739bd0cf36e12649db27643adea12f18e1779c570a6651a2a3c;
submission/submission.json has SHA256
767f7c84703eb03f917abf9f676def176af2b5ebaf3bf54f87197a000699aa14.
Sections 2--8 and 10 below restate that construction. No accepted verdict is
a proof premise. Its material published lineage includes:

- CS1-LBQ, 603d96b1-a332-49a9-90ca-ef5cb6b8a5f2: linear merge, leaf boost,
  source transforms and Pell coefficient; evaluated 4456e60ff6e0edec393bc48478e03495b0767869,
  proof SHA256 1509a51e074b9a3f5f91fec57dd550cd192b26fca98e1da7340191d2dc374241.
- Exact collective tests, 844c0fd2-9b1c-4e84-a37c-f402e109985f:
  evaluated 7c4b4ed099799e146213c1e3c43a50151482dc6b, proof SHA256
  c0c011d54153f5e9c8f7436e581a42942e820689e0f52cef6cb8e02e7f1fce96.
- CS1-BACKWARD, 70936e29-d357-4713-b84f-47acebe365fd:
  evaluated d50e5146cf9f3c924c1cf26e0e725a3f3d2e5ad3; source member
  submission/leap-research/decoder-wave/CS1-BACKWARD/proof.md, SHA256
  40dcb36879994c071f43235c1f2ce28080020265c7c514c8e179ad1f51a73e3f.
- CS1-C3L, cafd8e10-c7b0-4b97-ac39-c4bd8e7315b0:
  evaluated 8d020246585004cdeb25c2906a02dd6512890360, proof SHA256
  9e9799a01eaeb752df4e1b8db1b9934fb0156739197dcb2a6e8eb2be4eb86164.

The collimation idea is from G. Kuperberg, arXiv:1112.3333v1, Algorithm 4.1.
Its Proposition 4.2 assumes QRACM, and Section 4.5's coefficient estimate is
heuristic. Section 4.6 also uses a special square-bitlength hidden-shift
setting. None supplies the charged all-N bound claimed here: explicit
lookups, rank maps, retry estimates and source reductions are proved below.
A. Yu. Kitaev, quant-ph/9511026v1, Section 3 equations (16)--(19) and Lemmas
9--10 describe eigenphase tests. Here the only controlled unitaries are
explicit modular translations, not control or inversion of the source.

The new lever is the number of roots: large odd moduli allow a computed
integer source shift to align the next two inverse lifts to X eigenstates.
The alignment error has a geometric seed part and an O(1/M) rounding part.
A size test bounds their sum. Small odd moduli keep scored lifts and have
only O(sqrt(n)) such steps. Both branches need O(n) expected roots.
There is no added rotation synthesis, numerical oracle, QRAM or postselection.

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
4. Put T = 2^lam'. Prepare a new lam'-qubit register V uniformly over
   r = 0,...,T-1 using Hadamards. Coherently compute z = (R-r) mod sz
   into a fresh register. Here sz is the exact measured bucket size; the
   modulo-sz arithmetic is a reversible classical circuit, extended by the
   identity outside its valid range. Measure z and reset its register from the
   measured classical value. Compute (z+r) mod sz from V and XOR it into R,
   clearing R, then uncompute the scratch. Retain V.
5. For v in [0,T), let rank_v = (z+v) mod sz and find the unique pair
   (x_v,y_v) in S_e of that rank using the ordered partner runs and offsets.
   The inverse map is implemented by a single sweep in cyclic rank order,
   wrapping once, costing O(L+T) iterations. From V, LOOKUP v -> (x_v,y_v)
   and XOR into x,y to clear them. Output V with the label table whose v-th
   entry is al[x_v]+be[y_v]. Store its common residue and high parts as in
   (6.2) below.

For the output table put sv = hA[x_v]+hB[y_v]+car, so sv is congruent to e
modulo 2^b. Then

    lab[v] = (cA+cB-car 2^p + 2^p e) + 2^(p+b) floor(sv/2^b).      (6.2)

The first term lies in [0,2^(p+b)) and is independent of v. On FAIL both
inputs are reset and released and never reused. All registers have fixed
widths, so memory is allocated deterministically.

Correctness. Given a bucket of size sz, the pre-window state has the form
sz^(-1/2) sum_(j=0)^(sz-1) exp(2 pi i lab_j th)|j>. Tensoring the uniform V
and measuring z=(j-r) mod sz gives, for EACH z, probability exactly 1/sz:
there are exactly T orthogonal preimages, one for each r. Clearing j leaves

    T^(-1/2) sum_(r=0)^(T-1) exp(2 pi i lab_((z+r) mod sz) th)|r>.

Thus the output has exactly equal amplitudes and T distinct incidences; no
incomplete block is discarded. The probability is independent of phases.
The bucket measurement and the cyclic window outcome depend only on bits
below p+b and on fresh measurement randomness. A measurement implementation
may use the computed rank register above and ordinary basis measurements.

Lemma 6.1 (bucket bounds). For ANY input tables, FAIL is exactly the event
that the measured bucket has size <T and has probability at most
2^b(T-1)/2^(2lam). Suppose additionally that the pair-row labels are sums of
independent uniform D-bit source labels with distinct 0/1 incidence vectors,
and that, conditional on the complete past below p, all source bits at or
above p remain independent uniform. If p+b<=D, and
2^(2lam-b) >= 4T, then the conditional mean FAIL probability is <1/T.

Proof. The first bound counts fewer than T failing rows in each of 2^b buckets.
For the second, condition on all source labels' low p bits, every earlier
low-bit transcript, and all current row-incidence vectors. Their high b-bit
blocks are independent uniform in Z/(2^b). Write M=2^(2lam), choose a uniformly
random row r, and let C count OTHER rows whose next b bits match its sum.
For two distinct rows v,w different from r, the binary reductions of their
coefficient differences v-r,w-r are distinct nonzero incidence vectors.
They are linearly independent over F_2; an odd 2x2 minor makes the pair of
linear forms surjective and uniform modulo 2^b. Known carries from the low
p bits only translate the outputs. Therefore the collision indicators are
pairwise independent with mean 2^(-b), so

    mu_C=(M-1)/2^b >= 4T-1,    Var(C)<=mu_C.

The measured bucket is selected with probability proportional to its size,
which is exactly equivalent to picking r uniformly. Its size is 1+C. The
failure event C<T-1 is bounded by Chebyshev:

    Pr(C<T-1) <= mu_C/(mu_C-(T-1))^2 < 1/T.

The inequality holds for all mu_C>=4T-1 and T>=2. The last output length in
this tree is T=2 and can instead use the unconditional 1/4 bound from the
first part. For b=0 the failure event is impossible because M>=4T.

Freshness invariant. For any tree node, condition on a transcript containing
only the low p bits of each source label used in that node, previous bucket
and window outcomes, their retry decisions, and any earlier external history
independent of the current fresh source copies. The remaining source blocks
are independent uniform. At a leaf this follows from the accepted label law.
Each merge computes its bucket and cyclic rank order from bits below p+b;
the bucket measurement has probability sz/M and z has conditional probability
1/sz, both independent of phases and higher source bits. Thus the enlarged
low transcript determines the output incidence list while leaving the bits
above p+b independent and uniform. Retried subtrees use disjoint fresh copies.
This induction also includes the uniformly sampled window outcome; no claim
is made after conditioning on high label-table entries or private extractor
transcripts. Distinctness of incidences follows from tensoring disjoint leaf
sets and the injective cyclic-window rank map.

Cost. Write L = 2^lam and L' = 2^lam'. A merge makes eight lookup passes of L
rows and one of L' rows, each with O(lam + b) bit fields. Classically it
performs O(L lam) comparisons of (b + lam)-bit keys, O(L) binary searches of
O(lam) steps on b-bit keys, and O(L') additions of high parts of at most
O(n) bits. With lam, b = O(sqrt n) (Section 7), this is O(n (L + L')) core steps.
The quantum scratch is O(sqrt n) beyond the two index registers. The classical
scratch (order, pos, lo, cnt, off, Dx, aa, bb and the inverse cyclic-window table) is
O((L + L') sqrt n) bits, and the output table is L' fields of w' bits plus
p + b bits for c'.

## 7. The tree TREE_D

Input: a supplier of LEAF QUBITS. Each is a positive qubit with a known label
uniform on [0, 2^D), D >= 2, independently. Put B = D - 1, the number of bits to
collimate. The parameters are computed by exact integer arithmetic:

    mu = ceil(sqrt(2B)) + 1,  kappa = 2,
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
    m+x <= r+2048,
    m+x-s <= r-16u+2048,
    A(B) <= 2^2070 u 2^(r-16u).

The exact bit capacities satisfy

    sum_i bmax_i = m(m+1)/2-s(s-1)/2+x(m+1)+kappa >= B,
    bmax_i+lam_(i+1)-2lam_i = -kappa.

Consequently, every non-root merge fails with conditional probability less
than 2^(-q) under the freshness invariant of Lemma 6.1; the root fails with
probability at most 1/4 for arbitrary input tables. Their product of expected
retry factors is less than 3.

Proof. First r+1<=mu<=r+2. Therefore

    floor(sqrt(mu)) > u-1,
    floor(sqrt(mu)) <= sqrt(r+2) <= u+1.

Since kappa=2 and x0=ceil(log2(3))=2, while 16floor(sqrt(mu))>=16,
we have x=16floor(sqrt(mu)) and q=x+3. Hence 16u-16<x<=16u+16
and q<=16(u+1)+3<=35u<=64u for u>=1. This proves the first two bounds.

The depth proof needs only x>=0 and s^2<=256mu. Let
j0=ceil(sqrt(2B+s^2)). The capacity condition holds at j0, apart from
the lower bound j>=s+1. Concavity gives

    sqrt(2B+s^2) <= r+128mu/r
                       <= r+128+256/sqrt(2) < r+310.

Since s+1<=mu, it follows that m<=mu+512.

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

The capacity identities follow by adding the capacities and substituting the
growing, capped, and root lengths. To bound retry factors, every non-root
output length is at least 2^q. Lemma 6.1 and the freshness invariant give
failure probability <2^-q for each non-root merge after averaging its two
freshly prepared children conditional on the low-bit transcript. The root
failure is <=1/4 for all tables. For k=floor(sqrt(mu))>=1, m<=mu+512<
(k+1)^2+512 and q=16k+3, so m 2^-q < 1/100 (the bound decreases with k).
Thus

    (4/3)(1-2^-q)^(-(m-1)) <= (4/3) exp(2m 2^-q) < 3.

The recurrence is for independently regenerated whole input pairs; it does
not condition on the full high label table of either child. The cost of an
attempt may be correlated with its success. Summing over attempts still gives
expected cost E[attempt cost]/Pr(success), since each whole attempt is fresh.
This proves the lemma.



Allocate b_(m-1), b_(m-2), ..., b_0 in that order greedily, b_i = min(bmax_i,
B - (already allocated)). Then sum_i b_i = B. Put p_0 = 0 and p_(i+1) = p_i + b_i,
so p_m = B, and let nq_D = 2^m (kappa+1+x) be the number of leaf qubits per tree.
Substituting directly in all three cases (growing levels: lam_(i+1) = lam_i + 1 and
bmax_i = x + i = lam_i - kappa - 1; capped levels: lam_(i+1) = lam_i and bmax_i = x + m - s + 1
= lam_i - kappa; root: lam_m = 1 and bmax_(m-1) = 2 lam_(m-1) - kappa - 1) gives

    b_i + lam_(i+1) - 2 lam_i <= bmax_i + lam_(i+1) - 2 lam_i = -kappa,        (7.1)

so 2^(2lam_i-b_i) >= 4*2^lam_(i+1). Lemmas 6.1 and 7.1 give the stated
level-wise retry bounds; the root uses the distribution-free bound.

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
kappa=2, x=O(n^(1/4)), and 2^kappa=4, with absolute
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
sort key, rank and cyclic-window selection uses only label bits below position B,
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

## 9. Odd-part root supplier and two backward modes

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

### 9.2 Terminal seed and deterministic choice of backward mode

Assume n>=64 and M>=3. Use the exact tree R=nq_d and ell=ceil(log2 R).
Set

    H = ceil(log2 M), L = ell+7,
    nu = ceil(log2(n+ell+8)),
    K_seed = 32768(ell+nu+40), K_back = 512(nu+30),
    K_odd = ceil(log2 n)+30, v_n = ceil(sqrt n),
    M_cut = 1024 * 2^ell * v_n.

All are computed by integer arithmetic (integer square root and bit length).
Choose LARGE mode if M>=M_cut, SMALL mode otherwise. This choice depends
only on N. The seed is the same in both modes.

#### 9.2.1 Seed at physical scales H through H+L

Localize phi=2^H theta mod 1. At each local stage u=0,...,L, obtain
K_seed unshifted roots using the supplier of Section 9 at physical scale
H+u. Measure each in an independent fair X/Y basis, recording (W,beta,Z).
Use the dyadic grid with denominator 2^P_u, P_u=u+ell+8, and score

    score(c) = sum_i Z_i tab_beta_i(2^u W_i c mod 1).

Stage zero enumerates the entire grid. Stage u>0 enumerates its points in
the closed circular arc of radius 2^(-u-2) around the preceding center.
The arc endpoints are grid points. Stream candidates, retain the least
maximizer, and release the records before the next stage.

Here is the success proof with all confidence factors. Conditional on
earlier stages being correct, the true phi lies in the enumerated arc.
A nearest grid candidate c0 satisfies |2^u W(phi-c0)|<=2^-8 modulo a
consistent local representative, using |W|<2R and R<=2^ell. Its exact
per-record mean score is at least cos(pi/128)/2. A far candidate at
circular distance >=2^(-u-3) from phi has

    2^u ||phi-c|| in [1/8,1/2],

because the incoming localization error and current arc radius are each
at most 2^(-u-2). At u=0 the full circle gives the same upper endpoint.
By (8.2), its mean score is at most cos(pi/8)/2. This remains true after
conditioning on the past before each fresh root. For an exact single
score Z cs_beta in [-1,1], the centered martingale increments have
absolute value <=2. Azuma at deviation K_seed/64 gives one-sided error

    exp(-K_seed/32768) <= 2^(-ell-nu-40).

There are at most 2^(ell+8) grid candidates at stage zero and fewer at
later stages, so the near and far one-sided events number at most
2^(ell+10). The table approximation adds at most K_seed/625 to each
score. A strictly positive exact margin after the two deviations and
two table errors is

    [9/128 - (22/7)^2/(2*128^2)
       - (22/7)^4/(24*8^4)]/2 - 2/64 - 2/625
       = 4372721/73758720000 > 0.

This uses 3<pi<22/7 and the elementary cosine bounds. Therefore stage
u returns a center within 2^(-u-3) except with probability at most
2^(-nu-30)<=2^-30/(n+ell+8). A first-error union bound over ell+8 stages
is at most 2^-30, which we conservatively charge as 2^-20 below.
The last center z_H has denominator 2^(2ell+15) and

    ||2^H theta-z_H|| <= e0 = 2^(-ell-10) <= 1/(1024R).       (9.1)

The seed uses F_seed=(ell+8)K_seed roots. No stage conditions the source
distribution on correct extraction or on a global resource cap.

#### 9.2.2 SMALL mode: retain the scored inverse lifts

For j=H-1,...,0 form u0=z_(j+1)/2 and u1=(z_(j+1)+1)/2, acquire
K_back unshifted roots at physical scale j, and use Section 9.1's
two-candidate score. Set z_j to the selected lift.
The incoming radius is at most e0 and halves at each correct lift.
Section 9.1 applies because e0<=1/(64R). The conditional error per step
is exp(-K_back/512)<=2^-30/(n+ell+8), so the entire small backward pass
adds at most 2^-30. Its exact root count is H K_back.

The size test proves this count is O(n), not O(n log n):

    M<M_cut implies H<=ell+10+ceil(log2 v_n)=O(sqrt n),
    H K_back=O(sqrt(n) log n+(log n)^2)=O(n).

The last statement uses ell=O(sqrt n), proved from Section 7, and
log n=O(sqrt n). This is an actual bound for the selected small-M branch.

#### 9.2.3 LARGE mode: align the fresh sources before collimation

For j=H-1,...,0 form the same exact candidates u0 and u1. Compute

    t = floor(M u0 + 1/2),
    b = (2^j)^(-1) t mod M,  in [0,M).

The inverse exists because M is odd. The dyadic multiplication and
rounding are exact integer operations; ties round upward. Since u0<1/2,
t lies in [0,M), and |u0-t/M|<=1/(2M).

Make at most K_odd independent root attempts. For every original copy
used by this attempt, apply Shift_b FIRST and Mult_alpha_j SECOND,
then use the same LE, k<2^d rejection, X and TREE_d as in Section 9.
Keep the first returned root with W odd. Even roots are discarded and
all their original copies remain charged. If all attempts have even W,
abort and output zero. On an odd root, measure X exactly: choose z_j=u0
on + and z_j=u1 on -. No trigonometric score or approximate rotation is
used in this mode.

This is a complete implementation of the aligned-root operation.
Shift_b maps rho_s to rho_(s-b), and Mult_alpha_j maps that to
rho_(alpha_j(s-b)). With B=d-1>=a2, the root phase is

    2^B W alpha_j(s-b)/N
       = W 2^j(s1-b)/M = W(2^j theta-t/M) mod 1.           (9.2)

The equality uses the stated CRT equation for alpha_j and
2^j b=t mod M. It does not require knowing s. Transformed copies still
have uniform independent latent labels even conditional on the complete
earlier decoder history. Their accepted labels are uniform D-bit strings.
Thus (8.3) gives probability 1/2 of odd W on every fresh attempt.
The expected number of attempts, including the capped failure case, is
at most two. A bit's parity-cap failure is at most 2^-K_odd, so the whole
odd-part parity-cap error is at most 2^-30. This rejection is an actual
bounded operation, not free postselection.

#### 9.2.4 Alignment error, adaptive decisions, and exact rounding

Let k=H-1-j, and condition only on the seed and earlier choices being
correct, before the new attempt. The true phase x=2^j theta is within
e0/2^(k+1) of exactly one of u0,u1. Write that lift as u_c=u0+c/2,
c in {0,1}. For a suitable circular representative delta,

    x-t/M = c/2+delta mod 1,
    |delta| <= e0/2^(k+1)+1/(2M).

For EVERY odd W, the root in (9.2) has X mean
(-1)^c cos(2pi W delta). Its probability of the wrong bit is exactly

    sin^2(pi W delta)
       <= 4 pi^2 R^2 [e0/2^(k+1)+1/(2M)]^2.              (9.3)

This bound is pointwise in W; it survives conditioning on odd W and
every earlier failed even attempt. No independence between the value
of W and its parity, or between an attempt's work and its success, is
asserted. The root law and the bit law are established in the ideal
process before imposing the global source cutoff.

Summing first-error probabilities and using (a+b)^2<=2a^2+2b^2 gives

    sum_(k=0)^(H-1) Pr[wrong lift at k | earlier success]
       <= (8/3) pi^2 R^2 e0^2 + 2 pi^2 H R^2/M^2
       <= (14/3)(22/7)^2/1024^2
        = 121/2752512 < 2^-14.                            (9.4)

Indeed sum_(k>=0)4^(-k-1)=1/3, H<=n, R<=2^ell, and the large-mode
test M>=1024*2^ell*ceil(sqrt n) bounds the second term. Both moduli
arbitrarily close to the threshold and phases near binary boundaries
are included. The source shifts used for tests do not change the stored
dyadic lifts: after a correct choice the approximation error still
halves exactly. In particular the O(1/M) test error is not accumulated
into the approximation center.

In either mode, if all choices are correct then

    ||theta-z_0|| <= e0/2^H <= 1/(1024 R M) < 1/(2M).

Return s1=floor(M z_0+1/2) mod M. It equals s mod M. The denominator
of z_0 is exactly represented with H+2ell+15 bits after the binary point.
Circular rounding includes theta=0, centers near one, and every binary
boundary. On every failure branch the same operations remain defined
and return an integer residue.

#### 9.2.5 Root budget

Set

    G_odd = F_seed + H K_back                 in SMALL mode,
    G_odd = F_seed + 2H                       in LARGE mode.

This is an upper bound on the EXPECTED number of returned roots in the
ideal process with the per-bit caps, uniformly after any decoder history.
In small mode it is also the exact count absent earlier abort. Both modes
satisfy G_odd=O(n), since F_seed=O(ell^2+ell log n)=O(n). The complete
algorithm below converts this expectation into every-branch resource
bounds by its explicit acquisition cutoff. It never uses G_odd as an
uncounted deterministic limit on a random number of attempts.

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
reindexes a cyclic window, so equal magnitudes persist. Its outcome and retry
law depends only on stored low labels. The top-bit and odd-W laws thus
remain valid. The displayed phase identity and exact parity conclusion
are used only when the odd residue and earlier bits are correct. Set bit
g of s2. In the ideal run with s1 correct, every accepted bit is correct.
Output (s1 + M s2) mod N.

## 11. Complete algorithm and every-branch cutoff

For n<64, enumerate cand=0,...,N-1. For each candidate acquire at most
n+10 fresh copies, apply Shift_cand, and measure the control in X. Reject
at its first minus. Output the first candidate passing every test, or zero
if none passes. The correct candidate always passes, and each wrong one
has all-plus probability 2^(-n-10), because the two data branches are
orthogonal. Failure is <=N 2^(-n-10)<=2^-10. Its deterministic finite
cost and N(n+10) sample bound are absorbed by absolute outer constants.

For n>=64 factor out powers of two, N=2^a2 M, using bit operations.
Compute the Section 7 schedules for 1<=B<=n and their exact maximum

    A_star = max_(1<=B<=n) 2^m(B)(kappa(B)+1+x(B)).

If M=1 set s1=0, G_odd=0 and skip Section 9. Otherwise run Section 9,
with its seed and size-selected backward mode. After obtaining s1, run
the 2-adic procedure of Section 10, with at most
K2=ceil(log2 n)+30 attempts per bit (or single-label attempts at width
one). If no accepted odd W or label-one appears, abort with output zero.
Output (s1+M s2) mod N.

Before any source acquisition, enforce the integer cutoff

    Q_star = 6 A_star (G_odd+2a2)+2a2,
    Qcap = 1024 Q_star.                                    (11.1)

If the next acquisition would exceed Qcap, stop and output zero. LE uses
this exact Qcap in h=ceil(log2(Qcap(n+5)))+14. Thus the label extractor is
fixed before the first copy. Every discarded Fourier label, even root,
failed merge and abandoned subtree consumes this same budget. All loops
either have explicit finite lengths or consume source acquisitions.

Expected source cost in the ideal process before the global cutoff:
each leaf qubit accepts an original label with probability >1/2 in the
odd-part supplier, and uses at most one original in the 2-adic supplier.
The new Shift_b and Mult_alpha_j are permutations producing independent
coset mixtures; they do not change either law. For a level i whole-attempt,
let p_i be its failure probability after averaging its two fresh child trees,
conditional on the prior external history. Lemmas 6.1 and 7.1 give
p_i<2^-q for non-root levels and p_i<=1/4 at the root. Attempts at a level
use fresh children and have the same law conditional on that history. Hence
C_(i+1) <= 2 C_i/(1-p_i), C_0<=2q: the sum over attempt reach probabilities
requires no independence between a successful attempt and its own cost. The
product of the retry factors is less than 3, so a returned tree uses at most
6A_star originals in expectation, uniformly after any external history. The
conditional averaging is over the children's unexposed high source bits; it is
not a claim of a bound for every fixed pair of full input tables.


For each requested aligned odd root or 2-adic parity, the next attempt's
cost is uniformly bounded by 6A_star and its acceptance probability is
1/2. Summing reach probabilities bounds expected cost by 12A_star, even
if its cost and its parity are correlated. Truncation only reduces this
expectation. Width-one searches use at most two originals in expectation.
Consequently the total is <=Q_star. Markov's inequality gives probability
at most 2^-10 of exceeding Qcap. This compares capped and uncapped ideal
runs; no distributional statement is conditioned on the cutoff succeeding.

Wrong earlier decoded bits do not invalidate this expected resource
bound: all leaf products still have equal basis magnitudes, and all merge
measurements and reindexing preserve that property. Their retry laws use
only stored labels. Every fresh source transform maps an independent ideal
copy to another ideal coset copy, irrespective of whether its chosen
classical shift is a correct estimate. In the 2-adic procedure the labels
remain uniform on the stated power-of-two range. Thus acceptance and
cost bounds hold even after a wrong decoder decision.

## 12. Joint success for every N and every s

On the n>=64 branch the ideal seed fails with probability <=2^-20.
Small-mode scored lifts add <=2^-30. Large-mode aligned lift errors add
<2^-14 and their parity cutoff adds <=2^-30. The two modes are mutually
exclusive. The 2-adic parity cutoff adds <=2^-30 and, when s1 and earlier
bits are correct, every accepted 2-adic measurement is exact.
The global acquisition cutoff adds <=2^-10. Section 5's label coupling
adds <=2^-12 for this Qcap. A single bound covering either mode is

    failure <= 2^-20 + 2*2^-30 + 2^-14 + 2^-10 + 2^-12
             < 2^-8.                                     (12.1)

All terms are first-error, truncation or coupling bounds for the original
unconditional process. No source label is conditioned on successful
extraction. On the finite branch failure is <=2^-10. Hence for every N>=2
and fixed s, one specified CS1-WINDOW configuration recovers the entire s
with unconditional probability at least 1-2^-8 > 2/3.

## 13. Every-branch resource ledger

Put Y=(2n)^(1/4), E=2^sqrt(2n), and u=(2B)^(1/4) for tree width B.
All fixed-size gates, generation, bit arithmetic, allocation and resets
are core steps as in Section 2. The final address factor is charged to
every such operation, not just to the quantum circuit.

### 13.1 The sample cutoff

By Lemma 7.1, A(B)<=2^2070 u 2^(u^2-16u). Because u<=Y and this
quadratic is convex,

    u^2-16u <= max(0,Y^2-16Y) <= Y^2-16Y+64.

Thus, without assuming a monotone integer schedule,

    A_star=O(Y 2^(Y^2-16Y)).                              (13.1)

In particular ell=ceil(log2 R)=O(sqrt n), nu=O(log n), and all physical
scales H+u and dyadic denominators have O(n) bits. The seed takes O(n)
roots. Section 9.2.5 proves G_odd=O(n) in each selected mode. With a2<=n,
the actual enforced cap (11.1) gives on every execution branch

    Q <= Qcap = O(n^(5/4) 2^(sqrt(2n)-16(2n)^(1/4))).      (13.2)

The missing log n relative to the preceding root budget is a consequence
of the source-aligned algorithm, not of an enlarged exponent coefficient.

### 13.2 Tree work, including the boosted leaves

A leaf of q=kappa+1+x qubits builds 2^q labels using O(n2^q) core work.
A merge producing level i+1 costs O(n2^(kappa+1+x+i)); its inputs have
consumed at least 2^(i+1)q original copies. At any fixed level, ancestry
sets of different attempts are disjoint: failed inputs are discarded and
never reused. Every original participates in at most m merge levels.
Charge the leaf and merges to those originals to get

    O(n(m+1)2^kappa 2^x/q) core work per acquisition.       (13.3)

This deterministic charge includes failed attempts and partial trees
abandoned by a cutoff. With m+1=O(sqrt n), 2^kappa=4, q>=x+1,
and x<=16Y+16, monotonicity of 2^z/(z+1) for z>=1 gives

    2^x/q <= 2^(16Y+16)/(16Y+17)
          <= 2^12 * 2^(16Y)/Y.

Every tree width therefore obeys the common bound

    C(n)=O(n^(5/4)2^(16Y)) core work per acquisition.

Multiplying this one uniform maximum by the actual cap (13.2) proves

    total tree core work = O(n^(5/2) E).                     (13.4)

There is no multiplication of independently chosen configurations.
The new source feedback is one additional Shift_b, O(n) core work per
copy. The original Mult_alpha costs O(n^2). LE costs
O(n h log(h+2)+n^2)=O(n^2), because log Qcap=O(sqrt n).
Their total is O(n^(13/4) E 2^(-16Y)), which is O(n^(5/2) E)
because 2^(16Y) eventually dominates every fixed power of n. Per-copy counters use O(sqrt n) bits.
Explicit source acquisition costs (n+1)Qcap are charged separately below.

### 13.3 Decoding, precision, and uniform setup

The seed enumerates at most 512R candidates at each of ell+8 stages,
using K_seed=O(sqrt n) records. In each circular interval initialize each
record's residue 2^u W c mod 2^P_u by schoolbook multiplication. For
consecutive candidates update by one O(n)-bit addition. The top twelve
bits select the fixed trigonometric table; score arithmetic has O(log n)
bits. Hence the seed takes

    O(n R(ell+8)K_seed)+poly(n) = O(n^2 R)+poly(n)
        = O(n^(9/4) E 2^(-16Y))+poly(n),

which is below (13.4). Only the current records, residues and maximum are
stored. No length-R score table is allocated.
Small-mode backward scoring is polynomial work using two candidates per
step and exact dyadic arithmetic. Large-mode feedback computes each t
and b by integer multiplication, division by a power of two, and modular
inversion/multiplication on O(n)-bit inputs. Schoolbook Euclid and modular
arithmetic give a polynomial total, with O(n^2) classical scratch if
desired. No coherent arithmetic is needed to choose b. The physical
Shift_b and Mult_alpha circuits were already counted per acquired copy.
On every branch at most H K_odd odd-part parity attempts and a2 K2
2-adic attempts occur; their measurement and controller costs are
polynomial or charged to acquisitions. All wrong-bit branches have the
same bounded integer widths.

The fixed table of Section 4 is generated, not supplied as advice.
All selection scores are rational table values; the aligned bit tests
are exact Clifford operations after exact modular permutations. All
schedule, cap, CRT, modular inverse, final rounding and circuit descriptor
calculations are bounded bit algorithms on O(n)-bit data, taking a fixed
polynomial in n. Such a polynomial is O(E) asymptotically, with a finite
prefix absorbed in an absolute constant. Gate descriptions are streamed.

### 13.4 Both peak spaces and charged addresses

Each tree has m=O(sqrt n), lambda_i=O(sqrt n), and the depth-first index
stack contains sum_i lambda_i=O(n) qubits. Active merge scratch is
O(sqrt n); one original source, LE and each modular permutation require
O(n) qubits. Roots are measured and released immediately after their
W is available. The feedback shift adds only the existing O(n) scratch.
Thus S_Q=O(n), including every failure and abort branch.

Level-i high-label fields are O(n) bits. The depth-first stack has O(m)
tables, each of length at most 2^(kappa+1+x+m-s). All merge scratch fits
the same bound, so

    S_C = O(n^2 2^(x+m-s))+poly(n)
        = O(n^2 2^(sqrt(2n)-16(2n)^(1/4))),              (13.5)

using Lemma 7.1 and the same convexity maximum over B<=n. The seed
records use O(n^(3/2)) classical bits, LE O(n log n), and feedback and
other setup polynomial bits, all absorbed in (13.5). Fields are allocated
at fixed widths even if numeric values or extracted labels are wrong.
Each allocation and eventual reset/release is included in the record or
per-copy charges. Only allocated memory is counted; no hidden preloaded
tables or stored exponential circuit descriptions exist.

The address length ceil(log2(S_C+S_Q+2)) is O(sqrt n). Multiplying (13.4)
and the smaller costs by this factor and adding (n+1)Qcap proves

    T = O(n^3 2^sqrt(2n)).                           (13.6)

Every source cutoff and parity cap is literal. Hence (13.2), (13.5),
(13.6) and S_Q=O(n) are joint every-branch bounds for the same algorithm.

## 14. Exact structured envelopes and indices

Use exactly the Pell rational a=u_333/v_333 from Section 0; no smaller
enclosure and no use of a-sqrt(2) to absorb work is made. Declare

    B_T = n^3 2^(a sqrt n),
    B_C = 2^(a sqrt n-19n^(1/4)),
    B_Q = n,
    B_samples = 2^(a sqrt n-19n^(1/4)).

The time bound is first proved with the actual sqrt(2n) exponent. For
classical bits and samples, 19^4=130321<131072=2*16^4, so
c=16*2^(1/4)-19>0. The ratios of (13.5) and (13.2) to their structured
envelopes are respectively bounded by n^2 2^(-c n^(1/4)) and
n^(5/4) 2^(-c n^(1/4)), which tend to zero. This uses only the inherited
fourth-root margin, not the positive Pell slack.

The logarithms of the three exponential representatives have leading
term a sqrt n, so their exact growth indices are 1/2. For B_Q=n the
index is zero. The four joint indices are therefore [1/2,1/2,0,1/2];
the only numeric objective is time 1/2. No index reduction is asserted.

## 15. Source error tolerance

The tolerance is epsilon(n)=0. All acquired copies must be independent
ideal coset states. No positive fraction of malformed copies is allowed
by this proof. This is a limit of the claim, not an impossibility result.

The exact error-model text shared with the fifth structured claim is:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.
