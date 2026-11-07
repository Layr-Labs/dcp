# Polynomial-copy correlation decoding with an exact reversible Grover search

## Status and scope

This is an analytic algorithm submission, not an executed quantum experiment and
not a new-record or historical-novelty claim. It is independently prepared for
account ethvs. It does not reuse either account's prior Yukon candidates.
Phase estimation, Pauli measurements, reversible classical arithmetic and Grover
search are standard methods, identified below. We do NOT claim the research goal
2^{O(n^{1/3})}, a subexponential-time algorithm, or superiority to known DCP
algorithms. In particular the time growth index here is **1**, not 1/2.

We fix one algorithm CPG-512 for every N >= 2, s in Z/NZ and
n = ceil(log_2 N). It takes exactly m=512(n+2) fresh independent ideal source
copies and has unconditional full-secret success at least 2/3. All the following
are joint worst-case, all-branch bounds in the protected uniform Clifford+T,
classical bit-operation model:

* T = O(2^{n/2} n^{20});
* S_C = O(n^{16}) allocated classical bits;
* S_Q = O(n^8) allocated qubits;
* Q = m <= 1536n, hence O(n) acquired copies.

The polynomial factors are deliberately conservative proved upper envelopes,
not fitted runtimes, optimized space claims or a dominance claim. No bound on
actual optimal running time is inferred. No QRAM, inverse source circuit,
purification, coherent source access, subset-sum or hidden-shift oracle is used.
Only the supplied fresh mixed-state copies are acquired.

## 1. An exact latent-label decomposition (not a physical oracle)

Put omega=exp(2 pi i/N) and
|chi_k> = N^{-1/2} sum_{x=0}^{N-1} omega^{-kx}|x>, k=0,...,N-1.
Let U_N be addition of 1 modulo N on the valid residue subspace; on unused
computational basis states x>=N it is the identity. This is a permutation of
all n-bit strings. U_N|chi_k> = omega^k|chi_k>.
Direct expansion of the specified input mixed state gives

rho_s = (1/N) sum_k |phi_{k,s}><phi_{k,s}| tensor |chi_k><chi_k|,
|phi_{k,s}> = (|0> + omega^{ks}|1>)/sqrt(2).                    (1)

Indeed <chi_k|x> = omega^{kx}/sqrt(N); in a coset vector the
relative coefficient of |1> is omega^{ks}, and averaging x eliminates all
k != k' blocks. Formula (1) describes the actual density matrix. We neither
observe the unavailable x nor request a purification. Each copy can be
analyzed as having an independent uniform latent k. Operations that are
diagonal in the chi basis preserve phi even when their measured estimate of k
is wrong.

## 2. Label measurement using implementable modular phase estimation

Set r=n+ceil(log_2(4096m)), L=2^r. For each fresh copy:

1. Initialize r zero phase-estimation qubits and apply H to all of them.
2. Apply the r classically chosen controlled permutations
   U_N^{2^j}, j=0,...,r-1, with the ordinary phase-estimation bit ordering.
3. Apply the inverse r-qubit binary Fourier circuit, measure its register to
   obtain y in {0,...,L-1}, and set k_hat to the nearest integer to Ny/L,
   reduced modulo N. Use a fixed deterministic rule for ties.
4. Discard/reset the residue and phase-estimation registers. Choose a fair
   basis a in {X,Y} using H followed by a basis measurement on a fresh zero
   qubit, measure the first coset qubit in that basis, and retain b=+1 or -1.
   X measurement is H then Z; Y measurement is S-dagger then H then Z.
5. Save the classical record (k_hat,a,b). Recycle all quantum workspace.

There are exactly m records, independent between source acquisitions.
For the moment use ideal inverse Fourier rotations. On an eigenvector chi_k,
phase estimation has output probability

p_y = | L^{-1} sum_{j=0}^{L-1} exp(2 pi i j(k/N-y/L)) |^2.

If d_y is the circular distance from y to Lk/N, 0<d_y<=L/2, then
p_y <= 1/(4d_y^2), because |sin(pi d_y/L)|>=2d_y/L and the
numerator of the geometric-series formula is at most 1 in magnitude.
Incorrect nearest-integer decoding requires d_y>=D=L/(2N).
There are at most two outcomes in each unit-distance shell, so comparison with
sum_{j>=floor D} 1/j^2 gives a tail <=1/(D-2)<=2/D for D>=4.
We retain the still looser bound 8N/L. Since L>=4096m N, the
probability of a wrong k_hat on each copy is <=1/(512m).
A union bound gives probability <=1/512 of any wrong label.
The bound holds for every N and k, including non-powers of two and labels near
0; distances and nearest-integer rounding are circular.

