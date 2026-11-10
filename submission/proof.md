# CYCLIC-QSCALE: retuned quarter-log sizes and a curvature work bound

## 1. Complete configuration and theorem

Use the complete algorithm specified by quarterlog_base.md and its included
cyclic_base.md, with the parameter scale and resource proof replaced here.
quarterlog_base.md is this session's fixed-gamma=1/4 manuscript, SHA-256
e8beddc549050e9beec89c8d6470ddc57737ebbfe07d9088a841b9be512dd0a8.
cyclic_base.md is the unmodified full cyclic-window/source-aligned proof
from e9fc2eca-9d1c-469b-a629-a43e0f7ce928, candidate
45d9985c85813b2f3d30c62c717faba3621eb57a. Both full source arguments
are supplied, not invoked through earlier verdicts. Their older resource
theorems concern their own configurations and are not silently substituted
for the new one below.

For every N>=2 and s in Z/NZ let n=ceil(log2 N). Fix gamma=1/4 and
c=127/128 for every instance and resource. Use the counted one-sided
rational logarithm ell(mu) of quarterlog_base.md Section 2, and set

    mu=ceil(sqrt(2B))+1, kappa=2,
    x=s=max(2,floor(c mu/(ell(mu)^(1/4)))), q=x+3,
    m=min{z>=s+1:z(z+1)/2-s(s-1)/2+x(z+1)+2>=B}.

The floor is a counted integer instruction: for ell=r/d in lowest terms,
take the integer fourth root of floor(127^4 mu^4 d/(128^4 r)).
Keep the boosted lengths, residue windows, greedy allocation, leaf table,
cyclic-window instrument, failed-input disposal, source transforms,
collective extractor, actual-size backward decoder, 2-adic procedure and
finite n<64 branch of the included sources. Recompute all actual decoder
and confidence parameters and the literal cap

    A_star=max_(1<=B<=n) q(B)2^m(B),
    Q_star=8 A_star(G_odd+2a2)+2a2, Qcap=1024 Q_star.

This ONE configuration recovers the entire s with unconditional probability
at least 1-2^-8. On every branch it obeys jointly

    T=O(n^3 2^J(n)),
    S_C=O(n^(3/2)(log2 n)^(-1/2)2^F(n)), S_Q=O(n),
    Q=O(n^(3/2)(log2 n)^(-1/4)2^F(n)),
    J(n)=a sqrt(n)+(16129/8192)sqrt(n)(log2 n)^(-1/2)
                 -(4/3)sqrt(n)(log2 n)^(-1)
                    +2sqrt(n)(log2 n)^(-3/2),
    F(n)=a sqrt(n)-(5/3)sqrt(n)(log2 n)^(-1/4)
                    +2sqrt(n)(log2 n)^(-1/2).

The exact Pell rational a=u_333/v_333 in cyclic_base.md proves a>sqrt2.
All constants are absolute, independent of N,s and outcomes. Evaluate these
eventual positive envelopes for n>=2^512 and extend them positively on the
finite smaller prefix. The algorithm and success guarantee still apply to
every N. Exact indices are 1/2,1/2,0,1/2. Malformed fraction is zero under
independent ideal copies, not a maximum-tolerance assertion. Every acquisition,
failed attempt, rejected label, discarded root and aborted subtree counts.

## 2. Capacity, precision and unconditional recovery

Write L_mu=log2(mu). The included rational series proves
L_mu<=ell<=L_mu+1/mu with polynomial charged parameter work. The mean
value theorem for v^(-1/4), flooring and the fixed factor c give for mu>=4

    c mu/(L_mu^(1/4))-2<=x<=c mu/(L_mu^(1/4)).          (1)

The max with two respects the upper bound: mu/L_mu^(1/4) is increasing
for mu>=4, is greater than three at four, and c>2/3. At mu=3 the actual
instruction gives x=2. In every case 2<=x=s<=mu-1. Consequently capacity
holds at z=mu, m<=mu, and the source's exact sum/slack identities still
hold. All selected windows are in the B-bit low prefix and all rank maps
remain injective. The source's conditional high-block collision and
top-bit independence proofs therefore apply unchanged, with fresh non-root
failure <2^-q and root failure <=1/4. No fixed-full-label-table bound is
assumed for the non-root condition.

