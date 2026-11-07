# Exact one-third tolerance under a joint clean marginal in linear quantum space

This is one complete algorithm, named LQ-MARGINAL. Its required evidence is
[this main proof](linear_quantum_marginal.md),
[the selected literal controller](linear_quantum_marginal_controller.md),
[the complete deterministic filter proof](linear_quantum_marginal_filter.md),
and [the complete joint-input and endpoint proof](linear_quantum_marginal_model.md).
All five claims cite all four files. They include every needed source,
channel, score, statistical, circuit, controller, precision and endpoint proof.
Section 10 gives exact direct sources and inherited credits.

## 0. Joint theorem and single parameter rule

**Proved.** For every integer N>=2 and s in Z/NZ, set n=ceil(log2 N).
The LQ-MARGINAL deterministic-filter algorithm below outputs the entire s with unconditional
probability at least 11/16>2/3 under the exact model below, at epsilon(n)=1/3.
On EVERY execution branch its simultaneous bounds are

    T=O(2^(n/2)*n^(7/2)*(log2 n)^2),
    S_C=O(n^2), S_Q=O(n), Q=3*2^16*(n+32)=O(n).

All constants are absolute, independent of N, s, input state and outcomes.
Logarithmic cost estimates use log2(n+2); the displayed asymptotic envelopes
are read for n>=2 and the single n=1 modulus has finite absolute cost.
Their exact representative-envelope growth indices are 1,0,0,0.
There is no validity threshold and no source or success postselection.

The fixed parameters are

    K=2^n; Q=3*2^16*(n+32); r=Q/3;
    q=14; p=q+3+bitlength(n); J0=max(1,n-2);
    L_F=bitlength(16*(J0+1)*Q*2^60); R_F=200*L_F;
    a_n=least positive integer with a_n^2>=n+1;
    A_scale=2^64*a_n; R_v=4n+128;
    L=max{j>=0:9^j<=K};
    B_j=least power of two >=A_scale*3^j, j=0,...,L;
    b_j=log2 B_j; S_j=sum_(i<j)b_i; D_attempts=1024;
    g=bitlength(2^80*(Q+1)); G=2^g.

Put M=2K and ell=log2(n+2). Bitlength(a)=floor(log2 a)+1 for positive
integer a. Every loop has its
public finite cap. No selector seed or random Grover time is used. Each E_j
has two dyadic blocks; the shared verifier has R_v single blocks at B_L.
The Q source deliveries are never repeated and no source call occurs in a
unitary or its inverse. Compute a_n exactly by binary search with schoolbook
squares. The actual B_j, b_j, codes and every emitted power use this one rule.
The complete deterministic proof is in
[the filter appendix](linear_quantum_marginal_filter.md), Sections 2--10.
All repeated gates use the actual online controller in
[the controller appendix](linear_quantum_marginal_controller.md), Section 3.
It uses ready operand addresses, marked scans and counted pointer carries;
no constant-cost gate-emission assumption is made.

### Exact error-model specification

Among the Q acquired copies, an adversary fixes a set B of at most floor(epsilon(n) Q) malformed positions, possibly depending on N and s. The joint state is arbitrary subject to its reduced state on all other positions being exactly rho_s^{tensor (Q-|B|)}. Malformed systems may be correlated or entangled with each other and with other systems subject to that marginal promise. No source control, purification access, or preparation inverse is supplied.

The ideal state is

    rho_s=(1/N) sum_(x=0)^(N-1) |psi_(x,s)><psi_(x,s)|,
    psi_(x,s)=(|0,x>+|1,(x+s) mod N>)/sqrt(2).

Here epsilon(n)=1/3 and r=Q/3 is an integer. For each fixed-B input
component sigma_HBR, H is the good set and R is any inaccessible reference.
Its only clean constraint is Tr_(BR) sigma=rho_s^(tensor |H|). In particular,
H may be entangled with BR. Convex mixtures with different B are allowed:
uniform success extends by linearity, and branch resource caps are fixed.
The algorithm is given neither B nor R.

All Q raw registers are fixed jointly before delivery. The inaccessible
source holds unread registers passively and releases them in the fixed
acquisition order. It makes no replacement, measurement, feedback choice,
or later transformation. Only acquired registers enter algorithm storage.
The rules exclude state held by the inaccessible source. Each delivery
still costs n+1 source work units and counts once in Q. Every acquired row
and the current position/probe work is charged. Conditional states of
unread systems can change after measurements; the input promise is on the
original joint state, not on those conditional states. Model Sections 1--2
prove the component reduction and physical delivery/memory interpretation.

### Complete algorithm schedule

1. Acquire and compress exactly Q sources sequentially by Section 2. Keep
   each row and its classical valid flag, label and prefix word. Measure,
   reset and release its position/probe work before the next delivery.
2. After the last delivery prepare the ordinary work gradient of Section 7
   with 80 capped attempts. On total
   gradient-preparation failure output 0, after all Q copies were acquired.
3. Apply the known exact-gate unitary U: create the coherent row/axis records
   of Section 3, run Section 6's 1024 bounded deterministic-filter attempts and
   near-clean verifications, and compute the first verified class answer.
4. Copy only that answer to a fresh register, apply the LITERAL inverse U,
   retain all work, and measure the copied class. Replace an invalid class
   by 0 to make the procedure total.
5. At odd N return the singleton. At even N run Section 8's same-bank
   phase-corrected trit decision with fresh final helpers and threshold r.

For N=2 the only class representative is 0. Steps 3-4 and all selector probes
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

## 2. Streaming compression of the fixed joint input

**Proved (source decomposition).** With

    chi_k=N^-1/2 sum_(x<N) exp(-2*pi*i*k*x/N)|x>,
    phi_(k,s)=(|0>+exp(2*pi*i*k*s/N)|1>)/sqrt(2),

expansion of the ideal coset mixture gives

    rho_s=(1/N) sum_(k<N)
        |phi_(k,s)><phi_(k,s)| tensor |chi_k><chi_k|.

