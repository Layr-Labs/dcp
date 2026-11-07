# PSG2-GBGR: bounded Grover collimation with grouped sums

## 0. Joint theorem and provenance

For every integer N>=2 and every secret s in Z/NZ, put n=ceil(log2 N)
and L=log2 n. The single PSG2-GBGR algorithm below recovers the entire
secret from independent ideal coset copies with unconditional probability
at least 1-2^-8>2/3. On EVERY branch, including failed searches, retries,
rejected copies, and all cutoff branches, its simultaneous bounds are

    T   = O(n^2 L^(3/2) 2^((71/100)sqrt(nL))),
    S_C = O(n^2) classical bits,
    S_Q = O(n) qubits,
    Q   = O(n^(5/4)L^(1/4)
              2^((71/100)sqrt(nL)
                  -(7/80)sqrt(n/L)-(1/2)(nL)^(1/4))).

All outside constants are absolute, independent of N, s, and outcomes.
These envelopes apply for n>=2; the finite branch covers n=1. The growth
indices are [1/2,0,0,1/2]. Section 10 gives the zero-tolerance model.
This main proof and the required `grover_grouped_caps.md`,
`grover_grouped_oracle.md` and `grover_grouped_compiler.md` define one
complete algorithm. They contain the full source, retry-cap, grouped-circuit,
stored-tape and helper proofs. All five claims require all four proof files.
Section 9.5 also proves the tighter nested-log time bound. The declared
supported envelope is the displayed L^(3/2) bound.

Direct sources and actual reuse:

- The exact complete own source package is `grover_stride_retry_l2.md`,
  SHA-256 a24ae207804e3b494ae78d0c260adfc7255f97e637dc15d8f6725bce60d36745;
  `grover_stride_retry_l2.json`, SHA-256
  fde94a80955f0dd97aa78faf0f4e78a45cc61ac4ec0f59a90262c468ba33734c;
  `grover_stride_retry_l2_caps.md`, SHA-256
  307dacf6e310e0b24878e8133d609528b0cfbb8d88b0be18313bea92d877b263;
  and `grover_stride_retry_l2_compiler.md`, SHA-256
  697869d57d7603de1f39e712189cf26dc1cf2f8d8324ef32a103836c3bdf1243.
  Its complete source, statistics, caps, decoder, precision and helper
  proofs are reproduced in this package.
- The own grouped circuit `grouped_oracle.md`, SHA-256
  a922b88fa5815e0caf00835c2fd4309832806f5dca39f44e76032730e6e60272,
  supplies exact G1 and its retained-history proof, reproduced in the
  required oracle appendix with the complete polynomial constructor.
- The own `stored_oracle_stream.md`, SHA-256
  366497582e1c87ceb0e2e48ecf5aa40e7e3ad52b86ec3e4cf09d2a49da167927,
  supplies the literal stored-tape controller, reproduced in full in the
  compiler appendix. Its proof uses physical current-cell tape steps and
  keeps the complete charge on every actual indexed access and gate.
- The exact own retry configuration has main SHA-256
  515f4eb6b8c02806e8e0f3ba60c3f5a19cb3e13e2b80485dc85347c2e42a007b
  and retry appendix SHA-256
  97abcaeed66e3d88a200045a1a69128212afc1dd7adbaea237c988ec49b3603e.
  The full supplier, source model, caps and success proof are reproduced here.
- The own bounded compiler proof `grover_stride_compiler.md`, SHA-256
  4c5bcd59c95fa2c10be21ab610cdfe76f6b8d2d31300582b97417a7f5b7e896f,
  supplies the complete counted stream reproduced in the compiler appendix.
  Its local tape/ready-address method came from
  `critical_third_cache_generator_l2.md`, SHA-256
  eb122317b103da59cdd982b29f863da27d1d932313e8b67861d1d212a64088f3.
  Only that generator method is used; the full derivation is included here.
