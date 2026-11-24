# Root-exponential streaming spectral channels with linear quantum storage

## 1. Single program and joint estimates

For all $N\ge2$ and $s\in\mathbb Z/N\mathbb Z$, let $n=\lceil\log_2N\rceil$.
The algorithm below recovers the entire secret with probability at
least $1-2^{-7}$ under the adaptive spectral channel model in
channel-mixer.md, including the independent ideal case. It tolerates
malformed fraction one under that model. In particular a supplier
can keep quantum memory, correlate its copy preparations through
that memory, and use the earlier observed label-probe outcomes as
feedback, subject to each chosen channel satisfying the uniform
spectral gap on every input memory state.

Use the CS1-LBQ virtual tree, phase decoder and storage policy in
cs-source.md with the source-interface changes below. Its use of
classical collimation tables allows root-exponential work with
linear quantum storage. The resource envelopes for our complete
configuration on every execution branch are
$$
 T,Q=O(2^{a\sqrt n}),\quad
 S_C=O(2^{a\sqrt n-9 n^{1/4}}),\quad S_Q=O(n).
$$
Here $a=u_{333}/v_{333}$, with $(u_0,v_0)=(10,7)$ and recurrence
$(u,v)\mapsto (3u+4v,2u+3v)$. The exact rational value appears in
cs-source.md Section 0 and in the structured declarations. It
satisfies $a>\sqrt2$ by the positive Pell norm. These are
work, ordinary classical bits, entire allocated qubits and
acquired-copy bounds for the same program.

## 2. Source substitutions and guards

For $n\ge64$ take the CS1-LBQ setup, tree, phase-vector merges,
branching over odd and dyadic parts, and full decoder exactly as
in cs-source.md Sections 6–13. Determine $C=Q_{\rm cap}$ by
its Section 11; this is the cap on logical source requests.
For $n<64$ set $C=N\cdot256(n+16)$ and use Section 4 below.
In either branch define
$$
 \delta=2^{-10},\quad L=\lceil\log_2 C\rceil,\quad
 w=64\delta^{-1}(n+L+32),\quad A=wC.
$$
The current logical acquisition count never exceeds $C$.
Replace each original raw acquisition, its immediate public
unit or known controlled shift, and its LE operation by
one call to the complete streaming mixer of channel-mixer.md
Sections 2–4, with these values of $\delta,L,w,A$. The
original unit or shift is applied separately to each
raw input of the new mixer. It returns one reported label
and a negative-phase row. The original caller's X gates,
label checks, table creation, rejection and reuse run as before.
The original high-confidence LE, its fallback counter, and
any algorithmic actions internal to that estimator are
replaced entirely by this definite raw interface. No extra
raw acquisition follows a failed logical request guard.
Exactly $w$ raw copies are acquired in each reached call,
including its internally erased rows. Thus $Q\le A$ on
every branch.

The physical mixer uses the fixed-width native readout
in readout.md, with its accuracy cap set to $A$. It starts
one position register at a time, applies the public
known transform, probes it, and traces it out. Stores of
probe directions and labels are part of ordinary memory.
The first retained phase row is the accumulator. After
finishing all raw arrivals for the current block, independently
erase or include each later row with probability $1/2$.
For each included row, use CNOT and measured parity to
combine it with a fair sign, updating the report accordingly.
The retained support relation and uniform-in-memory
channel spectral gap are precisely the premise of the
carried mixer proof. It accounts for adaptive probes,
hidden latent labels, conditional private quantum memory,
signed-erasure characters, and the block-by-block joint
coupling to fresh uniform labels. It includes errors of
at most $2^{-10}$ for all raw readouts and $2^{-32}$ for
all imperfectly mixed labels across the actual program.

## 3. Success and main-branch cost

With the comparison interface, each logical request yields
a uniform latent label with its correct ideal row, already
in the effective secret coordinates of the original
transform. It is conditionally independent of the preceding
logical history. The original CS1-LBQ logical algorithm's
ideal source-cap event is bounded by $2^{-10}$ and its
odd decoder error by $2^{-20}$, with exact remaining
dyadic recovery conditional on success, by cs-source.md
Sections 8–12. The old label-extractor error and
fallback counter are absent in this run. The new coupling
errors add $2^{-10}+2^{-32}$. Thus total failure is below
$2^{-7}$.

