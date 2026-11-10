# Guarded cheap Fourier-label estimate

Material source: CS1-C3Q, submission32076cd3-77d5-4058-813d-7e66be4714f8,
evaluated sourcec80fdd7c40bac9f0f594c66fa0781457ae673e5d, proof.md Section5.2
and its uniform rotation-compilation argument. That source uses Dawson
and Nielsen, The Solovay-Kitaev algorithm, arXiv:quant-ph/0505030v2,
Theorem1 and Sections3–4. The exact circuit, probability and compilation
arguments are reproduced below. No prior verdict is a premise. This
file adds the explicit deterministic resource guard and mode accounting.

On the main branch n>=2^40, before ANY source acquisition, attempt the uniform template construction
below. Use its integer n-only parameters and target rotation tolerance
eta/64 for compilation. Include all initialization and base-net search
in this attempt. Limit the attempt to n^2 compiler elementary classical bit
operations, n bits of compiled words INCLUDING angle/layout metadata,
and n bits of compiler workspace, checking before every allocation and
compiler operation. The O(log n)-bit budget-counter updates are also
charged, adding at most O(n^2 log n) one-time bit work; they do not
recursively count themselves against the compiler-instruction budget. If a limit would be exceeded, discard partial words and set
MODE_RUN. Otherwise certify each word's accuracy as below; any absent
certificate sets MODE_RUN. Set MODE_QPE only when ALL templates are
complete and certified. This is a fixed deterministic function of n,
not of N,s,latent labels or any measurement history. It does not abort
the challenge and consumes no source copies.

In MODE_RUN the cheap estimate is the existing RUN(F(h_A)) of
verified_extract.md, with its error bound at most1/(2n). In MODE_QPE
use the following estimate. BOTH modes use exactly the same subsequent
random-shift verifier, high-confidence fallback and global fallback cap.
No estimate is accepted merely because compilation completed.

Let q=ceil(log2(4096n)), m=n+q, L=2^m. On m zero ancillas prepare the standard
phase-estimation state using H and controlled translations by -2^j mod N.
Generate the constants2^j mod N by modular doubling, keeping only the
current n-bit constant; no m-by-n table is stored. For latent data
eigenstate chi_k, the resulting ancilla state is
L^(-1/2) sum_(x=0)^(L-1) exp(2pi i x k/N)|x>.
The data and all source spectators remain exactly unchanged. Apply inverse
QFT over Z/LZ, measure z, and return round(Nz/L) mod N.

The exact-QFT measurement probability is
 |L^(-1) sum_x exp(2pi i x(k/N-z/L))|^2.
For circular distance delta=||k/N-z/L||<=1/2, sin(pi delta)>=2delta, so
p(z)<=1/(4 L^2 delta^2). Sorting z by distance from Lk/N, at most two points
have distance in [r,r+1). If a=L/(2N)>=2048n, the probability of distance >=a
is bounded by (1/2) sum_(r>=floor(a)) r^-2 <= 1/(2(floor(a)-1)) < 1/(1024n).
Thus rounding fails with probability <1/(1024n) for every k.

Implement inverse QFT with its standard H, swaps and controlled phases
CP(phi)=diag(1,1,1,exp(i phi)), phi=-2pi/2^r. Omit phases with r>b,
where b=ceil(log2(2^20 n m)). Their summed operator-norm error is at most
2pi m 2^-b <1/(2^16 n). There are at most mb retained phases.
Implement each CP(phi) up to a global phase by
Rz(phi/2) on both wires, CNOT, Rz(-phi/2) on target, CNOT.
Direct evaluation gives relative phases (1,1,1,exp(i phi)).
Use the certified compiled words below for each of the at most 3mb
single-qubit rotations with norm error
eta=1/(2^22 n m b). Total synthesis error is at most 3/(2^22 n).
Total circuit error is <1/(2^15 n); total-variation error in measured z is
at most twice this. Therefore total cheap-estimate error is <1/(512n),
which is stronger than the inherited 1/(2n) requirement.


The inverse QFT referred to above is an explicit circuit. With qubits
numbered from zero (least significant), first reverse their order by swaps.
For j=0,...,m-1 apply CP(-2pi/2^(j-k+1)) between j and each k=0,...,j-1,
then H on j. Reversing this circuit, direct induction gives
F_L|x>=L^(-1/2)sum_z exp(2pi i xz/L)|z>, proving the claimed inverse.
Only the truncation and synthesized rotations specified above replace
these ideal gates. The full-width QFT is a proof reference, not an
unimplemented oracle.

