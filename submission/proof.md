# RPF-PA2-LQ: polynomial quantum space with linear original acquisitions

## 0. One program, supported fractional model and joint bounds

The actual lean adaptive implementation is material from this session's complete PA-LQ candidate; exact source IDs/publication statuses are disclosed in the public note and dependency declaration. Its own review is not a theorem premise. The complete adaptive/direct-tail/uniform4L engine is material from published RPF-PA 9a885b1c-7cc9-4f6b-99d1-d0e46cbc33cd. The measured-record quantum bank and streamed classical inventory are material from RPF-16Q fbdd86c2-74f7-4dd2-a876-7f512146233d. The larger log-squared fraction and literal longer J are developed in this session's earlier unsubmitted PA2 draft. Their score and spectral arguments are fully supplied here. The new lean record/helper/scan/generator word was developed in this session's RPF-8L work; its first local review rejected ambiguous reverse-scan boundaries, now explicitly corrected to DISTINCT tail flags. No earlier verdict is a mathematical premise, and this adaptive construction requires its own fresh joint review. Every selected source, coupling, score, column, safety and native method is fully supplied.

For N>=2 let n=ceil(log2N), Q=3*2^40(n+32), q=Q/2,n0=4096. ONE program has unconditional ENTIRE-secret success>=2/3, and on EVERY branch
 T=O(2^(n/2-(1/4)*(log2n)^2)*n^4*log2n),
 S_C=O(n), S_Q=O(n^5/(log2n)^2),
 EXACTQ=3*2^40(n+32)=O(n).
Their growth indices are1,0,0,0. The time guarantee is NOT subexponential time. Constants and all full addresses/generation/initialization/failed work count. No optimality or all-coordinate dominance is claimed.

The literal fraction isepsilon(n)=(log2n)^2/(32n). In the structured fractional expression ONLY, L denotes log2(n); the separate tree variable L=2^r retains its previous meaning. Before private coins, an adversary fixes B with |B|<=floor(Q*(log2n)^2/(32n)), possibly depending onN,s. The complete joint source/reference state is arbitrary subject to the reduced state on all other original positions being EXACTLYrho_s tensor(Q-|B|). Bad systems may be entangled/correlated with good ones and arbitrary inaccessible reference subject to that promise. Fixed-set mixtures follow by linearity. No source control, preparation inverse or purification is supplied. This is an explicit fractional guarantee, not a per-copy probability or a count claim converted through an upper sample bound.

Acquire EXACTLYQ on every branch, preprocess1 and score the firstq records2; retain lastq phases asD. There is NO global position permutation. If n<n0 use8. Otherwise m=n+160,k_n=ceil(log2n),a0=floor(m/(2k_n)),b0=floor(log2a0)-ceil(log2k_n),z=2^b0,a=z floor(a0/z),D=ceil(log2a),A=2^D,r=floor(m/a),m_c=ar,t=m-m_c,L=2^r. Corehas a REALr-bitgroups plus A-a ZERO-BITemptygroups. SetCcap=nextpow2(8a),Pcap=2^160*Ccap*L,K=2^162,Kcarry=nextpow2(m_c+1),B=popcount(a-1),F=a-1-B,H=2^t*L^F*Kcarry*K. These are public exact integers. Run6-7 with the actual bounded column3-5 and ACTUALJ=1024*2^ceil(k_n^2/4). All five claims belong to these SAME choices.

Published-source/primary credits: earlier balanced source supplies the full-reference hidden-label channel/coupling and finite eigenlabel probes, re-established in1/native2. PGM/preimage background: Bacon-Childs-vanDam, arXiv:quant-ph/0501044; eigenphase probes: Kitaev, quant-ph/9511026; in-place witness tests: Marriott-Watrous, cs/0506068; randomized lengths/amplification: Boyer-Brassard-Hoyer-Tapp, quant-ph/9605034, and Brassard-Hoyer-Mosca-Tapp, quant-ph/0005055. Generalized-birthday filtering background: Wagner, CRYPTO2002, with Camion-Patarin precedence noted on the author's page https://people.eecs.berkeley.edu/~daw/papers/genbday.html . Hierarchical filtering is not claimed invented here. No outside native oracle or prior asymptotic cost theorem is assumed.

