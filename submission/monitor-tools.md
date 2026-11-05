# Fully charged clock with source work priced separately for QSR11

Let a be the full allocated-memory address width and b the largest working,
source, reservation or private iteration counter width. circuit-tools.md
proves a=O(log2n), b=O(H), H=sqrt(n log2n), including ALL allocated buffers.
Before each nonsource core event perform stored-bit ripple comparison and
increment. A whole-node reservation is the same b-bit subtraction/comparison;
after reserving G its known bounded instrument is padded and debited.
Its guard does not interrupt a promised complete instrument.

Construct each clock-bit's global indexed address by schoolbook a-bit
arithmetic. Including generation of those operations' own operand indices
and loops takes O(a^3) raw steps per addressed bit. Charge EACH raw step
the full a-bit indexed-access price, giving O(b*a^4+a+1) physical work per
NONSOURCE core event. Ordinary gate/address generation is itself already
core work; its own accesses and this monitor's accesses are all charged.
The monitor is not recursively monitored. No word, index, read, reset or
gate-address emission is free.

A source acquisition has the same controller charge and additionally n+1
for the new DCP register. Count this separately for all Qcap acquisitions.
Other n-bit arithmetic, initialization and clearing are decomposed into
their individual counted core events; they are never single free words.
Thus total body/cleanup work is at most
 O((B+G)*H*(log2n)^4 + (n+1)Qcap).
Cleanup uses its separate G core budget and acquires no sources.

Writing x=log2n, the main proof gives B=O(n^(11/2)*2^P),
Qcap=O(n^(3/2)*sqrt(x)*2^(H/2-2Z)), P=H-2Z+2sqrt(x), Z=sqrt(n)/x.
Since G<=B, the first term is O(n^6*x^(9/2)*2^P).
The source term O(n^(5/2)*sqrt(x)*2^(H/2-2Z)) is smaller, with an
additional positive exponent gap H/2+2sqrt(x). All branch source/work
guards are still enforced before exceeding their caps. Public pre-clock
O(n^16) work is included as well: P>=H/2>=64x, so it fits the SAME
time envelope. The fixed finite prefix is covered by its disclosed
absolute outside constants. No physical preparation cost or controller
work is suppressed by separating source events.
