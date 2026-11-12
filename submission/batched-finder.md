# A counted-gate batched finder for a measured subset-sum fiber

## 1. Purpose, model and direct conceptual sources

This file proves the helper used by BJ3-C in proof.md. It does NOT import
an efficient quantum memory lookup, quantum walk or claw-finding oracle.
All gates, Boolean operations, addresses, generation and allocated cells
are counted. Only exact Clifford+T operations, fresh zero qubits and
computational-basis measurement are used. The original phase-index register
is held untouched while all discovery queries run on separate registers.

A conceptual source is Chukhin, Kulikov, Levitskii and Mihajlin,
*Improved Quantum Algorithms for Subset Sum and k-SUM*,
arXiv:2608.07309v1 (7 August 2026), Sections 3.1-3.3:
https://arxiv.org/html/2608.07309v1 . Their four-block filtering and canonical
representative ideas motivate this decomposition. Their QRAQM assumption
(Section 2.3), quantum walk, inner claw routine and quoted running-time
exponent are NOT used. The following bounded sampler, fixed classical
subsets, complete sorting-network predicates and all required arguments
are supplied here in the counted-gate model.

The measured-basis-record implementation and CQ reasoning are adapted
from own published QLOG-BANK f949830e-3dd9-4a7e-af4e-4aabedbfb672,
whose complete published physical proof has SHA-256
cd1f8f1af807ce35a8f2994666627eb63aca4dd03c2db645dee3dac7a60cbb8b.
Only its READ/WRITE/CQ method is used. Its old seven-region polynomial
layout, old sieve profile and numerical resource theorem are not executed.

Fix the original input bit length n and a positive width 1<=b<=n.
Put k=b+6 and C=4096, D=C+1. Inputs to a discovery call are classical
weights c_1,...,c_k in [0,2^b), measured residue e in [0,2^b), and a
classical list E of at most C already found DISTINCT k-bit strings.
The task is to find a NEW y outside E with sum_i c_i y_i=e (mod 2^b).
This is a fully counted algorithm, not an additional input oracle.

Let M=2^ceil(k/4). One complete bounded finder trial has worst-case
work M^(3/2)poly(n), qubits M poly(n), and O(n^2) ordinary classical bits.
If any new witness exists, the trial finds one with probability >=1/32.
It never returns an incorrect or repeated witness. Constants and polynomial
degrees are fixed, independent of the instance and sampled outcomes.
Sections 2-8 establish each part, including memory access and cleanup.

## 2. Four disjoint blocks and exact integer targets

Partition the k positions into FOUR groups by their index modulo 4.
Each group has at most ceil(k/4) bits and is one block. The blocks are
disjoint and cover all positions. Each block domain has at most M assignments.
This balanced partition optimizes the largest explicit batch in this
counted-gate implementation; it is not the source paper's QRAQM partition.
For an assignment alpha in block i, let Sigma_i(alpha) be its exact
NONNEGATIVE integer weighted sum and let its tuple identifier be the
corresponding k-bit mask, zero outside that block. All sums have O(n) bits.

Choose subsets S_2,S_4 independently by including each assignment in the
corresponding block with an independent fair coin. Enumerate their whole
domains and store the selected tuples and exact sums. Their sizes are at
most M. A fixed full witness survives these choices with probability 1/4.
The large arrays are counted basis-qubit records, not ordinary classical
storage; Section 8 gives explicit access and work rules.

The modular condition is equivalent to an exact equality for some
integer target T=e+t2^b with t in {0,...,k}. Values outside the true sum
range simply have no witnesses. For a chosen t, SHIFT EVERY block-1 sum
by -T, writing A_1(alpha)=Sigma_1(alpha)-T. Thus the target equation is

 A_1(alpha_1)+Sigma_2(alpha_2)+Sigma_3(alpha_3)+Sigma_4(alpha_4)=0. (2.1)

This target shift is essential: the right residue query below is -q
only in this ZERO-TARGET form. No unshifted-target shortcut is assumed.

## 3. A finite uniform prime sampler with an elementary certificate