All controlled U_N^{2^j} are implemented, not given as free black boxes.
Their offsets 2^j mod N are produced by r modular doublings. Addition of a
known offset modulo N, with identity on x>=N, and its inverse are ordinary
O(n^2)-size Boolean circuits using comparison, addition and conditional
subtraction. A clean reversible implementation can compute the permutation
into a second register, swap, and uncompute with the inverse permutation.
Lifting a bounded fan-in Boolean circuit to Toffoli/CNOT/X, retaining its
intermediate bits and reversing them, uses O(n^2) gates and workspace here.
Controlled versions add only a constant-factor cost per gate. No control of
source preparation is used. Toffoli has an exact constant-size Clifford+T
implementation with clean ancillas, which are counted and reset.

### Clifford+T implementation and precision

There are at most 4r^2 single-qubit phase rotations in a decomposition of the
inverse binary Fourier circuit into one-qubit phase rotations and exact
CNOT/H gates. Controlled phase diag(1,1,1,e^{i alpha}) decomposes into
P(alpha/2) on control and target, CNOT, P(-alpha/2) on target and CNOT;
P differs from R_z by a global scalar, which is immaterial in this un-controlled
one-qubit decomposition. The desired angles are dyadic rational multiples of
pi of description length O(r), computable by charged classical arithmetic.
Approximate every such rotation in operator norm, up to a global scalar, to

eta = 1/(65536 m r^2).

A constructive finite-gate compilation fact used here is the usual deterministic
Solovay--Kitaev algorithm for an inverse-closed finite algebraic universal
single-qubit gate set (H,T, with T-dagger=T^7). For a computable target angle
with O(r) bits of symbolic description and tolerance eta, a conservative
bound adequate here is O(p^4) output gates and O(p^{12}) classical bit work
and workspace, p=O(r+log(1/eta)+1). This is an upper bound, not a gate-optimal
synthesis assertion. The original length exponent is log(5)/log(3/2)<4.
The recursion depth is O(log p), the commutator error improves from e to
O(e^{3/2}), and the five recursively approximated words give the p^4 length
bound. Matrix products, square roots and commutator axes can be evaluated
with O(p) guard precision by interval arithmetic; even charging O(p^4)
bit work per elementary numerical step and conservatively O(p^4) such steps
fits the p^{12} bound. The fixed coarse algebraic gate net is generated by
finite enumeration anew and charged; it is a constant independent of N,s,
not instance-dependent advice or a preloaded quantum table. Inverses are
realized within the same finite gate set. This is constructive gate synthesis,
not an additional problem oracle.

Reference for this compilation fact and recurrence: C. M. Dawson and
M. A. Nielsen, "The Solovay-Kitaev algorithm", Quantum Information & Computation
6(1), 81--95 (2006), arXiv:quant-ph/0505030, algorithm and error/length analysis.
The needed theorem, gate set, precision and applicability are specified here;
no external text is needed to supply a DCP algorithm or a missing success lemma.
The arithmetic of rational and algebraic gate entries uses finite precision,
not free exact real arithmetic. A depth fixed from eta and guard precision
fixed from p provide a branch-independent synthesis bound.

Across all m label measurements there are at most 4mr^2 approximated rotations.
The telescoping operator-norm/channel hybrid bound, followed by measurement,
gives total variation from the ideal joint record distribution at most
2*(4mr^2)*eta = 1/8192. A coupling with the latent, correctly labeled ideal
records therefore fails with probability at most
1/512+1/8192 < 1/256. No approximation is used in the later Grover oracle.
The couplings are proof devices, not executable resources or postselection.

## 3. A uniform correlation gap for every competing shift

For t in Z/NZ define
f_t(k,X)=cos(2 pi kt/N), f_t(k,Y)=sin(2 pi kt/N).
In the correctly labeled ideal model,
E[b | k,a]=f_s(k,a). For the bounded random variable Z_t=b f_t(k,a),

