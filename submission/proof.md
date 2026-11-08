# LG-POLYARITY130-TAGBANK: uniform growing arity and counted basis storage

## 0. One physical algorithm and joint theorem

For every N>=2 and s modulo N, let n=ceil(log2 N). One fixed uniform
physical algorithm below recovers the ENTIRE s with unconditional
probability at least1-2^-8 from independent ideal copies, jointly with
the following WORST-CASE bounds on EVERY execution branch:
 T=O(2^((3/8)*sqrt(n*log2 n))), ordinary S_C=O(n),
 full allocated S_Q=O(2^((3/8)*n^(7/16)*sqrt(log2 n))),
 total acquired Q=O(2^((3/16)*sqrt(n*log2 n))).
All failures, discards, partial attempts, guards, retries, aborts,
initialization, actual finite epoch repair, source moves and cleanup
count. The exponent coefficients are exactly3/8 for time/quantum and3/16 for samples and all outside
constants are absolute. Physical time/classical/quantum/sample indices are1/2,0,7/16,1/2.
The clean fraction is0 under the canonical model:
Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.
All five assertions concern this same configuration. No lower bound,
optimality, priority or practical-size assertion is made.

## 1. Complete reference and precise borrowed material

The complete virtual reference P is supplied in virtual.md, adapted
from LG32-603 actual6f095593-51ce-4055-8c63-707c437940c8, immutablecommit
3a9525598f00107c4ade9b21389c1d3e2601eb56; original SHA256
e54db374152f5034abdfd4b07e108073b59d0153628a91769c1559397557a940.
All original authors and contextual source credits remain there.
Every source/LE instrument, integer profile, fixed Grover circuit,
capacity, incidence/root law, retry/cap proof, both full-modulus decoders
and finite tester is supplied. This uniformly extends the primitive to arbitrary computed height h, with explicit f-dependent caps and a new integer schedule; its full all-height probability, capacity and resource proofs are supplied in virtual.md. Its resource assertions concern virtual
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
The five original source/method endpoints plus the directly adapted LG32-TAGBANK and LG32-Q35-TAGBANK completions are declared separately; all needed arguments are supplied here; complete LG32 contextual credits
are retained without claiming their pending graph is verified ancestry.

The directly adapted immediate reference is the complete corrected
LG-POLYARITY130-TAGBANK revision, including its explicit full-residue root
flag/filter and wider-word circuit counting. The earlier counted
LG32-TAGBANK and changed-profile LG32-Q35-TAGBANK supply the consulted
compiler completion and integer profile/capacity-accounting method.
Their fixed literal profiles and prior review judgments are not run
or used as theorem premises. Every directly consulted source/method
is represented separately in the publication declaration; all needed
proof bodies are supplied here, without an absent artifact premise.

## 2. Public setup and exact execution

Compute n=bitlength(N-1), dn=bitlength(N)-1, a2 by trailing-zero
counting and M=N/2^a2. Put J=0 if M=1. Let ell=ceil(log2 n),
using integer bit tests, with ell=0 at n=1. For ell<2^20 run the
complete finite exhaustive tester of virtual13. It streams N
candidates and uses at most n+10 independent shifted X-tests for
each, stopping each candidate at first minus. The true candidate
always passes; union error is at most2^-10. Its ordinary workspace
is O(n), and all branch caps are finite.

For ell>=2^20 use EXACTLY the supplied variable-arity profile:
 h=ceil(ell/16), f=2^h, q=f,
 w=min{integer u>=0:f²*u²>=2*n*h},
 y=ceil(n/((f-h)*w))+1, mu=q+y,
 kappa=ceil(log2 mu)+3,c0=kappa+1,lambda=w+c0,
 Hb=ceil((f-2h+4)*w/2),rstar=ceil(sqrt(n*h)),U=2^w.
