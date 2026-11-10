# LLV-GBANK-RATIONAL-PURE: linear classical storage at pure half-root source growth

## 0. One physical algorithm and joint guarantee

For every N>=2 and s in Z/NZ put n=ceil(log2N). The one physical
LLV-GBANK-RATIONAL-PURE interpreter below executes the complete virtual program V
in virtual.md and recovers the entire secret with unconditional probability
at least 1-2^-8 from independent ideal source copies. On EVERY branch,
including failed extractions, retries, discarded sources, abort and cleanup,
 T=O(2^((1/2)sqrt(n)log2n+sqrt(n)*(log2n)^(1/8))),
 S_C=O(n) classical bits, S_Q=O(n^2) allocated qubits,
 Q=O(2^((1/2)sqrt(n))) acquired source copies.
All outside constants are absolute. The representatives apply for n>=2;
the same finite virtual branch and physical simulator cover n=1.
The four exact growth indices are [1/2,0,0,1/2]; only time scores [1/2].
The guaranteed malformed fraction is 0 with this exact model:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

The basis-qubit bank, all its metadata and unused padding, original
coherent data, source scratch and allocation growth count in S_Q.
This is a concrete storage tradeoff and a sharper time representative
for the same selected virtual parameters. It claims neither fourth-root
TIME nor dominance of the square-root-time, larger-source family.

## 1. Actual direct sources and full evidence

The selected complete virtual program is GPS-RATIONAL-PURE, supplied in
virtual.md under a virtual-only scope header. Its full proof hash is
deea23d00ca8fabfe817d24bccbdbae9d309680308e7ea8dca4b467aaa412d6a.
It selects p=2,q=1,beta=1/8,eta=1 and recomputes all actual width,
source/cap/precision/decoder quantities. The full proof is included,
not an opaque historical theorem. Its public identifier and artifact
checks accompany the note/dependency declaration before upload.

Immediate physical-template source: LLV-GBANKQ4-PURE, full main hash
9a6436538bf63b4fe5b388118b3e84821d2395a3a3f2399bd41f4975e4fb1de1.
Its public mapping and verified evidence accompany the note before upload.
We retain its seven padded regions, typed ownership, measured READ/WRITE,
growing paired span, exact CQ/channel proof, source moves, output-first
cleanup and separately paid n^16 interpreter. Its fourth-root virtual
profile is replaced by the complete selected pure-half-root program.
Historical physical source LLV-GBANKQ13,
32c09169-8484-4657-b441-5b3e1f4b542c, commit
a048955fb8c3caa85916fd174db14971962f4f9b, was fetched and its full
main/virtual hashes matched official resource evidence. No predecessor
verdict or provisional graph relationship is a mathematical premise.

The physical template credits LLV-GBANK, proof SHA-256
488ba20d6ea74838bc45716fd7358866089a8e35cd8a46df8eb75b70f2d04b4f.
We retain the template's complete fixed-region/direct-wire method, measured READ/WRITE,
CQ/history proof, source-moving channel, complete decoding and separately
charged overhead. Its different virtual tree/profile is not adopted.
The selected virtual program here is exactly GPS-RATIONAL-PURE in virtual.md.
The bank source credits PSG21, 9fdfdb12-834d-441c-8bb1-717ab380abf3,
proof 43e2ac8f392a5301733dbb393088588641b06c3345864d83002f123a6de3830f,
for generic measured-basis storage, CQ coupling and overhead, and GordoAR's
PSG2-QSTORE, 2b2b0036-7bbc-4ce5-80a8-b8928f0ce120,
main 92b96a0fee5eb35ec700ef6449ec16c8cd05c806f0fe7cab980576099ccc776a,
transfer 5c44c9268e55edf7bc55277ef244e97d9730dd1f09f1e13fa3746a54d34a5325,
for fixed maximum address spans and direct stable mapping. These inherited
credits and all V's credits remain. No Dense virtual program or PSG21
parent algorithm is imported. The two immediate materials (the refined V and the physical template),
public mappings and source/use citations accompany the submission; pending
attribution is not a verified ancestry or redundancy decision.

## 2. Exact virtual configuration and instruction stream

