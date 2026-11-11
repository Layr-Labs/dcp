# RPF-G: growing-arity nominal preimages with linear original acquisitions

## 0. One program, supported fractional model and joint bounds

Material sources are the complete nominal/constant-accuracy RPF engine and its bounded multi-list precursors. Exact platform IDs, full-file hashes and publication/history are documented in the public note/dependency declaration; no source verdict or finite diagnostic is a premise. Every source/coupling/score/column/PGM/reflection/native method used is supplied here. NEW: the arity grows with public n, its full capacity growth is proved/charged uniformly, and the weaker supported fraction gives a constant all-good selection weight.

For N>=2 let n=ceil(log2N), Q=3*2^40(n+32), q=Q/2,n0=4096. ONE program has unconditional ENTIRE-secret success>=2/3, and on EVERY branch
 T=O(2^(n/2-(1/4)sqrt(n)log2(n)+(7/5)sqrt(n))*n^(15/2)),
 S_C=O(n²), S_Q=O(2^((11/5)sqrt(n))*n^5),
 EXACTQ=3*2^40(n+32)=O(n).
Their growth indices are1,0,1/2,0. The time guarantee is NOT subexponential time. Constants and all full addresses/generation/initialization/failed work count. No optimality or all-coordinate dominance is claimed.

The literal fraction isepsilon(n)=1/(32n). Before private coins, an adversary fixes B with |B|<=floor(Q/(32n)), possibly depending onN,s. The complete joint source/reference state is arbitrary subject to the reduced state on all other original positions being EXACTLYrho_s tensor(Q-|B|). Bad systems may be entangled/correlated with good ones and arbitrary inaccessible reference subject to that promise. Fixed-set mixtures follow by linearity. No source control, preparation inverse or purification is supplied. This is an explicit fractional guarantee, not a per-copy probability or a count claim converted through an upper sample bound.

Acquire EXACTLYQ on every branch, preprocess1 and score the firstq records2; retain lastq phases asD. There is NO global position permutation. If n<n0 use8. Otherwise m=n+160,d=floor(floor(log2n)/2),a=2^d,r=ceil(m/a),L=2^r. Divide the m REAL bits intoa consecutive groups of floor(m/a) orceil(m/a) bits, summing exactlym. Set A_d=sum_(j=1)^(d-1)(a/2^j)*3^(2^(j-1)), C_d=nextpow2(A_d), Pcap=2^160*C_d*L,K=2^162,Kcarry=nextpow2(m+1),F=a-d-1,H=L^F*Kcarry*K. These are public exact integers. Run6-7 with the actual bounded column3-5 and constantJ=1024. All five claims belong to these SAME choices.

Published-source/primary credits: earlier balanced source supplies the full-reference hidden-label channel/coupling and finite eigenlabel probes, re-established in1/native2. PGM/preimage background: Bacon-Childs-vanDam, arXiv:quant-ph/0501044; eigenphase probes: Kitaev, quant-ph/9511026; in-place witness tests: Marriott-Watrous, cs/0506068; randomized lengths/amplification: Boyer-Brassard-Hoyer-Tapp, quant-ph/9605034, and Brassard-Hoyer-Mosca-Tapp, quant-ph/0005055. Generalized-birthday filtering background: Wagner, CRYPTO2002, with Camion-Patarin precedence noted on the author's page https://people.eecs.berkeley.edu/~daw/papers/genbday.html . Hierarchical filtering is not claimed invented here. No outside native oracle or prior asymptotic cost theorem is assumed.

## 1. Source and unconditional reference comparison

Let omega=e^(2pi i/N), chi_k=N^-1/2 sum_(x<N)omega^(-kx)|x>, phi_k=(|0>+omega^(ks)|1>)/sqrt2. Orthogonality gives exactly
 rho_s=(1/N)sum_k |phi_k><phi_k| tensor|chi_k><chi_k|.
