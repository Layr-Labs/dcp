# RLQGR3: robust measured records with adaptive exact arithmetic

## Configuration, scope and provenance

For every N>=2 and s in Z/NZ set n=ceil(log2 N), D=2^n,
m=2048(n+10), J=n+4, H=n+ceil(log2(m(J+1)+2))+20, M=2^24 H.
Acquire exactly Q=m copies on every branch. The algorithm below has
unconditional full-secret success >2/3 jointly with branchwise bounds

 T=O(2^(n/2+64sqrt(log2 n)) n^2(log2 n)^2),
 S_C=O(n^2) bits, S_Q=O(n) qubits, Q=m=O(n).

The time envelope applies for n>=2; the n=1 case has absolute cost.
The indices are1,0,0,0 and the count tolerance is floor(Q/10) under the
explicit model below. Direct source: RLQGR2 submission
8657ff0f-f4d3-4605-a583-a6d57d3205f4, for the measured-record algorithm,
robustness proof, Grover configuration, clean normalization and reciprocal
reduction. Its RLQGR1/GRST1/RST1 ancestry remains acknowledged. The new
fast-arithmetic.md supplies adaptive exact Toom interpolation over a composite
ring. It extends Gidney1904.07356v1 Section2Eq1 output preconditioning, with
all implementation and bounds reproduced. Standard context includes
Kitaev quant-ph/9511026v1 eigenvalue measurement, Ettinger/Hoyer
quant-ph/9807029 dihedral sampling, and Grover quant-ph/9605043v3 search.
No external result, prior verdict or diagnostic is an inaccessible subroutine.

## Full corruption model

Before private randomness, an adversary chooses at most floor(Q/10) acquisition
positions and an arbitrary joint state on those declared n+1-qubit registers.
It may know N,s and the algorithm; malformed copies may be mutually entangled.
Every other copy is an independent ideal rho_s for the same s, and their
product is independent of the malformed subsystem. The adversary cannot
alter registers/controller after delivery or choose positions adaptively from
private outcomes. The algorithm is not told the positions. Clean input is
the empty set. This is precisely the fifth structured error_model and is
byte-identical to RLQGR2. No per-copy error probability or impossibility of
larger tolerance is asserted. All operations below are defined for arbitrary
malformed registers, including invalid encoded data labels.

## Exact phase labels from the source

Let chi_k=N^(-1/2)sum_y exp(2pi i k y/N)|y>, and
phi_(k,s)=(|0>+exp(-2pi i k s/N)|1>)/sqrt2.
Expanding rho_s and summing over x cancels unequal Fourier labels, giving
rho_s=(1/N)sum_k |phi_(k,s)><phi_(k,s)| tensor |chi_k><chi_k|.
These Fourier vectors are notation, not a circuit oracle. Translation
T_a|y>=|y+a modN> has eigenvalue exp(-2pi i k a/N) on chi_k.
Extend it by identity on y>=N. An extra |+> ancilla controlling T_(-2^j)
then measured in X or Y has mean cos(2pi*2^j*k/N) or sin thereof.
X measurement is H then Z; Y is S^dagger,H,Z. Given latent k these
measurements leave chi_k and the source control unchanged, so repetitions
are independent. They require only exact Clifford+T modular permutations.

For each acquired copy and each j=0,...,J, take M measurements in EACH
basis using reset ancillas. Let x_j,y_j be their signed empirical means.
Generate rational 64-direction cos/sin tables C_r,S_r as specified below.
Choose the least r maximizing x_j C_r+y_j S_r. This estimates the circle
phase2^j*k/N with error<1/16 whenever both means have error<=delta=1/1024.
Indeed the computed dot product differs from exact cos(angle difference)
by at most2eta+2delta<1/256, eta=2^(-16). The nearest grid direction has
dot>=1-(pi/64)^2/2>=511/512 using pi<4. Any direction at circular distance
>=1/16 has dot<=cos(pi/8)<=31/32, since
1-cos(pi/8)=2sin^2(pi/16)>=1/32 by sin u>=2u/pi on[0,pi/2].
The gap15/512 exceeds twice1/256, proving the decoder property.

For completeness, independent X_i in[-1,1] satisfy
Pr(|mean-Emean|>d)<=2exp(-a d^2/2) for a observations. The centered log
MGF has second derivative a tilted variance<=1, and value/derivative zero
at zero; integrate twice and optimize the exponential Markov inequality.
Here M delta^2/2=8H. Union over2m(J+1) means gives
4m(J+1)exp(-8H)<1/1024, uniformly in the honest latent labels. In fact
exp(-8H)<2^(-8H) and H>=ceil(log2(m(J+1)+2))+20.
Apply this only to honest positions; malformed ones have no accuracy promise.

Unwrap the decoded phases: start g_J=r_J/64, then for j=J-1 down to0 choose
the closer to r_j/64 of the two circular lifts(g_(j+1)+b)/2, b=0 or1;
ties use b=0. If the next error is e<1/16, the good lift is within e/2 of
the true preceding phase and within1/16+e/2<3/32 of the decoded direction.
The other is more than13/32 away. Thus each step halves the error and
final error is <(1/16)2^(-J)<=2^(-n-8)<1/(2N).
Round N*g_0 to nearest integer modulo N, ties downward, obtaining k.
The numerator/denominator have O(n) bits. This handles all k and wraparound.
The procedure always returns a label in[0,N), even on malformed inputs.
No label failure is detected, retried or postselected.

