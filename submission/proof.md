# ERC-4096: exact-gate robust label sampling and classical correlation decoding

## Declaration, provenance, and what is NOT claimed

This proof is prepared anew for account web5200 under the DCP rules at
cdb1ebff130d861e2c61e9cf517ab66c0a56ca7a. ERC-4096 is a specified classical
exhaustive decoder of locally measured quantum samples. It has neither a
Grover search nor approximate quantum Fourier rotations. Its additional
statement is a nonzero guaranteed malformed-copy fraction under the explicit
nonadaptive product-clean/arbitrary-bad input model below.

This is a new algorithm/configuration and proof snapshot, not an author-name
change to an existing account-B submission. The author/controller has historical
context, so no erased-memory or historical-originality claim is made. Standard
character orthogonality, Hadamard tests, reversible arithmetic, Taylor bounds
and Hoeffding concentration are derived/applied here, rather than supplied by
any previous Yukon evaluation. This proof does not rely on another account's
review verdict or candidate files. Scientific novelty and comparison to all
known algorithms are separate questions. No new record, reward, experiment,
frontier dominance or attainment of the 2^{O(n^{1/3})} research goal is asserted.

All five submitted statements refer to this ONE ERC-4096 configuration:

* for every integer N>=2 and s in Z/NZ, n=ceil(log_2 N);
* acquire exactly m=4096(n+4) source copies, regardless of outcomes;
* total sequential work T=O(2^n n^12), time-envelope growth index 1;
* peak allocated classical bits S_C=O(n^4), growth index 0;
* peak allocated qubits S_Q=O(n^4), growth index 0;
* total acquired source copies Q=m<=20480n, hence O(n), growth index 0;
* guaranteed malformed fraction epsilon(n)=1/64 in the model in section 1;
* unconditional full-secret recovery probability at least 2/3;
* every bound holds on EVERY execution branch, including failures.

All outer big-O constants are absolute, independent of N, s, input corruption,
measurement outcomes and private randomness. The polynomial degrees are
conservative explicit ceilings, not measured or optimized complexity claims.
The time index is **1**, NOT 1/2 or 1/3. No matching lower bounds are asserted.

## 1. Full-secret task and precise corrupted-copy promise

For clean inputs, each supplied copy is the problem's mixed state

rho_s = (1/N) sum_{x=0}^{N-1} |psi_{x,s}><psi_{x,s}|,
|psi_{x,s}> = (|0,x>+|1,(x+s) mod N>)/sqrt(2).

Only the copy itself and the binary integer N are given. No x, purification,
inverse preparation, coherent preparation control, QRAM, hidden-shift or
subset-sum oracle is available or used. n is the residue bit length; the
ordinary binary integer N has at most n+1 significant bits, which are included
in the storage/work accounting. This is the specified mathematical input,
not an extra wire-format parser or a promised bounded JSON serialization.

For the additional error guarantee fix the ordered m incoming systems, each
with the same n+1-qubit layout. Before the algorithm's private random choices,
a corruption set B with h<=floor(m/64) positions is fixed; let C be its
complement and c=m-h. On the accessible incoming systems the state is a
product of c independent ideal rho_s copies at positions C and an arbitrary
joint density matrix sigma_B on positions B, with the registers interleaved
in their original order. sigma_B may be entangled across all bad positions
and may depend on N, s and the chosen set B. It is independent of the clean
copies and of future private random choices. The set and incoming joint state
are not chosen or replaced adaptively after seeing those choices/results.
Bad systems may have support on unused residue strings x>=N as well.

This is an explicit additional model, not an assertion about arbitrary
adaptive corruption. It includes the ordinary clean-input problem by h=0.
The incoming sequence is acquired one system at a time; unavailable future
source systems are not allocated algorithm storage. We never need access to
a batch-preparation circuit or to any external purification of this state.
Entangled bad systems can yield arbitrarily correlated classical records;
the proof below does NOT assume independence for those records.

## 2. Exact structural identity for an ideal copy

Let zeta=exp(2 pi i/N), and define an analysis basis

|chi_k> = N^{-1/2} sum_{x=0}^{N-1} zeta^{-kx}|x>,
|eta_{k,s}> = (|0>+zeta^{ks}|1>)/sqrt(2),  k=0,...,N-1.

