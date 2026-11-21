"""Supplementary checks, not a quantum implementation or proof certificate.

Run with Python 3.11+ and NumPy. The full q=128(n+1) batch is checked
analytically through exact binomial tails; quantum simulations use toy q.
"""
import itertools
import json
import math
from fractions import Fraction

import numpy as np


def one_source(N, s, x):
    M = 1 << (N - 1).bit_length()
    v = np.zeros(2 * M, dtype=complex)
    v[x] = 1 / math.sqrt(2)
    v[M + (x + s) % N] = 1 / math.sqrt(2)
    return v


def candidate_unitary(N, t):
    M = 1 << (N - 1).bit_length()
    C = np.zeros((2 * M, 2 * M), dtype=complex)
    for b in range(2):
        for y in range(M):
            z = (y - t) % N if b and y < N else y
            C[b * M + z, b * M + y] = 1
    H = np.array([[1, 1], [1, -1]]) / math.sqrt(2)
    return np.kron(H, np.eye(M)) @ C


def product_state(vectors):
    result = np.ones(1, dtype=complex)
    for v in vectors:
        result = np.kron(result, v)
    return result


def local_apply(v, U, axis, q):
    d = U.shape[0]
    a = np.moveaxis(v.reshape((d,) * q), axis, 0)
    a = (U @ a.reshape(d, -1)).reshape(a.shape)
    return np.moveaxis(a, 0, axis).reshape(-1)


def weight_mask(d, q, r):
    indices = np.arange(d ** q)
    weights = np.zeros(d ** q, dtype=int)
    for axis in range(q):
        digit = (indices // (d ** (q - axis - 1))) % d
        weights += digit >= d // 2
    return weights <= r


def project(v, U, q, mask):
    z = v.copy()
    for axis in range(q):
        z = local_apply(z, U, axis, q)
    z[~mask] = 0
    for axis in reversed(range(q)):
        z = local_apply(z, U.conj().T, axis, q)
    return z


def toy_case(N, s, q, bad_position=None, seed=0):
    r = 0 if bad_position is None else 1
    g = q - (bad_position is not None)
    d = 2 << (N - 1).bit_length()
    mask = weight_mask(d, q, r)
    U = [candidate_unitary(N, t) for t in range(N)]
    rng = np.random.default_rng(seed)
    bad = rng.normal(size=d) + 1j * rng.normal(size=d)
    bad /= np.linalg.norm(bad)
    probabilities = np.zeros(N)
    wrong_initial = np.zeros(N)
    fallback = 0.0
    preservation = 0.0
    idempotence = 0.0
    for offsets in itertools.product(range(N), repeat=g):
        it = iter(offsets)
        pieces = [bad if j == bad_position else one_source(N, s, next(it))
                  for j in range(q)]
        v = product_state(pieces)
        preserved = project(v, U[s], q, mask)
        preservation = max(preservation, float(np.linalg.norm(preserved - v)))
        for t in range(N):
            pv = project(v, U[t], q, mask)
            wrong_initial[t] += float(np.vdot(pv, pv).real) / N ** g
            idempotence = max(idempotence, float(np.linalg.norm(project(pv, U[t], q, mask) - pv)))
        current = v.copy()
        for t in range(N):
            accepted = project(current, U[t], q, mask)
            probabilities[t] += float(np.vdot(accepted, accepted).real) / N ** g
            current -= accepted
        fallback += float(np.vdot(current, current).real) / N ** g
    eta = float(Fraction(sum(math.comb(g, j) for j in range(min(r, g) + 1)), 2 ** g))
    lower = max(0.0, 1 - s * math.sqrt(eta)) ** 2
    assert preservation < 1e-11, (N, s, preservation)
    assert idempotence < 1e-11, (N, s, idempotence)
    assert abs(sum(probabilities) + fallback - 1) < 1e-10
    assert probabilities[s] + 1e-11 >= lower
    for t in range(N):
        if t != s:
            assert wrong_initial[t] <= eta + 1e-11
    return {'N': N, 's': s, 'toy_q': q, 'r': r,
            'bad_position': bad_position,
            'correct_branch_probability': float(probabilities[s]),
            'telescoping_lower_bound': lower,
            'max_preservation_error': preservation,
            'max_idempotence_error': idempotence}


def main():
    parity_cases = 0
    for a, b, c in itertools.product(range(2), repeat=3):
        assert 4*a*b*c == a+b+c-(a^b)-(a^c)-(b^c)+(a^b^c)
        parity_cases += 1
    local_cases = 0
    for N in range(2, 17):
        M = 1 << (N - 1).bit_length()
        for t in range(N):
            U = candidate_unitary(N, t)
            assert np.allclose(U.conj().T @ U, np.eye(2*M), atol=1e-14)
            for s in range(N):
                for x in range(N):
                    w = U @ one_source(N, s, x)
                    minus = float(np.vdot(w[M:], w[M:]).real)
                    assert abs(minus - (0 if s == t else 0.5)) < 1e-13
                    local_cases += 1
    tail_checks = []
    for n in range(1, 65):
        q = 128*(n+1)
        r = q//4
        g = q-r
        tail = Fraction(sum(math.comb(g, j) for j in range(r+1)), 2**g)
        tail_upper = math.exp(-q/32)
        assert float(tail) <= tail_upper
        loss_upper = 2**n * math.exp(-q/64)
        assert loss_upper < 1/8
        tail_checks.append({'n': n, 'q': q, 'exact_binomial_tail_float': float(tail),
                            'hoeffding_upper': tail_upper,
                            'success_lower': (1-loss_upper)**2})
    toy = []
    for N in range(2, 6):
        for q in (1, 2, 3):
            for s in range(N):
                toy.append(toy_case(N, s, q))
    for N in (2, 3):
        for s in range(N):
            for bad_position in (0, 3):
                toy.append(toy_case(N, s, 4, bad_position, seed=20261120+s))
    print(json.dumps({'status':'passed', 'numpy':np.__version__,
                      'limitations':'Toy quantum batches; no full-size hardware execution, no formal proof certificate, no general correlated-error simulation.',
                      'ccz_identity_cases':parity_cases,
                      'local_state_checks':local_cases,
                      'prescribed_batch_tail_checks':tail_checks,
                      'toy_sequential_cases':toy}, indent=2))


if __name__ == '__main__':
    main()
