# Arbitrary-order Kuperberg sieve for the DCP

## Claim

Let n=ceil(log2 N). For every N>=2 and s in Z/NZ, this submission uses the arbitrary-order dihedral sieve of Kuperberg, followed by a fixed phase-estimation decoder and candidate verification. Its joint resource envelopes in the challenge's uniform Clifford+T model are

* total sequential work T = O(2^(3 sqrt(n)) n^10);
* allocated classical space S_C = O(2^(3 sqrt(n)) n^10) bits;
* allocated quantum space S_Q = O(2^(3 sqrt(n)) n^10) qubits;
* fresh source copies Q = O(2^(3 sqrt(n)) n^10).

The common polynomial factor is a conservative allowance for all bit operations, addresses, gates, precision, list data, samples, and failed batches. The exponent coefficient 3 is explicit: Kuperberg's theorem gives O(8^(sqrt(log2 N))) source queries, and 8^(sqrt(log2 N))=2^(3 sqrt(log2 N)). The outer O includes multiplicative constants and finite thresholds. Each envelope has exact growth index 1/2.

This is an adaptation of published work, not a new sieve. It is a small candidate for improving the challenge's exhaustive-search time index 1 to 1/2; it does not meet the challenge's aspirational 1/3 index.

## The supplied state is the dihedral coset state

Write D_N=<a,b | a^N=b^2=1, bab=a^-1> and H_s={1,a^s b}. The right coset a^x H_s is {a^x,a^(x+s)b}. Encode a^x as |0,x> and a^(x+s)b as |1,x+s mod N>. The uniform state on this coset is exactly

  (|0,x>+|1,x+s mod N>)/sqrt(2).

Averaging over uniform x gives exactly rho_s from the challenge. Each challenge call therefore supplies one independent D_N/H_s coset-state copy. The algorithm uses no x value, purification, coherent control of the source, or source-preparation circuit. Kuperberg's arbitrary-N Algorithm 2 uses coset-state copies; his Section 8.1 distinguishes it from the power-of-two variant that needs a stronger hiding operation in later stages.

Fourier sampling the cyclic register produces a known uniform k in Z/NZ and the phase qubit

  |psi_k> = (|0>+exp(2 pi i k s/N)|1>)/sqrt(2),

up to global phase and the equivalent k versus -k convention. This is the input format used by the sieve. A final sign change converts conventions if needed.

## Finite-list sieve and its failure analysis

For N in the finite prefix before the arbitrary-order sieve's parameter m reaches a fixed threshold m0, use exhaustive shift testing. For all larger N, set m=ceil(sqrt(log2 N-2)). Kuperberg's arbitrary-N Algorithm 2 uses lists L_j of labels in

  0 <= k < W_j,   W_j=2^(m^2-mj+1),   j=0,...,m.

The initial width W_0 is at least N/2 because m^2>=log2N-2, and labels k and -k represent equivalent phase states, so the initial interval retains the whole Fourier-label range after sign normalization. At stage j, randomly pair the current labels subject to |k-l|<=W_(j+1), extract |psi_|k-l|> by the CNOT-and-measurement operation, and keep the difference branch. Every such output lies in [0,W_(j+1)). All list capacities and stage counts are fixed from n; if a list is underfilled the computation records failure and stops. It never draws an unbounded number of samples or restarts until success.

Here is the list-size estimate. Partition [0,W_j) into 2^m intervals of width W_(j+1). A maximal matching loses at most one unmatched item per interval, so its pair count P_j obeys P_j >= (|L_j|-2^m)/2. For each pair the difference outcome has probability exactly 1/2, independent conditional on the input list, hence |L_(j+1)| is binomial with P_j trials and probability 1/2. In the power-of-two proof, take target sizes |L_j|>=C_(m-j)2^(3m-2j), where C_0=3 and

  C_k = C_(k-1)/(1-2^(-k-m/3)) + 2^(-2k).

Kuperberg proves 3<=C_k<9. The Chernoff estimate uses b=2^(j-4m/3) and bounds the probability of violating the next target by exp(-2^(m/3-1)) per stage. Therefore the probability any of the m list transitions underflows is at most m exp(-2^(m/3-1)). For arbitrary N the same interval widths give the same bin count and binomial transition; Section 5 of Kuperberg carries over this list-size analysis. The one extra label-distribution fact needed there is that the final labels 0 and 1 are asymptotically almost equally likely: the lowest label bit is not used as a pairing key. We use this stated arbitrary-N lemma only to infer that, above some fixed m0, either target label occurs with probability at least 1/3. The finite prefix below m0 uses exhaustive testing. This makes each target-label batch a bounded-probability trial and makes its cap explicit below.

## Full-secret decoder, fixed repetition, and success

The final arbitrary-N procedure produces states with labels 2^j mod N for j=0,...,n. The factorization N=2^a M with M odd and the multiplication-by-2^(-j) automorphism on the odd component are the label-generation steps in Kuperberg's Algorithm 2. His remark after that algorithm notes that one copy each of |psi_1>, |psi_2>, ..., |psi_(2^n)> suffices for a quantum Fourier transform that reveals s. The following phase-estimation circuit makes that decoder explicit.

