# R4-BANK: a linear-classical-space implementation of four-level ranking

## 0. One physical algorithm and joint guarantees

For every integer N>=2 and every secret modulo N, n=ceil(log2 N), the ONE
physical program specified here recovers the entire secret with unconditional
probability at least 1-2^-8. On every execution branch, simultaneously,

 T=O(2^(n/12)n^25), S_C=O(n),
 S_Q=O(2^(n/12)n^(4/3)), Q=O(n^5).

All constants are absolute and outside the bounds. Addressing, circuit
creation, every allocated/padded cell, source acquisition/rejection,
measurement, reset, output and cleanup are counted. Exact representative
growth indices are 1,0,1,0. Malformed fraction zero requires independent
ideal coset states; no positive tolerance or impossibility is asserted.

The underlying VIRTUAL program and its complete mathematical proof are
reproduced byte for byte in virtual-source.md. Its helper is class-ranking.md
and its complete source/decoder proof is family-source.md. The physical
program executes exactly that four-level selection/decoder schedule,
through the explicit storage translation in Sections 2-5 below. It is not
a combination of resource bounds from different level schedules. The
virtual program's quadratic CLASSICAL store is reimplemented with counted
basis qubits; its output distribution, gates on active coherent registers,
loop bounds, original source usage and cap outcomes are unchanged. This
wrapper independently proves all resulting physical resource bounds.

## 1. Material sources and complete source files

The directly adapted R4 submission is a04427bc-c023-4904-905d-340739f5ffc7. The exact retained files are identified below. Its exact main proof is reproduced as
virtual-source.md, SHA-256
5886832dcbf1a5b67fbe786330498e873a7faf9e5a8c7a7df8aba7a1267d71fd.
Its exact class-ranking.md has SHA-256
c7ff0a8a505748a13d76b98edea864541599b21cc545f0b8004bf743b266866d.
R4 supplies the ACTUAL four-level schedule, tightened high arity
ceil(4(b+ell)/3)+128, dyadic modulus 2^(ceil(k/4)+64), LOW fallback,
Cartesian rank/inverse, logarithmic-leftover full decoder, finite extraction
and literal all-branch acquisition cap. All proofs are included in full;
a published verdict or attribution edge is not used as a mathematical premise.

The basis-memory simulation is directly adapted from own published
QLOG-BANK f949830e-3dd9-4a7e-af4e-4aabedbfb672, evaluated commit
59100526ce3dc11de2289a0a5d3f1b2c1c59463b, source proof SHA-256
cd1f8f1af807ce35a8f2994666627eb63aca4dd03c2db645dee3dac7a60cbb8b.
R4 already used this for LARGE helper tables. Here we additionally store
ALL growing virtual classical records in a separate, explicitly bounded
polynomial basis-qubit bank. Old polynomial-bank numerical bounds and
any whole-program interpreter costs are not inherited; the direct access,
streamed instruction schedule and cost proof are given below.

The complete family-source.md is unchanged with SHA-256
11f96191f1ab9c78f070472c4cb5e0552ec25381398ffc13b51d7f9c1b7c3fc7,
originally supplied by own QLOG 8870de8c-e8dd-4d03-82c7-57842e846e4f,
evaluated commit4f7e2b4f8dbcf19aa8dce588a8771a21297f42be. Its full
exact transforms, extractor, low-fiber moment, unused-block/frequency law,
all-modulus decoder and exhaustive finite tester remain the direct source.
Historical credits in all retained files remain, including own R3 and
BJ3-C and the conceptual four-block/canonical-table source
arXiv:2608.07309v1 Sections 3.1-3.3. No QRAQM/walk/oracle theorem or
prior numerical verdict is imported. No literature-first claim is made.

## 2. Full virtual-classical store and physical layout

Use exactly the explicitly bounded bit-string RAM implementation of
virtual-source.md and class-ranking.md. Its large helper tables are ALREADY
counted physical basis qubits and remain in that role. All other virtual
classical records have simultaneous peak at most C0(n+1)^2 bits by that
proof. Choose the fixed integer C0=2^80. The field bounds below give an explicit
capacity certificate; there is no input-dependent constant or advice. Reserve a
contiguous bank V=C0(n+1)^2 basis qubits, initialize every cell to zero,
and charge all of them even unused. Known fixed fields subdivide it into:

* input/constants and cap/precision/Euclid/CRT source/extraction records;
* pending labels, coefficients and their validity/ownership fields;
* four depth-first frames, offsets and finite loop counters;
* the current decoder's K full frequency/basis/outcome and grid-score records;
* fixed-C LOW found strings and all remaining virtual classical scratch.

