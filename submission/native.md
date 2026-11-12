# RPF-TAIL-CONSTANT8-CHECKPOINT-EPS207 finite words and charged generator

## 1. Exact Boolean/Clifford+T words

Widths come from PUBLIC bounds: residues<2^n, sums<m2^n, paddedtargets<(2m+2)2^n, join totals<=productofinputcapacities, all offsets<=wholeallocation. EACH routine also includes its exact public maximum for every fixed-degree power/product (in particular C(A), D and pi constants in2) or its declared fixed-point precision/guard. Twice the sum of THAT routine's maximum bit lengths plus32 suffices; all widths areO(n) with fixed constants. Signed keys use bounded two's complement. Invalid division/overflow has a fixed flag/default, never an unbounded loop/allocation.

Compute each BooleanAND in a fresh bit byCCX, XOR byCNOT, NOT byX; retain intermediatebits. Copy output and reverse every gate with inputs unchanged. Ripple addition uses carry_i=(a_i ANDb_i) XOR((a_i XORb_i) ANDcarry_(i-1)); comparison usesborrow, equalitybitwiseAND. Schoolbook multiplication hasO(w) shiftedpartialproduct/addrows, O(w²) gates/history; restoringdivision hasO(w) compare/subtractrows, alsoO(w²). Greedyintegerroot testing successivebits by bounded squaring costsO(w³). All loops fixedwidth, all histories counted. This supplies totalreversible arithmetic, not unit-cost integerinstructions.

For publica reduce modN anddefineF_a(x)=x+a modN forx<N, elsex. It is a wholewordpermutation, inverseF_-a. ComputeF_a intozero word, swapwords, XORcomputeF_-a ofnewx toclearoldx, reversearithmetictemps. KnownADD^(2^j) usespublica=2^jmodN byrepeateddoubling; ONLYknownADD powers getthis shortcut, neverGrover. Controlled versions useextraBooleancontrols.

ExactCCZ follows4abc=a+b+c-(a xor b)-(a xor c)-(b xor c)+(a xor b xor c)mod8: compute7parities into7cleanhelpers, applyT forpositive/Tdag fornegative terms, reverseparities. H onthirdwire before/after givesCCX. ControlledT/S computesAND(control,target), phaseshelper, uncomputesAND. ControlledH usesA=SHTHSdag, AZAdag=H, soAdag,controlledZ,A isexactCH. ControlledX/CNOT areCNOT/CCX; constantmorecontrols useconstantmanyANDhelpers. Scalars are exact, controls haveconstantoverhead. On dirtyhelpers thesewords stilldefineunitaries; inverses always reverseLITERALgates.

An all-zero test computeszeroindicators/ANDtree, copiesrootflag and reverses forcoherentuse. For outer reflection, compute the SINGLE all-zero(A) flag, phase it by Z and reverse the entire Boolean computation, clearing its separate apparatus0 for ANY A. This is exact I-2P. V never touches this apparatus. Qv reflection is V,Z on C,literalVdag. Outer measurements are ONLY C tests/final candidate, not P or individual A wires. Fixed random trial/rotation bounds and safety are proof7. No source preparation inverse or reflection about the unknown D state is used.


## 2. Finite phase probes, arithmetic and score

For aU eigenvaluee^(2pi i theta), Hprepareprobe, controlledU^(2^j), thenH forcosine orSdag,H forsine. ItsZoutcome mean iscos/sin(2pi2^jtheta). For EACHj in{0,...,t} repeat eachbasis h=ceil(2^31(n+t+1)) times. Conditionedeigenstate outcomes areindependent. Bounded-variablemgf (convexendpointbound for+/-1) giveserror>1/256 probability<=2exp(-h/(2*256²)); unionover2(t+1) is<delta=2^-512n fort=O(n). Explicitly t=n+4 and h=2^31(n+t+1), so the union failure is at most4(n+5)exp(-2^14(2n+5)). Since e>2 and4(n+5)<=2^(n+5) for n>=1, this is less than2^(n+5-2^14(2n+5))<2^-512n. InsideV keepallrawprobes andcomputeallclassicaldecodingREVERSIBLY; outsideV sourceprobes maybemeasured. Eigenstate register isunchanged; forsuperpositions its orthogonalblocks give the correspondingmixture ofprobabilities.

