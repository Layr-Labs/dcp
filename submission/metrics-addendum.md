# RS6: every acquired source copy and exact-zero clean-input tolerance

This concerns exactly RS6 in proof.md, recycle-sieve.md, phase-labels.md,
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

R=4(J+1)L_0, ell, L_i=ceil(F*(293/50)^(ell-i)) and F=2^62lambda are the
exact common parameters in proof.md. No outer retries or hidden samples exist.
Early returns only reduce counts. recycle-sieve.md proves
L_0=O(log2 n*2^((112940423/50000000)sqrt n)), J+1<=n and ell<=(44273/50000)sqrt n+2.
The verification copies fit the same bound, giving uniformly

    Q=O(n(log2 n)*2^((112940423/50000000)sqrt n)).

All constants are absolute; finite n<=16 is absorbed, with n=1 explicitly
bounded instead of evaluating asymptotic logn there. The envelope logarithm
is(112940423/50000000)sqrt n+log2 n+log2log2 n, so its exact growth index is1/2.
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
acquisition architecture is retained and re-established for RS6's new group
instrument and quotas. All present claims need fresh joint review; no older
verdict or provisional graph edge establishes them.

The development inherited through RR8 reuses SG6 dc8d6d56-9618-46bc-97a3-e9b18ec65099's
primary/triangular rescue component, but changes pairing to whole-bucket
SUM pooling and proves the new conditional populations and quotas in
recycle-sieve.md. This is the single present configuration.

The development inherited through RR8 reuses PS7 cda83fcf-1faa-41d5-b858-d5ec44122fe6's
population framework but adds a third SUM pass and globally recycled PRIMARY
rejects. recycle-sieve.md gives the complete changed channel/count/cost proof;
old pass-specific bounds are not assumed unchanged.

## Current configuration and direct source provenance

This file is adapted from published RR8 at candidate
 ae634c28a7e4a2683087607a83a432adb370b5d7. RS4 and RS4V added the exact
fourth same-bucket SUM channel and sharper p=2679/10000 primary-V coin;
RS5 added a global V-SUM rescue with success9/50. RS6 retains those
channels and adds the disjoint first-V-reject rescue proved below and in
recycle-sieve.md Section11. All inherited PG4/PG5, SG6/PS7 and VFD3/FD2
acknowledgments identify material retained THROUGH RR8; they do not assert
that the current author fetched each unpublished intermediate artifact.
Every needed proof is reproduced; no prior verdict is a premise.

## RS6 first-global-V rejected-difference rescue

The actual RS6 program also retains the REJECTED difference category from
the FIRST global primary-V pass. recycle-sieve.md Section 11 proves its
nonuniform S/(4642H^4) law, exact 121-term correlation evaluator, positive
rational piecewise Bernstein certificate, small-H cases and success1/8.
It uses already acquired qubits, no new source and no free count oracle.
There are thirteen conditional events. All global channels together now
have <=3PV/2 coin calls; total stage calls are <=7L_i/8, replacing the
old 3L_i/4 theorem. Section 8 proves fewer thanR calls and preserves the
literal4R physical-trial cutoff. Extra buffers and all O(n)-bit kernel
arithmetic, generation, addresses and resets fit the same envelopes.
The actual new schedule is q=293/50,r=25509/10000,F=2^62lambda and
resource coefficient112940423/50000000. All earlier summary bounds are
interpreted with these exact new parameters and the complete Section 8
coin proof, never with a predecessor's stronger call bound or verdict.
