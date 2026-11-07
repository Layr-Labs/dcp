# EP-D: exact one-third tolerance with independent-scale filtering and linear qubits

## 0. Joint theorem and single parameter rule

**Proved.** For every integer N>=2 and s in Z/NZ, set n=ceil(log2 N).
The independent-scale geometric-filter algorithm below outputs the entire s with unconditional
probability at least 11/16>2/3 under the exact model below, at epsilon(n)=1/3.
On EVERY execution branch its simultaneous bounds are

    T=O(2^(n/2)*n^(7/2)*(log2 n)^2),
    S_C=O(n^2), S_Q=O(n), Q=3*2^16*(n+32)=O(n).

All constants are absolute, independent of N, s, supplier and outcomes.
Logarithmic cost estimates use log2(n+2); the displayed asymptotic envelopes
are read for n>=2 and the single n=1 modulus has finite absolute cost.
Their exact representative-envelope growth indices are 1,0,0,0.
There is no validity threshold and no source or success postselection.

The fixed parameters are

    K=2^n; Q=3*2^16*(n+32); r=Q/3;
    q=14; p=q+3+bitlength(n); J0=max(1,n-2);
    L_F=bitlength(16*(J0+1)*Q*2^60); R_F=200*L_F;
    A_scale=2^65*ceil(sqrt(n+1)); H_filter=2048; R_verify=64n+2048;
    J_scale=max{j>=0:9^j<=K};
    B_j=least power of two >=A_scale*3^j, j=0,...,J_scale;
    m_j=log2 B_j; m=m_(J_scale); D_attempts=1024;
    g=bitlength(2^80*(Q+1)); G=2^g.

Bitlength(a)=floor(log2 a)+1 for positive integer a. The square-root ceiling
is the unique integer a>=1 with (a-1)^2<n+1<=a^2, computed by integer binary
search. After acquisition draw mutually independent uniform classical words:
H_filter words of m_j bits for each scale j, and R_verify words of m bits
for verification. All words are retained and reused across attempts and
inverse calls. Every loop has its public
finite cap. The Q source deliveries are never repeated and no source call
occurs in a unitary or its inverse.

### Exact error-model specification

Adaptive malformed-copy model with fraction epsilon(n). Parameters: N >= 2 is the modulus, s in Z/NZ the secret, n = ceil(log2 N), Q the total number of source copies the algorithm acquires, and epsilon(n) the tolerated malformed fraction. Copies are delivered one at a time in acquisition order j = 1, ..., Q. Before copy j is delivered, an adversary that knows N, s, the full description of the algorithm, and every measurement outcome the algorithm obtained before copy j is delivered, and that may hold, process and measure an arbitrary private quantum system, decides adaptively whether copy j is malformed; on every execution branch at most floor(epsilon(n) Q) of the Q acquired copies are malformed. A malformed copy is an arbitrary (n+1)-qubit state (the register shape of an ideal copy) supplied from the adversary's system: it may be pure or mixed, may be entangled with the adversary's remaining system and with other malformed copies, and may depend on all of the information above; it is not entangled with clean copies or with the algorithm's workspace, ancillas or internal random bits. Every copy that is not malformed is clean: at the moment of its delivery, a fresh ideal coset state rho_s = (1/N) sum_x |psi_{x,s}><psi_{x,s}| in tensor product with everything else (the adversary's system, all other copies and the algorithm's workspace), i.e. clean copies are independent ideal coset states. The adversary interacts with the algorithm only by supplying copies; after delivery it has no access to the copy or to the algorithm's quantum or classical systems. All measurements have countably many outcomes. The algorithm is not told which copies are malformed. Quantifiers: the guarantee must hold for every N >= 2 (no validity threshold), every s in Z/NZ and every such adversary, including the adversary that corrupts nothing (the clean problem): the algorithm outputs the entire s with probability at least 2/3, and the four declared resource bounds hold on every execution branch. The fraction bounds the number of malformed copies among acquired copies; it is not a per-copy corruption probability.

### Complete algorithm schedule