Known ADD1 has eigenvalueomega^k onchi_k; extend ADDa by identity on padding x>=N. Privately uniformly translate position byj in[0,N), forgetj. The factor (1/N)sum_j omega^(j(k-l)) kills distinct valid k,l coherences, also against a reference. A bad padding/zero-mode coherence need not vanish; no separation of those modes is used. Each GOOD position has valid support globally by positivity of its marginal.

Each uniform range draw uses d=ceil(log2(2^40Q)) trials of ceil(log2range) fair bits, taking the first in range; conditional success is exactly uniform. A whole Q-draw procedure aborts with probability<=2^-40. Keep an abort flag but nevertheless acquire all Q originals. On success use the native2 nondemolition ADD eigenlabel instrument, t=n+4, reporting W modN with per-eigenstate error<=delta=2^-100n; measure probes and discard position, retaining phase qubit/W. Known translations act only on position, so every fixed probe transcript acts by a scalar onchi_k and never changesphi_k.

The exact twirl gives an analysis-only classical refinement of all good k. Their JOINT marginal is IID uniform, because the original good marginal is the stated product. Given all good k, the good phase subsystem is a PURE product; positivity forces it to factor from all bad/reference systems. The remaining state may depend onk. Define a comparison OUTPUT by replacing only GOOD reported W with its hiddenk, keeping every bad channel and reference unchanged. Couple actual/ideal outcomes using the same hidden k/probe transcripts: they differ only on a good report error. Full-reference trace distance<=Qdelta<2^-40. This is unconditional; do not condition uniform labels on successful extraction/bad reports. Later channels contract this distance. Work always refers to the physical capped instrument.

## 2. Fixed verification bank and exact score soundness

After all Q acquisitions, use the FIRST q phase/W records for verification and the LAST q for the unknown witness bankD. There is NO global source-position permutation. If the fixed malformed set has b<=floor(Q/(32n)) positions, either bank has bad fraction at most b/q<=1/(16n)<=1/16, deterministically. This does not infer independence of bad reports or condition good labels on them. Mixtures of fixed sets follow by linearity.

Measure verification phases in independent fair X/Y axes beta=0,pi/2, outcomes Z=+/-1; retain(W,beta_flag,Z). Define score(a)=q^-1 sum Z*cos(2pi*aW/N-beta). A good term has mean1/2 for a=s and0 otherwise: averaging the axes gives(1/2)cos(2pi*(a-s)W/N), then uniform goodW gives character orthogonality. The joint good marginal supplies independent good terms UNCONDITIONALLY, even though bad outputs can be correlated with them. Hoeffding for[-1,1] bounds a good-sum deviation q/16 by2exp(-q/512); union over all N candidates is<2^-40. Bound every bad contribution by its count, without conditioning on bad data. Thus, for every n>=1 including the finite fallback,
 score(s)>=(1-1/16)/2-1/16-1/16=11/32,
 score(a), a!=s, <=1/16+1/16=1/8.
Native2's exact common-denominator rational cosine polynomial has uniform error<1/128. The Boolean marker a<N AND4sum Z*C>=qD therefore accepts EXACTLYs, since11/32-1/128>1/4>1/8+1/128. It uses reserved clean scratch untouched by earlier stages. Hence clean-verifier soundness holds for EVERY witness/reference input, not just honest decoder outputs. Score records remain immutable. No random-split failure event is needed or charged.

## 3. A growing balanced tree: exact oracle and input-weighted caps

In the main range set d=floor(floor(log2n)/2), a=2^d, m=n+160, r=ceil(m/a), L=2^r. Partition the m REAL selected phase bits into a consecutive groups of sizes r_i=floor(m/a) or r, summing exactly m. A raw list has its PUBLIC length2^r_i<=L, not2^r phantom source bits. Its records contain unreduced integer subset sums and original real-bit IDs. Native sorting pads with presence0 as needed; no extra source copy or subset multiplicity is introduced. Put
 A_d=sum_(j=1)^(d-1) (a/2^j)*3^(2^(j-1)), C_d=nextpow2(A_d),
 Pcap=2^160*C_d*L, K=2^162, Kcarry=nextpow2(m+1).
All are exact public integers, with the actual C_d growth charged in9. Every nonroot output cap is Pcap; root cap is K. All overflow flags reject the WHOLE query.

