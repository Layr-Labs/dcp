# Exact one-third tolerance with linear quantum storage and nested search

## 0. Joint theorem and one parameter rule

**Proved.** For every integer N>=2 and s in Z/NZ, let n=ceil(log2 N).
Algorithm B below outputs the entire s with unconditional probability at
least 11/16>2/3 under the error model reproduced below, at epsilon(n)=1/3.
On every execution branch its joint bounds are

    T = O(2^n n^3 (log2 n)^2),
    S_C = O(n^2),  S_Q = O(n),  Q = 3*2^16*(n+32) = O(n).

Constants are absolute and independent of N, s, the supplier and outcomes.
Logarithmic cost estimates use log2(n+2), which is asymptotically equivalent
to log2 n; the single n=1 modulus has finite absolute cost. The representative
envelopes have growth indices 1,0,0,0. There is no validity threshold.

The fixed parameters, computed by finite integer arithmetic, are:

    K=2^n; Q=3*2^16*(n+32); r=Q/3;
    q=14; p=q+3+bitlength(n); J0=max(1,n-2);
    L_F=bitlength(16*(J0+1)*Q*2^60); R_F=200*L_F;
    m=ceil(n/2)+2; B=2^m;
    L=3^d, the least power of 3 >=32*n+512;
    P=2*160*(B-1)*(L-1); g=bitlength(2^80*(P+Q+1)); G=2^g.

Here bitlength(a)=floor(log2 a)+1 for positive integer a. The source count is
exactly Q even on preparation-failure branches. Every loop has a public finite
cap. Acquisition is never repeated, and no inverted circuit acquires a source.

### Exact error-model specification

Adaptive malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires, and epsilon(n) the tolerated malformed fraction. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm, and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed; on every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. A malformed copy is an arbitrary (n+1)-qubit state (the register shape of an ideal copy) supplied from the adversary's system: it may be pure or mixed, may be entangled with the adversary's remaining system and with other malformed copies, and may depend on all of the information above; it is not entangled with clean copies or with the algorithm's workspace, ancillas or internal random bits. Every copy that is not malformed is clean: at the moment of its delivery, a fresh ideal coset state rho_s = (1/N) sum_x |psi_{x,s}><psi_{x,s}| in tensor product with everything else (the adversary's system, all other copies and the algorithm's workspace), i.e. clean copies are independent ideal coset states. The adversary interacts with the algorithm only by supplying copies; after delivery it has no access to the copy or to the algorithm's quantum or classical systems. All measurements have countably many outcomes. The algorithm is not told which copies are malformed. Quantifiers: the guarantee must hold for every N >= 2 (no validity threshold), every s in Z/NZ and every such adversary, including the adversary that corrupts nothing (the clean problem): the algorithm outputs the entire s with probability at least 2/3, and the four declared resource bounds hold on every execution branch. The fraction bounds the number of malformed copies among acquired copies; it is not a per-copy corruption probability.

This is a cap on the number of corrupted deliveries, not independent
per-delivery noise. In particular it allows entanglement among malformed
copies and supplier choices depending on all earlier actual measurements.

### Complete algorithm schedule

1. Acquire and process Q sources sequentially by Section 2. Keep each row
   qubit, its classical valid flag and estimated Fourier label and prefix word;
   measure/reset/release its position and probe work before the next delivery.
2. Prepare the ordinary work gradient of Section 7, with 80 capped attempts.
   If all attempts fail, output 0. This happens after acquiring all Q sources.
3. Apply the known unitary U: generate coherent X/Y row records (Section 3),
   run the bounded coherent class selector (Section 6), and compute its answer.
4. Copy only the class answer to a fresh register and apply the literal inverse
   of U, retaining all residual work. Measure the copied class. Replace an
   invalid class ID by 0, to make the procedure total.
5. At odd N return this singleton. At even N run the same-row-bank trit
   decision of Section 8, using fresh final arithmetic helpers.

For N=2 there is only one class and steps 3-4 are omitted; its canonical
representative is 0. All other formulas, including Q, remain the same.

## 1. Exact arithmetic, table construction and label extraction

**Proved (arithmetic primitives).** A ripple carry computes addition,
subtraction, comparison and controlled addition on w-bit words in O(w) Boolean
gates and O(w) reusable clean scratch. One explicit construction computes the
carry recurrence c_(i+1)=MAJ(a_i,b_i,c_i), where
MAJ(a,b,c)=ab XOR ac XOR bc, into fresh bits, writes the sum by XOR, and reverses
the carry computation. Comparison with a constant is its carry-out version.
For an XOR-output computation, intermediate NOT/XOR/AND values use respectively
X and CNOT, two CNOTs, and Toffoli, followed by reversal after copying the output.
Repeated-input AND is a CNOT and repeated-input XOR is zero. This construction
returns its scratch to zero for every input and arbitrary XOR-output target.

