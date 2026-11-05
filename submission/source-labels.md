# RS14: truncated binary QPE with a globally reusable phase gradient

This is the ACTUAL source-label implementation. It replaces repeated
Hadamard-test source labeling. The rational grid/unwrap decoder remains
active for outer reconstruction and fresh verification, not source labeling.
The exact modular-addition Boolean circuits are in proof.md Section2.
The bounded gradient preparation, exact kickback and single global trace
distance argument directly reuse RR8 phase-labels.md Sections1-3,5, with
full source bytes authenticated at ae634c28a7e4a2683087607a83a432adb370b5d7.
The source translation, grouped truncated Fourier network and explicit
three-product arithmetic are specified in three-product.md. The bounded
gradient preparation and global error proof below remain fully reproduced.
No adaptive multiplication, recursive product-phase Fourier primitive or
arithmetic oracle from RR8 is used. Every actual coherent product/reduction
is the complete Boolean circuit in three-product.md, with counted history.

## 1. Exact source powers and dyadic parameters

Use the fixed acquisition capR from proof.md. Let

 a=clog(2^20 R), t=n+a+4,
 B=min(t,clog(2^30 R(t+1))).                            (1.1)

For positive integeru,clog(u)=ceil(log2u), implemented as bit_length(u-1).
Generate mu=floor(2^W/N),W=(t+1)+n+2 ONCE by ordinary restoring bit
division as in three-product.md. Prepare oneB-bit gradient usingSection3
BEFORE acquiring sources; an exhausted preparation aborts and outputs zero.
No source copy is consumed by preparation.

For each acquired source prepare a fresh/reset t-bit phase register|+>^t.
Apply the ONE exact coherent modular translationF_k(x)=(x+k)modN onvalid
DATAx<N,identity oninvalid encodings, with quantum phase wordk unchanged.
Its explicit three-product Boolean circuit, exact reduction, clean inverse
and full history/wire costs are proved in three-product.md Sections1-3.
This replaces all individual controlled powers. There is no repeated
application2^j times or supplied modular-arithmetic oracle. On the eigenstatechi_y these
operations yield exactly

 2^(-t/2)sum_(k=0)^(2^t-1) exp(2pi i k y/N)|k>,

while DATA remainschi_y and the source's first qubit remainsq_y. This is
only the analysis ensemble decomposition of the actual mixed state; no
purification, hiddeny register, inverse/preparation oracle or source
control is supplied. Apply the truncated inverse transform of Section2,
measure its integerZ, compute the nearest integer toNZ/2^t moduloN with
the explicit three-product multiplication, shifts and exact comparisons (tie down), and
retain the source first qubit. Reset/dispose DATA and phase scratch.
Every acquired label uses the SAME copy, with no additional fresh copy.

## 2. Exact kickback, explicit transform and charged truncation

For analysis only define

 |G_B>=2^(-B/2)sum_z exp(-2pi i z/2^B)|z>.

Translation z->z+d modulo2^B sends it toexp(2pi i d/2^B)|G_B>.
Thus adding or subtracting2^(B-r), conditioned on the AND of two phase
bits, implements their controlled phase exp(plus/minus2pi i bc/2^r)
EXACTLY whenr<=B and returns idealG_B unchanged, also on superpositions
and entangled inputs. A clean AND ancilla plus the controlled ripple
addition requiresO(B) Boolean gates andO(B) reusable scratch, all Clifford+T
via exact NOT,CNOT,Toffoli circuits. Compute the sum into clean scratch,
swap, and subtract from the old register to uncompute, as in proof.md
Section2; low-bit carry is discarded only within the reversible permutation.
There is no quantum-addressed lookup or supplied phase gate.

Here is a complete ordinary forward binary transform network on input
bitsx_0,...,x_(t-1), least significant first. Forj=t-1 down to0 applyH
on bitj; for eachk=j-1 down to0 apply the diagonal controlled phase
exp(2pi i x_k x_j/2^(j-k+1)). Finish by reversing bit order using swaps.
On a basis inputx, after itsH and phases bitj is
(|0>+exp(2pi i(x mod2^(j+1))/2^(j+1))|1>)/sqrt2.
Unprocessed lower bits still equal their input bits, and processed higher
bits are no longer touched. Multiplication of these factors and the final
reversal gives2^(-t/2)sum_z exp(2pi i xz/2^t)|z>, proving the network
implementsF_t by linearity. The inverse reverses every instruction and
negates every phase;H and swaps are their own inverses.