## Uniform rotation compilation used only on estimate ancillas

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

For this application b=O(log n), m=O(n), and log(1/eta)=O(log n).
There are O(b) distinct angles; compile their templates once, with
poly(log n) storage and initialization work. Each call uses O(n^2)
core steps for controlled translations and their modular constants,
and n poly(log n)=O(n^2) for all Fourier gates, template expansion,
counters, and phase decoding. Here the polylog power is an absolute
fixed constant: (log n)^d/n is bounded on integers n>=64 for every fixed d.
The asymptotic outside constant need not be small at concrete sizes.
The m estimate ancillas and reusable modular arithmetic use O(n) qubits.
The data register is still exactly chi_k after the procedure because
all data operations are controlled exact eigen-translations and every
approximation acts only on estimate ancillas. Thus spectators remain
unchanged, also after conditioning on measurement results.

The proved failure bound <1/(512n) implies

    Pr[k_A!=k] <= 1/(2n).                                                   (5.E)

This is uniform in k and prior history. The same inequality holds in
MODE_RUN by the reproduced RUN concentration proof. Thus the unchanged
verification and stochastic domination apply in both modes.


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
small resource budgets choose MODE_RUN instead of assuming an uncharged
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
or certify within the guards chooses MODE_RUN, before any data state is
acquired, so it cannot introduce source-label bias or a new error event.

There are O(log n) angle templates, each with poly(log n) gates and
precision bits. Compilation, certification and workspace have a fixed
polynomial in log n bound, including the finite constant net cost.
Consequently, for ALL sufficiently large n they fit the n-bit word and
workspace buffers and n^2 bit-work budget. MODE_QPE is then always used.
No unknown threshold is consulted by the program: the actual guards
fully specify its behavior. At the finitely many exceptional lengths,
MODE_RUN has its proved terminating caps and the same success bound.
Their finite set of N,s and bounded branches changes only the absolute
constant in the asymptotic time envelope. No small practical threshold
or useful physical runtime is claimed.

The code buffer and compiler workspace are TWO explicitly allocated
ordinary n-bit buffers, counted in S_C alongside the existing constant
many O(n)-bit staged words, input and output. They are not an uncounted
circuit description or a growing source recursion stack. All metadata
must fit INSIDE those buffers. Source algorithm recursion remains in the
basis-state bank. At compiler completion workspace is released; the
bounded code buffer is read and charged on every template use. Partial
code is erased before MODE_RUN. The total remains within a fixed
constant times n ordinary bits (in particular the existing2^20n staging
allowance: fewer than2^16 staged n-bit fields plus these two buffers
and the input/output remain below2^20 n bits).

The m estimate ancillas and O(n) arithmetic scratch are within c0 n;
there are still fewer than1024 fixed registers of at most4n qubits.
No quantum slot, descriptor or full physical prefix is omitted or
reduced. The compiler uses no quantum data. Its guarded work, including budget
control, has only polynomial charged physical cost and is included in
bootstrap.

## Structural work in the complete algorithm

For all sufficiently large n, the estimate has O(n^2) elementary work:
n controlled translations each O(n), plus n poly(log n) Fourier gates,
word decoding and rounding. The incremental local emitter of
verified_extract.md charges O(log n) per elementary gate, including
all template reads, reversals and actual local-index tuples. Thus cheap
extraction costs O(n^2 log n) structural work per call. Polynomially
logarithmic compiler overhead is paid once before source acquisition.

Verification costs O(n^2) preprocessing and O(n h_e log n) reference
bit work. The counted local field-stream generator in typed_dispatch.md
adds at most O(log n) to those bit steps, so it fits O(n^2 log n), since
h_e=O(sqrt n) and log n<=sqrt n. High-confidence exact RUN has aggregate
O(n^2 h_e log n)(Qcap/r+1)=O(n^2 log n Qcap)+poly(n), by the same global
fallback cap. Therefore complete LE structural work is
O(n^2 log n Qcap)+poly(n). Finite guarded MODE_RUN exceptions are
absorbed as stated above, with all actual-branch caps retained.

The current verifier's uniform correct-reject/wrong-accept probabilities
and its coupling require only (5.E) and unchanged eigenstate spectators,
which both modes satisfy. Wrong labels and fallback abort retain their
previous budgets. The independent global key cutoff is unchanged.
No success probability is conditioned on compilation, numerical success
or future cutoff survival; compilation mode is deterministic in n.