Writing each problem coset vector in this basis and summing over the supplied
uniform x gives the EXACT density-matrix identity

rho_s = (1/N) sum_k |eta_{k,s}><eta_{k,s}| tensor |chi_k><chi_k|.   (1)

To check the signs and off-diagonal blocks, <chi_k|x>=zeta^{kx}/sqrt(N).
The |1> branch adds the relative phase zeta^{ks}, and the x-average of
zeta^{(k-l)x} is 0 for k!=l and 1 for k=l. This works for every cyclic N,
including composite N and s=0. Thus one may analyze each ideal copy as having
a latent uniform k and the first-qubit state eta_{k,s}. This is a density-matrix
calculation, NOT an assertion that the hidden x or a purification is accessible.

The computable permutation U_N sends |x> to |x+1 mod N> for x<N and is the
identity for x>=N. On chi_k it has eigenvalue zeta^k. A controlled power of
this permutation acting on the residue and a separate test ancilla factors,
conditioned on k, as a phase qubit tensor the unchanged chi_k. It does not
alter eta_{k,s}. This factorization will allow repeated tests on the SAME
copy without acquiring further DCP copies.

## 3. Exact modular gates; no hidden preparation or rotation synthesis

For a known a in {0,...,N-1}, let f_a(x)=(x+a) mod N for x<N and f_a(x)=x
otherwise. Its inverse is f_{-a mod N}. A usual comparison, addition and
conditional subtraction computes f_a and its inverse with O(n^2) bounded
fan-in Boolean gates conservatively, on at most n+1-bit operands. In particular
x+a has n+1 bits; no overflow is dropped before comparison/subtraction.

Here is a clean implementation of a controlled permutation rather than an
uncosted oracle. For F_b(x)=f_a(x) if b=1 and x if b=0, use a reversible
Boolean-circuit lift to implement (b,x,y)->(b,x,y xor F_b(x)) with clean work
bits. Compute into a second zero n-bit register, SWAP the registers, and
XOR-compute F_b^{-1} from the new register into the old one, returning that
old register to zero. Boolean histories are uncomputed after each XOR-compute.
The exact unitary therefore maps |b,x,0> to |b,F_b(x),0> on ALL n-bit strings,
not only ideal inputs. It costs O(n^2) gates and retained-history work qubits
as a conservative bound. Controlled Boolean lifts use only a constant number
of additional clean ancillas per primitive, reused between gates.

Use exact Toffoli/CNOT/X circuits (the usual exact Clifford+T Toffoli
decomposition, not an uncompensated relative-phase substitute), with H and
S/S-dagger for preparation/measurement. Thus no arbitrary rotation, precision
of a quantum Fourier transform, free postselection or finite-gate compilation
oracle appears. Circuit generation, offsets, gate descriptions, classical
addresses, initialization and all ancillas are charged in section 8.

## 4. Bounded label extraction by quadrature tests and rational unwrapping

Define J=n+4, A=m(J+1), ell=ceil(log_2(65536 A)), and L=65536 ell.
These integers can be computed by bit length of (65536 A-1); no real logarithm
primitive is assumed. For each copy and each j=0,...,J perform EXACTLY L
X-quadrature and L Y-quadrature Hadamard tests of controlled U_N^{2^j}.
The known modular offsets 2^j mod N are generated by J doublings.
A test prepares a zero ancillary qubit with H, applies the controlled modular
permutation, measures X or Y, then resets that ancilla. X measurement is
H followed by computational-basis measurement; Y is S-dagger, H, then that
measurement. Counts are fixed in advance, even on bad outcomes.

For an ideal copy conditioned on k, the two quadrature outcomes in {-1,+1}
have expectations cos(2 pi 2^j k/N) and sin(2 pi 2^j k/N). The residue remains
chi_k and the first source qubit is not acted on. Repeated ancillary outcomes
are independent conditioned on k, since the residue eigenstate is unchanged.
There is NO reacquisition of a source copy between the tests.

