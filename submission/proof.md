# RPF-16VP16: sixteen-list measurement with a public nominal count and short reflections

## 0. One algorithm, promise and joint theorem

Material immediate source is the complete published sixteen-list quantum-record-bank engine fbdd86c2-74f7-4dd2-a876-7f512146233d. The generic read-only layer/corrected-tail methods and NEW variable-branch unequal bridge are material from this session's checkpoint/VP16 work; exact public IDs, file hashes and native/publication failures are disclosed in the note/dependencies. NEW actual sorting uses t_ck=16,H_ck=32,B_ck=2^ceil(ceil(log2n)/16), EXACTLY33 public frames and32B_ck allocated quantum pools, with NO padding of the layer count to B_ck^h. These names NEVER replace preimage H, score effect B or witness D. The complete source/coupling/score/cap/column/PGM/spectral/reachable safety and current native/helper/controller proof are supplied below. No source acceptance or finite diagnostic is a theorem premise. All five claims concern this ONE actual new V_R and literal inverse.

For N>=2 write n=ceil(log2N), u=n+2, Q=3*2^40(n+32), q=Q/2, n0=2^12. ONE program below has unconditional full-secret success>=2/3 and simultaneous bounds
 T=O(2^(1717n/4000)n^(9/2)), S_C=O(n), S_Q=O(2^(n/16)n^(17/16)),
 EXACT original acquisitions Q=3*2^40(n+32)=O(n).
Time/quantum indices are1; classical/sample indices0. Every branch is capped, including failure/unused originals, and all bit operations, gates, addresses, generation, initialization and memory count.

The literal malformed fraction is1/32: an adversary fixes B, |B|<=floor(Q/32), possibly depending onN,s. The joint state, with arbitrary inaccessible reference, has reduced state rho_s tensor(Q-|B|) on all other positions; bad systems may be arbitrarily entangled/correlated subject to that marginal. Mixtures over fixed B follow by linearity. No source control, preparation inverse or purification is available.

Acquire EXACTLY Q originals on every branch. Preprocess/split/score as1–2. If n<n0 run8. Otherwise m=16ceil((n+160)/16), r=m/16, L=2^r, Pcap=2^160*L, K=2^178, Kk=nextpow2(m+1), H=L^11*Kk*K. Run6–7 with the preimage word3–5. nextpow2 is computed by integer bit lengths. These are fixed choices for all five claims, not separately optimized configurations.

All constructions are supplied in this file, native.md and variable-native.md. Material source9fd0fa0e-7410-422f-a82d-67022c0c7cfc (published balanced sample program) receives credit for joint-source.md2 full-reference extraction/coupling and sources/RQ-SPLIT-proof.md3 finite eigenlabel probing. Its other engine, old output law/resource bounds and verdict are not premises. Standard credits: Bacon–Childs–vanDam2005, arXiv:quant-ph/0501044 (PGM/preimages); Marriott–Watrous2005, arXiv:cs/0506068 (binary in-place witness tests); Kitaev1995, arXiv:quant-ph/9511026 (eigenphase probes). No external native oracle is assumed.

## 1. Source and unconditional reference comparison

Let omega=e^(2pi i/N), chi_k=N^-1/2 sum_(x<N)omega^(-kx)|x>, phi_k=(|0>+omega^(ks)|1>)/sqrt2. Orthogonality gives exactly
 rho_s=(1/N)sum_k |phi_k><phi_k| tensor|chi_k><chi_k|.
Known ADD1 has eigenvalueomega^k onchi_k; extend ADDa by identity on padding x>=N. Privately uniformly translate position byj in[0,N), forgetj. The factor (1/N)sum_j omega^(j(k-l)) kills distinct valid k,l coherences, also against a reference. A bad padding/zero-mode coherence need not vanish; no separation of those modes is used. Each GOOD position has valid support globally by positivity of its marginal.

Each uniform range draw uses d=ceil(log2(2^40Q)) trials of ceil(log2range) fair bits, taking the first in range; conditional success is exactly uniform. A whole Q-draw procedure aborts with probability<=2^-40. Keep an abort flag but nevertheless acquire all Q originals. On success use the native2 nondemolition ADD eigenlabel instrument, t=n+4, reporting W modN with per-eigenstate error<=delta=2^-100n; measure probes and discard position, retaining phase qubit/W. Known translations act only on position, so every fixed probe transcript acts by a scalar onchi_k and never changesphi_k.

The exact twirl gives an analysis-only classical refinement of all good k. Their JOINT marginal is IID uniform, because the original good marginal is the stated product. Given all good k, the good phase subsystem is a PURE product; positivity forces it to factor from all bad/reference systems. The remaining state may depend onk. Define a comparison OUTPUT by replacing only GOOD reported W with its hiddenk, keeping every bad channel and reference unchanged. Couple actual/ideal outcomes using the same hidden k/probe transcripts: they differ only on a good report error. Full-reference trace distance<=Qdelta<2^-40. This is unconditional; do not condition uniform labels on successful extraction/bad reports. Later channels contract this distance. Work always refers to the physical capped instrument.

