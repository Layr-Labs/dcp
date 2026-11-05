# PG3: binary phase estimation with one reusable gradient register

This file specifies PG3 source-label extraction, building on PG2 and MDC1.
The new coherent/fast implementation is fully detailed in fast-labels.md. All sieve stages, quotas, verification, source acquisition
limits and finite-prefix branch retain their definitions in proof.md. The circuit
below is over Clifford+T and computational measurement. It does not assume an
arbitrary-modulus QFT, arbitrary phase gate, source inverse or additional oracle.

## 1. Exact reversible addition with a quantum addend

The ripple ADD equations in proof.md Section 2 remain Boolean identities when
both addends are quantum registers: the second addend is unchanged, and linearity
extends the basis-state implementation. To implement

    |x>|z> -> |x>|z+x mod 2^t>,

compute the Boolean t-bit sum into a clean target by compute/copy/uncompute,
swap the old and new z registers, then compute the inverse subtraction with the
same unchanged x into the old z register to clear it. Ignore carry out only when
forming the low t-bit result; all intermediate carry wires are uncomputed.
Every Boolean gate has bounded fan-in and is implemented with NOT, CNOT and
Toffoli. There are O(t) gates and O(t) clean temporary wires. Adding an extra
control b to choose between the sum and identity is implemented by Boolean
MUXes before reversal, still O(t) gates and scratch. Signs and fixed binary
shifts of x are wired choices, not quantum memory lookups. The same construction
implements controlled subtraction. It is exact on every encoded basis state.

## 2. The ideal gradient and its exact use

For an integer t>=1 define

    |G_t> = 2^(-t/2) sum_(z=0)^(2^t-1) exp(-2*pi*i*z/2^t)|z>.

The translation z -> z+d mod 2^t sends this state to
exp(2*pi*i*d/2^t)|G_t>, by changing the summation variable. Therefore controlled
addition of x*2^(t-r) into this register, with control b, induces
exp(2*pi*i*b*x/2^r) on the other registers and leaves G_t exactly unchanged.
Here 0<=r<=t; shifts and signs are chosen classically. The identity also holds
when b and x are in arbitrary superposition or entangled with external systems.
Thus an ideal G_t can be used repeatedly without replacement and without
correlating itself with the computation. There is no quantum-addressed access.

For completeness, an exact binary QFT F_t is defined by

    F_t|x> = 2^(-t/2) sum_z exp(2*pi*i*x*z/2^t)|z>.

The following standard circuit identity follows by expanding each output bit
of z in that sum. Process pivots j=t-1,...,0: apply H to bit j, then apply the
phase exp(2*pi*i*b*x_low/2^(j+1)), where b is that pivot and x_low is the integer
encoded by the untouched bits 0,...,j-1. Finally reverse bit order. Expanding
this phase gives, for each k<j, a controlled phase of angle 2*pi/2^(j-k+1).
The output tensor factors on a basis input are the factors with phases
exp(2*pi*i*x/2^(j+1)); their product is exactly the displayed Fourier sum.
Linearity proves the identity on arbitrary inputs. The j=0 phase is empty.

Implement every nonempty pivot phase by the single controlled addition of
x_low*2^(t-j-1) into G_t. Each uses O(t) exact Boolean gates by Section 1.
Reversing this circuit (including negative additions) implements F_t inverse.
The total is O(t^2) Clifford+T gates, including the H and SWAP gates, with O(t)
extra qubits beyond the input and gradient. There is no approximate individual
rotation and no uncharged synthesis of angles. All gates and addresses are
streamed from the stated loops.

## 3. A bounded preparation close to G_t, without supplied advice

An ideal gradient is used only in the analysis. Here is its actual preparation.
Fix the absolute constants K=40, p=60, D=2^p and H_cap=1024. Its tensor factors,
ordered from the most significant bit, have the form

    |q_j> = (|0>+exp(-2*pi*i/2^j)|1>)/sqrt(2), j=1,...,t.

Prepare the first min(t,K) factors as specified below; initialize all later
factors to |+>. Generate the required fixed rational constants once by a
counted finite computation, independently of N,s and outcomes. The rational
Machin formula with 20 alternating arctangent terms and the 60-term sine and
cosine polynomials in proof.md Section 3 give a rational pi midpoint of error
<2^-90 and coordinate errors <2^-88 at all angles -2*pi/2^j, j=1,...,K.
The proof there bounds the larger argument range |angle|<7; here |angle|<=pi.
Round each coordinate times D to a nearest integer, breaking ties toward the
smaller integer; clamp to [-D,D]. Call the resulting signed integers a_j,b_j.
The computed coordinates differ from the true coordinates by <2^-88, rounding
adds at most 2^-61 and clamping cannot increase the error to a true coordinate
in [-1,1]. Hence

    |a_j/D-cos(-2*pi/2^j)| < 2^-60,
    |b_j/D-sin(-2*pi/2^j)| < 2^-60.                 (3.1)