For target y and padded carryk start T0=y+kN. At level j=1..d-1 there are v_j=a/2^j pair joins. Choose v_j-1 FREE r-bit hashes h_(j,i), derive the last as(T_(j-1)-sumfree h)modL, and set T_j=(T_(j-1)-sumall h)/L, an exact signed integer. At each node join its two child records on(q_left+q_right)modL=h_(j,i), retaining full payload IDs and q_new=(q_left+q_right-h_(j,i))/L. Initial q values are raw UNREDUCED subset sums. Root matches EXACTinteger q_left+q_right=T_(d-1), then sorts fullb IDs canonically. Negative T_j is bounded signed data, never an array address. All a-1 nodes are explicit native sort/scan duplicate joins, not supplied oracles.

The number of FREE hashes is F=sum_(j=1)^(d-1)(a/2^j-1)=a-d-1. Search X comprises these F r-bit fields, carry in[0,Kcarry), rank in[0,K), hence H=L^F*Kcarry*K, a power of two. Reject carry>m or invalid rootrank. A quantum rank request FULLSCANS all K slots. Every surviving b determines uniquely its carry(sumW_ib_i-y)/N, every node residue hash, and its canonical rank. Conversely all root/hash equalities reconstruct the full integer sum y+kN, so f_W(b)=y modN. Coincident sums retain distinct original IDs. Inverse F_Wy(b) computes these same actual hashes/carry, recomputes the SAME bounded tree and FULLSCANS its root for b/rank; absent or invalid0. This is a unique-index reversible oracle, not a many-representation finder.

We prove uniform INPUT(W,b) cap bounds for IID W_i uniformZ_N. A nonroot level-j node contains h=2^(j-1) disjoint child-pairs of raw groups. Compare any alternate assignment with the actual b restriction; D_i is its unreduced integer difference in childpair i. Sharing b's entire subtree of residue hashes is equivalent to: each D_i=0modL; every binary-pair sum=0modL²; every four-pair sum=0modL³; and so on up to the node's sum=0modL^j. These are algebraic DIFFERENCES of b's own hash constraints, so no independence of W-dependent target/hash values is asserted.

Fix an active set S of e changed childpairs. For each choose one original label variable X_i with coefficient+/-1 in D_i; these variables are distinct, independent uniform[0,N). Condition all other labels, so D_i=sigma_iX_i+c_i. At every nonempty node of this binary constraint tree designate its LEFTMOST active leaf as pivot. For each active leaf i, nodes with pivot i form a consecutive chain from that leaf; let its length be t_i. The sum of these lengths is w(S), the number of nonempty constraint nodes. The pruned tree has e leaves and at least e-1 branching nodes, hence w(S)>=2e-1, with unary ancestors only increasing it.

Count X_i RIGHTTOLEFT. Previously satisfied constraints whose pivot is to the right do not involve X_i. The largest node with pivot i gives ONE affine congruence with coefficient sigma_i=+/-1 moduloL^t_i. It implies every smaller constraint on i's chain: the removed sibling is either empty or has its own already-satisfied sum divisible by the required lower modulus. Thus at mostceil(N/L^t_i) choices are possible, and multiplication gives at most productceil(N/L^t_i) solutions. Inconsistency only reduces this count. Since t_i<=j and N>=L^j (proved9), the probability is at most2^e/L^w(S). This is explicit triangular elimination, not independent random residue assumptions.

Each changed childpair has at mostL² alternate real-bit assignments, even for unequal groups. The contribution for activityS is therefore at most L^(2e)*2^e/L^w(S)<=2^e L. Summing nonempty S and the equal-b contribution gives expected actual bucket size<=L(3^h-1)+1<=3^h L. Child caps only remove entries; to lose b some uncapped actual-b node must exceed its cap. Summing over ALL a-2 nonroot nodes gives total expected lost INPUTmass<=A_d L/Pcap<=2^-160. The factor A_d grows with n and is not hidden in a constant.

