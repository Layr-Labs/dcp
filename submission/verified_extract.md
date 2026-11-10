# Uniform high-confidence Fourier-label extraction (current)

This replaces the cheap estimate, random-shift verifier and rare RUN of
CS1-C3Q32076cd3-77d5-4058-813d-7e66be4714f8, whose source/QPE/compiler
route remains credited. The current LE below has no verifier or RUN
counter. The exact source identities and all outer algorithms remain.
Conceptual references: Cleve and Watrous, quant-ph/0006004, Section4
(multiplication-based QFT), and the phase-gradient method of Nam et al.,
npj Quantum Information6(2020), doi:10.1038/s41534-020-0257-5. The actual
uniform Clifford+T construction, bit work and error bounds used HERE
are explicit below. In particular no exact arbitrary-angle gate is a
primitive. The existing Dawson--Nielsen compiler proof is reproduced in
approx_estimate.md; its compiled words occur only in initialization.

## Parameters, finite guard and one-time preparation

Compute the exact outer Qcap=20rC_0+K before acquiring sources. Put
 t=ceil(log2(2^50 Qcap))+8, m=n+t,
 b=ceil(log2(2^50 Qcap(m+1)))+8.
These are integer bit lengths. Eventually t,b<2r and m<2n. First run
the exact n-only compiler/layout guards below, BEFORE any acquisition.
If any guard fails, run the complete exhaustive algorithm of
 distance_decoder.md Section13 on the ENTIRE problem. This extends that
algorithm's original small-n branch to deterministic exceptional lengths;
it never returns a made-up label or assumes an unproved estimate.
Its source bound is N(n+10), its ordinary storage O(n), and its success
is >=1-2^-10 by the same proof at every N. The guard-failure set of n is
finite as proved below, so this branch changes only absolute constants
in all four asymptotic bounds. Qcap bounds only the fast branch.

Set J=80 and eta=2^-100/J. Compile the fixed J rotations
 Rz(-2pi/2^j), 1<=j<=J, with certified operator error <=eta.
Use exactly the inverse-closed Clifford+T representatives, constructive
constant-net search, rational interval evaluation and recursive
Dawson--Nielsen compiler in approx_estimate.md. All angles, certification
precisions and the number of templates are FIXED CONSTANTS independent
of n. Guard their ACTUAL total ordinary code/directory and workspace by
one n-bit buffer each and their actual Boolean compilation/certification
work by n^2, including the finite net generation. Incomplete or absent
certificates select the exhaustive whole-problem branch. The exact
constructive density/compiler proof implies finite constant requirements,
so these guards succeed for every sufficiently large n; no unknown
threshold is queried. All guard updates and partial erasure are charged.
Physical scalar phases of compiled words are global because each word
is applied unconditionally, never as a controlled phase-ambiguous word.

In the reserved private prefix let B_G be the least power2>=8r+128.
Reserve the b gradient qubits in the fixed block beginning P-w-B_G,
with actual odd slot-wire map2k+3 as elsewhere. X still begins P-w.
Require b+16<=B_G, m<2n and this gradient block disjoint from every
actual source/tree/FW work span and below X, with low work end<c_F.
The existing polynomial native work layouts plus this O(r) block fit
for all sufficiently large n. Check the actual spans before sources;
on overflow select the same exhaustive branch. P, HQ, OWN, ROWS and
full prefix geometry are unchanged; the gradient consumes reserved
capacity, not an uncounted register. Compile buffers are ordinary;
the gradient itself is quantum memory counted in P.

Reset and H all b gradient bits. For j<=min(J,b), apply its compiled
rotation to physical gradient bit b-j; for j>J apply no rotation.
This prepares an approximation to
 |G_b>=2^(-b/2) sum_(y<2^b) exp(-2pi i y/2^b)|y>.
Indeed its ideal tensor factor at bit b-j is
 (|0>+exp(-2pi i/2^j)|1>)/sqrt2, up to scalar phase.
The sum of omitted angle magnitudes is <=2pi*2^-J; the compiled-word
errors sum to <=J eta. Thus the complete initialized state is within
norm delta=2pi*2^-80+2^-100<2^-76 of |G_b>, up to ONE global phase.
These are actual compiled words and b Hadamards, not a supplied state.
Initialize it ONCE and preserve it through every source, FW and TREE
operation. Per-module used-region resets explicitly exclude this block.
Only full cleanup at return/abort resets it. All its lifetime is counted.

## Exact kickback, truncation and global preparation error

