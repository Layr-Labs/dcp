# CYCLIC-BLOCKROOT: square-root blocks and denser small-modulus decoding

## 1. Complete construction and simultaneous theorem

Explicit supplier convention for this revision: every power-of-two leaf
uses Shift_sh_g, LE, then ONE X on the original control, and then the
label kk=k mod2^wd, exactly as the positive-qubit supplier in cyclic_base.md
Section 10. This is the same single conversion in all referenced suppliers,
not an additional second X. It gives the positive phase required by the
wide Fourier-label readout. The conversion costs one exact Clifford gate
per original copy and is included in the stated work and peak allocations.

Use the full algorithm supplied in blocklog_base.md, with the public block
size, small-width threshold, SMALL schedule, typed caps and resource analysis
replaced explicitly below. That complete manuscript includes its wide-root
balanced-count instrument, exact collective translation tests, all-modulus
block recovery, seed and error proofs. All further full sources are also
supplied: logscale_base.md contains the scaled logarithmic/curvature ledger;
log_base.md contains the counted rational logarithm and balanced schedules;
cyclic_base.md contains the exact circuits, original cyclic-window algorithm,
conditional freshness, source transforms and all-modulus decoder. Their older
resource theorems concern their older configurations. No prior verdict is a
mathematical premise. Material published IDs and exact full-file citations
are declared with the upload.

For every N>=2 and s in Z/NZ, n=ceil(log2 N), ONE uniform configuration
recovers the entire s with unconditional probability at least 1-2^-8 from
independent ideal copies. Its joint bounds on every execution branch are

    T=O(n^3 2^J(n)),
    S_C=O(n^(3/2)(log2 n)^(-2)2^F(n)), S_Q=O(n),
    Q=O(n (log2 n)^(-1)2^F(n)),
    J(n)=a sqrt(n)+(9/2)sqrt(n)/(log2 n)^2
                  -7sqrt(n)/(log2 n)^4+23sqrt(n)/(log2 n)^6,
    F(n)=a sqrt(n)-(5/2)sqrt(n)/(log2 n)+6sqrt(n)/(log2 n)^2.

The exact Pell rational a=u_333/v_333, and its proof a>sqrt2, are supplied
in cyclic_base.md Section 0. Constants are absolute and independent of N,s
and outcomes. These eventual positive representative envelopes are evaluated
for n>=2^4096 and extended positively on the finite smaller prefix. The
algorithm and correctness cover every N. Exact indices are 1/2,1/2,0,1/2.
The fractional malformed-copy guarantee is 0 under independent ideal copies;
no maximum possible tolerance or positive robustness is asserted.

For n<2^4096 run the complete original LOGSCALE algorithm with its literal
caps, as fully supplied. The finite prefix is absorbed by absolute outside
constants, including the stronger eventual source bound. No finite input is
excluded from correctness. Below assume n>=2^4096.

## 2. Fixed new parameters and exact capacities

Retain the counted rational logarithm, BASE scale c=8/9, finite kappa guard,
SEED increment delta_n=2t, all exact maxima and primitive procedures from
blocklog_base.md. Replace its public parameters by

    t=ceil(log2(n+2)), h=max(1,floor(isqrt(n)/8192)),
    Dcut=2^20(h+t+1)^2,
    lambda(b)=2b+2t+40 for 1<=b<=h.

Integer square roots and bit lengths are counted exact algorithms. Thus
h=Theta(sqrt n), not Theta(log n). For actual wide label width D>Dcut,
retain b<=h high bits, use auxiliary V=D-b+lambda(b)-1, BASE schedule
at V, root length lambda(b), and the root capacity reduced by lambda(b)-1.
Root-first greedily allocate exactly D-b actual low bits. All non-root
formulas, exact sum/slack identities, discard rules and retry accounting
are unchanged. The SEED schedule still uses V=D-1 and
x=s=min(mu-1,x0+2t), as fully specified in the included argument.

The wide root fits its inputs with the new threshold. Indeed
R=sqrt(2V)>1448(h+t+1), log2 R>10, x0<=R/4, and the capacity upper
bound used in blocklog_base.md forces m>=R/4. Thus
lambda_(m-1)=m+kappa+1>362(h+t+1)>2h+2t+40>=lambda(b).
The reduced root capacity is nonnegative, its total capacity is at least
D-b, and bmax_i+lambda_(i+1)-2lambda_i=-kappa still holds exactly.
All windows remain below position D-b, leaving b independent high source
bits. Source/collision reasoning never conditions on their full tables.

