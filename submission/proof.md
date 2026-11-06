# HS2: doubled-cap collimation with minimum-distance stride decoding

HS2 combines the fully derived HS1 stride construction (immutable local commit
573b5e331fe708e1bf29b05b488642f936149042) with the actual published doubled-cap
source 15f1d1c3-0ec1-45a3-92ea-f99fcefaef49, commit93a79cadf4c3270174860053caa4dd0530a63f27.
The latter's complete proof is included verbatim as cs1-base-proof.md,
SHA2562615b7a4802d9b8e3b529a2d8711c2652c92f13fdaf57b51f57b9f165e02a4c6.
Its internal section references refer to its own numbered sections. HS2 is
specified in this file; its four bounds do not mix configurations. Original
CS1 material also comes directly from published f1481815-9577-4990-abe3-7b79fa5d9284,
commit200ef0387acb280adcd272f4fbcdb805d1786bbe. Both participant sources are
materially acknowledged; accepted reviews are not mathematical premises.

Let n=ceil(log2 N). HS2 outputs every fixed s modulo every N>=2 with
unconditional probability at least 1-2^-8>2/3, and simultaneously has

    T=O(n^4 (log2 n) 2^(sqrt(2n))),
    S_C=O(n^2 2^(sqrt(2n)-2(2n)^(1/4))),
    S_Q=O(n),
    Q=O(n^(3/2) 2^(sqrt(2n))).

Its structured representatives use the SAME rational a=u_333/v_333>sqrt2
specified exactly in cs1-base-proof.md Section0 and the supplied submission.json:

    n^4 (log2 n) 2^(a sqrt n),  2^(a sqrt n-2 n^(1/4)),  n,
    n^(3/2) 2^(a sqrt n).

All four constants are absolute; indices are1/2,1/2,0,1/2. Fifth fraction0
uses exactly the parent's clean-input error-model text. This improves the
parent's full time by a logarithmic factor and its source envelope by a
logarithmic factor. The shared time index1/2 alone is not the improvement.
No cube-root time or new leading exponential constant is claimed.

## 1. Complete configuration and finite branch

If n<65536, run the included doubled-cap CS1-C2 algorithm in cs1-base-proof.md without
changes, including its n<64 exhaustive branch. This is a fixed finite set
of bit lengths, absorbed by absolute outer constants in every bound above.
Its unconditional success is at least1-2^-8. The finite branch is explicit;
it is not an asymptotic premise about the new algorithm.

For n>=65536 compute N=2^a2 M with M odd, d=floor(log2 N), and all CS1 tree
parameters exactly as in its Sections7 and11. Every call to LE, TREE_D,
MERGE, Mult_alpha and Shift_c retains its specified implementation. Define

    H=floor(sqrt(n)/16),
    ellH=floor(log2 H),
    Delta=floor(ellH/2)-1.

Compute H by integer square root followed by integer division by16, and
ellH by bitlength. H>=16, Delta>=1, and

    2^(Delta+3)<=4sqrt(H).                                        (1.1)

Let nq=nq_d=2^m(kappa+1) and keep the same root count per odd-part stage,

    K=2^13(ceil(log2 nq)+ceil(log2 n)+30).

If M=1 skip the odd-part section, set s1=0 and R=0. Otherwise define R as
the least integer R>=1 with

    2^(R Delta+3)>2M.

It is computed by an explicitly bounded integer loop, R<=n. The odd-part
stages are t=0,...,R-1 with j=t Delta. At each stage use exactly CS1's
source multiplier alpha_j, accepted-label filter k<2^d, TREE_d and random
X/Y root measurement to obtain K triples (W_i,beta_i,Z_i). Use EVERY root;
there is no Hamming-distance computation, selection test, rejection rule,
stored incidence vector or extra acquisition.

The grid and score are the same as CS1 Section9:

    P_j=j+ceil(log2 nq)+8,
    zeta=c/2^P_j,
    score(c)=sum_i Z_i tab_(beta_i)((2^j W_i c mod2^P_j)/2^P_j).

