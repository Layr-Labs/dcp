# Kuperberg's arbitrary-order DCP algorithm in the challenge model

## Claim

For every N >= 2 and s in Z/NZ, ideal independent DCP coset states suffice to recover s with success probability greater than 2/3 using total work, classical space, quantum space, and source copies bounded by O(2^(10 sqrt(n)) n^10), where n=ceil(log2 N). The time growth index is 1/2. This is a cost-model translation of a published algorithm, not a new sieve discovery.

## DCP states are the algorithm's input samples

Let D_N=<x,y | x^N=y^2=1, yxy=x^(-1)> and H_s=<yx^s>. The right coset x^u H_s contains x^u and x^(u+s)y. Encode these as |0,u> and |1,u+s>. Averaging over uniform u produces exactly the DCP density operator

  rho_s = (1/N) sum_u |(|0,u>+|1,u+s>)/sqrt(2)><...|.

Thus each input sample is the standard mixed dihedral coset state. The algorithm needs no purification, no knowledge of u, and no coherent access to the source after copies are acquired. Fourier sampling the rotation register gives a uniform known label k and a phase qubit

  |psi_k> = (|0>+exp(2 pi i k s/N)|1>)/sqrt(2).

## Algorithm and correctness source

Run Kuperberg's arbitrary-order Algorithm 5.1 [1, Section 5] on these supplied samples. It filters initial Fourier labels to a short interval, pairs phase qubits with close labels, and uses CNOT plus measurement to retain a known difference-label state. Its level schedule reduces labels to the final 0/1 range. For arbitrary N, Algorithm 5.1 step 4 specifies the additional construction: factor N=2^a M with M odd; use the divisibility sieve for each j; apply the stated automorphism x -> x^(2^(-j)) on C_M; and repeat the sieve steps. The paper states that this full procedure yields the phase observations needed to recover every residue of s. We invoke the published arbitrary-order algorithm as a whole. In particular, we do not infer a target label from divisibility alone or substitute a separate, unproved label transformation.

The success and final-label distribution claim is the published result: Theorem 1.1 states that the algorithm finds the hidden reflection for every N, and the discussion after Algorithm 5.1 describes the arbitrary-order final labels 0 and 1 as almost equally likely. The algorithm's list-size/Chernoff analysis is in Theorem 3.2; the paper says that its proof carries over to Algorithm 5.1. We treat these as the correctness theorem for the exact algorithm being run, rather than claiming a new proof of the subtle balance step. This yields a constant success lower bound p0>0 for sufficiently large n. For the fixed finite prefix below that threshold, use exhaustive testing; this does not change the asymptotic bounds.

To make all loops bounded, cap each label-filtering stage at a fixed number of raw copies and each sieve list at the theorem's stated target size; an underfilled list terminates that attempt as failure. Amplify a complete attempt R times, for a fixed R with (1-p0)^R<=1/12. Verify each proposed secret t on q=ceil(log2(12R)) fresh copies by subtracting t from the second register conditioned on the first being 1, then measuring the first in the X basis. For t=s, every ideal verification returns +. For t!=s, each independent check returns + with probability 1/2. A union bound makes the chance that any wrong proposal passes at most R 2^-q<=1/12. Thus full-secret success exceeds 5/6. This configuration has no unbounded retry loop.

## Uniform filter and cost bounds

Set x=log2 N and m=floor(sqrt(x)-2), as in Algorithm 5.1. The initial kept interval has width K=2^(m^2+1). A uniform Fourier label survives with probability min(1,K/N). Since m+2<=sqrt(x)<m+3, we have m>sqrt(x)-3, so

  n-(m^2+1) <= 6 sqrt(n)+O(1).

Consequently the rejection overhead is at most 2^(6 sqrt(n)+O(1)) uniformly for every N. This bound includes orders between powers of two; the worst case is not limited to N=2^(r^2).

The sieve list-size analysis in [1] gives O(8^(sqrt(log2 N)))=O(2^(3 sqrt(n))) kept samples per target construction. To obtain L accepted labels with a fixed cutoff, acquire B=ceil(2L/p) raw copies, where p=min(1,K/N). A Chernoff bound gives probability at most exp(-L/8) of receiving fewer than L survivors. L is the algorithm's prescribed list size, so for sufficiently large n this underfill probability is below 1/12; the finite prefix is handled by exhaustive search. The total source-copy budget per target construction is therefore O(2^(9 sqrt(n)) poly(n)). Algorithm 5.1 performs O(n) target constructions and a fixed number of amplified attempts, which contributes only a polynomial factor.

The source describes quasi-linear processing in the list size. At the challenge's bit level, each label has O(n) bits; sorting/pairing, arithmetic, list indexing, controller work, and address generation add polynomial factors in n and log L. Factoring N and the CRT operations are polynomial in n. Synthesize approximate Fourier transforms with aggregate variation error at most 1/12; the required precision contributes polynomial overhead in n and log L. A conservative uniform bound for all of these operations and all acquired samples is O(2^(10 sqrt(n)) n^10). The extra square-root-exponent slack absorbs the filter, all n target constructions, bounded amplification, and polynomial implementation overhead.

There are at most Q retained samples in any live list. Storing their labels, pair indices, and level counters uses O(Qn) classical bits. The quantum implementation stores at most Q phase qubits plus O(Qn^2) arithmetic and circuit-workspace qubits. Both are bounded by the same padded envelope. The accounting includes rejected filter samples, underfilled attempts, discarded states, all Fourier and group operations, factorization, synthesis, verification, and controller/address operations on every branch.

For B(n)=2^(10 sqrt(n)) n^10, log2(log2 B(n))=(1/2)log2(n)+O(1). Each resource envelope therefore has growth index 1/2. The guarantee assumes independent ideal DCP input states, so malformed-sample tolerance is zero. No finite-size leading constant or empirical runtime is claimed.

## Reference

[1] Greg Kuperberg, “A Subexponential-Time Quantum Algorithm for the Dihedral Hidden Subgroup Problem,” SIAM Journal on Computing 35(1), 170–188 (2005), DOI: 10.1137/S0097539703436345. Algorithm 5.1 handles arbitrary N; Theorem 1.1 gives the uniform time/query result; the discussion after Algorithm 5.1 states the final-label balance and arbitrary-order residue procedure. https://www.math.ucdavis.edu/research/infovault/greg/SIAM_JC-35-05.pdf
