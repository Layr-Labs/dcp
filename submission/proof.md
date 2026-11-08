# LG32-ASYM125-SHARP: explicit raw work, space and acquisition envelopes

## 0. One physical implementation and exact raw envelopes

For every N>=2 and s in Z/NZ set n=ceil(log2 N). The single physical
LG32-ASYM125-SHARP completion below recovers the whole s with
unconditional probability at least1-2^-8 from independent ideal copies.
Its simultaneous worst-case guarantees on EVERY branch are
 T=O(n^136*2^((23378749/4990000)*n^(2/3)+(12311877/1247500)*n^(1/3))),
 ordinary S_C=O(n),
 full S_Q=O(n^88*2^((3249/10000)*n^(2/3)+(3249/5000)*n^(1/3))),
 Q=O(n^(19/6)*2^((499/1000)*n^(1/3))).
Failed/rejected/discarded inputs, partial constructions, retries, caps,
ABORTs, addressing, initialization, exact finite overflow repair,
source moves and output-first cleanup are all included. Constants are
absolute. Upper-envelope indices are2/3,0,2/3,1/3 in that order;
the time score is2/3. The supported fraction is0 under the model:
Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.
All five assertions concern ONE fixed uniform physical configuration.

## 1. Complete reference and precise borrowed material

The complete virtual reference P is supplied in virtual.md, adapted
from LG32-603 actual6f095593-51ce-4055-8c63-707c437940c8, immutablecommit
3a9525598f00107c4ade9b21389c1d3e2601eb56; original SHA256
e54db374152f5034abdfd4b07e108073b59d0153628a91769c1559397557a940.
All original authors and contextual source credits remain there.
Every source/LE instrument, integer profile, fixed Grover circuit,
capacity, incidence/root law, retry/cap proof, both full-modulus decoders
and finite tester is supplied. This changes the literal schedule to cubic-root depth and square-depth widths; the full new integer-capacity and all-branch resource derivations are supplied in virtual.md. Its resource assertions concern virtual
P. Its conditional-history wording is made explicit using a reduced
low-bit field and finite stopped-coordinate product kernels, excluding
current LE/high arithmetic/helper transcripts. Its fresh-attempt cost
bound uses the conditional tower, allowing own cost/success dependence.
This method is directly adapted from IFW1232-FILTERED actual
 db6af0c1-2762-4fd4-a5ea-d78910d65cb1;
that source's constant-width profile is not selected. No previous
judgment or absent artifact is a theorem premise.

The physical compiler directly adapts indexed EXPONENTIAL unknown-wire
allocation from HPC127-TAGBANK actual6c0e2efd-41bd-4018-a24e-e386f3069c9b,
commit f0fbd85526d7db908a14887ad9ab3cdb7ab602bd; its HPC virtual
algorithm/profile is not run. Generation tags and finite exact repair
are adapted from IFCS1310-TAGBANK actualfc8aa038-cba6-42bf-a317-df1c36c956f7,
commit f761015e2fa6cdb58dfb8b2fec05a28136108f14. Its old unrestricted
Hp/success argument is not adopted. The separately consulted measured
bank/CQ/source-transfer/fixed-prefix method is LLV-GBANKQ25 actual
fbb8f36c-3904-4bf0-9ddf-e9f5d83657ae, commit
100a8e307fd90c489c4d90717613869fed576b3b; its quarter-profile source
and historical comparison are not used. Tags/free lists are standard.
The five original source/method endpoints and the directly adapted LG32-TAGBANK, LG32-Q35-TAGBANK and LG32-ASYM125-TAGBANK completions are declared separately; all needed arguments are supplied here; complete LG32 contextual credits
are retained without claiming their pending graph is verified ancestry.

## 2. Public setup and exact reference execution

