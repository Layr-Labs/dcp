# CYCLIC-LOG: balanced logarithmic boost and plateau

## 1. Algorithm and joint theorem

For every N>=2 and s in Z/NZ, let n=ceil(log2 N). Use the complete
cyclic-window, source-aligned algorithm supplied in cyclic_base.md, with
the schedule, retry coefficient and resource conclusions replaced below.
The included source is unmodified from submission
e9fc2eca-9d1c-469b-a629-a43e0f7ce928, candidate
45d9985c85813b2f3d30c62c717faba3621eb57a. Its fixed16 theorem concerns
its original configuration, not this one. All its circuits, source
identities, low-prefix collision proof, top-bit law, collective extractor,
general-modulus backward decoder and finite branch are included in full.
No prior acceptance verdict is a mathematical premise.

One fixed CYCLIC-LOG configuration outputs the entire s with unconditional
probability at least 1-2^-8, and on EVERY branch obeys jointly

    T=O(n^3 2^E(n)), S_C=O(n^(3/2)(log2 n)^(-2)2^F(n)), S_Q=O(n),
    Q=O(n^(3/2)(log2 n)^(-1)2^F(n)),
    E(n)=a sqrt(n)+6 sqrt(n)(log2 n)^(-2),
    F(n)=a sqrt(n)-(5/2)sqrt(n)(log2 n)^(-1)
                      +6 sqrt(n)(log2 n)^(-2).

Here a is exactly u_333/v_333 defined with its Pell recurrence in the
included source's Section 0; that recurrence proves a>sqrt2. Every
constant is absolute. These are eventual representative envelopes;
assign any positive values on n<512, where the asymptotic expressions
need not be evaluated. The algorithm and its success guarantee still
apply to every N. This finite extension does not affect big-O or the
structured asymptotic comparison. The indices are 1/2,1/2,0,1/2.
The fractional malformed-copy guarantee is epsilon(n)=0 under independent
ideal copies; no maximum possible tolerance or positive robustness is
claimed. Q counts every acquisition, rejection, failure and discard.

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

Define

    h(mu)=max(2,floor(mu/ell(mu))).

For mu>=4, the function mu/log2(mu) is at least two, and the precision
bound gives the useful sharp estimates

    mu/log2(mu)-2 <= h(mu) <= mu/log2(mu).             (1)

Indeed ell<=L+1/mu implies mu/ell>=mu/L-1/L^2, and taking the floor
loses less than one. The max with two respects the upper bound for
mu>=4. At mu=3 use h=2, as the same rational prescription specifies.

## 3. Balanced schedule, capacity and retry bound

For B=D-1>=1 compute

    mu=ceil(sqrt(2B))+1, kappa=2,
    x=s=h(mu), q=x+3,
    C(z)=z(z+1)/2-s(s-1)/2+x(z+1)+2,
    m=min{z>=s+1:C(z)>=B}.

Keep the source's exact boosted lengths, residue capacities, greedy
allocation, leaf sum tables, cyclic-window instrument and depth-first
VEC recursion with these x,s. The function h gives 2<=x<=mu-1:
this is immediate for mu=3, while log2(mu)>=2 for mu>=4 and
h<=mu/log2(mu)<=mu/2. Hence the depth constraint is well defined.
At z=mu, C(mu)>=mu^2/2>=B because x=s<=mu makes the extra
term x mu-x^2/2 nonnegative. Thus m<=mu. Adding the source's
three capacity regimes gives sum bmax_i=C(m), and substitution gives
bmax_i+lam_(i+1)-2lam_i=-2. The greedy allocation exists.

The cyclic-window merge and the low-prefix conditioning are unchanged.
All inspected bits lie below the retained top bit and the selected
incidences remain distinct. The source's independent-high-block collision
proof therefore gives fresh non-root failure <2^-q after averaging the
whole fresh child pair under that invariant; the root has its separate
distribution-free bound <=1/4. No fixed-full-table bound is assumed.

