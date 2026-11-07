# PSG-D4-H: four-level robust isolated records with complete online generation and a heralded filter

**Snapshot provenance.** This snapshot reproduces public submission
75db891b-a4dc-4d63-8c19-dd0af0d9cf04 (PSG-D4, by GordoAR) unchanged except this
provenance paragraph and title, the theorem sentence and bounds list of Section 0
(the epsilon and Q lines), one added paragraph at the end of Section 1, and the new
final Section 7 (heralded filter and tolerance). The other three proof files
are byte-for-byte the originals, and so is the text of Sections 1-6 apart from that one
added paragraph. The heralded model,
FILTER and its two lemmas come from my own public submissions
aeec33bc-0d38-43b1-a551-14a60353e05e and b867bd2f-8997-459c-9aa6-930bdcb9bc07. No
earlier verdict is a premise; every step needed is restated in Section 7.

**Global statement.** Every source acquisition made by PSG-D4, in all four proof
files, is served by FILTER of Section 7: this includes every acquisition of a root
record, of a data record, of the finite branch, and every acquire/discard padding and
dummy-record acquisition, each being exactly one FILTER call. When the copies carry
no herald bit, FILTER is the identity and the algorithm is exactly PSG-D4. Wherever
the four files count Q = 7*2^40 n^5 acquisitions, that count is the number of FILTER
calls, equivalently the number of copies handed over; it is exactly Q on every branch
whatever the registers contain. Wherever they say "Section 1's adaptive model", read
the unflagged model of Section 1 for Sections 1-6 and the three appendix files; those
proofs are unchanged and still prove the unflagged guarantee. **In this snapshot the
fifth structured claim is the heralded tolerance of Section 7**, not the unflagged
epsilon(n) = 1/(60129542144 n^4).

## 0. One joint all-N theorem

For every integer N>=2, secret s in Z/NZ and n=ceil(log2 N), the ONE
algorithm below outputs the entire s with unconditional probability at
least 1-2^-8>2/3 under exactly Section 1's unflagged adaptive model with the
epsilon(n) below (proved here, but not the fifth claim of this snapshot), and also
under the heralded model of Section 7 with epsilon_H=1-1/x^4, x=10^64-3 (the fifth
claim). On every execution branch of either model its simultaneous bounds are

    T=O(n^(9/2)log2(n+2)2^(n/8)), S_C=O(n^2), S_Q=O(n),
    Q=7*2^40n^5=7696581394432n^5 exactly (copies acquired in the clean
    problem, copies handed over by FILTER in the heralded model, where at
    most D Q raw copies are acquired, D=x^4, x=10^64-3, a fixed integer),
    epsilon(n)=1/(7*2^33n^4)=1/(60129542144n^4) (unflagged, Section 1),
    epsilon_H=1-1/x^4 (heralded, Section 7).

All constants are absolute and independent of N,s,the adversary and
outcomes. In the unflagged model the literal count gives
floor(epsilon(n) Q)=128n, including n=1,N=2. It counts all acquired copies, not independent fault probability.
The clean adversary is included. There is no validity threshold.

Every claim cites ALL FOUR required proof files:
[psg_depth_four.md](psg_depth_four.md),
[psg_depth_four_base.md](psg_depth_four_base.md),
[psg_depth_four_compiler.md](psg_depth_four_compiler.md),
[psg_depth_four_family.md](psg_depth_four_family.md).
The base includes the full source/extraction, exact primitive and helper,
root, decoder, virtual-record and finite proofs. The compiler includes
the full online controller and every charged work/space term. The family
includes the complete all-integer profile, expectation, root cap, record
count, adaptive contamination, decoder and fixed-constant proof. All
premises are included. A source verdict or external construction is not
an oracle. The auxiliary family theorem is instantiated ONLY at d=4;
no other depth is a selected algorithm or formal resource claim.

The time representative has log2 equal to
n/8+(9/2)log2 n+log2log2(n+2), so its exact growth index is 1.
The n^2,n,n^5 space/copy envelopes have index 0. log2(n+2) is positive
for the n=1 finite branch and equivalent to log2 n asymptotically.

## 1. Exact adaptive model

