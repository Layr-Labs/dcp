# RPF-TAIL-LOG-PACKET-ROBUST333: adaptive core/tail decoder with constant subspace reflections and strong inverse-linear full-joint noise

## 0. One algorithm, promise and joint theorem

The COMPLETE PA-LQ adaptive core/direct-tail/zero-bit padding/omitted hash/popcount/triangular4L cap/full-column method, COMPLETE lean comparator-history/scan/full-fee generator AND COMPLETE constant-p0 spectral/reflection/Jordan-renewal/reachable-range method are material from102f6f9d-a7b8-45a3-90b5-4eb66f3c3868. All are supplied fully here; none is claimed invented. The private full-bank split/finite stronger-noise score and reference-preserving physical bank framework is material from published13acaec4-f868-42c7-aff7-0b1734b8ff9d. Current develops the operator bad-score tail in2, ACTUALLY changes score threshold to1/6, uses selector d_selceil log2(4m) and ACTUALconstantJ1024 reflection schedule. Its exact malformedfraction is333/(1000n), not either source's promise. The new log-packet arity a0=floor(2m/(3ceil log2n)) and full physical ledger9 are re-established. The preceding one-pass drafts are actual development history, not selected outer words or accepted-result premises. Current requires its OWN fresh joint review.

For N>=2 write n=ceil(log2N), u=n+2, Q=3*2^40(n+32), q=Q/2, n0=2^256. ONE program below has unconditional full-secret success>=2/3 and simultaneous bounds
 T=O(n^(7/2)log2n*2^(n/2-(3/4)(log2n)^2+2(log2n)^(3/2))), S_C=O(n), S_Q=O(n^(9/2)/(log2n)^2),
 EXACT original acquisitions Q=3*2^40(n+32)=O(n).
Time index1, quantum index0, classical/sample indices0. Every branch is capped, including failure/unused originals, and all bit operations, gates, addresses, generation, initialization and memory count.

The literal malformed fraction is333/(1000n): an adversary fixes B, |B|<=floor(333Q/(1000n)), possibly depending onN,s. The joint state, with arbitrary inaccessible reference, has reduced state rho_s tensor(Q-|B|) on all other positions; bad systems may be arbitrarily entangled/correlated subject to that marginal. Mixtures over fixed B follow by linearity. No source control, preparation inverse or purification is available.

Acquire EXACTLY Q originals on EVERY branch and preprocess/split/score as1--2. If n<n0 execute8. Otherwise compute the COMPLETE growing choices in3 and execute the constant-reflection protocol6--7 with preimage word3--5 and the whole layout/fees in9. All five claims concern these SAME public choices and actual words. nextpow2, group powers and every parameter use bounded integer arithmetic, with no real-valued advice.

All constructions are supplied in this file, native.md and lean-native.md. Material source9fd0fa0e-7410-422f-a82d-67022c0c7cfc (published balanced sample program) receives credit for joint-source.md2 full-reference extraction/coupling and sources/RQ-SPLIT-proof.md3 finite eigenlabel probing. Its other engine, old output law/resource bounds and verdict are not premises. Standard credits: Bacon–Childs–vanDam2005, arXiv:quant-ph/0501044 (PGM/preimages); Marriott–Watrous2005, arXiv:cs/0506068 (binary in-place witness tests); Kitaev1995, arXiv:quant-ph/9511026 (eigenphase probes). No external native oracle is assumed.

## 1. Source and unconditional reference comparison

Let omega=e^(2pi i/N), chi_k=N^-1/2 sum_(x<N)omega^(-kx)|x>, phi_k=(|0>+omega^(ks)|1>)/sqrt2. Orthogonality gives exactly
 rho_s=(1/N)sum_k |phi_k><phi_k| tensor|chi_k><chi_k|.
Known ADD1 has eigenvalueomega^k onchi_k; extend ADDa by identity on padding x>=N. Privately uniformly translate position byj in[0,N), forgetj. The factor (1/N)sum_j omega^(j(k-l)) kills distinct valid k,l coherences, also against a reference. A bad padding/zero-mode coherence need not vanish; no separation of those modes is used. Each GOOD position has valid support globally by positivity of its marginal.

Each uniform range draw uses d=ceil(log2(2^40Q)) trials of ceil(log2range) fair bits, taking the first in range; conditional success is exactly uniform. A whole Q-draw procedure aborts with probability<=2^-40. Keep an abort flag but nevertheless acquire all Q originals. On success use the native2 nondemolition ADD eigenlabel instrument, t=n+4, reporting W modN with per-eigenstate error<=delta=2^-100n; measure probes and discard position, retaining phase qubit/W. Known translations act only on position, so every fixed probe transcript acts by a scalar onchi_k and never changesphi_k.

The exact twirl gives an analysis-only classical refinement of all good k. Their JOINT marginal is IID uniform, because the original good marginal is the stated product. Given all good k, the good phase subsystem is a PURE product; positivity forces it to factor from all bad/reference systems. The remaining state may depend onk. Define a comparison OUTPUT by replacing only GOOD reported W with its hiddenk, keeping every bad channel and reference unchanged. Couple actual/ideal outcomes using the same hidden k/probe transcripts: they differ only on a good report error. Full-reference trace distance<=Qdelta<2^-40. This is unconditional; do not condition uniform labels on successful extraction/bad reports. Later channels contract this distance. Work always refers to the physical capped instrument.

## 2. Private split and exact score with arbitrary correlated bad phases

After ALL Q acquisitions, privately Fisher-Yates permute full phase/W pairs using1's same capped uniform range primitive, abort<=2^-40. Conditional validity the permutation is exactly uniform and independent of source. Firstq=Q/2 records are verification, lastq the unknown witness. Write p=|B|/Q<=333/(1000n)<=333/1000. Main n>=n0 has DETERMINISTIC bankbadfraction<=2p<=333/(500n). In the finite prefix, for a half's hypergeometric bad countX, Var(X)<=q/4, so with eta=2^-20 Chebyshev and a union bound put BOTH bankfractions<=p+eta except probability1/(2q eta²)=1/(3(n+32))<=1/99. This depends only on fixed B/private coins, not labels, bad reports or phase outcomes. Because 333/1000+2^-20< p_star=1/3-1/4096, both main and finite events give bankbadfraction<=p_star. No main split concentration is required.