At t=0 enumerate the whole grid on the circle. At t>=1 enumerate the grid
points within circular distance rad_j=2^(-j-3) of the previous center.
Use the same direct integer-interval enumeration, running residues and
least-maximizer tie rule as CS1. Both arc endpoints are on the grid:
P_j increases by Delta from the preceding stage and P_j>=j+3. Return the
least maximizing center z_t. After the last stage set s1=round(M z_(R-1))
modulo M. The intended success invariant, proved below, is

    dist_circle(theta,z_t)<2^(-j-Delta-3), theta=s1_true/M.           (1.2)

Run CS1 Section10 unchanged to recover the 2-adic part from s1. Output its
same CRT result. The 2-adic section retains its source shifts and parity
retries exactly; no minimum-distance promise is needed in that section.

## 1A. Re-derived doubled-cap schedule compatibility

Every tree with B=D-1 uses exactly the following included-parent parameters:

    mu=ceil(sqrt(2B))+2, kappa=ceil(log2 mu)+1,
    s=min(floor(sqrt(4mu)),mu-1),
    m=min{m>=s+1: m(m+1)/2-s(s-1)/2+kappa>=B}.

Its lam_i and bmax_i formulas are those in included Section7. For all B>=1,
mu>=4, 1<=s<=mu-1 and s<=2sqrt(mu). Since z(z-1)/2 increases for z>=1,

    s(s-1)/2<=2mu-sqrt(mu).

The extra headroom has the exact identity

    mu(mu+1)/2=(mu-2)^2/2+5mu/2-2.

As mu-2>=sqrt(2B), it follows that

    mu(mu+1)/2-s(s-1)/2>=B+mu/2+sqrt(mu)-2>=B.

Thus m exists and s+1<=m<=mu. With t=m-s>=1, the total bmax capacity is

    t(t-1)/2+(s-1)(t+1)+kappa+2t+1
      =m(m+1)/2-s(s-1)/2+kappa>=B.

Greedy nonnegative allocation still gives sum_i b_i=B and p_m=B. At growing,
capped and root levels respectively, direct substitution gives exactly the
same local failure margin

    b_i+lam_(i+1)-2lam_i<=-kappa.

Since 2^kappa>=2mu>=2m, each merge failure bound remains<=1/(2m), and its
retry inflation over the entire tree is at most e<3 exactly as in the
included Lemma11.1. All output entries still have distinct binary incidence
vectors: the merge instrument and its bijective reindexing have not changed.
All decisions still read label bits strictly below B. The new length cap
therefore changes neither the low-bit nature of G nor the held-out-top-bit
factorization used in Sections3-4. These are structural facts about the
same instrument, not imported independent assumptions about two algorithms.

Uniformly for B<=n, mu<=sqrt(2n)+3 and 2^m<=8*2^(sqrt(2n)). This is only a
fixed outside-factor change to all tree-work and leaf-count estimates. The
new K and Q_Hcap are computed from these actual larger-depth parameters,
not copied from HS1. Section3 re-derives the conservative pool bound with
32 in place of31, retaining log2 A<=4sqrt n at n>=65536.

For memory define s(x)=min(floor(2sqrt x),x-1) for integers x>=4. Each of
floor(2sqrt x) and x-1 grows by at most1 per unit step, so x-s(x) is
nondecreasing. At MU=ceil(sqrt(2n))+2 and n>=64, MU>=14 and
s(MU)=floor(2sqrt MU)>=2sqrt MU-1. Therefore

    m-s<=MU-s(MU)<=sqrt(2n)+4-2(2n)^(1/4).

The deterministic stack and scratch estimates in the included proof then
establish S_C=O(n^2 2^(sqrt(2n)-2(2n)^(1/4))) and S_Q=O(n) on every branch.
There is no larger root-record allocation from the HS2 decoder: K remains
O(sqrt n), the candidate grid/counters have O(n)-bit entries, and R is
smaller than the unit-stride stage count. Consequently all polynomial
decoder/LE scratch is absorbed in this classical envelope.

To pass to the exact supported classical representative, the logarithm of
its ratio is at most

    2log2 n-2(2^(1/4)-1)n^(1/4),