## 1. Source and unconditional reference comparison

Let omega=e^(2pi i/N), chi_k=N^-1/2 sum_(x<N)omega^(-kx)|x>, phi_k=(|0>+omega^(ks)|1>)/sqrt2. Orthogonality gives exactly
 rho_s=(1/N)sum_k |phi_k><phi_k| tensor|chi_k><chi_k|.
Known ADD1 has eigenvalueomega^k onchi_k; extend ADDa by identity on padding x>=N. Privately uniformly translate position byj in[0,N), forgetj. The factor (1/N)sum_j omega^(j(k-l)) kills distinct valid k,l coherences, also against a reference. A bad padding/zero-mode coherence need not vanish; no separation of those modes is used. Each GOOD position has valid support globally by positivity of its marginal.

Each uniform range draw uses d=ceil(log2(2^40Q)) trials of ceil(log2range) fair bits, taking the first in range; conditional success is exactly uniform. A whole Q-draw procedure aborts with probability<=2^-40. Keep an abort flag but nevertheless acquire all Q originals. On success use the native2 nondemolition ADD eigenlabel instrument, t=n+4, reporting W modN with per-eigenstate error<=delta=2^-100n; measure probes and discard position, retaining phase qubit/W. Known translations act only on position, so every fixed probe transcript acts by a scalar onchi_k and never changesphi_k.

The exact twirl gives an analysis-only classical refinement of all good k. Their JOINT marginal is IID uniform, because the original good marginal is the stated product. Given all good k, the good phase subsystem is a PURE product; positivity forces it to factor from all bad/reference systems. The remaining state may depend onk. Define a comparison OUTPUT by replacing only GOOD reported W with its hiddenk, keeping every bad channel and reference unchanged. Couple actual/ideal outcomes using the same hidden k/probe transcripts: they differ only on a good report error. Full-reference trace distance<=Qdelta<2^-40. This is unconditional; do not condition uniform labels on successful extraction/bad reports. Later channels contract this distance. Work always refers to the physical capped instrument.

## 2. Fixed verification bank and exact score soundness

After all Q acquisitions, use the FIRST q phase/W records for verification and the LAST q for the unknown witness bankD. There is NO global source-position permutation. If the fixed malformed set has b<=floor(Q*(log2n)^2/(32n)) positions, either bank has bad fraction at most b/q<=(log2n)^2/(16n)<=3/32, deterministically. ForALLn>=1 putv=log2n>=0. Themaximumofv²2^-v is4/(e²(ln2)²)<9/7<3/2: derivativevanishesat2/ln2, ln2>2/3 bythemidpointintegral, ande²>7 becausethefirstfiveexp(2)Taylor terms sumto7withpositivetail. Thus thedeclaredfractionhasthisuniformboundevenonfinitefallbackn. This does not infer independence of bad reports or condition good labels on them. Mixtures of fixed sets follow by linearity.

Measure verification phases in independent fair X/Y axes beta=0,pi/2, outcomes Z=+/-1; retain(W,beta_flag,Z). Define score(a)=q^-1 sum Z*cos(2pi*aW/N-beta). A good term has mean1/2 for a=s and0 otherwise: averaging the axes gives(1/2)cos(2pi*(a-s)W/N), then uniform goodW gives character orthogonality. The joint good marginal supplies independent good terms UNCONDITIONALLY, even though bad outputs can be correlated with them. Hoeffding for[-1,1] bounds a good-sum deviation q/16 by2exp(-q/512); union over all N candidates is<2^-40. Bound every bad contribution by its count, without conditioning on bad data. Thus, for every n>=1 including the finite fallback,
 score(s)>=(1-3/32)/2-3/32-1/16=19/64,
 score(a), a!=s, <=3/32+1/16=5/32.
