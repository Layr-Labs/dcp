# Reused coset tests with amplitude amplification

For every integer N >= 2, let n = ceil(log2 N), L = 2^n, and k = n+24.
The unknown shift is s in Z/NZ. This algorithm uses exactly k independent
ideal source copies on every execution branch. It recovers the full s with
probability at least 2/3. All resource bounds below refer to this one algorithm.

The one-copy test below is the test from the supplied exhaustive-search
baseline. Here its acceptance test is used as a coherent reflection, and the
same k copies are used in all iterations. The proof supplies the required
reflection and error bound. It does not assume an external search oracle.
No claim of novelty or of the research target 2^{O(n^{1/3})} is made.

## Algorithm

Acquire k copies and retain them. Each copy has a first qubit and an n-qubit
residue register. No source inverse, source control, offset x, or purification
is used by the algorithm.

If n=1, then N=2. Apply a Hadamard to the first qubit of each copy and measure
these k qubits. Output 0 if all outcomes are 0, and output 1 otherwise.

For n>=2, create an n-qubit candidate register in

$$
|u\rangle=L^{-1/2}\sum_{t=0}^{L-1}|t\rangle.
$$

Set r = floor(3 sqrt(L)/4). Compute this integer exactly as
r = floor(isqrt(9L)/4), where isqrt denotes the nonnegative integer square root.
Apply r repetitions of the following two operations, then measure the candidate
register. Return its value if it is below N, and return 0 otherwise.

1. Apply the reflection R defined and implemented below.
2. Apply D = 2|u><u| - I to the candidate register.

There are no restarts, early exits, or measurement-dependent loops in this branch.

## One-copy test and the reflection

For 0<=t<N, define a permutation of all n-bit strings by

$$
f_t(y)=\begin{cases}(y-t)\bmod N,&y<N,\\y,&y\ge N.\end{cases}
$$

Let C_t apply f_t to a residue register if its first qubit is 1, and let
V_t = (H tensor I) C_t. Define the acceptance projector

$$
A_t=V_t^\dagger(|0\rangle\langle0|\otimes I)V_t,
\qquad P_t=A_t^{\otimes k}.
$$

For a source component with offset x, C_t gives

$$
\frac{|0,x\rangle+|1,(x+s-t)\bmod N\rangle}{\sqrt2}.
$$

If t=s, V_t puts the first qubit in state |0>. If t!=s, the two
residue basis states are distinct, so a measurement of this qubit after V_t
has outcome 0 with probability exactly 1/2. Thus, for the clean mixed source,

$$
\operatorname{Tr}(P_s\rho_s^{\otimes k})=1,
\qquad
\operatorname{Tr}(P_t\rho_s^{\otimes k})=2^{-k}\quad(t\ne s).
\tag{1}
$$

Independence of the k source copies gives the second equality.

The implemented reflection is

$$
R=\sum_{t<N}|t\rangle\langle t|\otimes(I-2P_t)
 +\sum_{N\le t<L}|t\rangle\langle t|\otimes I.
\tag{2}
$$

To implement it, compute a flag [t<N]. For each saved copy, apply C_t
conditioned on this flag, and then apply H to its first qubit. Change the sign
if the flag is 1 and all k first qubits are 0. Undo these Hadamards and
controlled permutations, and clear the flag. All arithmetic scratch qubits
are cleared. On a candidate t>=N the sign change is disabled, so the full
operation is the identity. On t<N it is I-2P_t. The data registers are not
measured or replaced in these iterations.

## Success probability

A purification is used only to prove the error bound. It is not an input
or an operation of the algorithm. Write a normalized purification of the
retained state as

$$
|\Phi_s\rangle=\bigotimes_{j=1}^k
 \left(N^{-1/2}\sum_{x=0}^{N-1}|x\rangle_{E_j}|\psi_{x,s}\rangle\right).
$$

Extend all actual operations by the identity on E. Equation (1) implies

$$
P_s|\Phi_s\rangle=|\Phi_s\rangle,
\qquad \|P_t|\Phi_s\rangle\|=2^{-k/2}\quad(t\ne s).
\tag{3}
$$

For comparison define the ideal operation
R_* = (I-2|s><s|) tensor I. This is a mathematical comparison only.
For any normalized candidate state |v> = sum_t a_t |t>, orthogonality of
the candidate basis states and (3) give