For a known c modulo N, define the full permutation a_c(x)=(x+c) mod N when
x<N, and a_c(x)=x on padding N<=x<2^n. Comparisons with N and N-c, followed by
the appropriate constant sum, give an O(n)-size XOR-output circuit. Compute
the permutation into a new register, swap, and XOR-compute its inverse into
the old one to clear that register. This gives an in-place O(n)-gate,
O(n)-scratch circuit. Including an unchanged control among the inputs gives
the controlled version, with the entire padded-domain permutation guarded.
All controlled Boolean gates have constant-size clean-ancilla decompositions.
For a mod-2^w register adder use the same compute/swap/inverse-compute method,
preserving the addend. These facts also give O(w)-gate signed comparison,
controlled increment and multi-controlled phase with O(w) clean scratch.

An exact Toffoli word, in chronological order, is

    H(c), CX(b,c), Tdag(c), CX(a,c), T(c), CX(b,c), Tdag(c),
    CX(a,c), T(b), T(c), H(c), CX(a,b), T(a), Tdag(b), CX(a,b).

The parity identity
4abc=a+b+c-(a XOR b)-(a XOR c)-(b XOR c)+(a XOR b XOR c)
verifies the word, without a relative phase. Tdag=T^7, Sdag=T^6, and Z=T^4.
Thus all Boolean gates and all finite phase tests below are exact Clifford+T.
Every released qubit is measured and reset by a conditional X; all measurement
outcomes and address operations are charged. Gate templates are emitted from
their bit loops, rather than stored as a long circuit description.

### Fixed cosine table

**Proved.** At startup, for each a=0,...,2^q-1 compute the rational number

    x_a=2*(103993/33102)*a/2^q,
    C_a=round(2^25 * sum_(j=0)^20 (-1)^j*x_a^(2j)/(2j)!),
    round(z)=floor(z+1/2).

Store signed C_a in 27 bits. Its normalized error from cos(2*pi*a/2^q) is
less than tau=2^-24, and |C_a|<=2^25. For details, Machin's identity
pi=16 arctan(1/5)-4 arctan(1/239), with 40 alternating terms and the first
omitted term as a rigorous remainder, gives
3.1415926535<pi<3.1415926536 and |pi-103993/33102|<6*10^-10.
The identity follows from the tangent double-angle and subtraction formulas:
4 arctan(1/5)-arctan(1/239) is in (0,pi/2) and has tangent 1.
The angular error is <1.2*10^-9. Since x_a<6.3, the degree-40 cosine
polynomial, also its degree-41 Taylor polynomial, has remainder bounded by
(6.3)^42/42!<2.8*10^-18. Rounding contributes at most 2^-26. Their sum is
<2^-24. The unrounded polynomial is within 2.8*10^-18 of [-1,1], so the
rounded integer is in [-2^25,2^25]. These are fixed-size rational computations
and a fixed-size table, with their finite work and memory included.

A coherent lookup XORs C_a into a word by scanning all 2^q classical entries,
computing equality with the q-bit quantum address, copying the corresponding
classical word under that equality, and uncomputing equality. Its gate and
workspace costs are absolute constants because q=14. Applying the lookup
twice clears its output. Sine uses the quarter-period-shifted cosine entry.
No quantum-addressed memory primitive is assumed.

### Repeated phase test and exact dyadic decoding

**Proved (label lemma).** Let a register be a translation eigenvector with
eigenphase phi. At levels i=0,...,J and offsets h=0,...,7, perform R tests:
fresh control |+>, controlled translation by 2^i modulo the register modulus,
Tdag^h on the control, H, computational measurement. Its outcome-0
probability is (1+cos(2*pi*(2^i*phi-h/8)))/2. Given the eigenphase, all probe
outcomes are independent and the tested eigenvector is unchanged.

Let z_(i,h) count zeros, choose h_i maximizing z_(i,h), smallest on ties,
and put beta_i=h_i/8. Starting x_J=beta_J, descend: choose between
x_(i+1)/2 and x_(i+1)/2+1/2 the circularly closer to beta_i, smallest on ties.
With probability at least 1-16*(J+1)*exp(-R/200),

    circular_distance(x_0,phi)<2^-J/8.

Indeed each empirical probability deviates by >=1/20 with probability at
most 2 exp(-R/200), by the exponential bound proved in Section 5. Union over
8(J+1) tests. The nearest eighth-grid offset is within 1/16 turn, giving
probability >(1+.92)/2=.96. Offsets at least 1/8 turn away give probability
<(1+.71)/2=.855, since cos(pi/8)>.92 and cos(pi/4)<.71. The gap exceeds 2/20;
therefore each chosen beta_i is within 1/8 turn of the true dyadic phase.
If the finer estimate has error e<1/8, its two halves differ by half a turn;
one has error e/2 and is within <3/16 of beta_i, the other is farther than
5/16. Induction halves the error at every level. All decoded x_i are exact
dyadics with at most J+3 fractional bits. The rule is total on every count
vector, including failed estimates.