Native2's exact common-denominator rational cosine polynomial has uniform error<1/128. The Boolean marker a<N AND4sum Z*C>=qD therefore accepts EXACTLYs, since19/64-1/128>1/4>5/32+1/128. It uses reserved clean scratch untouched by earlier stages. Hence clean-verifier soundness holds for EVERY witness/reference input, not just honest decoder outputs. Score records remain immutable. No random-split failure event is needed or charged.

## 2A. Actual record bank, reference law and O(n) classical controller

Rrec is a bank of ALLOCATED QUBITS of total sizeO(Qn)=O(n²), counted inSQ. Acquire ALLQrawsystemsfirst inO(Qn)qubits. Processonecopyat a time: measured/decodedW and verification(beta,Z) pass through a reusableO(n)-bit classicalrow, are written by classicallycontrolledX into a basisrow ofRrec, then the classicalrow is erased/reset at chargedcost. No classicaltranscript table remains. If the full measuredrecord/reference law is sum_r |r><r|_C tensor sigma_r, this write/erase channel produces EXACTLYsum_r |r><r|_Rrec tensor sigma_r. Thus allreferencecouplings in1 contract through it. Only measured basisinformation is copied; the unknownphase/reference state sigma_r is untouched.

OutsideV sourceprobe stages run t,t-1,..0, keeping currentcos/sin tallies, current six-bit gridangle and the currentO(n)-bitdyadic unwrapvalue. Native2's backwardsunwrap then discards completedtallies. PublicADD^(2^j)coefficients are regenerated by iterative doubling of1modN asneeded, not stored as a growingtable. Good conditionalchi_k probes act by scalars, so order doesnot change their independentoutcome/error proof; badsourcechannels remain arbitrary. Extra coefficientregeneration is polynomial insideO(n^9). Firstvalid capped range draws store only currentdraw/firstvalidvalue/flag/trialcounter; everyrawdraw is discarded/reset. There is NO global permutation: first q rows form the fixed score bank and last q form D. Verification rows are measured and streamed in that fixed order. The source range abort remains exactly Section1's capped translation abort. Allthese operations/resets/feescount.

After fixed-bank verificationRrec is immutable and CQdiagonal, with arbitrary conditionalD/reference states. V_R copies its witnesslabels byCNOT atPUBLICrowindices into quantumWwork; routing stillFULLSCANSq positions. The score's W/beta/Z are read-only Booleanquantumcontrols for the generic bounded arithmetic innative1-2. Eachrecordsector has the same clean mathematicaldecoder and exactunique-scorepredicate; the fixed-degree score arithmetic is separately charged polynomial work; its quantum histories are included in Section9. No hostbranch depends on quantumrecordbits. Rrec never changes. On each realizedr,V_R is a blockV_r; the initialCQmixture and blockdiagonal gates give exactlythe conditional analyses3-7. The literalinverse is the NEWactualV_Rdag, not an asserted equality ofdirtyextensions to older compiledwords.

Put P=I_(D,Rrec) tensor|0_A><0_A|, withA EVERYmutableV_Rwire, includingWwork/probes/coins/arithmetic/histories. Rrec is immutableINPUT and is NOTzerotested. WithQv=V_Rdag C V_R, proof7's spectralinequality, Jordanrenewal and invariantRangeP+Range(QvP) apply blockwise and totheCQmixture. Range(C V_R P) has exactlythe truecandidate onthe scoreevent for everyD/referenceinput. The unknownD is never reset/reflectedabout as a knownstate. In fallback8 check a measuredcandidate by reloadingthatknowncandidate, computingthe SAMErecord-controlled marker and measuringitsoneflag; chargeclearing/resets. This preserves the unique-score searchlaw usingO(n)classicaloutcome/outputstorage and no additionaloriginal.

