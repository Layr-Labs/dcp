# RS4: recycle primary rejected differences and a third sum level

This is the actual RS4 stage and complete quota/resource proof. It retains
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

Keep third-pass SUM outcomes; discard all failed tertiary differences. RS4 retains these third-pass SUM states for Section 6. The integer counts use O(n)-bit words (degree seven),
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
O(n) bits and count kernels have at most degree-fifteen O(n)-bit intermediates.
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

 q=193/32, r=259/100, epsilon=2^-20,
 ell=min{v>=1: v+sum_(j=0)^(v-1)floor(r*j)>=m-1}, J=m-1-ell,
 lambda=clog(1024h), M_meas=8192lambda, F=2^62lambda,
 L_i=ceil(F q^(ell-i)), R=4(J+1)L_0, global_trial_limit=4R.

Here clog(z) is the bit length of z-1. Compute exact integer quotas by
ceil(F193^t/32^t), and ell by binary search on [1,m-1]. Greedily assign
b_i<=floor(r(ell-i-1)) to total J and split their low/high portions to
sum a_i=j for each target. This is one outcome-independent configuration.
For n<=16 retain the exact n+10-test exhaustive branch from proof.md.
All source precision, reciprocal and phase parameters are recomputed from
this R, as specified in the retained source helpers.

We need r<log2 q<2593/1000. The series
ln 2=2 sum_(j>=0) 1/((2j+1)3^(2j+1)), with its geometric tail, proves
693/1000<ln 2<693148/1000000. For the upper bound use its first eight terms
and tail <=9/[4*17*3^17]. The lower bound follows from its first three terms.
For x=(41/100)(693/1000),
1+x+x^2/2+x^3/6>256/193. Thus 2^(41/100)>256/193=8/q,
which gives log2 q>259/100. For x=(407/1000)(693148/1000000),
1+x+x^2/[2(1-x/3)]<256/193. The upper exponential bound follows from
j!>=2*3^(j-2) for j>=2. Thus 2^(407/1000)<256/193 and log2 q<2593/1000.
Every comparison here is an exact rational inequality.

Capacity is at least (259/200)(ell^2-ell). Taking a feasible ceiling shows
ell<=sqrt(200n/259)+2<=(879/1000)sqrt n+2, since
879^2*259=200114019>200000000. Capacity is also <3ell^2, so
ell>=sqrt((n-2)/3); hence ell=Theta(sqrt n). Consequently

 L_0=O((log2 n) 2^(c sqrt n)), c=2279247/1000000,           (6.3)

because 2593*879=2279247. F's larger fixed constant does not change this
bound. This is a proved explicit coefficient, not an unknown inner O term.

## 7. Nine conditional concentration events and exact quota success

Fix a stage bucket vector, I=L_i, K=2^b_i<=q^(t-1), t=ell-i>=1.
Primary P1>=(I-K)/2 pairs have multinomial category counts D1,Z1,V with
marginals Bin(P1,1/4), Bin(P1,1/2), Bin(P1,1/4). Conditional on complete
earlier categories, let

 P2>=(Z1-K)/2, D2~Bin(P2,p2>=1/6), Z2~Bin(P2,1/2),
 P3>=(Z2-K)/2, D3~Bin(P3,p3>=gamma3=151/1260), Z3~Bin(P3,1/2),
 P4>=(Z3-K)/2, D4~Bin(P4,p4>=1/12),
 PV=floor(V/2)>=(V-K)/2, DV~Bin(PV,1/4).

Use the NINE lower events D1>=eP1/4, Z1>=eP1/2, V>=eP1/4,
D2>=eP2/6, Z2>=eP2/2, D3>=e gamma3 P3, Z3>=eP3/2,
D4>=eP4/12, DV>=ePV/4, where e=1-epsilon. Counts at different levels
are NOT independent; apply the later conditional bounds uniformly over
the preceding good category vectors.

Substitution gives Y=D1+D2+D3+D4+DV>=aP1-bK, with

 a=e/4+e^2/24+gamma3 e^3/16+e^2/32+(1/12)e^4/64,
 b=e/12+gamma3(e^2/8+e/2)+e/8
     +(1/12)(e^3/32+e^2/8+e/2).

Let theta=6661/40320+1/1536. At e=1, a/2=theta.
Using e^j>=(1-j epsilon), the loss in a is less than epsilon/2,
since 1/4+2/24+3gamma3/16+2/32+4/(12*64)<1/2.
Also a/2+b<1 at e=1 and thus at every e in [0,1]. Therefore

 Y>=(theta-epsilon)I-K.                                  (7.1)

The exact rational surplus is
q(theta-epsilon)-1=3209861/10569646080>1/4096.
Since I>=Fq^t, K<=q^(t-1), and F>=8192, (7.1) exceeds
Fq^(t-1)+1>=ceil(Fq^(t-1)). Thus the actual next quota, including its
ceiling, is reached on the nine events.

Put G=Fq^(t-1). P1>=G since q>6 and F is large. On the preceding good
events, P2>=G/16, P3>=G/256, P4>=G/4096 and PV>=G/32.
For example e>=1/2 and P2>=eP1/4-K/2>=G/8-G/(2F)>=G/16;
iterate this inequality for P3 and P4. The V case is identical starting
with V>=eP1/4. These estimates hold for F>=8192.

