# PFD-N1: all-modulus full-secret decoding from n+1 source copies

## Joint theorem and fixed parameters

For every integer N>=2 and every fixed secret s in Z_N, put

    n=ceil(log2 N), m=n+1, K=2^m,
    q_lab=n+ceil(log2 m)+11,
    p=ceil(m/2)+26,
    A_rot=20(m+3)(q_lab+p+3)^2.

The single algorithm below acquires exactly m independent ideal DCP source
copies, with no retries or verification copies. It returns the entire s with
unconditional probability at least

    Cstar-1/128 > 43/64 > 2/3,
    Cstar=(1+sqrt(2)+4sqrt(3))^2/128.

Its every-branch joint resource bounds are

    T = O(2^(n/2) n^2 log(n+2)),
    S_C = O(n^2), S_Q = O(n), Q=n+1.

All constants are independent of N, s, the extracted labels and outcomes.
For n>=2 the supported time representative uses log2 n; the generic N=2
configuration has constant work and space. The growth indices are 1 for
time and 0 for both memories and samples. A guaranteed malformed fraction
of 0 is claimed. No positive tolerance or impossibility of tolerance is
asserted. Bad extraction outcomes are included in both success and cost.

The statistical lemma and two-reflection proposal were supplied in the
research handoff. PFD-15 supplies the preceding few-copy decoding context,
the arithmetic emitter and resource-controller construction. Sources are
identified in sources.md; no hosted judgment is a mathematical premise.

## 1. Raw-source decomposition and the plus-shift convention

Write omega=exp(2 pi i/N) and

    |chi_b> = N^(-1/2) sum_u omega^(b u)|u>,
    |p_a(s)> = (|0>+omega^(a s)|1>)/sqrt(2).

The supplied raw coset mixture is exactly

    rho_s = (1/N) sum_a |p_a(s)><p_a(s)| tensor |chi_-a><chi_-a|.

To verify this, its matrix element on (b,u),(c,v) is 1/(2N) precisely
when u-v=(b-c)s mod N, and zero otherwise, agreeing with the raw mixture.
This algorithm does not apply an initial X to the source phase qubit.
Independent sources give independent uniform latent a values. No
purification or source-preparation inverse is assumed available.

Let T_N:z->z+1 mod N on valid n-bit encodings, and the identity on encodings
>=N. Then T_N|chi_b>=omega^(-b)|chi_b>. On the raw data state chi_-a it
has eigenphase a/N, so source phase estimation reports a directly. A power
T_N^(2^r) is one modular addition of the known constant 2^r mod N, not 2^r
individual additions. This extension is a known permutation everywhere.

For grid M=2^q, use

    PE(U)=(F_M^dagger tensor I)(sum_j |j><j| tensor U^j)(H^q tensor I),
    F_M|j>=M^(-1/2) sum_l exp(2 pi i j l/M)|l>.

The binary QFT has O(q^2) controlled dyadic phases, Hadamards and swaps.
Use q=q_lab for source extraction. Measure j and set

    a_hat=floor(Nj/M+1/2) mod N,

with ties upward. Discard that source's data and estimation registers and
retain its phase qubit. Acquire exactly m sources on every branch.

### Phase-estimation tail

For eigenphase alpha, the probability at j is

    |M^(-1) sum_(r=0)^(M-1) exp(2 pi i r(alpha-j/M))|^2.

If d_j is the circular distance between alpha and j/M, then for d_j>0,
P(j)<=1/(4M^2 d_j^2), by |sin(pi x)|>=2|x| for |x|<=1/2. There are
at most four points in each unit-width bin of M d_j. Thus, for M e>=2,

    Pr[d_j>=e] <= 1/(floor(M e)-1).                           (1)

For rounding, e=1/(2N). Our M_lab>=2048mN gives a per-source error at
most 1/(1024m-1)<=1/(512m), hence a total extraction error <=1/512.
This is an unconditional coupling with the ideal independent labels.
Conditional on each latent label, extraction touches only its product
data register, so the associated phase qubit is untouched. We do not
condition on all estimates being correct and then assert uniformity.
Finite-gate synthesis is charged separately in Section 7.

## 2. The ideal full-secret fiber measurement

