# PSG49-F7B: measured basis storage for the fixed sieve

## 1. Joint algorithm and theorem

For every N>=2 and s modulo N, n=ceil(log2 N), put L=log2 n, F=sqrt(nL),
G=sqrt(n)L^(-7/16) for n>=2. PSG49-F7B runs the exact PSG49-F7 program of
`core-proof.md`, including q=49/100, f=2599/7401, both literal caps and its
n<256 finite branch, through the measured-basis interpreter of Section 2.
It recovers the ENTIRE secret with unconditional probability >=1-2^-8>2/3.
On EVERY branch it has the simultaneous guarantees

    T=O(2^((7401/9800)F+(3/4)G)), S_C=O(n), S_Q=O(n^2),
    Q=O(2^((49/100)F+(3/8)G)).

The exact growth indices are (1/2,0,0,1/2). All constants are absolute and
include the finite n=1 case. The clean fractional tolerance is 0.
This exchanges physical types of memory. It does not combine the two
memory claims of two algorithms, and does not claim O(n) for both at once.

`core-proof.md` supplies the complete selected program and its proof;
`family-source.md` supplies the complete source algorithms it cites. Both
are included in full. Their selected classical-memory bound O(n^2) is the
LOGICAL memory simulated here, not this snapshot's claimed classical space.
No prior hosted verdict is a premise. The change below is a complete
bit-level simulation with an explicitly charged overhead.

## 2. Measured-basis interpreter

First express the fixed uniform classical controller of PSG49-F7 as its
ordinary finite Boolean instruction program. The core proof already charges
its bit arithmetic, streamed gate generation and indexed reads/writes.
Decompose each Boolean instruction into fixed-size logic on O(1) operand bits,
classical conditional branches and indexed read/write operations. Modular
arithmetic, sorting of the fixed-size discovery list, integer profile search,
loop counters and gate generators are all the explicit finite integer programs
in the supplied source. No exponentially long compiled circuit is stored.

Store EVERY logical classical memory bit of this program, including its
logical registers, labels, stack/frames, frequency records, counters, tables,
working strings, program-control words and simulated input/output buffers,
as a physical qubit in |0> or |1>. Its original quantum registers remain quantum
registers. Memory-bit addresses and quantum-wire addresses have O(log n) bits,
since the core proof's peak logical classical plus quantum memory is O(n^2).
A constant finite interpreter program is uniform, fixed independently of N,s.
It keeps a bounded number of physical classical address, operand, branch and
instruction words; long simulated words live in the basis-qubit bank.

To read an addressed bank bit, perform a computational-basis measurement of
that classically addressed wire and put the result in one temporary classical
bit. This leaves its basis value unchanged. To write desired value b, read the
old bit a and apply X iff a differs from b. Erase temporary classical bits
when the instruction finishes. Fixed-size Boolean logic then reads its few
operands, computes the desired result in O(1) temporary bits, writes it back,
and clears those bits. To follow a branch, read the condition and update the
simulated instruction-control word by the same operations. A finite microprogram
implements variable-length arithmetic and nested loops one Boolean instruction
at a time, reading/storing their control variables in the bank. It does not
hold a full n^2-bit logical state or a full circuit in physical classical memory.

To execute an original quantum instruction, compute its finite gate type and
classical wire addresses in this interpreter, apply the same gate to the
original quantum wires, and recycle temporary words. If a wire-address word
is stored in the bank, read its O(log n) bits by the operations above before
applying the classically addressed gate. Original computational-basis
measurement results are written into their simulated bank slots. Original
fresh |0> allocations, measurements, source-copy acquisitions, discards and
exact H,S,Toffoli/CNOT/NOT gates are executed in the original order.

Only CLASSICALLY addressed accesses occur. No address superposition is used,
no coherent random-access primitive is assumed, and every measurement, write,
reset, gate, memory access and address construction is paid. An address is
obtained by streamed bit operations, not a free read of an integer word.
Original logical allocation/release uses one bank wire per logical controller
bit, resetting released wires for reuse. The interpreter keeps the original
logical slot layout: logical stacks/frames and their own allocation indices
are bank data. The finite uniform program computes a physical bank address
from a logical slot address with O(log n) temporary bits. The original peak
O(n^2) slot bound therefore bounds the bank as well. Arithmetic scratch and
control words of the simulated program occupy their original logical slots;
only O(n) interface words and O(log n) address scratch are added. No auxiliary
allocation table or growing instruction array is introduced. All these
allocation, reset and address computations are paid.

