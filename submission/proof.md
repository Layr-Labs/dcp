# RWT-S16: one retained threshold witness, sixteen-part error tolerance

## 1. Joint theorem and exact hypotheses

For every integer N >= 2 and every secret s in Z/NZ, put n=ceil(log2 N),
k=2(n+16), h=floor(k/16), and L=2^n. RWT-S16 below acquires exactly k
source registers once, and outputs the entire secret with unconditional
probability at least 95/128 > 2/3. In the charged uniform Clifford+T and
classical bit-operation model of rules.md it has simultaneous worst-case bounds

    T = O(2^(n/2) n^2 (log2(n+2))^2),
    S_C = O(n) bits, S_Q = O(n^2) qubits, Q = 2(n+16) = O(n).

All constants are independent of N, s, the adversary and outcomes. For n>=2
the time representative is B_T(n)=2^(n/2)n^2(log2 n)^2; set B_T(1)=1.
The shifted logarithm gives an all-bit-length bound and is equivalent in
big-O to that representative. The other representatives are n, n^2, n.
Their exact growth indices are respectively 1,0,0,0.

The ideal density matrix used throughout is
rho_s=(1/N) sum_(x=0)^(N-1) |psi_(x,s)><psi_(x,s)|, where
|psi_(x,s)>=(|0,x>+|1,(x+s) mod N>)/sqrt(2). These are exactly the
input states in rules.md, Problem and goal; the charged costs are those in
rules.md, Computation and resources. Neither x nor source preparation data
is an algorithm input.

The guaranteed malformed fraction is epsilon(n)=1/16. Its precise model text is:

> Among the Q acquired copies, an adversary fixes a set B of at most floor(epsilon(n) Q) malformed positions, possibly depending on N and s. The joint state is arbitrary subject to its reduced state on all other positions being exactly rho_s^{tensor (Q-|B|)}. Malformed systems may be correlated or entangled with each other and with other systems subject to that marginal promise. No source control, purification access, or preparation inverse is supplied.

Here each source position has exactly one first qubit and n data qubits, even
when malformed. The entire acquisition finishes before any witness test; there
is no replacement of registers during computation. Writing b=|B| and g=k-b,
the only state promise is that the good-position marginal of the joint density
matrix sigma is rho_s^(tensor g), with b<=h. These quantifiers allow arbitrary
bad registers and correlations consistent with that marginal. The original
clean source is the case B empty. This is a global fraction promise, not an
independent stochastic corruption probability. No access to B is provided.

## 2. One-copy test and threshold estimate

For each valid candidate t<N define the unitary C_t on a source register by
subtracting t modulo N from its data y when its first bit is 1 and y<N.
For first bit 0 or invalid y>=N it is identity. Define C_t also to be identity
for t>=N. These definitions are permutations of every n-bit encoding, with
inverse controlled addition modulo N on the same valid range. Set, for t<N,

    P_t = C_t^dagger (|+><+| tensor I) C_t.

On an ideal component (|0,x>+|1,x+s mod N>)/sqrt(2), applying C_t gives
(|0,x>+|1,x+s-t mod N>)/sqrt(2). If t=s this is |+>|x>; if t!=s
the two data labels differ, so the first qubit's X-basis outcome is fair.
Thus P_s is identity on the support of rho_s, and Tr(P_t rho_s)=1/2 for
wrong t. Projectors on different copies commute. On the product good marginal,
wrong-t failure outcomes are independent fair bits.

Let Pi_t be the joint projector that at most h of the k single-copy P_t tests
fail (at least k-h pass). For t>=N set Pi_t=0. For every promised sigma,

    Pi_s sigma = sigma,
    Tr(Pi_t sigma) <= delta := 2^(-n-16) for t!=s.                 (1)

To prove the first assertion, let G be the product of P_s on good positions
and identity on bad ones. The good marginal gives Tr((I-G)sigma)=0.
Since sigma is positive, (I-G)sigma^(1/2)=0 (its squared Hilbert-Schmidt
norm is zero), whence G sigma=sigma. Every vector in this support can fail
only on b<=h bad positions. Therefore Pi_s G=G and Pi_s sigma=sigma.
This remains valid even when good and bad systems are entangled.