We always have q>=5 and m2^-q<=1/2. For 3<=mu<16 use m<=15
and q>=5. For mu>=16, (1) gives
q>=mu/log2(mu)+1>=log2(mu)+1, since log2(mu)<=sqrt(mu).
Together with m<=mu this gives the claimed bound. Since
-ln(1-p)<=2p for p<=1/32, the retry product is at most
(4/3)e<4. The fresh-attempt, reach-probability cost argument is the
one fully supplied in cyclic_base.md; it does not assume independence
of an attempt's cost and its success.

Replace the literal cap by

    A_star=max_(1<=B<=n) q(B)2^m(B),
    Q_star=8 A_star(G_odd+2a2)+2a2,
    Qcap=1024 Q_star.

Compute this exact integer maximum and the actual decoder tree size
before acquiring copies. All decoder grids, its small/large mode test,
and extractor confidence use those actual values. Computing h for at
most n widths takes polynomial setup work and polynomial-only scratch,
which are charged. Logarithm rationals are released between widths;
no uncharged table of parameters is needed.

## 4. Smooth depth, table and leaf bounds

Only for analysis let R=sqrt(2B), L=log2 R, and g(R)=R/log2 R.
For R>=4, g is increasing and 0<g'(R)<=1/2. Since
R+1<=mu<=R+2, (1) implies

    g(R)-2<=x<=g(R)+2, q<=4g(R).                      (2)

The latter uses g(R)>=2. Completing the square bounds m by the maximum
of s+1 and ceil(sqrt(R^2+s^2+(x+1/2)^2)-x-1/2).
Because x=s, concavity gives the square-root candidate plus x at most

    R+x^2/R+x/(2R)+1/(8R)+1.

By (2), x^2/R<=R/L^2+4/L+4/R<=R/L^2+3 for R>=4,
and the remaining terms are bounded by an absolute constant.
The lower constraint also fits: since x<=mu/log2(mu)<=mu/2,
s+1+x=2x+1<=mu+1<=R+3. Consequently

    m+x<=R+R/L^2+C,
    m<=f(R)+C, f(R)=R-R/L+R/L^2                      (3)

with a uniform absolute C, enlarged for the finitely many B with R<4.
For L>=2,

    f'(R)=1-1/L+1/L^2+(1/ln(2))(1/L^2-2/L^3)>0.

Thus f and g are increasing in the range used for the asymptotic maximum.
Equations (2)--(3) give, with R*=sqrt(2n), L*=log2 R*,

    A_star=O((R*/L*)2^f(R*)),
    Qcap=O(n^(3/2)(log2 n)^(-1)2^f(R*)).              (4)

Fixed small-width trees contribute a constant absorbed in this bound;
no monotonicity of the rounded integer schedule is assumed.

## 5. Correctness and every-branch resources

The actual log root size is O(sqrt n), since m<=mu and q=O(sqrt n).
The included source's size-selected, source-aligned decoder therefore
still uses G_odd=O(n) roots in expectation. Its seed and feedback use
the new actual tree size. Its low-prefix, top-bit and pointwise odd-W
arguments are unchanged. With the retry constant below four, a returned
tree uses at most 8 A_star source copies in expectation. The same
reach-probability and parity argument proves Q_star is an expectation
bound before imposing the cutoff. Markov adds error <=2^-10.
The collective label coupling, seed/backward decisions, explicit parity
caps and finite exhaustive branch retain the source's remaining error
budget, whose total is <2^-8. This proves the unconditional joint
success claim, without conditioning on ideal extraction or cap success.

The deterministic tree core-work charge per acquired copy is
O(n(m+1)2^kappa 2^x/q). Every copy has at most one ancestor merge at
any level because failed inputs are discarded. For all actual widths,
x<=g(R*)+2 up to a fixed constant covering small widths. The function
2^v/(v+3) is increasing for v>=1, so

    2^x/q=O((L*/R*)2^g(R*)).

With m=O(sqrt n), the common charge is
O(n log n 2^g(R*)). Multiplying by the actual cutoff (4) yields

    tree core work=O(n^(5/2)2^(R*+R*/(L*)^2)).          (5)

