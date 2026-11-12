# RPF-TAIL-SQRT-ONEPASS: growing balanced-tree measurement with a one actual decoder pass under inverse-linear full-joint noise

## 0. One algorithm, promise and joint theorem

The COMPLETE core/direct-tail/omitted-empty-hash/popcount-index/triangular uniform-cap and full-target column method is material from published PA-LQ102f6f9d-a7b8-45a3-90b5-4eb66f3c3868, particularly its entire3--5. These are NOT new inventions here; they are supplied fully with the actual retuned parameters. The physical packed layer/unequal bridge/controller/source-record method is material from published88e03dc7-0f02-4740-93bf-47d69f02213f and the accepted one-pass selector/protocol from this session's eight-list one-pass work, with its exact public IDs/statuses in note/dependencies. This NEW actual configuration chooses square-root POWER-OF-TWO core arity, total m=n+160 and a DIRECT coherently searched residual tail, then performs ONE V_R. Sections3/9 re-establish ALL growing-node/layout/address/depth costs;6--7 prove full-reference one-pass success under EXACT1/(32n). No parent verdict or old polynomial-space time formula supplies these new joint bounds.

For N>=2 write n=ceil(log2N), u=n+2, Q=3*2^40(n+32), q=Q/2, n0=2^20. ONE program below has unconditional full-secret success>=2/3 and simultaneous bounds
 T=O(n^(17/4)2^(n/2-(1/4)n^(1/2)log2n+n^(1/2)+(1/2)(log2n)^(1/2))), S_C=O(n), S_Q=O(n²(log2n)^(1/2)2^(2n^(1/2)+2(log2n)^(1/2))),
 EXACT original acquisitions Q=3*2^40(n+32)=O(n).
Time index1, quantum index1/2, classical/sample indices0. Every branch is capped, including failure/unused originals, and all bit operations, gates, addresses, generation, initialization and memory count.

The literal malformed fraction is1/(32n): an adversary fixes B, |B|<=floor(Q/(32n)), possibly depending onN,s. The joint state, with arbitrary inaccessible reference, has reduced state rho_s tensor(Q-|B|) on all other positions; bad systems may be arbitrarily entangled/correlated subject to that marginal. Mixtures over fixed B follow by linearity. No source control, preparation inverse or purification is available.

Acquire EXACTLY Q originals on EVERY branch and preprocess/split/score as1--2. If n<n0 execute8. Otherwise compute the COMPLETE growing choices in3 and execute the ONE-pass protocol6--7 with preimage word3--5 and the whole layout/fees in9. All five claims concern these SAME public choices and actual words. nextpow2, group powers and every parameter use bounded integer arithmetic, with no real-valued advice.

All constructions are supplied in this file, native.md and sqrtlog-native.md. Material source9fd0fa0e-7410-422f-a82d-67022c0c7cfc (published balanced sample program) receives credit for joint-source.md2 full-reference extraction/coupling and sources/RQ-SPLIT-proof.md3 finite eigenlabel probing. Its other engine, old output law/resource bounds and verdict are not premises. Standard credits: Bacon–Childs–vanDam2005, arXiv:quant-ph/0501044 (PGM/preimages); Marriott–Watrous2005, arXiv:cs/0506068 (binary in-place witness tests); Kitaev1995, arXiv:quant-ph/9511026 (eigenphase probes). No external native oracle is assumed.

## 1. Source and unconditional reference comparison

Let omega=e^(2pi i/N), chi_k=N^-1/2 sum_(x<N)omega^(-kx)|x>, phi_k=(|0>+omega^(ks)|1>)/sqrt2. Orthogonality gives exactly
 rho_s=(1/N)sum_k |phi_k><phi_k| tensor|chi_k><chi_k|.
Known ADD1 has eigenvalueomega^k onchi_k; extend ADDa by identity on padding x>=N. Privately uniformly translate position byj in[0,N), forgetj. The factor (1/N)sum_j omega^(j(k-l)) kills distinct valid k,l coherences, also against a reference. A bad padding/zero-mode coherence need not vanish; no separation of those modes is used. Each GOOD position has valid support globally by positivity of its marginal.

Each uniform range draw uses d=ceil(log2(2^40Q)) trials of ceil(log2range) fair bits, taking the first in range; conditional success is exactly uniform. A whole Q-draw procedure aborts with probability<=2^-40. Keep an abort flag but nevertheless acquire all Q originals. On success use the native2 nondemolition ADD eigenlabel instrument, t=n+4, reporting W modN with per-eigenstate error<=delta=2^-100n; measure probes and discard position, retaining phase qubit/W. Known translations act only on position, so every fixed probe transcript acts by a scalar onchi_k and never changesphi_k.

