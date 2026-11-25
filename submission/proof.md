# Full-shift subset-fiber erasure with a signed representation table

Let \(N\ge2\) and \(n=\lceil\log_2 N\rceil\). Set \(k=n\) when either \(50\cdot2^n\ge99N\), or \(n\ge576\) and \(4\cdot2^n\ge 5N\). Set \(k=n+1\) otherwise. This algorithm acquires exactly \(k\) independent ideal copies. Set \(D=2^k\). For every modulus and shift it succeeds with probability greater than 2/3. The decoder uses signed subset representations in a classical table and a coherent right-half search to list the relevant subset-sum fibers. It streams the table using only classical addresses.

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

Let \(\mu=D/N\), so \(5/4\le\mu<4\). For each fixed label vector use \(E_z\) for averaging over all \(N\) residues, and set \(M_2=E_z m_z^2\). Since \(E_z m_z=\mu\), Hölder's inequality gives
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

## A wider n-copy window from bounded factorial moments

Let \(k=n\), \(D=2^k\), \(\mu=D/N\in[5/4,2)\), and \(V=m_z\) for an independent uniform residue \(z\). Fix \(1\le r\le10\). For an ordered tuple of distinct binary selectors, the equations saying that their sums all equal \(z\) have a coefficient matrix whose columns are the ordinary \(r\)-bit patterns and a final column of minus ones. Let \(d\) be its rational rank.

If, for each coordinate, two ordinary columns differ only in that coordinate, their integer span contains all the unit vectors. The matrix then induces a surjection onto \((\mathbb Z/N\mathbb Z)^r\). Its uniform input therefore gives probability \(N^{-r}\) of zero. In general take a nonsingular \(d\)-by-\(d\) minor \(A\), and condition on all variables other than those selected columns. The number of possible choices for those variables is at most \(|\det A|\), including for composite \(N\). Indeed the kernel size of \(A\) modulo \(N\) equals its cokernel size over that finite group, which is the index of \(A\mathbb Z^d+N\mathbb Z^d\) in \(\mathbb Z^d\). This is at most the lattice index \(|\det A|\). By Hadamard, \(|\det A|\le d^{d/2}\le10^5<2^{17}\). The probability is thus at most \(2^{17}/N^d\).

For a given coordinate the binary cube partitions into \(2^{r-1}\) pairs along that axis. A full-rank tuple missing an edge along that axis is contained in a set selecting one endpoint from each pair. There are \(2^{2^{r-1}}\) such sets, and at most \((2^{r-1})^k\) tuples per set. Union over the \(r\) axes. For deficient rank, the column span is one of at most \(2^{rd}\) spans of \(d\) binary vectors, counting the final column with its sign reversed. It contains the all-ones vector. Select \(d\) coordinates giving an injective projection, and express each omitted coordinate as a linear form of the selected coordinates. A form with only one nonzero coefficient must have that coefficient one because of the all-ones vector, but this duplicates a selected coordinate on every ordinary column, contrary to distinct selector rows. Every omitted coordinate thus has at least two nonzero coefficients. Fix one such form and two nonzero coefficients. On every two-bit face of the projected cube in those positions, the four values \(a,a+b,a+c,a+b+c\), with \(bc\ne0\), cannot all belong to \(\{0,1\}\). If all were binary, both nonzero differences from \(a\) would have to equal \(1-2a\), which would place the fourth value outside the set. Thus at most \(3\cdot2^{d-2}\) cube points can correspond to binary vectors in the span. If \(d=1\) no such deficient tuple exists by the same distinctness argument. The number of tuples in a given deficient span is bounded by \(((3/4)2^d)^k\).

The baseline estimate for \(\mathbb E(V)_r\) is \((D)_r/N^r\), with falling factorials. Its absolute error on full-rank exceptions is at most
\[
 r\,2^{2^{r-1}}(2^{17}+1)\mu^r 2^{-k}\le 2^{544-k}.
\]
The absolute error from deficient rank is at most
\[
 \sum_{d=1}^{r-1}2^{rd}(2^{17}+1)\mu^d(3/4)^k
 \le 2^{121}(3/4)^k .
\]
Both estimates use the sum of actual and baseline bounds on each exceptional tuple. The difference \(\mu^r-(D)_r/N^r\) is at most \(\binom r2\mu^r/D\) by bounding the chance of a repeat in \(r\) independent uniform words. Since \((3/4)^5<1/4\), for \(k\ge576\) the three errors together are less than \(2^{-16}\). Dividing by \(r!\) shows that \(\mathbb E\binom Vr\) differs from the Poisson moment \(\mu^r/r!\) by less than \(2^{-16}\).

