# Far-pair offset collimation under collective weight dephasing

For every \(N\ge2\) and \(s\in\mathbb Z/N\mathbb Z\), let \(n=\lceil\log_2 N\rceil\). The algorithm below uses the collective source model below, including independent ideal copies, and outputs the entire shift with probability greater than \(0.98\). Its simultaneous bounds on every branch are
$$
 T=O\!\left(2^{(9/8)\sqrt{n\log_2 n}+\sqrt n}\right),\quad
 S_C=O(n^2),\quad S_Q=O(n),\quad
 Q=O\!\left(2^{(1/4)\sqrt{n\log_2 n}-(1/4)\sqrt n}\right).
$$
The four indices are \(1/2,0,0,1/2\). The guaranteed malformed fraction is one in the stated collective model.

## Parameters and fallback

Let \(L=\lceil\log_2(n+2)\rceil\), \(g=16+L\), \(r_0=n-1\), and \(R=r_0-g\). Set \(l=\lfloor\log_2 n\rfloor\), \(L_*=L+\lceil\log_2(L+1)\rceil+64\), and
$$
 A=\lfloor\sqrt{nl}\rfloor-\lceil\sqrt n\rceil-8L-128,\qquad
 D=\left\lfloor A/(2L_*)\right\rfloor.
$$
Integer square roots and bit lengths compute these parameters exactly. If \(R\le0\) or \(D\le0\), use the fallback specified below. Otherwise let
$$
 B=\left\lfloor\frac{R-L_*D(D-1)/2}{D}\right\rfloor,\qquad
 f=R-L_*D(D-1)/2-DB.
$$
If \(B<1\), use the fallback. For \(i=1,\dots,D\), set \(d_i=B+(i-1)L_*+[i\le f]\) and \(e=\lfloor\frac12\log_2 B\rfloor-8\), evaluated by integer bit length. Use bucket bits \(b_i=d_i+e\), and let \(m_i\) be the least even integer at least \(b_i+L+16\). Put \(M=\max_i m_i\), \(r_i=r_{i-1}-d_i\), and \(P_i=2^{\sum_{j\le i}b_j}\), with \(P_0=1\). Thus \(r_D=g\). Use the main algorithm only if the following public checks pass:
$$
 b_i\ge1,\quad b_i\ge\lceil3m_i/4\rceil+16,\quad
 M\le4B,\quad M\le20(n+1),\quad g-e\ge0,\quad
 2^{g-e}\ge 2^{10}M,\quad(2^{28}M)^2\le2^{L_*}.
$$
Otherwise use the fallback. The analysis below proves that only finitely many bit lengths use it.

## The collective source model

Get the usual raw registers in consecutive blocks. Each main-branch block has \(8m_1\) copies. The fallback uses consecutive pairs. Before emitting a block of size \(J\), the provider starts with \(J\) fresh independent ideal coset states, independent of its memory and of existing solver registers, then acts on its private quantum memory with the isometry
$$
 \sum_{w=0}^J \Pi_w\otimes V_w ,
$$
where \(\Pi_w\) projects the block's branch qubits onto total Hamming weight \(w\), \(V_w\) is an arbitrary isometry on the provider memory into a common output space, and the position registers are untouched. This is one isometry since the projectors are orthogonal. The provider can select these isometries based on earlier blocks, classical outcomes known to it, and private records. Its memory can correlate multiple blocks and can be entangled with the solver through earlier deliveries. It cannot alter the chosen action within a block, access previously emitted registers, or access future private solver randomness. It emits the raw registers in order, and the algorithm may process each before the next arrives. The provider's retained preparation systems are inaccessible.

This promise admits weight-dependent coherent memory even when it cannot be expressed as a distribution of classical common phase rotations. For instance, for a two-copy block, isometries can append a flag zero on weights zero and one and flag one on weight two. The overlaps for weight differences \(1-0\) and \(2-1\) differ, whereas a distribution of common rotations would give identical overlaps at equal differences. Choosing identical isometries for all weights produces independent ideal copies. The algorithm sees no flags. Every acquired register may be malformed by this channel, so the claimed fraction is \(1\), with the stated restriction on its form.

## Fallback