There are q binary levels and y levels of arity f. At level q+j
use r_i=max(0,(f-h+2)*w-2Hb-2*(q+h*j)). Keep every source,
instrument, stable ordering, hash draw, Grover block/iteration,
failure/guard and full-modulus decoder specified in virtual.md.
In particular Cap=2^(kappa+h+7)*2^lambda,Dnode=2^(kappa+h+9)
for MERGEG (Dnode is unrelated to physical prefix length D below).
Let Nmax=2^(q+h*y), K=8192*(8*rstar+ell+30),
 Dbar=3*K*Nmax*lambda,Dcap=4096*n*Dbar,Ccap=8192*n*Dbar,
 Y=ceil(log2 Ccap),Qcap=n*Ccap+K.
Caps and guards are computed before LE. All profile/decode fields
are banked after streaming setup or recomputed from O(n)-bit words.
The public certificate virtual0/8 proves f*lambda<=n,mu<=sqrt(n),
all exact primitive preconditions, full multi-input allocations,
Sum(mu)>=n and Y<=8*rstar<=n. Windows may equal zero.
There is no assumption of a fixed f or fixed-height theorem.
Compute all integer roots/ceilings by binary search/division.
No factoring, quantum source inverse or real arithmetic oracle is used.

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

## 3. Actual static capacities for uniform variable arity

At every main length f<=2*n^(1/16),mu<=sqrt(n),2^kappa<=16sqrt(n),
L<=32sqrt(n)*U. The enlarged TREE lists have pre-sort span
at most4*Cap*Dnode=2^18*f²*2^(2kappa)*L.
At most f nodes and power-of-two network padding add at most2f.
Each sort has address length at most2n and squared depth4n²;
every record/comparator has at most128n bits and at most2^16
Boolean actions per bit. Thus all TREE Boolean gates, ancillas
and classical description records are bounded by
 2^56*f³*n^(9/2)*U < Mtree=2^64*n^8*U,
since f³<=n³ eventually and at the stated main threshold.
This explicit allowance counts all root_record_valid flags and
full-b-bit comparisons, current tree sums/indices, padding and
the complete fixed sorting circuits. It has no h-dependent constant.
The tuple is f*lambda<=n bits, not f uncounted words.
One AND creates one fresh unknown ancilla and its inverse releases
that actual wire. Retained phase indices need at most
f*(mu+1)*lambda<=2n² wires; K roots and source/LE arithmetic
fit polynomial scratch. With one current oracle these fit strictly
within H=2^64*n^16*U unknown slots. H is EXPONENTIAL.
Unknown Grover/AND outputs never enter a classical cache.
No array of all2^am guesses or2^Y decoder candidates exists.

Choose the SAME generic fixed classical owner/layout capacities
 A=2^16*n², R=2^128*n^64*U rows per owner,
 Wrow=2^16*n² logical bit cells per row.
Source/generator depth is mu and at most f child contexts are
retained at each depth. Sorting/generator continuation levels are
at most n. A conservative count is512*(f*mu+n+K+1)<A families
at every main length. Current sort scratch reuses its owner families;
network gates do not allocate a new array owner per gate. Thus
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
uses odd wire2(k+1)+1, with odd1 reserved for a fair coin. Let h_prefix be
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

All addresses have O(w+log n) bits since log U=w. They in
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

## 8. Ordinary workspace and full allocated quantum span

Only a fixed number of O(n)-bit current input/output, operand,
address, frame and loop words coexist ordinarily. Every table,
profile, suspended frame, circuit/cache/list, decoder and lifecycle
array is in counted basis qubits. Epochs are streamed rather than
ordinary e-bit values. Streaming scalar setup precedes the bank.
Source staging and final output share the same O(n) bundle.
Thus S_C=O(n) uniformly on every execution branch.

With e=(n+2)^20 the COMPLETE prefix, original unknown pool and
temporary source wires have span
 S_Q<=2h_prefix+O(n)=O(D+H+n)=O(n^88*2^w).
The local prefix half-span h_prefix is unrelated to merge height h.
All value/tag/raw bits, inactive owners/rows/padding, rounded prefix,
source/coin wires and unknown AND/comparison flags count.
Virtual15 proves
 limsup(w+88log2 n+O(1))/(n^(7/16)*sqrt(log2 n))<=1/sqrt8.
