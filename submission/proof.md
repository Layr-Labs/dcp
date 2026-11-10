# CYCLIC-TRIPLEBOOST: inverse-cubic-log schedules with complete block accounting

## 1. Full construction and simultaneous claim

The complete primitive cyclic-window/source-aligned algorithm is supplied
unchanged as cyclic_base.md from e9fc2eca-9d1c-469b-a629-a43e0f7ce928, commit
45d9985c85813b2f3d30c62c717faba3621eb57a. It supplies the exact Clifford+T
source transformations, collective label extraction, explicit lookups and
merge circuits, conditional freshness/collision proof, top-bit law, scored
backward lemma, all-modulus identities and finite algorithm. The complete
counted rational logarithm is supplied as log_base.md from CYCLIC-LOG
1f1debc0-0a4b-409c-bcc4-1eb8c5c9d470, commit
07a195ac7f4dbfc975beddec776c818994c936d1. Their old resource theorems concern
their old configurations. The complete replacement block algorithm and all
new probability/resource arguments are given here; no missing manuscript or
prior verdict is a premise. Material block/typed-cap predecessors developed
in this session are declared with exact citations at upload.

For every N>=2 and every s in Z/NZ, n=ceil(log2 N), ONE fixed uniform
configuration recovers the entire s with unconditional probability at least
1-2^-8 from independent ideal copies. On every execution branch jointly,

    T=O(n^3 2^J(n)),
    S_C=O(n^(3/2)(log2 n)^(-6)2^G(n)), S_Q=O(n),
    Q=O(n(log2 n)^(-3)2^G(n)),
    J(n)=a sqrt(n)+91sqrt(n)/(log2 n)^6
                  -2800sqrt(n)/(log2 n)^12
                  +186000sqrt(n)/(log2 n)^18,
    G(n)=a sqrt(n)-11sqrt(n)/(log2 n)^3
                  +91sqrt(n)/(log2 n)^6-(log2 n)^3.

The exact Pell rational a=u_333/v_333, with its proof a>sqrt2, is supplied
in cyclic_base.md Section 0. Constants are absolute and independent of N,s
and outcomes. These eventual positive representatives are evaluated for
n>=2^4096 and extended positively on the finite smaller prefix; correctness
covers every N. Their exact indices are 1/2,1/2,0,1/2. Malformed fraction
is zero under independent ideal copies, with no positive robustness or
maximum possible tolerance assertion. Every original copy counts, including
failed, rejected, discarded and cutoff-abandoned acquisitions.

For n<2^4096 run the complete original fixed16 cyclic-window algorithm
supplied in cyclic_base.md with its literal caps, including its n<64
exhaustive branch. This finite public-input branch has unconditional
success at least 1-2^-8 and finite worst-case resources, absorbed by absolute
outside constants in all stated eventual envelopes. No input is excluded
from recovery. Below assume n>=2^4096.

## 2. Counted parameters and actual schedule maxima

Write ln for the natural logarithm; all log2 notation is base two. Compute

    t=ceil(log2(n+2)), h=max(1,floor(isqrt(n)/8192)),
    Dcut=2^20(h+t+1)^2, lambda(b)=2b+2t+40, 1<=b<=h.

Integer roots, bit lengths and arithmetic are counted bit algorithms. For
auxiliary width V>=1 compute mu=ceil(sqrt(2V))+1. Use the EXACT rational
ell(mu) from log_base.md Section 2, as follows. For k=floor(log2 mu),
J0=k+20, z=(mu-2^k)/(mu+2^k), compute

    A=2 sum_(j<J0) z^(2j+1)/(2j+1),
    B0=2 sum_(j<J0) (1/3)^(2j+1)/(2j+1),
    delta0=(9/4)3^(-2J0-1), ell=k+(A+delta0)/B0.

The integrated geometric series for the natural logarithm, B0>=2/3 and
its positive tail bound delta0 prove
log2(mu)<=ell<=log2(mu)+1/mu. There are O(log mu) terms with polynomial
operand bit length in log mu, hence counted polynomial setup work and bits.
This is not advice or unit-cost real arithmetic.