Generate64rationalcirclepoints byfiniteMachin/Taylor: pi_bar=16atan(1/5)-4atan(1/239), eachseries200terms. Remainder<16/(401*5^401)+4/(401*239^401)<2^-900. Identity follows tan(4atan(1/5)-atan(1/239))=1 in(0,pi/2). Degree400cos/sinpolynomials at2pi_bar*l/64 givecoordinateerror<1/4096. These arecomputedconstants, notinstanceadvice. Picknearestgridpoint toempirical2-vector byexactrational squareddistance; output itsEXACTanglel/64. Empiricalvectorerror<1/128, nearesttruegridchord<=pi/64, rationalerrorsleavechosenchord<1/8; 2sin(pi*d)>=4d on[0,1/2] impliescircularphaseerror<1/32.

Backwardunwrap: startbeta_t; forj=t-1..0 selectnearerofbeta_(j+1)/2,(beta_(j+1)+1)/2 tocoarseangle_j usingcircularcomparisons. Correctroot isunique sincecoarse+rooterrors<=3/64<1/4. Finalcircularerror<=2^-t/32; allangles arefiniteO(t)-bitdyadics. Badtranscripts usetotalboundeddecoding. Witht=n+4, roundNbeta_0 modN givesexactvalidlabel outsideerrorsector. Forfrequencygamma_s, ADD1eigenvalueomega^-s, soNEGATEreportedlabel. Retainfrequencyregisterthroughacceptance: orthogonalityprevents anydimensionN errorfactor.

Variableprecisionb usesB=b+ceil(log2(b+2))+80 fractionalbits. Forpi sumB+1 fixedpointterms ofeachMachinseries. Denominators(2l+1)5^(2l+1), (2l+1)239^(2l+1) haveO(B)bits; eachschoolbookdivisionrounds<=2^-B, total<=20(B+1)2^-B plusgeometrictail<2^-2B. Thuspiaccuracy<2^-b, generationO(B³)classicalwork/O(B)space. Noevergrowingproductdenominator iscalledO(B)bits.

Takeb=2log2H+40 forpi usedinthePUBLICnominalj;B=O(n). No global Grovercount estimator isexecuted.

For the PUBLICnominalj, M0=2^m andmu=M0/N. Generatefinitepi P_pi/D_pi withb=2log2H+40 and computej=floor-sqrt(floor(P_pi²*H*N/(16D_pi²*M0))) CLASSICALLY frompublicN,n. Its error from(pi/4)sqrt(H/mu) is<2. All publicintegers/rootloop widthsO(n), generatedwiththefinite arithmeticabove atchargedpolynomialcost. The actual literalword has EXACTLYj Groveriterations, witha publicclassicalcounter0..j-1 anditsinversej-1..0 (each inverse iteration emits literalGdag with reversed mark/diffusion order); neverrunanoldJmax=sqrtH loop withchargedinactivegates. Every iteration uses the FULLexactboundedmark andpositive diffusion. Keep the scalarminuscompensation byZon a fixedactive|1> helper, whichisprepared/cleared byX; no unknown/coherent count or activecomparison isused. No quantumglobalcountfield, countcopy, count-inverse orj(c)cleanup exists. Aftersearch the SINGLEfailuretag isNOT(validtuple), andoutput/inverseindex cleanupisnative3/proof4. The source/secret known-ADD eigenphaseprobes andexactscore belowremaininuse.

For EXACTscore useconstantpi_bar=P_pi/D_pi above. E=2D_piN, D=400!*E^400. Forr=aWmodN andbetaflag0/1, A=4P_pi*r-betaflag*P_pi*N. Defineinteger
 C(A)=sum_(l=0)^200 (-1)^l A^(2l)[400!/(2l)!]E^(400-2l).