The ACTUAL inverse network omits every controlled phase whose denominator
has r>B. It implements the product of retained phases for each output by ONE
controlled quantum-word gradient subtraction, exactly as proved in
three-product.md Section4. The grouped operation equals the product of
the at mosttB retained phases. There aret Hadamards andO(t) swaps;
all quantum-word ripple operations and AND-word cleanups are counted.
For any omitted gate, its operator norm distance from identity is at most
2pi/2^r<8/2^r. Telescope the unitary product and sum over all omitted
r for each bit: the resulting transform's operator norm distance from
F_t^-1 is at most8t2^-B. IfB=t there are no omitted gates and distance0.
Otherwise2^B>=2^30R(t+1), so the error per extraction is<1/(2^27R).
The trace-distance change on any input, including entangled inputs, is
at most this operator norm bound, by purification and contractivity.
Across at mostR extractions telescope the full adaptive channels, charging
<2^-27 ONCE in total. This comparison is to a mathematical exact-transform
reference algorithm; it does not assert the physical network uses any
omitted gate or arbitrary phase primitive. The actual gradient comparison
is a separate single initial-state comparison, as proved below.

## 3. One bounded actual gradient preparation

An ideal gradient is used only in the analysis. Here is its actual preparation.
Fix the absolute constants K=40, p=60, D=2^p and H_cap=1024. Its tensor factors,
ordered from the most significant bit, have the form

    |q_j> = (|0>+exp(-2*pi*i/2^j)|1>)/sqrt(2), j=1,...,B.

Prepare the first min(B,K) factors as specified below; initialize all later
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
on preparation success, the prepared pure state G_B_actual obeys

    ||G_B_actual-G_B|| < 4K*2^-60+8*2^-K < 2^-36. (3.3)

This also covers B<K by omitting the absent tail. For pure normalized states
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


## 4. Uniform QPE tail, global comparison and conditional ensemble

For the exact-transform reference puttheta=y/N,Hq=2^t. The measurement law is

 Pr[Z]=Hq^-2 |sum_(k=0)^(Hq-1) exp(2pi i k(theta-Z/Hq))|^2.

For circular distanced betweenZ andHq theta,0<d<=Hq/2, the geometric
sum givesPr[Z]<=1/(4d^2), since|sin(pi d/Hq)|>=2d/Hq. At an exact grid
point the measurement is exact. Nearest-integer rounding ofNZ/Hq moduloN
is correct ifd<Hq/(2N). SetD0=Hq/(2N)>=2^(t-n-1)>=2^23R. There are
at most two integers with distance in each[l,l+1); the decreasing-square
integral bound gives failure at most

 (1/2)sum_(l=floor D0)^infinity l^-2
 <=1/(2(floor D0-1))<1/(2^23R).

This holds for every latenty and past transcript. DATA andq_y remain
unchanged conditional ony. A latent-label ideal sieve can be coupled to
the exact-transform reference up to the first wrong label; the conditional
union across at mostR extractions costs<2^-23. Do not condition label
laws on a hidden correctness event or survival of the physical sampler.

First compare the ACTUAL prepared gradient to idealG_B by the SINGLE
initial input trace-distance bound<2^-36, plus preparation-abort<2^-122.
The rest of the adaptive algorithm, including every use, measurement and
output, is one quantum channel, so no multiplication by the number of
uses is permitted or needed. Then compare the ideal-gradient truncated
network to the exact-transform reference, costing<2^-27 by Section2.
Finally couple that reference to the latent-label sieve, costing<2^-23.
Their total is less than1/1024. All actual correlations from gradient
reuse are covered by contractivity; only idealG_B is invariant. Source
first qubits are not measured by extraction. The exact conditional product
laws and17-event sieve are established in the latent-label analysis, then
transferred by these additive bounds. Four other1/1024 budgets remain
shortages, physical rational-sampler cutoff, outer phase reconstruction
and fresh whole-secret verification. Full success remains>=1019/1024.

## 5. Every branch's actual primitive resources

three-product.md gives the complete new gate/bit accounting. The exact
source translation and measured-residue product useO(n^(8/5)) logical
work, and the grouped truncated Fourier networkO(tB)=O(n^(3/2)). All
history wires, clean reversals, generatedmu and fixed gate addresses are
counted. FullO(n) address/generation charges giveO(n^(13/5)) per labeled
acquisition, andR=O(nL) givesO(n^(18/5)L) source work. The new actual
kernel arithmetic has the same aggregate bound. No quadratic per-copy
modular-power or rounding routine remains active. Fixed polynomial
parameter/mu/gradient generation remains counted once before source use.

WithL=O(sqrt n2^(c sqrt n)), the joint time bound isO(n^(41/10)2^(c sqrt n)).
Classical and quantum history scratch isO(n^(8/5)); the full peaks are
O(nL+n^(8/5))=O(nL),O(L+n^(8/5))=O(L), whileQ=O(nL) and the exact
acquisition inequalities remain. Every cap and error comparison above
is unchanged, since the arithmetic and grouped-network identities are exact.
The source-labels file and three-product.md together specify one actual
source circuit; no previous slower implementation is silently counted as
this program. Only the finite exhaustive branch bypasses gradient/QPE.
