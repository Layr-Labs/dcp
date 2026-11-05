# Exhaustive shift testing

This is a simple exponential-time baseline for every N ≥ 2 and every s in Z/NZ.
It makes no claim of novelty. Set n = ceil(log₂ N) and k = n+2.
Use the single algorithm below for all four resource claims.

For t = 0, …, N−1, perform k independent tests using fresh source copies.
In a test, apply controlled subtraction of t modulo N to the second register,
conditioned on the first qubit being 1. Then measure the first qubit in the
X basis. If any result is −, reject t and move to the next value. If all k
results are +, output t and halt. Discard each used sample before the next test.
If no t passes, output 0 (the proof shows this branch has probability zero).

## Correctness

On a component with offset x, controlled subtraction produces

$$
\frac{|0,x\rangle+|1,(x+s-t)\bmod N\rangle}{\sqrt2}.
$$

When t = s, this is |+⟩|x⟩, so the test always returns +. When t ≠ s,
the two second-register basis states are distinct. Tracing them out gives
I/2 on the first qubit, so the test returns + with probability exactly 1/2.
This holds for each x, hence also for the mixed source.

Fresh independent copies make the probability of k consecutive + results for
an incorrect t exactly 2^{-k}, conditional on reaching that t. The correct t
never fails. The probability of outputting any incorrect earlier value is at
most the union bound

$$
(N-1)2^{-k}<2^n2^{-(n+2)}=\frac14.
$$

Thus full-secret recovery succeeds with probability greater than 3/4, in
particular at least 2/3, for every N and s. This is unconditional: no
postselection is assumed.

## Implementing the controlled subtraction

On n-bit strings define f_t(y) = (y−t) mod N for y < N, and f_t(y) = y
for y ≥ N. This is a permutation; its inverse is conditional addition of t
modulo N on the same valid range. The extension ensures a unitary on the entire
register even when N is not a power of two.

Comparisons and subtraction/addition with carry are Boolean circuits of O(n)
gates and wires: scan the bits once for each comparison or arithmetic
operation, retaining the carry/borrow. Comparing with N and t and selecting
between y−t and y+N−t requires a fixed number of such operations on n+1 bits.
An n-bit result is selected; the valid modular result is below N.

Reversible evaluation can retain each Boolean gate's value in a fresh bit,
XOR the result into a target register, and reverse all gates to clear the
intermediate bits. NOT, CNOT, and Toffoli implement these steps; Toffoli has
an exact constant-size Clifford+T decomposition. For a permutation, compute
f_t into a zero register, swap registers, and XOR f_t^{-1} of the new first
register into the old input, clearing that old input. Choosing the identity
on control 0 and f_t on control 1 makes this the required controlled
permutation. Its inverse computation uses the same control.

These constructions use O(n) gates and temporary wires per evaluation;
the conservative bounds O(n²) gates and O(n²) qubits suffice here. A uniform
classical generator emits their regular carry/comparison gates using binary
counters and the at-most-(n+1)-bit constants N,t. It needs at most O(n²) working bits and
O(n³) bit operations per test, including address handling and synthesis of
the fixed-size gates. There is no stored exponential circuit or lookup table.
The X-basis measurement is a Hadamard followed by a computational-basis
measurement.

## Joint costs and indices

There are at most N(n+2) samples and tests on every execution branch.
Each sample costs n+1; the preceding conservative O(n³) work bound per test
also covers source acquisition, initialization, disposal, measurement, and
loop bookkeeping. The peak workspace is reused between tests. Thus this
same algorithm has uniform worst-case bounds

$$
T(N,s)=O(Nn^4)\subseteq O(2^n n^4),\qquad
S_C(N,s)=O(n^2),\qquad S_Q(N,s)=O(n^2),\qquad
Q(N,s)\le N(n+2)=O(2^n n).
$$

All hidden constants are absolute; enlarging them covers the finitely many
small bit lengths. These are upper bounds, not tight space estimates.

For B_T(n)=2^n n^4, log₂ B_T(n)=n+4 log₂ n, so the definition in the rules
gives g(B_T)=1. For either space envelope n², log₂ B(n)=2 log₂ n gives
g(B)=0. Fixed multiplicative constants do not change these limits.
For the sample envelope B_samples(n)=2^n n, log₂ B_samples(n)=n+log₂ n,
so g(B_samples)=1. The four resource indices are [1, 0, 0, 1]; only time
is a numeric objective, so the published score vector is [1]. The stronger
N-dependent time and sample bounds and polynomial space expressions remain
in the claim statements. Sample count includes all unsuccessful tests and
discarded copies, independently of how little quantum workspace is retained.

## Fractional error tolerance

The preceding correctness and resource proof assumes that all acquired copies
are independent ideal coset states. It therefore establishes the malformed-sample
fractional guarantee epsilon(n)=0 jointly with all four bounds, for the same algorithm.
No positive tolerance is claimed or scored. This describes the proved guarantee;
it does not assert that the algorithm's maximum possible tolerance is zero.