Compute n as the bit length of N-1 and dn as bitlength(N)-1. Obtain
a2 by trailing-zero counting, M=N/2^a2; put unused J=0 if M=1.
Compute ceil(sqrt(n)) and z=ceil(cuberoot(n)) with integer binary search. All logarithmic
ceilings mean integer bit-length tests, never real oracles. For
n<2^60 use the original finite exhaustive tester in virtual.md:
stream candidates0,...,N-1 and test each with n+10 fresh shifted
X measurements, stopping at first minus; output first passing candidate
or0. The true candidate always passes; a wrong candidate passes with
probability2^(-n-10), so the union error is at most2^-10.
It uses O(n) ordinary bits/qubits and a finite deterministic cap.

For n>=2^60 use the exact virtual parameters
 r=ceil(sqrt(n)), z=ceil(cuberoot(n)),
 w=floor(3249*z²/10000), y=ceil(499*z/5000),
 Hb=ceil(23378749*z²/4990000), mu=32+y, kappa=ceil(log2(mu))+3,
 c0=kappa+1, lambda=c0+w, U=2^w. The public z here is distinct from the locally scoped g-bit TREE/listing guess denoted z in the virtual primitive.
Retain the32 binary and subsequent32-input levels, all windows,
capacities, list ordering, hash draws, fixed Grover lengths, FAIL and
ABORT rules, supplier counters, guards before each source acquisition,
K-root batches and all decoder steps. In particular
 K=8192*(3r+ceil(log2(n))+30), Nmax=2^(32+5y),
 Dbar=3*K*Nmax*lambda, Dcap=4096*n*Dbar,
 Ccap=8192*n*Dbar, Y=ceil(log2(Ccap)), Qcap=n*Ccap+K.
Use the exact original definition wherever its integer ceiling is
specified. Compute these public scalars before LE; no large profile
array is stored ordinarily. Each scalar has O(n) bits. Depth profiles
and contexts are banked after initialization, or recomputed streamed.
All full N-bit label arithmetic stays full width, with signed carries.
Neither factoring nor a quantum source inverse is assumed.

Fixed finite bit code implements all source loops, arithmetic, stable
sorts and lookup circuits. Resolve equal-key ties by original logical
row order. Qubit handles are opaque identity tokens; they cannot alter
source equality, sorting, random kernels or accepted labels. Return/pass
transfers ownership without cloning. Code-generation/return frames and
long records are banked; only constant-many O(n)-bit fields are staged.

Finite numerical completion. For the rational pt needed by listing,
let a=am and q=16*a+128. In Machin's formula truncate each alternating
atan series at q terms and round each term downward to a multiple of
2^-q. Stream terms with integer schoolbook powers/division and one
current fixed-point sum; indices/powers have O(a) bits because bases
are fixed and there are q terms. Directed rounding gives an interval
for pi of width at most40*q*2^-q+40*5^(-2*q), smaller than2^(-a-8)
for every a>=8. Take its lower endpoint pt. Thus pt<=pi and pi-pt
is below the required error; t is computed by exact floor multiplication
because a is even. The Section4 constant trigonometric tables use their
explicit fixed Taylor/interval prescription, streamed if needed.
This completion is polynomial in n, uses O(n) staging, and does not
alter the stated Grover error or introduce a transcendental oracle.

## 3. Actual static capacities with wider coherent circuits

The new main-branch proof gives mu<=r, lambda<=n,2^kappa<=16r,
so L=2^lambda<=32rU. The largest TREE pre-sort list is
Cap*D=2^(2kappa+16)L<=4*2^29*n^(3/2)*U, including ceil-root margin.
There are at most31 internal nodes and network padding doubles list
length. Addresses in a current TREE list have at most2n bits for
n>=2^60; squared sorting depth is at most4n². A full tuple/index/sum
record has at most128n bits. Ripple comparison, validity and controlled
swap use at most2^16 actions per bit. Multiplying these explicit
factors, including all31 nodes and fixed bookkeeping margins, is
less than
 Mtree=2^64*n^8*U