For later use, let L_n=log2 n. We have t+1<=L_n+3. For L_n>=4096,
2^(L_n/2)>=8192(L_n+3): it holds at 4096 and the ratio increases since
ln(2)/2-1/(L_n+3)>0. Hence

    t+1<=sqrt n/8192,
    h+t+1<=sqrt n/4096,
    Dcut<=n/16.                                      (1)

Also h>=sqrt n/16384 on this range, from isqrt(n)>=sqrt n-1 and flooring.
These are public integer branches, not instance-dependent advice.

Recompute Ao,As,Aw,Ac,Rbar,ellbar,nu from the full included definitions
with these new h,Dcut and wide auxiliary widths. Ao is the BASE one-bit
maximum through n, As the SEED one-bit maximum, Aw the new WIDE maximum,
and Ac the BASE one-bit maximum through Dcut, including the width-one
sentinel. All maxima are literal integer computations with polynomial
setup work in n and are not replaced by asymptotic estimates in the code.

## 3. Balanced root selection, Fourier-label readout and all-modulus recovery

The complete instrument of blocklog_base.md Section 3 applies for every
b, not merely logarithmic b. Conditional on its low-only transcript, the
root has L=2^lambda(b) distinct binary incidence rows. For M0=2^b, the
nonempty high-label linear forms are pairwise independent uniform modulo
M0; at most one empty incidence contributes a deterministic residue.
Thus the exact same Chebyshev bound holds:

    Pr[unbalanced counts] <=16M0^2/L<=2^-36/(n+2)^2.

This proof uses the untouched b-bit source blocks and odd 2-by-2 minors;
it does not assume independent full row labels or independent subset sums.
Select exactly K=min_r C_r rows per residue, measure the explicit selection
flag, and reindex them as (r,k). Flag probability is at least one half on
a balanced table, independent of all phases. The selected ideal dyadic-grid
state is a Fourier eigenstate on r tensor a uniform k register, even if K
is not a power of two. Discard k and use exact controlled translations
and the collective tests at modulus 2^b to read the residue label. Set
confidence ceil(log2((b+5)(n+1)))+64 and test count 2^21 times that integer
per basis/level, exactly as supplied. Ideal readout error is <=2^-60/(n+1).
No new coset copy, inverse QFT, synthesized rotation or QRAM is required.

The complete selected-state perturbation proof still gives
Pr[wrong label]<=2eta+2(2pi |epsilon| vmax)^2, vmax<2^b Rbar.
All tables, flags, normalization and bijections are exactly the supplied
instrument, with larger row counts now explicitly charged in Section 6.
Use Ktry=64(t+40) whole attempts per block; expected attempts stay at most
three uniformly over prior history, and cap failure is <=2^-32(t+40).
The count and selection laws depend only on equal magnitudes/stored labels,
so this accounting holds even after previous decoder mistakes. The ideal
phase interpretation is needed only on the first-error-success path.

Retain the denser SEED localization from blocklog_base.md, including
Fseed=(ellbar+28)32768(ellbar+nu+80), its actual grids, source transforms
and e0=2^(-ellbar-30). If the odd modulus M is one, skip it. Otherwise
H=ceil(log2 M), and LARGE still means

    M>=2^30 *2^h *Rbar*ceil(sqrt n).

In LARGE retain the full source-aligned block decoder: inverse lifts
u_a=(z+a)/2^b with b=min(h,jold), exact t0=round(M u_0), source shift
(2^j)^(-1)t0, CRT unit at actual B=d-b, wide root and selected label.
The LARGE guard still ensures B>=a2. The shift is used only for the test;
the stored lift error shrinks by 2^b exactly. The same pointwise bounds
and geometric first-error sum give total alignment/readout error <2^-45.
There are now O(n/h)=O(sqrt n) expensive wide blocks, including the last
short block. Circular rounding returns s mod M on success.

In SMALL retain the original two-candidate backward score and
Kback=512(nu+60) roots per bit, BUT USE SEED-SCHEDULE ONE-BIT ROOTS,
not BASE roots. The characteristic bound and |W|<2As<=2Rbar are valid
for this schedule too, by the full freshness/top-bit proof. Its incoming
seed error is below 1/(64Rbar), so the original two-candidate proof with
that bound applies. Error remains <=2^-60. The failed LARGE test gives
H<=ellbar+h+O(log n)=O(sqrt n), hence H Kback=O(sqrt n log n)=O(n).
Every such scored root is charged to the SEED TYPE of source cap below.
This change is necessary to retain the stronger source guarantee.

