# Exact one-third tolerance with cached phase comparisons

## 0. Joint theorem and one parameter rule

**Proved.** For every integer N>=2 and s in Z/NZ, let n=ceil(log2 N).
Algorithm A below outputs the entire s with unconditional probability at
least 11/16>2/3 under the error model reproduced below, at epsilon(n)=1/3.
On every execution branch its joint bounds are

    T = O(2^(n/2) n^2 (log2 n)^2),
    S_C = O(n^2),  S_Q = O(n^2),  Q = 3*2^16*(n+32) = O(n).

Constants are absolute and independent of N, s, the supplier and outcomes.
Logarithmic cost estimates use log2(n+2), which is asymptotically equivalent
to log2 n; the single n=1 modulus has finite absolute cost. The representative
envelopes have growth indices 1,0,0,0. There is no validity threshold.

The fixed parameters, computed by finite integer arithmetic, are:

    K=2^n; Q=3*2^16*(n+32); r=Q/3;
    q=14; r_phi=26; p=r_phi+2+bitlength(n); J0=max(1,n-2);
    L_F=bitlength(16*(J0+1)*Q*2^60); R_F=200*L_F;
    H=64*(n+1)+1280;
    at level ell=0,...,n: 64 stages with B_ell=2^(ceil(ell/2)+2);
    then 1280 stages with B_n;
    tau_i=-1/256+J_i/2^23, J_i independent uniform 16-bit integers;
    g=bitlength(2^80*(Q+1)); G=2^g.

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
2. Draw the H independent 16-bit threshold integers of Section 6, after all
   deliveries. Prepare the ordinary work gradient of Section 7, with 80 capped attempts.
   If all attempts fail, output 0. This happens after acquiring all Q sources.
3. Apply the known unitary U: generate coherent X/Y row records (Section 3),
   run the bounded coherent class selector and pivot-cache computations
   (Sections 4 and 6), and compute its answer.
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

## 4. Constant-size phase caches and interpolated scores

**Proved (two phase encodings).** Set r_phi=26 and p=r_phi+2+bitlength(n).
For record j and bit i=0,...,n-1 the classical prefix word supplies

    a_(j,i)=floor(e_j/2^(n-i)) mod 2^p
           =floor(2^p frac(2^i*k_j/N)).

For a quantum n-bit class representative v, accumulate
V_j(v)=sum_i v_i*a_(j,i) mod 2^p by controlled constant additions. Define its
fresh phase F_j(v) as the top r_phi bits of V_j(v). Define its exact-grid phase

    E_j(v)=floor(2^r_phi frac(k_j*v/N)).

Both are r_phi-bit words, a constant width independent of n. The prefix
sum underestimates the unwrapped exact phase by less than n/2^p, which is
less than 2^(-r_phi-2). Consequently F_j(v) is either E_j(v) or E_j(v)-1
modulo 2^r_phi. Its circular error from k_j*v/N is <(5/4)*2^-r_phi; the
exact-grid error is <2^-r_phi. This follows directly by writing the prefix
sum as the exact sum minus the sum of its <1-unit truncation errors, then
taking the top bits. More explicitly,
V_j(v) is congruent to 2^p*k_j*v/N-z modulo 2^p for a real z in [0,n).
Dividing by 2^(p-r_phi) moves the exact r_phi-grid coordinate downward by
less than 1/4, so its floor is unchanged or reduced by one. This includes
phase wraparound.

At even N, a class representative v has members v and v+h, h=N/2. From
either phase word for v, the corresponding member word is obtained by adding
2^(r_phi-1)*(k_j mod 2) modulo 2^r_phi. This is an exact half-turn shift,
because k_j*h/N=k_j/2. At odd N the classes are singletons.

**Proved (cost of each encoding).** Compute all Q fresh phase words of a
candidate v into a shared Q*r_phi-qubit cache: for each j accumulate V_j(v),
copy its top r_phi bits, and reverse that accumulation. This costs
O(Q*n*p)=O(n^2 log(n+2)) gates and O(n) quantum space, including the cache.
The controller reads only sequential classical prefix slices.