1. Acquire and compress exactly Q sources sequentially by Section 2. Keep
   each row and its classical valid flag, label and prefix word. Measure,
   reset and release its position/probe work before the next delivery.
2. After the last delivery draw the independent seed banks of Section 6 and prepare the
   ordinary work gradient of Section 7 with 80 capped attempts. On total
   gradient-preparation failure output 0, after all Q copies were acquired.
3. Apply the known exact-gate unitary U: create the coherent row/axis records
   of Section 3, run Section 6's 1024 bounded geometric-filter attempts and
   near-clean verifications, and compute the first verified class answer.
4. Copy only that answer to a fresh register, apply the LITERAL inverse U,
   retain all work, and measure the copied class. Replace an invalid class
   by 0 to make the procedure total.
5. At odd N return the singleton. At even N run Section 8's same-bank
   phase-corrected trit decision with fresh final helpers and threshold r.

For N=2 the only class representative is 0. Steps 3-4 and seed generation
are omitted; the Q rule and the gradient/endpoint procedure are unchanged.

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
quantum-indexed reads. Computing member t=c or c+N/2 costs O(n) gates.

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

## 6. Geometric filtering in one shared opponent register

### The tournament and its degree count

**Proved (class tournament).** At odd N use C=N singleton classes. At even N
use C=N/2 classes {a,a+N/2}, 0<=a<C. For canonical distinct IDs a<b, let a
beat b iff some member of a has nonnegative empirical score against every
member of b; otherwise b beats a. This is a deterministic tournament on every
record string, using at most four Section 4 pair signs per edge. On Section 5's
event the true class beats every other class: its true member beats all rival
members, and every rival member loses to the true member. There is at most
one vertex of indegree zero, since an edge between two vertices excludes two
such vertices. Write Win(v) for v<C and indegree zero. Self-pairs are explicitly
rejected by the equality test [v=w], and padding IDs are invalid.

Let K=2^n. For any real d_0>0, fewer than 2d_0+1 vertices have indegree <d_0.
Indeed, for a nonempty set of h such vertices, its h(h-1)/2 internal incoming
edges are no more than its total indegrees, which are <h*d_0. On a record
string with a source, subtracting that source shows that fewer than 2d_0
FALSE vertices have indegree <d_0. This uses no transitivity among the false
vertices.

### Reflections, checked trials, and a reversible stopping code

Use an opponent register of n+1 qubits, with M_op=2K addresses. Define D_v(w)
to mean that v<C, w<C, w!=v and w beats v. Thus the extra K addresses are
unmarked, and a valid vertex with indegree d has marked fraction a=d/M_op<1/2.
Each D evaluation has O(n^2 log(n+2)) gate/controller cost and O(n) reusable
scratch by Section 4. Its validity and self-equality gates cost O(n).

Let |u_1>,|u_0> be uniform marked and unmarked vectors. With sin^2(theta)=a,
the initial uniform opponent is cos(theta)|u_0>+sin(theta)|u_1>. The mark is
diag(1,-1) in this basis. Diffusion 2|uniform><uniform|-I is the matrix
[[cos(2theta),sin(2theta)],[sin(2theta),-cos(2theta)]]. Their product is the
rotation [[cos(2theta),-sin(2theta)],[sin(2theta),cos(2theta)]]. Consequently
j Grover iterations on |u_0> give marked probability sin^2(2j theta).
Both reflections preserve span{|u_0>,|u_1>}, which justifies this restriction.
A failed exact check projects back onto |u_0>, up to the real scalar factor
cos(2j theta).
An initial exact check on the uniform opponent has the same failed direction.
For d=0 the uniform opponent is unchanged and no check succeeds.