Measure each verification phase in an INDEPENDENT private fair X/Y axis beta=0,pi/2, outcomeZ=+/-1, after its label instrument. Store(W,beta_flag,Z) in allocated Rrec. Define score(a)=q^-1 sum Zcos(2pi*aW/N-beta). A GOOD term has mean1/2 for a=s and0 otherwise, by averaging beta then uniformW and character orthogonality. The GOOD reduced measurement law is an independent product; it is never conditioned on bad labels/reports/score success.

We supply the stronger BAD-SCORE bound, with no independence assumption on malformed copies. For fixedcandidatea, a realized bad labelW and theta=2pi*aW/N, the first-moment POVM operator of Y=Zcos(theta-beta) on its arbitrary phasequbit is
 A_theta=(cos(theta)X+sin(theta)Y_Pauli)/2,
with eigenvalues+/-1/2. For lambda>=0 and any outcome y in[-1,1], endpoint convexity gives exp(lambda y)<=cosh(lambda)+y sinh(lambda). Therefore its local positive MGF operator satisfies
 M_theta(lambda)<=cosh(lambda)I+sinh(lambda)A_theta
 <=(cosh(lambda)+(1/2)sinh(lambda))I
 <=exp(lambda/2+lambda²/2)I.
For the last scalar inequality, f(lambda)=log((3/4)e^lambda+(1/4)e^-lambda) has f(0)=0,f'(0)=1/2 and f''(lambda) the variance of a +/-1 variable, hence<=1; integrate twice. ReplacingYby-Y gives the same bound. All beta choices/local measurements are independent instruments, even when the input bad qubits are entangled. Conditional on ALL bad reported labels, for ANY joint bad state sigma (including a remaining reference),
 E exp(lambda sum_bad Y_i)=Tr sigma tensor_i M_theta_i(lambda)
 <=exp(b lambda/2+b lambda²/2).
The bound is uniform in every label sequence and conditional state, so averaging labels/reference preserves it. Markov with lambda=u/b gives BOTH tails
 Pr(|sum_bad Y_i|>b/2+u)<=2exp(-u²/(2b)).
For b=0 the sum is identically0. This is an operator-product norm bound; no factorization of bad states or conditional-good-label law is asserted.

Setu=q/2^20. Good Hoeffding and the preceding bad bound, using each count<=q, give total failure over ALL N candidate scores<=4N exp(-q/(2*2^40))=4N exp(-3(n+32)/4)<2^-30. Explicitly exp(3/4)>2 by the firstfour Taylor terms, and exp(24)>(8/3)^24>2^33 (exp1>8/3 and2^39>3^24); hence4Nexp(-3(n+32)/4)<4exp(-24)<2^-31. These are UNCONDITIONAL good and bad events intersected by a union bound, not good IID assertions after observing bad reports.

On these events and the bank bound, putting p_b=b/q<=p_star,
 score(s)>=(1-p_b)/2-p_b/2-2^-19
 >=1/6+1/4096-2^-19,
 score(a!=s)<=p_b/2+2^-19
 <=1/6-1/8192+2^-19.
Native2's ACTUAL fixed rational cosine polynomial has error<2^-190: its angle error<4*2^-900 and Taylor tail<2^-201 sum to less than2^-190. This stronger explicit bound uses the SAME generated coefficients, not extra precision advice. The ACTUAL changed Boolean marker is
 a<N AND 6 sum Z*C >= qD.
Its exact threshold1/6 lies STRICTLY between the two rational-score intervals above, since2^-19+2^-190<1/8192. Thus it accepts EXACTLY the ENTIRE s. It uses reserved clean scratch untouched by the decoder, giving clean-verifier soundness for EVERY witness/reference input. No success/score independence or malformed independence is assumed. The Rrec storage/channel and complete fees are2A/native.

## 2A. Actual record bank, reference law and O(n) classical controller

Rrec is a bank of ALLOCATED QUBITS of total sizeO(Qn)=O(n²), counted inSQ. Acquire ALLQrawsystemsfirst inO(Qn)qubits. Processonecopyat a time: measured/decodedW and verification(beta,Z) pass through a reusableO(n)-bit classicalrow, are written by classicallycontrolledX into a basisrow ofRrec, then the classicalrow is erased/reset at chargedcost. No classicaltranscript table remains. If the full measuredrecord/reference law is sum_r |r><r|_C tensor sigma_r, this write/erase channel produces EXACTLYsum_r |r><r|_Rrec tensor sigma_r. Thus allreferencecouplings in1 contract through it. Only measured basisinformation is copied; the unknownphase/reference state sigma_r is untouched.

OutsideV sourceprobe stages run t,t-1,..0, keeping currentcos/sin tallies, current six-bit gridangle and the currentO(n)-bitdyadic unwrapvalue. Native2's backwardsunwrap then discards completedtallies. PublicADD^(2^j)coefficients are regenerated by iterative doubling of1modN asneeded, not stored as a growingtable. Good conditionalchi_k probes act by scalars, so order doesnot change their independentoutcome/error proof; badsourcechannels remain arbitrary. Extra coefficientregeneration is polynomial insideO(n^9). Firstvalid capped range draws store only currentdraw/firstvalidvalue/flag/trialcounter; everyrawdraw is discarded/reset. Private Fisher–Yates usesCLASSICALrowindices and literalSWAPgates onphase/fullquantumlabelrows, so its uniformconditionalpermutation andabortlaws are unchanged withoutquantumaddresslookup. Allthese operations/resets/feescount.

