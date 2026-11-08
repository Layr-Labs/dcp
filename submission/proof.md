# IFCS60-QBOOST163-POLYLEDGER: indexed generation-tag storage for a saturated boosted sieve

## 0. One physical implementation and joint theorem

For every N>=2,s in Z/NZ let n=ceil(log2N). The ONE physical
IFCS60-QBOOST163-POLYLEDGER implementation below executing complete IFCS1310S60
reference P recovers the WHOLE secret with unconditional probability
at least1-2^-8 from independent ideal source copies. On EVERY branch,
including failures, discarded/rejected inputs, source/fallback aborts,
wrong extracted labels, initialization and cleanup, jointly
 T=O(n^20*2^((38662667/23996000)*sqrt n)),
 S_C=O(n) ordinary classical bits,
 S_Q=O(n^2*2^((5999/10000)*sqrt n)) allocated qubits,
 Q=O(n^(7/4)*2^((38662667/23996000)*sqrt n-n^(1/4))) acquired DCP copies.
Outside constants are absolute, independent of N,s and outcomes.
Exact growth indices are[1/2,0,1/2,1/2]; only time scores[1/2].
The fifth expression is0 under the exact canonical model

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

Fixed classically indexed basis wires store every exponential classical
record as COUNTED quantum allocation. Per-ROW generation tags and polynomial stale-row clearing implement
lazy zero arrays; exact overflow renumbering works at every length and
introduces no extra abort or error event. Original coherent queries
remain serial circuits; no bank QRAM is assumed. This different sample/
space/time configuration is not a priority, optimality, practical-speed
or cube-root-time claim. The original n<4096 finite tester is retained.


This candidate directly adapts the full typed-bank and explicit
acyclic charged-helper/driver framework of its privately developed
115 completion, using the complete .5999-width quarter-boost program
from its private101 profile research. Both full source modules are
supplied, including deterministic merge-per-leaf amortization11.2.
The fixed n16 helper/driver ledger and both +32 row paddings remain;
every bound below is proved for this actually selected configuration.
The private precursors have no invented public UUIDs. Actual published
material sources are declared separately before upload; no prior
review judgment or missing file is a theorem premise.

## 0.1. Complete public setup and decoder notation

For EVERY integer N>=2, compute public integers
 n=bitlength(N-1)=ceil(log2N), d=bitlength(N)-1=floor(log2N),
 a2=max{a>=0:2^a dividesN}, M=N/2^a2.
Count trailing zero bits of N for a2 and shift for M. These are exact
integer bit operations using O(n) staged words, not a factoring oracle.
Thus M is odd, N=2^a2*M, 2^d<=N<2^(d+1), and d<=n<=d+1.
The notation below for s1,s2 refers to TRUE secret components in the
proof, not unknown values required by public setup; the decoders
compute their estimates. If M=1 the odd decoder sets s1=0 and skips;
if a2=0 the 2-adic decoder sets s2=0 and skips. Otherwise for M>=3,
 d=a2+floor(log2M)>=a2+1,
so d-1>=a2 and the CRT exponent d-1-a2 is nonnegative. Powers of2
are units modulo odd M. A fresh latent label k uniform on[0,N)
passes k<2^d with probability2^d/N>1/2, and the accepted label is
uniform on[0,2^d); this is the actual range used in decoder9.

On the MAIN branch n>=4096, after computing Section7's literal
profile, define the unused-as-needed public decoder parameters too:
 m_d=min{m in[1,mu]:Sum(m)>=d-1}, nq_d=2^(h_(m_d))*(kappa+1+nu),
 J=min{j>=0:2^(j+3)>2*M},
 K=2^13*(ell(nq_d)+ell(n)+30),
where ell(x)=min{r>=0:2^r>=x}, ell(1)=0, and forx>=2 it is
bitlength(x-1). The tree at D=d exists since d>=4095 on this branch;
Section7 proves m_d<=mu and h_(m_d)<=hmax. These definitions apply
EVEN WHEN M=1 and decoder9 is skipped: then J=0, the unused nq_d/K
are still computed for the declared Q* cap. Thus J+1<=n in every
main case, and all cap/precision/fallback parameters are unambiguously
computed before acquisitions. They agree with decoder9 when M>=3.
For n<4096 only the complete finite tester is executed; its setup
requires the public n,N and has no tree or odd-decoder call.