Set X=2^20 M(n+1)^4, an explicit composite even integer >=16, and
ell=ceil(log2 X). Each candidate is chosen uniformly from [0,2^ell)
using measured Hadamard coins. Reject values outside [2,X]. Test each
remaining candidate by exact trial division through floor(sqrt z), and
accept at its first certified prime. Make AT MOST 1024 ell candidate
trials; return FAIL if none is accepted. All counters, trial division,
comparisons and address operations are finite counted bit computations.
No table of primes, primality oracle or unbounded loop is present.

Every prime <=X lies in the candidate range: when X is a power of two,
X itself is composite. Conditional on finding a prime, its value is
exactly uniform among ALL primes <=X, since each candidate assigns the
same probability to every such prime. By (3.1) below, a candidate is
accepted with probability >=pi(X)/(2X)>=1/(4log2 X)>=1/(4ell).
Thus the literal candidate cap has failure at most

 (1-1/(4ell))^(1024ell)<=exp(-256)<2^-256.

The complete bounded sampler costs at most O(ell sqrt(X)) polynomial-bit
trial-division work, using only a fixed number of O(n)-bit staged words.
Its asymptotic time is sqrt(M)poly(n); its ordinary classical scratch is
O(n^2) or less. It never allocates an X-entry prime array. The theoretical
symbol pi(X) used in the proof is not a quantity the algorithm must know.

Here is the required prime-count bound, without PNT or interval assumptions.
For an even integer X=2m>=16,

 binom(2m,m)>=2^(2m)/(2m+1).

Legendre's formula writes the exponent of a prime p in this binomial as
sum_j[floor(2m/p^j)-2floor(m/p^j)]. Each summand is 0 or 1, and only
powers p^j<=2m contribute. Thus p to this exponent is <=2m=X.
Multiplying over all primes <=X gives binom(2m,m)<=X^pi(X). Hence

 pi(X)>=(X-log2(X+1))/log2 X >= X/(2log2 X).          (3.1)

The last inequality follows from 2^(X/2)>=X+1 for even X>=16; this
holds at 16 and is preserved when X increases by 2.

Fix a full witness whose block-2 and block-4 tuples survived. Call a
prime bad for that witness if some selected tuple in either block has a
DIFFERENT exact sum from the witness's sum but the same residue modulo p.
There are at most 2M such nonzero differences. Each has magnitude
<k2^b, and at most log2(k2^b)<=4(n+1) distinct prime divisors.
Thus at most 8M(n+1) primes are bad. Using (3.1), their fraction is

 <=16M(n+1)log2 X/X <=1/[4096(n+1)^2] <1/4096.       (3.2)

For the displayed uniform bound, k<=n+6 gives log2 M<=2(n+1), and
log2 X=20+log2 M+4log2(n+1)<=16(n+1).
Equal exact sums are harmless and are explicitly NOT counted as bad.
These bounds hold conditional on any fixed selected subsets containing
the witness; the prime draw is independent of those subsets.

## 4. Canonical dictionaries and preserving nonexcluded witnesses

For the sampled p, group S_2 and S_4 by their sum residue. In each bucket
retain the first D DISTINCT tuple records in order of (exact sum,tuple),
or every record if fewer. The groups and canonical headers are computed
classically using counted basis-record operations and stored in padded
arrays of O(M) records with O(Dn) bits each. There is no dense array of p
quantum-addressed buckets. A missing bucket means an empty list.

For a proposed pair (t,q), 0<=t<=k and 0<=q<p, query block 2 at
(q-A_1(alpha_1)) mod p for EVERY block-1 assignment, and block 4 at
(-q-Sigma_3(alpha_3)) mod p for EVERY block-3 assignment. For every returned
representative form the left or right record

 F=A_1(alpha_1)+Sigma_2(alpha_2), with tuple (alpha_1,alpha_2),
 G=-Sigma_3(alpha_3)-Sigma_4(alpha_4), with tuple (alpha_3,alpha_4).

Every equality F=G is an exact full solution of (2.1), not only a modular
collision. Test its full k-bit mask against E before marking it.

