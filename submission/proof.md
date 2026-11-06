# CW1-CL: three-qubit leaves with strided backward recovery

## 0. Joint theorem and notation

For every integer N>=2 and s in Z/NZ, put n=ceil(log2 N) and L=log2 n.
The single algorithm below recovers the complete secret from independent
ideal coset copies with unconditional probability at least 1-2^-8>2/3.
On EVERY execution branch, including all discarded copies, failed trees,
retries, wrong labels, and cap aborts, its joint bounds are

    T=O(n^(7/2) L 2^((3/2)sqrt n)),
    S_C=O(n^2 2^sqrt n) classical bits,
    S_Q=O(n) qubits,
    Q=O(n 2^((3/2)sqrt n)).

All outside constants are absolute and independent of N, s and outcomes.
The asymptotic representatives use n>=2; the finite branch covers n=1.
Their exact growth indices are [1/2,1/2,0,1/2]. Source tolerance is zero
with the exact model in Section 15. These are one algorithm's simultaneous
guarantees, not resource bounds from different parameter choices.

Write d=floor(log2 N), N=2^a2 M with M odd, s1=s mod M, and
s=s1+M s2 modulo N with 0<=s2<2^a2. Let omega=exp(2 pi i/N).
A label is a known integer; W is a full signed root frequency.
All logarithms are base two except ln. Ceilings and floors of integer
logarithms and square roots are computed by integer arithmetic.

## 1. Direct sources and actual use

The width-capped long-ramp supplier is CW1S, public submission
32303149-73e3-4acd-af1f-4a6052d73869, evaluated commit
174d649db7c03b0619a486e9ce515c7b95e8ff2d. Its exact proof has SHA-256
f680e71657013d62c319a71e48ed20c2f0670072b9f494e156101fca0501df84.
Its complete merge, tree profile, label representation and low-bit
induction are reproduced in Sections 6--8. Its finite-pool support
argument and stride score bound are used in Section 9.

CW1S credits the capped profile to CW1,
cfe82a87-0d65-454e-b1df-4789dc95aab4, and the pool/distance/stride
argument to HS2, 8b85be12-4b9c-40e6-a62f-d2d232d62402. It credits
CS1, b56c7ceb-de59-42da-9e3b-6ee96e4e4145, identical to
f1481815-9577-4990-abe3-7b79fa5d9284, for linear merge, source transforms,
free-frequency scoring and label arguments. These credits remain in force.

Terminal localization and circular backward recovery use CS1-BACKWARD,
70936e29-d357-4713-b84f-47acebe365fd. Direct exact collective label tests
use 844c0fd2-9b1c-4e84-a37c-f402e109985f. The local complete proof
grover_backward.md, SHA-256
feddaf5b5ba6610b0d6491e104b509cf70d668f4ceed4d23ec76c36a4d042431,
supplied the exact collective extractor, one-bit fallback, and all-N
backward composition reproduced here. The local research proof
stride_decoder_transfer.md, SHA-256
abe770f323abf2b161678df4ee06d6dd39e09f7bfe71ce643863b52b3ef0eb3f,
supplied the strided terminal seed, exact multiple lifts, and the
conservative pointer costs. All required proofs are reproduced below.

Historical sources are Kuperberg arXiv:1112.3333v1, Algorithm 4.1,
Proposition 4.2 and Section 4.6, and Kitaev quant-ph/9511026. CW1S
also credits COL3 on this challenge for the earlier label-test and
source-transform composition. No review verdict is a proof premise.
Physical source multiplication and controlled shifts are retained.

This complete proof directly adapts the approved local CW1-BS proof,
cw1_backward_stride.md, SHA-256
99556cd9f48ddb22fa1cb8f56530548e6d6a9058b08af0424ac6d9df65a22032.
The three-qubit leaf schedule and exact zero-removal startup are from
cw1_variable_padding.md, read at SHA-256
22ff465cf2d8ab53749c353c137aa5c8d7ed609e13999763dff182d0e6bba160.
Its full integer capacity, success and cost arguments are reproduced here.
The fixed aligned field layout and field/gate generator are from
cw1_backward_resources.md, SHA-256
69021f8358d763e4ffd3efed78f197222531f492072cd8ddc2e742cc8dcbba9e,
and their complete integration in cw1_backward_fast.md, SHA-256
44f424894a6b9e41871ac8e7f0672cf23ec15660ca75b32fd2d21d6bd05565e9.
Only that table implementation is used from the latter proof. Source
processing here is the physical transform and ordinary collective
extractor reproduced in Sections 3--5.

## 2. Counted implementation

A logical operation is one NOT/CNOT/Toffoli/H/S/S-dagger gate, a one-qubit
computational measurement or reset, a Boolean operation on at most three
classical bits, or a classical bit read/write. A v-bit add, comparison,
copy, increment, or ripple subtraction uses O(v) such operations.
Reversible scratch is cleared by compute/copy/uncompute or by the
explicit inverse of a permutation. Toffoli has an exact constant-size
Clifford+T implementation. No approximate quantum rotation is used.

All loop control, integer arithmetic, parameter computation, initialization,
reset, and circuit generation are counted. A source acquisition costs n+1.
Every indexed action also pays ceil(log2(S_C+S_Q+2)) bit operations.
Logical circuit counts in Sections 3--10 exclude no required operation:
Section 13 adds explicit pointer/generation work and the indexed charge.
It distinguishes polynomial-address source scratch from exponential
classical tree tables, and gives a conservative every-branch total.
Gates are generated in streaming order; no exponential circuit is stored.

Only fresh mixed source copies are available. The algorithm uses no
source purification, controlled source preparation, inverse source,
QRAM, free table lookup, arbitrary-N QFT, or hidden-shift oracle.

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
which EXTRACT recovers.

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

## 5. Exact collective label extraction EXTRACT

