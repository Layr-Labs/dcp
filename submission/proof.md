# RLQGR2: classical phase records and linear-quantum-space search

## Complete theorem and provenance

For every integer N>=2, s in Z/NZ, n=ceil(log2 N), set
D=2^n, m=2048(n+10), J=n+4,
H=n+ceil(log2(m(J+1)+2))+20 and M=2^24 H.
The one algorithm below acquires EXACTLY Q=m source copies,
recovers the entire s with unconditional probability >2/3, and on every branch
has jointly

 T=O(2^(n/2) n^(13/5) (log2 n)^2), S_C=O(n^2) bits, S_Q=O(n) qubits, Q=O(n).

The time envelope is for n>=2 with absolute finite cost at n=1. The four exact
growth indices are [1,0,0,0]. The fifth unscored tolerance law is floor(Q/10) under the explicit fixed-
position corruption model below. This includes clean ideal input.
All constants are absolute.

RLQGR2 directly reuses RLQGR1 submission
641e8707-91e2-4257-a82d-d1f7bde2349e for the entire measured-record
algorithm, label extraction, robust score proof, exact Grover schedule and
streamed addressing. RLQGR1's GRST1/RST1 ancestry remains acknowledged.
This candidate replaces schoolbook modular products in the score oracle
with the explicit clean linear-space fast arithmetic of fast-arithmetic.md.
That construction adapts Gidney, Asymptotically Efficient Quantum Karatsuba
Multiplication, arXiv:1904.07356v1, Section 2 Eq.(1) and Section 3.
The padded-word shears and output accumulation are materially from that
published method; the proof and audit here implement the needed integer
identities explicitly. No author code or prose is copied. The fixed-schoolbook
base, normalization accounting, reciprocal reduction and rational exponent
upper envelope are stated in the addendum. No paper result is a black-box
subroutine without implementation and cost accounting here.

The measured-record framework already replaced GRST1's quantum block and hybrid by individual label extraction, immediate X/Y measurement and a
classical score predicate implemented exactly and reversibly.
Standard context: Kitaev, Quantum measurements and the Abelian Stabilizer
Problem, quant-ph/9511026v1, eigenvalue measurement construction; Ettinger
and Hoyer, On Quantum Algorithms for Noncommutative Hidden Subgroups,
quant-ph/9807029, dihedral sampling result; Grover, A fast quantum mechanical
algorithm for database search, quant-ph/9605043v3, algorithm/amplitude analysis.
No external theorem, accepted verdict or numerical test is a proof premise:
every required identity, probability estimate and circuit cost is given here.
This is a source-only resource tradeoff, not a novelty claim over established
polynomial-sample dihedral algorithms or a subexponential-time breakthrough.

## Exact spectral ensemble and counted measurements

Let |chi_k>=N^(-1/2) sum_(y=0)^(N-1) exp(2pi i k y/N)|y>, and
|phi_(k,s)>=(|0>+exp(-2pi i k s/N)|1>)/sqrt(2).
Expanding the two data registers of rho_s and summing over x cancels
all unequal Fourier labels, giving the EXACT mixed-state identity

 rho_s=(1/N) sum_(k=0)^(N-1) |phi_(k,s)><phi_(k,s)| tensor |chi_k><chi_k|.

The Fourier vectors are analytic notation; no Fourier circuit is invoked.
For each fresh copy the latent k is uniform and independent of other copies.
Translation T_a:|y> -> |y+a mod N> has eigenvalue exp(-2pi i k a/N)
on |chi_k>. Its complete-domain identity extension on invalid y>=N is unitary.
Prepare an extra ancilla |+>, apply controlled T_(-2^j mod N) to the data,
and measure that ancilla in X or Y. Its mean is respectively
cos(2pi*2^j*k/N) or sin(2pi*2^j*k/N). X measurement is H then Z;
Y measurement is S^dagger then H then Z. All gates are exact Clifford+T.
The eigenstate data register is unchanged conditional on either result, and
the source control is untouched. Thus repetitions are independent given k.
Only counted modular translations, one ancilla and measurements are needed.