Translation by a has eigenvalue exp(2*pi*i*k*a/N) on chi_k.
For each delivery j, measure a valid-position flag v_j. On valid positions
run Section 1's fixed repeated label test with J0,R_F; decode k_j in [0,N).
On invalid positions set k_j=0. Retain the row. Measure/reset/release all
position and probe work. Store v_j,k_j and the exact classical prefix

    e_j=floor(2^(n+p)*k_j/N),

using binary long division. Probe outcomes and counts are charged; unused
fine outcomes are not used by any later gate after count/label/reset.
The label lemma gives the uniform error

    Pr[k_j!=k | true position eigenlabel k]
       <16*(J0+1)*2^-L_F <delta_F=2^-60/Q.

Here exp(-L_F)<2^-L_F and the bitlength inequality is strict.

**Proved (full-input retained channel).** For each complete valid probe
outcome a its position operator is K_a=sum_k c_a(k)|chi_k><chi_k|,
acting as identity on row and every external system. If d(a) is the total
decoder, put p(ell|k)=sum_(a:d(a)=ell)|c_a(k)|^2. For arbitrary row/position/
reference input tau, the retained valid branch is exactly

    A_ell(tau)=sum_(k<N) p(ell|k)
        (I_rowR tensor <chi_k|)tau(I_rowR tensor |chi_k>).

Partial trace of the released position kills cross-k terms by Fourier
orthogonality. The invalid branch is the padded-block partial trace with
v=0 and zero label/prefix. The validity measurement removes valid/padding
cross terms. This is an identity of channels with an arbitrary reference;
it is not restricted to clean inputs or score expectations.

Model Section 3 supplies the full derivation and the exact hidden true-k
refinement obtained from this channel. The original product good marginal
gives uniform independent good hidden labels and pure rows phi_(k,s),
with arbitrary bad/reference extension. Uniform delta_F and a union bound
give unconditional probability <2^-60 of any good decoding error. No
probability is conditioned on all labels, on unused reset outcomes, or on
successful label estimation. The actual sequential instrument is unchanged.

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
The actual literal generator is the controller appendix, Section 3. Its
complete slice event costs O(p+a_addr) raw bit/head actions, including
address setup, known-bit preparation, controlled ripple, cleanup and
reverse, where a_addr=O(log(n+2)). This proves the stated complete raw
edge/controller count before the single final address charge. The
reusable p-bit addend and control remain within O(n) quantum scratch.

## 5. Simultaneous signs from the product good marginal

**Proved.** Combine each slot's compression and its fresh X/Y row-record
instrument. These local instruments commute on different raw slots, even
for an entangled input. Thus their common measured-record law is unchanged
if the proof reveals all good records first and bad records afterward.
The physical algorithm uses its fixed streaming order and deferred coherent
row records. It does not know B or store the proof order.

In the good-first order, good outcome marginals are the product clean law.
For any fixed pair (s,u) outside the true class, Section 4's full-input
observable error beta<1/320 gives conditional means >=11/20-beta on each
good slot. After all good records, every subsequent bad conditional state
is arbitrary and its mean is >=-1-beta. The complete next local instrument,
including its fresh axis and decoded label, is averaged in this bound.
Do not condition all physical bad labels before a good mean is evaluated.
The product marginal was promised only for the original joint input.

Hence the sum of the Q conditional means is at least Q*(1/30-beta).
Each centered score increment has conditional mean zero and interval
width 4. The complete conditional exponential proof in model Section 5
gives either tail exp(-2*x^2/(16Q)). It also proves the width-1 Bernoulli
estimate used by Section 1's label tests. Set x=Q/64 and use the reverse
orientation when needed. Fewer than K^2 ordered comparisons are required.
Their simultaneous failure probability is less than

    2*K^2*exp(-Q/32768)
      =2*K^2*exp(-6*(n+32))<2^-80.

Outside that event, every true-versus-other-class empirical average is
strictly positive, since

    1/30-beta-1/64 > 1/30-1/320-1/64=7/480>0.

Its reverse is strictly negative. Model Sections 4--5 prove the exact
record-law identity, all conditional bounds, exponential iteration and
union bound, with arbitrary bad-good/reference entanglement. Neither
independence of bad slots nor transitivity of false edges is assumed.

## 6. Deterministic phase filtering in one shared opponent register

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

### Selected parameters and registers

Use the exact Section 0 parameter rule, with M=2K and the class rule above.
Each attempt retains candidate v, opponent w, stopping code z, one logical
probe and a fresh verification-output bit. The shared verifier has its own
opponent/code/probe. All are allocated and retained, including actual
leakage. The full rule is also stated in filter Section 2. Logical probes
are separate from clean Boolean helpers; no reset is assumed on arbitrary
logical inputs. For N=2 this selector and its probes are omitted.

### The literal Grover sign and the symmetric probe

For a fixed candidate v and fixed computational row-record string, let
D_v(w) mean v<C, w<C, w!=v, and w beats v in the source's class tournament.
The predicate uses at most four source pair signs, has reusable linear
quantum scratch, and is exact for every record string. Let d be its marked
count. For valid v, 0<=d<C<=K, so a=d/M<1/2.

For d>0, let u_0 and u_1 be the normalized uniform unmarked and marked
vectors. Write sin^2(theta)=a, with 0<theta<pi/4, and use basis (u_0,u_1).
Let R_D=diag(1,-1), R_u=2|uniform><uniform|-I and G_v=R_u R_D.
The exact source sign gives

    G_v=[cos(2theta),-sin(2theta)]
        [sin(2theta), cos(2theta)]
       =cos(2theta) I+sin(2theta) J,
    J=[0,-1;1,0], J u_0=u_1.                       (D3)

The controlled implementation preserves this sign. In particular a
controlled diffusion made from H, a zero phase, H has its additional
controlled minus corrected by Z on the unchanged active flag, as in the
source/controller proof. A replacement by -G_v is not permitted. Every
G_v^(-1) below is the actual inverse word R_D R_u, with the same exact
controls and full address costs. No phase approximation is used.