Input: a data register holding chi_k beside arbitrary spectators. Set

    J_e=n+4, h_e=ceil(log2(2^16 Qcap(n+5))), F(h_e)=2^21 h_e.

Here Qcap is the exact source cap of Section 11. Each call executes the
fixed procedure RUN(F(h_e)) once, outputs its integer label, and resets
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
F = F(h_e) this is 2 exp(-h_e). So RUN(F(h_e)) returns a value other than k with
probability at most 4 (J_e + 1) e^(-h_e) = 4 (n+5) e^(-h_e), uniformly in k.
A call uses 2F(h_e) rounds, each with O(n) quantum core steps. Incrementing
all outcome counters costs O(n F(h_e) log(F(h_e)+2)) bit operations even without
amortization. There are O(n) counters, each of O(log(F(h_e)+2)) bits. Each of
the 64 direction scores per level is computed by integer arithmetic on
O(log(F(h_e)+2)) bits; the fixed table denominator is common to all scores.
Exact dyadic unwrapping and final multiplication and rounding cost O(n^2).
Therefore the total core work per call is

    O(n h_e log(h_e+2)+n^2)=O(n^2),

because Section 13 proves h_e=O(sqrt n). Thus
n h_e log(h_e+2)=O(n^(3/2)log n)=O(n^2).
Quantum scratch is O(n), and classical scratch is O(n log n). All work is bounded on every
branch. To make the collective map total on the data encoding, first
compute [u<N] and apply the modular subtraction only on that subspace;
the data validity is preserved, so its flag can be cleared. This changes
neither the O(n) cost per round nor the action on the source.

For each call, conditional on its latent label and all earlier history,
its error probability is at most 4(n+5)e^(-h_e). Thus over at most Qcap calls,

    Pr[any wrong label] <= 4(n+5)Qcap e^(-h_e) <= 2^-14.

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

For b=0, omit the empty residue registers and set e=0. Then order[y]=y,
all pairs are in the sole fiber, and rank(x,y)=2^lam*x+y. Thus rank,
block measurement, and inverse maps are explicit at this boundary too.

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

Cost. Write E=2^lam and Eout=2^lam'. A merge makes eight lookup passes
of E rows and one of Eout rows, each with O(lam+b) bit fields. Classically
it makes O(E lam) comparisons of (b+lam)-bit keys, O(E) binary searches
of O(lam) steps on b-bit keys, and O(Eout) additions of O(n)-bit high
parts. Since lam,b=O(sqrt n) by Section 7, this is O(n(E+Eout)) logical
operations. Quantum scratch is O(sqrt n) beyond the two input indices.
Classical scratch for all rank, residue and inverse-block tables is
O((E+Eout)sqrt n) bits. The output table has Eout fields of w' bits and
p+b bits for its common residue. Section 13 counts pointer generation
and all indexed charges for these operations.

## 7. Three-qubit leaves and exact startup merges

A TREE_D call has independent retained positive phase qubits with known
uniform labels in [0,2^D), D>=2. Put B=D-1<=n. For n>=64 compute

    w=ceil(sqrt n), R0=max(0,n-w(w-1)/2),
    mu=w+1+ceil(R0/(w+1)), kappa=ceil(log2 mu)+1,
    a=kappa-2, loss=a(a-1)/2.

Define

    Snew(m)=w(w-1)/2+(m-1-w)(w+1)+kappa+2w+1-loss,
    m=min{j>=w+1:Snew(j)>=B}.

Equivalently, with base=w(w-1)/2+kappa+2w+1-loss, compute
m=w+1+max(0,ceil((B-base)/(w+1))). All computations are exact integer
operations. The table exponents and removal capacities are

    lam_i=3+2i                         for 0<=i<a,
    lam_i=kappa+1+min(i,w)              for a<=i<m,
    lam_m=1;

    bmax_i=0                           for 0<=i<a,
    bmax_i=i                           for a<=i<w,
    bmax_i=w+1                         for w<=i<=m-2,
    bmax_(m-1)=kappa+2w+1.

Allocate actual b_i greedily from i=m-1 down to zero, taking
min(bmax_i,B-already_allocated). Put p_0=0 and p_(i+1)=p_i+b_i.
No zero-removal level is deleted: it executes an actual bounded merge.

### 7.1 Integer capacity and depth

The global depth calculation is independent of the changed startup.
Since sqrt n<=w<sqrt n+1 and w^2>=n,
R0<=n/2+w/2 when positive, so R0/(w+1)<=sqrt n/2+1/2. Therefore

    w+1<=mu<(3/2)sqrt n+7/2<=2sqrt n<=2w,
    2^kappa>=2mu, 2^kappa<=4mu.                       (7.1)

Let t=ceil(log2 w). Since w>=8, t>=3. From mu<=2w,
a=kappa-2<=t<w, while mu>=w+1>=9 gives a>0. For every integer
t>=3, t(t-1)<=2^t: it holds at three, and the next ratio
(t+1)/(t-1) is at most two. Since 2^(t-1)<w,

    loss<=t(t-1)/2<=2^(t-1)<w.                        (7.2)

At mu, the capacity before subtracting loss is
w(w-1)/2+ceil(R0/(w+1))(w+1)+kappa+2w+1, which is at least
n+kappa+2w+1 by the definition of R0. Thus Snew(mu)>n.
The per-tree minimum exists and satisfies w+1<=m<=mu. Summing the
stated capacities gives Snew(m)>=B exactly. Greedy allocation therefore
ends with sum_i b_i=B, p_m=B, and all p_i in [0,B].

### 7.2 Startup success and later failure bounds

