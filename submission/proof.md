# CYCLIC-BLOCKBOOST: fixed logarithmic retuning of all block-root schedules

## 1. Full algorithm and joint theorem

Explicit supplier convention for this revision: every power-of-two leaf
uses Shift_sh_g, LE, then ONE X on the original control, and then the
label kk=k mod2^wd, exactly as the positive-qubit supplier in cyclic_base.md
Section 10. This is the same single conversion in all referenced suppliers,
not an additional second X. It gives the positive phase required by the
wide Fourier-label readout. The conversion costs one exact Clifford gate
per original copy and is included in the stated work and peak allocations.

Use the complete square-root-block algorithm in blockroot_base.md, with the
OTHER/SEED schedules, their exact maxima and the following resource analysis
replacing its corresponding choices. That full argument and all its complete
sources are supplied: blocklog_base.md gives the balanced wide-root instrument
and typed caps; logscale_base.md gives the scaled-logarithmic curvature ledger;
log_base.md gives the counted rational series and balanced-family proof;
cyclic_base.md gives exact circuits, source identities, conditional freshness,
cyclic-window instruments and all-modulus decoding. No acceptance verdict is
a premise, and none of those older resource theorems is silently substituted
for this new configuration.

For every N>=2 and every s in Z/NZ, n=ceil(log2 N), this ONE fixed uniform
algorithm recovers the entire s with unconditional probability at least
1-2^-8 from independent ideal copies. On every execution branch jointly,

    T=O(n^3 2^J(n)),
    S_C=O(n^(-13/2)(log2 n)^(-2)2^F(n)), S_Q=O(n),
    Q=O(n^(-7)(log2 n)^(-1)2^F(n)),
    J(n)=a sqrt(n)+(9/2)sqrt(n)/(log2 n)^2
                  -7sqrt(n)/(log2 n)^4+23sqrt(n)/(log2 n)^6,
    F(n)=a sqrt(n)-(5/2)sqrt(n)/(log2 n)+6sqrt(n)/(log2 n)^2.

Here a=u_333/v_333 is the exact Pell rational in cyclic_base.md Section 0,
with the supplied proof a>sqrt2. All constants are absolute and independent
of N,s and outcomes. Evaluate these eventual positive representative envelopes
for n>=2^4096 and extend positively on the finite smaller prefix; algorithmic
correctness still covers every N. Their exact indices are 1/2,1/2,0,1/2.
Negative polynomial prefactors do not make the full positive exponential
resources tend to zero. Fractional malformed-copy tolerance is zero under
independent ideal copies, with no maximum possible tolerance assertion.

For n<2^4096 use the complete original LOGSCALE finite-prefix branch supplied
in the sources with its literal caps. This finite public-input branch is
absorbed by absolute outside constants in all eventual envelopes. No input
is excluded from recovery. Below assume n>=2^4096.

## 2. Concrete integer schedule changes

Retain the square-root block parameters exactly:

    t=ceil(log2(n+2)), h=max(1,floor(isqrt(n)/8192)),
    Dcut=2^20(h+t+1)^2, lambda(b)=2b+2t+40.

For each auxiliary width V use mu=ceil(sqrt(2V))+1, the exact counted rational
ell(mu) with log2(mu)<=ell(mu)<=log2(mu)+1/mu, and

    x0=max(2,floor(8mu/(9ell(mu)))),
    kappa=ceil(log2 mu)+1 if mu<32, and 2 otherwise.

Replace the old BASE by the OTHER schedule

    x=s=min(mu-1,x0+8t), q=kappa+1+x,

and replace the old SEED by the new SEED schedule

    x=s=min(mu-1,x0+10t), q=kappa+1+x.

Both use the least m>=s+1 satisfying the exact generic capacity
C(m)=m(m+1)/2-s(s-1)/2+x(m+1)+kappa>=V. All arithmetic is exact integer
or counted rational arithmetic. The coefficients eight and ten are fixed
parts of this ONE algorithm, not selected separately for different resources.
They change the actual leaf boost, plateau and depth by unbounded amounts.

Capacity holds at mu, so m<=mu. The boosts are at least x0 and at most mu-1.
Thus the complete finite kappa guard and m2^-q<=1/2 retry proof remains
valid. The product is below four. The generic capacity sums and slack
identities remain exact. For wide calls use V=D-b+lambda(b)-1 and reduce
the root capacity by lambda(b)-1, allocating exactly D-b actual bits.
For one-bit calls use V=D-1. All selected windows remain in the exposed
low prefix; exact cyclic rank maps and independent untouched high source
blocks therefore retain all collision, balancing and top-bit proofs.

At wide widths D>Dcut, the new x is still <=R/4, R=sqrt(2V), on this
public n range: the unshifted x0 is <=R/8 for these enormous R, while
10t<=R/8. These follow from R>1448(h+t+1), h=Theta(sqrt n), and
log2 R>=log2(n)/2-O(1)>=2000. The same capacity upper bound forces
m>=R/4, so lambda(b)<=m+kappa+1. Root capacity is nonnegative and
all wide outputs fit their inputs as required by the full argument.