Suppose a new witness survives and p is good for it. Choose its true
integer target t and q=(A_1(alpha_1)+Sigma_2(alpha_2)) mod p. Both queried
target buckets contain only the respective witness exact sums. Therefore
ANY combination of their retained tuples with the fixed outer tuples
satisfies (2.1). If the product of retained list sizes exceeds C, not all
these distinct full strings can lie in E. If the product is at most C,
neither original bucket was truncated (a truncated bucket retains C+1
entries), so the original new witness is retained. In either case there
is a nonexcluded solution among the constructed F/G records.

There are O(DM) F/G records. To check all equalities without a quadratic
scan through large duplicate buckets, sort records by (exact value,type,
tuple), with LEFT before RIGHT within a value. Retain only the first
D distinct left tuple-pairs at that value and compare EACH right tuple
against those D entries and against E. This is exact: if there are more
than C left entries, every fixed right entry has >C distinct full strings,
so one is outside E. If there are <=C left entries, all are retained.
All left partial tuples are distinct by construction, even when sums
are duplicated. The bounded buffer and E have fixed absolute sizes;
no enumeration of all pairs in a large equal-value bucket occurs.

## 5. The coherent predicate is a fixed-address sorting circuit

Here is an explicit implementation of all lookups and equalities in
Section 4 for a SUPERPOSITION of (t,q). It requires no coherent memory
access primitive. All circuits act on known indexed wires. Array dimensions
and every comparator's locations are fixed before the query register is
prepared; the controller generates the gates with finite counters.

For each outer tuple compute its exact sum and required residue query
using ripple arithmetic and long division on O(n)-bit words. Prepare
query records containing (residue,QUERY,ordinal,tuple). Copy canonical
bucket headers containing (residue,HEADER,ordinal,list of <=D tuples)
into the same working array. A HEADER sorts before a QUERY with the same
residue; ordinals break ties. Pad to a power of two with distinct invalid
sentinels whose keys exceed every valid residue.

Use a bitonic sorting network. On L records it has O(L(log L)^2)
comparators, with endpoints generated by the standard nested loops over
powers of two and the pair i,i XOR j. A comparator reversibly computes
its comparison flag, conditionally swaps the full record and keeps one
flag. Ripple comparison, controlled swaps and exact Toffoli decompositions
use poly(n) gates per comparator. Temporary comparison scratch is cleaned;
all retained flags count as allocated qubits.

After sorting, use a prefix circuit to carry the last header's key and
its D-tuple list. At each row a selector writes a NEW prefix state:
choose that row's header when its type is HEADER, otherwise the preceding
state. For a query, copy the carried list into its answer iff the keys
match, and otherwise copy an empty list. All preceding prefix states and
selector/intermediate bits are retained until the answer is copied, then
uncomputed. This is a Boolean circuit of O(L poly(n)) size and scratch,
not a hidden pointer traversal or postselection operation.

Inverse the sorting network while carrying answers with their records.
For each comparator in reverse order, use its saved flag to undo the swap,
then recompute the comparison on the restored original keys to erase that
flag. The answer field never affects a sorting key. Query answers now
occupy their known original positions. Copy the required fields, and
reverse the full lookup construction when its output is no longer needed.
This implements a clean coherent lookup on every basis value of (t,q),
and hence on an arbitrary superposition by linearity.

Construct D padded F/G slots per outer query by exact arithmetic. Each
slot has an EXPLICIT valid bit inherited from its returned representative.
Missing representatives are invalid PAD rows, never an arithmetic zero
that could mark a query. Sort invalid slots after every valid value, and
exclude them from the left buffer and every match clause. The signed sum
keys can use two's-complement comparison or a common fixed positive offset.
A second
fixed sorting network implements the exact-value ordering in Section 4.
Its prefix circuit carries the current value, the first D left tuples
and their valid flags. On a RIGHT row, loop over all D positions and the
at most C excluded strings, using exact equality circuits to compute
whether any full tuple is new. The buffer position range is a fixed
constant, not a quantum address. Build a Boolean OR of these clause bits
with its history retained. Apply Z to this one predicate bit and reverse
ALL computations, including both networks and all arithmetic histories.

