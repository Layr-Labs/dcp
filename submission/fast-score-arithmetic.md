# Reversible interpolation with inline product accumulation

For operands of bit width w >= 2, let b=ceil(log2(w+1)) and let m
be the least power of 16 with mb>=w. Set t=2b+ceil(log2 m)+1 and
P=31! * 2^t+1. Work with coefficients in R=Z/PZ. Each residue
uses O(log(w+2)) bits, and P is strictly larger than the maximum
coefficient m (2^b-1)^2 of the uncarried ordinary convolution. Encode
both integers as base-2^b digits, using m residue slots per operand,
and allocate a 2m-coefficient padded accumulator. Later use the
ordinary carry pass below. These arrays occupy O(w) qubits.

All scalar operations on residue words are exact. For a known scalar
addition from another residue word, multiply the source by the known
scalar modulo P in scratch using schoolbook controlled modular
addition, add the temporary result into the target, then uncompute
the scratch. Unit scalar multiplication of a target is a permutation.
Evaluate it into scratch using the same modular circuit, exchange
words, and clear the old word by computing the product with the
inverse scalar. Extend all permutations by identity on binary padding.
A controlled modular ripple operation uses O(log w) wires, and the
whole constant-size collection of scalar operations for one word step
has O(polylog(w+2)) gates and controller work, including the addresses.
All public coefficients and inverses can be computed once by ordinary
polynomial-width Euclidean or modular arithmetic. They are only
O(log w) bits and the cost to compute them is polylogarithmic in w.

## Recursive product addition

A length k=16h call sees its operands as polynomials
a(Z)=sum_{i=0}^{15} a_i Z^i and b(Z)=sum_{i=0}^{15} b_i Z^i
in Z=X^h, with blocks a_i,b_i in R[X] of degree less than h.
Use evaluation points j=0,1,...,30. For each j define

    L_j(Z)=product_{0<=l<=30,l!=j}(Z-l)/(j-l).

All integers of absolute value in [1,30] are units modulo P,
since P=1 modulo each. Thus these polynomials are well-defined,
and interpolation works over the coefficient ring. In detail, the
Vandermonde matrix has determinant product_{i<j}(j-i), a unit,
so its map is invertible, and the L_j evaluate to the corresponding
standard basis. Treating the block coefficients as polynomials in
X gives the product identity

    a(Z) b(Z) = sum_{j=0}^{30} L_j(Z) a(j) b(j).

After substituting X^h for Z, the identity retains all product
coefficients of degree below 2k. Let L_j(Z)=Z^ell U_j(Z), with ell=0
for j=0 and ell=1 otherwise. For j=0 the constant coefficient is 1.
For j>0 the only zero constant factor is the simple factor Z,
and the constant coefficient of U_j is a product and quotient of
nonzero small integers. In all cases U_j has unit constant c0.

Multiplication by U_j(X^h) on the truncated output view
R[X]/(X^(2k)) is an invertible linear map V_j. It is implementable
in place in O(k) scalar steps, because the degree in Z is a fixed
constant. In descending output coefficient order update coefficient
i to c0 times itself plus the specified scaled earlier coefficients
i-lh for nonnegative indices. Each earlier coefficient still has
its input value. For the inverse traverse in ascending order,
subtract the other terms using the already-restored earlier
coefficients, and multiply by c0 inverse. No scratch array for
an extra polynomial is allocated. This procedure works on arbitrary
accumulator contents.

For a single j, apply V_j inverse to the accumulator. In each
input operand replace block 0 in place by the linear combination
defining its evaluation at j, using the untouched higher blocks as
sources and the coefficient 1 of block 0. Recursively add the
product of these length-h evaluation blocks directly into the
2h-word output slice starting at ell*h. Restore both input block
zeros by subtracting the same contributions, and apply V_j to the
whole current output view. By linearity this has added exactly
L_j(X^h)*a(j)*b(j). All transforms accept an arbitrary accumulator
and restore the input arrays. Repeating these 31 steps implements
the full product add. A child's product never exceeds its 2h-word
slice, since both its polynomials have degree below h. For k=1
add the two residue words' scalar product modulo P into the first
output coefficient using reversible schoolbook modular arithmetic,
clearing its temporary scratch and leaving the second coefficient
unchanged. This is a local O(polylog w) operation. Each full inverse
is the reverse visitation order with every elementary gate inverted.

