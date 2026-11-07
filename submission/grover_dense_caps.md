# Required appendix: PSG2-DENSE-E exact caps and source bound

This appendix, grover_dense.md, grover_dense_oracle.md,
grover_dense_compiler.md, grover_dense_dense.md and grover_dense_bound.md
define one complete algorithm. Mathematical section references below are
to the main unless an appendix is named. All six proof files are required.

The only acquisition guard is Qcap_dense. Qcap_old is the exact auxiliary
precision/pool bound. The old q0,C, physical scales, F, H0 and Wcap are
retained, with their dense premises fully proved in dense Sections 6--11.
No bound Qcap_dense<=the old Qcap_new is asserted or used.

## R1. Exact selected parameters and guards

For n>=256 use the main's actual truncated profile, with u=floor(sqrt R)
and m=mstar retained nominal values. Define

    q0=(2u+1)2^(R-u),
    C=C_old=6(2u+1)2^(R-u-(m-1)), H0=F+2n,
    Qstar_old=C H0+2n, Qcap_old=1024 Qstar_old,
    beta_m=min(1,32*25^m/72^m),
    Qstar_dense=beta_m C H0+2n,
    Qcap_dense=ceil(1024 Qstar_dense),
    Wstar=6*2^R H0, Wcap=1024 Wstar.

Every acquisition, including a rejected copy or a failed/partial child,
is checked before execution against Qcap_dense. Each positive-width
combiner builds its b+5 children, then checks/adds its nominal weight2^v
before building the oracle array/program or executing the attempt. At
zero width return one child with no combiner and no extra four copies.
A failed guard resets/releases work and outputs0 for the whole run.
Children already built remain counted. Scalar K2=ceil(log2 n)+30 caps
remain before each 2-adic bit's finite repeat schedule.

All guards are fixed public integers. C is integral because every retained
gap is at least5 and R-u>=5(m-1). Compute 25^m,72^m and compare
32*25^m with72^m. Use the smaller numerator divided by72^m for beta_m,
then compute the outer ceiling exactly. The fields have O(R+m+log n)
bits. Powers, products, comparisons, divisions, every bit/index operation
and all initialization are paid polynomial work with O(n^2) classical
space. The cap is not replaced by an asymptotic envelope.

## R2. New instrument, frequency and expectation premises

The complete eleven-rank-bit instrument and all-domain permutation are
in dense Section3. The exact grouped G1 circuit and initial copy/G1/uncopy
wrapper are in main4.1, the oracle and dense3. On every verified list they
produce the exact cyclic signed label, including wrap edges, incomplete
lists and reference systems. Every success kernel depends only on low
residues and index/rank data. Distinct endpoints give a nonzero signed
incidence over disjoint child leaf sets; no numerical zero label is rejected.

Dense4--5 give the full planted first/second-moment and Grover miss proofs:
complete cyclic success>=63/65, measured-fiber tail<1/4094, discovery miss
<2^-37 and hence fresh success>24/25 at every positive width. The list cap
is2048; there are128 trials per block and at most2048 blocks. At k<13
full enumeration has at most4096 indices. These are fresh-before-children
bounds, not arbitrary fixed-child-list bounds or empirical distributions.

Dense6 proves product_i(2v_i+5)/(2v_i+1)<32 uniformly. Dense7 separately
proves the exact old q0 bound for the dense returned tree on n>=256,
including partial widths and shortcut-only calls. No factor32 enlarges
q0. Thus |W|<2q0 and all one-pass full signed sums fit the unchanged
n+ceil(log2 q0)+4 field. The original finite n<256 branch is unchanged.

Dense8--9 give the joint termination/unused-block induction for b+5
children. The conditional geometric source recurrence is

    E_i<=(25/24)(b_i+5)E_(i-1)

at active levels and has multiplier1 at shortcuts. The current attempt's
cost need not be independent of its success. Insert the same full nominal
m for every tree width D. With rbar_i=2v_i+1 and old nominal telescoping,

    E_root<=32(25/72)^m[2 product_nominal(3rbar_i)]
          <=32(25/72)^m C.

There is also E_root<=C, since (25/24)(2v+5)<=3(2v+1) for v>=1.
Consequently E_root<=beta_m C, including all leading zero or partial
levels and a B=0 root. Every leaf has expected cost at most two originals.
The full ratio, old-q0 and conditional proofs are included in the dense
appendix, rather than inferred from finite profiles.

