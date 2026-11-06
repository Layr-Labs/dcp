#!/usr/bin/env python3
"""Finite exact diagnostics for proof.md; not the asymptotic implementation."""
import hashlib
import itertools
import json
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
    cases = 0
    for a, b, c in itertools.product(range(2), repeat=3):
        phase = a+b+c-(a ^ b)-(a ^ c)-(b ^ c)+(a ^ b ^ c)
        assert phase == 4*a*b*c
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


class Span:
    """Constant-size address formula, with an optional leading-zero wire."""
    def __init__(self, start, length, stride=1, padding=None):
        self.start, self.length = start, length
        self.stride, self.padding = stride, padding

    def __len__(self):
        return self.length + (self.padding is not None)

    def __getitem__(self, i):
        if i == self.length and self.padding is not None:
            return self.padding
        assert 0 <= i < self.length
        return self.start + self.stride*i

    def padded(self, zero):
        return Span(self.start, self.length, self.stride, zero)


class StreamCircuit:
    """Fixed-many sweep records; each yielded descriptor has constant arity.

    Python models the grammar, not the proof's per-bit execution costs.
    No per-gate or per-bit pointer table is retained by this generator.
    """
    def __init__(self, inputs):
        self.wires, self.blocks = inputs, []

    def block(self, kind, length, size, *args):
        base = self.wires
        self.wires += length*size
        self.blocks.append((kind, length, size, base, args))
        return base

    def constants(self, length, value):
        return Span(self.block('constant', length, 1, value), length)

    def conj(self, a, b):
        return self.block('and', 1, 1, a, b)

    def sub(self, a, b, zero):
        w = len(a)
        base = self.block('sub', w, 7, a, b, zero)
        return Span(base+1, w, 7), base+7*(w-1)+6

    def add(self, a, b, zero):
        w = len(a)
        base = self.block('add', w, 5, a, b, zero)
        return Span(base+1, w, 5), base+5*(w-1)+4

    def mask(self, flag, a):
        return Span(self.block('mask', len(a), 1, flag, a), len(a))

    def negate(self, a):
        return self.block('not', 1, 1, a)

    def select(self, flag, a, b):
        return Span(self.block('select', len(a), 3, flag, a, b)+2, len(a), 3)

    def gates(self, reverse=False):
        def and_gate(a, b, z):
            return (a, z) if a == b else (a, b, z)
        blocks = reversed(self.blocks) if reverse else iter(self.blocks)
        for kind, length, size, base, args in blocks:
            positions = range(length-1, -1, -1) if reverse else range(length)
            for i in positions:
                z = base+size*i
                if kind == 'constant':
                    small = [(z,)] if (args[0] >> i) & 1 else []
                elif kind == 'and':
                    small = [and_gate(*args, z)]
                elif kind == 'not':
                    small = [(z,), (args[0], z)]
                elif kind == 'mask':
                    flag, a = args
                    small = [and_gate(flag, a[i], z)]
                elif kind == 'select':
                    flag, a, b = args
                    small = [(a[i], z), (b[i], z), and_gate(flag, z, z+1),
                             (a[i], z+2), (z+1, z+2)]
                else:
                    a, b, zero = args
                    x, y = a[i], b[i]
                    previous = zero if i == 0 else z-1
                    small = [(x, z), (y, z), (z, z+1), (previous, z+1)]
                    if kind == 'add':
                        small += [and_gate(x, y, z+2), and_gate(z, previous, z+3),
                                  (z+2, z+4), (z+3, z+4)]
                    else:
                        assert kind == 'sub'
                        small += [(z+2,), (x, z+2), and_gate(z+2, y, z+3),
                                  (z+4,), (z, z+4), and_gate(z+4, previous, z+5),
                                  (z+3, z+6), (z+5, z+6)]
                yield from (reversed(small) if reverse else small)


def streamed_evaluator(N, direction):
    n = (N-1).bit_length()
    t, y, target = Span(0, n), Span(n+2, n), Span(2*n+2, n)
    b, v = n, n+1
    c = StreamCircuit(3*n+2)
    zero = c.constants(1, 0)[0]
    modulus = c.constants(n+1, N)
    ty, yy = t.padded(zero), y.padded(zero)
    _, tv = c.sub(ty, modulus, zero)
    _, yv = c.sub(yy, modulus, zero)
    h = c.conj(c.conj(v, b), c.conj(tv, yv))
    if direction == '-':
        difference, borrow = c.sub(yy, ty, zero)
        result, _ = c.add(difference, c.mask(borrow, modulus), zero)
    else:
        total, _ = c.add(yy, ty, zero)
        _, below = c.sub(total, modulus, zero)
        ge = c.negate(below)
        result, _ = c.sub(total, c.mask(ge, modulus), zero)
    selected = c.select(h, y, Span(result.start, n, result.stride))

    def gates():
        yield from c.gates()
        for i in range(n):
            yield selected[i], target[i]
        yield from c.gates(reverse=True)
    return c, gates