Section 13 of cs-source.md proves the capped logical bound
$C=O(n^{3/2}2^{\sqrt{2n}})$ and all remaining logical work
at most a fixed polynomial in $n$ times $2^{\sqrt{2n}}$.
The uniform readout and public transforms
use polynomial work per read copy in our interface.
Since $\log C=O(\sqrt n)$, $w=O(n)$, so raw acquisitions
and charged processing add at most another fixed
polynomial times $2^{\sqrt{2n}}$. The same grade
includes preparation of the parameter cap, gate
generation, basis operations, cleanup, and addressing
at the enlarged actual memory width $O(\sqrt n)$.

A suspended tree call retains the CS1-LBQ stage's original
$O(n)$ quantum workspace. The mixer adds $w=O(n)$ row wires,
one current position register, and a reused $O(n)$
readout/transform workspace. There is never a simultaneous
array of full raw positions. Keep the $w$ measured label
words and current LE unwrapping values in $O(n^2)$ extra
ordinary bits. All arithmetic uses fixed-width guarded
loops even after any wrong report. The CS1-LBQ virtual
stack and its tables need
$O(n^2 2^{\sqrt{2n}-8(2n)^{1/4}})$ ordinary bits by its
Section 13. Adding the polynomial mixer space keeps
this bound, since the exponential factor grows without
bound. The same source proves its inclusion in
$O(2^{a\sqrt n-9n^{1/4}})$, using
$8\cdot2^{1/4}>9$. For work and samples, the fixed gap
$a-\sqrt2>0$ multiplied by $\sqrt n$ absorbs every
fixed logarithmic polynomial exponent. In particular
for any fixed $r$ we have
$n^r2^{\sqrt{2n}}=O(2^{a\sqrt n})$.
The algorithm uses exact integers, independent of the
asymptotic threshold at which this comparison holds.
The capped physical ledgers hold on every outcome,
and finitely many smaller $n$ change only absolute
outside constants.

## 4. Finite branch

For $1\le n<64$, use $H=256(n+16)$ logical calls per
candidate, with identity public transform and streaming
mixer exactly as above. Each returned phase row is
flipped by X. Choose a fair basis bit $\beta$, measure
in X for $\beta=0$ or Y for $\beta=1$, and let $Z$
be its signed result. Use the rational table of readout.md
with score $Z\,\mathrm{tab}_\beta((kt\bmod N)/N)$ for
trial candidate $t$. Clamp the table to $[-1,1]$ before
multiplying. Choose the first candidate whose mean
exceeds $1/4$ or zero if none. Execute the full $NH$
schedule. The ideal exact expectation is one half
at the true candidate and zero elsewhere by averaging
$\frac12\cos(2\pi k(s-t)/N)$ over uniform labels.
The table error is smaller than $1/625$, and threshold
failure requires an ideal deviation at least $1/5$.
One Hoeffding bound per candidate gives union failure
$N\exp(-H/50)<2^{-12}$. The raw extraction and mixer
coupling terms keep failure below $2^{-7}$. Every
resource use is finite and bounded explicitly on
this fixed finite branch, loading only one label array
at a time.

## 5. Indices and provenance

Both $2^{a\sqrt n}$ and $2^{a\sqrt n-9n^{1/4}}$ have
double logarithm $(1/2)\log_2n+O(1)$ as $n$ grows.
Their growth indices are $1/2$, while the linear
qubit bound has index zero. All acquisitions count
toward the proved fraction in exactly the channel model
of the fifth claim.

CS1-LBQ supplies the exact root schedule, phase merges
and decoder, classical table storage, branchwise bounds and
the fixed rational exponent. Its proof is reproduced
unchanged as cs-source.md. The published streaming
spectral channel result from this session supplies the
complete source model, mixer and raw readout, with the
declared coefficients and quantum conditioning proof.
Its relevant source sections are reproduced as
channel-mixer.md and readout.md. The new integration
changes the operating root regime and classical-table
resource bounds and retains linear quantum storage
under the same adaptive quantum-memory source promise.
