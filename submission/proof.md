# Spectral mixing of biased coset preparations before collimation

## 1. Theorem and executable interface

For every integer $N\ge 2$ and $s\in\mathbb Z/N\mathbb Z$, let
$n=\lceil\log_2N\rceil$. This algorithm recovers the entire secret with
unconditional probability at least $1-2^{-7}$. On every execution branch
its joint resource bounds are

- charged total work $O(2^{c\sqrt n})$,
- peak ordinary classical storage $O(n)$ bits,
- peak allocated quantum storage $O(2^{c\sqrt n})$ qubits,
- acquired source copies $O(2^{c\sqrt n})$,

where the exact rational $c=1154700538379252/10^{15}$. The growth indices
are $1/2,0,1/2,1/2$. The theorem includes the clean source and admits a
malformed fraction of 1 in the spectral-gap model of Section 2. There is
no herald for a malformed preparation or its bias.

Use the complete PCROOT-1 physical bank in base-bank.md, logical algorithm
in virtual.md, and compiler in odd_partition.md, with the following
substitutions. Section 6 replaces the whole finite branch. On the main
branch keep all parameters, pool caps, source-request caps, decoder and
bank logic of PCROOT-1. Its source-request cap is denoted by $C=4nC_0+K$.
At each logical request plus its source transform and label extraction,
call the mixer of Sections 3 and 4. It supplies the same type of interface
(a reported label and a row wire) to the same caller as the replaced
sequence. Keep the caller's subsequent X gate, truncation, label
reduction, releases and other operations as before. Define for both
branches
$$
w=n+\lceil\log_2 C\rceil+32,\qquad C_{\rm raw}=w C.
$$
Here $C$ for the finite branch is defined in Section 6. Each mixer call
acquires exactly $w$ raw copies, including the last call of any aborted
branch. All quantities are computed by integer arithmetic.

## 2. Source promise

Write $\omega=e^{2\pi i/N}$. Let
$\chi_k=N^{-1/2}\sum_y\omega^{ky}|y\rangle$,
$\phi_k(s)=(|0\rangle+\omega^{-ks}|1\rangle)/\sqrt2$, and let $V_s$
be the span of $\phi_k(s)\otimes\chi_k$ for $0\le k<N$.
For a single-copy density operator $\sigma$ supported on $V_s$ define
$p_\sigma(k)=\langle\phi_k(s),\chi_k|\sigma|\phi_k(s),\chi_k\rangle$.
Call a preparation admissible if
$$
\left|\sum_{k=0}^{N-1}p_\sigma(k)\omega^{jk}\right|\le\tfrac12
\qquad(1\le j<N).
$$
The ideal state is admissible, with $p(k)=1/N$. A malformed copy may be
any admissible $\sigma$ on the same wires. The density matrix may
contain coherences between coset vectors. As an example for $N\ge3$,
a mixture of the Fourier basis vectors in $V_s$ that is uniform on
all but one label has every nonconstant coefficient of magnitude
$1/(N-1)$. It has a missing label and contains no positive ideal
component in a convex decomposition.

Before each raw delivery, the supplier may choose the kind of copy and
its state using $N,s$, the algorithm, all earlier measurement outcomes,
and private classical randomness and records. Conditional on
its choices and classical record, the new register is prepared in the
chosen density matrix in tensor product with the workspace and other
copies. The supplier's correlation between preparations is classical.
The supplier never accesses delivered systems or future private
algorithm randomness. Ordinary clean deliveries are independent ideal copies at
delivery and have the same expectation guarantee. All parameters of
the promised states may be unknown to the algorithm. For a block of
$w$ deliveries, the solver performs no measurement and exposes no
sample-dependent result while acquiring the block. Conditional on the
pre-block branch and the supplier's selections within the block, its
raw registers are therefore in the product of the selected density
operators and factor from the solver's existing state. The private
classical record can in particular contain a randomly chosen sequence
of different biases. No bound on their number beyond the full
acquisition count is needed.

## 3. The mixer and its correct-label version

