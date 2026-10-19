"""Finite check that discarded pairing histories differ only by global phase.
This does not check or refute the information-loss paper's theorem, and does not
establish correctness of the entire research draft.
"""
from collections import Counter
import cmath
from math import pi, sqrt
from pathlib import Path
import json
from flat_sieve_checks import parameters, schedule

count = 0
worst_probability_error = 0.0
worst_density_error = 0.0
histories = Counter()
for N in range(2, 50):
    J = parameters(N)[-1]
    for j in range(J + 1):
        multiplier = 1
        for width, low, high, middle in schedule(N, j):
            B, M = 1 << width, 1 << middle
            for u in range(B):
                bucket_u = (u % (1 << low), u >> (low + middle))
                for v in range(B):
                    bucket_v = (v % (1 << low), v >> (low + middle))
                    if bucket_u != bucket_v:
                        continue
                    d = abs(u - v) >> low
                    if d >= M // 2:
                        continue
                    new_label = multiplier * (1 << low) * d
                    for s in range(N):
                        omega = cmath.exp(2j * pi * s * multiplier / N)
                        # Full initial two-qubit vector, CNOT, then target=1.
                        original = [0.5, omega ** v / 2, omega ** u / 2, omega ** (u + v) / 2]
                        after_cnot = [original[0], original[1], original[3], original[2]]
                        kept = [after_cnot[1], after_cnot[3]]
                        probability = sum(abs(z) ** 2 for z in kept)
                        worst_probability_error = max(worst_probability_error, abs(probability - 0.5))
                        assert abs(probability - 0.5) < 1e-10
                        kept = [z / sqrt(probability) for z in kept]
                        if u < v:
                            kept.reverse()
                        target = [1 / sqrt(2), cmath.exp(2j * pi * s * new_label / N) / sqrt(2)]
                        delta = max(abs(kept[a] * kept[b].conjugate() - target[a] * target[b].conjugate())
                                    for a in (0, 1) for b in (0, 1))
                        worst_density_error = max(worst_density_error, delta)
                        assert delta < 1e-10
                        histories[(N, s, multiplier << low, d)] += 1
                        count += 1
            multiplier <<= low
result = {
    'scope': 'Finite conditional output-state checks only; not an official or independent proof review.',
    'conditional_history_cases': count,
    'retained_record_groups': len(histories),
    'largest_number_of_old_histories_for_one_retained_record': max(histories.values()),
    'maximum_parity_probability_error': worst_probability_error,
    'maximum_output_density_matrix_error': worst_density_error,
}
Path(__file__).with_name('label_retention_results.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
