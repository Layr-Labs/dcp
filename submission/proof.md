# HSR1: minimum-distance stride decoding with ramped collimation budgets

## 0. Complete theorem, configuration, and provenance

Let N>=2, s in Z/NZ, n=ceil(log2 N), and L=max(1,log2 n). The single algorithm HSR1 specified below recovers the entire s with unconditional probability at least1-2^-8>2/3. Its simultaneous EVERY-BRANCH bounds, including failed attempts, discarded copies, restarts and aborts, are

    T   = O(n^4/L * 2^(sqrt(2n))),
    S_C = O(n^2 * 2^(sqrt(2n)-2(2n)^(1/4))),
    S_Q = O(n),
    Q   = O(n^(3/2)/L * 2^(sqrt(2n)-(2n)^(1/4))).                 (0.1)

There is no source purification, inverse, coherent control, QRAM, subset-sum oracle, or postselection. The source is acquired one copy at a time. Its cost, all classical bit operations, gate generation, arithmetic precision, disposal and addressing are included. All constants are absolute, independent of N,s and outcomes.

The accompanying rbs1-base-proof.md is the exact immutable RBS1 proof from commit8685760ba9356c7c87a385aacc6891593cf61e95, SHA256bcf9b03b9b2fadf3b78a82ca3a5f4b03ca752c9aca245971b0f7d8840e8d787b. It specifies all primitive circuits and routines used here. Its Section0 theorem describes RBS1, not HSR1; this document explicitly replaces its odd-part stage schedule, source cap and resulting resource analysis. Every other routine, fixed allocation and finite branch is inherited as specified below. RBS1 is an unpublished source at preparation time; that precise provenance is preserved, and its eventual submission UUID must be added when publication makes a dependency link eligible. No independence is claimed.

The minimum-distance/stride argument is materially reused from our HS2, commit58d646bab4bd075d705c3bec13c2efc7a8b55d54, submitted as8b85be12-4b9c-40e6-a62f-d2d232d62402, publication pending at preparation. Its earlier local HS1 source is573b5e331fe708e1bf29b05b488642f936149042. The original published source is CS1 f1481815-9577-4990-abe3-7b79fa5d9284, proofSHA256e1b698d021f72cc5fd17f0132a2c30ba213dc2c424e613087d711804f074b528 (also published with identical proof as b56c7ceb-de59-42da-9e3b-6ee96e4e4145). The doubled-cap source read for HS2 is15f1d1c3-0ec1-45a3-92ea-f99fcefaef49. The inherited RBS1 provenance additionally names6e91de62-9a4f-4f08-bfa8-1beacca11e0f for its published cap improvement. These are mathematical sources, not correctness certificates.

Use EXACTLY the rational a=u333/v333 from base Section0: (u0,v0)=(10,7), (u(k+1),v(k+1))=(3u(k)+4v(k),2u(k)+3v(k)). The identity u(k)^2-2v(k)^2=2 proves a>sqrt2. No improvement below uses slack between a and sqrt2. The four structured representatives are

    n^4 (log2 n)^(-1) 2^(a sqrt n),
    2^(a sqrt n-2n^(1/4)),
    n,
    n^(3/2) (log2 n)^(-1) 2^(a sqrt n-n^(1/4)).                 (0.2)

These are eventual asymptotic representatives; L gives a well-defined full-domain form at n=1. Exact growth indices are1/2,1/2,0,1/2. Fractional tolerance is0 with the identical clean-input model text in Section8.

## 1. The one algorithm

For n<65536 run RBS1 from the included base proof, including its own n<64 direct branch. This is a fixed finite set of bit lengths, not a missing validity threshold; Section6 proves the uniform extension of the resource bounds.

For n>=65536 compute N=2^a2 M with M odd, d=floor(log2 N), and

    H=floor(sqrt(n)/16), ell=floor(log2 H), Delta=floor(ell/2)-1.