For one call, acquire the whole block of $w$ copies in a directly
indexed scratch region. Use the same publicly specified source transform
on every raw copy. The transform is Mult_alpha for the odd supplier
of virtual.md Section 11, Shift_c for the dyadic supplier of
Section 12, and the identity in Section 6 here. Define the effective
secret to be $\alpha s$, $s-c$, or $s$, respectively.

Run LE from virtual.md Section 5 separately on each transformed data
register. Release that data register by the partial-trace discard at
the end of the call. The algorithm does not measure the final position
register or retain a reset outcome. A recycled scratch position is
initialized afresh before reuse. Its public accuracy parameter
uses $C_{\rm raw}$ in place of the old source cap. Keep the first
row as an accumulator with reported label equal to the first report.
For each further row, apply CNOT with accumulator as control and new row
as target, then measure the target in Z and release it. If the outcome
is zero add its report modulo $N$. If the outcome is one subtract its
report modulo $N$. Keep only the accumulator and the updated report.
Return the final row and report. No X is applied by the mixer. In the
correct-label version of the mixer the report at each LE is the
actual latent Fourier label. The circuit itself uses the bounded
estimators and exact CNOT measurements just given.

We verify the latent-label interpretation on all allowed inputs.
The controlled translations used in LE are diagonal in the
$\chi_k$ basis on the valid position span. Its ancillary measurements
therefore have Kraus operators diagonal in that basis. When the data
is traced out, every off-diagonal term in its Fourier basis vanishes.
This applies to the joint row, report, and all internal LE outcomes,
including if an outside observer receives the outcomes. The data
register can thus be regarded as projected in the Fourier basis for
the analysis. The conditional row is exactly $\phi_k(s)$, because
there is just one basis vector in $V_s$ for each $k$.

The transform Shift_c leaves $k$ unchanged and shifts the row phase
to $\phi_k(s-c)$. On a basis state Mult_alpha permutes the Fourier
index by $k\mapsto\alpha^{-1}k\bmod N$, and changes the row to
$\phi_{\alpha^{-1}k}(\alpha s)$. Thus each nontrivial Fourier
coefficient of the new reported-label law in the ideal LE version is
still at most $1/2$ in magnitude. The ideal input also has that property.
These statements follow for the transformed coherent density operator
by the same diagonal measurement argument. Formula (5.1) of virtual.md
bounds the probability of an erroneous report uniformly in latent $k$
at every LE call. With $C_{\rm raw}$ in that formula, the union bound
for all raw calls is at most $2^{-10}$, on either branch of the
algorithm. This compares the actual and latent-report versions with
common readout outcomes until the first wrong report. In particular the
error analysis includes the actual adaptive supplier after earlier calls.