To create a permanent pivot's exact-grid cache, for each j compute k_j*v mod N
in an n-bit accumulator by n controlled additions of the classical constants
2^i*k_j mod N. It costs O(n^2) gates and O(n) reusable scratch. Generate these
constants by counted classical doubling/reduction. Retain this one record's
n constants in O(n^2) classical bits, reused for the next record; forward
and literal reverse orders then have the same O(n^2) generation cost.
No inverse of noninvertible doubling modulo an even N is assumed.
From the valid remainder,
extract r_phi fractional bits by repeated doubling, comparison with N and
conditional subtraction, retaining the quotient bits. Each of these fixed
r_phi steps costs O(n) gates. Copy the quotient to the permanent cache,
reverse fraction extraction and reverse the modular product. All helpers
clear. The same XOR-output circuit works for arbitrary cache target contents.
One whole permanent cache costs O(Q n^2)=O(n^3) gates and O(n) qubits. This
polynomial work is performed once per potential pivot, never per Grover query.

### A continuous piecewise-linear table function

**Proved.** Write c_a=C_a/2^25 for Section 1's 2^q table values, q=14. Define
the periodic piecewise-linear function I(x) by linear interpolation between
c_a and c_(a+1 mod 2^q) on each interval [a/2^q,(a+1)/2^q]. Then

    |I(x)-cos(2*pi*x)| <= zeta,
    zeta=tau+pi^2/2^(2q+1),  tau=2^-24,
    |I(x)-I(y)| <=7*circular_distance(x,y),  |I(x)|<=1.

The interpolation error of a twice differentiable function on a length-delta
interval is at most max|f''|*delta^2/8: subtract its secant, apply Rolle's
theorem twice to the error minus a suitable multiple of (x-a)(x-b), and use
|(x-a)(x-b)|<=delta^2/4. Here max|cos(2*pi*x)''|=4*pi^2. Table endpoint error
adds at most tau by convexity. Each segment slope has magnitude at most
2*pi+2*tau*2^q<7. The periodic join uses c_0, so the same bound holds across
the last interval and on circular distance. Range follows by convexity.

On an r_phi-bit word W, with a its top q bits and b its remaining r_phi-q
bits, this interpolation is exactly

    [(2^(r_phi-q)-b)*C_a+b*C_(a+1 mod 2^q)] / 2^(25+r_phi-q).

Both lookups are counted full fixed-table equality scans. The remaining
multiplication and additions have fixed widths independent of n and hence
absolute constant cost. Sine uses I(x-1/4). No real arithmetic or rotation
oracle is used.

### Contextual pair and class scores

For an ordered pair of distinct valid classes, one is the candidate and uses
its fresh phase cache; the pivot uses its exact-grid cache. Construct member
phases by the half-turn rule above. For members t,u, replace the four
exponentials of h_tu in Section 3 by interpolated cosines or sines at the
corresponding phase words for t,u,2t-u,2u-t. The affine word combinations are
computed modulo 2^r_phi. Form h's component, clamp it to [-1,1], multiply by
2y and assign zero on invalid source flags. Denote this rational score Z_j.
It has magnitude at most 2. Its common denominator is

    D=10*2^(25+r_phi-q)=10*2^37.

Use integer accumulation in bitlength(Q)+44 signed bits. Comparison of its
average with a threshold is exact; no summation or threshold rounding occurs.

**Proved (uniform observable error).** The affine phases have circular error
at most (7/2)*2^-r_phi: twice a fresh phase and one exact-grid phase is the
largest case. Thus every interpolated trigonometric term has error at most

    eta_c=7*pi*2^-r_phi+zeta.

The absolute coefficient sum in h is 6/5. Clamping cannot increase error from
its true component in [-1,1]. Averaging the fair axes, the correct-label row
observable error is <=(12/5)*eta_c; changing a label changes a clamped row
observable by norm <4. The complete local instrument consequently differs
from M_tu by operator norm at most

    beta_c=(12/5)*eta_c+4*(2^-60/Q) <1/320.

Use pi<22/7, q=14, r_phi=26 for the last rational inequality. Section 2's
diagonal-label argument makes this a bound on every malformed input as well
as clean inputs. Both assignments of fresh/exact-grid roles satisfy it.

**Proved (role discrepancy).** Fix the entire local shadow record string.
For two canonical class IDs a<b define F_ab^(1) as the maximum over a's
members of the minimum over b's members of the empirical average score,
when a uses fresh phases and b exact-grid phases. Define F_ab^(2) with the
opposite phase assignment. These are ordinary rational functions of records.
Their difference is at most

    epsilon_role=51*2^-r_phi.

Indeed exchanging roles changes each member's phase by at most one grid cell.
Each affine phase changes by at most three cells. The interpolator's slope
bound gives at most 21*2^-r_phi change per trigonometric term. The coefficient
sum and score factor give at most (12/5)*21*2^-r_phi<51*2^-r_phi per local
score. Clamping and empirical averaging do not increase the bound. Neither
maximum nor minimum increases the sup-norm perturbation. This is a
deterministic statement on every record string, not a concentration claim.