For every j=0,...,J take M independent measurements in EACH basis, with
fresh reset ancillas. Let the empirical means be x_j,y_j. Use the finite
64-direction decoder below to produce r_j/64 estimating the circle phase
2^j*k/N mod1 to circular error <1/16. Then apply the explicit unwrapping
routine below and round N times the resulting rational to the nearest
integer modulo N (ties downward). Call the result the extracted label.
Its error probability over ALL m copies is <1/1024, proved below.
A failed extraction need not be detectable; its outcomes are included in the
analysis, not discarded and not retried.

## Finite constants, without real-arithmetic or synthesis oracles

Generate once two rational direction tables for 64 and 1024 equally spaced
angles, with signed integer cos/sin entries divided by E=2^20. Each entry
approximates the exact sine/cosine to error eta=2^(-16).
This is a counted fixed finite classical computation, not preloaded advice.
One explicit generator uses
pi=16 arctan(1/5)-4 arctan(1/239).
Sum the first 64 terms of each alternating arctangent series. The error is
at most 16/(129*5^129)+4/(129*239^129)<2^(-100).
Use the resulting rational pi approximation in the rational angle 2pi*r/L,
L=64 or1024, and sum the first 256 sine/cosine Taylor terms; round to
nearest integer multiples of E^(-1), ties downward.
The angles have magnitude <8, and Taylor remainders are bounded by
8^512/512! and 8^513/513!, each <2^(-40), with a larger harmless bound
2^(-30) covering both angle and truncation errors. These integer inequalities
can be checked directly or by grouping factorial factors. The final rounding
adds at most 2^(-21), so the total is <2^(-16). Clamp each rounded integer
to [-E,E]; this cannot increase error relative to a sine/cosine in [-1,1]
and ensures every actual score term is in [-1,1], including on corrupt data.
The Machin identity follows from the tangent addition formula: tan(4 arctan
(1/5)-arctan(1/239))=1, with that angle in (0,pi/2).
The alternating-series error and ordinary Taylor remainder bounds are valid
on these fixed intervals. All terms, factorials and rational operations
have fixed finite bit sizes, independent of N; their entire generation,
storage and access cost is charged as an absolute constant. Only the rounded
tables are needed during the variable-size algorithm.

## Decoder and uniform extraction error

The 64-direction decoder maximizes x_j C_r+y_j S_r over r=0,...,63,
where C_r,S_r are the generated rationals; ties use the least r.
Let delta=1/1024. Suppose both empirical means differ from their exact means
by at most delta. For a direction psi=2pi r/64 the discrepancy between its
computed dot product and cos(2pi*phase-psi) is at most
2eta+2delta<1/256, since empirical means lie in [-1,1].
A nearest grid direction is within pi/64 and has ideal dot product at least
1-(pi/64)^2/2>=511/512, using pi<4.
Any direction of circular phase distance >=1/16 has angular distance >=pi/8
and dot product <=cos(pi/8)<=31/32: use
1-cos(pi/8)=2 sin^2(pi/16)>=1/32, from concavity
sin(u)>=2u/pi on [0,pi/2]. The ideal margin is at least15/512,
which exceeds twice the possible computed error. Thus every maximizing
direction has circular phase error <1/16.

A bounded variable X in [-1,1] has
E exp(lambda(X-E X))<=exp(lambda^2/2). To verify this, the second derivative
of the centered log moment-generating function is the variance under an
exponential tilt, at most one because the tilted variable remains in [-1,1].
The value and first derivative at zero vanish, so integrating twice gives
the inequality. Chernoff optimization gives, for M independent observations,
Pr(|mean-E X|>delta)<=2 exp(-M delta^2/2).
Here M delta^2/2=8H. Union over 2m(J+1) empirical means is at most
4m(J+1) exp(-8H)<1/1024. Indeed exp(-8H)<2^(-8H),
H>=ceil(log2(m(J+1)+2))+20, so the bound is much smaller than
4*2^(-160). Conditional on any latent k the same estimate holds;
therefore it holds unconditionally and uniformly in s.

