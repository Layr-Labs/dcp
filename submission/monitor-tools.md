# Fully charged bit-serial working clock for QSR1

Let a=ceil(log2(M+2)) for the ENTIRE allocated classical/quantum memory,
and b the largest of the working/source counter lengths. The main proof
gives a=O(log n), b=O(sqrt(n log n)). Both include constants and actual
preparation/count/metadata buffers; this is not quantum-addressed memory.

Before each core event compare/increment the stored binary clocks by full
ripple passes. Reserving gcount is the same b-bit subtraction/comparison;
a completed block debits its fixed cost and no guard interrupts a unitary.
A source event also checks its source counter before acquisition. Every
counter bit, carry, loop index and generated address is stored and charged.
There is no free word operation or recursively monitored monitor.

For each bit in a clock pass, construct the global indexed address by
schoolbook addition/copy on a-bit words. Straight bit-serial loops and their
own a-bit indices use at most O(a^3) primitive bit/head operations per
address, including generation of the controller's own operand indices.
Charge EACH such operation its full a-bit indexed-access price, giving
O(a^4) per addressed clock bit. The b-bit passes and gate/source event
therefore cost at most O(b*a^4+n+a), with all constants independent of
outcomes. Ordinary address/gate generation outside the monitor is itself
core work and receives the same final access charge; this bound includes it
rather than treating those events or the monitor's own accesses as free.

Writing x=log2n and H=sqrt(nx), the bound is O(sqrt(n)*x^(9/2)+n).
Since x^3<=n throughout n>=2^20, x^(9/2)<=(n)^(3/2), so it is O(n^2).
Terminal cleanup has at most G additional core steps and no source copies;
its loops obey the same charge. Thus body work O((B+G)n^2)=O(Bn^2).
The deterministic parameter preprocessing is separately fully charged by
its public worst-case bound. No machine-width assumption, source inverse,
free index or uncharged reset/initialization is used.
