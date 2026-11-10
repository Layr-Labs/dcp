# CYCLIC-GCAP-D: a growing leaf boost and growing terminal plateau

## Algorithm and joint theorem

For every N>=2 and s in Z/NZ, let n=ceil(log2 N). Use the complete
cyclic-window, source-aligned algorithm in cyclic_base.md, with the exact
schedule, retry constant and consequent bounds replaced by this document.
The source is reproduced unmodified from submission
e9fc2eca-9d1c-469b-a629-a43e0f7ce928, candidate
45d9985c85813b2f3d30c62c717faba3621eb57a. Its original fixed16 theorem
concerns different parameters. Here it supplies the explicit circuits,
source identity, collective extractor, cyclic-window instrument and its
freshness proof, top-bit law, general-N recovery instructions and cutoffs.
No previous verdict is a premise; all arguments needed are in the snapshot.

One fixed CYCLIC-GCAP-D configuration outputs the entire s with
unconditional probability at least 1-2^-8. On every branch it satisfies

    T=O(n^3 2^E(n)), S_C=O(n^2 2^F(n)), S_Q=O(n),
    Q=O(n^(11/8)2^F(n)),
    E(n)=a sqrt(n)+(6/5)n^(1/4),
    F(n)=a sqrt(n)-(5/4)n^(3/8)+(6/5)n^(1/4).

The exact rational a=u_333/v_333 and its Pell recurrence are in the
included source's Section 0, which proves a>sqrt2. All constants are
absolute, independent of N,s and outcomes. Epsilon(n)=0 under independent
ideal source copies is the fractional error-tolerance guarantee. It is
not a claim of impossibility of positive tolerance. The exact indices
are 1/2,1/2,0,1/2. Every acquired copy, failure, discard and abort counts.

## 1. Schedule and its elementary capacity proof

For B=D-1>=1 set, by exact integer roots and comparisons,

    mu=ceil(sqrt(2B))+1, kappa=2,
    x=s=floor(mu^(3/4)), q=x+3,
    C(z)=z(z+1)/2-s(s-1)/2+x(z+1)+2,
    m=min{z>=s+1:C(z)>=B}.

The floor is the largest integer v with v^4<=mu^3; it is at most mu-1.
Keep the source's lam_i, bmax_i, root-first greedy bit allocation, leaf
sum table, failed-input disposal and depth-first recursion formulas with
these x,s. In particular lam_i=3+x+min(i,m-s) for i<m, lam_m=1,
and bmax_i=x+i on growing levels, x+m-s+1 on plateau levels, and
2+2x+2(m-s)+1 at the root. Every leaf has q qubits.

Since x=s<=mu-1, the capacity at z=mu satisfies
C(mu)>=mu^2/2>=B: the extra term x mu-x^2/2 is nonnegative,
as are the remaining linear and constant terms. Also mu>=s+1.
Thus m exists and m<=mu. Direct addition and substitution give

    sum bmax_i=C(m)>=B,
    bmax_i+lam_(i+1)-2lam_i=-kappa.

The greedy allocation exists and every measured window is within the
B-bit prefix, as in the included source. The cyclic-window selection
is injective and all selection laws depend only on that prefix.
Consequently the independent-high-bit collision/freshness proof in
cyclic_base.md Section 6 applies unchanged. Averaged over fresh whole
child attempts under its low-prefix invariant, non-root failure is
less than 2^-q; the root has the separate distribution-free bound 1/4.
This is not a bound for every fixed pair of full non-root label tables.

## 2. A uniform retry constant and revised source cap

The leaf boost here can be smaller than the source's fixed16 boost on
small widths. We therefore prove a new retry bound instead of retaining
its numerical factor three. We always have q>=5 and m2^-q<1/2.
For 3<=mu<16, m<=mu<=15<2^(q-1). For mu>=16,
log2(mu)<=sqrt(mu) (the two are equal at 16 and the square-root
derivative is larger thereafter), and sqrt(mu)<=mu^(3/4).
Since q>=mu^(3/4)+2,

    m2^-q<=mu 2^(-mu^(3/4)-2)<=1/4.

For p<=2^-q<=1/32, -log(1-p)<=2p. Thus the product of expected
non-root retry factors and the root factor is less than

    (4/3)exp(2m2^-q)<(4/3)e<4.

The source's argument averages fresh whole attempts, and sums their
reach probabilities without assuming that an attempt's cost is
independent of its success. With leaf acceptance costing at most two
originals in expectation, a returned tree now costs at most
8 A_star originals in expectation, where

    A(B)=q2^m, A_star=max_(1<=B<=n) A(B).

Replace Section 11's Q_star by the explicit integer

    Q_star=8 A_star(G_odd+2a2)+2a2, Qcap=1024 Q_star.

All other literal caps and instructions are unchanged. Compute the exact
maximum by a polynomial number of integer operations before acquiring
source copies. Recompute the extractor confidence from this actual Qcap.
The odd-part root budget G_odd uses the actual new tree size in its seed
and its deterministic small/large mode choice. Its O(n) proof uses only
log2(A(B))=O(sqrt n), which holds here since m<=2mu and q=O(n^(3/8)).
When the odd part is 1 skip its decoder, as in the source.

Expected tree cost, odd-W probability 1/2 and the same reach-probability
accounting now establish the revised expectation Q_star. Markov bounds
source cutoff failure by 2^-10. The unchanged top-bit and source-aligned
recovery proofs, finite parity caps and label coupling retain the source's
other error bounds. Their sum in Section 12 is still less than 2^-8.
All are unconditional first-error/cutoff bounds; no high source bits
are conditioned on an extractor's success or a global cap passing.
The n<64 exhaustive branch and its <=2^-10 error are unchanged.