After split/verificationRrec is immutable and CQdiagonal, with arbitrary conditionalD/reference states. V_R copies its witnesslabels byCNOT atPUBLICrowindices into quantumWwork; routing stillFULLSCANSq positions. The score's W/beta/Z are read-only Booleanquantumcontrols for the generic bounded arithmetic innative1-2. Eachrecordsector has the same clean mathematicaldecoder and exactunique-scorepredicate; the score arithmetic is separately charged polynomial work; the actual comparator-history and linear record words are specified in lean-native. No hostbranch depends on quantumrecordbits. Rrec never changes. On each realizedr,V_R is a blockV_r; the initialCQmixture and blockdiagonal gates give exactlythe conditional analyses3-7. The literalinverse is the NEWactualV_Rdag, not an asserted equality ofdirtyextensions to older compiledwords.

Put P=I_(D,Rrec) tensor|0_A><0_A|, withA EVERY mutableVwire and separate reflection apparatus returned0 after each use. Rrec is immutableINPUT, excluded fromP. ForQv=V_Rdag C V_R,7 proves spectral/Jordan renewal and invariantS=RangeP+Range(QvP) blockwise and on the CQmixture. Range(C V_R P) has ONLYthe entiretruecandidate on the scoreevent for everyD/referenceinput. UnknownD is never reset or reflected about as knownstate. Only binaryC tests and finalcandidate are measured; nofine-grainedA/P measurement. The main's ACTUALknownV_Rdag reverses everycurrentgate/scalar, without asserting identity of dirtyextensions to olderwords. Finitefallbackreloadsitsknownmeasuredcandidate and uses the SAME exactmarker; all resets/output/disposal count.

Classicalmemory inventory: publicN/n/Q/q/m/r/L/caps/H/j/J andinput/output; percopyrange/probe/unwrap/verificationrows; arithmeticoperand/result/remainder/accumulator buffers; and generatorloop/base/stride fields. There is a CONSTANTnumber ofO(n)-bitwords. Inplace schoolbookmultiplication uses fixed-widthoperand/resultaccumulation, restoringdivision usesquotient/remainder, and greedyroot usescandidate/trialsquare, eachO(n)space. PublicMachin terms haveO(n)-bitindividualdenominators and fixed-pointaccumulators(native2); no growingdenominator product or savedclassicalhistory is used. Degree400 and64gridpoints are FIXEDcounts. Allsource/probe histories insideV are QUANTUMancillas includedinSQ.

The ACTUAL emitter uses complete-A-leaf public heap/level/node loops, common node packet stride, ONE history flag per comparator, clean reused O(n) arithmetic and distinct forward-head/reverse-tail sequential scans. Lean-native supplies every Boolean operation/generator/fee. No circuit table, node directory or recursion frame stack is stored. Whole allocation is polynomial, giving FULL fee O(logn). The complete main inventory is9, not a fixed-tree or different-arity formula.

## 3. Adaptive nonpower-of-two core tree and unique direct-tail index

For mainn>=2^256 letm=n+160,k_n=ceil(log2n),a0=floor(2m/(3k_n)),b0=floor(log2a0)-ceil(log2k_n),z=2^b0,a=z*floor(a0/z). Section9 proves these are positive publicintegers. LetD=ceil(log2a),A=2^D,r=floor(m/a),m_c=ar,t=m-m_c,L=2^r. The firstm_c REALphasebits form a consecutive r-bitcoregroups; the lastt REALbits are the directlysearchedtail. Complete the balancedtree toA leaves with A-a ZERO-BITgroups. Eachsuchrawlist has EXACTLYONEpresentrecord(0,emptyID), paddingpresence0elsewhere; it has no source phase, extra input bit or representation multiplicity. PutCcap=nextpow2(8a),Pcap=2^160*Ccap*L,K=2^162,Kcarry=nextpow2(m_c+1). Allnonrootinternaloutputs havecapPcap,rootcapK; ANYoverflow rejectsWHOLEquery. Everyraw/nonroot/root/unary/empty/paddingregion is charged.

At publiclevelj=1..D-1 therearev_j=ceil(a/2^j) nonemptyreal-bit subtrees, the FIRSTv_j nodes. Choosev_j-1 FREEr-bit hashes there; derive the LASTNONEMPTYhash as(T_(j-1)-sumfreeh)modL. Everytrailing empty-onlynodehash is FORCED0, never a searchfield. StartT0=y_c+carry*N withy_c=(y-f_tail(u))modN andf_tail(u)=sum_tail W_i u_i modN. UpdateT_j=(T_(j-1)-sumNONEMPTYh)/L, exactsignedinteger. Eachactualpairjoin uses(qleft+qright)modL=h, outputquotient(qleft+qright-h)/L, unreducedrawsums andfullrealbitIDs. Unarynodes withoneemptychild are REALboundedjoins; theirhash isnotforced0 unlessBOTHchildrenempty. Empty-onlynodesproduceonly(0,emptyID) atforcedhash0. RootmatchesEXACTintegerqleft+qright=T_(D-1),sortscoreIDs canonicallyandFULLSCANSallKrank slots. Allcounts/flags/targets/histories are retained and literallyreversed bynative3.

The number ofsearchedfreehashes is
 F=sum_(j=1)^(D-1)(ceil(a/2^j)-1)=a-1-B, B=popcount(a-1).
Indeedceil(a/2^j)=floor((a-1)/2^j)+1 andsum_(j>=1)floor((a-1)/2^j)=a-1-popcount(a-1), withtermsj>=Dzero. SearchX comprisesDIRECTt-bit tailu, theseFr-bitfields, corecarryin[0,Kcarry), androotrankin[0,K), soH=2^t*L^F*Kcarry*K. Rejectcarry>m_c. The trailing-emptyhashes are NOTfreefieldsthatcostextraGroverdomain. Realcoreinputlengthism_c=ar, NOTAr; zero-bitgroups neverincreaseM0.