E Z_t = (1/(2N)) sum_k [cos(2 pi ks/N)cos(2 pi kt/N)
                       +sin(2 pi ks/N)sin(2 pi kt/N)]
      = (1/(2N)) sum_k cos(2 pi k(s-t)/N)
      = 1/2 if t=s, and 0 otherwise.                         (2)

This is an exact finite-group character identity for every N and s. It
assumes neither a pseudorandom output nor coprime k or t. For each fixed t,
the m variables are independent and lie in [-1,1]. Write A_t=m^{-1}sum_j Z_t.
Hoeffding's inequality gives

Pr(A_s<3/8) <= exp(-m/128),
Pr(A_t>1/8) <= exp(-m/128), t!=s.

Union bounding over the N candidates, including s, the event E that
A_s>=3/8 and all A_t<=1/8 has probability at least
1-N exp(-m/128) >= 1-1/128. The last inequality follows from
N<=2^n and m=512(n+2): exp(n ln2-4(n+2))<1/128 for n>=1.
The competitor scores need not be mutually independent; the union bound does
not require that. This is full-secret separation, not recovery of one bit.

## 4. An exact finite Boolean predicate from the measured classical data

The later search never consults another quantum source copy. All its arithmetic
is exact integer/rational arithmetic with bounded bit lengths.
Set pi_0=3141592653589793/10^15. Machin's identity
pi=16 arctan(1/5)-4 arctan(1/239), and 20 alternating-series terms in each
arctangent, certify |pi_0-pi|<10^{-14}. These are constant-sized rational
computations, counted in preprocessing. For z=kt mod N let v=2 pi_0 z/N;
0<=v<7. Use

C(v)=sum_{h=0}^{20} (-1)^h v^{2h}/(2h)!,
S(v)=sum_{h=0}^{19} (-1)^h v^{2h+1}/(2h+1)!.

Taylor's theorem bounds their errors by 7^{42}/42! and 7^{40}/40!, respectively,
both <2^{-20}. The change from pi to pi_0 contributes at most 2*10^{-14}
by the Lipschitz bound for sine/cosine. Let q_t(k,a) be the exact signed integer
floor(4096*C(v)) or floor(4096*S(v)) for basis X or Y. Consequently

|q_t(k,a)/4096 - f_t(k,a)| < 1/1024.                         (3)

Floor for negative values is Euclidean floor, not truncation toward zero.
Define the exact Boolean predicate on the n-bit candidate register:

F(t)= [t<N and 4 sum_{j=1}^m b_j q_t(k_hat_j,a_j) > 4096m].  (4)

For t>=N set F(t)=false. On event E and correctly coupled records,
the score for s is >=3/8-1/1024>1/4 while every other residue has score
<=1/8+1/1024<1/4. Thus F has exactly one marked n-bit string, namely s.
There are no ambiguous score ties on this event. On other records F is still
a well-defined finite Boolean function and all resource bounds remain true.

For completeness, this predicate is an implementable reversible circuit.
Each exact polynomial has degree at most 40; its rational numerator and
common denominator have O(n) bits, since N and pi_0's denominator are the
only nonconstant denominators and the degree is fixed. Modular multiplication,
polynomial evaluation, signed integer division/floor, accumulation and the
final comparison can be expressed as bounded straight-line schoolbook Boolean
circuits. Each O(n)-bit product or division costs O(n^2) elementary Boolean
operations; there are O(m)=O(n) fixed-degree evaluations. Allowing all
bookkeeping, comparisons and bit-length guards, the circuit has O(n^4)
Boolean gates. Every input data record and gate description has explicitly
bounded length; accumulation needs O(log(m+2)) extra bits.

A standard retained-history reversible lift computes each Boolean gate into a
new clean work bit using at most a constant number of Toffoli/CNOT/X gates.
It retains O(n^4) intermediate bits, flips a phase ancilla |-> conditioned
on F, and reverses all computation. This yields the exact phase oracle
|t> -> (-1)^{F(t)}|t>, with O(n^4) gates, O(n^4) clean work qubits and
O(n^4 log(n+2)) stored gate-description bits. Classical data are compiled
as ordinary gate constants into this one circuit; there is NO quantum-indexed
lookup, QRAM or free memory access. Its uniform generation is counted.
Integer arithmetic is finite, not a unit-cost arbitrary-integer primitive.

