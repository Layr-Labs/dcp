# Arbitrary-order Kuperberg sieve for DCP

## Claim

For every cyclic order N >= 2 and secret s in Z/NZ, the independent DCP coset-state source can be decoded with success probability at least 2/3 using total work, classical space, quantum space, and source copies bounded by O(2^(3 sqrt(n)) n^10), where n=ceil(log2 N). The time growth index is 1/2. This is a translation of a known subexponential algorithm into the challenge's uniform cost model, not a claim of a new sieve.

## Exact input correspondence

Write D_N=<x,y | x^N=y^2=1, yxy=x^(-1)> and H_s=<yx^s>. The right coset x^u H_s contains x^u and x^(u+s)y. Encode these as |0,u> and |1,u+s>. Averaging the resulting coset states over uniform u gives exactly

  rho_s = (1/N) sum_u |(|0,u>+|1,u+s>)/sqrt(2)><...|.

Thus every DCP input copy is one ordinary mixed coset-state sample. The algorithm does not need a purification, a label u, or coherent access to the source. Applying the QFT to the rotation register and measuring k produces a uniform known k in Z/NZ and the phase qubit

  |psi_k> = (|0> + exp(2 pi i k s/N)|1>)/sqrt(2).

This is the sample-only model used by Kuperberg's general-order algorithm.

## Sieve and full-secret recovery

Use Kuperberg's Algorithm 5.1 for arbitrary N [1, Section 5]. Set m=floor(sqrt(log2 N)-2). First filter Fourier labels to the stated interval 0 <= k < 2^(m^2+1); the rejection overhead is N/2^(m^2+1)=2^(O(sqrt(n))). At level j, labels lie in the interval specified by Algorithm 5.1, and the list is paired so each pair differs by at most 2^(m^2-m(j+1)+1). A CNOT and one-qubit measurement combine the pair into a known-label phase state with label k-l or k+l. Retain the difference outcome. The label interval shrinks by the stated factor at each of m levels, leaving labels 0 and 1.

The probability statement needed here is the arbitrary-order final-label balance stated directly after Algorithm 5.1: Kuperberg notes that labels 0 and 1 in the final list are almost equally likely. In the same paragraph he identifies the precise issue: the lowest bit is almost uncorrelated with the pairing choice. We use that published balance statement as the final-level lemma. Consequently, above a fixed finite threshold n0, a generated final state is label 1 with probability at least 1/3; the explicit list-size and Chernoff analysis in the proof of Theorem 3.2 supplies a sufficiently large final list. For n<n0, enumerate all N candidate secrets and verify them directly. Since n0 is a fixed constant, this is a fixed finite prefix and does not affect the asymptotic bounds.

For arbitrary N, Kuperberg's Algorithm 5.1, steps 4 onward, handles all residues. Factor N=2^a M with M odd. For each j from 1 through ceil(log2 N), its divisibility sieve produces phase labels divisible by 2^min(a,j). The Chinese remainder decomposition Z/NZ ~= Z/2^aZ x Z/MZ separates the two components. On the odd component, multiplication by 2^(-j) modulo M is a group automorphism; applying the corresponding relabeling maps the divisible labels to labels whose odd component is 1, while the 2-primary component retains the required divisibility. The resulting observations are the cosine observations for 2^j(s-t) modulo N described in Algorithm 5.1. Taken over j, they determine s modulo each prime-power component and hence determine s modulo N by CRT. The factorization costs polynomial time using the uniform quantum factoring algorithm and is included in the total work.

Kuperberg's published general-N theorem gives a constant-success algorithm with 2^(O(sqrt(log N))) time and queries. To make the challenge guarantee explicit, run a fixed number of independent copies sufficient to raise its constant success probability above 5/6. Check each proposed t with fresh DCP states: controlled-subtract t in the second register and measure the first in the X basis. The true t always returns + on ideal states; a wrong t returns + with probability 1/2 per independent copy. Eight checks per proposal make the probability that any of seven wrong proposals passes at most 7/256. This leaves success above 2/3. All retries, list sizes, and verification counts are fixed by N and the published bounds; there is no unbounded repeat-until-success loop. Underfilled lists terminate with failure, and the fixed amplification accounts for this event.

## Uniform cost accounting

The source query/time bound in [1] is O(8^(sqrt(log2 N)))=O(2^(3 sqrt(n))). The algorithm makes O(n) target-state constructions and uses at most O(log n) bounded batches per construction to obtain the required labels. Fourier filtering costs a factor 2^(O(sqrt(n))); factorization and CRT postprocessing are polynomial in n. Charging bit-level label arithmetic, comparisons, list indexing, and address generation adds polynomial factors in n and in the logarithm of the list size. Approximate QFTs and measurement circuits can be synthesized with aggregate variation error at most 1/12 using polynomial overhead in n and the number of operations. Absorbing these fixed polynomial factors into the displayed padded envelope gives O(2^(3 sqrt(n)) n^10) for total gates/controller work and source copies.

The live list has no more entries than the total number of acquired samples. Storing its labels, pair indices, and level counters therefore takes O(Q n) classical bits. The direct implementation stores at most Q phase qubits and O(Q n^2) arithmetic/circuit workspace qubits. Both fit the same padded envelope. These are peak allocated spaces; all failed batches, discarded states, Fourier filtering, factorization, verification, measurements, and address computations are counted. The guarantee is for ideal independent input copies, so the claimed malformed-sample tolerance is zero.

For B(n)=2^(3 sqrt(n)) n^10, log2(log2 B(n))=(1/2)log2(n)+O(1), so all four resource growth indices are 1/2. No finite-size leading constant or empirical runtime is claimed.

## Reference

[1] Greg Kuperberg, “A Subexponential-Time Quantum Algorithm for the Dihedral Hidden Subgroup Problem,” SIAM Journal on Computing 35(1), 170–188 (2005), DOI: 10.1137/S0097539703436345. In particular, Algorithm 5.1 and its arbitrary-order discussion give the sample-state sieve, final-label balance, and CRT/automorphism residue recovery; Theorem 1.1 gives the uniform time and query bound. https://www.math.ucdavis.edu/research/infovault/greg/SIAM_JC-35-05.pdf
