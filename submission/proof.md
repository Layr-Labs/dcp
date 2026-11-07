# CS1-WINDOW-P-MIN-E: fractional-depth space tradeoff

## 0. Theorem and notation

For every integer N >= 2 and every s in Z/NZ put n = ceil(log2 N). The single
algorithm CS1-WINDOW-P-MIN-E below receives N in binary and fresh independent copies of rho_s,
and outputs the entire s with unconditional probability at least 1 - 2^-8 > 2/3.
On EVERY execution branch (including every failure, retry, discard and abort)
it satisfies jointly

    T   = O(n^20 2^(c sqrt(n))),
    S_C = O(n^20 2^(beta sqrt(n))),
    S_Q = O(n),
    Q   = O(n^20 2^(beta sqrt(n))),

where P=u_333, c=sqrt(2+4/P^2), and beta=c-sqrt(2)/P.
These are raw bounds; Section 14 proves tighter supported envelopes.

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

and a = u_333/v_333 is the leading exponent coefficient in the time envelope.
Since a > sqrt(2), 2^(sqrt(2n)) <= 2^(a sqrt(n)) for all n >= 1. The declared envelopes are
E(n), E_b(n), n, and E_b(n),
with exact growth indices 1/2, 1/2, 0, 1/2 (Section 14). The fifth claim is the
heralded-erasure tolerance of Section 15. E and b are defined in Section 14; E_b in envelopes.md.

Notation used throughout:
- d = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with s = s1 + M s2 (mod N).
- omega = exp(2 pi i/N). Data basis states are |u>, u in [0,N), stored in n qubits.
- A "label" is a known integer. A "multiplier" W is an integer frequency factor.
- hd denotes a Hamming distance. T denotes total work only.

## 1. Sources and the algorithmic change

Section 15 adds a larger supported heralded-erasure guarantee using the
fixed identity a=10^32-1, b=d=1, c=1-a. All raw acquisitions continue
to be counted through the literal FILTER cutoff. This constant-factor
change is independent of the minimum-P schedule change below.

This candidate builds directly on public submission
a0fc67df-0e8b-4cf6-95bd-2f391e07aeb1 at evaluated commit
28f9e5cca09c5e9707ffcf2cc79a4295b415b931. It retains that algorithm and
all proof mechanisms, but changes the fixed parameter from 10^256-1 to
u_333, the exact Pell numerator in Section 0. All parameterized lemmas
below are restated and used with this new fixed P. The time envelope is
held fixed by using a SEPARATE constant H0=10^256-1 in its negative terms;
Section 14 makes this distinction explicit. The new parameter is the
smallest positive integer satisfying c(P)<a, and yields strictly lower
raw memory and source coefficient than the source configuration. Section
14 gives an exact rational upper enclosure near that new coefficient.

CS1-WINDOW-P-MIN-E modifies CS1-SAB, public submission
d06db402-97ca-43ce-8337-715e6152eebc, evaluated at commit
316a11cc7143fd483b578ec5cf23622f861f67d9. It retains its source-aligned
backward decoding and the cyclic-window instrument in Section 6. This
configuration changes the leaf boost and length cap to a fixed fractional
share of the depth. It has a slightly larger raw leading time coefficient,
but a strictly smaller leading memory and source coefficient. The complete
construction is below. Direct sources are the public CS1-WINDOW
submission e9fc2eca-9d1c-469b-a629-a43e0f7ce928 (evaluated commit
45d9985c85813b2f3d30c62c717faba3621eb57a) for the cyclic window and the
fixed-prefix freshness proof, df3b80c1-31f0-4325-b459-848a4b6d7182
(evaluated commit 9945c6c2ea871be37d1201db0f0d80648d47c1ae) for the exact
supported time envelope E, and aeec33bc-0d38-43b1-a551-14a60353e05e
(evaluated commit 78333b72fd9c41f992654b21d7e4ea9592b22363) for the
heralded FILTER and exact tolerance model. The parameterized
algorithm and all changed bounds are proved here, not inferred from their
review verdicts.

