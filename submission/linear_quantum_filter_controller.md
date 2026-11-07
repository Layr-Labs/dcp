# Complete selected literal controller for LQ-FILTER

## 1. Required interface and actual sources

This is a required proof appendix to
[the main LQ-FILTER proof](linear_quantum_filter.md), with
[the full deterministic filter proof](linear_quantum_filter_filter.md).
All five claims cite all three files. Section 3 is the actual online
controller, including every prefix slice, arithmetic template, loop,
ready address, pointer carry, gate dispatch and inverse stream. The
quantum circuit and source/model/endpoint proofs are in the main file.
The selected a_n, A_scale, B_j, b_j, R_v, L and Q are its Section 0 parameters.

The literal-generation method is credited to the complete local proof
critical_third_cache_generator_l2.md, 16253 bytes, SHA-256
`eb122317b103da59cdd982b29f863da27d1d932313e8b67861d1d212a64088f3`,
Sections 2--6, read directly. Its complete public form is E, submission
f0bfcbc9-ef55-4754-b61e-061100ace74f, commit
725ccdfea43184deed9aabe890bdb35b3b2e5037, member
[submission/critical_third_cache_l2_controller.md](https://github.com/Layr-Labs/dcp/blob/725ccdfea43184deed9aabe890bdb35b3b2e5037/submission/critical_third_cache_l2_controller.md),
30611 bytes, SHA-256
`88c0279062fd2b9a948b2f1922e80c620437e6552a25e37fff4af483e3eeb340`,
Section 10. Exact archived bytes, member hash and public commit were
checked, and the complete needed method was read. Only its classical
ready-address/tape-head/marked-loop method is used here. No E phase
cache, robust marginal-source model or selector is executed. The full
needed controller proof follows, so no external compiler theorem or
review verdict is a mathematical premise. The direct semantic source
and its complete inherited credits are in main Section 10.

## 2. Exact words selected by the controller

### 2.1. Arithmetic interface

Main Sections 1 and 4 give the exact phase-free Toffoli and carry words,
total padded-domain permutations, fixed table, score and all-word
clean-helper maps. A helper starts and ends zero for every logical data
word. This remains true on dirty logical verification data. The known
addend implementation in Section 3.3 selects an explicit controlled
constant-adder realization of the same map. Its quantum control is
unchanged and its known classical prefix bits are read, not measured
from a quantum register. No relative phase is added by these Boolean
implementations.

### 2.2. Exact symmetric-probe and stop interface

Filter Sections 3--4 give the full-input unitary module and actual inverse.
Compute D_v(w) into a clean flag, phase it under the unchanged active flag,
and uncompute it. D_v(w) depends on neither code nor probe. For controlled
diffusion apply H, controlled zero sign flip, H, and Z on the unchanged
active flag to supply the required controlled minus sign. Inactive
branches receive identity. The inverse is the literal R_D R_u word.

For module code c retain alpha=[z in {0,c}]. Emit H on the logical probe,
2t Grover words controlled on alpha AND probe, erase that conjunction,
emit H and t inverse Grover words controlled on alpha. Recompute the
conjunction, XOR c into z under it, and erase it before the probe changes.
Compute D_v(w), XOR alpha AND D_v(w) into the probe, and reverse D_v.
The exchange preserves membership in {0,c}, so recomputing it clears alpha.
All clean helpers clear on every logical input, including nonzero probes.
Outside {0,c} the unconditional H pair cancels exactly. Invalid and initial
marked checks use their exact total 0/code exchanges. No code is reset or
overwritten. The complete inverse reverses every elementary gate, flag and
phase word. The logical probe is separate from clean Boolean scratch.

### 2.3. Chronological recursive and inverse schedules

For j>0 the actual chronological V_j word is

    V_(j-1), O_live, V_(j-1)^dagger, R_zero, V_(j-1), E_j.

Its actual inverse is

    E_j^dagger, V_(j-1)^dagger, R_zero^dagger,
    V_(j-1), O_live^dagger, V_(j-1)^dagger.

V_0 is the complete F_0 word. Its inverse reverses every gate in F_0.
R_zero acts only on the current attempt's candidate, opponent, code and logical probe;
it excludes read-only row/axis records, all other attempts, the gradient
and clean arithmetic helpers. X,Z,X on a zero helper supplies its
unconditional minus and returns that helper to zero. All helpers are
cleared before either reflection. Every local inverse reverses the
actual Clifford+T word, including phases.

The shared W_v verifier is one fixed unitary word on its candidate and
logical opponent/code/probe workspace. Its initial uniform preparation is H, not a
reset of that workspace between calls. It remains a total known word
when actual verification leaves leakage. Its arithmetic helpers clear
on every logical word. The ideal-inner-zero hybrid argument in main
Section 6 accounts for the leakage; the controller does not assume it
vanishes. The entire known U and inverse include row/axis generation,
all retained attempts and probes, the shared verifier and its probe,
verifications and answer logic. Acquisition is outside U and its inverse.

## 3. Complete selected literal controller

### 3.1. Layout and raw operations

Put ell=log2(n+2). L continues to mean the recursive depth in the source.
Pad each classical prefix, label, code, public-bound and arithmetic row
to the next power-of-two length. Pad the fixed field types separately.
Do the same for the fixed quantum register types and attempt banks.
Rows have O(n) bits; there are O(n) classical rows and 1024 quantum
attempt banks. This uses O(n^2) classical bits and O(n) qubits. Padding
does not change an arithmetic width or data map. Include unused padding,
all initialized cells, pointer fields and controller work in M_alloc.
Then

    a_addr=ceil(log2(M_alloc+2))=O(ell),  p=Theta(ell).

An array bit has address base+(row<<shift)+bit. Addresses of fixed field
types have fixed bases. Setting a fixed number of ready operand-address
words at the start of one bit scan costs O(a_addr) raw bit actions:
copy the known row/bit fields, shift by the fixed field width, and add
fixed offsets by ripple. There is no product of two changing addresses.

Use a finite-program bit controller with a fixed number of local work
tapes and heads. Count each bit read/write, head move, endpoint test,
fixed-size logic step and gate dispatch as a raw action. Conservatively
charge O(a_addr) for every raw action, including local head moves. This
also pays every required indexed access and every operand use of a
fixed-arity gate. An indexed gate directly uses the current ready address
words. It does not require an additional serial copy of all address bits
before paying its indexed-gate charge. Every address construction, copy,
inspection or change that is actually performed is counted separately.

Within a ripple bit gadget, finite control selects a fixed number of
ready operand fields. These include adjacent carry bits, the data bits
and the unchanged outer control. Moving to the next bit changes their
addresses by fixed power-of-two strides. There is no new full address
construction at each gate.

### 3.2. Carries, endpoints and a complete bit scan

For increment, a tape head starts at the pointer's low marker, reads and
flips the trailing ones and the next zero, then returns to the marker.
Decrement uses trailing zeros. A high marker handles full wraparound.
Each visited cell costs a fixed number of raw actions. No separate
numeric bit cursor is copied or updated for this carry walk.

For m consecutive increments of a w-bit pointer from any starting value,
bit h changes at most floor(m/2^h)+1 times. Hence at most 2m+w bits change
in total. Reads, writes, carry tests, moves and returns have the same
bound up to an absolute constant. The statement also holds for decrement,
reverse scans and a fixed power-of-two stride, by ignoring fixed low bits.
An isolated carry can cost O(a_addr); constant cost for one gate is not
assumed.

End a local loop with a marked strip, traversed by a head. A scan of m
positions, endpoint test and rewind use O(m+1) raw actions. A fixed number
of strips suffices because arithmetic-template loop depth is fixed.
Each strip is at most Cn cells long for an absolute C: lengths include
Q, R, n, m, p and the short sum words. Total strip space is O(n).
The exponential iteration loop uses the binary counter in Section 3.5,
not an exponential strip.

Including ready-address setup, a fixed number of ripple, copy, swap,
comparison or Boolean passes over w bits therefore costs

    O(w+a_addr) raw actions.                         (C1)

The bound includes reverse endpoint setup and all returns of the local
heads. Extra O(a_addr) setup for a short action is retained. Numeric
outer indices can be updated by the conservative O(a_addr) bit method
per outer event; they are not tested after every ripple gate.

### 3.3. Prefix slices and the controlled-addition map

This is the point at which overlapping prefixes could otherwise hide
another logarithmic factor. For every row j and operand bit i, locate
the p bits of e_j starting at bit n-i. Compute this start once, with
O(a_addr) raw work. Scan precisely those p bits using the prefix pointer.
Do not copy the full n+p-bit prefix to obtain one slice.

One explicit constant-addition implementation is as follows. Use one
reusable p-qubit addend A, one control helper f, and the source's O(p)
ripple scratch, all initially zero. For each of the p known prefix bits,
apply X to the corresponding A bit iff that classical bit is one. Copy
the unchanged quantum operand bit t_i to f by CNOT. Add A into the phase
word modulo 2^p under f by the controlled in-place ripple word. Clear f
by the same CNOT. Apply the same known X preparations to clear A.
This is exactly phase <- phase+t_i*a_(j,i) mod 2^p. It returns A, f and
ripple scratch to zero on every logical operand and phase word. It uses
O(p) gates and qubits and no source-dependent classical branch.

The known-prefix preparation scans and ripple passes use (C1). Each
complete slice event, including control-wire setup, costs
O(p+a_addr)=O(ell) raw actions. Its inverse subtracts with the reversed
word, reads the same classical slice, and has the same bound. Starting
the next overlapping slice can conservatively reset all pointers in
O(a_addr) raw actions. No assumption about carry alignment between slices
is needed.

There are n slice events per operand and Q rows. A fixed number of
operands and member-pair orientations is used. Therefore all prefix
arithmetic, its setup, known-bit reads and reverses cost

    O(Q*n*(p+a_addr))=O(n^2*ell) raw actions.          (C2)

This avoids a stored table of all Q*n slice constants or gate words.
The new reusable addend is O(p) qubits and is shared across rows,
operands, recursive levels and attempts. It is within the linear quantum
scratch already allowed for the exact arithmetic.

### 3.4. Remaining edge and reflection templates

The affine phase combinations use a fixed number of p-bit ripple passes.
The cosine scan has a fixed number of gates because q=14. Even assigning
O(a_addr) raw address preparation separately to every gate in that fixed
scan gives O(a_addr) raw work per lookup, with its absolute table-size
factor retained. Thus no constant-width lookup is incorrectly assigned
free address setup. Its rational table construction has finite absolute
work and space, both charged.

The score numerator, coefficient 11 and clamp have fixed arithmetic
width. The sum word has s=bitlength(Q)+32=Theta(ell) bits. Per row, the
score arithmetic, exact addition, term cleanup and later reverse cost
O(s+a_addr) raw actions by (C1). Reading or controlling on a row/axis bit
has O(a_addr) setup and a constant number of gates. Copying the final
sign has the same setup allowance. Validity, equality, class-member and
canonical-ID arithmetic use O(n+a_addr) raw actions for each of a fixed
number of n-bit passes. Combining these costs with (C2) gives the full
edge/controller bound

    E_raw = O(Q*[n*(p+a_addr)+s+a_addr]+n+a_addr)
          = O(n^2*ell).                            (C3)

This includes both full scans around the copied sign. It holds for a
fixed number of pair signs per class edge and for arbitrary input words.
It does not condition on the empirical tournament being correct.

Zero reflection and diffusion need O(n+a_addr) raw actions. Active and
stop-code tests, their XOR exchanges and cleanup use
O(log(n+2)+a_addr)=O(ell) raw actions apart from their edge calls.
All exact controlled Boolean decompositions have fixed arity and a
constant number of gates per local bit gadget. The forward and reverse
streams use the same rules and bounds. No measured, quantum or unknown
record value is used as a memory address.

### 3.5. Deterministic modules, blocks and recursion dispatch

Each module computes alpha by two O(ell)-bit comparisons, performs its
two H gates and controlled powers, generates/uses its known code, makes
the guarded code XOR, evaluates/reverses D_v to clear the logical probe,
and clears all flags. Retain alpha across both controlled powers. Retain
alpha AND probe only during the first controlled power, then erase it
before the next H; recompute it only for the code exchange. Controls
remain unchanged while their constituent Grover words execute.

Keep one reusable O(n)-bit classical iteration counter and one bound
buffer. For each Grover iteration, compare/increment the counter by full
O(n)-bit scans, counting all reads, writes, carries, endpoint tests and
returns. Construct t=2^h and 2t by zeroing/copying the finite O(n)-bit
buffer and setting the designated bit, also with counted address setup.
One module costs

    O((3t+1)*(E_raw+n)) raw actions.               (C4)

This charges the short t=1 modules, every exact predicate check and even
full O(n)-bit counter work for them. A block has sum_(h<b)t=B-1 and
b<=B for B>=2. Including all module ends, h counters, code generation,
power-buffer setup and block endpoints, it costs O(B*(E_raw+n)). There
is no unproved constant-delay increment and no B-cell classical strip.
The exponential loop uses the finite binary counter, not stored history.

All new public integers have bounded sizes: b_j=O(n), code values O(n^2),
their binary widths O(ell), and loop-counter/bound buffers O(n). Public
code schoolbook arithmetic O(ell^2) is O(n) and is performed once per
module, with a fixed-size slot retained during the comparisons/XORs.
Use an O(n)-cell marked strip, or counted full-width binary tests, for
the h, block and R_v loops. Initial marking, end tests and rewinds cost
O(n) per block/module if needed and are already covered by C4. A new
endpoint is not created by an uncharged search through an exponential
word. Inverse loops descend through the same finite public indices,
load the same codes and bounds, reverse every local word, and have the
same charges. Actual nonzero probes or stopping words do not alter the
classical stream or any loop count.

Recursion frames contain a level, direction and one of a fixed number
of program positions, each O(ell) bits. A stack head enters, reads and
leaves O(ell) cells per frame occurrence. The schedules in filter Section 7
give the exact forward and inverse emitter, with depth at most L+1=O(n).
The complete stack uses O(n*ell) classical bits.
Only a leaf block uses the large iteration/bound buffers, so these are
reused between calls. No child recursion occurs inside a module. There
is no stored expanded circuit, quadratic quantum history, or quantum
recursion frame. Reflection/address setup and frame dispatch cost fit
the complete recurrence in main Section 9 and filter Section 10.3. The first-verified logic, complete U and
U^dagger use the same counted Boolean/reverse templates.

### 3.6. Other literal templates and setup

The acquisition translations and comparisons have w=O(n). Applying (C1)
to each exact probe gives O(n) raw controller work per probe, besides
its counted gates. There are O(n) levels, O(ell) probes per offset and
Q=O(n) deliveries. Thus acquisition costs O(n^3*ell) before the final
address charge. Count increments, exact dyadic reconstruction and
binary prefix division fit this bound. Position, probe and measurement
reset words are charged. Measured histories need not be retained by
the algorithm after the required count, label and prefix is stored.

The gradient has g=O(ell) bits and at most 80 attempts. Its tests,
classical inverse modulo 2^g, doubled constant generation, two multiplier
sequences, swap and inverse all have polynomial work. Reuse the stored
O(g^2) classical constants and one O(g) quantum scratch space. None of
these words is an unknown-input preparation inverse.

For the endpoint, classical k_j*t multiplication, reduction and division
have O(n^2) raw work per row, so O(n^3) total. Rounded gradient translations
are exact controlled additions on g bits. They clear their O(g) helpers.
Trit measurements, counters, invalid-class comparison and the final
choice have polynomial counted work on every outcome. The invalid class
is changed to 0; both possible valid even-N endpoint values lie in [0,N).

Generating all 3^j and B_j values by exact integer arithmetic costs at
most the source's O(n^3) raw allowance. Store O(n) public words of O(n)
bits. Exact binary search for ceil(sqrt(n+1)) with schoolbook squares
uses polynomial work in bitlength(n+1), within that allowance and the
same space. Initializing the aligned layout, O(n) loop strips, fresh
qubits, code buffers, all buffers and table is charged polynomial work. These
steps add no exponential data structure or uncounted advice.

This covers every repeated template: prefix preparation and arithmetic,
table/score scans, carry and Boolean cleanup, member/validity tests,
Grover/reflection and stop/probe words, deterministic power/iteration loops, recursive
dispatch, verification, answer selection, acquisition, gradient,
endpoint and the literal inverse of each unitary part.