## 5. A cutoff Grover search, with independently bounded every-branch work

For n<=4 enumerate t=0,...,N-1, evaluate (4) classically, and return the
first marked residue, or 0 if none. This finite prefix has bounded work,
requires no additional samples, and succeeds on the same event E.

For n>=5 let M=2^n, theta=arcsin(M^{-1/2}), and
A=pi/(4 theta)-1/2. Compute a rational A_hat with |A_hat-A|<=1/16,
choose the nearest nonnegative integer R to A_hat, and FIX this R before any
Grover attempt. Hence |R-A|<=9/16. Use at most THREE attempts:

* initialize the n candidate qubits to the uniform superposition with H;
* perform exactly R ordinary Grover iterations with the exact phase oracle
  from (4) and the exact diffusion 2|+><+|-I;
* measure t, check (4) classically, and if t<N and F(t) is true output t;
  otherwise reset all qubits and proceed to the next bounded attempt.

After three unverified outcomes return 0. There is no unbounded repeat-until-
success loop. The multi-controlled phase in diffusion has an O(n)-size
clean-ancilla Toffoli implementation, so the whole search is exactly Clifford+T.
Only the initial sample label circuits were approximated.

A_hat is computed without free real arithmetic. One explicit procedure uses
p=16n+512 fixed-point interval bits. Obtain sqrt(2) by p-step bisection when
n is odd, and x=M^{-1/2} otherwise by an exact power of two. Bound arcsin(x)
by 4n+64 terms of its positive series
sum_{h>=0} binom(2h,h)x^{2h+1}/(4^h(2h+1)); for x<=1/sqrt(32), its
tail is bounded by x^{2J+3}/(1-x^2) after J terms. Bound pi using p terms of
the two alternating Machin series. Outward-rounded p-bit rational interval
operations with O(n) guard bits give an interval for A of width below 1/8:
x>=2^{-n/2}, the reciprocal derivative contributes at most an absolute
constant times 2^n, while accumulated rounding and the stated tails are
smaller than 2^{-4n-100}. Use the midpoint as A_hat. All these series lengths,
bisection counts, precisions and arithmetic operand lengths are O(n), fixed
before outcomes, so their bit work and workspace are polynomial in n.
This is a specified precision schedule, not an assumed unit-time arcsine or
an unbounded test for transcendental equality. The rounding of R need not
identify the exact floor of a transcendental number.

Condition on E and correct record coupling. There is exactly one marked item.
The standard two-dimensional Grover rotation calculation gives success
sin^2((2R+1)theta). It follows directly by writing the uniform state as
sin(theta)|s>+cos(theta)|unmarked>, and multiplying the two reflections.
For n>=5, theta<1/5 (sin(1/5)>1/sqrt(32)), and

|(2R+1)theta-pi/2| <= (9/8)theta <9/40.

Since cos^2 u>=1-u^2, one attempt has success >3/4. Reinitializing creates
the same conditional distribution on the next attempt. The verification
accepts no other candidate on E, so conditional failure of all three attempts
is <=(1/4)^3=1/64. Also R<=2 sqrt(M), an outcome-independent finite cutoff.

Combining the statistical failure <=1/128, label/compilation coupling failure
<1/256, and conditional Grover failure <=1/64, total failure is at most
1/128+1/256+1/64=7/256<1/3. Therefore for every N,s the entire s is output
with unconditional probability at least 249/256, in particular at least 2/3.
The weaker >=2/3 guarantee is used in every claim. Failure executions are
included in the following upper bounds and consume no extra samples.

## 6. Joint all-branch resource accounting

There are no instance-dependent nonuniform constants. All claimed O constants
are absolute. N needs at most n+1 input bits; source registers use n+1 qubits.
The algorithm fixes m=O(n), r=O(n) (indeed r<=32n for n>=1), eta^{-1}=poly(n),
p=O(n), and all integers in fixed-degree score arithmetic have O(n) bits.
Every loop bound and circuit-generation precision is fixed from N,n, before
sample outcomes.

