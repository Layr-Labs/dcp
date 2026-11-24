# Paired phase drift with a shrinking conditional label gap

## 1. Exact algorithm and simultaneous bounds

For all $N\ge2$ and $s$ modulo $N$, put $n=\lceil\log_2 N\rceil$.
The following PCROOT-1-based algorithm recovers the entire secret
with probability at least $1-2^{-7}$ under the paired phase-drift
channel promise reproduced in pair-mixer.md Section 2. Its fraction
of allowed malformed copies is 1 under that promise. It allows
unknown phase drift shared by each consecutive pair, quantum memory,
and adaptive decisions; clean ideal copies are also covered. On
every branch its simultaneous work, ordinary classical, allocated
quantum, and acquired-copy envelopes are
$$
 T=O(2^{(5/4)\sqrt n}),\qquad S_C=O(n),\qquad
 S_Q=O(2^{(5/4)\sqrt n}),\qquad Q=O(2^{(9/8)\sqrt n}).
$$
The exact indices are $1/2,0,1/2,1/2$.

Use the complete PCROOT-1 tree, logical decoder, counted bank
and polynomial odd-cell compiler in virtual.md, base-bank.md and
odd_partition.md. For $n\ge2^{512}$ use the asymmetric exact schedule in schedule.md, which replaces
virtual.md Section 8 and the schedule in base-bank.md Section 2.
Its beginning parameter-only pass obtains the logical
acquisition cap $C=4nC_0+K$. Write $r=\lceil\sqrt n\rceil$ in both branches. For $n<2^{512}$ use Section 4
here with $H=256(n+16)$ and $C=NH$. In both cases set
$$
 \delta=2^{-10-\lfloor r/256\rfloor},\quad L=\lceil\log_2 C\rceil,\quad
 w=64\delta^{-1}(n+L+32),\quad A=8wC.
$$
Each reached logical acquisition debits the old cap up front.
Replace the acquisition, the immediately subsequent source transform,
and LE by the complete bounded pair phase-drift mixer in
pair-mixer.md Sections 3–4 with these parameters. It performs
$4w$ physical pairs and hands back one reported label and one
negative-phase row or aborts. The caller's subsequent X, label
check or rejection, table operations and feedback are preserved.
The raw acquisition count satisfies $Q\le A$ in every branch,
including all rejected, erased and unused copies in reached calls.
The raw fixed input transform inside each pair is Mult_alpha from
virtual.md Section 11, Shift_c from its Section 12, or the
identity in Section 4 here.

A logical call begins with no prior raw pair partly consumed.
The raw labels are extracted individually by readout.md with
accuracy cap $A$. The mixer stores at most $w$ corrected rows whose
shared phases have canceled. It uses one ordinary label and scratch
staging area at a time. Completed measured label words are stored
in a separate counted basis-registered array of $O(wn)$ bits
realized as allocated qubit wires. Z reads and X updates are
classically indexed and paid. Neither the raw mixer nor its memory
is an extra oracle. At its output, move the returned row into
the logical current row slot by swap, and transfer the now
classical report using the physical bank's original measured transfer.
Clear and release the rest of the current raw scratch and basis
slots. An abort releases all and outputs zero.

## 2. Source and ideal logical interface

The supported raw channels have the two coset position-row factors
of the same unknown extra phase within each scheduled pair. In the
conditional latent-label calculation, tracing Fourier positions
turns the emitted row into a pure phase state at its label and
fixed phase. This holds with the full joint memory and observed
probe history. On odd CNOT parity the identical phase factors in
the two surviving row terms cancel, giving the exact ideal
difference-phase row. The parity bit is fair for any fixed label
pair and phase and the second channel obeys its spectral gap under
every history, hence retained odd labels have that conditional
gap in the uncapped comparison. The paired module details the
stopped comparison and the bounded-execution failure estimate.
Delayed private inclusion bits and the independent merge signs
then give a Fourier contraction and a coupling to a fresh
uniform label with the exact corresponding pure row. The proof
carries the supplier history and memory without conditioning
the clean comparison on favorable raw outcomes.

The new interface's total raw LE failure is at most $2^{-10}$,
its pair-count cap error less than $2^{-32}$, and its logical
mixing discrepancy less than $2^{-32}$. In the comparison the
complete inherited PCROOT feeder and decoder therefore obtain
their required uniform-input law at every logical request and
original source transformation. From virtual.md Sections 7–13 the
reproduced old ideal correctness terms besides physical LE are
smaller than $2^{-8}-2^{-10}$. This includes the original
identity and tree cutoffs, caps, truncation and complete decoding.
The only physical source extraction error in the new program is
the one just accounted. The sum is below $2^{-7}$.

