# CYCLIC-GCAP: growing plateaus in cyclic-window collimation

## 1. Full algorithm and theorem

Use the full algorithm in cyclic_base.md with the changed tree parameters,
resource lemma and consequences specified below. That included file is an
unmodified copy of the proof in submission e9fc2eca-9d1c-469b-a629-a43e0f7ce928,
commit 45d9985c85813b2f3d30c62c717faba3621eb57a. Its old theorem applies to
its old fixed16 cap, not to the new configuration. This amendment replaces
that cap and the resulting resource conclusions. Its explicit source
identities, uniform gates and costs, collective label extraction, cyclic
window instrument, freshness proof, top-bit law, source-aligned backward
decoder, exact 2-adic procedure, finite branch and literal cutoffs remain
part of this algorithm. They are supplied in full, not invoked through a
previous verdict. Read the two files jointly for the complete proof.

For every N>=2 and s in Z/NZ, set n=ceil(log2 N). One configuration of
CYCLIC-GCAP recovers the entire s with unconditional success at least
1-2^-8. On every branch it obeys jointly

    T=O(n^3 2^(a sqrt(n)+(3/5)n^(1/4))),
    S_C=O(n^2 2^(a sqrt(n)-(5/4)n^(3/8)+(3/5)n^(1/4))),
    S_Q=O(n),
    Q=O(n^(5/4) 2^(a sqrt(n)-18n^(1/4))).

Every outside constant is absolute and independent of N,s and sampled
outcomes. The exact rational a is u_333/v_333, explicitly given with its
Pell recurrence in cyclic_base.md Section 0. It satisfies a>sqrt(2).
The malformed fraction is epsilon(n)=0, with all acquired copies independent
ideal coset states. This clean-input guarantee asserts no maximum tolerance.
The four resource indices are 1/2,1/2,0,1/2; only time is scored.

## 2. The one schedule change

For a tree with B=D-1>=1, retain

    mu=ceil(sqrt(2B))+1, kappa=2,
    x=16 floor(sqrt(mu)), q=kappa+1+x,

but replace the constant-multiple square-root cap by

    s=min(mu-1,floor(mu^(3/4))).

The depth is still the smallest integer m>=s+1 with

    m(m+1)/2-s(s-1)/2+x(m+1)+kappa>=B.

Keep the source's exact formulas for lam_i, bmax_i, root-first greedy
allocation, leaf tables and depth-first VEC recursion with these parameters.
The two floor operations are exact integer roots, including the largest
v satisfying v^4<=mu^3 for floor(mu^(3/4)). All parameters are uniform.

The cyclic-window instrument, including its S<T failure rule and recorded
uniform window outcome, is retained literally. It retains T distinct ranks
without a remainder loss. All its explicit arithmetic and table circuits
are counted. The independent high-label collision lemma in the included
source applies unchanged: earlier decisions and selected indices still
inspect only the low prefix, and changing the predetermined widths neither
conditions on high bits nor changes incidence-vector injectivity. Thus
non-root failure, averaged over fresh children under that invariant, is
less than 2^-q. The final two-state root has the separate distribution-free
failure bound at most 1/4. No bound is asserted for every fixed pair of full
non-root tables; the low-prefix conditioning is essential.

## 3. Revised finite depth and table lemma

In this section only put R=sqrt(2B), u=sqrt(R), and r=ceil(sqrt(mu)/2).
Then R+1<=mu<=R+2 and

    16u-16<x<=16u+16, q<=64u.

The latter is exactly the source's elementary square-root bound and does
not involve s. Since s^2<=mu^(3/2) and 2mu r>=mu^(3/2), the capacity
condition holds at U=mu+r. Also U>=mu>=s+1. Hence m<=U<=2mu.
The exact sum and slack identities in the included source continue to hold:

    sum_i bmax_i=m(m+1)/2-s(s-1)/2+x(m+1)+kappa>=B,
    bmax_i+lam_(i+1)-2lam_i=-kappa.