Classicalmemory inventory: publicN/n/Q/q/m/r/L/caps/H/j/J andinput/output; percopyrange/probe/unwrap/verificationrows; arithmeticoperand/result/remainder/accumulator buffers; and generatorloop/base/stride fields. There is a CONSTANTnumber ofO(n)-bitwords. Inplace schoolbookmultiplication uses fixed-widthoperand/resultaccumulation, restoringdivision usesquotient/remainder, and greedyroot usescandidate/trialsquare, eachO(n)space. PublicMachin terms haveO(n)-bitindividualdenominators and fixed-pointaccumulators(native2); no growingdenominator product or savedclassicalhistory is used. Degree400 and64gridpoints are FIXEDcounts. Allsource/probe histories insideV are QUANTUMancillas includedinSQ.

The actual generator is iterative with CONSTANT nesting depth. It enumerates level/node indices of the complete A-leaf heap and computes node/child bases from public heap formulas and a uniform power-of-two packet stride. It stores no A-entry directory and no recursive host stack. Inside each node, bitonic, sequential scan, arithmetic and fixed Boolean templates use constant many loop counters. Inverse words run the same loops backwards. Section9 and lean-native3 charge every setup, pointer operation, gate generation and full address fee.

Rrec/source/staging/copies addO(n²)qubits and polynomialwork, included in Section9's O(a²Ln) quantum peak and full whole-program time bound. Basisrecords are not free: their initialization, write/erase, knownrowSWAP/CNOT/data-control gates and FULLglobaladdressfees are charged. Alltime/SQ/Q/fraction choices remain thoseof0; the newstorage/controller is ONEprogram satisfyingthe improvedSC bound jointly.

## 3. Adaptive nonpower-of-two core tree and unique direct-tail index

For mainn>=4096 letm=n+160,k_n=ceil(log2n),a0=floor(m/(2k_n)),b0=floor(log2a0)-ceil(log2k_n),z=2^b0,a=z*floor(a0/z). Section9 proves these are positive publicintegers. LetD=ceil(log2a),A=2^D,r=floor(m/a),m_c=ar,t=m-m_c,L=2^r. The firstm_c REALphasebits form a consecutive r-bitcoregroups; the lastt REALbits are the directlysearchedtail. Complete the balancedtree toA leaves with A-a ZERO-BITgroups. Eachsuchrawlist has EXACTLYONEpresentrecord(0,emptyID), paddingpresence0elsewhere; it has no source phase, extra input bit or representation multiplicity. PutCcap=nextpow2(8a),Pcap=2^160*Ccap*L,K=2^162,Kcarry=nextpow2(m_c+1). Allnonrootinternaloutputs havecapPcap,rootcapK; ANYoverflow rejectsWHOLEquery. Everyraw/nonroot/root/unary/empty/paddingregion is charged.

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

The malformed count inwitnessbank is atmostTOTALb<=Q*(log2n)^2/(32n). Mainm<=2n,m<=q/2give nextbadprobability<=b/(q-m)<=(log2n)^2/(8n)=x<=3/16<1/2, bytheuniformratioinequalityin2. Afteranypreviousgooddrawsthisstillboundsthenextbadprobability. Concavityoflog2(1-x) aboveitschordon[0,1/2]giveslog2(1-x)>=-2x. Thusconditionalallgoodweight>=(1-x)^m>=2^-2mx>=2^(-(log2n)^2/2). Samplervalidweight>=3/4;usep0=(1/2)*2^(-(log2n)^2/2). ThisboundneverconditionsIIDlabels onbadreports,scoreorsurvival. At n=1literalerrorfraction0andfinitefallback applies.

Let B be the normalized valid-all-good DECODER-ONLY effect requiring the true full candidate and the PGM-zero flag; 0<=B<=I. It does not consult score data. V is the coherent selector/routing, decoder4-5, known-ADD readout and exact score marker2 with dedicated untouched score scratch. C accepts only selector-valid/PGM-zero/candidate<N/score. On the score-uniqueness event its predicate equals the true-candidate predicate for EVERY input, so the actual clean acceptance effect A>=p0B. No such inequality is used off that event. V has no internal measurements.

