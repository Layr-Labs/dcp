# CYCLIC-HALFTRIM: a lower-order trim of the balanced square-root-log boost

## 1. Full construction and simultaneous theorem

The complete cyclic-window/source-aligned algorithm is supplied in
cyclic_base.md, unchanged from e9fc2eca-9d1c-469b-a629-a43e0f7ce928,
commit 45d9985c85813b2f3d30c62c717faba3621eb57a. The complete balanced
rational-logarithm family proof is supplied as rootlog_base.md, from
CYCLIC-ROOTLOG 7dbdb6dc-54c1-4759-82e8-e8dc4743d94b, commit
e14083d26279ab6e6857f1b611d0c0beec0b1045. Both full arguments are
included. Prior verdicts are not premises. Replace their parameter choice,
resource conclusions and retry coefficient by the following single choice.

Write ln for the natural logarithm, log2 for base two. For each collimated
width B, compute mu=ceil(sqrt(2B))+1 and the exact rational ell(mu) in
rootlog_base.md Section 2. Fix beta=3/64, kappa=2 and

    x=s=max(2,floor(mu/sqrt(ell)-beta mu/ell)), q=x+3,
    m=min{z>=s+1:z(z+1)/2-s(s-1)/2+x(z+1)+2>=B}.

This uses integer arithmetic: for ell=r/d, the floor before the max is
the largest integer v>=0 satisfying

    (64 v r+3 mu d)^2 <= 4096 mu^2 r d.

The expression on the left is nonnegative and increasing in v. The
unrounded expression is positive for ell>=1, so v exists. Binary search
on [0,mu] with exact integer products takes polynomial work and bits in
log(mu), including the counted rational series. Retain all source circuit,
leaf, merge, allocation, failure-disposal, extractor, backward-decoder,
2-adic and finite n<64 procedures with these actual parameters. Recompute
all actual tree-size-selected grids, precision and confidence parameters.
Set literally

    A_star=max_(1<=B<=n) q(B)2^m(B),
    Q_star=8 A_star(G_odd+2a2)+2a2, Qcap=1024 Q_star.

For every N>=2 and every s in Z/NZ, n=ceil(log2 N), this ONE algorithm
recovers the entire s with unconditional probability at least 1-2^-8.
Its joint bounds on every branch are

    T=O(n^3 2^J(n)),
    S_C=O(n^(3/2)(log2 n)^(-1)2^F(n)), S_Q=O(n),
    Q=O(n^(3/2)(log2 n)^(-1/2)2^F(n)),
    J(n)=a sqrt(n)+(20/7)sqrt(n)/(log2 n)
           -(1/3)sqrt(n)/(log2 n)^(3/2)
           +(1/64)sqrt(n)/(log2 n)^2,
    F(n)=a sqrt(n)-2sqrt(n)/(log2 n)^(1/2)
           +3sqrt(n)/(log2 n).

Here a=u_333/v_333 is the exact Pell rational from cyclic_base.md
Section 0, which proves a>sqrt2. Constants are absolute, independent of
N,s and outcomes. These eventual representative envelopes are evaluated
for n>=2^1024 and extended positively on the finite smaller prefix.
Correctness still covers all N. Exact indices are 1/2,1/2,0,1/2.
The malformed fraction is 0 under independent ideal copies, with no
maximum-tolerance assertion. Every acquired and discarded copy is counted.

## 2. Rounding, capacity, freshness and literal caps

The supplied rational series proves L_mu<=ell<=L_mu+1/mu, with
L_mu=log2(mu). Let v(L)=L^(-1/2)-beta L^(-1). For L>=2,
v>0, v'<0, and |v'|<=1/2. The mean value theorem and flooring give

    mu v(L_mu)-2 <= x <= mu v(L_mu)                  (1)

for mu>=4. The max with two respects this upper bound: mu v(log2 mu)
is increasing there and its value at four exceeds two. At mu=3 the
actual instruction gives x=2. Thus 2<=x=s<=mu-1 always. Capacity holds
at m=mu, since x=s makes the extra term x mu-x^2/2 nonnegative;
hence m<=mu. The three exact residue-capacity regimes and merge slack
bmax_i+lambda_(i+1)-2lambda_i=-2 of the full source still hold. All
selected windows stay in the exposed low prefix; rank maps remain
injective. The conditional independent-high-bit collision and retained
top-bit proofs therefore continue to apply. Fresh non-root failure is
<2^-q under whole-child averaging; root failure is <=1/4. This does
not assert a bound for every fixed full non-root label table.