Also require 0<=t<=k and 0<=q<p in the predicate. Invalid encoded query
values are unmarked. The resulting unitary is exactly the sign flip for
existence of a verified nonexcluded full witness among those canonical
records, with all workspace returned to zero. All these classical
Boolean circuits have exact reversible compute/copy/uncompute realizations
using NOT, CNOT and Toffoli. Clifford+T synthesis adds only a fixed factor.
No approximation error or uncharged rotation gate occurs.

Because L=O(DM), log L=O(n), every record and arithmetic word has O(n)
bits and D,C are absolute constants, the entire predicate costs
M poly(n) gates/bit operations/qubits on EVERY branch. Gate generation,
coefficient/exclusion reads, known addresses and their full charge are
included. The layout and implementation are completed in Section 8.

After measuring a query (t,q), the same dictionary joins and bounded-buffer
scan can be performed classically on basis records to recover an actual
witness. Verify its exact target sum, residue and absence from E before
returning it. This also costs M poly(n). Thus the finder never outputs a
false or repeated witness, including on unsuccessful seed choices.

## 6. Bounded quantum search and trial success

Let U=2^ceil(log2(k+1)) and V=2^ceil(log2 X). Search the power-of-two
domain of pairs (t,q) in [0,U) times [0,V) using Hadamards. It has
A=UV<=4(k+1)X elements and all admissible (t,q) are present. Pick a
uniform integer j from [0,J0), J0=2^ceil(log2(A)/2), using measured
Hadamard bits. Make exactly j Grover iterations for Section 5's predicate,
measure (t,q), and perform the classical witness recovery/verification.
All loops are bounded, including unsuccessful searches.

For completeness, if m queries are marked and sin^2 gamma=m/A, the
uniform state's good/bad plane gives probability sin^2((2j+1)gamma)
after j iterations. For 1<=m<=A-1 the mean over j is exactly

 1/2-sin(4J0 gamma)/(4J0 sin(2gamma)).

Since sin(2gamma)=2sqrt((m/A)(1-m/A))>=sqrt(2/A) and J0>=sqrt A,
this mean is >=1/2-1/(4sqrt2)>1/4. This argument covers dense marked sets
as well as a unique solution. If m=A, success is 1. If m=0, recovery
returns no witness; verification prevents false positives.

Fix any one new witness at the start of the trial. Its block-2 and block-4
tuples survive with probability 1/4. Conditional on that event the bounded
uniform-prime draw succeeds with probability >=1-2^-256, and its prime is
good with probability >=1-1/4096. On these events Section 4 proves that
some query is marked. The bounded Grover procedure finds a marked query
with probability >1/4. Therefore the WHOLE trial succeeds with probability
at least (1/4)(1-2^-256)(1-1/4096)(1/4)>1/32.

This is a worst-case guarantee for every fixed weight list, residue and
excluded set admitting a new solution, not a heuristic distribution claim.
Every trial draws fresh subsets, bounded prime candidates and Grover iteration count.

## 7. Complete discovery and the original phase instrument

To discover a fiber, run at most C=4096 discovery blocks. Each block makes
at most 4096 independent trials, stopping at its first verified new
witness and adding it to E. Stop all discovery after an empty block or
C found strings. The found list is always distinct and correct.
When a new witness remains, a block misses with probability <=
(31/32)^4096<2^-128; the last inequality follows from
2*31^32<32^32. At most C blocks give premature stopping probability
<=C*2^-128<=1/1024. Conditional on a fiber of size <=C, the entire fiber
is therefore discovered except with this probability.

During discovery the original k input phase qubits have been held
untouched after measuring their low-residue sum e. Their magnitudes on
that fiber are equal. Sort the found k-bit strings, pair consecutive ones,
and discard an odd leftover. Compute on the ORIGINAL index register the
flag and constant-size pair ID by equality with these at most C strings,
and measure them. If it matches no retained pair, FAIL and discard all
inputs. Otherwise it has exactly the two original phases indexed by
known y0,y1. XOR y0, choose a differing pivot, and clear the other differing
bits by CNOTs from that pivot. The remaining qubit has the exact phase
label difference sum_i (y1_i-y0_i)a_i, with full signed labels a_i.
No correctness assumption about discovery completeness is needed for a
returned pair. Every successful result is exact.

