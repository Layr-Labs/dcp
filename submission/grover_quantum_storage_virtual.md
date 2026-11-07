# Required virtual Dense P appendix

This file specifies ONLY the virtual Dense machine P used by
[the physical storage algorithm](grover_quantum_storage.md) and
[its complete simulator](grover_quantum_storage_transfer.md).
Every algorithm name, resource assertion, allocation statement, controller
assertion, work/space/source bound and physical-implementation description
in the source body below refers to P, its virtual classical memory and
its original quantum registers. None is a claim about this package's
physical classical allocation. P's full mathematical source, success,
guard, primitive, circuit, decoder and finite-case proofs are retained.
The new physical resource and simulation claims are established in the
physical main and transfer files. Every copied local proof filename is
rebound to this package's corresponding virtual appendix. Source provenance,
historical comments and exact source hashes retain their original meaning.
An old acceptance/review statement is provenance, not a proof premise.

## Complete virtual source body

# PSG2-DENSE-E: dense cyclic extraction with rational envelopes

## 0. Joint theorem, complete package and sources

For every integer N>=2 and secret s in Z/NZ, put n=ceil(log2 N), L=log2 n.
The single PSG2-DENSE-E algorithm below recovers the entire secret from
independent ideal copies with unconditional probability at least1-2^-8>2/3.
Its simultaneous bounds on EVERY branch, including all failed searches,
retries, rejected copies, wrong numerical labels, cutoffs and cleanup, are

    T=O(2^((177/250)sqrt(nL))),
    S_C=O(n^2) classical bits, S_Q=O(n) qubits,
    Q=O(2^((177/250)sqrt(nL)-(5/32)sqrt(n/L)
           -(1/2)(nL)^(1/4))).

All outside constants are absolute and independent of N,s and outcomes.
Displayed envelopes apply for n>=2. The unchanged finite branch handles
n=1, N=2 without division by L. Resource indices are [1/2,0,0,1/2].
The exact independent ideal-source model and epsilon(n)=0 are in Section 10.

This main and the required grover_quantum_storage_virtual_caps.md, grover_quantum_storage_virtual_oracle.md,
grover_quantum_storage_virtual_compiler.md, grover_quantum_storage_virtual_dense.md and grover_quantum_storage_virtual_bound.md
define one complete algorithm. Every claim requires all six proof files.
The dense appendix reproduces the complete instrument, probability,
product, frequency, guard and resource proof. The bound appendix contains
the entire rational-envelope proof, applied with kappa=5/32.

The algorithm uses k=b+5 only at positive widths, a 2048-string list,
128 trials per block and the exact eleven-rank-bit cyclic instrument.
Zero-width levels return one child. The sole acquisition guard is
Qcap_dense; Qcap_old sets EXTRACT precision and bounds the conceptual pool.
Wcap, q0,C and all decoder/pool parameters keep their exact old values,
with their new dense premises proved in the required dense appendix.
No comparison with the earlier Qcap_new is used or needed.

Mathematical main/cap references in the new copied oracle/compiler refer
to this configuration. Historical source filenames and hashes retain
their original meaning. Their auxiliary formulas do not override the
selected final envelopes (9.5)/(9.9). All actual gates, instruction bits,
source calls, memories, numerical precision and failed branches are counted.

Actual sources are the complete paired configuration, dense proof
b9404e273739276a67c5d48d699a2dd0a0d1c7abf7323714a3fb438857c209d9,
and rational proof 52beb2406a880e26bcbb34a910a40658a06044d44d082743b62faf283c11a3c8.
Their complete identities and the original local grouped/compiler history
are retained in the required appendices. The later public grouped source
is aa3ec389-f35c-4992-9b6f-e8b37f3359ac, commit
a43e8867eae10e718c329de529d3364a82519f59. The bound appendix distinguishes
its exact published compiler from the original local compiler bytes.
PSG14C was read before the earlier pair-transfer freeze; CYG1 was read
later and supplies the cyclic instrument here, with CYC1/PSG1 credits
retained. No CYC1 archive was directly read, no seven-moment theorem is
needed, and no verdict is a mathematical premise.

## 1. Charged implementation conventions

All arithmetic is on explicit bit strings. A w-bit add, comparison, copy or
increment has O(w) Boolean gates using ripple carry, with O(w) scratch.
Reversibly compute a Boolean circuit, copy out its answer, then reverse it;
a permutation can be computed into a fresh register, swapped, and erased by
its inverse. NOT, CNOT and Toffoli suffice, and Toffoli has an exact constant
Clifford+T decomposition. Wire counters, generation, initialization, resets,
measurements and classical reads/writes are counted. Every indexed action
also pays O(log(S_C+S_Q+2)) bit operations. Build the polynomial-size exact
G1 program once per positive-width attempt, after its weighted check.
Execute it with the literal physical-tape controller of the compiler
appendix. Each instruction bit, head step, gate and address debit is counted.
Other helper gates use the counted ready-address scans in that appendix.
No circuit description of exponential length is stored.

Only H, S, S-dagger and these exact reversible gates are used. In particular,
there is no arbitrary-N QFT circuit or approximate rotation to synthesize.
Fourier LABELS are inferred by nondestructive translation tests, with their
precision, tests and global error budget charged below. The source is used
only for fresh mixed copies; no purification, preparation inverse/control,
QRAM, hidden-shift oracle or subset-sum oracle is available or used.

Write N=2^a2 M with M odd, d=floor(log2 N), omega=exp(2 pi i/N),
s1=s mod M and s=s1+M s2 (mod N), 0<=s2<2^a2.

## 2. Source identities and exact transforms

Let chi_k = N^(-1/2) sum_u omega^(k u)|u> and phi_k(s) = (|0> + omega^(-k s)|1>)/sqrt 2.
Substituting |u> = N^(-1/2) sum_k omega^(-k u) chi_k into
rho_s = (1/N) sum_x |psi_x><psi_x|, with psi_x = (|0,x> + |1,x+s>)/sqrt 2, gives

    rho_s = (1/N) sum_(k=0)^(N-1) |phi_k(s)><phi_k(s)| (x) |chi_k><chi_k|,       (3.1)

because the cross terms k != k' carry (1/N) sum_x omega^(-(k-k')x) = 0.

Latent-label model. By (3.1) each copy is literally a convex mixture, with
uniform weights, of the product states phi_k(s) (x) chi_k. The whole algorithm
is a linear (adaptive) quantum instrument applied to independent copies. So
the joint law of all its classical outcomes equals the law obtained by first
drawing, for every copy, an independent uniform latent label k, and then
running on the product state phi_k(s) (x) chi_k. All probabilities below use
this model. Applying X to the control maps phi_k(s) to, up to a global phase,
the POSITIVE qubit pq_k(s) = (|0> + omega^(k s)|1>)/sqrt 2.

Two exact data transforms act on a fresh copy before label extraction. Each
is a permutation of all 2^n data encodings, extended by the identity on
encodings >= N. Each maps the copy exactly to rho_s' for a known transformed
secret s'. The latent-label model is then applied to rho_s' via (3.1), so the
latent label of a copy is the Fourier label of its TRANSFORMED data register,
which EXTRACT recovers.

(T1) Mult_alpha: u -> alpha u mod N, for a known alpha coprime to N. Since
x -> alpha x is a bijection of Z/NZ, the copy becomes exactly rho_(alpha s).
It is implemented with n controlled modular additions of the constants
alpha 2^v mod N into a clean register, a swap, and the inverse computation with
alpha^(-1): O(n^2) core steps and O(n) scratch.

(T2) Shift_c: if the control is |1>, replace u by u - c mod N, for a known c.
Since |1,x+s> becomes |1,x+(s-c)>, the copy becomes exactly rho_(s-c). This
takes O(n) core steps.

Modular addition of a known constant in [0,N) is a ripple comparison with N,
an addition, a comparison and a selector. It is the identity on encodings
>= N, uses O(n) Boolean gates, and is computed cleanly: compute, swap or XOR
the result out, then uncompute.

## 3. Finite-precision classical table and source-label extraction