For unwrapping, set g_J=r_J/64. For j=J-1 down to0 choose the closer,
in circular distance to r_j/64, of the two lifts
(g_(j+1)+b)/2, b in{0,1}; ties use b=0.
If g_(j+1) has circular error e<1/16 relative to 2^(j+1)k/N,
one lift lies within e/2 of the true previous phase and the other is a
half-circle away. The good lift is within 1/16+e/2<3/32 of r_j/64;
the wrong lift is farther than 13/32. Hence the choice is correct and its
error is at most e/2. Induction gives final circular error
<(1/16)2^(-J)<=2^(-n-8)<1/(2N).
The final rational has O(n) bits, and rounding N*g_0 modulo N therefore
recovers k exactly. This proof covers wraparound, arbitrary N and all k,
not just powers of two or typical labels. No unknown phase is computed
by an uncharged operation; decoder and lifting use rational arithmetic.

## Classical records with uniform separation of the full secret

After extracting a label, choose a fresh fair basis bit B and measure the
SOURCE control qubit in X when B=0 or Y when B=1. Let the stored sign a
be the X outcome when B=0 and the NEGATIVE of the Y outcome when B=1.
For the analytic source phase -2pi k s/N, the respective conditional means
are cos(2pi k s/N) and sin(2pi k s/N). Store (label,B,a), discard/reset
all quantum registers of that copy, and only then acquire the next copy.
Thus no two source copies need coexist. Exactly m copies are acquired,
including every erroneous extraction or unhelpful record.

For analysis first use the true latent label k_i, even on extraction-error
outcomes, to define the ideal record. Eigenstate tests act trivially on the
source control conditional on k_i; consequently the ideal records are
independent with k_i uniform, B_i fair, and the conditional sign means above.
For a candidate t<N define independent bounded variables

 X_i(t)=a_i cos(2pi k_i t/N) if B_i=0,
 X_i(t)=a_i sin(2pi k_i t/N) if B_i=1.

Their common mean is
(1/(2N)) sum_k [cos(2pi ks/N)cos(2pi kt/N)
                   +sin(2pi ks/N)sin(2pi kt/N)]
=(1/(2N))sum_k cos(2pi k(s-t)/N),
which equals1/2 at t=s and0 otherwise by the finite geometric-series identity.
Applying the proved concentration inequality with deviation1/32 and union
over every t<N gives failure at most
2N exp(-m/2048)<=2^(n+1)exp(-(n+10))<1/1024.
For n>=1 this is at most4 exp(-11)<4(2/5)^11<1/1024, using e>5/2.
No conditioning on successful label extraction is used to assert independent
records: on the event that every extraction is correct, the actual records
coincide with these ideal ones. Union the extraction-error and concentration
failure events additively. With probability >1-1/512, both hold.

The actual score replaces the sine/cosine by a fixed rational table entry.
Compute z=label*t mod N exactly, q=floor(1024 z/N), and take the appropriate
1024-grid entry at q, multiplied by a. Circular angular discrepancy is
<2pi/1024<1/128. Sine and cosine are 1-Lipschitz in radians, so adding table
error eta yields a term error <1/128+2^(-16)<1/100.
Therefore on the joint good-record event, the mean rational score is
at least1/2-1/32-1/100>1/4 at s, and at most1/32+1/100<1/4
at every other valid t. This proves UNIQUE separation for the entire secret,
not merely a parity or an average-case advantage.

The robust extension below proves that this separation persists under the
claimed number of malformed copies. Define the exact classical predicate h(t): t<N AND the sum of the integer
signed table entries is at least mE/4. Here mE/4 is an integer.
All computations of h use only stored records and exact integer arithmetic.
On the joint event, h(t)=1 precisely at t=s among D candidate labels.
On bad data h may be arbitrary; the algorithm and all bounds still apply.

## Explicit adversarial count model and robust score separation

Let Q=m be the actual acquired-copy count and tau=floor(Q/10). Before the
algorithm's private randomness is drawn, an adversary may select a set C of
at most tau acquisition positions and any joint density operator on those
source registers. It may know N,s and the complete algorithm. The remaining
positions contain a product of independent ideal rho_s copies for the same
fixed s, tensor-independent of the malformed subsystem. Malformed copies may
be entangled or classically correlated with EACH OTHER. The adversary cannot
alter the controller or registers after delivery, select positions based on
the algorithm's private outcomes, or correlate the ideal copies with its
malformed subsystem. These promises define the error model, not additional
algorithmic resources. The algorithm is not told C or which copies are faulty.
All source registers have the declared n+1 qubits; corrupt data labels may
be invalid encoded y>=N. Translations have the full-domain unitary extension,
so every step and allocation remains well-defined for such inputs.

