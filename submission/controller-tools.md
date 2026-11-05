# Explicit bit-serial control for PSR2 and MSRL4

This helper supplies the counted implementation used in the main proof.
It gives no oracle and assumes no previous verdict. N, parameters, observed
labels and tables are ordinary classical data. Quantum arrays are accessed
only through the explicitly emitted equality/XOR row scans in the main proof.

## Per-mask core cost and the smaller allowance

Let s be the enumerated input-index width: m for PSR2 and t=mR for MSRL4.
Both main proofs establish s<=n, all subset-label/aggregate words have O(n)
bits, and at most n operands enter a subset sum. Fix padded widths, rather
than variable-length operations that could hide branch costs. Use a fixed
finite-control bit-serial generator with counted work-tape head moves,
Boolean transitions, explicit mask/loop counters and bit pointers.
There is no indexed instruction oracle, free machine word or stored gate stream.

A classical table base is computed from its known index and stride by
schoolbook arithmetic. Within a word, advance a sequential pointer rather
than recomputing the product at every bit. A pointer update, loop test,
fixed Boolean-gate emission and its own bit-position/control arithmetic on
O(n)-bit registers cost O(n^2) primitive bit/head operations: at most O(n)
positions, with O(n) work even if locating/returning to each position.
Read/write addresses and every bit of a gate's wire description are generated
in these operations. Their actual allocated-memory access charge is added
separately below; this is a CORE count, not an uncharged RAM instruction.

Per enumerated mask, at most O(n^2) logical bit/gate positions suffice for
the at-most-n O(n)-bit subset additions, validity/key comparisons, rank
comparison/increment, output metadata and mask/count progression. Thus a
conservative2^40 n^4 core operations covers a mask, including all controller
generation. The fixed number of forward/reverse/count/inverse/output passes
cost at most2^50 n^4*2^s. In MSRL4, coherent validity uses a fixed number
of m literal L-row queries, computed once and uncomputed after rank; mL<=2^s
for m>=2,L>=2. Their polynomial per-row emission fits the same bound.
No quantum query is inserted inside each classical enumerated mask.
MSRL4 writes all retained output rows in ONE pass.

Quantum equality, ripple addition/comparison and controlled increments have
linear reused scratch in their operand widths. Clean XOR evaluations compute,
copy and reverse; direct inverse enumeration erases equality scratch after
each controlled XOR. No history of2^s gate values is retained. All fixed
Boolean gates use exact constant-size Clifford+T NOT/CNOT/Toffoli networks.

Private gradient/source helpers are unchanged. Their classical, arithmetic,
measurement, reset and generated-gate work is at most2^80 n^8 in the main
proofs' valid width ranges. Fixed rational direction constants are generated
once before the core clock and charged as finite setup, not treated as advice.
Since s>=sqrt(n log2 n)>=16log2 n in these branches,2^s>=n^16. Therefore
 2^80 n^8+2^50 n^4*2^s < (2^100 n^5*2^s)/2.
Use G=2^100 n^5*2^s. This leaves the leaf retry slack (at most16/15 in
MSRL4), covers expected source filters and bounded gradient preparation, and
proves E0=G and the nonrecursive G term used in the exact retry recurrence.
It is a looser safe count, not an optimal compiler assertion.

## Fully charged monitor and allocation addresses

Put Hscale=sqrt(n log2 n) for analysis only. From the literal cap formulas
and the main proof's independent parameter inequalities, clock bit length
b=ceil(log2(B+1)) satisfies Hscale<=b<=C Hscale for an absolute C.
The lower bound follows from B>=G>=2^s; the upper is algebraic and does
not assume this implementation's correctness or runtime bound.
Source counters and enumeration widths are at most O(b).

Let a be an upper bound on a full classical/quantum operand address,
including all allocated control/scratch/constants. In PSR2, S_C=O(n^2),
S_Q=O(n), so a=O(log n). In MSRL4, S_C=O(n^(7/4)2^(n^(1/4))),
S_Q=O(n), so a=O(n^(1/4)+log n)=O(n^(1/4)).
Fixed direction-generation workspace changes only absolute constants.

Before each core step, compare the b-bit counter to the stored constant B;
abort if equal, otherwise increment. Use the same bit-serial pointer scheme.
Each of O(b) counter positions needs O(a^2) bit operations for addresses,
loop position and return, plus ripple work. In both cases a^2=O(b):
for PSR2, (log2 n)^3<=n for n>=4096 (dyadic base ell=13 and the n=4096
case, then induction) implies(log2 n)^2<=Hscale; for MSRL4, a^2=O(sqrt n)
<=O(Hscale). Thus monitor control/compare/increment uses O(b^2)
primitive bit/head operations including its OWN addresses and loop control.

EVERY one of those monitor operations also pays its O(a) allocated-memory
access charge. The monitor is not recursively monitored: its whole work is
explicitly added as O(b^2 a) per core step. Ordinary core bit/gate operands
pay O(a), their address emission already counted as core work, and a source
acquisition additionally pays n+1. This gives O(b^2 a+n) fully charged work.

For PSR2, b^2 a=O(n(log2 n)^2)<=O(n^2), using(log2 n)^2<=n.
For MSRL4 it is O(n^(5/4)log2 n)<=O(n^2); its main inequalities give
log2 n<=n^(1/4), even yielding the stronger n^(3/2) allowance, unused here.
Hence O(n^2) fully charged work per core step safely covers the monitor,
controller's own memory, gate/wire execution and direct source charge.
No word or counter update is free.

Initialization, deterministic parameter generation and abort cleanup receive
these same full addressing/control charges. PSR2's allocation is polynomial.
MSRL4's polynomial times2^(n^(1/4)) table initialization/cleanup is absorbed
by the strict exponent-growth gap to sqrt(n log n). All reserved bits/qubits
are initialized/reset with counted operations, whether allocated lazily per
frame or zeroed initially. No favorable cap branch is postselected.
