#!/usr/bin/env python3
"""Exact finite guards for CYC1. Not a proof by testing or a quantum simulator.
Run: python3 diagnostic.py --out /path/to/results.json
All arithmetic relevant to assertions is integer or Fraction arithmetic.
"""
from argparse import ArgumentParser
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, combinations_with_replacement, product
from math import comb, factorial, isqrt
from pathlib import Path
import json


def sigma(b):
    return F(5, 6) if b >= 8191 else F(3, 4)


def profile(R):
    v, xs = R, []
    while v > 0:
        xs.append(v)
        v -= 1 + v.bit_length()
    assert v in (-1, 0)
    return xs[::-1], v


def widths(vs, D):
    remaining = D - 1
    bs = [0] * len(vs)
    for i in reversed(range(len(vs))):
        bs[i] = min(vs[i], remaining)
        remaining -= bs[i]
    assert remaining == 0
    return bs


def recurrence(vs, bs, cyclic=True):
    e, w, leaves = F(1), F(0), 1
    for v, b in zip(vs, bs):
        if b:
            p = sigma(b) if cyclic else F(1, 2)
            e = (b + 1) * e / p
            w = ((b + 1) * w + (1 << v)) / p
            leaves *= b + 1
    return e, w, leaves


def ceil_fraction(x):
    return -(-x.numerator // x.denominator)


def profile_checks():
    # Derive minimizers without assuming S(R) is monotone.
    maximum_n = 8192
    minima, highest = {}, 0
    for R in range(1, maximum_n + 1):
        vs, terminal = profile(R)
        capacity = sum(vs)
        for n in range(highest + 1, min(capacity, maximum_n) + 1):
            minima[n] = R
        highest = max(highest, min(capacity, maximum_n))
        if highest == maximum_n:
            break
    assert len(minima) == maximum_n
    allocations = caps_count = 0
    rows = []
    for n in [256, 257, 511, 1024]:
        R = minima[n]
        vs, terminal = profile(R)
        Emax, Wmax = F(1), F(0)
        for D in range(1, n + 1):
            bs = widths(vs, D)
            e, w, leaves = recurrence(vs, bs)
            old_e, old_w, _ = recurrence(vs, bs, False)
            assert e <= old_e and w <= old_w
            assert leaves <= 1 << (R + 1)
            assert e <= (1 << (R + 1)) * F(2, 3)**len(vs)
            assert w <= 4 * (1 << R)
            Emax, Wmax = max(Emax, e), max(Wmax, w)
            allocations += 1
        K = (1 << 13) * (R + 1 + (n - 1).bit_length() + 30)
        H0 = n * K + 2*n
        qstar, wstar = 2*Emax*H0 + 2*n, Wmax*H0
        qcap, wcap = ceil_fraction(1024*qstar), ceil_fraction(1024*wstar)
        assert F(qstar, qcap) <= F(1, 1024)
        assert F(wstar, wcap) <= F(1, 1024)
        rows.append(dict(n=n, R=R, depth=len(vs), Qcap_bits=qcap.bit_length(),
                         Wcap_bits=wcap.bit_length(), Emax=str(Emax), Wmax=str(Wmax)))
        caps_count += 1
    # Exact pointwise certificate for all thresholds and representative partial widths.
    scalar_checks = 0
    for v in range(1, 20001):
        delta = 1 + v.bit_length()
        for b in sorted({0, 1, v, min(v, 8190), min(v, 8191)}):
            a = F(b + 1) / sigma(b) if b else F(1)
            assert a <= F(2, 3) * (1 << delta)
            if v >= 9101:
                assert a <= F(3, 5) * (1 << delta)
            scalar_checks += 1
    # Huge nominal labels are represented by integer budgets, not enumerated subsets.
    for R in [8190, 8191, 9100, 9101, 10000, 16384]:
        vs, terminal = profile(R)
        for D in [1, 2, 8191, 8192, 9102, sum(vs), sum(vs)+1]:
            if D - 1 > sum(vs):
                continue
            bs = widths(vs, D)
            e, w, _ = recurrence(vs, bs)
            assert w <= 4*(1 << R)
            assert e <= (1 << (R + 1))*F(2,3)**len(vs)
            allocations += 1
    return dict(minimal_profiles=len(minima), all_D_allocations=allocations,
                scalar_partial_width_checks=scalar_checks, exact_cap_sets=caps_count, rows=rows)


def fiber_hist(labels, M):
    h = [0] * M
    h[0] = 1
    for a in labels:
        h = [h[e]+h[(e-a) % M] for e in range(M)]
    return h


def instrument_checks():
    cases = edges = 0
    for m in range(2, 65):
        width = m.bit_length()
        domain = 1 << width
        image = set()
        # Encoding extension, postmeasurement supports and clearing the old subset.
        for j in range(domain):
            for c in range(2):
                t = (j-c) % m if j < m else j
                image.add((t,c))
        assert len(image) == 2*domain
        fiber = [3*j+1 for j in range(m)]
        for t in range(m):
            branches = [(j,c) for j in range(m) for c in range(2) if (j-c) % m == t]
            assert set(branches) == {(t,0),((t+1) % m,1)}
            for j,c in branches:
                selected = fiber[t if c == 0 else (t+1) % m]
                assert fiber[j] ^ selected == 0
            assert sum(F(1, 2*m) for _ in branches) == F(1,m)
            edges += 1
        # Kraus Gram sum is diagonal: output basis indices c differ on each edge.
        gram = [[F(0) for _ in range(m)] for _ in range(m)]
        for t in range(m):
            gram[t][t] += F(1,2)
            gram[(t+1) % m][(t+1) % m] += F(1,2)
        assert all(gram[i][j] == int(i == j) for i in range(m) for j in range(m))
        cases += 1
    return dict(fiber_sizes=cases, cyclic_edges=edges, identity_extension=True,
                cleanup=True, kraus_completeness=True)


def moment_checks():
    coeffs = []
    for k in range(1,8):
        full = F(((1 << k)-1)*(factorial(k)+1)*(1 << (k-1)),factorial(k))
        reference = F(k*(k+1)*(1 << (k-1)),2*factorial(k))
        deficient = sum(F(2*(1 << (k*d))*factorial(d)*(1 << d),factorial(k))
                        for d in range(1,k))
        assert full+reference < 1 << 28
        assert deficient < 1 << 70
        coeffs.append(dict(k=k,full_and_reference=str(full+reference),
                           deficient_including_reference=str(deficient)))
    error = F(1 << 28,1 << 8191)+(1 << 70)*F(63,64)**8192
    assert error < F(1,1 << 50)
    cycle = sum(F((-2)**j, factorial(j)) for j in range(7))
    pair = sum(F((-2)**j,factorial(j)) for j in range(8))
    pair += sum((-1)**(j-2)*comb(j,2)*F(2**j,3*factorial(j)) for j in range(2,8))
    assert cycle == F(7,45) and pair == F(11,63)
    assert cycle+7*error < F(1,6)
    assert pair-F(80,3)*error > F(31,180)
    # Exact pointwise Bonferroni polynomials; a proof for all integers is in proof.md.
    for z in range(257):
        upper = sum((-1)**j*comb(z,j) for j in range(min(z,6)+1))
        lower = sum((-1)**j*comb(z,j) for j in range(min(z,7)+1))
        lower2 = sum((-1)**(j-2)*comb(j,2)*comb(z,j) for j in range(2,min(z,7)+1))
        assert lower <= int(z==0) <= upper
        assert lower2 <= int(z==2)
    return dict(coefficients=coeffs, threshold_b=8191,error_below='2^-50',
                cycle_success_lower='5/6',pair_success_upper='149/180')


def rank(rows, r, mod2=False):
    mat = [[F((x >> j)&1) for j in range(r)] for x in rows]
    k, pivot = len(mat), 0
    for j in range(r):
        pos = next((i for i in range(pivot,k) if mat[i][j] != 0),None)
        if pos is None:
            continue
        mat[pivot],mat[pos] = mat[pos],mat[pivot]
        factor = mat[pivot][j]
        mat[pivot] = [x/factor for x in mat[pivot]]
        for i in range(k):
            if i != pivot and mat[i][j]:
                factor = mat[i][j]
                mat[i] = [a-factor*b for a,b in zip(mat[i],mat[pivot])]
                if mod2:
                    mat[i] = [F(x.numerator % 2) for x in mat[i]]
        pivot += 1
        if pivot == k:
            break
    return pivot


def modular_matrix_checks():
    counts = Counter()
    # All distinct nonzero row sets at r=3, k<=3, M=4 and 8. Includes even minors.
    for M in [4,8]:
        r = 3
        vectors = list(product(range(M),repeat=r))
        for k in range(1,4):
            for rows in combinations(range(1,1 << r),k):
                d, d2 = rank(rows,r), rank(rows,r,True)
                zeros = sum(all(sum(a[j] for j in range(r) if row >> j & 1) % M == 0
                                for row in rows) for a in vectors)
                probability = F(zeros,M**r)
                assert probability <= F(factorial(d),M**d)
                if d2 == k:
                    assert probability == F(1,M**k)
                counts[f'rankQ={d},rankF2={d2}'] += 1
    assert any('rankQ=3,rankF2=2' == key for key in counts)
    return dict(matrices=sum(counts.values()), classes=dict(counts))


def finite_identities():
    masks = planted_cases = 0
    means = []
    for b,r in [(1,2),(2,3),(3,4)]:
        M, K = 1 << b, 1 << r
        planted, measured = Counter(),Counter()
        pair_sum,cycle_sum = F(0),F(0)
        for labels in product(range(M),repeat=r):
            h = fiber_hist(labels,M)
            planted[h[0]-1] += 1
            for c in h:
                if c:
                    measured[c-1] += c
            pair_sum += F(sum(c % 2 for c in h),K)
            cycle_sum += F(sum(c == 1 for c in h),K)
            assert sum(c==1 for c in h) <= sum(c%2 for c in h)
            planted_cases += 1
        assert all(planted[z]*K == measured[z] for z in set(planted)|set(measured))
        assert F(sum(z*c for z,c in planted.items()),M**r) == F(K-1,M)
        assert F(sum(comb(z,2)*c for z,c in planted.items()),M**r) == F(comb(K-1,2),M**2)
        pair_mean,cycle_mean = pair_sum/M**r,cycle_sum/M**r
        assert cycle_mean <= pair_mean <= F(1,4)
        means.append(dict(b=b,r=r,pair_failure=str(pair_mean),cycle_failure=str(cycle_mean)))
    for M in [2,4,8]:
        mask = (1 << M)-1
        def rotate(x,a):
            return ((x << a)|(x >> (M-a))) & mask
        for r in range(5):
            for labels in combinations_with_replacement(range(M),r):
                h = fiber_hist(labels,M)
                A = sum(1 << e for e,c in enumerate(h) if c)
                S = sum(1 << e for e,c in enumerate(h) if c == 1)
                P = sum(1 << e for e,c in enumerate(h) if c % 2)
                s,u = S.bit_count(),A.bit_count()
                singleton_total = 0
                for a in range(M):
                    hh = fiber_hist(labels+(a,),M)
                    aa = A|rotate(A,a)
                    ss = (S & ~rotate(A,a))|(rotate(S,a) & ~A)
                    pp = P^rotate(P,a)
                    assert aa == sum(1 << e for e,c in enumerate(hh) if c)
                    assert ss == sum(1 << e for e,c in enumerate(hh) if c == 1)
                    assert pp == sum(1 << e for e,c in enumerate(hh) if c % 2)
                    singleton_total += ss.bit_count()
                    masks += 1
                assert singleton_total == 2*s*(M-u)
    return dict(planted_label_assignments=planted_cases,mask_transitions=masks,means=means)


def suffix_checks():
    count = 0
    for p in [1,2]:
        r = 3
        for low in product(range(1 << p),repeat=r):
            fibers = [[] for _ in range(1 << p)]
            for x in range(1 << r):
                fibers[sum(low[j] for j in range(r) if x >> j & 1) % (1 << p)].append(x)
            for fiber in fibers:
                if len(fiber) < 2:
                    continue
                for t,x in enumerate(fiber):
                    y = fiber[(t+1) % len(fiber)]
                    coeff = [((y >> j)&1)-((x >> j)&1) for j in range(r)]
                    assert any(coeff)
                    hist = [0]*4
                    for high in product(range(4),repeat=r):
                        lab = sum(c*(lo+(h << p)) for c,lo,h in zip(coeff,low,high))
                        assert lab % (1 << p) == 0
                        hist[(lab >> p) % 4] += 1
                    assert len(set(hist)) == 1
                    count += 1
    canonical,sorted_full = F(0),F(0)
    for a,b in product(range(2),repeat=2):
        sums = [0,a,b,a+b]
        for order,which in [(list(range(4)),0),(sorted(range(4),key=lambda i:(sums[i],i)),1)]:
            odd = F(sum((sums[order[(j+1)%4]]-sums[order[j]]) % 2 for j in range(4)),16)
            if which:
                sorted_full += odd
            else:
                canonical += odd
    assert canonical == F(1,2) and sorted_full == F(3,8)
    return dict(suffix_cases=count,canonical_odd=str(canonical),full_sorted_odd=str(sorted_full))


def precision_checks():
    assert F(7**81,factorial(81)) < F(1,2**170)
    assert F(16,81*5**81)+F(4,81*239**81) < F(1,2**91)
    assert F(44,7*4096)+F(1,2**20) < F(1,625)
    assert 1-F(22,7*128)**2/2 > F(511,512)
    assert F(99,70)**2 > 2
    assert (2+F(99,70))/4 < F(37,40)**2
    assert (F(511,512)-F(37,40))/2 > F(2,64)+F(2,625)
    return dict(exact_rational_guards=7, extraction_and_decoder_constants=True)


def main():
    parser = ArgumentParser()
    parser.add_argument('--out',type=Path)
    args = parser.parse_args()
    result = dict(precision=precision_checks(),instrument=instrument_checks(),moments=moment_checks(),
                  modular_matrices=modular_matrix_checks(),finite_identities=finite_identities(),
                  suffix=suffix_checks(),profiles=profile_checks())
    result['diagnostic_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    result['scope'] = 'Exact finite diagnostic evidence; analytic all-N proof is separate.'
    out = json.dumps(result,indent=2)+'\n'
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(out)
    print(out)


if __name__ == '__main__':
    main()
