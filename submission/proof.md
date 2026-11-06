# PSW1: variable-width streaming sieve with a weighted work cutoff

## 0. Joint theorem and provenance

For every integer N>=2 and every s in Z/NZ, let n=ceil(log2 N) and
L=log2 n. The single algorithm PSW1 below recovers the entire s from
independent ideal source copies with unconditional probability at least
1-2^-8>2/3. On every execution branch, including failed attempts, rejected
copies and both cutoff branches, it has the simultaneous bounds

 T=O(n^5 L^2 2^(sqrt(nL)+sqrt n)),
 S_C=O(n^2) classical bits, S_Q=O(n) qubits,
 Q=O(n^(3/2)L^(1/2)2^(sqrt(nL)+sqrt n)).

These asymptotic representatives apply for n>=2; the explicit finite branch
covers n=1 as well. All constants are absolute and independent of N,s and
outcomes. The exact resource growth indices are [1/2,0,0,1/2]. The fifth
claim is fractional tolerance0 with the baseline's exact clean-copy model.
This is not a cube-root-time or optimality claim.

Direct material source: PSR2 submission 16bb6065-c3ca-45fb-b514-86106a310646,
archive 7f835a08d1b109847a9b921c02b35361ed350bd0. Its complete streaming
combiner, signed-label framework, source/decoder implementation and most
proof text are reproduced/adapted here. Also directly consulted and used:
SLS submission 59facd77-4082-40d9-910e-9060c197e72a, archive
643c22bdf74a96b1e08a0eb56f562396c3084adc, for the comparator-rank sweep,
distribution-free pairing proof and polynomial-space charging; and CS1
submission f1481815-9577-4990-abe3-7b79fa5d9284, archive
200ef0387acb280adcd272f4fbcdb805d1786bbe, for latent-label extraction,
untouched top bits, exact source transforms and full-frequency all-modulus
decoding. Prior verdicts are not premises. All needed arguments are included.

The changed algorithm uses widths that vary by level and an additional
weighted-attempt cutoff. The old source-only cutoff would not establish the
new worst-case time: it could multiply the source budget by the largest
combiner cost. Section8 instead bounds expected weighted attempts, then
caps that exact quantity. Its explicit parameter profile yields the stated
leading sqrt(n log n) time exponent while preserving polynomial memory.
The polynomial-space Regev class is established literature; no new class
or invention of subset-sum collimation is claimed. The historical sources
are Regev quant-ph/0406151, Section3; Kuperberg1112.3333, Section4.6; and
Kitaev quant-ph/9511026. They provide context, not unaccounted subroutines.

## 1. Charged implementation conventions

All arithmetic is on explicit bit strings. A w-bit add, comparison, copy or
increment has O(w) Boolean gates using ripple carry, with O(w) scratch.
Reversibly compute a Boolean circuit, copy out its answer, then reverse it;
a permutation can be computed into a fresh register, swapped, and erased by
its inverse. NOT, CNOT and Toffoli suffice, and Toffoli has an exact constant
Clifford+T decomposition. Wire counters, generation, initialization, resets,
measurements and classical reads/writes are counted. Every indexed action
also pays O(log(S_C+S_Q+2)) bit operations. Gates are generated in streaming
order; no circuit description of exponential length is stored.

Only H, S, S-dagger and these exact reversible gates are used. In particular,
there is no arbitrary-N QFT circuit or approximate rotation to synthesize.
Fourier LABELS are inferred by nondestructive translation tests, with their
precision, tests and global error budget charged below. The source is used
only for fresh mixed copies; no purification, preparation inverse/control,
QRAM, hidden-shift oracle or subset-sum oracle is available or used.

Write N=2^a2 M with M odd, d=floor(log2 N), omega=exp(2 pi i/N),
s1=s mod M and s=s1+M s2 (mod N), 0<=s2<2^a2.

## 2. Source identities and exact transforms

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

## 3. Finite-precision classical table and source-label extraction

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


EXTRACT uses Qcap fixed in Section 8. Put J_e=n+4,

    h=ceil(log2(2^16 Qcap (n+5))), F=2^21 h.

It runs RUN(F) below once, without verification, fallback or restart.
Conditional on the latent label k, the data register is unchanged by every
test. Afterward discard that register and keep its control qubit, applying X
when the positive phase convention is needed. The latent-label mixture makes
this procedure valid for the mixed source, without access to its purification.

