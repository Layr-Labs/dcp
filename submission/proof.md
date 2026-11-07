# LLV-GFL300C: compact classical full-log tables save a logarithmic factor

## 0. One physical algorithm and joint theorem

For every N>=2 and s in Z/NZ put n=ceil(log2N). The one physical
LLV-GFL300C implementation below recovers the entire secret with
unconditional probability at least1-2^-8 from independent ideal copies.
On EVERY branch, including failed extraction/search, discarded sources,
abort, setup and cleanup, jointly
 T=O(2^((1/2)sqrt nlog2n+(1/4)sqrt n+2sqrt n(log2n)^(-1/2))),
 S_C=O(n^3/log2n) allocated CLASSICAL bits,
 S_Q=O(n) allocated qubits, Q=O(2^((1/2)sqrt n)) source copies.
Outside constants are absolute. Representatives apply for n>=2; the
same explicit finite branch covers n=1. Exact growth indices are
[1/2,0,0,1/2]; only time scores[1/2]. Fractional tolerance is0 under
this identical clean model:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

The actual change is compact CLASSICAL backing: full-vector slots use
the exact retained-vector bound, completed two-label roots use a separate
pool, and all bases/field locators use the smaller fixed reservation.
Classical bits remain classical bits. There is no basis-qubit data bank
and no transfer of their cost to quantum space. All original coherent
registers and quantum padding are counted in S_Q. This preserves the
selected program's time/source/linear-quantum envelopes while saving a
logarithmic classical-space factor. No generic novelty, priority,
practical speed, optimality or positive robustness is asserted.

## 1. Actual direct sources and complete evidence

The actual complete selected-program source is LLV-GFL300, public
submission7da6b54a-575f-43b7-bd43-baee290960c8, commit
6e17b174372b1b4c92b4007b77825a62a6a464ea, full proof SHA-256
8867fd3c02c4220ec35844b8abf505318befb291259da60d0d4b03c707b4087f.
Its ENTIRE body is copied after the explicit reference-only header in
virtual.md. Every source primitive/verified extraction, phase/failure
instrument, exact profile/cap/finishing rule, all-modulus decoder,
finite branch and probability proof is included. Its coarse original
classical n^3 declaration describes the reference allocation, not this
new compact physical allocation. No old JSON, historical acceptance
or opaque imported theorem supplies a premise.

The distinct direct compact-layout source is LLV-GBANK300C,
physical proof SHA-2564db7268a26f14d8e91b9305429fe6d3a3bfb7059b509266bb5c4bc8229e1f6f7.
It supplies the exact-count full-vector pool, separate TWO-label roots,
smaller fixed regions/field locators and maximum-slot packing proof.
Those capacity arguments are reproduced below. Its measured basis-bank
representation and quantum-storage allocation are NOT adopted: the
packed cells here are ordinary allocated classical memory. The original
program's coherent qubits stay in their separately counted linear pool.
Both actual read/use routes and exact source/dependent citations accompany
the declaration, with full public identity/hash verification before upload.
Pending references are not certified ancestry or redundancy.

All selected-source LLV-GBR200/LLV-GRF320/LLV-GQPL and inherited
upstream credits remain. The compact source's LLV-GBANK300/LLV-GBANK,
PSG21 and GordoAR PSG2-QSTORE credits remain for the fixed-layout
method route. No extra peer algorithm or different virtual profile is
adopted. The new packing is credited prior material in this application;
no source verdict replaces the complete proof supplied here.

## 2. The selected program and actual uniform bit stream

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
record is classical data. A fixed finite controller generates/consumes one
instruction at a time; no exponential code or advice is preloaded. All
addresses use the bounded canonical regions below. Numerical counters may
haveO(n) bits without making their bit-cell addresses exponential.

## 3. Actual compact CLASSICAL regions and bounded quantum pools