For n>=256 the proof gives at most 64(n+1) pending phases, signed label
words O(n), k<=20(n+1) coefficients, K=O(log n) frequency words,
n+5 extraction counters of O(log n) bits, and a fixed number of arithmetic
words or O(n^2) work areas. For an explicit generous check: rmax<=20(n+1), so log2 q0<=
4log2(n+1)+18, log2 nq<=5log2(n+1)+20, and
K<=2^20(n+1). A full label/frequency/residue record has <=64(n+1)
bits; hence decoder records use <2^27(n+1)^2 bits. Pending labels,
coefficients, depth frames, extraction counters and LOW lists each fit
2^30(n+1)^2 bits, with room for schoolbook O(n^2) scratch. The
fixed 4096-entry rational trig tables and their finite generation scratch
also fit 2^40(n+1)^2 bits. Subdivide V into eight equal regions of
2^77(n+1)^2 cells for these fields, controller scratch and spare cells.
Thus the full explicit layout fits the chosen V. Fixed-C lists can also be banked. This is a capacity bound on simultaneously
live records, not the whole history of all attempts. Release/reset a virtual
field when the corresponding ordinary algorithm frees it; no ever-growing
transcript is retained. Loop-local arrays reuse their fixed fields.

Place the bank before the existing helper prefix in the physical address
space. Shift all helper numeric addresses by V. The original sixteen
W-qubit regions, every header/padded row and local coherent scratch are
still fully counted. Original quantum data, phase qubits and coherent
sum/rank/predicate registers remain QUANTUM registers: the translation
never treats them as measured classical memory. Only virtual classical
bits are moved to the polynomial bank. One helper runs at a time.

The actual ordinary controller holds input/output as needed and a FIXED
number of O(n)-bit words: instruction window, numeric bit addresses,
a few Boolean operands, word staging, counters for the currently emitted
loops and arithmetic scratch for address generation. Bit-string arithmetic
may stream work to its virtual bank fields rather than allocate an ordinary
array. There is no stored exponential instruction list, no duplicate of
pending labels/coefficients/frequencies, and no materialized classical
copy of a whole helper table. This uses O(n) ordinary bits.

## 3. Exact READ/WRITE and correlated-state simulation

Maintain the invariant

 rho=sum_x p_x |x><x|_bank tensor rho_x^(other registers),

jointly with the ordinary controller transcript. Here x is the entire
virtual classical memory plus already-classical helper tables; rho_x
may be correlated with it. This is a mathematical density-operator
representation, not a physically stored transcript. It allows arbitrary
correlations with unmeasured phase registers.

A virtual READ of a classically computed bit address a measures that
known bank cell in the computational basis, places the result in the
fixed ordinary operand window, and leaves the bank cell unchanged.
Conditional on that result the remaining state is exactly the matching
rho_x. WRITE(a,b) first READs the old basis bit and applies X if needed
to make it b. Known record copies and swaps are finite loops of these
bit primitives. Cells newly storing ordinary measurement outcomes are
written only AFTER the original program's measurement; no new coherent
register is measured by the translation.

A classical elementary instruction reads its fixed finite operands through
READ, computes its Boolean result in the fixed operand window, writes it
with WRITE and releases the window. Variable addresses are computed by
the original finite bit algorithm, reading their virtual bits as needed.
Instruction dispatch and gate generation are streamed by the original
fixed loop program; a fixed instruction window is sufficient. These are
DIRECT known numeric addresses, not a scan of all V bits per access.
O(n)-bit word operations are expanded into their stated finite Boolean
loops, with intermediate arrays in the bank and a fixed word window.

Induct on the original program's instructions and measurements. READ/WRITE
exactly simulate access to its ordinary classical memory; Boolean
instructions, original measurements and classically selected quantum
gates then have the same joint probabilities and conditional active
states. Acquiring a mixed source copy inserts exactly the same independent
rho_s as before. Updating a source or ownership counter uses the same
logical value. Thus the compiled physical computation has exactly the
same output, source-cap/FAIL events and full-secret success distribution
as the virtual program. It never needs a preparation inverse, coherent
source control, purification, QRAM or another input oracle.

Coherent queries to existing LARGE tables are still the explicit LINEAR
scans in class-ranking.md, including compare/copy/uncompute. A banked
coefficient or row is read into a small CLASSICAL staging word before
using it as a known constant in that quantum circuit. The coherent key,
answer, original index, rank and inverse scratch are not measured. This
separation prevents the simulation from turning coherent lookup into
free random access or an inadvertent phase measurement.

## 4. Source/success guarantee and physical spaces