All square roots/logarithms used as integers are computed by exact integer square-root and bit-length operations. Here H>=16 and Delta>=1; Delta=Theta(log n). Retain RBS1 Sections2-8 and10 exactly, with the new cap in Section2. In particular, for TREE_D with B=D-1>=1 use

    u=ceil(sqrt(2B)), v=floor(sqrt u), m=u-v+4,
    sigma=2floor(sqrt m), t=m-sigma, h=ceil(log2 m),
    kappa_i=3+min(i,h), delta_i=min(max(i-1,0),v),
    lambda_i=min(i,t)+kappa_i+2+delta_i (0<=i<m), lambda_m=1,
    bmax_i=2lambda_i-lambda_(i+1)-kappa_i.

Allocate b_i from the root down, b_i=min(bmax_i, remaining B); p_0=0 and p_(i+1)=p_i+b_i. The base proves nonnegative budgets, exact capacity>=B, p_m=B, per-level conditional failure<=2^-kappa_i for ANY tables, and product retry inflation<2. Leaves use exactly5 distinct accepted copies; nq_D=5*2^m. These facts are unchanged because neither the stage multiplier nor the decoder affects a merge's low-bit instrument. Each MERGE consumes its inputs even on failure. Roots and all attempts use disjoint source copies.

If M=1 set s1=0,R=0,K=0 and skip the odd part. Otherwise define nq=nq_d,

    K=2^13(ceil(log2 nq)+ceil(log2 n)+30),
    R=least positive integer with 2^(R Delta+3)>2M.

There are exactly R stages, indexed j=0,Delta,...,(R-1)Delta. For a stage j use the base Section9 unit alpha_j (CRT: alpha_j=1 mod2^a2 and alpha_j=2^j*(2^(d-1-a2))^(-1) modM), the identical source instrument, and exactly K roots TREE_d. Thus root i has known frequency f_i=2^j W_i and |W_i|<2nq, and its X/Y randomized measurement is exactly as in the base. Physical Mult_alpha_j is retained and charged. No new approximate QFT or gate synthesis is used: label extraction consists of exact controlled modular translations and H/S tests as specified in base Section5, including its error coupling and capped high-confidence branch.

At stage j put P_j=j+ceil(log2 nq)+8 and grid c/2^P_j on R/Z. Stage0 examines the whole grid. A later stage examines the one or two explicit grid intervals of circular radius2^(-j-3) around the preceding selected center. Grid endpoints are included: P_j-P_(j-Delta)=Delta, and 2^(-j-3) is an integer multiple of2^-P_j. Use exactly the base rational score table and running-residue score algorithm, and choose the least maximizing c. The set is fixed before that stage's new roots are measured. After stage j its target circular error is

    |theta-z_j|circle <2^(-j-Delta-3), theta=s1/M.               (1.1)

There are at most2^(ceil(log2 nq)+8)+2 candidates per stage, including stage0. At the final stage the target radius is2^(-R Delta-3)<1/(2M); output s1=round(M z_j) modM. Run the unchanged base Section10 to recover s2 and output s=s1+M s2 modN. Its correctness requires the correct s1 and is exact then. Even on erroneous s1 its cost and equal-magnitude/odd-root cost bounds still hold, as proved in base Section11.

## 2. Fixed caps and coupling

Use starred tree parameters from Section1 at B=n, and nq*=5*2^m*. Before the first source call compute

    Qstar=6 nq* (R K+2a2)+2a2,
    Qcap=1024 Qstar.                                           (2.1)

Set the base LE parameters h_e,h_A,t_V and Cf=ceil(Qcap/ceil(sqrt n)) using THIS Qcap. The source down-counter aborts before an acquisition would exceed Qcap; the high-confidence counter aborts before call Cf+1. These are literal cutoffs on all branches, not expected costs.

For the ideal uncapped run, base Lemma11.1 applies without alteration to each root: expected acquisitions<=6nq* uniformly over all earlier history and transformed secret. Its proof uses the distribution-free failure bounds and geometric tails, NOT independence between an attempt's cost and its success. There are exactly RK odd roots and expected at most2a2 roots for the 2-adic part (or2 per direct bit). Therefore expected total acquisitions<=Qstar. Markov bounds the cap event by2^-10. This proof still holds after an erroneous odd decode because construction outcome laws do not depend on the phases; only the phase-bit correctness assertion requires correct earlier bits.