The exact twirl gives an analysis-only classical refinement of all good k. Their JOINT marginal is IID uniform, because the original good marginal is the stated product. Given all good k, the good phase subsystem is a PURE product; positivity forces it to factor from all bad/reference systems. The remaining state may depend onk. Define a comparison OUTPUT by replacing only GOOD reported W with its hiddenk, keeping every bad channel and reference unchanged. Couple actual/ideal outcomes using the same hidden k/probe transcripts: they differ only on a good report error. Full-reference trace distance<=Qdelta<2^-40. This is unconditional; do not condition uniform labels on successful extraction/bad reports. Later channels contract this distance. Work always refers to the physical capped instrument.

## 2. Private split and exact score soundness

After ALL Q acquisitions, uniformly Fisher-Yates permute phase/W pairs with the SAME bounded private-range primitive; abort<=2^-40. Conditional validity gives exact uniform permutation independent of input. First q records form verification bank, second q the unknown witness. Global p=|B|/Q<=1/(32n)<=1/32. In main n>=2^20, EVERY permutation gives each bank bad fraction<=2p<=1/(16n)<33/1024, deterministically. No main split concentration event is needed. In finite n<2^20 use one half's hypergeometric count X, variance<=Q/4. Absolute deviationQ/2048 has probability<=2^20/Q<1/1024; the complementary half deviation is its negative. Both bad fractions are then<=p+1/1024<=33/1024. These bounds concern ONLY fixed B/private coins, not good labels, bad reports or phase outcomes. The acquisition/permutation schedule is unchanged.

Measure verification phases in independent fair X/Y axes beta=0,pi/2, outcomesZ=+/-1. Retain(W,beta_flag,Z). Define score(a)=q^-1 sum Zcos(2pi*aW/N-beta). A good term has mean1/2 for a=s,0 otherwise: averagebeta gives(1/2)cos(2pi*(a-s)W/N), then uniformW gives character orthogonality. Good marginal terms are independent, without conditioning on bad data. Hoeffding for[-1,1] gives good-sum deviationq/16 probability<=2exp(-q/512); union over all N candidates is<2^-40. Bound every bad contribution by its count, regardless of correlations. On these events
 score(s)>=(1-33/1024)/2-1/16-33/1024=797/2048,
 score(a) for a!=s <=1/16+33/1024=97/1024.
Native2 gives an EXACT rational cosine polynomial with error<1/128 and common positive denominatorD. The Boolean marker a<N AND4sum Z*C>=qD therefore accepts EXACTLY s. It is computed with reserved clean scratch, untouched by earlier stages. Thus clean-verifier soundness holds for EVERY witness/reference state, not merely honest decoder outputs. The measured score records occupy the immutable quantumRrec bank of2A.

## 2A. Actual record bank, reference law and O(n) classical controller

Rrec is a bank of ALLOCATED QUBITS of total sizeO(Qn)=O(n²), counted inSQ. Acquire ALLQrawsystemsfirst inO(Qn)qubits. Processonecopyat a time: measured/decodedW and verification(beta,Z) pass through a reusableO(n)-bit classicalrow, are written by classicallycontrolledX into a basisrow ofRrec, then the classicalrow is erased/reset at chargedcost. No classicaltranscript table remains. If the full measuredrecord/reference law is sum_r |r><r|_C tensor sigma_r, this write/erase channel produces EXACTLYsum_r |r><r|_Rrec tensor sigma_r. Thus allreferencecouplings in1 contract through it. Only measured basisinformation is copied; the unknownphase/reference state sigma_r is untouched.

OutsideV sourceprobe stages run t,t-1,..0, keeping currentcos/sin tallies, current six-bit gridangle and the currentO(n)-bitdyadic unwrapvalue. Native2's backwardsunwrap then discards completedtallies. PublicADD^(2^j)coefficients are regenerated by iterative doubling of1modN asneeded, not stored as a growingtable. Good conditionalchi_k probes act by scalars, so order doesnot change their independentoutcome/error proof; badsourcechannels remain arbitrary. Extra coefficientregeneration is polynomial insideO(n^9). Firstvalid capped range draws store only currentdraw/firstvalidvalue/flag/trialcounter; everyrawdraw is discarded/reset. Private Fisher–Yates usesCLASSICALrowindices and literalSWAPgates onphase/fullquantumlabelrows, so its uniformconditionalpermutation andabortlaws are unchanged withoutquantumaddresslookup. Allthese operations/resets/feescount.

After split/verificationRrec is immutable and CQdiagonal, with arbitrary conditionalD/reference states. V_R copies its witnesslabels byCNOT atPUBLICrowindices into quantumWwork; routing stillFULLSCANSq positions. The score's W/beta/Z are read-only Booleanquantumcontrols for the generic bounded arithmetic innative1-2. Eachrecordsector has the same clean mathematicaldecoder and exactunique-scorepredicate; the score arithmetic is separately charged polynomial work; the actual linear layer-copy functions are specified in sqrtlog-native. No hostbranch depends on quantumrecordbits. Rrec never changes. On each realizedr,V_R is a blockV_r; the initialCQmixture and blockdiagonal gates give exactlythe conditional analyses3-7. The literalinverse is the NEWactualV_Rdag, not an asserted equality ofdirtyextensions to older compiledwords.

