"""Finite diagnostics for a new DCP research draft; not an official verifier.

All quantum measurement probabilities used below are derived analytically in the
research note. Finite checks do not establish the asymptotic resource theorem.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product
from math import ceil, isqrt, pi, sqrt
import cmath
import json
import random
from pathlib import Path


def cd(a, b):
    d = (a - b) % 1
    return min(d, 1 - d)


def decode(angles):
    z = angles[-1]
    for angle in reversed(angles[:-1]):
        candidates = (z / 2, (z + 1) / 2)
        z = min(candidates, key=lambda v: cd(v, angle))
    return z


def parameters(N):
    n = (N - 1).bit_length()
    m = N.bit_length() - 1
    b = isqrt(n)
    b += b * b < n
    remaining = m - 1
    blocks = []
    while remaining:
        consumed = min(b + 1, remaining)
        blocks.append(consumed - 1)
        remaining -= consumed
    return n, m, b, blocks, m - 1 - len(blocks)


def schedule(N, j):
    n, m, b, blocks, J = parameters(N)
    assert 0 <= j <= J
    left, width, shift = j, m, 0
    steps = []
    for grouped in blocks:
        low = min(left, grouped)
        high = grouped - low
        left -= low
        middle = width - grouped
        assert middle >= 1
        steps.append((width, low, high, middle))
        width = middle - 1
        shift += low
    assert left == 0 and width == 1 and shift == j
    return steps


def check_uniformizer():
    cases = 0
    for k in range(1, 12):
        M = 1 << k
        result = {}
        for d in range(M):
            p = Q(1, M) if d == 0 else Q(2 * (M - d), M * M)
            accept = Q(0) if d >= M // 2 else Q(1) if d == 0 else Q(M, 2 * (M - d))
            assert 0 <= accept <= 1
            result[d] = p * accept
        assert sum(result.values()) == Q(1, 2)
        assert all(result[d] == Q(1, M) for d in range(M // 2))
        assert all(result[d] == 0 for d in range(M // 2, M))
        cases += 1
    return cases


def check_all_buckets():
    cases = pairs = 0
    for width in range(1, 7):
        B = 1 << width
        for low in range(width):
            for high in range(width - low):
                middle = width - low - high
                M = 1 << middle
                buckets = defaultdict(list)
                for u in range(B):
                    key = (u % (1 << low), u >> (low + middle))
                    buckets[key].append(u)
                for values in buckets.values():
                    assert len(values) == M
                    histogram = Counter()
                    for u in values:
                        for v in values:
                            assert abs(u - v) % (1 << low) == 0
                            d = abs(u - v) >> low
                            if d < M // 2:
                                accept = Q(1) if d == 0 else Q(M, 2 * (M - d))
                                histogram[d] += accept / (M * M)
                            pairs += 1
                    assert set(histogram) == set(range(M // 2))
                    assert all(p == Q(1, M) for p in histogram.values())
                    assert sum(histogram.values()) == Q(1, 2)
                    cases += 1
    return {'buckets': cases, 'ordered_pairs': pairs}


def check_schedules():
    count = 0
    for n in range(1, 129):
        for N in {1 << n, (1 << n) - 1, (1 << (n - 1)) + 1}:
            if N < 2:
                continue
            _, _, b, blocks, J = parameters(N)
            assert len(blocks) <= b - 1
            for j in range(J + 1):
                schedule(N, j)
                count += 1
    return count


def check_phase_decode_and_candidates():
    count = 0
    for N in range(2, 129):
        _, _, _, blocks, J = parameters(N)
        for s in range(N):
            theta = Q(s, N)
            for pattern in range(4):
                angles = []
                for j in range(J + 1):
                    sign = 1 if (j + pattern) % 2 == 0 else -1
                    err = Q(sign, 16 if pattern < 2 else 32)
                    angles.append(((1 << j) * theta + err) % 1)
                z = decode(angles)
                assert cd(z, theta) <= Q(1, 16 * (1 << J))
                candidates = [t for t in range(N) if cd(Q(t, N), z) <= Q(1, 8 * (1 << J))]
                assert s in candidates
                assert len(candidates) <= (1 << len(blocks)) + 2
                count += 1
    return count


def check_spectral_decomposition():
    cases = 0
    worst = 0.0
    for N in range(2, 13):
        omega = cmath.exp(2j * pi / N)
        for s in range(N):
            rho = [[0j] * (2 * N) for _ in range(2 * N)]
            for x in range(N):
                a, b = x, N + (x + s) % N
                for u, v in ((a, a), (a, b), (b, a), (b, b)):
                    rho[u][v] += 1 / (2 * N)
            alt = [[0j] * (2 * N) for _ in range(2 * N)]
            for y in range(N):
                vec = [omega ** (-y * x) / sqrt(2 * N) for x in range(N)]
                vec += [omega ** (y * (s - x)) / sqrt(2 * N) for x in range(N)]
                for u in range(2 * N):
                    for v in range(2 * N):
                        alt[u][v] += vec[u] * vec[v].conjugate() / N
                chi = [omega ** (-y * x) / sqrt(N) for x in range(N)]
                for x in range(N):
                    assert abs(chi[(x - 1) % N] - omega ** y * chi[x]) < 1e-10
            delta = max(abs(rho[u][v] - alt[u][v]) for u in range(2 * N) for v in range(2 * N))
            worst = max(worst, delta)
            assert delta < 1e-10
            cases += 1
    return {'cases': cases, 'maximum_entry_error': worst}


def simulate(width, j, seed):
    # Modest diagnostic batch, smaller than the proposed theorem's conservative
    # batch sizes. This tests the classical label process, not a quantum circuit.
    N = 1 << width
    steps = schedule(N, j)
    _, _, b, _, _ = parameters(N)
    initial_count = (1 << (b + 2)) * (16 ** len(steps))
    rng = random.Random(seed)
    labels = [rng.randrange(1 << width) for _ in range(initial_count)]
    counts = [len(labels)]
    for current_width, low, high, middle in steps:
        M = 1 << middle
        buckets = defaultdict(list)
        for u in labels:
            key = (u % (1 << low), u >> (low + middle))
            buckets[key].append(u)
        outputs = []
        for values in buckets.values():
            for i in range(0, len(values) - 1, 2):
                if rng.randrange(2) == 0:  # CNOT parity outcome rejected
                    continue
                d = abs(values[i] - values[i + 1]) >> low
                if d >= M // 2:
                    continue
                if d == 0 or rng.randrange(2 * (M - d)) < M:
                    outputs.append(d)
        labels = outputs
        counts.append(len(labels))
    assert all(x in (0, 1) for x in labels)
    return {'width': width, 'target_exponent': j, 'stage_counts': counts, 'usable_final_states': labels.count(1)}


def main():
    results = {
        'scope': 'Finite research diagnostics only; no official review or asymptotic certification.',
        'uniformizer_moduli': check_uniformizer(),
        'bucket_checks': check_all_buckets(),
        'schedules': check_schedules(),
        'phase_decode_and_candidate_cases': check_phase_decode_and_candidates(),
        'spectral_decomposition': check_spectral_decomposition(),
        'label_process_simulations': [],
    }
    for width in (6, 8, 12, 16):
        J = parameters(1 << width)[-1]
        for j in sorted({0, J // 2, J}):
            results['label_process_simulations'].append(simulate(width, j, 1000 + 10 * width + j))
    destination = Path(__file__).with_name('flat_sieve_results.json')
    destination.write_text(json.dumps(results, indent=2) + '\n')
    print(json.dumps(results, indent=2))

if __name__ == '__main__':
    main()