The stronger depth estimate is

    m+x<=R+(1/2)u+2048,                              (A)
    m+x-s<=R-R^(3/4)+(1/2)u+2049.                   (B)

To prove it, completion of the square bounds m by the maximum of s+1 and

    ceil(sqrt(2B+s^2+(x+1/2)^2)-x-1/2).

For mu>=1024 we have (x+1/2)^2<=257mu and R>=1022. The concavity estimate
sqrt(R^2+v)<=R+v/(2R) gives

    s^2/(2R)<= (R+2)^(3/2)/(2R)<=(1/2)sqrt(R)+2,
    (x+1/2)^2/(2R)<= (257/2)(R+2)/R<129.

For the first inequality, the mean value theorem gives
(R+2)^(3/2)-R^(3/2)<=3sqrt(R+2)<=4sqrt(R), and division by 2R
is at most 2. The ceiling contributes at most one. Thus this square-root
candidate plus x is at most R+(1/2)u+132.
The other candidate satisfies
s+1+x<=mu^(3/4)+16sqrt(mu)+1<=mu+1<=R+3,
because mu^(3/4)<=mu/2 and 16sqrt(mu)<=mu/2 for mu>=1024.
If mu<1024, m<=mu+ceil(sqrt(mu)/2)<=1040 and x<=496, so the
uniform constant 2048 in (A) suffices as well. Finally
s=floor(mu^(3/4))>=R^(3/4)-1, since floor(mu^(3/4))<=mu-1 for all
integer mu>=3. Subtract this from (A) to obtain (B).

The expected retry product remains less than three. For k=floor(sqrt(mu))
we have m<=2mu<2(k+1)^2 and q=16k+3. The elementary bound
2(k+1)^2 2^(-16k-3)<1/100 holds at k=1 and decreases thereafter.
The root retry factor is at most 4/3 and the non-root product is at most
exp(2m 2^-q), so their product is less than three. The averaging and
fresh-attempt recurrence is exactly that in cyclic_base.md Sections 6--7
and 11, not an independence assumption about an attempt's cost and success.

Let A(B)=q2^m, the number of leaf qubits in a complete successful tree.
By (A), x>16u-16 and q<=64u,

    A(B)<=C u 2^(R-(31/2)u)                           (C)

for an absolute constant C, uniformly for every B>=1.

## 4. Caps, correctness and acquisitions

The algorithm still computes the EXACT integer

    A_star=max_(1<=B<=n) A(B),
    Q_star=6 A_star(G_odd+2a2)+2a2, Qcap=1024 Q_star

and uses the same literal source cutoff and parity-attempt caps in the
included source's Section 11. Enumerating B<=n and computing these integer
parameters costs a fixed polynomial in n and is charged. It does not
require building any exponential table. The label extractor's confidence
parameter is recomputed from this actual Qcap before the first acquisition.

The source-aligned decoder's actual R=nq_d is computed from the new tree.
Its grids, seed precision, physical scales and deterministic small/large
mode test use that R, exactly as specified. Since log2 R=O(sqrt n), the
proof in Section 9.2.5 still establishes G_odd=O(n) in either selected mode.
The small-mode bound H=O(sqrt n) and all other integer-width bounds remain
valid. No old numerical tree depth or fixed16 cap is used there.

The source's freshness, top-bit and decoder proofs now apply with the new
fixed widths. They give the same ideal seed and backward error budget,
and exact 2-adic recovery after a correct odd-part result. Section 3's
retry product gives the same expected-acquisition bound Q_star. Markov
bounds cutoff error by 2^-10. The collective label extractor with its
actual Qcap has total wrong-label probability at most 2^-12. The sum
with decoder and finite-attempt errors in the included source's Section 12
is at most 2^-8. This is an additive first-error coupling, not conditioning
on ideal labels or on passing a cutoff. The finite branch n<64 is unchanged.

For Y=(2n)^(1/4), bound (C) uniformly over B<=n. The function u^2-(31/2)u
is convex and bounded below, so

    max_(1<=u<=Y) [u^2-(31/2)u] <= Y^2-(31/2)Y+C0

