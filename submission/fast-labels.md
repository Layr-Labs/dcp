# PG3: coherent source powers, truncated Fourier blocks and exact fast rounding

These lemmas replace the PG2 physical source circuit and its work accounting;
the original spectral ensemble, minimum-depth sieve, quotas, preparation of one
approximate gradient, all-acquisitions sample count and final verification are
unchanged. Everything is a uniform Clifford+T/classical bit construction.

## A. Apply all phase-estimation powers with one coherent modular translation

Keep a=clog(2^20 R), t=n+a+4, m=floor(log2 N). The phase input K is t qubits
in |+>^t. Instead of t separate controlled translations, implement

    |k>|x> -> |k>|(x+k) mod N>, x<N,
    |k>|x> -> |k>|x>, x>=N.

This is a permutation on the entire encoded domain for each k. On chi_y the
translation by k has eigenvalue exp(2pi i*k*y/N); hence it produces exactly
the same joint phase-estimation state as the product of controlled powers.
No coherent source operation beyond arithmetic on its acquired data is used.

To compute r=k mod N, use restoring division on a t-bit working integer W
initially equal to k. For j=t-m-1,...,0 compare W with N*2^j and subtract that
threshold exactly when W is at least the threshold. Initially W<2^t<=2N*2^j.
After a stage W<N*2^j; this is twice the next threshold. Induction proves that
one subtraction per stage suffices and the final W is in [0,N), congruent to k.
The threshold is a t-bit integer. Each comparison/conditional subtraction uses
O(t) Boolean gates and wires. There are t-m=O(sqrt(n)) stages because
m>=n-1 and a=O(sqrt(n)). The total Boolean circuit has O(n^(3/2)) gates.

Evaluate that circuit reversibly into a clean remainder register, retaining
intermediate Boolean values, copying the remainder, and reversing to clear
all division garbage. Keep k unchanged. The resulting r<N can be used as a
quantum addend in the modular permutation of proof.md Section 2: replace its
constant c by r in the displayed arithmetic/MUX formulas. They are still
identities on basis states, including r=0 and invalid x encodings. For each
fixed r the subtraction formula is the inverse. Compute/swap/inverse therefore
implements the in-place controlled modular permutation with O(n) further
gates and clean scratch. Finally uncompute r using the unchanged k. All gates
are exact Clifford+T after the same Boolean decomposition. The entire controlled
power operation has O(n^(3/2)) gates and temporary qubits, with no stored
exponential circuit or table. The nested finite division loops and their
reverse can be streamed from their bit indices and block bases.

## B. Truncate the binary Fourier circuit with a global error bound

Define b=min(t,clog(2^30 R*t)). Prepare one actual b-qubit gradient by the
bounded rational preparation already specified for PG2. In the inverse Fourier
circuit omit only controlled phases with denominator larger than 2^b. A pivot
formerly had a phase block exp(+-2pi i*B*x_low/2^(j+1)). If j+1>b, retain only
bits k>=j+1-b of x_low. The retained block is exp(+-2pi i*B*x_keep/2^b).
If j+1<=b, keep the block exactly using the corresponding shift into the b-bit
gradient. Each retained pivot block is one O(b)-gate controlled addition.
There are t pivots, so the logical gate count is O(t*b)=O(n^(3/2)); bit reversal
and H gates are included. Here b=O(sqrt(n)) follows from log R=O(sqrt(n)) and
log t=O(log n). The min handles all finite parameter values.

For one pivot the sum of omitted rotation angles is at most
2pi*sum_(d=b+1)^infinity 2^-d=2pi*2^-b<8*2^-b. For diagonal phases,
|exp(iu)-1|<=|u| gives the same operator-norm bound. Telescoping products of
unitaries give total operator error at most 8t*2^-b for one inverse Fourier
circuit. If b=t no phase is omitted and its error is zero; otherwise by the
choice of b the total across at most R invocations is at most 2^-27.
The same telescoping argument applies to adaptive algorithms: purify all
measurements as isometries retaining their records, control future operations
on those records, and include unused slots as identities up to the fixed R cap.
Equivalently, each invocation changes any output distribution by at most its
operator error and contractivity handles the remaining channel.

Only the ideal b-bit gradient is assumed unchanged and uncorrelated by every
retained phase block. The actual gradient's single global comparison error and
bounded preparation abort stay below 2^-36 and 2^-122 as in PG2, independently
of b and the number of uses. Combining ideal QPE residue error (<2^-23 over
all acquisitions), Fourier truncation (<=2^-27), gradient distance (<2^-36)
and preparation abort (<2^-122) is strictly less than 1/1024. Thus the original
five-budget full-secret success guarantee of at least 1019/1024 is preserved.
No actual imperfect register is assumed refreshed after a use.