The O(n^2) source-transform and collective-extraction cost per copy
is smaller: its extra polynomial factor is dominated by the retained
negative R*/L* in (4). Seed scoring is O(n^2 A_star) plus polynomial
setup and is also smaller. Uniform arithmetic, feedback, initialization,
measurements, resets, disposal, circuit generation and failed/aborted
work are included as in the source's complete resource ledger.
Explicit source cost (n+1)Qcap is charged and is below (5).

The quantum stack and all active scratch remain O(n) because m and
all lam_i are O(sqrt n). We use the actual stored high-part widths to
bound classical storage more sharply than a full n-bit field at every
level. A level-i field has width

    w_i=B+1+i+ceil(log2 q)-p_i,
    B-p_i=sum_(j=i)^(m-1) b_j.

Every b_j and m are O(sqrt n), so
w_i=O(sqrt n (m-i+1)), uniformly for all actual B<=n and branches.
There are only a constant number of resident tables at any level in
depth-first evaluation, including the current merge and output. Write
t=m-s and lambda_max=3+x+t. For plateau levels i=t,...,m-1,
their table lengths are 2^lambda_max, and the sum of their widths is
O(sqrt n sum_(d=1)^s(d+1))=O(sqrt n s^2). Growing levels i=t-d
have lengths 2^(lambda_max-d) and widths
O(sqrt n (s+d+1)); summing their geometric tail costs only
O(sqrt n (s+1)2^lambda_max). Common residues add O(nm) bits.
Merge scratch costs O(sqrt n 2^lambda_max); root records and all other
scratch are polynomial and separately included. Since x=s,
lambda_max=3+m. Also s=O(R*/L*) uniformly. Thus the whole stack obeys

    S_C=O(n^(3/2)(log2 n)^(-2)2^f(R*)).                 (6)

Polynomial scratch and the finite prefix are absorbed in absolute
outside constants. Address length is O(sqrt n), giving total work

    T=O(n^3 2^(R*+R*/(L*)^2)).                         (7)

All caps are literal and fixed before acquisition. These bounds are
simultaneous for every execution branch, including incorrect labels
and early decoder mistakes, not expected work conditional on success.

## 6. Exact rational envelopes and scope

Let t=log2 n. Then R*=sqrt2 sqrt n, L*=(t+1)/2. Since sqrt2<3/2,

    R*/(L*)^2=4sqrt2 sqrt n/(t+1)^2<=6 sqrt n/t^2.

This and a>sqrt2 give E for total work. For the other exponential
bound, sqrt2>7/5 and sqrt2<3/2 imply

    f(R*)/sqrt n
       <=sqrt2-(14/5)/(t+1)+6/(t+1)^2
       <=sqrt2-(5/2)/t+6/t^2,  t>=9.

The last step uses (14/5)t>=(5/2)(t+1) for t>=9 and
(t+1)^(-2)<=t^(-2). Replacing sqrt2 by the exact larger a gives F.
Also R*/L*=O(sqrt n/log2 n), proving the stated sample prefactor.
The finite n<512 prefix is assigned positive representative values
and covered by an absolute constant. All algorithmic guarantees still
hold there. No finite-prefix numerical fit is used.

The structured objects therefore have exactly the leading term
(a,1/2,0), the time correction (6,1/2,-2), and for classical memory
and samples the additional term (-5/2,1/2,-1), with the displayed
outer n/log powers. Each exponential logarithm is a sqrt n+o(sqrt n),
so its exact growth index is 1/2. The quantum envelope n has index 0.
No unknown coefficient inside an exponent is assigned a value.

The complete cyclic-window/source-aligned machinery is material reuse
of e9fc2eca-9d1c-469b-a629-a43e0f7ce928. The balanced growing boost
and plateau develop this session's CYCLIC-GCAP-D construction. Here
a one-sided rational logarithm calculation makes the sizes smooth to
within an absolute additive constant, avoiding an extra uncharged
rounding loss in the time exponent. This is a new explicit resource
tradeoff at index 1/2, not a solution of the 1/3 research goal or a
claim of global frontier membership.
