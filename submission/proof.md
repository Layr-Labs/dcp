# WD22-MARGIN160: trimmed recursive window dissection with linear quantum space

## 0. Joint theorem and exact configuration

For every integer N>=2 and s in Z/NZ, put n=ceil(log2 N),d=floor(log2 N),N=2^a M with M odd. The SINGLE algorithm below recovers the entire s from independent ideal cyclic DCP copies with unconditional probability at least1-2^-8. EVERY branch, including rejected copies, wrong estimates, failed listing/merges and cap aborts, satisfies jointly

 T=O(2^[(1112693/471750)sqrt(n)-160n^(49/100)]),
 SC=O(2^[(3/20)sqrt(n)-12n^(49/100)]),
 SQ=O(n),
 Q=O(2^[(1112693/471750)sqrt(n)-172n^(49/100)]).

All constants are absolute and growing exponent coefficients are literal. Clean-copy malformed tolerance is0. Below n=2^32768 execute the finite exhaustive branch of Section9. Above it compute exactr=ceil(sqrt n),U=min{u>=0:u^100>=n^49},Lg=ceil(log2 n),w=floor(3r/20)-16U,y7=ceil(3w/4),y11=ceil(35w/34),y16=ceil(7w/8),y22=ceil(1533r/10000),mu=2w+y7+y11+y16+y22,kappa=ceil(log2 mu)+3,c0=kappa+1. K=8192(3r+Lg+30); all batch caps are defined before extraction confidence is chosen. Section5 fixes the binary/seven/eleven/sixteen/twenty-two-input schedule. These are operational widths/counts and finite caps, not just metadata.

## 1. Material sources and counted model

The immediate author working source is the complete WD16-MARGIN108 proof,whose physical framework and recursive7/11/16 definitions are retained but whose verdict is not transferred. The new contribution here adds LIST22(first6+last16),its525-per-guess cost bound and1024 normalized expected-step budget,a larger StepCap2^(2kappa+14),the new terminal22-input phase and actual3r/20-16U width. The direct public source is WD16-221(4371b084-3f7e-4d31-874e-6739549feb0a), canonical3658bb118474eb8ce50154b377bee2c5d72661dd, fullproof SHAcd8c7636688a0455a7162658f59ab0de5317a7f38a1638945195295e261630ac, read in full. It supplies recursive seven/eleven/sixteen-input listed merges, full-fiber abort/second-moment analysis, node-budget phases and physical batch framework. WD11-210(438efd04-e4d1-4b4a-bb03-de909e42ab7e) separately supplies the inspected eleven-input recursive step and whole-fiber failure method. DSW-2255(a5bd20c1-c4b5-45cf-a31b-99c1a01ac1ac) supplies the inspected larger-K/Y guard method for time exponents above2sqrt n through that lineage. These literal older numeric profiles are replaced here.

The author's actual DSW-MARGIN96 working source supplies the rewritten common source/extraction, scanned binary-merge, coarse-conditioning, physical decoder, all-branch ledger and U-margin proof format. It is independently reviewed but that verdict is no premise here. The present kernel is WHOLE listed fiber with abort on overflow, replacing that source truncated-membership-list kernel. Primary public DSW-178(805e29da-0e31-4efe-9049-8cf98151a91e) and the inspected IFC1(1294d17f-2acf-4e10-9996-6b4375388f49),DS7(151242ce-c9a9-4927-8937-f43b014386d4),MW4(e93f341a-7965-4a93-b5c4-7b0f7a799c37),PM4(2c82753c-68eb-449e-85b0-5b21e7c37eba),HPC(2aad498c-d5e9-4f64-a222-3b2f7f961738),LL(2db348f1-6660-48c8-8e10-b056131f6baa),CS1(f1481815-9577-4990-abe3-7b79fa5d9284),MWC(fba0753d-0ac1-4826-a154-51f63448765b) supply their qualified physical/window/listing/node-budget frameworks through the primary sources. No heap-pair stream, pairing/recycling pool, Grover kernel or older verify/retry extractor is run. PSieve(4256e671-97b0-4f84-82ce-12aeee17224e) is an inspected comparator: its consecutive-pair bucket count differs from the measured-rank remainder proof here, not a claimed source of this exact kernel/inequality. The author's public ODDPOLYCAP86-FRACTIONAL(670d2a5b-63e5-43be-8df5-daab8ea1c491) separately informs integer U margins/native-polynomial absorption; its odd-token kernel/clipped geometry/exponential quantum arena are not run. These are actual qualified uses, not certified graph ancestry.

The actual new22-input recursion,added phase,changed widths/counts and finite caps are specified and proved below. This is a derived extension,no priority or optimality claim. The sharper integer log7/log11 certificates and U-margin method are retained with independently changed complete bounds. All necessary mathematical arguments are supplied below; source verdicts and audits are not premises.

A core operation is an exact Clifford+T gate (Toffoli decomposes into a constant number), single-qubit measurement/reset, bounded-fan-in Boolean operation, or classical bit read/write. A b-bit arithmetic operation costs O(b). Every core operation additionally pays ceil(log2(A+2)) address bit work for TOTAL allocated classical bits plus qubits A. Each copy costs n+1. Classical gate generation, all initialization and inactive fixed scratch are counted. No QRAM, free-word arithmetic, ideal state preparation or uncharged source oracle is supplied.

## 2. Source, physical transforms, and label extraction