For mu<16, m<=15 and q>=5 give m2^-q<1/2. For mu>=16,
mu/L_mu^(3/2) increases with L_mu>=4 and is two at four, while
1-beta/sqrt(L_mu)>=1-beta/2=125/128. Thus
mu v(L_mu)>=L_mu, and (1) gives q>=L_mu+1. Again m2^-q<=1/2.
Using -ln(1-p)<=2p for p<=1/32 gives retry product at most (4/3)e<4.
Fresh-whole-attempt reach-probability accounting, without independence
of attempt cost and success, gives expected tree acquisitions <=8 A_star.

Since log2(q2^m)=O(sqrt n), the actual-size source-aligned decoder retains
its O(n) expected-root budget. The actual Q_star is an uncapped ideal
expectation bound and Markov adds <=2^-10 acquisition-cutoff error.
The full source's collective extraction coupling, seed/backward errors,
parity caps and finite exhaustive branch keep total failure below 2^-8.
These are unconditional first-error and cutoff comparisons, including
wrong-label branches. Every literal resource cap is enforced on every
branch, with no conditioning on successful extraction or avoiding cutoff.

## 3. Exact depth profile and maxima over all requested widths

For analysis put R=sqrt(2B)>=4, L=log2 R, u=v(L), g(R)=R u and
S=sqrt(1+2u^2). Differentiation gives

    g'=u(1-eta),
    eta=[1/(2 ln(2)L)](1-2beta/sqrt L)/(1-beta/sqrt L).

Since L>=2 and ln2>2/3, 0<eta<3/8. Also 0<u<1, so 0<g'<1.
With R+1<=mu<=R+2, (1) implies

    g(R)-2<=x<=g(R)+2, q<=4g(R).                     (2)

Here g>=2 for R>=4. Completing the capacity square bounds m by the
maximum of s+1 and ceil(sqrt(R^2+s^2+(x+1/2)^2)-x-1/2).
For R>=16, u^2<=1/4, hence 2u<=S. The lower constraint plus x is
therefore <=R S+5. For the square-root candidate, x<=g+2 and g<=R
bound the difference of radicands from R^2+2g^2 by 9R+41/4.
Dividing by the sum of square roots bounds their difference by less
than five for R>=16; the ceiling costs at most one. Consequently

    m+x<=R S+64, m<=h(R)+66, h(R)=R(S-u).             (3)

The fixed constants also cover the finitely many smaller B directly
using m<=mu. Moreover

    h'=S-u-eta*u*(2u/S-1)>3/8.

Indeed S-u>1/2 since S^2-(u+1/2)^2=(u-1/2)^2+1/2>0; and
2u/S<=2/sqrt3<7/6 for u<=1, while eta<3/4. If the last parenthesis
is negative its contribution only helps; otherwise its magnitude is
less than (3/4)/6. This proves monotonicity for every R>=4.
Thus no rounded integer profile is assumed monotone. For R*=sqrt(2n),
L*=log2 R*, g*=g(R*), h*=h(R*), exact maximization in the cap yields

    A_star=O(g*2^h*), Qcap=O(n g*2^h*).               (4)

Fixed small widths are absorbed by an absolute constant. g* is
Theta(sqrt(n)/(log2 n)^(1/2)). All setup and maximization work is counted.

## 4. Every-branch charge and retained memory/sample guarantees

The deterministic charge per acquired copy is
O(n(m+1)2^kappa 2^x/q). Failed inputs are discarded, so each acquisition
pays at most one merge per level. By (2), monotonicity of 2^v/(v+3)
and m=O(sqrt n), the common charge is O(n^(3/2)2^g*/g*).
Multiplying by the ACTUAL cutoff (4) gives tree core work
O(n^(5/2)2^(R*S*)). Source transforms and collective labels cost O(n^2)
per copy and are smaller by the negative g* in h*. Seed scoring
O(n^2 A_star), feedback and polynomial rational setup are also smaller.
All initialization, measurements, disposal, explicit lookups, circuit
generation, wrong-label work, failed attempts and abandoned subtrees
are included. Address length is O(sqrt n). Therefore

    T=O(n^3 2^(R*sqrt(1+2u*^2))).                     (5)

