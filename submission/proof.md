# LST: linearly stored, streamed cutoff shift testing

## Theorem and provenance

Let N>=2, n=ceil(log2 N), and s be any element of Z/NZ. LST uses the exact
sequential tests, k=n+4, and global budget 48N of public submission
f22bcee1-44ba-4cd1-b9ae-3d5c7e71dd8a (commit
0bc6b1ebce10cae23831491ba3a46f2ed477209c). That cutoff and correctness
argument are reused explicitly, rather than claimed as new. The supplied
repository baseline also contains the linear-size Boolean arithmetic needed
below. The contribution is to specify and charge a streaming implementation
without the predecessor's deliberately quadratic gate/space overestimates.
For this same implementation, every branch jointly satisfies

    T = O(N n log2(n+2)), S_C = O(n), S_Q = O(n), Q <= 48N,

and Pr(output=s)>5/6. Constants are absolute and independent of N,s,outcomes.
Thus uniform supported envelopes are 2^n n log2 n, n, n, 2^n, respectively
(asymptotic n>=2; an absolute constant separately covers n=1).
The indices are 1,0,0,1. This is an elementary tightening of the supplied
baseline, not a subexponential algorithm or a novelty claim about DCP research.
No external subroutine is assumed beyond the exact finite Clifford+T
implementations of constant-size reversible Boolean gates explained below.

## Algorithm

Keep binary classical registers N,t,j,c. Initially t=0,c=0 and k=n+4.
For each t=0,...,N-1 set j=0 and do the following until a minus is observed
or j=k. If c=48N output 0 and halt. Otherwise acquire one fresh source copy,
increment c, and apply f_t to its second register controlled by its first
qubit, where on n-bit integers

    f_t(y) = (y-t) mod N for y<N, and f_t(y)=y for y>=N.

Measure its first qubit in the X basis (H then Z measurement). Dispose of
all sample wires; all arithmetic ancillas have already been uncomputed.
On minus increment t and start the next candidate. On plus increment j;
if j=k output t and halt. If the enumeration ends, output 0. Gate blocks
are generated one gate at a time, as specified below; no whole circuit list
is retained. This specifies every abort and failed branch. No postselection,
restart, source inversion or coherent source control is used.

## Success with a hard sample cap

On a component of the mixed source, controlled subtraction gives
(|0,x>+|1,(x+s-t) mod N>)/sqrt(2). For t=s the first qubit is |+>.
For t!=s its reduced density matrix is I/2, because the two second-register
basis vectors differ. Hence a true candidate always passes a test and any
wrong one passes with probability exactly 1/2. The statement holds after
averaging x and conditional on the previous tests by independence of copies.

For analysis imagine independent outcome lists for every wrong candidate
and omit the global cutoff. Let X_t be its first-minus waiting time truncated
at k; E X_t=sum_{j=0}^{k-1}2^{-j}<2. The probability some wrong candidate has
k pluses is at most (N-1)2^{-k}<1/16. The uncapped computation takes no more
than W=k+sum_{t!=s} X_t tests even if it returns early at a wrong candidate.
Since n+4<=3N for N>=2, E W<2(N-1)+n+4<=5N. Markov gives
Pr(W>48N)<5/48. If W<=48N the cap cannot change the uncapped output.
Therefore total failure probability is below 1/16+5/48=1/6. This proves
success >5/6 unconditionally. Every actual branch has at most 48N copies;
expected-time reasoning is used only to bound the probability of the
explicitly specified abort, never as the resource guarantee itself.

## Linear-size Boolean arithmetic

Here are enough implementation details to fix the storage and uniformity
claims. Represent numbers by little-endian bit arrays. A w-bit addition
stores each next carry and sum, using a constant number of AND/XOR/NOT
operations per position; subtraction is addition of the complemented
subtrahend plus one, with one extra carry. Comparison uses the final carry
of subtraction, or a ripple equality/less-than scan with two bits per
position. A selection z_i=(b AND u_i) XOR ((NOT b) AND v_i) costs a constant
number of gates per position. Each whole operation has O(w) Boolean gates
and O(w) recorded intermediate bits. All these bounds are literal linear
bounds with absolute constants. Taking w=n+2 handles every signed candidate
intermediate below without overflow.

For y<N use the comparison y>=t to select y-t or y+N-t; for y>=N select y.
The branch values can all be computed, and selection performed bitwise.
Only a fixed number of comparisons, additions, subtractions and selections
is involved. For the inverse, compute z=y+t in n+2 bits, select z-N if
z>=N and z otherwise, and retain y on the invalid range y>=N. The inverse
on the valid range is (y+t) mod N, since 0<=y,t<N gives z<2N.
For the controlled operation additionally select identity if the controlling
qubit is zero. The result is a constant number of ripple blocks and thus a
uniform O(n)-gate Boolean circuit and O(n) total intermediate Boolean nodes.
Both maps are permutations on all n-bit strings, mutually inverse; this
matters when N is not a power of two.

## Reversible conversion and exact gates

