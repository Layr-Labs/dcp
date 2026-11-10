"""D2: reviewer-written replica of RQ-SPLIT Section 6 phase-word/score arithmetic
used by SPTS1 sketches. Exact integers; the cosine grid uses double-precision
cos rounded to 2^-30 (table VALUES are irrelevant to the structural checks).

Checks on random (N, W, records, classes, sketches):
 (a) fresh window word a_W(t) within one circular cell of exact T_W(t);
 (b) exact antisymmetry G(t,u) = -G(u,t) when each member keeps its word
     (justifies 'negative transpose' in SPTS1 Sec. 8);
 (c) per-record fresh/exact role discrepancy <= eps_role = 51*2^-26;
 (d) canonical class comparison via the candidate matrix M and its negative
     transpose equals the direct definition F=max min;
 (e) pair count over the full 2^16 threshold grid with a SHARED sketch:
     #(x wins as candidate vs pivot p) + #(p wins as candidate vs x) <= 2^16+7.
"""
import json, math, random, resource, sys, time
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_CPU, (45, 45))
resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2,) * 2)
t0 = time.process_time()
q, RPHI, BCOS = 14, 26, 30
C = [round(math.cos(2 * math.pi * v / 2**q) * 2**BCOS) for v in range(2**q)]
C = [max(-2**BCOS, min(2**BCOS, c)) for c in C]
SH = RPHI - q
DEN = 10 * 2**(BCOS + SH)            # = Zden = 10*2^42
assert DEN == 10 * 2**42

def interp(x):                       # numerator over 2^(BCOS+SH)
    x %= 2**RPHI
    h, z = x >> SH, x & (2**SH - 1)
    return C[h] * (2**SH - z) + C[(h + 1) % 2**q] * z

def cs(beta, x):
    return interp(x) if beta == 0 else interp(x - 2**(RPHI - 2))

def fresh_word(W, t, N, n, p):
    E = (2**(n + p) * W) // N
    V = 0
    for ell in range(n):
        if (t >> ell) & 1:
            V = (V + (E >> (n - ell)) % 2**p) % 2**p
    return V >> (p - RPHI)

def exact_word(W, t, N):
    return (2**RPHI * ((W * t) % N)) // N

def score(rec, at, au):                # numerator over DEN; members' words at, au
    W, beta, Z = rec
    M = 2**RPHI
    v = 11 * (cs(beta, at) - cs(beta, au)) + cs(beta, (2 * at - au) % M) - cs(beta, (2 * au - at) % M)
    return Z * v

def words(rec, rep, N, n, p, fresh):
    W = rec[0]
    w = fresh_word(W, rep, N, n, p) if fresh else exact_word(W, rep, N)
    ws = [w]
    if N % 2 == 0:
        ws.append((w + 2**(RPHI - 1) * (W % 2)) % 2**RPHI)   # member rep+N/2
    return ws

def matrix(sketch, recs, xrep, xfresh, yrep, N, n, p):
    """mean-score numerators (times len) of x-members vs y-members; x fresh iff xfresh, y the other role."""
    nx = 2 if N % 2 == 0 else 1
    M = [[0] * nx for _ in range(nx)]
    for i in sketch:
        r = recs[i]
        wx = words(r, xrep, N, n, p, xfresh)
        wy = words(r, yrep, N, n, p, not xfresh)
        for a in range(nx):
            for b in range(nx):
                M[a][b] += score(r, wx[a], wy[b])
    return M

def Fval(Mfirst):  # max over first-members of min over second-members
    return max(min(row) for row in Mfirst)

def cand_wins(sketch, recs, cand, piv, tau_num, N, n, p):
    """Candidate fresh, pivot exact; canonical first = smaller rep. tau_num = tau*len*DEN."""
    M = matrix(sketch, recs, cand, True, piv, N, n, p)       # cand rows, pivot cols
    if cand < piv:
        return Fval(M) >= tau_num
    MT = [[-M[a][b] for a in range(len(M))] for b in range(len(M))]  # pivot rows (negative transpose)
    return not (Fval(MT) >= tau_num)

rng = random.Random(20261109)
stats = dict(word_checks=0, antisym=0, role_records=0, max_role_disc=0, transpose_checks=0, pair_checks=0, max_pair_excess=0)
EPS_NUM = F(51, 2**26) * DEN
for trial in range(14):
    n = rng.randint(4, 12)
    N = rng.randint(2**(n - 1) + 1, 2**n)
    p = RPHI + 4 + max(1, math.ceil(math.log2(n)))
    recs = [(rng.randrange(N), rng.randrange(2), rng.choice((1, -1))) for _ in range(48)]
    reps = range(N // 2) if N % 2 == 0 else range(N)
    for _ in range(40):
        rec = recs[rng.randrange(len(recs))]
        t = rng.randrange(N)
        a, T = fresh_word(rec[0], t, N, n, p), exact_word(rec[0], t, N)
        d = (a - T) % 2**RPHI
        assert min(d, 2**RPHI - d) <= 1
        stats['word_checks'] += 1
        t2, u2 = rng.randrange(2**RPHI), rng.randrange(2**RPHI)
        assert score(rec, t2, u2) == -score(rec, u2, t2)
        stats['antisym'] += 1
    for _ in range(3):
        x, y = rng.sample(list(reps), 2)
        sketch = [rng.randrange(len(recs)) for _ in range(24)]
        for i in set(sketch):   # per-record role discrepancy
            Ma = matrix([i], recs, x, True, y, N, n, p)
            Mb = matrix([i], recs, x, False, y, N, n, p)
            dmax = max(abs(Ma[a][b] - Mb[a][b]) for a in range(len(Ma)) for b in range(len(Ma)))
            assert dmax <= EPS_NUM, dmax
            stats['max_role_disc'] = max(stats['max_role_disc'], float(F(dmax, DEN) / F(51, 2**26)))
            stats['role_records'] += 1
        # (d) transpose route equals direct definition with the pivot first
        M = matrix(sketch, recs, x, True, y, N, n, p)
        Mpiv = matrix(sketch, recs, y, False, x, N, n, p)    # pivot y exact rows, cand x fresh cols
        MT = [[-M[a][b] for a in range(len(M))] for b in range(len(M))]
        assert MT == Mpiv
        stats['transpose_checks'] += 1
        # (e) pair count over all 2^16 thresholds with shared sketch
        L = len(sketch)
        def count(cand, piv):
            M = matrix(sketch, recs, cand, True, piv, N, n, p)
            if cand < piv:
                f = Fval(M)
            else:
                f = Fval([[-M[a][b] for a in range(len(M))] for b in range(len(M))])
            c = 0
            # tau_num(J) = (-2^15 + J) * 2^-23 * L * DEN; DEN*2^-23 = 10*2^19 integer
            step = L * 10 * 2**19
            for J in range(2**16):
                first_wins = f >= (J - 2**15) * step
                c += first_wins if cand < piv else (not first_wins)
            return c
        tot = count(x, y) + count(y, x)
        assert tot <= 2**16 + 7, tot
        stats['max_pair_excess'] = max(stats['max_pair_excess'], tot - 2**16)
        stats['pair_checks'] += 1
stats.update(status='passed', cpu_seconds=time.process_time() - t0,
             scope='Random finite replicas of the Sec. 6 arithmetic; structural, not a proof.')
json.dump(stats, open(sys.argv[1], 'w'), indent=2)
print(json.dumps(stats, indent=2))
