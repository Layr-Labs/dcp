# CYCLIC-BLOCKSCALE: refined rational scale within the complete time budget

## 1. Full algorithm and simultaneous theorem

Explicit supplier convention for this revision: every power-of-two leaf
uses Shift_sh_g, LE, then ONE X on the original control, and then the
label kk=k mod2^wd, exactly as the positive-qubit supplier in cyclic_base.md
Section 10. This is the same single conversion in all referenced suppliers,
not an additional second X. It gives the positive phase required by the
wide Fourier-label readout. The conversion costs one exact Clifford gate
per original copy and is included in the stated work and peak allocations.

Use the complete BLOCKBOOST algorithm in blockboost_base.md, replacing its
unshifted scale and its memory/source exponential conversion explicitly below.
The complete BLOCKROOT, BLOCKLOG, LOGSCALE, rational-logarithm and original
cyclic-window arguments it uses are supplied as separate full files. All
circuits, source identities, exact lookups, low-prefix freshness, balanced
wide-root instrument, all-modulus block decoding, denser SMALL mode, typed
caps and work/space accounting are present in these files. Their older
resource theorems concern their own configurations. No prior acceptance
verdict is a mathematical premise.

For every N>=2 and every s in Z/NZ, n=ceil(log2 N), this ONE fixed uniform
configuration recovers the entire s with unconditional probability at least
1-2^-8 from independent ideal copies. Jointly on every execution branch,

    T=O(n^3 2^J(n)),
    S_C=O(n^(-13/2)(log2 n)^(-2)2^G(n)), S_Q=O(n),
    Q=O(n^(-7)(log2 n)^(-1)2^G(n)),
    J(n)=a sqrt(n)+(9/2)sqrt(n)/(log2 n)^2
                  -7sqrt(n)/(log2 n)^4+23sqrt(n)/(log2 n)^6,
    G(n)=a sqrt(n)-(63/25)sqrt(n)/(log2 n)
                  +(9/2)sqrt(n)/(log2 n)^2.

Here a=u_333/v_333 is the exact Pell rational with its proof a>sqrt2 in
cyclic_base.md Section 0. Constants are absolute and independent of N,s and
outcomes. These eventual positive representative envelopes are evaluated
for n>=2^4096 and extended positively on the finite smaller prefix;
algorithmic correctness covers every N. Exact indices are 1/2,1/2,0,1/2.
Negative polynomial prefactors multiply positive leading exponentials.
Malformed fraction is zero under independent ideal copies, not a maximum
possible tolerance assertion. All failed, rejected, discarded and cutoff-
abandoned original copies count.

On n<2^4096 use the complete original LOGSCALE finite-prefix branch with
its literal caps. This finite public-input branch is absorbed by absolute
outside constants even for the stronger eventual G envelope; no input is
excluded from full recovery. Below assume n>=2^4096.

## 2. Exact scale replacement and unchanged integer construction

Fix c=1783/2000 in every call and every resource. Retain

    t=ceil(log2(n+2)), h=max(1,floor(isqrt(n)/8192)),
    Dcut=2^20(h+t+1)^2, lambda(b)=2b+2t+40.

For auxiliary width V compute mu=ceil(sqrt(2V))+1 and the supplied exact
rational ell(mu), with log2(mu)<=ell(mu)<=log2(mu)+1/mu. Replace x0 by

    x0=max(2,floor(1783mu/(2000ell(mu)))).

For ell=r/d, this is the exact integer division floor(1783mu d/(2000r)),
followed by max with two. Keep kappa=ceil(log2 mu)+1 for mu<32, otherwise
two. OTHER calls use x=s=min(mu-1,x0+8t), SEED calls use
x=s=min(mu-1,x0+10t), q=kappa+1+x. The least integer m>=s+1 satisfies

    C(m)=m(m+1)/2-s(s-1)/2+x(m+1)+kappa>=V.

All BASE/OTHER uses in the complete sources mean this NEW OTHER schedule;
all SEED uses mean this NEW SEED schedule. Wide calls use V=D-b+lambda(b)-1,
retain b high source bits, reduce the generic root capacity by lambda(b)-1
and allocate D-b actual low bits root-first. One-bit calls use V=D-1.
All label field widths, extractor and decoder confidences, grids, source
multipliers, modes, exact maxima Ao,As,Aw,Ac,Rbar,ellbar and both typed caps
are recomputed using these actual parameters. No old cap is reused.