All checks are coherent. Retain one binary stopping code z, initially 0.
Code 0 means live; code 1 records invalid v; code 2 records a marked initial
opponent. Every later trial has its own distinct nonzero code. A trial applies
its Grover iterations only when z=0, then records its code when its opponent
is marked. It freezes all earlier stopped branches. This is implemented on
EVERY logical word by the following permutation: conditional on D_v(w)=1
and z in {0,c}, XOR the trial's constant c into z. It exchanges 0 and c,
fixes every other code, and preserves the condition z in {0,c}. Thus its
Boolean helper can be uncomputed after the exchange. The initial invalid
check uses the same exchange with c=1 and predicate v>=C. The initial
opponent check uses c=2. No overwrite, irreversible assignment or measurement
is hidden in the stopping rule. Comparisons and guarded XORs use O(log(n+2))
gates apart from the edge predicate. All helpers clear on every input word.

For j uniform in [0,B), the mean marked probability starting from |u_0> is
at least 1/2-1/(2B sin(2theta)). To see this, use sin^2 x=(1-cos(2x))/2 and
sum exp(4ij theta). The geometric sum has modulus
|sin(2B theta)/sin(2theta)|<=1/sin(2theta). Equivalently its real sum
follows by telescoping the sine addition formula. Since a<=1/2,
sin(2theta)=2sqrt(a(1-a))>=sqrt(2a). If B>=4/sqrt(a), the mean marked
probability is at least 1/4. Empty predicates never stop.

### Independent post-acquisition seeds and a smaller scale multiplier

Set

    A_scale=2^65*ceil(sqrt(n+1)); H_filter=2048;
    R_verify=64n+2048; J_scale=max{j>=0:9^j<=K};
    B_j=least power of two >= A_scale*3^j, j=0,...,J_scale;
    m_j=log2 B_j; m=m_(J_scale).

After acquisition, draw mutually independent uniform classical words
b_(j,h) of m_j bits for 0<=j<=J_scale and 1<=h<=H_filter, and separate
independent uniform m-bit words c_1,...,c_(R_verify). These are read-only
inputs to every subsequent unitary. Trial (j,h) uses exactly b_(j,h) Grover
iterations. Verification uses exactly c_h iterations per trial. The words
are fixed across all attempts, inverses and recursive invocations; no
fresh draw is made during a unitary. Independence is asserted across the
initial word draws, including across scales. All seed bits are sampled
by H and measurement after the final delivery, with the work charged.
Their total number is H_filter*sum_j m_j+R_verify*m=O(n^2).

For every acquisition transcript these fresh draws are independent of the
bank and of the conceptual row records. Any later supplier operations,
even if chosen using revealed classical outcomes, act only on its disjoint
private system. After averaging private outcomes they preserve the bank's
reduced state separately for every seed value. There are no further
deliveries or communicated private outcomes. Thus they cannot spoil the
fixed-record independent-seed average used below.

An unamplified tester F_j begins with uniform v in K addresses and uniform w
in M_op addresses, applies the invalid and initial opponent checks, then
performs H_filter checked trials at each scale 0,...,j. Let E_i denote the
scale-i trial block. Its trial h has code 3+i*H_filter+(h-1). The stopping
code needs ceil(log2(3+(J_scale+1)*H_filter))=O(log(n+2)) qubits. Neither
a clock register nor an independent opponent register is retained per trial.
Let q_j be F_j's live probability, and q_j^false its live probability on
false valid candidates. Fix any record string with unique source v_*.
The source is always live and contributes exactly 1/K to q_j.

**Proved (independent-scale first moment).** Put delta_f=(3/4)^H_filter and
set d_i=32K/B_i^2=16M_op/B_i^2. For a fixed candidate with indegree d>0,
a=d/M_op, the initial failed check has survival 1-a. Each later failed
check returns its opponent to the same uniform unmarked direction.
Consequently its live probability for fixed classical times is exactly

    (1-a)*product_(i=0)^j product_(h=1)^H_filter
                  cos^2(2*b_(i,h)*theta),   sin^2(theta)=a.

All these factors are nonnegative and at most 1. If d>=d_i, then
B_i>=4/sqrt(a); averaging the independent times of that scale bounds its
survival factor by delta_f. For the first such scale i_0<=j, all later
scales also qualify. Independence ACROSS scales therefore bounds its
expected survival by delta_f^(j-i_0+1). This uses independence at a fixed
record string, before any selection of a seed event.

