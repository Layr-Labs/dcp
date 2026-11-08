# PART31-190-TAGBANK: exact 31-qubit odd-partition instrument with counted basis storage

## 0. One physical algorithm and joint theorem

For everyN>=2 and secret s moduloN,put n=ceil(log2N). The one
uniform physical algorithm below recovers the ENTIREsecret with
unconditional probability at least1-2^-7 from independent ideal copies.
On EVERYbranch,jointly,including failures/discards/retries/aborts,
 T=O(2^((11891/10000)*sqrt n)),ordinaryS_C=O(n),
 full allocatedS_Q=O(2^((11891/10000)*sqrt n)),
 total acquiredQ=O(2^((11891/10000)*sqrt n)).
All exponent coefficients are EXACT11891/10000;outside constants are absolute.
Indices are1/2,0,1/2,1/2. Clean fraction0 uses the canonical model:
Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.
No positive robustness,impossibility,novelty,priority,practical size,
optimality or matching lower bound is asserted.

## 1. Complete reference and exact material use

The completevirtualreferenceP is supplied in virtual.md. It adapts
kshitij-hashTRIAD-125,actualf5b375dd-1e5c-4728-95dc-b855b2dc5827,
archive965917f88ec25ccab3d9ce78e07c717a1590a54f,originalproofSHA256
4802f6c40f92567f239d216c49e6e9e1370b8a3af1c62d6524cc84c901d23f8d.
The peer's overlapping-cell/coin-erasure/returned-input approach and
complete source/transforms/LE/linearmerge/decoder framework are
credited. NEWvirtual7 supplies a different 31qubitoddpartitioncover,
exactdyadicdilation,finiteidentityrejection andcost/yieldcertificate.
The newprofile/capacity/fullfailure/raw-resource proofs are supplied
in8/13/14/15. The sourceis MODIFIED,not claimedbyteexact as awhole.
Unchangedcore source/linearmerge/decoderblocks are identifiedprecisely.
The peer's threequbitinstrument and its oldliteralprofile/verdict are
not run as a substitute for this newmacro. No novelty/priority or
claimofgeneralmeasurementoptimality is made. Contextualcreditsfrom
the peer remain in the fullvirtualframework. ItsconventionalS_C
bound differs fromthiscountedphysicalCn realization.

The indexed unknown-wire allocator/head/virgin/next,ownership and
lifecycle method is directly adapted from HPC127-TAGBANK actual
6c0e2efd-41bd-4018-a24e-e386f3069c9b,archive
f0fbd85526d7db908a14887ad9ab3cdb7ab602bd. Its olderHPC virtual
pairing algorithm and numerical profile are NOTselected here.
Generation-tag lazy arrays,bit-serial access and exact finite repair
are adapted from IFCS1310-TAGBANK actualfc8aa038-cba6-42bf-a317-df1c36c956f7,
archivef761015e2fa6cdb58dfb8b2fec05a28136108f14. Its unrestricted
Hp/source-success argument is NOTadopted. The separately consulted
measured-bit bank,sourceSWAP,arbitrary-reference correlated-CQ and
irreversible-forgetting treatment is LLV-GBANKQ25 actual
fbb8f36c-3904-4bf0-9ddf-e9f5d83657ae,archive
100a8e307fd90c489c4d90717613869fed576b3b. Its source profile and
resource comparator are NOTused. Reduced-field/cost-tower clarification
also directly uses IFW1232-FILTERED actualdb6af0c1-2762-4fd4-a5ea-d78910d65cb1;
its literal constant-width algorithm is NOTselected. All five distinct
material routes are retained;no graph or verdict is a premise.

The immediate private working bitbank body was180,whose irrelevant
power-log schedule,coefficient and fixed-K workspace analysis are
removed. That complete private development is acknowledged,without
inventing a public180UUID. If laterpublished,add its direct material
link after both endpoints exist. Only its generic bank implementation
is reused;the exact published storage/CQ methods above remain credited.
Every argument needed HERE is supplied in this file and virtual.md.

The immediateprivate workingcompletions185and188 supply their
completegeneric bank body andpositivegap/profile-accounting method.
Their genuineacceptances are historical,not premises for thisNEW
instrument/profile. Private180's genericbody is acknowledgedabove.
If anyprivate inputlaterpublishes,additsactualmateriallinkafterboth
endpoints exist;no fakeUUID or absentproof is used. This exact new
completealgorithm requires its OWNfresh jointreview.

