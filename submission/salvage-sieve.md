# SG6: four-input sum salvage with an exact uniform output instrument

This file replaces the pair-only flat-difference sieve and its quota analysis.
All source/QPE, exact adaptive arithmetic, bounded gradient preparation, global
4R rational-sampler cap, outer decoder and fresh-copy verification are retained
with the new parameters below. The claims concern one complete SG6 execution.

## 1. Exact four-input channel, including common bucket offsets

A stage has independent uniform integer labels u in [0,B), with conditional
phase qubit q_(A*u)=(|0>+exp(2pi i*s*A*u/N)|1>)/sqrt2. For chosen a,c>=0 let
M=B/2^(a+c), an even power of two at least four, and decompose

    u=r+2^a(v+M*h), 0<=v<M.

The bucket key is (r,h). Conditional on the full bucket vector, the middle
values v remain independent uniform. Stable-sort only by bucket and original
position, group consecutive records in FOUR within each bucket, and discard
its at-most-three leftovers. Never use middle values to choose group members.
For this group let f0=A*(r+2^a*M*h), A'=A*2^a. Its four phase frequencies are
f0+A'v1,...,f0+A'v4. All these are known integer labels; s is still unknown.

Apply CNOT and measure the target on primary pairs (1,2) and (3,4). Each
outcome is independently fair for every fixed input frequency vector: all
computational amplitudes have magnitude one half. Outcome one leaves
q_(f1-f2) up to a global phase; X reverses its sign if needed. Outcome zero
leaves q_(f1+f2). These identities follow directly from the two remaining
amplitudes [exp(2pi i*s*f2/N),exp(2pi i*s*f1/N)] or
[1,exp(2pi i*s*(f1+f2)/N)], respectively. They hold for every modulus,
including wraparound of the sum frequencies.