For a pivot-associated threshold tau_p, canonical class a wins against b iff
its contextual F_ab is >=tau_p; otherwise b wins. Exclude self-pairs and
invalid classes. At most four exact integer average comparisons implement
this rule. The role assignment is determined by which operand is the
candidate and which is the cached pivot. A fixed global tournament is not
assumed for these contextual comparisons.

**Proved (membership cost).** Given a candidate's fresh cache and a saved
pivot's cache, one member pair scan uses O(Q log(Q+2)) gates: all phase,
interpolation and clamping words have constant width, while accumulation
uses O(log(Q+2)) bits. One class comparison has the same order. Membership
scans all O(n) prior potential pivots, ignoring those whose accepted flag is
zero, and copies the AND of the required wins. Including fresh-cache creation
and its reversal, it costs O(n^2 log(n+2)) gates and unaddressed controller
bit operations. Shared scratch is O(n). All record/pivot addresses are public
loops; phase words are arithmetic operands, not quantum memory addresses.


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
(s,u) and either fresh/exact-grid phase-role assignment, conditional means m_j satisfy

    m_j>=11/20-beta_c at clean positions, m_j>=-1-beta_c at bad positions.

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
2 exp(-Q/32768)=2 exp(-6(n+32)). The two phase-role assignments and the
constant-size class member choices give fewer than 8K^2 score functions.
A union bound gives simultaneous failure <2^-80: since e>2,

    16*K^2*exp(-6(n+32)) <2^(-4n-188) <2^-80.

The clean count is at least 2Q/3 on every branch. Thus on the simultaneous
event, every true-versus-other-class empirical average is strictly positive:

    (2/3)*(11/20)-(1/3)-beta_c-1/64
      >1/30-1/320-1/64 =7/480>0.

Its reverse score is strictly negative. Neither independence of malformed
copies nor transitivity among false candidates has been assumed.

## 6. Bounded coherent elimination with fresh thresholds

**Proved (true-class property).** Group secrets into singleton classes at odd
N and antipodal pairs {v,v+N/2} at even N. Let C be their count. On Section 5's
simultaneous event, in either phase-role assignment the actual true member
s has empirical score >gamma_0=7/480 against every member of any other class,
and every rival member has score <-gamma_0 against s. Therefore the correct
class beats every other class, in every contextual comparison whose threshold
is in [-1/256,1/256). This follows directly from the canonical max/min rule;
1/256<gamma_0. No ordering among false classes is needed.

Before U, after acquiring all sources, draw independent 16-bit fair integers
J_i for every potential pivot stage. Set

    tau_i=-1/256+J_i/2^23,   0<=J_i<2^16.

They are classical read-only inputs to U. Threshold i is used only AFTER its
stage's pivot sampling, for comparisons against that pivot in later stages.
Thus its distribution is independent of its pivot and the current contender
set, conditional on the complete record string and earlier stage history.
One can reveal the independent threshold list progressively; the sampler
never uses its current or future thresholds. The bank's reduced state is
independent of this post-acquisition randomness.

**Proved (contextual shrinkage).** Fix an arbitrary record string and a subset
S of k valid classes. For any a<b in S the two possible candidate/pivot
assignments give values F1,F2 with |F1-F2|<=epsilon_role. On the uniform
threshold grid the probability of lying between these values is at most

    nu=128*epsilon_role+2^-16 =59/2^19 <1/1024.

A length-ell interval contains at most ell/2^-23+1 grid points. For a pivot
b, a survives iff tau<=F1; for a pivot a, b survives iff tau>F2. Their
probabilities sum to at most 1+nu. Summing over all unordered pairs gives,
for a uniform pivot p in S and a fresh independent tau,

    E |{v in S\{p}: v contextually beats p}| <=(1+nu)*(k-1)/2 <3k/4.

This proof needs neither transitivity nor one fixed global tournament. On
good records the true class remains in the next set unless p itself is that
class, whereupon the next set is empty.

### Mixed uniform-clock sampler

**Proved.** For a Boolean contender predicate f on K=2^n addresses, use a
fresh fair coin c, a uniform clock j in [0,B), and a uniform candidate.
If c=0 apply no Grover iterations; if c=1 apply j iterations. Compute the
exact f flag. The whole operation is unitary; all coin, clock, candidate and
flag registers are retained. It emits B-1 controlled Grover iterations, even
on the c=0 branch. Conditional on success, its candidate marginal is exactly
uniform on S=f^-1(1), since marked amplitudes are equal in every coin/clock
branch. If a=|S|/K=sin^2 theta, its success probability is

    p_success=a/2+(1/2)[1/2-sin(4B theta)/(4B sin(2theta))],