For wrong t, threshold acceptance implies that the number F of failures on
good positions is <=h, regardless of the bad positions. The threshold
projector is bounded above by that good-count projector tensor identity
on bad positions. The marginal promise makes F~Binomial(g,1/2).
For z=1/15, the event F<=h implies z^F>=z^h. Markov's elementary inequality
(applied to the nonnegative variable z^F) gives

    Pr(F<=h) <= z^(-h) E[z^F] = 15^h (8/15)^g
      <= (8/15)^k (225/8)^h
      <= [(8/15)(225/8)^(1/16)]^k < 2^(-k/2).

The middle inequality uses g=k-b>=k-h and 8/15<1; the last uses h<=k/16.
The strict base comparison is exact: raising it to power 16 reduces it to

    2^53 < 15^14,
    9007199254740992 < 29192926025390625.

Since k/2=n+16 this proves (1), without an external concentration premise.

## 3. Complete algorithm and coherent circuit

Acquire all k copies and keep them as witness W. Compute all integer parameters
from N; no advice or tables are supplied.

If N=2, perform H and computational-basis measurement on every first qubit
(the t=0 test). Output 0 if at most h outcomes are 1, otherwise output 1.
All k copies are acquired and tested, without early stopping. If s=0 the
threshold always passes. If s=1 its probability of passing is <=delta=2^-17
by (1). This branch therefore exceeds the joint theorem's success bound.

For N>=3, compute r as the largest nonnegative integer satisfying
16r^2<=9L, equivalently r=floor(3 sqrt(L)/4). Integer binary search and
schoolbook squaring compute it exactly; no real arithmetic is needed.
Initialize an n-qubit candidate register A with H on every qubit to give
|u>=L^(-1/2) sum_(t=0)^(L-1)|t>. Define

    R = I - 2 sum_t |t><t|_A tensor Pi_t,
    D = (2|u><u|-I)_A tensor I_W.

Apply DR exactly r times, then measure A. Output that integer if it is below
N, otherwise output 0. There are no restarts, additional verification passes,
postselection, extra copies or outcome-dependent loop lengths.

To implement R, compute the flag [t<N] coherently. On every witness copy,
apply C_t followed by H on its first qubit. Reversibly count how many of those
first qubits are 1. Apply a minus phase if the valid flag is true and this
count is <=h; reverse the count computation, every H and every C_t, and
clear the flag. This gives precisely R: the first-qubit-zero projector is
conjugated to P_t. Invalid candidates have no marked subspace. Data encodings
outside the modulus remain unitary even for arbitrary malformed inputs.

The diffusion D is H on all candidate qubits, a zero-string phase reflection,
and H again, with a fixed global sign that does not affect output probabilities.
A linear chain of Toffoli gates implements the multi-controlled phase using
O(n) clean scratch, and uncomputes it. All circuits below use exact Clifford+T.
No quantum-addressed memory primitive or preparation inverse is used.

## 4. Repeated-witness disturbance and unconditional success

For analysis alone choose a purification |Omega> of sigma on an inaccessible
reference E. This is a mathematical device, not an algorithm input. Equation
(1) implies Pi_s|Omega>=|Omega> and ||Pi_t|Omega>||^2<=delta for wrong t.
Let R*=(I-2|s><s|)_A tensor I_W be a comparison oracle, never implemented.
For any normalized candidate state |v>=sum_t v_t|t>, orthogonality of the
candidate labels gives

    ||(R-R*)|v,Omega>||^2
      = 4 sum_(t!=s) |v_t|^2 Tr(Pi_t sigma) <= 4 delta.           (2)

Put V=DR and V*=DR*. In the ideal comparison computation W,E stay fixed,
so every intermediate state is |v_j,Omega>. The identity

    V^r-(V*)^r = sum_(j=0)^(r-1) V^(r-1-j)(V-V*)(V*)^j

and unitarity, applied to the initial state, prove

    ||V^r|u,Omega>-(V*)^r|u,Omega>||
       <= 2r sqrt(delta) <= 3/512 < 1/128.                      (3)

No product-state or independence assumption is made about actual intermediate
states; their disturbance and entanglement are covered by this telescoping
bound. It does not count only the first use of the witness.

