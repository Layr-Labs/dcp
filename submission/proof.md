# PARTROOT197-Q1: uniform partition sieve with ordinary arrays and a fully counted quantum pool

## 0. Onealgorithm,jointclaim

For everyN>=2 ands moduloN,n=ceil(log2N),thissingleuniformphysical
algorithm recovers theENTIREsecret withunconditionalprobability>=1-2^-7
fromindependentidealcopies. JointlyonEVERYbranch,
 T=O(2^((141421357/100000000)sqrt n)),
 S_C=O(2^((141421357/100000000)sqrt n)) ordinaryclassicalbits,
 S_Q=O(2^(sqrt n)) fullyallocatedqubits,
 Q=O(2^(sqrt n)) totalacquiredcopies.
Thecoefficientsareexact141421357/100000000fortime/classicalspace,1forquantumspace/
samples,withabsoluteoutsideconstants. Allfourindicesare1/2. Clean0
requires independentidealcopies;it assertsnopositiverobustnessorimpossibility.
Allfailure/discard/retry/partialattempt/abort/finitecompiler/source/initialization/
address/allocation/cleanupcostsandallinactivequbits areincluded.

## 1. Completeprogramandscope

The completevirtualP in virtual.md supplies sourceidentities/transforms,
LE,linearMERGE,growingodd-partitioninstrument,actualintegerprofile,
conditional lowbitlaw,odd/fullmodulusand2-adicdecoders,allcaps and
uniformcompiler/rate/capacity/failure/resourceproofs. It ispartofTHIS
archive;no oldverdict or absentpaper suppliesapremise. Runexactlythat
P,withitsknownbits as ordinaryclassicalbitarrays anditsunknownwires
realized bythefixedquantumpool2below. No generation-tagged measured
basisbankor quantumencodingofknownclassicaltables isexecuted here.

At n<2^512 runthe fullstreamingtestvirtual13:classicaln-bitcandidate,
up ton+10freshshiftedXtestspercandidate,firstminusrejects. Itspeak
ordinary/quantumworkspaceO(n),error<=2^-10andfiniteallbranchcaps
satisfythejointenvelopesafterfiniteprefixconstantadjustment.

At n>=2^512,publicr=ceil√n,k=leastodd>=ceil(n^(1/8)),
L=ceilLogn,M7=ceil(n^(7/16)),s0=r-32M7,m0=min{j:2j²>=2n-s0²},
m=dl=m0+16L,ell=s0-m,K/kappa/q/F/Y/Ci
are EXACTLYvirtual7/8. UseQcap=4nC0+K. Parameterwords andcanonical
macrocompilercountershave<=O(n)bits;alllonglabels/tables/frames/
profiles/free/ownershiprecords belowareordinaryclassicalbits andARE
counted inS_C. Currentarrays arefinite withpubliccapacities;bitreads/
writes useknownclassicalindices under the chargedaddressmodelvirtual2.
No quantumaddressedRAM,unpaidlookup,arbitraryrotationor gatecacheisused.

## 2. Fixedwholequantumpoolandexplicitindexedlifecycle

AllocateBEFOREsources the WHOLEpublicprefix
 H_Q=C0+2^20*n^16+16n²+n
zeroqubits,includinginactivepadding. Reset/initializeeachwireonce,
payingitsfulladdresscost. Thisprefixincludesalllocalunknownsource/
pool/index/lookup/ripple/LE/transform/macro/cleaningwires. A freshsource
copytemporarilyarrivesonn+1additionalwires,ALSOcounted,thenisSWAPped
intoallocatedzero slotsanditsincomingwiresreset/released. TheseSWAPs/
resets arecharged. Everyacquisitionisexactlyone originalguardedrequest;
zeroancillas andSWAPsare notsourcecopies. Totalpeakquantumallocation
is<=H_Q+n+1;noinactivewireor sourceinputisomitted.

Classicalmetadataordinaryarraysstorelive/freeflags,nextfreeindices,
currentwirehandlesandcontrollerownershipbindings forH_Qslots. Allhave
fixedfieldwidth<=O(n),becausevirtual8logC0<=2r<n andlogH_Q=O(sqrt n+log n).
Initializationofthe WHOLEmetadataarrays ischarged. Maintainhead of
freelistandvirgin counterv,initiallyhead=null,v=0. allocate():ifhead
nonnull poptheknownnextfreeword;else takevandincrementv. Bindthe
returnedzero slot tothecurrentlogicalwirehandle. release():onlyafter
allcurrentownershave surrenderedthatlogicalwire,measure/resetitand
pushitsknownindex ontothefreelist. allreleasedwiresarezero. The
virgin counterneverexceedsH_Q;allfields arefixed-width withnocounter
wraporepochargument. ThereisNOwholepoolscanperallocation/instruction.

