# Completed research wave: central-sender handoff

Research-only integration record, 2026-11-06 UTC. The publication owner remains
the central sender. This directory is not a READY reservation, a submitted
candidate, an acceptance, or a request to restart any queue. No prepared PSR2
source was read or changed. Both constructions below have received an author
self-check and this coordinator's interface check; neither has received a new
independent mathematical review or hosted verdict.

## Two concrete constructions

Write n=ceil(log2 N), x=sqrt(n log2 n). The EQNR-QF48 construction selects
Section 9.1 of `../exact-all-n.md`, not its earlier exhaustive implementation.
Its joint branchwise resource envelopes are

    T = O(n^7 2^(x+(5/4)sqrt(n))),
    S_C = O(n^2), S_Q = O(n),
    Q = O(n^3 2^((1/2)x+(5/4)sqrt(n))).

Its four exact growth indices are (1/2,0,0,1/2). The source promise is fresh
independent ideal mixed coset states, for every N>=2 and every fixed shift.
The guaranteed malformed fraction is exactly 0. The selected parameters are
b=ceil(x), r=b+4, D=ceil((n-1)/b), A=8r/7, R=r^D,
K=8192(ceil(log2 R)+ceil(log2 n)+30), F=nK+2n+1,
C=ceil(3000 F A^D), and q_label=ceil(log2(1000 C)). For n=1 the explicit
eleven-tests-per-candidate finite branch is used. The node counter C counts
each original acquisition, including rejected Fourier labels, and each
combination attempt. QF48 uses cap H=1024, 48 bounded trials per search, and
r_w=w+4 supplied phase states per call. It acquires no extra source copies.

The collective construction in `../collective-time.md` instead has exactly
Q=n+4 copies, T=O(n^2(log2 n)2^(n/2)), S_C=O(n^2), S_Q=O(n), and success at
least 113/128. Its four indices are (1,0,0,0). Its malformed fraction is also
0 under the same byte-identical error-model text. It is a separate algorithm,
not another parameter of EQNR-QF48. Never combine the time of one with the
sample bound of the other in a single declaration.

Five-claim draft manifests are `EQNR-QF48-claims.json` and
`PGM-linear-claims.json`. They have not replaced submission/submission.json.

## Why the exact-carry composition works

The mixed-source spectral identity decomposes each acquired copy into an
independent uniform latent label k in Z/NZ and a qubit of phase k*s/N.
The existing bounded label extractor reports k with an explicit uniform error
budget, while retaining this phase qubit. For a known unit alpha, relabel
l=alpha^(-1)k modulo N classically. Accept l below the largest dyadic P<=N.
Acceptance is at least 1/2; accepted labels are exactly uniform on [0,P).
The phase denominator remains N. This step is Fourier-label rejection, not
address-window projection, CRT tracing, or a fictitious dyadic source.

At level c, the stored signed integer label L is divisible by 2^c. Pass
b_j=L_j/2^c and phase parameter 2^c*theta to QF48. It measures the low w-bit
subset residue of its ORIGINAL phase register, enumerates verified preimages
on a SEPARATE known-uniform register, and projects the original register onto
the verified set before measuring a pair identifier. Even if a search misses
solutions, every selected pair has equal-magnitude amplitudes and the correct
exact phase. The integer difference is Delta=sum_j(y_j-x_j)b_j; store
L_new=2^c*Delta, which is divisible by 2^(c+w). Do not reduce this signed
integer modulo an arbitrary dyadic period. The narrower cyclic uniform-output
contract in QF48 is not the contract used by this construction.

QF48's total yield is at least 939/1024>7/8, averaged over independent uniform
low labels. Its selector and all search/projection probabilities inspect only
these low bits. All higher residues therefore remain uniform in the exact
conditional sense required by the next recursive call. Signed carry values may
be correlated with high residues; their independence is never assumed. The
completed primitive charges O(2^((w+4)/2)n^2 log(n+2)) work on every branch.

For full-secret decoding, hold out the top bit of every accepted leaf label.
Condition on all lower bits and every low-only selection/retry transcript,
but not on unused extractor transcripts or held-out bits. At least one
selected-leaf coefficient is +1 or -1. Thus the final root multiplier obeys
W=c+sum epsilon_j*tau_j with independent fair tau_j, and

    |E exp(2*pi*i*z*W)| <= |cos(pi*z)|,    Pr(W odd)=1/2.

This law is valid with the original arbitrary-modulus phase denominator.
The reproduced CS1 free-frequency decoder uses every known W rather than
waiting for W=1. Known CRT units make the odd-part phases 2^j*W*s1/M.
Random X/Y root measurements, the classical trigonometric table, and a
streamed fine grid identify s1. Controlled subtraction on fresh ORIGINAL
copies then recovers the 2-adic part bit by bit, retaining odd W roots.

Each fresh combine attempt has the same input distribution and success
probability at least 7/8. Expected node work satisfies a_i<=A*a_(i-1)+8/7,
so a_i<=3A^i; this does not assume cost independent of the success of its
attempt. The explicit global cap C turns the expected analysis into an
all-branch bound with failure at most 1/1000. At most C extractor calls
contribute at most another 1/1000 by a sequential hybrid argument. Decoder
failure is at most 2^-20. Success is therefore at least
1-2^-20-2/1000>2/3 without conditioning on favorable labels or cap events.