## C. Exact rounding with a proved O(n^(3/2)) classical multiplication

Rounding N*Z/2^t must be charged. Schoolbook multiplication would exceed the
new per-label budget, so use the following explicit three-way integer product
algorithm, with signed recursion as needed. For nonnegative A,B of bit length
at most v, choose k=ceil(v/3), base D=2^k, and write

    A=A0+A1*D+A2*D^2, B=B0+B1*D+B2*D^2.

Their product polynomial has coefficients c0,...,c4. Recursively compute the
five products at evaluation points 0,1,-1,2,infinity:

    c0=A0*B0, c4=A2*B2,
    V1=(A0+A1+A2)*(B0+B1+B2),
    Vm=(A0-A1+A2)*(B0-B1+B2),
    V2=(A0+2A1+4A2)*(B0+2B1+4B2).

Signed arguments are reduced to absolute values with a sign bit. Recover

    u=(V1-Vm)/2,
    c2=(V1+Vm)/2-c0-c4,
    w=(V2-c0-16c4)/2,
    c3=(w-u-2c2)/3,
    c1=u-c3.

Substitution of the polynomial evaluation identities proves every division is
exact and these are the product coefficients. Recombine sum_i c_i D^i by
ordinary shifts and additions, including carries. Division by the fixed
integers 2 or 3 is a linear-time binary operation: scan the bits maintaining
a remainder of at most two, emitting the quotient bit. All additions,
subtractions, evaluations and recombination use O(v) bit work. Each recursive
argument has bit length at most ceil(v/3)+3 because the largest evaluation
magnitude is <7*2^k. Use ordinary multiplication below a fixed threshold,
for example v<=32, whose cost is an absolute finite constant.

Consequently the bit-work recurrence is

    C(v) <= 5*C(ceil(v/3)+3)+O(v).

It proves C(v)=O(v^(3/2)), with an explicit rational power, rather than an
uncounted multiplication oracle. For v>32 set z=v-6. Since ceil(v/3)+3<=v/3+4,
the child parameter minus six is at most z/3. The strict inequality
5/3^(3/2)<1 follows from 25<27. Induction with a sufficiently large absolute
outer constant bounds the five child costs plus O(v) by a multiple of
(v-6)^(3/2); finitely many base sizes are absorbed. Standard depth-first
evaluation retains only a constant number of O(v)-bit intermediates per level;
the sizes decrease geometrically, so O(v) working bits suffice. The recursion
is uniform and every sign, carry and exact quotient is handled by the stated
bit operations.

Here v=O(n), because t=O(n). Compute the product P=N*Z by this algorithm.
Then the nearest integer with ties toward the smaller is

    q=floor((P+2^(t-1)-1)/2^t).

The formula holds for integer P by its remainder modulo 2^t; at a halfway
remainder 2^(t-1) it rounds down. A power-of-two quotient is a bit selection,
not a division subroutine. The result lies in [0,N], and q=N is replaced by
zero to obtain the residue. These remaining steps use O(n) bit work.

## D. Joint charged cost

Coherent modular translation, truncated binary Fourier transform and exact
rounding each use O(n^(3/2)) logical bit/gate operations. The full streamed
address-generation allowance is O(A_addr^2)=O(n) charged work per operation,
including each classical bit access. Thus per acquired source label work is
O(n^(5/2)), and all R=O(nL_0) extractions cost O(n^(7/2)L_0). Parameter
computation, source charge, resets and measurement are within this budget.
The unchanged sieve already costs O(n^(7/2)L_0), and final verification is
smaller. Hence total work is

    T=O(n^(7/2)L_0)=O(n^4 2^((244949/100000)sqrt(n))).

Quantum scratch for the reversible division has grown to O(n^(3/2)); it must
be counted rather than described as O(n). It is nevertheless O(L_0) since the
same exact quotas grow exponentially in sqrt(n). Therefore peak quantum space
is O(L_0+n^(3/2))=O(L_0), and the existing stated quantum envelope is unchanged.
Classical controller space and fast-multiplication scratch are polynomial and
fit O(nL_0). Total allocated memory remains O(nL_0), which justifies the same
O(sqrt(n)) address length. No different cost model or access primitive is used.
All loops, attempts and allocations are capped; these are branchwise bounds.
All acquired source copies are counted by the unchanged addendum; the new
preprocessing, arithmetic and Fourier circuit acquire none.
