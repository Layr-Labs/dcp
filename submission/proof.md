# RST1: retained-block sequential shift testing

## Scope and provenance

For every integer N>=2 and fixed s in Z/NZ, set n=ceil(log2 N) and k=n+6.
The algorithm below recovers s with probability at least 49/64>2/3.
All source copies are independent ideal mixed states as specified in rules.md.
Only submission/ is changed. This is a concrete low-sample alternative to the
repository exhaustive baseline, not a new subexponential DCP algorithm.
The baseline controlled subtraction and its reversible arithmetic construction
are reused and sharpened below. The idea of reusing a coset-state block through
sequential subgroup tests is standard: see Ettinger, Hoyer and Knill,
Hidden Subgroup States are Almost Orthogonal, arXiv:quant-ph/9901034v1,
Theorem 1, Section 2 and Lemmas 2-4. Noncommutative sequential
measurement estimates are also standard; see Gao, Quantum union bounds for
sequential projective measurements, arXiv:1410.5688, Theorem 1, and
O'Donnell and Venkateswaran, The Quantum Union Bound made easy,
arXiv:2103.07827, Theorem 1.1. No external theorem is needed as a black box:
the weaker elementary inequality needed here is proved in full below.
This instantiation and charged accounting improve the supplied baseline's
full envelopes; no novelty over established polynomial-query HSP results is
asserted. Prior public sieve submissions are comparators, not material sources
for the algorithm or proof here. Their square-root time index is better than
our index 1; their displayed sample and memory guarantees are larger.

## The exact projective test

A copy occupies a control qubit and an n-bit data register. For each candidate
t in {0,...,N-1}, define U_t as controlled subtraction of t modulo N on valid
data strings y<N, identity on invalid strings y>=N. Let
A_t=U_t^dagger (|+><+| tensor I) U_t, extended to the whole encoded register.
It is an orthogonal projector. On the given source rho_s,
tr(A_s rho_s)=1 and tr(A_t rho_s)=1/2 for every t!=s.
Indeed U_t sends the pure component with offset x to
(|0,x>+|1,x+s-t mod N>)/sqrt(2). At t=s its control is |+>;
otherwise the data strings differ and its reduced control is I/2.
This calculation works for every x and thus for the mixture.

Acquire exactly k copies once, in state sigma=rho_s tensor-power k.
Put P_t=A_t tensor-power k. Then P_s sigma=sigma and
tr(P_t sigma)=2^(-k) for t!=s. Test P_t using one binary measurement,
without measuring individual sample control qubits:
apply U_t and H to each copy's control, compute the predicate that all k
controls are zero into one clean flag by a reversible AND chain, measure only
the flag, reverse the AND chain to clear its work and flag, then reverse all
H and U_t. On each observed outcome these operations implement exactly the
Luders instrument P_t or I-P_t on the retained block. To clear the measured
flag one may reverse the entire predicate computation, including the flag
XOR, on its outcome subspace. The flag becomes zero on both branches.
Individual controls are never measured. Otherwise the rejected-state map
would be a different instrument and the proof would not apply.

## Algorithm, every branch

Acquire k independent copies. For t=0,...,N-1 in increasing order perform
the preceding binary projective test on the same retained block. On outcome
P_t output t and halt. On I-P_t keep the resulting block and continue.
If the loop ends output zero. No restart, fresh test copy, source inverse,
purification access, Fourier transform, arbitrary rotation or postselection
is used. The fallback is specified even though no favorable property is
assumed about it. Every branch uses exactly k source calls and at most N tests.

## Elementary sequential-projection estimate

Purify sigma mathematically as a unit vector v; this inaccessible environment
is used only in the analysis. Extend every projector by identity there.
Let r be the integer representative of s. For i=0,...,r-1 define
Q_i=I-P_i, v_0=v, v_(i+1)=Q_i v_i, and d_i=P_i v_i.
Then v-v_r=sum_i d_i. Orthogonal projection gives the telescoping identity
sum_i ||d_i||^2=1-||v_r||^2<=1.
Also <v,d_i>=<P_i v,d_i>, so Cauchy-Schwarz on the direct sum yields

 |<v,v-v_r>| <= (sum_i ||P_i v||^2)^(1/2)
                       (sum_i ||d_i||^2)^(1/2) <= sqrt(a),
 a=sum_i ||P_i v||^2=r 2^(-k) < 2^n 2^(-(n+6))=1/64.

For r=0 the empty sequence has a=0 and v_r=v. Since P_s v=v,
|<v,P_s v_r>|=|<v,v_r>|>=1-sqrt(a)>=7/8.
Cauchy-Schwarz with unit v now proves
||P_s v_r||^2 >= (7/8)^2=49/64.
The left hand side is exactly the UNCONDITIONAL probability of rejecting
all smaller candidates and then accepting s. That event outputs the entire
correct secret. Early wrong outputs, true-test rejection, and fallback may
all fail and are already included in the complement. No independence between
successive tests on the disturbed block is assumed. The estimate is uniform
in every N and s, including N=2 and n=1.

## Exact uniform arithmetic and circuit generation

