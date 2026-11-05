# RR8: recycle primary rejected differences and a third sum level

This is the actual RR8 stage and complete quota/resource proof. It retains
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

Discard third-pass SUM outcomes and all failed tertiary differences. RR8 has
no fourth SUM level. The integer counts use O(n)-bit words (degree seven),
computed by the explicit charged adaptive arithmetic and exact division by
fixed factorials. A call to a unit-cost binomial or count routine is not assumed.

## 4. Global primary-reject pooling and a separate exact quarter-success law

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
where f=2-sqrt3>1/4 because3<49/16. The remaining terms are
H/3+H*delta/2-delta/6>=0. ThusJ_delta>=H^3/4, andJ0>=H^3/2.

Reject delta>=H. At delta=0 use coinH^3/(2J0); at positive delta use
coinH^3/(4J_delta). ZERO IS NOT ALWAYS KEPT IN THIS CHANNEL. The numerators
are at most the positive denominators by the preceding bounds. Before the
CNOT, absolute-difference counts areJ0 at zero and2J_delta at positive delta,
out ofH^4. After the difference outcome and this coin, each retained label
has probability exactly1/(4H). Hence the global-V rescue succeeds with
probability EXACTLY1/4 and has the same uniform[0,H),q_(A'd) ensemble.
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
rescues, then global-V rescues; within each use the original generation order
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
O(n) bits and count kernels have at most degree-seven O(n)-bit intermediates.
All buffers and current local program/pointer records are included.

## 6. Exact deterministic configuration and coefficient

For n<=16 retain the exhaustive verifier with n+10 fresh tests per candidate.
For n>=17, m=floor(log2 N), h=n+1, define

    q=97/16, r=259/100, epsilon=2^-20 (analysis constant),
    ell=min{v>=1 : v+sum_(j=0)^(v-1)floor(r*j)>=m-1},
    J=m-1-ell, lambda=clog(1024h), M_meas=8192lambda,
    F=2^60lambda, L_i=ceil(Fq^(ell-i)),
    R=4(J+1)L_0, global_coin_trial_limit=4R.

clog(z) is the bit length of z-1. Compute all parameters exactly; quotas are
ceil(F97^t/16^t). Binary-search the capacity on[1,m-1], whose endpoint is
feasible because capacity>=v. Greedily allocate b_i<=floor(r*(ell-i-1)) to
totalJ, and split low/high widths so sum a_i equals each targetj. All source,
phase and trial caps are outcome-independent. The width identity givesM>=4
and finalA=2^j,B=2, withA*B<=N throughout. Sums may wrap modulo actualN;
no fictitious power-of-two group or coherent source operation is assumed.

We prove r<log2q<2601/1000. The series
ln2=2sum_(j>=0)1/((2j+1)3^(2j+1)), from integrating2/(1-t^2) on[0,1/3],
has first three terms842/1215 and tail<=1/6804. Thus
693/1000<ln2<347/500. For x=(41/100)(693/1000),
1+x+x^2/2>128/97, so2^(41/100)>128/97=8/q andq>2^(259/100).
For x=(399/1000)(347/500),
1+x+x^2/[2(1-x/3)]<128/97. The upper exponential bound is valid forx<3
byj!>=2*3^(j-2), j>=2. Therefore2^(399/1000)<128/97 andq<2^(2601/1000).
All comparisons are between explicit small rationals and proved exponentials.

Capacity is at least(259/200)(ell^2-ell), hence
ell<=sqrt(200n/259)+2<=(879/1000)sqrt n+2,
using879^2*259=200114019>200000000. Its upper bound<3ell^2 also gives
ell>=sqrt((n-2)/3), soell=Theta(sqrt n). Consequently

    L_0=O((log2 n)*2^(c sqrt n)),
    c=(2601/1000)*(879/1000)=2286279/1000000=2.286279. (6.1)

F and all ceilings are explicit; the very large finiteF is not presented
as a practical small-n speedup. No unknown inside-exponent constant is guessed.

## 7. Seven conditional concentration events and actual quota success

Fix a stage bucket vector, letI=L_i,K=2^b_i<=q^(t-1),t=ell-i>=1.
Primary pairs P1>=(I-K)/2 have category countsD1,Z1,V with separate marginal
lawsBin(P1,1/4),Bin(P1,1/2),Bin(P1,1/4). They are multinomial, NOT independent.
The first SUM-pair countP2>=(Z1-K)/2. Conditional on all primary categories,
D2~Bin(P2,p2>=1/6), Z2~Bin(P2,1/2). The next SUM-pair count
P3>=(Z2-K)/2, and conditional on both earlier category vectors,
D3~Bin(P3,p3>=gamma). Global reject-pair countP_V=floor(V/2)>=(V-K)/2;
conditional on primary categories,D_V~Bin(P_V,1/4).

Use the seven events

    D1>=(1-epsilon)P1/4, Z1>=(1-epsilon)P1/2,
    V>=(1-epsilon)P1/4,
    D2>=(1-epsilon)P2/6, Z2>=(1-epsilon)P2/2,
    D3>=(1-epsilon)gamma P3, D_V>=(1-epsilon)P_V/4.

Heregamma=151/1260 andepsilon=2^-20. On all seven, substituting the lower
pair-count bounds gives Y=D1+D2+D3+D_V>=a P1-bK, where

    a=(1-epsilon)/4+(1-epsilon)^2/24
       +gamma(1-epsilon)^3/16+(1-epsilon)^2/32,
    b<=(1-epsilon)/12+gamma(1-epsilon)^2/8
          +gamma(1-epsilon)/2+(1-epsilon)/8.

At epsilon zero, a/2=theta=6661/40320 and a/2+b=18081/40320<1/2.
The elementary(1-epsilon)^j>=1-j epsilon bounds the loss in a by less than
epsilon/2. WithP1>=(I-K)/2 this proves the conservative bound

    Y>=(theta-epsilon)I-K/2.                    (7.1)

The exact surplus is qtheta-1=997/645120 and
q(theta-epsilon)-1>1/1024. ForF>=4096,(7.1) therefore exceeds
Fq^(t-1)+1>=ceil(Fq^(t-1)), including all rounding. Good count events thus
imply the actual next quota, not merely a favorable expectation.

Put G=Fq^(t-1). We haveP1>=G. On the required SUM events,P2>=G/16 and
P3>=G/256; on the V event,P_V>=G/32. These follow fromepsilon<=1/2,
K<=G/F andF>=128. Applying elementary Bernoulli Chernoff bounds separately,
conditional on each preceding good category vector when needed, the seven
failure exponents are at least

    epsilon^2 P1/8, epsilon^2 P1/4, epsilon^2 P1/8,
    epsilon^2 P2/12, epsilon^2 P2/4,
    epsilon^2 gamma P3/2, epsilon^2 P_V/8.

Every term is >=G/2^56, usinggamma/2>1/32 andepsilon^2=2^-40.
Thus stage shortage<=7exp(-G/2^56)<=7exp(-16lambda).
No unconditional independence ofD1,Z1,V,D2,Z2 or later counts is used:
condition on complete earlier categories, use uniform bounds, then union.

Initial qualification shortage<=exp(-L_0/4), final label-one shortage
<=exp(-F/16), withF/M_meas=2^47>=8. All stages/batches and these checks
have failure<=7h(h+2)exp(-16lambda)<1/1024, since2^lambda>=1024h.
The exact conditional output law in Section5 justifies induction after
availability/prefix selection. Outer phase error remains<1/1024 on available
batches; estimates are not asserted on an aborted branch.

## 8. Global physical trial cutoff and unchanged source ceilings

Every coin numerator is <=its positive O(n)-bit denominator by Sections1-4.
Use fresh fair bits, reject draws beyond the denominator and compare with
the numerator on a completed draw. Conditional completion probability is
always>=1/2. Keep the single literal4R sampler-trial limit across all passes.
The primary-reject zero coin in Section4 is included; it is not skipped.

The coin bound is NOW3I/4, not the formerI/2. Primary calls<=P1-Z1;
second-SUM calls<=P2-Z2; tertiary calls<=P3; global-V calls<=P_V<=V/2.
SinceP2<=Z1/2,P3<=Z2/2,V<=P1-Z1, their total is<=3P1/2<=3I/4.
Withsum_i L_i<2L_0 (q>6,F large), all batches have fewer than
(3/2)(J+1)L_0<R coins. The original adaptive Bernoulli/ideal-sampler coupling
therefore still bounds cutoff-abort byexp(-R/4)<1/1024. All failed draws,
zero-label coins, counters and resets are charged on every branch.

For ideal labels/uncapped coins, shortage, outer phase and fresh verification
budgets are each<=1/1024. Transfer the global cutoff with another1/1024,
and the complete actual source/gradient implementation with another1/1024.
Thus unconditional full-secret success>=1019/1024 for allN,s. Trace distance
is a whole-computation comparison, not a measurable good-gradient event.
All physical loops, source calls, trials and allocations have hard caps.

The exact source-copy ceiling is stillN(n+10) forn<=16 and
4(J+1)L_0+(n+10)(2^ell+2) otherwise, including discards, failed tests and
aborts. All new recycling uses already acquired qubits and no additional
source call. The all-outcome candidate interval bound is unchanged. The
independent ideal-source tolerance expression remains exactlyzero jointly;
no robustness optimality is asserted.

## 9. Complete charged resources and exact structured bounds

C_d,J_delta are cubic andE_d has the nine constant-degree-seven terms(3.1).
Evaluate all products by the explicit adaptive integer algorithm and exact
fixed-factorial division, costingO(n*2^(20sqrt(log2 n))) logical work per
record/pair with absolute constants. Full O(A_addr^2)=O(n) bit/address charges,
sum_i L_i<2L_0 and O(n) targets give ordinary recycling work
O(n^3 L_0*2^(20sqrt(log2 n))). The4R O(n)-bit trials costO(n^3 L_0).
Exact source extraction costsO(n^3 L_0*2^(21sqrt(log2 n))) and dominates.
All generated constants, quota construction, initialization, local compiled
program/pointer records, measurements, discards, failures and verification
are counted. No unit-cost kernel, binomial, integer product or hidden oracle
is introduced. Work is sequential; no parallelism is credited.

All phase populations together useO(L_0) wires andO(nL_0) classical label/
wire records. Local source/Fourier/arithmetic histories and instruction words
have log sizeO(log n+sqrt(log n))=o(sqrt n), belowL_0's exponential scale.
Their complete memory is included before establishingO(sqrt n) addresses.
Together with(6.1), for c=2286279/1000000 this proves jointly on every branch

    T=O(n^3(log2 n)*2^(c sqrt n+21sqrt(log2 n))),
    S_C=O(n(log2 n)*2^(c sqrt n)),
    S_Q=O((log2 n)*2^(c sqrt n)),
    Q=O(n(log2 n)*2^(c sqrt n)).                 (9.1)

The first bound has nPower3/logPower1 and exponent terms
(c,nPower1/2,logPower0),(21,nPower0,logPower1/2). Classical/sample fields
have nPower1/logPower1 and onlyc; quantum has nPower0/logPower1 and onlyc.
The logarithm of every envelope isc sqrt n+O(log n), so all exact indices
are1/2. The n=1 cases are explicitly finite; expressions apply forn>=2.
Relative to PS7 every envelope ratio is
2^(-(1180959/500000-2286279/1000000)sqrt n), tending to zero with the same
error context. This is an improvement of full upper guarantees, not a new
growth index, practical small-n speedup, optimality, fastest-known theorem
or the cube-root research goal. The very largeF is explicitly part of the
finite program and must not be misrepresented as a measured advantage.

PS7/SG6 supply the primary/triangular pooling framework, PG5/PG4 the adaptive
exact source and global sampler, and the earlier named MDC1/VFD3/FD2
foundations remain acknowledged in proof.md. Higher-sum recycling, CNOT
combination and distribution flattening are standard techniques. The exact
new kernels, rejected-state law and all needed proofs are reproduced here;
no prior verdict or inaccessible paper is a mathematical premise.
