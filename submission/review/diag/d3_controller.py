"""D3: reviewer-written SCALED simulation of the SPTS1 Sec. 4-7 controller on an
abstract contextual comparison model (NOT DCP records, NOT production constants).

State vectors are simulated directly: V_j|0> via the operator recursion (3),
applied as explicit reflections, and t Grover iterates V_j R0 V_j^dag O_{S_r}.
Scaled constants: D=2^12, 64n -> c0=2, Cblock=5 (so K=3, Hmax=15). Same
sixteen-attempt dyadic schedule, Bcap_j A_j >= 16 root, token debit B*A_j
before each attempt, saved-pivot full champion.

Comparison model: each pivot gets a fresh uniform 'sketch' vector u (one value per
candidate). Candidate x beats pivot p iff u_x < w(x,p) with w(x,p)+w(p,x)<=1+nu_sim
(contextual, nu_sim=0.01), the true class beats any pivot w.p. 1-1e-3 and a
wrong class beats the true pivot w.p. 0.05 (so false contenders survive a true
pivot, exercising the champion). Full comparisons: true beats all; others cyclic.
Reports token use until the true class is visited vs the analytic 2^16 sqrt(D),
chi-square uniformity of accepted pivots, champion success.
"""
import json, resource, sys, time
import numpy as np
resource.setrlimit(resource.RLIMIT_CPU, (45, 45))
resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2,) * 2)
t0 = time.process_time()
rng = np.random.default_rng(91120261)
n = 12; D = 2**n; root = 2**(n // 2); c0 = 2; CB = 5
K = 0
while (c0 * 3**(K + 1))**2 <= D: K += 1
H = CB * K
A = [3**j for j in range(K + 1)]
Bcap = []
for j in range(K + 1):
    b = 1
    while b * A[j] < 16 * root: b *= 2
    Bcap.append(b)
strength = rng.normal(size=D)
NU = 0.01

def wprob(x, p, true):
    if x == true: return 1 - 1e-3
    if p == true: return 0.05
    s = 1 / (1 + np.exp(-(strength[x] - strength[p]) * 3))
    return np.clip(s + NU / 2 * np.sign(x - p), 0, 1)

def full_beats(a, b, true):  # a challenger beats champion b?
    if a == true: return True
    if b == true: return False
    return (a + b) % 3 == 0       # arbitrary cyclic relation among false classes

def R0(v):
    w = -v.copy(); w[0] = v[0]; return w

def run(true):
    S = np.ones(D, bool)
    prefixes = [S.copy()]          # P_0
    psi = [np.full(D, 1 / np.sqrt(D))]
    pivots = []; tokens = 0; visit_tokens = None; attempts_per_pivot = []
    accept_rank = []               # (index of accepted among sorted contenders, |S|)
    beta_ratio = []
    r = 0
    while r < H:
        j = r // CB
        if j >= len(psi):          # build V_j|0> from frozen prefix P_j via (3)
            Pj = S.copy(); prefixes.append(Pj)
            prev = psi[-1]
            v = np.where(Pj, -prev, prev)                       # O_{P_j} V_{j-1}|0>
            v = 2 * prev * (prev @ v) - v                       # V_{j-1} R0 V_{j-1}^dag
            psi.append(v)
            if Pj.any():
                amps = v[Pj]
                assert np.allclose(amps, amps[0])
                beta_ratio.append(float(amps[0] * np.sqrt(D) / A[j]))
        st = psi[j]
        B = 1; fails = 0; acc = None; att = 0
        if not S.any():
            break                  # exhausted (real algorithm would burn budget)
        while acc is None:
            tokens += B * A[j]; att += 1
            if rng.random() < 0.5:
                v = st
            else:
                v = st.copy()
                for _ in range(rng.integers(B)):
                    v = np.where(S, -v, v)
                    v = 2 * st * (st @ v) - v
            pr = v * v; pr /= pr.sum()
            x = rng.choice(D, p=pr)
            if S[x]:
                acc = x
            else:
                fails += 1
                if fails == 16:
                    fails = 0; B = min(2 * B, Bcap[j])
        cont = np.flatnonzero(S)
        accept_rank.append((int(np.searchsorted(cont, acc)), len(cont)))
        attempts_per_pivot.append(att)
        pivots.append(int(acc))
        if acc == true and visit_tokens is None: visit_tokens = tokens
        S[acc] = False
        u = rng.random(D)
        if acc == true:
            w = np.full(D, 0.05)
        else:
            w = 1 / (1 + np.exp(-(strength - strength[acc]) * 3))
            w = np.clip(w + NU / 2 * np.sign(np.arange(D) - acc), 0, 1)
            w[true] = 1 - 1e-3
        keep = u < w
        S &= keep
        r += 1
    champ = pivots[0] if pivots else 0
    for x in pivots[1:]:
        if full_beats(x, champ, true): champ = x
    return dict(tokens_to_visit=visit_tokens, visited=true in pivots, last_is_true=(pivots[-1] == true) if pivots else False,
                champion_ok=champ == true, accept_rank=accept_rank, beta_ratio=beta_ratio, npiv=len(pivots))

res = []
while time.process_time() - t0 < 22 and len(res) < 3000:
    res.append(run(int(rng.integers(D))))
vis = [x['tokens_to_visit'] for x in res if x['tokens_to_visit'] is not None]
# uniformity: rank/|S| should be uniform on [0,1); bucket into 10 bins
# randomized probability-integral transform: (rank+U)/|S| is exactly U[0,1) under uniform acceptance
u = np.array([(a + rng.random()) / s for x in res for a, s in x['accept_rank']])
hist = np.histogram(u, bins=10, range=(0, 1))[0]
expct = len(u) / 10
chi2 = float(((hist - expct)**2 / expct).sum())
out = dict(runs=len(res), K=K, Hmax=H, Bcap=Bcap,
           visited_fraction=sum(x['visited'] for x in res) / len(res),
           failure_reasons=dict(true_removed_or_cap=sum(not x['visited'] for x in res)),
           champion_success=sum(x['champion_ok'] for x in res) / len(res),
           last_pivot_wrong_but_champion_right=sum((not x['last_is_true']) and x['champion_ok'] for x in res),
           mean_tokens_to_visit=float(np.mean(vis)), max_tokens_to_visit=int(np.max(vis)),
           analytic_expected_bound_2_16_sqrtD=2**16 * root,
           accepted_samples=len(u), uniformity_chi2_9dof=chi2,
           min_beta_ratio=min(b for x in res for b in x['beta_ratio']) if any(x['beta_ratio'] for x in res) else None,
           cpu_seconds=time.process_time() - t0,
           scope='Scaled abstract controller; checks sampler uniformity/recursion/champion wiring only.')
json.dump(out, open(sys.argv[1], 'w'), indent=2)
print(json.dumps(out, indent=2))