For every i<a, including i=a-1, lam_(i+1)=lam_i+2. At the boundary,
lam_(a-1)=2kappa-3 and lam_a=2kappa-1. Since lam_i>=3,
lam_(i+1)<=2lam_i. Also b_i=0. The sole residue fiber contains all
2^(2lam_i) input pairs. Its exact rank is 2^lam_i*x+y. The output
block length 2^(lam_i+2) divides the fiber size exactly. Every possible
block is complete, so the merge has failure probability ZERO for every
input table and phase. The index clearing and output table in Section 6
then give the exact selected phase vector. No label event or rejection
cost is omitted by this startup.

For a<=i<w, b_i+lam_(i+1)-2lam_i<=i-(kappa+i)=-kappa.
For w<=i<=m-2, it is at most (w+1)-(kappa+1+w)=-kappa.
At the root it is at most (kappa+2w+1)+1-2(kappa+1+w)=-kappa.
Thus every later merge has conditional failure at most 2^-kappa by
Lemma 6.1. This bound is pointwise in the input tables. All output
exponents are at most twice their input exponent. Startup output
lengths are four times input lengths; later lengths grow by at most
a factor two, stay fixed, or shrink to two at the root.

### 7.3 Leaves, labels, and evaluation

LEAF uses exactly THREE retained phase qubits as its index. Its eight
labels are built from lab[0]=0 and
lab[x+2^j]=lab[x]+k_j for x<2^j, j=0,1,2. This is the exact tensor
product phase vector, collimated to p_0=0.

A level-i vector has 3*2^i nominal retained ancestors. Each table label
is a nonnegative subset sum of these labels, all below 2^(B+1), so
it is less than 2^(B+3+i). Store the common residue modulo 2^p_i and
high parts in fixed width

    width_i=B+3+i-p_i.                               (7.3)

This is positive and O(n). It also holds on numerical-label error
branches, because acceptance/reduction always puts stored leaf labels
in the declared interval. No incidence vectors are stored.

VEC(0) returns LEAF. To obtain VEC(i), i>0, build fresh VEC(i-1)
children X1,X2 from disjoint source sets and run
MERGE(X1,X2;p_(i-1),b_(i-1),lam_i). On failure discard both children
and rebuild both. On success return the output. Startup merges cannot
fail; the same rule remains total at all levels.

TREE_D returns VEC(m), whose two labels are congruent modulo 2^B.
Its ideal state, up to global phase, is
(|0>+exp(2 pi i 2^B W th)|1>)/sqrt2, with

    nq_D=3*2^m,
    W=(lab[1]-lab[0])/2^B=hi[1]-hi[0], |W|<2nq_D.     (7.4)

Every lam_i is at most kappa+1+min(i,w): on startup this follows
from i<=a, and afterwards it is equality before the root. Hence
lam_max=kappa+1+w<=2sqrt n for n>=64. Indeed
log2 mu<=log2(2sqrt n)<=sqrt n/2 from n>=64, so
kappa<=sqrt n/2+2 and w<sqrt n+1 give that bound. Also
b_i<=kappa+2w+1<=4sqrt n.

Depth-first evaluation keeps at most m finished sibling indices plus
one active index, including two inputs at the same level. They use
at most (m+1)lam_max<=(2sqrt n+1)2sqrt n<=8n qubits. Merge scratch
is counted separately. Finally 2^m<=2^mu<12*2^((3/2)sqrt n).

## 8. Top-bit independence

Write each leaf label as k_j = low_j + 2^B tau_j, with 0 <= low_j < 2^B and
tau_j in {0,1}. Since k_j is uniform on [0, 2^(B+1)), low_j and tau_j are
independent and tau_j is a fair bit. Let Gt be the sigma-field generated by:
- all low_j of the tree's leaves, including those of discarded attempts;
- all measurement outcomes (e, bl) of its merges;
- all tree-construction decisions of the controller (merge parameters, FAIL
  and retry decisions, leaf acceptance tests and which copies are used).
Gt is defined in the ideal latent-label process. It excludes EXTRACT's
internal test records, root X/Y basis coins and root outcomes. The ideal
process replaces every extractor output by its latent label and averages
out its private records. Accepted leaf top bits are not conditioned on
those records or on successful extraction. Waiting counts and rejected
latent labels can be included: the accepted label remains independently
uniform given those data.

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
copies, whose labels enter the same factorization. Startup block kernels
are independent even of low labels. Almost-sure termination follows in
Section 11; the factorization therefore holds for the finite returned
tree. QED.

Let x0 and x1 be the leaf-incidence vectors of the two root entries. Distinct
indices at a node correspond to distinct incidence vectors: this holds at
leaves, is preserved by concatenating disjoint coordinate sets, and
re-indexing is a bijection. This includes startup: a block can make a
leaf contribution common to both entries, but cannot merge two distinct
binary incidence vectors. Thus hd=|x0 xor x1|>=1. From (7.4),

    W = cst + sum_(j in Sp) tau_j - sum_(j in Sm) tau_j,                        (8.1)

where cst = (sum_j low_j (x1_j - x0_j)) / 2^B is a Gt-measurable integer, and Sp and
Sm are disjoint Gt-measurable sets with |Sp| + |Sm| = hd. A fair bit tau has
E exp(2 pi i phi tau) = e^(i pi phi) cos(pi phi). Hence, for every real phi,

    | E[ exp(2 pi i phi W) | Gt ] | = |cos(pi phi)|^hd <= |cos(pi phi)|,       (8.2)

and, with phi = 1/2, Pr[W odd | Gt] = 1/2.                                     (8.3)

## 9. Terminal seed and strided backward recovery of the odd part

If M=1, put s1=0 and F=0 and skip this section. Otherwise M>=3.
Every odd tree uses D=d=floor(log2 N), B=d-1>=n-2, and q=nq_d from
Section 7. In particular, B is large even when M is small. Only the
later 2-adic part uses small active widths. Set theta=s1/M.

For ANY nonnegative physical scale j, compute by extended gcd and CRT

    alpha_j=1 mod2^a2,
    alpha_j=2^j (2^(d-1-a2))^(-1) mod M.