Here is the ideal-search success calculation, reproduced rather than imported
as an oracle-complexity assumption. In the basis |s>, |w>, with |w> the
normalized uniform superposition of all other candidate labels, write
|u>=sin(theta)|s>+cos(theta)|w>, theta=arcsin(1/sqrt(L)). The reflection R*
is diag(-1,1), and multiplication by D rotates this vector to
sin((2j+1)theta)|s>+cos((2j+1)theta)|w> after j iterations. Thus the success
probability after r iterations is sin^2((2r+1)theta).

For L=4, r=1 and success is 1. For L=8, r=2 and success is 121/128,
using sin(5theta)=11/(4 sqrt(8)). For L>=16, integrating the increasing
derivative of arcsin on [0,1/sqrt(L)] gives

    1/sqrt(L) <= theta <= 1/sqrt(L-1) <= 16/(15 sqrt(L)).

Since 3sqrt(L)/4-1<r<=3sqrt(L)/4,

    5/4 <= (2r+1)theta <= 28/15.

Indeed the lower bound follows from 3/2-1/sqrt(L)>=5/4, and the upper
from (3/2+1/sqrt(L))*16/15<=28/15. This interval lies inside
[pi/3,2pi/3] (the elementary bounds 3<pi<22/7 suffice). Ideal success is
therefore >=3/4 for every N>=3, including non-powers of two.

For normalized pure states the trace distance equals
sqrt(1-|<a|b>|^2) and is <=||a-b||, since |<a|b>|^2>=2 Re<a|b>-1.
Any event probability changes by at most that distance; tracing out W,E cannot
increase it. Equation (3) therefore reduces the probability of A=s by less
than 1/128. The measured-candidate success is at least 95/128. Mapping an
invalid encoding to 0 cannot remove the event A=s. Together with the N=2
branch this proves the full theorem under every promised state.

## 5. Exact reversible arithmetic and charged uniform costs

A fixed number of n+2-bit ripple additions/subtractions, comparisons and
bitwise selections computes the controlled permutations and their inverses.
For subtraction, choose y-t when y>=t and y+N-t otherwise, on the valid
range; for addition reduce y+t once if it is >=N. Compute the validity
flags [y<N], [t<N] and the first-bit control; use identity otherwise.
Each ripple operation has O(n) Boolean gates and O(n) retained intermediate
bits. Its inputs include coherent t and the source bit; neither is measured.

Reversible Boolean evaluation stores intermediate gate values, XORs its output
into a zero target, then reverses the evaluation. NOT, CNOT and Toffoli suffice.
For a permutation f, compute f(y) into zero Z, swap Y,Z, and XOR f^(-1)(Y)
into Z to clear the old y. Use the same preserved control in the inverse.
This realizes C_t with O(n) gates and O(n) reusable scratch, on all encodings.
Toffoli is exact constant-size Clifford+T: conjugate CCZ by H on its target;
CCZ is synthesized by computing the seven parities in

    4abc = a+b+c-(a xor b)-(a xor c)-(b xor c)+(a xor b xor c)

and applying T or T^dagger to each parity and uncomputing. Each parity has
constant size. This identity supplies phase (-1)^(abc) and needs only constant
scratch; no approximate rotations, precision assumption or synthesis table.

Use a ceil(log2(k+1))-bit threshold counter. Add each first-qubit-one indicator
with a controlled ripple increment, using O(log(k+2)) gates and reusable
scratch. Compare to h, apply Z on the computed phase flag, and reverse
comparison and increments. Counter overflow never occurs because k fits.
The threshold and its reverse cost O(k log(k+2)) gates. Consequently each
iterate costs O(kn+k log(k+2)+n)=O(n^2) exact gates.

All k(n+1) retained witness qubits, including idle ones, are counted.
Candidate, modular scratch, flags and counter add O(n) qubits. Peak quantum
allocation is O(n^2). The controller stores N (up to n+1 bits), n,k,h,r,
iteration/copy/ripple counters, O(n)-bit integer-arithmetic scratch and one
gate descriptor, totaling O(n) classical bits. It streams the regular circuit
and regenerates inverse passes; it stores no complete circuit or sample table.
Measurement results in the N=2 branch are counted and discarded one at a time.

