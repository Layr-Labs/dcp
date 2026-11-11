# RPF: bounded four-list measurement with binary witness reuse

## 0. One algorithm, promise and joint theorem

For N>=2 write n=ceil(log2N), u=n+2, Q=3*2^40(n+32), q=Q/2, n0=2^20. ONE program below has unconditional full-secret success>=2/3 and simultaneous bounds
 T=O(2^(7n/16)n^(671/2)), S_C=O(n²), S_Q=O(2^(n/4)n^120),
 EXACT original acquisitions Q=3*2^40(n+32)=O(n).
Time/quantum indices are1; classical/sample indices0. Every branch is capped, including failure/unused originals, and all bit operations, gates, addresses, generation, initialization and memory count.

The literal malformed fraction is1/32: an adversary fixes B, |B|<=floor(Q/32), possibly depending onN,s. The joint state, with arbitrary inaccessible reference, has reduced state rho_s tensor(Q-|B|) on all other positions; bad systems may be arbitrarily entangled/correlated subject to that marginal. Mixtures over fixed B follow by linearity. No source control, preparation inverse or purification is available.

Acquire EXACTLY Q originals on every branch. Preprocess/split/score as1–2. If n<n0 run8. Otherwise m=4ceil((n+64ceil(log2u))/4), r=m/4, L=2^r, Pcap=nextpow2(Lu^100), K=nextpow2(u^200), Kk=nextpow2(m+1), H=L*Kk*K. Run6–7 with the preimage word3–5. nextpow2 is computed by integer bit lengths. These are fixed choices for all five claims, not separately optimized configurations.

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

## 3. Exact bounded four-list oracle and weighted cap loss

For selected W define f(b)=sum W_jb_j modN, c_y=|f^-1(y)|. Four r-variable groups yield four length-L lists of UNREDUCED integer sums and subset IDs. Search X=(h,k,j) in[0,L)*[0,Kk)*[0,K), power-of-two sizeH. TargetT=y+kN. Join first two lists on low-r sumh, last two on low-r sumT-h, each capacityPcap; then join pair records on exact full integer sumT, capacityK. Reject the WHOLE branch on any overflow, k>m or j outside final count. Sort final solutions by fullb to define canonical rankj. Native3 implements duplicate joins by fixed padded sorting/scan words; quantum rank requests use FULL K-slot scans. Every input, including malicious W, has finite bounded behavior.

A surviving b determines uniquely h=its first-pair residue, k=(sum W_jb_j-y)/N and canonicalj. Conversely every marked tuple gives a validb. Distinct subset IDs are never deduplicated when sums coincide. Let c'_y count these marked tuples. This exact Boolean predicate defines the phase oracle by compute/phase/literal-uncompute. F(b) recomputes that same bounded list and returns its unique(h,k,j), or0 if absent.

Here are INPUT-weighted cap bounds, without conditioning on a target/hash. Fix b and average IID uniform W. For any different paira, its sum difference fromb has a +/-1 coefficient. Conditioning all other labels, congruence0 modL has probability<=ceil(N/L)/N<=2/L (N>=L). Thus expected size of b's actual pair bucket<=2L+1; each pair cap loses <=3u^-100 of uniform(W,b) mass by Markov. For the full modular target, distinct b' differences similarly give exactly1/N, hence
 E c_(f(b))=1+(2^m-1)/N<=1+2^68u^64.
Exclude entire heavy targets c_y>K; their input mass<=u^-200+2^68u^-136. On remaining targets no final local cap can overflow and c'_y<=K. If D'_W is the surviving input set, ell=1-|D'_W|/2^m obeys
 E ell<=6u^-100+u^-200+2^68u^-136.                  (3.1)
Heavy columns are discarded ONLY in analysis; the actual bounded circuit may behave arbitrarily there. This is not a uniform-y guarantee.

## 4. Clean uniform-preimage column