Translation Tr_c: u -> u + c mod N satisfies Tr_c chi_k = omega^(-k c) chi_k.
A TEST WITH SHIFT c (0 <= c < N) works as follows. Prepare an ancilla in |+>.
Apply Tr_((N - c) mod N) controlled by it, so the |1> branch gets eigenvalue
omega^(k c). Measure the ancilla in X (H then Z) or in Y (S^dagger, H, then Z).
The +-1 outcome has mean cos(2 pi c k/N) or sin(2 pi c k/N). Conditioned on
k, chi_k and every spectator are unchanged and outcomes are independent. A test
at LEVEL j is the test with shift 2^j mod N. Each test costs one controlled
modular addition, O(n) core steps.

### Level-wise extraction RUN(F)

For each j = 0..J_e take F tests at level j per basis, giving empirical means
x_j and y_j. Then decode as follows.

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
RUN(F(h)) uses 2 (J_e + 1) F(h) tests, that is O(n^2 h) core steps.


Since e^-h <= 2^-h, the per-call probability of an incorrect label is at most
4(n+5)2^-h <= 1/(2^14 Qcap). The union bound for at most Qcap adaptive calls is
2^-14, including discarded copies. Couple to an ideal run which outputs the
true latent label on every call, ignoring EXTRACT's internal test outcomes.
No later choice uses those internal outcomes. This coupling preserves the
untouched-bit argument; one does not condition it on extraction succeeding.
Each call takes O(n^2 h+n^2) core operations, O(n) qubits and O(n^2) classical
bits. For unwrapping store the n+5 six-bit directions; handle one empirical
mean at a time with binary counters. All loops have their stated fixed bounds.

## 4. Streaming combiner and the depth-first tree

Main-branch parameters are computed once for n>=256. For an integer v>=1 put

    delta(v)=ceil(log2(2(v+1)))=1+bit_length(v), where bit_length(v)=floor(log2 v)+1.

Starting from a positive integer R, repeatedly replace v by v-delta(v)
until nonpositive. Write the positive values in reverse order as
v_1,...,v_mstar=R, and call their sum S(R). The terminal v_0 is -1 or0:
for v>=5, delta(v)<v, and v=1,2,3,4 give terminal -1,-1,0,0.
Choose R as the least positive integer with S(R)>=n. This is a concrete
finite computation: S(R)>=R, so R<=n; a sequential search and integer
profile generation take polynomial work and memory. In fact Section9
proves R=O(sqrt(n log n)). Set

    q0=2^(R+1).

A PS_TREE_D call, 1<=D<=n, receives independent leaf phase qubits whose
known labels are uniform on [0,2^D). Put B=D-1. If B=0 return one leaf.
Otherwise use all mstar profile levels. From i=mstar down to1 allocate
b_i=min(v_i,B-already_allocated). Since S(R)>=n>B, this finishes with
sum_i b_i=B. Put r_i=b_i+1 and p_i=sum_(j<i)b_j. Level0 returns a leaf.
When b_i=0, leveli simply returns its level(i-1) child without a combiner.
Otherwise build r_i fresh level(i-1) outputs and apply the following
combiner. Before each attempt, AFTER its child outputs have been built,
add 2^v_i to the global weighted-attempt counter, or abort if that would
exceed Wcap of Section8. Both counters are exact binary integers.
All repeated attempts get the same charge, including every failed attempt.

For i>=1, recursively obtain r_i independent outputs from level i-1,
one at a time, retaining earlier siblings. Their integer labels a_1,...,a_r_i
are all divisible by 2^p, p=sum_(t<i)b_t. Their joint state is

    2^(-r_i/2) sum_(x in {0,1}^r_i) exp(2 pi i th A(x)) |x>,
    A(x)=sum_j x_j a_j,

where th is the current source secret divided by its effective denominator.
The combiner returns a qubit of label A(x1)-A(x0), or FAIL:

1. Reversibly compute (A(x)/2^p) mod 2^b_i, measure it to obtain e,
   and clear that now-classical register. The remaining state is uniform in
   magnitude on the fiber X_e={x: (A(x)/2^p) mod 2^b_i=e}.
2. Compute R_e(x)=#{y<x: y in X_e} into a clean (r_i+1)-bit register.
   This is an explicit quantum circuit, not an oracle: enumerate all
   classical y=0,...,2^r_i-1; compute its residue classically from the stored
   a_j; if it equals e, compare quantum x to constant y and conditionally
   increment the rank counter. Uncompute each comparison scratch immediately.
   Each iteration uses polynomially many (at most O(n^3)) core operations,
   and O(n) scratch; it retains no list of subsets or sums.
