"""Finite sanity checks for proof.md, not an unbounded proof or resource test.

This diagnostic stores circuits for classical simulation; SEST-1 streams the
affine-address schedules in proof.md. No external dependencies or inputs.
"""

from fractions import Fraction
from itertools import product
import json


class BooleanCircuit:
    def __init__(self, n, modulus, candidate, inverse):
        self.n = n
        self.width = n + 1
        self.ops = []
        self.next_wire = n + 3
        self.control, self.zero, self.one = n, n + 1, n + 2
        y = list(range(n)) + [self.zero]
        N, t = self.constant(modulus), self.constant(candidate)
        if inverse:
            w, _ = self.add(y, t, self.zero)
            nN = self.notword(N)
            d, b = self.add(w, nN, self.one)
            u = self.mux(b, w, d)
        else:
            nt = self.notword(t)
            d, b = self.add(y, nt, self.one)
            r, _ = self.add(d, N, self.zero)
            u = self.mux(b, r, d)
            nN = self.notword(N)
        _, a = self.add(y, nN, self.one)
        v = self.emit('not', a)
        q = self.emit('and', self.control, v)
        self.output = self.mux(q, y[:n], u[:n])

    def constant(self, value):
        return [self.one if value >> i & 1 else self.zero
                for i in range(self.width)]

    def emit(self, op, *inputs):
        target = self.next_wire
        self.next_wire += 1
        self.ops.append((op, inputs, target))
        return target

    def notword(self, value):
        return [self.emit('not', a) for a in value]

    def add(self, left, right, carry):
        result = []
        for a, b in zip(left, right):
            p = self.emit('xor', a, b)
            d = self.emit('xor', p, carry)
            u = self.emit('and', a, b)
            v = self.emit('and', p, carry)
            carry = self.emit('xor', u, v)
            result.append(d)
        return result, carry

    def mux(self, q, left, right):
        result = []
        for a, b in zip(left, right):
            e = self.emit('xor', a, b)
            h = self.emit('and', q, e)
            result.append(self.emit('xor', a, h))
        return result

    def oracle(self, control, value, target):
        bits = [0] * self.next_wire
        for i in range(self.n):
            bits[i] = value >> i & 1
        bits[self.control], bits[self.one] = control, 1

        def toggle(instruction):
            op, inputs, output = instruction
            a = bits[inputs[0]]
            if op == 'not':
                bit = a ^ 1
            elif op == 'xor':
                bit = a ^ bits[inputs[1]]
            else:
                bit = a & bits[inputs[1]]
            bits[output] ^= bit

        for instruction in self.ops:
            toggle(instruction)
        result = target
        for i, wire in enumerate(self.output):
            result ^= bits[wire] << i
        for instruction in reversed(self.ops):
            toggle(instruction)
        assert not any(bits[self.n + 3:]), 'scratch did not clear'
        assert sum(bits[i] << i for i in range(self.n)) == value
        assert bits[self.control] == control
        assert bits[self.zero] == 0 and bits[self.one] == 1
        return result


def main():
    cases = configurations = 0
    for N in range(2, 34):
        n = (N - 1).bit_length()
        m = n + 1
        for t in range(N):
            minus = BooleanCircuit(n, N, t, False)
            plus = BooleanCircuit(n, N, t, True)
            assert len(minus.ops) == 20 * m + 3 * n + 2
            assert len(plus.ops) == 19 * m + 3 * n + 2
            for c, y in product(range(2), range(1 << n)):
                expected = (y - t) % N if c and y < N else y
                shifted = minus.oracle(c, y, 0)
                assert shifted == expected
                assert plus.oracle(c, shifted, 0) == y
                assert plus.oracle(c, shifted, y) == 0
                expected_plus = (y + t) % N if c and y < N else y
                assert plus.oracle(c, y, 0) == expected_plus
                cases += 1
            configurations += 1
        per_false = 1 - Fraction(1, 1 << (n + 2))
        for secret in range(N):
            assert per_false ** secret > Fraction(3, 4)
    for a, b, c in product(range(2), repeat=3):
        phase = a + b + c - (a ^ b) - (a ^ c) - (b ^ c) + (a ^ b ^ c)
        assert phase == 4 * a * b * c
    print(json.dumps({'status': 'pass', 'moduli': '2 through 33 inclusive',
                      'candidate_configurations': configurations,
                      'controlled_basis_cases': cases,
                      'phase_identity_cases': 8,
                      'scope': 'finite sanity check; no mathematical acceptance'},
                     sort_keys=True))


if __name__ == '__main__':
    main()