## Counted finite tables

Generate cos/sin entries for grids64 and1024 as signed integers divided by
E=2^20. Each has error<eta=2^(-16). One explicit finite rational generator
uses pi=16arctan(1/5)-4arctan(1/239), the first64 alternating terms of each,
then the first256 sine/cosine Taylor terms at the corresponding rational
angle2pi*r/L. Arctangent error<=16/(129*5^129)+4/(129*239^129)<2^(-100).
Angles have magnitude<8. The remainders8^512/512! and8^513/513! are each
<2^(-40); a bound2^(-30) covers angle and truncation error. Rounding to
nearest E^(-1), ties downward, adds<=2^(-21). Clamp entries to[-E,E], which
cannot increase error. The Machin identity follows from tangent addition,
with4arctan(1/5)-arctan(1/239) in(0,pi/2) and tangent1.
All these are fixed finite computations, with all arithmetic/generation,
storage and access counted as absolute constants. They are not instance
advice, arbitrary-precision real arithmetic or quantum rotation synthesis.

## Records, score predicate and robust separation

After extracting a label, choose a fresh fair basis bit B. Measure the SOURCE
control in X if B=0 or Y if B=1; store the X sign or NEGATED Y sign a,
respectively. The means are cos(2pi ks/N) and sin(2pi ks/N). Store(label,B,a),
release/reset that copy and its scratch, then acquire the next. Thus only one
source copy coexists during extraction. Exactly m copies are acquired.

First analyze an IID ideal record sequence with true labels. For t<N define
X_i(t)=a_i cos(2pi k_i t/N) at B_i=0, or a_i sin(...) at B_i=1.
Its mean is(1/(2N))sum_k cos(2pi k(s-t)/N), which equals1/2 at t=s and0
otherwise by the geometric-series identity. It is in[-1,1]. The proved
concentration inequality with deviation1/32, union over every valid t, gives
failure<=2N exp(-m/2048)<=2^(n+1)exp(-(n+10))<1/1024.
For n>=1 this is at most4exp(-11)<4(2/5)^11<1/1024, using e>5/2.

The actual score computes z=label*t mod N, q=floor(1024z/N) and uses the
signed 1024-grid entry C_q/E or S_q/E. Angle error<2pi/1024<1/128 and
1-Lipschitz sine/cosine plus eta give term error<1/100. Entries are in[-1,1].
Let S be the sum of the signed integer table entries. Define h(t) as
[t<N AND S>=mE/4]. The threshold is an integer.

For the full corruption model, at each malformed position analytically
substitute an independent synthetic ideal record. At honest positions use
their latent true labels and source-control outcomes. Because positions are
fixed and honest copies are a product independent of the malformed subsystem,
this reference sequence is IID with exactly the preceding distribution.
This does NOT condition on correct label extraction or assume independence
of malformed outcomes. On correct honest extractions, actual and reference
records agree at every honest position. At each malformed position arbitrary
actual and reference rational score terms differ by at most2, deterministically
for every t. Consequently actual average score differs from the reference
trigonometric average by at most1/100+2|C|/m<=1/100+1/5.
On concentration and honest-label success the true average is at least
1/2-1/32-1/100-1/5=207/800>1/4; false averages are at most
1/32+1/100+1/5=193/800<1/4. This holds uniformly for every allowed malformed
joint state. Such a state produces arbitrary correlated classical records,
already covered by this deterministic inequality. No union over corrupt
values is needed. Label and concentration errors total<1/512, so h has
unique marked secret with probability>1-1/512. The actual count Q=m,
not its upper envelope, appears in floor(Q/10).

## Exact search and unconditional success

For n>=2 prepare n Hadamards, uniform on D labels, use exactly
j=isqrt(9D) div4 query/diffusion iterations and measure the candidate.
Output the measured value if<N and zero otherwise. There are no new copies,
restarts or postselection. At n=1 evaluate h(0),h(1) classically, return the
unique pass if any and zero otherwise; this fixed branch succeeds on the
same good-record event.
On that event the implemented predicate is an EXACT unique-marked oracle.
Write theta=arcsin(1/sqrt D), |b> uniform on labels except s. The initial
candidate is sin(theta)|s>+cos(theta)|b>. Query diag(-1,1) and diffusion
2|u><u|-I give marked probability sin^2((2j+1)theta) by2-by-2 multiplication.
For D>=4, theta>=1/sqrt D and arcsin(x)/x<=pi/3 for x<=1/2 (it is the
average of an increasing integrand). Therefore the angle is in[1,2pi/3]:
use j between3sqrt D/4-1 and3sqrt D/4. Sine squared attains its minimum
at an endpoint there, and sin1>=1-1/6=5/6, while sin^2(2pi/3)=3/4.
Thus marked success>=25/36, and unconditional success>=25/36-1/512>2/3.
The circuit uses only the exact integer iteration count, not theta or pi.

