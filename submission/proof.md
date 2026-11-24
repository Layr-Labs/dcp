# Collimation with globally diverse correlated coset preparations

## 1. One counted algorithm

Let $N\ge2$, $s\in\mathbb Z/N\mathbb Z$, and $n=\lceil\log_2N\rceil$.
The algorithm below recovers the entire secret with probability at least
$1-2^{-7}$ under the source promise of Section 2. Its branchwise envelopes
are $O(2^{c\sqrt n})$ work, $O(n)$ classical bits, $O(2^{c\sqrt n})$
allocated qubits and $O(2^{c\sqrt n})$ source copies, where
$c=288675134594813/250000000000000$. The same configuration covers
the independent ideal source and malformed fraction 1 in the stated
model.

Use the PCROOT-1 logical program, physical bank and polynomial odd-cell
compiler in virtual.md, base-bank.md and odd_partition.md on the main
branch $n\ge2^{512}$, with the following interface changes. Compute its
public logical source cap $C=4nC_0+K$ before any allocation by the
rolling parameter pass. On the finite branch define $C$ as in Section 7.
For both branches put
$$
 L=\lceil\log_2 C\rceil,\quad
 d=\left\lceil\frac{\lceil\sqrt n\rceil}{\max(1,\lceil\log_2 n\rceil)}\right\rceil,
 \quad\delta=2^{-d},\quad w=64\cdot 2^d(n+L+32),\quad Q=wC.
$$
Acquire all $Q$ raw copies in a counted array before drawing any private
random bits or performing any measurement. Then shuffle the array using
Section 4 and divide the shuffled order into $C$ consecutive blocks of
size $w$. Initialize any inherited bank after these deliveries. Compute the ceilings in the schedule by integer roots, integer bit lengths and upward division.

Process the blocks in order as the solver requests new logical copies.
Replace the original acquisition, source transform and LE sequence by
the mixer of Section 3, which returns one reported label and one phase
row. Apply every subsequent control flip, label rejection or reduction,
and record allocation in the base program as written. The finite branch
instead uses Section 7. If an abort or a successful answer ends a branch
before the last block is used, discard the unused registers. They were
acquired and remain counted. Each branch, including an abort after initialization, acquires exactly $Q$.

## 2. Correlated source model

Write $\omega=e^{2\pi i/N}$ and define
$$
 \chi_k=N^{-1/2}\sum_y\omega^{ky}|y\rangle,\qquad
 \phi_k(s)=(|0\rangle+\omega^{-ks}|1\rangle)/\sqrt2,\qquad
 v_k(s)=\phi_k(s)\otimes\chi_k .
$$
Let $V_s$ be the span of the $N$ orthonormal vectors $v_k(s)$.
A latent label is an index of this basis. The clean density operator
is the uniform mixture of its basis projectors.

The source supplies one of the following types of joint state, without
disclosing its type, any labels, or which copies are malformed. A
classical mixture of allowed specifications is permitted. Condition on
the provider's classical specification in the analysis.

**Product spectral preparations.** Clean copies are independent ideal
states. Each malformed register is in any density matrix $\sigma$
supported on $V_s$ whose diagonal distribution $p_\sigma(k)$ obeys
$|\sum_k p_\sigma(k)\omega^{jk}|\le 1-\delta$ for each nonzero $j$ modulo
$N$. Conditional on the specification all raw registers form a product.
The provider may choose different states and classically correlate the
choices across positions.

**Correlated spectrally diverse preparations.** Clean positions are in
independent ideal states in tensor product with all remaining systems.
The $m$ malformed positions are in an arbitrary joint state, possibly
entangled with one another and an external reference, supported on
$V_s^{\otimes m}$ in their registers. If $m\ge Q/2$, its joint diagonal
in the product basis has support only on label tuples
$(k_i)_{i\,\mathrm{malformed}}$ such that for every nonzero $j$ modulo $N$,
$$
 \frac1m\sum_{i\,\mathrm{malformed}}\Re(\omega^{j k_i})\le 1-\delta.
