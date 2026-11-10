# CYCLIC-POLYSPACE: signed subset-sum roots with polynomial classical space

## 1. Configuration, provenance and simultaneous guarantee

For every N>=2 and s in Z/NZ set n=ceil(log2 N). We give ONE fixed algorithm
using only the original independent ideal DCP copies of the challenge. It
recovers the full s with unconditional probability at least 1-2^-8 and has
joint worst-case, every-branch bounds

    T=O(n^30 2^(16sqrt(n log2 n))),
    S_C=O(n^6), S_Q=O(n),
    Q=O(n^20 2^(8sqrt(n log2 n))).

The eventual positive envelopes are evaluated for n>=64 and extended
positively over the finite smaller prefix. Correctness covers all N, all s.
All constants are absolute. Failed, rejected, discarded and cutoff-abandoned
work and original source acquisitions count. The exact growth indices are
1/2,0,0,1/2 in the displayed order. Malformed fraction is zero: no noisy
source guarantee or maximum possible tolerance is claimed.

The subset-sum combiner is materially based on Oded Regev's polynomial-space
algorithm, https://arxiv.org/abs/quant-ph/0406151, Section 3. We do not claim
its discovery. Our detailed construction below supplies its signed-label,
low-prefix root law, original-copy Clifford+T implementation, all-modulus
recovery, explicit caps and paid resource accounting in this challenge.
The full published cyclic-window source e9fc2eca-9d1c-469b-a629-a43e0f7ce928
is supplied unchanged as cyclic_base.md. We use its Sections 1-5 exact source
transforms/collective label extraction, Section 8 characteristic root law
method, Sections 9.1 and 9.2.1-9.2.2 streamed scores/backward decoding, and
Section 10 CRT/power-of-two identity. We REPLACE its TREE and old budgets
entirely. The old exponential classical-memory theorem is not used. All
source identities, exact circuits and numerical score-margin arguments are
supplied, so no prior acceptance verdict or missing quantum oracle is needed.

## 2. Exact parameters, leaves and signed labels

For n<64 run the complete exhaustive finite branch of cyclic_base.md
Section 11: at most N(n+10) original copies, success at least 1-2^-10.
All remaining definitions concern n>=64. Factor N=2^a2 M with M odd by
bit arithmetic; let d=floor(log2 N). Compute exact public integers

    vplus=ceil(log2(n+2)), b0=ceil(sqrt(n*vplus)),
    rmax=b0+4, kmax=ceil((n-1)/b0),
    R=rmax^kmax, ell=ceil(log2 R).

These are finite integer roots, powers, divisions and bit lengths; no real
arithmetic oracle is used. A root of width D in [1,n] starts from independent
one-qubit states (|0>+exp(2pi i a_j xi)|1>)/sqrt2 whose known integer labels
a_j are independent uniform in [0,2^D). Their particular physical supplier
and phase xi are specified in Section 6. Put B=D-1. Partition the B low
positions, starting at zero, into consecutive blocks of size b0 except for
a possibly shorter last block. The number k_D of blocks is ceil(B/b0),
with k_D=0 for D=1. At stage i let p be the number of cleared positions,
b=min(b0,B-p), and r=b+4. A stage-i returned qubit has signed integer label
a divisible by 2^(p+b). Preserve this SIGNED label; never change its sign
based on the remaining high bits. Congruences use exact signed integer sums.

Each leaf uses a fresh original source and its collective latent-label
extractor LE from cyclic_base.md Sections 4-5, with the new confidence of
Section 7. For odd suppliers reject original labels k>=2^d, counting each
rejection, then apply exactly ONE X to the original control. For dyadic
suppliers use Shift_sh, LE, ONE X, and k mod2^D. The X is the original
positive-phase conversion; it is not repeated inside a combiner.

## 3. One combiner, exact gates, and constant average success

Generate r fresh complete stage-(i-1) returned qubits sequentially, recursively
using new disjoint original copies. With labels a_1,...,a_r divisible by 2^p,
their tensor product has equal-magnitude amplitudes with phases
exp(2pi i xi sum_j z_j a_j), z in {0,1}^r. Reversibly compute

    u(z)=sum_j z_j (a_j/2^p) mod2^b

in b scratch bits using the exact adders of the supplied primitive, measure
u and uncompute the sum register. For the observed bucket u enumerate ALL
2^r bitstrings z classically in lexicographic order, computing u(z). Count
m, store its first 32 solutions and stop storing further solutions (continue
counting up to 33; no larger exact count is needed). This is a streaming
exhaustive search, never an exponentially stored list or an advice table.
If m<2 or m>32 discard all r quantum inputs and restart the whole attempt
with fresh children. Otherwise project onto the first two solutions z0,z1
by an equality-to-either flag, measure it, and restart wholly if rejected.