In EACH realized immutable-record sector r, the ACTUAL single V_R computes the known decoder and exact score flag from clean helpers. On the score-uniqueness event, acceptance outputs exactly s for EVERY unknown witness/reference state. Its main performs only ONE flag measurement after V_R, then output/disposal; there is no failure/reflection/reset cycle. The complete CQ/reference source comparison and raw-coin orthogonality apply to this word. In finite fallback, Grover search is over known freshly prepared candidate registers with the SAME record-controlled score; it never resets or reflects about unknown D. All helper, source, output and disposal costs count.

Classicalmemory inventory: publicN/n/Q/q/m/r/L/caps/H/j/J andinput/output; percopyrange/probe/unwrap/verificationrows; arithmeticoperand/result/remainder/accumulator buffers; and generatorloop/base/stride fields. There is a CONSTANTnumber ofO(n)-bitwords. Inplace schoolbookmultiplication uses fixed-widthoperand/resultaccumulation, restoringdivision usesquotient/remainder, and greedyroot usescandidate/trialsquare, eachO(n)space. PublicMachin terms haveO(n)-bitindividualdenominators and fixed-pointaccumulators(native2); no growingdenominator product or savedclassicalhistory is used. Degree400 and64gridpoints are FIXEDcounts. Allsource/probe histories insideV are QUANTUMancillas includedinSQ.

The ACTUAL emitter uses public group/level/node loops and closed heap/stride/hash-plane formulas, without a G-entry directory or full pointer frame per level. Nonroot packets share a Pcap-based stride; ROOT has its own larger stride for Pcap+K. AllG-2 histories/root/raw/stage arrays and all H_ck*B_ck sort-pool arrays including unused slots count. The caller retains only constantmany O(n)-bit fields; sort reconstruction uses an O(logn)-bit packed path. Sections3/9 and sqrtlog-native prove actual D_sort<=6n, used sort height<=sqrt(log2n)/2+2 and full global fee O(sqrt n). This gives SC=O(n) and the jointly stated gate/work/space bounds; it is not the fixed-eight inventory with G hidden as a constant.

## 3. Selected complete PA-LQ core/tail/cap method with square-root arity

For main n>=n0=2^20, m=n+160. Compute D_grp=floor(floor(log2n)/2), a=2^D_grp, A_tree=a, G=a, r=floor(m/a), m_c=a*r, t=m-m_c, L=2^r. These are bounded integer bit-length/shift/division choices. First m_c REAL phase bits form a consecutive r-bit core groups; the last t REAL bits are the directly searched tail. The complete padded-tree schema below uses A_tree=nextpow2(a); in THIS configuration A_tree=a, hence zero additional leaves, but every actual core/raw/node/target/history/flag region is counted. A zero-bit leaf in this schema has EXACTLY ONE present (0,emptyID) record, never an extra source bit or a phantom representation. Put Ccap=nextpow2(8a)=8a, Pcap=2^160*Ccap*L, K=2^162, Kcarry=nextpow2(m_c+1), F=a-D_grp-1. ALL nonroot caps are Pcap and root capK; any overflow rejects WHOLEquery. The entire complete PA-LQ direct-tail/cap/index method is supplied below; only the ACTUAL arity parameters and outer one-pass protocol/physical ledger are retuned. Section9 proves all guards for this configuration.

At publiclevelj=1..D_grp-1 therearev_j=ceil(a/2^j) nonemptyreal-bit subtrees, the FIRSTv_j nodes. Choosev_j-1 FREEr-bit hashes there; derive the LASTNONEMPTYhash as(T_(j-1)-sumfreeh)modL. Everytrailing empty-onlynodehash is FORCED0, never a searchfield. StartT0=y_c+carry*N withy_c=(y-f_tail(u))modN andf_tail(u)=sum_tail W_i u_i modN. UpdateT_j=(T_(j-1)-sumNONEMPTYh)/L, exactsignedinteger. Eachactualpairjoin uses(qleft+qright)modL=h, outputquotient(qleft+qright-h)/L, unreducedrawsums andfullrealbitIDs. Unarynodes withoneemptychild are REALboundedjoins; theirhash isnotforced0 unlessBOTHchildrenempty. Empty-onlynodesproduceonly(0,emptyID) atforcedhash0. RootmatchesEXACTintegerqleft+qright=T_(D_grp-1),sortscoreIDs canonicallyandFULLSCANSallKrank slots. Allcounts/flags/targets/histories are retained and literallyreversed bynative3.

The number ofsearchedfreehashes is
 F=sum_(j=1)^(D_grp-1)(ceil(a/2^j)-1)=a-1-b_pop, b_pop=popcount(a-1).
Indeedceil(a/2^j)=floor((a-1)/2^j)+1 andsum_(j>=1)floor((a-1)/2^j)=a-1-popcount(a-1), withtermsj>=Dzero. SearchX comprisesDIRECTt-bit tailu, theseFr-bitfields, corecarryin[0,Kcarry), androotrankin[0,K), soH=2^t*L^F*Kcarry*K. Rejectcarry>m_c. The trailing-emptyhashes are NOTfreefieldsthatcostextraGroverdomain. Realcoreinputlengthism_c=ar, NOTAr; zero-bitgroups neverincreaseM0.