Adaptive malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires, and epsilon(n) the tolerated malformed fraction. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm, and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed; on every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. A malformed copy is an arbitrary (n+1)-qubit state (the register shape of an ideal copy) supplied from the adversary's system: it may be pure or mixed, may be entangled with the adversary's remaining system and with other malformed copies, and may depend on all of the information above; it is not entangled with clean copies or with the algorithm's workspace, ancillas or internal random bits. Every copy that is not malformed is clean: at the moment of its delivery, a fresh ideal coset state rho_s = (1/N) sum_x |psi_{x,s}><psi_{x,s}| in tensor product with everything else (the adversary's system, all other copies and the algorithm's workspace), i.e. clean copies are independent ideal coset states. The adversary interacts with the algorithm only by supplying copies; after delivery it has no access to the copy or to the algorithm's quantum or classical systems. All measurements have countably many outcomes. The algorithm is not told which copies are malformed. Quantifiers: the guarantee must hold for every N >= 2 (no validity threshold), every s in Z/NZ and every such adversary, including the adversary that corrupts nothing (the clean problem): the algorithm outputs the entire s with probability at least 2/3, and the four declared resource bounds hold on every execution branch. The fraction bounds the number of malformed copies among acquired copies; it is not a per-copy corruption probability.

The model above is the unflagged model of the original PSG-D4. It and its whole
analysis (Sections 1-6 and the three appendix files) are kept verbatim as proved text.
In this snapshot the fifth structured claim is not this model: it is the heralded model
and tolerance of Section 7. The unflagged guarantee with
epsilon(n)=1/(60129542144 n^4) is still proved but is not claimed.

## 2. One actual four-level rule

The program always fixes d=4, C_4=7 and n_4=2^256. These are constants
of the selected program, not inputs chosen by the adversary or outcomes.
In all implementation estimates, L=log2(n+2).
Select exactly

    d=4, n_4=2^256, C_4=7, q0=(2R+1)^4,
    Qroot=7168q0, Wroot=8192*2^R,
    K=2^17n, Proot=7168n^4, Hmax=8192K=2^30n,
    Qtot=7*2^40n^5=7696581394432n^5 exactly,
    epsilon(n)=1/(7*2^33n^4)=1/(60129542144n^4).

For n>=n_4=2^256, put ell=ceil(log2 n). Scan integer trials starting
at R=ceil(n/8). For each trial compute

    c=ceil(log2(3(2R+1))), v_i=R-(4-i)c, i=1,...,4.

Take the first trial with v_1>=ceil(R/2) and 8R-12c>=n. No capacity
monotonicity is used. The feasible trial
Rtest=ceil(n/8)+ceil(3(ell+2)/2) proves

    n/8<=R<=n/8+(3/2)log2 n+13/2,
    2^R<=2^(13/2)n^(3/2)2^(n/8), R<n/3,
    v_i>=R/2>=u=floor(R/4)>=R/8,
    n<=8R<=64u, 2R+1<=n, q0=(2R+1)^4<=n^4.

All ceilings, positivity and scalar bounds are proved for this entire
range in psg_depth_four_family.md Section 3 with fixed d=4. The search
uses O(log(n+2)) trials and explicit integer arithmetic. For each
1<=D<=n and 0<=B<D, allocate b_i=min(2v_i,remaining) from i=4 down
to 1, then reduce remaining. Capacity makes the final remainder zero.
Set r_i=b_i+1 and p_i=sum_(j<i)b_j. Skip a zero width; B=0 returns
one leaf. Each positive width uses k=b_i+1 children, the exact primitive
below, and its nominal weight 2^v_i. Every returned tree has at most
product_active r_i<=q0 nominal leaves. Its full signed label is 2^B W,
with |W|<2^(D-B)q0 and a nonzero signed incidence on disjoint leaves.
All fields have n+ceil(log2 q0)+4=O(n) bits. High and zero labels are
not filtered. These rules cover every partial and zero-width tree.

The primitive is the exact verified disjoint-pair instrument in base
Section 4, with at most 64 found strings, separate queries, fixed bounded
Grover discovery, original-index pair projection and a full signed output.
On a failed projection discard all children and create fresh ones.
Select the complete ready-address/tape-head/marked-strip controller in
compiler G.2--G.4 for every circuit, inverse and numerical operation.