The exact simulation preserves the LOW and HIGH success bounds, low-only
selection, untouched-high-block law and Cartesian pair phase identities.
It preserves the literal Qcap=1024(6q0H0+2n), recomputed extraction
confidence, finite odd decoder and exact 2-adic recovery. The supplied
virtual proof therefore gives full-secret error at most
2^-10+2^-14+2^-20<2^-8 and Q=O(n^5), including failed/rejected original
copies, on every physical branch. The finite n<256 exhaustive branch
may use its direct ordinary O(n) implementation; no bank is necessary.

The ordinary controller space is O(n) by Section 2. Its final answer is
an explicit n-bit integer, read from the bank into the output window
before resetting any memory it needs. On FAIL/abort output zero then
clean up. All bank/helper initialization and complete resets are charged.
The input, output and finite arithmetic of the small-n branch satisfy
the same ordinary-space envelope with an absolute outside constant.

The complete physical qubit width is at most the original helper/active
quantum width plus V. Original S_Q=O(2^(n/12)n^(4/3)) absorbs O(n^2):
for all sufficiently large n, n^2<=2^(n/12)n^(4/3), and the finitely
many smaller instances enlarge only an outside constant. This counts
the ENTIRE V including unused cells and all shifted helper cells. The
full address length remains O(n), including every extra basis record.
There is no assertion that basis qubits cease to count as qubits.

## 5. Charged work of the actual translated controller

Use the virtual implementation's explicit BIT operations, streamed
reversible gates and generated known addresses; no unit-cost arithmetic
or arbitrary-value word RAM is introduced. Uniformly charge O(n) for
each primitive address/gate/bit action, a conservative bound already
used in class-ranking.md Sections 8-9 and virtual-source.md Section 6.
The polynomial bank's known numeric bit address is computed by adding
a fixed offset or zero-extending its explicit virtual index. With O(n)
bit strings this takes O(n) bit operations; READ/WRITE invokes a fixed
number of known-wire gates/measurements plus a fixed number of ordinary
operand-bit actions, with the same O(n) address/gate-generation fee.
Each original constant-fan-in bit instruction thus expands to a fixed
number of O(n)-charged physical actions. Word operations stream their
original finite Boolean loops, without nested full-bank scans.

The existing conservative estimates consequently remain valid, with a
changed absolute outside constant. More explicitly, generating <=L raw
subset rows uses O(L(n+1)^7) charged work; sorting/merging basis records
uses O(L(n+1)^8); controlled coherent scans and inverse arithmetic use
O(L(n+1)^6). Moving coefficient/metadata operands through READ/WRITE
has the same bit-level address charge already included in those bounds.
All are below the common HIGH O(L(n+1)^12) bound. LOW tests at most
2^(b+6) strings; computing a sum needs O(k*n) Boolean arithmetic actions
with O(n) charged access, fixed-C membership scans and loop bookkeeping,
well inside its O((n+1)^8) per-string allowance. Hence LOW remains
O((n+2)^20), and the smaller ordinary window changes no bound.

For source/extraction/decoder control, all counters/labels have O(n)
bits. Exact source multiplication uses O(n^2) elementary arithmetic/gates;
collective extraction uses O(log n) bounded rounds, O(n) counters and
O(n)-bit modular additions, with finite decoding/unwrapping. The odd
decoder has nq=O(n^5), at most O(nq) candidates per stage, K=O(log n)
records, O(n)-bit residues and the fixed finite trig table. Streaming
banked residues/score/max uses schoolbook integer arithmetic and a
fixed number of staging words. Including every access and generated
gate, O((n+1)^16) per bounded acquisition/root/stage is still generous.
Full V initialization/reset costs O(V(n+1)), a polynomial below the
selected total bound, and all helper allocation/reset costs remain paid.

The physical logical-phase conservation count is unchanged: each positive
helper consumes k>=7 acquired phase outputs and returns at most one.
Thus I<=Qcap/6=O(n^5) on EVERY branch. With
Lmax=O(2^(n/12)n^(1/3)), the HIGH contribution is
O(2^(n/12)n^(52/3)); LOW contributes O(n^25). Source/decoder/bank
polynomials are smaller. Therefore total physical work is
O(2^(n/12)n^25), simultaneously with the spaces/source bound. No
expected-time substitution or postselection resource discount occurs.

## 6. Exact representatives and fractional-error statement

For the actual physical program, log2 B_T=n/12+25log2n and
log2 B_SQ=n/12+(4/3)log2n, giving growth indices 1,1. The ordinary
n and original-copy n^5 representatives have index zero. All four
structured objects describe this one translated R4 configuration.

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

At fraction zero, unconditional recovery is at least 1-2^-8 jointly
with every all-branch resource bound above. No positive tolerance or
impossibility theorem is asserted; this fifth expression has no score.