With known labels a=(a_1,...,a_m), define

    f_a(x)=sum_i a_i x_i mod N,
    eta_t=|{x in {0,1}^m : f_a(x)=t}|,
    |u_t>=eta_t^(-1/2) sum_(f_a(x)=t)|x> for eta_t>0.

The ideal phase input is K^(-1/2) sum_x omega^(s f_a(x))|x>.
Computing f into target T gives

    sum_(t:eta_t>0) sqrt(eta_t/K) omega^(s t)|u_t>|t>.

A common-positive-phase erasure u_t -> |+^m>, followed by H^m, would
leave the target state

    |zeta_a,s> = sum_t sqrt(eta_t/K) omega^(s t)|t>.

Its true-secret Fourier-basis probability is

    P_a(s)=(sum_t sqrt(eta_t))^2/(NK).                         (2)

This is independent of s and has no acceptance normalization. The
algorithm does not receive eta_t, a witness, or a fiber oracle; these
quantities define the proof, not extra inputs to the implementation.
The construction below implements the required erasure from f alone.

## 3. Ideal success margin with m=n+1

Separate the last uniform label A. Let xi be the histogram of the first n
labels and lambda=2^n/N in [1,2). Then eta_t=xi_t+xi_(t-A).
Introduce an independent uniform T and put X=xi_T, Y=xi_(T-A), S=X+Y.
Conditional on xi, the map (T,A)->(T,T-A) is a bijection of Z_N squared.
Hence X,Y are conditionally independent draws from the same histogram law.

For any distinct binary selectors, at least one difference coefficient is
+1 or -1. Their sums collide modulo N with probability 1/N, for any N.
The usual collision calculation for the first n labels therefore gives

    E X=lambda,
    E X^2=lambda^2+lambda-lambda/N,
    E XY=lambda^2,
    E S=2lambda,
    E S^2=4lambda^2+2lambda-2lambda/N.                         (3)

The XY identity follows from conditional independence and the deterministic
histogram mean lambda. It does not assume independent subset-sum collisions.
If q is the fraction of odd entries in a given xi, then

    Pr[S odd | xi]=2q(1-q)<=1/2.                              (4)

### Integer square-root minorant

Set a0=sqrt(2)-1/2, b0=(sqrt(2)-1)/4 and
c0=3(1+sqrt(2))/4-sqrt(3)>0. For every integer k>=0,

    sqrt(k)>=a0 k-b0 k^2-c0 1_(k odd).                        (5)

Indeed the gap before the parity correction factors exactly as

    sqrt(k)-a0 k+b0 k^2
      =b0 sqrt(k)(sqrt(k)-sqrt(2))(sqrt(k)-2)(sqrt(k)+2+sqrt(2)).

It is nonnegative outside 2<k<4. The sole violating integer is k=3,
where its value is -c0. This proves (5), including k=0. From (3)-(4),

    E sqrt(S)>=F(lambda),
    F(lambda)=((3sqrt(2)-1)/2)lambda
               -(sqrt(2)-1)lambda^2-c0/2.                    (6)

In fact the exact second moment adds the nonnegative term 2b0 lambda/N.
It is not needed for the uniform margin below.

### All-modulus interval split

Put Z(a)=N^(-1) sum_t sqrt(eta_t). Since K=2lambda N,

    E P_a = E Z(a)^2/(2lambda)
          >= (E Z(a))^2/(2lambda).                           (7)

Also E Z=E sqrt(S). Write A0=(3sqrt(2)-1)/2 and B0=sqrt(2)-1.
The derivative of F(lambda)/sqrt(2lambda) has the sign of

    A0 lambda-3B0 lambda^2+c0/2.

For 1<=lambda<=11/10 this is at least
lambda(14-9sqrt(2))/5+c0/2>0. Moreover

    F(1)=(1+sqrt(2)+4sqrt(3))/8>0.

Thus (6)-(7) give E P_a>=Cstar on this whole interval.
For lambda>=11/10, put Z2=sum_t eta_t^2. Holder gives
(sum sqrt(eta_t))^2>=K^3/Z2. Since E Z2=K+K(K-1)/N,

    E P_a >= K/(N+K-1)
           >= 2lambda/(1+2lambda) >= 11/16 > Cstar.           (8)

This covers every N, including odd and composite moduli. All bad and
unbalanced histograms remain in the expectations.

The constants admit elementary exact certificates. The lower bounds
sqrt(2)>141/100 and sqrt(3)>173/100 give

    Cstar>(933/100)^2/128=870489/1280000>87/128.

