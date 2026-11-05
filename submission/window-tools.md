# A counted linear-space high-confidence phase window for MSR10

This helper uses the private known-register Grover circuits reproduced in
quantum-count-tools.md. It does not prepare or invert a source state.
Windowed phase estimation is standard context: Patel, Tan, Subasi and
Sornborger, arXiv:2403.18927v2; Greenaway, Pol and Sim, arXiv:2404.01396v2.
The sine-power window, preparation, Fourier estimate and implementation costs
needed here are proved explicitly below. No paper supplies a free window,
state-preparation oracle, source inverse, arbitrary rotation or accuracy bound.

## Window parameters and physical preparation

Let U=2^t, Kcap=2^40 n^2 L, J=ceil(sqrt(U Kcap)), rwin=1024n, an EVEN
integer, and tau=ceil(log2(2^16 rwin J)), T=2^tau. Set
w_k=sin^rwin(pi*k/T), k=0,...,T-1, and S2=sum_k w_k^2.
The ideal private window is |w>=sum_k w_k|k>/sqrt(S2).
All angles have dyadic denominators with tau<=2t<128n=p. The counted
ideal gradient implements them exactly by conditional translation, including
when controls are superposed. The actual gradient is compared once globally.

Start a private tau-bit register in H^tau|0>. Perform rwin Hadamard tests
of the known diagonal exp(2pi*i*k/T), each with one fresh/reset test qubit,
and require MINUS in all tests. For a fixed k, the joint amplitude multiplier
is ((1-exp(2pi*i*k/T))/2)^rwin, equal to a global scalar times
exp(pi*i*rwin*k/T)*w_k. Since rwin is even, subtract the known integer
frequency rwin/2 using gradient translations controlled by k to remove this
phase exactly. The accepted state is |w>. Each test diagonal is a sequence
of tau bit-controlled dyadic rotations, not an arbitrary unitary oracle.
One test ancilla is reused, and no test history is stored. Failed attempts
reset the entire private system and start again. They never touch a source.

For |x-1/2|<=1/(8sqrt(rwin)), sin(pi*x)>=1-1/(8rwin), by cos y>=1-y^2/2
and pi^2<16. Bernoulli gives sin^(2rwin)(pi*x)>=3/4 there. Since
T>=16sqrt(rwin), at least T/(8sqrt(rwin)) grid points lie in that interval.
Thus S2>=T/(16sqrt(rwin)), so a complete preparation attempt succeeds with
probability at least1/(16sqrt(rwin)). Use at most Awin=2^20n^2 attempts,
then abort and output zero. Even failed tests/attempts, resets, private coins,
classical controls and all dyadic gate-generation work are charged. Abort
probability is at most exp(-Awin/(16sqrt(rwin)))<2^(-100n) for n>=2^20.
The cap and all state widths are finite integers, independent of the secret.

Prepare one GLOBAL window before counting. The coherent count circuit below
returns the ideal reference window unchanged. Its approximate physical reuse
is justified by a whole-computation hybrid, not an invariance claim about
the imperfect actual workspace. A separate fresh private window is prepared
for each measured factor estimate; it is reset after that estimate. At most
a constant number of tau-bit window registers are live.

## An elementary exponentially small Fourier tail

Extend f(x)=sin^rwin(pi*x) on[0,1] by zero outside. Its derivatives of order
less than rwin vanish at both endpoints. Its exponential expansion has sum
of absolute coefficients1 and all frequencies at most rwin/2. Hence
integral_0^1 |f^(rwin)(x)| dx <=(pi*rwin)^rwin.
For F(v)=integral_0^1 f(x)exp(2pi*i*v*x) dx, integrate by parts rwin times:
 |F(v)| <=(rwin/(2|v|))^rwin for v!=0.
This is a bound on a finite explicit function, not on an assumed oracle.

For real v define g_v(x)=f(x)exp(2pi*i*v*x) on[0,1] and extend periodically.
Its continuous first derivative and integrable second derivative give an
absolutely convergent Fourier series. (Two integrations by parts bound its
integer coefficients by a constant times1/j^2.) The coefficients are
F(v-j). Evaluating the absolutely convergent series at k/T and summing the
finite grid gives the exact identity
 sum_(k=0)^(T-1) f(k/T)exp(2pi*i*v*k/T)=T sum_(j in Z) F(v-jT).
The interchange is justified by absolute convergence. The left side is
unchanged when v is shifted by an integer multiple of T.