Let u_j,v_j be their empirical means. For each quadrature, Hoeffding for an
interval of length 2 bounds the chance of an error greater than 1/64 by
2 exp(-L/8192). For the clean positions alone, a union bound over the two
quadratures, J+1 phases and c<=m copies bounds any such error by

4 A exp(-L/8192) = 4 A exp(-8 ell)
 <= 4 A/(65536 A)^8 < 1/256.                                  (2)

The inequality uses ell>=log_2(65536 A)>=ln(65536 A). It does not assert
any test accuracy or independence on bad systems. Their records are allowed
to be arbitrary and will be handled by deterministic boundedness.

### 4.1 A finite classical phase grid with certified accuracy

Use the fixed rational pi_*=3141592653589793/10^15. The identity
pi=16 arctan(1/5)-4 arctan(1/239), with 20 alternating-series terms for each
arctangent, bounds |pi_*-pi|<10^{-14}. This is a fixed finite rational
computation performed and charged during initialization, not advice.
For 0<=v<7 define the degree-40 and degree-39 polynomials

P_X(v)=sum_{r=0}^{20} (-1)^r v^{2r}/(2r)!,
P_Y(v)=sum_{r=0}^{19} (-1)^r v^{2r+1}/(2r+1)!.

Taylor's theorem bounds the respective errors by 7^{42}/42! and 7^{40}/40!,
each smaller than 2^{-20}. Changes of the angle by d change sine/cosine by
at most |d|. Generate, rather than preload, the 256 rational grid vectors
G_q=(P_X(2 pi_* q/256),P_Y(2 pi_* q/256)), q=0,...,255.
Their coordinate error from the true unit-circle vectors is <1/1024.
All degree, coefficient and fixed-denominator lengths here are absolute
constants. Grid storage/computation/scans are counted classical resources.

For an observed pair (u_j,v_j), select the grid vector with smallest rational
squared distance, breaking ties deterministically, and write alpha_hat_j=q/256.
If both empirical errors are <=1/64, the true nearest grid phase has chord
distance <=pi/256<1/64. The minimizing property and triangle inequality bound
the distance of the true unit vector to the selected true grid vector by

1/64 + 2sqrt(2)/64 + 2sqrt(2)/1024
 < 1/64+3/64+3/1024 = 67/1024 < 1/8.

For circular phase distance d<=1/2, the chord is 2 sin(pi d)>=4d.
Consequently alpha_hat_j is within delta=1/32, circularly, of
alpha_j=frac(2^j k/N). Phase selection uses only finite integer/rational
arithmetic; it is not an exact-real arctangent subroutine.

### 4.2 Recovering the full label, for arbitrary N

Start z_J=alpha_hat_J. For j=J-1 down to 0, choose from
{z_{j+1}/2,(z_{j+1}+1)/2} the root nearest alpha_hat_j in circular distance,
using a fixed tie rule. If z_{j+1} has circular error e<=delta, one root has
error e/2 from alpha_j; the other differs by half a turn. Their distances to
alpha_hat_j are respectively <=3delta/2 and >=1/2-3delta/2. Since delta<1/6,
the correct root is uniquely nearer. Its error HALVES; it is not reset to
the original constant error at each step. Induction yields

dist_circular(z_0,k/N) < delta 2^{-J}.

Set k_hat to the nearest integer to N z_0, reduced modulo N. N<=2^n and
J=n+4 make the circular integer error <1/512, so k_hat=k on accurate clean
tests. The dyadic z_j have O(n) bits; wrap-around, nearest-root comparisons
and the final rounding are exact bounded rational/integer operations.
Even when every test is inaccurate or the input is bad, this procedure
always returns an integer k_hat in {0,...,N-1} after the same bounded loops.

After label extraction, choose a fair independent private basis a in {X,Y}
using H and computational-basis measurement of a fresh zero qubit. Measure
the first source qubit in that basis, keep b in {-1,+1}, and save the record
(k_hat,a,b). Measure/reset and release all temporary quantum registers before
acquiring the next source copy. Exactly m systems are acquired on every branch.

The clean ideal records (k,a,b) can be coupled to the actual records so that
all clean labels agree except on an event of probability <1/256 by (2).
The first-qubit state eta_{k,s} is unaffected by the ancillary tests conditioned
on k. No independence conditional on a successful label event is assumed
later: concentration and the coupling error are combined by a union bound.

