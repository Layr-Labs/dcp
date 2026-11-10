#!/usr/bin/env python3
"""Finite exact diagnostics; not a DCP solver or a proof of asymptotic claims."""
from fractions import Fraction as F
from itertools import combinations, product
import json
from pathlib import Path


def tournaments(h):
    edges = list(combinations(range(h), 2))
    for mask in range(1 << len(edges)):
        yield tuple(((mask >> i) & 1) for i in range(len(edges)))


def wins(t, h, x, y):
    if x == y:
        return False
    edges = list(combinations(range(h), 2))
    a, b = sorted((x, y))
    return bool(t[edges.index((a, b))]) == (x == a)


def run():
    counts = {}
    for h in range(1, 6):
        ts = list(tournaments(h))
        for t in ts:
            total = sum(wins(t, h, x, p) for p in range(h) for x in range(h))
            assert F(total, h) == F(h - 1, 2)
        counts[str(h)] = len(ts)
    seed_pairs = 0
    for h in range(2, 5):
        ts = list(tournaments(h))
        for a, b in product(ts, repeat=2):
            total = sum(wins(t, h, x, p) for t in (a, b) for p in range(h) for x in range(h))
            assert F(total, 2*h) == F(h-1, 2)
            seed_pairs += 1
    # For each pivot choose a tournament in which everyone beats it.
    h = 3
    dependent = []
    for p in range(h):
        dependent.append(next(t for t in tournaments(h) if sum(wins(t,h,x,p) for x in range(h)) == h-1))
    dependent_mean = F(sum(wins(dependent[p],h,x,p) for p in range(h) for x in range(h)), h)
    assert dependent_mean == 2 > F(h-1,2)

    # Full order 0 > 1 > 2. Sketch after pivot 0 erroneously accepts 1.
    full = lambda x,y: x < y
    visited = [0, 1]
    sketch_accepts = lambda candidate,pivot: (candidate,pivot) == (1,0)
    assert all(full(0,x) for x in (1,2)) and sketch_accepts(1,0)
    champion = visited[0]
    for x in visited[1:]:
        champion = champion if full(champion,x) else x
    assert visited[-1] != 0 and champion == 0

    vectors = 0
    sampler_cases = 0
    for D in (4,16,64):
        n = D.bit_length()-1
        zero = [F(int(i == 0)) for i in range(D)]
        def had(v):
            out = v[:]
            # n even, each one-qubit H contributes 1/sqrt(2); pair transforms.
            for bit in range(0,n,2):
                for base in range(D):
                    if base & (3 << bit): continue
                    ids = [base | (k << bit) for k in range(4)]
                    vals = [out[i] for i in ids]
                    for a,idx in enumerate(ids):
                        out[idx] = sum(((-1)**((a & b).bit_count()) * vals[b] for b in range(4)), F()) / 2
            return out
        def r0(v): return [v[0]] + [-x for x in v[1:]]
        def oracle(v,S): return [-x if i in S else x for i,x in enumerate(v)]
        # Nested but uneven reductions, and an empty set, all j <= 3.
        sequences = [[set(range(D)),set(range(D//2)),set(range(D//4))],
                     [set(range(D//2)),set(range(D//4)),set()],
                     [set(range(1,D)),set(range(1,D//2)),{1}]]
        for sets in sequences:
            def apply(j,v,inv=False):
                if j == 0: return had(v)
                S=sets[j-1]
                if not inv:
                    v=apply(j-1,v); v=oracle(v,S); v=apply(j-1,v,True); v=r0(v); return apply(j-1,v)
                v=apply(j-1,v,True); v=r0(v); v=apply(j-1,v); v=oracle(v,S); return apply(j-1,v,True)
            alpha=F(1,2**(n//2))
            for j,S in enumerate(sets,1):
                alpha = alpha*(3-4*len(S)*alpha*alpha)
                v=apply(j,zero)
                assert all(v[i] == alpha for i in S)
                assert sum(x*x for x in v) == 1
                assert apply(j,v,True) == zero
                vectors += 1
                subset=set(sorted(S)[::2])
                if subset:
                    # Grover step: oracle then reflection about V_j|0>.
                    state=v
                    mixture = [F() for _ in range(D)]
                    for clock in range(4):
                        for i in range(D):
                            mixture[i] += state[i]**2 / 4
                        probs=[state[i]**2 for i in subset]
                        assert len(set(probs)) == 1
                        sampler_cases += 1
                        state=oracle(state,subset)
                        state=apply(j,state,True); state=r0(state); state=apply(j,state)
                    mixed = [(v[i]**2 + mixture[i])/2 for i in subset]
                    assert len(set(mixed)) == 1
            # Mixed direct and random-clock probabilities are equal termwise.
        # Violate nesting: second set contains marked and unmarked amplitudes.
        sets=[set(range(D//2)), {0,D-1}]
        def nonnested(j,v,inv=False):
            if j == 0: return had(v)
            if not inv:
                return nonnested(j-1,r0(nonnested(j-1,oracle(nonnested(j-1,v),sets[j-1]),True)))
            return nonnested(j-1,oracle(nonnested(j-1,r0(nonnested(j-1,v,True))),sets[j-1]),True)
        v=nonnested(2,zero)
        assert v[0] != v[-1]
    assert 2*F(3,4)**4 < F(3,4)
    assert F(7,8)**16 < F(1,4)
    return {'tournaments_by_vertices':counts,'independent_seed_pairs':seed_pairs,
            'dependent_seed_mean':str(dependent_mean),'dependent_seed_bound':str(F(h-1,2)),
            'full_winner':0,'visited_pivots':visited,'last_pivot':visited[-1],'full_tournament_champion':champion,
            'nested_vector_cases':vectors,'sampler_clock_cases':sampler_cases,'non_nested_negative_cases':3,
            'geometric':{'2_rho_pow_4':str(2*F(3,4)**4),'three_quarters':str(F(3,4)),
                         'tail_16':str(F(7,8)**16),'quarter':str(F(1,4))},'status':'passed'}

if __name__ == '__main__':
    result=run()
    out=json.dumps(result,indent=2,sort_keys=True)+'\n'
    Path(__file__).with_name('results.json').write_text(out)
    print(out,end='')
