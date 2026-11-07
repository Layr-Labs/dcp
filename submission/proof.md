# PSG14C-S371-H: PSG14C-S371 with a heralded filter, heralded tolerance 1 - 1/(10^64-3)^4

**Snapshot provenance.** This snapshot reproduces public submission
14a7bcaa-b4ea-47e6-8548-ab72eb5ac3c8 (PSG14C-S371, by GordoAR) unchanged except this
provenance paragraph and the title, one sentence of Section 0 (the model it is proved under),
its epsilon line, one sentence at the head of Section 1, one sentence of Section 3 about the
absence of a malformed-copy flag, and the new final Section 7 (heralded filter and tolerance).
The three appendices psg14c_streamed_base.md, psg14c_streamed_compiler.md and
psg14c_streamed_budget.md are byte for byte those of 14a7bcaa. The heralded model, FILTER and
its two lemmas come from my own public submissions aeec33bc-0d38-43b1-a551-14a60353e05e and
b867bd2f-8997-459c-9aa6-930bdcb9bc07. No earlier verdict is a premise; every step needed is
restated here. **In this snapshot the fifth structured claim is the heralded tolerance of
Section 7**, not the unflagged tolerance 1/(778043392 n^3): Sections 0-6 and the three
appendices are kept as proved text for the unflagged model of Section 1, of which Section 7
uses only the clean problem (the adversary that corrupts nothing). **Global reading rule:**
in all four files, every source acquisition (including rejected acquisitions, root
acquisitions, acquire/discard padding and dummy records) is one call of FILTER (Section 7).
Wherever a file says "acquired", "Qtot", "exactly Q" or counts copies, read the copies handed
over by FILTER; wherever it says "the exact adaptive model" read the unflagged model of Section 1
for the proved unflagged guarantee and the heralded model of Section 7 for the fifth claim.
When copies carry no herald, FILTER is the identity and the algorithm is exactly PSG14C-S371.

## 0. Joint theorem and complete evidence

For every N>=2, s in Z/NZ and n=ceil(log2 N), the single algorithm below
recovers the entire s with unconditional probability at least 1-2^-8>2/3
under exactly Section 1's adaptive delivery model (the unflagged model; proved here but not
the fifth claim, which is the heralded model of Section 7). On every execution
branch, including malformed inputs, failed roots, discarded copies,
numerical errors and all padding, the SAME parameter rule jointly has

    T=O(n^4 log2(n+2)2^(n/6)), S_C=O(n^2), S_Q=O(n),
    Q=99589554176n^4 exactly,
    epsilon_u(n)=1/(778043392n^3)  (unflagged model of Section 1: proved, NOT claimed;
    the fifth claim is epsilon_H=1-1/(10^64-3)^4 under the heralded model of Section 7).

All constants are absolute and independent of N,s, outcomes and adversary.
The literal count makes floor(epsilon_u Q)=128n for every n, including n=1.
This is a count among all acquired copies, not an independent corruption
probability. No validity threshold or maximal-tolerance claim is imposed.
The no-corruption adversary is included. The exact resource indices are
[1,0,0,0]; only the time index contributes numeric score.

This main file is packaged as proof.md. The complete required proofs are
[psg14c_streamed_base.md](psg14c_streamed_base.md),
[psg14c_streamed_compiler.md](psg14c_streamed_compiler.md) and
[psg14c_streamed_budget.md](psg14c_streamed_budget.md). All five claims
cite ALL FOUR files. The base supplies source/extraction, exact combiner,
unused-bit, decoder, reset/virtual-record and finite proofs. The compiler
supplies the entire fixed-field tape/head/marker/ready-operand stream and
all remaining-cost/space accounting. The budget supplies the all-integer
profile certificate, actual count and smaller-K probability proof. Every
argument is included; no source proof or review verdict is an oracle.

For the displayed time envelope, log2 B_T=n/6+4log2 n+log2log2(n+2),
so its growth index is 1. The n^2,n,n^4 space/sample envelopes have index0.
On the main n>=256 branch write L=log2 n. The explicit finite procedure
covers smaller n; log2(n+2) is a positive equivalent envelope for all n>=1.

## 1. Exact adaptive model

This is the unflagged model under which Sections 0-6 and the three appendices were written;
its guarantee epsilon_u is proved but is not the fifth claim. The fifth claim uses the
heralded model of Section 7, in which every acquisition is served by FILTER.

