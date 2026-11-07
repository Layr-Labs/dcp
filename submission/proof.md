# LLV-GBANK300: linear classical space for the low-source extended-table sieve

## 0. One physical algorithm and joint guarantee

For everyN>=2 ands inZ/NZ putn=ceil(log2N). The single physical
LLV-GBANK300 interpreter below recovers the entire secret with unconditional
probability at least1-2^-8 from independent ideal copies. On EVERY actual
branch, including failed attempts, discarded sources and cleanup,
 T=O(2^((1/2)sqrt nlog2n+(1/4)sqrt n+2sqrt n(log2n)^(-1/2))), S_C=O(n) classical bits,
 S_Q=O(n^(3)) allocated qubits,
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

## 1. Actual direct sources and full virtual evidence

The actual complete virtual programV is LLV-GFL300, reproduced in
virtual.md with an explicit VIRTUAL-ONLY scope header. Its entire source
body is byte-identical to the frozen direct proof SHA-256
8867fd3c02c4220ec35844b8abf505318befb291259da60d0d4b03c707b4087f.
All source-only primitives, label extraction, phase/failure instruments,
profile, exact source/leaf guards, all-modulus decoders, finite branch and
unconditional probability proof are present. Its old classical/quantum
statements describe VIRTUAL allocation, not this physical machine. No
old JSON or ancestor acceptance is used as a mathematical premise.

The actual direct storage-adapter source is LLV-GBANK, complete physical
proof SHA-256488ba20d6ea74838bc45716fd7358866089a8e35cd8a46df8eb75b70f2d04b4f.
It supplies fixed regions/maximal slot bounds, the direct stable wire map,
CQ read/write and forgetting proof, complete bit-level interpreter, clean
source-channel preservation and separately charged simulation overhead.
Those arguments are reproduced and adapted here toE-row tables. Its
different virtual LLV-GBR200 algorithm is not adopted. Our selectedV is
exactly the complete program in our own virtual.md.

The bank source fully credits PSG21,9fdfdb12-834d-441c-8bb1-717ab380abf3,
proof43e2ac8f392a5301733dbb393088588641b06c3345864d83002f123a6de3830f,
for the generic measured-basis/CQ/overhead method, and GordoAR's
PSG2-QSTORE,2b2b0036-7bbc-4ce5-80a8-b8928f0ce120,
main92b96a0fee5eb35ec700ef6449ec16c8cd05c806f0fe7cab980576099ccc776a,
transfer5c44c9268e55edf7bc55277ef244e97d9730dd1f09f1e13fa3746a54d34a5325,
for the direct fixed-layout/address-span refinement. Those acknowledgments
and all V's inherited source credits remain. No additional peer algorithm
or uncarried method is imported. In particular no PSG21 parent or Dense
virtual program/profile is used. Public mappings and both-endpoint citations
appear in the explicit declaration. Provisional references are not verified
ancestry, and no earlier verdict replaces a proof here.

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

A full phase table hasE=2^lambda labels; the last output has only two,
so padding it toE entries for storage is harmless and counted. The
physical capacity parameter below definesE for small finite lengths too.
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

## 3. Fixed padded regions and maximum address ranges

Defineell_bank=max(1,ceil log2n),lambda_bank=ell_bank,
E=2^lambda_bank. On the main branchlambda_bank=lambda exactly;
for the finite branch this is just public padding, not a new source profile.
ThusE>=2, E<=2n, andE=O(n^(1)).
Putr_addr=ceil(log2(n+2)),U=2^(2r_addr),C=2^48,W=C*U*E.
Reserve seven classical virtual regions, eachW bit slots, at bases tW:
0input/parameters/profile/caps/constants;
1retained label/vector pool and its metadata;
2frames/return contexts/loops;
3current residues/sort/tuple/rank/search data;
4source/LE/transforms/schoolbook arithmetic;
5decoder records/residues/CRT/scores/current candidate;
6remaining streamed generator, allocator and reusable control scratch.
Every fixed subfamily has a padded canonical subrange, with row/field
indices and reusable slots. Freed/retried vectors, frames and scratch use
the SAME addresses. No lifetime allocation number, sparse-name dictionary,
per-bit key or added per-bit active flag grows with runtime. All original
pool/free/pointer metadata is itself data in these regions.

Here are sufficient analytic capacities on EVERY main-branch history,
including wrong LE labels. The full virtual proof bounds
 m<=n,lambda*sum_i fan_i<=8n,fan_max*lambda<=n,
 K<=2^16n, kappa<=ell,2^kappa<16(m+2).
These follow from its exact capacity ceilings and uniform main parameters;
in particularm=O(sqrt n/logn),lambda<=ell and the terms m*kappa and
m*lambda areO(sqrt n). Hence the number of retained vectors/roots is
at most a fixed multiple ofsum_i fan_i+fan_max+K+1, covered by2^17n
vector slots. Give a slot16nE bits for itsE full3n-bit labels and
bounded references/free/header fields. This2^21n^2E-bit pool covers
all levels and roots; a final root actually uses only two labels.
Constant-size frame templates ofO(n) bits, at mostm+1 frames, and the
profile/return records fit2^20n^2 bits. Pointer bit widths areO(logn).