The predecessor CS1-SAB cites CS1-BLC16L, public submission
effe7602-1685-4fd7-b6a2-b2be4d191c4d, evaluated commit
084eca871169a15a171fa1bbfe2fd30e0e9de997. Its actual submission/proof.md has
SHA256 ba0dc0a4fcfe3739bd0cf36e12649db27643adea12f18e1779c570a6651a2a3c;
submission/submission.json has SHA256
767f7c84703eb03f917abf9f676def176af2b5ebaf3bf54f87197a000699aa14.
Sections 2--8 and 10 below adapt and restate that lineage. No accepted verdict is
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
    P = u_333,
    x = max(ceil(log2(mu + 512)) + 10, ceil(mu/P)),
    s = min(mu - 1, x),
    m = min{ m >= s+1 : m(m+1)/2 - s(s-1)/2 + x(m+1) + kappa >= B },
    lam_i = kappa + 1 + x + min(i, m-s) (0 <= i <= m-1),  lam_m = 1,
    bmax_i = x + i (0 <= i <= m-s-1),  bmax_i = x + m-s+1 (m-s <= i <= m-2),
    bmax_(m-1) = kappa + 2x + 2(m-s) + 1.

So leaves have kappa+1+x qubits (LEAF BOOST: x extra qubits per leaf), lengths grow by
one bit per level up to level m-s and then stay at 2^(kappa+1+x+m-s) for the last s-1
levels below the root (LENGTH CAP).

Lemma 7.1 (fractional boost and cap). Put q=3+x and A(B)=q 2^m,
r=sqrt(2B), C=sqrt(1+2/P^2), and gamma=C-1/P. Then m<=mu,
q=O(r), x=O(r), and uniformly over every integer B>=1,

    m+x <= C r + O(1),       m+x-s <= gamma r + O(1),
    A(B) = O((r+1) 2^(gamma r)).                             (7.0)

The constants in O() depend only on the fixed integer P and are absolute
for this single configuration. The retry-factor product is less than 3.

Proof. Since s<=mu-1, m=mu is an admissible depth: its capacity is at least
mu(mu+1)/2 - s(s-1)/2 + x(mu+1)+2 >= mu(mu+1)/2 >= B.
Therefore m<=mu. Also x>=ceil(log2(mu+512))+10, q=x+3, so
m 2^(-q) <= 2^-13. Every non-root output has at least 2^q rows. The
freshness and collision lemma gives non-root failure <2^-q when a whole
fresh pair is averaged, while the root has failure <=1/4 for every pair.
The retry product is at most (4/3) exp(2m2^(-q))<3, with independent whole
attempts as in Section 11. It is not a pointwise high-table bound.

Since P is a fixed positive integer, eventually ceil(mu/P) exceeds
ceil(log2(mu+512))+10, and is <=mu-1. For all such B, x=s=mu/P+O(1)=r/P+O(1).
The capacity inequality holds whenever m>=s+1 and

    m >= ceil(sqrt(2B+s^2+(x+1/2)^2)-x-1/2).

Hence the minimal m satisfies

    m+x <= max(s+1+x, sqrt(2B+s^2+(x+1/2)^2)+O(1)).

Here s+1+x=2r/P+O(1) is below C r+O(1), while the square root is
C r+O(1), because x=s=r/P+O(1). Thus m+x<=C r+O(1) and, since s=x,
m+x-s=m<=gamma r+O(1). The same inequalities hold for the finitely many
smaller B after enlarging the constants. Since q=O(r+1), (7.0) follows.
The finite-prefix constant may be enormous, but it is independent of N,s,
and all outcomes.

The capacity identities in the schedule remain exact:

    sum_i bmax_i=m(m+1)/2-s(s-1)/2+x(m+1)+kappa>=B,
    bmax_i+lam_(i+1)-2lam_i=-kappa.

The first is by summation; the second follows in each growing, capped and
root case. These identities and Lemma 6.1 are used below. QED.

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
kappa=2, x=O(sqrt n), and 2^kappa=4, with absolute
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

### 11.1 Heralded filter (used only by the fifth claim's error model)