Notation (CW1's): d = floor(log2 N); N = 2^a2 M with M odd; s1 = s mod M; s2 in [0, 2^a2) with
s = s1 + M s2 (mod N); omega = exp(2 pi i/N); data basis states |u>, u in [0,N), are stored in n qubits. A
"label" is a known integer, a "multiplier" W an integer frequency factor, hd a Hamming distance; T denotes
total work only.

<!-- COMPLETE_PUBLIC_SETUP_END -->

## 1. Actual complete sources and evidence scope

The directly consulted original saturated framework is IFCS1310S60, public
7bd3dabc-c131-48b7-a46d-30fe2e1301fb, commit
4a86c6fc47fab61ec0eec71ebe756f9a2404606b, full proof SHA256
1ebbab84308e96da2d6f8f148ccabd9bf6822cd7539c9b07efece2e69800cb3b.
The NEW quarter-boost/amortized selected program P adapts that framework.
The ENTIRE selected source argument is supplied across virtual-phase.md then
virtual-decode.md with VIRTUAL-ONLY resource scope. It is NOT byte-exact:
new5.7 marginalizes CURRENT LE transcripts in the ideal law,8.2 defines
precise low-bit Hp with full stopped-coordinate factorization, and11.1
uses explicit conditional fresh-attempt costs. All exact source profile,
LE/error/fallback/source caps, saturated r=0/unsaturated merge cases,
moment algebra, both full decoders and success proof are supplied.
Original pure envelopes remain true VIRTUAL reference statements;
this main proves sharper raw physical bounds with explicit powers.
No original JSON, public verdict or graph edge supplies a theorem.

The immediate tagged-bank method predecessor is actual public
IFCS1310-TAGBANK fc8aa038-cba6-42bf-a317-df1c36c956f7,commit
f761015e2fa6cdb58dfb8b2fec05a28136108f14, main SHA256
a5652df5cb9098207a1d7650aa2eef0cd13b41bcb2dbf8355529d1cba2c0820c.
Its fixed tags, exact finite overflow repair, indexed bit-serial fields,
whole spans and arbitrary-reference CQ/source channels are adapted.
Its OLD unrestricted Hp success lemma is NOT a premise and its native
or hosted acceptance cannot cure the known LE-transcript conditioning
gap. Original uncorrected family remains on publication hold.

The separate proof-repair source is local IFW1232-FILTERED, main
c9e9a9f7f8d5cd8078044952c930a51a624700264664c8b0c81d4b81d2966c94,
phasef91d8ec7d7da6142462fb37d55803f63beba169355dbf51cf09bc7d3a24aa37d,
decode52da08dd3db91d2e6788af82415987f9dc8260e362b5465c32708b37f758a79a.
It supplies reduced ideal law, coarser low-bit/stopped selection lemma
and conditional fresh-attempt cost proof, NOT its constant-width source
profile or native verdict. Here the saturated profile is retained;
its lower bound p0=1-1/(2mu) replaces the width-source mu+4 expression.
Source r=0 Stage1 has indicator0 and needs no nontrivial independence;
Stage2 still uses its positive r' as supplied. Actual public repair
identity must be bound before upload; no placeholder is submitted.
This changed complete saturated declaration needs its OWN fresh review.

The distinct corrected measured-bank method source is LLV-GBANKQ25,
public fbb8f36c-3904-4bf0-9ddf-e9f5d83657ae, commit
100a8e307fd90c489c4d90717613869fed576b3b, full main SHA256
08608c19bf8d7ba42b50cf01f86662bc4e38ae0de63a2825ed4f86c8f10ca7d0.
Its direct-wire bit interpreter, fixed complete ranges, measured CQ
and irreversible-forgetting/source coupling and uniform generated
instructions are adapted here. Its different quarter-square-root
virtual program and unused historical finishing comparison are not
adopted. Full raw source identities and all five official evidence
bindings were checked; all unique declaration/show/history rationales,
evidence/citations and decision metadata were read with no cursor.
P has13 pending declarations/no accepted edges; pending is neither
verified ancestry nor false and supplies no mathematical premise.

The original tag prototype was never natively reviewed or submitted.
Its history remains credited through the published tagged predecessor;
no prototype score or unrelated phase program supplies a theorem.
Generation tags are standard programming, not an invention claim.
All source-author IFC1, IFC-B/IFCB45, BL1, IFC34, CW1, MW4/MWG716K,
CS1/CS1-LB, CS1-C3L, LL-150, Howgrave-Graham/Joux, Schroeppel/Shamir
and Kuperberg credits in the full body remain. Original first-person
provenance in the adapted body denotes its original authors.
Bank-method PSG21 and PSG2-QSTORE credits remain as in that source.
No external quantum-walk, coherent data structure or positive-corruption
theorem is used. Material public sources must receive both-endpoint
exact-file citations before upload.

## 2. Exactly selected stream, profile and finite branch

For n<4096 execute P's original exhaustive tester: for candidate0..N-1
in order take at most n+10 fresh copies, apply Shift_candidate, measure
control in X, and reject on the first minus. Output the first passing
candidate, or0. The true candidate always passes and each wrong one
passes a fresh test with probability1/2. Union bound gives error<=2^-10.
Stream with O(n) ordinary classical bits and O(n) qubits. All these
finitely many lengths change only outside constants of the envelopes.

For n>=4096 execute the NEW quarter-power-boost P, with
mu0=5999/10000,H00=38662667/23996000,tau0=H00.
Its literal integer parameters are
 w_s=least w with100000000*w^2>=35988001*n,
 v_s=least integer v withv^4>=n,
 nu=v_s,gamma=0,Astar=(w_s-nu)*(w_s+nu-1)/2,
 G=least integer>=0 with Sstar(G)>=n,
 Sstar(J)=Astar+sum_(j<J)min(2w_s+2j+gamma+3,3w_s+3),
 mu=w_s-nu+G+1,kappa=ceil(log2mu)+3,Lam=kappa+1+w_s,
 hmax=w_s-nu+2G+2.
These are source variables. The physical generation word G_tag is
DIFFERENT from source G and source precision G of LE. All square-root
ceilings and finite sums are computed by integer arithmetic, no real
log/square-root oracle. Full virtual Section7 specifies every actual
binary/four-input input exponent, saturated r=0 window, root/partial
width and greedy capacity, including its Lemmas7.0/7.1 and premises.
They are not replaced by a constant-width or favorable-label schedule.

Set nqmax=2^hmax*(kappa+1+nu). The UNCHANGED literal source cap is
 Q*=6*nqmax*((J+1)*K+2a2)+2a2,Qcap=1024Q*,
where J is the odd-decoder stage count, not the sum index. Keep the LE
fallback cap Cf=ceil(Qcap/ceil(sqrt n)), all other LE/verification caps,
source rejections, failures, retries, stopping and both decoder guards
at EXACTLY their logical positions. Compiler work is separately charged;
no source call or logical quantum instrument is inserted or omitted.

Use fixed finite streamed bit code for ripple/schoolbook arithmetic,
merge sort, array heaps, flat lists and source gate generation. Resolve
unspecified heap ties by original LOGICAL tuple/row indices, never
physical owner IDs. Source arrays keep their lengths/field widths,
logical equality/aliasing, bounds checks and row domains. A fixed zero
completion of fresh scratch is valid. All source fields are O(n) bits;
only constant-many ordinary operands are staged, while return frames,
loop contexts, numeric scratch and generator state are banked. There
is no exponentially stored instruction/circuit list or duplicate
ordinary classical recursion stack. Original coins, measurements,
resets, exact constant Clifford+T Toffoli word and source instruments
are retained, including wrong-label and abort paths.

## 3. Source-specific capacities bound MAXIMUM addresses

Layout symbols A,B,D,H,e,G_tag in this main are physical parameters.
Source P's own homonymous logical fields remain exactly its own; in
particular its LE precision parameter is not the physical epoch counter.

This is a concrete layout, not an inference from observed occupancy.
Virtual Sections6-7,11,13 establish on EVERY main-branch execution:
 - depth<=mu+1<=2sqrt n+1<=n, arity<=4;
 - every phase exponent lam_i<=Lam and table rows<=2^Lam;
 - high labels<=3n bits, heap/sort/run arrays O(2^Lam) rows;
 - Buf,Tl<=Cp<=2^(Lam+kappa+3)+1 rows, including saturated r=0;
 - fixed constant-many named array families per frame/merge;
 - K=2^13*(ceil(log2nq)+ceil(log2n)+30)=O(sqrt n) decoder records,
   no stored candidate grid; all scalar/LE/helper frames polynomial;
 - original pending/scratch/source/LE/transform qubits use O(n).
Fixed lengths and cutoff guards hold with wrong numerical labels too.
The complete probability proof and source work/cap arguments are the
full supplied reference, not an earlier score or graph declaration.

Computepublicr_phys=leastintegerwithr_phys²>=n byintegerbinarysearch.
Put A_small=2^18*r_phys,G_big=4096,A=A_small+G_big,
 Rsmall=2^(Lam+32), Rbig=2^(Lam+kappa+32), Wrow=2^16*n.
SMALLownerIDsare0..A_small-1;GLOBALBIGIDsareA_small..A-1.
EachSMALLownerhasRsmallrows;eachBIGownerhasRbigrows.
EveryphysicalrowhasWrowvaluecellsandONEe-bitrowepoch.
New3.2classifiesalllogicalarraysandproveswhichownerclassfits. Actual arrays use their
source lengths and field widths, with the remaining region padding
ignored by the logical program. A global/scalar/frame block can pack
many ordinary fields in rows; a table or stream array receives its own
owner. An owner handle plus row/bit offset is an injective stable address.
Release/reuse returns the SAME owner, not a lifetime-growing address.

For explicit conservative counting, fewer than512 named table, heap,
sort, run, list, arithmetic, generator and frame families per depth suffice:
there are at most five retained phase tables per level; binary scratch
has the listed order,pos,lo,cnt,off,Dx,residue and inverse-block arrays;
the four-input step adds two heaps, sort/run fields, Buf,Tl and block
maps; LE/transform, scalar and decoder families are fixed in the supplied
code. Packing each additional scalar family in one row is more than
sufficient. Also
 K<=2^13*(hmax+ceil(log2Lam)+ceil(log2n)+32)<=O(n).
Weuse the sharperdecoderbound,notO(n): putrho=sqrt n>=64.
BecauseLam<=n and2log2rho+1<=rho (base13<64,derivative
1-2/(rho ln2)>0),ceil(log2Lam)<=ceil(log2n)<=rho.
Withhmax<2rho,K<=2^13*(4rho+32)<=36864rho.
The otherfamiliescount512(mu+5)+4096<1024rho+6656.
Thus512(mu+5)+K+4096<37888rho+6656<=37992rho
 <40000rho<2^18*r_phys=A_small<=A onEVERYmainbranch.
Thisisanexplicitmaximum-liveownerbound,notobservedoccupancy or
anexpectedretrycount. Ownerrelease/reuse prevents lifetimegrowth.
ThecommonMAXIMUMrowbound,includingCpandsentinels,isbelowRbig;
every ordinary logical record is normalized into component rows by3.1; each component fits theNEW Wrow. Schoolbook
scratch can use polynomially many rows in these same families. These
are analytic upper capacities, independent of success/retry history.

The complete logical classical address span is therefore at most
 B=(A_small*Rsmall+G_big*Rbig)*Wrow.
All allocator bindings, flags and free-owner state are counted below.
Choosing a free owner can scan the A slots, which costs only poly(n).
Alternatively an active logical object can be found by a scan of this
polynomial owner directory. No scan over B cells is required to find a
classical address. Source array identity/equality and within-array offsets
are preserved; handles are never used as numerical phase labels or tie
breaks. The memory representation adds only polynomial work per logical
object/bit operation. A bounded-owner allocator completion uses polynomial bookkeeping per
logical object/bit operation. Total added allocations are at most
poly(n)*(C_P+1), with C_P the original elementary operation count;
these costs are explicitly included in Section9. No O(poly(n)*Qcap)
allocation claim is needed for inner helper loops. Its live directory
space is the fixed counted raw region, independent of lifetime. No source probability
argument depends on a physical allocation address.

Pad original quantum objects to a fixed pool of H=2^32*n^2 slots.
This includes the source's at most30n pending index qubits and its
current O(n) arithmetic/lookups, source, extraction, comparison and
reset scratch, with generous polynomial padding. Quantum slot metadata
is counted raw basis data. Quantum free/reinitialize may scan a whole
polynomial-sized register/pool if necessary; that costs poly(n), not B.
Such a scan resets ONLY the released owner slots; all other live P
quantum registers remain untouched.
Original coherent addresses are canonical pool offsets, not lifetime IDs.

## 3.1. Complete component-record layout and finite field bounds

Thissectiondefinesanactualfixedcompletionofthebitcode,notastorage
boundinferredfromobservedvalues. Putrho=sqrt n>=64. Keepalllogical
arraylengths/domains/fieldwidths; representtheirfieldsseparately.
AphysicalrowhasWrow=2^16*n valuebitsandONErowepoch. Unusedbits
andunmappedrowsarepaddingandremainfullyallocated/countable.

Firstderiveuniformcomponentwidthboundsfromtheliteralpublicsource.
By7,hmax<2rho,Lam<=2rho<=n,kappa<=rho/2,A_leaf<=Lam.
Also log2n<=rho/4: at64,12<=16,andthegaprho/4-2log2rho
haspositivederivative1/4-2/(rho ln2). Ceil(log2n)<=rho follows.
Theliteraldecoderformula givesK<=36864rho as3proves,andJ+1<=n.
Thuswitha2<=n,theEXACTsourcecap obeys
 Qcap=1024[6*2^hmax*A_leaf*((J+1)K+2a2)+2a2]
 <=2^30*n²*2^hmax.
Indeedthefirstcoefficientisatmost1024*12*36866=453009408<2^29,
andtheadditive2048nfitswithintheremaining2^30bound.
Consequentlylog2Qcap<=hmax+2log2n+30.

LE'sh_e=ceil(log2(Qcap(n+5)))+14 isatmost
 2rho+3log2n+46<4rho<=n.
Its h_A<=2log2n+18<=rho;F(h)=2^21*h thereforehasatmost
log2n+22<n bits,andt_V=64h_e hasatmostlog2n+7<n bits.
T_V<=log2n+16 andG=n+40+T_V<=n+56+log2n<=2n.
Unwrappedg_j'sdyadicwordsuseatmostn+10bits;verificationrhwords
andproductsfit4n bits. Uniformcusesn+20<=2n bits. Thiscovers
theactualnumericalrecordwidths,notonlysuccessfulestimatelabels.
Everyfixedrational/tableconstantusesfewerthan32bits<n.

Phasehighlabelsuseatmost3n bits. Binaryrank/countersuseatmost
2Lam+1<=n bits;fourtupleindicesuseatmost4Lam<=8rho<=n.
Four-inputcutoff/heap/offsetwordsneedatmostLam+kappa+4<n bits.
Qcap/fallback/decoderloopcountersfitn bitsbytheprecedingcapbounds.
Signeddifferences,carryfieldsandfixedschoolbookproductsfit16n bits.
Originalowner/field/addressdescriptorsareO(n)-bitwords;theexplicit
A/Rsmall/Rbig/Wrow formulasneedfewerthan16n bitsat4096andthereafter,
bythepositivegapsbetweenlinear n andsqrt n/logn. For anexplicitaddressbound,A<=2^19rho,eachrowcount<=Rbig=2^(Lam+kappa+32),
Wrow=2^16*n andLam+kappa<=2.5rho give
log2B<=67+2.5rho+3log2rho<=67+2.875rho.
Sincee/Wrow<1,thetotalrawprefixplusHhasaddressbitlengthatmost
3+max(log2B,35+4log2n)<=70+2.875rho<=4rho
forrho>=64;roundingtoapairedpower-of-twoprefixaddsonebit.
Henceallactualphysicaladdressfieldsfitn bits,wellwithin16n.
Alltheseare
deterministicfixed-widthbounds,includingwronglabelsandabortpaths.

Chooseexplicitnormalformrecordsasfollows. Eachsourcearrayrowis
ascalarorboundedtuple;lab/residue/rank/sort/runrowsarescalarsor
constantfieldtuples,heaps/fiberlistsuseatmost16scalarcomponents.
NumericLE/decoder/control/gate/framefieldsarestoredcomponentwise.
Reserve512componentpositionsperlogicalrecord. Arraysarenotembedded
aslonginlinefields:separatearraysretainseparateownersandtheir
originaldomains. Eachremainingfinitecontrollerfieldgetsitsown
componentposition;thefixedinstructionformatcontainsprogramcounter,
returnpoint,ownerhandles,dimensionsandboundedmanycurrentloopwords.
Therearenogrowinginlinecallstacksorcircuit/transcriptlists.
Useexplicitripple/schoolbookstreamedlinear-spacearithmetic,soits
digits/temporariesareseparaterowswith16n-bitcomponents,notone
polynomial-lengthword. Theactualfiniteformatsfit512positions:
arraytuplesuseatmost16;thefixedcontrollerusesatmost512named
scalar/controlfieldsalreadycountedinthefamilycompletionof3.
Thecompletionusesonlytheoriginalownerfamilies,notanownerperbit.

AlllogicalarrayrowcountsEarebelow2^(Lam+kappa+20).
Forphasetables/binaryscratch/heaps,E<=2^Lam;four-inputBuf/Tl
cutoffsareatmostCp<=2^(Lam+kappa+3)+1<2^(Lam+kappa+4).
LElevelarrayshaven+20rows. Thechosenfinitecontroller/numerical/
linear-spacearithmeticcompletionusesatmost2^16*n²rowsperowner,
anexplicitgenerousboundforthenlevelwordsandfixedcomponentformats;
itdoesnotinvokeanunspecifiedpolynomialdegree. Thisalsofits,
sinceLam+kappa+20=w+2kappa+21>=mu0rho+29 and
 mu0rho+29-(16+2log2n)=mu0rho+13-4log2rho>0:
at64thegap is at least14.6 since mu0>=2/5,andderivativemu0-4/(rho ln2)>0.
Allscalar/metadatawordpositions/finiteformatsarepubliclyfixed.

Maplogical(owner,rowx,componentt,bitb),0<=t<512,0<=b<width_t<=16n,
toPHYSICALrow512*x+t,bitbwithinWrow=2^16*n.
BecauseE<2^(Lam+kappa+20),512E<2^(Lam+kappa+29)<Rbig.
ThisisthecommonMAXIMUMrowbound;3.2provesthesmallerRsmallbound
foreachSMALLtype. AllmappedrowsfitTHEIRdeclaredfixedtype;allsparecomponents,
rowtailsandunusedRrowsremainallocatedpadding. Themapisinjective
andstable;aliasesofthesamelogicalfieldmaptothesamephysicalbits.
Theoriginalarrayrowandcomponentdomains/boundschecksarepreserved.

BeforealogicalREAD/WRITE,thefixedbitcodecomputesthenormalized
physicalbitoffseti=(512*x+t)*Wrow+b. Types/componentwidthsare
fixedcodeorrawdescriptorwords,notanexponentialdictionary;their
constant512formatsandownerbindingsareallocatedinanADDITIONAL
2^20*n4rawdescriptorregion:atmost512componentdescriptorsof16n
bitsperowneruse8192*A*n<=2^32*n^(3/2)<=2^20*n4 atallmainn.
Retain theentireoriginal2^20*n4scratchregionseparately;thenewD
thereforehas2^21*n4totalpolynomialmetadata/scratchpadding.
OnALLOC,thefixedcodewritesitsselectedtype/row/fielddescriptors
beforeanymappedaccess. FREEdropsbinding;unuseddescriptorpositions
areneverread. Descriptorupdatesuserawknownaddresses,notrecursive
taggedreads,andpolynomialinitializationisinsidechargedhelpers.
AllmappingarithmeticusesO(n)-bitwordswithschoolbookpolynomialwork,
chargedperbit. Return/passkeepsownerandlogicalfielddescriptors.
Originalphaseindices,tuple/rankvalues,tiebreakkeysandcollimation
labelsremainLOGICALvalues,neverphysicalnormalizedrowoffsets.
InparticularserialLOOKUPstillloopsoriginalknownlogicalrowx0,
readsthesamecomponentbitsandemitstheSAMEcontrolledquantumgate.
Theaddressnormalizationdoesnotcreateaquantum-addressedbankoperation.

## 3.2. Complete typed pools and temporary-scope certificate

Allretainedphase-vectorlabeltables/commonresidues,sourceLErecords,
numerical/decoder/control/framefamiliesuseSMALLowners. Theiractual
recordrowcountsareatmost2^Lam forphasearrays,and2^16*n²for
theexplicitfinitecontroller/linear-spacenumericcompletionof3.1.
Forphasearrays,512E<=2^(Lam+9)<Rsmall.
Forpolynomialrecords,E<=2^16*n²<2^(Lam+23),because
 Lam+23=w+kappa+24>=mu0rho+28,
andmu0rho+28-(16+4log2rho)=mu0rho+12-4log2rho>0.
At64thegap is at least13.6 since mu0>=2/5;derivativemu0-4/(rho ln2)>0
thereafter. Hence512E<Rsmall forallSMALLrecords.
ThepreviousA_smalllive-familycertificateof3alreadycoversALL
sourcefamilies;movingMERGEtemporariesoutonlyreducesthesmallneed.

EverytemporaryarraycreatedINSIDEMERGEusesaGLOBALBIGowner.
Thisincludesbinaryorder/pos/lo/cnt/off/Dx/residue/inverse-block
scratch,andfour-inputheaps,run/sortfields,Buf,Tl,block/rank/inverse
listsandarithmeticarraytemporaries. Allcutoffs/rowboundsareatmost
2^(Lam+kappa+20),so512E<2^(Lam+kappa+29)<Rbigby3.1.
AssignonefixedBIGroletoeachsimultaneouslylivearrayinthefinite
MERGE/helpercompletion. Therearefewerthan512namedfamiliesin3;
4096rolesincludealltemporarycopiesandhelperformatswithpadding.
Usebottom-upiterativemerge-sort/flatheaploops,notrecursivearrays.
UnusedBIGrolesstillhavetheirENTIRERbigrowregionsallocated.

Hereisthelifetimecertificate,includingallfailure/retry/abortcases.
VEC(i)firstbuildsALLitsf_(i-1)inputsbyrecursiveVECcalls,andONLY
THENcallsMERGE. NoMERGEisactivewhileitsinputsarebeingbuilt.
WithinMERGE,thequantumlookups/gatesandclassicalsort/heap/list
operationsnevercallVEC,LEorsourceacquisition. Theyoperateonlyon
thealreadybuiltinputs. ThusatmostONEMERGEisactiveACROSSALLDEPTHS.
AfinishedchildMERGEreleasesalltemporarybindingsbeforeitsVEC
return;aretainedsiblingkeepsONLYitsphase-vectorrecordandunknown
indexregister. ItsBuf/Tl/helperarraysarenotretainedsubtrees.

Chooseexplicitoutputcompletion:allocateaseparateSMALLphaseowner,
writethecomputedoutputlab/highparts/commonresidue/headerthere,
andcompletealllookup/rankuncomputationsbeforereleasinginputsand
temporaryarrays. OutputrecordsNEVERaliasBIGtemporarylists.
Source6alreadyconstructstheoutputtablewithO(n*2^lam')bitwriting
work;thiscompletionusesatmostthatorderandoneextraSMALLphase
destination. Fivephasetablesperlevelcoverfourinputsplusoutput.
AllunknownquantumregistersstillusetheoriginalcountedHpool.

OnMERGEFAIL,reset/releasetheinputs,dropanyunfinishedoutputbinding,
andreleaseALLBIGrolesbeforeanotherVECattemptbuildsfreshinputs.
NoqueryoccursinsideMERGE,soafallback/sourcecapabortduringinput
constructionhasnoactiveMERGEtemporarypool. Anyglobaltermination
releasesactualSMALLbindingsandtheinactiveBIGroles;thefullphysical
prefixisstillcountedandcleanupcharged. Allsort/heaphelpersareflat
withfixedtemporaryrolesandcannotrecursivelyborrowanoccupiedrole.
ThefiniteBIGroleassignmentcanthusbereusedatEVERYtreelevelwithout
simultaneousaliasing. Pointer/tuple/tieidentitiesremainlogical,
neverphysicalroleIDs. Everylivealiasofonearraykeepsitsbinding;
releasedtemporaryaliasesarenotusedafterreturn/failure.

BIGreuseislogicalforgetting,notanassumptionofproduct-statejunk.
OldrawtemporaryvaluesmaycorrelatewithreturnedphasevectorsandR.
ThelogicalprogramforgetsitsMERGEtemporariesafterconstructingthe
separateoutputrecord;pi alreadytracesthemout. FREEdropsbinding,
andfreshgenerationrowtagsprovidezero-initializedlogicalarrays.
Subsequentrawreset/overwritesofthatforgottenjunkpreservethe
retainedreducedstatebythesamearbitrary-referenceCQargumentin7.
Nophase-statecopyorsourcepreparationisinvokedbysharingbasisdata.

## 4. All tag, raw metadata and paired-prefix storage is counted

Put e=4*r_phys,withr_phys=ceil(sqrt n)asdefinedin3, the NUMBER OF BITS in an epoch word. Integerbinarysearch andmultiplication compute this exactly usingO(n) stagedspace andpolynomialwork. It is a public
polynomial integer. Put Lrows=A_small*Rsmall+G_big*Rbig.
Ownero'srowbaseis o*Rsmall ifo<A_small,and
A_small*Rsmall+(o-A_small)*Rbig otherwise.
ItsrowcountisRsmall orRbigaccordingtoitsfixedclass.
EveryownerhasitsENTIREdeclaredphysicalrows,
eachwithWrowstoredvaluebitsand ONEe-bitrowtag,notWrowseparatetags.
AllvaluesoccupythefirstB=Lrows*WrowRAWslots. Row(owner,x)'stagbitj
isRAWslot B+(rowbase(owner)+x)*e+j. Valuebitb isRAWslot
(rowbase(owner)+x)*Wrow+b. Theseareinjectivefixedknownintegeraddresses.
AdditionalRAWbasisregionsholdownerepochs,allocatedflags/objectbindings,
oneglobalG_tag,onereusablee-bitbackup andfixedinterpreter/poolmetadata.
Theyarenottag-recursive. Ownerdirectoryfieldsarestoredrawbasisrecords.
A conservative totalrawbasis-slotlimitis
 D_bank=D=B+Lrows*e+(A+8)*e+A+H+2^21*n^4.
The last polynomial region covers flags, owner bindings, pool records and
fixed scratch; unused capacity is included. Full epoch words are NEVER
held as e-bit ordinary classical operands. Compare/copy/increment them
bit-serially with a reusable bit/carry and O(log e)-bit loop counters.

RAW slot j is physical even wire2j. Original quantum q is odd wire
2(q+1)+1; reserve odd wire1 for a fresh fair bit. Let h be the least
power of two at least max(D,H+1,2). Initially allocate and initialize
the WHOLE prefix0,...,2h-1 to zero. Every unused owner, row, field,
tag, generation word and padding wire counts in S_Q. Addresses stay
fixed throughout P; no per-bit sparse directory or lifetime allocations
outside this prefix are added. The global persistent owner starts at
epoch1, G_tag=1, with logical input/globals initialized by the bit interface.

A temporary source register of n+1 wires is also counted. For each
original request acquire ONE rho_s, SWAP it into the zero mapped source
slots, then release the now-zero temporary register. SWAP is three CNOTs
per qubit and every address is charged. Initialization/padding uses
fresh zero qubits, not DCP copies. No inverse/control of unknown source
preparation, accessible source purification or reflection is supplied.

For main n, all physical address WORDS have O(n) bits. Indeed
Lam+kappa<= mu0*sqrt n+2log2n+O(1), so
 log2B<= mu0*sqrt n+6log2n+O(1),
 log2(D+H+2)<= mu0*sqrt n+26log2n+O(1).
This is O(n), including complete fixed spans, not only live occupancy.
All address addition/multiplication/shifts on these words use charged
schoolbook bit operations and O(n) staged space. Numeric e and its loop
indices have O(log n) bits although an epoch VALUE has e stored bits.

## 5. Explicit indexed bit and lazy-array operations

RAW_READ(j) measures known even wire2j in Z into one reusable classical
bit. RAW_WRITE(j,b) reads old z, applies X iff z differs from b, then
forgets z after use. All addresses are CLASSICAL known words. No gate
is addressed by a superposed bank index, and no coherent dictionary
or RAM operation is assumed. Bit arithmetic and loop/address generation
are charged. Source classical Boolean gates become a fixed number of
such reads/writes; logical multi-bit operations remain explicit loops.

For eachNORMALIZEDphysicalbitoffseti suppliedby3.1,computephysicalrowx=floor(i/Wrow),b=i modWrow. Thesearethemappedcomponentrow/bit,whileallsourcevalues/domainsremainlogical.
READ(owner,i): compareROW(owner,x)'stagwiththeowner'scurrentepoch,
bitbybitwithareusableequalitybit. Onmatchreturnthestoredvaluebitb;
onmismatchreturn0,withoutclearinganything. Forgethelperoutcomes.
WRITE(owner,i,v): comparetheROWtagwiththeownerepoch. Ifmismatched,
RAW_WRITE0 toALL WrowvaluebitsinTHISONErow,thenbitseriallycopy
theownerepochintotheROWtag. FinallyRAW_WRITEthetargetvaluebitb to v.
Onamatchonlythetargetbitisupdated. Theclear/stamp/writeisONEatomic
logicalprimitive;noPstep/sourcecallinterleavesitsinternalrawactions.
Afterclearallotherrowbitsare0,soactivatingtherowcannotexposestale
junk. Wrow=2^16*n isPOLYNOMIAL;thisisnotanR-roworB-cellscan.
Epochvaluesremainbanked;onlycurrentOn-bitaddresses/indicesandfixed
manyhelperbitsarestaged. Initialrowtags0andactiveepochsnonzero.

ALLOC_SMALLchoosesafreeSMALLownerbypolynomialdirectoryscan.
ALLOC_BIG(role)borrowsthefixeddesignatedglobalrole,provedinactive
by3.2;distinctsimultaneouslylivetemporarieshavedistinctroles.
Bindthelogicalarray/type/fielddescriptorsbeforeanymappedaccess.
Bothoperationsusefreshgenerationsinthesameway.
Before using a new generation, if G_tag is
all ones run the exact renumbering of Section6. Increment G_tag bit-serially
and copy it into the owner's epoch; mark that owner active. NO per-cell
clear is performed. All its old ROWtags differ from the fresh generation,
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
 - Ifactive,copyitsOLDepochintothecountedRAWbackup. ForEACHofitsdeclaredRsmall/Rbig
   rows,snapshottheequalityofOLDrowtagandbackupinonehelperbit.
   Ifunequal,RAW_CLEARallWrowvaluesinthatrow;ifequal,keepthemall.
   Thenstampthatrowtagwithj+1,paddedtoe bits. OnlyafterALLrows
   areprocessedsettheowner'scurrentepochtoj+1.
 - Ifinactive,clearallitsvaluebits,rowtagsandownerepochto0.
Then set G_tag=A, clear/reuse the backup, and resume the requested ALLOC.

ForEVERYmainn>=4096,r_phys<rho+1<=65rho/64,so
 A=A_small+4096<=266304rho<2^19rho.
Hence log2(A+2)<20+log2rho<4rho<=e:
at64,256>26,andthegapderivative4-1/(rho ln2)>0 thereafter.
ThusA+2<2^e atEVERYmainlength,soeachowneridentifier fits in e bits and there is room for another generation. This is a finite
exact reencoding of the SAME logical record, including unwritten cells;
it adds no abort, accepted event, source request or probability error.
It clears stale generations even in inactive owners. Afterward every
stored tag is at most A, current active epochs are j+1, and G_tag=A.
Until the next renumbering every new generation exceeds all prior tags.
Inductively ALLOC's unwritten cells always decode0; WRITEclearsastalerowbeforestampingthe
currentowner generation; FREE cannot expose stale data. Repeated wraps
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

Define pi by decoding active logical arrays through their current epochs,
keeping P's logical control/object bindings and mapped quantum registers,
and forgetting all physical-only tags/allocator details/junk. Thus the
conditional P state for logical record c is the mixture over every z
with decoded record c, not one selected physical history.

Initially this gives P's prescribed input and zero scratch. On a basis
branch, each logical READ returns exactly its decoded bit. RAW Z reads
leave a CQ state unchanged nonselectively; they may reveal a branch
label to a short helper, which is then forgotten. OnastalerowthedecodedlogicalvaluesareALLzero,independentlyofraw
junkthere. ClearingthatROW'srawvaluesbeforeitsfirstwriteonlyforgets
physical-onlydata. Evenifjunkiscorrelatedwiththereferenceorthe
mappedPquantumstate,pi alreadytakesitspartialtrace; trace-preserving
rawresetandforgettingcannotchangethereducedretainedstate. Stamping
afreshrowafterthatclearactivatesonlyzeros,andthefinaltargetwrite
hasexactlythelogicalWRITEaction. Rowtagmatchesleaveallotherbits
unchanged. No conditioningonretainedhelperoutcomesisasserted.
Boolean updates and
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

TypedaddressingisapointwiseinjectiveencodingforeachLIVElogical
arraybinding. BIGrolealiasesneveroverlapby3.2;retainedphaseoutputs
haveSMALLdestinations. Droppingtemporarybindingsandlaterreusing
theirrawregionsisexactlythelogicalforgettingchannelalreadyproved.
Thetype/rowbasearithmeticreadsrawpublic/bindingdescriptorswith
ordinaryknownaddresses;itdoesnotconditionthelogicalsourceanalysis
onextrahelperoutcomes. Arraydomain/row/fieldidentitiesareunchanged.

In particular the FULL virtual Sections3-12 establish unconditional
whole-secret recovery at least1-2^-8 for every N,s: their latent-label
and LE coupling, conditional incidence/fiber bounds, fresh-child/source
and high-confidence caps, both all-modulus decoders and finite tester
are all present. No prior review is a theorem premise. We do NOT claim
their held-out-bit failure bounds conditional on every new helper
measurement transcript; those extra outcomes are marginalized by pi.
The logical distribution is what is preserved. Under a different
adaptive malformed supplier model such extra measurements could matter;
no positive robustness or such transfer is asserted here.

## 8. Every classical bit and allocated qubit is charged

Ordinary classical storage consists of input N, final n-bit output,
constant-many O(n)-bit operands/addresses/current-frame fields and finite
control. Owner scans and cell/epoch loops keep only their O(n)-bit
indices and reusable bits. An e-bit epoch word is stored ONLY in the
basis bank and processed bit-serially. All P frames, numerical scratch,
labels, heaps, lists, decoder records, long counters, allocator maps
and old histories are bank records. Therefore S_C=O(n), even when
input, output and source staging coexist. No e-bit or array-sized
ordinary classical temporary is introduced.

The FULL prefix, not just occupied cells, satisfies
 S_Q<=2h+O(n)=O(D+H+n).
Use theSHARPERliteralbound,notanunspecifiedlogarithmicloss.
Withrho=sqrt n andmu_tree<2rho,
 kappa=ceil(log2mu_tree)+3<log2rho+5,
 2kappa<log2n+10,
 Lam+kappa=w+2kappa+1<mu0rho+log2n+12.
ConsequentlyRsmall=O(sqrt n*2^(mu0sqrt n)),
Rbig=O(n*2^(mu0sqrt n)). SinceA_small=O(sqrt n),
G_big=4096andWrow=O(n),B=(A_small*Rsmall+G_big*Rbig)Wrow
 =O(n²*2^(mu0sqrt n)).
AllallocatedBIGowners,unusedrolesandretainedSMALLownersareincluded.
Lrows*e=B*e/Wrow=O(B/sqrt n).
D=B+Lrows*e+(A+8)e+A+H+2^21*n4=O(B):
remainingpolynomialregionsfitbypositiveleadingmu0.
Retain this explicit raw bound rather than hiding its polynomial:
 S_Q=O(n^2*2^((5999/10000)*sqrt n)).
mu0=5999/10000 is exact; all polynomial additions and prefix rounding
are counted. This sharper upper envelope is asymptotically below the
older pure3/5 envelope, but is not a practical-size memory assertion.
Original quantum pools, all tags,
owner words, values, obsolete junk, free flags/bindings, backup, unused
padding, fair-bit/source scratch, growth/initialization and cleanup are
included. Bounds do not depend on labels being numerically correct or
on how many retry histories were realized.

## 9. Explicit finite helper completion and charged cost

Use the following finite bitcode completion. Constants below depend
only on this fixed program and the fixed component formats, never on
N,s,n,branch data, row counts or retry history. All addresses, counters,
epochs, fields and source/gate descriptors have at most c*n bits for a
fixed c by Sections3-4. In this section the deliberately loose bounds
A=O(n),e=O(n),Wrow=O(n),H=O(n²) are used. The tighter square-root owner
and epoch bounds are needed for space, but not for these costs.
The full physical address debit is at most c*n per elementary bit,
gate, measurement or classical Boolean action. This debit is included
at EVERY level of the following accounting, including loop arithmetic.

The driver holds only a constant number of O(n)-bit operands, raw
addresses, a current-frame owner/location, opcode and helper loop
indices in ordinary storage. These are the existing current operands,
not a table indexed by n. Suspended call contexts, return addresses,
long words not currently staged and all arrays stay in counted banks.
The current frame's raw descriptor address is known BEFORE a logical
operand fetch: it is obtained from the driver/current-frame register
or from a raw return-link field. The descriptor array is a counted raw
metadata region at fixed, directly computable addresses, as in3.1.
Fetch the owner/type/row/field binding from that raw region into the
current constant-size operand bundle, then enter the row helper.
A row helper NEVER calls a logical fetch to find its own handle or
recursively invokes the interpreter. Loop indices remain current
short operands until the helper returns. Copy out any retained result
before reusing that bundle. Thus this staging convention is acyclic;
it does not assume unit-cost access to a banked operand or a growing
ordinary-classical call stack.

Here is the complete helper hierarchy and its worst-case charged work.
RAWADDR computes a fixed affine/product/quotient/remainder address
from O(n)-bit current fields using ripple addition and schoolbook
multiply or long division. A fixed number of such operations costs
O(n²) Boolean iterations, hence O(n³) WITH the full address debit.
RAWGET/RAWSET use RAWADDR and one measured-basis read or reset/write;
raw metadata flags, row tags and counted backups use these operations.
No RAW operation consults logical storage, allocates a generation,
calls a source, or invokes another level of interpreter dispatch.

ROWGET obtains the row base for the fixed SMALL/BIG type and compares
at most e raw tag bits with the staged/current owner's epoch. The
epoch itself is read as at most e raw bits from the fixed owner-header
region. Thus O(n) RAW actions suffice, or O(n^4) charged work. It returns
zero on mismatch, else reads the selected raw value bit. ROWSET makes
the same test; on mismatch it clears all Wrow=O(n) raw value cells in
this row, copies e tag bits, then writes the selected bit. It too costs
O(n^4), not O(n³): the O(n) row loop multiplies the O(n³) RAW bound.
This correction explicitly counts address generation for EVERY clear
write. No logical operation or source step interleaves with row
activation. Matching and stale cases spend at most the same bound.
All component normalization and the two typed row-base formulas use
only a fixed number of RAWADDR schoolbook operations at this level.

WORDGET/WORDSET stream at most c*n bits through ROWGET/ROWSET into or
out of one current word. They cost O(n^5); extra loop arithmetic costs
only O(n³). Numerical Boolean operations on the current constant-many
words use fixed ripple/schoolbook bit loops, O(n³) charged arithmetic,
plus O(n^5) for their input/output word transfers. No simultaneous
polynomial-size array is staged in ordinary memory.

RAWMETAWORD streams at most c*n raw bits, cost O(n^4), without logical
row access. OWNERDIRECTORY scans at most A=O(n) fixed-format records,
using RAWMETAWORD and current comparisons, cost O(n^5). It does not
scan Rsmall,Rbig,Lrows or B. ALLOC_SMALL uses this directory scan;
ALLOC_BIG uses its fixed, inactive role. Both bind at most512 fixed
component descriptors of O(n) bits and an epoch/header; raw binding
work is O(n^4). Epoch increment/copy is O(n) RAW actions, O(n^4).
FREE drops raw bindings and ownership, and has no whole-row scan.
The finite overflow branch is excluded from these helper bounds and
charged separately below; the exact Section6 algorithm still runs.

QPOOL scans H=O(n²) fixed raw records using RAWMETAWORD, and hence
costs O(n^6). Reservation or release of at most O(n) wires per original
source/primitive event can conservatively rescan the pool per wire,
O(n^7). Known physical slots are then reset, measured, swapped or
acted on at their charged O(n)-bit addresses. Wires carrying unknown
states are transferred by handles/SWAP, not copied; pool management
never measures a retained unknown register. Original entangled gates
and source moves use exactly these located wires and current finite
descriptors. Scratch allocation of a fixed primitive follows this
same O(n)-wire bound; larger loops are explicit old program events.

OPCODE fetches a constant number of raw context fields, stages a
constant number of logical words by WORDGET, executes the appropriate
bit/gate/arithmetic/array/scope operation above, and stores a constant
number of words by WORDSET. A push/return writes/reads raw frame
links and banked context words, then updates the known current-frame
address; it does not recursively interpret a helper. A combined
array/gate primitive has at most O(n) current wires/fields to visit.
Even allowing an additional O(n) outer dispatch/field sweep over the
O(n^7) pool path, this costs O(n^8). Fixed512-component format factors
are constants. Choose the conservative uniform bound O(n^12) for
EVERY finite helper event, including the full physical address debit.
There is no hidden exponential scan or unspecified polynomial here.

For clarity the nonrecursive call graph is
 OPCODE -> WORD/OWNERDIRECTORY/QPOOL -> ROW/RAWMETAWORD -> RAW.
Directory and pool records are raw; neither calls OPCODE or WORD.
WORD calls ROW but ROW never calls WORD. RAW terminates at staged
schoolbook arithmetic and direct physical bit/gate actions. A current
source request is executed only at OPCODE, never inside a helper.
The source's LE, VEC, sort/heap/list and decoder length loops remain
explicit P loops, not subcalls inside RAW/ROW/WORD. Flat sorting and
GLOBALBIG roles satisfy the lifetime certificate of3.2.

Now count how often the helpers execute. Let C_P count the actual
original bit/gate/explicit-control loop operations, and let T_P include
all their full charged work; in particular C_P<=O(T_P). A fixed finite
ripple/schoolbook decomposition of a current O(n)-bit word operation
uses at most O(n²) elementary iterations. Streaming their operand and
control fields and decoding a current O(n)-bit instruction uses at
most O(n²) extra visits per iteration, so O(n^4) visits per old event
is a safe upper bound, even when the old bit loops were already charged.
Long records remain banked; these are visits, not extra ordinary space.
Use this explicit DRIVER completion to count helper INVOCATIONS.
The driver has a finite opcode tag and current frame/operand bundle.
For a source bit/gate/control step it stages the fixed fields, invokes
that complete OPCODE helper, stores its constant-many results, then
moves to the old program's next instruction/control state. Branches,
array-loop tests/increments and call/return instructions are old P
control steps counted in C_P. Expanding a current word arithmetic or
gate-generator step into fixed ripple/schoolbook visits uses the n4
allowance just proved. Each such visit invokes a constant number of
complete helper routines from the acyclic hierarchy, not a separate
interpreter for each physically touched directory/pool record.

More explicitly partition the finite driver tags as follows.
BIT and WORD fetch their fixed source/destination bundles, execute the
appropriate row/word operation and return one current result. ARITH
and COMPARE have fixed finite arithmetic opcodes; their current-word
Boolean iterations may be explicit visits, at most n4 per old step.
GATE and MEASURE stage a fixed gate tag and the current wire handles,
then execute the located old primitive and its exact instrument.
SCOPE_ENTER/SCOPE_EXIT bind/drop the finite owner families for that
old call, return or array allocation. A larger repeated family list
is the old P control loop and counts a step per iteration. Each scope
has at most512 fixed formats, so its current constant-size family
bundle causes only a fixed number of complete helper invocations.
SOURCE locates its O(n) destination wires and performs the one old
request plus SWAP/transfer; its per-wire pool loops are INSIDE QPOOL
and the n12 charged event allowance, not extra source requests.
RETURN fetches the fixed raw link/current result bundle and updates
the known frame address; its fixed context words are streamed through
WORDGET/WORDSET. It does not scan or unwind every live frame at once.
INITPOOL/RELEASEPOOL perform any original H-slot reset/reservation
completion not already in an old primitive; charge at most O(H+1)
extra events. Array identity, scope and type determine the finite
opcode's operands; no dynamic code list is materialized.

Inside each of these complete events, raw directory scans, pool scans,
per-wire reservation, component-field loops and row tag/clear loops
are exactly the operations included in the helper costs above. Their
loop bodies may call lower helpers, but these lower calls are charged
inside that event's n12 cost. They never dispatch a new logical source
opcode, invoke VEC, append an unbounded continuation stack or enumerate
an exponential logical array on allocation. Each such event returns
to its caller in the fixed finite hierarchy. This is the acyclic
code completion already specified, now with an explicit event boundary.

Conversely any repeated long source operation is an old P loop and
increments C_P for each logical step. Only currently staged O(n)-bit
operands have arithmetic loops added by the compiler; n4 covers their
fixed decomposition. Original array output copying, leaf table fills,
sort/heap/list scans and decoder loops are not silently absorbed into
one event; they are retained old bit/control operations. Source calls
count Qcap as well even if already included in C_P. Each logical
scope allocation/free is charged to its corresponding old control
transition, not to the number of owners elsewhere in the live bank.
The maximum-live-owner and typed-lifetime certificates ensure capacity;
they do not multiply the number of transitions per old step.

It follows by induction on old P control transitions (including wrong
labels, failure returns, retries and abort cleanup) that the number of
complete helper event invocations is at most
 O(n^4)*(C_P+Qcap+H+1).
At a transition, the finite driver tag performs the stated bounded
current-field decomposition and returns; long source loops use another
old transition, while internal helper loops use their already charged
local cost. The induction does not assume favorable measurement data
or bounded expected retry count: every actual old step counts until
the deterministic caps stop it. Calls push one bounded frame bundle;
returns restore one bundle. The original depth bound controls space,
not an uncharged multiplication of event counts.

Multiplying by the explicit O(n12) CHARGED cost of each complete event
therefore gives O(n16)*(T_P+Qcap+H+1), since C_P<=O(T_P).
The directory/pool/field bounds were already included in n12; charging
an extra n16 event multiplier for them would count their work twice.
This sharpened count follows from the specified driver boundary and
complete helper loops, not from ignoring any raw physical instruction.
Startup initializes the ENTIRE fixed paired prefix, including every
inactive owner/row/value/tag/backup and padding wire. Output-first
cleanup resets it completely. A raw streaming scan uses O(n³)*D
charged work including loop/address arithmetic; O(n^12)*D is a safe
explicit allowance for both scans, raw descriptor initialization and
fixed input/output preparation. There is no uncharged allocation.
Thus, when no renumbering occurs, total charged time is at most
 O(n^16)*(T_P+Qcap+H+1)+O(n^12)*D.
This is a specified finite completion with explicit bounds for every
helper case, not an assignment of a convenient unspecified exponent.
The ordinary staging remains O(n) throughout all these nested loops.

There are at most O(n^20)*(C_P+Qcap+H+1) new generations, by the same
fixed control/frame/array-scope accounting; loops generate work, not
ordinary O(n^20) scratch. All old branch budgets are at most a fixed
polynomial times2^(tau0*sqrt n).
Thus the logarithm of the number of new
generations is O(sqrt n), uniformly over EVERY branch. In contrast theactuale=4ceil(sqrt n) isatleast4sqrt n.
The eventbound givesnumberofgenerations+A+2<=C*n^P*2^(tau0sqrt n)
forfixedabsoluteC,P,sinceC_P isboundedbythefullchargedsourceT_P,
Qcap<=poly(n)*2^(2sqrt n),andH/A arepolynomial.
Thereforelog2(numberofgenerations+A+2)<=tau0sqrt n+Plog2n+log2C.
Here tau0=H00<2<4. Thepositivedifference
(4-tau0)sqrt n dominatesPlog2n+log2C,eventuallystrictly.
Thusnumberofgenerations+A+2<2^e eventually,withoutrequiringe/sqrt n
todiverge. This is an all-branch analyticboundwithfixedconstants.
For all sufficiently large n the entire run
uses fewer than2^e-A-2 generations, so G_tag never reaches its maximum
and NO renumbering occurs. This is an ANALYTIC eventual fact, not an
unchecked all-input assertion or a new runtime guard.

For every remaining fixed finite length, the original program has
finite deterministic source/fallback/loop budgets, and each actual
overflow is repaired exactly by Section6 with finite fixed D. Every
logical allocation triggers at most one such finite scan and then makes
progress. Thus correctness, termination and fixed storage bounds hold
even on those earlier branches. No failure event is hidden or excluded.

## 10. Actual .5999 quarter-boost bounds with the complete polynomial ledger

The supplied complete source uses EXACT mu0=5999/10000,
H00=38662667/23996000,tau0=H00,w=ceil(mu0sqrt n),
v=least integer withv^4>=n,nu=v,gamma0. Public square tests are
100000000*w²>=35988001*n; binary search uses constant-many
O(n)-bit words and polynomial work, not a real-root oracle.
Full virtual7 supplies all .5999 height/capacity premises B1-B7,
withhmax<H00sqrt n-v+6 andmu_tree<2sqrt n. Full source/guard/
filtration/decoder instruments remain supplied and are not replaced
by an absent artifact or a prior accepted profile.

The ACTUAL source cap includes A_leaf=kappa+1+nu=O(n^(1/4)),
K=O(sqrt n),J<=n,a2<=n, hence
 Qcap=O(n^(7/4)*2^hmax)
 =O(n^(7/4)*2^(H00sqrt n-n^(1/4))).
Every unsuccessful,partial,rejected,discarded,retry and aborted
request counts. Full deterministic11.2 retains the A_leaf denominator
in merge/table workperqueryO(n²2^v/A_leaf); it cancels against
Qcap=O(n^(3/2)A_leaf2^hmax). Thus corework is
O(n^(7/2)*2^(hmax+v)),and the full O(sqrt n) address debit gives
 T_P=O(n^4*2^(H00sqrt n)).
LE,decoders,partial terminalLEAFs,one global clear and setup are
included separately in complete virtual13 and fit this same bound.
This is all-branch deterministic accounting,not an expectation or
a changed source instrument. The height constant6 affects only an
absolute outside factor.

All typed SMALL/GLOBALBIG row and live-width capacities are retained.
Their proofs usemu_tree<2sqrt n,arity<=4 and positive mu0>=2/5;
the stronger .5999 value preserves the old numerical LOWER margins.
Full actualH=O(n²),D=O(n²*2^(mu0sqrt n)) follow from3-8,
including both+32 paddings,all inactive rows,tags and unknown wires.
The explicit9 ledger n^16*(T_P+Qcap+H+1)+n^12*D therefore gives
 T=O(n^20*2^(H00sqrt n)).
The query term's power71/4 and exponentH00sqrt n-n^(1/4)
fit the source term. Prefix coefficientmu0<H00 and polynomial
unknown-pool coefficient0<H00 fit their positive exponent gaps.
Exact source transfers preserveQcap one-for-one. Thus jointly
 S_C=O(n),S_Q=O(n²*2^((5999/10000)*sqrt n)),
 Q=O(n^(7/4)*2^((38662667/23996000)*sqrt n-n^(1/4))).
Every address,generator,source,lifecycle,tag repair and cleanup action
counts; zero initialization,metadata and source SWAPs are not copies.

Epoch widthe=4ceil(sqrt n) and H00<2<4 give eventual no-wrap
with all fixed polynomial event constants; exact finite overflow
repair handles every earlier length without extra failure or source
request. The original finite tester and exceptional lengths change
only absolute outside constants,not the selected execution or claims.
No lower bound,priority,optimality or practical-size claim follows.

## 11. Exact indices and joint theorem scope
Positiveleading sqrt-n terms giveindices1/2,0,1/2,1/2;
ordinaryn hasindex0andcanonicaltolerance0retainstheideal-copylaw.
TheONEactualtypedpoolimplementationhasallfourboundsonEVERYbranch,
includingwronglabels,failure/retry/abort/initialization/cleanup.
ThecompleteSMALL/BIGcapacity/lifetime/normalization/rowtag/finite
overflow/CQ/source/chargedcostargumentsaresuppliedwiththefull
virtualsource/filtration/cap/decoders. Everyinactiveowner/row/value/
tag/metadata/backup/pool/source/helper/paddingwirecounts.
Nohistoricalverdict,externalartifactcomparisonorgraphstatusproves
amathematicalclaim. Alloriginalmethodandauthorcreditsremain.
