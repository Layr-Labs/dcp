# Linear-qubit private source mixing with shrinking phase-and-amplitude promises

For every $N\ge2$, $s$ modulo $N$, and $n=\lceil\log_2N\rceil$,
the same uniform program recovers the entire $s$ with probability
at least $1-2^{-7}$ for the paired phase-and-amplitude channel in
pair-mixer.md Section 2, including independent clean copies.
It can tolerate every actual copy being malformed under that
precise promise. Its branchwise resource bounds are
$$
 T,Q=O(2^{a\sqrt n}),\qquad
 S_C=O(2^{a\sqrt n-9 n^{1/4}}),\qquad S_Q=O(n).
$$
Here $a=u_{333}/v_{333}$ is the exact rational from
$(u_0,v_0)=(10,7)$ and $(u,v)\mapsto(3u+4v,2u+3v)$,
printed in cs-source.md Section 0 and the claims.
The recurrence preserves $u^2-2v^2=2>0$ with positive
terms. Hence $a>\sqrt2$.

## 1. Configuration and actual caps

For $n\ge64$, run the CS1-LBQ logical tree, classical
tables and complete arbitrary-modulus decoder of cs-source.md
Sections 6–13, keeping its exact logical acquisition cap
$C=Q_{\rm cap}$. For $n<64$ use Section 4 here with
$H=256(n+16)$ and $C=NH$. Compute the least integer
$h$ with $h^3\ge n$ by integer comparisons. Set
$$
 \delta=\eta=2^{-10-h},\quad
 L=\lceil\log_2 C\rceil,\quad w=64\delta^{-1}(n+L+32),
 \quad P=4w/\eta,\quad A=2PC .
$$
Each reached logical acquisition debits C before processing
exactly P physical pairs. Guard all operations by these
integer caps. Replace its acquisition, subsequent immediate
known unit or controlled shift, and source label extraction
by the following. Apply the same fixed unit or controlled
shift to each raw delivery of the call, or the identity for
the finite branch. Use the pointwise source model and the
odd correction of pair-mixer.md Sections 2–3, with this kept
row count and cap. Native label extraction uses raw cap A.
Use private-mixer.md to process the first w odd corrected
rows, releasing each row as the new target is absorbed and
keeping only the current accumulator. Continue through all P
raw pairs, discarding all subsequent rows. On a shortage
abort the solver and output zero; otherwise measure only
the final accumulator label at the end and return that report
and one negative-phase row. The caller's subsequent X,
acceptance, labels and logical feedback are unchanged.
Every acquired raw copy, including all discarded or failing
ones, is counted, and $Q\le A$ on every actual branch.

The source promise permits a shared unknown classical phase
and a shared unknown amplitude weight in $[\eta,1-\eta]$ per
pair, with the pointwise second-copy Fourier gap $\delta$.
Both lower bounds shrink with length. A clean delivery uses
the independent original coset state and forces ordinary
balanced weight and zero additional phase in its pair.
The first malformed channel has no spectral restriction.
All support, memory and transcript restrictions are those
of the exact error-model field and pair-mixer.md Section 2.

## 2. Source comparison and correctness

Conditional on latent labels after position discard and on the
phase and weight chosen for the whole pair, each raw row is
pure at its own label. Odd parity cancels the common amplitude
and phase factors exactly, yielding a balanced negative-phase
row at the difference label. At fixed shared weight p, the
odd event has probability $2p(1-p)\ge\eta$ independent of
labels and preceding probes. The second-label character gap
therefore survives subtraction and conditioning on odd given
the weight. Averaging over weights with success weights
preserves the gap. A stopped comparison with a conceptual
extension beyond the physical pair cap proves the same gap
for the first w odds without favorable-cap conditioning.
The pointwise promise covers the conditional state of the
provider's memory even when it is entangled and adaptive.
The conditional exponential moment for pair indicators gives
a shortage bound $e^{-w}$ per logical call. Source report
errors add at most $2^{-10}$ across A raw probes.

Private-mixer.md implements the signed-erasure accumulation
via local channels that produce no new measurement transcript
during raw delivery. Its inclusion via a fresh |+> qubit,
controlled parity update, controlled modular accumulator
update and the private trace-out of the two temporary wires
give exactly the same keep/add/subtract probabilities as the
deferred classical mixer. The new operations commute, on
each fixed observable history, past later supplier
operations and raw measurement instruments on other systems.
Thus the law used by the Fourier proof of pair-mixer.md
Section 4 is the actual law of the private implementation.
No probability argument assumes the provider cannot observe
the real label-probe or pair-parity outcomes.

