# PSG-LB2-BANK: linear classical space for the published log-log-band sieve

## 0. One physical algorithm and joint guarantee

For everyN>=2 ands inZ/NZ putn=ceil(log2N). The single physical
PSG-LB2-BANK interpreter below recovers the whole secret with unconditional
probability at least1-2^-8 from independent ideal source copies. On EVERY
actual execution branch, including errors, failures, discards and cleanup,

 T=O(2^(n/(2log2n)-4n/(log2n)^2)),
 S_C=O(n) classical bits, S_Q=O(n^2) allocated qubits,
 Q=O(2^((log2n)^2)) acquired copies.

All outside constants are absolute. Exact indices are[1,0,0,0];
only time scores[1]. Fractional tolerance is0 under the exact model

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

The bank's basis-state qubits and all padding count inS_Q. They are not
free classical storage or omitted quantum memory. This physical machine
trades the virtual machine's quadratic classical/linear quantum allocation
for linear classical/quadratic quantum allocation. The source and complete
output law are preserved. No positive robustness, practical speed,
optimality, priority or cube-root time is claimed.

## 1. Actual direct sources and complete virtual program

The COMPLETE selected virtual program P is PSG-LB2, public submission
70787ca2-e394-4b8a-9867-b3e29c536ec8, commit
8a7818fd0b3297c8e292b2b255375266b7deba25, full proof SHA256
83d543263d7f3cf2d8d7be8827350fe4b115e502d23a54f760678019382512f6.
Its ENTIRE body is copied byte-identically after the virtual-only scope
header in virtual.md. Every source/collective-extraction transform,
streaming verified-pair Grover combiner, actual log-log-band search,
unused-block/termination proof, full signed-label law, source and
weighted-work cutoffs, all-modulus decoder, finite branch and full
unconditional probability proof is included. Its quadratic classical/
linear quantum assertions concern P, not this physical interpreter.
No prior manifest or review is a mathematical premise. Its PSG-LB,
PSG5-SHARP, PSG5, PSG15 and upstream credits remain, including its
explicit distinction between unpublished local history and actual
public source archives.

The distinct actual storage-adapter source is corrected LLV-GBANKQ25,
public fbb8f36c-3904-4bf0-9ddf-e9f5d83657ae, commit
100a8e307fd90c489c4d90717613869fed576b3b, main proof SHA256
08608c19bf8d7ba42b50cf01f86662bc4e38ae0de63a2825ed4f86c8f10ca7d0.
It supplies seven fixed maximum-region/direct-wire storage ranges,
measured READ/WRITE, exact correlated-CQ forgetting/source coupling,
fully decoded uniform bit interpreter, whole counted paired prefix
and separately charged polynomial compiler overhead. All are reproduced
and adapted below to P's DIFFERENT signed-label/band/decoder/counter
program. Its quarter-square-root virtual program, two-entry-table
fan-in schedule and finishing comparison are NOT adopted. Neither
that virtual body nor its unused erroneous historical comparison is
imported here. P's own bounded verified-pair primitive is used at
every executed arity. Both actual direct sources have full public
artifacts and all5 official evidence checked, and exact source/dependent
citation endpoints. Pending attribution is not certified ancestry.

The generic storage transformation is prior work. Inherited bank
credits remain LLV-GBANK, PSG21
9fdfdb12-834d-441c-8bb1-717ab380abf3,
proof43e2ac8f392a5301733dbb393088588641b06c3345864d83002f123a6de3830f,
and PSG2-QSTORE 2b2b0036-7bbc-4ce5-80a8-b8928f0ce120,
main92b96a0fee5eb35ec700ef6449ec16c8cd05c806f0fe7cab980576099ccc776a,
transfer5c44c9268e55edf7bc55277ef244e97d9730dd1f09f1e13fa3746a54d34a5325.
No other virtual algorithm, external quantum-walk/QRAQM oracle or
positive-corruption mechanism is imported.

## 2. The selected virtual instruction stream