This is a unit modulo N. Acquire a fresh source copy, apply Mult_alpha_j,
extract its transformed latent label k, accept only k<2^d, and apply X
to its control. The ideal accepted labels are independent uniform on
[0,2^d), with acceptance probability 2^d/N>1/2. A TREE_d root has phase

    2^(d-1) W alpha_j s/N = W 2^j theta mod1.

Thus the output is (|0>+exp(2 pi i W 2^j theta)|1>)/sqrt 2, with |W|<2q.
The CRT identity is valid also at terminal seed scales above n. All
scales used below are O(n), and every alpha_j is computed with charged
polynomial bit work. No root is filtered by its full label or support.

At any scale, measure each root in an independent fair X/Y basis,
recording (W_i,beta_i,Z_i), where Z_i is +1 or -1. For a candidate zeta
at that scale, its exact score summand has conditional expectation

    E[Z_i cs_beta_i(W_i zeta) | W_i,past]
       =(1/2)cos(2 pi W_i(x-zeta)),

where x is the true phase at that scale. The computed summand replaces
cs by the Section 4 table and has error less than 1/625. All candidate
sets below are fixed before the fresh stage roots are measured. Scores
are streamed with the least index as a deterministic tie rule.

### 9.1 Exact parameter rule and fallback

The global tree parameters mu,kappa are from Section 7. Define the
uniform expected source bound per root and the following exact integers:

    C=18*2^mu, ell=ceil(log2 q)=m+2, U=n+ell+40,
    A=2^40(C+1)U^3, gpool=ceil(log2(2A)),
    hdist=floor(B/(8gpool)),
    H=ceil(log2 M), nu=ceil(log2(n+ell+4)),
    Kseed=8192(ell+nu+30), Kone=512(nu+30).

If n<256 or hdist<16, run the complete one-bit decoder of Section 9.2,
with exact root count

    F=(ell+4)Kseed+H Kone.                             (9.1)

Otherwise set

    Delta=floor(floor(log2 hdist)/2)-1,
    Kblock=8192(Delta+nu+30),
    Sseed=ceil((ell+3)/Delta), Sback=ceil(H/Delta),
    F=Sseed Kseed+Sback Kblock.                       (9.2)

Use Sections 9.3--9.5. In that case Delta>=1 and
2^(Delta+3)<=4sqrt(hdist). The exact source cap, set before extraction,
is Qcap=1024[C(F+2n)+2n], as in Section 11. The number F and physical
scale sequence depend only on N and the chosen branch, never on a root
measurement, score, candidate center, or preceding success.

Both branches are explicit finite arithmetic procedures. Section 13
proves that the fallback occurs at only finitely many bit lengths,
uniformly over N and s, and that the single parameter rule has F=O(n).
There is no assumption that hdist is large in every execution.

### 9.2 Complete one-bit fallback

#### 9.2.1 Two-candidate lemma

Write ||x|| for circular distance to 0. Suppose a known dyadic center
z in [0,1) satisfies

    ||2x - z|| <= e,             e <= 1/(64q).

The inverse images of z under doubling are

    u_0 = z/2,                  u_1 = (z+1)/2.

Exactly one of them, denoted u_*, lies within e/2 of x; the other is 1/2
away from u_*. This is a statement on the circle, so it includes z=0,
wraparound, and x arbitrarily close to any binary boundary.

Produce k fresh roots with phase W_i x. For each independently choose
beta_i uniformly from {0,1}, measure X or Y respectively, and record
Z_i in {+1,-1}. Use the Section 4 trigonometric table:

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
as decoding proceeds backward. It does not degrade by q per step.

#### 9.2.2 One-bit terminal seed

Apply the explicit localization algorithm below to the phase

    phi = 2^H theta mod 1

for local stages u = 0,1,...,ell+3. Local stage u obtains roots at physical
scale H+u, using the same TREE_d and Kseed roots. At every local stage, measure its Kseed roots in independent fair X/Y
bases and record (W_i,beta_i,Z_i). On its dyadic candidate grid compute
score(c)=sum_i Z_i tab_beta_i(((2^u W_i c) mod2^P_u)/2^P_u), with the
Section 4 table. Stream candidates and return the least maximizing one.
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
at least cos(pi/128)/2. Martingale concentration at deviation Kseed/64,
table error Kseed/625, and the at most 2^(ell+9) near/far events imply
failure at most 2^-20/(n+ell+4) per stage. The strict score margin can be checked
without floating point using pi > 3, pi < 22/7, and the alternating
cosine bounds:

    [9/128 - (22/7)^2/(2*128^2)
       - (22/7)^4/(24*8^4)]/2 - 2/64 - 2/625
      = 4372721/73758720000 > 0.

At the last seed stage, obtain z_H satisfying, except on seed failure,

    ||phi-z_H|| <= e_H = 2^-(ell+6) <= 1/(64q).

There are ell+4 seed stages. In the concentration bound use the present
nu=ceil(log2(n+ell+4)). The failure per seed stage is at most
2^-20/(n+ell+4). Thus the total seed failure is at most 2^-20, without a bound on the number of profile levels. No bound
ell+4<=n is needed.

The seed's exact denominator is 2^(2ell+11). The seed is an ordinary
localization of a real phase on the circle. It does NOT presume phi is a
dyadic rational or try to round phi to a secretly known rational grid.

#### 9.2.3 One-bit backward steps

For j = H-1,H-2,...,0:

1. Form the exact dyadic candidates z_(j+1)/2 and (z_(j+1)+1)/2.
2. Acquire Kone fresh TREE_d roots at physical scale j.
3. Apply the two-candidate scoring rule of Section 9.2.1 and set z_j to its
   deterministic maximizer.

