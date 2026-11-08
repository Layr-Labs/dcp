"""Reviewer's independent diagnostics for PROOF.md (filtered search).

Standard library only.  Written from the formulas in PROOF.md and
sources/ROB-G2-proof.md, without importing or copying the parent's check.py.
Each process is capped at 45 CPU seconds and 512 MiB.

Parts
  A  exact ROB-G2 gap constants (pi < 22/7) and exact table range at extremes
  B  exact integer schedule premises for every n in [20, 20000]
  C  multiset accumulator / comparator width for the filter list
  D  reduced-space (3-dim) high-precision simulation of the ACTUAL operator
     word (V, V R_0 V^dagger = 2|psi><psi|-I, O_v, O_f) using matrix powers,
     for every n in [20, 160] and a grid of retained-set sizes h in [1, G/64]
  E  L versus Q crossover (constants only)
"""
from fractions import Fraction as F
from decimal import Decimal, getcontext
from math import isqrt
import json, resource, sys, time
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (45, 45))
resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))
t0 = time.process_time()
out = {}

def clog2(x):
    return (x - 1).bit_length()

# ---------- A: gap constants straight from ROB-G2 Section 4.1 / 6 ----------
pi_up = F(22, 7)
tau = F(1, 2**24)
q_bits = 24
eta = 3 * pi_up / 2**q_bits + tau           # ROB-G2: eta = 3 pi 2^-q + tau
R = 1 + tau
pF = F(1, 10**8)
kappa = 2 * R * pF + eta
eps, delta, theta = F(3333, 10000), F(1, 50000), F(6667, 40000)
Lo = (1 - eps) * (F(1, 2) - kappa) - eps * (F(1, 2) + eta) - delta
Hi = kappa + eps * (F(1, 2) + eta) + delta
gamma = F(1, 250000)
assert Lo - theta == F(256318304059827, 58720256000000000000) or Lo - theta > F(256318304059827, 58720256000000000000)
assert theta - Hi >= F(24376142481, 5872025600000000)
assert Lo - theta > gamma and theta - Hi > gamma
out['A_gap'] = dict(Lo_minus_theta=str(Lo - theta), theta_minus_Hi=str(theta - Hi),
                    Lo_minus_theta_float=float(Lo - theta), theta_minus_Hi_float=float(theta - Hi),
                    gamma=str(gamma),
                    slack_over_gamma=[float((Lo - theta) / gamma), float((theta - Hi) / gamma)])
# monotonicity: Lo decreasing, Hi increasing in pi (via eta) -> pi upper bound is the safe side
eta2 = 3 * F(3, 1) / 2**q_bits + tau
kappa2 = 2 * R * pF + eta2
assert (1 - eps) * (F(1, 2) - kappa2) - eps * (F(1, 2) + eta2) - delta > Lo

# Table range: |c_k| <= 2^25 means table[k] = c_k/2^25 in [-1,1] (sharper than Lemma B's R).
pit = F(103993, 33102)
def c_k(k):
    x = 2 * pit * k / 2**q_bits
    P, term = F(0), F(1)
    for i in range(21):
        if i:
            term = term * (-x * x) / ((2 * i - 1) * (2 * i))
        P += term
    z = 2**25 * P
    return (z + F(1, 2)).__floor__()
ext = {k: c_k(k) for k in (0, 1, 2**22, 2**23 - 1, 2**23, 2**23 + 1, 2**24 - 1)}
assert all(abs(v) <= 2**25 for v in ext.values())
out['A_table_extremes'] = {str(k): v for k, v in ext.items()}

# ---------- B: exact integer schedule premises ----------
def params(n):
    d = clog2(n + 2); a = 4 * d + 8
    b = max(12, n - a + 12)
    k = (isqrt(1 << (n - b)) - 1) // 2
    j = 3 * isqrt(1 << b) // 4
    return d, a, b, k, j

