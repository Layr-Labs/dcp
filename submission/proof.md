# GPS-LOGBANK: faster inverse-log source growth with linear classical memory

## 0. One physical algorithm and joint theorem

For every integer N>=2 and every fixed s in Z/NZ let n=ceil(log2 N)
and L=log2 n. The ONE physical GPS-LOGBANK interpreter below executes
the full virtual.md program with the Section2 profile. It returns the
entire secret with unconditional probability at least 1-2^-8 from
independent ideal coset copies. On EVERY execution branch its joint
bounds are

    T=O(2^((4/5)*sqrt(n)*L^2)),
    S_C=O(n) classical bits, S_Q=O(n^2) allocated qubits,
    Q=O(2^(sqrt(n)/(3L))) acquired original source copies.

Expressions in L apply for n>=2; the specified finite branch covers
n=1 with an absolute outside constant. The exact resource indices are
(1/2,0,0,1/2). The fifth, unscored, malformed fraction is 0 under:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

Constants are independent of N,s and outcomes. The quantum bound counts
the whole basis bank, all allocation metadata and padding, coherent data,
source scratch and growth overlap. The classical input and final output
are counted. This is a memory/source/time tradeoff, not a cube-root time
algorithm, positive robustness theorem, or time index below one half.

## 1. Materials, exact hypotheses and scope

The complete virtual source/extraction/Grover-combiner/untouched-bit/
full-modulus decoder/two-cutoff framework is GPS-RATIONAL-PURE,
submission 5d7a5a3e-eaf0-4a0d-aab3-9cb18e2d7e32, published commit
5dcd313e579453b26b1422cfbab6f0db8cffccb2, proof SHA-256
deea23d00ca8fabfe817d24bccbdbae9d309680308e7ea8dca4b467aaa412d6a.
Our earlier GPS-LOGSOURCE submission
9474674d-43d6-4a97-9560-ccec3e002644 introduced the direct logarithmic
width argument in this research session. Here its actual coefficient
changes from 2 to 3/2 and every cap is recomputed. The complete adapted
virtual proof is supplied in virtual.md, not assumed from a verdict.

The physical storage template is LLV-GBANKQ4-PURE,
submission 1a79e54e-4dc2-40a6-9b98-c83d2a5c62ef, published commit
5235ed82fb723974b1dc4f5603a9faf7b16fb9e3, proof SHA-256
9a6436538bf63b4fe5b388118b3e84821d2395a3a3f2399bd41f4975e4fb1de1.
Sections3-5 reproduce its seven padded regions, fixed maximum spans,
measured READ/WRITE, growing paired prefix, exact correlated-CQ proof,
source movement and output-first cleanup. Section6 pays its conservative
n^16 factor against the NEW explicit virtual work ledger.
Both published files were fetched and their full hashes compared with
official evidence. Source identities provide provenance, not correctness.
No historical acceptance or provisional dependency edge is a premise.

The template's historical LLV-GBANKQ13-EIGHTH/LLV-GBANKQ13/LLV-GBANK
credits, PSG21 (9fdfdb12-834d-441c-8bb1-717ab380abf3) for generic
measured-basis storage and CQ simulation, and PSG2-QSTORE
(2b2b0036-7bbc-4ce5-80a8-b8928f0ce120) for maximum-span/direct mapping
remain acknowledged. The virtual framework's GPS-Q4/GPS-Q13/GPS and
Regev/Grover/Kitaev/BBHT credits are retained in virtual.md. Neither the
bank principle nor Grover search is claimed as a new invention here.

The precise transferred hypotheses are: the V program is uniform;
its virtual classical record has the typed O(n^2) maximum spans in
Section3; its coherent pool has O(n) maximum slots; it uses measured
classical control with classically indexed wires and explicit serial
controlled subset sums; it has the two actual acquisition/fallback
cutoffs; and its clean input copies are independent. Virtual Sections
2-9 prove its channel, success, actual-branch ledger and profile facts.
Sections3-6 below check those hypotheses for this selected profile.
The old physical source's fourth-root virtual program is NOT executed.

## 2. Exact virtual configuration

Run every instruction, gate, measurement, source request, guard, retry,
failure and cleanup of virtual.md. For n<2^16384 it uses its finite
exhaustive shift tester. Otherwise compute exactly

    v=ceil(sqrt n), ell=ceil(log2 n), z=ceil(log2 ell),
    b=ceil(3*v*ell*(ell+4*z+32)/2), m=ceil((n-1)/b),
    q0=(b+1)^m, G=(2*(b+1))^m,
    K=8192*(ceil(log2 q0)+ell+30), H0=nK+2n,
    Qcap=1024*(2G H0+2n), Cf=ceil(Qcap/ceil(sqrt n)).