Partition the false vertices into those with d<d_j, those whose first
qualifying scale is i=1,...,j, and those already qualifying at scale 0.
The first group has fewer than 2d_j vertices. The scale-i group has
fewer than 2d_(i-1) vertices by its upper degree bound, and the last group
has fewer than K vertices. The degree-count lemma gives

    E_b q_j^false
      <=64/B_j^2 + sum_(i=1)^j [64/B_(i-1)^2]*delta_f^(j-i+1)
                    +delta_f^(j+1).

This remains valid when a threshold is below 1: every false vertex has
integer indegree at least 1, and the corresponding low-degree group is
empty. Power-of-two rounding gives

    B_j/B_(i-1) < 2*3^(j-i+1).

Writing t=j-i+1 and summing a geometric series yields

    E_b q_j^false
      <=(64/B_j^2)*(1+4*sum_(t>=1)(9*delta_f)^t)
                    +delta_f^(j+1)
      <128/B_j^2+delta_f^(j+1).

Indeed (3/4)^4<1/2 implies delta_f<2^-512; in particular
1+36*delta_f/(1-9*delta_f)<2. The additive tail now decays with the
number of scales, rather than being paid independently at every scale.

Let Z=sum_(j=0)^(J_scale-1)9^j*q_j^false, empty when J_scale=0.
Since A_scale^2>=2^130*(n+1) and J_scale<=n,

    E_b Z <=128*J_scale/A_scale^2+delta_f/(1-9*delta_f)
           <2^-123+2^-511<2^-122.

Markov's inequality gives Pr_b[Z>1/64]<2^-116. This bound is uniform over
fixed record strings having a source. It is averaged over post-acquisition
classical randomness, not a simultaneous certificate for all records at
one seed and not an assertion conditioned on the final malformed positions.

### A fixed amplification schedule with no estimates or histories

All reflection identities in this subsection are first proved at a fixed
record string and seed. Their physical circuits are block diagonal in those
read-only records and preserve every other attempt and its environment.

For a state-preparation unitary V on the attempt registers, define

    Trip(V)=V R_zero V^dagger O_live V,
    R_zero=2|0><0|-I,  O_live=I-2 P_[z=0].

Operator products in this definition compose RIGHT TO LEFT: apply V, then
O_live, then V^dagger, R_zero, V. The zero reflection excludes the read-only
row records, gradient, classical inputs and the other attempts. It acts on
this attempt's candidate, opponent and stopping registers. Clean Boolean
helpers can be excluded; they clear on every invocation. Both reflections
have O(n) exact Clifford+T implementations. Implement R_zero as the negative
of the zero-state sign flip; an unconditional -1 is X,Z,X on a helper in
|0>, which returns that helper to |0>. This fixes all global signs literally.

If psi=V|0> and p=||P_live psi||^2, direct expansion gives

    P_live Trip(V)|0>=(3-4p) P_live psi.

Indeed V R_zero V^dagger=2|psi><psi|-I and
<psi|O_live|psi>=1-2p. Projecting
2(1-2p)psi-O_live psi onto live gives the stated factor. This is a statement
about a reflection around one prepared vector, and does not require the
live subspace to be one dimensional.

Define V_0=F_0 and V_j=E_j Trip(V_(j-1)) for j=1,...,J_scale.
This is also an operator product: apply Trip(V_(j-1)) first, then E_j.
All invocations
reuse the SAME attempt registers and arithmetic helpers. This is a finite
recursive gate word, not a measured or adaptive recursion. Its classical
emitter uses O(n) recursion frames of O(log(n+2)) bits, and stores no expanded
circuit. For its prepared state let p_j be the live probability. Because E_j
never returns a stopped branch to live on the reachable forward states,
induction gives the exact identity

    P_live V_j|0> = [product_(h<j)(3-4p_h)] P_live F_j|0>.

To justify the reachability assertion, Trip(V_(j-1))|0> is a linear
combination of V_(j-1)|0> and O_live V_(j-1)|0>; it creates no new code
values. Earlier nonzero codes differ from every code in E_j. Thus E_j only
filters the previous live component. Its later stopped components cannot
interfere into the live subspace. The direction equality holds on arbitrary
false-edge orientations and on each fixed row-record block.