For v in [0,4096) the controller computes rationals Cos[v], Sin[v] within 2^-20
of cos(2 pi v/4096) and sin(2 pi v/4096).

- Bound pi within 2^-90 using Machin's formula pi = 16 atan(1/5) - 4 atan(1/239),
  summing the first 40 terms of each alternating arctangent series. This gives
  two-sided bounds; the tails are below 16 (1/5)^81/81 + 4 (1/239)^81/81 < 2^-91.
- The identity follows from tan(2 atan(1/5)) = 5/12, tan(4 atan(1/5)) = 120/119
  and tangent subtraction.
- At the angle 2 v p_mid/4096 < 7, where p_mid is the midpoint of the pi bounds,
  sum 80 Taylor terms. The remainder is <= 7^81/81! < 2^-170. The angle error
  is < 2^-89, and sin and cos are 1-Lipschitz.
- Round each value to denominator 2^20.

This is a fixed finite rational computation, charged once as an absolute
constant (not advice).

For x in [0,1) put tab_0(x) = Cos[floor(4096x)] and tab_1(x) = Sin[floor(4096x)],
and let cs_0(x) = cos(2 pi x), cs_1(x) = sin(2 pi x). Since cs is 2pi-Lipschitz,

    |tab_beta(x) - cs_beta(x)| <= 2 pi/4096 + 2^-20 < 1/625.                    (4.1)


### Exact collective extraction EXTRACT

Input: a data register holding chi_k beside arbitrary spectators. Set

    J_e=n+4, h_ext=ceil(log2(2^16 Qcap_old(n+5))), F(h_ext)=2^21 h_ext.

Here Qcap_old is the auxiliary precision budget of Section 8. Each call executes the
fixed procedure RUN(F(h_ext)) once, outputs its integer label, and resets
the data and test registers. No rejection or fallback is used.

Translation Tr_c: u -> u + c mod N satisfies Tr_c chi_k = omega^(-k c) chi_k.
A TEST WITH SHIFT c (0 <= c < N) works as follows. Prepare an ancilla in |+>.
Apply Tr_((N - c) mod N) controlled by it, so the |1> branch gets eigenvalue
omega^(k c). Measure the ancilla in X (H then Z) or in Y (S^dagger, H, then Z).
The +-1 outcome has mean cos(2 pi c k/N) or sin(2 pi c k/N). Conditioned on
k, chi_k and every spectator are unchanged and outcomes are independent. A test
at LEVEL j is the test with shift 2^j mod N. Each test costs one controlled
modular addition, O(n) core steps.

A ROUND (in basis X or Y) is one test at every level j = 0..J_e at once, built as
follows. Prepare ancillas r_0..r_(J_e) in |+> and read them as the integer
x = sum_j r_j 2^j < 2^(J_e+1) = 2^(n+5). Since N > 2^(n-1), x < 64 N.
- Copy x into a zeroed (n+5)-qubit scratch z with CNOTs. For i = 5 down to 0:
  compute the bit a_i = [z >= N 2^i] into a fresh qubit by a comparator with a
  classical constant, and controlled on a_i subtract N 2^i from z. Before step i,
  z < N 2^(i+1), so afterwards z < N 2^i; at the end z = x mod N. Each step is
  O(n) NOT/CNOT/Toffoli gates with O(n) reusable carry qubits.
- Subtract z from the data register modulo N (u -> u - z mod N on u in [0, N),
  a standard O(n) register subtraction with a borrow-controlled add-back of N
  and a comparator to clean the borrow flag).
- Undo the reduction step by step and the copy, returning z, the a_i and all
  carries to |0> exactly.
The net map is |x>|u> -> |x>|u - x mod N> on basis states, which equals the
product over j of Tr_((N - 2^j) mod N) controlled by r_j, because translations
compose additively. Since Tr_(-x) chi_k = omega^(k x) chi_k and
omega^(k x) = prod_j (omega^(k 2^j))^(r_j), the ancillas end in the product state
tensor_j (|0> + omega^(k 2^j)|1>)/sqrt 2 with chi_k and every spectator unchanged.
Measuring every r_j in the round's basis therefore gives, conditioned on k,
independent outcomes with exactly the law of separate tests at levels
j = 0..J_e. A round costs O(n) core steps and n+5 ancillas plus O(n) scratch,
all reset afterwards, so the quantum space stays O(n).

### 3.1 RUN(F): level-wise extraction

Use the complete RUN(F) algorithm and proof in Part C of the required
compiler appendix. That section specifies every test, direction score,
dyadic unwrap, final rounding, reset, cost and concentration bound; it is
part of this algorithm. RUN(F(h_ext)) uses 2F(h_ext) collective rounds.
For each latent label and earlier history its wrong-label probability is
at most4(n+5)e^(-h_ext). Its core work is O(n^2), quantum scratch O(n),
and classical scratch O(n log n). Over Qcap_dense<=Qcap_old calls, the
first label error has probability at most2^-14. The actual/ideal coupling
there stops at the first label error and does not condition fresh labels
on successful extraction.

## 4. Work-balanced profile and bounded-search combiner

Main-branch parameters are computed once for n>=256. For a positive integer v,

 delta(v)=ceil(log2(3(2v+1)))+1
         =bit_length(3(2v+1)-1)+1.

Starting at a positive trial R put u=floor(sqrt R). Descend by
v<-v-delta(v), retaining only values v>=u and stopping as soon as the
next value is below u. Reverse the retained values to obtain
v_1,...,v_mstar=R, with sum S_u(R). For i>=2 the usual decrement relates
v_i and v_(i-1), while the base v_1 directly combines fresh leaves.
Choose the least positive R with 2S_u(R)>=n. Search sequentially; no
monotonicity is assumed. It terminates by R<=ceil(n/2), since2S_u(R)>=2R.
Generate profiles and counters with counted polynomial-time integer
arithmetic. Put

    q0=(2u+1)*2^(R-u).

A PS_TREE_D call,1<=D<=n, has independent ideal leaves with uniform known
labels in[0,2^D). Put B=D-1. When B=0 return one leaf. Otherwise allocate
actual widths b_mstar,...,b_1 greedily from the root down, b_i=min(2v_i,
B-already_allocated). Then sum_i b_i=B. Let r_i=b_i+5 for b_i>0 and r_i=1 otherwise; put
p_i=sum_(j<i)b_j. Level0 returns a leaf. A zero-width level just returns
its child. For b_i>0, recursively build r_i fresh child outputs, then check
and add weight2^v_i to the global weighted-attempt counter before executing
the combiner below. If that would exceed Wcap, abort. On FAIL discard ALL
inputs and query scratch, and build fresh children before trying again.
No output label, including zero, is rejected inside the tree merely because
of its higher bits or value.

### 4.1 Exact preparation and cyclic verified-list output

At a positive width, k=b+5 child phase qubits have full signed labels
a_j divisible by2^p. Their original register is

    2^(-k/2) sum_x exp(2pi i theta A(x))|x>, A(x)=sum_j a_j x_j.

Set c_j=(a_j/2^p) mod2^b. Initialize the separate k-bit query z and
b-bit accumulator to zero. Apply k CNOTs x->z, run the fixed-query G1
word, then the same k CNOTs to clear z before measuring/resetting the
accumulator to obtain e. All 2k indexed gates are charged. The exact
map is |x>|0>_z|f(x)> with clean helpers, including with references.

Hold the original phase index untouched during discovery. Sort the at
most2048 distinct verified strings by original binary index, never by
full labels. Use exactly the complete instrument in dense Section 3:
if h<2 fail; otherwise measure membership in the verified list, XOR its
canonical rank into eleven zero bits, prepare output c in |+>, apply
(q,c)->((q-c) mod h,c) for q<h and identity otherwise, and measure the
changed rank t. No unchanged rank copy remains. Clear the original index
using x_t and x_next, next=(t+1)mod h, then reset rank/helpers and return c.
The full signed label is A(x_next)-A(x_t), computed only after selection.
Its nonzero incidence and divisibility by2^(p+b) are proved there.

