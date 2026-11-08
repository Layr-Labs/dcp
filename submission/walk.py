"""Streamed exact controlled two-reflection walk for PFD-N1.

Arithmetic bodies of O(n) gates are the largest materialized templates.
The exponential repetition stream is never collected in production.
"""
from dataclasses import dataclass
from arithmetic import (layout as arithmetic_layout, sum_gates,
                        controlled_zero_phase)


@dataclass(frozen=True)
class WalkLayout:
    arithmetic: object

    @property
    def outer_control(self): return self.arithmetic.qubits
    @property
    def block(self): return self.arithmetic.qubits + 1
    @property
    def qubits(self): return self.arithmetic.qubits + 2


def layout(labels, N):
    return WalkLayout(arithmetic_layout(labels, N))


def plus_reflection(loc, inverse=False, correct_sign=True):
    if inverse and correct_sign:
        yield ('Z', loc.control)
    order = reversed(range(loc.m)) if inverse else range(loc.m)
    yield from (('H', i) for i in order)
    small = list(controlled_zero_phase(range(loc.m), loc.control, loc.diffusion_scratch))
    yield from (reversed(small) if inverse else small)
    order = reversed(range(loc.m)) if inverse else range(loc.m)
    yield from (('H', i) for i in order)
    if not inverse and correct_sign:
        yield ('Z', loc.control)


def target_reflection(labels, N, loc, inverse=False, correct_sign=True):
    if inverse and correct_sign:
        yield ('Z', loc.control)
    yield from sum_gates(labels, N, loc)
    sums = tuple(range(loc.m, loc.m + loc.n))
    pairs = tuple(zip(loc.target, sums))
    yield from (('CX', a, b) for a, b in (reversed(pairs) if inverse else pairs))
    small = list(controlled_zero_phase(sums, loc.control, range(loc.m + loc.n, loc.m + 2 * loc.n)))
    yield from (reversed(small) if inverse else small)
    yield from (('CX', a, b) for a, b in (reversed(pairs) if inverse else pairs))
    yield from sum_gates(labels, N, loc, inverse=True)
    if not inverse and correct_sign:
        yield ('Z', loc.control)


def selected_reflection(labels, N, position, which, inverse=False, correct_sign=True):
    loc = position.arithmetic
    if which == 0:
        yield ('X', position.block)
    yield ('CCX', position.outer_control, position.block, loc.control)
    if which == 0:
        yield ('X', position.block)
        yield from plus_reflection(loc, inverse, correct_sign)
        yield ('X', position.block)
    else:
        yield from target_reflection(labels, N, loc, inverse, correct_sign)
    yield ('CCX', position.outer_control, position.block, loc.control)
    if which == 0:
        yield ('X', position.block)


def controlled_walk_gates(labels, N, inverse=False, wrong_target_phase=False):
    pos = layout(labels, N)
    if inverse:
        yield ('CZ', pos.outer_control, pos.block)
    yield ('H', pos.block)
    for which in ((1, 0) if inverse else (0, 1)):
        yield from selected_reflection(labels, N, pos, which, inverse,
                                       not (wrong_target_phase and which == 1))
    yield ('H', pos.block)
    if not inverse:
        yield ('CZ', pos.outer_control, pos.block)


def parameters(N):
    assert isinstance(N, int) and N >= 2
    n = (N - 1).bit_length()
    m = n + 1
    q_lab = n + (m - 1).bit_length() + 11
    p = (m + 1) // 2 + 26
    return {'n': n, 'm': m, 'q_lab': q_lab, 'p': p,
            'rotation_bound': 20 * (m + 3) * (q_lab + p + 3) ** 2}


def power_schedule(p, inverse=False):
    """Descriptors for controlled W^(2^r). Repetitions are real loop iterations."""
    assert p >= 2
    for bit in (reversed(range(p)) if inverse else range(p)):
        yield bit, 1 << bit, inverse


def sign_phase_gates(phase_register):
    assert len(phase_register) >= 2
    yield ('Z', phase_register[-1])
    yield ('Z', phase_register[-2])


def decoded_source_label(j, grid, N):
    return ((2 * N * j + grid) // (2 * grid)) % N


def decoded_secret(j, grid, N):
    return (-decoded_source_label(j, grid, N)) % N