Since |3-4p|<=3, p_j<=9^j q_j. On a seed with Z<=1/64,

    sum_(h<J_scale) p_h <=(9^J_scale-1)/(8K)+Z <1/8+1/64=9/64.

Every factor 1-(4/3)p_h is positive. The elementary product inequality
product(1-x_h)>=1-sum x_h for x_h in [0,1], proved by induction, yields

    product_(h<J_scale)(3-4p_h) >=3^J_scale*(13/16).

The source's opponent remains uniform and live throughout F_(J_scale). Therefore
V_(J_scale) returns v_* with probability at least

    (169/256)*9^J_scale/K >169/2304 >1/16.

For J_scale=0 the empty product is 1 and this bound also holds. No stage measures
its candidate, estimates p_j, or keeps a prior candidate or phase cache.

### A near-clean verification with the same register-saving trials

For read-only v let W_v act on a SEPARATE shared verification opponent/code
workspace: prepare uniform w in M_op, make the invalid and initial checks, and
perform only R_verify trials of length c_h, with distinct codes
3,...,R_verify+2.
Let its output predicate be z=0 AND v<C. For the source it is exactly 1;
for invalid v it is exactly 0. For any valid nonsource the expected
false-accept probability is at most delta_v=(3/4)^R_verify, because its
indegree d>=1 gives a=d/M_op>=1/M_op and 4/sqrt(a)<=4sqrt(M_op), while
B_(J_scale)>=A_scale*3^J_scale>A_scale*sqrt(K)/3>4sqrt(M_op).

Set delta_det=2^(-8n-256). Union and Markov bounds over at most K valid
nonsources show that, except for a seed event of probability at most

    K*delta_v/delta_det <2^(-7n-256),

every nonsource's false-accept probability is <=delta_det. Here
(3/4)^4<1/2 gives delta_v<2^(-16n-512). Together with
Z<=1/64, the total bad-seed probability is <2^-110 for every fixed good
record string. The independent verification seed bank obeys this bound at each fixed
record string. No independence between the two good-seed events is needed
for their union bound.

Run W_v, XOR its output predicate into a fresh verification bit, and run
W_v^dagger. If its deterministic correct predicate value is x, its output
on verification bit 0 and inner work 0 differs from |x>|0> by squared norm
exactly 2*Pr[wrong predicate]. This follows by writing the conjugated
orthogonal predicate projectors, as in Section 8. Thus this physical
verification is within vector error

    sqrt(2*delta_det)<2^(-4n-127)

of XOR by Win(v) with clean inner work, on the initial-inner-zero subspace.
The estimate extends to all superpositions of v because those blocks are
orthogonal, including entanglement with the attempt's retained opponent/code.
There is no phase synthesis in this construction. Arithmetic helpers are
clean on every logical word, and the shared logical verification work is
retained even when it leaks from zero.

### Complete bounded coarse selector and its error

Make exactly D_attempts=1024 attempts. Each uses fresh candidate/opponent/code
registers and applies V_(J_scale), then the preceding verification with a fresh output
bit. All attempts share the one verification workspace. Retain their registers
and bits. Compute the first verified candidate into the answer, or 0 if none;
the Boolean first-verified flags are computed/uncomputed with O(D_attempts*n)
work and space. Include validity explicitly. This defines a total unitary on
every record string and seed, whether a source exists or not.

For comparison replace each verification by exact XOR Win and identity on
its inner work. At fixed good records and good seed, each fresh V_(J_scale) has
source probability >1/16, and false candidates never verify. The probability
all 1024 attempts miss is <(15/16)^1024<2^-64, since (15/16)^16<1/2.
The ideal comparison circuit keeps verification work zero after every call.
Telescoping the actual circuit against the ideal one on the successive IDEAL
states gives total vector difference

    <1024*2^(-4n-127)=2^(-4n-117)<=2^-121.

