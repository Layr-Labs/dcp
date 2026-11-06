#!/usr/bin/env python3
"""Finite exact diagnostics for proof.md; not the asymptotic implementation."""
import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


class BooleanCircuit:
    """Diagnostic circuit list. The proof's controller streams this grammar."""

    def __init__(self, inputs):
        self.wires = inputs
        self.gates = []

    def fresh(self):
        q = self.wires
        self.wires += 1
        return q

    def const(self, bit):
        q = self.fresh()
        if bit:
            self.gates.append((q,))
        return q

    def xor(self, a, b):
        q = self.fresh()
        self.gates.extend([(a, q), (b, q)])
        return q

    def neg(self, a):
        q = self.const(1)
        self.gates.append((a, q))
        return q

    def conj(self, a, b):
        q = self.fresh()
        self.gates.append((a, q) if a == b else (a, b, q))
        return q

    def add(self, a, b, zero):
        carry, result = zero, []
        for x, y in zip(a, b):
            u = self.xor(x, y)
            result.append(self.xor(u, carry))
            carry = self.xor(self.conj(x, y), self.conj(u, carry))
        return result, carry

    def sub(self, a, b, zero):
        borrow, result = zero, []
        for x, y in zip(a, b):
            u = self.xor(x, y)
            result.append(self.xor(u, borrow))
            borrow = self.xor(self.conj(self.neg(x), y),
                              self.conj(self.neg(u), borrow))
        return result, borrow

    def select(self, flag, a, b):
        return [self.xor(x, self.conj(flag, self.xor(x, y)))
                for x, y in zip(a, b)]


def evaluator(N, direction):
    n = (N - 1).bit_length()
    # Input and target registers are fixed. Other wires start at zero.
    t = list(range(n))
    b, v = n, n + 1
    y = list(range(n + 2, 2 * n + 2))
    target = list(range(2 * n + 2, 3 * n + 2))
    c = BooleanCircuit(3 * n + 2)
    zero = c.const(0)
    modulus = [c.const((N >> i) & 1) for i in range(n + 1)]
    ty, yy = t + [zero], y + [zero]
    _, tv = c.sub(ty, modulus, zero)
    _, yv = c.sub(yy, modulus, zero)
    h = c.conj(c.conj(v, b), c.conj(tv, yv))
    if direction == '-':
        difference, borrow = c.sub(yy, ty, zero)
        correction = [c.conj(borrow, q) for q in modulus]
        result, _ = c.add(difference, correction, zero)
    else:
        total, _ = c.add(yy, ty, zero)
        _, below = c.sub(total, modulus, zero)
        ge = c.neg(below)
        correction = [c.conj(ge, q) for q in modulus]
        result, _ = c.sub(total, correction, zero)
    selected = c.select(h, y, result[:n])
    forward = list(c.gates)
    gates = forward + list(zip(selected, target)) + list(reversed(forward))
    return {'n': n, 'wires': c.wires, 'gates': gates,
            't': t, 'b': b, 'v': v, 'y': y, 'target': target,
            'scratch_start': 3 * n + 2}


def apply(gates, state):
    for gate in gates:
        if len(gate) == 1:
            state[gate[0]] ^= 1
        elif len(gate) == 2:
            a, z = gate
            assert a != z
            state[z] ^= state[a]
        else:
            a, b, z = gate
            assert len({a, b, z}) == 3
            state[z] ^= state[a] & state[b]


def put(state, wires, value):
    for i, q in enumerate(wires):
        state[q] = (value >> i) & 1


def get(state, wires):
    return sum(state[q] << i for i, q in enumerate(wires))


def check_permutations():
    cases = 0
    for N in range(2, 10):
        minus, plus = evaluator(N, '-'), evaluator(N, '+')
        n, L = minus['n'], 1 << minus['n']
        for t, y, b, v in itertools.product(range(L), range(L), range(2), range(2)):
            for first, second, sign in [(minus, plus, -1), (plus, minus, 1)]:
                state = bytearray(max(first['wires'], second['wires']))
                put(state, first['t'], t)
                put(state, first['y'], y)
                state[first['b']], state[first['v']] = b, v
                expected = (y + sign*t) % N if v and b and t < N and y < N else y
                # Clean XOR evaluator, including a nonzero initial target.
                for target in (0, L - 1):
                    put(state, first['target'], target)
                    apply(first['gates'], state)
                    assert get(state, first['target']) == target ^ expected
                    assert get(state, first['y']) == y
                    assert not any(state[first['scratch_start']:])
                    apply(first['gates'], state)
                    assert get(state, first['target']) == target
                put(state, first['target'], 0)
                # In-place permutation: evaluate, swap, inverse-evaluate.
                apply(first['gates'], state)
                swaps = [(a, z) for a, z in zip(first['y'], first['target'])]
                for a, z in swaps:
                    apply([(a, z), (z, a), (a, z)], state)
                apply(second['gates'], state)
                assert get(state, first['y']) == expected
                assert get(state, first['target']) == 0
                assert not any(state[first['scratch_start']:])
                assert get(state, first['t']) == t
                assert (state[first['b']], state[first['v']]) == (b, v)
                cases += 1
    counts = []
    for n in (1, 2, 3, 4, 8, 16, 32, 64, 128):
        N = (1 << n) if n == 1 else (1 << n) - 1
        a, b = evaluator(N, '-'), evaluator(N, '+')
        gates = len(a['gates']) + 3*n + len(b['gates'])
        scratch = max(a['wires'], b['wires']) - a['scratch_start'] + n
        assert gates <= 600*n + 600
        assert scratch <= 250*n + 250
        counts.append({'n': n, 'permutation_gates': gates, 'scratch_qubits': scratch})
    return {'basis_permutation_cases': cases, 'finite_gate_counts': counts}