## 3. Complete algorithm and total output

Compute n, Qtot, the base Section 3 source table and the distinct old finite
label precision P_label_old=2^40n^4. All computations use explicit
bit arithmetic, with indexed work and setup charged.

If n<2^256, make mF=2^20(n+16) one-copy shadow records. For each acquire
one original source copy, run the full EXTRACT(P_label_old), apply X for
the positive control convention, draw one fresh fair X/Y basis, measure
one sign and store label/basis/sign. Reset between records. Scan every
t in [0,N) with exact kt mod N and clamped rational table scores. Save
the least maximizing t. Acquire/discard to exactly Qtot, then return it.
The fit mF<=2^25n<=Qtot includes N=2. This is a literal finite scan,
with a finite maximum loop count; it is not advice or a source oracle.

If n>=2^256, compute the exact four-level profile above and factor
N=2^a M by trailing zeros, without factoring M. Run the complete odd arc
decoder of base Section 6, then the complete multi-bit 2-adic decoder
of Section 7. Their source units, shifts, roots, frequencies, grids,
endpoint rules, clamping, least ties, CRT and final rounding are all
specified and proved there and in family Section 7. Both use
hmax=1+floor(R/32), and every actual stage takes exactly K=2^17n records.
When M=1 set only s1=0,Sodd=0; K remains positive. If a=0 there are no
2-adic stages. A requested zero cancellation returns a leaf.

Each actual ROOT RECORD executes this bounded rule:

1. Reset scratch and local source/weighted counters. Before each source
   acquisition check Qroot. After a positive node's children are built,
   check and charge its 2^v_i against Wroot before parent query/array setup.
   A failed guard ends only this root; executed children remain counted.
2. A root abort stores a neutral score-0 flag. A returned root is measured
   ONCE with one fresh fair X/Y basis. Store its bounded numerical record.
3. Acquire/discard copies until the record's actual count equals Proot.
   Use a separate padding counter, not the smaller Qroot guard. Reset
   every nonrecord register. Keep only classical history and stage data.

All later records/stages run, including after wrong earlier scalars or
numeric labels. The proved fit Qroot<=Proot is state independent. There
are at most 513 odd and 257 2-adic stages, hence at most 770K data
records. Save the final candidate (s1+M*t0) mod N. Fill the total number
of records to Hmax=8192K with Proot-copy acquire/discard dummy records.
Only then return the saved candidate. Thus every main execution has
exactly Hmax*Proot=7*2^40n^5 acquisitions, as does the finite branch.
No whole-run abort, root reuse, second root measurement, odd-W filter,
source inverse or hidden copy is present. Every branch outputs a residue.

## 4. Complete unconditional success proof

The base's character expansion makes clean labels exact uniform latent
variables. Collective controlled translations infer them without an
arbitrary-N QFT, approximate rotation or source inverse. The fixed
EXTRACT precision has per-call error <=1/(2^14 P_label), uniformly in
the latent label; tests, counters and unwrapping are explicit. Main roots
use P_label=Qroot; the finite branch keeps its distinct old precision.

The full parity-support calculation makes complete disjoint-pair lost
mass <=1/4 on average. Two distinct nonzero difference rows have a unit
2-by-2 minor, giving the measured-fiber second factorial moment <2,
hence fiber-size tail <1/1008. Fixed bounded Grover discovery on separate
queries loses <1/1024 on small fibers. Fresh success is therefore >37/50
BEFORE child generation. This is not a claim for a fixed arbitrary list.
The d-level unused-block induction in family Section 6 proves termination,
fresh numeric quotients, independent children and the held-out-block
characteristic bound. No high block or zero label is selected against.

At four levels expected root acquisitions are <=2(50/37)^4q0<7q0.
The actual common gap gives expected total nominal weight <=8*2^R.
Thus Qroot=1024*7q0 and Wroot=1024*8*2^R each have clean reference
cutoff loss <=1/1024. EXTRACT(Qroot) adds <=2^-14. Capped and uncapped
clean root laws couple with disagreement p0=33/16384, including neutral
aborts. A bounded clean capped score therefore has conditional mean
allowance 2p0+1/625 from its ideal trigonometric score. No mean is
conditioned on successful extraction or root survival.