For modulus D, b=ceil(log2 D), take J=max(1,b-2). Since D<=2^(J+2),
round(D*x_0) mod D is the true eigenlabel: its circular residue error is
<D*2^-J/8<=1/2, so no rounding tie occurs. Reconstruction, multiplication,
rounding and reduction use O(b^2) classical bit operations and O(b) scratch,
besides O(b log R) count bits. A fair classical bit is H followed by measurement.

## 2. Streaming compression, with supplier feedback retained

**Proved (source decomposition).** With

    chi_k=N^-1/2 sum_(x<N) exp(-2*pi*i*k*x/N)|x>,
    phi_(k,s)=(|0>+exp(2*pi*i*k*s/N)|1>)/sqrt(2),

direct expansion of the given coset mixture gives

    rho_s=(1/N) sum_(k<N) |phi_(k,s)><phi_(k,s)| tensor |chi_k><chi_k|.

Translation by a on the position has eigenvalue exp(2*pi*i*k*a/N) on chi_k.
The label probes act on position and their fresh controls, leaving the row
unchanged conditional on k. This is an ensemble identity for the supplied
mixed state, not access to an unavailable purification or Fourier transform.

For each delivery j: measure a valid-position flag v_j. On valid positions run
the preceding label procedure with J0,R_F, obtaining k_j in [0,N). On invalid
positions put k_j=0. Retain the source row qubit. Measure/reset/release all
position and probe work. Store v_j,k_j and

    e_j=floor(2^(n+p)*k_j/N)

classically, using binary long division. A complete clean delivery has v_j=1,
an unchanged row phi_(k,s), uniform latent k, and

    Pr[k_j != k | latent k, earlier history, clean delivery]
      <16*(J0+1)*2^-L_F <2^-60/Q.

Here exp(-L_F)<2^-L_F and the bitlength rule is strict. Consequently the
probability of ANY mislabelled clean delivery is <2^-60 even for an adaptive
supplier, by conditional union bounds. No independence of supplier decisions
is used. Position reset outcomes are part of the actual public history.

**Proved (bad-input diagonal bound).** On a valid position eigenbasis the
entire probe instrument is block diagonal: controlled translations are diagonal
there and every other gate acts on a probe. The effect of reporting label ell
is sum_k p(ell|k)|chi_k><chi_k| tensor I_row, with
p(k|k)>1-2^-60/Q uniformly in k. Measuring/discarding position kills cross-k
terms in each score expectation. The valid flag kills valid/padded cross terms.
These statements hold on arbitrary input density matrices and entangled bad
blocks; conditional row states may be arbitrary. They do not assert that
malformed rows are independent or that all reported labels are correct.

Supplier processing of its private system during this local instrument does
not invalidate its marginal POVM. On each branch of the actual public probe
history, the supplier's completely positive maps act on a disjoint system;
the algorithm's subsequent local gates never depend on private supplier
outcomes. Move those maps past the remaining local gates and measurements,
keeping their classical control histories. Summing their private outcomes
then leaves the local outcome law unchanged. This argument applies before
the next delivery, without discarding its dependence on those private
outcomes. Bounds for this delivery are conditioned only on its earlier
history, not on the supplier's later private outcomes.

The acquisition schedule makes real measurements before later deliveries.
We therefore do not reduce the supplier to fixed bad positions. The direct
causal proof in Section 5 explicitly allows the resulting feedback.

## 3. Bounded pair witnesses and coherent row records

**Proved (witness lemma).** Let P_valid be the valid-source projector. Let U_t
add t modulo N on row 1 of valid positions, fixing padding, and put
R_t=U_t X_row U_t^dagger. These are Hermitian involutions, all equal to X on
padding. On valid words rho_t=(P_valid+R_t P_valid)/(2N), and translation
traces give tr(R_t rho_s)=1_[t=s]. Also R_t R_u R_t=R_(2t-u).
For A=(R_t-R_u)/2 define

    M_tu=(7A-2A^3)/5
        =[11(R_t-R_u)+R_(2t-u)-R_(2u-t)]/20.

The identity follows by expansion using the two involution squares. Since
||A||<=1 and (7x-2x^3)/5 increases from -1 to 1 on [-1,1], ||M_tu||<=1.
It is zero on padding and M_ut=-M_tu. For t!=u with 2(t-u)!=0 modulo N,

    tr(M_tu rho_t)=11/20,   tr(M_tu rho_u)=-11/20.

The only excluded distinct pairs are antipodes at even N. The trace formulas
above prove these means, since neither affine extra index equals the true
index in a nonexcluded comparison. On an actual k block R_t is
cos(2*pi*k*t/N) X+sin(2*pi*k*t/N) Y. Thus M_tu has complex coefficient

    h_tu(k)=[11(exp(2*pi*i*k*t/N)-exp(2*pi*i*k*u/N))
                 +exp(2*pi*i*k*(2t-u)/N)-exp(2*pi*i*k*(2u-t)/N)]/20,

