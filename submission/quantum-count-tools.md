# Explicit high-confidence coherent counting for QSR2

Context: Brassard, Hoyer, Mosca and Tapp, Quantum Amplitude Amplification and
Estimation, quant-ph/0005055v1, Section4, https://arxiv.org/pdf/quant-ph/0005055 .
Windowed phase-estimation context is acknowledged in window-tools.md. The
sine-power preparation, exponentially small tail and full cost are proved
there. This helper gives the remaining Grover, integer-count and factor
circuits. QSR2 declares O(n) quantum storage, including the private window.

## Domain, Boolean oracle, and exact Grover circuits

Let U=2^t, L=2^R, Kcap=2^40 n^2 L. In this application t=mR and n>=2^20.
A classical predicate description specifies a subset S of[0,U). It includes
child tables, a measured low key, an optional binary hash, and optionally a
QUANTUM comparison argument x. Write P_x(z) for membership of z in that
subset and z<x when a prefix count is requested. The promised accepted set
has at most Kcap marked elements, so every prefix count is also bounded.

The main proof implements P by m literal L-row equality/XOR queries, reversible
additions, measured-key comparisons, a classical binary-matrix hash and a
ripple comparison with x. All rows and gate addresses are generated. No
quantum-addressed memory, physical source inverse or subset-sum oracle is given.
Here a query means this explicit Boolean circuit, whose full cost is multiplied
below. It computes a flag, phases that flag by Z, and reverses all scratch.
The private z register starts in H^t|0>. Define diffusion EXACTLY as
D=2|uniform><uniform|-I=-H^t (I-2|0><0|) H^t. Its zero test is computed
by Toffoli gates and reversed. The leading minus sign is essential here. The usual two-by-two
matrix multiplication on marked/unmarked uniform vectors gives eigenvalues
exp(+/-2i theta), where sin^2 theta=M/U, M=|S_x|. The known uniform vector
lies in their span. At M=0 its eigenphase is0. No eigenstate of the DCP
source is prepared or inverted by this operation.

Controlled Grover is also explicit: compute P, apply controlled Z to its flag,
uncompute, then H^t, a controlled zero-negating reflection, H^t, and Z
on the phase-control qubit. That last Z implements the leading minus sign
of D only in its controlled branch. Without it the Grover eigenphases would
be shifted by1/2 and the stated count formula would be wrong. Compute/phase/
uncompute cancels all Boolean-network global phases. Fixed-arity Boolean
controls use exact Toffoli/CNOT/NOT decompositions over Clifford+T. In particular
we control the logical reflection circuits, not an assumed free controlled
version of an unknown unitary. Their inverses are the known reversed circuits.

## Dyadic window phase estimation

Put J=ceil(sqrt(U Kcap)), rwin=1024n,
qpeBits=ceil(log2(2^16 rwin J)), Tpe=2^qpeBits.
window-tools.md prepares the private sine-power window on this phase register
using only ordinary zeros, dyadic gradient translations, counted measurements
and bounded retries. On the ideal gradient p=128n every Fourier rotation is
exact, since qpeBits<=2t<p. Use binary controlled powers of the explicit
Grover circuit, then the inverse binary Fourier transform. Folding the phase
gives gamma=min(a/Tpe,1-a/Tpe). With eps=1/(2^10J), the proved window tail
makes |gamma-theta/pi|<=eps except with weight delta=2^(-100n), uniformly
for every marked count and both conjugate eigenphases. That helper proves
the physical preparation, normalization and Fourier bound in full; no oracle
or free state is supplied. The actual gradient is replaced only once globally.

## Exact integer output on a bounded marked set

Generate a dyadic beta with |beta-pi^2|<=2^-P,
P=ceil(log2(Kcap+1))+32. Use P+16 alternating terms in the rational Machin
arctangent formula, square, and round to denominator2^P. Remainder estimates
for arctangent give more than the required precision. This is finite counted
CLASSICAL computation; no arbitrary phase or coefficient is advice.

On a phase estimate form v=U*beta*gamma^2, round to the nearest integer and
clamp to Kcap+1. This is exact integer arithmetic on the phase numerator,
its square, the known beta numerator and a power-of-two quotient. At the
reference count M<=Kcap, theta<=2sqrt(M/U). The Taylor remainder
0<=theta^2-sin^2 theta<=theta^4/3 gives
0<=U theta^2-M<=16Kcap^2/(3U).
The main QSR2 proof establishes directly t-2R>=80log2n. Thus
Kcap^2/U=2^80n^4 2^(2R-t)<=2^(80-76log2n)<=2^-1440,
and the displayed small-angle bias is below2^-180. This direct condition
also covers the smaller classical table width used here.
The phase error eps changes U*pi^2*gamma^2 by at most
64sqrt(U Kcap)*eps+16U*eps^2<1/8.
The beta error contributes less than2^-28. Thus rounding returns EXACTLY M
on every eps-good phase estimate, with room before a half-integer boundary.
At M=0 the same bound gives rounded0. No quantum transcendental calculation
is needed. The small-angle approximation is used only under the stated cap.

A clean schoolbook reversible product uses shifted controlled additions into
a zero accumulator, leaving its inputs intact; reverse the additions to clear
it. A constant number of O(qpeBits+P)-bit buffers suffices to square the phase
numerator, multiply by beta, form the power-of-two quotient, round, clamp and
XOR the result into a separate small register. Reverse the arithmetic to
clear all product/fold/comparison scratch. This is O(n) quantum scratch and
polynomial gates, not a stored history of polynomially many n-bit values.
The clamped output has w=ceil(log2(Kcap+2)) bits even on a bad phase estimate.