Recompute every exact maximum Ao,As,Aw,Ac using these new schedules.
Ao is OTHER one-bit through n, As new SEED one-bit through n, Aw OTHER
wide, and Ac OTHER one-bit through Dcut; include the width-one sentinel.
Set Rbar=max(Ao,As,Aw,1), ellbar=ceil(log2 Rbar), and
nu=ceil(log2(n+ellbar+28)). Every decoder grid, source multiplier, mode,
precision, confidence and literal cap uses these actual recomputed values.

## 3. Complete recovery and separate typed caps

Retain every step of blockroot_base.md's algorithm with OTHER substituted
for each old BASE call and the new SEED for each old SEED call. In particular:

- The seed uses Fseed=(ellbar+28)32768(ellbar+nu+80) new-SEED roots,
  the supplied streaming grids and exact source transformations. It yields
  error e0=2^(-ellbar-30) except with probability at most 2^-50.
- SMALL odd moduli use new-SEED one-bit scored roots, Kback=512(nu+60)
  per inverse step. LARGE uses the exact square-root blocks, source shifts,
  CRT multipliers and OTHER wide roots under the unchanged guard
  M>=2^30*2^h*Rbar*ceil(sqrt n).
- The power-of-two part uses OTHER wide roots above Dcut and OTHER one-bit
  roots in the tail, with the same exact phase identities and parity caps.
- Wide-table balance/selection, uniform reindexing and exact collective
  modular-translation tests are unchanged, with Ktry=64(t+40) attempts and
  the supplied confidence ceil(log2((b+5)(n+1)))+64. All failed whole roots
  are discarded and all their original copies count.

The new one-bit schedules have exactly the same proved characteristic
bound and fair top-bit law, and their root multipliers satisfy |W|<2Rbar.
The wide schedules leave b untouched independent high source bits, so
pairwise high-label uniformity, the Chebyshev count bound, selection success
and the exact Fourier-label/perturbation proof are unchanged. Source shifts
and CRT identities refer to actual low-bit collimation widths, not V.
No fictitious source modulus or uncounted oracle is introduced.

With odd terms zero when M=1, compute literally

    U_seed=8 As [Fseed+1_SMALL H Kback],
    U_other=1_LARGE 24 Aw ceil(H/h)
             +24 Aw ceil(a2/h)+16 Ac min(a2,Dcut)+2,
    Q_seedcap=4096 U_seed, Q_othercap=4096 U_other,
    Q_global=Q_seedcap+Q_othercap.

Each acquired original copy keeps its public call type. Enforce both caps
separately, including rejected labels, failed tables, selection failures,
parity failures and abandoned subtrees. The same uniform wrong-history
expectation argument applies: stored latent labels are uniform and all
construction/selection laws use equal magnitudes. Original source acceptance
cost is at most two, tree retry factor below four, selected wide-block
expected attempts at most three, and tail parity expected attempts at most
two. Thus these are expectation bounds without success conditioning.

Markov adds at most 2^-11 total typed-cap error. Each original source's
collective extraction uses confidence ceil(log2(Q_global(n+5)))+20 and
per-basis count 2^21 times that integer; its coupling error is <=2^-18.
All other seed, SMALL/LARGE, instrument and parity first-error bounds from
the full supplied proof remain the same with actual Rbar. Their sum is
less than 2^-8. All branches have defined widths, caps and integer outputs,
including after extraction or decoder mistakes. Recovery is unconditional
and covers every N and s, including the explicitly retained finite branch.

## 4. Uniform shifted profiles, not a rounded monotonicity assumption

Use the exact unshifted analytic profile from logscale_base.md:

    R=sqrt(2V), L=log2 R, c=8/9,
    g(R)=cR/L,
    f(R)=R[sqrt(1+2c^2/L^2)-c/L].

For unshifted integer x0, the full proof gives x0=g(R)+O(1), increasing
g and f with bounded derivatives, and the square-root capacity estimate.
For either fixed k in {8,10}, write delta=kt. If R>=n^(1/4), the min
with mu-1 is inactive for sufficiently large n and x=g+delta+O(1).
The change of the square-root radicand gives the UNIFORM bounds

    m+x<=R sqrt(1+2c^2/L^2)+O(1),
    m<=f(R)-kt+O(1).                                (1)

Indeed the extra square-root difference is
O(g delta/R+delta^2/R+1)=O(delta/L+delta^2/R+1)=O(1), since
L>=log2(n)/4, t<=log2(n)+2 and k is fixed. The lower constraint
2x+1 fits the same bound because x/R tends uniformly to zero on this
range. Subtract x to obtain the second inequality. All O(1) constants
are fixed absolute constants for this configuration, not functions of n.
Any finite preliminary range is absorbed by the allowed outside constant.