3. Measure all rank bits except the low bit, obtaining j=floor(R_e(x)/2).
   Enumerate the classical subsets again, counting members of X_e, and save
   just x0 and x1, of ranks 2j and 2j+1. If x1 does not exist, FAIL and discard.
   Otherwise the state is the equal-magnitude superposition of x0,x1,
   together with their rank registers.
4. The measured high rank bits can be reset. Clear the remaining rank bit
   by XOR with the branch indicator: choose a position at which x0 and x1
   differ, and use x's bit there, XORing a known constant if necessary.
   Map x to the branch-indicator qubit by XORing x0, then using its chosen
   differing pivot bit to clear every other differing position. This is an
   invertible affine circuit on all basis states. All other input qubits
   are now zero and are released. The surviving qubit has phase
   exp(2 pi i th [A(x1)-A(x0)]), up to a global phase.

The output label is an integer divisible by 2^(p+b_i). Signed additions and
right shifts for the known divisible labels have the same bit costs.
If FAIL occurs, discard this node's inputs, rebuild r_i fresh child outputs
and retry. Retry also means fresh copies throughout those child calls.

Combiner lemma (distribution-free). For any fixed child labels, the residue
measurement has probability |X_e|/2^r_i and each subsequent pair has its size
as probability mass divided by 2^r_i. Exactly |X_e| mod 2 indices in each
fiber are unpaired. Thus

    Pr[FAIL | all child labels] <= 2^b_i/2^r_i = 1/2.

This holds for arbitrary labels, not only a heuristic uniform distribution.
The measurements are only computational-basis measurements of deterministic
functions, so their distributions do not depend on the phases or the secret.
Every step, including exponentially long scans and FAIL branches, is charged.

For every stage, 2r_i<=2(v_i+1)<=2^delta(v_i), so
product_i r_i<=product_i(2r_i)<=2^(R-v_0)<=2^(R+1)=q0.
A returned tree contains q_D=product_i r_i distinct leaves, although
construction may consume many more through failures. Every root frequency
is a signed sum of those leaf labels, with each coefficient in {-1,0,1} and
at least one nonzero: distinct x0,x1 differ in some child, and child leaf sets
are disjoint. This is an induction from the single-leaf state. Consequently
its label is 2^B W, with integer |W|<2 q0. Sums used during a node obey the
same bound by the number of leaves below it. All stored labels and sums have
O(n+log2 q0)=O(n) bits, including on branches with incorrect extracted labels.
Pairing, rank and success decisions inspect label residues below bit B only.
The tree is evaluated depth first and keeps no full recursion tree.

## 5. Untouched top bit and root-frequency distribution

For the ideal run write each accepted leaf label k_l=u_l+2^B tau_l,
0<=u_l<2^B, where tau_l are independent fair bits. Condition on all low u_l,
all subset residue/rank measurements and retry choices, and independent past
roots. Every conditioned measurement has probabilities depending only on low
residues, not on phases; all pair choices inspect bits below B. Therefore
the tau_l of a returned tree remain independent fair bits. This factorization
also includes discarded attempts. Internal EXTRACT records are averaged out
in this ideal run; they do not guide any tree decision.

Lemma 5.1. The root has known frequency 2^B W, and conditional on the above
low-bit information,

    W=c+sum_(l in S+)tau_l-sum_(l in S-)tau_l, |S+|+|S-|>=1,
    |E exp(2 pi i y W)| <= |cos(pi y)|,                         (5.2)
    Pr[W odd]=1/2.                                            (5.3)

Here c is an integer because the root's low-label sum is divisible by 2^B.
The signed sets are determined by low-bit pairings; they are nonempty by
the distinct-incidence induction in Section 4. Each fair bit contributes
an absolute characteristic factor |cos(pi y)|, proving both statements.
This argument makes no uniformity claim for W itself.

## 6. Odd-part recovery by free-frequency decoding

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so N >= 3 * 2^a2
and d - 1 >= a2. Put theta = s1/M in [0,1). Every stage uses D = d, B = d - 1,
nq = q0 and

    K = 2^13 (ceil(log2 nq) + ceil(log2 n) + 30).