On n-bit data define f_t(y)=y-t modulo N for y<N and y otherwise.
It is a permutation with inverse g_t(y)=y+t modulo N on the valid range,
identity elsewhere. Boolean circuits with O(n) gates and O(n) wires implement
both, using a fixed number of ripple comparisons, additions and subtractions
on n+1 bits and bitwise selection. For example compare y<N and y<t;
for valid y select y-t if y>=t and y+N-t otherwise. The carry/borrow
recurrences each use fixed-size Boolean gates per bit. Invalid y is selected
unchanged. The inverse uses y+t and comparison with N. All integers have
O(n) bits; nothing uses unit-cost arbitrary precision.

Retain intermediate Boolean gate values, XOR the output into a target, and
reverse the evaluation to clear intermediates. This gives a reversible
compute-XOR circuit of O(n) gates and work qubits. To implement f_t in place,
compute f_t into zero, swap input and output, then XOR g_t of the new input
into the old input, clearing it. The control-0 alternative is identity.
This yields exactly U_t, with O(n) gates and ancillas, and its inverse is
implemented by reversing these gates. Every Boolean gate has constant arity;
NOT/CNOT/Toffoli implement it with a constant overhead, and Toffoli has an
exact constant-size Clifford+T decomposition. There is no precision error
or synthesis parameter. Work ancillas are zero when U_t finishes.

A reversible k-fold AND needs O(k) Toffoli gates and O(k) clean scratch bits:
negate the controls, compute successive prefix ANDs, copy the last prefix
to the flag and reverse the prefixes; undo negations. Reverse this predicate
circuit after measurement as specified above. For k>=2 this uses a simple
linear chain; here k>=7. Thus the complete P_t instrument uses O(kn+k)=O(n^2)
logical gates, O(n) additional scratch qubits beyond the O(kn) retained block,
and one flag measurement per candidate. Ancillas are reused across copies.
Every source acquisition costs n+1; the k acquisitions cost O(n^2).
Initialization, reset and final disposal use at most the stated work budget.

Generate circuits as streamed instructions, never a length-N stored program.
The controller holds N,t, copy/bit indices and a constant number of counters,
each O(n) bits or fewer. A local arithmetic circuit may be stored with its
O(n) gates and O(log(n+2))-bit local wire indices; this takes O(n log(n+2))
classical bits and at most O(n^2) charged work to generate. Its inverse uses
the same description in reverse. For each invocation, compute the global
wire index from the copy base plus local offset using O(log(n+2))-bit
arithmetic. The retained block and all other allocations are polynomial:
M=O(n^2) bits plus qubits. Address length is consequently O(log(n+2)).
Allow O(log^2(n+2)) bit work per logical gate for decoding the local record,
computing wire indices, controller counters and their own addressed accesses,
as well as the model's separate O(log(M+2)) address charge. Elementary ripple
arithmetic on these indices fits that allowance. Local generation costs
O(n^2) per candidate, candidate increment O(n log(n+2)) at worst, and reading
all n bits of t for the arithmetic description is included. These estimates
are deterministic uniform bounds, independent of measured outcomes.

Total work per binary test is O(n^2 log^2(n+2)), including arithmetic,
addresses, measurement, branch handling and resetting. Since
log^2(n+2)=O(n) for positive integer n, a supported conservative polynomial
envelope is O(n^3). There is no large-memory address hidden in this step.
Hence the jointly declared bounds, on EVERY branch, are

 T=O(N n^2 log^2(n+2)) subseteq O(2^n n^2 (log2 n)^2) for n>=2,
 S_C=O(n log2 n) bits for n>=2, S_Q=O(n^2) qubits,
 Q=k=n+6=O(n).

We declare the sharper logarithmic time envelope, which is supported by the
structured contract. Classical space is O(n log(n+2)): the O(n log(n+2))
local gate description, N,t and constant-many O(n)-bit counters dominate;
there is no classical array of quantum amplitudes or saved transcript. Thus
O(n log2 n) holds for n>=2. The n=1 branch has fixed absolute cost and space.
Absolute outer constants handle all small n. There are no expected-time
loops or unbounded retries. The environment used to purify sigma is not
allocated accessible memory; its size has no implementation role.

## Indices, structured envelopes and error model

For B_T=2^n n^2 (log2 n)^2, log2 B_T=n+2 log2 n+2 log2(log2 n),
so the exact growth index is 1. For B_C=n log2 n, B_Qspace=n^2 and
B_samples=n the double logarithm divided by
log2 n tends to zero; all three indices are exactly 0. Outer constant
multipliers do not affect these limits. The four structured envelopes are
therefore 2^n n^2 (log2 n)^2, n log2 n, n^2 and n (n>=2). All concern the same configuration k=n+6.
The tolerance law is tau(n,Q)=0, where the actual acquired count is Q=n+6.
Every acquired copy must be an independent ideal coset state. No guarantee
is asserted for malformed copies; zero is a guarantee, not an impossibility
result. The unconditional success and resource proof applies jointly under
exactly this clean-input model.

Relative to the original repository baseline, time improves from the proved
2^n n^4 envelope to 2^n n^2 (log2 n)^2; classical space improves from n^2
to n log2 n, the quantum workspace envelope is unchanged, and
sample count improves from 2^n n to n. These compare upper guarantees,
not tight lower bounds on either program. This is not dominance over
square-root-time sieve submissions: their time is better and their currently
declared storage/sample bounds are worse. It does not prove the cube-root
research goal or a new fastest DCP algorithm. Its purpose is an explicit,
self-contained polynomial-sample and polynomial-space frontier alternative.