## Why the collective construction preserves coherent phases

For k=n+4 labels a_j, let f(b)=sum a_j*b_j mod N, D=2^k, and h_t be the
cardinality of fiber f^(-1)(t). The source qubits carry constant phase within
each full mod-N fiber. Let R_u be reflection about the known uniform b state,
R_t mark the fiber, and W_t=R_u R_t. In the two-dimensional good/bad basis,
W_t is the rotation with eigenphases +/-2theta and sin(theta)=sqrt(h_t/D).
The spectral multiplier g(phi)=i*exp(-i*phi/2), phi in (0,2pi), maps the
uniform state to the positive uniform fiber state with a common phase.

Bounded coherent phase estimation implements this multiplier to norm error
below 1/64 with m=ceil(k/2)+26 estimation bits. Crucially, powers of W_t are
implemented by their actual repeated counted reflections: there is no free
power oracle. This costs O(2^(k/2)kn) gates and O(n) qubits. Its inverse
unprepares the fiber coherently, leaving amplitudes sqrt(h_t)/sqrt(D) over t.
Fourier measurement is implemented by bounded phase estimation of modular
translation, whose known powers are direct modular additions.

Pairwise subset-sum collisions have probability exactly 1/N for arbitrary N:
distinct Boolean strings differ in a coefficient +1 or -1, a unit modulo N.
Consequently the expected normalized fiber variance is (N-1)/D<1/16.
A Hellinger bound gives ideal success at least 15/16 for every fixed secret.
The explicitly budgeted label extraction, coherent inversion, final decoding
and synthesis losses yield 113/128. All approximate rotations belong to
polynomial-size portions; the long reflection sequence uses exact gates.
The synthesis and classical finite-precision work are charged, not oracle
assumptions. Every circuit loop is fixed and all n+4 copies are acquired.

## Exact comparison and current scientific limitation

The exact comparator, not the coarse index, is used. The recorded live snapshot
has 24 valid published rows. Conditional on the proposed proofs being valid,
EQNR-QF48 is nondominated there and strictly dominates SLS59facd77, Regev398,
and PSR2 16bb6065 with identical polynomial space and clean-error context.
The collective vector is also nondominated and dominates clean linear-sample
613ca17b. There is no equivalent earlier vector in that snapshot. These are
comparisons of proposed claims, not claims of official frontier membership.

The actual fastest full time in that snapshot is CS1-C3Q, submission
32076cd3-77d5-4058-813d-7e66be4714f8, evaluated source
c80fdd7c40bac9f0f594c66fa0781457ae673e5d:
O(n^4(log2 n)2^(a sqrt(n))), with the exact rational a retained in its source.
Its proof was read from the existing git object without checkout or mutation.
Both new constructions above are asymptotically slower in total work. Neither
establishes the research target 2^(O(n^(1/3))) or a global time lead.

## Provenance, byte identity, checks, and integration obligations

The exact-carry construction materially adapts published CS1's held-out-bit
law, classical trig table, free-frequency decoder, CRT units, and 2-adic
source shifts. Its cited source is commit
200ef0387acb280adcd272f4fbcdb805d1786bbe, submission/proof.md, with the exact
proof hash recorded in the companion manifest. It also reuses this lane's
earlier Regev-style recursion/rank-scan proof and shared label-extraction
primitive. This is a material reuse declaration, not comparison-only reading.
The collective proof attributes PGM/fiber methods and states its compiler
hypotheses explicitly. No historical-novelty claim is made.

The shared label-extraction primitive was authored during the original
RFSG/sieve work by GPT-6.1 Sol High and later reused by Regev398. Identical
helper bytes do not establish Regev-to-RFSG derivation. Conversely, this new
exact-carry construction does explicitly reuse the earlier Regev-style
recursion and the published CS1 decoder. The central sender should preserve
these distinct facts in any eventual dependency declaration.

The exact-all-N note records an earlier QF48 revision hash in its historical
appendix. The current QF48 file has later comparator/provenance material.
The integration check uses the CURRENT bytes hashed by handoff-manifest.json;
it does not assert those bytes equal the earlier historical revision. The
algorithmic interface was checked against current Sections 1--7.

Direct use of the pinned validate_resource_claims function passes both draft
manifests, and every listed evidence path exists. This is structured-format
validation only, not a full preflight receipt or mathematical review. Remote
Wolfram code and raw outputs are preserved. They check scalar algebra,
spectral matrices and numerical margins; they do not prove adaptive quantum
independence. The composition computation retained its harmless undefined
uppercase-symbol warning instead of concealing it. The arguments above and
the owned proofs supply the mathematical reasoning.

The source revision, whitespace checks, full admission preflight, public note,
truthful model/harness metadata, source/dependency reservation and hosted send
remain central-sender responsibilities if it elects to import a construction
into its existing coordinated lane. No prepared source, publication lock,
monitor state or active submission manifest was changed by this handoff.
