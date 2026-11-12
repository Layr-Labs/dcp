# Lean join word: linear record functions, one comparator flag, sequential scans

## 1. Actual Boolean words and helper lifetimes

This specifies the NEWphysicalimplementation used byRPF-PA-LQ, replacinggenericper-recordschoolbook budgets and doubling-layer scans. A record has a CONSTANTnumber of fields ofO(n)bits, including its fullm-bitpayload, signedkey/sum/quotient, presence/tag/count/rank/start and flags. Publicmaximums fromproof3/9 fix theirwidths; padfield/recordstridesto powersoftwo(lessthanafactor2), and give everyregion a publicalignedbase. No extra sourcebit or searchindex is introduced.

A binaryadd/subtract/compare uses ripplecarry/borrow withconstantmanyBoolean gatesandfreshcarrybits perinputbit. For exampleborrow forx-y is((NOTx)ANDy) XOR((NOT(x XORy))ANDborrowin); thetwo terms aredisjoint. A mux is XOR/AND perbit. Concatenation, shift/divisionbypublicL=2^r andpayloadcopy arebitwires/CNOTs. These areO(n)gateswithO(n)temporarybits. Computeintotemporary, copyresult and REVERSEthe evaluator withinputsunchanged toclearitscarry/Booleanbits. Genericn²multiplication/division is NOTreserved/executed perjoinrecord. Whole-querycarry/hash/inverse arithmetic mayuseboundedO(n²)routines separately, countedbelow.

For each bitoniccomparator encode lexicographic(paddingclass,signedkey,tag,payloadID), withsignedsignbias; fieldcountisconstant. Computeitsstrictcomparison intoONEfresh historybit, then immediatelyREVERSEALLpredicatearithmetic BEFORErecordsarechanged. OnlythatONEhistorybitpersists. ConditionallySWAPeveryrecordbitusingthatflag. The evaluator'sO(n)cleanscratchis reused bythenextcomparator. Inversefirstunswapsusingthesavedflag, thenrecomputes/XORstheoriginalpredicate toeraseitandcleansscratch. Thus totalgatecountpercomparatorO(n), historyONEbit, witha literalunitaryinverse onallbasisstates. No globallydirty-extension soundness is assumed. ExactCCX/constantcontrolsarenative1'ssuppliedClifford+Twords, notoracleoperations.

## 2. Sequential prefix, suffix and marker scans

Use JOIN-KEY/padding equality ONLY, ignoring tag/payload, for two DISTINCT boundary arrays: head_i=(i=0 OR key_i!=key_(i-1)) and tail_i=(i=M-1 OR key_i!=key_(i+1)). Padding class is part of key in both. Compute both with clean adjacent-key comparisons before either scan. B_i is 1 only for present B records. Forward scan inputs are (B_i,head_i); reverse-order scan inputs are (B_i,tail_i). The reverse scan NEVER reuses the forward head flags. Retain the reset monoid, multiplicities/output starts and rightmost PRESENT marker propagation. Change ONLYthe scanword: initializec_0=x_0 inafreshprefixrow; fori=1..M-1compute c_i=op(c_(i-1),x_i) intoa freshrow, preservingbothinputs. Eachreset/add/mux/markerop is anO(n)wordwithcleanscratchaftercopy. RetainONEprefixstateperlane, NOTalllogarithmicdoublinglayers. Suffixes use the reverse public order with the separately computed tail flags. For each lane i, forward_i=sum of B_j from its bucket start through i, and suffix_i=sum of B_j from i through its bucket end. Induction along either traversal proves these formulas: its first bucket lane resets and subsequent equal-key lanes add. Hence forward_i+suffix_i-B_i is exactly the whole bucket B count, and forward_i-1 is each present B lane's zero-based rank. Both boundary arrays remain until dependent scans are reversed, then their adjacent-key comparison words are undone. Allotherprefix uses (globalcounts/starts andmarkerpropagation) use thesamesequentialrecipe, withabsent-zero initialmarker andpresentbit checks.

Associativity impliesthese are EXACTLYtheoldprefix/suffixvalues; no inputdistributionorbucketstabilityassumption is added. The completedjoinoutputs/canonicalIDs/overflowdecisionsarethereforeunchanged. To reverse, deleteprefixstatesfromlasttofirst byrecomputingfromthepreviousstateandunchangedinputrow. Inputsarekept untilthisreversal; sortingisundoneonlyafterdependentprefixworkisundone. Records/payloads/keyties/negativekeys/caps/paddingremaincovered bynative3'sfullduplicate-joinconstruction. This hasO(M)scanrecordoperations andO(Mn)retainedprefixdata, ratherthanlogarithmicallymanyfullrecordlayers. It usessequentialwork, notfreeparallelism.

