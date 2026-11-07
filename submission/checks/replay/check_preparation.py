#!/usr/bin/env python3
"""Independent support and reversible-arithmetic checks for partial pivots."""
from collections import defaultdict
from hashlib import sha256
from pathlib import Path
import itertools
import json
import random
import resource

HERE = Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_AS, (512 << 20,)*2)
resource.setrlimit(resource.RLIMIT_CPU, (45,)*2)


def pivot_indices(labels, b):
    result = []
    for i in range(b):
        candidates = [j for j, a in enumerate(labels) if a and (a & -a) == 1 << i]
        if not candidates:
            break
        result.append(candidates[0])
    return result


def operations(labels, pivots, residue):
    """Reversible known-constant additions and CNOTs, before gate synthesis.

    x starts with free bits arbitrary and pivot bits zero, accumulator zero.
    Every operation is reversible on the entire ambient basis, not just support.
    """
    ops = [('add', residue)]
    for j, a in enumerate(labels):
        if j not in pivots:
            ops.append(('cadd', j, -a))
    for bit, j in enumerate(pivots):
        ops.append(('cx_from_acc', bit, j))
        ops.append(('cadd', j, -labels[j]))
    return ops


def run(ops, x, accumulator, modulus, inverse=False):
    for op in reversed(ops) if inverse else ops:
        sign = -1 if inverse else 1
        if op[0] == 'add':
            accumulator = (accumulator + sign*op[1]) % modulus
        elif op[0] == 'cadd':
            accumulator = (accumulator + sign*((x >> op[1]) & 1)*op[2]) % modulus
        else:
            assert op[0] == 'cx_from_acc'
            x ^= ((accumulator >> op[1]) & 1) << op[2]
    return x, accumulator


def subset_label(labels, x, M):
    return sum(a for j, a in enumerate(labels) if (x >> j) & 1) % M


def main():
    rng = random.Random(0xD1EDA1)
    counts = dict(label_tuples=0, coarse_fibers=0, prepared_basis_states=0,
                  whole_space_inverse_cases=0, membership_recovery_columns=0,
                  full_fibers=0)
    for b in range(1, 7):
        M = 1 << b
        for q in [b+1, b+2]:
            tuples = [tuple([0]*q), tuple([1]*q),
                      tuple([1 << (i % b) for i in range(q)])]
            tuples += [tuple(rng.randrange(M) for _ in range(q)) for _ in range(32)]
            if b <= 2:
                tuples += list(itertools.product(range(M), repeat=q))
            for labels in tuples:
                counts['label_tuples'] += 1
                all_pivots = pivot_indices(labels, b)
                full = defaultdict(set)
                for x in range(1 << q):
                    full[subset_label(labels, x, M)].add(x)
                for t in range(len(all_pivots)+1):
                    pivots = all_pivots[:t]
                    mod = 1 << t
                    coarse = defaultdict(set)
                    for e, fiber in full.items():
                        coarse[e % mod].update(fiber)
                    free = [j for j in range(q) if j not in pivots]
                    for residue in range(mod):
                        ops = operations(labels, pivots, residue)
                        image = set()
                        for w in range(1 << len(free)):
                            start = sum(((w >> i) & 1) << j for i, j in enumerate(free))
                            y, scratch = run(ops, start, 0, mod)
                            assert scratch == 0
                            assert run(ops, y, 0, mod, inverse=True) == (start, 0)
                            image.add(y)
                            counts['prepared_basis_states'] += 1
                        assert len(image) == 1 << (q-t)
                        assert image == coarse[residue]
                        counts['coarse_fibers'] += 1
                        # Arbitrary pivot bits and scratch, not just promised inputs.
                        for _ in range(2):
                            start = rng.randrange(1 << q), rng.randrange(mod)
                            y, scratch = run(ops, *start, mod)
                            assert run(ops, y, scratch, mod, inverse=True) == start
                            counts['whole_space_inverse_cases'] += 1
                    for e, fiber in full.items():
                        support = coarse[e % mod]
                        assert fiber <= support
                        outside = support - fiber
                        for x in fiber:
                            marked = fiber - {x}
                            assert len(marked) == len(fiber)-1
                            # Each failure output is either diagonal or in the same
                            # outside set for EVERY x. Thus all recovery Kraus columns
                            # share the same scalar in the Grover amplitude formula.
                            assert support - marked == {x} | outside
                            assert x ^ x == 0
                            counts['membership_recovery_columns'] += 1
                        counts['full_fibers'] += 1
    result = dict(status='PASS', counts=counts,
        limits=dict(address_space_bytes=512 << 20, cpu_seconds=45),
        scope='Exact support, inverse arithmetic and recovery partitions. Not a compiled Clifford+T circuit or all-N DCP proof.',
        script_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
    (HERE/'preparation-results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