EachsurvivingFULLb=(bcore,u) hasf_W(b)=y modN andaUNIQUEindex: actualtailu, corecarry(sumcore-y_c)/N, each FREEactualsubtreehash,canonicalcorerootrank. Derivedlastnonemptyhashes/forcedzerohashes are determined bytheseconstraints andtotalcoretarget. Coincidentsumsretain distinctrealbitIDs. InverseF_Wy(b)extractstailu, recomputestailtarget/corecarry/everycorehash, runsSAMEcappedcompleteA-leaftreeincludingzero-bitgroups, andFULLSCANSthe rootforbcore/rank; absent/invalid0. A nonheavyFULLcolumnc_y<=K implies everyfixedtail/hashrootcount<=K. No core-onlydensity or independent-targetpromise is assumed.

Compute g(X), copyFULLb=(corepayload,u) andSINGLEtagNOTvalid, reverseALLg/tailtargetwork withX unchanged, THENcomputeF(B),XORitsENTIREindexincludingtailu intoX,andreverseFtempswithBunchanged. Thusmarkedbranchescleareveryhash/carry/rank/tailhelper. Everymarkedfullbitstring occurs once acrossalltailvalues, withcommonphaseomega^(s*y). Forcedemptyrawrecordsarenotphantomsourcebits; theirpresence1mattersforunaryjoins.

We prove a sharper UNIFORMbucket bound, essential to the polynomial physical cap. Fix an actual fullb and average over IID uniformW. A nonroot level-j node ofthecompleteA-leafpaddedtree contains h=2^(j-1) disjoint raw-group childpairs; some arezero-bitgroups. Alternates CANNOTchangeemptygroups, so allowedactivitysets form a SUBSETofthecomplete tree used below. The sameupperbounds thereforeapply, includingunarynodes. For an alternate assignment let S be its e changed childpairs; each has at mostL² alternatives. Define D_i as the UNREDUCEDalternate-minus-actual sum in that pair. Equality of all actual subtree hashes means eachD_i=0modL, each binary-pair sum=0modL², each four-pair sum=0modL³, up to node sum=0modL^j. No target/hash independence is assumed: these are exact DIFFERENCE constraints.

For each changed pair choose one original labelX_i with coefficient sigma_i=+/-1 inD_i. Condition all other labels; distinctX_i remain independent uniform[0,N). At every nonempty constraint-tree node pivot on its LEFTMOST active leaf. Nodes with pivoti form a consecutive chain of lengtht_i<=j; sum_i t_i=w(S), the number of nonempty constraint nodes. CountX_i RIGHTTOLEFT: the largest chain node imposes ONE affine congruence sigma_iX_i+c=0modL^t_i. Every lower chain constraint follows because removed siblings are empty or already satisfy their lower modulus constraints. Nodes pivoted to the right do not involveX_i. Thus the number of satisfying label choices is at most product_i ceil(N/L^t_i), with inconsistency reducing it. This is an explicit triangular affine elimination even for odd/compositeN.

Section9 proves N>=2hL^j. Putx=L^j/N, soex<=hx<=1/2. The ceiling product divided byN^e is at most L^-w(S)*(1+x)^e <=2L^-w(S): binomial coefficients are at moste^k, so(1+x)^e<=sum_(k>=0)(ex)^k<=2. The ceiling overhead is a SINGLEfactor2, not2^e. This stronger finite-precision estimate is why the old exponentially large bucket coefficient is unnecessary in THISnew physical configuration.

Define T_j=sum_(S INCLUDINGempty) L^(2|S|-w(S)) for the complete constraint tree ofheightj, h=2^(j-1) leaves. ExactlyT1=1+L and
 T_j=1+(T_(j-1)^2-1)/L.
Indeed the two independent child activity sets combine, and every nonempty combined set adds one root constraint. WithqL=1+1/L, induction yields T_j/L<=qL^(2^j-1): square the preceding bound and absorb the remaining1/L term into the extraqL, since its preceding power is>=1. Section9 givesL>=4h; hence(2h-1)/L<=1/2 and the same binomial/geometric argument givesqL^(2h-1)<=2. ThereforeT_j<=2L. Summing alternate assignments now bounds the expected uncapped actual bucket by
 1+2(T_j-1)<=4L,
UNIFORMLY over all growing levels. Child caps only remove entries. A fixedb is lost at a nonroot node only if its uncapped actual bucket exceedsPcap; sum Markov over ALLA-2<2a nonrootINTERNALnodes gives expected lost INPUTmass<=8aL/Pcap<=2^-160. Rawleavesarenotcapped; forcedempty-onlynodes haveonepresentzerorecordandcannotoverflow. No n-dependent factor is absorbed into a constant.

Put M0=2^m andmu=M0/N using ALLcore-and-tailbits. Then2^160<=mu<2^161. For distinct fullsubsets their moduloNcollision probability is1/N by a +/-1 label coefficient. Thus V(W)=(1/N)sum_y(c_y/mu-1)^2 hasEV<1/mu. On heavyc_y>K, v=K/mu-1>=1 and weighted INPUTmass is bounded byV(W)(v^-2+v^-1), with mean<=2/(mu*v)<=4/K=2^-160. Exclude heavy FULLcolumns ONLYinanalysis. On all other columns no fixed-tail root exceedsK. Setcprime to physical surviving count there and analysis0 on heavy columns; then ell=1-sum cprime/M0 obeysEell<=2^-159. The actual heavy-column unitary remains finite and capped. All averages are unconditional IIDgood-label averages, not labels conditioned on bad reports, uniform independent targets, or surviving hash queries.


## 4. Actual public-nominal-count positive preimage column

Put M0=2^m, mu=M0/N. These are PUBLIC rationals/integers, independent of W,y,s. Main-range m=n+160 gives2^160<=mu<2^161. Let cprime_y be the physical surviving marked count for nonheavy targets c_y<=K. In analysis only set cprime_y=0 on heavy columns, as in3; those entire columns are charged as lost input. The physical oracle/unitary always keeps its public caps and may behave arbitrarily on heavy inputs. No global quantumcount estimator, countcopy or countuncompute is executed. Exact bucket counts inside the bounded join remain ordinary explicit Boolean words.

Generate finitepi P_pi/D_pi as native2 with precision b=2log2H+40. Compute PUBLIC
 j=floor-sqrt(floor(P_pi²*H*N/(16D_pi²*M0))).