For any positive integer t, start a probe in 0 and apply chronologically

    H_probe, controlled-on-probe G_v^(2t), H_probe, G_v^(-t).

Before the last word, probe outcomes 0 and 1 have operators
(I+G_v^(2t))/2 and (I-G_v^(2t))/2. Since the powers commute, after it the
operators are exactly

    K_0=(G_v^(-t)+G_v^t)/2=cos(2t theta) I,
    K_1=(G_v^(-t)-G_v^t)/2=-sin(2t theta) J.         (D4)

Thus from u_0 the two components are

    probe 0:  cos(2t theta) u_0,
    probe 1: -sin(2t theta) u_1.                   (D5)

The signs are retained scalar amplitudes. Failure restores exactly the
same unmarked direction, and success lies exactly in the marked subspace.
When d=0, the uniform opponent is fixed by G_v. The two H gates cancel on
that state, no success occurs, and the opponent remains uniform. This
empty case is also why the literal controlled sign in D3 is required.

### A total module on every logical input, and its actual inverse

Assign a distinct nonzero code c to this probe. At module entry compute
the Boolean helper

    alpha=[z=0 OR z=c].

The following is the complete chronological module. All G_v iterations
are emitted even on stopped quantum branches.

1. Apply an unconditional H to b_probe. Compute f=alpha AND b_probe in
   a clean helper. Apply G_v exactly 2t times controlled on f. Uncompute
   f from the unchanged alpha and b_probe BEFORE the next H.
2. Apply the second unconditional H to b_probe. Apply the literal inverse
   G_v exactly t times, each controlled on alpha.
3. Compute f=alpha AND b_probe. For each 1 bit of the classical constant
   c, apply CNOT from f to that bit of z. This exchanges 0 and c when
   alpha=b_probe=1, fixes the other code words, and preserves alpha.
   Uncompute f BEFORE changing b_probe.
4. Compute D_v(w) in clean predicate work, XOR alpha AND D_v(w) into
   b_probe, and reverse the predicate computation. It does not change
   v,w,z or the read-only records.
5. Recompute the same membership predicate from the new z to clear
   alpha. Clear every comparison and Boolean helper by its literal
   reverse word.

The saved alpha is valid after Step 3 because z in {0,c} is invariant
under the guarded exchange. Step 4 leaves z unchanged. The conjunction
helpers are erased before either of their defining bits changes. D_v is
independent of b_probe, so its helper can be cleared after the probe XOR.
These facts hold for every logical word, including arbitrary probe values
and superpositions. Every clean Boolean helper returns to zero.

If alpha=0, all controlled words and permutations are inactive. The two
unconditional H gates cancel exactly, even for an arbitrary input probe.
Thus all earlier stopped codes outside {0,c} are fixed. If alpha=1 and
the reachable input is z=0, b_probe=0, opponent u_0, D5 followed by Steps
3--4 gives

    cos(2t theta)|z=0,b_probe=0>u_0
      -sin(2t theta)|z=c,b_probe=0>u_1.             (D6)

The same probe is therefore zero at every completed reachable module.
No intermediate measurement, fresh probe, per-probe history, reset or
irreversible assignment occurs. This conclusion is not asserted for an
arbitrary logical input; such an input is still acted on by the total
unitary just specified.

The inverse is the exact reverse sequence of ALL elementary gates. In
particular it first computes the final membership flag, reverses the
controlled D XOR, reverses the code exchange, applies controlled G_v^t,
H, controlled G_v^(-2t), H, and clears the initial membership flag, with
the corresponding conjunction and predicate words in reverse order.
There is no inverse of a measured check and no assumption that the input
probe is zero. Module inversion retains the same code-invariance argument
and returns all clean helpers to zero on every logical word.

### Finite codes, blocks and complete prepared states

A dyadic block at scale B_j=2^b_j consists of the b_j modules

    h=0,...,b_j-1, t=2^h.

E_j contains TWO such blocks, each with its own distinct codes. Set
S_j=sum_(i<j)b_i. One explicit coarse-code rule is

    c(j,r,h)=3+2S_j+r*b_j+h,
    r in {0,1}, h in {0,...,b_j-1}.                 (D7)

Code 1 still records invalid v and code 2 still records an initially
marked opponent. Those two initial checks are the source's reversible
predicate-controlled exchanges of 0 with the indicated code. They do
not use or change b_probe. A coarse stopping register of width

    ceil(log2(3+2*sum_(j=0)^L b_j))

contains every selected code. Since L=O(n), b_j=O(n), there are O(n^2)
codes and this width is O(ell). No current code is reused by a later
coarse module. No code has to store an entire opponent or probe history.

Define F_j as follows: start the whole logical attempt at zero, prepare
uniform v over K and uniform w over M by H gates, make the invalid and
initial marked checks, then execute E_0,...,E_j. Let q_j and q_j^false
be its live and false-valid live probabilities, with live meaning z=0.
On an initially valid false candidate, failure of the initial marked
check leaves u_0. D6 then applies successively. Every earlier nonzero
code differs from the current module's code, so that branch is fixed.
The completed F_j state has b_probe=0 on every branch. This includes
invalid candidates and initially marked opponents. At a source vertex
d=0, all checks and modules leave the uniform opponent and code zero;
its contribution to q_j is exactly 1/K.

Every integer in D7 is public. S_j can be generated once along with the
public bounds; schoolbook code computation takes O(ell^2) raw work per
module. Its buffer is retained while its bits are used, and reused later.
No expanded module or gate program is stored.

### Deterministic failure and the tournament sum

For B=2^b, the product identity obtained by b uses of
sin(2x)=2sin(x)cos(x) is

    product_(h=0)^(b-1) cos(2^(h+1)theta)
      =sin(2B theta)/(B sin(2theta)).               (D8)

On the all-failure branch each completed module restores u_0. Hence the
one-block failure probability, conditional on that direction, is

    product_(h=0)^(b-1) cos^2(2^(h+1)theta)
      <=min(1,1/(B^2 sin^2(2theta)))
      <=min(1,K/(B^2 d)).                          (D9)

