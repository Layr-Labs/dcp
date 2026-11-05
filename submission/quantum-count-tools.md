# Explicit high-confidence coherent counting for MSR6

Context: Brassard, Hoyer, Mosca and Tapp, Quantum Amplitude Amplification and
Estimation, quant-ph/0005055v1, Section4, https://arxiv.org/pdf/quant-ph/0005055 .
Coherent median repetition and its ancillary cost are standard context; see
also Patel, Tan, Subasi and Sornborger, arXiv:2403.18927v2, Introduction,
https://arxiv.org/html/2403.18927v2 . No oracle, taper state or implementation
bound from those papers is assumed. The required circuit and accounting are
reproduced here. MSR6 explicitly declares O(n log2 n) quantum storage.

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

## Dyadic phase estimation and an elementary tail bound

Put J=ceil(sqrt(U Kcap)) by integer square root,
qpeBits=ceil(log2(2^16 J)), Tpe=2^qpeBits.
A phase register H^qpeBits|0> controls Grover^k by binary powers, followed
by the inverse binary Fourier circuit. At most2Tpe Grover iterations suffice,
including reverse work. Its dyadic controlled rotations are implemented by
translation into the counted gradient Gamma_p, with p=128n. Since
qpeBits<=2t<p, these phases are EXACT on the ideal-Gamma reference. A
controlled dyadic phase uses a computed Boolean control and a conditional
addition of the known power of two to Gamma; uncompute its flag and scratch.
H, swaps, reflections and additions have exact Clifford+T decompositions.
The actual gradient's initial trace error is charged once by the main proof.

For an eigenphase nu, outcome a has amplitude
 (1/Tpe) sum_(k=0)^(Tpe-1) exp(2pi i k(nu-a/Tpe)).
For circular distance d<=1/2 this has magnitude at most1/(2Tpe*d), using
the geometric sum and sin(pi d)>=2d. Summing the squared bound over at most
two outcomes in each integer-distance shell shows that error larger than
K/Tpe has probability at most1/(2(K-2)), K>=3.
Set eps=1/(2^10 J). Then Tpe*eps>=64, so a phase estimate has circular
error at most eps with probability at least15/16, uniformly in nu. Folding
its dyadic value to gamma=min(a/Tpe,1-a/Tpe) changes error by at most eps
from theta/pi, for either Grover eigenphase. The superposition of the two
orthogonal eigenvectors gives the same success bound for the private uniform
input. This is a probability calculation, not physical eigenvector access.

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
For the MSR6 parameters this is below2^-180: t>=Hscale, R<=Hscale/16,
Hscale>=20log2 n imply t-2R>=17.5log2 n; therefore
Kcap^2/U=2^80 n^4 2^(2R-t)<=2^(80-13.5log2 n)<=2^-190.
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

## Coherent median, cleaning, and the declared larger quantum allocation

Let ell=ceil(log2 n), s=t+ell+10000, rho=2^18 s+1 (an O(t) odd integer).
Prepare rho independent private z/phase workspaces and perform the above
phase estimation and clamped integer computation on each, all controlled
by the same x if x is quantum. For each fixed computational x the private
inputs and circuits are a product, so the measured estimates are independent,
each correct with probability at least15/16. This assertion is in the ideal
Gamma reference, not a fresh-noise claim about the actual reused gradient.
Hoeffding's elementary bounded-variable bound makes a wrong median probability
at most delta=exp(-rho/4), uniformly in x. Ties among estimates are harmless.

Compute the median coherently without an oracle or stored sorting history.
Give pairs(value,index) their lexicographic total order. For each classical
candidate index i, count comparisons against all j in a log(rho+1)-bit
accumulator, using one clean reused w-bit comparator and ordinary controlled
increments. Under the flag that i has the median rank, XOR its w-bit value
into the external target. Reverse the comparisons/increments before the
next i. Exactly one i has the required rank. This costs polynomially many
fixed-arity gates and O(w+log rho) scratch beyond the stored estimates.
All i,j are CLASSICAL circuit-generation indices, not quantum table lookups.