Run PRECISELY P's public integer parameter rule and its complete
source/test/combiner/decoder/two-cutoff schedule. On n>=256 compute
ell=bit_length(n-1),kband=max(1,ell+bit_length(ell)-1-5).
For each positive trial R putj=bit_length(R-1),u=max(1,R-kband*j).
Starting atR descend bydelta(v)=bit_length(3(2v+1)-1), retainv>=u,
reverse into the ascending list, and choose the FIRST R whose twice-sum
capacity reachesn. Scan sequentially without assuming monotonicity.
The scan terminates byceil(n/2). Exact greedy cancellation widths
b_i<=2v_i, child aritiesr_i=b_i+1, zero-width shortcuts and partial
targets are precisely P's; there is no new fixed-fan or finishing rule.
All source/weighted-attempt counters are checked at P's own positions.
The actual caps areq0=(2u+1)2^(R-u),H0=Sodd*K+2n,
Qcap=1024(6q0H0+2n),Wcap=1024*3*mstar*2^R*H0.
P's n<256 exhaustive branch is unchanged. The simulator does not
change a virtual algorithmic choice or add a success-dependent guard.

Fix ordinary uniform bit implementations of the stated arithmetic and
arrays: finite Boolean code, bit reads/writes, explicit integer loops,
constant-arity exact Clifford+T gates, computational measurements,
reset/release, fair coins and source requests. Ripple/bit-serial schoolbook
arithmetic suffices; long numbers are bit fields, not unit-cost words.
The original streamed known-weight and at-most64-solution exclusion loops are retained. Any
virtual call/return state, recursion frame, generator cursor or allocator
record is virtual memory, not an extra physical classical stack.
The instruction/gate stream is generated online by this fixed finite code.
No exponential circuit description or table is preloaded.

Every virtual memory field has a fixed canonical packed location in
Section3. A virtual numerical counter may haveO(n) bits even when its
value is exponential; that does not make its BIT address exponential.
Quantum operands are bounded virtual slot indices. Multi-bit operations
are loops of bit primitives. Their data and intermediate records use the
same counted virtual fields, with only a fixed number of staged operands.

## 3. Fixed regions bound the entire address span

This step is specific toP; a live-occupancy bound alone would not suffice.
Put r_addr=ceil(log2(n+2)),U=2^(2r_addr),C=2^48.
Reserve seven virtual classical regions, eachW=C*U bit slots, in this
fixed order. Regiont has base tW. Its subfamilies use fixed padded
subranges and canonical row/field offsets. All bases are public shifts
and additions ofO(logn)-bit numbers, generated with charged bit work.

0. Input copy, parameters, profile, cap/precision words and fixed constants.
1. Retained phase-label/node pool, current root, free/pointer metadata.
2. Recursion frames, return contexts, loop state and saved counters.
3. Current residue, sorting, tuple-list, rank and search-control arrays.
4. Source/LE/transform fields and schoolbook arithmetic scratch.
5. Decoder records, residues, CRT/score fields and streamed candidates.
6. Remaining reusable generator, allocator, instruction and control scratch.

Allocate each array its analytic upper row count and fixed field width;
reuse its same cells after release. For retained vectors use a bounded
pool or per-level child slots, with free/vector references stored inside
these regions. A retry reuses those slots, not a newly minted permanent
address. Stack frames use depth indices at mostmstar+1<=n+1. There is only
one current found-solution list, of length at most64. Decoder batches reuse one record region. No circuit
or instruction history accumulates with execution time. Each classical
address and pointer uses these region/subrange offsets; there is no
sparse-name dictionary outside the bank.

Here are conservative analytic capacities for EVERY reachable branch,
including wrong extracted labels and both source/work cutoff exits.
P's first-feasible scan has1<=R<=ceil(n/2), retained valuesv>=1,
andmstar<=R. Greedy widths sum to B<=n-1, so the depth-first
frontier has at mostB+1<=n phase qubits. Every partial/full combiner
hasr_i=b_i+1<=n+1 inputs. Released children reuse pool slots.

