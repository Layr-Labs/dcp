# PS7: pool same-bucket sum outputs before a second difference pass

This is the actual PS7 sieve stage and complete replacement quota analysis.
The exact source/QPE/arithmetic framework and global sampler cap are retained
with the parameters below. Pairing uses bucket and original positions only.
No prior verdict or empirical distribution assumption is a proof premise.

## 1. Exact primary categories and conditional quantum ensembles

At a stage the labels u are independent uniform in[0,B), with conditional
phase qubit q_(A*u). Decompose u=r0+2^a(v+M*h0), with M=B/2^(a+c) an even
power of two>=4. Bucket by(r0,h0), then pair consecutive records in original
position order inside each bucket, leaving at most one unmatched record per
bucket. Given the full bucket vector, all v are independent uniform in[0,M).
A bucket has common f0=A*(r0+2^a*M*h0) and A'=A*2^a, so frequencies are
f0+A'v. This does not replace N by a power-of-two modulus.

For each pair apply CNOT and measure its target. The two outcomes are fair
for every label and secret, because all computational amplitudes have equal
magnitudes. Outcome zero leaves q_(f1+f2); outcome one leaves q_(f1-f2) up
to a global phase. Apply X to the difference if its known integer sign is
negative. These follow directly from remaining amplitudes
[1,exp(2pi i*s*(f1+f2)/N)] or
[exp(2pi i*s*f2/N),exp(2pi i*s*f1/N)].