The last inequality uses sin^2(2theta)=4a(1-a)>=2a=d/K. The two blocks
at a scale leave probability at most min(1,(K/(B^2d))^2). No statistical
independence is used: the two scalar failure factors multiply on exactly
the same restored direction. Previous-scale factors and failure of the
initial marked check are at most 1.

Fix any good record string with the source vertex. The source's tournament
count says that fewer than 2x false vertices have indegree d<x for every
real x>0. For completeness, a set of h vertices all with indegree <x has
h(h-1)/2 internal incoming edges and total indegree <hx, so h<2x+1.
The source is one such vertex for every x>0; removing it gives the stated
strict false-vertex count. All false vertices have d>=1.

Put t=K/B^2. Vertices with d<t contribute less than 2t to the sum of
their two-block survival upper bounds. In each bin

    2^r t<=d<2^(r+1)t, r=0,1,...,

there are fewer than 2^(r+2)t vertices and each contributes at most
2^(-2r). The bin contribution is therefore at most 4t*2^-r. Summing
the geometric series, including the low-degree set, gives

    sum_false min(1,(t/d)^2)<=2t+8t=10t,
    q_j^false<=10/B_j^2.                           (D10)

Empty bins, including all bins below the minimum integer degree, cause
no exception. If t<1 the low set is empty. This argument is deterministic
for EACH fixed good record string. False-edge transitivity is not needed.

Retain the source's exact index range

    Z=sum_(j=0)^(L-1)9^j*q_j^false,

with empty sum zero when L=0. Since B_j>=A_scale*3^j, L<=n and
a_n^2>=n+1, D10 gives

    Z<=10L/A_scale^2
      <=(10/2^128)*n/(n+1)<1/64.                   (D11)

This is a deterministic inequality, with no seed event or Markov bound.

### The fixed recursive amplification and reachability

Use the source's literal words

    Trip(V)=V R_zero V^dagger O_live V,
    V_0=F_0, V_j=E_j Trip(V_(j-1)), j=1,...,L,
    O_live=I-2P_[z=0].                             (D12)

Products compose right to left. R_zero=2|0><0|-I acts on the current
candidate, opponent, code AND its logical probe. It excludes the read-only
records, gradient, other attempts, verification-output bit and clean
Boolean helpers. Including the probe is necessary: it is part of the
unitary logical workspace. The exact zero test and corrected global sign
use O(n) gates, as in the controller proof. There is no extra quantum
recursion stack or live-time estimate.

For psi=V|0> and p=||P_live psi||^2,

    V R_zero V^dagger=2|psi><psi|-I,
    <psi|O_live|psi>=1-2p,
    P_live Trip(V)|0>=(3-4p)P_live psi.             (D13)

Moreover Trip(V)|0>=2(1-2p)psi-O_live psi. Thus it creates no code or
probe support absent from psi. This proves reachability inductively:
before E_j its state is a linear combination of the preceding prepared
state and its live sign flip, all previous stopped codes are old codes,
and b_probe=0 on every term. Every code used in E_j is new. E_j therefore
fixes all previously stopped terms and only filters the preceding live
component. Its own success components have distinct nonzero codes.

If p_j is V_j's prepared live probability, induction gives the exact
direction identity

    P_live V_j|0>
      =[product_(h<j)(3-4p_h)]P_live F_j|0>.        (D14)

Signed cosines and the success signs in D6 do not invalidate this vector
identity. E_j is the same linear word in both sides, stopped-code
subspaces are orthogonal, and the scalar factors in D13 are literal.
There is no assumption that a failed amplitude is positive.

Since |3-4p_h|<=3, p_j<=9^j q_j. On a fixed good record, q_j=1/K+q_j^false
and D11 implies

    sum_(h<L)p_h<1/8+1/64=9/64.

Each x_h=(4/3)p_h lies in [0,1). The elementary induction
product(1-x_h)>=1-sum x_h therefore gives

    product_(h<L)(3-4p_h)>=(13/16)*3^L.

The source component in F_L remains exactly uniform/live. Thus a fresh
V_L returns that source with probability at least

    (169/256)*9^L/K>169/2304>1/16.                 (D15)

The strict lower bound follows from K<9^(L+1). For L=0 all products and
the Z sum are empty; the same inequality holds. It is valid without any
selector seed and for every fixed good record string.

The chronological forward call for j>0 is

    V_(j-1), O_live, V_(j-1)^dagger, R_zero,
    V_(j-1), E_j.

Its literal inverse is

    E_j^dagger, V_(j-1)^dagger, R_zero^dagger,
    V_(j-1), O_live^dagger, V_(j-1)^dagger.

All modules, checks and local arithmetic are reversed as defined above.
Reachability is used only for the success proof. The full inverse words
remain defined on every logical input, including nonzero probes.

### Deterministic shared verification and 1024 retained attempts

For read-only v let W_v use its separate shared logical opponent/code/probe
workspace. Starting that workspace at zero, it prepares uniform w, makes
the invalid and initial marked checks, then performs R_v SINGLE dyadic
blocks at scale B_L. Give each (repeat,h) module a new code, for example

    c_v(r,h)=3+r*b_L+h,
    0<=r<R_v, 0<=h<b_L.

Its code width ceil(log2(3+R_v*b_L)) is O(ell). The complete W_v is the
literal full-input unitary of filter Section 4 composed with the exact initial
preparation/checks. The output predicate is [z=0 AND v<C]. It is exactly
1 for the source and exactly 0 for invalid v on the prepared inner-zero
subspace. No preparation is treated as a reset on arbitrary inner inputs.

For a valid false vertex d>=1, maximality of L gives 3^L>sqrt(K)/3.
Consequently

    K/B_L^2<9/A_scale^2<1/4.

Each failed block restores u_0; D9 therefore bounds every false vertex's
acceptance probability by

    (K/B_L^2)^R_v<(1/4)^(4n+128)
      =delta_det=2^(-8n-256).                      (D16)

