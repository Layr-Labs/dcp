## 2. Adaptive spectral channel model

Write $\omega=e^{2\pi i/N}$,
$\chi_k=N^{-1/2}\sum_y\omega^{ky}|y\rangle$, and
$\phi_k(s)=(|0\rangle+\omega^{-ks}|1\rangle)/\sqrt2$.
Let $V_s$ be the span of the orthonormal
$v_k(s)=\phi_k(s)\otimes\chi_k$ for $0\le k<N$.
A clean delivery is the independent ideal state $\rho_s$, in product
with everything else. On a malformed delivery the provider applies
a quantum channel to its private memory. The channel emits an
$(n+1)$-qubit copy register $A$ and an updated private memory $E'$.
For every density operator $\tau$ on the channel's input memory,
the copy marginal is supported on $V_s$. Its diagonal law
$p_\tau(k)=\langle v_k(s)|\operatorname{Tr}_{E'}(\Lambda(\tau))|v_k(s)\rangle$
must satisfy
$$
  \left|\sum_k p_\tau(k)\omega^{jk}\right|\le1-\delta
  \quad\text{for every }j=1,\ldots,N-1.
$$
The bound is uniform over the memory input of each chosen channel.
It therefore holds for the marginal of a memory entangled with
other systems. The channel may entangle its output with the
new memory and, through that memory, other delivered copies.

Before each delivery, the provider may process and measure
its private memory and choose a channel or a clean delivery using
$N,s$, the algorithm, all previous measurement outcomes and its
private records. The chosen malformed channel obeys the bound
for every possible input memory state, including one conditioned on
unseen latent labels. This includes adaptation to raw label
extraction inside each block. The private memory starts independent
of the solver. The provider has no access to delivered registers,
future randomness or any private solver workspace. Only the
copy register enters the solver. No spectral weights, measurement
of the provider memory or corruption indication are supplied.

Fixed or adaptive product spectral preparations are special cases,
by using a channel that prepares the selected state independently of
its memory. For an example with genuine inter-copy entanglement,
the first channel can emit one half of a maximally entangled state
in the $v_k(s)$ basis, holding its other half in its memory. Its
emitted marginal is uniform. The second channel can, with weight
$1-\delta$, transfer the retained memory to a copy in the same basis,
and with weight $\delta$, emit an independent ideal copy. The second
channel's spectrum meets the gap for every possible memory input
because all its nonconstant coefficients are multiplied by
$1-\delta$. For $N=2$, the two output copies have a Bell-state
component of weight $1-\delta$ and a completely mixed component of
weight $\delta$ on $V_s\otimes V_s$. Its partial transpose has a
eigenvalue $-1/2+3\delta/4<0$, so the output copies can be
entangled in this model.

## 3. Physical streaming interface

For a logical call with known transform, acquire one raw copy at a
time. The transform is the unit multiplication or known controlled
shift of cs-source.md Sections 9–10, or identity in the finite branch.
Perform it immediately on the new raw register. Run the fixed length
LE in readout.md with its raw upper bound parameter set to $A$.
Release the position wires by partial trace after these probes, with
no final position measurement. Keep the single row qubit and its
reported label. The label is kept as an $O(n)$-bit ordinary word.
Proceed to the next raw acquisition after completing those steps.
After $w$ acquisitions retain $w$ row qubits and $w$ classical
reports. The labels and all earlier readout outcomes may have been
used by the provider for its later decisions.

Take the first row and its report as the accumulator. For each of
the remaining $w-1$ records draw a fresh fair inclusion bit after
the last delivery. If zero, release the row; if one, apply the CNOT
from accumulator to that row, measure its target in Z, and release
it. On target outcome zero add its report to the accumulator modulo
$N$, and on outcome one subtract it. This leaves the accumulator
in the negative-phase convention. Pass its row and final reported
label to the original caller. The caller's later X, sign and label
operations are preserved. Every one of the $w$ reports and rows is
accounted even when it is later discarded. The $w$ stored rows
are never measured or coupled to one another before the last raw
delivery in their block.

## 4. Adaptive mixing proof

The logical transforms on $V_s$ preserve the one-to-one Fourier
position and row relation. If a supplier requests multiplication
by a unit $\alpha$, the Fourier index maps by multiplication by
$\alpha^{-1}$ and the effective secret is $\alpha s$. A controlled
shift preserves the index and changes the effective secret to
$s-c_0$ for its known offset $c_0$. The spectral promise survives
both maps because unit multiplication permutes nonzero character
indices. The latent-label measurement representation of LE holds jointly
with the provider memory and all retained registers. In fact the new
copy and everything else has a block expansion
$$
 \sum_{k,l}|v_k(s)\rangle\langle v_l(s)|\otimes X_{kl}.
$$
On each fixed LE transcript the Kraus operators on position are
diagonal in the Fourier basis. The unit and shift transforms also
preserve orthogonality of two distinct Fourier position labels.
Private operations conditioned on the probe history act on the other tensor factor and do not affect Fourier-position orthogonality. When that position is discarded, the terms with $k\ne l$ vanish.
Thus one can put a latent measurement of the new copy in its
$v_k(s)$ basis before the physical transform and probes, keeping
the hidden label only in the analysis. This preserves every actual
probe outcome and joint memory state after that position discard.
Given the latent $k$ the emitted row is the fixed pure state
$\phi_k(s')$ and factors from all other systems.

By induction one can condition on the complete latent and public
past while keeping the solver's live quantum state and the provider's
memory in product form on each such history. Initially this is the
source promise. Each conditioned latent measurement leaves the new
row pure and acts only on the provider side of that product apart
from exposing a classical outcome. Supplier memory operations act
on one factor, and the inherited algorithm's operations act on the
other factor; any conditioning on their classical outcomes preserves
the product on a fixed branch. The ordinary schedule performs the
entire current LE and position discard before any next delivery.
Thus the dephased calculation agrees with the adaptive observed
law, even if a different input memory state arises on different
latent branches. For every such branch the uniform channel gap gives
the same bound on the conditional law of the next latent label.
The logical caller and prior solver quantum state need not be
independent of the hidden label distribution unconditionally.
The product statement is only for a fixed classical and latent
history in this analysis.

Replacing the label report by its latent label costs at most $2^{-10}$
over all raw calls, by the uniform-in-label error bound in readout.md
with cap $A$. Keep common probe outcomes and memory operations
until the first wrong report. The physical controller can compute
the report without supplying it as an extra measurement outcome;
given the probe transcript the corresponding classical arithmetic
is fixed. Thus the comparison can carry the same supplier
measurement history up to that mismatch.

Consider one block in this correct-report analysis, and condition
on its complete pre-block history. For a fixed nonzero character
$j$, write $D_i=(1-\Re\omega^{j k_i})/2\in[0,1]$ for the transformed
latent label at delivery $i$. Conditional on every earlier latent
label, probe outcome and provider selection record, and on the
choice of channel before sampling the new latent label, the
conditional expectation of $D_i$ is at least $\delta/2$. The
channel bound applies to the current conditioned memory state. For every $t>0$,
$$
 \mathbb E[e^{-tD_i}\mid{\rm earlier}]\le
 1-(1-e^{-t})\delta/2
 \le\exp(-(1-e^{-t})\delta/2)
$$
by the chord inequality for $e^{-tx}$ on $[0,1]$, then averaging
over the step's choice. Iterating conditional expectations for
the product and using Markov with $t=\ln2$ gives
$$
 \Pr\!\left[\sum_{i=1}^w D_i < w\delta/4 \mid {\rm preblock}\right]
 \le \exp(-(1-\ln2)w\delta/4)
 \le \exp(-w\delta/16).
$$
The proof uses conditional drift and does not require independent
labels across adaptive deliveries. Union over $N-1$ characters.

The timing matters even on two labels. In a toy process where an
adder exposes each previous exact running parity, a provider can
choose the next label equal to that parity with probability
$1-\delta/2$. Each draw meets the same conditional spectral gap
and the next running parity is zero with probability
$1-\delta/2$, however many draws have elapsed. The inclusion bits
here are chosen only after the final delivery, so there is no
known running selected parity during the stream.


Conditional on the full latent vector and the probe history
within the block, the rows are a product of the specified pure
phases. On each inclusion, the target sign is uniform for every
pair of labels, by expanding the four terms of the two-qubit
state. Target outcome zero keeps 00 and 11, giving the label sum,
and one keeps 01 and 10, giving the label difference. Thus
after the last delivery the output label $K$ is distributed as
$k_1+\sum_{i=2}^w E_i k_i \pmod N$, where the independent variables
$E_i$ have probabilities $1/2,1/4,1/4$ at $0,+1,-1$.
The conditional output row is precisely $\phi_K(s')$. The
character magnitude of this signed sum is
$\prod_{i=2}^w (1-D_i)$. On the event that every character has
$\sum_i D_i\ge w\delta/4$, it is at most
$\exp(1-w\delta/4)$ for each character. We removed at most one
unit of deficiency for the accumulator. Random omission makes
this formula valid even for an order-two character.

By finite Fourier inversion, conditional on a good vector the
total variation distance of $K$ to uniform is at most
$(N-1)\exp(1-w\delta/4)/2$. Averaging over the latent vectors and
probe records bounds the block distance conditional on the whole
prior history by the sum of this and $(N-1)\exp(-w\delta/16)$.
The row itself is pure and fixed at each returned label,
so this bounds the full delivered pair. Multiplying by
$C\le2^L$ gives a total error below $2^{-32}$, using $N\le2^n$
and $w\delta=64(n+L+32)$.

One can realize this bound by first-mismatch coupling. At each
reached logical call, condition on the past, couple the real
block output label to a fresh uniform label, and give the
comparison $\phi_K(s')$ for its own uniform label. Carry the
actual block's side transcript and conditional provider memory state
to drive future supplier choices. Sample the record
conditional on the original label in the coupling and carry its
corresponding quantum memory state as an auxiliary system. The
conditional factorization above ensures that the inherited solver's
state on a matching history can be coupled identically. Those choices have no control over the
comparison's next independently uniform label. On each matched
history the new pure rows are identical and the inherited
algorithm can use the same operations and outcome coupling until
the next logical acquisition. This proves equality to the clean
logical process except for the stated total error. In particular
we never assume a block is uniform after conditioning on its
current inclusion bits or reports.

