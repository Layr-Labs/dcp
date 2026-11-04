# RR9: four SUM levels and a sharper global-reject rescue

This is the actual RR9 stage and complete quota/resource proof. It retains
the exact adaptive source framework, bounded gradient preparation and one
hard global sampler, but replaces PS7's two-pass population handling. Every
claimed state law below is an exact conditional instrument, not a numerical
model or independence assumption about correlated population counts.

## 1. Primary populations, including the formerly discarded state

At a stage decompose an independent uniform label
u=r0+2^a(v+M*h0), with v uniform in[0,M), M an even power of two>=4.
Bucket by(r0,h0), pair consecutive original positions, and leave at most one
unmatched input per bucket. Given the bucket vector, all middle values are
independent. Write f0=A*(r0+2^a*M*h0), A'=A2^a and H=M/2.

CNOT/target measurement on a primary pair is fair on every label and secret.
A SUM leaves q_(2f0+A'(v1+v2)); a difference, after its known-sign X,
leaves q_(A'd), d=|v1-v2|. These follow from the two amplitudes
[1,exp(2pi i*s*(f1+f2)/N)] or
[exp(2pi i*s*f2/N),exp(2pi i*s*f1/N)]. All frequency sums use the actualN.

Flatten primary differences as before: keep zero, reject d>=H, and otherwise
keep with probability M/[2(M-d)]. The kept categoryK has probability1/4 and
the uniform label/qubit ensemble on[0,H). SUM categoryS has probability1/2
and normalized triangular countT(j)/M^2, whereT(j)=j+1 up toM-1 and2M-1-j
thereafter, with phaseq_(2f0+A'j).

NOW retain, rather than discard, rejected primary differences as categoryV.
It has probability1/4. Its normalized frequency is q_(A'd), with NO bucket
offset. The integer label distribution is W_H(d)/H^2 on[0,2H), where

    W_H(0)=0,
    W_H(d)=H-d, 1<=d<H,
    W_H(d)=2H-d, H<=d<2H.                       (1.1)

To derive it, the unconditional difference weight at positive d is
(M-d)/M^2. BelowH subtract the primary-kept weight1/(2M); at/aboveH subtract
nothing. Normalize the remaining total1/4 to obtain(1.1). At zero the whole
weight was kept, soW_H(0)=0. The weights sumH^2 exactly by the two triangular
sums. No primary reject is asserted uniform.

Disjoint primary inputs imply independent category flags with probabilities
(1/4,1/2,1/4), and product conditional states. Given ALL categories, primary
kept labels are independent uniform, SUM labels independent triangular, and
V labels independent with law(1.1); these populations are mutually independent
at the STATE level. Their counts are multinomial and NOT independent.
The ideal rational samplers are integrated over their trial histories here;
no conditioning on a physical cap or individual trial length is used.

## 2. Second SUM pass and its exact triangular rescue

Pair all first-pass SUM states within the same bucket by original-primary-pair
position, never sum value. Their common offset is2f0. A second CNOT difference
cancels it, leavingq_(A'd), d=|sum1-sum2|. Let

    C_d=sum_j T(j)T(j+d)
       =(2M^3+M)/3-Md^2+(d^3-d)/2, 0<=d<=M.     (2.1)

The identity follows by splitting the triangle correlation into its three
quadratic ranges and summing i andi^2; the exact expansion is reproduced in
the primary/pooled foundation. More explicitly the products are
(j+1)(j+d+1), (j+1)(2M-1-j-d), and
(2M-1-j)(2M-1-j-d), with breaksM-1-d,M-1. The standard finite sum formulas
follow by successive differences and require no counting oracle.

The absolute-difference counts areC0 at zero and2C_d at positive d, out ofM^4.
For0<=d<M/2, C_d decreases andC_(M/2)=23M^3/48+M/12>=C0/2;
C_d-C_(d+1)=M(2d+1)-(3/2)d(d+1)>0. Thus the coinC0/(2C_d) is valid.
Keep zero, reject d>=H and otherwise use that coin. The conditional kept
ensemble is uniform[0,H), with probability

    p2=C0/(4M^3)=1/6+1/(12M^2)>=1/6.           (2.2)

Discard rejected second-pass differences; only PRIMARY rejected differences
are recycled by Section4. Retain second-pass SUM outcomes for another pass.
Each has probability1/2 independent of its input labels and normalized count
T4=T*T, the distribution of a sum of FOUR uniform middle values. Its common
frequency offset is4f0, with label range[0,4M-4]. Conditional on all first and
second categories these states are independent T4 ensembles and independent
of kept primary/second outputs and the primaryV population. At most one
unpaired SUM at each same-bucket pooling step is discarded and charged.

## 3. Third SUM pass with a proved order-eight count kernel

Pair second-pass SUM states within each bucket in original generation order.
CNOT difference cancels their common4f0; after sign correction its frequency
isA'd, where d is the absolute difference of two T4 labels. Define
E_d=sum_j T4(j)T4(j+d). A completely specified exact formula is

    E_d=sum_(j=0)^8 (-1)^j binom(8,j)
          *binom(4(M-1)+d-jM+7,7),             (3.1)

where the last binomial is zero when its upper argument<7. To prove it,
replace each of four subtracted uniform values by M-1 minus that value.
The signed difference count becomes the coefficient of
(1+x+...+x^(M-1))^8 at4(M-1)+d. Use
(1-x^M)^8/(1-x)^8 and the weak-composition countbinom(t+7,7).
Thus(3.1) is finite integer arithmetic with nine terms, not a subset-sum oracle.

At zero the exact central polynomial is

    E0=(151M^7+70M^5+49M^3+45M)/315.            (3.2)

Indeed binom(y+3,7)=(y^7-14y^5+49y^3-36y)/5040. In(3.1) atd=0,
the nonzero terms y=4M,3M,2M,M have weights1,-8,28,-56. Their combined
coefficients are2416M^7+1120M^5+784M^3+720M over5040, yielding(3.2).
In particular E0>=151M^7/315>13M^7/32.

We prove2E_d>=E0 for every0<=d<=H without a Gaussian approximation. Extend
finite sequences by zero. For nonnegativef, weighted Cauchy followed by
summing overx gives

    ||f*g||_2^2 <= ||f||_1^2 ||g||_2^2.

Apply this to f=T and g=shift_dT-T. SinceT4=T*T and||T||_1=M^2,

    E0-E_d=(1/2)||shift_dT4-T4||_2^2
       <=M^4(C0-C_d)
       <=3M^7/16+M^5/4 <=13M^7/64 <=E0/2.      (3.3)

The middle inequality uses(2.1)'s decrease throughH, and the last usesM>=4
and(3.2). The weighted Cauchy step is elementary:
( sum_y f(y)g(x-y) )^2<=sum_y f(y)*sum_y f(y)g(x-y)^2;
sumx and interchange finite sums. No unproved convolution theorem is needed.

Absolute differences have countsE0 at zero and2E_d at positive d, out ofM^8.
Keep zero, reject d>=H, and otherwise keep with probabilityE0/(2E_d), valid
by(3.3). The retained ensemble is uniform[0,H) with correctq_(A'd), and

    p3=E0/(4M^7)>=gamma=151/1260.              (3.4)

Discard all failed tertiary differences and retain third-pass SUMs for
the fourth pass below. These counts use O(n)-bit words (degree seven),
computed by the explicit charged adaptive arithmetic and exact division by
fixed factorials. A call to a unit-cost binomial or count routine is not assumed.


### 3a. Fourth SUM pass: an exact order-sixteen kernel

Third-pass SUM states have middle count T8=T4*T4, the sum of eight
independent uniforms, and common offset8f0 within each original bucket.
Pair them within bucket in original generation order. Their difference
cancels the offset and has correlation

    B_d=sum_(j=0)^16 (-1)^j binom(16,j)
        *binom(8(M-1)+d-jM+15,15),

with binomial zero if its upper argument<15. The same coefficient argument
as(3.1) proves this formula. Its central polynomial, by expanding the eight
nonzero fixed-factor binomials, is

 B0=M*(2330931341M^14+1122261140M^12+810231422M^10
       +649783420M^8+547079533M^6+474040840M^4
       +422422704M^2+454053600)/6810804000 > M^15/3.

Every coefficient is positive. We prove B_d>=B0/2 for0<=d<=H.
For any finite sequencef, shift_d f-f is the sum of d shifted adjacent
differences. Cauchy and translation invariance give
||shift_d f-f||_2²<=d²||shift_1 f-f||_2².
Use f=T8=T4*T4 and the weighted Cauchy convolution inequality(3.3).
Since ||T4||_1=M^4, and direct subtraction in(3.1) gives
E0-E1=(M^5+M^3+M)/3, we obtain

 B0-B_d<=d²(B0-B1)<=d² M^8(E0-E1)
       <=(M^15+M^13+M^11)/12
       <=(1+1/16+1/256)M^15/12 < M^15/6 < B0/2.

Here M>=4 and d<=M/2; all bounds are universal, not Gaussian estimates.
Keep zero, reject d>=H, and for positive d use B0/(2B_d). Exactly as before,
the kept ensemble is uniform[0,H),q_(A'd), with success probability

    p4=B0/(4M^15)>=delta=2330931341/27243216000 >1/16.

Discard fourth SUM outcomes, unpaired entries, and rejected fourth differences.
There are exactly FOUR SUM-chain CNOT levels in RR9. The17 constant-degree
fifteen binomial terms use fifteen-factor integer products and exact fixed
factorial division. Their word sizes are O(n); no counting oracle is assumed.

## 4. Global primary-reject pooling and a sharper exact success law

PrimaryV states have frequencyq_(A'd) with offset ZERO for every original
bucket. They may therefore be pooled globally within this stage by original
primary-pair position, not by d or across different stages/targets. Pair them
and apply CNOT difference/sign correction. Their middle distribution isW_H/H^2.
Let J_delta=sum_x W_H(x)W_H(x+delta). For0<=delta<H,

    J0=(2H^3+H)/3,
    J_delta=J0-H^2 delta+(H/2)delta^2+(H/2)delta
                       +(delta^3-delta)/6.     (4.1)

Here is an exact expansion. LetU(v)=H-v on[0,H), zero elsewhere;
W_H=U+shift_H U-H*delta_0. The same-block term is
B_delta=sum_(j=delta+1)^H j(j-delta), and the crossing term is
sum_(j=1)^delta j(H-delta+j). Combining2B_delta, the crossing term and
-H(H-delta) yields(4.1); at zero the result is
2sum_(j=1)^H j^2-H^2=(2H^3+H)/3. Expand by the elementary finite sums.

Forx=delta/H in[0,1], the cubic part of(4.1) is H^3 f(x), with
f(x)=2/3-x+x^2/2+x^3/6. It is convex there and has its minimum atsqrt3-1,
where f=2-sqrt3>v=267949/1000000, since
1732051²=3000000666601>3*10^12. The remaining terms
H/3+H*delta/2-delta/6 are nonnegative. Thus J_delta>=vH³ and
J0>=(2/3)H³>2vH³. This sharpens RR8's conservative quarter bound.

Reject delta>=H. At zero use coin2vH³/J0; at positive delta use
coinvH³/J_delta. Clear the fixed rational denominator10^6 to obtain integer
numerator/denominator. ZERO IS NOT ALWAYS KEPT. Both coins are<=1 by the
proved bounds. Absolute difference counts areJ0 at zero and2J_delta at
positive delta, out ofH^4, and the CNOT difference probability is1/2.
Consequently every retained label has probabilityv/H, total success EXACTLYv.
The retained ensemble is the same uniform[0,H),q_(A'd). All cubic arithmetic,
fair draws, failed/zero-label coins and discards are charged.

## 5. Full conditional product law, ordering and allocations

For every retained label in any pass, all erased histories yield exactly the
same densityQ_(A'd); scalars are only global phases. Kept-primary states,
first/second/third SUM populations, and primaryV populations use disjoint original
pairs after conditioning on their categories. The second/third/fourth SUM pair
assignment depends only on categories and same-bucket positions; the V pair
assignment uses categories/global original positions after offset cancellation.
Thus the inputs of each new conditional channel are independent with the
specified triangular/T4/W laws. Applying the exact instruments above proves
inductively that, conditional on ALL category/keep flags, every kept label
and phase state has the uniform PRODUCT ensemble. This is a statement about
states, not an assertion that population COUNTS at different levels are
independent.

Output in fixed order: primary successes, second-SUM rescues, third-SUM
rescues, fourth-SUM rescues, then global-V rescues; within each use the original generation order
and bucket order where required. Checking availability and retaining a fixed
prefix therefore preserves the uniform product law for the next stage.
No label-value sorting or postselection is used. Ideal rational samplers are
analyzed without conditioning on trial counts/no cap; the physical cutoff is
transferred additively in Section8.

Each CNOT consumes two phase inputs and leaves at most one, with no quantum
copying. Primary kept/SUM/V buffers together have at most the primary-pair
count, and every subsequent pass reduces or discards that population. Total
outputs are at most the primary-pair count<=I/2; quantum peak is O(I) plus
counted source/arithmetic scratch. Classical labels for sums of eight have
O(n) bits and count kernels have at most degree-fifteen O(n)-bit intermediates.
All buffers and current local program/pointer records are included.

## 6. Exact configuration and a certified coefficient

For n<=16 use the same exhaustive branch. For n>=17, m=floor(log2 N),
h=n+1, set q=599/100, r=51651/20000, epsilon=2^-20,

 ell=min{a>=1:a+sum_(j=0)^(a-1)floor(r*j)>=m-1}, J=m-1-ell,
 lambda=clog(1024h), M_meas=8192lambda, F=2^68lambda,
 L_i=ceil(F599^(ell-i)/100^(ell-i)), R=4(J+1)L0,
 global_coin_trial_limit=4R.

clog(x) is the bit length of x-1. All capacities, ceilings,
widths, targets and source caps are generated exactly as in proof.md.
The width identity guarantees M>=4, final A=2^j,B=2 and A*B<=N.
All frequency operations use the actual arbitrary modulusN.

Here is a finite rational certificate for r<log2q<w=2582557/1000000.
Let l=2sum_(j=0)^15 1/((2j+1)3^(2j+1)),
u_l=l+18/(8*33*3^33). The integrated geometric series gives
l<ln2<u_l. For0<=x<41 define
P(x)=sum_(j=0)^39 x^j/j!, U(x)=P(x)+x^40/[40!(1-x/41)].
The positive exponential series and term-ratio bound give P(x)<=exp(x)<=U(x).
The explicit rational comparisons U(r*u_l)<599/100<P(w*l) certify both
log bounds. They can be checked by clearing positive factorial/power
 denominators and repeated integer products; the current evidence program
reproduces precisely these comparisons. All series lengths are fixed.
No floating logarithm or unknown exponent constant is a proof premise.

Capacity>=r(ell²-ell)/2, hence ell<=sqrt(2n/r)+2
<=(880017/1000000)sqrt n+2; the final inequality is the exact integer
comparison880017²*51651>2*10^12*20000. Capacity<3ell² gives
ell=Theta(sqrt n). Thus

 L0=O(log2 n*2^(c sqrt n)),
 c=(880017/1000000)*(2582557/1000000)
  =2272694063469/1000000000000=2.272694063469.

F is deliberately a huge explicit finite constant, not a practical claim.

## 7. Nine conditional count events and actual quotas

Fix the stage bucket vector; letI=L_i,K=2^b_i<=q^(t-1),t=ell-i.
Primary pair countP1>=(I-K)/2 has multinomialD1,Z1,V with separate
Bin(P1,1/4),Bin(P1,1/2),Bin(P1,1/4) marginals.
LetP2>=(Z1-K)/2,P3>=(Z2-K)/2,P4>=(Z3-K)/2 and
P_V=floor(V/2)>=(V-K)/2. Conditional on each complete earlier category
vector, D2~Bin(P2,p2>=1/6), Z2~Bin(P2,1/2),
D3~Bin(P3,p3>=gamma=151/1260), Z3~Bin(P3,1/2),
D4~Bin(P4,p4>=delta), D_V~Bin(P_V,v).
These counts are correlated; no unconditional independence is asserted.

Putz=1-epsilon. The nine good events are
D1>=zP1/4,Z1>=zP1/2,V>=zP1/4,D2>=zP2/6,Z2>=zP2/2,
D3>=z gamma P3,Z3>=zP3/2,D4>=z delta P4,D_V>=zvP_V.
On these, substitution givesY=D1+D2+D3+D4+D_V>=aP1-bK, where

 a=z/4+z²/24+gamma z³/16+delta z⁴/64+v z²/8,
 b=z/12+gamma z²/8+gamma z/2+delta z³/32+delta z²/8
       +delta z/2+v z/2.

At epsilonzero,
 theta=a0/2=1/8+1/48+gamma/32+delta/128+v/16
      =72791093701609/435891456000000,
 a0/2+b0=224637116653981/435891456000000<1.
The elementary(1-epsilon)^j>=1-j epsilon givesa/2>theta-epsilon.
Since all coefficients decrease withz, a/2+b<1. Thus the conservative
bound isY>=(theta-epsilon)I-K. It is NOT the olderK/2 bound.
The exact rational comparisonq(theta-epsilon)-1>1/4096 follows by common
denominators. WithG=Fq^(t-1), I>=qG,K<=G/F andF>=8192,
Y>(1+1/4096-1/F)G>=G+1>=ceil(G), the actual nextquota.

On the requisite earlier good events P1>=G,P2>=G/16,P3>=G/256,
P4>=G/4096,P_V>=G/32. Induction usingz>=1/2,K<=G/F,F>=2^16
proves these conservative bounds. Elementary Chernoff gives the nine
failure exponents at least
 epsilon²P1/8,epsilon²P1/4,epsilon²P1/8,
 epsilon²P2/12,epsilon²P2/4,
 epsilon²gamma P3/2,epsilon²P3/4,
 epsilon²delta P4/2,epsilon²v P_V/2.
Every term>=G/2^60, sincegamma>1/16,delta>1/16,v>1/4.
F=2^68lambda implies each<=exp(-256lambda)<exp(-16lambda).
Use uniform conditional bounds and union, not independence of the counts.
Stage shortage<=9exp(-16lambda). Initial qualification and final label-one
shortages have their unchangedexp(-L0/4),exp(-F/16) bounds andF/M_meas=2^55.
The total across batches and stages is<=9h(h+2)exp(-16lambda)<1/1024.
The exact conditional product law above justifies the next stage after
availability and fixed-prefix selection. Outer estimates only use available
batches; aborted branches are not assigned successful estimates.

## 8. Hard sampler cutoff, total success and all acquired copies

Every exact coin numerator<=its positive O(n)-bit denominator. Use the
retained fresh fair-bit rejection sampler; conditional completion is>=1/2.
The special global-V zero coin is included. Primary calls<=P1-Z1,
secondary<=P2-Z2,tertiary<=P3-Z3,fourth<=P4,globalV<=P_V.
WithP2<=Z1/2,P3<=Z2/2,P4<=Z3/2,P_V<=V/2<=P1/2,
totalcalls<=3P1/2<=3I/4 on EVERY branch. Sinceq>5,
sum_i L_i<2L0, so across all batches fewer than(3/2)(J+1)L0<R coins
are requested. The original adaptive Bernoulli/ideal-sampler coupling still
gives global4R-trial-cap abort<=exp(-R/4)<1/1024. No conditioning on no cap
or on a trial history is used to assert uniform labels. All failed draws,
zero coins, counters, measurements, discards and resets count.

The five error budgets (whole-computation source/gradient comparison,
global cap, shortages, outer phase and fresh verification) remain each<=1/1024.
Therefore unconditional full-secret success>=1019/1024 for everyN,s.
The trace-distance comparison is not an observable good-gradient event.
Every loop/allocation/source-call/trial ceiling is fixed on all outcomes.
Source copies<=N(n+10) for n<=16 and
4(J+1)L0+(n+10)(2^ell+2) otherwise, including every abort/discard/failedtest.
Recycling acquires no further copies. The tolerance remains exactlyzero
under the canonical independent ideal-source error model, with no positive
robustness or impossibility assertion.

## 9. Complete joint resource envelopes

C_d,J_d,E_d,B_d use constant-degree<=15 exact integer arithmetic,
including seventeen binomial terms with fifteen factors and fixed factorial
division. The explicit adaptive integer algorithm costs
O(n*2^(20sqrt(log2 n))) logical work per record/pair. Full O(A_addr²)=O(n)
charges, sum_i L_i<2L0 andO(n) targets give total ordinary work
O(n³L0*2^(20sqrt(log2 n))). The4R O(n)-bit sampler trials costO(n³L0).
Exact source extraction costsO(n³L0*2^(21sqrt(log2 n))) and dominates.
All constants, matrices, quotas, local compiled program/pointer records,
initialization, address generation, failures and verification are included.
No unit-cost integer, count, binomial, arbitrary rotation or oracle is used.

All five output populations and live intermediate buffers together useO(L0)
qubits andO(nL0) classical label/wire records: every CNOT consumes two
inputs and leaves at mostone; additional passes reduce their own disjoint
populations, with no copying. Local arithmetic/source histories have log
sizeO(logn+sqrt(logn))=o(sqrt n), belowL0. Complete memory is included
before establishing address lengthO(sqrt n). Work is sequential.
Forc=2272694063469/1000000000000 the resulting bounds are

 T=O(n³(log2 n)*2^(c sqrt n+21sqrt(log2 n))),
 SC=O(n(log2 n)*2^(c sqrt n)),
 SQ=O((log2 n)*2^(c sqrt n)),
 Q=O(n(log2 n)*2^(c sqrt n)).

Their logarithms arec sqrt n+O(logn), so all exact indices remain1/2.
Finite n=1 is handled separately; these expressions apply forn>=2.
Relative to RR8 all four ratios are2^(-(2286279/1000000-c)sqrt n),
tending tozero in the same success/tolerance context. This improves full
upper guarantees, not the index, cube-root goal, practical timing or optimality.

RR9 directly reuses RR8 submission4e2ca900-70e1-4923-a469-ea5a1bc0e25b,
currently pending hosted review, and the PS7/SG6/PG5/PG4/MDC1/VFD3/FD2
sources explicitly credited in proof.md. Every needed argument is reproduced;
no verdict, pending graph edge, external reference or diagnostic is a premise.
