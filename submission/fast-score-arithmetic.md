# Linear-space exact modular product for the coherent score

Replace each schoolbook modular product in the phase-mark predicate
by the following exact reversible reduction. Keep the stored record
layout, score tables, thresholds, candidate-index conversion, and
checked Grover trials. This change concerns arithmetic after the
physical data acquisition, with the same score on every possible
record and candidate, including malformed records.

## Exact multiplication subroutine and cost model

For bit width w>=2 let b=ceil(log2(w+1)) and let m be the least power of two with mb>=w. Set t=2b+ceil(log2 m)+1 and work with coefficients in the ring R=Z/(2^t). Encode each operand as m base-2^b digits, stored in t-bit coefficient registers. The two input digit arrays and a 2m-coefficient accumulator use O(mt)=O(w) qubits. An addition or subtraction into one coefficient is the exact modulo-2^t ripple permutation, implemented with fresh carry scratch followed by inverse cleanup. All operations on the polynomial coefficients use that ring, including intermediate negative values. No assumption about an unwrapped intermediate coefficient or an integer carry between adjacent coefficients is needed.

For a recursive call of size k=2h, split the operands into polynomials a+X^h b1 and c+X^h d, with each of a,b1,c,d supported below degree h. View the 2k output slots as R[X]/(X^(2k)). To add the product, the mathematical identity is

    (1-X^h) (a*c - X^h*b1*d) + X^h*(a+b1)*(c+d).

Write Z=X^h and let the coefficient shift operator be Shift by h, truncated at the end of the current output view. The inverse of I-Shift is I+Shift+Shift^2+Shift^3 since Shift^4=0. Implement that inverse by visiting target coefficients in ascending order from h to 4h-1 and adding the current coefficient h positions earlier. At each step the source coefficient has already received its own earlier shifts when applicable. Implement I-Shift by the inverse traversal, visiting the same targets in descending order and subtracting the still-current earlier coefficient. Each is 3h word additions or subtractions, with no nonlocal carry. The physical sequence on this output view is:

1. Apply the ascending transform.
2. Recurse to add a*c into output words [0,2h), and use the inverse of the other recursive product circuit to subtract b1*d in [h,3h).
3. Apply the descending transform.
4. Replace a and c temporarily by a+b1 and c+d, by wordwise modular additions from their untouched upper halves. Recurse to add their product in [h,3h) and then restore a and c by wordwise subtraction.

The adjacent transforms conjugate the two signed product additions by I-Shift, and the last recursion adds the remaining identity term. A child product is supported below degree 2h, even for modular polynomial coefficients, so no recursive product reaches outside its explicitly named slice. The child action preserves the input words already present at its entry and adds to an arbitrary existing output. The inverse of a child circuit subtracts the same product and restores the inputs. At k=1 multiply two t-bit words and accumulate the low t bits into the first output coefficient. This can be done by schoolbook controlled ripple additions in O(t^2) gates with O(t) scratch and no change to the second output coefficient. For example for each bit pair grouped by the first operand bit, conditionally add the shifted second operand to the first output word, using an exact reversible ripple adder. Thus the entire recursion is an exact clean-input-preserving permutation, including on arbitrary accumulators. Its reverse is defined by reversing the gate visitation order and replacing each gate by its exact inverse.

No call allocates another polynomial or copies a subproduct. All retained working arrays are the original O(mt) words in bit count, plus reusable O(t) carry scratch for one local adder. Child output slices can overlap across different calls since those calls are consecutive. The recursion stack contains only classical slices, signs, and positions. Over sizes k the gate count satisfies G(k)<=3G(k/2)+O(kt) with G(1)=O(t^2); hence G(m)=O(m^(log2 3)t^2). The controller stores O(log w) stack frames of O(log w) bits each and emits both forward and inverse gates from these descriptions. Word-base address calculations, loop counters and every accessed bit and addressed gate cost at most a fixed power of log(w+2) per emitted gate. This includes sign or direction handling in a recursive inverse call. There is no stored list of gates.

Start the accumulator at zero. Each final convolution coefficient of the original digits, as an ordinary nonnegative integer, is at most m(2^b-1)^2<2^t. Its ring residue therefore determines that integer exactly. Pack these coefficients into binary output with one sequential carry pass. Set carry C0=0. For index i compute E_i=T_i+C_i in a fresh (t+1)-bit temporary, copy the low b bits to the output digit, save C_(i+1)=floor(E_i/2^b) in the carry tape, and reverse the addition into E_i. Each carry is below 2^t by induction. Retain the carry tape of O(mt) bits, then clear it in reverse order by recomputing the temporary sum, clearing the saved carry, and reversing its recomputation. At each reverse step the earlier carry is still present. The binary output is left intact because its bits are not needed to clear any carry. The total value of the original product is below 2^(2mb), so it fits in the 2m output digits. Then run the inverse polynomial computation to clear the accumulator and erase the operand digit encodings by undoing the original input copies. This gives a clean reversible ordinary product with O(w) qubits, including outputs and all padding, and at most O(m^(log2 3) t^2+mt) Boolean gates. The modular coefficient recursion adapts the inline product accumulation idea of Craig Gidney, [Asymptotically Efficient Quantum Karatsuba Multiplication](https://arxiv.org/abs/1904.07356).

Constant classical operands can first be written in quantum basis registers using X gates and cleared after the inverse. Since 3^5<2^8, the strict gap log2 3<8/5 absorbs all fixed polylogarithmic gate-controller and address charges. For w=O(n), the charged uniform work of one ordinary multiplication is therefore O(n^(8/5)). Wires and both operands with widths up to a fixed multiple of n, and all uncomputations, are included in this envelope.

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

When a residual score needs the full-secret candidate c+M0*t,
compute its product M0*t first by the same reversible multiplication
into fresh O(n)-bit workspace, then add c by a ripple adder. On valid
t the result lies in [0,N); on padding retain enough bits and carry
the validity flag as before. The output is uncomputed after the
predicate. Odd-stage modular products with power-of-two moduli can
either use the same exact reduction or copy the product's low bits.
Every per-record table lookup uses the existing constant-size list
of exact rational threshold comparisons. Forward and reverse score
passes therefore cost O(n^(13/5)) work for K=O(n) records, inclusive
of classical emission and all address charges. The linear quantum
space and the classical O(n^2) record storage are preserved.