C/D approximatescos(2pi*r/N-betaflag*pi/2): angleerror<4*2^-900, |A/E|<8, Taylorremainder<=8^402/402!<2^-401, totalcosineerror<2^-400: 201!>=2^200 and the201factors202..402 each exceed128, so402!>2^1607 whereas8^402=2^1206. Angleerror4*2^-900 plus2^-401 is less than2^-400. AllintegerwidthsO(n), withlargeFIXEDgeneratedcoefficients. CommonD isidenticalacrossrecords. Exactmarker isa<N AND6sumZ*C>=qD. Schoolbookfixedloops compute/copy/reverse withdedicatedcleanscratch. ImmutableRrec recordbankO(Qn)=O(n²)ALLOCATEDQUBITS; scoreW/beta/Z are read-onlyquantumBooleancontrols; coherentmarkerhistorypolynomialqubits. OnlyconstantmanyO(n)-bit classicalinput/operand/outputbuffers exist, asproof2A. Aftercandidate measurement use the SAMErecord-controlled exactmarker andmeasureitsflag asproof2A; no classicalbankcopy or extraoriginal is acquired.

## 3. Fixed padded duplicate join, canonical inverse and Groverword

Arrays carry key,payload,present,tag and bounded helper fields, all O(n) bits. The PUBLIC mathematical bitonic layers are: forK0=2,4,..M; forJ0=K0/2,..1 halves; pairi,z=i xorJ0>i, ascendingif(i ANDK0)=0 else descending. Full key order is padding/presence class,signed key,tag,payloadID. Marker-before-query ties are explicit TAG. Standard induction separates lower/upper bitonic halves at each half-stride layer and recursively merges them; doubling K0 ends sorted. The mathematical network has k(k+1)/2 layers and at most Mk(k+1)/4 comparisons for k=log2M. No arbitrary equal-key stability is assumed.

The ACTUAL implementation is the COMPLETE read-only layer-XOR and four-level unequal checkpoint bridge in checkpoint-native1--4. Each layer preserves its original input and XORs its sorted-layer function into a separate output, using clean reused O(n) predicate work; no persistent one-bit-per-comparator history is executed. Four public pools of B_ck arrays are reserved, all unused slots count, and prefix/last/reverse-prefix word cleans every lower pool for arbitrary final Z. Inputs and sorted outputs remain until dependent work reverses. Literal inverses work on every dirty extension; no old dirty-unitary identity is assumed.

SorttaggedA/Bunion. In head_i=(i0ORkey_i!=key_(i-1)), key means ONLY the JOIN KEY and padding class; tag/payload are SORT tie-breakers and MUST NOT split a join bucket. B_indicator is1 only on present B records. Compute head flags with this join-key equality, paddingaseparatekeyclass. Compute TAIL_i=(i=M-1 OR key_i!=key_(i+1)) separately with the SAME join-key/padding equality. Forward inputs are (B_indicator,head_i); reverse-order inputs are (B_indicator,TAIL_i), NEVER the head_i array. ForwardBprefixandreverseBsuffix useASSOCIATIVEresetmonoid
 (x,h)star(y,k)=(y ifk elsex+y,h ORk).
BucketBcount=forward+reverse-B_indicator; B_rank=forward-1. ACTUALsequentialprefixcomputesonefreshstateperlane frompreviousprefix/inputrow, retainingONLYtheseMstates. Reversefromlastlanetofirstwithinputsunchanged. Suffixes reverse order with TAIL flags. Induction gives each forward value as the bucket-start-through-i B sum and each suffix as the i-through-bucket-end B sum; their sum minus B_indicator is exactly the bucket count. Retain both boundary arrays until scans reverse, then uncompute them from unchanged sorted rows. Allmarker/count/startprefixesusethesameword(checkpoint-native4). AssociativitygivestheEXACTsamevalues;O(M)scanrecordoperations,allworksequential.

EachAlane'smultiplicityisitsbucketBcount, B/paddinglanes0. GlobalprefixsumassignsAoutputstart. FixedmarkerlanepresentonlyforpositiveAmultiplicity, stores(start,key,AID). EmitEXACTLYcapqueriespos0..cap-1 withpresencepos<min(fulltotal,cap). Sortmarkers/queriesbypos,markerfirstties, prefixpropagaterightmostPRESENTmarker (associative). Eachquery getsB_rank=pos-start. Matchrequests(key,rank,AID,pos) againstBmarkers(key,rank,BID) byanothersort, Bmarkerfirstties,andrightmostmarkerpropagation. CheckBOTHkey/rankbeforeoutput; sortrequestoutputsbypos,paddinglast. Distinctpositiverangespartitionallpairs. Allmarker/queryslotsfixed; presencebitsareNOTvariableallocation/filtering. FulltotalcountknownBEFOREtruncation; iftotal>cap rejectWHOLEbranch. Negativekeys/padding/overflowremainbounded.

