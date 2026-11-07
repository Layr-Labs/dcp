# Required appendix: PSG2-GBGR retry caps

This appendix, `grover_grouped.md`, `grover_grouped_oracle.md` and
`grover_grouped_compiler.md` define one algorithm. Main-file
section numbers refer to that file. For n>=256 the profile, q0, all source
transforms, discovery circuits, decoder counts, pool parameters, K2 and
weighted-attempt cap are the explicit ones in Sections 2--8. This appendix
proves its source guard. No evaluation result is a proof premise.

## R1. Fixed parameters and two distinct source budgets

Let m=mstar, u, R and v_1,...,v_m be the retained global profile of
Section 4. It is computed from n once. The tree width D can vary, but
this nominal profile does not. Define

    C=C_old=6(2u+1)2^(R-u-m+1), H0=F+2n,
    Qstar_old=C H0+2n, Qcap_old=1024 Qstar_old,
    Qstar_new=ceil(3^m C H0/4^m)+2n,
    Qcap_new=1024 Qstar_new,
    Wstar=6*2^R H0, Wcap=1024 Wstar.

All symbols are fixed before the main run. For M=1, F=0. For M>1,
F is the exact count from the h<16 fallback or h>=16 strided schedule.
The suffix `old` marks an auxiliary budget inside this configuration.
It sets EXTRACT precision and the analysis pool bound. It is not the
acquisition guard. Every acquisition is checked against Qcap_new.
Every combiner attempt is checked against the fixed Wcap after its
children are built and before its oracle array or queries are built.

C is integral: each retained gap is at least five, so
R-u>=R-v_1>=5(m-1) and R-u-m+1>=0. Compute the new ceiling by integer
powers and division. The numerator 3^m C H0 and denominator 4^m have
O(m+R+log(n+2)) bits. This gives polynomial setup work and at most
O(n^2) classical scratch by schoolbook arithmetic. Counter widths can
use the auxiliary Qcap_old bound. This setup is included in Section 9's
polynomial setup charge.

## R2. Conditional retry cost

Equation (4.1) proves, for every fresh node attempt,

    p_success>=463/1024>4/9.

This probability is conditional on the external past before fresh
children are generated. It averages the fresh independent uniform low
child labels and the search coins. It is not conditioned on an arbitrary
fixed child-label list, successful extraction, or later cap survival.
Section 5's unused-block induction supplies exactly this fresh-label law.
Every failure discards all children and starts with new independent calls.

Let E_i bound expected acquisitions for a level-i output, uniformly over
the external past before that call. At a positive width its attempt uses
r_i child calls. The conditional expected cost of this attempt is at most
r_i E_(i-1). The conditional probability that another attempt is needed
is at most 5/9. Thus

    E_i <= sum_(t>=1) (5/9)^(t-1) r_i E_(i-1)
         = (9/4) r_i E_(i-1).                         (R1)

The cost of an attempt can depend on whether it succeeds. This does not
change (R1). To bound its t-th term, condition on reaching attempt t,
then use its uniform fresh-child cost bound. The event of reaching it
depends only on earlier attempts. No cost-success independence is used.
A zero-width level returns its child, with no attempt and no multiplier.
An accepted raw leaf has expected cost at most two originals.

For any requested D, let I contain its positive-width levels, and put
rbar_i=2v_i+1 for every retained level. Section 4 has r_i<=rbar_i.
Every factor (9/4)rbar_i exceeds one. Therefore

    E_root <= 2 product_(i in I)((9/4)r_i)
           <= 2 product_(i=1)^m((9/4)rbar_i)
            = (3/4)^m [2 product_(i=1)^m(3rbar_i)].    (R2)

The full nominal factors may be inserted even when a lower level is
zero or partial. This is an upper bound; it does not assert execution
of those levels. For B=D-1=0 the output is one leaf, whose expected
cost is at most two; (R2) still applies.