## 2. Private split and exact score soundness

After ALL Q acquisitions, uniformly Fisher–Yates permute phase/W pairs using the same range capd; total abort<=2^-40. Conditional success gives exactly uniform permutation independent of input. First q records form a verification bank, second q an unknown witness bankD. Forb=|B|, putp=b/Q<=1/32. Bad countX in either half has meanqp and varianceq*p*(1-p)*q/(Q-1)<=q/32. Thus Var(X/q)<=1/(32q). Set eta=2^-20. By Chebyshev/union, either half exceeding p+eta has probability<=2/(32q*eta²)=1/(24(n+32))<1/1024 for n>=n0. This stronger event implies the old33/1024 bound used below. It concerns ONLY B/private permutation; no conditioning of good labels or bad reports is used. In the finite-prefix fallback use the original bound: varianceX<=Q/4 and a deviationQ/2048 give failure<=2^20/Q<1/1024. The actual source/permutation schedule is unchanged.

Measure verification phases in independent fair X/Y axes beta=0,pi/2, outcomesZ=+/-1. Retain(W,beta_flag,Z). Define score(a)=q^-1 sum Zcos(2pi*aW/N-beta). A good term has mean1/2 for a=s,0 otherwise: averagebeta gives(1/2)cos(2pi*(a-s)W/N), then uniformW gives character orthogonality. Good marginal terms are independent, without conditioning on bad data. Hoeffding for[-1,1] gives good-sum deviationq/16 probability<=2exp(-q/512); union over all N candidates is<2^-40. Bound every bad contribution by its count, regardless of correlations. On these events
 score(s)>=(1-33/1024)/2-1/16-33/1024=797/2048,
 score(a) for a!=s <=1/16+33/1024=97/1024.
Native2 gives an EXACT rational cosine polynomial with error<1/128 and common positive denominatorD. The Boolean marker a<N AND4sum Z*C>=qD therefore accepts EXACTLY s. It is computed with reserved clean scratch, untouched by earlier stages. Thus clean-verifier soundness holds for EVERY witness/reference state, not merely honest decoder outputs. The measured score records occupy the immutable quantumRrec bank of2A.

## 2A. Actual record bank, reference law and O(n) classical controller

Rrec is a bank of ALLOCATED QUBITS of total sizeO(Qn)=O(n²), counted inSQ. Acquire ALLQrawsystemsfirst inO(Qn)qubits. Processonecopyat a time: measured/decodedW and verification(beta,Z) pass through a reusableO(n)-bit classicalrow, are written by classicallycontrolledX into a basisrow ofRrec, then the classicalrow is erased/reset at chargedcost. No classicaltranscript table remains. If the full measuredrecord/reference law is sum_r |r><r|_C tensor sigma_r, this write/erase channel produces EXACTLYsum_r |r><r|_Rrec tensor sigma_r. Thus allreferencecouplings in1 contract through it. Only measured basisinformation is copied; the unknownphase/reference state sigma_r is untouched.

OutsideV sourceprobe stages run t,t-1,..0, keeping currentcos/sin tallies, current six-bit gridangle and the currentO(n)-bitdyadic unwrapvalue. Native2's backwardsunwrap then discards completedtallies. PublicADD^(2^j)coefficients are regenerated by iterative doubling of1modN asneeded, not stored as a growingtable. Good conditionalchi_k probes act by scalars, so order doesnot change their independentoutcome/error proof; badsourcechannels remain arbitrary. Extra coefficientregeneration is polynomial insideO(n^9). Firstvalid capped range draws store only currentdraw/firstvalidvalue/flag/trialcounter; everyrawdraw is discarded/reset. Private Fisher–Yates usesCLASSICALrowindices and literalSWAPgates onphase/fullquantumlabelrows, so its uniformconditionalpermutation andabortlaws are unchanged withoutquantumaddresslookup. Allthese operations/resets/feescount.

After split/verificationRrec is immutable and CQdiagonal, with arbitrary conditionalD/reference states. V_R copies its witnesslabels byCNOT atPUBLICrowindices into quantumWwork; routing stillFULLSCANSq positions. The score's W/beta/Z are read-only Booleanquantumcontrols for the generic bounded arithmetic innative1-2. Eachrecordsector has the same clean mathematicaldecoder and exactunique-scorepredicate; the fixed-degree score arithmetic is separately charged polynomial work; variable-native supplies the ACTUAL linear comparison/selected-copy record functions for the new sort. No hostbranch depends on quantumrecordbits. Rrec never changes. On each realizedr,V_R is a blockV_r; the initialCQmixture and blockdiagonal gates give exactlythe conditional analyses3-7. The literalinverse is the NEWactualV_Rdag, not an asserted equality ofdirtyextensions to older compiledwords.