The complete earlier source identities, exact reuse and historical credits
are reproduced verbatim in compiler Part D. They include PSG2-SBG, PSG13,
PSG2, CS1-BACKWARD, collective tests, CW1S/HS2 and the unpublished own
sources. The cap appendix also retains its exact material source table.
Every needed proof is contained in this four-file package.

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
and classical scratch O(n log n). Over Qcap_new<=Qcap_old calls, the
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
B-already_allocated). Then sum_i b_i=B. Let r_i=b_i+1 and
p_i=sum_(j<i)b_j. Level0 returns a leaf. A zero-width level just returns
its child. For b_i>0, recursively build r_i fresh child outputs, then check
and add weight2^v_i to the global weighted-attempt counter before executing
the combiner below. If that would exceed Wcap, abort. On FAIL discard ALL
inputs and query scratch, and build fresh children before trying again.
No output label, including zero, is rejected inside the tree merely because
of its higher bits or value.

### 4.1 Exact state preparation and verified-pair output

The inputs are phase qubits with full signed labels a_1,...,a_k divisible by
2^p, where k=b+1, b=b_i, p=p_i. Their joint state is

 2^(-k/2) sum_(y in{0,1}^k) exp(2pi i th A(y))|y>, A(y)=sum_j y_j a_j.

Set c_j=(a_j/2^p) mod2^b. Initialize the separate k-bit query z and
b-bit accumulator A to zero. CNOT each original y_j into z_j, run the
fixed-query-address G1 word on z,A, then CNOT each y_j into z_j again.
G1 preserves z and clears its helpers, so z returns exactly to zero.
The net map is |y>|0>_A -> |y>|f(y)>_A, also with arbitrary reference
registers entangled with y. Measure A to obtain e, and reset A.
This wrapper adds exactly 2k indexed CNOT gates and reuses the separate
query register. The remaining phase state has equal magnitudes on
C_e={y:f(y)=e}.
Hold this original register untouched during discovery on SEPARATE query
registers. The discovery procedure below returns at most64 distinct,
classically verified members of C_e, using only c_j,e and fresh random bits.
It need not certify completeness. Sort the found strings and pair adjacent
ones, dropping an unpaired singleton. Reversibly compute on the original y
a success flag and a constant-size pair ID from equality tests with the
known list, then measure them. If y matches no pair, FAIL and discard.
Otherwise it is now an equal-magnitude superposition of exactly two known
strings y0,y1, with their original phases. Reset measured flags from their
known values. XOR y0 into y, choose a differing pivot, and use CNOTs from
that pivot to clear every other differing position. The surviving qubit has
label a'=A(y1)-A(y0), a FULL signed integer, not reduced modulo2^D or N.
Every successful branch is exactly this phase qubit, up to global phase,
regardless of whether discovery found the entire fiber.

The output is divisible by2^(p+b), since both selected strings have residue e.
It has a nonzero symbolic incidence vector in{-1,0,1} over distinct original
leaves: y0!=y1 differs in some child, child incidence vectors are nonzero,
and child leaf sets are disjoint. This induction starts at a single leaf.
Full labels are stored, but ALL choices of found strings and pairs, and
all success probabilities, factor through input residues modulo2^(p+b).
The unknown phase th is absent from this selection kernel. Computing a
full output label after selection does not add a selection rule on its high
bits. This distinction is used in the marginal argument of Section5.

### 4.2 Bounded discovery, exact Clifford+T circuits

Fix C=64. If k<=7, enumerate at most128 strings and retain the first64
solutions; this has constant enumeration length. If k>=8, use at most64
search blocks. Each block makes at most64 trials, stopping at its first
new verified solution, which is added to the list. Stop discovery after an
empty block or after64 found solutions. The list never contains a duplicate
or a false solution. On each trial:

 * Set J0=2^ceil(k/2), draw uniform j in[0,J0) with ceil(k/2) fair bits.
 * Prepare a fresh k-qubit query in |+>^k. Apply j Grover iterations for
   membership in C_e minus the found list. Measure its candidate string.
 * Verify its residue and novelty classically. Reset query registers before
   the next trial. The original phase-index register is not touched.

