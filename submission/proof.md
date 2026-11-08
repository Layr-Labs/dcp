# LG32-Q35-TAGBANK: complete counted-basis implementation

## 0. One physical algorithm and simultaneous guarantees

For every N>=2 and s in Z/NZ set n=ceil(log2 N). The single physical
algorithm below recovers the entire s with unconditional probability
at least1-2^-8 from independent ideal copies. On EVERY branch jointly,
including all failed attempts, wrong extracted labels, rejected copies,
caps, aborts, initialization, source moves and output-first cleanup,
 T=O(2^((6831/1000)*sqrt(n))), S_C=O(n),
 S_Q=O(2^((1/2)*sqrt(n))), Q=O(2^((7/20)*sqrt(n))).
All constants are absolute. Full allocated quantum memory is counted.
The clean tolerance is0 with the canonical model:
Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.
All four guarantees concern this same implementation/configuration.

## 1. Complete reference and precise borrowed material

The complete virtual reference P is supplied in virtual.md, adapted
from LG32-603 actual6f095593-51ce-4055-8c63-707c437940c8, immutablecommit
3a9525598f00107c4ade9b21389c1d3e2601eb56; original SHA256
e54db374152f5034abdfd4b07e108073b59d0153628a91769c1559397557a940.
All original authors and contextual source credits remain there.
Every source/LE instrument, integer profile, fixed Grover circuit,
capacity, incidence/root law, retry/cap proof, both full-modulus decoders
and finite tester is supplied. The literal profile is changed to the lower-sample parameters inSection2; their complete capacity and raw resource proofs are supplied in the adapted virtual body. Its resource assertions concern virtual
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
The five source/method endpoints above and the directly adapted LG32-TAGBANK compiler completion are declared separately; all needed arguments are supplied here; complete LG32 contextual credits
are retained without claiming their pending graph is verified ancestry.

## 2. Public setup and exact reference execution

Compute n as the bit length of N-1 and dn as bitlength(N)-1. Obtain
a2 by trailing-zero counting, M=N/2^a2; put unused J=0 if M=1.
Compute ceil(sqrt(n)) with integer binary search. All logarithmic
ceilings mean integer bit-length tests, never real oracles. For
n<2^28 use the original finite exhaustive tester in virtual.md:
stream candidates0,...,N-1 and test each with n+10 fresh shifted
X measurements, stopping at first minus; output first passing candidate
or0. The true candidate always passes; a wrong candidate passes with
probability2^(-n-10), so the union error is at most2^-10.
It uses O(n) ordinary bits/qubits and a finite deterministic cap.

For n>=2^28 use the exact virtual parameters
 r=ceil(sqrt(n)), w=floor(4999r/10000), y=ceil(3499r/50000),
 Hb=ceil(162r/25), mu=32+y, kappa=ceil(log2(mu))+3,
 c0=kappa+1, lambda=c0+w, U=2^w.
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

## 3. Actual static capacity certificate

On the main branch mu<=r, lambda<=r, 2^kappa<=16r and
L=2^lambda<=32*r*U. At a TREE node the largest pre-sort list is
Cap*D=2^(2*kappa+16)*L<=2^29*n^(3/2)*U up to the harmless r/sqrt(n)
rounding factor, which is below4. There are at most31 internal nodes
(h<=5). Rounding a sorting network to the next power of two doubles
this list. For n>=2^28 its address length is less than2sqrt(n), so
log² of the rounded length is at most4n; tuple/index/sum records have
at most128r bits. A comparison, controlled swap and validity arithmetic
can be built with fewer than2^16 Boolean actions per record bit by
ripple addition/comparison and fixed bit loops. Combining these
explicit factors, including all31 nodes and rounding margins, gives
 Mtree <= 2^64*n^8*U
Boolean gates, intermediate wires and fixed circuit-description records
for one current TREE/mark oracle. This deliberately loose bound also
covers binary LOOKUP, transform and source LE scratch, all polynomial
in n. Computing AND reversibly on a fresh ancilla uses at most one
additional live wire per Boolean action; XOR/NOT use fixed templates.
Inverse uncomputation releases those ancillas. Phase/index inputs across
depth require at most32*(mu+1)*lambda wires. Retaining all K roots until
BATCH completes adds K qubits; K=O(r) since ceil(log n)<=r. Therefore
at every instant all original unknown qubits fit strictly within
 H=2^64*n^16*U.
This is an EXPONENTIAL pool. No assertion of polynomial unknown scratch
is made. Grover's am input qubits encode guesses in superposition;
there is no materialized array of all2^am guesses. Decoder candidate
loops are streamed, never a2^Y classical array.

Each table/sort/list has at most a polynomial multiple of the displayed
Cap*D; recursion retains fewer than512 named families per source or
sorting/generator level, plus the K decoder records and fixed helpers.
Sorting/generation stacks have O(log(Cap*D)) depth and source depth
is mu. Consequently fewer than A=2^16*n² owners suffice. One owner
names an array family, not an individual qubit/entry. Choose
 R=2^128*n^64*U rows per owner, Wrow=2^16*n² bits per row.
Then H<R, R/H=2^64*n^48. Full original scalar/label/wire fields and
constant-size multiword descriptors fit Wrow. Any longer register
list uses successive rows, including its complete banked map.
All source, generator, directory, circuit-cache and pool metadata arrays
fit R with the explicit margins above. Padded capacities do not create
logical tuples, list entries or additional samples.

A bounded cache may hold only the CURRENT Boolean circuit's classical
opcodes, constants and wire references, in counted basis rows. It never
holds coherent output values. Building M actual circuit records takes
polynomial work per record and the current oracle has at least M
source Boolean actions; its construction is charged to those actions.
Alternatively emit the same templates online with banked frames. No
lifetime-growing circuit or list of all guessed inputs is retained.
Classical TREE evaluation uses the same banked rows. Logical wire IDs
are current array/offset identities, reused after death, never a
lifetime gate counter. Fixed lookup is the complete SERIAL source
known-row circuit, with every emitted gate charged.