On success the state is a two-term equal superposition. An explicit affine
Clifford permutation maps z0 to zero and z1 to one computational bit: X the
bits of z0, choose a nonzero pivot of z0 xor z1, use that pivot as CNOT
control to clear the other nonzero positions, then swap it to position zero.
All other bits are now zero and can be released. Output the one qubit with
signed label a'=sum_j (z1_j-z0_j)a_j. Its phase is precisely a' xi after
removing a global phase, and a' is divisible by 2^(p+b). Equality flags use
O(r) reversible Boolean gates and scratch; all are exact X/CNOT/Toffoli,
with the supplied constant Clifford+T Toffoli decomposition. No QFT,
rotation-synthesis assumption, QRAM or controlled source is invoked.

Here is the success estimate, averaged over fresh child labels conditional
on earlier external history. Their current b low bits are independent uniform
mod2^b by Section 4. For any fixed u and every NONZERO binary z define
I_z=1_{sum z_j(a_j/2^p)=u mod2^b}. Distinct nonzero binary vectors give a
pair of linear forms with an invertible 2x2 minor over Z/2^bZ: either the
supports are nested and distinct, or each has an exclusive position. Thus
these indicators are pairwise independent, E I_z=2^-b. With
Y=sum_{z!=0} I_z, E Y=16-2^-b in [15.5,16), Var Y<=16.
Chebyshev gives Pr[|Y-EY|>=14]<=16/196. On the complementary event Y is
an integer between 2 and 29, so the full bucket count, adding the possible
zero vector, lies between 2 and 30, in particular between 2 and 32.
Thus each bucket is good with probability at least 1-16/196.

For fixed labels the joint probability of measuring a good bucket and then
passing its two-solution projection is exactly

    sum_good (m/2^r)(2/m)=2*(number of good buckets)/2^r.

Taking expectation gives success at least (1-16/196)/8>1/16. This is not a
claim that every fixed label list has constant success. Whole attempts use
fresh independent child outputs and therefore have this uniform conditional
average bound at every attempt. The law of child computation cost need not
be independent of that attempt's success.

## 4. Uniform unexposed bits and final characteristic law

Inductively, a stage-i output label divided by 2^(p+b) is uniform modulo
2^(D-p-b), independently of the external history before its fresh call.
The base is the independent uniform original labels. At a stage, expose only
children's labels below position p+b, the measured bucket, selected pair and
all retry decisions. These depend solely on those low bits and not the still
unspent high label blocks: bucket outcome probabilities are bucket cardinality
divided by 2^r, and projection probabilities are 2/m, independent of phases.
Given the exposed low history, the child high parts remain independent
uniform. At least one coefficient z1_j-z0_j is +1 or -1; therefore their
signed linear combination is uniform modulo the residual power of two.
Carries from the exposed low parts add only a known integer. This proves the
induction, including fresh whole retries and arbitrary earlier controller
history. Classical labels are stored in full, but every acceptance and pair
selection uses only these specified low positions and lexicographic index.

For the stronger characteristic statement, write every original leaf label
as low_j+2^B tau_j with B=D-1 and independent fair tau_j. Every measurement,
selection, counting flag and retry decision depends only on the low_j.
Selected output labels are signed sums of leaf labels with coefficients in
{-1,0,1}. Child leaf sets are disjoint; two distinct selected bitstrings differ
on a child having a nonempty signed incidence vector. Hence the final signed
incidence vector is nonzero. Conditional on the complete low-only history,

    W=a_final/2^B=c+sum_j epsilon_j tau_j,
    epsilon_j in {-1,0,1}, at least one epsilon_j nonzero.

Consequently for every real z,

    |E exp(2pi i z W)|<=|cos(pi z)|, Pr[W odd]=1/2.

This is exactly the supplied primitive Section 8 law, not merely an assumed
parity marginal. We retain negative W and its signed phase. Negating according
to a high label would spoil the low-only-history argument and is NOT done.
At depth i, |a|<rmax^i 2^D by the triangle inequality; thus final |W|<2R.
For D=1 a single leaf W in {0,1} gives the same law and bound. All statements
hold uniformly for fresh trees after earlier wrong decoder decisions because
those decisions change only source phases or public transforms, not the
uniform latent-label distribution. Extractor errors are coupled later.

## 5. Recursion cost and literal per-root expectation