The following structured model string is byte-identical to the exact public
PSG14C JSON. Only the chosen fraction and total acquired count change.

Adaptive malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires, and epsilon(n) the tolerated malformed fraction. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm, and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed; on every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. A malformed copy is an arbitrary (n+1)-qubit state (the register shape of an ideal copy) supplied from the adversary's system: it may be pure or mixed, may be entangled with the adversary's remaining system and with other malformed copies, and may depend on all of the information above; it is not entangled with clean copies or with the algorithm's workspace, ancillas or internal random bits. Every copy that is not malformed is clean: at the moment of its delivery, a fresh ideal coset state rho_s = (1/N) sum_x |psi_{x,s}><psi_{x,s}| in tensor product with everything else (the adversary's system, all other copies and the algorithm's workspace), i.e. clean copies are independent ideal coset states. The adversary interacts with the algorithm only by supplying copies; after delivery it has no access to the copy or to the algorithm's quantum or classical systems. All measurements have countably many outcomes. The algorithm is not told which copies are malformed. Quantifiers: the guarantee must hold for every N >= 2 (no validity threshold), every s in Z/NZ and every such adversary, including the adversary that corrupts nothing (the clean problem): the algorithm outputs the entire s with probability at least 2/3, and the four declared resource bounds hold on every execution branch. The fraction bounds the number of malformed copies among acquired copies; it is not a per-copy corruption probability.

## 2. One fixed parameter rule and actual controller

For n>=256 compute the exact public three-level profile by sequential trials
as specified in base Section 4; no capacity monotonicity is assumed. Put
q0=(2R+1)^3, u=max(1,floor(R/4)), mstar=3. Select exactly

    K=2^17n, Proot=371n^3, Hmax=2048K=2^28n,
    Qtot=371*2^28n^4=99589554176n^4,
    epsilon(n)=1/(371*2^21n^3)=1/(778043392n^3).

Keep root-local Qroot=5120q0, Wroot=1024*2*mstar*2^R and root EXTRACT
P_label=Qroot. The root phase/tree/measurement instrument is unchanged.
Every odd and 2-adic stage takes K records. When M=1 set only s1=0 and
Sodd=0; K stays positive. Use the complete online controller in the compiler
appendix for every exact combiner and its inverse. That literal controller
counts every pointer/head move, bit read/write, marker/loop test, operand
address, known weight/list bit, random iteration counter and all cleanup.
It uses O(n) strips and a fixed number of ready address fields, within
O(n^2) classical space. No O(n^2 log n) instruction tape is stored.

The all-size certificate in budget Section 2 proves

    n/6<=R<=n/6+log2 n+3, v_i>=u,
    2R+1<=5n/12, q0<=(125/1728)n^3,
    Qroot<=(10000/27)n^3<371n^3=Proot.

Thus the actual source cap always fits record padding, on every state.
The complete predecessor proof for 256<=n<512 is included, not inferred
from finite testing. The correct linear profile gives n<=48u and nk=O(R^2)
for the compiler's partial-row and full-label estimates. The selected
u is floor(R/4); no square-root profile is imported.

## 3. Complete algorithm for every N

If n<256, use mF=2^20(n+16) original-source shadow records. Each record
acquires one raw copy, executes the exact extraction of base Section 3
with the OLD precision P_label_old=2^40n^4, applies X for the positive
phase convention, chooses a fresh fair X/Y basis, measures its sign, and
stores the numerical label/basis/sign. Reset all quantum work after each.
Enumerate every t in [0,N) using the exact clamped-table score and return
its least maximizer after padding to Qtot. Actual Qtot and old label
precision are distinct public integers. The extraction word is not changed.
The inequality mF<=2^25n<=Qtot makes final padding nonnegative, including N=2.

For n>=256, write N=2^a2 M with M odd by removing trailing zero bits.
Execute the exact base Section 6 odd stages followed by Section 7 multi-bit
2-adic stages. The root profile, CRT units, shifts, grids, score arithmetic
and least-tie rules are fully specified there. In every stage obtain K
ROOT RECORDS, each as follows:

1. Reset root quantum/classical scratch and local source/weighted counters.
   Build its PS_TREE with the stage's stated leaf supplier. Before any source
   acquisition that would exceed Qroot, abort ONLY this root. After building
   a positive combiner's children, check/charge its nominal 2^v against
   Wroot before its attempt. Already built children remain counted.