Test candidate shifts \(u=0,\dots,N-1\). In a trial on two fresh copies from one block, subtract \(u\) modulo \(N\) from each position register conditioned on its own branch one. Measure the parity of the two branch bits and discard the pair on even parity. It is odd with probability \(1/2\), independently of the supplier memory and prior history. On odd parity the two branch words are \(01,10\), so the same \(V_1\) acts on the supplier memory. For each underlying ideal offset pair, when \(u=s\) the two position states coincide, and when \(u\ne s\) they are orthogonal. Decode the odd sector into a qubit by CNOT and the parity measurement, and measure that qubit in \(X\). The sign is always plus for \(u=s\), and fair for a wrong candidate conditional on the past. These conditional laws hold even when the supplier memory is entangled with earlier solver registers: tracing after the common isometry preserves their reduced state.

Require \(k=n+8\) odd trials all with plus. Reject after the first minus or when \(8k\) pairs have been used without accumulating \(k\) plus observations. Return the first passing candidate, or zero if none passes. For the right candidate the shortage probability is at most \(e^{-9k/8}\) by a binomial Chernoff bound with mean \(4k\). The wrong-pass probability is at most \(2^{-k}\) per candidate, using the conditional fair sign at each reached odd outcome. Therefore total failure is less than \(2^{-8}+e^{-9(n+8)/8}<0.02\). The uniform cap includes all discarded even outcomes. Reusable ripple arithmetic implements the two controlled translations exactly with \(O(n)\) working wires, fixing invalid residue encodings. The finite prefix in \(n\) covered by this fallback will be absorbed into the eventual resource envelopes.

## Row interface

Write \(\phi(a)=(|0\rangle+\exp(2\pi i as/N)|1\rangle)/\sqrt2\). All row labels for phases are understood modulo \(N\). A successful level \(i\) generator for a specified target \(a\) returns an exactly uniform residual \(x\) in \([0,2^{r_i})\) and a row \(\phi(a+P_i x)\) in the uncapped ideal comparison. A level-zero child is conceptual and is prepared within the level-one block procedure below.

At level \(i>0\), each completed child preparation gives \(m=m_i\) independent rows at level \(i-1\), one at target \(a\) and the others at zero. At level one the next section defines the preparation and its joint measurement. At higher levels invoke the child generator separately for each row. Denote the designated bit by \(z_*\). Set \(b=b_i\), \(Q_b=2^b\), and \(H=2^{r_{i-1}-b}=2^{r_i-e}\). Each child residual is \(l_j+Q_b h_j\). The \(l_j\)'s are independent uniform residues modulo \(Q_b\), the \(h_j\)'s are independent uniform integers in \([0,H)\), and the lists are independent.

Measure the Hamming weight \(w\) of the row word \(z\) and its modular low sum \(u=\sum_j l_j z_j\bmod Q_b\). Keep weights within \(K=\lfloor\sqrt m/4\rfloor\) of \(m/2\). Classify the words of the measured fiber according to \(z_*=0\) or \(1\). In each class put them in increasing word order, and match by rank up to the shorter class size. For implementation these lists are replaced by the verified bounded lists below. Reject matched pairs whose Hamming distance is at most \(\lfloor m/8\rfloor\). A diagonal rank measurement distinguishes each retained pair with a positive tag, all other words having tag zero. If positive, uncompute all row wires other than the designated bit with controlled flips based on the two known endpoints. The surviving state is \(\phi(a+P_i d)\), where
$$
 d=c+\sum_j(z_{1,j}-z_{0,j})h_j,\qquad
 c=Q_b^{-1}\sum_j(z_{1,j}-z_{0,j})l_j.
$$
The equality of buckets makes \(c\) integral and \(|c|\le m\). The equal Hamming weights give \(t\) positive and \(t\) negative coefficients. The distance check gives \(t>m/16\), and \(t\le m/2\). All pair choices and measured tag probabilities use only the low labels and independent search coins, since the measurements are diagonal and the initial magnitudes are all equal. Thus the higher digits retain their independent uniform distribution conditional on the chosen pair.

## Streaming raw blocks into the first transition