Ownershipismove-only. SourceVECframes andpoolrecordsreferonlytolive
handles. Newoutputvectors transferownershipoftheretainedindices;
PARTLEVELoutputs keeptheirpivotindices andreturntheirunmergedinput
identities. Reset/releaseonlycleared/privatewires ordiscardedowned
inputs,afterallparent/childaliasreferencesareupdated. As in the
suppliedP,nestedframes onlyretainownedsourceindices;thevirtualinput
sets toMERGE andeachmacroaredisjoint. Sorting/ties usevirtualrecord
orderandorigins,NEVERphysicalslotnumbers. Recycledphysicalindices
thereforecannotchange P'slogicalorderingorreturn-state law. No stale
handleisread:itslastownererases/transfersitbefore release. Pooloriginfieldsare originalsource-acquisitionordinals<=Qcap;output
pivotskeepthosefields. Privatewirehandlesarecurrentframe-localnames.
Allremainingloopcountershavepublicfinitewidths<=O(n);noglobal
unboundedlifetimecounterisrequired. Slotnamesreuseonlyafterallbindingsend.

Thisis a concrete indexedallocator,notafreeallocationoracle. Ordinary
known-indexbitreads/writespaytheirfulladdressdebit,andanywholeword
access/copy/arithmeticisexpandedintochargedbitsteps. Constant-many
operands peroriginalelementarygate/bitstep makebindings/lifecycle
costO(n²) perstepconservatively,includingtheiraddresses. ExtraSWAPs
areemittedonewireatatime;theirfulladdresscostcounts. Anoriginal
multi-bit operationretainsitsoriginalbitloops. Classicalphase-table
LOOKUP controlledbyunknownindicesisSTILLtheexplicitlinear-row
Clifford+T circuitvirtual6;ordinaryclassicaladdressingdoesnotturnit
intoQRAM. BooleanmacrofunctionsareSTILLtheexplicituniformonline
compilerchargedbyvirtual7/14.

## 3. Capacityandreference-preservingimplementation

Virtual14holdsthepoolat<=C0. Retainedsourceindicesareatmost
2(m+1)(dl+m)<=16n². The explicitlysuppliedlookup/ripple/LE/transforms
useO(n)scratch,coveredbygigantic2^20n16. Growingmacroancillasare
<=8F<=n byvirtual7.4. Theprogrammayusepoolwiresasaninputview,but
doesnotallocate asecondcopyofthem. These inventoriesjustifyH_Q on
EVERYbranch;currentqubitcapacityneverrunsout. Sourceincomingn+1
arecountedseparately. Allparameter/owner/tuple/canonicalmatching
arraysholdclassicalknownindicesorbits,notquantumcopiesofunknownstates.

For correctness,conditiononanyclassicalrecordr. Aknownbinding maps
currentlogicalunknownwires injectivelytoallocatedphysicalsLOTS;the
jointphysicalstate,includingarbitraryexternalreferences,is the
virtualstate underthatknownwirepermutation withunusedwireszero.
Metadataarrays/labels maybecorrelatedwithquantumdata;noindependence
isassumed. Allocationaddsazeroandknownbinding. Gatesredirecttheir
knownoperands,sourceSWAPs transferthewholejointstate,measurement/reset
anddiscardapplytheidenticalinstrument,andmove/releaseupdateonlythe
knownbindings afterP'sownownershiptransfer. Eachstepcommuteswith
thisdecoding. Summingoverrprovesthecomplete correlatedclassical-
quantumchannelwitharbitraryreferences,notjustitsbasisdistribution.
Thereisno cloning,coherentmeasurementofclassicaldataorfreeerasure.

ConsequentlythelogicalPoutcomes,returnedstates,root/discard/caplaw
andguardedsource-requestsequenceareEXACTLYpreserved. Itsconditional
lowbitfieldmarginalizesthefullhigh-label/arithmetic/gate-description
records asvirtual10specifies;ordinarybookkeeping doesnotcondition
thoseinto G. Virtual13thusprovesunconditionalwhole-secret success
>=1-2^-7forTHISrealization. No acceptedhistoryisusedasapremise.

## 4. Full charged ledger and exact selected envelopes

Virtual8 gives Y<=r-20M7<=sqrt n-19M7 and u=2m+2.
Virtual14 proves Qcap=O(n2^Y), T_P=O(n20*2^(u+16F)),
SCvirtual=O(n³2^u). Long arrays, tables, frames and allocator maps
are ordinary SC. The whole allocator metadata costs O(nH_Q),
including inactive capacities. A conservative ordinary SC bound
O(n32*2^(u+16F)) covers every record and exact parameter word.