At each record start, reset gives pure zero work even after private
reference entanglement. The model supplies fresh ideal product clean
copies. Condition on all earlier real/virtual history and actual stage
inputs. Match the real and a virtual clean capped prefix up to its first
bad delivery; thereafter complete the virtual record with its ideal
conditional kernel and fresh analysis randomness. Flags are set before
delivery. The full virtual law is the clean capped record law. It is
not conditioned on noncontamination, nor does it replace actual centers
with virtual ones. This is an outcome coupling, not a state copy or
an algorithmic extra source. The full proof includes adaptive decisions
within records and arbitrary conditional private quantum state.

Since floor(epsilon Qtot)=128n, at most 128n records can be contaminated,
even if all bad deliveries occur at one stage. Scores are bounded in
[-1,1]. Simultaneously for all candidates, actual/virtual average error
is <=2(128n)/K=1/512. No independence of real records or faults is used.
For each stage-start-fixed candidate, virtual centered scores have
conditional interval width 2. The complete exponential-moment proof gives
at t=1/512

    tail<=2exp(-Kt^2/2)=2exp(-n/4)<2^(1-n/4).

Together with mean and table errors, each side has allowance

    eta=2p0+1/625+1/512+1/512
       =48817/5120000<0.009535.

Twice eta is below the odd near/far gap 0.0379 and the 2-adic gap 1/2.
The exact odd grid geometry gives the next arc and final circular rounding;
the exact multi-bit uniform character sum gives each true next block.
All candidate-stage pairs number <=2^(n/8) for n>=2^256. Conditional
union and correct-arc/prefix induction give main failure <2^(1-n/8)<=2^-8.
Random later arcs and adaptive flags do not require independent successes.
The full count and geometry proof is included in family Sections 7--8.

The finite scan's ideal means are 1/2 at the secret and zero otherwise.
Old label precision and the table give virtual conditional means >3/8
and <1/8. With mF records, a 1/16 martingale deviation and union over
N<=2^n has probability <2^-20, for every n. Real/virtual error is
<=2(128n)/mF<1/4096. This leaves a strict unique true maximum. Padding
cannot change the stored candidate. The same argument covers the entire
finite range n<2^256, including N=2. Both branches therefore give the
claimed unconditional whole-secret guarantee under exactly Section 1.

## 5. Complete joint resources on every branch

The compiler includes full field layouts, ready addresses, physical carry
head moves and returns, marked loops, known-bit reads, short scans, random
iteration counters, exact gates and inverse streams. A complete m-bit
scan costs O(m+A) raw actions, with A=O(log(n+2)) debited to every actual
bit/head action and indexed gate operand. No free gate generator or
O(n^2 log n) instruction tape is used. With n<=8R<=64u, each complete
paid attempt has O(R^2 log2(n+2)2^v_i) work, including all setup,
failed discovery, projection, signed output and cleanup. The all-state
weighted guard bounds one root by O(R^2 log2(n+2)2^R). O(n) actual
roots and the exact profile give T=O(n^(9/2)log2(n+2)2^(n/8)).

Every source, reset, counter and padding action is charged. A conservative
O(n^2 log2(n+2)^2) allowance per acquired copy gives O(n^7 log2(n+2)^2)
additional work. Recursion/partial-stack work is polynomial(n) per event;
paid attempts number O(n2^(R-u)), u>=n/64. Grids and exact scores use
polynomial(n)2^(R/32) work. Positive exponential gaps absorb these charged
terms. Setup, CRT, table, finite precision and layout are explicit
polynomial computations. The n<2^256 exhaustive scan has a finite
maximum actual loop count, absorbed by an absolute constant. All finite
constants and absorption steps are proved in family Section 10.

Held/current siblings number <=B+1<=n. Original index, separate query,
reused row carries, source/extraction, reset and padding use O(n) qubits.
Full signed labels, one residue DATA array, four metadata frames, K
classical records, streamed grids, numerical arithmetic, strips, ready
fields, head positions and counters fit O(n^2) classical bits together.
Parent query buffers are created after children; no quantum stack,
kb-node history, exponential table or gate list is stored. The same
peaks hold on malformed, failed and wrong-scalar branches. The hard
before-action guards, total encodings and complete templates enforce
all four bounds together. No expected resource is used as a hard limit.