For independent Bernoulli sums, the elementary exponential-moment proof of
Chernoff gives failure <=exp(-epsilon^2 mu/2). Thus the nine exponents are
at least epsilon^2 times

 P1/8, P1/4, P1/8, P2/12, P2/4,
 gamma3 P3/2, P3/4, P4/24, PV/8.

Every exponent is >=G/2^58, because epsilon^2=2^-40,
24*4096<2^17 and gamma3/2>1/32. With F=2^62lambda this is >=16lambda.
A conditional union bound gives stage shortage <=9exp(-16lambda).
Initial qualification shortage is <=exp(-L_0/4); final label-one shortage
is <=exp(-F/16), with F/M_meas=2^49>=8. Across <=h batches, <=h stages
and these endpoint checks the total is <=9h(h+2)exp(-16lambda)<1/1024,
using exp(-x)<=2^-x and 2^lambda>=1024h. No independence between
population counts, cap survival or earlier availability is presumed.
Outer phase-estimation failure remains <1/1024 on available batches.

## 8. Every physical coin, sample and failure branch

There is still just one literal limit of 4R sampler trials. All new coins,
including zero-label and out-of-range trials, are included. For primary,
second, third, fourth and V passes, coin calls are respectively bounded by

 P1-Z1, P2-Z2, P3-Z3, P4, PV.

Since P2<=Z1/2, P3<=Z2/2, P4<=Z3/2, PV<=V/2 and V<=P1-Z1,
the sum is <=3P1/2<=3I/4. All output populations together have at most
P1 states: the sum branches consume existing states without copying, and
the primary-V branch also consumes a disjoint primary category.
With q>6, F large and ell<=n, sum_i L_i<2L_0 (the ceiling overhead ell is
smaller than L_0/2). Thus all batches use fewer than (3/2)(J+1)L_0<R coins.
Each trial completes with conditional probability >=1/2. A fresh-uniform
proof coupling dominates completions by Bin(4R,1/2), so cap-abort is at
most exp(-R/4)<1/1024. This is additive; it does not condition the exact
instrument on no abort. The complete retained proof is in fast-labels.md.

Ideal-label/uncapped-coin shortages, outer phase estimates and fresh candidate
verification each cost <=1/1024. The physical global cap costs another
1/1024 and the whole source/gradient implementation another 1/1024.
Consequently the complete program recovers s with probability >=1019/1024
for every N,s. Actual loops and allocations have hard limits on every branch.
The exact acquired-copy bound is unchanged in form:
Q<=N(n+10) for n<=16, and Q<=4(J+1)L_0+(n+10)(2^ell+2) otherwise.
Every acquired/discarded copy and failed attempt counts; new recycling
acquires no sources. All guarantees require independent ideal copies, with
tolerance tau(n,Q)=0 and the identical canonical error-model text.

## 9. All charged resources and comparison

The new F_d is seventeen degree-fifteen terms; calculate its fifteen-factor
products and exact constant-factorial divisions with the adaptive algorithm
in adaptive-arithmetic.md. Degree and number of terms are ABSOLUTE constants,
so O(n)-bit intermediates and O(n*2^(20sqrt(log2 n))) logical work per pair
suffice, as for the older cubic/seventh-degree kernels. No unit-cost binomial,
QRAM or hidden arithmetic oracle is assumed. Full O(A_addr^2)=O(n) address
and generation charges, O(n) targets and sum_i L_i<2L_0 give ordinary
sieve work O(n^3 L_0*2^(20sqrt(log2 n))). The 4R physical trials cost
O(n^3 L_0). Retained exact source extraction costs
O(n^3 L_0*2^(21sqrt(log2 n))) and dominates both. Initialization, exact
parameters, measurements, resets, bookkeeping and all failures are counted.

All five output populations together occupy O(L_0) qubits and O(nL_0)
classical label/address bits. A fixed number of pass buffers and O(n)-bit
kernel scratch do not change these peak bounds. Source/arithmetic local
records and program storage are included exactly as in the retained helpers;
their logarithmic size is o(sqrt n), and the full address width stays O(sqrt n).
There is no retained circuit history or parallel-work discount.

Substitute (6.3). For c=2279247/1000000 the SAME program obeys, on every branch,

 T=O(n^3(log2 n) 2^(c sqrt n+21sqrt(log2 n))),
 SC=O(n(log2 n) 2^(c sqrt n)), SQ=O((log2 n) 2^(c sqrt n)),
 Q=O(n(log2 n) 2^(c sqrt n)).

The four exact growth indices are 1/2, since log2 of each envelope is
c sqrt n+O(log n); the iterated log is (1/2)log2 n+log2 c+o(1).
The finite n<=16 program and outside constants do not affect the limit.
Compared with RR8's coefficient 2286279/1000000, every envelope ratio is
2^(-(7032/1000000)sqrt n), tending to zero under the same error context.
This compares proved upper guarantees, not a lower bound on RR8's actual
consumption. There is no claim of a new numerical index, fastest-known
literature result, practical small-n advantage or cube-root algorithm.
The larger fixed F and all finite constants are explicitly disclosed.