All later actual gates are unitary, so actual accumulated verification leakage
does not invalidate this bound. For normalized vectors x,y and any effect E,
expanding their expectations gives a probability difference <=2||x-y||.
The verification loss is consequently <2^-120.

Fixing and tracing the row-record computational values removes their
inter-block coherences in answer probabilities: every selector operation
preserves those values, including its zero reflections. The causal measured
record law of Section 5 therefore gives the physical circuit's unconditional
coarse failure, averaging acquisition transcripts, records and classical seed:

    e <2^-80+2^-110+2^-64+2^-120 <2^-60.

This proof uses no measurement of the row records and no inverse acquisition.
It is the failure probability of the actual exact-gate unitary. The source
bank is reused only through the known-unitary identity of Section 8.


## 7. Counted work gradient and the physical coarse unitary

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

Translation by a modulo G has eigenvalue exp(2*pi*i*a/G) on gamma.
A controlled addition therefore implements the corresponding controlled phase
while preserving gamma. The endpoint uses these translations with rounded
classical phase numerators. Every physical addition and its inverse is an
exact known Clifford+T word.

The coarse unitary uses only exact row-basis gates, Boolean edge arithmetic,
Grover reflections and reversible stop-code permutations. It does not use
the gradient. Section 6 bounds its ACTUAL physical unconditional error by

    e<2^-60.

Gradient-preparation error is charged once by trace-distance contraction
through every later operation, including the final row corrections.

## 8. Known undo, adaptive trits and endpoint success

**Proved (unconditional reuse lemma).** Fix a classical transcript
(ell,b), consisting of the acquisition transcript ell and ALL
post-acquisition seed words b. Let U_(ell,b) be the actual finite exact-gate
unitary for its row records and selector. The entire physical U is known from (ell,b) and public
parameters. For any purification psi of bank, ideal gradient and zero work,
write Pi_z=U^dagger P_z U for its conjugated answer projectors. Copying its
answer and applying its literal U^dagger produces

    sum_z |z> Pi_z|psi>.

The squared vector distance from |z_*>|psi>, where z_* is the fixed correct
class, is exactly 2(1-p), p=<psi|Pi_(z_*)|psi>. Apply this to the direct-sum
purification over all acquisition transcripts and seed words, with an orthogonal environment
copy of (ell,b). The unconditional coarse probability from Section 7 gives
p>1-2^-60; no correctness conditioned on every label transcript is asserted.
The final joint trace distance is <sqrt(2*2^-60)<2^-29 from the original
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

Let n_L,n_U,n_C be the numbers of the three trits.
Return t if n_L>r; otherwise t+h if n_U>r; otherwise use a fresh fair coin.
Give L priority on both-exceed branches to make the algorithm total. In the
ideal reference no false threshold can be crossed. Its success is at least

    1/2+(1/2)*Pr[X>r]
      =3/4-(1/4)*binom(2r,r)/4^r >=23/32.

To verify the last bound, b_r=binom(2r,r)/4^r satisfies
b_(r+1)/b_r=(2r+1)/(2r+2), b_0=1, and b_r<=1/sqrt(r+1). Squaring the
induction step reduces to 3r+2>=0. Since r>=64, b_r<1/8.

The total loss from known-undo disturbance, clean label errors, final phase
rounding and gradient preparation is less than

    2^-29+2^-60+2^-76+2^-80+2^-100 <1/256.

Thus full-secret success is >183/256>11/16>2/3. This includes every failure,
every supplier allowed by the exact specification, and the clean problem.
It is unconditional, with no postselected source or uncharged restart.

## 9. Joint resources and growth indices

All counts below are worst-case public bounds, including malformed inputs,
bad seeds, leaked verification work, preparation failure and incorrect answers.
There is exactly one algorithm and the single parameter rule of Section 0.