For a nonnegative integer \(v\), integration by parts and the Gaussian integral give
\[
 \sqrt v=\frac1{2\sqrt\pi}\int_0^\infty (1-e^{-vt})t^{-3/2}\,dt.
\]
Write \(u=1-e^{-t}\). The alternating binomial sum for \(1-(1-u)^v\) truncated at degree 10 is a lower bound, with gap at most \(\binom v{11}u^{11}\), by applying the two successive Bonferroni bounds to the union of \(v\) independent events of probability \(u\). After integrating, each coefficient of the signed moment sum has magnitude at most one, since \(u^r\le u\). For \(Y\) Poisson of mean \(\mu\), using its factorial moments then gives
\[
 \mathbb E\sqrt V\ge\mathbb E\sqrt Y-\left(10/2^{16}+2^{11}/11!\right).
\]
The normalized Poisson expectation \(\mathbb E\sqrt{Y/\mu}\) increases with \(\mu\). For \(\mu_1\le\mu_2\), thin \(Y_2\) by keeping each count with probability \(\mu_1/\mu_2\). The thinned count \(Y_1\) has mean and Poisson parameter \(\mu_1\) by its generating function, and \(\mathbb E[Y_1/\mu_1\mid Y_2]=Y_2/\mu_2\). Apply conditional Jensen.

For an explicit rational certificate at \(\mu_*=5/4\), the Taylor sum for \(e^{5/4}\) through degree 8 plus \(8/7\) times the degree-9 term is less than \(3491/1000\) and bounds the entire exponential above. For the first eight positive Poisson masses bound \(\sqrt j\) below by \(a_j/100000\) with \(a_j=(100000,141421,173205,200000,223606,244948,264575,282842)\), as checked by squaring. This yields
\[
 L=\frac{1000}{3491}\sum_{j=1}^8 \frac{a_j}{100000}\frac{(5/4)^j}{j!}
 \le \mathbb E\sqrt{\operatorname{Pois}(5/4)} .
\]
Write \(\varepsilon_0=10/2^{16}+2^{11}/11!\). Exact rational arithmetic gives \((L-\varepsilon_0)^2/(5/4)>2/3+1/400\). Monotonicity of the normalized Poisson expectation, and \(\mu\ge5/4\), imply the same lower bound for \((\mathbb E\sqrt V)^2/\mu\). Jensen over the label-dependent average of the square root proves the ideal success bound for every modulus in this branch. With listing cap \(H=1024\), the earlier projection bound costs less than \(1/800\), and adding the readout and synthesis costs still uses less than the \(1/400\) margin.

## Direct bounded listing and its coherent interface

Set the absolute cap (H=1024). The direct finite fallback implements an approximate clean lookup for the entire sorted fiber of (z), on all (z) such that (m_z\le H). Its output is a fixed-length array of (H) words tagged with validity bits, with invalid slots at the end. Every gate bound also applies to (z) outside this guarantee.

In the following idealized analysis of the listing circuit, a search trial prepares a uniform (k)-bit candidate. The mark checks that the candidate sums to (z) and differs from all valid words previously selected. It computes the modular sum by controlled additions of each label into a rolling register using exact ripple logic. Each constant modular addition can be evaluated in fresh scratch, swapped into place and cleared using the inverse addition, with identity on padded values. Only a constant number of linear-sized words, counters and scratch registers are live. Use probability (1/2) to run no Grover steps. Otherwise choose (j) uniformly from (0,\ldots,J-1), where (J=2^{\lceil k/2\rceil+2}), and apply (j) Grover steps. Recompute the mark and return the word only if it is valid. For (q) remaining matches among (D) candidates, write (\sin^2\theta=q/D). If (q>D/2), the no-step branch yields success probability greater than (1/4) after including its probability. If (1\le q\le D/2), the success averaged over (j) is
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

## A representation table for coherent subset-fiber listing

The main branch uses the following right search in the same coherent listing interface. The rank-erasure algorithm needs a canonical list of each small fiber on most of its incoming phase-state mass. A shorter-time implementation uses a table of signed representations of ordinary binary solutions. It uses exponential ordinary classical memory and only linear quantum storage. The auxiliary modulus in this implementation is independent of \(N\); using unreduced sums avoids any assumption that this modulus divides \(N\).

