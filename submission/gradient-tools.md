# A counted approximate gradient for known classical phase corrections

This helper uses the mixed-eigenlabel preparation developed in CGRST1
bc7954eb-c7bb-47c0-abcd-6a95a0257673 (unpublished after a hosted review failure).
It is reproduced in full. The reusable-gradient kickback and one-initial-
trace-distance design was materially consulted in PG4
e40f2d5a-68c9-418b-b4e8-64a80305968e, phase-labels.md Sections2-3.
That source credits Nam, Su and Maslov, arXiv:1803.04933v2 SectionII.
Our preparation below is different from PG4's pure-state preparation; no
PG4 Fourier circuit, code or arithmetic subroutine is assumed. label-tools.md
reproduces the needed source-only eigenvalue measurement with fixed tables.

Put p=n+ceil(log2(Qcap+2))+40 and K=2^p. The analytic reference is
Gamma=K^(-1/2)sum_y exp(-2pi i y/K)|y>.
Controlled translation by an integer c modulo K gives phase exp(+2pi i c/K)
on its control and leaves Gamma unchanged, by reindexing the sum. This holds
on superposed controls and entangled external systems. The actual algorithm
is NOT given Gamma or a purification of any source.

For at most A=n+20 attempts prepare a maximally mixed p-bit register by
Hadamards on zero followed by computational measurements whose results are
erased and never used. This is I/K, equivalently a UNIFORM ensemble of Fourier
vectors chi_b. Apply label-tools.md with modulus K,d=p,planned count C=A.
If its observed label b is even reset/release the register and continue.
If odd, compute a=-b mod K and its odd inverse by counted extended Euclid.
Apply y->a*y mod K and retain the register. If no observed odd label occurs,
abort the whole DCP algorithm and output zero. Every attempt is counted.

The odd constant permutation is implemented with elementary arithmetic:
compute a*y mod2^p by p controlled additions of a*2^i into a clean p-bit
accumulator, copy result and reverse; this is a clean compute-XOR map.
Use compute,swap,inverse-value evaluation to implement the permutation in
place, with the classically computed inverse a^(-1). Each controlled ripple
add costs O(p) gates and O(p) reused scratch, so complete product/permutation
costs O(p^2) gates and O(p) qubits. There is no retained p^2 Boolean history.
All operations are exact NOT/CNOT/Toffoli and their fixed Clifford+T
decompositions. Every original/temporary register and inverse is included.

On a correctly learned odd latent b the permutation maps chi_b to
chi_(b*a^(-1))=chi_(-1)=Gamma. Fresh mixed registers have independent uniform
b, so all A true labels even has probability2^(-A). The lemma's union of
all gradient-label errors is<1/2048 and2^(-A)<1/2048 in the large branch.
Thus bad-gradient/abort weight is<1/1024. The physical retained state is
generally MIXED, not a heralded exactly pure Fourier state. Its good analysis-
ensemble components all equal Gamma, and the rest may be arbitrary. Replacing
it and aborts by an always-supplied ideal Gamma costs at most1/1024 in trace
distance for the final algorithm. Metadata is unused thereafter. Contractivity
charges this ONCE for the entire future adaptive computation, not per reuse.
The ideal invariance is not asserted for the imperfect physical state.

For a known source label k and known previous residue s0, compute
z=k*s0 mod N and c=floor(K*z/N) CLASSICALLY by charged schoolbook bit arithmetic.
Controlled SUBTRACTION of c into Gamma induces exp(-2pi i c/K) on the source
control, leaves the ideal Gamma unchanged and approximates the desired
exp(-2pi i k*s0/N) within norm<2pi/K<8/K. Constant addition is the same
clean ripple permutation, O(p) gates/scratch, with full initialization,
addressing and inverse work counted. Classical k,s0 do not require QRAM or
quantum multiplication. There are at most Qcap such corrections, so the
whole-computation comparison is<=8Qcap*2^(-p)<1/1024. Computational measurements
and feedback are quantum channels and do not amplify an earlier trace error.

All data/ancilla registers are ordinary fresh zeros; no extra DCP source copy
is acquired here. label-tools.md uses J=p+4 and O(log n) repetitions per basis,
p<=2n, and at most2n attempts. Together with the p-bit odd permutations,
resets, measurement outcomes, Euclid, classical division, bit-index generation
and discarded attempts, a conservative2^80 n^8 basic-step bound covers this
helper in QSR14's large branch; fixed rational tables are generated before
the clock. Peak quantum scratch is O(n), and classical scratch polynomial.
The actual branch counters enforce all work ceilings even on bad preparations.
