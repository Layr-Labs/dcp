"""Exact-integer falsification checks for the IFW-12-32 schedule of proof.md.

Configuration under test (proof.md Section 7, a = 1/2, A = 3/2, C = 3/4):

    w  = least integer with (4w)^2  >= 9n          (= ceil((3/4) sqrt n)),
    lw = least integer with (2lw)^2 >= 9n          (= ceil((3/2) sqrt n)),
    mu = least M >= 1 with (M-1)(w+lw+2) + 2w+lw+2 >= n,
    kappa = ceil(log2(mu+4)) + 3,  Lam = kappa+1+w, l = kappa+1+lw,
    r = 2Lam - l = kappa+1+2w-lw,  nqmax = 16*4^mu*Lam.

Every expected value below was derived by hand from these definitions before
running (see the assert blocks); failures print the first violated fact and
exit nonzero. These are finite falsification checks supporting, not replacing,
the analytic proof: they verify the parameter-dependent size facts S1-S6,
Lemma 7.0, the MERGE4I preconditions including the A = 2C endpoint analysis,
the Wald/Markov/LE cutoff constants, the field widths and the envelope
coefficient identities on every n of a dense range, a power-of-two ladder,
exhaustive tree-allocation cases, and large-n spot checks. Exact integer
arithmetic only (isqrt, Fraction); standard library only; no randomness.
"""

import sys
import time
from fractions import Fraction
from math import isqrt

FAILURES = []
CHECKS = [0]


def check(cond, fact, detail=""):
    CHECKS[0] += 1
    if not cond:
        FAILURES.append((fact, detail))
        if len(FAILURES) >= 5:
            report()
            sys.exit(1)


def clog2(x):
    """ceil(log2 x) for integer x >= 1."""
    return (x - 1).bit_length()


def least_sqrt_div(a, b):
    """Least y >= 0 with (b*y)^2 >= a (y = ceil(sqrt(a)/b), exact)."""
    y = (isqrt(a) + b - 1) // b
    while (b * y) ** 2 < a:
        y += 1
    while y > 0 and (b * (y - 1)) ** 2 >= a:
        y -= 1
    return y


