# PG3: source-copy count and malformed-sample tolerance

This addendum concerns exactly the PG2 algorithm, parameters, finite-prefix
branch and cost model in `proof.md`. It changes no algorithmic step. The
original time and two space bounds and full-secret success guarantee hold
jointly with the source-copy bound below.

The historical starting point of the reused addendum is VFD3 submission
`c2e60e34-e31d-4a65-8f18-a420030cf3e4`, candidate commit
`fd04f6b1ad73d1c71f5cfe309a0b1ebce1954586`. Its proof and diagnostic artifacts
are retained. The proof's earlier FD2 attribution remains applicable. Neither
the earlier official verdict nor an attribution graph edge is a mathematical
premise; the needed algorithm and proof are present in this submission.

## 1. Count every acquired source copy

For an input modulus N >= 2 and fixed secret s, let n = ceil(log2 N).
Write K(N,s;w) for the number of fresh DCP source copies actually acquired
on an execution branch w. A source copy counts when acquired, even if it is
discarded, rejected, consumed by a failed test, or acquired on a branch that
later aborts. Reusing one acquired register for several operations does not
acquire another source copy. K counts neither gates nor output phase qubits.

All symbols below have exactly their definitions in `proof.md`, Section 1.
In particular, k = n+10. For n >= 17,

    ell = min{u>=1 : 3*u*u-u >= 2*(floor(log2 N)-1)},
    J = floor(log2 N) - 1 - ell,
    lambda = ceil(log2(1024(n+1))),
    F = 1048576 lambda,
    L_0 = F(2*8^ell - 4^ell) + ell*8^ell,
    R = 4(J+1)L_0.

For every execution branch, including aborts and erroneous estimates,

    K(N,s;w) <= N(n+10),                          if n <= 16;
    K(N,s;w) <= R + (n+10)(2^ell+2),              if n >= 17.       (1)

To establish the first line, the finite-prefix branch tests at most N
candidates. It acquires at most k fresh copies for each candidate, stopping
that candidate at the first failed test. Early termination can only reduce
the count.

For the second line, there are J+1 target batches. Each acquires at most
4L_0 fresh source copies, so all initial batch acquisitions total at most R.
The binary phase estimation translations for a source label operate on
that acquired copy's data register and fresh ancillas; they do not call the DCP source
again. Sieve pairing, rational coins, phase measurements, phase-table
generation, and classical reconstruction likewise acquire no additional
DCP copies.

Section 9 of `proof.md` proves that the final candidate set has at most
2^ell+2 members for every reconstructed value, even an erroneous one.
Section 10 acquires at most k fresh copies for each such candidate. These
verification copies are additional to the batch budget R and are included
in (1). All aborts stop acquisition; there is no outer retry or restart
that is omitted from the count.

## 2. Uniform asymptotic sample bound

For n >= 17, Section 11 of `proof.md` establishes

    L_0 = O(sqrt(n) 2^((244949/100000) sqrt(n))).

Also J+1 <= n and ell <= (244949/300000)sqrt(n)+2. Therefore

    R <= 4nL_0 = O(n^(3/2) 2^((244949/100000) sqrt(n))),

and

    (n+10)(2^ell+2)
      = O(n 2^((244949/300000) sqrt(n)))
      = O(n^(3/2) 2^((244949/100000) sqrt(n))).

Combining these inequalities with (1) proves the joint, worst-case bound

    K(N,s;w) = O(n^(3/2) 2^((244949/100000) sqrt(n))).                  (2)

All constants are absolute and independent of N, s and branch w. The
finitely many input lengths n <= 16 have the explicit bound in (1) and
are absorbed by an absolute outer constant. In particular n=1 is covered
without evaluating log(n) in an asymptotic formula.

For the eventually positive envelope

    B_K(n) = n^(3/2) 2^((244949/100000) sqrt(n)),

we have log2 B_K(n) = (244949/100000)sqrt(n) + (3/2)log2 n. Thus
log2(log2 B_K(n)) = (1/2)log2 n + O(1), and its growth index under the
pinned rules is exactly 1/2. The inner coefficient is the explicit rational
244949/100000; it is not an unspecified big-O constant replaced by a number.
This sample bound counts physical input copies and is distinct from the
larger bound on total charged work.

## 3. Guaranteed malformed-sample count: zero

The original theorem assumes fresh independent copies of the specified
mixed state rho_s, for one fixed secret s. It gives no robustness theorem
for an adversary replacing source copies with other quantum states.

Accordingly the guaranteed malformed-sample count for this submission is

    E(N) = 0 for every N >= 2.                                    (3)

Here "malformed" refers to a source acquisition that violates the stipulated
ideal-source condition. For zero malformed acquisitions the input law is
exactly the law in `proof.md`. That proof therefore supplies unconditional
full-secret success at least 1019/1024 > 2/3, jointly with the original
time/space bounds and (1)-(2). This establishes (3) as a guaranteed lower
bound on the tolerated number, without asserting that it is an optimal
upper bound on this algorithm's possible robustness.

Equation (3) is an exact zero count, not O(1), a nonzero constant count, a
fraction of the samples, or a probability of malformed input. The internal
failure budget 5/1024 under ideal inputs is not a malformed-sample tolerance
and is not converted into one. No positive corruption tolerance, entangled
adversarial-source guarantee, or noisy-source guarantee is claimed.

## 4. Revision and representation

The predecessor MDC1 directly reused VFD3-M4 submission
6f4423a3-e180-476f-987a-b1c4cdaa898e, candidate
c3719a087388963198f068135526bd69fe3ab877, with a minimum feasible depth ell.
PG2 retains that schedule and its explicit inside-exponent coefficient
244949/100000, strictly between sqrt(6) and 4899/2000. The sample acquisition
identities (1) still apply. PG2 further replaces the physical source extractor
as specified below, with a smaller charged time bound. All five declarations
require fresh joint mathematical review under dcp-joint-bounds-v6. Earlier
judgments are not used to establish any statement of this candidate.

## 5. PG2 source extractor replacement

PG2 reuses MDC1 submission 7c30b190-e90b-492c-b52c-29cf1a9da1a7. Its
phase-labels.md replaces source-label extraction by binary QPE and one shared
bounded approximate gradient. Gradient preparation acquires zero source
copies, and each extraction still consumes exactly its one acquired copy.
Consequently both exact branchwise acquisition bounds and the sample envelope
above apply unchanged, including preparation aborts (which acquire zero).
The extra global trace-distance and preparation-abort errors, together with
the new ideal QPE label-error union bound, fit the original source error budget
of 1/1024, so success remains at least 1019/1024. The only changed resource
claim is the smaller time polynomial power 9/2, proved in phase-labels.md
Section 6 and proof.md Section 11. The independent ideal-source assumption,
exact-zero tolerance and error-model text remain unchanged.

## 6. PG3 coherent extraction and exact fast rounding

PG3 directly reuses PG2 submission 873cba1f-780f-4fad-bd5b-9cf12b8de874
and the MDC1/VFD3-M4 foundations acknowledged above. It substitutes one
coherent modular translation and a truncated binary inverse Fourier circuit,
with exact fast classical rounding. These operations still acquire zero
extra source copies. The same branchwise sample count and clean-input
tolerance therefore apply. The new global source error accounting in
phase-labels.md and fast-labels.md remains below 1/1024, preserving success
1019/1024 and all three non-time resource envelopes. The charged time
polynomial power is reduced to 4 by the complete fast-labels.md analysis.
No historical algorithm paragraph overrides these PG3 execution definitions.
