# Aligned bit-array work monitor for COL18

This is an explicit CLASSICAL implementation lemma, not a RAM word operation
or a change to the mathematical source. It implements the same B-core-step
guard as COL17 with a smaller fully charged overhead. All data, address
registers, padding, initialization, pointer arithmetic and their own accesses
are allocated and counted. No clock operation is hidden in another clock.

## Layout and functional invariant

Let B>=1 be the literal integer core cap, b=ceil(log2(B+1)),
k=max(1,ceil(log2 b)), P=2^k. Then b<=P<=2b. Reserve two disjoint
P-bit aligned CLASSICAL blocks, one for the constant B and one for a
counter c initially0. Pad high bits by0. Their ordinary absolute addresses
are multiples of P, so an element address is a fixed binary prefix followed
by the k-bit element index j. Compute block bases, prefixes, padding and
initial contents once by counted integer operations. Alignment adds only
O(b) bits beyond the two arrays. This is an allocation choice, not advice.

Use resident absolute-address operands with those fixed prefixes and a
current index j in[0,P). The prefix is not added or copied afresh for each
position: the address value is the fixed concatenation prefix||j. Every use
of that resident address still costs the FULL global address charge A below.
The changing suffix is k bits. It is copied/updated by counted small-word
bit loops; it is never treated as a unit-cost integer or hidden instruction.

At entry, scan both blocks from least to most significant bit, accumulating
one equality flag. If c==B, abort before the next core step. Otherwise scan
the counter with an ordinary one-bit carry and add1, preserving high padding;
then execute one core step. Reset j to0 at each completed pass. Each scan
uses at most P positions and a fixed number of flags. The invariant0<=c<=B
holds by induction. A nonaborting entry has c<B, so the increment has no
overflow past b bits and returns c+1. Exactly B core steps can occur before
abort. No secret or favorable measurement history enters this invariant.
The carry/equality automata and call/return control have fixed finite states.
The core controller's tapes/state are preserved while the monitor runs.

## Explicit local control rather than A-bit addition per position

Here is a conservative implementation bound for the moving suffix and all
its own loop positions. A Boolean copy, compare or ripple increment on a
k-bit local word can be generated with at most C k^3 primitive bit/head
operations, before applying the global address charge. The logical ripple
has O(k) positions. Their positions have O(log(k+2)) bits; generate/update
those positions by ordinary schoolbook bit loops, including their counters.
Where those loops need a bit-position counter, apply the same construction
at the strictly smaller width ceil(log2(k+2)). Recursion stops at a fixed
small width with literal Boolean templates. The decreasing widths and the
bound (log2(k+2))^3=O(k) give a uniform C k^3 total; finite smaller widths
are absorbed in C. All primitive accesses in this construction are still
charged by A; the recurrence is only a CORE count, not an access exemption.

To make this local accounting literal, reserve each small word in an aligned
block of at most twice its width. Its bit addresses also have a fixed prefix
and a moving index of the next smaller width. The prefixes are computed at
initialization and remain resident. This terminates with the fixed finite
Boolean templates, so the controller's own address arithmetic is included,
rather than an infinite regress or an indexed instruction oracle.
The address operand may use fixed wiring for its unchanged prefix and its
current suffix; no integer addition or permutation of data is assumed free.
The indexed bit operation's mandatory A-bit address cost accounts for using
the full resident address. Suffix generation is additional counted work.
If prefixes/registers are copied when entering the monitor, even O(A) bit
copies, each paying A, contribute O(A^2) per entry and are included below.

There are O(b) array positions and O(k^3) local bit/control operations per
position. Each one, INCLUDING accesses to the local pointer/control words,
pays the whole allocated-memory charge, bounded by A bit operations. The
compare/carry logic and main array reads/writes are smaller. Consequently
one complete guard/increment costs
 O(A^2+b*A*(log2(b+2))^3)
fully charged work, not O(1), O(b) or an uncharged word increment. The
monitor is not recursively monitored; this complete work is explicitly added
for every core step. Source acquisition additionally pays n+1 as specified.

## Application to the declared sieve

COL18's literal cap formula is identical to COL17 and algebraically gives
B<=2^300 n^5*2^(2u), u=ceil(sqrt n). Its core allowance is at least2^R
with R>=u, so b=Theta(u). The complete classical/quantum allocation has
address width O(u). Use the same conservative A=ceil(2^10u) padded width
as the main proof. Added aligned clock/control blocks have at most
O(b+A log(b+2)+(log(b+2))^3) bits, polynomially smaller than the tables
and within the main polynomial scratch allowance. They add no quantum space.
Every alignment gap and resident prefix bit is included in this bound.

Thus each guard and its own accesses cost O(n(log2 n)^3), including a
source operation's extra n+1. Ordinary core accesses/gates pay O(A) and
are also covered by this bound; their address generation already belongs
to the core task ledger in the main proof. Multiplying the core cap yields
T=O(n^6(log2 n)^3*2^(2sqrt n)). The quantum operations, source cap,
precision, success budget and resource contexts are identical to COL17.
Initialization and cleanup of these blocks use the same bit operations and
full address charge; they fit the stated total, as does all earlier setup.
The finite n=1 branch is separately specified since log2 n vanishes there.
No old review is a premise for this new monitor lemma.
