# Computational-basis backing for the variable-depth solver

Use the exact algorithm, product source premise and all public schedules
in variable-profile.md. Replace its main-branch storage and circuit
organization by the one below, keeping every score and acquisition
decision. The finite prefix n<1024 uses its original circuit and costs;
on the fixed finite width range its classical allocation is bounded by
an absolute constant times n.

The main branch keeps the current stage's score records and suspended
combiner child labels in computational-basis registers. They are known
classical information that the algorithm obtained by measurement or
exact deterministic processing. Charge all these bits as physical
qubits. They are never an uncharged classical table. The registers have
fixed addresses determined by the public dimensions and current frame,
with no quantum-address coherent lookup operation. On the classical
controller use only a constant number of ordinary O(n)-bit temporary
values for any one local arithmetic step or record read.

## Source readout without a classical counter array

Use the same controlled translations and binary unwrapping as BASE13
Section 3, but collect exactly F probes per axis one level at a time,
as specified by its individual test description. For level j build
shift 2^j mod N by ordinary modular doubling. Apply the controlled
translation to the position register using one freshly reset probe
and measure in its specified X or Y axis. In the ideal hidden-label
experiment the position eigenstate and spectator row are unchanged
and the probe means and independence are the same as in the collective
round arrangement. Record just the two empirical counters for the
current level, compute its rounded direction as in BASE13, and discard
those two counters before going to the next level. Store the n+5
six-bit directions and perform the descending lifts with one running
dyadic value. The phase-label guarantee and per-slot union bound are
unchanged. Work is polynomial in n for each processed input. This
uses O(n) classical bits including the shift, the rounding calculation,
the counters, directions, the running dyadic word and the output
label. Exact modular translation takes O(n) reusable qubit scratch.
The known CRT multiplier, if used, is computed by Euclidean arithmetic
holding a constant number of O(n)-bit integer words and implemented
as the reversible modular permutation in BASE13. Whenever memory for
a schoolbook product is needed, keep just the operands, the product
and a constant number of scratch words of O(n) bits.

## Combiner and suspended frames

When a leaf or intermediate root is known, write its full signed label
columns into fresh zero basis registers, using addressed X gates on
the one current O(n)-bit classical value. Store no parallel list of
labels classically. A combiner receives at most b_i+1 child rows and
their fixed length label columns for its public actual width b_i.
Its low-residue membership operations use the bits of the logical
label column in the positions for c_j as the controls of a generic
reversible arithmetic circuit. For each y_j conditionally add c_j
to the b_i-bit accumulator by an ordinary ripple adder controlled
on y_j, with the c_j bits read as ordinary input wires. A control
can be introduced through a reusable Toffoli and uncomputed. No
modification to the stored label is needed, and there is no data-dependent choice of which circuits to execute coherently. The
same circuit applies when measuring the residue on the original
index register and when implementing Grover membership on the
separate scratch query register. Extracting the fixed bit slice is
merely wiring those positions, including two's-complement low bits.

The bounded discovery keeps at most 64 measured candidate strings
of b_i+1 bits, their small flags and the residue, in a single reusable
classical work area. The combiner never recurses while this list
is live. Its postmeasurement verification may read one child label
at a time by measuring the appropriate stored basis register. Such
reads leave that basis register in its original basis state. The
verified pair projection, pivot CNOT cleanup, and choice to retry
are those of BASE13. After identifying a successful pair, sum each
label column for the selected basis-string difference by once
scanning the children. Keep one O(n)-bit accumulated signed value
per column and one current label at a time. Overwrite the output
basis register for the new root and discard the old children,
including every consumed or failed label register. Measured basis
registers can be reset to zero by addressed X gates from their
known bits. The scratch is reused between calls. Every operation
on row phases and labels therefore matches the original distribution,
with only physical location of classical information changed.

The number of pending frames is at most R. Each frame saves a
constant number of O(log(n+2))-bit indices and counters, such as
its level, child interval starts, number of live rows and the next
child position. Keep global work and source guards once in O(n)
bits, rather than in each frame. Profile widths and fixed stack
layout can be recomputed from these same public small fields or
kept in O(R log(n+2)) bits. Since R=O(sqrt(n log n)), the stack,
these descriptors and all outstanding counts use O(n) classical
bits. Full signed values are not stored in these fields. Across
frames, the number of saved label records is O(sum_i v_i)=O(n).
With O(n)-bit label columns the physical backing allocation is
O(n^2) qubits. Child rows and the one active combiner's quantum
work fit within that total. Uniform gate emission for modular
ripple operations holds fixed widths, loop counters and wire
indices rather than entire circuits. All indices and gates pay
the logarithmic address debit for the O(n^2) total allocation.

## Score records and final recovery

Gather one stage's K records in predetermined basis registers
whose width is O(n) bits per record and whose count is O(n).
The global controller retains the current prefix, stage number
and a constant number of O(n)-bit bounds. Its phase predicate
scans the records in public order. Use generic reversible
multiplication of two quantum word registers into a fresh product
register, or compute the modular remainder directly by repeated
conditional additions. Adding a word controlled by an operand
bit preserves both operands. Evaluate the fixed rational score
table using the resulting residue and condition on the stored
axis and measured sign via counted gates. Add the term into the
score register and reverse the entire record scratch evaluation
before moving to the next record. The score records are unchanged,
including when the candidate is in superposition. Padding and
the zero-term abort record have their original behavior. Use
a basis read of one record at a time for each classical verified
mark check, and reset these backing registers before the next
stage. The fixed-address scan costs polynomial work per predicate
and O(n) reusable quantum scratch. It never performs a query
that takes a superposition of record addresses.

All active classical arithmetic uses O(n) bits of temporary
integer storage. For multiplication and division outside a
coherent predicate, use schoolbook shifted addition and ordinary
long division on fixed polynomial-width values. Dynamic counters
for decoder scales and trials use O(n) bits and are not kept on
the combiner stack. Signed weight products and score angles have
O(n) bit lengths by the original profile proof. The fixed gates
for small rational tables and readout directions can be generated
uniformly as in BASE13, and carry work on variable-width words
is counted. No full score table over candidates is generated.

The classical bit upper bound is O(n) and the quantum upper bound
is O(n^2). Each slot, including failed attempts, still uses at
most poly(n) 2^R total work and the same source copy cap. This
remains true if classical indexed control and readback cost an
additional polynomial factor. Each bounded terminal search pays
polynomial work per oracle and has the same count of trials and
iterations, hence the same exponential work envelope. The pure
branchwise time and sample powers and both storage bounds hold
jointly. Source state chronology, label approximation and all
score-distribution arguments from variable-profile.md are
unchanged by the basis representation, so its success guarantee
applies without a new error term.