Put P=I_(D,Rrec) tensor|0_A><0_A|, withA EVERYmutableV_Rwire, includingWwork/probes/coins/arithmetic/histories. Rrec is immutableINPUT and is NOTzerotested. WithQv=V_Rdag C V_R, proof7's spectralinequality, Jordanrenewal and invariantRangeP+Range(QvP) apply blockwise and totheCQmixture. Range(C V_R P) has exactlythe truecandidate onthe scoreevent for everyD/referenceinput. The unknownD is never reset/reflectedabout as a knownstate. In fallback8 check a measuredcandidate by reloadingthatknowncandidate, computingthe SAMErecord-controlled marker and measuringitsoneflag; chargeclearing/resets. This preserves the unique-score searchlaw usingO(n)classicaloutcome/outputstorage and no additionaloriginal.

Classicalmemory inventory: publicN/n/Q/q/m/r/L/caps/H/j/J andinput/output; percopyrange/probe/unwrap/verificationrows; arithmeticoperand/result/remainder/accumulator buffers; and generatorloop/base/stride fields. There is a CONSTANTnumber ofO(n)-bitwords. Inplace schoolbookmultiplication uses fixed-widthoperand/resultaccumulation, restoringdivision usesquotient/remainder, and greedyroot usescandidate/trialsquare, eachO(n)space. PublicMachin terms haveO(n)-bitindividualdenominators and fixed-pointaccumulators(native2); no growingdenominator product or savedclassicalhistory is used. Degree400 and64gridpoints are FIXEDcounts. Allsource/probe histories insideV are QUANTUMancillas includedinSQ.

The ACTUAL generator computes public B_ck=2^ceil(ceil(log2n)/16), reserves32B_ck quantum checkpoint arrays and uses EXACTLY33 classical frames (32 internal levels plus a base frame). Each frame holds constant many O(n)-bit public words. It processes only nonempty unequal blocks of the ACTUAL layer count, with no padding to B_ck^h. The literal prefix/last-child/uncompute word and frame phase counters are variable-native2--3. Power-of-two array strides and running pointers supply the fully charged O(Ln4) record/gate budget; separately polynomial per-call metadata is counted in9. No growing-in-n host stack, B_ck-entry classical directory or stored circuit exists. This gives SC=O(n), including all frames, source/score buffers and public arithmetic.

Rrec/source/staging/copies addO(n²)qubits and polynomialwork, included in the NEW O(Ln^(17/16)) quantum peak / O(Ln4) charged time word bounds. Basisrecords are not free: their initialization, write/erase, knownrowSWAP/CNOT/data-control gates and FULLglobaladdressfees are charged. Alltime/SQ/Q/fraction choices remain thoseof0; the newstorage/controller is ONEprogram satisfyingthe improvedSC bound jointly.

## 3. Sixteen-group bounded oracle and weighted input-mass caps

For selected W, f(b)=sum W_jb_j modN, c_y=|f^-1(y)|. Set m=16ceil((n+160)/16), r=m/16,L=2^r. Kk=nextpow2(m+1), K=2^178.  Sixteen rawlists;8pairnodes,4secondnodes,2thirdnodes,1root. Every nonroot capacityP=2^160*L, rootK=2^178; any overflow rejectsWHOLEtuple.

ForT=y+carry*N, choosefreeh1..h7, deriveh8=(T-sum h1..h7)modL; eightpairnodes haveunreducedS_i withS_i modL=h_i, vi=(S_i-hi)/L. PutU=(T-sumhi)/L. Choosefreeg1..g3 andderiveg4=(U-sumg1..g3)modL; foursecondnodes impose(v_(2j-1)+v_(2j))modL=g_j, retaining quotientw_j=(v_(2j-1)+v_(2j)-g_j)/L andalloriginalIDs. PutV=(U-sumgj)/L. Chooseonefreez in[0,L); leftthirdnodehas(w1+w2)modL=z, right(w3+w4)modL=(V-z)modL. Storefullt12=w1+w2 andt34=w3+w4; ROOTEXACTt12+t34=V, canonicalb sort/rankj. SignedU,V useboundedfields, neveraddresses. X has those eleven r-bit free hashes, carry in[0,Kk), and rankj in[0,K). Freehashbits7+3+1=11r. H=L^11*Kk*K. Native rejects carry>m and any invalidrank. Every survivingb determinesUNIQUE h/g/z/carry/canonicalrank; inverse recomputesS_i,hi,vi,gj,wj,z andSAMEboundedtree/fullKscan. Genericnativejoinonly, no externaloracle.

NEWthirdnodecap lemma. Fixuniforminputb,W, andconsideralternatesonits8groups, fourchildpairs. LetD1..D4 bealternate-minus-b integerchanges in eachchildpair. Membership inbactualthirdbucket equivalentto:
 Di=0modL forALLi; D1+D2=0modL²; D3+D4=0modL²; sumDi=0modL³.