There are O(a+b+cap) base rows per bounded join; ALL eight-group nodes give S=O(L). Sort k_sort<=r+182<=n/4, D_sort<n². Actual B_ck=2^ceil(ceil(log2n)/2),H_ck=4 give at most16D_sort base calls and allocate EVERY4B_ck pool array per sort. Full workspace O(Ln^(3/2)),d_addrO(n),TOTAL join O(Ln4), native6 global-zero O(Ln^(7/2)) and whole mark O(Ln4). All source/score/helper/padding regions and whole allocation fees count.

Direct-tail CONSTANT EIGHT arity binding: m=n+160,a=8,A_tree=a,D_grp=3,r=floor(m/a),m_c=ar,t=m-m_c,L=2^r,Pcap2^160 nextpow2(8a)L,K2^162,Kcarrynextpow2(m_c+1),F=a-D_grp-1,H=2^t L^F Kcarry K,mainn0=2^40. FIRSTm_c phases form core groups; LASTt REAL phases form the direct tail. The X register is u(tbits), Fr free-hash bits, corecarry and rank. Compute f_tail(u) by fixed-wire controlled additions of the tail labels, y_c=(y-f_tail(u))modN, T0=y_c+carryN. At levels1..D_grp-1 derive the last nonempty hash, normalize child sums and remaining target exactly asproof3, with root EXACT remaining sum. ANY cap overflow/carry>m_c/invalidrank rejects WHOLEquery. All raw/child/quotient/history/stage arrays retain their inputs until reversal. Each parent carries ONLY its current value/ID/presence and constantmany O(n)-bit helper fields; child histories stay in SEPARATE node blocks, not recursively duplicated payloads.

The word g(X) copies FULLb=(corepayload,u) and SINGLE NOTvalid tag, then reverses ALL g/tail-target work withXunchanged. F(B) extracts tailu, recomputes tail/core target, all actual core hashes/carry, SAME capped tree and FULLK canonical rank, then XORs the ENTIRE index includingu intoX and reverses every F temporary withBunchanged. Thus all marked branches clear all hash/carry/rank/tail helpers, with commonphaseomega^(s*y) for the FULL target. No core-only density, per-tail Grover loop, tail measurement or extra source bit is assumed. The global diffusion and nominalj below act on the ENTIRE H domain includingu.

Public heap/level/node loops and checkpoint-native4 fixed FOUR-frame bridge emitter use O(n) classical bits and fully paid public metadata. No growing recursion stack, host circuit table or quantum-selected address exists. ALL pool, source, score, routing and outerzero helpers count under proof9 entireallocation.

GusesmarkphaseandPOSITIVEdiffusionH_X(2|0><0|-I)H_X. Ifzero-signflip isI-2|0><0|, applyZtoactivecontroltoCOMPENSATEminus; The current iteration count is public; the exact scalar is still included. Each PUBLIC-j Groveriteration is a literal fullmark/diffusion word; there is no globalpowered-count loop. Preimageextraction keepsXunchangedwhilecomputingg(X), copyingb/NOTvalidtag, thenreversingg; onlyTHENcomputeF(B), XORintoX,andreverseFtempswithBunchanged. The PUBLICnominalj loop is exactlySection2/proof4; there is no global quantumcount/countcopy/active-flag computation. Vhasnointernalmeasurements; read-onlyW,Y stayoutsidePGMzero test. Allrawselector/probecoinsremaincoherent. LiteralVdag reversesEVERYelementaryword/scalar/flag, evenondirtyextensions.

## 4. Entire current constant-eight checkpoint program