This is an explicit finite rational calculation, not a preloaded advice table.
Its time and storage are absolute constants, although no practicality of those
constants is asserted. No integer has unbounded precision in that calculation.

To prepare one approximate factor for z_j=(a_j+i*b_j)/D, initialize a target B
and selector C to |+>, and a p-bit register R to a uniform superposition by H.
Let the signed weight w(B,C) be D,0,a_j,b_j for (B,C)=(0,0),(0,1),(1,0),(1,1),
respectively. Compute into a flag [R<|w(B,C)|], using reversible comparisons
with width p+1, and uncompute all comparison scratch. Apply S to C and apply
the sign (-1)^[w(B,C)<0] by an exact Boolean phase circuit. The weight choice
and sign are fixed Boolean functions of B,C and the generated constants.
Measure the flag; require one. Apply H to C and all R bits, then measure them;
require all zeros. Any failure resets and discards only this local preparation
attempt. On success the unnormalized target amplitudes are

    (1,z_j)/(2*sqrt(2)).

Indeed projection of C,R onto their initial uniform states adds the signed
counts D and a_j+i*b_j, with denominator 2*sqrt(2)*D. Therefore the success
probability is (1+|z_j|^2)/8>=1/8, and the normalized output is exactly
(|0>+z_j|1>)/sqrt(1+|z_j|^2). This formula also proves the state is independent
of which successful attempt was retained. Previous factors are untouched.
The flag measurement, all zero projections, failures, resets and attempts are
physical counted operations. This is not free postselection.

Permit at most H_cap attempts per factor; on a shortage abort the entire sieve,
output zero and acquire no source copies. All attempts have fixed finite size.
Since (7/8)^8<1/2, the total abort probability is at most

    K*(7/8)^1024 < 64*2^-128 = 2^-122.             (3.2)

For vectors v,w with w nonzero, normalization changes their distance by at most
2||v-w||/||w||, by the triangle inequality and reverse triangle inequality.
Use v=(1,z_j), w=(1,exp(-2*pi*i/2^j)); (3.1) shows each normalized factor's
Euclidean distance is <4*2^-60. Telescoping tensor products bounds the error
of all prepared factors by 4K*2^-60. For j>K the distance from |q_j> to |+> is
at most 2*pi/2^j. Summing gives a truncation error <8*2^-K. Thus, conditional
on preparation success, the prepared pure state G_t_actual obeys

    ||G_t_actual-G_t|| < 4K*2^-60+8*2^-K < 2^-36. (3.3)

This also covers t<K by omitting the absent tail. For pure normalized states
the trace distance is at most their Euclidean distance, as follows from
sqrt(1-|<v,w>|^2)<=sqrt(2-2 Re<v,w>). The rest of the entire adaptive algorithm,
including every reuse, measurement and final output, is one quantum channel.
Trace distance cannot increase under such a channel: for any measured event
its probability difference is bounded by the input trace distance (equivalently
use the variational characterization 0<=E<=I and the channel adjoint).
Consequently (3.3) is charged ONCE to the complete computation, not once per
use. The actual gradient is not assumed to remain uncorrelated or exactly
unchanged. That invariance is used only in the ideal comparison algorithm.
Together (3.2) and (3.3) cost <1/4096 in final success probability.

## 4. The concrete PG3 spectral-label extractor

Use the exact spectral ensemble in proof.md Section 4. Define

    a=clog(2^20 R), t=n+a+4, b=min(t,clog(2^30 R*t)).

Prepare one actual b-bit gradient by Section 3, aborting to zero on a
preparation shortage before acquiring source copies. For each source, create
a t-bit |+> register, implement the one coherent translation
|k>|x> -> |k>|x+k mod N> on valid source data (identity on invalid x), and
apply the truncated inverse binary Fourier circuit with cutoff denominator
2^b. Measure its t-bit integer Z, compute the nearest residue to N*Z/2^t
by the exact fast algorithm in fast-labels.md, and retain the first source
qubit. Release/reset the source data and QPE scratch. The ideal translation
and its restoring-division circuit are proved in fast-labels.md Section A;
the truncated Fourier blocks and global error are proved in Section B;
the exact fast rounding is Section C. These are the actual PG3 operations,
replacing PG2's separate controlled translations and full Fourier circuit.
No source acquisition is repeated by the extraction procedure.