Reverse all estimate arithmetic, phase estimation and private H preparations
after the median copy. The resulting circuit is a genuine unitary
C^dagger XOR_median C. On known-zero private workspace it approximates
|x,y> -> |x,y XOR M_x>, workspace0, with vector error at most2sqrt(delta).
Indeed the difference from copying M_x is supported on the bad-median
projection of norm at most sqrt(delta); conjugation preserves norms. This
bound holds for every x and every target state. Orthogonality of distinct x
extends it to superpositions and outside entanglement. The circuit is an
involution, so the same circuit supplies its inverse. No source preparation
is reversed. Reusing approximately clean scratch is handled by a complete
computation hybrid with ideal prefixes, not independent actual query errors.

There are O(rho*(t+qpeBits+w))=O(t^2)=O(n log2 n) quantum bits of stored
estimation work. We explicitly INCLUDE them in S_Q. A coherent median is
not claimed to use O(n) qubits. Product scratch is reused across estimates.
All classical input tables, emitted descriptions, counters and comparisons
are separately included in the main storage/work bounds.

## A private factor estimate for an arbitrary nonempty marked set

Before hashing, M may exceed Kcap. Use fresh PRIVATE uniform phase estimation
copies with the same precision, measure their full t+4-bit rounded value
U*beta*gamma^2, reset all private work, and take a classical median over rho
copies. The actual source phase index is not a control in this mode: the
predicate is determined solely by the already measured low key and classical
data. Measuring/resetting these private systems therefore does not measure
the source superposition or its unknown phase.

For all0<theta<=pi/2, M<=U theta^2<=4M. The eps phase error changes this
by at most sqrt(M)/16+1/65536, and the beta error is at most M/2^28 plus1/65536 (use
gamma<=2sqrt(M/U)+eps and2^-P<=1/(2^32 Kcap)). Rounding gives
an integer in[M/2,8M] on every good phase estimate; M=1 follows directly
from the strict lower bound before rounding. The median has that factor
accuracy except with probability delta. Output width t+4 covers all estimates.
Its outputs depend only on the predicate, hence on low labels/index hashes,
not on unused top source-label bits. The classical list uses O(t^2) bits.
All repetitions, resets and inverse gate work are charged; they acquire no
DCP source copies.

## Literal time blocks and error transfer

A Boolean predicate query is expanded in the main proof, not free. At most
rho*O(Tpe) such queries and a polynomial number of ordinary gates implement
one count/factor operation. Since Kcap=2^40n^2L,
Tpe<=2^38 n 2^(ceil((t+R)/2)), rho<=2^21t and t<=n,
an explicit deliberately loose core bound is
 gcount=2^1000 n^30 2^(ceil(t/2)+2R).
It includes each predicate's full literal-row gates, generated addresses,
integer arithmetic, median loops and all resets. The main proof supplies a
polynomial-per-row query bound and a larger nonrecursive G for all calls.

Reserve gcount core steps BEFORE invoking a count/factor block; abort if the
remaining core allowance is smaller. Pad a completed block to this fixed cost
with counted private no-ops. Thus no core cutoff interrupts a promised
unitary block. The ordinary bit work of checking/reserving this budget and
all monitor addresses is explicitly added in the main proof. A block abort
implies that the uncapped reference would exceed B, so Markov applies to the
same literal counted cost. Padding is not free and is included in gcount.

For analysis only, replace a wrong private factor estimate by the true M,
leaving accurate outputs untouched, and replace the approximate coherent count
by its exact XOR function. The pointwise failure bound and vector bound above
make the capped physical computation close to this idealized reference by
at most B*(delta+2sqrt(delta)). The reference still pays every full gcount
block: no oracle is granted to the physical program or charged for free.
All factor outputs in the reference meet their promises, allowing uniform
retry expectations. The main literal formulas give log2 B<=1024s. With
rho=2^18s+1 the total replacement error is below1/1024. The whole reference
comparison includes arbitrary adaptive histories and does not assume fresh
independent actual counting noise. The initial gradient replacement and
source-label coupling are charged separately and unconditionally.