EachsurvivingFULLb=(bcore,u) hasf_W(b)=y modN andaUNIQUEindex: actualtailu, corecarry(sumcore-y_c)/N, each FREEactualsubtreehash,canonicalcorerootrank. Derivedlastnonemptyhashes/forcedzerohashes are determined bytheseconstraints andtotalcoretarget. Coincidentsumsretain distinctrealbitIDs. InverseF_Wy(b)extractstailu, recomputestailtarget/corecarry/everycorehash, runsSAMEcappedcompleteA_tree-leaftreeincludingzero-bitgroups, andFULLSCANSthe rootforbcore/rank; absent/invalid0. A nonheavyFULLcolumnc_y<=K implies everyfixedtail/hashrootcount<=K. No core-onlydensity or independent-targetpromise is assumed.

Compute g(X), copyFULLb=(corepayload,u) andSINGLEtagNOTvalid, reverseALLg/tailtargetwork withX unchanged, THENcomputeF(B),XORitsENTIREindexincludingtailu intoX,andreverseFtempswithBunchanged. Thusmarkedbranchescleareveryhash/carry/rank/tailhelper. Everymarkedfullbitstring occurs once acrossalltailvalues, withcommonphaseomega^(s*y). Forcedemptyrawrecordsarenotphantomsourcebits; theirpresence1mattersforunaryjoins.

We prove a sharper UNIFORMbucket bound, essential to the polynomial physical cap. Fix an actual fullb and average over IID uniformW. A_tree nonroot level-j node ofthecompleteA_tree-leafpaddedtree contains h=2^(j-1) disjoint raw-group childpairs; some arezero-bitgroups. Alternates CANNOTchangeemptygroups, so allowedactivitysets form a SUBSETofthecomplete tree used below. The sameupperbounds thereforeapply, includingunarynodes. For an alternate assignment let S be its e changed childpairs; each has at mostL² alternatives. Define D_i as the UNREDUCEDalternate-minus-actual sum in that pair. Equality of all actual subtree hashes means eachD_i=0modL, each binary-pair sum=0modL², each four-pair sum=0modL³, up to node sum=0modL^j. No target/hash independence is assumed: these are exact DIFFERENCE constraints.

For each changed pair choose one original labelX_i with coefficient sigma_i=+/-1 inD_i. Condition all other labels; distinctX_i remain independent uniform[0,N). At every nonempty constraint-tree node pivot on its LEFTMOST active leaf. Nodes with pivoti form a consecutive chain of lengtht_i<=j; sum_i t_i=w(S), the number of nonempty constraint nodes. CountX_i RIGHTTOLEFT: the largest chain node imposes ONE affine congruence sigma_iX_i+c=0modL^t_i. Every lower chain constraint follows because removed siblings are empty or already satisfy their lower modulus constraints. Nodes pivoted to the right do not involveX_i. Thus the number of satisfying label choices is at most product_i ceil(N/L^t_i), with inconsistency reducing it. This is an explicit triangular affine elimination even for odd/compositeN.

Section9 proves N>=2hL^j. Putx=L^j/N, soex<=hx<=1/2. The ceiling product divided byN^e is at most L^-w(S)*(1+x)^e <=2L^-w(S): binomial coefficients are at moste^k, so(1+x)^e<=sum_(k>=0)(ex)^k<=2. The ceiling overhead is a SINGLEfactor2, not2^e. This stronger finite-precision estimate is why the old exponentially large bucket coefficient is unnecessary in THISnew physical configuration.

Define T_j=sum_(S INCLUDINGempty) L^(2|S|-w(S)) for the complete constraint tree ofheightj, h=2^(j-1) leaves. ExactlyT1=1+L and
 T_j=1+(T_(j-1)^2-1)/L.
Indeed the two independent child activity sets combine, and every nonempty combined set adds one root constraint. WithqL=1+1/L, induction yields T_j/L<=qL^(2^j-1): square the preceding bound and absorb the remaining1/L term into the extraqL, since its preceding power is>=1. Section9 givesL>=4h; hence(2h-1)/L<=1/2 and the same binomial/geometric argument givesqL^(2h-1)<=2. ThereforeT_j<=2L. Summing alternate assignments now bounds the expected uncapped actual bucket by
 1+2(T_j-1)<=4L,
UNIFORMLY over all growing levels. Child caps only remove entries. A_tree fixedb is lost at a nonroot node only if its uncapped actual bucket exceedsPcap; sum Markov over ALLA_tree-2<2a nonrootINTERNALnodes gives expected lost INPUTmass<=8aL/Pcap<=2^-160. Rawleavesarenotcapped; forcedempty-onlynodes haveonepresentzerorecordandcannotoverflow. No n-dependent factor is absorbed into a constant.