## 3. Growing-boost depth and space certificate

For analysis put R=sqrt(2B), u=sqrt(R), Z_B=R^(3/4). Then
R+1<=mu<=R+2 and

    Z_B-1<x<=Z_B+2, q<=8 R^(3/4).

The upper bound follows from the mean value theorem applied to t^(3/4)
for t>=1; its derivative is at most 3/4. The coarse constant eight
also covers the +3 in q and every B>=1.

Completing the square gives

    m<=max(s+1,ceil(sqrt(R^2+s^2+(x+1/2)^2)-x-1/2)).

Because x=s<=mu^(3/4),

    s^2+(x+1/2)^2<=2mu^(3/2)+mu^(3/4)+1/4.

Concavity of the square root bounds the square-root candidate plus x
by R plus half this expression divided by R, plus one. In particular,
mu<=R+2 and the mean value theorem give

    mu^(3/2)/R <= sqrt(R)+5,
    mu^(3/4)/(2R) <=3/2, 1/(8R)<=1/8,

for R>=sqrt2; the first uses
(R+2)^(3/2)-R^(3/2)<=3sqrt(R+2)<=5sqrt(R) here.
Thus a uniform bound of R+sqrt(R)+32 covers that candidate.
For the lower constraint, 2mu^(3/4)<=mu+2 for all mu>=0:
writing t=mu^(1/4), the polynomial t^4-2t^3+2 has its global
nonnegative-domain minimum 5/16 at t=3/2. Hence
s+1+x=2x+1<=mu+3<=R+5, covered by the same bound. We obtain

    m+x<=R+sqrt(R)+32,
    m+x-s<=R-R^(3/4)+sqrt(R)+33.                  (1)

Together with x>=R^(3/4)-1 and q<=8R^(3/4), this gives

    A(B)<=C R^(3/4)2^(R-R^(3/4)+sqrt(R)).          (2)

The function f(R)=R-R^(3/4)+sqrt(R) is increasing for R>=1,
since f'(R)>=1-3/4=1/4. Taking the maximum over all actual widths
therefore yields, for Z=(2n)^(3/8),Y=(2n)^(1/4),

    A_star=O(n^(3/8)2^(sqrt(2n)-Z+Y)),
    Q<=Qcap=O(n^(11/8)2^(sqrt(2n)-Z+Y)).          (3)

This uses the one actual configuration and exact maximum, not separately
chosen configurations for time and samples.

## 4. Every-branch resource ledger

The source's deterministic tree charge per acquisition is
O(n(m+1)2^kappa 2^x/q), including every failed attempt and cutoff-
abandoned subtree. At most one merge per level can charge a particular
acquisition, because failed inputs are discarded. Here m=O(sqrt n),
kappa=2, q=x+3. The function 2^v/(v+3) is increasing for v>=1;
x<=Z+2 and Z>=1 imply

    2^x/q<=2^(Z+2)/(Z+5)<=4 2^Z/Z.

Every tree width thus has the common deterministic charge
O(n^(9/8)2^Z) per acquisition. Multiplying by (3) gives

    tree core work=O(n^(5/2)2^(sqrt(2n)+Y)).       (4)

Source transforms and collective label extraction take O(n^2) per
copy, so their total is O(n^(27/8)2^(sqrt(2n)-Z+Y)), below (4).
Seed decoding is O(n^2 A_star) plus polynomial setup, also below (4).
All source feedback, gate generation, initialization, classical processing,
measurements, disposal and wrong-label branches have the same finite
width/cap bounds as in the included source. Acquiring sources explicitly
costs (n+1)Qcap, which is included and is smaller than (4).

The depth-first quantum stack remains O(n), since m=O(sqrt n),
x=O(n^(3/8)) and every lam_i=O(sqrt n). Active merge, source and
extractor scratch are O(n). All tables and classical scratch are bounded
by O(n^2 max_(B<=n)2^(x+m-s)) plus polynomial workspace. Equation (1)
and monotonicity of f give

    S_C=O(n^2 2^(sqrt(2n)-Z+Y)).                  (5)

The exponent is eventually positive of order sqrt n, absorbing the
polynomial-only scratch and finite initial range into an absolute
constant. Address length is O(sqrt n), so (4) gives total charged work

    T=O(n^3 2^(sqrt(2n)+Y)).                      (6)

Equations (3),(5),(6) and S_Q=O(n) are simultaneous every-branch bounds
for the configuration whose recovery probability was proved in Section 2.

## 5. Exact envelopes and provenance

Since a>sqrt2, 6/5>2^(1/4), and 5/4<2^(3/8), termwise comparison
gives exactly E,F in the theorem and structured declarations. The
exponential logarithms are a sqrt n+o(sqrt n), so all three exponential
envelopes have exact index 1/2. The quantum envelope n has index 0.
No unspecified inner coefficient is replaced by a guessed value.

The complete cyclic-window proof and source-aligned decoder are reused
from e9fc2eca-9d1c-469b-a629-a43e0f7ce928. The growing plateau and its
explicit paid-overhead analysis develop this session's GCAP work. The
new configuration grows the LEAF boost as well as the terminal plateau;
it gives both classical memory and total source copies a 3/8-power
saving, rather than only a fourth-root saving in sources. It uses a
new explicit uniform retry constant and a correspondingly larger
literal cap. The original source's references are retained in full.
This is a distinct time/source tradeoff, not a claim of a 1/3 time
index, practical runtime or global frontier leadership.
