# CYCLIC-DOUBLEBOOST: inverse-square-log roots, squared-log boosts and block recovery

## 1. Complete construction and joint theorem

Explicit supplier convention for this revision: every power-of-two leaf
uses Shift_sh_g, LE, then ONE X on the original control, and then the
label kk=k mod2^wd, exactly as the positive-qubit supplier in cyclic_base.md
Section 10. This is the same single conversion in all referenced suppliers,
not an additional second X. It gives the positive phase required by the
wide Fourier-label readout. The conversion costs one exact Clifford gate
per original copy and is included in the stated work and peak allocations.

Use the complete square-root-block instrument and all-modulus decoder supplied
in blockboost_base.md and its included full sources, with the base schedule,
shifts, finite kappa guard and resource conclusions explicitly replaced below.
The complete inverse-square-logarithm schedule is supplied as doublelog_base.md,
from CYCLIC-DOUBLELOG 17eb8b17-04b5-4584-bfda-97bc6b181419, commit
2db69b223a2847f77b6ff8ae379cda03c890908b. The original cyclic circuits,
source identities, conditional freshness, exact translations, rational logarithm,
capacity windows, backward recovery and counted work model are all supplied
in full. Previous verdicts are not mathematical premises. Their old resource
theorems apply to their own old configurations, not this one.

For every N>=2 and every s in Z/NZ, n=ceil(log2 N), ONE fixed uniform
algorithm recovers the entire s with unconditional probability at least
1-2^-8 from independent ideal copies. On every branch jointly,

    T=O(n^3 2^J2(n)),
    S_C=O(n^(3/2)(log2 n)^(-4)2^G2(n)), S_Q=O(n),
    Q=O(n(log2 n)^(-2)2^G2(n)),
    J2(n)=a sqrt(n)+23sqrt(n)/(log2 n)^4
                   -180sqrt(n)/(log2 n)^8
                   +2900sqrt(n)/(log2 n)^12,
    G2(n)=a sqrt(n)-(11/2)sqrt(n)/(log2 n)^2
                   +23sqrt(n)/(log2 n)^4-(log2 n)^2.

Here a=u_333/v_333 is the exact Pell rational in cyclic_base.md Section 0,
with its proof a>sqrt2. All constants are absolute and independent of N,s
and outcomes. Use these eventual positive representative envelopes for
n>=2^4096 and extend them positively on the finite smaller prefix. Algorithmic
correctness covers every N. Exact indices are 1/2,1/2,0,1/2. Malformed
fraction is zero under independent ideal copies, with no maximum possible
tolerance or positive robustness claim. Every original acquisition counts,
including rejected, failed, discarded and cutoff-abandoned copies.

For n<2^4096 run the original complete DOUBLELOG algorithm with its literal
caps, as supplied in doublelog_base.md and cyclic_base.md. This finite public
branch is absorbed by absolute outside constants in all eventual envelopes;
no input is excluded from correctness. Below assume n>=2^4096.

## 2. Exact new schedules, blocks and finite guard

Retain the square-root block constants and compute them by exact arithmetic:

    t=ceil(log2(n+2)), h=max(1,floor(isqrt(n)/8192)),
    Dcut=2^20(h+t+1)^2, lambda(b)=2b+2t+40.

For auxiliary width V compute mu=ceil(sqrt(2V))+1 and the counted rational
ell(mu) supplied in full, satisfying log2(mu)<=ell(mu)<=log2(mu)+1/mu.
Use the inverse-square-logarithm base and finite guard

    x0=max(2,floor(mu/(ell(mu)^2))),
    kappa=ceil(log2 mu)+1 if mu<65536, and 2 otherwise.

For ell=r/d the base floor is exact integer division floor(mu d^2/r^2).
OTHER calls use x=s=min(mu-1,x0+t^2). SEED calls, including SMALL odd
scored steps, use x=s=min(mu-1,x0+t^2+2t). Put q=kappa+1+x and let m
be the least integer m>=s+1 with

    C(m)=m(m+1)/2-s(s-1)/2+x(m+1)+kappa>=V.