**Proved (quantum space).** Streaming acquisition retains Q row qubits and
one O(n)-qubit position/probe workspace. Coherent axes add Q qubits. Each of
1024 retained attempts has an n-bit candidate, an (n+1)-bit opponent, an
O(log(n+2))-bit stopping code and a verification bit. Their TOTAL is O(n),
because 1024 is an absolute constant. Their count does not grow with J_scale, H_filter or R_verify.
One shared verification opponent/code workspace uses O(n) qubits, including
any actual leakage. Edge, phase, accumulator and arithmetic helpers use O(n)
qubits; zero-reflection helpers use O(n). The recursion creates no quantum
stack or per-level sampler. The endpoint gradient uses O(log(n+2)) qubits.
Retaining the old work and adding answer-copy and fresh endpoint helpers
therefore gives peak S_Q=O(n) on every branch.

**Proved (classical space).** Labels, valid flags and prefix words occupy
Q*(2n+p+1)=O(n^2) bits. The filter seed words take
H_filter*sum_(j=0)^J_scale m_j=O(n^2) bits, because H_filter is an absolute
constant, J_scale=O(n) and m_j=O(n). The verification seeds take
R_verify*m=O(n^2) bits. Storing all B_j and powers 3^j uses O(n^2) bits;
they are public constants generated by integer arithmetic, not advice.
The fixed cosine table and its rational construction have absolute constant
size. Acquisition counters need O(n log log(n+2)) bits. Grade-school integer
arithmetic uses O(n) scratch. The gradient multiplier constants occupy
O(g^2)=O(log^2(n+2)) classical bits, with O(g) decoded digits. The recursion
emitter has O(n) frames, each holding a level index, direction and one of a
fixed number of program locations, O(log(n+2)) bits per frame. A leaf trial's
O(n)-bit iteration counter is reused; no child recursion occurs inside a
trial. Public attempt/record/bit counters and gate descriptions fit O(n^2).
No contender list, edge table, phase history or expanded circuit is stored.
Thus S_C=O(n^2), the total live allocated memory is O(n^2), and the required
address charge is O(log(n+2)) per operation.

**Proved (work).** Let c_edge=O(n^2 log(n+2)) be Section 4's unaddressed
edge cost, including controller work. A controlled opponent Grover iteration
costs O(c_edge+n): exact edge compute/phase/uncompute and controlled diffusion
on n+1 qubits. Implement controlled diffusion with unconditional H gates,
a controlled zero phase and unconditional H gates; Z on the unchanged active
control corrects its controlled global minus. Every trial emits its entire
classical iteration count and an exact check, including on stopped quantum
branches. All stop-code helpers are computed/uncomputed with counted gates.

The square-root ceiling satisfies sqrt(n+1)<=ceil(sqrt(n+1))<sqrt(n+1)+1,
so A_scale=O(sqrt(n)). Since B_j<2*A_scale*3^j and H_filter=2048 is constant,
the work of E_j is

    O(H_filter*B_j*(c_edge+n))
       =O(A_scale*3^j*n^2 log(n+2)).

The initial uniform preparation, validity and initial check fit this bound.
For t_j the work of V_j, the literal recursive gate word obeys

    t_0=O(A_scale*n^2 log(n+2)),
    t_j<=3t_(j-1)+O(A_scale*3^j*n^2 log(n+2)).

Induction gives t_j=O((j+1)*3^j*A_scale*n^2 log(n+2)). Hence all 1024
V_(J_scale) calls cost O(2^(n/2)*n^(7/2) log(n+2)), because
J_scale<=n and 3^J_scale<=sqrt(K). Each W_v verification and its inverse
costs O(R_verify*B_(J_scale)*(c_edge+n))
=O(2^(n/2)*n^(7/2) log(n+2)) as well. First-verified selection, answer
copying and the literal inverse of the entire coarse unitary add a constant
factor or polynomial work. These are worst-case public bounds, not mean
costs over random times, successful seeds or source records.

