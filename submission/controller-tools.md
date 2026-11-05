# Explicit bit-serial control for QSR15

This helper supplies the counted implementation used in the main proof.
It gives no oracle and assumes no previous verdict. All gate fields, loop
positions, addresses, scratch initialization and inverses are charged.

## Complete raw core accounting

circuit-tools.md supplies the fully expanded streaming per-mask compiler,
fixed coherent-row scans, all inverse/output passes and helper absorption.
Its ACTUAL whole-node allowance is G=2^1000n^3*2^t. No generated instruction,
operand field or controller operation is free. The remainder of this helper
adds the cost of the external clock and EVERY allocated-memory access.

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

For QSR15, C=O(n sqrt(n log2n)) and q<=2^(Hscale/4+2J) with J/Hscale<=1/8. The new root/cap expressions give b=Theta(Hscale) exactly as required here. The complete finite-grid estimator is separately included in E_D by the main proof; it is not asserted to fit the basic n^8 helper count. Source/work caps, p and clocks are recomputed for the known-frequency root.