Put M0=2^m andmu=M0/N using ALLcore-and-tailbits. Then2^160<=mu<2^161. For distinct fullsubsets their moduloNcollision probability is1/N by a +/-1 label coefficient. Thus V(W)=(1/N)sum_y(c_y/mu-1)^2 hasEV<1/mu. On heavyc_y>K, v=K/mu-1>=1 and weighted INPUTmass is bounded byV(W)(v^-2+v^-1), with mean<=2/(mu*v)<=4/K=2^-160. Exclude heavy FULLcolumns ONLYinanalysis. On all other columns no fixed-tail root exceedsK. Setcprime to physical surviving count there and analysis0 on heavy columns; then ell=1-sum cprime/M0 obeysEell<=2^-159. The actual heavy-column unitary remains finite and capped. All averages are unconditional IIDgood-label averages, not labels conditioned on bad reports, uniform independent targets, or surviving hash queries.


## 4. Actual public-nominal-count positive preimage column

Put M0=2^m, mu=M0/N. These are PUBLIC rationals/integers, independent of W,y,s. Main-range m=n+160 gives2^160<=mu<2^161. Let cprime_y be the physical surviving marked count for nonheavy targets c_y<=K. In analysis only set cprime_y=0 on heavy columns, as in3; those entire columns are charged as lost input. The physical oracle/unitary always keeps its public caps and may behave arbitrarily on heavy inputs. No global quantumcount estimator, countcopy or countuncompute is executed. Exact bucket counts inside the bounded join remain ordinary explicit Boolean words.

Generate finitepi P_pi/D_pi as native2 with precision b=2log2H+40. Compute PUBLIC
 j=floor-sqrt(floor(P_pi²*H*N/(16D_pi²*M0))).
Its distance from(pi/4)sqrt(H/mu) is<2: finitepi scaling contributes<1/16, and floor-sqrt of a floored nonnegative rational equals floor of its real square root. All integers haveO(n)bits, and j generation/storage/full fees are counted. The ACTUAL loop executes EXACTLY these j iterations, not an old sqrtH loop with inactive controls. j=O(sqrt(H/mu)); both it and its inverse loop are fixed by the public input.

Start X uniformly on its power-of-two H domain and apply exact
 G=(2|u_H><u_H|-I)(I-2P_mark)
exactly j times. Every G genuinely invokes the bounded mark word; no fastpower is assumed. Native uses the positive diffusion scalar exactly. A_tree fixed|1> helper supplies any minus compensation, then is cleared; no y-dependent phase is dropped. For physical count c, its two-dimensional angle is theta=asin(sqrt(c/H)) and marked amplitude sin((2j+1)theta). c0 has no marked component.

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


## 6. Actual one-pass selector and unconditional decoder completeness

The ACTUAL source tolerance is epsilon(n)=1/(32n). In the main range,
ANY private permutation gives witness-bank bad fraction at most
|B|/q<=2epsilon(n)=1/(16n), deterministically; no favorable split is needed.
Main m<=2n. A uniform ordered m-subset without replacement has expected
number of malformed positions<=m/(16n)<=1/8. By the union/Markov bound,
the probability it is ALLGOOD is at least7/8. This statement concerns only
the fixed bad set and private selector coins, never bad reports or labels.

The ACTUAL coherent Fisher-Yates selector changes its per-range trial cap
to d_sel=ceil(log2(16m)), retaining ALL fair raw coin words. Each bounded
range draw has per-trial acceptance>=1/2. The probability any of the m draws
fails is at most m*2^-d_sel<=1/16, so selector validity>=15/16. Conditional
validity gives EXACT uniform ordered subsets: each draw is uniformly
accepted from its actual remaining public range, independently of quantum
data; bounded failure has no label-dependent postselection. The validity
and all-good statement together give weight at least(15/16)(7/8)=105/128.

Copy selected immutable Rrec labels and route their phases by full q-slot
scans. The decoder is EXACTLY the capped known word of3--5 and native3,
including its public-nominal Grover loop and known-ADD readout. For an
all-good selected subset, its phase input conditioned on those hidden labels
is the pure product from1 and factors from all other systems/reference.
Ignoring score and all bad reports, the UNCONDITIONAL selected good-label
marginal is IID uniform. The complete full-reference/channel/column proof
in5 consequently gives mean entire-secret decoder failure<2^-20.
This uses only selection of GOOD POSITIONS, independent of labels/phase
outcomes, not conditioning on score, a bad report or decoder success.

No Markov event or witness-reflection amplification is required. The directly searched tail u/free hashes/rank are COHERENT parts of the known preimage column, with their cleanup/common-phase proof in3--4; they are not classical mixture coins. The raw
selector/probe coins remain orthogonal through acceptance; tracing them
makes the physical output law a positive average over the exact subsets,
so the valid-all-good lower bound applies to the ACTUAL coherent word.
Do not infer independence between score and decoder labels. Instead, first
ignore score and bound true decoder output by
 (105/128)(1-2^-20),
then subtract the UNCONDITIONAL score-failure and full-source-label
comparison errors by a union bound. This is valid with arbitrary allowed
reference correlations and fixed-set mixtures.