Given ALL good hidden labels, the selected good phases are pure products factoring from the remaining bad/reference state; B ignores unselected/bad phases. Its mean completeness is(5.1) over the UNCONDITIONAL IID good-label marginal, irrespective of bad reports. Markov gives failure<=1/1024 for an event on which Tr(rho B)>=1-1/1024. Do not condition label uniformity on verification outcomes, score success, bad reports or previous survival. Intersect this event with the score/source events by a union bound; source-label distance is charged once.

## 7. Randomized subspace reflections, unknown witness and exact safety

D is ALL original witness phase wires; A is every other mutable V wire, initially0. P=I_(D,Rrec) tensor|0_A><0_A|, excluding immutable Rrec as specified in2A. Qv=V^dag C V; Av=P Qv P onRangeP. On the score event Av>=p0B with the ACTUAL p0=(1/2)*2^(-(log2n)^2/2) proved in6. The decoder-only B from Section6 hasTr rho B>=1-1/1024 except the already bounded unconditional good-label event.

For E=1_(Av<c p0), EBE<=cE. Hence
 ||E rho^(1/2)||_HS <=||E B^(1/2)rho^(1/2)||_HS+||(I-B^(1/2))rho^(1/2)||_HS <=sqrt(c)+sqrt(epsilon)
wheneverTr rho B>=1-epsilon, since(1-sqrt b)^2<=1-b. At c=epsilon=1/1024, initial spectral mass below a0=p0/1024 is<=1/256. This bound does not assume A and B commute.

First make ONE binary Qv test: apply V, measure ONLY C; accept/output candidate, or on failure apply literalV^dag, leaving state inQv-perp. Put U=(I-2P)(I-2Qv), each factor an EXACT subspace phase reflection. I-2P computes all-zero(A) in a separate clean AND-tree apparatus, phases its single flag withZ and reverses the entire Boolean computation, returning apparatus0 on ANY A. I-2Qv is V, Z on C, literalV^dag. No source preparation inverse or reflection about the unknown D state occurs.

Choose the ACTUAL POWER-OF-TWO J=1024*2^ceil(k_n²/4),k_n=ceil(log2n). Herea0=p0/1024=2^(-(log2n)^2/2)/2048, soJ>=16/sqrt(a0)=512sqrt2*2^((log2n)^2/4). Formainn>=4096,a0<=1/4096. Thepublicintegerk_n/multiply/ceil/powerandJcounterarebounded: log2J=O((log2n)^2)<=O(n),using2. UniformjthususesEXACTlog2J fairbits; noapproximate/transcendentalparameteriscomputedincircuit. For at most16 trials choose fresh UNIFORM CLASSICAL j in[0,J) by log2J fair bits, apply U^j, then make the same binary Qv test and stop on acceptance. On failure literalV^dag returns toQv-perp. Charge all j<=J-1 words; discard only classical trial coins, never reset D/A or measure P. At timeout output0. The program acquires no additional originals.

In a Jordan blocklambda=sin^2theta for P,Qv, starting inQv-perp, acceptance afterj rotations is sin^2(2jtheta). Forlambda in[a0,1-a0], sin(2theta)=2sqrt(lambda(1-lambda))>=sqrt(2a0). Geometric summation gives
 r_lambda=(1/J)sum_(j=0)^(J-1)sin^2(2jtheta)>=1/2-1/(2J|sin(2theta)|)>2/5.
On every failed Qv test, that block is AGAIN its unique Qv-perp direction. Thus independent classical choices j renew the same success rate; sixteen trials fail<= (3/5)^16<1/1024. This is exact Jordan-block renewal, not a conditional freshness assertion for the original witness. Cross-block/reference coherences do not affect trace probabilities because each map preserves the blocks. Forlambda>1-a0 the INITIAL Qv failure is< a0; forlambda<a0 bound by its initialmass1/256. Total failure on score/good-label events is<=1/256+1/1024+a0<.01. Degenerate lambda0/1 obey the limiting statements directly.