Defineell_bank=max(1,ceil log2n),E=2^ell_bank,
J_bank=max(1,ceil(E/ell_bank)),r_addr=ceil(log2(n+2)),
U=2^(2r_addr),C=2^48,W=C*U*J_bank.
On the main branch ell_bank=lambda=ell, E<=2n and E>=ell.
ThereforeJ_bank<=2E/ell, and W=O(n^2E/ell). Reserve seven
physical classical regions of W bit slots at bases tW, in this order:
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
classical data. No duplicate classical map or coherent bank address is added.
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
uses a counted bitmap/free scan, classical-region-resident ordered cell-ID lists,
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
MAXIMUM physical classical slot plus one on every branch is
 B=7C*U*J_bank=O(n^2E/ell) asymptotically,
not merely the number of observed live bits. Small finite lengths
change only the absolute outside constant.

The original quantum program still uses a compact pool with maximum
slot plus oneH=2^32*2^r_addr=O(n), including siblings/roots, current
query/rank/residue scratch and source/LE helpers. Allocate individual
free cells, with all bitmap/ordered-ID lists in the counted classical regions.
Stream one known ID into the controller for each gate or source SWAP,
never an entire n-entry classical map. No contiguous-block assumption,
lifetime cell ID or uncounted address history is introduced. Reset a
released cell by Section4's correct channel before reuse. The entire classical reservation and quantum pool, including unused
padding in each, are counted separately. Complete addresses have
O(logn) bits by these maximum fixed spans.

## 4. Executed physical operations on separate classical/quantum memory

Reserve classical cells0,...,B-1 in the seven fixed compact regions.
These are ordinary counted bits. Read/write a known cell with an ordinary
classical bit operation; charge its complete O(logn)-bit address and all
operand decoding. No memory access is a unit-cost long word. An n-bit
arithmetic operation expands into its stated ripple/schoolbook bit steps.
The controller holds a fixed number of O(n)-bit staged words and short
indices; all bulk labels, arrays, frames, counters and allocator records
are in the counted classical reservation. There is no uncounted stack,
lifetime-name directory or stored exponential gate list.

Original coherent logical cells use their separate fixed pool0,...,H-1.
Count EVERY pool qubit, including unused padding. A register's ordered
cell-ID list and free bitmap are ordinary classical data in the above
regions. Stream a known ID per gate. The original Clifford+T gates,
measurements, resets, failed trials and guards execute in the same order.
Classical table lookups inside coherent predicates remain the original
SERIAL known-row scans: read the known stored bit and emit the same gate
controlled on the original quantum equality/index bits. A superposed
candidate never addresses classical memory. No QRAM oracle is added.

A source request acquires exactly one n+1-qubit DCP copy; if needed
move it by known-ID SWAPs into the logical source register, using O(n)
temporary qubits counted in S_Q. Each SWAP is three CNOTs, fully charged.
No source inverse, reflection or extra acquisition is used. A fresh fair
bit uses a scratch qubit, H and Z measurement. Reset/discard is the allowed
trace-out/fresh-zero channel, or Z measurement/conditional X with outcome
forgotten, valid even with arbitrary reference correlations.

Release classical fields by clearing/reusing the SAME fixed cells; do not
retain an allocation history. At termination copy the final residue to
its counted n-bit output FIRST, then clear/release the whole classical
reservation and quantum pool, retaining that output. Initialization and
all cleanup are charged. This physically implements the new fixed backing
layout, not a promise about a small observed live space.

## 5. Exact logical semantics and whole-secret probability

At aligned steps the physical classical fields encode exactly V's logical
record c with its references translated to their canonical subranges.
The original coherent registers, including arbitrary reference R, have
the same conditional density rho_c. Formally the joint CQ state is
 sum_c p_c |c><c|_classical tensor rho_c_(logical quantum,R),
with physical storage locations relabeled by the fixed field locators.
Initialization gives this relation. An ordinary classical read/write or
Boolean step reads and updates exactly the same logical fields, including
alias order. Irreversible overwriting/forgetting mixes conditional quantum
states exactly as ordinary classical forgetting does. No measurement of
classical storage qubits is involved because these cells ARE classical.