## R3. All-N roots and source expectation

For n<256 use exactly the existing finite algorithm. It uses no profile
or dense cap. For n>=256 and M=1, set F=0 and skip the odd decoder/pool.
For M>1, keep q0,C,A_pool,g_pool,h_pool,Delta, all physical transforms
and the root counts from main6.3. The h_pool<16 branch keeps F=F_old
and its one-bit seed/backward schedule; the strided branch keeps its exact F.
The dense root law is uniform before every fresh root call in both cases.

At wd>=2 use the same nominal profile with D=wd. Conditional numeric
root parity is exactly fair by the nonzero signed top-bit law. Summing
conditional pre-call root costs gives at most two calls per bit in
expectation, without root-cost/parity independence. K2 truncation only
reduces that expectation and adds at most n2^-K2<=2^-30 failure. Width
one retains direct fair-label acquisition and the explicit2n allowance.
Thus the ideal reference process without the two global guards obeys

    E Q_ideal<=beta_m C(F+2n)+2n=Qstar_dense.

Wrong earlier scalar outputs do not invalidate this resource law. Input
magnitudes stay equal, the cyclic Gram effects are diagonal, and known
physical shifts preserve independent uniform numeric labels. Correct
phase identities are used for correctness only after a correct prefix.
EXTRACT errors enter by coupling, not by conditioning labels to be correct.

## R4. Fixed weight cap, pool, precision and success

Use sigma=24/25 with the actual dense child count. An active-level expected
weight contribution is

    (25/24)2^v_i product_(active j>i)a_j,
    a_j=(25/24)(b_j+5)<=3(2v_j+1).

Inserting nominal ancestors bounds this by
(25/24)2^R2^(-(m-i)). Summing gives less than(25/12)2^R<6*2^R per root.
The same conditional parity argument over all roots proves E W_ideal<=Wstar.
This includes failed ancestors and children before a failed parent check.
It does not use the invalid factor3 times the larger actual arities.

Markov at the exact Qcap_dense and Wcap costs at most2^-10 each. Since
beta_m<=1 and Qcap_old is integral,

    Qcap_dense<=Qcap_old.

Keep the exact conceptual A_pool=2^40(C+1)U^3 and all old pool/scales.
The old integer certificate Qcap_old<=2^27(C+1)U^2<=A_pool includes the
dense run. q0 and C are valid by R2, so no decoder grid or precision is
changed. Use one global low signed-sum distance event for the complete
fixed odd schedule. A dense root's nonzero signed support has at least
h_pool coordinates on that event and odd fit: a smaller support would
be a forbidden vanishing low relation. The independent top bits in fresh
disjoint root supports give the same characteristic power and decoder
law. The full conditioning proof is in dense9. Its event excludes private
EXTRACT records, accepted top bits and later adaptive 2-adic cap survival.

Keep h_ext=ceil(log2(2^16 Qcap_old(n+5))) exactly. Uniform per-call error
and at most Qcap_dense<=Qcap_old calls give first-label error<=2^-14.
Couple to exact latent labels until the first error or guard; no
successful-extraction conditioning is imposed on the root laws.

The complete strided failure union is

    2^-190+2^-20+2*2^-10+2^-14+2^-30<2^-8.

The h_pool<16 fallback union is
2*2^-10+2^-14+2^-20+2*2^-30<2^-8. M=1 has no odd loss. The original
finite branch fails below2^-10. These prove entire-secret success
at least1-2^-8 for every N,s under the exact independent ideal-copy model.
All guards, trial limits and resets bound every actual outcome branch.

## R5. Actual pre-envelope source bound and selected rational envelopes

Dense12 proves 72^2=5184>5000=8*25^2 and log2(72/25)>3/2. With the
unchanged m>(1/16)sqrt(n/L),

    2^(-(m-1))(25/72)^m
      <=2*2^(-(5/32)sqrt(n/L)).

Use beta_m<=32(25/72)^m only as an upper bound for the exact minimum.
The actual guard therefore gives, before any leading-profile substitution,

    Q<=Qcap_dense
      =O(n(2u+1)2^(R-u-(m-1))*32(25/72)^m+n+1)
      =O(n^(5/4)L^(1/4)
          2^(R-(5/32)sqrt(n/L)-(1/2)(nL)^(1/4))+n).   (R8a)

