# PSG22: public-coin robust decoding with a measured basis bank

## A. One physical configuration and exact joint promise

For every N>=2,s in Z/NZ,n=ceil(log2N),L=log2n, the single physical
algorithm PSG22 below, under the EXACT adaptive model reproduced inG,
tolerates fractionepsilon(n)=1/(1073741824 n^3)=1/(2^30n^3) and recovers
the entire s with unconditional probability at least1-2^-8>2/3. Its
simultaneous every-branch bounds are

 T=O(n^12 L^(3/2)2^(n/6)), SC=O(n), SQ=O(n^2L), Q=O(n^4).

ActualQ=2^40n^4 on every branch, including all padding, failures and aborts,
so the allowed malformed count is EXACTLY1024n at every length. These
asymptotic representatives apply for n>=2 and the explicit finite branch
coversn=1. All constants are absolute. Indices are[1,0,0,0], score[1].
The same fixed interpreter, source schedule, guards and public coin timing
support every claim. This is a physical storage tradeoff, not joint
dominance, constant tolerance, optimality or cube-root time. All bank
qubits, metadata, initialization, resetting, scanning, generation, controller
and addressing work are counted. The polynomial time factor is explicitly
larger than the virtual parent bound.

Two actual material inputs are used. The complete corrected PSG14C
artifact30304a9e-15d5-4b58-9998-d5a4ccc1a67e, public
398d8457f6c25e29a941403e4e75eccb290dda79, supplies the full three-level
algorithm and adaptive record analysis. It is reproduced byte-identically
in parent.md. The separately used bank compiler is PSG21 local181569e,
for its measured address-keyed records, storage/cost construction and
stepwise encoding invariant. Its own declared theorem was CLEAN ONLY;
no positive-noise theorem is imported from it. The NEW proof here gives
an explicit public-coin realization and causal transcript/adversary
reduction, followed by the conditional record argument. Both material
sources are declared when published. Historical credits stay carried in
the complete parent artifacts; no provisional path or old verdict is a
mathematical premise and no outside proof component is separately imported.

The virtual program P is the exact corrected configuration in parent.md,
including its positive sharedK in theM=1 branch, finite shadow procedure,
root guards, fixed record padding, grid rules and full signed frequencies.
The new virtual public-coin program G realizes every fair choice as specified
inE. The PHYSICAL program is the bank interpreter ofG described below.
All statements in parent.md about memory/work refer to virtualP; physical
resources and the complete actual observation process are proved here.

## B. The virtual program P and physical representation

Execute the precise corrected PSG14C three-level program in parent.md through
the interpreter below. Every specification and resource assertion in that
file refers to the VIRTUAL parent machine, not PSG22's physical classical
allocation. The full file is included as a proof, not as an accepted-result
oracle. Its source identities, unused-block induction, quantum circuits,
full-modulus decoder and cutoff proof are reproduced there in full.
PSG22's physical resource assertions are exactly SectionsA,C,D here and the adaptive analysis inE-F.

Choose its bit-level implementation as described there: finite uniform
control code; Boolean logic and bit reads/writes; explicit integer loops;
Clifford+T gates and computational measurements; source requests, reset,
allocation/release and fresh classical coins. Multi-bit arithmetic is
expanded into the counted bit operations and addresses specified there.
The instruction stream is generated online, not stored exponentially.
The parent's recursion/call state, loop counters and gate descriptors are
ordinary virtual memory, and are emulated with the rest of its data.

The parent's actual peak virtual classical allocation is S(n)=O(n^2).
Its described arrays, labels, scratch and frames have bit addresses of
O(log(n+2)) bits. Its numerical words have O(n) bits: signed phase labels,
N/residues, source/work counters and precision parameters have these
explicit bounds in Sections3,5,8,9 of parent.md. The trigonometric table
is a fixed finite computation of absolute size. We fix their ordinary
bit-level implementations; a constant number of O(n)-bit staging words
suffices for an instruction, and additional working words and all stack
state are virtual cells rather than physical classical storage.