for every main-branch length. This bounds all Boolean actions, current
classical gate-description records and reversible AND ancillas.
In particular the O(sqrt(n))-width assumption of the fixed profile
is not imported. All known source label/index/arithmetic fields have
O(n) bits, as does the am-qubit Grover input (with constant factor).

An AND creates at most one unknown ancilla per actual gate. Inverse
uncomputation releases the same actual wires. Retained phase indices
use at most32(mu+1)lambda wires; K roots add K wires. LE/source/ripple
scratch is polynomial in n. Their sum with one current oracle fits
strictly in H=2^64*n^16*U unknown slots. The pool is EXPONENTIAL.
A Grover superposition never materializes all2^am classical guesses;
decoder candidates are streamed, not a2^Y stored grid.

Choose the SAME generic fixed classical owner/layout capacities
 A=2^16*n², R=2^128*n^64*U rows per owner,
 Wrow=2^16*n² logical bit cells per row.
Source/generator/sorting stack depths are at mostn; each depth has
fewer than512 fixed families, plus K records and fixed helpers, so
A exceeds the simultaneous owner count. An owner names an array,
not one entry or qubit. Tables/sorts/lists have polynomial multiples
of Cap*D entries; the counted current circuit cache has at mostMtree
records, and QMAP/next/ownership arrays have H rows. All fit R,
with R/H=2^64*n^48. Complete multiword descriptors fit Wrow or are
streamed across successive rows. All ordinary input/output/current
operand/address fields remain O(n) bits; long records are banked.

A bounded cache holds ONLY current Boolean opcodes/constants/wire
references, never coherent values or all possible guesses. Preparing
M records takes polynomial work per record and the corresponding
oracle has at leastM original Boolean actions, which pay that work.
The same fixed templates may instead be emitted online with banked
frames. Every original serial lookup row/gate is still executed;
there is no quantum-addressed RAM. Logical wire IDs are current array/
offset identities, reused after death, not lifetime-growing counters.
Padding cannot create logical tuples or samples. Stable ties use only
original logical order, never physical slot identities.

The injective flattening(owner,row,bit) has complete logical span
 B=A*R*Wrow=2^160*n^68*U.
Every inactive owner/row/field, metadata array and padding bit counts.
Directory scans over A are polynomial, with short ordinary staging.

The complete virtual TREE includes an explicit full-b-bit root_record_valid flag per retained root slot, used by both MARK and the classical append scan. Its O(Cap*n) gates/ancillas and all flag storage fit the already counted Mtree and H margins. No unfiltered root tuple is appended and no source query is added.

## 4. Counted tags, prefix, source moves and indexed unknown pool

Set e=(n+2)^20 BITS per epoch and
 D=B*(e+1)+(A+8)*e+A+2^20*n^4.
Every logical bit c<B has value at raw address(e+1)c and e tag bits
following it. Owner epochs, one global generation G and a backup
occupy the next(A+8)e region; active flags and complete fixed binding/
raw interpreter scratch fit A+2^20n4. All intervals are disjoint and
below D. Tags are not tag-recursive. Epoch VALUES stay in qubits;
bit loops use O(log e) indices/carry, not an ordinary e-bit operand.

Raw basis bit j uses physical even wire2j. Unknown pool slot k<H
uses odd wire2(k+1)+1, with odd1 reserved for a fair coin. Let h be
the least power of two at least max(D,H+1,2). Initialize the WHOLE
prefix0,...,2h-1, including padding/inactive spans, before P. Count
one additional source register of n+1 wires. Every original request
acquires one independent ideal rho_s, swaps its n+1 wires into clean
mapped source slots using three CNOTs per wire, and releases the zero
source temporary. All addresses and source costs are charged.