Its distance from(pi/4)sqrt(H/mu) is<2: finitepi scaling contributes<1/16, and floor-sqrt of a floored nonnegative rational equals floor of its real square root. All integers haveO(n)bits, and j generation/storage/full fees are counted. The ACTUAL loop executes EXACTLY these j iterations, not an old sqrtH loop with inactive controls. j=O(sqrt(H/mu)); both it and its inverse loop are fixed by the public input.

Start X uniformly on its power-of-two H domain and apply exact
 G=(2|u_H><u_H|-I)(I-2P_mark)
exactly j times. Every G genuinely invokes the bounded mark word; no fastpower is assumed. Native uses the positive diffusion scalar exactly. A fixed|1> helper supplies any minus compensation, then is cleared; no y-dependent phase is dropped. For physical count c, its two-dimensional angle is theta=asin(sqrt(c/H)) and marked amplitude sin((2j+1)theta). c0 has no marked component.

Let tau=2^-40. Call a target REGULAR if |c_y/mu-1|<=tau and d_y=c_y-cprime_y<=tau*mu. Then 0<cprime_y and |cprime_y/mu-1|<=2tau. Put z0=sqrt(mu/H), z=sqrt(cprime_y/H). Main-range K>=2mu andH=2^t*L^F*Kcarry*K imply z0<=L^(-F/2)<=2^-192<=2^-64<=tau/32, by the explicit Fr/2>=192 bound in9. Also z<=2z0<=1/4. Write j=pi/(4z0)+eta, |eta|<2. From z<=asinz<=z+z³, |sqrt(1+d)-1|<=|d| for|d|<=1/2, andpi<4,
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
 <=2^-79+2^-118<2^-78,
since3 gives Eell<=2^-159 andmu>=2^160,tau=2^-40. Heavy columns are nonregular under the analysis definition cprime0. These inequalities explicitly charge lost INPUT, rather than a uniform-y measure.

The good selected phase input is M0^-1/2 sum_b omega^(s f(b))|b>. Compute f(b) into read-only Y, apply U_y^dag toB/fresh0work, and coherently require B/allpreimageauxiliaries0. W,Y are excluded from that PGM-zero test. The intended surviving frequency vector is M0^-1/2 sum_y sqrt(cprime_y)omega^(sy)|y>. The zero-auxiliary vector error has squared block weights c_y/M0; distinctY blocks are orthogonal. Section4 bounds its norm by16tau+2sqrt(beta), so its mean is<=16tau+2sqrt(Ebeta). This uses the adjoint of a single prepared column in eachY block, not a whole-unitary operator-norm claim.

For full counts, Cauchy and the same secondmoment give expected L1 distance ofc_y/M0 from1/N at most sqrt(N/M0)<=2^-80. Its ideal correct-frequency amplitude alpha=sum_y sqrt(c_y)/sqrt(N*M0)>=1-L1/2, so mean failure<=2^-80. Removing input fractionell changes the frequency vector by<=sqrt(ell), since(sqrt c-sqrt cprime)²<=c-cprime. Retain the conservative allowance4sqrt(Eell).

Native2 known-ADD readout, with t=n+4 anddelta=2^-100n, identifies the true frequency with per-eigenstate error<=delta; negate its decoded label as specified there. Retain Y through acceptance. Orthogonal frequency eigenstates make the classical readout law a mixture, so no dimensionN error multiplier occurs. Comparing squared overlaps of norm-at-most-one frequency vectors changes success by at most twice their norm distance. Therefore the complete decoder mean failure is at most
 2^-80+4sqrt(Eell)+32tau+4sqrt(Ebeta)+delta
 <2^-80+2^-77+2^-35+2^-37+2^-100<2^-34<2^-20.  (5.1)
Use Eell<=2^-159,Ebeta<2^-78,tau=2^-40 anddelta=2^-100n. These are fixed adequate accuracy margins for the constant success target; no vanishing-error assumption is needed. Bad columns are handled by their weighted norm mass and the physical word remains finite; no artificial target rejection is executed.

## 6. Actual verifier and unconditional good-label completeness

Coherently choose an ordered m-subset of witnessD by Fisher-Yates range draws, d_sel=ceil(log2(4m)) trials each, retaining ALL fair raw coins. Validity>=3/4, and conditional validity gives EXACT uniform ordered subsets, independently of source values. Copy the immutable quantum Rrec label rows at PUBLIC row indices into quantum work and route each selected phase/label through a FULL q-position scan. All coin/buffer/routing work is polynomial. Coins remain orthogonal through acceptance, so the clean acceptance effect is the positive weighted average over returned subsets.

The malformed witness count is at mostTOTAL b<=333Q/(1000n). In mainn>=n0>=2^20, m=n+160<=n(1+1/4096) and m/q<2^-40. After any previous all-good draws, nextbadprobability<=b/(q-m). Consequently the union/Bernoulli bound gives conditional all-goodweight at least
 1-m*b/(q-m)
 >=1-(333/500)*(1+1/4096)/(1-2^-40)>1/3.
The strict rational lastinequality follows by crossmultiplication. Conditionalvalidity isexactuniform withoutreplacement, so sampler-valid/allgoodweight>= (3/4)(1/3)=1/4. Take ACTUALp0=1/4. No additive m/q penalty repeated n times is introduced; the nextbad bound uses the actualratio b/(q-m). No bad-setknowledge enters the circuit.

Let B be the normalized valid-all-good DECODER-ONLY effect requiring the true full candidate and the PGM-zero flag; 0<=B<=I. It does not consult score data. V is the coherent selector/routing, decoder4-5, known-ADD readout and exact score marker2 with dedicated untouched score scratch. C accepts only selector-valid/PGM-zero/candidate<N/score. On the score-uniqueness event its predicate equals the true-candidate predicate for EVERY input, so the actual clean acceptance effect A>=p0B. No such inequality is used off that event. V has no internal measurements.

