# LLV-GBANK: linear classical space for the low-source two-entry sieve

## 0. One physical algorithm and joint guarantee

For everyN>=2 ands inZ/NZ putn=ceil(log2N). The single physical
LLV-GBANK interpreter below recovers the whole secret with unconditional
probability at least1-2^-8 from independent ideal source copies. On EVERY
actual execution branch, including errors, failures, discards and cleanup,

 T=O(2^((1/2)sqrt nlog2n+2sqrt n(log2n)^(1/4))),
 S_C=O(n) classical bits, S_Q=O(n^2) allocated qubits,
 Q=O(2^((1/2)sqrt n)) acquired copies.

All outside constants are absolute. Exact indices are[1/2,0,0,1/2];
only time scores[1/2]. Fractional tolerance is0 under the exact model

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

The bank's basis-state qubits and all padding count inS_Q. They are not
free classical storage or omitted quantum memory. This physical machine
trades the virtual machine's quadratic classical/linear quantum allocation
for linear classical/quadratic quantum allocation. The source and complete
output law are preserved. No positive robustness, practical speed,
optimality, priority or cube-root time is claimed.

## 1. Actual direct sources and complete virtual program

The virtual programP is exactly the complete LLV-GBR200 algorithm in
virtual.md. Its original proof body is reproduced without mathematical
changes, SHA-25674f2883577a0a8bd7d9e5c8e7ccf4a69f3e1a5fd8c90d96debdb79e5e09e4b7b.
The added scope header applies to EVERY assertion in that file: its
S_C=O(n^2),S_Q=O(n) statements concern virtualP, not physical LLV-GBANK.
All source-only primitives, fresh-label laws, phase/failure arguments,
all-modulus decoders, finite branch, guards and unconditional probability
proof are supplied there. No prior review is a mathematical premise.
There is only one selected virtual configuration, not a mixture of
resource guarantees from different profiles.

Two direct published storage-method sources were read and used:
PSG21,9fdfdb12-834d-441c-8bb1-717ab380abf3, commit
05f0ab81b2cc641c7a917ed56dffb3204688e795, full proof SHA-256
43e2ac8f392a5301733dbb393088588641b06c3345864d83002f123a6de3830f;
and GordoAR's PSG2-QSTORE,2b2b0036-7bbc-4ce5-80a8-b8928f0ce120,
commitf0d457ecfdbb761f5a602ee0fb52f0d1e4ea1d30, main proof SHA-256
92b96a0fee5eb35ec700ef6449ec16c8cd05c806f0fe7cab980576099ccc776a,
complete transfer SHA-256
5c44c9268e55edf7bc55277ef244e97d9730dd1f09f1e13fa3746a54d34a5325.
PSG21 supplies the measured-basis interpreter, read/write, CQ-history
coupling, clean-model limitation and explicit overhead methodology.
PSG2-QSTORE supplies the distinct direct stable wire map and fixed-region
maximum-address proof without per-bit keys or flags. Its proof also credits
PSG21 for the common method; that shared route is acknowledged here.
Both were actual direct reads and material sources. The generic storage
idea is not new. Their exact published files match official evidence;
provisional graph declarations are not certified ancestry.
Neither PSG21's parent.md nor Dense's six virtual proofs/algorithm are
imported. Their time/profile/sample constants are not used. All old
LLV-GBR200 upstream acknowledgments remain in virtual.md. Public source
mappings and both-endpoint citations appear in the declaration.

## 2. The selected virtual instruction stream

Run preciselyP's public parameter rule and its full source/test/merge/
decoder/guard schedule. On the main branch, as fixed in virtual.md,
v=floor sqrt n,ell=ceil log2n,ell2=ceil log2ell,
D=ell+2ell2+4,m=floor((v-256ell)/D),
kappa=ceil log2(m+2)+3,lambda=1,
A_bar=ceil((n+m*kappa)/m)+2,
center=ceil(ell*(m-1)/2),fan_i=A_bar+ell*i-center.
There are two labels per phase table. The exact capacity prefix, final
arityk=R+kappa+1(includingR=0), source/leaf caps, all FIND schedules
and both decoders remain preciselyP's. The finite exhaustive branch
n<2^4096 is the same virtual branch, not a new success-conditioned run.