and |h_tu(k)|<=1 for every k,t,u. This last bound holds block by block for
arbitrary real phases as well, by the same two-involution polynomial argument.

For each retained row append a fresh axis qubit |+>. Controlled on axis 1,
apply Sdag to the row, then apply H to the row. Its computational value is the
sign record b, y=(-1)^b. Axis 0 is an X measurement and axis 1 a Y measurement
in the conceptual measured experiment. The axis and row remain coherent in
the actual algorithm. Controlled Sdag has the exact word
Tdag(axis), Tdag(row), CX(axis,row), T(row), CX(axis,row).
Every later score operation preserves both of these computational values.
The record-generation unitary has a known inverse and uses O(Q) qubits.

The ideal pair score is 2y Re h on axis X, 2y Im h on axis Y, and zero if the
position flag is invalid. Its mean on any source density is tr(M_tu rho),
because the fresh axis is fair. Each score lies in [-2,2].

## 4. Prefix arithmetic for every quantum pair operand

**Proved (uniform approximation).** For each stored e_j and i=0,...,n-1 set

    a_(j,i)=floor(e_j/2^(n-i)) mod 2^p
           =floor(2^p frac(2^i*k_j/N)).

For an n-bit operand t compute V_j(t)=sum_i t_i*a_(j,i) mod 2^p by controlled
constant additions. Its normalized circular error from k_j*t/N is <n/2^p.
For u do the same and form the four p-bit phases

    V_j(t), V_j(u), 2V_j(t)-V_j(u), 2V_j(u)-V_j(t)  (mod 2^p).

The last two have error <3n/2^p<2^(-q-1). No modular reduction of the operands
2t-u or 2u-t modulo N is needed: their exponential phases have the required
period. Take the top q bits of each phase, and use the cosine table or its
quarter-period shift. Each trigonometric value differs from its ideal value
by at most

    eta=3*pi*2^-q+tau,  tau=2^-24.

Indeed truncating to q bits adds <2^-q turns, and cosine is 2*pi-Lipschitz.
This is valid for every record and every quantum operand's basis value.

Form the real or imaginary numerator

    Hnum=11*(C_t-C_u)+C_(2t-u)-C_(2u-t),

and clamp it to [-20*2^25,20*2^25]. Define the implemented rational score
Z_j(t,u)=y*Hnum/(10*2^25), with Z=0 on invalid positions. Clamping cannot
increase component error because the true components of h lie in [-1,1].
Scores remain in [-2,2], are exactly antisymmetric, and have a fixed common
denominator D=10*2^25. Accumulate integer numerators in a signed word of
bitlength(Q)+32 bits, which exceeds the needed 2*D*Q range. There is no
rounding in score summation or sign testing.

The expected-score observable of the complete local instrument, before its
label measurement, differs from M_tu in operator norm by at most

    beta=(12/5)*eta+4*(2^-60/Q) <1/320.

On a correct label each component error is at most (6/5)*eta, so its row
observable error is at most (12/5)*eta. Two clamped row observables differ by
norm at most 2sqrt(2)<4. Apply the uniform diagonal label-error bound of
Section 2 and triangle inequality in each k block, then take their direct
sum. On padding both are zero. The numerical inequality follows from
pi<22/7 and q=14. This is a bad-input bound, not only a clean-state estimate.

**Proved (score cost).** One pair score scan costs
O(Q*(n*p+log(Q)+1))=O(n^2 log(n+2)) gates and the same number of unaddressed
controller bit operations. Compute a term, add its numerator, and reverse its
term computation. Copy the sum's sign and reverse the full scan. Quantum
scratch is O(n): operands and class arithmetic use O(n), the phase and sum
words use O(log(n+2)), and the table workspace is constant. Constants
a_(j,i) come from sequential classical prefix-word slices; they are not
quantum-indexed reads. Computing member t=p or p+N/2 costs O(n) gates.

## 5. Simultaneous signs under the full adaptive model

**Proved (causal record lemma).** Consider the mathematical experiment that
reveals a copy's private axis and row sign immediately after its local label
instrument, before processing the next delivery, but does not give these
additional, virtual outcomes to the supplier. This experiment has the same
joint law for the actual public acquisition transcript and all final shadow
records as the physical circuit with the row records generated coherently
after acquisition. The local row instrument acts on a delivered row only.
All later supplier operations act on its private system, and all later source
processing acts on other rows and registers. These channels commute, including
on entangled malformed inputs. Later controller/supplier choices depend only
on the actual public transcript, not on the deferred row records. One may
therefore move each such local instrument backward through the later channels
one at a time, conditional on that public transcript. Private supplier outcomes
can be included in the history; countability justifies conditioning and summing.

