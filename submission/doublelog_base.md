# CYCLIC-DOUBLELOG: a faster logarithmic time correction

## 1. Full algorithm and theorem

Use the complete cyclic-window/source-aligned algorithm in cyclic_base.md
with the schedule, finite-width slack, retry cap and resource analysis
below replacing its original fixed16 configuration. The source is supplied
unmodified from e9fc2eca-9d1c-469b-a629-a43e0f7ce928, candidate commit
45d9985c85813b2f3d30c62c717faba3621eb57a. All source identities, circuits,
collective extraction, cyclic-window freshness/collision proof, top-bit
law, source-aligned all-modulus decoder, finite branch and literal caps
are present in the snapshot. Its old theorem concerns its old parameters.
No previous validity verdict is a proof premise.

For every N>=2 and s in Z/NZ, n=ceil(log2 N), one fixed CYCLIC-DOUBLELOG
configuration recovers the entire s with unconditional probability at
least 1-2^-8 under independent ideal source copies. On every branch jointly,

    T=O(n^3 2^E), S_C=O(n^(3/2)(log2 n)^(-4)2^F), S_Q=O(n),
    Q=O(n^(3/2)(log2 n)^(-2)2^F),
    E=a sqrt(n)+23sqrt(n)(log2 n)^(-4),
    F=a sqrt(n)-(11/2)sqrt(n)(log2 n)^(-2)
                       +23sqrt(n)(log2 n)^(-4).

The exact Pell rational a=u_333/v_333 and its proof a>sqrt2 are in the
included source's Section 0. All outside constants are absolute and
independent of N,s and outcomes. These eventual positive representatives
are evaluated for n>=2^128 and extended positively on the finite smaller
prefix; the algorithm and success guarantee still cover every N. The
exact indices are 1/2,1/2,0,1/2. Fractional malformed-copy tolerance is
zero under independent ideal copies, not a maximum-tolerance claim.
Every acquisition, failure, rejection, discarded root and abort counts.

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

## 3. Fixed gamma=2 schedule and guarded finite-width slack

For B=D-1>=1 compute mu=ceil(sqrt(2B))+1 and the exact rational ell(mu)
above. Define by integer arithmetic

    x=s=max(2,floor(mu/(ell(mu)^2))),
    kappa=ceil(log2 mu)+1 if mu<2^16, and kappa=2 otherwise,
    q=kappa+1+x,
    C(z)=z(z+1)/2-s(s-1)/2+x(z+1)+kappa,
    m=min{z>=s+1:C(z)>=B}.

All parameters are public functions of N and B, fixed before samples.
The ceil logarithm in the finite guard is an exact integer bit length.
Since ell>1, 2<=x=s<=mu-1. Use the source's generic boosted lengths,
capacity windows and depth-first VEC formulas at these x,s,kappa:
lam_i=kappa+1+x+min(i,m-s) below the root, lam_m=1; bmax_i=x+i on
growing levels, x+m-s+1 on capped levels, and
kappa+2x+2(m-s)+1 at the root. Keep the root-first greedy allocation,
leaf tables, cyclic window and failed-input disposal unchanged.

Capacity holds at m=mu: C(mu)>=mu^2/2>=B, since x=s makes
x mu-x^2/2 nonnegative. Thus m exists and m<=mu. The exact identities
sum bmax_i=C(m) and bmax_i+lam_(i+1)-2lam_i=-kappa still hold.
Every window lies in the B-bit low prefix. Since kappa>=2, the source's
independent-high-block collision proof still has at least four times
the target mean bucket size, giving fresh non-root failure <2^-q.
Root failure has the separate distribution-free bound <=2^-kappa<=1/4.
These bounds use the same low-prefix, fresh-whole-child invariant,
not arbitrary fixed full high label tables.

The guard ensures a uniform retry constant. If mu<2^16, then
2^kappa>=2mu and q>=kappa+3, so m2^-q<=1/16.
If mu>=2^16, write L_mu=log2 mu>=16. The mean value theorem and
ell-L_mu<=1/mu give

    mu/(L_mu^2)-2<=x<=mu/(L_mu^2).

Indeed the change in mu v^(-2) is at most 2/L_mu^3<1, and flooring
loses less than one. The max with two respects this bound here.
For L_mu>=16, 2^L_mu>=L_mu^3: it holds at 16 and the ratio increases
because ln2-3/L_mu>0. Thus q=x+3>=L_mu+1 and m2^-q<=1/2.
In both regimes q>=5. Since -ln(1-p)<=2p for p<=1/32, the product
of non-root retry factors and root factor is at most (4/3)e<4.
The finite guard satisfies kappa<=17 everywhere, so its space and
work overhead is an absolute constant, explicitly included below.

Compute the exact maximum and literal source cap

    A_star=max_(1<=B<=n) q(B)2^m(B),
    Q_star=8 A_star(G_odd+2a2)+2a2, Qcap=1024 Q_star.

All decoder sizes, grids, small/large mode tests and extractor confidence
use the actual new parameters. Computing the exact maximum takes
polynomial setup work and bits; no lookup table is preloaded.

## 4. Depth and table estimates

For analysis put R=sqrt(2B), L=log2 R and g(R)=R/L^2.
For mu>=2^16, (1/mu)-accurate ell and the previous precision bound,
together with R+1<=mu<=R+2, imply

    g(R)-2<=x<=g(R)+2, q<=4g(R).

Here g is increasing with derivative between zero and one in this
range. Completion of the square, followed by concavity, gives

    m+x<=R+x^2/R+x/(2R)+1/(8R)+1