One-bit calls use V=D-1. A wide call at actual label width D>Dcut retaining
b<=h bits uses V=D-b+lambda(b)-1, the generic non-root boosted lengths,
root index length lambda(b), root capacity reduced by lambda(b)-1, and
root-first allocation of exactly D-b actual low bits. All classical and
quantum operations are the supplied exact circuits and counted bit algorithms.

Capacity at mu gives m<=mu for both shifted schedules. The finite guard
has kappa<=17, so its factor 2^kappa is explicitly a fixed outside constant
in work and space, not an omitted varying cost. For mu<65536,
2^kappa>=2mu and q>=kappa+3 imply m2^-q<=1/16. For mu>=65536,
L_mu=log2 mu>=16, precision gives mu/L_mu^2-2<=x0<=mu/L_mu^2,
and mu>=L_mu^3. Thus q>=L_mu+1, giving m2^-q<=1/2. Increasing x
by t^2 or t^2+2t only strengthens the bound. The fresh-tree retry product
is at most (4/3)e<4, exactly as established in doublelog_base.md.

All capacity sums and slack identities are algebraic in x,s,kappa. Wide
slack remains -kappa and total capacity is at least D-b. The root fits
its inputs: D>Dcut gives R=sqrt(2V)>1448(h+t+1); the unshifted x0 is
<=R/8 and t^2+2t<=R/8 on n>=2^4096, since R is a fixed positive
multiple of sqrt n and 2^(log2(n)/2) dominates (log2(n)+2)^2. The ratio
is increasing on this range and the left-endpoint comparison holds exactly.
Hence x<=R/4; the capacity upper bound forces m>=R/4, and
lambda(b)<=2h+2t+40<m+kappa+1=lambda_(m-1). All capacities are nonnegative.
Every actual inspected window stays in the low D-b prefix, leaving b
independent untouched source bits. No success estimate is conditioned on
full non-root high-label tables.

Recompute the exact maxima Ao,As,Aw,Ac as in the full block construction,
using NEW OTHER/SEED schedules; include the width-one sentinel. Recompute
Rbar=max(Ao,As,Aw,1), ellbar=ceil(log2 Rbar), nu=ceil(log2(n+ellbar+28))
and every decoder/extractor mode, grid, multiplier, precision and confidence.
These public integer computations have counted polynomial setup cost.

## 3. Full all-modulus recovery and literal typed caps

Retain every step of the complete block construction with these new schedules:

- The seed uses new-SEED one-bit roots at the supplied physical scales,
  Fseed=(ellbar+28)32768(ellbar+nu+80), and the complete streaming score
  proof, returning error e0=2^(-ellbar-30) except with probability <=2^-50.
- SMALL odd moduli use new-SEED scored one-bit roots, Kback=512(nu+60)
  per inverse step. LARGE uses OTHER wide roots and the full block source
  shifts/CRT multipliers under M>=2^30*2^h*Rbar*ceil(sqrt n).
- The power-of-two part uses OTHER wide roots above Dcut and OTHER one-bit
  parity roots in the tail, retaining the complete exact phase identities.
- Balanced count testing, selected flags, bijective residue/rank reindexing,
  exact collective translations and confidence formulas are unchanged.
  Ktry=64(t+40) bounds whole attempts, and every failed attempt is discarded.

The low-prefix freshness proof still applies because the new integer widths
are predetermined. The nonempty high-label incidence forms remain pairwise
uniform modulo 2^b by their odd minors, with at most one empty incidence.
Thus the balanced-count Chebyshev bound, selection probability at least one
half, exact selected Fourier-eigenstate identity and perturbation norm bound
all apply without any uniform-subset-sum assumption. Fair top-bit and
characteristic bounds for one-bit roots likewise hold for the new schedules.
All root multipliers satisfy the actual Rbar bound. The exact source shift
and CRT identity uses the actual retained-low-bit width, not auxiliary V.
No new source oracle, QRAM or inverse-QFT synthesis is assumed.

