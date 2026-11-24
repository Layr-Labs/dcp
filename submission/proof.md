# Fixed source slots with robust coherent terminal decoding

The full algorithm and joint guarantees are in root-slots.md. In
particular, it uses a single stage controller, with fixed consecutive
source slots and bounded-score contamination analysis. The mathematical
input promise is fixed malformed positions chosen before private
randomness, with the exact ideal product marginal on clean positions.

The base13.md archive supplies the finite shadow procedure, native
Fourier label extraction, and the low-residue combiner implementation
and marginal law. The terminal-block.md archive supplies the two-branch
modulus split and the centered odd-stage grids. The coherent-search.md
archive supplies the two-level integer profile and exact bounded
coherent search and score implementation. When the archives give a
different wrapper, clean-only error calculation, stage sample count,
or branch count, the explicit root-slots.md rules apply. In particular
the full signed Fourier label column in the residual stages permits
calculating all prefix-dependent scores from locally gathered records.

For every modulus N >= 2, the probability of recovering the entire
secret is at least 7/8 with all costs enforced branchwise, at fraction
1/(524288*n^2), where n=ceil(log2 N). The work, classical bits,
qubits, and acquired copies respectively have asymptotic envelopes
O(2^(n/6) n^(103/30)), O(n^2), O(n), and O(n^3).

The score uses the linear-space reversible integer arithmetic in
fast-score-arithmetic.md for all candidate modular products.