Only one child is active at a time. Its polynomial storage is
just a view within the initial arrays, and arithmetic scratch is
polylogarithmic in w and reused between word operations. The
controller uses a logarithmic-depth stack of O(log w)-bit slices,
cursors, widths and phases, emitting elementary reversible gates
from them. There is no stored circuit of superlinear length.
Per-node nonrecursive work is O(k polylog(w+2)); the recurrence
is C(k)<=31 C(k/16)+O(k polylog(w+2)). The charged work is
O(m^(log_16 31) polylog(w+2)), since the level work forms a
geometric sum with ratio 31/16. These bounds count binary word
address construction, controller arithmetic and gate accesses.
Thus for w=O(n) the work is O(n^(5/4)), using 31^4<16^5 and
absorbing the fixed logarithmic factors. The synthesis of
elementary reversible word gates uses exact Clifford+T.

## Recovering ordinary binary digits

Begin the coefficient accumulator at zero. The final convolution
coefficients are strictly below P, so the stored residues recover
the ordinary integer coefficients. Use one sequential carry pass,
with C_0=0: compute E_i=T_i+C_i in fresh scratch, copy its low b
bits to the corresponding binary output digit, and save
C_(i+1)=floor(E_i/2^b). Clear E_i before proceeding. Each carry
fits O(log(w+2)) bits since T_i<P and the carry is below P by
induction. Keep the m-scale carry tape in O(w) bits. After the pass
erase its entries in reverse order by recomputing their temporary
sum from the still-present preceding carry and coefficient. The
product fits 2m binary digits of b bits, with final carry zero.
Reverse the coefficient multiplication to clear its accumulator,
then uncopy the original operand representations. This returns a
clean binary product and keeps all workspace O(w).

The method uses polynomial interpolation for multiplication and
adapts the idea of in-place shifted product accumulation from
Craig Gidney, [Asymptotically Efficient Quantum Karatsuba Multiplication](https://arxiv.org/abs/1904.07356).
The interpolation construction and branchwise workspace bounds
above suffice independently of that paper's algorithm.

## Reversible reciprocal reduction

For modulus D of bit length at most w, first reduce the fixed record
multiplier modulo D using counted classical polynomial preprocessing.
Assume that the quantum operand x is a nonnegative padded w-bit
argument and the now-loaded multiplier k is below D. Form p=x*k in
a fresh 2w-bit register through the multiplier. Precompute the
integer constant u=floor(2^(2w)/D) by classical integer long division
only once per stage modulus, using O(w) scratch. This preprocessing
takes polynomial work outside the search loop. If an arbitrary
record multiplier was not already reduced, reduce it outside the
search and retain its residue in the existing fixed-width record.
Signed record multipliers therefore also use valid residues.

Compute p*u into a fresh register of width at most 4w+1 and view
its upper bits as q=floor(p*u/2^(2w)). Then

    p/D - 1 < p*u/2^(2w) <= p/D.

Consequently q is either floor(p/D) or one smaller. Reversibly form
q*D in another output register and form r0=p-q*D with ripple
subtraction in a fresh word. This yields 0<=r0<2D. Compute r in a
fresh output word as r0 if r0<D, else r0-D, using an exact
comparison and one controlled subtraction. This construction
computes p mod D including D=1 and padded operand values. The width
of each register, including q*D, is O(w), and all scratch is cleared
after using r by reversing comparison, subtraction, and the three
product computations. Add only a constant number of extra O(w)-bit
registers. Products and divisions in the precomputation are
ordinary counted classical bit arithmetic, including exact
power-of-two constants, address debits and a polynomial bound
on every branch. They are never repeated per Grover iteration.