Fix the inverse-cubic-log base and finite guard:

    x0=max(2,floor(mu/(ell(mu)^3))),
    kappa=ceil(log2 mu)+1 if mu<65536, and 2 otherwise.

For ell=r/d the base floor is exact division floor(mu d^3/r^3).
OTHER calls use x=s=min(mu-1,x0+t^3). SEED calls use
x=s=min(mu-1,x0+t^3+2t). Put q=kappa+1+x and define

    C(m)=m(m+1)/2-s(s-1)/2+x(m+1)+kappa,
    m=min{z>=s+1:C(z)>=V}.

Always 2<=x=s<=mu-1. Capacity holds at mu because x=s and
x mu-x^2/2>=0, so m<=mu. Every schedule is a fixed public function of
n and V, used identically across the simultaneous resource claims.

A one-bit tree at actual label width D>=2 uses V=D-1. A wide tree at
actual width D>Dcut retaining b<=h bits uses V=D-b+lambda(b)-1 and
B=D-b actual low bits. The latter auxiliary width may exceed n slightly;
all maxima below use its actual value. Compute literal integer maxima:

    Ao=max q2^m over OTHER one-bit widths 2<=D<=n, including 1;
    As=max q2^m over SEED one-bit widths 2<=D<=n, including 1;
    Aw=max q2^m over OTHER wide widths Dcut<D<=n,1<=b<=h, including 1;
    Ac=max q2^m over OTHER one-bit widths 2<=D<=min(n,Dcut), including 1;
    Rbar=max(Ao,As,Aw,1), ellbar=ceil(log2 Rbar),
    nu=ceil(log2(n+ellbar+28)).

Empty maxima equal one. Width one uses the parity single-label procedure
specified below. All polynomially many maximum computations are counted;
the algorithm never substitutes an asymptotic maximum into its literal caps.

## 3. Exact tree, fresh retries and high-block invariants

Use cyclic_base.md's generic boosted vectors, leaf sum table, explicit
lookups and cyclic-window merge at these actual parameters. Below the root,
index lengths are lam_i=kappa+1+x+min(i,m-s). The generic capacities are
x+i on growing levels, x+m-s+1 on plateau levels, and
kappa+2x+2(m-s)+1 at a one-bit root. Their sum is C(m), and every merge
satisfies bmax_i+lam_(i+1)-2lam_i=-kappa. Root-first greedily allocate the
required low bits; unused capacity is harmless.

For a wide root change ONLY the final length from one to lambda(b), and
reduce its capacity by lambda(b)-1. The capacity sum becomes
C(m)-lambda(b)+1>=D-b, and the slack identity remains exactly -kappa.
All actual windows lie below D-b. The root output fits its inputs and all
capacities are nonnegative: the public bounds below show x<=R/4,
m>=R/4 and lambda(b)<m+kappa+1=lam_(m-1), R=sqrt(2V).

First t+1<=log2(n)+3 and, for log2 n>=4096,
sqrt n>=8192(log2(n)+3). The ratio increases with log2 n and the
left-endpoint integer comparison holds. Hence h=Theta(sqrt n),
h+t+1<=sqrt n/4096 and Dcut<=n/16. If D>Dcut then
R>1448(h+t+1). On this range x0<=R/8 and t^3+2t<=R/8:
R is a fixed positive multiple of sqrt n, whereas t^3+2t is polynomial
in log2 n; their ratio is increasing beyond the threshold and its endpoint
comparison holds. If m<R/4 and x<=R/4, then
C(m)<=m^2/2+(x+1/2)m+3x/2+kappa<R^2/2=V, a contradiction.
Thus m>=R/4>362(h+t+1)>lambda(b), proving the claimed root fit.