$$
If $m<Q/2$, there is no restriction on the latent-label joint
distribution of the malformed registers beyond the common support
condition $V_s^{\otimes m}$.

The source cannot access the delivered registers or the solver after
delivery. All choices precede any solver measurement or random draws.
The promise applies to the whole acquired batch and allows any number
of malformed copies up to $Q$. The model excludes phase errors that
leave $V_s$. Within $V_s$ the second type allows arbitrary label
coherence and entanglement, subject to the diagonal spread promise
when malformed copies are at least half the batch.

A correlated example is a uniform coherent sum over distinct ordered
permutations of a common multiset containing each label equally often.
This example applies with $m=Q$ when $Q$ is divisible by $N$. Each tuple has every nonconstant
empirical coefficient zero. An individual register is in general
correlated with the others, and the input needs no independent ideal
copy. For batch sizes here much smaller than the modulus, there also
exist spectrally diverse tuples with unequal or unrepeated labels:
independent uniform labels satisfy this diversity constraint with
positive probability by the same independent-label concentration
argument as Section 5, since the clean label expectation of the real
part is zero and $1-\delta\ge1/2$. Superpositions of distinct certified
tuples are permitted, with exact phases and amplitudes unknown to the
solver. The product model also permits each label law to be
`(1−delta) point mass at zero + delta uniform`, whose nonconstant
coefficients are exactly $1-\delta$. The gap may vanish with $n$,
while all its arithmetic and actual block widths are specified.

## 3. Exact row mixer and Fourier-label analysis

For a block, apply the caller's original source transform to each
processed register. The transform is the unit permutation Mult_alpha
of virtual.md Section 11 in the odd stages, the controlled arithmetic
Shift_c of Section 12 in the dyadic stages, and the identity in the
finite branch. Their effective secrets are respectively $\alpha s$,
$s-c$, and $s$. Denote the effective secret by $s'$.

Always process the first register. Run LE from virtual.md Section 5
with its confidence calculation using $Q$ as the raw-copy cap. Release
the position register by partial-trace discard after LE, without a
final measurement of that position. Keep the first row as the
accumulator and its label report as the current report. For each
other register, draw a fresh fair bit. If it is zero, discard the
register. If it is one, process the register by the same transform
and LE. Then perform a CNOT from the accumulator row to the new row,
measure the new row in Z and release it. Outcome zero adds the new
report to the current report modulo $N$, and outcome one subtracts
it. The accumulator row and its report are the outputs of the mixer.
The caller performs the original X gate if specified; the mixer
retains the negative phase convention.

This process has an exact latent-label interpretation even in the
correlated source model. On the label basis, the register shuffle is
a permutation of whole factors. The logical Shift_c only changes
the phase row, with unchanged Fourier index, and Mult_alpha permutes
the Fourier index by $k\mapsto \alpha^{-1}k\bmod N$. The input support
remains the span of product phase-and-position vectors of the
specified effective secrets. Each controlled translation for LE
acts diagonally on the Fourier position basis. Its measurement
Kraus operators, including when chosen from earlier classical
outcomes, are diagonal. Other logical processing acts on the rows
and classical reports. For a pair of distinct complete latent label
vectors, pick a coordinate on which they differ. Along any fixed
classical branch, follow its permuted position register. Local
translations preserve its two distinct Fourier basis vectors and a
unit transform preserves their orthogonality. The position register
is eventually discarded, and the off-diagonal term has zero trace
over that register. This includes skipped registers and all unused
blocks. No measurement result from such a discarded position enters
any transcript. Therefore starting with exact dephasing of the
whole source in its product label basis produces the same observable
algorithm law. This argument includes coherent label correlations
with an external system, since the external system is inaccessible
and all its cross terms are multiplied by the same zero inner
products. In the dephased analysis, conditioned on the complete
latent vector, each row is the appropriate fixed pure qubit, with no
further correlation in the row state.

