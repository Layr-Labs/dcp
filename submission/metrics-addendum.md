# VFD3: source-copy count and fractional malformed-sample tolerance

This addendum concerns exactly the VFD3 algorithm, parameters, finite-prefix
branch and cost model in `proof.md`. It changes no algorithmic step. The
original time and two space bounds and full-secret success guarantee hold
jointly with the source-copy bound below.

The starting point is published VFD3 submission
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

    ell = 1 + ceil((1633/2000) sqrt(n)),
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
The repeated Hadamard tests for a source label operate on that acquired
copy's data register and fresh ancillas; they do not call the DCP source
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

    L_0 = O(sqrt(n) 2^((4899/2000) sqrt(n))).

Also J+1 <= n and ell <= (1633/2000)sqrt(n)+2. Therefore

    R <= 4nL_0 = O(n^(3/2) 2^((4899/2000) sqrt(n))),

and

    (n+10)(2^ell+2)
      = O(n 2^((1633/2000) sqrt(n)))
      = O(n^(3/2) 2^((4899/2000) sqrt(n))).

Combining these inequalities with (1) proves the joint, worst-case bound

    K(N,s;w) = O(n^(3/2) 2^((4899/2000) sqrt(n))).                  (2)

All constants are absolute and independent of N, s and branch w. The
finitely many input lengths n <= 16 have the explicit bound in (1) and
are absorbed by an absolute outer constant. In particular n=1 is covered
without evaluating log(n) in an asymptotic formula.

For the eventually positive envelope

    B_K(n) = n^(3/2) 2^((4899/2000) sqrt(n)),

we have log2 B_K(n) = (4899/2000)sqrt(n) + (3/2)log2 n. Thus
log2(log2 B_K(n)) = (1/2)log2 n + O(1), and its growth index under the
pinned rules is exactly 1/2. The inner coefficient is the explicit rational
4899/2000; it is not an unspecified big-O constant replaced by a number.
This sample bound counts physical input copies and is distinct from the
larger bound on total charged work.

## 3. Guaranteed fractional malformed-sample tolerance: zero

The original theorem assumes fresh independent copies of the specified mixed
state rho_s, for one fixed secret s. It gives no robustness theorem for an
adversary replacing source copies with other quantum states.

For every integer N >= 2 and n = ceil(log2 N), define the guaranteed fraction

    epsilon(n) = 0.                                               (3)

If Q copies are acquired, the permitted malformed count is at most
floor(epsilon(n) Q) = 0. Here a malformed acquisition violates the ideal-source
promise. In addition to having no malformed acquisitions, the joint input law
must consist of independent copies of rho_s; marginal correctness alone does
not suffice. These are exactly the assumptions of `proof.md`, so its proof
supplies unconditional full-secret success at least 1019/1024 > 2/3 for every
N and s, jointly with the original time/space bounds and (1)-(2).

This establishes the fractional guarantee for every n >= 1. The value zero is
in the supported fractional-tolerance-v1 family and requires no asymptotic
threshold. The implied zero malformed count is identical to the earlier DEV
clean-input promise, but this submission explicitly declares a fraction and
requests a fresh joint review under the production v7 policy. No conversion
from an asymptotic sample bound into a fractional promise is used.

Zero is a guaranteed fraction, not a claim of optimal robustness. It does not
assert impossibility of positive tolerance, a per-copy corruption probability,
or an entangled/adversarial/noisy-source guarantee. The ideal-input failure
budget 5/1024 is not a corruption tolerance and is not converted into one.

## 4. Production evaluation and provenance

This production candidate retains the VFD3 algorithm, original proof and all
nine diagnostic artifacts from DEV submission
`6f4423a3-e180-476f-987a-b1c4cdaa898e`, candidate
`c3719a087388963198f068135526bd69fe3ab877`. All four resource claims and their
structured declarations are unchanged. Only this explanatory addendum, the
manifest title, and the fifth claim change for the production fractional
contract. The preceding DEV candidate reused submission
`42e58ec0-80c2-4963-9539-c4fdb27e3ea5`, candidate
`9979b7e2298bf389e883843d714c389dff5e568f`; earlier VFD3 and FD2 provenance
remains in this addendum and `proof.md`. No earlier verdict is a proof premise.

The fresh production clone on 2026-11-06 is pinned to
`cdb1ebff130d861e2c61e9cf517ab66c0a56ca7a`, with required
`dcp-joint-bounds-v7` validity and `dcp-time-growth-v2` scoring. The four
resource claims use `dcp-bounds-v4`. The unscored fifth claim uses
`dcp-fractional-error-tolerance-v1`, expression `0`, and the production seed's
exact clean-input error-model text. The corresponding protected output schema
is `reviewed-fraction-v1`. This differs from the DEV v6 count declaration
`dcp-error-tolerance-v1` and its historical `reviewed-expression-v1` output.

Any official projection must come from this candidate's own trusted review
and dossier. Local checks, diagnostic artifacts, historical verdicts and hash
matches do not substitute for the production joint mathematical review.