All seed slices, iteration counts and public bounds have O(n) bits.
Counting/emitting an iteration costs O(n) controller bit work, dominated
by c_edge. Current trial/level code computation, seed access and recursion
entry/exit fit the corresponding trial or node cost. Each frame holds only
a level, direction and local program location; an O(n)-bit leaf iteration
counter is shared by all leaves. The phase/score Boolean gate templates are
emitted from finite local loops, with literal reversal when required.
Public B_j values and powers are generated by counted repeated multiplication
and power-of-two rounding, in O(n^3) bit work or less. The square-root ceiling
is computed by binary search with exact integer squaring in polynomial work
and O(n) scratch. All seed generation and initialization costs O(n^2).
Classical wire addresses and record indices have O(log(n+2)) bits, so a
single such factor covers gate generation/addressing. Quantum address
superpositions do not access a memory primitive: the edge always scans the
classical records and the fixed cosine table explicitly.

Acquisition costs O(n^3 log(n+2)) before addresses: R_F=O(log(n+2)) probes
per phase level per offset, O(n) levels, O(n) gates per probe, Q=O(n)
sources; exact dyadic reconstruction and binary long division fit that bound.
Gradient preparation, initialization, seed generation, measurements/resets,
source charges Q(n+1), and final classical products/divisions are polynomial
and fit the same exponential envelope. The 80 gradient attempts are capped.
No source is acquired in V_j, W_v, their inverses or any restarted search.
Thus the charged joint bound is

    T=O(2^(n/2)*n^(7/2)*(log2 n)^2),
    S_C=O(n^2), S_Q=O(n), Q=3*2^16*(n+32)=O(n).

The displayed big-O is read for n>=2; the single n=1 modulus N=2 has the
specified finite absolute cost and the same Q rule. For its coarse class
there is only one possibility, so no selector or seed is needed.

For B_T(n)=2^(n/2)n^(7/2)(log2 n)^2,
log2 B_T=n/2+(7/2)log2 n+2log2 log2 n, and
log2(log2 B_T)/log2 n tends to 1. For n^2,n,n the same ratio in the rules'
max{4,B} convention tends to 0. Absolute outer constants preserve these
values. These prove exact representative-envelope growth indices 1,0,0,0;
no matching lower bound on actual work or storage is asserted.

## 10. Dependencies, comparisons and scope

**Proved (scope and attribution).** The production dependencies are ROB-G2
(55a6ce76-34af-468f-b735-a1197f3d3459), R24
(f892f7ea-957b-4dde-8374-dab2736231d0), EP-A
(493303b5-06f6-4ee0-9596-d8cae89c8bb4), and EP-B
(49ed28c4-0baf-44d8-a7be-cfbb7c262761). ROB-G2 supplies the measured-label
phase tests, classical binary-prefix interface and counted table arithmetic.
R24 supplies the cubic bounded pair witness, class grouping and same-bank
copy/undo with the trit endpoint. EP-A combines these at exactly one third.
EP-B, "EP-B: exact 1/3 adaptive malformed-copy tolerance with linear qubits,
O(2^n n^3 log^2 n) work",
supplies Section 4's direct-prefix arithmetic for BOTH quantum pair operands,
Section 5's role-free score signs and its 2K^2 union count, and the class
edge interface. These ingredients are restated and proved here.

The immediate selector baseline is EP-C (exact 1/3 with linear qubits at
2^{n/2} n^5 log^2 n). Its geometric filtering, reversible stopping codes,
fixed tripling, shared-work verification and same-bank endpoint are restated
in this proof. The present changes are independent trial seeds across scales,
constant filter repetitions, the first-qualifying-scale survival bound,
and A_scale=Theta(sqrt(n)). The repeated verification trials still grow
linearly with n. No theorem is imported merely because it was accepted.
The fixed tripling identity and every application are proved directly.
Generic square-root query bounds for tournament winners are not claimed as
new.

For the declared envelopes, this point strictly dominates EP-C: time changes
from O(2^(n/2)n^5 log^2 n) to O(2^(n/2)n^(7/2) log^2 n) and the other
resources and exact tolerance match. Relative to EP-A it has lower quantum
space and a worse time polynomial. Relative to ROB-G2 it has larger
fractional tolerance, 1/3 rather than 3333/10000, and a worse time polynomial.
No claim of dominance over those two points, a linear-classical-space bound,
practical small constants or an exhaustive current frontier is made.