def check_streaming():
    rows = []
    for n in (1, 2, 3, 4, 8, 16, 32, 64, 128):
        for N in sorted({1 << n, max(2, (1 << n)-1)}):
            for direction in ('-', '+'):
                reference = evaluator(N, direction)
                circuit, stream = streamed_evaluator(N, direction)
                assert circuit.wires == reference['wires']
                assert list(stream()) == reference['gates']
                assert len(circuit.blocks) <= 15
                rows.append({'n': n, 'direction': direction,
                             'sweep_records': len(circuit.blocks),
                             'gates': len(reference['gates'])})
    return rows


def before_acquisition(N, cap, state):
    t, j, q = state
    if t == N or (cap is not None and q == cap):
        return 0, q
    assert 0 <= t < N and (cap is None or q < cap)
    return None


def after_test(k, state, plus):
    t, j, q = state
    q += 1
    if not plus:
        return (t+1, 0, q), None
    j += 1
    if j == k:
        return None, (t, q)
    return (t, j, q), None


def distribution(N, s, cap):
    """Exact branch distribution of output and copies, with fresh test laws."""
    n, k = (N-1).bit_length(), (N-1).bit_length()+4
    active, terminal = {(0, 0, 0): Fraction(1)}, {}
    while active:
        following = {}
        for state, mass in active.items():
            stopped = before_acquisition(N, cap, state)
            if stopped is not None:
                terminal[stopped] = terminal.get(stopped, 0)+mass
                continue
            outcomes = [(True, Fraction(1))] if state[0] == s else [
                (True, Fraction(1, 2)), (False, Fraction(1, 2))]
            for plus, p in outcomes:
                nxt, stopped = after_test(k, state, plus)
                if stopped is not None:
                    terminal[stopped] = terminal.get(stopped, 0)+mass*p
                else:
                    following[nxt] = following.get(nxt, 0)+mass*p
        active = following
    assert sum(terminal.values()) == 1
    assert all(q <= N*k and (cap is None or q <= cap) for _, q in terminal)
    return terminal


def check_search():
    cases, boundary_cases, worst = 0, 0, Fraction(1)
    for N in range(2, 13):
        n, k = (N-1).bit_length(), (N-1).bit_length()+4
        for s in range(N):
            uncapped = distribution(N, s, None)
            mean = sum(q*p for (_, q), p in uncapped.items())
            expectation_bound = 2*(N-1)*(1-Fraction(1, 1 << k))+k
            assert mean <= expectation_bound <= 4*N
            for cap in sorted({1, k-1, k, k+1, 2*N, 128*N}):
                capped = distribution(N, s, cap)
                coupled = {}
                for (out, q), mass in uncapped.items():
                    key = (out, q) if q <= cap else (0, cap)
                    coupled[key] = coupled.get(key, 0)+mass
                assert capped == coupled
                tail = sum(p for (_, q), p in uncapped.items() if q > cap)
                assert tail <= mean/cap
                if cap == 128*N:
                    success = sum(p for (out, q), p in capped.items() if out == s)
                    bound = 1-Fraction(N-1, 1 << k)-expectation_bound/cap
                    assert success >= bound > Fraction(29, 32)
                    worst = min(worst, success)
                cases += 1
        # Acceptance at precisely B occurs before the next acquisition check.
        state = (N-1, k-1, 128*N-1)
        nxt, terminal = after_test(k, state, True)
        assert nxt is None and terminal == (N-1, 128*N)
        assert before_acquisition(N, 128*N, (0, 0, 128*N)) == (0, 128*N)
        boundary_cases += 2
    # A succinct, positive-probability clean-input branch reaches the true cap.
    # Every wrong candidate has k-1 plus results then a minus. Secret is N-1.
    traces = []
    for n in (125, 126, 128, 256):
        N, k = (1 << (n-1))+1, n+4
        B = 128*N
        rejected, passed = divmod(B-1, k)
        assert rejected < N-1 and B <= N*k
        state = (rejected, passed, B-1)
        assert before_acquisition(N, B, state) is None
        nxt, terminal = after_test(k, state, passed < k-1)
        assert terminal is None and nxt[2] == B
        assert before_acquisition(N, B, nxt) == (0, B)
        assert (N-1).bit_length() == n and B.bit_length() <= n+8
        traces.append({'n': n, 'cap_reached': True,
                       'budget_bits': B.bit_length(), 'synthetic_trace': True})
    return {'exact_distribution_cases': cases, 'boundary_cases': boundary_cases,
            'small_case_minimum_success': str(worst),
            'uniform_proved_success_strictly_greater_than': '29/32',
            'production_cutoff_trace_checks': traces}
def main():
    result = {'diagnostic': 'finite exact checks, not hosted acceptance',
              'ripple_cases': check_ripple(),
              'permutations': check_permutations(),
              'exact_toffoli_phase_cases': check_phases(),
              'one_copy_projector_cases': check_projectors(),
              'streamed_descriptor_checks': check_streaming(),
              'capped_sequential_search': check_search()}
    result['candidate_sha256'] = {
        name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
        for name in ('proof.md', 'submission.json', 'diagnostic.py')}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