Dense Section 3 gives the complete exact gate implementation of the rank
permutation on all4096 encodings, its Kraus maps and their Gram sum.
It proves membership success h/|F_e| and the exact phase for every verified
incomplete list and reference system. Numerical zero output labels are
not filtered. All selection kernels use only low residues and known
indices, with equal basis magnitudes and no unknown-phase dependence.
This cyclic instrument is the selected postprocessing; adjacent disjoint
pairing is not used.

### 4.2 Bounded discovery, grouped sum and literal execution

Set Hcap=2048. If k<13 enumerate all2^k<=4096 indices and retain the
first Hcap solutions. Otherwise use at most Hcap blocks, each with at
most128 trials, stopping that block at its first new verified solution.
Stop discovery at an empty block or Hcap found solutions. The list has
no duplicate or false member. Each trial draws uniform
j in[0,J0), J0=2^ceil(k/2), prepares a fresh uniform k-bit query, applies
j exact membership Grover iterations, measures, verifies and resets it.
The original phase index is not touched by these queries.

The selected sum is G1 in grover_quantum_storage_virtual_oracle.md, with explicit k=b+5
query wires and b output bits. It sends |z>|A>|0> to
|z>|A+sum_j c_j z_j mod2^b>|0> exactly for every z,A. At k<max(16,u)
use direct controlled additions; other rows use the full group tables,
selected count records, retained-input/history binary sum and complete
batch reverse in that appendix. Its widened allocation covers k<=n+4,
h_count=1, partial groups/batches and all modular high bits. All G1 work
is clean and O(n) qubits; its exact slot count is O(n log2(L+2)).

After the weighted check, read the actual k by b low residue bits from
the signed child labels with counted indexed accesses. The explicit
oracle constructor materializes every mask, heap/wire map, instruction
and marker in O(nL^4) charged polynomial work and O(n^2) classical space.
Build only G1 once per attempt; its c_j and actual wire map stay fixed.
Use the initial wrapper of Section 4.1 and dense Section 3.

Each membership reflection runs G1 forward from a zero accumulator,
compares with e, excludes all at most2048 found strings, applies Z on its
clean flag, then reverses the tests and G1. Diffusion is the exact H
passes and clean forward/reverse Toffoli chain. The new compiler Part B
reads every stored tag/operand bit, counts all physical head movement
and reverse steps, and pays each indexed gate's full address debit.
Both G1 passes cost O(nL log2(L+2)). Part A counts every complete list,
comparison, verification, diffusion and control scan. The 2048 tests
change constants only. Every arithmetic gate remains exact Clifford+T.

The iteration word has ceil(k/2)<=v+3 bits, so J0<=8*2^v. At most
2048*128=2^18 trials occur. Every fair bit, counter update, stop test,
query initialization, measurement, verification and reset is charged.
Dense Sections 10--11 and compiler Part B include all these words.
The rank-permutation construction, list sorting, membership/rank scans,
cyclic index clearing and one-pass full signed output are paid one-off
polynomial work. Signed output uses coefficients x_next,j-x_t,j and the
field n+ceil(log2 q0)+4, whose unchanged safety is proved in dense Section 7.

With n<2(u+1)^4 and v>=u, the paid one-off polynomials fit O(2^v).
Thus a complete paid attempt, including failed/partial paths, costs

    O(nL log2(L+2)2^v).                              (4.2)

Only one attempt/program is active. It releases its state before building
fresh children on failure. A weighted failure starts no program; source
failure in child construction keeps the full partial-stack charge.
All resets, erasure and abort cleanup are counted. Quantum work remains
O(n); all labels, programs, maps and 2048 strings fit O(n^2) classical bits.

### 4.3 Exact dense success

Dense Sections 4--5 contain the complete planted-law first/second-moment
and fixed-fiber Grover proof. With k=b+5 they prove complete cyclic
survival >=63/65, fiber tail <1/4094 and discovery miss <2^-37. Hence,
before generating each fresh attempt's children,

    Pr[success]>=63/65-1/4094-2^-37>24/25.             (4.1)

This is averaged over fresh independent uniform low residues and query
coins, not a fixed-child-list assertion. The same full proof covers
small enumerated widths. Successful cyclic outputs have the exact phase,
including incomplete lists. The joint induction below supplies the fresh
uniform law and termination without conditioning on extraction or caps.

## 5. Unused blocks, termination and the root frequency

Lemma U (joint induction). In the ideal uncapped process, every tree-level
call terminates almost surely. If it cancels p bits, its returned label
x/2^p mod2^(D-p) is uniform, conditional on any external past before the
fresh call. Distinct fresh child calls give independent such quotients.

Proof. The leaf statement is the exact uniform latent-label source law.
Assume the statement at the lower level. Before a new node attempt starts,
its freshly generated children have independent uniform quotients modulo
2^(D-p). Their residues c_j modulo the next2^b are thus independent uniform.
Equation(4.1) gives conditional success at least24/25 before child generation,
whatever the earlier external past. Every failure releases its inputs and
restarts with fresh children. The geometric bound proves almost-sure
termination and finite expected attempts at this level.

It remains to prove the output law that closes the induction. Fix any
finite successful selection transcript through this level, containing all
used leaf values modulo2^(p+b), search choices/outcomes, residue, membership and changed-rank
measurements, and retry choices. Its probability kernel is a function ONLY
of those low parts, by4.1 and4.2; quantum searches used separate registers.
Write each original leaf as k_l=u_l+2^(p+b)H_l, with H_l independent uniform
in Z/2^(D-p-b). The selected output has a symbolic signed incidence vector
z_l in{-1,0,1}, not allzero, determined by the low transcript. Consequently

 x/2^(p+b) mod2^(D-p-b)=c+sum_l z_l H_l mod2^(D-p-b).

Here c is an integer determined by the low parts. At least one z_l is a
unit +1 or-1, so the sum is uniform on that cyclic group. Marginalizing over
all finite successful low transcripts proves the output law. Fresh disjoint
leaf sets give the conditional independence for successive child calls.
This conditioning excludes internal EXTRACT records and stored high
labels: the ideal process marginalizes them and uses exact latent labels.
Extraction errors enter by additive coupling, not conditioning on correct
extraction. Storing full labels does not change the law: decisions use
only low residues and do not filter high output values. QED.

For the unchanged nominal rbar_i=2v_i+1, the profile still gives
3rbar_i<=2^(delta(v_i)-1) above the base. These are nominal bounds,
not the dense arities. Dense Sections 6--8 prove the uniform product
ratio <32, the old q0 frequency bound and the new source/weight recurrences.
In particular every returned tree has actual distinct-leaf count
q_D_dense=product_i r_i<=q0 for every D, including partial and zero widths.
Its full signed root is2^B W with |W|<2q0. All intermediate signed sums
fit n+ceil(log2 q0)+4 bits by the one-pass signed-leaf bound proved there.
No incidence vector is stored. The accepted leaf law and the low-bit
proof above are unchanged at the new base with b+5 independent children.

For the root, retain the stronger full-frequency argument as well as Lemma U.
Write each accepted leaf label k_l=u_l+2^B tau_l, with independent fair bits
tau_l. Condition on all low u_l, residue/search/membership/rank outcomes and retry
choices, and independent previous roots. All these kernels use bits below
B and are phase-independent, so the tau_l of the returned root remain iid
fair. Its nonzero incidence vector gives

 W=c+sum_(l in S+)tau_l-sum_(l in S-)tau_l, |S+|+|S-|>=1.

Lemma5.1. For every real y, conditional on that low transcript,

 |E exp(2pi i yW)|<=|cos(pi y)|,                            (5.2)
 Pr[W odd]=1/2.                                           (5.3)

Each independent fair bit contributes absolute factor|cos(pi y)|; at least
one is present. The integer c is low-transcript measurable. With y=1/2 the
parity is fair. This bounds the full signed W's characteristic function; it does not
assert a uniform integer distribution.

## 6. Odd-part source and the strided backward decoder

If M=1 set s1=0 and skip this section. Otherwise M>=3, D=d, B=d-1>=a2,
ell=ceil(log2 q0), with q0 from Section 4. Write theta=s1/M. For ANY nonnegative physical
scale j, compute the CRT unit alpha_j by

    alpha_j=1 mod2^a2,
    alpha_j=2^j*(2^(d-1-a2))^-1 mod M.