We have m2^-q<=1/2. For mu<16 use m<=15,q>=5. For mu>=16, the function
2^L/L^(5/4) increases on L>=4. At four its value is 2sqrt2>2, so c>1/2
implies c mu/L_mu^(1/4)>L_mu. By (1), q>=c mu/L_mu^(1/4)+1>L_mu+1.
Since -ln(1-p)<=2p for p<=1/32, the retry product is at most (4/3)e<4.
Fresh-whole-attempt reach-probability accounting gives expected tree
acquisitions <=8 A_star. It never assumes independence of attempt cost
and success. The actual root logarithmic size is O(sqrt n), so the
source-aligned decoder still has expected root budget O(n) and all its
actual-size hypotheses hold.

The recomputed Q_star is thus an uncapped ideal expectation bound, and
Markov adds <=2^-10 acquisition-cutoff error. The unchanged collective-label
coupling, seed/backward decisions, parity caps and finite exhaustive branch
retain total failure below 2^-8 as proved in the supplied source. These
are unconditional first-error and cutoff comparisons. Incorrect extracted
labels or earlier decoder mistakes still obey every literal cap and fixed
width. Neither correctness nor resource accounting conditions on perfect
extraction or passing a cutoff.

## 3. Exact square-root profile and its monotonicity

For analysis put R=sqrt(2B), L=log2 R, u=c L^(-1/4),
g(R)=R u and S=sqrt(1+2u^2). For R>=4, g is increasing with derivative
between zero and one, and R+1<=mu<=R+2. Thus (1) implies

    g(R)-2<=x<=g(R)+2, q<=4g(R).                       (2)

Completion of the square bounds m by the maximum of s+1 and
ceil(sqrt(R^2+s^2+(x+1/2)^2)-x-1/2). For R>=16, u^2<=1/2.
The lower constraint plus x is then
2x+1<=2g+5<=R S+5. For the square-root candidate, compare its radicand
with R^2+2g^2. From x<=g+2 and g<=R,

    2x^2+x+1/4-2g^2<=9g+41/4<=9R+41/4.

Dividing by the sum of the two square roots bounds the difference by
(9R+41/4)/(2R)<5 for R>=16; the ceiling contributes at most one.
Hence m+x<=R S+64 uniformly, with 64 also covering the finitely many
smaller widths. Subtract (2) and enlarge the same constant to obtain

    m<=h(R)+66, h(R)=R(S-u).                          (3)

The function h is increasing for R>=4. With eta=1/(4ln(2)L),

    h'(R)=S-u-eta*u*(2u/S-1).

Here S-u>1/2, since S^2-(u+1/2)^2=(u-1/2)^2+1/2>0.
Also 0<u<=1 gives 2u/S<=2/sqrt3<7/6, and eta<3/4.
Therefore h'(R)>1/2-1/8=3/8. This justifies taking a uniform maximum
over ALL requested widths; no rounded-profile monotonicity is assumed.
For R*=sqrt(2n), L*=log2 R*, g*=g(R*), h*=h(R*),

    A_star=O(g*2^h*), Qcap=O(n g*2^h*).                (4)

Fixed small-width trees are absorbed by the absolute constant. The literal
cap uses the exact maximum, not its earlier first-order upper estimate.

## 4. Every-branch work and retained storage/source guarantees

The deterministic tree charge per acquisition is
O(n(m+1)2^kappa 2^x/q). Every acquired copy has at most one charged merge
per level because failed inputs are discarded. By (2) and monotonicity
of 2^v/(v+3), the common charge is O(n^(3/2)2^g*/g*).
Multiplying by the ACTUAL cutoff (4), for this same configuration, yields

    tree core work=O(n^(5/2)2^(R*sqrt(1+2c^2/(L*)^(1/2)))).   (5)

The O(n^2) per-copy source transforms and collective label extraction are
smaller by their retained negative g*. Seed scoring O(n^2 A_star), all
feedback and polynomial rational setup are also below (5). Source cost,
initialization, classical processing, explicit lookups, circuit generation,
measurement, reset/disposal and all failed/cutoff-abandoned work are counted.
Address length is O(sqrt n), so total work is n^3 times the exponential
in (5).

