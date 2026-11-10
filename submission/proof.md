# CYCLIC-ROOTLOG: a balanced square-root-logarithm schedule

## 1. Algorithm and joint theorem

Use the full cyclic-window/source-aligned algorithm in cyclic_base.md,
with the schedule, retry factor and resource analysis below replacing
its original fixed16 configuration. That source is reproduced unchanged
from e9fc2eca-9d1c-469b-a629-a43e0f7ce928, candidate commit
45d9985c85813b2f3d30c62c717faba3621eb57a. All circuits, source identities,
collective extraction, cyclic-window freshness/collision argument,
top-bit law, source-aligned odd decoder, exact 2-adic recovery and finite
branch are supplied in full. Its original theorem concerns its original
parameters, not these. No acceptance verdict is a proof premise.

For every N>=2 and s in Z/NZ, n=ceil(log2 N), one fixed CYCLIC-ROOTLOG
configuration recovers the entire s with unconditional probability at
least 1-2^-8. Its joint bounds on every branch are

    T=O(n^3 2^E), S_C=O(n^(3/2)(log2 n)^(-1)2^F), S_Q=O(n),
    Q=O(n^(3/2)(log2 n)^(-1/2)2^F),
    E=a sqrt(n)+3sqrt(n)(log2 n)^(-1),
    F=a sqrt(n)-2sqrt(n)(log2 n)^(-1/2)+3sqrt(n)(log2 n)^(-1).

The exact rational a=u_333/v_333 and its Pell proof a>sqrt2 are in
cyclic_base.md Section 0. Constants are absolute, independent of N,s
and outcomes. These eventual representative envelopes are evaluated
for n>=2^64 and assigned any positive values on the finite smaller
prefix. Algorithmic correctness still covers every N. This extension
affects neither big-O nor the asymptotic comparison. The indices are
1/2,1/2,0,1/2. Fractional tolerance is 0 under independent ideal copies;
no maximum possible tolerance or positive robustness is asserted.

## 2. An explicit rational logarithm calculation

Write ln for the natural logarithm; all log2 notation denotes base two.
The logarithm used to choose the schedule is computed uniformly, not
supplied as advice or treated as real arithmetic at unit cost.
For integer mu>=3, let k=floor(log2 mu), J=k+20 and

    z=(mu-2^k)/(mu+2^k),
    A=2 sum_(j=0)^(J-1) z^(2j+1)/(2j+1),
    B0=2 sum_(j=0)^(J-1) (1/3)^(2j+1)/(2j+1),
    delta=(9/4)3^(-2J-1),
    ell(mu)=k+(A+delta)/B0.

All these are exact rationals computed by counted integer arithmetic.
The expansion ln(w)=2 sum z^(2j+1)/(2j+1), z=(w-1)/(w+1),
follows by integrating the geometric series for 2/(1-z^2). For
w=mu/2^k in [1,2), 0<=z<1/3. The positive tail is at most
2 z^(2J+1)/((2J+1)(1-z^2))<=delta. The same tail bound applies
at w=2. Also 2/3<=B0<=ln(2)<1 and 0<=A<1. Consequently, if
L=log2(mu),

    L<=ell(mu),
    ell(mu)-L <= delta/B0+A delta/(B0(B0+delta))<4delta<=1/mu.

For the last inequality mu<2^(k+1) or <=2^(k+1) is enough:
4delta mu<=18*2^k/3^(2k+41)<1. Thus the rational prescription
has the required one-sided accuracy. There are O(log mu) terms with
rational operands of polynomial bit length in log mu. Schoolbook
rational arithmetic therefore costs a fixed polynomial in log mu bits
and time. All such setup costs are charged.

## 3. Balanced schedules: general lemma and the fixed choice

The following lemma is proved for a fixed rational gamma in (0,1].
The algorithm CLAIMED HERE fixes gamma=1/2 for all instances and all
four resources. The auxiliary generality does not mix configurations.

For mu=ceil(sqrt(2B))+1 and the exact rational ell(mu) above, put

    x=s=max(2,floor(mu/(ell(mu)^gamma))), q=x+3, kappa=2.

There is no real-arithmetic primitive in this instruction. For
gamma=a0/b0, fixed positive integers a0<=b0, x before the max is the
largest integer v with v^b0 ell(mu)^a0<=mu^b0. Clear the rational
denominator and use integer binary search on [0,mu]. For gamma=1/2,
this is simply isqrt(floor(mu^2/ell(mu))). This uniform procedure uses
polynomial work and bits in log(mu) for the fixed choice. Since
ell lies within 1/mu above L_mu=log2(mu), the mean value theorem for
v^(-gamma), followed by flooring, gives for mu>=4

    mu/(L_mu^gamma)-2 <= x <= mu/(L_mu^gamma).           (1)

