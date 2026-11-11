# RPF-16S: sixteen-list measurement with randomized subspace reflections

## 0. One algorithm, promise and joint theorem

Material immediate source is the eight-list short-reflection construction, which supplies its complete source/score/column/PGM/shortened-reflection engine. Its earlier four-list binary and reflection origins remain credited. The sixteen-group bounded join tree in3/native3 and its ledger9 are new in this draft. Its actual platform source IDs, complete file hashes and operational-retry history are specified in the dependency declaration/public note. Every source/preimage/column/count/score/native argument used here is supplied and re-established in this archive. Section7 retains the actual shortened randomized-reflection rotation cap proved by the immediate source; Section9 rederives the whole cost for this actual sixteen-group tree. No earlier verdict is a mathematical premise; balanced-source/academic credits remain below.

For N>=2 write n=ceil(log2N), u=n+2, Q=3*2^40(n+32), q=Q/2, n0=2^20. ONE program below has unconditional full-secret success>=2/3 and simultaneous bounds
 T=O(2^(69n/160)n^(3351/10)), S_C=O(n²), S_Q=O(2^(n/16)n^108),
 EXACT original acquisitions Q=3*2^40(n+32)=O(n).
Time/quantum indices are1; classical/sample indices0. Every branch is capped, including failure/unused originals, and all bit operations, gates, addresses, generation, initialization and memory count.

The literal malformed fraction is1/32: an adversary fixes B, |B|<=floor(Q/32), possibly depending onN,s. The joint state, with arbitrary inaccessible reference, has reduced state rho_s tensor(Q-|B|) on all other positions; bad systems may be arbitrarily entangled/correlated subject to that marginal. Mixtures over fixed B follow by linearity. No source control, preparation inverse or purification is available.

Acquire EXACTLY Q originals on every branch. Preprocess/split/score as1–2. If n<n0 run8. Otherwise m=16ceil((n+64ceil(log2u))/16), r=m/16, L=2^r, Pcap=nextpow2(Lu^100), K=nextpow2(u^200), Kk=nextpow2(m+1), H=L^11*Kk*K. Run6–7 with the preimage word3–5. nextpow2 is computed by integer bit lengths. These are fixed choices for all five claims, not separately optimized configurations.

All constructions are supplied in this file and native.md. Material source9fd0fa0e-7410-422f-a82d-67022c0c7cfc (published balanced sample program) receives credit for joint-source.md2 full-reference extraction/coupling and sources/RQ-SPLIT-proof.md3 finite eigenlabel probing. Its other engine, old output law/resource bounds and verdict are not premises. Standard credits: Bacon–Childs–vanDam2005, arXiv:quant-ph/0501044 (PGM/preimages); Marriott–Watrous2005, arXiv:cs/0506068 (binary in-place witness tests); Kitaev1995, arXiv:quant-ph/9511026 (eigenphase probes). No external native oracle is assumed.

## 1. Source and unconditional reference comparison

Let omega=e^(2pi i/N), chi_k=N^-1/2 sum_(x<N)omega^(-kx)|x>, phi_k=(|0>+omega^(ks)|1>)/sqrt2. Orthogonality gives exactly
 rho_s=(1/N)sum_k |phi_k><phi_k| tensor|chi_k><chi_k|.
Known ADD1 has eigenvalueomega^k onchi_k; extend ADDa by identity on padding x>=N. Privately uniformly translate position byj in[0,N), forgetj. The factor (1/N)sum_j omega^(j(k-l)) kills distinct valid k,l coherences, also against a reference. A bad padding/zero-mode coherence need not vanish; no separation of those modes is used. Each GOOD position has valid support globally by positivity of its marginal.

Each uniform range draw uses d=ceil(log2(2^40Q)) trials of ceil(log2range) fair bits, taking the first in range; conditional success is exactly uniform. A whole Q-draw procedure aborts with probability<=2^-40. Keep an abort flag but nevertheless acquire all Q originals. On success use the native2 nondemolition ADD eigenlabel instrument, t=n+4, reporting W modN with per-eigenstate error<=delta=2^-100n; measure probes and discard position, retaining phase qubit/W. Known translations act only on position, so every fixed probe transcript acts by a scalar onchi_k and never changesphi_k.