Preprocessing includes generation and synthesis of the entire label circuit,
all modular offsets, its stored gate list, the score oracle and R; it is not
free. The synthesis bound above, multiplied by O(r^2) rotations, is O(n^{14})
classical bit work. All saved synthesis work, output words, rational intervals
and indexed gate descriptions fit O(n^{16}) classical bits conservatively.
Label acquisition executes m circuits, each with O(n^3) exact modular gates
and O(r^2 p^4)=O(n^6) synthesized gates. Count source cost m(n+1), gates,
measurements, classical label decoding and random basis initialization; their
sum, even after charged address operations and all temporary bit bookkeeping,
is O(n^{16}). Saved records need O(m(n+2))=O(n^2) classical bits.

The uniformly generated exact Boolean phase oracle has O(n^4) gates and
O(n^4) history qubits; the gate descriptions have O(n^5) bits as a loose
bound. Sample arithmetic uses no more workspace than its lifted circuit.
The sample registers and label synthesis do not accumulate quantum states
between acquisitions. Peak quantum storage is bounded conservatively by
O(n^8), including coset inputs, phase registers, reversible modular-arithmetic
ancillas, every oracle history bit, diffusion ancillas and initialization.
Peak classical storage, including the controller, N, counters, all records,
stored complete circuits and synthesis work, is O(n^{16}).

M_alloc=O(n^{16}) total allocated bits/qubits, so every classically addressed
access/gate pays O(log(n+2)) address-bit work. The constant implicit in
M_alloc only contributes an absolute constant to this address length. All
gate and memory-access counts above include this factor within their loose
polynomial upper bounds, rather than treating addressing as free. Initializing
all allocated memory is charged. There is no locality/depth shortcut or
parallel work claim.

Every search execution performs at most three R<=2*2^{n/2} iterations,
with O(n^4) oracle/diffusion gates and bounded classical dispatch. Including
addressing, outcome verification, resets, data initialization, the controller
and all preprocessing, a uniform bound O(2^{n/2}n^{20}) is conservative:
O(n^{16}) preprocessing is absorbed, and per-iteration polynomial overhead
is smaller than n^{20}. The n<=4 finite classical branch is also absorbed by
one absolute O constant. There are exactly m acquired copies, not just m
accepted labels; wrong label estimates and failed Grover attempts are already
charged. The independent source's inaccessible internal state is the only
excluded storage, exactly as the contract prescribes.

## 7. Structured envelopes, growth indices and error tolerance

Use the representative envelopes
B_T=2^{n/2}n^{20}, B_C=n^{16}, B_Q=n^8, B_samples=n.
They describe the complete respective proved O bounds for the SAME CPG-512
configuration and the SAME unconditional >=2/3 guarantee.
For time, log_2 B_T=n/2+20log_2 n, and
log_2 log_2(max(4,B_T))/log_2 n ->1. The exact time growth index is 1.
For any fixed positive-degree polynomial, the numerator is O(log log n),
so the three polynomial resource indices are exactly 0.
The declared inner time coefficient 1/2 is explicit; there is no unsupported
2^{O(...)} hidden inner constant. Outer coefficient 1 is only the canonical
big-O representative and DOES NOT assert measured constant 1.

The fifth claim's fractional error tolerance is epsilon(n)=0. Its error model
requires every acquired copy to be an independent ideal rho_s for the same
s. It asserts the joint guarantee under this promise; it makes no assertion
about malformed copies or the impossibility of positive tolerance. Gate
approximation errors are internal implementation errors already covered above,
not a promise of corrupted-source robustness. There is no fifth numeric score.

## 8. Attribution and limits

The source problem, resource model and admission schema are the organizer's
pinned rules.md at cdb1ebff130d861e2c61e9cf517ab66c0a56ca7a.
Fourier sampling/phase estimation and Grover's two-reflection search are
standard quantum algorithms; the latter's rotation and cutoff proof is supplied
in section 5, the former's distribution and implementation in sections 1--2.
Finite-gate compilation uses the precise constructive Solovay--Kitaev fact
identified and charged in section 2. Hoeffding's bounded-independent-variable
inequality is applied with interval length 2, not an oracle or distributional
heuristic. Elementary reversible arithmetic, Taylor/Machin series and all
resource consequences needed for the stated bounds are detailed above.

No mathematical historical novelty, actual experiment, cryptographic break,
known-algorithm record, reward, full frontier dominance or attainment of the
organizer's 2^{O(n^{1/3})} goal is claimed. Equal time indices do not imply
equal full guarantees. This is a new account-B participation attempt with its
own proof snapshot; acceptance, promotion and any scientific novelty are for
independent review, not asserted by this submission.