Run V's complete instruction, source, search, decoder and guard sequence.
On its main branch n>=2^4096, compute integers
 v=ceil(sqrt(n)), ell=ceil log2n, z=ceil log2ell,
 b=v*(ell+2z+16), m=ceil((n-1)/b).
Integer root calculation, ceilings and all preprocessing are charged.
For each requested D, 2<=D<=n, put B_width=D-1. Allocate widths TOP DOWN
from level m to 1, b_i=min(b,remaining width), and r_i=b_i+1 on nonzero
levels. Their total width is B_width. A zero level passes through the
same owned qubit without cloning or allocating another state. Put
 q0=(b+1)^m, G=(2(b+1))^m, R=b+1.
The entire pair-search schedule, sign representation, EXTRACT verification,
untouched-bit arithmetic, odd and 2-adic decoders remain precisely V's.
The TWO executed guards are its global acquisition cap and global
fallback/extraction cap. There is no substituted weighted-work cutoff.
In particular every acquisition internal to a failed EXTRACT or fallback
is simulated once; a delivered phase is not counted as one source copy.
The selected finite exhaustive branch is n<2^4096, as in V.

Fix finite uniform bit implementations of Boolean logic, bit reads/writes,
explicit loops, ripple/schoolbook arithmetic, exact Clifford+T primitives,
computational measurement, fair coins, reset/discard and source requests.
Long words are bit fields, never unit-cost operands. A fixed finite
controller generates one instruction at a time. Every recursion frame,
return context, generator cursor, cap/counter and allocator record is
virtual data in the bank. No exponential circuit, full fiber or instruction
history is preloaded. Numeric O(n)-bit counters may have exponential
VALUES, but their bit-cell ADDRESSES use the fixed polynomial spans below.

## 3. Fixed padded regions and maximum address spans

Put r_addr=ceil(log2(n+2)), U=2^(2r_addr), C=2^48, W=C*U.
Reserve seven virtual classical regions of W bit slots at bases tW:
0 input/parameters/profile/caps/constants;
1 retained signed labels, root/node pool and free/reference metadata;
2 recursion frames/return contexts/loop state;
3 current label sums/residues/search/pair-description scratch;
4 source/EXTRACT/transforms and schoolbook bit arithmetic;
5 decoder records, residues, scores/CRT and streamed candidate;
6 reusable generator, allocator, instruction and remaining control scratch.
All subfamilies have fixed padded row/field subranges. Freed, failed or
retried objects reuse the SAME addresses; there is no lifetime-name
counter, sparse address dictionary, per-bit key or external active flag.
Profile indices and frame depth are at most m+1. No array grows with the
number of attempts. Subrange bases can be prefix sums of the following
analytic capacities, computed with charged bit operations.

Here are capacities independent of correctness events, including wrong
extracted labels. Virtual9.1 gives R<=n and m<=n. Because
m=ceil((n-1)/b), mb<n-1+b and thus mR< n-1+b+m<=3n.
For any actual width, sum over nonzero r_i=B_width+number(nonzero)<=2n.
The depth-first live phase count is B_width+1<=n+1; reserving R child
slots at each of m levels even bounds their total fixed slots by 3n.
Decoder root count K<=2^15*sqrt(n)<=2^15n, from virtual9.1.
At most a fixed multiple of mR+K+R+1 nodes cover pending siblings,
current roots, active source/combiner helpers and ownership references.
A literal pool has 2^17n slots of 16n bits each. Each retained phase has
one signed label, a bounded reference/owner and free metadata. Source9.2
bounds label magnitude by q0*2^D; log2q0<=log2G<=sqrt(n)/2 on the
main branch by virtual9.1's intermediate inequality. A full 3n-bit signed
field therefore suffices, even for wrong labels. The 16n template covers
label, pointers and fixed header fields for n>=2^4096. This pool uses
2^21n^2 bits, below a region capacity. Root batches reuse these slots.
Ownership passing at a zero level moves the reference to the SAME qubit;
erasing an obsolete label/reference does not reset that qubit. Release
quantum data only when V itself releases its final logical owner.

