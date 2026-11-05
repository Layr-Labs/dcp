# RR9: every acquired source copy and exact-zero clean-input tolerance

This concerns exactly RR9 in proof.md, recycle-sieve.md, phase-labels.md,
fast-labels.md and adaptive-arithmetic.md. Let n=ceil(log2 N), k=n+10,
and Q(N,s;w) count every fresh source copy on branchw, including discarded,
rejected, failed and aborted acquisitions. Internal reuse is not another copy.

## 1. Exact branchwise acquisitions

For n<=16 the unchanged exhaustive branch tests at mostN candidates using
at mostk fresh copies each, soQ<=N(n+10). For n>=17 the J+1 batches each
acquire at most4L_0 copies. Every extractor uses exactly that single acquired
copy. Source arithmetic, Fourier/gradient preparation, pooled-sum salvage,
new rational coins and all generated matrices acquire no extra copies.
The all-outcome candidate interval has at most2^ell+2 members even on
erroneous estimates; verification uses at mostk fresh copies per candidate.
Thus on every branch, including every failure,

    Q<=4(J+1)L_0+(n+10)(2^ell+2), n>=17.

## 2. Uniform sample envelope and index

R=4(J+1)L_0, ell, L_i=ceil(F*(599/100)^(ell-i)) and F=2^68lambda are the
exact common parameters in proof.md. No outer retries or hidden samples exist.
Early returns only reduce counts. recycle-sieve.md proves
L_0=O(log2 n*2^((2272694063469/1000000000000)sqrt n)), J+1<=n and ell<=(880017/1000000)sqrt n+2.
The verification copies fit the same bound, giving uniformly

    Q=O(n(log2 n)*2^((2272694063469/1000000000000)sqrt n)).

All constants are absolute; finite n<=16 is absorbed, with n=1 explicitly
bounded instead of evaluating asymptotic logn there. The envelope logarithm
is(2272694063469/1000000000000)sqrt n+log2 n+log2log2 n, so its exact growth index is1/2.
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
acquisition architecture is retained and re-established for RR9's new group
instrument and quotas. All present claims need fresh joint review; no older
verdict or provisional graph edge establishes them.

RR9 directly reuses SG6 dc8d6d56-9618-46bc-97a3-e9b18ec65099's
primary/triangular rescue component, but changes pairing to whole-bucket
SUM pooling and proves the new conditional populations and quotas in
recycle-sieve.md. This is the single present configuration.

RR9 directly reuses PS7 cda83fcf-1faa-41d5-b858-d5ec44122fe6's
population framework but adds third and fourth SUM passes and globally recycled PRIMARY
rejects. recycle-sieve.md gives the complete changed channel/count/cost proof;
old pass-specific bounds are not assumed unchanged.

RR9 directly reuses RR8 submission4e2ca900-70e1-4923-a469-ea5a1bc0e25b.
Its current exact stage has FOUR SUM-chain levels and global-V success
v=267949/1000000, proved in recycle-sieve.md. The changed kernel B_d has
degree15. All current costs include it and the changed zero-label V coin.
