# Exhaustive DCP testing with randomized corruption tolerance

## Algorithm and guarantee

Let N>=2 and n=ceil(log2 N). The algorithm tests every candidate shift using independent blocks of source copies, but randomizes which candidate receives each block in each round. It uses

  k=1024(n+1) copies per candidate per round,
  R=10000(n+1) rounds,
  Q=R N k copies in total.

The adversary chooses at most floor(Q/1024) corrupted copy positions and the corresponding single-copy states before seeing any of the algorithm's random permutations. All uncorrupted positions contain independent ideal DCP states rho_s. Corrupted positions may contain arbitrary fixed single-copy density operators; the joint input across positions is a product state. The adversary may know s. It may not adapt the corruption positions or states to the secret random permutations or measurement outcomes.

For each round r, generate an independent uniformly random permutation pi_r of the N candidate shifts. Visit blocks b=0,...,N-1 in order. Block b is assigned candidate t=pi_r(b) and consumes the next k source copies. For each copy, subtract t modulo N from the second register conditional on the first register being 1, then measure the first register in the X basis. Let Y_(r,t) be the number of + outcomes in the block. Mark the candidate positive in that round if

  Y_(r,t) >= 11k/16.

Keep one classical counter C_t for each candidate, initially zero, and increment it whenever t is positive. After all R rounds, output the unique t with C_t>R/2. If there is no unique such t, output a fixed default. Every execution uses exactly Q source copies and all loops have fixed bounds.

## Correctness under the corruption model

For an ideal source copy and candidate t=s, the controlled subtraction maps the state to |+> tensor |x>, so the X measurement is + with certainty. For t!=s, the first register is maximally mixed after tracing out the second register, so the X outcome is an unbiased bit. Outcomes from different uncorrupted source copies are independent.

Fix any allowed corruption pattern, independently of the secret random permutations. In round r let D_r be its number of corrupted positions. Call the round good if D_r<=Nk/64. Since the total corruption count is at most RNk/1024, fewer than R/16 rounds can be bad. In a good round, at most N/16 blocks can contain more than k/4 corruptions: each such block accounts for more than k/4 distinct corruptions, while the round has at most Nk/64 total. Call these blocks heavy.

For any fixed candidate t, its assigned block is uniform among the N blocks in each round, independently across rounds. In each good round its probability of landing in a heavy block is at most 1/16. Therefore the probability that any fixed candidate is assigned to more than R/8 heavy blocks across all good rounds is at most

  (e/4)^(R/16).

This is the multiplicative Chernoff bound for at most R independent indicators with mean at most R/16. A union bound over N candidates bounds the probability of any such event by N(e/4)^(R/16).

For the true candidate s, every non-heavy block contains at least 3k/4 clean copies, all of which return +. Thus it is positive in every such good round. Except on the event just bounded, it is positive in at least 15R/16-R/8=13R/16 rounds, which is greater than R/2.

Now fix a wrong candidate t. In a non-heavy block let c<=k/4 be the number of corrupted positions. The corrupted tests can contribute at most c plus outcomes. The other k-c tests are independent fair bits. If the block reaches the threshold 11k/16, the number of fair bits must exceed its mean by at least k/16. Hoeffding's inequality gives

  Pr[block is positive] <= exp(-k/128).

The probability that this wrong candidate is positive in at least R/4 non-heavy good rounds is at most

  2^R exp(-kR/512).

If this event does not occur and the candidate is assigned to at most R/8 heavy good blocks, then its total positives are at most R/16 bad rounds + R/8 heavy good rounds + R/4 non-heavy good rounds = 7R/16, less than R/2. A union bound over all N wrong candidates gives total failure probability at most

  N(e/4)^(R/16) + N 2^R exp(-kR/512).

For R=10000(n+1), k=1024(n+1), and N<=2^n, this is less than 1/100 for every n>=1. Hence the algorithm outputs the full secret with probability greater than 0.99 under the stated 1/1024 malformed-copy fraction. This exceeds the required 2/3.

## Joint resource bounds

The algorithm always acquires Q=R N k=O(N(n+1)^2) source copies. Since N<=2^n, this is O(2^n n^2). The controlled modular subtraction and X measurement for one copy require O(n^2) counted gates and controller operations using a straightforward reversible ripple implementation. The source acquisition itself costs n+1. Candidate ordering, counter updates, and permutation generation cost O(N n) bit operations per round, which is below the per-copy arithmetic cost. Over all R rounds, total sequential work is O(N n^4), hence O(2^n n^4).

To generate a uniform candidate permutation, use Fisher-Yates and store the current candidate array. The array uses O(Nn) classical bits. The counters C_t use O(N log(R+1)) bits, also O(Nn). Reuse the permutation array for each round. Thus peak allocated classical space is O(Nn)=O(2^n n). The algorithm processes source copies one at a time, reusing the same quantum wires, so peak quantum workspace is O(n^2) qubits including the state, arithmetic ancillas, and circuit workspace. No samples are retained across tests. These bounds count all permutations, counters, measurements, gates, source copies, and candidate blocks on every execution branch.

The representative envelopes and growth indices are:

* T: B_T(n)=2^n n^4, index 1;
* S_C: B_C(n)=2^n n, index 1;
* S_Q: B_Q(n)=n^2, index 0;
* Q: B_samples(n)=2^n n^2, index 1.

For the first, second, and fourth envelopes, log2(log2 B(n))=log2(n)+O(1), giving index 1. For n^2 the index is 0. These are full uniform bit-length bounds for the same algorithm and success guarantee.

## Pareto tradeoff and error model

The included clean-input baseline has time index 1, polynomial classical and quantum space, O(2^n n) samples, and zero claimed fractional tolerance. This candidate keeps time index 1 and polynomial quantum space, while using exponential classical storage and O(2^n n^2) samples to obtain a positive constant malformed-copy tolerance. The tradeoff is intentional: the positive tolerance can add a nondominated point in the full resource/tolerance frontier, although it does not improve the numeric time objective.

The tolerance claim is exactly epsilon(n)=1/1024. Among the Q acquired positions, at most floor(Q/1024) may be malformed. The corrupted locations and single-copy states must be fixed independently of the algorithm's secret random permutations and measurement outcomes. The uncorrupted positions are independent ideal coset states. Corrupted registers are arbitrary product-state replacements and are not entangled with other positions. This is a stated restricted error model; no guarantee is made for adaptive corruption after the random permutations are revealed.

## Evidence and limits

This is a proof-backed robustness extension of exhaustive candidate verification, not a new subexponential-time DCP algorithm. Its resource bounds deliberately make the classical storage cost explicit rather than treating the random candidate order as free. No empirical simulator results are claimed. The only randomness used for the guarantee is the algorithm's independent permutations and the ideal measurement outcomes from clean copies.