Fix ordinary uniform bit implementations of the stated arithmetic and
arrays: finite Boolean code, bit reads/writes, explicit integer loops,
constant-arity exact Clifford+T gates, computational measurements,
reset/release, fair coins and source requests. Ripple/bit-serial schoolbook
arithmetic suffices; long numbers are bit fields, not unit-cost words.
The original serial table and tuple-exclusion loops are retained. Any
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
1. Retained two-label vector/node pool, root labels, free/pointer metadata.
2. Recursion frames, return contexts, loop state and saved counters.
3. Current residue, sorting, tuple-list, rank and search-control arrays.
4. Source/LE/transform fields and schoolbook arithmetic scratch.
5. Decoder records, residues, CRT/score fields and streamed candidates.
6. Remaining reusable generator, allocator, instruction and control scratch.

Allocate each array its analytic upper row count and fixed field width;
reuse its same cells after release. For retained vectors use a bounded
pool or per-level child slots, with free/vector references stored inside
these regions. A retry reuses those slots, not a newly minted permanent
address. Stack frames use depth indices at mostm+1. There is only one
current tuple list. Decoder batches reuse one record region. No circuit
or instruction history accumulates with execution time. Each classical
address and pointer uses these region/subrange offsets; there is no
sparse-name dictionary outside the bank.

Here are conservative analytic capacity bounds establishing the selected
fixed constants for every reachable branch, including wrong LE labels.
From virtual8, m<=sqrt(n)/log2n<=n,kappa<=ell,fan_max<=n and
sum_i fan_i<=n+m*kappa+3m<=5n on the main branch. Also
K=2^13(2ceil sqrt n+ell+30)<=2^15ceil sqrt n<=2^16n.
The number of retained vector/root slots is bounded by a fixed multiple
ofsum_i fan_i+fan_max+K+1. Each has two3n-bit labels, plusO(logn)
indices; a bound2^24n^2 covers this pool, metadata and fixed copies.
For a literal pool choice reserve2^17n vector slots of16n bits each,
including labels, free bits and bounded references; the stated counts
fit that2^21n^2-bit subrange. Releasing a vector returns its same slot.
A frame has a fixed number of n-bit-or-shorter fields; at mostm+1
frames, profile and return records fit2^20n^2 slots. Counter widths
need only a fixed multiple ofn: log2Qcap<=sqrt n/2 on the main branch,
label fields are3n bits, all indices/widths fitO(logn), and FIND loop
counters have at mostfan_max+O(logn)<=O(n) bits.

Forlambda=1,Cp=2^(kappa+2)+1<64(m+2)+1<=193n(main).
Each tuple hasU_query<=fan_max<=n bits. A fixed number of tuple,
rank, residue, ordering and input-array copies therefore fit2^24n^2
slots. Their maximum rows and all stored lengths/pointers are included.
Bit-serial schoolbook additions, multiplication, division and Euclid
can reuseO(n^2) Boolean workspace; choose fixed templates below
2^24n^2 bits rather than store their history. LE hasO(n) classical
scratch; its tests stream counts, notF recorded outcomes. The finite
trigonometric table has fewer than2^20 bits. Cap powers haveO(n)-bit
intermediates and use this same reusable arithmetic region.
DecoderK records each use at most a fixed multiple ofn bits; scores,
residues and current-candidate arithmetic are streamed. Even fixed copies
of all these records fit2^24n^2 bits. The remaining fixed instruction,
address, allocator and scratch subfamilies use the same bounded arrays,
not a number of records proportional to runtime. Thus reserving2^32n^2
bits per listed region/subfamily collection is already sufficient.
SinceU>=n^2,C=2^48 is a fixed conservative bound, not a constant chosen
from a history or an unknown runtime search. Fixed subrange bases may be
assigned by prefix sums of these stated analytic capacities.