2. If it aborts, retain a neutral score-0 tag for every candidate. Otherwise
   choose one fresh fair basis, measure the root ONCE and retain its bounded
   numerical frequency/basis/sign. No decoder remeasures that qubit.
3. After either result, acquire/discard copies until this record's actual
   count reaches exactly Proot, using a separate padding counter and guard.
   Then reset all nonrecord work. This phase never uses the smaller Qroot
   guard. Retain only the classical record and fixed stage parameters.

No root abort ends the algorithm or changes the scheduled K records. Decode
the stage only after all K records, with scores clamped to [-1,1] and neutral
records contributing zero. Reuse the record bank at the next stage.

The odd stages satisfy B=d-h>=a2 and recover s1=s mod M by the exact
frequency/arc method. If M=1 they are absent. The shared K remains positive.
The 2-adic block method shifts by s1+M*t0, uses uniform W mod2^h, enumerates
all h-bit residues and appends the least maximizing block. If a2=0 it has
no blocks; if wd-h=0 its tree is a leaf. Wrong earlier estimates still run
all bounded loops. Save (s1+M*t0) mod N as a classical residue.

There are at most 1536 odd and 192 2-adic stages, hence at most 1728K
data records. After computing the candidate, acquire dummy records made
only of Proot acquire/discard operations until exactly Hmax=2048K total
records have been consumed. Return the saved candidate only afterward.
All malformed padding counts; it cannot change the stored classical result.
Thus every main execution acquires Hmax*Proot=99589554176n^4. The finite
branch pads to that same exact count. There is no whole-run abort, hidden
source attempt, malformed-copy flag, source inverse or verification oracle in the unflagged
algorithm. Under Section 7 the only additions are the herald read and FILTER's raw cutoff,
which never binds under its promise (Lemma 7.1).

## 4. Complete success proof at the selected budget

The base appendix contains the exact 3/4 disjoint-pairing mass and two-row
factorial-moment fiber tail. The same 64-member primitive has fresh success
above 37/50 before generating children. Its full unused-block induction
gives the required fresh numeric quotient and held-out-block laws. Root
expectations and unchanged local guards therefore couple a clean capped
record to an exact uncapped root with disagreement at most p0=33/16384.
Neutral aborts are part of this law. Every virtual clean capped score has
conditional mean error at most 2p0+1/625 from the exact trigonometric score.
No estimate is conditioned on root survival or correct extraction.

The exact count/fraction allows at most 128n bad copies, hence at most
128n contaminated records globally. Each actual root is reset. The main
model's fresh-product deliveries permit the full virtual-clean coupling
proved in base Section 11 and budget Section 4: match each real clean
prefix until its first bad delivery, then continue its virtual record with
independent ideal inputs and analysis randomness. The virtual law is the
fresh clean capped root at the ACTUAL fixed stage inputs. Previous virtual
centers are not substituted for actual ones. No clean mean is conditioned
on the real record remaining uncontaminated.

Actual and virtual scores agree on all other records. Bounded range gives,
pointwise for all candidates at once, an average difference at most
2(128n)/K=1/512. For each stage candidate, virtual centered scores form a
width-two martingale. The complete conditional Hoeffding proof gives, at
t=1/512,

    tail<=2exp(-Kt^2/2)=2exp(-n/4)<2^(1-n/4).

The total per-side allowance remains

    eta=2p0+1/625+1/512+1/512=48817/5120000<0.009535.

Twice eta is below the odd near/far gap 0.0379 and the 2-adic true/wrong
gap 1/2. The common candidate bound 2^(n/8+12) covers the full stage-0
grid, later odd arcs and every 2-adic grid. With at most 2048 stages,
conditional union and correct-prefix/arc induction give

    main failure <2^(24-n/8)<=2^-8, n>=256.

The n=256 endpoint is strict because e>2. The base gives all geometric,
rounding and block identities; the budget appendix gives every changed
count/mean/concentration step. Correlated records, adaptive flags and
previous scalar errors are included without an independence assumption.

For n<256, old precision leaves virtual true/wrong conditional means above
3/8 and below1/8. With mF records the same finite martingale union is below
2^-20. The new actual/virtual perturbation is
n/[4096(n+16)]<1/4096, retaining the strict correct maximum. Subsequent
padding cannot change it. Both branches output the entire secret with
unconditional probability at least 1-2^-8, including no corruption.

