# Streamed exhaustive shift testing (SEST-1)

## 1. Scope, provenance, and theorem

This specifies an implementation and resource analysis of the elementary
exhaustive-testing baseline. It makes no novelty or subexponential-time claim.

[R] is `Layr-Labs/dcp`, revision
`a74599ed97e222c1872e254e36592277ba631935`, `rules.md`.
[B] is `submission/proof.md` at the same revision, sections “Correctness” and
“Implementing the controlled subtraction.” All arguments needed from these
sources are reproduced below. No external theorem, arithmetic library, circuit
synthesis service, or fetched reference is needed. Section 4 supplies an exact
Clifford+T construction instead of relying on an external decomposition theorem.

For every integer N >= 2, put n = ceil(log2 N), m = n+1, k = n+2, and
L = ceil(log2(n+2)). All logarithms are base two. N occupies m classical bits,
with leading zeros when necessary. The secret is any s in {0,...,N-1}.
The only source access consists of fresh independent copies of

$$
\rho_s=\frac1N\sum_{x=0}^{N-1}|\psi_{x,s}\rangle\langle\psi_{x,s}|,
\qquad |\psi_{x,s}\rangle=
\frac{|0,x\rangle+|1,(x+s)\bmod N\rangle}{\sqrt2}.
$$

Neither x, a purification, an inverse, nor controlled source preparation is
assumed available.

**Theorem.** The single algorithm SEST-1 defined in sections 2–5 outputs the
entire s with unconditional probability greater than 3/4 for every N and s.
There exist positive absolute constants C_T, C_C, C_Q such that for all N >= 2,
all s, and every branch of this bounded program, jointly

$$
T\le C_T N(n+2)(n+1)L^2,\qquad
S_C\le C_C(n+1),\qquad S_Q\le C_Q(n+1).
$$

The constants are independent of N, s, and measurement outcomes. T includes
all sequential classical bit work, addressing, circuit generation, gates,
initialization, source copies, measurements, and unsuccessful attempts in [R].
S_C and S_Q include all accessible storage, inputs, outputs, and ancillas.
These are big-O results; finite numerical constants are not asserted.
Uniform envelopes are B_T(n)=2^n(n+2)(n+1)L^2 and B_C(n)=B_Q(n)=n+1.
Their exact growth indices are respectively 1, 0, 0.

## 2. Algorithm and unconditional full-secret recovery

Visit t=0,...,N-1 in increasing order. Perform up to k tests per candidate,
each using a fresh source copy. Each test applies the permutation

$$
|c,y\rangle\longmapsto|c,F_t^-(c,y)\rangle,\qquad
F_t^-(c,y)=
\begin{cases}
(y-t)\bmod N,&c=1,\ y<N,\\
y,&\text{otherwise}.
\end{cases}
$$

Here c is the source's first qubit and y is an n-bit word. Measure c in the
X basis using H and computational-basis measurement. On minus (bit 1),
reject t immediately and advance to the next candidate. On k successive plus
results, output the entire n-bit representation of t and halt. If all
candidates fail, output 0 and halt. This last alternative makes the program
total but has probability zero on the stated input. After each test measure
the data register in the computational basis, discarding the measurement
bits one at a time. Reuse storage. There is no repeat-until-success loop.

On every pure component of the mixture, the controlled subtraction gives

$$
\frac{|0,x\rangle+|1,(x+s-t)\bmod N\rangle}{\sqrt2}.
$$

If t=s this is |+>|x>, so plus is certain. If t differs from s modulo N,
the two data basis states are distinct; otherwise their equality would imply
t=s. The reduced control state is therefore I/2 and plus has probability
exactly 1/2. These conclusions hold for every x, hence for the mixture.

Conditional on any history reaching an incorrect candidate, its fresh copies
are independent with that same state. The candidate passes with probability
2^(-k). The true candidate cannot fail. A union bound over all incorrect
earlier candidates gives

$$
\Pr(\text{wrong output})\le (N-1)2^{-(n+2)}
<2^n2^{-(n+2)}=\frac14.
$$

This includes early wrong outputs and uses no postselection. The algorithm
recovers the full secret with probability >3/4, hence at least 2/3.

## 3. Explicit Boolean circuits

All words are little endian. Arithmetic uses width m=n+1; pad y with one
zero bit. N and t are m-bit constants loaded into basis-state registers.
Also allocate constant zero and one wires. No quantum-addressed array is used.
Each Boolean instruction NOT, XOR, or AND has a fresh output wire. Retain
all intermediates until uncomputation. Use these fixed macros:

* ADD(A,B,c0), for i=0,...,m-1, emits in order
  p_i=a_i XOR b_i; d_i=p_i XOR c_i; u_i=a_i AND b_i;
  v_i=p_i AND c_i; c_(i+1)=u_i XOR v_i.
  Its result is the word d and carry c_m.
