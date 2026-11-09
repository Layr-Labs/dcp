# Exact fixed odd-partition macro ODD

This is a self-contained reproduction/adaptation of PARTROOT196 virtual.md
Sections7.1-7.2 (public commit34211deace09bfd907619767f8aa5fa30ba44114).
Here k=10000000000000001 is a FIXED odd integer, h=(k-1)/2,
and w=1/[h(h+1)] is a LOCAL cell weight, distinct from proof.md's key width.
A labeled input i is the equal-amplitude phase qubit with table(t0^i,t1^i).
Its phase parameter th is common to the batch. Inputs have equal difference
keys modulo2^(p+c), so each pair difference is collimated to p+c.
Toffoli, NOT, CNOT, H, computational measurements and resets are the only
quantum operations; Toffoli has an exact fixed Clifford+T decomposition.

### 7.1. Complete uniform cell family,poststates and rate

A-cell:chooseoneunorderedoddpair,leaveotherk-2coordinatesfree,weightw.
Forj=0,...,h-1,J_j-cell:partitionallkcoordinates intoj unorderedoddpairs
andoneall-equalremaindergroupofsizek-2j. Itspercellweightandcountare
 w_j=(1-w*j*(k-j))*(k-2j)!/(k-j)!,
 N_j=k!/(2^j*j!*(k-2j)!).
CanonicalenumerationlistsA,J0,...,J_(h-1),thenlexicographicsortedpairlists;
the remainderis theircomplement. Thisnames eachcellonce. The formulas
are uniformfiniteinteger/rationalalgorithms givenpublick,notadvice.
Computefactorialproducts/rationalreductionsserially;donotstorethe
entirecellfamily or its truth-table history.

LetPi_cell projectontothecomputationalcell. IfxhasminorityHammingweight
t<=h,thereare t(k-t)containingAcells. A J_jcontainsxonlyifj=t orj=k-t;
forj<h onlyj=t<hispossible. Thereare (k-t)!/(k-2t)! suchJ_tcells:
matchthe tminoritybits todistinctmajoritybits,leavingequalbits.
For t<h,totalweightis
 w*t*(k-t)+[(k-t)!/(k-2t)!]*w_t=1.
At t=h,Jcellsareabsentandw*h(h+1)=1. Allweightsarenonnegative.
Therefore sum_cell w_cell Pi_cell=I onEVERYoneofthe2^k basisinputs
andalljointstates. The normalizedKrausoperatorsaresqrt(w_cell)Pi_cell.
This is an all-kidentity,not a finite LP/empiricaloptimalityclaim.

On productequatorialinputs,a cellwithLindependentbinarycomponents
hasprobabilityw_cell*2^(L-k),independentofphases,labels,secret,past.
Thus the typeprobabilitiesare
 P_A=choose(k,2)*w/2=k/(k+1),
 P_j=N_j*w_j*2^(j+1-k)=2^(1-k)*choose(k,j)*(1-w*j*(k-j)).
They sumto1 bycompleteness. This is the sameconditionaltypelaw at
EVERYreachedmacro,evenwhenlaterkeysdependonallpreviousoutcomes.

EveryconstrainedgroupGbecomesonephasequbit. Its canonicalpatternb
has smalleroddpairindex0/larger1,orall0foranequalgroup. Outputtable:
 (sum_(i inG)t_(b_i)^i,sum_(i inG)t_(1-b_i)^i).
Choose smallestwirev;CNOTv->i for everyotheri,thenXtoiifb_i xor b_v=1;
finallyXvifb_v=1. Everyothergroupwire becomeszero,andvindexalpha
selectsb xoralpha. This holds onEVERYstate supportedonthecell,
includingarbitraryreferences. Onproductphaseinputs,disjointconstraints
factor the projectionintoallgroupoutputs andunchangedfreeinputs,
inproductwith eachotheranduntouchedreferences. Nothingiscloned.

EachoddpairisGOOD:equalkeys makeDel_a-Del_b divisibleby2^(p+c).
The all-equalgroupRECYCLES atoldp,withdifferenceitsinputDelsum.
A givesoneGOOD andk-2unchanged inputs;J_j givesjGOOD andoneRECYCLED.
GOODleavesLIVE. NetLIVEcostCis2onA andk-1onJ_j;GOODcountGis1onA,
j onJ_j. Compute p=E G=P_A+sum_j jP_j,mu=E C andq=mu/p bythe
exactfiniteformulasBEFORE computing sourceC_i. These are exact fixed-k rationals, not a log oracle. G isnotBernoulli,andmay
dependonitsownC. For every odd k>=3,
 2<q<=2+7/sqrt(k),mu=(3k-1)/(k+1),p>=k/(k+1)>=3/4. (7.1)

Here is a proof ofthe uniformratebound. LetX~Bin(k,1/2),B=|X-k/2|,
T=min(X,k-X). The displayedP_j equalsPr[T=j]*(4B²-1)/(k²-1).
The j=h termis0,soitcanbe included. Independent centeredfairbits give
 E B²=k/4,E B4=(3k²-2k)/16:
expandthefourthpower,retainingthe kfourthpowers and6choose(k,2)
pairedsecondpowers;allodd/crosssingleterms vanish. Therefore
 sumP_j=1/(k+1),mu=(3k-1)/(k+1),
 p=3k/[2(k+1)]-E[4B³-B]/(k²-1),
 mu-2p=[2E(4B³-B)-(k-1)]/(k²-1).