In the ideal process all accepted D-bit source labels are independent
uniform. The cyclic-window instrument is the EXACT source circuit: measured
bucket plus uniformly measured cyclic rank offset and injective reindexing,
with equal output magnitudes. Its next outcome law depends only on exposed
low source bits; retained high blocks remain independent uniform. Distinct
binary incidence vectors persist through disjoint-child tensoring and
injective rank maps. Therefore the full conditional freshness/collision
proof applies at every new width. Fresh non-root failure is <2^-q under
whole-child averaging, while root failure is <=2^-kappa<=1/4 pointwise.
This is not a claim for every fixed full non-root high-label table.

The retry constant is uniform. If mu<65536, kappa<=17 and
2^kappa>=2mu, q>=kappa+3 give m2^-q<=1/16. If mu>=65536, with
L_mu=log2 mu>=16, the rational enclosure and flooring give
mu/L_mu^3-2<=x0<=mu/L_mu^3. The derivative error is at most 3/L_mu^4<1.
Since 2^16=16^4 and 2^L/L^4 increases for L>=16, mu>=L_mu^4.
Thus q>=mu/L_mu^3+1>=L_mu+1 and m2^-q<=1/2. The shifts can only
increase q. From -ln(1-p)<=2p for p<=1/32, the complete retry product
is <=(4/3)e<4. The source acceptance loss at most two therefore gives
expected original copies <=8q2^m per returned tree. Fresh-whole-attempt
reach accounting does not assume independence of cost and success.

One-bit roots retain the exact source top-bit law. Conditional on low-only
history and independent past, their multiplier is
W=c_low+sum epsilon_j tau_j with nonzero signed incidence difference and
independent fair source top bits. Consequently |W|<2q2^m<=2Rbar,
Pr[W odd]=1/2 and |E exp(2pi i zW)|<=|cos(pi z)| for every real z.
Private extractor outcomes are averaged out in this ideal statement.

## 4. Complete balanced wide-root measurement

A returned wide root has L0=2^lambda(b) equal-magnitude rows, with known
high labels v_j and M0=2^b. Conditional on its low-only transcript,

    v_j=c_j+sum_l I_(j,l) tau_l modulo M0,

where tau_l are independent uniform b-bit blocks and the distinct binary
incidence vectors I_j and carries c_j are fixed. Every nonempty form is
uniform. Two distinct nonempty binary vectors are independent over F2;
an odd 2-by-2 minor makes the paired forms surjective modulo M0. At most
one incidence is empty. Thus residue count C_r has variance <=L0/M0 and
mean within one of L0/M0. Chebyshev and the union bound yield

    Pr[some C_r outside [L0/(2M0),3L0/(2M0)]]
       <=16M0^2/L0<=2^-36/(n+2)^2.

This holds uniformly over low transcripts and previous failed attempts.

Classically test these counts. Discard the entire root if unbalanced.
Otherwise set K=min_r C_r and select the first K rows of each residue
in fixed index order. Mark them by explicit lookup, measure the flag,
and discard the entire root on zero. Success probability is exactly
M0 K/L0>=1/2, independent of phases. On success bijectively reindex each
selected row as (r,k), 0<=r<M0,0<=k<K, by explicit lookup and inverse
lookup to clear the old index. Invalid encodings have arbitrary total
reversible extensions. As K<=L0/M0, the output encoding fits the old index.
All tables and their costs are counted below.

If the root's high-label phase is v_j(a/M0+epsilon), then at epsilon=0
the selected normalized state is exactly

    M0^(-1/2)sum_r exp(2pi i a r/M0)|r>
       tensor K^(-1/2)sum_k |k>.

Discard k. The remaining register is an exact modular-translation eigenstate.
Use cyclic_base.md Section 5's collective exact controlled translations,
direction tests and dyadic unwrap at modulus M0 to read a. Use levels
0,...,b+4, confidence ceil(log2((b+5)(n+1)))+64 and per-basis count
2^21 times that integer. Ideal error eta<=2^-60/(n+1). The controlled
translations act on the root, require no original source copies and need
no inverse QFT, approximate rotations or QRAM.

For nonzero epsilon, all selected magnitudes and normalization are identical
to the ideal case, and Euclidean distance is <=e=2pi |epsilon|vmax,
vmax<2^b q2^m<=2^b Rbar. Triangle inequality for the wrong-outcome projector
gives Pr[wrong a | selected]<=2eta+2e^2, also after discarding k.
Selection normalization has no extra cost because flag probability is
exactly the same for both states.