## 5. Correlation expectations and a concentration event for the clean records

For each trial candidate t in {0,...,N-1} define
F_t(k,X)=cos(2 pi kt/N), F_t(k,Y)=sin(2 pi kt/N).
For an ideal record, E[b|k,a]=F_s(k,a). Using a uniformly random basis and the
uniform k in (1), exact finite character orthogonality gives

E[b F_t(k,a)]
 = (1/(2N)) sum_k (cos(2 pi ks/N)cos(2 pi kt/N)
                  +sin(2 pi ks/N)sin(2 pi kt/N))
 = (1/(2N)) sum_k cos(2 pi k(s-t)/N)
 = 1/2 if t=s and 0 if t!=s.                                  (3)

No primality, coprimality, random-mapping heuristic or known-s assumption is
used. This separates the ENTIRE secret s from every competing residue.
For each fixed t, the c CLEAN variables b F_t are independent and bounded
in [-1,1]. Their independence comes from the promised product clean state
and separate fresh private basis choices. Bad systems are independent of
that product, and the prescribed local test schedule is not adapted to
other records. Correlations among bad systems are irrelevant here.

Let R_t be the sum over clean positions of these ideal variables. Hoeffding
with deviation m/16 gives the two one-sided bounds

Pr(R_s < c/2-m/16) <= exp(-m^2/(512c)) <= exp(-m/512),
Pr(R_t > m/16) <= exp(-m/512), for each t!=s.

c>0 because h<=m/64. Union bounding N events (or conservatively 2N events)
shows that, with probability at least 1-1/128, simultaneously

R_s >= c/2-m/16, and R_t <=m/16 for every t!=s.                 (4)

Indeed 2N exp(-m/512)<=2 exp(n ln2-8(n+4))<1/128 for all n>=1.
Candidate sums need not be mutually independent. This event is asserted on
the latent IDEAL clean records before conditioning on label correctness;
combining it with (2) does not silently alter the means in (3).

## 6. Exact finite scores and deterministic protection against bad records

For z=(kt) mod N compute v=2 pi_* z/N and define the signed integer
q_t(k,a)=floor(4096 P_a(v)), using Euclidean floor for negative values.
By the Machin/Taylor bounds above and the extra floor error,

|q_t(k,a)/4096 - F_t(k,a)|
 <= 2*10^{-14}+2^{-20}+2^{-12} < 1/1024.                       (5)

It also follows that |q_t(k,a)/4096|<=1+1/1024 for EVERY label k and basis a,
including labels output from arbitrary malformed states.
Define the actual normalized rational score

D_t = (1/(4096m)) sum_{all m records i} b_i q_t(k_hat_i,a_i).

This sum is computed with bounded exact integer operations, not a real-arithmetic
oracle. Accept a candidate exactly when D_t>1/4. Enumerate t=0,...,N-1 in
fixed order, return the first accepted t, and return 0 if there is none.
There is no quantum search or additional source acquisition during enumeration.

On the intersection of (4) and correct labels for the clean positions, clean
rounding contributes at most 1/1024 in normalized absolute error. Any bad
records, however correlated or malicious, contribute at most
(h/m)(1+1/1024) in absolute value. Hence

D_s >= c/(2m)-1/16-1/1024-(h/m)(1+1/1024)
    >= 63/128-1/16-1/1024-(1/64)(1+1/1024)
     = 27071/65536 > 1/4,

D_t <= 1/16+1/1024+(1/64)(1+1/1024)
     = 5185/65536 < 1/4, for all t!=s.                        (6)

Thus exactly one candidate is accepted and it is s. This deterministic bound
handles ALL bad records and uses no independence or measurement-quality
assumption on them. If a false label or concentration event fails, the
algorithm may return any value but still respects all resource limits.

Total failure probability is at most 1/256+1/128=3/256, so for every N,s,
every fixed allowed corruption set and every allowed joint sigma_B,
unconditional full-secret success is at least 253/256, in particular >=2/3.
The stated weaker >=2/3 threshold is shared by every manifest claim.
It remains true for zero corruption, supplying the required original DCP result.