worst = dict(lower=F(10), upper=F(0))
for n in range(20, 20001):
    d, a, b, k, j = params(n)
    D, G = 1 << n, 1 << b
    m = n - b
    assert 8 <= m and b <= n and G >= 4096 and G % 64 == 0
    assert 2**(4 * d) >= (n + 2)**4
    q = 2 * k + 1
    assert q * q * G <= D                       # q <= x
    assert (q + 2)**2 * G >= D                  # q >= x - 2
    assert 64 * q * q * G >= 49 * D             # q/sqrt(D) >= (7/8)/sqrt(G)
    assert D <= (G // 4096) * (1 << a)          # D 2^-a <= G/4096
    J = 2 * j + 1
    assert 4 * J * J <= (3 * isqrt(G) + 2)**2 <= 9 * G + 12 * isqrt(G) + 4  # J <= 3sqrtG/2 + 1
    assert (2 * J + 5)**2 >= 9 * G               # J >= 3sqrtG/2 - 5/2
    assert k >= 7 and j >= 48
out['B_schedule_cases'] = 20000 - 20 + 1

# uniform rational chain (re-derived)
assert F(256, 16383) < F(1, 63)
lo_angle = (F(3, 2) - F(5, 128)) * F(7, 8) * (1 - F(1, 6 * 63))
hi_angle = (F(3, 2) + F(1, 64)) * F(64, 63) * F(129, 128)
assert lo_angle == F(70499, 55296) and hi_angle == F(4171, 2688)
assert F(129, 128)**2 * F(16383, 16384) >= 1
x = F(5, 4)
s5 = x - x**3/6 + x**5/120 - x**7/5040
assert s5**2 > F(7, 8) and hi_angle < F(25, 16) and F(25, 16) <= F(25, 8) / 2  # and pi > 25/8 strictly
total = F(7, 8) * F(127, 128) * (F(31, 32) - F(1, 2**16)) * F(7, 8)
assert total == F(395079601, 536870912) and total > F(2, 3)
# with the true a>=28 for n>=20, the third factor is 31/32-2^-28 (parent's 2^-16 is just weaker)
out['B_uniform_chain'] = dict(angle=[str(lo_angle), str(hi_angle)], sin2_lower=float(s5**2),
                              total=str(total), total_float=float(total))

# ---------- C: multiset accumulator width ----------
for n in list(range(20, 2000)) + [10**4, 10**6]:
    d, a, *_ = params(n)
    L = 125000000000 * a
    w = L.bit_length() + 29
    assert L * (2**26 + 1) < 2**(w - 1)
    # comparator constant Theta_f + 1, |C*| <= L(6667 2^25 + 40000(2^25+1))
    Cstar = L * (6667 * 2**25 + 40000 * (2**25 + 1))
    assert Cstar // 40000 + 2 < 2**(w - 1)
    Q = 2**33 * (n + 4)
    r = clog2(128 * L)
    assert L * F(1, 2**r) <= F(1, 128)
    assert 2 * Q > (1 << clog2(Q))              # each trial succeeds w.p. > 1/2
out['C_width_ok'] = True

# ---------- D: reduced-space simulation of the actual operator word ----------
def simulate(n, h, prec):
    getcontext().prec = prec
    d, a, b, k, j = params(n)
    D = Decimal(2) ** n
    one, two = Decimal(1), Decimal(2)
    # basis: e0=|s>, e1=uniform over the other h-1 filter-marked, e2=uniform over D-h unmarked
    u = [one / D.sqrt(), (Decimal(h - 1) / D).sqrt(), (Decimal(D - h) / D).sqrt()]
    def mat_mul(A, B):
        return [[sum(A[i][t] * B[t][c] for t in range(3)) for c in range(3)] for i in range(3)]
    def refl(v):   # 2|v><v| - I
        return [[two * v[i] * v[c] - (one if i == c else 0) for c in range(3)] for i in range(3)]
    def power(M, e):
        Rm = [[one if i == c else Decimal(0) for c in range(3)] for i in range(3)]
        while e:
            if e & 1: Rm = mat_mul(Rm, M)
            M = mat_mul(M, M); e >>= 1
        return Rm
    Of = [[-one, 0, 0], [0, -one, 0], [0, 0, one]]
    Ov = [[-one, 0, 0], [0, one, 0], [0, 0, one]]
    step = mat_mul(refl(u), Of)                       # R_u O_f
    Vk = power(step, k)                               # (R_u O_f)^k
    psi = [sum(Vk[i][t] * u[t] for t in range(3)) for i in range(3)]   # V|0>
    W = mat_mul(refl(psi), Ov)                        # V R_0 V^dag O_v
    Wj = power(W, j)
    fin = [sum(Wj[i][t] * psi[t] for t in range(3)) for i in range(3)]
    norm = sum(v * v for v in fin)
    return float(fin[0] * fin[0]), float(abs(norm - 1)), float(psi[0])

worst_sim, cases, maxnormerr = 1.0, 0, 0.0
per_n = {}
for n in range(20, 161):
    d, a, b, k, j = params(n)
    G = 1 << b
    hs = sorted({1, 2, 3, G // 64, G // 128, G // 64 - 1} |
                {max(1, (G // 64) >> s) for s in range(0, b, max(1, b // 8))})
    prec = n // 3 + 60
    mn = 1.0
    for h in hs:
        p, ne, _ = simulate(n, h, prec)
        mn = min(mn, p); maxnormerr = max(maxnormerr, ne); cases += 1
    per_n[n] = mn
    worst_sim = min(worst_sim, mn)
    if time.process_time() - t0 > 38:
        break
out['D_reduced_space'] = dict(n_range=[20, max(per_n)], cases=cases,
                              min_success=worst_sim, max_norm_error=maxnormerr,
                              min_success_by_n_sample={str(k): per_n[k] for k in list(per_n)[::10]})
assert worst_sim > 7 / 8

# ---------- E: L vs Q ----------
cross = next(n for n in range(20, 10**5) if 125000000000 * params(n)[1] < 2**33 * (n + 4))
out['E_first_n_with_L_lt_Q'] = cross
out['cpu_seconds'] = time.process_time() - t0
Path(__file__).with_name('independent_results.json').write_text(json.dumps(out, indent=1) + '\n')
print(json.dumps(out, indent=1))