The exact twirl gives an analysis-only classical refinement of all good k. Their JOINT marginal is IID uniform, because the original good marginal is the stated product. Given all good k, the good phase subsystem is a PURE product; positivity forces it to factor from all bad/reference systems. The remaining state may depend onk. Define a comparison OUTPUT by replacing only GOOD reported W with its hiddenk, keeping every bad channel and reference unchanged. Couple actual/ideal outcomes using the same hidden k/probe transcripts: they differ only on a good report error. Full-reference trace distance<=Qdelta<2^-40. This is unconditional; do not condition uniform labels on successful extraction/bad reports. Later channels contract this distance. Work always refers to the physical capped instrument.

## 2. Private split and exact score soundness

After ALL Q acquisitions, uniformly Fisher–Yates permute phase/W pairs using the same range capd; total abort<=2^-40. Conditional success gives exactly uniform permutation independent of input. First q records form a verification bank, second q an unknown witness bankD. Forb=|B|, bad countX in either half has meanb/2, varianceb(Q-b)/(4(Q-1))<=Q/4. Either half exceeding bad fraction33/1024 implies |X-b/2|>Q/2048, so split failure<=2^20/Q<1/1024. This event concerns only B/private permutation.

Measure verification phases in independent fair X/Y axes beta=0,pi/2, outcomesZ=+/-1. Retain(W,beta_flag,Z). Define score(a)=q^-1 sum Zcos(2pi*aW/N-beta). A good term has mean1/2 for a=s,0 otherwise: averagebeta gives(1/2)cos(2pi*(a-s)W/N), then uniformW gives character orthogonality. Good marginal terms are independent, without conditioning on bad data. Hoeffding for[-1,1] gives good-sum deviationq/16 probability<=2exp(-q/512); union over all N candidates is<2^-40. Bound every bad contribution by its count, regardless of correlations. On these events
 score(s)>=(1-33/1024)/2-1/16-33/1024=797/2048,
 score(a) for a!=s <=1/16+33/1024=97/1024.
Native2 gives an EXACT rational cosine polynomial with error<1/128 and common positive denominatorD. The Boolean marker a<N AND4sum Z*C>=qD therefore accepts EXACTLY s. It is computed with reserved clean scratch, untouched by earlier stages. Thus clean-verifier soundness holds for EVERY witness/reference state, not merely honest decoder outputs. The measured score records stay immutable.

## 3. Sixteen-group bounded oracle and weighted input-mass caps

For selected W, f(b)=sum W_jb_j modN, c_y=|f^-1(y)|. Set m=16ceil((n+64ceil(log2u))/16), r=m/16,L=2^r. Kk=nextpow2(m+1), K=nextpow2(u^200).  Sixteen rawlists;8pairnodes,4secondnodes,2thirdnodes,1root. Every nonroot capacityP=nextpow2(Lu^100), rootK=nextpow2(u^200); any overflow rejectsWHOLEtuple.

ForT=y+carry*N, choosefreeh1..h7, deriveh8=(T-sum h1..h7)modL; eightpairnodes haveunreducedS_i withS_i modL=h_i, vi=(S_i-hi)/L. PutU=(T-sumhi)/L. Choosefreeg1..g3 andderiveg4=(U-sumg1..g3)modL; foursecondnodes impose(v_(2j-1)+v_(2j))modL=g_j, retaining quotientw_j=(v_(2j-1)+v_(2j)-g_j)/L andalloriginalIDs. PutV=(U-sumgj)/L. Chooseonefreez in[0,L); leftthirdnodehas(w1+w2)modL=z, right(w3+w4)modL=(V-z)modL. Storefullt12=w1+w2 andt34=w3+w4; ROOTEXACTt12+t34=V, canonicalb sort/rankj. SignedU,V useboundedfields, neveraddresses. X has those eleven r-bit free hashes, carry in[0,Kk), and rankj in[0,K). Freehashbits7+3+1=11r. H=L^11*Kk*K. Native rejects carry>m and any invalidrank. Every survivingb determinesUNIQUE h/g/z/carry/canonicalrank; inverse recomputesS_i,hi,vi,gj,wj,z andSAMEboundedtree/fullKscan. Genericnativejoinonly, no externaloracle.

NEWthirdnodecap lemma. Fixuniforminputb,W, andconsideralternatesonits8groups, fourchildpairs. LetD1..D4 bealternate-minus-b integerchanges in eachchildpair. Membership inbactualthirdbucket equivalentto:
 Di=0modL forALLi; D1+D2=0modL²; D3+D4=0modL²; sumDi=0modL³.