def check_ripple():
    cases = 0
    for width in range(1, 7):
        modulus = 1 << width
        for a, b in itertools.product(range(modulus), repeat=2):
            carry = borrow = total = diff = 0
            for i in range(width):
                x, y = (a >> i) & 1, (b >> i) & 1
                u = x ^ y
                total |= (u ^ carry) << i
                diff |= (u ^ borrow) << i
                carry = (x & y) ^ (u & carry)
                borrow = ((1 ^ x) & y) ^ ((1 ^ u) & borrow)
            assert total == (a+b) % modulus
            assert carry == (a+b >= modulus)
            assert diff == (a-b) % modulus
            assert borrow == (a < b)
            cases += 1
    return cases


def check_phases():
    for a, b, c in itertools.product(range(2), repeat=3):
        phase = a+b+c-(a ^ b)-(a ^ c)-(b ^ c)+(a ^ b ^ c)
        assert phase == 4*a*b*c
    cases = 0
    for count in range(1, 10):
        for bits in itertools.product(range(2), repeat=count):
            state = bytearray(bits + (0,) * (count - 1))
            gates = []
            acc = 0
            for j in range(1, count):
                out = count+j-1
                gates.append((acc, j, out))
                acc = out
            apply(gates, state)
            phase = -1 if state[acc] else 1
            assert phase == (-1 if all(bits) else 1)
            apply(reversed(gates), state)
            assert tuple(state[:count]) == bits and not any(state[count:])
            cases += 1
    return cases


def projector_entry(N, t, u, v):
    # A_t = (I + C_t^dagger X C_t)/2 on valid source residues.
    b, y = v
    swapped = (1, (y+t) % N) if b == 0 else (0, (y-t) % N)
    return Fraction(int(u == v) + int(u == swapped), 2)


def check_projectors():
    cases = 0
    for N in range(2, 20):
        for s, t in itertools.product(range(N), repeat=2):
            weight = Fraction(0)
            for x in range(N):
                support = [(0, x), (1, (x+s) % N)]
                weight += sum(projector_entry(N, t, u, v)
                              for u, v in itertools.product(support, repeat=2)) / (2*N)
            assert weight == (1 if s == t else Fraction(1, 2))
            for k in range(1, 7):
                assert weight**k == (1 if s == t else Fraction(1, 2**k))
            cases += 1
    return cases


def check_search():
    bounds = []
    for n in range(2, 19):
        L, k = 1 << n, n+24
        r = math.isqrt(9*L) // 4
        # Exact characterization of floor(3 sqrt(L)/4), with no real arithmetic.
        assert 16*r*r <= 9*L < 16*(r+1)*(r+1)
        # g/sqrt(L) is the marked amplitude; b/sqrt(L) each other amplitude.
        g = b = Fraction(1)
        for _ in range(r):
            g, b = ((1-Fraction(2,L))*g + Fraction(2*(L-1),L)*b,
                    -Fraction(2,L)*g + (1-Fraction(2,L))*b)
        probability = g*g/L
        assert probability + (L-1)*b*b/L == 1
        assert probability >= Fraction(25, 36)
        assert Fraction(4*r*r, 1 << k) <= Fraction(3,8192)**2
        bounds.append({'n': n, 'rounds': r, 'ideal_success_at_least_25_over_36': True})
    lower = Fraction(25,36) - Fraction(3,4096)
    assert lower == Fraction(25573,36864) and lower > Fraction(2,3)
    assert 1-Fraction(1,1 << 25) > lower
    return {'finite_search_checks': bounds, 'proved_success_lower_bound': str(lower),
            'margin_above_two_thirds': str(lower-Fraction(2,3))}


def main():
    result = {'diagnostic': 'finite exact checks, not hosted acceptance',
              'ripple_cases': check_ripple(),
              'permutations': check_permutations(),
              'conjunction_cases': check_phases(),
              'one_copy_projector_cases': check_projectors(),
              'search': check_search()}
    result['candidate_sha256'] = {
        name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
        for name in ('proof.md', 'submission.json', 'diagnostic.py')}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