for the square-root candidate. The lower constraint also fits:
2x+1<=2g(R)+5<=R+R/L^4+5 by 2u<=1+u^2 with u=L^-2.
Using x<=g(R)+2 bounds the other candidate by R+R/L^4+16.
Subtracting x>=g(R)-2 therefore gives

    m+x<=R+R/L^4+C0,
    m<=f(R)+C0, f(R)=R-R/L^2+R/L^4,                    (1)

with the explicit common constant C0=2^20 covering all widths.
For the finite guarded regime mu<2^16, m+x<2^17 and m<2^16,
whereas R+R/L^4 and f(R)=R(1-u+u^2) are positive. Thus the same
C0 covers that entire regime without any distributional assumption.
It contributes only an absolute outside factor to an asymptotic bound.

The function f is increasing for R>=4: with u=L^-2<=1/4,

    f'(R)=1-u+u^2+[2/(ln2 L)](u-2u^2)>0.

Also g is increasing for R>=16. The finitely many smaller widths
have bounded parameters, so for R*=sqrt(2n), L*=log2 R*, (1) gives

    A_star=O((R*/(L*)^2)2^f(R*)),
    Qcap=O(n^(3/2)(log2 n)^(-2)2^f(R*)).                (2)

This is a uniform maximum over actual widths; it does not presume
monotonicity of rounded integer schedules. Its constants include the
finite slack guard and all fixed-width trees.

## 5. Joint success and deterministic resources

The new widths and slack guard are predetermined public parameters.
All selection maps still inspect only the low prefix and remain
injective, preserving the source's freshness and top-bit laws. The
actual log root size is O(sqrt n), so the source-aligned decoder's
proof still gives G_odd=O(n). Its phase shifts, source multipliers,
mode test and precision use the actual tree size. The retry product
below four gives expected tree demand <=8 A_star. Reach-probability
accounting is valid even when an attempt's cost correlates with success.
The same root/parity argument establishes Q_star, and Markov adds
cutoff error <=2^-10. The unchanged collective-extractor coupling,
seed/backward/parity errors and finite exhaustive branch retain the
source's total error bound below 2^-8. These are unconditional
first-error/cutoff comparisons, not conditioning on perfect labels
or passing a cap.

The deterministic per-copy tree charge is
O(n(m+1)2^kappa 2^x/q), including every failed attempt and any final
partial tree. Here 2^kappa<=2^17. Uniformly over actual widths,
monotonicity of 2^v/(v+3) gives

    2^x/q=O(2^g(R*)/g(R*)).

For guarded finite widths x and q are bounded constants, absorbed
by the same asymptotic bound. As m=O(sqrt n), the per-copy charge is
O(n(log2 n)^2 2^g(R*)). Multiplication by the actual cap (2) gives

    tree core work=O(n^(5/2)2^(R*+R*/(L*)^4)).           (3)

Source transforms and collective label extraction cost O(n^2) per
copy and are smaller after retaining the negative g(R*) in (2).
Seed scoring is O(n^2 A_star) plus polynomial setup and is also
smaller. All feedback, rational arithmetic, source acquisition,
initialization, circuit generation, explicit lookups, measurements,
resets, disposal, incorrect-label branches and aborted work are counted.
The additional finite-width slack changes these bounds only by the
explicit fixed factor 2^17, not an unknown exponent coefficient.

The quantum stack and active scratch are O(n), since m<=mu and
all lam_i=O(sqrt n), with kappa<=17. Classical high-part fields
have width w_i=B+1+i+ceil(log2 q)-p_i=O(sqrt n(m-i+1)). The s
plateau levels sum to O(sqrt n s^2 2^lambda_max); growing levels
form a smaller geometric tail. Here lambda_max=kappa+1+m and
2^kappa is uniformly bounded, while s=O(g(R*)) uniformly apart
from finitely many bounded widths. Common residues, merge scratch,
source/extractor records and all other polynomial scratch are included.
Consequently

    S_C=O(n^(3/2)(log2 n)^(-4)2^f(R*)).                  (4)

The exponential is eventually positive of order sqrt n and absorbs
polynomial-only scratch and the finite prefix. Address length is
O(sqrt n), turning (3) into total charged work

    T=O(n^3 2^(R*+R*/(L*)^4)).                          (5)

Equations (2),(4),(5) and O(n) qubits hold jointly on every branch
of this one configuration, including every cutoff and earlier mistake.

## 6. Exact structured coefficients and scope

Let t=log2 n, so R*=sqrt2 sqrt n and L*=(t+1)/2. Then

    R*/(L*)^4=16sqrt2 sqrt n/(t+1)^4<=23sqrt n/t^4,

using sqrt2<10/7. Also for t>=128,
56t^2>=55(t+1)^2, because t^2-110t-55 is positive at 128
and increases thereafter. Since sqrt2>7/5,

    4sqrt2/(t+1)^2>=(11/2)/t^2.

Therefore f(R*)<=sqrt2 sqrt n-(11/2)sqrt n/t^2+23sqrt n/t^4.
Replace only the leading sqrt2 by the exact larger a. This proves
exactly E,F and the outer powers in the theorem. The finite n<2^128
prefix receives a positive representative extension and an absolute
outside constant; the executed algorithm and all success/cap instructions
are unchanged there. Each exponential logarithm is a sqrt n+o(sqrt n),
so its exact index is 1/2; linear quantum space has index zero.

The rational logarithm and balanced-family accounting develop this
session's CYCLIC-LOG/CYCLIC-ROOTLOG work. The complete cyclic-window
source is direct material reuse of e9fc2eca-9d1c-469b-a629-a43e0f7ce928.
The finite-width slack guard and gamma=2 precision, retry and analytic
estimates are rechecked here, rather than invoking a gamma<=1 lemma
outside its range. This is a faster-time/weaker-memory-source tradeoff,
not a lower growth index, a practical runtime claim or global frontier
leadership. The research target of time index 1/3 is not established.