## 7. Implementable finite classical arithmetic, not a hidden oracle

For scoring, z=kt mod N is computed with schoolbook multiplication and long
division on at most 2n+O(1) bits. pi_* has a fixed integer numerator and
denominator D0=10^15. Every polynomial term can use a common positive
integer denominator (D0 N)^40 * 40!. It is divisible by the denominators
of both fixed-degree polynomials; all relevant numerator/denominator lengths
are O(n), with absolute factors from degree 40 and the fixed constants.

Exact signed summation and Euclidean division produce q_t. Each product or
long division of O(n)-bit integers uses O(n^2) bit operations by ordinary
schoolbook algorithms; the polynomial degree and number of terms are fixed.
No denominator is allowed to grow with the number of records: each q_t is
quantized separately before the sum. q_t has a constant-size signed range,
and the running sum needs O(log(m+2)) additional bits. Comparison with
4096m/4 is exact. The constants, factorials, common denominator and all
initialization are generated and charged, not treated as preloaded advice.

The phase grid has constant-size rational data. Empirical-mean denominators
are L, with O(log(L+2)) bits. Squared-distance comparisons and min selection
therefore use finite rational arithmetic of bounded bit length. Unwrapping
retains dyadic rationals with denominator at most 256*2^J and O(n) bits.
Every counter/loop bound/precision is fixed from N and n before source outcomes.
The algorithm contains no adaptive until-success loop or expected-time omission.

## 8. Joint charged resource bounds on every execution branch

Exactly Q=m=4096(n+4)<=20480n source copies are acquired; count every bad
copy and every inaccurate label. Hadamard-test repeats on a retained residue
state do not acquire copies, but their full gate/measurement work is counted.
Each acquisition costs n+1 work units, per the protected model.

m=O(n), J=O(n), ell=O(log(n+2)), and L=O(log(n+2)), with explicit large
absolute factors. Complete classical generation of all J+1 controlled modular
circuits, their offsets and gate lists is polynomial. Each modular circuit
has O(n^2) exact gates. Including integer-address representations, retaining
all J+1 lists costs O(n^3 log(n+2))=O(n^4) classical bits. Its generation,
counted bitwise, fits O(n^6) total work conservatively. It does not assume
an uncharged code-generation device or a supplied table of modular powers.

For the acquisition stage, there are exactly 2m(J+1)L Hadamard tests, each
using O(n^2) exact gates plus reset/preparation/measurement. Classical outcome
counts, grid scans, unwrapping and register resets are counted. After all
address and arithmetic bookkeeping their work fits O(n^8) conservatively.
The source cost m(n+1), generated constant grid, counters, measurement bits,
code storage and initialization are included. Final stored records use
O(m(n+2))=O(n^2) bits. Retaining every individual ancillary outcome is not
necessary; the algorithm stores only the two bounded counters during a phase.

Peak quantum registers consist of one acquired n+1-qubit system, a test
ancilla, a second n-bit permutation register and O(n^2) history/clean work
qubits for the EXACT reversible modular computation. These are reused and
uncomputed/reset between tests and copies. An O(n^4) peak-qubit ceiling is
therefore conservative, including all input, output and initialization
registers. No quantum state or history is accumulated over the m acquisitions.
Inaccessible future source storage is excluded exactly as specified in the
challenge, not counted as free accessible quantum memory.

All classical input, records, code lists, constant grid, counters, arbitrary-
precision operands and scratch buffers fit O(n^4) allocated bits. Fixed-degree
scoring needs only O(n)-bit arithmetic operands and a bounded number of them
at once, plus the O(n^2) stored records and counters. No table of N scores,
candidates or quantum labels is allocated. t is one O(n)-bit counter; its
score is computed and discarded before the next candidate.

Total allocated memory M=S_C+S_Q=O(n^4); thus each classically indexed access
and classically addressed gate pays O(log(n+2)) address-bit work, including
the absolute constant in M. All bounds here count this factor explicitly
within their conservative polynomial ceilings. Quantum-indexed memory access
is not performed, and there is no depth, locality or parallel-work shortcut.
Memory and code initialization, release/reset, every measurement and bitwise
operation are included in sequential work.

