# Uniform compiler for one-time phase-gradient preparation

The normative current source algorithm is verified_extract.md. Compile only
its J=80 fixed unconditional rotations at its fixed constant tolerance.
The following constructive compiler/net/certification proof is retained
from the credited CS1-C3Q route32076cd3-77d5-4058-813d-7e66be4714f8;
no approximate real-angle gate is a primitive. Apply the actual n-bit code,
n-bit workspace and n^2 work guards BEFORE sources. Failure selects the
complete exhaustive full-problem branch. All target angles, requested
precision and template counts are constants, so all requirements are
finite constants and every guard eventually succeeds.

Algorithmic source: Dawson and Nielsen, The Solovay-Kitaev algorithm,
arXiv:quant-ph/0505030v2, Theorem 1 and Sections 3-4. For a fixed inverse-closed
dense single-qubit gate set, their recursive compiler uses a constant net,
commutator corrections and recursion depth O(log log(1/eta)). Its error
contracts as epsilon -> C epsilon^(3/2); sequence length multiplies by five
and recursive compilation calls by three. Thus length and computation are
poly(log(1/eta)). We use this algorithm, not an oracle. Generate the fixed
net by word enumeration and certified constant-radius covering once, charging
its finite cost. Evaluate targets and intermediate matrices with guard precision
O(log(1/eta)) bits, enlarged by a fixed constant factor to bound accumulated
rounding error by eta/2. Matrix arithmetic then adds only polynomial bit
factors. Working storage is poly(log(1/eta)). Inverse words use reversed
sequences of inverse gates. The gate set uses the inverse-closed representatives listed below, physically H,T,T^-1 up to scalar phases;
only unconditionally applied single-qubit gates are compiled, so such phases
are global. Controlled phases are first decomposed into CNOTs and unconditional
rotations. This supplies the required uniform bit-cost guarantee.

Applicability of density can be seen directly, rather than assuming an
additional universality oracle. Put A=Rz(pi/4), B=Rx(pi/4)=H A H. Up to a
scalar these are available T and H T H. For V=AB its half-angle theta has
2cos(theta)=1+1/sqrt(2). This is not an algebraic integer: its irreducible
primitive integer polynomial is 2X^2-4X+1. If theta/pi were rational, twice
its cosine would be a sum of roots of unity and hence an algebraic integer.
Thus powers of V densely cover rotations about its axis. That axis has
nonzero x and z components. Conjugation by Z gives a nonparallel axis.
The two corresponding one-parameter subgroups generate SU(2): their
infinitesimal generators and their commutator span its three-dimensional
Lie algebra, so their closed subgroup has full dimension and is SU(2).
All inverse gates are available as fixed words (T^-1=T^7 and H^-1=H).

For angles that are rational multiples of pi, target entries can be computed
to p bits with poly(p) Boolean work using alternating arctangent series for
pi, range reduction and Taylor evaluation for sine/cosine. With p=O(log n)
this is poly(log n). The constant net is generated during the algorithm;
it is not instance-dependent advice or a preloaded uncharged table.


## Explicit template certification, guard and storage

Use the inverse-closed SU(2) letter representatives
{iH,-iH,Rz(pi/4),Rz(-pi/4)}, encoded by two bits. Their physical gates
are H,H,T,T^7 respectively. Matrix certification uses the representatives;
physical execution differs only by the known product scalar. Inversion
reverses a word and exchanges its inverse letter codes. This explicitly
handles H's determinant phase and does not control a phase-ambiguous word.
Pack code letters and an angle directory in the guarded n-bit buffer.
Directory offsets/lengths use ceil(log2(n+1)) bits, so O(log n) entries
need only O((log n)^2) metadata bits, not one full n-bit word per angle.
All directory/table reads and per-use word expansion are charged.

A fully uniform initial-net construction can be fixed in advance as a
PROGRAM, not data: take base error epsilon0=2^-20 and the normalized
nonzero rational quaternion grid with coordinates i/2^28, |i|<=2^28.
Its covering radius on SU(2) is less than epsilon0/16. Enumerate gate
words by length until every grid point has a certified word within
epsilon0/4, using rational interval bounds. Density and compactness give
a finite strict covering, so this search terminates with a fixed finite
cost and storage independent of n. The compiler guard counts all of it;
small resource budgets choose the whole-problem exhaustive branch instead of assuming an uncharged
net. Grid rounding and its certified words give the base approximation
required by the cited recursive compiler. The exceptionally large fixed
cost has no practical-runtime interpretation.


The compiler uses the inverse-closed determinant-one representatives of
Clifford+T letters; actual H,T,T^-1 words differ only by known scalar
phases. Evaluate their2x2 matrices and the Rz target entries with rational
interval arithmetic. For each real and imaginary entry require its
absolute error upper bound to be at most eta/16. This implies Frobenius
and hence operator-norm error below eta. Requesting compiler error
eta/64 gives strict slack for certification; evaluate products and
trigonometric targets with enough guard precision that interval widths
are below eta/64. Known scalar phases need not be physically applied:
words occur only as UNCONDITIONAL single-qubit rotations after the CP
decomposition. A word is never promoted to a controlled gate up to an
unknown relative phase. T^-1 is the exact word T^7 if needed.

All matrix arithmetic, precision increases, net search, word enumeration,
verification, word copies and inversions are included in the bit-work
and space limits. The compiler is constructive, not an oracle: its fixed
initial net is generated by word enumeration with covering certification,
as in the cited algorithm. It is neither instance advice nor preloaded
memory. Recursion uses only its bounded workspace. A failure to finish
or certify within the guards chooses the whole-problem exhaustive branch, before any data state is
acquired, so it cannot introduce source-label bias or a new error event.


The current J fixed templates need a constant-size directory, represented
inside the guarded code buffer. All compilation, certificates, matrices,
net searches, word copies and guard control are charged, with no instance
advice. On success their physical H,T,T^7 words prepare the gradient once;
no rotation template is executed during any subsequent source QFT.
On failure discard all partial buffers before the exhaustive branch.
Because every requirement is a fixed finite constant, both n-bit buffers
and n^2 work suffice for every sufficiently large n, without the program
querying that unknown threshold. The buffers and all ordinary input,
output, source/controller/worklist scopes remain within2^20n bits.
