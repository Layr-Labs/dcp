# CYCLIC-BLOCKLOG: balanced wide roots, block decoding and separately capped seeds

## 1. Complete source and joint theorem

The complete cyclic-window/source-aligned construction is supplied unchanged
as cyclic_base.md from e9fc2eca-9d1c-469b-a629-a43e0f7ce928, commit
45d9985c85813b2f3d30c62c717faba3621eb57a. The complete counted rational
logarithm and balanced-family argument is supplied as log_base.md from
CYCLIC-LOG 1f1debc0-0a4b-409c-bcc4-1eb8c5c9d470, commit
07a195ac7f4dbfc975beddec776c818994c936d1. The full retuned logarithmic
schedule and curvature ledger developed in this session are supplied as
logscale_base.md. All are mathematical arguments, not prior-verdict premises.
Replace their one-bit decoder, common source cap and parameters as specified
below. The primitive exact circuits, lookups and source reductions remain
those supplied in full; no new source oracle or QRAM is introduced.

For every N>=2 and s in Z/NZ, n=ceil(log2 N), ONE uniform algorithm recovers
the entire s with unconditional probability at least 1-2^-8 from independent
ideal copies. Jointly on every execution branch,

    T=O(n^3 2^J(n)),
    S_C=O(n^(3/2)(log2 n)^(-2)2^F(n)), S_Q=O(n),
    Q=O(n^(3/2)(log2 n)^(-2)2^F(n)),
    J(n)=a sqrt(n)+(9/2)sqrt(n)/(log2 n)^2
                  -7sqrt(n)/(log2 n)^4+23sqrt(n)/(log2 n)^6,
    F(n)=a sqrt(n)-(5/2)sqrt(n)/(log2 n)+6sqrt(n)/(log2 n)^2.

The exact Pell rational a=u_333/v_333, with its proof a>sqrt2, is in
cyclic_base.md Section 0. All constants are absolute and independent of N,s
and outcomes. These eventual positive envelopes are evaluated for n>=2^1024
and extended positively on the finite smaller prefix. Correctness covers
every N. Exact indices are 1/2,1/2,0,1/2. Malformed fraction is zero under
independent ideal copies, not a maximum possible tolerance assertion.

The substantive new result is a factor log2(n) improvement in the source
upper bound relative to logscale_base.md, with its full time, space and
clean-copy guarantees retained. It uses wide-root Fourier-label extraction,
block backward decisions, a separately configured cheaper-source seed, and
TWO type-specific source caps. It does not assert a time index of 1/3,
tight actual resource functions, practical speed or global frontier leadership.

For n<2^1024 run the complete old LOGSCALE algorithm with its literal caps.
This is a finite public-input branch and is absorbed by absolute outside
constants in all declared envelopes, including the extra logarithmic source
factor. The algorithm still covers this entire prefix. Below assume n>=2^1024.

## 2. Public integer parameters and exact maxima

Write ln for the natural logarithm and log2 for base two. Set

    t=ceil(log2(n+2)), h=floor(log2 n), Dcut=2^20(t+1)^2,
    lambda(b)=2b+2t+40 for 1<=b<=h, delta_n=2t.

All ceil logarithms are exact integer bit-length instructions. Every rational
ell(mu) is generated and charged by log_base.md, with
log2(mu)<=ell(mu)<=log2(mu)+1/mu. For an auxiliary width V>=1 define

    mu=ceil(sqrt(2V))+1,
    x0=s0=max(2,floor(8mu/(9ell(mu)))),
    kappa=ceil(log2 mu)+1 if mu<32, and 2 otherwise.

The BASE schedule uses x=s=x0, q=kappa+1+x and least m>=s+1 with

    C(m)=m(m+1)/2-s(s-1)/2+x(m+1)+kappa>=V.

The SEED schedule uses x=s=min(mu-1,x0+delta_n) and the same kappa and
capacity prescription. In both cases m<=mu by x=s and capacity at mu;
q>=5. Increasing x from x0 can only improve the proof q>=log2(mu)+1
in the unguarded regime. The guarded regime satisfies m2^-q<=1/16.
Thus both have retry product <=(4/3)e<4 by logscale_base.md's proof.

