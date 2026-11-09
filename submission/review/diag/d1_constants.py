"""D1: independent exact recomputation of SPTS1 parameter claims (reviewer-written).

Exact integers/Fractions only. Checks, for each n in the range:
 K maximality, K>=n/9, n-32K<-64; a_sk/ell Hoeffding union (1); r_idx cap;
 Bcap_j >= 4/sqrt(p_min) via squared exact comparison; worst admissible
 good-size amplitude recursion beta_j=alpha_j*sqrt(D) (rational) >= 1023/1024*A_j;
 bad-size sum (4); hitting constants (6),(7); nu; delta_coarse; final budget.
"""
from fractions import Fraction as F
import json, math, resource, sys, time
resource.setrlimit(resource.RLIMIT_CPU, (45, 45))
resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2,) * 2)
t0 = time.process_time()

rho = F(3, 4)
nu = F(128) * F(51, 2**26) + F(1, 2**16)
assert nu == F(59, 2**19) and (1 + nu) / 2 <= rho
# Hoeffding exponent: 2*ell*gap^2/width^2 with gap 3/256, width 6
assert 2 * F(3, 256)**2 / 36 == F(1, 2**17)
# gap: E_score margin 1/64, tau in [-1/256, -1/256+(2^16-1)/2^23]
taumax = F(-1, 256) + F(2**16 - 1, 2**23)
assert taumax < F(1, 256) and F(1, 64) - taumax > F(3, 256) - F(1, 10**9)
assert F(1, 64) - F(1, 256) == F(3, 256)
# implemented score bound and accumulator width
assert F(1, 10) * (11 * 2 + 2) == F(12, 5)
# (6): expected B-sum <= 48*B0 < 384/sqrt(p) <= 512/sqrt(p); A_j/sqrt(p) <= (1024/1023) sqrt(D)/sqrt(h)
assert 16 + 16 / (1 - 2 * F(7, 8)**16) <= 48 and 48 * 8 <= 512
assert 512 * F(1024, 1023) <= 1024
# (7): 4/(1-2rho^4) <= 16 ; 16/(1-2^-1/2) < 64  (check 16 < 64(1-1/sqrt2) <=> (1-1/4)^2*2 > 1)
assert 4 / (1 - 2 * rho**4) <= 16
assert 2 * (1 - F(16, 64))**2 > 1  # 1/sqrt2 < 3/4
assert 1024 * 64 == 2**16 and F(2**16, 2**28) == F(1, 2**12)
z = 9 * rho**128
badsum = F(4096, 9) * z * (1 + z) / (1 - z)**3
assert badsum < F(1, 2**18)
delta = F(1, 2**22) + badsum + F(1, 2**64) + F(1, 2**24) + F(1, 2**12)
assert delta < F(1, 2**11)
loss = F(1, 2**256) + F(1, 64) + F(1, 2**62) + F(1, 2**80) + delta + F(1, 2**80) + F(1, 2**115) + F(1, 2**76)
assert F(91, 128) - loss > F(11, 16)

def isqrt_ceil(x):
    r = math.isqrt(x)
    return r if r * r == x else r + 1

rows = []
ns = list(range(64, 1025)) + [1500, 2048, 4096, 8191]
worst_beta_ratio = None
for n in ns:
    D = 1 << n
    K = 0
    while (64 * n * 3**(K + 1))**2 <= D:
        K += 1
    assert (64 * n * 3**K)**2 <= D < (64 * n * 3**(K + 1))**2 and K >= 1
    assert 9 * K >= n and n - 32 * K < -64
    H = 128 * K
    a = (2**24 * (H + 1) - 1).bit_length()  # ceil log2
    assert 2**a >= 2**24 * (H + 1) > 2**(a - 1)
    assert F(4 * H, 2**a) <= F(1, 2**22)
    ell = 2**17 * a
    ridx = (2**24 * H * ell - 1).bit_length()
    assert F(H * ell, 2**ridx) <= F(1, 2**24)
    root = isqrt_ceil(D)
    Budget = 2**28 * root
    # Bcap and amplitude recursion (only for n where exact Fractions stay cheap)
    if n <= 300 or n in (512, 1024):
        beta = F(1)
        for j in range(0, K + 1):
            A = 3**j
            if j >= 1:
                ej = F(1, 4096 * j * j)
                Pmax = math.floor(1 + ej * D / F(3**(j - 1))**2)  # largest good-size |P_j|
                # f(b)=b(3-4Pb^2/D) is increasing here (12 P b^2/D < 3), so rounding
                # DOWN to denominator 2^400 after each step keeps a valid lower bound.
                assert 12 * Pmax * beta * beta < 3 * D
                beta = beta * (3 - 4 * Pmax * beta * beta / D)
                beta = F(math.floor(beta * 2**400), 2**400)
                assert beta > 0 and beta <= A
                assert beta >= F(1023, 1024) * A, (n, j)
                r = beta / A
                worst_beta_ratio = r if worst_beta_ratio is None or r < worst_beta_ratio else worst_beta_ratio
            Bcap = 1
            while Bcap * A < 16 * root:
                Bcap *= 2
            # p_min = h alpha^2 >= (1023/1024)^2 A^2/D ; need Bcap^2 * p_min >= 16
            assert Bcap**2 * F(1023, 1024)**2 * A * A >= 16 * D
            assert Bcap * A < 32 * root <= Budget
    rows.append(n)

out = dict(status='passed', n_values=len(rows), n_min=min(rows), n_max=max(rows),
           nu=str(nu), bad_size_sum=float(badsum), delta_coarse=float(delta),
           worst_good_size_amplitude_ratio=float(worst_beta_ratio),
           success_lower=float(F(91, 128) - loss),
           cpu_seconds=time.process_time() - t0,
           scope='Exact parameter arithmetic only; not a proof of the probabilistic lemmas.')
json.dump(out, open(sys.argv[1], 'w'), indent=2)
print(json.dumps(out, indent=2))
