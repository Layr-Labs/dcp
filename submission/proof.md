# PSG21: a measured basis-state bank for the clean streaming sieve

## A. One physical algorithm and its joint theorem

For every N>=2 and s in Z/NZ, let n=ceil(log2N), L=log2n. The single
physical algorithm PSG21 below recovers the entire s from independent
ideal source copies with unconditional probability at least1-2^-8>2/3.
Its simultaneous every-branch bounds, including all failures and aborts, are

 T=O(2^((819/1000)sqrt(nL))), SC=O(n), SQ=O(n^2 L),
 Q=O(2^((819/2000)sqrt(nL))).

These asymptotic representatives apply for n>=2, with the explicit finite
parent branch and its finite simulation coveringn=1. All outside constants
are absolute. The indices are[1/2,0,0,1/2]; only time is numeric score[1/2].
The fifth claim is fractional tolerance0 under EXACT model text:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

This is a physical storage tradeoff: all emulated classical data and its
address metadata are counted as allocated qubits. The controller itself
has linear classical storage. The larger quantum envelope is part of the
same configuration, not combined with a different smaller-memory run.
No positive robustness, optimality, cube-root time or practical speed is
claimed. In particular no robustness conclusion under newly exposed
bank measurements is inferred from a different adversarial model.

The complete immediate working artifact is PSG17, submission
b1f0c9d8-e0b1-4f3e-b744-a35b392fa8c4, local1623b61. It supplies the entire
virtual program P, reproduced exactly in parent.md, including its circuits,
parameter rule, two guards, source precision, complete decoder, finite
branch, success proof and sharper INTERNAL resource accounting. Its public
archive is declared when eligible; no unpublished commit identity is
invented. The new component is the explicit basis-bank interpreter and
its charged simulation proof here. No additional outside proof component
is separately imported. The parent retains its historical source credits;
no provisional ancestry or predecessor verdict is a mathematical premise.

## B. The virtual program P and physical representation

Execute the precise PSG17 program in parent.md, with u=floor(R/2), through
the interpreter below. Every specification and resource assertion in that
file refers to the VIRTUAL parent machine, not PSG21's physical classical
allocation. The full file is included as a proof, not as an accepted-result
oracle. Its source identities, unused-block induction, quantum circuits,
full-modulus decoder and cutoff proof are reproduced there in full.
PSG21's physical resource assertions are exactly SectionsA,C,D here.

Choose its bit-level implementation as described there: finite uniform
control code; Boolean logic and bit reads/writes; explicit integer loops;
Clifford+T gates and computational measurements; source requests, reset,
allocation/release and fresh classical coins. Multi-bit arithmetic is
expanded into the counted bit operations and addresses specified there.
The instruction stream is generated online, not stored exponentially.
The parent's recursion/call state, loop counters and gate descriptors are
ordinary virtual memory, and are emulated with the rest of its data.

The parent's actual peak virtual classical allocation is S(n)=O(n^2).
Its described arrays, labels, scratch and frames have bit addresses of
O(log(n+2)) bits. Its numerical words have O(n) bits: signed phase labels,
N/residues, source/work counters and precision parameters have these
explicit bounds in Sections3,5,8,9 of parent.md. The trigonometric table
is a fixed finite computation of absolute size. We fix their ordinary
bit-level implementations; a constant number of O(n)-bit staging words
suffices for an instruction, and additional working words and all stack
state are virtual cells rather than physical classical storage.

Represent each LIVE virtual classical bit by a record in a bank of
computational-basis qubits. A record has an active flag, the virtual bit
address, and its value bit. Address words and record flags are included:
each record has O(log(n+2)) qubits. Records for dead cells are marked free
and reused. A doubling-capacity array of records, retained after shrinking,
has capacity at most a fixed factor times the largest live-cell count
so far, plus a fixed constant. Each expansion copies the old records by
measurement into fresh basis qubits, resets/releases the old bank, and
counts both banks during copying. Hence bank peak is O(S(n)log(n+2))
qubits, not a function of the number of cells ever allocated or the
possibly exponential number of interpreter steps. Free records need
only their active flag until reused; resetting and overwriting them is
explicitly counted.

Virtual qubit i is mapped to a separate set of physical wires (for example
using even wire indices), while bank wires use a disjoint set. Current
maximum indices and allocated space are O(n^2 log(n+2)). Computing wire
indices and every addressed operation pays its full address debit.
Source registers may arrive in separate temporary wires and be moved by
counted SWAP gates to the assigned virtual-register wires; this adds
O(n) gates per request and O(n) temporary qubits. It does not request an
extra DCP copy. The source state and gate action are otherwise unchanged.

## C. Explicit access, execution, semantics and storage

All bank addresses are CLASSICAL when accessed. To read virtual addressj,
scan active records using a classical record index, measure the basis
flag and successive basis key bits, and compare withj by Boolean steps.
On the unique match, measure its value qubit in Z into a temporary
classical bit. A write scans in the same way, measures the old value,
and applies X exactly when old and new differ. To create a record, scan
for a free slot or expand capacity, reset its basis qubits by Z followed
by classically controlled X, and write its key and value in the same way.
Release marks matching live records free; range release scans and compares
keys. Empty/unused classical regions may be reserved by virtual allocator
metadata without allocating a physical value until initialized. If an
instruction initializes a whole region at once, perform every record
creation and count it; the work bound below permits even this conservative
implementation. Failed allocations/aborts follow the parent's specified
branch. Every bank measurement, comparison, reset, X, initialization and
address computation is charged.