Put M0=2^m, mu=M0/N. Since m=n+160, 2^160<=mu<2^161. Distinct full subsets collide moduloN with probability1/N by the +/-1 coefficient argument. Therefore V(W)=(1/N)sum_y(c_y/mu-1)² has E V<1/mu. For heavy c_y>K, let v=K/mu-1>=1. Weighted INPUTmass is at most V(W)(v^-2+v^-1), so its mean<=2/(mu*v)<=4/K=2^-160. Exclude those entire heavy columns only in analysis. On nonheavy c_y<=K no root cap can overflow. If cprime is the physical surviving count there and analysis0 on heavy columns, ell=1-sum cprime/M0 satisfies Eell<=2^-160+2^-160=2^-159. The physical heavy-column unitary remains bounded.

## 4. Actual public-nominal-count positive preimage column

Put M0=2^m, mu=M0/N. These are PUBLIC rationals/integers, independent of W,y,s. Main-range m=n+160 gives2^160<=mu<2^161. Let cprime_y be the physical surviving marked count for nonheavy targets c_y<=K. In analysis only set cprime_y=0 on heavy columns, as in3; those entire columns are charged as lost input. The physical oracle/unitary always keeps its public caps and may behave arbitrarily on heavy inputs. No global quantumcount estimator, countcopy or countuncompute is executed. Exact bucket counts inside the bounded join remain ordinary explicit Boolean words.

Generate finitepi P_pi/D_pi as native2 with precision b=2log2H+40. Compute PUBLIC
 j=floor-sqrt(floor(P_pi²*H*N/(16D_pi²*M0))).
Its distance from(pi/4)sqrt(H/mu) is<2: finitepi scaling contributes<1/16, and floor-sqrt of a floored nonnegative rational equals floor of its real square root. All integers haveO(n)bits, and j generation/storage/full fees are counted. The ACTUAL loop executes EXACTLY these j iterations, not an old sqrtH loop with inactive controls. j=O(sqrt(H/mu)); both it and its inverse loop are fixed by the public input.

Start X uniformly on its power-of-two H domain and apply exact
 G=(2|u_H><u_H|-I)(I-2P_mark)
exactly j times. Every G genuinely invokes the bounded mark word; no fastpower is assumed. Native uses the positive diffusion scalar exactly. A fixed|1> helper supplies any minus compensation, then is cleared; no y-dependent phase is dropped. For physical count c, its two-dimensional angle is theta=asin(sqrt(c/H)) and marked amplitude sin((2j+1)theta). c0 has no marked component.

Let tau=2^-40. Call a target REGULAR if |c_y/mu-1|<=tau and d_y=c_y-cprime_y<=tau*mu. Then 0<cprime_y and |cprime_y/mu-1|<=2tau. Put z0=sqrt(mu/H), z=sqrt(cprime_y/H). Main-range K>=2mu andH=L^F*Kcarry*K imply z0<=L^(-F/2)<=L^-1<=2^-64<=tau/32, sincea>=64,F>=2,r>=n/a>=a. Also z<=2z0<=1/4. Write j=pi/(4z0)+eta, |eta|<2. From z<=asinz<=z+z³, |sqrt(1+d)-1|<=|d| for|d|<=1/2, andpi<4,
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

Coherently choose an ordered m-subset of witnessD by Fisher-Yates range draws, d_sel=ceil(log2(4m)) trials each, retaining ALL fair raw coins. Validity>=3/4, and conditional validity gives EXACT uniform ordered subsets, independently of source values. Copy the classical label bank to quantum work and route each selected phase/label through a FULL q-position scan. All coin/buffer/routing work is polynomial. Coins remain orthogonal through acceptance, so the clean acceptance effect is the positive weighted average over returned subsets.

The malformed count in the witness bank is at most the TOTAL b<=Q/(32n). Main-range m<=2n and m<=q/2 give
 b/(q-m)<= (Q/(32n))/(Q/4)=1/(8n).