All roots and ceilings are charged integer computations. For each
requested D<=n, allocate b_i=min(b,remaining) from level m down to1,
and r_i=b_i+1 when positive. Zero levels pass the SAME owned qubit.
Its two actual guards are the acquisition cap Qcap and high-confidence
fallback cap Cf, checked at their original virtual positions. Source
copies internal to failed extraction or discarded supplier labels are
individual acquisitions; a delivered phase is not counted as one copy.
The controller streams a fixed finite bit implementation of arithmetic,
allocation and Clifford+T generation. Its frames, return contexts,
generator cursors and metadata are all virtual bank data. No table,
circuit or instruction history is preloaded as advice.

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
Decoder root count K<=2^15*sqrt(n)<=2^15n, from virtual Section9.1.
At most a fixed multiple of mR+K+R+1 nodes cover pending siblings,
current roots, active source/combiner helpers and ownership references.
A literal pool has 2^17n slots of 16n bits each. Each retained phase has
one signed label, a bounded reference/owner and free metadata. Source9.2
bounds label magnitude by q0*2^D; log2q0<=log2G<=sqrt(n)/(3 log2 n) on the
main branch by virtual Section9.1's intermediate inequality. A full 3n-bit signed
field therefore suffices, even for wrong labels. The 16n template covers
label, pointers and fixed header fields for n>=2^16384. This pool uses
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

## 6. Fully paid physical resources and success

The input N, output residue and a fixed number of O(n)-bit staged
operands use O(n) physical classical bits. Short addresses and scan
fields use O(log(n+2)) bits, and the finite controller has constant
code. Every other label, profile, cap, recursion context, register-ID
list, allocator record and measurement record is in the counted bank.
Thus S_C=O(n), without a duplicate classical stack or history.
The whole paired prefix has O(B+H)=O(n^2) qubits, including padding,
virtual classical bits and metadata. Original coherent registers,
growth overlap, fair-bit wire and n+1 temporary source wires are
included in S_Q=O(n^2) on EVERY branch. Classical basis values held
in that prefix still count as qubits, even when READ measures them.

Every bank access, address computation, field decoding, bit loop,
source SWAP, initialization, release and cleanup is paid. B=O(n^2),
H=O(n); even scanning the full bank for one requested bit costs only
polynomial work. Region clearing by separate scans costs O(B^2
polylog(n+2)); arithmetic and original predicate gates are generated
online. The same explicit interface therefore has the conservative
bound

    T_physical <= C1*n^16*(T_V+n^2), n>=2.                 (6.1)

For completeness, reads/writes stage a fixed number of O(n)-bit
operands, metadata/free scans visit at most B bit cells, and register-ID
lists stream one known ID at a time. Ripple/schoolbook arithmetic has
fixed polynomial bit cost on O(n)-bit words. A full scan per bit and
separate clearing passes cost at most O(n^8) times a virtual charged
step; n^16 conservatively also covers controller/generator decoding,
pointer validation, source moves and complete startup/cleanup. There
is no hidden unbounded compilation, long-word unit operation, coherent
bank address or uncounted retry. The original two guards remain exact.

Use the STRONGER explicit virtual ledger in virtual Section9.3,
equation(9.4), not its already loosened supported representative:

    log2(T_V/C0)<=(3/4)yL^2+3yLlog2 L+64yL, y=sqrt n.

This includes virtual source work, every failure, addresses, gate
generation and cleanup. Since T_V>=1, (6.1) is bounded by an absolute
constant times n^18 T_V. The added exponent 18L is at most yL on the
main branch. Hence

    log2(T_physical/C2)<=(3/4)yL^2+3yLlog2 L+65yL.

For all L>=16384, L/20>=3log2 L+65: at the endpoint it is
819.2>=107, and the derivative of L/20-3log2 L-65 is positive
thereafter, using ln 2>1/2. We conclude

    T_physical <= C2*2^((4/5)yL^2).                       (6.2)

The actual selected width coefficient3/2 is essential to this paid
time margin. The old coefficient2 is not combined with (6.2). Finite
smaller n change only an absolute outside constant and use the same
explicit finite virtual algorithm and physical interpreter.

Each physical source request corresponds one-for-one to a virtual
request, including every internal extraction/fallback and rejection.
The basis-bank initialization never calls the source. Virtual9.1
proves Qcap<=2^(y/(3L)) on every main history; finite smaller lengths
are absorbed by an outside constant. This proves the physical sample
bound, independently of peak memory. Sections4-5 preserve the whole
virtual output channel, not merely a favorable subset of outcomes.
Virtual8's included proof therefore gives unconditional success at
least1-2^-8 for every N,s, jointly with all four physical resources.

## 7. Exact indices, tolerance and resource comparison

For B_T=2^((4/5)sqrt(n)*L^2), log2 log2 B_T=L/2+2log2 L+
log2(4/5), whose ratio to L tends to1/2. For B_samples=2^(y/(3L))
the corresponding logarithm is L/2-log2 L-log2 3, giving1/2.
The polynomial spaces n and n^2 have index0. These four exact
rational values describe the full supported physical bounds.