Acquire a fresh original copy, apply Mult_alpha_j, extract k with EXTRACT, reject
k>=2^d, and on acceptance apply X to the first qubit. In the ideal reference,
accepted labels are iid uniform in[0,2^d), with original acquisition acceptance
2^d/N>1/2. The retained phase is k*alpha_j*s/N. A PS_TREE_d root is consequently
(|0>+exp(2pi i W 2^j theta)|1>)/sqrt2, because
2^(d-1-a2)*alpha_j=2^j modulo M and s=s1 modulo M. This uses the original modulus. CRT units exist at every scale used below.

Section 5 proves that each root has |W|<2q0 and a nonzero signed
incidence vector over distinct accepted leaves. Construction kernels use
only bits below B; roots use disjoint fresh leaf sets. Conditional on the
low construction data, W=c+sum epsilon_l tau_l with independent fair top
bits and coefficients in {-1,1}. The one-bit fallback below uses only the
resulting parity law. Sections 6.3--6.6 use a finite low-bit distance event
to prove a larger support. Internal EXTRACT records are marginalized in
the ideal process. Section 8 compares this process with the actual run.

### 6.1 Exact two-candidate backward lemma

Write ||x|| for circular distance to 0. Suppose a known dyadic center
z in [0,1) satisfies

    ||2x - z|| <= e,             e <= 1/(64q0).

The inverse images of z under doubling are

    u_0 = z/2,                  u_1 = (z+1)/2.

Exactly one of them, denoted u_*, lies within e/2 of x; the other is 1/2
away from u_*. This circular statement includes zero, wraparound, and binary boundaries.

Produce k fresh roots with phase W_i x. For each independently choose
beta_i uniformly from {0,1}, measure X or Y respectively, and record
Z_i in {+1,-1}. Use the source's constant-size trigonometric table:

    score(b) = sum_i Z_i tab_beta_i(W_i u_b mod 1).

The table error is uniformly less than 1/625. Output the smaller index
maximizing score, making the algorithm total even on failure branches.

**Lemma.** Conditional on the incoming center satisfying the displayed
accuracy hypothesis, the wrong candidate is chosen with probability at
most exp(-k/512). No stronger root law is needed.

Proof. Let delta = x-u_* be the circular representative with
|delta| <= e/2. Define the exact score difference for one root by

    X_i = Z_i [cs_beta_i(W_i u_*) - cs_beta_i(W_i u_other)],
    cs_0(t)=cos(2 pi t),          cs_1(t)=sin(2 pi t).

Averaging over the fresh basis coin and root outcome, conditional on W_i,
gives

    E[X_i | W_i,past]
      = (cos(2 pi W_i delta)
         - cos(2 pi W_i(delta +/- 1/2)))/2
      = 1_{W_i odd} cos(2 pi W_i delta).

The sign in +/- 1/2 does not matter for integer W_i. Pointwise,

    |2 pi W_i delta| < pi/32.

By the conditional parity law, E[X_i | past] >= mu = cos(pi/32)/2.
In particular, the useful cosine need not be independent of parity.
It is bounded below for EVERY W in the prescribed support.

Each |X_i| <= 2, so the martingale increments
X_i-E[X_i|past] have absolute value at most 4. The computed score difference
differs from sum_i X_i by at most 2k/625. Since

    mu - 2/625 > 1/4,

Azuma gives

    Pr[computed true-minus-false score <= 0]
       <= exp(-(k/4)^2/(2*16*k)) = exp(-k/512).

For an entirely rational numerical margin, pi < 22/7 and
cos(v) >= 1-v^2/2 imply

    (1-(22/7)^2/(2*32^2))/2 - 2/625 - 1/4
       = 7664023/31360000 > 0.

Conditioning precedes the new root or uses only its low transcript. QED.

If the correct lift is selected, its error is e/2. Thus accuracy improves
as decoding proceeds backward. It does not degrade by q0 per step.

### 6.2 One-bit fallback: terminal seed and backward decoder

Assume n >= 256 and M >= 3. Set exactly

    H = ceil(log2 M),
    J_seed = ell+3,
    nu = ceil(log2(n+ell+4)),
    K_seed = 8192(ell+nu+30),
    K_back = 512(nu+30).

#### 6.2.1 Seed at scale H

Apply the explicit localization algorithm below to the phase

    phi = 2^H theta mod 1

for local stages u = 0,1,...,J_seed. Local stage u obtains roots at physical
scale H+u, using the same PS_TREE_d and K_seed roots. At every local stage, measure its K_seed roots in independent fair X/Y
bases and record (W_i,beta_i,Z_i). On its dyadic candidate grid compute
score(c)=sum_i Z_i tab_beta_i(((2^u W_i c) mod2^P_u)/2^P_u), with the
Section 3 table. Stream candidates and return the least maximizing one.
At stage u, the
dyadic denominator is 2^(P_u), where P_u = u+ell+8.
Stage 0 enumerates the whole grid. Each later stage enumerates the grid
points in the closed circular arc of radius 2^-(u+2) around the previous
center. The arc endpoints are grid points, so nearest-point guarantees
hold even at boundaries.

For completeness, the source proof of this localization uses only the
contract above. A nearest candidate zeta_0 obeys

    |2^u W (phi-zeta_0)| <= 2^-8.

A far candidate, at distance at least 2^-(u+3), has
2^u ||phi-zeta|| in [1/8,1/2] inside the incoming arc. Thus its expected
per-root score is at most cos(pi/8)/2, while the near candidate has score
at least cos(pi/128)/2. Martingale concentration at deviation K_seed/64,
table error K_seed/625, and the at most 2^(ell+9) near/far events imply
failure at most 2^-20/(n+ell+4) per stage. The strict score margin can be checked
without floating point using pi > 3, pi < 22/7, and the alternating
cosine bounds:

    [9/128 - (22/7)^2/(2*128^2)
       - (22/7)^4/(24*8^4)]/2 - 2/64 - 2/625
      = 4372721/73758720000 > 0.

At the last seed stage, obtain z_H satisfying, except on seed failure,

    ||phi-z_H|| <= e_H = 2^-(ell+6) <= 1/(64q0).

There are ell+4 seed stages. In the concentration bound use the present
nu=ceil(log2(n+ell+4)). The failure per seed stage is at most
2^-20/(n+ell+4). Thus the total seed failure is at most 2^-20 for every
n>=256, without a bound on the number of profile levels. No bound
ell+4<=n is needed.

The seed's exact denominator is 2^(2ell+11). The seed localizes a real circular phase; it does not assume phi is dyadic.

#### 6.2.2 Backward steps

For j = H-1,H-2,...,0:

1. Form the exact dyadic candidates z_(j+1)/2 and (z_(j+1)+1)/2.
2. Acquire K_back fresh PS_TREE_d roots at physical scale j.
3. Apply the two-candidate scoring rule of Section 6.1 and set z_j to its
   deterministic maximizer.

If all preceding choices were correct, the true phase x_j = 2^j theta
has distance at most e_H/2^(H-j) from z_j. Every such incoming radius is
small enough for the lemma. Since exp(-K_back/512) <= 2^-30/n and H <= n,
the conditional error union bound is at most 2^-30.

The union bound uses first-error events and fresh independent roots,
including after adaptive decisions.

#### 6.2.3 Exact rounding and boundary digits

The output center z_0 has denominator 2^(H+2ell+11), and

    ||theta-z_0|| <= 2^-(H+ell+6) <= 1/(64 q0 M) < 1/(2M).

Return

    s1 = floor(M z_0 + 1/2) mod M.

It equals s mod M on the good event. Strict distance excludes a tie.
Reduction modulo M handles wraparound, including theta=0 and z_0 near 1.
The circular argument also handles every binary boundary.

No repeated numerical phase truncation is used. Each lift is an exact
integer numerator over a power-of-two denominator. Each backwards step
adds one denominator bit. The only approximation in the scores is the
source's fixed trigonometric table, already budgeted in both lemmas.

#### 6.2.4 The fallback root budget