Original coherent gates retain every control and their logical action;
original measurement and fair-coin instruments have the same outcomes
and update the same fields. Source SWAPs identify exactly the same fresh
ideal input channel once per request. Reset/discard has Section4's exact
channel identity with references. Field relocation and released-slot reuse
never clone a phase state or reset a still-owned register. Induction
therefore preserves the full logical state, source-request sequence and
output distribution, including failed extraction labels, partial children,
search failures, discarded copies and abort cleanup.

The COMPLETE reference proof in virtual.md establishes all source/phase/
conditional-overflow/capped-recursion/top-bit/decoder arguments. Thus this
one physical implementation has exactly its unconditional whole-secret
success at least1-2^-8 for every modulus and secret under independent
ideal copies. No favorable-event conditioning, prior acceptance or
empirical audit is a premise. The canonical clean error expression0 and
its model are unchanged; no positive adaptive tolerance is asserted.

## 6. All physical resources and unchanged strict time envelope

Classical space is the WHOLE reservation B plus O(n) controller/input/
output fields. Section3 gives B=7C*U*J_bank, J_bank=O(E/ell),
E=O(n),ell=Theta(log2n). Therefore S_C=O(n^3/log2n), including
all unused classical padding, labels, arrays, free/ID metadata, counters,
frames and arithmetic. The finite branch fits the same reservation;
all smaller lengths change only an absolute outside constant.

Quantum allocation is H=O(n) plus O(n) temporary source/transform,
coin and cleanup scratch. The original depth-first pending-vector
and current query/rank bounds are unchanged. Classical heap cells are
not qubits. The ENTIRE quantum pool and any growth/source overlap count,
so S_Q=O(n) on every branch, including failure and abort.

All added work is charged separately. Each field locator is a finite
integer computation from public padded sizes and logical indices. Full
addresses and gate descriptors are generated through bit loops. Even
charging polynomial scans and O(B^2 polylogn) full-region setup/cleanup
fits a conservative O(n^12) factor times virtual bit work plus polynomial
startup, since B=O(n^3),H=O(n). Original variable-width operations are
first expanded into bit steps, source moves charge O(n) gates/addresses,
and every physical address fee uses Mem=S_C+S_Q. Hence every branch has
 T_physical<=poly(n)*(T_V+n^3).
The original acquisition/leaf guards remain at their original positions.
This counts every failed construction and cleanup, not expected work.

Do not multiply a final pure exponential and drop the polynomial.
Virtual14 supplies the stronger internal estimate, with x=sqrt n,L=log2n,
 log2(T_V/C0)<=xL/2+x/4+O(x/L)+O(L^2).
The added fixed polynomial contributes O(L). Since x/L and L^2 are
o(xL^(-1/2)), the exact stated three-term envelope follows eventually:
 log2(T_physical/C1)<=xL/2+x/4+2xL^(-1/2).
The SAME capped program and backing compiler run at earlier lengths;
their finite maximum ratio changes one absolute outside constant. No
fast-branch postselection, new threshold or unreported polynomial is used.

Each physical source acquisition corresponds to exactly one virtual
request and there are no others. All rejected, failed, discarded and
aborted copies are counted. Virtual8 proves the literal main
nCcap+K<=2^(sqrt n/2), and the explicit finite branch changes only an
absolute outside constant. Thus Q=O(2^((1/2)sqrt n)) jointly with
all above resources and full-secret success. Local zero preparations
are charged work/space, not DCP copies.

## 7. Binding, exact indices and comparison

All five current claims cite this physical main and complete scoped
virtual.md. Every needed primitive and probability argument is supplied;
no parent JSON, historical verdict or inaccessible compiler is a premise.
The one current algorithm uses actual compact classical memory and
separate linear quantum storage. The old coarse reference n^3 classical
statement is not combined with a different configuration's bounds.

The exact time-envelope index is1/2, source index1/2, polynomial space
indices0. Only time supplies the numeric score[1/2]. These are indices
of upper envelopes, not runtime lower bounds. Relative to LLV-GFL300,
classical space saves a logarithmic factor with the same time/source/
linear-quantum/error envelopes. It is a finer proved memory improvement
from explicit actual reservations, not a claim of generic novelty,
priority, practical performance, optimality or positive robustness.