Let \(u=\lfloor k^{2/3}\rfloor\), calculated by the integer cube root of \(k^2\). A weight \(w\) is central when \(|w-k/2|\le u\). Let \(G\) be the number of central weights, \(a=\lfloor349k/20000\rfloor\), \(r=\lfloor9567n/20000\rfloor\), and \(P=2^r\). Set \(L_b=2^{\lceil5982n/25000\rceil}\). For each central weight \(w\), define a left signed class of words in \(\{-1,0,1\}^k\) with exactly \(\lfloor w/2\rfloor+a\) positive and \(a\) negative coordinates. The right class has \(w-\lfloor w/2\rfloor+a\) positive and \(a\) negative coordinates. Write \(S_{w,1},S_{w,2}\) for their cardinalities.

For any fixed binary word \(x\) of weight \(w\), it has at least
$$
 R_w=\binom w{\lfloor w/2\rfloor}\frac{(k-w)!}{a!a!(k-w-2a)!}
$$
representations \(x=l+h\) with left vector \(l\) and right vector \(h\) in these classes. In fact these are all such representations. Allocate the ones of \(x\) between \(l\) and \(h\) in the prescribed counts. On zero coordinates the two signed entries are opposite, with \(a\) of each nonzero orientation. Every selected left half determines a unique right half \(h=x-l\). The number of represented left halves on a fixed support is at most \(2^{2a}\): signs on the \(x=1\) positions are fixed, and only the \(2a\) nonzero zero coordinates can have either sign.

Let \(S_{\min},S_{\max}\) be the extrema of \(S_{w,i}\) over central weights and both classes, and \(R_{\min}=\min_w R_w\). Require all classes and factorial counts to be defined, positive and negative counts unequal, central weights at least two, \(k-w\ge2a\) throughout the central range, \(P\ge4\), each class support size at most \(\lceil 3n/10\rceil\), and
$$
 2^{\lfloor95673n/100000\rfloor}\le S_{\min}\le S_{\max}\le 2^{\lceil3827n/4000\rceil},
 \qquad
 R_{\min}\ge 2^{\lfloor17937n/25000\rfloor}.
$$
Additional public checks are given below. If any public check fails, use the direct bounded listing of the precursor for that modulus, with the same \(k\), all five guarantee premises and \(H=1024\). These fallback lengths are finite.

Write the measured labels \(b_i\) as integers \(0\le b_i<N\), and define the signed integer sum \(F_{\mathrm{int}}(l)=\sum_i b_i l_i\), with no modular reduction. For each central \(w\), draw an independent uniform \(c_w\bmod P\). Build a classical list at \(w\) of exactly \(L_b\) signed left halves satisfying \(F_{\mathrm{int}}(l)\equiv c_w\bmod P\). Draw with replacement so each draw uses the same low predicate and does not query previously stored records. Store the selected word and its exact signed integer sum; duplicates are permitted. Left and right classes have ordinary polynomial-time lexicographic rank and unrank using counts of completions by binomial products with binary operands. An index outside the cardinality is invalid. Use the linear-scratch reversible unranking below.

For the left draw, the search starts at the uniform state over the padded binary index space for that class, marks only valid indices satisfying the low sum, and uses a uniformly randomized Grover iteration count in \([0,2^{\lceil r/2\rceil+4})\), along with a fair choice allowing zero iterations. Verify the returned index and retain it only if marked. Run at most \(512(n+1)\) trials for each draw, aborting globally if none succeeds. Every accepted draw is exactly uniform on the good indices because all marked amplitudes coincide at each possible iteration count. Trials and independent draws use fresh initialization. Left tables are computed before any coherent fiber listing and are fixed classical data thereafter.

## Correctness of the classical preparation and coverage

A spectral label is uniform on \([0,N)\). The distribution of its low residue mod \(P\) differs from uniform by at most \(P/N\) in total variation: every residue has one of the two consecutive possible multiplicities. Thus \(kP/N\) bounds the discrepancy for all low labels together. Analyze the following low-sum events with uniform independent residues and add this discrepancy once.