Given ALL good hidden labels, the selected good phases are pure products factoring from the remaining bad/reference state; B ignores unselected/bad phases. Its mean completeness is(5.1) over the UNCONDITIONAL IID good-label marginal, irrespective of bad reports. Markov gives failure<=1/1024 for an event on which Tr(rho B)>=1-1/1024. Do not condition label uniformity on verification outcomes, score success, bad reports or previous survival. Intersect this event with the score/source events by a union bound; source-label distance is charged once.

## 7. Randomized subspace reflections, unknown witness and exact safety

D is ALL original witness phase wires; A is every other mutable V wire, initially0. P=I_(D,Rrec) tensor|0_A><0_A|, excluding immutable Rrec as specified in2A. Qv=V^dag C V; Av=P Qv P onRangeP. On the score event Av>=p0B with the ACTUAL constantp0=1/4 proved in6. The decoder-only B from Section6 hasTr rho B>=1-1/1024 except the already bounded unconditional good-label event.

For E=1_(Av<c p0), EBE<=cE. Hence
 ||E rho^(1/2)||_HS <=||E B^(1/2)rho^(1/2)||_HS+||(I-B^(1/2))rho^(1/2)||_HS <=sqrt(c)+sqrt(epsilon)
wheneverTr rho B>=1-epsilon, since(1-sqrt b)^2<=1-b. At c=epsilon=1/1024, initial spectral mass below a0=p0/1024 is<=1/256. This bound does not assume A and B commute.

First make ONE binary Qv test: apply V, measure ONLY C; accept/output candidate, or on failure apply literalV^dag, leaving state inQv-perp. Put U=(I-2P)(I-2Qv), each factor an EXACT subspace phase reflection. I-2P computes all-zero(A) in a separate clean AND-tree apparatus, phases its single flag withZ and reverses the entire Boolean computation, returning apparatus0 on ANY A. I-2Qv is V, Z on C, literalV^dag. No source preparation inverse or reflection about the unknown D state occurs.

Choose the ACTUAL constantJ=1024. Sincea0=p0/1024=1/4096, J=16/sqrt(a0). For at most16 trials choose fresh UNIFORM CLASSICAL j in[0,J) by log2J fair bits, apply U^j, then make the same binary Qv test and stop on acceptance. On failure literalV^dag returns toQv-perp. Charge all j<=J-1 words; discard only classical trial coins, never reset D/A or measure P. At timeout output0. The program acquires no additional originals.

In a Jordan blocklambda=sin^2theta for P,Qv, starting inQv-perp, acceptance afterj rotations is sin^2(2jtheta). Forlambda in[a0,1-a0], sin(2theta)=2sqrt(lambda(1-lambda))>=sqrt(2a0). Geometric summation gives
 r_lambda=(1/J)sum_(j=0)^(J-1)sin^2(2jtheta)>=1/2-1/(2J|sin(2theta)|)>2/5.
On every failed Qv test, that block is AGAIN its unique Qv-perp direction. Thus independent classical choices j renew the same success rate; sixteen trials fail<= (3/5)^16<1/1024. This is exact Jordan-block renewal, not a conditional freshness assertion for the original witness. Cross-block/reference coherences do not affect trace probabilities because each map preserves the blocks. Forlambda>1-a0 the INITIAL Qv failure is< a0; forlambda<a0 bound by its initialmass1/256. Total failure on score/good-label events is<=1/256+1/1024+a0<.01. Degenerate lambda0/1 obey the limiting statements directly.

Safety is exact for dirty A: S=RangeP+Range(QvP) is invariant under P,Qv, their complements AND both reflections. Every reachable Qv-accept state lies inRange(QvP), and after V lies inRange(CVP), where the clean-input exact score marker forces the ENTIRE true candidate for every D/reference state. Globally dirty false-accept states elsewhere need not be sound. No fine-grained work measurement is used.

Union the source-label distance, single capped translation-range abort, score and good-label event failures with this conditional failure. The private full-bank permutation has its charged capped-range abort; main bankbounds are deterministic. In finitefallback, the separate splitfailure<=1/99 is included as2/8 prescribe. Unconditional whole-secret success is>=2/3 under the SAME literal333/(1000n) promise for everyN,s. Every original was already acquired; all trial/rotation counts are fixed.

## 8. Finite fallback, same acquisitions/noise

For n<n0 use the SAMEQ/split/score; discard unused witnesses with full charge. On its events the score marker has exactly one solution inH0=2^n. Do16 independent trials: uniform classicalj in[0,J), J=2^(ceil(n/2)+2); initialize a fresh uniform candidate register, perform j exactGrover words for the marker, measurethecandidate and check it bythe coherentrecord-controlledmarker as2A, returningfirstpassing. No new source copy is acquired.

For theta=asin(1/sqrtH0), mean trialsuccess is
 (1/J)sum_j sin²((2j+1)theta)=1/2-sin(4Jtheta)/(4Jsin2theta)>=1/2-1/(16sqrt2)>2/5,
usingJ>=4sqrtH0, sin2theta>=sqrt(2/H0). Failure<=(3/5)^16<1/1024, independently across fresh trial coins/search initializations on fixed score data. Finite bankfailure<=1/99, scorefailure<2^-30, bounded source/range errors and (3/5)^16<1/1024 sum to less than1/10, so unconditional finite success>=2/3. WorkO(2^(n/2)poly(n)), spacepolynomial, exactQ. The finite setn<n0 has a finite maximum ratio to the declared envelopes, absorbed into an outside constant independent ofN,s,outcomes. No faster exponential rate is asserted on that finite prefix.

## 9. Actual robust log-packet program and entire charged resources