In the ideal representation of each raw copy, measuring the position in the modular-increment eigenbasis reports a uniform latent \(k\) and leaves the branch \(\phi(k)\). The position eigenvector's coefficients are \(N^{-1/2}\exp(-2\pi i kx/N)\), so the two branches at \(x,x+s\) have that relative phase, independently of the mixture offset. The collective isometry acts on branch weights and leaves all position registers alone. Thus the ideal latent labels remain independent uniform over the block. Conditioned on them, the branch product \(\bigotimes_j\phi(k_j)\) has undergone the prescribed weight-controlled isometry. This representation is used for the proof. The actual readout uses guarded phase estimation as below.

At level one, acquire the next complete block of \(8m_1\) raw copies. In the first eight positions, keep the first label with \(x=(k-a)\bmod N<2^{n-1}\) for the designated row. In the other \(8(m_1-1)\) positions, keep the first \(m_1-1\) labels with \(x=k<2^{n-1}\). Drop every other branch register. Extract and process the positions one at a time. Finish the entire block even when enough rows have been kept. If too few were kept, reject this level-one attempt. Each label passes its prescribed filter with probability \(2^{n-1}/N\ge1/2\). The designated shortage probability is at most \(2^{-8}\); the ordinary shortage probability is at most \(e^{-9(m_1-1)/8}\) by the binomial lower-tail bound. In particular sufficient rows are prepared with probability greater than \(1/2\). Conditional on this event, the accepted residuals are mutually independent uniform in their prescribed intervals. This is because, conditional on the filter bits, the labels of passing positions are independent uniform on their respective allowed sets, and all kept positions are chosen using the filter bits alone.