For at most Qcap actual LE calls, base Sections5.5-5.6 prove wrong-label probability<2^-11 and fallback-cap probability<=2^-20. They are valid with the revised Qcap: their inequalities depend only on h_e=ceil(log2(Qcap(n+5)))+14 and the explicit minimum cap. The minimum remains Qcap>=6*1024*nq* whenever any roots are needed. If M=1 then a2>=1, so the same minimum holds. The base lower bound Cf>=20 and its binomial domination still apply. On the complement of those events the actual and ideal capped runs can be coupled to coincide. LE coins, estimates, verification verdicts and fallbacks are NOT conditioned upon in the held-out-bit argument.

## 3. A low-bit-only event for the ramped tree

This section is analysis only: no tape, incidence vector or event test is allocated or enumerated by the algorithm.

For the ideal uncapped odd part, every acquired label transformed by alpha_j is uniform modulo N independently of the previous history. The multiplier is a unit depending only on j,N. Acceptance iff k<2^d gives an i.i.d. tape of accepted labels uniform on[0,2^d), independent of acceptance waiting counts and rejected labels. This includes accepted copies later discarded in failed trees. Write its coordinates

    k_r=L_r+2^B tau_r, B=d-1>=n-2,

where all L_r are independent uniform modulo2^B and all tau_r are independent fair bits, independent of the lows and waiting counts.

Choose an analysis-only deterministic pool length A as the original unit-stride RBS1 conservative cap at B=n:

    Kbar=2^13(ceil(log2 nq*)+ceil(log2 n)+30),
    A=1024[6nq*(n Kbar+2n)+2n].                                (3.1)

R<=n, K<=Kbar, a2<=n, so the actual Qcap<=A. All odd accepted copies in any capped run have tape index<=A. This remains true for every outcome, including retries and early source aborts.

A coarse explicit bound suffices: log2 A<=4sqrt n for n>=65536. Here is a derivation independent of hidden exponent constants. Put x=sqrt n>=256. Since sqrt2<3/2,
 m*<=u*+4<=3x/2+5, log2 nq*<=3x/2+8.
Also ceil(log2 n)<=x/8: log2 n=2log2 x, and 2log2 x+1<=x/8 at x=256 and thereafter by derivatives. Consequently Kbar<=2^13(13x/8+39)<=2^14 x. Using nq*=5*2^m*, nKbar+2n<=2^15 x^3 and the additive2n term gives

    A<=2^(m*+31) x^3,
    log2 A<=3x/2+36+3log2 x<=4x.                               (3.2)

The last difference is positive at256 and increasing since5/2-3/(x ln2)>0. All these relaxations increase A's upper bound.

Let G exclude every nonempty signed relation of fewer than H distinct low labels among the first A tape coordinates:

    sum_(r in S) epsilon_r L_r !=0 mod2^B
    for 1<=|S|<H, epsilon_r in{-1,+1}.

For each fixed support and signs the signed sum is uniform modulo2^B, since one remaining coefficient is a unit +/-1. Thus

    Pr[G^c] <=2^-B sum_(h=1)^(H-1) binom(A,h)2^h
            <=H(2A)^H 2^-B <=2^(-n/2).                        (3.3)

For the last inequality use H<=x/16, B>=x^2-2 and (3.2): after adding n/2 the binary log is at most

    F(x)=-x^2/4+x/16+log2 x+2.

F(256)=-16358<0 and F'(x)=-x/2+1/16+1/(x ln2)<0 for x>=256. No exponential-distance assumption is used.

Every two distinct root entries have distinct binary incidence vectors on their distinct supporting source coordinates, by the base's injective reindexing and concatenation of disjoint supports. Their labels agree modulo2^B, hence their incidence difference is a signed zero relation in the lows. On G, whenever the root's copies lie in the pool,

    hd=|x0 xor x1|>=H.                                         (3.4)

