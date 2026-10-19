"""Check the source-only modular-shift estimator and rational phase decoder.
Small finite diagnostics; not an implementation of the complete DCP algorithm.
"""
import cmath
from fractions import Fraction as Q
import json
from math import cos, sin, pi, sqrt, log2, ceil
from pathlib import Path
import random


def cd(a, b):
    d = (a - b) % 1
    return min(d, 1 - d)


def decode(angles):
    z = angles[-1]
    for alpha in reversed(angles[:-1]):
        z = min((z / 2, (z + 1) / 2), key=lambda v: cd(v, alpha))
    return z


def build_grid():
    # Ordinary finite diagnostic uses libm only to initialize this fixed table.
    # The proof specifies a rational Taylor/Machin construction instead.
    scale = 1 << 16
    return [(Q(round(scale * cos(2 * pi * r / 64)), scale),
             Q(round(scale * sin(2 * pi * r / 64)), scale)) for r in range(64)]


def grid_angle(x, y, grid):
    r = min(range(64), key=lambda k: (grid[k][0] - x) ** 2 + (grid[k][1] - y) ** 2)
    return Q(r, 64)


def exact_shift_tests():
    count = 0
    worst = 0.0
    for N in range(2, 34):
        n = (N - 1).bit_length()
        for y in range(N):
            chi = [cmath.exp(-2j * pi * y * x / N) / sqrt(N) for x in range(N)]
            for h in range(n + 3):
                shift = pow(2, h, N)
                a0 = [v / sqrt(2) for v in chi]
                a1 = [chi[(x - shift) % N] / sqrt(2) for x in range(N)]
                px = sum(abs((u + v) / sqrt(2)) ** 2 for u, v in zip(a0, a1))
                py = sum(abs((u - 1j * v) / sqrt(2)) ** 2 for u, v in zip(a0, a1))
                phi = 2 * pi * pow(2, h, N) * y / N
                error = max(abs(px - (1 + cos(phi)) / 2), abs(py - (1 + sin(phi)) / 2))
                assert error < 1e-11
                worst = max(worst, error)
                count += 1
    return {'controlled_shift_XY_cases': count, 'maximum_probability_error': worst}


def bounded_noise_tests(grid):
    count = 0
    worst = Q(0)
    for denominator in (17, 31, 64, 97, 128):
        for numerator in range(denominator):
            theta = Q(numerator, denominator)
            for sx in (-1, 1):
                for sy in (-1, 1):
                    x = Q(round((1 << 24) * cos(2 * pi * float(theta))), 1 << 24) + Q(sx, 32)
                    y = Q(round((1 << 24) * sin(2 * pi * float(theta))), 1 << 24) + Q(sy, 32)
                    alpha = grid_angle(x, y, grid)
                    error = cd(alpha, theta)
                    assert error < Q(1, 16)
                    worst = max(worst, error)
                    count += 1
    return {'adversarial_coordinate_noise_cases': count, 'maximum_phase_error': str(worst)}


def sampling_tests(grid):
    rng = random.Random(260619)
    count = 0
    samples = 4096  # smaller than the theorem's conservative count
    for N in (3, 7, 8, 17, 31, 35, 45, 64, 97, 127, 128, 193):
        n = (N - 1).bit_length()
        for y in sorted({0, 1, N // 3, N // 2, N - 1}):
            angles = []
            for h in range(n + 3):
                phi = 2 * pi * (pow(2, h, N) * y % N) / N
                px, py = (1 + cos(phi)) / 2, (1 + sin(phi)) / 2
                x = Q(2 * sum(rng.random() < px for _ in range(samples)) - samples, samples)
                z = Q(2 * sum(rng.random() < py for _ in range(samples)) - samples, samples)
                angles.append(grid_angle(x, z, grid))
            estimate = decode(angles)
            t = (N * estimate.numerator * 2 + estimate.denominator) // (2 * estimate.denominator) % N
            assert t == y
            count += 1
    return {'sampled_label_recoveries': count, 'shots_per_X_or_Y_estimate': samples}


def main():
    grid = build_grid()
    result = {'scope': 'Finite checks only; no official review or resource certification.',
              **exact_shift_tests(), **bounded_noise_tests(grid), **sampling_tests(grid)}
    Path(__file__).with_name('spectral_shift_results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