Give each Boolean circuit node a fresh zero wire. An XOR node is computed
with two CNOTs, AND with Toffoli, and NOT by X followed by CNOT. Fanout is
implemented by separate CNOTs; there are only O(n) node input incidences.
Keep inputs and earlier node values unchanged. After evaluation, XOR its
n output bits into a separate target and reverse all node gates. This is
an XOR oracle for f_t using O(n) elementary reversible gates, O(n) scratch
qubits, and zero final garbage. The same holds for the inverse. Constants
N and t are classical bits; the generator emits X or identity operations
as needed and does not store a quantum copy of its classical program.

To make an in-place permutation on register Y, starting with target Z=0,
compute Z=f_t(Y), swap Y,Z, then XOR f_t^{-1}(Y) into Z. The result is
Y=f_t(old Y) and Z=0. Use the controlled maps in both XOR oracles, with
the same source first qubit as an additional retained input. On control
zero both maps are identity, so that branch also clears Z. The first qubit
is never measured during this construction. The constant number of
work/target/node arrays uses O(n) qubits and O(n) gates in total per test.
NOT,CNOT,Toffoli and SWAP suffice (a SWAP is three CNOTs). Toffoli has an
exact constant-size Clifford+T decomposition; no approximate arithmetic,
rotations, phase estimation, synthesis precision or stored real constants
are needed. A fixed finite gate template is part of the uniform algorithm.
All zero wires are initialized and all discarded sample wires are accounted.

## Streaming generation and bit-operation addresses

This section is essential: linear gate count alone would not prove the
time claim in the challenge's addressed bit-operation model. Fix a compile-
time layout containing a constant number of arrays of length n+2. Allocate
one node block for each of the constant-size Boolean templates per ripple
position. Node addresses are affine functions A*i+B*n+C with fixed integer
coefficients; array boundaries may be padded by a fixed number of nodes.
A node depends only on input bits at i, the carry or comparison state at
i-1, and a fixed finite list of same-position nodes. Therefore emitting
one node's constant number of reversible gates needs only O(log(n+2))
bit operations on array indices. The reverse oracle scans positions and
within-position nodes in reverse order, using the same formulas. It does
not store the forward gate list or a recursion stack of length n.

N and t have n+1 bits at most, and each constant bit lookup incurs its
O(log(n+2)) address cost. At one position the generator needs a constant
number of such reads. It retains only a constant number of node addresses
and O(log(n+2))-bit counters plus the O(n)-bit classical input and main loop
registers. Overall allocated classical bits and qubits are O(n), so the
challenge charge ceil(log2(M+2)) is O(log(n+2)). Writing each constant-size
gate descriptor and its addresses costs O(log(n+2)), as does reading
its index-sized fields. Applying each emitted gate also pays that address
charge. The extra cost of fixed-template Toffoli decomposition is constant
in gate count, with the same wire-address charge per elementary gate.
Thus all O(n) gates, their generation, and all addressed classical
operations of the ripple templates cost O(n log(n+2)) per test, using
O(n) classical storage rather than retaining O(n) gate descriptors.

Main loop increments/comparisons may scan O(n) counter bits, costing
O(n log(n+2)) with addressing. In particular c<=48N has only n+6 bits;
there is no exponential-size counter. The first measurement, initialization,
disposal, and the n+1 source charge all fit the same bound. Computing k,
48N, and initial layout addresses uses O(n log(n+2)) or less. A constant
number of n-bit words is reused. No quantum-addressed lookup or QRAM is
present. The controller and quantum arrays have peak sizes O(n) even on
failed or cutoff branches.

## Joint envelopes, indices, and error model

Multiply the per-test bound by 48N. Candidate-loop overhead is at most
N times the same per-test bound, even if a candidate terminates immediately.
Thus T=O(N n log2(n+2)), S_C=O(n), S_Q=O(n), Q<=48N, on every branch
of this exact algorithm. Since N<=2^n and log2(n+2)=O(log2 n) for n>=2,
the supported declarations are B_T=2^n n log2 n, B_C=B_Q=n,
B_samples=2^n. For n=1, log2 n vanishes; as usual big-O envelopes apply
for sufficiently large n, and the actual N=2 computation uses the same
finite algorithm with bounded nonzero resources. No all-n pointwise
inequality to a zero envelope is being claimed.

For time, log2 B_T=n+log2 n+log2 log2 n, so its defined limsup index is 1.
For samples log2 B_samples=n, giving 1. For either space envelope n,
log2 log2 n divided by log2 n tends to zero, giving 0. Multiplicative
absolute constants do not affect these limits. All statements describe
one configuration k=n+4, cap 48N, and the streamed circuit just specified.

The fifth claim is epsilon(n)=0, under exactly the baseline error-model
text: 'Malformed fraction among acquired copies. The proved guarantee
requires every copy to be an independent ideal coset state; no behavior
is promised for malformed copies.' It supplies no positive robustness
claim and does not assert impossibility of positive robustness. Under this
promise the success proof and every resource bound hold jointly.

Relative to the supplied baseline envelopes 2^n n^4,n^2,n^2,2^n n,
all four envelopes are no worse and each is asymptotically smaller.
Relative to the cited cutoff predecessor 2^n n^3,n^2,n^2,2^n,
the first three strictly improve and the fourth ties. The numerical time
index remains 1. Other subexponential algorithms offer different time-space
tradeoffs; this work asserts neither a globally best algorithm nor promotion.