After any previous all-good draws this bounds the next bad probability. Thus the conditional all-good weight is at least(1-1/(8n))^m>=1-m/(8n)>=3/4 by Bernoulli's inequality. Together with sampler-validity its weight is>=9/16; use the conservative p0=1/4. The sharper ratio b/(q-m) matters: subtracting m/q as an additive error would give an erroneous exponential loss at unbounded n. No bad-set knowledge enters the circuit.

Let B be the normalized valid-all-good DECODER-ONLY effect requiring the true full candidate and the PGM-zero flag; 0<=B<=I. It does not consult score data. V is the coherent selector/routing, decoder4-5, known-ADD readout and exact score marker2 with dedicated untouched score scratch. C accepts only selector-valid/PGM-zero/candidate<N/score. On the score-uniqueness event its predicate equals the true-candidate predicate for EVERY input, so the actual clean acceptance effect A>=p0B. No such inequality is used off that event. V has no internal measurements.

Given ALL good hidden labels, the selected good phases are pure products factoring from the remaining bad/reference state; B ignores unselected/bad phases. Its mean completeness is(5.1) over the UNCONDITIONAL IID good-label marginal, irrespective of bad reports. Markov gives failure<=1/1024 for an event on which Tr(rho B)>=1-1/1024. Do not condition label uniformity on verification outcomes, score success, bad reports or previous survival. Intersect this event with the score/source events by a union bound; source-label distance is charged once.

## 7. Randomized subspace reflections, unknown witness and exact safety

D is ALL original witness phase wires; A is every other mutable V wire, initially0. P=I_D tensor|0_A><0_A|, excluding immutable read-only data. Qv=V^dag C V; Av=P Qv P onRangeP. On the score event Av>=p0B with the ACTUAL constantp0=1/4 proved in6. The decoder-only B from Section6 hasTr rho B>=1-1/1024 except the already bounded unconditional good-label event.

For E=1_(Av<c p0), EBE<=cE. Hence
 ||E rho^(1/2)||_HS <=||E B^(1/2)rho^(1/2)||_HS+||(I-B^(1/2))rho^(1/2)||_HS <=sqrt(c)+sqrt(epsilon)
wheneverTr rho B>=1-epsilon, since(1-sqrt b)^2<=1-b. At c=epsilon=1/1024, initial spectral mass below a0=p0/1024 is<=1/256. This bound does not assume A and B commute.

First make ONE binary Qv test: apply V, measure ONLY C; accept/output candidate, or on failure apply literalV^dag, leaving state inQv-perp. Put U=(I-2P)(I-2Qv), each factor an EXACT subspace phase reflection. I-2P computes all-zero(A) in a separate clean AND-tree apparatus, phases its single flag withZ and reverses the entire Boolean computation, returning apparatus0 on ANY A. I-2Qv is V, Z on C, literalV^dag. No source preparation inverse or reflection about the unknown D state occurs.

Choose the ACTUAL constantJ=1024. Sincea0=p0/1024=1/4096, J=16/sqrt(a0). For at most16 trials choose fresh UNIFORM CLASSICAL j in[0,J) by log2J fair bits, apply U^j, then make the same binary Qv test and stop on acceptance. On failure literalV^dag returns toQv-perp. Charge all j<=J-1 words; discard only classical trial coins, never reset D/A or measure P. At timeout output0. The program acquires no additional originals.

In a Jordan blocklambda=sin^2theta for P,Qv, starting inQv-perp, acceptance afterj rotations is sin^2(2jtheta). Forlambda in[a0,1-a0], sin(2theta)=2sqrt(lambda(1-lambda))>=sqrt(2a0). Geometric summation gives
 r_lambda=(1/J)sum_(j=0)^(J-1)sin^2(2jtheta)>=1/2-1/(2J|sin(2theta)|)>2/5.
On every failed Qv test, that block is AGAIN its unique Qv-perp direction. Thus independent classical choices j renew the same success rate; sixteen trials fail<= (3/5)^16<1/1024. This is exact Jordan-block renewal, not a conditional freshness assertion for the original witness. Cross-block/reference coherences do not affect trace probabilities because each map preserves the blocks. Forlambda>1-a0 the INITIAL Qv failure is< a0; forlambda<a0 bound by its initialmass1/256. Total failure on score/good-label events is<=1/256+1/1024+a0<.01. Degenerate lambda0/1 obey the limiting statements directly.