Let D = M0^4, where M0 is the fixed integer in Section 15, and epsilon = 1 - 1/D.
Every source acquisition requested anywhere in Sections 5--11 is served by
FILTER: acquire one raw copy; if it carries a herald bit f = 1, reset its
n+1 qubits to |0> without any other operation and acquire again; otherwise
hand the register to the requesting step. In the clean problem there is no
herald and FILTER is the identity. Let Qcap* be the exact clean acquisition
bound of the branch: Qcap* = Qcap of (11.1) on the n >= 64 branch, and
Qcap* = N(n+10) on the finite branch n < 64 (whose candidate tests request at
most n+10 copies for each of the N candidates). A raw-acquisition counter
enforces the literal cutoff Qraw = D * Qcap*, on both branches: if the next raw
acquisition would exceed Qraw, stop and output zero. Qcap* still bounds the
number of well-formed copies handed to the algorithm, exactly as before; it
does not bound raw acquisitions under the heralded model, which are bounded
by Qraw instead.

Lemma 11.1. Under the heralded model with fraction epsilon = 1 - 1/D, the Qraw
cutoff is never reached before the algorithm itself stops.
Proof. On either branch, the clean algorithm never requests more than Qcap*
copies (on the main branch by the Qcap cutoff of (11.1), on the finite branch
by its explicit loop bounds). Suppose the raw cutoff is reached while the
algorithm still awaits a requested copy, so R <= Qcap* - 1 well-formed copies
have been handed over. Then Q = Qraw = D Qcap* raw copies were acquired and
B = Q - R >= D Qcap* - Qcap* + 1 are malformed. The promise gives
B <= floor(epsilon Q) = floor((1 - 1/D) D Qcap*) = D Qcap* - Qcap*, a
contradiction. QED.

Lemma 11.2. Under the heralded model, the joint law of every measurement
outcome of the algorithm and its output equals that of the clean run.
Proof. A malformed register is reset without interacting with any algorithm
register, so it is traced out; whatever the adversary does on its private
system and on malformed registers acts on systems disjoint from the
algorithm's. Each well-formed copy is, at delivery, a fresh rho_s in tensor
product with everything else, irrespective of the adversary's adaptive
decisions. By induction over requests, the sequence of handed-over copies
is distributed exactly as independent ideal copies supplied on request, and
by Lemma 11.1 the extra cutoff never changes the run. QED.

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
and fixed s, one specified CS1-WINDOW-P-MIN-E configuration recovers the entire s
with unconditional probability at least 1-2^-8 > 2/3.

## 13. Every-branch resource ledger

Use the fixed constants P,C,gamma from Section 7, and set c=sqrt(2) C,
beta=sqrt(2) gamma. Lemma 7.1 and monotonicity of gamma sqrt(B) for B<=n give

    A_star=O((sqrt(n)+1) 2^(beta sqrt(n))).

The exact acquisition cap in Section 11 has G_odd=O(n) (Section 9) and
therefore Qcap=O(n^2 2^(beta sqrt(n))) for n>=2. This includes every fresh
copy, even those in failed attempts. The loose n^20 bound stated in Section 0
allows all fixed setup and finite-prefix overheads.

Each leaf builds 2^q labels in O(n 2^q) core operations. Each level-i merge
costs O(n 2^(q+i)); at any fixed level, its input ancestry sets are disjoint
and each has consumed at least q2^(i+1) copies. Thus exactly as in the
predecessor, failed and partially completed trees included, their total
core work is at most

    O(Qcap * n(m+1)2^x/q).

Since q>=x+1 and m=O(sqrt n), this is at most
O(poly(n) 2^((m+x) upper bound))=O(n^20 2^(c sqrt(n))). More explicitly,
use the joint B-dependent Qcap estimate for m, and the fixed cap computed as
A_star for any width: Section 7 bounds x by x(n) and m by D sqrt(2n)+O(1),
so m+x<=c sqrt(n)+O(1). Source transforms, O(n^2) label extraction,
initialization, source work, gate generation and counters are at most
poly(n) Qcap, also below n^20 2^(c sqrt(n)).

The decoder uses R=A(d-1) (or corresponding width) <=A_star, O(sqrt n)
seed stages and records, and polynomial-bit arithmetic. Its total work is
poly(n) A_star and its peak record space is poly(n); Section 9 gives the
exact branch and error counts. Fixed finite setup, all loop counters,
classical computation of parameters and the finite n<64 branch have
polynomial or absolute-constant cost, absorbed in the same raw upper bound.
The absolute polynomial degree 20 is conservative for all these explicit
operations.

