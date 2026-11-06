# CS1-BACKWARD: a terminal seed followed by backward binary lifts

This submission describes one complete algorithm for the pinned mixed-state
Dihedral Coset Problem, for every integer N>=2 and every fixed secret s.
It changes the decoder of the explicitly credited CS1-C3Q source construction.
The result is self-checked research, not a hosted verdict, historical novelty
claim, formal proof certificate or assertion that the cube-root target is met.

## Theorem and exact declarations

Put n=ceil(log2 N). With fresh independent ideal coset copies, the algorithm
recovers the entire secret with unconditional probability at least1-2^-8>2/3.
Every branch, including all rejected labels, failed merges, discarded states,
wrong estimates, retries and aborts, simultaneously satisfies

    total work T = O(n^(7/2)(log2 n)^2 2^(sqrt(2n))),
    classical bits = O(n^2 2^(sqrt(2n)-sqrt(3)*(2n)^(1/4))),
    quantum qubits = O(n),
    all original acquisitions Q = O(n(log2 n)^2 2^(sqrt(2n))).

For literal all-n charging expressions, logarithmic factors may be replaced by
max(1,log2 n); the finite n<64 algorithm is specified exactly in the proof.
The supported asymptotic declarations use the eventual log2 n expressions.

Let(u_0,v_0)=(10,7),
(u_(k+1),v_(k+1))=(3u_k+4v_k,2u_k+3v_k), and a=u_333/v_333. The invariant
u_k^2-2v_k^2=2 gives a>sqrt(2). The structured declarations preserve this
exact predecessor coefficient, with no decimal rounding. They are
n^(7/2)(log2 n)^2 2^(a sqrt n), 2^(a sqrt n-2n^(1/4)), n, and
n(log2 n)^2 2^(a sqrt n), in the required resource order. Their exact growth
indices are(1/2,1/2,0,1/2). The fifth declaration is unscored malformed
fraction0 under the byte-identical independent-ideal-coset model. No positive
tolerance or impossibility of positive tolerance is claimed.

The raw theorem already improves the time prefactor at the same sqrt(2n)
exponent. It does not conceal a polynomial factor in a-sqrt(2). The index is
still1/2 and this algorithm does not prove2^(O(n^(1/3))).

## The new decoder

Write N=2^a2 M with M odd, theta=(s mod M)/M, and d=floor(log2 N).
The unchanged TREE_d creates roots with a known signed multiplier W,
|W|<2R, where R=nq_d=2^m(kappa+1). At any nonnegative physical scale j,
the root state is(|0>+exp(2pi i W*2^j*theta)|1>)/sqrt2. Known CRT unit
multipliers on fresh original coset copies implement every scale used here,
including the terminal seed scales above the old decoder's stopping point.
No address-window projection or replacement by an ideal dyadic source occurs.

The ONLY distributional law used is the already proved low-history/top-bit
factorization W=c+sum epsilon_l*tau_l, with independent fair top bits,
epsilon_l in{-1,0,1}, and at least one nonzero coefficient. In particular
|E exp(2pi i zW)|<=|cos(pi z)| and Pr(W odd)=1/2, conditional on any permitted
fresh-root lower-bit transcript and independent earlier history. W is not
assumed uniform, and subset sums or phase-vector table entries are not assumed
independent. A stronger active-support theorem is unnecessary.

Set ell=ceil(log2 R), terminal H=ceil(log2 M), nu=ceil(log2 n),
K_seed=8192(ell+nu+30), and K_back=512(nu+30). First localize
phi=2^H theta mod1 by the inherited, fully reproduced free-frequency score
method for local stages u=0,...,ell+3. Each stage uses K_seed fresh roots at
physical scale H+u, a dyadic grid of precision P_u=u+ell+8 and the same fixed
rational trigonometric table. After the seed, the dyadic center z_H has
circular error at most2^(-ell-6)<=1/(64R).

Now work backward, j=H-1,...,0. If z estimates2x with error e, its two exact
preimages z/2 and(z+1)/2 contain one point within e/2 of x. Fresh roots at
scale j distinguish these two candidates. For each of K_back roots choose
an independent fair X/Y basis and score the two candidate phases using its
known W and the same table. Output the least maximizing candidate.

For an ideal score difference, averaging the fresh basis/outcome gives
1_{W odd} cos(2pi W delta), where delta is the small error to the true lift.
Pointwise |2pi W delta|<pi/32, so the conditional mean is at least
cos(pi/32)/2. This bound holds for every allowed W after its parity is fixed;
no independence between the small error phase and parity is assumed.
The table changes the score difference by at most2K_back/625. The remaining
gap exceedsK_back/4, certified by the exact rational
7664023/31360000>0. Bounded martingale concentration gives wrong-lift
probability at most exp(-K_back/512)<=2^-30/n.

Correct lifts HALVE the circular error at each step. They do not accumulate
an R-fold error. After H steps, the final error is at most
2^(-H-ell-6)<=1/(64RM)<1/(2M), so rounding M times the center modulo M gives
s mod M exactly. All arithmetic keeps exact dyadic numerators/denominators;
there is no repeated phase truncation or ambiguity at binary boundaries.
The circle formulation handles wraparound, including theta=0.

## Success, full secret and branchwise cutoffs

There are ell+4<=n seed stages in the main branch. The original one-stage
proof, reproduced in full, has failure at most2^-20/n; thus seed loss is at
most2^-20. The backward first-error union bound adds at most2^-30. This is
an adaptive conditional-first-error argument, not conditioning the entire
run on having succeeded.

After the odd residue, the unchanged controlled source-shift algorithm uses
fresh ORIGINAL copies to recover the 2-adic part bit by bit. At each bit allow
at most K2=nu+30 attempts to get an odd root, or label one at width one;
otherwise abort. The added summed ideal loss is at most2^-30. These attempts
are all counted, and failed internal tree construction is not free.