The malformed fraction is epsilon(n)=0 under the exact model in
Section0. All acquired copies must be independent ideal coset states.
The CQ proof transfers that clean promise only, and makes no positive
corruption assertion or impossibility claim. All claims refer to one
physical algorithm/configuration. The virtual quadratic-classical/
linear-quantum declarations are scoped virtual data, not current claims.

As a comparison of DECLARED supported guarantees, this physical vector
strictly improves LG-ASYM147-QUASIPOLY, submission
d8ed8bbe-4d69-4611-b83e-09be4cff3825, under the identical error model
and zero fraction. That row declares T=O(2^(yL^2)), S_C=O(n),
S_Q=O(2^(91L^3)), Q=O(2^((339/1000)y/L)). Our work is smaller
since4/5<1; our source bound is smaller since1/3<339/1000; our
quantum space is smaller since log2(n^2)=2L=o(L^3); classical
space and tolerance are equal. This is a comparison of reviewed
upper bounds, not a lower bound on another algorithm. That row
was used as a comparator only, not as a source of the algorithm.
The comparison is separate from whether hosted review accepts this
candidate. No global optimality or cube-root work is asserted.

## 8. Scoped fixed-integer logarithmic family

The selected five physical claims above are ONLY the h=1 program of
Section2. This additional theorem does not import resources from another
configuration. For each FIXED integer h>=2 there is a corresponding
uniform program of the same framework/interpreter with joint envelopes

    T=O_h(2^((4/5)*sqrt(n)*(log2 n)^(h+1))),
    S_C=O_h(n), S_Q=O_h(n^2),
    Q=O_h(2^(sqrt(n)/(3*(log2 n)^h))),

clean fraction0, unconditional full-secret success>=1-2^-8 for every N,s.
Constants may depend on h, never on the instance or outcomes. It uses
finite exhaustive testing for n<2^L0, L0=16384(h+1)^2, and otherwise

    b=ceil(3*v*ell^h*(ell+2(h+1)z+32)/2),
    m=ceil((n-1)/b), v=ceil(sqrt n),
    ell=ceil(log2 n), z=ceil(log2 ell).

Recompute ALL products, decoder counts, extraction precisions and the
two actual cutoffs from this width. No input-dependent h is substituted.
This statement does not imply polynomial copies, an attained zero source
index, or the cube-root time target. It supplies distinct configurations.

Proof. Put L=log2 n, y=sqrt n, D_h=L+2(h+1)log2 L+32. At L>=L0,
D_h<=ell+2(h+1)z+32<=L+2(h+1)log2 L+4(h+1)+33<=2L.
The last comparison holds at L0 using log2(h+1)<=h and improves
thereafter by differentiation; its linear derivative correction is
2(h+1)/(L ln 2)<1. Also (L+1)^h<=2L^h because
(1+1/L)^h<=exp(h/L)<2. The integer formula thus gives

    (3/2)y L^h D_h<=b<=16y L^(h+1).

One has y>=64L^(h+3) on this range. Indeed at L0 the logarithmic
comparison follows from
6+(h+3)(14+2log2(h+1))<=2h^2+20h+48
 <8192(h+1)^2=L0/2;
its difference has positive derivative 1/2-(h+3)/(L ln 2).
Therefore b<=n/4, R<=n, mR<=3n and all polynomial-storage and
arithmetic hypotheses of virtual Sections2-9 and Sections3-6 hold
for this fixed h, including h_e=O_h(sqrt n).

With A=log2(2(b+1))<=L/2+(h+1)log2 L+6<=D_h/2-10,
and A<=L, the ceiling m<=2y/(3L^h D_h)+1 gives

    log2 G<=y/(3L^h)-(20/3)y/(L^h D_h)+L
            <=y/(3L^h)-(10/3)y/L^(h+1)+L.

The SAME exact cap bound Qcap<=2^28 G n^2 is valid, using K<=2^15y.
The displayed negative margin absorbs 3L+28, because
(10/3)y/L^(h+1)>= (640/3)L^2. Hence the stated pure copy
representative holds on every main branch, without dropping a factor.

For fixed h the exact integer ceilings give
b/2=(3/4)yL^(h+1)+O_h(yL^h log2 L).
Apply the explicit every-branch ledger (virtual9.3) and pay the physical
n^16 factor of (6.1). The total logarithmic work is at most
(3/4)yL^(h+1)+O_h(yL^h log2 L)+O_h(L).
Since log2 L=o(L), this is at most (4/5)yL^(h+1) eventually.
All smaller lengths are finite for fixed h. The original conditional
combiner, untouched-high-bit law, decoder and both cutoff couplings are
uniform in this valid profile, so the same unconditional success proof
applies. The CQ interpreter preserves the request sequence and channel.
This proves all four resources and clean tolerance jointly. Each time
and source envelope has index1/2, and the two spaces have index0.
