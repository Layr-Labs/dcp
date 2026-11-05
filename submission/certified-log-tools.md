# Counted certified rational logarithm preprocessing for QSR1

This is ordinary classical exact rational arithmetic on the public bit length
n, before any source acquisition or quantum preparation. It supplies no real
oracle, advice, arbitrary gate or extra source copy. Its work and peak storage
are INCLUDED in the final bounds, separately from the working-core clock.

## Explicit interval and runtime integer parameter

Set e=floor(log2n) using the integer bit length of n, z=n/2^e in[1,2), and
u=(n-2^e)/(n+2^e) in[0,1/3]. Use K=ell+16 terms, where ell=ceil(log2n) is computed by integer bit length.
Form exact rational sums, updating one current odd power at each step:
 Az=2sum_(j=0)^(K-1) u^(2j+1)/(2j+1),
 A2=2sum_(j=0)^(K-1) (1/3)^(2j+1)/(2j+1), eps=3^(-2K).
The geometric integral identity
 ln((1+u)/(1-u))=2sum_(j>=0)u^(2j+1)/(2j+1)
follows by integrating the absolutely convergent geometric series on[0,u].
The omitted tail is nonnegative and at most
 2u^(2K+1)/((2K+1)(1-u^2))<=3^(-2K)=eps,
including u=0 by continuity. Hence ln z in[Az,Az+eps] and
ln2 in[A2,A2+eps], with A2>=2/3. Define the RATIONAL runtime parameter
 xplus=e+(Az+eps)/A2.
Then xplus>=x=log2n. Since ln z<=ln2 and ln2-A2<=eps,
 0<=xplus-x<=eps/A2+ln z*eps/(A2 ln2)<=3eps.
For K=ell+16,3eps<=2^(-2ell)<=n^(-2), because
3^(2ell+32)>=3*4^ell. No million-term series is used in this configuration. No irrational rounding decision is required anywhere. The upper bound
xplus(K) decreases with K: its numerator Az+eps decreases because the
new series term is at most(2/9)eps while eps decreases by(8/9)eps,
and its positive denominator A2 increases. This also permits independent
coarse-interval diagnostics when needed; actual optimized K is short enough
for the finite parameter diagnostics to execute directly.

Write xplus=a/b with positive integers a,b. Let v=floor(na/b), compute
j=isqrt(v), and set T0=j if j^2*b>=na, otherwise j+1. This is exactly the
least integer with T0^2>=n*xplus, using integer square root, division and
comparison only. The square-root difference is bounded by
 sqrt(n*xplus)-sqrt(nx)<=n*n^(-2)/sqrt(nx)<1.
Therefore H=sqrt(nx)<=T0<=H+2. Compute R=ceil(sqrt(xplus))
by the same exact rational integer-root procedure, then m=ceil(T0/R), t=mR,
retaining only these compact integer parameters. Release the large rational temporaries BEFORE preparing
the gradient/window, acquiring sources or entering the working-core clock.
It follows that sqrt(x)<=R<=sqrt(x)+2, m<=sqrt(n)+2 and
H<=t<T0+R<=H+R+2.

## Bit-level generation and near-quadratic peak memory

The normalized numerator/denominator of u have O(log n) bits. K=O(log n),
so current powers have O((log n)^2) bits and even unreduced sums have
O((log n)^3) bits, summing all term-denominator lengths. Stream current
powers and a constant number of numerator/denominator accumulators; no list
or arithmetic history is retained. Since(log2n)^3<=n for n>=2^20 (check20
and the decreasing ratio x^3/2^x), this log routine uses O(n) classical bits.
Its fixed public loops and schoolbook operations fit O(n^16) fully charged
work, with no quantum registers or source copies.

The remaining compact parameters and exact caps have O(n)-bit numerators
and denominators by the main proof. Generate their powers by repeated
squaring with a constant number of current buffers, or at most O(log n)
such buffers; all memory is O(n^2). Schoolbook arithmetic, loop/index
generation and every full allocated-memory address charge fit the same
conservative O(n^16) deterministic preprocessing allowance. Release all
unneeded buffers before quantum/source work. No O(n^3) allocation is used.
Neither logarithm precision nor pre-clock parameter generation is free.

The declared classical envelope is O(n^2(log2n)^(-1/2)2^sqrt(log2n)). It
contains O(n^2), since2^sqrt(x)>=sqrt(x). Thus these preprocessing buffers,
input bits and cap generation fit the SAME full bound. Its work fits the
declared time representative. The n<2^20 branch skips this routine and
uses the specified baseline. No real oracle, advice, fast reciprocal or
uncounted preparation is introduced.
