## 2. Paired phase-drift channel model

Write $\omega=e^{2\pi i/N}$,
$\chi_k=N^{-1/2}\sum_y\omega^{ky}|y\rangle$, and
$$
 \phi_{k,\beta}(s)=
 \bigl(|0\rangle+e^{i\beta}\omega^{-ks}|1\rangle\bigr)/\sqrt2,\qquad
 v_{k,\beta}(s)=\phi_{k,\beta}(s)\otimes\chi_k.
$$
Let $V_{s,\beta}$ be the span of these $N$ orthonormal
vectors. Consecutive raw acquisitions $(1,2),(3,4),\ldots$
are grouped into pairs. Before the first copy of a pair,
the provider chooses a classical common phase $\beta$ for
that pair, unknown to the solver. It may depend on all
previous observations and private memory records. A clean
delivery is an independent ideal $\rho_s$, and in a pair
with any clean delivery this common phase is zero modulo
$2\pi$. The decision and any flags are withheld.

For each malformed delivery the provider selects a
trace-preserving quantum channel on its private input
memory, producing the raw register and updated memory.
For every possible input density operator on the memory,
the copy marginal must be supported on the chosen
$V_{s,\beta}$. The output may be coherent or entangled
with the rest through that memory. The first delivery
has no further spectral restriction. For the second
delivery, if malformed, the marginal diagonal law
$p(k)$ in the displayed basis for every input memory
state must obey
$$
 \left|\sum_k p(k)\omega^{jk}\right|\le1-\delta
 \quad\text{for all }j=1,\ldots,N-1 .
$$
A clean second copy also satisfies this bound, because
its label is uniform. Before each delivery the provider
may process or measure its private memory and choose
the channel using $N,s$, the algorithm and every earlier
measurement outcome, including the first copy's probes
in the current pair. The pair's earlier chosen $\beta$
remains fixed. The private memory starts independent of
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
$v_{k,\beta}(s)$ and the second in a biased mixture of
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
transform changes the extra common phase. A unit
permutes nonzero Fourier characters so the second-copy
gap is preserved. The label-extraction error bound
applies uniformly in $k$ even to the twisted rows,
since all probes operate only on position.

We use the equivalent latent-label representation.
For any density operator on the copy and other systems,
within its fixed phase choice the copy can be expanded
as $\sum_{k,l}|v_{k,\beta}\rangle\langle
v_{l,\beta}|\otimes X_{kl}$. On each probe transcript
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
$a_1,a_2$, phase $\beta$, and earlier transcript, each
parity occurs with probability one half. For outcome one
the 01 and 10 terms survive with coefficients
$e^{i\beta}\omega^{-a_2s'}/2$ and
$e^{i\beta}\omega^{-a_1s'}/2$, respectively.
Their ratio gives the pure negative-phase row
$\phi_{a_1-a_2,0}(s')$ up to a global phase.
Thus the common phase cancels exactly.
Compute its report by subtracting the two reports
modulo $N$. The matched-report analysis uses the
true label $a_1-a_2$.

For a nonzero character index $j$, condition first
on the state before the pair and then on the history
up to the second delivery, including $a_1$ in the
analysis. The conditional absolute mean of
$\omega^{-ja_2}$ is at most $1-\delta$. The
factor $\omega^{ja_1}$ has unit magnitude, so
the full difference law has its $j$th characteristic
magnitude at most $1-\delta$ by conditional
expectation and the triangle inequality. Since
the odd result is fair even given both labels
and the other history, the same bound holds
for the label of a retained odd row conditioned
on its preceding raw-pair history.

Acquire and test exactly $4w$ pairs in a logical call.
Retain the first $w$ odd rows and discard any later ones. Store the reported label of each kept row in a counted measured-basis register, reading one word at a time during the later signed-erasure pass.
If fewer than $w$ are obtained, abort the full solver
after this call. In the latent-report analysis, the
odd results are i.i.d. fair conditional on any
preceding logical history. The probability of fewer
than $w$ is at most $\exp(-w/2)$ by Hoeffding.
For an uncapped analytical comparison, extend each
call beyond the $4w$ pairs until it obtains $w$ odds
if necessary, using any allowed clean source after
the cap. The real and comparison calls can agree
up to the cap event. If the needed $w$ rows occur
before the cap, the comparison includes the additional
pairs up to $4w$ to preserve all observable supplier
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