Expanding its numerator gives 51+2sqrt(2)+8sqrt(3)+8sqrt(6).
The upper bounds sqrt(2)<3/2, sqrt(3)<7/4, sqrt(6)<5/2 make this
strictly less than 88, proving Cstar<11/16. Positivity of c0 and the
derivative coefficient follows directly by squaring positive rationals.
No floating-point estimate is a premise. Numerically Cstar is about
0.681880871309, but only the exact inequalities are used in the claims.

## 4. Two known reflections and their occupied-span sign

Define Rplus=2|+^m><+^m|-I, Rt=2Pi_t-I, where Pi_t marks f_a(x)=t,
and H_t=(Rplus+Rt)/2. For 0<eta_t<K, let alpha=sqrt(eta_t/K),
beta=sqrt(1-alpha^2), and v_t be the uniform complement of u_t.
In the basis (u_t,v_t),

    H_t=alpha [[alpha,beta],[beta,-alpha]].

It has eigenvalues +alpha and -alpha, and

    sign(H_t) u_t=alpha u_t+beta v_t=|+^m>.                   (9)

The phase is the same positive phase for every target. For a full fiber,
u_t=|+^m> is the +1 eigenvector, and (9) holds directly. Empty fibers have
zero amplitude. A gap on the entire selector Hilbert space is neither
needed nor claimed: zero eigenvalues can occur outside this occupied span.

Let D_t=(Rplus-Rt)/2. With one block ancilla, form

    B_t=H_anc SELECT(Rplus,Rt) H_anc
       =[[H_t,D_t],[D_t,H_t]],
    W_t=Z_anc B_t.

The identities H_t^2+D_t^2=I and H_t D_t=-D_t H_t imply B_t^2=I.
For an H_t eigenvector v of eigenvalue mu with |mu|<1, the vectors

    |0>v,  |1>D_t v/sqrt(1-mu^2)

form an orthonormal invariant plane of W_t. Its matrix is

    [[mu,sqrt(1-mu^2)],[-sqrt(1-mu^2),mu]].

The walk eigenphases are +/-arccos(mu). Applying sign(cos(theta)) gives
the same sign(mu) on both eigenvectors, hence returns the block ancilla
to zero and implements sign(H_t) on |0>v. The endpoint mu=+/-1 follows
directly with D_t v=0. Target T remains coherent throughout, so distinct
target blocks stay orthogonal.

## 5. Coherent phase-estimation/sign/inverse circuit

Use p=ceil(m/2)+26 phase bits, M_walk=2^p. Perform PE(W_T), apply

    D_sign|j>=+|j> for j<M_walk/4 or j>=3M_walk/4,
                 -|j> otherwise,

then the actual inverse PE circuit. The PE register is not measured.
D_sign is exactly Z on each of its two highest bits. The half-open
boundary convention is fixed even on irrelevant zero-eigenvalue blocks.

On every relevant occupied eigenvector, |mu|=alpha>=K^(-1/2).
Its circular eigenphase distance from either sign boundary is at least

    arcsin(alpha)/(2pi) >= 1/(8sqrt(K)) = e.

The estimates use arcsin(x)>=x and pi<4. If a grid estimate has the wrong
sign, its circular error is at least e. Since M_walk e>=2^23, (1) gives

    wrong-sign probability <=1/(2^23-1).

For a walk eigenvector, unitary PE uncomputation shows that the squared
vector error is exactly the PE average of |D_sign(j)-sign(mu)|^2. Hence

    error^2 <=4/(2^23-1)<1/512^2.                             (10)

Different walk eigenvectors have orthogonal errors; the retained target
keeps different fibers orthogonal as well. The same norm bound holds on
their superpositions, including references attached to the stated span.
Apply selector Hadamards after the eraser. The whole state is within norm
1/512 of |0>_selector,block,PE tensor |zeta_a,s>. Residual registers may
then be discarded with this unconditional error charged.

The schedule uses exactly 2(M_walk-1) controlled W or W^dagger calls.
Each W^(2^r) is implemented by that many repetitions. No fast-forwarding
or unit-cost high power is assumed. The loop counter has O(n) bits.

### Controlled reflection phases and literal emitter