A primary difference has d=|v1-v2|. Reject d>=M/2, keep zero, and otherwise
keep by the exact coin M/[2(M-d)]. Uniform v1,v2 have counts M at zero and
2(M-d) at positive d. The successful primary instrument is therefore

    (1/(2M)) sum_(d=0)^(M/2-1) |d><d| tensor Q_(A'd),

with trace1/4 and normalized uniform label/qubit law. A primary SUM outcome
has trace1/2 and normalized classical/quantum law

    sum_(j=0)^(2M-2) T(j)/M^2 |j><j| tensor Q_(2f0+A'j),

where T(j)=j+1 for j<=M-1 and 2M-1-j thereafter. Its flag is independent of
the original labels; the sum law is triangular, not asserted uniform.
The third category is a rejected primary difference, with total probability
1/4; its qubit is discarded. Disjoint primary inputs imply independent category
flags and conditional states. In particular, conditional on ALL categories,
kept-primary labels are independent uniform, sum labels are independent with
lawT/M^2, and these two retained populations are independent. Conditioning on
a difference coin outcome affects only that pair's disjoint input values.

## 2. Stable sum pooling and its exact rescue instrument

Store EVERY primary SUM state with its middle-sum label and original pair
position. Within each bucket, pair these sum states in original-pair order,
never by their sum values. Each has the SAME offset2f0; the number and pair
assignment are determined only by primary categories and original positions.
There is at most one leftover SUM state per bucket. Conditional on the full
primary-category vector, the paired sum inputs are independent triangular
ensembles. Different bucket offsets are never combined.

Apply CNOT/target measurement to each such pair. On difference outcome one,
correct the sign with X to obtain q_(A'd), d=|j1-j2|. Their common offset
cancels exactly. The SUM outcome at this SECOND pass is discarded; PS7 does
not recurse further. Primary-kept states remain untouched.

Let C_d=sum_j T(j)T(j+d). For0<=d<=M, splitting at j=M-1-d,M-1 and summing
the three quadratic products gives

    C_d=(2M^3+M)/3-Md^2+(d^3-d)/2.                 (2.1)

The products are (j+1)(j+d+1), (j+1)(2M-1-j-d), and
(2M-1-j)(2M-1-j-d). Expand them using sum i=v(v+1)/2 and
sum i^2=v(v+1)(2v+1)/6, verified by successive differences. Thus (2.1)
is an exact count, not a model for an unproved distribution. The absolute
sum-difference counts are C0=M(2M^2+1)/3 at zero and 2C_d at positive d,
out of M^4 ordered middle quadruples. Also

    C_d-C_(d+1)=M(2d+1)-(3/2)d(d+1)>0, 0<=d<M/2,
    C_(M/2)=23M^3/48+M/12>=C0/2.

The latter difference is M(7M^2-4)/48>=0; the first inequality follows
by d<=M/2. Hence2C_d>=C0 for every0<=d<M/2. Keep zero, reject d>=M/2,
and otherwise keep with probability C0/(2C_d). It is a valid rational coin
with positive denominator. Including the second-pass CNOT difference, each
accepted label has identical weight C0/(2M^4), so the normalized law is the
SAME uniform Q_(A'd) ensemble as a primary success. The total rescue-success
probability, conditional on the two primary SUM states, is

    p_M=C0/(4M^3)=1/6+1/(12M^2)>=1/6.             (2.2)

No extra factor for primary SUM flags is inserted in this conditional formula.

For each new label, every erased old history leaves exactly the same density
matrixQ_(A'd); its scalar phase is global. Disjoint rescue pairs have independent
inputs conditional on primary categories and independent fresh coins. Thus,
conditional on every primary category and rescue keep flag, ALL kept primary
and rescued labels/qubits have the uniform PRODUCT ensemble. This also proves
their mutual independence; it does not assume that the two marginal count
populations are independent. Discarding old labels adds no dephasing.

Use a fixed output order: all primary successes in original-pair order,
then rescue successes in bucket/original-pair order. This order is a function
of categories and positions, not retained label values. Conditioning on enough
outputs and taking the first target number preserves the product law. This
is the exact next-stage induction invariant, including pool sizes and prefix
selection. All physical outcomes and discarded states remain charged.

## 3. Actual parameters and fully rational coefficient proof

For n=ceil(log2 N)<=16 retain the exhaustive verifier with n+10 fresh tests
per candidate. For n>=17 let m=floor(log2 N), h=n+1 and set

    q=55/8, r=25/9, epsilon=1/4096 (analysis constant),
    ell=min{v>=1 : v+sum_(j=0)^(v-1)floor(r*j)>=m-1},
    J=m-1-ell, lambda=clog(1024h),
    M_meas=8192lambda, F=2^36 lambda,
    L_i=ceil(F q^(ell-i)), R=4(J+1)L_0,
    global_coin_trial_limit=4R.

Hereclog(z) is the bit length of z-1, namelyceil(log2 z). Generate every integer
exactly: L_i=ceil(F55^t/8^t). Compute ell by integer binary search on[1,m-1]
using the displayed capacity sum; that endpoint is feasible because capacity
is at leastv. Allocate b_i greedily up tofloor(r*(ell-i-1)) to totalJ, then
for targetj split b_i into a_i,c_i greedily so sum a_i=j. All widths and caps
are fixed independently of s and outcomes. Setup, constants and integer
arithmetic are counted; ordinary polynomial-time preprocessing suffices.

The same width identity gives M>=4 at every stage, and updates
A<-A2^a_i, B<-B/2^(b_i+1) end atA=2^j,B=2. All ordinary frequencies obey
A*B<=N, and sum frequencies during pooling need not be reduced modulo any
fictitious group. The CNOT identities above hold for integer frequencies
modulo the actualN even when sums wrap around it.

We prove r<log2q<1391/500. The exact interval
69/100<ln2<347/500 follows from
ln2=2sum_(j>=0)1/((2j+1)3^(2j+1)): its first three terms total842/1215,
and its remaining positive tail is at most1/6804. This series follows by
integrating2/(1-t^2) from0 to1/3. All displayed rational comparisons hold by
integer arithmetic.
For the lower logarithm bound put x=(2/9)(69/100)=23/150. Then
2^(2/9)>exp(x)>=1+x+x^2/2=52429/45000>64/55, so q>2^(25/9).
For the upper bound put x=(109/500)(347/500)=37823/250000. For0<=x<3,
exp(x)<=1+x+x^2/[2(1-x/3)], by j!>=2*3^(j-2) forj>=2. That rational
expression is strictly below64/55. Therefore2^(109/500)<64/55=8/q,
so q<2^(1391/500). These are proved inside-exponent coefficients, not fitted
or guessed logarithms.

Capacity is at least(25/18)(ell^2-ell), so
ell<=ceil(sqrt(18n/25))+1<=sqrt(18n/25)+2<=(849/1000)sqrt n+2,
using849^2*25=18020025>18000000. Capacity is <3ell^2, so
ell>=sqrt((n-2)/3); henceell=Theta(sqrt n). Consequently

    L_0=O((log2 n)*2^(c sqrt n)),
    c=(1391/500)*(849/1000)=1180959/500000=2.361918. (3.1)

The exact F and ceilings remain part of the program. Increasing F from SG6
changes actual finite budgets; no small-n practical speedup is asserted.

## 4. Three-event shortage analysis without false count independence

Fix a stage bucket vector, let I=L_i, K=2^b_i<=q^(t-1), t=ell-i>=1.
The primary-pair count P satisfies P>=(I-K)/2. Let D count kept primary
differences and Z count primary SUM states. The independent per-pair category
instrument in Section1 gives

    D~Binomial(P,1/4), Z~Binomial(P,1/2).

D and Z are NOT claimed independent; only their separate Chernoff bounds are
used. Let U be the number of pooled same-bucket sum pairs. With at most one
unmatched sum per bucket, U>= (Z-K)/2. Conditional on the ENTIRE primary
category vector, rescue successes W are independent with lawBinomial(U,p_M),
p_M>=1/6, by Sections1-2. Total outputs are Y=D+W.

Put epsilon=1/4096. Consider events

    D>=(1-epsilon)P/4,
    Z>=(1-epsilon)P/2,
    W>=(1-epsilon)U/6.

On all three,

    Y>=((1-epsilon)/4+(1-epsilon)^2/24)P-(1-epsilon)K/12
      >=(7/48-epsilon/6)I-11K/48.                (4.1)

The fractional surplus is exact:
q*(7/48-epsilon/6)-1=457/196608>1/512. SinceI>=Fq^t andK<=q^(t-1),
(4.1) is at least Fq^(t-1)+1>=ceil(Fq^(t-1)) forF>=1024. This follows
from (457/196608)F-11/48>=1 and q^(t-1)>=1. Therefore the three events
ensure the actual next quota, including its ceiling.

Also P>=Fq^(t-1). On the Z event,
U>=(1-epsilon)P/4-K/2>=Fq^(t-1)/16, sinceepsilon<=1/2,F>=8.
The elementary Chernoff inequality for independent Bernoulli variables gives

    Pr(D event fails)<=exp(-epsilon^2 P/8),
    Pr(Z event fails)<=exp(-epsilon^2 P/4),
    Pr(Z event and W event fails)<=exp(-epsilon^2 Fq^(t-1)/(16*12)).

For the last line condition on each primary-category vector satisfying Z's
event; the bound is uniform because U has the stated lower bound andp_M>=1/6.
Integrating these conditional bounds needs no independence ofD,Z,U. Since
epsilon^2=2^-24 and16*12*2^24<2^32, each term is at most
exp(-Fq^(t-1)/2^32)<=exp(-16lambda). Thus

    Pr(stage shortage | bucket vector)<=3exp(-16lambda). (4.2)

The bound is uniform in that vector. The product state law after availability
and prefix retention justifies applying it at every subsequent stage.
Initial qualification from4L_0 source copies fails with probability<=exp(-L_0/4).
The finalF iid binary labels have fewer than2M_meas ones with probability
<=exp(-F/16), sinceF/M_meas=2^23>=8. Both are smaller thanexp(-16lambda).
At mosth(h+2) checks thus fail with probability at most
3h(h+2)exp(-16lambda)<1/1024, using2^lambda>=1024h.
Outer phase measurement error remains<=4h exp(-M_meas/2048)<1/1024.
These are availability/intersection bounds, not phase estimates on an aborted
branch or favorable-outcome conditioning of the physical program.

## 5. Hard sampler, all branchwise caps and unconditional success

Primary coins have numeratorM, denominator2(M-d); rescue coins numeratorC0,
denominator2C_d. Keep zero and reject outside the target interval. Every
numerator is at most its positive O(n)-bit denominator. Drawclog(Denom)
independent fair bitsV, retry whenV>=Denom and otherwise accept whenV<Num.
Each trial completes with conditional probability at least1/2, regardless of
all earlier labels/outcomes. Exact cubic counts use the charged adaptive
product, not a constant-cost arithmetic oracle.

Permit at most4R total sieve-coin trials. A primary pair in the SUM category
requires no difference coin. If there areP primary pairs andZ sum states,
primary coin calls are at mostP-Z and rescue calls at mostfloor(Z/2), hence
at mostP<=I/2 in total. This is a deterministic bound on every branch, not
an average. Sum_i L_i<2L_0 becauseq>6,F large, and ell<=q^ell<=L_0/F;
therefore all batches need fewer than(J+1)L_0<R coins. The existing adaptive
Bernoulli coupling then bounds needing more than4R trials byexp(-R/4)<1/1024.
The hard cap, all rejected draws and resets are counted. Never condition on
no cap and assert the ideal rational instrument; transfer it additively.

For exact latent labels and ideal uncapped coins, shortage, outer-phase and
fresh-copy verification failure each have probability<=1/1024. Transferring
to the literal global cap costs at most1/1024, and the complete actual
source/gradient comparison costs at most1/1024. Thus success>=1019/1024,
without treating trace distance as an observable good-resource flag. Every
stage, source and trial is capped on every branch. The finite exhaustive
branch also meets that guarantee.

## 6. Complete joint charged envelopes and acquisitions

Sum buffers store O(n)-bit labels and indexed phase-wire positions. Primary
and sum-rescue populations together never need more than a constant multiple
ofI wires/records; no quantum state is copied. The second-pass SUM outcomes
are discarded and their costs included. Cubic C_d construction takes
O(n*2^(20sqrt(log2 n))) logical bit work per primary/rescue group by the
fully specified adaptive arithmetic. All full addresses and instruction
copies cost O(A_addr^2)=O(n), giving ordinary stage/batch work
O(n^3 L_0*2^(20sqrt(log2 n))). The 4R random-trial cap costsO(n^3 L_0).
Exact source extraction costsO(n^3 L_0*2^(21sqrt(log2 n))) and dominates.
All new parameter and ceiling construction, fixed/generated matrices,
initialization, local program/pointer records, resets, failures and final
verification fit the same envelope. No parallel work is discounted.

Withc=1180959/500000, substitution of(3.1) proves jointly

    T=O(n^3(log2 n)*2^(c sqrt n+21sqrt(log2 n))),
    S_C=O(n(log2 n)*2^(c sqrt n)),
    S_Q=O((log2 n)*2^(c sqrt n)),
    Q=O(n(log2 n)*2^(c sqrt n)).                 (6.1)

Classical records costO(nL_0) and accessible phase listsO(L_0). Extra local
arithmetic/Fourier/gradient scratch and pointer/instruction records have log
sizeO(log n+sqrt(log n))=o(sqrt n), so they fit those bounds and justify the
sameO(sqrt n) address length before charging operations. All spare arrays,
sum buffers, inputs, counters and ancillas are included and reused between
sequential batches.

Every acquired source copy is still bounded byN(n+10) forn<=16 and by
4(J+1)L_0+(n+10)(2^ell+2) otherwise. Pooling only existing qubits, fair coins,
arithmetic and generated constants acquire none. The final candidate bound
holds even for erroneous estimates; its O(n2^((849/1000)sqrt n)) verification
copies fit(6.1). Exact-zero malformed-copy tolerance under the same canonical
independent ideal-source model is joint with all four bounds; no robustness
optimality is claimed. Expressions apply forn>=2 andn=1 is explicitly finite.

The time structured bound has nPower3/logPower1 and exponent terms
(c,nPower1/2,logPower0) and(21,nPower0,logPower1/2). Classical/sample fields
have nPower1/logPower1 and onlyc; quantum has nPower0/logPower1 and onlyc.
The logarithm of every envelope is c sqrt n+O(log n), so each exact growth
index is1/2. Relative to SG6 the four envelope ratios are
2^(-(481/200-1180959/500000)sqrt n), tending to zero. This improves all four
upper guarantees with the same error context, not their numerical indices,
a small-n timing claim, optimality, a fastest-known DCP theorem or the
cube-root research goal.

## 7. Material sources

The primary and triangular rescue instrument/count proof directly reuse SG6
submissiondc8d6d56-9618-46bc-97a3-e9b18ec65099. PS7 changes how SUM states
are paired, proves the whole-population conditional law and three-event
concentration, and uses new exact quotas. PG5/PG4 supply adaptive exact
source arithmetic/Fourier and the global sampler; earlier MDC1/VFD3/FD2
foundations remain explicitly acknowledged in proof.md. Pooling/recycling
sum states and the CNOT identities are standard operations. The claim is
only the proved joint improvement over these specific declared guarantees.
All required distributions, coefficients, caps and charged algorithms are
reproduced; no prior verdict or inaccessible source theorem is a premise.