Suppose now the k=b+6 low residues are independent uniform in Z/2^b.
The actual measured fiber has the size-biased law of the fiber at a
uniform binary index Y. For any other z, one coefficient in f(z)-f(Y)
is +/-1, so its residue is uniform. Hence

 E|fiber(f(Y))|=1+(2^k-1)/2^b<65.

Markov bounds probability of a fiber larger than C by <65/4096.
On complete discovery only one index in each odd fiber is discarded,
whose total mass is <=2^b/2^k=1/64. Including discovery error, the whole
phase-combination attempt succeeds with probability at least

 1-65/4096-1/1024-1/64=3963/4096>20/21.              (7.1)

This is the required fresh-call average BEFORE child generation, not a
pointwise promise conditional on arbitrary fixed full labels. All selection
choices, including prime trials, subset coins, query measurements,
verification and pair choice, depend only on the cancelled low residues
and their independent coins, never on unused high blocks or the unknown
phase. The nonzero signed incidence of the two distinct index strings
has a unit +/-1 on some disjoint original leaf. Thus the unused-block and
fair-parity/characteristic-function arguments in the included source
apply unchanged to this NEW finder. Failed attempts discard every input
and scratch; no free postselection or reuse is assumed.

## 8. Streamed physical allocation and exact storage accounting

For a standalone helper, set Aword=1024(n+1), W=2^256 M(n+1)^4.
Reserve sixteen DENSE regions of W qubits each, initially zero, plus
O(n) phase/query/source staging. The entire prefix counts, including
unused cells. A caller can reserve it at its largest M and reuse prefixes.
Known bases, row strides and bit offsets specify every address; their
bit lengths are <=Aword. No sparse indexing convention is used.

The regions hold raw S_2/S_4 records, canonical dictionary headers,
lookup inputs/answers, F/G lists, two sorting networks' comparison flags,
prefix histories, bounded-match/OR flags, arithmetic scratch, recovery
records and fixed metadata. There is NO prime table: Section 3 stages one
candidate/divisor/remainder at a time. Slots are reused between trials,
and no execution history grows across them.

Here are concrete capacities and the scratch schedule. A number, tuple
identifier, prime, target, address or sum uses O(n) bits, bounded by
Aword. Raw domains have <=M records; dictionary headers have <=M records
of O(D Aword) bits. Padded F/G lists have <=2DM records. Each network
can be padded to <2^16 M records. Its binary logarithm is <=10(n+1), so
at most 2^24 M(n+1)^2 single comparison flags suffice. A comparator
computes its flag, copies it out, and uncomputes its local arithmetic
scratch BEFORE swapping the keys/payloads. This local scratch is reused
at the next comparator; a full word-sized history is NOT retained per
comparison.

For modular arithmetic on each query, reversibly compute its answer into
an output field and reverse the local computation, reusing O(Aword^2)
scratch for the next query. Retain only the actual O(n)-bit query outputs,
not every long-division gate value across all M records. A prefix selector
retains one O(D Aword)-bit carry state per record. Its temporary Boolean
scratch is likewise cleaned after copying that carry state. This costs
O(M D Aword), not an unbounded history.

The exact-sum join's first-D-left buffer is in those prefix states. For
each right/left candidate, compute the fixed C exclusion comparisons and
validity test, copy one clause bit, and reverse its local comparison/OR
scratch. Only that clause bit and the global OR's bounded history remain;
all O(Aword) local scratch is reused. There are O(MDC) clause/control bits,
with D,C absolute constants. Invalid padded rows never enter a buffer or
produce a clause. Query records, carried representative tuples, dictionaries
and signed values all include their explicit validity flags.

Thus the LARGE arrays have at most O(M(n+1)^2) bits with fixed absolute
D,C/template constants; arithmetic scratch adds O((n+1)^2). The very
conservative W=2^256 M(n+1)^4 regions cover these arrays, padding,
metadata, source moves and cleanup counters: for example flag count is
<=2^24M(n+1)^2, and combined prefix/record bounds are below
2^50M(n+1)^2 using D<2^13, C=2^12, Aword=2^10(n+1).
The extra two n powers and fixed coefficient leave ample explicit slack.
All sixteen regions, not only their live subranges, are charged.

