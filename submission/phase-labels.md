# RS5: binary phase estimation with one reusable gradient register

This file specifies the exact adaptive source extractor retained by RS5.
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

The exact binary transform F_t is defined by
F_t|x>=2^(-t/2)sum_z exp(2pi i*x*z/2^t)|z>. Its actual recursive circuit,
product-phase construction and inverse are proved in fast-labels.md Section 4.
This replaces the older pivot-by-pivot circuit; no unproved Fourier primitive
is invoked.

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

## 4. The concrete RS5 spectral-label extractor

Put a=clog(2^20 R), t=n+a+4. Prepare one actual t-bit gradient by Section 3,
aborting to zero on a preparation shortage before acquiring copies. Generate reciprocal floor(2^t/N) once, and generate every adaptive
interpolation matrix with all its actual bit costs as specified in
adaptive-arithmetic.md. Count local program/pointer records as well. For each acquired source create a t-bit |+> register,
apply exact coherent modular translation by its integer k using the reciprocal
circuit in fast-labels.md Section 3, then apply the inverse binary Fourier
transform by the recursive product-phase circuit in Section 4 there. This
Fourier circuit is exact for the ideal shared gradient; no phase is truncated.
Measure the phase integer Z and round N*Z/2^t by the exact fast algorithm in
Section 5 there. Retain the first source qubit and reset/dispose data/QPE
scratch. Every new product is the explicitly proved adaptive integer algorithm,
not an oracle. It is cleanly reversible when acting on quantum
registers. The same acquired source copy supplies the whole extraction.

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

For RS5, couple exact ideal-gradient QPE to the latent-label sieve until
an incorrect reported residue, retaining the same q_y and later randomness.
That union is less than 2^-23. The reciprocal circuit and recursive Fourier
identity are exact, so there is no truncation contribution. Compare actual
gradient preparation to that ideal-gradient computation using (3.2)-(3.3):
the single global trace-distance contribution and abort probability are less
than 2^-36+2^-122. Their sum with 2^-23 is below 1/1024. All correlations from
actual reuse are handled by contractivity; only an ideal resource is assumed
unchanged. The new global coin trial budget is separately coupled to ideal
coins with probability less than 1/1024 by fast-labels.md Section 6. Together
with shortage, outer-phase and final-verification budgets, success remains
at least 1019/1024 for every N,s.

## 6. Joint charged resources and provenance

recycle-sieve.md supplies the new quota and all-resource substitution;
fast-labels.md and adaptive-arithmetic.md count every unchanged exact source
operation, generated constant, current pointer/program record and full address.
Source/gradient error stays below1/1024 for the new fixedR; grouped salvage
and the same global4R trial cap retain the other budgets. All bounds and
success1019/1024 remain joint; the n<=16 branch stays exhaustive.

The explicit gradient preparation and global error argument reuse PG2
873cba1f-780f-4fad-bd5b-9cf12b8de874 and PG3
5a99915d-bf94-4f6a-8969-5cc6e601a1a9, with MDC1/VFD3 ancestry in proof.md.
The gradient/addition idea is standard: Nam, Su and Maslov,
arXiv:1803.04933v2 Section II (2019). Its RUS synthesis/norm-equation
algorithm is not assumed. The required preparation, arithmetic and error
proofs are in this snapshot; earlier verdicts are not premises.

PG5 directly reuses PG4 e40f2d5a-68c9-418b-b4e8-64a80305968e's exact
Fourier/reciprocal framework and global sampler cap, replacing its fixed
radix with the fully counted adaptive product. No earlier verdict is a premise.

RS5 directly retains PG5 7e1c8dba-adc8-46db-bf59-1f31688d41c2's
adaptive exact extractor, with only its deterministic R and resource
substitution updated to the new pooled-sum sieve.

RS5 directly reuses SG6 dc8d6d56-9618-46bc-97a3-e9b18ec65099's
primary/triangular rescue component, but changes pairing to whole-bucket
SUM pooling and proves the new conditional populations and quotas in
recycle-sieve.md. This is the single present configuration.

RS5 directly reuses PS7 cda83fcf-1faa-41d5-b858-d5ec44122fe6's
population framework but adds a third SUM pass and globally recycled PRIMARY
rejects. recycle-sieve.md gives the complete changed channel/count/cost proof;
old pass-specific bounds are not assumed unchanged.

## RS5 extension and provenance

This file is adapted from RR8 at ae634c28a7e4a2683087607a83a432adb370b5d7.
The present program adds the fourth SUM channel proved in recycle-sieve.md,
with q=59/10, F=2^62lambda and coefficient 282894777/125000000. The historical
ancestry descriptions above identify inherited material. Any old three-pass
summary is extended by that explicit fourth pass; no predecessor verdict is
used. All five kernels, including the degree-fifteen kernel, have constant
degree and O(n)-bit operands. Their counted adaptive arithmetic fits the
same O(n*2^(20sqrt(log2 n))) logical work per pair with absolute constants.

## RS5 sharper primary-reject coin

RS5 extends RS4 (b16fcbf5-7e11-4148-80f1-cee7ae2df6b5), retaining
its entire four-pass exact stream. In the global primary-V rescue only,
use p=2679/10000, zero coin 2p H^3/J0 and positive coin p H^3/J_delta.
recycle-sieve.md Section 4 proves the stronger exact success p; Section 7
uses DV>=e p PV in the eleven-event proof. Every sample/trial limit remains
unchanged in form, recomputed for q=59/10, r=25607/10000 and F=2^62lambda.
The new resource coefficient is 282894777/125000000. This is a new actual
acceptance instrument and configuration; no old verdict validates it.

## RS5 global V-SUM extension

The current program also retains and globally pairs SUMs from the first
primary-V rescue, as proved in recycle-sieve.md Section 10. Its exact W*W
correlation and positive rational Bernstein certificate establish beta=9/50.
The extra two conditional events give eleven in total. The combined coin
calls for both global V channels remain <=PV, preserving the old literal
4R trial and source limits. No extra source is acquired. All parameters
are recomputed for q=59/10,r=25607/10000 and coefficient282894777/125000000.
The 625-term integer kernel, extra buffers, resets and all full address
charges fit the same ordinary-sieve and space bounds. This is a new
channel, not an assumption of a predecessor's acceptance. RS4V development
submission d034cb7a-4593-4053-a03d-387e4514da0e is materially reused.