For everychangedchildpairchooseone +/-1 coefficient variableX_i amongits2rgrouplabels; conditionalonallothers theseX_i are independentuniform[0,N). AssumeN>=L³. A modulusL^j constraint ononeX admits<=ceil(N/L^j)<=2N/L^j choices regardlesssign/offset. Countd numberchangedchildpairs:
 d0: contribution1.
 d1: peraltprob<=2/L³; <=4L² alternatives gives<=8/L.
 d2 samehalf: choosefirstXmodL thenother tocanceltheTOTALmodL³; this automaticallysatisfiesitsownmodL andhalfmodL². Prob<=4/L4, <=2L4 alternatives contributes<=8. Differenthalves: firstmustvanishmodL², secondcancelmodL³, prob<=4/L5, <=4L4 alternatives contributes<=16/L.
 d3: in thetwo-changedhalf, choosefirstXmodL thensecondtovanishtheirsum modL²; the singlechangedotherhalf mustcancelTOTALmodL³, automaticallysatisfyingitsownhalfmodL². Prob<=8/L6, <=4L6 alternatives contributes<=32.
 d4: chooseX1modL, X2tocancelD1modL², X3modL, X4tocancelTOTALmodL³. LastconstraintautomaticallygivesD4modL andD3+D4modL². Prob<=16/L7, <=L8 alternatives contributes<=16L.
Thus expectedthirdbucket<=16L+41+24/L<=16L+65<=81L. Earlierchildcaps onlyremoveentries. Firstpair<=3L, second<=9L, henceALL14nonrootcapsweightedINPUTmassloss<=(8*3+4*9+2*81)*2^-160=222*2^-160. No uniformtarget/conditionedhash premise. ForfullcountsputM0=2^m,mu=M0/N, with2^160<=mu<2^176. ThecollisionsecondmomentE[(1/N)sum(c_y/mu-1)²]<1/mu andK=2^178>=2mu implyweightedheavyinputmass<=4/K=2^-176: forv=K/mu-1>=1 use(1+d)Iheavy<=d²(v^-2+v^-1). Thisisnotuniform-targetconditioningorathirdmoment. ExcludingentireheavycolumnsONLYinanalysis, surviving cprime isphysicalnonheavycountand0onheavy. Sinceall14nonrootcapsloseatmost222*2^-160, Eell<=222*2^-160+2^-176<2^-152. Everyphysicalheavywordremainsbounded;nonheavyc_y<=Kprecludesrootcapoverflow.

## 4. Actual public-nominal-count positive preimage column

Put M0=2^m, mu=M0/N. These are PUBLIC rationals/integers, independent of W,y,s. Main-range rounding gives2^160<=mu<2^176. Let cprime_y be the physical surviving marked count for nonheavy targets c_y<=K. In analysis only set cprime_y=0 on heavy columns, as in3; those entire columns are charged as lost input. The physical oracle/unitary always keeps its public caps and may behave arbitrarily on heavy inputs. No global quantumcount estimator, countcopy or countuncompute is executed. Exact bucket counts inside the bounded join remain ordinary explicit Boolean words.

Generate finitepi P_pi/D_pi as native2 with precision b=2log2H+40. Compute PUBLIC
 j=floor-sqrt(floor(P_pi²*H*N/(16D_pi²*M0))).
Its distance from(pi/4)sqrt(H/mu) is<2: finitepi scaling contributes<1/16, and floor-sqrt of a floored nonnegative rational equals floor of its real square root. All integers haveO(n)bits, and j generation/storage/full fees are counted. The ACTUAL loop executes EXACTLY these j iterations, not an old sqrtH loop with inactive controls. j=O(sqrt(H/mu)); both it and its inverse loop are fixed by the public input.

Start X uniformly on its power-of-two H domain and apply exact
 G=(2|u_H><u_H|-I)(I-2P_mark)
exactly j times. Every G genuinely invokes the bounded mark word; no fastpower is assumed. Native uses the positive diffusion scalar exactly. A fixed|1> helper supplies any minus compensation, then is cleared; no y-dependent phase is dropped. For physical count c, its two-dimensional angle is theta=asin(sqrt(c/H)) and marked amplitude sin((2j+1)theta). c0 has no marked component.

Let tau=2^-40. Call a target REGULAR if |c_y/mu-1|<=tau and d_y=c_y-cprime_y<=tau*mu. Then 0<cprime_y and |cprime_y/mu-1|<=2tau. Put z0=sqrt(mu/H), z=sqrt(cprime_y/H). Main-range mu<2^176,K=2^178 andH>=L^11K imply z0<=L^-2<=tau/32, sinceL>=2^24 atn>=n0. Also z<=2z0<=1/4. Write j=pi/(4z0)+eta, |eta|<2. From z<=asinz<=z+z³, |sqrt(1+d)-1|<=|d| for|d|<=1/2, andpi<4,
 |(2j+1)asinz-pi/2| <=4tau+7z<=4tau+14z0<16tau<pi/2.