Use exact G=(2|u_H><u_H|-I)(I-2P_mark). Its relevant eigenvalues are exp(+/-2i theta), theta=asin(sqrt(c'_y/H)). Include its diffusion scalar minus sign under every control. For nonheavy y, c'_y<=K. Apply coherent native2 phase probing toG with
 t=ceil((log2H+log2K)/2)+10, h=ceil(2^30(n+t+1)).
Each G^(2^j) is GENUINELY2^j repeated oracle words. Final phase error<=2^-t/32 exceptdelta. Hsin²(pi*phase), evaluated to count error1/32, rounds to exactc'_y: additional phase error is bounded by2pi sqrt(HK)|d|+pi²H d²<1/32. Both eigenphases decode to SAME count. Conditional eigenstate probes are independent; their orthogonality proves the coherent correctness bound for their initial uniform-state superposition. All raw probes/history remain quantum.

For count computationU, copy its output then apply literalU^dag. Correct-copy sector is U^dag Pi_c U|0>, overlap with|0> equal to the REAL NONNEGATIVE probability>=1-delta. Its full output differs from |0>|c> by <=2sqrt(delta). Count and output-search workspaces are separate.

With c>=1 compute j within2 of(pi/4)sqrt(H/c) by native2 finite division/root. Fixed loop Jmax=2^(ceil(log2H/2)+2)=O(sqrtH) applies G under counter<j; charge all inactive controlled words. Reverse each active flag immediately, then uncompute j(c) withc UNCHANGED, BEFORE count erasure. Since p=c/H<=K/H=1/(LKk), sqrtp is tiny. Put z=sqrtp<=1/4. Since z<=asin(z)<=z+z^3 and |j-pi/(4z)|<2, the amplification angle error is between -3z and 5z+(pi/2)z^2+5z^3<6z. Hence its absolute value is<=6z<=3/2<pi/2, giving POSITIVE marked amplitude and column distance<=6z<16sqrtp. The finite pi approximation plus floor-root gives error<2, without a one-sided rounding assumption; the existing16sqrtp allowance is unchanged. Set j=0 for c=0.

KeepX unchanged while computing its solver output, copying b into fresh B, assigning the SINGLE failure tag NOT(valid tuple), then reversing solver work. Now computeF(B), XOR it intoX, and reverse that temporary work while B is unchanged. Marked branches haveX=0,tag=0,helpers0; unmarked branches keep tag1 even ifdummyb erasesX. Truec=0 already makes every tuple invalid: do NOT toggle the same tag a second time. Finally reverse the separate clean-count-copy word. Replacing count by its ideal deterministic value before/after the exact search incurs at most another2sqrt(delta), independent of the number of intervening gates.

This defines an actual finite unitary U_y, read-only on W,y, whose clean column is within e=8sqrt(delta)+16sqrt(K/H) of |mu'_y>|0_aux> on c'_y>0 nonheavy columns. mu'_y is uniform over survivors. Zero-count intended columns have tag1 and no success overlap. Dirty/heavy behavior is the literal unitary extension with the same caps. No unknown-source inverse occurs.

## 5. PGM completeness using column accuracy only

Good phase input is2^-m/2 sum_b omega^(s f(b))|b>. Compute f intoY, apply U_y^dag toB/fresh workspace, and COHERENTLY require B/all preimage auxiliaries0. W,Y are excluded from that test. Ideal zero-auxiliary frequency vector is2^-m/2 sum_y sqrt(c'_y)omega^(sy)|y>. Coherent known-ADD readout from native2 returns s (negate its decoded eigenlabel); retainY and all probe bits through acceptance. Different frequency eigenstates remain orthogonal, so per-eigenstate errordelta introduces NO factorN. There is no intermediate postselection/measurement inV.

Collision counting gives E sum_y(c_y/2^m-1/N)²=(1-1/N)2^-m, so expected L1 deviation<=sqrt(N/2^m)<=u^-32. Ideal correct amplitude alpha=sum sqrt(c_y)/sqrt(N2^m)>=1-L1/2; ideal mean failure<=u^-32. Removing input fractionell loses amplitude<=sqrt(ell), by Cauchy and(sqrt c-sqrt c')²<=c-c'. Column error changes the zero-auxiliary vector by <=e: distinctY blocks are orthogonal and their input squared norms sum to1. Arbitrary heavy columns add norm<=sqrt(ell). Thus mean decoder failure<=
 u^-32+4sqrt(6u^-100+u^-200+2^68u^-136)+2e+delta <2^-20.  (5.1)
At n0 the first term<=2^-640 and all other displayed terms are smaller; elementary monotone bounds hold thereafter. This uses the adjoint of ONE prepared column, not an unjustified whole-unitary approximation.

## 6. Actual verifier and unconditional good-label event

Coherently choose an ordered m-subset of witnessD by Fisher–Yates range draws, d_sel=ceil(log2(4m)) trials each. Keep ALL fair raw coins. Validity>=3/4; conditional validity gives EXACT uniform ordered subsets. Copy classical labels to a quantum buffer; quantum-selected phase/label swaps use full q-position scans. All coin/buffer/scan work is polynomial. Raw coins remain orthogonal through acceptance, making the clean acceptance effect a positive average over subsets.

On the split event m/q<=1/1024; each successive all-good draw has probability>=1-33/1024-m/q>=24/25. Sampler-valid all-good weightw>=(24/25)^m/2. Define B as the normalized all-good valid DECODER-ONLY effect requiring true candidates andPGM-zero flag, with0<=B<=I. It does not consult score data. On the score-uniqueness event, the physical marker equals that true-candidate predicate for EVERY witness, so the actual acceptance effect A>=wB. No such inequality is used off that event.

V is the coherent selector/routing, decoder4–5 and exact score marker2, with dedicated untouched score scratch. AcceptC only on selector-valid/PGM-zero/candidate<N/score. All V operations are known finite Clifford+T words; there are NO internal measurements. For clean ancillary inputs on the score event, every accepted vector has candidate=s for arbitrary D/reference.

Given ALL good hidden labels, selected good phases are pure products factoring from the rest; B ignores unselected/bad phases. Its mean completeness is(5.1) over the UNCONDITIONAL IID good-label marginal, irrespective of bad reports. Markov gives an event, failure<=1/1024, on which Tr(rho B)>=1-1/1024. Do not obtain it by conditioning labels on score/bad reports/prior survival. Intersect it with split/score events by union bound; source-label distance is charged once.

## 7. Binary witness-preserving rewinding, exact safety

D comprises ALL original witness phase wires at fixed locations, A all other mutableV wires initially0. P=I_D tensor|0_A><0_A|; immutable data are spectators. Qv=V^dag C V, Av=P Qv P onRangeP. On the score event Av>=p0B, p0=2^(-ceil(m/16)-1), since25^16<2*24^16. InitialP excludes ALL witnessD; the DIFFERENT internalPGM-zero flag includes selectedB and excludes W,Y.

For E=1_(Av<c p0), Av>=p0B implies EBE<=cE. IfTr rho B>=1-epsilon, then
 ||E rho^(1/2)||_HS <=||E B^(1/2)rho^(1/2)||_HS+||(I-B^(1/2))rho^(1/2)||_HS <=sqrt c+sqrt epsilon.
Indeed||E B^(1/2)||²=||EBE||<=c and(1-sqrt b)²<=1-b. Atc=epsilon=1/1024 low-eigenvalue mass<=1/256, without assuming Av,B commute.

Initial binaryQv test: applyV, measure ONLYC; stop/output candidate ifaccepted, else literalV^dag. Then at most t=2^(ceil(m/16)+16) cycles: binaryP test followed by the sameQv test. The P apparatus computes SINGLE all-zero(A) flag, measures ONLY that flag, then reverses its whole Boolean computation. On either Boolean eigenspace it clears exactly0 and is reusable. Never measure/reset individual A wires or reprepareD.

In a Jordan block use P=diag(1,0), Qv=[[lambda,sqrt(lambda(1-lambda))],[sqrt(lambda(1-lambda)),1-lambda]]. Initial vector(1,0) accepts with probabilitylambda. On Qv failure the normalized direction is q_perp=(sqrt(1-lambda),-sqrt(lambda)). A BINARY P measurement, forgetting only its one-bit outcome, gives density diag(1-lambda,lambda). Its Qv acceptance probability is2lambda(1-lambda); each Qv failure returns the same q_perp direction in this block. Thus no source or witness reinitialization is assumed. Tensor arbitrary reference identities and sum block weights; cross-block terms have zero trace under these block-preserving operations. Following failure, eachP-then-Qv cycle succeeds2lambda(1-lambda); survival=(1-lambda)(1-2lambda(1-lambda))^t. Forlambda>=a=p0/1024 this is<=max(exp(-at),1/(et)): below1/2 use2lambda(1-lambda)>=lambda; above1/2 putz=1-lambda, use2lambda z>=z andz exp(-zt)<=1/(et). Atat=32 residual<1/65536. Initial low mass plus high residual bound conditionalfailure<=1/256+1/65536. Degenerate0/1 blocks obey the limits.

Dirty safety: S=RangeP+Range(QvP) is invariant underP,Qv and their complements, becauseP S subsetRangeP andQv S subsetRange(QvP). Initial state is inRangeP; every reachableQv acceptance lies inRange(QvP). AfterV it lies inRange(VQvP)=Range(CVP), where clean-input score soundness forces ENTIREcandidate=s. Tensor arbitrary reference identities throughout. V need not be sound on globally arbitrary dirty states. Fine-grained A measurement would break this invariant and is not used.

At timeout output0. Union split<1/1024, score<2^-40, good-label<1/1024, each of the two range-procedure aborts<=2^-40 and global label distance<2^-40. Together with conditional failure above this gives success>0.99, hence>=2/3. All originals were already acquired; all cycles/costs are capped.

## 8. Finite fallback, same acquisitions/noise

For n<n0 use the SAMEQ/split/score; discard unused witnesses with full charge. On its events the score marker has exactly one solution inH0=2^n. Do16 independent trials: uniform classicalj in[0,J), J=2^(ceil(n/2)+2); initialize a fresh uniform candidate register, perform j exactGrover words for the marker, measure/check the candidate classically and return firstpassing. No new source copy is acquired.

For theta=asin(1/sqrtH0), mean trialsuccess is
 (1/J)sum_j sin²((2j+1)theta)=1/2-sin(4Jtheta)/(4Jsin2theta)>=1/2-1/(16sqrt2)>2/5,
usingJ>=4sqrtH0, sin2theta>=sqrt(2/H0). Failure<=(3/5)^16<1/1024, independently across fresh trial coins/search initializations on fixed score data. Same source/split/score union gives success>=2/3. WorkO(2^(n/2)poly(n)), spacepolynomial, exactQ. The finite setn<n0 has a finite maximum ratio to the declared envelopes, absorbed into an outside constant independent ofN,s,outcomes. No faster exponential rate is asserted on that finite prefix.

## 9. Joint whole ledger and exact degrees

For n>=n0, log2u<=n/512 (integer check at n0, then decreasinglog2(x+2)/x), so m<=2n, N>=L, u^100<=L. Also L<=2^17*2^(n/4)*u^16. All record/count/offset/index widths areO(n). Native3 networks have fixed lengthS=O(Lu^100+u^200)=O(Ln^100), O(Sn²) comparisons/scans and conservativelyO(n²) reversible gates/saved bits per recordoperation. HenceO(Ln^104) gates/qubits per bounded solver. Native4 streams addresses/gates with amortizedO(n²) classical work INCLUDING fullindexedfees; one oracle's TOTAL workO(Ln^106).

H=O(Ln^201), K=O(n^200); largest genuineGrover powerO(sqrt(HK))=O(sqrtL*n^(401/2)). O(n) probe repeats and geometric power summation giveO(sqrtL*n^(403/2)) oracle calls. The whole preimage column and inverse costO(L^(3/2)n^(615/2)); itsO(sqrtH) outputsearch, inverseindex, score/selector/readout, sourcepolynomial work and binaryzeroapparatus fitbelow. Initialization is charged. All parallelwork is summed.

Peak qubitsO(Ln^104) include ALL saved decisions/scans, constantmany separate count/output solver regions, polynomialsource/basis/probe/coin/arithmetic fields, inactivepadding and a binary apparatus linear in mutableV qubits. Compute-phase-uncompute clears each oracle's history for EVERY searchstate; it is reused, not multiplied by the number of calls. Thus S_Q=O(2^(n/4)n^120). Classical dataQ O(n)-bit records plus generatedconstants, inputs/outputs and generator/counters takeO(n²); no exponentialclassical list/circuit word is stored. M=allallocatedbits+qubits haslogM=O(n), and each genuinelyindexed classicalread/gate pays thatfullfee. Quantum-chosen access is always explicit scan/sort.

At mostO(2^(m/16)) verifier/inverse/binarytestcalls occur, giving
 T=O(2^(7m/16)n^(615/2))=O(2^(7n/16)n^(671/2)),
as64log2u addsu^28. SourceQ(n+1), preprocessing, failedbranches, generation, cleanup and every reservation are included. All Q originals are acquired even on abort/fallback; no restart changesQ. The finiteprefix argument8 completes allN jointbounds.

## 10. Scope, credit and provenance

Four-list/PGM circuits and all quantified native lemmas are complete in this archive; tests/verdicts are not premises. The standard tools credited in0, comparison networks/prefix scans/schoolbook arithmetic and two-projector decomposition are not claimed invented. Related Helm–MayPQCrypto2020 subset-sum tradeoffs supply no assumedpreimage oracle. Earlier published source9fd0fa0e joint/RQ methods are rederived here, not substituted by its acceptance. Earlier operational failures and receipt IDs are disclosed in the public note. This proof repair makes the generic rounding error<2 and the explicit binary Jordan-block calculation unambiguous, preserving the SAME actual binary-cycle word/parameters/resource bounds. It needs its OWN fresh atomic review; no earlier verdict is rebound.