A one-bit tree at actual label width D>=2 uses V=D-1 and root index
length one. A WIDE tree at actual label width D>Dcut, retaining b<=h
bits, uses the BASE schedule at

    V=D-b+lambda(b)-1,
    B=D-b.

Its non-root lengths and capacities are the generic source formulas with
these x,s,kappa,m. Change only root output length from one to lambda(b)
and root bmax from kappa+2x+2(m-s)+1 to
kappa+2x+2(m-s)+2-lambda(b). Greedily allocate exactly B actual low bits
root-first. The sum of capacities is C(m)-lambda(b)+1>=B, and every
merge obeys bmax_i+lambda_(i+1)-2lambda_i=-kappa. All windows lie in
the B-bit low prefix and leave b source bits unexposed.

The wide root capacities are nonnegative, and lambda(b)<=lambda_(m-1).
Here is an explicit sufficient estimate. For D>Dcut, R=sqrt(2V) exceeds
1448(t+1), while log2 R>10, mu<=R+2 and x0<=R/4. If m<R/4, then
C(m)<=m^2/2+(x+1/2)m+3x/2+kappa<R^2/2=V (R>100), a contradiction.
Thus m>=R/4>362(t+1)>lambda(b), as lambda(b)<=4t+40 and t>=1024.
At the last non-root level lambda_(m-1)=m+kappa+1 because s>=2.
These estimates also show that the wide output table has no more rows
than its input tables. All actual formulas use integer comparisons;
none assumes monotonicity of rounded schedules.

Compute exact public maxima before acquisition:

    Ao=max q2^m over BASE one-bit widths 2<=D<=n, including 1;
    As=max q2^m over SEED one-bit widths 2<=D<=n, including 1;
    Aw=max q2^m over WIDE widths Dcut<D<=n, 1<=b<=h, including 1;
    Ac=max q2^m over BASE one-bit widths 2<=D<=min(n,Dcut), including 1;
    Rbar=max(Ao,As,Aw,1), ellbar=ceil(log2 Rbar),
    nu=ceil(log2(n+ellbar+28)).

Empty maxima equal one. These polynomially many integer computations have
polynomial work and bit length in n and are charged. Width one uses the
source's single-label parity procedure. Every source extraction confidence
uses the actual final cap in Section 7, including all failed/discarded copies.

## 3. A balanced wide-root instrument proved from untouched source bits

Conditional on the complete low-only transcript of a returned wide root,
its table has L=2^lambda(b) distinct binary incidence vectors. Put M0=2^b.
Write each original source label as low+2^B tau, with independent uniform
tau in Z/M0. Each output high label is

    v_j=c_j+sum_l I_(j,l) tau_l modulo M0,

where carries c_j and binary incidence vectors I_j are determined by that
low transcript. This is the same freshness induction as cyclic_base.md:
all bucket, rank, cyclic-window, retry and size decisions see only low B
bits. Private extractor transcripts are averaged out in the ideal process.

For every nonempty I_j, v_j is uniform modulo M0. For two distinct
nonempty binary vectors, their reductions over F2 are independent; some
2-by-2 minor is odd, so the paired linear map is surjective modulo M0.
Thus the corresponding v_j,v_k are pairwise independent uniform. At most
one incidence vector is empty, giving one deterministic known residue.
For every residue r, its count C_r has variance <=L/M0 and mean within
one of L/M0. Chebyshev, the union bound over M0 residues, and L/M0>=8 give

    Pr[some C_r outside [L/(2M0),3L/(2M0)]]
       <=16 M0^2/L <=2^-36/(n+2)^2.                 (1)

The statement is uniform over all low transcripts, including their costs,
so it does not assume attempt cost and table quality are independent.

After constructing a root, classically count its full high labels modulo
M0. If the count condition fails, reset the root and discard the whole
attempt. Otherwise let K=min_r C_r and select the first K rows of each
residue in fixed index order. Mark selected rows by an explicit lookup,
measure the flag, and discard on flag zero. The success probability is
M0 K/L>=1/2, EXACTLY independent of all phases. On success reindex
selected row j bijectively as (r,k), 0<=r<M0,0<=k<K. Implement the map
and its inverse with the source's explicit lookups, then clear the old
index. All tables have polynomially many rows in n and O(n)-bit entries;
reversible arithmetic, comparison and lookup circuits are counted.