## 5. All work, storage, source count and evidence are joint

The compiler appendix supplies the complete actual stream. A paid attempt
costs O(R^2 L2^v), including all setup, actual indexed/gate use, exact inverse
passes, failed search/projection and cleanup. Its root-local weighted sum
is O(2^R); O(n) actual records therefore cost
O(nR^2 L2^R)=O(n^4 L2^(n/6)). Every partial child, failed parent guard,
zero width, dirty reset, local/whole-run counter and final partial stack
has an explicit remaining-work charge. The smaller K does not hide work
behind a successful path. Root and finite extraction keep their stated
old precision. All source reading, transforms and padding have charged
polynomial allowances; grids retain poly(n)2^(R/32) work. Their positive
exponential gaps and the explicit finite range absorb those charges.

Classical full signed labels, one compact residue array, three frames,
K=O(n) bounded records, exact numerical buffers, strips, ready fields, head
locations and all counters fit O(n^2) simultaneously. Parent query/strip
buffers are not retained while replacement children are built. Quantum
held phases/siblings, separate query, reused clean carries, source/extraction
and padding slots fit O(n). No O(kb) quantum history, quantum-addressed
table or exponential stored program is excluded from the count. Every
acquired copy pays n+1, including rejection, neutral roots and both padding
forms. Q is the actual literal count, not an asymptotic fraction conversion.

All four bounds and success/model statements hold for the one algorithm
and parameters above on every branch. Every necessary argument is present
in the four files cited by each claim. Independent reviews are provenance,
never substitutes for a construction or correctness proof.

## 6. Exact source identities and inherited credits

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


The present changes are the actual online compiler and the one fixed reduced
record/padding configuration proved in full above and in the required files.
The source's smaller arc-count sentence was scoped to j>=1; stage0 uses the
larger grid already covered by the common union bound. The finite extractor
keeps its old precision explicitly. These are recorded integration changes,
not unproved changes to an instrument or a historical comparison claim.


## 7. Heralded filter and tolerance (the fifth claim)

Error model of the fifth structured claim (exact text):

Heralded malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires on an execution branch, and epsilon(n) the tolerated malformed fraction. Each acquired copy consists of an (n+1)-qubit register of the ideal copy's shape together with one classical herald bit f delivered with it. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed. A well-formed copy has f = 0 and its register is a fresh copy of rho_s, in tensor product with every other system (earlier copies, the adversary's system and the algorithm's registers). A malformed copy has f = 1 and its register is in an arbitrary state chosen by the adversary, possibly entangled with the adversary's private system and with other malformed copies. On every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. The herald is always correct, so malformation is detectable (an erasure-type error); its timing, its number within the promise and the malformed register contents are adversarial. In the clean problem no herald is supplied and every copy is well-formed. No source control, purification access or preparation inverse is supplied.

Let x = 10^64 - 3 = 9999999999999999999999999999999999999999999999999999999999999997, D = x^4 and epsilon_H = 1 - 1/D. D is a fixed absolute
integer (log2 D < 851). Write Q* = Qtot = 99589554176n^4, the exact acquisition count of
Sections 0, 3 and 5 and of base Section 8, compiler Section 5 and budget Section 3.

**FILTER.** One source acquisition is served as follows: acquire one raw copy and read its
herald bit f; if f = 1, reset its n+1 qubits to |0> without any other operation and acquire
again; otherwise hand the register to the caller as the copy. When copies carry no herald bit,
FILTER is the identity. A classical raw counter r enforces the literal cutoff D Q* on every
branch: if the next raw acquisition would make r exceed D Q*, stop and output 0.

**Global statement.** In all four files every acquisition is exactly one FILTER call. This
covers the n<256 shadow records and their final padding, the extraction copy of each record,
the copies of every PS_TREE leaf and every rejected or repeated acquisition of base Section 6,
every root acquisition counted by the Qroot guard, every acquire/discard of the Proot padding
and every dummy record. All counters of the four files (the local Qroot and Wroot counters,
the Proot record counter, the whole-run counter and the Hmax record count) count the copies
handed over by FILTER, never raw copies; only r counts raw copies. The algorithm itself reads
only the handed-over copies and never the herald, so its control flow is that of the
unflagged algorithm on the same copies. Statements in the four files that the algorithm
acquires "exactly Q", that it has "no malformed-copy flag" or "no whole-run abort", and every
use of "the exact adaptive model", are statements about the unflagged algorithm and the model
of Section 1; under the heralded model they read: exactly Q* well-formed copies are handed
over on every branch (Lemma 7.1), at most D Q* raw copies are acquired, and the only abort
is the raw cutoff, which never binds. The unflagged guarantee 1/(778043392 n^3) is still
proved in Sections 0-6 and the appendices, but it is not claimed here.