For the power-of-two component use the exact full block procedure when
wd>Dcut: after the known source shift, labels k mod2^wd are uniform and
the wide phase is exactly v rem/2^h. Read the next h low bits. There are
at most ceil(a2/h)=O(sqrt n) wide blocks. Finish wd<=Dcut with the
original BASE one-bit parity procedure and its literal caps. There are
at most Dcut tail bits. Their cost is not called polynomial in n without
proof; Section 6 bounds their smaller exponential coefficient explicitly.
Every wrong-history law and first-error argument is the supplied one.

## 4. New typed budgets, unconditional caps and recovery probability

Recompute every confidence from the actual caps. With odd terms zero if
M=1, define literal integer expectation budgets

    U_seed=8 As [Fseed+1_SMALL H Kback],
    U_other=1_LARGE 24 Aw ceil(H/h)
              +24 Aw ceil(a2/h)+16 Ac min(a2,Dcut)+2.

Here 1_SMALL and 1_LARGE are mutually exclusive public mode indicators;
Fseed=0 if M=1. The SMALL root budget is deliberately moved into the
seed type because those roots use its denser schedule. Factors eight,
three and two have exactly the supplied fresh-root acceptance, retry,
selected-root and odd-label/parity expectation meanings. They hold
uniformly after earlier wrong decisions, without conditioning on correct
extraction or avoiding a cap.

Enforce two type-specific literal caps on EVERY acquired source copy:

    Q_seedcap=4096 U_seed, Q_othercap=4096 U_other,
    Q_global=Q_seedcap+Q_othercap.

Exceeding either cap aborts to output zero. Seed localization and SMALL
score calls have fixed seed type; wide calls and small 2-adic tail calls
have other type. Discarded roots and rejected labels keep their type and
are charged. Markov adds at most 2^-11 total cap error. Use confidence
ceil(log2(Q_global(n+5)))+20 and per-basis count 2^21 times that integer
for each original source's exact collective extraction; its full union
coupling error is <=2^-18.

The supplied seed, SMALL/LARGE, balanced-instrument, parity and cap errors
therefore still sum to less than 2^-8. All comparisons are unconditional
first-error/truncation arguments. Sizes, bounds and integer outputs remain
defined after mistakes. The finite smaller n branch retains its complete
original guarantee. Thus full-secret recovery holds for every N,s.

## 5. Uniform maxima and the stronger full source envelope

Use the exact analytic BASE functions from logscale_base.md:

    R*=sqrt(2n), L*=log2 R*, c=8/9,
    g*=cR*/L*, f*=R*[sqrt(1+2c^2/(L*)^2)-c/L*].

The full arguments prove increasing bounded-derivative profiles, uniform
rounded bounds and the finite guard. Here
V_wide<=n+h+2t+39=n+O(sqrt n), so its largest R changes by O(1), not an
unbounded subleading exponent. Bounded derivatives change g and f by O(1).
Consequently the exact Aw and Ao satisfy

    Aw,Ao=O(g*2^f*).

The denser SEED proof is unchanged: for R>=n^(1/4), the extra delta_n=2t
changes m+x by O(delta_n/log R+delta_n^2/R+1)=O(1) and reduces m by
delta_n+O(1). Smaller R give 2^O(n^(1/4)), below the global maximum even
after division by n^2. Hence uniformly

    As=O(n^-2 g*2^f*), ellbar=O(sqrt n), Fseed=O(n).

The extra SMALL count H Kback=O(sqrt n log n) is also O(n). Thus
Q_seedcap=O(n^-1 g*2^f*). For wide calls the total number of successful
blocks budgeted is O(sqrt n), so their other-type budget is
O(sqrt n g*2^f*)=O(n(log2 n)^(-1)2^f*).

It remains to bound the tail, without ignoring its exponential tables.
For every actual one-bit tail width D<=Dcut, m<=mu<=sqrt(2D)+2,
q=O(sqrt D+1). Using (1),

    Ac<=poly(n)2^(sqrt(2Dcut)+2)
       <=poly(n)2^((1/2)sqrt n).