In this causal experiment, condition on all previous real and virtual records
and supplier choices. The next clean/malformed choice is made before its
copy and before its fresh axis. At a clean choice its input is exactly rho_s
in tensor product with this history. At a malformed choice its conditional
input is arbitrary, which Section 4 permits. The branchwise count of malformed
choices is still at most r; refinement by virtual outcomes cannot violate a
cap that held on every actual branch. Hence for every fixed nonexcluded pair
(s,u), conditional means m_j satisfy

    m_j>=11/20-beta at clean positions, m_j>=-1-beta at bad positions.

In the reverse orientation the inequalities have the opposite signs. This
argument does not condition on the final bad-position set or on all labels.

**Proved (conditional exponential bound).** If Z_j is adapted and lies in an
interval of length w, D_j=Z_j-E[Z_j|past] has conditional mean zero and lies
in a translated interval of length w. Convexity bounds its conditional MGF
by exp(lambda^2*w^2/8): for interval [a,a+w] containing zero, the secant bound
gives log MGF=-h*t+log(1-t+t*exp(h)), h=lambda*w, t=-a/w. This function and
its first derivative vanish at 0, and its second derivative is at most 1/4.
Iterating conditional MGFs and applying Markov, optimized at
lambda=4*x/(Q*w^2), gives either tail bound exp(-2*x^2/(Q*w^2)). This also
proves the Bernoulli bound used for the phase tests, with w=1.

Use w=4, x=Q/64. A two-sided score deviation has probability at most
2 exp(-Q/32768)=2 exp(-6(n+32)). Union over fewer than K^2 ordered pairs
gives probability <2^-80 of a failed sign needed here: since e>2,

    2*K^2*exp(-6(n+32)) <2^(-4n-191) <2^-80.

The clean count is at least 2Q/3 on every branch. Thus on the simultaneous
event, every true-versus-other-class empirical average is strictly positive:

    (2/3)*(11/20)-(1/3)-beta-1/64
      >1/30-1/320-1/64 =7/480>0.

Its reverse score is strictly negative. Neither independence of malformed
copies nor transitivity among false candidates has been assumed.

## 6. Nested coherent search for the true class

**Proved (class tournament).** For odd N use C=N singleton classes. For even
N use C=N/2 classes {a,a+N/2}, 0<=a<C. Canonicalize each pair as a<b and let
a beat b iff some member of a has nonnegative empirical score against every
member of b; otherwise b beats a. This is one orientation per edge on every
record string, with at most four pair signs per edge. On Section 5's event
the true class beats every other class. A tournament has at most one vertex
with no incoming edge, because the mutual edge excludes two such vertices.
Define Win(v) as validity and the absence of a valid beating opponent.

**Proved (random-time sampler).** Given any exact Boolean predicate on K
addresses, initialize a uniform candidate and uniform m-bit clock j in [0,B),
apply j Grover iterations, and compute the exact predicate flag. This is a
known unitary A_0 with B-1 emitted controlled iterations. If the marked fraction
is a=sin^2 theta, summing the two-dimensional Grover rotation gives average
success 1/2-sin(4B theta)/(4B sin(2theta)). For 0<a<1,
sin(2theta)>=sqrt(2/K) and B>=4sqrt(K), so success is at least 1/4. Empty and
full predicates have success 0 and 1. The marked candidate marginal is exactly
uniform, since every marked basis amplitude is equal within each clock branch.
Diffusion uses H, the zero-state phase and H; controlled versions keep the
outer H unconditional and correct the diffusion's global minus with Z on the
control. Marking is exact compute/controlled-Z/uncompute. Clock powers emit
all their 2^ell iterations explicitly. Thus there is no powered-query oracle.

For read-only candidate v define B_v(w) to mean that v,w are valid distinct
classes and w beats v. A pair sign costs O(n^2 log(n+2)) gates (Section 4), so
an edge has that same cost. Let A_0(v) be the random-time sampler for B_v,
retaining its clock, opponent and exact base flag. It preserves v and all row
records. It uses only known gates and O(n) logical inner work.

**Proved (inner amplification and near-clean phase).** With omega=exp(i*pi/3),
let R_0 phase only the all-zero INNER work, excluding v, source data, gradient
and shared arithmetic helpers; let R_good phase inner flag 1. Recursively use
A_(j+1)=A_j R_0 A_j^dagger R_good A_j. On an initial-zero inner workspace,
if failure is z the new bad amplitude is multiplied by omega*z, because
(omega-1)^2=-omega. Thus failure is cubed. The calculation also includes z=0,1,
and holds on every read-only candidate/record block. Take L=3^d least with
L>=32n+512. The resulting A_d uses L base samplers/inverses and L-1 selective
omega phases, reusing the same inner workspace. For a nonempty opponent set,

    Pr[flag 0] <=(3/4)^L <=2^(-L/4) <=2^(-8n-128).