The max with two respects the upper bound because gamma<=1 and
mu/log2(mu)>=2 there. At mu=3 the actual prescription remains a
bounded integer between two and mu-1. In all cases 2<=x=s<=mu-1.

Use the source's exact boosted lengths, residue capacities, greedy
root-first allocation, leaf sum tables, cyclic-window merge and
failed-input disposal at these x,s. The depth is the least m>=s+1
with C(m)>=B, where

    C(z)=z(z+1)/2-s(s-1)/2+x(z+1)+2.

At z=mu, x=s makes C(mu)>=mu^2/2>=B, because x mu-x^2/2 is
nonnegative. Hence m exists and m<=mu. Summing the three bmax regimes
gives C(m), and bmax_i+lam_(i+1)-2lam_i=-2. All residue windows stay
below B. The unchanged low-prefix conditioning and incidence injectivity
therefore satisfy the cyclic-window source's freshness proof: fresh
non-root failure is <2^-q under that invariant, while the root has the
separate distribution-free bound <=1/4. This is not a fixed-full-table
bound for non-root inputs.

We have q>=5 and m2^-q<=1/2. For mu<16 use m<=15. For mu>=16,
(1) gives q>=mu/(log2 mu)^gamma+1>=mu/log2(mu)+1>=log2(mu)+1.
The last inequality follows from log2(mu)<=sqrt(mu). Since
-ln(1-p)<=2p for p<=1/32, the retry product is at most (4/3)e<4.
Use the source's fresh-whole-attempt and reach-probability argument,
without assuming independence of attempt cost and success.

Define the actual literal cap by

    A_star=max_(1<=B<=n) q(B)2^m(B),
    Q_star=8 A_star(G_odd+2a2)+2a2, Qcap=1024 Q_star.

The exact maximum is computed before acquisition. All decoder grids,
seed precision, its size-selected backward mode and extractor confidence
use the actual new tree and Qcap. The O(n) expected-root budget proof
remains applicable because log2(q2^m)=O(sqrt n). The source's explicit
parity caps and finite branch are retained. The factor eight accounts
for two acquisitions per accepted leaf and retry product below four.

## 4. Uniform analytic bounds for the balanced family

For analysis let R=sqrt(2B)>=4, L=log2 R and g(R)=R L^(-gamma).
Then g is increasing, 0<g'(R)<=1. Since R+1<=mu<=R+2, (1) implies

    g(R)-2<=x<=g(R)+2, q<=4g(R).                       (2)

The second uses g(R)>=R/L>=2. Completion of the square bounds m by
the maximum of s+1 and
ceil(sqrt(R^2+s^2+(x+1/2)^2)-x-1/2). The square-root candidate plus x
is at most R+x^2/R+x/(2R)+1/(8R)+1. Since x=s and (2) holds,

    m+x<=R+R L^(-2gamma)+C.                            (3)

The lower constraint fits this bound as well, not just for large R:
2x+1<=2g(R)+5<=R+R L^(-2gamma)+5, using 2u<=1+u^2
with u=L^(-gamma). The omitted terms in the square-root estimate are
bounded constants because L>=2 and g(R)/R<=1. A uniform constant
covers the finitely many B with R<4.

Subtracting the lower bound for x gives

    m<=f(R)+C, f(R)=R-R L^(-gamma)+R L^(-2gamma).        (4)

This f is increasing for R>=4. Indeed, writing u=L^(-gamma) in (0,1],

    f'(R)=1-u+u^2+[gamma/(ln(2)L)](u-2u^2).

Here 1-u+u^2>=3/4, u-2u^2>=-1, and
gamma/(ln(2)L)<=1/(2ln2)<3/4 since ln2>2/3. Thus f'>0.
These inequalities also show g'>0 as used in (2).
Consequently, with R*=sqrt(2n), L*=log2 R*,

    A_star=O(g(R*)2^f(R*)),
    Qcap=O(n^(3/2)(log2 n)^(-gamma)2^f(R*)).           (5)

No monotonicity of a rounded integer schedule is assumed. Fixed
small-width trees only enlarge an outside constant.

## 5. Joint correctness and every-branch work