A whole attempt creates a fresh root, tests counts and measures the flag.
Its selection probability exceeds 1/3 uniformly. Use at most
Ktry=64(t+40) whole attempts per block; otherwise abort to zero. Expected
attempts are at most three, and abort probability <=(2/3)^Ktry
<=2^-32(t+40). Costs may correlate with selection; uniform fresh-attempt
expectation/reach accounting still bounds a selected block by 24q2^m
original copies. Equal magnitudes and uniform stored labels make these
cost/selection laws hold after wrong decoder decisions too. Correct phase
identities are used only on the first-error-success path.

## 5. Seed localization, fully specified

Factor N=2^a2 M with M odd; d=floor(log2 N), s1=s mod M. If M=1 skip
odd recovery. Otherwise H=ceil(log2 M), theta=s1/M. A SEED one-bit root
at physical scale j uses actual D=d, B=d-1>=a2. Before label extraction
apply the source's exact Mult_alpha with CRT unit
alpha=1 mod2^a2 and alpha=2^j*(2^(B-a2))^-1 mod M. Accept labels k<2^d,
with probability >1/2, apply X and run the SEED tree. Its root phase is
W2^j theta exactly by the supplied source identity, with the characteristic
law and bound from Section 3. This transformation is on original coset copies.

Use local stages u=0,...,ellbar+27 and

    Kseed=32768(ellbar+nu+80), Fseed=(ellbar+28)Kseed,
    P_u=u+ellbar+28.

At each stage take Kseed fresh SEED roots at physical scale H+u, measure
in independent fair X/Y bases, and score dyadic grid candidates c using
the supplied exact rational trigonometric table at 2^u Wc. Stage zero uses
the full grid of denominator 2^P_u; later stages use its points in the
closed circular arc of radius 2^(-u-2) about the previous center. Stream
them and retain the least maximizer.

Conditional on prior success, the true phi=2^H theta lies in the arc.
A nearest grid point has phase error <=2^-28 using |W|<2Rbar<=2^(ellbar+1).
A point at distance >=2^(-u-3) has 2^u circular distance in [1/8,1/2],
so its mean score is <=cos(pi/8)/2 by the characteristic bound. The near
mean is at least the stronger version of cos(pi/128)/2 from the full
source proof. Its exact positive table/Azuma score margin in Section 9.2.1
therefore still applies. At most 2^(ellbar+28) candidates give at most
2^(ellbar+30) one-sided events, each <=2^(-ellbar-nu-80). A first-error
union over all stages is <=2^-50. The final center z_H satisfies

    ||2^H theta-z_H||<=e0=2^(-ellbar-30)<=1/(2^30 Rbar).

Every value is rational/integer, and consecutive-candidate score updates
use the supplied streamed O(n^2 Rbar)+poly(n) implementation. No score
array, numerical oracle or source postselection is assumed.

## 6. Odd-component backward recovery

Choose LARGE iff M>=2^30*2^h*Rbar*ceil(sqrt n). Otherwise use SMALL.
In SMALL, for j=H-1,...,0 form inverse lifts u0=z/2,u1=(z+1)/2 and use
Kback=512(nu+60) fresh SEED one-bit roots at scale j with the exact
Section 9.1 two-candidate score. Incoming error <=e0<=1/(64Rbar), so
its theorem applies with this actual multiplier bound. Correct error halves;
first-error probability over H steps is <=2^-60. The count H Kback is
literal. Failed LARGE test implies H<=ellbar+h+O(log n)=O(sqrt n),
so this count is O(sqrt n log n)=O(n). All these calls have SEED type.

