# Sequential shift tests with a deterministic cutoff

## Theorem and assumptions

For every integer N >= 2, put n = ceil(log2 N). The input is N in binary and a sequence of independent copies of the ideal state rho_s specified in rules.md, for a fixed but arbitrary s in Z/NZ. The algorithm below returns s with probability at least 2/3. On every branch it uses at most 48N copies and O(N n^3) total charged work, O(n^2) classical bits, and O(n^2) qubits. The constants are absolute. It makes no claim of robustness to malformed samples. In particular the guaranteed malformed fraction is 0; this is not a statement that positive tolerance is impossible. The elementary probability arguments and circuit construction below are self-contained; no external theorem is used as a black box except the standard exact constant-size Clifford+T implementation of Toffoli, specified in the baseline in this repository.

## Algorithm

Set k=n+4 and a sample counter to zero. For t=0,1,...,N-1, run up to k tests sequentially, stopping this candidate immediately upon a minus result. Before each test, if the counter is 48N, output 0 and halt; otherwise increment it and acquire a fresh source copy. Apply controlled subtraction of t modulo N to the second register, conditioned on first qubit 1. Measure the first qubit in the X basis and discard the whole sample. If the result is minus, move to the next t; if k consecutive results are plus, output t and halt. If all candidates are exhausted, output 0. All control and arithmetic are uniform, with no advice.

## Correctness and cutoff

After controlled subtraction, each component of an ideal source copy is

    (|0,x> + |1,(x+s-t) mod N>)/sqrt(2).

If t=s, the first qubit is |+> and every test returns plus. If t differs from s, the two second-register basis states are distinct; the first qubit is maximally mixed and each test returns plus with probability exactly 1/2. This holds after averaging over x. The fresh copies make the outcomes independent, even conditioned on the past.

Couple the algorithm to an uncapped process that tests candidates in the same order, and imagine an independent infinite outcome sequence for each candidate. For each wrong candidate let X_t be the number of tests until the first minus, truncated at k. Then E[X_t]=sum_{j=1}^k 2^{-(j-1)} < 2. The uncapped process has an erroneous output only if some wrong candidate has k pluses; a union bound gives probability at most (N-1)2^{-k} < 1/16 because N <= 2^n. Regardless of whether the uncapped process stops earlier due to an erroneous candidate, the number of tests it would perform is bounded above by W = k + sum_{t != s} X_t. The term k allows all tests of the true candidate, whether or not it is reached. By linearity E[W] < 2(N-1)+n+4 <= 5N, using n+4 <= 3N for every N>=2. Markov's inequality gives Pr(W>48N) < 5/48. If W <= 48N the cutoff never prevents the uncapped output. A union bound therefore gives failure probability less than 1/16 + 5/48 = 1/6, and success greater than 5/6. This argument counts all tests on all candidates, including those which are not actually reached in a branch; it does not condition on successful execution or assume free restarts.

## Circuit implementation and joint resource bounds

For n-bit y, define f_t(y)=(y-t) mod N for y<N and f_t(y)=y for y>=N. This is a permutation, with inverse adding t modulo N on the valid range. Comparisons, conditional addition and subtraction on n+1 bits have uniform Boolean circuits with O(n) constant-fan-in gates and O(n) intermediate bits. Reversibly evaluate the circuit using NOT, CNOT and Toffoli, copy its output to a fresh register, and reverse the evaluation. Evaluate the inverse in the standard compute-swap-uncompute construction to implement the permutation in place; condition the operations on the first qubit. Toffoli and its constantly controlled variants have exact constant-size Clifford+T decompositions. This yields O(n) elementary gates and O(n) temporary wires, and in particular O(n^2) of each is a conservative bound. The X measurement uses a Hadamard and a computational-basis measurement. Ancillas and the used sample are reset or discarded before the next test.

A uniform controller generates each gate from N,t and binary counters using O(n^2) classical workspace and at most O(n^3) bit operations per test, conservatively accounting for the O(n^2) gate bound, address calculations, fixed-gate synthesis, initialization, measurement and access to O(n^2) allocated bits and qubits. The counter up to 48N, k, and loop variables use O(n) bits. Source acquisition costs n+1 work, included in O(n^3). There are at most 48N tests on every branch; final bookkeeping also fits O(N n^3). Thus T=O(N n^3) subset O(2^n n^3), S_C=O(n^2), S_Q=O(n^2), and Q<=48N=O(2^n). The sample count includes every acquired copy, including copies from unsuccessful tests and the last allowed test. No quantum addressed memory or hidden oracle is used. All four bounds hold simultaneously with the success proof above.

For 2^n n^3 and 2^n the growth index as defined in rules.md is 1; for n^2 it is 0. Therefore the four indices are 1,0,0,1. The explicit improvement over the provided exhaustive-search baseline is a factor n in the stated uniform work envelope and in its sample envelope; this is not a solution of the 2^{O(n^{1/3})} research goal.