For each reached LE on a transformed label, the error bound in
virtual.md Section 5 is uniform in that label and the past. At
most $Q$ calls are made, so changing to correct reports in the analysis
costs at most $2^{-10}$. This comparison can keep every genuine
ancillary outcome up to the first wrong report. In the correct-report
process, combining two phase rows with labels $a,b$ has a uniform
target measurement outcome. On bit zero it keeps the 00 and 11
terms and hence produces $\phi_{a+b}(s')$. On bit one it keeps the
01 and 10 terms and produces $\phi_{a-b}(s')$ up to a global phase.
The sign bits are therefore independent fair signs conditional on
all labels and inclusion decisions. For a fixed block with transformed
labels $k'_1,\ldots,k'_w$, the returned row conditional on the new
label $K$ is precisely $\phi_K(s')$, and the label has the law
$$
 K=k'_1+\sum_{i=2}^w E_i k'_i\pmod N,\qquad
 \Pr[E_i=0]=1/2,\quad \Pr[E_i=1]=\Pr[E_i=-1]=1/4
$$
with independent $E_i$. The random inclusion is essential at even
order: the sign alone would leave the parity contribution unchanged.

## 4. Bounded shuffle

Run an in-place Fisher–Yates shuffle. For each step of range $b$
descending from $Q$ to 2, use $d=2\lceil\log_2Q\rceil+40$ fresh fair
bits interpreted as an integer, reduce it modulo $b$, and swap the
corresponding full raw register with the current last position.
The index is always an ordinary classical word. For each $b$ the
law differs from exact uniform on $[0,b)$ by at most $b/2^d$ in
total variation, by counting the preimage sizes. A first-mismatch
coupling over $Q-1$ draws changes the permutation law by at most
$Q^2/2^d\le2^{-40}$. Use the conceptual exact uniform shuffle in the
analysis below. All real loop lengths, random bits and swaps are
bounded. Each full-register swap uses at most $3(n+1)$ CNOT gates;
compute range and addresses with counted ordinary arithmetic.

## 5. Diversity and mixing under an arbitrary fixed latent vector

For a fixed nonzero character $j$, put
$D_j(k)=(1-\Re(\omega^{jk}))/2\in[0,1]$. Call a whole vector good
if its empirical mean of $D_j$ is at least $\delta/4$ for every
nonzero $j$. We first state the bounded-variable multiplicative
lower-tail inequality used here. For independent $X_i\in[0,1]$ with
$\mu=\sum_i\mathbb E X_i$, convexity gives
$$
\mathbb E \exp(-tX_i)\le 1-(1-e^{-t})\mathbb E X_i
     \le \exp(-(1-e^{-t})\mathbb E X_i).
$$
Multiply and apply the exponential Markov inequality with $t=\ln2$.
It gives
$\Pr[\sum_i X_i<\mu/2]\le
\exp[-(1-\ln2)\mu/2]\le\exp(-\mu/8)$.

In product mode each summand's expectation is at least $\delta/2$,
including clean positions. Apply the inequality at
$\mu\ge Q\delta/2$, and take a union over characters, to get
probability at most $(N-1)\exp(-Q\delta/16)$ for a nongood whole
vector. In the correlated mode with $m\ge Q/2$ the promise implies
goodness deterministically: the malformed average of $D_j$ is at
least $\delta/2$. For $m<Q/2$, the $g=Q-m>Q/2$ clean labels have
independent $D_j$ values with mean $1/2$. Their empirical mean is
at least $1/4$ simultaneously except on a set of probability at
most $(N-1)\exp(-g/16)$. Since $\delta\le1/2$, the average over
the entire batch on that event is at least $\delta/4$. With
$Q\ge w=64\delta^{-1}(n+L+32)$ and $N\le 2^n$, both failure
bounds are below $2^{-32}$. This calculation is valid conditional
on each allowed source specification and hence unconditionally.

Fix a good whole vector. For a block after an exact shuffle and for
fixed untransformed labels $k_1,\ldots,k_w$ in it, put
$$
f_j(k)=\frac{1+\Re(\omega^{jk})}{2}\in[0,1].
$$
By the independent inclusion and sign law, the magnitude of character
$j$ of $K$ is $\prod_{i=2}^w f_j(k_i)$ for the identity and shifts.
For a unit transform it is the same expression at the permuted
character $\alpha^{-1}j$. In particular the sum of the magnitudes
over all nonzero characters is invariant under the choice of caller
transform, including an adaptive unit choice. By Fourier inversion,
the block's returned label has total variation distance from uniform
at most
$$
 \delta_b=\frac12\sum_{j=1}^{N-1}\prod_{i=2}^w f_j(k_i).
$$
The returned row conditional on the label is exact, so this also
bounds distance for the joint label and row.

The $w-1$ nonaccumulator positions in any preassigned block are a
uniform ordered sample without replacement from the acquired vector
under an exact shuffle. For nonnegative numbers $a_1,\ldots,a_Q$, the
average product of a uniform $r$-element subset is at most
$(\sum_i a_i/Q)^r$. Here is a proof: the relevant elementary symmetric
sum cannot decrease when replacing two entries by their average.
Terms containing exactly one depend on their sum, and terms
containing both are a nonnegative coefficient times their product.
Iteratively average the current minimum and maximum. The mean stays
fixed, and the sum of squared deviations decreases by half the squared
range at each step. The range tends to zero, so by continuity the
symmetric sum is at most its value on the constant vector. The
inequality also covers $r=1$ directly.

Apply this inequality to $a_i=f_j(k_i)$ for the entire good vector.
Their mean is at most $1-\delta/4$. Thus, at fixed good vector, for each block
$$
 \mathbb E_{\mathrm{shuffle}}\delta_b
 \le \frac{N-1}{2}(1-\delta/4)^{w-1}.
$$
A joint comparison to independent uniform logical labels is obtained
as follows. Condition first on the whole vector and shuffle for the
two processes. At each reached block, if all earlier labels have
matched, the current call is the same and the current transform has
the same effect on the label law in both processes. Couple the real
block's label to a freshly uniform label with discrepancy at most
$\delta_b$. On equality the returned pure rows agree, and the inherited
logical algorithm can proceed by the same operations and measurement
outcomes until the next call. The real process can carry its hidden
mixer transcript, while the inherited program reads only the logical
label and row. The uniform comparison marginal is clean conditional
on the histories, fixed vector and shuffle. At each call the actual
input rows are the conditioned fixed pure states on that block and
future inclusion and measurement signs in that block are independent
of the prior calls. Therefore the first-mismatch bound is at most
$\sum_{b=1}^C\delta_b$, also for branches stopping earlier. No
independence between shuffled blocks is needed. Average this bound
over the exact shuffle and the good latent vector:
$$
 \frac{C(N-1)}{2}(1-\delta/4)^{w-1}<2^{-32}.
$$
Indeed $(1-\delta/4)^{w-1}\le\exp(-(w-1)\delta/4)$ and
$(w-1)\delta/4\ge 15(n+L+32)$, with $C\le 2^L$.
The mixer never checks the latent vector's good event. This estimate
also does not condition on inclusion signs or report histories from
the current block, which could disclose the label.

## 6. Main branch bounds

Under the uniform logical comparison, the unchanged collating and
decoding algorithm receives its exact ideal logical inputs, including
the correct secret transform at each actual call. The ideal supplier
truncation, pool yield and cutoff, identity cutoff, tree and full
decoder errors in virtual.md Sections 7–13 together total less
than $2^{-8}-2^{-10}$ after excluding its original LE term. Add the
new LE error $2^{-10}$, shuffle error $2^{-40}$, bad-diversity
probability less than $2^{-32}$, and mixing error less than
$2^{-32}$. The unconditional sum is below $2^{-7}$.

All new physical storage is charged. Reserve $Q(n+1)$ raw wires,
with a contiguous wire range per copy, and a constant number of
regenerated $O(n)$ arithmetic and readout fields. During a mixer call,
operate on one register at a time, with one accumulator and a single
reported label word. Keep at most $n+5$ six-bit direction values
and one $O(n)$-bit current value for LE unwrapping. The trigonometric
table is of absolute constant size. The raw buffer and processing
scratch are separate from the inherited bank. The output row is
moved into the bank's assigned row slot by a swap and its report
stored through the existing classical transfer. Counts include a
full buffer and cleanup even on a branch using very few logical
requests. The shuffle needs no stored permutation, just a constant
number of ordinary counters and addresses. All such fields and
the pre-bank parameter pass fit $O(n)$ ordinary bits.

For the base's allocation exponent $u$, the logical cap
$C=O(n^3 2^u)$ and $\log C=O(\sqrt n)$. Hence $w=O(n\,2^d)$ with
$d=O(\sqrt n/\log_2 n)$ eventually. Raw quantum
storage $Q(n+1)$, all mixer and shuffle steps, acquisitions,
transfers, per-access fees and cleanup therefore add at most a fixed
polynomial times $2^{u+d}$ to the corresponding exponential resources.
In particular the enlarged memory still has $O(\sqrt n)$-bit
addresses. Because the inherited bank uses controlled wire and data
addresses already charged at that order, its asymptotic work is
preserved. The logical caps remain in force independently of the
reports produced on any branch. The inherited charged compiler and
interpreter costs are also bounded by a fixed polynomial times $2^u$.
Equation (8.8) in virtual.md gives
$$
 u\le(2/\sqrt3)\sqrt n+64n^{1/3}.
$$
Thus all three exponential resources are
$O(2^{(2/\sqrt3)\sqrt n+C_1 n^{1/3}+d})$ for an absolute $C_1$.
The added $d$ is $o(\sqrt n)$.
Since $3(288675134594813)^2>4(250000000000000)^2$, the declared $c$
strictly exceeds $2/\sqrt3$, so the root-exponential representative
absorbs the subleading term eventually. All operations are specified
by the bounded integer schedule, independently of that asymptotic
comparison. The resource growth indices are $1/2$ for the three
exponential representatives and zero for linear classical space.

## 7. Finite branch

For $1\le n<2^{512}$ let $H=256(n+16)$ and $C=NH$. Use the same raw
acquisition, shuffle and mixer. For each candidate $t=0,\ldots,N-1$
make $H$ calls with identity transform. Apply X to the returned row,
then choose a fresh uniform basis bit $\beta$. Measure the row in X
for $\beta=0$ or Y for $\beta=1$, with signed outcome $Z$. Score the
sample by $Z\,\mathrm{tab}_\beta((kt\bmod N)/N)$, where the table is the
rational one in virtual.md Section 4, clamped to $[-1,1]$ before
multiplying by $Z$. Keep the first candidate with mean score above
$1/4$. Run the entire public schedule and output that candidate, or
zero if none was recorded.

Under the ideal logical interface, averaging the exact score over
the independent basis bit and the row measurement yields
$(1/2)\cos(2\pi k(s-t)/N)$. Uniform $k$ gives average $1/2$ for $s=t$
and zero otherwise. The clamped table has error less than $1/625$.
For each candidate the observations are independent under the
comparison. Hoeffding at deviation $1/5$ gives total wrong
classification probability at most $N\exp(-H/50)<2^{-12}$.
Add the four source, readout and shuffle error terms of Section 6.
The result is below $2^{-7}$ here too. All finite-branch sizes and
steps are explicitly bounded. This fixed finite prefix of $n$
only enlarges outside absolute constants of the asymptotic resource
guarantees.

## 8. Material sources

PCROOT-1 supplies the complete collimation algorithm, label readout,
physical basis bank and odd-cell compiler in the accompanying
reproduced files. OTP-LIMIT-BANK supplies the label-first block
interface, bounded raw-register shuffle, and signed CNOT phase
combiner. The spectral product construction supplied the bounded
character attenuation viewpoint and the finite X/Y decoder. The
present algorithm uses random erasure together with the sign,
and treats an entire correlated label vector with a private shuffle
and a sampling-without-replacement bound. The full latent projection,
empirical promise, Fourier coefficient estimate and branchwise counts
are derived above.
