# Adaptive exact modular-word Toom accumulation in linear quantum space

This is the actual clean multiplication used by RLQGR3. It extends the
reversible output-preconditioning idea of Gidney, Asymptotically Efficient
Quantum Karatsuba Multiplication, arXiv:1904.07356v1, Section 2 Eq.(1),
which RLQGR2 already used. Here the recursion evaluates/interpolates many
blocks over a deliberately constructed coefficient ring. All operations are
exact reversible Boolean operations; no arbitrary rotations, field oracle,
prime search, precision-dependent quantum transform or outside arithmetic
algorithm is assumed. The ordinary Lagrange identity and every necessary
unit condition are supplied below. No claim of priority over the literature
is made for polynomial interpolation or the output-preconditioning method.

## Fixed uniform parameters and finite branch

Use one common operand-width v=8(n+1) for ALL multiplication calls in the
DCP oracle; pad shorter operands with zeros. The constant number of products
in reciprocal reduction have inputs shorter than v. Put L=ceil(log2 v).
If L<4096, use the former exact controlled-shift/add schoolbook integer
product, with O(v^2) gates and O(v) quantum scratch, and its inverse. A
constant number of linear-size words suffices for each shift/add, as in the
previous modular-product routine. For each operand bit, controlled-add the shifted other operand into a
2v-bit temporary using a clean ripple permutation; XOR that product into
the requested target and reverse the additions. This uses O(v^2) gates
and O(v) qubits and does not allocate v^2 retained Boolean history. Its cost is absorbed in the stated asymptotic
envelope by an absolute outside constant. The threshold is deliberately
conservative, and no practical finite-size advantage is asserted.

For L>=4096 set s=floor(sqrt L) by integer square root, k=2^s, and choose
m=k^ell as the largest power of k at most v/(k^2 L). Then let
w=ceil(v/m), B=2w+log2(m)+1, D0=(2k-2)!, P=D0*2^B+1,
and W=ceil(log2 P). All are integers computed by counted arithmetic.
No parameter is fitted to an instance outcome. Let R=Z/PZ, which need NOT
be a field. Store each coefficient in a W-bit computational-basis register,
using valid residues0,...,P-1. There are m input digits of w bits, with
zero padding beyond v, and 2m output coefficient words. Initialize padded
input residues by counted CNOT copying of computational bits; this reversible
Boolean step is valid on superpositions and is not measurement or cloning
of an arbitrary state.

The choice of m ensures

 k^2 L<=w<=2k^3 L,    m*w<=v+m<=2v,
 W<=4w<=8k^3 L,       ell<=L/s<=sqrt L+2.

Indeed the next power km violates the defining bound, which gives the upper
word-size estimate; the lower follows from m<=v/(k^2 L). Also
log2 D0<=(2k-2)log2(2k-2)<=2k(s+1), while log2 m<=L.
Thus W<=2w+L+2k(s+1)+2<=4w at this threshold. The power k exists with
m>=1 because v is much larger than k^2 L for L>=4096.

## Ring units and generated interpolation constants

Every integer1,...,2k-2 divides D0, so gcd(P,j)=1 for all of them.
Consequently every nonzero difference of two evaluation points
0,1,...,2k-2 is a unit modulo P. Compute Lagrange polynomials

 l_r(Z)= product_(j!=r) (Z-j)/(r-j),  r=0,...,2k-2,

using modular inverse via counted extended Euclid. The polynomials obey
l_r(j)=1 at j=r and0 otherwise. The evaluation matrix has Vandermonde
determinant equal up to sign to the product of these unit differences,
and is invertible over R. Therefore for EVERY polynomial F of degree<=2k-2
with coefficients in any commutative R-algebra,

 F(Z)=sum_r F(r) l_r(Z).

This proves the interpolation identity also when the coefficients themselves
are polynomials; no finite-field hypothesis is being silently used.
All coefficients, powers r^j and needed inverses are generated once, not
preloaded as advice. Inverses exist by the explicit gcd/unit proof.

For r=0, l_0 has constant coefficient1. For r!=0 it has exactly one factor Z:
write l_r(Z)=Z K_r(Z), where K_r(0) is a unit. To see the latter, its constant
term is a signed product of nonzero integers from1,...,2k-2 divided by
product_(j!=r)(r-j), all units modulo P. Write d_r=0,K_r=l_r at r=0;
d_r=1,K_r=l_r/Z otherwise. Thus K_r always has unit constant coefficient.
This is what makes the output preconditioning below reversible.

## Exact reversible coefficient primitives

