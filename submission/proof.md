# PSR-W34: streaming collimation with polynomial classical space at block width n^(3/4)

## 0. Joint theorem and provenance

For every integer N >= 2 and s in Z/NZ let n = ceil(log2 N). The single PSR-W34
algorithm below recovers the entire s from independent ideal rho_s copies with
unconditional probability at least 3/4. On every execution branch, including failed
attempts, rejected copies and cutoff branches, jointly:

    T   = O(n^7 2^(n^(3/4) + (3/4) n^(1/4) log2 n + n^(1/4))),
    S_C = O(n^2) bits,
    S_Q = O(n) qubits,
    Q   = O(n^(11/4) 2^((3/4) n^(1/4) log2 n + n^(1/4))).

The constants are absolute, independent of N, s and all outcomes. The formulas are
asymptotic representatives for n >= 2; the finite small-n branch below covers every
N >= 2, including n=1. The exact indices are [3/4, 0, 0, 1/4]. The fifth guarantee is
fractional tolerance 0 with exactly the baseline clean error-model text. These are
upper bounds, not optimality claims.

PSR-W34 IS the algorithm PSR2 of kaankolcu (Yukon submission
16bb6065-c3ca-45fb-b514-86106a310646, "PSR2: streaming collimation with polynomial
classical space") with ONE parameter changed: the number b of label bits collimated per
tree level is b = ceil(n^(3/4)) (the least integer with b^4 >= n^3) instead of
b = ceil(sqrt(n L/2)), L = ceil(log2(n+2)); it is also my own PSR-W23 (Yukon submission ef9cfb09-b4c9-471d-bb04-76c54a83d1d0,
b = ceil(n^(2/3))) with that one parameter changed again. Sections 1-3, 5-8 and 10 of this file are PSR2's text, reproduced in
full so that the file is self-contained; in Section 4 only the parameter block differs, and
Section 9 (the every-branch accounting) is recomputed. PSR2 itself reproduces and adapts
Sections 3-5.1 and 8-10 of CS1 (AdamGagol, Yukon submission
f1481815-9577-4990-abe3-7b79fa5d9284). No earlier verdict is a premise.

Primary sources, as in PSR2:

* O. Regev, arXiv:quant-ph/0406151v1, Section 3 (pp. 5-6): a combiner of l+4 phase qubits with a
  measured l-bit subset sum, and the polynomial-space tree. PSR2 replaces the combiner by an
  r = b + 1 streamed-fiber combiner that needs no bounded-fiber hypothesis (Section 4 below).
  Regev's omitted arbitrary-N extension is proved in Sections 5-7 below, as in PSR2.
* G. Kuperberg, arXiv:1112.3333v1, Algorithm 4.1, Proposition 4.2, Algorithm 4.4 and
  Section 4.6: depth-first collimation, untouched-label-bit argument.
* A. Kitaev, arXiv:quant-ph/9511026v1: eigenvalue measurement; the complete bounded-error
  label extraction is proved in Section 3.

What changes with b. A tree has m = ceil(B/b) levels instead of about sqrt(2n/log2 n), so it needs
(2r)^m expected source copies, retries counted: m is about n^(1/4), and log2 (2r) is about (3/4) log2 n,
so the samples are 2^((3/4) n^(1/4) log2 n + n^(1/4)) up to polynomial factors (sample growth
index 1/4, against 1/2 for PSR2). A combiner scans all 2^r subsets with r = b + 1, so time is
the samples times 2^(n^(3/4)) (time growth index 3/4, against 1/2 for PSR2). Classical and quantum
memory stay polynomial: nothing stored depends on 2^r. This is a different parameter point of
Regev's combiner, not an asymptotic speedup and not a new exponent:
fewer source copies are bought with more scan time, and the result is a Pareto tradeoff
against PSR2, not dominance of it.

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

Main-branch global parameters, computed once from n>=64:

    b=ceil(n^(3/4)), r=b+1, m*=ceil((n-1)/b), q0=r^m*.

Integers and roots here are computed by integer arithmetic (b is the
least integer with b^4>=n^3). A PS_TREE_D call, 1<=D<=n, takes independent
phase qubits with labels uniform in [0,2^D). Put B=D-1. Partition B bits into
m=ceil(B/b) successive blocks b_i, from low to high: b_i=b except possibly
the last, and sum b_i=B. Put r_i=b_i+1. For B=0 just return one leaf.

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

A returned tree contains q_D=product_i r_i <=q0 distinct leaves, although
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


## 8. Complete algorithm, hard acquisition cutoff and success

For n<64 use the finite exhaustive branch: for candidates t=0,...,N-1 test
at most n+10 fresh copies per candidate, subtracting t modulo N on control 1
and measuring that control in X. Reject on a minus; output the first candidate
passing every test, or 0 if none. The true shift always passes. For t!=s the
two data branches are orthogonal, so each independent test is fair. The chance
of any false candidate passing is at most (N-1)2^(-n-10)<2^-10. There are
at most N(n+10) acquired copies, O(n) qubits and O(n^2) classical bits.
Its time is O(N n^4); on the finite set n<64 this is covered by an absolute
constant in each declared asymptotic envelope.

For n>=64 compute all global parameters in Section 4 and decoder K. Define

    A=(2r)^m*,
    Qstar=2 A (n K+2n)+2n,
    Qcap=1024 Qstar.

Before any acquisition that would exceed Qcap, abort, release all registers,
and output 0. Otherwise run the odd-part decoder in Section 6 followed by
Section 7 and output (s1+M s2) mod N. EXTRACT uses this fixed Qcap.

In the ideal uncapped run, an accepted odd-part leaf costs at most 2 source
copies in expectation; a 2-adic leaf costs one. If E_i bounds the expected
cost through level i, the conditional success bound 1/2 implies

    E_0<=2, E_i <= 2 r_i E_(i-1), E_m<=2 (2r)^m* =2A.

For clarity no independence between cost and success of a node attempt is
needed: the event that attempt t is reached depends only on preceding
attempts, and its fresh inputs have the same cost law. Summing over attempts
with conditional failure probability <=1/2 gives the geometric upper bound.
The decoder uses at most nK roots. For each of at most n 2-adic bits, the
odd-W selection needs an expected two roots by (5.3); the wd=1 case needs an
expected two copies. Therefore ideal expected acquisitions are <=Qstar.
Markov bounds cutoff failure by 1/1024. The odd-part union bound is <=2^-20;
conditional on correct s1 the parity measurements make no further error.
The union probability of EXTRACT label error is <=2^-14 on the capped run.
An additive coupling gives total failure <=2^-10+2^-20+2^-14<1/4.
The finite branch also succeeds with probability >3/4. No success conditioning,
free postselection or expected-only resource statement is used.

## 9. Every-branch resource accounting and explicit envelopes

For n>=64 put c=n^(1/4) (so c>=2.82 and c^3>=22.4), ell=log2 n and E(n)=(3/4) c ell + c.
The exact finite parameters are b=ceil(n^(3/4)) (the least integer with b^4>=n^3), r=b+1,
m*=ceil((n-1)/b), q0=r^m* and A=(2r)^m*. They obey, for every n>=64:

(a) c^3<=b<c^3+1: b^4>=n^3=c^12 gives b>=c^3, and minimality gives (b-1)^4<c^12, so b-1<c^3.
(b) m*<c+1: m*=ceil((n-1)/b)<(n-1)/b+1<n/c^3+1=c+1, using b>=c^3.
(c) 2r=2b+2<2c^3+4=2c^3(1+2/c^3), and ln(1+x)<=x, so
    log2(2r) < 1+(3/4) ell+(2/c^3)/ln 2   (log2 c^3=(3/4) ell).
(d) log2 A=m* log2(2r) < (c+1)(1+(3/4) ell)+(c+1)(2/(c^3 ln 2))
    <= (3/4) c ell+c+(3/4) ell+1+0.5, because (c+1)/c^3<0.171 for c>=2.82 and 2/ln 2<2.886 (0.171*2.886<0.5).
    Hence log2 A<E(n)+(3/4) ell+1.5, and, as 2^(3 ell/4)=n^(3/4),
    A < 3 n^(3/4) 2^(E(n)).
(e) 2^r=2^(b+1)<2^(c^3+2)=4*2^(n^(3/4)).
(f) q0<A, because r<2r. Also ell<2.16 c (ln c<=c/e gives log2 c<=c/(e ln 2)<0.531 c, and ell=4 log2 c), so
    log2 A < 1.62 c^2+2.62 c+1.5 <= n for n>=64 (at c=64^(1/4)=2.83 it reads below 22<=64, and (1.62 c^2+2.62 c+1.5)/c^4 decreases).
    Hence log2 q0<=n, K=2^13(ceil(log2 q0)+ceil(log2 n)+30)<=2^13(n+ell+32)=O(n), and
    h=ceil(log2(2^16 Qcap (n+5)))=O(log Qcap+log n)=O(n).

These are inequalities of explicit deterministic parameters. In particular the retry
factor 2^m* inside A=(2r)^m*, at most 2^(c+1), is the part n^(1/4) of E(n); m* log2 r gives the part
(3/4) n^(1/4) log2 n.

Samples. Qstar=2A(nK+2n)+2n<=2A n(K+3), so on every branch
Q<=Qcap=1024 Qstar<=2048 A n(K+3)=O(n^2 A)=O(n^(11/4) 2^(E(n))), counting ALL fresh copies
including rejected labels, internal failed trees, discarded roots and cutoff. The source charge
(n+1)Q is included below.

Quantum space. At most r_i-1 saved sibling qubits are retained per active
recursion level. Their number is at most
sum_i r_i=B+m<=n+(c+1)=O(n). A combiner needs O(r_i+n)=O(n)
scratch for the input, residue, rank, comparisons and additions (r_i<=c^3+2<=n); these scratch
wires are reused by all nodes. Label extraction and transforms need O(n) more.
Measured root qubits are released immediately. Therefore S_Q=O(n).

Classical space. Each active level retains at most r_i labels, each O(n+log2 q0)=O(n)
bits, and a constant number of O(n)-bit counters/parameters. Across the
stack this is O(n sum_i r_i)=O(n^2). The rank scan stores only one subset
counter, its sum and count, plus the selected two r_i-bit strings. It never
stores 2^r_i subsets. Decoder K records and residues are O(n) bits each and
K=O(n); EXTRACT needs at most O(n^2) scratch. Store modular-multiply constants
as n O(n)-bit numbers, or generate them on demand. All allocations together
are O(n^2) bits. Quantum and classical memory addresses therefore cost O(log n).

Work. Each EXTRACT call costs O(n^2 h+n^2)=O(n^3) core operations, including all precision
tests, rational unwrapping and circuit generation; exact source transforms
cost O(n^2). Each node attempt scans at most 2^r subsets twice. Each scan step
has at most O(n^3) core work, including recomputing its signed sum (at most r labels of O(n)
bits), quantum comparison of an r-bit register and reversible controlled increment of an
(r+1)-bit counter; residue calculation and selected-pair cleanup are polynomially smaller.

Charge each node attempt to its consumed source descendants. Failed attempts
discard all inputs. Each acquisition belongs to at most one attempted node
at any particular level, and there are m*<c+1<=n levels. Hence on every branch,
even one cut off in a recursive call, there are at most O(n Qcap) completed
or active attempts. Rank scanning cannot loop without consuming its inputs.
All tree work is bounded by O(n^4 2^r Qcap) core operations. Classical
decoder search has at most O(q0) candidates per stage, K=O(n) records and O(n^2)
work per record, for O(n^4 q0) work total over <=n stages. Preprocessing
(integer roots, powers, CRT by Euclid, constants and fixed trigonometric
table generation) uses O(n^6) core work by schoolbook arithmetic.
The source, addressing, initialization and measurement charges give

    T = O(n^4 2^r Qcap log n + n^4 q0 log n + n^6 log n + n^3 Qcap log n)
      = O(n^(27/4) (log2 n) 2^(n^(3/4)+E(n)))
      = O(n^7 2^(n^(3/4)+E(n))).

The first line is the sum of the tree work, decoder search, preprocessing and extraction work,
each times the O(log n) address factor (S_C+S_Q is polynomial). With 2^r<4*2^(n^(3/4)) and
Qcap=O(n^(11/4) 2^(E(n))) the first term is O(n^(27/4) log n 2^(n^(3/4)+E(n))); q0<A gives
n^4 q0=O(n^(19/4) 2^(E(n))), n^3 Qcap=O(n^(23/4) 2^(E(n))) and n^6=O(n^6), all smaller. The last
step uses log2 n<2.16 n^(1/4). These are simultaneous deterministic bounds for the same capped
algorithm, not bounds for different configurations.

The declared envelopes are

    B_T(n)=n^7 2^(n^(3/4)+(3/4) n^(1/4) log2 n+n^(1/4)),   B_C(n)=n^2,   B_Q(n)=n,
    B_samples(n)=n^(11/4) 2^((3/4) n^(1/4) log2 n+n^(1/4)).

For B_T, log2 B_T=n^(3/4)+O(n^(1/4) log n), so log2 log2 B_T=(3/4) log2 n+o(1) and the index is
3/4. For B_samples, log2 B_samples=(3/4) n^(1/4) log2 n (1+o(1)), so
log2 log2 B_samples=(1/4) log2 n+log2 log2 n+O(1) and the index is 1/4 (the term log2 log2 n is
o(log2 n)). For B_C=n^2 and B_Q=n the limit is zero. Thus the exact indices are [3/4,0,0,1/4].
They do not assert fourth-root time or equivalence with other algorithms. The time envelope is larger
than PSR2's, while the sample envelope has a smaller growth index; classical and quantum memory
are the same polynomial envelopes as PSR2's. This is a Pareto tradeoff, not dominance of PSR2.
Relative to the repository exhaustive baseline all four resource guarantees are no worse
asymptotically, and time, qubits and samples are strictly better.

## 10. Error tolerance and limits

The fractional tolerance is epsilon(n)=0 under the exact error-model text:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

All N>=2 and s meet the success and resource guarantees above under this
promise. No positive tolerance or impossibility of greater tolerance is
asserted. The result is a rigorous implementation/accounting tradeoff of
known sieve ideas, not a new exponent breakthrough. Hosted mathematical
acceptance, if obtained, remains fallible review rather than formal proof.