There is no seed or union-bound exceptional event. The statement is
simultaneous for all false candidates on every fixed good record string.

Execute W_v, XOR its predicate into the fresh verification-output bit,
and execute the actual W_v^dagger. If P is its conjugated predicate
projector on the inner work, the resulting comparison with the correct
Win(v) XOR and unchanged inner zero has squared vector error exactly
2 times the wrong-predicate probability. For example when Win(v)=0,
the two nonzero error terms are -P|0> on output 0 and P|0> on output 1,
which are orthogonal. The Win(v)=1 case uses I-P. Thus D16 gives

    vector error<=sqrt(2 delta_det)<2^(-4n-127).    (D17)

The estimate uses the fresh verification-output bit in 0. The physical
controlled XOR remains a full unitary on arbitrary output-bit inputs;
that larger subspace does not need the D17 error bound. For superposed v
the stated estimate holds blockwise in v, and hence in norm, including
entanglement with the retained attempt or an inaccessible environment.
The stated bound is on the initial-inner-zero subspace. On an arbitrary
inner state, including actual leaked probe/code/opponent work, the exact
W, controlled XOR and W^dagger are used and remain unitary.

Make exactly 1024 fresh logical attempts. Run V_L and then this verifier
with a fresh output bit for each, sharing the same verifier workspace.
Retain every attempt register, probe and output bit. Compute the first
valid verified candidate into the answer, or 0 if none, with the source's
total reversible first-verified logic. No measurement, abort or retry is
conditioned on verification success.

For the comparison circuit replace each verification by the exact Win(v)
XOR and identity on its inner work. At fixed good records the fresh V_L
calls act on separate zero registers, so D15 gives total miss probability

    <(15/16)^1024<2^-64.

Every preceding IDEAL verification leaves its shared work zero. A
telescoping hybrid therefore uses D17 only on that initial-zero subspace
and gives total vector error

    <1024*2^(-4n-127)=2^(-4n-117)<=2^-121

for n>=1. Later actual gates preserve vector norms. Actual leakage is
retained and counted; it need not be zero before a later actual call.
For normalized states, any outcome probability differs by at most twice
their vector distance. The verification probability loss is <2^-120.

Every selector operation preserves the computational row-record values.
For each retained acquisition transcript ell its selector word is
sum_x |x><x| tensor S_(ell,x). Taking the answer trace sets x=x', even
when records are entangled with an inaccessible reference. Thus the
physical answer law is the average of these fixed-block laws under the
good-first measured-record law of Section 5 and model Sections 4--6.
The actual unconditional coarse error is

    e<2^-80+2^-64+2^-120<2^-60.                    (D18)

The fixed B is used only in the proof. Good and bad systems need not
factor. No success is conditioned on all labels or on accurate decoding.
Model Section 6 supplies the full coherent-block operator calculation.

### Complete known unitary and endpoint interface

U_ell creates the coherent row/axis records, executes all 1024 complete
attempt preparations with their logical probes and shared verifier probe,
and computes the total first-verified answer. Its actual full-input
inverse reverses every gate. Acquisition is outside U_ell and is never
inverted or repeated. After answer copy and undo, retain all old logical
work, including both sorts of probes, and use fresh endpoint helpers.
Sections 7--8 prove the complete gradient, unconditional known-undo and
same-bank endpoint bounds from the coarse error D18. The exact source
count is Q=3*2^16*(n+32), with all deliveries before the selector.

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
independent of the acquired row bank and of all its acquisition outcomes.
Its parameters use only N and its ancillas and randomness are fresh.
It is therefore a product channel with the acquired bank and any reference
extension. Computational measurement outcomes in this paragraph are not
used as advice or ignored when charging work. No source or reference
operation supplies further information to the algorithm.

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

## 8. Known undo and same-bank endpoint success

The complete proof is in model Sections 6--8. Its actual known unitary U_ell
contains row/axis creation, all retained attempts and logical probes,
the shared verifier including leakage and its probe, and the answer logic.
Copy only the class answer and apply its literal inverse. Acquisition and
label measurements are outside U. Conjugated answer projectors give exact
squared vector distance 2 times coarse failure on any purification.
A direct-sum purification over retained acquisition transcripts and D18
therefore give joint bank/reference trace distance <2^-29 from the original
compressed bank, original work/gradient and correct class. Old work remains
allocated; fresh endpoint helpers are used. The estimate is unconditional.

At odd N return the class singleton. At even N let h=N/2 and t be the class.
For each retained row compute a_j=floor(G*((k_j*t) mod N)/N) classically,
subtract it from the gradient controlled by row 1, then measure X on the row.
Assign C on invalid flags or even k_j, L on valid odd k_j with sign +1,
and U on valid odd k_j with sign -1. Return t if L>r; else t+h if U>r;
else use a fresh fair coin. L has priority if both exceed on other branches.

On the original compressed comparison bank, the Fourier-diagonal channel
gives an exact hidden-label refinement. Substituting hidden k only in good
phase/parity tests agrees with the actual endpoint whenever all good labels
are accurate, at unconditional loss <2^-60. The original product good
marginal gives independent fair good parities. Good rows never give a false
trit and their correct count dominates Bin(2r,1/2). Arbitrarily correlated
bad rows can give at most r false trits on every comparison outcome.
The reference success is at least 23/32. No conditional binomial law after
bad records or successful decoding is used. Uniform phase rounding costs
<16Q/G<2^-76 even on entangled rows. The total loss, including known undo
and the gradient failure flag, is

    <2^-29+2^-60+2^-76+2^-80+2^-100<1/256.

Thus full-secret success is >183/256>11/16>2/3 under every allowed joint
input, including the clean case. The false-trit cap is used only on the
comparison bank; trace-distance contraction handles the actual disturbed
bank. Model Sections 6--8 prove each channel comparison and threshold bound.
At N=2 the class is 0 and the selector/U/probes are omitted. Exactly the
same Q=3*2^16*33, acquisition, gradient and trit decision remain. The same
endpoint proof applies with zero undo loss and finite absolute cost.