For any fixed class of size \(S\) and residue \(c\bmod P\), let \(C\) count its words with low sum \(c\). Each signed word has some unit coefficient, hence \(\mathbb EC=S/P\). Two words of different supports have a unit-determinant minor using a coordinate in their support difference and a nonzero coordinate of the other word. They have independent uniform sums. Two different words of the same support are neither identical nor negatives, because class sign counts are fixed and unequal. They have a nonzero minor of magnitude at most two, and their joint probability of both hitting the specified residue is at most \(2/P^2\). To see the last bound, condition on other variables. A nonsingular integer two-by-two matrix of determinant \(d\) has at most \(|d|\) solutions for a given right-hand side modulo \(P\), by the cokernel-index argument in the factorial-moment section. Thus
$$
 \operatorname{Var}C\le S/P+S\,B_c/P^2,\qquad
 B_c=2^{\lceil3n/10\rceil},
$$
using at most \(B_c\) elements per support. By Chebyshev and a union bound over the \(2GP\) class-residue pairs, the probability that any pool count is outside \([S/(2P),2S/P]\) is at most
$$
 8G(P^2+PB_c)/S_{\min}.
$$
This event definition includes both possible class types and all choices of \(c_w\). On the good event a left trial starts with marked fraction at least \(1/(4P)\) and succeeds with probability at least \(1/8\) by the randomized Grover estimate established in the bounded listing section. The probability of any draw-cap abort is at most \(G L_b 2^{-64(n+1)}\), using \((7/8)^{512(n+1)}\le e^{-64(n+1)}\le2^{-64(n+1)}\).

For a fixed central \(x\), apply the same variance estimate to its \(R_w\) left representations, now with at most \(2^{2a}\) representatives on any support. A choice of low residue \(c_w\), even fixed independently of the labels, gives probability at most \(4(P+2^{2a})/R_{\min}\) that fewer than \(R_w/(2P)\) of its representations fall in that cell. On the good events for its representation count and the overall class count, a uniform accepted left draw hits some representation of \(x\) with probability at least \(R_w/(4S_{w,1})\). Thus \(L_b\) independent uniform draws miss \(x\) with probability at most \(4 S_{\max}/(L_b R_{\min})\), using \(e^{-z}\le1/z\) for \(z>0\). These independent draws are an exact comparison for capped draws except on the already budgeted abort event.

Call a binary word covered if it has a representation in its stored left list, has a central weight, and none of the global list-pool or draw-cap bad events occurs. If classical table preparation aborts, define every word uncovered. For independent uniform \(x\), Hoeffding bounds the probability of a noncentral weight by \(2^{1-\lfloor 2u^2/k\rfloor}\). The full expected uncovered fraction is therefore at most the public rational expression
$$
 \mathcal E=2^{1-\lfloor 2u^2/k\rfloor}+kP/N
 +\frac{8G(P^2+P B_c)}{S_{\min}}
 +\frac{4(P+2^{2a})}{R_{\min}}
 +\frac{4S_{\max}}{L_b R_{\min}}
 +G L_b\,2^{-64(n+1)}.
$$
Require \(\mathcal E\le2^{-64}\). Each term tends to zero under the stated public class checks. In particular the leading exponents in the displayed ratios are strictly separated. The expected total squared phase-state mass on fibers containing any uncovered word is at most \(\sqrt{5\mathcal E}\). Indeed if \(U\) is the number of uncovered words and \(D=2^k\), at most \(U\) fibers contain one. Their phase-state mass is at most \(\sqrt{(U/D)(\sum_z m_z^2/D)}\) by Cauchy–Schwarz. Average and apply Cauchy–Schwarz again, using \(\mathbb E\sum_z m_z^2/D=\mu+1-1/N<5\). This covers arbitrary correlations between word coverage, label instance and the sizes of bad fibers.

## Finding words with a coherent target and a counted list scan

The desired residue \(z\) stays coherent. A right query consists of a central \(w\), an integer \(q\in[0,k]\), and a signed right half \(h\) from the right class at \(w\), represented by its lexicographic index. Use a padded binary space in which the \(w,q,h\)-index fields range over their least enclosing powers of two, taking \(S_{\max}\) as capacity for the index. The maximum possible ordinary binary sum is \(k(N-1)\), so every solution of residue \(z\) has full sum \(z+qN\) for some allowed \(q\). Define low membership by validity of all fields and
$$
 F_{\mathrm{int}}(h)\equiv z+qN-c_w\pmod P .