For analysis, place at every malformed position a synthetic independent ideal
record drawn exactly as in the clean construction, independently of all honest
copies and of the adversary. At honest positions use the latent label and
source-control record already defined. The resulting ideal reference record
sequence is IID with precisely the mean and concentration above. This uses
fixed positions and the product independence promise; it does NOT condition
honest records on favorable extraction or on adversarial observations.
The union bound for extraction errors is applied only to honest positions,
no more than m copies, so remains <1/1024. On all correct honest extractions,
the actual and ideal reference records agree at every honest position.

At a malformed position no extraction correctness, independence or output
bias is assumed. The procedure always returns a label modulo N, B in{0,1}
and a sign in{-1,1}; each fixed-table score term is bounded in [-1,1].
Its difference from the corresponding ideal reference RATIONAL score term
is therefore at most2 on every branch and for every candidate t, even if
malformed outputs are correlated with each other or with earlier observations.
The synthetic ideal rational term differs from its ideal trigonometric term
by <1/100. For every candidate, the actual average score thus differs from
the reference trigonometric average by at most

 1/100 + 2|C|/m <=1/100+1/5.

On the reference concentration event, the true candidate's actual average is
at least1/2-1/32-1/100-1/5=207/800>1/4, and a false candidate's is
at most1/32+1/100+1/5=193/800<1/4.
These are exact rational comparisons. Hence h has unique marked candidate s
under EVERY allowed adversarial joint state on at most floor(Q/10) positions,
except for a total probability <1/512 from honest-label extraction and IID
reference concentration. No union over possible corruptions is needed:
the bounded-score perturbation inequality is deterministic and uniform in
their actual values. An arbitrary joint malformed state yields arbitrary
classical outputs through the bounded finite protocol, already covered.
Honest copies are independent of the malformed subsystem, so measurements
on that subsystem cannot disturb or bias their ideal product law.

This establishes the good-record event and the subsequent search guarantee
under the stated full corruption model, not only on clean input. Every loop,
acquisition and memory ceiling is unchanged on arbitrary malformed registers.
The exact count Q=m, rather than its O(n) upper envelope, is used in the law.
No conversion from a per-copy corruption probability or a maximum-tolerance
impossibility claim is made. Clean source input is the special case C empty.

## Search, finite branch and unconditional correctness

For n>=2 prepare the n-qubit uniform candidate state on D labels. Implement
the exact reflection |t> -> (-1)^(h(t)) |t> with the reversible classical
score computation below. Repeat it followed by diffusion 2|u><u|-I exactly
j=isqrt(9D) div4 times. Measure t and output it if valid, otherwise zero.
For n=1 evaluate h(0),h(1) classically, return the unique passing candidate
if one exists, and otherwise return zero. This finite branch has constant
resources and succeeds on the same joint good-record event.
There are no retries, postselection, verification copies or additional sources.

For clarity, the exact Grover bound is reproduced. On the good-record event,
let theta=arcsin(1/sqrt D) and |b> be uniform on labels other than s.
The initial state is sin(theta)|s>+cos(theta)|b>. In this basis the query
is diag(-1,1) and diffusion is2|u><u|-I. Matrix multiplication yields marked
probability sin^2((2j+1)theta). Since D>=4,

 1 <=(3sqrt D/2-1)/sqrt D <=(2j+1)theta
 <=(3sqrt D/2+1)*(pi/3)/sqrt D <=2pi/3.

Use theta>=1/sqrt D and the monotonicity of arcsin(x)/x on(0,1/2],
which follows from averaging its increasing derivative integrand.
The minimum of sin^2 on[1,2pi/3] is at an endpoint. The sine series gives
sin1>=5/6, and the other endpoint has square3/4, so success>=25/36.
The same global sign for diffusion implementation and its reference is harmless.
No physical circuit uses theta, pi, arcsines or approximate gates.
Unconditional success is at least25/36-1/512>2/3 for n>=2;
for n=1 it is at least1-1/512>2/3. All bad-data branches are included.

