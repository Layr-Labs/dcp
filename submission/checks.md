# Finite falsification checks for the IFW-12-32 schedule

`checks.py` is a self-contained exact-integer test of the parameter-dependent
obligations of `proof.md` for the declared configuration
(a, A, C) = (1/2, 3/2, 3/4). It uses only the Python standard library
(`math.isqrt`, `fractions.Fraction`), no randomness, and exits nonzero on the
first violated fact (up to five are reported). These are finite falsification
checks: they support, and do not replace, the analytic proof of `proof.md`.

## Command and observed result

Executed in Ubuntu WSL:

    cd submission && python3 checks.py

Observed on 2026-11-07 (Python 3.14.4, WSL2, 12-core host):

    checks run: 40684392
    IFW-12-32 checks: all passed
    allocation cases verified: 76429
    elapsed: 5.1 s
    peak RSS: 13124 KiB
    exit status 0

Resource measurement: `/usr/bin/time -v` reported 5.10 s user time,
0.02 s system time, 13,124 KiB maximum resident set size, single process.

Re-run unchanged after the final `proof.md` edits (no `checks.py` change),
same environment: 40,684,392 checks, 76,429 allocation cases, elapsed 4.4 s,
peak RSS 13,108 KiB, exit status 0.

## Independently derived expected values (asserted first)

- n = 4096: (w, lw, mu, kappa, Lam, l, r) = (48, 96, 28, 8, 57, 105, 9),
  with 2w - lw = 0, r = kappa + 1 (hand-derived from the definitions:
  sqrt 4096 = 64, so w = 48 and lw = 96 exactly; w + lw + 2 = 146 and
  27 x 146 + 194 >= 4096 > 26 x 146 + 194 gives mu = 28; kappa =
  ceil(log2 32) + 3 = 8).
- n = 4097: (w, lw, mu, kappa, Lam, l, r) = (49, 97, 28, 8, 58, 106, 10),
  with 2w - lw = 1, r = kappa + 2.
- Capacities at n = 4096: (bin, binr, bm4, rc4) = (49, 105, 154, 210).
- Rational identities: 3/2 + 8/9 = 43/18, 2/(9/4) = 8/9, 43/18 - 8/9 = 3/2,
  2C = A, 3 + a = 7/2.
- Success budget: 2^-20 + 2^-10 + 2^-11 + 2^-20 = 769/524288 < 2^-8, and
  1 - 769/524288 > 2/3.
- Finite branch: for every tested N (including N = 2^4095, n = 4095),
  N 2^-(n+10) <= 2^-10, i.e. N <= 2^n with n = ceil(log2 N).

## What is covered

For every n in the dense range [4096, 10^6] (every single integer), plus a
power-of-two ladder 2^12..2^40 and spot values 10^7, 10^8, 10^10, 10^12:

- parameter definitions by exact integer predicates ((4w)^2 >= 9n with
  minimality, (2lw)^2 >= 9n, mu definition and minimality, 8(mu+4) <= 2^kappa
  < 16(mu+4));
- size facts S1-S6 of proof.md Section 7 in integer form, including the
  endpoint analysis lw <= 2w, 2w - lw in {0,1}, r in {kappa+1, kappa+2};
- Lemma 7.0(a) (Phi(mu) >= n) and 7.0(c) ((9(mu-1))^2 < 16n, the exact
  8/9-coefficient claim);
- MERGE4I preconditions (Lam >= kappa+2, Lam+1 <= l <= 2Lam, l >= kappa+3,
  r' >= 1 below the root and at the root, r' >= w+3);
- Wald cutoff constants (2^kappa >= 8(mu+4) and the exact integer inequality
  (2m)^m < 3(2m-1)^m for m = mu+4; for mu+4 > 20000 the check uses
  m = 20000, valid because (2m/(2m-1))^m decreases in m);
- LE cap constants (Lemma 5.2): (sqrt n + 1)/n <= 65/4096 in exact integer
  form 4096^2 n <= (65n - 4096)^2, and Cf >= 20 support 6144 Lam >=
  20(isqrt(n)+1);
- field widths log2 nqmax <= n (via bit lengths of 16 x 4^mu x Lam);
- a generous explicit bound on log2 Qcap ((8/9)sqrt n + 2 log2 n + O(1),
  supporting h_e = O(sqrt n)) with the worst-case stage count;
- n log2 n <= 2^lw (Section 13's core-step combination).

Tree allocation (proof.md Section 7): for n in {4096, 4097, 4100, 5000, 8192,
2^16, 2^20, 10^6}, the complete m4 = 0 domain (all B < rc4) and, for
m4 in [0, min(mu,10)] and {mu-2, mu-1, mu}, every R in [0, bm4) with
B = Phi(m4) + R <= n: 76,429 allocations in total. Each verified case checks
m4 maximality (Phi(m4) <= B < Phi(m4+1)), 0 <= R < bm4, beta = ceil(R/bin)
minimality, b_i <= capacity, sum b_i = B, beta <= 4, m <= mu + 4 and
nq_D = 2^beta 4^m4 Lam <= nqmax.

## Honest scope and limitations

- The dense range ends at 10^6 and the ladder at 2^40; the all-N statements of
  proof.md rest on the analytic chains there, not on these sweeps. The sweeps
  falsify transcription errors and base-case mistakes.
- The allocation verification samples m4 in [0, min(mu,10)] and the top three
  values; intermediate m4 at large n are structurally identical (the same
  beta = ceil(R/bin) code path over the complete R range) but were not all
  enumerated here. A larger 31,108,686-case research run over 14 n values with
  the same assertions is preserved in the mission's private research record.
- The exact Wald inequality is checked directly for mu+4 <= 20000 and via the
  decreasing-in-m reduction above for larger mu; the analytic proof of
  Lemma 11.1 (rt^m <= exp(m/(2(mu+4)-1)) <= e < 3) covers all m.
- The log2 Qcap check asserts a deliberately generous explicit bound; the
  proof claims only h_e = O(sqrt n).
- No quantum hardware, simulation of the full algorithm, or probability
  experiment is performed or claimed: the probability and concentration
  arguments of proof.md Sections 5, 8, 9 and 12 are proved analytically there.
