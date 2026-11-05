# Adaptive exact multiplication and the resulting PG5 resource envelope

This replaces the fixed sixteen-way product in PG4, while retaining its exact
Fourier factorization, reciprocal reduction, bounded gradient preparation,
minimum-depth sieve and global 4R rational-sampler cap. All matrix generation,
interpolation, classical bit work and reversible circuit generation are counted.
No precomputed instance advice or fast-arithmetic oracle is supplied.

## 1. The actual adaptive recursion

The recursion parameter v is a declared maximum bit width, known to the
uniform controller, not a measured bit length of quantum input values. All
child widths and loops are chosen from this bound independently of the data.
Zero-padding is permitted. For v<=65536 use ordinary fixed-loop schoolbook
multiplication, with all its finite work included. For v>65536 define

    L=floor(log2 v), u=floor(sqrt(L)), k=2^u, s=ceil(v/k).

Compute L,u,k by binary integer operations. Split each operand into k base-2^s
digits, regard it as a polynomial of degree k-1, evaluate both polynomials at
j=0,...,2k-2, and recursively multiply the resulting pairs at their declared
maximum width. As in PG4, signs are explicit where needed. Here the evaluated
polynomials have nonnegative arguments; signed interpolation does not require
unknown quantum branches to choose a recursion schedule.

Generate the interpolation constants within this call, charging every bit
operation. Put d=2k-2 and D=d!. Form

    P_j(X)=prod_(0<=h<=d,h!=j)(X-h),
    d_j=prod_(h!=j)(j-h)=(-1)^(d-j) j! (d-j)!,
    M_(j,i)=(D/d_j)*coefficient_i(P_j).

The signed d_j divides D. Root polynomials are generated successively from one
by multiplication by X-h; factorials, signed products, exact quotients and
matrix coefficients use ordinary schoolbook binary arithmetic. Given recursive
products V_j, recover

    c_i=(sum_(j=0)^d M_(j,i)*V_j)/D.

Lagrange interpolation proves this is exactly each integer product coefficient:
the degree-d interpolant agrees at d+1 distinct points, so its difference
from the product polynomial vanishes. Every final division is consequently
exact. Recombine sum_i c_i 2^(s*i) with carries. Growing constants are NOT
unit-cost coefficients: multiplication/division by D or M uses their actual
binary widths and elementary bit algorithms. They are generated and stored
as part of the uniform computation, not preloaded tables.

## 2. Width contraction and all nonrecursive costs

The largest point is below 2k. A polynomial with k digits below 2^s evaluates
to less than 2^s*(2k)^k. A safe child width is therefore

    b=ceil(v/k)+k*(u+1)+1 <= v/k+k*(u+1)+2.

For L>=16 and u=floor(sqrt L)>=4,

    k^2*(u+1)+2k <= 2^(u^2) <= v.

The first inequality holds at u=4 (1312<65536); increasing u multiplies its
left side by less than eight while multiplying 2^(u^2) by 2^(2u+1)>=512.
This proves it inductively for every integer u>=4. Hence b<=2v/k<v, and every
recursive call shrinks. Its use as an integer allocated-width bound handles
all leading-zero operands without data-dependent quantum control.

Here are conservative explicit bit-cost bounds sufficient for the analysis.
D, the coefficients of P_j, and the coefficients of the scaled interpolation
matrix have O(k log k), hence O(k^2), bits. For P_j this follows by bounding its
coefficient absolute sum by prod_(h!=j)(1+h)<= (2k)^(2k); multiplying by D
adds O(k log k) bits. There are O(k^2) matrix coefficients. The straightforward
root-polynomial, factorial, exact-quotient and matrix construction described
above takes at most O(k^8) bit work, including indices and loop arithmetic:
there are O(k^3) coefficient updates, each a schoolbook operation on O(k^2)
bits, and O(k^2) further such bounded-width products/quotients. This is a loose
upper bound and includes construction rather than assuming a lookup table.

Evaluated and recursive-product widths are O(v/k), by the preceding width
inequality. Horner evaluation uses O(k^2) additions or products by point
indices of O(log k) bits. The interpolation has O(k^2) products of O(k^2)-bit
matrix constants with O(v/k)-bit values, followed by exact schoolbook division
by the O(k^2)-bit D. Binary schoolbook multiplication/division costs the product
of the operand widths, and signed arithmetic changes only constants. Summing,
carrying, recombining and fixed-width controller loops fit the same loose bound.
Thus ALL nonrecursive bit work is at most

    c0*v*k^8

for one absolute c0, independent of v and data. Temporary constants and
intermediate values fit at most the number of bit operations, which is a valid
space upper bound. No growing arithmetic object is unit cost.