Write v=log2n, k_n=ceil(log2n). Main n>=2^256 uses EXACT3: m=n+160, a0=floor(2m/(3k_n)), b0=floor(log2a0)-ceil(log2k_n), z=2^b0, a=z floor(a0/z), D=ceil(log2a), A=2^D, r=floor(m/a), m_c=ar, t=m-m_c, L=2^r, B=popcount(a-1), F=a-1-B, Ccap=nextpow2(8a), Pcap=2^160 Ccap L, K=2^162, Kcarry=nextpow2(m_c+1), H=2^t L^F Kcarry K. Each integer is computed by bit lengths, shifts and bounded division; all widths<=O(n) and constantmany buffers suffice. REAL core bits are ar; A-a extra leaves contain ZERO bits and one presentzero record each, never extra phases/multiplicity. Entire tail0<=t<a is coherent in X and global diffusion; its full cleanup and commonphase are3.

### Parameter guards and exact exponent

For v>=256, k_n in[v,v+1), n/(2v)<=a0<=n/k_n, z<=a0/k_n, and a>=a0(1-1/k_n). The lower a0 follows from floor(2(n+160)/(3k_n))>=2n/(3(v+1))-1>=n/(2v); the upper follows from 2(n+160)/3<=n. Thus a>=n/(3v), a<=n/v and a<=A<2a. We have r>=3k_n/2-1, and in fact r>=floor(3k_n/2) since a<=a0<=2m/(3k_n). Also m/a0<=3k_n/2+1 because a0>=2m/(3k_n)-1 and m>=3k_n²; dividing by(1-1/k_n) gives m/a<=3k_n/2+4. Therefore
 3v/2-1<=r<=3v/2+6,
 n^(3/2)/2<=L<=64n^(3/2).
For the exponent below use the slightly sharper r>=3v/2-1; no false rounding of a half-integer is assumed.

As a multipleofz, a-1 has at least b0 trailing1 bits, so B>=b0. From a0>=n/(2v), floorlog a0>=v-log2v-2 and ceil(log2k_n)<=log2v+2, hence B>=v-2log2v-4. With B-1>=v-2log2v-5>0 and r>=3v/2-1,
 E=t/2+(1+F/2)r=m/2-(B-1)r/2
 <=n/2-(3/4)v²+(3/2)v log2v+(17/4)v+80.
Indeed expand the lower product; remaining -log2v-5/2 terms only improve this upper bound. For v>=256, log2v<=sqrt(v)/2 (equality at256, decreasing ratio thereafter), and (17/4)v+80<=(5/4)v^(3/2). Thus
 E<=n/2-(3/4)v²+2v^(3/2).
This uses the ACTUAL tail and popcount, not fictitious D-1 freehashes or rounded totalm.

All cap/column guards are explicit. L>=n^(3/2)/2>=2a at every nonroot level with h=2^(j-1), since A<2a implies4h<=A<=2a at the highest level; more precisely atj<=D-1,4h<=A<=2a, and L>=2a ensures L>=4h. We have L>=2a from above. Also D<=v+1 and r<=1.5v+6, so (D-1)r+log2(4a)<=2v²+8v+2<=n-1. Check v256 and divide by2^v; v²/2^v and v/2^v decrease thereafter. Hence N>=4aL^(D-1), so N>=2hL^j. K<=L, F>=a/2 because B<=D<=v+1 and a>=n/(3v), and Fr/2>=192. These verify every use of the COMPLETE uniform4L/input-weighted cap/heavy FULL-target argument3--4. All counts still use FULLm and mu in[2^160,2^161), never the core alone.

### Complete native layout and uniform generator

All A raw/empty packets, A-2 nonroot joins and separate root packet have constantmany padded public stage arrays at caps in3. Root uses Pcap+K, not a larger uncounted packet. Ccap<16a and K<=L give S=O(AaL)=O(a²L)=O(n²L/v²) WHOLE base rows. Original child/quotient/target histories remain in separate node blocks; parent carries constantmany O(n)-bit value/ID/presence/helper fields, not recursive payload histories. Raw empty records are actually allocated; all zero/padding/stage/copy/inverse regions count.

The ACTUAL sort is lean-native1: one predicate flag per bitonic comparison, immediately cleaned ripple helpers, controlled swaps, then literal reverse unswap/recompute-erase. Scan2 uses distinct head/tail flags and one retained prefix state per lane. Its clean bounded joins enumerate exactly3's pairs/canonical ranks/caps; arbitrary dirty inputs still have a literal inverse, with no equality to an older dirty extension required. No checkpoint pool, layer bridge or generic sort oracle is allocated.

At mostfive padding expansions give k_sort<=r+ceil(log2a)+179<=4v forv>=256; D_sort<=10v². Whole comparison flags O(Sv²) are below O(Sn). Base record/prefix/history/input/output regions and comparator flags cost O(Sn). Shared clean arithmetic plus source/Rrec/score/probe/selector/routing/tail polynomial auxiliaries add at most O(n^4) qubits. As a>=n/(3v) and L>=n^(3/2)/2, Sn>=c n^(9/2)/v² dominates n4. Thus entire SQ=O(Sn+n4)=O(Ln³/v²), giving EXACT
 S_Q=O(n^(9/2)/(log2n)^2), growthindex0.
Every measured record is an allocated basis qubit bank with the exact reference-preserving write/erase channel2A, never free classical storage.

For explicit reflection allocation, first reserve the ACTUAL V workspace M_base=O(Sn+n^4), including its PGM auxiliary-zero computation scratch, all flags/records/prefixes and polynomial source/score/selector regions. PGM Boolean zero tests use at most a constant multiple of their tested-wire count in indicators/AND nodes, so they fit O(Sn+n^4), are reversed after copying their one flag, and do not test their OWN temporary computation wires. Allocate a SEPARATE outer reflection apparatus Z_outer of O(M_base) qubits. V NEVER touches Z_outer. To implement I-2P, compute one indicator for EACH mutable V wire in A and their binary AND tree into Z_outer, phase the root by Z and reverse ALL indicators/tree gates. On EVERY A basis state, Z_outer returns exactly0. P tests ALL mutable V wires A, excludes unknown D/immutable Rrec, and does NOT test the separate Z_outer apparatus itself; work at reflection boundaries stays in its exact zero sector. There is no recursive self-test. The ENTIRE allocation including Z_outer is O(M_base), a constant-factor addition already covered by the stated Sn+n4 envelope, not an O(n4) bound on Z_outer alone. Each full test has O(M_base) gates and O(M_base*d_addr³) conservative pointer/native/address work, which fits O(Sn v³) (and polynomial auxiliaries since Sn dominates n4). Every apparatus wire is initialized, zeroed and disposed with that full fee. The tested wires may be laid out as one known mutableV region after the immutable inputs. Enumerate a power-of-two padded AND heap with public child indices2i and2i+1, prepare padding indicators1 and reverse them too. Constantmany O(d_addr)-bit node/current/base fields suffice; even O(d_addr³) fully charged schoolbook setup per node gives the stated conservative total, without a stored circuit or per-level pointer stack. No all-zero oracle or uncharged workspace is assumed.