Safety is exact for dirty A: S=RangeP+Range(QvP) is invariant under P,Qv, their complements AND both reflections. Every reachable Qv-accept state lies inRange(QvP), and after V lies inRange(CVP), where the clean-input exact score marker forces the ENTIRE true candidate for every D/reference state. Globally dirty false-accept states elsewhere need not be sound. No fine-grained work measurement is used.

Union the source-label distance, single capped translation-range abort, score and good-label event failures with this conditional failure. No global permutation/split failure event exists. Unconditional whole-secret success is>=2/3 under the SAME literal(log2n)^2/(32n) promise for everyN,s. Every original was already acquired; all trial/rotation counts are fixed.

## 8. Finite fallback, same acquisitions/noise

For n<n0 use the SAMEQ/fixed-bank/score; discard unused witnesses with full charge. On its events the score marker has exactly one solution inH0=2^n. Do16 independent trials: uniform classicalj in[0,J), J=2^(ceil(n/2)+2); initialize a fresh uniform candidate register, perform j exactGrover words for the marker, measure the candidate, reload it as a known quantum value, compute the SAME Rrec-controlled marker in clean scratch, measure its flag and return first passing, as2A; store only the current O(n)-bit candidate classically. No new source copy is acquired.

For theta=asin(1/sqrtH0), mean trialsuccess is
 (1/J)sum_j sin²((2j+1)theta)=1/2-sin(4Jtheta)/(4Jsin2theta)>=1/2-1/(16sqrt2)>2/5,
usingJ>=4sqrtH0, sin2theta>=sqrt(2/H0). Failure<=(3/5)^16<1/1024, independently across fresh trial coins/search initializations on fixed score data. Same source/score union gives success>=2/3. WorkO(2^(n/2)poly(n)), spacepolynomial, exactQ. The finite setn<n0 has a finite maximum ratio to the declared envelopes, absorbed into an outside constant independent ofN,s,outcomes. No faster exponential rate is asserted on that finite prefix.

## 9. Joint allocation and work for the adaptive lean word

All actual adaptive parameters of Section 3 remain unchanged. Put v=log2 n,
k=ceil(v), m=n+160, a0=floor(m/(2k)), b0=floor(log2 a0)-ceil(log2 k),
z=2^b0, a=z floor(a0/z), A=2^ceil(log2 a), r=floor(m/a), t=m-ar,
L=2^r, Ccap=nextpow2(8a), Pcap=2^160 Ccap L. Empty groups have ZERO
source bits and exactly one present zero record. There is no global source
permutation. The first q records are verification records and the last q
are the unknown witness. The literal tolerance is (log2n)^2/(32n); the ACTUAL longer reflection schedule is Section7's power-of-two J.

The following public bounds are independent of the new implementation.
For k>=12, induction gives 2^(k-1)>=4k² and
2k²+5k<=2^(k-1)-1. As n>2^(k-1), n>=4k². We obtain
 a0>=2k-1>=2^ceil(log2 k), b0>=0, z<=a0/k,
 a>=a0-z>=m/(2k)-m/(2k²)-1>=m/(2k+4).
The last inequality follows from m>=2k²(k+2)/(k-2), itself implied by
m>=4k² and k>=6. Consequently 2k<=r<=2k+4 and
 n²<=L<=64n², 64<=a<=n, a<=m/(2k)<=n/v.
The last bound uses n>=160. Also A<=2a, D=ceil(log2 a)<=k,
D+1<=a/2, B=popcount(a-1)<=D and F=a-1-B>=a/2.
Thus Fr/2>=384, as required by the nominal-column accuracy ledger.