The ENTIRE zeroed H_Q prefix plus n+1 source wires count, so
 SQ<=H_Q+n+1=O(2^Y+n16).
Initialization/cleanup/reset of the prefix costs O(nH_Q), metadata
initialization O(n²H_Q), and each original bit/gate/lifecycle event
has O(n²) driver cost. Source transfers cost O(n³Qcap) conservatively.
Together with original chargedP this yields
 T=O(n32*2^(u+16F)).
Addresses have O(sqrt n+log n)<=O(n) bits; all quantum LOOKUP rows
and uniform macrocompiler bitloops remain explicit. There is no
wholeH_Q scan per event, unpaid advice or favorable-branch ledger.

Virtual8.9 gives u+16F<=sqrt2*sqrt n+208M7, with M7=ceil(n^(7/16)).
Thus jointly T,ordinarySC<=C*2^[sqrt2*sqrt n+512M7]. Virtual15
proves the strict rational gap to c=141421357/100000000 and hence
 T,ordinarySC=O(2^((141421357/100000000)*sqrt n)).
The NEGATIVE sample marginY<=sqrt n-19M7 absorbs all fixed quantum/
source polynomials, proving jointly SQ,Q=O(2^sqrt n). These are
exact exponent coefficients, with only absolute outside constants.
No exponential compiler is treated as a constant at equal leading
coefficients. The finite tester changes only outside constants.
All four indices are1/2. Full source/record/arbitrary-referencechannel
correctness is established by2/3 and virtual13, not an old verdict.

## 5. Precisematerialprovenanceandlimitations

Sourceframework/overlap/coin-erasure/unchangedreturns directlyadapt
kshitij-hashTRIAD125 actualf5b375dd-1e5c-4728-95dc-b855b2dc5827,
archive965917f88ec25ccab3d9ce78e07c717a1590a54f. SeparatelyconsultedG4
actualb48a1af4-3e6b-45d7-8cdb-a414739ddc21,archive
0cca4a7452d2b18eea6c3ba24ac8123ce7fa2886,inspiredmultipleoutputs and
random-consumptionproof. The indexedhead/virgin/next/ownershipmethod
isadaptedfrom6c0e2efd-41bd-4018-a24e-e386f3069c9b,archive
f0fbd85526d7db908a14887ad9ab3cdb7ab602bd;HERE itsmetadataareordinary
classicalarraysandtheexplicitresourceledgerisrederived. Reduced-
field/reached-attemptcostproof usesdb6af0c1-2762-4fd4-a5ea-d78910d65cb1.
Arbitrary-reference/correlated-recordchannelproofprinciplewas separately
consultedinfbb8f36c-3904-4bf0-9ddf-e9f5d83657ae,archive
100a8e307fd90c489c4d90717613869fed576b3b;itsmeasuredbasis-bitbank,
quarterprofileandresourcecomparatorareNOTselectedhere.

Public18574ff1ce3-b5ce-48f1-a153-640c223b8ab0/public188
9fe91c4a-7574-4d0f-8bf1-4df2b1ca2eae supplythevirtualframework/
profile/positivegapaccountingworkinglayout;public186
 da050be2-d8cd-4124-9d6c-4efc2ed5883b suppliesfiniteidentitycaps/
uniformprefix;public1891e083775-5d0a-4070-bcdc-ded8ada75d3a supplies
partitionmultiple-output/disjointincidenceworkingproof. Theirgeneric
measured-basisbankimplementationsandliteraloldprofilesarenotrun.
Public19038897382-d7d7-44fe-8205-64ad028a41a5(archive
91c5c2f1bc11f25768459d9192e92dfec018ecb2)andprivate191/193/194supplied
odd-family/growingcompiler/profileworking
proofs. Addactualmateriallinksafterpublication,nofakeUUIDs/verdictpremises.
Generation-tags/finitetag-epochrepairfromfc8isNOTpartofthisordinary-
arrayprogram;classicalfieldsinsteadhavepublicfinitecapwidths. Its
methodisnotdeclared asusedmerelybecausethewrappersusedit.

Thisis a differentSC/SQtradeoff,not a claimtodominatelinearordinary-
spaceorpolynomial-qubitconstructions. Hugefixedcutoffgrowingcircuits
areexplicitlypaid,not practicalhardwareclaims. No priority,general
measurementoptimality,matchinglowerbound,cube-rootworkor positive
corruptiontoleranceisclaimed. Everyneededargumentishereandvirtual.md.

Working provenance update: private195 supplied the ordinary-array/fixed-pool
channel and ledger; private196 supplied integer-root/slack/subleading
proof presentation. Current new actual Q1 schedule differs from both.
Neither unreviewed work nor predecessor acceptance proves this program.
Add actual direct material links only after publication inspection.