If all preceding choices were correct, the true phase x_j = 2^j theta
has distance at most e_H/2^(H-j) from z_j. Every such incoming radius is
small enough for the lemma. Since exp(-Kone/512) <= 2^-30/n and H <= n,
the conditional error union bound is at most 2^-30.

This union bound is over first-error events, not conditioning the complete
run on success. Previous branch decisions can be adaptive; every newly
called source uses fresh independent mixed copies.

#### 9.2.4 Exact fallback rounding

The output center z_0 has denominator 2^(H+2ell+11), and

    ||theta-z_0|| <= 2^-(H+ell+6) <= 1/(64 q M) < 1/(2M).

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
Section 4 fixed trigonometric table, already budgeted in both lemmas.

The fallback uses exactly the F in (9.1). All of its phases, products,
centers and score records have O(n) bits. It is total on bad events and
uses fixed stage lengths. There are no hidden retries in this decoder.

### 9.3 A finite low-bit pool and the support event

Assume the active stride branch. The analysis pool contains the capped run. Since Delta>=1,
Sseed<=ell+3 and Sback<=n. Also Kseed,Kblock<=2^15 U. Consequently

    F<=2^15 U^2,
    Qcap<=2^27(C+1)U^2<=A.

This bound is prior to any asymptotic simplification. There is no circular
choice of A from an unproved root budget.

Extend the accepted odd-leaf sequence to an infinite independent uniform
sequence. This is possible because source transforms depend only on the
fixed physical scale sequence, never on decoder centers. Given the
waiting counts and rejected values, the next accepted label still has
the same uniform law. Independent fresh arrays per fixed root call give
an equivalent construction; concatenating their used prefixes gives this
pool. Adaptive failures only determine how many new coordinates are used.

Let E be the low-bit event that no nonempty signed sum on fewer than hdist distinct
coordinates among the first A low labels vanishes modulo 2^B. A fixed
nonempty signed sum is uniform modulo 2^B: expose all but one coordinate,
whose coefficient is a unit. Thus

    Pr[E fails] <= 2^-B sum_(t=1)^(hdist-1) binom(A,t)2^t
                <= hdist(2A)^hdist 2^-B
                <= 2^(-3B/4).

For the last inequality, hdist gpool<=B/8 and log2 hdist<=log2 B<=B/8 for B>=64.
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

Let Fitodd say that the complete ideal odd schedule fits Qcap.
This event is Llow-measurable. On E and
Fitodd, every root's nonzero support has at least hdist coordinates: its
full signed label is divisible by 2^B, so a smaller support would give
a forbidden signed low relation. In particular, for every real x,

    |E[exp(2 pi i x W) | Llow]| <= |cos(pi x)|^hdist.       (9.3)

Earlier decoder outcomes only reveal top bits of disjoint earlier root
sets. Hence (9.3) remains valid with those outcomes exposed. This is the
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
Thus the candidate set has at most 2^(ell+8)<=512q elements, and a
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

    |cos(pi x)|^hdist <= exp(-2 hdist x^2)<=exp(-1/8).

By (9.3), a far candidate's expected exact score is at most
exp(-1/8)/2<=4/9. For each fixed candidate, martingale concentration
bounds a one-sided deviation Kseed/64 by exp(-Kseed/8192). The score
comparison is strict, since

    499/1000-4/9 > 2/64+2/625.

There are at most 2^(ell+9) near/far events. Their union probability
is at most 2^-20/(n+ell+4), by the exact Kseed and nu above. Hence the
output center has error less than 2^-(j+Delta+3), which is exactly the
next incoming radius. This argument is conditional on any Llow in
E and Fitodd and on earlier stages. It includes adaptive centers.

At the final stage obtain z_H with

    ||2^H theta-z_H|| <= e=2^-(Sseed Delta+3)
                         <=2^-(ell+6)<=1/(64q).

The seed's largest local physical scale is (Sseed-1)Delta<ell+3.
Its final denominator exponent is (Sseed-1)Delta+ell+8<2ell+11.
There is no hidden physical scale or precision increase.

### 9.5 Exact backward blocks

Suppose a dyadic z approximates 2^j theta with circular error e_j<=e.
Take r=min(Delta,j), set j'=j-r, and form all 2^r exact lifts

    u_a=(z+a)/2^r, 0<=a<2^r.

Exactly one lift ustar has circular distance at most e_j/2^r from
x=2^j' theta. Acquire Kblock fresh roots at physical scale j'. Score
these lifts with sum_i Z_i tab_beta_i(W_i u_a mod1) and choose the
least maximizing a. Repeat until j=0. This uses exactly Sback blocks.
The physical scale sequence and root counts are fixed by N, not scores.

For the correct lift delta=x-ustar, every |W delta|<1/64, because
|W|<2q, e_j<=1/(64q), and r>=1. Its expected exact per-root score is
at least cos(pi/32)/2>49/100. For any other lift, the circular distance
from x is at least

    (1-e_j)/2^r >= 1/2^(r+1) >= 1/sqrt hdist.

The last bound follows from 2^Delta<=sqrt hdist/2. Its distance is also at
most 1/2. Thus (9.3) bounds its expected score by exp(-1/8)/2<=4/9.
This looser exponent is sufficient and avoids a dependence on r.

The same concentration calculation has at most 2^(Delta+1) events.
Kblock gives error at most 2^-20/(n+ell+4) per block. The margin is
strict since

    49/100-4/9 > 2/64+2/625.

On a correct choice, the new error is exactly bounded by e_j/2^r.
There is no rounding or loss of denominator bits in a lift. After all
blocks, ||theta-z_0||<=e/2^H<1/(2M). Return

    floor(M z_0+1/2) mod M.

This returns s mod M, including wraparound and binary-boundary cases.