The separately consulted G4-124 actualb48a1af4-3e6b-45d7-8cdb-a414739ddc21,
archive0cca4a7452d2b18eea6c3ba24ac8123ce7fa2886,proofSHA256
f7fd909455db4e5f0494cdfac437116d6e1201db7d757927db6b016eaee59b4b,
supplies the material multi-component matching-cell andrandomconsumption
inspiration,not the new31-qubit instrument,its6174015488/2820021981law orprofile.
Private186 supplies the immediate finite-trial/uniform-prefix/physical
working proof. No private or peer verdict transfers. Its precise proof
and direct published sources are retained;add186actualIDwhenpublished.

The immediate privatePART7-189 supplies the disjoint multiple-output
partition-cell working proof. This31-qubit child replaces its literal
7-qubitfamily/rate/profile,proving every new condition in full. Earlier
acceptances nevertransfer;link theactual189afterits publicationgate.

## 2. Exact setup and preserved virtual execution

Compute n=bitlength(N-1),r=ceil(sqrt n),ell_n=ceil(log2 n).
For n<2^60 run virtual13's complete streaming finite tester:enumerate
allN candidates with at mostn+10 independent shiftedX-tests each,
stopping each candidate at firstminus. It usesO(n) ordinary staging,
error<=2^-10,finite all-branch caps,and no bank is required.

For n>=2^60 compute PUBLIC
 u=ceil(1189*r/1000)+2,U=2^u,
 A=2^16*n²,R=2^128*n^64*U,Wrow=2^16*n²,
 H=2^96*n^64*U,e=(n+2)^20.
These precedeP's source,caps and measurements. Their binary scalar
representations needO(n) bits;no giant array is ordinary storage.
Initialize the full paired prefix4,then compute and bank P's schedule:
 ell=ceil617r/1250,m=ceil6309r/10000,dl=ceil5581r/10000,
 kappa=ceilLogm+1,K=8192(2r+ell_n+30),
 C_ell=4096*n*K*2^m*dl,
 C_i=ceil(6174015488ell*C_(i+1)/(2820021981(ell-1))) backwardsi,
 Y=ceilLogC0,Qcap=4nC0+K.
EachCi is computed in a constant number ofO(n)-bit current words;
long Ci/pb/tb/position arrays go in the bank. All exact greedy bit
allocations,16(Y+1)PART31rounds,Ltry=Y+ell_n+64,sourceguards andbranches are
EXACTLY virtual8-13. No factoring,Fourier transform,transcendental
oracle,source inverse or inferred circuit is substituted.

P's core actions and all loop/arithmetic/sort/lookup instructions are
finite bitcode. Original equal-key ties use original logical order.
Physical wire/owner identities do not alter source labels,keys,coin
laws or acceptance events. A pool holds unknown phase qubits,whose
KNOWNlabel pairs and wireIDs are separate counted basis records.
EachPART31nonidentityoutcome merges each of its disjoint constrained
groups into a knownpivot,mayproduceupTo14goodoutputs plusarecycled
component,andreturns everyfreeinput unchanged. Released
wiresarezero bytheexactprojector/dilationproof. Identitytokens leave
allinputs unchanged;thefinite Ltrycapabortscleanly. No unknowninput
is cloned or read as classicaldata. Fixedtruthfunctionsgenerateonly
known-addressClifford+Tgates;thereis no QRAM. Allsourcecopyrequests,
includingfailures/discards/aborts,areoriginalguardedrequests.

## 3. Full static capacities,fields and maximum live domains

Virtual8.3 gives C0<=2^33*r^4*2^((148614967/125000000)r).
Since r<=2sqrt n and148614967/125000000<1189/1000,we have
 C0<=2^37*n²*U.
Also dl+m<=(1189/1000)r+2<=u,so every phase-label table has at mostU
rows. SourceY<=2r<n;every full label has3n bits. A pooled record
has two3n-bit labels,a known current wireID,finite links/counters
and flags. Roots/decoder residues haveO(n)-bit values,K<=3n on ALL
main lengths,and grid candidates are STREAMED,not all stored.
Scalar products/carries/counters fit a conservative128n² bits per
fixed-format record;multiword operations retain their actual bitloops.
The constant rationaltrig table is fixed finite code/data,not advice.
There is no variable-precision Grover-angle computation inP.

Owners denote wholeARRAYS,not entries or unknown qubits. Constant-many
LIVE/OUTPUT/sort pool arrays are reused perlevel. The depth-first tree
holds at mostthree tables and fixed scratch roles per sourcelevel;
depthm<=n. Schedule,decoder,LE,transform,return/generator and allocator
roles are fixed families,with fewer than512(n+K+1) live owners.
SinceK<=3n,this is<A=2^16n² at allmainn>=2^60. Retries reuse released
owners and retain no lifetime histories. Pooled phase qubits reside
inH slots,not one ARRAYowner per qubit. Per-owner record domains are
at most constant multiples ofC0,U or polynomialn²;all fitR,including
all map/free/next arrays ofH records,sinceR/H=2^32. Fixed-format
records fitWrow=2^16n². Long scalar/tuple values are not truncated.

