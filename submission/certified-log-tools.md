# Counted certified rational logarithm preprocessing for MSR10

This is ordinary classical exact rational arithmetic on the public bit length
n, before any source acquisition or quantum preparation. It supplies no real
oracle, advice, arbitrary gate or extra source copy. Its work and peak storage
are INCLUDED in the final bounds, separately from the working-core clock.

## Explicit interval and runtime integer parameter

Set e=floor(log2n) using the integer bit length of n, z=n/2^e in[1,2), and
u=(n-2^e)/(n+2^e) in[0,1/3]. Use the integer number of terms K=n.
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
For K=n>=2,3eps<=n^(-2), since3^(2n)>=3n^2 holds at2 and is preserved
when n increments. No irrational rounding decision is required anywhere. The upper bound
xplus(K) decreases with K: its numerator Az+eps decreases because the
new series term is at most(2/9)eps while eps decreases by(8/9)eps,
and its positive denominator A2 increases. This also permits independent
coarse-interval diagnostics to enclose the runtime choice K=n.

Write xplus=a/b with positive integers a,b. Let v=floor(na/b), compute
j=isqrt(v), and set T0=j if j^2*b>=na, otherwise j+1. This is exactly the
least integer with T0^2>=n*xplus, using integer square root, division and
comparison only. The square-root difference is bounded by
 sqrt(n*xplus)-sqrt(nx)<=n*n^(-2)/sqrt(nx)<1.
Therefore H=sqrt(nx)<=T0<=H+2. Set m=ceil(n^(1/4)), R=ceil(T0/m)
and t=mR by counted integer roots/division, retaining only these compact
integer parameters. Release the large rational temporaries BEFORE preparing
the gradient/window, acquiring sources or entering the working-core clock.
It follows that R<=n^(1/4)sqrt(x)+3 and t<H+m+2.

## Bit-level generation, memory and preprocessing work

The normalized numerator/denominator of u have O(log n) bits. For each of
K=n terms, its odd power and odd denominator have O(n log n) bits. Even
WITHOUT cancellation, multiplying denominators while summing all terms uses
O(n^2 log n) bits: sum the O(j log n+log(j+1)) lengths over j<=n.
The numerator has the same order, since all sums are bounded by constants
and the public integer e adds only O(log log n) bits. A constant number
of such buffers, current powers and accumulators suffices. Thus classical
preprocessing uses O(n^3) bits, with no quantum registers and Q=0.

At most polynomially many operations on O(n^3)-bit arrays are performed.
Schoolbook multiplication/division costs O(n^6) raw bit operations
per operation; at most O(n^2) such operations is a loose upper bound for
all sums, powers, interval and integer-parameter computations. Bit-index
and loop generation add at most O(n) per primitive, and every access pays
the full allocated-memory address, at most O(n) in this configuration.
Consequently2^200 n^16 FULLY CHARGED work is a conservative explicit bound.
Resets, buffer initialization and release bookkeeping are included. There is
no stored list of all powers or arithmetic history. Fixed public loops and
bounded operand lengths give a worst-case bound without a probabilistic cap. Rational pairs may be kept unreduced; no
Euclid, fast reciprocal or external arithmetic theorem is needed.
No assumption that these large rational operands have only O(n) bits is made.

The subsequent working-core guard applies only after these temporaries are
released. Its operands, precision and monitor words again have O(n) bits as
proved in the main text. The deterministic preprocessing work is added to
that phase's charged work; it is not made free by occurring before a clock.

## Joint-envelope absorption

With A=n^(1/4)sqrt(log2n), for n>=2^20 we have A>=(5/4)log2n.
Indeed dividing gives n^(1/4)/sqrt(log2n)>=5/4, true at2^20 and increasing.
Thus O(n^3) preprocessing bits fit O(n^(7/4)2^A), the declared classical
envelope. Its O(n^16) work fits the declared n^128 times positive exponential
representative. No extra quantum storage or source acquisitions occur during
this phase. The n<2^20 branch skips this routine and uses the exact baseline.
The enormous theoretical resources of the DCP algorithm are mathematical
guarantees; finite diagnostics of this lemma are not executions at large n.