Thus the marked amplitude is POSITIVE and the full Grover state differs from the normalized marked state by at most16tau in norm. This estimate uses only relative closeness to the public mu, not a measured or coherently estimated count.

Keep X unchanged while computing its canonical solver output g(X), copy b into fresh B and the SINGLE tag NOT(validtuple), and reverse g. Only then compute the SAME canonical F(B), XOR it intoX, and reverse F temporaries withB unchanged. On marked branches, X/tag/allhelpers are0; distinct marked tuples correspond uniquely to surviving b. On unmarked branches tag1 remains, even if dummyb accidentally erases an index. The all-zero-count case already has no marked tuple and receives no second tag XOR. Literal reversal defines the inverse on all dirty inputs.

Therefore this actual finite U_y has its clean column within16tau of |muprime_y>|0_aux> on REGULAR columns, where muprime_y is the uniform surviving b state. All nonregular/heavy columns have a bounded unitary extension; comparison distance is at most2. Zero-count intended columns have no success overlap. No whole-unitary approximation, unknown-source inverse, intermediate measurement or postselection is used.

## 5. Input-weighted nominal-count error and PGM completeness

For each fixed W the full counts obeysum_y c_y=M0. Any pair of distinct subsets b,bprime has a coefficient+/-1 in f(b)-f(bprime); conditional on all other IID uniform labels its moduloN collision probability is exactly1/N, also for composite/oddN. Hence
 E_W[(1/N)sum_y(c_y/mu-1)²]=(1-1/N)/mu<=1/mu.
This is a joint second-moment identity. It does NOT assume a uniform target independent of the input or condition labels on bad reports.

Let beta(W)=sum_y(c_y/M0)1_(nonregular y), the actual INPUT-weighted mass of bad columns. For d=c_y/mu-1 and |d|>tau, (1+d)1_bad<=d²(tau^-2+tau^-1). On the remaining count-regular columns, c_y<=mu(1+tau); the number with d_y>tau*mu is at most M0*ell/(tau*mu). Thus
 E beta <=2/(mu*tau²)+2Eell/tau
 <=2^-79+2^-111<2^-78,
since3 gives Eell<2^-152 andmu>=2^160,tau=2^-40. Heavy columns are nonregular under the analysis definition cprime0. These inequalities explicitly charge lost INPUT, rather than a uniform-y measure.

The good selected phase input is M0^-1/2 sum_b omega^(s f(b))|b>. Compute f(b) into read-only Y, apply U_y^dag toB/fresh0work, and coherently require B/allpreimageauxiliaries0. W,Y are excluded from that PGM-zero test. The intended surviving frequency vector is M0^-1/2 sum_y sqrt(cprime_y)omega^(sy)|y>. The zero-auxiliary vector error has squared block weights c_y/M0; distinctY blocks are orthogonal. Section4 bounds its norm by16tau+2sqrt(beta), so its mean is<=16tau+2sqrt(Ebeta). This uses the adjoint of a single prepared column in eachY block, not a whole-unitary operator-norm claim.

For full counts, Cauchy and the same secondmoment give expected L1 distance ofc_y/M0 from1/N at most sqrt(N/M0)<=2^-80. Its ideal correct-frequency amplitude alpha=sum_y sqrt(c_y)/sqrt(N*M0)>=1-L1/2, so mean failure<=2^-80. Removing input fractionell changes the frequency vector by<=sqrt(ell), since(sqrt c-sqrt cprime)²<=c-cprime. Retain the conservative allowance4sqrt(Eell).

Native2 known-ADD readout, with t=n+4 anddelta=2^-100n, identifies the true frequency with per-eigenstate error<=delta; negate its decoded label as specified there. Retain Y through acceptance. Orthogonal frequency eigenstates make the classical readout law a mixture, so no dimensionN error multiplier occurs. Comparing squared overlaps of norm-at-most-one frequency vectors changes success by at most twice their norm distance. Therefore the complete decoder mean failure is at most
 2^-80+4sqrt(Eell)+32tau+4sqrt(Ebeta)+delta
 <2^-80+2^-74+2^-35+2^-37+2^-100<2^-34<2^-20.  (5.1)
Use Eell<2^-152,Ebeta<2^-78,tau=2^-40 anddelta=2^-100n. These are fixed adequate accuracy margins for the constant success target; no vanishing-error assumption is needed. Bad columns are handled by their weighted norm mass and the physical word remains finite; no artificial target rejection is executed.

## 6. Actual verifier and unconditional good-label event