Every full OR final MERGEF has
 Cp<=2^(lambda+kappa+1)+1<32E(m+2)+1<=97nE,
and tuple/query lengthf*lambda<=n. Constant copies of its tuples,
rank, residue, ordering, input and sort records fit2^24n^2E bits.
Input tables and residue arrays have at mostfan_max*E rows andO(n)-bit
fields. Only one current tuple list exists. Labels remain in their full
3n-bit fields, not compressed or treated as secret advice.
Schoolbook integer arithmetic uses reusableO(n^2) Boolean scratch;
cap integers and source counters haveO(n)-bit fields. Main precision
powers haveO(n)-bit output length or less atn>=2^4096 (the fixed power
hasO(ell) bits and the growing powerO(ell^3), both<=O(n)). LE streams
its counters and usesO(n) scratch. The fixed rational trigonometric table
has fewer than2^20 bits. DecoderK records, scores/residues and streamed
candidate arithmetic fit2^24n^2 bits. No list of all decoder candidates
or generated gates is stored. Remaining fixed code/allocator/control
subfamilies use these same bounded arrays;2^40n^2E per region collection
is a sufficient conservative bound. Fixed subrange bases can be prefix
sums of those analytic capacities. SinceU>=n^2,C=2^48 is fixed and
sufficient, not chosen from an observed history or uncomputed maximum.

The finite exhaustive branch stores candidate/test/acquisition fields,
source/shift scratch and bit arithmetic, not all candidates or outcomes.
It fits the same capacities with paddedO(n+1)-bit fields, includingn=1.
Its code is finite and every setup/compile operation is charged.
Thus the MAXIMUM virtual classical slot plus one is
 B=7C*U*E=O(n^2E), independent of retries, not just live occupancy.

Give the original logical quantum registers a compact pool of cells with
maximum slot plus oneH=2^32*2^r_addr=O(n). The virtual proof bounds all
simultaneously live phases/siblings, roots, query and source/LE/rank scratch
by a fixed multiple ofn, below thisH. Allocate individual free cells,
not necessarily contiguous blocks. An ordered register stores its cell-ID
list in the bank; indexed Clifford+T gates on those known cells implement
its logical bit order. A bitmap/free scan and those ID lists, including
all heads and source-register maps, are counted virtual bank metadata.
TheirO(nlogn) live information and fixed pool bitmap fit2^40n^2E bits.
The complete finite family collections fit2^40n^2E, still belowC*U*E.

Allocate/register cells one at a time and stream each ID into the bank.
When a gate or source SWAP needs an ID, decode only that short field;
never stage an entire n-entry source/register map classically. A released
cell is reset/discarded by the channel in Section4 before its free flag
is cleared. Allocation can always find free cells by the proved maximum
simultaneous count, without a contiguous-block fragmentation assumption.
The finite source branch also hasO(n) active qubits. All new allocator
steps are charged in the polynomial simulation factor. Reused cells keep
the same canonical IDs; no lifetime ID or sparse translation history grows.
This gives a maximum quantum address rangeH, not just live occupancy.
The physical prefix counts all its unused padding;B=O(n^2E) dominatesH.
Both address spans are polynomial, so complete addresses haveO(logn) bits.

## 4. Physical bank, access and executed operations

Store virtual classical bit i as the basis value of physical wire2i.
Store virtual quantum wireq at wire2(q+1)+1; reserve wire1 for a fair bit.
Maintain one allocated paired prefix0,...,2h-1, initiallyh=2. Before
accessingi>=h orq+1>=h doubleh until the slot fits, appending and
initializing every new wire. Old indices/states remain fixed. Never
shrink the prefix duringV. Every unused padding wire counts inS_Q.
The maximumh is below2max(2,B,H+1), so the entire prefix isO(n^2E).
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

The full paired prefix hasO(B+H)=O(n^2E) allocated qubits, including its
unused padding, all virtual data/metadata, original coherent registers,
coin scratch and growth overlap. Temporary source wires addO(n). Because
E=O(n^(1)), this proves
 S_Q=O(n^(3)).
Basis-state wires are counted qubits and still contribute to the full
address fee. The proof uses maximum reserved ranges and slot reuse, not
success-conditioned or small observed occupancy.

All added work is charged separately. WithE<=2n, B=O(n^3) andH=O(n^2),
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
 T_physical<=poly(n)*(T_V+n^2E).
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
S_C=n andS_Q=n^(3) envelopes.

The exact time-envelope growth index is1/2. Source2^((1/2)sqrt n) has
index1/2; both polynomial space envelopes have index0. Only time is the
numeric objective. These are upper-envelope indices, not runtime lower
bounds. The bank method is credited prior work. The larger physical quantum
space buys linear classical memory atV's full time/source envelopes; it
is a distinct resource tradeoff, not an optimality or generic novelty claim.
No positive robustness, priority, practical speed or cube-root time.