Suppose the incoming root phase is v_j(a/M0+epsilon), up to a global phase.
If epsilon=0, the reindexed state is exactly

    M0^(-1/2) sum_r exp(2pi i a r/M0)|r>
       tensor K^(-1/2)sum_k |k>.

Discard the second register. The first is an exact modular-translation
eigenstate with eigenphase label a. Use the full source's exact controlled
translations and collective tests (Section 5) at modulus M0 to read a.
No inverse QFT or synthesized rotation is required. Choose confidence so
its ideal error eta<=2^-60/(n+1): set its confidence integer to
ceil(log2((b+5)(n+1)))+64, run F=2^21 times that integer tests per
basis at every level j=0,...,b+4, and use the exact direction/unwrap
algorithm from that section. The union error 4(b+5)exp(-confidence)
is then at most 2^-62/(n+1), below eta. The repetition count is polynomial
in log n. Modular
translations here act on the prepared root register, requiring no new
original coset copies.

For nonzero epsilon, before the measurement the normalized selected state
has the same basis magnitudes and each phase differs by at most
2pi |epsilon| vmax, vmax=max_j |v_j|. Its Euclidean distance from the
ideal state is therefore at most e=2pi |epsilon| vmax. Contraction of
unitaries and projections and the triangle inequality give

    Pr[wrong a | selected] <=2eta+2e^2.              (2)

This also holds after discarding k. Selection normalization introduces no
extra factor: the selected probability is exactly M0 K/L for both states.
The full source-label magnitude bound gives vmax<2^b q2^m<=2^b Rbar.

One whole attempt constructs a fresh root, tests counts, and measures the
flag. From (1), its selection probability exceeds 1/3 uniformly over prior
history. Use at most Ktry=64(t+40) whole attempts per block, then abort and
output zero. Expected attempts are at most three, even when attempt cost
correlates with selection; fresh-whole-attempt renewal/reach accounting
applies. The cap failure per block is <=(2/3)^Ktry<=2^-32(t+40).
The construction/selection laws use only equal magnitudes and stored labels,
so these cost and cap statements remain valid after earlier wrong decisions.
Correct phase interpretation is needed only on the first-error-success path.

## 4. Denser-source seed with the same localization guarantee

Factor N=2^a2 M with M odd, and let s1=s mod M. If M=1 skip the odd
seed and decoder. Otherwise H=ceil(log2 M). Use the original odd-part
root supplier at actual width D=d=floor(log2 N), but with SEED schedule,
not BASE, at physical scales H+u. It applies the same exact source
multiplier and accepts latent labels k<2^d, with probability >1/2.
Its one-qubit root satisfies the proved characteristic bound
|E exp(2pi i zW)|<=|cos(pi z)| and |W|<2As<=2Rbar.

Use the original streaming seed decoder with these explicit parameters:

    local stages u=0,...,ellbar+27,
    P_u=u+ellbar+28,
    Kseed=32768(ellbar+nu+80), Fseed=(ellbar+28)Kseed.

Stage zero enumerates the full dyadic grid; each later stage enumerates
its points in the same closed circular arc of radius 2^(-u-2) about the
previous center. Measure roots in independent fair X/Y bases and use the
supplied fixed rational trigonometric table. A nearest grid point now has
phase error at most 2^-28, better than the source's 2^-8. The far-point
cos(pi/8) bound and strictly positive score margin in Section 9.2.1 still
hold. There are at most 2^(ellbar+28) candidates per stage. The same
Azuma exponent, with the new Kseed, makes the first-error union over all
ellbar+28 stages at most 2^-50. The last center z_H satisfies

    ||2^H(s1/M)-z_H||<=e0=2^(-ellbar-30)<=1/(2^30 Rbar). (3)

All arithmetic, grids and streamed scores are explicit rational bit
algorithms. No exponential score table is stored. This proof uses the
actual larger Rbar even though the denser seed has fewer source leaves.