$$
The public constants \(c_w\) can be loaded by scanning all central weights, with a reversible comparison and XOR for each. Use a unitary \(A_z\) to prepare uniform padded query fields and a uniform coin \(j\) in a binary range of size \(J_1=2^{\lceil299n/1250\rceil+8}\), and apply \(j\) Grover iterations of low membership under classically streamed coherent guards. Retain the coin as part of the state. Every computational query field in the low-pass subspace has equal probability under this preparation after ignoring that coin. In the good pool event the cardinality of low-pass fields is between \(G(k+1)S_{\min}/(2P)\) and \(M_{\mathrm{lo}}=2G(k+1)S_{\max}/P\). The padded space has at most \(8G(k+1)S_{\max}\) fields. Thus its low-pass fraction is at least \(S_{\min}/(16PS_{\max})\) and at most \(2/P\). Require \(J_1^2\ge256 P S_{\max}/S_{\min}\). The geometric-series Grover bound gives low-pass probability at least \(3/8\) in \(A_z|0\rangle\) for every \(z\) on this event.

For a candidate \(h\), an exact oracle scans every saved left record, with equality to the candidate weight as an additional guard. It checks whether \(x=l+h\) is binary, whether \(\sum_i b_i x_i=z+qN\), and whether \(x\) differs from all already verified words for the current fiber. The integer sum test can add the stored signed sum to \(F_{\mathrm{int}}(h)\). A reversible binary counter records the number of matching records; flip the mark sign for a nonzero counter and uncompute. The capacity of the counter is all records, including duplicates. The oracle never uses a quantum address to read the classical table. Check all records in ordinary classical order. A marked field necessarily passes the low predicate, by the construction of its qualifying left half.

For a good fiber and a nonempty remainder, at least one right field is marked, by the representation covering each remaining word. The chance of initially finding a marked field under \(A_z|0\rangle\) is at least \(3/(8M_{\mathrm{lo}})\). Use randomized Grover search with respect to that initial state, implementing diffusion by the actual \(A_z\), its inverse, and a zero-state reflection. Use a fair zero-step branch and otherwise a uniform iteration count in a binary range of length \(J_2=2^{\lceil23921n/100000\rceil+8}\). Require \(J_2^2\ge128 M_{\mathrm{lo}}\). This gives trial success at least \(1/8\) for any such nonempty remainder. If no mark exists, verification never returns a word.

To verify and recover a word in a successful right field, stream the table again and select its first matching record. Count matches and set a fresh index to the first match, then reverse the count, without touching the recorded index. Drop the record data by uncomputation. A further streamed scan XORs the binary sum \(l+h\) at the selected index into a word register. An absence flag distinguishes no match. The earlier listing procedure with \(H=1024\) and 512 trials per slot now uses these right searches. Keep the trial coins, right fields and verification results coherent, choose the first successful trial and exclude its returned word at following slots. The canonical ordering, invalid-slot zeros, and compute–copy–uncompute proof are unchanged. On a fiber with at most \(H\) words, all covered and with the global events good, the norm error per clean lookup is at most \(2\sqrt{\delta}\), with \(\delta=H(7/8)^{512}<2^{-80}\).

## Arithmetic scratch and joint cost of the tables

The class rank data and the signed sums have \(O(n)\)-bit encodings. For reversible unranking without storing polynomially many arithmetic histories, use an equivalent register-level conversion by successive weighted radix steps. Keep the rank and remaining symbol counts. At each coordinate compare the current rank against the number of completions for each next symbol, select one symbol, and subtract the cumulative preceding completions. The counts and resulting symbol suffice to reverse the subtraction and restore the previous counts. The completion counts are binomial products of at most \(k\) binary factors. The reversible arithmetic details below implement these counts within \(O(n)\) scratch using bounded arithmetic. All prefix symbols are already required in the output word and record the branch of each step. To erase an unranking, reverse the steps using the output symbols and perform the inverse calculation. Index-invalid states use a separate range flag. Signed sum evaluation uses a rolling register of \(O(n)\) bits, additions of known constants under symbol controls, and reused scratch.