For one decoder attempt, tensor one state |psi_(2^j mod N)> for every j=0,...,n. Since 2^j mod N and 2^j induce the same phase, the product state is

  2^(-(n+1)/2) sum_(y=0)^(2^(n+1)-1) exp(2 pi i y s/N)|y>.

Apply the inverse Fourier transform of dimension 2^(n+1) and measure r. The geometric-series formula for the amplitude gives probability at least 4/pi^2 that r is the nearest integer to 2^(n+1)s/N. Since N<=2^n, this implies |rN/2^(n+1)-s|<=1/4; rounding rN/2^(n+1) to the nearest integer recovers s exactly.

Run exactly seven independent decoder attempts. Each requested phase state is produced by at most r_n=ceil(20 log2(2n+2)) independent sieve batches. A batch's output label is measured classically, so a state with the requested label can be retained and all other states discarded. Above m0, a batch yields each target label with probability at least 1/3 by the arbitrary-N near-balance lemma. There are at most 7(n+1) requested phase states; consequently the probability at least one is unavailable is at most 7(n+1)(2/3)^r_n, which is below 1/24 for n>=1.

Verify each of the seven candidate residues with exactly eight fresh DCP copies. For proposed t, subtract t from the second register conditioned on the first register being 1, then measure the first qubit in the X basis. If t=s, the test always returns +. If t!=s, the first register is maximally mixed and each independent test returns + with probability 1/2, so a wrong candidate passes all eight with probability 1/256. The ideal probability of no correct phase-estimation candidate is at most (1-4/pi^2)^7. A union bound for the seven false candidates and the phase-label generation failures gives ideal success at least

  1 - 1/24 - (1-4/pi^2)^7 - 7/256 > 0.9.

Compile the complete bounded procedure with total variation error at most 1/12. The implemented success remains greater than 2/3. All sieve batches, decoder attempts, and verification copies have fixed caps; every branch has the claimed resource ceiling.

## Uniform cost translation

The arbitrary-N sieve has O(8^(sqrt(log2 N))) source queries per target-label construction; at most 7(n+1)r_n constructions and constant verification copies are used. Since log2 N<=n, this gives

  Q = O(n log(n+2) 2^(3 sqrt(n))).

This is contained in the declared O(2^(3 sqrt(n)) n^10) sample envelope. A source call costs n+1 work units.

Each live label has n bits and a list index has O(log Q)=O(sqrt(n)+log n) bits. There are at most n sieve stages, at most Q pair operations per stage, and O(n log Q) bit work per sort/group comparison batch. Sorting, pairing, label arithmetic, address generation, and data movement therefore take O(Q n^3) classical bit operations under the benchmark's charged-address rule; no QRAM is assumed. At most Q phase qubits and their labels are live during a sieve batch, plus polynomially many temporary transform and synthesis registers. Thus both allocated workspace measures are O(Q n^5), a conservative bound including all retained samples and circuit descriptions.

An approximate Fourier transform on an n-bit cyclic register uses O(n^2) controlled rotations. Choose the total synthesis error so that the accumulated variation distance over the fixed circuit is at most 1/12. The batch cap is O(n log(n+2)2^(3sqrt(n))), so the logarithm of the inverse per-gate precision is O(sqrt(n)+log n). Solovay-Kitaev synthesis of each rotation takes O(log^4(1/delta))=O(n^2) gates at that precision; uniform circuit generation and its description use polynomially many bit operations per rotation. The QFTs, inverse QFTs, measurements, initializations, source costs, and all gate addresses are therefore bounded by O(Q n^6). Combining this with Q above gives total work O(2^(3 sqrt(n)) n^8), below the common n^10 envelope. All four bounds use the same fixed schedule and include failed label batches, failed decoders, and verification.

For B(n)=2^(3 sqrt(n)) n^10, log2(log2 B(n))=(1/2)log2(n)+O(1), so the exact growth index is 1/2.

## Error model and limits

The guarantee assumes every acquired copy is an independent ideal state rho_s. The fifth structured claim sets the tolerated malformed fraction to epsilon(n)=0; this does not claim positive tolerance is impossible. This submission does not prove the challenge's aspirational 1/3 time index, a practical finite-size speedup, or a new quantum technique. Its novelty is limited to mapping and accounting a known arbitrary-order sieve in this DCP benchmark. The arbitrary-N final-label balance is explicitly used as Kuperberg's stated lemma; reviewers should check that interpretation and the finite-threshold selection against the paper's proof.

## Reference

Greg Kuperberg, “A subexponential-time quantum algorithm for the dihedral hidden subgroup problem,” arXiv:quant-ph/0302112 (2003), Theorems 1.1 and 3.1, Section 5 Algorithm 2, and Section 8.1. https://arxiv.org/abs/quant-ph/0302112
