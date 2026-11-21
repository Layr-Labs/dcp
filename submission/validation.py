"""Supplementary exact constants and numerical toy coherent-search checks.

Not a full prescribed-batch implementation or a formal proof certificate.
Run with Python 3.11+ and NumPy; no network access or credentials needed.
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
    a = np.moveaxis(v.reshape((d,) * q + (-1,)), axis, 0)
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
    z = z.reshape(len(mask), -1)
    z[~mask] = 0
    z = z.reshape(-1)
    for axis in reversed(range(q)):
        z = local_apply(z, U.conj().T, axis, q)
    return z


def purification(N, s, q, bad_position=None):
    """Purify a product clean marginal, entangling one bad register if requested."""
    d = 2 << (N - 1).bit_length()
    g = q - (bad_position is not None)
    rank = N ** g
    ref_dim = rank if bad_position is None else (rank + d - 1) // d
    omega = np.zeros((d ** q, ref_dim), complex)
    if bad_position is not None:
        rng = np.random.default_rng(20261121 + N + s)
        z = rng.normal(size=(d, d)) + 1j*rng.normal(size=(d, d))
        bad_basis, _ = np.linalg.qr(z)
    for label, offsets in enumerate(itertools.product(range(N), repeat=g)):
        it = iter(offsets)
        vectors = [bad_basis[:, label % d] if j == bad_position
                   else one_source(N, s, next(it)) for j in range(q)]
        ref = label if bad_position is None else label // d
        omega[:, ref] += product_state(vectors) / math.sqrt(rank)
    assert abs(np.linalg.norm(omega) - 1) < 1e-12
    if bad_position is not None:
        # Trace out bad plus inaccessible reference; verify the JOINT good marginal.
        a = np.moveaxis(omega.reshape((d,) * q + (ref_dim,)), bad_position, q-1)
        a = a.reshape(d ** g, d * ref_dim)
        marginal = a @ a.conj().T
        rho = sum(np.outer(one_source(N,s,x),one_source(N,s,x).conj())
                  for x in range(N)) / N
        expected = rho
        for _ in range(g-1): expected = np.kron(expected, rho)
        assert np.linalg.norm(marginal-expected) < 1e-11
    return omega


def coherent_case(N, s, q, bad_position=None):
    r = 0 if bad_position is None else 1
    g = q - (bad_position is not None)
    n = (N-1).bit_length()
    L = 1 << (n+3)
    k = math.isqrt(9 << (n-1))
    d = 2 << n
    omega = purification(N, s, q, bad_position)
    flat = omega.reshape(-1)
    mask = weight_mask(d, q, r)
    U = [candidate_unitary(N,t) for t in range(N)]
    projections = [project(flat,u,q,mask) for u in U]
    preservation = float(np.linalg.norm(projections[s]-flat))
    assert preservation < 1e-11
    wrong_max = max(float(np.vdot(projections[t],projections[t]).real)
                    for t in range(N) if t!=s)
    eta = float(Fraction(sum(math.comb(g,j) for j in range(r+1)), 2**g))
    assert wrong_max <= eta+1e-11
    actual = np.tile(flat / math.sqrt(L), (L,1))
    ideal = actual.copy()
    # Check oracle involution on a state entangled across candidate and source.
    rng = np.random.default_rng(1000+N+s)
    probe = rng.normal(size=actual.shape) + 1j*rng.normal(size=actual.shape)
    probe /= np.linalg.norm(probe)
    original_probe = probe.copy()
    for _ in range(2):
        for t in range(N): probe[t] -= 2*project(probe[t],U[t],q,mask)
    involution_error = float(np.linalg.norm(probe-original_probe))
    assert involution_error < 1e-11
    step_errors = []
    for j in range(1,k+1):
        for t in range(N): actual[t] -= 2*project(actual[t],U[t],q,mask)
        actual = 2*actual.mean(axis=0,keepdims=True)-actual
        ideal[s] *= -1
        ideal = 2*ideal.mean(axis=0,keepdims=True)-ideal
        error = float(np.linalg.norm(actual-ideal))
        assert error <= 2*j*math.sqrt(eta)+1e-10
        assert abs(np.linalg.norm(actual)-1)<1e-10
        step_errors.append(error)
    theta = math.asin(1/math.sqrt(L))
    ideal_amplitude = math.sin((2*k+1)*theta)
    assert abs(np.linalg.norm(ideal[s])-ideal_amplitude)<1e-11
    probability = float(np.vdot(actual[s],actual[s]).real)
    lower = max(0,ideal_amplitude-2*k*math.sqrt(eta))**2
    assert probability+1e-10>=lower
    return {'N':N,'s':s,'toy_q':q,'toy_r':r,'L':L,'k':k,
            'entangled_bad_position':bad_position,
            'correct_measurement_probability':probability,
            'hybrid_success_lower':lower,
            'original_wrong_projector_max':wrong_max,
            'max_preservation_error':preservation,
            'oracle_involution_error':involution_error,
            'step_state_distances':step_errors}


def main():
    parity_cases = 0
    for a,b,c in itertools.product(range(2),repeat=3):
        assert 4*a*b*c == a+b+c-(a^b)-(a^c)-(b^c)+(a^b^c)
        parity_cases += 1
    exp_partial = sum((Fraction(16,3)**j/math.factorial(j) for j in range(13)),Fraction())
    assert exp_partial > 192
    assert Fraction(263,288)**2 > Fraction(5,6)
    assert Fraction(9,28) < Fraction(1,3)
    assert Fraction(49,15) < Fraction(121,36)
    local_cases = 0
    for N in range(2,17):
        M = 1 << (N-1).bit_length()
        for t in range(N):
            u = candidate_unitary(N,t)
            assert np.allclose(u.conj().T@u,np.eye(2*M),atol=1e-14)
            for s in range(N):
                for x in range(N):
                    w = u@one_source(N,s,x)
                    minus = float(np.vdot(w[M:],w[M:]).real)
                    assert abs(minus-(0 if t==s else .5))<1e-13
                    local_cases += 1
    scalar = []
    for n in range(1,65):
        q = 128*(n+1); r = q//4; g = q-r
        L = 1 << (n+3); k = math.isqrt(9 << (n-1))
        assert 16*k*k<=9*L<16*(k+1)**2
        tail = Fraction(sum(math.comb(g,j) for j in range(r+1)),2**g)
        upper = math.exp(-q/24)
        assert float(tail)<=upper
        angle = (2*k+1)*math.asin(1/math.sqrt(L))
        amplitude = math.sin(angle)
        loss = 2*k*math.exp(-q/48)
        assert amplitude>17/18 and loss<1/32
        lower = (amplitude-loss)**2
        assert lower>5/6
        scalar.append({'n':n,'q':q,'k':k,'tail_float':float(tail),
                       'hoeffding_upper':upper,'ideal_amplitude':amplitude,
                       'hybrid_error_upper':loss,'success_lower':lower})
    toy = []
    for N in range(2,5):
        for s in range(N):
            for q in (1,2): toy.append(coherent_case(N,s,q))
    for N in (2,3):
        for s in range(N):
            toy.append(coherent_case(N,s,3))
            for bad in (0,3): toy.append(coherent_case(N,s,4,bad))
    print(json.dumps({'status':'passed','numpy':np.__version__,
                      'limitations':'Numerical toy circuits, not the full prescribed batch or a formal certificate. Selected entangled extensions are tested; universal error guarantees rest on the proof. Tail probabilities are exact rationals but compared as floats.',
                      'exact_exp_partial_sum':str(exp_partial),
                      'exact_success_floor':str(Fraction(263,288)**2),
                      'ccz_identity_cases':parity_cases,
                      'local_state_checks':local_cases,
                      'prescribed_batch_scalar_checks':scalar,
                      'toy_coherent_cases':toy},indent=2))


if __name__=='__main__': main()