The one-bit fallback root count is the deterministic integer

    F_old = (ell+4) K_seed + H K_back.

The profile estimate in Section 9 gives ell=O(R) and R^2=O(nL).
Thus F_old=O(ell^2+ell log n+n log n)=O(nL).
Each backward step has two candidates. Initialization streams at most
2^(ell+8) <= 512q0 candidates per stage, keeping a maximum and root records.

Section 9's profile bound proves ell^2=O(nL).

### 6.3 Exact pool parameters and the finite fallback

Assume n>=256 and M>1. Put q=q0 and define the exact uniform
expected original-copy bound per root by

    C=C_old=6(2u+1)2^(R-u-mstar+1).

Use mstar from Section 4, and set

    ell=ceil(log2 q), U=n+ell+40,
    A=2^40 (C+1) U^3,
    g=ceil(log2(2A)), h=floor(B/(8g)).

All these are explicit integers with polynomial bit length. If h<16,
use Sections 6.1--6.2 and set F=F_old. The new asymptotic bounds
still hold on this fallback: Section 9 proves ell=O(sqrt(nL)) and
log2 C=O(sqrt(nL)), so h tends to infinity uniformly in N and s.
Thus only finitely many bit lengths use this executable fallback; their
resource maximum changes an outside constant. M=1 uses no odd decoder or pool.

For h>=16 put

    Delta=floor(floor(log2 h)/2)-1,
    H=ceil(log2 M), nu=ceil(log2(n+ell+4)),
    Kseed=8192(ell+nu+30),
    Kback=8192(Delta+nu+30),
    Sseed=ceil((ell+3)/Delta), Sback=ceil(H/Delta),
    F=Sseed Kseed+Sback Kback.

Then Delta>=1 and 2^(Delta+3)<=4sqrt h. Sections 6.5--6.6 use exactly
these F roots. For a pure 2-power set F=0 without computing odd parameters.

Use the exact source budget

    Qstar_old=C(F+2n)+2n, Qcap_old=1024 Qstar_old,
    beta_m=min(1,32*25^mstar/72^mstar),
    Qstar_dense=beta_m*C*(F+2n)+2n,
    Qcap_dense=ceil(1024 Qstar_dense).

Also use

    Wstar=6*2^R(F+2n), Wcap=1024 Wstar.

Keep the existing before-action cap checks. Keep K2=ceil(log2 n)+30
attempts at each 2-adic bit and the existing direct width-one case.
A root's source cost and outcome need not be independent. The uniform
fresh-attempt arguments of Sections 5 and 8 give expected total sources
<=Qstar_dense and expected total weight <=Wstar, by the required appendix.
Use Qcap_dense before every acquisition. Keep Qcap_old for EXTRACT
precision and pool analysis. Each operational cap costs at most 2^-10 failure by Markov.

The analysis pool really contains the capped run. Since Delta>=1,
Sseed<=ell+3 and Sback<=n. Also Kseed,Kback<=2^15 U. Consequently

    F<=2^15 U^2,
    Qcap_dense<=Qcap_old<=2^27(C+1)U^2<=A.

Thus A contains the capped run without an asymptotic root estimate.

### 6.4 The accepted pool and conditional top bits

In the ideal latent-label process, every transformed Fourier label is
independent uniform in [0,N). For an accepted y<2^d, waiting count t,
and specified rejected labels z_1,...,z_(t-1)>=2^d,

    Pr[T=t, rejected labels=z, accepted label=y]=N^(-t).

This is the probability of the waiting/rejection record times 1/2^d.
Thus the accepted label is uniform in [0,2^d), independent of this full
record. This also holds when t=1. Each source unit transform preserves
the uniform latent-label law.

Give each root in the fixed odd schedule an independent infinite fresh
array of these labels. A construction retry or the return of a root
uses a stopped prefix whose stopping rule depends only on low labels,
independent search coins, and low-dependent measurement kernels. A
change to the next array is therefore independent of unused accepted
top bits. Concatenate the used prefixes, then extend with independent
unused coordinates. The result is an infinite independent uniform pool.
Physical scales and root counts are fixed by N, not by decoder centers.
No high-label or decoder outcome controls the prefix lengths.

Let E be the low-bit event that no signed sum on fewer than h distinct
coordinates among the first A low labels vanishes modulo 2^B. A fixed
nonempty signed sum is uniform modulo 2^B: expose all but one coordinate,
whose coefficient is a unit. Thus

    Pr[E fails] <= 2^-B sum_(t=1)^(h-1) binom(A,t)2^t
                <= h(2A)^h 2^-B
                <= 2^(-3B/4).

For the last inequality, h g<=B/8 and log2 h<=log2 B<=B/8 for B>=64.
Here B>=n-2>=254. The bound is therefore less than 2^-190.

Let Llow be defined in the ideal latent-label process. Include all low
pool coordinates, waiting counts and rejected latent labels, and all
construction/search/residue/membership/rank outcomes in the fixed odd-root schedule.
Marginalize the extractor's internal records; they are not in Llow and
do not control this ideal process. Do not include decoder outcomes,
X/Y basis coins, or accepted top bits. The joint probability kernels
for construction depend only on low data. Conditional on Llow, the accepted tau_v remain independent
fair bits, and every root uses a fixed disjoint subset of them. This
statement follows by induction over finite fresh attempts and then by
almost-sure termination; it does not condition label extraction on
success. Extraction errors are treated by an additive coupling later.

Let Fitodd say that the complete ideal odd schedule fits its source cap
and its weight cap. This event is Llow-measurable. On E and
Fitodd, every root's nonzero support has at least h coordinates: its
full signed label is divisible by 2^B, so a smaller support would give
a forbidden signed low relation. In particular, for every real x,

    |E[exp(2 pi i x W) | Llow]| <= |cos(pi x)|^h.       (6.3)

Earlier decoder outcomes only reveal top bits of disjoint earlier root
sets. Hence (6.3) remains valid with those outcomes exposed. This is the
fresh-root conditioning needed below. We never condition on the full
source cap event of the later adaptive 2-adic procedure.

### 6.5 The strided terminal seed

The unknown terminal phase is phi=2^H theta mod1. There are exactly
Sseed stages. Stage t=0,...,Sseed-1 sets j=t Delta and acquires Kseed
roots at physical scale H+j. Measure each in an independent fair X/Y
basis; store (W_i,beta_i,Z_i), Z_i in {+1,-1}.

Use grid denominator exponent P_j=j+ell+8. Stage zero uses the whole
grid c/2^P_j. Later stages use all grid points in the closed circular
arc of radius 2^-(j+3) about the preceding center. Its endpoints are
grid points: the previous denominator divides 2^P_j and P_j>=j+3.
Thus the candidate set has at most 2^(ell+8)<=512q elements, and a
nearest candidate is within 2^-(P_j+1) of phi whenever the incoming
accuracy condition holds. Stream the grid in one or two integer
intervals. Do not store the candidate list.

Score a candidate zeta by

    score(zeta)=sum_i Z_i tab_beta_i(2^j W_i zeta mod1),

with the existing fixed rational sine/cosine table, uniform error less
than 1/625. Choose the least maximizing grid index, also on bad events.
The ideal exact per-root score xi has expectation

    E[xi | W_i,past]=(1/2)cos(2 pi 2^j W_i(phi-zeta)).

For the nearest point, |2^j W_i(phi-zeta)|<2^-8, so its conditional
mean is at least cos(pi/128)/2>499/1000.

A far candidate has circular distance at least 2^-(j+Delta+3) from phi.
At stage zero the distance is at most 1/2. At later stages both points
lie in the incoming arc, so their distance is at most 2^-(j+2).
Therefore x=2^j(phi-zeta), with its relevant signed representative,
has 2^-(Delta+3)<=|x|<=1/2. Since sin(pi|x|)>=2|x|,

    |cos(pi x)|^h <= exp(-2h x^2)<=exp(-1/8).

By (6.3), a far candidate's expected exact score is at most
exp(-1/8)/2<=4/9. For each fixed candidate, the exact score lies in [-1,1]. Its
conditional range has length two. The conditional exponential-moment
bound for a centered variable in a range of length two is exp(t^2/2).
Applying it in sequence and optimizing t gives a one-sided deviation
Kseed/64 bound exp(-Kseed/8192). The score
comparison is strict, since

    499/1000-4/9 > 2/64+2/625.