Every nonroot height j<=D-1 satisfies j(r+1)<=k(2k+5)<=n-1.
Hence 2hL^j<=2^(n-1)<N for 2h=2^j, and 4h<=A<=2a<=L.
Both hypotheses of Section 3's uniform 4L activity lemma hold, including
unary and empty subtrees. Forbidden changes to empty groups restrict the
activity families, so do not invalidate the upper bound. There are A-2<2a
nonroot INTERNAL nodes. Expected lost INPUT mass is at most
8aL/Pcap<=2^-160. The root weighted-heavy and public-nominal error
estimates remain those of Sections 3--5 for this actual full m-bit domain.

The NEW physical layout uses complete power-of-two packets at all public
heap nodes, including raw, unary, empty-only and root nodes. Each packet
has constant many arrays of power-of-two length O(Pcap), power-of-two
record/field strides, sequential prefix arrays, and one bit per bitonic
comparison. Raw real lists fill only their first L present records; empty
lists fill only one present zero record. All other slots have presence0.
Their initialization, padding and inverse words are executed and charged.
Root rank still FULLSCANS K slots; root padding creates no marked index.
With Ccap<16a and K<=Pcap, whole lane count is S=O(a²L).

Lean-native Sections 1--3 specify the actual clean linear record words,
one saved flag per comparison, reusable scratch and sequential scans with
DISTINCT forward head and reverse tail boundary arrays. Each record has
constant many O(n)-bit fields, including full real IDs and signed targets.
The largest sort has log M=O(log n). Across every node the gates are
O(S n(log n)²) and persistent quantum storage is
O(S(n+(log n)²))=O(Sn). Scan arrays and both boundary arrays are counted.
Raw generation uses O(Lmn) gates and fits this bound: a>=n/(2k+4)
and k>=12 imply a²(log n)²>=c n, with an absolute positive c.
Target/hash/carry/inverse arithmetic and full K scans are bounded
polynomial words within the same oracle budget. No generic schoolbook
multiplication or division is executed for every elementary record bit.

There is NO classical A-entry directory or recursive host stack. Iterate
levels and node numbers; public heap formulas and a common power-of-two
packet stride give each node and child base using shifts/additions.
Reverse the same loops in descending order. The nesting depth of node,
bitonic(K0,J0,i), scan(lane,field), arithmetic and fixed gate-template
loops is constant. Public counters H,j and all arithmetic buffers have
O(n) bits; there are constant many such classical words. Significant
physical addresses and within-word counters have O(log n) bits. The
running-pointer and underflow-counter implementation of lean-native3
pays every actual changed bit and EVERY full global address fee. Since
the WHOLE allocation is polynomial, d=ceil(log2(Malloc+2))=O(log n).
Even O(n)-bit public boundary setup per record costs O(n d); individual
gates do not copy/add a full n-bit address. Thus WHOLE oracle work is

    O(S n(log n)^3).

The uniform source/score/selector/readout auxiliary quantum allocation
is O(n^4), as follows explicitly. Rrec/all raw sources/staging use O(n²)
qubits. Inside V there are O(n²) raw known-ADD probes; reusable ADD
scratch is cleaned between probes. Retained bounded reversible counts,
grid and unwrap history use O(n^4) bits. The fixed-degree400 score
uses O(n²) arithmetic history per record, O(n³) total. Full selection
range trials, q-position scans, copies and routing histories fit O(n^4).
Tail/core inverse arithmetic uses O(n³). All these, and the zero-phase
apparatus linear in EVERY mutable V qubit, fit O(Sn):
S can be chosen with S>=a²L, and a²Ln>=n^5/(2k+4)²>=c n^4,
using n>=4k². Constant many oracle/output/inverse regions are included.
The record bank is explicitly allocated qubits, not uncounted data.
The ENTIRE peak quantum space is therefore

    O(a²Ln)=O(n^5/(log2 n)^2).

Public pi/root/cap setup and streaming source preprocessing are executed
once, with O(n^9) a conservative work bound. Other nonmark parts of V
have polynomial work. They need not fit a per-mark budget: they are
charged separately to the complete column/exponential envelope below.
Each mark's history is literally reversed and reused; no history
accumulates over Grover iterations. All zero tests, resets, gate
emission, and failed branches pay their full fees.