For EACH primary difference outcome, let d=|v1-v2| (or |v3-v4|). Reject
d>=M/2; keep d=0; otherwise keep by a rational coin M/[2(M-d)]. The retained
frequency is A'd. Since independent uniform v1,v2 have counts M at d=0 and
2(M-d) at d>0, the successful one-pair instrument is exactly

    (1/(2M)) sum_(d=0)^(M/2-1) |d><d| tensor Q_(A'd),

where Q_f=|q_f><q_f|. Its trace is 1/4 and normalized output is uniform.
Two primary differences, when both retained, have the product of this law.

If BOTH primary outcomes were zero, retain the two sum-phase qubits instead
of discarding them. Their frequencies are 2f0+A'(v1+v2) and
2f0+A'(v3+v4), with the SAME offset. Apply another CNOT and measure its target.
On outcome one, correct the sign by X using the known sum labels. The common
offset cancels and the frequency is exactly

    A'*d, d=|(v1+v2)-(v3+v4)|.

On outcome zero discard it. These cases acquire no new source copies. If
any primary outcome was a difference, there is no sum-rescue operation; its
unused sum state, if any, is discarded. Thus a group produces at most two
retained states, never primary and rescued states simultaneously.

## 2. Exact rescue flattening and output independence

Let T(j) count ordered pairs of uniform middle values with sum j:
T(j)=j+1 for 0<=j<=M-1 and T(j)=2M-1-j for M<=j<=2M-2. Define

    C_d=sum_j T(j)*T(j+d).

For 0<=d<=M an exact expansion gives

    C_d=(2M^3+M)/3-M*d^2+(d^3-d)/2.                (2.1)

For clarity, split the sum at j=M-1-d and M-1: the three products are
(j+1)(j+d+1), (j+1)(2M-1-j-d), and
(2M-1-j)(2M-1-j-d). Expanding each quadratic and using
sum_(i=1)^v i=v(v+1)/2 and sum i^2=v(v+1)(2v+1)/6 yields (2.1).
Those elementary identities follow by comparing successive v, so the formula
requires no distribution heuristic or external counting oracle.

At d=0 the absolute-difference count is C0=M(2M^2+1)/3; for d>0 it is 2C_d,
out of M^4 ordered quadruples. The count is positive on [0,M/2]. Moreover

    C_d-C_(d+1)=M(2d+1)-(3/2)d(d+1)>0, 0<=d<M/2,
    C_(M/2)=23M^3/48+M/12,
    C_(M/2)-C0/2=M(7M^2-4)/48>=0.

The strict decrease follows, for example, by d<=M/2 in the displayed
quadratic. Hence 2C_d>=C0 throughout 0<=d<M/2. The rescue rule is: reject
d>=M/2, keep zero, and for 1<=d<M/2 keep by rational coin C0/(2C_d).
It is a probability in [0,1], with positive denominator. Every retained label
has exactly the same unnormalized weight C0/M^4 before the rescue CNOT.

Conditional on both primary sums and rescue outcome one, the normalized
retained label is consequently uniform in [0,M/2), with conditional qubit
q_(A'd). The additional group's successful component is

    C0/(8M^4) sum_(d=0)^(M/2-1) |d><d| tensor Q_(A'd),

including the probability 1/4 of both primary sums and 1/2 of the rescue
difference. Its trace is C0/(16M^3)=1/24+1/(48M^2).

Each history with a given new label leaves the SAME conditional density
matrix Q_(A'd); any label-history scalar is only a global phase. Thus erasing
all old labels and discarded registers adds no dephasing. For two outputs,
only the disjoint primary differences can have survived, and their conditional
law is the uniform product law already displayed. Conditional on ANY full
primary/rescue/keep-flag pattern, the group's retained records therefore have
the product of the same normalized uniform ensemble. Mixing flag patterns
with the same output count does not change it. This proves the complete
classical/quantum instrument, not only its marginal label distribution.

Groups are disjoint. Conditional on the bucket vector they and their ideal
coin randomness are independent. Conditional on every group-output flag
pattern the successful records are independent uniform with their correct
qubits. Process groups in bucket/original-position order and primary outputs
in pair order, with rescue last when applicable. Taking the first specified
number after checking availability preserves that product law, even when
conditioning on enough outputs. This is the induction invariant for the next
stage. No conditioning on revealed middle values is used to assert constant
success, and no middle-value sorting or pairing is permitted.

Writing X in {0,1,2} for one group's output count, its exact mean is

    E X=1/2+C0/(16M^3)=13/24+1/(48M^2)>=13/24.    (2.2)

This exceeds the pair-only mean of one half for four inputs. It is a statement
about the exact ideal instrument; all physical trial caps are coupled later.

## 3. Parameters, capacity and the exact exponential coefficient

Let n=ceil(log2 N), m=floor(log2 N), h=n+1. The n<=16 branch remains the
original exhaustive verifier with k_verify=n+10. For n>=17 set

    q=739/100, r=72/25,
    ell=min{v>=1 : v+sum_(j=0)^(v-1) floor(r*j)>=m-1},
    J=m-1-ell,
    lambda=clog(1024*h), M_meas=8192*lambda, F=2^32*lambda,
    L_i=ceil(F*q^(ell-i)), i=0,...,ell,
    R=4*(J+1)*L_0, global_coin_trial_limit=4R.

Here clog(z) is the bit length of z-1. Powers and ceilings are exact rational
integer operations: L_i=ceil(F*739^t/100^t). Compute ell by integer binary
search on [1,m-1], with the displayed finite sum for its capacity. Its upper
endpoint is feasible because capacity>=v, so J>=0. All parameters and loop
caps are independent of outcomes and s. Their generation is counted; ordinary
schoolbook integer operations suffice for this one-time polynomial work.

Allocate b_i greedily in increasing i up to floor(r*(ell-i-1)), until exactly
J bits have been allocated. Capacity ensures this succeeds. For target j,
allocate its low widths a_i greedily from b_i; set c_i=b_i-a_i. Then
sum a_i=j, sum b_i=J. As in the original endpoint argument, M=B/2^b_i is
an even power of two at least four, and A'=A*2^a_i, B'=B/2^(b_i+1) end at
A=2^j,B=2. The product A*B never exceeds N; no fictitious power-of-two modulus
is substituted for N. After grouping, retain the first L_(i+1) outputs or abort.

We prove r<log2 q<1443/500 using only small rational inequalities. First

    69/100<ln2<347/500.

Indeed ln2=2 sum_(j>=0) 1/((2j+1)3^(2j+1)), obtained by integrating the
geometric series 2/(1-t^2) from zero to 1/3. The first three terms sum to
842/1215; the remaining positive tail is at most 1/6804. These two rational
bounds imply the displayed interval. Therefore
2^(3/25)>1+(3/25)(69/100)=2707/2500. Since
739*2707=2000473>2000000, q>8/2^(3/25)=2^(72/25).

For the upper bound put x=(57/500)(347/500)=19779/250000. For 0<=x<3,
exp(x)<=1+x+x^2/[2(1-x/3)], because j!>=2*3^(j-2) for j>=2. This rational
upper expression is 131723402947/121703500000, and multiplying it by 739
is strictly less than 800. Thus 2^(57/500)<800/739=8/q, proving
q<2^(1443/500). All constants inside the bound are established, not guessed.

The capacity is at least (36/25)(ell^2-ell), using floor(x)>=x-1. Hence
ell<=ceil((5/6)sqrt(n))+1<=(5/6)sqrt(n)+2. Its upper bound is <3ell^2, so
m>=n-1 also gives ell>=sqrt((n-2)/3). In particular ell=Theta(sqrt n).
The exact quotients give

    L_0<=F*q^ell+1=O((log2 n)*2^((481/200)sqrt(n))),
    (1443/500)*(5/6)=481/200=2.405.               (3.1)

The first inequality retains F=2^32 lambda and the exact capacity schedule;
no outside finite constants are invented. The large F is deliberate to make
the finite shortage proof simple. This does not assert a practical small-n
speedup. All constants are absolute and the finite exhaustive branch is
absorbed in the common asymptotic envelopes.

## 4. Uniform bounded-output shortage proof

At a stage with t=ell-i>=1 there are K=2^b_i possible buckets. Since
b_i<=r(t-1) and 2^r<q, K<=q^(t-1). Grouping four leaves at most 3K unmatched
records, so there are at least (L_i-3K)/4 groups. Conditional on the bucket
vector, their independent outputs X_g lie in [0,2] and have mean at least
13/24. Put mu=E sum X_g and target z=L_(i+1). Then

    mu>=13/96*(L_i-3K), mu<=L_i/2<=4F*q^(t-1),
    z<=F*q^(t-1)+1.

The fractional surplus is exact: 13q/96-1=7/9600>1/2048. Since F>=2^32,

    mu-z >= (F*7/9600-13/32)*q^(t-1)-1
           >= F*q^(t-1)/4096.                   (4.1)

For the last step use q^(t-1)>=1, 7/9600>1/2048 and F/4096>=45/32.
All means here integrate over the independent middle values and quantum/coin
outcomes; they do not condition on those values and assume a constant flag law.

For independent Y_g=X_g/2 in [0,1], convexity gives
E exp(-uY_g)<=1-EY_g+(EY_g)exp(-u). The elementary Chernoff derivation for
Bernoulli variables therefore applies to these bounded variables with mean
mu/2. Consequently

    Pr(sum X_g<z)<=exp(-(mu-z)^2/(4mu))
       <=exp(-F*q^(t-1)/2^28)<=exp(-16lambda).   (4.2)

There are at most h batches and h+2 shortage checks per batch. Initial
qualification from 4L_0 source copies has mean at least 2L_0 and shortage
<=exp(-L_0/4). Final F iid binary labels have shortage of 2M_meas ones
<=exp(-F/16), since F/M_meas=2^19>=8. These bounds are smaller than
exp(-16lambda). Therefore the probability of any first shortage is at most

    h*(h+2)*exp(-16lambda)<1/1024,

using exp(-x)<=2^-x and 2^lambda>=1024h. The exact product instrument from
Section 2 justifies the next stage after availability and prefix retention.
Outer phase measurement error remains <=4h*exp(-M_meas/2048)<1/1024.
These are unconditional intersection-event bounds; no estimate is assumed
to exist on an aborted branch.

## 5. Physical exact coins and the global hard cutoff

Primary coins use numerator M and denominator 2(M-d); rescue coins use
numerator C0 and denominator 2C_d. Skip the coin for d=0 and reject outside
the target interval. Every stated numerator is <=its positive denominator by
Sections 1-2. Implement either rational coin by drawing clog(D) fair bits V,
retrying if V>=D and otherwise accepting when V<numerator. Each trial
completes with probability at least one half for EVERY history, regardless
of the classical label-dependent denominator. All integers have O(n) bits:
C_d is a degree-three expression in O(n)-bit labels. Fair bits, all rejected
draws, comparisons, resets and counters are physically counted.

Use the same single hard limit of 4R trials across the whole algorithm.
At most two coins occur per four-input group: two primary differences or
one rescue coin, never both kinds. Thus a stage needs at most L_i/2 coins.
Furthermore, with q>2 and F large,

    sum_(i<ell)L_i <= (q/(q-1))*F*q^ell+ell <2L_0.

For example q/(q-1)<6/5 and ell<=q^ell<=L_0/F make the last inequality
immediate. Hence all batches have fewer than (J+1)L_0<R coins.
The adaptive Bernoulli domination and ideal-coin coupling in fast-labels.md
Section 6 still bound global-cap abort by exp(-R/4)<1/1024. This replaces
no new model assumption; never condition on no cap and assert an exact
physical uniform law. Analyze the ideal product instrument, then transfer
it by this additive error. Source/gradient, shortage, outer-phase and fresh
verification budgets remain separately at most 1/1024, so full-secret success
is at least 1019/1024 jointly with all the resources below.

## 6. Complete charged costs, acquisitions and structured representation

Each group uses a constant number of CNOTs, measurements and kept phase wires.
Computing C_d exactly includes d^2,d^3 and degree-three known integer arithmetic.
Use the fully specified adaptive product; this costs
O(n*2^(20sqrt(log2 n))) LOGICAL bit work per group, not O(n) guessed from the
old pair-only channel. Including full O(A_addr^2)=O(n) addresses, ordinary
all-stage/all-batch group work is O(n^3 L_0*2^(20sqrt(log2 n))). The hard
4R sampler-trial cap costs O(n^3 L_0), since each O(n)-bit trial is charged
O(n^2). Stable bucket grouping likewise fits. Source extraction still costs
O(n^3 L_0*2^(21sqrt(log2 n))) in total and dominates these terms. All new
parameter/quota construction, initialization, fixed or growing constants,
failed attempts and final verification fit that same source envelope.

With c=481/200, substituting (3.1) proves the JOINT branchwise guarantees

    T=O(n^3(log2 n)*2^(c sqrt(n)+21sqrt(log2 n))),
    S_C=O(n(log2 n)*2^(c sqrt(n))),
    S_Q=O((log2 n)*2^(c sqrt(n))),
    Q=O(n(log2 n)*2^(c sqrt(n))).                 (6.1)

Classical records cost O(nL_0), accessible phase lists O(L_0). Extra local
adaptive/Fourier histories, generated matrices, pointer/instruction words and
one source/QPE workspace have logarithmic size O(log n+sqrt(log n)), below
L_0's exponential-in-sqrt(n) growth. They remain within these memory bounds,
so the O(sqrt n) address length is justified before charging access. All
batches are sequential and all allocated spare arrays/scratch are included.

For n>=17 every acquisition is still counted by

    Q<=4(J+1)L_0+(n+10)(2^ell+2).

The verification interval bound is unchanged for every estimate, including
erroneous ones; its extra O(n2^((5/6)sqrt n)) copies fit (6.1). For n<=16
Q<=N(n+10) and the fixed exhaustive branch is unchanged. Rescue operations,
new coins, generated constants and arithmetic acquire NO additional copies.
All five bounds, success and exact-zero independent-ideal-source tolerance
are for this same configuration on every modulus and secret.

The supported time structure has nPower3/logPower1 and exponent terms
(c,nPower1/2,logPower0) and (21,nPower0,logPower1/2). Classical and sample
bounds have nPower1/logPower1 and only the c term. Quantum space has
nPower0/logPower1 and only the c term. Every exact growth index is 1/2:
the logarithm of each envelope is c sqrt n+O(log n), so its iterated logarithm
is (1/2)log2 n+O(1). Expressions apply for n>=2; the finite n=1 branch has
absolute bounded cost and no asymptotic log(n) expression is evaluated there.

Compared with the corresponding PG5 envelopes, every new resource ratio is
(log2 n)/sqrt n times 2^(-(244949/100000-481/200)sqrt n), tending to zero
(the extra time sqrt(log n) term cancels). This is a strict joint improvement
of full upper guarantees, with the same tolerance context, not a new time
index, a practical timing assertion, an optimal sieve or a fastest-known DCP
claim. The large F constant must not be hidden as a measured small-n speedup.

Material sources are the PG5/PG4 adaptive exact source framework and global
sampler, and the earlier explicitly acknowledged flat-difference/MDC1/VFD3
foundations. The sum/difference CNOT identities are elementary and reproduced
above; no prior result or external theorem is a premise of the new four-input
instrument. Every required count, conditional density law, finite-error and
charged resource argument is contained in this snapshot.
