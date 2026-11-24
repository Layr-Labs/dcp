# Private signed-erasure accumulation during paired acquisition

Use the paired source and odd correction of pair-mixer.md Sections
2–3, with the current public bounds on delta and eta. This file
replaces all storage and processing of the retained-row list. Its
probability argument gives exactly the same output law as the
deferred procedure in pair-mixer.md Section 4. The computational
basis reconstruction of the public final label is the only new
observable measurement inside the source wrapper. It happens after
every raw delivery of the current logical block.

## Actual circuit for one retained odd row

Keep an n-wire accumulator label Z holding the reported residue in
the computational basis or a classical mixture thereof, and one
accumulator phase qubit. On the first odd, prepare Z from the
measured reported difference and move its row into the accumulator.
For each subsequent retained odd, write a for its ordinary reported
difference and A for its corrected phase row. Independently prepare
a private inclusion qubit B in |+>. Controlled by B, apply CNOT
from the accumulator row to A (a Toffoli). Then apply the reversible
permutation on Z controlled by B and the basis value of A:
if B=0 leave Z unchanged; if B=1 and A=0 add a modulo N;
if B=1 and A=1 subtract a modulo N. Outside [0,N) use identity.
This permutation preserves both controls, is an exact controlled
known-constant arithmetic circuit over Clifford+T, and uncomputes
its current ripple scratch. It has O(n) temporary wires using the
standard reversible add/subtract and comparisons of the readout.
Release B and A by partial trace, without a computational-basis
measurement or a record accessible to the supplier. Only the
quantum label and row of the accumulator remain.

A wire release is the same physical trace-out operation used for
the raw Fourier position in the native label module. Use fresh
zero wires for the next temporary slot. Taking the partial trace
and issuing fresh |0> has charged preparation and release of the
old allocated wire; neither operation produces a classical
measurement transcript. The private supplier cannot access any
of these wires. At most one inclusion and one new target wire
are live for this step. Qubit allocation here means peak allocated
wires, so released wires and their replacements never cause an
accumulating allocation. All releases and preparations are charged.

In the analysis, conditional on an accumulator label z and the
new corrected label a, their phase rows are pure and have the
same effective secret. The B=0 branch leaves the accumulator
unchanged when its new discarded row is traced out. The B=1
branch has equal probabilities for A=0,1 by direct CNOT parity.
After tracing A, these alternatives are exactly the pure
negative-phase rows at z+a and z-a, with their corresponding
basis accumulator labels. The coin trace yields the mixture
with weights 1/2,1/4,1/4. It is precisely the signed-erasure
instrument, including its independence of the old z and a.
The statement holds also when different hidden paths reach the
same accumulator label, since each path there has the same row.

## Observable history and delayed comparison

The implementation retains the first w odds and still executes
every raw pair out to the block's actual cap. Whether a retained
row is absorbed is determined solely by its observable odd flag
and the counter w. Nothing is revealed about an inclusion or
its sign before the last raw pair. There are no new observable
readouts of Z, B, or A during this private processing. Source
delivery, position probes, raw pair parity and counts remain
exactly as in the original correction. All other outcomes are
kept and used by the provider as before. The private operations
do not act on provider memory; they do not act on any future
delivered register, and they do not affect subsequent raw
measurements, raw scheduling or abort checks.

To formalize deferral, enlarge the probability analysis to keep
the latent label at each fixed raw probe transcript. A corrected
row, once created, is pure at its latent label and factored
from the rest, by pair-mixer.md Section 3. Conditional queries
to the provider and conditional instruments on later raw
registers act only on other systems. The private processing map
is controlled by already observed classical values only. Its
unitaries and partial traces commute with those later raw and
provider operations, for each fixed observed history. Moving it
past them gives the same subnormalized output with the same
observable history. In that mathematical comparison all relevant
corrected rows can first be gathered and only then processed
by the exact same private channels. This is a proof equivalence,
with no deferred-list allocation in the executable algorithm.
It justifies the independence of the auxiliary signed-erasure
coins from the entire current raw history in the Fourier analysis.
One can also obtain the equivalence by conditioning on all raw
latent labels and delaying the independent branch values of the
private maps.

On shortage abort the solver and release the accumulator.
Otherwise, after processing all raw pairs, measure Z in the
computational basis and hand the reported residue and one
row to the caller. In the ideal reported-label comparison
this is exactly the signed sum and pure row analyzed in
pair-mixer.md Section 4. Its conditional Fourier contraction
therefore applies unchanged. The randomized physical steps
do not rely on favorable native reports. For wrong reported
labels, all gates remain defined and the actual caps stay
valid; the result is handled by the existing first-mismatch
coupling. At main or finite branches the same bounded
adapter is used, and no source copy is acquired by the
private accumulation itself.

## Resources

The accumulator, one current pair and raw readout's live
scratch require O(n) allocated qubits. Addresses and arithmetic
registers have O(n) bits. The ordinary controller holds only a
fixed number of current operands and counters, plus the O(n)
native extraction directions. There is no w-row buffer or
w-label array. Per pair and per retained row, the extra work
is polynomial in n and all address lengths, charging every
gate, qubit preparation, discard, indexed call, and the single
final reported-label readout. The pair cap itself still counts
even if too few odds are produced. This analysis applies even
when w grows exponentially in a subleading function of n.