Coherently choose an ordered m-subset of witnessD by Fisher–Yates range draws, d_sel=ceil(log2(4m)) trials each. Keep ALL fair raw coins. Validity>=3/4; conditional validity gives EXACT uniform ordered subsets. Copy immutableRrec labels byCNOT to a quantum buffer; quantum-selected phase/label swaps use full q-position scans. All coin/buffer/scan work is polynomial. Raw coins remain orthogonal through acceptance, making the clean acceptance effect a positive average over subsets.

In the main range m<=2n and q=3*2^39(n+32), so m/q<2^-38<2^-30. On the stronger split event each successive all-good draw has probability>=1-p-eta-m/q>=R, R=31/32-2^-20-2^-30=1040186367/2^30. To justify the subtraction, p/(1-x)<=p+x whenever0<=x<=1-p; usex=i/q for previous all-good draws. Sampler-valid all-good weightw>=R^m/2. Define B as the normalized all-good valid DECODER-ONLY effect requiring true candidates andPGM-zero flag, with0<=B<=I. It does not consult score data. On the score-uniqueness event, the physical marker equals that true-candidate predicate for EVERY witness, so the actual acceptance effect A>=wB. No such inequality is used off that event.

V is the coherent selector/routing, decoder4–5 and exact score marker2, with dedicated untouched score scratch. AcceptC only on selector-valid/PGM-zero/candidate<N/score. All V operations are known finite Clifford+T words; there are NO internal measurements. For clean ancillary inputs on the score event, every accepted vector has candidate=s for arbitrary D/reference.

Given ALL good hidden labels, selected good phases are pure products factoring from the rest; B ignores unselected/bad phases. Its mean completeness is(5.1) over the UNCONDITIONAL IID good-label marginal, irrespective of bad reports. Markov gives an event, failure<=1/1024, on which Tr(rho B)>=1-1/1024. Do not obtain it by conditioning labels on score/bad reports/prior survival. Intersect it with split/score events by union bound; source-label distance is charged once.

## 7. Randomized subspace reflections, unknown witness and exact safety

D is ALL original witness phase wires andRrec is the read-only quantumrecordbank. A is every mutableV_Rworkwire, initially0. P=I_(D,Rrec) tensor|0_A><0_A| as2A; neither unknownDnorimmutableRrec is zerotested. AllV/Qv/Avsymbols in7 denote the ACTUALrecord-controlledV_R/blockwiseprojectors of2A. Qv=V^dag C V; Av=P Qv P onRangeP. On the score event Av>=p0B, p0=2^(-ceil(23m/500)-1), using R^500>2^-23. The exact finite integer inequality is1040186367^500*2^23>2^15000, computable by fixed repeated squaring/multiplication with no real-number oracle. Therefore R^m>=2^(-23m/500)>=2^(-ceil(23m/500)); this supports the ACTUAL shorter rotation cap below. The decoder-only B from Section6 hasTr rho B>=1-1/1024 except the already bounded unconditional good-label event.

For E=1_(Av<c p0), EBE<=cE. Hence
 ||E rho^(1/2)||_HS <=||E B^(1/2)rho^(1/2)||_HS+||(I-B^(1/2))rho^(1/2)||_HS <=sqrt(c)+sqrt(epsilon)
wheneverTr rho B>=1-epsilon, since(1-sqrt b)^2<=1-b. At c=epsilon=1/1024, initial spectral mass below a=p0/1024 is<=1/256. This bound does not assume A and B commute.

First make ONE binary Qv test: apply V, measure ONLY C; accept/output candidate, or on failure apply literalV^dag, leaving state inQv-perp. Put U=(I-2P)(I-2Qv), each factor an EXACT subspace phase reflection. I-2P computes all-zero(A) in a separate clean AND-tree apparatus, phases its single flag withZ and reverses the entire Boolean computation, returning apparatus0 on ANY A. I-2Qv is V, Z on C, literalV^dag. No source preparation inverse or reflection about the unknown D state occurs.

Choose J=2^(ceil((ceil(23m/500)+11)/2)+4), so J>=16/sqrt(a) andJ=O(2^(23m/1000)). For at most16 trials choose fresh UNIFORM CLASSICAL j in[0,J) by log2J fair bits, apply U^j, then make the same binary Qv test and stop on acceptance. On failure literalV^dag returns toQv-perp. Charge all j<=J-1 words; discard only classical trial coins, never reset D/A or measure P. At timeout output0. The program acquires no additional originals.

In a Jordan blocklambda=sin^2theta for P,Qv, starting inQv-perp, acceptance afterj rotations is sin^2(2jtheta). Forlambda in[a,1-a], sin(2theta)=2sqrt(lambda(1-lambda))>=sqrt(2a). Geometric summation gives
 r_lambda=(1/J)sum_(j=0)^(J-1)sin^2(2jtheta)>=1/2-1/(2J|sin(2theta)|)>2/5.