The stages are j = 0, 1, ..., J, where J = min{ j >= 0 : 2^(j+3) > 2M }. By
minimality, J + 1 <= log2 M <= n.

Source for stage j. Compute alpha_j by extended Euclid and CRT so that
alpha_j = 1 (mod 2^a2) and alpha_j = 2^j (2^(d-1-a2))^(-1) (mod M). Then alpha_j is a
unit modulo N. A leaf qubit is made as follows:
- acquire a fresh copy and apply Mult_(alpha_j);
- run EXTRACT to obtain k, and accept iff k < 2^d (otherwise discard the copy and
  acquire again);
- on acceptance, apply X to the control.

In the ideal run, accepted labels are i.i.d. uniform on [0, 2^d), each copy is
accepted with probability 2^d/N > 1/2, and the qubit is pq_k(alpha_j s), i.e. it
has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^(d-1) W th = W 2^(d-1-a2) alpha_j s / M = 2^j W s1 / M   (mod 1),            (9.1)

because 2^(d-1-a2) alpha_j = 2^j (mod M) and s = s1 (mod M). So a PS_TREE_d root of
stage j is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known
frequency f = 2^j W.

Measurement. For i = 1..K:
- run PS_TREE_d;
- obtain a fair bit beta_i by measuring H|0>;
- measure the root in X (beta_i = 0) or Y (beta_i = 1), recording Z_i in {+1,-1}
  together with W_i and beta_i.

Ideally E[Z_i | f_i, beta_i] = cs_(beta_i)(f_i theta) with f_i = 2^j W_i.

Candidates. Put P_j = j + ceil(log2 nq) + 8, and identify an integer c with the
point zeta = c/2^(P_j) on the circle R/Z.
- Stage 0 uses every c in [0, 2^(P_0)).
- Stage j >= 1 uses every c whose point lies within circular distance
  rad_j = 2^-(j+2) of the previous center z_(j-1). This is one or two explicit
  integer intervals.
- Both z_(j-1) (denominator 2^(P_(j-1))) and rad_j are multiples of 2^-(P_j),
  so the two arc endpoints are themselves candidates.
- There are at most 2^(ceil(log2 nq)+7) + 2 <= 2^(ceil(log2 nq)+8) candidates.

The candidate set is fixed by information available at the start of the stage.

Score. For each candidate, using exact integer arithmetic,

    score(c) = sum_i Z_i * tab_(beta_i)( ((f_i c) mod 2^(P_j)) / 2^(P_j) ).

Enumerate the candidates in increasing order, keeping the K residues
(f_i c) mod 2^(P_j) and updating each with one addition per step, and keep a
running maximum. Let z_j = c*/2^(P_j) for the least maximizer c*. All loops have
fixed lengths, and the decoder returns a candidate on every branch.

Lemma 6.1. Suppose theta is within circular distance rad_j of z_(j-1) (no
condition when j = 0). Then, in the ideal run, with probability at least
1 - 2^-20/n, theta is within circular distance 2^-(j+3) of z_j.

Proof. Let Fs_i be the sigma-field of everything up to and including root i
of the stage, and Gt_i the sigma-field of Section 5 for tree i. For a
candidate point zeta, let Delta = theta - zeta, taken as a circular
difference, and let xi_i = Z_i cs_(beta_i)(f_i zeta). Conditional on
Fs_(i-1), Gt_i and the top bits of tree i (hence on W_i), averaging over the
fair basis bit gives

    E[xi_i | ...] = (1/2)[cos(2 pi f_i theta) cos(2 pi f_i zeta) + sin(..) sin(..)]
                  = (1/2) cos(2 pi f_i Delta).

By (4.1), the computed score differs from sum_i xi_i by at most K/625.

Near point. Let zeta0 be the candidate nearest theta. In stage 0 the
candidates cover the circle. In stage j >= 1 the candidate arc contains theta
and has candidate endpoints. Either way |Delta0| <= 2^-(P_j + 1). Since
|f_i| < 2^j 2 nq,

    |f_i Delta0| < 2^(j+1) nq 2^-(P_j + 1) <= 2^-8.

So E[xi_i | Fs_(i-1)] >= (1/2) cos(pi/128) for every realization.