For everychangedchildpairchooseone +/-1 coefficient variableX_i amongits2rgrouplabels; conditionalonallothers theseX_i are independentuniform[0,N). AssumeN>=L³. A modulusL^j constraint ononeX admits<=ceil(N/L^j)<=2N/L^j choices regardlesssign/offset. Countd numberchangedchildpairs:
 d0: contribution1.
 d1: peraltprob<=2/L³; <=4L² alternatives gives<=8/L.
 d2 samehalf: choosefirstXmodL thenother tocanceltheTOTALmodL³; this automaticallysatisfiesitsownmodL andhalfmodL². Prob<=4/L4, <=2L4 alternatives contributes<=8. Differenthalves: firstmustvanishmodL², secondcancelmodL³, prob<=4/L5, <=4L4 alternatives contributes<=16/L.
 d3: in thetwo-changedhalf, choosefirstXmodL thensecondtovanishtheirsum modL²; the singlechangedotherhalf mustcancelTOTALmodL³, automaticallysatisfyingitsownhalfmodL². Prob<=8/L6, <=4L6 alternatives contributes<=32.
 d4: chooseX1modL, X2tocancelD1modL², X3modL, X4tocancelTOTALmodL³. LastconstraintautomaticallygivesD4modL andD3+D4modL². Prob<=16/L7, <=L8 alternatives contributes<=16L.
Thus expectedthirdbucket<=16L+41+24/L<=16L+65<=81L. Earlierchildcaps onlyremoveentries. Firstpair<=3L, second<=9L, henceALL14nonrootcapsweightedINPUTmassloss<=(8*3+4*9+2*81)u^-100=222u^-100. No uniformtarget/conditionedhash premise. Rootheavycolumnsadd<=u^-200+2^80u^-136 becausem<=n+64log2u+79.


Thus for the survivor set Dprime and lost INPUT fraction ell=1-|Dprime|/2^m,
 E ell<=222u^-100+u^-200+2^80u^-136.
This is a uniform INPUT(W,b) bound. No uniform-target or conditional-independence assertion is used. On nonheavy targets c_y<=K, root capacity cannot overflow and survivorcount cprime_y<=K. Heavy columns are excluded only in analysis; their physical unitary word remains capped and may behave arbitrarily. Every node uses native3 fixed sort/scan duplicate joins, all histories retained for reversal. Original IDs preserve distinct subsets when sums coincide. Native root/rank requests scan ALLK slots; no QRAM or input-dependent allocation is supplied.

## 4. Clean uniform-preimage column