For an empty set flag 1 remains impossible. The circuit A_d, Z on its flag,
A_d^dagger is consequently phase +1 on empty opponent sets and approximates
phase -1 on nonempty opponent sets with vector error at most 2^(-4n-63)
on the inner-zero input subspace. This follows directly from
||(Z+I)A_d|0>||^2=4 Pr[flag 0]. A further -1 phase on validity marks exactly
Win(v). All candidate/record values are preserved, so the norm estimate extends
to arbitrary superpositions in those values with initial inner work zero.

For a controlled outer iteration, run A_d and A_d^dagger unconditionally,
controlling only the middle flag Z and the validity phase. On a disabled
control this is EXACTLY the identity even if inner work has leaked out of
zero. No controlled unknown state or approximate word is required.

**Proved (bounded outer selection).** Use 160 fresh outer clock/candidate
registers, each with the same B-1 controlled Grover iterations, substituting
the preceding near-clean phase for the exact Win oracle. After each attempt
compute a FRESH exact Win flag by scanning all K public opponent addresses,
counting incoming wins and testing zero. Reverse the scan to clear its
arithmetic. This costs O(K n^2 log(n+2)) gates per attempt, uses an O(n)-bit
loss counter and O(n) reusable scratch, and never trusts a leaked inner flag.
Retain the outer attempt's registers and verification flag. Compute the first
verified candidate into the final answer, or 0 if no verification succeeds.

First compare with an ideal outer circuit having the exact Win phase and
identity action on the inner workspace. On good row records Win has exactly
one marked item. Each attempt has success at least 1/4 and the 160 attempts
are independent conditional on these computational records; their failure is
at most (3/4)^160<2^-40. Exact verification outputs no false winner.

The comparison circuit keeps the shared inner work zero before every query.
There are 160(B-1)<2^(n+11) near-clean queries. Telescope the actual product
against the comparison product on its successive IDEAL states; each local
difference has norm at most 2^(-4n-63). All later actual gates are unitary.
Total vector error is therefore <2^(-3n-52)<=2^-55, and the outcome error is
<2^-54. This argument allows arbitrary accumulated actual inner-work leakage:
there is no reset or assumption that actual intermediate work is clean.
Separate Boolean arithmetic helpers return zero on every logical inner word
and are reusable even on such leaked states. Inner logical work itself is
retained through all attempts and through the final inverse.

The coherent row values and saved outer attempt values remain read-only to
later arithmetic. Expanding the state in these computational values and tracing
them in the answer probability removes off-diagonal terms. Therefore the
ideal comparison probability is exactly the measured-record probability used
in Section 5, including on entangled malformed states. The ideal-inner-phase
coarse failure is <2^-80+2^-40+2^-54.

The selective phase count in the physical forward U is
P=2*160*(B-1)*(L-1): each approximate Win query contains A_d and A_d^dagger.
The full verification scans contain no selective omega phases.


## 7. Counted work gradient and physical selective phases

**Proved (gradient preparation).** The ordinary work state

    gamma=G^-1/2 sum_(z<G) exp(-2*pi*i*z/G)|z>

is prepared without a source call. In each of 80 attempts initialize g qubits,
apply H and computational measurement, and discard the outcome from further
use. The reduced state is I/G, with exact ensemble
(1/G) sum_b |chi_b><chi_b| in the negative-exponent Fourier convention of
Section 2. Run the label lemma on modulus G with
J_g=max(1,g-2) and R_g=200*bitlength(16*(J_g+1)*80*2^100).
Each label error is <2^-100/80. If the estimated b is even, reset/release and
try again. For an odd b, compute b^-1 modulo G classically and apply the exact
permutation z->b*z mod G, clearing its scratch with the inverse multiplier.
On a correct label this turns chi_b into gamma. The multiplier uses two
sequences of g controlled constant additions and a swap, with O(g^2) gates
and O(g) scratch.
Explicitly, with registers (z,0), add b*z into the second register by
bit-controlled constant additions, swap the two registers, then subtract
b^-1 times the new first register from the second. The latter becomes zero
for every input z. This is a full known unitary word, not an irreversible
multiplication or an assumed XOR-output multiplier.
A single multiplier's doubled constants are kept in O(g^2) CLASSICAL bits,
reused for the inverse and the next attempt; their generation is O(g^2) bit
work before addresses. The gate stream and its literal reverse need no
quadratic quantum scratch and no inversion of modular doubling.

The all-even latent-label probability is 2^-80, and the probability of any
label error is <2^-100. On their complement the accepted reduced state is
exactly gamma and success is declared. Ignoring unused metadata, the actual
preparation output, including its failure flag, is within trace distance
2^-80+2^-100 of |success><success| tensor |gamma><gamma|. This is an
unconditional state comparison, not free postselection. Preparation is
independent of the acquired row bank. Computational measurement outcomes in
this paragraph are not used as advice or ignored when charging work. Supplier
processing of its private system after the last delivery cannot change this
reduced-state assertion: conditioned on each actual public transcript, it is
a trace-preserving operation on a disjoint system and leaves the algorithm's
reduced state unchanged. Private outcomes are averaged, never communicated
back to the algorithm. Equivalently these operations can be postponed past
all later algorithm operations, which do not use those private outcomes.

