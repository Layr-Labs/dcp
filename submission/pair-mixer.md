## 2. Paired amplitude and phase-drift channel model

Write $\omega=e^{2\pi i/N}$,
$\chi_k=N^{-1/2}\sum_y\omega^{ky}|y\rangle$, and
$$
 \phi_{k,\beta,p}(s)=
 \sqrt{1-p}|0\rangle+\sqrt p\,e^{i\beta}\omega^{-ks}|1\rangle,\qquad
 v_{k,\beta,p}(s)=\phi_{k,\beta,p}(s)\otimes\chi_k.
$$
Let $V_{s,\beta,p}$ be the span of these $N$ orthonormal
vectors. Consecutive raw acquisitions $(1,2),(3,4),\ldots$
are grouped into pairs. Before the first copy of a pair,
the provider chooses a classical common phase $\beta$ and common
weight $p\in[\eta,1-\eta]$ for that pair, unknown to the solver. Set
$\eta=2^{-10-\lfloor\lceil\sqrt n\rceil/512\rfloor}$. They may depend on all
previous observations and private memory records. A clean
delivery is an independent ideal $\rho_s$, and in a pair
with any clean delivery the phase is zero modulo $2\pi$ and
the weight is $1/2$. The decision and any flags are withheld.

For each malformed delivery the provider selects a
trace-preserving quantum channel on its private input
memory, producing the raw register and updated memory.
For every possible input density operator on the memory,
the copy marginal must be supported on the chosen
$V_{s,\beta,p}$. The output may be coherent or entangled
with the rest through that memory. The first delivery
has no further spectral restriction. For the second
delivery, if malformed, the marginal diagonal law
$\pi(k)$ in the displayed basis for every input memory
state must obey
$$
 \left|\sum_k \pi(k)\omega^{jk}\right|\le1-\delta
 \quad\text{for all }j=1,\ldots,N-1 .
$$
Here $\delta=2^{-10-\lfloor\lceil\sqrt n\rceil/256\rfloor}$, with $n=\lceil\log_2 N\rceil$.
A clean second copy also satisfies this bound, because
its label is uniform. Before each delivery the provider
may process or measure its private memory and choose
the channel using $N,s$, the algorithm and every earlier
measurement outcome, including the first copy's probes
in the current pair. The pair's earlier chosen $\beta$ and $p$
remain fixed. The private memory starts independent of
the solver. The provider cannot access already delivered
registers, the solver's private state, or future random
bits. This pointwise channel constraint is tested only as
a mathematical premise. The physical solver obtains only
the ordinary raw copy registers.

In particular, all copied raw states may have a nonzero
common phase in every pair, with the phase varying between
pairs. This is a phase error outside the exact clean
subspace when $\beta\ne0$. For instance, for each pair a
provider may make the first copy in an arbitrary
$v_{k,\beta,p}(s)$ and the second in a biased mixture of
those same-phase vectors meeting the stated Fourier gap.
It need not behave stochastically independently between
pairs. The number of malformed deliveries is constrained
only by the fraction of actual acquisitions and the
stated pair and channel promises.

## 3. Corrected phase rows by odd parity

For each raw delivery of a pair apply the logical
caller's unit or shift transform on its position,
then native LE from readout.md with raw cap $A$.
Use the identity transform in the finite branch.
Discard the position without an extra measurement,
and keep the row and report. The unit $\alpha$ maps
the Fourier label to $\alpha^{-1}k$ and effective secret
to $\alpha s$, while a known shift maps the effective
secret to $s-c$ without changing the label. Neither
transform changes the common phase or weight. A unit
permutes nonzero Fourier characters so the second-copy
gap is preserved. The label-extraction error bound
applies uniformly in $k$ even to the twisted rows,
since all probes operate only on position.

We use the equivalent latent-label representation.
For any density operator on the copy and other systems,
within its fixed phase and weight choices the copy can be expanded
as $\sum_{k,l}|v_{k,\beta,p}\rangle\langle
v_{l,\beta,p}|\otimes X_{kl}$. On each probe transcript
the position operators are diagonal in the Fourier basis.
The unit permutes that basis, and the controlled shift
preserves each basis line. Position discard removes the
off-diagonal terms. Provider memory operations chosen
after measurement outcomes act on the other factor and
leave this conclusion intact. Conditioning on the new
latent label therefore leaves its row in the specified
pure phase state. By induction on deliveries, conditional
on the complete latent and measured history, the solver's
live rows and state factor from the provider memory on
each such branch. The spectral premise is valid on
the memory state of every branch because each selected
channel satisfies it for every input. The comparison
with all reports equal to their latent labels costs
at most $2^{-10}$ over $A$ calls, by the uniform estimate
in readout.md. Keep the real probe outcomes through a
first-mismatch comparison so adaptive provider choices
have their correct observed history until the mismatch.