With odd terms zero if M=1, define literal integer expectation budgets

    U_seed=8 As [Fseed+1_SMALL H Kback],
    U_other=1_LARGE 24 Aw ceil(H/h)
              +24 Aw ceil(a2/h)+16 Ac min(a2,Dcut)+2,
    Q_seedcap=4096 U_seed, Q_othercap=4096 U_other,
    Q_global=Q_seedcap+Q_othercap.

The supplied fresh-root accounting applies uniformly after earlier wrong
decisions, since construction/selection laws depend on equal magnitudes and
uniform stored labels. Factors eight, three and two include all source
acceptance, internal retry, whole-root selection and parity costs. Enforce
each type's cap on EVERY original acquisition. Copies never change type.
Source extraction uses confidence ceil(log2(Q_global(n+5)))+20 and
per-basis count 2^21 times that integer, with union coupling error <=2^-18.
The two Markov cap errors sum to <=2^-11. The supplied seed, SMALL/LARGE,
alignment, selection/readout and parity first-error bounds keep total failure
below 2^-8. Every branch has defined fixed widths, integer outputs and caps.
This is unconditional recovery, including the explicit finite branch.

## 4. Inverse-square-log exact profiles and squared-logarithm source saving

For analysis put R=sqrt(2V), L=log2 R,

    u=L^-2, g(R)=R/L^2,
    f(R)=R[sqrt(1+2/L^4)-1/L^2].

On R>=32, g is increasing with bounded derivative. With S=sqrt(1+2u^2),
eta=2/(ln(2)L)<3/4, the exact derivative is
f'=S-u-eta*u*(2u/S-1)>3/8. Completing the capacity square and the
rational precision bound gives x0=g+O(1), m+x0<=RS+O(1), m<=f+O(1).
The guarded finite smaller widths are absorbed by an explicit fixed constant,
as in the complete DOUBLELOG proof; kappa<=17 is included throughout.

For either delta=t^2 or t^2+2t and R>=n^(1/4), the min with mu-1 is
inactive eventually and x=g+delta+O(1). The exact square-root comparison
changes m+x by at most

    O(g delta/R+delta^2/R+1)
       =O(delta/L^2+delta^2/R+1)=O(1),

uniformly, since L>=log2(n)/4 and t<=log2(n)+2. The lower constraint
2x+1 fits RS+O(1) because x/R tends uniformly to zero. Therefore

    m+x<=RS+O(1), m<=f-delta+O(1).                  (1)

For R<n^(1/4), m<=mu and q=O(mu) give 2^O(n^(1/4)) maxima. They are
below the global right side even after division by 2^(t^2) and a polynomial.
Wide auxiliary V<=n+O(sqrt n) changes R by O(1), hence g and f by O(1).
No rounded-profile monotonicity is assumed. For R*=sqrt(2n), L*=log2 R*,
g*=g(R*), f*=f(R*), exact maxima thus satisfy

    Ao,Aw=O(g*2^(f*-t^2)),
    As=O(n^-2 g*2^(f*-t^2)).                        (2)

Consequently ellbar=O(sqrt n), Fseed=O(n), and SMALL H Kback=O(n).
The number of wide blocks is O(sqrt n). The fixed square-root block cutoff
still satisfies Dcut<=n/16, and Ac<=poly(n)2^((1/2)sqrt n). This tail has
a strict leading gap below f*/sqrt n→sqrt2 even after division by 2^(t^2),
so its entire literal budget fits the same target. From (2) and the caps,

    Q_global=O(sqrt n g*2^(f*-t^2))
       =O(n(log2 n)^(-2)2^(f*-t^2)).                (3)

The complete high-part plateau/geometric allocation ledger gives

    S_C=O(n^(3/2)(log2 n)^(-4)2^(f*-t^2)), S_Q=O(n). (4)

OTHER and SEED have s=O(g*) at maximizing widths, m is lower by delta,
and lambda_max=m+kappa+1; 2^kappa<=2^17 is fixed. All small-R/tail/root
postprocessing tables, scores, extractor records, residues and setup have
smaller leading coefficients and are included in (4), after the squared-log
saving as well. Allocations stay fixed-width after incorrect labels.