* NOTWORD(B) emits one NOT per bit.
* MUX(q,A,B), of the stated width, emits per bit
  e_i=a_i XOR b_i; h_i=q AND e_i; z_i=a_i XOR h_i.
  It returns A if q=0 and B if q=1.

ADD uses five Boolean instructions per bit. If a_i=b_i=1, then p_i=0,
u_i=1, v_i=0. Otherwise u_i=0, so the carry is p_i AND c_i. Thus u_i
and v_i never both equal one, their XOR is the carry, and d_i is the sum
bit. Induction proves that ADD returns A+B+c0 modulo 2^m, together with
its carry. In particular ADD(A,NOTWORD(B),1) returns A-B modulo 2^m
and carry [A>=B]. The NOTWORD and MUX truth tables follow directly from
their formulas. No arithmetic oracle is being invoked.

The minus schedule is precisely:

1. nt=NOTWORD(t).
2. (d,b)=ADD(y,nt,1).
3. (r,unused)=ADD(d,N,0).
4. u=MUX(b,r,d), of width m.
5. nN=NOTWORD(N).
6. (unused,a)=ADD(y,nN,1).
7. v=NOT(a); q=c AND v.
8. z=MUX(q,y,u), using the low n bits only.

Variables denote wires from their macros, with no uncharged word copying.
Keep unused carry and sum outputs too. Here b=[y>=t] and a=[y>=N]. If y<N
and y>=t, d=y-t is correct and b=1 selects it. If y<N and y<t, then
d=2^m+y-t, and r=(d+N) mod 2^m=y-t+N is in {0,...,N-1}; b=0 selects r.
The last selection returns y when c=0 or y>=N. Thus z=F_t^-(c,y) for every
n-bit input, not just those in the source support.

Its inverse F_t^+(c,y) adds t modulo N when c=1 and y<N and fixes the
complement. Use this exact plus schedule:

1. (w,unused)=ADD(y,t,0).
2. nN=NOTWORD(N).
3. (d,b)=ADD(w,nN,1).
4. u=MUX(b,w,d), of width m.
5. (unused,a)=ADD(y,nN,1).
6. v=NOT(a); q=c AND v.
7. z=MUX(q,y,u), using the low n bits only.

Since y<=2^n-1 and t<N<=2^n, y+t<2^m and w is the exact sum. For y<N,
w<2N; b=[w>=N] selects d=w-N exactly when necessary. The same guard fixes
c=0 and invalid y. The two maps are therefore inverse permutations on all
n-bit words, including for non-power-of-two N.

The minus schedule has 20m+3n+2 Boolean instructions; the plus schedule has
19m+3n+2. Every output is allocated, so inputs, constants, and all retained
intermediates use O(m) wires. These are Boolean-instruction counts, not
finite constants for Clifford+T gates or total addressed work.

## 4. Exact reversible implementation

Into a fresh zero z, compute NOT(a) with X(z), CNOT(a,z), XOR(a,b) with
two CNOTs, and AND(a,b) with Toffoli(a,b;z). If both AND inputs name the
same wire, use CNOT(a,z). Outputs always differ from their input wires.
For any section-3 schedule H, compute it, CNOT its n result bits into an
arbitrary target Z, and reverse the entire computation. This implements

$$
E_H: |c,y,Z,0_{\rm scratch}\rangle
\longmapsto |c,y,Z\mathbin{\oplus}H(c,y),0_{\rm scratch}\rangle.
$$

Constants are preserved. This holds on every basis vector and by linearity
on superpositions and mixed states. Scratch is cleared. The computation
has O(m) gates and O(m) scratch wires.

For completeness Toffoli needs no approximate synthesis theorem. For bits
 a,b,z, the exact integer identity

$$
4abz=a+b+z-(a\oplus b)-(a\oplus z)-(b\oplus z)
 +(a\oplus b\oplus z)
$$

holds: for Hamming weights 0,1,2,3 the right side is 0,0,0,4 respectively.
Apply T to a,b,z. Compute each pair parity in one clean ancillary qubit
using CNOTs, apply T-dagger, and uncompute. Then compute their triple parity
in that same qubit, apply T, and uncompute. The combined phase is exactly
exp(i*pi*abz)=(-1)^(abz), giving CCZ and restoring the ancilla to zero.
Conjugate the target z by H to obtain Toffoli. T-dagger is seven T gates;
X and CNOT are Clifford. Thus this is a fixed constant-size exact template
using one reusable ancillary qubit. Its reversed sequence is also exact.

To implement in-place controlled subtraction, allocate a zero n-bit Z:

1. Apply E_(F^-) from the data word into Z.
2. Swap corresponding data and Z wires, with three CNOTs per swap.
3. Apply E_(F^+) from the new data word into Z.

After the swap the data word is F_t^-(c,y) and Z=y. Since
F_t^+(c,F_t^-(c,y))=y, step 3 clears Z. The control is unchanged. Each
oracle clears its own Boolean scratch, so that allocation is reused. The
result is exactly the unitary in section 2 using O(m) Clifford+T gates and
O(m) accessible qubits, including constants, sample, Z and all scratch.
For simplicity charge initialization and reset of all constant registers
on every test, even though they could be reused within a candidate.