The active quantum stack and scratch use O(n) qubits, as m and all index
lengths remain O(sqrt n). Stored high-part fields have width
O(sqrt n(m-i+1)). The s plateau levels sum to
O(sqrt n s^2 2^lambda_max), with a smaller geometric growing-level tail.
Since x=s, lambda_max=m+3, and s=O(g*), this gives classical bits
O(n^(3/2)(log2 n)^(-1)2^h*). Polynomial scratch, extractor records and
seed scores are separately included and absorbed by this exponential.
Equation (4) gives sample prefactor n^(3/2)(log2 n)^(-1/2).

It remains to compare h* to the exact retained target F. Using
S<=1+u^2 in (3) gives

    m<=R-R/L^(1/2)+(1+beta)R/L
         -2beta R/L^(3/2)+beta^2 R/L^2+66.           (6)

Let t=log2 n. Relative to sqrt2 sqrt n-2sqrt n/sqrt t, the first
negative term costs at most sqrt n/t^(3/2): indeed
2(1/sqrt t-1/sqrt(t+1))<=1/t^(3/2) by integrating v^(-3/2).
Discard the further negative term in (6). It suffices that

    1/sqrt t+2sqrt2(1+beta)+4sqrt2 beta^2/t <=3.

For t>=1024 use sqrt2<99/70 to bound the middle term by 6633/2240,
the first by 1/32 and the last by 1/65536. Their exact rational sum
is less than three. Thus h*<=F(n)+O(1), replacing only the leading
sqrt2 by a. All retained memory and sample envelopes follow jointly
for this same configuration. Trimming can increase actual source and
memory use; the claim is preservation of these declared upper bounds.

## 5. Work improvement with an explicit negative lower-order term

Concavity sqrt(1+2z)<=1+z for z>=0, applied to (5), gives exponent

    R+R/L-2beta R/L^(3/2)+beta^2 R/L^2.

For t=log2 n this is exactly

    sqrt2 sqrt n +2sqrt2 sqrt n/(t+1)
        -(3/8)sqrt n/(t+1)^(3/2)
        +4sqrt2 beta^2 sqrt n/(t+1)^2.

Use 2sqrt2<20/7, and 4sqrt2 beta^2<1/64. For t>=16,
81t^3>=64(t+1)^3, because (1+1/t)^3 decreases and at t=16
its value is less than 81/64. Taking positive square roots gives
(3/8)/(t+1)^(3/2)>=(1/3)/t^(3/2). Replacing the leading sqrt2
by a proves exactly J(n). The more conservative common threshold
t>=1024 also proves the other bounds. The finite smaller n receive
positive representative extensions and absolute outside constants,
while the actual finite algorithms still apply.

All exponential logarithms are a sqrt n+o(sqrt n), so their exact
index is 1/2; the linear quantum-space index is zero. Relative to
CYCLIC-ROOTLOG, the declared quantum/classical/sample envelopes and
clean-copy model are identical. Its old-minus-new time exponent is

    (1/7)sqrt n/t+(1/3)sqrt n/t^(3/2)
                   -(1/64)sqrt n/t^2,

which tends to positive infinity. This is a strict improvement of the
proved time guarantee, not a tight-cost or practical-runtime assertion.
The algorithm actually changes its integer boost by an unbounded
lower-order amount, and the proof charges that change. No index-1/3
algorithm or leadership over the global frontier is established.

## 6. Material sources

The full rational-logarithm and balanced-family derivation is supplied
as rootlog_base.md; the full cyclic-window/circuit/decoder derivation
is supplied as cyclic_base.md. The exact-square-root maximum and derivative
ledger is developed from the CYCLIC-QSCALE analysis in this session.
Those direct predecessors are declared with published IDs and exact
submission/ archive-member citations when uploaded. No acceptance
verdict, finite arithmetic check or unproved general lower bound is
used as a mathematical premise.