This follows from the same u,2u+1 and H0 estimates; it keeps the exact
actual R in the exponent. The factor32 is an absolute outside constant.
Dense10--11 and main9.5 prove the complete pre-envelope work

    T=O(n^2 L log2(L+2)2^R).

Every source, recursion, decoder, setup, failure, instruction-bit and
cleanup term is included. The rational bound appendix applies to these
two inputs with kappa=5/32. It proves the selected final envelopes

    T=O(2^((177/250)sqrt(nL))),
    Q=O(2^((177/250)sqrt(nL)-(5/32)sqrt(n/L)
           -(1/2)(nL)^(1/4))).                       (R8)

For n>=2 these expressions have fixed rational coefficients and no outer
polynomial prefactors. The original finite branch handles n=1 without
division by L. SC=O(n^2), SQ=O(n), the exact model, epsilon(n)=0 and
success remain those of main10/R4. Resource indices are [1/2,0,0,1/2].
No displayed envelope replaces any actual source/weight/precision cap.

## R6. Exact material source identities

The complete main proof adapts the exact own PSG2-SBG submission proof,
SHA-256 ab233182c257989f5b6592c20f33b7f2ccf8e1996ae6301c893981a5f5857923,
from submission 321bac1d-9e52-408f-b257-30d36939e972, commit
da0dae531d1bf317d093478c7c37ebe592a4bd97. Its immutable source is
[PSG2-SBG proof](https://github.com/Layr-Labs/dcp/blob/da0dae531d1bf317d093478c7c37ebe592a4bd97/submission/proof.md).
It also retains all
PSG2, CS1-BACKWARD, collective-test, CW1S/HS2 and unpublished own-source
credits given in Section 0. Each needed algorithm and proof is reproduced
in this package.

The success-margin audit read PSG13, submission
4c42d100-f644-429d-b50d-7b3e5d226af8, evaluated commit
abf41b73e429dfa332ed263db78bf29363a499fc, member `submission/proof.md`,
SHA-256 fca9c2959397ba2dba8bf71f5a9284335335ff9a41db750623785fd54ca5afd6.
Its immutable source is
[PSG13 proof](https://github.com/Layr-Labs/dcp/blob/abf41b73e429dfa332ed263db78bf29363a499fc/submission/proof.md).
Lines 477--553 give the verified-pair margin and fresh-tree law audited
for this retry calculation. Those passages supplied the earlier own retry configuration. The earlier
paired transfer then used PSG14C's parity/two-row argument. This dense
configuration uses the complete cyclic instrument and first/second-moment
proof in the dense appendix. R1--R5 and that appendix give the full guard
and source proof; no PSG13 wrapper or three-level resource claim is required.

The inspected local audit is `psg13_saved_source_audit.md`, SHA-256
f6d6eac685a43af520846c25031c4db6a13051a16e0d0fa4f12f7a91ce12d89c.
It records exact public predecessor identities and the retry lemma.
Its public PSG9 file is submission e74645e4-aa15-4084-a89f-9f5b0a32993c,
commit 7eca8d7f224e23641d39b6be6b47131ec477611f, proof SHA-256
7d34ebe1a70a052250f02a153ea5d866a5ff9a069f062c000d0c6fa4e04b8c30.
Verified-pair and fresh-call passages were inspected there. The audit
keeps unresolved private aliases `ce0de50` and `33d4854` distinct from
published full files. This package assumes no equality of those aliases.

The retained direct public sources have these exact identities:

| Source | Evaluated commit | Member | SHA-256 |
| --- | --- | --- | --- |
| PSG2, b267909b-a859-49d3-9c64-18eca846b18c | 5292134d56d56a849d16d42063379905bfd297d6 | submission/proof.md | 6dab91a37961032b862229cb80850eadb54979541c7ef34c4141802f4ea69ee9 |
| CS1-BACKWARD, 70936e29-d357-4713-b84f-47acebe365fd | d50e5146cf9f3c924c1cf26e0e725a3f3d2e5ad3 | submission/leap-research/decoder-wave/CS1-BACKWARD/proof.md | 40dcb36879994c071f43235c1f2ce28080020265c7c514c8e179ad1f51a73e3f |
| Collective tests, 844c0fd2-9b1c-4e84-a37c-f402e109985f | 7c4b4ed099799e146213c1e3c43a50151482dc6b | submission/proof.md | c0c011d54153f5e9c8f7436e581a42942e820689e0f52cef6cb8e02e7f1fce96 |
| CW1S, 32303149-73e3-4acd-af1f-4a6052d73869 | 174d649db7c03b0619a486e9ce515c7b95e8ff2d | submission/proof.md | f680e71657013d62c319a71e48ed20c2f0670072b9f494e156101fca0501df84 |

PSG2 supplies discovery, exact verified pairs, fresh-label induction and
the supplier framework. CS1-BACKWARD supplies terminal localization and
backward recovery. Collective tests supply the one-subtraction register
identity. CW1S supplies the distance and stride-score argument and retains
its credit to HS2, 8b85be12-4b9c-40e6-a62f-d2d232d62402. Section 0 also
records the exact unpublished own-source hashes and their specific uses.

## R7. Complete probability-source chronology

The probability transfer first read the exact published PSG14C archive,
submission 30304a9e-15d5-4b58-9998-d5a4ccc1a67e, commit
398d8457f6c25e29a941403e4e75eccb290dda79, proof SHA256
2abeb473f0ea10cd5f7305cf58f8696dddd148967337a851183bfc55254ce0b6,
JSON SHA256 626dd5115b1e5bf45f6fac74e659a902708ae1a580918daa1daa9b4b684b53d6.
Its Section 4.3 reproduces the parity-support and two-row factorial-moment
arguments for the same bounded adjacent-disjoint-pair instrument. These
arguments gave the earlier paired transfer its fresh37/50 certificate.
The present dense24/25 argument is reproduced in dense4--5. PSG14C credits CYG1
and, upstream, CYC1. Those inherited credits are retained.

The bounded own transfer was then frozen as psg14c_retry_transfer.md,
SHA256 42ef49d4387927b1c9c6cf2eeaa7889c7e9fa61c3cff1a849993d39adec8e318.
Only after that freeze did root read the public CYG1 note and then its
exact archive for separate cyclic-instrument research. CYG1 is submission
70564803-3637-426f-9587-e1333aa07b39, commit
ed8984b1d82c7fb891d1ba200c13743589abd34d; its proof SHA256 is
c7903f95a1165d6587f1e09a10cee11d7df74590aefd8efc92f18cf89bcf8aa1,
JSON SHA256 a7297eb330c407f338cd9bb7b0e1602434d60091188c0f00bb8b0313d993744d,
and public-note SHA256
65ef808aa7d153f3bff8236feaf2c1541aa792c88b1557b9bb9ad205cf63eb0c.
That frozen paired transfer kept the adjacent disjoint-pair instrument.
The present dense configuration uses CYG1's exact cyclic instrument with
an eleven-bit rank and list cap2048. Its new density32 probability bound
uses only the fully reproduced first/second moments. No seven-moment
theorem is required, and no verdict is a mathematical premise.

The direct immutable PSG14C proof is
[PSG14C proof](https://github.com/Layr-Labs/dcp/blob/398d8457f6c25e29a941403e4e75eccb290dda79/submission/proof.md).
The later inspected immutable CYG1 archive is
[CYG1 proof](https://github.com/Layr-Labs/dcp/blob/ed8984b1d82c7fb891d1ba200c13743589abd34d/submission/proof.md).
The own bounded transfer and its independent audit record provenance;
every probability, conditional retry and cap argument is reproduced in
this appendix. No unavailable note, acceptance result or external archive
is a mathematical premise. Earlier inherited credits in R6 and compiler
Part D are retained without change.


The direct dense construction is dense_cyclic_source_transfer.md, SHA256
b9404e273739276a67c5d48d699a2dd0a0d1c7abf7323714a3fb438857c209d9,
reproduced in full in grover_dense_dense.md. Its exact CYG1 source credits
CYC1, submission 7a4cecdc-7941-4027-8c95-8520de9fbcf3, commit
cd8f16692833b52dd0fd3a8dd335667eec5a6e61, proof SHA256
e75607fc05101e99cac8480cfbffc23729c64f6f5a03643ee02de917274b4a17,
and PSG1's separate-query discovery/fresh-label framework. No direct CYC1
archive inspection is claimed. All needed instrument and moment arguments
are inside this package. The original local grouped/paired/compiler
sources, later public grouped F and rational-note identities are in the
required bound appendix; all inherited credits in compiler Part D remain.