The profile recurrence gives, for i>=2,

    3rbar_i<=2^(v_i-v_(i-1)-1).

Consequently

    2 product_(i=1)^m(3rbar_i)
      <=6(2v_1+1)2^(R-v_1-(m-1))
      <=6(2u+1)2^(R-u-(m-1))=C.                      (R3)

The last step uses v_1>=u and the decrease of (2x+1)2^-x on positive
integers. Equations (R2)--(R3) prove, uniformly for every D,

    E_root <= (3/4)^m C.                              (R4)

The same nominal m is used for every root, including all-zero and partial
lower profiles. Applying a saving only to the active depth is unnecessary.

## R3. All decoder cases and incorrect earlier outputs

For n<256, execute the finite exhaustive procedure of Section 8. It uses
neither this profile nor these caps. The whole range is finite, so its
explicit maximum changes only the absolute envelope constants.

For n>=256 and M=1, set F=0 and skip the odd decoder and its pool.
For M>1, keep C, A, g, h, Delta, physical scales and root counts from
Section 6.3. If h<16, use F=F_old and the specified one-bit seed and
backward lifts. If h>=16, use the exact strided seed and backward counts.
Every such root has D=d, B=d-1, so (R4) applies in both cases.

At a 2-adic width wd>=2, use the same global profile with D=wd and
B=wd-1. Conditional parity is fair by (5.3), including after an incorrect
odd residue or earlier bit. Sum over the geometric number of root calls:
there are at most two calls in expectation for each bit. Conditional
expected root cost is bounded by (R4) at every fresh call, so this sum
needs no independence between root cost and its parity. The truncation
at K2=ceil(log2 n)+30 attempts only reduces the expectation. Its failure
probability is at most n2^-K2<=2^-30.

At width one, each direct attempt uses one fresh copy. Its known label
is odd with conditional probability one half, so expected cost is at
most two. Retain the explicit 2n direct-copy term in Qstar_new.
This overcounts safely when wider 2-adic bits also use the H0 term.

An earlier incorrect scalar output can make stored reduced labels differ
from the actual phase labels. It does not change equal basis magnitudes.
Residue and pair measurements have probabilities determined by basis
membership; the separate Grover queries use only known low labels.
Physical shifts by the recorded scalar preserve uniform fresh Fourier
labels. Thus the low-label induction, success margin and parity law
continue to bound resources on these histories. Correct phase identities
are used for correctness only after earlier scalar outputs were correct.

It follows that the ideal reference process, with the scalar attempt
caps but without the source or weighted caps, has expected acquisitions

    E Q_ideal <= (3/4)^m C(F+2n)+2n <= Qstar_new.       (R5)

It may continue beyond any physical cap only in this probability
analysis. No uncounted physical acquisition is executed.

## R4. Weighted attempts, pool, extraction and success

Keep the weighted cap unchanged. The weaker bound p_success>=1/3 is
still valid. The conditional geometric proof in Section 8 bounds the
expected number of level-i attempts by

    3 product_(j>i)(3r_j).

With nominal upper factors for omitted levels, Section 5 gives
product_(j>i)(3r_j)<=2^(R-v_i-(m-i)). Charging each executed attempt
weight 2^v_i and summing gives less than 6*2^R per root. The same fair
parity sum over all roots gives expected total weight at most Wstar.
Failed ancestors and children built before a failed weighted check remain
charged. Zero-width levels have no combiner weight.

Apply Markov to the ideal acquisition count in (R5) and separately to its
weighted total. The Qcap_new cutoff and Wcap cutoff each have probability
at most 2^-10. A check aborts before its action. Thus the actual counts
obey these caps on every branch. No independence of caps and decoder
events is assumed.

Since C H0 is an integer and (3/4)^m<=1,

    ceil((3/4)^m C H0)<=C H0,
    Qcap_new<=Qcap_old.                               (R6)