## 6. Exact source use and chronology

This proof first used local depth-two and S371 texts, then the complete
local fixed-depth proof robust_fixed_depth_family.md at SHA-256
51b1791cbdc7e4662773c00d16fe7e28ee8e17be6df06fbd88cb293e57e4b3cb.
The required family appendix reproduces all of its mathematics and source
credits, removes its bounded-task/check reporting, and fixes the actual
selected interface to d=4. The base copies source/extraction, primitive,
unused-block, decoder, coupling and literal-helper text from local
psg_depth_two_base.md, f58e64e83594a4258b40632973ca8e3fb9e042e3290b5441415894d1a961c268.
The compiler copies G.2--G.4 from local psg_depth_two_compiler.md,
ec581df033589d913337deebc4bb2f2bdb57b2b364720999b85ed83c2a0f37ff,
with the proved four-level substitutions. The D2 inputs are local sources;
no public identity for D2 is asserted here. Full original arguments are
included in this package; the source hashes give credit, not missing premises.

The same S371 source was then compared with its saved publication archive:
submission 14a7bcaa-b4ea-47e6-8548-ab72eb5ac3c8, immutable commit
49a5f9826710b4fefe536bd13279b74d41da555d. Its
[main proof](https://github.com/Layr-Labs/dcp/blob/49a5f9826710b4fefe536bd13279b74d41da555d/submission/proof.md),
[base](https://github.com/Layr-Labs/dcp/blob/49a5f9826710b4fefe536bd13279b74d41da555d/submission/psg14c_streamed_base.md),
[compiler](https://github.com/Layr-Labs/dcp/blob/49a5f9826710b4fefe536bd13279b74d41da555d/submission/psg14c_streamed_compiler.md) and
[budget](https://github.com/Layr-Labs/dcp/blob/49a5f9826710b4fefe536bd13279b74d41da555d/submission/psg14c_streamed_budget.md)
have hashes e6d8a9d2910bce77ad26c54ee96b60f703bd5ed1f03c021c6ca2bec642242db2,
bba18b26ef7260f1ec1a1c834baa9f545659bf1e887d8c81df8b5fb263562599,
4ff058eb9aa0f631126cd8443b691aa72d3d1ec7884dec06a5236542f71f79c1 and
b9afa4f8a5a8cfae9defb7a86fc302e5e615b485ad609d7292b6a14c38c4c6f4.
The first three equal the local inputs. The local budget at
2668b8f2c135c52a4911db4766a458f312b24a485e12d06d7cd7b5663b2ab854
has exactly one additional terminal LF. The publication's JSON hash is
689de39623d45132cf2de3f2b88c71f367771a434556d2a7d342aef8d4eb5f66.
This preserves local-first/public-later chronology and does not use a
verdict as a mathematical premise. All new profile/count/time changes
are proved here, not inferred from that source's result.

The following inherited source record is copied from S371. Its direct-read
statements describe that earlier author's work, not new archive reads by
this packager. Original public/local distinctions and upstream credit
are retained. The complete required arguments are in this package.

The direct public material source is PSG14C, submission
`30304a9e-15d5-4b58-9998-d5a4ccc1a67e`, immutable commit
`398d8457f6c25e29a941403e4e75eccb290dda79`. The exact
[proof](https://github.com/Layr-Labs/dcp/blob/398d8457f6c25e29a941403e4e75eccb290dda79/submission/proof.md)
and [claims](https://github.com/Layr-Labs/dcp/blob/398d8457f6c25e29a941403e4e75eccb290dda79/submission/submission.json)
have SHA-256
`2abeb473f0ea10cd5f7305cf58f8696dddd148967337a851183bfc55254ce0b6` and
`626dd5115b1e5bf45f6fac74e659a902708ae1a580918daa1daa9b4b684b53d6`.
Those complete bytes were read and are the semantic source. The actual
local compiler and budget sources are reproduced in their required files:
psg14c_compiler_transfer.md, SHA-256
`0524ec65f682efc625237ad074d71430cfdfdf60d6e80cc1ecb6167b82e61224`,
and psg14c_record_budget.md, SHA-256
`41021054aeed39ebeb552fc13dfce9717245f3c3cedbb9761ee2236c835cdca3`.
The exact literal helper closure is also reused from local
psg13_verified_base.md, SHA-256
`d68deac7104659ab598837f07791e16e077018740ff9cec24962bc6335f95ecd`.
No public identity is invented for a local intermediate. Full generic
compiler/earlier method credits and their exact hashes are retained in
the compiler appendix.

The complete public source credits are retained below as inherited credits.
Claims about which predecessor the original working author consulted are
that source's descriptions; this package does not claim those originals
were newly read. Its immediate correction input was the published PSG14
artifact, submission `720fb0a6-7a00-40c8-bb92-3c0649aa5755`, commit
`51400781cedeb3fc1cdebdfacb697314a75f5286`. Its old K=0 M=1 defect is
historical; the corrected source and this package keep K positive. No
rejected or accepted verdict is a mathematical premise. Private aliases
remain distinct from unrelated public snapshots.

The original working artifact credits PSG13 for the reset/virtual-transcript method and exact
label two-basis finite shadow branch. PSG12 (localce0de50) supplies the
three-level Grover sieve, polynomial-source cap design, compact persistent
implementation and all-modulus stride geometry, inherited from PSG9.
That artifact also credits ROB-G a5c17989-ca3a-49c1-8cea-49d37de89a27, public
1e7300e39bdc1d352dbb895601723712f51d3b62, supplies the EXACT error-model
text and shadow-score/martingale motivation. Its compressed-feature Grover
search and constant33/100 tolerance are not executed or claimed here.

The public CYG1 note70564803-3637-426f-9587-e1333aa07b39 was directly
consulted for its stronger fresh-attempt accounting: parity-support mass
for complete DISJOINT pairing and the two-row factorial-moment fiber tail.
Those two arguments are reproduced in full in4.3, giving37/50 success
for the SAME64-member disjoint-pair primitive. PSG14C does not execute
CYG1's cyclic instrument or use its seven-moment5/6 theorem. That note
credits CYC1 upstream; no direct consultation of a CYC1 archive is claimed.
CYG1 was unpublished when the original working artifact was written; its actual identifier
and unavailable-link status are disclosed without inventing an archive.
The standard coupling/concentration ideas are not claimed as invented here.
No predecessor verdict is a mathematical premise.

Its historical local material sources include PSG7 (commit d772839), for persistent
charged descriptors and its counter/cursor proof, and PSG8 (commit bd374e2),
for compact stage-local rows and separate full-precision pre/postprocessing.
They were unpublished local snapshots when this proof was written; no public
archive identity is invented. The earlier local PSG4 supplies the linear-base
Grover/stride configuration; PSG3 supplies collective label-test rounds;
PSG1 supplies bounded verified discovery and unused-block induction; and
PSW1/PSW2 supply variable-width, weighted-cutoff and truncated-base development.
All needed arguments are reproduced, and prior verdicts are not premises.

That artifact directly consulted the published sources PSR2 submission
16bb6065-c3ca-45fb-b514-86106a310646, archive
7f835a08d1b109847a9b921c02b35361ed350bd0, for signed-label streaming, source
extraction, complete decoding and substantial adapted proof text; SLS
59facd77-4082-40d9-910e-9060c197e72a, archive
643c22bdf74a96b1e08a0eb56f562396c3084adc, for rank/pairing and polynomial-space
accounting context; and CS1 f1481815-9577-4990-abe3-7b79fa5d9284, archive
200ef0387acb280adcd272f4fbcdb805d1786bbe, for exact latent labels, source
transforms, untouched bits and full-modulus decoder material. The final
candidate replaces exhaustive ranking by the explicitly counted search below.

WTS1 submission50a9f13c-eda5-4239-a3c8-28ed83e8ce83, archive
9d8256a16cc1f29c7543af470f03ebc37f8bf0b4, supplies the held-out-block
characteristic lemma, stride rule, essential all-N restriction B>=a2 and
charged enlarged grid. Its vector-table sieve is not executed here.
The collective round was directly informed by the public note and then proof
of844c0fd2-9b1c-4e84-a37c-f402e109985f, archive
7c4b4ed099799e146213c1e3c43a50151482dc6b. That note credits the collective
translation identity in this solver's earlier CS1-C3A public note
05c80793-e172-437e-837c-4c10dd0c4929; its hosted execution failed, so no
mathematical verdict or published source archive is asserted for that entry.

CST-128 submissionf95bb4e2-3d08-4ca0-a34f-99841dca855a, archive
6b7500d549149709fb089338c116904f210b23d1, Section3, was directly consulted
for affine ripple-wire layout, regenerated reverse passes and fully charged
address accounting. Its O(n(log n)^2) test bound is already proved there,
not a new result claimed here. Its sequential shift search is not executed.

Established historical sources include Regev quant-ph/0406151 Section3,
Kuperberg1112.3333 Section4.6, Kitaev quant-ph/9511026, Grover
quant-ph/9605043, and Boyer-Brassard-Hoyer-Tapp quant-ph/9605034v1 Sections3-4.
The needed state, search, precision and circuit arguments are given below.
The inherited historical credit record ends here. No maximal-tolerance,
optimality or historical-invention claim is part of this package.


The inherited ready-address method also has a public counterpart in
submission aa3ec389-f35c-4992-9b6f-e8b37f3359ac, commit
a43e8867eae10e718c329de529d3364a82519f59, compiler
bd2645f64079e2271ecc91859e52edfc748e7efd50013b1d744ff92f5684ece4,
Part A2. S371's publication record reports its exact source comparison.
The method was originally read locally in grover_stride_compiler.md;
its now-public counterpart is an inherited credit, not a new claim that
this task fetched it. PSG-D4 executes the complete controller reproduced
in its own compiler appendix, with its own profile and record counts.
No grouped G1 or stored-program implementation is selected.

## 7. Heralded filter and tolerance

Error model of the fifth structured claim (exact text):

Heralded malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires on an execution branch, and epsilon(n) the tolerated malformed fraction. Each acquired copy consists of an (n+1)-qubit register of the ideal copy's shape together with one classical herald bit f delivered with it. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed. A well-formed copy has f = 0 and its register is a fresh copy of rho_s, in tensor product with every other system (earlier copies, the adversary's system and the algorithm's registers). A malformed copy has f = 1 and its register is in an arbitrary state chosen by the adversary, possibly entangled with the adversary's private system and with other malformed copies. On every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. The herald is always correct, so malformation is detectable (an erasure-type error); its timing, its number within the promise and the malformed register contents are adversarial. In the clean problem no herald is supplied and every copy is well-formed. No source control, purification access or preparation inverse is supplied.

Let x = 10^64 - 3 = 9999999999999999999999999999999999999999999999999999999999999997, D = x^4, epsilon_H = 1 - 1/D, and Q* = 7*2^40 n^5, the
handed-over copy count of Sections 0 and 3. D is a fixed absolute integer
(log2 D < 851). The literal raw cutoff is D*Q*.

**FILTER.** Every acquisition of PSG-D4 (Section 3, the compiler and the family file,
including every acquire/discard padding and dummy record) is served as follows: acquire
one raw copy in the (n+1)-qubit acquisition slot and read its herald bit f; if f = 1,
reset its n+1 qubits to |0> without any other operation and acquire again; otherwise
hand the register to the requesting step as the copy. When copies carry no herald bit,
FILTER is the identity and the algorithm is exactly PSG-D4. A classical raw counter r
enforces the cutoff on every branch: if the next raw acquisition would make r exceed
D*Q*, stop and output 0. All source counters, guards and the Qroot and Proot checks of
Section 3 count handed-over copies, as before; r is separate. The cutoff is the only
stop that is not in the original algorithm. Section 3's statement that there is no
whole-run abort concerns the algorithm; by Lemma 7.1 the cutoff never triggers on a
branch that satisfies the promise.

**Lemma 7.1 (the cutoff never binds).** Under the heralded model with fraction
epsilon_H, on every branch the cutoff D*Q* is never reached before Q* copies are
handed over.
*Proof.* By Section 3 and claim 3 the number of acquisition events is exactly Q* on
every branch whatever the registers contain, and each is one FILTER call. Suppose the
cutoff is reached while copy j <= Q* is awaited. Every handed-over copy has herald 0,
so at most Q* - 1 well-formed copies were handed over, and D*Q* raw copies were
acquired; hence at least D*Q* - Q* + 1 of the raw copies are malformed. The promise
gives at most floor((1 - 1/D) D Q*) = D*Q* - Q*, a contradiction. ∎

**Lemma 7.2 (clean law).** Under the heralded model, the joint law of every measurement
outcome of PSG-D4 with FILTER and of its output equals that of the clean run of PSG-D4
on Q* independent ideal copies.
*Proof.* A malformed register is reset without interacting with any algorithm register,
so it is traced out. Whatever the adversary does on its private system and on malformed
registers acts on systems disjoint from the algorithm's. The adversary may decide
adaptively, from the algorithm's outcomes so far, which raw copies are malformed, but
each handed-over copy has herald 0 and is, at its delivery, a fresh rho_s in tensor
product with every other system, conditional on all earlier history. Every random choice of
the algorithm (fresh fair bases, internal bits) is made after delivery as in the clean
run. By induction over the Q* handed-over copies, the algorithm sees exactly Q*
independent ideal copies delivered in order, and every decision it takes is a function
of them and of its own random bits. This is the clean problem, and by Lemma 7.1 the extra cutoff never
changes the run. ∎

**Theorem 7.3.** Under the heralded model with fraction epsilon_H, for every N >= 2 and
every s, PSG-D4 with FILTER outputs the entire s with probability at least
1 - 2^-8 > 2/3, and on every branch T = O(n^(9/2) log2(n+2) 2^(n/8)), S_C = O(n^2),
S_Q = O(n), the number of copies handed over is exactly Q* = 7*2^40 n^5, and the
number of raw copies acquired is at most D*Q* = O(n^5).
*Proof.* Success: Lemma 7.2 and Section 4 (the finite branch and the main branch)
applied to the clean problem, which is the adversary of Section 1 that corrupts nothing.
Resources: by the literal cutoff at most D*Q* raw copies are acquired on every branch, an
O(n^5) count with the absolute constant 7*2^40*D. Each raw copy costs n+1 for the
acquisition, one herald read, and on a malformed copy a reset of n+1 qubits, so O(n)
operations at the address charge A = O(log(n+2)) of Section 5, plus one increment and
comparison of r. The counter r has bitlength at most 851 + 43 + 5*bitlength(n) =
O(log n), so its step costs O(log(n+2)^2) and does not change the per-copy cost
O(n log(n+2)). The extra work is therefore O(D*Q*n log(n+2)) = O(n^6 log(n+2)). The
claimed time bound exceeds this: the ratio of n^6 log2(n+2) to
n^(9/2) log2(n+2) 2^(n/8) is n^(3/2)/2^(n/8), bounded by an absolute constant (below 17)
for every n >= 1, so for all n >= 2 the extra work is at most an absolute constant times the
bound T of Section 5; the n < 2^256 branch is covered by the same absolute constants.
The classical space grows by the O(log n) bits of r and one herald bit, so S_C = O(n^2).
A malformed register occupies at most one additional (n+1)-qubit slot beyond the
registers already counted in Section 5, and it is reset before the next acquisition, so
S_Q = O(n). All other steps run exactly as in Section 5 on the Q* handed-over copies, so
the four bounds hold jointly on every branch. ∎

**Tolerance integers.** The displayed integers t_i satisfy t_1*...*t_3 = x^2 + 1 exactly
(direct integer multiplication; they need not be prime):

    t_1 = 5909009547859618446014307935656485996455360061473289284034355157
    t_2 = 8461654968574415353741992088106541809421651544931744139485636465
    t_3 = 2

Each of x - 1, x, x + 1 and every t_i has at most 64 decimal digits. The supported expression

    9999999999999999999999999999999999999999999999999999999999999996*9999999999999999999999999999999999999999999999999999999999999998*5909009547859618446014307935656485996455360061473289284034355157*8461654968574415353741992088106541809421651544931744139485636465*2/9999999999999999999999999999999999999999999999999999999999999997^4

equals (x - 1)(x + 1)(x^2 + 1)/x^4 = (x^4 - 1)/x^4 = 1 - 1/x^4 = epsilon_H, a constant in
(0, 1), with normalized numerator and denominator of 256 digits. This guarantee covers
detectable (heralded) malformed copies only; no tolerance of undetectable corruption is
claimed in the fifth claim.
