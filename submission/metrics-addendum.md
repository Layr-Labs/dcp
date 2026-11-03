# VFD3: source-copy count and malformed-sample tolerance

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

## 4. Evaluation and representation

This schema migration retains the algorithm, proof and all five mathematical
guarantees of submission `42e58ec0-80c2-4963-9539-c4fdb27e3ea5`, candidate
`9979b7e2298bf389e883843d714c389dff5e568f`. No earlier verdict is a proof premise.
The source-copy bound and exact-zero tolerance above apply unchanged.

The fresh DEV clone on 2026-11-03 is pinned to
`ccca08c059492a6b056a79375b2f43b97b5fa044`, with the required
`dcp-joint-bounds-v6` policy. The four resource claims use `dcp-bounds-v4`.
The unscored tolerance claim uses `dcp-error-tolerance-v1`, expression `0`,
and the clone's canonical clean-input `error_model` text. This is the same
ideal independent-source assumption used in Section 3; E(N)=0 there is the
constant law tau(n,Q)=0 for the same acquired-copy count Q.

The protected exporter can now project all four reviewed resource claims and
the reviewed tolerance expression. The export name `reviewed-expression-v1`
is distinct from the candidate declaration's `dcp-error-tolerance-v1` schema.
Any official projection must come from the new candidate's own trusted
review and dossier; no source or evidence hashes are supplied as acceptance.