The physical classical controller includes the initially delivered binary N,
the length n, its final n-bit answer, and a constant number of n-bit boundary
or source/circuit-interface words. These total O(n) bits. The simulated
instruction pointer and loop control can remain in the bank. Even keeping a
single global microstep counter classically costs O(n): from core-proof.md's
literal R<=ceil(n/2), both budget logs and the branchwise total-work log are
O(n), up to absolute constants, including the fixed finite branch. No growing
array is retained as physical classical data. Each long comparison/arithmetic
word in the original program is evaluated through the bank one bit at a time.

## 3. Exact equivalence, including mixed states

At each measured transcript the simulated classical bank is a computational
basis string identical to the original controller's state. Jointly with quantum
data it may be a classical-quantum mixture

    sum_x p_x |x><x|_bank tensor sigma_x.

Reading a bank bit in the computational basis preserves this mixture and
does not disturb sigma_x on a branch. Writing and classical logic transform
x exactly as in the original controller; its chosen quantum gates, conditional
branches, source requests and outcome storage therefore agree. Induct on the
finite instruction sequence, including original measurements. Tracing out the
bank gives exactly the same law of all logical transcripts and quantum data
as the original adaptive program. No assumption that labels are independent
of held quantum states is needed for this simulation.

The proof applies to the challenge's mixed source and its inaccessible x.
Additional basis measurements are merely reads of already classical records;
they do not measure an unmeasured source or quantum query register. Therefore
all correctness, cap, decoder and extraction proofs in core-proof.md apply
unchanged. Source acquisitions occur in exactly the same order and number.
Full-secret success remains at least 1-2^-8 for all N and s.

## 4. Joint charged resources

The bank occupies O(n^2) qubits because it replaces the original O(n^2) logical
classical bits one for one, plus a constant number of O(n)-bit interface words.
The original quantum memory remains O(n). Thus total peak quantum space is
O(n^2). Physical classical data and the finite controller use O(n) bits as
shown in Section 2. This includes N, output, addresses, operand bits, counters
and any boundary words. The source memory excluded by the rules is unchanged.

The selected original program's every-branch ledger BEFORE positive-gap
absorption is

    T_raw=O(n^(5/2)L^(5/2)2^R),
    Q<=Qcap=O(n(2u+6)2^(R-u)).

A direct indexed bank-bit access costs O(log n) addressed operations; assembling
a complete O(log n)-bit gate address costs a polynomial in n in the most
conservative bit implementation. The finite interpreter described above uses
at most polynomial(n) extra work per original instruction, with no new search,
source access or quantum lookup. It needs no extra polynomial-size classical
workspace or extra asymptotic bank size: its finite program and long scratch
are the original logical slots and O(n) interface scratch. Its own addressed
gates pay O(log n) since total allocated memory is O(n^2). Thus total work is
at most polynomial(n)2^R on EVERY branch. This deliberately conservative
polynomial overhead is safe for the exact envelope because it is applied to
T_raw before the gap is absorbed.

The inherited analytic bound R<=(7401/9800)F+G/2+1 leaves the positive gap G/4
to the declared (3/4)G. Since G/log n tends to infinity, this gap absorbs every
fixed polynomial interpreter overhead as well as all original polynomial
work. Consequently T=O(2^((7401/9800)F+(3/4)G)). The number Q of source copies
is EXACTLY the original branch count. The same source gap
3/8-2401/7401=2995/59208>0 gives the stated Q envelope. Neither memory claim
uses this absorption; their explicit bit/qubit counts are already proved.
The finite input prefix changes only absolute multiplicative constants.

The indices follow as in core-proof.md Section 6: both exponential envelopes
have index 1/2, both polynomial memories index 0. This is one physical
algorithm: a measured-basis simulation of the selected complete core.

## 5. Fraction and scope

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

The fifth fraction is exactly 0. All five claims refer to the same measured-
basis configuration. The construction trades more quantum storage for less
classical storage and does not prove a time-index breakthrough, positive
malformed tolerance, both linear memories, or practical advantage.