At a depth-first tree, each retained table has at most 2^(3+x+m-s) rows;
there are O(m) tables of O(n)-bit fields, plus polynomial scratch. Section 7
gives x+m-s<=beta sqrt(n)+O(1), so S_C=O(n^20 2^(beta sqrt(n))). The depth-first
quantum index stack has sum lam_i=O(m(x+m))=O(n); root, source and modular
arithmetic scratch add O(n). Hence S_Q=O(n). All registers have fixed bounded
widths and the literal source cap applies to every branch.

Under the Section 15 heralded model, FILTER enforces at most D Qcap* raw
acquisitions, where D=M0^4 is a fixed absolute constant. A raw acquisition
costs n+1; reading the herald and resetting a malformed (n+1)-qubit register
cost O(n) core operations. The raw counter uses O(log Qcap*+log D) bits;
the reset uses the existing source register, so S_C and S_Q retain their
bounds. Since D is fixed, all raw sample and work bounds retain the stated
O() forms. The global promise and Lemma 11.1 prevent the raw cap from
changing the output law; Lemma 11.2 gives the clean success probability.
In the clean problem the filter is the identity.

The challenge's address multiplier is O(log(S_C+S_Q+2))=O(sqrt n), so it and
the source charge (n+1)Qcap are absorbed into O(n^20 2^(c sqrt n)). Therefore
all raw claims in Section 0 hold on every branch for this same algorithm.

## 14. Exact supported envelopes and indices

The algorithmic constant is P=u=u_333; a=u/v is the exact Pell rational
of Section 0. In this section ONLY, define H0=10^256-1 to describe the
unchanged time envelope; H0 is not used in the schedule.

The identity u^2-2v^2=2 gives P^2>2v^2, hence

    c(P)^2 = 2+4/P^2 < 2+2/v^2 = a^2.

Further (u-1)^2<2v^2<u^2 (since u>2). Thus u is the smallest positive
integer P for which c(P)<a. For real P>=2, setting t=1/P gives
beta(P)=sqrt(2+4t^2)-sqrt(2)t, whose derivative in t is
4t/sqrt(2+4t^2)-sqrt(2)<0 for 0<t<=1/2. Hence beta increases with P
on this range; reducing the fixed P to u strictly improves the raw
classical-space and source coefficient among the source's admissible
integer choices c(P)<a. The time coefficient increases but remains
strictly below a, which suffices for the unchanged E(n).

Define A=u-1, B=v. They are coprime: if a common prime divides v and
u-1, reducing u^2-2v^2=2 modulo it gives 1=2, a contradiction.
Compute D as the positive residue -A^(-1) modulo B and C=(A D+1)/B.
The exact values are

    C = 4944903328659608430077683349163950503293749505518464781889829685697029717315859012146919538138315678130125588043444281557617593846694168147163829453094769841789324521139844847559047028430696412641452668987743590842724458466263346185490147158553575106014752
    D = 3496574676007140236075639064851844457760593417656713026768856872037459585846293376347831707729831813701320704433518438675585607227239648435421446982983095693410105884036746546662892456736483288942471821215534736580689364940545429989484421449570919656495015

so B C-A D=1 and b=C/D is reduced. Both integers have 256 decimal digits.
Direct integer checks, or substitution of these displayed values, give
D<u^2/2 and C^2<2D^2. The determinant implies

    b = (u-1)/v + 1/(vD).

The Pell lower approximant 2v/u is strictly below sqrt(2), since
2v^2<u^2. Thus

    beta = c(P)-sqrt(2)/u < a-2v/u^2
         = (u-1)/v + 2/(v u^2)
         < (u-1)/v + 1/(vD) = b < sqrt(2).         (14.1)

Every gap is strict and independent of N. In particular beta<b, so the
fixed polynomial in each raw memory/sample bound is absorbed by the
strict exponential gap. These are exact rational/integer certificates;
no floating-point approximation supplies an inequality.

The source's algorithmic P_old=10^256-1 is larger than u (direct integer
comparison); the monotonicity above establishes beta(P)<beta(P_old).
For comparison with its declared b_old=l/w, let w be the positive inverse
of u modulo v and l=(uw-1)/v. Direct comparison gives Cw<lD, so b<b_old.
For comparison with the separately explored fixed-P SHARP enclosure
p_star/d_star with d_star=7*10^255-5201 and
p_star=floor(sqrt(2*d_star^2)), direct comparison also gives
C*d_star<p_star*D. Thus the new supported memory/sample envelopes are
strictly smaller than that enclosure as well.
Define for n>=2, L=log2 n and

    E(n)=2^[a sqrt(n) - H0 sqrt(n) sum_(j=1)^27 L^(-1/(10^256-j))
            - (10^58-1) sqrt(n) L^(-1/(10^256-28))].