Mainn>=2^40 selects exact eight-group core3, COMPLETE read-only layer-XOR/four-level bridge/sequential distinct scans checkpoint-native1--4, proof9 full ledger and source/operator-score/product-selector/spectral/Jordan/reachable proof1--2/6--7. All current pool regions and literal inverse words are counted. No equality of globally dirty extensions to prior sort words is assumed. Exact rational1/6 marker and delta2^-512n native probes remain; p0=1/4,J1024,sixteen trials are unchanged. UnknownD is never reset/reflected as a known state; all5claims are simultaneous. Finite n<2^40 uses8 with SAME exactQ. No test/verdict is a premise.

## 5. Entire evaluator allocation

Proof9's CURRENT M_base=O(S*n*H_ck*B_ck+n4)=O(Ln^(3/2)) includes EVERY4B_ck checkpoint array,
raw/root/scan/source/score/router/probe/helper and inner evaluator. The separate linear outer evaluator
is excluded only from its OWN tested set; all mutable V scratch including inner calculators is tested.
Native6 below supplies the ACTUAL streaming phase/flag emitter with O(M_base*d_addr²) charged work,
not an old Sn-only apparatus or d³ emitter. Full d_addr comes from the entire physical allocation.

## 6. Current streaming global/PGM zero-tree and initialization emitter

This is the CURRENT actual generator, replacing the precursor's generic conservative global-zero emitter.
Let A0 be the public list of wires tested, length R<=M_base. For outer P, this is ALL mutable V/A, including
PGM calculator scratch but excluding unknown D, immutable Rrec and the SEPARATE outer calculator Zout.
For an inner PGM zero test it is its stated tested workspace, excluding only that calculator. The public
layout puts the complete mutable arena contiguously; exclusions are finitely many named role intervals
from the fixed literal word. Repeated tree roles are generated by existing heap loops, not a stored table.
The fixed finite region-role list and its loop counters use constant-many O(n)-bit words. Traversing all
tested intervals and recomputing each repeated-role base costs at most O(M_base*d_addr^2), even charging
O(d_addr) bit operations with full fee per wire; it never examines quantum data to choose an address.

Let P=nextpow2(R), allocate disjoint one-bit leaf indicators z[0..P-1] and heap parents y[1..P-1], all0.
For actual tested wire w_i, emit CNOT(w_i,z_i), then X(z_i), so z_i=1-w_i on basis inputs. For padding i>=R,
emit X(z_i). For h=P-1 down to1 emit Toffoli(child(2h),child(2h+1),y_h), where child(j) is y_j if j<P
and z_(j-P) otherwise. Phase Z on y_1; for P=1 phase z_0. Reverse EVERY gate in reverse order.
Thus the circuit is diagonal, phases exactly the all-zero tested basis states, and returns ALL calculator
wires to0 for every tested input and reference. Linearity proves the zero reflection on arbitrary states;
no calculator self-test or reflection on unknown D is present. This is the same required projector, with
an explicitly changed generator, not a new assumption about dirty unitary extensions.

Use public constant-many base/current-child/current-parent pointers of width d=ceil(log2(M_alloc+2)).
At each node form2h,2h+1 by shift and one-bit addition, compare toP, subtractP when needed, and add the
corresponding public base. All are O(d) BIT OPERATIONS with restoring ripple carry and no multiplication.
Use a d-bit loop counter; even a worst-case O(d) decrement and termination comparison per node fits.
Each Toffoli expands to a FIXED finite Clifford+T template; its address tuple copies O(d) bits per emitted
gate. Every quantum gate pays FULL d address fee. Conservatively each of the O(d) classical bit operations
also pays FULL d, so each node/leaf emission costs O(d^2). Reverse iteration uses the same bounded counters,
not a history stack. Actual/padding leaves, internal nodes, phase, initialization of all calculator wires,
reverse gates and output-first disposal number O(P)=O(R), hence TOTAL O(R*d^2). All prior flag and helper
arena bits initialize/dispose through linear public interval loops with the SAME per-bit bound. No unit-cost
address arithmetic, free gate list, RAM/QRAM or extra ordinary classical memory is used. Since R<=M_base,
complete zero/arena work is O(M_base*d^2). Separate constant-many evaluator instances multiply this only
by an outside constant, with every wire included in the current physical prefix and global address fee.