## 9. Joint resources and growth indices


### 9.1. Fixed layout and the inherited complete edge stream

Use the complete actual controller proved in the current controller appendix,
Section 3. It is a finite-program bit controller with a fixed number of
local tapes/heads, marked bounded strips and ready operand-address words.
Pad public fields and rows to power-of-two slots. Include all padding,
inputs, initialization, tape heads, strips and buffers in allocation.
Every actual read/write, head move, endpoint test, fixed-size logic step,
address change/copy and gate dispatch counts as a raw action. Apply a
conservative full a_addr=ceil(log2(M_alloc+2)) debit to EVERY raw action,
even when a local tape action would require less under the rules. Thus
every classical indexed access and fixed-arity indexed quantum gate has
its full required address charge. There is no free instruction, word
copy, random tape access or quantum-addressed memory operation.

A ready address field is used directly by the classically addressed gate;
the rule does not require an extra fresh instruction copy per gate. Any
address read, construction or copy the controller actually performs is
counted. Consecutive arithmetic gadgets move the ready addresses by their
fixed strides. A carry walk reads/flips all visited bits and moves back
to its marked low end; no separate binary cursor is cleared per gate.
Across m consecutive increments or decrements of a w-bit address the
total is O(m+w) raw actions. Marked strip endpoints and rewinds cost
O(m+1). Hence a fixed number of complete w-bit ripple/copy/Boolean passes
cost O(w+a_addr), including initial address setup, inverse and head returns.

In particular, an edge predicate has the proved full raw cost

    E_raw=O(Q*[n*(p_phase+a_addr)+s+a_addr]+n+a_addr)
         =O(n^2*ell),                               (D19)

where p_phase=Theta(ell), s=bitlength(Q)+32=Theta(ell). This includes
all actual known-prefix reads: for every row and operand bit, set its
slice address in O(a_addr), scan its p_phase bits, prepare a reusable
known addend, controlled-add, reverse the preparation, and restore the
heads. It does not read a complete prefix for each overlapping slice or
store all Q*n slice constants. It also includes the fixed q=14 cosine
table scans with O(a_addr) setup charged for every constant-width gate,
the signed accumulations and reverse scans, the copied sign, all fixed
member-pair orientations, validity, equality and cleanup. No unchanged
source-array access is dropped in the new bound.

The exact controlled G_v and G_v^(-1) use this edge word and an O(n)
diffusion with the literal sign in D3. Their raw gate/controller cost is
O(E_raw+n). Their arithmetic helpers clear for every logical input and
every active flag. A quantum control bit is used as data, never as a
memory index. One additional conjunction helper in filter Section 4 gives the
required alpha AND probe control without changing any gate-arity bound.

### 9.2. Each new loop and every inverse

Each module computes alpha by two O(ell)-bit comparisons, performs its
two H gates and controlled powers, generates/uses its known code, makes
the guarded code XOR, evaluates/reverses D_v to clear the logical probe,
and clears all flags. Retain alpha across both controlled powers. Retain
alpha AND probe only during the first controlled power, then erase it
before the next H; recompute it only for the code exchange. Controls
remain unchanged while their constituent Grover words execute.

Keep one reusable O(n)-bit classical iteration counter and one bound
buffer. For each Grover iteration, compare/increment the counter by full
O(n)-bit scans, counting all reads, writes, carries, endpoint tests and
returns. Construct t=2^h and 2t by zeroing/copying the finite O(n)-bit
buffer and setting the designated bit, also with counted address setup.
One module costs

    O((3t+1)*(E_raw+n)) raw actions.               (D20)

This charges the short t=1 modules, every exact predicate check and even
full O(n)-bit counter work for them. A block has sum_(h<b)t=B-1 and
b<=B for B>=2. Including all module ends, h counters, code generation,
power-buffer setup and block endpoints, it costs O(B*(E_raw+n)). There
is no unproved constant-delay increment and no B-cell classical strip.
The exponential loop uses the finite binary counter, not stored history.

All new public integers have bounded sizes: b_j=O(n), code values O(n^2),
their binary widths O(ell), and loop-counter/bound buffers O(n). Public
code schoolbook arithmetic O(ell^2) is O(n) and is performed once per
module, with a fixed-size slot retained during the comparisons/XORs.
Use an O(n)-cell marked strip, or counted full-width binary tests, for
the h, block and R_v loops. Initial marking, end tests and rewinds cost
O(n) per block/module if needed and are already covered by D20. A new
endpoint is not created by an uncharged search through an exponential
word. Inverse loops descend through the same finite public indices,
load the same codes and bounds, reverse every local word, and have the
same charges. Actual nonzero probes or stopping words do not alter the
classical stream or any loop count.

Recursion frames contain a level, direction and one of a fixed number
of program positions, each O(ell) bits. A stack head enters, reads and
leaves O(ell) cells per frame occurrence. The schedules in filter Section 7
give the exact forward and inverse emitter, with depth at most L+1.
Only a leaf block uses the large iteration/bound buffers, so these are
reused between calls. No child recursion occurs inside a module. There
is no stored expanded circuit, quadratic quantum history, or quantum
recursion frame. Reflection/address setup and frame dispatch cost fit
the same recurrence below. The first-verified logic, complete U and
U^dagger use the same counted Boolean/reverse templates.

### 9.3. Complete selected recurrence

Since a_n<sqrt(n+1)+1<=2sqrt(n+1),

    B_j<2 A_scale*3^j=O(sqrt(n)*3^j).

Two blocks and the initial preparations/checks therefore have raw work
O(B_j*(E_raw+n)). Let t_j be the full raw work of V_j, including the
classical emitter. The selected literal recursion satisfies

    t_0=O(sqrt(n)*(E_raw+n)),
    t_j<=3t_(j-1)+O(sqrt(n)*3^j*(E_raw+n)).

