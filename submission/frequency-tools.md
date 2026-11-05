# Counted constant-accuracy estimation from known random frequencies

This lemma is part of QSR17, not an oracle or a prior accepted result.
A root supplies (W,|q_W(theta)>) with KNOWN integer W, |W|<=2q,
and q_W(theta)=(|0>+exp(2pi i W theta)|1>)/sqrt2. Conditional on LOWER
construction/selection data and the pair identifier, W=kappa+Bin(d,1/2)
for some integer kappa and d>=1. They may vary and need not be known.
Different calls have disjoint fresh sources/private randomness. No law
conditional on the entire high-label transcript is asserted.

## Uniform shifted-binomial population gap

Choose fair X/Y, measure Z in{+1,-1}, and record(W,basis,Z). Score u by
S_u=2Zcos(2piWu) in X or2Zsin(2piWu) in Y. Conditional on W, its mean
is cos(2piW(theta-u)). For delta=theta-u the generating function is
 exp(2pi i(kappa+d/2)delta)*cos(pi delta)^d.
For circular |delta|<=1/2, cos(pi delta)>=0, so the REAL part is at most
cos(pi delta), uniformly over d>=1 and integer kappa. No centeredness,
even support, common incidence weight or nonnegative mean is required.
At circular distance>=1/32,
 1-cos(pi delta)>=2sin^2(pi/64)>=1/512,
by sin y>=2y/pi on[0,pi/2]. Thus E S_u<=1-1/512, while E S_theta=1.
The same inequalities hold after any allowed lower-history mixture.
All label dependence is retained in S_u; no full-record conditional law
is substituted for the actual fresh-root distribution.

## A finite grid, concentration, and exact decoding

Set Mgrid=2^22(q+1). Enumerate u=k/Mgrid for k=0,...,Mgrid-1.
The nearest grid point u0 has circular error<=1/(2Mgrid).
For every |W|<=2q, |2pi W(theta-u0)|<2^-18, using pi<4.
Hence E S_(u0)>=1-2^-37, by cos x>=1-x^2/2.
The population gap from u0 to every grid point at distance>=1/32 is
larger than1/1024. The grid is an explicit enumeration, not advice.

For the same q used in all stages set
 hstat=ceil(log2(Mgrid+1))+ceil(log2(n+7))+20,
 Kstat=2^32 hstat.
Collect Kstat fresh triples per stage. Every score lies in[-2,2]. Its centered
log MGF has second derivative (a tilted variance) at most4, so the usual
integration and optimized Markov bound gives
 Pr(|empirical mean-E mean|>2^-13)<=2 exp(-Kstat*(2^-13)^2/8)
 =2exp(-8hstat).
Root calls are independent since their entire sources are fresh; alternatively
the same bounded conditional-gap/MGF argument applies to fixed past histories.
Union over all Mgrid grid points and at most n+5 stages is at most
2(n+5)Mgrid exp(-8hstat)<1/1024. Indeed exp(-8hstat)<=2^(-8hstat),
and hstat contains ceil(log2(Mgrid+1)),ceil(log2(n+7)) and20.
No union over all N secrets is used or needed.

Evaluate each empirical score with an additional absolute error<2^-13.
Then each computed score differs from its population by<2^-12 on the
simultaneous concentration event. Twice this allowance is2^-11<1/1024,
so a maximizer, ties resolved by smallest k, has circular error<1/32.
Output that rational grid point. This is a finite exact classical procedure.

Generate pi by the same64-term rational Machin construction as label-tools.md.
For any required W,k reduce W*k modulo Mgrid by counted signed integer
arithmetic. The argument2pi*((W*k) mod Mgrid)/Mgrid lies in[0,8).
Use256 sine/cosine Taylor terms, then round to denominator2^20.
The same explicit factorial/remainder bounds in label-tools.md give error
<2^-19, including pi error, truncation and rounding. Multiplying by2Z
changes this by at most2^-18<2^-13. Accumulate the rounded integers and
compare sums directly; all candidates share denominator2^20 Kstat.
Neither floating-point arithmetic nor physical real rotations are required.

## Unwrapping and storage/work

Suppose stage j=0,...,J=n+4 has phase theta_j=2^j theta modulo1.
Use the estimator separately at each stage. With all stage errors<1/32,
start g_J at its estimated grid point. For j=J-1,...,0 choose the closer
in circular distance to the j-th estimate among (g_(j+1)+b)/2, b=0,1,
with a fixed tie rule. If next error e<1/32, the correct lift is within e/2
of theta_j and within1/32+e/2<3/64 of its estimate; the wrong lift is
farther than29/64. Thus the correct lift is chosen, its error halves,
and final error<2^(-n-9). Round M*g_0 modulo odd M to recover the exact
numerator of theta with denominator M<=2^n. All comparisons and rounding
are rational bit computations of bounded width, not angle oracles.

The main proof establishes log2q<=H/2+3log2n and H>=128log2n.
For this actual n-less choice hstat<=log2q+log2n+52<=H. Thus
Kstat<=2^32H<=2^33n, and C<=2^35nH. The union bound above never
requires an additive n in hstat; its log-grid/log-stage/20 terms suffice. The Kstat records have O(n)
bits each; they require O(n^2) CLASSICAL bits. Keep only one grid index,
current sum and best-so-far pair while enumerating the grid. No q-sized
score array, Fourier transform or amplitude distribution is allocated.
All quantum roots are measured and released before generating the next.

For completeness, a very loose core bound of2^150 n^12 q covers one entire
stage's grid evaluation, including all Kstat records, at most256 rational
Taylor terms each, reductions, rounding, comparisons and emitted bit-loop
control. Every operand has O(n) bits: fixed Taylor degrees multiply widths
only by an absolute constant; score sums add O(log Kstat) bits. Schoolbook
rational operations, explicit bit pointers and their control fit O(n^8)
primitive bit/head operations per record/grid evaluation. Since
Mgrid<=2^23 q, Kstat<=2^33n, the displayed allowance is ample.
Every operation still receives the full allocated-memory address and clock
charge in the main proof. This is core accounting, not a free word operation.
The actual main allowance is G=2^1000n*m*R^5*2^t. Since q=r*m^(D+1)
and E_D>=Gm^D, the whole n+5-stage ratio is at most2^154n^13*r*m/G.
The main proof gives r*m<=n,t>=192log2n, so this ratio is below1.
The complete grid work is thus included in E_D and Wstar, with no source
or query oracle. This is a core bound; all full addresses and the monitor's
own work are additionally priced by controller-tools.md.

Parameter generation, storing records, basis coins, measurements, erasures,
initialization, inverse work and controller loops are all charged. The source
and work clocks cap every branch, including statistical failures. The lemma
is a mathematical proof; finite numerical diagnostics do not certify it.
