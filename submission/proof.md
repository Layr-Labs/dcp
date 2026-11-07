# LLV-GBANK300C: linear classical space for the low-source extended-table sieve

## 0. One physical algorithm and joint guarantee

For everyN>=2 ands inZ/NZ putn=ceil(log2N). The single physical
LLV-GBANK300C interpreter below recovers the entire secret with unconditional
probability at least1-2^-8 from independent ideal copies. On EVERY actual
branch, including failed attempts, discarded sources and cleanup,
 T=O(2^((1/2)sqrt nlog2n+(1/4)sqrt n+2sqrt n(log2n)^(-1/2))), S_C=O(n) classical bits,
 S_Q=O(n^3/log2n) allocated qubits,
 Q=O(2^((1/2)sqrt n)) acquired DCP copies.
All outside constants are absolute. The displayed asymptotic representatives
apply forn>=2; the same finite virtual branch and simulator covern=1.
Exact indices are[1/2,0,0,1/2]; only time scores[1/2]. Fractional tolerance
is0 under the exact model

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

All basis-bank qubits, unused padding, original coherent registers,
metadata and source-moving scratch count in physicalS_Q. The virtual
program's polynomial classical/linear quantum allocation is replaced by
this one physical linear-classical implementation. This is a storage/time
tradeoff, not a dominance or optimality claim. No positive robustness,
practical timing, generic simulation novelty, priority or cube-root growth.

## 1. Actual direct source and complete virtual evidence

The actual complete direct source is LLV-GBANK300, physical proof
SHA-256ad0e443b5937a00d5ebac641845b4481bd2b825f38a0699c8e27ed49ab95c790,
and full scoped virtual proof SHA-256
71adc12b2de7b327638f150378eb96c44edc435626492b2951321e7de7f130d2.
It supplies BOTH the complete selected full-log virtual algorithm and
its fixed-region measured-bank/CQ/source/overhead method. The complete
virtual body remains byte-identical to its included LLV-GFL300 source,
SHA-2568867fd3c02c4220ec35844b8abf505318befb291259da60d0d4b03c707b4087f,
with only the explicit virtual-only scope header identifying our current
physical interpreter. Every primitive, phase/failure law, exact profile,
cap, finishing call, decoder, finite branch and probability proof is
included. No ancestor JSON, opaque theorem or prior verdict is a premise.

The direct source's LLV-GFL300 and LLV-GBANK use routes, and all
inherited upstream credits, remain. Its bank credits PSG21,
9fdfdb12-834d-441c-8bb1-717ab380abf3, full proof
43e2ac8f392a5301733dbb393088588641b06c3345864d83002f123a6de3830f,
and GordoAR PSG2-QSTORE,2b2b0036-7bbc-4ce5-80a8-b8928f0ce120,
main92b96a0fee5eb35ec700ef6449ec16c8cd05c806f0fe7cab980576099ccc776a,
transfer5c44c9268e55edf7bc55277ef244e97d9730dd1f09f1e13fa3746a54d34a5325.
No distinct additional peer profile or Dense/PSG21-parent algorithm is
imported. The actual direct public source identity and both source/
dependent citation endpoints accompany the declaration. Pending links
are not verified ancestry and no generic bank novelty is asserted.

The NEW physical backing layout reserves full E-label slots according
to the exact retained-vector count and puts completed two-label roots
in a separate pool. It replaces the old n-slot/E-padded reservation,
not merely a reported allocation total. Fixed region capacities, bases,
field locators and the entire counted prefix all change accordingly.
The logical program, output law, source sequence and guards stay V's.
Its coarse virtual classical n^3 declaration remains valid and scoped
virtual-only; our independently proved packing yields the smaller
physical quantum bound. All changed layout inequalities are below.

## 2. Selected virtual configuration and uniform instruction stream