This implication covers ALL possible successful roots and outcomes, not merely a randomly selected favorable pair. It does not assert exponential hd or uniform separation over all histories without G.

## 4. Conditioning, stride geometry, and score separation

Consider the ideal uncapped odd-part process first. Its R,K,stage multipliers and tree schedules are fixed. All tree construction outcomes and decisions depend only on the accepted low labels and construction randomness: MERGE measures functions of label bits below p+b<=B on equal-magnitude superpositions. Adding2^B to a leaf label changes no residue, sorting key, rank, remainder or measurement probability used to select surviving entries. Reading or adding high parts for storage does not select entries. No copy is reused after a failed attempt.

As in base Section8, condition on the pool's low labels and construction data, acceptance waiting counts and discarded labels. The event G and the event that the entire odd part fits Qcap are measurable from this low/construction data and do not depend on retained top bits or X/Y root outcomes. The stage's physical alpha_j depends on j,N, not the decoded center; thus the number of acquired odd copies also has this measurability. On odd-fit every constructed root lies in the first A accepted coordinates. Conditioning further on G and odd-fit therefore retains i.i.d. fair top bits. Exposing earlier roots' X/Y outcomes and earlier decoded centers leaves a current root's top bits fair: the source supports of distinct roots are disjoint. This is an ideal-label coupling argument; it does not condition on actual LE success or its internal verdicts.

For every such low/construction realization satisfying G and odd-fit, each current W has

    W=c+sum_(r in Sp)tau_r-sum_(r in Sm)tau_r,
    |Sp|+|Sm|=hd>=H.

The sets and c are fixed by that low/construction realization. Consequently

    |E exp(2pi i phi W)|=|cos(pi phi)|^hd
                       <=exp(-2H phi^2), |phi|<=1/2.           (4.1)

Indeed sin(pi|phi|)>=2|phi| by concavity on[0,pi/2], so cos^2(pi phi)<=1-4phi^2<=exp(-4phi^2).

Assume the incoming stage arc contains theta (no assumption at stage0). Its nearest grid point zeta0 is within2^(-P_j-1) of theta, since endpoints are included. The base frequency bound |W|<2nq gives |f(theta-zeta0)|<2^-8. The ideal randomized X/Y score contribution xi_i=Z_i cs_beta_i(f_i zeta0) therefore has conditional expectation at least(1/2)cos(pi/128), for every frequency.

A candidate is far if its circular error is at least2^(-j-Delta-3). At stage0 circular distance<=1/2. Later both theta and the candidate lie in the radius2^(-j-3) arc, so their difference has absolute value<=2^(-j-2). With phi=2^j(theta-zeta),

    1/(4sqrt H)<=2^(-Delta-3)<=|phi|<=1/2,                     (4.2)

because 2^(Delta+3)=4*2^floor(ell/2)<=4sqrt H. Combining (4.1) with the fair basis gives every far candidate conditional mean score<= (1/2)e^(-1/8)<=4/9.

The base fixed rational trigonometric table differs from its target by<1/625 per term. Each sum of centered ideal scores has martingale increments in intervals of length2, so the Azuma bound used in base Lemma9.1 gives deviation K/64 with probability<=exp(-K/8192). Both candidate set and near point are fixed conditional on earlier stage outcomes. Union bounding all near/far candidates uses at most2^(ceil(log2 nq)+9) events. Since K=2^13(ceil(log2 nq)+ceil(log2 n)+30), the bad-stage probability is<=2^-20/n.

The margin after both deviations and both table errors is strictly positive:

    (1/2)(1-(22/(7*128))^2/2)-4/9-2/64-2/625
       =94628687/4515840000>0.                                (4.3)

Thus no far point can maximize the computed score outside those events. Its error satisfies (1.1). That output radius is exactly the next stage's incoming radius, because the next j is j+Delta. R<=n stages give total conditional odd decoding failure<=2^-20. The bound is uniform over every conditioned low/construction realization satisfying G and odd-fit, so it integrates without treating G as independent of the decoder. In particular,

    Pr[odd decoder wrong AND G AND odd-fit]<=2^-20.             (4.4)

