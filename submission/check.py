"""Exact certificates and small search-circuit checks, not production DCP replay."""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import hashlib
import json
import random
import resource
import sys
import time

ROOT = Path(__file__).resolve().parent


def ceil_log2(x):
    return (x - 1).bit_length()


def parameters(n):
    d = ceil_log2(n + 2)
    a = 4 * d + 8
    b = max(12, n - a + 12)
    assert n >= 20 and b <= n
    domain, cap = 1 << n, 1 << b
    k = (isqrt(1 << (n - b)) - 1) // 2
    j = 3 * isqrt(cap) // 4
    return domain, cap, a, k, j


def odd_sine_polynomial(steps, z):
    """sin((2 steps+1) asin(sqrt(z)))/sqrt(z), as a polynomial in z."""
    if steps == 0:
        return F(1)
    old, now = F(1), 3 - 4 * z
    for _ in range(1, steps):
        old, now = now, 2 * (1 - 2 * z) * now - old
    return now


def walsh(state):
    out = state[:]
    width = 1
    while width < len(out):
        for start in range(0, len(out), 2 * width):
            for i in range(start, start + width):
                a, b = out[i], out[i + width]
                out[i], out[i + width] = a + b, a - b
        width *= 2
    root = isqrt(len(out))
    assert root * root == len(out)
    return [a / root for a in out]


def phase(state, marked):
    return [-v if i in marked else v for i, v in enumerate(state)]


def zero_reflection(state):
    return [state[0]] + [-v for v in state[1:]]


def uniform_reflection(state):
    return walsh(zero_reflection(walsh(state)))


def circuit(domain, marked, secret, k, j, omit_inverse=False):
    counts = dict(filter=0, full=0)

    def prepare(state):
        state = walsh(state)
        for _ in range(k):
            state = phase(state, marked)
            counts['filter'] += 1
            state = uniform_reflection(state)
        return state

    def inverse(state):
        for _ in range(k):
            state = uniform_reflection(state)
            state = phase(state, marked)
            counts['filter'] += 1
        return walsh(state)

    state = prepare([F(1)] + [F(0)] * (domain - 1))
    for _ in range(j):
        state = phase(state, {secret})
        counts['full'] += 1
        if not omit_inverse:
            state = inverse(state)
        state = zero_reflection(state)
        state = prepare(state)
    assert sum(v * v for v in state) == 1
    return state, counts


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (45, 45))
    resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))
    started = time.process_time()
    tau = F(1, 2**24)
    eta = (3 * F(22, 7) + 1) / 2**24
    kappa = 2 * (1 + tau) / 10**8 + eta
    epsilon, delta, threshold = F(3333, 10000), F(1, 50000), F(6667, 40000)
    lo = (1 - epsilon) * (F(1, 2) - kappa) - epsilon * (F(1, 2) + eta) - delta
    hi = kappa + epsilon * (F(1, 2) + eta) + delta
    gamma = F(1, 250000)
    assert lo - threshold > gamma and threshold - hi > gamma
    assert 2 / gamma**2 == 125000000000

    angle_lo = (F(3, 2) - F(5, 128)) * F(7, 8) * F(377, 378)
    angle_hi = (F(3, 2) + F(1, 64)) * F(64, 63) * F(129, 128)
    assert F(256, 16383) < F(1, 63)
    assert F(129, 128)**2 * (1 - F(1, 16384)) > 1
    assert F(129, 8192) < F(1, 63)
    assert F(64, 63)**2 * (1 - F(1, 63**2)) > 1
    assert F(5, 4) < angle_lo < angle_hi < F(25, 16)
    x = F(5, 4)
    sine_lower = x - x**3 / 6 + x**5 / 120 - x**7 / 5040
    assert sine_lower > 0 and sine_lower**2 > F(7, 8)
    total = F(7, 8) * F(127, 128) * (F(31, 32) - F(1, 2**16)) * F(7, 8)
    assert total == F(395079601, 536870912) and total > F(2, 3)

    parameter_cases = 0
    for n in range(20, 4097):
        domain, cap, a, k, j = parameters(n)
        assert cap >= 4096 and domain >= 256 * cap and a >= 16
        q = 2 * k + 1
        assert q*q*cap <= domain <= (q + 2)**2 * cap
        assert (1 + F(domain, 1 << a)) * 64 / cap <= F(1, 32)
        assert (k * (2*j + 1))**2 <= domain and j*j <= cap
        assert cap <= max(F(4096), F(16 * domain, (n + 2)**4))
        parameter_cases += 1

    sampler_cases = 0
    for population in range(2, 33):
        size = 1 << ceil_log2(population)
        for retries in range(1, 7):
            fail = F(size - population, size)
            per_index = sum((fail**r / size for r in range(retries)), F(0))
            assert population * per_index == 1 - fail**retries
            assert per_index / (1 - fail**retries) == F(1, population)
            assert fail**retries <= F(1, 2**retries)
            sampler_cases += 1

    rng = random.Random(20261109)
    circuit_cases = 0
    for domain in (4, 16, 64):
        for modulus in (domain // 2 + 1, domain - 1, domain):
            order = list(range(modulus))
            rng.shuffle(order)
            for h in sorted({1, 2, modulus // 2, modulus}):
                marked = set(order[:h])
                secret = order[h // 2]
                assert secret in marked and all(t < modulus for t in marked)
                for k in (0, 1, 3):
                    alpha = odd_sine_polynomial(k, F(h, domain)) / isqrt(domain)
                    for j in (0, 1, 3):
                        state, counts = circuit(domain, marked, secret, k, j)
                        expected = alpha * odd_sine_polynomial(j, alpha*alpha)
                        assert state[secret] == expected
                        assert counts == dict(filter=k*(2*j+1), full=j)
                        circuit_cases += 1

    bad, _ = circuit(16, {0, 1, 2}, 0, 1, 1, omit_inverse=True)
    good, _ = circuit(16, {0, 1, 2}, 0, 1, 1)
    assert bad[0]**2 != good[0]**2
    counterexample_t = 100
    bad_probability = F(counterexample_t - 1, counterexample_t)
    mean = bad_probability*(counterexample_t+1) + (1-bad_probability)
    assert mean == counterexample_t and bad_probability == F(99, 100)

    source = ROOT / 'sources/ROB-G2-proof.md'
    assert hashlib.sha256(source.read_bytes()).hexdigest() == (
        '64a87926620815ae4030997207eedff9f4507b5fb825c3c07d88c5794f566228')
    result = dict(
        all_passed=True, python=sys.version, arithmetic='fractions.Fraction throughout',
        gap_below=str(lo-threshold), gap_above=str(threshold-hi), gamma=str(gamma),
        angle_lower=str(angle_lo), angle_upper=str(angle_hi),
        sine_success_lower=str(sine_lower**2), unconditional_success_lower=str(total),
        parameter_cases=parameter_cases, capped_sampler_cases=sampler_cases,
        exact_small_search_circuits=circuit_cases,
        missing_inverse_negative_control_detected=True,
        original_markov_slack_counterexample=dict(mean=counterexample_t,
            threshold=counterexample_t, probability_above_threshold=str(bad_probability)),
        scope='Small exact H-layer/Boolean-phase-oracle circuits; not emitted score gates or production DCP source replay.',
        cpu_seconds=time.process_time()-started)
    (ROOT / 'results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