Execute exactlyV's public parameter, source/test/merge/decoder and guard
schedule. On the main branchn>=2^4096, letv=floor sqrt n,
ell=ceil log2n, and compute
lambda=ell,P_prec=ell^2,H_n=bit_length(n^P_prec-1),
m=floor(P_prec*(v-256ell)/(H_n+ell)),
kappa=ceil log2(m+2)+3,A_bar=ceil((n+m*kappa)/(m*lambda))+2,
center=ceil((m-1)/2),fan_i=A_bar+i-center.
P_prec is the scalar precision calledP in the virtual proof; it is not
our virtual-program symbolV.
Full leveli hasfan_i inputs, width(fan_i-1)lambda-kappa and output
log lengthlambda. Exact prefix capacity selectsu full levels and the
lastk=ceil((R+kappa+1)/lambda)-input, widthR, one-qubit-output merge.
Every actual partial arity and zero remainder is handled exactly as the
full virtual proof specifies. Source/leaf caps, FIND trials, failures,
decoders and the explicit finite branch remainV's, not the bank parent's.

A full phase table has E=2^lambda labels; a completed final root has
only two. The actual compact backing store keeps those two cases in
SEPARATE pools, without padding final roots to E. Public array lengths
and every index/gate schedule are unchanged. The capacities below also
cover the unchanged finite branch.
All virtual operations have ordinary finite uniform bit implementations:
Boolean logic, reads/writes, explicit loops, Clifford+T gates, computational
measurement, reset/release, fair coins and source requests. Ripple and
schoolbook bit arithmetic suffice. Long numbers and bulk operations are
expanded into counted bit steps, not unit-cost words.
Every call/return context, generator cursor, loop counter and allocator
record is virtual data. A fixed finite controller generates/consumes one
instruction at a time; no exponential code or advice is preloaded. All
addresses use the bounded canonical regions below. Numerical counters may
haveO(n) bits without making their bit-cell addresses exponential.

## 3. Compact fixed regions and maximum address spans

Defineell_bank=max(1,ceil log2n),E=2^ell_bank,
J_bank=max(1,ceil(E/ell_bank)),r_addr=ceil(log2(n+2)),
U=2^(2r_addr),C=2^48,W=C*U*J_bank.
On the main branch ell_bank=lambda=ell, E<=2n and E>=ell.
ThereforeJ_bank<=2E/ell, and W=O(n^2E/ell). Reserve seven
classical-virtual regions of W bit slots at bases tW, in this order:
0 input/parameters/profile/caps/precision/constants;
1 retained full-vector and SEPARATE final-root pools with their metadata;
2 frames, return contexts and loops;
3 current tuples/residues/rank/search data;
4 source/LE/transforms/schoolbook arithmetic;
5 decoder records, scores/residues/CRT and streamed candidate;
6 reusable generator, allocator and remaining control scratch.
Every subfamily has a fixed padded subrange with public row/field
locators. All subrange bases are prefix sums of analytic capacities
below. Every released/retried object reuses the SAME slots. No lifetime
name, sparse key directory or instruction history accumulates.

This is an actual replacement backing layout for V's logical records.
Array indices, labels, outcomes and logical references have the same
values and meaning; field locators translate them to the new fixed
subranges with charged bit arithmetic. The virtual proof specifies a
uniform array/bit program, not a requirement to keep the old bank's
oversized physical padding. Generate one logical operation and its
field address at a time. All translating cursor/allocator metadata is
bank data. No duplicate classical map or coherent bank address is added.
Thus instruction-by-instruction logical semantics is unchanged while
physical addresses and maximum allocated range are genuinely smaller.

Here are analytic capacities on EVERY history, including wrong labels.
The complete virtual proof givesm=O(sqrt n/logn), and its exact ceilings
implylambda*sum_i fan_i<=8n. Alsofan_max<=9sqrt n/8<=n/ell
atn>=2^4096, andm<=n/ell. Pending full-output vectors consist of
at most a fixed number of sum_i fan_i+fan_max+m+1 slots: retained
siblings, a current node/leaf and the unfinished final merge's inputs.
Completed batch roots have output log1 and are NOT full vectors.
Consequently a fixed pool of 2^20*ceil(n/ell) FULL slots covers all
such simultaneous objects. Give each full slot16nE bits, including
its E labels of3n bits, ownership, free and pointer/header fields.
Sinceceil(n/ell)<=2n/ell, this pool uses at most2^25 n^2E/ell bits.
Every current output uses the same pool before its input slots are
returned; the constant covers that overlap. Source/leaf construction
uses at most one current full-output record in addition to siblings.