For h>=16 retain the conceptual pool A=2^40(C+1)U^3 exactly. Section 6.3
proves Qcap_old<=2^27(C+1)U^2<=A. Hence Qcap_new<=A. This pool is a
proof variable, not allocated storage. The same low-bit distance event
has failure below 2^-190. Conditional on the low construction transcript,
uninspected top bits of disjoint fresh roots remain independent and fair.
Fitodd uses the new source cap and the fixed weighted cap; it is still
low-transcript measurable. No later cap-survival event is added to the
top-bit conditioning. Thus Sections 6.5--6.6 retain odd-decoder failure
at most 2^-20 on the distance and fit events.

EXTRACT keeps the exact precision rule

    h_ext=ceil(log2(2^16 Qcap_old(n+5))).

For every latent label and earlier history, its per-call error is at most
1/(2^14 Qcap_old). There are at most Qcap_new calls. Equation (R6) and
actual/ideal coupling to the first label error or cutoff bound the total
label error by 2^-14. This does not condition the fresh-label law on
correct extraction. Reusing the larger precision budget changes no
quantum circuit, field width or work estimate from Section 3.

For the strided branch the complete failure bound is

    2^-190+2^-20+2*2^-10+2^-14+2^-30 < 2^-8.

For h<16, seed and lift failures are at most 2^-20 and 2^-30. Including
the two caps, extraction and 2-adic attempt cap gives

    2*2^-10+2^-14+2^-20+2*2^-30 < 2^-8.

For M=1 there is no odd-decoder loss. The finite branch fails with
probability below 2^-10. These cases prove unconditional full-secret
success at least 1-2^-8 for every N and s. Every failed, partial and
aborted construction remains in the resource counts.

## R5. Every-branch resources and the exact new source term

Section 9 proves, with L=log2 n,

    2^R=O(2^((71/100)sqrt(nL))),
    u>=(1/2)(nL)^(1/4)-1,
    2u+1=O((nL)^(1/4)),
    m>(1/16)sqrt(n/L), H0=O(n).

The fallback h<16 occurs at finitely many n uniformly in N and s.
Its finite maximum is included in the same absolute constants.
As (4/3)^5>4, log2(4/3)>2/5. Therefore

    2^(-(m-1))(3/4)^m
      =2*2^(-(1+log2(4/3))m)
      <=2*2^(-(7/80)sqrt(n/L)).                       (R7)

From the exact Qcap_new formula, allowing the ceiling's additive one,

    Q<=Qcap_new
      =O(n(2u+1)2^(R-u-(m-1))(3/4)^m+n)
      =O(n^(5/4)L^(1/4)
          2^((71/100)sqrt(nL)-(7/80)sqrt(n/L)
              -(1/2)(nL)^(1/4))).                    (R8)

The last exponential eventually dominates the additive n. The finite
remainder changes only an absolute constant. Equation (R8) counts all
failed and discarded acquisitions on every branch.

Wcap=O(n2^R) remains fixed. Bounds for all indexed gates, oracle work,
recursion movement, abort cleanup, source transforms, extraction and
gate generation in Section 9 can use the auxiliary bound Qcap_old.
The smaller acquisition guard executes a prefix of the same reference
process. Cap setup adds only the polynomial work already charged in R1.
The complete selected bit-stream proof is reproduced in the required
compiler appendix; main Section 9.5 includes every separate work term.
Thus the simultaneous bounds are:

    T=O(n^2 L^(3/2) 2^((71/100)sqrt(nL))),
    S_C=O(n^2), S_Q=O(n).

The structured source term uses coefficient -7/80, nPower 1/2 and
logPower -1/2. Its other terms and polynomial prefactors are exactly
(R8). The exact growth indices are [1/2,0,0,1/2]. The clean-source model
and zero tolerated malformed fraction are exactly those in Section 10.

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
for this retry calculation. The same 463/1024 constant is derived in
Section 4 of the main proof. R1--R8 give the complete sharper resource
argument; no PSG13 wrapper or three-level resource claim is required.

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