Represent each LIVE virtual classical bit by a record in a bank of
computational-basis qubits. A record has an active flag, the virtual bit
address, and its value bit. Address words and record flags are included:
each record has O(log(n+2)) qubits. Records for dead cells are marked free
and reused. A doubling-capacity array of records, retained after shrinking,
has capacity at most a fixed factor times the largest live-cell count
so far, plus a fixed constant. Each expansion copies the old records by
measurement into fresh basis qubits, resets/releases the old bank, and
counts both banks during copying. Hence bank peak is O(S(n)log(n+2))
qubits, not a function of the number of cells ever allocated or the
possibly exponential number of interpreter steps. Free records need
only their active flag until reused; resetting and overwriting them is
explicitly counted.

Virtual qubit i is mapped to a separate set of physical wires (for example
using even wire indices), while bank wires use a disjoint set. Current
maximum indices and allocated space are O(n^2 log(n+2)). Computing wire
indices and every addressed operation pays its full address debit.
Source registers may arrive in separate temporary wires and be moved by
counted SWAP gates to the assigned virtual-register wires; this adds
O(n) gates per request and O(n) temporary qubits. It does not request an
extra DCP copy. The source state and gate action are otherwise unchanged.

## C. Explicit access, execution, semantics and storage

All bank addresses are CLASSICAL when accessed. To read virtual addressj,
scan active records using a classical record index, measure the basis
flag and successive basis key bits, and compare withj by Boolean steps.
On the unique match, measure its value qubit in Z into a temporary
classical bit. A write scans in the same way, measures the old value,
and applies X exactly when old and new differ. To create a record, scan
for a free slot or expand capacity, reset its basis qubits by Z followed
by classically controlled X, and write its key and value in the same way.
Release marks matching live records free; range release scans and compares
keys. Empty/unused classical regions may be reserved by virtual allocator
metadata without allocating a physical value until initialized. If an
instruction initializes a whole region at once, perform every record
creation and count it; the work bound below permits even this conservative
implementation. Failed allocations/aborts follow the parent's specified
branch. Every bank measurement, comparison, reset, X, initialization and
address computation is charged.

There is no coherent lookup or extra QRAM oracle. Even a one-bit read may
scan the whole bank. Temporary classical storage consists of the inputN,
the eventual output, a fixed number of O(n)-bit staged operands, requested
addresses, scan counters and the finite interpreter state. It is O(n).
The parent loop/call/return context is represented in bank cells; it is
not an uncounted classical interpreter stack. Multiword operations are
bit loops with their intermediates in bank cells or these fixed staged
words. Parent instruction decoding and generator steps are included.
Quantum measurement outcomes are streamed into bank records, with at
most O(n) outcome bits staged if a whole source-sized register is read.
Fresh coins are generated and recorded as the parent requests them.

Condition on the complete coupled virtual history. The bank is always
EXACTLY a computational-basis encoding of the virtual RAM state. The
original virtual quantum registers have exactly the state prescribed
by P on that history. This holds initially by basis initialization.
A bank read measures a definite bit and changes neither its value nor
the conditioned state of the original quantum registers. A write/reset
or allocation updates exactly the corresponding classical value. A
parent quantum gate, source request, coin or original measurement is
executed identically on the mapped registers and updates the encoding.
Release and discard reproduce the same reduced state. This proves the
invariant inductively for every step, including failed search, rejected
samples, cleanup and abort paths. Equivalently the bank/original-register
state is a classical-quantum mixture over basis encodings, and these
accesses implement ordinary reads of that classical component.

The stepwise invariant applies for any matching source deliveries and original
outcomes. For an adaptive guarantee, extra observations must also be modeled;
SectionsE-F prove that separately, rather than importing a positive-noise
claim from the clean-only compiler source.