Large CLASSICAL helper arrays are computational-basis records within this
counted prefix. READ measures a classically specified cell into one
reusable classical bit. WRITE reads and applies X iff the old bit differs.
Ordinary coefficients/exclusions use O(n^2) bits; a fixed number of
O(n)-bit staged words and counters suffice for streaming, bounded prime
sampling, sorting and recovery. No ordinary classical copy of a large
array or exponential address map exists.

The simulation is a CQ mixture: conditional on virtual classical records,
record cells are a definite basis string possibly correlated with
arbitrary phase/reference states. READ preserves each conditional state;
WRITE realizes the same classical update/forgetting. COHERENT query,
network and prefix arrays are separately typed and are never measured
while a query is active. Copying a basis record into a query workspace
uses known indexed bitwise CNOTs, not a superposed memory address.

Known-index access is DIRECT: compute base+row*stride+bit with O(n)-bit
arithmetic and address that wire. Its cost is poly(n), including the FULL
address fee O(log(16W+O(n)))=O(n). No exponential bank scan is performed
per access. Quantum-dependent queries are handled exclusively by the
fixed comparator networks and prefix circuits, never by substituting a
classical indexed read for a coherent lookup.

Every gate is streamed by finite counters. Network endpoints use powers
of two and XOR indices; ripple/selector templates generate their other
known addresses. All comparison flags and retained prefix states are
counted qubits. After the final predicate phase, reverse all computations.
After a completed trial or discarded attempt clear/reset all used storage;
initialization and final cleanup of the ENTIRE prefix are also counted.
The original phase index is released only through verified pairing or
FAIL discard. There is no stored exponential circuit or hidden staging.

## 9. Explicit conservative polynomial factors

For the selected resource record the following generous bound keeps all
polynomials visible. Word width and physical address width are O(n).
A local classical arithmetic computation can be bounded by Aword^6 bit
work, allowing long division and indexed bit accesses. A single emitted
elementary gate or bit template, including its controller's address
arithmetic and the model's full fee, can conservatively be charged
O(Aword^4) work. These are fixed-length binary operations; no arbitrary
integer or real unit-cost arithmetic is assumed.

The bounded prime sampler makes O(n) candidates and at most sqrt(X)
trial divisors per candidate. Its work is <=sqrt(M)(n+1)^9 times an
absolute constant, and its scratch is polynomial without a large table.
Dictionary generation/sorting and recovery use at most O(M(n+1)^2)
comparisons plus O(M) word tasks. In a coherent predicate, O(M(n+1)^2)
network comparators each have O(n)-bit key/payload work; every local
bit/gate emission costs at most O((n+1)^4). Per-query long division,
prefix selectors, validity checks and the fixed C,D exclusions are covered
by the same or smaller order. Thus a complete predicate is bounded by
M(n+1)^8 times an absolute constant.

The search iteration limit is O(sqrt(kX))<=C3 sqrt(M)(n+1)^3.
Its diffusion, loop bookkeeping, measurements and classical witness
recovery obey the same budget. Entire-prefix initialization/reset costs
O(W Aword^4)=O(M(n+1)^8). A fixed C^2 number of trials does not change
any n exponent. Allowing extra room for staging, output, seed generation
and all guards gives the conservative COMPLETE helper bounds

 work <= C4 M^(3/2)(n+1)^16,
 qubits <= C5 M(n+1)^4, ordinary classical bits <=C6(n+1)^2.    (9.1)

Constants are absolute. All circuits and loops listed above are bounded
on every branch, including failed prime draws, failed searches, empty
fibers and discarded phase inputs. Since M=2^ceil(k/4), the exponential
parts are exactly 2^(3k/8) and 2^(k/4), up to outside constants. These
joint bounds include initialization, every address, circuit generation
and final cleanup for THIS compact sampler/layout implementation.