Translation by a modulo G has eigenvalue exp(2*pi*i*a/G) on gamma. Thus,
computing any Boolean predicate into a clean helper, adding floor(G/6) to
the gradient controlled by it, and uncomputing the predicate, realizes a
selective phase with error <8/G from omega. Inverses subtract the SAME
integer, so they are exact inverses of the physical gate words. Arithmetic
helpers clear for any gradient state; the gradient register is kept.

There are P=2*160*(B-1)*(L-1) selective omega phases in the forward U. On ideal gamma,
a telescoping product bound gives vector error <8P/G<2^-77 compared with
ideal omega phases, uniformly on all source/history superpositions. For an
effect E and normalized purifications x,y, the outcome difference is at most
2||x-y||, by expanding <x|E|x>-<y|E|y>. Consequently the PHYSICAL coarse
unitary on an ideal gradient has failure

    e<2^-80+2^-40+2^-54+2^-76 <2^-38.

The gradient preparation error is charged once by trace-distance contraction
through the complete remaining algorithm, not once per selective phase.

## 8. Known undo, adaptive trits and endpoint success

**Proved (unconditional reuse lemma).** Fix a classical acquisition transcript
ell, and let U_ell be the actual finite, rounded-gate unitary for its row
records and selector. The entire physical U is known from ell and public
parameters. For any purification psi of bank, ideal gradient and zero work,
write Pi_z=U^dagger P_z U for its conjugated answer projectors. Copying its
answer and applying its literal U^dagger produces

    sum_z |z> Pi_z|psi>.

The squared vector distance from |z_*>|psi>, where z_* is the fixed correct
class, is exactly 2(1-p), p=<psi|Pi_(z_*)|psi>. Apply this to the direct-sum
purification over all classical transcripts, with an orthogonal environment
copy of ell. The unconditional coarse probability from Section 7 gives
p>1-2^-38; no correctness conditioned on every label transcript is asserted.
The final joint trace distance is <sqrt(2*2^-38)<2^-18 from the original
compressed bank, original work/gradient and the correct class. Partial trace
and the final instrument contract trace distance. Retain/count residual old
work and use fresh final helpers. Only U is inverted: acquisition and label
measurements are outside it, and no input-preparation inverse is supplied.

At odd N this already gives the secret. Suppose N is even, h=N/2 and the
correct class representative is t=s mod h. On each retained row use its
classical label k_j to compute a_j=floor(G*((k_j*t) mod N)/N). Subtract a_j
from the gradient controlled by row 1. On gamma the row phase approximates
exp(-2*pi*i*k_j*t/N), with vector error <8/G per row. Across Q rows the
outcome error is <16Q/G<2^-76. All products and divisions here are classical
counted integer operations, and all physical translations are exact.

Now measure X on each row. Assign trit C on invalid flags or even k_j; on
valid odd k_j assign L for X sign +1, U for X sign -1. On an unchanged clean
row with correct label and ideal phase correction, truth s=t gives C/L
with parity-even/odd and never U. Truth s=t+h gives C/U and never L. Bad
rows give arbitrary trits but their false-trit count is at most r pathwise.

**Proved (predictable clean thinning).** Enumerate clean deliveries in order.
Each clean choice is made before the fresh latent uniform Fourier label is
drawn, so its parity is a fresh fair bit even conditional on all preceding
real and virtual records. The model enforces at least 2r clean deliveries
on every branch. Therefore the parities of the first 2r clean deliveries are
independent fair bits. One formal proof sums, for each next clean index,
over its disjoint possible preceding histories; the conditional next parity
probability is 1/2 on every such history. Induction gives probability 2^-a
for each a-bit string, for a<=2r. Adaptive choices can depend on previous
labels and outcomes but cannot inspect a clean copy before choosing it.
Extra clean deliveries can only increase the correct-trit count. This proof
uses neither a final fixed bad set nor a binomial law conditional on that set.

In the ideal unchanged-row comparison with true clean labels, the correct
count therefore dominates X~Bin(2r,1/2). Replacing these ideal labels by the
reported ones changes the complete final success probability by at most
Pr[any clean label error]<2^-60: couple the actual causal latent-label and
probe experiment, leaving all bad instruments unchanged. On the no-error
event the ideal and actual row instruments agree. This comparison does not
condition the distribution of the clean parities on successful estimation.

Return t if L>r; otherwise t+h if U>r; otherwise use a fresh fair coin.
Give L priority on both-exceed branches to make the algorithm total. In the
ideal reference no false threshold can be crossed. Its success is at least

    1/2+(1/2)*Pr[X>r]
      =3/4-(1/4)*binom(2r,r)/4^r >=23/32.