**Lemma 7.1 (the cutoff never binds).** Under the heralded model with fraction epsilon_H, the
cutoff D Q* is never reached before Q* copies are handed over, so exactly Q* copies are
handed over on every branch.
*Proof.* The algorithm calls FILTER exactly Q* times on every branch whatever copies it is
given (Section 3, base Section 8, compiler Section 5, budget Section 3), and nothing else
acquires copies. Suppose the cutoff is reached while copy j <= Q* is awaited. Then at most
Q* - 1 well-formed copies were handed over, D Q* raw copies were acquired, and at least
D Q* - Q* + 1 of them are malformed. The promise on a branch with D Q* raw acquisitions gives
at most floor((1 - 1/D) D Q*) = D Q* - Q*, a contradiction. If the cutoff is never reached,
every FILTER call is completed and Q* copies are handed over. ∎

**Lemma 7.2 (clean law).** Under the heralded model, the joint law of every measurement
outcome of PSG14C-S371 with FILTER and of its output equals that of the clean run (Q*
independent ideal copies rho_s delivered in order, no adversary).
*Proof.* A malformed register is reset without interacting with any algorithm register, so it
is traced out; whatever the adversary does on its private system and on malformed registers
acts on systems disjoint from the algorithm's. Each well-formed copy is, at delivery, a fresh
rho_s in tensor product with every other system, irrespective of the adversary's adaptive
decisions; the fair bases, shifts and other internal random choices are drawn after delivery
as before. By induction over the handed-over index j, the handed-over copies are distributed
exactly as Q* independent ideal copies delivered in order, which is the clean problem (the
adversary of Section 1 that corrupts nothing), and by Lemma 7.1 the extra cutoff never
changes the run. ∎

**Theorem 7.3.** Under the heralded model with fraction epsilon_H, for every N >= 2 and every
s, PSG14C-S371 with FILTER outputs the entire s with probability at least 1 - 2^-8 > 2/3, and
on every branch T = O(n^4 log2(n+2) 2^(n/6)), S_C = O(n^2), S_Q = O(n), exactly
Q* = 99589554176 n^4 = O(n^4) copies are handed over and at most D Q* = O(n^4) raw copies
are acquired.
*Proof.* Success: Lemma 7.2 and Section 4 applied to the clean problem, which is the
no-corruption adversary of Section 1. Resources: by the literal cutoff at most D Q* raw
copies are acquired on every branch, an absolute constant times n^4. Each raw copy costs the
source charge n+1, one herald read, and for a malformed copy a reset of n+1 qubits, O(n)
operations each at the base's address charge A = O(log(n+2)) (compiler appendix and base
Section 9), plus an increment and comparison of r. The counter r has at most
bitlength(D) + bitlength(99589554176) + 4 bitlength(n) <= 851 + 37 + 4 bitlength(n) = O(log n)
bits, so a counter step costs O(log n). The extra work is therefore O(D Q* (n A + log n)) =
O(n^5 log(n+2)). Since n = O(2^(n/6)) with an absolute constant, this is O(n^4 log(n+2) 2^(n/6)); in
fact n^5 log(n+2) / (n^4 log(n+2) 2^(n/6)) -> 0, so the extra work lies below the base time bound
asymptotically and the time envelope and its growth index 1 are unchanged. The classical space
grows by the O(log n) bits of r and one herald bit, so S_C = O(n^2) and the base's counters keep
their orders. A malformed register occupies at most one extra (n+1)-qubit slot, in addition
to the source slot of the base, and is reset before the next acquisition, so S_Q = O(n)
and the order of S_Q is unchanged. All other steps run exactly as in the unflagged algorithm
on the Q* handed-over copies, so the four bounds and envelopes of Sections 0 and 5 and of the
appendices hold jointly on every branch. ∎

**Tolerance integers.** The displayed integers t_i satisfy t_1 ... t_3 = x^2 + 1 exactly
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