The finite exhaustive branch uses the candidate, test and acquisition
counters, source/shift scratch and streamed bit arithmetic. It stores no
list of all candidates or outcomes and fits the same regional capacities
for every finite n, includingn=1. Field widths may be padded to a fixed
multiple of(n+1), still withinC*U. The finite code and all compile steps
are counted. No correctness event is used for these allocation bounds.
The greatest virtual classical slot plus one is therefore
 B=7C*U=O(n^2), independently of the number of retries or allocations.

Similarly reserve bounded virtual QUANTUM pools for retained phases/roots,
current original indices and fresh search scratch, source/LE/transforms,
rank and comparison/reset helpers. Their total maximum slot plus one is
bounded byH=2^32*2^r_addr=O(n). Indeed virtual14 bounds pending siblings
bysum_i fan_i and current query/residue scratch byO(fan_max)<=O(n);
K<=2^16n root qubits andO(n) source/helper qubits fit this fixedH.
Reuse pool slots after each discard/release. The pool's bitmap, free-list
or head indices are virtual classical data above. Original quantum
addresses are canonical pool offsets, not lifetime allocation numbers.
This establishes a maximum quantum slot range, as well as live occupancy.

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

P's original coherent table lookups are implemented by their existing
SERIAL row scans. For each known row and bit, READ its stored classical
value and generate the same controlled gate on the original quantum
index/equality/scratch registers. A superposed original table index never
becomes a bank wire address. This retains every coherent control and
phase exactly, while using only classically chosen bank reads.
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
This separately counts all added work; P's original source/leaf guards
remain checked at exactly their own positions. Additional simulator work
is not hidden behind a nominal old guard or an expected-time estimate.

We do NOT multiplyP's final pure exponential and silently drop the
polynomial. Virtual14 proves the sharper internal estimate, uniformly
withx=sqrt n,L=log2n,
 log2(T_P/C)<=xL/2+xlog2L+O(x)+O(L^2).
The extra polynomial simulation factor addsO(L), so the SAME bound
with adjusted absolute constants holds forT_physical. Since
log2L=o(L^(1/4)) andL^2=o(xL^(1/4)), it follows eventually that
 log2(T_physical/C')<=xL/2+2xL^(1/4).
The strict eventual gap absorbs every fixed polynomial bank/compiler/
addressing cost. The identical capped program and simulator run at the
remaining finite lengths; their finite maximum ratio to the positive
envelope changes only one absolute outside constant. This includesn=1
and the entire explicit finite branch. No postselected fast branch or
new runtime threshold is substituted.

Exactly one physical source request executes each virtual source request,
with no others. Fresh zero bank/padding qubits are not DCP copies; their
preparation was counted above. Therefore actualQ_physical=Q_P on the
coupled run, including all rejects, failed children and aborts. The
literal main guardQcap<=2^(sqrt n/2) and the finite branch's outside
constant giveQ=O(2^((1/2)sqrt n)).

## 7. Complete binding, indices and limits

All five current physical claims cite this file and the full virtual.md.
Every source/probability/decoder proof is reproduced; no parent JSON or
historical verdict supplies a theorem. This main and its layout define
one physical implementation. VirtualP's quadratic classical/linear
quantum declarations are explicitly scoped to virtual memory and are
not combined with the new physical bounds.

The time envelope's exact growth index is1/2, as its leading logarithm
is(1/2)sqrt nlog2n. Source2^((1/2)sqrt n) has index1/2; spacesn,n^2
have index0. Error expression0 has the identical independent-ideal-copy
model. These are upper-envelope indices, not matching lower bounds.
The storage transformation and its generic method are prior work; this
application to the low-source profile is a new resource configuration.
No priority, generic novelty, practical performance, positive robustness,
optimality or cube-root time is claimed.