There are at most ell+3+n<n+ell+4 seed stages and backward blocks.
A union bound over first incorrect stages gives total decoder failure
at most 2^-20 conditional on every Llow in E and Fitodd. Integrating
this bound gives odd recovery error at most 2^-20+2^(-3B/4) apart
from source-cap or extraction errors. Section 12 adds those errors
without conditioning on successful extraction or on a favorable cap.

## 10. Recovery of the 2-adic part

If a2=0, set s2=0 and skip this section. Otherwise write
s-s1=M s2 modulo N, with 0<=s2<2^a2. At bit g=0,...,a2-1 let
s2low be the already chosen low g bits and put

    sh_g=s1+M s2low mod N, wd=a2-g,
    rem=(s2-s2low)/2^g mod2^wd.

When the earlier choices are correct, s-sh_g=M2^g rem modulo N.
Acquire a fresh copy, apply the physical Shift_sh_g, run EXTRACT,
and apply X to the control. Reduce the returned label to kk=k mod2^wd.
The ideal kk is uniform on [0,2^wd), since 2^wd divides N. With correct
earlier choices its phase is exp(2 pi i kk rem/2^wd).

If wd=1, discard kk=0. For kk=1, measure X; the result is + exactly
when rem is even. If wd>=2, build TREE_wd from such leaves. Discard
an even W; for odd W, the root phase is exp(pi i W rem)=(-1)^rem,
so an X measurement determines the next bit exactly.

Each ideal attempt has acceptance probability exactly 1/2 by (8.3),
including after an incorrect odd answer or earlier bit. On such a wrong
history the reduced labels need not describe the phases. Nevertheless,
all basis magnitudes remain equal. Every merge selects by basis
membership and its outcome probabilities depend only on the low label
data. The unused top-bit argument and parity law still apply. The
phase identity is needed for correctness only on correct earlier choices.
No source or cost bound assumes that the earlier choices were correct.

Allow exactly K2=ceil(log2 n)+30 attempts per bit, stopping at the first
odd W or width-one label one. If none occurs, abort and output zero.
The probability of any such failure is at most n2^-K2<=2^-30.
Each truncated search uses at most two roots or direct originals in
expectation. Upon success set the bit and continue. Finally return
(s1+M s2) mod N.

## 11. Complete algorithm, source cap, and termination

For n<64, test cand=0,...,N-1 in order with at most n+10 fresh copies
per candidate. Apply Shift_cand and measure the control in X, rejecting
at the first minus result. Output the first candidate with all plus
results, or zero if none. The true candidate always passes. For every
wrong candidate the two data states are orthogonal, so each test is fair.
A union bound gives error at most N2^(-n-10)<=2^-10. The source bound
is N(n+10), and each charged test has polynomial work and storage.
This finite set of inputs is absorbed into absolute resource constants.

For n>=64 compute a2,M,d and the exact tree profile of Section 7. Set

    C=18*2^mu.

If M=1 set s1=0 and F=0. Otherwise compute the parameters in Section 9.1
and its specified F, including the fallback predicate. Set

    Qstar=C(F+2n)+2n,
    Qcap=1024 Qstar.                                  (11.1)

These are exact integers of polynomial bit length. Compute h_e for
EXTRACT from this fixed Qcap. Initialize an acquisition counter to zero.
Before any acquisition that would exceed Qcap, stop, release registers,
and output zero. Count all acquisitions, including rejected labels,
failed merges, discarded roots, and partial trees. First run the chosen
odd decoder, then Section 10 with its K2 cap, and output the full secret.
No tree is exempt from the source counter.

Expected ideal source bound. A retained odd leaf qubit needs fewer
than two originals in expectation; a 2-adic leaf qubit needs one.
Thus the three-qubit leaf has uniform conditional expected cost C_0<=6.
Put eta=1/(1-2^-kappa). At startup levels i<a the next expected cost
is at most 2C_i. At later levels it is at most 2eta C_i. These bounds
do not assume independence of attempt cost and success: conditional
on reaching a fresh attempt, its children have the same cost bound;
the pointwise failure bound controls the geometric probability of
reaching later attempts. Summing gives the recurrences. Induction
also proves almost-sure termination at every finite tree depth.

Since m<=mu and 2^kappa>=2mu,

    eta^(m-a)<=exp(m/(2^kappa-1))<e<3.

Every root, at every scale and earlier history, therefore satisfies

    expected originals <=6*2^m eta^(m-a)<18*2^m<=C,
    C=18*2^mu.                                       (11.2)

All failed merges, discarded inputs and rejected labels are counted.
The nominal retained ancestor count nq_D is not used in place of
this expected original-copy bound.

The odd decoder uses exactly F roots. Each of at most n 2-adic bits
uses at most two roots in expectation, or at most two originals at
width one. Thus ideal expected acquisitions are at most Qstar, also
on wrong-answer histories. Markov gives probability at most 2^-10 of
exceeding Qcap. The capped and ideal uncapped algorithms can be coupled
until that event. Nothing conditions a root on fitting the source cap.

Every actual branch terminates: decoder and arithmetic loops have fixed
lengths, every tree retry needs new leaves, and every new leaf needs an
acquisition. The global cap stops any attempt to exceed Qcap. Source
errors can affect the selected trees or labels but cannot bypass this
cap or any fixed field width.

## 12. Unconditional success

For the active stride branch, Section 9 proves odd recovery except for
its low-pool event, decoder score errors, source-cap event or extraction
errors. The low-pool failure is at most 2^(-3B/4)<2^-190. Conditional
on each fixed low transcript in E and Fitodd, the decoder failure is
at most 2^-20; integrating preserves this bound without an independence
assumption. Fitodd's failure is contained in the global ideal source
cap event of Section 11.

Section 5 couples the actual capped computation to the ideal latent
computation until the first wrong extracted label, with total error
at most 2^-14. Section 10 adds at most 2^-30 for its per-bit attempt
caps. With correct previous choices, all its bit measurements are exact.
The total error is therefore less than

    2^-190+2^-20+2^-10+2^-14+2^-30 < 2^-8.            (12.1)

