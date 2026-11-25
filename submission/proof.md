# Full-shift readout by coherent subset-rank erasure

Let \(N\ge2\) and \(n=\lceil\log_2 N\rceil\). Set \(k=n\) if \(50\cdot2^n\ge99N\), and \(k=n+1\) otherwise. This algorithm acquires exactly \(k\) independent ideal copies. Set \(D=2^k\). For every modulus and shift it succeeds with probability greater than 2/3. The decoder uses ordered subset-sum fibers computed by a bounded coherent search. It has no lookup table or quantum-addressed memory.

## Phase rows and ideal rank erasure

Write (\omega=exp(2\pi i/N)) and use translation (U|x\rangle=|x+1\bmod N\rangle), extended by the identity on padding. A Fourier eigenvector with eigenvalue (\omega^b) has coefficients (\omega^{-bx}). Measuring the eigenvalue on the position register of a source copy gives a uniform (b\in\mathbb Z/N\mathbb Z) and leaves the row \((|0\rangle+\omega^{bs}|1\rangle)/\sqrt2\). Indeed the position inner products on the two arms differ by the factor (\omega^{bs}), for every offset (x). Use the bounded approximate implementation below in the actual algorithm.

For the (k) independent labels (b_i), let (F(x)=\sum_i b_i x_i\bmod N) for a binary word (x) and let (m_z=|{x:F(x)=z}|). Order the solutions within each fiber by binary word, with zero-based rank (r(x)). The tensor product phase state, after the reversible change of encoding (|x\rangle\mapsto|F(x),r(x)\rangle), is
$$
  D^{-1/2}\sum_{z=0}^{N-1}\omega^{sz}|z\rangle
     \sum_{0\le r<m_z}|r\rangle .
$$
For each nonempty fiber, erase the rank by applying an \(m_z\)-dependent unitary sending its normalized uniform state to the rank basis state zero. After that operation the residue amplitude on \(z\) is \(\omega^{sz}\sqrt{m_z/D}\). The ideal probability to observe the eigenvector \(N^{-1/2}\sum_{z<N}\omega^{sz}|z\rangle\) is
$$
 P_b=\frac{(\sum_z\sqrt{m_z})^2}{ND}.
$$
The actual decoder applies phase estimation for \(U\) on the residue register. The desired eigenvalue is \(\omega^{-s}\), so rounding and negating return \(s\). Orthogonality of the residue eigenvectors ensures that all other components can only add to the probability of returning \(s\).

## Averaging the ideal success probability

For each nonzero word \(x\), \(F(x)\) is uniform modulo \(N\), because some coefficient is 1. If two nonzero words are distinct, their two rows contain a pair of columns with determinant \(+1\) or \(-1\). If their supports intersect, take a common column and one in the symmetric difference. If they are disjoint, take one column from each. Conditioning on the other labels gives an invertible two-column map over \(\mathbb Z/N\mathbb Z\). Thus indicators \([F(x)=z]\) for different nonzero words are pairwise independent for every fixed \(z\), including for composite \(N\). The zero word contributes the deterministic term \([z=0]\).

Let \(\mu=D/N\), so \(99/50\le\mu<4\). For each fixed label vector use \(E_z\) for averaging over all \(N\) residues, and set \(M_2=E_z m_z^2\). Since \(E_z m_z=\mu\), Hölder's inequality gives
$$
 \mu=E_z[(\sqrt{m_z})^{2/3}(m_z^2)^{1/3}]
       \le (E_z\sqrt{m_z})^{2/3}M_2^{1/3}.
$$
Therefore \(P_b\ge\mu^2/M_2\). For the expected second moment, the means are \((D-1)/N+[z=0]\). The mean-over-\(z\) square of their deviation from \(\mu\) is \((1-1/N)/N\). The variance at each \(z\) is \((D-1)(1-1/N)/N\) by pairwise independence. Adding these contributions yields \(\mathbb E M_2=\mu^2+\mu(1-1/N)\). Convexity of the reciprocal gives \(\mathbb E P_b\ge\mu/(\mu+1)\), which is at least \(3/4\) for \(\mu\ge3\).