Safety is exact for dirty A: S=RangeP+Range(QvP) is invariant under P,Qv, their complements AND both reflections. Every reachable Qv-accept state lies inRange(QvP), and after V lies inRange(CVP), where the clean-input exact score marker forces the ENTIRE true candidate for every D/reference state. Globally dirty false-accept states elsewhere need not be sound. No fine-grained work measurement is used.

Union the source-label distance, single capped translation-range abort, score and good-label event failures with this conditional failure. No global permutation/split failure event exists. Unconditional whole-secret success is>=2/3 under the SAME literal1/(32n) promise for everyN,s. Every original was already acquired; all trial/rotation counts are fixed.

## 8. Finite fallback, same acquisitions/noise

For n<n0 use the SAMEQ/fixed-bank/score; discard unused witnesses with full charge. On its events the score marker has exactly one solution inH0=2^n. Do16 independent trials: uniform classicalj in[0,J), J=2^(ceil(n/2)+2); initialize a fresh uniform candidate register, perform j exactGrover words for the marker, measure/check the candidate classically and return firstpassing. No new source copy is acquired.

For theta=asin(1/sqrtH0), mean trialsuccess is
 (1/J)sum_j sin²((2j+1)theta)=1/2-sin(4Jtheta)/(4Jsin2theta)>=1/2-1/(16sqrt2)>2/5,
usingJ>=4sqrtH0, sin2theta>=sqrt(2/H0). Failure<=(3/5)^16<1/1024, independently across fresh trial coins/search initializations on fixed score data. Same source/score union gives success>=2/3. WorkO(2^(n/2)poly(n)), spacepolynomial, exactQ. The finite setn<n0 has a finite maximum ratio to the declared envelopes, absorbed into an outside constant independent ofN,s,outcomes. No faster exponential rate is asserted on that finite prefix.

## 9. Uniform whole ledger for growing arity

Main n>=4096 gives a²<=n<4a², a>=64,d>=6, m=n+160<=2n, and padded length ar<=n+160+a<=2n. Also d-1<=a/4 (true atd6 and preserved when a doubles), so(d-1)r<=ar/4<=n/2<=n-1. HenceN>=L^(d-1), as required by EVERY level's lattice count. Every record uses O(n)-bit full sums, signed quotients, real-bit IDs, flags and total/offset/address fields. Unequal public group sizes never pad the REAL source input: M0=2^(n+160), notL^a.

There are a-2 nonroot nodes. Each coefficient in A_d is at most3^(a/4), hence A_d<=a*3^(a/4), and C_d<2A_d. The ACTUAL Pcap=2^160*C_d*L is therefore O(a*L*3^(a/4)), with its fixed160-bit factor charged. K=2^162<=Pcap because A_d*L>=4. The WHOLE a-1-node tree, raw arrays and root have total padded lane count
 S=O(a*Pcap)=O(a²*L*3^(a/4))=O(n*L*3^(a/4)).
This is not a fixed-arity constant: the full growth of a,A_d and all arrays is included. Each node retains every comparator/scan/Boolean history until literal reversal.

Native3 sorting/scans cost O(Sn²) record operations and conservativeO(n²) gates/saved bits per operation, so the WHOLE mark oracle hasO(Sn^4) gates/qubits. Raw-list generation, quotient/hash/last-target/carry arithmetic and FULLK root/rank scans fit. Native4 running-offset/shifted-stride generation costs amortizedO(n²) per elementary gate INCLUDING the full global address fee, so TOTAL oracle work isO(Sn^6). Node-level public setup is polynomial and included; no per-gate free multiplication is assumed.

K/mu<=4, Kcarry=O(n), so the PUBLIC actualj0=O(sqrt(H/mu))=O(L^(F/2)*sqrt n), F=a-d-1. Exactlyj0 repeated G words are emitted; no global quantumcount or fast power exists. A full column/inverse costs
 O(L^((a-d+1)/2)*3^(a/4)*n^(15/2)).