The terminal radius and exact rounding recover the entire s1. The unchanged 2-adic routine then recovers the remaining bits.

## 5. Unconditional success and all-domain termination

The ideal uncapped total acquisition expectation<=Qstar. The actual execution has fixed source/fallback cutoffs and finite loops, including all wrong-label branches; every non-fixed retry consumes fresh source copies. Therefore it terminates on every branch. By the cap/LE couplings, (3.3), and (4.4),

    Pr[failure] <=2^-10+2^-11+2^-20+2^-20+2^(-n/2)<2^-8

on the main branch. A total-cap fit implies odd-fit, so no further conditional-cap assumption is used. On n<65536 the included RBS1 algorithm has success>=1-2^-8 for every N,s (its n<64 direct branch is even stronger). These give the stated unconditional all-N guarantee. Hosted review or any finite check is not a mathematical premise.

## 6. Joint branchwise resource accounting

Take starred B=n parameters and abbreviate u,v,m. They obey m+v=u+4 and m<=sqrt(2n)-(2n)^(1/4)+6. Also nq*=5*2^m and K=O(sqrt n).

For sufficiently large n, Delta=Theta(log n), and R=O(n/log n) uniformly in M<=N. (When M=1,R=0.) Since a2<=n and log n<=sqrt n eventually, (2.1) gives

    Qcap=O(n^(3/2)/log n *2^m)
         =O(n^(3/2)/log n *2^(sqrt(2n)-(2n)^(1/4))).            (6.1)

This includes all acquired copies, accepted or rejected, discarded trees, failed/restarted attempts, verification fallbacks and cut-off branches. It is a literal cap. No conditioning on G improves a declared resource bound.

Base Lemma11.2's deterministic table accounting survives unchanged: each merge attempt at level i+1 costs O(nm2^v2^i), and its two completed inputs have at least5*2^(i+1) distinct acquisitions. Each acquisition supports at most one attempted merge per level, at most m total, including discarded and partial subtrees. Thus merges cost at most O(nm^2 2^v)Qcap core steps on EVERY actual branch. In particular,

    O(nm^2 2^v)Qcap=O(n^(7/2)/log n *2^(m+v))
                    =O(n^(7/2)/log n *2^(sqrt(2n))).           (6.2)

All LE calls together, including capped high-confidence runs, cost O(n^2 log n)Qcap+O(n^(5/2)). By (6.1) this is O(n^(7/2)2^m)+polynomial, also bounded by (6.2), since log n=O(2^v). The unchanged physical transforms cost O(n^2) per copy and are included. Parameter generation, exact modular arithmetic, CRT, all gate generation, fixed-width lookups, reset/disposal and source-counter operations are charged in these base bounds.

For completeness the strided decoder still fits: O(nq_d) candidates per stage, K=O(sqrt n), R=O(n/log n) stages, and O(n) bit operations per score update give O(n^(5/2)/log n *nq_d) core operations, smaller than (6.2). Even keeping the base's more generous O(n^(5/2)nq_d) bound suffices, since nq_d<=nq* and (log n)/n=O(1). The largest j is<=n+Delta and P_j=O(n), so no arithmetic width changes its order. All loops have explicit fixed lengths.

Classical space is exactly the base ramped-tree allocation envelope: O(n^2 2^(sqrt(2n)-2(2n)^(1/4))) plus polynomial scratch. The largest index width and the depth-first stack remain unchanged; fewer stages store no additional tables. The K score triples/residues fit O(n^(3/2)) bits. The low-bit event and pool are never stored. Quantum peak remains O(n), including the entire simultaneous tree stack, all siblings, arithmetic, LE data and ancillas, and merges on abort branches.

