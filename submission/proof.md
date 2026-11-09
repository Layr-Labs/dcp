# DSW-MARGIN96: a trimmed measured-window dissection schedule

## 0. Joint theorem and exact configuration

For every integer N>=2 and s in Z/NZ, write n=ceil(log2 N), d=floor(log2 N), N=2^a M with M odd. The algorithm below, given independent ideal cyclic DCP copies, outputs the entire s with probability at least 1-2^-8. All branches, including discards, failed merges, cap aborts and wrong label estimates, satisfy jointly

 T=O(2^[(399319/225000)sqrt(n)-96 n^(49/100)]),
 SC=O(2^[(7999/20000)sqrt(n)-40 n^(49/100)]),
 SQ=O(n),
 Q=O(2^[(399319/225000)sqrt(n)-100 n^(49/100)]).

Constants are absolute; the rational coefficients inside the exponents are literal. Clean-copy error tolerance is zero. The resource objects and success guarantee all refer to this ONE configuration.

For n<2^32768 use the finite exhaustive procedure in Section 9. Otherwise compute exactly

 r=ceil(sqrt n); U=min{u>=0: u^100>=n^49}; Lg=ceil(log2 n);
 t=floor(7999r/60000)-16U; w=3t;
 y1=ceil(3t/2); y4=ceil(3t/10); y7=ceil(51r/160);
 mu=3t+y1+y4+y7; kappa=ceil(log2 mu)+3; c0=kappa+1.

Integer roots, ceilings, counters, and allocation parameters use ordinary finite bit arithmetic. This is an operational change to the table widths and level counts, not a relabeling of an older envelope.

## 1. Provenance and model

The main design source is the public DSW-178 proof (805e29da-0e31-4efe-9049-8cf98151a91e): measured windows on four/seven-input dissection, fixed-size chunks, capped listing, full-label physical merges, depth-first capped batches, and the free-frequency/2-adic decoders. This proof supplies every argument used here rather than importing its verdict. Earlier material sources inspected are IFC1 (1294d17f-2acf-4e10-9996-6b4375388f49, measured pair-sum windows), DS7 (151242ce-c9a9-4927-8937-f43b014386d4, seven-input guess/chunk listing), MW4 (e93f341a-7965-4a93-b5c4-7b0f7a799c37, physical flag/rank/block merges and overflow moments), PM4 (2c82753c-68eb-449e-85b0-5b21e7c37eba, full-label and deferred-bit formulation), HPC (2aad498c-d5e9-4f64-a222-3b2f7f961738, fixed-confidence label extraction), LL (2db348f1-6660-48c8-8e10-b056131f6baa, direct leaf-table/batch framework), CS1 (f1481815-9577-4990-abe3-7b79fa5d9284, linear merge and physical decoder framework), and MWC (fba0753d-0ac1-4826-a154-51f63448765b, node-budget schedule viewpoint). These earlier connections are qualified design/proof use through the primary source, not certified ancestry. No Grover kernel, heap pair stream, pairing/recycling stage, or earlier verification-based label extractor is executed here. PSieve (4256e671-97b0-4f84-82ce-12aeee17224e) was inspected for comparison: its distribution-free consecutive-pair count is distinct from the rank-tail remainder proof below. It supplies comparison context, not this merge or its failure inequality.

The author's ODDPOLYCAP86-FRACTIONAL (670d2a5b-63e5-43be-8df5-daab8ea1c491) informs the exact U=ceil(n^.49) margin method and separation of native polynomial factors from literal fractional-exponent envelopes. Its odd-token kernel, clipped geometry and exponential quantum memory are not used. Here the new actual trim is 16U in t, paid by spare DSW capacity. A sharper integer certificate for log2 7 and explicit polynomial absorption give the theorem. All proofs below are independent of diagnostics and earlier acceptance.

