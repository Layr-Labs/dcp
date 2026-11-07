# COMPLETE ADAPTED virtual IFW-12-32, part2/2

All resource assertions concern VIRTUAL P. Read virtual-phase.md then
virtual-decode.md as ONE source proof. Explicitly ADAPTED from actual
d8c97e5d-b6be-4684-84ea-a20585c455f5,commit
77ea9d1cb9fca3eb62d593e7dde282cc0d1a1547,original full proof SHA256
e1455f0b08ac0a6dce46fd071ac395042cdb74fc51711ebee0ca2fd02e5dbf93.
NOT byte-identical: new Section5.7 defines reduced ideal law; Section8.2
replaces Hp and its factorization/stopping proof; Section11.1 replaces
the retry-cost appeal with explicit conditional fresh-attempt sums.
All original algorithm/profile/guards/decoders and credits remain.
Historical first-person provenance denotes original authors.

--- BEGIN COMPLETE ADAPTED VIRTUAL PART ---

## 9. Odd part: s1 = s mod M by free-frequency decoding

If M = 1, put s1 = 0 and skip this section. Otherwise M >= 3, so N >= 3 * 2^a2
and d - 1 >= a2. Put theta = s1/M in [0,1). Every stage uses D = d, B = d - 1,
nq = nq_d and

    K = 2^13 (ceil(log2 nq) + ceil(log2 n) + 30).

The stages are j = 0, 1, ..., J, where J = min{ j >= 0 : 2^(j+3) > 2M }. By
minimality, J + 1 <= log2 M <= n.

Source for stage j. Compute alpha_j by extended Euclid and CRT so that
alpha_j = 1 (mod 2^a2) and alpha_j = 2^j (2^(d-1-a2))^(-1) (mod M). Then alpha_j is a
unit modulo N. A leaf qubit is made as follows:
- acquire a fresh copy and apply Mult_(alpha_j);
- run LE to obtain k, and accept iff k < 2^d (otherwise discard the copy and
  acquire again);
- on acceptance, apply X to the control.

In the ideal run, accepted labels are i.i.d. uniform on [0, 2^d), each copy is
accepted with probability 2^d/N > 1/2, and the qubit is pq_k(alpha_j s), i.e. it
has phase exp(2 pi i k th) with th = alpha_j s/N. For every integer W,

    2^(d-1) W th = W 2^(d-1-a2) alpha_j s / M = 2^j W s1 / M   (mod 1),            (9.1)

because 2^(d-1-a2) alpha_j = 2^j (mod M) and s = s1 (mod M). So a TREE_d root of
stage j is, ideally, (|0> + exp(2 pi i f theta)|1>)/sqrt 2 with the known
frequency f = 2^j W.

Measurement. For i = 1..K:
- run TREE_d;
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

Lemma 9.1. Suppose theta is within circular distance rad_j of z_(j-1) (no
condition when j = 0). Then, in the ideal run, with probability at least
1 - 2^-20/n, theta is within circular distance 2^-(j+3) of z_j.

Proof. Let Fs_i be the sigma-field of everything up to and including root i
of the stage, and Gt_i the sigma-field of Section 8 for tree i. For a
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
every far zeta. Tree i uses copies independent of Fs_(i-1). By Lemma 8.1, its
top bits are fair and independent given Fs_(i-1) and Gt_i. So by (8.2) with
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

For stage j+1 the hypothesis of Lemma 9.1 is the conclusion of stage j, since
2^-(j+3) = rad_(j+1). By induction, with probability at least 1 - 2^-20, theta
lies within 2^-(J+3) < 1/(2M) of z_J. Output s1 = floor(M z_J + 1/2) mod M. This
equals s mod M because theta = s1/M, and the circular distance handles
wrap-around.

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

By (8.3), each attempt succeeds with probability exactly 1/2, even if s1 was
wrong. Set bit g of s2. In the ideal run with s1 correct, every bit is correct.
Output (s1 + M s2) mod N.

## 11. The complete algorithm and its source cap

Finite branch (n < 4096, i.e. N <= 2^4095). For each cand = 0..N-1 in order, use
n+10 fresh copies: apply Shift_cand, measure the control in X, and reject cand
at the first minus outcome. Output the first cand with no rejection, or 0.
- For cand = s every outcome is plus.
- For cand != s the two data branches are orthogonal, so each outcome is uniform.
- A union bound over cand gives Pr[wrong] <= N 2^-(n+10) <= 2^-10.
- Q <= N(n+10), and all other resources are bounded by absolute constants.