## 5. Uniform ideal-extractor error and the global comparison

First suppose G_t is ideal. Conditional on latent y, the source data remains
chi_y throughout, and its first qubit remains q_y. The exact pre-Fourier phase
register is 2^(-t/2) sum_k exp(2*pi*i*k*y/N)|k>. Write theta=y/N and H=2^t.
The Fourier measurement probability at integer Z is

    P(Z)=H^-2 |sum_(k=0)^(H-1) exp(2*pi*i*k*(theta-Z/H))|^2.

For d the circular distance between Z and H*theta, 0<d<=H/2, the geometric
sum and |sin(pi*d/H)|>=2d/H give P(Z)<=1/(4d^2). At d=0 the exact grid point
has probability one and causes no decoding error. Rounding N*Z/H is correct
whenever dist(Z/H,theta)<1/(2N). Thus failure requires d>=D0=H/(2N).
There are at most two integers with distance in each interval [l,l+1).
For D0>=4, comparison of the decreasing inverse-square sum with its integral
therefore bounds the failure probability by

    (1/2) sum_(l=floor(D0))^infinity 1/l^2
       <= 1/(2*(floor(D0)-1)).

Here D0>=2^(t-n-1)>=2^23 R, so this is <1/(2^23 R). This bound is uniform
in every latent y and every past history. In the ideal-gradient computation
the gradient returns unchanged after every operation, so the usual latent-label
coupling applies across all acquisitions. There are at most R extractions;
the union probability of any incorrect reported label is <2^-23.

For PG3, first couple exact full-Fourier ideal QPE to the latent-label sieve
until a reported label is incorrect, retaining the same q_y and subsequent
randomness. That union costs <2^-23. Next compare all truncated-Fourier
invocations with their exact full-Fourier versions by fast-labels.md Section B;
this costs at most 2^-27 globally. The ideal b-bit gradient returns unchanged
in every retained phase block. Finally compare actual gradient preparation to
that ideal-gradient truncated computation: (3.2)-(3.3) cost <2^-122+2^-36.
The sum of all four terms is less than 1/1024. Contractivity and the fixed R
cap justify these global comparisons even with adaptive later operations.
No actual correlated gradient is treated as a fresh ideal resource. Thus the
same four remaining sieve/verification budgets still give success at least
1019/1024 for every modulus and secret.

## 6. Joint charged resources

fast-labels.md Sections A-D give full implementations and bit/gate accounting.
The restoring division uses O(t*(t-m))=O(n^(3/2)) Boolean gates, the truncated
inverse binary Fourier transform O(t*b)=O(n^(3/2)) gates, and exact residue
rounding O(n^(3/2)) bit operations by the specified five-product recursion.
The full streamed-address charge is O(A_addr^2)=O(n) per logical operation.
Consequently source-label work is O(n^(5/2)) per acquired copy and
O(n^(7/2)L_0) across all R=O(nL_0) acquisitions. The unchanged sieve has the
same work upper bound; all verification and remaining operations fit it.
With L_0=O(sqrt(n)2^((244949/100000)sqrt(n))) the total is

    T=O(n^4 2^((244949/100000)sqrt(n))).

Reversible division needs O(n^(3/2)) temporary qubits and must be included in
peak allocation. Since it is O(L_0), both space envelopes remain unchanged.
Classical fast-arithmetic scratch and controller use polynomial space within
O(nL_0). The full sample count is unchanged: gradient preparation, coherent
translation, Fourier transform and classical rounding acquire no extra DCP
copies. Every bound includes capped preparation failures and all aborts; the
finite n<=16 branch is unchanged and never prepares a gradient.

## 7. Provenance

This construction reuses MDC1's complete sieve and its inherited VFD3-M4
foundations, with attribution in proof.md. The reusable-gradient/addition idea
is standard: Yunseong Nam, Yuan Su and Dmitri Maslov, arXiv:1803.04933v2,
Section II (2019), describes reusable gradient states for Fourier circuits.
That paper motivated checking a gradient implementation here. We do not use
its synthesis, RUS norm-equation algorithm or stated T-count as an oracle.
Sections 1-5 above provide the required adder identity, full binary-QFT circuit,
explicit bounded rational state preparation, and global error argument for
this particular source-only algorithm. PG2 submission
873cba1f-780f-4fad-bd5b-9cf12b8de874 is a direct material dependency for
these gradient preparation and error arguments; MDC1 and VFD3-M4 remain
acknowledged in proof.md. All proof premises needed for this
candidate's review are contained in the snapshot; no external retrieval is
required and no prior verdict is a premise.