The selected exact sum circuit is G1 in the required oracle appendix.
It sends |z>|A>|0> to |z>|A+f(z) mod2^b>|0> for every z and A.
For k<max(16,u) it uses direct controlled additions. Otherwise it uses
w=floor(log2(k)/2), d_count=ceil(log2(w+1)), g_count=ceil(k/w), and
h_count=min(b,max(1,floor(n/(g_count*d_count)))). Each batch builds each
group's complete subset-count table, copies its selected counts, and
clears the table. A reversible sum retains all its inputs/history, adds
one batch result into the accumulator, then clears the sum and selected
counts by exact reverse circuits. The appendix proves O(n) qubits and
H=O(n log2(L+2)) elementary slots for the complete G1 word. It includes
all short rows, last groups/batches, top modular bits and reverse work.

After the weighted check, form the k by b known residue array by reading
actual signed child-label bits p,...,p+b-1. They give exactly
(a_j/2^p) mod2^b, also for negative labels. The original field has p+b<=n-1.
Read each bit through counted indexed access. Power-of-two row padding is
only for addresses. The oracle appendix gives the full uniform constructor:
it generates every mask, heap schedule, wire address, instruction bit and
marker in polynomial work with O(n^2) classical bits. Initialize the O(n)
quantum pool and store only this polynomial-size G1 word once per attempt.
Its addresses and c_j remain fixed throughout the attempt.

Use Section 4.1's copy/G1/uncopy wrapper for the first coherent f(y)
preparation. It uses this same stored word and its fixed query addresses.
Its 2k extra indexed CNOTs are paid once per attempt. A membership
reflection on the separate query runs G1 forward from a zero accumulator,
compares with e, excludes at most64 known found strings, applies Z on the
clean computed flag, then reverses the tests and G1. Diffusion is H^k,
a clean forward/reverse Toffoli chain and the exact sign gate, then H^k.
Z=S^2. All gates have fixed exact Clifford+T words; no phase approximation
or quantum lookup is used. This computes exactly the same f, membership
and phase maps as Sections 4.1 and 4.3 require. Every choice still uses
only the same low residues. No high child-label bit changes selection.

Use Part B of the compiler appendix to read the literal stored G1 tape
forward or backward. It reads O(L) actual instruction bits per elementary
gate, counts all local head movement and operands, and pays the full
indexed gate debit. Each complete pass costs O((H+1)L). Comparison,
found-list tests and diffusion use Part A's complete ready-address scans,
with charged work O((k+b+a_addr)L), a_addr=O(L). The iteration word has
ceil(k/2) bits; even full decrement and stop tests cost O(k+a_addr) raw
actions. Including both G1 passes, all helper scans and loop control, one
iteration therefore costs O(n L log2(L+2)) charged sequential work.
There are at most4096 trials, each with fewer than J0<=2^(v+1) iterations.

Initial coherent preparation, classical verification, fair bits, sorting,
projection tests, affine clearing, measurements and resets are also counted.
After pair selection, compute the full signed label from at most k child
labels by O(k) additions/subtractions on fields of
n+ceil(log2 q0)+4=O(n) bits, including guard bits. This costs O(nk) core
bit work and O(n) scratch. This is once per attempt. Program generation,
these one-off operations and cleanup have a fixed polynomial charged
bound, explicit in the appendices. The inequalities n<2(u+1)^4 and v>=u
absorb that paid polynomial into O(n L log2(L+2)2^v). Thus a complete paid
attempt, including all failed/partial paths, costs

    O(n L log2(L+2) 2^v).                             (4.2)

No cap interrupts an uncounted word. A weighted failure builds no program;
its children remain charged. Only one attempt/program is active, and its
residue array, program and scratch are released before new children are
built. Retained labels and all programs/helpers fit S_C=O(n^2); live
quantum history, the original/query registers and source stack fit S_Q=O(n).

