# Exact padded-word products and reciprocal modular reduction

This addendum specifies the actual arithmetic used by RLQGR2 in proof.md.
The construction adapts Gidney, Asymptotically Efficient Quantum Karatsuba
Multiplication, arXiv:1904.07356v1, Section 2 Eq.(1) and Section 3:
https://arxiv.org/html/1904.07356v1 . In particular, temporary triangular
shears of padded output words allow three recursive product additions
without recursively computing and uncomputing six products. This established
method is materially used and is not claimed as a new multiplication result.
All needed ring identities, clean normalization, resource bounds and the
modular-reduction use are supplied below, rather than assuming an arithmetic
oracle or requiring the reviewer to fetch that paper.

## A fully specified recursive accumulator

For operand bit length v>=2 choose w=ceil(log2(v+2)) and let m be the least
power of two with mw>=v. Then mw=O(v), w=Theta(log(v+2)), and m=O(v/w).
Split each input into m little-endian base-2^w digits, padding zero beyond
its v bits. Store input digits separately in A=w+log2 m+1 bits each.
Store output coefficient words in B=2w+3log2 m+2 bits, interpreted modulo
R=2^B independently of all other output words. No word-to-word carries are
performed during recursive accumulation. Original inputs are preserved;
CNOT copies their basis bits into the padded input bands, a reversible
Boolean copying step valid also on superpositions. It does not clone an
arbitrary quantum state or measure data. Zero padding is allocated/countable.

Define ACC(u,v,t,sign) for two m-word bands and a 2m-word target band.
It must restore both input bands and add sign times their polynomial
convolution to t modulo R coefficient by coefficient. Sign is classically
+1 or-1. At m=1 compute the product of the two A-bit input words into
clean scratch by schoolbook Boolean multiplication, add or subtract it into
the B-bit target word t_0 modulo R, then uncompute the product scratch.
The second target word is untouched. This costs O(log^2(v+2)) logical gates
and scratch bits when A,B=O(log(v+2)); the Boolean schoolbook circuit retains
its O(A^2) gate values, copies the product and reverses them. Ripple modular
addition on B bits is an exact in-place permutation using O(B) gates/scratch.
Fixed-size Boolean operations use NOT/CNOT/Toffoli with exact Clifford+T.

For m=2h execute the following fixed sequence. Every indicated word addition
or subtraction is modulo its allocated word width. The input sum operations
are in their A-bit bands; the output operations are in B-bit words.

1. For i=0,...,3h-1 in INCREASING order, add t_i to t_(i+h).
2. Recurse ACC(u_low,v_low,t[0:2h],sign).
3. Recurse ACC(u_high,v_high,t[h:3h],-sign).
4. For i=3h-1,...,0 in DECREASING order, subtract t_i from t_(i+h).
5. For each i<h add u_(i+h) to u_i and v_(i+h) to v_i.
6. Recurse ACC(u_low,v_low,t[h:3h],sign) using those modified low bands.
7. Subtract the unchanged high bands to restore both low input bands.

These are the actual loop orders and target ranges; there is no hidden
recursive product register. Each recursive target has exactly twice its
input word count. All target coefficient indices use views into the one
allocated top-level band. Classical sign controls addition versus subtraction.
Reversing the entire gate stream implements the inverse. The only base-case
products are fully accounted for, and their scratch is reused serially.

## Algebraic verification and padding

View target coefficients as a polynomial modulo X^(4h) over Z/RZ. Step1
is multiplication by (1-X^h)^(-1): increasing indices propagate each
coefficient through all later h-shifted positions. Step4 is its inverse,
multiplication by (1-X^h), using decreasing order. For a split
u=a+X^h b and v=x+X^h y, the first two recursive additions followed by
step4 contribute

 sign*(1-X^h)*(ax-X^h by).

The third contributes sign*X^h(a+b)(x+y). Their sum is exactly
sign*(a+X^h b)(x+X^h y). Existing target contents are restored by the
inverse shears; the transformation therefore adds the convolution to an
ARBITRARY initial target, not merely to zero. Induction establishes ACC.
This identity is over the coefficient ring, so intermediate negative values
and modular wraparound are harmless. All maps are reversible on their full
encoded registers; there is no truncating irreversible carry discard.