Rawsubsetlistsarefilled bycleanINPLACEadditions ofselectedquantumWlabels, controlledbythePUBLICsubsetID bits. Eachn-bitadd iscomputedas a wholewordpermutation withcleanripplehelpers, reversedbysubtraction; no sequenceofrawpartial-sumhistoriesisretained. The finalunreducedsum/payloadis stored perrow. The globalbitwidth preventsvalidsumoverflow; arbitrarybasisinputs stillhaveaboundedpermutationextension. Allraw/childarraysremainuntiltheir literalreverse. CanonicalinverseF andeveryqueryFULLKscan remain unchanged.

## 3. Explicit uniform generator and full address charge

The newlayoutallocatesrecord/prefixarrays andONEflagpersortcomparator, plusreusablecleanscratch. No n²helperreservationperrecordorall-scan-layerallocationexists. LetSbeWHOLEpaddedlanesacrossallnodes,Mthelargestsortlength,andd=ceil(log2(Malloc+2))forALLallocatedclassicalbits/qubits. Publicarray/nodepacketsandstridesarepoweroftwo paddedwithatmostconstantfactorwaste. The actual adaptive A-leaf layout uses public heap formulas and a common power-of-two node-packet stride. Iterate level/node indices without a directory or host stack. All buffers/counters fit constant many O(n)-bit classical words; Rrec records are allocated qubits (proof2A).

SortingusesO(S log²M)comparatorsandoneflagpercomparator. Alllinearrecordopsandsequentialscans thereforeuseO(S n d²)gates and

    O(S(n+d²)) quantumrecord/historybits.

ThisincludesALLnodes, paddedarrays, root, prefixes, comparisonflags andconstantmanycompute/output/inverse regions. SharedO(n)cleanwordhelpersareactuallyreused. Eachprogrammedsize/flag count is a finitepublicinteger; adding ALL actual auxiliary V regions, linear reflection apparatus and classical controller gives d=O(r+log n)=O(n) for this CURRENT constant-eight program as proved in9. Everybyte/qubitinitializationandcleanupiscounted.

For gateemissionkeepconstantmanyrunningbit/field/rowpointers. WithinanO(n)-gateword theymovebyunitsteps; boundedbinaryincrement/decrement hasamortizedO(1)changedbitsperstep. ForalooplimitL0 initialize counterL0-1 usingitsPUBLICminimalbitwidth, executebody, subtract1withripple andstoponUNDERFLOW, avoidingarepeatedfullzerotest. Totalvisits/bitflipsareO(L0+log(L0+1))=O(L0). FixedClifford+Ttemplatesareunrolled. Reversewords useboundedreversecounters; thereisnostoredcircuit/historyhoststack.

Recordboundarysetupmaycopy/addO(n)bitsatFULLaddressfee d. Paddedstridesmake bitonicpartneroffsets shifts/xors; source/raw andscanpartnersuseshifts/additions, notan n-by-n multiplyperelementarygate. SetupO(n)d plusOnemittedgatesandpointerupdatesatfeed isO(n d) perrecordoperation. Serializationpays theFULLglobalfee forEVERYgate; itsaddressbitsarenotfree. Consequently TOTALmarkwork is

    O((S(n+d²)+n4) d³),

including conservative full global-zero apparatus generation. The join-only word remains O(S n d³); after flags exceed Sn the complete mark bound pays the larger memory term.

Initialization of ALL S(n+d²)+n4 bits and every linear zero apparatus fit this enlarged bound. Thisisabit-operation/generationledger, notunit-costRAMoronlygatecount.

## 4. Current constant-eight application and whole allocation

Currentproof3/9select k=3,a=8, mainn0=2^40,m=n+160,r=floor(m/8),t=m-8r,F=4.
General1--3 supplies ACTUAL SAME comparator/scan words. EVERY exact sort flag count B*k_sort*(k_sort+1)/4
is allocated alongside padded record/prefix/history regions. The common heap stride is nextpow2(sum of
padded region lengths), with successor bases recomputed AFTER complete enlarged tree blocks. Old-node
histories remain separate; no recursive payload copying/checkpoint pool or Sn-only stride is used.

Here S=O(L),k_sort=O(n),d_addr=O(n). Full M_base=O(S(n+k_sort^2)+n4)=O(Ln2), including all flags,
helpers and PGM evaluator scratch. Outer zero apparatus is a separate counted constant-factor linear
addition to WHOLE testedA; its calculator is excluded from its own test. CURRENT native6 streaming heap emitter gives complete charged O(M_base*d_addr^2)=O(Ln4), including
all enlarged global/PGM apparatus, initialization and generation. Every node uses O(d_addr) bit operations
with full address fee per operation, constant-many public pointers and a fixed Clifford+T template.
Join-only O(Sn*d_addr^3)=O(Ln4) is not used to undercount global zero work. Public j and exact identity
3r+t/2=3n/8+60+t/8 inproof9 give totalT n^(9/2)2^(3n/8) and SQ n2 2^(n/8).
Full source/reference/bank/operator-score/product-selector/spectral/Jordan safety remains supplied;
Q/h and corruption promise are unchanged. All failed trials, literal inverses and disposal count.