### 4.3 Discovery probability and the measured-fiber moment

Suppose the measured fiber has at most64 members. At any search trial with
1<=m<=64 remaining solutions, let A=2^k and sin^2(gamma)=m/A. In the
normalized good/bad two-dimensional basis the marking reflection and
uniform-state reflection rotate by2gamma; therefore success after j
iterations is sin^2((2j+1)gamma). Summing the cosine geometric progression
for uniform j gives

 mean success=1/2-sin(4J0*gamma)/(4J0*sin(2gamma)).

For k>=8, m<=64<=A/2, hence sin(2gamma)>=sqrt(2/A) and J0>=sqrt A.
The mean is at least1/2-1/(4sqrt2)>1/4. A64-trial block consequently misses
while solutions remain with probability at most(3/4)^64<2^-16.
Over at most64 relevant blocks, premature stopping has probability at most
64*2^-16=1/1024. Once no solutions remain a block simply finds none;
no counting oracle is used. Small k is enumerated exactly up to the list cap.

Now suppose c_j are independent uniform residues in Z/2^b. The residue
measurement has the same probability law as e=f(Y) for an independent
uniform classical index Y. For each z!=Y, f(z)-f(Y) contains a coefficient
+1 or-1 of a uniform c_j and is uniform modulo2^b. Therefore

 E |C_(f(Y))|=1+(2^k-1)/2^b<3.

This is the SIZE-BIASED fiber law of the actual measurement. Markov gives
Pr[|C_e|>64]<3/64. If discovery is complete, the failure mass of dropping
one singleton from each odd fiber, averaged over residue outcomes, is
#odd_fibers/2^k<=2^b/2^k=1/2, for every fixed weight list.
Combining large-fiber, discovery-miss and singleton events yields

 Pr[success]>=1-3/64-1/1024-1/2=463/1024>4/9.              (4.1)

Equation(4.1) averages fresh uniform weights and search coins, not fixed
child labels. Correct outputs and low-bit kernels still hold for fixed
labels. Section 5 supplies fresh uniform weights at each retry.

## 5. Unused blocks, termination and the root frequency

Lemma U (joint induction). In the ideal uncapped process, every tree-level
call terminates almost surely. If it cancels p bits, its returned label
x/2^p mod2^(D-p) is uniform, conditional on any external past before the
fresh call. Distinct fresh child calls give independent such quotients.

Proof. The leaf statement is the exact uniform latent-label source law.
Assume the statement at the lower level. Before a new node attempt starts,
its freshly generated children have independent uniform quotients modulo
2^(D-p). Their residues c_j modulo the next2^b are thus independent uniform.
Equation(4.1) gives conditional success at least4/9 before child generation,
whatever the earlier external past. Every failure releases its inputs and
restarts with fresh children. The geometric bound proves almost-sure
termination and finite expected attempts at this level.

It remains to prove the output law that closes the induction. Fix any
finite successful selection transcript through this level, containing all
used leaf values modulo2^(p+b), search choices/outcomes, residue and pair
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

The new decrement gives, above the base,

    3r_i<=3(2v_i+1)<=2^(delta(v_i)-1).

Since v_(i-1)=v_i-delta(v_i), it follows that

    product_(j>i)(3r_j)<=2^(R-v_i-(mstar-i)).           (5.1)

The base has r_1<=2v_1+1. Since (2x+1)2^-x decreases for integers
x>=1 and v_1>=u, the number of nominal leaves satisfies

    q_D=product_i r_i
       <=(2v_1+1)2^(R-v_1-(mstar-1))<=q0.

The weaker bound q0 is retained for all label widths and the decoder.
The stronger product in (5.1) will determine the source and work caps.

A returned tree has q_D nominal distinct leaves. Its label is2^B W with
integer |W|<2q0. All stored labels and sums have O(n+log q0)=O(n) bits,
including incorrect numerical-label branches. No incidence vector is stored.
Lemma U is unchanged at the new base: its inputs are independent fresh
uniform leaves and the same low-bit selection proof applies to its b_1 bits.