Main branch (n >= 4096). Compute a2, M, d, J, K and all tree parameters. The values
w, lw, mu, kappa, Lam, l and nqmax are those of Section 7, and m4 <= mu, m <= mu + 4 and nq_D <= nqmax for every
B <= n used. Put

    Q* = 6 * nqmax ((J+1)K + 2 a2) + 2 a2,    Qcap = 1024 Q*,

and then h_e, h_A, t_V and Cf from Section 5. A binary down-counter of acquisitions is kept,
at amortized O(1) bit flips per acquisition. IFW-12-32 stops, releases everything
and outputs 0 before an acquisition would exceed Qcap. Otherwise it runs
Section 9 and then Section 10. Parameter, CRT and table computations are
polynomial in n.

Lemma 11.1 (expected ideal acquisitions). In the ideal UNCAPPED run, the
expected number of acquisitions is at most Q*.

Proof. An accepted leaf qubit needs at most 2 acquisitions in expectation
(acceptance probability > 1/2 in Section 9, and 1 in Section 10). Let Qv_i be the
expected number of acquisitions until VEC(i) returns. By Lemma 6.1 and Section 7 at binary levels, and by
Lemma 8.2 at four-input levels, each merge attempt succeeds with conditional probability at least
1 - 2^(2-kappa) >= 1 - 1/(2(mu + 4)), given Hp of Lemma 8.2 at four-input levels and given everything before its
step 1 at binary levels (Lemma 6.1 holds for any input tables, so all labels may be included). For four-input attempts Hp is the REDUCED field of Section8.2,
not the actual full pre-merge record; the external history before its
fresh input construction may be full. Conditional on that external
history, averaging the Hp bound gives success probability at least
p0=1-1/(2(mu+4)),rt=1/p0. Current input-construction costs may correlate with
that attempt's outcome; independence between them is NOT required.
At each invocation all inputs are freshly rebuilt and failed inputs
are discarded. By induction on height their conditional expected
construction cost is at most f_i*Qv_i uniformly over the external past.
Let Reach_j mean that the j-th attempt is begun. Given the full past
at the start of an attempt, its fresh source/product law is the one
just proved, so P(Reach_j)<= (1-p0)^(j-1). Tower conditioning gives
 E[sum_j 1_Reach_j*C_j]
 <=sum_j P(Reach_j)*f_i*Qv_i <= f_i*Qv_i/p0.
Use monotone convergence for these nonnegative sums, or truncate the
number of attempts and pass to the limit. This proves almost-sure
return and Qv_(i+1)<=rt*f_i*Qv_i without conditioning on current LE
outcomes or assuming independence of C_j and current success.
Moreover
rt^m <= exp(m/(2(mu + 4) - 1)) <= e < 3 for m <= mu + 4. A LEAF needs Lam accepted leaf qubits, so
Qv_m <= 3 * 2^beta 4^m4 * 2 Lam = 6 nq_D <= 6 nqmax. Section 9 runs (J+1)K trees. Section 10 needs, per bit, an
expected 2 trees by (8.3), or, when wd = 1, an expected 2 single acquisitions since kk is uniform on {0,1}. Summing
gives the bound. QED.

Lemma 11.2 (work per branch). On every actual branch of the main branch, the
number of core steps is at most
O(n^2 log n + n 2^lw) Qcap + O(n^(5/2) nq) + poly(n),
where nq = nq_d.

Proof. Charge every core step to an acquisition, or to the fixed-length loops.
- Each acquisition (transform, acceptance test, X, counter update) takes O(n^2)
  core steps. All LE calls together take O(n^2 log n) Qcap + O(n^(5/2)) core
  steps on every branch (Section 5.6), since there is one LE call per
  acquisition and Q <= Qcap.
- A LEAF table of 2^Lam entries costs O(n 2^Lam), charged to its Lam acquisitions.
- A binary merge attempt (inputs and output of length at most 2^Lam) costs O(n^2 2^Lam) by Section 6.2. Its two
  inputs were built from at least 2 Lam acquisitions that no other attempt at that level uses, since inputs of a failed
  merge are discarded and never reused. With at most four binary levels and the LEAF tables, this is
  O(n^2 2^Lam / Lam) <= O(n^2 2^(kappa+1) 2^w) = O(n^(5/2) 2^w) <= O(n 2^lw) per
  acquisition, by S4 (2^(kappa+1) <= 64 sqrt n) and S1 (2^(lw-w) >= 64 n^2).