The inherited marker implements I-2Pi_t. Rt is its negative. The emitter
therefore applies Z on the selected control as well as that marker.
Likewise, controlled Rplus includes the sign of 2|+><+|-I.
Dropping either selected phase changes the walk and is incorrect.

`walk.py` computes a clean selected-control flag from the outer PE control
and the block bit. It applies the appropriate reflection and clears that
flag. The block Hadamards surrounding controlled SELECT can be unconditional:
when the outer control is zero they cancel. A controlled Z on the block
implements the final Z_anc. The inverse emitter reverses the reflection
order and its small phase/arithmetic templates. No controlled arbitrary
Hadamard synthesis is used. All these calls are exact Clifford+T.

## 6. Final arbitrary-modulus Fourier measurement

Reuse q_lab-bit phase estimation of the same plus shift T_N on target T.
If its ideal Fourier component is chi_s, the phase is -s/N. Therefore
output

    s_hat=-floor(Nj/M_lab+1/2) mod N.                         (11)

The sign negation is essential. For each Fourier eigenstate the rounding
error is at most 1/(1024m-1)<=1/512. For an arbitrary target density
operator, tracing out the target makes the outcome law a classical mixture
of its Fourier components. Thus the same error bound compares this readout
with ideal Fourier-basis measurement for the actual target state. This
does not assume a free arbitrary-modulus QFT unitary.

## 7. Finite gates and complete success budget

Arithmetic, comparisons, selected reflections, controlled walks and D_sign
are exact Clifford+T. Only the polynomially many outer binary-QFT rotations
need approximation. There are m source QFTs, two walk QFTs and one readout
QFT. Ordinary controlled-phase decomposition uses at most three
unconditional one-qubit phase rotations per controlled phase. In particular
their number is below A_rot=20(m+3)(q_lab+p+3)^2.

Use a uniform finite-gate compiler to approximate each such one-qubit
rotation to norm error <=1/(512 A_rot), up to a global phase. Use its actual
reversed adjoint word in inverse circuits. After controlled-phase
decomposition, these approximate words are unconditional. Their phases
therefore combine into one global circuit phase, never a target-dependent
or selected-branch phase. The repeated controlled walks themselves are exact.

The imported compiler hypothesis is the standard constructive
Solovay-Kitaev algorithm for a fixed inverse-closed universal one-qubit
library, with polynomial work, output length and workspace in the required
precision bits. The coarse fixed net is constructed and charged, not
instance-dependent advice. Its output emission and classical arithmetic
are counted. The reference and scope are stated in sources.md.

All requested precision bits are O(log(n+2)). Phase angles with longer
symbolic dyadic denominators can be computed or truncated to that absolute
accuracy with charged polynomial work. The fixed n-dependent sequence has
polynomially many approximate rotations. A hybrid argument bounds the whole
synthesis error by 1/512. Approximation never occurs inside the exponentially
repeated walk loop.

The four unconditional outcome-error allowances are:

    source extraction        1/512,
    coherent sign erasure    1/512,
    all finite-gate synthesis 1/512,
    final label rounding     1/512.

For normalized pure vectors, Euclidean distance bounds trace distance;
mixtures and subsequent channels cannot increase it. Thus the norm errors
above bound each event-probability change without an additional factor two.
The coupling error for bad source estimates and the final rounding error
are also unconditional. Combining with Section 3,

    Pr[s_hat=s]>=Cstar-1/128>43/64>2/3.                       (12)

There is no division by a heralded probability. Generic N=2 is included:
m=2, q_lab=13 and p=27. Its ideal ensemble success is 7/8, since the
all-zero label list has success 1/2 and the other three lists have success
1. The same global budget suffices. No three-copy exception is used.

## 8. Joint uniform resource ledger

The known controlled permutation u->u+c mod N for u<N, identity otherwise,
has an O(n)-gate, O(n)-scratch realization. The emitter computes an
(n+1)-bit ripple sum, compares/subtracts N, tests the input range, selects
the result, and clears its Boolean history. Compute/copy/uncompute, SWAP,
and a known inverse-constant evaluation clear the old input. It works on
every binary encoding. `arithmetic.py` is reused from PFD-15.

Compute f using m controlled additions, clearing each addition's scratch
before the next. To mark a fiber, compute f, compare to the retained target,
apply its controlled phase, and reverse the computation. This costs O(mn)
gates and O(m+n) live qubits. It does not retain m arithmetic histories.
Known-uniform reflections use Hadamards and a clean AND chain in O(m)
gates and scratch. The selected-control and block operations add constant
work to a call. Consequently each controlled W or its inverse uses O(mn)
exact gates and O(m+n) quantum workspace.

