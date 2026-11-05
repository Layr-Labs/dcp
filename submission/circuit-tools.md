# Complete streamed operand generation and exact rank work for QSR15

These are raw CORE counts. Every raw event additionally pays the full
allocated-memory and external-monitor costs in controller-tools.md.
No instruction/gate/word/address/controller operation is free. Define
x=log2n, a0=n^(1/4), H=sqrt(nx), U=2^t and L=2^R only for analysis.
The main proof fixes the integer program for every n>=2^20 and proves
R<=a0+1, m<=2a0sqrt(x), H<=t<=2H, t-R>=H/2>=96x,
sqrt(x)<=a0 and all data words O(n) bits. No real advice is used.

## Allocated addresses and streaming generator

The explicit stack, initialized tables and arithmetic/statistical buffers
fit the loose allocation2^10000 n^3L bits/qubits. Thus complete operand
addresses, including scratch, have width
 a_addr<=10001+3x+R<=512a0.
Indeed(10002+3x)/2^(x/4) decreases for x>=20 and its endpoint is below315;
R<=a0+1 includes its ceiling. The actual tighter memory bound remains
O(n^(7/4)L), not the loose address-proof allocation. No extra table is
allocated merely to reach that loose upper bound. Public B,Qcap,q constants
and a constant number of O(H)-bit counters fit the same buffers.

Materially adapt the streaming schoolbook construction of published
QSR11 circuit-tools.md lines20-40: keep a constant number of a_addr-bit
workwords and one constant-arity gate buffer. Each operand is a fixed
combination of row/field offset products and sums. Schoolbook a_addr-bit
arithmetic costs O(a_addr^2) bit positions. Explicit schoolbook loop/index
control and generation of those operations' OWN operand addresses costs
at most O(a_addr^3) raw bit/head transitions per such position. Serially
output every operand-field bit, expand fixed Toffoli networks exactly, and
reuse scratch rather than accumulating emitted instructions. A deliberately
loose2^20a_addr^6 raw steps per fixed-arity logical bit/gate covers this
complete process. The same scheme reads/writes classical bits and emits
measurement/reset operations; no data word is a unit-cost operation.
The finite machine uses ordinary initialized loop counters and sequential
bit pointers. Each raw step ALSO receives its full global access price.
No extra control oracle or recursive monitor is assumed.

The published near-quadratic private-counter specialization is not reused:
here a_addr=O(n^(1/4)), and the raw stream counts below are new.
Clock widths remain Theta(H) from the actual cap formula, including the
fixed1000-bit coefficient. Controller scratch O(a_addr) fits the same
classical envelope and does not change quantum storage.

## Ordinary classical product-mask work

A product mask z<U is an explicit CLASSICAL t-bit counter. Read its m
R-bit fields and for each field form the actual row/field address in the
already allocated classical child table. Read the row's constant number
of O(n)-bit aggregate words, adding them serially with reused carry/sum
scratch. This uses O(mn+t) logical bit operations, including explicit
row selection; no quantum-addressed table or QRAM is used in this part.
Every address is emitted by the generator above, not treated as a free
RAM instruction. Padding/normalization are fixed widths and binary shifts,
with each touched bit counted.

Test the low residue/root target with O(n) logical positions. Compare the
quantum x to the CLASSICAL z and conditionally increment its t+1-bit rank
accumulator with O(t) fixed-arity gates. Reversing that computation uses the
same count. For g inverse, maintain the exact CLASSICAL valid-row count c
using O(t) bit operations, compare the quantum rank to c with O(t) gates,
XOR the literal z into the output with O(t) gates and erase the equality
flag. The old index erasure and measured high-rank chunk use a constant
number of such passes. Output metadata for every retained L row is written
in ONE additional classical U pass, computing each retained row from the
same subset sum, with O(n+t) extra bit work per z. No U-sized list is saved.

Consequently one z costs a fixed constant times mn+t logical positions.
Because m<=2a0sqrt(x), t<=2H, n>=2^20,
 mn+t<=4n^(5/4)sqrt(x).
The address generator satisfies2^20a_addr^6<=2^74n^(3/2).
With the fixed ripple/add/compare/XOR constants and complete control fields,
one full mask is bounded by2^110n^(11/4)sqrt(x)<=2^110n^3 raw steps.
The last inequality is sqrt(x)<=a0. The constant number of forward/reverse/
count/inverse/output passes, including enumeration, initialization and flag
reset, costs at most2^130n^3U. No multiplication by L is introduced here.

## Coherent validity outside the U enumerations

The exact instrument also needs validity of its QUANTUM product index.
For each child, scan its L literal classical rows; compare the R-bit index
to the literal row number, XOR the n-bit constant record into one reused
scratch word, erase equality, add into the accumulator, and reverse the
lookup before proceeding. Only one n-bit scratch word and a constant
number of flags are live. Total gates are O(mL(n+R)+mn+t), including
root/low-key comparison and uncomputation. Compute validity a FIXED number
of times per instrument, retain its one bit during the rank scan and erase
it afterwards. This is outside the classical z loop. Source controls are
preserved exactly; the complete numerical rank/g XOR maps are total and
unitary before the specified high-rank measurement.

The same generator gives at most2^130n^3L raw steps for these fixed queries,
which fits the U allowance since L<=U. There is no mL quantum scan per z,
no coherent table of flags, and no uncomputed gate-generation history.

## Helpers, initialization and smaller guard

For the unchanged source/leaf/gradient/basic helper circuits one may keep
the old slow bit-serial implementation. A loose2^200n^12L+2^80n^8 bound
covers Pascal data, constant-weight leaf ranking/output enumeration,
expected leaf retries/source filters, bounded n+20 gradient attempts,
Euclid, known correction inverses, initialized table buffers and terminal
live-table clearing. The leaf enumerates at most2^r<=2^12L(R+2)^2 masks;
all its words/loop widths are O(n), so the stated polynomial covers its
complete older implementation. The stack has at most O(n) tables, each
with at most L O(n)-bit entries; clearing is in the same bound and needs
no fresh sources. The complete statistical grid is bounded separately
in the main proof and included in E_D, not this basic-helper allowance.

Here U/L>=2^(H/2)>=n^96 and U>=n^192. Thus the old polynomial-times-L
helpers,2^80n^8 term and fixed2^130n^3U passes sum to less than
(2^1000n^3U)/2, for every n>=2^20. The remaining margin includes the
at-most16/15 geometric leaf retry factor. Set the ACTUAL public allowance
G=2^1000n^3U and recompute E_i,Wstar,B and both clocks accordingly.
This is an allowance, not a claim the old n^4 program paid padding work.
The larger fixed coefficient need not give a numerically smaller guard
at every small n. All asymptotic comparisons retain that absolute constant.