During input sum operations each digit is a sum of at most m original
w-bit digits, hence is <m*2^w<2^A. Input sums do not wrap on the initialized
padded bands, and their later subtraction restores them exactly. The final
target with initial zero contains actual nonnegative convolution coefficients
c_i<m*2^(2w)<2^B. Thus their ring representation is the exact integer value
when accumulation completes, despite any intermediate modular wrap.
The initially padded input bands can be cleared by their original input bits
after ACC returns, or retained for the reverse pass described next.

## Clean linear-size normalization

At top level only, start a zero padded target band and perform ACC once.
Normalize its coefficients into ordinary base-2^w product digits by a forward
scan. Start carry=0; at word i compute d_i=(c_i+carry) mod2^w and next
carry=floor((c_i+carry)/2^w). The carry and intermediate sums have O(log(v+2))
bits. For example c_i<2^B and induction gives carry<2^B, so B+1-bit sums
suffice. There are 2m words, and the true product is <2^(2mw), so final
carry after the top digit is zero. Each word's addition/split is an ordinary
Boolean ripple circuit. Retain ALL its gate values and carry history until
the product digits have been XORed into the desired 2v-bit target, then
reverse the entire normalization. This costs O(m log(v+2))=O(v) logical
gates and retained work bits. There is no separate full-width addition for
every coefficient. The extra normalized high digits are zero for v-bit
inputs and may be left as work until the reverse normalization clears them.

Reverse ACC to clear the padded coefficient band, and clear the padded
input copies. The resulting exact clean map is
(a,b,z)->(a,b,z XOR (a*b)) on ordinary fixed-length integers, with all
scratch returned to zero. The target need not initially be zero. If a
constant is one operand, load its computational-basis bits using counted X
gates and clear them after the inverse work. No approximation, quantum
Fourier transform, arbitrary rotation or measurement is used in the product.

## Gate, space and uniform generation bounds

With global A,B=O(log(v+2)), let C(k) count logical gates for a k-word ACC.
The explicit loops give C(k)<=3C(k/2)+O(k log(v+2)), with
C(1)=O(log^2(v+2)). Therefore

 C(m)=O(m^(log2 3) log^2(v+2))
     =O(v^(log2 3) (log(v+2))^(2-log2 3)).

The top normalization and reverse at most double this cost plus O(v).
Since 2^8=256>243=3^5, log2 3<8/5. The positive power slack absorbs
that fixed logarithmic factor, proving a supported conservative logical
bound O(v^(8/5)). The more detailed logarithmic expression is retained
here and not misrepresented as a different actual routine. The n=1 or
other fixed small operand sizes use schoolbook multiplication directly.

The two padded inputs use 2mA=O(v) qubits; target coefficients use
2mB=O(v); normalization history uses O(v). Each base has only
O(log^2(v+2)) scratch, reused, and ripple word-add scratch is O(log(v+2)).
No quantum register is allocated per recursive call. A classical depth-first
stack stores O(log(v+2)) frames of O(log(v+2))-bit word bases, lengths,
stage and sign. Its O(log^2(v+2)) bits are counted in classical space.
The word operations use complete ripple/compute-swap-inverse circuits, so
the gate count includes CNOT, NOT, Toffoli decomposition and uncomputation,
not only T count or depth. All parallel operations are serialized/count-summed.

For uniform generation, maintain band bases as integers and advance them by
word width during each scan; recursion splits add fixed half-band offsets.
Emit each ripple gate using base+local-bit addresses. Prepare offsets using
counted additions; no per-gate large index multiplication is used. Frame
updates are O(log(v+2)) Boolean steps and happen at most once per recursive
node, already dominated by the word/base gates. All index operations and
their own accesses pay the model's full O(log(n+2)) address width in the
whole RLQGR2 allocation. The proof.md O(log^2(n+2)) overhead per logical
gate is therefore sufficient. Descriptions are streamed, not exponentially
stored, and original words, normalization history and controller are included
before the memory address bound is applied.

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
costs O(n^(8/5)) logical gates, INCLUDING all inverse work.

The reciprocal generation has polynomial charged work and O(n) classical
space, included in preprocessing. Its bits are constants, not instance-
dependent advice or a free oracle. Power-of-two quotients use bit copies,
not division calls. The final quotient/remainder correction is exact, with
no probability or numerical precision assumption. This completes the
counted modular-product implementation used once per classical score record.