Induction, L+1=O(n) and 3^L<=sqrt(K) give

    t_L=O((L+1)*3^L*sqrt(n)*(E_raw+n))
       =O(sqrt(K)*n^(7/2)*ell).                    (D21)

The shared verifier and its inverse have raw cost

    O(R_v*B_L*(E_raw+n))
      =O(sqrt(K)*n^(7/2)*ell),                     (D22)

because R_v=O(n). Its verification code/repeat loops and copied predicate
are included by Section 9.2. All 1024 calls, all retained attempts,
answer copying and the literal inverse of U add a constant factor or
polynomial overhead. No branch-dependent early stopping is used to
obtain D21 or D22.

Generate ceil(sqrt(n+1)) by exact integer binary search and schoolbook
squares. Generate all 3^j, B_j, b_j and S_j uniformly by integer
arithmetic, with at most O(n^3) raw work and O(n^2) stored bits. The
source/controller's acquisition cost is O(n^3*ell) raw, including
translations, all R_F=O(ell) tests per level/offset, exact reconstruction,
prefix division, measurements, resets and source charges Q(n+1).
Gradient initialization and all 80 attempts, the fixed table's counted
rational construction, final classical products/divisions, endpoint
translations, trit counts, fresh coin and invalid-answer handling have
their unchanged polynomial caps. These fit D21: any fixed polynomial
is absorbed by 2^(n/2)*n^(7/2)*ell with an absolute outer constant, and
the bounded finite n prefix can enlarge that same constant. No validity
threshold, finite-input advice, or change to the source algorithm is
introduced by that asymptotic comparison.

### 9.4. Simultaneous allocated space and the full address charge

Classical labels, flags and prefixes use Q*(2n+p_phase+1)=O(n^2) bits.
All public powers/bounds use O(n^2); S_j and current code data fit within
that budget. The recursion uses O(n*ell) bits. A fixed number of O(n)
counter/bound buffers and local strips, ready addresses/head locations,
arithmetic scratch, acquisition counts and gradient constants fit O(n^2).
There is no seed bank and no stored O(n^2)-gate or exponential program.
Every initialized/padded cell and the fixed table is included. Thus
S_C=O(n^2) without transferring any stored-program space assumption.

Unread raw registers remain passive state of the inaccessible source and
are excluded under the rules; no acquired register is returned there.
Quantum storage is the Q acquired rows and Q axes, each linear in n, with
the reusable acquisition/edge arithmetic of O(n) qubits. Every retained
attempt has O(n) candidate/opponent work, O(ell) code and just one added
logical probe; 1024 is an absolute constant. The one shared verifier
has O(n) logical work, including its code/probe and any actual leakage.
The O(n) zero-test helpers now include the attempt probe in the test.
The gradient uses O(ell), and the answer-copy/residual old work and fresh
endpoint helpers add O(n). All these banks can coexist with the classical
allocation, so the simultaneous peak remains S_Q=O(n), S_C=O(n^2).

An explicit allocation by a fixed number of padded banks is at most
C(n+2)^2 classical bits plus C(n+2) qubits for an absolute C, including
the fixed-size table and head records. Choose the corresponding padded
address width before initializing the layout; there is no circular
definition based on the eventual circuit length. Then a_addr=O(ell).
Multiplying the entire raw count D21--D22 by that full factor pays all
indexed gates/accesses and all local operations conservatively. This
proves the joint theorem of Section 0. It does not use a constant-delay gate generator or a free
address copy.

All limits depend only on N and the public parameter rule. Malformed
records, missing sources on bad record blocks, actual verification
leakage, incorrect answers and gradient-preparation failures cannot
enlarge a counter, code, loop, recursion depth or allocated bank. All
specified modules and gates are executed on stopped quantum branches.
No measured intermediate success affects the filter stream. Thus the
resource and source-count bounds hold on every execution branch for
every N>=2, jointly with the exact clean-joint-marginal specification of Section 0.


For B_T(n)=2^(n/2)n^(7/2)(log2 n)^2,
log2 B_T=n/2+(7/2)log2 n+2log2 log2 n, and
log2(log2 B_T)/log2 n tends to 1. For n^2,n,n the same ratio in the rules'
max{4,B} convention tends to 0. Absolute outer constants preserve these
values. These prove exact representative-envelope growth indices 1,0,0,0;
no matching lower bound on actual work or storage is asserted.

## 10. Direct sources and inherited credits

### 10.1. Direct semantic source