with the continuous empty/full endpoint values. The bracket follows by
summing sin^2((2j+1)theta), using the two-reflection Grover rotation. If
a>=1/2, the c=0 part alone gives success >=1/4. If 0<a<1/2 and B>=4/sqrt(a),
sin(2theta)>=sqrt(2a), so the bracket is >=1/4 and success >=1/8.

Diffusion is H, a zero-state phase and H. Its controlled global minus is
corrected by Z on the iteration control if needed. A Grover mark computes
membership, applies a controlled Z to the exact flag and uncomputes it.
The clock-bit powers explicitly emit 2^ell iterations, additionally controlled
by coin c. H gates in diffusion remain unconditional. Only known exact
Clifford+T and Boolean gates are used; no selective pi/3 approximation is
needed in this selector.

### Public finite schedule

For each level ell=0,...,n make exactly 64 potential pivot attempts with

    B_ell=2^(ceil(ell/2)+2),  T_ell=K/2^ell.

Then make 1280 additional attempts with B_n. Thus H=64(n+1)+1280 is the
public number of stages. At each stage the contender predicate is validity
and a win against EVERY earlier ACCEPTED pivot at that pivot's saved
threshold. Begin with all valid classes. Run the mixed sampler. Its fresh
exact verification flag records whether its candidate is in the contender
set. On flag 1 the candidate becomes a pivot; on flag 0 the set is unchanged.
There is no false-empty stopping decision. Compute and retain the stage's
exact-grid phase cache, even on unaccepted/invalid branches. Later comparisons
ignore its cache when the accepted flag is 0. Return the last accepted pivot,
or 0 if none; a last-stage accepted pivot is included.

Every later stage preserves earlier stage registers and caches. Arithmetic
helpers return clean on every logical operand word. Conceptually revealing
the row records and each completed stage's saved values gives exactly their
measured probabilities: all subsequent gates are block diagonal in those
values. This deferred-measurement statement holds on arbitrary entangled rows.

**Proved (finite error bound).** Fix good records. A successful sampler gives
a uniform pivot independent of its fresh threshold. For |S|>=T_ell its
success is >=1/8 by B_ell>=4sqrt(K/T_ell). Contextual shrinkage on success
and no change on failure give expected next size <=rho*|S|, rho=31/32.
For |S|<T_ell the size never increases. Hence universally at that level

    E[next size | S] <=rho*|S|+(1-rho)*T_ell.

Let a0=rho^64<1/4. Across the level's 64 attempts,
E[size_after]<=a0*E[size_before]+(1-a0)*T_ell. Inductively after each level
E[size]<=2T_ell: initially C<=K, and at the next level the preceding bound
is <=4T_ell, giving (1+3a0)T_ell<2T_ell. Thus after level n the expectation
is <=2. In the tail, T_n=1, so every nonempty set has success >=1/8 and
contracts by rho. After 1280=20*64 tail attempts,

    E[size] <=2*rho^1280 <2*(1/4)^20=2^-39.

The true class survives until selected, and a set becomes empty exactly when
that class is selected. Markov bounds the probability that it was not selected
by <2^-39. Later failed attempts do not overwrite the last accepted pivot.
Including the <2^-80 sign-event failure, the actual exact-gate coarse unitary
has unconditional failure <2^-38. No source is acquired in this selector.

**Proved (query budget).** The total number of emitted Grover iterations is
at most 64*sum_(ell=0)^n B_ell+1280 B_n <1536 B_n=O(2^(n/2)), since
sum B_ell<4B_n. There are H=O(n) final verification calls and pivot cache
computations in addition. This is a worst-case public bound, not an expected
stopping-time estimate.


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

The coarse unitary contains only exact row-basis gates, Boolean score/cache
arithmetic and exact Grover reflections. It does not use the gradient. By
Sections 5-6 its unconditional failure is

    e<2^-80+2^-39<2^-38.

This is the failure of the actual physical coarse unitary, without a phase
synthesis premise. Gradient preparation error is charged once by trace-distance
contraction through all later operations, including the final row corrections.

## 8. Known undo, adaptive trits and endpoint success

**Proved (unconditional reuse lemma).** Fix a classical acquisition transcript
ell, and let U_ell be the actual finite exact-gate unitary for its row
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