Thisispositive:everyJoutcomehascostk-1>=2j+2 andtotalJmasspositive.
ByCauchy,E B³<=sqrt(E B² E B4)<=sqrt(3k³)/8. Hence
 0<mu-2p<=8E B³/(k²-1)<=sqrt3*k^(3/2)/(k²-1).
Usep>=3/4 andk²/(k²-1)<=9/8 toobtainq-2<7/sqrtk,proving7.1.
For our FIXED k=10000000000000001, sqrt(k)>10^8, so
2<mu/p<2+7*10^-8<20000001/10000000=RHO.
No lower bound k>=n^(1/8) is asserted or used. All parameters are
fixed independently of n. The exact controller uses the rational RHO,
not floating-point moments or an oracle for logarithms.

Alloutputentriesaresums onDISJOINTleafsets. alpha->b xoralpha is
injectiveonitsgroup;differentcomponentsusedisjointgroups,andfree
inputskeepstate,tableandwireID. The product,disjointincidence and
fullpositive3n-bitlabelinvariants thuspersist for everypublick.

### 7.2. Uniform exact dyadic dilation with its full growing cost

LetL=h(h+1). Eachreduceddenominatorofw_j divides
 L*(k-j)!/(k-2j)!<=k^(k+2). IncludingtheAdenominatorL,theirlcmD
satisfies D<=k^(k²):the productexponentis(k+2)h+2<=k².
ComputeD seriallybyEuclid/lcm. Put b_k=ceilLogk,
 coinbits=ceilLogD+2<=k²b_k+3,M=2^coinbits,
 scale=floor(M/D) in{4,5,6,7},R=M-scaleD<D<=M/4.
GiveeachcellscaleD*w_cell distincttokens,aninteger;addRidentitytokens.
Everybasisinputbelongs toscaleD+R=Mtokens by7.1. Orderallnonidentity
bycanonicalcell/copyorder,thenidentity. Thereare<=2k^(k+1)cells:
choose(k,2)<=k²,and eachN_j<=k!<=k^k,withfewerthank Jtypes.
Sincew_cell<=1,totaloutcomeIDs<4M k^(k+1),so
 outcomebits<=2k²b_k+8.
Thesearecomputedparameterbounds,not an exponentiallylargeadvicearray.

Preparecoinbitsqubitsr andoutcomebitsqubitsz inzero;applyHadamardsto
allr. f(x,r) isther-thcontainedtoken,r=0,...,M-1;XORfintoz.
h(x,z) isz'srankamongcontainedtokens,or0oninvalidpairs;XORh into r,
clearingr. UncomputeBoolean scratch,measure/resetz. Identityleaves
allinputsunchanged;otherwiseperformthe groupcleanup7.1. Decode the
measuredID bycanonicalenumeration/range-arithmetic,not a QRAMlookup.

For arbitraryjointinputsum_x|x>|R_x>,beforemeasuringzthestateis
 sum_x|x>|R_x>|0>_r (1/sqrtM)sum_(z containsx)|z>.
Rankbijectionproves this exactlyonallbasisinputs andthusallreferences.
TokenKrausisPi_cell/sqrtM,orI/sqrtMforidentity. Identityprobability
R/M<1/4 isinput-independent;conditionalonnonidentity,the aggregated
percellweightisscaleD*w_cell/(scaleD)=w_cell. Everyprivate/released
wireisclean onallinputs,without anequatorial/product assumption.

The following costbound is UNIFORMINn,not a fixed-macroconstant.
SetF=8k²(b_k+1). Itbounds bothf/hinputbitcounts,targetbitcounts,
currentmatching/counterwordlengthsandconstant-manyarithmeticoperands.
CompileeachBooleanfunctiononeoutputbitatatime:enumerateinputpatterns,
computeNOT/Toffoliequalityflag,copybit,uncomputeflag. Targetisnever
itsownfunctioninput. AtmostF2^Fterms eachwithO(F)gatesgive<=2^(2F)
elementarygates;<=8Fprivateancillas suffice,withreusableflagchains.
Toffolihas the exactClifford+T completionof2.

Evaluateeachclassicaltruthfunctionvaluebygrowingcanonicalmatchinglists,
cell-membershiptests,andtokenranges/ranks,usingO(F)currentbits.
Atmost2^Finputpatterns and2^Ftokens perpattern,and a conservative
F^16 schoolbookarithmetic/enumerationoverhead,fit2^(16F)coresteps
forF>=128. This paysfactorial/denominator/reduction/membership/rank,
measurementIDdecoding,groupcleanup/fulltablesumsandgateemission.
Multiplyingbyn payscompleteO(n)-bit known-wire/operandstaging:
 oneactualtrialcosts<=C*n*2^(16F)coresteps.          (7.3)
Onlyconstant-manyF-bitcurrentwords,packedmatchingindices andO(n)
currentwords coexist. No storedtruth-table/history,QRAM,unknown-address
memory,arbitraryrotationoracle or input-specificadviceisused.
All k-dependent setup is fixed finite work, charged by Gamma=2^(16F0),
where F0=8*k^2*(ceilLog2(k)+1). Arithmetic on the current O(n)-bit
labels adds only polynomial(n) factors. This child fixes k; it never
uses the parent's growing-k rate or lower bound as a theorem.

Each reached macro tries this circuit at most Ltry=Y+ceilLog2(n)+64
times. Identity returns every input exactly unchanged, with all reference
systems unchanged. If all trials are identity it ABORTs; otherwise it
performs the displayed cleanup and returns the normalized A/J_j outcome.
This finite implementation applies to every joint input and cleans all
released wires. A trial acquires no source copy. proof.md bounds both
the total number of starts and the unconditional identity-cap coupling.
