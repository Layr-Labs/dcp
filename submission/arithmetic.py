"""Streamed exact arithmetic for the known controlled Grover walk.

Only a single O(n)-gate arithmetic subroutine is materialized at a time.
The full exponentially repeated walk is not stored as a circuit listing.
"""
from dataclasses import dataclass


class BooleanEvaluation:
    def __init__(self, first_scratch):
        self.next = first_scratch
        self.gates = []
        self.zero = self.fresh()
        self.one = self.fresh()
        self.gates.append(('X', self.one))

    def fresh(self):
        out = self.next
        self.next += 1
        return out

    def xor(self, *bits):
        out = self.fresh()
        self.gates.extend(('CX', b, out) for b in bits)
        return out

    def conjunction(self, a, b):
        out = self.fresh()
        self.gates.append(('CX', a, out) if a == b else ('CCX', a, b, out))
        return out

    def add(self, a, b):
        carry, result = self.zero, []
        for x, y in zip(a, b):
            result.append(self.xor(x, y, carry))
            carry = self.xor(self.conjunction(x, y),
                             self.conjunction(x, carry),
                             self.conjunction(y, carry))
        return result, carry

    def constant(self, value, width, control=None):
        bits = format(value, f'0{width}b')
        assert len(bits) == width
        return [(self.one if control is None else control)
                if bit == '1' else self.zero for bit in reversed(bits)]

    def select(self, flag, yes, no):
        return self.xor(no, self.conjunction(flag, self.xor(yes, no)))


def evaluate_mod_add(n, N, c, inputs, control, outputs, scratch_start):
    ev = BooleanEvaluation(scratch_start)
    width = n + 1
    padded = list(inputs) + [ev.zero]
    raw, _ = ev.add(padded, ev.constant(c % N, width, control))
    subtraction = ev.constant((1 << width) - N, width)
    reduced, wrap = ev.add(raw, subtraction)
    _, invalid = ev.add(padded, subtraction)
    result = [ev.select(invalid, inputs[i], ev.select(wrap, reduced[i], raw[i]))
              for i in range(n)]
    gates = ev.gates + [('CX', a, b) for a, b in zip(result, outputs)] + ev.gates[::-1]
    return gates, ev.next


def mod_add_circuit(n, N, c):
    """Controlled F_c, identity on encodings >=N, with clean extra wires."""
    assert 2 <= N <= 1 << n and 0 <= c < N
    inputs, control = list(range(n)), n
    outputs = list(range(n + 1, 2 * n + 1))
    first, q1 = evaluate_mod_add(n, N, c, inputs, control, outputs, 2*n+1)
    second, q2 = evaluate_mod_add(n, N, 0 if c == 0 else N-c, inputs, control, outputs, 2*n+1)
    swaps = [g for a, b in zip(inputs, outputs)
             for g in [('CX', a, b), ('CX', b, a), ('CX', a, b)]]
    return first + swaps + second, max(q1, q2)


def run_boolean(gates, basis):
    phase = 1
    for op, *wires in gates:
        if op == 'X': basis ^= 1 << wires[0]
        elif op == 'CX':
            if basis >> wires[0] & 1: basis ^= 1 << wires[1]
        elif op == 'CCX':
            if all(basis >> w & 1 for w in wires[:2]): basis ^= 1 << wires[2]
        elif op == 'Z':
            if basis >> wires[0] & 1: phase *= -1
        elif op == 'CZ':
            if all(basis >> w & 1 for w in wires): phase *= -1
        else: raise ValueError(op)
    return basis, phase


@dataclass(frozen=True)
class GroverLayout:
    n: int
    m: int
    adder_qubits: int

    @property
    def sum_qubits(self): return self.m + self.adder_qubits - 1
    @property
    def target(self): return tuple(range(self.sum_qubits, self.sum_qubits + self.n))
    @property
    def control(self): return self.sum_qubits + self.n
    @property
    def diffusion_scratch(self): return tuple(range(self.control + 1, self.control + self.m))
    @property
    def qubits(self): return self.control + max(1, self.m)


def layout(labels, N):
    n = (N-1).bit_length()
    return GroverLayout(n, len(labels), mod_add_circuit(n, N, 0)[1])


def sum_gates(labels, N, loc, inverse=False):
    n, m = loc.n, loc.m
    order = reversed(range(m)) if inverse else range(m)
    for i in order:
        gates, used = mod_add_circuit(n, N, labels[i])
        assert used <= loc.adder_qubits
        mapping = list(range(m, m+n)) + [i] + list(range(m+n, m+used-1))
        assert len(mapping) == used
        for gate in (reversed(gates) if inverse else gates):
            yield (gate[0], *(mapping[w] for w in gate[1:]))


def controlled_zero_phase(wires, control, scratch):
    wires = list(wires)
    yield from (('X', w) for w in wires)
    chain = []
    if len(wires) == 1:
        flag = wires[0]
    else:
        chain.append(('CCX', wires[0], wires[1], scratch[0]))
        for i in range(2, len(wires)):
            chain.append(('CCX', scratch[i-2], wires[i], scratch[i-1]))
        flag = scratch[len(wires)-2]
    yield from chain
    yield ('CZ', control, flag)
    yield from reversed(chain)
    yield from (('X', w) for w in wires)


def marking_gates(labels, N, loc):
    yield from sum_gates(labels, N, loc)
    sums = list(range(loc.m, loc.m+loc.n))
    for a, b in zip(loc.target, sums): yield ('CX', a, b)
    scratch = list(range(loc.m+loc.n, loc.m+2*loc.n))
    yield from controlled_zero_phase(sums, loc.control, scratch)
    for a, b in zip(loc.target, sums): yield ('CX', a, b)
    yield from sum_gates(labels, N, loc, inverse=True)


def diffusion_gates(loc, correct_sign=True):
    yield from (('H', i) for i in range(loc.m))
    yield from controlled_zero_phase(range(loc.m), loc.control, loc.diffusion_scratch)
    yield from (('H', i) for i in range(loc.m))
    if correct_sign:
        yield ('Z', loc.control)


def controlled_grover_gates(labels, N, inverse=False, correct_sign=True):
    loc = layout(labels, N)
    if inverse:
        yield from diffusion_gates(loc, correct_sign)
        yield from marking_gates(labels, N, loc)
    else:
        yield from marking_gates(labels, N, loc)
        yield from diffusion_gates(loc, correct_sign)