Each W-bit residue addition modulo P is an in-place permutation on valid
residues, extended by identity on invalid encodings. Comparisons, schoolbook
multiplication, restoring remainder and selection have O(W^2) Boolean gates
and retained work bits. Clean evaluation computes a function, XORs its output
and reverses those gates. A permutation is applied in place by compute,
swap and inverse evaluation. Constant scaling x->c*x mod P is such a
permutation when c is a unit, with its known inverse; use identity extension
for x>=P. Addition of c*x into a separate valid target is also reversible
for any c, by subtracting the same value. Invalid input cases may act
identically, preserving full-domain unitarity. All initialized word inputs
and every intermediate word here remain valid residues.

These primitives cost O(W^2) logical gates and scratch per operation,
including cleanup and ALL NOT/CNOT/Toffoli gates. Toffoli has an exact
constant-size Clifford+T decomposition. A base product of two valid residues
is computed by Boolean schoolbook multiplication and restoring remainder,
added with the requested sign into one coefficient word modulo P, then
uncomputed. Scratch is reused serially. No arbitrary-size integer operation
or invalid-state promise is used as an uncounted gate.

## Invertible triangular output transform

For a polynomial K(Z)=c0+c1 Z+...+cd Z^d with c0 a unit, define T_K on a
length-b target word band as multiplication by K(X^h), modulo X^b over R.
Implement it by visiting i=b-1,...,0 in DECREASING order:
scale word i by c0, then add c_j times word i-jh for every j>=1 with i-jh>=0.
Lower words are still their original values at that visit, so the result is
exactly the indicated polynomial multiplication. Implement its inverse in
INCREASING order: subtract those earlier-word multiples (now already restored)
and scale by c0^(-1). This is an explicit sequence of reversible word
operations. It costs O(k*b*W^2) logical gates for the degree<=2k-2 cases used
here, with one reused O(W^2)-bit scratch region. It acts correctly on arbitrary
initial target coefficients; no temporary matrix of quantum values is stored.

## Recursive accumulation, exact target ranges and proof

ACC(u,v,t,sign) receives q=k^a input words in each band and a target band of
2q words. It restores its inputs and adds sign times their polynomial
convolution over R to the target. At q=1 use the counted base product above,
affecting target word0 only. Otherwise put h=q/k and split each input into
k bands of h words, denoted u_j(X),v_j(X), j=0,...,k-1.
For each r=0,...,2k-2 in fixed increasing order:

1. In the LOW input band replace u_0 by u_0+sum_(j=1)^(k-1) r^j u_j,
   coefficientwise modulo P; similarly replace v_0. This is reversible because
   the coefficient of the old low band is1 and the high bands are unchanged.
2. Let d=d_r and use the target subband starting at word d*h, with length
   b=2q-d*h. Apply T_(K_r)^(-1) on that WHOLE subband.
3. Recurse ACC on the two modified low bands, adding into the FIRST2h words
   of that preconditioned subband with the same sign.
4. Apply T_(K_r) on the same whole subband.
5. Restore both low input bands by subtracting the unchanged high-band terms.

These are the actual operations and loop ranges; recursion does not allocate
a product band. The inverse transform in step2 and forward transform in
step4 restore all old target values and add
sign*X^(d*h) K_r(X^h) u(r,X)v(r,X)
=sign*l_r(X^h) u(r,X)v(r,X).
Summing over r and applying the proved interpolation identity to the
product of the two degree(k-1) polynomials in Z yields the full original
input convolution after substituting Z=X^h. Its degree is<=2q-2, so all
terms fit the 2q-word target. For d=1, the shortened band still has enough
words: K_r degree<=2k-3 times h plus a child degree<=2h-2 gives at most
(2k-1)h-2. The recursive call uses exactly2h initial words of that band.
Induction proves ACC for arbitrary initial target words and arbitrary valid
residue inputs, with all input bands restored. Intermediate negative values
are ring residues; no data are discarded or postselected.

## Clean ordinary-integer result and linear quantum allocation

At the TOP only, start a zero coefficient band and perform ACC. Original
digits are <2^w, so final integer convolution coefficients are nonnegative
and <m*2^(2w)<P. Their residue representatives are therefore the exact
integer coefficients, notwithstanding arbitrary intermediate modular wrap.
Normalize by a forward carry scan: add the previous carry to coefficient i,
write its low w bits as digit i, and retain the quotient by2^w as the next
carry. All local sums/carries have O(W) bits. Retain every Boolean carry and
normalization gate value until ordinary product bits are XORed into the
requested output, then reverse normalization, reverse ACC and clear padded
input copies. The normalization has O(mW)=O(v) gates and history bits.
There is no full-width addition for each coefficient and no carry across
all output words inside recursion. The final ordinary product fits2v bits;
extra normalized high padding digits are zero and are reversed away.

The two padded inputs, coefficient band and normalization history occupy
O(mW)=O(v) qubits. Word/base scratch is O(W^2), reused, and for L>=4096

 W^2<=64 k^6 L^2<=2^(6s+6+2log2 L)<=2^(L/2)<=v.