The exact DOUBLELOG coefficient proof, using concavity, gives for v=log2 n

    f*<=sqrt2 sqrt n-4sqrt2 sqrt n/(v+1)^2
                         +16sqrt2 sqrt n/(v+1)^4
       <=a sqrt n-(11/2)sqrt n/v^2+23sqrt n/v^4.

Here 56v^2>=55(v+1)^2 on v>=128, sqrt2>7/5 and 16sqrt2<23.
Since t^2>=v^2, (3)--(4) imply exactly the stated G2 envelope and prefactors.
The explicit negative term -(log2 n)^2 is a supported exponent term with
n power zero and log power two; it comes from the actual integer boost.

## 5. Every-branch work and an explicit improved curvature time bound

The deterministic OTHER per-acquisition charge is
O(n^(3/2)2^(g*+t^2)/g*), and the SEED charge has an additional factor
2^(2t)=Theta(n^2). Multiplication by EACH type's OWN literal cap cancels
2^(t^2), and cancels n^2 for SEED. Total tree core work is
O(n^(5/2)2^(R*sqrt(1+2/(L*)^4))). Wide outputs fit inputs, so the full
lookup/ancestry charge holds, including failures and abandoned partial trees.

Source transforms and collective extraction cost O(n^2) per copy and are
smaller by the retained negative g*. Streamed seed scores and counted
polynomial setup are also smaller. Root postprocessing costs
poly(n)2^(sqrt n/4096), including tables and lookups; tail tables have leading
coefficient at most one half. Both are below the ACTUAL sqrt2 main profile
even after the squared-logarithm and polynomial savings. No nonpolynomial
table is silently treated as free or called polynomial. All initialization,
circuit generation, arithmetic, measurements, resets/disposal and wrong-label
work is counted. Address length is O(sqrt n), so

    T=O(n^3 2^(R*sqrt(1+2/(L*)^4))).                 (5)

For z>=0 the supplied positive polynomial P=1+z-z^2/2+z^3/2 obeys
P^2-(1+2z)=(z^4/4)(z^2-2z+5)>=0. Apply it at z=1/(L*)^4.
For v=log2 n the exponent in (5) is at most

    sqrt2 sqrt n+16sqrt2 sqrt n/(v+1)^4
        -128sqrt2 sqrt n/(v+1)^8
        +2048sqrt2 sqrt n/(v+1)^12.

The exact rational inequalities (140/99)^2<2<(99/70)^2 give

    16(99/70)<23, 2048(99/70)<2900,
    128(140/99)*4096^8>180*4097^8.

As v/(v+1) increases, the last comparison proves
128sqrt2/(v+1)^8>=180/v^8 for all v>=4096. The positive terms are
bounded by 23/v^4 and 2900/v^12. Replacing only the leading sqrt2 by a
establishes exactly J2(n). The full quantum stack and active scratch remain
O(n), with root/test registers O(sqrt n) and all large tables classical.

All exponential logarithms are a sqrt n+o(sqrt n), so exact indices are
1/2,1/2,0,1/2. Compared with the original DOUBLELOG, time improves by the
strict lower-order exponent 180sqrt n/v^8-2900sqrt n/v^12 tending to infinity;
classical memory gains 2^-v^2, and source copies gain n^-1/2*2^-v^2. Quantum
space and clean-copy model are identical. This is a different tradeoff from
the scaled logarithmic BLOCKSCALE branch: the time correction is smaller,
while its principal negative memory/source correction is weaker. No all-axis
dominance over that separate branch, global frontier leadership, tight-cost
claim or time-index-1/3 algorithm is asserted.

## 6. Provenance and finite-check limits

The full DOUBLELOG source supplies the inverse-square-logarithm parameter,
finite guard and coefficient conversion. The complete BLOCKBOOST/BLOCKROOT
lineage supplies the wide-root instrument, exact readout, block recovery,
denser SMALL mode and separate typed caps. The new squared-logarithm all-call
boosts, exact shifted profiles, quasipolynomial memory/source gain and signed
curvature conversion are developed here. Direct material predecessors are
declared with exact archive paths, hashes and both-endpoint citations at upload.
Prior acceptance and finite arithmetic checks are not mathematical premises.
