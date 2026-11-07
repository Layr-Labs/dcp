#!/usr/bin/env python3
"""Score recovered-state schedules from the saved exact census, without a GPU."""
from fractions import Fraction as F
from functools import cache
from hashlib import sha256
from pathlib import Path
import json
import resource

HERE = Path(__file__).resolve().parent


def pack(x):
    return dict(numerator_hex=hex(x.numerator), denominator_hex=hex(x.denominator),
                display=float(x))


def unpack(x):
    return F(int(x['numerator_hex'], 16), int(x['denominator_hex'], 16))


@cache
def probability(A, marked, J):
    g = h = F(1)
    total = F(0)
    for _ in range(J):
        total += F(marked, A) * g * g
        g, h = ((1 - F(2*marked, A))*g + F(2*(A-marked), A)*h,
                -F(2*marked, A)*g + (1 - F(2*marked, A))*h)
    return total / J


@cache
def schedule(A, m, early, terminal):
    last = (A.bit_length() - 1 + 1) // 2
    reach = F(1)
    predicates = preparations = F(0)
    for ell in range(last + 1):
        J = 1 << ell
        repetitions = terminal if ell == last else early
        p = probability(A, m-1, J)
        miss = F(1)
        attempts = F(0)
        for _ in range(repetitions):
            attempts += miss
            miss *= 1 - p
        predicates += reach * attempts * F(J+1, 2)
        preparations += reach * attempts * J
        reach *= miss
    assert 0 <= reach <= 1
    assert (reach == 1) == (m == 1)
    return 1-reach, predicates, preparations


def main():
    spec = json.loads((HERE/'schedule-protocol.json').read_text())
    lim = spec['limits']
    resource.setrlimit(resource.RLIMIT_AS, (lim['address_space_bytes'],)*2)
    resource.setrlimit(resource.RLIMIT_CPU, (lim['cpu_seconds'],)*2)
    raw = json.loads((HERE/spec['input']).read_text())
    assert raw['status'] == 'PASS'
    for name, expected in raw['hashes'].items():
        assert sha256((HERE/name).read_bytes()).hexdigest() == expected, name
    output = dict(status='PASS', scope=spec['scope'], cases=[],
                  limits=lim, hashes={p: sha256((HERE/p).read_bytes()).hexdigest()
                    for p in ['results.json', 'schedule-protocol.json', 'score_schedules.py']})
    fixed_reproductions = 0
    for case in raw['cases']:
        b, q = case['b'], case['r']
        A = 1 << q
        denominator = A * case['ordered']
        rows = []
        for early in spec['nonterminal_trials']:
            for limit in range(b+1):
                success = predicates = preparations = F(0)
                for t, histogram in enumerate(case['joint_residue_histogram']):
                    size = A >> min(t, limit)
                    for m, count in enumerate(histogram):
                        if m == 0 or count == 0:
                            continue
                        assert m <= size
                        w = F(m * count, denominator)
                        p, c, u = schedule(size, m, early, spec['terminal_trials'])
                        success += w*p
                        predicates += w*c
                        preparations += w*u
                if early == 0:
                    previous = case['scores'][limit]
                    assert success == unpack(previous['success'])
                    assert predicates == unpack(previous['marked_predicate_evaluations'])
                    assert preparations == unpack(previous['query_preparation_calls'])
                    fixed_reproductions += 1
                rows.append(dict(nonterminal_trials=early, prefix_cap=limit,
                    success=pack(success), predicates=pack(predicates),
                    preparations=pack(preparations),
                    predicates_per_output=pack(predicates/success),
                    preparations_per_output=pack(preparations/success)))
        best = min(rows, key=lambda x: unpack(x['predicates_per_output']))
        baseline = rows[0]
        selection = dict(nonterminal_trials=best['nonterminal_trials'],
                         prefix_cap=best['prefix_cap'],
                         predicate_ratio_to_fixed_unconditioned=pack(
                             unpack(best['predicates_per_output']) /
                             unpack(baseline['predicates_per_output'])))
        output['cases'].append(dict(b=b, q=q, scores=rows, best_by_predicates=selection))
        print(json.dumps(dict(b=b, q=q,
            nonterminal_trials=best['nonterminal_trials'], prefix_cap=best['prefix_cap'],
            ratio_to_fixed_unconditioned=selection['predicate_ratio_to_fixed_unconditioned']['display'],
            predicates_per_output=best['predicates_per_output']['display'],
            success=best['success']['display'])), flush=True)
    output['exact_fixed_schedule_reproductions'] = fixed_reproductions
    (HERE/'schedule-results.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', fixed_reproductions=fixed_reproductions,
                         configurations=sum(len(c['scores']) for c in output['cases']))))


if __name__ == '__main__':
    main()