For the fallback, its seed error is at most 2^-20 and its backward
first-error sum is at most 2^-30. Add the same source, extraction,
and 2-adic errors; their sum is also less than 2^-8. For M=1 there
is no odd decoder error. The finite branch has error at most 2^-10.
Thus every N>=2 and every s satisfy the stated unconditional success.
All resource bounds include the same bad, discarded and aborted branches.

## 13. Every-branch resource bounds

Put E=2^((3/2)sqrt n), L=log2 n and n>=64. The exact profile gives

    m<=mu<(3/2)sqrt n+7/2<=2sqrt n, 2^mu<12E,
    2^kappa<=4mu=O(sqrt n), kappa+1=Theta(L),
    lam_i<=kappa+1+min(i,w), lam_max=O(sqrt n),
    2^lam_max=O(sqrt n 2^sqrt n).

For an odd tree, q=3*2^m=O(E) and ell=m+2=O(sqrt n). The uniform
root source bound is C=18*2^mu=O(E). Fixed field widths and all bounds
below apply on numerical-label and abort branches too.

### 13.1 Root count, fallback, and exact source cap

The pool parameters obey log2 A=O(sqrt n), gpool=O(sqrt n), and
B>=n-2 for every odd M>1. Thus hdist=Omega(sqrt n) tends to infinity
uniformly in M. The n<256 or hdist<16 fallback occurs at only finitely
many bit lengths. Its executable rule remains part of the algorithm;
the finite maximum over their inputs affects only an outside constant.
On the active branch Delta=Theta(L), nu=O(L), Kseed=O(sqrt n), and
Kblock=O(L). The exact formula (9.2) gives

    F=O(ell^2/L+ell+n)=O(n).

For M=1, F=0. Small odd M only reduces H and its backward blocks;
it does not reduce the odd-tree width B. The 2n term in (11.1) covers
all small-width 2-adic trees without a support event. Hence

    Q<=Qcap=1024[C(F+2n)+2n]=O(n E)                   (13.1)

on every branch. The literal F is polynomial in n in both branches,
so log2 Qcap=O(sqrt n) and the collective extractor has h_e=O(sqrt n).
All cap and field parameters have O(n) bits or fewer. Expected source
cost is used only for the cap's failure probability.

### 13.2 Fixed aligned fields and uniform generation

Reserve the polynomial source, decoder, arithmetic, and controller
scratch FIRST. Its addresses have O(L) bits. Reserve all tree arrays
after it. A field of f bits is padded to t=2^ceil(log2(max(1,f))) bits.
An array with a power-of-two row count Ein has size Ein*t, also a
power of two; align its base to a multiple of that size. Padding costs
at most a factor two. Greedy alignment loses less than the next block's
size, so total padding and alignment cost only a constant space factor.

Use fixed slots, not a growing heap. At each depth through mu, reserve
three table slots of Emax=2^(kappa+1+w) rows and field width the next
power of two at least 3n. The Section 7 high parts are below 3n bits
for n>=64. Reserve a constant number of such maximum-size array slots
for the one active merge's scratch. A smaller power-of-two array size
divides its slot size, so the fixed base is aligned for every actual
row count and field width. Depth-first evaluation needs at most two
input/sibling tables and one output per depth. Reuse a slot only after
release; reuse merge scratch only after the active merge ends. Slot
flags and base addresses are stored in the polynomial prefix.

For such an array a field-bit address is the concatenation of its fixed
prefix, row bits, and log2 t=O(L) offset bits. At field selection, write
the prefix and row bits into a working address register in O(Aaddr)
raw bit operations, where Aaddr=ceil(log2(Mem+2))=O(sqrt n) by the
space bound below. Hold those bits fixed while the field is processed.
Offset updates, comparisons, or resets take O(L) raw work per logical
bit action. The full address already exists; its use pays Aaddr under
the model, which covers reading/copying that full index for the action.
There is O(Aaddr) setup per field, not per bit. No row-width multiply
is hidden: field addresses are formed by concatenation.

A constant number of working field addresses suffices per comparison,
copy or addition. Their Aaddr-bit contents fit in the prefix. Quantum
lookups remain full scans of the known classical rows. Quantum wire
numbers have O(L) bits because only O(n) qubits are allocated. Emit
each exact gate and its inverse from sequential wire-pointer loops in
O(L) raw work per gate; read the selecting table bit through the field
pointer above. No quantum address or lookup oracle is used. Every
controller operation and emitted gate still pays the global Aaddr.
Raw costs below include this generation, but not yet that global charge.

### 13.3 Merge, leaf, and recursive work

For one merge let Ein=2^lam and Eout=2^lam'. The classical sort makes
O(Ein*lam) comparisons and moves on (b+lam)-bit keys. Field selection
and bit-pointer generation give raw cost O((b+lam)L+Aaddr) per
comparison or move. Since lam,b,Aaddr=O(sqrt n), the total is O(nLEin).
Binary search has O(lam) iterations per row, each costing
O((lam+b)L+Aaddr) for midpoint arithmetic, keys and field selection.
Its cost and the rank/offset arrays fit the same bound.

Each output high part needs a constant number of field selections and
an O(n)-bit addition, with raw cost O(nL+Aaddr)=O(nL). The inverse-block
scan has O(Ein+Eout) operations on O(sqrt n)-bit indices. Full quantum
lookup scans have O((Ein+Eout)(lam+b)) gates and table reads, O(L)
generation per action, and O(Aaddr) field setup per row. Initialization
and exact inverse passes are included. Therefore

    raw merge work=O(nL(Ein+Eout)).                   (13.2)