apart from a nonpositive contribution from a>sqrt2. This tends to minus
infinity. For example 2(2^(1/4)-1)>0.378 and, for n>=2^36,
0.378 n^(1/4)>=2log2 n; the quotient n^(1/4)/log2 n is increasing there.
This proves the stated 2^(a sqrt n-2n^(1/4)) envelope without guessing any
inner coefficient. Smaller bit lengths only change an absolute outer constant.

## 2. Caps and coupling: no unbounded favorable branch

Let MU,KAP be the doubled-cap parent parameters mu,kappa at B=n. Replace its Section11 source
budgets by

    Q_H*=6*(2^MU)*(KAP+1)(R K+2a2)+2a2,
    Q_Hcap=1024 Q_H*.

Here MU and KAP name those two integers; 2^MU is a literal integer power. Define LE's h_e,h_A,t_V and high-confidence-run cap Cf from this
Q_Hcap exactly as in parent Section5. Before exceeding Q_Hcap acquisitions,
abort with output0, as in CS1. The fallback-run counter aborts as specified
there. All source copies, including rejected ones and failed tree inputs,
are charged and capped literally. All other fixed-width allocations and
fixed decoder loops are unchanged except for the displayed stage count.

The uncapped ideal process replaces every LE output by the true latent label
and removes both caps. Each successful tree has the same conditional merge
success and expected source bound as parent Lemma11.1. Replacing the number
of odd stages by R gives E[acquisitions]<=Q_H*. The bound on the two-adic
part remains valid even if the odd answer is wrong, as noted in parent
Section10. Markov therefore bounds reaching the source cap by1/1024.
The high-confidence-counter and wrong-LE-output bounds from parent
Lemmas5.1,5.2 and Section5.6 retain exactly their hypotheses and give total
coupling discrepancy below2^-11+2^-20. In particular high-confidence
extraction is not required to succeed on every branch: its incorrect outputs
and its explicit cap are already charged in this coupling.

## 3. A low-bit event forcing root distance

This lemma is about the ideal process; it introduces no physical table,
preparation, randomness or oracle.

For odd-part leaves, CS1's exact data transform makes rho_(alpha_j s), and
its latent label is uniform on Z/NZ for every alpha_j and s. Conditional on
acceptance k<2^d, the label is uniform on [0,2^d). Successive accepted labels
are independent of all earlier history: each comes from a fresh independent
copy, and each fixed/adaptively chosen unit transform preserves the uniform
label law. Conditioning on the accepted interval preserves that law. We
may therefore couple the successive accepted labels used by all odd-part
stages to an independent sequence L_1,L_2,... uniform on [0,2^d).
Writing B=d-1, their low B bits l_i and top bits tau_i are mutually
independent, with l_i uniform modulo2^B and tau_i fair. No algorithm obtains
or conditions on this analytic latent sequence as a side channel.

Use as an ANALYSIS POOL bound the larger unit-stride doubled-cap parent cap A=Q_C2cap,
computed from that parent's original stage count J+1 at this same N. The new R<=J+1:
R is the least positive integer with2^(R Delta+3)>2M and Delta>=1.
Thus Q_Hcap<=A. In any source-capped execution, the total number of accepted
odd-part leaves is at most A. It suffices to consider the first A accepted
labels of the infinite analytic sequence, including its unused extension.
Unused labels are analytic random variables, not acquired copies.

Let G be the event that no nonzero signed sum of fewer than H distinct
pool coordinates vanishes modulo2^B. It depends ONLY on the l_i, never on
tau_i. For a fixed support of size h>=1 and fixed coefficients in{+1,-1},
condition on all but one low label. The remaining coefficient is a unit
modulo2^B, so this sum is uniform; its zero probability is exactly2^-B.
A union bound gives

    Pr[not G]<=2^-B sum_(h=1)^(H-1) binom(A,h)2^h
             <=H(2A)^H 2^-B.                                    (3.1)

Explicit size bound. For n>=64, the original parent cap satisfies

    A<=2^29 2^MU n^3,
    log2 A<=sqrt(2n)+3log2 n+32.