The finite kappa guard and unconditional retry proof remain valid. Always
2<=x0<=mu-1, hence 2<=x=s<=mu-1 and capacity holds at mu, so m<=mu.
For mu>=32, mean-value precision gives

    c mu/log2(mu)-2<=x0<=c mu/log2(mu).

The ratio c mu/(log2 mu)^2 increases from c*32/25>1 at mu=32.
Thus q>=log2(mu)+1. The guarded smaller widths have m2^-q<=1/16,
and all larger widths have m2^-q<=1/2. Increasing x by the fixed shifts
only strengthens this retry bound. The product remains <=(4/3)e<4.
Every capacity sum and merge slack identity is algebraic in x,s,kappa,
so remains exact. All inspected windows are low-only. At the large wide
widths c<1 still gives x0<=R/8 and 10t<=R/8, so m>=R/4 and the wide
root fits its inputs by the supplied quantitative cutoff proof.

## 3. Uniform analytic profiles and both typed maxima

For analysis define R=sqrt(2V), L=log2 R,

    g_c(R)=cR/L,
    f_c(R)=R[sqrt(1+2c^2/L^2)-c/L].

The full exact-square-root proof in the supplied sources uses only 0<c<1.
In particular g_c is increasing with derivative between zero and one on
R>=32. With u=c/L, S=sqrt(1+2u^2), eta=1/(ln(2)L),

    f_c'=S-u-eta*u*(2u/S-1)>3/8,

since S-u>1/2, 2u/S<7/6 and eta<3/4. Completing the capacity square
and rounded precision gives m+x0<=RS+O(1), m<=f_c+O(1), uniformly after
absorbing the finite kappa guard. The min constraint is handled as in the
complete profile proof, not silently ignored.

For shifts kt with k=8 or 10 and R>=n^(1/4), the same complete argument
gives

    m+x<=R sqrt(1+2c^2/L^2)+O(1),
    m<=f_c(R)-kt+O(1).

The extra square-root difference is O(kt/L+k^2t^2/R+1)=O(1), uniformly
in this range for each fixed k. Smaller R give 2^O(n^(1/4)) bounds and
are below every global maximum after a fixed polynomial divisor.
Wide auxiliary V<=n+O(sqrt n) changes its largest R by O(1), so bounded
derivatives preserve the full exponential bounds up to constants. Put
R*=sqrt(2n), L*=log2 R*, g*=g_c(R*), f*=f_c(R*). Exact maxima satisfy

    Ao,Aw=O(n^-8 g*2^f*), As=O(n^-10 g*2^f*).

There is no assumption that rounded integer schedules are monotone.
Dcut<=n/16 remains true, and the crude m<=mu bound for Ac gives a smaller
leading coefficient at most one half, below f*/sqrt n→sqrt2. All tail
budgets are therefore below the same target after any fixed polynomial
divisor. The literal typed expectation/cap definitions are those supplied
in full, with NEW maxima:

    U_seed=8 As [Fseed+1_SMALL H Kback],
    U_other=1_LARGE 24 Aw ceil(H/h)
              +24 Aw ceil(a2/h)+16 Ac min(a2,Dcut)+2,
    Q_seedcap=4096 U_seed, Q_othercap=4096 U_other.

Here ellbar=O(sqrt n), Fseed=O(n), H Kback=O(n) in SMALL, and the number
of wide blocks is O(sqrt n). Consequently

    Q_global=Q_seedcap+Q_othercap
       =O(n^-7(log2 n)^(-1)2^f*),                    (1)
    S_C=O(n^(-13/2)(log2 n)^(-2)2^f*), S_Q=O(n).     (2)

The complete high-part plateau/geometric proof, all branch allocations and
all smaller-coefficient root/tail tables remain included in (2).

## 4. Unconditional recovery and every-branch work remain proved

The balanced wide-root count law, pairwise uniform untouched high blocks,
selected-state Fourier-label identity and perturbation norm bound depend
on incidence/low-prefix invariants, not the numerical scale c. They apply
unchanged. The root-source multiplier bound uses the new Rbar. Retain
all seed/SMALL/LARGE source shifts, CRT multipliers, block choices, exact
collective translation tests, parity caps, alignment guard and confidence
formulas from the full algorithm with this actual Rbar and Q_global.
The two typed caps count every original acquisition, including failures.