For the elementary last bound, log2 L<=sqrt L, and8sqrt L+6<=L/2 at this
threshold and thereafter. The coefficient tables are CLASSICAL. No quantum
register is allocated per recursive frame. The finite branch also has
linear quantum space. Consequently the complete product compute-XOR map
preserves its original inputs, clears all scratch and uses O(v) qubits.

## Explicit adaptive work bound, with constants inside exponents

Let C(q) count logical gates at fixed global k,W. The stated loops give
C(q)<=(2k-1)C(q/k)+O(k^2 q W^2), with C(1)=O(W^2).
Summing levels and using 2k-1<=2k yields

 C(m)=O(k^2 m W^2 2^ell)
     =O(v k^5 L 2^ell)
     =O(v 2^(7 sqrt L)).

Here mW^2<=16m w^2<=64v k^3 L, k<=2^sqrt L,
ell<=sqrt L+2, and L<=2^sqrt L. The top copy/reverse/normalization costs
are included by an absolute factor. This is a fixed explicit exponent7,
not an unidentified constant inside an exponential.

Uniform classical setup computes the factorial, modulus, all interpolation
coefficients and inverse scalars by ordinary schoolbook arithmetic and
extended Euclid. A deliberately loose full bound is O(k^5 W^4 L^4) charged
work, covering polynomial construction and all coefficient bit accesses.
Using W<=8k^3 L gives an upper bound by an absolute constant times
2^(25sqrt L+12), which is O(v) for L>=4096. The tables have O(k^2 W)
bits, also O(v); indeed k^2 W<=8k^5 L<=2^(6sqrt L+3)<=v.
This counts all generated constants rather than importing advice. The
factorial uses only the explicitly bounded O(k) factors. Schoolbook modular
operations and extended Euclid have polynomial word cost dominated by the
loose W^4 L^4 allowance; no primality hypothesis or search is required.

A depth-first stack uses O(ell L)=O(L^2) classical bits. Every generated gate
address, table offset, frame update and word index is computed with ordinary
binary arithmetic. Allow a conservative O(L^4) fully addressed bit operations
PER logical gate, including the global memory address charge O(log(n+2)),
its own indexed accesses and even schoolbook index products. This is ample:
indices have O(L) bits and multiplication/division uses O(L^2) Boolean steps,
each with O(L) address charge. The fourth power also covers loop/frame work.
No gate stream is stored. Classical setup tables and stack fit below the
O(n^2) record allocation of RLQGR3; quantum allocation is established first.

Since L^2<=2^(2sqrt L), the complete charged product bound is
O(v 2^(9sqrt L) L^2), including setup and all inverse work. With
v=8(n+1)<=16n, sqrt L<=sqrt(log2 n)+3 for n>=2, and L=O(log n).
Therefore the explicitly chosen conservative bound

 O(n 2^(64sqrt(log2 n)) (log2 n)^2)

holds with an absolute OUTSIDE constant. The inside coefficient64 is
specified and proved to exceed the displayed compiled-work bound; it is
not chosen by replacing an unknown O() in an exponent. At the finite branch
L<4096, the linear-space schoolbook cost has a finite maximum ratio to this
positive envelope for n>=2, absorbed by that same outside constant.
No assertion of useful finite-size constants is made. The n=1 case is
handled by the fixed finite DCP branch.

## Exact fast modular product for every encoded candidate

The record label a lies in[0,N); candidate t lies in[0,2^n), including
invalid candidate labels, so z=a*t<2^(2n). First compute z with the clean
product above. Set b=2n+1 and precompute the CLASSICAL integer
C=floor(2^b/N) once by charged schoolbook restoring division. It and all
products below have O(n) bits. Compute p=z*C using the clean product and
copy its high bits to obtain q0=floor(p/2^b). Since

 0<=z/N-z*C/2^b<z/2^b<1,

q0 is floor(z/N) or one less. Compute q0*N with another fast product and
r0=z-q0*N by exact binary subtraction. Then 0<=r0<2N; one comparison and
optional subtraction yields r=z mod N. Copy r into the requested n-bit
modular-result target and reverse the comparison, subtraction and products,
clearing q0,p,z and every scratch register. The clean result map preserves
its inputs and XORs a*t mod N into a target, with O(n) quantum scratch.
A constant number of O(n)-bit products plus linear additions/comparisons
costs O(n 2^(64 sqrt(log2 n)) (log2 n)^2) charged work, INCLUDING all inverse work.

The reciprocal generation has polynomial charged work and O(n) classical
space, included in preprocessing. Its bits are constants, not instance-
dependent advice or a free oracle. Power-of-two quotients use bit copies,
not division calls. The final quotient/remainder correction is exact, with
no probability or numerical precision assumption. This completes the
counted modular-product implementation used once per classical score record.
