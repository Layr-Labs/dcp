# Subsampled pair buckets for robust terminal decoding

The single algorithm is specified in pair-buckets.md. That file gives
the actual parameters and overrides the archives' root trees, sample
budgets, wrappers, and score thresholds. The archives supply the
native Fourier-label instrument, arbitrary-modulus phase reductions,
exact reversible scoring, and finite verified Grover schedule.

For n=ceil(log2 N) and every secret modulo N, the algorithm recovers
the full secret with probability at least 7/8 at fixed-position
malformed fraction 1/16777216. Its simultaneous worst-branch
envelopes are O(2^(n/3) n^5) sequential work, O(n^2) classical bits,
O(n) qubits, and O(2^(n/3) n) acquired copies. The growth indices
are 1, 0, 0, 1. The clean systems' reduced state must be the ideal
product, as in the structured corruption model.