This is valid also for b=0 with its explicit rank concatenation.
Startup has Eout=4Ein; later Eout<=2Ein or the root shrinks to two.
Thus a level-i attempt costs O(nL2^lam_i) raw work. Its two children
have 3*2^(i+1) distinct nominal source ancestors. Charge equally to
those ancestors. At a fixed level different attempts have disjoint
ancestry because failed inputs are discarded and never reused. Each
acquired original receives at most one charge per level. A partial
tree at abort has only a prefix of these charged operations.

The leaf has eight entries and three retained originals, with raw work
O(nL) per retained original. Using the proved upper bound on lam_i,
all leaf/merge raw work per acquired original is at most

    O(nL[1+sum_(i=0)^(m-1)2^lam_i/(3*2^(i+1))])
      =O(nL2^kappa(w+2))=O(n^2L).                    (13.3)

The geometric sum after the width cap is at most two; the preceding
sum has at most w unit terms. Rejected originals have no table charge.
The denominator is the actual three-qubit leaf size, not kappa+1.
Multiply by global Aaddr=O(sqrt n), also on controller reads/writes,
to get charged tree work O(n^(5/2)L Qcap) on every branch.

There are O(mQcap) calls, merge tests and frame changes, plus a final
partial stack. Each frame or cap update can conservatively use O(nL)
raw work. Its charged total is O(n^2L Qcap)+poly(n), below the tree
allowance. This covers zero-removal levels, root measurements, label
differences, control movement and reset. Clearing O(n) quantum work
at abort and releasing fixed slots fit the same bound. Table clearing
or overwriting is already in (13.2).

### 13.4 Source processing, decoder, and initialization

Physical Mult_alpha has O(n^2) logical work per original. Controlled
Shift uses O(n). Collective extraction has
O(n h_e log(h_e+2)+n^2)=O(n^2) logical work, including the ordinary
exact dyadic unwrap and schoolbook final multiply/round. The polynomial
prefix and quantum wire indices add O(L) raw generation per action.
Every action still pays the global O(sqrt n) indexed charge. Thus
fully charged source processing costs O(n^(5/2)L) per acquisition,
including rejected copies, wrong-label paths, all counters and resets.
An n-bit transfer to a leaf field has O(nL+Aaddr) raw work and fits.
The literal source acquisition cost n+1 is smaller and is included.

The active terminal seed has O(ell/L+1) stages, at most 512q grid
candidates per stage and O(ell+L) records. Initialize each exact
O(n)-bit residue by a schoolbook product once per stage record, then
advance it by one addition per candidate. Stream the candidates with
only a running maximum. Its logical work is

    O(nq(ell^2/L+ell))+poly(n)=O(n^2 E)+poly(n).

Even the conservative O(n) generation/index factor gives O(n^3E),
below the total claimed below. Backward blocks have at most sqrt n
candidates, polynomially many stages and records, and O(n)-bit exact
scores/products. Their complete charged work is polynomial. Physical
scales and the final dyadic denominator exponent H+2ell+11 are O(n).
The finite fallback has fixed finite work for its finitely many bit
lengths and changes only an outside constant.

Profile computation, CRT and source-transform constants, fixed tables,
field parameters and final rounding have polynomial setup. If the whole
fixed classical allocation is initialized at the start, count its
O(n^2 2^sqrt n) bits separately. Even O(sqrt n) raw generation and
the O(sqrt n) indexed charge per bit give O(n^3 2^sqrt n), below the
time bound. This is not silently treated as polynomial setup. Later
attempted-array initialization is already included in (13.2).

Combining source, tree, control, decoder, and allocation costs with
(13.1),

    T=O(n^(5/2)L Qcap)+O(n^3E)+O(n^3 2^sqrt n)+poly(n)
      =O(n^(7/2)L2^((3/2)sqrt n)).                    (13.4)

Every term bounds the actual capped branch. No work expectation or
unaccounted successful-tree conditioning is used for this conclusion.

### 13.5 Space

At most m finished sibling indices and one active index are live,
including two same-level inputs. They occupy at most
(m+1)lam_max<=8n qubits. An active merge adds O(sqrt n) scratch, and
source transforms/collective extraction use O(n) reusable qubits.
Each root is measured at once. Thus S_Q=O(n) on every branch.

The fixed allocation has O(mu) table slots and a constant number of
merge-scratch slots. Each has at most 2^(kappa+1+w) rows and O(n)-bit
fields; the new widths (7.3) are below 3n for n>=64. Aligned padding
costs a constant factor, so

    S_C=O(mu*n*2^(kappa+1+w))+poly(n)
        =O(n^2 2^sqrt n).                            (13.5)

The prefix contains source counters, O(nL) extraction records,
O(n(ell+L)) seed records, exact arithmetic, frame/base addresses and
allocation metadata. All are polynomial size. No exponential gate
stream, candidate list, or trace is stored. Fixed widths and slots are
valid also on incorrect numerical labels and source-cap aborts. This
proves the global Aaddr=O(sqrt n) used above, including during operations
in the smaller polynomial prefix.

## 14. Exact structured envelopes

The four structured representatives are

    B_T(n)=n^(7/2)(log2 n)2^((3/2)n^(1/2)),
    B_C(n)=n^2 2^(n^(1/2)),
    B_Qubits(n)=n,
    B_Sources(n)=n2^((3/2)n^(1/2)).

Every coefficient and power is an explicit rational. The time, classical
space, and source representatives have exact growth index 1/2; quantum
space has index zero. The representatives apply for n>=2, with the
explicit finite branch covering n=1. All four bounds hold jointly for
the one algorithm and the same source cutoff (11.1).

## 15. Error tolerance and scope

The claimed fractional tolerance is epsilon(n)=0 under this exact model:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

Under this promise the unconditional full-secret and every-branch resource
guarantees hold for all N>=2 and all s. No positive tolerance is asserted.
A zero-tolerance proof does not prove that larger tolerance is impossible.