For integersu>=1, (2u+1)2^-u<=2; henceq0<=2^(R+1).
Full signed labels have magnitude<2^n q0, so3n bits with sign and
fixed padding suffice forn>=256, including wrong numerical labels.
P never reduces these signed labels merely to save storage. Current
signed-label updates may use a fixed number of wider temporary fields;
16n-bit padded arithmetic rows suffice and are counted separately.
Retained node/label, free-list and pointer metadata fit2^24n^2 bits.
A concrete pool reserves2^17n rows of16n bits, i.e.2^21n^2 bits;
the analytic frontier and metadata counts fit it on every branch.

Sinceh<=1+u/8 andlog2q0<=R+1, P's decoder formula gives
K=2^13(ceil(log2nq)+ell+30)<=2^16n forn>=256.
Sodd<=n, soH0<=2^16n^2+2n. The source and weighted caps then
have at mostR+3ell+40<=2n bits in this range. Their exact powers,
products, precision words and all individual numerical fields are
bounded by fixed multiples ofn. The n+5 extraction counters have
O(logn) bits each, and storing them explicitly fits2^24n^2 bits.

At mostmstar+1<=n+1 recursion frames hold a fixed number of padded
O(n)-bit fields, return contexts, counter snapshots and profile data;
2^24n^2 bits cover them and fixed copies. Only ONE found list of at
most64 strings is current, with each string having at mostn+1 bits.
Residue weights/current input, ordering, query-generation and comparison
fields fit2^24n^2 bits. This is P's bounded verified-pair search, not
an exponential fiber table. Every generated gate descriptor is streamed.

Bit-serial schoolbook addition, multiplication, division and Euclid
reuseO(n^2) Boolean workspace: choose fixed templates below2^24n^2
bits, releasing temporaries instead of retaining histories. The rational
trigonometric table has fewer than2^20 bits. P's collective extraction
rounds stream outcomes into explicit counters, without an acquisition-
length transcript. The numerical label, signed sums, precision and
cap powers haveO(n)-bit intermediates within the same arithmetic region.
K<=2^16n decoder records each need a fixed multiple ofn bits;
scores, CRT residues and candidate scans are streamed. Even fixed
copies fit2^24n^2 bits. Remaining finite generator/address/allocator
subfamilies use these bounded arrays, not runtime-many records.
Thus2^32n^2 bits per listed regional subfamily collection suffice.
SinceU>=n^2,C=2^48 is a fixed conservative upper bound, chosen
from the stated analytic capacities. Canonical subranges are assigned
by fixed prefix sums of those capacities; no occupancy oracle is used.

The finite exhaustive branch uses the candidate, test and acquisition
counters, source/shift scratch and streamed bit arithmetic. It stores no
list of all candidates or outcomes and fits the same regional capacities
for every finite n, includingn=1. Field widths may be padded to a fixed
multiple of(n+1), still withinC*U. The finite code and all compile steps
are counted. No correctness event is used for these allocation bounds.
The greatest virtual classical slot plus one is therefore
 B=7C*U=O(n^2), independently of the number of retries or allocations.

Similarly reserve fixed virtual QUANTUM pools for P's at mostn
pending source-phase qubits, current original index/query registers,
collective translation/extraction, source transforms and rank/comparison/
reset helpers. Their maximum slot plus one is bounded by
H=2^32*2^r_addr=O(n). Each original combiner usesO(r_i+n)=O(n)
scratch; extraction and transforms useO(n) more, with fixed simultaneous
copies covered byH. Reuse fixed slots after every discard/release.
Pool metadata stays in the counted classical regions. Original quantum
addresses are canonical pool offsets, not lifetime allocation numbers.
Thus maximum slot range, not only live occupancy, is bounded.

## 4. Physical bank, access and executed operations

Store virtual classical bit i as the basis value of physical wire2i.
Store virtual quantum wireq at wire2(q+1)+1; reserve wire1 for a fair bit.
Maintain one allocated paired prefix0,...,2h-1, initiallyh=2. Before
accessingi>=h orq+1>=h doubleh until the slot fits, appending and
initializing every new wire. Old indices/states remain fixed. Never
shrink the prefix duringP. Every unused padding wire counts inS_Q.
The maximumh is below2max(2,B,H+1), so the entire prefix isO(n^2).
No per-bit key, active flag or translation directory is added. P's own
allocator metadata remains in its counted virtual regions.