Selector/score/source/known-ADD readout/initialization/reset work is polynomial and fits this bound; public pi/root/capacity generation is charged. The separate all-zero phase apparatus is linear in the O(Sn^4) mutable qubits, its full word costsO(Sn^6), and the constant outer1024-by16 schedule is included. All failed/capped or nominally parallel work counts sequentially.

Peak qubits O(Sn^4)=O(L*3^(a/4)*n^5) include ALL tree nodes/padding/histories, constantmany mark/output/inverse regions, all originals/probes/coins/arithmetic and all-zero phase apparatus. Histories are actually cleared onEVERYX/W/y basisstate and reused between iterations. Classical source/score recordsQ O(n) bits useO(n²); public offsets/directory ofa entries withO(n)-bit fields useO(an)<=O(n²), and the bounded generator/counters/constants fit the same budget. A_d hasO(a)bits and is generated by finite integer powers/sums. Public arithmetic may use irreversible inplace scratch; no classical gate-history tape or exponential circuit/list is stored. Malloc countsALLbits/qubits and log2(Malloc+2)=O(n). Every indexed classical operation and quantum gate pays that FULLfee; quantum-selected reads are full scans/sorts.

For the explicit envelopes write c=log2(3)/4<2/5, using3^5<2^8, and x=sqrt n/a in[1,2). Then r<=n/a+161 and
 r+c a<=sqrt n*(x+(2/5)/x)+161 <=(11/5)sqrt n+161,
since(5x-1)(x-2)<=0. Thus SQ=O(2^((11/5)sqrt n)n^5).

The time exponential is E=(a-d+1)r/2+c a. Since ar<=n+160+a and r>=n/a,
 E<=n/2+80+(9/10)a-(d-1)n/(2a).
Use d=(1/2)log2n-log2x. After extracting n/2-(1/4)sqrt n log2n+80, the remaining coefficient ofsqrt n is
 U=-(x-1)log2n/4+(x/2)log2x+x/2+(9/10)/x.
For n>=4096, its first term is<=-3(x-1). Concavity gives log2x<=(3/2)(x-1), since ln2>2/3 (the strict midpoint integral bound on1/t over[1,2]). Hence(x/2)log2x<= (3/2)(x-1), and x/2+(9/10)/x<=7/5+(x-1)/2. ThusU<=7/5-(x-1)<=7/5, proving
 T=O(2^(n/2-(1/4)sqrt n log2n+(7/5)sqrt n)*n^(15/2)).
Time growth index is1 because its exponent is n/2+o(n); quantum index is1/2, classical/sample indices0. These are exact rational structured envelopes, not an unknown inner big-O.

Every branch acquires EXACTQ=3*2^40(n+32), even on abort/fallback; no restart changes it. Fixed first/second banks and actual1/(32n) promise apply to the SAME program. For n<4096 the same finite fallback8 supplies every N with a finite uniform outsideconstant; growing-tree arrays are not allocated there. All four resources and the full fractional model hold jointly. No subexponential TIME, all-coordinate dominance or optimality is claimed.

## 10. Scope, credit and provenance

Growing-tree/PGM circuits and all quantified native lemmas are complete in this archive; tests/verdicts are not premises. The standard tools credited in0, comparison networks/prefix scans/schoolbook arithmetic and two-projector decomposition are not claimed invented. Related Helm–MayPQCrypto2020 subset-sum tradeoffs supply no assumedpreimage oracle. Earlier published source9fd0fa0e joint/RQ methods are rederived here, not substituted by its acceptance. The actual earlier submission documents its own local operational failures/compaction; no hosted judgment is asserted here. This changed growing-arity configuration requires its OWN fresh whole-proof review; no parent verdict is reused.

Randomized Grover-length/rotation credit: Boyer, Brassard, Høyer and Tapp, arXiv:quant-ph/9605034; amplitude amplification/estimation credit Brassard, Høyer, Mosca and Tapp, arXiv:quant-ph/0005055. The exact unknown-witness/spectral-tail/reachable-safety application is proved here, not imported as an uncosted oracle.