Use counted BIG metadata arrays QMAP, next, active/ownership, plus
head, nonempty and virgin fields. Every array has at most H rows<R.
Initially head is empty, virgin0. ALLOC_Q pops head when nonempty,
otherwise takes virgin and increments it. FREE_Q resets ONLY an actual
dead logical wire, forgets the outcome, writes next[k]=head and pushes
k. Mapping and next reads are CLASSICAL known-index bitbank accesses,
not quantum-addressed operations. No H scan occurs per allocation,
gate, source, attempt, root or BATCH. Returning a register retains its
handle; dropping an alias alone never frees a live wire. A gate reads
current operand IDs from QMAP and addresses the corresponding known
odd wires. Each index below virgin is uniquely live or on the free
stack; free/virgin slots are zero. This invariant follows immediately
by pop/push/reset induction. If no slot existed, all H would be live,
contradicting Section3; no new runtime abort is needed.

Wire lifecycle accounting is explicit. Each TREE Boolean AND has an
actual original gate and at most one new ancilla. Reversing its M-gate
computation includes M original gates and permits the M releases.
Oracle input/phase/source scratch has polynomially many wires per
actual source instruction/bit loop. Phase vector passing transfers
existing wires; only actual reset/discard releases them. Full registers
are initialized/freed by one event per actual wire, charged to their
original bit/gate/reset operations. Hence total actual mapping/allocate/
release events are bounded by a fixed polynomial times(T_P+Qcap+H+1).
Initializing all H slots and final global cleanup occur ONCE each.
All long lifecycle maps/free-list records are basis qubits in B.

All addresses have O(n^(2/3)+log(n)) bits since log U=w. They in
particular have O(n) bits. The numerical value e and its bit-loop index
need O(log n) bits although an epoch value occupies e stored qubits.
Schoolbook address arithmetic uses O(n) ordinary staging. Quantum
input-dependent TREE computations still operate on unknown qubits;
only classical descriptions/wire identities enter the measured bank.

## 5. Explicit indexed bit and lazy-array operations

RAW_READ(j) measures known even wire2j in Z into one reusable classical
bit. RAW_WRITE(j,b) reads old z, applies X iff z differs from b, then
forgets z after use. All addresses are CLASSICAL known words. No gate
is addressed by a superposed bank index, and no coherent dictionary
or RAM operation is assumed. Bit arithmetic and loop/address generation
are charged. Source classical Boolean gates become a fixed number of
such reads/writes; logical multi-bit operations remain explicit loops.

READ(owner,i): compare that cell's tag with the owner's current epoch,
bit by bit, using a reusable equality bit. On equality return its stored
value; otherwise return0. All temporary raw outcomes are forgotten.
WRITE(owner,i,b): set the value by RAW_WRITE, then copy the owner's
current epoch into the tag bit-serially. Intermediate physical substeps
are internal to this logical primitive; no P step or source call is
interleaved. Initial tags are0 and active epochs are nonzero.

ALLOC chooses a free owner. Before using a new generation, if G_tag is
all ones run the exact renumbering of Section6. Increment G_tag bit-serially
and copy it into the owner's epoch; mark that owner active. NO per-cell
clear is performed. All its old tags differ from the fresh generation,
so every unwritten cell logically reads0. FREE marks the logical owner
inactive and drops the logical reference; its old data/tags remain
counted ignored junk. The next allocation gets a new generation. Do not
erase an exponential array on each free/retry.

This realizes zero-initialized classical arrays. Where source code only
specifies fresh scratch, the zero convention is a valid fixed completion;
every logically used source entry is initialized or checked as specified.
P's row domains, lengths, bounds checks and masks are unchanged: padding
does not create extra tuples or circuit rows. Logical copies/updates
retain their original bit loops and logical aliasing. Return/pass of an
array transfers its owner handle; retained siblings keep distinct live
owners. The source's discard-and-rebuild rule never reuses a released
logical input as an accepted new one.

P's LOOKUP is STILL its original SERIAL known-row circuit. For each
known row/bit, READ that logical table bit and emit the SAME controlled
gate on P's original quantum index/equality/output registers. A
superposed P index is not a bank address. Heap and stream accesses are
classically selected. Every source gate, coin, measurement, guard,
failure and retry executes at the specified logical point. No subtree
construction or source request is placed inside a quantum lookup.

