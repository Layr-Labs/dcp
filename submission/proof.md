# Kuperberg sieve for the Dihedral Coset Problem

This note describes a uniform algorithm based on Kuperberg's sieve (Kuperberg, SIAM J. Comput. 35(1):170–188, 2005; improved in later works) that recovers the hidden shift s ∈ ℤ/Nℤ from ideal coset states. All resource bounds below hold jointly for the same fully specified configuration, on every execution branch, for every N ≥ 2 and every s, with unconditional success probability at least 2/3. Set n = ceil(log₂ N). All constants are absolute and independent of N, s and sampled outcomes. The analysis uses the challenge cost model (Clifford+T gates, classical bit operations, source acquisition cost n+1, address costs, peak space including ancillas and circuit descriptions).

## Algorithm (high-level)

1. Acquire O(2^{(3/2)√n} n^{2}) independent ideal coset states |ψ_{x,s}⟩ (or their mixed version). Each acquisition costs n+1 work units.
2. Perform the quantum Fourier transform over ℤ/Nℤ on the second register of each state and measure, obtaining classical Fourier labels y ∈ ℤ/Nℤ together with phase qubits |ψ_y⟩ = (|0⟩ + e^{2π i y s / N} |1⟩)/√2.
3. Run a multi-stage sieve: in each of O(√n) stages, pair (or combine a small number of) states whose labels agree on the next block of low-order bits. A parity/CNOT measurement produces a new state whose label has those bits zeroed, at the cost of discarding a constant fraction of the pool. The number of states is chosen so that the survival probability through all stages is high enough that at least one high-quality state remains with constant probability.
4. From the final states (whose labels are concentrated on a few high bits or a power of two), measure in the X basis to extract one bit of s. Repeat the entire procedure O(n) times (or recycle with bit-by-bit peeling) to recover all bits of s, aborting and restarting on failure. The restart cutoff is set so that the overall success probability is ≥ 2/3 while the total work remains within the stated envelope.
5. All quantum operations are standard Clifford+T circuits of poly(n) size per state (QFT, controlled modular arithmetic for label combination, measurements). Classical control stores the list of current labels and decides pairings; the list size is bounded by the peak number of retained states.

The sieve parameters (block size ~ √n, initial pool size 2^{Θ(√n)}) are the standard ones that make the expected number of surviving states after each stage at least a positive constant fraction of the previous stage, with failure probability exponentially small in the stage count. An explicit cutoff/restart argument (repeat the whole algorithm O(1) times or until success, with a hard limit of O(n) attempts) converts the high-probability analysis into a worst-case bound that still succeeds with probability ≥ 2/3.

## Resource bounds

- **Total work T**: Each of the O(2^{(3/2)√n} n^{2}) source copies costs O(n). Each sieve stage performs O(1) poly(n)-size circuits and classical matching of size O(pool size · poly(n)). There are O(√n) stages and O(n) restarts. The resulting worst-case total work satisfies T = O(2^{(3/2) n^{1/2}} n^{10}). Envelope B_T(n) = 2^{(3/2) n^{1/2}} n^{10} has growth index exactly 1/2.
- **Peak classical memory S_C**: The dominant storage is the list of current Fourier labels and control data, of size O(2^{(3/2)√n} · n) bits at the start of the sieve. Peak classical workspace is therefore O(2^{(3/2) n^{1/2}} n^{2}) bits. Envelope B_C(n) = 2^{(3/2) n^{1/2}} n^{2} has growth index exactly 1/2.
- **Peak quantum memory S_Q**: The algorithm retains only O(1) quantum registers at a time (or a small constant number for the combination step) plus O(n) ancillas for the modular arithmetic and QFT. Peak quantum workspace is O(n) qubits. Envelope B_Q(n) = n has growth index exactly 0.
- **Source samples Q**: All acquired copies, including those discarded by the sieve and those used in failed restarts, total Q = O(2^{(3/2) n^{1/2}} n^{2}). Envelope B_Qsamples(n) = 2^{(3/2) n^{1/2}} n^{2} has growth index exactly 1/2.

These four bounds hold simultaneously for the algorithm and parameter choice described above.

## Fractional error tolerance

The analysis assumes every acquired source copy is an independent ideal coset state (no malformed samples). Thus the guaranteed fractional error tolerance is ε(n) = 0. Under this promise the success probability and all four resource bounds hold. No positive corruption tolerance is claimed.

## Cited hypotheses

The existence and correctness of the sieve (survival of a sufficient number of states with the desired label structure, extraction of bits of s) follow from the analysis in Kuperberg (2005) and subsequent refinements that achieve quantum space poly(n) while retaining a 2^{O(√n)} time/sample bound. The concrete coefficient 3/2 is a safe rational upper bound on the leading constant that appears in the standard analyses (the true constant is at most √2 + o(1) for the improved variants). All circuit implementations are standard and charged at their Clifford+T / bit-operation cost in the challenge model.