The complete source geometric-filter algorithm, compression, adaptive sign proof,
shared opponent and verifier, recursive word, same-bank undo and endpoint
come from public submission 6e8dae83-9556-4fa1-9e3e-0237b7083742, commit
2f4f96f7fe3fe58cbf815ea0e2158ab562f2f777. Its
[exact proof](https://github.com/Layr-Labs/dcp/blob/2f4f96f7fe3fe58cbf815ea0e2158ab562f2f777/submission/proof.md)
is 49265 bytes, SHA-256
`c708912df1e846cf2655bb590a61cba967eab00b77ded14108e63e5803c000eb`.
Its
[exact declarations](https://github.com/Layr-Labs/dcp/blob/2f4f96f7fe3fe58cbf815ea0e2158ab562f2f777/submission/submission.json)
are 9741 bytes, SHA-256
`e8179c9414c40d70b23cbe07c4a36ba84fe0dee7ff1017d350f5f6305ec28a31`.
Both were read directly. The complete needed acquisition, score, gradient, known-undo and endpoint
arguments are reproduced in the current four proof files. Its original
adaptive-freshness proof is replaced by the joint-input channel and good-first
proof here; the two input specifications are not identified.
The selector is the deterministic symmetric-probe word of Section 6 and
[the filter appendix](linear_quantum_marginal_filter.md). Its selected scale,
code rule, verification and complete charged work are proved in these
current files; no seed/trial schedule is retained.

The current filter appendix proves the selected square-root scale and the
complete deterministic replacement. All needed semantic proofs are
present in this main file and the model appendix. No local note is required evidence.

### 10.2. Direct literal-controller source

The actual online bit/head/ready-address construction uses the local
complete proof critical_third_cache_generator_l2.md, 16253 bytes,
SHA-256
`eb122317b103da59cdd982b29f863da27d1d932313e8b67861d1d212a64088f3`.
Its public complete form is E, submission
f0bfcbc9-ef55-4754-b61e-061100ace74f, commit
725ccdfea43184deed9aabe890bdb35b3b2e5037, member
[submission/critical_third_cache_l2_controller.md](https://github.com/Layr-Labs/dcp/blob/725ccdfea43184deed9aabe890bdb35b3b2e5037/submission/critical_third_cache_l2_controller.md),
30611 bytes, SHA-256
`88c0279062fd2b9a948b2f1922e80c620437e6552a25e37fff4af483e3eeb340`,
Section 10. The exact archived public bytes, member hash and commit were
checked and the method was read directly. The controller appendix gives
the full needed construction for this different circuit. That complete classical generation method is used here. After the symmetric
probe proposal was formed, E's dyadic Hadamard-probe and sine-product argument
was read directly in
[submission/critical_third_cache_l2_selector.md](https://github.com/Layr-Labs/dcp/blob/725ccdfea43184deed9aabe890bdb35b3b2e5037/submission/critical_third_cache_l2_selector.md),
24815 bytes, SHA-256
`29dbd4735d0e725577114ec8f0e0151c19b46acc4e382a9265defacb88006afe`,
lines 71--109. That prior identity is credited and proved again here; it is
not claimed as new. E keeps probe/pivot history; the present symmetric word
returns its single probe to zero on reachable prepared states. E's cache and quantum-prefix circuits are not executed. Its exact joint
clean-marginal input promise and good-first/endpoint proof method are
selected here, as detailed in Section 10.4.

### 10.3. Inherited source credits

The direct semantic source credits ROB-G2
(55a6ce76-34af-468f-b735-a1197f3d3459), R24
(f892f7ea-957b-4dde-8374-dab2736231d0), and EP-A
(493303b5-06f6-4ee0-9596-d8cae89c8bb4). In that source's stated chain,
ROB-G2 supplies the measured-label phase tests, classical binary prefix
interface and counted table arithmetic. R24 supplies the bounded cubic
pair witness, class grouping and same-bank copy/undo plus trit endpoint.
EP-A combines these interfaces at exactly 1/3 with the same adaptive
model. These inherited credits are preserved. They do not assert that
the original ROB-G2, R24 or EP-A files were read to build this package.
The complete arguments needed here are proved in the current four
proof files.

The geometric filter itself is credited to the direct semantic source.
It replaces that source chain's coherent pivot selector and retains no
pivot cache or pivot/sampler history. The fixed recursive tripling idea
is also used for general variable-time search by Ambainis, Kokainis and
Vihrovs, arXiv:2302.06749v2 (2023), Section 3.2. This is an inherited
paper credit, not a claim of direct consultation here. The selected checker uses deterministic symmetric probes, two dyadic
blocks per coarse level and one shared opponent register. The exact degree
sum and literal tripling proof establish its schedule. No general
variable-time-search theorem, prior acceptance or broad novelty claim is
imported. Generic square-root query upper bounds for
finding tournament winners are not claimed as new.

### 10.4. Immediate local source and material joint-model source

The immediate complete local algorithm source is the frozen LQ-FILTER
package. Its four exact files were read before this construction:

- main, 65030 bytes, SHA-256
  `7ad0c2892738991ecfb36598ac52b82f38e23f18bf7a195e846bcfc18a29fd1b`;
- controller, 17972 bytes, SHA-256
  `2e966d88aa44835cf297fe0d0e4ab022164b27500e5bfa4c9eccca0d39b89251`;
- filter appendix, 31637 bytes, SHA-256
  `2df2fdf7fc319cea3dbe6add8f05156efcccd77a99b772a550245e04d9839474`;
- declarations, 14229 bytes, SHA-256
  `12cf0e3f97d599f74d5fda7d8175b4490042aca53f19849e789d0a176ca810b6`.

No public submission identity is assigned to that local package here.
The physical acquisition/filter/controller/gradient/endpoint schedule and
parameters are preserved; the selected input specification and proof change.
Its earlier local-first controller dependency and later public E read are
preserved in Section 10.2. The symmetric-probe proposal preceded its E dyadic
reread. Neither source identity nor that chronology is replaced by a verdict.

The added direct public model/statistical/endpoint source is E, submission
f0bfcbc9-ef55-4754-b61e-061100ace74f, commit
725ccdfea43184deed9aabe890bdb35b3b2e5037. Its exact
[main proof](https://github.com/Layr-Labs/dcp/blob/725ccdfea43184deed9aabe890bdb35b3b2e5037/submission/critical_third_cache_l2.md)
has 64512 bytes, SHA-256
`a368460e91b468a7baa607a68813eaaeec62e3cf00090277e1fe34c625466eba`.
Its model, good-first concentration, known-undo and same-bank endpoint
passages in Sections 0, 3 and 7 were read directly. Its
[phase proof](https://github.com/Layr-Labs/dcp/blob/725ccdfea43184deed9aabe890bdb35b3b2e5037/submission/critical_third_cache_l2_phase.md)
has 24351 bytes, SHA-256
`1682b3d086335db15e3a3254fcbd1967bbd44b5b27605105fb4dc21c24e34680`;
its all-input score and marginal endpoint passages were also read. The
four E proof files equal their archived manifest pins. E's exact structured
model, good-first record method and unconditional marginal endpoint method
are material sources. This package proves their transfer through its
streaming measured-label channel, not through E's retained raw bank or cache.

The local bounded transfer note has SHA-256
`9e51396e979a8e2957dd2cbae83fde63814ece259ac58d53325a6d6097ba1932`.
Its full mathematical proof is reproduced in the model appendix with current
package interfaces. No bounded note, review, acceptance or unavailable
source is required to fill a proof gap. No unread original consultation
is claimed; all inherited credits and actual read history are preserved.