## Linear-qubit reversible predicate with no QRAM

The m records occupy O(mn)=O(n^2) classical bits. They are read by the
classical controller in a FIXED sequential loop, never quantum-addressed.
A single reflection computes the sum, copies its comparison with mE/4 to
a phase flag (also requiring t<N), applies Z and reverses the entire sum.
The candidate t stays as n quantum bits. The signed accumulator uses
ceil(log2(2mE+1))+2=O(log(n+2)) qubits with enough headroom that no sum
on any branch overflows, even when every record/sign is erroneous.

For each record compute z=label*t mod N using the exact clean fast
compute-XOR circuit proved in fast-arithmetic.md. It uses a constant number
of products on O(n)-bit operands and one exact reciprocal correction.
The reciprocal floor(2^(2n+1)/N) is generated once by charged schoolbook
integer division. Each product uses the explicit padded-word recursive
accumulator and clean normalization of the addendum. Logical work per record
is O(n^(8/5)), quantum scratch O(n), and the input t and classical label are
preserved. The claim applies to every candidate t<2^n, including invalid
candidates; labels are always reduced modulo N by extraction. Reverse the
clean modular-product circuit to clear z after its score term is used.
There is no loop of n full-width modular additions per score product and
no stored quantum computation history of superlinear length.

Compute q=floor(1024 z/N) by ten binary fractional-division stages: start
remainder z, double, compare with N, record the next quotient bit and
conditionally subtract N. Since every stage has O(n)-bit operands and there
are exactly ten, even retaining all intermediate Boolean histories and
then reversing them uses O(n) gates and qubits. Copy q to a clean 10-bit
register, reverse the division histories, and later uncompute q by repeating
that same compute-XOR map. All work is exact.

For each possible 10-bit q, an equality-controlled XOR selects the appropriate
fixed-table integer into a clean signed constant-size register. A linear
AND with fixed ten controls, XOR into each output bit and uncompute implements
this at O(1) gates/scratch in the asymptotic n model; the full finite table
and its generation are counted, with no random-access oracle. Add or subtract
the selected integer into the sum according to the classical basis/sign
record, then reverse table lookup, quotient and modular product. Every term's
scratch is zero before the next record. The sum remains and is later
uncomputed by traversing records backward, reading their classical label constants again.
The threshold and t<N comparisons use ripple circuits and O(n) scratch.

All active quantum registers together occupy O(n) qubits: candidate, one
modular-product accumulator, temporary permutation register, ripple scratch,
constant-depth division bands, fixed-size table buffers, phase flag and
O(log n) sum. The source phase-extraction stage likewise has just one
(n+1)-qubit source copy, one ancilla and O(n) scratch. Quantum memory is
REUSED between these two stages. There is no retained quantum source block,
coherent source control or hidden subset-sum/likelihood oracle.

## Complete uniform and branchwise charged resource proof

Source extraction, score lookup, comparison and diffusion use the same
regular bit-scan templates as RLQGR1. Fast multiplication uses a depth-first
classical recursion stack of O(log(n+2)) frames with O(log(n+2))-bit indices,
thus O(log^2(n+2)) classical bits. Its word-band bases advance by additions;
no per-gate index product is needed. Each word ripple circuit is emitted
as a regular scan and reversed directly when required. The addendum counts
all base-case schoolbook Boolean steps and their clean uncomputation.
The complete allocated memory is O(n^2) classical bits plus O(n) qubits,
established before charging addresses, so address width is O(log(n+2)).
A fixed finite set of index additions per logical gate uses O(log(n+2))
Boolean operations, each paying full O(log(n+2)) indexed-access cost.
O(log^2(n+2)) per logical gate therefore covers controller generation,
local access and gate addressing. Stack updates happen once per recursive
node and fit within that per-gate budget. Long Grover-counter work per
query is dominated by the score calculation. No large-word operation is free.