## 5. Streaming generation and joint worst-case resources

This fixes a uniform controller with no retained gate list. Reserve blocks
for inputs/constants, Z, and the outputs of each macro in section 3. The
number of macros is fixed. Allocate ADD's five outputs at addresses
base+5i,...,base+5i+4; MUX's three outputs at base+3i,...,base+3i+2;
and NOTWORD's output at base+i. The previous carry is either the initial
constant wire or the preceding bit's fifth output. Any macro result can be
referenced by its block base, stride (one, three, or five), and fixed offset.
All bases are fixed integer multiples of m and n plus fixed offsets. Each
required address is obtained by a constant number of O(L)-bit additions,
subtractions, and multiplications by fixed integers.

Forward evaluation traverses the fixed macro schedule and its bits in
increasing order. Reverse evaluation traverses macros, bits, and elementary
gates within each Boolean instruction in decreasing order, inverting each
gate. Bases are recomputable from m and the fixed macro position; no forward
trace is saved. Output CNOTs, swaps, and the constant Toffoli template likewise
have specified affine addresses or constant-size descriptions. This defines
a uniform bounded-loop generator rather than assuming free circuit generation.

The controller stores N,t, and output in O(m) bits and a constant number of
O(L)-bit counters, block bases, loop bounds, and current addresses. Elementary
index arithmetic uses bitwise carry scans, not unit-cost large integers.
The current gate template and measurement result need only constant additional
storage apart from their O(L)-bit addresses. Instructions are emitted and
discarded immediately. There is no saved circuit, history, table, or list of
source samples. All allocated classical storage, including temporary index
arithmetic and the fixed program, is O(m). All quantum allocation was shown
to be O(m). Both statements concern this same algorithm on every branch.

Thus total allocation M<=C*m for an absolute C, and the address charge
ceil(log2(M+2)) is O(L). Generating one addressed Boolean instruction requires
O(L) elementary bit operations: its constant number of index computations
are additions/subtractions or multiplication by a fixed integer on O(L)-bit
values. Each indexed bit access can itself cost O(L), giving O(L^2) work
per emitted Boolean instruction including the accesses inside index arithmetic.
The elementary Clifford+T expansion has constant length; each addressed
gate costs O(L), already covered. No quantum-addressed memory access remains
to be implemented.

A test has O(m) Boolean instructions and O(m) CNOTs, swaps, initialization,
reset, and disposal operations, each bounded by this O(L^2) charge. Loading
constant registers costs O(m) addressed bit operations. Source acquisition
costs m=n+1. The candidate counter increments and comparisons cost O(m)
addressed bit operations; test counters occupy O(L) bits. They fit within
O(m L^2) per test, including the bookkeeping of a rejected candidate.
Every reached candidate performs at least one test. Initial parsing and
allocation and final output also fit this envelope. Therefore full work
per test, including its share of controller work, is O(m L^2).

Every possible sequence of measurement bits executes at most Nk tests, even
sequences of probability zero. There is no expectation-only or postselected
resource estimate, and every failure is charged. Registers are reused across
tests. It follows jointly on every branch that

$$
T=O(N(n+2)(n+1)L^2),\qquad S_C=O(n+1),\qquad S_Q=O(n+1).
$$

All hidden constants are absolute because the schedules and templates have
fixed size and the arithmetic bounds are uniform. Here n>=1, m>=2, L>=2;
increasing a finite absolute constant covers small instances too.

## 6. Exact indices

N<=2^n gives the uniform time envelope. Its logarithm is

$$
\log_2 B_T(n)=n+\log_2(n+2)+\log_2(n+1)+2\log_2 L
             =n+O(\log_2 n).
$$

Thus log2(log2 B_T(n))=log2 n+o(1), so the limsup ratio in [R] is 1.
For either space envelope n+1 the ratio is
log2(log2(n+1))/log2 n for sufficiently large n, which tends to zero.
The max{4,B(n)} affects only a finite prefix here; n=1 is irrelevant to the
limit. Every fixed positive multiplicative constant leaves these limits
unchanged. The canonical rational indices are ("1","1"), ("0","1"),
and ("0","1") in time, classical-space, quantum-space order.

## 7. Limitations and comparison

The argument is analytic and self-contained. `arithmetic_check.py` only checks
finite arithmetic instances, the reversible compute/swap/uncompute construction,
and the phase identity. It is not an unbounded proof or resource measurement.
Structural validation and mocked exporter tests likewise cannot establish
mathematical acceptance.

[B] declared O(N n^4), O(n^2), O(n^2) and the same [1,0,0] vector. This
submission supplies a specified linear-space implementation and retains the
work expression actually derived for it. It does not assert novelty, tightness
of prior bounds, superiority to established DCP algorithms, or attainment of
the research goal 2^{O(n^{1/3})}.