$$
\|(R-R_*)(|v\rangle|\Phi_s\rangle)\|^2
 =4\sum_{\substack{t<N\\t\ne s}}|a_t|^2 2^{-k}
 \le4\,2^{-k}.
\tag{4}
$$

Set W=DR and W_*=DR_*. A telescoping expansion gives

$$
W^r-W_*^r
 =\sum_{j=0}^{r-1}W^{r-1-j}(W-W_*)W_*^j.
$$

Every ideal intermediate state W_*^j|u>|Phi_s> is a candidate state
tensored with the unchanged |Phi_s>. All other factors in the expansion
are unitary. Equation (4) and the triangle inequality therefore give

$$
\|W^r|u\rangle|\Phi_s\rangle-W_*^r|u\rangle|\Phi_s\rangle\|
 \le2r\,2^{-k/2}
 \le\frac32\sqrt L\,2^{-k/2}=\frac3{8192}.
\tag{5}
$$

This argument allows arbitrary changes to the saved state during the actual
computation. It does not apply a fresh-copy assumption at later iterations.

For completeness, the ideal success bound follows directly from two dimensions.
Let theta = arcsin(1/sqrt(L)), and let |b> be the normalized uniform sum
of candidates other than s. Then
|u> = sin(theta)|s> + cos(theta)|b>. In the ordered basis (|s>,|b>),
multiplication of D with diag(-1,1) gives

$$
W_* =\begin{pmatrix}\cos(2\theta)&\sin(2\theta)\\
-\sin(2\theta)&\cos(2\theta)\end{pmatrix}.
$$

Thus the ideal probability of measuring s after r iterations is
sin^2((2r+1)theta). Put a=1/sqrt(L), so 0<a<=1/2 for n>=2.
The elementary bounds

$$
a\le\arcsin(a)\le(\pi/3)a
$$

follow from the derivative of arcsin and its convexity on [0,1/2];
the upper bound is the chord from (0,0) to (1/2,pi/6).
The definition of r now gives

$$
1\le\frac32-a\le(2r+1)\theta
 \le(\pi/3)(\tfrac32+a)\le2\pi/3.
$$

On [1,2pi/3], the minimum of sin^2 is at an endpoint. Also
sin(1)>=1-1/6=5/6: integrate cos(z)>=1-z^2/2 on [0,1].
The cosine inequality follows from
1-cos(z)=2sin^2(z/2)<=z^2/2 and |sin(w)|<=|w|.
Consequently the ideal probability is at least
min(25/36,3/4)=25/36.

For normalized pure states |p>,|q> and any event projector E,

$$
|\langle p|E|p\rangle-\langle q|E|q\rangle|
 \le2\|p-q\|,
$$

by expanding the difference and applying Cauchy--Schwarz.
Apply this to the event that the measured candidate is s, including the
purifying registers. Equation (5) proves actual success at least

$$
\frac{25}{36}-\frac3{4096}>\frac23.
\tag{6}
$$

Mapping invalid measured candidates to 0 cannot decrease this bound.
Tracing out the unused purifying registers gives the same measurement
probabilities for the specified mixed input.

If n=1, the one-copy calculation with t=0 proves success 1 when s=0.
When s=1, the k measured bits are independent fair bits. The only failure
is the all-zero string, of probability 2^{-k}. Thus this branch also has
success at least 2/3, for both possible shifts.

## Uniform implementation and joint resource bounds

All arithmetic uses binary integers of O(n) bits. N itself can require n+1
bits. Comparisons, addition, subtraction, and selection are finite Boolean
circuits with a linear number of gates and scratch bits. For example, each
carry or borrow depends on a fixed number of bits, and a scan through the
bit positions performs one arithmetic operation. For y,t<N, select y-t
if y>=t, and y+N-t otherwise. Keep y unchanged if y>=N. This computes f_t;
conditional addition computes its inverse. The same construction works with
the quantum candidate bits as inputs and leaves those bits unchanged.