For the root, retain the stronger full-frequency argument as well as Lemma U.
Write each accepted leaf label k_l=u_l+2^B tau_l, with independent fair bits
tau_l. Condition on all low u_l, residue/search/pair outcomes and retry
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
    Qstar_new=ceil(3^mstar C(F+2n)/4^mstar)+2n,
    Qcap_new=1024 Qstar_new.

Also use

    Wstar=6*2^R(F+2n), Wcap=1024 Wstar.

Keep the existing before-action cap checks. Keep K2=ceil(log2 n)+30
attempts at each 2-adic bit and the existing direct width-one case.
A root's source cost and outcome need not be independent. The uniform
fresh-attempt arguments of Sections 5 and 8 give expected total sources
<=Qstar_new and expected total weight <=Wstar, by the required appendix.
Use Qcap_new before every acquisition. Keep Qcap_old for EXTRACT
precision and pool analysis. Each operational cap costs at most 2^-10 failure by Markov.

The analysis pool really contains the capped run. Since Delta>=1,
Sseed<=ell+3 and Sback<=n. Also Kseed,Kback<=2^15 U. Consequently

    F<=2^15 U^2,
    Qcap_new<=Qcap_old<=2^27(C+1)U^2<=A.

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
construction/search/residue/pair outcomes in the fixed odd-root schedule.
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
projection onto verified pairs depend only on basis membership. The
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

Define exact integer budgets

    C=C_old=6*(2u+1)*2^(R-u-mstar+1), H0=F+2n,
    Qstar_old=C*H0+2n, Qcap_old=1024 Qstar_old,
    Qstar_new=ceil(3^mstar*C*H0/4^mstar)+2n,
    Qcap_new=1024 Qstar_new,
    Wstar=6*2^R*H0, Wcap=1024 Wstar.

The exponent R-u-mstar+1 is nonnegative. Every retained gap is at
least five, so R-u>=R-v_1>=5(mstar-1). Thus these are exact integers.
The acquisition and weighted-attempt caps are separate. The powers and
ceiling above are computed by polynomial-bit integer arithmetic.
Initialize the acquisition counter and the weighted-attempt counter to zero.
Before any acquisition that would exceed Qcap_new, abort, release all registers
and output0. Before a combiner attempt, after building its inputs, check
whether adding its nominal weight2^v_i would exceed Wcap; if so abort
likewise, otherwise add it and execute the complete attempt. EXTRACT uses
Qcap_old for precision; Qcap_new is the acquisition guard. Run the odd-part decoder followed by the2-adic procedure,
then output(s1+M*s2) mod N. No circuit execution is hidden in either counter.

Expected source bound. The required appendix proves, conditional on the
external past before fresh children are generated,

    E_i<=(9/4)r_i E_(i-1),
    E_root<=(3/4)^mstar C.

The full nominal product covers every skipped or partial level and B=0.
It uses no independence between attempt cost and success. With F odd
roots and at most two roots per 2-adic bit in expectation, including
wrong earlier decoder outputs, ideal expected acquisitions are at most
`(3/4)^mstar C H0+2n<=Qstar_new`. The appendix gives all cases,
exact cap arithmetic, pool inclusion and the precision coupling.

Expected weighted-attempt bound. For a root call, the expected number of
leveli attempts is at most 3 product_(j>i)(3r_j). The same conditional
geometric-sum argument proves this by induction, including attempts in
failed ancestors. Telescoping the profile gives

 product_(j>i)(3r_j)<=2^(R-v_i-(mstar-i)).

Hence the expected weight at level i is at most
3*2^R*2^(-(mstar-i)). Its sum over levels is strictly less than
6*2^R, by the geometric series.
Zero-width shortcuts contribute zero. Summing over all roots, with the
same conditional argument for odd-W repeats, bounds ideal expected total
weighted attempts by Wstar.