Put completed two-label root records in a SEPARATE 2^17n-slot pool
with16n bits per slot, including all ownership/free metadata. This
uses2^21n^2 bits. K<=2^16n by the complete virtual decoder bound,
so the pool covers all roots plus staging even on failed/aborted runs.
It introduces no E multiplier. Both sorts of node keep their actual
index-register size, lambda or1. The existing phase instruments and
rank/projection gates use their original public logical lengths.
Labels remain full3n-bit fields; neither compression nor a secret-
dependent assumption is used. Logical qubits are reset only when V
actually releases their final owner, not when a reference is moved.

Frames/profile/return state are at mostm+1 fixed templates ofO(n) bits,
covered by2^20n^2 bits. Caps and source/search counters haveO(n)-bit
fields. Main precision powers haveO(ell^3)<=O(n)-bit lengths.
For the current full OR partial MERGEF,
 Cp<=2^(lambda+kappa+1)+1<32E(m+2)+1.
The exact main bounds give m+2<=2sqrt n/L, L=log2n, and query length
U_query=fan_max*lambda<=2sqrt n L. Hence the SINGLE current tuple
list, its sort/rank/residue/exclusion records and fixed scratch copies
fit2^24 nE bits, including the cases Cp exceeds the domain or fiber.
Tuple records haveO(U_query+logCp) bits, not an extra n-bit label
per possible subset; labels stay in the separately counted input/output
tables. Input/sort/residue tables have at mostfan_max*E rows withO(n)
fields, so reserve the integer capacity2^24*n*r*E bits, where
r=ceil sqrt n is already computed by V. Since2ell<=sqrt n and
r<=2sqrt n on the main branch, both collections fit2^24 n^2E/ell
bits. All capacity formulas used by the actual compiler are integers
formed from n,r,ell,E,m,fan_max and their exact public ceilings;
fractional powers here are analytic bounds, not size-computation oracles. No full fiber,
subset list, recursion tree or generated circuit is stored.

The complete source/LE/decoder/schoolbook/control ledger fits a fixed
multiple ofn^2 bits, includingO(ell^3)-bit precision intermediates,
streamed candidates, fixed finite trigonometric table and constant
scratch copies. Cover each of these finite collections by2^32n^2
bits plus the absolute2^20-bit table. Logical quantum pool allocation
uses a counted bitmap/free scan, bank-resident ordered cell-ID lists,
heads and metadata ofO(nlogn) bits plus a linear bitmap. Those fit
the same collections. BecauseJ_bank>=1 andJ_bank>=E/ell, all the
listed subfamilies and their fixed copies fit2^40n^2J_bank bits per
region collection, below C*U*J_bank sinceU>=n^2.

The finite branch keeps candidates/test/acquisition fields, source/shift
scratch and streamed arithmetic, not all outcomes/candidates. Padded
O(n+1)-bit fields and fixed templates fit2^40n^2+2^20 bits, within
the same W even for n=1. It does not allocate main-profile table pools
that its exhaustive program never uses. All public size computations,
initialization, code generation and cleanup are charged. Thus the
MAXIMUM classical-virtual slot plus one on every branch is
 B=7C*U*J_bank=O(n^2E/ell) asymptotically,
not merely the number of observed live bits. Small finite lengths
change only the absolute outside constant.

The original quantum program still uses a compact pool with maximum
slot plus oneH=2^32*2^r_addr=O(n), including siblings/roots, current
query/rank/residue scratch and source/LE helpers. Allocate individual
free cells, with all bitmap/ordered-ID lists in the counted bank.
Stream one known ID into the controller for each gate or source SWAP,
never an entire n-entry classical map. No contiguous-block assumption,
lifetime cell ID or uncounted address history is introduced. Reset a
released cell by Section4's correct channel before reuse. The full
paired prefix counts all padding; B dominates H. Complete addresses
areO(logn) bits by these maximum fixed spans.

## 4. Physical bank, access and executed operations

Store virtual classical bit i as the basis value of physical wire2i.
Store virtual quantum wireq at wire2(q+1)+1; reserve wire1 for a fair bit.
Maintain one allocated paired prefix0,...,2h-1, initiallyh=2. Before
accessingi>=h orq+1>=h doubleh until the slot fits, appending and
initializing every new wire. Old indices/states remain fixed. Never
shrink the prefix duringV. Every unused padding wire counts inS_Q.
The maximumh is below2max(2,B,H+1), so the entire prefix isO(n^2J_bank).
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

