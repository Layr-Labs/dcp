# Kuperberg's arbitrary-order sieve for the DCP

## Claim and scope

Let n = ceil(log2 N). The algorithm below outputs the full hidden shift s for every N >= 2. It uses one fixed family of parameters, a bounded number of source copies, and no restart loop whose running time depends on a favorable random outcome. Its joint resource envelopes in the challenge's uniform Clifford+T model are

* total sequential work T = O(2^(3 sqrt(n)) n^20);
* allocated classical workspace S_C = O(2^(3 sqrt(n)) n^20) bits;
* allocated quantum workspace S_Q = O(2^(3 sqrt(n)) n^20) qubits;
* fresh source copies Q = O(2^(3 sqrt(n)) n^20).

The polynomial factor is deliberately loose. It accounts for bit-level controller work, address costs, approximate transforms, gate synthesis, all samples, and saved data. Kuperberg's arbitrary-N query bound has the more precise form O(8^(sqrt(log2 N))) = O(2^(3 sqrt(n))); the common polynomially padded bound is used here so no resource relies on free arithmetic or memory access. Each displayed envelope has exact growth index 1/2. These are big-O bounds, so the multiplicative constants and finite threshold are not claimed as explicit numbers. The exponent coefficient 3 is taken from the cited 8^(sqrt(log2 N)) query bound; it is not an unknown constant inside the exponent.

This is an adaptation of a known quantum algorithm and a resource-accounting result, not a new sieve discovery. It is submitted because the benchmark's included baseline has time index 1 and this known arbitrary-order algorithm gives a rigorously smaller index if the reduction and cost-model translation below are accepted.

## Exact input correspondence

Write the dihedral group as D_N = <a,b | a^N=b^2=1, bab=a^-1> and its reflection subgroup as H_s = {1,a^s b}. The right coset a^x H_s is {a^x, a^(x+s)b}. Encode a^x as |0,x> and a^(x+s)b as |1,x+s mod N>. The uniform coset state is then

  (|0,x> + |1,x+s mod N>)/sqrt(2),

and averaging a uniformly random x gives exactly the challenge state rho_s. Thus each challenge source call supplies precisely one independent mixed D_N/H_s coset state. The algorithm never needs x, a purification, the source-preparation circuit, or coherent source access. Kuperberg's Algorithm 2 (the arbitrary-N algorithm in Section 5) uses only these coset-state copies; Section 8.1 explicitly distinguishes it from the earlier power-of-two algorithm that needs a stronger coherent hiding operation in later stages.

After Fourier transformation on the cyclic register and measurement of its character k, one has a uniformly random k in Z/NZ and a phase qubit proportional to

  |0> + exp(2 pi i k s/N)|1>.

If the convention for the dihedral reflection yields x-s, the output label is -s mod N and a final classical negation recovers the challenge convention. This is a bijective relabeling, not an assumption about s.

## Bounded algorithm and arbitrary N

For N in {2,3,4}, use exhaustive shift testing; this finite branch always recovers s with success greater than 2/3 and contributes only a constant to the asymptotic bounds. For N >= 5, use Kuperberg's arbitrary-N Algorithm 2 (Section 5 of the cited paper), with its parameter m = ceil(sqrt(log2 N - 2)). It proceeds as follows.

1. Acquire the fixed batch of coset states required by the theorem and Fourier-sample each once, retaining the classical character label and its phase qubit.
2. At stage j, sort/group the current labels into intervals of the stage's prescribed width. Pair labels whose difference lies in the next, narrower interval. Apply the CNOT-and-measurement summand-extraction operation to each pair and keep the difference outcome. This creates states with labels closer to zero. The list is finite from the outset; each stage scans and pairs only items already present. If a required list is too small, mark this attempt as failed and stop it. Never request extra samples or repeat until success.
3. At the last stage the retained labels are 0 or 1. Apply the Ettinger-Hoyer measurement to the label-1 phase states to obtain the shift information, with the fixed measurement batch specified by the algorithm.
4. For arbitrary composite N, write N=2^a M with M odd. Apply the power-of-two sieve to obtain labels divisible by 2^min(a,j) for the prescribed j values, and use multiplication by the inverse of 2^j in the odd cyclic factor. These give the phase observations used by Algorithm 2 to recover the whole residue s mod N. The number of such stages is at most ceil(log2 N); Kuperberg's Section 5 query bound already includes this arbitrary-N reduction.

Every loop is over a list of bounded size or over at most n stages. All randomized choices are measurements within this finite computation. An underfilled list causes a failed attempt rather than an unbounded retry. Kuperberg's Theorem 3.1 proves the list survival probability for the power-of-two sieve by a Chernoff argument: with m = ceil(sqrt(n-1)), stage-j lists are maintained above C_(m-j) 2^(3m-2j) for constants 3 <= C_k < 9; maximal matching leaves at least (|L_j|-2^m)/2 pairs, and each pair produces the difference label with probability 1/2. The stated tail bound is at most exp(-2^(m/3-1)) per stage, so the probability all m stages meet their lower bounds tends to 1. The highest label bit is unused in pairing and remains unbiased, yielding a final target label. Section 5 specifies the corresponding intervals for arbitrary N, states that the same proof carries over, and gives the same O(8^(sqrt(log2 N))) query bound; its final near-zero labels feed the stated shift-estimation step. This submission uses the theorem's bounded-error output guarantee, not an expected-query variant.