For a complete pair apply CNOT from its first row to
its second, measure the target in Z, and keep the
control only on outcome one. Conditional on the labels
$a_1,a_2$, phase $\beta$, weight $p$ and earlier transcript, the
odd probability is $h(p)=2p(1-p)\ge\eta$. For outcome one
the 01 and 10 terms survive with coefficients
$\sqrt{p(1-p)}e^{i\beta}\omega^{-a_2s'}$ and
$\sqrt{p(1-p)}e^{i\beta}\omega^{-a_1s'}$, respectively.
Their ratio gives the usual balanced pure negative-phase row
with label $a_1-a_2$ and secret $s'$, up to a global phase.
Thus the common amplitude bias and common phase cancel exactly.
Compute its report by subtracting the two reports
modulo $N$. The matched-report analysis uses the
true label $a_1-a_2$.

For a nonzero character index $j$, condition on the state
before the pair and on its selected $\beta,p$, which are fixed
before either label is delivered. Then condition on the history
up to the second delivery, including $a_1$ in the analysis.
The conditional absolute mean of $\omega^{-ja_2}$ is at most
$1-\delta$. The factor $\omega^{ja_1}$ has unit magnitude.
Taking conditional expectation over that history gives the same
characteristic bound for the difference. With $p$ fixed the
odd probability is independent of the labels and intermediate
history. So conditional on success the same bound holds.
Averaging over the selected phase and weight with their
success-weighted probabilities preserves the bound.

Acquire and test exactly $P=4w/\eta$ pairs in a logical call.
Retain the first $w$ odd rows and discard later ones. Store
their reported labels in a counted measured-basis register.
If fewer than $w$ rows are obtained, abort after the call.
Given any past at a pair boundary its odd indicator $I$ has
conditional mean at least $\eta$. Consequently
$\mathbb E[e^{-I}\mid\mathrm{past}]\le
\exp[-(1-e^{-1})\eta]$.
Iterating this conditional inequality over all $P$ pairs
and applying Markov gives
$\Pr[\sum I<w]\le
\exp[w-(1-e^{-1})\eta P]\le e^{-w}$,
using $1-e^{-1}>1/2$. The argument allows arbitrary
adaptation and correlations between pairs.
For an uncapped analytical comparison, extend each
call beyond the $P$ pairs until it obtains $w$ odds
if necessary, using any allowed clean source after
the cap. The real and comparison calls can agree
up to the cap event. If the needed $w$ rows occur
before the cap, the comparison includes the additional
pairs up to $P$ to preserve all observable supplier
history. This is a comparison only, with unconditional
error summed across at most $C$ calls less
than $2^{-32}$. It does not condition the retained
label law on successful completion before the cap.
In the uncapped analysis the next retained corrected
label satisfies the gap conditional on the history
before searching for that next odd row. To see this,
condition on any number of failed parities and their
intermediate history up to the last pair: the
conditional expectation for the eventual success in
that pair is bounded by the same gap, and the
probability weights sum to one. Its corrected row
is pure and separated from provider memory at its
latent label.

## 4. Streaming spectral mixing of corrected rows

In a block's uncapped comparison take the $w$ retained
corrected rows. The executable program chooses all
inclusion bits only after its entire bounded block
of raw pairs has been processed. Keep the first
corrected row as accumulator. For every later one
independently include it with probability one half.
If included, CNOT accumulator to that row and measure
its target in Z, keeping the signed sum or difference.
Omitted rows are released. The output is one pure
logical row conditional on the new sum label in the
latent analysis, and the actual report is the same
signed sum on the reported values.

Let $b_i$ be the latent corrected labels of a block.
For each nonzero $j$, $D_i=(1-\Re\omega^{j b_i})/2$
has conditional mean at least $\delta/2$. Conditional
on history before the block, the chord bound
$\mathbb E[e^{-tD_i}\mid\mathrm{past}]
\le\exp[-(1-e^{-t})\delta/2]$ and iteration at
$t=\ln2$ give
$\Pr[\sum_iD_i<w\delta/4]\le\exp(-w\delta/16)$.
Use the filtration through the next retained
pair's search as in Section 3. Union over $N-1$
characters. When conditioning on the final
native transcript before inclusion, the $w$
corrected rows are a product at their retained
latent labels, with side memory an independent
factor on that branch. Conditional on them, each
later label receives coefficient $0,+1,-1$ with
probabilities $1/2,1/4,1/4$, independently. The
conditional magnitude of character $j$ of the
signed sum is $\prod_{i=2}^w(1-D_i)$, at most
$\exp(1-w\delta/4)$ on the simultaneous good
event. The Fourier inversion bound conditional
on the prior history, after averaging current
native transcripts, is
$$
 (N-1)\left(\exp(-w\delta/16)+\exp(1-w\delta/4)/2\right)
$$
in total variation from uniform. The row is
fixed and pure conditional on the returned
label. Multiplying by $C$ gives total
comparison error less than $2^{-32}$.

For this adaptive comparison, take each current
logical label coupled to a fresh uniform one
conditional on the entire preceding history. Carry
the actual block's side transcript and its conditional
provider memory state as auxiliary data. One can sample
that record conditional on the original block output
in the coupling. The ideal logical output is still
uniform conditional on the history before the block.
On agreement, both solver rows agree and factor from
the conditional auxiliary memory. Their subsequent
operations can use the same outcomes through the next
call. This makes a first-mismatch bound valid even
when later phase choices and channels use all earlier
measurement outcomes. The contributions of exceeding
a pair cap, erroneous native reports, and imperfect
mixing are added without assuming independence
between these events.