For an integer z, modular ADD_z on the gradient gives
 ADD_z|G_b>=exp(2pi i z/2^b)|G_b>.
Change summation variable y'=y+z modulo2^b to verify this identity.
It holds coherently for quantum-controlled z and arbitrary spectators:
the ideal gradient factors out unchanged after every such addition.
Use clean reversible addition, not a quantum-addressed load. For a
q-bit operand, compute its sum with the target into zero scratch, swap
with target, then compute the inverse difference to clear old target.
This realizes an in-place sum with O(q) Boolean/Clifford+T gates and
O(q) clean scratch. All gates use fixed wires; input values control
ordinary quantum gates rather than selecting physical addresses.

To apply a product phase exp(2pi i AB/2^q), compute the full product
AB in clean native SSA using the reproduced Toom3 Boolean circuit.
For q>=b, add its b bits at positions q-b,...,q-1 to the gradient.
This realizes exp(2pi i floor((AB mod2^q)/2^(q-b))/2^b), whose scalar
phase differs by at most2pi*2^-b on every computational basis input.
For q<b, add its low q bits shifted b-q. This is the exact phase.
Crucially that shifted sum changes ONLY the top q gradient bits;
its actual ripple circuit has length q, not b. Lower gradient bits
are untouched. Reverse the whole product computation once to clear
all its SSA scratch. This clearing is exact even for an imperfect,
entangled gradient: the addition did not change the product operand.
Only the ideal factorization assertion uses |G_b>.

Preparation error is global, not a fresh-state error per operation.
Compare the actual entire algorithm with one initialized with |G_b>,
using the SAME subsequent fixed/adaptive CPTP maps, including every
measurement, classical branch, reuse and cleanup. Initial pure-state
norm distance <=delta bounds trace distance <=delta, and contraction
bounds the distance of the entire final classical outcome laws by
delta. There is NO multiplier equal to the number of reuses. Actual
imperfect-gradient correlations are retained in that comparison; no
conditional per-call independence of the actual gradient is assumed.
The ideal-gradient reference admits the exact factorizations above.

## Recursive inverse Fourier circuit

Write q=a+d, a=floor(q/2), d=q-a. Input x=x_L+2^a x_H.
Apply F_(2^d) to the high d bits, naming their output y_L. Apply
exp(2pi i x_L y_L/2^q) by the product-phase circuit above. Apply
F_(2^a) to the low a bits, naming output y_H. Rotate the two output
blocks to represent y=y_L+2^d y_H. This is F_(2^q): expanding xy/2^q
modulo integers gives x_H y_L/2^d+x_L y_H/2^a+x_L y_L/2^q.
Base q=1 is H. Unequal block rotation is three fixed bit reversals,
O(q) SWAPs with known classical wire coordinates. The inverse circuit
is its literal reverse with negative phases. No basis state or phase
value selects a physical address. Product functions use the same clean
copy/compute/reverse implementation on arbitrary quantum inputs.

There are q-1 product-phase nodes, so for ideal gradient the complete
circuit's operator error against exact F_(2^q) is at most
2pi q2^-b by telescoping unitary errors; exact small-node phases add
no error. The inverse obeys the same bound. This derivation also fixes
all phases of the implemented circuit, rather than controlling an
unspecified unitary up to scalar.

## High-confidence label measurement and source channel

Given actual data eigenstate chi_k and arbitrary spectators, prepare
m zero ancillas and H them. The product of controlled translations
by -2^i mod N is the single exact permutation
 |x>|u> -> |x>|u-x mod N>, 0<=u<N,
extended by identity when u>=N. It prepares
 2^(-m/2) sum_x exp(2pi i xk/N)|x> tensor chi_k.
Compute x mod N by the FAST Barrett product described below, not
bitwise long division in each call. Compute the clean modular
subtraction, swap and clean inverse addition to implement exactly
this permutation on all padded inputs. Source data operations are
exact Clifford+T words; Fourier/gradient approximations act only on
estimate ancillas. Data therefore stays chi_k, including after an
ancilla measurement, in the ideal-gradient reference.

Apply the recursive inverse Fourier circuit, measure z and return
 round(Nz/2^m) mod N, ties deterministically toward the lower integer.
With an exact inverse QFT the same geometric-series calculation as
approx_estimate.md gives, for L=2^m and a=L/(2N)>=2^(t-1),
 Pr[wrong label] <=1/(2(floor(a)-1))<=2^(2-t).