## 6. Complete physical resources for the one simulation

The counted classical inputN, final output and a fixed number ofO(n)-bit
staged operands useO(n) bits. Address/scan/head fields haveO(logn) bits;
finite code has constant size. Every other label, loop/call/return context,
arithmetic field, cap counter, instruction descriptor and allocator record
resides in the counted bank. There is no physical classical recursion stack,
large address map, duplicate record or growing measurement transcript.
Therefore physicalS_C=O(n) on EVERY branch.

The full paired prefix hasO(B+H)=O(n^2J_bank) allocated qubits, including its
unused padding, all virtual data/metadata, original coherent registers,
coin scratch and growth overlap. Temporary source wires addO(n). Because
E=O(n),J_bank=O(E/ell),ell=Theta(log2n), this proves
 S_Q=O(n^3/log2n).
Basis-state wires are counted qubits and still contribute to the full
address fee. The proof uses maximum reserved ranges and slot reuse, not
success-conditioned or small observed occupancy.

All added work is charged separately. WithE<=2n,J_bank<=E, B=O(n^3) andH=O(n),
a full bank scan costs polynomial work, with full bit/address/operand
field decoding. Even initializing/clearing an entire region by one full
scan per cell costsO(B^2 polylogn). Original variable-length operations
are first expanded into bit steps. Original gates keep every coherent
control; source-register SWAPs costO(n) gates plus addresses per request,
on top of the originaln+1 source charge. The sum of all prefix growth,
initialization, output-first readout and whole-prefix cleanup is polynomial.
A conservativeO(n^12) factor per charged virtual primitive covers these
finite bit loops, full scans, bulk region operations and gate decoding.
Hence on every branch
 T_physical<=poly(n)*(T_V+n^2J_bank).
Virtual source/leaf guards are checked at exactly their original points.
Added simulator work is not deleted, hidden behind a nominal old guard,
or replaced by an expected-time estimate.

Do NOT drop the simulation polynomial from a final pure exponential.
Virtual14 proves, uniformly withx=sqrt n,L=log2n,
 log2(T_V/C)<=xL/2+x/4+O(x/L)+O(L^2).
The added polynomial bank factor contributesO(L). Sincex/L andL^2
are both o(xL^(-1/2)), the same strict eventual gap establishes
 log2(T_physical/C')<=xL/2+x/4+2xL^(-1/2).
The SAME capped program and interpreter run at earlier lengths; the fixed
finite prefix changes only one absolute outside constant. No selected fast
branch, new runtime threshold or postselection is introduced.

There is exactly one physical DCP acquisition per virtual acquisition and
no other source request. Fresh local zero bank/padding qubits are charged
work and quantum allocation, not DCP copies. Every rejection, failed child,
discarded source and abort therefore has exactlyV's actual source sequence.
Its main guardQcap<=2^(sqrt n/2) and the finite outside constant give
 Q=O(2^((1/2)sqrt n)).
The exact CQ/channel argument in Section5 transfersV's full output law,
so the complete virtual proof establishes unconditional full-secret success
at least1-2^-8 for everyN,s jointly with all these resources. The error
expression0 and identical independent-ideal-copy model are unchanged.

## 7. Complete binding, indices and tradeoff

All five current claims cite this physical main and the complete scoped
virtual.md. Every needed source, phase/failure, cap and decoder proof is
included; no parent JSON, historical verdict or unavailable compiler is a
premise. The virtual n^(3) classical/linear quantum declarations
are explicitly virtual-only and are not combined with different physical
allocations. This main defines one physical interpreter with counted
S_C=n andS_Q=n^3/log2n envelopes.

The exact time-envelope growth index is1/2. Source2^((1/2)sqrt n) has
index1/2; both polynomial space envelopes have index0. Only time is the
numeric objective. These are upper-envelope indices, not runtime lower
bounds. The bank method is credited prior work. The larger physical quantum
space buys linear classical memory atV's full time/source envelopes; it
strictly saves a logarithmic quantum-space factor relative to the direct
source, with the same other envelopes. This follows from the changed
maximum reservation and root/full packing, not an omitted padding charge.
No optimality or generic novelty is claimed.
No positive robustness, priority, practical speed or cube-root time.