There is no coherent lookup or extra QRAM oracle. Even a one-bit read may
scan the whole bank. Temporary classical storage consists of the inputN,
the eventual output, a fixed number of O(n)-bit staged operands, requested
addresses, scan counters and the finite interpreter state. It is O(n).
The parent loop/call/return context is represented in bank cells; it is
not an uncounted classical interpreter stack. Multiword operations are
bit loops with their intermediates in bank cells or these fixed staged
words. Parent instruction decoding and generator steps are included.
Quantum measurement outcomes are streamed into bank records, with at
most O(n) outcome bits staged if a whole source-sized register is read.
Fresh coins are generated and recorded as the parent requests them.

Condition on the complete coupled virtual history. The bank is always
EXACTLY a computational-basis encoding of the virtual RAM state. The
original virtual quantum registers have exactly the state prescribed
by P on that history. This holds initially by basis initialization.
A bank read measures a definite bit and changes neither its value nor
the conditioned state of the original quantum registers. A write/reset
or allocation updates exactly the corresponding classical value. A
parent quantum gate, source request, coin or original measurement is
executed identically on the mapped registers and updates the encoding.
Release and discard reproduce the same reduced state. This proves the
invariant inductively for every step, including failed search, rejected
samples, cleanup and abort paths. Equivalently the bank/original-register
state is a classical-quantum mixture over basis encodings, and these
accesses implement ordinary reads of that classical component.

All extra bank measurement outcomes are deterministic given the encoded
virtual data when read. They do not amount to cloning unknown quantum
states, reflecting about a source, or access to an inaccessible
purification. Only the ideal independent-copy model is asserted here.
Under it the coupling preserves the unconditional distribution of P's
original outcomes, termination, entire output and source count. No
adversary assumption under additional information is needed or asserted.
Therefore the complete proof in parent.md gives full-secret success at
least1-2^-8 for PSG21 for every N and every fixed secret, includingn=1.

Peak physical classical space is O(n) by the staged-controller description.
The bank and its metadata use O(n^2 log(n+2)) qubits; original registers
and any source-moving scratch use O(n) more. Peak during expansion is
at most a constant multiple of this total. For n>=2 it is O(n^2L).
This bounds physical allocations on every branch, including wrong
numerical labels and aborts. No virtual classical label, descriptor,
record, original stack word, address map or stored circuit is excluded:
it either resides in this counted bank or the O(n) staged controller.

## D. Charged time and copies for the SAME simulation

We use a deliberately conservative POLYNOMIAL overhead bound. A scan
examines O(S(n)) records of O(log(n+2)) bits; every elementary read/write,
comparison, gate, measurement and reset also pays O(log(n+2)) for its
physical address. A single original bit operation or fixed-arity gate
can therefore be interpreted in polynomial work. Even a region operation
that creates O(S(n)) records with a whole scan per record costs at most
O(S(n)^2 polylog(n+2)). Array expansion/copying and source-register moves
fit the same bound. The finite code's integer and loop instructions are
already decomposed into parent bit steps; staging/parsing adds polynomial
work. Taking a generous O(n^8) factor per charged parent step bounds all
these costs for n>=2, with an absolute outside constant; initialization,
final readout and finite exceptional cases are included. This is an upper
bound on counted gates and classical steps, not unit-cost memory access.
All parallel work remains sequentially summed.

The parent's declared pure exponential bound alone is NOT used to erase
that overhead. Section9 of parent.md establishes the sharper INTERNAL
bound, before its own polynomial absorption,

 T_P=O(n^(5/2)L^2 2^((817/1000)sqrt(nL))).

Thus the physical simulation has the explicit internal bound

 T_21=O(n^(21/2)L^2 2^((817/1000)sqrt(nL))).

The exact gap819/1000-817/1000=1/500 is positive. For any fixeda,b and
delta>0, n^a L^b=O(2^(delta sqrt(nL))), as proved by the logarithmic
limit and explicit certificate in Section9 of parent.md. This applies
also witha=21/2,b=2,delta=1/500. In the sufficient internal-certificate
range L>=1048576, sqrt(nL)>=L^2 and the gap contributes more than2000L,
while the enlarged polynomial logarithm is at most(25/2)L. Hence

 T_21=O(2^((819/1000)sqrt(nL))).

The ordinary P algorithm and the SAME interpreter run at all smaller
lengths; the bounded finite prefix enlarges an absolute constant. No new
threshold or postselected fast branch defines the algorithm. The two
parent guards are emulated exactly, and the polynomial simulation bound
covers every additional physical operation even though it is not a
parent nominal attempt. This establishes worst-case time on every branch.

There is exactly one physical DCP source request per virtual request and
no others. Fresh |0> bank qubits are not DCP copies and their preparation
is charged to time/storage. Consequently the ACTUAL acquired-copy count
is exactly P's count, including every rejection, failed child and abort,
and its separately proved bound remains

 Q_21=O(2^((819/2000)sqrt(nL))).

The four structured envelopes in the JSON are therefore jointly those
of SectionA for this single physical implementation. Both exponential
envelopes have growth index1/2 by loglog/ log limits; n andn^2L have
index0. Tolerance0 matches the exact clean model. No greater tolerance
or impossibility of greater tolerance is claimed. The entire full-secret
proof for the virtual program is reproduced next in parent.md, with
its historical attributions and explicit finite branch.