With $\delta w=64(n+L+32)$, the union of shortage events
is below $2^{-32}$, and the signed-erasure Fourier comparison
over C logical calls contributes below $2^{-32}$. It preserves
the real provider's side transcript up to the first mismatch
and supplies a uniform logical label with its exact negative-phase
row at each requested effective secret. From cs-source.md
Sections 8–12 the reproduced CS1-LBQ ideal source-cap and
full-secret decoding errors together are at most
$2^{-10}+2^{-20}$ under these logical uniform inputs.
The summed unconditional failure is below $2^{-7}$.
The proof handles all source copies allowed by the exact
promise, including the clean independent source.

## 3. Fully charged resource bounds

The original logical cap is
$C=O(n^{3/2}2^{\sqrt{2n}})$ by cs-source.md Section 13,
and original retained charged work is a polynomial times
$2^{\sqrt{2n}}$. In particular $L=O(\sqrt n)$.
Here $w=O(n2^h)$ and $P=O(n2^{2h})$, with all cap
and address bit lengths $O(n)$. Every raw pair, each
native LE probe, the ordinary reported difference
and the private controlled modular accumulation cost
a fixed polynomial in n and address length. Preparing
and releasing all temporary wires counts, including
failed and extra pairs. The logical solver and wrapper
jointly take work and samples bounded by a polynomial
times $2^{\sqrt{2n}+2h}$. The fixed positive gap
$a-\sqrt2$ absorbs the subleading $2h=O(n^{1/3})$ plus
all polynomial factors. No algorithm operation needs the
real constant in the asserted growth envelope.

The suspended CS1-LBQ tree has $O(n)$ allocated qubits
by its original proof. One active raw logical call
uses an $O(n)$-qubit accumulator, native working registers,
one current pair and streamed Clifford+T control scratch.
No array of w live rows is needed. Work addresses are
classically indexed, and the registers released by partial
trace do not accumulate. Allocated qubits remain linear,
even though the number of raw pairs per logical call rises
with input length. The additional ordinary staging is $O(n)$
bits and never stores w reports. The original ordinary
space $O(n^2 2^{\sqrt{2n}-8(2n)^{1/4}})$ from cs-source.md
Section 13 fits $O(2^{a\sqrt n-9n^{1/4}})$ by its Section 14.
The $O(n)$ extra ordinary bits absorbed there do not alter
the stated bound. The finite branch can affect only
absolute constants. These counts include every branch,
such as native misreports, pair shortage, decoder
cutoffs and terminal cleanup.

## 4. Fixed finite branch and indices

For $n<64$, use the same wrapper with H and C above. For
each candidate t perform the H observations with identity
transform. Flip X on each returned row, choose fair X/Y
basis $\beta_0$, and score its sign $Z$ by
$Z\,\mathrm{tab}_{\beta_0}((kt\bmod N)/N)$, clamping the
fixed rational table to $[-1,1]$. The ideal uniform-label
comparison gives a mean of one half for t=s and zero for
every other t. Approximation costs less than 1/625, so a
wrong decision at threshold one quarter requires deviation
at least one fifth. The ideal error union is at most
$N\exp(-H/50)<2^{-12}$. Include raw and mixing differences.
Run all prescribed observations on a nonabort branch and
return the first candidate above threshold, or zero.
The overall failure stays under $2^{-7}$.

The time, ordinary memory and sample envelopes all have
double logarithm $(1/2)\log_2 n+O(1)$ eventually and hence
exact growth index 1/2. Linear allocated qubits give index
zero. The declared malformed fraction one concerns actual
raw acquisitions under the exact paired support, weight,
phase and conditional gap promise.

CS1-LBQ supplies the root-exponential logic and full
modulus decoder. Prior phase-drift mixing supplies the
bounded source-coupling architecture and native readout.
Prior amplitude correction supplies the shared ratio
cancellation and variable parity cap. The private
streamed accumulation here preserves these guarantees
without a retained-row bank. This permits the input
promises to decay while keeping the joint original
root-exponential resource envelopes.