There are at most 2^(ell+9) near/far events. Their union probability
is at most 2^-20/(n+ell+4), by the exact Kseed and nu above. Hence the
output center has error less than 2^-(j+Delta+3), which is exactly the
next incoming radius. This argument is conditional on any Llow in
E and Fitodd and on earlier stages. It includes adaptive centers.

At the final stage obtain z_H with

    ||2^H theta-z_H|| <= e=2^-(Sseed Delta+3)
                         <=2^-(ell+6)<=1/(64q).

The seed's largest local physical scale is (Sseed-1)Delta<ell+3.
Its final denominator exponent is (Sseed-1)Delta+ell+8<2ell+11.

### 6.6 A backward block of up to Delta bits

Suppose a dyadic z approximates 2^j theta with circular error e_j<=e.
Take r=min(Delta,j), set j'=j-r, and form all 2^r exact lifts

    u_a=(z+a)/2^r, 0<=a<2^r.

Exactly one lift ustar has circular distance at most e_j/2^r from
x=2^j' theta. Acquire Kback fresh roots at physical scale j'. Score
these lifts with sum_i Z_i tab_beta_i(W_i u_a mod1) and choose the
least maximizing a. Repeat until j=0. This uses exactly Sback blocks.
The physical scale sequence and root counts are fixed by N, not scores.

For the correct lift delta=x-ustar, every |W delta|<1/64, because
|W|<2q, e_j<=1/(64q), and r>=1. Its expected exact per-root score is
at least cos(pi/32)/2>49/100. For any other lift, the circular distance
from x is at least

    (1-e_j)/2^r >= 1/2^(r+1) >= 1/sqrt h.

The last bound follows from 2^Delta<=sqrt h/2. Its distance is also at
most 1/2. Thus (6.3) bounds its expected score by exp(-1/8)/2<=4/9.
This looser exponent is sufficient and avoids a dependence on r.

The same concentration calculation has at most 2^(Delta+1) events.
Kback gives error at most 2^-20/(n+ell+4) per block. The margin is
strict since

    49/100-4/9 > 2/64+2/625.

On a correct choice, the new error is exactly bounded by e_j/2^r.
Lifts preserve exact denominator bits. After all
blocks, ||theta-z_0||<=e/2^H<1/(2M). Return

    floor(M z_0+1/2) mod M.

This returns s mod M, including wraparound and binary-boundary cases.

There are at most ell+3+n<n+ell+4 seed stages and backward blocks.
A union bound over first incorrect stages gives total decoder failure
<=2^-20 conditional on every Llow in E and Fitodd. Section 8 integrates
this bound and adds the unconditional cap, extraction, distance-event,
and 2-adic attempt errors. No support test is made. All copies and failed work are charged.

### 6.7 Exact roots, grid work, and memory

The exact count is

    F=ceil((ell+3)/Delta)*8192(ell+nu+30)
       +ceil(H/Delta)*8192(Delta+nu+30).               (6.4)

Section 9 proves ell=O(sqrt(nL)), log2 C=O(sqrt(nL)), and
ell^2=O(nL). Thus log2 A=O(sqrt(nL)), h=Omega(sqrt(n/L)), and

    Delta=Omega(L), Delta=O(L), nu=O(L).

These estimates concern only odd trees with B>=n-2. They are uniform
in M and s. Formula (6.4) consequently gives

    F=O(ell^2/L+ell+n)=O(n).                           (6.5)

M=1 has F=0. For small M, H is smaller, and the same bound applies.
The exact source cap still contains 2n to cover the 2-adic part; that
part does not require a log n stride.

Seed work. There are at most 512q grid candidates per stage and
Kseed records. Initialize exact residues at each interval's first
candidate by schoolbook multiplication. Then update each residue with
one O(n)-bit addition per candidate. All exponents, signed frequency
fields, scales, and dyadic numerators have O(n) bits. The logical work is

    O(n q Sseed Kseed)+poly(n)
       =O(n q(ell^2/L+ell))+poly(n).                  (6.6)

For this decoder arithmetic use the conservative O(L^2) charged
allowance per local bit action defined in Section 9.5. This gives
O(n^2 L^2 q)+poly(n). Its ratio to the full time bound is included
there using q/2^R=(2u+1)2^-u. Bounded search uses G1 and the literal stored-tape
controller in Section 4.2 and the required appendices.

Backward work. There are at most 2^Delta<=sqrt h/2<=sqrt n candidates
per block, Sback<=n, and Kback=O(L) records. Direct exact products,
comparisons, table evaluation, and streaming scores therefore take
polynomial work. Using schoolbook multiplication gives the conservative
logical bound O(n^(7/2)L); extra address/generation charges remain
polynomial. No uncounted candidate oracle is used.

Only one stage's records and running residues are stored: Kseed=O(ell+L)
records of O(n) bits, or Kback=O(L) records during backward blocks.
Candidate lists are streamed. Thus decoder storage is O(n(ell+L)),
inside O(n^2). Quantum storage is the existing one-root workspace; measure each root at once.
The final denominator has at most H+2ell+11 bits, as before.


## 7. 2-adic recovery

If a2 = 0, put s2 = 0 and skip this section. Otherwise s - s1 = M s2 (mod N) for
a unique s2 in [0, 2^a2). The bits of s2 are found at levels g = 0..a2-1. Let
s2low be the known low g bits. Put sh_g = s1 + M s2low (mod N), wd = a2 - g, and
rem = (s2 - s2low)/2^g in Z/2^wd. Then s - sh_g = M 2^g rem (mod N).

Leaf qubit for level g:
- acquire a copy and apply Shift_(sh_g), which makes the secret s - sh_g;
- run EXTRACT to obtain k, and apply X to the control.

Ideally the phase is exp(2 pi i k M 2^g rem/N) = exp(2 pi i kk rem/2^wd), with
kk = k mod 2^wd. Since 2^wd divides N and k is uniform on Z/NZ, kk is uniform on
[0, 2^wd). Use kk as the label.

- If wd = 1: if kk = 1, measure X; the outcome is + iff rem is even. If kk = 0,
  discard and repeat.
- If wd >= 2: run PS_TREE_wd (D = wd). If W is even, discard and repeat. If W is
  odd, the root is (|0> + exp(pi i W rem)|1>)/sqrt 2 = (|0> + (-1)^rem |1>)/sqrt 2,
  and an X measurement gives rem mod 2 exactly.

By (5.3), each attempt has odd W with probability exactly 1/2,
even after an incorrect odd residue or earlier bit. On such a history,
the stored reduced labels need not describe the actual phases. However,
every input qubit has equal basis magnitudes. Residue measurement and
the cyclic verified-list instrument depend only on basis membership and rank outcomes. The
separate Grover queries use only low labels and the measured residue.
Their probabilities also depend only on those low data. The unused top-bit argument and parity
law therefore still hold. The displayed phase identity is used for
correctness only when the earlier residue and bits are correct. Set bit g of s2. In the ideal run with s1 correct, every bit is correct.
Output (s1 + M s2) mod N.


## 8. Complete algorithm, two cutoffs and success

For n<256 use exhaustive shift testing. For t=0,...,N-1 use at most n+10
fresh copies, subtract t modulo N controlled by the first qubit, and measure
that qubit in X. Reject t at the first minus and output the first candidate
passing every test, or0 if none. The true t=s always passes; each wrong
candidate passes a fresh test with probability1/2. Thus wrong output has
probability<(N-1)2^(-n-10)<2^-10. It uses at most N(n+10) copies,
O(n) qubits and O(n^2) classical bits. All charged work is O(Nn^4).
This finite prefix is absorbed in the bounds.