Set omega=exp(2pi i/N), chi_k=N^-1/2 sum_u omega^(ku)|u>, and phi_k(s)=(|0>+omega^(-ks)|1>)/sqrt2. Expanding the data basis and averaging the coset offset kills all distinct Fourier labels, giving exactly

 rho_s=N^-1 sum_(k=0)^(N-1) |phi_k(s)><phi_k(s)| tensor |chi_k><chi_k|.

Independent source copies therefore admit independent uniform latent k. This is an equality of density operators under any adaptive instrument, not an assumption that the controller receives k. An X on the control changes the negative phase to the positive phase up to a global scalar.

For a known unit alpha modulo N, multiply data u by alpha modulo N: the source becomes rho_(alpha s). Compute with controlled constant modular additions, swap and uncompute using alpha inverse; O(n^2) core operations and O(n) scratch suffice. A controlled subtraction c on the |1> data branch changes rho_s exactly to rho_(s-c), at O(n) cost. Modular constant additions use ripple carry, comparisons, selectors, and uncomputation. Define these permutations as the identity on encodings >=N; all registers have fixed widths and costs include those tests.

The controller constructs a fixed rational trigonometric table indexed by v=0,...,4095. Machin's identity with 40 terms in each arctangent bounds pi within 2^-90; 80 Taylor terms on angles below 7 and rounding to denominator 2^20 give Cos[v],Sin[v] within 2^-20 of cos(2pi v/4096),sin(2pi v/4096). These finite loops are part of the program, not advice. The tails satisfy the alternating arctangent bound and 7^81/81!<2^-170. Put tab_beta(x)=Cos[floor4096x] or Sin[floor4096x]. Lipschitz continuity gives uniform error <2pi/4096+2^-20<1/625.

Precompute the copy cap Qcap of Section 9, then h=ceil(log2(Qcap(n+5)))+12, F=2^21 h, J=n+4. Label extraction on chi_k performs, for j=0,...,J, F X-tests and F Y-tests of controlled translation by (N-2^j) mod N on an ancilla in |+>. Its eigenvalue is exp(2pi i 2^j k/N). Tests leave chi_k and all spectators unchanged conditioned on k, and have independent signs of means cos/sin(2pi 2^j k/N). Each uses O(n) exact gates.

From empirical coordinates x_j,y_j choose the least q in [0,64) maximizing x_j Cos[64q]+y_j Sin[64q]; set alpha_j=q/64. When both means are within 1/1024, table errors imply dot-product error <1/256. A nearest direction has value >=511/512, while a direction at distance >=1/16 has value <=31/32. Their gap 15/512 exceeds 2/256. Thus alpha_j approximates 2^j k/N within 1/16 on the circle. Starting at g_J=alpha_J, successively choose the preimage g_(j+1)/2 or (g_(j+1)+1)/2 nearest alpha_j. If the previous error is e<1/16, the correct preimage is within 1/16+e/2<3/32 of alpha_j and the other beyond 13/32; the error halves. Finally |g_0-k/N|_circle<2^-(n+8)<1/(2N), so rounding Ng_0 modulo N recovers k.

For independent bounded signs Hoeffding's estimate gives each mean failure <=2 exp(-F/(2*1024^2))=2e^-h. The union per call is <=4(n+5)e^-h. Even for adaptive calls, at most Qcap calls have any wrong result with probability <=4(n+5)Qcap*2^-h<=2^-10. Couple the ideal process that substitutes latent k for each extracted label to the real process until this event. Every real call returns an n-bit label and resets its data after its fixed tests; its resource bound holds even on error. Cost is O(n^2h) core work and O(n) classical/quantum scratch. The ideal analysis never conditions on internal extraction outcomes.

## 3. Phase vectors and exact physical merges

A phase vector of length 2^lambda consists of a lambda-qubit index and a classical table a[x] of nonnegative 3n-bit labels. Ideally its state is 2^(-lambda/2) sum_x exp(2pi i a[x]theta)|x>. It is collimated to p if the labels share a residue modulo 2^p. A lookup into an E-row table with v-bit fields is implemented by scanning every row, computing equality to its known index with a Toffoli chain, XORing field bits under that flag, and clearing the chain. This self-inverse circuit costs O(E(lambda+v)) gates, O(lambda+v) scratch, and explicitly reads/generates every table bit; there is no QRAM. Computing, swapping/XORing and uncomputing additions makes clean reversible arithmetic. Sorting/searching is classical bit arithmetic.

### 3.1 Binary merge