Implement the weight-bucket measurement by measuring weight first and then the low sum. For fixed latent labels and kept positions, trace the discarded branch registers in their computational word basis. For a fixed discarded word \(d'\) and a kept word of measured weight \(w\), the memory operation is \(V_{w+\mathrm{wt}(d')}\) regardless of the kept word's particular bits. Thus after projecting to weight \(w\) the conditional kept phase state is exactly the ideal projected state for all \(d'\). The probability of \(w\) is the binomial weight law, since all word magnitudes are equal and the operations on memory are isometries. This argument holds for an arbitrarily entangled joint state of the old solver registers and provider memory by including a purifying reference. For each \(d'\) the same isometry factors from every kept term; tracing the memory, and summing the discarded words, preserves the old solver's reduced state and makes the measured kept system independent of it except through classical controls. A shortage also preserves the old solver state, since it is based on label filter bits whose joint law is independent of the memory, followed by discarding the block systems. Thus the first transition after the weight measurement has the same conditional phase and bucket laws as the clean computation, with the sole additional failure possibility of an insufficient block. All later levels operate on the resulting clean conditional phase rows. Neither provider memory nor even earlier adaptive choices can change those conditional laws.

## A cap on listing with a constant success lower bound

First analyze the ideal complete lists before the distance check. Condition on the designated low label. For a retained weight \(w\), the two classes consist of nonzero ordinary binary words of weights \(w,w-1\) on \(m-1\) bits. Their sizes \(S_0,S_1\) both exceed \(2^{m-1}/(16v)\), where \(v=\lceil\sqrt m\rceil\). For details, the binomial law of \(m-1\) fair bits gives weight within \(\sqrt m\) of its mean with probability at least \(3/4\) by Chebyshev. There are at most \(4\sqrt m\) such values, so its central binomial masses are at least \(3/(16\sqrt m)\). At up to \(K\) steps from a nearest central maximum, the product of the adjacent binomial ratios is at least \(1-2K(K+1)/m\ge3/4\) by bounding each ratio at step \(j\) below by \(1-4j/m\). The lower bound \(1/(16v)\) follows, as does \(2K+1\ge v/8\).

For any fixed retained weight and bucket, write \(C_0,C_1\) for the class occupancies and \(\mu_j=S_j/Q_b\). Distinct ordinary nonzero binary words have a two-column minor of determinant plus or minus one. Consequently their low sums are independent uniforms, given the designated label. Each occupancy has variance at most its mean. Its mean is at least \(2^{L+11}/v\ge32\) by the checks on \(M\). Chebyshev gives probability at least \(3/4\) that both counts are at least half their respective means. Hence \(\mathbb E\min(C_0,C_1)\ge(3/8)\min(\mu_0,\mu_1)\). Each matched pair contributes two phase words out of \(2^m\). Summing over buckets and retained weights gives a probability at least \(3/1024\) of observing a valid pair from the complete-list procedure.

The expected mass of complete matched words that fail the distance check is at most \(2^{3m/4-b}\le2^{-16}\). Indeed for any word in designated class zero, the number of nearby words is at most \(2^{3m/4}\). To bound it, use
\(\sum_{j\le m/8}\binom mj\le2^{m/8}(3/2)^m\le2^{3m/4}\). A given distinct pair is in the same bucket with probability \(1/Q_b\), by conditioning on all low labels except one with a nonzero unit difference. The expected number of such pairs is bounded by summing over the at most \(2^{m-1}\) possible class-zero endpoints. Each selected pair costs only two words, and this calculation even counts close pairs the procedure would not have selected.

Use a list cap \(U=2^{16}(1+2^{m-b})\) for the combined measured fiber. For a retained weight let \(C=C_0+C_1\). Since each \(\mu_j\le2^{m-b}\), the inequality \(C^2\le2C_0^2+2C_1^2\) and the above variance calculation give
$$
 2^{-m}\sum_{w,u}\mathbb E C^2\le 2(1+2^{m-b}),
$$
where the sum includes only retained weights and all buckets. This follows by summing \(\mathbb E C_j^2\le(1+2^{m-b})\mu_j\), whose total mean over both classes and all measured labels is at most \(2^m\). The chance of measuring such a fiber of size exceeding \(U\) is at most \(2^{-m}\sum_{w,u}\mathbb E C^2/U\le2^{-15}\).

The actual listing circuit performs at most \(U\) discovery slots. Each slot gets \(128\lceil\log_2(U+2)\rceil+512\) trials to find a new word of the measured bucket and weight. Trials use a fresh uniform selector word and a fair bit to choose between uniform guessing and a uniformly randomized Grover schedule of \(j\in[0,2^{\lceil m/2\rceil+2})\) iterations. Verify each result on measurement and only accept a match absent from the saved list. If a slot finds none, end listing. The stored list, even on error, consists of distinct true members. If any match remains, each trial succeeds with probability at least \(1/8\). For a fraction of marks above \(1/2\), the no-iteration branch alone suffices. Otherwise write \(\sin^2\theta\) for the fraction of marks. The average of \(\sin^2((2j+1)\theta)\) is at least \(1/2-1/(2J|\sin 2\theta|)\) by the geometric sum, with \(J=2^{\lceil m/2\rceil+2}\), and \(\sin 2\theta\ge\sqrt{2/2^m}\). This gives the stated conservative bound including the mixture probability. On a fiber of size at most \(U\), conditioning on earlier slot outputs and union bounding gives probability below \(2^{-16}\) of stopping with any match still missing. This algorithm has a worst-case finite schedule even on heavy fibers. Its queries use fresh work registers independent of the held row state.

Build the two class lists by sorting the verified words, then emit one reversible equality test per usable word to write the known pair tag into a fresh register by XOR. The measured positive tag identifies the two words classically. These gates are classically addressed and every emitted test is charged. If the complete list and verified list agree, pair selection after the distance check agrees. Even when they differ, any returned pair obeys the bucket, weight, and distance constraints. Subtracting the three losses from the complete-list success lower bound gives probability greater than \(1/512\) of measuring a retained pair.

## Uniform output over a wider high interval

For a selected pair let \(Y=\sum_{j=1}^t(U_j-V_j)\) with \(U_j,V_j\) independent uniforms on \([0,H)\), so \(d=c+Y\), and let \(\sigma^2=t(H^2-1)/6\). The signed sum is symmetric and unimodal. A centered symmetric unimodal mass on integers is a nonnegative linear combination of indicators of centered integer intervals. The convolution of two such indicators has symmetric masses nonincreasing away from their combined center, by counting interval intersections. The difference of two uniforms is symmetric and triangular, so iterative convolution gives the claim for \(Y\).

An individual uniform has variance \((H^2-1)/12\) and centered fourth moment \((H^2-1)(3H^2-7)/240\), at most three times its variance squared, by the elementary sums of powers of integers. Expanding the fourth moment for the independent centered summands gives \(\mathbb E Y^4\le3\sigma^4\). Paley–Zygmund on \(Y^2\) gives \(\Pr(|Y|\ge\sigma/2)\ge3/16\), and Chebyshev gives \(\Pr(|Y|>4\sigma)\le1/16\). The annulus between these radii contains at least \(1/8\) mass and at most \(8\sigma+1\le9\sigma\) integers, since \(\sigma\ge1\). By unimodality every integer with \(|y|\le\sigma/2\) has probability at least \(1/(72\sigma)\). Also
$$
 H\sqrt m/12<\sigma\le H\sqrt m,
$$
using \(H\ge2\), \(m/16<t\le m/2\), and \((H^2-1)/6\ge H^2/8\). For every \(d\in[0,2^{r_i})\), the required argument satisfies
$$
 |d-c|\le 2^e H+m
 \le H\sqrt m/256 + H/1024
 < \sigma/2 .
$$
The bounds use \(2^e\le\sqrt B/256\), \(m\ge B\) if \(e\ge0\), and the following direct extension when \(e<0\): since \(m\ge B+e+L+16\), \(e\ge-8\) and \(L\ge1\), we still have \(m\ge B\). The input guard gives \(H\ge2^{10}M\).

Write \(p_d\) for the exact probability of this value given the pair and low data. Keep \(d\) inside the prescribed interval with probability \(1/(128v H p_d)\), otherwise reject. This probability is at most one by \(p_d\ge1/(72H\sqrt m)\). For each conditional pair law the result is exactly uniform on the interval given success. The probability of this final acceptance, conditioned on a retained pair, is \(2^e/(128v)>2^{-18}\), since \(2^e>\sqrt B/512\) and \(v\le2\sqrt m\le4\sqrt B\). Pairing and thinning together succeed with probability greater than \(2^{-27}\). For the first transition also multiply by its conditional block preparation probability above \(1/2\). Thus \(p_*=2^{-28}\) is a uniform lower bound at all levels, including level one.

The conditional probabilities are rational and computable by counting bounded compositions. Replace each of the \(t\) negative uniforms by \(H-1\) minus an independent uniform; to get \(Y=d-c\), the new sum of \(2t\) nonnegative entries must be \(z=d-c+t(H-1)\). The numerator counting such words in \([0,H)\) is
$$
 \sum_{j=0}^{2t}(-1)^j\binom{2t}{j}\binom{z-jH+2t-1}{2t-1},
$$
where the second binomial is zero for \(z-jH<0\). Inclusion-exclusion gives this formula. The denominator is \(H^{2t}\). The terms, partial sums, and rational acceptance fraction can be generated and stored in \(O(nm)\) bits by elementary multiplication and exact division with polynomial work. Use a draw from the fraction's denominator range, with a bounded rejection implementation below.

## Separate deterministic work and sample budgets

In an ideal comparison with no global budgets, each call retries using fresh blocks until success. The level-one transition succeeds with conditional probability at least \(p_*\), and the residual is uniform conditional on success and all past observations. By induction on finite depth, every child call terminates almost surely with the specified uniform output, the conditional phase being pure and independent of provider memory. A fresh parent attempt succeeds with conditional probability at least \(p_*\) and yields a uniform successful residual. The first accepted attempt preserves that law. Independence includes the contents of a returned row conditioned on its classical residual and supplies a product of correctly labeled phases for each parent. The actual coherent branch registers from earlier successful child calls are isolated during the later recursive calls.

At the top, for each of the \(n+16\) targets \(2^j\bmod N\) for \(0\le j<n+16\), call the top generator until its residual is zero. In the ideal comparison this succeeds with probability \(2^{-g}\) per top call and yields the exact target phase. Let \(C_0=(n+16)2^g\). Set
$$
 A_i=\prod_{j=i+1}^D (2^{28} m_j)\quad(0\le i\le D),\qquad
 w_i=2^{\lceil m_i/2\rceil}\quad(1\le i\le D).
$$
Each first-level attempt costs exactly \(8m_1\) raw acquisitions, so the expected total raw draws are at most \(8 C_0 A_0\). The expected number of level-\(i\) transition attempts is at most \(2^{28}C_0 A_i\). These expectations count failed attempts. The derivation iterates the geometric retry bound at each level. More explicitly the cost of an individual attempt may correlate with its own acceptance. The event of reaching an attempt depends only on previous attempts, so its future fresh cost has the same expectation, and summation over reached attempts yields a factor at most \(1/p_*\). Apply the same calculation at the outer zero-residual filter, then sum over all targets.

Use two hard budgets computed exactly before drawing any samples:
$$
 R_{\max}=2^{10}\cdot8 C_0 A_0,\qquad
 W_{\max}=2^{10}\cdot 2^{28} C_0\sum_{i=1}^D A_i w_i .
$$
Charge each raw acquisition one unit against \(R_{\max}\), checking that an entire block fits before acquiring its first copy. Charge each transition attempt \(w_i\) against \(W_{\max}\) at its start, before requesting its children or a raw block. If a budget would be exceeded, abort and output zero. Any children already constructed on a later aborted branch have been charged. Markov's inequality in the ideal comparison gives total probability at most \(2^{-9}\) of crossing at least one budget. The hard caps therefore give a bounded actual algorithm that agrees with the ideal comparison apart from that loss and the implementation errors below.

A rational acceptance coin with denominator \(B_c\) is drawn using the least enclosing binary range, rerolling if the draw is outside \([0,B_c)\). Use at most \(\lceil\log_2 W_{\max}\rceil+20\) trials, aborting globally if exhausted. On each attempted draw the rejection probability is less than \(1/2\). Only one such coin is requested per transition attempt, and the cap counts at most \(W_{\max}\) attempts, so a coupling with unlimited rejection loses at most \(2^{-20}\). A Grover schedule draw uses exact fixed-length fair bits from \(H\) and \(Z\) measurement, with no rejection needed. Every aborted branch still pays for the coins and other work already performed.

## Source precision and full-shift recovery

Use modular increment on the valid residues, identity on padding. Binary phase estimation on a source position register uses \(n+h\) control bits with \(h=\lceil\log_2 R_{\max}\rceil+20\), controlled modular translations by the prescribed powers of two, an inverse binary Fourier transform and nearest-\(1/N\) rounding of the report. Up to synthesis error, its label is coupled to the ideal latent label with failure at most \(1/(2(2^{h-1}-1))\). Indeed on an eigenphase, the probability of a report at nonzero circular distance \(d\) in control-lattice units is at most \(1/(4d^2)\) by the geometric sum and the inequality \(\sin(\pi d/2^{n+h})\ge2d/2^{n+h}\) on the first half of the circle. Wrong rounding needs distance at least \(2^{h-1}\). Summing two lattice points per unit-distance shell proves the bound. The comparison changes only the position label report. It preserves the conditional branch and memory state from the collective source section, since phase estimation leaves the position eigenvector unchanged and the exact spectral decomposition is a classical mixture of latent label tuples. Approximate the Fourier gates with total operator-norm error, up to global phase, at most \(2^{-20}/R_{\max}\) per readout. Clifford+T synthesis is described in the work accounting. A hybrid over at most \(R_{\max}\) acquisitions gives discrepancy less than \(2^{-18}\) in the output distribution, including adaptive stopping. The ideal label coupling acts on positions and thus still holds with the collective branch isometry, the previous solver state and supplier memory. Synthesis error applies to every joint state by operator-norm control and contractivity under the subsequent joint channels. The same provider strategy is used in the hybrid conditioned on the available classical history. Treat skipped readouts after halt as identity to apply the hybrid to the fixed cap.

When all targets are returned, the row product has amplitude proportional to \(\exp(2\pi i z s/N)\) on binary word \(z\) of \(n+16\) bits. Apply the inverse binary Fourier transform to that product, measure, and round to the nearest point of denominator \(N\). The same circular tail bound with \(h=16\), plus a total synthesis norm error at most \(2^{-13}\), gives failure less than \(2^{-10}\). Combining the probability bounds for budgets, coin exhaustion, raw precision and final decoding leaves unconditional success greater than \(0.98\). The exact two-copy fallback meets the same guarantee under this model.

## Resource accounting

A modular addition by a controlled constant uses \(O(n)\) exact gates and temporary bits or wires. Compute the ripple sum, comparisons and conditional subtraction into scratch, and reverse the Boolean circuit after copying output. Extend the result by identity on invalid encodings. Evaluate into a fresh word, swap, and use the inverse addition to zero the old word. Classical generation streams addresses and constants. Weight and low sum predicates for a selector on \(m\le O(n)\) wires are implemented by a succession of modular additions and ripple increments with reused scratch, and tested against the measured values. Exclusion of verified words is a classically streamed equality circuit. Each equality flag for a word can be XORed into a single exclusion flag then uncomputed, since the list entries are distinct and a candidate can match at most one. All these gates and diffusion are implemented exactly with Toffoli, CNOT, Clifford gates, their inverses, and their fixed exact Clifford+T decompositions. All initialization, addressed bit access and gate costs are included. The complete bounded listing, matching, tagging, uncomputation and rational thinning at level \(i\) use at most \(O(w_i\,\mathrm{poly}(n))\) charged work beyond their already charged child calls. This follows from \(U=O(n)\), the polynomial number of capped trials, and \(O(w_i)\) iterations per trial. Sorting uses \(O(Um)\) bits and polynomial charged time. Exact label generation, all cap counters and loop bookkeeping, and release of intermediate registers cost polynomial work per counted action, plus one polynomial setup and finalization cost.

Each synthesized controlled Fourier rotation can be decomposed into unconditional one-qubit axial rotations and exact CNOT gates via the parity formula \(xy=(x+y-(x\operatorname{xor}y))/2\) for bits. The constructive Solovay–Kitaev algorithm applied to the fixed inverse-closed single-qubit Clifford+T set emits words of length \(O(\log(1/\eta)^{3.97})\) for accuracy \(\eta\) in operator norm up to global phase. The controller compiles one rotation at a time with an evenly divided error budget, using rational phase approximations at guard precision within the error budget. Constant-size matrix arithmetic and bounded-depth recursive synthesis use \(O(\log(1/\eta)^2+\log(1/\eta)\log\log(1/\eta))\) bits of arithmetic and stack scratch, in addition to the word symbols, by retaining only local matrices along the logarithmic-depth recursion. The input dyadic angle and its approximation are uniform and the base library is fixed. The approximation orders and size bounds of this standard synthesis have polynomial classical work in \(\log(1/\eta)\). Here \(\log(1/\eta)=O(\log(R_{\max}n))=O(\sqrt{n\log n})\), as shown below. Since \(3.97<4\), the word length and working precision fit \(O(n^2)\) bits and cost polynomial work per physical readout. All controlled translations and exact reversible logic use bounded workspace as described above.

Depth-first recursion keeps at most \(DM=O(n)\) child row qubits plus \(O(n)\) final rows and the current source and \(O(n)\) search/weight/sum/measurement scratch. The verified lists are classical, and only one exists at a time, after the relevant children have returned. During a raw block the controller holds at most one position register and its phase-estimation scratch, plus at most \(m_1\) selected branch wires. The supplier retains any not-yet-emitted registers and its private memory, which are not solver workspace. Thus the quantum peak is \(O(n)\), including discarded register initialization and active recursion. Classical label descriptors of \(O(n)\) bits each require \(O(n DM)=O(n^2)\) bits. The list has \(O(Um)\) bits and the rational arithmetic \(O(nm)\) bits, both \(O(n^2)\), including all explicit control counters. The budget estimates below fit \(O(n)\) bits each; storing all per-depth fields and counters is within the same classical allocation. Quantum-addressed memory access is unnecessary. The deterministic charged work is bounded by \(O((1+R_{\max}+W_{\max})\mathrm{poly}(n))\).

## Envelopes and uniformity

Let \(L_0=\log_2 n\), \(Z=\sqrt{nL_0}\) and \(S=\sqrt n\). We have \(L=L_0+O(1)\), \(L_*=L_0+O(\log L_0)\), and \(A=Z-S+o(S)\). In the last identity, replacing \(L_0\) by \(l\) in the first square root changes it by \(O(S/\sqrt{L_0})=o(S)\). The explicit \(8L+128\) reservation and integer rounding are also \(o(S)\). Consequently,
$$
 D=(Z-S+o(S))/(2L_*),\qquad B/Z\to7/4,\qquad d_D/Z\to9/4 .
$$
The latter limits follow by substituting \(R=n-O(\log n)\) into the definition of \(B,d_i\), including the rounded remainder. Uniformly \(e=O(\log n)\) and \(m_i=d_i+O(\log n)\). Thus the checks \(B>0\), \(M\le4B\), \(b_i\ge\lceil3m_i/4\rceil+16\), \(M\le20(n+1)\), and \(g-e\ge0\) eventually hold. For the high interval guard, \(2^{g-e}/M\) tends to infinity because \(2^g\ge2^{16}(n+2)\), \(2^e\le\sqrt B/256\), and \(M\sqrt B=O((n\log n)^{3/4})\). Also \(M\le 3\sqrt{nL}\) eventually. This gives
\(\log_2(2^{28}M)\le 30+(L+\log_2 L)/2\le L_*/2\), so the last guard eventually holds. The exact public checks, rather than an asymptotic threshold, determine the branch.

Throughout the main branch every factor \(2^{28}m_i\) is at most \(2^{L_*/2}\). The raw budget satisfies
$$
 \log_2 R_{\max}\le D L_*/2+2L+O(1)
 \le Z/4-S/4 + O(1).
$$
Here the explicit guard in \(A\) subtracts \(32L\) after division by four. The bounds \(l\le L_0\) and \(\lceil S\rceil\ge S\) apply for all main lengths. In the weighted budget,
$$
 \log_2(A_i w_i)\le (D-i)L_*/2 + (B+(i-1)L_*)/2 + O(L)
                 = B/2+(D-1)L_*/2+O(L)
$$
uniformly in \(i\). The logarithm of the number of terms and the outer factors are \(O(L)\). Using the definition of \(B\), we obtain
$$
 \log_2 W_{\max}\le R/(2D)+(D-1)L_*/4+O(L)
                  = (9/8)Z+(7/8)S+o(S).
$$
For the last equality, \(nL_*/Z=Z+O(S\log L_0/\sqrt{L_0})=Z+o(S)\), so expansion of \(R/(2D)\) at \(Z-S+o(S)\) gives \(Z+S+o(S)\). The second term is \((Z-S)/8+o(S)\). The strict gap from \(7/8\) to 1 absorbs the \(o(S)\) term and every fixed polynomial work overhead. The raw budget has smaller leading exponent than this work budget. This proves the stated work and acquisition envelopes. The finitely many fallback bit lengths have finite branchwise resource maxima, so enlarging the absolute constants covers them, including \(n=1\). The stretched exponentials have exact growth index \(1/2\), and the polynomial workspace envelopes have index zero.

## Prior work

The direct clean-source precursor supplies the far-pair filter, wide-interval thinning, integer schedule and deterministic resource budgets. The new features are the streamed block-weight projection, its source-error proof, the block-specific budget change and the exact pair-weight fallback. The clean Fourier row interface, designated offset, central equal-weight pairing and bounded-composition thinning start from Yukon submission 6f49290a-4e30-41fd-933e-9916667f3cc4. The proof here uses a distance threshold and a fourth-moment annulus estimate so that thinning leaves a much wider uniform interval with constant probability. Verified Grover listing and separate Markov budgets use the general approach of the dense collimation at e2d3ffa5-7cea-4cf3-a9f8-9b9d75a2f75a. This variant uses ordered bipartite pairs and an exact offset rather than cyclic neighbors and a signed-leaf decoder. The randomized iteration bound follows Boyer, Brassard, Høyer and Tapp, [Tight bounds on quantum searching](https://arxiv.org/abs/quant-ph/9605034). For uniform synthesis see Dawson and Nielsen, [The Solovay–Kitaev algorithm](https://arxiv.org/abs/quant-ph/0505030).