## Reversible score implementation and quantum space

Read the m classical records in a FIXED sequential loop; no quantum-addressed
memory is assumed. Compute S in a signed register of
ceil(log2(2mE+1))+2 bits, enough for every possible malformed sum. After
comparison/validity phase marking, reverse the whole score computation.
For each record compute label*t mod N by fast-arithmetic.md, add its score
term, then clear its product/lookup scratch. This clean exact modular product
preserves t and uses O(n) qubits and charged work
O(n 2^(64sqrt(log2 n))(log2 n)^2). It includes its generated constants,
coefficient arithmetic, complete inverse work and whole-memory addressing.
It covers every encoded t<2^n and has a fixed finite small-size branch.

Compute q by TEN binary fractional-division stages on z: double a remainder,
compare with N, record quotient bit, conditionally subtract N. Retaining all
these constant-many O(n)-gate histories uses O(n) qubits. Copy q to ten clean
bits and reverse; repeat this compute-XOR to clear it later. For each possible
q, an equality-controlled XOR selects the fixed integer table value, using a
finite counted network, not a lookup oracle. Add/subtract into S, then reverse
lookup, q and modular product. Threshold and t<N comparisons are ordinary
clean ripple circuits. Reversing the record loop clears S after marking.

Complete-domain modular addition/subtraction has O(n) Boolean gates/wires:
compare with N, carry/borrow scan, select the modular result for valid data,
identity otherwise. Retain gate values, XOR output, reverse for clean
evaluation; apply a permutation in place by compute-swap-inverse. NOT/CNOT/
Toffoli implement fixed-arity gates with exact constant-size Clifford+T.
These implement extraction translations and ordinary comparisons/diffusion.
Diffusion is n Hadamards, a multi-controlled phase on all-zero, n Hadamards,
up to a harmless common global sign. It costs O(n) gates/clean scratch.

The search has candidate n bits, one O(n) modular scratch system (whose full
linear bound is proved in the addendum), constant-depth division history,
fixed table buffers and O(log n) sum. Extraction needs one n+1 copy, one
ancilla and O(n) scratch. These stages reuse space. Thus S_Q=O(n).
Records occupy O(mn)=O(n^2) bits. Generated arithmetic tables/stack have the
addendum's bounded storage and fit this classical envelope, as do N,
reciprocal, fixed tables, input/output, every counter and intermediate integer.
No amplitude array or full circuit description is allocated.

## Charged uniform work and declarations

All ordinary ripple circuits stream fixed bit-scan templates, with reverse
order for inverse gates. Source/record bases advance by addition. Total
allocation O(n^2) bits/qubits is established first, so every address costs
O(log(n+2)). Fixed index arithmetic and its own addressed accesses allow
O(log^2(n+2)) per ordinary logical gate. Adaptive arithmetic instead allows
O(log^4(n+2)) fully addressed controller work per logical gate and explicitly
absorbs the excess into its proven64sqrt(log2 n) term. Tables are generated
and classically read by counted bits; no index product, arithmetic word,
stack update or gate emission is free. See the addendum for the detailed
uniform recurrence, linear scratch bound, finite branch and reciprocal proof.

Across m=O(n) records, charged reflection work is
O(n^2 2^(64sqrt(log2 n))(log2 n)^2), including all reverse circuits.
Grover uses at most3*2^(n/2)/4 reflections. Long O(n)-bit iteration-counter
work per reflection is smaller. Arithmetic setup is explicitly counted in
the addendum and reused, rather than imported as advice.
Statistical preprocessing uses2m(J+1)M=O(n^3) translations, O(n) gates each;
addressing, counters, empirical means, fixed-grid decoding, rational lifting
and rounding, residue constants and recording fit a conservative O(n^5)
charged bound. All variable integers have O(n) bits and schoolbook bit cost
is included. Exact square root and parameter generation also fit polynomial
work. Fixed rational-table generation is a finite outside constant. Source
acquisition costs m(n+1)=O(n^2). These polynomial costs are absorbed by the
claimed exponential envelope for n>=2, and the n=1 branch is fixed finite.
Every loop and allocation has a deterministic ceiling on arbitrary malformed
inputs; there is no expected-time assumption, hidden restart or omitted failure.

The four supported envelopes are2^(n/2+64sqrt(log2 n))n^2(log2 n)^2,
n^2,n,n. Their indices are1,0,0,0, since time log is n/2+O(log n) and the
other bounds are polynomial. The coefficient64 is explicit and proved,
not an unknown inside-exponent constant. Relative to RLQGR2 time ratio is
n^(-3/5)2^(64sqrt(log2 n))->0, with all other envelopes/model unchanged.
This is an actual adaptive arithmetic change, not a tighter rational label
on a fixed routine. No O(2^(n/2)n^2 polylog n), practical crossover, optimality,
new fastest-known DCP result or cube-root goal is claimed. Different rows,
including stronger-tolerance RGRST1 with more qubits, remain tradeoffs.