def params(n):
    w = least_sqrt_div(9 * n, 4)
    lw = least_sqrt_div(9 * n, 2)
    base = 2 * w + lw + 2
    step = w + lw + 2
    mu = 1
    if base < n:
        mu = 1 + -(-(n - base) // step)
    kappa = clog2(mu + 4) + 3
    lam = kappa + 1 + w
    l = kappa + 1 + lw
    r = 2 * lam - l
    return {
        "n": n, "w": w, "lw": lw, "mu": mu, "kappa": kappa,
        "Lam": lam, "l": l, "r": r,
        "bin": lam - kappa, "binr": 2 * lam - 1 - kappa,
        "bm4": lam + l - kappa, "rc4": 2 * lam + l - 1 - kappa,
    }


def phi(p, k):
    return 0 if k == 0 else (k - 1) * p["bm4"] + p["rc4"]


def dense_checks(p):
    n, w, lw, mu, kappa = p["n"], p["w"], p["lw"], p["mu"], p["kappa"]
    lam, l, r = p["Lam"], p["l"], p["r"]
    # definitions (independent of the closed forms asserted next)
    check((4 * w) ** 2 >= 9 * n and (4 * (w - 1)) ** 2 < 9 * n, "w-def", n)
    check((2 * lw) ** 2 >= 9 * n and (2 * (lw - 1)) ** 2 < 9 * n, "lw-def", n)
    check((mu - 1) * (w + lw + 2) + 2 * w + lw + 2 >= n, "mu-def", n)
    check(mu == 1 or (mu - 2) * (w + lw + 2) + 2 * w + lw + 2 < n, "mu-min", n)
    check(8 * (mu + 4) <= 2 ** kappa and 2 ** kappa < 16 * (mu + 4), "kappa-def", n)
    # closed forms of the capacities (derived by hand)
    check(p["bin"] == w + 1 and p["binr"] == 2 * w + kappa + 1, "bin-forms", n)
    check(p["bm4"] == w + lw + kappa + 2, "bm4-form", n)
    check(p["rc4"] == 2 * w + lw + 2 * kappa + 2, "rc4-form", n)
    # S1
    check(lw - w >= 2 * clog2(n) + 6, "S1-gap", n)
    check((1 << (lw - w)) >= 64 * n * n, "S1-power", n)
    check(l >= lam + 1, "S1-l>Lam+1", n)
    # S2 endpoint analysis
    check(lw <= 2 * w, "S2-lw<=2w", n)
    check(2 * w - lw in (0, 1), "S2-2w-lw", n)
    check(r == kappa + 1 + 2 * w - lw, "S2-r-identity", n)
    check(r in (kappa + 1, kappa + 2), "S2-r-range", n)
    check(l <= 2 * lam, "S2-l<=2Lam", n)
    # S3
    check((mu + 4) ** 2 < 4 * n, "S3-mu+4<2sqrt", n)
    check(81 * (mu - 1) * (mu - 1) < 16 * n, "S3-mu-1<4/9sqrt", n)
    # S4
    check(mu + 4 < n, "S4-mu+4<n", n)
    check(w >= clog2(n) + 3, "S4-w>=logn+3", n)
    check(kappa <= w, "S4-kappa<=w", n)
    check((2 ** kappa) ** 2 < 1024 * n, "S4-2^kappa<32sqrt", n)
    # S5
    check(lam * lam < 4 * n, "S5-Lam<2sqrt", n)
    check(l <= 2 * lam, "S5-l<=2Lam(dup)", n)
    check(p["rc4"] <= 4 * lam and p["rc4"] * p["rc4"] < 64 * n, "S5-rc4<8sqrt", n)
    check(lam >= kappa + 2, "pre-Lam>=kappa+2", n)
    check(l >= kappa + 3, "pre-l>=kappa+3", n)
    # S6
    check(4 * (mu + 5) * lam <= 20 * n, "S6-stack<=20n", n)
    # Lemma 7.0(a),(c)
    check(phi(p, mu) >= n, "7.0a-Phi(mu)>=n", n)
    check(81 * (mu - 1) * (mu - 1) < 16 * n, "7.0c-4^mu", n)
    # MERGE4I preconditions at the endpoint
    check(lam + 1 <= l, "pre-Lam+1<=l", n)
    check(r >= 1, "pre-r>=1", n)
    check(p["bm4"] - r >= 1, "pre-r'>=1-below-root", n)
    check(2 * l - lam - kappa >= w + 3, "pre-r'>=w+3", n)
    check(p["rc4"] - r >= 1, "pre-r'>=1-root", n)
    # Wald cutoff precondition: 2^kappa >= 8(mu+4) makes attempts
    # succeed with conditional probability >= 1 - 1/(2(mu+4)).
    check(2 ** kappa >= 8 * (mu + 4), "wald-2^kappa", n)
    # LE cap constants (Lemma 5.2): (sqrt n + 1)/n <= 65/4096 for n >= 4096,
    # and Cf >= 20 support via Qcap >= 6144 nqmax >= 6144 Lam.
    check(65 * n >= 4096 and 4096 * 4096 * n <= (65 * n - 4096) ** 2, "LE-(sn+1)/n", n)
    check((4 * lam) ** 2 >= 9 * n, "LE-Lam>=Csqrt", n)
    check(6144 * lam >= 20 * (isqrt(n) + 1), "LE-Cf>=20", n)
    # n log n <= 2^lw (Section 13 core-step combination)
    check((1 << lw) >= n * clog2(n), "core-nlogn<=2^lw", n)


def heavy_checks(p):
    n, w, lw, mu, kappa = p["n"], p["w"], p["lw"], p["mu"], p["kappa"]
    lam, l, r = p["Lam"], p["l"], p["r"]
    # Wald factor: rt^m < 3 for m = mu+4, rt = 2(mu+4)/(2(mu+4)-1).
    # The exact integer inequality (2m)^m < 3(2m-1)^m is checked directly for
    # m <= 20000. For larger m the function (2m/(2m-1))^m is decreasing in m
    # (its log m*ln(1+1/(2m-1)) has derivative ln(1+1/(2m-1)) - 1/(2m-1) < 0),
    # so the exact check at m = 20000 covers it.
    m = mu + 4
    m_eff = min(m, 20000)
    check((2 * m_eff) ** m_eff < 3 * (2 * m_eff - 1) ** m_eff, "wald-rt^m<3", n)
    # Field widths: log2 nqmax <= n (nqmax = 16*4^mu*Lam = 2^(4+2mu)*Lam).
    e = n - 4 - 2 * mu
    check(e >= 1 and lam.bit_length() <= e + 1, "fields-log2nqmax<=n", n)
    # nqmax definition and nq_D <= nqmax support at full depth (beta = 4, m4 = mu).
    nqmax = 16 * (4 ** mu) * lam
    check(nqmax == (1 << (4 + 2 * mu)) * lam, "nqmax-def", n)
    # h_e = O(sqrt n) support: log2 Qcap <= (8/9) sqrt n + 2 log2 n + O(1),
    # checked as a generous explicit bound with the worst-case stage count.
    nb = clog2(n)
    k = 8192 * (clog2(nqmax) + nb + 30)
    qstar = 6 * nqmax * (n * k + 2 * n) + 2 * n
    qcap = 1024 * qstar
    check(qcap.bit_length() - 1 <= (8 * isqrt(n)) // 9 + 2 * nb + 80, "he-log2Qcap", n)
    # Markov cap scale: Qcap = 1024 Q* >= 6144 nqmax.
    check(qcap >= 6144 * nqmax, "markov-Qcap>=6144nqmax", n)


def allocation_checks(n):
    """Exhaustive tree-allocation verification for one n over sampled m4."""
    p = params(n)
    bm4, rc4, bin, binr = p["bm4"], p["rc4"], p["bin"], p["binr"]
    mu, lam = p["mu"], p["Lam"]
    nqmax = 16 * (4 ** mu) * lam
    allocations = 0
    m4set = list(range(0, min(mu, 10) + 1))
    for extra in (mu - 2, mu - 1, mu):
        if extra > 10:
            m4set.append(extra)
    for m4 in m4set:
        if m4 == 0:
            bmax = min(rc4 - 1, p["n"])
            for B in range(1, bmax + 1):
                allocations += 1
                check_allocation(p, B, 0, m4)
        else:
            for R in range(0, bm4):
                B = phi(p, m4) + R
                if B <= p["n"]:
                    allocations += 1
                    check_allocation(p, B, phi(p, m4), m4)
    # complete small-B coverage including the m4 = 0 root case
    for B in range(1, min(rc4 + 2, p["n"]) + 1):
        allocations += 1
        check_allocation(p, B, None, None)
    return allocations


def check_allocation(p, B, phi_val, m4_hint):
    n, mu = p["n"], p["mu"]
    bm4, rc4, bin, binr = p["bm4"], p["rc4"], p["bin"], p["binr"]
    lam, r = p["Lam"], p["r"]
    if B >= rc4:
        m4 = 1 + (B - rc4) // bm4
    else:
        m4 = 0
    if m4_hint is not None:
        check(m4 == m4_hint, "alloc-m4-hint", (n, B))
    check(phi(p, m4) <= B and phi(p, m4 + 1) > B, "alloc-m4-maximal", (n, B))
    if m4 >= 1:
        R = B - phi(p, m4)
        check(0 <= R < bm4, "alloc-R-range", (n, B))
        beta = -(-R // bin)
        rem = R
        total = 0
        for _ in range(beta):
            b = min(bin, rem)
            check(0 <= b <= bin, "alloc-b<=bin", (n, B))
            total += b
            rem -= b
        check(rem == 0 and total == R, "alloc-binary-sum", (n, B))
        check(beta == 0 or (beta - 1) * bin < R, "alloc-beta-minimal", (n, B))
    else:
        beta = 1
        while (beta - 1) * bin + binr < B:
            beta += 1
        rem = B
        total = 0
        levels = 0
        b = min(binr, rem)
        check(0 <= b <= binr, "alloc-root<=binr", (n, B))
        total += b
        rem -= b
        levels += 1
        while rem > 0:
            b = min(bin, rem)
            check(0 <= b <= bin, "alloc-low<=bin", (n, B))
            total += b
            rem -= b
            levels += 1
        check(levels == beta and total == B and (beta - 1) * bin + binr >= B,
              "alloc-m4=0-sum", (n, B))
    check(beta <= 4, "alloc-beta<=4", (n, B))
    m = beta + m4
    check(m <= mu + 4, "alloc-m<=mu+4", (n, B))
    nq_d = (1 << beta) * (4 ** m4) * lam
    check(nq_d <= 16 * (4 ** mu) * lam, "alloc-nq_D<=nqmax", (n, B))
    check(m4 >= 1 or B < rc4, "alloc-m4=0-domain", (n, B))


def report():
    print("checks run: %d" % CHECKS[0])
    if FAILURES:
        for fact, detail in FAILURES:
            print("FAIL: %s (n=%s)" % (fact, detail))
        print("IFW-12-32 checks: FAILED (%d failure(s))" % len(FAILURES))
    else:
        print("IFW-12-32 checks: all passed")


def main():
    t0 = time.time()
    # ---- independently hand-derived expected values, asserted first ----
    p = params(4096)
    check((p["w"], p["lw"], p["mu"], p["kappa"], p["Lam"], p["l"], p["r"])
          == (48, 96, 28, 8, 57, 105, 9), "expect-n=4096", 4096)
    q = params(4097)
    check((q["w"], q["lw"], q["mu"], q["kappa"], q["Lam"], q["l"], q["r"])
          == (49, 97, 28, 8, 58, 106, 10), "expect-n=4097", 4097)
    # endpoint identities at both parities of 2w - lw
    check(2 * p["w"] - p["lw"] == 0 and p["r"] == p["kappa"] + 1, "endpoint-r=kappa+1", 4096)
    check(2 * q["w"] - q["lw"] == 1 and q["r"] == q["kappa"] + 2, "endpoint-r=kappa+2", 4097)
    # hand-derived capacities at n = 4096
    check((p["bin"], p["binr"], p["bm4"], p["rc4"]) == (49, 105, 154, 210),
          "expect-capacities-4096", 4096)
    # exact rational identities of the declared envelopes
    check(Fraction(3, 2) + Fraction(8, 9) == Fraction(43, 18), "id-3/2+8/9", "const")
    check(2 / Fraction(9, 4) == Fraction(8, 9), "id-2/(9/4)", "const")
    check(Fraction(43, 18) - Fraction(8, 9) == Fraction(3, 2), "id-43/18-8/9", "const")
    check(2 * Fraction(3, 4) == Fraction(3, 2), "id-2C=A", "const")
    check(Fraction(3) + Fraction(1, 2) == Fraction(7, 2), "id-3+a", "const")
    # success chain: 2^-20 + 2^-10 + 2^-11 + 2^-20 = 769/524288 < 2^-8
    budget = (Fraction(1, 2 ** 20) + Fraction(1, 2 ** 10)
              + Fraction(1, 2 ** 11) + Fraction(1, 2 ** 20))
    check(budget == Fraction(769, 524288), "id-budget=769/524288", "const")
    check(budget < Fraction(1, 256), "id-budget<2^-8", "const")
    check(1 - budget > Fraction(2, 3), "id-success>2/3", "const")
    # finite branch union bound: N 2^-(n+10) <= 2^-10 (n = ceil(log2 N))
    for N in (2, 3, 4, 5, 7, 4095, 2 ** 12 - 1, 2 ** 20 - 1, 2 ** 4095):
        nfb = (N - 1).bit_length()
        check(N <= 2 ** nfb and N * 2 ** 10 <= 2 ** (nfb + 10), "finite-branch", N)
    # ---- dense sweep over every n in [4096, 10^6] ----
    for n in range(4096, 1000001):
        pr = params(n)
        dense_checks(pr)
        if (n - 4096) % 101 == 0:
            heavy_checks(pr)
    # ---- power-of-two ladder to 2^40 ----
    for exp in range(12, 41):
        n = 2 ** exp
        pr = params(n)
        dense_checks(pr)
        heavy_checks(pr)
    # ---- large-n spot checks ----
    for n in (10 ** 7, 10 ** 8, 10 ** 10, 10 ** 12):
        pr = params(n)
        dense_checks(pr)
        heavy_checks(pr)
    # ---- exhaustive tree allocation over sampled m4 and all R ----
    allocations = 0
    for n in (4096, 4097, 4100, 5000, 8192, 2 ** 16, 2 ** 20, 10 ** 6):
        allocations += allocation_checks(n)
    report()
    print("allocation cases verified: %d" % allocations)
    print("elapsed: %.1f s" % (time.time() - t0))
    return 1 if FAILURES else 0


if __name__ == "__main__":
    try:
        peak = None
        code = main()
        try:
            import resource
            peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        except Exception:
            peak = None
        if peak is not None:
            print("peak RSS: %d KiB" % peak)
        sys.exit(code)
    except AssertionError as error:
        print("ASSERTION FAILURE: %s" % error)
        sys.exit(2)