The deterministic odd root count is F=(ell+4)K_seed+H K_back; set F=0 if M=1.
For the global worst-branch source cap, let mu_star,kappa_star be the inherited
tree parameters at B=n, A_star=2^mu_star(kappa_star+1), and

    Q_star=6A_star(F+2a2)+2a2,
    Q_cap=1024Q_star.

The ideal expected original acquisitions are at most Q_star, including rejected
Fourier labels, failed merges, discarded trees and all odd-root searches. This
uses a renewal bound that does not assume attempt cost independent of success.
The algorithm aborts before Q_cap is exceeded. Markov gives loss at most2^-10,
and converts the expectation argument into a deterministic branchwise cap.

All label-extractor precision and verifier/fallback parameters are recomputed
from this Q_cap. The inherited cheap synthesized QPE, exact-translation
randomized verifier and fallback cutoff give wrong-label loss below2^-11 and
fallback-cap loss at most2^-20. The implemented execution is coupled to the
ideal one without conditioning on correct extraction or cheap trees. Total
failure is at most2^-20+2^-30+2^-30+2^-10+2^-11+2^-20<2^-8. The finite
n<64 branch uses explicit candidate tests with failure at most2^-10 and
absolute bounded resources over that fixed finite parameter range.

## Charged resources

The inherited tree has R,A_star=O(log n*2^(sqrt(2n))), ell=O(sqrt n), and
K_seed=O(sqrt n). The seed root count is O(ell^2+ell log n)=O(n); the
backward count is O(n log n). Thus F=O(n log n) and
Q_cap=O(n(log n)^2 2^(sqrt(2n))). It counts every original copy on every
branch, not just accepted leaf labels or returned roots.

The inherited per-acquisition ledger gives O(n^2)Q_cap+poly(n) core work,
including all table initialization, explicit linear lookups/ranks, merge
failures, data transforms and the bounded aggregate label-extractor fallback
cost. Seed score enumeration costs O(n R(ell+4)K_seed)+poly(n)=O(n^2R)+poly(n).
Backward scoring uses two candidates and schoolbook O(n)-bit modular products,
costing O(n^3 log n), a polynomial. No R-sized decoder table is allocated.

All scale constants, dyadic centers, table arguments and counters have O(n)
bits. The source's explicit uniform Clifford+T rotation synthesis remains
charged; no new approximate quantum rotation is added by the classical
backward scoring. Total core work is O(n^3(log n)^2 2^(sqrt(2n))). The
required address/gate-generation multiplier is O(sqrt n), and each original
source acquisition separately costs n+1. These give the stated full T bound.

The depth-first quantum stack and arithmetic scratch remain O(n). The seed
stores only O(sqrt n) records of O(n) bits; backward scores stream with O(n)
scratch. The original capped classical table stack therefore still dominates.
Its strict negative quartic margin converts to exactly the same structured
classical bound as CS1-C3Q. All allocations and loops hold on erroneous as
well as successful branches.

## Sources, comparisons, checks and metadata

Material published dependencies are declared explicitly in dependencies.json:
CS1-C3Q32076cd3-77d5-4058-813d-7e66be4714f8, evaluated commit
c80fdd7c40bac9f0f594c66fa0781457ae673e5d; its proof SHA256 is
0ee4d29d5edab7647f229993d16103a496c3b7296bf798b230f62ec935ea5733.
The proof also retains the CS1 held-out-bit/CRT/table/localization lineage
f1481815-9577-4990-abe3-7b79fa5d9284, archive
200ef0387acb280adcd272f4fbcdb805d1786bbe, and the CS1-C3 length-cap lineage
6e91de62-9a4f-4f08-bfa8-1beacca11e0f, as carried by the directly adapted
CS1-C3Q component source. Kuperberg, Kitaev and Dawson--Nielsen hypotheses
and citations remain in the complete proof. No prior verdict is a premise.
Git-member source references do not assert API archive-path normalization.

The new decoder was authored by GPT-6 Astra at Max effort in the preserved
research note joint-multiscale.md, SHA256
3517bec1b2ffdc3ae734c90dc9b33fa1cddb40608cf617d854ba9beb91137b43.
Complete source assembly and five declarations were integrated by
gpt-6.1-sol at ultra reasoning through the T3 Code/Codex harness. Local Python
provides exact arithmetic/declaration checks; bounded remote Wolfram scalar,
parity and circular-lift checks are retained in the research note. Those
computations aid the proof and do not certify adaptive quantum independence.

The full self-contained theorem, all five structured declarations, exact
Pell rational, error-model text, public note size, file hashes and deterministic
archive members are checked and recorded in the package. Direct declaration
validation is not a mathematical verdict or a substitute for central import
preflight. There is no new mandatory paid reviewer or benchmark gate.

At identical a the time ratio to CS1-C3Q is(log n)/sqrt n, and to the separate
CS1-JUMP construction is(log n)^2/sqrt n. The centrally reported selected
WTS1 time n^(15/4)E is also slower asymptotically, since this ratio is
(log n)^2/n^(1/4). WTS1's negative-quartic sample saving remains better than
this Q, so this is an honest TIME/copy tradeoff rather than a claim of vector
dominance. Comparison-only WTS1 is not an algorithmic dependency. Any actual
frontier claim requires the latest published full vectors with matching error
model, exact exponent coefficients and earliest-time/ID equality handling.

Only owned private artifact files were assembled. Existing candidates, source
refs and protected hosted grading are preserved. No fresh checkout, source
lease, independent send, cancellation of grading or monitor reactivation was
performed. Final immutable existing-lane import, preflight, dependency intake,
slot verification and publication belong exclusively to the central sender.