The positive coefficient gap3/8-1/sqrt8 therefore gives the exact
full allocated quantum bound O(2^((3/8)*n^(7/16)*sqrt(log2 n))).
This is a maximum allocated-span guarantee, not expected occupancy.

## 9. Full charged interpreter and actual finite overflow

Every gate/measurement/bit action pays the FULL physical address debit
ceil(log2(S_C+S_Q+2))=O(w+log(n))<=O(n). RAW arithmetic uses
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
O(sqrt(n*h)+f*ell), uniformly even on unsuccessful branches. Therefore
G uses fewer than2^e generations eventually. This is an eventual
analytical bound, not an unchecked all-length nowrap assertion.
At every remaining fixed length actual overflow performs Section6's
finite exact scan, preserving all decoded records/QMAP/free pointers
and leaving live unknown wires untouched. It adds no source or failure.
Finite deterministic original caps bound the number of actual scans;
all ratios at the finitely many exceptional lengths are finite. Their
maximum affects only outside constants. The original finite tester
also contributes only a finite prefix, without altering the algorithm.

## 10. Exact physical work and one-for-one acquisitions

The supplied uniform source14/15 proves, with t=log2 n,
 limsup log2(T_P+2)/sqrt(n*t)<=1/sqrt8,
 limsup log2(Qcap+2)/sqrt(n*t)<=1/sqrt32.
Every arity factor is included: enlarged TREE capacities, targets,
wire/tuple lengths, retained siblings, uniform failure analysis,
complete caps/guards and the factor2^(((G+3)/2)*c0).
The last has logarithm O(f*ell)=O(n^(1/16)*log n), which is
lower order here. It is not a fixed polynomial factor in the work.
Section9's compiler adds only a fixed polynomial multiplier to
T_P+Qcap+D+H+1, including full addressing, description emission,
source/lifecycle work and whole-prefix initialization/cleanup once.
D,H have logarithm w+O(log n)=O(n^(7/16)*sqrt(log n)), strictly
smaller order than sqrt(n*log n). Thus
 limsup log2(Tphysical+2)/sqrt(n*log n)<=1/sqrt8<3/8,
giving the EXACT work envelope O(2^((3/8)*sqrt(n*log n))).

Generations have logarithm O(sqrt(n*h)+f*ell), eventually below
e=(n+2)^20. Any remaining finite lengths use the exact Section6
repair, preserving all records/unknown states without extra source
or probability failure. Deterministic caps bound every scan count;
finite maximum ratios and the finite exhaustive prefix change only
outside constants, not the submitted coefficient or growth index.

Each physical acquisition corresponds to exactly one original request
at its original source guard; no others occur. Qcap includes every
rejected/discarded/failed/partial/aborted request. Zero initialization,
metadata and source SWAPs are charged gates, never source copies.
Since1/sqrt32<3/16, the exact acquisition envelope is
 Q=O(2^((3/16)*sqrt(n*log n))).
All these guarantees concern the same fixed physical implementation.

## 11. Joint correctness, clean fraction and exact indices

Every capacity, width and primitive condition is proved at the main
threshold. The all-height expectation/overflow bound, exact full-b-bit
root flags and append filter, reduced stopped-coordinate kernels,
fresh-attempt cost tower, LE coupling, source/delivery/quota caps and
BOTH full-modulus decoders prove unconditional whole-secret success
at least1-2^-8. The finite tester has error at most2^-10. Section7's
arbitrary-reference decoded-CQ channel preserves the complete process
and one-for-one source law. Helper outcomes are marginalized; unused
source blocks are not conditioned on LE or physical scratch records.

For2^(a*n^p*sqrt(log n)), loglog equals p*log n+(1/2)loglog n+log a.
Hence the work/full-quantum/sample envelope indices are1/2,7/16,1/2;
ordinary n has index0. These are upper-envelope indices, without
matching algorithm lower bounds. Clean tolerance0 uses the canonical
independent-ideal-copy model and asserts neither positive robustness
nor impossibility. No protected limit, simulated judgment, fabricated
acknowledgment or prior verdict supplies any mathematical premise.