In LARGE start at jold=H and center z_H. While jold>0 set b=min(h,jold),
j=jold-b and u_a=(z+a)/2^b for a=0,...,2^b-1. Compute exactly
t0=floor(Mu0+1/2) with ties upward, and bshift=(2^j)^-1 t0 mod M.
Use fresh copies with Shift_bshift FIRST and Mult_alpha SECOND, where
alpha=1 mod2^a2 and alpha=2^j*(2^(B-a2))^-1 mod M, B=d-b.
The guard ensures floor(log2 M)>h, so B>=a2 and this CRT source identity
is valid. Accept k<2^d, apply X, and make an OTHER wide root retaining b.
Its high-label phase is exactly

    v 2^B alpha(s-bshift)/N
       =v(2^j theta-t0/M)=v(a/2^b+epsilon) mod 1,
    |epsilon|<=e_in/2^b+1/(2M)

for the correct inverse lift. Read a with Section 4 and set z=u_a,
jold=j. The stored error shrinks exactly by 2^b; rounding t0 affects only
the physical test shift and is not accumulated into the center.

On a first-error-success history the per-block wrong probability is at most
2eta+16pi^2 Rbar^2 e_in^2+4pi^2 Rbar^2 2^(2h)/M^2. Incoming errors shrink
by at least two, so summing at most n blocks gives

    2n eta+(64/3)pi^2 Rbar^2 e0^2
              +4pi^2 n Rbar^2 2^(2h)/M^2 <2^-45.

Whole-attempt cap errors add at most n2^-32(t+40). Conditional selection
needs no hidden success premise: it is an actual capped operation, and the
state error bound is pointwise in every selected high-label table. In either
mode final error e0/2^H<1/(2M); circular rounding of Mz gives s1, including
zero and wraparound/binary-boundary phases. All failure branches still
return a defined residue.

## 7. Power-of-two component and exact typed caps

If a2=0 skip. Otherwise after s1 maintain low g bits of s2 with
s=s1+M s2 mod N. Put sh_g=s1+M s2low mod N, wd=a2-g and
rem=(s2-s2low)/2^g. Apply Shift_sh_g on each fresh copy, extract its latent
k, apply X to the CONTROL qubit exactly as in cyclic_base.md Section 10,
and use kk=k mod2^wd, uniform. On correct history its control phase is
kk rem/2^wd. If wd>Dcut, use an OTHER wide tree at D=wd retaining b=h;
its high phase is exactly v rem/2^h. The selected eigenstate readout gives
rem mod2^h with error <=eta. Append those h bits. There are at most
ceil(a2/h) wide calls.

When wd<=Dcut use the full original one-bit parity method with OTHER trees.
An odd W occurs with probability one half; measure X to read the next bit
exactly on correct history. At wd=1 take a single kk=1 label, otherwise
discard and retry. Use at most K2=ceil(log2 n)+30 attempts per bit. At most
min(a2,Dcut) tail bits give total parity-cap failure <=2^-30 and expected
attempts at most two per bit. Even after earlier errors, stored labels are
uniform and all index magnitudes stay equal, so these cost and retry laws
remain valid; only phase interpretation requires earlier correctness.
Return (s1+M s2) mod N.

With all odd terms zero if M=1, define computable integer expectation budgets

    U_seed=8 As [Fseed+1_SMALL H Kback],
    U_other=1_LARGE 24 Aw ceil(H/h)
              +24 Aw ceil(a2/h)+16 Ac min(a2,Dcut)+2.

Factors eight include at most two source acceptance loss and below-four
internal retries; three is the whole-wide-attempt expectation; two is tail
parity. All expectations hold uniformly after any earlier history, without
conditioning on correct labels or successful decoding. Enforce SEPARATELY

    Q_seedcap=4096 U_seed, Q_othercap=4096 U_other,
    Q_global=Q_seedcap+Q_othercap.

Every acquired copy keeps its fixed public call type. Both caps count all
failures/discards; exceeding either aborts to zero. Markov gives at most
2^-11 total cutoff error in the uncapped ideal process. Each original
source's full collective label extractor uses confidence
ceil(log2(Q_global(n+5)))+20 and test count 2^21 times that integer per basis,
giving union coupling error <=2^-18. Section 4's root readout needs no new
original copies. The seed, SMALL/LARGE, readout/selection, parity, extraction
and cutoff first-error bounds sum to less than 2^-8. This is an unconditional
comparison, not a no-error or no-postselection resource premise. Literal
widths and caps constrain every wrong-label/abort branch too.

