# CYCLIC-LOGSCALE: a scaled logarithmic boost with a curvature ledger

## 1. Complete fixed algorithm and theorem

Use the complete source-aligned cyclic-window algorithm supplied unchanged
as cyclic_base.md, from e9fc2eca-9d1c-469b-a629-a43e0f7ce928, commit
45d9985c85813b2f3d30c62c717faba3621eb57a. The full logarithmic schedule
and counted rational series are supplied as log_base.md, from CYCLIC-LOG
1f1debc0-0a4b-409c-bcc4-1eb8c5c9d470, commit
07a195ac7f4dbfc975beddec776c818994c936d1. Replace their parameters,
retry coefficient and resource conclusions explicitly by the following.
Both full arguments are included; previous verdicts are not premises.

Write ln for the natural logarithm; all log2 notation is base two. Fix
c=8/9. For every requested collimation width B compute, before acquisition,

    mu=ceil(sqrt(2B))+1, ell=the rational log of log_base.md Section 2,
    x=s=max(2,floor(8mu/(9ell))),
    kappa=ceil(log2 mu)+1 if mu<32, and 2 otherwise,
    q=kappa+1+x,
    m=min{z>=s+1:z(z+1)/2-s(s-1)/2+x(z+1)+kappa>=B}.

For ell=r/d, the floor is exact integer division floor(8mu d/(9r)).
The finite guard uses exact bit lengths and kappa<=6. Retain the full
source's generic boosted lengths, capacities, greedy allocation, leaf
sum tables, cyclic rank instrument, failed-input disposal, source transforms,
collective labels, actual-size-selected backward decoder, 2-adic procedure
and finite n<64 exhaustive branch, at these actual x,s,kappa. Recompute
every decoder/extractor confidence and size parameter. Set literally

    A_star=max_(1<=B<=n) q(B)2^m(B),
    Q_star=8 A_star(G_odd+2a2)+2a2, Qcap=1024 Q_star.

For every N>=2 and every s in Z/NZ, n=ceil(log2 N), this ONE configuration
recovers the entire s with unconditional success at least 1-2^-8 under
independent ideal copies. Jointly on every execution branch,

    T=O(n^3 2^J(n)),
    S_C=O(n^(3/2)(log2 n)^(-2)2^F(n)), S_Q=O(n),
    Q=O(n^(3/2)(log2 n)^(-1)2^F(n)),
    J(n)=a sqrt(n)+(9/2)sqrt(n)/(log2 n)^2
                   -7sqrt(n)/(log2 n)^4
                   +23sqrt(n)/(log2 n)^6,
    F(n)=a sqrt(n)-(5/2)sqrt(n)/(log2 n)
                   +6sqrt(n)/(log2 n)^2.

The exact Pell rational a=u_333/v_333 is in cyclic_base.md Section 0,
with its proof a>sqrt2. All constants are absolute, independent of N,s
and outcomes. Use these eventual positive representative envelopes for
n>=2^1024 and extend them positively on the finite smaller prefix;
algorithmic correctness covers every N. Exact indices are 1/2,1/2,0,1/2.
Malformed fraction is zero under independent ideal copies, not a maximum
possible tolerance claim. Failed/discarded/cutoff-abandoned copies count.

## 2. Precision, valid windows and unconditional recovery

The supplied rational-series calculation proves
L_mu<=ell<=L_mu+1/mu, L_mu=log2 mu, with polynomial charged work and
operand bit lengths in log(mu). For mu>=32, flooring and the derivative
of 1/v give

    c mu/L_mu-2<=x<=c mu/L_mu.                        (1)