Each whole attempt at stage i generates at most rmax children. Its success
probability is at least 1/16 after conditional averaging. The reach-event
sum therefore gives C_i<=16rmax C_(i-1) for expected ORIGINAL acquisitions
per returned qubit; base C_0<=2, including every rejected original label.
The bound does not require independence of an attempt's own cost and success.
Thus every returned tree of any requested width costs at most

    Croot=2(16rmax)^kmax

original copies in expectation, uniformly after every external history.
This is a computed integer bound used below. Every internal whole retry
consumes fresh leaves; there are no free retries or rejected uncounted copies.
All recursion is depth first. After source cutoff any unfinished subtree is
abandoned and counted. No resource theorem relies on eventual tree success.

## 6. Complete all-modulus decoder, using only supplied exact score proofs

If M=1 skip the odd part and set s1=0. Otherwise put H=ceil(log2 M), and
use the supplied cyclic_base.md Section 9 physical supplier with D=d,B=d-1:
for any required nonnegative scale j compute the CRT unit

    alpha_j=1 mod2^a2,
    alpha_j=2^j*(2^(d-1-a2))^-1 mod M.

M>=3 implies d-1>=a2. Apply Mult_alpha_j to a fresh original copy, LE,
reject k>=2^d, and apply X. Source acceptance is 2^d/N>1/2. Its latent
label is uniform in [0,2^d), with phase k alpha_j s/N. The new root has
phase W 2^j theta, theta=s1/M, exactly as the supplied Section 9 identity.
This remains true for terminal scales beyond H; no fictitious dyadic source
is assumed for odd moduli. Use the new R and ell from Section 2 throughout.

Set nu=ceil(log2(n+ell+8)), Kseed=32768(ell+nu+40), Kback=512(nu+30).
Perform EXACTLY cyclic_base.md Section 9.2.1's terminal seed at physical
scales H through H+ell+7 with these new parameters, its same dyadic grid,
constant trigonometric table, streamed score updates, least-maximizer tie
rule and explicit finite candidate ranges. It uses

    Fseed=(ell+8)Kseed

fresh new roots. The supplied characteristic/near-point/Azuma/grid-union
proof uses only |W|<2R and the Section 4 law, so it applies unchanged and
returns ||2^H theta-z_H||<=2^(-ell-10)<=1/(1024R) except with probability
at most 2^-20. It includes binary boundaries, zero and circular wraparound.

Use its Section 9.2.2 scored backward mode for ALL odd M: for j=H-1,...,0
score the two exact lifts z/2,(z+1)/2 with Kback fresh new roots at scale j,
using the supplied exact rational table and lexicographic tie rule. There is
no LARGE/alignment branch in this configuration. The Section 9.1 proof
requires only the Section 4 root law and |W|<2R, hence each first wrong
lift has probability at most 2^-30/(n+ell+8); after H<=n steps total is
at most 2^-30. Correct error halves at each step. Round Mz to obtain s1;
its final circular error is <1/(2M), so this returns the whole odd residue.
We charge ALL H Kback calls; the older SMALL-mode O(n) count is not used.

For the power-of-two component use cyclic_base.md Section 10. Maintain low
g bits of s2 with s=s1+M s2 mod N. For remaining width D=a2-g use
sh=s1+M s2low mod N, Shift_sh on each original, LE, ONE X, and
k mod2^D. On a correct history its phase is k rem/2^D. A new width-D root
has phase W rem/2, so an odd W gives the next bit by an X measurement.
Try at most K2=ceil(log2 n)+30 roots at each bit, rejecting even W; if all
are even abort to zero. Width one uses the same one-leaf root. Conditional
odd probability is one half by Section 4 even after arbitrary earlier history.
Total parity cutoff failure is at most 2^-30. Expected roots per requested
bit is at most two, with the same reach argument even when odd parity and
root cost correlate. Return (s1+M s2) mod N. Every branch outputs an integer.

## 7. Literal global cap and unconditional full-secret success

Set odd terms Fseed,H Kback to zero if M=1, and compute

    Qstar=Croot*(Fseed+H Kback+2a2+1),
    Qcap=4096 Qstar.

Before EACH original source acquisition, if it would exceed Qcap, abort to
zero. Every rejected original, failed projection, discarded subtree, even W
and unfinished work consumes the same counter. The label extractor LE uses
confidence ceil(log2(Qcap(n+5)))+20 from the first copy, rather than any old
TREE cap. Its exact test count is 2^21 times this confidence per basis, as
supplied in cyclic_base.md. The same union calculation gives total mismatch
with ideal reference labels at most 2^-18. All precision parameters are fixed
before sampling and computable without knowing s.