For explicit unknown capacity,virtual14 bounds the pool byC0,all
retained source-tree indices by2(m+1)(dl+m)<=16n²,and all current
lookup/ripple/LE/transform wires by a generous2^20n16. PART31 uses onlyconstant<512currentcoin/outcome/Booleanancillas,
withallprivate/releasedwires clean byvirtual7.2,evenonbadinputs. Therefore C0+2^20n16+16n²<H=2^96n64U on ALL
main lengths. Every unknown state is mapped injectively to this pool;
no new allocation failure is added. KnownwireIDs are not quantum data.
There is no retained historical gate cache,or array of quantum guesses.
Original serial LOOKUP gates are emitted online from current tables,
with their full logical rows and original wire identities.

The complete logical value-bit span is
 B=A*R*Wrow=2^160*n^68*U.
It reserves every inactive owner,row,field,tail and map slot. No typical
occupancy argument selects this prefix. Raw descriptors and frame
locations are staged before logical helpers,not fetched recursively.
All physical address widths are at mostu+512+100ell_n<n on ALLmain
lengths: u<=2r<=4sqrt n and the continuousupperbound
4sqrt n+512+100(log2n+1)<n holds at2^60 with positive derivative
margin thereafter. Thus every pointer/current field fitsO(n) bits.
Only constant-many such current words coexist ordinarily.

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

Wire lifecycle accounting is explicit. Every PART31/LOOKUP/adder
ancilla has an original prepare/gate/reset/uncompute event. Reversing
a finite comparator or lookup chain releases its actual clean wires.
The source/phase/LE index registers have polynomial current scratch
per actual original instruction. Phase-vector passing andallPART31 unmerged-input returns transfer existing identities,not cloned states. An alias
alone never releases a live wire. Registers are initialized/released
one actual wire at a time,and their original actions pay those events.
Thus total mapping/allocate/release events are at most a fixed
polynomial timesT_P+nQcap+H+1. AllH slots are initialized and finally
cleared ONCE,not per source call,gate,PART31,attempt or root. Every
long lifecycle map and free-list record is counted basis storage.

All addresses have O(u+log n) bits since log U=u. They in
particular have O(n) bits. The numerical value e and its bit-loop index
need O(log n) bits although an epoch value occupies e stored qubits.
Schoolbook address arithmetic uses O(n) ordinary staging. Quantum
input-dependent PART31 andMERGE operations still act on unknown qubits;
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

In particular the complete supplied PART31 virtual3-13 establishes
whole-secret success>=1-2^-7. Its top-bit fieldG in10 includes only
low leaf coordinates,phase/label-independentPART31cellandidentityoutcomes,low-bit merge outcomes
and low-bit controller decisions;it excludesLE scratch,full highlabel
values and root measurements. Added physical helper outcomes are
marginalized bypi,not inserted intoG. The same unconditional output
and acquisition laws therefore hold. All original root instruments,
returned unmergedqubits,PART31cell/identityIDs and phase-table ownership are
preserved. No held-out-bit independence conditional on a physical
helper/full-label transcript is asserted.

For completeness,the virtual9.1 retry-cost argument can be written
without any assumption of cost/success independence. Given remaining
pool contents and the past at a reached parent attempt,the two fresh
child calls have conditional expected cost at most2A_i,by the uniform
induction bound for all remaining contents. Distribution-free merge
failure has conditional probability<=2^-kappa. Thus the chance of
reaching attemptj is at most(2^-kappa)^(j-1),and summing
 E[cost_j*1{attemptjreached}]<=2A_i*Pr[attemptjreached]
givesA_(i+1)<=2A_i/(1-2^-kappa). This conditions on reach,not on
that same attempt's success. Phantom completion and Markov apply
exactly as invirtual9.1. The supplied10 low-field factorization,
full decoders,all caps and additive LE coupling remain sufficient.

## 8. Ordinary and complete allocated quantum space

All long source records,tables,label/phasewire lists,arrays,profiles,
return frames,decoder root lists and lifecycle maps are counted basis
qubits. Only fixed currentO(n)-bit operands/addresses and streaming
loop variables are ordinary. Epoch values are streamed,not an
ordinarye-bit register. Setup uses the same bound. HenceS_C=O(n)
on EVERYbranch,including abort,cleanup and finite exact repair.

With e=(n+2)^20 andB=2^160n68U,the completeD formula4 andunknownH
haveD+H+n=O(n88U). The fully initialized rounded paired prefix and
source/coin temporaries satisfyS_Q<=2h_prefix+O(n)=O(n88U).
Inactive tags/owners/rows,raw descriptors,padding,entangled unknown
pool and source transfers are all included,not only live occupancy.
Usingr<=sqrt n+1 givesu<=(1189/1000)*sqrt n+1189/1000+3,so
 U<=2^5*2^((1189/1000)sqrt n).