The max with two respects the upper bound in this range. For all mu>=3,
2<=x=s<=mu-1. Capacity holds at z=mu since x=s and
x mu-x^2/2 is nonnegative, hence m<=mu. Use explicitly
lambda_i=kappa+1+x+min(i,m-s) below the root and lambda_m=1;
bmax_i=x+i on growing levels, x+m-s+1 on capped levels, and
kappa+2x+2(m-s)+1 at the root. Their sum is the stated capacity and
bmax_i+lambda_(i+1)-2lambda_i=-kappa. Every selected window is in
the B-bit low prefix. The source's injective rank maps and conditional
independent-high-block collision proof therefore apply, giving fresh
non-root failure <2^-q for kappa>=2 and root failure <=2^-kappa<=1/4.
The non-root bound uses fresh whole-child averaging, not arbitrary
fixed full high label tables. The retained high top bit stays untouched.

If mu<32, 2^kappa>=2mu and q>=kappa+3 give m2^-q<=1/16.
If mu>=32, the ratio mu/L_mu^2 increases with L_mu>=5, since
ln2-2/L_mu>0. Its value after multiplication by c at five is
256/225>1. Thus c mu/L_mu>=L_mu, and (1) gives q>=L_mu+1;
again m2^-q<=1/2. Always q>=5. From -ln(1-p)<=2p for p<=1/32,
the retry product is at most (4/3)e<4. The fixed factor 2^kappa<=64
is included in the work and space constants, not dropped from the algorithm.

Fresh-whole-attempt reach-probability accounting gives expected tree
acquisitions <=8 A_star without requiring independence of attempt cost
and success. The actual log root size remains O(sqrt n), so the supplied
source-aligned decoder retains its O(n) expected-root bound. Recomputed
Q_star bounds the uncapped ideal expectation, and Markov adds <=2^-10
cutoff error. The full source's collective-label extraction coupling,
seed/backward/parity error budgets, literal parity caps and finite branch
keep total failure below 2^-8. These are unconditional first-error and
cutoff comparisons. Wrong-label branches obey the same fixed widths and
caps; no resource or success argument conditions on perfect extraction.

## 3. Exact profile and uniform maxima

For R=sqrt(2B)>=32 let L=log2 R, u=c/L, g(R)=R u,
S=sqrt(1+2u^2). Then 0<g'<1. As R+1<=mu<=R+2, (1) gives

    g(R)-2<=x<=g(R)+2, q<=4g(R).                     (2)

The square-root candidate obtained by completing the capacity square is
ceil(sqrt(R^2+s^2+(x+1/2)^2-2kappa)-x-1/2); dropping the negative
term only increases it. The depth is bounded by the maximum of that
candidate and s+1. Since u^2<1/2, 2u<=S, so the lower constraint plus
x is <=R S+5. For the square-root candidate, the positive radicand
excess over R^2+2g^2 is <=9R+41/4 by x<=g+2 and g<=R.
Dividing by the sum of square roots gives a difference less than five,
and the ceiling costs at most one. Therefore, with C0=1024,

    m+x<=R S+C0, m<=h(R)+C0+2, h(R)=R(S-u).          (3)

This also covers all finite widths with R<32 directly from m<=mu and
x<=mu-1. With eta=1/(ln(2)L)<3/4,

    h'=S-u-eta*u*(2u/S-1)>3/8.

Indeed S-u>1/2, since S^2-(u+1/2)^2=(u-1/2)^2+1/2>0;
and 2u/S<=2/sqrt3<7/6 for u<=1. If 2u/S-1 is negative the last
term helps, otherwise its magnitude is <1/8. Thus h is increasing
on R>=32. No rounded-profile monotonicity is presumed. For
R*=sqrt(2n), L*=log2 R*, g*=g(R*), h*=h(R*), the literal maximum gives

    A_star=O(g*2^h*), Qcap=O(n g*2^h*).               (4)

Finite guarded widths are absorbed by an absolute constant. Computing
the exact maximum and rational parameters uses counted polynomial setup.

## 4. Deterministic work, space and retained resource budgets