The schedule still uses only the exposed low prefix. The source's
conditional independent-high-bit and top-bit arguments, source transforms
and source-aligned decoder apply with the actual new widths. The retry
product below four gives expected tree acquisitions <=8 A_star. The
same root/parity reach-probability argument establishes Q_star as an
uncapped ideal-process expectation bound. Markov adds <=2^-10 cutoff
error. The unchanged label-extraction coupling and seed/backward/parity
error budget in cyclic_base.md Section 12 keeps the total below 2^-8.
All are unconditional first-error and cutoff comparisons. Incorrect
labels and earlier decoder mistakes still obey the fixed resource caps.
The n<64 exhaustive branch is unchanged.

Every acquisition pays at most one merge at each level because failed
inputs are discarded. The deterministic common core-work charge is
O(n(m+1)2^kappa 2^x/q). For every actual width, (2) and the increase
of 2^v/(v+3) give

    2^x/q=O(2^g(R*)/g(R*)).

Thus the charge is O(n(log2 n)^gamma 2^g(R*)). Multiply by the actual
cutoff (5), for this same fixed gamma, to obtain

    tree core work=O(n^(5/2)2^(R*+R*(L*)^(-2gamma))).    (6)

The O(n^2) per-copy source transforms and collective extraction are
smaller because their negative g(R*) in (5) dominates every polynomial
factor. Seed scoring O(n^2 A_star), feedback and polynomial rational
setup are also below (6). All initialization, measurements, resets,
disposal, explicit lookups, circuit generation, wrong-label branches,
failed attempts, abandoned subtrees and (n+1)Qcap source cost are charged.

Quantum stack and active scratch are O(n): m and all index lengths
are O(sqrt n). To count classical bits, use actual stored high-part
widths w_i=B+1+i+ceil(log2 q)-p_i. Since B-p_i is the sum of the
remaining windows, w_i=O(sqrt n(m-i+1)). There are only constantly many
resident tables per level. The s plateau levels sum to
O(sqrt n s^2 2^lambda_max) bits; growing levels have a smaller geometric
tail. Merge scratch is O(sqrt n 2^lambda_max), and common residues,
extractor records, seed scores and all other polynomial scratch are
separately included. Because x=s, lambda_max=3+m, and uniformly
s=O(g(R*)), we get

    S_C=O(n^(3/2)(log2 n)^(-2gamma)2^f(R*)).            (7)

Polynomial-only scratch and the finite prefix are absorbed by this
eventually positive exponential envelope. Address length is O(sqrt n),
so (6) gives total charged work

    T=O(n^3 2^(R*+R*(L*)^(-2gamma))).                  (8)

These bounds, (5) and O(n) qubits hold jointly on every branch of the
single stated configuration whose success was proved above.

## 6. Fixed gamma=1/2 and exact supported envelopes

Now fix gamma=1/2 once and for all, as the claimed algorithm does.
Put t=log2 n. The actual work correction is

    R*/L*=2sqrt2 sqrt n/(t+1)<=3sqrt n/t.

The negative storage/source term has the particularly simple coefficient

    R*/sqrt(L*)=2sqrt n/sqrt(t+1).

By the mean value theorem,
2(1/sqrt(t)-1/sqrt(t+1))<=t^(-3/2). Since sqrt2<10/7 and t>=64,

    2sqrt2+1/sqrt(t)<=20/7+1/8<3.

Therefore

    f(R*)<=sqrt2 sqrt n-2sqrt n/sqrt(t)+3sqrt n/t.

Replace only the leading sqrt2 by the exact larger a. Equations
(5),(7),(8) then give exactly E,F and the outer powers in the theorem.
The finite n<2^64 prefix is assigned positive representative values
and absorbed in outside constants, while the algorithm remains defined
and correct there. No finite-prefix fitted index or hidden coefficient
is used. Each exponential logarithm is a sqrt n+o(sqrt n), so its exact
index is 1/2. The quantum envelope n has exact index zero.

The rational logarithm routine and balanced-family analysis develop
this session's CYCLIC-LOG work, and the full cyclic-window machinery is
material reuse of e9fc2eca-9d1c-469b-a629-a43e0f7ce928. All material
published predecessors are declared explicitly. This configuration pays
a larger sqrt n/log n time correction for a stronger sqrt n/sqrt(log n)
source/memory saving. It is a resource tradeoff at index 1/2, not the
1/3 research goal, practical-device evidence or global frontier leadership.
