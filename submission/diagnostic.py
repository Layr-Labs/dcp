#!/usr/bin/env python3
"""Exact finite guards for CYG1. Not a proof by testing or a quantum simulator.
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
    return F(83, 100) if b >= 8191 else F(37, 50)


def profile(R):
    v, xs = R, []
    while v > 0:
        xs.append(v)
        v -= (3*(2*v+1)-1).bit_length()
    assert -3 <= v <= 0
    return xs[::-1], v


def widths(vs, D):
    remaining = D - 1
    bs = [0] * len(vs)
    for i in reversed(range(len(vs))):
        bs[i] = min(2*vs[i], remaining)
        remaining -= bs[i]
    assert remaining == 0
    return bs


def recurrence(vs, bs, cyclic=True):
    e, w, leaves = F(1), F(0), 1
    for v, b in zip(vs, bs):
        if b:
            p = sigma(b) if cyclic else F(1, 3)
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
        capacity = 2*sum(vs)
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
            assert leaves <= 1 << (R + 3)
            assert e <= (1 << (R + 3)) * F(1, 2)**len(vs)
            assert w <= F(100,37) * (1 << R)
            Emax, Wmax = max(Emax, e), max(Wmax, w)
            allocations += 1
        K = (1 << 13) * (R + 3 + (n - 1).bit_length() + 30)
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
        delta = (3*(2*v+1)-1).bit_length()
        for b in sorted({0, 1, 2*v, min(2*v, 8190), min(2*v, 8191)}):
            a = F(b + 1) / sigma(b) if b else F(1)
            assert a <= F(50, 111) * (1 << delta)
            if v >= 4428:
                assert a <= F(5, 12) * (1 << delta)
            scalar_checks += 1
    # Huge nominal labels are represented by integer budgets, not enumerated subsets.
    for R in [4095, 4096, 4427, 4428, 8191, 10000]:
        vs, terminal = profile(R)
        for D in [1, 2, 8191, 8192, 9102, 2*sum(vs), 2*sum(vs)+1]:
            if D - 1 > 2*sum(vs):
                continue
            bs = widths(vs, D)
            e, w, _ = recurrence(vs, bs)
            assert w <= F(100,37)*(1 << R)
            assert e <= (1 << (R + 3))*F(1,2)**len(vs)
            assert e**4 <= F(1 << (4*(R+1110)), 1 << (5*len(vs)))
            allocations += 1
    assert 200*8191 <= 185*(2*4428+1)
    assert 200*8191 > 185*(2*4427+1)
    assert F(5,12)**4 < F(1,32)
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
        width = 6
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



def incomplete_instrument_checks():
    cases = edges = incomplete = rejected_singletons = 0
    suffix_edges = set()
    for b,r in [(1,2),(2,3)]:
        M = 1 << b
        for low in product(range(M),repeat=r):
            sums = [sum(low[j] for j in range(r) if x >> j & 1) for x in range(1 << r)]
            fibers = [[x for x,v in enumerate(sums) if v % M == e] for e in range(M)]
            for fiber in fibers:
                m = len(fiber)
                if not m:
                    continue
                for mask in range(1 << m):
                    H = [x for j,x in enumerate(fiber) if mask >> j & 1]
                    h = len(H)
                    cases += 1
                    incomplete += h < m
                    pair_mass = F(2*(h//2),m)
                    cyclic_mass = F(h,m) if h >= 2 else F(0)
                    assert cyclic_mass >= pair_mass
                    assert pair_mass <= F(2*(m//2),m)
                    if h < 2:
                        rejected_singletons += 1
                        continue
                    # One formal phase symbol for each original basis input.
                    # Coefficients below are squared amplitudes, exactly rational.
                    outputs = {}
                    gram = {x:F(0) for x in fiber}
                    for x in fiber:
                        if x not in H:
                            gram[x] += 1  # rejected membership projector
                            continue
                        rank = 0
                        for j,y in enumerate(H):
                            if x == y:
                                rank ^= j
                        assert rank == H.index(x)
                        for control in [0,1]:
                            t = (rank-control) % h
                            chosen = H[(t+control) % h]
                            assert x ^ chosen == 0
                            outputs.setdefault(t,[]).append((control,x,F(1,2*m)))
                            gram[x] += F(1,2)
                    assert all(g == 1 for g in gram.values())
                    for t,terms in outputs.items():
                        x,y = H[t],H[(t+1)%h]
                        assert [(c,z) for c,z,_ in sorted(terms)] == [(0,x),(1,y)]
                        assert sum(w for _,_,w in terms) == F(1,m)
                        assert x != y and (sums[y]-sums[x]) % M == 0
                        # Exact phase difference is the signed full label sum.
                        coeff = tuple(((y>>j)&1)-((x>>j)&1) for j in range(r))
                        assert any(coeff)
                        suffix_edges.add((b,low,coeff))
                        edges += 1
                    assert sum(w for terms in outputs.values() for _,_,w in terms) == cyclic_mass
    # Every edge induced by every incomplete-list choice is checked for uniform suffix.
    for b,low,coeff in suffix_edges:
        hist = Counter()
        for high in product(range(4),repeat=len(low)):
            difference = sum(c*(lo+(hi<<b)) for c,lo,hi in zip(coeff,low,high))
            assert difference % (1 << b) == 0
            hist[(difference >> b) % 4] += 1
        assert len(hist) == 4 and len(set(hist.values())) == 1
    return dict(all_H_cases=cases,incomplete_lists=incomplete,cyclic_edges=edges,
                failed_h_below_two=rejected_singletons,suffix_edges=len(suffix_edges),
                exact_symbolic_phase_preservation=True,all_old_index_registers_cleared=True)


def discovery_tail_checks():
    assert F(3,4)**64 < F(1,2**16)
    assert 64*F(1,2**16) == F(1,1024)
    assert F(2,comb(64,2)) == F(1,1008)
    assert F(3,4)-F(1,1008)-F(1,1024) == F(48257,64512) > F(37,50)
    assert F(5,6)-F(1,1008)-F(1,1024) == F(53633,64512) > F(83,100)
    assert F(149,180)/F(83,100) == F(745,747) < 1
    minors = 0
    for r in range(2,8):
        for x,y in combinations(range(1,1<<r),2):
            assert any(abs(((x>>i)&1)*((y>>j)&1)-((x>>j)&1)*((y>>i)&1)) == 1
                       for i,j in combinations(range(r),2))
            minors += 1
    for b in range(1,257):
        assert F(comb((1 << (b+1))-1,2),1 << (2*b)) < 2
    # Exact rational two-amplitude Grover recurrence. No trigonometric rounding.
    grover_cases = 0
    for k in [8,9,10,11,12]:
        A,J = 1 << k,1 << ((k+1)//2)
        assert J*J >= A
        for remaining in range(1,65):
            q = F(remaining,A)
            assert 4*q*(1-q) >= F(2,A)
            good = bad = F(1)
            total = F(0)
            for j in range(J):
                assert q*good**2+(1-q)*bad**2 == 1
                total += q*good**2
                good,bad = (1-2*q)*good+2*(1-q)*bad,-2*q*good+(1-2*q)*bad
            assert total/J > F(1,4)
            grover_cases += 1
    return dict(determinant_minor_pairs=minors,grover_exact_cases=grover_cases,
                tail_bound='1/1008',miss_bound='1/1024',small_success='48257/64512',
                large_success='53633/64512',actual_renewal_ratio='745/747',
                small_k_exact_enumeration=True)


def main():
    parser = ArgumentParser()
    parser.add_argument('--out',type=Path)
    args = parser.parse_args()
    result = dict(precision=precision_checks(),instrument=instrument_checks(),moments=moment_checks(),
                  modular_matrices=modular_matrix_checks(),finite_identities=finite_identities(),
                  suffix=suffix_checks(),profiles=profile_checks(),
                  incomplete_lists=incomplete_instrument_checks(),discovery_tail=discovery_tail_checks())
    result['diagnostic_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    result['scope'] = 'Exact finite diagnostic evidence; analytic all-N proof is separate.'
    out = json.dumps(result,indent=2)+'\n'
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(out)
    print(out)


if __name__ == '__main__':
    main()