## 7. Actual main program, one binary test and full safety

The ACTUAL main executes ONE V_R: coherent bounded selector/routing,
preimage-PGM/known-ADD decoder, and reserved clean exact record-controlled
score marker. Accept flag C is selector-valid AND PGM-zero AND
candidate<N AND score. All inputs/helpers are the actual clean allocated
regions, and every internal operation is a known bounded Clifford+T word.
There are NO intermediate measurements. Measure ONLY C, output its
candidate on acceptance; on rejection output0 and dispose input/work at
full cost. There is no second V, witness reset or outer reflection loop.
Inner public-nominal Grover iterations inside the known preimage column
are still executed and fully charged; no inner oracle/power is free.

On the score-uniqueness event, C can accept ONLY the entire s for EVERY
witness/reference input, since its exact marker uses immutable Rrec and
reserved clean scratch. This is a clean-input ONE-pass assertion; no
unsupported globally dirty soundness is needed after an earlier failure.
The actual literal inverse exists for all finite known words but is not
used to reset or reflect about the unknown witness. Output/disposal and
failed selector/decoder branches remain bounded and charged.

Union source-label comparison, two bounded private-range aborts, score
failure and the all-good decoder error with Section6. With the conservative
source comparison<=2^-20, the total main success is at least
 105/128 -2^-20-2^-20-2^-39-2^-40 >4/5>2/3.
All bounds are unconditional. Fixed B may depend on N,s before coins;
the full joint good marginal and arbitrary allowed entanglement/reference
promise of0/1 are used throughout, not independent per-copy corruption.
Section8 supplies correctness for every smaller input with the SAME
source acquisitions/error promise and exact immutable score marker.

## 8. Finite fallback, same acquisitions/noise

For n<n0 use the SAMEQ/split/score; discard unused witnesses with full charge. On its events the score marker has exactly one solution inH0=2^n. Do16 independent trials: uniform classicalj in[0,J), J=2^(ceil(n/2)+2); initialize a fresh uniform candidate register, perform j exactGrover words for the marker, measurethecandidate and check it bythe coherentrecord-controlledmarker as2A, returningfirstpassing. No new source copy is acquired.

For theta=asin(1/sqrtH0), mean trialsuccess is
 (1/J)sum_j sin²((2j+1)theta)=1/2-sin(4Jtheta)/(4Jsin2theta)>=1/2-1/(16sqrt2)>2/5,
usingJ>=4sqrtH0, sin2theta>=sqrt(2/H0). Failure<=(3/5)^16<1/1024, independently across fresh trial coins/search initializations on fixed score data. Same source/split/score union gives success>=2/3. WorkO(2^(n/2)poly(n)), spacepolynomial, exactQ. The finite setn<n0 has a finite maximum ratio to the declared envelopes, absorbed into an outside constant independent ofN,s,outcomes. No faster exponential rate is asserted on that finite prefix.

## 9. Whole growing-tree native inventory and charged resources

The ACTUAL main parameters are EXACTLY3: m=n+160, a=2^floor(floorlog2n/2), G=A_tree=a, k_grp=D_grp=log2a, r=floor(m/a), m_c=ar, t=m-m_c, F=a-D_grp-1, L=2^r, Pcap=2^163aL, K=2^162, Kcarry=nextpow2(m_c+1), H=2^t L^F Kcarry K; all G=a=2^k_grp raw lists,
G-2 nonroot joins, root join, normalized targets and quotient/ID histories
are counted. There is no fixed-arity constant in this inventory.
S=O(G²L)<=O(nL) whole base rows counts raw/original/sorted/prefix/boundary/
marker/query/root/canonical/input/output/inverse and per-node stage data.
Every padded pool and unused slot is included. Source/Rrec/staging,
selector/probe/score/routing/arithmetic and target/hash auxiliaries are
separately polynomial, O(n^4) qubits, and fit since L>=n^6.

The known bounded oracle is emitted with PUBLIC level/node loops, not an
n-bit pointer stack or G-entry classical directory. Raw group g uses one
fixed raw stride. Nonroot node (ell,j) has sequential ID
 (G-G/2^(ell-1))+j; at ell1 its children are raw2j,2j+1, and thereafter
children are previous-level IDs (G-G/2^(ell-2))+2j and the next ID.
Root uses the final two nonroot IDs. All nonroot blocks have one public
power-of-two stride for constantmany Pcap-based stage/pool arrays; root
has a SEPARATE public stride for Pcap+K. Thus total allocation is O(GPcap+K),
not G copies of the larger root packet. Compute bases from PUBLIC IDs
and strides in constantmany O(n)-bit current registers, paying all arithmetic.
All targets T_ell are QUANTUM O(n)-bit fields (k_grp of them); all free/
derived hashes, quotient histories, subset IDs and helper fields are
allocated quantum data, not a free classical transcript. Their polynomial
cost is included. The ENTIRE X starts with its t-bit tail prefix: hash-plane_base=base_X+t; carry starts at base_X+t+Fr and rank follows the public carry field. RELATIVE hash-plane offsets use
 [G-G/2^(ell-1)-(ell-1)]*r bits, with fixed public fields; no quantum value