The base explicit classical address convention charges O(sqrt n) bit work per core step, since log2(S_C+S_Q+2)=O(sqrt n). Multiplying ALL core operations by this charge and adding (n+1)Qcap gives T=O(n^4/log n *2^(sqrt(2n))). In particular no unit-cost indexing or controller is assumed. No approximate arbitrary-N QFT is called; all quantum primitives in this configuration are the base exact Clifford+T circuits. Its classical trig approximation and exact integer roundings already enter the success/cost proof, with no uncharged real arithmetic.

All these bounds are eventual inequalities with absolute constants; replacing log n by L extends their formulas to n=1. The finite set n<65536 has finite, explicitly capped costs under RBS1. Taking the maximum of each finite-prefix resource divided by its positive target expression extends a single absolute constant for that resource to every N>=2. Thus this is a full all-N algorithm, not an asymptotic success promise.

## 7. Exact representatives and comparison

Since a>sqrt2, the time and sample representatives in (0.2) follow from (0.1) without absorbing any polynomial using the tiny sqrt-power gap. For classical space use the strict quarter-power gap exactly as in base Section14:

    n^2 2^(sqrt(2n)-2(2n)^(1/4)) /2^(a sqrt n-2n^(1/4))
       <=2^(2log2 n-2(2^(1/4)-1)n^(1/4))=O(1).

Indeed 2^(1/4)-1>189/1000 and n^(1/4)/log2 n tends to infinity. For samples (2n)^(1/4)>=n^(1/4); retain the outside inverse log factor. Each exponential representative has logarithm a sqrt n+O(n^(1/4)+log n+loglog n), so its exact index is1/2. The linear qubit bound has index0. No numeric index improvement or cubic-root algorithm is claimed.

Against the prepared RBS1 vector under IDENTICAL clean error-model text and exact a, the time and sample ratios are both1/log2 n ->0, and both space representatives are identical. Thus these bounds strictly dominate its declared vector if both are established. Against HS2, time improves by1/(log2 n)^2 and samples by2^(-n^(1/4))/log2 n, with the same declared spaces and error model. Compare complete normalized expressions; index ties, sorting order and outer Big-O constants prove no gain by themselves. An even faster newly published full-time envelope would require a fresh comparison before publication.

## 8. Fraction, primary sources, checks, and limitations

Fractional guarantee: epsilon(n)=0, with exact canonical error-model text:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

This means zero malformed acquired copies. It makes no positive robustness or maximal-tolerance claim. ROB-G's adaptive malformed-copy model is a different model and is not incorporated here.

Primary literature consulted: Greg Kuperberg, arXiv:1112.3333v1, 14 Dec2011, Algorithm4.1 and Sections4.2-4.6, https://arxiv.org/html/1112.3333v1 . The rigorous Section4.6 construction imposes simplifying N=2^n, n=m^2 and two-hidden-shift hypotheses; Proposition4.2 uses QRACM. Neither its QRACM cost nor its heuristic sqrt(2n) estimate establishes this theorem. The included base explicitly rederives distribution-free linear-access merges, the complete arbitrary-modulus schedule, retry and source bounds in this model; Sections3-4 above establish the additional low-bit event and stride conditioning. Kitaev, quant-ph/9511026v1, Section3 equations16-19 and Lemmas9-10, https://arxiv.org/pdf/quant-ph/9511026v1 , treats eigenvalue testing of known controlled unitaries and powers. Here the known unitary is modular translation of the supplied register, implemented and charged exactly; source control/inversion is never invoked. The base supplies the finite-precision-free H/S tests and exact rational reconstruction rather than assuming a black-box measurement oracle.

Self-checks: re-derived compatibility of p_m=B, distribution-free merge outcomes, constant retry product, disjoint incidence vectors, accepted-tape uniformity, low-only event and odd-fit conditioning; re-derived revised source/fallback cap and EVERY-BRANCH charge; checked exact rational score margin and elementary pool inequalities. Bounded remote arithmetic and structural admission are supporting checks only, not a proof certificate. No local timing score, executable quantum implementation or formal certification is claimed. All cited base statements needed by the modified configuration are included as evidence, and mathematical correctness remains subject to review.