To make a Boolean computation reversible, store each gate result in a clean
scratch bit, XOR the final result into a target, and reverse the computation.
Use NOT, CNOT, and Toffoli. For a permutation, compute the result into a zero
register, swap the input and result, and XOR the inverse function into the old
input to clear it. Include the control flag and first qubit in the Boolean
selection. All scratch bits return to zero. The conservative bounds O(n^2)
gates and O(n^2) scratch qubits per controlled permutation suffice.
Reuse these scratch qubits between saved copies.

These gates have exact Clifford+T implementations. In particular the bit
identity

$$
4abc=a+b+c-(a\mathbin\oplus b)-(a\mathbin\oplus c)
 -(b\mathbin\oplus c)+(a\mathbin\oplus b\mathbin\oplus c)
$$

implements CCZ with a constant number of T or T-inverse gates: compute the
three pair parities and the triple parity in clean bits, apply the indicated
phases, then clear the parity bits. Hadamards on the target convert CCZ to
Toffoli. Also T-inverse=T^7. There is no gate approximation or precision cost.
An AND chain computes the condition for the sign change in (2) with O(k)
gates and O(k) scratch qubits, then clears it. The diffusion D uses n
Hadamards before and after a sign change on the all-zero candidate state,
with the same AND construction. This gives D up to a global sign, which
has no effect; a constant Clifford circuit can supply that sign if required.

A uniform classical controller emits the finite circuit loops with binary
counters. It stores no full sequence of r iterations. The saved source copies
use k(n+1)=O(n^2) qubits. The candidate, flags, AND chains, and reused
arithmetic scratch need O(n^2) further qubits. The input, loop counters,
integer arithmetic scratch, output, and generated gate descriptors require
O(n^2) classical bits. Hence the total allocated bits and qubits M are O(n^2).
Every classical indexed access and classically addressed gate therefore has
address length ceil(log2(M+2))=O(log(n+2)), which is also O(n).

There are k=O(n) controlled permutations per reflection, each with the
polynomial construction above. To charge all implementation details, allow
O(n^2) classical bit operations for the generation, bounded-width arithmetic,
addresses, and execution of each elementary reversible gate. This is a
uniform upper bound: its wire numbers and loop counters have O(n) bits,
and their addition, comparison, or multiplication uses at most O(n^2) bit
operations by the usual bit scans and school multiplication. With at most
O(k n^2)=O(n^3) such gates per iteration, the total is O(n^5) work per
iteration. This also covers the diffusion, initialization of temporary wires,
and loop control. The workspace is reused; this work allowance does not
require a stored circuit of that size.

The exact integer r is computed once. Binary search for isqrt(9L) has O(n)
steps, each using O(n^2) bit operations for a square and comparison, with
O(n^2) bits of space. Its O(n^3) work is included. Acquisition of all k source
copies costs exactly k(n+1)=O(n^2) source work units. Preparing |u>, final
measurement, and the n=1 branch also take polynomial work within the stated
bound. The algorithm performs a fixed finite number of operations on every
branch. In particular all successes and failures have the joint bounds

$$
T(N,s)=O(2^{n/2}n^5),\qquad
S_C(N,s)=O(n^2),\qquad S_Q(N,s)=O(n^2),\qquad
Q(N,s)=n+24=O(n).
$$

All constants are absolute. These bounds include the input, source acquisition,
saved copies, generated circuits, scratch space, addresses, gates, initialization,
and measurements. Enlarging the constants covers n=1. No extra source copies
are acquired in any branch.

For B_T(n)=2^{n/2}n^5, log2(B_T)=n/2+5log2(n), so the growth index in
the rules is exactly 1. For n^2 or n, the corresponding double logarithm is
O(log log n), so each index is 0. The four indices are [1,0,0,0]; the single
numeric objective is the time index [1]. These envelopes have the exact
supported structured form, with exponent coefficient 1/2 for time and empty
exponents for the three polynomial envelopes.

## Fractional error tolerance

For this same algorithm, epsilon(n)=0 is proved for every N>=2 and every s.
All k=n+24 acquired copies must be independent ideal coset states. Thus the
number of malformed copies permitted is floor(epsilon(n)k)=0. Equations
(1)--(6), and the n=1 calculation, establish success at least 2/3 together
with all four resource bounds under every input with this promise. No behavior
is promised for malformed copies, and no positive tolerance is asserted.
This does not prove that a positive tolerance is impossible.