chooses a classical address. Reverse level/node/word order for literal
uncomputation. No full circuit, recursion history or frame directory is stored.

Public N/n/Q/q/G/D_grp/m/m_c/t/r/L/caps/F/H/nominalj/input/output,
source/probe/range/unwrap rows, current stride/base/level/node fields and
bounded in-place arithmetic use CONSTANTMANY O(n)-bit classical buffers.
Nested loop indices are only a fixed number of public counters; tree levels
are iterated, not stored as full pointer frames. The sort controller below
uses a packed phase path. Consequently the ENTIRE classical inventory is
O(n), despite growing G. Persistent measured records remain allocated qubits.

For each actual sort, D_sort=k_sort(k_sort+1)/2<=6n by3. The ACTUAL read-only
layer XOR and unequal prefix/last/uncompute bridge in sqrtlog-native use
r_ck=ceil(sqrt(ceil(log2n))), H_ck=r_ck, B_ck=2^(2r_ck).
There is NO layer padding to B_ck^h. The ACTUAL bridge stops at d=1 rather than filling reserved depth.
Its used height h<=ceil(log_(B_ck)D_sort)
<=(log2n+log2 6)/(2r_ck)+1<=sqrt(log2n)/2+2, since r_ck>=sqrt(log2n).
Thus actual base calls<=2^h D_sort<=24n*2^(sqrt(log2n)/2).
Reserved height remains r_ck, and ALL unused slots are physically counted. Reserve EVERY H_ck*B_ck array per packet, including
unused slots. Its packed phase digits occupy O(logn) bits, and root
reconstruction uses constantmany O(n)-bit current fields. It stores NO full
O(n)-bit frame per level. All comparisons/copies/prefix scans and changed
pointer bits pay full global fees as below. Literal inverse reverses ALL
gates/scalars; all lower pools clear for clean inputs, including arbitrary
initial final output XOR; dirty extensions still have exact inverses.

Entire quantum allocation is
 O(S n H_ck B_ck+n^4)=O(L n² r_ck 2^(2r_ck)).
Since r<=2sqrt n+1 and r_ck<=sqrt(log2n)+2,
 SQ=O(n²(log2n)^(1/2)2^(2n^(1/2)+2(log2n)^(1/2))).
This counts ALL growing nodes and reflection/zero/phase apparatus actually
executed in the preimage/PGM/score words. The unknown witness has no outer
reflection apparatus/rotation schedule; the actual main performs ONE V_R.

Importantly, the ENTIRE allocation gives full global address fee
 d_addr=ceil(log2(M_alloc+2))=O(r+logn+sqrt(logn))=O(sqrt n).
Classical O(n) bits and polynomial source auxiliaries do not enlarge this
order. No fee is changed or omitted: this is the actual same FULL fee
computed from the stated whole allocation. Each layer-XOR word uses O(Mn)
gates and O(n) reusable helpers. Aligned public record/field strides,
running pointers and minimal underflow counters give O(n) total changed
pointer/setup bits per record word; EVERY such bit and EVERY gate address
pays d_addr. Thus whole oracle gates O(Sn²2^(sqrt(log2n)/2))<=O(Ln3 2^(sqrt(log2n)/2)),
and record/native full work O(Sn^(5/2)2^(sqrt(log2n)/2))<=O(Ln^(7/2)2^(sqrt(log2n)/2)).
There is no n-bit copy/multiplication per gate or uncharged layer decoder.

Conservatively charge metadata/reconstruction/descriptor recovery O(n4)
TOTAL per base/call, separately from per-record generation. There are
O(G n*2^(sqrt(log2n)/2)) such calls over ALL joins, giving O(n^(11/2)2^(sqrt(log2n)/2)),
within L n^(7/2)2^(sqrt(log2n)/2) since L>=n^6. Public heap/hash/target offset and
parameter setup fit this budget. Schoolbook/restoring-division work uses
constantmany O(n)-bit buffers, not growing denominator products/history.
All initialization/zero/disposal of reserved unused slots costs at most
 O(S n d_addr r_ck B_ck)<=O(L n^(5/2)r_ck 2^(2r_ck)).
For r_ck>=5, the integer inequality
2r_ck+ceil(log2r_ck)<=(r_ck-1)² follows from r_ck=5 and induction
(right-hand increments>=9, left-hand increments<=3). By the actual ceilings,
log2n>(r_ck-1)²; hence r_ck*B_ck<n. ALL initialization/disposal is therefore
O(Ln^(7/2)), inside the stated oracle budget. Source/selector/probe/score/
readout/public-pi/root conservative O(n^9) work also fits because L>=n^6.
Raw-list generation has O(G L r n)=O(Ln²) gates (Gr=m<=2n), fitting too.