A core operation is a one-qubit measurement/reset, an exact Clifford+T gate (Toffoli has a constant exact decomposition), a Boolean operation of bounded fan-in, or one classical bit read/write. A b-bit addition/comparison costs O(b). Each core operation additionally pays ceil(log2(A+2)) bit work, with A the total allocated classical bits plus qubits. A source call costs n+1. Gates and their classical controls are generated and counted; no QRAM, free word arithmetic, or coherent random-access oracle is assumed. Thus charged work is bounded by core work times (1+ceil(log2(A+2))) plus (n+1)Q. Initialization and all scratch allocations are included.

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

### 3.2 Four/seven-input measured-window dissection

Let f=4 or 7, e_f=2 or 4, k_f=2 or 3. Inputs are disjoint phase vectors, length L=2^lambda>=16, collimated to p. Set

 b=f lambda-lambda'-kappa-v;
 m_f=2^(lambda'+kappa), Cp=2m_f+1,
 StepCap=2^(kappa+8)L^e_f*2^-v.

Require lambda>=kappa+4, 1<=lambda'<=lambda+1, b>=2lambda, and 0<=v<=lambda-kappa-1 for f=4 or v<=2lambda-kappa-1 for f=7. These hold in Section 5. Write c_j=label_j[0] mod 2^p, a_j[x]=floor(label_j[x]/2^p) mod 2^b, car=floor(sum c_j/2^p). By lookups, clean addition, measurement, and uncomputation measure the full residue e=(sum a_j+car) mod 2^b and window c=(sum_(j<=k_f) a_j) mod 2^v. Let S be the tuple fiber with these two outcomes, sz=|S|, target=e-car mod 2^b.

The classical list procedure uses the following exact generators, all with deterministic tie order.

* PAIRS(A,B;q,z): for each index of A, binary-search sorted B for the run giving a_A+a_B=z mod 2^q; emit every matching pair, pausing/resuming at any report.
* FOUR(q,z,D): last four tables are U1,...,U4. For each dt in D modulo 2^lambda, stream PAIRS(U1,U2;lambda,dt) in consecutive chunks of at most L pairs. Sort each nonempty chunk by its full sum modulo 2^q. Stream PAIRS(U3,U4;lambda,z-dt), binary-search each complementary full sum in the chunk, and emit all matches. D restricts the first-pair residue. Require lambda<=q<=b.
* For f=4 use FOUR(b,target,D), D={dt:dt=c mod 2^v}.
* For f=7 put g=2lambda. For each gamma in [0,2^g) with gamma=c mod 2^v, enumerate the first three indices summing to gamma modulo 2^g: for each x1 call PAIRS(X2,X3;g,gamma-a1[x1]). Split these triples into consecutive L-sized chunks and sort each by its sum modulo 2^b. Run FOUR(g,target-gamma,all residues) on the last four tables; binary-search the complementary full b-bit sum in the triple chunk and append each seven-tuple.

A listing step is a loop iteration, binary search, or emitted item; sorting at most L items costs L such steps, each with O(n) bit work. Preparation of sorted copies costs at most 3L steps. Stop with failure when StepCap would be reached; stop normally as soon as Cp distinct tuples have been appended. Each admissible tuple has a unique first-pair residue, unique chunk and (for seven inputs) unique gamma and triple chunk. Conversely every append has both measured outcomes, so without a step-cap failure the list contains min(sz,Cp) distinct members of S, exhaustively if sz<=Cp. No quantum state preparation or conditioning is hidden in this classical procedure.

To apply the list physically, scan each tuple row, compute equality to all f input indices, XOR its known row number into a fresh rank register and toggle a fresh membership flag; uncompute equality. Rows are distinct. Measure the flag and fail if zero. Measure floor(rank/2^lambda') and fail unless the complete block is in the list. Lookup the tuple from the low rank bits to clear all input registers and clear the known high bits/flag. Remaining rank bits are a flat phase vector of length 2^lambda'; labels are the f-label sums. Phases are preserved because the map is bijective on the selected block. Every resulting sum has the measured full residue, so collimation advances by b. All failure paths reset/release all inputs, which are never recycled.

For fixed arbitrary tables, laws depend only on label bits below p+b. Let Over_(e,c) indicate step exhaustion for that outcome. Weighted membership loss is sum(sz-Cp)_+/L^f; block-tail loss is <2^(b+v+lambda')/L^f=2^-kappa. Therefore

 Pfail <=2^-kappa + sum (sz-Cp)_+/L^f + sum (sz/L^f)Over_(e,c).                 (3.1)

The listing, lookups, rank/flag operations, and output-label generation cost O(n 2^kappa L^e_f 2^-v) core work on EVERY branch. Indeed Cp=2^(lambda'+kappa+1)+1 and L are dominated by that expression under the given window constraints. Quantum scratch is O(sqrt n); classical scratch is O((L+Cp)sqrt n+2^lambda' n), including sorted copies, chunks and the tuple list. Counters, keys, arithmetic and addresses are counted separately as specified in Section 1.

## 4. Fresh bits and capped-list failure analysis

Every table index has an injective 0/1 incidence vector over its source leaves. Tensoring tables concatenates disjoint coordinates; a selected merge block bijectively relabels distinct tuples. This proves injectivity at every level, including unsuccessful attempts before release. A label is the sum of its incidence leaves.

Analyze an attempt at position p with b more bits. Condition on the selection/control history, all already-used lower bits of its leaves, and external copies. Do NOT condition on stored but unused higher labels or on extraction test records. All earlier subtree kernels read bits strictly below p. Their measurement probabilities are determined by those bits and independent of phases. Other subtrees have disjoint leaves. An induction on adaptive steps therefore leaves the bits p through p+b-1 of these leaves independent uniform residues modulo 2^b, even though full labels are stored. This is a coarse history, sufficient to determine selected incidences and all earlier selection decisions. Labels at unused positions are not part of it. Retry/cap decisions use no such bits.

Distinct nonempty incidence sets give pairwise independent uniform residue sums: take a leaf in their symmetric difference and one in the other set. The resulting two-coordinate linear map has determinant +1 or -1 (triangular or identity), invertible over Z/2^b. This argument works for correlated entries within one table; it requires no independent-entry assumption.

For a four/seven-input tuple split its first k_f inputs from the rest. Call it good if both half incidences are nonempty. At most L^k_f+L^(f-k_f)<=2L^(f-2) tuples are not good. For a fixed outcome (e,c), a good tuple has independent uniform half sums, hence joint outcome probability 2^-(b+v). Let S count good tuples in that outcome. Then E S<=m_f. Distinct good tuples differing in both halves have independent outcome indicators by the determinant argument in each disjoint half. Pairs sharing a half have joint probability 2^-(2b+v); there are at most L^(2f-k_f)+L^(f+k_f) ordered such pairs. Consequently

 Var S <= m_f+2m_f^2/L,

because 2^v(L^-k_f+L^-(f-k_f))<=2/L under the window restrictions. Since Cp=2m_f+1 and sz is at most S plus bad tuples, use (S-2m_f)_+<=(S-E S)^2/m_f on S>2m_f. Sum over all 2^(b+v)=L^f/m_f outcomes and add the total number of bad tuples to obtain

 A:=E sum(sz-Cp)_+/L^f
 <=2^(-lambda'-kappa)+2/L+2/L^2
 <=2^(-lambda'-kappa)+2^(-kappa-2).                                      (4.1)

For the step tail, fix the outcomes first and count an unrestricted listing. For each dt in FOUR(q,z,D), the two disjoint pair sets P,P' have E|P|,E|P'|<=L+1, including the possible empty-incidence pair. Scanning P costs L+|P|, and at most 1+|P|/L chunks each require at most 2L+2|P'| steps before reports. Independence between the two table groups bounds expected pre-report work by 13L per dt. For the restricted set D, expected reports are <=L^4 2^-q |D|/L+3, where the constant accounts for empty halves; here q>=2lambda in the calls charged below. Charge two steps per report.

At f=4, |D|=L2^-v, q=b, and m_f<=L^2 2^-v, so preparation, reports and appends total <=21L^2 2^-v expected steps. At f=7, unrestricted FOUR(g,...) with g=2lambda has expected cost <=16L^2. For one gamma the first-three stream has expected size <=L+1, scanning cost L^2+size, and at most 1+size/L chunks, each with sorting cost L and an independent FOUR call on the other four tables. Expected cost per gamma is <=36L^2. There are L^2 2^-v gamma values; all remaining work gives <=37L^4 2^-v. Thus in both cases E steps<=37L^e_f 2^-v and, for each fixed (e,c),

 P(Over_(e,c)) <=(37/256)2^-kappa.

The actual outcomes are SIZE-WEIGHTED, so this fixed-outcome estimate alone is insufficient. Split sz<=Cp+(sz-Cp)_+ in the last sum of (3.1). Its expectation is at most

 (Cp/m_f)(37/256)2^-kappa+A <=(1/2)2^-kappa+A,

since Cp/m_f<=3. Combining (3.1) and (4.1) gives

 Pfail<=2^-kappa+2[2^(-lambda'-kappa)+2^(-kappa-2)]+(1/2)2^-kappa
 <=2^(2-kappa)                                                        (4.2)

for every lambda'>=1. This bound is conditional on the stated coarse past, sufficient for repeated fresh disjoint attempts. It is not asserted after revealing unused labels. Binary failure has its stronger distribution-free estimate from Section 3.1.

## 5. Actual schedule, uniform guards, and capacity

For n>=2^32768, put x=sqrt n. Since U<=n^.49+1 and r>=x,

 U/r<=n^(-.01)+1/x<=2^-327.68+2^-16384<2^-327<2^-325.

Also U>=Lg, since n^.49>=log2 n+1 at the cutoff and the ratio increases thereafter. The floor loss and 16U are less than (1/60000)r, giving

 (1333/10000)r <=t<= (7999/60000)r.

Indeed 7999/60000-1333/10000=1/60000, and 16U+1<r/60000. These enormous but fixed uniform guards imply t>=2100. Substitution gives mu<=2r; 8mu<=2^kappa<=16mu and c0<=log2 r+6<=t/64. The last inequality holds at r>=2^16384 and is preserved since logarithmic growth is slower than linear growth. All floor/ceiling definitions remain actual integer instructions.

Define levels i=0,...,mu-1:

 A: 3t binary levels, lambda_i=c0+i, window v_i=0.
 C: y1 four-input levels j=0,...,y1-1, lambda_i=c0+3t,
    v_i=max(0,3t-2j).
 D: y4 four-input levels, same lambda, v_i=0.
 S: y7 seven-input levels j=0,...,y7-1, same lambda,
    v_i=max(0,ceil((27t-14j)/5)).

Let N_0=1, N_(i+1)=f_i N_i, H_i=log2 N_i, Nmax=N_mu. The exact schedule gives H_i=i in A and H_(3t+j)=3t+2j in C/D. Since 7^5>2^14, in S we have H_i>=33t/5+14j/5. Consequently

 lambda_i<=c0+H_i for binary levels,
 2lambda_i-v_i<=2c0+H_i for four-input levels,
 4lambda_i-v_i<=4c0+H_i for seven-input levels.                   (5.1)

These inequalities allocate actual node cost against subtree size. Windows satisfy v_i<=3t=lambda_i-kappa-1 at arity four and v_i<=27t/5+1<=2lambda_i-kappa-1 at arity seven. On multi-input levels L<=2^c0 N_i.

For a nonroot level define q_i=f_i lambda_i-lambda_(i+1)-kappa-v_i. Its root capacity is R_i=f_i lambda_i-1-kappa-v_i. A prefix of m levels has capacity Sum(m)=sum_(i<m-1)q_i+R_(m-1). Equivalently Sum(m)=sum_(i<m)(f_i-1)lambda_i+c0-1-m kappa-sum_(i<m)v_i. Hence

 Sum(m+1)-Sum(m)=(f_m-1)lambda_m-kappa-v_m>0.

Nonroot capacities, and therefore also root capacities, have the following lower bounds: A level i has at least i; C level j at least 6t+2j; D at least 9t; S at least 18t-v_i. The first three phase totals are at least (9/2)t^2-(3/2)t, (45/4)t^2-(3/2)t, (27/10)t^2. The S window sum is at most (729/140)t^2+8t: compare the positive decreasing arithmetic sequence ceil((27t-14j)/5) with its triangle area and endpoint terms. Thus

 Sum(mu)>=(927/70)t^2+18t y7-11t.                              (5.2)

With t>=1333r/10000 and y7>=51r/160, its quadratic coefficient is exactly

 (927/70)(1333/10000)^2+18(1333/10000)(51/160)
 =7000837353/7000000000>1.0001.

The loss 11t<1.467r is smaller than .0001r^2 at this cutoff. Therefore Sum(mu)>=r^2>=n uniformly, including the floor loss and U trim.

For any requested 1<=B<=n choose least m with Sum(m)>=B. Allocate b_(m-1)=min(R_(m-1),B), then allocate descending levels greedily up to q_i until B bits are allocated. Set p_0=0 and p_(i+1)=p_i+b_i. Then p_m=B. If any multi-input level is present, Sum(m)-B<Sum(m)-Sum(m-1)<=6(c0+3t). Phase A alone has capacity >=(9/2)t^2-(3/2)t>=6(c0+3t). Thus descending allocation fills EVERY multi-input level before reaching A. At these levels b_i=f_i lambda_i-lambda' -kappa-v_i exactly, with lambda'=lambda_(i+1) or 1 at the root. All Section 3.2 preconditions follow: lambda>=kappa+4, lambda'<=lambda+1, and b>=2lambda (at arity four use v<=lambda-kappa-1; arity seven is even larger). Binary levels have b_i+lambda'-2lambda_i<=-kappa. Nonnegative b=0 is permitted for binary merges. All read positions are below B.

The exact integer inequality 7^135<2^379 gives log2 7<379/135. For reproducibility its two sides are respectively

 1225280161540062728885066636859253659932220047915814591596258989665758668905651575158678006823392458638363378205943
 1231312693637327475383720003129487931408741852202045208373384168882678805359287831606695820465153613775207124697088.

Using ceiling losses in y1,y4,y7 and the ACTUAL trimmed t,

 log2 Nmax =3t+2y1+2y4+y7 log2 7
 <=(33/5)t+4+(379/135)y7
 <=(399319/225000)r-(528/5)U+4+379/135,                          (5.3)

where (33/5)(7999/60000)+(379/135)(51/160)=399319/225000 exactly. Also

 w=3t<=(7999/20000)r-48U.                                    (5.4)

No positive slack has been silently added to either leading coefficient.

## 6. Capped recursive batches and unused top bits

Set K=8192(2r+Lg+30), Dbar=3K Nmax c0, Dcap=2^12 n Dbar, Ccap=2^13 n Dbar, Y=ceil(log2 Ccap). These are all exact integers. Before any extraction, compute Qcap=n Ccap+K. From (5.3), K<=3*8192r, c0<=r and n<=r^2, we obtain

 log2 Ccap<=1.78r+4log2 r+40<=2r-1,

so Y<=2r<=n and 2^Y<=2Ccap. Bounds use a deliberately weaker leading coefficient only for this auxiliary finite guard, not for the final envelopes.

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

These elementary numeric bounds can be certified by the finite Taylor inequalities already used in Section 2. Union over at most 2^(Y+8) far points and the near point has probability <=2^(Y+10)exp(-K/8192)<=2^-20/n, since K/8192=2r+Lg+30 and Y<=2r. Outside this event the maximizing point has distance <2^-(j+3). This is precisely the next stage's radius. Induction, then rounding Mz_Jodd modulo M, recovers s1 with total stage error <=2^-20 because 2^-(Jodd+3)<1/(2M). Root outcomes are not used to select the batch that produced them.

## 8. Recovering the power-of-two component

Let s=s1+M s2 mod N with 0<=s2<2^a. If a=0 finish. For g=0,...,a-1, let low be the already inferred low g bits of s2, wd=a-g and rem=(s2-low)/2^g, assuming prior bits correct. Shift the source by sh=s1+M low mod N, extract k and apply X. Put kk=k mod 2^wd. Since 2^wd divides N, the ideal kk is uniform on [0,2^wd), and the physical qubit phase is exp(2pi i kk rem/2^wd).

If wd=1, acquire at most K such leaves, keep the first with kk=1 and measure X, which reports rem mod 2 exactly. If none, set the bit to zero. If wd>=2, BATCH with B=wd-1 and this supplier returns K roots. Keep the first odd W and measure X; its relative phase exp(pi i W rem)=(-1)^rem gives the next bit exactly. If none exists, set it to zero. Oddness is a classical inspection of known W, and the unused top-bit argument gives failure <=2^-K for each bit, conditional on all earlier correct decoding. There is no need to assert correctness after an incorrect earlier bit. Update low and continue. Output s1+M s2 mod N.

## 9. Finite branch, caps, and total success

For n<2^32768, enumerate candidates c=0,...,N-1. For each use at most n+10 fresh copies, Shift_c and measure the control in X; reject immediately after the first minus sign. Output the first candidate with all plus signs, or 0. For c=s every sign is plus. For c!=s the data branches are orthogonal and each sign is independent fair. The chance of a false candidate surviving is at most N2^-(n+10)<=2^-10. Source, computation and memory on this finite set of bit lengths have a finite absolute upper bound. The final displayed envelope is positive at each of those finitely many n; increasing one absolute big-O constant covers their worst ratio, however large that constant is. This is a uniform terminating algorithm, not nonuniform advice.

On the main branch compute parameters, all batch allocation formulas and Qcap=n Ccap+K before the label-confidence parameter h. There are at most Jodd+1+a<=log2 M+a=log2 N<=n batch/bit stages and at most one wd=1 direct stage. Every batch stops at Ccap acquisitions or Dcap delivered leaves; the direct stage uses at most K copies. Hence Q<=Qcap on EVERY actual execution, including wrong estimates and aborts. On ABORT release everything and return zero. Arithmetic inputs outside the current supplier's accepted label range are discarded, so corrupt extraction decisions do not violate fixed widths.

In the ideal process, union of batch abort events is at most 2^-12+2^-11; odd decoder error at most 2^-20; and two-adic misses at most n2^-K<=2^-40. Add the probability <=2^-10 of any label-extraction error from the coupling. Their sum is <2^-8. The finite branch has error <=2^-10. Thus for every N,s the unconditional full-secret success probability is at least 1-2^-8. These are additive error bounds; no favorable labels, overflows or quantum measurement events are postselected without being counted. Copy independence is the stated input promise.

## 10. Resources, including physical address charges

We now bound ALL actual branches directly from loops, caps and fixed storage, irrespective of the ideal coupling. All stated big-O constants are absolute for this fixed algorithm. From the parameters, K,mu,c0,w=O(r), 2^c0,2^kappa=O(r), Dcap/c0=O(n^(3/2)Nmax), Ccap=O(n^2 Nmax) and log2 Qcap=O(r).

Samples: Q<=n Ccap+K=O(n^3 Nmax).

Quantum allocation: depth-first recursion stores at most seven index registers per level of at most c0+w qubits, hence <=7mu(c0+w)=O(n). Each merge adds O(r) scratch; source transformations and extraction add O(n) and are reset before reuse. Roots are measured at once, rather than retained as a bank. Therefore SQ=O(n), including all inactive fixed scratch and physical input registers.

Classical allocation: at most eight label tables per recursion level, each at most 2^(c0+w) fields of 3n bits, occupy O(mu*n*2^(c0+w))=O(n^2 2^w). Binary merge scratch is smaller. The higher-arity list/chunk/sorted scratch O((2^lambda+Cp)r+2^lambda' n), with Cp<=2^(lambda'+kappa+1)+1 and lambda'<=c0+w, also fits O(n^2 2^w). Allocate these arenas by maximal schedule widths rather than hoping for typical sizes. Decoder K records/residues and all counters/extraction work are polynomial and fit the same bound. Their complete initialization costs at most O(n^2 2^w) core work, which is below the time bound below. Thus SC=O(n^2 2^w) on every branch.

Core work per batch:

* Each of at most Ccap acquisitions costs O(n^2) transform work and O(n^2h)=O(n^(5/2)) extraction work; total O(n^(5/2)Ccap).
* A leaf table costs O(n2^c0) and consumes c0 delivered leaves. At most Dcap/c0 such calls occur.
* A merge at level i has per-attempt cost O(n 2^kappa 2^(4c0)N_i)=O(n^(7/2)N_i). For arity four/seven apply (5.1) to its physical O(n 2^kappa 2^(e_f lambda_i-v_i)) cost; binary cost is bounded by the same larger expression. This includes every rejected membership and short block. There are at most Dcap/(N_(i+1)c0) attempted merges at that level: each consumes at least N_(i+1)c0 delivered source leaves, none reused in another attempt at that SAME level. Successful lower vectors and failed subtree attempts only increase leaf consumption. Sum over O(r) levels to get O(n^4 Dcap/c0)=O(n^(11/2)Nmax) per batch, covering the leaf calls as well.
* Decoder enumeration uses <=2^(Y+8) candidate points, each updating K O(n)-bit residues and its fixed-precision score, hence O(Kn2^Y)=O(n^(3/2)Ccap). Storing known frequencies, producing all classical controls, and modular arithmetic are charged.

At most n batches give O(n^(13/2)Nmax) core work; fixed-degree polynomial setup (integer roots, exact parameters/CRT, offsets, initial score residues, gate-stream controls and the rational table) is absorbed by the positive exponential in Nmax. No loop runs without either a fixed bound, StepCap, or consumption under a source/demand cap. Failed attempts release their storage; unused arena allocation is still counted.

Total allocation has logarithm O(r), so the address multiplier is O(r). Adding source call tariffs (n+1)Q yields the native simultaneous ledger

 T=O(n^7 Nmax), SC=O(n^2 2^w), SQ=O(n), Q=O(n^3 Nmax).             (10.1)

This ledger is not an idealized word-cost or expected-time claim. The capped expectations in Section 6 were used only for success; every bound here is deterministic over branches. Even all-failure branches obey (10.1).

## 11. Literal envelopes and growth indices

Let z=n^(49/100) and x=sqrt n. From r<=x+1, U>=z, U>=Lg>=log2 n, (5.3) and (5.4), with a fixed additive constant C,

 log2(n^7 Nmax)<=alpha*x-(528/5)U+7log2 n+C
                  <=alpha*x-(493/5)U+C<=alpha*x-96z+C,
 log2(n^3 Nmax)<=alpha*x-(528/5)U+3log2 n+C
                  <=alpha*x-(513/5)U+C<=alpha*x-100z+C,
 log2(n^2 2^w)<=(7999/20000)x-48U+2log2 n+C
                  <=(7999/20000)x-46U+C<=(7999/20000)x-40z+C,

where alpha=399319/225000. The constant absorbs r-x<=1, ceiling constants and outer resource constants. It is outside the exponent's growing terms. This proves all four exact objects in submission.json simultaneously with the success guarantee, including their ZERO outside polynomial factors for T,SC,Q. Positive leading n^.5 terms eventually dominate the negative n^.49 corrections. Thus each exponential envelope has log2 log2 B=(1/2)log2 n+O(1), with limit index 1/2. SQ's envelope is n, whose index is zero. These are indices of the displayed envelopes, not lower bounds on optimal DCP complexity.

The fifth object is the expression 0 for malformed-copy tolerance, in the independent ideal-copy model. No positive corruption guarantee or impossibility of robustness is asserted. The theorem and the joint objects rely on the complete physical algorithm and proofs above, not on the diagnostic audit, source scores, previous acceptance, or a numerical search. The very large finite threshold, unoptimized absolute constants, and clean-input restriction are explicit limitations. This improves a particular resource tradeoff and does not achieve growth index 1/3.