Flatten logical address(owner,row,bit)=owner*R*Wrow+row*Wrow+bit.
The complete logical bit span, counting all inactive padding, is
 B=A*R*Wrow=2^160*n^68*U.
Per-family scalar/metadata arrays use this same span; no auxiliary
ordinary array exists. Directory scans over A are polynomial.

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

All addresses have O(sqrt(n)+log(n)) bits since log U=w. They in
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

## 8. Whole allocation and ordinary classical workspace

Only a fixed number of O(n)-bit input/output/operand/address/frame
words and bit-loop indices coexist ordinarily. All long scalar,
source/table/list/decoder/generator/control/return/pool records remain
banked. Source preparation and final output use the same staging.
Thus S_C=O(n) on every branch. Fixed control code is uniform.
The complete prefix plus temporary source wires gives
 S_Q<=2h+O(n)=O(D+H+n)=O(n^88*2^w).
Since r<=sqrt(n)+1 and w<=4999r/10000, this is
 O(n^88*2^((4999/10000)*sqrt(n))).
The EXACT positive gap1/2-4999/10000=1/10000 absorbs88log2(n)
and all constants. Hence S_Q=O(2^((1/2)*sqrt(n))). This includes
all original coherent ancillas, both banks, tags, backups, padding,
unused owners/rows/fields, H pool slots, source and fair-coin wires.
It is a maximum allocated-span guarantee, not expected occupancy.

## 9. Full charged interpreter and actual finite overflow

Every gate/measurement/bit action pays the FULL physical address debit
ceil(log2(S_C+S_Q+2))=O(sqrt(n)+log(n))<=O(n). RAW arithmetic uses
fixed schoolbook loops on O(n) bits with charged Boolean operations.
A bank bit streams e=O(n^20) tag bits; a bank word repeats this over
O(n) bits. Directory selection scans A=O(n²) entries, with raw current
frame/descriptor location staged before entering the logical helpers.
Suspended frames and descriptor arrays remain banked. No helper fetches
its own raw handle recursively. Gate generation streams finite templates;
ordinary code contains no unbounded stack or circuit description.

An explicit conservative hierarchy suffices: raw address/bit work n4;
tag read/copy/increment n25; streamed logical word n27; directory/
fixed-field/frame selection n32; gate/word/lifecycle dispatch n40.
Each exponent is an upper allowance after charging its own address
arithmetic; epoch loops are fixed twenty-degree and never invoke
source operations. Nested source loops remain original instructions,
not hidden in a helper. A finite bounded-arity driver emits at most
n20 helper invocations per original bit/gate or actual lifecycle event;
network/template generation and current cache construction are charged
as in Section3. The larger n100 allowance covers their product and
ordinary staging accesses. No H-sized scan is included in this per-event
cost. Complete prefix initialization/cleanup is a raw D+H scan once.
Thus eventually Tphysical<=poly(n)*(T_P+Qcap+D+H+1), with a fixed
polynomial (n120 is a sufficient conservative combined allowance).

The number of generations is bounded by a fixed polynomial times the
fixed original operation/copy budgets and H. All these have logarithm
O(sqrt(n)+log(n)), uniformly even on unsuccessful branches. Therefore
G uses fewer than2^e generations eventually. This is an eventual
analytical bound, not an unchecked all-length nowrap assertion.
At every remaining fixed length actual overflow performs Section6's
finite exact scan, preserving all decoded records/QMAP/free pointers
and leaving live unknown wires untouched. It adds no source or failure.
Finite deterministic original caps bound the number of actual scans;
all ratios at the finitely many exceptional lengths are finite. Their
maximum affects only outside constants. The original finite tester
also contributes only a finite prefix, without altering the algorithm.

## 10. Exact work and acquisition envelopes

The complete virtual Section14 proves on EVERY branch
 T_P=O(n^14*2^((68299/10000)*sqrt(n))),
 Qcap=O(n³*2^((3499/10000)*sqrt(n))).
Its time coefficient68299/10000=6.8299 is strictly below6831/1000=6.831.
D and H have coefficient4999/10000=.4999, strictly smaller still.
Every fixed polynomial in the Section9 bound is absorbed by the
positive time gap11/10000: sqrt(n)/log(n) tends to infinity. Therefore
 Tphysical=O(2^((6831/1000)*sqrt(n)))
with the exact stated rational, and all failures/cleanup included.
One physical acquisition executes each original request and no others;
Qcap includes every discarded/rejected sample, partial attempt and
abort. Bank zeros/metadata and SWAPs are gates, never extra samples.
The exact gap7/20-3499/10000=1/10000 absorbs the source polynomial, so
 Q=O(2^((7/20)*sqrt(n))).

## 11. Joint success and indices

Virtual Sections3-13, with the explicit reduced finite-step law and
fresh-attempt tower, prove unconditional whole-secret success at least
1-2^-8 with the unchanged caps, odd/2-adic decoders and finite tester.
The Section7 arbitrary-reference decoded-channel identity transfers
that FULL output law to this physical implementation. It does not
condition held-out-label proofs on physical helper outcomes, which
are marginalized. No positive corruption guarantee is transferred.
All five objects concern this same algorithm. The exact growth indices
of the upper envelopes are1/2,0,1/2,1/2; only time has score1/2.
For exponential square-root envelopes this follows from loglog growth;
for n it is0. These are upper-envelope indices, not lower bounds,
priority, optimality, cube-root-time or practical-speed assertions.