On every failed Qv test, that block is AGAIN its unique Qv-perp direction. Thus independent classical choices j renew the same success rate; sixteen trials fail<= (3/5)^16<1/1024. This is exact Jordan-block renewal, not a conditional freshness assertion for the original witness. Cross-block/reference coherences do not affect trace probabilities because each map preserves the blocks. Forlambda>1-a the INITIAL Qv failure is< a; forlambda<a bound by its initialmass1/256. Total failure on score/good-label events is<=1/256+1/1024+a<.01. Degenerate lambda0/1 obey the limiting statements directly.

Safety is exact for dirty A: S=RangeP+Range(QvP) is invariant under P,Qv, their complements AND both reflections. Every reachable Qv-accept state lies inRange(QvP), and after V lies inRange(CVP), where the clean-input exact score marker forces the ENTIRE true candidate for every D/reference state. Globally dirty false-accept states elsewhere need not be sound. No fine-grained work measurement is used.

Union the unchanged source-label distance, two bounded range aborts, split, score and good-label failures with this conditional failure. Unconditional whole-secret success remains>2/3 for every N,s and the same literal fixed-joint fraction1/32. Fixed trial/rotation caps count every failure branch.

## 8. Finite fallback, same acquisitions/noise

For n<n0 use the SAMEQ/split/score; discard unused witnesses with full charge. On its events the score marker has exactly one solution inH0=2^n. Do16 independent trials: uniform classicalj in[0,J), J=2^(ceil(n/2)+2); initialize a fresh uniform candidate register, perform j exactGrover words for the marker, measurethecandidate and check it bythe coherentrecord-controlledmarker as2A, returningfirstpassing. No new source copy is acquired.

For theta=asin(1/sqrtH0), mean trialsuccess is
 (1/J)sum_j sin²((2j+1)theta)=1/2-sin(4Jtheta)/(4Jsin2theta)>=1/2-1/(16sqrt2)>2/5,
usingJ>=4sqrtH0, sin2theta>=sqrt(2/H0). Failure<=(3/5)^16<1/1024, independently across fresh trial coins/search initializations on fixed score data. Same source/split/score union gives success>=2/3. WorkO(2^(n/2)poly(n)), spacepolynomial, exactQ. The finite setn<n0 has a finite maximum ratio to the declared envelopes, absorbed into an outside constant independent ofN,s,outcomes. No faster exponential rate is asserted on that finite prefix.

## 9. Actual constant-depth variable-branch checkpoint ledger

The physical sorting program fixes t_ck=16, H_ck=32 and computes
k_n=ceil(log2 n), B_ck=2^ceil(k_n/16), by integer bit length and shift.
These CHECKPOINT parameters never replace the preimage search-domain H,
the score effect B, or source/private-coin choices. For main n>=4096,
 n^(1/16)<=B_ck<=4n^(1/16), B_ck>=2.
All actual mathematical16Q parameters remain
m=16ceil((n+160)/16), r=m/16, L=2^r, Pcap=2^160L, K=2^178,
Kcarry=nextpow2(m+1), H=L^11 Kcarry K. Thus n+160<=m<=n+175<=2n,
K<=L and L>=n^5. Base data-array lane count S=O(L) includes all sixteen-raw/fifteen-join, marker/query/root packets; checkpoint rows multiply it by B_ck and are counted below.
Original and sorted rows, all raw/child/root/marker/query/padding and
canonical inverse arrays remain counted.

Variable-native1--3 supplies the ACTUAL READ-ONLY layer-XOR word and
unequal-block bridge. A sort has D_sort=k(k+1)/2 layers for k=log2 M<=n,
so D_sort<=n². It does NOT pad D_sort to a power of B_ck. A segment d>1 has
b=min(B_ck,d) NONEMPTY children of length floor(d/b) or ceil(d/b),
with exact public start offsets. Repeated ceiling division bounds depth
by H_ck=32, since B_ck^32>=n²>=D_sort. Each prefix array remains until
its reverse child clears it using the preceding prefix. The last child
writes to the final arbitrary output Z. All lower pools clear after
each child and are reused. The exact full segment function is Z XOR
(composed layers)(A), with A unchanged and ALL internal pools/helpers0.
This holds coherently against a reference; globally dirty inputs still
have a literal unitary inverse, with no stronger function assertion needed.

If C(d) counts base-layer calls, C(1)=1 and
 C(d)=2 sum_(i=0)^(b-2)C(d_i)+C(d_(b-1))<=2 sum_i C(d_i).
The children lengths sum to d, so C(d)<=2^32 d. Internal call count
is also O(C(d)) since each internal node has at least3 children.
The EXPLICIT recomputation multiplier2^32 is a fixed outside constant,
not dependent on n,N,s or outcomes. No practical crossover claim is made.
A base layer uses O(Mn) gates and O(n) reusable ripple scratch, so the
WHOLE sort uses O(MnD)=O(Mn³) gates. Corrected sequential scans use
DISTINCT heads and reverse tails; all prefix states/flags/raw additions
fit O(Sn) data and O(Sn²) gates. The clean duplicate/rank/cap/canonical
functions in3--5 are unchanged by these actual new physical words.