**Proved (quantum space).** Streaming acquisition retains Q source rows and
one position/probe workspace, O(n) qubits. Coherent row axes add O(n). Each of
H=64(n+1)+1280 stages keeps an O(n)-qubit candidate/clock/coin/flag register
and Q*r_phi exact-grid phase bits, also O(n) because r_phi=26 is constant.
All stage caches and histories together use O(n^2) qubits. The shared fresh
candidate cache is Q*r_phi=O(n); score, class and exact modular-product
helpers are O(n). The gradient is O(log(n+2)) qubits and its preparation is
reused across attempts. Retaining all old work and adding fresh endpoint
helpers still gives peak S_Q=O(n^2). No cache is claimed to use linear total
space across all stages.

**Proved (classical space).** Q labels and prefix words occupy
Q*(2n+p+1)=O(n^2) bits. The 16H fair threshold bits and their integer
comparison constants use O(n log(n+2)) bits or less. The fixed table and its
rational construction have absolute constant size. Reused phase-test counters
need O(n log log(n+2)) bits, and grade-school integer arithmetic uses O(n)
scratch. A reused one-record list of doubled modular-product constants adds
O(n^2) classical bits and prevents reverse-generation time overhead.
Public stage/record/bit/Grover counters and addressed templates fit O(n^2) bits. There is no exponential gate list, contender list or edge table.
Thus S_C=O(n^2), total live bits plus qubits M_live=O(n^2), and each classically
addressed operation pays O(log(n+2)).

**Proved (work).** Source compression costs O(n^3 log(n+2)) gates and
unaddressed bit operations. A fresh candidate phase cache costs
O(n^2 log(n+2)); each cached-pivot class comparison costs O(n log(n+2)).
Scanning H=O(n) prior potential pivots therefore costs O(n^2 log(n+2)),
including cache creation/uncomputation, exact average comparisons and AND.
Section 6 bounds ALL emitted Grover iterations by O(2^(n/2)); their total
gate/controller work is O(2^(n/2)n^2 log(n+2)) before addresses.

Creating each permanent exact-grid pivot cache costs O(n^3), for O(n^4)
over all H stages. Final contender verification at all stages costs
O(n^3 log(n+2)). Gradient preparation, threshold generation, source charges
Q(n+1), initialization, measurements/resets, answer copying and trit processing
are polynomial work within O(n^4+n^3 log(n+2)). Literal inversion doubles
the appropriate forward terms. These polynomial costs are absorbed by the
stated exponential envelope: n^2<=2^(n/2) for n>=16 (check 16 and 17, then
use (n+2)^2<=2n^2). Finitely many smaller instances have absolute finite cost.

The controller emits ripple, fixed-table/interpolation, multi-control and
Grover circuits by bit loops. Each prefix slice costs O(p) bit operations and
emits O(p) gates. Cache-generation modular constants use O(n) operations
per n-bit doubling, already included in its O(n^2) product cost per record.
Constant-width interpolation arithmetic has absolute fixed cost. Wire
addresses and indices have O(log(n+2)) bits. One such overhead factor covers
local circuit generation and the required address charge; no n-bit modular
product is recomputed for every gate of a membership oracle. Long loop
counters cost O(n) per iteration, dominated by its membership computation.
All public bounds and threshold comparison integers are generated by charged
integer arithmetic. Hence the joint total work is

    T=O(2^(n/2)n^2(log2 n)^2).

This worst-case bound includes every failed sampler, cache for an unaccepted
pivot, invalid word, preparation failure and incorrect final class. There are
no source restarts, hidden quantum-memory accesses or uncharged rotations.

For B_T(n)=2^(n/2)n^2(log2 n)^2,
log2 B_T=n/2+2log2 n+2log2 log2 n, so its growth index is 1. The n^2,n^2,n
classical-space, quantum-space and sample envelopes have index 0. Absolute
outer constants preserve the indices; these are upper-envelope indices.


## 10. Dependencies

This proof restates every needed argument. The declared production dependencies
are ROB-G2, submission 55a6ce76-34af-468f-b735-a1197f3d3459 (uniform phase tests,
classical prefix words, coherent truncated phase accumulation and explicitly
counted constant-table lookup), and R24, submission
f892f7ea-957b-4dde-8374-dab2736231d0 (bounded cubic pair witness, coarse class grouping,
known-unitary answer copying/undo and same-bank endpoint trit threshold).
The model text is identical to both dependencies. No prior acceptance is
used as a mathematical premise.