Far points. Call zeta far if |Delta| >= 2^-(j+3). In stage 0 we always have
|Delta| <= 1/2. In stage j >= 1, both theta and zeta lie within rad_j of
z_(j-1), so |Delta| <= 2^-(j+1). Hence xx = 2^j |Delta| lies in [1/8, 1/2] for
every far zeta. Tree i uses copies independent of Fs_(i-1). By Lemma 5.1, its
top bits are fair and independent given Fs_(i-1) and Gt_i. So by (5.2) with
phi = 2^j Delta, and since a real part is at most the modulus,

    E[xi_i | Fs_(i-1)] = E[ (1/2) Re E[exp(2 pi i 2^j Delta W_i) | Fs_(i-1), Gt_i] | Fs_(i-1) ]
                       <= (1/2) cos(pi xx) <= (1/2) cos(pi/8).

Concentration. For each fixed candidate, sum_i (xi_i - E[xi_i | Fs_(i-1)]) is a
martingale whose increments lie in intervals of length 2. By Azuma-Hoeffding
it deviates by at least K/64 with probability at most
exp(-(K/64)^2/(2K)) = exp(-K/8192). Outside these events for zeta0 and every far
candidate,

    score(zeta0) >= (K/2) cos(pi/128) - K/64 - K/625
                 >  (K/2) cos(pi/8)   + K/64 + K/625 >= score(far zeta),

because (1/2)(cos(pi/128) - cos(pi/8)) > 0.0379 > 2/64 + 2/625 = 0.03445. So the
maximizer is not far. There are at most 2^(ceil(log2 nq)+9) events, and since
e^-x <= 2^-x, exp(-K/8192) <= 2^-(ceil(log2 nq) + ceil(log2 n) + 30). The failure
probability is therefore at most 2^(9-30)/n <= 2^-20/n. QED.

For stage j+1 the hypothesis of Lemma 6.1 is the conclusion of stage j, since
2^-(j+3) = rad_(j+1). By induction, with probability at least 1 - 2^-20, theta
lies within 2^-(J+3) < 1/(2M) of z_J. Output s1 = floor(M z_J + 1/2) mod M. This
equals s mod M because theta = s1/M, and the circular distance handles
wrap-around.


## 7. 2-adic recovery

If a2 = 0, put s2 = 0 and skip this section. Otherwise s - s1 = M s2 (mod N) for
a unique s2 in [0, 2^a2). The bits of s2 are found at levels g = 0..a2-1. Let
s2low be the known low g bits. Put sh_g = s1 + M s2low (mod N), wd = a2 - g, and
rem = (s2 - s2low)/2^g in Z/2^wd. Then s - sh_g = M 2^g rem (mod N).

Leaf qubit for level g:
- acquire a copy and apply Shift_(sh_g), which makes the secret s - sh_g;
- run EXTRACT to obtain k, and apply X to the control.

Ideally the phase is exp(2 pi i k M 2^g rem/N) = exp(2 pi i kk rem/2^wd), with
kk = k mod 2^wd. Since 2^wd divides N and k is uniform on Z/NZ, kk is uniform on
[0, 2^wd). Use kk as the label.

- If wd = 1: if kk = 1, measure X; the outcome is + iff rem is even. If kk = 0,
  discard and repeat.
