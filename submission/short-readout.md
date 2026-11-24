# Short label readout and charged source arithmetic

Use this module to implement every native source readout and odd-part
source multiplier in pair-buckets.md. The score uses the exact arithmetic
in fast-score-arithmetic.md. All changes preserve the ideal label law
and phase formulas per clean copy, with the reported label errors
handled by the replacement budget instead of a global error-free event.

## Copywise precision

Set the BASE13 precision parameter to C=2^40, independent of the
number of source copies. The required exponent and number of collective
probe rounds are h_read=ceil(log2(2^16 C(n+5))) and F=2^21 h_read.
Thus F=O(log(n+2)). The usual proof, including the native diagonal
translation law and exact dyadic lift, yields per-copy label error
at most 1/(2^14 C)<=2^-54. It applies in the clean good marginal for
each position including a public modulus-unit multiplier. Neither
that error estimate nor the row phase conditional on a latent label
assumes conditioning on other record outcomes. Markov suffices for
the required simultaneous bound on counts. The physical instrument
uses the same bounded iterations for all reports.

Inside one collective round, generate the exact O(n) Clifford+T
translation and measure the n+5 probes. Maintain the O(n) empirical
counters with O(log F) bits each, using O(n polylog(n+2)) total
work per whole round including addressed accesses and uniform gate
emission. Compare the two empirical fractions at a level with the
finite rational direction table using ordinary arithmetic of
O(log F) width and fixed table precision. There are O(n) levels.
The table's size does not depend on n and its evaluation and
initialization are counted. This part of the source readout uses
O(n polylog(n+2)) work in total.

## Linear-pass dyadic lift

As in BASE13, retain one six-bit alpha_j direction for each
level. Write the current g_(j+1) as its exact represented dyadic
fraction, initially alpha_(n+4). The two possible lifts are y =
g_(j+1)/2 and y+1/2. The first is nearer in circular distance to
alpha_j exactly when y is in the closed half-circle centered at
alpha_j, with either boundary tie decided in favor of the first.
The two endpoints have six-bit fractional representations since
they are alpha_j plus or minus one quarter modulo one. Thus all
comparisons can use the first six bits of y and a bit indicating
whether any less significant bit is one. With equal six-bit prefix,
this bit distinguishes exact endpoint equality from strictly above.
Choose the usual union of two intervals when the half-circle wraps.
No approximation to the lift decision is made, even on an arbitrary
transcript.

Prepending zero to the fraction bits gives y, and prepending one
gives y+1/2. The first six bits after a prepend are the new bit
followed by the old first five bits. The less-significant flag
is the old flag OR the old sixth bit. Retain also the full final
dyadic numerator by appending the prepended bits to an ordinary
classical buffer in little-endian order, one update per level.
This requires O(n) bits and O(n polylog(n+2)) work, including the
addressed read of each direction and bit write. At the end compute
the one integer product of the numerator and N with the exact
interpolated multiplication. Fixed-width rounding of its high bits
implements floor(N*g_0+1/2), and reduce a result N to zero. To use
that circuit on basis integers write the temporary operand registers
by addressed X gates and read the product, then reset the readout
workspace. This costs O(n^(5/4)) counted work and O(n) qubits.
The entire readout per processed source therefore takes O(n^(5/4))
time, with O(n^2) classical and O(n) quantum scratch at most.

## Public unit multipliers and selected cells

Make the source position permutation u->alpha u mod N for u<N
and identity on padding. Compute the product and exact modular
remainder into auxiliary registers using fast-score-arithmetic.md.
Copy logically selected output, either that residue or input u on
padding, into a clean word, then reverse scratch. Exchange the two
words and clear the old input using the same procedure with alpha
inverse modulo N. The fixed input flag and the other local scratch
are clear. All steps implement the exact modular permutation on
arbitrary inputs including padding, and the O(n^(5/4)) work and
O(n) qubit bounds of the module include all three-product residue
computations. Stage-dependent alpha and inverse and integer
reciprocals are computed classically once per stage using polynomial
work. The number of stages is bounded by an absolute constant.

At the start of a stage sort its K sampled cell indices
classically, retain repeats as multiplicities, and use binary
search on the sorted distinct indices for each raw copy's cell.
All comparisons use O(n)-bit values with O(log(n+2)) address width.
Initialization and sorting are polynomial in n, performed once
per stage, not once per raw source. A single lookup uses O(log K)
comparisons, each O(n polylog(n+2)) bit work including control.
Counters for the round and copy require O(n) bits and polynomial-log
controller overhead per indexed bit. When a raw position
has a selected cell, update its record, keeping a maximum of two
row qubits and the occupancy count. Likewise finish selected
cells by advancing through the sorted indices, without a full scan
per raw report or per round. The total fixed-order bookkeeping,
report handling, label subtraction and record copying fit
O(M n polylog(n+2)) over a stage, and retain the same O(n^2)
classical and O(n) quantum storage. One can implement the sorted
array by ordinary insertion sort because its cost is only
polynomial preprocessing. There is no coherent lookup oracle.

Use the same interpolated product and reduction inside each
coherent score predicate. The K=O(n) records cost O(n^(9/4))
work per score pass with the proof's exact flags and sign tests.
Checking measured outputs can use ordinary polynomial arithmetic
because the number of classical checks is polynomial in n.
All exponentials arise only in M copy requests and the bounded
square-root search. With h=n-floor(n/3) and the unchanged M,
both totals are at most O(2^(n/3)n^(9/4)). Acquisition and both
space guarantees are the same for this implementation.