At most m+1 frames, their fixed number of O(n)-bit counter/cap fields,
profile and return contexts fit 2^20n^2 bits. Acquisition and fallback
caps have O(sqrt(n)+logn) bit lengths; search iteration words need at
most R+O(logn)<=O(n) bits. For a current r_i-input combiner, signed labels,
residue and pair description have at most O(n) rows of O(n)-bit fields.
It retains only the fixed number of found Grover strings and a current
query of at most R bits, not all subsets or fibers. The serial controlled
label-sum/exclusion predicate streams known row j and label bit: read its
classical value and emit the SAME controlled addition/exclusion gates on
the coherent subset bits. A superposed subset y never selects a bank
wire. These current arrays and fixed scratch copies fit 2^24n^2 bits.
Schoolbook multiply/divide/Euclid and source transforms/EXTRACT reuse
2^24n^2 bit templates, with streamed tests rather than saved outcomes.
The fixed finite trigonometric table has fewer than 2^20 bits. Decoder
K records and fixed copies of residues/score/current candidate fit
2^24n^2 bits, by K<=2^15n. It streams candidates; no list of all candidates
exists. The finite family of generator/allocator/control subfamilies fits
2^40n^2 bits per collection, still below C*U since U>=n^2.

The finite branch stores candidate/test/acquisition counters, source/shift
scratch and streamed arithmetic, not all outcomes or candidates. Pad its
fields to fixed multiples of n+1 rather than using the main 3n label
shortcut. These same generous capacities cover every finite length,
including n=1. Finite code and every compile step are charged.
The MAXIMUM classical slot plus one is consequently B=7C*U=O(n^2),
independent of retry count, not merely an observed live-space bound.

For logical quantum slots use a fixed pool with maximum slot plus one
H=2^32*2^r_addr=O(n). The mR<=3n per-level phase slots, K<=2^15n roots,
O(R) query/residue scratch and O(n) source/EXTRACT/helpers fit this H.
Alternatively allocate individual cells within the same fixed pool;
free scans/bitmaps, heads and register-ID lists are counted bank data.
A logical register uses an ordered bank-resident ID list; generate gates
on its known IDs in logical bit order. Stream one ID per gate or source
SWAP, never stage an entire n-entry map in physical classical memory.
The O(nlogn) pool metadata fits the above capacities. Released cells use
Section4's discard/reset channel; slot reuse never invents lifetime IDs.
This is a maximum address range as well as a live-qubit bound, with no
contiguous-free-block assumption. The finite branch also has O(n) live
qubits. Both spans are polynomial; complete addresses have O(logn) bits.

## 4. Physical bank, access and executed operations

Store virtual classical bit i as the basis value of physical wire2i.
Store virtual quantum wireq at wire2(q+1)+1; reserve wire1 for a fair bit.
Maintain one allocated paired prefix0,...,2h-1, initiallyh=2. Before
accessingi>=h orq+1>=h doubleh until the slot fits, appending and
initializing every new wire. Old indices/states remain fixed. Never
shrink the prefix duringV. Every unused padding wire counts inS_Q.
The maximumh is below2max(2,B,H+1), so the entire prefix isO(n^2).
No per-bit key, active flag or translation directory is added. V's own
allocator metadata remains in its counted virtual regions.

READ(i) measures known wire2i inZ into a reusable classical bit.
WRITE(i,b) reads oldz, appliesX exactly whenz differs fromb, then
clears the temporaryz after its last use. Reset isWRITE(i,0).
Read before writing operands, including aliased fields, inV's exact
order. A Boolean primitive stages its fixed number of bits and writes
its output. Multi-bit arithmetic and field decoding remain loops of
these operations; no long word is a unit-cost fetch.
A released virtual classical field is cleared byWRITE(i,0) on all its
cells, with temporary read outcomes forgotten, before the same subrange
is reused. All free/pool metadata is updated through the same interface.
This avoids retaining an uncounted classical release history; the full
range-clearing cost is included in the polynomial overhead.
All bank addresses are CLASSICAL. Ordinary gates on classically selected
wires are allowed; compute the complete wire index and pay its address
fee. For a conservative upper work bound, charge even a full
classical scan of the reserved bank per access, as well as all actual
indexed gate/address work. There is no coherent bank query or extra QRAM oracle.

