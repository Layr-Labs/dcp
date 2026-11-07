# Required appendix: PSG2-DENSE-E rational envelope and source identity

This appendix and grover_dense.md, grover_dense_caps.md,
grover_dense_oracle.md, grover_dense_compiler.md and grover_dense_dense.md
define one complete algorithm. The selected kappa is 5/32. Main (9.5a)
and cap R8a prove the actual source pre-envelope; dense11/main(9.9a)
prove the complete work E4. The exact guard is Qcap_dense with the rational
minimum, while Qcap_old retains the exact extractor/pool precision and
Wcap keeps its old value. The same executed profile is used. The proof
below changes no operational cap, source transform, decoder or error budget.

The complete passed paired source used for construction has main SHA256
92505651a374957979bd8ba00e2698f7b4a3b5573304020b246ce71192915365,
caps a792ced4068cc0e52c26de5da929b77edbe6b9fba493f67254e07fbf889aae0e,
JSON 49e0ffe92642b5a31d9464529d7789ca80533301229d2fc7a4ee80bf20baaabb,
with original local oracle d34f10863ec822ea9e1153f501eae1e7c1a9337a8d4ac4847f75a060aa2c0414
and compiler cf4b575204c25ef8a0911fd4ebefca5ce465267acd91931d14569584d9cf551d.
The new files adapt the dense instructions narrowly; they do not claim
byte identity to those original algorithms. The dense source is
b9404e273739276a67c5d48d699a2dd0a0d1c7abf7323714a3fb438857c209d9,
with all of its mathematical content reproduced in the dense appendix.