For completeness a method of obtaining each binomial count with linear scratch is to update the exact coefficient along the sequence \(\binom{M}{j+1}=\binom{M}{j}(M-j)/(j+1)\). Multiply by the short integer \(M-j\) into a fresh product, and divide exactly by \(j+1\), preserving the output. The original coefficient is uniquely determined by the final quotient, so compute the inverse rational update into temporary registers to XOR-clear the original after swapping. Extend all calculations by fixed scratch targets and use this cleanup on the valid coefficient subspace. Long division by a short integer uses reversible compare-subtract rounds with the quotient flags retained, and at most \(O(n)\) simultaneously live bits. Products are formed by linear-workspace reversible shift-add. Each multiplication/division takes polynomial gates, and the inverse update and reverse iteration clean all intermediates. Iterate from coefficient one, XOR the desired coefficient into its destination and reverse. If \(M,j\) are quantum counts, use controlled iterations over the public range \(0,\ldots,k\), with the counts retained, defining invalid inputs by an identity branch. The product of two binomial values obtains a completion count. Reuse scratch for each coordinate and never retain a history of all counts and multiplications. These constructions use \(O(n)\) qubits and polynomial time since only a constant number of \(O(n)\)-bit registers are live. Exact reversible circuits can use ripple arithmetic, comparisons, Toffoli, CNOT and X with clean work. Classical state generation consumes polynomial charged time per invocation. All coherent reads of candidate symbols use fixed, classically emitted wires. The only large persistent table is ordinary classical storage and is accessed by streams. The rule's address debit is \(O(n)\) because the allocation is at most exponential in \(n\). This is included in all suppressed polynomial factors.

The finite number of trial histories and retained fiber words is absolute. The coherent preparation and inverse, classic list scan, and arithmetic require \(O(n)\) live quantum registers measured in qubits. Every sample count remains exactly \(k\). The classical table holds \(G L_b\) words and signed sums, so peak ordinary classical bits are \(O(2^{(2393/10000)n})\) after absorbing polynomial factors. Left table construction takes \(O(2^{(5982/25000+9567/40000)n}\operatorname{poly}(n))\) work. Each right search uses \(O(J_2 (J_1+G L_b)\operatorname{poly}(n))\) work, since both \(A_z\) and its inverse are charged. This is at most \(O(2^{(47849/100000)n}\operatorname{poly}(n))\), all preparation, failures, lookups, verification and decoding included. The supported work envelope is \(O(2^{(957/2000)n})\). Both time and classical memory have growth index 1, and samples and quantum space have index zero.

All public checks hold eventually. Indeed \(k/n\to1\), \(w/k=1/2+o(1)\) uniformly over central weights and \(a/k\to349/20000\); Stirling's formula gives
$$
 n^{-1}\log_2 S_{w,i}\to H(5349,349,14302;20000),\qquad
 n^{-1}\log_2 R_w\to \tfrac12+\tfrac12 H(349,349,9302;10000),
$$
where \(H(a,b,c;d)=\log_2 d-(a\log_2 a+b\log_2 b+c\log_2 c)/d\). The first limit lies in \((95673838/10^8,95673840/10^8)\), and the second lies in \((71748841/10^8,71748844/10^8)\). These interval assertions can be checked entirely with rationals. For each positive integer logarithm in \(H\), write the integer as \(2^j x\) with \(1\le x<2\). Use
$$
 \ln x=2\sum_{i=0}^{11}\frac{t^{2i+1}}{2i+1}+\operatorname{tail},\qquad
 t=\frac{x-1}{x+1},\qquad 0\le\operatorname{tail}\le
 \frac{2t^{25}}{25(1-t^2)} .
$$
Use \(t=1/3\) to bound \(\ln 2\) and divide using the two interval endpoints. These inequalities provide the class and representation margins. The separate bounds on \(J_1,J_2\) have strict exponent margins \(0.47840-0.47837\) and \(0.47842-0.47840\), respectively, absorbing polynomial factors. All terms of \(\mathcal E\) tend to zero. The finite fallback uses the same \(k\) and error margins and has uniformly finite cost at every such \(n\). Thus the stated envelopes hold for all bit lengths with absolute multiplicative constants.

## Using the listing in the decoder