The source's deterministic per-acquisition charge is
O(n(m+1)2^kappa 2^x/q). Every failed input is discarded, so each
acquisition pays at most one merge per level. By (2), the increase of
2^v/(v+3), m=O(sqrt n) and 2^kappa<=64, the common charge is
O(n^(3/2)2^g*/g*). Multiplication by the ACTUAL cutoff (4) yields
O(n^(5/2)2^(R*S*)) tree core work. The O(n^2) per-copy source
transforms and collective extraction are smaller by the negative g*
in h*. Seed scoring O(n^2 A_star), feedback and polynomial setup are
also smaller. All initialization, circuit generation, lookups, source
cost, measurements, reset/disposal, failed attempts, wrong-label branches
and abandoned work are counted. Address length is O(sqrt n), giving

    T=O(n^3 2^(R*sqrt(1+2c^2/(L*)^2))).              (5)

The depth-first quantum stack and scratch use O(n) qubits. Classical
high-part field widths are O(sqrt n(m-i+1)). The s plateau levels sum
to O(sqrt n s^2 2^lambda_max), with a smaller geometric growing-level
tail. Here lambda_max=kappa+1+m, kappa<=6 and s=O(g*), so classical
bits are O(n^(3/2)(log2 n)^(-2)2^h*). All polynomial scratch, extractor
records, residues and seed scores are included. Sample prefactor in
(4) is n^(3/2)(log2 n)^(-1).

Using S<=1+u^2 in (3), the exponent is bounded by

    h(R)<=R-c R/L+c^2 R/L^2.                         (6)

For t=log2 n>=1024, sqrt2>140/99 and
25t>=4455 imply

    2sqrt2 c/(t+1)>=(5/2)/t.

Also 4sqrt2 c^2/(t+1)^2<=6/t^2, since sqrt2<99/70.
Thus h*<=F(n) after replacing only the leading sqrt2 by a. This proves
the exact retained memory and source guarantees for the same fixed
configuration. Actual memory/source use may grow when reducing the
boost; preservation of declared guarantees is the claim.

## 5. Explicit curvature time bound

For z>=0, P(z)=1+z-z^2/2+z^3/2 is positive and

    P(z)^2-(1+2z)=(z^4/4)(z^2-2z+5)>=0.

Consequently sqrt(1+2z)<=P(z). Apply this to z=c^2/(L*)^2
in (5). With t=log2 n the exponent is at most

    sqrt2 sqrt n+4sqrt2 c^2 sqrt n/(t+1)^2
         -8sqrt2 c^4 sqrt n/(t+1)^4
         +32sqrt2 c^6 sqrt n/(t+1)^6.

The exact rational bounds sqrt2<99/70 and sqrt2>140/99 give

    4(99/70)c^2<9/2, 32(99/70)c^6<23,
    8(140/99)c^4*1024^4>7*1025^4.

Because (t/(t+1))^4 increases, the last inequality holds for all
t>=1024. Hence the negative term is <=-7sqrt n/t^4, while the
positive terms are bounded by (9/2)sqrt n/t^2 and 23sqrt n/t^6.
Replace only the leading sqrt2 by a to obtain exactly J(n).
Finite smaller n receive positive representative extensions and absolute
outside constants without changing the actual all-N success guarantee.

Every exponential logarithm is a sqrt n+o(sqrt n), so exact index is
1/2; O(n) quantum space has index zero. Compared with CYCLIC-LOG,
all other declared envelopes and the clean-copy model are identical,
and the old-minus-new time exponent is

    (3/2)sqrt n/t^2+7sqrt n/t^4-23sqrt n/t^6,

which tends to positive infinity. The algorithm actually changes its
boost scale and uses a finite slack guard. This is a strict improvement
of the proved time guarantee, not tight resource dominance, finite-size
speed or global frontier leadership. Time index 1/3 is not achieved.

## 6. Provenance

The full original cyclic algorithm and full rational-log predecessor
are included. The exact-square-root maximum/derivative and polynomial
curvature framework are developed from CYCLIC-QSCALE in this session.
Direct material predecessors are declared with published IDs, exact
submission/ archive paths, hashes and both-endpoint citations at upload.
No prior verdict or finite arithmetic test is a mathematical premise.