Apply Markov separately to source count and weighted attempts in this
ideal uncapped process. The Qcap_new and Wcap cutoffs each change it only on an event of
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

On the actual capped run there are at most Qcap_new<=Qcap_old EXTRACT
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

Since (4/3)^5>4, log2(4/3)>2/5. Thus

    2^(-(mstar-1))(3/4)^mstar
      =2*2^(-(1+log2(4/3))mstar)
      <=2*2^(-(7/80)sqrt(n/L)).

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

    Q<=Qcap_new=O(n(2u+1)2^(R-u-(mstar-1))(3/4)^mstar+n)
      =O(n^(5/4)L^(1/4)
          2^((71/100)sqrt(nL)
              -(7/80)sqrt(n/L)-(1/2)(nL)^(1/4))).       (9.5)

This includes all copies in failed and partial constructions. The separate geometric weighted cap is

    Wcap=O(n2^R).                                    (9.6)

Each operational cap is checked before its charged action. Since
Qcap_new<=Qcap_old, all work bounds can use Qcap_old. Both counter
widths and the extractor parameter are O(R+log n)=O(sqrt(nL));
collective extraction retains Section 3's total cost and error budget.
The extra integer cap setup uses polynomial work and O(n^2) bits.

### 9.4 Space

A depth-first call retains at most sum_i(r_i-1)+1=B+1<=n phase
qubits. One active attempt has the original and separate query registers.
The required oracle appendix proves O(n) total selected-count records,
subset-table bits, accumulator, reusable carry scratch and retained sum
history, with all reverse work included. Source extraction and transforms
also use O(n). Released registers are reused. Thus S_Q=O(n) on every branch.

Every full signed label has O(n+log2 q0)=O(n) bits. There are O(n)
retained labels. The one residue array has O(kb)=O(nL) bits. The exact
stored G1 tape has O(nL log2(L+2))=O(n^2) bits; its full polynomial
constructor uses O(n^2) scratch, including all masks, schedule/wire maps,
markers and temporary inverse subwords. Only one attempt is active.
The found list has at most64 strings. Profile and recursion snapshots use
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
precision while Qcap_new<=Qcap_old is the actual acquisition guard.

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

Using (9.2) yields the tighter internal bound

    T=O(n^2 L log2(L+2) 2^((71/100)sqrt(nL))).         (9.9a)

The declared supported theorem uses log2(L+2)=O(sqrt L), giving

    T=O(n^2 L^(3/2) 2^((71/100)sqrt(nL))).             (9.9)

Equation (9.9a) is retained as additional detail. Its nested logarithm is
not exactly represented by the supported envelope family. The structured
claim represents exactly the selected weaker theorem (9.9); it does not
pretend to encode the sharper nested-log factor.

### 9.6 Exact structured expressions

The selected structured time and source envelopes are exactly (9.9) and (9.5).
The space envelopes are n^2 and n. Every exponent coefficient is an
explicit rational. The extra source term uses nPower=1/2 and
logPower=-1/2, which represents sqrt(n/L); its coefficient is -7/80.
Both source corrections are lower order than sqrt(nL). For both T
and Q, log2 B(n)=(71/100)sqrt(nL)(1+o(1)), so
log2 log2 B(n)=(1/2)log2 n+(1/2)log2 L+O(1). Dividing by log2 n
gives the exact index 1/2. For n^2 and n, log2 log2 B(n)=O(log2 L),
so their exact indices are zero.

## 10. Error tolerance and limits

The fractional tolerance is epsilon(n)=0 under the exact error-model text:

Malformed fraction among acquired copies. The proved guarantee requires every copy to be an independent ideal coset state; no behavior is promised for malformed copies.

For all N>=2 and s, this promise gives the stated joint guarantees.
No positive tolerance or impossibility of greater tolerance is asserted.
The result uses the exact grouped sum and stored-tape implementation above. Hosted
acceptance remains fallible review, not formal proof.