READ(i) measures known wire2i inZ into a reusable classical bit.
WRITE(i,b) reads oldz, appliesX exactly whenz differs fromb, then
clears the temporaryz after its last use. Reset isWRITE(i,0).
Read before writing operands, including aliased fields, inP's exact
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

P's known-weight membership circuits and at-most64-solution
exclusion circuits are generated by their original classical serial
loops. For each known weight/string bit READ its stored basis value
and emit the same controlled gates on the ORIGINAL quantum query/
equality/scratch registers. A superposed original query index never
becomes a bank wire address. No child construction or source request
is inserted into a Grover oracle. Every original coherent control and
phase is retained with only classically selected bank reads.
Every gate/operand descriptor is generated/decoded through the same bit
interface. Fixed Toffoli operations expand to exact Clifford+T words;
no uncounted circuit compiler or stored exponential instruction list.

Execute everyP gate, measurement, coin, reset, discard, source request,
guard, failure and retry at its specified virtual position. Stage a
measurement result only until it is streamed to its virtual field;
there is no growing classical measurement transcript. A fresh fair bit
usesH andZ on reserved wire1, writes it asP requests and resets it.
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
AfterP terminates, stream its final residue to the countedO(n)-bit
classical output FIRST; only then clear/release the entire prefix and
short fields, retaining that output. All cleanup work is counted.

## 5. Exact classical-quantum invariant

At aligned virtual steps the joint state, including arbitrary referenceR,
has the form
 sum_(c,z) p(c,z) |z><z|_controller tensor |c><c|_bank
                   tensor rho_(c,z)_(mapped P registers,R).
Herez contains finite control and the cleared/staged short fields, and
c is precisely
P's current classical record, not a coherent unknown memory string.
The bank and live registers may be correlated; a stored measured label
can be correlated with a still-coherent phase/query register. No product
or independence assumption between these systems is needed.

Initialization gives the invariant. For READ of biti, projectors onto
c_i=b leave the nonselective CQ state unchanged. Keeping the outcome
only appends the virtual bit on each conditional record; rho_c is
unchanged. WRITE produces precisely the updated basis string. When
records merge after an irreversible overwrite, their conditional states
mix exactly as classical forgetting requires. Boolean steps and pointer
moves update the finite control identically. Original gates haveP's
same conditional action; original measurements and coins have the same
instruments and updatec. Reset/discard has Section4's channel identity.
Each fresh ideal request supplies the same independentrho_s. Induction
therefore preservesP's complete reduced state and classical history at
every virtual step, including failed extraction labels, search failures,
partial children, rejected samples and abort cleanup.

This is not a claim that reading an arbitrary superposed bank is harmless.
Only the reachable CQ representation is used. Extra bank outcomes are
deterministic givenP's classical record. The unconditional full output
law and actual source-request sequence are exactlyP's. In particular,
virtual.md's complete argument establishes full-secret success at least
1-2^-8 for everyN,s. No favorable-event conditioning, acceptance oracle,
source reflection, inaccessible purification or unknown-state cloning.
The argument covers ideal independent source copies only. Under a
different adaptive corruption model extra bank measurements might be
visible to a supplier and change future behavior; no such transfer is
claimed. The exact canonical clean-model text and fraction0 are unchanged.

## 6. All physical space and fully charged time

InputN, final output and a fixed number ofO(n)-bit staged operands use
O(n) physical classical bits. Address/scan fields haveO(logn) bits;
finite code has constant size. Every other classical label, loop/call
context, counter, arithmetic field, generator descriptor and allocator
record is in the counted bank. No separate physical classical stack,
large address map or duplicate measurement transcript is retained.
Thus physicalS_C=O(n) on every branch.