Only constant-many O(n)-bit operands, public address words/current frame
location, finite control and bit-serial helper counters are ordinary
classical storage. All original long arrays, scalar records, recursion/
return frames, generator contexts, loop/cap counters and allocator state
remain in counted basis memory. The fixed code generates instructions
online. There is no growing classical transcript or physical call stack.

## 6. Exact overflow renumbering, with no additional failure

We do NOT assume a counter can never wrap at every input length.
The e-bit G_tag represents0,...,2^e-1, tested by a bit-serial all-ones scan;
2^e need not be materialized as an ordinary classical integer. If ALLOC
needs a new generation when G_tag is maximal, PAUSE P and do the following.

For each owner j=0,...,A-1:
 - If active, copy its OLD epoch into the counted raw backup word.
   For every one of its R*Wrow cells, compute the OLD decoded value
   using that backup; store this value and replace its tag by j+1,
   padded to e bits. Only after all cells set its owner epoch to j+1.
 - If inactive, set all its values/tags and epoch to0.
Then set G_tag=A, clear/reuse the backup, and resume the requested ALLOC.

A+2<2^e, so there is room for another generation. This is a finite
exact reencoding of the SAME logical record, including unwritten cells;
it adds no abort, accepted event, source request or probability error.
It clears stale generations even in inactive owners. Afterward every
stored tag is at most A, current active epochs are j+1, and G_tag=A.
Until the next renumbering every new generation exceeds all prior tags.
Inductively ALLOC's unwritten cells always decode0; WRITE stamps the
current owner generation; FREE cannot expose stale data. Repeated wraps
are handled in exactly the same way. It makes progress after every wrap
and does not rely on unknown constants in a resource estimate.

During this scan store the old epoch only in the raw backup, not in
an e-bit classical register. Loop indices for owners/cells/epoch bits
are O(n)-bit words. No P quantum operation or source query occurs until
the reencoding ends. The source's live original quantum registers can
remain untouched throughout. Cost is D*poly(n); space is the fixed
prefix plus the already counted backup/short staging. It is NOT claimed
to be a cheap operation if triggered at a finite small length.

## 7. Decoded correlated-CQ invariant and full correctness

At aligned logical steps, including any arbitrary reference R, the
physical state is of the form
 sum_z p_z |z><z|_(basis bank/raw metadata) tensor rho_z_(mapped P quantum,R),
with short finite control/staged classical fields included as necessary.
The basis records may be correlated with the phase/query registers and
R. No product-state assumption between bank and quantum data is made.
Tags, obsolete values, unused padding and released records are included
in z and remain counted; they need not be independent of retained data.

The quantum component of pi also uses the counted live descriptor map
to relabel each injectively assigned physical slot as its original P
wire, and traces out free/padding slots. Section4 proves this map
remains injective and respects ownership/aliasing through every actual
quantum allocation, transfer and release. Allocate pops a zero free slot
or uses a virgin zero; release applies the same trace-out/zero channel.
These identities hold with arbitrary entangled references, by linearity.

Define pi by decoding active logical arrays through their current epochs,
keeping P's logical control/object bindings and mapped quantum registers,
and forgetting all physical-only tags/allocator details/junk. Thus the
conditional P state for logical record c is the mixture over every z
with decoded record c, not one selected physical history.

Initially this gives P's prescribed input and zero scratch. On a basis
branch, each logical READ returns exactly its decoded bit. RAW Z reads
leave a CQ state unchanged nonselectively; they may reveal a branch
label to a short helper, which is then forgotten. Boolean updates and
WRITE change the decoded record just as P requests. When old records
merge after overwriting or forgetting, their conditional quantum states
mix exactly as classical irreversible forgetting requires. ALLOC decodes
to a fresh zero array; FREE drops just the logical object; renumbering
has the same decoded record on every basis branch. Extra obsolete
records are never passed as logical operands. By linearity these
identities hold for arbitrary conditional rho_z and arbitrary R.