For storage and samples it suffices to use S<=1+u^2 in (3):

    m<=R-c R/L^(1/4)+c^2 R/L^(1/2)+66.                 (6)

The O(n) quantum stack/scratch proof is unchanged because m<=mu and all
index lengths remain O(sqrt n). Stored high-part fields have width
O(sqrt n(m-i+1)). The s plateau levels sum to O(sqrt n s^2 2^lambda_max)
with a smaller geometric growing-level tail. Since x=s,
lambda_max=m+3 and s=O(g*), classical bits are
O(n^(3/2)(log2 n)^(-1/2)2^h*), plus polynomial scratch absorbed by the
eventually positive exponential. Samples have prefactor
n g*=O(n^(3/2)(log2 n)^(-1/4)) in (4).

To compare (6) with the unchanged target F, put t=log2 n. The exact
rational check at t=512 is

    648 c^4*512-625*513=59235921/65536>0.

Its linear slope 648c^4-625 is positive, so for all t>=512,
648c^4 t>=625(t+1). Taking fourth powers in reverse gives
c 2^(3/4)/(t+1)^(1/4)>=(5/3)/t^(1/4). The positive correction
2c^2/(t+1)^(1/2)<=2/t^(1/2), because c<=1. Therefore (6) implies
exactly the target F after replacing only the leading sqrt2 by a.
All four resources and success concern the SAME scaled configuration.
Underlying source/memory use can increase when reducing the boost; the
claim is that these full declared guarantees remain satisfied, not that
all underlying exact costs stay unchanged.

## 5. Curvature inequality and exact improved time envelope

For every z>=0 define P=1+z-z^2/2+z^3/2. It is positive, and direct
expansion gives

    P^2-(1+2z)=(z^4/4)(z^2-2z+5)>=0.

Thus sqrt(1+2z)<=1+z-z^2/2+z^3/2. Apply this to
z=c^2/(L*)^(1/2) in the work bound (5). With t=log2 n, its exponent
is at most

    sqrt2 sqrt n
      +2c^2 sqrt n/(t+1)^(1/2)
      -c^4 sqrt2 sqrt n/(t+1)
      +2c^6 sqrt n/(t+1)^(3/2).

The positive leading correction is bounded by
(16129/8192)sqrt n/t^(1/2), since 2c^2=16129/8192 exactly.
For the negative term use sqrt2>7/5 and the exact rational comparison

    (21c^4-20)*512-20=83842581/524288>0.

The slope 21c^4-20 is positive, so for t>=512,
c^4 sqrt2/(t+1)>=(4/3)/t. Finally 2c^6/(t+1)^(3/2)<=2/t^(3/2).
Replacing only the leading sqrt2 by the exact larger a proves J(n).
The finite n<2^512 prefix receives a positive representative extension
and absolute outside constants; all algorithmic guarantees remain valid
there. Every exponential logarithm is a sqrt n+o(sqrt n), hence exact
index 1/2. Linear quantum space has index zero.

Relative to the unscaled quarter-log target, classical/quantum space,
samples and clean-copy model have exactly the same declared envelopes.
Its time envelope improves strictly: the old-minus-new exponent is

    (255/8192)sqrt n/t^(1/2)+(4/3)sqrt n/t-2sqrt n/t^(3/2),

which tends to positive infinity. This comparison is between the proved
guarantees, not a claim about tight actual resource functions or practical
runtime. The algorithm actually changes its scale, and the charged-work
proof also retains a negative curvature term instead of using only
first-order concavity. The resource index remains 1/2; the challenge's
1/3 research goal and global frontier leadership are not established.

## 6. Provenance

The complete fixed-quarter-log manuscript is supplied as quarterlog_base.md;
its rational logarithm, family framework and all-modulus construction are
material sources. The full cyclic-window source and its earlier references
are supplied in cyclic_base.md. Published material predecessor IDs and exact
submission/ archive-member citations are declared with the upload. The
scale choice, coefficient-budget checks, monotone exact-square-root ledger
and explicit polynomial curvature bound are developed here. No prior
acceptance or finite numerical check is a proof premise.