All uniform wrong-history expectation bounds still hold. Markov adds
<=2^-11 from the two caps, original source extraction coupling <=2^-18,
and the supplied seed, scoring, alignment, selection/readout and parity
first-error bounds keep the total below 2^-8. Nothing conditions on correct
extraction, avoiding caps or successful postselection. Every wrong branch
has defined fixed widths and returns an integer. The finite branch retains
its full original guarantee. Thus recovery covers every modulus and secret.

The OTHER and SEED deterministic per-copy charges are respectively
O(n^(3/2)2^(g*+8t)/g*) and O(n^(3/2)2^(g*+10t)/g*). Multiplication by
their OWN literal caps cancels the actual n^8/n^10 factors. Tree core work
is O(n^(5/2)2^(R*sqrt(1+2c^2/(L*)^2))). Addressing multiplies by O(sqrt n).
Source transforms, extraction, seed scores, full circuit generation,
initialization, lookups, measurements, resets/disposal and all failed or
abandoned work are counted. The retained negative g* dominates polynomial
source/score factors. Wide postprocessing has leading coefficient at most
1/4096 and tail tables at most one half, both strictly below the ACTUAL
sqrt2 main coefficient. They remain included despite the fixed polynomial
memory/source improvements. Therefore

    T=O(n^3 2^(R*sqrt(1+2c^2/(L*)^2))).              (3)

Quantum scratch remains O(n); all exponential tables are classical and
explicitly streamed. The hidden time constant can change under retuning;
no practical or tight-cost speed assertion is made.

## 5. Exact coefficient margins and the stronger G envelope

Let v=log2 n>=4096, so R*=sqrt2 sqrt n and L*=(v+1)/2. The exact
rational inequalities (140/99)^2<2<(99/70)^2 give

    4(99/70)c^2<9/2,
    32(99/70)c^6<23,
    8(140/99)c^4*4096^4>7*4097^4,
    [2(140/99)c-63/25]*4096>63/25.                  (4)

They are finite integer comparisons after clearing denominators; c is the
fixed rational 1783/2000 throughout. The slopes in the last comparisons
are positive, and v/(v+1) increases. Thus for every v>=4096,

    2sqrt2 c/(v+1)>=(63/25)/v,
    8sqrt2 c^4/(v+1)^4>=7/v^4.

Using sqrt(1+2z)<=1+z for z>=0 yields

    f*<=sqrt2 sqrt n-2sqrt2 c sqrt n/(v+1)
                       +4sqrt2 c^2 sqrt n/(v+1)^2
       <=sqrt2 sqrt n-(63/25)sqrt n/v+(9/2)sqrt n/v^2.

Replacing only the leading sqrt2 by a proves f*<=G(n), establishing
exactly (1)--(2) with the submitted exponential and prefactors.

For time use the complete polynomial curvature inequality

    sqrt(1+2z)<=1+z-z^2/2+z^3/2,
    (1+z-z^2/2+z^3/2)^2-(1+2z)=(z^4/4)(z^2-2z+5)>=0.

At z=c^2/(L*)^2, (3)'s exponent is at most

    sqrt2 sqrt n+4sqrt2 c^2 sqrt n/(v+1)^2
             -8sqrt2 c^4 sqrt n/(v+1)^4
             +32sqrt2 c^6 sqrt n/(v+1)^6.

The exact margins (4) bound it by J(n), again replacing only the leading
sqrt2 by a. Thus the FULL old time envelope is retained, including its
negative and positive curvature corrections, not merely its growth index.

All exponential logarithms are a sqrt n+o(sqrt n), so exact index is 1/2;
linear quantum space has index zero. Compared with BLOCKBOOST, the old
memory/source exponent minus the new one is

    (1/50)sqrt n/log2 n+(3/2)sqrt n/(log2 n)^2,

which tends to positive infinity. Polynomial/log prefactors, full time,
quantum-space and clean-copy guarantees are identical. The actual schedule
changes its scale by an unbounded amount in the boost; the margins above
pay for it within the time budget. This is a strict improvement of complete
proved guarantees, not a claim of tight actual costs, global frontier
leadership or time index 1/3.

## 6. Provenance and verification limits

The complete all-call shifted BLOCKBOOST construction and all full sources
are supplied, including their references to published material. The rational
scale refinement, exact coefficient margins and stronger simultaneous
memory/source conversion are developed here. Direct material predecessors
are declared with exact submission/ archive paths, full-file hashes and both
endpoints at upload. Finite schedule/coefficient checks debug the proof;
neither they nor prior acceptance are mathematical premises.