Here addressing is charged explicitly. Total allocated bits and qubits
M=O(n^2), hence each address has O(log2(n+2)) bits. Gates' wire indices are
obtained from a copy's fixed base and ripple offsets. Maintain the base while
scanning a copy and increment offsets rather than multiplying for every gate.
At a copy boundary even schoolbook multiplication of O(log(n+2))-bit indices,
with addressing charged per bit operation, costs O(log(n+2)^3) work.
There are O(k)=O(n) such boundaries per iterate; their work is absorbed by
O(n^2 log(n+2)^2), since log(n+2)=O(n).
Within a copy, additions/comparisons of wire indices, controller accesses to
constant N bits, gate emission and prescribed gate addressing each cost at
most O(log(n+2)^2) work per gate. Carry circuits and parity templates have a
fixed number of operands. Thus an iterate's full sequential charged work is
O(n^2 log(n+2)^2), not just its quantum gate count. Reverse passes are also
charged. The O(n)-bit iteration counter can be incremented with
O(n log(n+2)) work per iterate, within the same envelope.

Compute r by O(n) steps of binary search with O(n)-bit schoolbook squaring
and bit comparisons: O(n^3 log(n+2)) addressed work and O(n) classical bits.
Uniform allocation/index preparation, initialization, disposal, final output
and k acquisitions (each costing n+1) add polynomial work within
O(2^(n/2)n^2 log(n+2)^2). Indeed n/(2^(n/2)log(n+2)) is bounded for n>=1,
so the stated preprocessing is absorbed without changing the exponential
coefficient 1/2. No arbitrary integer operation is unit cost. Summing all
r<=3*2^(n/2)/4 iterations gives the joint time bound in Section 1. All loop
lengths are deterministic; every wrong-answer branch has the same bounds.
The fixed N=2 branch is absorbed by absolute constants.

The exact acquisition count is Q=k=2(n+16), even on failure. No discarded
or restarted sample is hidden. This proves the sample envelope n jointly
with both spaces, charged work and the fractional guarantee.

## 6. Structured envelopes, growth indices and provenance

For n>=2, log2 B_T=n/2+2 log2 n+2 log2(log2 n), so the rules' double-log
index is exactly 1. For n, n^2 and n the inner logarithms grow as a fixed
positive multiple of log2 n, making the double-log index 0. The max{4,B}
convention and finite extension at n=1 do not affect these limits. Every
positive outer constant has the same index. Thus the exact resource indices
are 1/1,0/1,0/1,0/1. The structured time exponent coefficient is exactly 1/2
on n^1, with outer nPower=2 and logPower=2; this is the full proved asymptotic
envelope. Outer coefficient 1 is only a big-O representative, not a finite
constant. The fraction 1/16 is supported fractional-tolerance-v1 syntax and
has no score.

Material public sources used in constructing this candidate:

* GordoAR, submission 613ca17b-835c-4180-98af-b08f0c06c5bc, immutable commit
  dad28090a6fe6b51e884ce80633e0221a259105d, submission/proof.md, especially
  the saved-witness reflection and telescoping/success argument (lines 42-204).
* kaankolcu, RWT25, submission 3f48c893-2d1b-4e9b-ac9e-e9d318149910,
  immutable commit dd6041a0fc1cfe8c29b2af14c5ffc7b29b18ee75,
  submission/proof.md Sections 1-5 (lines 11-207): threshold projector,
  good-marginal adversarial promise, support argument, reused-witness hybrid,
  small-L cases and streamed reversible arithmetic.

These are declared contribution dependencies. We reproduce all arguments and
assume no prior mathematical acceptance. In particular the moment estimate in
Section 2 establishes the new k=2(n+16), epsilon=1/16 configuration directly;
RWT25 instead uses k=32(n+16), epsilon=1/4. Its error-model text is preserved
for comparable model context, but this candidate gives a smaller fraction.
The logarithmic factors in our time envelope are retained explicitly.

The baseline's exact shift test is also reproduced above. General search and
hybrid background is Grover, quant-ph/9605043v3 Sections 2-3 (condition oracle
available), and Bennett et al., quant-ph/9701001v1 Theorem 3.3 (oracle-query
perturbations). Neither is used as an unproved black-box premise: our oracle
is explicitly implemented and the needed two-dimensional rotation and mixed
state telescoping bound are proved here under the stated hypotheses.

This theorem does not establish cube-root time, optimality, maximal tolerance,
priority, or Pareto dominance over the public sources. Lower finite sample
constants trade against a lower guaranteed malformed fraction. Format checks
and deterministic diagnostics do not certify the mathematics; configured
hosted review is separate from the proof and from advisory critique.