Indeed MU<=sqrt(2n)+3, KAP+1<=n, J+1<=n, a2<=n, and
ceil(log2 nq)<=MU+KAP+1. Hence K<=2^15 n, and inserting these into the
parent's literal Q*,Qcap gives the displayed conservative bound. For
n>=65536, put x=sqrt(n)>=256. The elementary inequality
log2 n<=sqrt(n)/2 holds for n>=256: with y=sqrt n>=16, y-4log2 y is zero
at16 and increasing because log_e2>1/2. Since sqrt2<3/2 and32<=x/8,
log2 A<4x. Also B=d-1>=n-2, H<=x/16, and log2 H<=log2 x. The binary
logarithm of(3.1) is consequently at most

    -3x^2/4+x/16+log2 x+2 <=-x^2/2=-n/2.                        (3.2)

For the last inequality subtract -x^2/2. The resulting function is
f(x)=-x^2/4+x/16+log2 x+2; f(256)=-16358, and its derivative is
-x/2+1/16+1/(x log_e2)<0 for x>=256 (bound the last term by2/x).
Therefore Pr[not G]<=2^(-n/2).

Root incidence. Every entry of every successful phase vector has a binary
incidence vector indicating which acquired leaf labels are summed to make
its label. At a leaf this is its bit-string index. Merging concatenates
incidence vectors on disjoint acquired copies, and the rank/reindex map is
a bijection on the retained pairs. Thus different entries retain distinct
incidence vectors through every successful merge, including after retries.
A returned root's two labels are equal modulo2^B. Their difference is a
nonzero signed sum whose support size is their incidence Hamming distance
hd. If all its coordinates lie in the first A pool entries, G implies

    hd>=H.                                                       (3.3)

No incidence vector or G test is computed by HS2. All counting here is a
union bound over possibilities, not an uncharged subset-sum subroutine.

## 4. Held-out bits, adaptive conditioning and the score gap

It is essential that G is a low-bit event. Apply the parent Section8
factorization to the entire odd-part pool: conditional on all its low bits,
all merge computational-basis outcomes and construction decisions have laws
independent of the held-out top bits. This follows node by node because
MERGE measures only functions of label sums below bit B on equal-magnitude
superpositions. Reindexing, sorting and remainder decisions also read only
those low bits and index order. Adding multiples of2^B does not change any
such decision. Retries use fresh disjoint coordinates. Conditioning further
on G therefore leaves all current uninspected top bits independent fair.

To apply this statement on a finite capped execution without conditioning
on an unknown favorable output, first consider the uncapped ideal odd-part
process. Its number of stages R and roots per stage K are fixed. Its source
consumption, retries and merge outcomes depend on accepted low labels,
construction randomness and the acceptance waiting counts, not on root X/Y
outcomes or the top bits of accepted labels. Conditional on an accepted label
being in [0,2^d), it is uniform there independently of the waiting count and
discarded-label values; this is the usual independent-trials factorization
for a fixed interval filter, applied at each fresh source acquisition. (The stage transformations depend on j,N, not on the decoder
center.) Thus the event that its odd part fits the source cap is also a
low-bit/construction event. On that event every odd root uses only pool
coordinates<=A, and(3.3) holds on G. Conditional on those low labels and
construction outcomes, earlier root measurements and decoder centers may
be exposed in order. Distinct roots use disjoint top bits; a current root's
still-uninspected top bits remain fair independently of that earlier
measurement history. This is the same parent factorization with additional
LOW-BIT conditioning; it does not condition on LE's internal acceptance
verdicts in the actual process. Actual/ideal LE differences are covered
separately by Section2's coupling.

In this conditional law, write the current root frequency multiplier as

    W=c+sum_(v in Sp) tau_v-sum_(v in Sm) tau_v,

with Sp,Sm fixed by the conditioned incidence vectors and
|Sp|+|Sm|=hd>=H. The parent characteristic identity therefore becomes

    |E exp(2pi i phi W)|=|cos(pi phi)|^hd<=|cos(pi phi)|^H.         (4.1)

For |phi|<=1/2, sin(pi|phi|)>=2|phi| by sine concavity. Hence
cos^2(pi phi)<=1-4phi^2<=exp(-4phi^2), and

    |cos(pi phi)|^H<=exp(-2H phi^2).                              (4.2)