V's original coherent table lookups are implemented by their existing
SERIAL row scans. For each known row and bit, READ its stored classical
value and generate the same controlled gate on the original quantum
index/equality/scratch registers. A superposed original table index never
becomes a bank wire address. This retains every coherent control and
phase exactly, while using only classically chosen bank reads.
Every gate/operand descriptor is generated/decoded through the same bit
interface. Fixed Toffoli operations expand to exact Clifford+T words;
no uncounted circuit compiler or stored exponential instruction list.

Execute everyV gate, measurement, coin, reset, discard, source request,
guard, failure and retry at its specified virtual position. Stage a
measurement result only until it is streamed to its virtual field;
there is no growing classical measurement transcript. A fresh fair bit
usesH andZ on reserved wire1, writes it asV requests and resets it.
For a source request ensure the mapped source slot exists and is zero,
acquire exactly oneDCP copy on n+1 temporary wires, and if needed move
it byn+1 SWAPs to the mapped slots. Each SWAP is three CNOTs; the
now-zero temporary wires are released before prefix growth. This adds
O(n) temporary qubits and counted work but no second source copy.
No bank initialization or inverse calls the DCP source.

For reset/discard use the allowed trace-out/reinitialize channel, or
Z measurement followed by conditionalX with the outcome forgotten.
This channel equals trace-out followed by fresh zero even with arbitrary
references. It does not presume the discarded register is independent.
AfterV terminates, stream its final residue to the countedO(n)-bit
classical output FIRST; only then clear/release the entire prefix and
short fields, retaining that output. All cleanup work is counted.

## 5. Exact classical-quantum invariant

At aligned virtual steps the joint state, including arbitrary referenceR,
has the form
 sum_(c,z) p(c,z) |z><z|_controller tensor |c><c|_bank
                   tensor rho_(c,z)_(mapped V registers,R).
Herez contains finite control and the cleared/staged short fields, and
c is precisely
V's current classical record, not a coherent unknown memory string.
The bank and live registers may be correlated; a stored measured label
can be correlated with a still-coherent phase/query register. No product
or independence assumption between these systems is needed.

Initialization gives the invariant. For READ of biti, projectors onto
c_i=b leave the nonselective CQ state unchanged. Keeping the outcome
only appends the virtual bit on each conditional record; rho_c is
unchanged. WRITE produces precisely the updated basis string. When
records merge after an irreversible overwrite, their conditional states
mix exactly as classical forgetting requires. Boolean steps and pointer
moves update the finite control identically. Original gates haveV's
same conditional action; original measurements and coins have the same
instruments and updatec. Reset/discard has Section4's channel identity.
Each fresh ideal request supplies the same independentrho_s. Induction
therefore preservesV's complete reduced state and classical history at
every virtual step, including failed extraction labels, search failures,
partial children, rejected samples and abort cleanup.

This is not a claim that reading an arbitrary superposed bank is harmless.
Only the reachable CQ representation is used. Extra bank outcomes are
deterministic givenV's classical record. The unconditional full output
law and actual source-request sequence are exactlyV's. In particular,
virtual.md's complete argument establishes full-secret success at least
1-2^-8 for everyN,s. No favorable-event conditioning, acceptance oracle,
source reflection, inaccessible purification or unknown-state cloning.
The argument covers ideal independent source copies only. Under a
different adaptive corruption model extra bank measurements might be
visible to a supplier and change future behavior; no such transfer is
claimed. The exact canonical clean-model text and fraction0 are unchanged.

## 6. Fully charged resources and strict time margin

Input N, final output and a fixed number of O(n)-bit staged operands use
O(n) physical classical bits. Short addresses/scan fields use O(logn)
bits and finite controller code has constant size. All remaining labels,
arrays, call/return state, numeric counters, generator/arithmetic fields
and allocation metadata are in the counted bank. No duplicate classical
recursion stack, map or measurement transcript exists. Thus S_C=O(n).
The WHOLE paired prefix has O(B+H)=O(n^2) qubits, including all padding,
metadata and original coherent data. Growth overlap, reserved fair-bit
and temporary n+1 source wires also fit O(n^2), proving S_Q=O(n^2).
All bounds hold on EVERY branch including initialization, wrong labels,
failed work and cleanup. Basis states still count as allocated qubits.