The ACTUAL public nominal j=O(2^(t/2)L^(F/2)sqrt n), because H=2^t L^F Kcarry K, Kcarry=O(n), and K/mu is in(2,4]. The DIRECT tail is coherently part of X and global diffusion; it is NOT separately measured or classically enumerated. One whole column/V_R therefore costs O(2^(t/2)L^(1+F/2)n4*2^(sqrt(log2n)/2)). Main performs ONE V_R, with every inner known Grover word fully charged.

Its exact exponential factor obeys
 t/2+(1+F/2)r =m/2-(D_grp-1)r/2
 <=n/2-(1/4)sqrt n log2n+sqrt n+(1/4)log2n+79.
Indeed D_grp>=log2n/2-1, r>=sqrt n-1, m=n+160, and the lower product coefficient is positive in the main range. The +(1/4)log2n term contributes only n^(1/4), giving the exact joint time envelope
 T=O(n^(17/4)2^(n/2-(1/4)n^(1/2)log2n+n^(1/2)+(1/2)(log2n)^(1/2))).
There is no rounded-up m-n term proportional to G.

All failed/aborted/inactive/padded operations, complete addresses/generation,
source acquisitions and output/disposal are included on EVERY branch.

The actual selector cap ceil(log2(16m)), ONE-pass proof6--7 and SAME exact
score marker give unconditional whole-secret success>=2/3 for EVERY N,s
under full fixed-joint epsilon(n)=1/(32n). EXACT Q=3*2^40(n+32) is acquired
on EVERY branch, including discard/abort/finite fallback. Main n>=2^20 uses
this growing tree; the remaining FINITE range uses8 with an absolute maximum
resource ratio, not a practical or faster-rate claim there. Indices are
1(time),0(classical),1/2(quantum),0(samples). Compared with polynomial-space
adaptive rows this trades faster lower-order time for more quantum memory;
compared with fixed arity it trades slower leading time for lower quantum
space index. No all-resource dominance, optimality or cube-root goal is claimed.

### Actual square-root core guards and direct-tail data

For every n>=2^20, sqrt n/2<a<=sqrt n, m=n+160<=2n, a>=1024, D_grp>=10. We have a<=r, sqrt n-1<=r<2sqrt n+1 and0<=t<r. Thus L>=n^6 (sqrt n-1>=6log2n at2^20, with increasing difference), K<=L, and F=a-D_grp-1>=a/2, so Fr/2>=a²/4>=2^18>192, as used in4. The main cap guards are N>=4a L^(D_grp-1), hence N>=2hL^j for EVERY nonroot levelj and h=2^(j-1), and L>=a>=4h. They follow from (D_grp-1)r+2+D_grp<=sqrt n log2n+log2n+2<=n-1: divide by n, check2^20 and use decreasing ratios thereafter. All counts concern the ACTUAL full m-bit input, not just core m_c; total mu has2^160<=mu<2^161 and rootK2^162 bounds FULL-column heaviness, including ALL tail values.

For nonroot/root join packets maxcap is Pcap since K<=L<Pcap. The standard at-mostfive expansions yield k_sort<=log2(Pcap)+16=r+D_grp+179<=3sqrt n, so D_sort<=6n. The last inequality follows because r<2sqrt n+1 and (log2n/2+180)/sqrt n<1 from2^20 onward. ALL target/carry/hash/quotient/presence/default fields are bounded quantum data; no signed value chooses a host address.

Each node exposes ONLY its current normalized integer, ID and presence; constantmany query/tag/sum helper fields have O(n) bits. Prior input/quotient/scan histories remain in SEPARATE allocated node blocks, not recursively copied into parent record payloads. Core IDs have m_c bits; full output appends the t tail bits exactly once. The tail target f_tail(u) and modular y_c use fixed-wire controlled additions at PUBLIC tail-label positions, with full arithmetic/cleanup fees, not a quantum-selected lookup. InverseF extracts u, rebuilds the SAME target/tree and rank, and XORs the ENTIRE X including its u prefix before reversing temporaries. Every marked full b is unique and has common phase omega^(s*y), as3 proves.

## 10. Scope, credit and provenance

Growing-tree/PGM circuits and all quantified native lemmas are complete in this archive; tests/verdicts are not premises. The standard tools credited in0, comparison networks/prefix scans/schoolbook arithmetic and two-projector decomposition are not claimed invented. Related Helm–MayPQCrypto2020 subset-sum tradeoffs supply no assumedpreimage oracle. Earlier published source9fd0fa0e joint/RQ methods are rederived here, not substituted by its acceptance. The actual earlier submission documents its own local operational failures/compaction; no hosted judgment is asserted here. This changed record-bank/controller configuration requires its OWN fresh whole-proof review; no parent verdict is reused.

Randomized Grover-length/rotation credit: Boyer, Brassard, Høyer and Tapp, arXiv:quant-ph/9605034; amplitude amplification/estimation credit Brassard, Høyer, Mosca and Tapp, arXiv:quant-ph/0005055. The actual one-pass success is proved in6--7 and randomized finite-prefix Grover law in8; no external oracle is assumed.