- If wd >= 2: run PS_TREE_wd (D = wd). If W is even, discard and repeat. If W is
  odd, the root is (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2,
  and an X measurement gives rem mod 2 exactly.

By (5.3), each attempt succeeds with probability exactly 1/2, even if s1 was
wrong. Set bit g of s2. In the ideal run with s1 correct, every bit is correct.
Output (s1 + M s2) mod N.


## 8. Complete algorithm, two cutoffs and success

For n<256 use exhaustive shift testing. For t=0,...,N-1 use at most n+10
fresh copies, subtract t modulo N controlled by the first qubit, and measure
that qubit in X. Reject t at the first minus and output the first candidate
passing every test, or0 if none. The true t=s always passes; each wrong
candidate passes a fresh test with probability1/2. Thus wrong output has
probability<(N-1)2^(-n-10)<2^-10. It uses at most N(n+10) copies,
O(n) qubits and O(n^2) classical bits. All charged work is O(Nn^4).
The fixed finite prefix is absorbed in the stated asymptotic bounds.

For n>=256 compute the profile of Section4, all decoder parameters and K.
Define integer budgets

    H0=nK+2n,
    Qstar=4*2^R*H0+2n, Qcap=1024Qstar,
    Wstar=2*mstar*2^R*H0, Wcap=1024Wstar.

The harmless use of nK+2n overbounds (J+1)K+2a2 for every modulus.
Initialize the acquisition counter and the weighted-attempt counter to zero.
Before any acquisition that would exceed Qcap, abort, release all registers
and output0. Before a combiner attempt, after building its inputs, check
whether adding its nominal weight2^v_i would exceed Wcap; if so abort
likewise, otherwise add it and execute the complete attempt. EXTRACT uses
this fixed Qcap. Run the odd-part decoder followed by the2-adic procedure,
then output(s1+M*s2) mod N. No circuit execution is hidden in either counter.

Expected source bound. In the ideal uncapped run each accepted leaf costs
at most two source copies. A leveli attempt succeeds with conditional
probability at least1/2. Therefore, uniformly over preceding history,
E_i<=2r_i E_(i-1). Zero-width shortcuts only reduce this bound.
As 2r_i<=2^delta(v_i),

    E_root<=2 product_i(2r_i)<=2^(R+2)=4*2^R.

No independence of attempt cost and success is required. The event of
reaching an attempt depends on earlier attempts; its fresh child calls
have the same uniform conditional cost bound. Summing their geometric
upper bound gives the displayed recurrence. Odd-part decoding uses at
most nK roots; each of at most n2-adic bits needs two roots in expectation
by parity fairness, or two direct copies when wd=1. Thus ideal expected
acquisitions are at most Qstar, irrespective of earlier decoder outcomes.

Expected weighted-attempt bound. For a root call, the expected number of
leveli attempts is at most 2 product_(j>i)(2r_j). The same conditional
geometric-sum argument proves this by induction, including attempts in
failed ancestors. Telescoping the profile gives

 product_(j>i)(2r_j)<=2^(R-v_i).

Hence the expected sum of weights at that level is at most
2*2^(R-v_i)*2^v_i=2*2^R, and at most2*mstar*2^R over all levels.
Zero-width shortcuts contribute zero. Summing over all roots, with the
same conditional argument for odd-W repeats, bounds ideal expected total
weighted attempts by Wstar.

Apply Markov separately to source count and weighted attempts in this
ideal uncapped process. Each cutoff changes it only on an event of
probability at most1/1024. In particular, a work cutoff before the next
attempt implies the uncapped weighted total would exceed Wcap; children
already built are already charged. There is no assumption that caps and
decoder events are independent. The odd-part error is at most2^-20, and
conditional on its correctness the2-adic measurements make no error.
On the actual capped run the probability of any EXTRACT label error is
at most2^-14 by Section3. Couple the actual and ideal processes until
a label error or cutoff. Total failure is at most

    2^-10+2^-10+2^-14+2^-20 < 2^-8.

The finite branch meets that bound as well. This proves unconditional
full-secret success at least1-2^-8. All trials, failures and aborts remain
in the resource counts; nothing is postselected free of charge.

## 9. Every-branch resources and explicit envelopes

### Exact profile estimates

Let D_R=max_(1<=v<=R)delta(v)=1+bit_length(R)<=log2R+2.
In the descending profile, each step interval has length at most D_R.
The upper rectangles of heights equal to the successive positive v cover
[0,R]. Thus

    R^2/2=integral_0^R x dx <=D_R*S(R), S(R)>=R^2/(2D_R).

The final interval is truncated at0 and obeys the same inequality.
For n>=65536 let L=log2n>=16 and Rtest=ceil(sqrt(nL)+sqrt n).
Since 1/sqrt n<=1/8,

 Rtest<=sqrt n*(sqrt L+9/8),
 log2Rtest<=(L+log2L+1)/2,
 2D_Rtest<=L+log2L+5.

For the middle inequality use
1+9/(8sqrt L)<=41/32<sqrt2. Also
2sqrt L-log2L-4>=0 for L>=16: it is zero at16 and its derivative
1/sqrt L-1/(L ln2) is positive there and thereafter. Consequently

 Rtest^2>=n(L+2sqrt L+1)>=n(L+log2L+5)>=2nD_Rtest,

so S(Rtest)>=n. The minimal chosen R is therefore at most Rtest.
This proves

    2^R=O(2^(sqrt(nL)+sqrt n)), R=O(sqrt(nL)).

For the finite interval256<=n<65536, R<=n supplies an absolute outside
constant (even2^65536 suffices for the exponential inequality). The algorithm
uses the same profile search throughout that interval; no giant exhaustive
prefix is introduced to obtain this inequality. The actual finite parameters
can be much smaller than this loose outside constant.
Since S(R)<=R^2 and S(R)>=n, R>=sqrt n. Hence2^R>=n for n>=16.

### Source copies

K=O(R+log n)=O(sqrt(nL)), so H0=nK+2n=O(n^(3/2)L^(1/2)). On every branch,

 Q<=Qcap=O(n^(3/2)L^(1/2)2^R)
       =O(n^(3/2)L^(1/2)2^(sqrt(nL)+sqrt n)).

This includes rejected labels, discarded trees, failed attempts and aborted
runs. The cap's binary length is O(R+log n)=O(sqrt(nL))=O(n), so the
EXTRACT parameter h is O(n); all its stated precision and probability
bounds remain valid under the new budgets.

### Space

A depth-first tree keeps at most sum_i(r_i-1)+1=B+1<=n source-phase qubits
as siblings/current outputs. Each combiner uses O(r_i+n)=O(n) scratch,
and source extraction/transforms use O(n) more. Released registers are
reused, so S_Q=O(n).

A successful leveli label is a signed sum of its distinct original leaf
labels, with coefficients in{-1,0,1}. Its magnitude is less than
q0*2^D, so O(n+R)=O(n) bits suffice even for incorrect numerical label
branches. O(n) retained phase qubits require O(n^2) label bits. Recursion
counters and budget snapshots use O(mstar*(R+log n))=O(R^2+R log n)
=O(nL)<=O(n^2) bits. The profile, single streaming subset/rank counter,
two selected strings, EXTRACT scratch and modular arithmetic fit O(n^2)
as well. K decoder frequencies and residues have O(n) bits each with
K=O(n), giving O(n^2). No list of2^r_i subsets is stored. Therefore
S_C=O(n^2) and every address/gate pays O(log n)=O(L).

### Work, on every actual branch

Each leveli attempt scans at most2^r_i subsets a fixed number of times.
As in Section4, each scan element, signed-sum recomputation, gate generation,
comparison and increment costs at most O(n^3) core operations. Since
r_i=b_i+1<=v_i+1, total attempt work is O(n^3 2^v_i).
The new counter checks/updates need O(R+log n)=O(n) bit operations per
attempt and are covered by the same bound. Thus the weighted cutoff gives

 all combiner core work <=O(n^3 Wcap)=O(n^5 L2^R),

because mstar<=R and H0=O(nR) imply Wcap=O(nR^2 2^R)=O(n^2 L2^R).
This argument holds even if a source cutoff occurs inside a child call.
A completed attempt was charged before it began; an unexecuted attempt
performs only the already charged children and one polynomial check.

Each EXTRACT takes O(n^3) core operations, since h=O(n). Its source
transforms and acquisition also fit that bound. Total leaf work is at most
O(n^3 Qcap)=O(n^(9/2)L^(1/2)2^R), smaller than O(n^5 L2^R).
Classical decoder grids cost at most O(n^4 q0)=O(n^4 2^R) core operations
using the conservative per-record bounds of Section6. Preprocessing uses
O(n^6) by schoolbook arithmetic, including profile search and tables.
It is smaller than O(n^5 L2^R), since2^R>=n. Resets, aborted allocations,
source counters and loop control are covered by these bounds.
Multiplying by the full O(L) address charge, and adding the n+1 cost per
acquisition, gives

 T=O(n^5 L^2 2^R)
  =O(n^5 L^2 2^(sqrt(nL)+sqrt n)).

All four bounds apply jointly to this single parameter rule and both caps.

### Exact growth indices

For B(n)=n^p L^q 2^(sqrt(nL)+sqrt n), with the stated nonnegative p,q,
log2B=sqrt n*(sqrt L+1)+O(log n). Thus
log2log2B=(1/2)log2n+(1/2)log2log2n+O(1), whose ratio to log2n tends
to1/2. The two space envelopes n^2,n have index0. The supported resource
structures are exactly the above expressions; no coefficient is inferred
from a heuristic or unspecified inner big-O. Only time contributes the
numeric score[1/2].

## 10. Error tolerance and limits

The fractional tolerance is epsilon(n)=0 under the exact error-model text:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

All N>=2 and s meet the success and resource guarantees above under this
promise. No positive tolerance or impossibility of greater tolerance is
asserted. The result is a rigorous implementation/accounting tradeoff of
known sieve ideas, not a new exponent breakthrough. Hosted mathematical
acceptance, if obtained, remains fallible review rather than formal proof.
