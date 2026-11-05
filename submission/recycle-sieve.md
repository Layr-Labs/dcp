# RS7: four SUM passes with a sharper rejected-difference instrument

This is the actual RS7 fifteen-event stage and complete quota proof.
Its source states and reported labels come only from the elementary
repeated-Hadamard extractor in proof.md Section4; schoolbook bit arithmetic
in Section11 implements every classical kernel. One literal global sampler
counts all physical trials. Every state law below is an exact conditional
instrument, not a distributional heuristic or independent-count assumption.

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

Keep third-pass SUM outcomes; discard all failed tertiary differences. RS7 retains these third-pass SUM states for Section 6. The integer counts use O(n)-bit words (degree seven),
computed by the explicit charged schoolbook arithmetic and exact division by
fixed factorials. A call to a unit-cost binomial or count routine is not assumed.

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
where f=2-sqrt3>p=2679/10000 because (17321/10000)^2>3. The remaining terms are
H/3+H*delta/2-delta/6>=0. Thus J_delta>=p H^3, and J0>=2H^3/3>2p H^3, with p=2679/10000.

Reject delta>=H. At delta=0 use coin 2p H^3/J0; at positive delta use
coin p H^3/J_delta. ZERO IS NOT ALWAYS KEPT IN THIS CHANNEL. The numerators
are at most the positive denominators by the preceding bounds. Before the
CNOT, absolute-difference counts areJ0 at zero and2J_delta at positive delta,
out ofH^4. After the difference outcome and this coin, each retained label
has probability exactly p/H. Hence the global-V rescue succeeds with
probability EXACTLY p=2679/10000 and has the same uniform[0,H),q_(A'd) ensemble.
Implement these coins with integer numerators 5358H^3 at zero and
2679H^3 at positive delta, and common denominator 10000J_delta.
All cubic arithmetic, fair draws, failed/zero-label coins and discards count.

## 5. Full conditional product law, ordering and allocations

For every retained label in any pass, all erased histories yield exactly the
same densityQ_(A'd); scalars are only global phases. Kept-primary states,
first/second SUM populations, and primaryV populations use disjoint original
pairs after conditioning on their categories. The second/third SUM pair
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
counted source/arithmetic scratch. Classical labels for sums of four have
O(n) bits and count kernels have fixed-degree (at most27) O(n)-bit intermediates.
All buffers and current local program/pointer records are included.

## 6. Fourth SUM pass and exact deterministic configuration

Keep third-pass SUM outcomes instead of discarding them. Each has probability
1/2, independent of its two input labels. Conditional on all earlier category
flags, these are independent sums of EIGHT original uniform [0,M) labels,
with common frequency offset 8f0 and multiplier A'. Pair them within the
same original bucket, in original generation order. Their difference cancels
8f0 exactly. For an absolute difference d the remaining phase is q_(A'd).
No primary V state or sum from another bucket is mixed into these pairs.

Let F_d be the correlation count of two eight-fold uniform sums. Replacing
each subtracted variable by M-1 minus itself gives the exact integer formula

 F_d = sum_(j=0)^16 (-1)^j binom(16,j)
       binom(8(M-1)+d-jM+15,15).                         (6.1)

The binomial is zero when its upper argument is below 15. Otherwise compute
it by the product of its fifteen consecutive factors divided by 15!.
The formula follows by expanding (1-x^M)^16/(1-x)^16 and counting weak
compositions. It is seventeen constant-degree integer terms, not a count
oracle. All intermediate values have O(n) bits.

Here are exact polynomial certificates for positivity and flattening. Write
H=M/2 (a positive integer). Direct expansion of (6.1) gives

 F_0 = (2386873693184/212837625)H^15
     + (57402368/42525)H^13 + (51803008/212625)H^11
     + (14540608/297675)H^9 + (2186132/212625)H^7
     + (1041848/467775)H^5 + (1066724/2149875)H^3 + (2/15)H.

 2F_H-F_0 = (2021749533234257/217945728000)H^15
     + (1066650359/1555200)H^13 + (837883421/15552000)H^11
     - (138861587/76204800)H^9 - (86478337/31104000)H^7
     - (9170783/8553600)H^5 - (46135813/137592000)H^3 - (7/60)H.

These identities can also be checked by multiplying the fifteen factors in
(6.1): at d=0 only j<8 survive, and at d=H only j<=8 survive. The first
leading coefficient, divided by 2^15, is 2330931341/6810804000 >1/3.
All other central coefficients are positive, so F_0>M^15/3. In the second
polynomial the leading coefficient is >9000 and the absolute sum of all
negative coefficients is <7, by exact rational comparison. For H>=1 each
negative monomial is at most its coefficient times H^15. Thus 2F_H>F_0.

For completeness F_d decreases for d>=0. A sequence symmetric unimodal
about c remains symmetric unimodal after convolution with the uniform
sequence on [0,M): its adjacent difference at x is f(x)-f(x-M), which
is nonnegative up to the new center because x is then no farther from c
than x-M, and is nonpositive after it. This proves the assertion inductively
starting with one uniform sequence. The sixteen-fold convolution is symmetric
about 8(M-1); (6.1) is its value at distance d from that center. Hence for
0<=d<=H, F_d>=F_H>F_0/2.

Fourth-pass absolute differences have counts F_0 at zero and 2F_d at positive
d, out of M^16. Keep zero, reject d>=H, and otherwise use coin F_0/(2F_d).
The ratio is in [0,1] by the preceding proof. Including the fair difference
outcome, every kept d in [0,H) has mass F_0/(2M^16), the SAME conditional
qubit Q_(A'd), and total success

 p4 = F_0/(4M^15) >= gamma4 = 1/12.                       (6.2)

Discard all fourth-pass SUMs and failed fourth differences. Section 5's
product-law induction applies to this extra pass: condition on the third
SUM flags and all earlier categories, then disjoint pairs are independent
with the eight-fold convolution law. Conditioning on their keep flags
leaves independent uniform output-label/qubit ensembles, independent of all
other kept populations. Output in order primary, second, third, FOURTH,
then global primary-V rescue, with original generation/bucket ordering
inside each. Availability and keeping a fixed prefix preserve the uniform
product law. No success probability conditional on revealed labels is used.

The complete configuration is now, for n>=17, m=floor(log2 N), h=n+1,

 q=5847/1000, r=6369/2500, epsilon=2^-20,
 ell=min{v>=1: v+sum_(j=0)^(v-1)floor(r*j)>=m-1}, J=m-1-ell,
 lambda=clog(1024h), M_meas=8192lambda, F=2^62lambda,
 L_i=ceil(F q^(ell-i)), R=4(J+1)L_0, global_trial_limit=4R.

Here clog(z) is the bit length of z-1. Compute exact integer quotas by
ceil(F5847^t/1000^t), and ell by binary search on [1,m-1]. Greedily assign
b_i<=floor(r(ell-i-1)) to total J and split their low/high portions to
sum a_i=j for each target. This is one outcome-independent configuration.
For n<=16 retain the exact n+10-test exhaustive branch from proof.md.
The source repetition count is M_src=8192clog(1024R(n+3)), exactly as
in proof.md Sections1 and4. No reciprocal or shared phase resource is used.

We need r<log2 q<25477/10000. The series
ln 2=2 sum_(j>=0) 1/((2j+1)3^(2j+1)), using its first eight terms and
geometric tail <=9/[4*17*3^17], proves
693147/1000000<ln 2<693148/1000000.
For x=(3-6369/2500)*(693147/1000000), the exact rational inequality
sum_(j=0)^6 x^j/j! > 8/q proves 2^(3-r)>8/q, hence log2 q>r.
For x=(3-25477/10000)*(693148/1000000), the exact rational inequality
sum_(j=0)^6 x^j/j! + x^7/(7!*(1-x/8)) <8/q proves
2^(3-25477/10000)<8/q, hence log2 q<25477/10000. The tail majorant follows
because the ratio of successive terms from degree seven onward is at
most x/8<1. All these finite comparisons are exact integer/rational checks.

Capacity is at least (r/2)(ell^2-ell). A feasible ceiling gives
ell<=sqrt(2n/r)+2 <=(22151/25000)sqrt n+2,
since (6369/2500)*(22151/25000)^2>2 by exact integer comparison.
Capacity is also <3ell^2, so ell>=sqrt((n-2)/3) and ell=Theta(sqrt n).
Consequently

 L_0=O((log2 n)2^(c sqrt n)), c=564341027/250000000,       (6.3)

because (25477/10000)*(22151/25000)=564341027/250000000.
F remains 2^62lambda. No unknown inner O coefficient is inferred.

## 7. Fifteen conditional concentration events and exact quota success

Fix a stage bucket vector, I=L_i, K=2^b_i<=q^(t-1), t=ell-i>=1.
Primary P1>=(I-K)/2 pairs have multinomial category counts D1,Z1,V with
marginals Bin(P1,1/4), Bin(P1,1/2), Bin(P1,1/4). Conditional on complete
earlier categories, let

 P2>=(Z1-K)/2, D2~Bin(P2,p2>=1/6), Z2~Bin(P2,1/2),
 P3>=(Z2-K)/2, D3~Bin(P3,p3>=gamma3=151/1260), Z3~Bin(P3,1/2),
 P4>=(Z3-K)/2, D4~Bin(P4,p4>=1/12),
 PV=floor(V/2)>=(V-K)/2, DV~Bin(PV,p=2679/10000), ZV~Bin(PV,1/2),
 P5=floor(ZV/2)>=(ZV-K)/2, D5~Bin(P5,beta=9/50),
 RV~Bin(PV,eta=2321/10000), P6=floor(RV/2)>=(RV-K)/2,
 D6~Bin(P6,betaR=1/8), ZR~Bin(P6,1/2),
 P7=floor(ZR/2)>=(ZR-K)/2, D7~Bin(P7,beta7=1/5).

Use the FIFTEEN lower events D1>=eP1/4, Z1>=eP1/2, V>=eP1/4,
D2>=eP2/6, Z2>=eP2/2, D3>=e gamma3 P3, Z3>=eP3/2,
D4>=eP4/12, DV>=e p PV, ZV>=e PV/2, D5>=e beta P5, RV>=e eta PV, D6>=e betaR P6, ZR>=eP6/2, D7>=e beta7 P7,
where e=1-epsilon. Sections 10-12 prove the new exact channels. Counts at different levels
are NOT independent; apply the later conditional bounds uniformly over
the preceding good category vectors.

Substitution gives Y=D1+D2+D3+D4+DV+D5+D6+D7>=aP1-bK, with

 a=e/4+e^2/24+gamma3 e^3/16+p e^2/8+(1/12)e^4/64+beta e^3/32+eta betaR e^3/16+eta beta7 e^4/64,
 b=e/12+gamma3(e^2/8+e/2)+p e/2
     +(1/12)(e^3/32+e^2/8+e/2)+beta(e^2/8+e/2)+betaR(eta e^2/4+e/2)+beta7(eta e^3/16+e^2/8+e/2).

Let theta=6661/40320+1/1536+(p-1/4)/16+9/3200+2321/2560000+2321/6400000. At e=1, a/2=theta.
Using e^j>=(1-j epsilon), the loss in a is less than epsilon/2,
since 1/4+2/24+3gamma3/16+2p/8+4/(12*64)+3beta/32+3eta betaR/16+4eta beta7/64<1/2.
Also a/2+b<1 at e=1 and thus at every e in [0,1]. Therefore

 Y>=(theta-epsilon)I-K.                                  (7.1)

The exact rational surplus is
q(theta-epsilon)-1>1/8192, by direct exact rational substitution.
Since I>=Fq^t, K<=q^(t-1), and F>=16384, (7.1) exceeds
Fq^(t-1)+1>=ceil(Fq^(t-1)). Thus the actual next quota, including its
ceiling, is reached on the fifteen events.

Put G=Fq^(t-1). P1>=G since q>5 and F is large. On the preceding good
events, P2>=G/16, P3>=G/256, P4>=G/4096, PV>=G/32, P5>=G/512, P6>=G/512 and P7>=G/4096.
For example e>=1/2 and P2>=eP1/4-K/2>=G/8-G/(2F)>=G/16;
iterate this inequality for P3 and P4. The V case is identical starting
with V>=eP1/4. Finally P5>=ePV/4-K/2>=G/256-G/(2F)>=G/512.
Using e>=3/4 and eta>=1/5 gives
P6>=e eta PV/2-K/2>=3G/1280-G/(2F)>=G/512 for F>=1280.
Then P7>=eP6/4-K/2>=3G/8192-G/(2F)>=G/4096 for F>=4096.
These estimates hold for F>=16384.

For completeness the lower-tail inequality used here follows from
E exp(-tX)<=exp(mu(exp(-t)-1)) for independent Bernoulli sums of mean mu.
Markov with t=-ln(1-delta) gives exponent
-mu[delta+(1-delta)ln(1-delta)]<=-mu delta^2/2, since the bracket minus
delta^2/2 has nonnegative derivative and vanishes at zero. Thus
Pr(X<=(1-delta)mu)<=exp(-mu delta^2/2). This also applies after fixing any
preceding category vector, with its actual conditional independent trials.

For independent Bernoulli sums, the elementary exponential-moment proof of
Chernoff gives failure <=exp(-epsilon^2 mu/2). Thus the fifteen exponents are
at least epsilon^2 times

 P1/8, P1/4, P1/8, P2/12, P2/4,
 gamma3 P3/2, P3/4, P4/24, PV/8, PV/4, beta P5/2, eta PV/2, betaR P6/2, P6/4, beta7 P7/2.

Every exponent is >=G/2^58, because epsilon^2=2^-40,
24*4096<2^17, gamma3/2>1/32 and 512*2/beta<2^13, 32*2/eta<2^9 and 2048*2/betaR=2^15 and 4096*2/beta7<2^16. With F=2^62lambda this is >=16lambda.
A conditional union bound gives stage shortage <=15exp(-16lambda).
Initial qualification shortage is <=exp(-L_0/4); final label-one shortage
is <=exp(-F/16), with F/M_meas=2^49>=8. Across <=h batches, <=h stages
and these endpoint checks the total is <=15h(h+2)exp(-16lambda)<1/1024,
using exp(-x)<=2^-x and 2^lambda>=1024h. No independence between
population counts, cap survival or earlier availability is presumed.
Outer phase-estimation failure remains <1/1024 on available batches.

## 8. Every physical coin, sample and failure branch

There is still one literal limit of 4R sampler trials, including every new
coin, zero-label case and failed draw. Let ZV,RV be SUM/reject categories
of the FIRST global-V pass. Its coin calls are <=PV-ZV; V-SUM rescue calls
are <=ZV/2, and the R rescue and its SUM child have combined calls
<=P6-ZR+P7<=P6<=RV/2. Since RV<=PV-ZV,
these global calls total <=3PV/2. All other primary/SUM passes together
have calls <=P1-Z1+P2-Z2+P3-Z3+P4<=P1. As PV<=V/2<=P1/2,

 total stage coins <=7P1/4<=7I/8.                         (8.1)

This REPLACES the earlier 3I/4 bound. Across sum_i L_i<2L_0 and J+1
targets, calls are fewer than (7/4)(J+1)L_0<R=4(J+1)L_0. No old stronger
coin bound is assumed. All output populations still contain at most P1
states: DV,ZV,RV are disjoint categories and each rescued pair consumes
two states to return at most one. Peak storage changes only by an absolute
buffer factor, with all initialization and release counted.
With q>5, F large and ell<=n, the same geometric/ceiling bound gives
sum_i L_i<2L_0. Every source acquisition limit is unchanged in form.
Each trial completes with conditional probability >=1/2. A fresh-uniform
proof coupling dominates completions by Bin(4R,1/2), so cap-abort is at
most exp(-R/4)<1/1024. This is additive; it does not condition the exact
instrument on no abort. Analyze uncapped ideal coins and couple until the first global budget abort.
If at most R coins have not all completed after 4R trials, there were fewer
than R completions. Every trial's completion indicator, conditional on the
past, has probability at least one half. To see the required domination,
represent that indicator using a fresh independent uniform U with threshold
its conditional completion probability. It is at least the Bernoulli indicator
[U<=1/2]. Additional outcomes can be conditionally sampled with independent
randomness; this is a proof coupling, not a source operation. Extend an already
finished execution with dummy Bernoulli trials if necessary. The number of
completions therefore stochastically dominates Binomial(4R,1/2), of mean 2R.
The elementary Chernoff inequality proved in Section7 gives

    Pr(global trial budget causes an abort)<=exp(-R/4)<1/1024.

The last inequality holds uniformly: L_0>=F, J+1>=1, so R>=4F and
F=2^62*clog(1024(n+1))>=2^62. This comparison is additive. We do not
condition on no abort and assert an unbiased or independent successful
instrument; the ideal exact product law is transferred by the coupling.
The bound replaces, rather than adds to, the original 1/1024 coin budget.
All other shortage, outer-phase and verification budgets are unchanged.
The total failure remains at most 5/1024, preserving success1019/1024.



Ideal-label/uncapped-coin shortages, outer phase estimates and fresh candidate
verification each cost <=1/1024. The physical global cap costs another
1/1024 and the whole source-label implementation another 1/1024.
Consequently the complete program recovers s with probability >=1019/1024
for every N,s. Actual loops and allocations have hard limits on every branch.
The exact acquired-copy bound is unchanged in form:
Q<=N(n+10) for n<=16, and Q<=4(J+1)L_0+(n+10)(2^ell+2) otherwise.
Every acquired/discarded copy and failed attempt counts; new recycling
acquires no sources. All guarantees require independent ideal copies, with
tolerance tau(n,Q)=0 and the identical canonical error-model text.

## 9. All charged resources and comparison

The new R-SUM kernel has14641 fixed numerator products, as proved in
Section12; the F_d kernel has seventeen degree-fifteen terms; K_d has 625 fixed
coefficient/binomial terms as explicitly given in Section 10; calculate the binomials by at most fifteen-factor
products and exact constant-factorial divisions with the schoolbook algorithms in proof.md Section11. Degree and number of terms are ABSOLUTE constants,
so O(n)-bit intermediates and O(n^2) logical work per pair
suffice, as for the older cubic/seventh-degree kernels. No unit-cost binomial,
QRAM or hidden arithmetic oracle is assumed. Full O(A_addr^2)=O(n) address
and generation charges, O(n) targets and sum_i L_i<2L_0 give ordinary
sieve work O(n^4 L_0). The 4R physical trials cost
O(n^3 L_0). Retained elementary source extraction costs
O(n^(9/2) L_0) and dominates both. Initialization, exact
parameters, measurements, resets, bookkeeping and all failures are counted.

All eight output populations together occupy O(L_0) qubits and O(nL_0)
classical label/address bits. A fixed number of pass buffers and O(n)-bit
kernel scratch do not change these peak bounds. Source/arithmetic local
records and program storage are included as in proof.md Section11;
their logarithmic size is o(sqrt n), and the full address width stays O(sqrt n).
There is no retained circuit history or parallel-work discount.

Substitute (6.3). For c=564341027/250000000 the SAME program obeys, on every branch,

 T=O(n^(9/2)(log2 n) 2^(c sqrt n)),
 SC=O(n(log2 n) 2^(c sqrt n)), SQ=O((log2 n) 2^(c sqrt n)),
 Q=O(n(log2 n) 2^(c sqrt n)).

The four exact growth indices are 1/2, since log2 of each envelope is
c sqrt n+O(log n); the iterated log is (1/2)log2 n+log2 c+o(1).
The finite n<=16 program and outside constants do not affect the limit.
The strict full-envelope comparison with RS6S at the same elementary
time polynomial and smaller leading coefficient is proved in proof.md Section12.
It compares upper guarantees, not a lower bound on actual consumption or
an optimality claim. The exact source extractor and every schoolbook
arithmetic cost are now elementary and fully reproduced in proof.md.

## 10. A global SUM rescue of the primary-V channel

Retain, instead of discarding, SUM outcomes from the global primary-V pairs.
Conditional on all earlier categories these outcomes are independent with
probability 1/2 and normalized label law B/H^4, B=W_H*W_H. Their phase
is q_(A'j), with ZERO common offset across all original buckets. Pool only
this one stage/target population globally by original V-pair position.
Pair consecutively, apply CNOT and require difference; sign-correct by X.
The retained phase at absolute difference d is q_(A'd).

Let K_d=sum_x B(x)B(x+d). Here is a completely specified exact evaluator.
Write W(z)=sum W_H(j)z^j. From the two descending ramps and missing zero,

 W(z)=N(z)/(1-z)^2,
 N(z)=(H-1)z-Hz^2+Hz^H-Hz^(H+1)+z^(2H+1),
 Nrev(z)=z^(2H+1)N(z^-1).

Then K_d is the coefficient at 4H-2+d in
N(z)^2 Nrev(z)^2/(1-z)^8. Enumerate the FIVE terms of each factor, their
625 ordered products, and for product c z^e add
c*binom(4H-2+d-e+7,7) when 4H-2+d-e>=0, otherwise zero.
Compute each binomial by seven consecutive factors and exact division by
7!. Signed coefficients, all additions, intermediate values and generation
are counted O(n)-bit arithmetic, with an absolute constant number of terms.
There is no count, subset-sum or quantum lookup oracle.

We prove K_d>=9H^7/50 for all integers H>=2,0<=d<=H and the stronger
zero bound K0>=9H^7/25. The central exact polynomial is

 K0=227H^7/630+2H^6/15+41H^5/90+7H^3/45-2H^2/15+H/35.

Its leading coefficient exceeds9/25 by1/3150. Also
7H^3/45-2H^2/15=H^2(7H-6)/45>=0 for H>=1; every other coefficient is
positive. This proves the zero bound without a numerical approximation.

For the general d, the 625-term expansion on this interval is the polynomial

 K(d)=d^7/1680+H d^6/120
 +d^5(-3H^2/40+H/40-1/120)
 +d^4(-H^3/9+5H^2/24-H/72)
 +d^3(H^4/2-H^3+7H^2/24-H/8+7/240)
 +d^2(-13H^5/30+2H^4/3-7H^3/18+H^2/8-11H/180)
 +d(-H^4/2-13H^2/60+H/10-3/140)+K0.             (10.1)

Here is a finite exact certificate and why the expansion is valid everywhere
claimed. Encode a numerator monomial as c z^(aH+b). A product of the four
numerators contributes a binomial with remainder (4-a)H+d-2-b. Products
with a>=5 have negative remainder for 0<=d<=H and contribute zero. For
products with a<=4, the remainder is always at least -7 for H>=2,d>=0.
The polynomial (remainder+7)...(remainder+1)/7! equals zero at each of
-7,...,-1, so it agrees with the guarded binomial even at the boundary.
Expanding these included products yields (10.1) by finite integer algebra.

Set x=d/H in [0,1], z=H-2>=0. Exact expansion gives

 K(d)-(9/50)H^7 = sum_(k=0)^7 z^k
     sum_(j=0)^7 b_(k,j) binom(7,j)x^j(1-x)^(7-j).         (10.2)

The full rational 8-by-8 coefficient table is the archived evidence file
vsum-bernstein.json, reproduced below in increasing k and j:

1174/25, 326911/7350, 450539/11025, 8903/245, 114206/3675, 182461/7350, 61213/3675, 124/25
25233/175, 676969/4900, 8444059/66150, 1258448/11025, 72623/735, 10727813/132300, 1275653/22050, 8161/350
42844/225, 290638/1575, 1616353/9450, 91967/600, 46841/350, 2124581/18900, 133088/1575, 74167/1800
6331/45, 173629/1260, 53651/420, 2878901/25200, 70139/700, 30901/360, 608/9, 27197/720
2837/45, 19634/315, 435181/7560, 64399/1260, 224/5, 73699/1890, 26869/840, 3583/180
7741/450, 26981/1575, 74128/4725, 19237/1400, 50221/4200, 49738/4725, 113003/12600, 10979/1800
598/225, 598/225, 3781/1575, 463/225, 2467/1400, 2456/1575, 17333/12600, 1819/1800
284/1575, 284/1575, 503/3150, 209/1575, 58/525, 409/4200, 1117/12600, 1759/25200

All 64 displayed coefficients are positive. Each term of (10.2) is
nonnegative, proving the desired inequality for every real H>=2 and
x in[0,1], hence for all required integers. The polynomial identity is
verified either by expanding x^j(1-x)^(7-j), or by the explicit rational
finite identity checks in the diagnostic; it is not an extrapolation from
asymptotic data or a floating root calculation. The certificate is fixed,
independent of N,s and source outcomes, and is fully provided in this proof.
The algorithm does NOT rely on preloaded instance advice: its actual K_d
computation is the uniform counted 625-term evaluator above.

Now set beta=9/50. Reject d>=H. At zero use coin9H^7/(25K0); at positive
d use9H^7/(50K_d). The central and general bounds prove both ratios <=1.
The absolute-difference counts before CNOT are K0 at zero,2K_d at positive
d, out of H^8. Including its fair difference outcome, each retained d<H
has mass beta/H. The channel succeeds exactly beta=9/50 and returns the
same uniform[0,H),q_(A'd) ensemble as all other stage outputs.
Discard this pass's SUMs and failed differences. No further recursion is used.

The conditional product proof follows the existing instrument induction:
condition on earlier categories, then the first V-pass SUM flags. Disjoint
original pairs are independent with the B/H^4 sum law. Pairing depends only
on flags and generation positions. Condition on the new keep flags and
obtain independent uniform output-label/qubit states, independent of the
other retained populations. Erasing old histories preserves the stated
conditional density matrix. Output in order primary, second/third/fourth
SUM rescues, global primary-V rescues, then these new global V-SUM rescues.
Availability and fixed-prefix retention preserve the next-stage invariant.

Every extra pair uses already acquired qubits and no new source. First
V-pass coin calls are <=PV-ZV, where ZV counts its SUMs; the new pass has
at most P5<=ZV/2 coins. Their total is <=PV, exactly the allowance used in
Section 8. This is the allowance for the two earlier global channels alone.
Section 11 adds R-rescue calls, and Section 8 re-establishes the complete
7I/8 coin-call and unchanged 4R physical-trial bounds on EVERY branch. All eight output populations still contain
at most P1 states, since each SUM pair consumes two states and produces at
most one. Constant extra buffers, degree-seven K arithmetic and initialization
fit O(nL_0) classical/O(L_0) quantum and the existing ordinary-sieve envelope.
All failed draws, flags, measurements, resets and address charges count.

## 11. Rescue the FIRST global-V rejected-difference category

Keep the rejected DIFFERENCE category of the FIRST global primary-V pass,
in addition to its kept uniform DV outputs and its SUMs ZV used in Section10.
Do not keep rejected states from any other pass. These three first-pass
categories have probabilities p=2679/10000, 1/2, eta=2321/10000 respectively.
They use disjoint inputs conditional on all category flags; their COUNTS
are multinomial, not independent.

Here is the exact conditional rejected-state law, including the zero atom.
Let D=10000, P=2679, aR=D-2P=4642. Extend J_d by zero beyond 2H-1.
For H<=d<2H put v=2H-d; direct summation of the two remaining ramps gives

 J_d=v(v-1)(3H-v-1)/6.                                 (11.1)

Indeed sum_(x=1)^(v-1) (H-x)(v-x) has exactly this value by the elementary
sums of x and x^2. For d<H use the cubic J_d of Section4 and J0=(2H^3+H)/3.
Define nonnegative integer weights

 S0 = D J0 - 2P H^3,
 S_d = 2D J_d - 2P H^3, 0<d<H,
 S_d = 2D J_d, H<=d<2H.                               (11.2)

They are nonnegative because the actual first-V coins are valid. More
explicitly J_d>=pH^3 below H and J0>=2pH^3. Unconditionally the residual
mass at zero is J0/(2H^4)-p/H, at positive d<H it is J_d/H^4-p/H,
and at d>=H it is J_d/H^4. Their sum is eta=1/2-p. Dividing by eta
therefore gives the normalized law

 Pr_R(d)=S_d/(aR H^4), sum_d S_d=aR H^4.                (11.3)

The conditional phase density is Q_(A'd), not a decohered or relabeled
approximation. Histories leading to a new d have the same phase up to a
scalar. The exact rejected law is not asserted uniform.

Pool these R states globally within the same stage/target, in original
first-V-pair generation order. All common bucket offsets have already
cancelled. Pair consecutively and use the CNOT difference/sign instrument.
Let C_R(d)=sum_x S_x S_(x+d). Counts before the fair difference outcome
are C_R(0) at zero and 2C_R(d) at positive d, out of aR^2 H^8.
We now give a uniform counted evaluator and a complete certificate of

 C_R(0)>=aR^2 H^7/4,
 C_R(d)>=aR^2 H^7/8, 1<=d<H.                          (11.4)

All actual middle widths are powers of two, so H is a power of two >=2.
Handle H=2,4 by the following explicit finite integer arrays:

 H=2: S=[17136,37136,20000,0],
      C_R(0..1)=[2072724992,1379082496].
 H=4: S=[97088,297088,157088,137088,280000,160000,60000,0],
      C_R(0..3)=[248757118976,189832159232,138697279488,129853599744].

Squaring/correlating these at most eight entries verifies (11.4) directly.
The finite branch computes the arrays from (11.1)-(11.2) and their at-most-
eight-term correlations, with all constant work charged. No small-H advice
is an uncharged resource. Every other production H is >=8.

### Exact constant-term evaluator for H>=8

Set S(z)=sum_d S_d z^d. Its cubic pieces, zero exception and end point imply
S(z)=N_R(z)/(1-z)^4. The following eleven terms specify N_R completely;
each row gives (a,b,c) for c z^(aH+b):

 (0,0, 2H(1963H^2+5000)/3),
 (0,1, 2H(4111H^2-30000H+20000)/3),
 (0,2, -2(8037H^3-20000H^2+10000H-10000)),
 (0,3, 2H(28037H^2-30000H+10000)/3),
 (0,4, -10000H(2H^2+1)/3),
 (1,0, 2H^2(2679H-10000)),
 (1,1, -2H(8037H^2-20000H+10000)),
 (1,2, 2H^2(8037H-10000)),
 (1,3, -2H(2679H^2-10000)),
 (2,1, -20000H), (2,2, 20000(H-1)).

To verify the list, multiply (11.2) by (1-z)^4: the fourth finite
difference of a cubic vanishes in the interior. The only possible terms
are at offsets 0..4, H..H+3 and 2H..2H+3. At each boundary compute
sum_(j=0)^4 (-1)^j binom(4,j) S_(aH+b-j), with the piecewise formula
and zero outside its support. Expanding gives exactly the eleven nonzero
terms above. Each displayed division by three is exact on integer H.
This supplies an elementary algebraic proof of the generating function.

Put Nrev_R(z)=z^(2H+3)N_R(z^-1). Reversal of the polynomial S gives
C_R(d) as the coefficient at 2H-1+d of

 N_R(z) Nrev_R(z)/(1-z)^8.                              (11.5)

The actual algorithm enumerates its 11^2=121 ordered numerator products.
For a product c z^e add c binom(2H-1+d-e+7,7) when 2H-1+d-e>=0,
otherwise zero. Compute the binomial using seven factors and exact division
by 7!. Every signed coefficient, temporary word and intermediate product
has O(n) bits, with an absolute constant degree/number of terms. The
schoolbook multiplication/division algorithms in proof.md Section11 counts all arithmetic,
constant generation, precision and address operations. There is no count,
subset-sum, memory-lookup or large-integer oracle.

### Positive certificate, including the exceptional zero

At zero, direct expansion of (11.5), or summing squares of the two cubic
pieces in (11.2), gives the exact polynomial

 C_R(0)=4H(321326083H^6-561295000H^5+1013057500H^4
       -418705000H^3+490000000H^2-595000000H+90000000)/63.

Set z=H-8. The coefficients of C_R(0)-aR^2 H^7/4 in increasing powers
z^0,...,z^7 are

 24158041501696, 458083343793664/21, 76159948669696/9,
 16451192619520/9, 2136563057440/9, 166800153808/9,
 7246625992/9, 945920749/63.

They are all positive. This proves the zero bound for every H>=8 and,
with the finite arrays, every production H.

For positive d, expansion of (11.5) gives C_R(d)=P_R(H,d), where

 P_R=5000000d^7/63+10000000d^6H/9
 -40000000d^5H^2/3+10000000d^5H/3-10000000d^5/9
 -63395000d^4H^3/3+100000000d^4H^2/3-50000000d^4H/9
 +682220000d^3H^4/9-526790000d^3H^3/3+100000000d^3H^2/9
 -50000000d^3H/3+35000000d^3/9
 -20740000d^2H^5/3+200000000d^2H^4/3-36605000d^2H^3/3
 -80000000d^2H/9-415413476dH^6/9+107160000dH^5
 -1278520000dH^4/9-73210000dH^3/3-160000000dH^2/3
 +40000000dH/3-20000000d/7+1285304332H^7/63
 -80740000H^6/3+578890000H^5/9+280000000H^3/9
 -80000000H^2/3+40000000H/7.                            (11.6)

This formula is used ONLY for 1<=d<H, H>=8. At d=0 it differs from
C_R(0); the separate central certificate above is essential. To verify its
range, represent each numerator product exponent as aH+b. In (11.5)
the remainder is (2-a)H+d-1-b. Products with a>=3 have negative remainder
through d<H, so contribute zero. For a<=2 the remainder is >=-7 when
d>=1,H>=8; the polynomial binomial vanishes for remainders -7,...,-1.
Thus the guarded binomials equal their polynomial forms on this range.
Expanding the included terms yields exactly (11.6). No assumption of
smoothness at the zero atom is made.

Here is a finite exact certificate for the positive-d inequality. Partition
x=d/H in [0,1] into four closed quarters. On quarter i=0,1,2,3 write
x=(u+i)/4, 0<=u<=1, and z=H-8>=0. The complete exact rational arrays
b_(i,k,j), 0<=k,j<=7, are archived in evidence/vreject-bernstein.json,
which is part of this proof and the evidence for every claim. They satisfy

 P_R(H,d)-(aR^2/8)H^7 = sum_(k=0)^7 z^k
      sum_(j=0)^7 b_(i,k,j) binom(7,j)u^j(1-u)^(7-j).   (11.7)

All 256 archived rational coefficients are positive. The smallest is
5742665/144, still strictly positive. The identity may be verified by
expanding the binomial basis; the included diagnostic independently checks
each bidegree-(7,7) identity at an 8-by-8 rational grid, which proves that
polynomial identity exactly. This is a constant algebraic certificate,
not a fitted-instance success experiment. Each basis term is nonnegative
for z>=0,u in[0,1], proving (11.4) for positive d. The actual integer
evaluator (11.5) is used by the algorithm; no instance-dependent certificate
or table is supplied as free advice.

### Exact retained channel, product law and complete charges

Set betaR=1/8. Reject d>=H. At zero use coin aR^2 H^7/(4C_R(0)); at
positive d use aR^2 H^7/(8C_R(d)). The two bounds (11.4) prove valid
positive integer denominators and numerators <=denominators. Including
the fair CNOT difference outcome, every retained d<H has mass betaR/H.
Thus this channel succeeds EXACTLY 1/8 and has the same uniform[0,H),
Q_(A'd) ensemble as the other stage outputs. Retain this R pass's SUMs for Section12; discard failed differences.
Only the additional R-SUM pass is applied; its outputs are then terminal.

Condition on complete earlier categories and FIRST-global-V DV,ZV,RV flags.
The retained R states have independent law (11.3), independent of all
other retained populations at the state level. Pairing uses flags and
original positions only. The exact channel above proves the independent
uniform conditional kept ensemble after its own flags. Erasing old
histories preserves Q_(A'd). Output the existing populations in their
order, then this R rescue and its new SUM rescue in that order. Availability and a fixed successful prefix
therefore preserve the next-stage product ensemble, without independence
of correlated population COUNTS or conditioning on cap survival.

The two additional concentration events and all new unmatched losses are
explicitly included in Section7. Every channel uses already acquired
qubits and no fresh source; the source count remains unchanged in form.
The actual stage coin theorem is the 7I/8 bound in Section8.
Section12 proves that this R pass and its SUM child together use at mostP6
calls, hence at mostRV/2, preserving the stated bound. Section8 proves
fewer thanR total calls, preserving the literal 4R physical-trial cap
and its additive <1/1024 loss. All failed draws, zero atoms, resets,
measurements, initialization, buffer releases and address work count.

The new 121-term constant-degree O(n)-bit kernel fits the schoolbook ordinary-sieve work envelope in proof.md Section11. Eight output populations still contain
O(L_0) phase qubits and O(nL_0) classical label/pointer bits. Local
arithmetic programs and quantum/source scratch are included before the
O(sqrt n) address width is justified. Work is sequential with no parallel
credit. Together with the exact elementary source-label and outer-recovery proofs,
this establishes the SAME fifteen-event configuration's success at
least1019/1024 and all four every-branch resource guarantees, jointly
with tau(n,Q)=0 under the canonical independent ideal-source context.

## 12. A global SUM rescue of the first-R pass

Retain SUM outcomes from the R-rescue pass of Section11, instead of
resetting them. Do not retain its failed differences. Given all preceding
categories, its inputs have the independent S/(aR H^4) law of (11.3),
aR=4642, and phase q_(A'd). Its fair SUM branch has probability1/2,
label distribution T/(aR^2 H^8) with T=S*S, and phase q_(A'j) with
ZERO common offset. Pool these ZR SUMs within the same stage/target by
original R-pair position. Pair them, apply CNOT, keep only difference,
and sign-correct. Their retained frequency is A'd, d an absolute difference.

Define E_R(d)=sum_x T_x T_(x+d). Before the fair CNOT difference, the
absolute-difference counts are E_R(0) at zero,2E_R(d) at positive d,
out of aR^4 H^16. We prove

 E_R(0)>=(2/5)aR^4 H^15,
 E_R(d)>=(1/5)aR^4 H^15 for 1<=d<H.                    (12.1)

### Exact uniform integer evaluator

S(z)=N_R(z)/(1-z)^4 and Nrev_R are the eleven-term numerators in
Section11. Since T=S*S, reversal at padded degree4H-2 gives E_R(d) as
the coefficient at4H-2+d of

 N_R(z)^2 Nrev_R(z)^2/(1-z)^16.                        (12.2)

Enumerate all11^4=14641 ordered numerator products. For product c z^e,
add c*binom(4H-2+d-e+15,15) when4H-2+d-e>=0, otherwise zero. Each
binomial is a fifteen-factor consecutive product and division by15!.
All signs, numerator coefficients, generation, multiplications, divisions
and additions are counted schoolbook operations. Intermediate bit widths
are O(n) with absolute constant degree; no count or subset-sum oracle is
assumed. Stream the fixed nested loops with a constant number of indices
and O(n)-bit words. No list of all labels or all H solutions is allocated.

For H=2,4,8, compute S by (11.1)-(11.2), convolve the at-most-sixteen-entry
S array with itself, and correlate that at-most-thirty-one-entry T array.
These are explicit fixed finite loops, with all their work/storage charged.
The exact central and minimum-positive counts for these three widths are:

 H=2: E0=8334839950808580096, Emin=6662195817036120064;
 H=4: E0=222604374051677309763584, Emin=159975469334372517150720;
 H=8: E0=6830482084072385744012836864, Emin=4745429871630420405880094720.

For each row, direct integer comparison gives5E0>=2aR^4H^15 and
5Emin>=aR^4H^15. The included diagnostic checks every positive d<H,
not merely one selected d, and reproduces these finite counts. This finite branch needs no supplied data table.
All other production H, being powers of two, are >=16.

### Complete polynomial certificates for H>=16

The exact fixed evidence file evidence/rsum-certificate.json is part of
the proof for every claim. It contains the 126 nonzero monomials of the
positive-d polynomial P_RSUM(H,d), the complete central polynomial,
the sixteen central shifted coefficients and the16-by16 positive basis
array. Every entry is an exact rational string; the definitions below
bind those data to the actual count (12.2).

For a numerator product with exponent aH+b let g_(a,b)(H) be its coefficient,
obtained by multiplying the FOUR explicit eleven-term lists from Section11.
For1<=d<H andH>=16, products with a>=5 have negative remainder
(4-a)H+d-2-b and contribute zero. For a<=4, that remainder is >=-15.
The polynomial binomial vanishes at remainders-15,...,-1. Hence on this
range the guarded count equals the fixed polynomial expression

 P_RSUM(H,d)=sum_(a<=4,b) g_(a,b)(H)
      prod_(j=0)^14[(4-a)H+d+13-b-j]/15!.               (12.3)

Expanding the finite expression gives the 126 archived monomials. All
terms of total degree above15 cancel exactly. The diagnostic verifies
this by exact INTEGER coefficient expansion, including the canceled
higher terms, rather than fitting values on sample instances. Thus
P_RSUM(H,Hx) has degree at most15 in each of H and x.
No equality to the guarded count is asserted at d=0 or d=H.

At zero the only included term with remainder below-15 is(a,b)=(4,14),
with remainder-16. Its polynomial binomial is-1 rather than the guarded
zero. Its coefficient is [N_(0,4)N_(0,0)]^2, which is positive. Therefore

 E_R(0)=P_RSUM(H,0)+[N_(0,4)(H)N_(0,0)(H)]^2.           (12.4)

Here N_(0,4)=-10000H(2H^2+1)/3 and
N_(0,0)=2H(1963H^2+5000)/3 as in Section11. Exact expansion yields the
archived central polynomial. These identities account for the zero atom;
using the positive-d polynomial alone there would be incorrect.

Put z=H-16>=0. The archived sixteen coefficients of
E_R(0)-(2/5)aR^4 H^15 in powers z^0,...,z^15 are all strictly positive.
This proves the central bound for every H>=16. Independently, with
x=d/H in[0,1], the archived positive rational array b_(k,j),0<=k,j<=15,
satisfies the exact identity

 P_RSUM(H,d)-(1/5)aR^4 H^15
   =sum_(k=0)^15 z^k sum_(j=0)^15
      b_(k,j)binom(15,j)x^j(1-x)^(15-j).               (12.5)

All256 coefficients are strictly positive. Every basis term is nonnegative
for z>=0 andx in[0,1], proving the positive-d bound throughout the required
range. The complete rational arrays and polynomial monomials are in the
snapshot, not an external citation or an instance-dependent advice table.
Their identities are verifiable by expansion. The exact diagnostic also
checks (12.5) at a16-by16 rational grid and (12.4)'s shifted central
identity at16 points; the explicit degree bounds make these FIXED
polynomial identities, not extrapolations of algorithm success rates.
The algorithm's actual count uses (12.2), not a free polynomial/certificate
lookup. The positivity certificate is mathematical evidence, not an
additional source operation or phase oracle.

### Exact retained law, all conditional events and hard limits

Reject d>=H. At zero use coin2aR^4 H^15/[5E_R(0)]; at positive d use
aR^4 H^15/[5E_R(d)]. The bounds (12.1) prove positive integer denominators
and numerators <=denominators. Including the fair difference outcome,
every retained d<H has mass1/(5H). Thus the new channel succeeds EXACTLY
1/5 and has the same uniform[0,H),Q_(A'd) ensemble as every other stage
output. Discard this new pass's SUMs and failed differences; no further
recursion is applied.

The full product law follows the prior exact instrument induction:
condition on complete preceding categories and the R-pass SUM flags.
Its disjoint SUM outputs have independent T/(aR^2 H^8) labels and the
specified phase density. Pairing depends only on generation position and
flags. Conditional on new keep flags, retained labels/qubits have the
uniform product ensemble independent of the other kept populations at
the state level. Counts remain correlated and are never declared independent.
Erasing old histories preserves the same conditional density for each d.
Output this R-SUM rescue AFTER the R-rescue outputs. Availability and a
fixed prefix preserve the next-stage invariant.

Its two new events are ZR>=eP6/2 and D7>=e(1/5)P7, with
P7=floor(ZR/2)>=(ZR-K)/2. Substitution gives the additional coefficients
eta beta7 e^4/64 in a and beta7(eta e^3/16+e^2/8+e/2) in b,
eta=2321/10000,beta7=1/5. Section7 includes them in the complete FIFTEEN-
event proof, its unmatched margin, rounding and exact smaller-q surplus.
Using e>=3/4 andeta>=1/5 gives P6>=G/512 andP7>=G/4096 on preceding
good events. Their new Chernoff exponents still exceed G/2^58, so the
same F=2^62lambda reserve gives16lambda and total shortage<1/1024.

The physical sampler cap also remains valid. R-pass coins are at most
P6-ZR; its new child has at mostP7<=ZR/2. Their combined calls are
<=P6, the allowance used in Section8. Thus the complete7I/8 stage bound,
fewer-thanR total calls and literal4R physical-trial limit are retained,
including every zero coin, failed draw, reset and measurement. This is
not an assumption that the added pass is free.

Only already acquired qubits are used. The eight output populations are
disjoint categories followed by pair consumption and still contain at
mostP1 states. Extra buffers and the14641 fixed schoolbook count terms
change only absolute constants in O(nL_0) classical bits, O(L_0) qubits
and O(n^4 L_0) ordinary sieve work. The elementary source work
O(n^(9/2)L_0) still dominates. Every generated coefficient, address,
intermediate bit, initialization and release is charged. Together with
the fresh source-label and outer-recovery proofs this establishes the
SAME actual fifteen-event configuration's full-secret success>=1019/1024,
four every-branch resource bounds and exact-zero canonical clean-input law.