Use exact G=(2|u_H><u_H|-I)(I-2P_mark). Its relevant eigenvalues are exp(+/-2i theta), theta=asin(sqrt(c'_y/H)). Include its diffusion scalar minus sign under every control. For nonheavy y, c'_y<=K. Apply coherent native2 phase probing toG with
 t=ceil((log2H+log2K)/2)+10, h=ceil(2^30(n+t+1)).
Each G^(2^j) is GENUINELY2^j repeated oracle words. Final phase error<=2^-t/32 exceptdelta. Hsin²(pi*phase), evaluated to count error1/32, rounds to exactc'_y: additional phase error is bounded by2pi sqrt(HK)|d|+pi²H d²<1/32. Both eigenphases decode to SAME count. Conditional eigenstate probes are independent; their orthogonality proves the coherent correctness bound for their initial uniform-state superposition. All raw probes/history remain quantum.

For count computationU, copy its output then apply literalU^dag. Correct-copy sector is U^dag Pi_c U|0>, overlap with|0> equal to the REAL NONNEGATIVE probability>=1-delta. Its full output differs from |0>|c> by <=2sqrt(delta). Count and output-search workspaces are separate.

With c>=1 compute j within2 of(pi/4)sqrt(H/c) by native2 finite division/root. Fixed loop Jmax=2^(ceil(log2H/2)+2)=O(sqrtH) applies G under counter<j; charge all inactive controlled words. Reverse each active flag immediately, then uncompute j(c) withc UNCHANGED, BEFORE count erasure. Since p=c/H<=K/H=1/(L^11*Kk)<=1/(LKk), sqrtp is tiny. Put z=sqrtp<=1/4. Since z<=asin(z)<=z+z^3 and |j-pi/(4z)|<2, the amplification angle error lies between -3z and 5z+(pi/2)z^2+5z^3, whose upper bound is<6z. Thus its absolute value is<=6z<=3/2<pi/2: marked amplitude is POSITIVE and column distance<=6z<16sqrtp. The latter is the unchanged error allowance. A generic finite pi approximation plus floor-root guarantees error<2, not necessarily<1; no one-sided rounding is assumed. Set j=0 for c=0.

KeepX unchanged while computing its solver output, copying b into fresh B, assigning the SINGLE failure tag NOT(valid tuple), then reversing solver work. Now computeF(B), XOR it intoX, and reverse that temporary work while B is unchanged. Marked branches haveX=0,tag=0,helpers0; unmarked branches keep tag1 even ifdummyb erasesX. Truec=0 already makes every tuple invalid: do NOT toggle the same tag a second time. Finally reverse the separate clean-count-copy word. Replacing count by its ideal deterministic value before/after the exact search incurs at most another2sqrt(delta), independent of the number of intervening gates.

This defines an actual finite unitary U_y, read-only on W,y, whose clean column is within e=8sqrt(delta)+16sqrt(K/H) of |mu'_y>|0_aux> on c'_y>0 nonheavy columns. mu'_y is uniform over survivors. Zero-count intended columns have tag1 and no success overlap. Dirty/heavy behavior is the literal unitary extension with the same caps. No unknown-source inverse occurs.

## 5. PGM completeness using column accuracy only

Good phase input is2^-m/2 sum_b omega^(s f(b))|b>. Compute f intoY, apply U_y^dag toB/fresh workspace, and COHERENTLY require B/all preimage auxiliaries0. W,Y are excluded from that test. Ideal zero-auxiliary frequency vector is2^-m/2 sum_y sqrt(c'_y)omega^(sy)|y>. Coherent known-ADD readout from native2 returns s (negate its decoded eigenlabel); retainY and all probe bits through acceptance. Different frequency eigenstates remain orthogonal, so per-eigenstate errordelta introduces NO factorN. There is no intermediate postselection/measurement inV.

Collision counting gives E sum_y(c_y/2^m-1/N)²=(1-1/N)2^-m, so expected L1 deviation<=sqrt(N/2^m)<=u^-32. Ideal correct amplitude alpha=sum sqrt(c_y)/sqrt(N2^m)>=1-L1/2; ideal mean failure<=u^-32. Removing input fractionell loses amplitude<=sqrt(ell), by Cauchy and(sqrt c-sqrt c')²<=c-c'. Column error changes the zero-auxiliary vector by <=e: distinctY blocks are orthogonal and their input squared norms sum to1. Arbitrary heavy columns add norm<=sqrt(ell). Thus mean decoder failure<=
 u^-32+4sqrt(222u^-100+u^-200+2^80u^-136)+2e+delta <2^-20.  (5.1)
At n0 the first term<=2^-640 and all other displayed terms are smaller; elementary monotone bounds hold thereafter. This uses the adjoint of ONE prepared column, not an unjustified whole-unitary approximation.

## 6. Actual verifier and unconditional good-label event

Coherently choose an ordered m-subset of witnessD by Fisher–Yates range draws, d_sel=ceil(log2(4m)) trials each. Keep ALL fair raw coins. Validity>=3/4; conditional validity gives EXACT uniform ordered subsets. Copy classical labels to a quantum buffer; quantum-selected phase/label swaps use full q-position scans. All coin/buffer/scan work is polynomial. Raw coins remain orthogonal through acceptance, making the clean acceptance effect a positive average over subsets.

On the split event m/q<=1/1024; each successive all-good draw has probability>=1-33/1024-m/q>=495/512. Sampler-valid all-good weightw>=(495/512)^m/2. Define B as the normalized all-good valid DECODER-ONLY effect requiring true candidates andPGM-zero flag, with0<=B<=I. It does not consult score data. On the score-uniqueness event, the physical marker equals that true-candidate predicate for EVERY witness, so the actual acceptance effect A>=wB. No such inequality is used off that event.

V is the coherent selector/routing, decoder4–5 and exact score marker2, with dedicated untouched score scratch. AcceptC only on selector-valid/PGM-zero/candidate<N/score. All V operations are known finite Clifford+T words; there are NO internal measurements. For clean ancillary inputs on the score event, every accepted vector has candidate=s for arbitrary D/reference.

Given ALL good hidden labels, selected good phases are pure products factoring from the rest; B ignores unselected/bad phases. Its mean completeness is(5.1) over the UNCONDITIONAL IID good-label marginal, irrespective of bad reports. Markov gives an event, failure<=1/1024, on which Tr(rho B)>=1-1/1024. Do not obtain it by conditioning labels on score/bad reports/prior survival. Intersect it with split/score events by union bound; source-label distance is charged once.

## 7. Randomized subspace reflections, unknown witness and exact safety

D is ALL original witness phase wires; A is every other mutable V wire, initially0. P=I_D tensor|0_A><0_A|, excluding immutable read-only data. Qv=V^dag C V; Av=P Qv P onRangeP. On the score event Av>=p0B, p0=2^(-ceil(m/20)-1), using512^20<2*495^20. The latter is an exact integer comparison; unlike the weaker previous bound it supports the actual shorter rotation cap below. The decoder-only B from Section6 hasTr rho B>=1-1/1024 except the already bounded unconditional good-label event.

For E=1_(Av<c p0), EBE<=cE. Hence
 ||E rho^(1/2)||_HS <=||E B^(1/2)rho^(1/2)||_HS+||(I-B^(1/2))rho^(1/2)||_HS <=sqrt(c)+sqrt(epsilon)
wheneverTr rho B>=1-epsilon, since(1-sqrt b)^2<=1-b. At c=epsilon=1/1024, initial spectral mass below a=p0/1024 is<=1/256. This bound does not assume A and B commute.

First make ONE binary Qv test: apply V, measure ONLY C; accept/output candidate, or on failure apply literalV^dag, leaving state inQv-perp. Put U=(I-2P)(I-2Qv), each factor an EXACT subspace phase reflection. I-2P computes all-zero(A) in a separate clean AND-tree apparatus, phases its single flag withZ and reverses the entire Boolean computation, returning apparatus0 on ANY A. I-2Qv is V, Z on C, literalV^dag. No source preparation inverse or reflection about the unknown D state occurs.

Choose J=2^(ceil((ceil(m/20)+11)/2)+4), so J>=16/sqrt(a) andJ=O(2^(m/40)). For at most16 trials choose fresh UNIFORM CLASSICAL j in[0,J) by log2J fair bits, apply U^j, then make the same binary Qv test and stop on acceptance. On failure literalV^dag returns toQv-perp. Charge all j<=J-1 words; discard only classical trial coins, never reset D/A or measure P. At timeout output0. The program acquires no additional originals.

In a Jordan blocklambda=sin^2theta for P,Qv, starting inQv-perp, acceptance afterj rotations is sin^2(2jtheta). Forlambda in[a,1-a], sin(2theta)=2sqrt(lambda(1-lambda))>=sqrt(2a). Geometric summation gives
 r_lambda=(1/J)sum_(j=0)^(J-1)sin^2(2jtheta)>=1/2-1/(2J|sin(2theta)|)>2/5.
On every failed Qv test, that block is AGAIN its unique Qv-perp direction. Thus independent classical choices j renew the same success rate; sixteen trials fail<= (3/5)^16<1/1024. This is exact Jordan-block renewal, not a conditional freshness assertion for the original witness. Cross-block/reference coherences do not affect trace probabilities because each map preserves the blocks. Forlambda>1-a the INITIAL Qv failure is< a; forlambda<a bound by its initialmass1/256. Total failure on score/good-label events is<=1/256+1/1024+a<.01. Degenerate lambda0/1 obey the limiting statements directly.

Safety is exact for dirty A: S=RangeP+Range(QvP) is invariant under P,Qv, their complements AND both reflections. Every reachable Qv-accept state lies inRange(QvP), and after V lies inRange(CVP), where the clean-input exact score marker forces the ENTIRE true candidate for every D/reference state. Globally dirty false-accept states elsewhere need not be sound. No fine-grained work measurement is used.

Union the unchanged source-label distance, two bounded range aborts, split, score and good-label failures with this conditional failure. Unconditional whole-secret success remains>2/3 for every N,s and the same literal fixed-joint fraction1/32. Fixed trial/rotation caps count every failure branch.

## 8. Finite fallback, same acquisitions/noise

For n<n0 use the SAMEQ/split/score; discard unused witnesses with full charge. On its events the score marker has exactly one solution inH0=2^n. Do16 independent trials: uniform classicalj in[0,J), J=2^(ceil(n/2)+2); initialize a fresh uniform candidate register, perform j exactGrover words for the marker, measure/check the candidate classically and return firstpassing. No new source copy is acquired.

For theta=asin(1/sqrtH0), mean trialsuccess is
 (1/J)sum_j sin²((2j+1)theta)=1/2-sin(4Jtheta)/(4Jsin2theta)>=1/2-1/(16sqrt2)>2/5,
usingJ>=4sqrtH0, sin2theta>=sqrt(2/H0). Failure<=(3/5)^16<1/1024, independently across fresh trial coins/search initializations on fixed score data. Same source/split/score union gives success>=2/3. WorkO(2^(n/2)poly(n)), spacepolynomial, exactQ. The finite setn<n0 has a finite maximum ratio to the declared envelopes, absorbed into an outside constant independent ofN,s,outcomes. No faster exponential rate is asserted on that finite prefix.

## 9. Joint whole ledger and exact degrees

For n>=n0, log2u<=n/2048: atn0, log2(n0+2)<21<n0/2048, and log2(x+2)/x decreases thereafter. Hence m<=2n, u^100<=L=2^(m/16), and N>=L³ since3r<=3n/8<=n-1. Rounding gives m<=n+64log2u+79 and L<=2^5*2^(n/16)*u^4. Every sum, signedquotient, cap, count, offset andaddress hasO(n)bits.

Sixteen raw lists,8pairnodes,4secondnodes,2thirdnodes and1root use a CONSTANT fifteen fixed duplicate joins. Each networklength S=O(Lu^100+u^200)=O(Ln^100). All arrays and histories are retained until literal inverse. Sorting/scans O(Sn²)recordoperations at conservativeO(n²)gates/savedbits peroperation giveO(Ln^104)gates/qubits for the WHOLEtree. Native4 full-address streaming generation costs amortizedO(n²)per elementarygate, setup included, so one oracle TOTAL O(Ln^106); extra quotient/hash/fullKscans fit.

H=L^11*Kk*K=O(L^11*n^201), K=O(n^200). Largest actualGroverpower O(sqrt(HK))=O(L^(11/2)*n^(401/2)); O(n)probe repeats/geometricpowers giveO(L^(11/2)*n^(403/2))oraclecalls. Full column/inverse costO(L^(13/2)*n^(615/2))=O(2^(13m/32)*n^(615/2)). LaterO(sqrtH)search, inverseindexerasure, source/score/selection/readout/zero-phase work fit. Every failed/inactive word and all initialization countsequentially.

PeakO(Ln^104)qubits includes all fifteen nodes, retained comparator/scan/Boolean histories, constantmany separate count/output regions, source/probe/coin/arithmetic fields and zero-phase apparatuslinear in mutableVqubits. Every oracle clears its solverhistory onEVERYsearchstate, so it is reused between repetitions. ThusSQ=O(2^(n/16)n^108). Classicalimmutable source/score Q O(n)-bitrecords plus generator/constants/offsets/counters/inputs/outputs fitO(n²); no exponentialclassicalarray/circuit. FULLglobal indexedfees have logM=O(n); quantum-chosen accesses are explicit scans/sorts.

Section7 actual shorter schedule hasO(2^(m/40))verifier/inverse/zero-phase words onEVERYbranch. Therefore
 T=O(2^(69m/160)*n^(615/2))=O(2^(69n/160)*n^(3351/10)),
since64*(69/160)=138/5 and615/2+138/5=3351/10. All source/preprocessing/failedwork/generation/address/cleanup/unusedallocation costs count. EXACTQ is acquired evenonabort/fallback; no restartchangesQ. Same finite-prefix8 suppliesallN<n0 with finiteoutsideconstants. ONEconfiguration holdsallfourresources andfraction1/32 jointly.

## 10. Scope, credit and provenance

Sixteen-list/PGM circuits and all quantified native lemmas are complete in this archive; tests/verdicts are not premises. The standard tools credited in0, comparison networks/prefix scans/schoolbook arithmetic and two-projector decomposition are not claimed invented. Related Helm–MayPQCrypto2020 subset-sum tradeoffs supply no assumedpreimage oracle. Earlier published source9fd0fa0e joint/RQ methods are rederived here, not substituted by its acceptance. The actual earlier submission documents its own local operational failures/compaction; no hosted judgment is asserted here. This changed reflection configuration requires its OWN fresh whole-proof review; no parent verdict is reused.

Randomized Grover-length/rotation credit: Boyer, Brassard, Høyer and Tapp, arXiv:quant-ph/9605034; amplitude amplification/estimation credit Brassard, Høyer, Mosca and Tapp, arXiv:quant-ph/0005055. The exact unknown-witness/spectral-tail/reachable-safety application is proved here, not imported as an uncosted oracle.