Parent instructions to reset/discard all quantum registers act ONLY on
mapped VIRTUAL P source, phase and query registers. The physical bank
represents P classical RAM and survives until that RAM is overwritten or
released. It is not included in a virtual-quantum reset instruction.
Conditional on the public transcript of SectionE, its contents are a
known pure basis encoding, so it leaves no unobserved coherent cross-record
workspace. This distinction preserves the parent record-isolation rule.

Peak physical classical space is O(n) by the staged-controller description.
The bank and its metadata use O(n^2 log(n+2)) qubits; original registers
and any source-moving scratch use O(n) more. Peak during expansion is
at most a constant multiple of this total. For n>=2 it is O(n^2L).
This bounds physical allocations on every branch, including wrong
numerical labels and aborts. No virtual classical label, descriptor,
record, original stack word, address map or stored circuit is excluded:
it either resides in this counted bank or the O(n) staged controller.

## D. Charged time and copies for the SAME simulation

We use a deliberately conservative POLYNOMIAL overhead bound. A scan
examines O(S(n)) records of O(log(n+2)) bits; every elementary read/write,
comparison, gate, measurement and reset also pays O(log(n+2)) for its
physical address. A single original bit operation or fixed-arity gate
can therefore be interpreted in polynomial work. Even a region operation
that creates O(S(n)) records with a whole scan per record costs at most
O(S(n)^2 polylog(n+2)). Array expansion/copying and source-register moves
fit the same bound. The finite code's integer and loop instructions are
already decomposed into parent bit steps; staging/parsing adds polynomial
work. Taking a generous O(n^8) factor per charged parent step bounds all
these costs for n>=2, with an absolute outside constant; initialization,
final readout and finite exceptional cases are included. This is an upper
bound on counted gates and classical steps, not unit-cost memory access.
All parallel work remains sequentially summed.

The virtual public-coin implementation has the same quantum operations,
coin laws and source requests as parentP, with fair choices drawn on use.
Preparing, H-measuring and resetting a coin ancilla costs constant gates
and its full address; a word needsO(n) such operations. This is covered by
the conservative polynomial simulation overhead, withO(n) temporary coin
qubits and outcome bits included in the stated physical bounds.

Section9 of parent.md proves the complete every-branch virtual bound
T_P=O(n^4L^(3/2)2^(n/6)). Multiplying by the explicitly countedO(n^8)
interpreter factor givesT_22=O(n^12L^(3/2)2^(n/6)). No exponent slack is
used to hide that polynomial. The finite parent enumeration and its finite
simulation have the same unconditional guarantee and are covered by an
absolute outside constant. Both virtual guards are emulated exactly; all
physical work outside their nominal counters is included in this separate
time proof. Actual acquired count is exactlyQ=2^40n^4 because every parent
source request is made once, padding included, and no others are made.
Fresh|0> bank/coin ancillas are not DCP copies and their preparation is
charged. ThusQ=O(n^4),SC=O(n),SQ=O(n^2L),T as inA hold jointly on every
branch, also for arbitrary permitted delivered registers.

## E. Public coins and the robust virtual program G

Realize EVERY random choice by fresh|0>,H,Z, obtaining independent fair
bits visible to the adversary as measurement outcomes. No random seed,
future coin string or private random oracle is stored or pre-sampled.
Grover trialj in[0,J0),J0=2^ceil(k/2), uses exactlyceil(k/2) newly measured
bits after that attempt's child inputs and measured residue are present.
They are drawn just before the trial. Each X/Y basis bit is drawn only
AFTER its root has returned, before measuring its phase/sign. In the
finite shadow branch it is drawn after source-label extraction and before
the sign measurement. Ties and all other control choices are deterministic
as in the parent. Padding follows the saved score, as before. Fresh coins
may be observed before later padding or retry deliveries; they are never
assumed secret after being drawn. Source copy promises and the exact
malformed fraction are unchanged.