For two negative-phase rows with labels $a,b$ and effective secret
$s'$, the CNOT measurement has fair outcomes, for every label pair.
The surviving row is exactly $\phi_{a+b}(s')$ on outcome zero and
$\phi_{a-b}(s')$ on outcome one, up to a global phase. Expand the
four computational-basis terms to check this: outcome zero keeps the
terms initially indexed 00 and 11, outcome one keeps 01 and 10.
Therefore the final row is $\phi_{K_*}(s')$ where
$K_*=k_1+\sum_{i=2}^w e_i k_i\bmod N$ and $e_i=+1$ or $-1$ is the
corresponding outcome sign. Conditional on every latent index and
LE transcript in a block, the outcomes are independent fair bits.
The block has already been acquired, so these outcomes never control
the choice of a later raw state within the block.

## 4. Spectral contraction and adaptive composition

Condition on a pre-block branch and the supplier's selected states
during block delivery. For the correct-label version, the input labels
are independent, with laws $p_i$ obeying the bound in Section 2 after
the chosen transform. Conditional on a fixed sign vector, their laws
are unchanged, because the signs are independent of the labels. In
particular, for every nonzero character index $j$,
$$
\bigl|\mathbb E[\omega^{jK_*}\mid(e_i)]\bigr|
  = |\widehat p_1(j)|\prod_{i=2}^{w}|\widehat p_i(e_i j)|
  \le 2^{-w}.
$$
Discrete Fourier inversion gives
$|\Pr[K_*=k\mid(e_i)]-1/N|\le (N-1)2^{-w}/N$ for each $k$,
hence total variation at most $(N-1)2^{-w}/2$.
This bound persists when averaging the sign vector, or averaging the
supplier's selections conditional on the pre-block branch. The
auxiliary past can include previous statistical outcomes, estimates and
malformed-position choices. The row conditional on the returned label
is the common fixed pure state $\phi_{K_*}(s')$. Replacing the joint
returned label and row by a uniform label together with its ideal row
therefore costs the same amount in trace distance. Existing live
registers are unchanged by the mixer and may be included in this
comparison. The probability bound does not condition on the block's
complete LE transcript, which can reveal the returned label.

For completeness, the replacement also works when the supplier observes
every block outcome and uses it on later blocks. In the latent-report
analysis, condition on the entire pre-block branch for both processes.
After selecting the raw states, couple their $K_*$ marginal to a fresh
uniform label with agreement probability at least
$1-(N-1)2^{-w}/2$. The original block's ancillary transcript can be
sampled conditionally on the original label in that coupling. Its
distribution in the original process is preserved. In the comparison
process carry that transcript as auxiliary supplier history, whether or
not the coupled returned labels agree. It affects only later supplier
choices. Each later comparison call uses its own fresh uniform label
conditional on all of this history. The ordinary algorithm receives
only the fixed row for the uniform returned label and the label itself.
Hence it has the clean logical law in the comparison process. On
agreements the pair of logical states is identical, so all common
ordinary operations, decisions and outcomes can be coupled up to the
next call by the same quantum instrument. This proves a first-mismatch
bound without treating the complete raw transcript as independent of
the returned label. Equivalently each coupling changes the reduced
label-and-row channel by its total variation distance and uses the
matched histories until a mismatch.

There are at most $C$ mixer calls on every branch. With $N\le2^n$ the
total mismatch budget is at most
$$
 C (N-1)2^{-w}/2 < 2^{-32}.
$$
No mixing check, public uniform-label oracle, or retries are performed
by the algorithm. The uniform draw occurs only in this comparison.

## 5. Main branch correctness and accounting

The uniform interface in Section 4 gives exactly the independent
latent-label and exact row input used by the inherited proof. For
example, the odd supplier applies X and retains reports below the
stated public truncation point, and the dyadic supplier applies X and
reduces reports modulo the relevant power of two. These operations have
their original laws under the comparison. All cutoff and concentration
arguments for the ideal collimation and decoding are in virtual.md
Sections 7–13. Their terms excluding physical LE error sum to less than
$2^{-8}-2^{-10}$. Add the actual LE error $2^{-10}$ and the new mixing
error $2^{-32}$. This gives failure below $2^{-7}$. The retained
physical bank implements the rest of the logical graph on its accessible
wires exactly as in base-bank.md. The source interface wire and reported
label are copied into their existing assigned logical slots. A row is
moved by a swap, and the visible reported label is ordinary classical
data, so this step makes no copy of an unknown qubit. All other scratch
from the block is released or reset before the next call.

Allocate a separate explicit contiguous region of $w(n+1)$ raw wires
outside the inherited counted bank, with reused $O(n)$ arithmetic and
probe workspace. A constant number of ordinary counters, addresses,
row labels, and the public transform parameters fit in $O(n)$ bits.
Run one transform, LE and row combine at a time. The table of
trigonometric constants from virtual.md Section 4 is of absolute
constant size. The backwards unwrapping of LE can store at most $n+5$
six-bit direction values and use one $O(n)$-bit current value. Thus
all LE workspace, including raw-sized confidence counts, is $O(n)$
ordinary bits. Already measured rows and discarded data within the
raw array remain in allocated quantum storage for this accounting.
With $w=O(n)$ the extra quantum reservation is $O(n^2)$. Actual raw
source count is at most $C_{\rm raw}$. Giving the raw region its
indices increases address widths by at most a constant factor, since
the baseline bank width is $O(\sqrt n)$ and $w(n+1)$ is polynomial.
There are polynomially many gates, measurements and generated
operations per raw copy. Controlled transforms, LE, arithmetic,
source moves, scratch allocation and cleanup are included. The
remainder of the work is bounded by the base algorithm's charged
work with that constant-factor address adjustment. The new
polynomial overhead multiplies at most the guarded count $C$.

To use a common asymptotic bound with the inherited analysis, write
$u$ for its allocation exponent. The source cap obeys
$C=O(n^3 2^u)$, the bank is bounded by a polynomial times $2^u$,
and virtual.md Section 8 gives
$$
u\le (2/\sqrt3)\sqrt n+64n^{1/3}.
$$
The upper bounds for all three exponential resources are consequently
$O(2^{(2/\sqrt3)\sqrt n+C_1n^{1/3}})$ for an absolute fixed $C_1$,
because every additional overhead above is polynomial. The exact
integer identity $3(1154700538379252)^2>4(10^{15})^2$ implies that
$c$ is strictly above $2/\sqrt3$. For sufficiently large $n$ that
fixed gap times $\sqrt n$ exceeds $C_1n^{1/3}$. The implementation
uses no asymptotic threshold or irrational constant in an operation.
The coefficient $c$ is solely in the envelope proof. Ordinary
classical storage stays linear in the main branch.

## 6. Finite branch

For $1\le n<2^{512}$, set $H=256(n+16)$ and $C=NH$.
Run the same mixer independently for each of $H$ observations at every
candidate $t=0,\ldots,N-1$, with identity source transform. In each
observation apply X to the returned negative-phase row, sample a fair
bit $\beta$, and measure the resulting row in X when $\beta=0$ or Y
when $\beta=1$. Let the signed result be $Z$. Compute the rational
score $Z\,\mathrm{tab}_\beta((kt\bmod N)/N)$ using the inherited table,
clamped to $[-1,1]$ before multiplying by $Z$. Return the first
candidate whose sample average exceeds $1/4$, or zero if no such
candidate exists. All scheduled observations run on every branch.
Table generation, rounding and determination of score order use
the exact definitions of virtual.md Section 4.

In the uniform ideal interface for each observation, averaging over
the fair basis gives ideal mean $(1/2)\cos(2\pi k(s-t)/N)$. The
uniform average over $k$ is $1/2$ when $s=t$, zero otherwise.
The clamped table perturbs any score by less than $1/625$.
Consequently a wrong-side deviation from the mean of at least $1/5$
is required for either an erroneous discard of the true candidate
or a false acceptance. Within each fixed candidate's ideal trials
the measured scores are independent and in $[-1,1]$, so the union
failure bound is $N\exp(-H/50)<2^{-12}$. Add the common LE
and mixing budgets. It is again less than $2^{-7}$. All branch
costs are explicitly bounded here, with $w=O(n)$ and the number of
trials fixed. The range of $n$ is fixed and finite, so its finite
work, samples and peak storage only affect absolute constants in
the common asymptotic envelopes. Streaming all candidate averages
requires one sum and one saved answer at a time.

## 7. Indices and provenance

The time, qubit and sample representatives have double logarithm
$(1/2)\log_2 n+\log_2 c$ eventually. Their growth index is $1/2$,
and the ordinary classical representative $n$ has index zero.
The fraction expression 1 applies to the same actual acquisition
count, success probability and resource guarantees for every
allowed selection of spectra. It is specific to the support,
spectral and delivery assumptions of Section 2.

PCROOT-1, Yukon submission bcd08da3-dd96-42d6-b542-133b67a48d05,
supplies the complete logic, physical memory implementation, and exact
compiler reproduced here. Its original material credit is included.
OTP-LIMIT-BANK, Yukon submission
63be7cca-89b9-4ec3-a50b-7ca93edcc335,
supplies the label-first interface and the signed-sum purification
pattern used for comparison and adaptation. In that proof a uniform
label contributes a one-time pad to a block. Here the spectral
contraction supplies mixing from biased factors even when none has
a uniform component, and the acquisition timing is local to each
block. Both prior mathematical arguments are explicitly identified in
the dependency declaration. All new correctness steps appear above.