Since m=n+1 and p=ceil(m/2)+26, there are O(2^(n/2)) walk calls. Their
large precision-dependent leading constant is fixed, not a practical
runtime claim. A classical controller retains N, the mn label bits and
inverse constants, counters and a streamed descriptor, using O(n^2) bits.
The total allocated memory is polynomial in n, so every indexed classical
access and addressed quantum gate pays O(log(n+2)) bit work.

The controller maintains short wire-index fields on sequential work tapes.
Updating offsets or emitting an address uses O(log(n+2)) local bit steps;
it is not implemented by a fresh indexed lookup for each bit of its own
address. Genuine indexed coefficient accesses and quantum gates still pay
their address debit. A fixed template needs a constant number of such
accesses per gate. Coefficients are read as binary fields, inverse constants
are prepared once, and row bases are advanced by adding n between rows.
No arbitrary long shift, division or multiplication is charged as unit work
inside the repeated loop. This is the explicit controller/accounting method
used in PFD-15 and its cited saved-copy predecessor.

Only an O(n)-gate arithmetic or zero-phase template is materialized at one
time, costing O(n log(n+2)) classical bits within O(n^2). The full walk,
its powers and its exponential repetition stream are not stored. The inverse
walk is generated by reversing macro order and the bounded templates.
Thus gate generation and all address work give

    O(2^(n/2) mn log(n+2))=O(2^(n/2)n^2 log(n+2)).             (13)

Source and readout shifts use known constant powers with polynomial total
work. QFT construction, classical rounding, allocation, initialization,
measurements, resets, discards and uniform synthesis have polynomial total
work, absorbed in (13). Their live compiler scratch is polynomial in
log(n+2), hence within O(n^2), and their registers are reused or discarded
between phases. Source extraction holds only the current n-bit data
register and its O(n)-bit PE register in addition to the retained phase
qubits. The core holds those m phase qubits, one n-bit target, one block
qubit, O(n) phase-estimation bits and O(n) reusable arithmetic scratch.
Peak accessible quantum storage is therefore O(n).

Exactly m=n+1 original source copies are acquired, regardless of label
outcomes or final correctness. No source operation is called by the eraser.
All schedules are fixed and bounded on bad-label branches as well. The
declared classical memory, quantum memory, source count and time apply
jointly to this one configuration.

For n>=2, log(n+2)=Theta(log2 n), giving the supported structured time
envelope. Its growth index is 1, since its exponent contains n/2, not
sqrt(n). The three polynomial resource envelopes have growth index 0.
At N=2 every register and loop has a fixed finite size; this preserves all
big-O statements despite the log2 n representative vanishing at n=1.

## 9. Scope, exact cap and diagnostics

At N=2^n, m copies lie in a 2^m-dimensional phase space conditional on the
secret-independent orthogonal Fourier-label block. For any N-outcome POVM,
its average true-secret probability is <=2^m/N by the trace bound. If m<n,
this is <=1/2. Thus n+1 is one copy above this necessary dimension bound,
not a proof of exact sample optimality. The source itself supplies n+1
accessible qubits, making linear quantum space optimal in order under this
accounting. No classical-space lower bound is claimed.

Compared with PFD-15, the exact cap falls from n+2 to n+1. The supported
asymptotic time/space/sample envelopes and index vector are tied, and this
configuration has a smaller success margin and conservative precision
constants. It is not an asymptotic frontier improvement or a reduction of
the time index. The improvement uses the stronger full-secret measurement
bound, not the alternating-path recycling wrapper.

The source guarantee requires every acquired copy to be an independent ideal
coset state. The guaranteed malformed fraction is 0. The finite diagnostics
check exact arithmetic and controlled walk columns, coherence and sign
conventions, complete small label ensembles, and numerical small-grid
PE/sign/readout sequences. They do not execute the enormous production grid
or a quantum device, and numerical extrapolation is not a proof premise.
The uniform synthesis algorithm is a cited constructive hypothesis; the
diagnostic uses ideal rotations on small grids rather than a numerical SK
compiler. No hosted judgment or finite experiment certifies the theorem.
