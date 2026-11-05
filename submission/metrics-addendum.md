# SG6: every acquired source copy and exact-zero clean-input tolerance

This concerns exactly SG6 in proof.md, salvage-sieve.md, phase-labels.md,
fast-labels.md and adaptive-arithmetic.md. Let n=ceil(log2 N), k=n+10,
and Q(N,s;w) count every fresh source copy on branchw, including discarded,
rejected, failed and aborted acquisitions. Internal reuse is not another copy.

## 1. Exact branchwise acquisitions

For n<=16 the unchanged exhaustive branch tests at mostN candidates using
at mostk fresh copies each, soQ<=N(n+10). For n>=17 the J+1 batches each
acquire at most4L_0 copies. Every extractor uses exactly that single acquired
copy. Source arithmetic, Fourier/gradient preparation, four-input salvage,
new rational coins and all generated matrices acquire no extra copies.
The all-outcome candidate interval has at most2^ell+2 members even on
erroneous estimates; verification uses at mostk fresh copies per candidate.
Thus on every branch, including every failure,

    Q<=4(J+1)L_0+(n+10)(2^ell+2), n>=17.

## 2. Uniform sample envelope and index

R=4(J+1)L_0, ell, L_i=ceil(F*(739/100)^(ell-i)) and F=2^32lambda are the
exact common parameters in proof.md. No outer retries or hidden samples exist.
Early returns only reduce counts. salvage-sieve.md proves
L_0=O(log2 n*2^((481/200)sqrt n)), J+1<=n and ell<=(5/6)sqrt n+2.
The verification copies fit the same bound, giving uniformly

    Q=O(n(log2 n)*2^((481/200)sqrt n)).

All constants are absolute; finite n<=16 is absorbed, with n=1 explicitly
bounded instead of evaluating asymptotic logn there. The envelope logarithm
is(481/200)sqrt n+log2 n+log2log2 n, so its exact growth index is1/2.
This all-acquisitions count is distinct from total work or peak stored qubits.

## 3. Exact-zero malformed-copy context

The guaranteed malformed-copy expression is exactly tau(n,Q)=0, with the
canonical independent ideal-source model in submission.json. Malformed means
an acquisition violating that promise. With zero malformed acquisitions,
the complete source/gradient, coin-cap, shortage, outer-phase and verification
proof gives unconditional success at least1019/1024 for everyN,s, jointly
with all four resource bounds. This is a clean-input guarantee, not positive
robustness, its impossibility, a nonzero constant or a conversion of failure
probability into corrupted-copy count. The fifth claim has no numeric score.

## 4. Material sources

Direct sources include PG5 7e1c8dba-adc8-46db-bf59-1f31688d41c2 and the
explicit PG4/PG3/PG2/MDC1/VFD3/FD2 foundations named in proof.md. The exact
acquisition architecture is retained and re-established for SG6's new group
instrument and quotas. All present claims need fresh joint review; no older
verdict or provisional graph edge establishes them.