For a Grover eigenphase nu and Fourier outcome a, let v=Tnu-a wrapped to
[-T/2,T/2]. Outside circular error eps=1/(2^10 J), |v|>=T eps.
Using the derivative estimate on j=0 and |v-jT|>=(|j|-1/2)T otherwise,
with eps<=1/2 and sum_(j!=0)(|j|-1/2)^(-rwin)<4*2^rwin,
gives the loose bound
 |sum_k f(k/T)exp(2pi*i*v*k/T)| <=5T*(rwin/(T eps))^rwin.
In fact retaining the factors2 improves it; the displayed slack suffices.
With window input and inverse binary Fourier transform, outcome probability
is this squared modulus divided by T*S2. The normalization bound therefore
gives probability at most400sqrt(rwin)*(rwin/(T eps))^(2rwin) per outcome.
Summing at most T outcomes and T eps>=64rwin bounds total bad-phase weight by
 delta=400T sqrt(rwin)64^(-2rwin) <2^(-100n).
Here tau<=2t<=2n, rwin=1024n and n>=2^20 make the last inequality explicit:
log2(delta)<=log2(400)+2n+log2(rwin)/2-12288n<-100n.
The same bound holds for both conjugate Grover eigenphases and their
orthogonal superposition, including the deterministic zero-count endpoint.

## Clean coherent counting, factor readout, and storage

Use the global |w> as the phase register, private H^t|0> for the counting
index, the explicit controlled Grover powers, and the inverse dyadic Fourier
circuit. All powers take O(T) literal predicate queries. Fold the phase
outcome and compute the exact rounded/clamped integer U*beta*gamma^2 by the
reversible schoolbook circuit in quantum-count-tools.md. Its small-angle,
phase-error and beta-error proof is unchanged: good phase weight yields the
EXACT bounded count. No coherent median array is used.

Writing C for this known circuit (without preparing the window), apply
C^dagger XOR_count C. On reference workspace |w> tensor |0> it approximates
XOR of the true count by vector error<=2sqrt(delta), uniformly for arbitrary
comparison inputs, target values and outside entanglement. The proof projects
onto the bad integer-count outcomes before the copy and uses norm contraction.
Distinct comparison encodings are orthogonal, so the uniform pointwise bound
extends to superpositions. In the ideal reference, the private window and
zero scratch are returned unchanged. The physical circuit is an involution;
its own reversed gates implement its inverse with the SAME window register.
The ideal-prefix telescoping bound handles all reuse without assuming fresh
actual counting noise or conditioning the actual workspace to be pristine.

For a private arbitrary-size factor estimate, prepare a separate bounded-
attempt window, use the full t+4-bit rounded output instead of clamping,
measure it and reset the private system. The count helper proves that good
phase weight gives a value in[M/2,8M] for any nonempty marked set. This
private predicate contains only low metadata and no physical source index.
No factor-median list or coherent repeated estimates are needed. Its fresh
preparation abort and bad estimate each cost at most2^(-100n), without
claiming that the approximate actual gradient remains pure after previous uses.
All these calculations take place in the one ideal-gradient reference.

## Full cost and unconditional replacement bound

Window preparation needs at most Awin*rwin*tau polynomial-many dyadic tests,
including resets and classical circuit generation. It uses O(n) qubits.
Since T<=2^17rwin J, counting uses only an extra polynomial factor in n
relative to the ordinary phase circuit. The previous deliberately loose
 gcount=2^1000 n^30 2^(ceil(t/2)+2R)
still covers the full expanded query work, Fourier gates, integer arithmetic,
window preparation, capped failed attempts and padding. The larger node
allowance G is unchanged. The coherent global window is prepared before
any source/index-controlled count, inside the same core/source guard scheme.
Reserve each full block before it starts. A fresh factor-window abort simply
returns zero globally; its rare probability is charged, not retried for free.

The main proof gives the stronger uniform clock inequality log2 B<=n/8.
Thus at most B calls, preparation aborts and private factors together cost
less than B*(3*2^(-100n)+2*2^(-50n))<1/1024 in total channel/vector transfer.
The single global-window abort is included. The ideal reference pays every
full block at the same padded cost; no free count or state preparation is
granted to the physical program. Source labels and the initial gradient are
compared separately and unconditionally once, as in the main proof.

The phase register, counting index, product arithmetic, gradient and private
window registers each have O(n) qubits, with a constant number live. Unranking
history has O(t*(R+log n)) qubits, also O(n): t<=9sqrt(n log n)/8,
R<=2n^(1/4)sqrt(log n), and n^(-1/4)log n and n^(-1/2)(log n)^(3/2)
are uniformly bounded for n>=2^20 by elementary dyadic induction. The tree
stack uses O(n) qubits. No rwin*n-bit test history or median array is retained.
Thus MSR10 has O(n) peak quantum storage, including all inverse work and failed
attempts. Classical storage and all other leading envelopes are unchanged.
