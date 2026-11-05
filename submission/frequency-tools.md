# Counted constant-accuracy estimation from known random frequencies

This lemma is part of QSR7, not an oracle or a prior accepted result.
A root supplies a pair (W,|q_W(theta)>) where W is a KNOWN integer,
|W|<=q, and q_W(theta)=(|0>+exp(2pi i W theta)|1>)/sqrt2.
Conditional on the low-label construction history and selected pair,
W is Bin(T,1/2)-T/2 for some even T>=2. T need not be known or fixed.
Different calls use disjoint fresh sources and private randomness. No
conditioning on the entire full-label transcript is asserted.

## Uniform population gap

Choose X or Y with a fresh fair private bit and measure the qubit, giving
Z in{+1,-1}. Record the classical triple(W,basis,Z). For a trial u define
S_u=2Z cos(2pi W u) in X, and S_u=2Z sin(2pi W u) in Y.
Conditioning first on W, its expectation over basis and outcome is
cos(2pi W(theta-u)). The centered-binomial generating function gives
 E exp(2pi i W delta)=cos(pi delta)^T.
For even T>=2 this is real, nonnegative and at most cos^2(pi delta).
The same upper bound holds after averaging any allowed history/T mixture.
If circular distance of u from theta is at least1/32, take
|delta| in[1/32,1/2]; then E S_u<=1-sin^2(pi/32)<=1-1/256.
The last inequality follows from concavity sin x>=2x/pi on[0,pi/2].
At u=theta, E S_u=1. These bounds are uniform in the unknown phase.
The label dependence of individual measurements is fully retained in S_u;
there is no assumption that a fixed full label record has this distribution.

## A finite grid, concentration, and exact decoding

Set Mgrid=2^20(q+1). Enumerate u=k/Mgrid for k=0,...,Mgrid-1.
The nearest grid point u0 has circular error<=1/(2Mgrid).
For every |W|<=q, |2pi W(theta-u0)|<2^-18, using pi<4.
Hence E S_(u0)>=1-2^-37, by cos x>=1-x^2/2.
The population gap from u0 to every grid point at distance>=1/32 is
larger than1/512. The grid is an explicit enumeration, not advice.

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
simultaneous concentration event. Twice this allowance is2^-11<1/512,
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
For this actual n-less choice hstat<=log2q+log2n+50<=H. Thus
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
Mgrid<=2^21 q, Kstat<=2^33n, the displayed allowance is ample.
Every operation still receives the full allocated-memory address and clock
charge in the main proof. This is core accounting, not a free word operation.
The actual main allowance is G=2^10000 n^26 2^(ceil((t+3R)/2)).
Here q=r*m^(D+1), E_D>=G A0^D>=Gm^D, r<=6n^(1/2) and m<=n.
Hence(n+5)2^150n^12q/E_D<=2^154n^15/G<=1. All n+5 stages fit E_D.
This uses the actual paid allowance. An obsolete stream-enumeration formula
G=2^100n^5*2^t is NOT used; the polynomial slack alone suffices here.
Parameter generation, storing records, basis coins, measurements, erasures,
initialization, inverse work and controller loops are all charged. The source
and work clocks cap every branch, including statistical failures. The lemma
is a mathematical proof; finite numerical diagnostics do not certify it.