In the uncapped ideal process, uniform expectation bounds from Section 5 and
reach probabilities for parity attempts imply expected originals <=Qstar.
No conditioning on correct decoder histories or successful extraction is
used in that estimate. Markov gives extra global-cutoff failure <=2^-12.
Couple the actual extracted-label process to this ideal process up to first
label mismatch as in the supplied primitive. The first-error union of seed
<=2^-20, backward <=2^-30, parity cutoff <=2^-30, global cap <=2^-12 and
label mismatch <=2^-18 is less than 2^-8. This is an unconditional success
bound for every N,s. Actual every-branch resources use the literal cap even
on wrong labels and on aborts, never an expected-successful-run estimate.

## 8. Explicit every-branch bit and qubit accounting

All labels are signed integers of O(D+kmax log rmax)=O(n) bits. Store a
pending child's single qubit and its known label. At most r_i-1 pending
children per active ancestor, plus the current children, are live. Since
sum_i r_i=(D-1)+4k_D=O(n), pending quantum storage is O(n) qubits and
pending known labels consume O(n^2) classical bits. A parent allocates its
subset-sum ancillas ONLY after all its children have returned; only the
current active combiner needs its O(n) scratch. The source transforms,
collective label extractor and exact modular circuits use shared O(n)
quantum scratch, because log Qcap=O(sqrt(n log n))=O(n). Equality flags,
affine compression, reset and disposal preserve this O(n) peak. There is no
simultaneous n-bit sum workspace at every recursive level and no coherent
list of the enumerated 2^r candidates.

Subset enumeration uses an r-bit counter, an O(n)-bit running signed sum,
a count saturated at 33, and at most 32 recorded r-bit solutions. It costs
poly(n)2^r elementary Boolean work per whole attempt and polynomial memory.
All visited internal attempts, including failed and cutoff-abandoned ones,
number at most O((kmax+1)(Qcap+1)): charge a newly begun attempt to a leaf
it eventually consumes or to an active unfinished path. No internal attempt
can complete or retry without generating fresh children. Thus every-branch
tree work is at most poly(n)2^rmax (Qcap+1), including source transforms,
labels, exact gate descriptions, zeroing, comparisons and all failures.

The seed stores only Kseed records of O(ell+n) bits and streams every
candidate. Its supplied O(n^2 R)+poly(n) score update per fresh record and
physical scale has no candidate array. Conservative poly(n)2^(2ell+30)
work covers all seed/backward scoring with polynomial classical storage.
The incoming/output rational centers have O(n+ell) bits. CRT, integer powers,
exact maxima, counters and precision computations use polynomial bit work
and memory. In particular S_C=O(n^6) is a conservative simultaneous bound.
All Boolean address widths are O(log n), since the classical storage is
polynomial; charge them explicitly by a polynomial factor below. Original
acquisition costs n+1 per copy, and all quantum gates, measurements, resets,
releases and circuit generation are included. No source preparation inverse,
purification or powered quantum oracle is provided or assumed.

For transparent eventual envelopes let v=log2 n. For all sufficiently large
n, b0<=2sqrt(nv), log2 rmax<=v, kmax<=sqrt(n/v)+1. Consequently

    log2 Croot <=1+kmax(4+log2 rmax)<=4sqrt(nv),
    ell<=kmax log2 rmax+1<=3sqrt(nv),
    rmax<=3sqrt(nv).

Fseed+H Kback+2a2+1=poly(n), in fact O(n^3), and the literal caps give
Qcap<=poly(n)2^(4sqrt(nv)). The streamed source/circuit work and subset
enumerations have exponent at most 7sqrt(nv); seed work at most 6sqrt(nv)
up to absolute constants and polynomial factors. Choosing the more
conservative displayed envelopes n^20 2^(8sqrt(nv)) for samples and
n^30 2^(16sqrt(nv)) for ALL charged work absorbs those polynomial costs,
addressing and every finite exceptional size. The finite prefix contributes
only absolute outside constants. These explicit coefficients are bounds,
not optimized constants or practical runtime assertions.

The two exponential logarithms are positive constants times
sqrt(n log2 n)+O(log n). Their growth index is exactly 1/2: every larger
power of n dominates them and every smaller one fails. Polynomial n^6 and
n have index zero. All four claims and the clean tolerance are proved for
this ONE configuration with the SAME actual cap, confidence, decoder and
per-branch allocation rules. This trades more time/samples than a
sqrt(n)-exponent classical-table sieve for polynomial classical memory;
no all-axis dominance, time-index-1/3 or global frontier is asserted.