The rest of the score argument is quantitative and independent of the
particular conditioned low labels.

Stage invariant. Assume the incoming candidate arc contains theta; there
is no condition at stage0. Its grid endpoints are candidates. Its nearest
grid point zeta0 is within2^(-P_j-1) of theta. Since |W|<2nq, the expected
ideal randomized-basis score of this point is at least
(1/2)cos(pi/128), exactly as in parent Lemma9.1.

A point is now far if its distance from theta is at least2^(-j-Delta-3).
At stage0 circular distance is at most1/2. Later both it and theta lie in
the incoming radius2^(-j-3), so their distance is at most2^(-j-2).
Thus the scaled difference phi=2^j(theta-zeta) obeys

    1/(4sqrt H)<=2^(-Delta-3)<=|phi|<=1/2.

By(4.1)-(4.2), its expected ideal score is at most(1/2)exp(-1/8)<=4/9.
The gap exceeds the parent concentration/table allowances:

    (1/2)(1-(22/(7*128))^2/2-8/9)-(2/64+2/625)
       =94628687/4515840000>0.                                  (4.3)

Here cos(pi/128)>=1-(pi/128)^2/2, pi<22/7, and exp(1/8)>=1+1/8
are elementary analytic bounds. The parent's rational trig table has error
<1/625, and its K/64 martingale deviations therefore still strictly
separate a near point from every far point.

The candidate set at a stage is fixed by earlier stages. Conditional on
that history and the low/construction data above, the score's centered
increments obey the same bounded martingale hypothesis as parent Lemma9.1.
There are at most2^(ceil(log2 nq)+9) relevant events, even using the original
larger candidate-count bound. With the same K, Azuma-Hoeffding therefore
bounds bad maximization by2^-20/n per stage. The bound holds for EVERY
conditioned low/construction realization satisfying G and fitting the odd
source cap, so it integrates without assuming independence of G and the
decoder. If the previous stage's target error holds, it equals the incoming
radius at the next j because j increases by Delta. Induction proves(1.2).
The last stage has R Delta+3>log2(2M), so its error is <1/(2M), and rounding
returns the exact s modulo M.

## 5. Unconditional success

There are R<=n odd stages. On G and if the source cap is not reached in
its odd part, the preceding conditional argument gives total odd decoding
failure at most2^-20. On successful odd decoding, the unchanged ideal
2-adic decoder is exact. The global source cap, LE-coupling discrepancy,
high-confidence abort, and low-distance bad event are all counted by an
additive union bound, without assuming they are independent:

    failure<=2^-20+2^-10+2^-11+2^-20+2^(-n/2)<2^-8.

The finite branch has the original >=1-2^-8 guarantee. All statements are
for each fixed secret and each modulus. There is no postselection on a
successful tree, accepted label, high-distance event, cap, or approximate
label estimator. Successful retries consume source copies and all failed
work is included in the literal resource cap.

## 6. Joint branchwise resources and exact structured comparison

The stride Delta is Theta(log n) for large n, since
H=floor(sqrt n/16)=Theta(sqrt n). Thus R=O(n/log n), K=O(sqrt n), and
KAP+1=O(log n), while2^MU=O(2^(sqrt(2n))). Therefore

    Q_Hcap=O(n^(3/2) 2^(sqrt(2n)) + n log n 2^(sqrt(2n)))
          =O(n^(3/2) 2^(sqrt(2n))).                              (6.1)

All acquisitions are bounded by that cap on EVERY branch. The original
LE implementation and fallback counter still require O(n^2 log n) core
steps per capped acquisition, amortized on every branch. Leaf and merge
charging is unchanged. The decoder has fewer stages and no extra work
besides O(log n)-bit stride/counter arithmetic. Its direct grid loops cost
at most the original O(n^(5/2)nq) core bound, which is already smaller than
the new acquisition term. All setup/CRT/parameter computations are
polynomial. Hence total core steps are

    O(n^2 log n) Q_Hcap + O(n^(5/2)nq)+poly(n)
       =O(n^(7/2) log n 2^(sqrt(2n))).                            (6.2)