Here is the robust conditional proof forG under its FULL public history.
At the start of a fresh record, fix that history and its stage parameters.
Future ideal copies are fresh products and futureH coin ancillas are fresh
products. Thus all conditional clean distribution calculations reproduced
in parent.md apply with exactly the same laws: source extraction, disjoint
pair mass, measured-fiber moment, bounded discovery and the joint unused-block
induction establish fresh-attempt probability at least37/50, root-frequency
characteristic bounds and the fair two-adic law. Conditioning is before
fresh generation, not on irrelevant high labels inside the new record.
Publishing an on-use coin does not change its conditional fairness before
its draw. Its information can affect an adversary's later corruption
choice, which the next coupling explicitly permits.

Clean local source/work guards fail with probability at most1/1024 each;
label errors add at most2^-14. Therefore clean capped record discrepancy
p0=33/16384 holds uniformly before each fresh record. Root generation
finishes before the new independent basis coin, so the ideal joint score
law retains the true/wrong and near/far gaps; a fixed earlier disclosed
basis is not substituted for this fresh draw.

Extend the probability space with a fully clean capped virtual record.
Couple its genuine input and fresh-coin transitions toG until the FIRST
malformed delivery into the actual record. Afterwards finish its clean
transitions independently. The first malformed choice is causal: it may
use all previous outcomes and all already drawn coin bits, plus arbitrary
private quantum processing, but cannot observe future clean inputs or
undrawn coin bits. Consequently the virtual record marginal, conditional
on history at record start, is exactly the fresh clean capped law. Never
condition that mean estimate on the actual record remaining uncontaminated.
This argument allows arbitrary adaptive selection within retries and
arbitrary allowed entanglement among malformed copies and private systems.

Each malformed delivery contaminates at most one actual record, including
padding/dummy records. With actualQ=2^40n^4 andfraction1/(2^30n^3), there
are at mostBbad=1024n contaminated records globally. Every bounded candidate
score agrees with its virtual score on an uncontaminated record and differs
by at most2 otherwise. A stage hasK=2^20n, so average perturbation is at
most1/512, SIMULTANEOUSLY for all candidates regardless of how the bad
frequencies or phases were chosen. Virtual-score martingale deviation1/512
has tail2exp(-2n)<=2^(1-2n), conditional on past history. Clean coupling,
table precision, this concentration and contamination give

 eta=2p0+1/625+1/512+1/512=48817/5120000<0.009535.

Twice eta is below the odd near/far gap0.0379 and the2-adic gap1/2. At most
2^(n/8+12) candidates per stage and2048 stages give conditional union bound
2^(24-15n/8)<2^-8 for n>=256. Stage induction and exact CRT recover the
entire secret. For n<256, mF=2^20(n+16) fresh one-copy shadow records with
after-copy fair basis give ideal means1/2 for s and0 for a wrong candidate;
precision preserves means>3/8 and<1/8. The parent deviation1/16 bound,
union overN<=2^n, fails below2^-20, and at most1/512 contamination
perturbation leaves the true maximizer unique. The same exactQ padding
andfraction apply. This proves full-secret success forG for every permitted
adversary even with its coin outcomes public; privacy of past coins was
not used. All needed quantum/distribution/finite proofs are reproduced in
parent.md and all new observation timing is specified here.

## F. Transcript closure and quantum-adversary reduction

GivenN andG's complete public outcome history, ALL its classical RAM bits
and control state are determined. This follows by induction: initialization
is deterministic; all classical operations and ties are deterministic;
every random choice is now an observedH measurement; an unknown quantum
state influences the controller only through an original observed quantum
measurement. The secret is not a private classical input to the controller.
Virtual numerical labels, even incorrect ones, are deterministic functions
of these outcomes. No undisclosed PRNG state or external advice is used.
The deterministic interpreter allocator and its keys/flags/capacity are
likewise functions of this virtual state and its instruction history.

Conditional on this history, the bank is a PURE known computational-basis
encoding of that state. Every extra bank read/key/flag/copy/reset outcome
is therefore deterministically computable from that history at that point.
It supplies no new information about unknown phase registers or the
adversary's private quantum system. In particular bank measurement does
not introduce a new conditional steering of that system: the bank value
was already fixed by the given public history. Bank contents can survive
a virtual root reset because they are just this public classical state;
all nonclassical virtual root/query/source registers are reset as inG.