The last inequality uses sqrt(1/8)<1/2. Multiplication by at most n tail
bits changes only a polynomial. Since f*/sqrt n tends to sqrt2>1,
this has a strictly smaller leading exponential coefficient and is
O(n(log2 n)^(-1)2^f*). This comparison uses the ACTUAL sqrt2 leading
profile, not only its rational slack. Therefore

    Q_global=O(n(log2 n)^(-1)2^f*)
             =O(n(log2 n)^(-1)2^F(n)).               (2)

The last inequality is the complete exact LOGSCALE coefficient proof.
Every actual source, including discarded/cutoff-abandoned copies, is counted.

## 6. Every-branch work, nonpolynomial root tables and both spaces

The original deterministic per-copy tree charge applies to wide roots
because their output table fits their input table. BASE/WIDE common
charge is O(n^(3/2)2^g*/g*); SEED charge is
O(n^(3/2)2^(g*+2t)/g*). Multiply each by its OWN literal typed cap:
seed/SMALL tree core work is O(n^(5/2)2^(R*S*)), and the other tree work
is O(n^2 2^(R*S*)) where S*=sqrt(1+2c^2/(L*)^2), plus the smaller tail.
A global cap is never substituted into the larger seed per-copy charge.
The tail is already covered by the other-type cap and common tree charge.

The source transforms/extraction and streamed seed scoring retain the full
source's smaller bounds: the negative g* in f* dominates polynomial factors.
Uniform maxima/setup are polynomial computations. Block processing is now
NOT polynomial: this is explicitly charged as follows. For b<=h,

    lambda(b)<=sqrt n/4096+2t+40,
    L=2^lambda(b)<=poly(n)2^(sqrt n/4096).

Count arrays, selection marks, lookup/bijection/inverse tables and fixed-width
row processing cost poly(n)L per whole attempt. Modular collective tests on
the root need O(sqrt n) active qubits and polynomial work beyond these tables.
There are only polynomially many whole attempts under Ktry and the public
bit/block caps. Their TOTAL charged work, including addressing, is therefore
poly(n)2^(sqrt n/4096), whose leading coefficient is strictly below sqrt2
in the tree work. It is absorbed by the stated time bound, not treated as
free or silently called polynomial. Similarly all tail processing is covered
by its tree charge or has leading coefficient at most 1/2, also smaller.

Initialization, circuit generation, explicit lookups, measurements, resets,
disposal, incorrect labels, failed attempts and abandoned subtrees all count.
The address length of the complete allocation is O(sqrt n). Multiplying
core tree work by that factor and adding explicit source acquisition gives

    T=O(n^3 2^(R*sqrt(1+2c^2/(L*)^2)))=O(n^3 2^J(n)),

using exactly the supplied polynomial curvature/rational-coefficient proof.

The quantum stack and active scratch remain O(n). A wide root and its test
ancillas add O(sqrt n) qubits, with lookup tables classical and streamed,
not one coherent qubit register per table row. The denser SEED stack still
has sum of index lengths O(n), and original source modular circuits use O(n).

For classical storage the full high-part plateau/geometric argument gives
O(n^(3/2)(log2 n)^(-2)2^f*) for BASE/WIDE. SEED m is lower by 2t+O(1)
while s=O(g*) at the largest widths, so it is no larger. All active root
postprocessing tables have poly(n)2^(sqrt n/4096) bits; all small-tail tables
have poly(n)2^((1/2)sqrt n) bits. Both leading coefficients are strictly below
f*/sqrt n→sqrt2. Thus they are absorbed by the SAME classical envelope.
All residues, extractor records, scores, setup, widths and allocation/reset
costs are included, including on wrong-label and capped branches.

The complete five joint bounds follow, with exact indices as stated. Compared
with the logarithmic-block construction's Q=n^(3/2)(log2 n)^(-2)2^F(n),
(2) improves the declared source envelope by the strict factor
(log2 n)/sqrt n→0, retaining all other complete guarantees. Compared with
LOGSCALE, the gain is n^(-1/2). These comparisons describe full proved upper
bounds for actually changed block sizes and SMALL schedules; they do not
assert tight costs, practical speed or a new time growth index.

## 7. Provenance and verification limits

The complete logarithmic-block argument is supplied as blocklog_base.md,
and every full source it uses is supplied separately. The scaled logarithmic
family, primitive cyclic circuits, counted rational parameters and original
decoders are material sources. The new square-root block scale, threshold,
denser SMALL mode, typed budget transfer and explicit smaller exponential
ledger are developed here. Public IDs and exact submission/ archive citations
are declared honestly at upload. Prior reviews and finite checks are not
proof premises; no end-to-end quantum execution is represented by them.