To verify the last bound, b_r=binom(2r,r)/4^r satisfies
b_(r+1)/b_r=(2r+1)/(2r+2), b_0=1, and b_r<=1/sqrt(r+1). Squaring the
induction step reduces to 3r+2>=0. Since r>=64, b_r<1/8.

The total loss from known-undo disturbance, clean label errors, final phase
rounding and gradient preparation is less than

    2^-18+2^-60+2^-76+2^-80+2^-100 <1/256.

Thus full-secret success is >183/256>11/16>2/3. This includes every failure,
every supplier allowed by the exact specification, and the clean problem.
It is unconditional, with no postselected source or uncharged restart.

## 9. Joint resources and growth indices

**Proved (quantum space).** Streaming acquisition retains Q=O(n) rows, one
position register and O(n) clean arithmetic/probe work. Row axes add O(n).
There are 160 outer clock/candidate/verification registers, each O(n) qubits;
160 is an absolute constant. The shared inner clock, opponent, flag and
fixed-point work are O(n), reused without assuming resets. Score, class and
full-verification arithmetic use O(n) clean scratch. Since
P=2*160*(B-1)*(L-1), B=2^O(n), L=O(n), the gradient width g is O(n).
Its capped preparation reuses O(n) quantum work. Retaining all old work while
adding fresh binary helpers still gives peak S_Q=O(n).

**Proved (classical space).** Q labels and prefixes use
Q*(2n+p+1)=O(n^2) bits. The fixed cosine table and its rational construction
workspace have absolute constant size. Source/gradient probe counters occupy
O(n log log(n+2)) bits. Grade-school multiplication, division and modular
inversion use O(n) scratch, with their polynomial bit work counted. A streaming
gate generator, public loop counters and O(log(n+2)) fixed-point recursion
frames fit O(n^2) classical bits. No exponential gate list, opponent list,
edge table or quantum-addressed memory is stored. Thus S_C=O(n^2), total
allocated bits/qubits M_live=O(n^2), and the address charge is O(log(n+2)).

**Proved (total work).** Each pair sign and class edge costs
O(n^2 log(n+2)) gates/controller bit operations before addresses. An inner
base sampler uses O(B) edges. Its amplification has L=O(n) base calls, so one
near-clean winner query costs O(B n^3 log(n+2)). There are 160(B-1)=O(B)
outer queries, giving O(B^2 n^3 log(n+2))=O(2^n n^3 log(n+2)) gates and
unaddressed bit operations. The 160 exact verification scans cost
O(2^n n^2 log(n+2)) and fit this bound. Forward/inverse, initialization and
answer copying change only absolute constants. The O(n)-gate selective
gradient additions and control computations fit the same count.

Source compression costs O(n^3 log(n+2)) before addresses. Gradient preparation
has constant 80 attempts on g=O(n) bits and polynomial work O(n^3 log(n+2))
or less, including measured probes, classical inverses and multipliers.
Final classical products/divisions and trit processing are polynomial within
the same envelope. Source charges Q(n+1), every measurement/reset, failed
attempt and allocated bit/qubit are included.

Ripple, comparison, table and multi-control circuits are emitted by bit loops
with O(log(n+2))-bit wire addresses. Prefix slices take O(p) operations per
constant and emit O(p)-gate additions. Local arithmetic generation is linear
in its emitted gates before the O(log(n+2)) indexing/address overhead.
The n-bit long iteration counters cost O(n) per iteration, dominated by its
edge computation. Fixed-point recursion traversal is counted by its O(L)
circuit nodes and needs no expanded circuit list. All public parameter
generation uses counted integer arithmetic. Hence all circuit generation,
classical memory access and classically addressed gates are covered by one
additional O(log(n+2)) factor, yielding T=O(2^n n^3(log2 n)^2).
Every execution branch obeys this bound, including erroneous records,
preparation failure, no verified candidate and inner-work leakage.

For B_T(n)=2^n n^3(log2 n)^2, log2 B_T=n+3log2 n+2log2 log2 n, whose
double-logarithmic growth index is 1. The n^2,n,n envelopes for classical
space, quantum space and samples have index 0. Absolute outer constants
preserve these indices. These are indices of proved upper-bound envelopes.


## 10. Dependencies

This proof restates every needed argument. The declared production dependencies
are ROB-G2, submission 55a6ce76-34af-468f-b735-a1197f3d3459 (uniform phase tests,
classical prefix words, coherent truncated phase accumulation and explicitly
counted constant-table lookup), and R24, submission
f892f7ea-957b-4dde-8374-dab2736231d0 (bounded cubic pair witness, class tournament,
known-unitary answer copying/undo and same-bank endpoint trit threshold).
The model text is identical to both dependencies. No prior acceptance is
used as a mathematical premise.