Inputs are disjoint phase vectors of length L=2^lambda collimated to p; desired output length L'=2^lambda'. Write labels a[x]=cA+2^p hA[x], b[y]=cB+2^p hB[y], and car=floor((cA+cB)/2^p). Lookup and cleanly measure e=(hA[x]+hB[y]+car) mod 2^b, for the allocated nonnegative bit count b. Sort y by (hB[y] mod 2^b,y); store inverse positions. For each x binary-search the run of matching y, store its endpoints lo_x,hi_x and cumulative offset off_x. Fiber size sz=sum_x(hi_x-lo_x). On a matching pair its rank is off_x+pos[y]-lo_x. Compute that rank into a fresh register by lookups/arithmetic; measure block floor(rank/L'). If the whole block is not contained in [0,sz), fail and release both inputs. Otherwise, for every v in the block find its unique pair via the offsets. Lookup the pair from v to XOR-clear x,y, and clear known high rank bits. The remaining low lambda' rank qubits form the output, with labels a[x_v]+b[y_v]. On failure all qubits are reset and not reused.

All pre-block measurements are computational measurements of functions of equal-magnitude indices, so fiber probability is sz/L^2 and its rank is uniform. Sum of discarded remainders is <=2^b(L'-1); hence failure probability <=2^(b+lambda'-2lambda), without a label-distribution assumption. Successful reindexing preserves the original phases and makes every sum collimated to p+b. The rank inverse is a bijection on that block. The lookup passes, mergesort, binary searches and additions cost O(n(L+L')) core work with O(sqrt n) quantum scratch and O(n(L+L')) classical scratch when lambda,b=O(sqrt n). Rank functions have O(sqrt n)-bit fields; only the final label additions need 3n-bit fields.

### 3.2 Recursive listed merges at arities seven, eleven, sixteen, twenty-two

Let f be 7,11,16,22, and define (k_f,e_f)=(3,4),(4,7),(5,11),(6,16). Inputs have disjoint leaves, common length L=2^lambda>=16 and collimation position p. For desired exponent 1<=lambda'<=lambda+1 and window v require lambda>=kappa+4 and 0<=v<=(k_f-1)lambda-kappa-1. The exact allocated bit count is b=f lambda-lambda'-kappa-v; it is at least 3lambda, and for f=11 at least4lambda. Define

 m_f=2^(lambda'+kappa), Cp=2^(kappa+2)m_f,
 StepCap=2^(2kappa+14)L^e_f 2^-v.

These are actual finite caps. The larger step allowance than the public WD16 source pays a conservative explicit preprocessing budget below; it changes only absolute factors in resources. Write c_j=label_j[0] mod 2^p, a_j[x]=floor(label_j[x]/2^p) mod 2^b, car=floor(sum c_j/2^p). By row-scanned lookups and clean reversible additions, compute and measure

 e=(sum_(j<=f)a_j+car) mod 2^b,
 c=(sum_(j<=k_f)a_j) mod 2^v.

Uncompute all temporary looked-up residues before measurement or reset from known outcomes. The tuple state is now supported on S={(x1,...,xf):both outcomes}, still with equal magnitudes and the original label-sum phases. Put target=e-car mod 2^b.

Enumerate S by the following purely classical paused generators. PAIRS(A,B;q,z) scans x of A and binary-searches sorted B for its entire matching run a_B[y]=z-a_A[x] mod 2^q. It emits every pair, retaining its current loop/run indices between calls.

LIST(V1,...,Vq;d,z,G) has q in {4,7,11,16,22}. Use split size k=2,3,4,5,6 respectively and g=(k-1)lambda, with g<=d<=b. G is a set of residues modulo 2^g, defaulting to all residues. For each gamma in G, generate the FIRST part with sum gamma modulo 2^g, in consecutive chunks of at most L tuples. For every nonempty chunk sort it by its full sum modulo 2^d; generate the SECOND part with sum z-gamma modulo 2^g, binary-search each complementary full d-bit sum in that chunk, and emit every matching concatenation. The first/second generators are fixed as follows:

| q | first k inputs | remaining inputs |
|---|---|---|
|4|PAIRS(V1,V2;lambda,gamma)|PAIRS(V3,V4;lambda,z-gamma)|
|7|for each x1, PAIRS(V2,V3;2lambda,gamma-a1[x1])|LIST(V4,...,V7;2lambda,z-gamma,all)|
|11|LIST(V1,...,V4;3lambda,gamma,all)|LIST(V5,...,V11;3lambda,z-gamma,all)|
|16|for each x1, LIST(V2,...,V5;4lambda,gamma-a1[x1],all)|LIST(V6,...,V16;4lambda,z-gamma,all)|
|22|for each x1,x2, LIST(V3,...,V6;5lambda,gamma-a1[x1]-a2[x2],all)|LIST(V7,...,V22;5lambda,z-gamma,all)|

Only recursive calls of smaller q occur, so recursion depth is at most five. Calls preserve the full residues needed for parent sums. All generated tuples retain their original input indices; no phases are inferred or used classically. Execute the top call LIST(X1,...,Xf;b,target,G), where G={gamma:gamma=c mod 2^v}. This is a finite loop over 2^(g-v) guesses. Prepare sorted copies for the literal PAIRS calls once, with at most 96L listing steps, which covers the at most44L copies/sorts used by this fixed recursion. A listing step means a loop iteration, a binary search, an emitted item, or an L-item sort charged L steps; each costs O(n) bit operations. Reports are charged twice, also paying the caller's search. Counters include every recursive step, even in a restarted inner generator. Fail and release all input qubits if the step count would reach StepCap or an append would exceed Cp. Otherwise the final list contains the WHOLE fiber.

Exactness follows by induction on q. Each tuple has a unique gamma for its first part, whose sum is in exactly one chunk; its second part is generated once by the induction hypothesis, and the full-sum search reports it once. Conversely every report has the target full sum and required gamma. Thus no tuple is duplicated or omitted when the caps do not trigger. At most one L-sized chunk per recursive activation is live, with constant recursion depth, so scratch bounds are deterministic even when a fiber is enormous.

With a complete list of sz<=Cp distinct tuples, compute its row index into a clean rank register by scanning every row and XORing its known index under equality to all f input indices, clearing the equality flag after each row. All current quantum support is in this list. Measure floor(rank/2^lambda'); fail if the selected block is incomplete. In a full block, lookup each tuple from the low rank bits to XOR-clear all input indices, reset known high rank bits and retain the low lambda' bits as output. Labels are full f-label sums. This is a bijection on the selected block, preserving phases and collimating to p+b. No membership postselection or idealized oracle is used. Every failure resets/releases its inputs without reuse.

For arbitrary fixed input tables, the outcome probabilities are sz/L^f and conditional ranks are uniform. Let Over_(e,c) be step exhaustion for the unlimited-list generator. Block remainders over the 2^(b+v) outcomes cost <2^(b+v+lambda')/L^f=2^-kappa. Hence

 Pfail<=2^-kappa+sum_(sz>Cp)sz/L^f
                   +sum_(sz<=Cp)(sz/L^f)Over_(e,c).                (3.1)

The physical operations and capped listing cost O(n 2^(2kappa)L^e_f 2^-v) core work on every branch, including abort. Indeed L^e_f 2^-v>=L²2^(kappa+1), m_f<=L², and L,Cp<=StepCap. The classical scratch is O((L+Cp)sqrt n+2^lambda' n), including chunks, sorted copies, rank list and output labels. Quantum scratch beyond the f indices is O(sqrt n). The gate stream is generated by the counted row scans.

## 4. Coarse fresh-bit conditioning and the size-weighted failure proof

Every table index has an injective 0/1 incidence vector over source leaves. This holds for subset-sum leaf tables; tensoring disjoint groups and bijective selected-block reindexing preserve it. At a merge position p condition on its selected leaf identities, previous outcomes/control and used lower bits, excluding stored but unused bits at positions >=p, extraction internals, and root measurements. Every earlier subtree decision/law depends only on bits below p; other subtrees have disjoint leaves. Induction over adaptive control leaves the residues p,...,p+b-1 of the selected leaves independent uniform modulo2^b. Full-label storage does not make those high bits part of the conditioning. Retry and cap decisions read only the used lows.


Here a bit is used by the selection/control history only when it feeds a residue,window,rank,list/block choice,retry or abort decision. Fixed-circuit arithmetic also computes higher parts of full output labels for storage. That counted arithmetic and its stored/intermediate high values are EXCLUDED from the coarse sigma-field and feed no selection decision before their position is reached. Fixed-width adders have deterministic instruction/address sequences; their high-bit values are not additional conditioned observations. The probability factorization concerns this explicitly coarsened selection history,not the entire controller memory.

Distinct tuple incidences differ on at least one coordinate with coefficient+1 or-1. Consequently the difference of their residue sums is uniform modulo2^b. Each nonempty incidence also has a uniform sum, and at most one tuple on given disjoint input groups has empty incidence. These facts do not assume independent table entries.

For a fixed residue/window outcome let sz be its fiber size. Set Z=sum_(e,c)sz²/L^f, the normalized count of ordered pairs of tuples with the same outcome. Split a tuple into its first k_f inputs and the rest. Identical pairs contribute1. Pairs differing in both parts have equal first windows with probability2^-v; conditional on that, the independent second-group difference fixes the full-residue equality with probability2^-b. Their contribution is at most m_f=L^f2^(-b-v). Pairs sharing the first or second part contribute at most respectively m_f 2^v L^-k_f and m_f 2^v L^(k_f-f), both <=m_f/L since v<=(k_f-1)lambda and f-k_f>=k_f. Thus

 E Z<=1+m_f+2m_f/L<=3m_f.

Actual outcome weighting matters: since sz1_(sz>Cp)<=sz²/Cp, expected overflow mass sum_(sz>Cp)sz/L^f is <=3m_f/Cp=(3/4)2^-kappa. This bounds entire aborted fibers, not just an unweighted probability over possible outcomes.

For the step tail fix(e,c) first. A family of q-tuples has expected size at a fixed d-bit sum at mostL^q2^-d+1 by uniform nonempty incidences and the possible empty tuple. Disjoint first/second groups are independent. Each first-part stream at modulus2^g has expected size at mostL+1, so at most2+1/L expected nonempty chunks occur. The following bounds charge scans,loop controls,caller searches and reports:

| subcall | expected pre-report cost per gamma | guesses | expected full-call cost |
|---|---|---|---|
|LIST4,d>=2lambda|2L+1+(2+1/L)(4L+2)<=13L|L|<=16L²|
|LIST7,d>=3lambda|L²+2L+1+(2+1/L)(L+16L²)<=36L²|L²|<=39L^4|
|LIST11,d>=4lambda|16L²+(2+1/L)(L+39L^4)<=118L^4|L³|<=121L^7|
|LIST16,d>=5lambda|16L³+2L+1+(2+1/L)(L+121L^7)<=250L^7|L^4|<=253L^11|
|LIST22,top d=b|16L^4+2L²+2L+1+(2+1/L)(L+253L^11)<=525L^11|L^5 2^-v|<=525L^16 2^-v plus top reports/preparation|

The first four rows include at most2(L^e+1) report steps, using their indicated lower modulus bound. For the new first-six stream, the two explicit index loops call LIST4 on the other four tables. Its expected cost is at most16L^4 plus2L²+2L+1 loop controls; the target may depend on the first two labels, independent of the other four. Its expected length is still at mostL+1. The last-sixteen generator acts on disjoint tables; its expected cost is bounded by the preceding row, including all restarts per chunk. This proves the last row. Every displayed inequality holds for allL>=16 by dividing through by its largest power and bounding1/L<=1/16. No simulation is a premise.

At the top of smaller arities the same per-gamma costs hold over onlyL^(k_f-1)2^-v guesses, giving at most525L^e_f2^-v before top reports/preparation. Top reports have expectation at mostm_f+2m_f/L+1<=3m_f<=3L²: nonempty halves contribute m_f,each empty-half case costs at mostm_f/L,and the doubly-empty tuple costs1. Reports are charged twice. Preprocessing costs at most96L. Since L^e_f2^-v>=2^(kappa+1)L² andL>=16,the two extra normalized costs are at most3 and3 respectively. Thus total expected listing work<=531L^e_f2^-v<=1024L^e_f2^-v.

With the ACTUAL StepCap=2^(2kappa+14)L^e_f2^-v, Markov gives P(Over_(e,c))<=(1/16)2^(-2kappa) for each fixed outcome. Weight safe-sized outcomes by sz<=Cp and sum their2^(b+v)=L^f/m_f possibilities. The last term of(3.1) is at most(Cp/m_f)(1/16)2^-2kappa=(1/4)2^-kappa in expectation. With block and overflow terms, conditional failure is at most(1+3/4+1/4)2^-kappa=2^(1-kappa)<=2^(2-kappa). The conditioning is the coarse selection/control past,not unused stored labels. Binary merges retain their distribution-free bound.

## 5. Actual trimmed schedule and full-capacity proof

At n>=2^32768 compute x=sqrt n,r=ceil x,U=min{u>=0:u^100>=n^49},Lg=ceil(log2 n). Uniformly U>=Lg and U/r<2^-327: use n^.49>=log2n+1 and its increasing ratio at the cutoff, and U/r<=n^(-.01)+1/x<=2^-327.68+2^-16384. Define ACTUAL

 w=floor(3r/20)-16U;
 y7=ceil(3w/4),y11=ceil(35w/34),y16=ceil(7w/8),y22=ceil(1533r/10000);
 mu=2w+y7+y11+y16+y22,kappa=ceil(log2mu)+3,c0=kappa+1.

Since16U+1<r/100000, w>=14999r/100000 and w<=3r/20. Therefore w>=3200,mu<=2r,8mu<=2^kappa<=16mu,and c0<=log2r+6<=w/64. All guards hold uniformly since the stated linear bounds dominate logarithms at the cutoff and thereafter. They do not assume monotonicity of a rounded ratio.

Use these exact phases:

 A: w binary ramp levels i,lambda_i=c0+i,v_i=0.
 B: w binary plateau levels,lambda_i=c0+w,v_i=0.
 S: y7 seven-input levels j,lambda_i=c0+w,v_i=max(0,ceil(2w-14j/5)).
 R: y11 eleven-input levels j,same lambda,v_i=max(0,ceil(3w-17j/5)).
 W: y16 sixteen-input levels j,same lambda,v_i=max(0,ceil(7w/2-4j)).
 X: y22 twenty-two-input levels j,same lambda,v_i=max(0,ceil(5w-22j/5)).

Set N_0=1,N_(i+1)=f_iN_i,H_i=log2N_i,Nmax=N_mu. Integer7^5>2^14 and11^5>2^17 imply log2 7>14/5,log2 11>17/5,log2 22>22/5. The exact phase counts ensure H_i=i in the binary phases,H_i>=2w+14j/5 in S,H_i>=4w+17j/5 in R,H_i>=15w/2+4j in W,and H_i>=11w+22j/5 in X. For the last inequality use y16>=7w/8, adding7w/2 to the preceding15w/2. Consequently

 lambda_i<=c0+H_i for binary;
 4lambda_i-v_i<=4c0+H_i for arity7;
 7lambda_i-v_i<=7c0+H_i for arity11;
 11lambda_i-v_i<=11c0+H_i for arity16;
 16lambda_i-v_i<=16c0+H_i for arity22.                       (5.1)

For k_f=3,4,5,6 respectively,the window limits are v_i<=2w,3w,ceil(7w/2),5w. They imply v_i<=(k_f-1)lambda_i-kappa-1. Thus each multi-input lambda>=kappa+4 and L>=16,with every necessary kernel precondition paid,including the new six-table window.

Nonroot capacity is q_i=f_i lambda_i-lambda_(i+1)-kappa-v_i; root capacity is R_i=f_i lambda_i-1-kappa-v_i. A prefix of m levels has Sum(m)=sum_(i<m-1)q_i+R_(m-1)=sum_(i<m)(f_i-1)lambda_i+c0-1-mkappa-sum_(i<m)v_i. Its increment is(f_m-1)lambda_m-kappa-v_m>0.

Conservative sums for A,B,S,R,W are respectively w²/2-w/2,w²+w,(53/14)w²-3w-2,(305/34)w²-4w-2,(371/32)w²-5w-2. For S/R use the positive arithmetic-progression area bound sum_(j>=0)(a-dj)_+<=a²/(2d)+a at(a,d)=(2w+1,14/5),(3w+1,17/5). For W use(a,d)=(7w/2+1,4),and y16>=7w/8:15wy16-(49/32)w² >=(371/32)w². These calculations include all ceilings.

For X,the levelwise capacity is at least21w-v_i. Its window sum is bounded by the same area bound with(a,d)=(5w+1,22/5),hence at most(125/44)w²+7w+2. Summing all phases,using w>=3200 to absorb additive constants,gives

 Sum(mu)>=(963807/41888)w²+21w*y22-19w,                    (5.2)

where963807/41888=1/2+1+53/14+305/34+371/32-125/44. With w>=14999r/100000,y22>=1533r/10000,the quadratic coefficient is exactly

 (963807/41888)(14999/100000)²+21(14999/100000)(1533/10000)
 =419089234349967/418880000000000>1.0004.

The linear loss19w<=2.85r is smaller than .0004r² at the cutoff. Thus Sum(mu)>=r²>=n uniformly,including the actual16U width trim.

For each batch1<=B<=n,choose least m with Sum(m)>=B. Allocate b_i descending from the root,up to R_(m-1) there and q_i at lower levels,until B bits are allocated;set p_0=0,p_(i+1)=p_i+b_i,p_m=B. The deficit Sum(m)-B is less than the last increment<=21(c0+w). Binary phases together have capacity at leastw²>=21(c0+w). Therefore every multi-input level is filled before greedy allocation reaches the binary phases. Its b_i equals f_i lambda_i-lambda'-kappa-v_i exactly,with lambda'=1 at a root or the next plateau exponent otherwise. Binary counts obey b_i+lambda'-2lambda_i<=-kappa. Every read position is below B;the recursive kernel is never called with inadequate b.

Use exact certificates7^135<2^379 and11^37<2^128;hence log2 7<379/135,log2 11<128/37,and log2 22<165/37. These are direct finite integer comparisons by repeated multiplication,not external asymptotic estimates. Set

 Bcoef=2+(3/4)(379/135)+(35/34)(128/37)+(7/8)4=1264301/113220.

Ceiling losses are absolute constants,so

 log2Nmax=2w+y7log2 7+y11log2 11+4y16+y22log2 22
 <=Bcoef*w+(165/37)(1533/10000)r+C
 <=(1112693/471750)r-16Bcoef*U+C,

where16Bcoef=5057204/28305>178.66. Also w<=(3/20)r-16U. These exact coefficients support the literal claims,without a growing epsilon.

## 6. Capped recursive batches and unused top bits

Set K=8192(3r+Lg+30), Dbar=3K Nmax c0, Dcap=2^12 n Dbar, Ccap=2^13 n Dbar, Y=ceil(log2 Ccap). These are all exact integers. Before any extraction, compute Qcap=n Ccap+K. From (5.3), K<=4*8192r, c0<=r and n<=r^2, we obtain

 log2 Ccap<=2.37r+4log2 r+48<=3r-1,

so Y<=3r<=n and 2^Y<=2Ccap. Bounds use a deliberately weaker leading coefficient only for this auxiliary finite guard, not for the final envelopes.

BATCH(B,supplier) requests K roots. Each source acquisition is counted against Ccap; each delivered leaf qubit against Dcap. Exceeding either cap aborts the WHOLE algorithm with output 0, releasing all storage. Supplier ideally provides independent labels uniform in [0,2^(B+1)), with each acquisition accepted with probability >=1/2. There is no pairing stage.

A level-zero vector requests c0 fresh leaf qubits with positive phase and labels k_j, taking their tensor product as index. Build its table by subset sums: lab[0]=0 and lab[x+2^j]=lab[x]+k_j. At a higher level recursively build f_i disjoint child vectors depth first, apply the allocated binary or dissection merge, and repeat from fresh children if it fails. At level m the output exponent is 1. Each root is a single qubit with known signed integer W=(lab[1]-lab[0])/2^B and relative phase exp(2pi i 2^B W theta). Measure/release each root before keeping the next; classical records remain.

To bound abort probability consider the process without caps and with ideal labels. Conditional merge failure is at most ep=2^(2-kappa). The reciprocal success inflation across mu levels is at most (1-ep)^(-mu)<=e<3 since 2^kappa>=8mu. Summing the conditional geometric attempts, or applying the stopped demand recurrence, gives expected leaf demand per K roots <=3K Nmax c0=Dbar. Markov gives demand-cap failure <=2^-12/n. Acquisition acceptance is >=1/2 independently of earlier control; the corresponding stopped acquisition expectation is <=2Dbar, giving acquisition-cap failure <=2^-12/n, conservatively <=2^-11/n. The capped process coincides with the uncapped one until a cap is hit. These expectations bound error probabilities ONLY; branchwise resource bounds use actual caps and fixed allocations.

A label is the sum of at most Ccap leaf labels below 2^(B+1). It is <2^(Y+n+1), fits 3n bits, and |W|<=2Ccap<=2^(Y+1). Even when extraction errs, all reported labels are in their supplier's prescribed range or are discarded, and these same deterministic bounds remain valid.

Write each ideal leaf label k_j=l_j+2^B tau_j. Condition on all lows l_j, all merge outcomes, listings, truncations, retries, cap/control decisions and external independent randomness, excluding root measurements and extraction internals. Every decision/outcome law depends only on bits below B: this follows from the function-measurement form of Section 3. The conditional law therefore factorizes into independent fair tau_j times a law of lows/control. Incidence injectivity gives for each root

 W=c+sum_(j in A)tau_j-sum_(j in D)tau_j,

with disjoint A,D, at least one term, and integer c determined by the coarse history. Roots have disjoint leaves. Therefore, conditional on that history, the root W's are independent,

 |E exp(2pi i z W)|=|cos(pi z)|^(|A|+|D|)<=|cos(pi z)|,
 P(W odd)=1/2.                                                (6.1)

Stored full labels do not license conditioning on unused tau_j; those are explicitly excluded. Abort and selection use only lows, so conditioning on no batch abort preserves this law. This provides the required physical frequency distribution rather than a postselected oracle.

## 7. Recovering the odd component with actual source transforms

If M=1 set s1=0. Otherwise M>=3 and d-1>=a. Write theta=s1/M for s1=s mod M. Use stages j=0,...,Jodd, where Jodd is least j>=0 with 2^(j+3)>2M; then Jodd+1<=log2 M. Each batch has B=d-1. By Euclid and CRT compute the unit alpha_j satisfying alpha_j=1 mod 2^a and alpha_j=2^j(2^(d-1-a))^-1 mod M. The supplier acquires a copy, applies Mult_alpha_j, extracts its label k, accepts iff k<2^d, and applies X on acceptance. This yields independent uniform k in [0,2^d) in the ideal process, each acceptance probability 2^d/N>1/2. Its phase parameter is alpha_j s/N and

 2^(d-1)W alpha_j s/N=2^j W s1/M mod 1.

Thus BATCH returns actual roots with relative phases exp(2pi i f_i theta), f_i=2^j W_i. No abstract frequency supplier replaces the physical copies or their costs.

For each root draw a fair beta_i by preparing H|0> and measuring it; measure that root in X or Y according to beta_i, storing sign Z_i, frequency W_i and beta_i. Its conditional mean is cos or sin(2pi f_i theta). Put P_j=j+Y+8. At j=0 enumerate every point c/2^P_j around the circle. At j>=1 enumerate every such point within circular radius 2^-(j+2) of the previous center. Endpoints are dyadic grid points. There are at most 2^(Y+8) candidates in either case. Score a candidate by sum_i Z_i tab_beta_i((f_i c mod 2^P_j)/2^P_j); retain the least maximizing c and use it as center z_j. Store K residues and advance to consecutive c by additions. Wrap the arc around zero in increasing integer order with the same recurrence or initialize its second interval explicitly. All signed residues are reduced modulo the positive power of two.

Here is the quantitative decoder guarantee. Assume theta is in the preceding arc (no assumption at stage zero), and condition on the coarse batch history of Section 6. Define xi_i=Z_i cs_beta_i(f_i zeta), using exact sine/cosine just for analysis. Across roots these are independent [-1,1] variables; their mean after averaging beta is (1/2)E cos(2pi f_i(theta-zeta)). Table error changes the total score by at most K/625. The closest grid point zeta0 is in the arc and differs from theta by at most 2^(-P_j-1); since |f_i|<=2^(j+Y+1), its mean is at least (1/2)cos(pi/128). For a far candidate |theta-zeta|_circle>=2^-(j+3), the stage arc implies 2^j|theta-zeta| in [1/8,1/2]. Equation (6.1) bounds its mean by (1/2)cos(pi/8).

For a fixed candidate Hoeffding bounds a score deviation K/64 by exp(-K/8192) (weakening the usual two-sided constants if necessary: using the one-sided tail needed for each far point and the near point separately gives at most 2exp(-K/8192), which is covered by the slack below). The mean gap satisfies

 (cos(pi/128)-cos(pi/8))/2>.0379>2/64+2/625.

These elementary numeric bounds can be certified by the finite Taylor inequalities already used in Section 2. Union over at most 2^(Y+8) far points and the near point has probability <=2^(Y+10)exp(-K/8192)<=2^-20/n, since K/8192=3r+Lg+30 and Y<=3r. Outside this event the maximizing point has distance <2^-(j+3). This is precisely the next stage's radius. Induction, then rounding Mz_Jodd modulo M, recovers s1 with total stage error <=2^-20 because 2^-(Jodd+3)<1/(2M). Root outcomes are not used to select the batch that produced them.

## 8. Recovering the power-of-two component

Let s=s1+M s2 mod N with 0<=s2<2^a. If a=0 finish. For g=0,...,a-1, let low be the already inferred low g bits of s2, wd=a-g and rem=(s2-low)/2^g, assuming prior bits correct. Shift the source by sh=s1+M low mod N, extract k and apply X. Put kk=k mod 2^wd. Since 2^wd divides N, the ideal kk is uniform on [0,2^wd), and the physical qubit phase is exp(2pi i kk rem/2^wd).

If wd=1, acquire at most K such leaves, keep the first with kk=1 and measure X, which reports rem mod 2 exactly. If none, set the bit to zero. If wd>=2, BATCH with B=wd-1 and this supplier returns K roots. Keep the first odd W and measure X; its relative phase exp(pi i W rem)=(-1)^rem gives the next bit exactly. If none exists, set it to zero. Oddness is a classical inspection of known W, and the unused top-bit argument gives failure <=2^-K for each bit, conditional on all earlier correct decoding. There is no need to assert correctness after an incorrect earlier bit. Update low and continue. Output s1+M s2 mod N.

## 9. Finite branch, caps, and total success

For n<2^32768, enumerate candidates c=0,...,N-1. For each use at most n+10 fresh copies, Shift_c and measure the control in X; reject immediately after the first minus sign. Output the first candidate with all plus signs, or 0. For c=s every sign is plus. For c!=s the data branches are orthogonal and each sign is independent fair. The chance of a false candidate surviving is at most N2^-(n+10)<=2^-10. Source, computation and memory on this finite set of bit lengths have a finite absolute upper bound. The final displayed envelope is positive at each of those finitely many n; increasing one absolute big-O constant covers their worst ratio, however large that constant is. This is a uniform terminating algorithm, not nonuniform advice.

On the main branch compute parameters, all batch allocation formulas and Qcap=n Ccap+K before the label-confidence parameter h. There are at most Jodd+1+a<=log2 M+a=log2 N<=n batch/bit stages and at most one wd=1 direct stage. Every batch stops at Ccap acquisitions or Dcap delivered leaves; the direct stage uses at most K copies. Hence Q<=Qcap on EVERY actual execution, including wrong estimates and aborts. On ABORT release everything and return zero. Arithmetic inputs outside the current supplier's accepted label range are discarded, so corrupt extraction decisions do not violate fixed widths.

In the ideal process, union of batch abort events is at most 2^-12+2^-11; odd decoder error at most 2^-20; and two-adic misses at most n2^-K<=2^-40. Add the probability <=2^-10 of any label-extraction error from the coupling. Their sum is <2^-8. The finite branch has error <=2^-10. Thus for every N,s the unconditional full-secret success probability is at least 1-2^-8. These are additive error bounds; no favorable labels, overflows or quantum measurement events are postselected without being counted. Copy independence is the stated input promise.

## 10. Deterministic resources for the extended recursion

All bounds apply directly to actual executions,including every cap failure and wrong label estimate. Parameters give K,mu,c0,w=O(r),2^c0,2^kappa=O(r),Dcap/c0=O(n^(3/2)Nmax),Ccap=O(n²Nmax),log2Qcap=O(r). The source and demand caps are actual integer counters,not expected consumption. Therefore Q<=nCcap+K=O(n³Nmax).

At most22 indices per level of at most c0+w qubits occupy<=22mu(c0+w)=O(n) qubits. The active constant-depth LIST recursion is classical;its physical merge adds onlyO(r) qubits. Extraction and source transforms useO(n),reset between calls. No coherent pool of roots is kept. All inactive declared scratch is counted,so SQ=O(n).

There are at most23 classical tables per depth-first level,each of at most2^(c0+w) fields of3n bits. These occupyO(mu*n*2^(c0+w))=O(n²2^w). The tuple cap Cp=2^(lambda'+2kappa+2)=O(n^(3/2)2^w) multipliesO(r)-bit tuple/rank fields,givingO(n²2^w) scratch. Each active recursive generator keeps a singleL-sized chunk;at most five nesting levels are live. Sorted copies/output labels are included. Binary scratch,decoder records,counters and extraction workspace fit the same bound. Allocate and initialize at declared maximal sizes even when a branch uses less. Hence SC=O(n²2^w).

Per batch,each of at mostCcap acquisitions usesO(n²) source transforms andO(n²h)=O(n^(5/2)) extraction work. A leaf-table call costsO(n2^c0) and consumesc0 delivered leaves;at mostDcap/c0 such calls occur. For a higher merge at leveli,combine(5.1) with its actual capped physical cost to get

 O(n2^(2kappa)2^(16c0)N_i)=O(n^10 N_i)

core operations. This upper bound covers all binary and smaller-arity attempts too. An attempted merge consumes at leastN_(i+1)c0 delivered leaves,none reusable by another attempt at that SAME level,even if it fails. Thus at mostDcap/(N_(i+1)c0) attempts occur there. SumO(mu)=O(r) levels to getO(n^(21/2)Dcap/c0)=O(n^12Nmax) tree work per batch. This charges every recursive restart,full-label operation,rank/inverse lookup,tuple overflow,step abort and initialization.

At each decoder stage,at most2^(Y+8) points each updateK residues ofO(n) bits and a fixed-precision score,forO(Kn2^Y)=O(n^(3/2)Ccap) work. All at mostn batches/stages,plus fixed-degree polynomial setup,giveO(n^13Nmax) core work. Setup includes exact integer parameters,CRT/Euclid,modular constants,rational tables,gate controls and initial residues. A binary ramp ofw>=.14999r levels ensuresNmax has a positive exponential,absorbing fixed setup polynomials and full-arena initialization. Every loop is fixed finite,step-capped,or consumes acquisitions/delivered leaves under a cap.

TOTAL allocated bits plus qubits have logarithmO(r). Charging that address tariff for every core operation and adding(n+1)Q source work yieldsT=O(n^(27/2)Nmax),and hence the conservative native simultaneous ledger

 T=O(n^14Nmax),SC=O(n²2^w),SQ=O(n),Q=O(n³Nmax).              (10.1)

All expectations in the failure analysis bound only error probabilities. This ledger is deterministic over every actual branch;no free-word RAM or expected-time substitution is made.

## 11. Exact literal envelopes and indices

Letz=n^(49/100),x=sqrt n,alpha=1112693/471750,Bcoef=1264301/113220. UniformlyU>=z,U>=Lg>=log2n,r<=x+1,and16Bcoef>178.66. Section5 yieldslog2Nmax<=alpha*r-16Bcoef*U+C andw<=(3/20)r-16U. Thus,with absolute additive constants,

 log2(n^14Nmax)<=alpha*x-(16Bcoef-14)U+C<=alpha*x-160z+C,
 log2(n³Nmax)<=alpha*x-(16Bcoef-3)U+C<=alpha*x-172z+C,
 log2(n²2^w)<=(3/20)x-14U+C<=(3/20)x-12z+C.

All cap/kernel constants andr-x<=1 add only constants. This proves the four exact structured objects,including zero outside polynomial powers forT,SC,Q and the literal linearSQ envelope. The finite terminating exhaustive prefix is covered by absolute big-O constants on its finite set of input bit lengths,where every displayed envelope is positive.

Each exponential envelope has a fixed positive n^.5 term dominating its negative n^.49 correction,so log2log2B=(1/2)log2n+O(1),giving exact index1/2. ForB(n)=n the index is0. These indices describe upper envelopes,not lower bounds on optimal DCP complexity. The fifth exact expression0 asserts the same joint guarantee only for independent ideal copies. It claims neither positive malformed tolerance nor impossibility of robustness. This is still index1/2,with an enormous unoptimized finite threshold;it does not achieve index1/3. The full physical mathematical argument here,not the diagnostic audit or an earlier verdict,establishes the claims.