For n>=256 compute the profile of Section 4. If M=1, set F=0 and
skip the odd decoder. If M>1, compute the pool parameters of Section 6.3.
For h<16 use the one-bit fallback of Sections 6.1--6.2 and set F=F_old.
For h>=16 use the exact strided parameters and F of Section 6.3, then
run Sections 6.5--6.6. At each 2-adic bit allow at most
K2=ceil(log2 n)+30 root attempts, or K2 direct attempts at width one.
Abort if none has odd W or label one. The conditional parity law gives
at most n2^-K2<=2^-30 added failure. The truncated search still uses
at most two attempts in expectation.

Define exact budgets

    C=C_old=6*(2u+1)*2^(R-u-mstar+1), H0=F+2n,
    Qstar_old=C*H0+2n, Qcap_old=1024 Qstar_old,
    beta_m=min(1,32*25^mstar/72^mstar),
    Qstar_dense=beta_m*C*H0+2n,
    Qcap_dense=ceil(1024 Qstar_dense),
    Wstar=6*2^R*H0, Wcap=1024 Wstar.

The exponent R-u-mstar+1 is nonnegative. Every retained gap is at
least five, so R-u>=R-v_1>=5(mstar-1). Thus C and the caps are exact integers; Qstar_dense is rational.
The acquisition and weighted-attempt caps are separate. The powers and
ceiling above are computed by polynomial-bit integer arithmetic.
Initialize the acquisition counter and the weighted-attempt counter to zero.
Before any acquisition that would exceed Qcap_dense, abort, release all registers
and output0. Before a combiner attempt, after building its inputs, check
whether adding its nominal weight2^v_i would exceed Wcap; if so abort
likewise, otherwise add it and execute the complete attempt. EXTRACT uses
Qcap_old for precision; Qcap_dense is the acquisition guard. Run the odd-part decoder followed by the2-adic procedure,
then output(s1+M*s2) mod N. No circuit execution is hidden in either counter.

Expected source bound. The required appendix proves, conditional on the
external past before fresh children are generated,

    E_i<=(25/24)(b_i+5)E_(i-1) at positive widths,
    E_root<=beta_m*C.

The full nominal product covers every skipped or partial level and B=0.
It uses no independence between attempt cost and success. With F odd
roots and at most two roots per 2-adic bit in expectation, including
wrong earlier decoder outputs, ideal expected acquisitions are at most
`beta_m*C*H0+2n=Qstar_dense`. The appendix gives all cases,
exact cap arithmetic, pool inclusion and the precision coupling.

Expected weighted-attempt bound. Dense Section 8 uses sigma=24/25
with the actual b_i+5 children. Let a_i=(25/24)(b_i+5) at active levels
and1 at shortcuts. Each a_i<=3(2v_i+1). A level-i contribution is at most
(25/24)2^v_i product_(active j>i)a_j, hence at most
(25/24)2^R 2^(-(mstar-i)). Their sum is less than(25/12)2^R<6*2^R.
This includes child attempts in failed ancestors and before a failed
parent check. Fair parity repetition and all F odd roots give the exact
old Wstar bound. Zero-width shortcuts add no weight.

Apply Markov separately to source count and weighted attempts in this
ideal uncapped process. The Qcap_dense and Wcap cutoffs each change it only on an event of
probability at most1/1024. In particular, a work cutoff before the next
attempt implies the uncapped weighted total would exceed Wcap; children
already built are already charged. There is no assumption that caps and decoder events are independent.
On the strided branch, avoiding the global caps implies Fitodd.
For every Llow in E and Fitodd, Sections 6.5--6.6 give decoder failure
at most 2^-20. Integrating gives at most 2^-20 plus Pr[E fails]<2^-190
and the two cap losses. We do not condition the top-bit law on the full
cap event of the later adaptive 2-adic run. The per-bit attempt caps add
at most 2^-30. With the correct odd residue and earlier bits, every
2-adic measurement is exact.

On the actual capped run there are at most Qcap_dense<=Qcap_old EXTRACT
calls. Precision uses Qcap_old, so the first label error has probability
at most 2^-14 by Section 3. Couple actual and ideal runs until this
first error or cutoff. The strided branch has total failure at most

    2^-190+2^-20+2*2^-10+2^-14+2^-30 < 2^-8.

For h<16, Sections 6.1--6.2 give seed error at most 2^-20 and lift
error at most 2^-30. Its same two caps, extraction error, and 2-adic
attempt cap give at most

    2*2^-10+2^-14+2^-20+2*2^-30 < 2^-8.

For M=1 the odd decoder has no failure. The n<256 finite branch has
failure below 2^-10. Thus every branch choice has unconditional full
secret recovery probability at least 1-2^-8. All failed trials and
aborts remain in the resource counts.

## 9. Every-branch resources and fixed rational envelopes

### 9.1 The changed integer profile

Write S(R) for the sum of the full positive profile before truncation,
using the new decrement. Its maximum step obeys

    D_R<=log2 R+6,

because delta(v)=ceil(log2(3(2v+1)))+1 and 3(2v+1)<=9v for v>=1.
Upper rectangles cover [0,R], so 2S(R)>=R^2/D_R. The removed tail
begins below u and has sum at most u^2<=R. Therefore

    2S_u(R)>=R^2/D_R-2R.                              (9.1)

For L>=4096, test the integer

    Rtest=ceil((71/100)sqrt(nL)).

It is at most sqrt(nL). Hence

    D_Rtest<=L/2+(log2 L)/2+6<=(503/1000)L.

The last inequality holds at L=4096, where
(3/1000)L=12.288>(log2 L)/2+6=12. It persists because
3/1000-1/(2L ln(2))>0 on that interval. Also
Rtest^2>=(5041/10000)nL. Consequently

    Rtest^2/D_Rtest >=(5041/5030)n>n+n/500.

For L>=4096, sqrt n>=1000sqrt L. At 4096 this follows from
2^2048>65536>64000, and 2^(L/2)/sqrt L increases thereafter.
Thus n/500>=2Rtest. Equation (9.1) proves 2S_u(Rtest)>=n.
The least feasible integer R is therefore at most Rtest, giving

    2^R=O(2^((71/100)sqrt(nL))),
    R=O(sqrt(nL)).                                    (9.2)

For 256<=n<2^4096 the same normal profile search is executed, and
R<=ceil(n/2) supplies an absolute finite-prefix constant. There is no
new exhaustive-secret branch. The threshold and the rational 71/100
are fixed, and no unspecified coefficient occurs inside an exponent.

The 71/100 estimate in this subsection is auxiliary. The required bound
appendix proves R<=ceil((283/400)sqrt(nL)) for L>=65536 and the selected
177/250 envelopes. The actual normal profile search is unchanged.

### 9.2 Lower bounds for the two source savings

Every new profile step is at least log2 v. Above sqrt R the spacing
is therefore at least (log2 R)/2. There are at most 1+2R/log2 R
such values, of total at most R+2R^2/log2 R. The remaining tail sums
to at most R. For R>=4, 2log2 R<=R, so

    S(R)<=3R^2/log2 R.

Since n<=2S_u(R)<=2S(R)<=2R^2, we have R>=sqrt(n/2).
For n>=256, log2 R>=L/2-1/2>=3L/8. Therefore

    n<=6R^2/log2 R<=16R^2/L,
    R>=sqrt(nL/16),
    u>=sqrt R-1 >=(1/2)(nL)^(1/4)-1,
    2u+1=O((nL)^(1/4)).                               (9.3)

For the retained level count, v_1-delta(v_1)<u and every gap is at
most D_R. Thus v_1<u+D_R and

    mstar>(R-u)/D_R.

Here R>=4, so u<=R/2. Also R<=ceil(n/2)<=n, and
D_R<=L+6<=2L for L>=8. Consequently

    mstar>R/(4L)>=(1/16)sqrt(n/L).                    (9.4)

The exact inequality 72^2>8*25^2 gives log2(72/25)>3/2. Thus

    2^(-(mstar-1))(25/72)^mstar
      =2*2^(-(1+log2(72/25))mstar)
      <=2*2^(-(5/32)sqrt(n/L)).

The factor32 in beta_m is an absolute outside constant.
The required appendix gives the complete source-envelope derivation.

### 9.3 Both resource caps