## 5. Odd part: small-modulus scoring or large-modulus block alignment

Choose LARGE iff

    M>=2^30 *2^h *Rbar*ceil(sqrt n).

Otherwise use the original SMALL two-candidate backward decoder, with BASE
one-bit roots and Kback=512(nu+60) roots per step. Its incoming error (3)
is below 1/(64Ao). Section 9.1 applies, first-error probability over H
steps is <=2^-60, and its deterministic root count is H Kback.
The failed LARGE test gives H<=ellbar+h+ceil(log2 ceil(sqrt n))+31,
so H=O(sqrt n) and H Kback=O(sqrt n log n).

In LARGE start at jold=H and stored z approximating 2^jold theta,
theta=s1/M. While jold>0, put b=min(h,jold), j=jold-b and
u_a=(z+a)/2^b for a=0,...,2^b-1. Compute exactly

    t0=floor(M u_0+1/2), bshift=(2^j)^(-1)t0 mod M.

Round ties upward. Since u_0<1/2, t0 is in [0,M). Use fresh copies with
Shift_bshift FIRST and Mult_alpha SECOND, where the CRT unit satisfies

    alpha=1 mod2^a2,
    alpha=2^j*(2^(B-a2))^(-1) mod M, B=d-b.

The LARGE guard implies floor(log2 M)>h, hence B>=a2. This is an exact
integer source transform on the original modulus, not a fictitious dyadic
source. Accept k<2^d, apply X, and run a WIDE tree at actual width d,
retaining b bits. Its root phase is

    v 2^B alpha(s-bshift)/N
      =v(2^j theta-t0/M)=v(a/2^b+epsilon) mod 1,

where the correct inverse lift u_a has

    |epsilon|<=e_in/2^b+1/(2M).

Apply Section 3's capped balanced instrument, obtaining a, and set z=u_a,
jold=j. The stored error shrinks exactly by 2^b after a correct decision;
rounding t0 is a test shift and is never added to the stored center.

For a first-error-success history, (2) and vmax<2^b Rbar give per-block
error at most

    2eta+16pi^2 Rbar^2 e_in^2
                   +4pi^2 Rbar^2 2^(2h)/M^2.

The incoming errors shrink by at least two each block. Summing at most n
blocks, (3) and the LARGE guard bound the total by

    2n eta+(64/3)pi^2 Rbar^2 e0^2
                +4pi^2 n Rbar^2 2^(2h)/M^2 <2^-45.

Capped-instrument aborts add at most n2^-32(t+40), much smaller. All
claims are pointwise in the selected high labels, after which only the
count/selection probability is used. There is no postselection premise.
The final stored error is e0/2^H<1/(2M); circular rounding of Mz gives
s1 exactly, including boundary phases, as in the supplied source.

## 6. Power-of-two part in blocks, with a polynomial-cost small-width tail

If a2=0 skip. Otherwise retain s2low and g as in cyclic_base.md Section 10:
sh_g=s1+M s2low mod N, wd=a2-g, rem=(s2-s2low)/2^g.
For each fresh original copy, apply Shift_sh_g, run LE to obtain k,
apply X to the CONTROL qubit once (the positive-qubit conversion of
cyclic_base.md Section 10), and then use kk=k mod2^wd. On correct earlier
decisions its phase is POSITIVE k rem/2^wd and kk is uniform. If wd>Dcut, retain b=h bits with a WIDE tree
at actual label width D=wd. Its root phase is exactly v rem/2^h.
Section 3 reads rem mod2^h with error at most eta (there is no alignment
perturbation). Update g by h and append those low bits. The number of
wide blocks is at most ceil(a2/h).

When wd<=Dcut, finish with the supplied one-bit Section 10 procedure using
BASE schedules, including its single-label width-one branch. There are at
most min(a2,Dcut) such bits, each with at most K2=ceil(log2 n)+30 attempts
and expected attempts at most two. Their total parity-cap error is <=2^-30.
Their phase identity is exact on correct histories. On wrong histories
stored labels remain uniform and phase-vector magnitudes stay equal, so
all retry, balance, selection and expected-copy bounds still hold uniformly.
Every branch returns a defined integer. Return s1+M s2 modulo N.

