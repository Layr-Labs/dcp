# Explicit bit-serial control for QSR14

This helper supplies the counted implementation used in the main proof.
It gives no oracle and assumes no previous verdict. All gate fields, loop
positions, addresses, scratch initialization and inverses are charged.

## Per-mask core cost and the smaller allowance

Let s=t=mR be the enumerated input-index width. The main proof establishes s<=n, all subset-label/aggregate words have O(n)
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
cost at most2^50 n^4*2^s. In QSR14, coherent validity uses a fixed number
of m literal L-row queries, computed once and uncomputed after rank; mL<=2^s
for m>=2,L>=2. Their polynomial per-row emission fits the same bound.
No quantum query is inserted inside each classical enumerated mask.
QSR14 writes all retained output rows in ONE pass.

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
 2^80 n^8+2^50 n^4*2^s < (2^100 n^4*2^s)/2.
Use G=2^100 n^4*2^s. This leaves the leaf retry slack (at most16/15 in
QSR14), covers expected source filters and bounded gradient preparation, and
proves E0=G and the nonrecursive G term used in the exact retry recurrence.
It is a looser safe count, not an optimal compiler assertion.

## Fully charged monitor and allocation addresses

Put Hscale=sqrt(n log2 n) for analysis only. From the explicit cap formulas
and the main proof's independent parameter inequalities, clock bit length
b=ceil(log2(B+1)) satisfies Hscale<=b<=C Hscale for an absolute C.
The lower bound follows from B>=G>=2^s; the upper is algebraic and does
not assume this implementation's correctness or runtime bound.
Source counters and enumeration widths are at most O(b).

Let a be an upper bound on a full classical/quantum operand address,
including all allocated control/scratch/constants. The directly counted
classical stack is O(n^(7/4)2^(n^(1/4))), quantum storage O(n), and
all other buffers fit the same allocation. Thus
 a=O(n^(1/4)+log2n)=O(n^(1/4)).
This memory argument depends on explicit syntactic field widths and the
fixed recursion stack, not on any time claim. The public constants B,
Qcap and q have O(Hscale) bits and fit the already allocated buffers.

Before each core step, compare the b-bit counter to the stored constant B;
abort if equal, otherwise increment. For each of O(b) positions use an
explicit a-bit binary pointer and a fixed ripple Boolean transition.
Generating/advancing its address, loop test and return takes O(a^2) raw
bit/head operations, including generation of the control operations' OWN
addresses. A sequential sweep of the at-most-a-bit pointer uses at most a
positions with at most O(a) moves/operations per position; loop state and
pointer scratch are reused. This implements the same explicit bit-serial
pointer scheme as above, rather than an atomic random-access word update.
The scan and ripple comparison/increment therefore need O(b*a^2) raw
operations. The terminal cleanup clock and source cap use the same scheme;
their widths are O(b). Monitor operations are explicitly added, not recursively
monitored. There is no unit-cost clock or unchecked favorable branch.

EVERY such raw monitor operation pays its full O(a) allocated-memory access
charge. Hence the complete monitor costs O(b*a^3) per core step. Ordinary
core operands cost O(a), with their address generation already counted in
the core ledger; each source acquisition additionally costs n+1. Therefore
fully charged work per core event is O(b*a^3+a+n). Using b=O(Hscale) and
a=O(n^(1/4)), this is O(n^(5/4)*sqrt(log2n)). The source charge n+1 is
included in that expression. In particular we retain O(b*a^2) directly;
loosening a^2 to O(b) would be unnecessary and give a weaker bound.
All loop/operand/gate/control fields remain ordinary initialized bits and
all Boolean circuits have fixed exact Clifford+T decompositions.

Initialization, deterministic parameter generation and abort cleanup receive
these same full addressing/control charges. The polynomial times2^(n^(1/4)) table initialization/cleanup is absorbed
by the strict exponent-growth gap to sqrt(n log n). All reserved bits/qubits
are initialized/reset with counted operations, whether allocated lazily per
frame or zeroed initially. No favorable cap branch is postselected.

For QSR14, C=O(n sqrt(n log2n)) and q<=2^(Hscale/4+2J) with J/Hscale<=1/8. The new root/cap expressions give b=Theta(Hscale) exactly as required here. The complete finite-grid estimator is separately included in E_D by the main proof; it is not asserted to fit the basic n^8 helper count. Source/work caps, p and clocks are recomputed for the known-frequency root.