For each of at most N candidates, at most m=O(n) records are processed with
bounded-degree O(n)-bit arithmetic. Even with all address, loop-control and
memory costs this is bounded by O(n^8) work per candidate conservatively.
Adding the O(n^8) preparation/sample stage yields a uniform ceiling
T(N,s)=O(N n^12), hence T=O(2^n n^12). The spare powers cover all explicit
bookkeeping and finite-prefix cases; they are upper ceilings, not a measured
claim that these degrees are necessary. All loops remain within these bounds
on bad outcomes, correlated malformed samples and unsuccessful decoding.
All four resource statements refer to THIS one m,J,L,threshold and corruption
configuration, not a mixture of separate parameter choices.

## 9. Growth indices, structured bounds, and scientific comparison

Use the complete representative envelopes
B_T=2^n n^12, B_C=n^4, B_Q=n^4, B_samples=n.
For T, log_2 B_T=n+12 log_2 n and the protected
log_2(log_2(max(4,B_T)))/log_2 n tends to 1.
For the positive-degree polynomial envelopes, the numerator is
O(log log n), giving limit 0. All indices are exact nonnegative rationals.
An outer structured coefficient 1 is big-O normalization, not an invented
finite-size constant 1. The inner time coefficient 1 is explicit.
The exact sample count remains m in the statement; O(n) is its uniform
representative bound, not a measured sample count or an omitted failure cost.

The fifth expression is the FRACTION 1/64, not a malformed-count expression
or a per-copy corruption probability. The promised count is at most
floor((1/64)Q) for the actual fixed Q=m, under section 1's model. No score
is attached to that claim. This constant fraction belongs to the protected
fraction family and is established jointly with the resource and success
claims, not inferred from a sample upper bound.

Different error-model texts define incomparable robustness scopes on the
configured frontend. This model is not silently equated with a prior
clean-input-only claim. Likewise the full-time guarantee is exponential
and no better than known subexponential DCP methods. The purpose here is an
explicit full-secret and bounded-corruption resource theorem/participation,
not a declaration of frontier dominance or the stated research target.
No candidate code, verdict or accepted-source hash from another account is
used as mathematical evidence. All evidence for these claims is this file.


## Appendix: the elementary concentration and exact-gate facts used above

For clarity the concentration inequality's needed form can be proved directly.
If X is any random variable in [-1,1], set
K(lambda)=log E exp(lambda(X-E X)). Then K(0)=K'(0)=0 and
K''(lambda) is the variance of X under the exponentially tilted distribution.
That tilted variable still lies in [-1,1], so Var(X)<=E[X^2]<=1.
Integrating twice gives K(lambda)<=lambda^2/2 for all real lambda.
For independent X_1,...,X_k, product moment-generating functions and Markov
bound the upper tail of their centered sum at d>0 by
exp(-lambda d+k lambda^2/2). Taking lambda=d/k yields
exp(-d^2/(2k)); apply the same argument to -X for the lower tail.
This supplies both uses here: d=L/64 gives a single tail exp(-L/8192),
and d=m/16 for c clean variables gives exp(-m^2/(512c)).
It is the usual Hoeffding bound for interval length 2, with its constants
and applicability supplied rather than left to an external reference.

An exact constant Clifford+T Toffoli construction can also be seen directly.
For computational bits a,b,c, the integer phase identity modulo 8 is

4abc = a+b+c -(a xor b)-(a xor c)-(b xor c)+(a xor b xor c).

Apply T to a,b,c, compute the three pair parities and triple parity into
four zero ancillas using CNOT, apply T-dagger to each pair parity and T to
the triple parity, then reverse the parity computations. Its accumulated
phase is exp(i pi abc), exactly CCZ with every ancilla reset to zero.
H on the target before and after CCZ gives the exact Toffoli, without an
uncompensated relative phase. T-dagger is T^7 if only H,S,CNOT,T names
are primitive. Negative controls and controlled versions of these fixed-
size Boolean gates use X and a constant number of such Toffoli gates/clean
ancillas. This is a bounded exact Clifford+T implementation on arbitrary
states, not an approximate or postselected gate. Its constant costs and
ancillas are included in the polynomial bounds in section 8.