## 3. Fully charged branchwise bounds

With the public allocation exponent $u$ of the base algorithm,
$C=O(n2^Y+K)$, $\log C=O(\sqrt n)$, and all base work and
allocated quantum space are at most fixed polynomials times $2^u$.
The added $8w$ raw sources per logical call have
$w=O(n2^{r/256})$.
Their processing, basis reads and writes, arithmetic, real
controller, label-estimation probes, counted transfers and cleanup
take fixed polynomial work per raw input. The wrapper needs
$O(n)$ ordinary bits for a constant number of public and current
raw words, the $O(n)$ small LE directions, and the block and loop counters. It never keeps an ordinary $w$ by $n$
label list. The complete $O(wn)$ basis label reservation, retained
rows, source scratch, extra physical addresses and preparation
are included in the allocated qubits. This contributes at most
$O(wn)$ qubits and has smaller leading exponent than the existing bank. Its address-width effect is at
most a constant factor, since the ordinary bank addressing is
bounded at $O(\sqrt n)$ and the new addresses are also $O(\sqrt n)$ bits. All
are counted in the fixed-polynomial factor in the actual work.
The original bank algorithms, including its distinct setup, live
unknown rows and typed allocation, keep their own actual paid
bounds while the interface is active.

The asymmetric parameter proof in schedule.md gives
$$
 Y\le (143/128)\sqrt n+O(n^{1/3}),\qquad
 u\le (159/128)\sqrt n+O(n^{1/3}).
$$
The raw source cap is polynomial times $2^{Y+r/256}$.
The physical work is the sum of the unchanged logical operations,
which are polynomial times $2^u$, and preparation and operation of
the extra basis bank and mixer, which are polynomial times
$2^{Y+r/256}$. This uses the original bank whose individual addresses
are only $O(n)$ bits, with no full-bank scan on each source call.
The physical quantum allocation is the original polynomial times
$2^u$ plus $O(wn)$ simultaneous source scratch and retained slots.
The work and quantum leading coefficient is at most $159/128$
and the raw source coefficient is at most $143/128+1/256=287/256$.
The positive gaps to $5/4$ and $9/8$ absorb the respective subleading
terms and polynomial factors. Ordinary
classical space remains linear for the original and source
controller combined, on every branch. All explicit finite lengths
remain covered.

## 4. Finite branch

For $1\le n<2^{512}$, set $H=256(n+16)$ and $C=NH$. Call the
same bounded mixer with identity transform exactly $H$ times
per candidate $t$ unless it aborts, in which case output zero.
For each report $k$, flip the row by X, and use a genuinely
fair X/Y basis bit. With signed measurement $Z$ and basis
$\beta_0$, use the rational score
$Z\,\mathrm{tab}_{\beta_0}((kt\bmod N)/N)$ from readout.md,
clamping the table to $[-1,1]$. Return the first candidate
above mean $1/4$, or zero if none exists, after running all
scheduled observations on a nonabort branch.

With exact uniform logical labels the ideal score mean is one
half for $s=t$ and zero otherwise. The table perturbs the
score by less than $1/625$. Thus an erroneous threshold
decision needs an ideal mean deviation at least $1/5$ and the
union error is at most $N\exp(-H/50)<2^{-12}$. Add the raw
readout, mixer and pair-cap errors. The finite-case failure
is below $2^{-7}$. Everything uses literal bounded operations
with the same current staging and measured-basis list. Its
fixed finite range can enlarge only absolute constants in the
joint asymptotic estimates.

## 5. Indices and material sources

For each fixed positive $c$, the envelope $2^{c\sqrt n}$ has double logarithm
$(1/2)\log_2 n+\log_2 c$ eventually, giving index $1/2$.
Linear ordinary classical memory gives index zero. The
fraction declaration refers to all actual raw acquisitions,
including every paired rejection and aborted logical call.

The complete PCROOT-1 algorithm, bank and polynomial odd-cell
compiler are reproduced from its published archive, including
the carried credit. The paired phase-drift correction and
bounded odd-first-success proof come from this session's paired
phase algorithm. The published streaming spectral-channel
work supplies its native readout, adaptive conditional Fourier
mixing, and private quantum-memory conditioning. This candidate
uses the faster PCROOT allocation and stores the phase mixer's
measured label list in an explicitly addressed quantum basis bank
to preserve linear ordinary classical space.

The conditional gap now decreases with the input length, including
when all copies are malformed. The replacement schedule reduces the input pool widths, increases
the final tree depth and uses distinct exponents for the true source
cap and the allocated bank.
