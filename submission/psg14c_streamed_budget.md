# Complete record-budget proof for PSG14C-S371

This required proof file is used jointly with proof.md,
psg14c_streamed_base.md and psg14c_streamed_compiler.md. All five claims
cite all four proofs. The complete local source is psg14c_record_budget.md,
SHA-256 `41021054aeed39ebeb552fc13dfce9717245f3c3cedbb9761ee2236c835cdca3`.
Its complete profile, all-N padding, count, mean, concentration, finite and
resource arguments are reproduced below. Symbols K_new/Proot_new/Qtot_new
are aliases for the ONE actual K/Proot/Qtot in this package; they do not
define a second algorithm. Root/decoder semantic proofs and the complete
actual compiler are included in the other required files.

## 1. Exact source and the selected change

Direct public source: PSG14C, submission
`30304a9e-15d5-4b58-9998-d5a4ccc1a67e`, commit
`398d8457f6c25e29a941403e4e75eccb290dda79`,
[proof](https://github.com/Layr-Labs/dcp/blob/398d8457f6c25e29a941403e4e75eccb290dda79/submission/proof.md)
and [claims](https://github.com/Layr-Labs/dcp/blob/398d8457f6c25e29a941403e4e75eccb290dda79/submission/submission.json).
The exact proof/JSON SHA-256 hashes are respectively
`2abeb473f0ea10cd5f7305cf58f8696dddd148967337a851183bfc55254ce0b6` and
`626dd5115b1e5bf45f6fac74e659a902708ae1a580918daa1daa9b4b684b53d6`.
The actual corrected public snapshot, including positive K when M=1, was
read. No private alias is equated with a public version. All inherited
source credits are preserved in proof.md. In particular,
PSG14C credits CYG1 note `70564803-3637-426f-9587-e1333aa07b39` and its
reported upstream CYC1 for the disjoint-pair probability analysis. Those
original notes were not read for this parameter calculation.

The complete online compiler transfer is fixed in
`psg14c_compiler_transfer.md`, SHA-256
`0524ec65f682efc625237ad074d71430cfdfdf60d6e80cc1ecb6167b82e61224`.
It preserves every exact source instrument and gives the full charged
T=O(n^4 L2^(n/6)), S_C=O(n^2), S_Q=O(n) implementation, using the complete source proof reproduced in this package. The full
controller is reproduced in psg14c_streamed_compiler.md and selected by
proof.md. Its bounds are not inferred from gate count alone. The present change keeps its actual online controller and all
root arithmetic/measurements fixed.

Put n=ceil(log2 N), L=log2 n on n>=2. On the n>=256 main branch select
exactly

    K_new=2^17 n,
    Proot_new=371n^3,
    Hmax_new=2048K_new=2^28 n,
    Qtot_new=371*2^28 n^4=99589554176 n^4,
    epsilon_new(n)=1/(371*2^21 n^3)
                  =1/(778043392 n^3).                   (B1)

Use K_new in EVERY odd and 2-adic stage, even for M=1. Only Sodd is zero
when the odd part is absent. Keep the profile, root supplier, source
transform, exact bounded search, output, table, grids and least-tie rules.
Root-local Qroot=5120q0, Wroot=1024*2*mstar*2^R and main EXTRACT
P_label=Qroot are unchanged. All root aborts are neutral records and end
that root only. Each root pads to Proot_new after returning. Dummy records
fill the total to Hmax_new.

For n<256 keep the original mF=2^20(n+16) one-copy shadow records and its
finite exhaustive score search. Only its final actual acquisition padding
uses Qtot_new. To keep EXTRACT literally unchanged, keep this finite
branch's old numerical precision P_label_old=2^40n^4; do not replace it
by the new actual count. Thus no source-label precision is reduced in
either branch. Old precision and actual acquisition/padding are distinct
public parameters. All these integers have charged finite constructions.

The supported malformed count is exactly

    floor(epsilon_new(n)Qtot_new)=2^7n=128n.              (B2)

The complete semantic proof is in psg14c_streamed_base.md. The conclusion
is success at least 1-2^-8 under its exact unchanged adaptive model,
with no validity threshold and the same time/space envelopes.

## 2. The exact profile bound q0<=(5n/12)^3

For a positive trial R define delta(v)=ceil(log2(3(2v+1))). Retain R and
at most two further positive values obtained by subtracting delta, as in
the actual public source. Let F(R) be twice their sum. The selected R is
the least positive integer with F(R)>=n, found by sequential integer
trials. No monotonicity of F is assumed.

For n>=256, the source profile certificate is direct: the trial
Rtest=ceil(n/6)+ceil(L)+1 is at most n/4. Hence every trial decrement is
at most ceil(L)+1, its third value is positive, and
F(Rtest)>=6Rtest-6(ceil(L)+1)>=n. Therefore

    n/6<=R<=n/6+L+3.                                   (B3)

The selected three values are positive and at least R/4: each decrement
is at most L+5, while 2(L+5)<=n/8<=3R/4 for n>=256. These inequalities
hold at 256 and their differences increase thereafter. Thus mstar=3,
u=floor(R/4), and the same actual compiler profile remains applicable.

If n>=512 then 2L+7<=n/12: it holds at 512 and the difference has positive
derivative 1/12-2/(n ln2). From (B3),

    2R+1<=n/3+2L+7<=5n/12.                             (B4)

It remains to prove (B4) for every integer 256<=n<512. Trial R=96 has
values 96,86,76, with decrements 10,10, and F(96)=516. It is feasible
throughout this interval, so minimality gives R<=96.

For R<=42, F(R)<=6R<=252<256. For 43<=R<=51, the first two decrements
are exactly 9 and 8; all three values are positive and
F(R)=6R-52<=254. Hence the selected R satisfies 52<=R<=96.
The following cases close the interval without a capacity monotonicity claim.

- If R=52, then 12(2R+1)=1260<=5*256<=5n.
- If 53<=R<=56, the predecessor R-1 has decrements 9,9 and three positive
  values. Thus F(R-1)=6R-60. Minimality and integer n give
  n>=F(R-1)+1=6R-59. Therefore
  5n-12(2R+1)>=6R-307>0.
- If 57<=R<=96, both predecessor decrements are at most 10 and all three
  predecessor values are positive. Hence F(R-1)>=6R-66, and minimality
  gives n>=6R-65. Then 5n-12(2R+1)>=6R-337>0 because 6R>=342.

This proves (B4) in every main-branch length. Taking cubes gives

    q0=(2R+1)^3<=(125/1728)n^3,
    Qroot=5120q0<=(10000/27)n^3<371n^3=Proot_new.       (B5)

The source cap and new padding are exact integers. Equation (B5) is a
parameter identity/inequality, independent of input states or outcomes.
Thus every root can pad its actual count to Proot_new on every branch,
including arbitrary malformed inputs and local aborts.

## 3. Exact records, root guards, dummy padding and all-N count

Keep the actual source/weighted guards before their actions. Qroot bounds
all root acquisitions, including rejected labels and failed/partial trees.
Before a paid positive combiner attempt, after building its children,
check/charge its weight against Wroot; overflow aborts only the root.
The unchanged bounded output/cleanup routines produce a neutral record
on any root abort, followed by padding with its separate Proot_new counter.
There is no whole-run abort and no retry after deciding to pad a record.
The guard Qroot is never applied to the padding phase.

Keep all fixed stage counts. The odd-part stage bound is at most 1536:
for h<hmax it is at most 8; for h=hmax,R>=256 it is at most
64n/R+1<=385; for R<256, n<=6R<1536 and Sodd<=n.
The 2-adic number of blocks is ceil(a2/hmax)<=192 because
hmax=1+floor(R/32)>R/32 and n<=6R. Wrong scalar answers change no
block width or stage count. All actual stages use exactly K_new records.
Hence actual records are at most 1728K_new<2048K_new=Hmax_new.

After computing the candidate, acquire exactly Hmax_new minus actual-record
count dummy records, each made of Proot_new acquire/discard operations.
The saved candidate is returned only afterward. Every padding copy is real
and charged; contaminated dummy records can be counted conservatively.
The total actual main-branch acquisition count is therefore exactly

    Hmax_new*Proot_new
      =2048*2^17*n*371*n^3
      =371*2^28*n^4=99589554176*n^4.                    (B6)

This includes the pure-power-of-two case: M=1 sets Sodd=0 only, and K_new
stays positive for its 2-adic records and dummy count. When a2=0 there are
no 2-adic blocks. A wd-h=0 tree is just a leaf and still has the same local
source guard, record measurement and padding. No odd-W postselection is
introduced by the multi-bit decoder.

For n<256 the finite branch makes the unchanged mF numerical records, then
pads directly to Qtot_new. For every n>=1,

    mF=2^20(n+16)<=17*2^20n<=2^25n<=Qtot_new.

The final padding count is nonnegative, so (B6) holds in this branch also,
including n=1,N=2. The finite EXTRACT precision remains P_label_old, while
the actual count is Qtot_new. No fractional count is inferred from big-O.
Multiplying the literal count in (B6) by the fraction in (B1) proves (B2)
on every actual path.

## 4. Clean local means and adaptive contamination stay valid

This section uses the full clean-root/held-out-block/score proofs reproduced
in psg14c_streamed_base.md. Their scope is unchanged; no external audit or
source oracle is a mathematical premise. The new compiler changes public generation only, and the
root guards, profile and measurement instrument are unchanged here.

The same fresh disjoint-pair primitive has conditional success at least
37/50 before its fresh children are generated. Its conditional geometric
cost sum bounds clean root acquisitions by 2(50/37)^3q0<5q0. Its expected
weighted work is at most 2*mstar*2^R. Thus Qroot and Wroot each have old
clean cutoff loss at most 1/1024. EXTRACT still uses P_label=Qroot and
has total local numerical-label error at most 2^-14. The same clean root
coupling to an exact uncapped root therefore has disagreement at most

    p0=2/1024+1/16384=33/16384.                          (B7)

A neutral abort has score 0; all other table/sign scores are clamped to
[-1,1]. Thus the virtual clean capped record's conditional mean differs
from its ideal trigonometric score by at most 2p0+1/625, uniformly over
candidates and prior history. This is a local mean bound, not a claim that
every actual or virtual root succeeds. The table and precision are fixed.

The exact adaptive model makes each clean delivery a fresh ideal product
with all other systems. Measurement/conditional-flip reset makes new work
pure zero even with old bad/reference entanglement. At the start of a
record condition on earlier real/virtual classical history and an arbitrary
conditional private quantum state. Share the ideal and real prefix until
its first malformed acquisition, then complete the virtual clean record by
its ideal conditional kernel and fresh analysis randomness. A flag is chosen
before its delivery. Summing adaptive stopping times does not select ideal
transcripts or condition on actual noncontamination. The full virtual marginal
is the fresh clean capped record law at that fixed stage input.

Each malformed copy contaminates at most one record, including padding or
dummies. The global count (B2) gives Bbad=128n. Actual and virtual records
match on every uncontaminated record. For any stage, simultaneously for ALL
candidate scores, bounded range gives the deterministic average perturbation

    2Bbad/K_new=2*128n/(2^17n)=1/512.                    (B8)

No independence of flags, records or adversary is assumed, and no clean-law
bound is conditioned on a record remaining clean. All earlier scalar or
numerical failures are included as histories. Correct phase/geometry identities
are used for correctness only after the preceding stage estimates were correct;
every-state loop/guard resource safety is independent of that event.

## 5. The smaller K still supplies the complete main success bound

For one candidate at a fixed stage start, let virtual scores X_i be in
[-1,1] with conditional means m_i. Centered increments have interval width
two. Convexity, or the tilted log-moment variance bound, gives

    E[exp(lambda(X_i-m_i)) | past]<=exp(lambda^2/2).

Iterating the conditional bound and optimizing lambda for either sign gives

    Pr[|sum_i(X_i-m_i)|>=K_new*t]
      <=2exp(-K_new*t^2/2).

With t=1/512 and K_new=2^17n, the new tail is

    2exp(-n/4)<2^(1-n/4).                               (B9)

The strict inequality uses e>2 and n>0. All old score-error terms at this
same threshold remain unchanged:

    eta=2p0+1/625+1/512+1/512<0.009535.

The terms are root coupling, table precision, virtual concentration and
actual/virtual contamination. Twice eta is below 0.01907, while the exact
odd near/far gap exceeds 0.0379; the multi-bit 2-adic true/wrong gap is 1/2.
Thus every stage still selects within the required next arc or selects
the exact correct 2-adic residue on the corresponding concentration event.

There are at most 2^(n/8+12) stage candidates. For the odd grid this uses
h-1<=n/32, log2q0<=3L and n/32+3L<=n/8 for n>=256, plus its fixed
ceiling/count allowance. For the 2-adic grid, 2^h<=2^(1+n/32) is smaller.
These bounds include all relevant near/far signs through the two-sided
factor already in (B9). Candidate sets are fixed conditional on the stage
start; later random arcs are handled by conditioning and induction.

Union bound at most 2048 stages and all their candidates using (B9):

    failure <2^11 *2^(n/8+12)*2^(1-n/4)
             =2^(24-n/8)<=2^-8                         (B10)

for every n>=256. In particular the endpoint n=256 is strict from (B9).
No increase in n, threshold or uncounted restart is used. The old odd
rounding/arc induction and the multi-bit prefix induction then return the
entire secret. No independence between successive good-stage events is
needed; the bounds hold conditional on the earlier successful prefixes.

## 6. The finite branch remains correct at the new global budget

For n<256 the exact latent-label trigonometric score has mean 1/2 for
t=s and 0 for every other t, by the uniform character sum. The fresh ideal
EXTRACT call keeps its old precision P_label_old=2^40n^4. Its local error
is at most 1/(2^14P_label_old), so a bounded score's mean changes by at most
2/(2^14P_label_old)<=2^-13. Table error remains below 1/625. Consequently
every virtual conditional true mean is above 3/8 and every wrong mean
is below 1/8, exactly as in the public finite proof.

The new adaptive budget can contaminate at most 128n one-copy records.
With the unchanged mF=2^20(n+16), its deterministic perturbation is

    2Bbad/mF = n/[4096(n+16)]<1/4096<1/512.              (B11)

Later padding faults cannot change the saved candidate. The same reset
virtual coupling and conditional Hoeffding bound with t=1/16 give, after
union over N<=2^n candidates,

    failure<=2^(n+1)exp(-mF/512)
            <=2^(n+1-2048(n+16))<2^-20.                (B12)

On its complement virtual average scores are at least 5/16 for the true
secret and at most 3/16 for every wrong one. The smaller perturbation
(B11) keeps a strict unique maximizing true secret. The finite procedure
and its positive error bound include every N=2 case, with no validity
threshold. Its exact Qtot_new count follows from Section 3, while its
source-label precision was kept literally unchanged.

## 7. Outputs, complete resources and exact model

Neutral root aborts do not abort the main algorithm or provide an output
phase to measure twice. Success records keep their same frequency/basis/
sign interface. Wrong records have bounded numerical encodings. Odd outputs
are reduced modulo M or set to 0; 2-adic least maximizers are h-bit residues,
and final output is (s1+M*t0) mod N. Finite maximization is over [0,N).
Thus all branches return a measured classical residue with the same output
interface, even after wrong earlier scalar/numerical outcomes.

The actual complete online compiler is reproduced in
psg14c_streamed_compiler.md. Its root-local Qroot/Wroot limits are fixed. A complete attempt costs O(n^2 L2^v),
one root has total weight O(2^R), and there are O(n) actual records with
K_new. Hence total combiner work is O(n^3 L2^R)=O(n^4 L2^(n/6)). The
unchanged full source extraction, transforms and precision cost at most
the old polynomial charge. Root/dummy padding and all source reading,
resets, counters and initialized slots cost O(n^5 log(n+2)); grids retain
their polynomial(n)2^(R/32) charge. The positive exponential gaps and the
explicit finite branch absorb these terms. No setup, failed record,
partial tree, last abort or inverse pass is free.

The smaller K retains O(n) records of O(n) bits, one active O(n^2) low-label
array, fixed-depth frames and reusable exact arithmetic. Online strips and
ready operands are included, so S_C=O(n^2). Held phases/query/source/carry
scratch still use O(n) qubits, including sequential padding and reset.
Counter/profile/new-n^4 setup is charged polynomial bit work in the same
store. All four bounds hold jointly on every branch. Changing K and Proot
introduces no quantum operation, extra root reuse or unknown-angle gate.

The exact error model is the byte-identical public JSON string below.
Only epsilon's expression and the fixed acquired count change. In particular,
clean-product delivery, arbitrary private quantum history, pre-delivery
adaptive flags, countable outcomes, forbidden workspace entanglement and
no post-delivery access retain their exact meanings.

Adaptive malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires, and epsilon(n) the tolerated malformed fraction. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm, and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed; on every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. A malformed copy is an arbitrary (n+1)-qubit state (the register shape of an ideal copy) supplied from the adversary's system: it may be pure or mixed, may be entangled with the adversary's remaining system and with other malformed copies, and may depend on all of the information above; it is not entangled with clean copies or with the algorithm's workspace, ancillas or internal random bits. Every copy that is not malformed is clean: at the moment of its delivery, a fresh ideal coset state rho_s = (1/N) sum_x |psi_{x,s}><psi_{x,s}| in tensor product with everything else (the adversary's system, all other copies and the algorithm's workspace), i.e. clean copies are independent ideal coset states. The adversary interacts with the algorithm only by supplying copies; after delivery it has no access to the copy or to the algorithm's quantum or classical systems. All measurements have countably many outcomes. The algorithm is not told which copies are malformed. Quantifiers: the guarantee must hold for every N >= 2 (no validity threshold), every s in Z/NZ and every such adversary, including the adversary that corrupts nothing (the clean problem): the algorithm outputs the entire s with probability at least 2/3, and the four declared resource bounds hold on every execution branch. The fraction bounds the number of malformed copies among acquired copies; it is not a per-copy corruption probability.

By the complete semantic proofs in psg14c_streamed_base.md and the
complete selected controller in psg14c_streamed_compiler.md, the ONE selected configuration jointly supports every N>=2,
every s and every allowed adversary, including no corruption:

    T=O(n^4 L2^(n/6)), S_C=O(n^2), S_Q=O(n),
    Q=99589554176n^4 exactly,
    epsilon(n)=1/(778043392n^3),
    full-secret success>=1-2^-8.                       (B13)

Use L=log2 n for n>=2, with the specified n=1 finite branch; log2(n+2)
gives an equivalent positive whole-domain time envelope. Resource growth
indices remain [1,0,0,0]. This is the one supported parameter point used by the main proof and all
four required proof files. No maximal-tolerance claim is made.
