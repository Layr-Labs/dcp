# RS5: every acquired source copy and exact-zero clean-input tolerance

This concerns exactly RS5 in proof.md, recycle-sieve.md, phase-labels.md,
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

R=4(J+1)L_0, ell, L_i=ceil(F*(59/10)^(ell-i)) and F=2^62lambda are the
exact common parameters in proof.md. No outer retries or hidden samples exist.
Early returns only reduce counts. recycle-sieve.md proves
L_0=O(log2 n*2^((282894777/125000000)sqrt n)), J+1<=n and ell<=(88377/100000)sqrt n+2.
The verification copies fit the same bound, giving uniformly

    Q=O(n(log2 n)*2^((282894777/125000000)sqrt n)).

All constants are absolute; finite n<=16 is absorbed, with n=1 explicitly
bounded instead of evaluating asymptotic logn there. The envelope logarithm
is(282894777/125000000)sqrt n+log2 n+log2log2 n, so its exact growth index is1/2.
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
acquisition architecture is retained and re-established for RS5's new group
instrument and quotas. All present claims need fresh joint review; no older
verdict or provisional graph edge establishes them.

RS5 directly reuses SG6 dc8d6d56-9618-46bc-97a3-e9b18ec65099's
primary/triangular rescue component, but changes pairing to whole-bucket
SUM pooling and proves the new conditional populations and quotas in
recycle-sieve.md. This is the single present configuration.

RS5 directly reuses PS7 cda83fcf-1faa-41d5-b858-d5ec44122fe6's
population framework but adds a third SUM pass and globally recycled PRIMARY
rejects. recycle-sieve.md gives the complete changed channel/count/cost proof;
old pass-specific bounds are not assumed unchanged.

## RS5 extension and provenance

This file is adapted from RR8 at ae634c28a7e4a2683087607a83a432adb370b5d7.
The present program adds the fourth SUM channel proved in recycle-sieve.md,
with q=59/10, F=2^62lambda and coefficient 282894777/125000000. The historical
ancestry descriptions above identify inherited material. Any old three-pass
summary is extended by that explicit fourth pass; no predecessor verdict is
used. All five kernels, including the degree-fifteen kernel, have constant
degree and O(n)-bit operands. Their counted adaptive arithmetic fits the
same O(n*2^(20sqrt(log2 n))) logical work per pair with absolute constants.

## RS5 sharper primary-reject coin

RS5 extends RS4 (b16fcbf5-7e11-4148-80f1-cee7ae2df6b5), retaining
its entire four-pass exact stream. In the global primary-V rescue only,
use p=2679/10000, zero coin 2p H^3/J0 and positive coin p H^3/J_delta.
recycle-sieve.md Section 4 proves the stronger exact success p; Section 7
uses DV>=e p PV in the eleven-event proof. Every sample/trial limit remains
unchanged in form, recomputed for q=59/10, r=25607/10000 and F=2^62lambda.
The new resource coefficient is 282894777/125000000. This is a new actual
acceptance instrument and configuration; no old verdict validates it.

## RS5 global V-SUM extension

The current program also retains and globally pairs SUMs from the first
primary-V rescue, as proved in recycle-sieve.md Section 10. Its exact W*W
correlation and positive rational Bernstein certificate establish beta=9/50.
The extra two conditional events give eleven in total. The combined coin
calls for both global V channels remain <=PV, preserving the old literal
4R trial and source limits. No extra source is acquired. All parameters
are recomputed for q=59/10,r=25607/10000 and coefficient282894777/125000000.
The 625-term integer kernel, extra buffers, resets and all full address
charges fit the same ordinary-sieve and space bounds. This is a new
channel, not an assumption of a predecessor's acceptance. RS4V development
submission d034cb7a-4593-4053-a03d-387e4514da0e is materially reused.