The WHOLE polynomial allocation implies full d_addr=ceil(log2(M_alloc+2))=O(v). Every elementary address, scalar/bit instruction, initialization, zero test and disposal pays this full fee. Linear O(n)-gate record words use O(n) changed-pointer/setup bits by running pointers and minimal underflow counters; no n-bit multiplication or zero-test per gate occurs. Lean-native3 proves charged record costO(nv); O(Sv²) comparison/scan operations give whole mark O(Snv³)=O(Ln³v), including all flags and initialization/disposal. Raw additions have O(aLrn)<=O(Ln²) gates; corecarry/hash/target/inverse whole-query O(n³) arithmetic and full K scans fit this mark budget. All n-bit quantum arithmetic is explicitly charged, not treated as a public short integer.

For completeness public array/heap/node/cap/stride/layer/record pointers and their arithmetic use ACTUAL O(v)-bit minimum widths, since their values/whole allocation are polynomialn. Complete-A heap IDs are iterated with constantmany public level/node counters and closed heap formulas; no A-entry directory or n-bit recursion frame per level. At levelj freehash offsets are r times sum_(ell<j)(ceil(a/2^ell)-1); compute by bounded public shifts/additions or the identity sum_(ell=1)^h floor(u/2^ell)=u-floor(u/2^h)-popcount(u mod2^h), u=a-1. Full X starts with t tail bits, then these Fr hash bits, carry and rank. Target values remain quantum data; no quantum value selects a host address. Even conservatively O(v^6) public descriptor/heap/reconstruction work per layer across O(Av²) layers is O(nv7), inside Ln³v. Quantum label fields are still On; only public indices use short widths. Classical full N/nominalj/pi/source/probe/score/output buffers use constantmany O(n)-bit registers, giving ENTIRE S_C=O(n). Public j counter uses minimal underflow widths and amortized total O(j+n) flips, all at full fee.

### Entire constant-reflection algorithm, not just the mark

The INNER ACTUAL nominal count is j=O(2^(t/2)L^(F/2)sqrt n), since Kcarry=O(n), K/mu in(2,4]. Whole known-preimage column/PGM work is O(j*Ln³v+poly(n)), hence O(2^E n^(7/2)v+poly(n)). Source preprocessing, full fixed-joint/reference channel, private permutation, selector, eigenphase decoding, exact score, public finitepi/nominalj construction, output and disposal have conservative O(n^9) NONMARK work, paid separately. They are outside the inner j preimage Grover iterations, not falsely required to fit one polynomial-size mark. Inside those iterations only the bounded known preimage mark/diffusion, full inverse/index and their charged word above execute. Uniform Hadamards/global zero test on X have O(n) gates and fit too.

E>=n/3 throughout this main range: B<=D<=v+1 and r<=1.5v+6 yield E>=n/2-(v+1)(1.5v+6)/2, and (v+1)(1.5v+6)/2<=n/6 atv256 and decreases relative2^v. Also the submitted upper exponent is>=n/3 there. Thus all separately paid polynomial work fits the COMPLETE bound
 T=O(n^(7/2)log2n*2^(n/2-(3/4)(log2n)^2+2(log2n)^(3/2))), growthindex1.
Main uses the ACTUALconstant-p0=1/4 reflection schedule6--7: initial binaryQvtest and atmost16 randomized known-reflection trials withACTUALJ1024. This changes whole chargedwork by a FIXED constant only, including ALL failed/capped/reflection/native/address/disposal operations; the separate outer zero-test apparatus is allocated LINEARLY in the complete V workspace as detailed above. Selectorcapceil log2(4m) and marker6sum>=qD are ACTUALknownwords. Full unconditionalentire-secret success>=2/3 underEXACTfixed-jointfraction333/(1000n) follows7; finiteprefixn<2^256 uses8 and finitebankfailure<=1/99 plus scoretail<2^-30. EXACTQ3*2^40(n+32) originals acquiredonEVERYbranch. All finite maximum resource ratios are absolute outside constants. Jointindices1,0,0,0. This actual grouping/score/selector/reflection configuration improves the source log²timecoefficient and quantum polynomial exponent while supplying a stronger fraction with the SAME fixed-joint model. No optimal tolerance, smaller numeric timeindex or practicalfinite-size claim is made.

## 10. Scope, credit and provenance

Growing-tree/PGM circuits and all quantified native lemmas are complete in this archive; tests/verdicts are not premises. The standard tools credited in0, comparison networks/prefix scans/schoolbook arithmetic and two-projector decomposition are not claimed invented. Related Helm–MayPQCrypto2020 subset-sum tradeoffs supply no assumedpreimage oracle. Earlier published source9fd0fa0e joint/RQ methods are rederived here, not substituted by its acceptance. The actual earlier submission documents its own local operational failures/compaction; no hosted judgment is asserted here. This changed record-bank/controller configuration requires its OWN fresh whole-proof review; no parent verdict is reused.

Randomized Grover-length/rotation credit: Boyer, Brassard, Høyer and Tapp, arXiv:quant-ph/9605034; amplitude amplification/estimation credit Brassard, Høyer, Mosca and Tapp, arXiv:quant-ph/0005055. The actual constant-reflection success is proved in6--7 and randomized finite-prefix Grover law in8; no external oracle is assumed.