Theorem 1.1 and the arbitrary-N algorithm use the standard bounded-error meaning of “algorithm that finds” the hidden reflection: success at least 2/3 for each hidden reflection. The fixed-batch Chernoff analysis in Theorem 3.1 gives high-probability list survival; Section 5 extends the same analysis to the arbitrary-N intervals and then applies the fixed Ettinger-Hoyer measurement and residue-recovery steps. On failure (including any underfilled-list branch), the bounded computation can return an arbitrary residue. No restart-until-success loop is used. Thus the theorem's bounded-error probability applies to the fixed batch, uniformly in s, and meets the challenge threshold. If a reviewer adopts a convention with a smaller constant, a constant number of independent copies of the entire bounded algorithm and fresh-state verification suffice; this changes only the outer constants, not the exponent or polynomial degree. Candidate verification subtracts a proposed t from the second register conditioned on the first register being 1, then measures the first qubit in the X basis. For t=s it returns + with certainty; for t != s the first register is maximally mixed and returns + with probability 1/2. All attempts and checks have fixed caps, so every branch obeys the resource bounds.

## Resource translation into the challenge model

Kuperberg's Theorem 3.1 gives O(8^(sqrt(log2 N))) source queries for its power-of-two sieve. Section 5 states the same query bound for Algorithm 2 at arbitrary N. With n=ceil(log2 N), log2 N <= n, so Q_base = O(2^(3 sqrt(n))). The additional fixed amplification and verification multiply this by a constant. The submitted common sample envelope O(2^(3 sqrt(n)) n^20) is therefore conservative.

The paper gives quasilinear time in the list data for Algorithm 2. A list has at most Q_base entries, each label has at most n bits, and its index has O(log Q_base)=O(sqrt(n)) bits. Sorting, grouping, comparison, pairing, label arithmetic, and indexed accesses can therefore be charged by a polynomial in n per list entry; no QRAM is assumed. Each source copy is charged n+1 units. The finite Clifford+T circuit for an approximate Z/N Fourier transform uses polynomially many rotations in n. Choose a total-variation error budget at most 1/12 across the bounded computation and synthesize every rotation to inverse-polynomial-in-the-total-gate-count accuracy. Since log Q_base=O(sqrt(n)), standard uniform single-qubit gate synthesis has polynomial overhead in n. Circuit generation, measurements, initialization, controller arithmetic, and precision bookkeeping are included in a polynomial factor. The deliberately loose n^20 covers these polynomial overheads; constants and a finite threshold are absorbed by the outer O.

At most Q_base phase qubits and their labels need be retained at one time. A label uses n classical bits, and the temporary transform/synthesis workspace is polynomial in n. Thus both peak spaces are O(Q_base poly(n)); all saved samples and failed lists are included. The total number of gates/bit operations and the count of source copies are also O(Q_base poly(n)). Consequently all four submitted envelopes hold jointly for the same finite-batch algorithm on every branch. The common bound B(n)=2^(3 sqrt(n)) n^20 has

  log2(log2 B(n)) = (1/2) log2(n) + O(1),

so its exact growth index is 1/2.

## Error model and limits

The source promise is exactly that all acquired copies are independent ideal states rho_s. The fifth claim therefore declares epsilon(n)=0, meaning no malformed copies are allowed by this guarantee. This does not assert that positive noise tolerance is impossible. The result does not establish the challenge's aspirational 1/3 time index, a practical speedup at finite sizes, explicit leading constants, or a new algorithmic technique. The essential arbitrary-N sieve and its success theorem are Kuperberg's published result; the contribution here is the explicit reduction to the exact DCP source and a conservative accounting translation. Review should focus on whether the source theorem's uniform bounded-error promise and arbitrary-N query bound transfer as stated, and whether the polynomial implementation overhead is adequate for the benchmark's specified Clifford+T model.

## References

Greg Kuperberg, “A subexponential-time quantum algorithm for the dihedral hidden subgroup problem,” arXiv:quant-ph/0302112 (2003), Theorem 1.1, Theorem 3.1, Section 5 (Algorithm 2), and Section 8.1. https://arxiv.org/abs/quant-ph/0302112

Theorem 3.1 states O(8^(sqrt(log2 N))) query complexity for the power-of-two sieve and proves list survival by a Chernoff bound. Section 5 extends the query estimate to arbitrary N and states quasilinear time in the list data. Section 8.1 explains that Algorithm 2 works from coset-state copies. The paper's theorem is used as a prior result, not represented as a new discovery.