## 7. Two typed acquisition caps and unconditional success

Let Fseed=0 and all odd budgets be zero if M=1. Otherwise define the
computable integer expectation budgets

    U_seed=8 As Fseed,
    U_odd=8 Ao H Kback in SMALL,
          24 Aw ceil(H/h) in LARGE,
    U_other=U_odd+24 Aw ceil(a2/h)+16 Ac min(a2,Dcut)+2.

Factors eight include the source acceptance loss at most two and the tree
retry product below four. A balanced selected wide block has expected
whole-root attempts at most three. Small 2-adic bits have expected attempts
at most two; width one is covered by Ac>=1. Ceilings only overcount blocks.
These expectation bounds hold uniformly after earlier wrong decisions,
by uniform latent labels and phase-independent construction/selection.
They do not condition on the seed, extraction or decoding being correct.

Enforce SEPARATELY, counting every actual source acquisition,

    Q_seedcap=4096 U_seed, Q_othercap=4096 U_other,
    Q_global=Q_seedcap+Q_othercap.

If either typed cap would be exceeded, abort and output zero. Each copy
is assigned to its fixed public seed/other call type before acquisition.
Markov against the uncapped ideal process gives total typed-cap error at
most 2*2^-12=2^-11. Type-specific caps are essential: denser seed copies
have a larger work charge and may not use the other type's budget.
Collective source extraction confidence and its coupling use Q_global;
set its confidence integer to ceil(log2(Q_global(n+5)))+20 and
its per-basis test count to 2^21 times that integer. The full-source
union bound is then 4(n+5)Q_global exp(-confidence)<=2^-18.

The seed, SMALL/LARGE decisions, balanced-instrument aborts, power-of-two
parity caps, source-extraction coupling and typed-cap errors sum to less
than 2^-8. They are unconditional first-error/cutoff comparisons. All labels,
lookup widths and circuit streams remain fixed and capped after mistakes.
No success conditioning supplies a resource bound. The finite smaller n
branch has its own original unconditional guarantee and literal caps.

## 8. Analytic source savings and uniform maxima

Use c=8/9, R=sqrt(2V), L=log2 R, g=cR/L,
S=sqrt(1+2(c/L)^2), f=R(S-c/L). The complete logscale_base.md proves
monotonicity, rounded precision x0=g+O(1), m+x0<=RS+O(1),
m<=f+O(1), and uniform maxima for BASE schedules, including its finite
kappa guard. For R*=sqrt(2n), g*=g(R*), f*=f(R*),

    Ao=O(g*2^f*), Aw=O(g*2^f*).                     (4)

For Aw, V<=n+O(log n). Changing the largest V by O(log n) changes R by
O(log n/sqrt n); derivatives of g,f are bounded on the large-width range.
Thus the exponent and prefactor change by O(1). Smaller widths use the
same monotone analytic bounds. No rounded profile is assumed monotone.

For SEED, delta_n=2t. If R>=n^(1/4), then L>=log2(n)/4, and
x_seed=g+delta_n+O(1); the min with mu-1 is inactive for all sufficiently
large n in this range. The capacity square-root estimate gives uniformly

    m_seed+x_seed<=RS+O(1),
    m_seed<=f-delta_n+O(1).                         (5)

To verify the bounded error, replace g by g+delta_n+O(1) inside
sqrt(R^2+2x^2+x+1/4). The extra difference is
O(g delta_n/R+delta_n^2/R+1)=O(delta_n/L+delta_n^2/R+1)=O(1).
The lower constraint 2x_seed+1 fits RS+O(1), since x_seed/R tends uniformly
to zero in this range. Subtract x_seed to obtain the second bound. For
R<n^(1/4), m<=mu and q=O(mu) imply q2^m=2^O(n^(1/4)), below the global
right side of (5) even after any fixed polynomial divisor. This proves
uniformly over ALL actual seed widths

    As=O(n^-2 g*2^f*).                              (6)