Every extra bank bit read/write, field decode, address comparison, gate
operand, conditional reset, source SWAP and output-first cleanup is charged.
B=O(n^2), H=O(n); even a full bank scan per accessed bit costs polynomial
work. Clearing a region by separate scans costs O(B^2 polylogn). Emit
schoolbook/ripple gates online, storing no full generated circuit. Source
moves stream n+1 known IDs and cost O(n) gates plus full addresses on top
of V's source charge. A conservative factor O(n^16) covers all these
finite bit loops per charged virtual step, and startup/cleanup as well:
 T_physical <= C1*n^16*(T_V+n^2), for n>=2.
The original acquisition and fallback guards are checked at their exact
virtual points. Added physical work is not hidden by changing a guard
or replacing a branch bound with expected work.

Use the stronger fully charged INTERNAL estimate in virtual Section9,
equation(9.4). With L=log2n, y=sqrt(n), for L>=2^64,

 log2(T_V/C0)<=(1/2)yL+(1/2)yL^(1/8).

Its proof starts from the explicit full work ledger, not a final loose
Big-O representative. The source/circuit/decoder and all virtual address,
preprocessing, failed work and cleanup costs are already included. The
startup n^2 and fixed constants are absorbed by an absolute outside
constant; the separately paid interpreter factor adds at most16L to the
exponent. Virtual9.1 proves y=sqrt(n)>=16L^2. Since L>=4096>=16,
y>=256L and16L<=y/16. Therefore

 (1/2)yL^(1/8)+16L <= (1/2)yL^(1/8)+y/16
                         <= yL^(1/8),

since L>=1. This proves the exact selected physical time envelope
O(2^((1/2)sqrt(n)L+sqrt(n)*L^(1/8))) after ALL interpretation and
cleanup work. Finite smaller lengths have the same capped program and
interpreter, and change only an absolute outside constant. No new branch,
favorable postselection, source oracle or omitted polynomial is introduced.

Every physical source request corresponds to exactly one virtual request,
including all internal EXTRACT and fallback acquisitions; there are no
others. Local zero bank/padding qubits are charged time/storage, not DCP
copies. Source9.1 proves Qcap<=2^((1/2)sqrt(n)) on every main history;
the unchanged finite branch changes only its absolute outside constant.
Thus Q=O(2^((1/2)sqrt(n))) on every physical branch. Section5's exact
CQ/channel induction preserves V's whole output law under independent
ideal copies. Its full included proof therefore gives unconditional
full-secret success >=1-2^-8 jointly with all resources and clean error0.

## 7. Binding and exact indices

All five current physical claims cite this main and full scoped virtual.md.
No older JSON, historical verdict or missing algorithm is a premise.
Virtual V's quadratic classical/linear quantum declarations are virtual
only. The one current physical interpreter has S_C=n, S_Q=n^2 envelopes.
The time logarithm has leading (1/2)sqrt(n)log2n, exact index 1/2.
The source envelope has exact index 1/2; polynomial spaces have index0.
Only time is the numeric objective. These are indices of upper envelopes,
not matching lower bounds. Lower source demand trades greater time than
the square-root family; the bank moves quadratic classical data to counted
qubits. No generic novelty, priority, practical timing, positive corruption
tolerance or optimality is asserted. Fourth-root refers to source growth.


## 8. Scope of the analytical family

For every fixed rational0<beta<1 and eta>0, the complete virtual proof
bounds its fully charged work by leading term(1/2)sqrt(n)L plus
(eta/2)sqrt(n)*L^beta eventually. The same polynomial physical factor
contributes only O(log n), absorbed by the remaining positive half-term.
Thus the same physical interpreter has the corresponding full time
family, unchanged other resources, success and clean model. Constants
may depend on fixed beta,eta, never on N,s or outcomes. Only beta=1/8,
eta=1 is numerically declared. No beta=0 endpoint, exact loglog syntax,
optimality, faster physical program or time index below1/2 is asserted.

The complete fixed-rational source/time law in virtual.md is a VIRTUAL
theorem. The current physical row selects only p=2,q=1,beta=1/8,eta=1.
It does not mix other exponents or V's original memory columns with this
interpreter's physical allocation. Parameters are fixed before asymptotics.