## 8. Uniform exact profiles and actual source maxima

For analysis let R=sqrt(2V), L=log2 R, u=L^-3,
g(R)=R/L^3 and f(R)=R[sqrt(1+2/L^6)-1/L^3]. For R>=256,
g is increasing with bounded derivative and

    f'=S-u-eta*u*(2u/S-1),
    S=sqrt(1+2u^2), eta=3/(ln(2)L)<3/4.

Because S-u>1/2 and 2u/S<7/6 for u<=1, f'>3/8. The finite smaller
widths and finite kappa guard are covered by an absolute constant. Rounded
precision x0=g+O(1) follows from the rational enclosure and R+1<=mu<=R+2.
Completing the capacity square bounds m by the maximum of s+1 and
ceil(sqrt(R^2+s^2+(x+1/2)^2)-x-1/2), dropping the harmless negative kappa
term. For unshifted x=s=g+O(1) this gives m+x<=RS+O(1), m<=f+O(1).

For delta=t^3 or t^3+2t and R>=n^(1/4), the min is inactive eventually,
x=g+delta+O(1), and the extra square-root change is
O(g delta/R+delta^2/R+1)=O(delta/L^3+delta^2/R+1)=O(1), uniformly.
The lower constraint 2x+1 fits RS+O(1) because x/R tends uniformly to
zero. Thus m+x<=RS+O(1), m<=f-delta+O(1). For R<n^(1/4), m<=mu and
q=O(mu) give 2^O(n^(1/4)), below the global bounds even after division
by 2^(t^3) and fixed polynomials. Wide V<=n+O(sqrt n) changes the largest
R by O(1), so bounded derivatives preserve all full exponential bounds.
No rounded integer profile is assumed monotone.

For R*=sqrt(2n), L*=log2 R*, g*=g(R*), f*=f(R*), actual maxima satisfy

    Ao,Aw=O(g*2^(f*-t^3)), As=O(n^-2 g*2^(f*-t^3)).

Hence ellbar=O(sqrt n), Fseed=O(n), SMALL H Kback=O(n), and the total
wide-block budget is O(sqrt n). The crude tail bound
Ac<=poly(n)2^(sqrt(2Dcut)+2)<=poly(n)2^((1/2)sqrt n) has a strict leading
gap below f*/sqrt n→sqrt2, even after the cubic-log saving. Literal caps give

    Q_global=O(sqrt n g*2^(f*-t^3))
       =O(n(log2 n)^(-3)2^(f*-t^3)).                (1)

For v=log2 n, concavity yields

    f*<=sqrt2 sqrt n-8sqrt2 sqrt n/(v+1)^3
                        +64sqrt2 sqrt n/(v+1)^6.

Exact rational bounds sqrt2>140/99 and sqrt2<99/70 give
8(140/99)*4096^3>=11*4097^3 and 64(99/70)<91. As v/(v+1) increases,
f*<=a sqrt n-11sqrt n/v^3+91sqrt n/v^6 on v>=4096. Since t^3>=v^3,
(1) gives exactly the submitted source envelope G.

## 9. Every-branch work and both peak allocations

The deterministic tree charge per acquired copy is
O(n(m+1)2^kappa 2^x/q), by disjoint ancestry at each level and discarded
failed inputs. It includes abandoned partial trees. Wide output rows do
not exceed input rows, so the full source's O(n(Lin+Lout)) merge charge
still applies. Uniformly the OTHER charge is
O(n^(3/2)2^(g*+t^3)/g*); SEED has the additional factor 2^(2t)=Theta(n^2).
Multiplying EACH by its OWN literal typed cap cancels 2^(t^3), and cancels
n^2 for SEED. Total tree core work is

    O(n^(5/2)2^(R*sqrt(1+2/(L*)^6))).