For R<n^(1/4), m<=mu and q=O(mu) make q2^m and all table maxima
2^O(n^(1/4)), below the global right side even after any fixed polynomial
divisor. This handles every capped-small-width regime, rather than
silently assuming the min is inactive there.

Put R*=sqrt(2n), g*=g(R*), f*=f(R*). Wide V<=n+O(sqrt n) changes R by
O(1), and bounded derivatives change g,f by O(1). Monotonic analytic
bounds, not rounded integer monotonicity, therefore establish

    Ao,Aw=O(n^-8 g*2^f*), As=O(n^-10 g*2^f*).        (2)

Here 2^-kt<=n^-k follows from t>=log2 n. The polynomial prefactor
q remains O(g*) at the maximizing widths. In particular ellbar=O(sqrt n),
Fseed=O(n), and SMALL H Kback=O(sqrt n log n)=O(n).

Dcut<=n/16 is unchanged. The crude m<=mu bound for Ac still gives
Ac<=poly(n)2^((1/2)sqrt n). This has a strict leading coefficient gap
below f*/sqrt n→sqrt2, so its entire tail budget remains below the
new target even after the fixed n^-8 saving. The same is true for all
polynomial setup and fixed-width sentinels. From the literal budgets,

    Q_seedcap=O(n^-9 g*2^f*),
    Q_othercap=O(n^(-15/2)g*2^f*)
               =O(n^-7(log2 n)^(-1)2^f*).

The seed type is smaller. The exact retained coefficient proof f*<=F(n)
therefore gives the full stated Q guarantee with all failed copies counted.

## 5. Every-branch work and improved classical storage

The generic deterministic per-copy tree charge still includes every
failed or abandoned attempt. For OTHER its common bound is
O(n^(3/2)2^(g*+8t)/g*), and for SEED it is
O(n^(3/2)2^(g*+10t)/g*). The small-R widths are below these same bounds.
Because 2^(kt)=Theta(n^k) for each fixed k, multiplying EACH by its OWN
typed cap in (2) and the literal budgets proves

    seed/SMALL core work=O(n^(5/2)2^(R*S*)),
    other tree core work=O(n^2 2^(R*S*)),
    S*=sqrt(1+2c^2/(L*)^2).

The polynomial factors n^8 and n^10 in the charges cancel their actual
source reductions; they are not dropped as free operations. A global
copy cap is never inserted into the larger SEED charge.

Source transforms and collective extraction cost O(n^2) per acquired copy.
The retained negative g* dominates all fixed polynomial factors, so these
and streamed seed scoring remain smaller than tree work. Wide-root table
processing has poly(n)2^(sqrt n/4096) charged cost; the tail has leading
coefficient at most one half. Both remain below the actual sqrt2 leading
main profile, even with the fixed polynomial savings. All generation,
initialization, explicit lookup, measurement, reset/disposal, failed and
wrong-label work is counted. Address length is O(sqrt n), so

    T=O(n^3 2^(R*S*))=O(n^3 2^J(n)),

using the supplied exact curvature/coefficient conversion. There is no
additional unbounded exponential correction or polynomial time factor.
The hidden time constant may grow under the fixed retuning; no practical
or tight-cost speed claim is made.

For classical memory the complete high-part field-width plateau/geometric
ledger gives O(sqrt n s^2 2^(m+kappa+1)). At the largest OTHER widths,
s=O(g*) and (1) lowers m by 8t, hence

    S_C=O(n^(3/2-8)(log2 n)^(-2)2^f*)
        =O(n^(-13/2)(log2 n)^(-2)2^F(n)).

SEED lowers m by 10t and is no larger. Small-R, root postprocessing,
extractor/score, setup and tail tables all have strictly smaller leading
coefficients and fit this SAME envelope after any fixed polynomial divisor.
Allocated widths remain fixed even on incorrect labels. Every allocation,
reset and release is counted. The quantum stack and active scratch remain
O(n), since all index lengths and roots are O(sqrt n) and their depth-first
sum is O(n); explicit lookup tables are classical and streamed.

These are simultaneous every-branch bounds for the single eight/ten-shift
configuration. The exact indices are unchanged, because each exponential
logarithm is a sqrt n+o(sqrt n), independent of its polynomial prefactor.
Compared with BLOCKROOT, classical memory and all source copies improve
by n^-8, while the full time, quantum-space and clean-copy guarantees are
identical. The change is an actual integer schedule retuning with its
costs and typed caps proved, not only a looser declaration exploiting a
rational leading coefficient. No global frontier or index-1/3 claim is made.

## 6. Material sources and finite checks

The complete BLOCKROOT construction and all full transitive mathematical
sources are supplied. They provide balanced wide roots, exact translations,
block alignment, denser SMALL decoding and the cost model. The fixed all-call
8t/10t retuning and its revised maxima, typed work cancellation and peak-space
ledger are developed here. Published predecessors are declared at upload
with exact submission/ archive-member paths, hashes and both-endpoint citations.
No earlier verdict or finite arithmetic check is used as a proof premise.