This bound is uniform in k. It follows by sorting measurement values
by circular distance from Lk/N, using sin(pi d)>=2d and summing
1/(4L^2 d^2) outside distance a; there are at most two values in each
unit distance shell. Correct rounding holds inside that radius.

Across at most Qcap adaptively requested copies the exact-QFT wrong
label probability is <=Qcap2^(2-t)<2^-50. The sum of inverse-QFT
operator errors over all calls is <=2pi Qcap m2^-b<2^-50.
Adding the ONE global gradient-preparation distance gives a total
actual/ideal outer-law coupling smaller than2^-40, in particular
below the old2^-10 extraction allocation. The ideal process replaces
each label by latent k and omits all extraction-private records,
including the gradient and estimate outcomes, from its outer logical
conditioning. It has exactly the same independent uniform latent
labels, source transforms and phase states as before. This is an
additive coupling; it does not condition on correct labels or future
cutoff survival. The previous separate verifier/RUN-cap event is gone.
The retained supplier, key, pool and decoder failure budgets therefore
still establish unconditional full-secret success >=1-2^-8.

## Actual Boolean arithmetic, emitter and complete resource count

The full Toom3 source kernel has five recursively multiplied children
of width ceil(s/3)+O(1). Its unchanged signed interpolation/exact small
divisions, fixed SSA compute-copy-reverse and ordinary active-worklist
proof are in typed_dispatch.md. Retain the sharper width recursion:
raw gates plus its fixed polynomial driver are bounded by
 C(k+1)^c 5^k for s=O(3^k). Since5^15<3^22, every such fixed
polynomial in k is absorbed by O(s^(22/15)). This counts full argument
formation/initial high zeros once per source scope and every actual
low-index bit update, not just multiplication gates. Weighted by full
d=Theta(r), a constant number of full-width products costs n^(59/30).
Ordinary worklist data is still <=4096s plus counted recursion metadata,
inside2^16n under the same actual layout guard. At a QFT node the
ACTUAL kernel word formats have its current width s; initialize/clear
all4096s active worklist bits and their used metadata, not the whole
2^16n capacity per node. Every field is fully written before use and
no stale higher field is read. Its complete physical argument buffers
retain initialized high zeros across these inline products and rebuild
only their low polynomial coordinates. Source T1 has its original full
n-width formats. Used quantum product spans are cleared/reset at their
actual s-dependent length; unused native capacity is charged globally
by prefix setup/cleanup. This is an explicit variable-width subroutine,
not a partial read of unchanged n-bit operands. Private SSA scratch is
O(n^(22/15)) times fixed alignment factors, below c_F eventually.

Precompute mu=floor(2^M/N), M=m+2, once per batch or globally for N.
Long division of this one fixed constant has polynomial charged work
and O(n) ordinary words. In each call x<2^m<2^M, so
 q=floor(x mu/2^M) differs from floor(x/N) by at most one downward.
One full comparison/subtraction corrects its remainder. All products
have O(n) operand bits because m<2n, and the correction is O(n) raw
Boolean work. This is exact Barrett division on all inputs, including
arbitrary wrong-label branches. Rounding Nz/2^m uses the same full
product, bit shift and one carry. Source T1 uses its exact existing
constant number of products; T2 and complete native exports cost less.

For the recursive QFT, sum of multiplier work at each binary split is
bounded by sum_j 2^j(n/2^j)^(22/15)=O(n^(22/15)). The complete fixed
polynomial bit-emitter factor is absorbed using the same strict gap
above, or n poly(log n) for the small nodes. Gradient additions total
O(n log b) raw gates: below b they cost O(q) per node and above b the
geometric sum of O(b) per node is O(n). Count all block SWAPs too.
Every private wire is polynomial in n; COMPLETE d-bit argument buffers
are initialized once per LE with high zeros. Per node/gate the explicit
low B=O(log n) coordinates may be rebuilt with counted polynomial-log
bit work. They are never rebuilt as whole d-bit words per small node.
Each gate/access consumes ALL d argument bits and pays d. Full input,
source frames, ordinary clear scopes and final cleanup are counted.
No uncounted ordinary instruction list or wire-version map is stored.
Thus the entire per-copy source/preprocessing/extraction work is
 O(n^(59/30)), and its executed total is
 O(n^(59/30) Qcap)+poly(n).
Compiler/constant generation, complete gradient initialization/reset,
all measured ancillas and aborted-call cleanup are included. Bootstrap
is polynomial, with prefix preparation still counted separately.