For everyfixeddegreep,n^p*2^(-sqrt n/10000) is bounded overn>=1:
its logarithm p*log2n-sqrt n/10000 tends to minusinfinity. Thus
 S_Q=O(2^((11891/10000)*sqrt n))
with EXACT11891/10000,including every finite exceptional length.

## 9. Full charged interpreter and actual finite overflow

Every gate/measurement/bit action pays the FULL physical address debit
ceil(log2(S_C+S_Q+2))=O(u+log(n))<=O(n). RAW arithmetic uses
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
network/template emission and actual array/wire actions retain their
original bitloop debit as in Section3. The larger n100 allowance covers their product and
ordinary staging accesses. No H-sized scan is included in this per-event
cost. Complete prefix initialization/cleanup is a raw D+H scan once.
Thus eventually Tphysical<=poly(n)*(T_P+Qcap+D+H+1), with a fixed
polynomial (n120 is a sufficient conservative combined allowance).

The number of generations before any hypothetical firstwrap is at most
a fixed polynomial timesT_P+nQcap+D+H+1. All these have logarithm
O(sqrt n+log n) byvirtual14 and the explicit allocations3/8. Hence
it is eventually less than2^e,e=(n+2)^20. This is an eventual
analytical bound,not an unchecked all-length nowrap assertion.
At every remaining fixed length actual overflow performs Section6's
finite exact scan, preserving all decoded records/QMAP/free pointers
and leaving live unknown wires untouched. It adds no source or failure.
Finite deterministic original caps bound the number of actual scans;
all ratios at the finitely many exceptional lengths are finite. Their
maximum affects only outside constants. The original finite tester
also contributes only a finite prefix, without altering the algorithm.

## 10. Full charged work and one-for-one source requests

The explicit finite bitbank/helper/lifecycle completion9 gives,when
no repair occurs,
 Tphysical=O(n160*(T_P+nQcap+D+H+1)).
The n160 allowance includes its n120 bitdriver/helper bound,wire
allocation/reset/mapping per actual original quantum event,and the
n+1 sourcewire transfers per acquisition. There is no wholeH scan
per allocate/free;prefix initialization/cleanup is one charged scan.
Even walkingO(n²) currentcontext fields across source depthn fits
this allowance. Original length-C0/list/sort/lookup loops remain
original charged bit actions,not hidden inside a constant helper.
PART31's fixed-arity gate sequence and its known table additions are
expanded through those same original bit actions. No source calls
or deferred subtree computation occur in a quantum lookup.

Virtual14 provesT_P=O(n6*2^((1189/1000)sqrt n)),
Qcap=O(n3*2^((1189/1000)sqrt n));section8 givesD+H+n=O(n88U).
ConsequentlyTphysical=O(n248*2^((1189/1000)sqrt n)) eventually.
The STRICTgap11891/10000-1189/1000=1/10000 absorbs the whole polynomial:
 Tphysical=O(2^((11891/10000)*sqrt n)).
Original finite exactepoch repair is used at every exceptional fixed
length as9 describes. Original caps bound all such work on every
branch,and finitely many ratios change only outsideconstants. The
finite tester is unchanged. No equality of leading coefficients is
used to suppress a growing polynomial.

Every physicalacquisition executes exactlyONEoriginal guarded source
request at its original logical point. All failures,discarded qubits,
partialattempts and aborts remain inQcap. Metadata zeros,SWAPs,tags,
PART31 ancillas and cleanup are gates,not fresh sourcecopies. Hence
 Q<=Qcap=O(2^((11891/10000)*sqrt n))
with the sameEXACTcoefficient and original independence promise.
No physical bookkeeping changesG or the logical failure budgets.

## 11. Joint scope,indices and limitations

The same physical program supplies all four bounds and entiresecret
success>=1-2^-7,not separate optimizing configurations. All resource
limits hold on every execution branch. Section7's exact decoded-CQ
law and full suppliedPART31source3-13 prove correctness;none of the
historical verdicts,finite diagnostics or external papers is a premise.

ForB(n)=2^((11891/10000)sqrt n),log2log2B=(1/2)log2n+log2(11891/10000),so its
index is exactly1/2. The linear classical envelope hasindex0.
The canonical malformed-fraction expression0 promises only independent
ideal copies;it asserts neither positive robustness nor impossibility.
This construction improves ordinary classical space and all three
selected exponential coefficients versus peerTRIAD125. It does not solve
cube-root totalwork or dominate every other tradeoff on the board.
No novelty or priority in its instrument/bank methods is claimed.