The full paired prefix, unused padding, bank values, all virtual metadata,
original quantum slots, fair-bit scratch and temporary source wires use
O(n^2) allocated qubits by Sections3-4. Basis-state storage does not
remove those wires from the total memory used for address fees. This
provesS_Q=O(n^2) jointly, including initialization, failure and cleanup.
All indices haveO(logn) bits because the MAXIMUM reserved ranges are
polynomial, not because we assume a small observed occupancy.

Use a conservative fixed polynomial overhead per charged virtual step.
A bank access can scanB=O(n^2) slots, decoding full address fields and
charging every comparison, measured bit, conditionalX/reset and physical
address. A fixed number ofO(logn)-bit operands per instruction is decoded
through bit loops. Even a whole-region initialization by separate full
scans for itsO(B) bits costsO(B^2 polylogn). Original variable-width
operations are first expanded into their charged bit steps. Prefix
expansions append a totalO(n^2) wires; output-first final cleanup also
has polynomial work. Source moves costO(n) gates plus addresses on top
of the mandatoryn+1 source charge. TakingO(n^8) per charged virtual
step generously covers these finite loops for n>=2, and initialization/
cleanup contribute a polynomial of the same kind. Hence on EVERY branch
 T_physical<=poly(n)*(T_P+n^2).
This separately counts all added work; P's original source/weighted-work guards
remain checked at exactly their own positions. Additional simulator work
is not hidden behind a nominal old guard or an expected-time estimate.

We do NOT multiply P's final pure exponential and silently discard
the compiler polynomial. PutL=log2n andE=n/(2L)-4n/L^2. The
COMPLETE virtual9 proves T_P=O(n^3 L^3 2^R), with explicit source
work2^(O(L^2)), decoder work2^(R/8+O(L^2)), and a uniform
gapE-R>=n/(8L^2) for the stated sufficient rangeL>=2^18.
That gap dominates EVERY fixedaL+b log2L, so it also absorbs
the additional polynomial bank/compiler factor. Source/decoder work
remains exponentially below2^E after that same polynomial factor.
Initialization/cleanup and preprocessing are polynomial and fit too.
Hence T_physical=O(2^E) on EVERY branch. The unchanged finite
program and simulator operate at every remaining length; their finite
maximum ratio to the positive envelope changes only one absolute
outside constant. The n=1 case is finite; the logarithmic display
describes n>=2. No new runtime threshold, oracle or postselection
is introduced for this estimate. P's original weighted work counter
still counts only its original weights; all added simulator work was
separately charged, not hidden behind that counter.

Exactly one physical source request executes each virtual request,
with no others. Fresh bank/padding zero qubits are not DCP copies;
their preparation is counted work/storage. Thus Q_physical=Q_P
on the coupled run, including all rejects, failed attempts and aborts.
The exact full cap in P's virtual8 and the coefficient certificate
in virtual9 proveQ=O(2^((log2n)^2)), with the same absolute outside
constants. No replacement of that quasipolynomial bound by a polynomial
is made. Every original partial/zero-width tree target is handled by
P's reproduced verified-pair/shortcut rules, not a foreign finishing
arity comparison. Full signed-label outputs, both all-modulus decoders
and the complete failure budget are preserved by the CQ coupling.

## 7. Complete binding, indices and limits

All five current physical claims cite this file and the full virtual.md.
Every source/probability/decoder proof is reproduced; no parent JSON or
historical verdict supplies a theorem. This main and its layout define
one physical implementation. VirtualP's quadratic classical/linear
quantum declarations are explicitly scoped to virtual memory and are
not combined with the new physical bounds.

The time envelope has exact growth index1 because its logarithm is
n/(2L)-4n/L^2, withL=log2n. Source2^(L^2) is quasipolynomial,
not polynomial, and has index0. The two polynomial spaces have index0.
Error expression0 has the identical independent-ideal-copy model.
These are upper-envelope indices, not lower bounds. The storage method
is prior work; this is its application to the published log-log-band
configuration with a distinct physical memory tradeoff. No optimality,
priority, practical speed, positive robustness or cube-root time claim.