Retain the original (k) row bits (x), compute (z=F(x)) reversibly into a zero register, and perform the approximate clean listing into another zero register. Scan the listing with equality checks to compute into a fresh register the index of (x) among the valid words. Use that index to XOR the corresponding (k)-bit word into the original register, zeroing it in the ideal successful listing. The index has (k) bits and the scan compares against classical slot constants. Specify the scans on all inputs by XOR of each enabled value, so missing matches produce zero and even malformed scratch remains governed by a unitary circuit. With the listing still available, count the valid slots coherently to obtain the size \(m\). Conditioned on that count, send the rank's normalized uniform state on indices \(0,\ldots,m-1\) to zero. Use identity when the count is zero. The inverse operation, preparation, is an explicit finite-dimensional circuit: for each admissible \(m\), build a binary prefix tree on the first \(m\) indices. On each nonempty prefix rotate the next bit so that the two output probabilities are the fractions of its leaves in the two children. Arbitrary prefixes off this support can act as identity. Take the reverse circuit for erasure. Only the lowest \(\log_2 H\) rank bits are acted on, or all \(k\) if \(k<\log_2 H\). Include only sizes up to the dimension on those bits. Thus there are a fixed finite number of controlled rotations on a fixed number of wires, using the low rank bits and the count. Synthesize them as fixed Clifford+T words up to global phase with total operator error at most \(2^{-16}\). Multi-bit conditions can be built using Toffoli gates and uncomputed. For each controlled real Y rotation, conjugate its target by a fixed Clifford carrying the Y axis to Z. Compile the resulting controlled axial rotation using exact Boolean control and parity, as in spectral readout. Any conditional scalar phase is a single-qubit phase on the computed control flag. Uncompute the flag after the controlled operation. Synthesis up to global phase applies to the unconditional one-qubit gates of the decomposition, so the global phases are independent of the flag. This is uniform, since all target rotation entries are square roots of ratios of fixed bounded integers and a finite certified search for each needed fixed-precision rotation terminates by universality. Uncompute the count from the listing, then undo the listing and run the final spectral readout. Any residual work registers on erroneous paths may be discarded.

For the ideal comparison, use exact rank listing and erasure in every fiber. Let \(B=\{z:m_z>H\}\), \(p_B=D^{-1}\sum_{z\in B}m_z\), and let \(p_U\) be the squared mass on any fiber with an uncovered word on the main branch. On the direct fallback put \(p_U=0\). On good fibers, outside both exceptional sets, the two clean lookups and exact rank rotations give vector-norm difference at most \(4\sqrt\delta\) on the unnormalized good component by a two-call hybrid. Ideal intermediate states have clean lookup scratch and the target \(z\) is retained. Rotation synthesis is accounted for separately.

Before final spectral readout both the ideal and actual rank circuits keep \(z\) fixed. For any state supported on \(B\) of norm \(\sqrt{p_B}\), project onto the desired target eigenvector on \(z\), tensored with identity on all scratch. The projected norm is at most \(\sqrt{|B|/N}\sqrt{p_B}\) by Cauchy–Schwarz using the eigenvector's flat coefficient magnitudes. Since \(|B|/N\le \mu p_B/H\), each of these two heavy components contributes at most \(\sqrt{\mu/H}\,p_B\) to the projected norm. For the remaining component on uncovered light fibers, each projected norm is at most \(\sqrt{p_U}\). The difference in target probabilities is therefore at most \(8\sqrt\delta+4\sqrt{\mu/H}\,p_B+4\sqrt{p_U}\), using twice the vector norm upper bound for the difference of the squared norms. If a global classical table preparation aborts, all words are uncovered and the loss bound trivially exceeds one. No physical postselection on either exceptional set is performed.

The second moment gives \(\mathbb E p_B\le (\mu+1-1/N)/H<5/H\); the coverage estimate gives \(\mathbb E p_U\le\sqrt{5\mathcal E}\). Thus the mean target loss is bounded by
$$
 8\sqrt\delta + 40/H^{3/2}+4(5\mathcal E)^{1/4}.
$$
With \(H=1024\) the first two terms sum to less than \(1/800\). The last is less than \(2^{-13}\) by the public coverage check on the main branch. The uncovered-fiber term is zero in the direct fallback.

## Uniform spectral readout

Use binary-register phase estimation of the padded modular increment. Let (d=n+\lceil\log_2(n+2)\rceil+16) and (M=2^d). Prepare a uniform control of (d) bits, use controlled modular additions by the powers of two modulo (N), apply the inverse binary Fourier transform on the control and read its integer (y). Round (Ny/M) to the nearest integer and reduce modulo (N) (fix any deterministic tie rule). On an eigenvector of angle (b/N), the ideal probability of (y) is the squared geometric sum
$$
 \left|M^{-1}\sum_{t=0}^{M-1} e^{2\pi i t(b/N-y/M)}\right|^2.