- A MERGE4I attempt costs O(n^(2a) 2^l) = O(n 2^l) core steps by Section 6.3, on every branch: there L = 2^Lam <= 2^l = mX,
  2^(lam') <= 2^Lam, lam (lam + b) <= 2 n^a * 10 n^a = 20 n^(2a) = 20 n, and Cp lam <= (2^(Lam+kappa+3) + 1) 2 n^a =
  O(2^kappa n^a 2^l) = O(n 2^l), as Lam + 1 <= l and 2^kappa <= 32 sqrt n (S4). An attempt at the j-th
  four-input level (j >= 1) has inputs built from 2^beta 4^j Lam >= 4^j Lam acquisitions that no other attempt at that
  level uses. Summed over j this is O(n^(2a) 2^l / Lam) = O(n 2^l / Lam) = O(sqrt n 2^kappa 2^lw) = O(n 2^lw) per
  acquisition, by S4, S5 and Lam >= C n^a = (3/4) sqrt n.
- Root measurements and bookkeeping are O(n) per tree, and each tree uses at
  least one acquisition.
- The decoder's fixed loops cost (J+1) * 2^(ceil(log2 nq)+8) * K * O(n)
  = O(n * nq * sqrt n * n) core steps, as K = O(n^(1-a)) = O(sqrt n) since log2 nq <= log2 nqmax =
  4 + 2mu + log2 Lam = O(sqrt n) (Section 7).
- Setup is poly(n) and runs once. It covers the parameters, extended Euclid and
  CRT for at most n stages, the Mult constants, Q*, h_e, the table of Section 4,
  the Section 10 shift values, and the decoder's initial residues
  (f_i c) mod 2^(P_j).

Every loop is either fixed-length or consumes acquisitions, so every branch
terminates with this many core steps. QED.

## 12. Success probability

In the ideal UNCAPPED run, Section 9 errs with probability at most 2^-20, and
Section 10 then never errs. By Markov and Lemma 11.1, the source cap is reached
in the ideal run with probability at most 1/1024. Capping changes the run only
on that event. The actual run differs from the ideal one only if some LE call
returns a wrong label or the high-confidence cap aborts, which has probability
below 2^-11 + 2^-20 (Section 5.6, Lemma 5.2). So

    Pr[output = s] >= 1 - 2^-20 - 2^-10 - 2^-11 - 2^-20 >= 1 - 2^-8 > 2/3.

The finite branch succeeds with probability at least 1 - 2^-10. These are
additive couplings. There is no conditioning on favorable labels, caps or
outcomes.

## 13. Resources on every branch

Throughout, n >= 4096. From Section 7: m4 <= mu, m <= mu + 4, nq_D <= nqmax,
4^mu < 4 * 2^((8/9) sqrt n) (the coefficient 8/9 = 2/(C+A) is exact), 2^lw < 2 * 2^((3/2) sqrt n), 2^w < 2 * 2^((3/4) sqrt n), 2^kappa < 32 sqrt n, mu + 4 < 2 sqrt n,
Lam < 2 sqrt n, and every lam_i, l and b_i is at most 8 sqrt n.

Sizes. log2 nq <= log2 nqmax <= 4 + 2mu + log2 Lam = O(sqrt n), so K = O(sqrt n); J + 1 <= n and a2 <= n, so
Lam ((J+1)K + 2 a2) = O(n^2) and Q* = O(n^2 4^mu). Also log2 Qcap = (8/9) sqrt n + O(log n) = O(sqrt n), so
h_e = O(sqrt n) and h_A, T_V = O(log n), and the cost statements of Section 5 hold as written.

Q. On every branch, Q <= Qcap = 1024 Q* = O(n^2 4^mu) = O(n^2 2^((8/9) sqrt n)).

Core steps. By Lemma 11.2, O(n^2 log n + n 2^lw) Qcap = O(n 2^lw n^2 4^mu) = O(n^3 2^lw 4^mu), as n log n <= 2^lw for n >= 4096
((3/2) sqrt n > log2 n + log2 log2 n + 1 there, increasingly). The
decoder term O(n^(5/2) nq) <= O(n^(5/2) nqmax) = O(n^(5/2) * 32 sqrt n * 4^mu) = O(n^3 4^mu) is smaller, and the poly(n) setup is smaller still.

S_Q. By S6 the depth-first stack holds at most 20 n index qubits. A merge adds O(n^a) = O(sqrt n) qubits of registers and scratch.
LE uses O(n) qubits (data, ancilla, arithmetic), and the data register is reset after each call. Transforms use O(n),
and each root qubit is measured at once. Released registers are reused. So S_Q = O(n).

S_C. The depth-first stack holds at most five tables per level (up to three finished siblings, the table being built or
merged, and one merge output), over at most mu + 5 levels, each of at most 2^Lam entries with high parts of at most 3n
bits and a common residue of at most n bits: 5(mu + 5)(3n 2^Lam + n) = O(sqrt n * n * sqrt n * 2^w) = O(n^2 2^w)
bits, as mu + 5 < 2 sqrt n (S3) and 2^Lam = 2^(kappa+1) 2^w <= 64 sqrt n * 2^w (S4). Binary merge scratch is O(2^Lam n^a) = O(n 2^w) bits
(Section 6.2); MERGE4I scratch is O((2^Lam + Cp)(Lam + b)) bits (Section 6.3) with Cp <= 2^(Lam+kappa+3)+1 = O(2^Lam 2^kappa) = O(n 2^w),
so the scratch is O(n^(3/2) 2^w) <= O(n^2 2^w) bits (Lam + b = O(sqrt n)).
The decoder stores K triples
(W_i, beta_i, Z_i) and K running residues of O(n) bits each, and enumerates its candidates without storing them. The
table of Section 4 is O(1), counters (including the O(sqrt n)-bit acquisition down-counter) and parameters are O(n)
bits, and LE uses O(n log n) classical scratch (Section 5.3) and the fallback counter. Since 2^w < 2 * 2^((3/4) sqrt n),
S_C = O(n^2 2^((3/4) sqrt n)). These are fixed allocations, so
the bound holds on every branch, including when labels are wrong; the work of each MERGE4I attempt is bounded through
its step 2.

T. By (2.1), with log2(S_C + S_Q + 2) = O(sqrt n) (the dominant term is log2 S_C = (3/4) sqrt n + 2 log2 n + O(1)),
T = O(n^3 2^lw 4^mu) * O(sqrt n) + (n+1) Qcap = O(n^(7/2) 2^lw 4^mu) = O(n^(7/2) 2^((43/18) sqrt n)), because
2^lw 4^mu < 8 * 2^((43/18) sqrt n) (lw < (3/2) sqrt n + 1 and 2mu < (8/9) sqrt n + 2 by S3 give
lw + 2mu < (43/18) sqrt n + 3, and 3/2 + 8/9 = 43/18 exactly), and the source term
(n+1) Qcap = O(n^3 2^((8/9) sqrt n)) is smaller.

All four bounds hold simultaneously for the same execution, with absolute constants independent of N, s and outcomes.

## 14. Exact growth indices and declared envelopes

The envelopes are

    B_T(n) = n^(7/2) 2^((43/18) sqrt n),   B_C(n) = n^2 2^((3/4) sqrt n),
    B_Q(n) = n,   B_samples(n) = n^2 2^((8/9) sqrt n).

By Section 13 the resources are O of these, and the finite branch n < 4096 is O(1). The coefficients 43/18, 3/4 and
8/9 are exact: at a = 1/2 the two exponential contributions to T share the power n^(1/2) and combine exactly
(2^lw < 2 * 2^((3/2) sqrt n), 4^mu < 4 * 2^((8/9) sqrt n), 3/2 + 8/9 = 43/18), and 2^w < 2 * 2^((3/4) sqrt n)
directly. For B(n) = 2^(c sqrt n) n^P with c > 0, log2 B = c sqrt n (1 + o(1)), so
log2 log2 B = (1/2) log2 n + log2 c + o(1) and g(B) = 1/2: g(B_T) = g(B_C) = g(B_samples) = 1/2. For B_Q(n) = n,
log2 log2 n / log2 n -> 0, so g = 0. The structured objects in submission.json are these envelopes.

## 15. Error tolerance

The fifth claim is epsilon(n) = 0 under the model in which every acquired copy
is an independent ideal coset state. Everything above is proved under this
model. No positive tolerance for malformed copies is claimed, and zero does
not assert that robustness is impossible.