## 3. A proved explicit coefficient in the product envelope

Let lambda=log2 v. Since k=2^u and u<=sqrt(lambda), nonrecursive work is
O(v*2^(8 sqrt(lambda))). Child widths are <=2v/k; there are 2k-1 children,
so their total declared width is <=4v. Moreover

    log2 b <= lambda-u+1 <= lambda-sqrt(L)+2.

For L>=16 the square-root decrease is at least 1/5:

    sqrt(lambda)-sqrt(log2 b)
      >= (sqrt(L)-2)/(2 sqrt(L+1)) >= 1/5.

The last elementary inequality holds at L=16 and persists, for example by
squaring its nonnegative sides. If a child reaches the finite schoolbook range,
use its already bounded base cost; there is no negative-log convention needed.

Induct on the allocated width with target A*v*2^(20 sqrt(log2 v)). The sum
of all child target bounds is at most

    A*4v*2^(20 sqrt(lambda)-4)
       = (A/4)*v*2^(20 sqrt(lambda)).

The nonrecursive c0*v*2^(8 sqrt(lambda)) fits the remaining three quarters
with sufficiently large absolute A. Enlarge A to cover every finite base width
v<=65536 (and zero/one-bit inputs). This proves the full uniform bit complexity

    M(v)=O(v*2^(20 sqrt(log2 v))).                 (3.1)

The inside coefficient twenty is derived by this contraction proof, not a
replacement of an unspecified big-O coefficient. The larger schoolbook finite
prefix and all matrix generation costs are included. The algorithm is actual
adaptive interpolation, not a progressively looser choice of a constant radix.

For use on quantum registers, replace each bounded-fan-in Boolean operation by
clean reversible evaluation, retaining its output until reversal. Copy the
result if needed, or use it for a phase and then reverse once. The gate count
and scratch are O(M(v)); classical generation and its bits are charged by the
same bit bound. Every gate is exact Clifford+T after the retained Toffoli
construction. The declared recursion widths make the entire circuit uniform
and independent of quantum operand values. Classical constants can be retained
for the reverse schedule or regenerated with another counted constant-factor
copy of the same work. No gate history survives after cleanup.

The uniform address representation can be made explicit without assuming
constant-time variable-stride multiplication. Assign each logical bit a
classical pointer record padded to P bits, where P is the least power of two
at least the full wire-address length A_addr. Its address is a base plus the
logical-bit index shifted by log2 P. A lookup or update copies O(A_addr) bits,
each paying its full address charge. Address buffers, allocation counters and
base-plus-shift calculations likewise cost O(A_addr^2) charged work per logical
Boolean operation. Array traversals use running cursors with binary addition;
no multiplication of two A_addr-bit variable indices is free. When useful,
retain the current arithmetic Boolean-gate list with its constant number of
wire addresses per gate, then read it backward for cleanup and release it.
This costs O(M(v)*A_addr) CLASSICAL bits, all counted, and O(A_addr^2) work
per stored/read instruction. The quantum Boolean-value history costs O(M(v))
qubits. This local description is polynomial/subpolynomial times linear in n,
not a list of the exponentially many complete sieve operations; all local
records are released/reused between product phases. Section 5 includes this
extra memory before justifying the common address length.

One can choose the word width without assuming the desired memory bound:
first count the data-independent local Boolean program length m with the
uniform generator, then increase a until the planned base allocation plus
O(m*next_power_of_two(a)) bits fits addresses of length a. This integer sizing
loop terminates and is charged once for that program. Its solution is
O(log(base+m+2)); in the present construction base=O(nL_0) and m is
subpolynomial times linear in n, so a=O(sqrt n). The subsequent explicit
allocation and all stored pointers fit that checked capacity. The sizing work
is polynomial in the counter widths and within the already counted generation
budget. This establishes the address bound with actual counted allocations,
not an assumption that an unbounded pointer table has negligible size.

## 4. Rectangular products and exact Fourier recursion

PG4's overlap-aware block product remains exact. For a long O(n)-bit operand
and a short w=O(sqrt(n))-bit operand, at most O(n/w) calls of (3.1), plus a
linear overlap/carry pass, cost

    O(n*2^(20 sqrt(log2 w))+n)
       <= O(n*2^(20 sqrt(log2 n))).

Constant factors in argument widths affect only an outer absolute constant,
since sqrt(log2(Cn))<=sqrt(log2 n)+sqrt(max(0,log2 C)). Thus the reciprocal
coherent translation in fast-labels.md has this same logical gate/bit bound.
Its initial classical reciprocal is still generated once with counted
restoring division. Exact measured-residue rounding N*Z uses (3.1) at width
O(n) and fits the same bound. All inverse cleanup and signed carry logic remain
as explicitly specified there.