The original local complete grouped source was main
079b9fcd68c7d0e0a116efd8dda21586fa723f6eff8a89aa6e8e8e9e98283744,
caps 5b66577a50211a3fac45beb0efcfda0cf94ba387c7d3e2748fb6ea81c16b875c,
JSON 115919ddb0fe5a7e44a26b09a6de7cb56b10de6a7b468e503bf7015e3af6f8be,
with the local oracle/compiler hashes above. That source predates its
later public F publication, submission aa3ec389-f35c-4992-9b6f-e8b37f3359ac,
commit a43e8867eae10e718c329de529d3364a82519f59. The exact published main
member is submission/grover_grouped.md with the same 079b9fcd...83744 hash.
[Public grouped source](https://github.com/Layr-Labs/dcp/blob/a43e8867eae10e718c329de529d3364a82519f59/submission/grover_grouped.md).
Published caps and oracle match the local hashes. The published compiler
has SHA256 bd2645f64079e2271ecc91859e52edfc748e7efd50013b1d744ff92f5684ece4;
it differs from the actual original local cf4b...51d by one EOF LF only.
This records actual local-first history and exact later publication; no
source equality beyond those checked bytes or verdict premise is assumed.

The local bounded grouped source was grouped_oracle.md, SHA256
a922b88fa5815e0caf00835c2fd4309832806f5dca39f44e76032730e6e60272.
The physical stored-stream method came from stored_oracle_stream.md,
SHA256 366497582e1c87ceb0e2e48ecf5aa40e7e3ad52b86ec3e4cf09d2a49da167927.
The earlier scan compiler was grover_stride_compiler.md, SHA256
4c5bcd59c95fa2c10be21ab610cdfe76f6b8d2d31300582b97417a7f5b7e896f,
which reused critical_third_cache_generator_l2.md, SHA256
eb122317b103da59cdd982b29f863da27d1d932313e8b67861d1d212a64088f3.
Only their actual compiler methods are reused. Cap R6/R7, dense1 and
compiler Part D preserve all direct public, original private-source and
inherited credits, including the PSG14C-first then later CYG1 chronology.

The earlier pair-envelope draft was used only as a text layout. Correctness
and resources here are proved from the complete paired algorithm, the
complete dense substitution and the rational proof below, all inside
this package. No status of that text template is a mathematical premise.

The complete rational proof below is copied verbatim from
 grover_rational_envelope.md, 6,817 bytes, SHA256
52beb2406a880e26bcbb34a910a40658a06044d44d082743b62faf283c11a3c8.
Its source-status paragraphs and historical kappa examples retain their
original meaning. Its general E7 implication applies here with the separately
proved kappa=5/32. Current main/cap/dense files supply every premise inside
this package. The selected final bounds are E6/E8 with this kappa and zero
outer polynomial prefactors. Formulas apply for n>=2; the original finite
branch covers n=1 without dividing by L. All old .71 displays are auxiliary.

## Complete verbatim rational proof

# A smaller rational envelope for the unchanged truncated profile

This is a bounded proof. It changes no algorithm, full candidate, stage or
declaration. The following envelope needs independent review before use.

## 1. Exact inputs and scope

The direct local source is the complete grouped proof `grover_grouped.md`,
SHA-256 `079b9fcd68c7d0e0a116efd8dda21586fa723f6eff8a89aa6e8e8e9e98283744`,
especially Sections 9.1--9.5. The source uses the literal truncated profile

    delta(v)=ceil(log2(3(2v+1)))+1,
    u=floor(sqrt R),

and the least positive integer R for which twice the retained profile sum
is at least n. All logarithms in resource formulas have base two. On the
main branch n>=256 and L=log2 n. The original finite branch stays unchanged.
As in the source, displayed resource envelopes apply for n>=2. The unchanged
finite branch covers n=1 (N=2); no expression divides by L at n=1.

The required source appendices remain those of the complete grouped package.
This note does not replace their algorithm, probability, controller or space
proofs. It proves a sharper envelope for their already bounded work.

The original source-saving coefficient is kappa=7/80. The independently
reviewed bounded pair transfer supplies kappa=43/320 in its own complete
integration; that value is not a premise needed for the time result here.
The same envelope argument applies to any fixed kappa for which the full
algorithm separately proves the pre-envelope source bound below.

The source's leading rational 71/100 is replaced by 177/250. Polynomial
prefactors can also be removed by a proved gap between an intermediate
profile bound and this declared coefficient. This is a bound improvement,
not a change to the executed profile or a new finite-input algorithm.

## 2. Integer profile bound

Let S_u(R) be the retained profile sum. The complete source proves

    D_R<=log2 R+6,
    2 S_u(R)>=R^2/D_R-2R.                         (E1)

For completeness, the full descending profile has gaps at most D_R.
Upper rectangles cover [0,R], so twice its sum is at least R^2/D_R.
The removed tail starts below u and has sum at most u^2<=R. This gives E1.
No monotonicity of S_u is needed: one feasible test value bounds the least
feasible R, which is how the actual algorithm defines R.

Fix the integers and rationals

    L0=65536,
    rho=283/400=0.7075,
    c=177/250=0.708,
    d0=2001/4000=0.50025.

For L>=L0 choose Rtest=ceil(rho sqrt(nL)). Then Rtest<=sqrt(nL), since
(1-rho)sqrt(nL)>=1. Consequently

    D_Rtest<=L/2+(log2 L)/2+6<=d0 L.               (E2)

At L0 the last non-L/2 term is 14, which is less than L0/4000.
The function ((log2 L)/2+6)/L decreases for L>=L0: its derivative has
numerator 1/(2 ln 2)-(log2 L)/2-6<0. Thus E2 holds on the full interval.

The exact rational calculation is

    rho^2-d0(1+1/2000)=449/8000000>0.

Therefore Rtest^2/D_Rtest>(1+1/2000)n. Also sqrt(n)>=4000 sqrt(L).
At L0 this follows from 2^32768>2^20>4000*256. The ratio
2^(L/2)/sqrt(L) increases thereafter. Thus n/2000>=2 sqrt(nL)>=2Rtest.
Equation E1 proves 2 S_u(Rtest)>=n. The selected R satisfies

    R<=ceil(rho sqrt(nL)),
    2^R<=2*2^(rho sqrt(nL)).                       (E3)

This is a statement about the unchanged normal profile search. No advice,
enumerated exception table or new algorithmic branch is introduced.

## 3. Removal of the polynomial factors

The complete grouped controller proof supplies the stronger internal bound

    T=O(n^2 L log2(L+2) 2^R).                      (E4)

For L>=L0,

    log2(n^2 L log2(L+2))
      =2L+log2 L+log2(log2(L+2))<=3L.

For example L+2<=2^L gives log2(log2(L+2))<=log2 L, and
2 log2 L<=L for L>=4. Further,

    3L <= (1/2000)sqrt(nL).                       (E5)

At L0 this follows from 2^32768>2^21>6000*256; the same increasing ratio
used in Section 2 proves it for larger L. Since c-rho=1/2000, E3--E5 give

    T=O(2^((177/250)sqrt(nL))).                    (E6)

For copies, suppose the complete selected algorithm proves

    Q=O(n^(5/4)L^(1/4)
        2^(R-kappa sqrt(n/L)-(1/2)(nL)^(1/4))+n).  (E7)

The grouped source-cap derivation gives E7 with kappa=7/80 before its old
71/100 substitution. The pair cap derivation gives its own kappa=43/320.
Any other value requires its own complete source proof; this note does not
supply an improved discovery probability or source recurrence.

The logarithm of the E7 prefactor is (5/4)L+(1/4)log2 L<=3L. Apply E3 and
E5 again to obtain

    Q=O(2^((177/250)sqrt(nL)
           -kappa sqrt(n/L)-(1/2)(nL)^(1/4))).      (E8)

The additive n is included. For fixed kappa the negative terms are lower
order than sqrt(nL), while log2 n=o(sqrt(nL)); hence the displayed envelope
eventually exceeds n. Its remaining finite prefix changes only the outside
constant. Equivalently, one can keep +n until that elementary comparison.

All operational acquisition caps, precision caps, weighted-work caps,
source transforms, decoders and aborts remain exactly as in the chosen full
algorithm. The sharper envelope must not be substituted for any actual cap.
The classical and quantum space proofs are unchanged: O(n^2) and O(n).
The source model and unconditional success theorem are also unchanged.

## 4. Uniformity, finite inputs and structured claims

For n<2^65536 execute the same existing finite or normal branch. There are
finitely many n, N and secrets in this prefix. Each all-outcome acquisition
and work cap is finite. The positive target envelopes therefore have a
finite maximum resource ratio over this prefix. This is a uniform outside
big-O constant. It is not advice or a nonuniform family, and no part of the
algorithm tests the threshold in this proof.

For the new time expression, nPower=0 and logPower=0; the exponential term
has coefficient 177/250, nPower=1/2 and logPower=1/2. For the source
expression, nPower=0 and logPower=0; retain the selected source's two
negative exponential terms, and replace only its leading coefficient by
177/250. The bounds on classical and quantum space stay n^2 and n.
All five formal claims must be current-only and must cite the complete
selected algorithm plus this proof if a future full package uses it.

The time-growth and source-growth indices remain 1/2. Indeed their
logarithms have leading term (177/250)sqrt(nL), and all source corrections
are lower order. This note makes no claim about a new algorithm or a
change in the exact success probability.

## 5. Checks and release state

Exact rational arithmetic checked the rho/d0 capacity gap, c-rho=1/2000,
the endpoint inequality 14<65536/4000 and 2^21>6000*256. These calculations
check the written constants; they do not replace the interval arguments.
Independent review and a complete consistent candidate are still required.
No stage or submission is authorized by this bounded note alone.