The finite range of n before these uniform estimates holds is absorbed
by an absolute constant. Since ellbar=O(sqrt n), Fseed=O(n). Also

    Ac<=2^O(sqrt Dcut)=n^O(1).

In SMALL, H Kback=O(sqrt n log n)=O(n/log n); in LARGE the number of
blocks is O(n/log n). Equations (4)--(6) and the explicit typed budgets yield

    Q_seedcap=O(n^-1 g*2^f*),
    Q_othercap=O((n/log n)g*2^f*),
    Q_global=O(n^(3/2)(log2 n)^(-2)2^f*).            (7)

All polynomial small-width source cost is absorbed by this positive
exponential. The original logscale coefficient proof gives f*<=F(n)
for n>=2^1024, replacing only its leading sqrt2 by a. This establishes
the claimed full source envelope, including all discarded and capped work.

## 9. Deterministic work and both peak spaces

The source's deterministic charge per acquired copy is
O(n(m+1)2^kappa 2^x/q), including each failed or abandoned subtree. The
wide output has at most as many rows as an input, so the same merge charge
holds. For BASE and WIDE calls the common charge is
O(n^(3/2)2^g*/g*). For SEED calls it is
O(n^(3/2)2^(g*+delta_n)/g*). The small-R seed widths are below this bound;
2^delta_n=Theta(n^2). Multiply EACH by its own literal typed cap (7):
seed tree core work is O(n^(5/2)2^(R*S*)), and other tree work is smaller
by a logarithmic factor. There is no substitution of a global copy budget
into the larger seed charge.

Source transforms and collective extraction cost O(n^2) per acquired copy;
the retained negative g* in f* makes them smaller. Seed score enumeration,
with finer grid by a fixed factor 2^20 and more stages by a fixed additive
constant, costs O(n^2 Rbar) plus polynomial work, and is likewise smaller.
Every balanced-root table operation, reindexing, exact translation test and
small-width tail has polynomial cost in n. There are only polynomially many
such operations under the explicit attempt and bit caps, so their total is
absorbed. All circuit generation, initialization, classical processing,
explicit lookup, measurement, reset/disposal and wrong-label work counts.
Address length is O(sqrt n). Therefore total charged work is

    O(n^3 2^(R*sqrt(1+2c^2/(L*)^2))).                (8)

The polynomial curvature inequality and exact rational conversion in
logscale_base.md give exactly J(n) from (8), including all three signed
correction terms and the same outer polynomial prefactor.

The quantum stack and active scratch use O(n) qubits. Wide roots add only
O(log n) index/test qubits and polynomially described lookup scratch with
O(n) active qubits; no polynomial number of coherent table rows is allocated.
Lookup tables are classical and streamed. Seed indices remain O(sqrt n).

Classical high-part fields have widths O(sqrt n(m-i+1)); the retained b
high bits and O(log n) root adjustment fit this bound. All plateau tables
sum to O(sqrt n s^2 2^(m+kappa+1)), with smaller geometric growing tails.
For BASE/WIDE this is O(n^(3/2)(log2 n)^(-2)2^f*). For SEED, (5) lowers
m by delta_n while s=O(g*), so it is no larger. Polynomial balanced-root
tables, extractor records, scores and small-width storage are included and
absorbed. Every allocated field is fixed-width even on incorrect labels.
These are every-branch peak allocations with all allocation/reset work
already charged, not expectations or numeric-value compression assumptions.

The complete five joint guarantees follow. Relative to LOGSCALE, the sample
envelope improves by the strict factor 1/log2(n); all other stated envelopes
are identical. The proof does not use a tiny rational leading-coefficient
gap to manufacture that gain: the actual decoder acquires fewer expensive
roots, and its separate seed schedule and typed caps account for all work.

## 10. Provenance and scope of finite checks

All full circuit, source, collision and original decoder arguments are supplied.
The full logarithmic schedule and its curvature ledger are supplied separately.
The balanced wide-root count instrument, block recovery, denser seed and typed
caps are new in this manuscript. Material published predecessors, including
this session's own, are declared with exact archive-member paths, hashes and
both-endpoint citations. Finite arithmetic/instrument checks debug the
construction; neither they nor earlier acceptance establish the theorem.