The exact Fourier factorization is unchanged: two half-size Fourier children
surround one product phase and an explicit block permutation. At each product
phase compute with (3.1), add only into the corresponding TOP local-width bits
of the shared gradient, then reverse. Summing recursion levels conservatively
costs at most O(log v) copies of the top-level envelope, because total width
per level is O(v) and all child widths are <=v. Hence

    Q(v)=O(v log(v)*2^(20 sqrt(log2 v)))
        =O(v*2^(21 sqrt(log2 v))).                (4.1)

For the last step let x=log2 v: x<=O(2^sqrt(x)). For x>=16 the logarithmic
inequality log2 x<=sqrt x holds at sixteen and its right-minus-left derivative
is positive thereafter; the finite prefix is absorbed by an outer constant.
This explains the exact extra coefficient one. All gates and classical
scheduling are counted; neither an FFT oracle nor arbitrary rotations appear.
Peak quantum scratch is bounded by the same subpolynomial-times-linear
expression. The actual gradient's single global approximation and preparation
abort, the exact QPE tail, and the unchanged global coin coupling retain their
original error budgets. No additional approximation has been introduced by
adaptive multiplication or the exact Fourier recursion.

## 5. Complete RS4V resource representation

The actual adaptive product and exact Fourier bounds above are unchanged.
With RS4V's new quotas L_0=O(log2(n)*2^((227281713/100000000)sqrt(n))), source work remains
O(n^3 L_0*2^(21sqrt(log2 n))). The salvage instrument's degree-at-most-fifteen count
arithmetic costs O(n^3 L_0*2^(20sqrt(log2 n))), and hard-capped sampler work
O(n^3 L_0), both smaller. recycle-sieve.md gives all grouping, conditional
state, shortage and exact new-parameter proofs. Substitution yields

    T=O(n^3(log2 n)*2^((227281713/100000000)sqrt(n)+21sqrt(log2 n))).

Local arithmetic/Fourier quantum scratch and classical current-program/pointer
records still have log sizeO(log n+sqrt(log n)), below L_0's exponential-in-
sqrt(n) growth. They fit O(L_0) quantum and O(nL_0) classical before the same
O(sqrt n) address bound is applied. All generation, coefficient matrices,
record copies, trial failures and resets are counted. Same exact source
acquisition ceilings and clean-input success/tolerance apply; the n<=16
exhaustive branch is unchanged. The supported new envelope, rational
coefficient227281713/100000000, full logarithmic factors and exact indices are proved
in recycle-sieve.md Section6. The adaptive theorem directly reuses PG5
7e1c8dba-adc8-46db-bf59-1f31688d41c2 and its earlier named foundations;
no historical verdict is a premise of any bound.

RS4V directly reuses SG6 dc8d6d56-9618-46bc-97a3-e9b18ec65099's
primary/triangular rescue component, but changes pairing to whole-bucket
SUM pooling and proves the new conditional populations and quotas in
recycle-sieve.md. This is the single present configuration.

RS4V directly reuses PS7 cda83fcf-1faa-41d5-b858-d5ec44122fe6's
population framework but adds a third SUM pass and globally recycled PRIMARY
rejects. recycle-sieve.md gives the complete changed channel/count/cost proof;
old pass-specific bounds are not assumed unchanged.

## RS4V extension and provenance

This file is adapted from RR8 at ae634c28a7e4a2683087607a83a432adb370b5d7.
The present program adds the fourth SUM channel proved in recycle-sieve.md,
with q=599/100, F=2^62lambda and coefficient 227281713/100000000. The historical
ancestry descriptions above identify inherited material. Any old three-pass
summary is extended by that explicit fourth pass; no predecessor verdict is
used. All four kernels, including the degree-fifteen kernel, have constant
degree and O(n)-bit operands. Their counted adaptive arithmetic fits the
same O(n*2^(20sqrt(log2 n))) logical work per pair with absolute constants.

## RS4V sharper primary-reject coin

RS4V extends RS4 (b16fcbf5-7e11-4148-80f1-cee7ae2df6b5), retaining
its entire four-pass exact stream. In the global primary-V rescue only,
use p=2679/10000, zero coin 2p H^3/J0 and positive coin p H^3/J_delta.
recycle-sieve.md Section 4 proves the stronger exact success p; Section 7
uses DV>=e p PV in the nine-event proof. Every sample/trial limit remains
unchanged in form, recomputed for q=599/100, r=1033/400 and F=2^62lambda.
The new resource coefficient is 227281713/100000000. This is a new actual
acceptance instrument and configuration; no old verdict validates it.
