# Four-level BASE13 port

## Explicit four-level schedule and padding estimates

For n>=1024 use depth at most four, and set
R_test=ceil(n/8)+2ceil(log2 n)+8.
For v<=n, 3(2v+1)<=8n, hence delta(v)<=log2 n+4.
The test value is <=n. Its fourth backward value is positive
since R_test-3(log2 n+4)>=n/8-log2 n-4>0.
The four-value sum is at least 4R_test-6(log2 n+4)>=n/2.
Thus the first feasible R obeys n/8<=R<=R_test. All four
backward values of that selected R are at least
R-3(log2 n+4)>=R/4, since n/32>=log2 n+4 on this domain.
The proposed use of u=max(1,floor(R/4)) and all four values
therefore meets the basic profile relation. The bound
2^R<=2048 n^2 2^(n/8) follows directly.

For the nominal q0=(2R+1)^4, the stronger inequality
2R_test+1<=n follows from n/4+4log2 n+23<=n, so q0<=n^4.
The existing h upper bound hmax=1+floor(u/8)<=1+R/32
is retained. If the odd modulus caps h below hmax, fewer
than nine decoder stages suffice by the short-modulus bound
with stride max(1,h-4). If h=hmax and R>=256, stride>=R/64
and Sodd<=64n/R+1<=513. If R<256, n<2048 from R>=n/8
and at most n+1<=2048 stages suffice. The modulus-one
case requires zero odd stages. Thus Sodd<=2048 throughout.

The inherited K=8192(ceil(log2 nq)+ceil(log2 n)+30),
with nq=2^(h-1)q0, is at most
8192(n/32+5log2 n+32) <=1024n for n>=1024.
For the last inequality, use log2 n<=n/102, which is true
at n=1024 and strengthens after that point. The interior
parentheses are then at most
n/32+5n/102+n/32 < n/8. Thus
H0=Sodd*K+2n<2^22 n. Replace the root expected source
factor 54 by 2*3^4=162. A source cutoff
1024(162 q0 H0+2n) is at most 2^41 n^5
since 162<2^8 and n>=1024.
For smaller n use the already counted finite shadow-score
algorithm, whose budget is at most 2^25 n, then pad to
P=2^41 n^5. Gate addresses and memory sizes remain
polynomial for a fixed depth of four. These estimates
supply concrete profile and source guard parameters,
with the decoder and weighted cutoff port specified below.

The charged combiner work carries over with an extra factor n
from the explicit profile rounding allowance: O(n^3 sqrt(L) 2^R)
before addressing, and O(n^5 L^(3/2) 2^(n/8)) after addressing.
The fixed-depth increase adds only one frame of retained labels.
The nominal signed integer label bound gains O(log n) bits,
still O(n), and the stride grid remains at most poly(n)2^(R/32).
The additional source readout work is polynomial. All original source and combiner gates are unchanged as specified below.

## Decoder and cutoff port

Keep the original leaf extractor, success/failure combiner, low-bit-only
retry rules, and full-modulus decoding, with the following uniform overrides.
At n<1024 execute the finite-shadow branch of Sections 8 and 3
using its original Qcap=2^35 n^4 precision parameter and exact
mF acquisitions, subsequently padded to the larger bank budget.
The argument for its finite-dimensional resource bounds uses only
that the branch is finite. Its correctness proof has no n<256
inequality. At n>=1024 set mstar=4 and q0=(2R+1)^4. Run PS_TREE
with exactly the greedy width and child allocation of Section 4,
now applied to the four values. Its induction in Section 5 has
one additional inductive step with exactly the same hypotheses.
A root still has a signed incidence vector with coefficients
in {-1,0,1}, supported on distinct source leaves, and at least
one nonzero coefficient. For each signed term the two child
subsets used in the final pair differ in an actual child position,
so there is no cancellation across children, whose leaf supports
are disjoint. The maximum support size is q0.

The full normalized signed frequency therefore remains bounded
by 2^h q0 at residual width h, and its unused high blocks have
the original independent uniform law conditional on the reduced
low transcript. No decoder proof uses a fixed nominal q0 value:
the explicit frequency grid and score concentration of Section 6
use q0 through nq=2^(h-1)q0, substitute the new q0 in that actual
grid, in K and in all width calculations. The factors D_A, the
trigonometric margin and parity law are independent of q0.
Section 7's parity identity and the stopping argument consequently
apply to a four-level root with no new measurements. The condition
R>=sqrt(n/2) used in Sections 4 and 6 holds for n>=1024 from
R>=n/8. The stated u floor and all h or short-modulus choices
remain unchanged.

Before any root work compute H0=Sodd*K+2n from these actual parameters.
In the acquisition and weighted cutoff definitions use
Qstar=162*q0*H0+2n and Wstar=12*2^R*H0, then Qcap=1024Qstar,
Wcap=1024Wstar. Use Qcap in the native label precision calculation
so the original unconditional coupling error stays below 2^-14.
The at-least-one-third conditional success per positive stage
and expected source cost product bound yield 162 q0.
The example of three levels in the cap proof must be replaced
throughout: the general recurrence bounds expected #attempts at
level i by 3 product_{j>i}(3r_j), and the product bound telescopes
unchanged via delta(v_j). This gives at most 3*2^R per level and
12*2^R per root. Thus Markov separately bounds the two abort
probabilities by 1/1024 in the ideal uncapped comparison. The
native-label and decoder errors retain their original upper bounds.
The algorithm keeps each prior control-flow guard, including all
aborted partial children, and charges every attempt and acquisition.