For \(99/50\le\mu\le3\), sharpen the second-moment bound using the final uniform label. Let \(c_z\) be the fiber counts for the first \(k-1\) labels alone, and \(\lambda=\mu/2\ge99/100\). Conditional on that prefix, choose \(z\) and the last label independently and uniformly. Then \(m_z=c_z+c_{z-b_k}\), a sum of two independent draws \(X,Y\) from the prefix's empirical histogram. Let \(a,b,c\) be the conditional probabilities that \(X\) is odd, positive even, or zero, respectively. The probability of a positive even sum is \(a^2+b^2+2bc\ge(a+b)^2/2\).

Writing \(M'_2=E_z c_z^2\), Cauchy–Schwarz gives \(a+b\ge \lambda^2/M'_2\). The prefix second-moment calculation is identical to the calculation above with \(2^{k-1}\) words. Thus \(\mathbb E M'_2=\lambda^2+\lambda(1-1/N)\), and Jensen gives \(\mathbb E(a+b)\ge\lambda/(\lambda+1)\). A further Jensen inequality shows that the unconditional probability of a positive even \(m_z\) is at least \(\frac12(\lambda/(\lambda+1))^2\).

For any nonnegative \(u\), set \(h(u)=\sqrt3\,u/2-u^2/(6\sqrt3)\). The difference \(\sqrt u-h(u)\) equals \(\frac{\sqrt3}{2}t(t-1)^2(t+2)\) with \(t=\sqrt{u/3}\). It is nonnegative and exceeds \(1/16\) on the positive even integers. At \(u=2\) and \(u=4\), the strict estimates are \(\sqrt2-7/(3\sqrt3)>1/16\) and \(2-10/(3\sqrt3)>1/16\). For \(u\ge4\), the factorization is increasing because \(t>1\) and all its positive factors increase. Combining the even-count probability with the exact second-moment bound gives
$$
 \mathbb E_b E_z\sqrt{m_z}
 \ge \frac{8\mu-\mu^2}{6\sqrt3}+\frac1{32}\left(\frac{\lambda}{1+\lambda}\right)^2.
$$
For \(2\le\mu\le3\), division of the first term by \(\sqrt\mu\) gives \(\sqrt\mu(8-\mu)/(6\sqrt3)\). Its derivative has the sign of \(8-3\mu\), so its minimum on this interval is at an endpoint. The value at 2 is \(\sqrt{2/3}\), and the value at 3 is \(5/6\). Since \(P_b=(E_z\sqrt{m_z})^2/\mu\), Jensen on this square yields the uniform estimate
$$
 \mathbb E P_b\ \ge\ \left(\sqrt{2/3}+\frac{1}{128\sqrt3}\right)^2
 > \frac23+\frac1{160}.
$$
On \(99/50\le\mu\le2\), that first normalized term is increasing by the same derivative check. The second normalized term is at least \((99/199)^2/(32\sqrt2)\). Their sum is greater than \(2051/2500\), since
$$
 \frac{8124}{10000}\frac{301}{300}
 + \frac{(99/199)^2}{32(99/70)} > \frac{2051}{2500}.
$$
Here \(8124/10000<\sqrt{33/50}\) and \(99/70>\sqrt2\), by squaring. Also \((2051/2500)^2>2/3+1/160\). Jensen's inequality on the square as above gives the same ideal success bound in this range. The bound also holds when \(\mu\ge3\), by the preceding \(3/4\) estimate.

## Bounded fiber listing

Set the absolute cap (H=512). We implement an approximate clean lookup for the entire sorted fiber of (z), on all (z) such that (m_z\le H). Its output is a fixed-length array of (H) words tagged with validity bits, with invalid slots at the end. Every gate bound also applies to (z) outside this guarantee.

In the following idealized analysis of the listing circuit, a search trial prepares a uniform (k)-bit candidate. The mark checks that the candidate sums to (z) and differs from all valid words previously selected. Use probability (1/2) to run no Grover steps. Otherwise choose (j) uniformly from (0,\ldots,J-1), where (J=2^{\lceil k/2\rceil+2}), and apply (j) Grover steps. Recompute the mark and return the word only if it is valid. For (q) remaining matches among (D) candidates, write (\sin^2\theta=q/D). If (q>D/2), the no-step branch yields success probability greater than (1/4) after including its probability. If (1\le q\le D/2), the success averaged over (j) is
$$
 \frac{1}{J}\sum_{j=0}^{J-1}\sin^2((2j+1)\theta)
 \ge \frac{1}{2}-\frac{1}{2J|\sin 2\theta|}\ge \frac{3}{8} .
$$
The first inequality sums the geometric series and the second uses (\sin 2\theta\ge \sqrt{2/D}) and (J\ge4\sqrt D). Thus the mixture succeeds with probability at least (1/8) whenever any match remains. If (q=0), the mark check rejects every trial.

Run (512) trials per slot and pick the first valid result, if any. Repeat for all (H) slots, excluding earlier valid results. Set the value in each invalid slot to zero during selection. Sort the selected results by validity then binary value. For (m_z\le H), all slots agree with the desired listing except with probability at most
$$
 \delta=H(7/8)^{512}<2^{-80}.
$$
This holds by conditioning on the earlier trial outputs, then applying the union bound. Verification and exclusion ensure no duplicates or false matches. The sort is a fixed reversible sequence of compare-and-swap operations with recorded swap flags.

The above analysis is of the measured version. The implementation stores each trial's candidate and all its control coins without measuring. It computes selection from these registers using computational-basis reversible gates. Subsequent trials use the selection as controls and fresh candidate registers. Squaring amplitudes of the retained orthogonal histories gives the same joint law as in the measured version. There are absolute constant numbers of trials, slots, selection registers and sorting flags. For a trial with a coherent iteration count, execute (J-1) stages, each with a zero-based index and guarded by the strict comparison that the count exceeds the index and by the branch coin. The uniform candidate comes from Hadamards. Guard the phase marker by controlling the final sign after computing its predicate. Guard diffusion by using the candidate-wide Hadamards unconditionally around the guarded reflection of the all-zero word. Controlled signs, comparisons, and these reflections have exact Clifford+T circuits using Toffoli, X, CNOT and Z. No controlled arbitrary rotations are needed for this subroutine.

For fixed good (z), write (V_z) for this unitary with its listing in a designated scratch register. Apply (V_z), XOR the listing into an output array, then apply (V_z^{-1}). Its action on zero scratch differs in vector norm by at most (2\sqrt\delta) from an ideal XOR of the true listing leaving scratch unchanged. Indeed on the success component before XOR the two XOR operations agree, and the norm of the remaining component is at most (\sqrt\delta). The same bound holds with an arbitrary initial XOR target and entangled reference, since (V_z) acts on neither. It holds in superposition over good (z) by orthogonality of the retained (z) register. We also use the inverse of this clean lookup, which is the same circuit.

## Using the listing in the decoder

Retain the original (k) row bits (x), compute (z=F(x)) reversibly into a zero register, and perform the approximate clean listing into another zero register. Scan the listing with equality checks to compute into a fresh register the index of (x) among the valid words. Use that index to XOR the corresponding (k)-bit word into the original register, zeroing it in the ideal successful listing. The index has (k) bits and the scan compares against classical slot constants. Specify the scans on all inputs by XOR of each enabled value, so missing matches produce zero and even malformed scratch remains governed by a unitary circuit. With the listing still available, count the valid slots coherently to obtain the size \(m\). Conditioned on that count, send the rank's normalized uniform state on indices \(0,\ldots,m-1\) to zero. Use identity when the count is zero. The inverse operation, preparation, is an explicit finite-dimensional circuit: for each admissible \(m\), build a binary prefix tree on the first \(m\) indices. On each nonempty prefix rotate the next bit so that the two output probabilities are the fractions of its leaves in the two children. Arbitrary prefixes off this support can act as identity. Take the reverse circuit for erasure. Only the lowest \(\log_2 H\) rank bits are acted on, or all \(k\) if \(k<\log_2 H\). Include only sizes up to the dimension on those bits. Thus there are a fixed finite number of controlled rotations on a fixed number of wires, using the low rank bits and the count. Synthesize them as fixed Clifford+T words up to global phase with total operator error at most \(2^{-16}\). Multi-bit conditions can be built using Toffoli gates and uncomputed. For each controlled real Y rotation, conjugate its target by a fixed Clifford carrying the Y axis to Z. Compile the resulting controlled axial rotation using exact Boolean control and parity, as in spectral readout. Any conditional scalar phase is a single-qubit phase on the computed control flag. Uncompute the flag after the controlled operation. Synthesis up to global phase applies to the unconditional one-qubit gates of the decomposition, so the global phases are independent of the flag. This is uniform, since all target rotation entries are square roots of ratios of fixed bounded integers and a finite certified search for each needed fixed-precision rotation terminates by universality. Uncompute the count from the listing, then undo the listing and run the final spectral readout. Any residual work registers on erroneous paths may be discarded.

For the ideal comparison, list and erase exactly on \(m_z\le H\). On all fibers the ideal complete decoder can be extended to a unitary which keeps \(z\) fixed and sends the normalized uniform fiber vector to zero scratch. On good fibers the exact listing and erasure circuit realizes that action. A two-call hybrid with exact rank rotations shows that the vector norm difference on the good component is at most \(4\sqrt\delta\), since this component has norm at most one and each ideal intermediate state has clean lookup scratch. Rotation synthesis is accounted for separately.

Let \(B=\{z:m_z>H\}\) and \(p=D^{-1}\sum_{z\in B}m_z\). Both the exact and physical decoders before final spectral readout keep the \(z\) register fixed. For any state of norm \(\sqrt p\) supported on \(B\), projection onto the target residue eigenvector (tensored with identity on scratch) has norm at most \(\sqrt{|B|/N}\sqrt p\). This is Cauchy–Schwarz on the sum of the scratch vectors, using the flat magnitude of the target residue eigenvector. Also \(|B|/N\le\mu p/H\), since each bad fiber contributes more than \(H\) words. Thus each of the two bad components contributes at most \(\sqrt{\mu/H}\,p\) to the norm of the projected state. Adding the good component comparison, the difference in target eigenvector probabilities is at most \(4\sqrt{\mu/H}\,p+8\sqrt\delta\), since both projected norms are at most one. This bound still applies if all fibers represented in the state are bad. No physical projection onto good fibers is performed.

Using \(m_z[m_z>H]\le m_z^2/H\) and the second moment already proved,
$$
 \mathbb E p\le\frac{\mu+1-1/N}{H}<\frac5H.
$$
Hence the mean target eigenvector probability loss is less than \(40/H^{3/2}+8\sqrt\delta\).

## Uniform spectral readout

Use binary-register phase estimation of the padded modular increment. Let (d=n+\lceil\log_2(n+2)\rceil+16) and (M=2^d). Prepare a uniform control of (d) bits, use controlled modular additions by the powers of two modulo (N), apply the inverse binary Fourier transform on the control and read its integer (y). Round (Ny/M) to the nearest integer and reduce modulo (N) (fix any deterministic tie rule). On an eigenvector of angle (b/N), the ideal probability of (y) is the squared geometric sum
$$
 \left|M^{-1}\sum_{t=0}^{M-1} e^{2\pi i t(b/N-y/M)}\right|^2.
$$
At circular distance (v>0) from (Mb/N) in integer units, the probability is at most (1/(4v^2)) by (\sin(\pi v/M)\ge 2v/M). A wrong rounding requires (v\ge M/(2N)). There are at most two outcomes per half-open unit-distance shell, and summing the reciprocal squares gives failure at most (1/(2(\lfloor M/(2N)\rfloor-1))). This is less than (1/(2^{14}(n+2))).

For raw source readout, analyze a hypothetical preliminary exact eigenvalue measurement on its position register. It does not affect the joint law of the reported label and the retained row, since the physical spectral readout preserves position eigenvectors and then discards the position register. Thus the ideal phase-estimation report can be coupled to the exact spectral label at the above cost per copy. The final spectral readout uses the same guarantee for the desired eigencomponent. Only (k+1) spectral readouts are used.

Use Clifford+T approximations to each controlled Fourier rotation with operator error up to global phase at most (2^{-16}/((k+1)d^2)). The inverse binary Fourier circuit has at most (d^2) rotations. A controlled phase can be constructed from one-qubit Z rotations and CNOT gates using the bit identity ab = (a+b-(a XOR b))/2. Use the uniform constructive Solovay–Kitaev synthesis algorithm with the fixed inverse-closed Clifford+T single-qubit generating set, as in Dawson and Nielsen, [The Solovay–Kitaev algorithm](https://arxiv.org/abs/quant-ph/0505030). Use polynomially many bits of precision and bit operations in (n) for this preprocessing. More specifically, it uses a fixed polynomial in (log(n+2)) for each rotation, including truncating its specified binary angle to the necessary precision and generating the gate sequence. Fixed starting nets and word libraries in the algorithm are absolute finite objects and can be compiled or generated as part of the uniform controller. The initial net and the recursive approximations can use a constant fraction of the target error for input accuracy and certify the operator-error bound using extra precision. By telescoping before measurements, the total change of output event probabilities from rotation synthesis is at most (2^{-15}).

The ideal rank erasure and exact final readout give success greater than \(2/3+1/160\). Bounded listing costs less than \(40/H^{3/2}+8\sqrt\delta\), which is less than \(1/250\) at \(H=512\). Phase readout costs at most \((k+1)/(2^{14}(n+2))\le2^{-14}\) by coupling, and the combined synthesis costs at most \(2^{-14}\) in output event probability. Their sum is less than \(1/160\), giving success greater than \(2/3\) unconditionally for every \(N,s\).

## A reversible block circuit for the search predicate

The main cost inside a search iteration is evaluating \(F(x)\) on known labels. We compress the circuit by grouping selector variables. Put \(\ell=\max\{1,\lfloor(\log_2 n)/2\rfloor\}\), padding the final block with zero selector bits and zero labels. Let \(w=\lceil\log_2(2\ell+1)\rceil\). Per block the classical label bits in column \(j\) specify a mask \(S_j\) of \(\ell\) bits, recording exactly the labels in that block which contribute a 1 in column \(j\). These masks are independent of the quantum selector. In a one-time polynomial computation, transpose the measured labels into a sequential work tape of these masks in block and column order. Use \(\ell\) bits per mask and \(n\) masks per block, for \(O(n^2)\) bits. The controller can scan this tape in either direction in order with single-cell head advances.

For one block, build all \(2^\ell\) population counts \(C[S]=\sum_{i\in S}x_i\) into zero quantum registers. The address of \(C[S]\) is a classical wire address computed from the mask \(S\). Generate the counts in increasing mask order, with \(C[0]=0\). For nonempty \(S\), copy \(C[S\setminus\{i\}]\) into \(C[S]\) and add the selected bit \(x_i\), where \(i\) is the least set bit of \(S\). Each step uses \(O(w)\) exact gates, including resetting the ripple arithmetic scratch. The count registers need \(O(2^\ell w)=O(n)\) qubits. One may use the next power of two above \(w\) as their stride so that the mask part of any wire address is just a binary field.

The exact unreduced sum of the selected labels in a block is \(\sum_{j=0}^{n-1}2^j C[S_j]\). Compute this sum with a \(w\)-bit carry \(c\), starting at zero. In column \(j\), add the count \(C[S_j]\) to \(c\), swap the low bit into a fresh output bit, and shift the carry representation by one position toward its low end, putting the vacated zero at the high end. A cyclic relabeling or \(O(w)\) swaps implements this shift reversibly. The carry before any column is at most \(\ell\), so the addition into its \(w\)-bit register does not overflow. After the last column, the \(n\) output bits and the residual carry give the block sum. All reversible steps can be undone with the same mask schedule in reverse. Column processing costs \(O(nw)\) gates plus the \(O(2^\ell w)\) gates for constructing the counts.

The block subtotal is less than \(\ell N\). To reduce it modulo \(N\), compare and conditionally subtract \(2^j N\) for \(j=w-1,\ldots,0\). For each of these \(w\) rounds keep its comparison bit and use a reversible subtraction controlled by that bit. This yields the exact remainder and is invertible given the comparison bits. Only \(O(n+w)\) scratch is live apart from the population count registers. Add that remainder to the accumulated residue with one in-place modular addition. Then undo reduction, column processing and the count construction, leaving only the accumulated residue. Process all blocks serially. In-place modular addition on valid residues, followed by identity on padded strings, is a permutation with a controlled inverse. Ripple comparison, addition and selection circuits compute it into scratch, swap and clear by the inverse. Each Boolean computation costs \(O(n)\) gates and workspace and reverses after its output is used. These circuits use exact NOT, CNOT and Toffoli. The quantum Horner-style accumulator never stores all block subtotals at once.

The controller materializes the mask tape once. During each forward and reverse predicate evaluation it streams the mask fields in order from a sequential tape head, with a constant number of linear sweeps. These advances and reads take \(O(n^2)\) ordinary single-cell steps. Any nonsequential access pays for its full address, including any access during the one-time transpose. To emit the quantum circuit, store a constant number of \(O(\log(n+2))\)-bit wire address fields on sequential work tapes. Each mask is copied from its \(\ell\) sequential input bits into one such field and its count-register addresses are formed by concatenation with the appropriate position and base fields. Template index increments, offsets, comparisons and carries on these short fields cost \(O(\log(n+2))\) sequential bit steps per emitted gate. The addressed gate itself also pays \(O(\log(n+2))\). Fixed words such as \(N\) and its shifted versions can be scanned serially, without a new table entry for each round or retained circuit description. When reversing the arithmetic for a block, the mask-head direction is also reversed, with its head returned to the appropriate end before starting the next block. Returning over a block's masks even when no masks are used costs \(O(n\ell)\) local steps, already within the total tape scan bound.

The \(O(1+k/\ell)\) blocks use \(O((1+k/\ell)(n+2^\ell)w)\) gates. Equality, list exclusion, the count guard and inversion add only \(O(n)\) or a constant factor to this gate bound. Including the serial tape work and all gate addressing, the charged cost of a search iteration is therefore
$$
 O\!\left(n^2+(1+k/\ell)(n+2^\ell)w\log_2(n+2)\right)
 = O\!\left(n^2(1+\log_2\log_2(n+2))\right).
$$
Here \(k\le n+1\), \(2^\ell=O(\sqrt n)\), and \(\ell\) is of order \(\log_2 n\). The fixed finite small lengths are covered by the same asymptotic bound.

## Joint resources and declared indices

The number of search iterations is \(O(2^{n/2})\) on every branch, with all loop caps absolute except the index width and the prescribed power-of-two iteration range. Source acquisition, fixed-cap listing scans, uniform gate synthesis and the one-time classical transpose all have fixed polynomial or constant cost outside those iterations. All source handling, failed trials, initialization, restoration and discard are charged. Thus the sharper work bound is
$$
 O\!\left(2^{n/2}n^2(1+\log_2\log_2(n+2))\right).
$$
For the supported envelope use \(O(2^{n/2}n^2(\log_2 n)^{1/8})\), since \(1+\log_2\log_2(n+2)=O((\log_2 n)^{1/8})\) for large \(n\). In particular it is asymptotically smaller than the envelope \(2^{n/2}n^2\log_2 n\). Both work expressions have index 1.

Peak allocated classical memory is \(O(n^2)\) bits, including the measured labels, the transposed tape, addresses, guard counters and the compiler workspace. Each Fourier rotation is compiled separately, using at most a fixed polynomial in \(\log(n+2)\) bits. The rank-erasure compiler is for a fixed finite set of dimensions and target precisions, so its maximal workspace is an absolute constant. Peak allocated quantum memory is \(O(n)\) qubits. The population count and all arithmetic scratch reuse one region, the coherent trial histories have a fixed absolute number of \(O(n)\)-bit records, and acquisition/readout uses a single temporary phase estimation register each time. The exact acquisition count \(k\) is \(n\) or \(n+1\) by the public modulus test and is \(O(n)\). All three other resource indices are 0. This same algorithm guarantees only fraction zero under the independent ideal-copy promise.

## Sources

The Fourier-phase representation and the ideal subset-fiber measurement belong to the pretty-good-measurement framework of Bacon, Childs and van Dam, [Optimal measurements for the dihedral hidden subgroup problem](https://arxiv.org/abs/quant-ph/0501044). The bounded, reversibly sorted search construction implements that decoding here without assuming a subset-sum sampler. The randomized search schedule uses the averaging argument of Boyer, Brassard, Høyer and Tapp, [Tight bounds on quantum searching](https://arxiv.org/abs/quant-ph/9605034). Yukon candidate 6f49290 supplied the guarded modular-translation readout and the determinant-one argument for pairwise independence of nonzero binary subsets. Its collimation, residual balancing and target generation are not part of this construction.
