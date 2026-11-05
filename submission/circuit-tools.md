# Explicit streaming predicate generation for QSR11

These bounds specialize to the SAME shifted-width near-quadratic program:
x=log2n>=32, H=sqrt(nx), R<=3sqrt(x), m<=sqrt(n), t<=9H/8,
K=2^40nL and L=2^R. They count every generated address and gate.
They are not an oracle-cost assumption.

## Addresses and a concrete bit-serial generator

The listed live allocations admit the loose explicit upper bound
2^10000 n^3 L bits/qubits: the table stack, at most one K-row dictionary,
2048n+1 private classical outcomes, Kstat<=2^33n statistical records,
matrices of at most2n^2 bits, O(n^2) arithmetic buffers, O(n) quantum
registers, constant direction tables and a constant number of counters
are all included. No emitted gate history is stored.
Consequently the full allocated-memory address width obeys
 a<=10001+3x+R<=2^10 x.
The source/work/reservation clocks and all private repetition counters
have O(H) bits, including their fixed10000-bit padding constants.
For example log2B<=10100+105x+(3/2)H; private phase counters have at most2t
bits. Since H>=128x and n>=2^32, one may bound their maximum b by16H.

Use a fixed bit-serial compiler with constant-many a-bit workwords.
For each fixed-arity logical gate, operands are constant-many row/field
offset products and sums of a-bit nonnegative integers. Schoolbook
multiplication/addition uses O(a^2) bit operations. Generating each such
operation's own operand indices by schoolbook offset arithmetic and
stored bit-serial loop indices costs at most O(a^3) raw bit/head steps,
as in the supplied fully addressed controller construction. Outputting its
constant-many a-bit operand fields and maintaining its own loop counters
is no larger. A deliberately loose2^20 a^6 raw CORE steps per generated
logical gate therefore covers this entire process, including readout of
classical constants and the gate itself. Reuse those workwords and one
gate buffer; do not compile a retained circuit list. Fixed Toffoli gates
are expanded into their exact constant Clifford+T decompositions.

A raw bit/head step is still charged its FULL indexed-memory price by
the external clock argument. There is no free head access, machine word,
operand index, uncounted scratch address or recursively monitored monitor.
The polynomial count here describes a concrete schoolbook generator;
it does not replace its own work by a unit-cost logical instruction.

## Base low-key/hash predicate

For each of m children, scan its L classical rows. For one row compute
equality of the R-bit child index with its literal row number, XOR its
n-bit constant into ONE reused word conditioned on that flag, and erase
the flag. Add the extracted word into a reused accumulator and reverse
the lookup before proceeding to the next child. Thus no m-by-n quantum
word array is allocated. Cost is O(mL(n+R)+mn) fixed-arity gates.
Raw/phase label and root-key words have only a fixed constant times n bits,
which changes only absolute factors. The binary hash costs O(t^2) CNOTs
and comparisons add O(n+t) gates; reverse their scratch after marking.
Hence the base predicate has O(n^(3/2)L+nx) logical gates.

A Grover diffusion has O(t) clean Toffoli/CNOT gates. Its explicit controlled
form includes the leading Z on the phase-control bit; that sign is not
discarded. Private Grover/QPE repetition indices can have O(H) bits:
their check/increment and emitted control indices cost at most O(H a^6)
raw steps per iteration and are included below.

## Complete-dictionary exclusion and exact rank lookups

At most K=2^40nL found masks are scanned. An equality of t-bit z with
one mask, an increment of a O(log K)-bit match counter, and reversal
use O(t+log K) gates. Only one equality flag and the match counter are
live. Thus exclusions, including their reversal, need at most
O(n L H)=O(n^(3/2)sqrt(x)L) gates. The same bound covers a literal exact
rank/g dictionary scan, with the known masks and rank numbers.
There is no coherent K-row table, coherent list of flags or QRAM.

## Convert the polylog generator factors to a uniform core bound

For x>=32 the ratio x^13/2^x decreases, because13/x<ln2. At32 its value
is2^33. Therefore x^(13/2)<=2^(33/2)sqrt(n).
Multiplying the above logical gate bounds by a^6=O(x^6) yields
 base gates: O(n^(3/2)x^6 L+nx^7)=O(n^2L),
 exclusion/lookup: O(n^(3/2)x^(13/2)L)=O(n^2L).
The private repetition-controller term H x^6 is O(n) by the same inequality.
All inverse and fixed-control factors fit, with generous explicit slack,
 base query <=2^1000 n^2L CORE steps,
 exclusion/diffusion query <=2^1500 n^2L CORE steps.
These are counted generated circuits. Every raw step still receives the
full global indexed-access and clock charge in monitor-tools.md.

The private-count query count in dictionary-tools.md is at most
2^56 n^(3/2) 2^(ceil((t+R)/2)). Thus its expanded work is at most
2^2000 n^(7/2) 2^E, E=ceil((t+3R)/2).
The bounded complete enumeration has at most2^36 n^(3/2) 2^(ceil((t+R)/2))
iterations, and all initialization/verification fits the same query price;
its work is at most2^2500 n^(7/2) 2^E.
The remaining2^900n^25L^2 work from exact scalar arithmetic, Fourier gates,
medians, sorting, initialization, records and generated loops is below
2^900 n^4 2^E, since E-2R>=63x. Expected leaf work and bounded gradient
preparation fit by the same exponential margin.
Their sum is less than the ACTUAL whole-node allowance
 G=2^10000 n^4 2^E.
Every reservation, padded runtime and expectation recurrence uses THIS G.
No larger previous padding or uncontrolled query is hidden in the bound.