for an absolute C0 (use the other endpoint and the finite minimum).
Since u<=Y, this yields

    A_star=O(n^(1/4)2^(sqrt(2n)-(31/2)(2n)^(1/4))),
    Q<=Qcap=O(n^(5/4)2^(sqrt(2n)-(31/2)(2n)^(1/4))).        (D)

The cutoff counts every label rejection, even root, failed merge, abandoned
subtree and all source copies on every branch.

## 5. Every-branch work and peak spaces

The source's deterministic per-acquisition tree charge depends on m,x,q,
kappa through O(n(m+1)2^kappa 2^x/q). Our m=O(sqrt n), kappa=2 and the
UNCHANGED x,q retain its uniform bound

    O(n^(5/4)2^(16Y)) core work per acquisition.

An acquisition is charged at most one merge at any given level, because
failed input subtrees are discarded. This includes partial trees and
wrong-label branches. Multiply this common bound by the actual cap (D):

    tree core work=O(n^(5/2)2^(sqrt(2n)+(1/2)Y)).             (E)

The source transforms and collective extraction require O(n^2) core work
per acquired copy. Their total, by (D), is
O(n^(13/4)2^(sqrt(2n)-(31/2)Y)), which is smaller than (E). The seed's
streamed score enumeration is O(n^2 A_star) plus polynomial setup, also
smaller. All source-aligned feedback and final integer arithmetic are
unchanged and polynomial, or charged per copy. Explicit source cost
(n+1)Qcap is included. Uniform gate generation, initialization, measurements,
resets, disposal, failures and abort branches are counted as in the full
ledger in cyclic_base.md Section 13.

Since m=O(sqrt n) and lam_i=O(sqrt n), the depth-first quantum stack and
arithmetic/extractor scratch still use O(n) qubits. Peak classical bits
are O(n^2 max_(B<=n)2^(x+m-s)) plus polynomial scratch. Bound (B) gives

    x+m-s<=f(sqrt(2B))+2049,
    f(z)=z-z^(3/4)+(1/2)sqrt(z).

f is increasing on z>=1, since f'(z)>=1-3/4=1/4. Consequently

    S_C=O(n^2 2^(sqrt(2n)-(2n)^(3/8)+(1/2)(2n)^(1/4))).     (F)

Its exponent is eventually positive of order sqrt n, so polynomial scratch
and the finite initial range are absorbed in an absolute outside constant.
The address charge is O(sqrt n). Multiplying (E) by that charge yields

    T=O(n^3 2^(sqrt(2n)+(1/2)(2n)^(1/4))).                  (G)

Equations (D),(F),(G) and the quantum bound hold simultaneously on every
branch of the one stated configuration, with unconditional recovery above.

## 6. Exact envelopes, provenance and limits

The Pell recurrence proves a>sqrt2. Also 3/5>(1/2)2^(1/4),
5/4<2^(3/8), and (31/2)2^(1/4)>18 (equivalently (36/31)^4<2).
Termwise comparison gives exactly the four introductory structured bounds.
Their exponential logarithms are a sqrt n+o(sqrt n), hence growth index
1/2; the linear quantum envelope has index 0. Coefficients and polynomial
prefactors are explicit; no unknown inner coefficient is guessed.

The full cyclic-window source, including its source-aligned decoder and
independent-high-bit collision proof, is materially reused from
 e9fc2eca-9d1c-469b-a629-a43e0f7ce928. The growing mu^(3/4) plateau and
explicit paid-overhead analysis develop this session's GCAP/GCAP-B work.
The unchanged source file retains its own references and detailed lineage.
The source proof is evidence to check, not a verdict to invoke.

Relative to GCAP-B's mixed-power envelopes, this variant retains the same
classical and quantum envelopes, improves the time prefactor from n^4 to
n^3, and replaces a positive fourth-root sample overhead by a negative
fourth-root term, with polynomial sample prefactor n^(5/4) instead of
n^(3/2). It remains a time/space tradeoff at time index 1/2, not a proof of
the challenge's 1/3 research target or a global frontier leadership claim.