The same deterministic allocations of CS1 Sections6-7 and13 apply to all
trees. The decoder stores no more triples/candidates than before. H and
Delta are scalar parameters; no analytic pool, incidence vectors, G predicate,
subset-sum table or pair-distance certificate is ever stored. Thus

    S_C=O(n^2 2^(sqrt(2n)-2(2n)^(1/4))), S_Q=O(n).

All classical accesses and classically addressed gates still pay
ceil(log2(S_C+S_Q+2))=O(sqrt n); no locality or QRAM discount is taken.
Charging this factor to(6.2), together with(n+1) per acquisition, gives
T=O(n^4 log n 2^(sqrt(2n))). This holds even on every abort/wrong-label branch,
because fixed allocations, fixed decoder limits and the two literal counters
give the same charging independently of mathematical success.

The parent's exact rational a>sqrt2 is retained, including its full rational
JSON coefficient. The same parent argument absorbs the displayed n^2 factor
and larger negative fourth-root term in S_C into
2^(a sqrt n-2 n^(1/4)). The other representatives are directly larger
upper envelopes. Their indices remain1/2,1/2,0,1/2 by the original double-log
calculation; no unknown inner constant is guessed.

Under exactly the same normalized context and error-model text, HS2 has the
same full time, qubit and sample representatives as HS1 but a strictly smaller
classical-space exponent, -2n^(1/4) instead of -n^(1/4). Thus it is an exact
supported-vector improvement over HS1 if both are accepted as written.
Compared with the doubled-cap parent15f1d1c3, it retains that parent's classical
and quantum envelopes while reducing time logPower2->1 and samples
logPower1->0. Exact equal vectors retain earliest submission time thenID;
sorting and equal coarse indices do not establish membership. Fresh current
frontier comparison remains the central sender's responsibility.

## 7. Fraction, primary provenance and checks

The fifth expression is0. Every acquired copy must be an independent ideal
rho_s. This clean promise supports all four joint bounds and success above;
it asserts neither positive robustness nor impossibility of robustness.
Its error-model text is the parent's exact submitted text, preserved in JSON.

Material published sources are full UUID f1481815-9577-4990-abe3-7b79fa5d9284,
commit200ef0387acb280adcd272f4fbcdb805d1786bbe, for the source instrument,
linear merge, original tree and free-frequency construction; and full UUID
15f1d1c3-0ec1-45a3-92ea-f99fcefaef49, commit93a79cadf4c3270174860053caa4dd0530a63f27,
for the actual doubled-cap schedule. The latter exact proof is included as
cs1-base-proof.md with its full hash at the beginning. The stride proof was
first written in immutable local HS1 commit573b5e331fe708e1bf29b05b488642f936149042;
if that candidate is published first, its full submission UUID must also be
declared by the central sender. The exact headroom/instrument/cap compatibility
is re-derived in Section1A; no accepted verdict substitutes for it.

The primary collimation source is Kuperberg, arXiv:1112.3333v1, Algorithm4.1,
Proposition4.2, Corollary4.3 and Section4.6,
https://arxiv.org/pdf/1112.3333 . Its distribution-free trimming and counted
linear-access implementation are distinguished from the heuristic leading
constant in Section4.5. The actual growing-schedule leading coefficient used
here is proved in the included CS1 construction, not imported as a theorem
from Kuperberg's heuristic section. The latent eigenlabel/controlled-shift
method is in the tradition of Kitaev, arXiv:quant-ph/9511026v1 Section3,
https://arxiv.org/pdf/quant-ph/9511026 ; the exact needed controlled modular
powers, rational decoding and failure budget are given in the included proof.
No hiding-function oracle, source inverse/control, purification or free QFT
is assumed. The concentration/counting arguments added here are reproduced.

Wolfram remote symbolic checks verified the displayed rational gap, derivative
certificate and conditional time-expression ratio, with code, assumptions and
output retained as development artifacts. Those calculations do not establish
adaptive independence, quantum correctness or a hosted score. Cheap format
checks are likewise not certification. Hosted acceptance is fallible mathematical
review, not a formal proof. No paid local judge or measured local score is claimed.