For any physical-interpreter adversaryA, construct aG adversaryA_G. It
internally runsA, with its entire arbitrary private quantum state. Between
successiveG outcomes/source requests it replays deterministic control and
the bank implementation, generating every intervening bank outcome thatA
would observe and allowingA the same private processing. It forwards each
newG outcome, including its coin outcomes, when obtained. It does not
predict an unknown future outcome. At the corresponding source requestj,
it supplies exactlyA's chosen type and(n+1)-qubit state. Both algorithms
request the same number of copies in the same order. The adversary has no
computational or private-space bound in the model, so generating a possibly
long deterministic bank transcript does not change its admissibility.

Induct on the joint classical outcome history AND private quantum state.
On mapped original registers the quantum instruments are those ofG.
Extra bank outcomes have probability1 conditional on the history and
act on known pure bank states. Thus they leave the conditional joint
state of original registers andA's private system unchanged. Private
operations thatA performs between those observations are the very same
operations run byA_G; they act on the private system and require no access
to the algorithm's registers. Original outcomes are passed unchanged.
Source-register SWAPs are counted local operations of the interpreter.
This establishes equality of joint outcome/output distributions, including
correlations and private quantum states, not only equality for a fixed
classical corruption schedule.

The source promise is preserved. Clean supplied copies remain fresh
rho_s in product with everything; adding/removing a publicly determined
basis bank cannot change that property. Malformed-copy shape and allowed
private-system entanglement are identical. They gain no entanglement with
algorithm workspace through a known basis encoding before delivery.
Bad-copy indices and the exact totalQ match branchwise, so the fractional
budget is identical. The adversary interacts only through source delivery
in either execution. ConsequentlyA_G is one of the adversaries covered
byE. Hence physicalPSG22 also returns the whole secret with probability
at least1-2^-8 for EVERY admissibleA.

## G. Exact model and joint structured guarantees

The model text below is IDENTICAL to the fifth structured object's text.
It includes ALL physical bank and public-coin measurements. No private
observation exception, oblivious placement assumption or different bank
promise is added.

Adaptive malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires, and epsilon(n) the tolerated malformed fraction. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm, and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed; on every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. A malformed copy is an arbitrary (n+1)-qubit state (the register shape of an ideal copy) supplied from the adversary's system: it may be pure or mixed, may be entangled with the adversary's remaining system and with other malformed copies, and may depend on all of the information above; it is not entangled with clean copies or with the algorithm's workspace, ancillas or internal random bits. Every copy that is not malformed is clean: at the moment of its delivery, a fresh ideal coset state rho_s = (1/N) sum_x |psi_{x,s}><psi_{x,s}| in tensor product with everything else (the adversary's system, all other copies and the algorithm's workspace), i.e. clean copies are independent ideal coset states. The adversary interacts with the algorithm only by supplying copies; after delivery it has no access to the copy or to the algorithm's quantum or classical systems. All measurements have countably many outcomes. The algorithm is not told which copies are malformed. Quantifiers: the guarantee must hold for every N >= 2 (no validity threshold), every s in Z/NZ and every such adversary, including the adversary that corrupts nothing (the clean problem): the algorithm outputs the entire s with probability at least 2/3, and the four declared resource bounds hold on every execution branch. The fraction bounds the number of malformed copies among acquired copies; it is not a per-copy corruption probability.

SectionsC-D bound physical resources on every branch of this SAME
interpreter; SectionsE-F prove its full-secret fractional guarantee in
this exact model for allN>=2. The fixed source count makes the allowed
number1024n exactly. The four structured bounds have the fixed common
scope/model/notation and respective growth indices1,0,0,0. Only time
contributes scalar[1]; the fraction has no score. The five statements
are established jointly, not imported from different configurations.
Physicalclassical/quantumspace are counted in this wrapper; the original
virtual memory claims in parent.md are not substituted for them.