Original quantum gates and classically controlled serial LOOKUP have
P's same conditional action on its quantum registers. Original
measurements/coins have the same instruments. Reset/discard is trace-out
followed by fresh zero even with references; use that allowed channel,
or Z measurement, conditional X and forgetting, on mapped slots.
Every ideal fresh source supplies the same independent rho_s and the
SWAP map preserves it exactly. Consequently at aligned steps
 pi o Phi_physical = Phi_P o pi,
including all actual extraction-error, failed-merge, partial-child,
rejected-source and abort branches. The complete reduced logical state,
unconditional output law and source-request sequence equal P's.

In particular the FULL virtual Sections3-13 establish unconditional
whole-secret recovery at least1-2^-8 for every N,s: their latent-label
and LE coupling, conditional incidence/root-frequency
law, supplier/pool/source caps, both all-modulus decoders and finite tester
are all present. No prior review is a theorem premise. We do NOT claim
their held-out-bit failure bounds conditional on every new helper
measurement transcript; those extra outcomes are marginalized by pi.
The logical distribution is what is preserved. Under a different
adaptive malformed supplier model such extra measurements could matter;
no positive robustness or such transfer is asserted here.

## 8. Exact ordinary and whole allocated quantum space

A fixed number of O(n)-bit current operands/input/output/address/frame
words and bit-loop indices use O(n) ordinary classical space. Every
long source/table/decoder/generator/return/lifecycle record is banked;
epoch values are streamed, not ordinary e-bit registers. Short source
staging and final output fit this same O(n), on every branch.

All inactive padding and raw metadata count. The complete paired
prefix and source temporaries obey S_Q<=2h+O(n)=O(D+H+n).
B=2^160*n^68*2^w and e=(n+2)^20 give D+H+n=O(n^88*2^w).
With z<=n^(1/3)+1,
 w<=(3249/10000)*n^(2/3)+(3249/5000)*n^(1/3)+3249/10000.
Absorbing only the CONSTANT2^(3249/10000) gives the exact claimed
 S_Q=O(n^88*2^((3249/10000)*n^(2/3)+(3249/5000)*n^(1/3))).
This includes the EXPONENTIAL unknown AND-ancilla pool, QMAP/free
metadata, all basis/tag/owner cells, backing epochs, full rounded
prefix, inactive rows/fields/owners and input/source/coin wires.
It is an all-branch maximum span, not expected occupancy.

## 9. Explicit acyclic finite charged driver and lifecycle ledger

Every physical action pays its FULL combined address debit
ceil(log2(S_C+S_Q+2))=O(n^(2/3)+log(n))<=O(n).
All fields/addresses/known wire IDs have O(n) bits. Every schoolbook
Boolean iteration pays this same debit; ordinary staging contains
constant-many current O(n)-bit operands, never a source call stack.
The current raw owner/frame/descriptor locations are staged BEFORE
logical access; RAW never fetches its own address through WORD.

The acyclic helper hierarchy is RAW -> tag/epoch -> WORD -> directory
and current OPCODE. Calls flow downward to already known raw spans.
RAW calculation uses at most O(n²) schoolbook Boolean iterations
and a constant number of known-address bit actions. O(n^4) charged
work covers them including their full address debit and loop updates.
A tag comparison/copy/increment visits e=O(n^20) raw bits, each with
that RAW work; O(n^25) is a complete allowance. A full O(n)-bit
logical WORD streams its bits through tags, so O(n^27) suffices.
A directory scan visits A=O(n²) current owner entries and bounded
header/word fields; O(n^32) covers the n² word scans and e-bit raw
header work. Fixed source operands and current multiword descriptors
have at most O(n²) bits and are streamed, not ordinary arrays.
O(n^40) covers each current OPCODE/field/frame/directory/known-wire
operation, including all nested RAW/tag/WORD work. Reserved raw
header records are not tag-recursive. Helper depth is fixed.