One score reflection uses O(m n^(8/5))=O(n^(13/5)) logical gates,
including all normalization, products, reciprocal correction, score lookup
and full reverse work. Loading each classical label as a computational-basis
constant and later clearing it uses O(n) gates; this is already dominated.
The fixed reciprocal and modulus occupy O(n) classical bits. There is no
per-record list of n modular multiples to generate or store. All classical
record reads and generated gate constants pay the same complete charge.
Diffusion uses O(n) gates and O(n) clean scratch. With
j<=3*2^(n/2)/4 iterations, total search work is therefore
O(2^(n/2)n^(13/5)log^2(n+2)). Every failed branch and all inverse circuits
are included. Table accesses remain finite counted gate networks.

Preprocessing is polynomial and also explicitly charged. There are
2m(J+1)M=O(n^3) Hadamard-test translations, each O(n) gates with the stated
addressing, for O(n^4 log^2(n+2)) work. Resetting and measuring all test
ancillas is within that bound. Collecting signed observation counts uses
O(log M)-bit arithmetic with the same charge. Decoding the constant-size grid,
rational lifting/rounding, residue constants, random basis bits and recording
all labels fit a conservative O(n^5) work bound. Each decoder denominator has
O(n) bits after lifting, so schoolbook multiplication/division and addressed
access are included in that allowance. Computing the reciprocal by charged schoolbook division, and H,M,m,J,j by binary arithmetic
and integer square root fits O(n^4) work and O(n^2) classical storage; fixed
rational table generation/storage adds a finite absolute constant. Source
acquisition costs m(n+1)=O(n^2). Every source data/control register is released
before the next copy; classical labels persist. All input, loop counters,
reciprocal, padded arithmetic bands, intermediate integers, outputs and tables fit O(n^2) classical
bits and O(n) qubits. No branch allocates a matrix of amplitudes.

The total preprocessing O(n^5+n^4 log^2(n+2)) is absorbed by
2^(n/2)n^(13/5)(log2 n)^2 uniformly for n>=2: its ratio tends to zero and is
bounded on the finite prefix. Since log(n+2)=Theta(log n) there, the claimed
supported time envelope follows with an absolute outside constant. The n=1
branch is fixed finite work. Every sampling, label-measurement and Grover loop
has the explicit deterministic ceilings above on every outcome. Label errors,
bad scores, invalid measured candidates and discarded copies do not change
the allocation or acquisition bound. Q is exactly m=2048(n+10) on all branches.

## Structured envelopes, model and comparison

The four envelopes are2^(n/2)n^(13/5)(log2 n)^2,n^2,n,n. Their logarithms give
exact growth indices1,0,0,0: the time logarithm is n/2+O(log n), and all
other envelopes are polynomial. The coefficient1/2 in the exponent is
explicit, not an unknown big-O constant. The time logarithmic expression
is for n>=2, with the finite n=1 resource exception explicit above.
Every claim concerns this one choice of m,J,H,M and the exact score predicate.
The fifth count law is tau(n,Q)=floor(Q/10), actual Q=m, under the fixed-
position product-independent-ideal corruption model stated in full above.
Malformed states may be jointly entangled among themselves; all honest
copies remain independent ideal states for the same s. The same unconditional
success and all four resource bounds hold jointly under every allowed input.
This is a proved count guarantee, not an assertion that a larger count is
impossible and not a per-copy corruption probability.

Relative to RLQGR1, all memory, sample and tolerance envelopes are unchanged,
while the declared time ratio is n^(-2/5), tending to zero. This improvement
comes from a different exact arithmetic algorithm, not a relabeling of an
unchanged bound or a numerical growth-index change. The time index remains1.
The corruption-model text is byte-identical to RLQGR1 and the tolerance law
remains floor(Q/10), so these full guarantees are directly comparable.
Relative to retained-block RGRST1, this algorithm has fewer qubits but more
classical storage, larger polynomial time and a smaller tolerated fraction;
those remain resource tradeoffs, not dominance. No comparison of upper
envelopes establishes tight lower bounds or optimality. The claimed result
is not subexponential in n, a new fastest-known DCP algorithm or the cube-root
goal. The external Karatsuba method is attributed as established arithmetic.