This is the identical supported envelope of public submission df3b80c1,
which is a material source for this representation. Each of the 28 negative
summands is o(sqrt(n)); their finite sum is o(sqrt(n)). Since a-c>0,
for every fixed k, n^k 2^(c sqrt(n))=O(E(n)). Since b-beta>0, for every
fixed k, n^k 2^(beta sqrt(n))=O(2^(b sqrt(n))). These are true asymptotic
statements with enormous finite thresholds, not practical speed claims.

Declare exactly E(n), E_b(n), n, and E_b(n) (E_b: envelopes.md) for T, S_C,
S_Q and Q. The common fixed context is that of rules.md. All three
exponential envelopes have growth index 1/2 because their leading terms
are positive constant times sqrt(n); n has index 0. Thus the four indices
are [1/2,1/2,0,1/2], with only time numerically scored. The explicit
structured objects spell out every rational term and match these expressions.

## 15. Source error tolerance

The tolerance is epsilon(n) = 1 - 1/m^4 under the identical heralded
malformed-copy model below. This snapshot uses x = 10^64 - 82 and an explicit factorization of x^2+1:

    x = 9999999999999999999999999999999999999999999999999999999999999918
    t_1 = 3703451866653595422444485034231095502509127229476212406042517153
    t_2 = 5400367203387420701081323716636384438164417013598401128084488865
    t_3 = 5

with t_1 * ... * t_3 = x^2 + 1 exactly (direct integer multiplication;
the factors need not be prime). Put m = x in Section 11.1, so D = m^4 = x^4.
Each of x, x-1, x+1 and every t_i has at most 64 decimal digits. The supported
expression is exactly

    9999999999999999999999999999999999999999999999999999999999999917*9999999999999999999999999999999999999999999999999999999999999919*3703451866653595422444485034231095502509127229476212406042517153*5400367203387420701081323716636384438164417013598401128084488865*5/9999999999999999999999999999999999999999999999999999999999999918^4

which equals (x-1)(x+1)(x^2+1)/x^4 = (x^4-1)/x^4 = 1-1/x^4 = 1-1/D. Its
normalized numerator and denominator have at most 256 digits; only
products, division and the integer power 4 are used. The filter and literal
raw-acquisition cap are unchanged apart from this fixed D, whose finite
overhead is charged and leaves the asymptotic envelopes unchanged. Since
x > 2*70710678118654752440084436210484^2 (the previous fixed value, exact
integer comparison), the fraction is strictly larger in the same model.
No ability to correct unheralded errors is claimed.

Theorem 15.1. Under the heralded model with this epsilon, for every N >= 2
and every s, the CS1-WINDOW-P-MIN-E configuration with FILTER (Section 11.1) outputs s
with probability at least 1 - 2^-8 > 2/3, and on every branch satisfies the
four resource bounds of Section 13, hence the declared
envelopes of Section 14.
Proof. Lemma 11.2 makes every outcome law identical to the clean run, so
Section 12 gives success >= 1 - 2^-8. Lemma 11.1 and Section 13 give the
resource bounds on every branch; the envelopes follow by Section 14 because
D is an absolute constant. With no malformed copies the algorithm is the
clean algorithm. QED.


The exact error-model text shared with the fifth structured claim is:

Heralded malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires on an execution branch, and epsilon(n) the tolerated malformed fraction. Each acquired copy consists of an (n+1)-qubit register of the ideal copy's shape together with one classical herald bit f delivered with it. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed. A well-formed copy has f = 0 and its register is a fresh copy of rho_s, in tensor product with every other system (earlier copies, the adversary's system and the algorithm's registers). A malformed copy has f = 1 and its register is in an arbitrary state chosen by the adversary, possibly entangled with the adversary's private system and with other malformed copies. On every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. The herald is always correct, so malformation is detectable (an erasure-type error); its timing, its number within the promise and the malformed register contents are adversarial. In the clean problem no herald is supplied and every copy is well-formed. No source control, purification access or preparation inverse is supplied.