Use the following finite DRIVER tags for the source bitcode:
 BIT_BOOLEAN/READ/WRITE for an original bit action;
 UNKNOWN_GATE/MEASURE/RESET with at most3 known wire IDs;
 QUERY_MOVE, expanded into n+1 individual wire transfers;
 ARRAY_BIND/FREE with lazy generation and owner metadata;
 CALL/RETURN/SCOPE with banked contexts and transfer of handles;
 LOOP/BRANCH and one current NETWORK/TEMPLATE record.
Each current tag obtains fixed-arity operands from already staged
raw descriptors. Full source words/arithmetic/sort/decoder/list loops
are the original actual bit instructions, not a hidden unit-cost
loop in a helper. Array fields and current contexts have O(n²) bits;
source/generator depth is at mostn. Even charging all field/staging
walks across those polynomial domains, n^20 helper invocations per
original bit/gate or actual wire event is an explicit conservative
upper bound: field walks are at most n², context walks at mostn,
and each index is an O(n)-bit ripple/schoolbook word with at most n²
bit iterations. Their product has degree at most5; n20 leaves ample
fixed bookkeeping margin. A directory/tag's INTERNAL iterations are
already in its charged helper, not more source driver events.

Let A_P count the original core bit/gate and charged emission events
of the supplied virtual ledger. By its cost definition A_P<=O(T_P).
Expanding a word/loop/emission tag into fully bit-serial controller
arithmetic is paid by the explicit n20 DRIVER allowance, rather than
inferred to be unit-cost on the physical machine. Long source loops
have actual bit/gate actions per iteration; empty fixed field/context
walks lie in the polynomial current domains already charged above. Known-index serial lookups stay their full
original row/gate loops. The current fixed Boolean cache is prepared
once per actual current oracle block: M records require polynomial
word bookkeeping, and the corresponding original computation has
at least M bit/gate actions. Gate generation uses direct array/offset
identities and fixed sorting-network index templates, not a scan of
all previous gates. Suspended loop/return contexts stay banked.

Explicit wire-event bound. Each reversible AND has one original gate
and at most one newly born unknown ancilla. Its uncompute has at
least one original gate per released such wire. Grover input/H/reset
registers, phase-index wires and original controlled swaps have an
original bit/gate/prepare/reset action per used wire. Source transfer
adds O(n) events per acquired copy. Leaf/merge returns PASS existing
handles; they do not allocate clones. Dropping an alias never releases
a still-live wire. Other scalar scratch/descriptor/rebinding contexts
have polynomially bounded current size at most O(n²) per original
instruction or return; even walking all bounded-depth context fields
is covered by n4. No array of all guesses or exponential instruction
history exists. Thus all actual wire/mapping/ownership/lifecycle events
are at most O(n^4*(A_P+n*Qcap+H+1)). A slot is released at most once
per birth; all H virgin slots are initialized and cleared ONCE, not
on every instruction. UNKNOWN_GATE/ALLOC/FREE use known-index QMAP,
head/virgin/next words, never a whole H scan. Large classical objects
are lazy bank owners, not exponentially many unknown births.

Combining n40 charged helpers, n20 driver invocations and n4 events,
and allowing the extra n source-wire factor, costs at most
 O(n^65*(T_P+Qcap+H+1)).
The larger chosen n120 allowance therefore gives the explicit complete
 Tphysical<=O(n^120*(T_P+Qcap+D+H+1))               (9.1)
when generation repair is absent. Full prefix initialization/output-
first cleanup is one raw scan costing at most O(n4*(D+H)), included
in (9.1). Every helper/driver step is fixed finite bitcode, with only
short ordinary operands and all return/long records counted.

