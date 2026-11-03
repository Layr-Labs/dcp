"""Finite VFD3 diagnostics; these do not prove asymptotics or run a quantum device."""

from fractions import Fraction as Q
from math import cos, isqrt, log2, pi, sin
from pathlib import Path
import json


def clog(x):
    assert x > 0
    return (x - 1).bit_length()


def ceil_sqrt_ratio(a, b):
    """Smallest nonnegative u for which b*u*u >= a, using integer arithmetic."""
    u = isqrt(a // b)
    return u if b * u * u >= a else u + 1


def parameters(n, m):
    assert n >= 17 and m in (n - 1, n)
    h = n + 1
    ell = 1 + ceil_sqrt_ratio(2666689 * n, 4000000)
    j_max = m - 1 - ell
    lam = clog(1024 * h)
    measurements = 8192 * lam
    final_size = 1048576 * lam
    lengths = [
        final_size * (2 * 8**t - 4**t) + t * 8**t
        for t in range(ell, -1, -1)
    ]
    remaining = j_max
    widths = []
    for i in range(ell):
        b = min(3 * (ell - i - 1), remaining)
        widths.append(b)
        remaining -= b
    assert remaining == 0
    return {
        "h": h,
        "ell": ell,
        "J": j_max,
        "M": measurements,
        "F": final_size,
        "lengths": lengths,
        "widths": widths,
        "R": 4 * (j_max + 1) * lengths[0],
    }


def distance(a, b):
    d = (a - b) % 1
    return min(d, 1 - d)


def unwrap(alphas):
    z = alphas[-1]
    for a in reversed(alphas[:-1]):
        z = min((z / 2, (z + 1) / 2), key=lambda x: (distance(x, a), x))
    return z


def round_fraction(x):
    return (2 * x.numerator + x.denominator) // (2 * x.denominator)


def approximate_phases(theta, top, perturbation=0):
    phases = []
    for j in range(top + 1):
        nearest = round_fraction(64 * ((2**j * theta) % 1))
        error = perturbation if j % 2 == 0 else -perturbation
        phases.append(Q((nearest + error) % 64, 64))
    return phases


def candidates(modulus, center, top):
    radius = Q(1, 8 * 2**top)
    low, high = modulus * (center - radius), modulus * (center + radius)
    lo = -((-low.numerator) // low.denominator)
    hi = high.numerator // high.denominator
    # Enumerate only the short integer interval, splitting the wrap by modulo.
    return sorted({t % modulus for t in range(lo, hi + 1)})


def log_int(x):
    bits = x.bit_length()
    shift = max(0, bits - 48)
    return shift + log2(x >> shift)


def main():
    parameter_cases = stage_cases = allocation_cases = 0
    n_values = list(range(17, 4097)) + [8192, 16384, 100000, 1000000]
    for n in n_values:
        for m in (n - 1, n):
            p = parameters(n, m)
            h, ell, target = p["h"], p["ell"], p["J"]
            lengths, widths = p["lengths"], p["widths"]
            assert 0 <= target and ell <= m - 1
            assert (3 * ell * ell - ell) // 2 >= m - 1
            assert sum(widths) == target
            assert 4000000 * (ell - 2) ** 2 < 2666689 * n
            assert lengths[0] <= 8**ell * (2 * p["F"] + ell)
            assert p["F"] >= 8 * p["M"]
            width = m
            for i, b in enumerate(widths):
                output = lengths[i + 1]
                buckets = 2**b
                assert buckets <= 8 ** (ell - i - 1)
                assert buckets * p["F"] <= output
                assert lengths[i] >= 8 * output
                # These exact inequalities are the input to the Chernoff proof.
                t = ell - i
                assert lengths[i] - 8 * output == p["F"] * 4**t + 8**t
                mean_lower = Q(lengths[i] - buckets, 8)
                mean_upper = Q(lengths[i], 8)
                gap = mean_lower - output
                assert gap >= Q(p["F"] * 4**t, 8) + Q(7 * 8 ** (t - 1), 8)
                assert mean_upper <= 8 ** (t - 1) * (2 * p["F"] + t)
                assert gap * gap / (2 * mean_upper) >= Q(p["F"], 24)
                assert width - b >= 2
                width -= b + 1
                stage_cases += 1
            assert width == 1
            assert 7 * sum(lengths[:-1]) <= 8 * lengths[0]
            targets = range(target + 1) if n <= 80 else sorted({0, target // 2, target})
            for j in targets:
                need = j
                low_total = 0
                for b in widths:
                    a = min(b, need)
                    need -= a
                    low_total += a
                    assert a >= 0 and b - a >= 0
                assert need == 0 and low_total == j
                allocation_cases += 1
            parameter_cases += 1

    # Test the actual rational table decoder, with adverse errors on both means.
    grid_data = json.loads(Path(__file__).with_name("phase_grid.json").read_text())
    denominator = grid_data["denominator"]
    grid = [
        (point["cosine_numerator"] / denominator, point["sine_numerator"] / denominator)
        for point in grid_data["points"]
    ]
    decoder_cases = 0
    max_decoder_error = 0.0
    for t in range(1024):
        theta = t / 1024
        for dx in (-1 / 32, 1 / 32):
            for dy in (-1 / 32, 1 / 32):
                x, y = cos(2 * pi * theta) + dx, sin(2 * pi * theta) + dy
                selected = min(
                    range(64),
                    key=lambda r: ((x - grid[r][0]) ** 2 + (y - grid[r][1]) ** 2, r),
                )
                error = abs(selected / 64 - theta)
                error = min(error, 1 - error)
                assert error < 1 / 16
                max_decoder_error = max(max_decoder_error, error)
                decoder_cases += 1

    # Exact rational unwrapping with alternating near-worst allowed grid errors.
    spectral_cases = interval_cases = 0
    moduli = list(range(2, 97)) + [127, 128, 129, 257, 1023, 1024, 1025, 65537]
    for modulus in moduli:
        n = (modulus - 1).bit_length()
        secrets = range(modulus) if modulus <= 96 else sorted(
            {0, 1, 2, modulus // 3, modulus // 2, modulus - 2, modulus - 1}
        )
        for secret in secrets:
            theta = Q(secret, modulus)
            for perturbation in (-3, 0, 3):
                phases = approximate_phases(theta, n + 2, perturbation)
                assert all(distance(a, (2**j * theta) % 1) <= Q(1, 16)
                           for j, a in enumerate(phases))
                estimate = unwrap(phases)
                assert distance(estimate, theta) <= Q(1, 16 * 2 ** (n + 2))
                assert round_fraction(modulus * estimate) % modulus == secret
                spectral_cases += 1
                for top in sorted({0, n // 2, max(0, n - 3)}):
                    coarse = unwrap(approximate_phases(theta, top, perturbation))
                    possible = candidates(modulus, coarse, top)
                    assert secret in possible
                    assert len(possible) <= modulus / (4 * 2**top) + 2
                    interval_cases += 1

    # The final interval bound holds even for erroneous phase estimates.
    invalid_estimate_cases = 0
    for n in (17, 18, 24, 32, 48, 64):
        for modulus in (2 ** (n - 1) + 1, 2**n - 1, 2**n):
            m = modulus.bit_length() - 1
            p = parameters(n, m)
            for i in (0, 1, 7, 31, 63):
                possible = candidates(modulus, Q(i, 64), p["J"])
                assert len(possible) <= 2 ** p["ell"] + 2
                invalid_estimate_cases += 1

    budgets = []
    for n in (64, 256, 1024, 4096, 16384):
        p = parameters(n, n)
        old_b = ceil_sqrt_ratio(n, 1)
        old_ell = (n - 1 + old_b) // (old_b + 1)
        old_m = 8192 * clog(128 * (n + 1))
        old_f = 2 ** (old_b + 8) * (n + 1) ** 2 + 16 * old_m
        old_l = 32**old_ell * old_f
        budgets.append({
            "n": n,
            "VFD3_depth": p["ell"],
            "VFD3_log2_initial_list": round(log_int(p["lengths"][0]), 6),
            "FD2_log2_initial_list": round(log_int(old_l), 6),
            "note": "Theoretical integer quotas, not measured execution times.",
        })

    result = {
        "scope": "Finite diagnostics only; not asymptotic proof or official evaluation.",
        "parameter_cases": parameter_cases,
        "stage_inequalities": stage_cases,
        "target_bit_allocations": allocation_cases,
        "phase_decoder_numeric_checks": decoder_cases,
        "maximum_observed_decoder_error_turns": max_decoder_error,
        "exact_spectral_label_reconstructions": spectral_cases,
        "exact_true_secret_interval_checks": interval_cases,
        "erroneous_estimate_interval_size_checks": invalid_estimate_cases,
        "theoretical_quota_comparison": budgets,
    }
    Path(__file__).with_name("schedule_results.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