$$
At circular distance (v>0) from (Mb/N) in integer units, the probability is at most (1/(4v^2)) by (\sin(\pi v/M)\ge 2v/M). A wrong rounding requires (v\ge M/(2N)). There are at most two outcomes per half-open unit-distance shell, and summing the reciprocal squares gives failure at most (1/(2(\lfloor M/(2N)\rfloor-1))). This is less than (1/(2^{14}(n+2))).

For raw source readout, analyze a hypothetical preliminary exact eigenvalue measurement on its position register. It does not affect the joint law of the reported label and the retained row, since the physical spectral readout preserves position eigenvectors and then discards the position register. Thus the ideal phase-estimation report can be coupled to the exact spectral label at the above cost per copy. The final spectral readout uses the same guarantee for the desired eigencomponent. Only (k+1) spectral readouts are used.

Use Clifford+T approximations to each controlled Fourier rotation with operator error up to global phase at most (2^{-16}/((k+1)d^2)). The inverse binary Fourier circuit has at most (d^2) rotations. A controlled phase can be constructed from one-qubit Z rotations and CNOT gates using the bit identity ab = (a+b-(a XOR b))/2. Use the uniform constructive Solovay–Kitaev synthesis algorithm with the fixed inverse-closed Clifford+T single-qubit generating set, as in Dawson and Nielsen, [The Solovay–Kitaev algorithm](https://arxiv.org/abs/quant-ph/0505030). Use polynomially many bits of precision and bit operations in (n) for this preprocessing. More specifically, it uses a fixed polynomial in (log(n+2)) for each rotation, including truncating its specified binary angle to the necessary precision and generating the gate sequence. Fixed starting nets and word libraries in the algorithm are absolute finite objects and can be compiled or generated as part of the uniform controller. The initial net and the recursive approximations can use a constant fraction of the target error for input accuracy and certify the operator-error bound using extra precision. By telescoping before measurements, the total change of output event probabilities from rotation synthesis is at most (2^{-15}).

The ideal rank erasure and exact final readout give success greater than \(2/3+1/400\). Bounded listing costs less than \(1/800+2^{-13}\), including heavy and uncovered fibers. Phase readout costs at most \((k+1)/(2^{14}(n+2))\le2^{-14}\) by coupling, and the combined synthesis costs at most \(2^{-14}\) in output event probability. Their sum is less than \(1/400\), giving success greater than \(2/3\) unconditionally for every \(N,s\).

## Joint guarantee

All main-branch work and allocation bounds are counted in the representation-table section. The public guards use only \(N\), before any source is acquired. On the finite fallback use the above direct search circuit, with the same sample count, heavy-fiber cap, spectral readouts, and exact rank erasure. Its worst-case cost is finite uniformly over outcomes for each such input length. Enlarging absolute constants covers all those lengths in the full envelopes. The complete bounds of this single configuration are \(T=O(2^{(957/2000)n})\), \(S_C=O(2^{(2393/10000)n})\), \(S_Q=O(n)\), and \(Q=k=O(n)\) with the exact public choice of \(k\) above. Their growth indices are respectively \(1,1,0,0\). The guaranteed malformed fraction is zero under the independent ideal promise.

## Sources

The Fourier-phase representation and the ideal subset-fiber measurement belong to the pretty-good-measurement framework of Bacon, Childs and van Dam, [Optimal measurements for the dihedral hidden subgroup problem](https://arxiv.org/abs/quant-ph/0501044). The bounded, reversibly sorted search construction implements that decoding here without assuming a subset-sum sampler. The randomized search schedule uses the averaging argument of Boyer, Brassard, Høyer and Tapp, [Tight bounds on quantum searching](https://arxiv.org/abs/quant-ph/9605034). Yukon candidate 6f49290 supplied the guarded modular-translation readout and the determinant-one argument for pairwise independence of nonzero binary subsets. The Poisson-window precursor supplies the adaptive copy count, the direct fallback, the canonical-list compute-copy-uncompute structure, and the ideal sample analysis. The signed left and right representations and the separate low-filter Grover preparation are inspired by Helm and May, [The Power of Few Qubits and Collisions](https://casa.rub.de/fileadmin/img/2_Forschung/2.1_Publikationen_PDFs/2020_The_Power_of_Few_Qubits_and_Collisions_Subset_Sum_below_Grover-s_Bound_Publication_ClusterofExcellence_CASA_Bochum.pdf). The proof here gives the uniform coverage analysis for arbitrary moduli, explicit measured classical left tables, the coherent right query, charged unranking and all-branch caps. Its collimation, residual balancing and target generation are not part of this construction.