Since K/mu<=4 and Kcarry=O(n), actual public-nominal j is
O(2^(t/2)L^(F/2)sqrt n). Exactly j full Grover words and their literal
inverses, followed by the constant16 trials, BEFORE multiplying by Section7's ACTUAL J,
give complete mark contribution

 O(2^(t/2+(F/2+1)r) a² n^(3/2)(log2 n)^3)
 =O(2^E a² n^(3/2)(log2 n)^3),
 E=m/2-(B-1)r/2.

Here t+ar=m and F=a-1-B. No dummy bits inflate m or amplitudes.
For completeness the exponent saving is uniform: a0>=n/(4k) gives
b0>=v-4-2log2 k. For v>=12, k<=v+1 and
log2(v+1)<=v/8+5/2 (verify at12; thereafter derivative<1/8), so
b0>=3v/4-9. Divisibility by 2^b0 forces at least b0 trailing ones
in a-1. For v>=14, B-1>=3v/4-10>0 and r>=2v, hence
 E<=n/2-3v²/4+10v+80<=n/2-v²/2+180.
For 12<=v<=14 use B>=1 to obtain the same bound. Finally a<=n/v
proves the column-work envelope BEFORE the outer J multiplier

    O(2^(n/2-(log2 n)^2/2) n^(7/2) log2 n).

The ACTUAL J=1024*2^ceil(k²/4) is O(2^(v²/4)n^(1/2)), since k<=v+1 and ceil(k²/4)<=(v+1)²/4+1. Multiply the complete column/inverse/zero-phase contribution by this J and the fixed16 trials. Thus WHOLE time is

    O(2^(n/2-(log2 n)^2/4) n^4 log2 n).

The uniform j counter has O(v²)<=O(n) classical bits; generating its fair bits and every actual iteration/failed trial is charged. No Grover word is replaced by a powered shortcut.

Once-only preprocessing is polynomial. Any polynomial nonmark V work is repeated at most O(J) times; O(J*poly(n)) also fits the final time envelope, since n/2-v²/2 dominates every fixed multiple of v=log2 n. No history or allocation accumulates over these repeated words. All separately charged fixed-degree polynomial work is smaller than this
exponential envelope, uniformly after absorbing a finite prefix. The
classical Rrec/streaming inventory of Section2A plus the constant-depth
public heap generator above gives O(n) allocated CLASSICAL bits.
EXACTLY Q=3*2^40(n+32) originals are acquired even after aborts. The
finite n<4096 fallback uses the SAME fixed banks, score and full joint
fraction(log2n)^2/(32n), with its finite outside constants. This is ONE program
with growth indices (1,0,0,0), weaker vanishing tolerance as stated, and
joint improved time/classical/quantum envelopes. It is not subexponential
time and no practical finite-size or optimality assertion is made.

## 10. Scope, credit and provenance

Growing-tree/PGM circuits and all quantified native lemmas are complete in this archive; tests/verdicts are not premises. The standard tools credited in0, comparison networks/prefix scans/schoolbook arithmetic and two-projector decomposition are not claimed invented. Related Helm–MayPQCrypto2020 subset-sum tradeoffs supply no assumedpreimage oracle. Earlier published source9fd0fa0e joint/RQ methods are rederived here, not substituted by its acceptance. The actual earlier submission documents its own local operational failures/compaction; no hosted judgment is asserted here. This changed growing-arity configuration requires its OWN fresh whole-proof review; no parent verdict is reused.

Randomized Grover-length/rotation credit: Boyer, Brassard, Høyer and Tapp, arXiv:quant-ph/9605034; amplitude amplification/estimation credit Brassard, Høyer, Mosca and Tapp, arXiv:quant-ph/0005055. The exact unknown-witness/spectral-tail/reachable-safety application is proved here, not imported as an uncosted oracle.