## Clean coherent count with one reused private window

After estimating the phase and computing its clamped integer count, XOR that
count into the external target and reverse the entire arithmetic, Fourier
and Grover circuit. Denote this genuine unitary involution by C^dagger X C.
On reference private workspace |window> tensor |0>, it approximates XOR of
the exact M_x with vector error<=2sqrt(delta), delta=2^(-100n). Before the
copy the difference is supported on the bad-count projection, of norm at
most sqrt(delta). Copying either value changes that component by at most
twice its norm; reversal preserves norms. The bound holds for every target
state. Orthogonality of different x extends it to superpositions and outside
entanglement. No DCP source operation is inverted.

The ideal reference returns the private window and all zero scratch unchanged.
Use this SAME window for subsequent count calls and reversed calls during
unranking. The physical inverse is the identical involution circuit with
its current window register. A whole-computation ideal-prefix vector hybrid
bounds all reuse disturbance, without a fresh-noise assumption about the
actual approximate workspace. window-tools.md supplies the complete argument
and global preparation/call losses. One constant number of O(n)-bit private
registers suffices; no coherent median array or repeated-estimate list lives
in quantum storage.

## A private factor estimate for an arbitrary nonempty marked set

Before hashing, M may exceed Kcap. Prepare a fresh bounded-attempt PRIVATE
window, use the same phase circuit without source-index control, measure the
full t+4-bit rounded U*beta*gamma^2 and reset the private system. Its predicate
uses only already measured low keys and classical metadata. No source phase
superposition or unknown phase is measured by this private estimate.

For every0<theta<=pi/2, M<=U theta^2<=4M. Good phase error changes this by
at most sqrt(M)/16+1/65536. The beta error contributes at most M/2^28 plus
1/65536, using gamma<=2sqrt(M/U)+eps and2^-P<=1/(2^32Kcap).
Rounding therefore gives an integer in[M/2,8M], including M=1 by the strict
lower bound before rounding. Output width t+4 covers even bad estimates.
A wrong factor estimate has probability at most2^(-100n) in the ideal-
gradient reference; fresh-window abort has the same bound and is charged.
The output depends only on lower-label/index data, not unused top source bits.
No median is needed because the phase window already supplies high confidence.
All private gates, resets, bounded failed preparations and inverse work count.

## Literal time blocks and error transfer

A Boolean predicate query is expanded in the main proof, not free. One block
uses O(Tpe) such queries, polynomial arithmetic/Fourier work, and bounded
private window preparation. Since Kcap=2^40n^2L and rwin=1024n,
Tpe<=2^49 n^2 2^(ceil((t+R)/2)). Each expanded predicate costs at most
2^200 n^12 L core steps. Including forward/reverse Grover and fixed
reflection constants, the full query work is at most
2^255 n^14 2^(ceil((t+R)/2)+R).
The integer identity ceil((t+R)/2)+R=ceil((t+3R)/2) is exact for all t,R.
Other work is polynomial: bounded window preparation uses at most2^20n^2
attempts of1024n tests, each with O(n) dyadic additions on O(n)-bit registers;
Fourier and clean count arithmetic have polynomial-size loops. All classical buffers here are O(n^2) or smaller; phase-constant buffers
are O((log n)^3). Even allowing O(n^2) schoolbook operations and both
bit-index/address-generation overheads,2^800 n^25 core steps is a loose
bound for all non-query work. Final reversible quantum arithmetic still uses
O(n) qubits; large coefficient-generation buffers are classical.
Consequently the ACTUAL smaller paid block is
 gcount=2^1000 n^30 2^(ceil((t+3R)/2)).
It includes all private preparation failures and counted padding. At most
64tL such blocks cover one node's rank, inverse, factors and ALL L output
records, including reversed searches. The exact identity
ceil((t+3R)/2)+R=ceil((t+5R)/2) and t<=n make their total at most
2^1006 n^31 2^(ceil((t+5R)/2)). Other fixed-node/preparation work and expected leaf work are bounded
by2^800 n^25 L with the elementary circuits in the main proof. Thus
 G=2^10000 n^40 2^(ceil((t+5R)/2))
covers every nonrecursive allowance and expected leaf work. No query, output
row, inverse, source filter, controller or padding operation is free.

Reserve the entire gcount amount BEFORE every count/factor block, aborting
if the remaining core budget is smaller. Pad completed blocks to this cost
with counted private no-ops. No guard interrupts a coherent unitary. A failed
reservation implies that the uncapped reference would exceed the same B.
Full address/generation/monitor charges are applied by the main proof.

For analysis only, replace a wrong private factor output by M, leaving
accurate outputs untouched, and replace each approximate count by exact
integer XOR. Retain the ideal global window and zero scratch in ideal prefixes.
The reference pays every full padded block and initial window preparation.
The main proof gives log2B<=n/8. Together with the window's delta=2^(-100n),
all preparation aborts, wrong private factors and coherent count replacements
cost less than B*(3delta+2sqrt(delta))<1/1024 over the complete capped
computation. No actual noise independence, physical source inverse or free
oracle is asserted. Source-label coupling and the single gradient initial
trace replacement are applied separately and unconditionally.