Original source transforms and collective labels cost O(n^2) per acquired
copy, and the retained negative g* makes their total smaller. Explicit
original acquisition cost (n+1)Q_global is smaller as well. Streamed
seed scoring O(n^2 Rbar), feedback and polynomial setup are also smaller.
Root postprocessing has L0<=poly(n)2^(sqrt n/4096) rows; every count, flag,
selection map, inverse lookup and collective translation is explicitly
counted. Polynomially many capped whole attempts give total
poly(n)2^(sqrt n/4096) charged work. The tail has leading coefficient at
most one half. Both are strictly below the ACTUAL sqrt2 main profile after
all cubic-log/polynomial savings; no nonpolynomial table is silently free.
All initialization, generation, lookups, arithmetic, measurements, reset,
disposal, wrong labels, failed roots and cutoff-abandoned work count.
Address length is O(sqrt n), yielding

    T=O(n^3 2^(R*sqrt(1+2/(L*)^6))).                 (2)

Depth-first quantum indices have sum O(m^2+qm)=O(n), and source modular
circuits and active scratch use O(n). Wide-root/test registers add only
O(sqrt n). Exponential tables are classical and streamed, not one coherent
register per table row. Thus S_Q=O(n) on every branch.

A level-i stored high-part field has width
w_i=D+i+ceil(log2 q)-p_i=O(sqrt n(m-i+1)), including retained b high bits,
remaining capacity windows and source carries. All common residues and
row/rank/lookup scratch fit the same per-level bound. There are constantly
many resident tables per level. The last s plateau levels at
lambda_max=m+kappa+1 sum to O(sqrt n s^2 2^lambda_max); growing levels
have a smaller geometric tail. At large widths s=O(g*), so

    S_C=O(n^(3/2)(log2 n)^(-6)2^(f*-t^3))
       =O(n^(3/2)(log2 n)^(-6)2^G(n)).

SEED m is lower by another 2t and is no larger. Smaller-width, root-table,
extractor/score, residue and setup allocations have smaller leading scales
and are included. Fixed fields remain allocated even if numeric values or
labels are wrong. Allocation, reset and release were charged above.

For the exact time conversion define P(z)=1+z-z^2/2+z^3/2>0 for z>=0.
Its square minus (1+2z) is (z^4/4)(z^2-2z+5)>=0. Apply sqrt(1+2z)<=P(z)
to z=1/(L*)^6 in (2). The exponent is at most

    sqrt2 sqrt n+64sqrt2 sqrt n/(v+1)^6
        -2048sqrt2 sqrt n/(v+1)^12
        +131072sqrt2 sqrt n/(v+1)^18.

The exact comparisons 64(99/70)<91,131072(99/70)<186000 and
2048(140/99)*4096^12>=2800*4097^12, together with monotonic v/(v+1),
prove exactly J(n). Replacing only leading sqrt2 by a changes no other
coefficient. All exponential logarithms are a sqrt n+o(sqrt n); the exact
resource indices are 1/2,1/2,0,1/2 as declared.

## 10. Comparison, provenance and verification scope

This is a new fixed inverse-cubic-log configuration with actual cubic-log
boosts and a fully specified block decoder. Its time correction is of order
sqrt(n)/log2(n)^6, smaller than the inverse-square-logarithm branch's
sqrt(n)/log2(n)^4. Its principal negative memory/source correction is weaker,
of order sqrt(n)/log2(n)^3 instead of sqrt(n)/log2(n)^2. It is a tradeoff,
not an all-axis dominance claim. No tight-cost, practical-speed, global
frontier or time-index-1/3 result is asserted.

The full primitive cyclic and rational-log sources are supplied. The wide-root
balance/readout, all-modulus blocks and typed-cap methods materially build on
the earlier BLOCKLOG/BLOCKROOT/BLOCKBOOST/DOUBLEBOOST work developed here;
all relevant arguments have been reproduced in this manuscript, so no absent
amendment or prior acceptance is needed. Material published predecessors are
declared at upload with exact submission/ archive paths, full-file hashes and
both-endpoint passages. Finite arithmetic/instrument checks debug formulas;
they are not an end-to-end quantum recovery simulation or proof premise.