The native source/controller inventory and EXACTLY33 public recursion
frames (32 internal levels plus one base frame) each have constant many O(n)-bit fields. There is NO B_ck-entry
classical directory and no growing-in-n host stack. Quantum checkpoint
pool addresses use aligned power-of-two array strides and public depth/
child index, never quantum-selected classical access. Variable-native3
emits each linear record word with running bit/field pointers and minimal
underflow counters; all gates and changed bits pay the FULL global fee
 d_addr=ceil(log2(Malloc+2))=O(n).
Per-record setup/gates therefore cost O(n d_addr). Public per-call
segment/frame/descriptor/offset setup is conservatively O(n^4) TOTAL
charged work using in-place public arithmetic; there are O(n²) such
calls per sort, so O(n^6) setup, separately counted. Since L>=n^5,
this is within the WHOLE marked oracle budget. No uncharged layer decoder
or repeated n-by-n multiplication per elementary gate is assumed.
Consequently the entire oracle has TOTAL charged work O(Ln4), including
all32B_ck checkpoint initialization, zero apparatus and cleanup.

ACTUAL public nominal j=O(L^(11/2)sqrt n) uses exactly j full Grover words
and literal inverses. Whole column/inverse work is O(L^(13/2)n^(9/2)).
The SAME source/private split and short-reflection schedule executes
O(2^(23m/1000)) whole verifier/inverse/zero-phase words on every branch.
Thus
 T=O(2^(1717m/4000)n^(9/2))=O(2^(1717n/4000)n^(9/2)),
since13/32+23/1000=1717/4000 and m-n<=175. Every source, failed/discarded/
inactive/padded operation, address/generation step, output and cleanup
counts. The existing conservative O(n^9) source/selector/probe/score/
readout/public-pi/root polynomial work also fits, because L>=n^5.
Only histories literally reversed are reused; no repetition-time history
accumulates. All33 frames are bounded workspace, not a stored circuit.

Quantum memory includes ALL32B_ck arrays at each whole packet, including
unused zero/padded slots; actually needed pools use at most32(B_ck-1)
arrays. Whole original/sorted/prefix/boundary/raw/root/marker fields and
shared Boolean work give O(SnB_ck), and all Rrec/source/staging O(n²),
O(n^4) auxiliary source/selector/probe/score/routing/arithmetic regions,
constant many marked/output/inverse regions and the allzero apparatus
linear in EVERY mutable V_R wire fit that allocation. Since
B_ck<=4n^(1/16) and L<=2^11 2^(n/16),
 S_Q=O(2^(n/16)n^(17/16)).
The33 classical frames plus the complete streamed record/controller
inventory are O(n) CLASSICAL bits. All persistent measured records are
allocated qubits, not free data. P=I_(D,Rrec) tensor zeroA includes EVERY
new mutable pool/flag/helper; the ACTUAL new V_R and literal inverse
define Qv. The full spectral/reachable safety proof uses those words,
not an older dirty extension or accepted verdict.

All branches acquire EXACT Q=3*2^40(n+32), including abort/discard/unused
and finite fallback. The SAME full fixed-joint fraction1/32, score and
private source split apply for every N,s, with unconditional entire-secret
success>=2/3. Finite n<4096 has its original finite outside constants.
Time/quantum indices are1, classical/sample indices0. Compared with16Q,
both time and quantum envelopes improve. Compared with a lean16 analogue, time
is the same envelope and quantum degree17/16 is smaller than2. Compared
with binary16CP, time is smaller while quantum n^(17/16) is eventually
larger than n logn. No cross-point optimum or finite-size dominance is claimed.

## 10. Scope, credit and provenance

Sixteen-list/PGM circuits and all quantified native lemmas are complete in this archive; tests/verdicts are not premises. The standard tools credited in0, comparison networks/prefix scans/schoolbook arithmetic and two-projector decomposition are not claimed invented. Related Helm–MayPQCrypto2020 subset-sum tradeoffs supply no assumedpreimage oracle. Earlier published source9fd0fa0e joint/RQ methods are rederived here, not substituted by its acceptance. The actual earlier submission documents its own local operational failures/compaction; no hosted judgment is asserted here. This changed variable-checkpoint/helper/controller configuration requires its OWN fresh whole-proof review; no parent verdict is reused.

Randomized Grover-length/rotation credit: Boyer, Brassard, Høyer and Tapp, arXiv:quant-ph/9605034; amplitude amplification/estimation credit Brassard, Høyer, Mosca and Tapp, arXiv:quant-ph/0005055. The exact unknown-witness/spectral-tail/reachable-safety application is proved here, not imported as an uncosted oracle.