The same finite driver bounds every new generation by a polynomial
times the fixed source/gate/copy budgets. Hence log(generations) is
O(n^(2/3)+log(n)), eventually below the e-bit generation capacity.
Actual exact Section6 repair handles ALL earlier fixed lengths: each
finite scan preserves decoded data/QMAP/free pointers, leaves live
unknown wires untouched, makes progress and adds no source or failure.
The source's finite hard caps and fixed loops bound the number of such
scans on every branch. The finite maximum ratios for all exceptional
lengths, including the original finite exhaustive branch, change only
absolute outside constants. No unchecked all-main nowrap claim or
new runtime guard is used.

## 10. Exact raw work and acquisition envelopes

The complete virtual Section14, for lambda,b=O(n), proves
 T_P=O(n^16*Nmax*2^Hb),
 log2(Nmax)<=(499/1000)*n^(1/3)+38,
 Hb<=v*n^(2/3)+2v*n^(1/3)+(v+1), v=23378749/4990000.
Substitute in the explicit n120 simulation bound9.1. Its source term
is exactly
 O(n^136*2^((23378749/4990000)*n^(2/3)+(12311877/1247500)*n^(1/3))).
The prefix n120D term has polynomial degree208 but leading coefficient
alpha=3249/10000<v at n^(2/3). Thus this fixed polynomial is absorbed
by the STRICT LEADING coefficient gap v-alpha, into the stated n136
target. The H term likewise has smaller leading coefficient; Qcap
has only an n^(1/3) exponential and is smaller still. These arguments
absorb no polynomial at an equal leading exponential coefficient.
The exact declared two-term T envelope therefore follows on every
branch, including initialization and output-first cleanup. Section9's
finite exact overflow costs contribute only outside constants.

Exactly one physical source acquisition executes each original
request and no others. The literal supplied cap is
 Qcap=n*Ccap+K=3*8192*n²*K*lambda*Nmax+K.
K=O(n^(1/2)), lambda=O(n^(2/3)), so the complete cap gives
 Qcap=O(n^(19/6)*Nmax),
including every rejected/discarded/failed/partial/aborted request.
No instruction/helper/repair creates another source call. Since
Nmax<=constant*2^((499/1000)*n^(1/3)), this is the EXACT submitted
 Q=O(n^(19/6)*2^((499/1000)*n^(1/3))).
Bank/pool zeros, metadata and SWAPs are charged work/storage, not
source copies. All three exact nonclassical envelopes and ordinary
O(n) staging concern the same fixed physical implementation.

## 11. Whole-secret success, clean fraction and growth indices

Every actual integer profile, cap and quantum source instrument is
supplied. Complete virtual Sections3-13 prove the reduced random-
stopped-prefix law, conditional fresh-attempt cost bounds, LE coupling,
source/delivery cutoffs and both full-modulus decoders at this profile.
Their unconditional full-secret success is at least1-2^-8, with the
finite exhaustive branch at least1-2^-10. The arbitrary-reference
correlated-CQ decoding inSection7 preserves that full reduced logical
state, source-request sequence and output law. Additional physical
helper outcomes are marginalized, never used to condition held-out
source bits. No positive malformed-copy tolerance is transferred.

For the exact T envelope, log2 B_T=v*n^(2/3)+tau*n^(1/3)+136log2(n)
is v*n^(2/3)*(1+o(1)); thus log2log2 B_T=(2/3)log2(n)+O(1)+o(1).
The same argument gives index2/3 for the exact quantum envelope.
For copies, log2 B_Q=(499/1000)n^(1/3)+(19/6)log2(n), giving index1/3.
The ordinary classical envelope n has index0. These prove all four
exact nonnegative scores2/3,0,2/3,1/3; only time is a numeric objective.
The fifth expression0 uses its explicit independent-ideal-copy model.
These are joint upper guarantees, not lower bounds, optimality,
priority, practical speed, cube-root time or robustness-impossibility.