The unchanged full-frequency bound is q0=(2u+1)2^(R-u).
For integer u>=1, (2u+1)2^-u<=3/2. Hence q0<=3*2^(R-1) and
ell=ceil(log2 q0)<=R+1. Section 6.7 gives, for the strided branch,

    F=O(ell^2/L+ell+n)=O(n),
    H0=F+2n=O(n).

For M=1, F=0, so the same estimate holds. The h<16 fallback applies
at only finitely many bit lengths uniformly in N and s; its finite
maximum is included in the outside constants of every displayed bound.
The source cap is therefore, on every branch,

    Q<=Qcap_dense
      =O(n(2u+1)2^(R-u-(mstar-1))*32(25/72)^mstar+n+1)
      =O(n^(5/4)L^(1/4)
          2^(R-(5/32)sqrt(n/L)-(1/2)(nL)^(1/4))+n).  (9.5a)

The required bound appendix applies with kappa=5/32 and absorbs only
the polynomial prefactor and additive term. The selected source bound is

    Q=O(2^((177/250)sqrt(nL)
             -(5/32)sqrt(n/L)-(1/2)(nL)^(1/4))).      (9.5)

This includes all copies in failed and partial constructions. The separate geometric weighted cap is

    Wcap=O(n2^R).                                    (9.6)

Each operational cap is checked before its charged action. Since
Qcap_dense<=Qcap_old, all work bounds can use Qcap_old. Both counter
widths and the extractor parameter are O(R+log n)=O(sqrt(nL));
collective extraction retains Section 3's total cost and error budget.
The extra integer cap setup uses polynomial work and O(n^2) bits.

### 9.4 Space

A depth-first call retains at most1+B+4*(active levels)<=n+4mstar=O(n)
phase qubits, as proved in dense Section 11. Original and separate query
registers have k<=n+4 bits. The widened grouped table/record/history pool
and carries use O(n), and rank/output helpers use O(1). Extraction and
transforms also use O(n). Released registers are reused. Thus S_Q=O(n)
on every branch, including abort cleanup.

Every full signed label has O(n+log2 q0)=O(n) bits. There are O(n)
retained labels. The one residue array has O(kb)=O(nL) bits. The exact
stored G1 tape has O(nL log2(L+2))=O(n^2) bits; its full polynomial
constructor uses O(n^2) scratch, including all masks, schedule/wire maps,
markers and temporary inverse subwords. Only one attempt is active.
The found list has at most2048 strings and eleven rank bits. Profile and recursion snapshots use
O(mstar(R+log n))<=O(nL) bits. The seed stores O(R+log n) records of O(n)
bits and streams scores. Backward records, counters, extraction scratch
and exact arithmetic fit O(n^2). Thus S_C=O(n^2), also on abort branches.
The full allocation gives a_addr=O(L), including every stored instruction.

### 9.5 Fully charged work

Put E=log2(L+2). The oracle appendix proves O(nE) elementary slots for G1
and O(n) quantum space by its explicit batch construction. Compiler Part B
counts all bits of the stored instruction tape, its current-cell reads,
operand writes, tag decoding, head returns, inverse and full gate-address
debits. Part A counts the separate comparison/list/diffusion scans and all
other local helpers. With iteration control, every full iteration costs
O(nLE). The oracle constructor supplies a fixed polynomial charged bound;
all one-off preparation, verification, signed labels, measurement, reset
and cleanup costs are also polynomial. Since n<2(u+1)^4 and v>=u, every
such polynomial is at most an absolute constant times 2^v. It is paid
before this asymptotic absorption. Thus (4.2) holds for every attempt.

Each attempt's nominal weight 2^v was charged before its array, program or
scratch was built. With Wcap=O(n2^R), all executed attempt work is

    O(nLE Wcap)=O(n^2LE 2^R).                        (9.7)

This includes failed/partial words and final program clearing. A failed
weighted check starts no program; its children remain charged. Zero-width
levels create no program. The G1 word is reused without a rebuild when
e or the found list is tested, since neither changes G1.

For source, recursion/cleanup and decoder arithmetic, use this separate
conservative generator. Pad fixed field/row arrays to powers of two. A
local indexed bit/gate address can be generated by a fixed number of shifts,
additions or full copies on O(L)-bit words in O(L) raw bit actions. A full
short-word control test has O(L) raw cost. Debit O(L) to every such raw
action and each indexed gate. This gives O(L^2) charged work per local
core action. Expand all integer arithmetic into bit operations. This
allowance is used only for the remaining terms below; the G1 replay uses
its literal physical-tape implementation and full instruction-bit count.

The whole recursion/reset/abort bound remains

    O(n^3L^2[Qcap_old+Wcap/2^u+1]).                   (9.8)

Between acquisitions and attempts, at most one stack of mstar<=n frames
is traversed; each has at most O(n^2) label/counter bits. Every attempt has
weight at least2^u. This counts failed children, zero-width shortcuts,
frame movement and the last partial stack. Its search/program work was
already included in (9.7). Keep the auxiliary upper bounds

    Qcap_old=O(n(2u+1)2^(R-u)+n),
    Wcap/2^u=O(n2^(R-u)), n<2(u+1)^4.

Write Hwork=n^2LE2^R. The ratio of (9.8) to Hwork is at most a constant
multiple of

    (L/E)[n^2(2u+1)2^-u+n^2 2^-u+(n^2+n)2^-R].

It is bounded by polynomial(u)2^-u plus polynomial(n)2^-R, using
R>=sqrt(n/2). Every source call retains its fully charged O(n^2L^2)
bound for collective extraction, transforms and acquisition counters.
Its total ratio to Hwork is O((L/E)[n(2u+1)2^-u+n2^-R]), also bounded.
The direct n+1 source cost is smaller. EXTRACT retains Qcap_old for
precision; Qcap_dense is the only acquisition guard.

The strided seed retains its full charged bound

    O(n q0(ell^2/L+ell)L^2)+poly(n)
      =O(n^2L^2 q0)+poly(n).

Its nonpolynomial ratio to Hwork is (L/E)(2u+1)2^-u, which is bounded.
This counts every initial product, streamed residue update, score and
reset. F=O(n). Backward blocks have at most2^Delta<=sqrt n candidates
and polynomial work. Profile search, CRT, exact pool/cap integers, finite
trigonometric tables and all layout/strip setup are charged polynomials.
R>=sqrt(n/2) absorbs them. The source's finite h<16 and n<256 branches
have finite uniform maxima; M=1 uses no odd decoder. All failed copies,
rejected roots, partial constructions and abort work remain in these counts.

The full account above proves the pre-envelope bound

    T=O(n^2 L log2(L+2) 2^R).                         (9.9a)

The required bound appendix proves an intermediate profile coefficient
283/400 and uses its exact 1/2000 gap to the selected coefficient 177/250.
That gap absorbs every displayed polynomial prefactor. Thus the selected
final bound is

    T=O(2^((177/250)sqrt(nL))).                       (9.9)

No algorithmic parameter, numerical cap or precision rule is replaced
by this envelope. For 2<=n<2^65536 the same capped normal or finite branch
has a uniform finite maximum ratio to the positive envelopes. The
unchanged finite branch covers n=1, so no expression divides by L there.

### 9.6 Exact structured expressions

The selected structured time and source envelopes are exactly (9.9) and (9.5).
The space envelopes are n^2 and n. Every exponent coefficient is an
explicit rational. The extra source term uses nPower=1/2 and
logPower=-1/2, which represents sqrt(n/L); its coefficient is -5/32.
Both source corrections are lower order than sqrt(nL). For both T
and Q, log2 B(n)=(177/250)sqrt(nL)(1+o(1)), so
log2 log2 B(n)=(1/2)log2 n+(1/2)log2 L+O(1). Dividing by log2 n
gives the exact index 1/2. For n^2 and n, log2 log2 B(n)=O(log2 L),
so their exact indices are zero.

## 10. Error tolerance and limits

The fractional tolerance is epsilon(n)=0 under the exact error-model text:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

For all N>=2 and s, this promise gives the stated joint guarantees.
No positive tolerance or impossibility of greater tolerance is asserted.
The result uses the exact dense cyclic instrument, grouped sum, tape and rational envelope. Hosted
acceptance remains fallible review, not formal proof.
